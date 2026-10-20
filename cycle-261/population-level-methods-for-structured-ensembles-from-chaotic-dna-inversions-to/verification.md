# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The number of contiguous segments in a binary sequence of length L=10 is 55.",
    "inputs": "L = 10",
    "formula": "L*(L+1)/2"
  },
  {
    "id": "Q2",
    "statement": "The total length summed over all contiguous segments for L=10 is 220.",
    "inputs": "L = 10",
    "formula": "sum_{k=1}^{L} k*(L-k+1)"
  },
  {
    "id": "Q3",
    "statement": "The average segment length is 4.0.",
    "inputs": "total length S = 220, number of segments = 55",
    "formula": "S / 55"
  },
  {
    "id": "Q4",
    "statement": "The saturation step count t_sat under the independence approximation is 3.",
    "inputs": "L = 10, average segment length = 4.0",
    "formula": "ceil(L / average_length)"
  },
  {
    "id": "Q5",
    "statement": "The first‑moment rate ̅M_1 under a bang‑bang broadcast input is 1/3 per unit input.",
    "inputs": "uniform gain density rho(ω)=1/2 on [-1,1]",
    "formula": "(1/2) * integral_{-1}^{1} ω^2 dω"
  },
  {
    "id": "Q6",
    "statement": "The variance at time t=0.3 with constant input u=+1 is σ^2 = 0.03.",
    "inputs": "t = 0.3, U(t)=t (since u=+1)",
    "formula": "U(t)^2 / 3"
  },
  {
    "id": "Q7",
    "statement": "The standard deviation at t=0.3 is approximately 0.1732.",
    "inputs": "σ^2 = 0.03",
    "formula": "sqrt(σ^2)"
  },
  {
    "id": "Q8",
    "statement": "The minimum steering time to reach M1_target = 0.1 is 0.3 time units.",
    "inputs": "M1_target = 0.1, first‑moment rate = 1/3",
    "formula": "M1_target / (1/3)"
  },
  {
    "id": "Q9",
    "statement": "For the right‑triangular gain density, the coefficient c2 = 7/18 ≈ 0.3889.",
    "inputs": "ρ_s(ω) = (2/3)(ω+1) on [0,1]",
    "formula": "(2/3) * integral_{0}^{1} (ω^3 + ω^2) dω"
  },
  {
    "id": "Q10",
    "statement": "The minimum steering time for the skewed gain distribution is approximately 0.2571 time units.",
    "inputs": "M1_target = 0.1, c2 = 7/18",
    "formula": "M1_target / c2"
  },
  {
    "id": "Q11",
    "statement": "The baseline expected number of tokens per cycle for a single leg with α=0.7 and γ=4 is 2.7731.",
    "inputs": "α = 0.7, γ = 4",
    "formula": "(1 - α^{γ+1}) / (1 - α)"
  },
  {
    "id": "Q12",
    "statement": "The baseline throughput is 0.55462 tokens per unit cost.",
    "inputs": "baseline expected tokens = 2.7731, draft cost per position = 1, γ = 4, verification cost = 1",
    "formula": "2.7731 / (γ*1 + 1)"
  },
  {
    "id": "Q13",
    "statement": "The ensemble effective acceptance probability is 0.94.",
    "inputs": "α1 = 0.5, α2 = 0.6, α3 = 0.7",
    "formula": "1 - (1-α1)*(1-α2)*(1-α3)"
  },
  {
    "id": "Q14",
    "statement": "The ensemble expected number of tokens per cycle is 4.43493296.",
    "inputs": "α_eff = 0.94, γ = 4",
    "formula": "(1 - α_eff^{γ+1}) / (1 - α_eff)"
  },
  {
    "id": "Q15",
    "statement": "The ensemble throughput is 0.886986592 tokens per unit cost.",
    "inputs": "ensemble expected tokens = 4.43493296, total cost = γ* (c1+c2+c3) + 1 = 5",
    "formula": "4.43493296 / 5"
  },
  {
    "id": "Q16",
    "statement": "The speedup of the ensemble over the best single leg is 1.5993.",
    "inputs": "ensemble throughput = 0.886986592, baseline throughput = 0.55462",
    "formula": "0.886986592 / 0.55462"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=55 expected=55 match=yes
CLAIM Q2: computed=220 expected=220 match=yes
CLAIM Q3: computed=4.0 expected=4.0 match=yes
CLAIM Q4: computed=3 expected=3 match=yes
CLAIM Q5: computed=1/3 expected=1/3 match=yes
CLAIM Q6: computed=0.03 expected=0.03 match=yes
CLAIM Q7: computed=0.1732 expected=0.1732 match=yes
CLAIM Q8: computed=0.3 expected=0.3 match=yes
CLAIM Q9: computed=0.3889 expected=0.3889 match=yes
CLAIM Q10: computed=0.2571 expected=0.2571 match=yes
CLAIM Q11: computed=2.7731 expected=2.7731 match=yes
CLAIM Q12: computed=0.55462 expected=0.55462 match=yes
CLAIM Q13: computed=0.94 expected=0.94 match=yes
CLAIM Q14: computed=4.43493296 expected=4.43493296 match=yes
CLAIM Q15: computed=0.886986592 expected=0.886986592 match=yes
CLAIM Q16: computed=1.5993 expected=1.5993 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 146, in <module>
  File "<string>", line 146, in <genexpr>
  File "<string>", line 36, in compare
TypeError: type function doesn't define __round__ method

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 55 | 55 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 220 | 220 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 4.0 | 4.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 1/3 | 1/3 | yes | match | script verdict (values not both numeric) |
| Q6 | 0.03 | 0.03 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 0.1732 | 0.1732 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 0.3 | 0.3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0.3889 | 0.3889 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 0.2571 | 0.2571 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 2.7731 | 2.7731 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 0.55462 | 0.55462 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q13 | 0.94 | 0.94 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 4.43493296 | 4.43493296 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q15 | 0.886986592 | 0.886986592 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q16 | 1.5993 | 1.5993 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
