import math

kB = 1.380649e-23
T = 300.0
ln2 = math.log(2)

# Q1: log10(2^(2^64)) = 2^64 * log10(2)
log10_2 = math.log10(2)
q1 = (2**64) * log10_2
print(f"CLAIM Q1: computed={q1:.6e} expected=5.553e18 match="
      f"{'yes' if math.isclose(q1, 5.553e18, rel_tol=1e-3) else 'no'}")

# Q2: sum_{j=0}^{8} binom(128, j)
from math import comb
q2 = sum(comb(128, j) for j in range(9))
print(f"CLAIM Q2: computed={q2:.6e} expected=1.53e12 match="
      f"{'yes' if math.isclose(q2, 1.53e12, rel_tol=1e-2) else 'no'}")

# Q3: E_bit = kB * T * ln2
q3 = kB * T * ln2
print(f"CLAIM Q3: computed={q3:.6e} expected=2.8709e-21 match="
      f"{'yes' if math.isclose(q3, 2.8709e-21, rel_tol=1e-4) else 'no'}")

# Q4: P_erase = f_cycle * N_dist * E_bit, f=1, N=1e9
q4 = 1.0 * 1e9 * q3
print(f"CLAIM Q4: computed={q4:.6e} expected=2.8709e-12 match="
      f"{'yes' if math.isclose(q4, 2.8709e-12, rel_tol=1e-4) else 'no'}")

# Q5: P_erase = 1e9 * 1e20 * E_bit
q5 = 1e9 * 1e20 * q3
print(f"CLAIM Q5: computed={q5:.6e} expected=2.87e8 match="
      f"{'yes' if math.isclose(q5, 2.87e8, rel_tol=1e-3) else 'no'}")

# Q6: N_max = P_obs * tau / (kB*T*ln2), P_obs=1e-12, tau=1
q6 = 1e-12 * 1.0 / (kB * T * ln2)
print(f"CLAIM Q6: computed={q6:.6e} expected=3.4832e8 match="
      f"{'yes' if math.isclose(q6, 3.4832e8, rel_tol=1e-4) else 'no'}")

# Q7: S = 40 * kB * ln2
q7 = 40 * kB * ln2
print(f"CLAIM Q7: computed={q7:.6e} expected=3.82785e-22 match="
      f"{'yes' if math.isclose(q7, 3.82785e-22, rel_tol=1e-4) else 'no'}")

# Q8: E_erase = S * T
q8 = q7 * T
print(f"CLAIM Q8: computed={q8:.6e} expected=1.14836e-19 match="
      f"{'yes' if math.isclose(q8, 1.14836e-19, rel_tol=1e-4) else 'no'}")

claims = [q1, q2, q3, q4, q5, q6, q7, q8]
expected = [5.553e18, 1.53e12, 2.8709e-21, 2.8709e-12, 2.87e8, 3.4832e8, 3.82785e-22, 1.14836e-19]
tols = [1e-3, 1e-2, 1e-4, 1e-4, 1e-3, 1e-4, 1e-4, 1e-4]
m = sum(1 for c, e, t_ in zip(claims, expected, tols) if math.isclose(c, e, rel_tol=t_))
print(f"VERIFICATION SUMMARY: 8 claims, {m} match, {8 - m} mismatch")
