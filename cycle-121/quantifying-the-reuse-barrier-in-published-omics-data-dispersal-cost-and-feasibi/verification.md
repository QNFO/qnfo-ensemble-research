# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Manual reproduction success probability at k=5, p=0.8, r=0 is 0.32768",
    "inputs": "k=5, p=0.8",
    "formula": "P_rep = p^k = 0.8^5"
  },
  {
    "id": "Q2",
    "statement": "Agent reproduction success probability at k=5, p=0.8, r=2 is approximately 0.9606",
    "inputs": "k=5, p=0.8, r=2",
    "formula": "P_rep = (1-(1-p)^(r+1))^k = (1-0.2^3)^5 = 0.992^5"
  },
  {
    "id": "Q3",
    "statement": "Expected retrieval visits per artifact with r=0 is 1.25 and total is 6.25",
    "inputs": "p=0.8, k=5",
    "formula": "E[N] = 1/p = 1/0.8; total = k*E[N] = 5*1.25"
  },
  {
    "id": "Q4",
    "statement": "Expected retrieval visits per artifact with r=2 is 1.24 and total is 6.20",
    "inputs": "p=0.8, r=2, k=5",
    "formula": "E[N] = sum_{j=1}^{3} j(1-p)^(j-1)p + 3(1-p)^3; total = k*E[N]"
  },
  {
    "id": "Q5",
    "statement": "Total retrieval-stage input tokens per paper before screening is 60400",
    "inputs": "L_tok=10400, D=5, F=25, f_oh=500, context 1000 tokens per extraction call",
    "formula": "T_in = L_tok + D*2000 + (D+F)*f_oh; T_total = T_in + F*1000"
  },
  {
    "id": "Q6",
    "statement": "Number of agent calls per paper is 30",
    "inputs": "D=5, F=25",
    "formula": "N_calls = D + F"
  },
  {
    "id": "Q7",
    "statement": "Full retrieval stage with 10:1 screening is 169400 tokens per accepted paper",
    "inputs": "S=10, L_tok=10400, f_oh=500, T_total=60400",
    "formula": "T_retr = S*(L_tok+f_oh) + T_total = 10*10900 + 60400"
  },
  {
    "id": "Q8",
    "statement": "Hartley entropy of the protocol specification is 83.05 bits at F=25, n_bar=10",
    "inputs": "F=25, n_bar=10",
    "formula": "H0 = F*log2(n_bar) = 25*log2(10)"
  },
  {
    "id": "Q9",
    "statement": "Shannon entropy bound is at most 41.5 bits over 25 fields",
    "inputs": "p=0.5, n=10, F=25",
    "formula": "H <= F*(0.5*0 + 0.5*log2(10)) = 25*1.661"
  },
  {
    "id": "Q10",
    "statement": "Agent success factor over manual is approximately 2.9316",
    "inputs": "P_agent=0.960634900447232, P_manual=0.32768",
    "formula": "ratio = P_agent/P_manual"
  },
  {
    "id": "Q11",
    "statement": "Manual success at k=10 is 0.1073741824 and agent success at k=10 is approximately 0.9228",
    "inputs": "p=0.8, r=2, k=10",
    "formula": "0.8^10 and 0.992^10"
  },
  {
    "id": "Q12",
    "statement": "Per-location success with retries at p=0.6, r=2 is 0.936",
    "inputs": "p=0.6, r=2",
    "formula": "P_loc = 1-(1-p)^3 = 1-0.4^3"
  },
  {
    "id": "Q13",
    "statement": "Majority voting over m=3 sources raises no-screening retrieval total from 60400 to 110400 tokens",
    "inputs": "m=3, F=25, 1000 tokens per context read, T_total=60400",
    "formula": "T_ctx = m*F*1000 = 75000; new total = 60400 - 25000 + 75000"
  },
  {
    "id": "Q14",
    "statement": "Corpus of 10^4 accepted papers requires approximately 1.694e9 retrieval tokens at 10:1 screening",
    "inputs": "T_retr=169400, N=10^4",
    "formula": "N*T_retr = 10^4*169400"
  },
  {
    "id": "Q15",
    "statement": "Going from k=2 to k=5 cuts manual success by 48.8% relative",
    "inputs": "p=0.8, k=2, k=5",
    "formula": "1 - 0.8^5/0.8^2 = 1 - 0.512"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, n - 1 - math.floor(math.log10(abs(x))))

claims = []

# Q1: P_rep = 0.8^5
c1 = 0.8**5
claims.append(("Q1", c1, "0.32768"))

