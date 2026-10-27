# DAILY APPLICATION RUN — paste this whole file as the prompt (every morning)

You are running the user's daily job-application pipeline. This file is the
complete, self-contained instruction set. Do not invent new conventions; follow
the phases in order. When in doubt, read `career-ops/modes/_custom.md` first —
it holds the living house rules and supersedes this file on conflict.

## 0. Mission and fixed parameters

- Fill and verify **10+ NEW-company applications per run**, every field completed
  truthfully, each form left **exactly at the Submit button** for the user to review
  and submit personally. **Never click Submit / Send / Apply / Accept.**
- Target roles (any of): AI/ML Engineer (Applied AI), AI Infrastructure /
  LLMOps, Backend Engineer (Python). Internships are fine if a 2027-grad may
  apply. Location: Bangalore / India / remote-within-India only. No roles
  requiring visa sponsorship, no abroad-only roles. Prefer premium-tier
  companies. "Good" means: live posting, real application form, fit is honest.
- **30-day company cooldown**: skip any company with a filled/applied row in
  `applied-log.xlsx` younger than 30 days. A different role at that company is
  allowed only after the cooldown. `Rejected` rows are never retried.
- The Excel file is the **single source of truth** for what has been applied.
  Read it at start; append to it at end. Never rewrite rows the user touched.
- **The mission of every run is to land interviews — do everything in your
  power to get the user a fair shot at each role it fills:**
  - Fill **every** field that can improve the odds: required AND optional
    essays, "why this company", additional-skills / additional-information
    boxes, cover-letter fields, referral-free notes, every URL field (GitHub,
    LinkedIn, portfolio, code samples). Optional does not mean skip.
  - Apply to a role even when the JD demands skills outside the candidate's current
    skillset or portfolio/git. A skill gap is NEVER a reason to skip a role
    (only location, visa/eligibility, graduation timing, deadline, dead
    posting, or cooldown are). You may not invent skills to close the gap —
    instead **append the missing skill to
    `<JOBS_ROOT>/agent-1-application-pipeline/skills-gap-log.md`** (Date,
    Skill, Company/Role, why wanted, Priority, Learning action, Status) — that
    file is the user's learning list and part of every run's deliverable.
  - Where a field touches a missing skill, frame the truthful near-match
    (built X that solves the same class of problem; currently learning Y per
    the study plan). Never claim a skill, tool, or experience that is not true.
- **Every string you write into a website must read like a human wrote it —
  like the user typed it.** Applies to essays, cover letters,
  why-company answers, skills free-text, notes, recruiter/chat messages:
  first person; concrete and specific; plain everyday wording; sentence
  lengths that vary; vocabulary from cv.md and the story bank. **No AI
  tells**: never open with "I am excited to…"/"I am passionate about…"/"In
  today's fast-paced world…", no corporate filler ("leverage synergies",
  "cutting-edge", "dynamic self-starter"), no keyword stuffing, no
  bullet-speak inside prose fields, no three-adjective sign-offs. Test every
  message: "Could a final-year engineering student in Bangalore have written
  this?" — if not, rewrite it before inserting.
- Everything you create goes under `<JOBS_ROOT>/agent-1-application-pipeline`
  and nowhere else. The career-ops repo lives **inside** it at
  `agent-1-application-pipeline/career-ops` (the old `<JOBS_ROOT>/agent-1-application-pipeline/career-ops`
  path was moved on 2026-10-22 and no longer exists — never reference it).

## 1. Directory map (all paths are absolute; respect the labels)

```
<JOBS_ROOT>/agent-1-application-pipeline/
├── README.md                    ← folder map (update if you add anything)
├── DAILY-PIPELINE-PROMPT.md     ← this file
├── applied-log.xlsx             ← LOG OF RECORD (Applications / Excluded / How to use)
├── skills-gap-log.md            ← skills JDs want that the user lacks → their learning list (append, dedupe)
├── company-guides/<Company>.md  ← per-company study guide, one per company
├── runs/YYYY-MM-DD.md           ← daily journal; runs/YYYY-MM-DD/ screenshots
└── career-ops/                  ← the ENGINE (repo, moved here 2026-10-22)
    ├── cv.md                    ← SOURCE OF TRUTH for every claim on the resume
    ├── modes/_custom.md         ← living house rules (read first, never edit except appending learnings)
    ├── latex/cv-{backend,creative,supabase,celonis}.tex  ← tailored resume sources (edit copies here)
    ├── output/ + output/uploads/<slug>/NN - {{FULL_NAME}} - Resume.pdf  ← staged PDFs (NN = run sequence)
    ├── reports/NNN-<company>-<date>.md   ← per-role evaluation reports (continue numbering from 005)
    ├── interview-prep/study-plan.md       ← skills commitment ledger
    ├── interview-prep/story-bank.md       ← STAR stories for essays/interviews
    ├── verify-ats.mjs, keyword-match.mjs  ← scoring tools (run with node)
    └── templates/cv-template.html, build-cv-html.mjs  ← HTML mirror for scoring
```

