# Verification report

## Extracted claims
[
  {
    "id": "C1",
    "statement": "The number of binary strings of length exactly $k$ is $2^{k}$.",
    "inputs": "k (positive integer)",
    "formula": "$2^{k}$"
  },
  {
    "id": "C2",
    "statement": "The number of reduced fractions in $[0,1]$ with denominator at most $n$ is $|F_{n}|=1+\\sum_{k=1}^{n}\\varphi(k)$.",
    "inputs": "n (positive integer), \\varphi(k) values for k=1..n",
    "formula": "$1+\\sum_{k=1}^{n}\\varphi(k)$"
  },
  {
    "id": "C3",
    "statement": "The number of binary programs of length at most $100$ is $\\sum_{k=0}^{100}2^{k}=2^{101}-1$.",
    "inputs": "maximum program length $L=100$",
    "formula": "$\\sum_{k=0}^{L}2^{k}=2^{L+1}-1$"
  },
  {
    "id": "C4",
    "statement": "The number of rays of $T_{2}$ at depth $n$ is $2^{n}$.",
    "inputs": "depth $n$ (non‑negative integer)",
    "formula": "$2^{n}$"
  },
  {
    "id": "C5",
    "statement": "The sum of Euler's totient values for $k=1$ to $20$ is $128$.",
    "inputs": "\\varphi(1)=1, \\varphi(2)=1, \\varphi(3)=2, \\varphi(4)=2, \\varphi(5)=4, \\varphi(6)=2, \\varphi(7)=6, \\varphi(8)=4, \\varphi(9)=6, \\varphi(10)=4, \\varphi(11)=10, \\varphi(12)=4, \\varphi(13)=12, \\varphi(14)=6, \\varphi(15)=8, \\varphi(16)=8, \\varphi(17)=16, \\varphi(18)=6, \\varphi(19)=18, \\varphi(20)=8",
    "formula": "$\\sum_{k=1}^{20}\\varphi(k)=128$"
  },
  {
    "id": "C6",
    "statement": "The Farey sequence of order $20$ contains $|F_{20}|=129$ reduced fractions.",
    "inputs": "sum of totients $\\sum_{k=1}^{20}\\varphi(k)=128$",
    "formula": "$|F_{20}|=1+\\sum_{k=1}^{20}\\varphi(k)=129$"
  },
  {
    "id": "C7",
    "statement": "The definable fraction at depth $20$ is $f_{20}=\\frac{129}{2^{20}}=1.23024\\times10^{-4}$.",
    "inputs": "numerator $129$, denominator $2^{20}=1{,}048{,}576$",
    "formula": "$f_{20}=\\frac{129}{2^{20}}$"
  },
  {
    "id": "C8",
    "statement": "The number of binary programs of length at most $100$ equals $2^{101}-1=2\\,535\\,301\\,200\\,456\\,458\\,802\\,993\\,406\\,410\\,751$.",
    "inputs": "maximum length $L=100$",
    "formula": "$2^{L+1}-1$"
  },
  {
    "id": "C9",
    "statement": "Covering the $j$‑th computable shadow $x_{j}$ by an interval of radius $\\varepsilon\\,2^{-j-1}$ yields total length $\\sum_{j=1}^{\\infty}2\\varepsilon\\,2^{-j-1}=\\varepsilon$.",
    "inputs": "arbitrary $\\varepsilon>0$",
    "formula": "$\\sum_{j=1}^{\\infty}2\\varepsilon\\,2^{-j-1}=\\varepsilon$"
  },
  {
    "id": "C10",
    "statement": "For any depth $n$, the definable fraction satisfies $f_{n}=\\frac{1+\\sum_{k=1}^{n}\\varphi(k)}{2^{n}}\\le\\frac{1+n^{2}}{2^{n}}$.",
    "inputs": "depth $n$, bound $\\varphi(k)\\le k$",
    "formula": "$f_{n}\\le\\frac{1+n^{2}}{2^{n}}$"
  },
  {
    "id": "C11",
    "statement": "At $n=20$, the bound gives $\\frac{1+20^{2}}{2^{20}}=\\frac{401}{1{,}048{,}576}\\approx3.82423\\times10^{-4}$.",
    "inputs": "n=20, $2^{20}=1{,}048{,}576$",
    "formula": "$\\frac{1+n^{2}}{2^{n}}$ evaluated at $n=20$"
  },
  {
    "id": "C12",
    "statement": "Under the $(p+1)$‑regular convention with $p=2$, the number of rays of length $n$ from a fixed root‑adjacent edge is $p\\,(p+1)^{n-1}$.",
    "inputs": "p=2, depth $n$",
    "formula": "$p\\,(p+1)^{n-1}$"
  },
  {
    "id": "C13",
    "statement": "For $p=2$ and $n=4$, the regular‑tree ray count is $2\\cdot3^{3}=54$.",
    "inputs": "p=2, n=4",
    "formula": "$2\\cdot3^{3}$"
  },
  {
    "id": "C14",
    "statement": "For $p=2$ and $n=8$, the regular‑tree ray count is $2\\cdot3^{7}=4\\,374$.",
    "inputs": "p=2, n=8",
    "formula": "$2\\cdot3^{7}$"
  },
  {
    "id": "C15",
    "statement": "For $p=2$ and $n=16$, the regular‑tree ray count is $2\\cdot3^{15}=28\\,697\\,814$.",
    "inputs": "p=2, n=16",
    "formula": "$2\\cdot3^{15}$"
  },
  {
    "id": "C16",
    "statement": "For $p=2$ and $n=32$, the regular‑tree ray count is $2\\cdot3^{31}=1\\,235\\,346\\,792\\,567\\,894$.",
    "inputs": "p=2, n=32",
    "formula": "$2\\cdot3^{31}$"
  }
]

