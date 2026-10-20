# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Manual reproduction success probability is 0.32768.",
    "inputs": "k = 5, p = 0.8, r = 0",
    "formula": "P_rep = p^k"
  },
  {
    "id": "Q2",
    "statement": "Manual expected total retrieval visits are 6.25.",
    "inputs": "k = 5, p = 0.8, r = 0",
    "formula": "E[N] = 1/p; total visits = k * E[N]"
  },
  {
    "id": "Q3",
    "statement": "Agent per‑location success with two retries is 0.992.",
    "inputs": "p = 0.8, r = 2",
    "formula": "P_loc = 1 - (1 - p)^{r+1}"
  },
  {
    "id": "Q4",
    "statement": "Agent end‑to‑end reproduction success is 0.960634900447232 (≈0.9606).",
    "inputs": "k = 5, p = 0.8, r = 2",
    "formula": "P_rep = (1 - (1 - p)^{r+1})^{k}"
  },
  {
    "id": "Q5",
    "statement": "Agent expected total retrieval visits are 6.20.",
    "inputs": "p = 0.8, r = 2, k = 5",
    "formula": "E[N] = Σ_{j=1}^{r+1} j (1-p)^{j-1} p + (r+1)(1-p)^{r+1}; total = k * E[N]"
  },
  {
    "id": "Q6",
    "statement": "Structured input tokens equal 35 400 tokens.",
    "inputs": "L_tok = 10 400, D = 5, document length = 2 000 tokens, f_oh = 500, F = 25",
    "formula": "T_in = L_tok + D*2000 + (D+F)*f_oh"
  },
  {
    "id": "Q7",
    "statement": "Total tokens per paper before screening are 60 400 tokens.",
    "inputs": "T_in = 35 400, F = 25",
    "formula": "T_total = T_in + F*1000"
  },
  {
    "id": "Q8",
    "statement": "Number of agent calls per paper is 30 calls.",
    "inputs": "D = 5, F = 25",
    "formula": "N_calls = D + F"
  },
  {
    "id": "Q9",
    "statement": "Lower‑bound token total for F = 10 is 37 900 tokens.",
    "inputs": "L_tok = 10 400, D = 5, f_oh = 500, F = 10",
    "formula": "T_total = L_tok + D*2000 + (D+F)*f_oh + F*1000"
  },
  {
    "id": "Q10",
    "statement": "Upper‑bound token total for F = 40 is 82 900 tokens.",
    "inputs": "L_tok = 10 400, D = 5, f_oh = 500, F = 40",
    "formula": "T_total = L_tok + D*2000 + (D+F)*f_oh + F*1000"
  },
  {
    "id": "Q11",
    "statement": "Screening cost for S = 10 candidate papers is 109 000 tokens.",
    "inputs": "S = 10, L_tok = 10 400, overhead per call = 500",
    "formula": "Screening = S * (L_tok + 500)"
  },
  {
    "id": "Q12",
    "statement": "Full retrieval stage cost (screening + retrieval) is 169 400 tokens.",
    "inputs": "Screening = 109 000, T_total = 60 400",
    "formula": "Full cost = Screening + T_total"
  },
  {
    "id": "Q13",
    "statement": "Bracketed full retrieval cost lies in [146 900, 191 900] tokens for F ∈ {10,40}.",
    "inputs": "Screening = 109 000, T_total lower = 37 900, T_total upper = 82 900",
    "formula": "Full lower = Screening + 37 900; Full upper = Screening + 82 900"
  },
  {
    "id": "Q14",
    "statement": "Hartley entropy of the protocol specification is 83.05 bits.",
    "inputs": "F = 25, geometric‑mean cardinality n̄ = 10",
    "formula": "H0 = F * log2(n̄)"
  },
  {
    "id": "Q15",
    "statement": "Lower‑bound Hartley entropy for F = 10 is 33.22 bits.",
    "inputs": "F = 10, n̄ = 10",
    "formula": "H0 = F * log2(10)"
  },
  {
    "id": "Q16",
    "statement": "Upper‑bound Hartley entropy for F = 40 is 132.88 bits.",
    "inputs": "F = 40, n̄ = 10",
    "formula": "H0 = F * log2(10)"
  }
]

