"""
Step 6 of the synthetic reading: computation and visualisation.

Statement tested (from initial_impression.md):
  Across the three stages of "Subha", the vocabulary of nature and
  non-human kinship falls away while the vocabulary of social and
  patriarchal structure takes over.

Reads the author-annotated themes in subha_themes.py and produces:
  figures/theme_heatmap.png  - number of expressions per dimension per stage
  figures/theme_trace.png    - how often each dimension's expressions occur,
                               sentence by sentence, across the whole story

Run:  python visualise.py      (needs matplotlib)
"""

import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from partial_reading import three_parts
from subha_themes import themes

HERE = Path(__file__).parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)

STAGES = ["Stage_I", "Stage_II", "Stage_III"]
STAGE_LABELS = ["Stage I\nchildhood", "Stage II\ngrowing up", "Stage III\nmarriage"]
DIMS = [("Voice", "Voice & silence", "#6a1b9a"),
        ("Nature", "Nature & non-human kinship", "#2e7d32"),
        ("Structure", "Social & patriarchal structure", "#ad1457"),
        ("Affect", "Affect & being", "#d4a72c")]

plt.rcParams.update({"font.family": "serif", "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False})

# ---- Figure 1: heat map of expression counts --------------------------------
counts = np.array([[len(themes.get(f"{s}_{d}", [])) for s in STAGES] for d, _, _ in DIMS])
fig, ax = plt.subplots(figsize=(7.5, 3.8))
im = ax.imshow(counts, cmap="RdPu", aspect="auto")
ax.set_xticks(range(3), STAGE_LABELS)
ax.set_yticks(range(len(DIMS)), [label for _, label, _ in DIMS])
for i in range(counts.shape[0]):
    for j in range(counts.shape[1]):
        ax.text(j, i, counts[i, j], ha="center", va="center",
                color="white" if counts[i, j] > counts.max() * 0.6 else "#2b1a22", fontsize=12)
ax.set_title('"Subha": number of extracted expressions per dimension and stage', pad=12)
for s in ax.spines.values():
    s.set_visible(False)
fig.colorbar(im, ax=ax, shrink=0.8, label="expressions")
fig.tight_layout()
fig.savefig(FIG / "theme_heatmap.png", dpi=200)
plt.close(fig)

# ---- Figure 2: sentence-by-sentence trace -----------------------------------
parts = three_parts()
sentences = [s for p in parts for s in p]
bounds = np.cumsum([len(p) for p in parts])[:-1]


def pattern(phrases):
    alts = sorted({re.escape(p.lower()) for p in phrases}, key=len, reverse=True)
    return re.compile(r"\b(" + "|".join(alts) + r")\b") if alts else None


window = 9
fig, ax = plt.subplots(figsize=(9, 4))
for d, label, colour in DIMS:
    phrases = [p for s in STAGES for p in themes.get(f"{s}_{d}", [])]
    pat = pattern(phrases)
    hits = np.array([len(pat.findall(s.lower())) if pat else 0 for s in sentences], float)
    smooth = np.convolve(hits, np.ones(window) / window, mode="same")
    ax.plot(range(1, len(sentences) + 1), smooth, label=label, color=colour, lw=2)
for b in bounds:
    ax.axvline(b + 0.5, color="#888", ls="--", lw=0.8)
for k, lab in enumerate(["Stage I", "Stage II", "Stage III"]):
    start = 0 if k == 0 else bounds[k - 1]
    end = len(sentences) if k == 2 else bounds[k]
    ax.text((start + end) / 2, ax.get_ylim()[1] * 0.97, lab, ha="center", va="top", color="#555")
ax.set_xlabel("Sentence in the story")
ax.set_ylabel(f"Occurrences per sentence\n(moving average, {window} sentences)")
ax.set_title('"Subha": where each dimension\'s vocabulary occurs across the story')
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(1, 1))
fig.tight_layout()
fig.savefig(FIG / "theme_trace.png", dpi=200)
plt.close(fig)

print("Counts (rows = dimensions, columns = stages):")
for (d, label, _), row in zip(DIMS, counts):
    print(f"  {label:<32} {row.tolist()}")
print("Saved figures/theme_heatmap.png and figures/theme_trace.png")