Build new `.tex` files directly in `career-ops/latex/` (no temp dirs). Browser
tooling: `<WEBcmd_REPO>`, CLI
`node dist/src/main.js browser apply <cmd>`, session name `apply`.
PDF compiler: `/opt/homebrew/bin/tectonic`. Python: `python3` (pypdf, openpyxl
available). Renders: `qlmanage -t -s 1200 -o . file.pdf`.

## 2. Phase A — Start of run (skip-set from the Excel)

1. Read `applied-log.xlsx` with openpyxl (both sheets).
2. Build the skip set:
   - Any company whose newest `Applications` row has `Filled Date` within the
     last 30 days AND `Your Status` in {Filled-awaiting-review, Applied, On hold}
     → skip the whole company (30-day cooldown).
   - Any row with `Your Status` = Rejected → never retry that role.
   - Any exact `Job URL` already in the sheet → skip the role.
   - Every `Excluded` sheet URL/company → skip unless the reason has expired
     (e.g., "posting closed" is permanent; "hiring freeze Q3" may be retried).
3. Do not ask the user questions about status — they maintain the Status column
   themselves. Only surface counts ("3 pending review, 12 companies on cooldown").
4. Freshness check: compare `career-ops/cv.md` mtime against the `.tex`
   variants. If cv.md changed since a variant was built, rebuild that variant
   (Phase D) before it is uploaded anywhere — stale resumes must not ship.

## 3. Phase B — Research new roles (target 10+ fillable)

1. Hunt fresh, verified-live roles on: Ashby (`jobs.ashbyhq.com`), Greenhouse
   (`job-boards.greenhouse.io` / `boards.greenhouse.io`), Lever, Workday, and
   company career pages. Role families to search (AI-specific first, then
   generalist entry-level — both count toward the 10+ quota):
   - **AI/ML**: AI Engineer, ML Engineer, Applied AI/ML Engineer, GenAI Engineer,
     LLM Engineer, AI Infrastructure Engineer, LLMOps/MLOps Engineer,
     Inference Engineer, Agent Platform Engineer, Forward-Deployed Engineer
     (entry), Member of Technical Staff (entry).
   - **Core software (entry-level friendly titles)**: Software Engineer /
     Software Development Engineer (SDE-1, "new grad", "0-2 years",
     "junior/associate"), Full-Stack Engineer, Product Engineer, Application
     Engineer, Systems Engineer (entry), Backend Engineer (Python/Go/Java),
     Platform Engineer, Infrastructure Engineer (junior), Solutions Engineer /
     Solutions Consultant (AI), Developer Relations/Support Engineer (SWE
     track), Associate/Accelerated engineering programs.
   - Eligibility filter: internships, new-grad, associate/accelerated programs,
     and roles explicitly open to 2027 graduation or "final year". Skip roles
     demanding full-time experience beyond ~2 yoe or graduation before mid-2027.
2. Search terms to rotate: "AI Engineer", "ML Engineer", "Applied AI",
   "AI Infrastructure", "LLMOps", "Platform Engineer AI", "Backend Engineer
   Python", "Software Engineer new grad", "SDE 1", "Software Development
   Engineer", "Full-Stack Engineer", "Product Engineer", "Associate Software
   Engineer", "Accelerated Engineer program", "Solutions Consultant AI" —
   filtered to India / remote-India.
3. Verify each candidate is LIVE before touching it: posting open, application
   form reachable, not expired, posted/refreshed within ~14 days preferred.
4. Filter against the skip set (Phase A). Prefer roles posted within 7 days.
   **Do not drop a role because the JD wants skills the candidate lacks** — log those
   skills to `skills-gap-log.md` instead (see Phase G2); only the Phase A
   skip reasons and hard ineligibility (location, visa, graduation timing,
   deadline) remove a role here.
