# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Register entropy for a qudit of dimension d=12 is H_{reg}=3.584963 bits per mode per use.",
    "inputs": "d = 12",
    "formula": "H_{reg}=\\log_{2}(d)"
  },
  {
    "id": "Q2",
    "statement": "Base truncation entropy for d=12 is S_{Base}=1.791759 nats = 2.584963 bits.",
    "inputs": "d = 12, \\log_{2}e = 1.442695",
    "formula": "S_{Base}=\\ln(d/2); \\text{bits}=S_{Base}\\times\\log_{2}e"
  },
  {
    "id": "Q3",
    "statement": "Number of qubits required to binary‑encode a d=12 qudit is m=4.",
    "inputs": "d = 12",
    "formula": "m=\\lceil\\log_{2} d\\rceil"
  },
  {
    "id": "Q4",
    "statement": "Encoded Hilbert‑space dimension for m=4 qubits is 2^{m}=16.",
    "inputs": "m = 4",
    "formula": "2^{m}"
  },
  {
    "id": "Q5",
    "statement": "Wasted levels when encoding d=12 into 4 qubits is 4.",
    "inputs": "2^{m}=16, d=12",
    "formula": "2^{m}-d"
  },
  {
    "id": "Q6",
    "statement": "Dimension‑overhead ratio for d=12 is 4/3 ≈ 1.333333.",
    "inputs": "2^{m}=16, d=12",
    "formula": "\\frac{2^{m}}{d}"
  },
  {
    "id": "Q7",
    "statement": "Encoding efficiency for d=12 is \\eta=0.896241.",
    "inputs": "d = 12, m = 4",
    "formula": "\\eta=\\frac{\\log_{2} d}{m}"
  },
  {
    "id": "Q8",
    "statement": "Idle fraction of the binary encoding for d=12 is 0.103759 (≈10.4%).",
    "inputs": "\\eta = 0.896241",
    "formula": "1-\\eta"
  },
  {
    "id": "Q9",
    "statement": "Physical environment entropy for amplitude‑damping with \\gamma=10^{-3} is H_{env}^{phys}=0.011408 bits.",
    "inputs": "\\gamma = 1\\times10^{-3}",
    "formula": "H_{env}^{phys}= -\\gamma\\log_{2}\\gamma-(1-\\gamma)\\log_{2}(1-\\gamma)"
  },
  {
    "id": "Q10",
    "statement": "Environment entropy of the Pauli‑twirled surrogate at \\gamma=10^{-3} is H_{env}^{twirl}=0.012908 bits.",
    "inputs": "\\gamma = 1\\times10^{-3}, p_X=p_Y=\\gamma/4, p_Z=\\gamma/2, p_I=1-\\gamma",
    "formula": "H_{env}^{twirl}= -\\sum_{i} p_i\\log_{2} p_i"
  },
  {
    "id": "Q11",
    "statement": "Entropy distortion for \\gamma=10^{-3} is \\Delta H = 1.5\\times10^{-3} bits.",
    "inputs": "H_{env}^{twirl}=0.012908 bits, H_{env}^{phys}=0.011408 bits",
    "formula": "\\Delta H = H_{env}^{twirl} - H_{env}^{phys}"
  },
  {
    "id": "Q12",
    "statement": "Ratio of twirled to physical environment entropy for \\gamma=10^{-3} is 1.131489.",
    "inputs": "H_{env}^{twirl}=0.012908 bits, H_{env}^{phys}=0.011408 bits",
    "formula": "H_{env}^{twirl} / H_{env}^{phys}"
  },
  {
    "id": "Q13",
    "statement": "Exact linear scaling of distortion is \\Delta H = 3\\gamma/2 bits for any \\gamma.",
    "inputs": "\\gamma (symbolic)",
    "formula": "\\Delta H = \\frac{3\\gamma}{2}"
  },
  {
    "id": "Q14",
    "statement": "Discarded Hilbert‑space weight for \\bar n=0.1 and d=12 is p_{disc}=3.186308\\times10^{-13}.",
    "inputs": "\\bar n = 0.1, d = 12",
    "formula": "p_{disc}=\\left(\\frac{\\bar n}{1+\\bar n}\\right)^{d}"
  },
  {
    "id": "Q15",
    "statement": "Cumulative register bookkeeping for M=10^{4} modes and N_{cycles}=10^{10} cycles is 3.584963\\times10^{14} bits.",
    "inputs": "H_{reg}=3.584963 bits, M=10^{4}, N_{cycles}=10^{10}",
    "formula": "N_{cycles}\\times M \\times H_{reg}"
  },
  {
    "id": "Q16",
    "statement": "Register entropy for d=20 is 4.321928 bits.",
    "inputs": "d = 20",
    "formula": "H_{reg}=\\log_{2} d"
  }
]

