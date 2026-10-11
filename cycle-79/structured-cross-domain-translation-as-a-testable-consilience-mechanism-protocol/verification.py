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
