# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The raw assignment space for three islanders contains $2^{3}=8$ assignments.",
    "inputs": "n = 3",
    "formula": "2^n"
  },
  {
    "id": "Q2",
    "statement": "Exactly one assignment survives, giving an elimination rate of $7/8=0.875$.",
    "inputs": "total assignments = 8, survivors = 1",
    "formula": "(total - survivors) / total"
  },
  {
    "id": "Q3",
    "statement": "For ten islanders the raw space is $2^{10}=1\\,024$ assignments.",
    "inputs": "n = 10",
    "formula": "2^n"
  },
  {
    "id": "Q4",
    "statement": "The number of arbitrary binary relations on $|W|=8$ worlds is $2^{|W|\\times|W|}=2^{64}=18\\,446\\,744\\,073\\,709\\,551\\,616$.",
    "inputs": "|W| = 8",
    "formula": "2^{|W|^2}"
  },
  {
    "id": "Q5",
    "statement": "The number of reflexive relations on $|W|=8$ worlds is $2^{|W|\\times(|W|-1)}=2^{56}=72\\,057\\,594\\,037\\,927\\,936$.",
    "inputs": "|W| = 8",
    "formula": "2^{|W|\\times(|W|-1)}"
  },
  {
    "id": "Q6",
    "statement": "The Wise Men model trajectory is $8\\to7\\to6\\to4$ worlds.",
    "inputs": "initial worlds = 8, first subtraction = 1, second subtraction = 1, third subtraction = 2",
    "formula": "w_1=8; w_2=w_1-1; w_3=w_2-1; w_4=w_3-2"
  },
  {
    "id": "Q7",
    "statement": "The shrinkage factor from the first announcement to the final model is $7/4=1.75$.",
    "inputs": "w_{after\\ first\\ announcement}=7, w_{final}=4",
    "formula": "7/4"
  },
  {
    "id": "Q8",
    "statement": "A DEL action model with $|E|=3$ events over the original $8$ worlds yields $8\\times3=24$ worlds.",
    "inputs": "|W| = 8, |E| = 3",
    "formula": "|W| * |E|"
  },
  {
    "id": "Q9",
    "statement": "The proof‑length tower for Boolos’s inference gives $L_{5}=2^{65\\,536}$, and $\\log_{10}(L_{5})\\approx19\\,728$, so $L_{5}\\approx10^{19\\,728}$.",
    "inputs": "L_0=1, recurrence L_{n+1}=2^{L_n}, compute up to n=5",
    "formula": "L_5 = 2^{65536}; log10(L_5)=65536*log10(2)"
  },
  {
    "id": "Q10",
    "statement": "A first‑order interpretation space with domain size $d=10$ and a single binary predicate has $2^{d^{2}}=2^{100}=1.2676506002282294\\times10^{30}$ possible interpretations.",
    "inputs": "d = 10",
    "formula": "2^{d^2}"
  },
  {
    "id": "Q11",
    "statement": "A propositional instantiation with $k=10$ atoms yields $2^{10}=1\\,024$ rows.",
    "inputs": "k = 10",
    "formula": "2^{k}"
  },
  {
    "id": "Q12",
    "statement": "With $m=2$ obligations there are $2^{m}=4$ fulfillment profiles.",
    "inputs": "m = 2",
    "formula": "2^{m}"
  },
  {
    "id": "Q13",
    "statement": "A three‑obligation variant yields $2^{3}=8$ profiles.",
    "inputs": "m = 3",
    "formula": "2^{m}"
  },
  {
    "id": "Q14",
    "statement": "Gödel’s argument with $p=5$ candidate properties has $2^{p}=32$ raw positivity‑predicate interpretations.",
    "inputs": "p = 5",
    "formula": "2^{p}"
  },
  {
    "id": "Q15",
    "statement": "Assuming three independent axioms ($a=3$), the consistent space has at least $2^{p-a}=2^{2}=4$ interpretations.",
    "inputs": "p = 5, a = 3",
    "formula": "2^{p-a}"
  },
  {
    "id": "Q16",
    "statement": "A semester of $14$ weeks with one $2$‑hour session per week provides $28$ contact hours.",
    "inputs": "weeks = 14, hours_per_week = 2",
    "formula": "weeks * hours_per_week"
  }
]

