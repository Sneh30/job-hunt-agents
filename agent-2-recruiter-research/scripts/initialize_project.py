#!/usr/bin/env python3
"""Idempotent safe directory initializer. Does not schedule recurring tasks."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRS = ["config", "resume", "scripts", "runs", "logs", "templates"]

def main():
    for folder in REQUIRED_DIRS:
        (ROOT / folder).mkdir(parents=True, exist_ok=True)
    settings = ROOT / "config" / "settings.json"
    state = ROOT / "config" / "state.json"
    if not settings.exists():
        settings.write_text(json.dumps({
            "project_root": str(ROOT),
            "target_companies_per_run": 10,
            "target_recruiters_per_run": 20,
            "gmail_ui_only": True,
            "never_send_automatically": True,
            "create_scheduler": False,
            "daily_output_columns": ["name", "company", "mail", "linkdin"]
        }, indent=2), encoding="utf-8")
    if not state.exists():
        state.write_text(json.dumps({
            "initialized": False,
            "gmail_login_verified": False,
            "resume_pdf_review_approved": False,
            "last_run_id": None,
            "last_run_date": None
        }, indent=2), encoding="utf-8")
    print(f"Project directories checked: {ROOT}")
    print("Existing files and master history were not overwritten.")
    print("No scheduler was created or configured.")

if __name__ == "__main__":
    main()
