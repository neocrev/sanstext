import random
import sys
import time

from .sound import play

_SPEED = 0.07
_PUNCT_DELAY = 0.35
_PUNCT = set(".,!?;:…")


def sans(
    text: str,
    *,
    end: str = "\n",
    speed: float = _SPEED,
    sound: bool = True,
    file=sys.stdout,
):
    for i, ch in enumerate(text):
        if ch in _PUNCT:
            if sound and ch not in " ":
                play()
            time.sleep(_PUNCT_DELAY)
        elif ch == "\n":
            time.sleep(speed * 2)
        else:
            if sound and ch not in " \t\r":
                play()
            delay = speed * random.uniform(0.7, 1.3)
            time.sleep(delay)
        print(ch, end="", flush=True, file=file)
    print(end=end, file=file)