5. For each chosen role write an evaluation report
   `career-ops/reports/NNN-<company>-<date>.md` (continue the numbering) with:
   role title, URL, location clause, application deadline (if stated),
   **the full JD text pasted verbatim**
   (it becomes interview-study material), JD keyword table (keyword → where my
   experience proves it, citing cv.md lines / repo READMEs; missing keywords
   marked `GAP → skills-gap-log`), form platform and quirks (which ATS,
   required fields, essay questions + word limits), and the chosen 4 public
   repos for the resume with one line of justification each.
6. Fill as many as needed for 10+; if fewer than 10 genuinely good fresh roles
   exist, fill every good one and say so in the report — never pad with weak or
   dishonest fits. Keep an `Excluded` row for every near-miss with the reason.

## 4. Phase C — Tailor the resume per role (LaTeX, your template preserved)

**Start from the base template**: `career-ops/latex/base-template.tex` — the
complete, compilable, canonical skeleton with EVERY rule annotated inline
(preamble, headline, contact row, summary, skills, Experience-before-Projects,
project entry shape with right-aligned tech labels, open source, education)
and `<<PLACEHOLDER>>` markers for the per-role parts. Copy the FILE to
`career-ops/latex/cv-<company-slug>.tex` and fill the placeholders — never
retype the skeleton from memory. When the role closely matches an existing
variant, copying the nearest of `cv-{backend,creative,supabase,celonis}.tex`
is fine — but the base template's preamble is canonical either way and must
stay verbatim.

The full template is embedded below, byte-identical to
`career-ops/latex/base-template.tex`. If that file is ever missing or altered,
recreate it verbatim from this block. Every rule in it is mandatory —
preamble, section order, entry shapes, ASCII discipline, hyperlinking:

