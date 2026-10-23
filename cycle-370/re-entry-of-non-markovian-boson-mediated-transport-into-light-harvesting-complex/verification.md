# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Transfer‑time interval $\\tau_{T}\\in[0.1039,\\,0.3823]\\;\\mathrm{ps}$.",
    "inputs": "Δ_min=110\\;\\mathrm{cm^{-1}}, \\;Δ_{max}=180\\;\\mathrm{cm^{-1}}, \\;V_{min}=50\\;\\mathrm{cm^{-1}}, \\;V_{max}=75\\;\\mathrm{cm^{-1}}, \\;c=2.9979\\times10^{10}\\;\\mathrm{cm\\,s^{-1}}",
    "formula": "τ_T = Δ/(2π c V^2); compute τ_T^{min} with Δ=110, V=75 and τ_T^{max} with Δ=180, V=50"
  },
  {
    "id": "Q2",
    "statement": "Optimal dephasing rate $\\Gamma^{*}=\\Delta$ ranges from $110$ to $180\\;\\mathrm{cm^{-1}}$.",
    "inputs": "Δ_min=110\\;\\mathrm{cm^{-1}}, \\;Δ_{max}=180\\;\\mathrm{cm^{-1}}",
    "formula": "Γ^{*}=Δ"
  },
  {
    "id": "Q3",
    "statement": "Optimal hopping rate $k^{*}=V^{2}/\\Delta$ lies in $[13.89,\\,51.14]\\;\\mathrm{cm^{-1}}$.",
    "inputs": "V_{min}=50\\;\\mathrm{cm^{-1}}, \\;V_{max}=75\\;\\mathrm{cm^{-1}}, \\;Δ_{min}=110\\;\\mathrm{cm^{-1}}, \\;Δ_{max}=180\\;\\mathrm{cm^{-1}}",
    "formula": "k^{*}=V^{2}/Δ; evaluate at the four corners of the (V,Δ) box and take the minimum and maximum"
  },
  {
    "id": "Q4",
    "statement": "Corner values of $k^{*}$ are $13.8889$, $22.7273$, $31.2500$, and $51.1364\\;\\mathrm{cm^{-1}}$ for (V,Δ) = (50,180), (50,110), (75,180), (75,110) respectively.",
    "inputs": "V=50\\;\\mathrm{cm^{-1}}, \\;Δ=180\\;\\mathrm{cm^{-1}}; V=50\\;\\mathrm{cm^{-1}}, \\;Δ=110\\;\\mathrm{cm^{-1}}; V=75\\;\\mathrm{cm^{-1}}, \\;Δ=180\\;\\mathrm{cm^{-1}}; V=75\\;\\mathrm{cm^{-1}}, \\;Δ=110\\;\\mathrm{cm^{-1}}",
    "formula": "k^{*}=V^{2}/Δ"
  },
  {
    "id": "Q5",
    "statement": "Single‑hop trapping efficiency $\\eta = 0.999001$.",
    "inputs": "κ=1\\;\\mathrm{ps^{-1}}, \\;γ_{rec}=10^{-3}\\;\\mathrm{ps^{-1}}",
    "formula": "η = κ/(κ+γ_{rec})"
  },
  {
    "id": "Q6",
    "statement": "Memory‑ratio for a fast bath $R_{\\mathrm{fast}} = τ_{B}/τ_{T}$ lies in $[0.26,\\,0.96]$ with $τ_{B}=0.1\\;\\mathrm{ps}$.",
    "inputs": "τ_{B}=0.1\\;\\mathrm{ps}, \\;τ_{T}^{min}=0.1039\\;\\mathrm{ps}, \\;τ_{T}^{max}=0.3823\\;\\mathrm{ps}",
    "formula": "R_{fast}=τ_{B}/τ_{T}; compute using τ_{T}^{max} for the lower bound and τ_{T}^{min} for the upper bound"
  },
  {
    "id": "Q7",
    "statement": "Memory‑ratio for a slow bath $R_{\\mathrm{slow}} = 1\\;\\mathrm{ps}/τ_{T}$ lies in $[2.6,\\,9.6]$.",
    "inputs": "τ_{B}=1\\;\\mathrm{ps}, \\;τ_{T}^{min}=0.1039\\;\\mathrm{ps}, \\;τ_{T}^{max}=0.3823\\;\\mathrm{ps}",
    "formula": "R_{slow}=τ_{B}/τ_{T}; compute using τ_{T}^{max} for the lower bound and τ_{T}^{min} for the upper bound"
  },
  {
    "id": "Q8",
    "statement": "Order‑of‑magnitude cost of a full non‑Markovian FMO simulation is approximately \\$1{,}000.",
    "inputs": "CPU\\_hours = 10^{4}, \\;price = 0.10\\;\\$\\,\\text{per CPU‑hour}",
    "formula": "Cost = CPU_hours \\times price"
  },
  {
    "id": "Q9",
    "statement": "Recombination rate $\\gamma_{\\mathrm{rec}} = 10^{-3}\\;\\mathrm{ps^{-1}}$.",
    "inputs": "τ_{e}=1\\;\\mathrm{ns}=10^{3}\\;\\mathrm{ps}",
    "formula": "γ_{rec}=1/τ_{e}"
  }
]

