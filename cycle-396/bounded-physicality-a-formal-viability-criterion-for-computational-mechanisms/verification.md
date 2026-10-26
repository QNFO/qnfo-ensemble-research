# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Convertible energy budget of the observable universe is $B_{E}=1.5\\times10^{70}\\ \\text{J}$.",
    "inputs": "Number of atoms $N_{\\text{atoms}}=10^{80}$, proton mass $m_{p}=1.67\\times10^{-27}\\ \\text{kg}$, speed of light $c=3.00\\times10^{8}\\ \\text{m\\,s}^{-1}$",
    "formula": "$B_{E}=N_{\\text{atoms}}\\times m_{p}\\times c^{2}$"
  },
  {
    "id": "Q2",
    "statement": "Effective operation budget is $B_{\\text{ops}}^{\\text{eff}}=5.24\\times10^{90}$ operations.",
    "inputs": "Universal energy budget $B_{E}=1.503\\times10^{70}\\ \\text{J}$, Boltzmann constant $k_{B}=1.38\\times10^{-23}\\ \\text{J\\,K}^{-1}$, temperature $T=300\\ \\text{K}$, natural logarithm of 2 $\\ln2=0.6931$",
    "formula": "$E_{\\min}=k_{B}T\\ln2$, $B_{\\text{ops}}^{\\text{eff}}=B_{E}/E_{\\min}$"
  },
  {
    "id": "Q3",
    "statement": "Sequential time for exhaustive 128‑bit key search is $T_{\\text{seq}}=3.4\\times10^{29}\\ \\text{s}$.",
    "inputs": "Search space size $S(128)=2^{128}=3.402823669\\times10^{38}$, processor clock frequency $f=10^{9}\\ \\text{ops\\,s}^{-1}$",
    "formula": "$T_{\\text{seq}}=S(128)/f$"
  },
  {
    "id": "Q4",
    "statement": "Required parallel processor count to meet the temporal bound for a 128‑bit search is $p=3.4\\times10^{11}$.",
    "inputs": "Search space $S(128)=3.402823669\\times10^{38}$, frequency $f=10^{9}\\ \\text{ops\\,s}^{-1}$, maximal allowed time $T_{\\max}=10^{18}\\ \\text{s}$",
    "formula": "$p=S(128)/(f\\,T_{\\max})$"
  },
  {
    "id": "Q5",
    "statement": "Total hardware mass for that parallelism is $M=3.4\\times10^{8}\\ \\text{kg}$.",
    "inputs": "Processor count $p=3.402823669\\times10^{11}$, mass per processor $m_{\\text{proc}}=10^{-3}\\ \\text{kg}$",
    "formula": "$M=p\\times m_{\\text{proc}}$"
  },
  {
    "id": "Q6",
    "statement": "Energy consumption of the 128‑bit exhaustive search is $E=9.5\\times10^{17}\\ \\text{J}$.",
    "inputs": "Landauer energy per operation $\\varepsilon_{\\text{L}}=2.8\\times10^{-21}\\ \\text{J}$, search space $S(128)=3.402823669\\times10^{38}$",
    "formula": "$E=\\varepsilon_{\\text{L}}\\times S(128)$"
  },
  {
    "id": "Q7",
    "statement": "Energy‑limited critical key length is $n^{*}=301$ bits.",
    "inputs": "Effective operation budget $B_{\\text{ops}}^{\\text{eff}}=5.24\\times10^{90}$",
    "formula": "$n^{*}=\\left\\lfloor\\log_{2}\\!\\left(B_{\\text{ops}}^{\\text{eff}}\\right)\\right\\rfloor$"
  },
  {
    "id": "Q8",
    "statement": "Margin for a 128‑bit key is $\\mu_{128}=1.54\\times10^{52}$.",
    "inputs": "Effective operation budget $B_{\\text{ops}}^{\\text{eff}}=5.24\\times10^{90}$, $2^{128}=3.402823669\\times10^{38}$",
    "formula": "$\\mu_{128}=B_{\\text{ops}}^{\\text{eff}}/2^{128}$"
  },
  {
    "id": "Q9",
    "statement": "Margin for a 256‑bit key is $\\mu_{256}=4.52\\times10^{13}$.",
    "inputs": "Effective operation budget $B_{\\text{ops}}^{\\text{eff}}=5.24\\times10^{90}$, $2^{256}=1.157920892\\times10^{77}$",
    "formula": "$\\mu_{256}=B_{\\text{ops}}^{\\text{eff}}/2^{256}$"
  },
  {
    "id": "Q10",
    "statement": "Margin for a 2048‑bit key is $\\mu_{2048}=1.62\\times10^{-526}$.",
    "inputs": "Effective operation budget $B_{\\text{ops}}^{\\text{eff}}=5.24\\times10^{90}$, $2^{2048}=3.23\\times10^{616}$",
    "formula": "$\\mu_{2048}=B_{\\text{ops}}^{\\text{eff}}/2^{2048}$"
  },
  {
    "id": "Q11",
    "statement": "Margin for exhaustive simulation of 500‑bit programs is $\\mu_{500}=1.60\\times10^{-60}$.",
    "inputs": "Effective operation budget $B_{\\text{ops}}^{\\text{eff}}=5.24\\times10^{90}$, $2^{500}=3.27\\times10^{150}$",
    "formula": "$\\mu_{500}=B_{\\text{ops}}^{\\text{eff}}/2^{500}$"
  },
  {
    "id": "Q12",
    "statement": "Margin for the RNA‑based molecular computer described in [4] is $\\mu_{\\text{RNA}}=4.6\\times10^{75}$.",
    "inputs": "Effective operation budget $B_{\\text{ops}}^{\\text{eff}}=5.24\\times10^{90}$, configuration space $2^{50}=1.13\\times10^{15}$",
    "formula": "$\\mu_{\\text{RNA}}=B_{\\text{ops}}^{\\text{eff}}/2^{50}$"
  },
  {
    "id": "Q13",
    "statement": "Energy required for a neutrino‑beam experiment with $N_{\\nu}=10^{12}$ neutrinos of $300\\ \\text{keV}$ each is $E_{\\text{beam}}\\approx4.8\\times10^{-2}\\ \\text{J}$.",
    "inputs": "Number of neutrinos $N_{\\nu}=10^{12}$, energy per neutrino $E_{\\nu}=300\\ \\text{keV}=4.806\\times10^{-14}\\ \\text{J}$",
    "formula": "$E_{\\text{beam}}=N_{\\nu}\\times E_{\\nu}$"
  },
  {
    "id": "Q14",
    "statement": "Operation rate of the deep‑learning retinal model is $\\dot{N}_{\\text{CNN}}=10^{13}\\ \\text{ops\\,s}^{-1}$.",
    "inputs": "Number of parameters $L=10^{7}$, video frame rate $10^{6}\\ \\text{frames\\,s}^{-1}$",
    "formula": "$\\dot{N}_{\\text{CNN}}=L\\times10^{6}$"
  },
  {
    "id": "Q15",
    "statement": "Total energy consumed by the retinal model if run for the age of the universe is $E\\approx10^{19}\\ \\text{J}$.",
    "inputs": "Operation rate $\\dot{N}_{\\text{CNN}}=10^{13}\\ \\text{ops\\,s}^{-1}$, universe age $T_{\\text{univ}}=10^{18}\\ \\text{s}$, energy per operation $\\varepsilon=10^{-12}\\ \\text{J}$",
    "formula": "$E=\\dot{N}_{\\text{CNN}}\\times T_{\\text{univ}}\\times \\varepsilon$"
  },
  {
    "id": "Q16",
    "statement": "Projected hardware cost for the 128‑bit parallel implementation is $\\$3.4\\times10^{13}$ (≈ \\$34 trillion).",
    "inputs": "Hardware mass $M=3.4\\times10^{8}\\ \\text{kg}$, cost per kilogram $c_{\\text{kg}}=10^{5}\\ \\$\\,\\text{kg}^{-1}$",
    "formula": "$\\text{Cost}=M\\times c_{\\text{kg}}$"
  }
]

