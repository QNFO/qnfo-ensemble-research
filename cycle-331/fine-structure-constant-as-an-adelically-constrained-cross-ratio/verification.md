# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The empirical fine‑structure constant used as input is α_emp = 0.0072973525693.",
    "inputs": "",
    "formula": ""
  },
  {
    "id": "Q2",
    "statement": "For the exponent triple (a,b,c) = (4,2,0) the model predicts α_model = 1/(2^4·3^2·5^0) = 1/144 ≈ 0.00694444.",
    "inputs": "a=4, b=2, c=0",
    "formula": "α_model = 1/(2^a * 3^b * 5^c)"
  },
  {
    "id": "Q3",
    "statement": "The difference between empirical and model values is Δ = α_emp – α_model = 0.0003529081249.",
    "inputs": "α_emp = 0.0072973525693, α_model = 0.0069444444444",
    "formula": "Δ = α_emp - α_model"
  },
  {
    "id": "Q4",
    "statement": "The relative error of the model is ε = Δ / α_emp ≈ 0.0483 (4.83%).",
    "inputs": "Δ = 0.0003529081249, α_emp = 0.0072973525693",
    "formula": "ε = Δ / α_emp"
  },
  {
    "id": "Q5",
    "statement": "For (a,b,c) = (1,0,0) the model gives α = 1/2 = 0.5 and relative error ε ≈ 67.52.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^1·3^0·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q6",
    "statement": "For (a,b,c) = (2,0,0) the model gives α = 1/4 = 0.25 and relative error ε ≈ 33.26.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^2·3^0·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q7",
    "statement": "For (a,b,c) = (0,1,0) the model gives α = 1/3 ≈ 0.33333 and relative error ε ≈ 44.68.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^0·3^1·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q8",
    "statement": "For (a,b,c) = (3,0,0) the model gives α = 1/8 = 0.125 and relative error ε ≈ 16.13.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^3·3^0·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q9",
    "statement": "For (a,b,c) = (1,1,0) the model gives α = 1/(2·3) = 1/6 ≈ 0.166667 and relative error ε ≈ 21.84.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^1·3^1·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q10",
    "statement": "For (a,b,c) = (4,0,0) the model gives α = 1/16 = 0.0625 and relative error ε ≈ 7.56.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^4·3^0·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q11",
    "statement": "For (a,b,c) = (2,1,0) the model gives α = 1/(4·3) = 1/12 ≈ 0.08333 and relative error ε ≈ 10.42.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^2·3^1·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q12",
    "statement": "For (a,b,c) = (0,2,0) the model gives α = 1/9 ≈ 0.111111 and relative error ε ≈ 14.23.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^0·3^2·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q13",
    "statement": "For (a,b,c) = (5,0,0) the model gives α = 1/32 = 0.03125 and relative error ε ≈ 3.28.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^5·3^0·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q14",
    "statement": "For (a,b,c) = (3,1,0) the model gives α = 1/(8·3) = 1/24 ≈ 0.0416667 and relative error ε ≈ 4.71.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^3·3^1·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q15",
    "statement": "For (a,b,c) = (1,2,0) the model gives α = 1/(2·9) = 1/18 ≈ 0.0555556 and relative error ε ≈ 6.61.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^1·3^2·5^0); ε = |α_emp-α|/α_emp"
  },
  {
    "id": "Q16",
    "statement": "For (a,b,c) = (4,1,0) the model gives α = 1/(16·3) = 1/48 ≈ 0.0208333 and relative error ε ≈ 1.86.",
    "inputs": "α_emp = 0.0072973525693",
    "formula": "α = 1/(2^4·3^1·5^0); ε = |α_emp-α|/α_emp"
  }
]

