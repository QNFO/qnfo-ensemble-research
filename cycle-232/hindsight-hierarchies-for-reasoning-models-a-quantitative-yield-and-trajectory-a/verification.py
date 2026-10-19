import math

# Inputs
P = 10000
N0 = 1000
sigma = 0.1
m = 5
r = 0.6
p = 0.8
mrp = m * r * p  # 2.4
phi90 = 0.9
phi50 = 0.5

def round_to_expected(val, expected_str):
    if '.' in expected_str:
        ndigits = len(expected_str.split('.')[1])
    else:
        ndigits = 0
    return round(val, ndigits)

def check(val, expected_str):
    rounded = round_to_expected(val, expected_str)
    match = (str(rounded) == expected_str)
    return rounded, match

# C1
C1_val = mrp
C1_exp = "2.4"
C1_cmp, C1_match = check(C1_val, C1_exp)

# C2
t = 5
N5 = P - (P - N0) * (1 - sigma) ** t
C2_exp = "4685.59"
C2_cmp, C2_match = check(N5, C2_exp)

# C3a
U0 = P - N0
add1 = sigma * U0
C3a_exp = "900"
C3a_cmp, C3a_match = check(add1, C3a_exp)

# C3b
N1 = P - (P - N0) * (1 - sigma) ** 1
U1 = P - N1
add2 = sigma * U1
C3b_exp = "810"
C3b_cmp, C3b_match = check(add2, C3b_exp)

# C3c
N2 = P - (P - N0) * (1 - sigma) ** 2
U2 = P - N2
add3 = sigma * U2
C3c_exp = "729"
C3c_cmp, C3c_match = check(add3, C3c_exp)

# C3d
N3 = P - (P - N0) * (1 - sigma) ** 3
U3 = P - N3
add4 = sigma * U3
C3d_exp = "656.1"
C3d_cmp, C3d_match = check(add4, C3d_exp)

# C3e
N4 = P - (P - N0) * (1 - sigma) ** 4
U4 = P - N4
add5 = sigma * U4
C3e_exp = "590.49"
C3e_cmp, C3e_match = check(add5, C3e_exp)

# C4
ratio = N5 / N0
C4_exp = "4.68559"
C4_cmp, C4_match = check(ratio, C4_exp)

# C5
t90 = math.log((P - phi90 * P) / (P - N0)) / math.log(1 - sigma)
C5_exp = "20.85"
C5_cmp, C5_match = check(t90, C5_exp)

# C6
t50 = math.log((P - phi50 * P) / (P - N0)) / math.log(1 - sigma)
C6_exp = "5.58"
C6_cmp, C6_match = check(t50, C6_exp)

# C7
T = 5
sum_N = (T + 1) * P - (P - N0) * (1 - (1 - sigma) ** (T + 1)) / sigma
C7_exp = "17829.69"
C7_cmp, C7_match = check(sum_N, C7_exp)

# C8
C5_val = mrp * sum_N
C8_exp = "42791.26"
C8_cmp, C8_match = check(C5_val, C8_exp)

# C9
A5 = C5_val / N0
C9_exp = "42.791256"
C9_cmp, C9_match = check(A5, C9_exp)

# C10
threshold = 1 / (m * r)
C10_exp = "0.3333"
C10_cmp, C10_match = check(threshold, C10_exp)

# C11
f5 = 1 - N0 / N5
C11_exp = "0.786582"
C11_cmp, C11_match = check(f5, C11_exp)

# C13
spurious = (1 - p) * m * r * sum_N
C13_exp = "10697.81"
C13_cmp, C13_match = check(spurious, C13_exp)

# Print results
claims = [
    ("C1", C1_cmp, C1_exp, C1_match),
    ("C2", C2_cmp, C2_exp, C2_match),
    ("C3a", C3a_cmp, C3a_exp, C3a_match),
    ("C3b", C3b_cmp, C3b_exp, C3b_match),
    ("C3c", C3c_cmp, C3c_exp, C3c_match),
    ("C3d", C3d_cmp, C3d_exp, C3d_match),
    ("C3e", C3e_cmp, C3e_exp, C3e_match),
    ("C4", C4_cmp, C4_exp, C4_match),
    ("C5", C5_cmp, C5_exp, C5_match),
    ("C6", C6_cmp, C6_exp, C6_match),
    ("C7", C7_cmp, C7_exp, C7_match),
    ("C8", C8_cmp, C8_exp, C8_match),
    ("C9", C9_cmp, C9_exp, C9_match),
    ("C10", C10_cmp, C10_exp, C10_match),
    ("C11", C11_cmp, C11_exp, C11_match),
    ("C13", C13_cmp, C13_exp, C13_match),
]

for cid, comp, exp, ok in claims:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,_,_,ok in claims if ok)} match, {sum(1 for _,_,_,ok in claims if not ok)} mismatch")
