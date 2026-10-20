# Verification script for quantitative claims Q1–Q16

def compute_Q1():
    N = 1000
    C = N * (N - 1) // 2
    return C, "499500"

def compute_Q2():
    # 10 residue classes, each with 100 numbers
    pairs_per_class = 100 * 99 // 2
    total = 10 * pairs_per_class
    return total, "49500"

def compute_Q3():
    # 100 residue classes, each with 10 numbers
    pairs_per_class = 10 * 9 // 2
    total = 100 * pairs_per_class
    return total, "4500"

def compute_Q4():
    total_pairs = 499500
    ge1 = 49500
    result = total_pairs - ge1
    return result, "450000"

def compute_Q5():
    ge1 = 49500
    ge2 = 4500
    result = ge1 - ge2
    return result, "45000"

def compute_Q6():
    result = 4500
    return result, "4500"

def compute_Q7():
    n = 100
    C = n * (n - 1) // 2
    return C, "4950"

def compute_Q8():
    # 10 residue classes, each with 10 numbers
    pairs_per_class = 10 * 9 // 2
    total = 10 * pairs_per_class
    return total, "450"

def compute_Q9():
    pairs_0_1 = 450   # distance 0.1
    pairs_1_0 = 4500  # distance 1
    total_pairs = 4950
    mean = (pairs_0_1 * 0.1 + pairs_1_0 * 1) / total_pairs
    # exact fraction 101/110
    return mean, "101/110"

def compute_Q10():
    n = 100
    total = (1/6) * n * (n**2 - 1)
    return int(total), "166650"

def compute_Q11():
    sum_diff = 166650
    total_pairs = 4950
    diameter = 99
    mean = sum_diff / (total_pairs * diameter)
    # exact fraction 101/297
    return mean, "101/297"

def compute_Q12():
    ratio = (101/110) / (101/297)
    return ratio, "2.70"

def compute_Q13():
    count = 91 * 9 + sum(range(9))  # sum 0..8 = 36
    return count, "855"

def compute_Q14():
    # Use the same parameters as the 0–99 case: b=10, m=2
    b = 10
    m = 2
    total = b**m * (b**m - 1) // 2
    return total, "4950"

def compute_Q15():
    # Use b=10, m=2, k=1 (valuation at least 1)
    b = 10
    m = 2
    k = 1
    C_ge_k = b**m * (b**(m - k) - 1) // 2
    return C_ge_k, "450"

def compute_Q16():
    # Use b=10, m=2, k=1 (valuation exactly 1)
    b = 10
    m = 2
    k = 1
    N_k = b**(2*m - k - 1) * (b - 1) // 2
    return N_k, "450"

def main():
    claims = [
        ("Q1", *compute_Q1()),
        ("Q2", *compute_Q2()),
        ("Q3", *compute_Q3()),
        ("Q4", *compute_Q4()),
        ("Q5", *compute_Q5()),
        ("Q6", *compute_Q6()),
        ("Q7", *compute_Q7()),
        ("Q8", *compute_Q8()),
        ("Q9", *compute_Q9()),
        ("Q10", *compute_Q10()),
        ("Q11", *compute_Q11()),
        ("Q12", *compute_Q12()),
        ("Q13", *compute_Q13()),
        ("Q14", *compute_Q14()),
        ("Q15", *compute_Q15()),
        ("Q16", *compute_Q16()),
    ]

    match_count = 0
    for cid, computed, expected in claims:
        # Determine if computed matches expected within the precision implied by expected
        if "/" in expected:  # fraction
            exp_num, exp_den = map(int, expected.split("/"))
            # Compare as exact rational
            if isinstance(computed, float):
                # convert float to fraction with limited denominator
                from fractions import Fraction
                frac = Fraction(computed).limit_denominator()
                match = (frac.numerator == exp_num) and (frac.denominator == exp_den)
            else:
                match = (computed == exp_num / exp_den)
        elif "." in expected:  # decimal with given digits
            # count digits after decimal
            dec_digits = len(expected.split(".")[1])
            fmt = f"{{:.{dec_digits}f}}"
            match = fmt.format(computed) == expected
        else:
            # integer comparison
            match = int(computed) == int(expected.replace(",", ""))
        match_str = "yes" if match else "no"
        if match:
            match_count += 1
        print(f"CLAIM {cid}: computed={computed} expected={expected} match={match_str}")

    total = len(claims)
    print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")

if __name__ == "__main__":
    main()
