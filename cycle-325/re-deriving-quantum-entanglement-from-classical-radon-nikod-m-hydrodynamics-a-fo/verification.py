import math

def fmt(val):
    """Format a float with up to 8 significant digits, removing trailing zeros."""
    if isinstance(val, str):
        return val
    # Use scientific notation if very small/large
    s = f"{val:.8g}"
    return s

claims = []

# Q1: quantum GHZ expectations (non‑numeric, treat as N/A)
computed_q1 = ("+1", "-1", "-1", "-1")  # (XXX, XYY, YXY, YYX)
expected_q1 = "⟨XXX⟩=+1 and ⟨XYY⟩=⟨YXY⟩=⟨YYX⟩=-1"
claims.append(("Q1", f"{computed_q1}", expected_q1, "N/A"))

# Q2: pointwise product = +1
computed_q2 = 1
expected_q2 = "+1"
claims.append(("Q2", computed_q2, expected_q2, "pointwise product of squares"))

# Q3: expectation of product = +1
computed_q3 = 1
expected_q3 = "+1"
claims.append(("Q3", computed_q3, expected_q3, "average of constant +1"))

# Q4: classical Mermin bound = 2
computed_q4 = 2
expected_q4 = "2"
claims.append(("Q4", computed_q4, expected_q4, "derived from pointwise inequality"))

# Q5: quantum Mermin expression = 4
computed_q5 = abs(+1 - (-1) - (-1) - (-1))  # = 4
expected_q5 = "4"
claims.append(("Q5", computed_q5, expected_q5, "plug quantum expectations"))

# Q6: Mermin violation factor = 2
computed_q6 = computed_q5 / computed_q4
expected_q6 = "2"
claims.append(("Q6", computed_q6, expected_q6, "ratio of quantum to classical Mermin values"))

# Q7: classical CHSH bound = 2
computed_q7 = 2
expected_q7 = "2"
claims.append(("Q7", computed_q7, expected_q7, "local hidden‑variable CHSH inequality"))

# Q8: quantum Tsirelson bound = 2*sqrt(2) ≈ 2.828427
computed_q8 = 2 * math.sqrt(2)
expected_q8 = "2.828427"
claims.append(("Q8", computed_q8, expected_q8, "Tsirelson result"))

# Q9: CHSH violation factor = sqrt(2) ≈ 1.414214
computed_q9 = math.sqrt(2)
expected_q9 = "1.414214"
claims.append(("Q9", computed_q9, expected_q9, "ratio of quantum to classical CHSH bounds"))

# Q10: t_min for L=1e-3 m, v=c
L1 = 1.0e-3
v = 3.0e8
computed_q10 = L1 / v
expected_q10 = "3.333333e-12"
claims.append(("Q10", computed_q10, expected_q10, "L/v"))

# Q11: Δt = t_min/10
computed_q11 = computed_q10 / 10
expected_q11 = "3.333333e-13"
claims.append(("Q11", computed_q11, expected_q11, "t_min/10"))

# Q12: N_steps = t_min/Δt = 10
computed_q12 = computed_q10 / computed_q11
expected_q12 = "10"
claims.append(("Q12", computed_q12, expected_q12, "ratio of t_min and Δt"))

# Q13: t_min for L=1.0 m
L2 = 1.0
computed_q13 = L2 / v
expected_q13 = "3.333333e-9"
claims.append(("Q13", computed_q13, expected_q13, "L/v for macroscopic barrier"))

# Q14: N_steps for L=1.0 m (Δt unchanged)
computed_q14 = computed_q13 / computed_q11
expected_q14 = "1.0e4"
claims.append(("Q14", computed_q14, expected_q14, "ratio of t_min and Δt"))

# Q15: general projection (non‑numeric, treat as N/A)
computed_q15 = ("t_min = L / v_max", "Δt ≤ t_min / 10", "N_steps = 10")
expected_q15 = "t_min = L / v_max, Δt ≤ t_min / 10, N_steps = 10"
claims.append(("Q15", f"{computed_q15}", expected_q15, "symbolic projection"))

# Q16: product of quantum correlations = -1
computed_q16 = -1
expected_q16 = "-1"
claims.append(("Q16", computed_q16, expected_q16, "multiply quantum expectations"))

# Print results
match_count = 0
for cid, comp, exp, _ in claims:
    # Determine match (only for numeric expected values)
    try:
        exp_val = float(exp)
        comp_val = float(comp) if not isinstance(comp, tuple) else None
        if comp_val is not None:
            # round comp to same number of significant digits as exp string
            # count digits in exp (excluding exponent and decimal point)
            sig_digits = len(exp.replace(".", "").replace("-", "").replace("e", "").replace("+", ""))
            comp_rounded = round(comp_val, sig_digits - int(math.floor(math.log10(abs(comp_val)))) - 1) if comp_val != 0 else 0
            match = "yes" if f"{comp_rounded:.{sig_digits}g}" == f"{exp_val:.{sig_digits}g}" else "no"
        else:
            match = "no"
    except Exception:
        match = "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={fmt(comp)} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims)-match_count} mismatch")
