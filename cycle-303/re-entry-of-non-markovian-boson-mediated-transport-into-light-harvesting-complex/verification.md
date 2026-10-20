# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Optimal dephasing rate \\(\\Gamma^{*}=\\Delta=100\\ \\mathrm{cm^{-1}}\\).",
    "inputs": "Δ = 100 cm^{-1}",
    "formula": "Γ* = Δ"
  },
  {
    "id": "Q2",
    "statement": "Optimal hopping rate \\(k^{*}=V^{2}/\\Delta=9\\ \\mathrm{cm^{-1}}\\).",
    "inputs": "V = 30 cm^{-1}, Δ = 100 cm^{-1}",
    "formula": "k* = V^2 / Δ"
  },
  {
    "id": "Q3",
    "statement": "Angular frequency \\(\\omega^{*}=2\\pi c k^{*}=1.6952\\times10^{12}\\ \\mathrm{rad\\,s^{-1}}\\).",
    "inputs": "c = 2.9979×10^{10} cm s^{-1}, k* = 9 cm^{-1}",
    "formula": "ω* = 2π c k*"
  },
  {
    "id": "Q4",
    "statement": "Transfer time \\(\\tau_{T}=1/\\omega^{*}=0.5899\\ \\mathrm{ps}\\).",
    "inputs": "ω* = 1.6952×10^{12} rad s^{-1}",
    "formula": "τ_T = 1 / ω*"
  },
  {
    "id": "Q5",
    "statement": "Transfer time via closed‑form \\(\\tau_{T}=\\Delta/(2\\pi c V^{2})=0.5899\\ \\mathrm{ps}\\).",
    "inputs": "Δ = 100 cm^{-1}, c = 2.9979×10^{10} cm s^{-1}, V = 30 cm^{-1}",
    "formula": "τ_T = Δ / (2π c V^2)"
  },
  {
    "id": "Q6",
    "statement": "Recombination rate \\(\\gamma_{\\mathrm{rec}}=1/\\tau_{e}=10^{-3}\\ \\mathrm{ps^{-1}}\\).",
    "inputs": "τ_e = 1 ns",
    "formula": "γ_rec = 1 / τ_e"
  },
  {
    "id": "Q7",
    "statement": "Single‑hop trapping efficiency \\(\\eta = \\kappa/(\\kappa+\\gamma_{\\mathrm{rec}})=0.999001\\).",
    "inputs": "κ = 1 ps^{-1}, γ_rec = 10^{-3} ps^{-1}",
    "formula": "η = κ / (κ + γ_rec)"
  },
  {
    "id": "Q8",
    "statement": "Fast memory ratio \\(R_{\\mathrm{fast}}=\\tau_{B}/\\tau_{T}=0.1/0.5899=0.1695\\).",
    "inputs": "τ_B = 0.1 ps, τ_T = 0.5899 ps",
    "formula": "R = τ_B / τ_T"
  },
  {
    "id": "Q9",
    "statement": "Slow memory ratio \\(R_{\\mathrm{slow}}=\\tau_{B}/\\tau_{T}=1/0.5899=1.6953\\).",
    "inputs": "τ_B = 1 ps, τ_T = 0.5899 ps",
    "formula": "R = τ_B / τ_T"
  },
  {
    "id": "Q10",
    "statement": "For \\(V=20\\ \\mathrm{cm^{-1}}, \\Delta=100\\ \\mathrm{cm^{-1}}\\): hopping rate \\(k^{*}=4.0\\ \\mathrm{cm^{-1}}\\).",
    "inputs": "V = 20 cm^{-1}, Δ = 100 cm^{-1}",
    "formula": "k* = V^2 / Δ"
  },
  {
    "id": "Q11",
    "statement": "For the same pair: angular frequency \\(\\omega^{*}=2\\pi c k^{*}=7.5345\\times10^{11}\\ \\mathrm{rad\\,s^{-1}}\\).",
    "inputs": "c = 2.9979×10^{10} cm s^{-1}, k* = 4.0 cm^{-1}",
    "formula": "ω* = 2π c k*"
  },
  {
    "id": "Q12",
    "statement": "Transfer time \\(\\tau_{T}=1/\\omega^{*}=1.3272\\ \\mathrm{ps}\\).",
    "inputs": "ω* = 7.5345×10^{11} rad s^{-1}",
    "formula": "τ_T = 1 / ω*"
  },
  {
    "id": "Q13",
    "statement": "Fast memory ratio for this case \\(R_{\\mathrm{fast}}=0.1/1.3272=0.0753\\).",
    "inputs": "τ_B = 0.1 ps, τ_T = 1.3272 ps",
    "formula": "R = τ_B / τ_T"
  },
  {
    "id": "Q14",
    "statement": "Slow memory ratio for this case \\(R_{\\mathrm{slow}}=1/1.3272=0.7535\\).",
    "inputs": "τ_B = 1 ps, τ_T = 1.3272 ps",
    "formula": "R = τ_B / τ_T"
  },
  {
    "id": "Q15",
    "statement": "For \\(V=50\\ \\mathrm{cm^{-1}}, \\Delta=150\\ \\mathrm{cm^{-1}}\\): hopping rate \\(k^{*}=16.6667\\ \\mathrm{cm^{-1}}\\).",
    "inputs": "V = 50 cm^{-1}, Δ = 150 cm^{-1}",
    "formula": "k* = V^2 / Δ"
  },
  {
    "id": "Q16",
    "statement": "Corresponding angular frequency \\(\\omega^{*}=3.1394\\times10^{12}\\ \\mathrm{rad\\,s^{-1}}\\).",
    "inputs": "c = 2.9979×10^{10} cm s^{-1}, k* = 16.6667 cm^{-1}",
    "formula": "ω* = 2π c k*"
  }
]

