# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The engineering cycle time is $T_{c}=8\\,\\mu\\text{s}$.",
    "inputs": "n_p=8 (A4), tau_p=5e-7 s (A2), tau_i=5e-7 s (A3)",
    "formula": "T_c = n_p * (tau_p + tau_i)"
  },
  {
    "id": "Q2",
    "statement": "The actuation duty factor is $f=0.5$.",
    "inputs": "tau_p=5e-7 s (A2), tau_i=5e-7 s (A3)",
    "formula": "f = tau_p / (tau_p + tau_i)"
  },
  {
    "id": "Q3",
    "statement": "The number of cycles per coherence window is $N_{c}=125$.",
    "inputs": "T_2=1e-3 s (A1), T_c=8e-6 s (Q1)",
    "formula": "N_c = floor(T_2 / T_c)"
  },
  {
    "id": "Q4",
    "statement": "The accumulated error over one window is $\\epsilon_{\\text{tot}} = 1.25\\times10^{-3}$.",
    "inputs": "N_c=125 (Q3), epsilon_c=1e-5 (A5)",
    "formula": "epsilon_tot = N_c * epsilon_c"
  },
  {
    "id": "Q5",
    "statement": "The projected end‑of‑window fidelity is $F_{\\text{proj}} \\approx 0.99875$.",
    "inputs": "epsilon_tot = 1.25e-3 (Q4)",
    "formula": "F_proj = 1 - epsilon_tot"
  },
  {
    "id": "Q6",
    "statement": "The actuation update rate per endpoint is $R_{u}=2\\times10^{6}\\,\\text{s}^{-1}$.",
    "inputs": "tau_p=5e-7 s (A2)",
    "formula": "R_u = 1 / tau_p"
  },
  {
    "id": "Q7",
    "statement": "The aggregate update rate for $K=64$ endpoints is $K R_{u}=1.28\\times10^{8}\\,\\text{s}^{-1}$.",
    "inputs": "K=64 (A6), R_u=2e6 s^-1 (Q6)",
    "formula": "K * R_u"
  },
  {
    "id": "Q8",
    "statement": "For a degraded coherence $T_{2}'=1\\times10^{-4}\\,\\text{s}$ the number of cycles is $N_{c}'=12$ and the projected fidelity is $F_{\\text{proj}}'\\approx0.99988$.",
    "inputs": "T_2'=1e-4 s (assumed), T_c=8e-6 s (Q1), epsilon_c=1e-5 (A5)",
    "formula": "N_c' = floor(T_2' / T_c); epsilon_tot' = N_c' * epsilon_c; F_proj' = 1 - epsilon_tot'"
  },
  {
    "id": "Q9",
    "statement": "The maximum per‑cycle error that keeps total error below 0.01 is $\\epsilon_{c}^{\\text{max}} = 8\\times10^{-5}$.",
    "inputs": "target total error = 0.01, N_c=125 (Q3)",
    "formula": "epsilon_c_max = 0.01 / N_c"
  },
  {
    "id": "Q10",
    "statement": "The closed‑loop latency is $T_{\\text{loop}} = 1.8\\times10^{-4}\\,\\text{s}$.",
    "inputs": "T_s=1.0e-4 s (A7), T_p=2.0e-5 s (A8), T_c'=5.0e-5 s (A9), T_a=1.0e-5 s (A10)",
    "formula": "T_loop = T_s + T_p + T_c' + T_a"
  },
  {
    "id": "Q11",
    "statement": "The coherence fraction consumed is $\\eta = 0.18$.",
    "inputs": "T_loop=1.8e-4 s (Q10), T_2=1e-3 s (A1)",
    "formula": "eta = T_loop / T_2"
  },
  {
    "id": "Q12",
    "statement": "The per‑cycle control payload is $B_{\\text{cycle}} = 6.4\\times10^{4}\\,\\text{bits}$.",
    "inputs": "W=64 bits (A11), N_q=1000 (A12)",
    "formula": "B_cycle = W * N_q"
  },
  {
    "id": "Q13",
    "statement": "The transmission time for the control payload is $\\tau_{\\text{tx}} = 6.4\\times10^{-7}\\,\\text{s}$.",
    "inputs": "B_cycle=6.4e4 bits (Q12), R_{link}=1.0e11 bit/s (A13)",
    "formula": "tau_tx = B_cycle / R_link"
  },
  {
    "id": "Q14",
    "statement": "The ratio of transmission time to loop latency is $3.56\\times10^{-3}$.",
    "inputs": "tau_tx=6.4e-7 s (Q13), T_loop=1.8e-4 s (Q10)",
    "formula": "tau_tx / T_loop"
  },
  {
    "id": "Q15",
    "statement": "The re‑entry reuse ratio is $\\rho = 0.5$.",
    "inputs": "N_reuse=6, N_{tot}=12 (A15)",
    "formula": "rho = N_reuse / N_tot"
  },
  {
    "id": "Q16",
    "statement": "If component 11 is portable, the reuse ratio upper bound is $\\rho \\approx 0.583$.",
    "inputs": "N_reuse=7, N_{tot}=12 (A15)",
    "formula": "rho = 7 / 12"
  }
]

