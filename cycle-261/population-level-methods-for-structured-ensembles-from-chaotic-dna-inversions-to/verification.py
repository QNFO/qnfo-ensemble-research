import math
from fractions import Fraction

def round_to_str(x, s):
    """Round float x to the same number of decimal places as string s."""
    if '.' in s:
        dec = len(s.split('.')[1])
        return round(x, dec)
    return x

def compare(computed, expected_str):
    """Return (match, formatted_computed, expected)"""
    # Handle fraction expected
    if '/' in expected_str and not '.' in expected_str:
        exp_frac = Fraction(expected_str)
        match = Fraction(computed).limit_denominator() == exp_frac
        comp_str = f"{Fraction(computed).limit_denominator()}"
        exp_str = expected_str
        return match, comp_str, exp_str

    # Handle numeric expected
    try:
        exp_val = float(expected_str)
    except ValueError:
        # fallback for cases like "1/3"
        exp_val = None

    if exp_val is not None:
        rounded = round_to_str(computed, expected_str)
        # format with same decimal places
        if '.' in expected_str:
            dec = len(expected_str.split('.')[1])
            comp_str = f"{rounded:.{dec}f}"
            exp_str = f"{exp_val:.{dec}f}"
        else:
            comp_str = str(int(round(computed)))
            exp_str = str(int(exp_val))
        match = math.isclose(rounded, exp_val, rel_tol=1e-12, abs_tol=1e-12)
        return match, comp_str, exp_str
    else:
        # fallback
        return False, str(computed), expected_str

def claim_Q1():
    L = 10
    return L * (L + 1) // 2

def claim_Q2():
    L = 10
    total = sum(k * (L - k + 1) for k in range(1, L + 1))
    return total

def claim_Q3():
    S = 220
    segments = 55
    return S / segments

def claim_Q4():
    L = 10
    avg_len = 4.0
    return math.ceil(L / avg_len)

def claim_Q5():
    # (1/2) * integral_{-1}^{1} ω^2 dω
    # integral ω^2 from -1 to 1 = 2/3
    return Fraction(1, 2) * Fraction(2, 3)

def claim_Q6():
    t = 0.3
    U = t  # since u=+1
    return U**2 / 3

def claim_Q7():
    sigma2 = 0.03
    return math.sqrt(sigma2)

def claim_Q8():
    M1_target = 0.1
    rate = Fraction(1, 3)
    return M1_target / float(rate)

def claim_Q9():
    # (2/3) * integral_0^1 (ω^3 + ω^2) dω
    # integral ω^3 = 1/4, ω^2 = 1/3
    return Fraction(2, 3) * (Fraction(1, 4) + Fraction(1, 3))

def claim_Q10():
    M1_target = 0.1
    c2 = Fraction(7, 18)
    return M1_target / float(c2)

def claim_Q11():
    alpha = 0.7
    gamma = 4
    return (1 - alpha**(gamma + 1)) / (1 - alpha)

def claim_Q12():
    tokens = 2.7731
    gamma = 4
    cost = gamma * 1 + 1
    return tokens / cost

def claim_Q13():
    a1, a2, a3 = 0.5, 0.6, 0.7
    return 1 - (1 - a1)*(1 - a2)*(1 - a3)

def claim_Q14():
    alpha_eff = 0.94
    gamma = 4
    return (1 - alpha_eff**(gamma + 1)) / (1 - alpha_eff)

def claim_Q15():
    tokens = 4.43493296
    total_cost = 5
    return tokens / total_cost

def claim_Q16():
    ens = 0.886986592
    base = 0.55462
    return ens / base

claims = {
    "Q1": (claim_Q1, "55"),
    "Q2": (claim_Q2, "220"),
    "Q3": (claim_Q3, "4.0"),
    "Q4": (claim_Q4, "3"),
    "Q5": (claim_Q5, "1/3"),
    "Q6": (claim_Q6, "0.03"),
    "Q7": (claim_Q7, "0.1732"),
    "Q8": (claim_Q8, "0.3"),
    "Q9": (claim_Q9, "0.3889"),
    "Q10": (claim_Q10, "0.2571"),
    "Q11": (claim_Q11, "2.7731"),
    "Q12": (claim_Q12, "0.55462"),
    "Q13": (claim_Q13, "0.94"),
    "Q14": (claim_Q14, "4.43493296"),
    "Q15": (claim_Q15, "0.886986592"),
    "Q16": (claim_Q16, "1.5993"),
}

for cid, (func, expected) in claims.items():
    comp = func()
    match, comp_str, exp_str = compare(comp, expected)
    print(f"CLAIM {cid}: computed={comp_str} expected={exp_str} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,(_,e) in claims.items() if compare(_,e)[0] for _ in [])} match, {len(claims) - sum(1 for _,(_,e) in claims.items() if compare(_,e)[0] for _ in [])} mismatch")
