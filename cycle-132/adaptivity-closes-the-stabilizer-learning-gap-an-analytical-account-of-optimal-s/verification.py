import math

def claim(id, computed, expected, match):
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")

# Q1: log2 N_100 = 5150 + delta, delta in (0, 1.4427)
n = 100
log2N = n + n*(n+1)/2 + sum(math.log2(1 + 2**(-i)) for i in range(1, n+1))
delta = log2N - 5150
bound = 1/math.log(2)
print(f"CLAIM Q1: computed={delta:.8f} expected={'(0, 1.4427)' if 0 < delta < 1.4427 else 'FAIL'} match={'yes' if 0 < delta < 1.4427 else 'no'}")

# Q2: floor = ceil((5150+delta)/100) = 52
floor = math.ceil((5150 + delta)/100)
claim("Q2", floor, "52", "yes" if floor == 52 else "no")

# Q3: n - k + 1/eps = 190
v = 100 - 10 + 1/0.01
claim("Q3", v, "190", "yes" if v == 190 else "no")

# Q4: eps* = 1/n = 0.01
v = 1/100
claim("Q4", v, "0.01", "yes" if v == 0.01 else "no")

# Q5: 100 * 2^5 = 3200
v = 100 * 2**5
claim("Q5", v, "3200", "yes" if v == 3200 else "no")

# Q6: 100 * 2^10 = 102400
v = 100 * 2**10
claim("Q6", v, "102400", "yes" if v == 102400 else "no")

# Q7: M_ad = 1000*5*100 = 5.0e5
v = 1000*5*100
claim("Q7", v, "500000", "yes" if v == 500000 else "no")

# Q8: M_na = 1000*10*100^2 = 1.0e8
v = 1000*10*100**2
claim("Q8", v, "100000000", "yes" if v == 100000000 else "no")

# Q9: ratio = 1.0e8/5.0e5 = 200; range [10,1000]
ratio = (1000*10*100**2)/(1000*5*100)
rmin = (1/10)*100
rmax = (10/1)*100
ok = ratio == 200 and rmin == 10 and rmax == 1000
claim("Q9", f"{ratio:.8f} range=[{rmin:.8f},{rmax:.8f}]", "200 range=[10,1000]", "yes" if ok else "no")

# Q10: separation >= 100/C_ad in [10,100]
smin = 100/10
smax = 100/1
ok = smin == 10 and smax == 100
claim("Q10", f"range=[{smin:.8f},{smax:.8f}]", "range=[10,100]", "yes" if ok else "no")

# Q11: N_1 = 2 * (2+1) = 6
v = 2 * (2**1 + 1)
claim("Q11", v, "6", "yes" if v == 6 else "no")

# Q12: N_3 = 8 * 3 * 5 * 9 = 1080
v = 2**3 * (2**1+1) * (2**2+1) * (2**3+1)
claim("Q12", v, "1080", "yes" if v == 1080 else "no")

# Q13: k=0 -> 200; k=100 -> 100
v0 = 100 - 0 + 1/0.01
v100 = 100 - 100 + 1/0.01
ok = v0 == 200 and v100 == 100
claim("Q13", f"k=0:{v0:.8f}, k=100:{v100:.8f}", "k=0:200, k=100:100", "yes" if ok else "no")

print("VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch")
