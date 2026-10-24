import math

def format_sig(x, sig):
    """Round x to sig significant figures and return as string in scientific notation."""
    if x == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(x))))
    factor = round(x / (10**exponent), sig)
    # Adjust if rounding pushes factor to 10
    if factor >= 10:
        factor /= 10
        exponent += 1
    return f"{factor:.{sig-1}f}e{exponent:+d}"

def main():
    # Claim Q1
    N_spins = 10**3
    C = 2**N_spins
    expected_Q1 = "1.07e+301"
    computed_Q1 = format_sig(C, 3)
    match_Q1 = "yes" if computed_Q1 == expected_Q1 else "no"
    print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={match_Q1}")

    # Claim Q2
    lower = 0.10
    upper = 0.20
    r_bar = (lower + upper) / 2
    expected_Q2 = "0.15"
    computed_Q2 = f"{r_bar:.2f}"
    match_Q2 = "yes" if computed_Q2 == expected_Q2 else "no"
    print(f"CLAIM Q2: computed={computed_Q2} expected={expected_Q2} match={match_Q2}")

    # Claim Q3
    configs_Q3 = 2**20          # ≈ 1.05×10⁶
    ops_per_sec = 10**9
    time_Q3 = configs_Q3 / ops_per_sec
    expected_Q3 = "0.001"
    computed_Q3 = f"{time_Q3:.3f}"
    match_Q3 = "yes" if computed_Q3 == expected_Q3 else "no"
    print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={match_Q3}")

    # Claim Q4
    configs_Q4 = 2**30          # ≈ 1.07×10⁹
    time_Q4 = configs_Q4 / ops_per_sec
    expected_Q4 = "1"
    computed_Q4 = f"{round(time_Q4):.0f}"
    match_Q4 = "yes" if computed_Q4 == expected_Q4 else "no"
    print(f"CLAIM Q4: computed={computed_Q4} expected={expected_Q4} match={match_Q4}")

    print("VERIFICATION SUMMARY: 4 claims, "
          f"{sum([match_Q1, match_Q2, match_Q3, match_Q4].count('yes'))} match, "
          f"{sum([match_Q1, match_Q2, match_Q3, match_Q4].count('no'))} mismatch")

if __name__ == "__main__":
    main()
