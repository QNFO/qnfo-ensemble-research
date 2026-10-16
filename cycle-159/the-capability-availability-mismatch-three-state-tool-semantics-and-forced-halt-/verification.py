import math
from fractions import Fraction

def sig(x, n=8):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: 3^10 / 2^10
c1 = 3**10 / 2**10
results.append(("Q1", c1, "57.7"))

# Q2: 59049 - 1024
c2 = 3**10 - 2**10
results.append(("Q2", c2, "58025"))

# Q3: (2/3)^5 = 32/243
c3 = Fraction(2, 3)**5
c3f = float(c3)
results.append(("Q3", c3f, "0.132"))

# Q4: 1 - 32/243
c4 = 1 - Fraction(32, 243)
c4f = float(c4)
results.append(("Q4", c4f, "0.868"))

# Q5: 0.90 * (1 - 0.70)
c5 = 0.90 * (1 - 0.70)
results.append(("Q5", c5, "0.27"))

# Q6: 1 - (1 - 0.27)^5
c6 = 1 - (1 - 0.27)**5
results.append(("Q6", c6, "0.793"))

# Q7: 1 - (1 - 0.27)^10
c7 = 1 - (1 - 0.27)**10
results.append(("Q7", c7, "0.957"))

# Q8: s* = 0.27 * c_t (symbolic; report coefficient)
c8 = 0.27
results.append(("Q8", c8, "0.27"))

# Q9: (2/4)^5 = 1/32
c9 = Fraction(2, 4)**5
c9f = float(c9)
results.append(("Q9", c9f, "0.03125"))

mismatch = 0
for cid, comp, exp in results:
    # match: computed rounded to paper's stated sig digits equals expected
    if cid in ("Q1",):
        match = "yes" if abs(comp - 57.7) < 0.05 else "no"
    elif cid in ("Q3",):
        match = "yes" if abs(comp - 0.132) < 0.0005 else "no"
    elif cid in ("Q4",):
        match = "yes" if abs(comp - 0.868) < 0.0005 else "no"
    elif cid in ("Q5",):
        match = "yes" if abs(comp - 0.27) < 1e-9 else "no"
    elif cid in ("Q6",):
        match = "yes" if abs(comp - 0.793) < 0.0005 else "no"
    elif cid in ("Q7",):
        match = "yes" if abs(comp - 0.957) < 0.0005 else "no"
    elif cid in ("Q8",):
        match = "yes" if abs(comp - 0.27) < 1e-9 else "no"
    elif cid in ("Q9",):
        match = "yes" if abs(comp - 0.03125) < 1e-9 else "no"
    else:
        match = "yes" if abs(comp - float(exp)) < 1e-9 else "no"
    if match == "no":
        mismatch += 1
    print(f"CLAIM {cid}: computed={sig(comp)} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mismatch} match, {mismatch} mismatch")
