# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Register entropy for a $d$‑level qudit with $d=12$ is $H_{\\mathrm{reg}}=\\log_{2}12=3.584963$ bits.",
    "inputs": "d = 12",
    "formula": "H_reg = log2(d)"
  },
  {
    "id": "Q2",
    "statement": "Base truncation entropy for $d=12$ is $S_{\\mathrm{Base}}=\\ln(12/2)=1.791759$ nats, which equals $2.584963$ bits after conversion.",
    "inputs": "d = 12, conversion factor log2(e) = 1.442695",
    "formula": "S_Base_nats = ln(d/2); S_Base_bits = S_Base_nats * log2(e)"
  },
  {
    "id": "Q3",
    "statement": "The number of binary qubits required to encode a $d=12$ level system is $m=\\lceil\\log_{2}12\\rceil=4$.",
    "inputs": "d = 12",
    "formula": "m = ceil(log2(d))"
  },
  {
    "id": "Q4",
    "statement": "The dimension‑overhead ratio for $d=12$ and $m=4$ is $2^{4}/12 = 16/12 = 4/3 = 1.333333$.",
    "inputs": "m = 4, d = 12",
    "formula": "ratio = 2^m / d"
  },
  {
    "id": "Q5",
    "statement": "Encoding efficiency for $d=12$ is $\\eta = \\log_{2}12 / 4 = 0.896241$.",
    "inputs": "d = 12, m = 4",
    "formula": "eta = log2(d) / m"
  },
  {
    "id": "Q6",
    "statement": "The idle fraction of the binary encoding is $1-\\eta = 0.103759$ (≈10.4 %).",
    "inputs": "eta = 0.896241",
    "formula": "idle = 1 - eta"
  },
  {
    "id": "Q7",
    "statement": "For a damping probability $\\gamma=10^{-3}$ the Pauli‑twirled error probabilities are $p_{X}=p_{Y}=\\gamma/4=2.5\\times10^{-4}$, $p_{Z}=\\gamma/2=5\\times10^{-4}$, $p_{I}=1-\\gamma=0.999$.",
    "inputs": "gamma = 1e-3",
    "formula": "p_X = gamma/4; p_Z = gamma/2; p_I = 1 - gamma"
  },
  {
    "id": "Q8",
    "statement": "The environment entropy of the physical amplitude‑damping channel with $\\gamma=10^{-3}$ is $H_{\\mathrm{env}}^{\\mathrm{phys}} = -\\gamma\\log_{2}\\gamma-(1-\\gamma)\\log_{2}(1-\\gamma)=0.011408$ bits.",
    "inputs": "gamma = 1e-3",
    "formula": "H_env_phys = -gamma*log2(gamma) - (1-gamma)*log2(1-gamma)"
  },
  {
    "id": "Q9",
    "statement": "The environment entropy of the Pauli‑twirled surrogate for $\\gamma=10^{-3}$ is $H_{\\mathrm{env}}^{\\mathrm{twirl}} = -\\sum_{i}p_{i}\\log_{2}p_{i}=0.012908$ bits.",
    "inputs": "p_I = 0.999, p_X = p_Y = 2.5e-4, p_Z = 5e-4",
    "formula": "H_env_twirl = - (p_I*log2(p_I) + 2*p_X*log2(p_X) + p_Z*log2(p_Z))"
  },
  {
    "id": "Q10",
    "statement": "The entropy distortion caused by Pauli twirling is $\\Delta H = H_{\\mathrm{env}}^{\\mathrm{twirl}}-H_{\\mathrm{env}}^{\\mathrm{phys}} = 1.5\\times10^{-3}$ bits.",
    "inputs": "H_env_twirl = 0.012908, H_env_phys = 0.011408",
    "formula": "Delta_H = H_env_twirl - H_env_phys"
  },
  {
    "id": "Q11",
    "statement": "The ratio of twirled to physical environment entropy is $H_{\\mathrm{env}}^{\\mathrm{twirl}}/H_{\\mathrm{env}}^{\\mathrm{phys}} = 1.131489$.",
    "inputs": "H_env_twirl = 0.012908, H_env_phys = 0.011408",
    "formula": "ratio = H_env_twirl / H_env_phys"
  },
  {
    "id": "Q12",
    "statement": "For any damping probability $\\gamma$, the exact distortion law is $\\Delta H = 3\\gamma/2$ bits.",
    "inputs": "gamma (symbolic)",
    "formula": "Delta_H = 3*gamma/2"
  },
  {
    "id": "Q13",
    "statement": "The discarded Hilbert‑space weight for a thermal mode with $\\bar n=0.1$ and $d=12$ is $p_{\\mathrm{disc}} = (0.1/1.1)^{12}=3.186308\\times10^{-13}$.",
    "inputs": "nbar = 0.1, d = 12",
    "formula": "p_disc = (nbar/(1+nbar))^d"
  },
  {
    "id": "Q14",
    "statement": "For $M=10^{4}$ modes and $N_{\\mathrm{cycles}}=10^{10}$ cycles the total register bookkeeping is $N_{\\mathrm{cycles}}\\times M \\times H_{\\mathrm{reg}} = 3.584963\\times10^{14}$ bits.",
    "inputs": "M = 1e4, N_cycles = 1e10, H_reg = 3.584963",
    "formula": "total_bits = N_cycles * M * H_reg"
  },
  {
    "id": "Q15",
    "statement": "For $M=10^{5}$ modes and $N_{\\mathrm{cycles}}=10^{11}$ cycles the projected bookkeeping is $3.584963\\times10^{16}$ bits.",
    "inputs": "M = 1e5, N_cycles = 1e11, H_reg = 3.584963",
    "formula": "total_bits = N_cycles * M * H_reg"
  },
  {
    "id": "Q16",
    "statement": "Assuming an energy cost of $1\\,$nJ per bit, the energy budget for $3.584963\\times10^{16}$ bits is $3.584963\\times10^{7}$ J.",
    "inputs": "bits = 3.584963e16, energy_per_bit = 1e-9 J",
    "formula": "energy = bits * energy_per_bit"
  }
]