## Script
```python
import math

def compare(computed, expected):
    # simple string comparison after formatting to match expected precision
    # determine number of significant digits in expected (ignoring exponent sign)
    exp = expected.replace('-', '').replace('+', '')
    if 'e' in exp:
        mantissa, exponent = exp.split('e')
        sig = len(mantissa.replace('.', '').lstrip('0'))
    elif '.' in exp:
        sig = len(exp.replace('.', '').lstrip('0'))
    else:
        sig = len(exp.lstrip('0'))
    # format computed with same number of significant digits
    fmt = f"{{:.{sig}g}}".format(computed)
    return fmt

# Inputs
n_p = 8                # A4
tau_p = 5e-7           # A2
tau_i = 5e-7           # A3
T2 = 1e-3              # A1
epsilon_c = 1e-5       # A5
K = 64                 # A6
T_s = 1.0e-4           # A7
T_p = 2.0e-5           # A8
T_c_prime = 5.0e-5     # A9
T_a = 1.0e-5           # A10
W = 64                 # A11
N_q = 1000             # A12
R_link = 1.0e11        # A13
N_reuse = 6            # A15
N_tot = 12             # A15

# Q1
T_c = n_p * (tau_p + tau_i)
print("CLAIM Q1: computed={:.8g} expected=8e-6 match={}".format(T_c, "yes" if compare(T_c, "8e-6")== "8e-6" else "no"))

# Q2
f = tau_p / (tau_p + tau_i)
print("CLAIM Q2: computed={:.8g} expected=0.5 match={}".format(f, "yes" if compare(f, "0.5")== "0.5" else "no"))

# Q3
N_c = math.floor(T2 / T_c)
print("CLAIM Q3: computed={} expected=125 match={}".format(N_c, "yes" if N_c==125 else "no"))

# Q4
epsilon_tot = N_c * epsilon_c
print("CLAIM Q4: computed={:.8g} expected=1.25e-3 match={}".format(epsilon_tot, "yes" if compare(epsilon_tot, "1.25e-3")== "1.25e-3" else "no"))

# Q5
F_proj = 1 - epsilon_tot
print("CLAIM Q5: computed={:.8g} expected=0.99875 match={}".format(F_proj, "yes" if compare(F_proj, "0.99875")== "0.99875" else "no"))

# Q6
R_u = 1 / tau_p
print("CLAIM Q6: computed={:.8g} expected=2e6 match={}".format(R_u, "yes" if compare(R_u, "2e6")== "2e6" else "no"))

# Q7
agg_rate = K * R_u
print("CLAIM Q7: computed={:.8g} expected=1.28e8 match={}".format(agg_rate, "yes" if compare(agg_rate, "1.28e8")== "1.28e8" else "no"))

# Q8
T2_prime = 1e-4
N_c_prime = math.floor(T2_prime / T_c)
epsilon_tot_prime = N_c_prime * epsilon_c
F_proj_prime = 1 - epsilon_tot_prime
print("CLAIM Q8: computed={} expected=12 match={}".format(N_c_prime, "yes" if N_c_prime==12 else "no"))
print("CLAIM Q8: computed={:.8g} expected=0.99988 match={}".format(F_proj_prime, "yes" if compare(F_proj_prime, "0.99988")== "0.99988" else "no"))

# Q9
epsilon_c_max = 0.01 / N_c
print("CLAIM Q9: computed={:.8g} expected=8e-5 match={}".format(epsilon_c_max, "yes" if compare(epsilon_c_max, "8e-5")== "8e-5" else "no"))

# Q10
T_loop = T_s + T_p + T_c_prime + T_a
print("CLAIM Q10: computed={:.8g} expected=1.8e-4 match={}".format(T_loop, "yes" if compare(T_loop, "1.8e-4")== "1.8e-4" else "no"))

# Q11
eta = T_loop / T2
print("CLAIM Q11: computed={:.8g} expected=0.18 match={}".format(eta, "yes" if compare(eta, "0.18")== "0.18" else "no"))

# Q12
B_cycle = W * N_q
print("CLAIM Q12: computed={:.8g} expected=6.4e4 match={}".format(B_cycle, "yes" if compare(B_cycle, "6.4e4")== "6.4e4" else "no"))

# Q13
tau_tx = B_cycle / R_link
print("CLAIM Q13: computed={:.8g} expected=6.4e-7 match={}".format(tau_tx, "yes" if compare(tau_tx, "6.4e-7")== "6.4e-7" else "no"))

# Q14
ratio = tau_tx / T_loop
print("CLAIM Q14: computed={:.8g} expected=3.56e-3 match={}".format(ratio, "yes" if compare(ratio, "3.56e-3")== "3.56e-3" else "no"))

# Q15
rho = N_reuse / N_tot
print("CLAIM Q15: computed={:.8g} expected=0.5 match={}".format(rho, "yes" if compare(rho, "0.5")== "0.5" else "no"))

# Q16
rho_upper = 7 / 12
print("CLAIM Q16: computed={:.8g} expected=0.583 match={}".format(rho_upper, "yes" if compare(rho_upper, "0.583")== "0.583" else "no"))

print("VERIFICATION SUMMARY: 16 claims, {} match, {} mismatch".format(
    sum(1 for line in [
        compare(T_c, "8e-6")== "8e-6",
        compare(f, "0.5")== "0.5",
        N_c==125,
        compare(epsilon_tot, "1.25e-3")== "1.25e-3",
        compare(F_proj, "0.99875")== "0.99875",
        compare(R_u, "2e6")== "2e6",
        compare(agg_rate, "1.28e8")== "1.28e8",
        N_c_prime==12,
        compare(F_proj_prime, "0.99988")== "0.99988",
        compare(epsilon_c_max, "8e-5")== "8e-5",
        compare(T_loop, "1.8e-4")== "1.8e-4",
        compare(eta, "0.18")== "0.18",
        compare(B_cycle, "6.4e4")== "6.4e4",
        compare(tau_tx, "6.4e-7")== "6.4e-7",
        compare(ratio, "3.56e-3")== "3.56e-3",
        compare(rho, "0.5")== "0.5",
        compare(rho_upper, "0.583")== "0.583"
    ] if line), 
    16 - sum(1 for line in [
        compare(T_c, "8e-6")== "8e-6",
        compare(f, "0.5")== "0.5",
        N_c==125,
        compare(epsilon_tot, "1.25e-3")== "1.25e-3",
        compare(F_proj, "0.99875")== "0.99875",
        compare(R_u, "2e6")== "2e6",
        compare(agg_rate, "1.28e8")== "1.28e8",
        N_c_prime==12,
        compare(F_proj_prime, "0.99988")== "0.99988",
        compare(epsilon_c_max, "8e-5")== "8e-5",
        compare(T_loop, "1.8e-4")== "1.8e-4",
        compare(eta, "0.18")== "0.18",
        compare(B_cycle, "6.4e4")== "6.4e4",
        compare(tau_tx, "6.4e-7")== "6.4e-7",
        compare(ratio, "3.56e-3")== "3.56e-3",
        compare(rho, "0.5")== "0.5",
        compare(rho_upper, "0.583")== "0.583"
    ] if line)))

```

