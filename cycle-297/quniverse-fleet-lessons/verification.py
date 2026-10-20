import math

def fmt(val, digits):
    """Format a float with a given number of decimal places, removing trailing zeros."""
    fmt_str = f"{{:.{digits}f}}".format(val)
    # Remove trailing zeros and possible trailing decimal point
    if '.' in fmt_str:
        fmt_str = fmt_str.rstrip('0').rstrip('.')
    return fmt_str

# Claims definitions with inputs and expected values
claims = [
    {
        "id": "Q1",
        "statement": "Effective unresolved‑failure probability $p_{\\text{eff}} = 0.06$.",
        "compute": lambda: 0.12 * (1 - 0.5),
        "expected": "0.06",
        "digits": 2
    },
    {
        "id": "Q2",
        "statement": "Expected monthly unresolved failures $E[F] = 2.16$.",
        "compute": lambda: 36 * 0.12 * (1 - 0.5),
        "expected": "2.16",
        "digits": 2
    },
    {
        "id": "Q3",
        "statement": "Count‑derived mitigation factor $\\alpha_{\\text{counts}} \\approx 0.599$.",
        "compute": lambda: 1889 / (1889 + 1264),
        "expected": "0.599",
        "digits": 3
    },
    {
        "id": "Q4",
        "statement": "Effective failure probability using $\\alpha_{\\text{counts}}$ is $p_{\\text{eff}}^{\\text{counts}} = 0.04812$.",
        "compute": lambda: 0.12 * (1 - (1889 / (1889 + 1264))),
        "expected": "0.04812",
        "digits": 5
    },
    {
        "id": "Q5",
        "statement": "Expected failures using $\\alpha_{\\text{counts}}$ is $E[F]^{\\text{counts}} \\approx 1.73$.",
        "compute": lambda: 36 * (0.12 * (1 - (1889 / (1889 + 1264)))),
        "expected": "1.73",
        "digits": 2
    },
    {
        "id": "Q6",
        "statement": "Variance of the failure count $\\operatorname{Var}[F] = 2.0304$.",
        "compute": lambda: 36 * 0.06 * (1 - 0.06),
        "expected": "2.0304",
        "digits": 4
    },
    {
        "id": "Q7",
        "statement": "Standard deviation $\\sigma_F \\approx 1.425$.",
        "compute": lambda: math.sqrt(36 * 0.06 * (1 - 0.06)),
        "expected": "1.425",
        "digits": 3
    },
    {
        "id": "Q8",
        "statement": "Papers per active project $= 9.65$.",
        "compute": lambda: 917 / 95,
        "expected": "9.65",
        "digits": 2
    },
    {
        "id": "Q9",
        "statement": "High‑severity gap proportion $= 11.9\\%$.",
        "compute": lambda: (5 / 42) * 100,
        "expected": "11.9",
        "digits": 1
    },
    {
        "id": "Q10",
        "statement": "Vector‑index size $S_{vi} \\approx 16.922\\ \\text{MiB}$.",
        "compute": lambda: (34657 * 512) / 1048576,
        "expected": "16.922",
        "digits": 3
    },
    {
        "id": "Q11",
        "statement": "Total storage $S_{\\text{tot}} \\approx 320.9\\ \\text{MB}$.",
        "compute": lambda: 304 + ((34657 * 512) / 1048576),
        "expected": "320.9",
        "digits": 1
    },
    {
        "id": "Q12",
        "statement": "Baseline composite autonomy score $C_{\\text{base}} = 4.26$.",
        "compute": lambda: 0.4*4.5 + 0.3*4.0 + 0.3*4.2,
        "expected": "4.26",
        "digits": 2
    },
    {
        "id": "Q13",
        "statement": "Improved composite autonomy score $C_{\\text{new}} = 4.66$.",
        "compute": lambda: 0.4*4.9 + 0.3*4.4 + 0.3*4.6,
        "expected": "4.66",
        "digits": 2
    },
    {
        "id": "Q14",
        "statement": "Score increment $= 0.40$.",
        "compute": lambda: (0.4*4.9 + 0.3*4.4 + 0.3*4.6) - (0.4*4.5 + 0.3*4.0 + 0.3*4.2),
        "expected": "0.40",
        "digits": 2
    },
    {
        "id": "Q15",
        "statement": "Baseline extra cost $= \\$10.8$.",
        "compute": lambda: 2.16 * 5,
        "expected": "10.8",
        "digits": 1
    },
    {
        "id": "Q16",
        "statement": "Projected baseline spend $= \\$160.8$.",
        "compute": lambda: 150 + (2.16 * 5),
        "expected": "160.8",
        "digits": 1
    }
]

for c in claims:
    computed = c["compute"]()
    # Round/format to the required number of significant digits as per expected string
    formatted = fmt(computed, c["digits"])
    match = "yes" if formatted == c["expected"] else "no"
    print(f"CLAIM {c['id']}: computed={formatted} expected={c['expected']} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for c in claims if fmt(c['compute'](), c['digits']) == c['expected'])} match, {sum(1 for c in claims if fmt(c['compute'](), c['digits']) != c['expected'])} mismatch")
