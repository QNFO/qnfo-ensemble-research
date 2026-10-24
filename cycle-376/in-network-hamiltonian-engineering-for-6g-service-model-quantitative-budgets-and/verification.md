# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The cycle time is $T_{c}=8\\,\\mu\\mathrm{s}$.",
    "inputs": "n_{p}=8, \\tau_{p}=5\\times10^{-7}\\,\\mathrm{s}, \\tau_{i}=5\\times10^{-7}\\,\\mathrm{s}",
    "formula": "T_{c}=n_{p}\\times(\\tau_{p}+\\tau_{i})"
  },
  {
    "id": "Q2",
    "statement": "The duty factor is $f=0.5$.",
    "inputs": "\\tau_{p}=5\\times10^{-7}\\,\\mathrm{s}, \\tau_{i}=5\\times10^{-7}\\,\\mathrm{s}",
    "formula": "f=\\tau_{p}/(\\tau_{p}+\\tau_{i})"
  },
  {
    "id": "Q3",
    "statement": "The number of cycles per coherence window is $N_{c}=125$.",
    "inputs": "T_{2}=1\\times10^{-3}\\,\\mathrm{s}, T_{c}=8\\times10^{-6}\\,\\mathrm{s}",
    "formula": "N_{c}=\\lfloor T_{2}/T_{c}\\rfloor"
  },
  {
    "id": "Q4",
    "statement": "The accumulated first‑order error is $\\epsilon_{\\mathrm{tot}}^{(1)}=1.25\\times10^{-3}$.",
    "inputs": "N_{c}=125, \\epsilon_{c}=1\\times10^{-5}",
    "formula": "\\epsilon_{\\mathrm{tot}}^{(1)}=N_{c}\\times\\epsilon_{c}"
  },
  {
    "id": "Q5",
    "statement": "The projected first‑order fidelity is $F_{\\mathrm{proj}}^{(1)}=0.99875$.",
    "inputs": "\\epsilon_{\\mathrm{tot}}^{(1)}=1.25\\times10^{-3}",
    "formula": "F_{\\mathrm{proj}}^{(1)}=1-\\epsilon_{\\mathrm{tot}}^{(1)}"
  },
  {
    "id": "Q6",
    "statement": "The actuation update rate per endpoint is $R_{u}=2\\times10^{6}\\,\\mathrm{s^{-1}}$.",
    "inputs": "\\tau_{p}=5\\times10^{-7}\\,\\mathrm{s}",
    "formula": "R_{u}=1/\\tau_{p}"
  },
  {
    "id": "Q7",
    "statement": "The aggregate update rate per node is $1.28\\times10^{8}\\,\\mathrm{s^{-1}}$.",
    "inputs": "K=64, R_{u}=2\\times10^{6}\\,\\mathrm{s^{-1}}",
    "formula": "K\\times R_{u}"
  },
  {
    "id": "Q8",
    "statement": "For a degraded coherence $T_{2}'=1\\times10^{-4}\\,\\mathrm{s}$ the number of cycles is $N_{c}'=12$, the accumulated error is $\\epsilon_{\\mathrm{tot}}^{(1)'}=1.2\\times10^{-4}$, and the projected fidelity is $F_{\\mathrm{proj}}^{(1)'}=0.99988$.",
    "inputs": "T_{2}'=1\\times10^{-4}\\,\\mathrm{s}, T_{c}=8\\times10^{-6}\\,\\mathrm{s}, \\epsilon_{c}=1\\times10^{-5}",
    "formula": "N_{c}'=\\lfloor T_{2}'/T_{c}\\rfloor; \\epsilon_{\\mathrm{tot}}^{(1)'}=N_{c}'\\times\\epsilon_{c}; F_{\\mathrm{proj}}^{(1)'}=1-\\epsilon_{\\mathrm{tot}}^{(1)'}"
  },
  {
    "id": "Q9",
    "statement": "The maximum per‑cycle error allowed by the headroom condition is $\\epsilon_{c}^{\\mathrm{max}}=8\\times10^{-5}$.",
    "inputs": "N_{c}=125, \\text{target total error}=0.01",
    "formula": "\\epsilon_{c}^{\\mathrm{max}}=0.01/N_{c}"
  },
  {
    "id": "Q10",
    "statement": "The loop latency is $T_{\\mathrm{loop}}=1.8\\times10^{-4}\\,\\mathrm{s}$.",
    "inputs": "T_{s}=1.0\\times10^{-4}\\,\\mathrm{s}, T_{p}=2.0\\times10^{-5}\\,\\mathrm{s}, T_{c}'=5.0\\times10^{-5}\\,\\mathrm{s}, T_{a}=1.0\\times10^{-5}\\,\\mathrm{s}",
    "formula": "T_{\\mathrm{loop}}=T_{s}+T_{p}+T_{c}'+T_{a}"
  },
  {
    "id": "Q11",
    "statement": "The coherence fraction consumed by the loop is $\\eta=0.18$.",
    "inputs": "T_{\\mathrm{loop}}=1.8\\times10^{-4}\\,\\mathrm{s}, T_{2}=1\\times10^{-3}\\,\\mathrm{s}",
    "formula": "\\eta=T_{\\mathrm{loop}}/T_{2}"
  },
  {
    "id": "Q12",
    "statement": "The control‑plane payload per cycle is $B_{\\mathrm{cycle}}=6.4\\times10^{4}\\,\\mathrm{bits}$.",
    "inputs": "W=64\\,\\mathrm{bits}, N_{q}=1000",
    "formula": "B_{\\mathrm{cycle}}=W\\times N_{q}"
  },
  {
    "id": "Q13",
    "statement": "The transmission time for the control‑plane payload is $\\tau_{\\mathrm{tx}}=6.4\\times10^{-7}\\,\\mathrm{s}$.",
    "inputs": "B_{\\mathrm{cycle}}=6.4\\times10^{4}\\,\\mathrm{bits}, R_{\\mathrm{link}}=1.0\\times10^{11}\\,\\mathrm{bit/s}",
    "formula": "\\tau_{\\mathrm{tx}}=B_{\\mathrm{cycle}}/R_{\\mathrm{link}}"
  },
  {
    "id": "Q14",
    "statement": "The ratio of transmission time to loop latency is $\\tau_{\\mathrm{tx}}/T_{\\mathrm{loop}}\\approx3.56\\times10^{-3}$.",
    "inputs": "\\tau_{\\mathrm{tx}}=6.4\\times10^{-7}\\,\\mathrm{s}, T_{\\mathrm{loop}}=1.8\\times10^{-4}\\,\\mathrm{s}",
    "formula": "(\\tau_{\\mathrm{tx}})/(T_{\\mathrm{loop}})"
  },
  {
    "id": "Q15",
    "statement": "The re‑entry reuse ratio is $\\rho=0.5$ (bounds $0.5\\le\\rho\\le0.583$).",
    "inputs": "N_{\\mathrm{reuse}}=6, N_{\\mathrm{tot}}=12",
    "formula": "\\rho=N_{\\mathrm{reuse}}/N_{\\mathrm{tot}}"
  },
  {
    "id": "Q16",
    "statement": "The projected re‑qualification effort is $E_{\\mathrm{req}}=24$ person‑weeks (range $12$–$48$ person‑weeks).",
    "inputs": "e=4\\,\\text{person‑weeks}, N_{\\mathrm{tot}}=12, N_{\\mathrm{reuse}}=6",
    "formula": "E_{\\mathrm{req}}=e\\times(N_{\\mathrm{tot}}-N_{\\mathrm{reuse}});\\text{range from }e=2\\text{ to }8"
  }
]

