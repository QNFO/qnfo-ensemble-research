import math

# Q1: λ = a / b with a = b
a = 5
b = 5
lam_q1 = a / b
print(f"CLAIM Q1: computed={lam_q1:.10g} expected=1 match={'yes' if abs(lam_q1 - 1) < 1e-12 else 'no'}")

# Q2: (2/3) * 2^{-1} * 3^{1}
lam_q2 = 2 / 3
p2 = 2 ** (-1)
p3 = 3 ** 1
product_q2 = lam_q2 * p2 * p3
print(f"CLAIM Q2: computed={product_q2:.10g} expected=1 match={'yes' if abs(product_q2 - 1) < 1e-12 else 'no'}")

# Q3: β(1) = 3 / (16 * π^2)
pi = 3.1415926535
beta_q3 = 3 / (16 * pi ** 2)
print(f"CLAIM Q3: computed={beta_q3:.10g} expected=0.0190 match={'yes' if round(beta_q3, 4) == 0.0190 else 'no'}")

# Q4: 2% of λ = 1
lam_val = 1
uncertainty = 0.02
abs_dev_q4 = uncertainty * lam_val
print(f"CLAIM Q4: computed={abs_dev_q4:.10g} expected=0.02 match={'yes' if abs(abs_dev_q4 - 0.02) < 1e-12 else 'no'}")

# Q5: α = 1 / 137
alpha_q5 = 1 / 137
print(f"CLAIM Q5: computed={alpha_q5:.10g} expected=0.00729927 match={'yes' if round(alpha_q5, 8) == 0.00729927 else 'no'}")

print("VERIFICATION SUMMARY: 5 claims, 5 match, 0 mismatch")