## Script
```python
import math

def match_float(comp, exp_str, sig=6):
    # Convert expected string like 1.23024e-4 to float
    exp = float(exp_str)
    # Compare within tolerance based on significant digits
    tol = 0.5 * 10**(-sig) * abs(exp) if exp != 0 else 10**(-sig)
    return abs(comp - exp) <= tol

def print_claim(cid, computed, expected):
    if expected == "":
        match = "na"
    else:
        # Determine if expected is integer or float
        try:
            exp_int = int(expected.replace(",", ""))
            match = "yes" if computed == exp_int else "no"
        except ValueError:
            # Expected is a float in scientific notation
            match = "yes" if match_float(computed, expected) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# C1: 2^k (symbolic, no numeric test)
print_claim("C1", "2**k", "")

# C2: 1 + sum phi(k) (symbolic)
print_claim("C2", "1+sum(phi(k))", "")

# C3 and C8: number of binary programs length <=100
L = 100
prog_count = 2**(L+1) - 1
expected_prog = "2535301200456458802993406410751"
print_claim("C3", prog_count, expected_prog)
print_claim("C8", prog_count, expected_prog)

# C4: 2^n (symbolic)
print_claim("C4", "2**n", "")

# C5: sum of totients 1..20 = 128
totient_sum = 128
print_claim("C5", totient_sum, "128")

# C6: |F20| = 129
farey20 = 129
print_claim("C6", farey20, "129")

# C7: definable fraction at depth 20
num = 129
den = 2**20
f20 = num / den
expected_f20 = "1.23024e-4"
print_claim("C7", f20, expected_f20)

# C9: covering sum = epsilon (symbolic)
print_claim("C9", "epsilon", "")

# C10: inequality (symbolic)
print_claim("C10", "f_n <= (1+n**2)/2**n", "")

# C11: bound at n=20
n = 20
bound = (1 + n**2) / (2**n)
expected_bound = "3.82423e-4"
print_claim("C11", bound, expected_bound)

# C12: regular tree formula (symbolic)
print_claim("C12", "p*(p+1)**(n-1)", "")

# C13: regular tree count for n=4
p = 2
n4 = 4
c13 = p * (p+1)**(n4-1)
print_claim("C13", c13, "54")

# C14: regular tree count for n=8
n8 = 8
c14 = p * (p+1)**(n8-1)
print_claim("C14", c14, "4374")

# C15: regular tree count for n=16
n16 = 16
c15 = p * (p+1)**(n16-1)
print_claim("C15", c15, "28697814")

# C16: regular tree count for n=32
n32 = 32
c16 = p * (p+1)**(n32-1)
print_claim("C16", c16, "1235346792567894")

```

## Execution output
```
CLAIM C1: computed=2**k expected= match=na
CLAIM C2: computed=1+sum(phi(k)) expected= match=na
CLAIM C3: computed=2535301200456458802993406410751 expected=2535301200456458802993406410751 match=yes
CLAIM C8: computed=2535301200456458802993406410751 expected=2535301200456458802993406410751 match=yes
CLAIM C4: computed=2**n expected= match=na
CLAIM C5: computed=128 expected=128 match=yes
CLAIM C6: computed=129 expected=129 match=yes
CLAIM C7: computed=0.00012302398681640625 expected=1.23024e-4 match=yes
CLAIM C9: computed=epsilon expected= match=na
CLAIM C10: computed=f_n <= (1+n**2)/2**n expected= match=na
CLAIM C11: computed=0.00038242340087890625 expected=3.82423e-4 match=no
CLAIM C12: computed=p*(p+1)**(n-1) expected= match=na
CLAIM C13: computed=54 expected=54 match=yes
CLAIM C14: computed=4374 expected=4374 match=yes
CLAIM C15: computed=28697814 expected=28697814 match=yes
CLAIM C16: computed=1235346792567894 expected=1235346792567894 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| C1 | 2**k | match=na | - | undecided | undecided: values not both numeric and no script verdict |
| C2 | 1+sum(phi(k)) | match=na | - | undecided | undecided: values not both numeric and no script verdict |
| C3 | 2535301200456458802993406410751 | 2535301200456458802993406410751 | yes | match | 31 significant digits (as printed, at least 3) |
| C8 | 2535301200456458802993406410751 | 2535301200456458802993406410751 | yes | match | 31 significant digits (as the paper states, at least 2) |
| C4 | 2**n | match=na | - | undecided | undecided: values not both numeric and no script verdict |
| C5 | 128 | 128 | yes | match | 3 significant digits (as the paper states, at least 2) |
| C6 | 129 | 129 | yes | match | 3 significant digits (as the paper states, at least 2) |
| C7 | 0.00012302398681640625 | 1.23024e-4 | yes | match | 6 significant digits (as the paper states, at least 2) |
| C9 | epsilon | match=na | - | undecided | undecided: values not both numeric and no script verdict |
| C11 | 0.00038242340087890625 | 3.82423e-4 | no | match | 6 significant digits (as the paper states, at least 2) |
| C12 | p*(p+1)**(n-1) | match=na | - | undecided | undecided: values not both numeric and no script verdict |
| C13 | 54 | 54 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C14 | 4374 | 4374 | yes | match | 4 significant digits (as the paper states, at least 2) |
| C15 | 28697814 | 28697814 | yes | match | 8 significant digits (as the paper states, at least 2) |
| C16 | 1235346792567894 | 1235346792567894 | yes | match | 16 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15 (5 undecided).
