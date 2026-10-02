# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Continuous optimum radix q* = 1 + sqrt(1 + c0/c1); for c0/c1 = 10, q* ≈ 4.31662479",
    "inputs": "c0=1, c1=0.1",
    "formula": "q* = 1 + sqrt(1 + c0/c1)"
  },
  {
    "id": "Q2",
    "statement": "For q=2, depth n = 20 and total cost E(2) = 2,516,581.2",
    "inputs": "N=1000000, c0=1, c1=0.1, q=2, ln(N)=13.815510, ln(2)=0.693147",
    "formula": "n = ceil(ln N / ln q) = ceil(13.815510/0.693147) = 20; M = (2^21 - 1)/1 = 2097151; E = (1 + 0.1*2)*2097151 = 2516581.2"
  },
  {
    "id": "Q3",
    "statement": "For q=3, depth n = 13 and total cost E(3) = 3,108,929.2",
    "inputs": "N=1000000, c0=1, c1=0.1, q=3, ln(N)=13.815510, ln(3)=1.098612",
    "formula": "n = ceil(13.815510/1.098612) = 13; M = (3^14 - 1)/2 = 2391484; E = (1 + 0.3)*2391484 = 3108929.2"
  },
  {
    "id": "Q4",
    "statement": "For q=4, depth n = 10, node count M = 1,398,101, total cost E(4) = 1,957,341.4 (optimal integer radix)",
    "inputs": "N=1000000, c0=1, c1=0.1, q=4, ln(N)=13.815510, ln(4)=1.386294",
    "formula": "n = ceil(13.815510/1.386294) = 10; M = (4^11 - 1)/3 = 1398101; E = (1 + 0.4)*1398101 = 1957341.4"
  },
  {
    "id": "Q5",
    "statement": "For q=5, depth n = 9 and total cost E(5) = 3,662,109.0",
    "inputs": "N=1000000, c0=1, c1=0.1, q=5, ln(N)=13.815510, ln(5)=1.609438",
    "formula": "n = ceil(13.815510/1.609438) = 9; M = (5^10 - 1)/4 = 2441406; E = (1 + 0.5)*2441406 = 3662109.0"
  },
  {
    "id": "Q6",
    "statement": "For q=7, depth n = 8 and total cost E(7) = 11,433,521.7",
    "inputs": "N=1000000, c0=1, c1=0.1, q=7, ln(N)=13.815510, ln(7)=1.945910",
    "formula": "n = ceil(13.815510/1.945910) = 8; M = (7^9 - 1)/6 = 6725601; E = (1 + 0.7)*6725601 = 11433521.7"
  },
  {
    "id": "Q7",
    "statement": "For q=10, depth n = 6 and total cost E(10) = 2,222,222.0",
    "inputs": "N=1000000, c0=1, c1=0.1, q=10, ln(N)=13.815510, ln(10)=2.302585",
    "formula": "n = ceil(13.815510/2.302585) = 6; M = (10^7 - 1)/9 = 1111111; E = (1 + 1.0)*1111111 = 2222222.0"
  },
  {
    "id": "Q8",
    "statement": "Saving of q=4 over q=2 is 22.2%",
    "inputs": "E(2)=2516581.2, E(4)=1957341.4",
    "formula": "(E(2) - E(4))/E(2) = (2516581.2 - 1957341.4)/2516581.2 = 0.222"
  }
]

## Script
```python
import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

def check(cid, computed, expected):
    if expected is None:
        m = "no"
    elif isinstance(computed, int) and isinstance(expected, int):
        m = "yes" if computed == expected else "no"
    else:
        m = "yes" if close(float(computed), float(expected)) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={m}")
    return m == "yes"

results = []

# Q1: continuous optimum
c0, c1 = 1.0, 0.1
qstar = 1 + math.sqrt(1 + c0 / c1)
results.append(check("Q1", round(qstar, 8), 4.31662479))

# Q2..Q7: exact integer evaluation for various q
N = 1000000
def evaluate(q):
    n = math.ceil(math.log(N) / math.log(q))
    M = (q ** (n + 1) - 1) // (q - 1)
    E = (c0 + c1 * q) * M
    return n, M, E

expected = {
    2: (20, 2097151, 2516581.2),
    3: (13, 2391484, 3108929.2),
    4: (10, 1398101, 1957341.4),
    5: (9, 2441406, 3662109.0),
    7: (8, 6725601, 11433521.7),
    10: (6, 1111111, 2222222.0),
}
ids = {2: "Q2", 3: "Q3", 4: "Q4", 5: "Q5", 7: "Q6", 10: "Q7"}
Evals = {}
for q in [2, 3, 4, 5, 7, 10]:
    n, M, E = evaluate(q)
    Evals[q] = E
    en, eM, eE = expected[q]
    ok = (n == en) and (M == eM) and close(E, eE)
    print(f"CLAIM {ids[q]}: computed=n={n},M={M},E={E} expected=n={en},M={eM},E={eE} match={'yes' if ok else 'no'}")
    results.append(ok)

# Q8: saving of q=4 over q=2
saving = (Evals[2] - Evals[4]) / Evals[2]
results.append(check("Q8", round(saving, 3), 0.222))

n_match = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results) - n_match} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4.31662479 expected=4.31662479 match=yes
CLAIM Q2: computed=n=20,M=2097151,E=2516581.1999999997 expected=n=20,M=2097151,E=2516581.2 match=yes
CLAIM Q3: computed=n=13,M=2391484,E=3108929.2 expected=n=13,M=2391484,E=3108929.2 match=yes
CLAIM Q4: computed=n=10,M=1398101,E=1957341.4 expected=n=10,M=1398101,E=1957341.4 match=yes
CLAIM Q5: computed=n=9,M=2441406,E=3662109.0 expected=n=9,M=2441406,E=3662109.0 match=yes
CLAIM Q6: computed=n=8,M=6725601,E=11433521.700000001 expected=n=8,M=6725601,E=11433521.7 match=yes
CLAIM Q7: computed=n=6,M=1111111,E=2222222.0 expected=n=6,M=1111111,E=2222222.0 match=yes
CLAIM Q8: computed=0.222 expected=0.222 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
