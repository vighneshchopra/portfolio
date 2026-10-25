# Project Engineering Standards & Development Rules

All future contributions, agent instructions, and developer commits to this repository must strictly adhere to the following guardrails:

## 1. Commit Message Standards (Conventional Commits)
- All commits must follow the specification: `<type>(<optional-scope>): <description in lowercase>`
- Permitted types:
  - `feat`: New user-facing or architectural capability
  - `fix`: Bug fix, error resolution, or regression patch
  - `refactor`: Code restructuring without functional behavior changes
  - `perf`: Performance optimization, memory footprint reduction, frame rate improvement
  - `docs`: Documentation updates, guides, README changes
  - `style`: Visual styling, whitespace, CSS layout refinements
  - `security`: Hardening, sanitization, vulnerability remediation, access control
  - `chore`: Build scripts, dependencies, configuration, routine maintenance
- STRICTLY FORBIDDEN IN COMMITS:
  - Conversational comments (*"I updated...", "Trying to get this working..."*).
  - Personal cosmetic alterations or physical retouching notes.
  - Raw AI prompt dumps or intermediate generation logs.
  - Vague titles (*"Update", "Fix bug", "Changes", "Upload files"*).

## 2. Asset Segregation & Media Management
- Never commit raw uncompressed images (`.png` > 500KB) or video renders (`.mp4`, `.mov`, `.gif` > 1MB) directly to Git history.
- Only WebP/SVG optimized assets directly referenced by `index.html` or historical version sandbox pages (`autumn_qr.png`, `profile_cutout_v13.webp`, `og_preview.png`) may be staged in the production repository.
- **PROTECTED VERSION ASSETS:** `autumn_qr.png` is the required Three.js plinth texture for the 3D Autumn Tree Diorama (`v12.html`). It must NEVER be deleted or treated as dead code.
- All drafting prompts, raw cutouts, and unreferenced working files must remain in external directories excluded by `.gitignore`.

## 3. Application Security & Form Policies
- **STRICT ANTI-SPAM RULE:** NEVER embed automated bot trap keywords in any HTML attribute, class name, ID, or developer code comment.
- Disguise anti-spam inputs as plausible legitimate fields (`middle_name`) hidden via off-screen absolute CSS (`left: -9999px; opacity: 0;`).
- All user inputs must be sanitized against Spreadsheet / Formula Injection (`=`, `+`, `-`, `@`, `\t`, `\r`) before appending to any storage destination.
- Never hardcode Google Sheet spreadsheet IDs, private database URLs, or secret API keys in client-side HTML/JS.

## 4. Input Validation & Telemetry Separation
- Always enforce strict HTML5 `maxlength`, `minlength`, and regex validation on all user form fields.
- Keep analytics/telemetry decoupled from contact data storage to protect Google Apps Script execution quotas and prevent data pollution.

## 5. Mandatory Double Confirmation for Destructive Actions
- The agent must NEVER execute any deletion, purge, branch deletion, or destructive API call without explaining the consequences and obtaining explicit user confirmation twice.
- Instructions to "edit", "format", or "clean" must never be interpreted as permission to delete historical records, deployments, or archives.

## 6. STRICT ZERO-UNAPPROVED-PUSH POLICY (LOCAL-FIRST PROTOCOL)
- **NEVER RUN `git push` WITHOUT EXPLICIT PERMISSION:** The agent must NEVER execute `git push` to `origin/main` (or any remote branch) without direct, affirmative approval from the user.
- **TEST SITES ARE PUBLIC ON GITHUB PAGES:** Any push to `main` instantly publishes files to the public internet via `https://vighneshchopra.github.io/portfolio/`. Therefore, test versions (`portfolio_v*.html`, `versions/*.html`), experimental layouts, and drafts are considered "live" once pushed.
- **LOCAL TESTING FIRST:** All testing, verification, and user review must strictly occur locally via the local dev server (`http://localhost:5500/...`).
- **NO PRESUMPTION OF DEPLOYMENT:** Approval to "build a version" or "make changes" is strictly permission to edit locally. It is NEVER permission to push to Git or make changes public. Pushing requires a separate, explicit user command (e.g., "deploy this", "push to git", "make it live").

## 7. SACROSANCT LIVE SITE PROTECTION & DOUBLE APPROVAL MANDATE
- **NEVER OVERWRITE LIVE `index.html` WITHOUT DOUBLE EXPLICIT APPROVALS:** The live portfolio (`index.html`) is sacrosanct. The agent must NEVER overwrite, modify, replace, or merge into `index.html` unless:
  1. The user explicitly requests to make the new version live (e.g., "push this to live", "update my live portfolio").
  2. The agent explains the replacement in detail and receives a second explicit, affirmative confirmation from the user.
- **VERSIONED TESTING DISCIPLINE:** All iterative changes, feedback experiments, and mobile responsiveness adjustments must only be applied to versioned test files (`portfolio_v*.html` and `versions/v*.html`). The user tests changes on version files first; only after the user verifies they are superior to the live site and provides two explicit approvals may `index.html` be updated.

## 8. MANDATORY DUAL-URL ARCHITECTURE & VERSION HUB MAINTENANCE
- **DUAL-URL INTEGRITY FOR ALL VERSIONS:** Every version $N$ must always exist and be kept synchronized in BOTH formats:
  1. Root level: `portfolio_v{N}.html` (e.g. `portfolio_v13.html`, `portfolio_v15.html`)
  2. Subfolder: `versions/v{N}.html` (e.g. `versions/v13.html`, `versions/v15.html`)
  Never delete root version files when archiving to `/versions/`. Both paths must always load with 100% of their assets intact.
- **CENTRAL VERSION HUB ("PORTFOLIO DESIGN SYSTEM VERSION CONTROL"):** The version hub is the central mission-control dashboard. It must be named **"Portfolio Design System Version Control"** and maintained at both:
  1. `versions/index.html` (accessible via `https://vighneshchopra.github.io/portfolio/versions/`)
  2. `portfolio_versions.html` (accessible via `https://vighneshchopra.github.io/portfolio/portfolio_versions.html`)
  The Hub MUST be updated every single time a new version or prototype is built, adding a direct card with live links before any push. All version cards must remain active and accessible.
