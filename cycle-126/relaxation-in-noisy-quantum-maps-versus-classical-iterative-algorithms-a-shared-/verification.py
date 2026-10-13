import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

ln10 = math.log(10)

# Q1
t1 = math.log(1e-6 / 1) / math.log(0.99)
# Q2
t2 = math.log(1e-6 / 1) / math.log(0.999)
# Q3
r3 = t2 / t1
# Q4
t4 = math.log(2 * 0.874 - 1) / math.log(0.99)
# Q5
t5 = math.log(2 * 0.874 - 1) / math.log(0.9)
# Q6
t6 = math.log(2 * 0.874 - 1) / math.log(0.999)
# Q7
dt7 = ln10 / (-math.log(0.99))

print("CLAIM Q1: computed=%.8f expected=1374.6 match=%s" % (t1, "yes" if sig(t1, 5) == 1374.6 else "no"))
print("CLAIM Q2: computed=%.8f expected=13808.6 match=%s" % (t2, "yes" if sig(t2, 6) == 13808.6 else "no"))
print("CLAIM Q3: computed=%.8f expected=10.045 match=%s" % (r3, "yes" if sig(r3, 4) == 10.045 else "no"))
print("CLAIM Q4: computed=%.8f expected=28.9 match=%s" % (t4, "yes" if sig(t4, 3) == 28.9 else "no"))
print("CLAIM Q5: computed=%.8f expected=2.756 match=%s" % (t5, "yes" if sig(t5, 4) == 2.756 else "no"))
print("CLAIM Q6: computed=%.8f expected=290.2 match=%s" % (t6, "yes" if sig(t6, 4) == 290.2 else "no"))
print("CLAIM Q7: computed=%.8f expected=229.1 match=%s" % (dt7, "yes" if sig(dt7, 4) == 229.1 else "no"))

claims = [sig(t1,5)==1374.6, sig(t2,6)==13808.6, sig(r3,4)==10.045, sig(t4,3)==28.9, sig(t5,4)==2.756, sig(t6,4)==290.2, sig(dt7,4)==229.1]
m = sum(claims)
print("VERIFICATION SUMMARY: %d claims, %d match, %d mismatch" % (len(claims), m, len(claims) - m))
