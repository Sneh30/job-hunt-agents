# Agent 2 — recruiter research and Gmail drafts

A bounded daily agent that finds companies worth applying to, identifies the right people,
verifies their email addresses, and leaves one personalized Gmail draft per recruiter waiting
for review.

It **never sends**. It **never uses the Gmail API**. It works only through the visible Gmail web
UI, and only inside a single manually started run.

## Daily use

1. Initialize once:

   ```bash
   python3 scripts/initialize_project.py
   ```

   This creates `config/settings.json`, `config/state.json`, and the `runs/` and `logs/`
   directories. It never overwrites existing files and never creates a scheduler.

2. Add your resume sources to `resume/` (see the README there) and edit `config/settings.json`
   with your paths, links, and targets.

3. Open the project in a coding-agent CLI and paste the full contents of `RUN_PROMPT.md`.

4. If Gmail is signed out, sign in yourself in the browser. The agent must never ask for or
   type a password, MFA code, recovery code, cookie, or session token.

5. Proofread each draft in its own tab and click **Send** yourself.

There is no scheduler, by design. One prompt, one run.

## What a run produces

- A dated run directory with the clean daily contact workbook
- A per-contact evidence file separating *found*, *verified*, and *drafted*
- One Gmail draft per verified recruiter, in its own browser tab
- An updated master tracker with deduplication across runs
- A closing report with exact counts and any shortfall

The clean daily workbook has exactly four columns: `name`, `company`, `mail`, `linkdin`. Every
row must be complete, unique, and contain a verified address.

## Hard requirements

| Requirement | Why |
|---|---|
| Gmail web UI only | Keeps the agent inside the same surface a human uses; no OAuth mail scopes |
| Verified emails only | No guessed patterns, inferred addresses, or masked-address reconstruction |
| One draft per tab | Human review stays practical |
| No sending, ever | The irreversible action stays with the human |
| Approval before paid enrichment | Credit-consuming lookups are quoted first |
| No scheduler | The agent cannot run unattended |
| Resume review before attachment | No false "attached" claims, no unreviewed PDFs |
| Separate discovery / verification / draft state | A found email is not a contacted person |

## Repository contents

```text
RUN_PROMPT.md                  the prompt pasted each day
PROJECT_SPEC.md                full behavior spec and safety constraints
config/settings.example.json   settings template (no secrets)
resume/README.md               where your resume sources go
scripts/initialize_project.py  idempotent skeleton initializer
scripts/validate_workbook.py   stdlib-only XLSX structure/content validator
templates/email_template.md    cold-email base with placeholders
logs/README.md                 logging rules
```

`master_recruiter_tracker.xlsx`, run outputs, and logs are created locally and are intentionally
not committed — they contain third-party contact data.

## Validator

```bash
python3 scripts/validate_workbook.py --help
```

The validator checks workbook structure, sheet names, headers, email syntax, duplicates, and
placeholder leakage without installing anything.

## Notes on publication

The spec and prompt are the real ones, sanitized: contact details and home-directory paths are
replaced with placeholders. No recruiter data, tracker workbook, or run output is included.