## Execution output
```
CLAIM Q1: computed=8e-06 expected=8e-6 match=no
CLAIM Q2: computed=0.5 expected=0.5 match=yes
CLAIM Q3: computed=125 expected=125 match=yes
CLAIM Q4: computed=0.00125 expected=1.25e-3 match=no
CLAIM Q5: computed=0.99875 expected=0.99875 match=yes
CLAIM Q6: computed=2000000 expected=2e6 match=no
CLAIM Q7: computed=1.28e+08 expected=1.28e8 match=no
CLAIM Q8: computed=12 expected=12 match=yes
CLAIM Q8: computed=0.99988 expected=0.99988 match=yes
CLAIM Q9: computed=8e-05 expected=8e-5 match=no
CLAIM Q10: computed=0.00018 expected=1.8e-4 match=no
CLAIM Q11: computed=0.18 expected=0.18 match=yes
CLAIM Q12: computed=64000 expected=6.4e4 match=no
CLAIM Q13: computed=6.4e-07 expected=6.4e-7 match=no
CLAIM Q14: computed=0.0035555556 expected=3.56e-3 match=no
CLAIM Q15: computed=0.5 expected=0.5 match=yes
CLAIM Q16: computed=0.58333333 expected=0.583 match=yes
VERIFICATION SUMMARY: 16 claims, 8 match, 8 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8e-06 | 8e-6 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 125 | 125 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.00125 | 1.25e-3 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.99875 | 0.99875 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 2000000 | 2e6 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 1.28e+08 | 1.28e8 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 12 | 12 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 0.99988 | 0.99988 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 8e-05 | 8e-5 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.00018 | 1.8e-4 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.18 | 0.18 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 64000 | 6.4e4 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 6.4e-07 | 6.4e-7 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 0.0035555556 | 3.56e-3 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 0.58333333 | 0.583 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 17.
