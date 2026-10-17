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
