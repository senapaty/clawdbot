# Personal Website - Project Documentation

## Project Overview

This is Akash Senapaty's personal website built with Hugo and the PaperMod theme. The site showcases professional experience in product management and gaming.

**Status**: ✅ Live and deployed on Cloudflare Pages
**Last Updated**: January 26, 2026
**Live URL**: Check Cloudflare Pages dashboard for your .pages.dev URL
**Note**: Project folder now synced via Dropbox with `.dropboxignore` configured

## Tech Stack

- **Hugo**: v0.152.2+extended
- **Theme**: PaperMod (https://github.com/adityatelange/hugo-PaperMod)
- **Hosting**: Cloudflare Pages
- **Repository**: git@github.com:senapaty/akashpersonal.git
- **Deployment**: Automatic on git push to main branch

## Directory Structure

```
/akashgg/
├── .dropboxignore              # Excludes build artifacts from Dropbox sync
├── .pages.toml                 # Cloudflare Pages build config
├── hugo.toml                   # Main site configuration (PaperMod settings)
├── CLAUDE.md                   # This documentation file
├── LICENSE                     # MIT License
├── content/                    # All site content (Markdown files)
│   ├── _index.md               # Homepage content
│   ├── about.md                # About page
│   ├── work.md                 # Work & Projects page
│   ├── now.md                  # Now page (current focus)
│   ├── contact.md              # Contact page
│   └── blog/                   # Blog posts directory
│       ├── _index.md
│       ├── art-of-pvp-design.md
│       ├── feature-launch-lessons.md
│       ├── from-mba-to-gaming.md
│       └── understanding-player-behavior.md
├── static/
│   ├── robots.txt              # Blocks all search engines
│   └── .geetkeep
├── themes/PaperMod/            # Theme files (directly included, not submodule)
├── layouts/partials/           # Custom layout overrides
│   ├── extend_head.html
│   └── header.html
├── assets/css/extended/        # Custom CSS
│   ├── custom.css
│   └── main.css
└── public/                     # Generated site (gitignored, dropboxignored)

```

## Navigation Structure

**Main Menu** (top nav):
1. Home (/)
2. About (/about)
3. Work (/work)
4. Now (/now)
5. Blog (/blog)
6. Contact (/contact)

**Footer Menu**:
- About
- Work
- Blog
- RSS (/index.xml)

**Social Links**:
- LinkedIn: https://in.linkedin.com/in/senapaty
- GitHub: https://github.com/akashgg
- Twitter: https://twitter.com/akashgg

## Content Pages

### Homepage (`content/english/_index.md`)
- Professional banner: "Product Manager | Gaming & Technology Enthusiast"
- Three feature sections:
  1. What I Do (skills and focus areas)
  2. Experience & Expertise (background and achievements)
  3. Let's Connect (call to action)
- Content based on LinkedIn profile

### About Page (`content/english/about/_index.md`)
- Personal introduction and career journey
- Education: MBA from Asian Institute of Management
- Notable work including Millionaire City
- Skills and interests
- Languages: English, Hindi, German

### Work Page (`content/english/work/_index.md`)
- Professional experience overview
- Key achievements (Millionaire City, Player Behavior Analysis)
- Skills & Expertise sections
- Education details
- Languages

### Now Page (`content/english/now/_index.md`)
- Current focus areas (Professional, Learning & Growth, Personal Interests)
- Location: Bengaluru, Karnataka, India
- Last updated: January 2026
- Inspired by Derek Sivers' now page concept

### Blog
- Directory: `content/blog/`
- **4 custom blog posts**:
  1. The Art of PvP Game Design (Jan 2026)
  2. 5 Hard-Learned Lessons from Launching Game Features (Dec 2025)
  3. From MBA to Gaming (Nov 2025)
  4. Understanding Player Behavior (Oct 2025)

### Contact
- Contact form page exists
- Form action currently set to "#" (needs configuration)
- Can integrate with Formspree or Airform.io

## Site Configuration

### Key Settings (hugo.toml)
- Base URL: "/"
- Title: "Akash Senapaty"
- Theme: "PaperMod"
- Default Language: English
- Profile Mode: Enabled (landing page with profile)
- Theme Switcher: Enabled (light/dark/auto)
- Reading Time: Enabled
- Breadcrumbs: Enabled
- Code Copy Buttons: Enabled
- **Search: Disabled** (JSON output removed to fix build issues)
- Outputs: HTML, RSS (no JSON)

### SEO Metadata
- Keywords: Product Management, Gaming, Technology, Portfolio
- Description: Personal website of Akash Senapaty - Product Manager specializing in gaming and technology
- Author: Akash Senapaty

## Running the Site

### Prerequisites
- Hugo Extended v0.144+ (currently using v0.152.2)
- Git with SSH keys configured for GitHub

### Development Server
```bash
hugo server
```
Then visit: http://localhost:1313/

The server will:
- Watch for file changes
- Auto-reload browser on changes
- Show draft posts (use -D flag)

### Build for Production (Local Testing)
```bash
hugo
```
Output: `public/` directory

### Deploy to Production
```bash
git add -A
git commit -m "Your commit message"
git push
```
Cloudflare Pages will automatically build and deploy in ~2 minutes.

## Important Notes

### Theme Installation Method
**PaperMod is included directly** (not as a git submodule). This means:
- All theme files are in `themes/PaperMod/` in your repository
- Any customizations you make to the theme are preserved
- No need to worry about submodule updates overwriting changes
- Theme updates require manual copying if desired

### Site Customization

**Site Config**: Edit `hugo.toml` for all main settings

**Social Links**: Edit `[[params.socialIcons]]` section in `hugo.toml`

**Navigation**: Edit `[[menu.main]]` section in `hugo.toml`

**Custom CSS**: Add to `assets/css/extended/custom.css`

**Custom Layouts**: Add to `layouts/partials/` to override theme defaults

**Custom Head Elements**: Edit `layouts/partials/extend_head.html`

### SEO & Search Engines
- `robots.txt` is configured to **block all search engines**
- Location: `static/robots.txt`
- Content: `User-agent: *` and `Disallow: /`
- To enable indexing, remove or modify this file

### Known Issues
- **Search functionality disabled**: JSON output was causing build errors with Hugo minify
- Can be re-enabled later by adding `"JSON"` back to `[outputs]` in hugo.toml
- For now, site navigation and blog listing provide access to all content

### Dropbox Sync Notes
- Project folder is now in Dropbox for multi-device access
- `.dropboxignore` file excludes build artifacts (`public/`, `resources/`, `.hugo_build.lock`)
- **Important**: When working across multiple machines, always `git pull` before starting work and `git push` when done
- Deployment still works the same: `git push` triggers Cloudflare Pages build

## Next Steps / TODO

### Content
- [ ] Add custom logo image (replace placeholder in `static/images/`)
- [ ] Add professional headshot/banner image
- [ ] Write first blog post
- [ ] Update contact form action URL (Formspree/Airform.io)
- [ ] Add more detailed project descriptions to Work page
- [ ] Add case studies or portfolio items

### Configuration
- [ ] Set proper baseURL for production deployment
- [ ] Add Google Analytics ID (if desired)
- [ ] Configure Disqus for blog comments (if desired)
- [ ] Set up proper favicon
- [ ] Update OG image for social sharing

### Deployment
- [x] ✅ Deployed to Cloudflare Pages
- [x] ✅ CI/CD pipeline active (auto-deploy on git push)
- [ ] Configure custom domain (optional)
- [x] ✅ Production build tested and working

### Optional Enhancements
- [ ] Add portfolio/projects section with case studies
- [ ] Integrate newsletter signup
- [ ] Add testimonials/recommendations
- [ ] Create custom 404 page
- [ ] Add reading time estimates to blog posts
- [ ] Set up analytics

## Reference Information

### LinkedIn Profile Summary
- Name: Akash Senapaty
- Location: Bengaluru, Karnataka, India
- Current Role: Complement 1
- Education: Asian Institute of Management (2008-2009)
  - Technology & Innovation Strategy
  - Consumer Behaviour
  - Social Marketing
  - Strategic Negotiations
- Languages: English, Hindi, German (elementary)
- Notable Project: Millionaire City (March 2012)
  - Developed new features with high engagement and monetization
- Expertise: Product management, player behavior analysis, game design, PvP mechanics

### Theme Resources
- Demo: https://adityatelange.github.io/hugo-PaperMod/
- GitHub: https://github.com/adityatelange/hugo-PaperMod
- Documentation: https://github.com/adityatelange/hugo-PaperMod/wiki

### Helpful Links
- Hugo Documentation: https://gohugo.io/documentation/
- Cloudflare Pages: https://developers.cloudflare.com/pages/
- Cloudflare Pages + Hugo Guide: https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/

---

## Session History

**January 19, 2026 - Initial Setup with HugoPlate**
1. Removed old Hugo site (Ghostwriter theme with retro blog posts)
2. Cloned HugoPlate theme from GitHub
3. Ran project setup script (`npm run project-setup`)
4. Installed Go 1.25.6 (required for Hugo Modules)
5. Configured site settings and navigation
6. Updated social links
7. Created all main content pages with personalized content from LinkedIn
8. Successfully started development server

**January 24, 2026 - Migration to PaperMod & Deployment**
1. **Theme Migration**: Switched from HugoPlate to PaperMod theme
   - Initially added as submodule (caused issues with customizations)
   - Converted to direct inclusion to preserve modifications
2. **Content Migration**: Restructured content from `content/english/` to `content/`
3. **Blog Posts**: Created 4 custom blog posts about gaming and product management
4. **SEO**: Added `robots.txt` to block all search engine indexing
5. **Git Setup**:
   - Removed old HugoPlate remote
   - Created new GitHub repository: `senapaty/akashpersonal`
   - Pushed code with PaperMod theme directly included
6. **Cloudflare Pages Deployment**:
   - Configured build settings (Hugo v0.152.2)
   - Fixed build errors by removing `--minify` flag
   - Disabled JSON output (search functionality) to resolve parsing errors
   - Successfully deployed to Cloudflare Pages
7. **Deployment Pipeline**: Automatic builds on git push to main branch

**January 26, 2026 - Project Cleanup & Dropbox Optimization**
1. **Moved project to Dropbox**: Relocated from local folder to Dropbox for multi-device sync
2. **Removed all HugoPlate remnants**:
   - Deleted directories: `.devcontainer/`, `.github/`, `.sitepins/`, `scripts/`, `i18n/`, `content_backup/`, `images/`
   - Removed unused deployment configs: `amplify.yml`, `netlify.toml`, `vercel.json`, `vercel-build.sh`, `.gitlab-ci.yml`, `_redirects`
   - Removed HugoPlate documentation: `readme.md`, `theme.toml`, `DEVELOPER_DOCS.md`, `MIGRATION_NOTES.md`
   - Removed unnecessary config: `.jshintrc`
3. **Created `.dropboxignore`**: Excludes build artifacts to optimize Dropbox sync
4. **Current state**: Clean project structure with only PaperMod theme and essential files

**Current Status**: ✅ Site is live on Cloudflare Pages with automatic deployments configured. Project is clean and optimized for Dropbox sync.

---

*This documentation was created to preserve project context and enable seamless continuation of work.*
