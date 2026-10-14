# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Pairwise chance agreement under uniform four-category model is p_e = 0.25",
    "inputs": "K = 4 categories, uniform distribution",
    "formula": "p_e = sum_{k=1}^{4} (1/4)^2 = 4 * 1/16"
  },
  {
    "id": "Q2",
    "statement": "Chance that M models all agree on one claim: p_all(3) = 0.0625, p_all(5) = 3.906e-3, p_all(7) = 2.441e-4",
    "inputs": "M = 3, 5, 7; uniform four-category chance model",
    "formula": "p_all(M) = (1/4)^(M-1)"
  },
  {
    "id": "Q3",
    "statement": "Unanimous agreement of M = 5 models across n = 60 claims has chance probability approx 3.2e-145",
    "inputs": "M = 5, n = 60, log10(4) = 0.60206",
    "formula": "p = 4^(-(M-1)*n) = 4^(-240), log10 p = -240 * 0.60206"
  },
  {
    "id": "Q4",
    "statement": "Benchmark size n = 109.3 (approx 110) claims for kappa CI half-width w = 0.10 with p_o = 0.80, p_e = 0.25",
    "inputs": "w = 0.10, p_o = 0.80, p_e = 0.25, z_{0.975} = 1.96",
    "formula": "n = p_o(1-p_o) / (w^2 (1-p_e)^2) * z^2"
  },
  {
    "id": "Q5",
    "statement": "Benchmark size n = 48.6 (approx 49) claims for half-width w = 0.15",
    "inputs": "w = 0.15, p_o = 0.80, p_e = 0.25, z = 1.96",
    "formula": "n = p_o(1-p_o) / (w^2 (1-p_e)^2) * z^2"
  },
  {
    "id": "Q6",
    "statement": "Worst-case benchmark size n_max = 170.7 (approx 171) claims for w = 0.10",
    "inputs": "p_o(1-p_o) max = 0.25, w = 0.10, p_e = 0.25, z = 1.96",
    "formula": "n_max = 0.25 / (w^2 (1-p_e)^2) * z^2"
  },
  {
    "id": "Q7",
    "statement": "Illustrative kappa: p_o = 0.80, p_e = 0.33, kappa = 0.7015 on hypothetical 50-claim confusion matrix",
    "inputs": "diagonal sum 40, n = 50; marginal products 23*21=483, 13*14=182, 12*13=156, 2*2=4, sum 825",
    "formula": "p_o = 40/50; p_e = 825/2500; kappa = (p_o - p_e)/(1 - p_e)"
  },
  {
    "id": "Q8",
    "statement": "Sample size n = 67.1 (approx 67) claims to detect Spearman rho = 0.35 at power 0.80, alpha = 0.05 two-sided",
    "inputs": "rho = 0.35, z_{0.975} = 1.96, z_{0.80} = 0.8416",
    "formula": "n = ((z_{0.975} + z_{0.80})/rho)^2 + 3"
  },
  {
    "id": "Q9",
    "statement": "Exploratory benchmark n = 50 is powered only for effects rho >= 0.4087",
    "inputs": "z_{0.975} + z_{0.80} = 2.8016, n = 50",
    "formula": "rho_min = 2.8016 / sqrt(n - 3)"
  },
  {
    "id": "Q10",
    "statement": "Standard error of the agreement gap SE(Delta) = 0.1017 with balanced split n1 = n2 = 55",
    "inputs": "p_o(1-p_o) = 0.16, (1-p_e)^2 = 0.5625, n_i = 55",
    "formula": "Var(kappa_i) = 0.16/(55 * 0.5625); SE = sqrt(2 * Var)"
  },
  {
    "id": "Q11",
    "statement": "A gap of Delta = 0.20 is about 1.97 standard errors; Delta = 0.30 is about 2.95 standard errors",
    "inputs": "Delta = 0.20 and 0.30, SE(Delta) = 0.1017",
    "formula": "z = Delta / SE(Delta)"
  },
  {
    "id": "Q12",
    "statement": "Confirmatory-scale run count is 1,650 runs (n = 110, M = 5, F = 3)",
    "inputs": "n = 110, M = 5, F = 3",
    "formula": "runs = M * F * n"
  },
  {
    "id": "Q13",
    "statement": "Expert adjudication effort for 110-claim confirmatory benchmark is 55 expert-hours under 15 minutes per expert per claim",
    "inputs": "n = 110, 2 experts, 0.25 hours per expert per claim",
    "formula": "hours = n * 2 * 0.25"
  }
]

