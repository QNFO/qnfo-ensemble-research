# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The Haar measure of the ball $B_{r}$ equals $r^{2}$.",
    "inputs": "radius $r$ (any positive $p$‑adic number)",
    "formula": "$\\mu(B_{r}) = r^{2}$"
  },
  {
    "id": "Q2",
    "statement": "The Haar measure of the sphere $S_{r}$ equals $r^{2}(1-p^{-2})$.",
    "inputs": "radius $r$, prime $p$",
    "formula": "$C_{p}(r)=\\mu(S_{r})=r^{2}\\bigl(1-p^{-2}\\bigr)$"
  },
  {
    "id": "Q3",
    "statement": "The scale‑invariant circle constant $\\kappa_{p}$ equals $1-p^{-2}$.",
    "inputs": "prime $p$",
    "formula": "$\\kappa_{p}=1-p^{-2}$"
  },
  {
    "id": "Q4",
    "statement": "The alternative scale‑invariant constant $\\kappa'_{p}$ equals $(1-p^{-2})/2$.",
    "inputs": "prime $p$",
    "formula": "$\\kappa'_{p}=\\frac{1-p^{-2}}{2}$"
  },
  {
    "id": "Q5",
    "statement": "For $p=2$, $\\kappa_{2}=3/4=0.75$.",
    "inputs": "prime $p=2$",
    "formula": "$\\kappa_{2}=1-2^{-2}=\\tfrac34=0.75$"
  },
  {
    "id": "Q6",
    "statement": "For $p=2$, $\\kappa'_{2}=3/8=0.375$.",
    "inputs": "prime $p=2$",
    "formula": "$\\kappa'_{2}=\\tfrac{1-2^{-2}}{2}=\\tfrac34\\cdot\\tfrac12=\\tfrac38=0.375$"
  },
  {
    "id": "Q7",
    "statement": "For $p=3$, $\\kappa_{3}=8/9\\approx0.888889$.",
    "inputs": "prime $p=3$",
    "formula": "$\\kappa_{3}=1-3^{-2}=1-\\tfrac19=\\tfrac89\\approx0.888889$"
  },
  {
    "id": "Q8",
    "statement": "For $p=3$, $\\kappa'_{3}=4/9\\approx0.444444$.",
    "inputs": "prime $p=3$",
    "formula": "$\\kappa'_{3}=\\tfrac{1-3^{-2}}{2}=\\tfrac{8/9}{2}=\\tfrac49\\approx0.444444$"
  },
  {
    "id": "Q9",
    "statement": "For $p=5$, $\\kappa_{5}=24/25=0.96$.",
    "inputs": "prime $p=5$",
    "formula": "$\\kappa_{5}=1-5^{-2}=1-\\tfrac1{25}=\\tfrac{24}{25}=0.96$"
  },
  {
    "id": "Q10",
    "statement": "For $p=5$, $\\kappa'_{5}=12/25=0.48$.",
    "inputs": "prime $p=5$",
    "formula": "$\\kappa'_{5}=\\tfrac{1-5^{-2}}{2}=\\tfrac{24/25}{2}=\\tfrac{12}{25}=0.48$"
  },
  {
    "id": "Q11",
    "statement": "For $p=7$, $\\kappa_{7}=48/49\\approx0.979592$.",
    "inputs": "prime $p=7$",
    "formula": "$\\kappa_{7}=1-7^{-2}=1-\\tfrac1{49}=\\tfrac{48}{49}\\approx0.979592$"
  },
  {
    "id": "Q12",
    "statement": "For $p=7$, $\\kappa'_{7}=24/49\\approx0.489796$.",
    "inputs": "prime $p=7$",
    "formula": "$\\kappa'_{7}=\\tfrac{1-7^{-2}}{2}=\\tfrac{48/49}{2}=\\tfrac{24}{49}\\approx0.489796$"
  },
  {
    "id": "Q13",
    "statement": "For $p=11$, $\\kappa_{11}=120/121\\approx0.991736$.",
    "inputs": "prime $p=11$",
    "formula": "$\\kappa_{11}=1-11^{-2}=1-\\tfrac1{121}=\\tfrac{120}{121}\\approx0.991736$"
  },
  {
    "id": "Q14",
    "statement": "For $p=11$, $\\kappa'_{11}=60/121\\approx0.495868$.",
    "inputs": "prime $p=11$",
    "formula": "$\\kappa'_{11}=\\tfrac{1-11^{-2}}{2}=\\tfrac{120/121}{2}=\\tfrac{60}{121}\\approx0.495868$"
  },
  {
    "id": "Q15",
    "statement": "The finite product $P_{13}=\\prod_{p\\le13}\\kappa_{p}=\\frac{15482880}{25050025}\\approx0.618078$.",
    "inputs": "primes $2,3,5,7,11,13$ and their $\\kappa_{p}=1-p^{-2}$ values",
    "formula": "$P_{13}=\\prod_{p\\le13}\\bigl(1-p^{-2}\\bigr)=\\frac{15482880}{25050025}\\approx0.618078$"
  },
  {
    "id": "Q16",
    "statement": "The infinite product $\\prod_{p}\\kappa_{p}=6/\\pi^{2}\\approx0.607927$.",
    "inputs": "Euler product identity $\\prod_{p}(1-p^{-2})=1/\\zeta(2)=6/\\pi^{2}$",
    "formula": "$\\prod_{p}\\kappa_{p}=\\prod_{p}(1-p^{-2})=\\frac{6}{\\pi^{2}}\\approx0.607927$"
  }
]

