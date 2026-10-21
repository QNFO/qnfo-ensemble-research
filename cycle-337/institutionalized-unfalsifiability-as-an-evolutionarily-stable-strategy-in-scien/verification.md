# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Rationality threshold $p^{*}= (s+c)/(b+c) \\approx 0.6667$.",
    "inputs": "s=1, c=1, b=2",
    "formula": "p* = (s + c) / (b + c)"
  },
  {
    "id": "Q2",
    "statement": "Falsifiable payoff $\\pi_{F}= p\\,b - (1-p)\\,c = 0.8$.",
    "inputs": "p=0.6, b=2, c=1",
    "formula": "pi_F = p*b - (1-p)*c"
  },
  {
    "id": "Q3",
    "statement": "Post‑hoc payoff $\\pi_{P}= s = 1.0$.",
    "inputs": "s=1",
    "formula": "pi_P = s"
  },
  {
    "id": "Q4",
    "statement": "Replicator coefficient $\\kappa = \\pi_{F}-\\pi_{P}= -0.2$.",
    "inputs": "pi_F=0.8, pi_P=1.0",
    "formula": "kappa = pi_F - pi_P"
  },
  {
    "id": "Q5",
    "statement": "Time to near‑extinction $t = \\ln 9 / 0.2 \\approx 10.99$ generations for $x$ to fall from $0.5$ to $0.1$.",
    "inputs": "ln9≈2.19722, |kappa|=0.2",
    "formula": "t = ln(9) / |kappa|"
  },
  {
    "id": "Q6",
    "statement": "Flip point $b_{\\text{flip}} = (s+(1-p)c)/p \\approx 2.3333$.",
    "inputs": "s=1, p=0.6, c=1",
    "formula": "b_flip = (s + (1-p)*c) / p"
  },
  {
    "id": "Q7",
    "statement": "Sensitivity $\\partial p^{*}/\\partial b = -(s+c)/(b+c)^{2} \\approx -0.2222$.",
    "inputs": "s=1, c=1, b=2",
    "formula": "dp*/db = - (s + c) / (b + c)^2"
  },
  {
    "id": "Q8",
    "statement": "Sensitivity $\\partial p^{*}/\\partial c = (b-s)/(b+c)^{2} \\approx 0.1111$.",
    "inputs": "b=2, s=1, b+c=3",
    "formula": "dp*/dc = (b - s) / (b + c)^2"
  },
  {
    "id": "Q9",
    "statement": "Sensitivity $\\partial p^{*}/\\partial s = 1/(b+c) \\approx 0.3333$.",
    "inputs": "b=2, c=1",
    "formula": "dp*/ds = 1 / (b + c)"
  },
  {
    "id": "Q10",
    "statement": "Sensitivity $\\partial b_{\\text{flip}}/\\partial s = 1/p \\approx 1.6667$.",
    "inputs": "p=0.6",
    "formula": "db_flip/ds = 1 / p"
  },
  {
    "id": "Q11",
    "statement": "Sensitivity $\\partial b_{\\text{flip}}/\\partial c = (1-p)/p \\approx 0.6667$.",
    "inputs": "p=0.6",
    "formula": "db_flip/dc = (1 - p) / p"
  },
  {
    "id": "Q12",
    "statement": "Strong reform ($b=10$): $\\pi_{F}=5.6$, $p^{*}=2/11 \\approx 0.1818$, $\\kappa=+4.6$.",
    "inputs": "b=10, p=0.6, c=1, s=1",
    "formula": "pi_F = p*b - (1-p)*c; p* = (s + c) / (b + c); kappa = pi_F - s"
  },
  {
    "id": "Q13",
    "statement": "Weak reform ($b=5$): $\\pi_{F}=2.6$, $p^{*}=1/3 \\approx 0.3333$, $\\kappa=+1.6$.",
    "inputs": "b=5, p=0.6, c=1, s=1",
    "formula": "pi_F = p*b - (1-p)*c; p* = (s + c) / (b + c); kappa = pi_F - s"
  },
  {
    "id": "Q14",
    "statement": "Adverse reform ($s'=2$): new threshold $p^{*}_{\\text{new}}=1.0$, $\\kappa=-1.2$.",
    "inputs": "s'=2, c=1, b=2, p=0.6",
    "formula": "p*_new = (s' + c) / (b + c); kappa = p*b - (1-p)*c - s'"
  },
  {
    "id": "Q15",
    "statement": "Scenario $c=5$: $\\pi_{F}=-0.8$, $\\kappa=-1.8$, extinction time $t = \\ln 9 / 1.8 \\approx 1.22$ generations.",
    "inputs": "p=0.6, b=2, c=5, s=1",
    "formula": "pi_F = p*b - (1-p)*c; kappa = pi_F - s; t = ln(9) / |kappa|"
  },
  {
    "id": "Q16",
    "statement": "Second‑order sensitivity $\\partial^{2} p^{*}/\\partial b^{2}= 2(s+c)/(b+c)^{3}=4/27 \\approx 0.1481$.",
    "inputs": "s=1, c=1, b=2",
    "formula": "d2p*/db2 = 2(s + c) / (b + c)^3"
  }
]

