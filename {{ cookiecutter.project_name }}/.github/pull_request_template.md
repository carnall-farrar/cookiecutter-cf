## Summary

Please provide a brief summary of the changes introduced in this PR.

- [ ] New feature
- [ ] Bug fix
- [ ] Refactor
- [ ] Documentation update
- [ ] Experiment/analysis

---

## Related Issues / Tasks

Link to any related GitHub issues or project tasks.

Closes #...

---

## Key Changes

Describe the key changes in this PR, for example:

- Modified preprocessing pipeline to include outlier removal
- Added a new feature engineering step for `customer_age_group`
- Trained new XGBoost model with hyperparameter tuning
- Updated `model_evaluation.ipynb` with new results

---

## How to Test / Reproduce

Steps to test this PR locally, e.g:

1. Run `python scripts/train_model.py --config config/train.yaml`
2. Execute the updated notebook: `notebooks/model_evaluation.ipynb`
3. Compare new vs old model metrics in `outputs/metrics.json`

---

## PR Checklist

- [ ] Code is ruff-formatted
- [ ] Code is tested (unit tests or notebook cells)
- [ ] Data pipeline runs successfully
- [ ] Project artifacts saved (e.g., `models/`, `outputs/`)
- [ ] README / relevant docs updated
- [ ] No secrets, credentials, or large files included

---

## Notes for Reviewers

Any context or questions for reviewers:

> e.g., “Should we increase the threshold for feature importance filtering?” or “This model only performs better on Segment A, not overall.”