## Script
```python
import math

def log2(x):
    return math.log(x, 2)

def compute():
    # Q1
    d = 12
    H_reg = log2(d)
    exp_Q1 = "3.584963"
    print(f"CLAIM Q1: computed={H_reg:.9g} expected={exp_Q1} match={'yes' if round(H_reg,6)==float(exp_Q1) else 'no'}")
    
    # Q2
    S_base = math.log(d/2)  # nats
    bits = S_base * log2(math.e)
    exp_Q2 = "2.584963"
    print(f"CLAIM Q2: computed={bits:.9g} expected={exp_Q2} match={'yes' if round(bits,6)==float(exp_Q2) else 'no'}")
    
    # Q3
    m = math.ceil(log2(d))
    exp_Q3 = "4"
    print(f"CLAIM Q3: computed={m} expected={exp_Q3} match={'yes' if m==int(exp_Q3) else 'no'}")
    
    # Q4
    hilbert_dim = 2**m
    exp_Q4 = "16"
    print(f"CLAIM Q4: computed={hilbert_dim} expected={exp_Q4} match={'yes' if hilbert_dim==int(exp_Q4) else 'no'}")
    
    # Q5
    wasted = hilbert_dim - d
    exp_Q5 = "4"
    print(f"CLAIM Q5: computed={wasted} expected={exp_Q5} match={'yes' if wasted==int(exp_Q5) else 'no'}")
    
    # Q6
    dim_overhead = hilbert_dim / d
    exp_Q6 = "1.333333"
    print(f"CLAIM Q6: computed={dim_overhead:.9g} expected={exp_Q6} match={'yes' if round(dim_overhead,6)==float(exp_Q6) else 'no'}")
    
    # Q7
    eta = log2(d) / m
    exp_Q7 = "0.896241"
    print(f"CLAIM Q7: computed={eta:.9g} expected={exp_Q7} match={'yes' if round(eta,6)==float(exp_Q7) else 'no'}")
    
    # Q8
    idle = 1 - eta
    exp_Q8 = "0.103759"
    print(f"CLAIM Q8: computed={idle:.9g} expected={exp_Q8} match={'yes' if round(idle,6)==float(exp_Q8) else 'no'}")
    
    # Q9
    gamma = 1e-3
    H_phys = -gamma*log2(gamma) - (1-gamma)*log2(1-gamma)
    exp_Q9 = "0.011408"
    print(f"CLAIM Q9: computed={H_phys:.9g} expected={exp_Q9} match={'yes' if round(H_phys,6)==float(exp_Q9) else 'no'}")
    
    # Q10
    p_I = 1 - gamma
    p_X = p_Y = gamma/4
    p_Z = gamma/2
    H_twirl = -(p_I*log2(p_I) + 2*p_X*log2(p_X) + p_Z*log2(p_Z))
    exp_Q10 = "0.012908"
    print(f"CLAIM Q10: computed={H_twirl:.9g} expected={exp_Q10} match={'yes' if round(H_twirl,6)==float(exp_Q10) else 'no'}")
    
    # Q11
    delta_H = H_twirl - H_phys
    exp_Q11 = "1.5e-03"
    print(f"CLAIM Q11: computed={delta_H:.9g} expected={exp_Q11} match={'yes' if abs(delta_H - 1.5e-3) < 1e-12 else 'no'}")
    
    # Q12
    ratio = H_twirl / H_phys
    exp_Q12 = "1.131489"
    print(f"CLAIM Q12: computed={ratio:.9g} expected={exp_Q12} match={'yes' if round(ratio,6)==float(exp_Q12) else 'no'}")
    
    # Q13
    # symbolic linear law; test with gamma=1e-3
    delta_linear = 3*gamma/2
    exp_Q13 = "3*gamma/2"
    print(f"CLAIM Q13: computed={delta_linear:.9g} expected={exp_Q13} match={'yes' if abs(delta_linear - delta_H) < 1e-12 else 'no'}")
    
    # Q14
    n_bar = 0.1
    p_disc = (n_bar/(1+n_bar))**d
    exp_Q14 = "3.186308e-13"
    print(f"CLAIM Q14: computed={p_disc:.9g} expected={exp_Q14} match={'yes' if abs(p_disc - 3.186308e-13) < 1e-20 else 'no'}")
    
    # Q15
    M = 1e4
    N_cycles = 1e10
    total_bits = N_cycles * M * H_reg
    exp_Q15 = "3.584963e+14"
    print(f"CLAIM Q15: computed={total_bits:.9g} expected={exp_Q15} match={'yes' if abs(total_bits - 3.584963e14) < 1e5 else 'no'}")
    
    # Q16
    d20 = 20
    H_reg20 = log2(d20)
    exp_Q16 = "4.321928"
    print(f"CLAIM Q16: computed={H_reg20:.9g} expected={exp_Q16} match={'yes' if round(H_reg20,6)==float(exp_Q16) else 'no'}")
    
    # Summary
    claims = 16
    matches = sum(1 for line in open(__file__) if "match=yes" in line)  # placeholder, not used
    # Since we cannot count matches programmatically here, we just print a static summary.
    print(f"VERIFICATION SUMMARY: {claims} claims, {matches} match, {claims - matches} mismatch")

if __name__ == "__main__":
    compute()

```

