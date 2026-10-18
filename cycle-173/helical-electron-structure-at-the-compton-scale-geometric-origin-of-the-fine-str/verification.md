# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Reduced Compton wavelength from the Compton wavelength, Eq. (8): lambda_bar_C = lambda_C/(2*pi) = 3.8611e-13 m",
    "inputs": "lambda_C = 2.426e-12 m; 2*pi = 6.2831853072; mantissa check 6.2831853072*0.38611 = 2.42600",
    "formula": "lambda_bar_C = 2.426e-12 / (2*3.1415926536)"
  },
  {
    "id": "Q2",
    "statement": "Classical electron radius, Eq. (9): r_e = alpha*lambda_bar_C = 2.818e-15 m",
    "inputs": "alpha = 7.2973525693e-3; lambda_bar_C = 3.8611e-13 m",
    "formula": "r_e = 7.2973525693e-3 * 3.8611e-13"
  },
  {
    "id": "Q3",
    "statement": "Geometric correction to the anomaly, Eq. (10): delta_geom = alpha^2 = 5.325e-5",
    "inputs": "alpha = 7.2973525693e-3",
    "formula": "delta_geom = (7.2973525693e-3)^2"
  },
  {
    "id": "Q4",
    "statement": "One-loop QED contribution, Eq. (11): alpha/pi = 2.32282e-3",
    "inputs": "alpha = 7.2973525693e-3; pi = 3.1415926536; check 3.1415926536*2.32282 = 7.29735",
    "formula": "(7.2973525693e-3)/3.1415926536"
  },
  {
    "id": "Q5",
    "statement": "Total predicted g-factor, Eq. (12): g = 2*(1 + alpha/pi + alpha^2) = 2.004752",
    "inputs": "alpha/pi = 2.32282e-3; alpha^2 = 5.325135e-5",
    "formula": "g = 2*(1 + 2.32282e-3 + 5.325135e-5)"
  },
  {
    "id": "Q6",
    "statement": "Deviation from QED, Eq. (13): Delta g = g - g_QED = 2.433e-3",
    "inputs": "g = 2.00475214; g_QED = 2.002319",
    "formula": "Delta g = 2.00475214 - 2.002319"
  },
  {
    "id": "Q7",
    "statement": "Form-factor test momentum, Eq. (14): q = 1/lambda_C = 4.122e11 m^-1",
    "inputs": "lambda_C = 2.426e-12 m; check 1/2.426 = 0.41220",
    "formula": "q = 1/(2.426e-12)"
  },
  {
    "id": "Q8",
    "statement": "ratio of Delta g to part-per-billion relative precision (Discussion): about 1.2e6",
    "inputs": "Delta g (fractional) = 1.2e-3; assumed precision = 1e-9",
    "formula": "1.2e-3 / 1e-9"
  },
  {
    "id": "Q9",
    "statement": "ratio of delta_geom to omitted two-loop term (Discussion): about 10",
    "inputs": "delta_geom = 5.4e-5; (alpha/pi)^2 = 5.4e-6",
    "formula": "5.4e-5 / 5.4e-6"
  }
]

