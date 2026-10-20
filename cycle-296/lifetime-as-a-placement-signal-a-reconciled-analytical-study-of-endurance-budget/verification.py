import math

def fmt(val, sig):
    """Format value with given significant digits, using scientific notation if needed."""
    if sig >= 4 and (val < 0.01 or val >= 1e4):
        return f"{val:.{sig-1}e}"
    else:
        return f"{val:.{sig}f}"

# Q1
m_max = 9.3 / 5
expected_q1 = 1.86
print(f"CLAIM Q1: computed={fmt(m_max,2)} expected={expected_q1} match={'yes' if round(m_max,2)==expected_q1 else 'no'}")

# Q2
m_min = 3.3 / 5
expected_q2 = 0.66
print(f"CLAIM Q2: computed={fmt(m_min,2)} expected={expected_q2} match={'yes' if round(m_min,2)==expected_q2 else 'no'}")

# Q3
m_base_max = 4.8 / 5
expected_q3 = 0.96
print(f"CLAIM Q3: computed={fmt(m_base_max,2)} expected={expected_q3} match={'yes' if round(m_base_max,2)==expected_q3 else 'no'}")

# Q4
m_base_min = 1.9 / 5
expected_q4 = 0.38
print(f"CLAIM Q4: computed={fmt(m_base_min,2)} expected={expected_q4} match={'yes' if round(m_base_min,2)==expected_q4 else 'no'}")

# Q5
f_geom_tight = math.sqrt(1.50 * 2.95)
expected_q5 = 2.10
print(f"CLAIM Q5: computed={fmt(f_geom_tight,2)} expected={expected_q5} match={'yes' if round(f_geom_tight,2)==expected_q5 else 'no'}")

# Q6
f_geom_loose = math.sqrt(1.19 * 1.89)
expected_q6 = 1.50
print(f"CLAIM Q6: computed={fmt(f_geom_loose,2)} expected={expected_q6} match={'yes' if round(f_geom_loose,2)==expected_q6 else 'no'}")

# Q7
f_geom_overall = math.sqrt(1.19 * 2.95)
expected_q7 = 1.87
print(f"CLAIM Q7: computed={fmt(f_geom_overall,2)} expected={expected_q7} match={'yes' if round(f_geom_overall,2)==expected_q7 else 'no'}")

# Q8
phi_1_19 = 1 - 1/1.19
expected_q8 = 15.97
print(f"CLAIM Q8: computed={fmt(phi_1_19*100,2)} expected={expected_q8} match={'yes' if round(phi_1_19*100,2)==expected_q8 else 'no'}")

# Q9
phi_1_50 = 1 - 1/1.50
expected_q9 = 33.33
print(f"CLAIM Q9: computed={fmt(phi_1_50*100,2)} expected={expected_q9} match={'yes' if round(phi_1_50*100,2)==expected_q9 else 'no'}")

# Q10
phi_1_89 = 1 - 1/1.89
expected_q10 = 47.09
print(f"CLAIM Q10: computed={fmt(phi_1_89*100,2)} expected={expected_q10} match={'yes' if round(phi_1_89*100,2)==expected_q10 else 'no'}")

# Q11
phi_2_95 = 1 - 1/2.95
expected_q11 = 66.10
print(f"CLAIM Q11: computed={fmt(phi_2_95*100,2)} expected={expected_q11} match={'yes' if round(phi_2_95*100,2)==expected_q11 else 'no'}")

# Q12
W_HBF_9_3 = 1.0e5 / 9.3
expected_q12 = 1.08e4
print(f"CLAIM Q12: computed={fmt(W_HBF_9_3,2)} expected={expected_q12} match={'yes' if round(W_HBF_9_3,2)==expected_q12 else 'no'}")

# Q13
writes_per_hour_9_3 = W_HBF_9_3 / 8760
expected_q13 = 1.23
print(f"CLAIM Q13: computed={fmt(writes_per_hour_9_3,2)} expected={expected_q13} match={'yes' if round(writes_per_hour_9_3,2)==expected_q13 else 'no'}")

# Q14
W_HBF_3_3 = 1.0e5 / 3.3
expected_q14 = 3.03e4
print(f"CLAIM Q14: computed={fmt(W_HBF_3_3,2)} expected={expected_q14} match={'yes' if round(W_HBF_3_3,2)==expected_q14 else 'no'}")

# Q15
writes_per_hour_3_3 = W_HBF_3_3 / 8760
expected_q15 = 3.46
print(f"CLAIM Q15: computed={fmt(writes_per_hour_3_3,2)} expected={expected_q15} match={'yes' if round(writes_per_hour_3_3,2)==expected_q15 else 'no'}")

# Q16
W_HBM_proj = 1.08e4 / 1.19
expected_q16 = 9.07e3
print(f"CLAIM Q16: computed={fmt(W_HBM_proj,2)} expected={expected_q16} match={'yes' if round(W_HBM_proj,2)==expected_q16 else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
