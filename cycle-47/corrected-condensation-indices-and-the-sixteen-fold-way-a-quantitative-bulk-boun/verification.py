import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: D_C^2 = 1+2+1+2+4+2+1+2+1 = 16
terms = [1, 2, 1, 2, 4, 2, 1, 2, 1]
q1 = sum(terms)
results.append(("Q1", q1, 16))

# Q2: D_C^2 = D_Ising^2 * D_antiIsing^2 = 4*4 = 16
d_ising_sq = 1**2 + (math.sqrt(2))**2 + 1**2
d_anti_sq = 1**2 + (math.sqrt(2))**2 + 1**2
q2 = d_ising_sq * d_anti_sq
results.append(("Q2", q2, 16))

# Q3: D_D^2 = 1^2+1^2+1^2+1^2 = 4
q3 = sum(1**2 for _ in range(4))
results.append(("Q3", q3, 4))

# Q4: kappa = D_C^2 / D_D^2 = 16/4 = 4
q4 = 16 / 4
results.append(("Q4", q4, 4))

# Q5: f_NA = 0/4 = 0
q5 = 0 / 4
results.append(("Q5", q5, 0))

# Q6: f_NA^(parent) = (2+2+4)/16 = 8/16 = 0.5
num = (math.sqrt(2))**2 + (math.sqrt(2))**2 + 2**2
q6 = num / 16
results.append(("Q6", q6, 0.5))

# Q7: mu = 2*(c_C - c_D), c_C = 1/2 + (-1/2) = 0, c_D = 0 -> mu = 0
c_C = 1/2 + (-1/2)
c_D = 0
q7 = 2 * (c_C - c_D)
results.append(("Q7", q7, 0))

# Q8: nu=0 anchor: mu = 2*0 = 0
c_toric = 0
q8 = 2 * c_toric
results.append(("Q8", q8, 0))

match_count = 0
for cid, computed, expected in results:
    m = close(computed, expected)
    if m:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if m else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
