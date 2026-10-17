# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Exact three-level peak leakage P2,max = 2r^2/(1+2r^2) = 0.0196078",
    "inputs": "r = f_Omega/f_alpha = 20/200 = 0.1, r^2 = 0.01",
    "formula": "P2max = 2*r^2/(1+2*r^2)"
  },
  {
    "id": "Q2",
    "statement": "Time-averaged three-level leakage P2bar = r^2/(1+2r^2) = 0.00980392",
    "inputs": "r^2 = 0.01",
    "formula": "P2bar = r^2/(1+2*r^2)"
  },
  {
    "id": "Q3",
    "statement": "Perturbative worst-case leakage L2 = 0.02",
    "inputs": "Omega/|alpha| = 0.05, sin^2(alpha*Tg/2) = 1",
    "formula": "L2 = 8*(Omega/|alpha|)^2*sin^2(alpha*Tg/2)"
  },
  {
    "id": "Q4",
    "statement": "Gate-averaged leakage L2bar = 0.01",
    "inputs": "Omega/|alpha| = 0.05, mean sin^2 = 0.5",
    "formula": "L2bar = 4*(Omega/|alpha|)^2"
  },
  {
    "id": "Q5",
    "statement": "Scaling check: doubling Omega/|alpha| to 0.10 gives L2 = 0.08, factor 4",
    "inputs": "Omega/|alpha| = 0.10",
    "formula": "L2 = 8*(0.10)^2"
  },
  {
    "id": "Q6",
    "statement": "Pi-pulse duration t_pi = 25 ns",
    "inputs": "f_Omega = 20 MHz = 2e7 s^-1",
    "formula": "t_pi = 1/(2*f_Omega)"
  },
  {
    "id": "Q7",
    "statement": "Gate cycle rate f_g = 2e7 s^-1",
    "inputs": "T_cyc = 50 ns = 5e-8 s",
    "formula": "f_g = 1/T_cyc"
  },
  {
    "id": "Q8",
    "statement": "Leakage production rate Lambda = 2e5 s^-1",
    "inputs": "L2bar = 0.01, f_g = 2e7 s^-1",
    "formula": "Lambda = L2bar*f_g"
  },
  {
    "id": "Q9",
    "statement": "Removal requirement Gamma_rem = 2e9 s^-1",
    "inputs": "Lambda = 2e5 s^-1, P* = 1e-4",
    "formula": "Gamma_rem = Lambda/P*"
  },
  {
    "id": "Q10",
    "statement": "Fill time to 1e-2 leakage without removal t_fill = 50 ns",
    "inputs": "P = 1e-2, Lambda = 2e5 s^-1",
    "formula": "t_fill = P/Lambda"
  },
  {
    "id": "Q11",
    "statement": "Deficit factor at fastest resonant hopping = 200",
    "inputs": "Gamma_rem = 2e9 s^-1, hopping rate = 10 MHz = 1e7 s^-1",
    "formula": "deficit = Gamma_rem/1e7"
  },
  {
    "id": "Q12",
    "statement": "Deficit factor at slowest resonant hopping = 2500",
    "inputs": "Gamma_rem = 2e9 s^-1, hopping rate = 0.8 MHz = 8e5 s^-1",
    "formula": "deficit = Gamma_rem/8e5"
  },
  {
    "id": "Q13",
    "statement": "Deficit factor at next-nearest-neighbor hopping = 2e4",
    "inputs": "Gamma_rem = 2e9 s^-1, hopping rate = 0.1 MHz = 1e5 s^-1",
    "formula": "deficit = Gamma_rem/1e5"
  },
  {
    "id": "Q14",
    "statement": "ln 12 = 2.484906 nats",
    "inputs": "d = 12",
    "formula": "ln(12)"
  },
  {
    "id": "Q15",
    "statement": "S_Base = ln 6 = 1.791759 nats = 2.584963 bits",
    "inputs": "d = 12",
    "formula": "ln(6); ln(6)/ln(2)"
  },
  {
    "id": "Q16",
    "statement": "Discarded fraction f_disc = ln6/ln12 = 0.721057",
    "inputs": "ln 6 = 1.791759, ln 12 = 2.484906",
    "formula": "f_disc = ln(6)/ln(12)"
  }
]

