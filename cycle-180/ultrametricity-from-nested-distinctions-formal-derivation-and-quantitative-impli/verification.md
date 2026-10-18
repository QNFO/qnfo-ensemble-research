# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The loss of strong‑lens detections when median $g$‑band seeing degrades from $0.8''$ to $0.9''$ is $3.4\\times10^{4}$ lenses.",
    "inputs": "baseline number of lenses N0 = 2.0×10^5 lenses, loss fraction f = 0.17",
    "formula": "ΔN = f * N0"
  },
  {
    "id": "Q2",
    "statement": "The remaining detectable lenses after the seeing degradation are $1.66\\times10^{5}$ lenses.",
    "inputs": "baseline number of lenses N0 = 2.0×10^5 lenses, loss ΔN = 3.4×10^4 lenses",
    "formula": "N1 = N0 - ΔN"
  },
  {
    "id": "Q3",
    "statement": "The triangle‑free process on $n=10^{6}$ vertices yields at least $1.0\\times10^{9}$ edges.",
    "inputs": "number of vertices n = 10^6",
    "formula": "E ≥ n^{3/2}"
  },
  {
    "id": "Q4",
    "statement": "The empirical violation probability of the ultrametric condition in the chunking simulation is $9\\times10^{-4}$.",
    "inputs": "number of violations v = 9, total runs R = 10^4",
    "formula": "p = v / R"
  },
  {
    "id": "Q5",
    "statement": "The planned psychophysical experiment will generate a total of $10^{4}$ chunking trials.",
    "inputs": "number of participants P = 10, trials per participant T = 1000",
    "formula": "total_trials = P * T"
  },
  {
    "id": "Q6",
    "statement": "The total data‑collection time for the experiment is $5{,}000$ seconds (approximately 1.4 hours).",
    "inputs": "total_trials = 10^4 trials, time per trial t = 0.5 seconds",
    "formula": "total_time = total_trials * t"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def format_sig(x, sig):
    # Use general format with specified significant figures
    fmt = "{{:.{}g}}".format(sig)
    return fmt.format(x)

claims = []

# Q1
N0 = 2.0e5
f = 0.17
delta_N = f * N0
computed_Q1 = delta_N
expected_Q1 = "3.4e4"
sig_Q1 = 2
match_Q1 = format_sig(round_sig(computed_Q1, sig_Q1), sig_Q1) == expected_Q1
claims.append(("Q1", computed_Q1, expected_Q1, match_Q1))

# Q2
N1 = N0 - delta_N
computed_Q2 = N1
expected_Q2 = "1.66e5"
sig_Q2 = 3
match_Q2 = format_sig(round_sig(computed_Q2, sig_Q2), sig_Q2) == expected_Q2
claims.append(("Q2", computed_Q2, expected_Q2, match_Q2))

# Q3
n = 1e6
E = n ** 1.5
computed_Q3 = E
expected_Q3 = "1.0e9"
sig_Q3 = 2
match_Q3 = format_sig(round_sig(computed_Q3, sig_Q3), sig_Q3) == expected_Q3
claims.append(("Q3", computed_Q3, expected_Q3, match_Q3))

# Q4
v = 9
R = 1e4
p = v / R
computed_Q4 = p
expected_Q4 = "9e-4"
sig_Q4 = 1
match_Q4 = format_sig(round_sig(computed_Q4, sig_Q4), sig_Q4) == expected_Q4
claims.append(("Q4", computed_Q4, expected_Q4, match_Q4))

# Q5
P = 10
T = 1000
total_trials = P * T
computed_Q5 = total_trials
expected_Q5 = "1e4"
sig_Q5 = 1
match_Q5 = format_sig(round_sig(computed_Q5, sig_Q5), sig_Q5) == expected_Q5
claims.append(("Q5", computed_Q5, expected_Q5, match_Q5))

# Q6
t = 0.5
total_time = total_trials * t
computed_Q6 = total_time
expected_Q6 = "5000"
# For a plain integer we treat sig figs as full precision
match_Q6 = int(round(computed_Q6)) == int(expected_Q6)
claims.append(("Q6", computed_Q6, expected_Q6, match_Q6))

# Output results
match_count = 0
for cid, comp, exp, ok in claims:
    print(f"CLAIM {cid}: computed={format_sig(comp, 8)} expected={exp} match={'yes' if ok else 'no'}")
    if ok:
        match_count += 1

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims)-match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=34000 expected=3.4e4 match=no
CLAIM Q2: computed=166000 expected=1.66e5 match=no
CLAIM Q3: computed=1e+09 expected=1.0e9 match=no
CLAIM Q4: computed=0.0009 expected=9e-4 match=no
CLAIM Q5: computed=10000 expected=1e4 match=no
CLAIM Q6: computed=5000 expected=5000 match=yes
VERIFICATION SUMMARY: 6 claims, 1 match, 5 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 34000 | 3.4e4 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 166000 | 1.66e5 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 1e+09 | 1.0e9 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.0009 | 9e-4 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 10000 | 1e4 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 5000 | 5000 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 6.
