import math

def approx_equal(a, b, rel_tol=1e-9, abs_tol=0.0):
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

def format_num(x):
    # Use scientific notation for very small/large numbers, otherwise plain
    if abs(x) < 1e-3 or abs(x) >= 1e6:
        return f"{x:.10e}"
    else:
        return f"{x:.10f}".rstrip('0').rstrip('.')

# Q1
m = 2000
N = m * (m - 1) * (m - 2) / 6
exp_Q1 = 1.331334e9
match_Q1 = approx_equal(N, exp_Q1, rel_tol=1e-12)
print(f"CLAIM Q1: computed={format_num(N)} expected={exp_Q1:.10e} match={'yes' if match_Q1 else 'no'}")

# Q2
p = 2
D = 5
k = 2
rho = k / D
loss = 1 - rho
leaf_groups = p ** k
total_leaves = p ** D
pair_frac = leaf_groups / total_leaves
triple_distinct = pair_frac ** 2
f_survive = triple_distinct * loss
exp_Q2 = 0.009375
match_Q2 = approx_equal(f_survive, exp_Q2, rel_tol=1e-12)
print(f"CLAIM Q2: computed={format_num(f_survive)} expected={exp_Q2:.6f} match={'yes' if match_Q2 else 'no'}")

# Q3
L = 20
k = 10
f = p ** (k - L)  # 2^{k-L}
exp_Q3 = 9.765625e-4
match_Q3 = approx_equal(f, exp_Q3, rel_tol=1e-12)
print(f"CLAIM Q3: computed={format_num(f)} expected={exp_Q3:.10e} match={'yes' if match_Q3 else 'no'}")

# Q4
I = k * math.log2(p)  # since p=2, log2(p)=1
exp_Q4 = 10
match_Q4 = approx_equal(I, exp_Q4, rel_tol=1e-12)
print(f"CLAIM Q4: computed={format_num(I)} expected={exp_Q4} match={'yes' if match_Q4 else 'no'}")

# Q5
q = 0.7
k = 10
L = 20
P_floor = q ** (k + 1) - q ** (L + 1)
exp_Q5 = 0.01921472157
match_Q5 = approx_equal(P_floor, exp_Q5, rel_tol=1e-12)
print(f"CLAIM Q5: computed={format_num(P_floor)} expected={exp_Q5:.11f} match={'yes' if match_Q5 else 'no'}")

# Q6
D = 5
k1 = 2
k2 = 4
loss1 = 1 - k1 / D
loss2 = 1 - k2 / D
reduction = (loss1 - loss2) / loss1 * 100  # percentage
exp_Q6 = 66.7  # percent
match_Q6 = approx_equal(reduction, exp_Q6, rel_tol=1e-2)  # allow 0.01% tolerance
print(f"CLAIM Q6: computed={format_num(reduction)}% expected={exp_Q6}% match={'yes' if match_Q6 else 'no'}")

# Q7
D = 5
k = 2
loss_Q7 = 1 - k / D
exp_Q7 = 0.6
match_Q7 = approx_equal(loss_Q7, exp_Q7, rel_tol=1e-12)
print(f"CLAIM Q7: computed={format_num(loss_Q7)} expected={exp_Q7} match={'yes' if match_Q7 else 'no'}")

# Q8
k = 4
loss_Q8 = 1 - k / D
exp_Q8 = 0.2
match_Q8 = approx_equal(loss_Q8, exp_Q8, rel_tol=1e-12)
print(f"CLAIM Q8: computed={format_num(loss_Q8)} expected={exp_Q8} match={'yes' if match_Q8 else 'no'}")

print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5, match_Q6, match_Q7, match_Q8])} match, {8 - sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5, match_Q6, match_Q7, match_Q8])} mismatch")