## Script
```python
import math

def close(a, b, rel=1e-12, abs_tol=1e-15):
    return abs(a - b) <= max(rel * max(abs(a), abs(b)), abs_tol)

claims = [
    ("Q1", lambda: math.log2(12), 3.584963),
    ("Q2", lambda: math.log(12/2) * 1.442695, 2.584963),
    ("Q3", lambda: math.ceil(math.log2(12)), 4),
    ("Q4", lambda: 2**4 / 12, 1.333333),
    ("Q5", lambda: math.log2(12) / 4, 0.896241),
    ("Q6", lambda: 1 - (math.log2(12) / 4), 0.103759),
    ("Q7_X", lambda: 1e-3 / 4, 2.5e-4),
    ("Q7_Z", lambda: 1e-3 / 2, 5e-4),
    ("Q7_I", lambda: 1 - 1e-3, 0.999),
    ("Q8", lambda: -1e-3*math.log2(1e-3) - (1-1e-3)*math.log2(1-1e-3), 0.011408),
    ("Q9", lambda: -(0.999*math.log2(0.999) + 2*2.5e-4*math.log2(2.5e-4) + 5e-4*math.log2(5e-4)), 0.012908),
    ("Q10", lambda: (-(0.999*math.log2(0.999) + 2*2.5e-4*math.log2(2.5e-4) + 5e-4*math.log2(5e-4))) - (-1e-3*math.log2(1e-3) - (1-1e-3)*math.log2(1-1e-3)), 1.5e-3),
    ("Q11", lambda: (-(0.999*math.log2(0.999) + 2*2.5e-4*math.log2(2.5e-4) + 5e-4*math.log2(5e-4))) / (-1e-3*math.log2(1e-3) - (1-1e-3)*math.log2(1-1e-3)), 1.131489),
    ("Q12", lambda: 3*1e-3/2, None),  # law, no numeric expected
    ("Q13", lambda: (0.1/1.1)**12, 3.186308e-13),
    ("Q14", lambda: 1e10 * 1e4 * 3.584963, 3.584963e14),
    ("Q15", lambda: 1e11 * 1e5 * 3.584963, 3.584963e16),
    ("Q16", lambda: 3.584963e16 * 1e-9, 3.584963e7),
]

for cid, func, expected in claims:
    computed = func()
    if expected is None:
        match = "yes"
        exp_str = ""
    else:
        match = "yes" if close(computed, expected) else "no"
        # format expected to match the paper's representation
        if isinstance(expected, float):
            # decide format based on magnitude
            if abs(expected) < 1e-2 or abs(expected) >= 1e5:
                exp_str = f"{expected:.6e}"
            else:
                exp_str = f"{expected:.6f}"
        else:
            exp_str = str(expected)
    print(f"CLAIM {cid}: computed={computed:.12g} expected={exp_str} match={match}")

```

## Execution output
```
CLAIM Q1: computed=3.58496250072 expected=3.584963 match=no
CLAIM Q2: computed=2.58496242746 expected=2.584963 match=no
CLAIM Q3: computed=4 expected=4 match=yes
CLAIM Q4: computed=1.33333333333 expected=1.333333 match=no
CLAIM Q5: computed=0.89624062518 expected=0.896241 match=no
CLAIM Q6: computed=0.10375937482 expected=0.103759 match=no
CLAIM Q7_X: computed=0.00025 expected=2.500000e-04 match=yes
CLAIM Q7_Z: computed=0.0005 expected=5.000000e-04 match=yes
CLAIM Q7_I: computed=0.999 expected=0.999000 match=yes
CLAIM Q8: computed=0.0114077577375 expected=0.011408 match=no
CLAIM Q9: computed=0.0129077577375 expected=0.012908 match=no
CLAIM Q10: computed=0.0015 expected=1.500000e-03 match=yes
CLAIM Q11: computed=1.13148946835 expected=1.131489 match=no
CLAIM Q12: computed=0.0015 expected= match=yes
CLAIM Q13: computed=3.1863081771e-13 expected=3.186308e-13 match=yes
CLAIM Q14: computed=3.584963e+14 expected=3.584963e+14 match=yes
CLAIM Q15: computed=3.584963e+16 expected=3.584963e+16 match=yes
CLAIM Q16: computed=35849630 expected=3.584963e+07 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3.58496250072 | 3.584963 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q2 | 2.58496242746 | 2.584963 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 1.33333333333 | 1.333333 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q5 | 0.89624062518 | 0.896241 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q6 | 0.10375937482 | 0.103759 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q7_X | 0.00025 | 2.500000e-04 | yes | match | 7 significant digits (as printed, at least 3) |
| Q7_Z | 0.0005 | 5.000000e-04 | yes | match | 7 significant digits (as printed, at least 3) |
| Q7_I | 0.999 | 0.999000 | yes | match | 6 significant digits (as printed, at least 3) |
| Q8 | 0.0114077577375 | 0.011408 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 0.0129077577375 | 0.012908 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 0.0015 | 1.500000e-03 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 1.13148946835 | 1.131489 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q12 | 0.0015 | match=yes | - | undecided | undecided: values not both numeric and no script verdict |
| Q13 | 3.1863081771e-13 | 3.186308e-13 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q14 | 3.584963e+14 | 3.584963e+14 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q15 | 3.584963e+16 | 3.584963e+16 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q16 | 35849630 | 3.584963e+07 | yes | match | 7 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 18 (1 undecided).
