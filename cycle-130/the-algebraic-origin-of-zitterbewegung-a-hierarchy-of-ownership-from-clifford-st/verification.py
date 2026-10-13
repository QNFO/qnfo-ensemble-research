import math

def sig(x, n=8):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

# Inputs (as stated in the paper)
c = 2.998e8          # m/s
m_e = 9.109e-31      # kg
hbar_J = 1.0546e-34  # J s
hbar_eV = 6.582e-16  # eV s
e = 1.602e-19        # J/eV
Delta = 0.1          # eV
a_Bohr = 5.29e-11    # m

# Q1: m_e c^2
q1 = m_e * c**2
# Q2: rest energy in MeV
q2 = (8.187e-14 / e) / 1e6
# Q3: omega_0 = 2 m_e c^2 / hbar
q3 = 2 * 8.187e-14 / hbar_J
# Q4: f_0 = omega_0 / (2 pi)
q4 = q3 / (2 * math.pi)
# Q5: T_0 = 1 / f_0
q5 = 1 / q4
# Q6: a_0 = hbar / (2 m_e c)
q6 = hbar_J / (2 * m_e * c)
# Q7: f = 2 Delta / (2 pi hbar_eV)
q7 = 2 * Delta / (2 * math.pi * hbar_eV)
# Q8: T = 1 / f
q8 = 1 / q7
# Q9: 1 / (2 pi hbar_eV)
q9 = 1 / (2 * math.pi * hbar_eV)
# Q10: hbar_J / hbar_eV
q10 = hbar_J / hbar_eV
# Q11: a_0 / a_Bohr
q11 = q6 / a_Bohr

claims = [
    ("Q1", q1, "8.187e-14"),
    ("Q2", q2, "0.5111"),
    ("Q3", q3, "1.5526e21"),
    ("Q4", q4, "2.471e20"),
    ("Q5", q5, "4.047e-21"),
    ("Q6", q6, "1.931e-13"),
    ("Q7", q7, "4.836e13"),
    ("Q8", q8, "2.068e-14"),
    ("Q9", q9, "2.418e14"),
    ("Q10", q10, "1.6023e-19"),
    ("Q11", q11, "3.65e-3"),
]

def match(computed, expected_str, stated_sig):
    exp_val = float(expected_str)
    comp_rounded = sig(computed, stated_sig)
    exp_rounded = sig(exp_val, stated_sig)
    return comp_rounded == exp_rounded

sig_digits = {"Q1": 4, "Q2": 4, "Q3": 5, "Q4": 4, "Q5": 4, "Q6": 4,
              "Q7": 4, "Q8": 4, "Q9": 4, "Q10": 5, "Q11": 3}

m_count = 0
for cid, comp, exp in claims:
    ok = match(comp, exp, sig_digits[cid])
    if ok:
        m_count += 1
    print(f"CLAIM {cid}: computed={comp:.8e} expected={exp} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {m_count} match, {len(claims) - m_count} mismatch")
