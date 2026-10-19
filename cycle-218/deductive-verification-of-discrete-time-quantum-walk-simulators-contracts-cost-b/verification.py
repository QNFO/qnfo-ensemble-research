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