## Script
```python
import math

def sig(x, d=8):
    return f"{x:.{d}g}"

results = []

# Q1: pairwise chance agreement, uniform 4 categories
p_e = sum((1/4)**2 for _ in range(4))
results.append(("Q1", p_e, "0.25"))

# Q2: p_all(M) = (1/4)^(M-1) for M=3,5,7
p3 = (1/4)**2
p5 = (1/4)**4
p7 = (1/4)**6
results.append(("Q2", p3, "0.0625"))
results.append(("Q2b", p5, "0.003906"))
results.append(("Q2c", p7, "0.00024414"))

# Q3: unanimous 5 models, 60 claims: 4^(-240)
log10p = -240 * 0.60206
p_unan = 10 ** log10p
results.append(("Q3", p_unan, "3.2e-145"))

# Q4: n for w=0.10, p_o=0.80, p_e=0.25, z=1.96
def n_kappa(w, po=0.80, pe=0.25, z=1.96):
    return po*(1-po) / (w**2 * (1-pe)**2) * z**2
n10 = n_kappa(0.10)
results.append(("Q4", n10, "109.3"))

# Q5: n for w=0.15
n15 = n_kappa(0.15)
results.append(("Q5", n15, "48.6"))

# Q6: worst case n_max, po(1-po)=0.25
nmax = 0.25 / (0.10**2 * 0.75**2) * 1.96**2
results.append(("Q6", nmax, "170.7"))

# Q7: illustrative kappa
po = 40/50
pe = (23*21 + 13*14 + 12*13 + 2*2) / 50**2
kappa = (po - pe) / (1 - pe)
results.append(("Q7a", po, "0.80"))
results.append(("Q7b", pe, "0.33"))
results.append(("Q7c", kappa, "0.7015"))

# Q8: Spearman sample size, rho=0.35
zsum = 1.96 + 0.8416
n_sp = (zsum/0.35)**2 + 3
results.append(("Q8", n_sp, "67.1"))

# Q9: rho_min for n=50
rho_min = zsum / math.sqrt(50 - 3)
results.append(("Q9", rho_min, "0.4087"))

# Q10: SE(Delta) with n1=n2=55
var_k = 0.16 / (55 * 0.5625)
se = math.sqrt(2 * var_k)
results.append(("Q10", se, "0.1017"))

# Q11: z-scores for Delta=0.20 and 0.30
z20 = 0.20 / se
z30 = 0.30 / se
results.append(("Q11a", z20, "1.97"))
results.append(("Q11b", z30, "2.95"))

# Q12: runs = M*F*n
runs = 5 * 3 * 110
results.append(("Q12", runs, "1650"))

# Q13: expert hours
hours = 110 * 2 * 0.25
results.append(("Q13", hours, "55"))

def match(computed, expected_str):
    # round computed to significant digits of expected string
    exp = float(expected_str)
    # count significant digits in expected
    s = expected_str.replace("-", "").replace(".", "").lstrip("0")
    digits = len(s.rstrip("e023456789")) if False else None
    # simpler: count sig digits manually via string
    import re
    m = re.match(r"^-?0*(\d[\d.]*)$", expected_str)
    # count significant digits
    digits = len(re.sub(r"[^0-9]", "", expected_str.split("e")[0]).lstrip("0"))
    if "e" in expected_str:
        mant = expected_str.split("e")[0]
        digits = len(re.sub(r"[^0-9]", "", mant).lstrip("0"))
    rounded = float(f"%.{digits}g" % computed)
    return "yes" if abs(rounded - exp) <= 1e-12 * max(1, abs(exp)) or rounded == exp else "no"

for cid, comp, exp in results:
    print(f"CLAIM {cid}: computed={comp:.8g} expected={exp} match={match(comp, exp)}")

n_claims = len(results)
n_match = sum(1 for _, c, e in results if match(c, e) == "yes")
print(f"VERIFICATION SUMMARY: {n_claims} claims, {n_match} match, {n_claims - n_match} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.25 expected=0.25 match=yes
CLAIM Q2: computed=0.0625 expected=0.0625 match=yes
CLAIM Q2b: computed=0.00390625 expected=0.003906 match=yes
CLAIM Q2c: computed=0.00024414062 expected=0.00024414 match=yes
CLAIM Q3: computed=3.2033176e-145 expected=3.2e-145 match=yes
CLAIM Q4: computed=109.27218 expected=109.3 match=yes
CLAIM Q5: computed=48.565412 expected=48.6 match=yes
CLAIM Q6: computed=170.73778 expected=170.7 match=yes
CLAIM Q7a: computed=0.8 expected=0.80 match=yes
CLAIM Q7b: computed=0.33 expected=0.33 match=yes
CLAIM Q7c: computed=0.70149254 expected=0.7015 match=yes
CLAIM Q8: computed=67.073164 expected=67.1 match=yes
CLAIM Q9: computed=0.40865536 expected=0.4087 match=yes
CLAIM Q10: computed=0.10170268 expected=0.1017 match=yes
CLAIM Q11a: computed=1.9665166 expected=1.97 match=yes
CLAIM Q11b: computed=2.9497749 expected=2.95 match=yes
CLAIM Q12: computed=1650 expected=1650 match=yes
CLAIM Q13: computed=55 expected=55 match=yes
VERIFICATION SUMMARY: 18 claims, 18 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.25 | 0.25 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.0625 | 0.0625 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2b | 0.00390625 | 0.003906 | yes | match | 4 significant digits (as printed, at least 3) |
| Q2c | 0.00024414062 | 0.00024414 | yes | match | 5 significant digits (as printed, at least 3) |
| Q3 | 3.2033176e-145 | 3.2e-145 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 109.27218 | 109.3 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 48.565412 | 48.6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 170.73778 | 170.7 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7a | 0.8 | 0.80 | yes | match | 3 significant digits (as printed, at least 3) |
| Q7b | 0.33 | 0.33 | yes | match | 3 significant digits (as printed, at least 3) |
| Q7c | 0.70149254 | 0.7015 | yes | match | 4 significant digits (as printed, at least 3) |
| Q8 | 67.073164 | 67.1 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 0.40865536 | 0.4087 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 0.10170268 | 0.1017 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11a | 1.9665166 | 1.97 | yes | match | 3 significant digits (as printed, at least 3) |
| Q11b | 2.9497749 | 2.95 | yes | match | 3 significant digits (as printed, at least 3) |
| Q12 | 1650 | 1650 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 55 | 55 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 18.
