import math

def fmt(x):
    # format with at least 8 significant digits, removing trailing zeros
    s = f"{x:.10g}"
    return s

# Q1
p_th = (1e-3 / (2**3))**(1/(3+1))
expected_q1 = "0.105"
match_q1 = "yes" if round(p_th, 3) == float(expected_q1) else "no"
print(f"CLAIM Q1: computed={fmt(p_th)} expected={expected_q1} match={match_q1}")

# Q2
gap = 4.0 / 0.0434  # temperatures in K (4 K / 43.4 mK = 4 / 0.0434)
expected_q2 = "92.2"
match_q2 = "yes" if round(gap, 1) == float(expected_q2) else "no"
print(f"CLAIM Q2: computed={fmt(gap)} expected={expected_q2} match={match_q2}")

# Q3a
P_q3a = (2**1) * (0.10**(1+1))
expected_q3a = "0.020"
match_q3a = "yes" if abs(P_q3a - 0.020) < 1e-12 else "no"
print(f"CLAIM Q3a: computed={fmt(P_q3a)} expected={expected_q3a} match={match_q3a}")

# Q3b
P_q3b = (2**2) * (0.10**(2+1))
expected_q3b = "0.004"
match_q3b = "yes" if abs(P_q3b - 0.004) < 1e-12 else "no"
print(f"CLAIM Q3b: computed={fmt(P_q3b)} expected={expected_q3b} match={match_q3b}")

# Q3c
P_q3c = (2**3) * (0.10**(3+1))
expected_q3c = "0.0008"
match_q3c = "yes" if abs(P_q3c - 0.0008) < 1e-12 else "no"
print(f"CLAIM Q3c: computed={fmt(P_q3c)} expected={expected_q3c} match={match_q3c}")

# Q4a
P_q4a = (2**1) * (0.30**(1+1))
expected_q4a = "0.180"
match_q4a = "yes" if abs(P_q4a - 0.180) < 1e-12 else "no"
print(f"CLAIM Q4a: computed={fmt(P_q4a)} expected={expected_q4a} match={match_q4a}")

# Q4b
P_q4b = (2**2) * (0.30**(2+1))
expected_q4b = "0.108"
match_q4b = "yes" if abs(P_q4b - 0.108) < 1e-12 else "no"
print(f"CLAIM Q4b: computed={fmt(P_q4b)} expected={expected_q4b} match={match_q4b}")

# Q4c
P_q4c = (2**3) * (0.30**(3+1))
expected_q4c = "0.0648"
match_q4c = "yes" if abs(P_q4c - 0.0648) < 1e-12 else "no"
print(f"CLAIM Q4c: computed={fmt(P_q4c)} expected={expected_q4c} match={match_q4c}")

# Q5a
P_q5a = (2**1) * (0.50**(1+1))
expected_q5a = "0.500"
match_q5a = "yes" if abs(P_q5a - 0.500) < 1e-12 else "no"
print(f"CLAIM Q5a: computed={fmt(P_q5a)} expected={expected_q5a} match={match_q5a}")

# Q5b
P_q5b = (2**2) * (0.50**(2+1))
expected_q5b = "0.500"
match_q5b = "yes" if abs(P_q5b - 0.500) < 1e-12 else "no"
print(f"CLAIM Q5b: computed={fmt(P_q5b)} expected={expected_q5b} match={match_q5b}")

# Q5c
P_q5c = (2**3) * (0.50**(3+1))
expected_q5c = "0.500"
match_q5c = "yes" if abs(P_q5c - 0.500) < 1e-12 else "no"
print(f"CLAIM Q5c: computed={fmt(P_q5c)} expected={expected_q5c} match={match_q5c}")

# Q6
N6 = 2**(4+1) - 1  # depth 4
p6 = 0.05
P_q6 = 1 - (1 - p6)**N6
expected_q6 = "0.797"
match_q6 = "yes" if round(P_q6, 3) == float(expected_q6) else "no"
print(f"CLAIM Q6: computed={fmt(P_q6)} expected={expected_q6} match={match_q6}")

# Q7
N7 = 2**(5+1) - 1  # depth 5
p7 = 0.01
P_q7 = 1 - (1 - p7)**N7
expected_q7 = "0.46909446"
match_q7 = "yes" if abs(P_q7 - 0.46909446) < 1e-9 else "no"
print(f"CLAIM Q7: computed={fmt(P_q7)} expected={expected_q7} match={match_q7}")

# Q8
d8 = 2
N8 = 2**(d8+1) - 1
expected_q8 = "7"
match_q8 = "yes" if N8 == int(expected_q8) else "no"
print(f"CLAIM Q8: computed={fmt(N8)} expected={expected_q8} match={match_q8}")

# Q9
cost_per_qubit = 1000
num_qubits = 15
total_cost = cost_per_qubit * num_qubits
expected_q9 = "15000"
match_q9 = "yes" if total_cost == int(expected_q9) else "no"
print(f"CLAIM Q9: computed={fmt(total_cost)} expected={expected_q9} match={match_q9}")

# Q10
gap_q10 = 4.0 / 0.0002  # 4 W / 0.2 mW
expected_q10 = "20000"
match_q10 = "yes" if int(gap_q10) == int(expected_q10) else "no"
print(f"CLAIM Q10: computed={fmt(gap_q10)} expected={expected_q10} match={match_q10}")

print(f"VERIFICATION SUMMARY: 10 claims, {sum([match_q1,match_q2,match_q3a,match_q3b,match_q3c,match_q4a,match_q4b,match_q4c,match_q5a,match_q5b,match_q5c,match_q6,match_q7,match_q8,match_q9,match_q10].count('yes'))} match, {sum([match_q1,match_q2,match_q3a,match_q3b,match_q3c,match_q4a,match_q4b,match_q4c,match_q5a,match_q5b,match_q5c,match_q6,match_q7,match_q8,match_q9,match_q10].count('no'))} mismatch")
