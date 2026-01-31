# TOOLS.md - Local Notes

## WhatsApp
- Status: Connected ✓ (switched from Telegram post-crash)
- Number: Own dedicated number
- Use for: Approval requests, proactive updates to AK

## Telegram (DEPRECATED - Post Crash)
- ~~Bot: Configured ✓~~
- ~~Channel: telegram~~
- ~~Chat ID: 31471725~~
- Switched to WhatsApp after system crash

## Email / Newsletter
- Gmail: rocco_bot@akashsenapaty.in (blocked by Workspace policy)
- **ListMonk**: https://monk.wowsumitra.com ✓
- ListMonk API: Configured ✓
- Main list: "Oct - last 6 months enquired" (26,679 subscribers)
- Tool: `tools/listmonk.py`
- Can: View campaigns, create drafts, check stats

## Skills Configured
- goplaces - Google Places API (for location searches)
- local-places - Local Google Places proxy
- nano-banana-pro - Gemini image generation
- openai-image-gen - OpenAI image generation
- openai-whisper-api - Audio transcription

## GitHub
- Repo: senapaty/clawdbot
- Deploy key: Configured ✓
- Backup: Daily at midnight IST (auto)
- Shared folder: /shared/ for collaborative markdown

## Missing / Needed
- [x] Brave Search API key (for travel news monitoring)
- [x] Email access - Gmail app password configured
- [x] GitHub access - clawdbot backup repo
- [ ] Browser access (for WOW Club website research)
- [ ] FBADMan repo access
- [ ] CMO repo access
- [ ] Social media access (Instagram, Facebook, X for WOW Club)

## WOW Club Contacts
- Simran: +91-99102-91169
- Upasana: +91-98109-57622
- Meenakchi: +91-98109-93423
- Shruti: +91-9910221609
- Namra: +91-98711-77890
- Anisha: +91-97179-29944

## Known Limitations

### Image Analysis
- **Issue:** `image` tool (openai/gpt-5-mini) returning empty responses
- **Workaround:** Use OCR text, external URLs, or manual description
- **When AK sends images:** Ask for text description or OCR output
- **Status:** Being investigated

### Web Search Rate Limits
- **Brave Search:** 1 request/sec, 2000 queries/month (free tier)
- **Symptom:** 429 errors after ~20 rapid queries
- **Strategy:** Batch searches, space out requests by 2-3 seconds

## Security / Secrets Management
- **NEVER commit secrets to git** — .env, API keys, passwords excluded from backup
- **Secrets stored in**: OpenClaw config (not in repo)
- **Backup excludes**: .env, *.key, *.pem, secrets/
- **Best practice**: Keep secrets in environment vars, not files

## WhatsApp Community
- URL: https://chat.whatsapp.com/D8T9H8RKGtl4DKwOflD6he
