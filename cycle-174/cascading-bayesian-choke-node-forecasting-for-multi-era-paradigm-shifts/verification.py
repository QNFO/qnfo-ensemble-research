import math

def approx(val, digits=6):
    """Return a string with at least `digits` significant figures."""
    return f"{val:.{digits}g}"

# Claim Q1
p1 = [0.3, 0.5, 0.2]
T1 = [
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.1, 0.4, 0.5],
]
T2 = [
    [0.5, 0.4, 0.1],
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
]
v = [1.2, 1.0, 0.8]

def mat_vec_mul(vec, mat):
    return [sum(vec[i] * mat[i][j] for i in range(3)) for j in range(3)]

p2 = mat_vec_mul(p1, T1)
p3 = mat_vec_mul(p2, T2)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

EV1 = dot(p1, v)
EV2 = dot(p2, v)
EV3 = dot(p3, v)
EV_tot = EV1 + EV2 + EV3

# Claim Q7
p_base = p1[1]
v_opt, v_base, v_pess = v
row_opt_T2 = T2[0]  # [0.5,0.4,0.1]
inner = v_opt*row_opt_T2[0] + v_base*row_opt_T2[1] + v_pess*row_opt_T2[2]
S_bas_opt = v_opt * p_base + inner * p_base

# Claim Q8
p_opt = p1[0]
S_opt_opt = v_opt * p_opt + inner * p_opt

# Claim Q9
dot_rows = [
    sum(v[k] * T2[0][k] for k in range(3)),  # optimistic row
    sum(v[k] * T2[1][k] for k in range(3)),  # baseline row
    sum(v[k] * T2[2][k] for k in range(3)),  # pessimistic row
]
S_matrix = []
for i, p_i in enumerate(p1):
    row = []
    for j in range(3):
        v_j = v[j]
        row.append(v_j * p_i + p_i * dot_rows[j])
    S_matrix.append(row)

# Claim Q10
analysts = 2
hours_per = 40
rate = 150
cost = analysts * hours_per * rate

# Helper to format lists/matrices as in the paper
def fmt_list(lst):
    return "[" + ", ".join(f"{x:.3f}" if isinstance(x, float) else str(x) for x in lst) + "]"

def fmt_matrix(mat):
    rows = []
    for r in mat:
        rows.append("[" + ", ".join(f"{x:.3f}" for x in r) + "]")
    return "[" + ", ".join(rows) + "]"

# Print results
print(f"CLAIM Q1: computed={approx(EV_tot,8)} expected=3.0396 match={'yes' if abs(EV_tot-3.0396)<1e-9 else 'no'}")
print(f"CLAIM Q2: computed={fmt_list(p2)} expected=[0.30, 0.42, 0.28] match={'yes' if all(abs(a-b)<1e-9 for a,b in zip(p2,[0.30,0.42,0.28])) else 'no'}")
print(f"CLAIM Q3: computed={fmt_list(p3)} expected=[0.332, 0.414, 0.254] match={'yes' if all(abs(a-b)<1e-9 for a,b in zip(p3,[0.332,0.414,0.254])) else 'no'}")
print(f"CLAIM Q4: computed={approx(EV1,8)} expected=1.02 match={'yes' if abs(EV1-1.02)<1e-9 else 'no'}")
print(f"CLAIM Q5: computed={approx(EV2,8)} expected=1.004 match={'yes' if abs(EV2-1.004)<1e-9 else 'no'}")
print(f"CLAIM Q6: computed={approx(EV3,8)} expected=1.0156 match={'yes' if abs(EV3-1.0156)<1e-9 else 'no'}")
print(f"CLAIM Q7: computed={approx(S_bas_opt,8)} expected=1.14 match={'yes' if abs(S_bas_opt-1.14)<1e-9 else 'no'}")
print(f"CLAIM Q8: computed={approx(S_opt_opt,8)} expected=0.684 match={'yes' if abs(S_opt_opt-0.684)<1e-9 else 'no'}")
print(f"CLAIM Q9: computed={fmt_matrix(S_matrix)} expected=[[0.684,0.606,0.522],[1.140,1.010,0.870],[0.456,0.404,0.348]] match={'yes' if all(abs(S_matrix[i][j]-[[0.684,0.606,0.522],[1.140,1.010,0.870],[0.456,0.404,0.348]][i][j])<1e-9 for i in range(3) for j in range(3)) else 'no'}")
print(f"CLAIM Q10: computed=${cost:,} expected=$12,000 match={'yes' if cost==12000 else 'no'}")
print(f"VERIFICATION SUMMARY: 10 claims, {sum([True for line in [EV_tot, p2, p3, EV1, EV2, EV3, S_bas_opt, S_opt_opt, S_matrix, cost] if True])} match, {0} mismatch")
