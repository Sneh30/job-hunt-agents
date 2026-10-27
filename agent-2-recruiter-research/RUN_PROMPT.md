# Daily run — paste this into Codex CLI

Read `PROJECT_SPEC.md`, `README.md`, `config/settings.json`, `config/state.json`, the full `resume/` folder, and the existing `master_recruiter_tracker.xlsx`. Then execute **one complete daily run now**.

This is a manually initiated run. I am the scheduler: **do not create, configure, or modify cron, launchd, Task Scheduler, recurring jobs, automations, or any other scheduler.** Do not stop at describing a plan. Carry out the research and workflow as far as the available tools and permissions permit.

Use my resume as the source of truth. Dynamically discover the best companies to apply to from current live openings and resume fit; do not use a fixed or preselected company list. Include suitable fresher/2027-graduate opportunities from ordinary Software Developer/SDE/backend roles through AI/agent systems, infrastructure/platform/SRE, automation, and embedded/systems engineering. Also consider paid internships, graduate programs, paid apprenticeships, and international positions only where Indian candidates are eligible and relocation/visa support is explicitly stated if needed.

Target 10 dynamically selected companies and 20 distinct India-relevant recruiter contacts (aim for 2 per company). Use only strictly verified professional emails; no guessing, no inferred address patterns, no masked-address reconstruction, and no placeholders. Use only Apollo features available under my current plan. Before any credit-consuming operation, tell me the total contacts and maximum credits and wait for my explicit approval; if unattended/approval unavailable, skip that operation and continue with other sources.

Maintain the master Excel tracker and all evidence, per-run outputs, and logs under this project directory. Deduplicate contacts across previous runs. Track discoveries, verified emails, Gmail drafts, and actually sent messages as separate states. Never classify a person as contacted just because their email was found or a draft was created.

Gmail requirements:
- Use **only the visible Gmail website UI** at `https://mail.google.com/` for all Gmail access and drafting. Do not use Gmail APIs, OAuth mail APIs, Apps Script, IMAP, SMTP, connectors, hidden endpoints, or direct data access.
- On first boot, open Gmail in the browser and ask me to sign in directly. Never ask for or type my password, MFA code, recovery code, cookies, or session secrets. Pause Gmail work until I confirm login.
- If browser UI control is unavailable, stop the Gmail stage and state the exact blocker. Do not substitute an API.
- Create one personalized email draft per qualified recruiter, **each in its own separate browser tab**. Save and verify each draft in the Gmail UI. Leave the tabs open for me to proofread.
- Never click Send, Schedule Send, bulk send, or any equivalent. I will proofread and click Send myself.
- Use the LaTeX resume provided in `resume/`. If a suitable PDF is missing, compile it only if local tools permit; do not attach until I have reviewed and approved the PDF. If approval has not happened, leave the resume unattached and do not falsely say it is attached.
- Do not overwrite or delete existing Gmail drafts. Check for duplicates and skip them.
- Draft only verified contacts. If fewer than 20 qualify, create drafts for the verified contacts found and report the shortfall. Do not pad the target.
- Detect messages that I manually sent only from Gmail's Sent folder UI, or from my explicit confirmation.

At completion, validate all output files, update the tracker and run logs, and report exact counts for companies researched, contacts found, strictly verified emails, drafts visibly saved, sent messages detected, and any shortfall or blocker. The per-run `verified_contacts.xlsx` must contain exactly `name`, `company`, `mail`, `linkdin`; every included row must be complete, unique, and contain only a verified email address in `mail`. Do not claim success for work not actually completed.

Start by checking the local directory/environment and continuing from existing state without destroying history.
