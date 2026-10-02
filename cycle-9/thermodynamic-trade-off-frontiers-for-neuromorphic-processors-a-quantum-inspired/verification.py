import math

def close(a, b):
    if b is None:
        return False
    if isinstance(b, tuple):
        return all(math.isclose(x, y, rel_tol=1e-6) for x, y in zip(a, b)) and len(a) == len(b)
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1
k_B, T = 1.380649e-23, 300.0
E_L = k_B * T * math.log(2)
results.append(("Q1", E_L, 2.87e-21))

# Q2
C_s, dV = 1.0e-13, 0.5
E_sw = C_s * dV**2
results.append(("Q2", E_sw, 2.5e-14))

# Q3
rho = E_sw / (k_B * T * math.log(2))
results.append(("Q3", rho, 8.7e6))

# Q4
alpha = 0.9
E_eff = E_sw * (1 - alpha)
rho4 = E_eff / (k_B * T * math.log(2))
results.append(("Q4", (E_eff, rho4), (2.5e-15, 8.7e5)))

# Q5
R_on, V_th = 1e4, 0.45
t_sw = R_on * C_s * math.log(V_th / (V_th - dV))
f_max = 1 / t_sw
results.append(("Q5", (t_sw, f_max), (2.2e-9, 4.6e8)))

# Q6
hbar = 1.0546e-34
E6 = 5.0e-14
t_ML = hbar / (2 * E6)
ratio = t_sw / t_ML
results.append(("Q6", (t_ML, ratio), (2.1e-21, 1e12)))

# Q7
P_leak = 1e-11
leaks = [P_leak / f for f in (1, 100, 10000)]
results.append(("Q7", tuple(leaks), (1.0e-11, 1.0e-13, 1.0e-15)))

# Q8
f_cross = P_leak / E_sw
results.append(("Q8", f_cross, 400.0))

match_count = 0
for cid, comp, exp in results:
    ok = close(comp, exp)
    if ok:
        match_count += 1
    if isinstance(comp, tuple):
        cs = "(" + ", ".join(f"{v:.6g}" for v in comp) + ")"
        es = "(" + ", ".join(f"{v:.6g}" for v in exp) + ")"
    else:
        cs, es = f"{comp:.6g}", f"{exp:.6g}"
    print(f"CLAIM {cid}: computed={cs} expected={es} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results)-match_count} mismatch")
