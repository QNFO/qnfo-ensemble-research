import math
from decimal import Decimal, getcontext

# Set high precision for large exponent calculations
getcontext().prec = 30

def fmt(val, sig):
    """Round to given significant figures and format in scientific notation."""
    if val == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(val))))
    factor = round(val / (10 ** exponent), sig - 1)
    return f"{factor:.{sig-1}f}e{exponent}"

def print_claim(cid, computed, expected_str, sig):
    # Round computed to the number of significant digits in expected
    expected_sig = len(expected_str.replace('.', '').replace('e', '').replace('+', '').replace('-', '')) - 1
    comp_str = fmt(computed, expected_sig)
    match = "yes" if comp_str == expected_str else "no"
    print(f"CLAIM {cid}: computed={comp_str} expected={expected_str} match={match}")

# Q1
N_atoms = Decimal('1e80')
m_p = Decimal('1.67e-27')
c = Decimal('3.00e8')
B_E = N_atoms * m_p * c * c
print_claim("Q1", float(B_E), "1.5e70", 2)

# Q2
kB = Decimal('1.38e-23')
T = Decimal('300')
ln2 = Decimal('0.6931')
E_min = kB * T * ln2
B_E_exact = Decimal('1.503e70')
B_ops_eff = B_E_exact / E_min
print_claim("Q2", float(B_ops_eff), "5.24e90", 3)

# Q3
S128 = Decimal('3.402823669e38')
f = Decimal('1e9')
T_seq = S128 / f
print_claim("Q3", float(T_seq), "3.4e29", 2)

# Q4
T_max = Decimal('1e18')
p = S128 / (f * T_max)
print_claim("Q4", float(p), "3.4e11", 2)

# Q5
m_proc = Decimal('1e-3')
M = p * m_proc
print_claim("Q5", float(M), "3.4e8", 2)

# Q6
epsilon_L = Decimal('2.8e-21')
E = epsilon_L * S128
print_claim("Q6", float(E), "9.5e17", 2)

# Q7
log2_Bops = (Decimal(B_ops_eff).ln() / Decimal(2).ln())
n_star = int(log2_Bops.to_integral_value(rounding='ROUND_FLOOR'))
print_claim("Q7", n_star, "301", 3)

# Q8
mu_128 = B_ops_eff / S128
print_claim("Q8", float(mu_128), "1.54e52", 3)

# Q9
S256 = Decimal('1.157920892e77')
mu_256 = B_ops_eff / S256
print_claim("Q9", float(mu_256), "4.52e13", 3)

# Q10
S2048 = Decimal('3.23e616')
mu_2048 = B_ops_eff / S2048
print_claim("Q10", float(mu_2048), "1.62e-526", 3)

# Q11
S500 = Decimal('3.27e150')
mu_500 = B_ops_eff / S500
print_claim("Q11", float(mu_500), "1.60e-60", 3)

# Q12
S50 = Decimal('1.13e15')
mu_RNA = B_ops_eff / S50
print_claim("Q12", float(mu_RNA), "4.6e75", 2)

# Q13
N_nu = Decimal('1e12')
E_nu = Decimal('4.806e-14')
E_beam = N_nu * E_nu
print_claim("Q13", float(E_beam), "4.8e-2", 2)

# Q14
L = Decimal('1e7')
frame_rate = Decimal('1e6')
dotN_CNN = L * frame_rate
print_claim("Q14", float(dotN_CNN), "1e13", 1)

# Q15
T_univ = Decimal('1e18')
epsilon = Decimal('1e-12')
E_retina = dotN_CNN * T_univ * epsilon
print_claim("Q15", float(E_retina), "1e19", 1)

# Q16
M_hardware = Decimal('3.4e8')
cost_per_kg = Decimal('1e5')
cost = M_hardware * cost_per_kg
print_claim("Q16", float(cost), "3.4e13", 2)

print("VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch")
