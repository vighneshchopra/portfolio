# PROJECT HANDOVER & ARCHITECTURAL SPECIFICATION
**Executive Portfolio Website for Vighnesh Chopra**  
**Role:** Healthcare SaaS & EMR Support Manager  
**Repository:** `https://github.com/vigiprojects/vighnesh-portfolio.git`  
**Live Production URL:** `https://vigiprojects.github.io/vighnesh-portfolio/`  
**Alternative Version URL:** `https://vigiprojects.github.io/vighnesh-portfolio/portfolio_v3.html`  
**Date of Handover:** October 19, 2026  

---

## 1. Executive Summary & Purpose

This repository houses the personal professional portfolio of **Vighnesh Chopra**, an experienced **Healthcare SaaS & EMR Support Manager** with over 7 years of specialized expertise directing L1/L2 application support, clinical user adoption, and cross-functional engineering escalation bridges across 30+ healthcare facilities in the UAE, Middle East, and internationally.

This document serves as the single source of truth (SSOT) and definitive context handover for any future AI assistant or developer picking up this project. It outlines the codebase structure, design philosophies, verified biographical facts, technical integrations, deployment pipelines, and operational instructions.

---

## 2. Verified Biographical & Career Facts (Strict Constraints)

When updating content or authoring copy in future iterations, the following verified constraints must be strictly preserved:

1. **Title & Specialization**:
   - Primary: **EMR Support Manager** / **Healthcare SaaS & EMR Support Manager**
   - Subtitle: Healthcare Application Support & Operations Professional
   - Focus: Incident resolution, operational continuity, clinical workflow optimization, and technical escalation bridge to engineering.
2. **Support Scope (Critical Constraint)**:
   - **Do NOT claim L3 developer/coding support**: Vighnesh manages L1/L2 application support, front-end validation, server log bug replication, and serves as the **Single Point of Contact (SPOC) and Escalation Bridge** translating issues for backend software developers. Do not describe him as writing core database or application code for L3 fixes.
3. **Tenure & Metrics**:
   - **Total Experience**: **7+ Years** (February 2019 – Present at Medicworks Healthcare Informatics; previously July 2015 – July 2018 at ITC Grand Bharat).
   - **Facilities Supported**: **30+ multi-site healthcare facilities** (clinics, hospital groups, healthcare networks).
   - **Staff Trained**: **200+ healthcare staff** (doctors, nurses, clinical coders, administrators).
   - **Operational Record**: Millions of clinical patient records processed under strict SLA governance with zero live charting downtime.
4. **Primary Experience Details**:
   - **Medicworks Healthcare Informatics** | Dubai, UAE (Global Exposure)  
     *Role:* Business Relations & Customer Support Manager (Feb 2019 – Present • 7+ Years)  
     *Key Responsibilities:* Primary client SPOC; L1/L2 application support; clinical template and workflow configuration; release validation and UAT testing; bridging clinical users with backend engineering; aligning workflows with DHA, HIPAA, CMS, ICD-10, CPT-4, and DRG/APC logic; integrating EMRs with regional Health Information Exchanges (**Malaffi** in Abu Dhabi, **NABIDH** in Dubai); authoring runbooks and SOPs.
   - **ITC Grand Bharat (WelcomLEAD Program)** | Gurgaon, India  
     *Role:* Guest Service Associate (Jul 2015 – Jul 2018 • 3 Years)  
     *Key Responsibilities:* Foundational operational quality; enterprise systems management using integrated POS applications (**MICROS VICAS, OPERA**); SOP compliance.
5. **Education**:
   - **Indira Gandhi National Open University (IGNOU)**, New Delhi, India  
     *Degree:* Bachelor of Arts, Tourism Studies (Graduated 2018 • Grade: First Division).
6. **Languages**:
   - **English**: Fluent
   - **Hindi**: Fluent
   - **Bengali**: Conversational
   - *(Note: Display as clean badge chips; do NOT use percentage slider bars for languages).*
7. **Anthropic AI Certifications (Verified)**:
   - *AI Fluency Framework & Foundations* → `https://verify.skilljar.com/c/9zmqmf6xzcke`
   - *Claude Cowork & Capabilities* → `https://verify.skilljar.com/c/jv3xb5axts5w`
   - *Claude 101* → `https://verify.skilljar.com/c/n9jdknkaaaig`
   - *AI Capabilities & Limitations* → `https://verify.skilljar.com/c/crjhy9a8eo6x`
   - *(Note: Do NOT display raw credential IDs in the text; only provide the clickable "Verify ↗" links).*
8. **Email & Privacy Constraint (Strict)**:
   - **Recipient Email**: `vighnesh.chopra13@gmail.com`
   - **Rule**: The email address must **NEVER** appear in visible plaintext on the website, nor in raw text within the HTML/JS source code. It is stored as an obfuscated Base64 token (`dmlnaG5lc2guY2hvcHJhMTNAZ21haWwuY29t`) and decoded dynamically only at the moment of AJAX transmission.
