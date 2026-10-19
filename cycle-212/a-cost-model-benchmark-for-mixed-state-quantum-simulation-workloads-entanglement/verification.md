# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For a 10‑qubit register the mixed‑to‑pure memory ratio is $R_{10}=1{,}024$.",
    "inputs": "n=10",
    "formula": "R_n = 2^n"
  },
  {
    "id": "Q2",
    "statement": "Pure‑state storage for $n=10$ qubits requires $2^{10}\\times16=16{,}384$ bytes = 16 KiB.",
    "inputs": "n=10, bytes_per_complex=16",
    "formula": "storage_pure = 2^n * bytes_per_complex"
  },
  {
    "id": "Q3",
    "statement": "Density‑matrix storage for $n=10$ qubits requires $4^{10}\\times16=16{,}777{,}216$ bytes = 16 MiB.",
    "inputs": "n=10, bytes_per_complex=16",
    "formula": "storage_density = 4^n * bytes_per_complex"
  },
  {
    "id": "Q4",
    "statement": "Entanglement of formation for $p=0.5$ is $E_{F}=1.000000$ ebits.",
    "inputs": "p=0.5",
    "formula": "E_F = -p*log2(p) - (1-p)*log2(1-p)"
  },
  {
    "id": "Q5",
    "statement": "Entanglement of formation for $p=0.25$ is $E_{F}=0.811278$ ebits.",
    "inputs": "p=0.25",
    "formula": "E_F = -p*log2(p) - (1-p)*log2(1-p)"
  },
  {
    "id": "Q6",
    "statement": "Entanglement of formation for $p=0.9$ is $E_{F}=0.468996$ ebits.",
    "inputs": "p=0.9",
    "formula": "E_F = -p*log2(p) - (1-p)*log2(1-p)"
  },
  {
    "id": "Q7",
    "statement": "The sensitivity $\\,\\mathrm{d}E_{F}/\\mathrm{d}p$ at $p=0.5$ equals $0$ ebits per unit $p$.",
    "inputs": "p=0.5",
    "formula": "dE_F/dp = log2((1-p)/p)"
  },
  {
    "id": "Q8",
    "statement": "A sweep over $K=21$ parameter values on $n=10$ qubits consumes $M_{\\text{sweep}}=352{,}321{,}536$ bytes (≈352 MB).",
    "inputs": "K=21, n=10, bytes_per_complex=16",
    "formula": "M_sweep = K * 4^n * bytes_per_complex"
  },
  {
    "id": "Q9",
    "statement": "The parameter‑averaged entanglement cost is $\\overline{E_{F}}=0.760091$ ebits.",
    "inputs": "E_F(p=0.25)=0.811278, E_F(p=0.5)=1.000000, E_F(p=0.9)=0.468996",
    "formula": "E_F_avg = (E_F1 + E_F2 + E_F3) / 3"
  },
  {
    "id": "Q10",
    "statement": "The composite difficulty score for $n=10$ is $\\Sigma(10)=778.333$ weighted ebit‑units.",
    "inputs": "R_10=1024, E_F_avg=0.760091",
    "formula": "Sigma = R_n * E_F_avg"
  },
  {
    "id": "Q11",
    "statement": "Energy per simulation step for $n=10$ is $E_{\\text{step}}=3.3554432\\times10^{-3}$ J.",
    "inputs": "n=10, e_DRAM=1e-10 J/byte, f_orch=2, bytes_per_complex=16",
    "formula": "E_step = 4^n * bytes_per_complex * e_DRAM * f_orch"
  },
  {
    "id": "Q12",
    "statement": "A $10^{4}$‑step workload consumes $E_{\\text{workload}}=33.554432$ J.",
    "inputs": "S=10000, E_step=3.3554432e-3 J",
    "formula": "E_workload = S * E_step"
  },
  {
    "id": "Q13",
    "statement": "For $n=5$ qubits the representation‑overhead ratio is $R_{5}=32$.",
    "inputs": "n=5",
    "formula": "R_n = 2^n"
  },
  {
    "id": "Q14",
    "statement": "A factor‑3 variation in the DRAM coefficient yields an energy range of roughly $11$–$101$ J for the $10^{4}$‑step workload.",
    "inputs": "E_workload_base=33.554432 J, factor=3",
    "formula": "E_lower = E_workload_base / factor; E_upper = E_workload_base * factor"
  }
]

