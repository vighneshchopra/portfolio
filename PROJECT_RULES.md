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
- Only WebP/SVG optimized assets directly referenced by `index.html` may be staged in the production repository.
- All drafting prompts, cutouts, 3D experiments, and reference files must remain in external directories excluded by `.gitignore`.

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
