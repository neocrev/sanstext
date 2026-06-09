import io
import math
import random
import struct
import sys
import tempfile
import wave
from pathlib import Path

SAMPLE_RATE = 22050
BLIP_DURATION = 0.06
BASE_FREQ = 500

def _gen_blip_wav(freq: int = 0) -> bytes:
    if freq == 0:
        freq = BASE_FREQ + random.randint(-150, 150)
    n = int(SAMPLE_RATE * BLIP_DURATION)
    samples = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = 1.0 - (i / n) ** 0.6
        val = math.sin(2 * math.pi * freq * t) * env * 0.4
        samples.append(int(val * 32767))
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(struct.pack("<" + "h" * n, *samples))
    return buf.getvalue()


def play():
    wav = _gen_blip_wav()
    try:
        import simpleaudio

        simpleaudio.play_buffer(wav, 1, 2, SAMPLE_RATE)
        return
    except ImportError:
        pass

    try:
        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        tmp.write(wav)
        tmp.close()
        p = Path(tmp.name)
        if sys.platform == "win32":
            import winsound

            winsound.PlaySound(str(p), winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif sys.platform == "darwin":
            import subprocess
            subprocess.Popen(["afplay", str(p)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            import subprocess
            subprocess.Popen(["aplay", str(p)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        p.unlink(missing_ok=True)
    except Exception:
        print("\a", end="", flush=True)
