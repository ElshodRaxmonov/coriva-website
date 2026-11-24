# Coriva website

Static pages for https://coriva.uz. Plain HTML, CSS and JavaScript: no framework, no build step.

- **Source of truth:** this repository. Edit the files here directly. (The pages were first generated from the design prototype; that generator is no longer used for the live site.)
- **Hosting:** Cloudflare Worker with static assets (project `coriva`). Every push to `main` deploys to production, so work on a branch and open a pull request.
- **Status:** preview. The waitlist and contact forms are not open yet and send nothing. The privacy notice and medical disclaimer are drafts pending legal review (`noindex`).
- **Languages:** English. Uzbek is a client-side draft in `i18n.js`, pending review.
- Photographs are credited in each page footer. Video clips are illustrative concept footage.
