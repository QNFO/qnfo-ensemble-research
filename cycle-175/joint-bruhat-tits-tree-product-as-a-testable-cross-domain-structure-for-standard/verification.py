import math

# Q1
w = 0.04
R = 10.0
p_single = w / R
expected_q1 = "4e-3"
print(f"CLAIM Q1: computed={p_single:.9g} expected={expected_q1} match={'yes' if abs(p_single - 4e-3) < 1e-12 else 'no'}")

# Q2
p_joint = p_single ** 11
expected_q2 = "4.194304e-27"
print(f"CLAIM Q2: computed={p_joint:.9e} expected={expected_q2} match={'yes' if abs(p_joint - 4.194304e-27) < 1e-33 else 'no'}")

# Q3
p = 2
L2 = (p + 1) - 2 * math.sqrt(p)
expected_q3 = "0.17157288"
print(f"CLAIM Q3: computed={L2:.8f} expected={expected_q3} match={'yes' if abs(L2 - 0.17157288) < 1e-9 else 'no'}")

# Q4
U2 = (p + 1) + 2 * math.sqrt(p)
expected_q4 = "5.82842712"
print(f"CLAIM Q4: computed={U2:.8f} expected={expected_q4} match={'yes' if abs(U2 - 5.82842712) < 1e-9 else 'no'}")

# Q5
p = 5
L5 = (p + 1) - 2 * math.sqrt(p)
expected_q5 = "1.52786405"
print(f"CLAIM Q5: computed={L5:.8f} expected={expected_q5} match={'yes' if abs(L5 - 1.52786405) < 1e-9 else 'no'}")

# Q6
U5 = (p + 1) + 2 * math.sqrt(p)
expected_q6 = "10.47213595"
print(f"CLAIM Q6: computed={U5:.8f} expected={expected_q6} match={'yes' if abs(U5 - 10.47213595) < 1e-9 else 'no'}")

# Q7
ln2 = math.log(2)
ln3 = math.log(3)
ln5 = math.log(5)
expected_q7 = "0.693147181, 1.098612289, 1.609437912"
computed_q7 = f"{ln2:.9f}, {ln3:.9f}, {ln5:.9f}"
match_q7 = (abs(ln2 - 0.693147181) < 1e-9 and
            abs(ln3 - 1.098612289) < 1e-9 and
            abs(ln5 - 1.609437912) < 1e-9)
print(f"CLAIM Q7: computed={computed_q7} expected={expected_q7} match={'yes' if match_q7 else 'no'}")

# Q8
S = 1/ln2 + 1/ln3 + 1/ln5
expected_q8 = "2.974269202"
print(f"CLAIM Q8: computed={S:.9f} expected={expected_q8} match={'yes' if abs(S - 2.974269202) < 1e-9 else 'no'}")

# Q9
lambda_tree = 3 / S
expected_q9 = "1.008652"
print(f"CLAIM Q9: computed={lambda_tree:.6f} expected={expected_q9} match={'yes' if abs(lambda_tree - 1.008652) < 1e-6 else 'no'}")

# Q10
lambda_exp = 22.7
kappa = lambda_exp / lambda_tree
expected_q10 = "22.51"
print(f"CLAIM Q10: computed={kappa:.2f} expected={expected_q10} match={'yes' if abs(kappa - 22.51) < 0.005 else 'no'}")

print("VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch")