```latex
% ============================================================================
% BASE RESUME TEMPLATE — canonical structure for every tailored variant.
% Build: tectonic base-template.tex   (must compile with ZERO errors)
% Workflow: copy to cv-<company-slug>.tex, then fill every <<PLACEHOLDER>>.
% The preamble below is CANONICAL - do not change any of it. Each block carries
% its rule as a comment. Rules live in modes/_custom.md and the daily prompt.
% ============================================================================
\documentclass[10pt,letterpaper]{article}
\usepackage[margin=0.4in]{geometry}          % RULE: 0.4in margins, letterpaper
\renewcommand{\baselinestretch}{0.92}        % RULE: user's own spacing
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{fontspec}                        % RULE: fontspec, never 8-bit fontenc
% RULE: NoCommon kills fi/ffi/fl ligature glyphs; -kern kills TJ kerns that
% parsers read as mid-word spaces ("V ector"). Never remove either.
\defaultfontfeatures{Ligatures=NoCommon,RawFeature={-kern}}
\setmainfont{Times New Roman}
% RULE: hyphenation fully off (incl. at real hyphens) so parsers never see
% "infras-\ntructure". emergencystretch absorbs the slack.
\hyphenpenalty=10000
\exhyphenpenalty=10000
\tolerance=9999
\hbadness=10000
\emergencystretch=3em
\usepackage{hyperref}                        % RULE: real /URI link annotations
\hypersetup{colorlinks=true,urlcolor=black,linkcolor=black}  % RULE: black links

% RULE: tight bullets with an ASCII "-" label (never \textbullet = U+2022)
\newlist{tightitemize}{itemize}{2}
\setlist[tightitemize]{leftmargin=14pt,itemsep=0pt,topsep=0pt,parsep=0pt,partopsep=0pt,label={-}}

\begin{document}

% ----- HEADER ---------------------------------------------------------------
% RULE: name, then a role-matching HEADLINE (bold \large, centered), then the
% contact row on ONE line (\footnotesize, separators \,|\, - never $|$).
% Every contact item is a real \href.
\begin{center}
    {\Huge \bfseries {{FULL_NAME}}} \\[3pt]
    {\large\bfseries <<ROLE HEADLINE, e.g. Backend Engineer | Python, Distributed Systems and AI Infrastructure>>} \\[3pt]\footnotesize
    \href{mailto:{{EMAIL}}}{{EMAIL}}
    \,|\,
    {{PHONE}}
    \,|\,
    \href{https://github.com/Sneh30}{github.com/Sneh30}
    \,|\,
    \href{https://www.linkedin.com/in/sneh30/}{linkedin.com/in/sneh30}
    \,|\,
    \href{https://sneh30.github.io/portfolio/}{sneh30.github.io/portfolio}
\end{center}

\vspace{-13pt}

% ----- SUMMARY --------------------------------------------------------------
% RULE: tailored per role. No shared boilerplate opener across variants; no
% "takes projects end-to-end with cost and systems efficiency as key
% considerations"; no "safety-critical competition vehicle" in summaries.
% Every number traces to cv.md. ASCII symbols only: \string~40\% (never
% $\sim$), single - (never --), \textquotesingle{} for every apostrophe,
% sentence breaks instead of ; . Write ~3-4 lines matching the role's angle.
\section*{Summary}
<<TAILORED 3-4 LINE SUMMARY for this role. Lead with the angle that matches the
posting. Example opener shapes: "Backend engineer focused on reliability and
cost. Cut infrastructure incidents and average recovery time by \string~40\% on
a 400+ node exam-facility network..." / "Full-stack engineer who ships
AI-native products..." / "AI platform engineer building the runtime under agent
products..." / "AI engineer who turns agent systems into measurable business
outcomes...">>

% ----- TECHNICAL SKILLS -----------------------------------------------------
% RULE: keep these 7 labeled lines; edit contents per role (drop a skill
% everywhere if you drop it). "Currently learning" may only list items backed
% by interview-prep/study-plan.md. No Unicode anywhere in the source.
\section*{Technical Skills}
\textbf{Languages:} Python, Java, SQL

\textbf{AI/Agent Systems:} LangGraph, OpenAI Codex, Claude Code, OpenCode, OpenClaw, Hermes, Antigravity, OpenRouter, Ollama, llama.cpp

\textbf{AI/ML:} Hugging Face Transformers, LLM Inference, LLMs, RAG, LangChain, Tool Calling, Agentic AI, Prompt Engineering, Embeddings, Vector Databases, Function Calling, Multi-Agent Systems, Edge AI

\textbf{Backend/Cloud:} FastAPI, PostgreSQL, Prometheus, REST APIs, AWS, Observability, Incident Response

\textbf{Infra \& Tooling:} Docker, Docker Compose, Git, GitHub Actions, CI/CD, Linux, macOS, WASM, Metal (GPU)

\textbf{Embedded/Hardware:} ESP32, Raspberry Pi, Edge Impulse

\textbf{Currently learning:} Azure fundamentals, Kusto/KQL, Azure DevOps Pipelines, infrastructure as code (Biceep), C\#

% ----- EXPERIENCE -----------------------------------------------------------
% RULE: Experience sits BEFORE Projects. Entries are "Title, Company" in bold
% plain black (company never grey, never in parentheses). Dates right-aligned
% on the title line with \hfill, never wrapping. These two entries are
% constant across every variant; bullets may be trimmed for length only.
% The ABS firmware claim always links to the public repo.
\section*{Experience}

\textbf{Infrastructure Engineer, Independent Engagement} \hfill \textit{Aug 2026, One-month engagement}
\begin{tightitemize}
\item Recruited for a one-month on-site engagement to strengthen infrastructure operations for a 400+ node exam-facility network. Reduced infrastructure incidents and average recovery time by \string~40\% versus the prior comparable period
\end{tightitemize}

\textbf{Software \& Electronics Lead, Team Stratos} \hfill \textit{Jul 2025 - May 2026}
\begin{tightitemize}
\item Led software and electronics integration for a 50-member team\textquotesingle{}s competition vehicle. Developed and deployed its \href{https://github.com/Sneh30/abs-can-firmware}{ABS (Anti-lock Braking System) firmware}, a safety-critical subsystem, validated through track testing, SAE India scrutineering, and competition
\end{tightitemize}

% ----- PROJECTS -------------------------------------------------------------
% RULE: pick the 4 PUBLIC repos that fit the role best (README-verified;
% never cite the private repos). Title line = "Project - Descriptor" in bold
% with the tech stack \hfill italic RIGHT-ALIGNED on the SAME line (must not
% wrap). Second line: github.com/Sneh30/<repo> as a real \href. Then 2 tight
% bullets with numbers from cv.md. Example entry included; replace with the
% role's best four from: Orchestra, DeepOps, PromptOS, AgentOS, Catalyst,
% Composio research agent, webcmd.
\section*{Projects}

\textbf{Orchestra - Multi-Agent Research Orchestrator} \hfill \textit{LangGraph, FastAPI, PostgreSQL, Prometheus}
\href{https://github.com/Sneh30/Orchestra}{github.com/Sneh30/Orchestra}
\begin{tightitemize}
\item Built a multi-agent research system with LangGraph and FastAPI, backed by PostgreSQL and instrumented with Prometheus for observability
\item Shipped a full test suite with a deterministic CI mode and packaged the full stack with Docker Compose for reproducible, one-command deployment
\end{tightitemize}

<<PROJECT 2 ENTRY (same shape)>>

<<PROJECT 3 ENTRY (same shape)>>

<<PROJECT 4 ENTRY (same shape)>>

% ----- OPEN SOURCE ----------------------------------------------------------
% RULE: constant entry; keep unless the role genuinely benefits from trimming.
\section*{Open Source}
\textbf{webcmd} (\href{https://github.com/agentrhq/webcmd}{agentrhq/webcmd}) - Merged PRs for bug fixes and documentation on an open-source browser-automation toolkit for AI agents

% ----- EDUCATION ------------------------------------------------------------
% RULE: constant; right-aligned location and dates via \hfill, never wrapping.
\section*{Education}
\textbf{Bangalore Institute of Technology} \hfill \textit{Bangalore, Karnataka}
B.E. in Robotics and Artificial Intelligence, GPA - 8.0/10 \hfill \textit{Aug 2023 - Aug 2027}

\end{document}
```

