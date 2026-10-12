import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, n - 1 - math.floor(math.log10(abs(x))))

claims = []

# Q1: P_rep = 0.8^5
c1 = 0.8**5
claims.append(("Q1", c1, "0.32768"))

# Q2: (1-0.2^3)^5
c2 = (1 - 0.2**3)**5
claims.append(("Q2", c2, "0.9606"))

# Q3: E[N] = 1/0.8; total = 5*1.25
e3 = 1/0.8
t3 = 5*e3
claims.append(("Q3", t3, "6.25"))

# Q4: E[N] = sum_{j=1}^{3} j*0.2^(j-1)*0.8 + 3*0.2^3; total = 5*E[N]
e4 = sum(j*(0.2**(j-1))*0.8 for j in range(1,4)) + 3*(0.2**3)
t4 = 5*e4
claims.append(("Q4", t4, "6.20"))

# Q5: T_in = 10400 + 5*2000 + 30*500; T_total = T_in + 25*1000
t_in = 10400 + 5*2000 + (5+25)*500
t5 = t_in + 25*1000
claims.append(("Q5", t5, "60400"))

# Q6: N_calls = 5+25
c6 = 5 + 25
claims.append(("Q6", c6, "30"))

# Q7: T_retr = 10*(10400+500) + 60400
c7 = 10*(10400+500) + 60400
claims.append(("Q7", c7, "169400"))

# Q8: H0 = 25*log2(10)
c8 = 25*math.log2(10)
claims.append(("Q8", c8, "83.05"))

# Q9: H <= 25*(0.5*log2(10))
c9 = 25*(0.5*math.log2(10))
claims.append(("Q9", c9, "41.5"))

# Q10: ratio = 0.992^5 / 0.8^5
c10 = ((1-0.2**3)**5)/(0.8**5)
claims.append(("Q10", c10, "2.9316"))

# Q11: 0.8^10 and 0.992^10
c11a = 0.8**10
c11b = (1-0.2**3)**10
claims.append(("Q11", c11b, "0.9228"))

# Q12: 1-0.4^3
c12 = 1 - 0.4**3
claims.append(("Q12", c12, "0.936"))

# Q13: 60400 - 25000 + 3*25*1000
c13 = 60400 - 25000 + 3*25*1000
claims.append(("Q13", c13, "110400"))

# Q14: 10^4 * 169400
c14 = 10**4 * 169400
claims.append(("Q14", c14, "1694000000"))

# Q15: 1 - 0.8^5/0.8^2
c15 = 1 - (0.8**5)/(0.8**2)
claims.append(("Q15", c15, "0.488"))

mism = 0
for cid, comp, exp in claims:
    # match check: round computed to sig digits of expected
    digits = len(exp.replace(".", "").lstrip("0")) if "." in exp else len(exp)
    m = sig(comp, digits)
    match = ("yes" if abs(m - float(exp)) < 1e-12 * max(1, abs(float(exp))) else "no")
    if match == "no":
        mism += 1
    print(f"CLAIM {cid}: computed={comp:.8f} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {len(claims)-mism} match, {mism} mismatch")
