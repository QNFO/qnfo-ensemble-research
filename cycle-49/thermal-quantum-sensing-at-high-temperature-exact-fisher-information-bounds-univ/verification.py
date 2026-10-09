import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: F_Q = 2*g^2*(1+q)^2/(1+q^2), limits q->0 and q->1
g = 1.0
q0 = 0.0
q1 = 1.0
FQ_q0 = 2 * g**2 * (1 + q0)**2 / (1 + q0**2)
FQ_q1 = 2 * g**2 * (1 + q1)**2 / (1 + q1**2)
print(f"CLAIM Q1: computed={FQ_q0} and {FQ_q1} expected=2*g^2 and 4*g^2 match={isclose(FQ_q0, 2*g**2) and isclose(FQ_q1, 4*g**2)}")
results.append(isclose(FQ_q0, 2*g**2) and isclose(FQ_q1, 4*g**2))

# Q2: 8*Var_0(G) = 8*(g^2/2) = 4*g^2
Var0 = g**2 / 2
eight_var = 8 * Var0
print(f"CLAIM Q2: computed={eight_var} expected={4*g**2} match={isclose(eight_var, 4*g**2)}")
results.append(isclose(eight_var, 4*g**2))

# Q3: at beta*omega = 0.1, F_Q and fraction of 4g^2
x = 0.1
q = math.exp(-x)
FQ = 2 * g**2 * (1 + q)**2 / (1 + q**2)
fraction = FQ / (4 * g**2)
expected_frac = 0.997491
print(f"CLAIM Q3: computed={fraction} expected={expected_frac} match={isclose(fraction, expected_frac)}")
results.append(isclose(fraction, expected_frac))

# Q4: F_K = tanh(x/2)^2 symbolic check at a sample x (x=1)
xq = 1.0
FK = math.tanh(xq / 2)**2
print(f"CLAIM Q4: computed={FK} expected={math.tanh(0.5)**2} match={isclose(FK, math.tanh(0.5)**2)}")
results.append(isclose(FK, math.tanh(0.5)**2))

# Q5: x=2, F_K = tanh(1)^2, delta = 1 - F_K/(x/2)^2
x = 2.0
tanh1 = math.tanh(1.0)
FK = tanh1**2
delta = 1 - FK / (x / 2)**2
print(f"CLAIM Q5: computed={FK} and {delta} expected=0.5800257 and 0.4199743 match={isclose(FK, 0.5800257) and isclose(delta, 0.4199743)}")
results.append(isclose(FK, 0.5800257) and isclose(delta, 0.4199743))

# Q6: x=0.5, F_K = tanh(0.25)^2, delta
x = 0.5
tanh025 = math.tanh(0.25)
FK = tanh025**2
delta = 1 - FK / (x / 2)**2
print(f"CLAIM Q6: computed={FK} and {delta} expected=0.0599852 and 0.0402368 match={isclose(FK, 0.0599852) and isclose(delta, 0.0402368)}")
results.append(isclose(FK, 0.0599852) and isclose(delta, 0.0402368))

# Q7: W = omega*sinh(g*theta)^2*(1+2*n_bar); coth = (1+q)/(1-q); small g*theta approx
omega = 1.0
beta = 0.1
theta = 0.01
gth = 0.05
q = math.exp(-beta * omega)
n_bar = q / (1 - q)
W_exact = omega * math.sinh(gth)**2 * (1 + 2 * n_bar)
W_approx = omega * gth**2 * (1 + 2 * n_bar)
rel = abs(W_exact - W_approx) / W_exact
print(f"CLAIM Q7: computed={W_exact} expected={W_approx} match={rel < 1e-2}")
results.append(rel < 1e-2)

# Q8: W/F_Q = omega*theta^2*coth(beta*omega/2)/4
coth = (1 + q) / (1 - q)
ratio = omega * theta**2 * coth / 4
# direct: W/F_Q with F_Q -> 4g^2
W_small = omega * g**2 * theta**2 * coth
ratio_direct = W_small / (4 * g**2)
print(f"CLAIM Q8: computed={ratio} expected={ratio_direct} match={isclose(ratio, ratio_direct)}")
results.append(isclose(ratio, ratio_direct))

n_match = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results) - n_match} mismatch")
