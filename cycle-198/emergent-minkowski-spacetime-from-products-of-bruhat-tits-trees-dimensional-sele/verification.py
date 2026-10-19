import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    else:
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1 and Q2 inputs
M = 4
l = 2
J = 1

inner_sqrt = math.sqrt(M**2 * l**2 - J**2)          # sqrt(M^2 l^2 - J^2)
term = (M * l**2) / 2
outer_plus = term + (l/2) * inner_sqrt
outer_minus = term - (l/2) * inner_sqrt
r_plus = math.sqrt(outer_plus)
r_minus = math.sqrt(outer_minus)

# Q3 inputs
p = 2
n = 10
V_n = 1 + (p + 1) * (p**n - 1) // (p - 1)  # integer division yields exact integer

# Q4 inputs
k = 10
cone_size = p**k

# Q5 inputs
n1 = 1
mu_n = 1/(p+1) * (1/p)**(n1-1)
total_mu = (p+1) * mu_n

# Q6 central charge condition
D_from_cc = 15 * 2 / 3

# Q7 projected vertex count
N = 10**3
D4 = 4
total_vertices_D4 = N**D4

# Q8 projected vertex count for D=10
D10 = 10
total_vertices_D10 = N**D10

# Prepare results
claims = [
    ("Q1", round_sig(r_plus, 4), "3.992"),
    ("Q2", round_sig(r_minus, 4), "0.2505"),
    ("Q3", V_n, "3070"),
    ("Q4", cone_size, "1024"),
    ("Q5", total_mu, "1"),
    ("Q6", D_from_cc, "10"),
    ("Q7", total_vertices_D4, "1e12"),
    ("Q8", total_vertices_D10, "1e30")
]

for cid, comp, exp_str in claims:
    # Determine match
    if cid == "Q8":
        # Claim expects the value to exceed 1e30, so equality is a mismatch
        match = "no"
    else:
        # Compare numeric values after converting expected string to float
        exp_val = float(exp_str)
        match = "yes" if abs(comp - exp_val) < 1e-12 else "no"
    # Format computed value with sufficient precision
    if isinstance(comp, float):
        comp_str = f"{comp:.10g}"
    else:
        comp_str = str(comp)
    print(f"CLAIM {cid}: computed={comp_str} expected={exp_str} match={match}")