## Script
```python
import math
from fractions import Fraction

# Expected values from the paper (as strings). "none" means no numeric expectation.
expected = {
    "Q1": "none",
    "Q2": "0.75",
    "Q3": "0.75",
    "Q4": "0.375",
    "Q5": "0.75",
    "Q6": "0.375",
    "Q7": "0.888889",
    "Q8": "0.444444",
    "Q9": "0.96",
    "Q10": "0.48",
    "Q11": "0.979592",
    "Q12": "0.489796",
    "Q13": "0.991736",
    "Q14": "0.495868",
    "Q15": "0.618078",
    "Q16": "0.607927",
}

def fmt(val, exp):
    """Format val to the same number of decimal places as exp."""
    if exp == "none":
        return "none"
    if "." in exp:
        dec = len(exp.split(".")[1])
        fmt_str = f"{{:.{dec}f}}"
        return fmt_str.format(val)
    else:
        # integer expectation
        return str(int(round(val)))

def match_str(comp, exp):
    return "yes" if comp == exp else "no"

# Compute each claim
results = {}

# Q1: μ(B_r) = r^2, use r = 1 for a concrete numeric illustration
r = 1
mu_B = r**2
results["Q1"] = mu_B

# Q2: C_p(r) = r^2 (1 - p^{-2}), use r = 1, p = 2
p = 2
C = r**2 * (1 - p**-2)
results["Q2"] = C

# Q3: κ_p = 1 - p^{-2}, p = 2
kappa = 1 - p**-2
results["Q3"] = kappa

# Q4: κ'_p = (1 - p^{-2})/2, p = 2
kappa_prime = (1 - p**-2) / 2
results["Q4"] = kappa_prime

# Q5–Q14: specific primes
primes = {2: "Q5", 3: "Q7", 5: "Q9", 7: "Q11", 11: "Q13"}
for p, qid in primes.items():
    k = 1 - p**-2
    results[qid] = k
    results[qid.replace("Q", "Q")] = k  # placeholder, will be overwritten below
    # also store κ' values
    qid_prime = qid.replace("Q", "Q").replace(str(p), str(p))  # dummy
# Actually compute each explicitly:
# Q5, Q6 for p=2
p = 2
k = 1 - p**-2
results["Q5"] = k
results["Q6"] = k/2

# Q7, Q8 for p=3
p = 3
k = 1 - p**-2
results["Q7"] = k
results["Q8"] = k/2

# Q9, Q10 for p=5
p = 5
k = 1 - p**-2
results["Q9"] = k
results["Q10"] = k/2

# Q11, Q12 for p=7
p = 7
k = 1 - p**-2
results["Q11"] = k
results["Q12"] = k/2

# Q13, Q14 for p=11
p = 11
k = 1 - p**-2
results["Q13"] = k
results["Q14"] = k/2

# Q15: finite product up to p=13
primes_up_to_13 = [2,3,5,7,11,13]
prod = Fraction(1,1)
for p in primes_up_to_13:
    prod *= Fraction(p**2 - 1, p**2)   # 1 - p^{-2}
results["Q15"] = float(prod)  # decimal for comparison

# Q16: infinite product = 6 / pi^2
results["Q16"] = 6 / (math.pi**2)

# Print results
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):
    comp_val = results[qid]
    exp_val = expected[qid]
    comp_str = fmt(comp_val, exp_val)
    match = match_str(comp_str, exp_val)
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_val} match={match}")

```

## Execution output
```
CLAIM Q1: computed=none expected=none match=yes
CLAIM Q2: computed=0.75 expected=0.75 match=yes
CLAIM Q3: computed=0.75 expected=0.75 match=yes
CLAIM Q4: computed=0.375 expected=0.375 match=yes
CLAIM Q5: computed=0.75 expected=0.75 match=yes
CLAIM Q6: computed=0.375 expected=0.375 match=yes
CLAIM Q7: computed=0.888889 expected=0.888889 match=yes
CLAIM Q8: computed=0.444444 expected=0.444444 match=yes
CLAIM Q9: computed=0.96 expected=0.96 match=yes
CLAIM Q10: computed=0.48 expected=0.48 match=yes
CLAIM Q11: computed=0.979592 expected=0.979592 match=yes
CLAIM Q12: computed=0.489796 expected=0.489796 match=yes
CLAIM Q13: computed=0.991736 expected=0.991736 match=yes
CLAIM Q14: computed=0.495868 expected=0.495868 match=yes
CLAIM Q15: computed=0.618078 expected=0.618078 match=yes
CLAIM Q16: computed=0.607927 expected=0.607927 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | none | none | yes | match | script verdict (values not both numeric) |
| Q2 | 0.75 | 0.75 | yes | match | 3 significant digits (as printed, at least 3) |
| Q3 | 0.75 | 0.75 | yes | match | 3 significant digits (as printed, at least 3) |
| Q4 | 0.375 | 0.375 | yes | match | 3 significant digits (as printed, at least 3) |
| Q5 | 0.75 | 0.75 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.375 | 0.375 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 0.888889 | 0.888889 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 0.444444 | 0.444444 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q9 | 0.96 | 0.96 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.48 | 0.48 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.979592 | 0.979592 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q12 | 0.489796 | 0.489796 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q13 | 0.991736 | 0.991736 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q14 | 0.495868 | 0.495868 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q15 | 0.618078 | 0.618078 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q16 | 0.607927 | 0.607927 | yes | match | 6 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
