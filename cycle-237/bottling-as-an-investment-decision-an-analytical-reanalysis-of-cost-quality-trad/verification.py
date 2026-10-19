import math

def binom_tail(N, p, k_min):
    total = 0.0
    for k in range(k_min, N+1):
        total += math.comb(N, k) * (p**k) * ((1-p)**(N-k))
    return total

def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def two_sided_p(z):
    return 2 * (1 - phi(abs(z)))

def wald_ci(x, N):
    phat = x / N
    se = math.sqrt(phat * (1 - phat) / N)
    lo = phat - 1.96 * se
    hi = phat + 1.96 * se
    return lo, hi

claims = {
    "Q1": {
        "computed": binom_tail(60, 0.025, 48),
        "expected": 1.3e-65,
    },
    "Q2": {
        "computed": (48 - 1.5) / math.sqrt(60 * 0.025 * 0.975),
        "expected": 38.45,
    },
    "Q3": {
        "computed": (48 - 3) / math.sqrt(60 * 0.05 * 0.95),
        "expected": 26.66,
    },
    "Q4": {
        "computed": (31 - 30) / math.sqrt(60 * 0.5 * 0.5),
        "expected": 0.258,
    },
    "Q5": {
        "computed": two_sided_p(0.258),
        "expected": 0.80,
    },
    "Q6": {
        "computed": wald_ci(48, 60),
        "expected": (0.6988, 0.9012),
    },
    "Q7": {
        "computed": wald_ci(31, 60),
        "expected": (0.3902, 0.6431),
    },
    "Q8": {
        "computed": 0.82 * 657,
        "expected": 538.74,
    },
    "Q9": {
        "computed": 1 / 657,
        "expected": 0.001522,
    },
    "Q10": {
        "computed": 0.94 / 0.25,
        "expected": 3.76,
    },
    "Q11": {
        "computed": 657 / 656,  # factor multiplying C0/cL
        "expected": 1.00152,   # symbolic factor
    },
    "Q12": {
        "computed": 1 / (0.82 - 1/657),
        "expected": 1.2218,
    },
    "Q13": {
        "computed": 1 / (0.94 - 0.25),
        "expected": 1.449,
    },
    "Q14": {
        "computed": 1 / (0.5 - 1/657),
        "expected": 2.006,
    },
    "Q15": {
        "computed": 1 / (0.25 - 1/657),
        "expected": 4.025,
    },
    "Q16": {
        "computed": 100 / (0.01 - 0.01/657),
        "expected": 10015,
    },
}

def match(val, exp):
    # handle intervals
    if isinstance(exp, tuple):
        lo, hi = exp
        return lo <= val[0] <= hi and lo <= val[1] <= hi
    # scalar comparison with relative tolerance 1e-3 (≈0.1%)
    return abs(val - exp) / exp < 1e-3

for cid, data in claims.items():
    comp = data["computed"]
    exp = data["expected"]
    if isinstance(comp, tuple):
        comp_str = f"[{comp[0]:.6f}, {comp[1]:.6f}]"
    else:
        comp_str = f"{comp:.6g}"
    exp_str = f"{exp:.6g}" if not isinstance(exp, tuple) else f"[{exp[0]:.4f}, {exp[1]:.4f}]"
    m = "yes" if match(comp, exp) else "no"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp_str} match={m}")
