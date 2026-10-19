# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "State‑vector dimension after $t=10^{3}$ steps is $d_{1000}=4002$.",
    "inputs": "d_c=2, t=1000",
    "formula": "d_t = d_c * (2*t + 1)"
  },
  {
    "id": "Q2",
    "statement": "State‑vector dimension after $t=10^{6}$ steps is $d_{10^{6}}=4{,}000{,}002$.",
    "inputs": "d_c=2, t=1000000",
    "formula": "d_t = d_c * (2*t + 1)"
  },
  {
    "id": "Q3",
    "statement": "Dense unitarity‑check cost for $t=10^{3}$ is $64{,}096{,}048{,}008$ multiply‑adds.",
    "inputs": "d_t=4002",
    "formula": "cost = d_t^3"
  },
  {
    "id": "Q4",
    "statement": "Sparse unitarity‑check cost for $t=10^{3}$ is $64{,}064{,}016$ multiply‑adds.",
    "inputs": "d_t=4002, k=2",
    "formula": "cost = k^2 * d_t^2   (with k=2 gives 4*d_t^2)"
  },
  {
    "id": "Q5",
    "statement": "Speedup factor of dense over sparse unitarity check is $1000.5$.",
    "inputs": "d_t=4002",
    "formula": "speedup = d_t / 4"
  },
  {
    "id": "Q6",
    "statement": "Number of unitarity constraints is $16{,}020{,}006$.",
    "inputs": "d_t=4002",
    "formula": "constraints = d_t * (d_t + 1)"
  },
  {
    "id": "Q7",
    "statement": "Simulation multiplication count for $t=1000$ is $8{,}016{,}000$ real multiplications.",
    "inputs": "t=1000",
    "formula": "M_t = 8 * t * (t + 2)"
  },
  {
    "id": "Q8",
    "statement": "Verification overhead ratio (normalization check vs simulation) is $50\\%$.",
    "inputs": "d_t (cancels)",
    "formula": "overhead = (4*d_t) / (8*d_t) = 0.5"
  },
  {
    "id": "Q9",
    "statement": "Naïve contract clause count for $t=1000$ is $5{,}000$.",
    "inputs": "t=1000",
    "formula": "K_t = 5 * t"
  },
  {
    "id": "Q10",
    "statement": "Projected double‑precision drift bound after $t=10^{6}$ steps is $\\approx 8.88\\times10^{-10}$.",
    "inputs": "t=1000000, epsilon_fp=2.2204e-16",
    "formula": "delta_t = 4 * t * epsilon_fp"
  },
  {
    "id": "Q11",
    "statement": "Graph‑generalized sparse‑over‑dense speedup for $N=100$, $k=3$ is $\\approx 33.33$.",
    "inputs": "N=100, k=3",
    "formula": "speedup = N / k"
  },
  {
    "id": "Q12",
    "statement": "Dense cost for graph‑generalized walk with $N=100$ is $1{,}000{,}000$ multiply‑adds.",
    "inputs": "N=100",
    "formula": "cost = N^3"
  },
  {
    "id": "Q13",
    "statement": "Sparse cost for graph‑generalized walk with $N=100$, $k=3$ is $90{,}000$ multiply‑adds.",
    "inputs": "N=100, k=3",
    "formula": "cost = k^2 * N^2"
  },
  {
    "id": "Q14",
    "statement": "Projected block‑diagonalization cost for the 3‑cycle periodicity contract is $432$ multiply‑adds.",
    "inputs": "block size=3, number of blocks=3, per‑block transform cost=27, eigenvalue extraction cost=351",
    "formula": "cost = (3 * 27) + 351"
  },
  {
    "id": "Q15",
    "statement": "Trace‑conservation check cost for a density matrix of dimension $d_t$ is $2 d_t$ additions and zero multiplications.",
    "inputs": "d_t",
    "formula": "cost = 2 * d_t additions"
  },
  {
    "id": "Q16",
    "statement": "Verified fraction of benchmark functions in [7] is $88.5\\%$.",
    "inputs": "verified=23, total=26",
    "formula": "fraction = (verified / total) * 100"
  }
]