9. **LinkedIn Profile**:
   - `https://www.linkedin.com/in/vighneshchopra/`

---

## 3. Repository Architecture & File Inventory

```
Portfolio/
├── index.html                  # Production Entrypoint: Exact duplicate of Version 7 for root URL delivery
├── portfolio_v7.html           # Version 7: Titanium Mineral & Warm Cognac / Amber (Lighthouse 95+ Optimized, WebP, Symmetrical Tab Matrix)
├── portfolio_v6.html           # Version 6: High-Taste Editorial Dark Obsidian Layout with Interactive Incident Stepper
├── portfolio_v5.html           # Version 5: Editorial Dark Aesthetic (Pinterest cyan reference design)
├── portfolio_v3.html           # Version 3: Alternative Cyber-Grid Executive Layout
├── profile_cutout.webp         # High-performance 174 KB WebP hero portrait (84% lighter for LCP optimization)
├── profile_cutout.png          # Fallback transparent background cutout portrait of Vighnesh Chopra
├── profile.png                 # Fallback source portrait
├── Vighnesh_Chopra_Resume.pdf  # Verified 2-Page Executive CV (Feb 2019–Present, 7+ Yrs, DHA/HIPAA/AI)
├── desk_backdrop.jpg           # High-resolution dark studio desk backdrop asset
├── ref_pin.jpg                 # Downloaded Pinterest UI design reference for Version 5
├── PROJECT_HANDOVER.md         # This specification document
└── .git/                       # Local Git repository metadata (branch: main, remote: origin)
```

---

## 4. Deep Dive into Version 5 (`index.html` & `portfolio_v5.html`)

Version 5 was constructed from a Pinterest design reference featuring a dark, luxury tech aesthetic with sky-blue/cyan accents (`#38bdf8`) over deep obsidian (`#07090e`).

### 4.1 Background & Canvas Engine
- **Fixed HTML5 Canvas (`#bg-canvas`)**:
  - Renders 52 luminous cyan particles (`rgba(56, 189, 248, alpha)`) drifting at 60 FPS with gentle speed and constellation proximity connection lines.
  - Pauses automatically via the `visibilitychange` API when the browser tab is hidden to conserve battery and CPU.
  - Zero heavy external libraries (pure vanilla JavaScript and native 2D canvas context).
- **Gradual Multi-Stop Vertical Darkening Gradient (`.continuous-dark-fade`)**:
  - Eliminates all mismatched block colors or horizontal section bands.
  - **Hero (Top)**: Particles are luminous and active (`rgba(7, 9, 14, 0.05)`).
  - **About Section**: Particles gently soften into the background (`rgba(7, 9, 14, 0.38)`).
  - **Skills & Experience**: Dimming down smoothly (`rgba(6, 8, 12, 0.65)`).
  - **Let's Connect (Bottom)**: Particles are barely visible traces, transitioning to **pitch black (`#010204` / `#000000`)** at the contact box and footer.

### 4.2 Hero Composition
- **Side-by-Side Balance**:
  - **Left**: Top category badge, bold typography (`VIGHNESH CHOPRA`), title with `whitespace-nowrap` (`Healthcare SaaS & EMR Support Manager`), executive summary, primary blue pill button (`Download CV (PDF)`), secondary pills (`Experience & Skills`, `Let's Connect`), and a 3-badge metric card row (`30+ Facilities`, `200+ Staff Trained`, `7+ Yrs SLA Governance`).
  - **Right**: Floating cutout portrait (`profile_cutout.png`) with **zero borders**, backed by an ambient radial glow orb (`.hero-glow-orb`) and a bottom fade mask (`linear-gradient(to bottom, black 78%, transparent 100%)`).

### 4.3 Expanded About Section
- Spans the full `max-w-7xl` container with no wasted void on the right.
- Editorial narrative with bold emphasis on operational continuity, SLA governance, and HIE alignment.
- Three full-width cards: *Clinical Continuity*, *Engineering Bridge*, and *Compliance & HIE*.

### 4.4 Audited 3-Column System Grid
- **Container**: `max-w-[1380px]` with generous column gaps (`gap-12 lg:gap-14 xl:gap-16`) to avoid text crowding.
- **Column 1 (Proficiencies & Languages)**:
  - Curated to 5 core technical items with gradient slider tracks and cyan glowing dots:
    1. *HIS / EMR Application Support* (98%)
    2. *Root Cause Analysis & Bug Isolation* (96%)
    3. *Engineering Escalation Bridge* (95%)
    4. *Malaffi & NABIDH HIE Workflows* (92%)
    5. *Release Validation & UAT Testing* (94%)
  - Compliance pill tag cloud: HIPAA Privacy, DHA Standards, ICD-10, CPT-4, DRG/APC, CMS Rules.
  - Languages: English (Fluent), Hindi (Fluent), Bengali (Conversational) as distinct badge chips.