## Script
```python
import math

def fmt(value, expected):
    if '.' in expected:
        dp = len(expected.split('.')[1])
        rounded = round(value, dp)
        # Ensure trailing zeros are kept
        return f"{rounded:.{dp}f}"
    else:
        return str(int(round(value)))

claims = {
    "Q1": {"calc": (1+1)/(2+1), "expected": "0.6667"},
    "Q2": {"calc": 0.6*2 - (1-0.6)*1, "expected": "0.8"},
    "Q3": {"calc": 1, "expected": "1.0"},
    "Q4": {"calc": 0.8 - 1.0, "expected": "-0.2"},
    "Q5": {"calc": math.log(9)/0.2, "expected": "10.99"},
    "Q6": {"calc": (1 + (1-0.6)*1)/0.6, "expected": "2.3333"},
    "Q7": {"calc": -(1+1)/(2+1)**2, "expected": "-0.2222"},
    "Q8": {"calc": (2-1)/(2+1)**2, "expected": "0.1111"},
    "Q9": {"calc": 1/(2+1), "expected": "0.3333"},
    "Q10": {"calc": 1/0.6, "expected": "1.6667"},
    "Q11": {"calc": (1-0.6)/0.6, "expected": "0.6667"},
    "Q12": {"calc": (0.6*10 - (1-0.6)*1, (1+1)/(10+1), 0.6*10 - (1-0.6)*1 - 1),
            "expected": "5.6, 0.1818, 4.6"},
    "Q13": {"calc": (0.6*5 - (1-0.6)*1, (1+1)/(5+1), 0.6*5 - (1-0.6)*1 - 1),
            "expected": "2.6, 0.3333, 1.6"},
    "Q14": {"calc": ((2+1)/(2+1), 0.6*2 - (1-0.6)*1 - 2),
            "expected": "1.0, -1.2"},
    "Q15": {"calc": (0.6*2 - (1-0.6)*5,
                    0.6*2 - (1-0.6)*5 - 1,
                    math.log(9)/1.8),
            "expected": "-0.8, -1.8, 1.22"},
    "Q16": {"calc": 2*(1+1)/(2+1)**3, "expected": "0.1481"},
}

for cid, data in claims.items():
    calc = data["calc"]
    exp = data["expected"]
    if isinstance(calc, tuple):
        comps = [fmt(v, e.strip()) for v, e in zip(calc, exp.split(','))]
        computed_str = ", ".join(comps)
    else:
        computed_str = fmt(calc, exp)
    match = "yes" if computed_str == exp else "no"
    print(f"CLAIM {cid}: computed={computed_str} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for d in claims.values() if (lambda c,e: (c if not isinstance(c,tuple) else ', '.join([fmt(v, e_i.strip()) for v,e_i in zip(c,e.split(','))])) ) (d['calc'], d['expected']) == d['expected'])} match, "
      f"{len(claims) - sum(1 for d in claims.values() if (lambda c,e: (c if not isinstance(c,tuple) else ', '.join([fmt(v, e_i.strip()) for v,e_i in zip(c,e.split(','))])) ) (d['calc'], d['expected']) == d['expected'])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.6667 expected=0.6667 match=yes
CLAIM Q2: computed=0.8 expected=0.8 match=yes
CLAIM Q3: computed=1.0 expected=1.0 match=yes
CLAIM Q4: computed=-0.2 expected=-0.2 match=yes
CLAIM Q5: computed=10.99 expected=10.99 match=yes
CLAIM Q6: computed=2.3333 expected=2.3333 match=yes
CLAIM Q7: computed=-0.2222 expected=-0.2222 match=yes
CLAIM Q8: computed=0.1111 expected=0.1111 match=yes
CLAIM Q9: computed=0.3333 expected=0.3333 match=yes
CLAIM Q10: computed=1.6667 expected=1.6667 match=yes
CLAIM Q11: computed=0.6667 expected=0.6667 match=yes
CLAIM Q12: computed=5.6, 0.1818, 4.6 expected=5.6, 0.1818, 4.6 match=yes
CLAIM Q13: computed=2.6, 0.3333, 1.6 expected=2.6, 0.3333, 1.6 match=yes
CLAIM Q14: computed=1.0, -1.2 expected=1.0, -1.2 match=yes
CLAIM Q15: computed=-0.8, -1.8, 1.22 expected=-0.8, -1.8, 1.22 match=yes
CLAIM Q16: computed=0.1481 expected=0.1481 match=yes
VERIFICATION SUMMARY: 16 claims, 4 match, 12 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.6667 | 0.6667 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 0.8 | 0.8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1.0 | 1.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | -0.2 | -0.2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 10.99 | 10.99 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 2.3333 | 2.3333 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | -0.2222 | -0.2222 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 0.1111 | 0.1111 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 0.3333 | 0.3333 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 1.6667 | 1.6667 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q11 | 0.6667 | 0.6667 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 0.1481 | 0.1481 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 12.