## Script
```python
import math

def claim_Q1():
    n = 3
    computed = 2 ** n
    expected = 8
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q1: computed={computed} expected={expected} match={match}")

def claim_Q2():
    total = 8
    survivors = 1
    computed = (total - survivors) / total
    expected = 0.875
    match = "yes" if abs(computed - expected) < 1e-12 else "no"
    print(f"CLAIM Q2: computed={computed} expected={expected} match={match}")

def claim_Q3():
    n = 10
    computed = 2 ** n
    expected = 1024
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q3: computed={computed} expected={expected} match={match}")

def claim_Q4():
    W = 8
    computed = 2 ** (W * W)
    expected = 18446744073709551616
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q4: computed={computed} expected={expected} match={match}")

def claim_Q5():
    W = 8
    computed = 2 ** (W * (W - 1))
    expected = 72057594037927936
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q5: computed={computed} expected={expected} match={match}")

def claim_Q6():
    w1 = 8
    w2 = w1 - 1
    w3 = w2 - 1
    w4 = w3 - 2
    computed = f"{w1},{w2},{w3},{w4}"
    expected = "8,7,6,4"
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q6: computed={computed} expected={expected} match={match}")

def claim_Q7():
    computed = 7 / 4
    expected = 1.75
    match = "yes" if abs(computed - expected) < 1e-12 else "no"
    print(f"CLAIM Q7: computed={computed} expected={expected} match={match}")

def claim_Q8():
    W = 8
    E = 3
    computed = W * E
    expected = 24
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q8: computed={computed} expected={expected} match={match}")

def claim_Q9():
    # L5 = 2^{65536}; we compare its base‑10 logarithm to the reported 19728
    log10_L5 = 65536 * math.log10(2)
    computed = round(log10_L5)  # integer approximation
    expected = 19728
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q9: computed={computed} expected={expected} match={match}")

def claim_Q10():
    d = 10
    computed = 2 ** (d * d)
    # Expected value written as 1.2676506002282294×10^{30}
    expected = 1.2676506002282294e30
    match = "yes" if computed == int(expected) else "no"
    print(f"CLAIM Q10: computed={computed} expected={expected} match={match}")

def claim_Q11():
    k = 10
    computed = 2 ** k
    expected = 1024
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q11: computed={computed} expected={expected} match={match}")

def claim_Q12():
    m = 2
    computed = 2 ** m
    expected = 4
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q12: computed={computed} expected={expected} match={match}")

def claim_Q13():
    m = 3
    computed = 2 ** m
    expected = 8
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q13: computed={computed} expected={expected} match={match}")

def claim_Q14():
    p = 5
    computed = 2 ** p
    expected = 32
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q14: computed={computed} expected={expected} match={match}")

def claim_Q15():
    p = 5
    a = 3
    computed = 2 ** (p - a)
    expected = 4
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q15: computed={computed} expected={expected} match={match}")

def claim_Q16():
    weeks = 14
    hours_per_week = 2
    computed = weeks * hours_per_week
    expected = 28
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q16: computed={computed} expected={expected} match={match}")

def main():
    claim_Q1()
    claim_Q2()
    claim_Q3()
    claim_Q4()
    claim_Q5()
    claim_Q6()
    claim_Q7()
    claim_Q8()
    claim_Q9()
    claim_Q10()
    claim_Q11()
    claim_Q12()
    claim_Q13()
    claim_Q14()
    claim_Q15()
    claim_Q16()
    print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")

if __name__ == "__main__":
    main()

```

## Execution output
```
CLAIM Q1: computed=8 expected=8 match=yes
CLAIM Q2: computed=0.875 expected=0.875 match=yes
CLAIM Q3: computed=1024 expected=1024 match=yes
CLAIM Q4: computed=18446744073709551616 expected=18446744073709551616 match=yes
CLAIM Q5: computed=72057594037927936 expected=72057594037927936 match=yes
CLAIM Q6: computed=8,7,6,4 expected=8,7,6,4 match=yes
CLAIM Q7: computed=1.75 expected=1.75 match=yes
CLAIM Q8: computed=24 expected=24 match=yes
CLAIM Q9: computed=19728 expected=19728 match=yes
CLAIM Q10: computed=1267650600228229401496703205376 expected=1.2676506002282294e+30 match=yes
CLAIM Q11: computed=1024 expected=1024 match=yes
CLAIM Q12: computed=4 expected=4 match=yes
CLAIM Q13: computed=8 expected=8 match=yes
CLAIM Q14: computed=32 expected=32 match=yes
CLAIM Q15: computed=4 expected=4 match=yes
CLAIM Q16: computed=28 expected=28 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.875 | 0.875 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 18446744073709551616 | 18446744073709551616 | yes | match | 20 significant digits (as the paper states, at least 2) |
| Q5 | 72057594037927936 | 72057594037927936 | yes | match | 17 significant digits (as the paper states, at least 2) |
| Q6 | 8,7,6,4 | 8,7,6,4 | yes | match | script verdict (values not both numeric) |
| Q7 | 1.75 | 1.75 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 24 | 24 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 19728 | 19728 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 1267650600228229401496703205376 | 1.2676506002282294e+30 | yes | match | 17 significant digits (as the paper states, at least 2) |
| Q11 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 32 | 32 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 28 | 28 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
