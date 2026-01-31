# Best Practices for Running Multiple Models in OpenClaw

**Research Date:** January 31, 2026  
**Purpose:** Safely configure text + image models without breaking the gateway

---

## Key Findings from OpenClaw Documentation

### 1. How Model Selection Works

OpenClaw selects models in this order:

1. **Primary model** (`agents.defaults.model.primary`)
2. **Fallbacks** in `agents.defaults.model.fallbacks` (in order)
3. **Provider auth failover** happens inside a provider before moving to next model

**Critical:** `agents.defaults.imageModel` is used **ONLY when** the primary model can't accept images.

This means:
- ✅ Kimi (text-only) → Falls back to imageModel for images
- ✅ GPT-4 (multimodal) → Uses same model for text + images
- ❌ Don't set imageModel if primary already supports images

---

## Recommended Approaches

### Approach 1: CLI Commands (SAFEST)

Instead of hand-editing config, use CLI commands:

```bash
# Set primary text model (keeps Kimi for coding)
openclaw models set kimi-code/kimi-for-coding

# Set image model separately (uses OpenRouter)
openclaw models set-image openrouter/openai/gpt-4o

# Add fallbacks
openclaw models fallbacks add openrouter/anthropic/claude-3-opus
openclaw models image-fallbacks add openrouter/google/gemini-flash-1.5
```

**Why this is safer:**
- Validates before applying
- No manual JSON editing
- Automatic restart handling
- Built-in error checking

---

### Approach 2: Auto-Scan with OpenRouter

```bash
# Scan OpenRouter for best models
openclaw models scan --set-default --set-image --max-candidates 3
```

This will:
- Probe models for image support
- Test tool calling latency
- Rank by context size + parameters
- Automatically set primary + image models
- Set fallbacks

**Requires:** OpenRouter API key in environment or auth profiles

---

### Approach 3: Manual Config (ADVANCED)

If you MUST edit config manually, here's the safe structure:

```json5
{
  "agents": {
    "defaults": {
      // Primary text model (Kimi stays for coding)
      "model": {
        "primary": "kimi-code/kimi-for-coding",
        "fallbacks": [
          "openrouter/openai/gpt-4o",
          "openrouter/anthropic/claude-3-sonnet"
        ]
      },
      
      // Image model (separate from text)
      // Used ONLY when primary can't handle images
      "imageModel": {
        "primary": "openrouter/openai/gpt-4o",
        "fallbacks": [
          "openrouter/google/gemini-flash-1.5"
        ]
      },
      
      // Allowlist - optional but recommended
      "models": {
        "kimi-code/kimi-for-coding": { 
          "alias": "Kimi Code" 
        },
        "openrouter/openai/gpt-4o": { 
          "alias": "GPT-4o" 
        },
        "openrouter/google/gemini-flash-1.5": {
          "alias": "Gemini Flash"
        }
      }
    }
  },
  
  "auth": {
    "profiles": {
      "kimi-code:default": {
        "provider": "kimi-code",
        "mode": "api_key"
      },
      "openrouter:default": {
        "provider": "openrouter",
        "mode": "api_key",
        "apiKey": "sk-or-v1-..."
      }
    }
  },
  
  "models": {
    "mode": "merge",
    "providers": {
      "openrouter": {
        "baseUrl": "https://openrouter.ai/api/v1",
        "api": "openai-completions",
        "models": [
          {
            "id": "openai/gpt-4o",
            "name": "GPT-4o",
            "input": ["text", "image"],
            "cost": {
              "input": 0.0025,
              "output": 0.01
            }
          }
        ]
      }
    }
  }
}
```

---

## Critical Safety Rules

### 1. Strict Config Validation

OpenClaw **refuses to start** if config is invalid:
- Unknown keys → Gateway won't boot
- Malformed types → Gateway won't boot
- Invalid values → Gateway won't boot

**Always validate first:**
```bash
openclaw doctor
# Fix any issues before restarting
```

### 2. Backup Before Changes

```bash
# Always backup current config
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup.$(date +%Y%m%d_%H%M%S)

# If something breaks, restore:
cp ~/.openclaw/openclaw.json.backup.* ~/.openclaw/openclaw.json
systemctl --user restart openclaw-gateway.service
```

### 3. Use `config.patch` Instead of `config.apply`

