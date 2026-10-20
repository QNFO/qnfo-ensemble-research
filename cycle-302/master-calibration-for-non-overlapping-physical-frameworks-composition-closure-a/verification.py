import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def compare(computed, expected_str):
    # parse expected to float
    expected = float(expected_str.replace('e', 'E'))
    # determine number of significant digits in expected
    # remove sign, decimal point, exponent part
    s = expected_str.lower()
    if 'e' in s:
        mantissa = s.split('e')[0].replace('.', '').lstrip('0')
    else:
        mantissa = s.replace('.', '').lstrip('0')
    sig = len(mantissa) if mantissa else 1
    comp_rounded = round_sig(computed, sig)
    exp_rounded = round_sig(expected, sig)
    match = 'yes' if comp_rounded == exp_rounded else 'no'
    return f"{comp_rounded:.{sig}g}", f"{expected_str}", match

# Q1
N = 29
C1 = N * (N - 1) / 2
c, e, m = compare(C1, "406")
print(f"CLAIM Q1: computed={c} expected={e} match={m}")

# Q2
C2 = N * (N - 1) * (N - 2) / 6
c, e, m = compare(C2, "3654")
print(f"CLAIM Q2: computed={c} expected={e} match={m}")

# Q3
ratio = 3654 / 406
c, e, m = compare(ratio, "9.0")
print(f"CLAIM Q3: computed={c} expected={e} match={m}")

# Q4
N2 = 58
maps = N2 * (N2 - 1) / 2
constraints = N2 * (N2 - 1) * (N2 - 2) / 6
ratio2 = constraints / maps
c, e, m = compare(ratio2, "18.667")
print(f"CLAIM Q4: computed={c} expected={e} match={m}")

# Q5
n = 7
pairs = n * (n - 1) / 2
c, e, m = compare(pairs, "21")
print(f"CLAIM Q5: computed={c} expected={e} match={m}")

# Q6
directed = n * (n - 1)
c, e, m = compare(directed, "42")
print(f"CLAIM Q6: computed={c} expected={e} match={m}")

# Q7
unassigned = 29 - 21
c, e, m = compare(unassigned, "8")
print(f"CLAIM Q7: computed={c} expected={e} match={m}")

# Q8
m_val = 2
unordered_pair = m_val * (m_val - 1) / 2
unordered_triple = m_val * (m_val - 1) * (m_val - 2) / 6
# combine as "1,0"
c_pair = round_sig(unordered_pair, 1)
c_triple = round_sig(unordered_triple, 1)
c = f"{c_pair:.0f},{c_triple:.0f}"
e = "1,0"
match = "yes" if c == e else "no"
print(f"CLAIM Q8: computed={c} expected={e} match={match}")

# Q9
e12 = 1e-3
e23 = 2e-3
e31 = 5e-4
delta = 1 - (1 - e12) * (1 - e23) * (1 - e31)
c, e, m = compare(delta, "3.4965e-3")
print(f"CLAIM Q9: computed={c} expected={e} match={m}")

# Q10
additive = e12 + e23 + e31
c, e, m = compare(additive, "3.5e-3")
print(f"CLAIM Q10: computed={c} expected={e} match={m}")

# Q11
k = 4
eps_min = 1e-2
delta2 = 1 - (1 - eps_min) ** k
c, e, m = compare(delta2, "3.94e-2")
print(f"CLAIM Q11: computed={c} expected={e} match={m}")

# Q12
tau = 1e-2
k_bound = math.log(1 - tau) / math.log(1 - eps_min)
c, e, m = compare(k_bound, "1")
print(f"CLAIM Q12: computed={c} expected={e} match={m}")

# Q13
E_max = 1e3  # MeV equivalent to 1 TeV
E_min = 500   # MeV equivalent to 500 GeV
factor13 = E_max / E_min
c, e, m = compare(factor13, "2")
print(f"CLAIM Q13: computed={c} expected={e} match={m}")

# Q14
E_max2 = 1.5e3
E_min2 = 0.5e3
factor14 = E_max2 / E_min2
c, e, m = compare(factor14, "3")
print(f"CLAIM Q14: computed={c} expected={e} match={m}")

# Q15
total_schisms = 29
domains = 7
mean = total_schisms / domains
c, e, m = compare(mean, "4.14")
print(f"CLAIM Q15: computed={c} expected={e} match={m}")

# Q16
eps = 1e-2
mediated = 1 - (1 - eps) ** 2
c, e, m = compare(mediated, "0.0199")
print(f"CLAIM Q16: computed={c} expected={e} match={m}")

print(f"VERIFICATION SUMMARY: {16} claims, {sum(1 for line in [c, e, m] if m=='yes')} match, {sum(1 for line in [c, e, m] if m=='no')} mismatch")
