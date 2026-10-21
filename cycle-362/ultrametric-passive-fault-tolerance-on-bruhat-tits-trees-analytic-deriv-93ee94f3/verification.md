# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Ball size for a $p=3$ tree of depth $t=1$ is $n_{1}=5$ qudits.",
    "inputs": "p = 3, t = 1",
    "formula": "n = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q2",
    "statement": "Ball size for a $p=3$ tree of depth $t=2$ is $n_{2}=17$ qudits.",
    "inputs": "p = 3, t = 2",
    "formula": "n = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q3",
    "statement": "Logical distance for depth $t=1$ is $d=3$.",
    "inputs": "t = 1",
    "formula": "d = 2*t + 1"
  },
  {
    "id": "Q4",
    "statement": "Logical distance for depth $t=2$ is $d=5$.",
    "inputs": "t = 2",
    "formula": "d = 2*t + 1"
  },
  {
    "id": "Q5",
    "statement": "Passive logical failure probability for $p=3$, $t=1$, $\\varepsilon=10^{-3}$ is $P_{\\mathrm{pass}} = 5.992003\\times10^{-6}$.",
    "inputs": "p = 3 (so p+1 = 4), t = 1, \\varepsilon = 1e-3",
    "formula": "P = sum_{k=t+1}^{p+1} C(p+1,k) * \\varepsilon^k * (1-\\varepsilon)^{p+1-k}"
  },
  {
    "id": "Q6",
    "statement": "Suppression factor is $S = \\varepsilon / P_{\\mathrm{pass}} \\approx 166.9$.",
    "inputs": "\\varepsilon = 1e-3, P_{\\mathrm{pass}} = 5.992003e-6",
    "formula": "S = \\varepsilon / P"
  },
  {
    "id": "Q7",
    "statement": "Passive logical failure probability for $p=3$, $t=2$, $\\varepsilon=10^{-3}$ is $P_{\\mathrm{pass}}^{(2)} \\approx 3.997\\times10^{-9}$.",
    "inputs": "p = 3 (so p+1 = 4), t = 2, \\varepsilon = 1e-3",
    "formula": "P = sum_{k=t+1}^{p+1} C(p+1,k) * \\varepsilon^k * (1-\\varepsilon)^{p+1-k}"
  },
  {
    "id": "Q8",
    "statement": "Energy barrier for logical distance $d=3$ is $E_{\\text{barrier}} = 8$ (arbitrary units).",
    "inputs": "d = 3",
    "formula": "E = 2^d"
  },
  {
    "id": "Q9",
    "statement": "Energy barrier for logical distance $d=5$ is $E_{\\text{barrier}} = 32$ (arbitrary units).",
    "inputs": "d = 5",
    "formula": "E = 2^d"
  },
  {
    "id": "Q10",
    "statement": "Projected hardware cost per logical qubit using a five‑qudit ball code is $\\$0.75$.",
    "inputs": "cost per tweezer = 0.10 USD, cost per control laser = 0.05 USD, number of qudits n = 5",
    "formula": "cost = n * (cost_tweezer + cost_laser)"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=5 expected=5 match=yes
CLAIM Q10: computed=0.75 expected=0.75 match=yes
CLAIM Q2: computed=17 expected=17 match=yes
CLAIM Q3: computed=3 expected=3 match=yes
CLAIM Q4: computed=5 expected=5 match=yes
CLAIM Q5: computed=5.992003e-06 expected=5.992003e-6 match=no
CLAIM Q6: computed=166.8891 expected=166.9 match=no
CLAIM Q7: computed=3.997e-09 expected=3.997e-9 match=no
CLAIM Q8: computed=8 expected=8 match=yes
CLAIM Q9: computed=32 expected=32 match=yes
VERIFICATION SUMMARY: 10 claims, 7 match, 3 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.75 | 0.75 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 17 | 17 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 5.992003e-06 | 5.992003e-6 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q6 | 166.8891 | 166.9 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 3.997e-09 | 3.997e-9 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 32 | 32 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
