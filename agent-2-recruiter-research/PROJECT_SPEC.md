# Project specification — Daily Recruiter Research + Gmail Drafting

## Goal and run model

This is a locally stored Opencode CLI project. The user manually pastes `RUN_PROMPT.md` into Codex CLI once per day. Each invocation runs exactly one cycle and exits. The user is the scheduler. Never create, configure, recommend implementing inside this project, or run cron/launchd/Task Scheduler/recurring automation.

Project root on the user's Mac:
`<PROJECT_ROOT>`

This distributed starter project is copied into that path by the user. Do not claim it has already been installed on the Mac. On first execution, inspect and initialize the local project idempotently.

## Candidate facts — source of truth

Read `resume/resume.tex` and `resume/resume_profile.md`. Do not invent or inflate facts. If a fact conflicts with later user-provided resume updates, ask or use the latest user-approved file as source of truth.

Candidate:
- Name: Sneh Raj Sinha
- Email: {{EMAIL}}
- Phone: {{PHONE}}
- LinkedIn: https://www.linkedin.com/in/sneh30/
- GitHub: https://github.com/Sneh30
- Portfolio: https://sneh30.github.io/portfolio/
- Education: B.E. Robotics and Artificial Intelligence, Bangalore Institute of Technology, Bengaluru, Karnataka; GPA 8.0/10; August 2023–August 2027. Treat as graduating in 2027; check specific eligibility.
- Summary positioning: AI systems engineer and Electronics & Software Lead; end-to-end projects with cost and systems efficiency; projects include PromptOS, DeepOps, Orchestra, ESP32-CAM Vision Suite; software/electronics leadership for a 50-member competition vehicle/team; embedded systems constraints.
- Technical skills as declared in resume: Python, Java, SQL; LangGraph, OpenAI Codex, Claude Code, OpenCode, OpenClaw, Hermes, Antigravity, OpenRouter, Ollama, llama.cpp; Hugging Face Transformers, LLM inference, RAG, LangChain, tool/function calling, agentic AI, prompt engineering, embeddings, vector databases, multi-agent systems, edge AI; FastAPI, PostgreSQL, Prometheus, REST APIs, AWS, observability, incident response; Docker, Docker Compose, Git, GitHub Actions, CI/CD, Linux, macOS, WASM, Metal/GPU; ESP32, Raspberry Pi, Edge Impulse.
- Experience:
  1. Infrastructure Engineer, independent engagement, Aug 2026, one-month on-site work for a 400+ node exam-facility network; reported reduction of incidents and average recovery time by ~40% versus prior comparable period.
  2. Software & Electronics Lead, Team Stratos, Jul 2025–May 2026; led software/electronics integration for a 50-member competition-vehicle team; developed/deployed ABS firmware; safety-critical subsystem validated through track testing, SAE India scrutineering, and competition.
- Projects:
  - Orchestra: multi-agent research orchestrator with LangGraph, FastAPI, PostgreSQL, Prometheus; deterministic CI mode; Docker Compose.
  - DeepOps: autonomous SRE platform; natural-language incidents, root-cause analysis and remediation plans, cost-optimization logic; pipeline core completed and being integrated/tested for end-to-end automated resolution.
  - PromptOS: Rust prompt compiler with custom lexer/parser/AST and ten optimization passes/four compilation modes; reported 80–85% inference-cost reduction in Economy mode; macOS app, Swift UI, llama.cpp, WASM, Metal.
  - ESP32-CAM Vision Suite: embedded computer vision using HSV quantization and centroid tracking; RGB565→RGB888→HSV conversion, L298N motor control, image collection/MJPEG server; 15+ camera-board variants.
- Open source: merged bug-fix/documentation PRs in agentrhq/webcmd, a browser-automation toolkit for AI agents.

Use these facts to find roles at multiple levels, but do not present the candidate as an experienced senior engineer. The one-month engagement and student status mean most target roles should fit 0–2 years of experience, campus hires, 2027 graduates, internships, graduate programmes, paid apprenticeships, or new-grad roles. Exclude roles that require substantial years of full-time experience unless the posting expressly allows freshers/new grads.

