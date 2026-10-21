import math

def approx_match(computed, expected_str, rel_tol=1e-5):
    try:
        expected = float(expected_str.replace('e', 'e'))
    except:
        # handle comma-separated expected values
        parts = [float(p.strip()) for p in expected_str.split(',')]
        return all(abs(computed - p) / p < rel_tol for p in parts)
    return abs(computed - expected) / expected < rel_tol

def print_claim(cid, computed, expected):
    match = "yes" if approx_match(computed, expected) else "no"
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={match}")

# Q1: Ball size n = 1 + (p+1)*(p**t - 1)/(p-1)
p = 3
t = 1
n1 = 1 + (p+1)*(p**t - 1)/(p-1)
print_claim("Q1", n1, "5")

# Q2: Passive logical failure probability
epsilon = 1e-3
t = 1
n = n1
P2 = math.comb(int(n), t+1) * epsilon**(t+1) * (1-epsilon)**(n-t-1)
print_claim("Q2", P2, "9.97003e-6")

# Q3: Suppression factor S = epsilon / P_pass
S = epsilon / P2
print_claim("Q3", S, "100.3")

# Q4: Ball size for t=2
t = 2
n2 = 1 + (p+1)*(p**t - 1)/(p-1)
print_claim("Q4", n2, "17")

# Q5: Passive logical failure for t=2
t = 2
n = n2
P5 = math.comb(int(n), t+1) * epsilon**(t+1) * (1-epsilon)**(n-t-1)
print_claim("Q5", P5, "6.71e-7")

# Q6: Energy barrier E = 2**d
d = 3
E = 2**d
print_claim("Q6", E, "8")

# Q7: Thermal activation bound p = exp(-2**d)
p_thermal = math.exp(-2**d)
print_claim("Q7", p_thermal, "3.3546e-4")

# Q8: Assumed reduction factor
R_scatter = 48
print_claim("Q8", R_scatter, "48")

# Q9: Projected logical error after scattering
P_scatter = P2 / R_scatter
print_claim("Q9", P_scatter, "2.08e-7")

# Q10: Sensitivity derivative 20*epsilon
derivative = 20 * epsilon
print_claim("Q10", derivative, "2.0e-2")

# Q11: Delta P = derivative * delta_epsilon (delta_epsilon = 1e-4)
delta_epsilon = 1e-4
delta_P = derivative * delta_epsilon
print_claim("Q11", delta_P, "2.0e-6")

# Q12: Physical error probabilities from fidelities
epsilon_1q = 1 - 0.9990   # 99.90%
epsilon_2q = 1 - 0.9956   # 99.56%
print_claim("Q12", epsilon_1q, "1.0e-3")
print_claim("Q12", epsilon_2q, "4.4e-3")

# Q13: Surface code logical error approx (epsilon_2q)^2
P_surf = epsilon_2q**2
print_claim("Q13", P_surf, "1.9e-5")

# Q14: QND Heisenberg time tau = 2**L / (J*L)
L = 17
J = 1
tau_H = 2**L / (J * L)
print_claim("Q14", tau_H, "7.71e3")

# Q15: Thermal activation bounds for d=3,5,10
bounds = []
for d in [3,5,10]:
    bounds.append(math.exp(-2**d))
expected_bounds = "3.3546e-4, 1.2664e-14, 1e-444.7"
print_claim("Q15", bounds[0], "3.3546e-4")
print_claim("Q15", bounds[1], "1.2664e-14")
print_claim("Q15", bounds[2], "1e-444.7")
