import math

def decimal_places(s):
    """Return number of decimal places in a numeric string like '0.1905' or '0.10'."""
    if 'e' in s or 'E' in s:
        # scientific notation, count digits after decimal in mantissa
        mantissa = s.split('e')[0]
        if '.' in mantissa:
            return len(mantissa.split('.')[1])
        else:
            return 0
    if '.' in s:
        return len(s.split('.')[1])
    return 0

def format_match(computed, expected):
    """Round computed to the same decimal precision as expected and format."""
    dp = decimal_places(expected)
    if dp > 0:
        fmt = f"{{:.{dp}f}}"
        comp_str = fmt.format(computed)
    else:
        # integer or scientific mantissa without decimal
        comp_str = f"{computed:.0f}"
    # handle scientific notation expected
    if 'e' in expected or 'E' in expected:
        comp_str = f"{float(comp_str):.1e}" if '.' in expected else f"{float(comp_str):.0e}"
    return comp_str

def main():
    claims = [
        # Q1
        ("Q1", 0.30 + 0.25 + 0.20 + 0.15 + 0.10, "1.00"),
        # Q2
        ("Q2", 42 / 5, "8.4"),
        # Q3
        ("Q3", 8 / (5 - 1), "2.0"),
        # Q4
        ("Q4", 5 / 8, "0.625"),
        # Q5
        ("Q5", 8 / 42, "0.1905"),
        # Q6
        ("Q6", (8 / 42) * 7, "1.333"),
        # Q7
        ("Q7", 3.0e13 / 200, "1.5e11"),
        # Q8
        ("Q8", (3.0e13 * 1) / 1e12, "30"),
        # Q9
        ("Q9", (3.0e13 * 4) / 1e12, "120"),
        # Q10
        ("Q10", (1.2e14 * 1.25) / 1e12, "150"),
        # Q11
        ("Q11", 20 * 19 / 2, "190"),
        # Q12
        ("Q12", 190 * (1 - 0.9), "19"),
        # Q13
        ("Q13", 0.30*1 + 0.25*0.5 + 0.20*1 + 0.15*0 + 0.10*0.5, "0.675"),
        # Q14
        ("Q14", 0.30*0 + 0.25*0 + 0.20*0.5 + 0.15*0 + 0.10*0, "0.10"),
        # Q15
        ("Q15", 1.00 - 0.30, "0.70"),
        # Q16
        ("Q16", 10 * 5, "50")
    ]

    for cid, comp, expected in claims:
        comp_str = format_match(comp, expected)
        match = "yes" if comp_str == expected else "no"
        print(f"CLAIM {cid}: computed={comp_str} expected={expected} match={match}")

    print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
          f"{sum(1 for _,c,e in claims if format_match(c,e)==e)} match, "
          f"{sum(1 for _,c,e in claims if format_match(c,e)!=e)} mismatch")

if __name__ == "__main__":
    main()
