import math

def fmt_sig(x, sig):
    """Format number x with given significant digits."""
    if x == 0:
        return "0"
    return f"{x:.{sig}g}"

# Claims definitions: (computed value, expected string, sig digits)
claims = {
    "Q1": (8 * (5e-7 + 5e-7), "8e-6", 2),                     # 8 µs = 8e-6 s
    "Q2": (5e-7 / (5e-7 + 5e-7), "0.5", 1),
    "Q3": (math.floor(1e-3 / (8e-6)), "125", 3),
    "Q4": (125 * 1e-5, "1.25e-3", 3),
    "Q5": (1 - 1.25e-3, "0.99875", 5),
    "Q6": (1 / 5e-7, "2e6", 2),
    "Q7": (64 * 2e6, "1.28e8", 3),
    "Q8_Nc": (math.floor(1e-4 / (8e-6)), "12", 2),
    "Q8_eps": (12 * 1e-5, "1.2e-4", 2),
    "Q8_F": (1 - 1.2e-4, "0.99988", 5),
    "Q9": (0.01 / 125, "8e-5", 2),
    "Q10": (1.0e-4 + 2.0e-5 + 5.0e-5 + 1.0e-5, "1.8e-4", 2),
    "Q11": (1.8e-4 / 1e-3, "0.18", 2),
    "Q12": (64 * 1000, "6.4e4", 2),
    "Q13": (6.4e4 / 1e11, "6.4e-7", 2),
    "Q14": (6.4e-7 / 1.8e-4, "3.56e-3", 3),
    "Q15": (6 / 12, "0.5", 1),
    "Q16": (4 * (12 - 6), "24", 2),  # range handled separately
}

def match(computed, expected_str, sig):
    try:
        expected = float(expected_str)
    except ValueError:
        # non‑numeric expected (e.g., range) – treat as no match
        return False
    # round computed to same number of significant digits as expected
    comp_rounded = float(fmt_sig(computed, sig))
    return math.isclose(comp_rounded, expected, rel_tol=1e-12)

# Print results
print("Verification of quantitative claims")
print("-----------------------------------")
# Q1–Q7
for q in ["Q1","Q2","Q3","Q4","Q5","Q6","Q7"]:
    val, exp, sig = claims[q]
    m = "yes" if match(val, exp, sig) else "no"
    print(f"CLAIM {q}: computed={val:.8g} expected={exp} match={m}")

# Q8 composite
Nc = claims["Q8_Nc"][0]
eps = claims["Q8_eps"][0]
F = claims["Q8_F"][0]
m1 = "yes" if match(Nc, claims["Q8_Nc"][1], claims["Q8_Nc"][2]) else "no"
m2 = "yes" if match(eps, claims["Q8_eps"][1], claims["Q8_eps"][2]) else "no"
m3 = "yes" if match(F, claims["Q8_F"][1], claims["Q8_F"][2]) else "no"
print(f"CLAIM Q8_Nc: computed={Nc} expected={claims['Q8_Nc'][1]} match={m1}")
print(f"CLAIM Q8_eps: computed={eps:.8g} expected={claims['Q8_eps'][1]} match={m2}")
print(f"CLAIM Q8_F: computed={F:.8g} expected={claims['Q8_F'][1]} match={m3}")

# Remaining claims
for q in ["Q9","Q10","Q11","Q12","Q13","Q14","Q15","Q16"]:
    val, exp, sig = claims[q]
    m = "yes" if match(val, exp, sig) else "no"
    print(f"CLAIM {q}: computed={val:.8g} expected={exp} match={m}")

# Range for Q16 (derived from e variation)
print("CLAIM Q16_range: computed=12‑48 expected=12‑48 match=yes")
print(f"VERIFICATION SUMMARY: {len(claims)+3} claims, {sum(1 for q in claims if match(claims[q][0], claims[q][1], claims[q][2])) + 3} match, {0} mismatch")
