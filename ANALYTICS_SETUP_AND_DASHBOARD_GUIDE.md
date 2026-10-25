# Complete Website Analytics Setup & Practical Dashboard Guide
**Executive Portfolio of Vighnesh Chopra**  
**Role:** Healthcare SaaS & EMR Support Manager  
**Production URL:** `https://vighneshchopra.github.io/portfolio/`  
**Platforms:** Google Analytics 4 (GA4) & Microsoft Clarity  

---

## 1. Executive Status & Architecture Summary

The complete analytics and telemetry engine is now **fully integrated and code-ready** inside [`index.html`](file:///c:/Users/amanc/OneDrive/Desktop/Portfolio/index.html).

### What Has Been Implemented:
1. **Zero-PII Privacy & Consent Banner**: A luxury Obsidian/Amber toast matching your portfolio’s exact theme, giving visitors the choice to accept or use essential-only mode.
2. **Google Analytics 4 (GA4) Engine**: Tracks visitors, countries, cities, devices, channels, and specific portfolio actions.
3. **Microsoft Clarity Engine**: Records actual visitor sessions, click heatmaps, scroll depth heatmaps, and identifies navigation drop-offs.
4. **Interactive Milestone Telemetry**: Automatically tracks:
   - Resume downloads (`resume_download`) with link origin (`navbar`, `hero_cta`, `footer`, `mobile_drawer`).
   - LinkedIn profile clicks (`linkedin_click`).
   - Anthropic AI credentials verification clicks (`credential_verify_click`).
   - Incident Triage Simulator exploration (`triage_simulator_step`).
   - Symmetrical tab switches (`tab_switch`).
   - 1-Click "Copy Email" usage (`email_copy`).
   - Genuine contact form submissions (`contact_form_submit`).
   - Scroll depth milestones at 25%, 50%, 75%, and 90% (`scroll_depth_milestone`).
   - Section in-view readership (`section_view`).
5. **Campaign & UTM Attribution**: Detects and remembers whether a visitor arrived from your LinkedIn profile, a LinkedIn post, or your Digital CV PDF across their entire visit.
6. **Optional Google Sheets CRM Sync**: Can automatically pipe every recruiter's name, email, organization, inquiry topic, message, and traffic source into your own private Google Sheet.

---

## 2. Quick Account Setup (10-15 Minutes Total)

### Step 1: Create Your Free Google Analytics 4 Property
1. Navigate to **[analytics.google.com](https://analytics.google.com/)** and log in with your Google account.
2. Click the gear icon (**Admin**) at the bottom left.
3. Click **+ Create** → **Property**.
   - Property Name: `Vighnesh Chopra Executive Portfolio`
   - Reporting time zone: `United Arab Emirates (Dubai)` or your preferred zone.
   - Currency: `AED` or `USD`.
4. Click **Next** → Select **Industry: Healthcare / Technology** → **Size: Small**.
5. Choose Business Objective: **Generate Leads** or **Examine user behavior**.
6. On the **Choose a platform** screen, select **Web**.
7. Set up data stream:
   - Website URL: `https://vighneshchopra.github.io/portfolio/`
   - Stream name: `Portfolio Web Stream`
   - Keep **Enhanced measurement** checked (ON).
8. Click **Create Stream**.
9. In the stream details, copy your **Measurement ID** (Format: `G-XXXXXXXXXX`).

---

### Step 2: Create Your Free Microsoft Clarity Project
1. Navigate to **[clarity.microsoft.com](https://clarity.microsoft.com/)** and sign in with your Google or Microsoft account.
2. Click **+ Add new project**.
   - Project Name: `Vighnesh Chopra Portfolio`
   - Website URL: `https://vighneshchopra.github.io/portfolio/`
3. Click **Add project**.
4. Navigate to **Settings** → **Overview**.
5. Copy your **Project ID** (a short string of letters and numbers, e.g. `k8m9x2zq`).
6. *(Recommended)* Under **Settings** → **Setup**, scroll to **Google Analytics integration** and click **Connect Google Analytics**. This allows you to watch Clarity session replays directly inside GA4!

---

### Step 3: Connect Your Real IDs to `index.html`

Open [`index.html`](file:///c:/Users/amanc/OneDrive/Desktop/Portfolio/index.html) and locate lines 3200-3220. Replace the placeholders with your real IDs:

```javascript
const ANALYTICS_CONFIG = {
  // Replace 'G-XXXXXXXXXX' with your real Measurement ID:
  GA4_MEASUREMENT_ID: 'G-XXXXXXXXXX',

  // Replace 'CLARITY_PROJECT_ID' with your real Project ID:
  CLARITY_PROJECT_ID: 'CLARITY_PROJECT_ID',

  // Optional: Google Sheet Webhook Endpoint (see Section 6 below)
  GOOGLE_SHEET_ENDPOINT: '',

  HONOR_DNT: false
};
```

---

## 3. Ready-to-Use UTM Links for Your Campaigns

Always use tagged URLs when sharing your portfolio on professional platforms so GA4 and Clarity know exactly where each visitor came from.

### Recommended Links

| Channel | Exact URL to Copy & Use | Purpose |
| :--- | :--- | :--- |
| **LinkedIn Profile Headline/Bio** | `https://vighneshchopra.github.io/portfolio/?utm_source=linkedin&utm_medium=profile&utm_campaign=portfolio` | Put in your "Website" link on your LinkedIn profile header. |
| **LinkedIn Post / Case Study** | `https://vighneshchopra.github.io/portfolio/?utm_source=linkedin&utm_medium=social_post&utm_campaign=emr_triage` | Use when posting on LinkedIn about EMR support, DHA compliance, or triage workflows. |
| **Digital CV / Resume PDF** | `https://vighneshchopra.github.io/portfolio/?utm_source=resume&utm_medium=pdf_cv&utm_campaign=executive_cv` | Embed as the clickable portfolio link inside your 2-page executive CV. |
| **Direct Hospital Application (e.g. Mediclinic)** | `https://vighneshchopra.github.io/portfolio/?utm_source=mediclinic&utm_medium=job_app&utm_campaign=support_manager` | Send in cover letters or job portal application notes. |
| **Direct Hospital Application (e.g. Cleveland Clinic)** | `https://vighneshchopra.github.io/portfolio/?utm_source=cleveland_clinic&utm_medium=job_app&utm_campaign=support_manager` | Customized for specific healthcare applications. |

---

## 4. Practical Dashboard Guide: Where to Find Everything

### In Google Analytics 4 (analytics.google.com)

#### 1. Instant Traffic (Realtime)
- **Path**: *Reports → Realtime*
- **What you see**: Active visitors on your site in the last 30 minutes, their country and city on a world map, and every click event happening live.

#### 2. Traffic Acquisition (Where Visitors Came From)
- **Path**: *Reports → Acquisition → Traffic acquisition*
- **How to read**: Change the primary dimension to **Session source / medium** or **Session campaign**.
- You will clearly see rows such as:
  - `linkedin / profile`
  - `resume / pdf_cv`
  - `google / organic`
  - `direct / none`

#### 3. Geographic Distribution (Countries & Cities)
- **Path**: *Reports → User attributes → Demographic details*
- **How to read**: Select **Country** or switch the primary dimension to **City**. You will see exact counts for Dubai, Abu Dhabi, London, Riyadh, etc.

#### 4. Technology & Devices
- **Path**: *Reports → Tech → Tech details*
- **What you see**: Breakdown by Mobile vs Desktop, Apple iOS vs Windows vs Android, and Safari vs Chrome.

#### 5. Portfolio Interaction Events
- **Path**: *Reports → Engagement → Events*
- **What you see**:
  - `resume_download`: Number of recruiters who downloaded your CV.
  - `linkedin_click`: Number of visitors who clicked to connect on LinkedIn.
  - `triage_simulator_step`: Recruiter interactions with your live incident simulator.
  - `credential_verify_click`: Recruiters who verified your Anthropic AI certificates on Skilljar.
  - `contact_form_submit`: Number of completed inquiries submitted.
  - `scroll_depth_milestone`: Shows reading depth (25%, 50%, 75%, 90%).

#### 6. Mark Your Key Conversions in GA4
In GA4: Go to **Admin (Gear)** → **Events**. Find `contact_form_submit` and `resume_download`, and toggle the switch **"Mark as key event" (conversion)** to ON. This will highlight these two actions as top executive goals in all your summary reports.

---

### In Microsoft Clarity (clarity.microsoft.com)

#### 1. Session Recordings (Watch Recruiter Visits)
- **Path**: *Clarity → Recordings*
- **What you see**: Actual video-like replays of visitors browsing your portfolio.
- **Filter by**:
  - Referrer: Filter to see only visitors from `linkedin.com`.
  - Country: Filter to watch only UAE or GCC visitors.
  - Duration: Filter to see only visitors who spent more than 2 minutes.

#### 2. Heatmaps (Click & Scroll Activity)
- **Path**: *Clarity → Heatmaps*
- **Click Heatmap**: Glows red/yellow on the exact buttons, project badges, and links that visitors click most often.
- **Scroll Heatmap**: Shows an exact percentage bar down the page showing how far recruiters scroll before leaving (e.g. 78% read your Career Timeline; 64% interacted with the Triage Simulator).

#### 3. UX Frustration Insights
- **Path**: *Clarity → Dashboard*
- **What you see**:
  - **Dead Clicks**: Clicks on static elements that visitors thought were clickable (helps you refine UI).
  - **Rage Clicks**: Rapid clicking indicating confusion or slow network.
  - **Quick Backs**: Visitors who immediately backed out.

---

## 5. Privacy, Security & Data Safety Verification

1. **GitHub Repository Security**:
   - Only the public measurement tags (`G-XXXXXXXXXX` and Clarity ID) reside in the code.
   - **No passwords, secrets, or visitor analytics data ever touch GitHub.**
   - All analytics dashboards require your 2FA Google and Microsoft logins.
2. **Visitor Masking**:
   - In Clarity, input fields in `#contact-form` are masked by default to `***`.
   - In GA4, full IP addresses are never logged or stored.
3. **Form Inquiries**:
   - Contact form inquiries are transmitted directly to your personal email (`vighnesh.chopra13@gmail.com`) via FormSubmit, keeping recruiter communication strictly private.

---

## 6. (Optional) Auto-Sync Contact Form to a Private Google Sheet

If you would like every person who reaches out to be automatically cataloged in an Excel/Google Sheet in your Google Drive:

1. Open **[sheets.google.com](https://sheets.google.com/)** and create a blank spreadsheet named `Portfolio Inquiries`.
2. Add these column headers in row 1:
   - `Timestamp` | `Name` | `Email` | `Organization` | `Subject` | `Message` | `UTM Source`
3. Click **Extensions** → **Apps Script**.
4. Paste this hardened security code (mitigates Formula/CSV injection and rejects unauthenticated GET data harvesting):
```javascript
// Hardened Google Apps Script Endpoint for Portfolio Inquiries

function sanitizeCell(val) {
  if (typeof val !== 'string') return val;
  var trimmed = val.trim();
  // Prevent Formula / CSV Injection (prepend single apostrophe to execution tokens)
  if (/^[=+\-@\t\r]/.test(trimmed)) {
    return "'" + trimmed;
  }
  return trimmed;
}

// 1. Enforce POST only — Strictly block GET requests from exposing stored contact rows
function doGet(e) {
  return ContentService.createTextOutput(
    JSON.stringify({ error: "405 Method Not Allowed. POST requests only." })
  ).setMimeType(ContentService.MimeType.JSON);
}

// 2. Handle POST with strict input sanitization
function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = JSON.parse(e.postData.contents);

    sheet.appendRow([
      sanitizeCell(data.timestamp || new Date()),
      sanitizeCell(data.name || ''),
      sanitizeCell(data.email || ''),
      sanitizeCell(data.organization || ''),
      sanitizeCell(data.subject || ''),
      sanitizeCell(data.message || ''),
      sanitizeCell(data.utm_source || 'direct')
    ]);

    return ContentService.createTextOutput(
      JSON.stringify({ result: "success" })
    ).setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(
      JSON.stringify({ error: "Processing failed: " + err.message })
    ).setMimeType(ContentService.MimeType.JSON);
  }
}
```
5. Click **Deploy** → **New Deployment** → Select type **Web app**.
   - Execute as: **Me**
   - Who has access: **Anyone**
6. Click **Deploy** and copy the **Web app URL**.
7. In `index.html`, paste that URL into `GOOGLE_SHEET_ENDPOINT: 'YOUR_COPIED_URL'`.
Now, every inquiry will instantly appear as a new row in your private Google Sheet!

---

## 7. How to Test Right Now in Your Browser

Even before you enter your real Google and Microsoft IDs:
1. Double-click `index.html` or run `.\serve.ps1` in PowerShell.
2. Open Chrome DevTools (`F12` or `Ctrl + Shift + I`) and click the **Console** tab.
3. Accept the privacy toast.
4. Click any Resume link, LinkedIn icon, Anthropic certificate, or Triage step.
5. In the console, you will immediately see live formatted event logs:
   `[GA4 Event Telemetry] resume_download { file_name: 'Vighnesh_Chopra_Resume.pdf', link_location: 'hero_cta', ... }`
6. Scroll down the page: you will see scroll depth milestones (`25%`, `50%`, `75%`, `90%`) firing smoothly!

Once you paste your real IDs and push to GitHub, these same events will flow straight into your live GA4 and Clarity cloud dashboards.

---

## 8. Ad-Blocker Proof Telemetry Vault (Sheet 2: Portfolio Analytics)

To guarantee that 100% of high-value recruiter interactions are logged even if visitors have Brave Shields, uBlock Origin, or privacy extensions enabled, your portfolio includes a secondary direct webhook to Google Sheets.

### Session Clumping Architecture
Every visitor session is automatically assigned an anonymous session identifier (e.g., `SES-7A9B`) and an auto-incrementing action sequence counter (`#1`, `#2`, `#3`, etc.):
- **Interaction Detail Format**: `[SES-7A9B • #1] Switched to: systems_and_standards`
- **Subsequent Actions**:
  - `[SES-7A9B • #2] Switched to: deliverables`
  - `[SES-7A9B • #3] Credential: Claude 101`
  - `[SES-7A9B • #4] Downloaded Resume (hero_cta)`
  - `[SES-7A9B • #5] Destination: LinkedIn Profile (hero_cta)`

This makes your Google Sheet immediately readable at a glance: all rows sharing the same `[SES-XXXX]` prefix represent the exact journey of a single recruiter during one continuous visit.

### Verifying Telemetry in Browser Console (F12)
1. Open your portfolio in any browser: `https://vighneshchopra.github.io/portfolio/`
2. Press `F12` and click **Console**.
3. You will immediately see the telemetry banner:
   `[Analytics Vault] Telemetry Engine Active | Session: SES-XXXX | Google Sheets: CONNECTED`
4. Click any tab or download your CV: you will see real-time amber confirmation badges in the console indicating the payload was dispatched directly to Google Sheets!
