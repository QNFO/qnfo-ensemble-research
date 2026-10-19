# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The number of Hilbert‑space amplitudes for a 50‑unit system is $H(50)=2^{50}\\approx1.1259\\times10^{15}$.",
    "inputs": "n = 50",
    "formula": "H = 2^n"
  },
  {
    "id": "Q2",
    "statement": "The number of pairwise relational parameters for 50 units is $R(50)=\\frac{50\\times49}{2}=1225$.",
    "inputs": "n = 50",
    "formula": "R = n*(n-1)/2"
  },
  {
    "id": "Q3",
    "statement": "The compression factor between Hilbert amplitudes and pairwise parameters is $\\rho(50)=9.19\\times10^{11}$.",
    "inputs": "H = 1.1259e15 (from Q1), R = 1225 (from Q2)",
    "formula": "rho = H / R"
  },
  {
    "id": "Q4",
    "statement": "Storing all complex amplitudes for $n=50$ in double‑precision requires $16\\times2^{50}=1.80144\\times10^{16}$ bytes, i.e. $18.014$ PB.",
    "inputs": "n = 50, bytes per amplitude = 16",
    "formula": "memory_H = 16 * 2^n"
  },
  {
    "id": "Q5",
    "statement": "Storing the pairwise relational description for $n=50$ needs $16\\times1225=19{,}600$ bytes $=1.96\\times10^{4}$ bytes.",
    "inputs": "R = 1225 (from Q2), bytes per parameter = 16",
    "formula": "memory_R = 16 * R"
  },
  {
    "id": "Q6",
    "statement": "The lower bound of the one‑sigma admissibility band is $\\sigma_E/Q_{\\beta\\beta}=2.1233\\times10^{-3}$.",
    "inputs": "FWHM lower = 0.005 (0.5 %), conversion factor c = 2.354820",
    "formula": "sigma/Q = (FWHM/Q) / c"
  },
  {
    "id": "Q7",
    "statement": "The upper bound of the one‑sigma admissibility band is $\\sigma_E/Q_{\\beta\\beta}=4.2466\\times10^{-3}$.",
    "inputs": "FWHM upper = 0.01 (1 %), conversion factor c = 2.354820",
    "formula": "sigma/Q = (FWHM/Q) / c"
  },
  {
    "id": "Q8",
    "statement": "For five independent stages each with relative error $\\varepsilon=10^{-2}$, the worst‑case linear stack error is $5\\times10^{-2}$.",
    "inputs": "n = 5, epsilon = 1e-2",
    "formula": "epsilon_WC = n * epsilon"
  },
  {
    "id": "Q9",
    "statement": "For the same five stages, the root‑sum‑square (RSS) stack error is $2.2361\\times10^{-2}$.",
    "inputs": "n = 5, epsilon = 1e-2",
    "formula": "epsilon_RSS = sqrt(n) * epsilon"
  },
  {
    "id": "Q10",
    "statement": "The ratio of worst‑case to RSS error for five stages is $\\sqrt{5}=2.2361$.",
    "inputs": "n = 5",
    "formula": "ratio = sqrt(n)"
  },
  {
    "id": "Q11",
    "statement": "At a frame rate of $90\\,$Hz the frame period is $T_f=1/90=0.011111\\,$s $=11.111\\,$ms.",
    "inputs": "f = 90 Hz",
    "formula": "T_f = 1 / f"
  },
  {
    "id": "Q12",
    "statement": "A single $90\\,$Hz frame consumes $55.6\\%$ of a $20\\,$ms motion‑to‑photon latency budget.",
    "inputs": "T_f = 11.111 ms (from Q11), B = 20 ms",
    "formula": "percentage = T_f / B"
  },
  {
    "id": "Q13",
    "statement": "One‑frame persistence at $90\\,$Hz blurs a head motion of $\\omega=360\\,\\mathrm{deg/s}$ by $\\theta_{blur}=4.0^{\\circ}$.",
    "inputs": "omega = 360 deg/s, p = 1, T_f = 0.011111 s (from Q11)",
    "formula": "theta_blur = omega * p * T_f"
  },
  {
    "id": "Q14",
    "statement": "Inter‑sample angular travel at $60\\,$Hz is $\\theta_{sample}=6.0^{\\circ}$ for $\\omega=360\\,\\mathrm{deg/s}$.",
    "inputs": "omega = 360 deg/s, f_t = 60 Hz",
    "formula": "theta_sample = omega / f_t"
  },
  {
    "id": "Q15",
    "statement": "Inter‑sample angular travel at $1000\\,$Hz is $\\theta_{sample}=0.36^{\\circ}$ for $\\omega=360\\,\\mathrm{deg/s}$.",
    "inputs": "omega = 360 deg/s, f_t = 1000 Hz",
    "formula": "theta_sample = omega / f_t"
  },
  {
    "id": "Q16",
    "statement": "The ratio of angular travel between $60\\,$Hz and $1000\\,$Hz trackers is $16.7$.",
    "inputs": "theta_60 = 6.0 deg (from Q14), theta_1000 = 0.36 deg (from Q15)",
    "formula": "ratio = theta_60 / theta_1000"
  }
]