- `config.apply` = Replaces **entire** config (dangerous)
- `config.patch` = Merges only changed keys (safer)

Example:
```bash
# Get current hash
openclaw gateway call config.get --params '{}'

# Patch just the image model
openclaw gateway call config.patch --params '{
  "raw": "{\\n  agents: { defaults: { imageModel: { primary: \\"openrouter/openai/gpt-4o\\" } } }\\n}\\n",
  "baseHash": "<hash-from-config.get>",
  "restartDelayMs": 5000
}'
```

### 4. Test with `/model` First

Before changing defaults, test models interactively:
```
/model list
/model openrouter/openai/gpt-4o
# Test image analysis
# If it works, then set as default
```

---

## What Went Wrong Before (Our Mistake)

### The Problem
Earlier today, I attempted to add OpenRouter by:
1. Adding auth profile with apiKey inline
2. Adding models.providers configuration
3. Adding imageModel.primary

**What I didn't realize:**
- The config syntax I used may have been invalid
- No validation before attempting restart
- Gateway failed to start due to config errors
- Had to revert

### The Correct Way (Next Time)

1. **Backup first:**
   ```bash
   cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup
   ```

2. **Use CLI commands (preferred):**
   ```bash
   openclaw models set-image openrouter/openai/gpt-4o
   ```
   
   OR

3. **If manual edit:**
   - Edit config file
   - Run `openclaw doctor` to validate
   - Only then restart

4. **If it fails:**
   ```bash
   # Automatic recovery
   cp ~/.openclaw/openclaw.json.backup ~/.openclaw/openclaw.json
   systemctl --user restart openclaw-gateway.service
   ```

---

## Voice Notes Configuration

For voice transcription (Whisper), OpenClaw uses:
- `openai-whisper-api` skill (already configured in our setup)
- Or can use OpenRouter's `/audio/transcriptions` endpoint

Current setup already has:
```json
"openai-whisper-api": {
  "apiKey": "sk-proj-..."
}
```

This should work for voice notes without additional changes.

---

## Recommended Action Plan

### For Our Setup (Current State)

**Current:**
- ✅ Kimi Code working (text)
- ❌ Image analysis broken (gpt-5-mini failing)
- ✅ Voice transcription (whisper configured)

**Recommended Fix:**

```bash
# Step 1: Backup
export BACKUP_DATE=$(date +%Y%m%d_%H%M%S)
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup.$BACKUP_DATE

# Step 2: Set image model via CLI (safest)
# First, ensure OPENROUTER_API_KEY is in environment
export OPENROUTER_API_KEY=sk-or-v1-...

# Then use CLI command
openclaw models set-image openrouter/openai/gpt-4o

# Step 3: Check status
openclaw models status

# Step 4: Test image
# Send a test image via WhatsApp
```

**If CLI approach fails:**
```bash
# Restore from backup
cp ~/.openclaw/openclaw.json.backup.$BACKUP_DATE ~/.openclaw/openclaw.json
systemctl --user restart openclaw-gateway.service
```

---

## Alternative: Use Environment Variable Only

If we don't want to modify config at all, we can set:

```bash
# Add to ~/.bashrc or service file
export OPENROUTER_API_KEY=sk-or-v1-...
export OPENAI_API_KEY=sk-or-v1-...  # OpenRouter is OpenAI-compatible
```

Then OpenClaw can use OpenRouter as an OpenAI alternative without config changes.

But this requires the `image` tool to be configurable to use a different endpoint, which may not be possible without config changes.

---

## Summary

| Approach | Risk | Best For |
|----------|------|----------|
| CLI `models set-image` | Low | Most users |
| `models scan --set-image` | Low | OpenRouter users |
| Manual config edit | Medium | Advanced users |
| `config.patch` | Medium | Programmatic changes |
| `config.apply` | High | Full config replacement |

**Bottom Line:**
- Use CLI commands when possible
- Always backup before changes
- Validate with `openclaw doctor`
- Test with `/model` before setting defaults
- Keep Kimi as primary for coding (as requested)
- Add OpenRouter only for image fallback

---

*Research compiled from:*
- https://docs.openclaw.ai/concepts/models
- https://docs.openclaw.ai/gateway/configuration
- Local OpenClaw docs at `/home/pi/.npm-global/lib/node_modules/openclaw/docs/`

*Prepared by Rocco 🤘*