## Script
```python
import math

def fmt(val, sig=8):
    """Format a float with given significant digits."""
    if val == 0:
        return "0"
    # Determine number of digits before decimal
    int_digits = int(math.floor(math.log10(abs(val)))) + 1
    # Total digits = sig, so decimal places = sig - int_digits
    dec = max(sig - int_digits, 0)
    fmt_str = f"{{:.{dec}f}}"
    return fmt_str.format(val).rstrip('0').rstrip('.') if '.' in fmt_str.format(val) else fmt_str.format(val)

# Q1: Transfer‑time interval
c = 2.9979e10  # cm/s
V_min, V_max = 50.0, 75.0          # cm^{-1}
Delta_min, Delta_max = 110.0, 180.0  # cm^{-1}

def tau_T(Delta, V):
    return Delta / (2 * math.pi * c * V**2)  # seconds

tau_min_s = tau_T(Delta_min, V_max)   # smallest tau (largest V, smallest Δ)
tau_max_s = tau_T(Delta_max, V_min)   # largest tau (smallest V, largest Δ)

tau_min_ps = tau_min_s * 1e12
tau_max_ps = tau_max_s * 1e12

computed_Q1 = f"{fmt(tau_min_ps,6)}-{fmt(tau_max_ps,6)} ps"
expected_Q1 = "0.1039-0.3823 ps"
match_Q1 = "yes" if (abs(tau_min_ps-0.1039)<1e-4 and abs(tau_max_ps-0.3823)<1e-4) else "no"
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={match_Q1}")

# Q2: Optimal dephasing rate Γ* = Δ
Gamma_min = Delta_min
Gamma_max = Delta_max
computed_Q2 = f"{fmt(Gamma_min,4)}-{fmt(Gamma_max,4)} cm^{-1}"
expected_Q2 = "110-180 cm^{-1}"
match_Q2 = "yes" if Gamma_min==110 and Gamma_max==180 else "no"
print(f"CLAIM Q2: computed={computed_Q2} expected={expected_Q2} match={match_Q2}")

# Q3: Optimal hopping rate interval
def k_star(V, Delta):
    return V**2 / Delta

k_vals = [
    k_star(V_min, Delta_max),  # (50,180)
    k_star(V_min, Delta_min),  # (50,110)
    k_star(V_max, Delta_max),  # (75,180)
    k_star(V_max, Delta_min),  # (75,110)
]
k_min = min(k_vals)
k_max = max(k_vals)
computed_Q3 = f"{fmt(k_min,5)}-{fmt(k_max,5)} cm^{-1}"
expected_Q3 = "13.89-51.14 cm^{-1}"
match_Q3 = "yes" if (abs(k_min-13.89)<0.01 and abs(k_max-51.14)<0.01) else "no"
print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={match_Q3}")

# Q4: Corner values of k*
corner_labels = ["(50,180)", "(50,110)", "(75,180)", "(75,110)"]
computed_Q4_vals = [k_star(V, D) for V, D in [(50,180),(50,110),(75,180),(75,110)]]
computed_Q4 = ", ".join(fmt(v,6) for v in computed_Q4_vals) + " cm^{-1}"
expected_Q4 = "13.8889, 22.7273, 31.2500, 51.1364 cm^{-1}"
match_Q4 = "yes" if all(abs(c - e) < 1e-4 for c, e in zip(computed_Q4_vals, [13.8889,22.7273,31.2500,51.1364])) else "no"
print(f"CLAIM Q4: computed={computed_Q4} expected={expected_Q4} match={match_Q4}")

# Q5: Single‑hop trapping efficiency
kappa = 1.0      # ps^{-1}
gamma_rec = 1e-3 # ps^{-1}
eta = kappa / (kappa + gamma_rec)
computed_Q5 = fmt(eta,8)
expected_Q5 = "0.999001"
match_Q5 = "yes" if abs(eta-0.999001) < 1e-9 else "no"
print(f"CLAIM Q5: computed={computed_Q5} expected={expected_Q5} match={match_Q5}")

# Q6: Memory‑ratio fast bath
tau_B_fast = 0.1  # ps
R_fast_low = tau_B_fast / tau_max_ps   # using largest τ_T gives lower bound
R_fast_high = tau_B_fast / tau_min_ps  # using smallest τ_T gives upper bound
computed_Q6 = f"{fmt(R_fast_low,3)}-{fmt(R_fast_high,3)}"
expected_Q6 = "0.26-0.96"
match_Q6 = "yes" if (abs(R_fast_low-0.26)<0.01 and abs(R_fast_high-0.96)<0.01) else "no"
print(f"CLAIM Q6: computed={computed_Q6} expected={expected_Q6} match={match_Q6}")

# Q7: Memory‑ratio slow bath
tau_B_slow = 1.0  # ps
R_slow_low = tau_B_slow / tau_max_ps
R_slow_high = tau_B_slow / tau_min_ps
computed_Q7 = f"{fmt(R_slow_low,2)}-{fmt(R_slow_high,2)}"
expected_Q7 = "2.6-9.6"
match_Q7 = "yes" if (abs(R_slow_low-2.6)<0.1 and abs(R_slow_high-9.6)<0.1) else "no"
print(f"CLAIM Q7: computed={computed_Q7} expected={expected_Q7} match={match_Q7}")

# Q8: Cost projection
CPU_hours = 1e4
price_per_hour = 0.10
cost = CPU_hours * price_per_hour
computed_Q8 = fmt(cost,6)
expected_Q8 = "1000"
match_Q8 = "yes" if abs(cost-1000) < 1e-6 else "no"
print(f"CLAIM Q8: computed={computed_Q8} expected={expected_Q8} match={match_Q8}")

# Q9: Recombination rate
tau_e_ps = 1e3  # 1 ns = 1000 ps
gamma_rec_calc = 1.0 / tau_e_ps
computed_Q9 = fmt(gamma_rec_calc,6)
expected_Q9 = "0.001"
match_Q9 = "yes" if abs(gamma_rec_calc-0.001) < 1e-9 else "no"
print(f"CLAIM Q9: computed={computed_Q9} expected={expected_Q9} match={match_Q9}")

print(f"VERIFICATION SUMMARY: 9 claims, {sum(1 for m in [match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9] if m=='yes')} match, {sum(1 for m in [match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9] if m=='no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.103818-0.382239 ps expected=0.1039-0.3823 ps match=yes
CLAIM Q2: computed=110-180 cm^-1 expected=110-180 cm^{-1} match=yes
CLAIM Q3: computed=13.889-51.136 cm^-1 expected=13.89-51.14 cm^{-1} match=yes
CLAIM Q4: computed=13.8889, 22.7273, 31.25, 51.1364 cm^{-1} expected=13.8889, 22.7273, 31.2500, 51.1364 cm^{-1} match=yes
CLAIM Q5: computed=0.999001 expected=0.999001 match=yes
CLAIM Q6: computed=0.262-0.963 expected=0.26-0.96 match=yes
CLAIM Q7: computed=2.6-9.6 expected=2.6-9.6 match=yes
CLAIM Q8: computed=1000 expected=1000 match=yes
CLAIM Q9: computed=0.001 expected=0.001 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q5 | 0.999001 | 0.999001 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q6 | 0.262-0.963 | 0.26-0.96 | yes | match | script verdict (values not both numeric) |
| Q7 | 2.6-9.6 | 2.6-9.6 | yes | match | script verdict (values not both numeric) |
| Q8 | 1000 | 1000 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 0.001 | 0.001 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 5.
