# Alternatives to OpenRouter for Multi-Modal AI

**Date:** January 31, 2026  
**Purpose:** Options for image understanding, voice transcription, and image generation without OpenRouter

---

## Current Situation

**What's Broken:**
- `image` tool uses `openai/gpt-5-mini` which returns empty responses
- This is the built-in OpenClaw image analysis tool

**What's Already Working:**
- ✅ Text/chat (Kimi Code)
- ✅ Image GENERATION (Gemini via nano-banana-pro skill)
- ✅ Voice TRANSCRIPTION (OpenAI Whisper API)
- ✅ Web search (Brave)

---

## 1. Image Understanding (Analyzing Screenshots/Photos)

### Option A: Google Gemini (RECOMMENDED - Already Configured!)

**Status:** API key already in config (`nano-banana-pro` skill)

**How to use for image analysis:**

```bash
# Use the nano-banana-pro skill with image input
# The skill can analyze images as well as generate them
```

**But wait** - the skill is designed for generation, not analysis. 

**Better approach:** Add Gemini as an image model provider directly.

**Pros:**
- ✅ Already have API key configured
- ✅ Gemini 1.5 Flash/Pro have excellent vision
- ✅ Fast and cheap
- ✅ Native Google integration

**Cons:**
- Need to configure as image model (requires config change)
- Or use via skill script workaround

**Cost:** ~$0.0015-0.003 per image

---

### Option B: Anthropic Claude (Claude 3 with Vision)

**What you need:**
- Anthropic API key ($5 free credit to start)
- Add to OpenClaw config

**Pros:**
- Excellent vision capabilities
- Very good at reading text in images
- Good at charts, diagrams, UI mockups

**Cons:**
- Requires new API key
- More expensive than Gemini (~$0.008-0.024 per image)
- Needs config changes

**Cost:** ~$0.008-0.024 per image

---

### Option C: Local Models (Ollama + LLaVA)

**What you need:**
- Ollama installed locally
- LLaVA or similar vision model
- Decent hardware (GPU optional but recommended)

**Setup:**
```bash
# Install ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull vision model
ollama pull llava

# Configure OpenClaw to use local model
```

**Pros:**
- ✅ Completely free (no API costs)
- ✅ Private (images stay on your machine)
- ✅ Works offline

**Cons:**
- Requires setup on your Pi (may be slow without GPU)
- Lower quality than cloud models
- Slower inference

**Cost:** FREE (runs locally)

---

### Option D: WhatsApp Native OCR (Workaround)

**For text-heavy images:**

1. **iPhone users:**
   - Long press image → "Copy Text"
   - Paste text in WhatsApp

2. **Android users:**
   - Google Lens → "Copy text"
   - Or use "Select" tool in Google Photos

3. **Send me the OCR text instead of image**

**Pros:**
- ✅ No config changes needed
- ✅ Works right now
- ✅ Free

**Cons:**
- Only works for text, not general image understanding
- Manual step for you

---

## 2. Voice Notes (Transcription)

### Option A: OpenAI Whisper API (ALREADY CONFIGURED!)

**Status:** ✅ Already working in your setup

**What you have:**
```json
"openai-whisper-api": {
  "apiKey": "sk-proj-..."
}
```

**How to use:**
- Send voice note via WhatsApp
- OpenClaw should automatically transcribe using Whisper

**If it's not working:**
- May need to configure WhatsApp to handle voice media
- Or I can call the skill directly

**Cost:** ~$0.006 per minute of audio

---

### Option B: WhatsApp Native Voice-to-Text

**Built into WhatsApp:**

1. **Android:**
   - Tap and hold voice message
   - Tap "Transcribe"

2. **iPhone:**
   - Play voice message
   - Tap transcript button (if available in your region)

**Pros:**
- ✅ Free
- ✅ No setup
- ✅ Works immediately

**Cons:**
- Only available on some devices/regions
- Quality varies

---

### Option C: Google Speech-to-Text

**What you need:**
- Google Cloud account
- Enable Speech-to-Text API
- Add credential to OpenClaw

**Pros:**
- Excellent accuracy
- Supports multiple languages
- Good for Indian languages

**Cons:**
- Requires Google Cloud setup
- Config changes needed

**Cost:** ~$0.024 per minute

---

## 3. Image Generation (Already Working!)

### Option A: Nano Banana Pro (Gemini) - ✅ CONFIGURED

**Status:** API key already in your config!

**How to use:**
```bash
# Generate image
uv run /path/to/generate_image.py --prompt "a cat playing guitar" --filename "cat-guitar.png"
```

**Or via skill:**
Just ask me: "Generate an image of..."

**Pros:**
- ✅ Already configured (GEMINI_API_KEY present)
- ✅ High quality (Gemini 3 Pro Image)
- ✅ Can edit existing images too
- ✅ Up to 4K resolution

**Cons:**
- May need credits on Google AI Studio

**Cost:** Free tier available, then pay-as-you-go

---

### Option B: OpenAI DALL-E (ALREADY CONFIGURED)

**Status:** Configured but may need credits

```json
"openai-image-gen": {
  "apiKey": "sk-proj-..."
}
```

**Pros:**
- ✅ Already configured
- Excellent quality

**Cons:**
- Requires OpenAI credits ($)
- More expensive than Gemini

**Cost:** $0.02-0.08 per image

---

## Summary: What Works Without OpenRouter

| Feature | Current Status | Alternative | Needs Config Change? |
|---------|---------------|-------------|---------------------|
| **Image UNDERSTANDING** | ❌ Broken (gpt-5-mini) | Gemini Vision / Claude / Local | Yes |
| **Voice TRANSCRIPTION** | ✅ Working (Whisper) | WhatsApp native | No |
| **Image GENERATION** | ✅ Working (Gemini) | DALL-E fallback | No |

---

## My Recommendation

### For Now (No Changes):

1. **Images:** Send me OCR text or describe the image
2. **Voice:** Use WhatsApp's native transcribe feature, then send text
3. **Image Gen:** Already works via nano-banana-pro (Gemini)

### If You Want Image Analysis:

**Easiest path:**
1. Get Gemini API key (you may already have one)
2. Configure as `imageModel` in OpenClaw
3. Restart gateway

**Risk level:** LOW - Gemini is already in your skills, just need to enable for image analysis

**Safest path:**
1. Backup config
2. Use CLI: `openclaw models set-image google/gemini-1.5-flash`
3. Test with one image

---

## Quick Comparison: Providers for Image Analysis

| Provider | Cost/Image | Quality | Setup | Risk |
|----------|-----------|---------|-------|------|
| **Gemini (Google)** | $0.0015 | Excellent | Easy (key exists) | Low |
| **Claude (Anthropic)** | $0.008 | Excellent | Medium (new key) | Low |
| **OpenRouter** | $0.003-0.01 | Excellent | Medium (new config) | Medium |
| **Local (LLaVA)** | FREE | Good | Hard (hardware) | Low |

---

## Bottom Line

**You already have:**
- ✅ Image generation (Gemini)
- ✅ Voice transcription (Whisper)
- ✅ Text/chat (Kimi)

**Missing:**
- ❌ Image understanding/analysis

**To fix image analysis:**
- **No OpenRouter needed** - Use Gemini (already configured in skills)
- **Or** - Use WhatsApp native OCR for text-heavy images

**Want me to configure Gemini for image analysis?** It's the safest option since the API key is already there.

---

*Prepared by Rocco 🤘*