## Company and role discovery

Do not use a fixed company list. On every run, use up-to-date searches and available authorized sources to discover employers from scratch, selecting ten companies with the strongest mix of:
- current or recent openings in India;
- explicit eligibility for freshers, graduates, interns, apprentices, or 0–2 years of experience;
- match with the candidate's resume, skills, projects, education and experience;
- plausible recruiter contact availability;
- newness vs recent runs, while allowing repeats if a genuinely new relevant vacancy/hiring signal exists.

Research company careers pages, job postings, trusted job boards, publicly viewable LinkedIn posts, company news, public hiring posts, and any authorized search tool. Cite URLs and dates in `Source Evidence`. Do not fabricate an opening, date, eligibility requirement, location, or hiring signal.

Consider roles across:
- Software Engineer / Software Developer / SDE I / Associate Software Engineer
- Backend Engineer / Python Developer / API Engineer
- AI Engineer / Applied AI / LLM Engineer / Agentic AI Engineer / AI automation
- ML Engineer only when actual eligibility and role match the resume (do not assume advanced ML depth)
- Platform Engineer / Infrastructure Engineer / Junior SRE / DevOps / Cloud Engineer
- Automation Engineer / Developer Productivity / AI tooling
- Embedded Software Engineer / Firmware Engineer / Edge AI / Systems Engineer
- Internship, graduate engineer, campus/new-grad, paid apprenticeship, trainee engineering programmes.

Geography:
- India-wide roles, including remote roles open to workers based in India.
- International opportunities only if the job explicitly accepts Indian applicants and states relevant visa sponsorship/relocation support or an eligible route. Do not infer sponsorship from the employer's size.
Opportunity types:
- full-time, graduate programmes, internships, paid apprenticeships.
Exclude unpaid opportunities unless the user later explicitly permits them, irrelevant sales/BPO roles, false "remote anywhere" interpretations, and roles that clearly require more experience than the resume establishes.

## Finding two suitable contacts per company

For each company target two people if possible, preferably recruiters for campus/graduate/new-grad or technical recruiting:
- University/graduate/campus recruitment
- Talent Acquisition Partner / technical recruiter for software, AI, platform, infrastructure, systems, embedded
- Hiring manager only if recruiter options cannot be found and professional email evidence is strong.

Use legal, public and authorized sources: search engines, public LinkedIn posts/profiles/pages, official hiring posts, career websites, public community posts, public biographies, professional directories, and authorized features from Apollo that exist on the user's current plan.

Do not scrape private or access-controlled LinkedIn data, bypass login/captcha, reconstruct masked emails, access leaked data, or use personal emails without explicit permission. If Apollo search/enrichment is unavailable or plan-restricted, log it and continue other methods. Credit-consuming Apollo enrichment requires explicit user approval for total contacts/maximum credits up front. If no approval is possible during an invocation, skip the paid/credit operation.

## Strict professional email verification

An email is eligible for `verified_contacts.xlsx` only if the exact professional address is supported by one of:
1. An accessible public source explicitly showing the exact email and tying it to the target person/current relevant hiring team, plus independent identity/current employment evidence.
2. An authorized professional contact database result with a clear exact address and positive email status, plus independent identity/current-employer match.
3. An actual deliverability verification result from an available legitimate service, plus separate evidence linking the address to the person/current company.

A syntax check alone is not verification. A domain/MX check alone is not verification. A source being indexed alone is not verification unless its displayed information can be inspected sufficiently to tie the address to the correct person/company. A generic careers inbox is never an individual recruiter's personal email. It may be separately tracked as a company contact but does not count toward the 20 individual recruiter target.

Reject guesses, inferred patterns, masked addresses, former-employer emails, unrelated same-name results, questionable directories, and any result whose attribution is ambiguous. Store excluded candidates/reasons in the internal research evidence rather than the clean daily contact workbook.

