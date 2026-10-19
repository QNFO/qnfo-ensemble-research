import math

def round_to_str(value, expected):
    """Round value to the same number of decimal places as expected string."""
    if '.' in expected:
        dp = len(expected.split('.')[1])
        rounded = round(value, dp)
        return f"{rounded:.{dp}f}"
    else:
        # integer expected
        return str(int(round(value)))

def check_claim(claim_id, computed, expected):
    comp_str = round_to_str(computed, expected)
    match = "yes" if comp_str == expected else "no"
    print(f"CLAIM {claim_id}: computed={comp_str} expected={expected} match={match}")
    return match == "yes"

def main():
    matches = 0
    total = 0

    # Q1
    total += 1
    computed = math.sqrt(2)
    expected = "1.41421356"
    if check_claim("Q1", computed, expected):
        matches += 1

    # Q2
    total += 1
    sqrt2 = 1.41421356  # input value
    d = 1
    computed = sqrt2 * d
    expected = "1.41421356"
    if check_claim("Q2", computed, expected):
        matches += 1

    # Q3
    total += 1
    d = 2
    computed = sqrt2 * d
    expected = "2.82842712"
    if check_claim("Q3", computed, expected):
        matches += 1

    # Q4
    total += 1
    d = 3
    computed = sqrt2 * d
    expected = "4.24264068"
    if check_claim("Q4", computed, expected):
        matches += 1

    # Q5
    total += 1
    C0 = 1
    computed = C0 * C0
    expected = "1"
    if check_claim("Q5", computed, expected):
        matches += 1

    # Q6
    total += 1
    C1 = 1
    computed = C0 * C1 + C1 * C0
    expected = "2"
    if check_claim("Q6", computed, expected):
        matches += 1

    # Q7
    total += 1
    C2 = 2
    computed = C0 * C2 + C1 * C1 + C2 * C0
    expected = "5"
    if check_claim("Q7", computed, expected):
        matches += 1

    # Q8
    total += 1
    N0, N1, N2, N3 = 1, 1, 2, 5
    computed = N0 + N1 + N2 + N3
    expected = "9"
    if check_claim("Q8", computed, expected):
        matches += 1

    # Q9
    total += 1
    d = 5
    computed = sqrt2 * d
    expected = "7.07106781"
    if check_claim("Q9", computed, expected):
        matches += 1

    print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {total - matches} mismatch")

if __name__ == "__main__":
    main()
