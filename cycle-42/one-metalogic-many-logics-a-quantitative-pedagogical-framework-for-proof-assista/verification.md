# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The propositional search space for 3 islanders has 8 assignments, of which exactly 1 survives, giving an elimination rate of 0.875.",
    "inputs": "n=3 islanders; survivors=1",
    "formula": "2^n = 2^3 = 8; elimination_rate = (8-1)/8 = 7/8 = 0.875"
  },
  {
    "id": "Q2",
    "statement": "For n=10 islanders the raw propositional space is 1024 assignments.",
    "inputs": "n=10",
    "formula": "2^10 = 1024"
  },
  {
    "id": "Q3",
    "statement": "The number of distinct binary accessibility relations on 8 worlds is 2^64 = 18446744073709551616 ≈ 1.84e19.",
    "inputs": "|W|=8",
    "formula": "2^(|W|*|W|) = 2^(8*8) = 2^64"
  },
  {
    "id": "Q4",
    "statement": "The number of reflexive accessibility relations on 8 worlds is 2^56 ≈ 7.21e16.",
    "inputs": "|W|=8",
    "formula": "2^(|W|*(|W|-1)) = 2^(8*7) = 2^56 = 72057594037927936"
  },
  {
    "id": "Q5",
    "statement": "The Wise Men model trajectory under public announcements is 8 -> 7 -> 6 -> 4, with shrinkage factor 7/4 = 1.75 from the first announcement onward.",
    "inputs": "|W0|=2^3=8; eliminations: 1, then 1, then 2",
    "formula": "|W1| = 8-1 = 7; |W2| = 7-1 = 6; |W3| = 6-2 = 4; shrinkage = 7/4 = 1.75"
  },
  {
    "id": "Q6",
    "statement": "A DEL action model with |E|=3 events over 8 original worlds yields 24 worlds.",
    "inputs": "|W|=8; |E|=3",
    "formula": "|W_new| = |W|*|E| = 8*3 = 24"
  },
  {
    "id": "Q7",
    "statement": "Boolos first-order proof-length tower: L1=2, L2=4, L3=16, L4=65536, L5 ≈ 10^19728.",
    "inputs": "L0=1; recurrence L_{n+1}=2^{L_n}",
    "formula": "L1=2^1=2; L2=2^2=4; L3=2^4=16; L4=2^16=65536; L5=2^65536; log10(L5)=65536*log10(2)=65536*0.30103=19728.3"
  },
  {
    "id": "Q8",
    "statement": "A first-order encoding with domain size d=10 and one binary predicate has 2^100 ≈ 1.27e30 candidate interpretations.",
    "inputs": "d=10",
    "formula": "2^(d^2) = 2^100 = 1267650600228229401496703205376"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if isinstance(expected, float) or isinstance(computed, float):
        match = math.isclose(float(computed), float(expected), rel_tol=1e-6)
    else:
        match = computed == expected
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")
    return match

results = []

# Q1: n=3 islanders; survivors=1
n = 3
survivors = 1
space = 2 ** n                      # 2^3 = 8
elim_rate = (space - survivors) / space   # (8-1)/8 = 7/8
results.append(check("Q1", elim_rate, 0.875))

# Q2: n=10 islanders, raw propositional space
n10 = 10
space10 = 2 ** n10                  # 2^10 = 1024
results.append(check("Q2", space10, 1024))

# Q3: distinct binary accessibility relations on 8 worlds
W = 8
rel_count = 2 ** (W * W)            # 2^64
results.append(check("Q3", rel_count, 18446744073709551616))
# also verify the approximation 1.84e19
approx_ok = math.isclose(rel_count, 1.84e19, rel_tol=0.01)
print(f"CLAIM Q3-approx: computed={rel_count} expected=1.84e19 match={'yes' if approx_ok else 'no'}")
results.append(approx_ok)

# Q4: reflexive accessibility relations on 8 worlds
refl_count = 2 ** (W * (W - 1))     # 2^56
results.append(check("Q4", refl_count, 72057594037927936))
approx_ok4 = math.isclose(refl_count, 7.21e16, rel_tol=0.01)
print(f"CLAIM Q4-approx: computed={refl_count} expected=7.21e16 match={'yes' if approx_ok4 else 'no'}")
results.append(approx_ok4)

# Q5: Wise Men trajectory 8 -> 7 -> 6 -> 4, shrinkage 7/4
W0 = 2 ** 3                          # 8
W1 = W0 - 1                          # 7
W2 = W1 - 1                          # 6
W3 = W2 - 2                          # 4
shrink = W1 / W3                     # 7/4
results.append(check("Q5", shrink, 1.75))
traj_ok = (W0, W1, W2, W3) == (8, 7, 6, 4)
print(f"CLAIM Q5-traj: computed={(W0, W1, W2, W3)} expected=(8, 7, 6, 4) match={'yes' if traj_ok else 'no'}")
results.append(traj_ok)

# Q6: DEL product update |W|=8, |E|=3
Wsize = 8
Esize = 3
Wnew = Wsize * Esize                 # 24
results.append(check("Q6", Wnew, 24))

# Q7: Boolos tower L0=1, L_{n+1}=2^{L_n}
L = [1]
for _ in range(5):
    L.append(2 ** L[-1])             # L1=2, L2=4, L3=16, L4=65536, L5=2^65536
results.append(check("Q7-L1", L[1], 2))
results.append(check("Q7-L2", L[2], 4))
results.append(check("Q7-L3", L[3], 16))
results.append(check("Q7-L4", L[4], 65536))
log10_L5 = L[4] * math.log10(2)      # 65536 * 0.30103 = 19728.3
results.append(check("Q7-L5log", round(log10_L5, 1), 19728.3))

# Q8: first-order interpretations, d=10, one binary predicate
d = 10
interp_count = 2 ** (d * d)          # 2^100
results.append(check("Q8", interp_count, 1267650600228229401496703205376))
approx_ok8 = math.isclose(interp_count, 1.27e30, rel_tol=0.01)
print(f"CLAIM Q8-approx: computed={interp_count} expected=1.27e30 match={'yes' if approx_ok8 else 'no'}")
results.append(approx_ok8)

total = len(results)
matched = sum(1 for r in results if r)
mismatch = total - matched
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.875 expected=0.875 match=yes
CLAIM Q2: computed=1024 expected=1024 match=yes
CLAIM Q3: computed=18446744073709551616 expected=18446744073709551616 match=yes
CLAIM Q3-approx: computed=18446744073709551616 expected=1.84e19 match=yes
CLAIM Q4: computed=72057594037927936 expected=72057594037927936 match=yes
CLAIM Q4-approx: computed=72057594037927936 expected=7.21e16 match=yes
CLAIM Q5: computed=1.75 expected=1.75 match=yes
CLAIM Q5-traj: computed=(8, 7, 6, 4) expected=(8, 7, 6, 4) match=yes
CLAIM Q6: computed=24 expected=24 match=yes
CLAIM Q7-L1: computed=2 expected=2 match=yes
CLAIM Q7-L2: computed=4 expected=4 match=yes
CLAIM Q7-L3: computed=16 expected=16 match=yes
CLAIM Q7-L4: computed=65536 expected=65536 match=yes
CLAIM Q7-L5log: computed=19728.3 expected=19728.3 match=yes
CLAIM Q8: computed=1267650600228229401496703205376 expected=1267650600228229401496703205376 match=yes
CLAIM Q8-approx: computed=1267650600228229401496703205376 expected=1.27e30 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```
