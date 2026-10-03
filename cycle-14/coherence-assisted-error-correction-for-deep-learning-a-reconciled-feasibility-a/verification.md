# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "SEC-DED ECC energy per inference is 2.5 µJ",
    "inputs": "A=10^8 bits/inference, check bits r=8, word size m=64, passes=2, e_par=0.1 pJ/bit",
    "formula": "E_SEC = A * (8/64) * 2 * 0.1e-12 J = 2.5e-6 J"
  },
  {
    "id": "Q2",
    "statement": "BCH(t=2) ECC energy per inference is 10 µJ",
    "inputs": "A=10^8 bits/inference, r=16, m=64, switching factor=4, e_par=0.1 pJ/bit",
    "formula": "E_BCH = A * (16/64) * 4 * 0.1e-12 J = 1e-5 J"
  },
  {
    "id": "Q3",
    "statement": "Upgrading SEC-DED to BCH costs 7.5 µJ/inference, i.e. 7.5 kJ/day ≈ 87 mW at 10^9 inferences/day",
    "inputs": "E_BCH=10 µJ, E_SEC=2.5 µJ, rate=10^9 inferences/day, day=86400 s",
    "formula": "ΔE = 10 - 2.5 = 7.5 µJ; P = 7.5e-6 * 1e9 / 86400 ≈ 0.0868 W"
  },
  {
    "id": "Q4",
    "statement": "TMR datapath protection costs 768 pJ per 256-MAC block",
    "inputs": "3 copies, B=256 MACs, 1 pJ per MAC",
    "formula": "E_TMR = 3 * 256 * 1 pJ = 768 pJ"
  },
  {
    "id": "Q5",
    "statement": "TMR residual per-MAC BER is 3×10⁻¹⁰",
    "inputs": "p_raw=10^-5",
    "formula": "p_TMR = C(3,2) * p_raw^2 = 3 * (1e-5)^2 = 3e-10"
  },
  {
    "id": "Q6",
    "statement": "Maximum coherent circuit depth is 5,000 gates",
    "inputs": "T2=100 µs, t_g=20 ns",
    "formula": "D_max = T2 / t_g = 100e-6 / 20e-9 = 5000"
  },
  {
    "id": "Q7",
    "statement": "A depth-14 syndrome circuit executes in 280 ns, a 357× margin against T₂",
    "inputs": "depth=14, t_g=20 ns, T2=100 µs",
    "formula": "t = 14 * 20 ns = 280 ns; margin = 100 µs / 280 ns ≈ 357"
  },
  {
    "id": "Q8",
    "statement": "Per-call latency is 110 µs per flagged tile",
    "inputs": "t_rt=10 µs, S=100, depth=50, t_g=20 ns",
    "formula": "t_call = t_rt + S * (depth * t_g) = 10 µs + 100 * (50 * 20 ns) = 110 µs"
  }
]

## Script
```python
import math

results = []

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=tol) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1: SEC-DED energy
E_SEC = 1e8 * (8/64) * 2 * 0.1e-12
check("Q1", E_SEC, 2.5e-6)

# Q2: BCH energy
E_BCH = 1e8 * (16/64) * 4 * 0.1e-12
check("Q2", E_BCH, 1e-5)

# Q3: upgrade cost and power
dE = (E_BCH - E_SEC) * 1e9  # J/day
P = dE / 86400
check("Q3", P, 0.0868, tol=1e-2)

# Q4: TMR energy per block
E_TMR = 3 * 256 * 1e-12
check("Q4", E_TMR, 768e-12)

# Q5: TMR residual BER
p_TMR = 3 * (1e-5)**2
check("Q5", p_TMR, 3e-10)

# Q6: max coherent depth
D_max = 100e-6 / 20e-9
check("Q6", D_max, 5000)

# Q7: syndrome circuit time and margin
t_syn = 14 * 20e-9
margin = 100e-6 / t_syn
check("Q7", margin, 357, tol=1e-2)

# Q8: per-call latency
t_call = 10e-6 + 100 * (50 * 20e-9)
check("Q8", t_call, 110e-6)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n-m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.5e-06 expected=2.5e-06 match=yes
CLAIM Q2: computed=1e-05 expected=1e-05 match=yes
CLAIM Q3: computed=0.08680555555555557 expected=0.0868 match=yes
CLAIM Q4: computed=7.68e-10 expected=7.68e-10 match=yes
CLAIM Q5: computed=3.0000000000000005e-10 expected=3e-10 match=yes
CLAIM Q6: computed=5000.0 expected=5000 match=yes
CLAIM Q7: computed=357.1428571428571 expected=357 match=yes
CLAIM Q8: computed=0.00010999999999999999 expected=0.00011 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
