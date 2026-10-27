# Agent 1 — daily application pipeline

A prompt-driven agent that turns a morning session into a batch of fully completed job
applications — staged, never submitted.

It runs on top of [career-ops](https://github.com/career-ops-hq/career-ops), an open-source
resume and evaluation engine. That checkout is **not** included in this repository.

## The daily loop

1. Paste `DAILY-PIPELINE-PROMPT.md` into a coding-agent CLI.
2. The agent reads the application log and skips anything inside the 30-day company cooldown.
3. It researches live roles that match the target role families and location constraints.
4. For each role it tailors a resume from the source-of-truth CV, compiles it, and verifies the
   PDF and ATS score before using it.
5. It fills every field it truthfully can, leaves the form open at the submit button, and
   records the staged application in the log.
6. The human reviews the open tabs, submits what looks right, and marks the outcome.

The agent never clicks **Submit**, **Send**, **Apply**, or **Accept**.

## Design notes

### The log is the source of truth

The Excel workbook drives cooldowns, deduplication, and rejection history. The agent reads it at
the start of every run and appends at the end. Columns the human owns — status and response —
are never rewritten.

### Resume variants, not one resume

Each role gets a variant built from a canonical CV. A variant is rebuilt whenever the source CV
changes, so a stale resume can never be uploaded. The build is verified (PDF exists, text
extracts, ATS keywords match) before the file is attached.

### Honest gaps

If a role asks for a skill the candidate does not have, the agent still applies — but it records
the gap in a learning log instead of inventing experience. It may frame a truthful near-match;
it may not claim the skill.

### Human voice

Free-text answers must read like the candidate wrote them: first person, concrete, varied
sentence length. Banned openers like "I am excited to…" and "I am passionate about…" are
explicitly called out in the prompt.

## What the prompt enforces

- No submission, ever
- 30-day company cooldown and exact-role deduplication
- Every claim traceable to the CV or the story bank
- No invented skills, metrics, or eligibility
- All created files stay under the project directory
- A closing report with counts, blockers, and fields left for the human

## Requirements

- A coding-agent CLI with file and browser control
- A [career-ops](https://github.com/career-ops-hq/career-ops) checkout
- A source-of-truth CV and story bank
- An application log workbook
- LaTeX for resume compilation, Node.js for the ATS scoring tools

## Notes on publication

`DAILY-PIPELINE-PROMPT.md` is the real run prompt, sanitized: contact details, home-directory
paths, and personal file names are replaced with placeholders. The workflow, guardrails, and
form-handling rules are unchanged. Application logs and generated resumes are not published.
