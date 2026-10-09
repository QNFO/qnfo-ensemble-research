import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: d* for P=1e-12, A=0.1, p=1e-3, p_th=1e-2
A = 0.1
P = 1e-12
p = 1e-3
p_th = 1e-2
d_req = 2 * math.log10(P / A) / math.log10(p / p_th) - 1
d_star = math.ceil(d_req)
if d_star % 2 == 0:
    d_star += 1
computed_q1 = d_star
results.append(("Q1", computed_q1, 21))

# Q2: N_phys at d=21
d = 21
N_phys = 2 * d**2 - 1
results.append(("Q2", N_phys, 881))

# Q3: p_L check at d=21
p_L = A * (p / p_th) ** ((d + 1) / 2)
results.append(("Q3", p_L, 1e-12))

# Q4: B = d*(d^2-1)
B = d * (d**2 - 1)
results.append(("Q4", B, 9240))

# Q5: bits per cycle and rate
bits_per_cycle = d**2 - 1
tau_c = 1e-6
R_cyc = bits_per_cycle / tau_c
results.append(("Q5", R_cyc, 4.40e8))

# Q6: E_L = (2d^2-1)*d*eps_q
eps_q = 1e-9
E_L = (2 * d**2 - 1) * d * eps_q
results.append(("Q6", E_L, 1.8501e-5))

# Q7: E_cyc = (2d^2-1)*eps_q
E_cyc = (2 * d**2 - 1) * eps_q
results.append(("Q7", E_cyc, 8.81e-7))

# Q8: Landauer limit at T=0.3 K
k_B = 1.380649e-23
T = 0.3
E_Land = k_B * T * math.log(2)
results.append(("Q8", E_Land, 2.87098e-24))

match_count = 0
for cid, computed, expected in results:
    match = isclose(float(computed), float(expected))
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
