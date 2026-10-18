# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The ultrametric distance for an hour-level difference is $d_{\\text{mix}} = 24^{-1} = 0.0416667$.",
    "inputs": "b_hour = 24",
    "formula": "1 / b_hour"
  },
  {
    "id": "Q2",
    "statement": "The ultrametric distance for a day-level difference is $d_{\\text{mix}} = 30^{-1} = 0.0333333$.",
    "inputs": "b_day = 30",
    "formula": "1 / b_day"
  },
  {
    "id": "Q3",
    "statement": "The ultrametric distance for a month-level difference is $d_{\\text{mix}} = 12^{-1} = 0.0833333$.",
    "inputs": "b_month = 12",
    "formula": "1 / b_month"
  },
  {
    "id": "Q4",
    "statement": "For timestamps t1, t2, t3, the maximum of distances d(t1,t2)=0.0416667 and d(t1,t3)=0.0333333 is 0.0416667, satisfying the strong triangle inequality.",
    "inputs": "d12 = 0.0416667, d13 = 0.0333333",
    "formula": "max(d12, d13)"
  },
  {
    "id": "Q5",
    "statement": "With a 100 MHz clock and three sequential field checks, the projected worst‑case latency is ≤ 3 × (1/100 MHz) = 30 ns.",
    "inputs": "frequency = 100 MHz, checks = 3",
    "formula": "checks * (1 / frequency) converted to nanoseconds"
  }
]

## Script
```python
import math

def fmt(x):
    # format with at least 8 significant digits, removing trailing zeros beyond decimal point
    s = f"{x:.9g}"
    # ensure at least 8 significant digits by adding zeros if needed
    if 'e' in s or '.' in s:
        # count significant digits (exclude leading zeros and decimal point)
        sig = len(s.replace('.', '').replace('-', '').replace('+', '').lstrip('0'))
        if sig < 8:
            # add zeros after decimal
            if '.' not in s:
                s += '.'
            s += '0' * (8 - sig)
    return s

# Q1
b_hour = 24
computed_q1 = 1 / b_hour
expected_q1 = "0.0416667"
match_q1 = fmt(computed_q1) == expected_q1
print(f"CLAIM Q1: computed={fmt(computed_q1)} expected={expected_q1} match={'yes' if match_q1 else 'no'}")

# Q2
b_day = 30
computed_q2 = 1 / b_day
expected_q2 = "0.0333333"
match_q2 = fmt(computed_q2) == expected_q2
print(f"CLAIM Q2: computed={fmt(computed_q2)} expected={expected_q2} match={'yes' if match_q2 else 'no'}")

# Q3
b_month = 12
computed_q3 = 1 / b_month
expected_q3 = "0.0833333"
match_q3 = fmt(computed_q3) == expected_q3
print(f"CLAIM Q3: computed={fmt(computed_q3)} expected={expected_q3} match={'yes' if match_q3 else 'no'}")

# Q4
d12 = 0.0416667
d13 = 0.0333333
computed_q4 = max(d12, d13)
expected_q4 = "0.0416667"
match_q4 = fmt(computed_q4) == expected_q4
print(f"CLAIM Q4: computed={fmt(computed_q4)} expected={expected_q4} match={'yes' if match_q4 else 'no'}")

# Q5
frequency_hz = 100e6  # 100 MHz
checks = 3
latency_seconds = checks / frequency_hz
latency_ns = latency_seconds * 1e9  # convert to nanoseconds
computed_q5 = latency_ns
expected_q5 = "30 ns"
# format computed as integer nanoseconds with at least 8 sig digits
computed_q5_str = fmt(computed_q5) + " ns"
match_q5 = computed_q5_str.startswith("30")  # accept any 30.xxx ns as match
print(f"CLAIM Q5: computed={computed_q5_str} expected={expected_q5} match={'yes' if match_q5 else 'no'}")

print(f"VERIFICATION SUMMARY: 5 claims, {sum([match_q1, match_q2, match_q3, match_q4, match_q5])} match, {5 - sum([match_q1, match_q2, match_q3, match_q4, match_q5])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.0416666667 expected=0.0416667 match=no
CLAIM Q2: computed=0.0333333333 expected=0.0333333 match=no
CLAIM Q3: computed=0.0833333333 expected=0.0833333 match=no
CLAIM Q4: computed=0.041666700 expected=0.0416667 match=no
CLAIM Q5: computed=30 ns expected=30 ns match=yes
VERIFICATION SUMMARY: 5 claims, 1 match, 4 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.0416666667 | 0.0416667 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 0.0333333333 | 0.0333333 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q3 | 0.0833333333 | 0.0833333 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q4 | 0.041666700 | 0.0416667 | no | match | 6 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 4.
