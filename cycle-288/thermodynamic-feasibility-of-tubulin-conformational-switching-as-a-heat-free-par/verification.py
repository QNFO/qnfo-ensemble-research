import math

# Constants
kB = 1.380649e-23  # J·K^{-1}
T = 310.0          # K
ln2 = 0.693147
kBT = kB * T

# Expected values as strings
expected = {
    "Q1": "2.97e-21",
    "Q2": "5.0e-21",
    "Q3": "5.0e-19",
    "Q4": "1.168",
    "Q5": "116.8",
    "Q6": "1.69",
    "Q7": "168.5",
    "Q8": "2.138e-20",
    "Q9": "4.99",
    "Q10": "5.80464e-20",
    "Q11": "13.56",
    "Q12": "9.28",
    "Q13": "9.3e-05",
    "Q14": "1.3e-06",
    "Q15": "7.39335e-21",
    "Q16": "1.73",
}

# Computations
results = {}

# Q1: Landauer limit
E_L = kBT * ln2
results["Q1"] = f"{E_L:.2e}"

# Q2: Soft stiffness mechanical energy
k_eff_soft = 0.01
x = 1.0e-9
E_m_soft = 0.5 * k_eff_soft * x**2
results["Q2"] = f"{E_m_soft:.1e}"

# Q3: Stiff stiffness mechanical energy
k_eff_stiff = 1.0
E_m_stiff = 0.5 * k_eff_stiff * x**2
results["Q3"] = f"{E_m_stiff:.1e}"

# Q4: Soft energy in kBT
results["Q4"] = f"{E_m_soft / kBT:.3f}"

# Q5: Stiff energy in kBT
results["Q5"] = f"{E_m_stiff / kBT:.1f}"

# Q6: Soft energy / Landauer
results["Q6"] = f"{E_m_soft / E_L:.2f}"

# Q7: Stiff energy / Landauer
results["Q7"] = f"{E_m_stiff / E_L:.1f}"

# Q8: Dipole-field difference (Δp * E)
delta_p = 641 * 3.336e-30  # C·m
E_field = 1.0e7            # V·m^{-1}
delta_U = delta_p * E_field
results["Q8"] = f"{delta_U:.3e}"

# Q9: ΔU in kBT
results["Q9"] = f"{delta_U / kBT:.2f}"

# Q10: Dimer dipole-field energy
p_ab = 1740 * 3.336e-30
U_ab = p_ab * E_field
results["Q10"] = f"{U_ab:.5e}"

# Q11: Dimer energy in kBT
results["Q11"] = f"{U_ab / kBT:.2f}"

# Q12: Average gap in kBT
gap_avg = (4.99 + 13.56) / 2.0
results["Q12"] = f"{gap_avg:.2f}"

# Q13: Error probability for average gap
P_err_avg = math.exp(-gap_avg)
results["Q13"] = f"{P_err_avg:.1e}"

# Q14: Error probability for dimer gap
P_err_dim = math.exp(-13.56)
results["Q14"] = f"{P_err_dim:.1e}"

# Q15: Screened dipole-dipole interaction (unscreened value)
p = p_ab
epsilon0 = 8.854e-12
epsilon_r = 80.0
r = 8.0e-9
U_dd = p**2 / (4 * math.pi * epsilon0 * epsilon_r * r**3)
results["Q15"] = f"{U_dd:.5e}"

# Q16: U_dd in kBT
results["Q16"] = f"{U_dd / kBT:.2f}"

# Print verification lines
for qid in sorted(expected.keys()):
    computed = results[qid]
    exp = expected[qid]
    match = "yes" if computed == exp else "no"
    print(f"CLAIM {qid}: computed={computed} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if results[q]==expected[q])} match, {sum(1 for q in expected if results[q]!=expected[q])} mismatch")