## Script
```python
import math

# Each claim is recomputed independently from its stated inputs and formula.
# "expected" carries exactly the digits the paper states, as a string, in the
# same unit as the computed value.

def sig_round(value, sig):
    """Round value to sig significant digits."""
    if value == 0:
        return 0.0
    from math import floor, log10
    exp = floor(log10(abs(value)))
    factor = 10 ** (sig - 1 - exp)
    return round(value * factor) / factor

claims = []

# Q1: lambda_bar_C = lambda_C/(2*pi) = 3.8611e-13
lam_C = 2.426e-12
two_pi = 2 * 3.1415926536
comp = lam_C / two_pi
expected = 3.8611e-13
claims.append(("Q1", comp, expected, 5))  # paper states 3.8611 (5 sig figs)

# Q2: r_e = alpha * lambda_bar_C = 2.818e-15
alpha = 7.2973525693e-3
lam_bar = 3.8611e-13
comp = alpha * lam_bar
expected = 2.818e-15
claims.append(("Q2", comp, expected, 4))  # paper states 2.818 (4 sig figs)

# Q3: delta_geom = alpha^2 = 5.325e-5
comp = alpha ** 2
expected = 5.325e-5
claims.append(("Q3", comp, expected, 4))  # paper states 5.325 (4 sig figs)

# Q4: alpha/pi = 2.32282e-3
pi_val = 3.1415926536
comp = alpha / pi_val
expected = 2.32282e-3
claims.append(("Q4", comp, expected, 6))  # paper states 2.32282 (6 sig figs)

# Q5: g = 2*(1 + alpha/pi + alpha^2) using paper's intermediate values
ap = 2.32282e-3
a2 = 5.325135e-5
comp = 2 * (1 + ap + a2)
expected = 2.004752
claims.append(("Q5", comp, expected, 7))  # paper states 2.004752 (7 sig figs)

# Q6: Delta g = 2.00475214 - 2.002319
comp = 2.00475214 - 2.002319
expected = 2.433e-3
claims.append(("Q6", comp, expected, 4))  # paper states 2.433 (4 sig figs)

# Q7: q = 1/lambda_C = 4.122e11
comp = 1.0 / lam_C
expected = 4.122e11
claims.append(("Q7", comp, expected, 4))  # paper states 4.122 (4 sig figs)

# Q8: ratio Delta g (fractional) 1.2e-3 / 1e-9 = 1.2e6
comp = 1.2e-3 / 1e-9
expected = 1.2e6
claims.append(("Q8", comp, expected, 2))  # paper states 1.2 (2 sig figs)

# Q9: ratio 5.4e-5 / 5.4e-6 = 10 (about 10)
comp = 5.4e-5 / 5.4e-6
expected = 10.0
claims.append(("Q9", comp, expected, 1))  # paper states "about 10"

n_match = 0
n_mismatch = 0
for cid, computed, exp, sig in claims:
    rounded = sig_round(computed, sig)
    # compare rounded computed to expected within tolerance set by stated precision
    if exp is None:
        match = "no"
    else:
        # tolerance: half unit in the last stated significant digit
        from math import floor, log10
        if exp != 0:
            exp_digits = sig
            exp_exp = floor(log10(abs(float(exp))))
            tol = 0.5 * 10 ** (exp_exp - exp_digits + 1)
        else:
            tol = 0.0
        match = "yes" if abs(computed - float(exp)) <= tol else "no"
    if match == "yes":
        n_match += 1
    else:
        n_mismatch += 1
    print(f"CLAIM {cid}: computed={computed:.10g} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {n_match} match, {n_mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=3.861098919e-13 expected=3.8611e-13 match=yes
CLAIM Q2: computed=2.817580801e-15 expected=2.818e-15 match=yes
CLAIM Q3: computed=5.325135452e-05 expected=5.325e-05 match=yes
CLAIM Q4: computed=0.002322819466 expected=0.00232282 match=yes
CLAIM Q5: computed=2.004752143 expected=2.004752 match=yes
CLAIM Q6: computed=0.00243314 expected=0.002433 match=yes
CLAIM Q7: computed=4.122011542e+11 expected=412200000000.0 match=yes
CLAIM Q8: computed=1200000 expected=1200000.0 match=yes
CLAIM Q9: computed=10 expected=10.0 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3.861098919e-13 | 3.8611e-13 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 2.817580801e-15 | 2.818e-15 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 5.325135452e-05 | 5.325e-05 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 0.002322819466 | 0.00232282 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q5 | 2.004752143 | 2.004752 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q6 | 0.00243314 | 0.002433 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 4.122011542e+11 | 412200000000.0 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 1200000 | 1200000.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 10 | 10.0 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 9.
