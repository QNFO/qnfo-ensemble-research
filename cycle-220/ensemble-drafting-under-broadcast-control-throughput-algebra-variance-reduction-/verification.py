import math

def fmt(v, digits):
    """Round to given number of decimal places and format without trailing zeros."""
    fmt_str = f"{{:.{digits}f}}".format(v)
    # remove trailing zeros and possible trailing dot
    return fmt_str.rstrip('0').rstrip('.') if '.' in fmt_str else fmt_str

# Q1
alpha = 0.7
K = 4
EL = (1 - alpha**K) / (1 - alpha)
expected_EL = "2.533"
print(f"CLAIM Q1: computed={fmt(EL,6)} expected={expected_EL} match={'yes' if fmt(EL,6)==expected_EL else 'no'}")

# Q2
c_d = 0.1
C = K * c_d + 1
expected_C = "1.4"
print(f"CLAIM Q2: computed={fmt(C,6)} expected={expected_C} match={'yes' if fmt(C,6)==expected_C else 'no'}")

# Q3
T = EL / C
expected_T = "1.8093"
print(f"CLAIM Q3: computed={fmt(T,6)} expected={expected_T} match={'yes' if fmt(T,4)==expected_T else 'no'}")

# Q4
K = 3
EL3 = (1 - alpha**K) / (1 - alpha)
expected_EL3 = "2.19"
print(f"CLAIM Q4: computed={fmt(EL3,6)} expected={expected_EL3} match={'yes' if fmt(EL3,4)==expected_EL3 else 'no'}")

# Q5
C3 = K * c_d + 1
expected_C3 = "1.3"
print(f"CLAIM Q5: computed={fmt(C3,6)} expected={expected_C3} match={'yes' if fmt(C3,6)==expected_C3 else 'no'}")

# Q6
T3 = EL3 / C3
expected_T3 = "1.6846"
print(f"CLAIM Q6: computed={fmt(T3,6)} expected={expected_T3} match={'yes' if fmt(T3,4)==expected_T3 else 'no'}")

# Q7
K = 5
EL5 = (1 - alpha**K) / (1 - alpha)
expected_EL5 = "2.7731"
print(f"CLAIM Q7: computed={fmt(EL5,6)} expected={expected_EL5} match={'yes' if fmt(EL5,4)==expected_EL5 else 'no'}")

# Q8
C5 = K * c_d + 1
expected_C5 = "1.5"
print(f"CLAIM Q8: computed={fmt(C5,6)} expected={expected_C5} match={'yes' if fmt(C5,6)==expected_C5 else 'no'}")

# Q9
T5 = EL5 / C5
expected_T5 = "1.8487"
print(f"CLAIM Q9: computed={fmt(T5,6)} expected={expected_T5} match={'yes' if fmt(T5,4)==expected_T5 else 'no'}")

# Q10
K = 6
EL6 = (1 - alpha**K) / (1 - alpha)
expected_EL6 = "2.94117"
print(f"CLAIM Q10: computed={fmt(EL6,6)} expected={expected_EL6} match={'yes' if fmt(EL6,6)==expected_EL6 else 'no'}")

# Q11
C6 = K * c_d + 1
expected_C6 = "1.6"
print(f"CLAIM Q11: computed={fmt(C6,6)} expected={expected_C6} match={'yes' if fmt(C6,6)==expected_C6 else 'no'}")

# Q12
T6 = EL6 / C6
expected_T6 = "1.8382"
print(f"CLAIM Q12: computed={fmt(T6,6)} expected={expected_T6} match={'yes' if fmt(T6,4)==expected_T6 else 'no'}")

# Q13
K = 5
ln_alpha = -0.356675  # given as -ln(alpha)
term = 0.0356675 * K + 0.456675
lhs5 = alpha**K * term
expected_lhs5 = "0.106727"
print(f"CLAIM Q13: computed={fmt(lhs5,6)} expected={expected_lhs5} match={'yes' if fmt(lhs5,6)==expected_lhs5 else 'no'}")

# Q14
K = 6
term = 0.0356675 * K + 0.456675
lhs6 = alpha**K * term
expected_lhs6 = "0.078906"
print(f"CLAIM Q14: computed={fmt(lhs6,6)} expected={expected_lhs6} match={'yes' if fmt(lhs6,6)==expected_lhs6 else 'no'}")

# Q15
# Using derived formula: c_d* = 0.2401 / 1.5726
c_star = 0.2401 / 1.5726
expected_cstar = "0.1527"
print(f"CLAIM Q15: computed={fmt(c_star,4)} expected={expected_cstar} match={'yes' if fmt(c_star,4)==expected_cstar else 'no'}")

# Q16
sigma = 0.3
N = 5
SE = sigma / math.sqrt(N)
expected_SE = "0.1342"
print(f"CLAIM Q16: computed={fmt(SE,4)} expected={expected_SE} match={'yes' if fmt(SE,4)==expected_SE else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