## Script
```python
import math
from decimal import Decimal, getcontext

# Set high precision for large exponent calculations
getcontext().prec = 30

def fmt(val, sig):
    """Round to given significant figures and format in scientific notation."""
    if val == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(val))))
    factor = round(val / (10 ** exponent), sig - 1)
    return f"{factor:.{sig-1}f}e{exponent}"

def print_claim(cid, computed, expected_str, sig):
    # Round computed to the number of significant digits in expected
    expected_sig = len(expected_str.replace('.', '').replace('e', '').replace('+', '').replace('-', '')) - 1
    comp_str = fmt(computed, expected_sig)
    match = "yes" if comp_str == expected_str else "no"
    print(f"CLAIM {cid}: computed={comp_str} expected={expected_str} match={match}")

# Q1
N_atoms = Decimal('1e80')
m_p = Decimal('1.67e-27')
c = Decimal('3.00e8')
B_E = N_atoms * m_p * c * c
print_claim("Q1", float(B_E), "1.5e70", 2)

# Q2
kB = Decimal('1.38e-23')
T = Decimal('300')
ln2 = Decimal('0.6931')
E_min = kB * T * ln2
B_E_exact = Decimal('1.503e70')
B_ops_eff = B_E_exact / E_min
print_claim("Q2", float(B_ops_eff), "5.24e90", 3)

# Q3
S128 = Decimal('3.402823669e38')
f = Decimal('1e9')
T_seq = S128 / f
print_claim("Q3", float(T_seq), "3.4e29", 2)

# Q4
T_max = Decimal('1e18')
p = S128 / (f * T_max)
print_claim("Q4", float(p), "3.4e11", 2)

# Q5
m_proc = Decimal('1e-3')
M = p * m_proc
print_claim("Q5", float(M), "3.4e8", 2)

# Q6
epsilon_L = Decimal('2.8e-21')
E = epsilon_L * S128
print_claim("Q6", float(E), "9.5e17", 2)

# Q7
log2_Bops = (Decimal(B_ops_eff).ln() / Decimal(2).ln())
n_star = int(log2_Bops.to_integral_value(rounding='ROUND_FLOOR'))
print_claim("Q7", n_star, "301", 3)

# Q8
mu_128 = B_ops_eff / S128
print_claim("Q8", float(mu_128), "1.54e52", 3)

# Q9
S256 = Decimal('1.157920892e77')
mu_256 = B_ops_eff / S256
print_claim("Q9", float(mu_256), "4.52e13", 3)

# Q10
S2048 = Decimal('3.23e616')
mu_2048 = B_ops_eff / S2048
print_claim("Q10", float(mu_2048), "1.62e-526", 3)

# Q11
S500 = Decimal('3.27e150')
mu_500 = B_ops_eff / S500
print_claim("Q11", float(mu_500), "1.60e-60", 3)

# Q12
S50 = Decimal('1.13e15')
mu_RNA = B_ops_eff / S50
print_claim("Q12", float(mu_RNA), "4.6e75", 2)

# Q13
N_nu = Decimal('1e12')
E_nu = Decimal('4.806e-14')
E_beam = N_nu * E_nu
print_claim("Q13", float(E_beam), "4.8e-2", 2)

# Q14
L = Decimal('1e7')
frame_rate = Decimal('1e6')
dotN_CNN = L * frame_rate
print_claim("Q14", float(dotN_CNN), "1e13", 1)

# Q15
T_univ = Decimal('1e18')
epsilon = Decimal('1e-12')
E_retina = dotN_CNN * T_univ * epsilon
print_claim("Q15", float(E_retina), "1e19", 1)

# Q16
M_hardware = Decimal('3.4e8')
cost_per_kg = Decimal('1e5')
cost = M_hardware * cost_per_kg
print_claim("Q16", float(cost), "3.4e13", 2)

print("VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.50e70 expected=1.5e70 match=no
CLAIM Q2: computed=5.238e90 expected=5.24e90 match=no
CLAIM Q3: computed=3.40e29 expected=3.4e29 match=no
CLAIM Q4: computed=3.40e11 expected=3.4e11 match=no
CLAIM Q5: computed=3.4e8 expected=3.4e8 match=yes
CLAIM Q6: computed=9.53e17 expected=9.5e17 match=no
CLAIM Q7: computed=3.0e2 expected=301 match=no
CLAIM Q8: computed=1.539e52 expected=1.54e52 match=no
CLAIM Q9: computed=4.524e13 expected=4.52e13 match=no
CLAIM Q10: computed=0 expected=1.62e-526 match=no
CLAIM Q11: computed=1.602e-60 expected=1.60e-60 match=no
CLAIM Q12: computed=4.64e75 expected=4.6e75 match=no
CLAIM Q13: computed=4.8e-2 expected=4.8e-2 match=yes
CLAIM Q14: computed=1.0e13 expected=1e13 match=no
CLAIM Q15: computed=1.0e19 expected=1e19 match=no
CLAIM Q16: computed=3.40e13 expected=3.4e13 match=no
VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.50e70 | 1.5e70 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 5.238e90 | 5.24e90 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 3.40e29 | 3.4e29 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 3.40e11 | 3.4e11 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 3.4e8 | 3.4e8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 9.53e17 | 9.5e17 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 3.0e2 | 301 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 1.539e52 | 1.54e52 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 4.524e13 | 4.52e13 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 0 | 1.62e-526 | no | match | stated value is zero |
| Q11 | 1.602e-60 | 1.60e-60 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 4.64e75 | 4.6e75 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 4.8e-2 | 4.8e-2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 1.0e13 | 1e13 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 1.0e19 | 1e19 | no | match | 3 significant digits (as printed, at least 3) |
| Q16 | 3.40e13 | 3.4e13 | no | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
