# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Harmonic-limit second-order leakage for a pi-pulse: L_P^(2) = theta^4/2 = 3.0440341",
    "inputs": "theta = pi/2 = 1.5707963",
    "formula": "L = theta^4/2"
  },
  {
    "id": "Q2",
    "statement": "First-order leakage bound at worst-case timing: L_2 = 0.02",
    "inputs": "Omega/|alpha| = 0.05, alpha*T_g/2 = pi/2",
    "formula": "L_2 = 8*(Omega/|alpha|)^2*sin^2(alpha*T_g/2)"
  },
  {
    "id": "Q3",
    "statement": "Gate-averaged leakage: L2_avg = 0.01",
    "inputs": "Omega/|alpha| = 0.05, mean of sin^2 = 1/2",
    "formula": "L2_avg = 8*(Omega/|alpha|)^2*(1/2)"
  },
  {
    "id": "Q4",
    "statement": "Scaled gate-averaged leakage at Omega/|alpha| = 0.10: 0.04",
    "inputs": "Omega/|alpha| = 0.10",
    "formula": "L2_avg = 4*(Omega/|alpha|)^2"
  },
  {
    "id": "Q5",
    "statement": "Exact three-level peak leakage P2_max = 1.96e-2",
    "inputs": "r = 0.1",
    "formula": "P2_max = 2*r^2/(1+2*r^2)"
  },
  {
    "id": "Q6",
    "statement": "Exact three-level time-averaged leakage P2_avg = 9.80e-3",
    "inputs": "r = 0.1",
    "formula": "P2_avg = r^2/(1+2*r^2)"
  },
  {
    "id": "Q7",
    "statement": "Pi-pulse duration t_pi = 25 ns",
    "inputs": "f_Omega = 20 MHz",
    "formula": "t_pi = 1/(2*f_Omega)"
  },
  {
    "id": "Q8",
    "statement": "Base-encoding entropy S_Base(12) = ln 6 = 1.7917595 nats",
    "inputs": "d = 12",
    "formula": "S_Base = ln(d/2)"
  },
  {
    "id": "Q9",
    "statement": "S_Base(12) in bits = 2.5849625",
    "inputs": "S_Base = 1.7917595 nats, ln 2 = 0.6931472",
    "formula": "bits = S_Base/ln(2)"
  },
  {
    "id": "Q10",
    "statement": "Discarded-information fraction f_disc = 0.721057",
    "inputs": "ln 6 = 1.7917595, ln 12 = 2.4849067",
    "formula": "f_disc = ln(6)/ln(12)"
  },
  {
    "id": "Q11",
    "statement": "Full ladder log-capacity log2(12) = 3.5849625 bits",
    "inputs": "ln 12 = 2.4849067, ln 2 = 0.6931472",
    "formula": "log2(12) = ln(12)/ln(2)"
  },
  {
    "id": "Q12",
    "statement": "Radix efficiency eta = 0.278943 (27.9%)",
    "inputs": "f_disc = 0.721057",
    "formula": "eta = 1 - f_disc"
  },
  {
    "id": "Q13",
    "statement": "S_Base(6) = ln 3 = 1.0986123 nats = 1.5849625 bits",
    "inputs": "d = 6, ln 2 = 0.6931472",
    "formula": "S_Base = ln(d/2); bits = S_Base/ln(2)"
  },
  {
    "id": "Q14",
    "statement": "S_Base(4) = ln 2 = 0.6931472 nats = 1 bit",
    "inputs": "d = 4, ln 2 = 0.6931472",
    "formula": "S_Base = ln(d/2); bits = S_Base/ln(2)"
  },
  {
    "id": "Q15",
    "statement": "Discarded fraction at d = 6: ln 3/ln 6 = 0.613147",
    "inputs": "ln 3 = 1.0986123, ln 6 = 1.7917595",
    "formula": "f_disc = ln(3)/ln(6)"
  },
  {
    "id": "Q16",
    "statement": "Crude projection L_P^(est) values 1.0e-2, 2.5e-3, 4.0e-2 at Omega/alpha = 0.1, 0.05, 0.2",
    "inputs": "Omega/alpha = 0.1, 0.05, 0.2",
    "formula": "L = (Omega/alpha)^2"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    from decimal import Decimal
    return round(x, n - 1 - int(math.floor(math.log10(abs(x)))))

results = []

# Q1: L = theta^4/2, theta = pi/2, expected 3.0440341
theta = math.pi / 2
q1 = theta**4 / 2
results.append(("Q1", q1, "3.0440341", 8))

# Q2: L2 = 8*(0.05)^2*sin^2(pi/2) = 0.02
q2 = 8 * (0.05)**2 * math.sin(math.pi / 2)**2
results.append(("Q2", q2, "0.02", 2))

# Q3: L2_avg = 8*(0.05)^2*(1/2) = 0.01
q3 = 8 * (0.05)**2 * 0.5
results.append(("Q3", q3, "0.01", 2))

# Q4: L2_avg = 4*(0.10)^2 = 0.04
q4 = 4 * (0.10)**2
results.append(("Q4", q4, "0.04", 2))

# Q5: P2_max = 2*r^2/(1+2*r^2), r=0.1, expected 1.96e-2
r = 0.1
q5 = 2 * r**2 / (1 + 2 * r**2)
results.append(("Q5", q5, "0.0196", 3))

# Q6: P2_avg = r^2/(1+2*r^2), expected 9.80e-3
q6 = r**2 / (1 + 2 * r**2)
results.append(("Q6", q6, "0.0098", 3))

# Q7: t_pi = 1/(2*f_Omega), f=20 MHz, expected 25 ns
f = 20e6
q7 = 1 / (2 * f) * 1e9  # in ns
results.append(("Q7", q7, "25", 2))

# Q8: S_Base(12) = ln(6), expected 1.7917595 nats
q8 = math.log(12 / 2)
results.append(("Q8", q8, "1.7917595", 8))

# Q9: bits = S_Base/ln(2), expected 2.5849625
q9 = math.log(6) / math.log(2)
results.append(("Q9", q9, "2.5849625", 8))

# Q10: f_disc = ln(6)/ln(12), expected 0.721057
q10 = math.log(6) / math.log(12)
results.append(("Q10", q10, "0.721057", 6))

# Q11: log2(12) = ln(12)/ln(2), expected 3.5849625
q11 = math.log(12) / math.log(2)
results.append(("Q11", q11, "3.5849625", 8))

# Q12: eta = 1 - f_disc, expected 0.278943
q12 = 1 - math.log(6) / math.log(12)
results.append(("Q12", q12, "0.278943", 6))

# Q13: S_Base(6) = ln(3) nats = ln(3)/ln(2) bits, expected 1.0986123 nats / 1.5849625 bits
q13n = math.log(3)
q13b = math.log(3) / math.log(2)
results.append(("Q13", q13n, "1.0986123", 8))
results.append(("Q13b", q13b, "1.5849625", 8))

# Q14: S_Base(4) = ln(2) nats = 1 bit
q14n = math.log(2)
q14b = math.log(2) / math.log(2)
results.append(("Q14", q14n, "0.6931472", 8))
results.append(("Q14b", q14b, "1", 1))

# Q15: f_disc(6) = ln(3)/ln(6), expected 0.613147
q15 = math.log(3) / math.log(6)
results.append(("Q15", q15, "0.613147", 6))

# Q16: crude projection (Omega/alpha)^2 at 0.1, 0.05, 0.2 -> 1.0e-2, 2.5e-3, 4.0e-2
q16a = 0.1**2
q16b = 0.05**2
q16c = 0.2**2
results.append(("Q16a", q16a, "0.01", 2))
results.append(("Q16b", q16b, "0.0025", 2))
results.append(("Q16c", q16c, "0.04", 2))

match_count = 0
for rid, computed, expected_str, nsig in results:
    expected = float(expected_str)
    match = "yes" if sig(computed, nsig) == expected else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {rid}: computed={computed:.8g} expected={expected_str} match={match}")

total = len(results)
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=3.0440341 expected=3.0440341 match=yes
CLAIM Q2: computed=0.02 expected=0.02 match=yes
CLAIM Q3: computed=0.01 expected=0.01 match=yes
CLAIM Q4: computed=0.04 expected=0.04 match=yes
CLAIM Q5: computed=0.019607843 expected=0.0196 match=yes
CLAIM Q6: computed=0.0098039216 expected=0.0098 match=yes
CLAIM Q7: computed=25 expected=25 match=yes
CLAIM Q8: computed=1.7917595 expected=1.7917595 match=yes
CLAIM Q9: computed=2.5849625 expected=2.5849625 match=yes
CLAIM Q10: computed=0.72105705 expected=0.721057 match=yes
CLAIM Q11: computed=3.5849625 expected=3.5849625 match=yes
CLAIM Q12: computed=0.27894295 expected=0.278943 match=yes
CLAIM Q13: computed=1.0986123 expected=1.0986123 match=yes
CLAIM Q13b: computed=1.5849625 expected=1.5849625 match=yes
CLAIM Q14: computed=0.69314718 expected=0.6931472 match=no
CLAIM Q14b: computed=1 expected=1 match=yes
CLAIM Q15: computed=0.61314719 expected=0.613147 match=yes
CLAIM Q16a: computed=0.01 expected=0.01 match=yes
CLAIM Q16b: computed=0.0025 expected=0.0025 match=yes
CLAIM Q16c: computed=0.04 expected=0.04 match=yes
VERIFICATION SUMMARY: 20 claims, 19 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3.0440341 | 3.0440341 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q2 | 0.02 | 0.02 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.01 | 0.01 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.04 | 0.04 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.019607843 | 0.0196 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 0.0098039216 | 0.0098 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 25 | 25 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 1.7917595 | 1.7917595 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q9 | 2.5849625 | 2.5849625 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q10 | 0.72105705 | 0.721057 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q11 | 3.5849625 | 3.5849625 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q12 | 0.27894295 | 0.278943 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q13 | 1.0986123 | 1.0986123 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q13b | 1.5849625 | 1.5849625 | yes | match | 8 significant digits (as printed, at least 3) |
| Q14 | 0.69314718 | 0.6931472 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q14b | 1 | 1 | yes | match | 3 significant digits (as printed, at least 3) |
| Q15 | 0.61314719 | 0.613147 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q16a | 0.01 | 0.01 | yes | match | 3 significant digits (as printed, at least 3) |
| Q16b | 0.0025 | 0.0025 | yes | match | 3 significant digits (as printed, at least 3) |
| Q16c | 0.04 | 0.04 | yes | match | 3 significant digits (as printed, at least 3) |

Mismatches: 0 of 20.
