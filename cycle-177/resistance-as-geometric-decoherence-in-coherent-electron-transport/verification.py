import math

# Constants
h = 6.626e-34          # J·s
e = 1.602e-19          # C
R0 = h / (2 * e**2)    # Ω
R0_kΩ = R0 / 1e3       # kΩ

# Input parameters
L_phi1 = 3e-6          # m
L_phi2 = 10.4e-6       # m
L = 10e-6              # m
L_phi_proj = 15e-6     # m

# Computations
S1 = R0 / L_phi1                       # Ω·m⁻¹
S1_per_um = R0 / 3.0                    # Ω·µm⁻¹ (L_phi1 = 3 µm)
S2 = R0 / L_phi2                       # Ω·m⁻¹
S2_per_um = R0 / 10.4                   # Ω·µm⁻¹ (L_phi2 = 10.4 µm)
LCI_opt = math.log(2 * math.pi)        # dimensionless
R1 = R0 * (L / L_phi1)                 # Ω
R2 = R0 * (L / L_phi2)                 # Ω
factor = R1 / R2                        # dimensionless
R_proj = R0 * (L / L_phi_proj)         # Ω
reduction = 1 - (R_proj / R1)          # dimensionless (fraction)

# Expected values (as plain numbers in the same units as computed)
expected = {
    "Q1": 12.9e3,          # Ω
    "Q2": 4.30e9,          # Ω·m⁻¹
    "Q3": 4.30e3,          # Ω·µm⁻¹
    "Q4": 1.24e9,          # Ω·m⁻¹
    "Q5": 1.24e3,          # Ω·µm⁻¹
    "Q6": 1.83,            # dimensionless
    "Q7": 43.0e3,          # Ω
    "Q8": 12.4e3,          # Ω
    "Q9": 3.5,             # dimensionless
    "Q10": 8.6e3,          # Ω
    "Q11": 80.0,           # percent
}

# Helper to round to the same number of significant figures as the expected value
def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Determine matches
matches = {}
matches["Q1"] = "yes" if round_sig(R0, 3) == round_sig(expected["Q1"], 3) else "no"
matches["Q2"] = "yes" if round_sig(S1, 3) == round_sig(expected["Q2"], 3) else "no"
matches["Q3"] = "yes" if round_sig(S1_per_um, 3) == round_sig(expected["Q3"], 3) else "no"
matches["Q4"] = "yes" if round_sig(S2, 3) == round_sig(expected["Q4"], 3) else "no"
matches["Q5"] = "yes" if round_sig(S2_per_um, 3) == round_sig(expected["Q5"], 3) else "no"
matches["Q6"] = "yes" if round_sig(LCI_opt, 3) == round_sig(expected["Q6"], 3) else "no"
matches["Q7"] = "yes" if round_sig(R1, 3) == round_sig(expected["Q7"], 3) else "no"
matches["Q8"] = "yes" if round_sig(R2, 3) == round_sig(expected["Q8"], 3) else "no"
matches["Q9"] = "yes" if round_sig(factor, 2) == round_sig(expected["Q9"], 2) else "no"
matches["Q10"] = "yes" if round_sig(R_proj, 3) == round_sig(expected["Q10"], 3) else "no"
matches["Q11"] = "yes" if round_sig(reduction*100, 2) == round_sig(expected["Q11"], 2) else "no"

# Print results
print(f"CLAIM Q1: computed={R0:.8g} expected={expected['Q1']:.8g} match={matches['Q1']}")
print(f"CLAIM Q2: computed={S1:.8g} expected={expected['Q2']:.8g} match={matches['Q2']}")
print(f"CLAIM Q3: computed={S1_per_um:.8g} expected={expected['Q3']:.8g} match={matches['Q3']}")
print(f"CLAIM Q4: computed={S2:.8g} expected={expected['Q4']:.8g} match={matches['Q4']}")
print(f"CLAIM Q5: computed={S2_per_um:.8g} expected={expected['Q5']:.8g} match={matches['Q5']}")
print(f"CLAIM Q6: computed={LCI_opt:.8g} expected={expected['Q6']:.8g} match={matches['Q6']}")
print(f"CLAIM Q7: computed={R1:.8g} expected={expected['Q7']:.8g} match={matches['Q7']}")
print(f"CLAIM Q8: computed={R2:.8g} expected={expected['Q8']:.8g} match={matches['Q8']}")
print(f"CLAIM Q9: computed={factor:.8g} expected={expected['Q9']:.8g} match={matches['Q9']}")
print(f"CLAIM Q10: computed={R_proj:.8g} expected={expected['Q10']:.8g} match={matches['Q10']}")
print(f"CLAIM Q11: computed={reduction*100:.8g} expected={expected['Q11']:.8g} match={matches['Q11']}")
print(f"VERIFICATION SUMMARY: 11 claims, {list(matches.values()).count('yes')} match, {list(matches.values()).count('no')} mismatch")
