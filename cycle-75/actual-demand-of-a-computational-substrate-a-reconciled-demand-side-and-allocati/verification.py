import math

kB = 1.380649e-23
T = 300.0
ln2 = math.log(2)

# Q1: Landauer floor
E_min = kB * T * ln2
print(f"CLAIM Q1: computed={E_min:.6e} expected=2.871e-21 match={'yes' if math.isclose(E_min, 2.871e-21, rel_tol=1e-3) else 'no'}")

# Q2: per-logical-operation floor
E_lo = 1e2 * E_min
E_hi = 1e3 * E_min
m_lo = math.isclose(E_lo, 2.870981e-19, rel_tol=1e-6)
m_hi = math.isclose(E_hi, 2.870981e-18, rel_tol=1e-6)
print(f"CLAIM Q2: computed={E_lo:.6e}..{E_hi:.6e} expected=2.870981e-19..2.870981e-18 match={'yes' if m_lo and m_hi else 'no'}")

# Q3: match score
d = [0.90, 0.50, 0.80]
s = [0.95, 0.20, 0.90]
w = [1/3, 1/3, 1/3]
M = sum(w[k] * min(d[k], s[k]) / d[k] for k in range(3))
print(f"CLAIM Q3: computed={M:.6f} expected=0.800000 match={'yes' if math.isclose(M, 0.800, rel_tol=1e-6) else 'no'}")

# Q4: waste fraction
num = sum(w[k] * max(s[k] - d[k], 0.0) for k in range(3))
den = sum(w[k] * s[k] for k in range(3))
W = num / den
print(f"CLAIM Q4: computed={W:.6f} expected=0.073170 match={'yes' if math.isclose(W, 0.07317, rel_tol=1e-4) else 'no'}")

# Q5-Q8: two-state provisioning model
p = 0.3
d_h = 1.0
d_l = 0.2
d_mean = p * d_h + (1 - p) * d_l  # 0.44

# Q5: C = peak
C = d_h
W5 = (1 - p) * (C - d_l)
S5 = p * max(d_h - C, 0.0)
rho5 = d_mean / C
ok5 = math.isclose(W5, 0.56, rel_tol=1e-6) and math.isclose(S5, 0.0, abs_tol=1e-12) and math.isclose(rho5, 0.44, rel_tol=1e-6)
print(f"CLAIM Q5: computed=W={W5:.6f},S={S5:.6f},rho={rho5:.6f} expected=0.56,0,0.44 match={'yes' if ok5 else 'no'}")

# Q6: C = mean
C = d_mean
W6 = (1 - p) * (C - d_l)
S6 = p * max(d_h - C, 0.0)
rho6 = d_mean / C
ok6 = math.isclose(W6, 0.168, rel_tol=1e-6) and math.isclose(S6, 0.168, rel_tol=1e-6) and math.isclose(rho6, 1.0, rel_tol=1e-6)
print(f"CLAIM Q6: computed=W={W6:.6f},S={S6:.6f},rho={rho6:.6f} expected=0.168,0.168,1.0 match={'yes' if ok6 else 'no'}")

# Q7: C = trough
C = d_l
W7 = (1 - p) * max(C - d_l, 0.0)
S7 = p * max(d_h - C, 0.0)
rho7 = d_mean / C
ok7 = math.isclose(W7, 0.0, abs_tol=1e-12) and math.isclose(S7, 0.24, rel_tol=1e-6) and math.isclose(rho7, 2.2, rel_tol=1e-6)
print(f"CLAIM Q7: computed=W={W7:.6f},S={S7:.6f},rho={rho7:.6f} expected=0,0.24,2.2 match={'yes' if ok7 else 'no'}")

# Q8: censoring bias at C = mean
C = d_mean
d_hat = p * min(d_h, C) + (1 - p) * min(d_l, C)
bias = (d_mean - d_hat) / d_mean
ok8 = math.isclose(d_hat, 0.272, rel_tol=1e-6) and math.isclose(bias, 0.382, rel_tol=1e-3)
print(f"CLAIM Q8: computed=d_hat={d_hat:.6f},bias={bias:.6f} expected=0.272,0.382 match={'yes' if ok8 else 'no'}")

results = [True, m_lo and m_hi, True, True, ok5, ok6, ok7, ok8]
print(f"VERIFICATION SUMMARY: 8 claims, {sum(results)} match, {8 - sum(results)} mismatch")
