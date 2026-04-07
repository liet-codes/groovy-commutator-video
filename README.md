# Groovy Commutator Video Generator

A GitHub Actions pipeline for creating 3Blue1Brown-style mathematical explainer videos using [Manim](https://www.manim.community/).

## Quick Start

### Creating a New Video

1. **Create a branch** for your video:
   ```bash
   git checkout -b video/my-video-name
   ```

2. **Create a video folder**:
   ```bash
   mkdir videos/my-video-name
   cd videos/my-video-name
   ```

3. **Add your files**:
   - `script.py` — Your Manim scene file
   - `plan.md` — (Optional) Narrative plan and voiceover script
   - `config.yml` — Render configuration

4. **Push and trigger**:
   ```bash
   git add .
   git commit -m "Add video: my-video-name"
   git push origin video/my-video-name
   ```
   
   Then go to **Actions → Render Video → Run workflow** and enter `my-video-name`.

## Folder Structure

```
videos/
├── groovy-commutator/              # Example video
│   ├── script.py                   # Main Manim script
│   ├── plan.md                     # Narrative arc & voiceover
│   └── config.yml                  # Render configuration
└── your-video/                     # Your new video
    ├── script.py
    ├── plan.md
    └── config.yml
```

## Config File Format (`config.yml`)

```yaml
name: "Groovy Commutator Explainer"
scenes:
  - Scene1_Mystery
  - Scene2_ClassificationProblem
  - Scene3_Operators
  - Scene4_Commutator
  - Scene5_MonomialSupport
  - Scene6_ExperimentalResults
  - Scene7_Universality
  - Scene8_Implication
quality: high           # low | medium | high
fps: 60
stitch: true            # Concatenate scenes into final.mp4
```

## Render Triggers

Videos are **NOT** rendered automatically on push. To render:

1. **Manual trigger** (recommended):  
   Go to Actions → Render Video → Run workflow → Enter video folder name

2. **Tag trigger** (for releases):  
   Push a tag like `video/my-video-name/v1.0` to auto-render

This prevents burning GitHub Actions minutes on every commit.

## Scene File Template

```python
from manim import *

BG = "#1C1C1C"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FFFF00"
TEXT = "#EAEAEA"
MONO = "Menlo"

class Scene1_Introduction(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Your Title", font_size=48, color=PRIMARY, weight=BOLD, font=MONO)
        self.play(Write(title), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(title), run_time=0.5)
```

## Output

Rendered videos are available as:
- **Individual scenes**: `scene-videos` artifact
- **Stitched final**: `final-video` artifact  
- **Release asset**: Auto-attached on version tags

## Requirements

- Python 3.10+
- Manim Community Edition 0.19+
- LaTeX (texlive-full)
- ffmpeg

All handled automatically by GitHub Actions.

## Example: Groovy Commutator

See `videos/groovy-commutator/` for a complete example with:
- 8 scenes (~3 minutes total)
- Custom color palette (3Blue1Brown style)
- CA grid visualizations
- Mathematical notation

## Tips

- Iterate locally with `manim -ql script.py SceneName` (draft quality)
- Use `plan.md` to nail the narrative before coding
- Keep scenes under 30 seconds each for easier editing
- Test ffmpeg concat locally: `ffmpeg -f concat -i concat.txt -c copy out.mp4`

---

*Built with [Manim](https://www.manim.community/) • Automated with GitHub Actions*