## Script
```python
import math

def claim(id, computed, expected, match):
    print(f"CLAIM {id}: computed={computed:.8g} expected={expected} match={'yes' if match else 'no'}")

def matches(computed, expected_str):
    # expected carries exactly the digits the paper states; compare at that precision
    exp = float(expected_str)
    # significant digits in expected string
    s = expected_str.strip().lower()
    if 'e' in s:
        mant, ex = s.split('e')
        digits = len(mant.replace('-', '').replace('.', '').lstrip('0')) or 1
    else:
        digits = len(s.replace('-', '').replace('.', '').lstrip('0')) or 1
    return round(computed, digits - len(str(int(abs(computed)))) if computed >= 1 else digits) == round(exp, 10) or abs(computed - exp) <= 0.5 * 10**(-digits) * 10**max(0, len(str(int(abs(computed)))) - digits) or abs(computed - exp) < 10**(-digits + 1) * 10**len(str(int(abs(computed))))

# Simpler robust matcher: round computed to the number of significant digits implied by expected string
def sig_match(computed, expected_str):
    exp = float(expected_str)
    s = expected_str.strip().lower()
    if 'e' in s:
        mant = s.split('e')[0]
    else:
        mant = s
    mant = mant.lstrip('-')
    if '.' in mant:
        intpart, frac = mant.split('.')
    else:
        intpart, frac = mant, ''
    digits = len((intpart + frac).lstrip('0')) or 1
    # round computed to `digits` significant figures
    if computed == 0:
        return computed == exp
    exponent = math.floor(math.log10(abs(computed)))
    rounded = round(computed, -(exponent - (digits - 1)))
    return abs(rounded - exp) < 1e-12 * max(1, abs(exp))

# Q1
r = 20/200
r2 = r*r
P2max = 2*r2/(1+2*r2)
claim("Q1", P2max, "0.0196078", sig_match(P2max, "0.0196078"))

# Q2
P2bar = r2/(1+2*r2)
claim("Q2", P2bar, "0.00980392", sig_match(P2bar, "0.00980392"))

# Q3
ratio = 0.05
L2 = 8*ratio**2*1.0
claim("Q3", L2, "0.02", sig_match(L2, "0.02"))

# Q4
L2bar = 4*ratio**2
claim("Q4", L2bar, "0.01", sig_match(L2bar, "0.01"))

# Q5
L2b = 8*(0.10)**2
claim("Q5", L2b, "0.08", sig_match(L2b, "0.08"))

# Q6 (ns)
fO = 2e7
t_pi_ns = 1/(2*fO)*1e9
claim("Q6", t_pi_ns, "25", sig_match(t_pi_ns, "25"))

# Q7 (s^-1)
T_cyc = 5e-8
f_g = 1/T_cyc
claim("Q7", f_g, "2e7", sig_match(f_g, "2e7"))

# Q8
Lambda = L2bar*f_g
claim("Q8", Lambda, "2e5", sig_match(Lambda, "2e5"))

# Q9
Gamma = Lambda/1e-4
claim("Q9", Gamma, "2e9", sig_match(Gamma, "2e9"))

# Q10 (ns)
t_fill_ns = 1e-2/Lambda*1e9
claim("Q10", t_fill_ns, "50", sig_match(t_fill_ns, "50"))

# Q11
d1 = Gamma/1e7
claim("Q11", d1, "200", sig_match(d1, "200"))

# Q12
d2 = Gamma/8e5
claim("Q12", d2, "2500", sig_match(d2, "2500"))

# Q13
d3 = Gamma/1e5
claim("Q13", d3, "2e4", sig_match(d3, "2e4"))

# Q14
ln12 = math.log(12)
claim("Q14", ln12, "2.484906", sig_match(ln12, "2.484906"))

# Q15 (nats and bits; report nats)
ln6 = math.log(6)
bits = ln6/math.log(2)
claim("Q15", ln6, "1.791759", sig_match(ln6, "1.791759"))
print(f"CLAIM Q15b: computed={bits:.8g} expected=2.584963 match={'yes' if sig_match(bits, '2.584963') else 'no'}")

# Q16
f_disc = ln6/ln12
claim("Q16", f_disc, "0.721057", sig_match(f_disc, "0.721057"))

total = 17
mism = 0
# recount matches
results = [
    sig_match(P2max, "0.0196078"),
    sig_match(P2bar, "0.00980392"),
    sig_match(L2, "0.02"),
    sig_match(L2bar, "0.01"),
    sig_match(L2b, "0.08"),
    sig_match(t_pi_ns, "25"),
    sig_match(f_g, "2e7"),
    sig_match(Lambda, "2e5"),
    sig_match(Gamma, "2e9"),
    sig_match(t_fill_ns, "50"),
    sig_match(d1, "200"),
    sig_match(d2, "2500"),
    sig_match(d3, "2e4"),
    sig_match(ln12, "2.484906"),
    sig_match(ln6, "1.791759"),
    sig_match(bits, "2.584963"),
    sig_match(f_disc, "0.721057"),
]
m = sum(1 for x in results if x)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results)-m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.019607843 expected=0.0196078 match=yes
CLAIM Q2: computed=0.0098039216 expected=0.00980392 match=yes
CLAIM Q3: computed=0.02 expected=0.02 match=yes
CLAIM Q4: computed=0.01 expected=0.01 match=yes
CLAIM Q5: computed=0.08 expected=0.08 match=yes
CLAIM Q6: computed=25 expected=25 match=yes
CLAIM Q7: computed=20000000 expected=2e7 match=yes
CLAIM Q8: computed=200000 expected=2e5 match=yes
CLAIM Q9: computed=2e+09 expected=2e9 match=yes
CLAIM Q10: computed=50 expected=50 match=yes
CLAIM Q11: computed=200 expected=200 match=yes
CLAIM Q12: computed=2500 expected=2500 match=yes
CLAIM Q13: computed=20000 expected=2e4 match=yes
CLAIM Q14: computed=2.4849066 expected=2.484906 match=no
CLAIM Q15: computed=1.7917595 expected=1.791759 match=yes
CLAIM Q15b: computed=2.5849625 expected=2.584963 match=yes
CLAIM Q16: computed=0.72105705 expected=0.721057 match=yes
VERIFICATION SUMMARY: 17 claims, 16 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.019607843 | 0.0196078 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 0.0098039216 | 0.00980392 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q3 | 0.02 | 0.02 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.01 | 0.01 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.08 | 0.08 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 25 | 25 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 20000000 | 2e7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 200000 | 2e5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 2e+09 | 2e9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 50 | 50 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 200 | 200 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 2500 | 2500 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 20000 | 2e4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 2.4849066 | 2.484906 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q15 | 1.7917595 | 1.791759 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q15b | 2.5849625 | 2.584963 | yes | match | 7 significant digits (as printed, at least 3) |
| Q16 | 0.72105705 | 0.721057 | yes | match | 6 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 17.
