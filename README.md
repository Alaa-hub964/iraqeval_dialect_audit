# Dialect Marker-Density Audit (Iraqi Arabic)

Reproducibility code for the paper **"Egyptian in Iraqi Clothing: A Native-Speaker
Audit of a Mislabelled 'Iraqi' Partition in a Public Arabic Dialect Corpus."**

This repository releases the **marker lexicons** and the **marker-density
diagnostic** used to audit dialect labels. The diagnostic is a simple,
transparent word-list screen — no trained model — so any reader can recompute it.

## Contents
- `marker_lexicons.py` — Iraqi / Egyptian / Gulf / Levantine marker word-lists + matching
- `marker_density_audit.py` — computes marker density and competing-dialect share for any corpus

## Quick start
```python
from marker_density_audit import audit
texts = [...]            # your list of Arabic strings
audit(texts, "my corpus")
```

To reproduce the paper's audit of the public corpus:
```python
from datasets import load_dataset
from marker_density_audit import audit
ds = load_dataset("dataflare/arabic-dialect-corpus", split="train")
rows = [r["text"] for r in ds if r.get("dialect") == "Iraqi"]
audit(rows, "dataflare Iraqi partition")
```

## Key finding
Across the public corpus's 4,756-row "Iraqi" partition: Iraqi-marker density is
6.7% (vs 47.2% in a native-verified reference). The partition is predominantly
Egyptian (45.5% Egyptian markers vs 1.1% Gulf/Saudi).

## Citation
Alowaidi, A., & Pateriya, P. K. (2026). Egyptian in Iraqi Clothing: A Native-Speaker
Audit of a Mislabelled "Iraqi" Partition in a Public Arabic Dialect Corpus.

## License
MIT
