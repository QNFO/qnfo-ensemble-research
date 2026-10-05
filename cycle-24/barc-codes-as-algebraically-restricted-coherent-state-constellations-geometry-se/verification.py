import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: d_max = 2*r*sin(pi/N) for N=6 -> r
N = 6
r = 1.0
d_max = 2 * r * math.sin(math.pi / N)
results.append(check("Q1", d_max, r))

# Q2: d_max = sqrt(nbar) where nbar = r^2
nbar = r ** 2
results.append(check("Q2", math.sqrt(nbar), r))

# Q3: nbar=8 -> r = sqrt(8) ≈ 2.8284271, d_max = sqrt(8)
nbar8 = 8.0
r8 = math.sqrt(nbar8)
d8 = math.sqrt(nbar8)
results.append(check("Q3", r8, 2.8284271))
results.append(check("Q3", d8, 2.8284271))

# Q4: worst-case overlap squared at nbar=8: exp(-8*(1-cos(pi/3)))
theta = math.pi / 3
overlap_sq = math.exp(-nbar8 * (1 - math.cos(theta)))
results.append(check("Q4", overlap_sq, math.exp(-4)))

# Q5: adjacent overlap magnitude = sqrt(e^-4) = e^-2
overlap_mag = math.sqrt(overlap_sq)
results.append(check("Q5", overlap_mag, math.exp(-2)))

# Q6: next-nearest (120 deg) overlap squared: exp(-8*1.5) = exp(-12)
theta2 = 2 * math.pi / 3
overlap_sq2 = math.exp(-nbar8 * (1 - math.cos(theta2)))
results.append(check("Q6", overlap_sq2, math.exp(-12)))

# Q7: opposite (180 deg) overlap squared: exp(-8*2) = exp(-16)
theta3 = math.pi
overlap_sq3 = math.exp(-nbar8 * (1 - math.cos(theta3)))
results.append(check("Q7", overlap_sq3, math.exp(-16)))

# Q8: diagonal contribution to <a†a>: (1/6)*(6*8) = 8
diag = (1.0 / N) * (N * nbar8)
results.append(check("Q8", diag, 8.0))

n = len(results)
m = sum(results)
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
