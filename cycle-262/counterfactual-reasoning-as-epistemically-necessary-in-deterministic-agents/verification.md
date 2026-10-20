# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "In the symmetric binary case, the expected utility of action u0 is 5 units.",
    "inputs": "P(h0|o)=0.5, P(h1|o)=0.5, U(u0,h0)=10, U(u0,h1)=0",
    "formula": "E[U|u0,o] = P(h0|o)*U(u0,h0) + P(h1|o)*U(u0,h1) = 0.5*10 + 0.5*0"
  },
  {
    "id": "Q2",
    "statement": "In the symmetric binary case, the expected utility of action u1 is 5 units.",
    "inputs": "P(h0|o)=0.5, P(h1|o)=0.5, U(u1,h0)=0, U(u1,h1)=10",
    "formula": "E[U|u1,o] = P(h0|o)*U(u1,h0) + P(h1|o)*U(u1,h1) = 0.5*0 + 0.5*10"
  },
  {
    "id": "Q3",
    "statement": "The collapsed agent that always selects u0 has an expected payoff of 5 units in the symmetric case.",
    "inputs": "P(h0)=0.5, P(h1)=0.5, U(u0,h0)=10, U(u0,h1)=0",
    "formula": "E[U_collapsed] = 0.5*10 + 0.5*0"
  },
  {
    "id": "Q4",
    "statement": "In the asymmetric case, the expected utility of action u0 is 6.2 units.",
    "inputs": "P(h0|o)=0.7, P(h1|o)=0.3, U(u0,h0)=8, U(u0,h1)=2",
    "formula": "E[U|u0,o] = 0.7*8 + 0.3*2 = 5.6 + 0.6"
  },
  {
    "id": "Q5",
    "statement": "In the asymmetric case, the expected utility of action u1 is 3.4 units.",
    "inputs": "P(h0|o)=0.7, P(h1|o)=0.3, U(u1,h0)=1, U(u1,h1)=9",
    "formula": "E[U|u1,o] = 0.7*1 + 0.3*9 = 0.7 + 2.7"
  },
  {
    "id": "Q6",
    "statement": "The epistemic-possibility-aware agent's expected utility advantage over the collapsed agent in the asymmetric case is 2.8 units (reported again in Section 4.3 as a 2.8-point reduction).",
    "inputs": "E[U|u0,o]=6.2, E[U|u1,o]=3.4",
    "formula": "Delta_EU = 6.2 - 3.4"
  },
  {
    "id": "Q7",
    "statement": "Storing a belief distribution over a hidden state space of size 10 requires about 80 bytes (10 floating-point numbers, at 8 bytes per number implied by the paper's figure).",
    "inputs": "|H|=10, bytes_per_float=8 (implied by the paper's 10 numbers = 80 bytes)",
    "formula": "bytes = |H| * bytes_per_float = 10 * 8"
  },
  {
    "id": "Q8",
    "statement": "Computing expected utilities for all actions per decision step entails 50 multiplications and additions.",
    "inputs": "|U|=5, |H|=10",
    "formula": "operations = |U| * |H| = 5 * 10"
  }
]

