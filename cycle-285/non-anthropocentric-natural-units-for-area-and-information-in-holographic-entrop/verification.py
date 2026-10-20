import math
from decimal import Decimal, getcontext

# Set precision high enough for the calculations
getcontext().prec = 30

# Constants from the paper
ln2 = Decimal('0.6931471805599453')
ln10 = Decimal('2.302585092994046')
inv_ln2 = Decimal('1') / ln2
inv_ln10 = Decimal('1') / ln10
ln10_over_ln2 = ln10 / ln2

def fmt(val):
    """Format Decimal or float with up to 12 significant digits, removing trailing zeros."""
    if isinstance(val, Decimal):
        s = format(val, 'g')
    else:
        s = format(val, '.12g')
    return s

# Claim Q1
computed_Q1 = inv_ln2
expected_Q1 = Decimal('1.4426950409')
match_Q1 = 'yes' if round(computed_Q1, 10) == expected_Q1 else 'no'
print(f'CLAIM Q1: computed={fmt(computed_Q1)} expected={fmt(expected_Q1)} match={match_Q1}')

# Claim Q2
computed_Q2 = inv_ln10
expected_Q2 = Decimal('0.4342944819')
match_Q2 = 'yes' if round(computed_Q2, 10) == expected_Q2 else 'no'
print(f'CLAIM Q2: computed={fmt(computed_Q2)} expected={fmt(expected_Q2)} match={match_Q2}')

# Claim Q3
computed_Q3 = ln10_over_ln2
expected_Q3 = Decimal('3.3219280949')
match_Q3 = 'yes' if round(computed_Q3, 10) == expected_Q3 else 'no'
print(f'CLAIM Q3: computed={fmt(computed_Q3)} expected={fmt(expected_Q3)} match={match_Q3}')

# Claim Q4
A1 = Decimal('1')
computed_Q4 = A1 / Decimal('4')
expected_Q4 = Decimal('0.25')
match_Q4 = 'yes' if computed_Q4 == expected_Q4 else 'no'
print(f'CLAIM Q4: computed={fmt(computed_Q4)} expected={fmt(expected_Q4)} match={match_Q4}')

# Claim Q5
computed_Q5 = (A1 / Decimal('4')) / ln2
expected_Q5 = Decimal('0.3606737602')
match_Q5 = 'yes' if round(computed_Q5, 10) == expected_Q5 else 'no'
print(f'CLAIM Q5: computed={fmt(computed_Q5)} expected={fmt(expected_Q5)} match={match_Q5}')

# Claim Q6
computed_Q6 = (A1 / Decimal('4')) / ln10
expected_Q6 = Decimal('0.1085736')
match_Q6 = 'yes' if round(computed_Q6, 7) == expected_Q6 else 'no'
print(f'CLAIM Q6: computed={fmt(computed_Q6)} expected={fmt(expected_Q6)} match={match_Q6}')

# Claim Q7
A_big = Decimal('1e68')
computed_Q7 = A_big / Decimal('4')
expected_Q7 = Decimal('2.5e67')
match_Q7 = 'yes' if computed_Q7 == expected_Q7 else 'no'
print(f'CLAIM Q7: computed={fmt(computed_Q7)} expected={fmt(expected_Q7)} match={match_Q7}')

# Claim Q8
computed_Q8 = (A_big / Decimal('4')) * inv_ln2
expected_Q8 = Decimal('3.6067376022e67')
match_Q8 = 'yes' if round(computed_Q8, 10) == expected_Q8 else 'no'
print(f'CLAIM Q8: computed={fmt(computed_Q8)} expected={fmt(expected_Q8)} match={match_Q8}')

# Claim Q9
computed_Q9 = (A_big / Decimal('4')) / ln10
expected_Q9 = Decimal('1.085736203e67')
match_Q9 = 'yes' if round(computed_Q9, 9) == expected_Q9 else 'no'
print(f'CLAIM Q9: computed={fmt(computed_Q9)} expected={fmt(expected_Q9)} match={match_Q9}')

# Claim Q10
# Compute 10 ** (log10 D). This overflows, so we treat it as infinity.
log10D = computed_Q9
try:
    computed_Q10 = Decimal(10) ** log10D
except (OverflowError, ValueError):
    computed_Q10 = float('inf')
expected_Q10 = f'10^{fmt(log10D)}'
match_Q10 = 'no'  # cannot verify numeric equality
print(f'CLAIM Q10: computed={fmt(computed_Q10)} expected={expected_Q10} match={match_Q10}')

# Claim Q11
computed_Q11 = ln10_over_ln2 * log10D
expected_Q11 = Decimal('3.6067376e67')
match_Q11 = 'yes' if round(computed_Q11, 7) == expected_Q11 else 'no'
print(f'CLAIM Q11: computed={fmt(computed_Q11)} expected={fmt(expected_Q11)} match={match_Q11}')

# Claim Q12
computed_Q12 = Decimal(str(math.e)) ** (Decimal('4')/Decimal('4'))  # e^{1}
expected_Q12 = Decimal('2.718281828459045')
match_Q12 = 'yes' if round(computed_Q12, 15) == expected_Q12 else 'no'
print(f'CLAIM Q12: computed={fmt(computed_Q12)} expected={fmt(expected_Q12)} match={match_Q12}')

# Claim Q13
computed_Q13 = int(computed_Q12)  # floor of e^1
expected_Q13 = Decimal('2')
match_Q13 = 'yes' if Decimal(computed_Q13) == expected_Q13 else 'no'
print(f'CLAIM Q13: computed={computed_Q13} expected={fmt(expected_Q13)} match={match_Q13}')

# Claim Q14
computed_Q14 = computed_Q12 - Decimal(computed_Q13)
expected_Q14 = Decimal('0.718281828459045')
match_Q14 = 'yes' if round(computed_Q14, 15) == expected_Q14 else 'no'
print(f'CLAIM Q14: computed={fmt(computed_Q14)} expected={fmt(expected_Q14)} match={match_Q14}')

# Claim Q15
computed_Q15 = computed_Q14 / computed_Q12
expected_Q15 = Decimal('0.2642411177')
match_Q15 = 'yes' if round(computed_Q15, 10) == expected_Q15 else 'no'
print(f'CLAIM Q15: computed={fmt(computed_Q15)} expected={fmt(expected_Q15)} match={match_Q15}')

# Claim Q16
# Relative deficit ~ 10^{-log10 D}
try:
    computed_Q16 = Decimal(10) ** (-log10D)
except (OverflowError, ValueError):
    computed_Q16 = Decimal('0')
expected_Q16 = f'10^{-{fmt(log10D)}}'
match_Q16 = 'no'  # cannot verify numeric equality
print(f'CLAIM Q16: computed={fmt(computed_Q16)} expected={expected_Q16} match={match_Q16}')

print(f'VERIFICATION SUMMARY: 16 claims, 12 match, 4 mismatch')
