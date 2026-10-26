# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Environmental decoherence rate for the chosen molecule is $1.2\\times10^{7}\\,\\mathrm{s^{-1}}$.",
    "inputs": "m = 1.66e-23 kg, k_B = 1.38e-23 J K^{-1}, T = 300 K, \\hbar = 1.055e-34 J s, \\Delta x = 1e-9 m",
    "formula": "Gamma_env = (2 * m * k_B * T / \\hbar^2) * (\\Delta x)^2"
  },
  {
    "id": "Q2",
    "statement": "Consciousness‑driven collapse rate under assumed parameters is $1.0\\times10^{-7}\\,\\mathrm{s^{-1}}$.",
    "inputs": "alpha = 1e-13 s^{-1} bit^{-1}, I = 1e6 bits",
    "formula": "Gamma_c = alpha * I"
  },
  {
    "id": "Q3",
    "statement": "Total decoherence rate is dominated by the environmental term, yielding $\\approx1.2\\times10^{7}\\,\\mathrm{s^{-1}}$.",
    "inputs": "Gamma_env from Q1, Gamma_c from Q2",
    "formula": "Gamma_tot = Gamma_env + Gamma_c"
  },
  {
    "id": "Q4",
    "statement": "Zeno‑effect bound $\\alpha < 10^{-5}\\,\\mathrm{s^{-1}\\,bit^{-1}}$ follows from sustained Rabi oscillations in a superconducting qubit.",
    "inputs": "Gamma_c_max = 1e-5 s^{-1}, I \\ge 1 bit",
    "formula": "alpha < Gamma_c_max / I"
  },
  {
    "id": "Q5",
    "statement": "Coherence time $\\tau_{\\text{coh}} = 1/\\Gamma_{\\text{tot}} \\approx 8.1\\times10^{-8}\\,\\text{s}$.",
    "inputs": "Gamma_tot \\approx 1.235e7 s^{-1}",
    "formula": "tau_coh = 1 / Gamma_tot"
  },
  {
    "id": "Q6",
    "statement": "Increasing $\\alpha$ to $10^{-5}\\,\\mathrm{s^{-1}\\,bit^{-1}}$ raises $\\Gamma_{\\text{c}}$ to $10^{1}\\,\\mathrm{s^{-1}}$.",
    "inputs": "alpha = 1e-5 s^{-1} bit^{-1}, I = 1e6 bits",
    "formula": "Gamma_c = alpha * I"
  },
  {
    "id": "Q7",
    "statement": "Reducing temperature to $1\\,\\text{K}$ lowers $\\Gamma_{\\text{env}}$ by a factor of $300$, giving $\\Gamma_{\\text{env}}\\approx4.1\\times10^{4}\\,\\mathrm{s^{-1}}$.",
    "inputs": "Gamma_env_original = 1.235e7 s^{-1} at T_original = 300 K, T_new = 1 K",
    "formula": "Gamma_env_new = Gamma_env_original * (T_new / T_original)"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1
m = 1.66e-23  # kg
kB = 1.38e-23  # J/K
T = 300.0  # K
hbar = 1.055e-34  # J·s
dx = 1e-9  # m
Gamma_env = (2 * m * kB * T / hbar**2) * dx**2
Gamma_env_rounded = round_sig(Gamma_env, 2)  # 2 sig figs as in "1.2×10^7"
expected_Q1 = "1.2e7"
match_Q1 = "yes" if f"{Gamma_env_rounded:.1e}" == expected_Q1 else "no"
print(f"CLAIM Q1: computed={Gamma_env_rounded:.1e} expected={expected_Q1} match={match_Q1}")

# Q2
alpha = 1e-13  # s^-1 bit^-1
I = 1e6  # bits
Gamma_c = alpha * I
Gamma_c_rounded = round_sig(Gamma_c, 2)  # 2 sig figs as in "1.0×10^-7"
expected_Q2 = "1.0e-7"
match_Q2 = "yes" if f"{Gamma_c_rounded:.1e}" == expected_Q2 else "no"
print(f"CLAIM Q2: computed={Gamma_c_rounded:.1e} expected={expected_Q2} match={match_Q2}")

# Q3
Gamma_tot = Gamma_env + Gamma_c
Gamma_tot_rounded = round_sig(Gamma_tot, 2)  # 2 sig figs as in "1.2×10^7"
expected_Q3 = "1.2e7"
match_Q3 = "yes" if f"{Gamma_tot_rounded:.1e}" == expected_Q3 else "no"
print(f"CLAIM Q3: computed={Gamma_tot_rounded:.1e} expected={expected_Q3} match={match_Q3}")

# Q4
Gamma_c_max = 1e-5  # s^-1
I_min = 1.0  # bit (>=1)
alpha_bound = Gamma_c_max / I_min
alpha_bound_rounded = round_sig(alpha_bound, 1)  # 1 sig fig as in "1×10^-5"
expected_Q4 = "1e-5"
match_Q4 = "yes" if f"{alpha_bound_rounded:.0e}" == expected_Q4 else "no"
print(f"CLAIM Q4: computed={alpha_bound_rounded:.0e} expected={expected_Q4} match={match_Q4}")

# Q5
Gamma_tot_approx = 1.235e7  # s^-1 (from paper)
tau_coh = 1.0 / Gamma_tot_approx
tau_coh_rounded = round_sig(tau_coh, 2)  # 2 sig figs as in "8.1×10^-8"
expected_Q5 = "8.1e-8"
match_Q5 = "yes" if f"{tau_coh_rounded:.1e}" == expected_Q5 else "no"
print(f"CLAIM Q5: computed={tau_coh_rounded:.1e} expected={expected_Q5} match={match_Q5}")

# Q6
alpha_high = 1e-5  # s^-1 bit^-1
Gamma_c_high = alpha_high * I
Gamma_c_high_rounded = round_sig(Gamma_c_high, 1)  # 1 sig fig as in "10"
expected_Q6 = "10"
match_Q6 = "yes" if f"{Gamma_c_high_rounded:.0f}" == expected_Q6 else "no"
print(f"CLAIM Q6: computed={Gamma_c_high_rounded:.0f} expected={expected_Q6} match={match_Q6}")

# Q7
Gamma_env_original = 1.235e7  # s^-1 at 300 K
T_original = 300.0
T_new = 1.0
Gamma_env_new = Gamma_env_original * (T_new / T_original)
Gamma_env_new_rounded = round_sig(Gamma_env_new, 2)  # 2 sig figs as in "4.1×10^4"
expected_Q7 = "4.1e4"
match_Q7 = "yes" if f"{Gamma_env_new_rounded:.1e}" == expected_Q7 else "no"
print(f"CLAIM Q7: computed={Gamma_env_new_rounded:.1e} expected={expected_Q7} match={match_Q7}")

print(f"VERIFICATION SUMMARY: 7 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.2e+07 expected=1.2e7 match=no
CLAIM Q2: computed=1.0e-07 expected=1.0e-7 match=no
CLAIM Q3: computed=1.2e+07 expected=1.2e7 match=no
CLAIM Q4: computed=1e-05 expected=1e-5 match=no
CLAIM Q5: computed=8.1e-08 expected=8.1e-8 match=no
CLAIM Q6: computed=10 expected=10 match=yes
CLAIM Q7: computed=4.1e+04 expected=4.1e4 match=no

[stderr]
Traceback (most recent call last):
  File "<string>", line 71, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.2e+07 | 1.2e7 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 1.0e-07 | 1.0e-7 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1.2e+07 | 1.2e7 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 1e-05 | 1e-5 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 8.1e-08 | 8.1e-8 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 4.1e+04 | 4.1e4 | no | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 7.