## Email writing requirements

Use a natural cold-email voice, roughly 90–150 words. Personalize with a specific verifiable signal such as the recruiter’s current role, relevant live job posting, team, or recruiting announcement. Never invent personal admiration, prior usage, meetings, or specific recruiter actions. Do not over-flatter or write a generic pitch.

Suggested base, personalize each message:
Subject: `Software engineering opportunities at {{Company}}`

Hi {{FirstName}},

I saw your work around {{specific verified recruiting context}} at {{Company}} and wanted to reach out about suitable early-career engineering opportunities.

I’m graduating in 2027 from Bangalore Institute of Technology and have been building practical projects in AI systems, automation, infrastructure, and embedded software. I enjoy learning quickly, working through unfamiliar problems, and taking projects from idea to working implementation.

Here’s my portfolio: https://sneh30.github.io/portfolio/

I’ve attached my resume for context. I’d appreciate being considered for a suitable opportunity, and I’m happy to complete a small relevant technical assignment to demonstrate what I can do.

Thanks for your time,
{{YourName}}

Do not say a resume is attached unless the reviewed PDF was actually attached. If no approved PDF exists, use a truthful alternative with the portfolio link and omit any attachment claim. Never make a role-specific claim about eligibility unless checked against the posting.

## Gmail website UI only — drafting and safety

All Gmail activity must use only the user-visible official website at `https://mail.google.com/` through an available, authorized browser UI automation tool. No Gmail APIs, direct network calls, hidden endpoints, Apps Script, IMAP, SMTP, Gmail connector, or direct mailbox data manipulation.

First boot:
- Open Gmail in the browser.
- If signed out, ask: “Please sign in to your Gmail account in this Gmail website tab. Do not share your password, one-time code, or recovery code with me.”
- Wait until user has signed in and confirms. Do not handle credentials.
- Confirm the Gmail page is actually signed in through visible UI, not by assuming.
- If visible browser automation cannot operate, stop the draft stage and report the exact missing capability. Do not switch to an API.
- If the session expires in later runs, ask the user to sign in again and pause the Gmail stage.

Create one new draft per qualifying verified recruiter:
- Every draft in its own separate browser tab.
- Fill To, personalized subject/body and, only if approved, resume PDF attachment.
- The resume PDF may be compiled from the supplied LaTeX if not found, but must first be shown to the user for review/approval before it is attached to any draft.
- Verify each draft is visibly saved in Gmail UI (e.g. confirmation or presence in Drafts).
- Leave all tabs open for user proofreading and manual send.
- Never click Send, Schedule Send, or any bulk-sending action. Never automatically send, queue, or enrol a message in an outreach sequence.
- Do not overwrite/delete existing Gmail drafts. Detect likely duplicates using recipient+subject/run information and skip rather than create duplicates.
- If a UI operation is ambiguous, inspect state and retry no more than twice. If still ambiguous, stop that draft, log the problem, and continue only if safe.
- Never claim a draft was saved unless visible UI evidence confirms it.

## Master Excel and per-run data

Root:
`<PROJECT_ROOT>`

Required files:
- `RUN_PROMPT.md`: repeated daily prompt
- `PROJECT_SPEC.md`: this specification
- `README.md`
- `config/settings.json`
- `config/state.json`
- `resume/resume.tex`
- `resume/resume_profile.md`
- `master_recruiter_tracker.xlsx`
- `runs/YYYY-MM-DD_run-NNN/verified_contacts.xlsx`
- `runs/YYYY-MM-DD_run-NNN/source_evidence.json`
- `runs/YYYY-MM-DD_run-NNN/research_summary.md`
- `runs/YYYY-MM-DD_run-NNN/draft_manifest.csv`
- `runs/YYYY-MM-DD_run-NNN/run.log`
- `logs/YYYY-MM-DD.log`
- scripts for workbook validation and setup that can safely re-run.