## Script
```python
import math

# Q1
H = 2**50
expected_Q1 = "1.1259e15"
print(f"CLAIM Q1: computed={H:.6g} expected={expected_Q1} match={'yes' if f'{H:.6g}'==expected_Q1 else 'no'}")

# Q2
R = 50*49//2
expected_Q2 = "1225"
print(f"CLAIM Q2: computed={R} expected={expected_Q2} match={'yes' if str(R)==expected_Q2 else 'no'}")

# Q3
rho = H / R
expected_Q3 = "9.19e11"
print(f"CLAIM Q3: computed={rho:.3e} expected={expected_Q3} match={'yes' if f'{rho:.3e}'==expected_Q3 else 'no'}")

# Q4
memory_H = 16 * 2**50
memory_H_PB = memory_H / 1e15
expected_Q4 = "18.014"
print(f"CLAIM Q4: computed={memory_H_PB:.3f} expected={expected_Q4} match={'yes' if f'{memory_H_PB:.3f}'==expected_Q4 else 'no'}")

# Q5
memory_R = 16 * R
expected_Q5 = "1.96e4"
print(f"CLAIM Q5: computed={memory_R:.2e} expected={expected_Q5} match={'yes' if f'{memory_R:.2e}'==expected_Q5 else 'no'}")

# Q6
sigma_low = 0.005 / 2.354820
expected_Q6 = "2.1233e-3"
print(f"CLAIM Q6: computed={sigma_low:.4e} expected={expected_Q6} match={'yes' if f'{sigma_low:.4e}'==expected_Q6 else 'no'}")

# Q7
sigma_high = 0.01 / 2.354820
expected_Q7 = "4.2466e-3"
print(f"CLAIM Q7: computed={sigma_high:.4e} expected={expected_Q7} match={'yes' if f'{sigma_high:.4e}'==expected_Q7 else 'no'}")

# Q8
epsilon_wc = 5 * 1e-2
expected_Q8 = "5e-2"
print(f"CLAIM Q8: computed={epsilon_wc:.2e} expected={expected_Q8} match={'yes' if f'{epsilon_wc:.2e}'==expected_Q8 else 'no'}")

# Q9
epsilon_rss = math.sqrt(5) * 1e-2
expected_Q9 = "2.2361e-2"
print(f"CLAIM Q9: computed={epsilon_rss:.4e} expected={expected_Q9} match={'yes' if f'{epsilon_rss:.4e}'==expected_Q9 else 'no'}")

# Q10
ratio = math.sqrt(5)
expected_Q10 = "2.2361"
print(f"CLAIM Q10: computed={ratio:.4f} expected={expected_Q10} match={'yes' if f'{ratio:.4f}'==expected_Q10 else 'no'}")

# Q11
Tf = 1/90
expected_Q11 = "0.011111 s = 11.111 ms"
computed_Q11 = f"{Tf:.6f} s = {Tf*1000:.3f} ms"
print(f"CLAIM Q11: computed={computed_Q11} expected={expected_Q11} match={'yes' if computed_Q11==expected_Q11 else 'no'}")

# Q12
percentage = (Tf*1000) / 20 * 100  # using ms values
expected_Q12 = "55.6%"
print(f"CLAIM Q12: computed={percentage:.1f}% expected={expected_Q12} match={'yes' if f'{percentage:.1f}%'==expected_Q12 else 'no'}")

# Q13
theta_blur = 360 * 1 * Tf
expected_Q13 = "4.0"
print(f"CLAIM Q13: computed={theta_blur:.1f} expected={expected_Q13} match={'yes' if f'{theta_blur:.1f}'==expected_Q13 else 'no'}")

# Q14
theta_sample_60 = 360 / 60
expected_Q14 = "6.0"
print(f"CLAIM Q14: computed={theta_sample_60:.1f} expected={expected_Q14} match={'yes' if f'{theta_sample_60:.1f}'==expected_Q14 else 'no'}")

# Q15
theta_sample_1000 = 360 / 1000
expected_Q15 = "0.36"
print(f"CLAIM Q15: computed={theta_sample_1000:.2f} expected={expected_Q15} match={'yes' if f'{theta_sample_1000:.2f}'==expected_Q15 else 'no'}")

# Q16
ratio_ang = theta_sample_60 / theta_sample_1000
expected_Q16 = "16.7"
print(f"CLAIM Q16: computed={ratio_ang:.1f} expected={expected_Q16} match={'yes' if f'{ratio_ang:.1f}'==expected_Q16 else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in open(__file__) if 'match=yes' in line)} match, {sum(1 for line in open(__file__) if 'match=no' in line)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.1259e+15 expected=1.1259e15 match=no
CLAIM Q2: computed=1225 expected=1225 match=yes
CLAIM Q3: computed=9.191e+11 expected=9.19e11 match=no
CLAIM Q4: computed=18.014 expected=18.014 match=yes
CLAIM Q5: computed=1.96e+04 expected=1.96e4 match=no
CLAIM Q6: computed=2.1233e-03 expected=2.1233e-3 match=no
CLAIM Q7: computed=4.2466e-03 expected=4.2466e-3 match=no
CLAIM Q8: computed=5.00e-02 expected=5e-2 match=no
CLAIM Q9: computed=2.2361e-02 expected=2.2361e-2 match=no
CLAIM Q10: computed=2.2361 expected=2.2361 match=yes
CLAIM Q11: computed=0.011111 s = 11.111 ms expected=0.011111 s = 11.111 ms match=yes
CLAIM Q12: computed=55.6% expected=55.6% match=yes
CLAIM Q13: computed=4.0 expected=4.0 match=yes
CLAIM Q14: computed=6.0 expected=6.0 match=yes
CLAIM Q15: computed=0.36 expected=0.36 match=yes
CLAIM Q16: computed=16.7 expected=16.7 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 85, in <module>
NameError: name '__file__' is not defined. Did you mean: '__name__'?

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.1259e+15 | 1.1259e15 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 1225 | 1225 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 9.191e+11 | 9.19e11 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 18.014 | 18.014 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 1.96e+04 | 1.96e4 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 2.1233e-03 | 2.1233e-3 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 4.2466e-03 | 4.2466e-3 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 5.00e-02 | 5e-2 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 2.2361e-02 | 2.2361e-2 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 2.2361 | 2.2361 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 55.6% | 55.6% | yes | match | script verdict (values not both numeric) |
| Q13 | 4.0 | 4.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 6.0 | 6.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 0.36 | 0.36 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 16.7 | 16.7 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15.
