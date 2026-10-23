# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Register entropy for a digitized qudit of dimension 12 is $H_{\\mathrm{reg}}=\\log_2 12 = 3.584963$ bits.",
    "inputs": "d = 12",
    "formula": "H_{\\mathrm{reg}} = \\log_2(d)"
  },
  {
    "id": "Q2",
    "statement": "Base truncation entropy for $d=12$ is $S_{\\mathrm{Base}} = \\ln(12/2) = \\ln 6 = 1.791759$ nats.",
    "inputs": "d = 12",
    "formula": "S_{\\mathrm{Base}} = \\ln(d/2)"
  },
  {
    "id": "Q3",
    "statement": "Converted base truncation entropy to bits: $1.791759 \\times \\log_2 e = 2.584963$ bits.",
    "inputs": "S_{\\mathrm{Base}} = 1.791759 \\text{ nats}, \\log_2 e = 1.442695",
    "formula": "bits = S_{\\mathrm{Base}} \\times \\log_2 e"
  },
  {
    "id": "Q4",
    "statement": "Number of qubits required to encode a $d=12$ qudit is $m = \\lceil\\log_2 12\\rceil = 4$.",
    "inputs": "d = 12",
    "formula": "m = \\lceil\\log_2(d)\\rceil"
  },
  {
    "id": "Q5",
    "statement": "Encoded Hilbert dimension is $2^{m}=16$.",
    "inputs": "m = 4",
    "formula": "2^{m}"
  },
  {
    "id": "Q6",
    "statement": "Wasted levels after binary encoding are $2^{m} - d = 4$.",
    "inputs": "2^{m}=16, d=12",
    "formula": "2^{m} - d"
  },
  {
    "id": "Q7",
    "statement": "Dimension‑overhead ratio is $\\frac{2^{m}}{d}=\\frac{16}{12}=\\frac{4}{3}\\approx1.333333$.",
    "inputs": "2^{m}=16, d=12",
    "formula": "(2^{m})/d"
  },
  {
    "id": "Q8",
    "statement": "Encoding efficiency is $\\eta = \\frac{\\log_2 d}{m}=\\frac{3.584963}{4}=0.896241$.",
    "inputs": "d=12, m=4",
    "formula": "\\eta = \\log_2(d) / m"
  },
  {
    "id": "Q9",
    "statement": "Idle fraction of the binary encoding is $1-\\eta = 0.103759 \\approx 10.4\\%$.",
    "inputs": "\\eta = 0.896241",
    "formula": "1 - \\eta"
  },
  {
    "id": "Q10",
    "statement": "Pauli‑twirled error probabilities for amplitude damping with $\\gamma=10^{-3}$ are $p_X=p_Y=\\gamma/4=2.5\\times10^{-4}$, $p_Z=\\gamma/2=5\\times10^{-4}$, $p_I=1-\\gamma=0.999$.",
    "inputs": "\\gamma = 10^{-3}",
    "formula": "p_X=p_Y=\\gamma/4,\\; p_Z=\\gamma/2,\\; p_I=1-\\gamma"
  },
  {
    "id": "Q11",
    "statement": "Physical environment entropy for $\\gamma=10^{-3}$ is $H_{\\mathrm{env}}^{\\mathrm{phys}} = h_2(\\gamma)=1.140776\\times10^{-2}$ bits.",
    "inputs": "\\gamma = 10^{-3}",
    "formula": "H_{\\mathrm{env}}^{\\mathrm{phys}} = -\\gamma\\log_2\\gamma - (1-\\gamma)\\log_2(1-\\gamma)"
  },
  {
    "id": "Q12",
    "statement": "Twirled environment entropy for $\\gamma=10^{-3}$ is $H_{\\mathrm{env}}^{\\mathrm{twirl}} = 1.290776\\times10^{-2}$ bits.",
    "inputs": "p_I=0.999, p_X=p_Y=2.5\\times10^{-4}, p_Z=5\\times10^{-4}",
    "formula": "H_{\\mathrm{env}}^{\\mathrm{twirl}} = -\\sum_i p_i \\log_2 p_i"
  },
  {
    "id": "Q13",
    "statement": "Entropy distortion for $\\gamma=10^{-3}$ is $\\Delta H = 1.500000\\times10^{-3}$ bits, and the ratio $H_{\\mathrm{twirl}}/H_{\\mathrm{phys}} = 1.131489$.",
    "inputs": "H_{\\mathrm{env}}^{\\mathrm{phys}}=1.140776\\times10^{-2}, H_{\\mathrm{env}}^{\\mathrm{twirl}}=1.290776\\times10^{-2}",
    "formula": "\\Delta H = H_{\\mathrm{twirl}} - H_{\\mathrm{phys}};\\; \\text{ratio}= H_{\\mathrm{twirl}}/H_{\\mathrm{phys}}"
  },
  {
    "id": "Q14",
    "statement": "Exact distortion law is $\\Delta H = \\frac{3\\gamma}{2}$ bits.",
    "inputs": "\\gamma",
    "formula": "\\Delta H = 3\\gamma/2"
  },
  {
    "id": "Q15",
    "statement": "Discarded Hilbert‑space weight for $\\bar n=0.1$, $d=12$ is $p_{\\mathrm{disc}} \\approx 3.186308\\times10^{-13}$.",
    "inputs": "\\bar n = 0.1, d = 12",
    "formula": "p_{\\mathrm{disc}} = \\left(\\frac{\\bar n}{1+\\bar n}\\right)^{d}"
  },
  {
    "id": "Q16",
    "statement": "Cumulative register bookkeeping for $M=10^{4}$ modes and $N_{\\mathrm{cycles}}=10^{10}$ cycles is $3.584963\\times10^{14}$ bits.",
    "inputs": "M = 10^{4}, N_{\\mathrm{cycles}} = 10^{10}, H_{\\mathrm{reg}} = 3.584963",
    "formula": "N_{\\mathrm{cycles}} \\times M \\times H_{\\mathrm{reg}}"
  }
]

