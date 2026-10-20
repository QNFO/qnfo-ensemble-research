import math

def fmt(val, exp):
    """Format val to match the precision of exp string."""
    if 'e' in exp:
        # scientific notation like 1.6952e12
        mant, exp_part = exp.split('e')
        digits = len(mant.split('.')[1]) if '.' in mant else 0
        fmt_str = f"{{:.{digits}e}}"
        return fmt_str.format(val)
    elif '.' in exp:
        # decimal notation
        digits = len(exp.split('.')[1])
        fmt_str = f"{{:.{digits}f}}"
        return fmt_str.format(val)
    else:
        # integer
        return str(int(round(val)))

# constants
c = 2.9979e10  # cm s^-1
Δ = 100.0      # cm^-1
V = 30.0       # cm^-1
k_star = V**2 / Δ
ω_star = 2 * math.pi * c * k_star
τ_T = 1e12 / ω_star  # ps

τ_e = 1e-9      # s
γ_rec = 1 / τ_e * 1e-12  # convert to ps^-1
κ = 1.0         # ps^-1
η = κ / (κ + γ_rec)

τ_B_fast = 0.1  # ps
τ_B_slow = 1.0  # ps
R_fast = τ_B_fast / τ_T
R_slow = τ_B_slow / τ_T

# additional cases
def case(Vc, Δc):
    k = Vc**2 / Δc
    ω = 2 * math.pi * c * k
    τ = 1e12 / ω
    return k, ω, τ

k20, ω20, τ20 = case(20.0, 100.0)
k50, ω50, τ50 = case(50.0, 150.0)

claims = [
    ("Q1", Δ, "100"),
    ("Q2", k_star, "9"),
    ("Q3", ω_star, "1.6952e12"),
    ("Q4", τ_T, "0.5899"),
    ("Q5", τ_T, "0.5899"),
    ("Q6", γ_rec, "0.001"),
    ("Q7", η, "0.999001"),
    ("Q8", R_fast, "0.1695"),
    ("Q9", R_slow, "1.6953"),
    ("Q10", k20, "4.0"),
    ("Q11", ω20, "7.5345e11"),
    ("Q12", τ20, "1.3272"),
    ("Q13", τ_B_fast/τ20, "0.0753"),
    ("Q14", τ_B_slow/τ20, "0.7535"),
    ("Q15", k50, "16.6667"),
    ("Q16", ω50, "3.1394e12"),
]

for cid, comp, exp in claims:
    comp_fmt = fmt(comp, exp)
    match = "yes" if comp_fmt == exp else "no"
    print(f"CLAIM {cid}: computed={comp_fmt} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if fmt(c,e)==e)} match, {sum(1 for _,c,e in claims if fmt(c,e)!=e)} mismatch")
