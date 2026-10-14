import math
from fractions import Fraction

def sig(x, n=6):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

def fmt(x):
    # at least 8 significant digits
    return f"{x:.8g}"

claims = []

# Q1: omega_2 = 6.283185 / 0.693147
c = 6.283185 / 0.693147
claims.append(("Q1", c, "9.064722"))

# Q2: omega_3 = 6.283185 / 1.098612
c = 6.283185 / 1.098612
claims.append(("Q2", c, "5.719203"))

# Q3: omega_5 = 6.283185 / 1.609438
c = 6.283185 / 1.609438
claims.append(("Q3", c, "3.903962"))

# Q4: omega_7 = 6.283185 / 1.945910
c = 6.283185 / 1.945910
claims.append(("Q4", c, "3.228919"))

# Q5: ratio omega_2/omega_3 = ln3/ln2 = 1.098612 / 0.693147
c = 1.098612 / 0.693147
claims.append(("Q5", c, "1.584962"))

# Q6: ratio omega_2/omega_5 = ln5/ln2 = 1.609438 / 0.693147
c = 1.609438 / 0.693147
claims.append(("Q6", c, "2.321929"))

# Q7: ratio omega_3/omega_5 = ln5/ln3 = 1.609438 / 1.098612
c = 1.609438 / 1.098612
claims.append(("Q7", c, "1.464974"))

# Q8: mean of omega_p = (9.064722 + 5.719203 + 3.903962 + 3.228919) / 4
c = (9.064722 + 5.719203 + 3.903962 + 3.228919) / 4
claims.append(("Q8", c, "5.479201"))

# Q9: Omega_1 = 6.283185 * 98 * 10^6
c = 6.283185 * 98 * 10**6
claims.append(("Q9", c, "615752100"))

# Q10: Omega_2 = 6.283185 * 120 * 10^6
c = 6.283185 * 120 * 10**6
claims.append(("Q10", c, "753982200"))

# Q11: Omega_3 = 6.283185 * 132 * 10^6
c = 6.283185 * 132 * 10**6
claims.append(("Q11", c, "829380420"))

# Q12: Omega_4 = 6.283185 * 160 * 10^6
c = 6.283185 * 160 * 10**6
claims.append(("Q12", c, "1005309600"))

# Q13: mean Omega = (6.157521 + 7.539822 + 8.293804 + 10.053096) * 10^8 / 4
c = (6.157521 + 7.539822 + 8.293804 + 10.053096) * 10**8 / 4
claims.append(("Q13", c, "801106100"))

# Q14: Delta_1 = ln120 - ln98 = 4.787492 - 4.584967
c = 4.787492 - 4.584967
claims.append(("Q14", c, "0.202525"))

# Q15: Delta_2 = ln132 - ln120 = 4.882802 - 4.787492
c = 4.882802 - 4.787492
claims.append(("Q15", c, "0.095310"))

# Q16: Delta_3 = ln160 - ln132 = 5.075174 - 4.882802
c = 5.075174 - 4.882802
claims.append(("Q16", c, "0.192372"))

match_count = 0
for cid, computed, expected_str in claims:
    expected = float(expected_str)
    # match: computed rounded to the significant digits the paper states equals stated value
    # determine number of significant digits in expected string
    digits = len(expected_str.replace(".", "").replace("-", "").lstrip("0"))
    comp_rounded = sig(computed, digits)
    match = "yes" if abs(comp_rounded - expected) < 10 ** (-digits) * 0.5 * 10 ** max(1, math.floor(math.log10(abs(expected))) + 1 - digits) or comp_rounded == expected else "no"
    # simpler robust check: round computed to stated sig digits and compare as strings
    comp_r = sig(computed, digits)
    match = "yes" if f"{comp_r:.{digits}g}" == f"{expected:.{digits}g}" else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={fmt(computed)} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")
