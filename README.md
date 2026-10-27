# job-hunt-agents

Two prompt-driven agents that run a job search end to end — except for the last click.

They research companies, verify recruiters, write drafts, and fill application forms. A human
reviews the work and presses **Send** or **Submit**. That boundary is enforced by the prompts,
not by convention.

| Agent | What it does | Final action |
|---|---|---|
| [`agent-2-recruiter-research`](agent-2-recruiter-research/) | Discovers companies from live openings, finds and verifies recruiter emails, dedupes contacts, writes one personalized Gmail draft per recruiter | You send |
| [`agent-1-application-pipeline`](agent-1-application-pipeline/) | Picks fresh roles, tailors a resume per role, fills every application field, leaves each form staged at the submit button, logs the run | You submit |

## Why this exists

Job hunting is a high-volume, low-signal pipeline: hundreds of postings, a handful of real
matches, and a lot of repetitive form filling. Automating the volume is easy. Automating it
without fabricating claims, spamming people, or submitting something you have not read is the
interesting part.

These agents are built around three rules:

1. **Never take the irreversible action.** No auto-send, no auto-submit, no scheduler.
2. **Evidence over inference.** Recruiter addresses must come from a verifiable source. No
   guessed patterns, no reconstructed addresses, no placeholders.
3. **State lives in plain files.** Excel workbooks, JSON, and Markdown. Every decision is
   inspectable after the run.

## How it works

### Agent 1 — daily application pipeline

A long, self-contained prompt pasted into a coding-agent CLI once per day. The agent reads an
application log, applies a 30-day company cooldown, researches live roles, builds a tailored
LaTeX resume per role, fills the application form field by field, and stops at the submit
button. It appends to the log and writes a daily journal.

The resume engine is [career-ops](https://github.com/career-ops-hq/career-ops), which is **not
vendored here**. You bring your own checkout and your own source-of-truth CV.

### Agent 2 — recruiter research and Gmail drafts

A bounded daily run with a written spec and two dependency-free Python helpers:

- `scripts/initialize_project.py` creates the project skeleton idempotently and refuses to
  overwrite existing state.
- `scripts/validate_workbook.py` validates the generated `.xlsx` workbook structure and cell
  content using only the standard library.

The run discovers companies dynamically, verifies contacts, and creates one Gmail draft per
recruiter **through the visible Gmail web UI**. It is explicitly forbidden from using the Gmail
API, SMTP, IMAP, or hidden endpoints, and from sending anything.

## Repository layout

```text
agent-1-application-pipeline/
  README.md                     design notes and daily loop
  DAILY-PIPELINE-PROMPT.md      the full run prompt, sanitized for publication
agent-2-recruiter-research/
  README.md                     setup and daily use
  PROJECT_SPEC.md               end-to-end behavior and hard safety requirements
  RUN_PROMPT.md                 the prompt pasted each day
  config/settings.example.json  non-secret settings template
  resume/README.md              where your own resume sources go
  scripts/                      initializer and workbook validator
  templates/email_template.md   cold-email base with placeholders
  logs/README.md                logging rules
```

## Safety model

- **No credentials in the repo.** API keys and OAuth tokens are read from the environment or a
  local, git-ignored file. `.env` is never committed.
- **Gmail stays in the browser.** The agent may drive the visible UI; it may not touch mail
  APIs. It must not ask for passwords, MFA codes, recovery codes, cookies, or session tokens.
- **Credit-spending enrichment is gated.** The agent reports the maximum credit cost and waits
  for explicit approval before any paid lookup.
- **No schedulers.** No cron, launchd, or Task Scheduler entries are created. The human is the
  scheduler.
- **No fabricated experience.** Resume claims come from one source-of-truth file. Missing
  skills are logged as gaps, never invented.
- **Attachments require review.** A resume PDF is attached only after the human has reviewed it.

## Setup

Agent 2 is runnable from this repo:

```bash
python3 agent-2-recruiter-research/scripts/initialize_project.py
```

That creates `config/settings.json`, `config/state.json`, and the run/log directories without
overwriting anything. Then:

1. Add your own `resume/resume.tex` and `resume/resume_profile.md`.
2. Copy `config/settings.example.json` to `config/settings.json` and set your paths and targets.
3. Open the project in your agent CLI and paste `RUN_PROMPT.md`.

Agent 1 additionally requires a local [career-ops](https://github.com/career-ops-hq/career-ops)
checkout and your own application log; see its README.

## What is deliberately not in this repo

- Resumes, cover letters, and application logs
- Recruiter contact exports and tracker workbooks
- Per-run outputs, screenshots, and logs
- `.env` files, API keys, and tokens
- Vendored copies of third-party projects

Those contain personal data or third-party contact data, so they stay local. This repository is
the reusable machinery, not the search itself.

## Credits

- [career-ops](https://github.com/career-ops-hq/career-ops) — open-source job-search engine used
  by Agent 1.
- [PWP_jobhunt](https://github.com/perryvegehan/PWP_jobhunt) — a related open-source job-search
  agent that fetches from ATS APIs, filters, ranks, and emails a digest.

Both retain their own licenses. No third-party code is redistributed here.
