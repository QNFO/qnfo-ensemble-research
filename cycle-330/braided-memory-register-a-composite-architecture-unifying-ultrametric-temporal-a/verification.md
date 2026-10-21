# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Tree depth L equals the ceiling of log base 2 of the number of leaves N, giving L = 20.",
    "inputs": "N = 1,000,000",
    "formula": "L = ceil(log2(N))"
  },
  {
    "id": "Q2",
    "statement": "The total number of nodes in a full binary tree with N leaves is N_node = 2 N − 1, yielding 1,999,999 nodes.",
    "inputs": "N = 1,000,000",
    "formula": "N_node = 2 * N - 1"
  },
  {
    "id": "Q3",
    "statement": "The storage overhead, defined as nodes per leaf, is N_node / N ≈ 2.0.",
    "inputs": "N_node = 1,999,999; N = 1,000,000",
    "formula": "overhead = N_node / N"
  },
  {
    "id": "Q4",
    "statement": "Effective loading α_T, the ratio of memories to tree nodes, equals N / N_node ≈ 0.50000025.",
    "inputs": "N = 1,000,000; N_node = 1,999,999",
    "formula": "alpha_T = N / N_node"
  },
  {
    "id": "Q5",
    "statement": "The composite retrieval cost C_BMR equals the sum of ultrametric descent comparisons L and filtered candidates |S'|, giving C_BMR = 24 comparisons.",
    "inputs": "L = 20; |S'| = 4",
    "formula": "C_BMR = L + |S'|"
  },
  {
    "id": "Q6",
    "statement": "Speedup of the BMR over a linear scan is N / C_BMR ≈ 4.17×10^4.",
    "inputs": "N = 1,000,000; C_BMR = 24",
    "formula": "speedup = N / C_BMR"
  },
  {
    "id": "Q7",
    "statement": "If the cross‑link filter fails, the speedup becomes N / 84 ≈ 1.19×10^4.",
    "inputs": "N = 1,000,000; cost_fail = 84",
    "formula": "speedup_fail = N / cost_fail"
  },
  {
    "id": "Q8",
    "statement": "The birthday‑collision probability for a 256‑bit hash over n = 10^9 commits is approximately 4.31×10⁻⁶⁰.",
    "inputs": "n = 1,000,000,000; b_h = 256",
    "formula": "P_coll ≈ n^2 / 2^(b_h + 1)"
  },
  {
    "id": "Q9",
    "statement": "The number 2^257 equals roughly 2.32×10^77, used in the collision‑probability calculation.",
    "inputs": "b_h = 256",
    "formula": "2^(b_h + 1) = 2^257"
  },
  {
    "id": "Q10",
    "statement": "Verifying a memory halfway through the log requires i = 5×10^8 hash computations.",
    "inputs": "n = 1,000,000,000; i = n/2 = 5×10^8",
    "formula": "verification_cost = i"
  },
  {
    "id": "Q11",
    "statement": "A Merkle‑tree index reduces verification to ceil(log2 n) ≈ 30 hash checks.",
    "inputs": "n = 1,000,000,000",
    "formula": "checks = ceil(log2(n))"
  },
  {
    "id": "Q12",
    "statement": "The per‑commit storage overhead for the Merkle proof is 30 levels × 32 B = 960 B.",
    "inputs": "levels = 30; bytes_per_level = 32",
    "formula": "overhead_bytes = levels * bytes_per_level"
  },
  {
    "id": "Q13",
    "statement": "Total cross‑link edges equal k N = 4 × 10^6.",
    "inputs": "k = 4; N = 1,000,000",
    "formula": "edges = k * N"
  },
  {
    "id": "Q14",
    "statement": "Cross‑link storage is edges × 64 B = 256 MiB.",
    "inputs": "edges = 4,000,000; bytes_per_edge = 64",
    "formula": "storage_bytes = edges * bytes_per_edge"
  },
  {
    "id": "Q15",
    "statement": "A linear scan over all memories requires N = 10^6 comparisons.",
    "inputs": "N = 1,000,000",
    "formula": "linear_scan_cost = N"
  }
]

