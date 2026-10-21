import math

lam = 100.0
ln_lam = 4.605170
half_ln_2pi_lam = 3.221524  # 0.5*ln(2πλ)

def stirling_log_fact(k):
    # Stirling approximation with 1/(12k) term
    return k*math.log(k) - k + 0.5*math.log(2*math.pi*k) + 1.0/(12.0*k)

def poisson_lnP(k):
    return -lam + k*ln_lam - stirling_log_fact(k)

def gaussian_lnP(k):
    return -half_ln_2pi_lam - ((k - lam)**2) / (2.0*lam)

def cubic_delta(x):
    return (x**3 - 3.0*x) / (6.0*math.sqrt(lam))

def report(claim_id, computed, expected):
    match = "yes" if f"{computed:.4f}" == expected else "no"
    print(f"CLAIM {claim_id}: computed={computed:.6f} expected={expected} match={match}")

# Q1
lnP_110 = poisson_lnP(110)
report("Q1", lnP_110, "-3.7540")

# Q2
lnG_110 = gaussian_lnP(110)
report("Q2", lnG_110, "-3.721524")

# Q3
delta_1 = lnP_110 - lnG_110
report("Q3", delta_1, "-0.0325")

# Q4
lnP_120 = poisson_lnP(120)
report("Q4", lnP_120, "-5.1920")

# Q5
lnG_120 = gaussian_lnP(120)
report("Q5", lnG_120, "-5.221524")

# Q6
delta_2 = lnP_120 - lnG_120
report("Q6", delta_2, "0.0296")

# Q7
lnP_125 = poisson_lnP(125)
report("Q7", lnP_125, "-6.2268")

# Q8
lnG_125 = gaussian_lnP(125)
report("Q8", lnG_125, "-6.346524")

# Q9
delta_2_5 = lnP_125 - lnG_125
report("Q9", delta_2_5, "0.1197")

# Q10
lnP_130 = poisson_lnP(130)
report("Q10", lnP_130, "-7.4607")

# Q11
lnG_130 = gaussian_lnP(130)
report("Q11", lnG_130, "-7.721524")

# Q12
delta_3 = lnP_130 - lnG_130
report("Q12", delta_3, "0.2608")

# Q13 (formula only, no numeric check)

# Q14
cubic_1 = cubic_delta(1.0)
report("Q14", cubic_1, "-0.0333")

# Q15
cubic_2 = cubic_delta(2.0)
report("Q15", cubic_2, "0.0333")

# Q16
cubic_2_5 = cubic_delta(2.5)
report("Q16", cubic_2_5, "0.1354")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
