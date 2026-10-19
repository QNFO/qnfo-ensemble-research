# Verification script for quantitative claims in the paper
# Computes each claim from the stated inputs and compares to the expected values.

def fmt(x, sig):
    """Format number with given significant digits (or decimal places)."""
    return f"{x:.{sig}g}"

def round_to_places(x, places):
    """Round x to a given number of decimal places."""
    return round(x, places)

def main():
    # Inputs
    f1 = 0.9990
    f2 = 0.9956
    f3 = 0.9870
    lambda_C = 2.4263e-12
    target_ratio = 1e-6

    # Q1
    sum_f = f1 + f2 + f3
    exp_Q1 = "2.9816"
    match_Q1 = "yes" if abs(sum_f - 2.9816) < 1e-12 else "no"
    print(f"CLAIM Q1: computed={sum_f:.10f} expected={exp_Q1} match={match_Q1}")

    # Q2
    mean = sum_f / 3
    exp_Q2 = "0.993866666666667"
    # round to 15 decimal places to compare (as many as in expected)
    match_Q2 = "yes" if round(mean, 15) == 0.993866666666667 else "no"
    print(f"CLAIM Q2: computed={mean:.15f} expected={exp_Q2} match={match_Q2}")

    # Q3
    prod12 = f1 * f2
    exp_Q3 = "0.9946044"
    match_Q3 = "yes" if abs(prod12 - 0.9946044) < 1e-12 else "no"
    print(f"CLAIM Q3: computed={prod12:.7f} expected={exp_Q3} match={match_Q3}")

    # Q4
    F_prod = prod12 * f3
    exp_Q4 = "0.9816745428"
    match_Q4 = "yes" if abs(F_prod - 0.9816745428) < 1e-12 else "no"
    print(f"CLAIM Q4: computed={F_prod:.10f} expected={exp_Q4} match={match_Q4}")

    # Q5
    delta = mean - F_prod
    exp_Q5 = "0.0121921238"
    # statement has 10 decimal places; round computed to 10 places for comparison
    delta_rounded = round(delta, 10)
    match_Q5 = "yes" if delta_rounded == 0.0121921238 else "no"
    print(f"CLAIM Q5: computed={delta:.13f} expected={exp_Q5} match={match_Q5}")

    # Q6
    prod6 = 6 * 0.5 * (1/3)
    exp_Q6 = "1"
    match_Q6 = "yes" if abs(prod6 - 1) < 1e-12 else "no"
    print(f"CLAIM Q6: computed={prod6:.1f} expected={exp_Q6} match={match_Q6}")

    # Q7
    prod10 = 10 * 0.5 * 0.2
    exp_Q7 = "1"
    match_Q7 = "yes" if abs(prod10 - 1) < 1e-12 else "no"
    print(f"CLAIM Q7: computed={prod10:.1f} expected={exp_Q7} match={match_Q7}")

    # Q8
    prod12_abs = 12 * 0.25 * (1/3)
    exp_Q8 = "1"
    match_Q8 = "yes" if abs(prod12_abs - 1) < 1e-12 else "no"
    print(f"CLAIM Q8: computed={prod12_abs:.1f} expected={exp_Q8} match={match_Q8}")

    # Q9
    ell = lambda_C / target_ratio
    exp_Q9 = "2.4263e-06"
    match_Q9 = "yes" if abs(ell - 2.4263e-6) < 1e-12 else "no"
    print(f"CLAIM Q9: computed={ell:.10e} expected={exp_Q9} match={match_Q9}")

    # Q10
    percent_mean = mean * 100
    exp_Q10 = "99.3867%"
    # round to 4 decimal places as in statement
    percent_mean_rounded = round(percent_mean, 4)
    match_Q10 = "yes" if percent_mean_rounded == 99.3867 else "no"
    print(f"CLAIM Q10: computed={percent_mean_rounded:.4f}% expected={exp_Q10} match={match_Q10}")

    # Q11
    percent_F = F_prod * 100
    exp_Q11 = "98.16745428%"
    # round to 8 decimal places as in statement
    percent_F_rounded = round(percent_F, 8)
    match_Q11 = "yes" if percent_F_rounded == 98.16745428 else "no"
    print(f"CLAIM Q11: computed={percent_F_rounded:.8f}% expected={exp_Q11} match={match_Q11}")

    # Summary
    total = 11
    matches = sum(1 for m in [match_Q1, match_Q2, match_Q3, match_Q4, match_Q5,
                              match_Q6, match_Q7, match_Q8, match_Q9,
                              match_Q10, match_Q11] if m == "yes")
    mismatches = total - matches
    print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {mismatches} mismatch")

if __name__ == "__main__":
    main()
