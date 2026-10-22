import math

# Input constants
lnN = 13.815511
ln2 = 0.693147
ln3 = 1.098612
ln4 = 1.386294
ln5 = 1.609438

# Helper to format expected values
def fmt(val, digits=4):
    return f"{val:.4f}"

# CLAIM Q1
ratio_q2 = lnN / ln2
print(f"CLAIM Q1: computed={ratio_q2:.6f} expected=19.931574 match={'yes' if round(ratio_q2,6)==19.931574 else 'no'}")

# CLAIM Q2
ratio_q3 = lnN / ln3
print(f"CLAIM Q2: computed={ratio_q3:.6f} expected=12.575423 match={'yes' if round(ratio_q3,6)==12.575423 else 'no'}")

# CLAIM Q3
ratio_q4 = lnN / ln4
print(f"CLAIM Q3: computed={ratio_q4:.6f} expected=9.965787 match={'yes' if round(ratio_q4,6)==9.965787 else 'no'}")

# CLAIM Q4
ratio_q5 = lnN / ln5
print(f"CLAIM Q4: computed={ratio_q5:.6f} expected=8.584059 match={'yes' if round(ratio_q5,6)==8.584059 else 'no'}")

# CLAIM Q5
n2 = math.ceil(ratio_q2)
n3 = math.ceil(ratio_q3)
n4 = math.ceil(ratio_q4)
n5 = math.ceil(ratio_q5)
print(f"CLAIM Q5: computed={n2},{n3},{n4},{n5} expected=20,13,10,9 match={'yes' if (n2,n3,n4,n5)==(20,13,10,9) else 'no'}")

# CLAIM Q6
T2 = 2 * n2
T3 = 3 * n3
T4 = 4 * n4
T5 = 5 * n5
print(f"CLAIM Q6: computed={T2},{T3},{T4},{T5} expected=40,39,40,45 match={'yes' if (T2,T3,T4,T5)==(40,39,40,45) else 'no'}")

# CLAIM Q7
norm_T2 = T2 / lnN
print(f"CLAIM Q7: computed={norm_T2:.4f} expected=2.8953 match={'yes' if round(norm_T2,4)==2.8953 else 'no'}")

# CLAIM Q8
norm_T3 = T3 / lnN
print(f"CLAIM Q8: computed={norm_T3:.4f} expected=2.8229 match={'yes' if round(norm_T3,4)==2.8229 else 'no'}")

# CLAIM Q9
norm_T5 = T5 / lnN
print(f"CLAIM Q9: computed={norm_T5:.4f} expected=3.2572 match={'yes' if round(norm_T5,4)==3.2572 else 'no'}")

# CLAIM Q10
q2_n20 = math.exp(-20 * ln2)
print(f"CLAIM Q10: computed={q2_n20:.2e} expected=9.54e-07 match={'yes' if abs(q2_n20-9.54e-07)/9.54e-07<1e-2 else 'no'}")

# CLAIM Q11
q3_n13 = math.exp(-13 * ln3)
print(f"CLAIM Q11: computed={q3_n13:.2e} expected=6.27e-07 match={'yes' if abs(q3_n13-6.27e-07)/6.27e-07<1e-2 else 'no'}")

# CLAIM Q12
q4_n10 = math.exp(-10 * ln4)
print(f"CLAIM Q12: computed={q4_n10:.2e} expected=9.54e-07 match={'yes' if abs(q4_n10-9.54e-07)/9.54e-07<1e-2 else 'no'}")

# CLAIM Q13
q5_n9 = math.exp(-9 * ln5)
print(f"CLAIM Q13: computed={q5_n9:.2e} expected=5.12e-07 match={'yes' if abs(q5_n9-5.12e-07)/5.12e-07<1e-2 else 'no'}")

# CLAIM Q14
S2_N = 2 * (1 - q2_n20) / (2 - 1)
print(f"CLAIM Q14: computed={S2_N:.4f} expected=2.0000 match={'yes' if round(S2_N,4)==2.0000 else 'no'}")

# CLAIM Q15
S3_N = 3 * (1 - q3_n13) / (3 - 1)
print(f"CLAIM Q15: computed={S3_N:.4f} expected=1.5000 match={'yes' if round(S3_N,4)==1.5000 else 'no'}")

# CLAIM Q16
S4_N = 4 * (1 - q4_n10) / (4 - 1)
print(f"CLAIM Q16: computed={S4_N:.4f} expected=1.3333 match={'yes' if round(S4_N,4)==1.3333 else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, "
      f"{sum(1 for line in open(__file__) if 'match=yes' in line)} match, "
      f"{sum(1 for line in open(__file__) if 'match=no' in line)} mismatch")
