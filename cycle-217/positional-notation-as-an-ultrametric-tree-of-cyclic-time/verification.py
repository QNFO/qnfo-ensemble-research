import math

def round_to_str(value, target_str):
    """Round value to the same number of decimal places as target_str."""
    if 'e' in target_str or 'E' in target_str:
        # scientific notation like 1.2096e5
        # Determine number of significant digits from mantissa
        mantissa = target_str.split('e')[0]
        sig_digits = len(mantissa.replace('.', '').replace('-', ''))
        rounded = round(value, sig_digits - int(math.floor(math.log10(abs(value)))) - 1)
        return f"{rounded:.{sig_digits}g}"
    if '.' in target_str:
        decimals = len(target_str.split('.')[1])
        rounded = round(value, decimals)
        fmt = f"{{:.{decimals}f}}"
        return fmt.format(rounded)
    else:
        # integer
        return str(int(round(value)))

def compare(value, target_str):
    rounded_str = round_to_str(value, target_str)
    return rounded_str == target_str, rounded_str

def main():
    claims = []

    # Q1
    b = 60
    d = b ** -1
    exp = "0.0166667"
    ok, comp = compare(d, exp)
    claims.append(("Q1", comp, exp, ok))

    # Q2
    b = 20
    d = b ** -1
    exp = "0.05"
    ok, comp = compare(d, exp)
    claims.append(("Q2", comp, exp, ok))

    # Q3
    N_R = 60 * 60 * 24 * 7
    exp = "604800"
    ok, comp = compare(N_R, exp)
    claims.append(("Q3", comp, exp, ok))

    # Q4
    log2_N = 7 + 3*math.log2(3) + 2*math.log2(5) + math.log2(7)
    exp = "19.2061"
    ok, comp = compare(log2_N, exp)
    claims.append(("Q4", comp, exp, ok))

    # Q5
    lamb = 2
    distances = [lamb**-ell for ell in range(0,5)]
    # Expected set as strings
    exp_set = {"0.0625","0.125","0.25","0.5","1"}
    comp_set = {round_to_str(d, s) for d,s in zip(distances, exp_set)}
    ok = comp_set == exp_set
    claims.append(("Q5", str(sorted(comp_set)), str(sorted(exp_set)), ok))

    # Q6
    ratio = (604800 - 1) / 5
    exp = "1.2096e5"
    ok, comp = compare(ratio, exp)
    claims.append(("Q6", comp, exp, ok))

    # Q7
    prob = 1/60
    exp = "0.0166667"
    ok, comp = compare(prob, exp)
    claims.append(("Q7", comp, exp, ok))

    # Q8
    prob = 1/(60*60)
    exp = "0.000277778"
    ok, comp = compare(prob, exp)
    claims.append(("Q8", comp, exp, ok))

    # Q9
    prob = 1/(60*60*24)
    exp = "0.0000115741"
    ok, comp = compare(prob, exp)
    claims.append(("Q9", comp, exp, ok))

    # Q10
    prob = 1/604800
    exp = "0.00000165344"
    ok, comp = compare(prob, exp)
    claims.append(("Q10", comp, exp, ok))

    # Q11
    prob = 1 - 1/60
    exp = "0.983333"
    ok, comp = compare(prob, exp)
    claims.append(("Q11", comp, exp, ok))

    # Q12
    prob = 1/60 - 1/(60*60)
    exp = "0.0163889"
    ok, comp = compare(prob, exp)
    claims.append(("Q12", comp, exp, ok))

    # Q13
    prob = 1/(60*60) - 1/(60*60*24)
    exp = "0.000266204"
    ok, comp = compare(prob, exp)
    claims.append(("Q13", comp, exp, ok))

    # Q14
    prob = 1/(60*60*24) - 1/604800
    exp = "0.00000992063"
    ok, comp = compare(prob, exp)
    claims.append(("Q14", comp, exp, ok))

    # Q15
    prob = 1/604800
    exp = "0.00000165344"
    ok, comp = compare(prob, exp)
    claims.append(("Q15", comp, exp, ok))

    # Q16
    H = math.log2(60)
    exp = "5.906891"
    ok, comp = compare(H, exp)
    claims.append(("Q16", comp, exp, ok))

    for cid, comp, exp, ok in claims:
        print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if ok else 'no'}")

if __name__ == "__main__":
    main()
