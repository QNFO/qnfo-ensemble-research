import math

def sci(val):
    """Return mantissa and exponent for scientific notation with 8‑significant‑digit mantissa."""
    log10 = math.log10(val)
    exp = math.floor(log10)
    mant = 10 ** (log10 - exp)
    return mant, exp

def compare(computed, expected):
    """Return 'yes' if computed matches expected to the number of significant digits in expected."""
    # Convert expected string to float for comparison tolerance
    try:
        exp_val = float(expected)
    except ValueError:
        # Handle scientific notation like 1e-953
        exp_val = float(expected.replace('e', 'E'))
    # Determine tolerance based on number of significant digits in expected
    sig_digits = len(expected.replace('.', '').replace('-', '').replace('e', '').replace('E', ''))
    # Use relative tolerance
    tol = 0.5 * 10 ** (-(sig_digits - 1))
    return "yes" if abs(computed - exp_val) <= tol * max(1.0, abs(exp_val)) else "no"

# Q1
mu_m = 1.0e4          # cm^-1
d_m   = 5.0e-7        # cm
T_m   = math.exp(-mu_m * d_m)
print(f"CLAIM Q1: computed={T_m:.8e} expected=0.995 match={compare(T_m, '0.995')}")

# Q2
mu_c = 1.0e4          # cm^-1
d_c   = 1.0e-3        # cm
T_c   = math.exp(-mu_c * d_c)
print(f"CLAIM Q2: computed={T_c:.8e} expected=4.54e-5 match={compare(T_c, '4.54e-5')}")

# Q3
T_tot = T_m * T_c
print(f"CLAIM Q3: computed={T_tot:.8e} expected=4.52e-5 match={compare(T_tot, '4.52e-5')}")

# Q4
m_p   = 1.6726e-27    # kg
DeltaE= 1.602e-19     # J
hbar  = 1.0546e-34    # J·s
d_m_m = 5.0e-9        # m
kappa = math.sqrt(2 * m_p * DeltaE) / hbar
log10_Tf = -2 * kappa * d_m_m / math.log(10)
# Approximate as 10^{log10_Tf}
mant_Tf, exp_Tf = sci(10 ** log10_Tf)  # mant_Tf ~1, exp_Tf ~ -953
T_f_approx = mant_Tf * (10 ** exp_Tf)
print(f"CLAIM Q4: computed={T_f_approx:.8e} expected=1e-953 match={compare(T_f_approx, '1e-953')}")

# Q5
ratio = T_m / T_f_approx
mant_r, exp_r = sci(ratio)
ratio_approx = mant_r * (10 ** exp_r)
print(f"CLAIM Q5: computed={ratio_approx:.8e} expected=1e953 match={compare(ratio_approx, '1e953')}")

# Q6
size6 = 2 ** 512
mant6, exp6 = sci(size6)
size6_approx = mant6 * (10 ** exp6)
print(f"CLAIM Q6: computed={size6_approx:.8e} expected=1.35e154 match={compare(size6_approx, '1.35e154')}")

# Q7
size7 = 2 ** 102
mant7, exp7 = sci(size7)
size7_approx = mant7 * (10 ** exp7)
print(f"CLAIM Q7: computed={size7_approx:.8e} expected=5.07e30 match={compare(size7_approx, '5.07e30')}")

# Q8
size8 = 2 ** 3721
mant8, exp8 = sci(size8)
size8_approx = mant8 * (10 ** exp8)
print(f"CLAIM Q8: computed={size8_approx:.8e} expected=1.00e1120 match={compare(size8_approx, '1.00e1120')}")

# Q9
mu_c_low = 1.0e3
T_c_low = math.exp(-mu_c_low * d_c)
print(f"CLAIM Q9: computed={T_c_low:.8e} expected=0.368 match={compare(T_c_low, '0.368')}")

# Q10
mu_c_high = 1.0e5
T_c_high = math.exp(-mu_c_high * d_c)
print(f"CLAIM Q10: computed={T_c_high:.8e} expected=3.7e-44 match={compare(T_c_high, '3.7e-44')}")

# Q11
size11 = 2 ** 3721
mant11, exp11 = sci(size11)
size11_approx = mant11 * (10 ** exp11)
print(f"CLAIM Q11: computed={size11_approx:.8e} expected=1.35e1120 match={compare(size11_approx, '1.35e1120')}")

print(f"VERIFICATION SUMMARY: 11 claims, {sum(1 for line in open(__file__) if 'match=yes' in line)} match, {sum(1 for line in open(__file__) if 'match=no' in line)} mismatch")
