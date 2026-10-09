# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Real dimension of the pure-state arena for n=10 is 2046",
    "inputs": "n=10",
    "formula": "2^(n+1) - 2"
  },
  {
    "id": "Q2",
    "statement": "Real dimension of the pure-state arena for n=50 is approximately 2.25e15",
    "inputs": "n=50",
    "formula": "2^(n+1) - 2"
  },
  {
    "id": "Q3",
    "statement": "Hilbert-space dimension D_50 is approximately 1.1259e15",
    "inputs": "n=50, log10(2)=0.301030",
    "formula": "2^n = 10^(n*log10(2))"
  },
  {
    "id": "Q4",
    "statement": "Hilbert-space dimension D_100 is approximately 1.2677e30",
    "inputs": "n=100, log10(2)=0.301030",
    "formula": "2^n = 10^(n*log10(2))"
  },
  {
    "id": "Q5",
    "statement": "Hilbert-space dimension D_300 is approximately 2.037e90",
    "inputs": "n=300, log10(2)=0.301030",
    "formula": "2^n = 10^(n*log10(2))"
  },
  {
    "id": "Q6",
    "statement": "Mixed-state parameter count for n=10 is 1,048,575",
    "inputs": "n=10",
    "formula": "4^n - 1"
  },
  {
    "id": "Q7",
    "statement": "Mixed-state parameter count for n=100 is approximately 1.6069e60",
    "inputs": "n=100, log10(2)=0.301030",
    "formula": "4^n - 1 = 10^(2n*log10(2)) - 1"
  },
  {
    "id": "Q8",
    "statement": "Memory for one n=50 state vector is 2^54 = 18,014,398,509,481,984 bytes = 16 PiB",
    "inputs": "bytes per amplitude=16, n=50",
    "formula": "M_n = 16 * 2^n"
  }
]

## Script
```python
import math

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = "n/a"
        print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
        return 0, 1  # no expected, count as informational
    if isinstance(computed, int) and isinstance(expected, int):
        match = computed == expected
    else:
        match = math.isclose(computed, expected, rel_tol=tol)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")
    return (1 if match else 0), 1

matched = 0
total = 0

# Q1: real dimension of pure-state arena for n=10: 2^(n+1) - 2
n1 = 10
q1 = 2**(n1 + 1) - 2
m, t = check("Q1", q1, 2046)
matched += m; total += t

# Q2: real dimension for n=50: 2^(n+1) - 2, approximately 2.25e15
n2 = 50
q2 = 2**(n2 + 1) - 2
q2_approx = q2 / 1e15  # express in units of 1e15
m, t = check("Q2", q2_approx, 2.25, tol=1e-2)
matched += m; total += t

# Q3: D_50 = 2^50 via 10^(n*log10(2)), log10(2)=0.301030
n3 = 50
log10_2 = 0.301030
q3 = 10**(n3 * log10_2)
m, t = check("Q3", q3, 1.1259e15, tol=1e-4)
matched += m; total += t

# Q4: D_100 = 2^100 via 10^(100*log10(2))
n4 = 100
q4 = 10**(n4 * log10_2)
m, t = check("Q4", q4, 1.2677e30, tol=1e-4)
matched += m; total += t

# Q5: D_300 = 2^300 via 10^(300*log10(2))
n5 = 300
q5 = 10**(n5 * log10_2)
m, t = check("Q5", q5, 2.037e90, tol=1e-3)
matched += m; total += t

# Q6: mixed-state parameter count for n=10: 4^n - 1
n6 = 10
q6 = 4**n6 - 1
m, t = check("Q6", q6, 1048575)
matched += m; total += t

# Q7: mixed-state parameter count for n=100: 4^100 - 1 = 10^(200*log10(2)) - 1
n7 = 100
q7 = 10**(2 * n7 * log10_2) - 1
m, t = check("Q7", q7, 1.6069e60, tol=1e-4)
matched += m; total += t

# Q8: memory for one n=50 state vector: M_n = 16 * 2^n bytes
bytes_per_amplitude = 16
n8 = 50
q8 = bytes_per_amplitude * 2**n8
m, t = check("Q8", q8, 18014398509481984)
matched += m; total += t

print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {total - matched} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2046 expected=2046 match=yes
CLAIM Q2: computed=2.251799813685246 expected=2.25 match=yes
CLAIM Q3: computed=1125900468894942.0 expected=1125900000000000.0 match=yes
CLAIM Q4: computed=1.2676518658578502e+30 expected=1.2677e+30 match=yes
CLAIM Q5: computed=2.037042077705773e+90 expected=2.037e+90 match=yes
CLAIM Q6: computed=1048575 expected=1048575 match=yes
CLAIM Q7: computed=1.6069412530128885e+60 expected=1.6069e+60 match=yes
CLAIM Q8: computed=18014398509481984 expected=18014398509481984 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
