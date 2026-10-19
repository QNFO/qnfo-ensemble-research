import math
from fractions import Fraction

results = []

def check(cid, computed, expected_str, sig=None):
    if expected_str is None:
        match = "no"
        results.append((cid, computed, "none", match))
        return
    exp_val = float(expected_str)
    if sig is None:
        match = "yes" if abs(computed - exp_val) <= 1e-9 * max(1.0, abs(exp_val)) else "no"
    else:
        # round computed to sig significant digits
        if computed == 0:
            rounded = 0.0
        else:
            rounded = round(computed, sig - int(math.floor(math.log10(abs(computed)))) - 1)
        match = "yes" if abs(rounded - exp_val) <= 1e-9 * max(1.0, abs(exp_val)) else "no"
    results.append((cid, computed, expected_str, match))

# Q1: C_tree = N*log2(N) + 2N - 2, N=1024
N = 1024
log2N = math.log2(N)
c_tree = N * log2N + 2 * N - 2
check("Q1", c_tree, "12286", sig=5)

# Q2: C_dot = N^2, N=1024
N = 1024
c_dot = N ** 2
check("Q2", c_dot, "1048576", sig=7)

# Q4: C_dot = N^2 * d, N=512, d=64
N = 512
d = 64
c_dot2 = N ** 2 * d
check("Q4", c_dot2, "16777216", sig=8)

# Q5: C_tree = N^2 * k, N=512, k=8
N = 512
k = 8
c_tree2 = N ** 2 * k
check("Q5", c_tree2, "2097152", sig=7)

def B(p, D):
    return 1 + (p + 1) * (p ** D - 1) / (p - 1)

# Q8: B_2(5)
b = B(2, 5)
check("Q8", b, "94", sig=2)

# Q9: B_3(5)
b = B(3, 5)
check("Q9", b, "485", sig=3)

# Q10: B_2(2)*B_3(2)
b = B(2, 2) * B(3, 2)
check("Q10", b, "170", sig=3)

# Q11: B_2(2)
b = B(2, 2)
check("Q11", b, "10", sig=2)

# Q12: B_3(2)
b = B(3, 2)
check("Q12", b, "17", sig=2)

# Q13: rho = 2*sqrt(p)/(p+1), p=2
p = 2
rho = 2 * math.sqrt(p) / (p + 1)
check("Q13", rho, "0.9428", sig=4)

# Q14: Delta = 1 - rho
delta = 1.0 - rho
check("Q14", delta, "0.0572", sig=3)

# Q15: T_mix = ln(1/eps)/Delta, eps=0.01
eps = 0.01
t_mix = math.log(1.0 / eps) / delta
check("Q15", t_mix, "80.5", sig=3)

# Q16: Delta_q = 2*Delta
delta_q = 2 * delta
check("Q16", delta_q, "0.1144", sig=4)

# Q17: T_mix_q = ln(1/eps)/Delta_q
t_mix_q = math.log(1.0 / eps) / delta_q
check("Q17", t_mix_q, "40.3", sig=3)

# Q18: t_cl(5) = 25
check("Q18", 5 ** 2, "25", sig=2)

# Q19: t_bal(5) = 5
check("Q19", 5, "5", sig=1)

for cid, computed, expected, match in results:
    print("CLAIM %s: computed=%.8g expected=%s match=%s" % (cid, computed, expected, match))

n = len(results)
m = sum(1 for r in results if r[3] == "yes")
k_mis = n - m
print("VERIFICATION SUMMARY: %d claims, %d match, %d mismatch" % (n, m, k_mis))