## Script
```python
import math

# Q1
H_reg = math.log2(12)
print(f"CLAIM Q1: computed={H_reg:.9g} expected=3.584963 match={'yes' if round(H_reg,6)==3.584963 else 'no'}")

# Q2
S_base = math.log(12/2)
print(f"CLAIM Q2: computed={S_base:.9g} expected=1.791759 match={'yes' if round(S_base,6)==1.791759 else 'no'}")

# Q3
bits = S_base * (1/math.log(2))  # log2(e) = 1/ln2
print(f"CLAIM Q3: computed={bits:.9g} expected=2.584963 match={'yes' if round(bits,6)==2.584963 else 'no'}")

# Q4
m = math.ceil(math.log2(12))
print(f"CLAIM Q4: computed={m} expected=4 match={'yes' if m==4 else 'no'}")

# Q5
dim = 2**m
print(f"CLAIM Q5: computed={dim} expected=16 match={'yes' if dim==16 else 'no'}")

# Q6
wasted = dim - 12
print(f"CLAIM Q6: computed={wasted} expected=4 match={'yes' if wasted==4 else 'no'}")

# Q7
overhead = dim / 12
print(f"CLAIM Q7: computed={overhead:.9g} expected=1.333333 match={'yes' if round(overhead,6)==1.333333 else 'no'}")

# Q8
eta = math.log2(12) / m
print(f"CLAIM Q8: computed={eta:.9g} expected=0.896241 match={'yes' if round(eta,6)==0.896241 else 'no'}")

# Q9
idle = 1 - eta
print(f"CLAIM Q9: computed={idle:.9g} expected=0.103759 match={'yes' if round(idle,6)==0.103759 else 'no'}")

# Q10
gamma = 1e-3
p_X = p_Y = gamma/4
p_Z = gamma/2
p_I = 1 - gamma
print(f"CLAIM Q10: computed=p_X={p_X:.9g},p_Y={p_Y:.9g},p_Z={p_Z:.9g},p_I={p_I:.9g} expected=p_X=2.5e-4,p_Y=2.5e-4,p_Z=5e-4,p_I=0.999 match={'yes' if (abs(p_X-2.5e-4)<1e-12 and abs(p_Z-5e-4)<1e-12 and abs(p_I-0.999)<1e-12) else 'no'}")

# Q11
H_phys = -gamma*math.log2(gamma) - (1-gamma)*math.log2(1-gamma)
print(f"CLAIM Q11: computed={H_phys:.9g} expected=1.140776e-2 match={'yes' if abs(H_phys-1.140776e-2)<1e-9 else 'no'}")

# Q12
H_twirl = -(p_I*math.log2(p_I) + 2*p_X*math.log2(p_X) + p_Z*math.log2(p_Z))
print(f"CLAIM Q12: computed={H_twirl:.9g} expected=1.290776e-2 match={'yes' if abs(H_twirl-1.290776e-2)<1e-9 else 'no'}")

# Q13
Delta = H_twirl - H_phys
ratio = H_twirl / H_phys
print(f"CLAIM Q13: computed=Delta={Delta:.9g},ratio={ratio:.9g} expected=Delta=1.500000e-3,ratio=1.131489 match={'yes' if (abs(Delta-1.5e-3)<1e-9 and abs(ratio-1.131489)<1e-6) else 'no'}")

# Q14
Delta_exact = 3*gamma/2
print(f"CLAIM Q14: computed={Delta_exact:.9g} expected=1.5e-3 match={'yes' if abs(Delta_exact-1.5e-3)<1e-12 else 'no'}")

# Q15
n_bar = 0.1
d = 12
p_disc = (n_bar/(1+n_bar))**d
print(f"CLAIM Q15: computed={p_disc:.9g} expected=3.186308e-13 match={'yes' if abs(p_disc-3.186308e-13)<1e-20 else 'no'}")

# Q16
M = 1e4
N_cycles = 1e10
total = N_cycles * M * H_reg
print(f"CLAIM Q16: computed={total:.9g} expected=3.584963e14 match={'yes' if abs(total-3.584963e14)<1e5 else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, X match, Y mismatch")

```

