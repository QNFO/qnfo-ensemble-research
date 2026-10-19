import math

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    else:
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Expected values and their formatting (decimal places)
expected = {
    "Q1": ("720", 0),
    "Q2": ("9.49", 2),
    "Q3": ("500", 0),
    "Q4": ("8.97", 2),
    "Q5": ("26.91", 2),
    "Q6": ("36.40", 2),
    "Q7": ("30", 0),
    "Q8": ("36.40", 2),
    "Q9": ("156.6", 1),
    "Q10": ("23.30", 2),
    "Q11": ("138.0", 1),
    "Q12": ("18.6", 1),
    "Q13": ("0.62", 2),
    "Q14": ("29.48", 2),
    "Q15": ("23.30", 2),
    "Q16": ("6.18", 2),
}

# 1. Orientation bins
N_theta = 360 / 0.5  # Q1
# 2. Orientation info
I_theta = math.log2(N_theta)  # Q2
# 3. Position bins per dimension
L = 10.0
delta_p = 0.02
N_p = L / delta_p  # Q3
# 4. Bits per dimension
bits_per_dim = math.log2(N_p)  # Q4
# 5. Total position info
I_p = 3 * bits_per_dim  # Q5
# 6. Raw per-sample info
I_raw = I_theta + I_p  # Q6
# 7. Bandwidth
B = 30  # Q7
# 8. Raw SNR (noise power = 1)
SNR0 = I_raw / 1.0  # Q8
# 9. Capacity without filtering
C1 = B * math.log2(1 + SNR0)  # Q9
# 10. Filtered SNR with alpha=0.8
alpha = 0.8
SNR_alpha = alpha**2 * SNR0  # Q10
# 11. Capacity with alpha=0.8
C0_8 = B * math.log2(1 + SNR_alpha)  # Q11
# 12. Capacity drop
delta_C = C1 - C0_8  # Q12
# 13. Per-sample capacity change
delta_C_per_sample = delta_C / B  # Q13
# 14. Information budget with alpha=0.9
I_09 = 0.9**2 * I_raw  # Q14
# 15. Information budget with alpha=0.8
I_08 = 0.8**2 * I_raw  # Q15
# 16. Difference between the two budgets
delta_I = I_09 - I_08  # Q16

# Mapping of computed values to claim IDs
computed = {
    "Q1": N_theta,
    "Q2": I_theta,
    "Q3": N_p,
    "Q4": bits_per_dim,
    "Q5": I_p,
    "Q6": I_raw,
    "Q7": B,
    "Q8": SNR0,
    "Q9": C1,
    "Q10": SNR_alpha,
    "Q11": C0_8,
    "Q12": delta_C,
    "Q13": delta_C_per_sample,
    "Q14": I_09,
    "Q15": I_08,
    "Q16": delta_I,
}

# Helper to format rounded value with required decimal places
def fmt(val, dec):
    fmt_str = f"{{:.{dec}f}}"
    return fmt_str.format(val)

# Verification loop
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):  # Q1, Q2, ...
    exp_str, dec = expected[qid]
    # Determine sig figs from expected string (ignoring leading zeros and decimal point)
    # For simplicity we use the decimal places already stored.
    comp_raw = computed[qid]
    # Round to the same number of significant figures as the expected value
    # Count significant figures: digits excluding leading zeros and decimal point.
    # Here we approximate by rounding to the same number of decimal places.
    comp_rounded = round(comp_raw, dec)
    comp_str = fmt(comp_rounded, dec)
    match = "yes" if comp_str == exp_str else "no"
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if fmt(round(computed[q], expected[q][1]), expected[q][1]) == expected[q][0])} match, {len(expected) - sum(1 for q in expected if fmt(round(computed[q], expected[q][1]), expected[q][1]) == expected[q][0])} mismatch")
