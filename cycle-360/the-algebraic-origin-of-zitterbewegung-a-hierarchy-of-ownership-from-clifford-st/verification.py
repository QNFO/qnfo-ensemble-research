import math

# Helper to round a number to n significant figures and format as scientific string
def fmt_sig(x, n):
    if x == 0:
        return f"{0:.{n-1}e}"
    exponent = int(math.floor(math.log10(abs(x))))
    factor = 10**(n-1-exponent)
    rounded = round(x * factor) / factor
    return f"{rounded:.{n-1}e}"

# Expected values (as strings) and their significant-figure counts
expected = {
    "Q1": ("1.6023e-19", 5),
    "Q2": ("8.187e-14", 4),
    "Q3": ("5.111e5", 4),
    "Q4": ("1.5526e21", 5),
    "Q5": ("2.471e20", 4),
    "Q6": ("1.553e21", 4),
    "Q7": ("1.931e-13", 4),
    "Q8": ("4.836e13", 4),
    "Q9": ("2.0678e-14", 5),
    "Q10": ("2.418e14", 4),
}

# Physical constants
c = 2.998e8            # m/s
m_e = 9.109e-31        # kg
hbar_Js = 1.0546e-34   # J·s
hbar_eVs = 6.582e-16   # eV·s
pi = math.pi

# Computations
results = {}

# Q1: ratio of ħ values
results["Q1"] = hbar_Js / hbar_eVs

# Q2: electron rest energy (J)
results["Q2"] = m_e * c**2

# Q3: rest energy in eV
results["Q3"] = results["Q2"] / 1.602e-19

# Q4: rest‑frame angular frequency (rad/s)
results["Q4"] = 2 * results["Q2"] / hbar_Js

# Q5: ordinary frequency (Hz)
results["Q5"] = results["Q4"] / (2 * pi)

# Q6: angular frequency using eV units
E_meV = 0.5111e6      # eV
results["Q6"] = 2 * E_meV / hbar_eVs

# Q7: position‑amplitude scale (m)
results["Q7"] = hbar_Js / (2 * m_e * c)

# Q8: ZB frequency for Δ=0.1 eV
Delta = 0.1            # eV
results["Q8"] = (2 * Delta) / (2 * pi * hbar_eVs)

# Q9: period corresponding to Q8
results["Q9"] = 1 / results["Q8"]

# Q10: universal conversion factor Hz/eV
h = 2 * pi * hbar_eVs
results["Q10"] = 1 / h

# Verification and reporting
match_count = 0
total = len(expected)

for qid, (exp_str, sig) in expected.items():
    comp = results[qid]
    comp_str = fmt_sig(comp, sig)
    match = "yes" if comp_str == exp_str else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")
