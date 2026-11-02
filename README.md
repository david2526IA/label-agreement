# Label Agreement

Evaluate paired human annotations before using a dataset for a computer-vision or ML project. The tool calculates observed agreement, expected agreement, Cohen's kappa and a readable confusion matrix.

## Input

One JSON object per line:

```json
{"id":"image-001","annotator_a":"defect","annotator_b":"ok"}
```

## Run

```bash
pip install .
label-agreement labels.jsonl --output agreement_report.json
```

## Scope

Kappa is a signal for dataset review, not proof of label correctness or model quality. Examine class balance, annotation guidance, individual disagreements and the original samples before deciding how to change a dataset.

## Development

```bash
pip install ".[dev]"
pytest -q
```

## License

MIT
