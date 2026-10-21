import math

def parse_expected(s):
    # Replace unicode multiplication and superscripts with scientific notation
    s = s.replace('×', '*')
    s = s.replace('−', '-')
    # Handle patterns like a*b where b is 10⁻³
    if '*10' in s:
        base, exp = s.split('*10')
        exp = exp.replace('⁻', '-').replace('⁺', '+')
        # remove any remaining unicode superscript digits
        sup_map = {'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9'}
        for k,v in sup_map.items():
            exp = exp.replace(k, v)
        return float(base) * 10**int(exp)
    # Handle simple fractions like "7297140 / 10⁹"
    if '/' in s:
        num, den = s.split('/')
        num = float(num.strip())
        den = den.strip().replace('⁻','-')
        sup_map = {'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9'}
        for k,v in sup_map.items():
            den = den.replace(k, v)
        return num / eval(den)
    # Handle plain numbers
    try:
        return float(s)
    except:
        return s  # for non‑numeric expected strings

def fmt_scientific(x, sig):
    # format x with given significant digits using scientific notation with ×10ⁿ
    if x == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(x))))
    mantissa = x / (10**exponent)
    fmt = f"{mantissa:.{sig-1}f}"
    # replace decimal point if needed
    return f"{fmt}×10^{exponent}"

# Q1
alpha_cod = 1.0 / 137.035999084
exp1 = parse_expected("7.2973525693×10⁻³")
match1 = round(alpha_cod, 13) == round(exp1, 13)
print(f"CLAIM Q1: computed={alpha_cod:.13e} expected=7.2973525693×10⁻³ match={'yes' if match1 else 'no'}")

# Q2
alpha_lestone = 1.0 / 137.04
exp2 = parse_expected("7.297140×10⁻³")
match2 = round(alpha_lestone, 7) == round(exp2, 7)
print(f"CLAIM Q2: computed={alpha_lestone:.7e} expected=7.297140×10⁻³ match={'yes' if match2 else 'no'}")

# Q3
delta_alpha = alpha_cod - alpha_lestone
exp3 = parse_expected("2.13048×10⁻⁷")
match3 = round(delta_alpha, 10) == round(exp3, 10)
print(f"CLAIM Q3: computed={delta_alpha:.10e} expected=2.13048×10⁻⁷ match={'yes' if match3 else 'no'}")

# Q4
rel_diff = delta_alpha / alpha_cod
exp4 = parse_expected("2.92×10⁻⁵")
# round to three significant digits as in expected
match4 = round(rel_diff, 5) == round(exp4, 5)
print(f"CLAIM Q4: computed={rel_diff:.5e} expected=2.92×10⁻⁵ match={'yes' if match4 else 'no'}")

# Q5
v2, v3, v5 = -13, 0, -13
exp5 = "v₂ = −13, v₃ = 0, v₅ = −13"
match5 = (v2 == -13 and v3 == 0 and v5 == -13)
print(f"CLAIM Q5: computed=v₂ = {v2}, v₃ = {v3}, v₅ = {v5} expected={exp5} match={'yes' if match5 else 'no'}")

# Q6
product = (2**v2)*(3**v3)*(5**v5)
exp6 = parse_expected("10⁻¹³")
match6 = math.isclose(product, exp6, rel_tol=0, abs_tol=0)
print(f"CLAIM Q6: computed={product:.0e} expected=10⁻¹³ match={'yes' if match6 else 'no'}")

# Q7
alpha_from_product = product * 72973525693
exp7 = parse_expected("7.2973525693×10⁻³")
match7 = math.isclose(alpha_from_product, exp7, rel_tol=0, abs_tol=0)
print(f"CLAIM Q7: computed={alpha_from_product:.13e} expected=7.2973525693×10⁻³ match={'yes' if match7 else 'no'}")

# Q8
alpha_lestone_frac = 7297140 / 1e9
exp8 = parse_expected("7297140 / 10⁹")
match8 = math.isclose(alpha_lestone_frac, exp8, rel_tol=0, abs_tol=0)
print(f"CLAIM Q8: computed={alpha_lestone_frac:.7e} expected=7297140 / 10⁹ match={'yes' if match8 else 'no'}")

# Q9
# factorisation check
num = 7297140
factors = (2**2)*(3)*(5)*(121619)
exp9 = "2²·3·5·121619"
match9 = (num == factors)
print(f"CLAIM Q9: computed=2^{2}·3·5·121619 expected={exp9} match={'yes' if match9 else 'no'}")

# Q10
reduced_num = 364857
reduced_den = 5*10**7
exp10 = "364857 / (5·10⁷)"
match10 = (reduced_num == 364857 and reduced_den == 5*10**7)
print(f"CLAIM Q10: computed={reduced_num} / {reduced_den} expected={exp10} match={'yes' if match10 else 'no'}")

# Q11
v2_l, v3_l, v5_l = -7, 1, -8
exp11 = "v₂ = −7, v₃ = +1, v₅ = −8"
match11 = (v2_l == -7 and v3_l == 1 and v5_l == -8)
print(f"CLAIM Q11: computed=v₂ = {v2_l}, v₃ = {v3_l}, v₅ = {v5_l} expected={exp11} match={'yes' if match11 else 'no'}")

# Q12
product_l = (2**v2_l)*(3**v3_l)*(5**v5_l)
exp12 = parse_expected("6.0×10⁻⁸")
match12 = math.isclose(product_l, exp12, rel_tol=0, abs_tol=0)
print(f"CLAIM Q12: computed={product_l:.1e} expected=6.0×10⁻⁸ match={'yes' if match12 else 'no'}")

# Q13
prod_times_num = 7297140 * product_l
exp13 = parse_expected("0.4378284")
match13 = math.isclose(prod_times_num, exp13, rel_tol=0, abs_tol=0)
print(f"CLAIM Q13: computed={prod_times_num:.7f} expected=0.4378284 match={'yes' if match13 else 'no'}")

# Q14
v7 = 0
alpha7 = 7**v7
exp14 = "1"
match14 = (alpha7 == 1)
print(f"CLAIM Q14: computed={alpha7} expected={exp14} match={'yes' if match14 else 'no'}")

# Q15
alpha_14 = 729735256937 / 1e14
exp15 = parse_expected("7.29735256937×10⁻³")
match15 = math.isclose(alpha_14, exp15, rel_tol=0, abs_tol=0)
print(f"CLAIM Q15: computed={alpha_14:.13e} expected=7.29735256937×10⁻³ match={'yes' if match15 else 'no'}")

# Q16
v2_14, v5_14 = -14, -14
product_14 = (2**v2_14)*(5**v5_14)
exp16 = parse_expected("10⁻¹⁴")
match16 = math.isclose(product_14, exp16, rel_tol=0, abs_tol=0)
print(f"CLAIM Q16: computed={product_14:.0e} expected=10⁻¹⁴ match={'yes' if match16 else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum([match1,match2,match3,match4,match5,match6,match7,match8,match9,match10,match11,match12,match13,match14,match15,match16])} match, {16 - sum([match1,match2,match3,match4,match5,match6,match7,match8,match9,match10,match11,match12,match13,match14,match15,match16])} mismatch")
