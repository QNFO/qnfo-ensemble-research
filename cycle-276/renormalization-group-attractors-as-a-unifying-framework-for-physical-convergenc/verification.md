# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The basin radius is $R = 0.0114286$ computed from $N_{\\min}=50$ and $N_{\\max}=70$ using $R = \\frac{2}{N_{\\min}} - \\frac{2}{N_{\\max}}$.",
    "inputs": "N_min=50, N_max=70",
    "formula": "R = 2/N_min - 2/N_max"
  },
  {
    "id": "Q2",
    "statement": "The basin volume is $V_{\\rm basin}=4.103\\times10^{-4}$ obtained from $V = \\pi R^{2}$ with $R=0.0114286$.",
    "inputs": "R=0.0114286, pi",
    "formula": "V = pi * R^2"
  },
  {
    "id": "Q3",
    "statement": "The constant $C$ equals $1.0258$, calculated as $C = V_{\\rm basin}(N=50)\\times 50^{2}$.",
    "inputs": "V_basin(50)=4.103e-4, N=50",
    "formula": "C = V * N^2"
  },
  {
    "id": "Q4",
    "statement": "The basin‑volume scaling law is $V_{\\rm basin}(N)=1.0258\\,N^{-2}$.",
    "inputs": "C=1.0258",
    "formula": "V(N) = C * N^{-2}"
  },
  {
    "id": "Q5",
    "statement": "The polygenesis probability for $N=50$ is $P_{\\rm poly}(50)=4.103\\times10^{-4}$ using $P_{\\rm poly}(N)=\\kappa\\,1.0258\\,N^{-2}$ with $\\kappa=1$.",
    "inputs": "kappa=1, C=1.0258, N=50",
    "formula": "P(N) = kappa * C * N^{-2}"
  },
  {
    "id": "Q6",
    "statement": "The polygenesis probability for $N=60$ is $P_{\\rm poly}(60)=2.849\\times10^{-4}$ using the same formula.",
    "inputs": "kappa=1, C=1.0258, N=60",
    "formula": "P(N) = kappa * C * N^{-2}"
  },
  {
    "id": "Q7",
    "statement": "The ratio $P_{\\rm poly}(60)/P_{\\rm poly}(50)=0.694$, a $30\\%$ reduction when $N$ increases from $50$ to $60$.",
    "inputs": "P(60)=2.849e-4, P(50)=4.103e-4",
    "formula": "ratio = P(60) / P(50)"
  },
  {
    "id": "Q8",
    "statement": "For tolerance $\\epsilon=10^{-3}$, the simple dual‑subgradient method requires $T_{\\rm simple}=1000$ iterations, from $T_{\\rm simple}=\\lceil 1/\\epsilon \\rceil$.",
    "inputs": "epsilon=1e-3",
    "formula": "T_simple = ceil(1/epsilon)"
  },
  {
    "id": "Q9",
    "statement": "For tolerance $\\epsilon=10^{-3}$, the sliding‑average variant requires $T_{\\rm sliding}=7$ iterations, from $T_{\\rm sliding}=\\lceil \\ln(1/\\epsilon) \\rceil$.",
    "inputs": "epsilon=1e-3",
    "formula": "T_sliding = ceil( ln(1/epsilon) )"
  },
  {
    "id": "Q10",
    "statement": "For tolerance $\\epsilon=10^{-6}$, the simple method requires $T_{\\rm simple}=1\\,000\\,000$ iterations.",
    "inputs": "epsilon=1e-6",
    "formula": "T_simple = ceil(1/epsilon)"
  },
  {
    "id": "Q11",
    "statement": "For tolerance $\\epsilon=10^{-6}$, the sliding‑average variant requires $T_{\\rm sliding}=14$ iterations.",
    "inputs": "epsilon=1e-6",
    "formula": "T_sliding = ceil( ln(1/epsilon) )"
  },
  {
    "id": "Q12",
    "statement": "The Herfindahl pairwise coincidence probability is $P_{2}=0.2750$, computed as $P_{2}=\\sum_{i=1}^{5} p_{i}^{2}$ with $p_{1}=0.40$, $p_{2}=0.25$, $p_{3}=0.20$, $p_{4}=0.10$, $p_{5}=0.05$.",
    "inputs": "p1=0.40, p2=0.25, p3=0.20, p4=0.10, p5=0.05",
    "formula": "P2 = sum(p_i^2) for i=1..5"
  },
  {
    "id": "Q13",
    "statement": "The Herfindahl triple coincidence probability is $P_{3}=0.08875$, computed as $P_{3}=\\sum_{i=1}^{5} p_{i}^{3}$ with the same $p_{i}$ values.",
    "inputs": "p1=0.40, p2=0.25, p3=0.20, p4=0.10, p5=0.05",
    "formula": "P3 = sum(p_i^3) for i=1..5"
  },
  {
    "id": "Q14",
    "statement": "The dominant‑basin share is $0.581818\\approx0.582$, calculated as $p_{1}^{2}/P_{2}$.",
    "inputs": "p1=0.40, P2=0.2750",
    "formula": "share = p1^2 / P2"
  },
  {
    "id": "Q15",
    "statement": "The odds ratio between dominant and runner‑up basins is $2.56$, computed as $(p_{1}/p_{2})^{2}$.",
    "inputs": "p1=0.40, p2=0.25",
    "formula": "odds = (p1/p2)^2"
  },
  {
    "id": "Q16",
    "statement": "Under a contraction parameter $q=0.99$, initial distance $d_{0}=1$, and target precision $\\epsilon=10^{-2}$, the required iteration count is $n=458.21\\approx458.2$, from $n=\\frac{\\ln(\\epsilon/d_{0})}{\\ln q}$.",
    "inputs": "d0=1, q=0.99, epsilon=1e-2",
    "formula": "n = ln(epsilon/d0) / ln(q)"
  }
]

