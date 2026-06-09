# SansText

Undertale-style Sans dialogue animation for your terminal.

Each character appears one by one with a retro blip sound.
Spaces are silent — just like Sans would want it.

## Install
```bash
pip install sanstext
```

## Usage
```python
from sanstext import sans

sans("heh heh heh. you're really something, kid.")
```

```bash
echo "ketchup is the best, right?" | sanstext
sanstext "hey. i'm sans. sans the skeleton."
sanstext --no-sound "silent mode"
```

## How it works
- Characters print one at a time with randomized typing delay
- Each non-space character triggers a retro game-style blip
- Punctuation adds a longer dramatic pause
- Sound generated as a WAV in memory — no external audio files
