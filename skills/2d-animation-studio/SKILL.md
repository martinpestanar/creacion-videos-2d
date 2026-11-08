---
name: 2d-animation-studio
description: Generates high-quality 2D animated videos (stories, explainers, cartoon shorts, or character motion) using Remotion, procedural Canvas2D/Three.js character systems, automated speech-to-text timing, procedural audio mixing, and multimodal Vision QA loops. Use when the user wants to create 2D animated videos, cartoon shorts, motion graphics, or video explainers.
---
# 2D Animation Studio (Antigravity + Gemini Architecture)

This skill guides Antigravity and Gemini to act as a full-fledged animation production studio, producing reproducible, deterministic, and modular 2D animated videos using **Code-as-Video**.

## Why this Architecture Beats Generic AI Video Generators
1. **Deterministic & Modifiable**: Every frame, character pose, color, and word timestamp is written in code. Changing a line of dialogue or a character's expression doesn't ruin the rest of the video.
2. **Infinite Resolution**: Rendered natively with Remotion in 1080x1920 (Shorts/Reels/TikTok) or 1920x1080 (YouTube/Landscape) with crisp vector outlines.
3. **Zero Hallucinations & Drift**: Characters remain 100% consistent across every shot because their vector/billboard geometry is fixed in procedural assets.
4. **Precise Frame-to-Speech Sync**: Visual beats land exactly 0 to 3 frames before narration words via exact millisecond timestamps.

---

## 5-Stage Production Pipeline

### Stage 1: Narrative & Scripting (`script.json`)
Structure the story into high-retention beats:
1. **Hook (0-5s)**: Surprising visual fact or absurd contradiction.
2. **Setting & Setup (5-15s)**: Introduces characters and core world.
3. **Escalation / Beats (15-40s)**: 3-4 escalating actions with visual dynamics.
4. **The Snap / Climax (40-50s)**: The breaking point or resolution.
5. **Analogy & Punchline (50-65s)**: Visual metaphor explaining the lesson with a callback twist.

### Stage 2: Voice Narration & Word-Level Timing
Generate or ingest narration audio (`voice.wav`):
- Run speech transcription with word-level boundaries to yield `words.json`:
  ```json
  [
    {"word": "Seventy-four", "start": 0.12, "end": 0.65},
    {"word": "soldiers", "start": 0.68, "end": 1.10}
  ]
  ```
- All camera transitions, cuts, zooms, and character expressions in `story.ts` must reference word timestamps or specific frame counts calculated as `Math.round(timestamp * fps)`.

### Stage 3: Visual System (2D Characters + Stylized World)
- **Character Rigging (`characters.ts`)**:
  - Draw characters on procedural HTML5 Canvas2D (`OffscreenCanvas` or React canvas).
  - Use modular sub-components: head shape, expression library (eyes: blink, shock, squint; mouth: talk, smile, o-shape), torso, and limbs.
  - Implement spring physics and walk-cycles (`walkPhase = Math.sin(frame * speed)`).
- **Scene & Backgrounds (`world.ts`)**:
  - Either pure 2D parallax layering (foreground, midground, background) or 2.5D Cel-Shaded Three.js world using `@remotion/three`.
  - Apply clean ink outlines: dark outline tint (`#1A1423`), cel-shading colors with 2-tone ramps.
- **Camera & Directing (`story.ts`)**:
  - Define camera cuts, pans, slow glides, and screen kicks on impacts.
  - Anticipation: character reactions happen 2 frames before the vocal punchline.

### Stage 4: Procedural Audio & Sound Design
- **SFX**: Sourced or procedurally synthesized per impact/action.
- **Background Music**: Dynamic ducking (`volume = isSpeaking ? 0.25 : 0.75`).
- Spliced and mastered cleanly with FFmpeg / Remotion audio graph.

### Stage 5: Multimodal Quality Assurance (Vision QA)
1. Export keyframe stills (`frame_hook.png`, `frame_mid.png`, `frame_end.png`).
2. Gemini inspects the stills visually:
   - Check line consistency, contrast, and readability of silhouettes.
   - Verify that characters aren't clipped by UI margins.
3. Once validated, execute production render:
   `npx remotion render src/index.ts ShortComposition out/final.mp4 --codec h264 --crf 16`