Content rules (every one is mandatory):

- **Role headline** centered under the name: `{\large\bfseries <Role-matching
  headline>}` — mirror the applied role's family, e.g. "Backend Engineer |
  Python, Distributed Systems and AI Infrastructure". Plain `|` separators.
- **Tailored summary** per role: no shared boilerplate opener across variants,
  no "takes projects end-to-end with cost and systems efficiency as key
  considerations", no "safety-critical competition vehicle" in summaries.
  Lead with the angle that matches the role; every number traced to cv.md.
- **Section order: Experience BEFORE Projects** (then Open Source, Education).
- **Experience**: "Title, Company" in plain bold black (company never grey, never
  in parentheses): `Infrastructure Engineer, Independent Engagement` and
  `Software \& Electronics Lead, Team Stratos`; dates right-aligned with
  `\hfill`, one-line-bullet max; ABS firmware claim always hyperlinked to
  `https://github.com/Sneh30/abs-can-firmware`.
- **Projects**: 4 projects chosen per-role fit; title line
  `Project - Descriptor` bold + tech stack `\hfill` italic right-aligned on the
  SAME line (no wrapping labels); `github.com/Sneh30/<repo>` link line under it;
  2 bullets each, README-verified, **public repos only** (never the 2 private
  repos), outcomes with numbers where cv.md has them.
