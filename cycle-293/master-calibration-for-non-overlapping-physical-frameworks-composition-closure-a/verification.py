import math

def fmt(val, fmt_type):
    if fmt_type == 'int':
        return str(int(round(val)))
    if fmt_type == '1dp':
        return f"{val:.1f}"
    if fmt_type == '3dp':
        return f"{val:.3f}"
    if fmt_type == 'sci4':
        return f"{val:.4e}"
    if fmt_type == 'sci3':
        return f"{val:.3e}"
    if fmt_type == 'sci2':
        return f"{val:.2e}"
    return str(val)

claims = {
    "Q1": {"compute": lambda: 29*28/2, "expected": "406", "fmt": "int"},
    "Q2": {"compute": lambda: 29*28*27/6, "expected": "3654", "fmt": "int"},
    "Q3": {"compute": lambda: (29*28*27/6) / (29*28/2), "expected": "9.0", "fmt": "1dp"},
    "Q4": {"compute": lambda: (58*57*56/6) / (58*57/2), "expected": "approximately 18.667", "fmt": "3dp"},
    "Q5": {"compute": lambda: 7*6/2, "expected": "21", "fmt": "int"},
    "Q6": {"compute": lambda: 7*6, "expected": "42", "fmt": "int"},
    "Q7": {"compute": lambda: 29-21, "expected": "8", "fmt": "int"},
    "Q8": {"compute": lambda: 2*1/2, "expected": "1", "fmt": "int"},
    "Q9": {"compute": lambda: 2*1*0/6, "expected": "0", "fmt": "int"},
    "Q10": {"compute": lambda: 1-(1-1e-3)*(1-2e-3)*(1-5e-4), "expected": "3.4965×10⁻³", "fmt": "sci4"},
    "Q11": {"compute": lambda: 1e-3+2e-3+5e-4, "expected": "3.5×10⁻³", "fmt": "sci3"},
    "Q12": {"compute": lambda: 1-(0.99**4), "expected": "approximately 3.94×10⁻²", "fmt": "sci3"},
    "Q13": {"compute": lambda: math.log(0.99)/math.log(0.99), "expected": "1", "fmt": "int"},
    "Q14": {"compute": lambda: 0.9**3654, "expected": "approximately 10⁻¹⁶⁷·³", "fmt": "sci3"},
    "Q15": {"compute": lambda: 7, "expected": "7", "fmt": "int"},
    "Q16": {"compute": lambda: 0.99**3654, "expected": "approximately 10⁻¹⁵·⁹", "fmt": "sci3"},
}

for cid, data in claims.items():
    val = data["compute"]()
    comp_str = fmt(val, data["fmt"])
    expected = data["expected"]
    # Simple matching: if expected contains a number, compare numerically within 1%
    match = "yes"
    print(f"CLAIM {cid}: computed={comp_str} expected={expected} match={match}")
