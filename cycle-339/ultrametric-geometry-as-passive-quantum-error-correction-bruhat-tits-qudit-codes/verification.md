# Verification report

## Extracted claims
[
  {
    "id": "C1",
    "statement": "The number of physical qudits in a ball of radius $t$ is $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$.",
    "inputs": "branching prime $p$, radius $t$",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p - 1)"
  },
  {
    "id": "C2",
    "statement": "For $p=3$ and $t=1$, the ball contains $n_1 = 5$ qudits.",
    "inputs": "p=3, t=1",
    "formula": "n_1 = 1 + (3+1)*(3^1 - 1)/(3 - 1) = 5"
  },
  {
    "id": "C3",
    "statement": "For $p=3$ and $t=2$, the ball contains $n_2 = 17$ qudits.",
    "inputs": "p=3, t=2",
    "formula": "n_2 = 1 + (3+1)*(3^2 - 1)/(3 - 1) = 17"
  },
  {
    "id": "C4",
    "statement": "For $p=3$ and $t=3$, the ball contains $n_3 = 53$ qudits.",
    "inputs": "p=3, t=3",
    "formula": "n_3 = 1 + (3+1)*(3^3 - 1)/(3 - 1) = 53"
  },
  {
    "id": "C5",
    "statement": "For $p=2$ and $t=1$, the ball contains $n_1 = 4$ qudits.",
    "inputs": "p=2, t=1",
    "formula": "n_1 = 1 + (2+1)*(2^1 - 1)/(2 - 1) = 4"
  },
  {
    "id": "C6",
    "statement": "For $p=2$ and $t=2$, the ball contains $n_2 = 10$ qudits.",
    "inputs": "p=2, t=2",
    "formula": "n_2 = 1 + (2+1)*(2^2 - 1)/(2 - 1) = 10"
  },
  {
    "id": "C7",
    "statement": "For $p=2$ and $t=3$, the ball contains $n_3 = 22$ qudits.",
    "inputs": "p=2, t=3",
    "formula": "n_3 = 1 + (2+1)*(2^3 - 1)/(2 - 1) = 22"
  },
  {
    "id": "C8",
    "statement": "The code distance is $d = 2t + 1$.",
    "inputs": "radius $t$",
    "formula": "d = 2*t + 1"
  },
  {
    "id": "C9",
    "statement": "For $p=3$, $t=1$ the distance is $d = 3$.",
    "inputs": "t=1",
    "formula": "d = 2*1 + 1 = 3"
  },
  {
    "id": "C10",
    "statement": "For $p=3$, $t=1$ the correctable error weight is $t_{\\mathrm{corr}} = \\lfloor (d-1)/2 \\rfloor = 1$.",
    "inputs": "d=3",
    "formula": "t_corr = floor((d - 1)/2) = floor((3 - 1)/2) = 1"
  },
  {
    "id": "C11",
    "statement": "The rate of the $p=3$, $t=1$ block is $1/5$.",
    "inputs": "n_1 = 5",
    "formula": "rate = 1 / n_1 = 1/5"
  },
  {
    "id": "C12",
    "statement": "The passive logical failure probability for $p=3$, $t=1$ under independent depolarising noise with per‑qudit error rate $\\varepsilon$ is $P_{\\mathrm{pass}} = 1-(1-\\varepsilon)^{5} - 5\\varepsilon(1-\\varepsilon)^{4}$.",
    "inputs": "per‑qudit error rate $\\varepsilon$, $n_1=5$",
    "formula": "P_pass = 1 - (1-ε)^5 - 5*ε*(1-ε)^4"
  },
  {
    "id": "C13",
    "statement": "With $\\varepsilon = 10^{-3}$ the passive failure probability is $P_{\\mathrm{pass}} \\approx 9.98\\times10^{-6}$.",
    "inputs": "ε = 10^{-3}",
    "formula": "P_pass = 1 - (1-0.001)^5 - 5*0.001*(1-0.001)^4 ≈ 9.98e-6"
  },
  {
    "id": "C14",
    "statement": "The suppression factor relative to an unencoded qudit is $\\varepsilon / P_{\\mathrm{pass}} \\approx 100.2$.",
    "inputs": "ε = 10^{-3}, P_pass ≈ 9.98×10^{-6}",
    "formula": "suppression = ε / P_pass ≈ 0.001 / 9.98e-6 ≈ 100.2"
  },
  {
    "id": "C15",
    "statement": "For $p=3$, $t=2$ the passive failure probability is $P_{\\mathrm{pass}}^{(2)} \\approx 6.73\\times10^{-7}$.",
    "inputs": "ε = 10^{-3}, n_2 = 17",
    "formula": "P_pass^(2) ≈ C(17,3)*ε^3*(1-ε)^{14} + correction ≈ 6.73e-7"
  },
  {
    "id": "C16",
    "statement": "The effective per‑qudit error for the active baseline is $\\varepsilon_{\\mathrm{eff}} = 1-(1-\\varepsilon)^{2} = 1.999\\times10^{-3}$.",
    "inputs": "ε = 10^{-3}",
    "formula": "ε_eff = 1 - (1-ε)^2 = 1 - 0.999^2 = 1.999e-3"
  }
]

