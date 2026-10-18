import math

# Each claim is recomputed independently from its stated inputs and formula.
# "expected" carries exactly the digits the paper states, as a string, in the
# same unit as the computed value.

def sig_round(value, sig):
    """Round value to sig significant digits."""
    if value == 0:
        return 0.0
    from math import floor, log10
    exp = floor(log10(abs(value)))
    factor = 10 ** (sig - 1 - exp)
    return round(value * factor) / factor

claims = []

# Q1: lambda_bar_C = lambda_C/(2*pi) = 3.8611e-13
lam_C = 2.426e-12
two_pi = 2 * 3.1415926536
comp = lam_C / two_pi
expected = 3.8611e-13
claims.append(("Q1", comp, expected, 5))  # paper states 3.8611 (5 sig figs)

# Q2: r_e = alpha * lambda_bar_C = 2.818e-15
alpha = 7.2973525693e-3
lam_bar = 3.8611e-13
comp = alpha * lam_bar
expected = 2.818e-15
claims.append(("Q2", comp, expected, 4))  # paper states 2.818 (4 sig figs)

# Q3: delta_geom = alpha^2 = 5.325e-5
comp = alpha ** 2
expected = 5.325e-5
claims.append(("Q3", comp, expected, 4))  # paper states 5.325 (4 sig figs)

# Q4: alpha/pi = 2.32282e-3
pi_val = 3.1415926536
comp = alpha / pi_val
expected = 2.32282e-3
claims.append(("Q4", comp, expected, 6))  # paper states 2.32282 (6 sig figs)

# Q5: g = 2*(1 + alpha/pi + alpha^2) using paper's intermediate values
ap = 2.32282e-3
a2 = 5.325135e-5
comp = 2 * (1 + ap + a2)
expected = 2.004752
claims.append(("Q5", comp, expected, 7))  # paper states 2.004752 (7 sig figs)

# Q6: Delta g = 2.00475214 - 2.002319
comp = 2.00475214 - 2.002319
expected = 2.433e-3
claims.append(("Q6", comp, expected, 4))  # paper states 2.433 (4 sig figs)

# Q7: q = 1/lambda_C = 4.122e11
comp = 1.0 / lam_C
expected = 4.122e11
claims.append(("Q7", comp, expected, 4))  # paper states 4.122 (4 sig figs)

# Q8: ratio Delta g (fractional) 1.2e-3 / 1e-9 = 1.2e6
comp = 1.2e-3 / 1e-9
expected = 1.2e6
claims.append(("Q8", comp, expected, 2))  # paper states 1.2 (2 sig figs)

# Q9: ratio 5.4e-5 / 5.4e-6 = 10 (about 10)
comp = 5.4e-5 / 5.4e-6
expected = 10.0
claims.append(("Q9", comp, expected, 1))  # paper states "about 10"

n_match = 0
n_mismatch = 0
for cid, computed, exp, sig in claims:
    rounded = sig_round(computed, sig)
    # compare rounded computed to expected within tolerance set by stated precision
    if exp is None:
        match = "no"
    else:
        # tolerance: half unit in the last stated significant digit
        from math import floor, log10
        if exp != 0:
            exp_digits = sig
            exp_exp = floor(log10(abs(float(exp))))
            tol = 0.5 * 10 ** (exp_exp - exp_digits + 1)
        else:
            tol = 0.0
        match = "yes" if abs(computed - float(exp)) <= tol else "no"
    if match == "yes":
        n_match += 1
    else:
        n_mismatch += 1
    print(f"CLAIM {cid}: computed={computed:.10g} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {n_match} match, {n_mismatch} mismatch")
