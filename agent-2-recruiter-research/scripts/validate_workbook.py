#!/usr/bin/env python3
"""Validate the structure and content of recruiter Excel workbooks using only Python's stdlib."""
import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from posixpath import normpath

NS = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pkgrel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
EMAIL_RE = re.compile(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", re.I)
DAILY_HEADERS = ["name", "company", "mail", "linkdin"]
MASTER_HEADERS = {
    "Companies": ["company", "official_domain", "eligible_locations", "target_role_families",
                  "current_hiring_signal", "source_url", "first_researched_at", "last_researched_at",
                  "run_ids", "notes"],
    "Contacts": ["contact_id", "full_name", "company", "company_domain", "title", "India_location",
                 "professional_email", "email_evidence_type", "email_verification_status", "LinkedIn_URL",
                 "source_URLs", "role_relevance", "first_discovered_at", "last_verified_at",
                 "first_run_id", "last_run_id", "outreach_status", "do_not_contact", "duplicate_key", "notes"],
    "Outreach": ["contact_id", "recipient_email", "subject", "Gmail_UI_status", "draft_created_at",
                 "sent_confirmed_at", "replied_at", "bounced_at", "status_evidence", "last_checked_at", "run_id"],
    "Source Evidence": ["evidence_id", "contact_id_or_company", "source_title", "source_URL", "source_type",
                        "accessed_at", "exact_email_visible", "identity_supported", "current_employer_supported",
                        "role_relevance_supported", "email_status_claim", "evidence_notes"],
    "Run Log": ["run_id", "started_at", "finished_at", "outcome", "companies_selected",
                "contacts_researched", "emails_passed_verification", "draft_tabs_saved",
                "sent_messages_detected", "duplicates_skipped", "errors", "shortfall_reason", "daily_output_path"],
}

def col_index(cell_ref):
    letters = re.match(r"([A-Z]+)", cell_ref or "")
    n = 0
    for char in letters.group(1) if letters else "":
        n = n * 26 + ord(char) - ord("A") + 1
    return n - 1

def read_xlsx(path):
    with zipfile.ZipFile(path) as z:
        wb_root = ET.fromstring(z.read("xl/workbook.xml"))
        rels_root = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        rel_map = {r.attrib["Id"]: r.attrib["Target"] for r in rels_root.findall("pkgrel:Relationship", NS)}
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            ss_root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in ss_root.findall("main:si", NS):
                shared.append("".join(t.text or "" for t in si.findall(".//main:t", NS)))
        result = {}
        for sheet in wb_root.findall("main:sheets/main:sheet", NS):
            name = sheet.attrib["name"]
            rel_id = sheet.attrib.get(f"{{{NS['rel']}}}id")
            target = rel_map.get(rel_id, "")
            target = target.lstrip("/")
            sheet_path = normpath(target if target.startswith("xl/") else "xl/" + target)
            root = ET.fromstring(z.read(sheet_path))
            rows = []
            for row_elem in root.findall(".//main:sheetData/main:row", NS):
                cells = {}
                for cell in row_elem.findall("main:c", NS):
                    idx = col_index(cell.attrib.get("r"))
                    typ = cell.attrib.get("t")
                    if typ == "inlineStr":
                        value = "".join(t.text or "" for t in cell.findall(".//main:t", NS))
                    else:
                        v = cell.find("main:v", NS)
                        raw = v.text if v is not None else ""
                        if typ == "s" and raw != "":
                            value = shared[int(raw)]
                        else:
                            value = raw
                    cells[idx] = value
                width = max(cells.keys(), default=-1) + 1
                rows.append([cells.get(i, "") for i in range(width)])
            result[name] = rows
        return result

def norm_row(row):
    return [str(x).strip() if x is not None else "" for x in row]

def validate_daily(sheets):
    errors = []
    if "Contacts" in sheets:
        rows = sheets["Contacts"]
    elif sheets:
        rows = next(iter(sheets.values()))
    else:
        return ["Workbook contains no worksheets."]
    if not rows:
        return ["Daily contacts worksheet is empty."]
    headers = norm_row(rows[0])
    if headers != DAILY_HEADERS:
        errors.append(f"Expected exact headers {DAILY_HEADERS}; found {headers}.")
        return errors
    seen_emails, seen_li, seen_name_company = set(), set(), set()
    included = 0
    for excel_row, raw in enumerate(rows[1:], start=2):
        row = norm_row(raw)
        if not any(row):
            continue
        # Always check all expected columns, including missing trailing columns.
        row = (row + [""] * 4)[:4]
        name, company, email, linkedin = row
        if not all(row):
            errors.append(f"Row {excel_row}: missing required field(s).")
            continue
        if not EMAIL_RE.fullmatch(email):
            errors.append(f"Row {excel_row}: mail cell is not a single plain email address.")
        if email.lower() in seen_emails:
            errors.append(f"Row {excel_row}: duplicate email address {email}.")
        if linkedin.rstrip("/").lower() in seen_li:
            errors.append(f"Row {excel_row}: duplicate LinkedIn URL.")
        key = (re.sub(r"\s+", " ", name).lower(), company.lower())
        if key in seen_name_company:
            errors.append(f"Row {excel_row}: duplicate normalized name + company.")
        seen_emails.add(email.lower())
        seen_li.add(linkedin.rstrip("/").lower())
        seen_name_company.add(key)
        included += 1
    print(f"Daily workbook: {included} contact row(s) checked.")
    return errors

def validate_master(sheets):
    errors = []
    for name, expected in MASTER_HEADERS.items():
        if name not in sheets:
            errors.append(f"Master workbook missing worksheet: {name}.")
            continue
        rows = sheets[name]
        headers = norm_row(rows[0]) if rows else []
        if headers != expected:
            errors.append(f"Worksheet {name}: expected headers {expected}; found {headers}.")
    print(f"Master workbook: {len(sheets)} worksheet(s) found.")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--kind", choices=["auto", "daily", "master"], default="auto")
    args = parser.parse_args()
    if not args.workbook.is_file():
        print(f"ERROR: file does not exist: {args.workbook}", file=sys.stderr)
        return 2
    try:
        sheets = read_xlsx(args.workbook)
    except Exception as exc:
        print(f"ERROR: workbook cannot be read: {exc}", file=sys.stderr)
        return 2
    kind = args.kind
    if kind == "auto":
        kind = "master" if all(name in sheets for name in MASTER_HEADERS) else "daily"
    errors = validate_master(sheets) if kind == "master" else validate_daily(sheets)
    if errors:
        print("VALIDATION FAILED:")
        for err in errors:
            print(f"- {err}")
        return 1
    print("VALIDATION PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
