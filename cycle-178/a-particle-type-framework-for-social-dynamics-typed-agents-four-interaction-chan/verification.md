# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Critical lepton seed fraction with mediation is $f_L^{\\text{crit}} = 0.19231$.",
    "inputs": "theta = 0.2, k_bar = 10, w_L = 0.08, mu = 3, f_M = 0.10",
    "formula": "f_L^{crit} = theta / (k_bar * w_L * (1 + mu * f_M))"
  },
  {
    "id": "Q2",
    "statement": "Critical lepton seed fraction without mediation is $0.25$.",
    "inputs": "theta = 0.2, k_bar = 10, w_L = 0.08",
    "formula": "f_{crit}^{no\\,med} = theta / (k_bar * w_L)"
  },
  {
    "id": "Q3",
    "statement": "Relative reduction of required seed fraction due to mediation is $0.2308$ (23.08%).",
    "inputs": "f_{crit}^{no\\,med} = 0.25, f_L^{crit} = 0.19231",
    "formula": "(f_{crit}^{no\\,med} - f_L^{crit}) / f_{crit}^{no\\,med}"
  },
  {
    "id": "Q4",
    "statement": "Critical seed fraction for the homogeneous baseline is $f_h^{\\text{crit}} = 0.6667$.",
    "inputs": "theta = 0.2, k_bar = 10, w_h = 0.03",
    "formula": "f_h^{crit} = theta / (k_bar * w_h)"
  },
  {
    "id": "Q5",
    "statement": "Typed‑to‑homogeneous seed‑fraction ratio is $3.467$.",
    "inputs": "f_h^{crit} = 0.6667, f_L^{crit} = 0.19231",
    "formula": "ratio = f_h^{crit} / f_L^{crit}"
  },
  {
    "id": "Q6",
    "statement": "Baryon conversion probability over 100 days is $p_B = 0.39347$.",
    "inputs": "lambda_w = 1e-2, g_B = 0.5, T = 100",
    "formula": "p_B = 1 - exp(-lambda_w * g_B * T)"
  },
  {
    "id": "Q7",
    "statement": "Lepton conversion probability over 100 days is $p_L = 0.09516$.",
    "inputs": "lambda_w = 1e-2, g_L = 0.1, T = 100",
    "formula": "p_L = 1 - exp(-lambda_w * g_L * T)"
  },
  {
    "id": "Q8",
    "statement": "Ratio of baryon to lepton conversion probabilities is $4.134$.",
    "inputs": "p_B = 0.39347, p_L = 0.09516",
    "formula": "p_B / p_L"
  },
  {
    "id": "Q9",
    "statement": "Number of baryons in the population is $N_B = 40$.",
    "inputs": "f_B = 0.04, N = 1000",
    "formula": "N_B = f_B * N"
  },
  {
    "id": "Q10",
    "statement": "Converted baryons after 100 days are $N_B^{\\text{conv}} = 15.74$.",
    "inputs": "N_B = 40, p_B = 0.39347",
    "formula": "N_B^{conv} = N_B * p_B"
  },
  {
    "id": "Q11",
    "statement": "Projected second‑order adopters from converted baryons are $N^{(2)} = 78.70$.",
    "inputs": "N_B^{conv} = 15.74, k_bar = 10, q = 0.5",
    "formula": "N^{(2)} = N_B^{conv} * k_bar * q"
  },
  {
    "id": "Q12",
    "statement": "Observed fraction of the population is $f_{\\text{obs}} = 0.34$.",
    "inputs": "f_D = 0.66",
    "formula": "f_{obs} = 1 - f_D"
  },
  {
    "id": "Q13",
    "statement": "Bias factor between true and observed reach is $2.9412$.",
    "inputs": "f_{obs} = 0.34",
    "formula": "bias = 1 / f_{obs}"
  },
  {
    "id": "Q14",
    "statement": "Number of extra parameters in the typed model is $\\Delta k = 60$.",
    "inputs": "typed parameters = 64, homogeneous parameters = 4",
    "formula": "Delta k = 64 - 4"
  },
  {
    "id": "Q15",
    "statement": "AIC break‑even log‑likelihood gain required is $60$.",
    "inputs": "Delta k = 60",
    "formula": "gain_{AIC} = Delta k"
  },
  {
    "id": "Q16",
    "statement": "BIC break‑even log‑likelihood gain required is $207.24$.",
    "inputs": "Delta k = 60, n = 1000, ln n = 6.90776",
    "formula": "gain_{BIC} = (Delta k * ln n) / 2"
  }
]

