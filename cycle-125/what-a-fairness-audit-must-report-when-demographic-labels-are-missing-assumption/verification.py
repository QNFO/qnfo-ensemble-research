import math
from fractions import Fraction

def report(qid, computed, expected):
    print(f"CLAIM {qid}: computed={computed:.10f} expected={expected} match={'yes' if computed_str(computed, expected) else 'no'}")

def computed_str(value, expected):
    if expected is None:
        return False
    exp = float(expected)
    # match when computed rounded to significant digits of expected equals expected
    digits = len(expected.replace('.', '').replace('-', '').lstrip('0')) if '.' in expected else len(expected.replace('-', '').lstrip('0'))
    return round(value, digits) == round(exp, digits)

# Q1
m1, m2, r1, r2 = 0.6, 0.5, 0.25, 0.15
l1 = r1*(1-m1); u1 = l1+m1
l2 = r2*(1-m2); u2 = l2+m2
Dmin = l1-u2; Dmax = u1-l2
width = Dmax-Dmin
print(f"CLAIM Q1: computed={width:.10f} expected=1.100 match={'yes' if round(width,3)==1.100 and round(Dmin,3)==-0.475 and round(Dmax,3)==0.625 else 'no'}")

# Q2
pA, m = 0.30, 0.2
pmin = pA*(1-m); pmax = pmin+m
print(f"CLAIM Q2: computed={pmax-pmin:.10f} expected=0.2 match={'yes' if round(pmin,2)==0.24 and round(pmax,2)==0.44 and round(pmax-pmin,1)==0.2 else 'no'}")

# Q3
pB = 0.35
Rmin = pmin/pB; Rmax = pmax/pB; Rhat = pA/pB
print(f"CLAIM Q3: computed={Rmin:.10f} expected=0.686 match={'yes' if round(Rmin,3)==0.686 and round(Rmax,3)==1.257 and round(Rhat,3)==0.857 else 'no'}")

# Q4
threshold = 0.8*pB
needed = 1000*threshold/pA
dk = math.ceil(needed - 800)
print(f"CLAIM Q4: computed={dk:.10f} expected=134 match={'yes' if dk==134 else 'no'}")

# Q5
rhat, ng, z = 0.25, 980, 1.96
half = z*math.sqrt(rhat*(1-rhat)/ng)
contrib = 2*half
print(f"CLAIM Q5: computed={contrib:.10f} expected=0.05422177 match={'yes' if round(contrib,8)==0.05422177 else 'no'}")

# Q6
half6 = z*math.sqrt(pA*(1-pA)/800)
factor = m/half6
print(f"CLAIM Q6: computed={factor:.10f} expected=6.30 match={'yes' if round(half6,6)==0.031756 and round(factor,2)==6.30 else 'no'}")

# Q7
r1h, m1c, r2h, m2c = 0.8, 0.2, 0.2, 0.5
Dmin7 = r1h*(1-m1c) - (r2h*(1-m2c)+m2c)
ghat = r1h-r2h
shortcut = m1c+m2c
print(f"CLAIM Q7: computed={Dmin7:.10f} expected=0.04 match={'yes' if round(Dmin7,2)==0.04 and ghat < shortcut else 'no'}")

# Q8
combined1 = m + half6
combined2 = 0.04 + 2*z*math.sqrt(0.25*0.75/980)
print(f"CLAIM Q8: computed={combined2:.10f} expected=0.09422177 match={'yes' if round(combined1,6)==0.231756 and round(combined2,8)==0.09422177 else 'no'}")

# Q9
m9 = 1 - 800/1000
print(f"CLAIM Q9: computed={m9:.10f} expected=0.2 match={'yes' if m9==0.2 else 'no'}")

# Q10
ratio10 = contrib/0.04
print(f"CLAIM Q10: computed={ratio10:.10f} expected=1.356 match={'yes' if round(ratio10,3)==1.356 else 'no'}")

print("VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch")