## Script
```python
import math

def claim_line(cid, computed, expected):
    match = "yes" if expected == "" else ("yes" if round(computed, len(expected.split('e')[-1]) if 'e' in expected else len(expected.split('.')[-1])) == float(expected) else "no")
    print(f"CLAIM {cid}: computed={computed:.9g} expected={expected} match={match}")

# C1: generic formula, no numeric expected
# We'll just compute for a sample p=5, t=2 to demonstrate the formula
p, t = 5, 2
C1 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C1", C1, "")

# C2
p, t = 3, 1
C2 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C2", C2, "5")

# C3
p, t = 3, 2
C3 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C3", C3, "17")

# C4
p, t = 3, 3
C4 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C4", C4, "53")

# C5
p, t = 2, 1
C5 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C5", C5, "4")

# C6
p, t = 2, 2
C6 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C6", C6, "10")

# C7
p, t = 2, 3
C7 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C7", C7, "22")

# C8: distance formula, no numeric expected
t = 4
C8 = 2 * t + 1
claim_line("C8", C8, "")

# C9
t = 1
C9 = 2 * t + 1
claim_line("C9", C9, "3")

# C10
d = 3
C10 = math.floor((d - 1) / 2)
claim_line("C10", C10, "1")

# C11
n1 = 5
C11 = 1 / n1
claim_line("C11", C11, "0.2")

# C12: formula, no numeric expected
eps = 0.001
C12 = 1 - (1 - eps)**5 - 5 * eps * (1 - eps)**4
claim_line("C12", C12, "")

# C13
eps = 0.001
C13 = 1 - (1 - eps)**5 - 5 * eps * (1 - eps)**4
claim_line("C13", C13, "9.98e-6")

# C14
eps = 0.001
P_pass = 1 - (1 - eps)**5 - 5 * eps * (1 - eps)**4
C14 = eps / P_pass
claim_line("C14", C14, "100.2")

# C15
eps = 0.001
n2 = 17
term3 = math.comb(n2, 3) * eps**3 * (1 - eps)**14
term4 = math.comb(n2, 4) * eps**4 * (1 - eps)**13
C15 = term3 + term4
claim_line("C15", C15, "6.73e-7")

# C16
eps = 0.001
C16 = 1 - (1 - eps)**2
claim_line("C16", C16, "0.001999")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in open(__file__) if 'match=yes' in line)} match, {sum(1 for line in open(__file__) if 'match=no' in line)} mismatch")

```

## Execution output
```
CLAIM C1: computed=37 expected= match=yes
CLAIM C2: computed=5 expected=5 match=yes
CLAIM C3: computed=17 expected=17 match=yes
CLAIM C4: computed=53 expected=53 match=yes
CLAIM C5: computed=4 expected=4 match=yes
CLAIM C6: computed=10 expected=10 match=yes
CLAIM C7: computed=22 expected=22 match=yes
CLAIM C8: computed=9 expected= match=yes
CLAIM C9: computed=3 expected=3 match=yes
CLAIM C10: computed=1 expected=1 match=yes
CLAIM C11: computed=0.2 expected=0.2 match=yes
CLAIM C12: computed=9.980015e-06 expected= match=yes
CLAIM C13: computed=9.980015e-06 expected=9.98e-6 match=no
CLAIM C14: computed=100.20025 expected=100.2 match=yes
CLAIM C15: computed=6.72890878e-07 expected=6.73e-7 match=no
CLAIM C16: computed=0.001999 expected=0.001999 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 92, in <module>
NameError: name '__file__' is not defined. Did you mean: '__name__'?

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| C1 | 37 | match=yes | - | undecided | undecided: values not both numeric and no script verdict |
| C2 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C3 | 17 | 17 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C4 | 53 | 53 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C5 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C6 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C7 | 22 | 22 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C8 | 9 | match=yes | - | undecided | undecided: values not both numeric and no script verdict |
| C9 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C10 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C11 | 0.2 | 0.2 | yes | match | 3 significant digits (as printed, at least 3) |
| C12 | 9.980015e-06 | match=yes | - | undecided | undecided: values not both numeric and no script verdict |
| C13 | 9.980015e-06 | 9.98e-6 | no | match | 3 significant digits (as the paper states, at least 2) |
| C14 | 100.20025 | 100.2 | yes | match | 4 significant digits (as the paper states, at least 2) |
| C15 | 6.72890878e-07 | 6.73e-7 | no | match | 3 significant digits (as the paper states, at least 2) |
| C16 | 0.001999 | 0.001999 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16 (3 undecided).
