from fractions import Fraction

def fmt(val):
    # format with at least 8 significant digits, remove trailing .0 for integers
    s = f"{float(val):.8g}"
    if s.endswith('.0'):
        s = s[:-2]
    return s

expected = {
    "Q1": "1",
    "Q2": "1",
    "Q3": "1",
    "Q4": "3",
    "Q5": "6",
    "Q6": "12",
    "Q7": "24",
    "Q8": "48",
    "Q9": "94",
    "Q10": "4",
    "Q11": "12",
    "Q12": "36",
    "Q13": "108",
    "Q14": "324",
    "Q15": "485",
    "Q16": "1",
}

# Q1
c1 = Fraction(1,2) * 3 * Fraction(2,3)
# Q2
c2 = Fraction(1,5) * 7 * Fraction(5,7)
# Q3
c3 = 4 * Fraction(3,4) * Fraction(1,3)
# Q4
c4 = 3
# Q5
c5 = 3 * 2
# Q6
c6 = 3 * 4
# Q7
c7 = 3 * 8
# Q8
c8 = 3 * 16
# Q9
c9 = 1 + 3 * (2**5 - 1) // 1  # integer arithmetic
# Q10
c10 = 4
# Q11
c11 = 4 * 3
# Q12
c12 = 4 * 9
# Q13
c13 = 4 * 27
# Q14
c14 = 4 * 81
# Q15
c15 = 1 + 4 * (3**5 - 1) // 2
# Q16
c16 = 1

claims = {
    "Q1": c1,
    "Q2": c2,
    "Q3": c3,
    "Q4": c4,
    "Q5": c5,
    "Q6": c6,
    "Q7": c7,
    "Q8": c8,
    "Q9": c9,
    "Q10": c10,
    "Q11": c11,
    "Q12": c12,
    "Q13": c13,
    "Q14": c14,
    "Q15": c15,
    "Q16": c16,
}

match_count = 0
for qid, val in claims.items():
    comp = fmt(val)
    exp = expected[qid]
    match = "yes" if comp == exp else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims)-match_count} mismatch")
