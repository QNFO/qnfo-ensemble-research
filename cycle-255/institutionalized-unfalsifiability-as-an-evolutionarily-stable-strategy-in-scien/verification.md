# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The accuracy threshold is $p^{*}=\\frac{s+c}{b+c}=\\frac{2}{3}\\approx0.6667$.",
    "inputs": "s=1, c=1, b=2",
    "formula": "(s + c) / (b + c)"
  },
  {
    "id": "Q2",
    "statement": "The payoff for a falsifiable strategy is $\\pi_{F}=p\\,b-(1-p)\\,c=0.8$.",
    "inputs": "p=0.6, b=2, c=1",
    "formula": "p * b - (1 - p) * c"
  },
  {
    "id": "Q3",
    "statement": "The payoff for a post‑hoc strategy is $\\pi_{P}=s=1$.",
    "inputs": "s=1",
    "formula": "s"
  },
  {
    "id": "Q4",
    "statement": "The reward at which the two strategies are equal is $b_{\\text{flip}}=\\frac{s+(1-p)c}{p}\\approx2.3333$.",
    "inputs": "s=1, p=0.6, c=1",
    "formula": "(s + (1 - p) * c) / p"
  },
  {
    "id": "Q5",
    "statement": "The replicator coefficient is $\\pi_{F}-\\pi_{P}=-0.2$.",
    "inputs": "pi_F=0.8, pi_P=1.0",
    "formula": "pi_F - pi_P"
  },
  {
    "id": "Q6",
    "statement": "The sensitivity of the threshold to $b$ is $\\partial p^{*}/\\partial b = -\\frac{s+c}{(b+c)^{2}}\\approx-0.2222$.",
    "inputs": "s=1, c=1, b=2",
    "formula": "- (s + c) / (b + c)^2"
  },
  {
    "id": "Q7",
    "statement": "The sensitivity of the threshold to $c$ is $\\partial p^{*}/\\partial c = \\frac{b-s}{(b+c)^{2}}\\approx0.1111$.",
    "inputs": "b=2, s=1, c=1",
    "formula": "(b - s) / (b + c)^2"
  },
  {
    "id": "Q8",
    "statement": "The sensitivity of the threshold to $s$ is $\\partial p^{*}/\\partial s = \\frac{1}{b+c}\\approx0.3333$.",
    "inputs": "b=2, c=1",
    "formula": "1 / (b + c)"
  },
  {
    "id": "Q9",
    "statement": "For a given narrative reward $s$, the required confirmed‑prediction reward is $b(s)=\\frac{s+1}{p}-1$, yielding $b=1.5$ for $s=0.5$, $b=2.3333$ for $s=1.0$, and $b=3.1667$ for $s=1.5$.",
    "inputs": "p=0.6, s∈{0.5,1.0,1.5}",
    "formula": "(s + 1) / p - 1"
  },
  {
    "id": "Q10",
    "statement": "For a given failure cost $c$, the required reward is $b(c)=\\frac{1+c}{p}-c$, giving $b=2.0$ for $c=0.5$ and $b=3.0$ for $c=2$.",
    "inputs": "p=0.6, c∈{0.5,2}",
    "formula": "(1 + c) / p - c"
  },
  {
    "id": "Q11",
    "statement": "With an increased narrative reward $s'=2$, the new accuracy threshold is $p^{*}_{\\text{new}}=\\frac{s'+c}{b+c}=1.0$.",
    "inputs": "s'=2, c=1, b=2",
    "formula": "(s' + c) / (b + c)"
  },
  {
    "id": "Q12",
    "statement": "Under the same $p=0.6$ but $s'=2$, the payoff difference is $\\pi_{F}-\\pi_{P}= -1.2$.",
    "inputs": "p=0.6, b=2, c=1, s'=2",
    "formula": "p * b - (1 - p) * c - s'"
  },
  {
    "id": "Q13",
    "statement": "The replicator dynamics become $\\dot{x}= -1.2\\,x(1-x)$.",
    "inputs": "payoff difference = -1.2",
    "formula": "dot{x} = (payoff difference) * x * (1 - x)"
  }
]