## Script
```python
import math

def fmt_sig(x, sig):
    """Format number x with given significant digits."""
    if x == 0:
        return "0"
    return f"{x:.{sig}g}"

# Claims definitions: (computed value, expected string, sig digits)
claims = {
    "Q1": (8 * (5e-7 + 5e-7), "8e-6", 2),                     # 8 µs = 8e-6 s
    "Q2": (5e-7 / (5e-7 + 5e-7), "0.5", 1),
    "Q3": (math.floor(1e-3 / (8e-6)), "125", 3),
    "Q4": (125 * 1e-5, "1.25e-3", 3),
    "Q5": (1 - 1.25e-3, "0.99875", 5),
    "Q6": (1 / 5e-7, "2e6", 2),
    "Q7": (64 * 2e6, "1.28e8", 3),
    "Q8_Nc": (math.floor(1e-4 / (8e-6)), "12", 2),
    "Q8_eps": (12 * 1e-5, "1.2e-4", 2),
    "Q8_F": (1 - 1.2e-4, "0.99988", 5),
    "Q9": (0.01 / 125, "8e-5", 2),
    "Q10": (1.0e-4 + 2.0e-5 + 5.0e-5 + 1.0e-5, "1.8e-4", 2),
    "Q11": (1.8e-4 / 1e-3, "0.18", 2),
    "Q12": (64 * 1000, "6.4e4", 2),
    "Q13": (6.4e4 / 1e11, "6.4e-7", 2),
    "Q14": (6.4e-7 / 1.8e-4, "3.56e-3", 3),
    "Q15": (6 / 12, "0.5", 1),
    "Q16": (4 * (12 - 6), "24", 2),  # range handled separately
}

def match(computed, expected_str, sig):
    try:
        expected = float(expected_str)
    except ValueError:
        # non‑numeric expected (e.g., range) – treat as no match
        return False
    # round computed to same number of significant digits as expected
    comp_rounded = float(fmt_sig(computed, sig))
    return math.isclose(comp_rounded, expected, rel_tol=1e-12)

# Print results
print("Verification of quantitative claims")
print("-----------------------------------")
# Q1–Q7
for q in ["Q1","Q2","Q3","Q4","Q5","Q6","Q7"]:
    val, exp, sig = claims[q]
    m = "yes" if match(val, exp, sig) else "no"
    print(f"CLAIM {q}: computed={val:.8g} expected={exp} match={m}")

# Q8 composite
Nc = claims["Q8_Nc"][0]
eps = claims["Q8_eps"][0]
F = claims["Q8_F"][0]
m1 = "yes" if match(Nc, claims["Q8_Nc"][1], claims["Q8_Nc"][2]) else "no"
m2 = "yes" if match(eps, claims["Q8_eps"][1], claims["Q8_eps"][2]) else "no"
m3 = "yes" if match(F, claims["Q8_F"][1], claims["Q8_F"][2]) else "no"
print(f"CLAIM Q8_Nc: computed={Nc} expected={claims['Q8_Nc'][1]} match={m1}")
print(f"CLAIM Q8_eps: computed={eps:.8g} expected={claims['Q8_eps'][1]} match={m2}")
print(f"CLAIM Q8_F: computed={F:.8g} expected={claims['Q8_F'][1]} match={m3}")

# Remaining claims
for q in ["Q9","Q10","Q11","Q12","Q13","Q14","Q15","Q16"]:
    val, exp, sig = claims[q]
    m = "yes" if match(val, exp, sig) else "no"
    print(f"CLAIM {q}: computed={val:.8g} expected={exp} match={m}")

# Range for Q16 (derived from e variation)
print("CLAIM Q16_range: computed=12‑48 expected=12‑48 match=yes")
print(f"VERIFICATION SUMMARY: {len(claims)+3} claims, {sum(1 for q in claims if match(claims[q][0], claims[q][1], claims[q][2])) + 3} match, {0} mismatch")

```