## Script
```python
import math

def fmt(val, fmt_str):
    return format(val, fmt_str)

# Expected values as strings
expected = {
    "Q1": "0.19231",
    "Q2": "0.25",
    "Q3": "0.2308",
    "Q4": "0.6667",
    "Q5": "3.467",
    "Q6": "0.39347",
    "Q7": "0.09516",
    "Q8": "4.134",
    "Q9": "40",
    "Q10": "15.74",
    "Q11": "78.70",
    "Q12": "0.34",
    "Q13": "2.9412",
    "Q14": "60",
    "Q15": "60",
    "Q16": "207.24",
}

# Computations
theta = 0.2
k_bar = 10
w_L = 0.08
mu = 3
f_M = 0.10
w_h = 0.03
lambda_w = 1e-2
g_B = 0.5
g_L = 0.1
T = 100
f_B = 0.04
N = 1000
f_D = 0.66
q = 0.5
ln_n = 6.90776
delta_k = 60
n = 1000

# Q1
f_L_crit = theta / (k_bar * w_L * (1 + mu * f_M))
c1 = fmt(f_L_crit, ".5f")
print(f"CLAIM Q1: computed={c1} expected={expected['Q1']} match={'yes' if c1==expected['Q1'] else 'no'}")

# Q2
f_no_med = theta / (k_bar * w_L)
c2 = fmt(f_no_med, ".2f")
print(f"CLAIM Q2: computed={c2} expected={expected['Q2']} match={'yes' if c2==expected['Q2'] else 'no'}")

# Q3
rel_red = (f_no_med - f_L_crit) / f_no_med
c3 = fmt(rel_red, ".4f")
print(f"CLAIM Q3: computed={c3} expected={expected['Q3']} match={'yes' if c3==expected['Q3'] else 'no'}")

# Q4
f_h_crit = theta / (k_bar * w_h)
c4 = fmt(f_h_crit, ".4f")
print(f"CLAIM Q4: computed={c4} expected={expected['Q4']} match={'yes' if c4==expected['Q4'] else 'no'}")

# Q5
ratio = f_h_crit / f_L_crit
c5 = fmt(ratio, ".3f")
print(f"CLAIM Q5: computed={c5} expected={expected['Q5']} match={'yes' if c5==expected['Q5'] else 'no'}")

# Q6
p_B = 1 - math.exp(-lambda_w * g_B * T)
c6 = fmt(p_B, ".5f")
print(f"CLAIM Q6: computed={c6} expected={expected['Q6']} match={'yes' if c6==expected['Q6'] else 'no'}")

# Q7
p_L = 1 - math.exp(-lambda_w * g_L * T)
c7 = fmt(p_L, ".5f")
print(f"CLAIM Q7: computed={c7} expected={expected['Q7']} match={'yes' if c7==expected['Q7'] else 'no'}")

# Q8
ratio_pb_pl = p_B / p_L
c8 = fmt(ratio_pb_pl, ".3f")
print(f"CLAIM Q8: computed={c8} expected={expected['Q8']} match={'yes' if c8==expected['Q8'] else 'no'}")

# Q9
N_B = f_B * N
c9 = fmt(N_B, ".0f")
print(f"CLAIM Q9: computed={c9} expected={expected['Q9']} match={'yes' if c9==expected['Q9'] else 'no'}")

# Q10
N_B_conv = N_B * p_B
c10 = fmt(N_B_conv, ".2f")
print(f"CLAIM Q10: computed={c10} expected={expected['Q10']} match={'yes' if c10==expected['Q10'] else 'no'}")

# Q11
N2 = 15.74 * k_bar * q  # using the given rounded N_B^{conv}=15.74
c11 = fmt(N2, ".2f")
print(f"CLAIM Q11: computed={c11} expected={expected['Q11']} match={'yes' if c11==expected['Q11'] else 'no'}")

# Q12
f_obs = 1 - f_D
c12 = fmt(f_obs, ".2f")
print(f"CLAIM Q12: computed={c12} expected={expected['Q12']} match={'yes' if c12==expected['Q12'] else 'no'}")

# Q13
bias = 1 / f_obs
c13 = fmt(bias, ".4f")
print(f"CLAIM Q13: computed={c13} expected={expected['Q13']} match={'yes' if c13==expected['Q13'] else 'no'}")

# Q14
c14 = fmt(delta_k, ".0f")
print(f"CLAIM Q14: computed={c14} expected={expected['Q14']} match={'yes' if c14==expected['Q14'] else 'no'}")

# Q15
gain_AIC = delta_k
c15 = fmt(gain_AIC, ".0f")
print(f"CLAIM Q15: computed={c15} expected={expected['Q15']} match={'yes' if c15==expected['Q15'] else 'no'}")

# Q16
gain_BIC = (delta_k * ln_n) / 2
c16 = fmt(gain_BIC, ".2f")
print(f"CLAIM Q16: computed={c16} expected={expected['Q16']} match={'yes' if c16==expected['Q16'] else 'no'}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for k in expected if eval('c'+k[-1])==expected[k])} match, {sum(1 for k in expected if eval('c'+k[-1])!=expected[k])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.19231 expected=0.19231 match=yes
CLAIM Q2: computed=0.25 expected=0.25 match=yes
CLAIM Q3: computed=0.2308 expected=0.2308 match=yes
CLAIM Q4: computed=0.6667 expected=0.6667 match=yes
CLAIM Q5: computed=3.467 expected=3.467 match=yes
CLAIM Q6: computed=0.39347 expected=0.39347 match=yes
CLAIM Q7: computed=0.09516 expected=0.09516 match=yes
CLAIM Q8: computed=4.135 expected=4.134 match=no
CLAIM Q9: computed=40 expected=40 match=yes
CLAIM Q10: computed=15.74 expected=15.74 match=yes
CLAIM Q11: computed=78.70 expected=78.70 match=yes
CLAIM Q12: computed=0.34 expected=0.34 match=yes
CLAIM Q13: computed=2.9412 expected=2.9412 match=yes
CLAIM Q14: computed=60 expected=60 match=yes
CLAIM Q15: computed=60 expected=60 match=yes
CLAIM Q16: computed=207.23 expected=207.24 match=no

[stderr]
Traceback (most recent call last):
  File "<string>", line 124, in <module>
  File "<string>", line 124, in <genexpr>
  File "<string>", line 1, in <module>
NameError: name 'c0' is not defined. Did you mean: 'c1'?

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.19231 | 0.19231 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 0.25 | 0.25 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.2308 | 0.2308 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 0.6667 | 0.6667 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 3.467 | 3.467 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 0.39347 | 0.39347 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 0.09516 | 0.09516 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 4.135 | 4.134 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 40 | 40 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 15.74 | 15.74 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 78.70 | 78.70 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 0.34 | 0.34 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 2.9412 | 2.9412 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q14 | 60 | 60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 60 | 60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 207.23 | 207.24 | no | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