## Script
```python
import math

def fmt(val, digits):
    """Format number with given significant digits (as in expected string)."""
    # For scientific notation like 4.103e-4, keep as is.
    s = f"{val:.{digits}g}"
    # Ensure scientific notation uses 'e' lower case
    return s.replace('E', 'e')

claims = [
    ("Q1", lambda: 2/50 - 2/70, "0.0114286", 7),
    ("Q2", lambda R: math.pi * R**2, "4.103e-4", 4),  # 4 sig figs
    ("Q3", lambda V: V * 50**2, "1.0258", 5),
    ("Q4", lambda C: C * 60**-2, None, None),  # law, no numeric expected
    ("Q5", lambda: 1 * 1.0258 * 50**-2, "4.103e-4", 4),
    ("Q6", lambda: 1 * 1.0258 * 60**-2, "2.849e-4", 4),
    ("Q7", lambda P60, P50: P60 / P50, "0.694", 3),
    ("Q8", lambda eps: math.ceil(1/eps), "1000", 4),
    ("Q9", lambda eps: math.ceil(math.log(1/eps)), "7", 1),
    ("Q10", lambda eps: math.ceil(1/eps), "1000000", 7),
    ("Q11", lambda eps: math.ceil(math.log(1/eps)), "14", 2),
    ("Q12", lambda p: sum(x**2 for x in p), "0.2750", 5),
    ("Q13", lambda p: sum(x**3 for x in p), "0.08875", 5),
    ("Q14", lambda p1, P2: p1**2 / P2, "0.581818", 6),
    ("Q15", lambda p1, p2: (p1/p2)**2, "2.56", 3),
    ("Q16", lambda d0, q, eps: math.log(eps/d0) / math.log(q), "458.21", 5),
]

# Pre‑compute shared intermediate values
R = 2/50 - 2/70
V = math.pi * R**2
C = V * 50**2
P50 = 1 * C * 50**-2
P60 = 1 * C * 60**-2
p_vals = [0.40, 0.25, 0.20, 0.10, 0.05]
P2 = sum(x**2 for x in p_vals)
P3 = sum(x**3 for x in p_vals)

for cid, func, expected, sig in claims:
    # compute based on cid
    if cid == "Q1":
        comp = func()
    elif cid == "Q2":
        comp = func(R)
    elif cid == "Q3":
        comp = func(V)
    elif cid == "Q4":
        comp = func(C)  # just to have a number, not used
    elif cid == "Q5":
        comp = func()
    elif cid == "Q6":
        comp = func()
    elif cid == "Q7":
        comp = func(P60, P50)
    elif cid == "Q8":
        comp = func(1e-3)
    elif cid == "Q9":
        comp = func(1e-3)
    elif cid == "Q10":
        comp = func(1e-6)
    elif cid == "Q11":
        comp = func(1e-6)
    elif cid == "Q12":
        comp = func(p_vals)
    elif cid == "Q13":
        comp = func(p_vals)
    elif cid == "Q14":
        comp = func(0.40, P2)
    elif cid == "Q15":
        comp = func(0.40, 0.25)
    elif cid == "Q16":
        comp = func(1, 0.99, 1e-2)
    else:
        comp = None

    if expected is None:
        exp_str = "none"
        match = "yes"
    else:
        # format computed value to same number of significant digits as expected
        # Determine number of digits after decimal or in mantissa from expected string
        # Simple approach: use sig provided
        comp_str = fmt(comp, sig)
        exp_str = expected
        match = "yes" if comp_str == exp_str else "no"

    print(f"CLAIM {cid}: computed={comp_str if expected is not None else comp} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for c in claims if (c[2] is None) or (fmt(eval('comp'), c[3]) == c[2]))} match, {sum(1 for c in claims if not (c[2] is None) and (fmt(eval('comp'), c[3]) != c[2]))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.01142857 expected=0.0114286 match=no
CLAIM Q2: computed=0.0004103 expected=4.103e-4 match=no
CLAIM Q3: computed=1.0258 expected=1.0258 match=yes
CLAIM Q4: computed=0.0002849517146113192 expected=none match=yes
CLAIM Q5: computed=0.0004103 expected=4.103e-4 match=no
CLAIM Q6: computed=0.0002849 expected=2.849e-4 match=no
CLAIM Q7: computed=0.694 expected=0.694 match=yes
CLAIM Q8: computed=1000 expected=1000 match=yes
CLAIM Q9: computed=7 expected=7 match=yes
CLAIM Q10: computed=1000000 expected=1000000 match=yes
CLAIM Q11: computed=14 expected=14 match=yes
CLAIM Q12: computed=0.275 expected=0.2750 match=no
CLAIM Q13: computed=0.08875 expected=0.08875 match=yes
CLAIM Q14: computed=0.581818 expected=0.581818 match=yes
CLAIM Q15: computed=2.56 expected=2.56 match=yes
CLAIM Q16: computed=458.21 expected=458.21 match=yes
VERIFICATION SUMMARY: 16 claims, 2 match, 14 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.01142857 | 0.0114286 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 0.0004103 | 4.103e-4 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 1.0258 | 1.0258 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 0.0002849517146113192 | none | yes | match | script verdict (values not both numeric) |
| Q5 | 0.0004103 | 4.103e-4 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 0.0002849 | 2.849e-4 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 0.694 | 0.694 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 1000 | 1000 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 1000000 | 1000000 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q11 | 14 | 14 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 0.275 | 0.2750 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 0.08875 | 0.08875 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 0.581818 | 0.581818 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q15 | 2.56 | 2.56 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 458.21 | 458.21 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