## Execution output
```
CLAIM Q1: computed=3.5849625 expected=3.584963 match=yes
CLAIM Q2: computed=1.79175947 expected=1.791759 match=yes
CLAIM Q3: computed=2.5849625 expected=2.584963 match=yes
CLAIM Q4: computed=4 expected=4 match=yes
CLAIM Q5: computed=16 expected=16 match=yes
CLAIM Q6: computed=4 expected=4 match=yes
CLAIM Q7: computed=1.33333333 expected=1.333333 match=yes
CLAIM Q8: computed=0.896240625 expected=0.896241 match=yes
CLAIM Q9: computed=0.103759375 expected=0.103759 match=yes
CLAIM Q10: computed=p_X=0.00025,p_Y=0.00025,p_Z=0.0005,p_I=0.999 expected=p_X=2.5e-4,p_Y=2.5e-4,p_Z=5e-4,p_I=0.999 match=yes
CLAIM Q11: computed=0.0114077577 expected=1.140776e-2 match=no
CLAIM Q12: computed=0.0129077577 expected=1.290776e-2 match=no
CLAIM Q13: computed=Delta=0.0015,ratio=1.13148947 expected=Delta=1.500000e-3,ratio=1.131489 match=yes
CLAIM Q14: computed=0.0015 expected=1.5e-3 match=yes
CLAIM Q15: computed=3.18630818e-13 expected=3.186308e-13 match=no
CLAIM Q16: computed=3.5849625e+14 expected=3.584963e14 match=no
VERIFICATION SUMMARY: 16 claims, X match, Y mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3.5849625 | 3.584963 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q2 | 1.79175947 | 1.791759 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 2.5849625 | 2.584963 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q4 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 16 | 16 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 1.33333333 | 1.333333 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 0.896240625 | 0.896241 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q9 | 0.103759375 | 0.103759 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q10 | p_X=0.00025,p_Y=0.00025,p_Z=0.0005,p_I=0.999 | p_X=2.5e-4,p_Y=2.5e-4,p_Z=5e-4,p_I=0.999 | yes | match | script verdict (values not both numeric) |
| Q11 | 0.0114077577 | 1.140776e-2 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q12 | 0.0129077577 | 1.290776e-2 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q13 | Delta=0.0015,ratio=1.13148947 | Delta=1.500000e-3,ratio=1.131489 | yes | match | script verdict (values not both numeric) |
| Q14 | 0.0015 | 1.5e-3 | yes | match | 3 significant digits (as printed, at least 3) |
| Q15 | 3.18630818e-13 | 3.186308e-13 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q16 | 3.5849625e+14 | 3.584963e14 | no | match | 7 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
