# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of renderings N_rend = 40 for n_t = 10 objects and n_d = 4 lexicons",
    "inputs": "n_t = 10, n_d = 4",
    "formula": "N_rend = n_t * n_d"
  },
  {
    "id": "Q2",
    "statement": "Number of lexicon pairs per object = 6",
    "inputs": "n_d = 4",
    "formula": "C(n_d, 2) = n_d*(n_d-1)/2"
  },
  {
    "id": "Q3",
    "statement": "Total pairwise analogy hypotheses N_hyp = 60",
    "inputs": "n_t = 10, C(4,2) = 6",
    "formula": "N_hyp = n_t * C(n_d, 2)"
  },
  {
    "id": "Q4",
    "statement": "Total evaluation points E_total = 180",
    "inputs": "N_hyp = 60, 3 criteria",
    "formula": "E_total = N_hyp * 3"
  },
  {
    "id": "Q5",
    "statement": "Single-rater budget T_rate = 5.0 h",
    "inputs": "N_hyp = 60, 5 min per rating",
    "formula": "T_rate = N_hyp * 5 / 60"
  },
  {
    "id": "Q6",
    "statement": "Three-rater budget T_rate^(3) = 15.0 h",
    "inputs": "T_rate = 5.0 h, 3 raters",
    "formula": "T_rate^(3) = 3 * T_rate"
  },
  {
    "id": "Q7",
    "statement": "Synthesis screening budget T_syn = 5.0 h",
    "inputs": "n_t = 10, B = 3, 10 min per screening",
    "formula": "T_syn = n_t * B * 10 / 60"
  },
  {
    "id": "Q8",
    "statement": "Total expert budget T_total = 20.0 h",
    "inputs": "T_rate^(3) = 15.0 h, T_syn = 5.0 h",
    "formula": "T_total = T_rate^(3) + T_syn"
  }
]

## Script
```python
import math
from math import comb

# Inputs stated in the paper
n_t = 10          # formal objects on the benchmark
n_d = 4           # domain lexicons
criteria = 3      # evaluation criteria per hypothesis
minutes_per_rating = 5
n_raters = 3
B = 3             # beam width for synthesis screening
minutes_per_screening = 10

# Q1: renderings
N_rend = n_t * n_d
print(f"CLAIM Q1: computed={N_rend} expected=40 match={'yes' if N_rend == 40 else 'no'}")

# Q2: lexicon pairs per object
pairs = comb(n_d, 2)
print(f"CLAIM Q2: computed={pairs} expected=6 match={'yes' if pairs == 6 else 'no'}")

# Q3: total pairwise analogy hypotheses
N_hyp = n_t * pairs
print(f"CLAIM Q3: computed={N_hyp} expected=60 match={'yes' if N_hyp == 60 else 'no'}")

# Q4: total evaluation points
E_total = N_hyp * criteria
print(f"CLAIM Q4: computed={E_total} expected=180 match={'yes' if E_total == 180 else 'no'}")

# Q5: single-rater budget in hours
T_rate = N_hyp * minutes_per_rating / 60
print(f"CLAIM Q5: computed={T_rate} expected=5.0 match={'yes' if math.isclose(T_rate, 5.0, rel_tol=1e-6) else 'no'}")

# Q6: three-rater budget
T_rate3 = n_raters * T_rate
print(f"CLAIM Q6: computed={T_rate3} expected=15.0 match={'yes' if math.isclose(T_rate3, 15.0, rel_tol=1e-6) else 'no'}")

# Q7: synthesis screening budget
T_syn = n_t * B * minutes_per_screening / 60
print(f"CLAIM Q7: computed={T_syn} expected=5.0 match={'yes' if math.isclose(T_syn, 5.0, rel_tol=1e-6) else 'no'}")

# Q8: total expert budget
T_total = T_rate3 + T_syn
print(f"CLAIM Q8: computed={T_total} expected=20.0 match={'yes' if math.isclose(T_total, 20.0, rel_tol=1e-6) else 'no'}")

matched = sum(1 for r in [
    N_rend == 40,
    pairs == 6,
    N_hyp == 60,
    E_total == 180,
    math.isclose(T_rate, 5.0, rel_tol=1e-6),
    math.isclose(T_rate3, 15.0, rel_tol=1e-6),
    math.isclose(T_syn, 5.0, rel_tol=1e-6),
    math.isclose(T_total, 20.0, rel_tol=1e-6),
] if r)
print(f"VERIFICATION SUMMARY: 8 claims, {matched} match, {8 - matched} mismatch")

```

## Execution output
```
CLAIM Q1: computed=40 expected=40 match=yes
CLAIM Q2: computed=6 expected=6 match=yes
CLAIM Q3: computed=60 expected=60 match=yes
CLAIM Q4: computed=180 expected=180 match=yes
CLAIM Q5: computed=5.0 expected=5.0 match=yes
CLAIM Q6: computed=15.0 expected=15.0 match=yes
CLAIM Q7: computed=5.0 expected=5.0 match=yes
CLAIM Q8: computed=20.0 expected=20.0 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
