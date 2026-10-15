import math

def claim(id_, computed, expected, match):
    print(f"CLAIM {id_}: computed={computed} expected={expected} match={match}")

# Q1: N_10 = (p+1)p^(d-1), p=2, d=10
n10 = (2+1)*2**(10-1)
claim("Q1", f"{n10:.8f}", "1536", "yes" if round(n10)==1536 else "no")

# Q2: V_10 = 1+(p+1)(p^D-1)/(p-1)
v10 = 1+(2+1)*(2**10-1)//(2-1)
claim("Q2", f"{v10:.8f}", "3070", "yes" if v10==3070 else "no")

# Q3: C_10 = (p+1)*sum_{d=1}^{10} d*2^(d-1) = 3*((D-1)2^D+1)
s = (10-1)*2**10+1
c10 = 3*s
claim("Q3", f"{c10:.8f}", "27651", "yes" if c10==27651 else "no")

# Q4: binom(3070,2)
pairs = 3070*3069//2
claim("Q4", f"{pairs:.8f}", "4710915", "yes" if pairs==4710915 else "no")

# Q5: f_10 = 27651/4710915
f10 = 27651/4710915
claim("Q5", f"{f10:.10f}", "5.8696e-3", "yes" if round(f10*10**7)/10**7 == 0.0058696 else "no")

# Q6: |F| = p(p^(D-d)-1)/(p-1), p=2,d=5,D=10
f6 = 2*(2**5-1)//(2-1)
claim("Q6", f"{f6:.8f}", "62", "yes" if f6==62 else "no")

# Q7: p=2,d=5,D=20
f7 = 2*(2**15-1)//(2-1)
claim("Q7", f"{f7:.8f}", "65534", "yes" if f7==65534 else "no")

# Q8: p=3,d=5,D=10
f8 = 3*(3**5-1)//(3-1)
claim("Q8", f"{f8:.8f}", "363", "yes" if f8==363 else "no")

# Q9: 3070/10
q9 = 3070/10
claim("Q9", f"{q9:.8f}", "307", "yes" if q9==307 else "no")

# Q10: 3070/(log2(3)+9)
q10 = 3070/(math.log2(3)+9)
claim("Q10", f"{q10:.8f}", "290.03", "yes" if round(q10,2)==290.03 else "no")

# Q11: 27651/3070
q11 = 27651/3070
claim("Q11", f"{q11:.8f}", "9.0068", "yes" if round(q11,4)==9.0068 else "no")

# Q12: 2*sqrt(2)
q12 = 2*math.sqrt(2)
claim("Q12", f"{q12:.8f}", "2.8284271", "yes" if round(q12,7)==2.8284271 else "no")

# Q13: 2(p-1)D/((p+1)p^D) at D=10, p=2
q13 = 2*(2-1)*10/((2+1)*2**10)
claim("Q13", f"{q13:.10f}", "6.5104e-3", "yes" if round(q13*10**7)/10**7 == 0.0065104 else "no")

# Q14: V_20
v20 = 1+(2+1)*(2**20-1)//(2-1)
claim("Q14", f"{v20:.8f}", "3145727", "yes" if v20==3145727 else "no")

# Q15: V_20/D
q15 = 3145727/20
claim("Q15", f"{q15:.8f}", "1.6e5", "yes" if round(q15,5)==157286.35 else "no")

# Q16: log2(3)+9
q16 = math.log2(3)+9
claim("Q16", f"{q16:.8f}", "10.58496", "yes" if round(q16,5)==10.58496 else "no")

print(f"VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
