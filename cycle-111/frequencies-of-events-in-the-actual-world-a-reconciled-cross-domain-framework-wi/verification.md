# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Radix-locked angular frequency omega_2 = 9.064722",
    "inputs": "2*pi = 6.283185; ln 2 = 0.693147",
    "formula": "omega_2 = 2*pi / ln(2)"
  },
  {
    "id": "Q2",
    "statement": "Radix-locked angular frequency omega_3 = 5.719203",
    "inputs": "2*pi = 6.283185; ln 3 = 1.098612",
    "formula": "omega_3 = 2*pi / ln(3)"
  },
  {
    "id": "Q3",
    "statement": "Radix-locked angular frequency omega_5 = 3.903962",
    "inputs": "2*pi = 6.283185; ln 5 = 1.609438",
    "formula": "omega_5 = 2*pi / ln(5)"
  },
  {
    "id": "Q4",
    "statement": "Radix-locked angular frequency omega_7 = 3.228919",
    "inputs": "2*pi = 6.283185; ln 7 = 1.945910",
    "formula": "omega_7 = 2*pi / ln(7)"
  },
  {
    "id": "Q5",
    "statement": "Arithmetic mean of omega_p = 5.479201",
    "inputs": "omega_2 = 9.064722; omega_3 = 5.719203; omega_5 = 3.903962; omega_7 = 3.228919",
    "formula": "mean = (omega_2 + omega_3 + omega_5 + omega_7) / 4"
  },
  {
    "id": "Q6",
    "statement": "Ratio omega_2/omega_3 = log_2 3 = 1.584962",
    "inputs": "ln 3 = 1.098612; ln 2 = 0.693147",
    "formula": "ratio = ln(3) / ln(2)"
  },
  {
    "id": "Q7",
    "statement": "Ratio omega_2/omega_5 = log_2 5 = 2.321929",
    "inputs": "ln 5 = 1.609438; ln 2 = 0.693147",
    "formula": "ratio = ln(5) / ln(2)"
  },
  {
    "id": "Q8",
    "statement": "Ratio omega_3/omega_5 = log_3 5 = 1.464974",
    "inputs": "ln 5 = 1.609438; ln 3 = 1.098612",
    "formula": "ratio = ln(5) / ln(3)"
  }
]

## Script
```python
import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

two_pi = 6.283185
ln2 = 0.693147
ln3 = 1.098612
ln5 = 1.609438
ln7 = 1.945910

# Q1: omega_2 = 2*pi / ln(2)
w2 = two_pi / ln2
print(f"CLAIM Q1: computed={w2:.6f} expected=9.064722 match={'yes' if close(w2, 9.064722) else 'no'}")

# Q2: omega_3 = 2*pi / ln(3)
w3 = two_pi / ln3
print(f"CLAIM Q2: computed={w3:.6f} expected=5.719203 match={'yes' if close(w3, 5.719203) else 'no'}")

# Q3: omega_5 = 2*pi / ln(5)
w5 = two_pi / ln5
print(f"CLAIM Q3: computed={w5:.6f} expected=3.903962 match={'yes' if close(w5, 3.903962) else 'no'}")

# Q4: omega_7 = 2*pi / ln(7)
w7 = two_pi / ln7
print(f"CLAIM Q4: computed={w7:.6f} expected=3.228919 match={'yes' if close(w7, 3.228919) else 'no'}")

# Q5: mean of omega_p
mean_w = (w2 + w3 + w5 + w7) / 4
print(f"CLAIM Q5: computed={mean_w:.6f} expected=5.479201 match={'yes' if close(mean_w, 5.479201) else 'no'}")

# Q6: omega_2/omega_3 = ln3/ln2
r23 = ln3 / ln2
print(f"CLAIM Q6: computed={r23:.6f} expected=1.584962 match={'yes' if close(r23, 1.584962) else 'no'}")

# Q7: omega_2/omega_5 = ln5/ln2
r25 = ln5 / ln2
print(f"CLAIM Q7: computed={r25:.6f} expected=2.321929 match={'yes' if close(r25, 2.321929) else 'no'}")

# Q8: omega_3/omega_5 = ln5/ln3
r35 = ln5 / ln3
print(f"CLAIM Q8: computed={r35:.6f} expected=1.464974 match={'yes' if close(r35, 1.464974) else 'no'}")

claims = [close(w2,9.064722), close(w3,5.719203), close(w5,3.903962), close(w7,3.228919),
          close(mean_w,5.479201), close(r23,1.584962), close(r25,2.321929), close(r35,1.464974)]
n = len(claims)
m = sum(claims)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=9.064722 expected=9.064722 match=yes
CLAIM Q2: computed=5.719203 expected=5.719203 match=yes
CLAIM Q3: computed=3.903962 expected=3.903962 match=yes
CLAIM Q4: computed=3.228919 expected=3.228919 match=yes
CLAIM Q5: computed=5.479201 expected=5.479201 match=yes
CLAIM Q6: computed=1.584962 expected=1.584962 match=yes
CLAIM Q7: computed=2.321929 expected=2.321929 match=yes
CLAIM Q8: computed=1.464974 expected=1.464974 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
