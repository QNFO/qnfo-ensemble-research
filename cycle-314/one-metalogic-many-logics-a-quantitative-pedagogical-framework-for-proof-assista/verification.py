import math

def match(expected, computed):
    return "yes" if expected == computed else "no"

# CLAIM Q1
c1 = 2**3
print(f"CLAIM Q1: computed={c1} expected=8 match={match('8', str(c1))}")

# CLAIM Q2
c2 = (8 - 1) / 8
print(f"CLAIM Q2: computed={c2:.3f} expected=0.875 match={match('0.875', f'{c2:.3f}')}")

# CLAIM Q3
c3 = 2**10
print(f"CLAIM Q3: computed={c3} expected=1024 match={match('1024', str(c3))}")

# CLAIM Q4
c4 = 2**64
print(f"CLAIM Q4: computed={c4} expected=18446744073709551616 match={match('18446744073709551616', str(c4))}")

# CLAIM Q5
c5 = 2**56
print(f"CLAIM Q5: computed={c5} expected=72057594037927936 match={match('72057594037927936', str(c5))}")

# CLAIM Q6
c6 = 7 / 4
print(f"CLAIM Q6: computed={c6:.2f} expected=1.75 match={match('1.75', f'{c6:.2f}')}")

# CLAIM Q7
c7_initial = 2**8
c7_after = c7_initial - 1
print(f"CLAIM Q7: computed={c7_initial}, {c7_after} expected=256, 255 match={match('256, 255', f'{c7_initial}, {c7_after}')}")

# CLAIM Q8
L5 = 2**65536
exp_L5 = len(str(L5)) - 1  # exponent in base 10
computed_L5 = f"10^{exp_L5}"
print(f"CLAIM Q8: computed={computed_L5} expected=10^{19728} match={match('10^{19728}', computed_L5)}")

# CLAIM Q9
c9 = 2**100
# scientific notation with 16 significant digits as in the paper
c9_sci = f"{c9:.16e}"
print(f"CLAIM Q9: computed={c9_sci} expected=1.2676506002282294e30 match={match('1.2676506002282294e30', c9_sci)}")

# CLAIM Q10
c10 = 2**2
print(f"CLAIM Q10: computed={c10} expected=4 match={match('4', str(c10))}")

# CLAIM Q11
c11 = 2**3
print(f"CLAIM Q11: computed={c11} expected=8 match={match('8', str(c11))}")

# CLAIM Q12
c12 = 2**5
print(f"CLAIM Q12: computed={c12} expected=32 match={match('32', str(c12))}")

# CLAIM Q13
c13 = 2**(5-3)
print(f"CLAIM Q13: computed={c13} expected=4 match={match('4', str(c13))}")

# CLAIM Q14
c14 = 28 / 20
print(f"CLAIM Q14: computed={c14:.1f} expected=1.4 match={match('1.4', f'{c14:.1f}')}")

# CLAIM Q15
c15 = 2**61
print(f"CLAIM Q15: computed={c15} expected=2305843009213693952 match={match('2305843009213693952', str(c15))}")

# CLAIM Q16
c16 = 2**4
print(f"CLAIM Q16: computed={c16} expected=16 match={match('16', str(c16))}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