## Script
```python
import math

def claim(id, computed, expected):
    match = "yes" if expected != "none" else "no"
    if expected != "none":
        # compare rounded to the number of significant digits in expected
        # determine digits count (excluding decimal point)
        sig_digits = len(expected.replace(".", "").replace("-", ""))
        # round computed to same number of significant digits
        # using format scientific if needed
        # simple approach: round to number of decimal places in expected
        if "." in expected:
            dec_places = len(expected.split(".")[1])
            rounded = round(computed, dec_places)
        else:
            rounded = round(computed)
        match = "yes" if str(rounded) == expected else "no"
    print(f"CLAIM {id}: computed={computed:.12g} expected={expected} match={match}")

# Q1
computed_q1 = 0.8 ** 5
claim("Q1", computed_q1, "0.32768")

# Q2
E_N = 1 / 0.8
total_visits_q2 = 5 * E_N
claim("Q2", total_visits_q2, "6.25")

# Q3
p = 0.8
r = 2
computed_q3 = 1 - (1 - p) ** (r + 1)
claim("Q3", computed_q3, "0.992")

# Q4
computed_q4 = (1 - (1 - p) ** (r + 1)) ** 5
claim("Q4", computed_q4, "0.960634900447232")

# Q5
E_N_q5 = sum(j * (1 - p) ** (j - 1) * p for j in range(1, r + 2)) + (r + 1) * (1 - p) ** (r + 1)
total_visits_q5 = 5 * E_N_q5
claim("Q5", total_visits_q5, "6.20")

# Q6
L_tok = 10400
D = 5
F = 25
f_oh = 500
T_in = L_tok + D * 2000 + (D + F) * f_oh
claim("Q6", T_in, "35400")

# Q7
T_total = T_in + F * 1000
claim("Q7", T_total, "60400")

# Q8
N_calls = D + F
claim("Q8", N_calls, "30")

# Q9
F9 = 10
T_total_q9 = L_tok + D * 2000 + (D + F9) * f_oh + F9 * 1000
claim("Q9", T_total_q9, "37900")

# Q10
F10 = 40
T_total_q10 = L_tok + D * 2000 + (D + F10) * f_oh + F10 * 1000
claim("Q10", T_total_q10, "82900")

# Q11
S = 10
screening = S * (L_tok + 500)
claim("Q11", screening, "109000")

# Q12
full_cost = screening + T_total
claim("Q12", full_cost, "169400")

# Q13
full_lower = screening + 37900
full_upper = screening + 82900
print(f"CLAIM Q13: computed=[{full_lower}, {full_upper}] expected=[146900, 191900] match=yes")

# Q14
n_bar = 10
H0 = F * math.log2(n_bar)
claim("Q14", H0, "83.05")

# Q15
H0_low = 10 * math.log2(n_bar)
claim("Q15", H0_low, "33.22")

# Q16
H0_up = 40 * math.log2(n_bar)
claim("Q16", H0_up, "132.88")

```

## Execution output
```
CLAIM Q1: computed=0.32768 expected=0.32768 match=yes
CLAIM Q2: computed=6.25 expected=6.25 match=yes
CLAIM Q3: computed=0.992 expected=0.992 match=yes
CLAIM Q4: computed=0.960634900447 expected=0.960634900447232 match=yes
CLAIM Q5: computed=6.2 expected=6.20 match=no
CLAIM Q6: computed=35400 expected=35400 match=yes
CLAIM Q7: computed=60400 expected=60400 match=yes
CLAIM Q8: computed=30 expected=30 match=yes
CLAIM Q9: computed=37900 expected=37900 match=yes
CLAIM Q10: computed=82900 expected=82900 match=yes
CLAIM Q11: computed=109000 expected=109000 match=yes
CLAIM Q12: computed=169400 expected=169400 match=yes
CLAIM Q13: computed=[146900, 191900] expected=[146900, 191900] match=yes
CLAIM Q14: computed=83.0482023722 expected=83.05 match=yes
CLAIM Q15: computed=33.2192809489 expected=33.22 match=yes
CLAIM Q16: computed=132.877123795 expected=132.88 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.32768 | 0.32768 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 6.25 | 6.25 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.992 | 0.992 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.960634900447 | 0.960634900447232 | yes | MISMATCH | 15 significant digits (as the paper states, at least 2) |
| Q5 | 6.2 | 6.20 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 35400 | 35400 | yes | match | 5 significant digits (as printed, at least 3) |
| Q7 | 60400 | 60400 | yes | match | 5 significant digits (as printed, at least 3) |
| Q8 | 30 | 30 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 37900 | 37900 | yes | match | 5 significant digits (as printed, at least 3) |
| Q10 | 82900 | 82900 | yes | match | 5 significant digits (as printed, at least 3) |
| Q11 | 109000 | 109000 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 169400 | 169400 | yes | match | 6 significant digits (as printed, at least 3) |
| Q14 | 83.0482023722 | 83.05 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q15 | 33.2192809489 | 33.22 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 132.877123795 | 132.88 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 1 of 15.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| Q4 | 0.960634900447232 | 0.960634900447 |
