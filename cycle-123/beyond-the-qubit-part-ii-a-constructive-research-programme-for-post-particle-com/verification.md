# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Compression factor rho(50) = 9.19e11",
    "inputs": "n=50",
    "formula": "rho = 2^n / (n*(n-1)/2)"
  },
  {
    "id": "Q2",
    "statement": "Pairwise parameter count R(50) = 1225",
    "inputs": "n=50",
    "formula": "R = n*(n-1)/2"
  },
  {
    "id": "Q3",
    "statement": "Hilbert amplitude count H(50) = 1.1259e15",
    "inputs": "n=50",
    "formula": "H = 2^n"
  },
  {
    "id": "Q4",
    "statement": "Hilbert description memory = 18.014 PB",
    "inputs": "16 bytes per amplitude, n=50, 1 PB = 1e15 bytes",
    "formula": "bytes = 16 * 2^50; PB = bytes / 1e15"
  },
  {
    "id": "Q5",
    "statement": "Pairwise description memory = 1.96e4 bytes",
    "inputs": "16 bytes per parameter, R(50)=1225",
    "formula": "bytes = 16 * 1225"
  },
  {
    "id": "Q6",
    "statement": "FWHM-to-sigma conversion constant = 2.354820",
    "inputs": "none",
    "formula": "2*sqrt(2*ln(2))"
  },
  {
    "id": "Q7",
    "statement": "One-sigma band upper end sigma_E/Q = 4.2466e-3",
    "inputs": "FWHM/Q = 0.01, constant 2.354820",
    "formula": "0.01 / 2.354820"
  },
  {
    "id": "Q8",
    "statement": "One-sigma band lower end sigma_E/Q = 2.1233e-3",
    "inputs": "FWHM/Q = 0.005, constant 2.354820",
    "formula": "0.005 / 2.354820"
  },
  {
    "id": "Q9",
    "statement": "Worst-case stack of 5 stages at 1e-2 = 5e-2",
    "inputs": "n=5, eps=1e-2",
    "formula": "eps_WC = n*eps"
  },
  {
    "id": "Q10",
    "statement": "RSS stack of 5 stages at 1e-2 = 2.2361e-2",
    "inputs": "n=5, eps=1e-2",
    "formula": "eps_RSS = eps*sqrt(n)"
  },
  {
    "id": "Q11",
    "statement": "Ratio worst-case/RSS = 2.2361",
    "inputs": "n=5",
    "formula": "ratio = sqrt(n)"
  },
  {
    "id": "Q12",
    "statement": "Frame count N = 3600",
    "inputs": "f=60 Hz, T=60 s",
    "formula": "N = f*T"
  },
  {
    "id": "Q13",
    "statement": "Random-walk drift = 6.0e-2 m per minute",
    "inputs": "eps_f=1e-3 m, N=3600",
    "formula": "delta = eps_f*sqrt(N)"
  },
  {
    "id": "Q14",
    "statement": "Linear-stack drift = 3.6 m",
    "inputs": "eps_f=1e-3 m, N=3600",
    "formula": "delta_lin = eps_f*N"
  },
  {
    "id": "Q15",
    "statement": "Drift ratio linear/random-walk = 60",
    "inputs": "delta_lin=3.6 m, delta=0.06 m",
    "formula": "ratio = 3.6/0.06"
  },
  {
    "id": "Q16",
    "statement": "Frame period at 90 Hz = 11.111 ms",
    "inputs": "f=90 Hz",
    "formula": "T_f = 1/f"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

claims = []

# Q1: rho(50) = 2^50 / (50*49/2) = 9.19e11 (paper states 9.19e11, 3 sig figs)
H50 = 2**50
R50 = 50 * 49 // 2
rho50 = H50 / R50
claims.append(("Q1", rho50, "9.19e11", 3))

# Q2/Q3 handled below; keep ids in order
# Q2: R(50) = 1225 (exact)
claims.append(("Q2", float(R50), "1225", None))

# Q3: H(50) = 2^50 = 1.1259e15 (paper: 1.1259e15, 5 sig figs)
claims.append(("Q3", float(H50), "1.1259e15", 5))

# Q4: memory = 16 * 2^50 bytes = 18.014 PB (paper: 18.014 PB, 5 sig figs)
bytes_H = 16 * 2**50
PB = bytes_H / 1e15
claims.append(("Q4", PB, "18.014", 5))

# Q5: pairwise memory = 16 * 1225 = 19600 bytes (paper: 1.96e4, 3 sig figs)
bytes_R = 16 * R50
claims.append(("Q5", float(bytes_R), "19600", 3))

# Q6: FWHM-to-sigma constant = 2*sqrt(2*ln2) = 2.354820 (6 sig figs)
c = 2 * math.sqrt(2 * math.log(2))
claims.append(("Q6", c, "2.354820", 6))

# Q7: upper band = 0.01 / c = 4.2466e-3 (5 sig figs)
up = 0.01 / c
claims.append(("Q7", up, "4.2466e-3", 5))

# Q8: lower band = 0.005 / c = 2.1233e-3 (5 sig figs)
lo = 0.005 / c
claims.append(("Q8", lo, "2.1233e-3", 5))

# Q9: worst-case stack = 5 * 1e-2 = 5e-2 (exact)
wc = 5 * 1e-2
claims.append(("Q9", wc, "5e-2", None))

# Q10: RSS stack = 1e-2 * sqrt(5) = 2.2361e-2 (5 sig figs)
rss = 1e-2 * math.sqrt(5)
claims.append(("Q10", rss, "2.2361e-2", 5))

# Q11: ratio = sqrt(5) = 2.2361 (5 sig figs)
ratio = math.sqrt(5)
claims.append(("Q11", ratio, "2.2361", 5))

# Q12: N = 60*60 = 3600 (exact)
N = 60 * 60
claims.append(("Q12", float(N), "3600", None))

# Q13: drift = 1e-3 * sqrt(3600) = 6.0e-2 m (2 sig figs)
drift = 1e-3 * math.sqrt(N)
claims.append(("Q13", drift, "0.06", 2))

# Q14: linear drift = 1e-3 * 3600 = 3.6 m (2 sig figs)
lin = 1e-3 * N
claims.append(("Q14", lin, "3.6", 2))

# Q15: ratio = 3.6 / 0.06 = 60 (exact)
dr = 3.6 / 0.06
claims.append(("Q15", dr, "60", None))

# Q16: frame period = 1/90 s = 11.111 ms (5 sig figs)
Tf_ms = (1 / 90) * 1000
claims.append(("Q16", Tf_ms, "11.111", 5))

mismatch = 0
for cid, computed, expected_str, nsig in claims:
    if nsig is None:
        match = (abs(computed - float(expected_str)) < 1e-12)
    else:
        match = (sig(computed, nsig) == float(expected_str))
    if not match:
        mismatch += 1
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected_str} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {len(claims) - mismatch} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=9.1910196e+11 expected=9.19e11 match=yes
CLAIM Q2: computed=1225 expected=1225 match=yes
CLAIM Q3: computed=1.1258999e+15 expected=1.1259e15 match=yes
CLAIM Q4: computed=18.014399 expected=18.014 match=yes
CLAIM Q5: computed=19600 expected=19600 match=yes
CLAIM Q6: computed=2.35482 expected=2.354820 match=yes
CLAIM Q7: computed=0.004246609 expected=4.2466e-3 match=yes
CLAIM Q8: computed=0.0021233045 expected=2.1233e-3 match=yes
CLAIM Q9: computed=0.05 expected=5e-2 match=yes
CLAIM Q10: computed=0.02236068 expected=2.2361e-2 match=yes
CLAIM Q11: computed=2.236068 expected=2.2361 match=yes
CLAIM Q12: computed=3600 expected=3600 match=yes
CLAIM Q13: computed=0.06 expected=0.06 match=yes
CLAIM Q14: computed=3.6 expected=3.6 match=yes
CLAIM Q15: computed=60 expected=60 match=yes
CLAIM Q16: computed=11.111111 expected=11.111 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 9.1910196e+11 | 9.19e11 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 1225 | 1225 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 1.1258999e+15 | 1.1259e15 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 18.014399 | 18.014 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 19600 | 19600 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 2.35482 | 2.354820 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q7 | 0.004246609 | 4.2466e-3 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 0.0021233045 | 2.1233e-3 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 0.05 | 5e-2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.02236068 | 2.2361e-2 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q11 | 2.236068 | 2.2361 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 3600 | 3600 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 0.06 | 0.06 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 3.6 | 3.6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 60 | 60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 11.111111 | 11.111 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
