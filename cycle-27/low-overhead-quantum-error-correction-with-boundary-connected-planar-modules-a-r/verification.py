import math

def check(id, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        try:
            match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
        except (TypeError, ValueError):
            match = "yes" if computed == expected else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: n_rot(22) = 2*22^2 - 2*22 + 1
d = 22
n_rot_22 = 2 * d**2 - 2 * d + 1
results.append(check("Q1", n_rot_22, 925))

# Q2: 12 patches at d=22
n_SC_12_22 = 12 * n_rot_22
results.append(check("Q2", n_SC_12_22, 11100))

# Q3: total with syndrome qubits ~ 2 * 11100
total_22 = 2 * n_SC_12_22
results.append(check("Q3", total_22, 22200))

# Q4: n_rot(18) and 12 patches at d=18
d18 = 18
n_rot_18 = 2 * d18**2 - 2 * d18 + 1
n_SC_12_18 = 12 * n_rot_18
results.append(check("Q4", n_SC_12_18, 7356))

# Q5: modular memory n_mod = 16k, k=12
k = 12
n_mod = 16 * k
results.append(check("Q5", n_mod, 192))

# Q6: overhead reduction vs d=22 baseline
ratio_22 = n_SC_12_22 / n_mod
results.append(check("Q6", ratio_22, 57.8125))

# Q7: n_mod bound for >=30x
bound = n_SC_12_22 / 30
results.append(check("Q7", bound, 370))

# Q8: overhead reduction vs d=18 baseline
ratio_18 = n_SC_12_18 / n_mod
results.append(check("Q8", ratio_18, 38.3125))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
