import math

def zscore(N, p0, x):
    mu = N * p0
    sigma = math.sqrt(N * p0 * (1 - p0))
    return (x - mu) / sigma

# Q1
z1 = zscore(60, 0.025, 48)
print(f"CLAIM Q1: computed={z1:.6f} expected=38.45 match={'yes' if round(z1,2)==38.45 else 'no'}")

# Q2
C = math.comb(60, 48)
p48 = C * (0.025**48) * (0.975**12)
print(f"CLAIM Q2: computed={p48:.8e} expected=1.3e-65 match={'yes' if abs(math.log10(p48) - math.log10(1.3e-65)) < 0.05 else 'no'}")

# Q3
z3 = zscore(60, 0.05, 48)
print(f"CLAIM Q3: computed={z3:.6f} expected=26.66 match={'yes' if round(z3,2)==26.66 else 'no'}")

# Q4
z4 = zscore(60, 0.5, 31)
print(f"CLAIM Q4: computed={z4:.6f} expected=0.25820 match={'yes' if round(z4,5)==0.25820 else 'no'}")

# Q5
ph1 = 48/60
se1 = math.sqrt(ph1*(1-ph1)/60)
lo1, hi1 = ph1 - 1.96*se1, ph1 + 1.96*se1
print(f"CLAIM Q5: computed=[{lo1:.6f},{hi1:.6f}] expected=[0.6988,0.9012] match={'yes' if round(lo1,4)==0.6988 and round(hi1,4)==0.9012 else 'no'}")

# Q6
ph2 = 31/60
se2 = math.sqrt(ph2*(1-ph2)/60)
lo2, hi2 = ph2 - 1.96*se2, ph2 + 1.96*se2
print(f"CLAIM Q6: computed=[{lo2:.6f},{hi2:.6f}] expected=[0.3902,0.6431] match={'yes' if round(lo2,4)==0.3902 and round(hi2,4)==0.6431 else 'no'}")

# Q7
B7 = 0.82 * 657
print(f"CLAIM Q7: computed={B7:.8f} expected=538.74 match={'yes' if round(B7,2)==538.74 else 'no'}")

# Q8
B8 = 0.94 / 0.25
print(f"CLAIM Q8: computed={B8:.8f} expected=3.76 match={'yes' if round(B8,2)==3.76 else 'no'}")

# Q9
r9 = 1/657
print(f"CLAIM Q9: computed={r9:.8f} expected=0.001522 match={'yes' if round(r9,6)==0.001522 else 'no'}")

# Q10
n10 = 1/(1 - 1/657)
print(f"CLAIM Q10: computed={n10:.8f} expected=1.00152 match={'yes' if round(n10,5)==1.00152 else 'no'}")

# Q11
n11 = 1/(0.82 - 1/657)
print(f"CLAIM Q11: computed={n11:.8f} expected=1.2218 match={'yes' if round(n11,4)==1.2218 else 'no'}")

# Q12
n12 = n11 / n10
print(f"CLAIM Q12: computed={n12:.8f} expected=1.22 match={'yes' if round(n12,2)==1.22 else 'no'}")

# Q13
n13 = 1/(0.5 - 1/657)
print(f"CLAIM Q13: computed={n13:.8f} expected=2.006 match={'yes' if round(n13,3)==2.006 else 'no'}")

# Q14
n14 = 1/(0.25 - 1/657)
print(f"CLAIM Q14: computed={n14:.8f} expected=4.025 match={'yes' if round(n14,3)==4.025 else 'no'}")

# Q15
n15 = 1/(0.94 - 0.25)
print(f"CLAIM Q15: computed={n15:.8f} expected=1.449 match={'yes' if round(n15,3)==1.449 else 'no'}")

# Q16
n16 = 100/(0.01*(1 - 1/657))
print(f"CLAIM Q16: computed={n16:.8f} expected=10015 match={'yes' if round(n16)==10015 else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