## Script
```python
import math

def fmt(val, expected):
    if '.' in expected:
        nd = len(expected.split('.')[1])
        fmt_val = f"{round(val, nd):.{nd}f}"
    else:
        fmt_val = str(int(round(val)))
    return fmt_val

claims = {
    "Q1": {"calc": lambda: (1+1)/(2+1), "expected": "0.6667"},
    "Q2": {"calc": lambda: 0.6*2 - (1-0.6)*1, "expected": "0.8"},
    "Q3": {"calc": lambda: 1, "expected": "1"},
    "Q4": {"calc": lambda: (1 + (1-0.6)*1)/0.6, "expected": "2.3333"},
    "Q5": {"calc": lambda: 0.8 - 1.0, "expected": "-0.2"},
    "Q6": {"calc": lambda: - (1+1)/(2+1)**2, "expected": "-0.2222"},
    "Q7": {"calc": lambda: (2-1)/(2+1)**2, "expected": "0.1111"},
    "Q8": {"calc": lambda: 1/(2+1), "expected": "0.3333"},
    "Q9": {"calc": lambda: [(s+1)/0.6 - 1 for s in (0.5,1.0,1.5)], "expected": ["1.5","2.3333","3.1667"]},
    "Q10": {"calc": lambda: [(1+c)/0.6 - c for c in (0.5,2)], "expected": ["2.0","3.0"]},
    "Q11": {"calc": lambda: (2+1)/(2+1), "expected": "1.0"},
    "Q12": {"calc": lambda: 0.6*2 - (1-0.6)*1 - 2, "expected": "-1.2"},
    "Q13": {"calc": lambda: -1.2, "expected": "-1.2"},
}

for cid, info in claims.items():
    val = info["calc"]()
    exp = info["expected"]
    if isinstance(val, list):
        matches = []
        for v, e in zip(val, exp):
            fv = fmt(v, e)
            matches.append(fv == e)
        match = all(matches)
        computed_str = "[" + ", ".join(fmt(v, e) for v, e in zip(val, exp)) + "]"
    else:
        computed_str = fmt(val, exp)
        match = computed_str == exp
    print(f"CLAIM {cid}: computed={computed_str} expected={exp if not isinstance(exp,list) else exp} match={'yes' if match else 'no'}")

```

## Execution output
```
CLAIM Q1: computed=0.6667 expected=0.6667 match=yes
CLAIM Q2: computed=0.8 expected=0.8 match=yes
CLAIM Q3: computed=1 expected=1 match=yes
CLAIM Q4: computed=2.3333 expected=2.3333 match=yes
CLAIM Q5: computed=-0.2 expected=-0.2 match=yes
CLAIM Q6: computed=-0.2222 expected=-0.2222 match=yes
CLAIM Q7: computed=0.1111 expected=0.1111 match=yes
CLAIM Q8: computed=0.3333 expected=0.3333 match=yes
CLAIM Q9: computed=[1.5, 2.3333, 3.1667] expected=['1.5', '2.3333', '3.1667'] match=yes
CLAIM Q10: computed=[2.0, 3.0] expected=['2.0', '3.0'] match=yes
CLAIM Q11: computed=1.0 expected=1.0 match=yes
CLAIM Q12: computed=-1.2 expected=-1.2 match=yes
CLAIM Q13: computed=-1.2 expected=-1.2 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.6667 | 0.6667 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 0.8 | 0.8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 2.3333 | 2.3333 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | -0.2 | -0.2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | -0.2222 | -0.2222 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 0.1111 | 0.1111 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 0.3333 | 0.3333 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 1.0 | 1.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | -1.2 | -1.2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | -1.2 | -1.2 | yes | match | 3 significant digits (as printed, at least 3) |

Mismatches: 0 of 11.
