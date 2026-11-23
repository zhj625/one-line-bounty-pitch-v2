"""Entry for make.fun's "One Line That Makes a Builder Fund a Bounty".

The whole entry is one sentence. Running this program writes that
sentence to /output/entry.txt, where the bounty's sealed scorer
checks it and the house judge compares it against the other lines.
"""

from pathlib import Path

OUTPUT = Path("/output/entry.txt")

# Final line: "what you need built" reads in one pass, no filler,
# and every clause stays true to how a bounty works — the sponsor
# funds the reward, agents race to build, only the winning entry
# is paid.
PITCH = (
    "Don't gamble on one hire: fund a bounty for what you "
    "need built, let AI agents race to build it best, and pay "
    "only the entry that wins."
)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(PITCH, encoding="utf-8")
    # The scorer collects the output as another user: keep it readable.
    OUTPUT.chmod(0o644)


if __name__ == "__main__":
    main()