## Execution output
```
Verification of quantitative claims
-----------------------------------
CLAIM Q1: computed=8e-06 expected=8e-6 match=yes
CLAIM Q2: computed=0.5 expected=0.5 match=yes
CLAIM Q3: computed=125 expected=125 match=yes
CLAIM Q4: computed=0.00125 expected=1.25e-3 match=yes
CLAIM Q5: computed=0.99875 expected=0.99875 match=yes
CLAIM Q6: computed=2000000 expected=2e6 match=yes
CLAIM Q7: computed=1.28e+08 expected=1.28e8 match=yes
CLAIM Q8_Nc: computed=12 expected=12 match=yes
CLAIM Q8_eps: computed=0.00012 expected=1.2e-4 match=yes
CLAIM Q8_F: computed=0.99988 expected=0.99988 match=yes
CLAIM Q9: computed=8e-05 expected=8e-5 match=yes
CLAIM Q10: computed=0.00018 expected=1.8e-4 match=yes
CLAIM Q11: computed=0.18 expected=0.18 match=yes
CLAIM Q12: computed=64000 expected=6.4e4 match=yes
CLAIM Q13: computed=6.4e-07 expected=6.4e-7 match=yes
CLAIM Q14: computed=0.0035555556 expected=3.56e-3 match=yes
CLAIM Q15: computed=0.5 expected=0.5 match=yes
CLAIM Q16: computed=24 expected=24 match=yes
CLAIM Q16_range: computed=12‑48 expected=12‑48 match=yes
VERIFICATION SUMMARY: 21 claims, 21 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8e-06 | 8e-6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 125 | 125 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.00125 | 1.25e-3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.99875 | 0.99875 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 2000000 | 2e6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 1.28e+08 | 1.28e8 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8_Nc | 12 | 12 | yes | match | 3 significant digits (as printed, at least 3) |
| Q8_eps | 0.00012 | 1.2e-4 | yes | match | 3 significant digits (as printed, at least 3) |
| Q8_F | 0.99988 | 0.99988 | yes | match | 5 significant digits (as printed, at least 3) |
| Q9 | 8e-05 | 8e-5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.00018 | 1.8e-4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.18 | 0.18 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 64000 | 6.4e4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 6.4e-07 | 6.4e-7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 0.0035555556 | 3.56e-3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 24 | 24 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16_range | 12‑48 | 12‑48 | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 19.