## Script
```python
import math

def fmt(val, fmt_type):
    if fmt_type == 'int':
        return str(int(val))
    if fmt_type == '1dp':
        return f"{val:.1f}"
    if fmt_type == '2dp':
        return f"{val:.2f}"
    if fmt_type == 'sci2':
        return f"{val:.2e}"
    return str(val)

# Expected values and formatting types
expected = {
    'Q1': ('4002', 'int'),
    'Q2': ('4000002', 'int'),
    'Q3': ('64096048008', 'int'),
    'Q4': ('64064016', 'int'),
    'Q5': ('1000.5', '1dp'),
    'Q6': ('16020006', 'int'),
    'Q7': ('8016000', 'int'),
    'Q8': ('0.5', '1dp'),
    'Q9': ('5000', 'int'),
    'Q10': ('8.88e-10', 'sci2'),
    'Q11': ('33.33', '2dp'),
    'Q12': ('1000000', 'int'),
    'Q13': ('90000', 'int'),
    'Q14': ('432', 'int'),
    'Q15': ('8004', 'int'),   # using d_t = 4002 as example
    'Q16': ('88.5', '1dp')
}

# Compute claims
d_c = 2
t1 = 1000
t2 = 1_000_000
d_t1 = d_c * (2 * t1 + 1)          # Q1, Q2 uses t2 later
d_t2 = d_c * (2 * t2 + 1)          # Q2
cost_dense = d_t1 ** 3              # Q3
cost_sparse = 4 * (d_t1 ** 2)       # Q4 (k=2 => k^2=4)
speedup_dense_sparse = d_t1 / 4     # Q5
constraints = d_t1 * (d_t1 + 1)     # Q6
M_t = 8 * t1 * (t1 + 2)             # Q7
overhead_ratio = 0.5                # Q8
K_t = 5 * t1                        # Q9
epsilon_fp = 2.2204e-16
delta = 4 * t2 * epsilon_fp        # Q10
N = 100
k = 3
speedup_graph = N / k               # Q11
dense_graph = N ** 3                # Q12
sparse_graph = k ** 2 * N ** 2      # Q13
block_cost = (3 * 27) + 351         # Q14
trace_cost = 2 * d_t1               # Q15 (additions)
verified = 23
total = 26
fraction = (verified / total) * 100 # Q16

# Prepare computed values with appropriate formatting
computed = {
    'Q1': fmt(d_t1, 'int'),
    'Q2': fmt(d_t2, 'int'),
    'Q3': fmt(cost_dense, 'int'),
    'Q4': fmt(cost_sparse, 'int'),
    'Q5': fmt(speedup_dense_sparse, '1dp'),
    'Q6': fmt(constraints, 'int'),
    'Q7': fmt(M_t, 'int'),
    'Q8': fmt(overhead_ratio, '1dp'),
    'Q9': fmt(K_t, 'int'),
    'Q10': fmt(delta, 'sci2'),
    'Q11': fmt(speedup_graph, '2dp'),
    'Q12': fmt(dense_graph, 'int'),
    'Q13': fmt(sparse_graph, 'int'),
    'Q14': fmt(block_cost, 'int'),
    'Q15': fmt(trace_cost, 'int'),
    'Q16': fmt(fraction, '1dp')
}

# Print results
for qid in sorted(expected.keys()):
    exp_val, _ = expected[qid]
    comp_val = computed[qid]
    match = 'yes' if comp_val == exp_val else 'no'
    print(f"CLAIM {qid}: computed={comp_val} expected={exp_val} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if computed[q]==expected[q][0])} match, {len(expected)-sum(1 for q in expected if computed[q]==expected[q][0])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4002 expected=4002 match=yes
CLAIM Q10: computed=8.88e-10 expected=8.88e-10 match=yes
CLAIM Q11: computed=33.33 expected=33.33 match=yes
CLAIM Q12: computed=1000000 expected=1000000 match=yes
CLAIM Q13: computed=90000 expected=90000 match=yes
CLAIM Q14: computed=432 expected=432 match=yes
CLAIM Q15: computed=8004 expected=8004 match=yes
CLAIM Q16: computed=88.5 expected=88.5 match=yes
CLAIM Q2: computed=4000002 expected=4000002 match=yes
CLAIM Q3: computed=64096048008 expected=64096048008 match=yes
CLAIM Q4: computed=64064016 expected=64064016 match=yes
CLAIM Q5: computed=1000.5 expected=1000.5 match=yes
CLAIM Q6: computed=16020006 expected=16020006 match=yes
CLAIM Q7: computed=8016000 expected=8016000 match=yes
CLAIM Q8: computed=0.5 expected=0.5 match=yes
CLAIM Q9: computed=5000 expected=5000 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 4002 | 4002 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 8.88e-10 | 8.88e-10 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 33.33 | 33.33 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 1000000 | 1000000 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q13 | 90000 | 90000 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q14 | 432 | 432 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 8004 | 8004 | yes | match | 4 significant digits (as printed, at least 3) |
| Q16 | 88.5 | 88.5 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 4000002 | 4000002 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 64096048008 | 64096048008 | yes | match | 11 significant digits (as the paper states, at least 2) |
| Q4 | 64064016 | 64064016 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q5 | 1000.5 | 1000.5 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 16020006 | 16020006 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q7 | 8016000 | 8016000 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 5000 | 5000 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