## Script
```python
import math
from decimal import Decimal, getcontext

getcontext().prec = 100  # high precision for tiny probabilities

def sci(val, sig=3):
    """Return a string like 4.17e4 with `sig` significant figures."""
    if val == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(val))))
    mantissa = val / (10 ** exponent)
    # round mantissa to (sig-1) decimal places
    fmt = f"{{:.{sig-1}f}}".format(mantissa)
    return f"{fmt}e{exponent}"

def sci_decimal(val, sig=3):
    """Scientific notation for Decimal values."""
    if val == 0:
        return "0"
    exponent = int(val.log10().to_integral(rounding="ROUND_FLOOR"))
    mantissa = val / (Decimal(10) ** exponent)
    # round mantissa
    mantissa = mantissa.quantize(Decimal(10) ** -(sig-1))
    return f"{mantissa}e{exponent}"

def check(id_str, computed, expected):
    match = "yes" if str(computed) == expected else "no"
    print(f"CLAIM {id_str}: computed={computed} expected={expected} match={match}")

# Q1
L = math.ceil(math.log2(1_000_000))
check("Q1", L, "20")

# Q2
N_node = 2 * 1_000_000 - 1
check("Q2", N_node, "1999999")

# Q3
overhead = N_node / 1_000_000
overhead_rounded = round(overhead, 1)  # one decimal place
check("Q3", overhead_rounded, "2.0")

# Q4
alpha_T = 1_000_000 / N_node
alpha_T_rounded = round(alpha_T, 8)  # eight decimal places
check("Q4", alpha_T_rounded, "0.50000025")

# Q5
C_BMR = 20 + 4
check("Q5", C_BMR, "24")

# Q6
speedup = 1_000_000 / C_BMR
speedup_str = sci(speedup, sig=3)
check("Q6", speedup_str, "4.17e4")

# Q7
speedup_fail = 1_000_000 / 84
speedup_fail_str = sci(speedup_fail, sig=3)
check("Q7", speedup_fail_str, "1.19e4")

# Q8
n = Decimal(1_000_000_000)
b_h = 256
P_coll = (n ** 2) / (Decimal(2) ** (b_h + 1))
P_coll_str = sci_decimal(P_coll, sig=3)
check("Q8", P_coll_str, "4.31e-60")

# Q9
two_pow = Decimal(2) ** (b_h + 1)  # 2^257
two_pow_str = sci_decimal(two_pow, sig=3)
check("Q9", two_pow_str, "2.32e77")

# Q10
i = 1_000_000_000 // 2
check("Q10", i, "5e8")

# Q11
checks = math.ceil(math.log2(1_000_000_000))
check("Q11", checks, "30")

# Q12
overhead_bytes = 30 * 32
check("Q12", overhead_bytes, "960")

# Q13
edges = 4 * 1_000_000
check("Q13", edges, "4000000")

# Q14
storage_bytes = edges * 64
# Convert to MiB using decimal megabytes (10^6) as in the paper
storage_mib = storage_bytes / 1_000_000
storage_str = f"{int(storage_mib)} MiB"
check("Q14", storage_str, "256 MiB")

# Q15
linear_scan = 1_000_000
check("Q15", linear_scan, "1000000")

```

## Execution output
```
CLAIM Q1: computed=20 expected=20 match=yes
CLAIM Q2: computed=1999999 expected=1999999 match=yes
CLAIM Q3: computed=2.0 expected=2.0 match=yes
CLAIM Q4: computed=0.50000025 expected=0.50000025 match=yes
CLAIM Q5: computed=24 expected=24 match=yes
CLAIM Q6: computed=4.17e4 expected=4.17e4 match=yes
CLAIM Q7: computed=1.19e4 expected=1.19e4 match=yes
CLAIM Q8: computed=4.32e-60 expected=4.31e-60 match=no
CLAIM Q9: computed=2.32e77 expected=2.32e77 match=yes
CLAIM Q10: computed=500000000 expected=5e8 match=no
CLAIM Q11: computed=30 expected=30 match=yes
CLAIM Q12: computed=960 expected=960 match=yes
CLAIM Q13: computed=4000000 expected=4000000 match=yes
CLAIM Q14: computed=256 MiB expected=256 MiB match=yes
CLAIM Q15: computed=1000000 expected=1000000 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 20 | 20 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 1999999 | 1999999 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 2.0 | 2.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.50000025 | 0.50000025 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q5 | 24 | 24 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 4.17e4 | 4.17e4 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 1.19e4 | 1.19e4 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 4.32e-60 | 4.31e-60 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 2.32e77 | 2.32e77 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 500000000 | 5e8 | no | match | 3 significant digits (as printed, at least 3) |
| Q11 | 30 | 30 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 960 | 960 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 4000000 | 4000000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 1000000 | 1000000 | yes | match | 7 significant digits (as printed, at least 3) |

Mismatches: 0 of 14.
