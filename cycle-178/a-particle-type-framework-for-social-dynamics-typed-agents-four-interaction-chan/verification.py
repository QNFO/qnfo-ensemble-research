import math

def fmt(val, fmt_str):
    return format(val, fmt_str)

# Expected values as strings
expected = {
    "Q1": "0.19231",
    "Q2": "0.25",
    "Q3": "0.2308",
    "Q4": "0.6667",
    "Q5": "3.467",
    "Q6": "0.39347",
    "Q7": "0.09516",
    "Q8": "4.134",
    "Q9": "40",
    "Q10": "15.74",
    "Q11": "78.70",
    "Q12": "0.34",
    "Q13": "2.9412",
    "Q14": "60",
    "Q15": "60",
    "Q16": "207.24",
}

# Computations
theta = 0.2
k_bar = 10
w_L = 0.08
mu = 3
f_M = 0.10
w_h = 0.03
lambda_w = 1e-2
g_B = 0.5
g_L = 0.1
T = 100
f_B = 0.04
N = 1000
f_D = 0.66
q = 0.5
ln_n = 6.90776
delta_k = 60
n = 1000

# Q1
f_L_crit = theta / (k_bar * w_L * (1 + mu * f_M))
c1 = fmt(f_L_crit, ".5f")
print(f"CLAIM Q1: computed={c1} expected={expected['Q1']} match={'yes' if c1==expected['Q1'] else 'no'}")

# Q2
f_no_med = theta / (k_bar * w_L)
c2 = fmt(f_no_med, ".2f")
print(f"CLAIM Q2: computed={c2} expected={expected['Q2']} match={'yes' if c2==expected['Q2'] else 'no'}")

# Q3
rel_red = (f_no_med - f_L_crit) / f_no_med
c3 = fmt(rel_red, ".4f")
print(f"CLAIM Q3: computed={c3} expected={expected['Q3']} match={'yes' if c3==expected['Q3'] else 'no'}")

# Q4
f_h_crit = theta / (k_bar * w_h)
c4 = fmt(f_h_crit, ".4f")
print(f"CLAIM Q4: computed={c4} expected={expected['Q4']} match={'yes' if c4==expected['Q4'] else 'no'}")

# Q5
ratio = f_h_crit / f_L_crit
c5 = fmt(ratio, ".3f")
print(f"CLAIM Q5: computed={c5} expected={expected['Q5']} match={'yes' if c5==expected['Q5'] else 'no'}")

# Q6
p_B = 1 - math.exp(-lambda_w * g_B * T)
c6 = fmt(p_B, ".5f")
print(f"CLAIM Q6: computed={c6} expected={expected['Q6']} match={'yes' if c6==expected['Q6'] else 'no'}")

# Q7
p_L = 1 - math.exp(-lambda_w * g_L * T)
c7 = fmt(p_L, ".5f")
print(f"CLAIM Q7: computed={c7} expected={expected['Q7']} match={'yes' if c7==expected['Q7'] else 'no'}")

# Q8
ratio_pb_pl = p_B / p_L
c8 = fmt(ratio_pb_pl, ".3f")
print(f"CLAIM Q8: computed={c8} expected={expected['Q8']} match={'yes' if c8==expected['Q8'] else 'no'}")

# Q9
N_B = f_B * N
c9 = fmt(N_B, ".0f")
print(f"CLAIM Q9: computed={c9} expected={expected['Q9']} match={'yes' if c9==expected['Q9'] else 'no'}")

# Q10
N_B_conv = N_B * p_B
c10 = fmt(N_B_conv, ".2f")
print(f"CLAIM Q10: computed={c10} expected={expected['Q10']} match={'yes' if c10==expected['Q10'] else 'no'}")

# Q11
N2 = 15.74 * k_bar * q  # using the given rounded N_B^{conv}=15.74
c11 = fmt(N2, ".2f")
print(f"CLAIM Q11: computed={c11} expected={expected['Q11']} match={'yes' if c11==expected['Q11'] else 'no'}")

# Q12
f_obs = 1 - f_D
c12 = fmt(f_obs, ".2f")
print(f"CLAIM Q12: computed={c12} expected={expected['Q12']} match={'yes' if c12==expected['Q12'] else 'no'}")

# Q13
bias = 1 / f_obs
c13 = fmt(bias, ".4f")
print(f"CLAIM Q13: computed={c13} expected={expected['Q13']} match={'yes' if c13==expected['Q13'] else 'no'}")

# Q14
c14 = fmt(delta_k, ".0f")
print(f"CLAIM Q14: computed={c14} expected={expected['Q14']} match={'yes' if c14==expected['Q14'] else 'no'}")

# Q15
gain_AIC = delta_k
c15 = fmt(gain_AIC, ".0f")
print(f"CLAIM Q15: computed={c15} expected={expected['Q15']} match={'yes' if c15==expected['Q15'] else 'no'}")

# Q16
gain_BIC = (delta_k * ln_n) / 2
c16 = fmt(gain_BIC, ".2f")
print(f"CLAIM Q16: computed={c16} expected={expected['Q16']} match={'yes' if c16==expected['Q16'] else 'no'}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for k in expected if eval('c'+k[-1])==expected[k])} match, {sum(1 for k in expected if eval('c'+k[-1])!=expected[k])} mismatch")
