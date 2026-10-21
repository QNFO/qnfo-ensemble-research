# Verification script for quantitative claims Q1–Q16

def fmt(val):
    """Format numbers with at least 8 significant digits."""
    if isinstance(val, float):
        # Use 8 significant digits, remove trailing zeros
        s = f"{val:.8g}"
    else:
        s = str(val)
    return s

# Q1: 2^n with n=3
n1 = 3
c1 = 2 ** n1
e1 = "8"
print(f"CLAIM Q1: computed={fmt(c1)} expected={e1} match={'yes' if fmt(c1)==e1 else 'no'}")

# Q2: survivors = 1 (given)
c2 = 1
e2 = "1"
print(f"CLAIM Q2: computed={fmt(c2)} expected={e2} match={'yes' if fmt(c2)==e2 else 'no'}")

# Q3: elimination rate = (total - survivors)/total = (8-1)/8 = 7/8
total3 = 8
survivors3 = 1
c3 = (total3 - survivors3) / total3
e3 = "0.875"
print(f"CLAIM Q3: computed={fmt(c3)} expected={e3} match={'yes' if fmt(c3)==e3 else 'no'}")

# Q4: 2^n with n=10
n4 = 10
c4 = 2 ** n4
e4 = "1024"
print(f"CLAIM Q4: computed={fmt(c4)} expected={e4} match={'yes' if fmt(c4)==e4 else 'no'}")

# Q5: 2^{|W|*|W|} with |W|=8 => 2^{64}
W5 = 8
c5 = 2 ** (W5 * W5)
e5 = "18446744073709551616"
print(f"CLAIM Q5: computed={fmt(c5)} expected={e5} match={'yes' if fmt(c5)==e5 else 'no'}")

# Q6: 2^{|W|*|W| - |W|} = 2^{56}
c6 = 2 ** (W5 * W5 - W5)
e6 = "72057594037927936"
print(f"CLAIM Q6: computed={fmt(c6)} expected={e6} match={'yes' if fmt(c6)==e6 else 'no'}")

# Q7: initial Wise Men worlds = 2^3
agents7 = 3
c7 = 2 ** agents7
e7 = "8"
print(f"CLAIM Q7: computed={fmt(c7)} expected={e7} match={'yes' if fmt(c7)==e7 else 'no'}")

# Q8: after king announcement = initial - 1
c8 = 8 - 1
e8 = "7"
print(f"CLAIM Q8: computed={fmt(c8)} expected={e8} match={'yes' if fmt(c8)==e8 else 'no'}")

# Q9: after agent a announcement = previous - 1
c9 = 7 - 1
e9 = "6"
print(f"CLAIM Q9: computed={fmt(c9)} expected={e9} match={'yes' if fmt(c9)==e9 else 'no'}")

# Q10: after agent b announcement = previous - 2
c10 = 6 - 2
e10 = "4"
print(f"CLAIM Q10: computed={fmt(c10)} expected={e10} match={'yes' if fmt(c10)==e10 else 'no'}")

# Q11: shrinkage factor = 7 / 4
c11 = 7 / 4
e11 = "1.75"
print(f"CLAIM Q11: computed={fmt(c11)} expected={e11} match={'yes' if fmt(c11)==e11 else 'no'}")

# Q12: product model size = |W| * |E| = 8 * 3
W12 = 8
E12 = 3
c12 = W12 * E12
e12 = "24"
print(f"CLAIM Q12: computed={fmt(c12)} expected={e12} match={'yes' if fmt(c12)==e12 else 'no'}")

# Q13: L1 = 2^{L0} with L0=1
L0 = 1
c13 = 2 ** L0
e13 = "2"
print(f"CLAIM Q13: computed={fmt(c13)} expected={e13} match={'yes' if fmt(c13)==e13 else 'no'}")

# Q14: L2 = 2^{L1}
L1 = c13
c14 = 2 ** L1
e14 = "4"
print(f"CLAIM Q14: computed={fmt(c14)} expected={e14} match={'yes' if fmt(c14)==e14 else 'no'}")

# Q15: L3 = 2^{L2}
L2 = c14
c15 = 2 ** L2
e15 = "16"
print(f"CLAIM Q15: computed={fmt(c15)} expected={e15} match={'yes' if fmt(c15)==e15 else 'no'}")

# Q16: L4 = 2^{L3}
L3 = c15
c16 = 2 ** L3
e16 = "65536"
print(f"CLAIM Q16: computed={fmt(c16)} expected={e16} match={'yes' if fmt(c16)==e16 else 'no'}")

# Summary
total = 16
matches = sum(1 for line in [
    fmt(c1)==e1, fmt(c2)==e2, fmt(c3)==e3, fmt(c4)==e4,
    fmt(c5)==e5, fmt(c6)==e6, fmt(c7)==e7, fmt(c8)==e8,
    fmt(c9)==e9, fmt(c10)==e10, fmt(c11)==e11, fmt(c12)==e12,
    fmt(c13)==e13, fmt(c14)==e14, fmt(c15)==e15, fmt(c16)==e16
] if line)
mismatches = total - matches
print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {mismatches} mismatch")