The master workbook must have these worksheets:
1. `Companies`: company, official domain, India/eligible locations, target role families, current hiring signals, job/source URLs, first/last researched dates, run IDs, notes.
2. `Contacts`: stable contact ID, name, company, domain, title, location, professional email, email evidence type/status, LinkedIn URL, source URLs, role relevance, first discovered, last verified, first/last run ID, outreach status, do-not-contact, dedupe key, notes.
3. `Outreach`: contact ID, email, subject, draft status, draft created time, sent confirmation time, reply time, bounce time, evidence, last checked, run ID.
4. `Source Evidence`: source ID, linked person/company, title, URL, type, access date/time, email visible, identity/current employer supported, hiring relevance, email status claim, evidence notes.
5. `Run Log`: run ID, times, companies selected, contacts researched, emails passed verification, draft tabs saved, messages newly detected in Sent, duplicates skipped, errors, shortfall, output path.

Per run:
- `verified_contacts.xlsx` has only four columns, exactly `name`, `company`, `mail`, `linkdin`; no other columns or notes.
- Every output row must have a verified exact work email and a correct LinkedIn URL.
- No blank rows or placeholders; all rows unique by email, LinkedIn, and normalized name+company.
- `mail` contains only the email address (no comments, source, labels, or explanation).
- If fewer than 20 pass verification, output only the qualifying rows and report exact shortfall.
- Keep excluded/unverified attempts in evidence/tracker, never in the clean output workbook.
- Daily run folders are immutable history; do not overwrite previous run output. Use unique run IDs and timestamped evidence.
- On master workbook updates, back up existing master first, write to a temporary file, validate, and replace only after success. Never reset/overwrite master history.
- Deduplicate by normalized email, canonical LinkedIn URL, and normalized name+company. Preserve strongest/latest evidence.
- Never delete history rows; update current status and last-checked dates.

Outreach states are distinct:
`discovered`, `verified`, `draft_created`, `sent_confirmed`, `replied`, `bounced`, `do_not_contact`, `draft_failed`, `verification_failed`.
Draft creation does not mean contacted. Set `sent_confirmed` only after the user explicitly confirms or a corresponding sent message is visible in Gmail's Sent folder UI. Respect opt-outs and do-not-contact flags. Do not automatically follow up.

## Run process and resilience

Every invocation:
1. Confirm working directory; inspect project files, config, resume, master workbook and last run.
2. Create a unique run ID.
3. Open/confirm Gmail sign-in through the UI; if the user must log in, pause Gmail operations but continue safe research if feasible.
4. Discover current hiring opportunities and select ten companies dynamically from scratch with history-based diversification.
5. Find at least two suitable recruiters per company where possible.
6. Verify identity, current employer, role relevance and exact professional email evidence.
7. Deduplicate against master contacts, do-not-contact, prior drafts, prior contacted people, and previous runs.
8. If Apollo credit-consuming enrichment could materially help, show the total count and maximum credits and wait for explicit approval. Without it, skip that step and log the reason.
9. Produce the clean verified contact Excel; validate it.
10. Compile the resume PDF only if needed and if a local tool is available; request user review/approval before attaching.
11. Create separately tabbed Gmail drafts for verified, eligible contacts, never send.
12. Update master workbook and run logs atomically, keeping backups and old run outputs.
13. Reopen/inspect all exported workbooks and check values/formatting. Confirm counts.
14. Return concise factual summary: ten companies target/actual; verified contacts actual; drafts visibly saved actual; any shortfall; output path. Do not say more than what was done.

Safe retries:
- Retry transient web/source errors with bounded retry (max 2 per source/action).
- For browser form operations, inspect after every action; max 2 retries. No duplicate submissions.
- If resume compile fails, do not attach the LaTeX file as if it were a PDF.
- If master workbook validation fails, do not overwrite it; restore from backup and report blocker.
- If Gmail UI automation is unavailable, do research/workbook stages but explicitly mark draft stage as blocked.
- Never log authentication secrets.
