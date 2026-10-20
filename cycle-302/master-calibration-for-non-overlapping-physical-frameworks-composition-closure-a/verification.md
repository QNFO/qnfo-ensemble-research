# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The number of unordered pairwise translation maps is \\(\\binom{29}{2}=406\\).",
    "inputs": "N = 29",
    "formula": "C(N,2) = N*(N-1)/2"
  },
  {
    "id": "Q2",
    "statement": "The number of independent composition constraints is \\(\\binom{29}{3}=3654\\).",
    "inputs": "N = 29",
    "formula": "C(N,3) = N*(N-1)*(N-2)/6"
  },
  {
    "id": "Q3",
    "statement": "The constraint‑to‑map ratio is \\(\\frac{3654}{406}=9.0\\).",
    "inputs": "constraints = 3654, maps = 406",
    "formula": "ratio = constraints / maps"
  },
  {
    "id": "Q4",
    "statement": "If each bifurcation is counted as two opposite‑direction frameworks (N=58), the ratio of constraints to maps is \\(\\frac{30856}{1653}\\approx18.667\\).",
    "inputs": "N = 58",
    "formula": "maps = C(N,2); constraints = C(N,3); ratio = constraints / maps"
  },
  {
    "id": "Q5",
    "statement": "For a family of n=7 domains, the number of unordered pairs is \\(\\binom{7}{2}=21\\).",
    "inputs": "n = 7",
    "formula": "C(n,2) = n*(n-1)/2"
  },
  {
    "id": "Q6",
    "statement": "The number of directed pairs for n=7 is \\(7\\times6=42\\).",
    "inputs": "n = 7",
    "formula": "directed pairs = n*(n-1)"
  },
  {
    "id": "Q7",
    "statement": "At least \\(29-21=8\\) bifurcations cannot be assigned a distinct unordered pair under the one‑schism‑per‑pair assumption.",
    "inputs": "total bifurcations = 29, unordered pairs = 21",
    "formula": "unassigned = total - unordered pairs"
  },
  {
    "id": "Q8",
    "statement": "For m=2 ontologies, the unordered‑pair count is \\(\\binom{2}{2}=1\\) and the unordered‑triple count is \\(\\binom{2}{3}=0\\).",
    "inputs": "m = 2",
    "formula": "C(m,2) = m*(m-1)/2; C(m,3) = m*(m-1)*(m-2)/6"
  },
  {
    "id": "Q9",
    "statement": "The closure bound for a three‑framework loop with edge errors \\(\\varepsilon_{12}=10^{-3}, \\varepsilon_{23}=2\\times10^{-3}, \\varepsilon_{31}=5\\times10^{-4}\\) is \\(\\Delta_{\\gamma}\\le3.4965\\times10^{-3}\\).",
    "inputs": "ε12 = 1e-3, ε23 = 2e-3, ε31 = 5e-4",
    "formula": "Δ = 1 - (1-ε12)*(1-ε23)*(1-ε31)"
  },
  {
    "id": "Q10",
    "statement": "The additive first‑order bound for the same three edges is \\(\\varepsilon_{12}+\\varepsilon_{23}+\\varepsilon_{31}=3.5\\times10^{-3}\\).",
    "inputs": "ε12 = 1e-3, ε23 = 2e-3, ε31 = 5e-4",
    "formula": "sum = ε12 + ε23 + ε31"
  },
  {
    "id": "Q11",
    "statement": "A translation chain of k=4 edges each with floor \\(\\varepsilon_{\\min}=10^{-2}\\) yields \\(\\Delta\\le1-(0.99)^{4}=3.94\\times10^{-2}\\).",
    "inputs": "k = 4, ε_min = 1e-2",
    "formula": "Δ = 1 - (1-ε_min)^k"
  },
  {
    "id": "Q12",
    "statement": "For tolerance \\(\\tau=10^{-2}\\) and \\(\\varepsilon_{\\min}=10^{-2}\\), the inequality \\(k\\le\\frac{\\ln(1-\\tau)}{\\ln(1-\\varepsilon_{\\min})}=1\\) holds.",
    "inputs": "τ = 1e-2, ε_min = 1e-2",
    "formula": "k ≤ ln(1-τ) / ln(1-ε_min)"
  },
  {
    "id": "Q13",
    "statement": "The collider energy window factor using the abstract range is \\(\\frac{1\\ \\mathrm{TeV}}{500\\ \\mathrm{GeV}}=2\\).",
    "inputs": "E_max = 1 TeV, E_min = 500 GeV",
    "formula": "factor = E_max / E_min"
  },
  {
    "id": "Q14",
    "statement": "Using the preface range, the energy window factor is \\(\\frac{1.5\\ \\mathrm{TeV}}{0.5\\ \\mathrm{TeV}}=3\\).",
    "inputs": "E_max = 1.5 TeV, E_min = 0.5 TeV",
    "formula": "factor = E_max / E_min"
  },
  {
    "id": "Q15",
    "statement": "Assuming a uniform distribution of the 29 schisms over 7 domains, the mean per‑domain count is \\(\\frac{29}{7}=4.142857\\approx4.14\\).",
    "inputs": "total schisms = 29, domains = 7",
    "formula": "mean = total / domains"
  },
  {
    "id": "Q16",
    "statement": "Replacing a direct translation edge with error \\(\\varepsilon=10^{-2}\\) by a mediated two‑edge chain yields \\(\\varepsilon_{\\text{mediated}}=1-(0.99)^{2}=0.0199\\).",
    "inputs": "ε = 1e-2",
    "formula": "ε_mediated = 1 - (1-ε)^2"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def compare(computed, expected_str):
    # parse expected to float
    expected = float(expected_str.replace('e', 'E'))
    # determine number of significant digits in expected
    # remove sign, decimal point, exponent part
    s = expected_str.lower()
    if 'e' in s:
        mantissa = s.split('e')[0].replace('.', '').lstrip('0')
    else:
        mantissa = s.replace('.', '').lstrip('0')
    sig = len(mantissa) if mantissa else 1
    comp_rounded = round_sig(computed, sig)
    exp_rounded = round_sig(expected, sig)
    match = 'yes' if comp_rounded == exp_rounded else 'no'
    return f"{comp_rounded:.{sig}g}", f"{expected_str}", match

# Q1
N = 29
C1 = N * (N - 1) / 2
c, e, m = compare(C1, "406")
print(f"CLAIM Q1: computed={c} expected={e} match={m}")

# Q2
C2 = N * (N - 1) * (N - 2) / 6
c, e, m = compare(C2, "3654")
print(f"CLAIM Q2: computed={c} expected={e} match={m}")

# Q3
ratio = 3654 / 406
c, e, m = compare(ratio, "9.0")
print(f"CLAIM Q3: computed={c} expected={e} match={m}")

# Q4
N2 = 58
maps = N2 * (N2 - 1) / 2
constraints = N2 * (N2 - 1) * (N2 - 2) / 6
ratio2 = constraints / maps
c, e, m = compare(ratio2, "18.667")
print(f"CLAIM Q4: computed={c} expected={e} match={m}")

# Q5
n = 7
pairs = n * (n - 1) / 2
c, e, m = compare(pairs, "21")
print(f"CLAIM Q5: computed={c} expected={e} match={m}")

# Q6
directed = n * (n - 1)
c, e, m = compare(directed, "42")
print(f"CLAIM Q6: computed={c} expected={e} match={m}")

# Q7
unassigned = 29 - 21
c, e, m = compare(unassigned, "8")
print(f"CLAIM Q7: computed={c} expected={e} match={m}")

# Q8
m_val = 2
unordered_pair = m_val * (m_val - 1) / 2
unordered_triple = m_val * (m_val - 1) * (m_val - 2) / 6
# combine as "1,0"
c_pair = round_sig(unordered_pair, 1)
c_triple = round_sig(unordered_triple, 1)
c = f"{c_pair:.0f},{c_triple:.0f}"
e = "1,0"
match = "yes" if c == e else "no"
print(f"CLAIM Q8: computed={c} expected={e} match={match}")

# Q9
e12 = 1e-3
e23 = 2e-3
e31 = 5e-4
delta = 1 - (1 - e12) * (1 - e23) * (1 - e31)
c, e, m = compare(delta, "3.4965e-3")
print(f"CLAIM Q9: computed={c} expected={e} match={m}")

# Q10
additive = e12 + e23 + e31
c, e, m = compare(additive, "3.5e-3")
print(f"CLAIM Q10: computed={c} expected={e} match={m}")

# Q11
k = 4
eps_min = 1e-2
delta2 = 1 - (1 - eps_min) ** k
c, e, m = compare(delta2, "3.94e-2")
print(f"CLAIM Q11: computed={c} expected={e} match={m}")

# Q12
tau = 1e-2
k_bound = math.log(1 - tau) / math.log(1 - eps_min)
c, e, m = compare(k_bound, "1")
print(f"CLAIM Q12: computed={c} expected={e} match={m}")

# Q13
E_max = 1e3  # MeV equivalent to 1 TeV
E_min = 500   # MeV equivalent to 500 GeV
factor13 = E_max / E_min
c, e, m = compare(factor13, "2")
print(f"CLAIM Q13: computed={c} expected={e} match={m}")

# Q14
E_max2 = 1.5e3
E_min2 = 0.5e3
factor14 = E_max2 / E_min2
c, e, m = compare(factor14, "3")
print(f"CLAIM Q14: computed={c} expected={e} match={m}")

# Q15
total_schisms = 29
domains = 7
mean = total_schisms / domains
c, e, m = compare(mean, "4.14")
print(f"CLAIM Q15: computed={c} expected={e} match={m}")

# Q16
eps = 1e-2
mediated = 1 - (1 - eps) ** 2
c, e, m = compare(mediated, "0.0199")
print(f"CLAIM Q16: computed={c} expected={e} match={m}")

print(f"VERIFICATION SUMMARY: {16} claims, {sum(1 for line in [c, e, m] if m=='yes')} match, {sum(1 for line in [c, e, m] if m=='no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=406 expected=406 match=yes
CLAIM Q2: computed=3654 expected=3654 match=yes
CLAIM Q3: computed=9 expected=9.0 match=yes
CLAIM Q4: computed=18.667 expected=18.667 match=yes
CLAIM Q5: computed=21 expected=21 match=yes
CLAIM Q6: computed=42 expected=42 match=yes
CLAIM Q7: computed=8 expected=8 match=yes
CLAIM Q8: computed=1,0 expected=1,0 match=yes
CLAIM Q9: computed=0.0034965 expected=3.4965e-3 match=yes
CLAIM Q10: computed=0.0035 expected=3.5e-3 match=yes
CLAIM Q11: computed=0.0394 expected=3.94e-2 match=yes
CLAIM Q12: computed=1 expected=1 match=yes
CLAIM Q13: computed=2 expected=2 match=yes
CLAIM Q14: computed=3 expected=3 match=yes
CLAIM Q15: computed=4.14 expected=4.14 match=yes
CLAIM Q16: computed=0.0199 expected=0.0199 match=yes
VERIFICATION SUMMARY: 16 claims, 3 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 406 | 406 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 3654 | 3654 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 9 | 9.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 18.667 | 18.667 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 21 | 21 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 42 | 42 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 1,0 | 1,0 | yes | match | script verdict (values not both numeric) |
| Q9 | 0.0034965 | 3.4965e-3 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 0.0035 | 3.5e-3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.0394 | 3.94e-2 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 2 | 2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 4.14 | 4.14 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 0.0199 | 0.0199 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