## Script
```python
import math

def fmt(val, sig=6):
    """Format a float to the given number of significant digits."""
    if val == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(val))))
    digits = sig - order - 1
    fmt_str = "{:." + str(max(digits, 0)) + "f}"
    return fmt_str.format(val)

# Q1
R_10 = 2**10
expected_Q1 = 1024
match_Q1 = fmt(R_10) == fmt(expected_Q1)
print(f"CLAIM Q1: computed={R_10} expected={expected_Q1} match={'yes' if match_Q1 else 'no'}")

# Q2
n = 10
bytes_per_complex = 16
storage_pure = (2**n) * bytes_per_complex
expected_Q2 = 16384
match_Q2 = fmt(storage_pure) == fmt(expected_Q2)
print(f"CLAIM Q2: computed={storage_pure} expected={expected_Q2} match={'yes' if match_Q2 else 'no'}")

# Q3
storage_density = (4**n) * bytes_per_complex
expected_Q3 = 16777216
match_Q3 = fmt(storage_density) == fmt(expected_Q3)
print(f"CLAIM Q3: computed={storage_density} expected={expected_Q3} match={'yes' if match_Q3 else 'no'}")

# Q4
p = 0.5
E_F_0_5 = -p*math.log2(p) - (1-p)*math.log2(1-p)
expected_Q4 = 1.000000
match_Q4 = fmt(E_F_0_5, sig=7) == fmt(expected_Q4, sig=7)
print(f"CLAIM Q4: computed={E_F_0_5:.6f} expected={expected_Q4:.6f} match={'yes' if match_Q4 else 'no'}")

# Q5
p = 0.25
E_F_0_25 = -p*math.log2(p) - (1-p)*math.log2(1-p)
expected_Q5 = 0.811278
match_Q5 = fmt(E_F_0_25, sig=7) == fmt(expected_Q5, sig=7)
print(f"CLAIM Q5: computed={E_F_0_25:.6f} expected={expected_Q5:.6f} match={'yes' if match_Q5 else 'no'}")

# Q6
p = 0.9
E_F_0_9 = -p*math.log2(p) - (1-p)*math.log2(1-p)
expected_Q6 = 0.468996
match_Q6 = fmt(E_F_0_9, sig=7) == fmt(expected_Q6, sig=7)
print(f"CLAIM Q6: computed={E_F_0_9:.6f} expected={expected_Q6:.6f} match={'yes' if match_Q6 else 'no'}")

# Q7
p = 0.5
dE_dp = math.log2((1-p)/p)
expected_Q7 = 0.0
match_Q7 = fmt(dE_dp) == fmt(expected_Q7)
print(f"CLAIM Q7: computed={dE_dp} expected={expected_Q7} match={'yes' if match_Q7 else 'no'}")

# Q8
K = 21
M_sweep = K * (4**n) * bytes_per_complex
expected_Q8 = 352321536
match_Q8 = fmt(M_sweep) == fmt(expected_Q8)
print(f"CLAIM Q8: computed={M_sweep} expected={expected_Q8} match={'yes' if match_Q8 else 'no'}")

# Q9
E_F_vals = [0.811278, 1.000000, 0.468996]
E_F_avg = sum(E_F_vals) / 3.0
expected_Q9 = 0.760091
match_Q9 = fmt(E_F_avg, sig=7) == fmt(expected_Q9, sig=7)
print(f"CLAIM Q9: computed={E_F_avg:.6f} expected={expected_Q9:.6f} match={'yes' if match_Q9 else 'no'}")

# Q10
Sigma = R_10 * E_F_avg
expected_Q10 = 778.333
# compare with 6 significant digits as in the paper
match_Q10 = fmt(Sigma, sig=6) == fmt(expected_Q10, sig=6)
print(f"CLAIM Q10: computed={Sigma:.6f} expected={expected_Q10:.6f} match={'yes' if match_Q10 else 'no'}")

# Q11
e_DRAM = 1e-10
f_orch = 2
E_step = (4**n) * bytes_per_complex * e_DRAM * f_orch
expected_Q11 = 3.3554432e-3
match_Q11 = fmt(E_step, sig=8) == fmt(expected_Q11, sig=8)
print(f"CLAIM Q11: computed={E_step:.9f} expected={expected_Q11:.9f} match={'yes' if match_Q11 else 'no'}")

# Q12
S = 10000
E_workload = S * E_step
expected_Q12 = 33.554432
match_Q12 = fmt(E_workload, sig=8) == fmt(expected_Q12, sig=8)
print(f"CLAIM Q12: computed={E_workload:.6f} expected={expected_Q12:.6f} match={'yes' if match_Q12 else 'no'}")

# Q13
R_5 = 2**5
expected_Q13 = 32
match_Q13 = fmt(R_5) == fmt(expected_Q13)
print(f"CLAIM Q13: computed={R_5} expected={expected_Q13} match={'yes' if match_Q13 else 'no'}")

# Q14
factor = 3
E_lower = E_workload / factor
E_upper = E_workload * factor
# Expected range "11–101" (approximate). We'll compare rounded integers.
match_Q14 = (round(E_lower) == 11) and (round(E_upper) == 101)
print(f"CLAIM Q14: computed={E_lower:.6f}–{E_upper:.6f} expected=11–101 match={'yes' if match_Q14 else 'no'}")

```

## Execution output
```
CLAIM Q1: computed=1024 expected=1024 match=yes
CLAIM Q2: computed=16384 expected=16384 match=yes
CLAIM Q3: computed=16777216 expected=16777216 match=yes
CLAIM Q4: computed=1.000000 expected=1.000000 match=yes
CLAIM Q5: computed=0.811278 expected=0.811278 match=no
CLAIM Q6: computed=0.468996 expected=0.468996 match=no
CLAIM Q7: computed=0.0 expected=0.0 match=yes
CLAIM Q8: computed=352321536 expected=352321536 match=yes
CLAIM Q9: computed=0.760091 expected=0.760091 match=no
CLAIM Q10: computed=778.333525 expected=778.333000 match=no
CLAIM Q11: computed=0.003355443 expected=0.003355443 match=yes
CLAIM Q12: computed=33.554432 expected=33.554432 match=yes
CLAIM Q13: computed=32 expected=32 match=yes
CLAIM Q14: computed=11.184811–100.663296 expected=11–101 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 16384 | 16384 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 16777216 | 16777216 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q4 | 1.000000 | 1.000000 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q5 | 0.811278 | 0.811278 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q6 | 0.468996 | 0.468996 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q7 | 0.0 | 0.0 | yes | match | stated value is zero |
| Q8 | 352321536 | 352321536 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q9 | 0.760091 | 0.760091 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q10 | 778.333525 | 778.333000 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q11 | 0.003355443 | 0.003355443 | yes | match | 7 significant digits (as printed, at least 3) |
| Q12 | 33.554432 | 33.554432 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q13 | 32 | 32 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 11.184811–100.663296 | 11–101 | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 14.
