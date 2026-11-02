"""Cohen's kappa with a readable confusion matrix."""

from __future__ import annotations

from collections import Counter
from typing import Any


def agreement(rows: list[dict[str, str]]) -> dict[str, Any]:
    """Calculate observed agreement and Cohen's kappa from paired labels."""
    if not rows:
        raise ValueError("at least one paired label is required")
    if any(not {"id", "annotator_a", "annotator_b"} <= row.keys() for row in rows):
        raise ValueError("rows need id, annotator_a and annotator_b")
    identifiers = [row["id"] for row in rows]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("ids must be unique")
    labels = sorted({row["annotator_a"] for row in rows} | {row["annotator_b"] for row in rows})
    matrix = {left: {right: 0 for right in labels} for left in labels}
    for row in rows:
        matrix[row["annotator_a"]][row["annotator_b"]] += 1
    total = len(rows)
    observed = sum(matrix[label][label] for label in labels) / total
    a_counts = Counter(row["annotator_a"] for row in rows)
    b_counts = Counter(row["annotator_b"] for row in rows)
    expected = sum((a_counts[label] / total) * (b_counts[label] / total) for label in labels)
    kappa = 1.0 if expected == 1 and observed == 1 else (observed - expected) / (1 - expected)
    return {"items": total, "labels": labels, "observed_agreement": round(observed, 4), "expected_agreement": round(expected, 4), "cohen_kappa": round(kappa, 4), "confusion_matrix": matrix, "scope": "label-consistency metric only; investigate disagreement by class, guidelines and sample context"}