## Script
```python
import math
from fractions import Fraction


def parse_dec(s):
    """Parse a decimal string exactly into a Fraction."""
    return Fraction(s)


def round_sig(x, n):
    """Round a Fraction to n significant digits (half-up), returning a Fraction."""
    if x == 0:
        return Fraction(0)
    ax = abs(x)
    e = int(math.floor(math.log10(float(ax))))
    while ax < Fraction(10) ** e:
        e -= 1
    while ax >= Fraction(10) ** (e + 1):
        e += 1
    unit = Fraction(10) ** (e - n + 1)
    q = x / unit
    if q >= 0:
        fl = q.numerator // q.denominator
        if q - fl >= Fraction(1, 2):
            fl += 1
        rq = Fraction(fl)
    else:
        aq = -q
        fl = aq.numerator // aq.denominator
        if aq - fl >= Fraction(1, 2):
            fl += 1
        rq = Fraction(-fl)
    return rq * unit


def sig_digits(s):
    """Count the significant digits carried by a plain decimal string."""
    t = s.strip().lstrip("+-")
    for ch in ("e", "E"):
        if ch in t:
            t = t.split(ch)[0]
    t = t.replace(".", "").lstrip("0")
    return len(t) if t else 1


def fmt(x, min_sig=8):
    """Format a Fraction exactly with at least min_sig significant digits."""
    if x == 0:
        return "0." + "0" * (min_sig - 1)
    neg = x < 0
    ax = -x if neg else x
    e = int(math.floor(math.log10(float(ax))))
    while ax < Fraction(10) ** e:
        e -= 1
    while ax >= Fraction(10) ** (e + 1):
        e += 1
    decimals = max(min_sig - 1 - e, 0)
    while True:
        scaled = ax * Fraction(10) ** decimals
        n = scaled.numerator // scaled.denominator
        if Fraction(n) != scaled:
            decimals += 1
            continue
        if decimals > 0:
            ip = n // 10 ** decimals
            fp = n % 10 ** decimals
            s = str(ip) + "." + format(fp, "0" + str(decimals) + "d")
        else:
            s = str(n)
        if sig_digits(s) >= min_sig:
            return ("-" if neg else "") + s
        decimals += 1


def check(cid, computed, expected_str):
    """Recompute-then-adjudicate: round computed to the paper's significant
    digits and compare against the expected value parsed from its string."""
    n = sig_digits(expected_str)
    rounded = round_sig(computed, n)
    expected = Fraction(expected_str)
    match = "yes" if rounded == expected else "no"
    print("CLAIM {}: computed={} expected={} match={}".format(
        cid, fmt(computed), expected_str, match))
    return match


def main():
    results = []

    # ---- Q1: symmetric case, expected utility of action u0 ----
    # Inputs: P(h0|o)=0.5, P(h1|o)=0.5, U(u0,h0)=10, U(u0,h1)=0
    # Formula: E[U|u0,o] = P(h0|o)*U(u0,h0) + P(h1|o)*U(u0,h1)
    p_h0 = parse_dec("0.5")
    p_h1 = parse_dec("0.5")
    eu0_sym = p_h0 * 10 + p_h1 * 0
    results.append(check("Q1", eu0_sym, "5"))

    # ---- Q2: symmetric case, expected utility of action u1 ----
    # Inputs: P(h0|o)=0.5, P(h1|o)=0.5, U(u1,h0)=0, U(u1,h1)=10
    # Formula: E[U|u1,o] = P(h0|o)*U(u1,h0) + P(h1|o)*U(u1,h1)
    eu1_sym = p_h0 * 0 + p_h1 * 10
    results.append(check("Q2", eu1_sym, "5"))

    # ---- Q3: collapsed agent that always selects u0, symmetric case ----
    # Inputs: P(h0)=0.5, P(h1)=0.5, U(u0,h0)=10, U(u0,h1)=0
    # Formula: E[U_collapsed] = 0.5*10 + 0.5*0
    eu_collapsed = p_h0 * 10 + p_h1 * 0
    results.append(check("Q3", eu_collapsed, "5"))

    # ---- Q4: asymmetric case, expected utility of action u0 ----
    # Inputs: P(h0|o)=0.7, P(h1|o)=0.3, U(u0,h0)=8, U(u0,h1)=2
    # Formula: E[U|u0,o] = 0.7*8 + 0.3*2 = 5.6 + 0.6
    p0 = parse_dec("0.7")
    p1 = parse_dec("0.3")
    eu0_asym = p0 * 8 + p1 * 2
    results.append(check("Q4", eu0_asym, "6.2"))

    # ---- Q5: asymmetric case, expected utility of action u1 ----
    # Inputs: P(h0|o)=0.7, P(h1|o)=0.3, U(u1,h0)=1, U(u1,h1)=9
    # Formula: E[U|u1,o] = 0.7*1 + 0.3*9 = 0.7 + 2.7
    eu1_asym = p0 * 1 + p1 * 9
    results.append(check("Q5", eu1_asym, "3.4"))

    # ---- Q6: epistemic-possibility advantage in the asymmetric case ----
    # Inputs: E[U|u0,o] and E[U|u1,o], each derived above from the stated
    # payoffs and probabilities (0.7/0.3 prior, payoffs {8,2} and {1,9})
    # Formula: Delta_EU = E[U|u0,o] - E[U|u1,o]
    delta = eu0_asym - eu1_asym
    results.append(check("Q6", delta, "2.8"))

    # ---- Q7: belief-storage footprint ----
    # Inputs: |H|=10 hidden states, 8 bytes per floating-point number
    # (implied by the paper's figure of 10 numbers = 80 bytes)
    # Formula: bytes = |H| * bytes_per_float = 10 * 8
    hidden_states = 10
    bytes_per_float = 8
    storage_bytes = hidden_states * bytes_per_float
    results.append(check("Q7", Fraction(storage_bytes), "80"))

    # ---- Q8: expected-utility computation cost per decision step ----
    # Inputs: |U|=5 actions, |H|=10 hidden states
    # Formula: operations = |U| * |H| = 5 * 10
    actions = 5
    ops = actions * hidden_states
    results.append(check("Q8", Fraction(ops), "50"))

    n_total = len(results)
    n_match = sum(1 for r in results if r == "yes")
    n_mismatch = n_total - n_match
    print("VERIFICATION SUMMARY: {} claims, {} match, {} mismatch".format(
        n_total, n_match, n_mismatch))


if __name__ == "__main__":
    main()

```

## Execution output
```
CLAIM Q1: computed=5.0000000 expected=5 match=yes
CLAIM Q2: computed=5.0000000 expected=5 match=yes
CLAIM Q3: computed=5.0000000 expected=5 match=yes
CLAIM Q4: computed=6.2000000 expected=6.2 match=yes
CLAIM Q5: computed=3.4000000 expected=3.4 match=yes
CLAIM Q6: computed=2.8000000 expected=2.8 match=yes
CLAIM Q7: computed=80.000000 expected=80 match=yes
CLAIM Q8: computed=50.000000 expected=50 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 5.0000000 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 5.0000000 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 5.0000000 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 6.2000000 | 6.2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 3.4000000 | 3.4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 2.8000000 | 2.8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 80.000000 | 80 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 50.000000 | 50 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 8.