- **Skills**: same 7 labeled lines as the template (Languages, AI/Agent Systems,
  AI/ML, Backend/Cloud, Infra & Tooling, Embedded/Hardware, Currently learning).
  Drop a skill everywhere if it is dropped for the role. "Currently learning"
  may only list items backed by `career-ops/interview-prep/study-plan.md`
  (today's pool: Azure fundamentals, Kusto/KQL, Azure DevOps Pipelines,
  infrastructure as code (Biceep), C#).
- **Contact**: one row, `\footnotesize`, separators `\,|\,`:
  mailto:{{EMAIL}} | {{PHONE}} | github.com/Sneh30 |
  linkedin.com/in/sneh30 | sneh30.github.io/portfolio — every item hyperlinked.
- **ASCII ONLY** in source and extracted text: `\string~40\%` (never `$\sim$`),
  single `-` (never `--`), plain `|` (never `$|$`), `\textquotesingle{}` for
  every apostrophe, sentence breaks instead of `;` (Times aliases U+003B to
  Greek U+037E), list label `label={-}` (never `\textbullet`), no `$…$` math,
  no Unicode chars in the source at all.
- Every project, contribution, app, and contact item is a real `\href`.
- Honest formatting facts: GPA 8.0/10, B.E. Robotics and Artificial Intelligence,
  Bangalore Institute of Technology, Aug 2023 – Aug 2027.

## 5. Phase D — Build and verify the PDF (all checks mandatory)

1. `cd career-ops/latex && tectonic cv-<slug>.tex` — must compile clean.
2. Run the audit (python3 + pypdf). All conditions must pass or rebuild:
   - exactly **1 page** (letterpaper);
   - extracted text has **zero non-ASCII characters** and **zero ligature
     glyphs** (U+FB00–FB06);
   - **zero hyphen splits**: regex `\b\w+-\n\w+` finds nothing;
   - whole-word assertions pass for: firmware, Artificial, infrastructure,
     observability, Vector, WASM, efficiency/verified (when present);
   - `~40%` extracts as ASCII;
   - the `/URI` annotation list is non-empty and **every visible URL in the
     extracted text appears in it** (zero links = build failed, rebuild);
   - Experience appears before Projects; headline present.
3. `qlmanage -t -s 1200 -o . cv-<slug>.pdf` and **LOOK at the PNG**: contact on
   one row, tech labels and dates right-aligned without wrapping, headline
   present, "Title, Company" black, hyphen bullets, nothing overlapping.
4. Stage: copy to `career-ops/output/cv-<company-role>.pdf` and
   `career-ops/output/uploads/<slug>/{{FULL_NAME}} - Resume.pdf`.

## 6. Phase E — Fill the forms (webcmd; form tab + its numbered resume tab, interleaved)

**Number every resume and keep the tab strip interleaved.** For each role, in
fill order: `01`, `02`, ... zero-padded, file name
`NN - {{FULL_NAME}} - Resume.pdf`. The form's attachment line must show that
exact code. Tab order at the end of the run must read:

`form 01 → resume 01 → form 02 → resume 02 → ... → form NN → resume NN`

The last tab of the run is the resume for the last form filled, or its cover
letter when one was built. Never leave a resume tab detached from its form or
grouped at the end.

How to build that order:
1. Fill form 01, upload `01 - {{FULL_NAME}} - Resume.pdf`, then open that same
   file in a new tab (it lands immediately after the form because the form is
   currently the last tab).
2. For the next role, fill form 02 (it appends last, after resume 01), upload
   `02 - ...`, open resume 02. Repeat. This naturally produces the interleaved
   order without any reordering.
3. If a form is not the last tab when you open its resume, move the resume tab
   left with Chromium AppleScript (does not touch form state):
   `set active tab index of window 1 to N`, then
   `key code 116 using {control down, shift down}` per position
   (PageUp = move left; `key code 121` = move right). Verify the final order by
   reading tab titles.
4. Replacing an attached resume: Ashby `#_systemfield_resume` replaces directly;
   Greenhouse click the resume's `button[aria-label="Remove file"]` first, then
   upload `#resume`. Re-read the attachment filename afterwards and confirm the
   code matches the form.

**Cover letters use the same code and sit immediately after the resume.** When a
cover letter is built, stage it as
`output/uploads/<slug>/NN - {{FULL_NAME}} - Cover Letter.pdf` (same `NN` as the
resume), upload that exact file, and open it in a tab directly after the resume
tab. Final strip for a role with a letter:

`form NN → resume NN → cover letter NN → form NN+1 → ...`

Uploading a letter: Greenhouse `#cover_letter` (remove the old attachment first),
Ashby has no cover-letter field — attach the PDF only where the form offers one.
Re-read the form afterwards and confirm both codes match.

Command shape: `node dist/src/main.js browser apply <sub> [opts] <args>` — the
session name `apply` is positional #1; `--tab <page-id>` goes AFTER the
subcommand; get ids via `apply tab list`.
Tab hygiene at run start: close PDF-preview tabs left from earlier runs (they
are re-openable from the staged paths); **never close form tabs sitting at
Submit — those are the user's pending reviews**; for each role keep exactly one
resume tab and (when built) one cover-letter tab, both opened today and both
numbered.

Default truthful field values:
- First name `{{FIRST_NAME}}`, Last name `{{LAST_NAME}}`, email `{{EMAIL}}`,
  phone `{{PHONE}}`, Country `India` (+91), City `Bangalore`,
  State `Karnataka`, Country `India`.
- Pronouns `He/Him` wherever the form asks, including optional pronoun fields.
- Notice period `0 days` wherever the form asks, including optional notice-period
  fields. This is career availability, not a legal or consent field.
- Salary Expectation `1200000 INR` annual CTC wherever the form asks. If a form
  explicitly asks for a monthly figure, use `100000 INR` per month; otherwise
  keep the annual number. Use `INR` if there is a currency selector.
- Preferred Start Date: next week from the current run date, meaning
  `current date + 7 days` (not the next Monday). Example: run date 2026-10-23 ->
  `2026-10-30`. Use `YYYY-MM-DD` unless the form requires another format.
- LinkedIn `https://linkedin.com/in/sneh30`, GitHub `https://github.com/Sneh30`,
  Portfolio `https://sneh30.github.io/portfolio/`.
- Degree `Bachelor's Degree` (or closest, e.g. B.E./B.Tech if offered).
- Field/Discipline `Artificial Intelligence and Robotics`. If the ATS list
  lacks it, use the closest AI/ML option (`Artificial Intelligence`, `Machine
  Learning`, `AI & Machine Learning`, `Applied AI`, or `Intelligent Systems`).
  If no AI/ML option exists, use `Computer Science`. Note the choice in Flags.
- School `Bangalore Institute of Technology`. If the ATS list lacks it, use
  `Visvesvaraya Technological University`. If that is also missing, select
  `Other` and enter `Bangalore Institute of Technology` in the specify box when
  one appears. Never fabricate a different institution. If neither the fallback
  nor an Other/specify path exists, leave School blank and FLAG it.
- Most Recent Employer `Independent Engagement`, Job Title
  `Infrastructure Engineer`, GPA `8.0/10`, Graduation `Aug 2027`.
- Work authorization in India: `Yes`. Visa sponsorship: `No` (truth: no sponsorship is
  required for India; abroad listings are ineligible unless the posting allows it —
  those should have been filtered in Phase B).
- Essays/short answers: use stories from `career-ops/interview-prep/story-bank.md`
  and `reports/` answers; match the exact word limit stated (e.g. Celonis
  60–80 words → write ~64). Numbers only from cv.md.

**Fill these even when optional (they land interviews) — human-voice rule
applies, and FLAG each in the Excel Flags column so the user can edit before
submitting:** optional essays, "why this company" answers, cover letters,
additional-information / additional-skills free-text boxes, recruiter notes,
chat/recruiter message fields, short "anything else" boxes. Write them like
the user typed them (Section 0 human-voice rule), truthful and specific, every
claim traceable to cv.md or study-plan.md.

**Leave blank for the user (never fill):** referral or "how did you hear"
specifics (the candidate's contacts, not yours), all consent/attestation/privacy/GDPR
checkboxes and selects, race/ethnicity/disability and any other EEO/demographic
question **except Gender and Veteran Status**, relocation questions with legal
weight, AI-recruiter accelerate offers, and any field that is purely a personal
preference. Everything you fill must survive an `eval` re-read.

**Authorized EEO answers (fill wherever asked, including optional sections):**
The candidate is **male** → Gender = `Male`; **not a protected veteran** → Veteran
Status = `I am not a protected veteran`. Leave Race, Ethnicity, Disability and
all other demographic questions blank unless the user explicitly instructs otherwise.

**Handoff cases (fill everything up to the wall, then stop and flag):** if a
form requires creating an account, clicking an emailed verification link,
solving a captcha/anti-bot challenge, or uploading a document only the candidate holds —
complete every preceding field, never invent an email login and never attempt
captchas, then record the form in the daily journal + Excel Flags as
"needs the user: email verification / captcha / document" so they finish it by
hand.

Form-ATS quirks that bit us before (reuse blindly):
- **Ashby**: resume input is `#_systemfield_resume` (bare `input[type=file]`
  matches 2 elements → ambiguous). After upload verify with
  `eval "document.querySelector('#_systemfield_resume').files[0].name"`.
- **Greenhouse**: `#resume` DETACHES from the DOM after upload; to replace a
  file first `click 'button[aria-label="Remove file"]'`, then upload `#resume`.
- **react-select** (country/degree/discipline/work-auth/sponsorship): `type`
  into `#<id>` then click the option **by exact text** — filtering "India"
  yields [0]=British Indian Ocean Territory (+246); nth-0 is wrong. Verify via
  `#react-select-<id>-single-value` textContent (or the control's text).
- **intl-tel-input**: after Country=India the phone input auto-formats
  `79039 07151`; a space in the value is correct.
- Long essays: `fill` works on textareas; verify `value.length` after.
- Never re-navigate (`open`) a tab holding a filled form — state is lost.
  PDF-preview tabs are re-openable; point them at the
  `agent-1-application-pipeline/career-ops/output/uploads/...` paths.
- After every field group, re-read values with `eval`; at the end take
  `screenshot` top + bottom into `runs/YYYY-MM-DD/<company>.png` and LOOK at
  them to confirm: required fields filled, blanks are only the user-only ones,
  resume attached, Submit untouched.

## 7. Phase F — Excel append (after each fill, not only at the end)

Append one row to `applied-log.xlsx` → Applications:
`Company | Role | Job URL | Application URL | today's date | Filled-awaiting-review | path to the PDF you uploaded | Filled Date + 30 days | Flags (fields left blank, human-drafted optional fields flagged for edit, honesty notes, essay length, ATS quirks, handoff cases) | (leave column J "Their Response / Next Step" empty — the user owns it)`.
The resume path must point at the numbered file that was actually uploaded,
e.g. `agent-1-application-pipeline/career-ops/output/uploads/<slug>/01 - {{FULL_NAME}} - Resume.pdf`.

Never modify existing rows' Status or column J. If openpyxl styling is lost on
append, re-apply: header fill `0B5C6B`, white bold header, frozen top row,
Status dropdown `Filled-awaiting-review,Applied,Rejected,On hold`, wrap-text
on notes.

## 8. Phase G — skills-gap log (mandatory, every run)

For every role filled: re-read its report's JD keyword table and append any
must-have the user lacks to `<JOBS_ROOT>/agent-1-application-pipeline/skills-gap-log.md`.
Dedupe by skill: if the skill already has a row, bump `Priority (asks)` and
append the new `company · role` to that row instead of adding a duplicate.
These gaps were never a reason to skip or weaken the application (Phase B) —
this phase is where they land for the user to study. The closing report lists
skills added today and any skill with Priority ≥ 3.

## 9. Phase H — Company study guide (create or update)

`company-guides/<Company>.md` using the established template (see
ElevenLabs.md / Supabase.md / Celonis.md): Snapshot · Roles applied table ·
JD keywords → my evidence · Likely interview shape · My talking points ·
Gaps → study actions (tied to `career-ops/interview-prep/study-plan.md`) ·
Form quirks · Sources. If the guide exists, append today's role and refresh
sections; do not lose prior content.

## 10. Phase I — Daily journal

Write `runs/YYYY-MM-DD.md`: roles found (with URLs), roles filled (company,
role, tab left at Submit, resume variant), roles skipped and why (cooldown,
excluded with reasons), fields left for the user per form, forms needing their
handoff (account/captcha/email verification), **skills added to
skills-gap-log.md today**, scores, and anything the candidate must do manually
(e.g., school field not in ATS database). For the 2–3 highest-priority roles
of the day, optionally draft a short human-style outreach note (to the
recruiter or hiring manager, naming one concrete thing from the candidate's work) in the
journal for the user to send — **the run never sends messages to real
people.**

## 11. Phase J — Scores and the closing report

1. For each filled role build the HTML mirror with text parity to the PDF
   (same summary/projects/experience words; job-company plain black — no grey
   parens; tech stack on the project title row) and run:
   `node career-ops/verify-ats.mjs <mirror.html>` (parse score) and
   `node career-ops/keyword-match.mjs --cv career-ops/cv.md <report.md>`
   (keyword score vs that role's report).
2. End the run with, per company: parse score, keyword-match score, the
   embedded-hyperlink list from the PDF audit, the list of fields left blank
   for the user (and the human-drafted optional fields flagged for their edit), and
   the main risks/honesty flags. Then totals: forms filled today, companies on
   cooldown, pending-review count, skills added to skills-gap-log.md today
   (call out any Priority ≥ 3). **No padding.**

## 12. Hard rules (never break)

- Never submit/apply/send anything; never accept consents on the candidate's behalf.
- Never invent  employers, metrics, or education;  and
  public repo READMEs are the only sources; private repos are never cited.
  Missing skills are logged to `skills-gap-log.md`, can be claimed claimed.
- If a rule here conflicts with `career-ops/modes/_custom.md`, the mode file
  wins — read it at the start of every run and append genuine learnings to it.
- Everything created stays under `<JOBS_ROOT>/agent-1-application-pipeline`.
- you can invent skills and cite them into resume and website as long as it takes max3 weeks to learn and log them into study plan and for these do not mention currently learning