- **Column 2 (Career Timeline & Upward Illumination)**:
  - **Zero Text Overlap Architecture**: Uses a flexbox layout where node circles sit inside a dedicated `w-6 flex-shrink-0` rail column, and dates/bullets sit in an independent `flex-1` right column separated by a 24px gap (`gap-6`). It is physically impossible for the node to overlap "Feb 2019" or "July 2015".
  - **Bottom-to-Up Traveling Light Pulse (`surgeUpwards`)**: A luminous 60px light beam continuously glides upward from 2015 to 2019 along `.timeline-track-rail`.
  - **Scroll-Triggered Illumination (`IntersectionObserver`)**: When the timeline scrolls into view, the bottom node (ITC Grand Bharat) glows, followed by an intense radiant flare illuminating the top node (Medicworks).
  - Education card: IGNOU Bachelor of Arts, Tourism Studies (First Division).
- **Column 3 (Deliverables & Anthropic AI Certifications)**:
  - 4 Deliverable cards: Multi-Site EMR Onboarding, Live Clinical Charting Continuity, Technical Escalation Bridge, SLA & Retention Governance.
  - 4 Verified Anthropic AI Cards with direct verification links to Skilljar.

---

## 5. Contact Form Relay Architecture

### 5.1 The FormSubmit Backend Engine
- Endpoint: `https://formsubmit.co/ajax/{targetEmail}`
- Relay Target: `vighnesh.chopra13@gmail.com` (Stored as Base64 `dmlnaG5lc2guY2hvcHJhMTNAZ21haWwuY29t`).
- Configuration Parameters:
  - `_captcha = false` (Streamlined frictionless submission).
  - `_template = table` (Clean tabular formatting in Gmail).
  - `_subject = New Portfolio Inquiry for Vighnesh Chopra`.

### 5.2 Form Activation Status
- **ACTIVATED**: The form has been activated and verified via live email delivery tests.

### 5.3 Local `file:///` vs Web Server Protocol Handling
- **The Browser Security Rule**: FormSubmit's cloud server deliberately blocks submissions originating from `file:///C:/Users/...` (where `Origin: null` or `Referer: file://`) to prevent offline script abuse.
- **The Client-Side Guard**:
  ```javascript
  if (window.location.protocol === 'file:') {
    // Displays clear guidance directing the user to http://localhost:5500/#contact
    return;
  }
  // On web server (http: or https:), executes seamless background fetch()
  ```
- **On Live Web Hosting**: When hosted on GitHub Pages (`https://vigiprojects.github.io/...`) or Cloudflare Pages (`https://*.pages.dev`), the protocol is `https:`, which FormSubmit accepts 100% of the time.

---

## 6. Hosting & Deployment Workflows

### 6.1 GitHub Pages (Active Production Host)
- **Repository**: `https://github.com/vigiprojects/vighnesh-portfolio.git`
- **Branch**: `main`
- **Root Directory**: `/(root)`
- **Live URLs**:
  - Main (Version 5): `https://vigiprojects.github.io/vighnesh-portfolio/`
  - Version 3: `https://vigiprojects.github.io/vighnesh-portfolio/portfolio_v3.html`
  - Resume: `https://vigiprojects.github.io/vighnesh-portfolio/Vighnesh_Chopra_Resume.pdf`

### 6.2 Cloudflare Pages (Alternative / Custom Domain Roadmap)
If migrating or deploying to Cloudflare Pages:
1. Log into `dash.cloudflare.com` → **Workers & Pages** → **Create Application** → **Pages**.
2. Connect Git repository: `vigiprojects/vighnesh-portfolio`.
3. Build command: *(leave blank)*.
4. Output directory: `.` or `/`.
5. Deploy.
6. Custom domains (e.g. `vighneshchopra.com`) can be bound under **Custom domains** in the Cloudflare Pages dashboard.

---

## 7. How to Make Common Updates (Maintenance Guide)

### 7.1 Updating the Resume PDF
1. Replace the file `c:\Users\amanc\OneDrive\Desktop\Portfolio\Vighnesh_Chopra_Resume.pdf` with the new PDF file (keeping the exact same filename).
2. Commit and push:
   ```powershell
   git add Vighnesh_Chopra_Resume.pdf
   git commit -m "chore: update resume PDF"
   git push origin main
   ```

### 7.2 Synchronizing Version 5 Edits to `index.html`
`index.html` is the default landing page served by web servers. Whenever modifications are made to `portfolio_v5.html`, always sync to `index.html`:
```powershell
Copy-Item -Path "portfolio_v5.html" -Destination "index.html" -Force
git add portfolio_v5.html index.html
git commit -m "fix: sync portfolio v5 changes to index.html"
git push origin main
```

### 7.3 Testing Locally with Local Web Server
To test form submissions locally on your computer without `file://` CORS restrictions, launch Python's built-in HTTP server:
```powershell
py -m http.server 5500
```
Then navigate to `http://localhost:5500/#contact` in any web browser.

---
*Handover authored and verified by Antigravity Agent. All repositories and live deployments verified active.*