# Q2: (1-0.2^3)^5
c2 = (1 - 0.2**3)**5
claims.append(("Q2", c2, "0.9606"))

# Q3: E[N] = 1/0.8; total = 5*1.25
e3 = 1/0.8
t3 = 5*e3
claims.append(("Q3", t3, "6.25"))

# Q4: E[N] = sum_{j=1}^{3} j*0.2^(j-1)*0.8 + 3*0.2^3; total = 5*E[N]
e4 = sum(j*(0.2**(j-1))*0.8 for j in range(1,4)) + 3*(0.2**3)
t4 = 5*e4
claims.append(("Q4", t4, "6.20"))

# Q5: T_in = 10400 + 5*2000 + 30*500; T_total = T_in + 25*1000
t_in = 10400 + 5*2000 + (5+25)*500
t5 = t_in + 25*1000
claims.append(("Q5", t5, "60400"))

# Q6: N_calls = 5+25
c6 = 5 + 25
claims.append(("Q6", c6, "30"))

# Q7: T_retr = 10*(10400+500) + 60400
c7 = 10*(10400+500) + 60400
claims.append(("Q7", c7, "169400"))

# Q8: H0 = 25*log2(10)
c8 = 25*math.log2(10)
claims.append(("Q8", c8, "83.05"))

# Q9: H <= 25*(0.5*log2(10))
c9 = 25*(0.5*math.log2(10))
claims.append(("Q9", c9, "41.5"))

# Q10: ratio = 0.992^5 / 0.8^5
c10 = ((1-0.2**3)**5)/(0.8**5)
claims.append(("Q10", c10, "2.9316"))

# Q11: 0.8^10 and 0.992^10
c11a = 0.8**10
c11b = (1-0.2**3)**10
claims.append(("Q11", c11b, "0.9228"))

# Q12: 1-0.4^3
c12 = 1 - 0.4**3
claims.append(("Q12", c12, "0.936"))

# Q13: 60400 - 25000 + 3*25*1000
c13 = 60400 - 25000 + 3*25*1000
claims.append(("Q13", c13, "110400"))

# Q14: 10^4 * 169400
c14 = 10**4 * 169400
claims.append(("Q14", c14, "1694000000"))

# Q15: 1 - 0.8^5/0.8^2
c15 = 1 - (0.8**5)/(0.8**2)
claims.append(("Q15", c15, "0.488"))

mism = 0
for cid, comp, exp in claims:
    # match check: round computed to sig digits of expected
    digits = len(exp.replace(".", "").lstrip("0")) if "." in exp else len(exp)
    m = sig(comp, digits)
    match = ("yes" if abs(m - float(exp)) < 1e-12 * max(1, abs(float(exp))) else "no")
    if match == "no":
        mism += 1
    print(f"CLAIM {cid}: computed={comp:.8f} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {len(claims)-mism} match, {mism} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.32768000 expected=0.32768 match=yes
CLAIM Q2: computed=0.96063490 expected=0.9606 match=yes
CLAIM Q3: computed=6.25000000 expected=6.25 match=yes
CLAIM Q4: computed=6.20000000 expected=6.20 match=yes
CLAIM Q5: computed=60400.00000000 expected=60400 match=yes
CLAIM Q6: computed=30.00000000 expected=30 match=yes
CLAIM Q7: computed=169400.00000000 expected=169400 match=yes
CLAIM Q8: computed=83.04820237 expected=83.05 match=yes
CLAIM Q9: computed=41.52410119 expected=41.5 match=yes
CLAIM Q10: computed=2.93162506 expected=2.9316 match=yes
CLAIM Q11: computed=0.92281941 expected=0.9228 match=yes
CLAIM Q12: computed=0.93600000 expected=0.936 match=yes
CLAIM Q13: computed=110400.00000000 expected=110400 match=yes
CLAIM Q14: computed=1694000000.00000000 expected=1694000000 match=yes
CLAIM Q15: computed=0.48800000 expected=0.488 match=yes
VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.32768000 | 0.32768 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 0.96063490 | 0.9606 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 6.25000000 | 6.25 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 6.20000000 | 6.20 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 60400.00000000 | 60400 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 30.00000000 | 30 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 169400.00000000 | 169400 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 83.04820237 | 83.05 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 41.52410119 | 41.5 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 2.93162506 | 2.9316 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q11 | 0.92281941 | 0.9228 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 0.93600000 | 0.936 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 110400.00000000 | 110400 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q14 | 1694000000.00000000 | 1694000000 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q15 | 0.48800000 | 0.488 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15.
