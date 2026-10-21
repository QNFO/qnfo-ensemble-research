import math

def compute_Q1():
    p, t = 3, 1
    n = 1 + (p + 1) * (p**t - 1) // (p - 1) if (p**t - 1) % (p - 1) == 0 else 1 + (p + 1) * (p**t - 1) / (p - 1)
    return n

def compute_Q2():
    p, t = 3, 2
    n = 1 + (p + 1) * (p**t - 1) / (p - 1)
    return n

def compute_Q3():
    t = 1
    d = 2 * t + 1
    return d

def compute_Q4():
    t = 2
    d = 2 * t + 1
    return d

def compute_Q5():
    p, t, eps = 3, 1, 1e-3
    total = 0.0
    for k in range(t + 1, p + 2):  # inclusive upper bound p+1
        total += math.comb(p + 1, k) * (eps ** k) * ((1 - eps) ** (p + 1 - k))
    return total

def compute_Q6(P_pass):
    eps = 1e-3
    return eps / P_pass

def compute_Q7():
    p, t, eps = 3, 2, 1e-3
    total = 0.0
    for k in range(t + 1, p + 2):
        total += math.comb(p + 1, k) * (eps ** k) * ((1 - eps) ** (p + 1 - k))
    return total

def compute_Q8():
    d = 3
    return 2 ** d

def compute_Q9():
    d = 5
    return 2 ** d

def compute_Q10():
    cost_tweezer = 0.10
    cost_laser = 0.05
    n = 5
    return n * (cost_tweezer + cost_laser)

# Compute all claims
results = {
    "Q1": compute_Q1(),
    "Q2": compute_Q2(),
    "Q3": compute_Q3(),
    "Q4": compute_Q4(),
    "Q5": compute_Q5(),
    "Q6": compute_Q6(compute_Q5()),
    "Q7": compute_Q7(),
    "Q8": compute_Q8(),
    "Q9": compute_Q9(),
    "Q10": compute_Q10(),
}

expected = {
    "Q1": "5",
    "Q2": "17",
    "Q3": "3",
    "Q4": "5",
    "Q5": "5.992003e-6",
    "Q6": "166.9",
    "Q7": "3.997e-9",
    "Q8": "8",
    "Q9": "32",
    "Q10": "0.75",
}

def match(val, exp):
    # compare after rounding to the number of significant digits in exp
    # count digits before 'e' or decimal point
    if 'e' in exp:
        # scientific notation: keep same number of mantissa digits
        mantissa, exponent = exp.split('e')
        sig_digits = len(mantissa.replace('.', '').replace('-', ''))
        fmt = f"{{:.{sig_digits-1}e}}"
        return fmt.format(val) == exp
    else:
        # plain number: compare as float with tolerance based on length
        try:
            exp_val = float(exp)
            return abs(val - exp_val) <= 1e-12 * max(1.0, abs(exp_val))
        except:
            return False

# Print results
for qid in sorted(results.keys()):
    comp = results[qid]
    exp = expected[qid]
    m = "yes" if match(comp, exp) else "no"
    # format computed with at least 8 significant digits
    if isinstance(comp, float):
        comp_str = f"{comp:.8g}"
    else:
        comp_str = str(comp)
    print(f"CLAIM {qid}: computed={comp_str} expected={exp} match={m}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(1 for q in results if match(results[q], expected[q]))} match, {sum(1 for q in results if not match(results[q], expected[q]))} mismatch")
