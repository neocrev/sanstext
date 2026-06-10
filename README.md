<p align="center">
  <img src="https://img.icons8.com/fluency/96/null/skull.png" width="80">
</p>

<h1 align="center">SansText</h1>

<p align="center">
  <strong>Undertale-style Sans dialogue animation for your terminal.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/sanstext?color=%23333&label=version&logo=python&logoColor=white">
  <img src="https://img.shields.io/pypi/pyversions/sanstext?color=%23333&logo=python&logoColor=white">
  <img src="https://img.shields.io/github/license/neocrev/sanstext?color=%23333">
  <img src="https://img.shields.io/badge/made%20by-neocrev-%23333">
</p>

---

Each character appears one by one with a retro blip sound.  
Spaces are silent — just like Sans would want it.

```bash
pip install sanstext
```

---

## Usage

### Python

```python
from sanstext import sans

sans("heh heh heh. you're really something, kid.")
```

### CLI

```bash
echo "ketchup is the best, right?" | sanstext
sanstext "hey. i'm sans. sans the skeleton."
sanstext --no-sound "silent mode"
```

---

## How it works

| What | How |
|------|-----|
| Typing animation | Characters printed one-by-one with randomized delay |
| Sound | Each non‑space character triggers a retro game‑style blip |
| Punctuation | Longer dramatic pause on `.,!?;:` |
| Spaces | Silent — no sound, shorter pause |
| Audio engine | WAV generated in memory — zero external audio files |

---

## API

```python
sans(
    text: str,
    *,
    end: str = "\n",
    speed: float = 0.07,
    sound: bool = True,
    file=sys.stdout,
)
```

| Param | Default | Description |
|-------|---------|-------------|
| `text` | — | Text to animate |
| `end` | `\n` | Line ending |
| `speed` | `0.07` | Seconds per character (base) |
| `sound` | `True` | Enable blip sounds |
| `file` | `stdout` | Output stream |

---

## Sound backends

1. `simpleaudio` — best quality, async playback (recommended)
2. `aplay` (Linux) / `afplay` (macOS) / `winsound` (Windows) — fallback
3. System bell `\a` — last resort

Install `simpleaudio` for audio:

```bash
pip install simpleaudio
```

---

<p align="center">
  <sub>heh heh heh … try it yourself, kid.</sub>
</p>
# pr1
# achievement 1
# achievement 2
# co-author test
# pair
