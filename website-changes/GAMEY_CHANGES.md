# Gamey Design Changes - Summary

## What I Added

### 1. HP/XP Reading Progress Bars
- **HP Bar**: Gradient health bar (red→yellow→cyan) at the very top of the page
- **XP Bar**: Blue gradient bar just below it
- Both fill as you scroll down the page
- Style inspired by: Quake II, Doom health bars, Clash Royale progress

### 2. Achievement System
Unlocks appear as toast notifications in bottom-right:
- **First Steps** (👣) - Scroll past 5%
- **Halfway There** (🎯) - Reach 50% scroll
- **Completionist** (🏆) - Reach 100% scroll
- **Speed Reader** (⚡) - Reach 90% in under 30 seconds
- **Click Master** (🖱️) - Click 50 times anywhere on page

Style: Dark gradient background with gold accent, game UI aesthetic

### 3. Konami Code Easter Egg
Type: **↑ ↑ ↓ ↓ ← → ← → B A**

Effects:
- Glitch animation on the page
- Unlocks "Terminal Mode" button
- Shows "Cheat Activated" achievement

### 4. Terminal Mode
A hidden retro CRT terminal view:
- **Activate**: Click the ⌨️ button (bottom-left, appears after 10s or Konami code)
- **Effects**:
  - Black background (#0d1117)
  - Green terminal text (#00ff00)
  - Scanline overlay effect
  - Monospace fonts
  - Yellow headers (like old DOS)
  - Persists across page reloads (saved in localStorage)

Inspired by: Prince of Persia (retro gaming), Doom terminal aesthetics

### 5. Cheat Code Hint
Very subtle text in bottom-right corner: `↑↑↓↓←→←→BA`
- Only visible on hover
- Opacity 0.3 (barely noticeable)
- Hints at the Konami code

### 6. Design Touches
- **Heading accents**: Subtle gradient underline on h1/h2 (Doom-style)
- **Color palette**: Uses gaming-inspired colors (cyans, golds, reds) but subtly

## Files Created/Modified

```
assets/css/gamey.css        # All styling
assets/js/gamey.js          # All JavaScript functionality
layouts/partials/extend_head.html   # Added CSS/JS links
```

## How to Apply

Since I have read-only access, you need to manually apply these changes:

### Option 1: Manual Copy
1. Go to: https://github.com/senapaty/akashpersonal
2. Create a new branch (e.g., `git checkout -b gamey-design`)
3. Copy the files from `website-changes/` folder in this repo
4. Commit and push
5. Test locally: `hugo server -D`
6. Merge to main if you like it

### Option 2: Patch File
I can create a `.patch` file you can apply with `git apply`

## Testing Locally

```bash
cd /path/to/akashpersonal
git checkout -b gamey-design
cp -r /path/to/website-changes/* .
hugo server -D
# Visit http://localhost:1313
```

## Try These:

1. **Scroll down** → Watch HP/XP bars fill
2. **Keep scrolling** → Unlock achievements
3. **Type Konami code** (↑↑↓↓←→←→BA) → See glitch effect
4. **Click terminal button** (bottom-left) → Toggle retro mode
5. **Hover bottom-right** → See cheat hint

## Design Philosophy

- **Subtle**: All effects are optional and non-intrusive
- **Readable**: Default mode maintains PaperMod's clean readability
- **Discoverable**: Easter eggs reward exploration
- **Gaming cred**: References your favorites without being cheesy

Let me know what you think! Can adjust/remove anything.

---
*Rocco 🤘*
