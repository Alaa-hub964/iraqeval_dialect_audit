"""
Marker-density audit: reproduces the paper's cross-corpus table.
Usage: pass any list of texts; prints marker density + competing-dialect share.
"""
from marker_lexicons import iraqi_marker_count, dialect_markers

def audit(rows, name="corpus"):
    rows=[t for t in rows if t and len(str(t).split())>=4]
    n=len(rows)
    bearing=sum(1 for t in rows if iraqi_marker_count(t)>0)
    eg=sum(1 for t in rows if dialect_markers(t)["egyptian"])
    gu=sum(1 for t in rows if dialect_markers(t)["gulf"])
    print(f"{name}: n={n}")
    print(f"  Iraqi-marker density : {100*bearing/n:.1f}%")
    print(f"  Egyptian-marker rows : {100*eg/n:.1f}%")
    print(f"  Gulf/Saudi-marker rows: {100*gu/n:.1f}%")
    return {"n":n,"marker_density":100*bearing/n,
            "egyptian":100*eg/n,"gulf":100*gu/n}

if __name__ == "__main__":
    # Example: audit a public corpus's "Iraqi" partition
    # from datasets import load_dataset
    # ds=load_dataset("dataflare/arabic-dialect-corpus", split="train")
    # rows=[r["text"] for r in ds if r.get("dialect")=="Iraqi"]
    # audit(rows, "dataflare Iraqi partition")
    print("Import audit() and pass a list of texts. See README.")