## Execution output
```
CLAIM Q1: computed=3.5849625 expected=3.584963 match=yes
CLAIM Q2: computed=2.5849625 expected=2.584963 match=yes
CLAIM Q3: computed=4 expected=4 match=yes
CLAIM Q4: computed=16 expected=16 match=yes
CLAIM Q5: computed=4 expected=4 match=yes
CLAIM Q6: computed=1.33333333 expected=1.333333 match=yes
CLAIM Q7: computed=0.896240625 expected=0.896241 match=yes
CLAIM Q8: computed=0.103759375 expected=0.103759 match=yes
CLAIM Q9: computed=0.0114077577 expected=0.011408 match=yes
CLAIM Q10: computed=0.0129077577 expected=0.012908 match=yes
CLAIM Q11: computed=0.0015 expected=1.5e-03 match=yes
CLAIM Q12: computed=1.13148947 expected=1.131489 match=yes
CLAIM Q13: computed=0.0015 expected=3*gamma/2 match=yes
CLAIM Q14: computed=3.18630818e-13 expected=3.186308e-13 match=no
CLAIM Q15: computed=3.5849625e+14 expected=3.584963e+14 match=no
CLAIM Q16: computed=4.32192809 expected=4.321928 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 105, in <module>
  File "<string>", line 100, in compute
NameError: name '__file__' is not defined. Did you mean: '__name__'?

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3.5849625 | 3.584963 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q2 | 2.5849625 | 2.584963 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 16 | 16 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 1.33333333 | 1.333333 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q7 | 0.896240625 | 0.896241 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 0.103759375 | 0.103759 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q9 | 0.0114077577 | 0.011408 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 0.0129077577 | 0.012908 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q11 | 0.0015 | 1.5e-03 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 1.13148947 | 1.131489 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q13 | 0.0015 | 3*gamma/2 | yes | match | script verdict (values not both numeric) |
| Q14 | 3.18630818e-13 | 3.186308e-13 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q15 | 3.5849625e+14 | 3.584963e+14 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q16 | 4.32192809 | 4.321928 | yes | match | 7 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
