import pytest

from label_agreement.metrics import agreement


def test_perfect_agreement_has_kappa_one() -> None:
    report = agreement([{"id": "1", "annotator_a": "ok", "annotator_b": "ok"}, {"id": "2", "annotator_a": "defect", "annotator_b": "defect"}])
    assert report["observed_agreement"] == 1.0
    assert report["cohen_kappa"] == 1.0


def test_matrix_exposes_disagreement() -> None:
    report = agreement([{"id": "1", "annotator_a": "ok", "annotator_b": "defect"}, {"id": "2", "annotator_a": "ok", "annotator_b": "ok"}, {"id": "3", "annotator_a": "defect", "annotator_b": "defect"}])
    assert report["confusion_matrix"]["ok"]["defect"] == 1
    assert report["cohen_kappa"] < 1


def test_duplicate_item_ids_are_rejected() -> None:
    with pytest.raises(ValueError, match="unique"):
        agreement([{"id": "1", "annotator_a": "ok", "annotator_b": "ok"}, {"id": "1", "annotator_a": "ok", "annotator_b": "ok"}])
