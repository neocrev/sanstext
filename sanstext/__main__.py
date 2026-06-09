import sys

from .core import sans


def main():
    args = sys.argv[1:]
    no_sound = "--no-sound" in args or "-s" in args
    if no_sound:
        args = [a for a in args if a not in ("--no-sound", "-s")]

    if not sys.stdin.isatty():
        text = sys.stdin.read()
    elif args:
        text = " ".join(args)
    else:
        text = "hey kid. want some ketchup?"

    sans(text, sound=not no_sound)


if __name__ == "__main__":
    main()
