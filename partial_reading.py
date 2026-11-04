"""
Step 1 of the synthetic reading: partial reading of "Subha".

The story is split into sentences and divided into three equal parts.
From each part only 20% of the sentences are kept:
  Part 1 - the FIRST 20% of its sentences
  Part 2 - a RANDOM 20% of its sentences (fixed seed, kept in story order)
  Part 3 - the LAST 20% of its sentences
The result is written to partial_reading.txt, which is read before the
full text in order to form an initial impression.

The same three parts are reused as Stage I, II and III in extract_themes.py.

Run:  python partial_reading.py
"""

import math
import random
import re
from pathlib import Path

HERE = Path(__file__).parent
SEED = 2026
SHARE = 0.20


def story_sentences():
    """Return the story's sentences (title and source note removed)."""
    text = (HERE / "subha.txt").read_text(encoding="utf-8")
    paragraphs = text.split("\n\n")
    start = next(i for i, p in enumerate(paragraphs) if p.startswith("When the girl"))
    story = " ".join(" ".join(paragraphs[start:]).split())
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'])", story) if s.strip()]


def three_parts():
    sentences = story_sentences()
    size = math.ceil(len(sentences) / 3)
    return [sentences[i:i + size] for i in range(0, len(sentences), size)]


def pick(part, how):
    k = max(1, round(len(part) * SHARE))
    if how == "first":
        return part[:k]
    if how == "last":
        return part[-k:]
    rng = random.Random(SEED)
    return [part[i] for i in sorted(rng.sample(range(len(part)), k))]


def main():
    parts = three_parts()
    total = sum(map(len, parts))
    labels = [("first", "First 20% of sentences"),
              ("random", f"Random 20% of sentences (seed {SEED}, in story order)"),
              ("last", "Last 20% of sentences")]
    out = ["PARTIAL READING",
           f'Three equal parts of Rabindranath Tagore\'s "Subha" ({total} sentences, '
           f"about {len(parts[0])} per part). From each part only 20% of the sentences "
           "were read before forming an initial impression.", ""]
    for n, (part, (how, label)) in enumerate(zip(parts, labels)):
        chosen = pick(part, how)
        out += [f"{'ABC'[n]}. Part {n + 1}: {label} ({len(chosen)} of {len(part)} sentences)", ""]
        out += [" ".join(chosen) + ' (Tagore, "Subha")', ""]
    (HERE / "partial_reading.txt").write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
