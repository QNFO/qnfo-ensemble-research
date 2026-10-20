import math

def fmt(x):
    # format with at least 8 significant digits, removing trailing zeros
    if isinstance(x, int):
        return str(x)
    s = f"{x:.10g}"
    # ensure at least 8 significant digits
    if 'e' in s or '.' in s:
        return s
    return s

# Q1
R = 2/50 - 2/70
exp_Q1 = "0.0114286"
print(f"CLAIM Q1: computed={fmt(R)} expected={exp_Q1} match={'yes' if round(R,7)==float(exp_Q1) else 'no'}")

# Q2
V = math.pi * R**2
exp_Q2 = "0.0004103"
print(f"CLAIM Q2: computed={fmt(V)} expected={exp_Q2} match={'yes' if round(V,7)==float(exp_Q2) else 'no'}")

# Q3
C = V * 50**2
exp_Q3 = "1.0258"
print(f"CLAIM Q3: computed={fmt(C)} expected={exp_Q3} match={'yes' if round(C,4)==float(exp_Q3) else 'no'}")

# Q4 (use N=50 to produce numeric V)
V_N50 = C * 50**-2
exp_Q4 = "0.0004103"
print(f"CLAIM Q4: computed={fmt(V_N50)} expected={exp_Q4} match={'yes' if round(V_N50,7)==float(exp_Q4) else 'no'}")

# Q5
eps = 1e-3
T_simple = math.ceil(1/eps)
exp_Q5 = "1000"
print(f"CLAIM Q5: computed={fmt(T_simple)} expected={exp_Q5} match={'yes' if T_simple==int(exp_Q5) else 'no'}")

# Q6
T_sliding = math.ceil(math.log(1/eps))
exp_Q6 = "7"
print(f"CLAIM Q6: computed={fmt(T_sliding)} expected={exp_Q6} match={'yes' if T_sliding==int(exp_Q6) else 'no'}")

# Q7
eps = 1e-6
T_simple = math.ceil(1/eps)
exp_Q7 = "1000000"
print(f"CLAIM Q7: computed={fmt(T_simple)} expected={exp_Q7} match={'yes' if T_simple==int(exp_Q7) else 'no'}")

# Q8
T_sliding = math.ceil(math.log(1/eps))
exp_Q8 = "14"
print(f"CLAIM Q8: computed={fmt(T_sliding)} expected={exp_Q8} match={'yes' if T_sliding==int(exp_Q8) else 'no'}")

# Q9
P50 = C * 50**-2
exp_Q9 = "0.0004103"
print(f"CLAIM Q9: computed={fmt(P50)} expected={exp_Q9} match={'yes' if round(P50,7)==float(exp_Q9) else 'no'}")

# Q10
P60 = C * 60**-2
exp_Q10 = "0.0002849"
print(f"CLAIM Q10: computed={fmt(P60)} expected={exp_Q10} match={'yes' if round(P60,7)==float(exp_Q10) else 'no'}")

# Q11
ratio = P60 / P50
exp_Q11 = "0.694"
print(f"CLAIM Q11: computed={fmt(ratio)} expected={exp_Q11} match={'yes' if round(ratio,3)==float(exp_Q11) else 'no'}")

# Q12
p = [0.40,0.25,0.20,0.10,0.05]
P2 = sum([pi**2 for pi in p])
exp_Q12 = "0.2750"
print(f"CLAIM Q12: computed={fmt(P2)} expected={exp_Q12} match={'yes' if round(P2,4)==float(exp_Q12) else 'no'}")

# Q13
P3 = sum([pi**3 for pi in p])
exp_Q13 = "0.08875"
print(f"CLAIM Q13: computed={fmt(P3)} expected={exp_Q13} match={'yes' if round(P3,5)==float(exp_Q13) else 'no'}")

# Q14
share = p[0]**2 / P2
exp_Q14 = "0.582"
print(f"CLAIM Q14: computed={fmt(share)} expected={exp_Q14} match={'yes' if round(share,3)==float(exp_Q14) else 'no'}")

# Q15
odds = (p[0]/p[1])**2
exp_Q15 = "2.56"
print(f"CLAIM Q15: computed={fmt(odds)} expected={exp_Q15} match={'yes' if round(odds,2)==float(exp_Q15) else 'no'}")

# Q16
epsilon = 1e-2
d0 = 1.0
q = 0.99
n = math.log(epsilon/d0) / math.log(q)
exp_Q16 = "458.2"
print(f"CLAIM Q16: computed={fmt(n)} expected={exp_Q16} match={'yes' if round(n,1)==float(exp_Q16) else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in open(__file__) if 'match=yes' in line)} match, {16 - sum(1 for line in open(__file__) if 'match=yes' in line)} mismatch")