## Script
```python
import math

# Empirical fine-structure constant used as input
alpha_emp = 0.0072973525693

def round_to_str(val, target):
    """Round val to the same number of decimal places as target string."""
    if '.' in target:
        nd = len(target.split('.')[1])
        fmt = f"{{:.{nd}f}}"
        return fmt.format(round(val, nd))
    else:
        return str(int(round(val)))

def claim(id_, computed, expected):
    comp_str = f"{computed:.12g}" if isinstance(computed, float) else str(computed)
    # Determine if expected is a numeric string
    try:
        # count decimal places in expected
        expected_str = str(expected)
        rounded = round_to_str(computed, expected_str)
        match = "yes" if rounded == expected_str else "no"
    except Exception:
        match = "no"
        rounded = comp_str
    print(f"CLAIM {id_}: computed={rounded} expected={expected} match={match}")

# Q1
claim("Q1", alpha_emp, "0.0072973525693")

# Q2
alpha_model = 1 / (2**4 * 3**2 * 5**0)  # 1/144
claim("Q2", alpha_model, "0.00694444")

# Q3
delta = alpha_emp - alpha_model
claim("Q3", delta, "0.0003529081249")

# Q4
epsilon = delta / alpha_emp
claim("Q4", epsilon, "0.0483")

# Helper to compute model alpha and relative error for given exponents
def compute_error(a, b, c):
    model = 1 / (2**a * 3**b * 5**c)
    rel_err = abs(alpha_emp - model) / alpha_emp
    return model, rel_err

# Q5
model, rel = compute_error(1,0,0)
claim("Q5", rel, "67.52")

# Q6
model, rel = compute_error(2,0,0)
claim("Q6", rel, "33.26")

# Q7
model, rel = compute_error(0,1,0)
claim("Q7", rel, "44.68")

# Q8
model, rel = compute_error(3,0,0)
claim("Q8", rel, "16.13")

# Q9
model, rel = compute_error(1,1,0)
claim("Q9", rel, "21.84")

# Q10
model, rel = compute_error(4,0,0)
claim("Q10", rel, "7.56")

# Q11
model, rel = compute_error(2,1,0)
claim("Q11", rel, "10.42")

# Q12
model, rel = compute_error(0,2,0)
claim("Q12", rel, "14.23")

# Q13
model, rel = compute_error(5,0,0)
claim("Q13", rel, "3.28")

# Q14
model, rel = compute_error(3,1,0)
claim("Q14", rel, "4.71")

# Q15
model, rel = compute_error(1,2,0)
claim("Q15", rel, "6.61")

# Q16
model, rel = compute_error(4,1,0)
claim("Q16", rel, "1.86")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for i in range(1,17) if True) - sum(1 for line in open(__file__) if 'match=no' in line)} match, {sum(1 for line in open(__file__) if 'match=no' in line)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.0072973525693 expected=0.0072973525693 match=yes
CLAIM Q2: computed=0.00694444 expected=0.00694444 match=yes
CLAIM Q3: computed=0.0003529081249 expected=0.0003529081249 match=yes
CLAIM Q4: computed=0.0484 expected=0.0483 match=no
CLAIM Q5: computed=67.52 expected=67.52 match=yes
CLAIM Q6: computed=33.26 expected=33.26 match=yes
CLAIM Q7: computed=44.68 expected=44.68 match=yes
CLAIM Q8: computed=16.13 expected=16.13 match=yes
CLAIM Q9: computed=21.84 expected=21.84 match=yes
CLAIM Q10: computed=7.56 expected=7.56 match=yes
CLAIM Q11: computed=10.42 expected=10.42 match=yes
CLAIM Q12: computed=14.23 expected=14.23 match=yes
CLAIM Q13: computed=3.28 expected=3.28 match=yes
CLAIM Q14: computed=4.71 expected=4.71 match=yes
CLAIM Q15: computed=6.61 expected=6.61 match=yes
CLAIM Q16: computed=1.85 expected=1.86 match=no

[stderr]
Traceback (most recent call last):
  File "<string>", line 97, in <module>
NameError: name '__file__' is not defined. Did you mean: '__name__'?

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.0072973525693 | 0.0072973525693 | yes | match | 11 significant digits (as the paper states, at least 2) |
| Q2 | 0.00694444 | 0.00694444 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q3 | 0.0003529081249 | 0.0003529081249 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q4 | 0.0484 | 0.0483 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 67.52 | 67.52 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 33.26 | 33.26 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 44.68 | 44.68 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 16.13 | 16.13 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 21.84 | 21.84 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 7.56 | 7.56 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 10.42 | 10.42 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 14.23 | 14.23 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 3.28 | 3.28 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 4.71 | 4.71 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 6.61 | 6.61 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 1.85 | 1.86 | no | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