## Script
```python
import math

def fmt(val, exp):
    """Format val to match the precision of exp string."""
    if 'e' in exp:
        # scientific notation like 1.6952e12
        mant, exp_part = exp.split('e')
        digits = len(mant.split('.')[1]) if '.' in mant else 0
        fmt_str = f"{{:.{digits}e}}"
        return fmt_str.format(val)
    elif '.' in exp:
        # decimal notation
        digits = len(exp.split('.')[1])
        fmt_str = f"{{:.{digits}f}}"
        return fmt_str.format(val)
    else:
        # integer
        return str(int(round(val)))

# constants
c = 2.9979e10  # cm s^-1
Δ = 100.0      # cm^-1
V = 30.0       # cm^-1
k_star = V**2 / Δ
ω_star = 2 * math.pi * c * k_star
τ_T = 1e12 / ω_star  # ps

τ_e = 1e-9      # s
γ_rec = 1 / τ_e * 1e-12  # convert to ps^-1
κ = 1.0         # ps^-1
η = κ / (κ + γ_rec)

τ_B_fast = 0.1  # ps
τ_B_slow = 1.0  # ps
R_fast = τ_B_fast / τ_T
R_slow = τ_B_slow / τ_T

# additional cases
def case(Vc, Δc):
    k = Vc**2 / Δc
    ω = 2 * math.pi * c * k
    τ = 1e12 / ω
    return k, ω, τ

k20, ω20, τ20 = case(20.0, 100.0)
k50, ω50, τ50 = case(50.0, 150.0)

claims = [
    ("Q1", Δ, "100"),
    ("Q2", k_star, "9"),
    ("Q3", ω_star, "1.6952e12"),
    ("Q4", τ_T, "0.5899"),
    ("Q5", τ_T, "0.5899"),
    ("Q6", γ_rec, "0.001"),
    ("Q7", η, "0.999001"),
    ("Q8", R_fast, "0.1695"),
    ("Q9", R_slow, "1.6953"),
    ("Q10", k20, "4.0"),
    ("Q11", ω20, "7.5345e11"),
    ("Q12", τ20, "1.3272"),
    ("Q13", τ_B_fast/τ20, "0.0753"),
    ("Q14", τ_B_slow/τ20, "0.7535"),
    ("Q15", k50, "16.6667"),
    ("Q16", ω50, "3.1394e12"),
]

for cid, comp, exp in claims:
    comp_fmt = fmt(comp, exp)
    match = "yes" if comp_fmt == exp else "no"
    print(f"CLAIM {cid}: computed={comp_fmt} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if fmt(c,e)==e)} match, {sum(1 for _,c,e in claims if fmt(c,e)!=e)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=100 expected=100 match=yes
CLAIM Q2: computed=9 expected=9 match=yes
CLAIM Q3: computed=1.6953e+12 expected=1.6952e12 match=no
CLAIM Q4: computed=0.5899 expected=0.5899 match=yes
CLAIM Q5: computed=0.5899 expected=0.5899 match=yes
CLAIM Q6: computed=0.001 expected=0.001 match=yes
CLAIM Q7: computed=0.999001 expected=0.999001 match=yes
CLAIM Q8: computed=0.1695 expected=0.1695 match=yes
CLAIM Q9: computed=1.6953 expected=1.6953 match=yes
CLAIM Q10: computed=4.0 expected=4.0 match=yes
CLAIM Q11: computed=7.5345e+11 expected=7.5345e11 match=no
CLAIM Q12: computed=1.3272 expected=1.3272 match=yes
CLAIM Q13: computed=0.0753 expected=0.0753 match=yes
CLAIM Q14: computed=0.7535 expected=0.7535 match=yes
CLAIM Q15: computed=16.6667 expected=16.6667 match=yes
CLAIM Q16: computed=3.1394e+12 expected=3.1394e12 match=no
VERIFICATION SUMMARY: 16 claims, 13 match, 3 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 100 | 100 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 9 | 9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1.6953e+12 | 1.6952e12 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 0.5899 | 0.5899 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 0.5899 | 0.5899 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 0.001 | 0.001 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 0.999001 | 0.999001 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 0.1695 | 0.1695 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 1.6953 | 1.6953 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 4.0 | 4.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 7.5345e+11 | 7.5345e11 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 1.3272 | 1.3272 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q13 | 0.0753 | 0.0753 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 0.7535 | 0.7535 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q15 | 16.6667 | 16.6667 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q16 | 3.1394e+12 | 3.1394e12 | no | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
