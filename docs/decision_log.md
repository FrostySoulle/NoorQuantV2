# Decision Log

---

## 2026-06-21

### Decision

Abandon NoorQuant V1 weighted scoring model.

### Reason

Independent reviews identified significant overfitting risk.

### Status

Accepted

---

## 2026-06-28

### Decision

Adopt a hypothesis-driven quantitative research framework.

### Reason

Indicator-first development encourages curve fitting.

Every trading rule must be statistically validated before entering the strategy.

### Status

Accepted

---

## 2026-06-28

### Decision

Freeze Research Engine v1.0.

### Reason

The research engine became modular and reusable.

Future work should create new research modules rather than modifying the core engine.

### Status

Accepted

---

## 2026-06-28

### Decision

Evaluate factors individually before researching combinations.

### Reason

Understanding each factor independently provides a baseline and prevents black-box models.

### Status

Accepted

---

## 2026-06-28

### Decision

Reject Relative Strength as a standalone factor.

### Reason

Relative Strength alone failed to produce a statistically significant edge across multi-year testing.

Later research demonstrated that RS can contribute positively inside multi-factor models.

### Status

Accepted

---

## 2026-06-28

### Decision

Reject Relative Volume as a standalone factor.

### Reason

RVOL alone produced no statistically significant predictive edge.

Future research will investigate RVOL as a trade filter or market regime filter instead of a ranking factor.

### Status

Accepted

---

## 2026-06-28

### Decision

Prioritize multi-factor research.

### Reason

Single-factor models consistently underperformed.

Combining complementary factors produced substantially stronger and more stable results.

### Status

Accepted

---

## 2026-06-28

### Decision

Introduce sequential threshold optimization.

### Reason

Optimal thresholds depend on the interaction between factors.

Thresholds should therefore be optimized after identifying the best factor combination.

### Status

Accepted

---

## 2026-06-28

### Decision

Adopt weighted multi-period scoring.

### Reason

Recent data should contribute more heavily than older data while still rewarding strategies that remain profitable across multiple market periods.

### Status

Accepted

---

## 2026-06-28

### Decision

Champion models must be validated before deployment.

### Reason

The highest-scoring model is only a research candidate until it passes model validation, robustness testing, and walk-forward analysis.

### Status

Accepted

2026-07-01
Decision
Freeze Validation Engine (v1.0)
Reason
First complete out-of-sample validation pipeline successfully executed from factor selection through validation. Future enhancements should preserve this baseline implementation.
Status
Accepted