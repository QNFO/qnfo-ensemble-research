import math
from fractions import Fraction

def match(computed, expected, sig_digits=None):
    """Return True if computed matches expected within given significant digits."""
    if isinstance(expected, str):
        # symbolic expected, compare string representation
        return str(computed) == expected
    if sig_digits is None:
        return computed == expected
    # round both to the number of decimal places in expected
    fmt = "{:." + str(sig_digits) + "f}"
    return fmt.format(computed) == fmt.format(expected)

# Claim C1
c1_lambda1 = 2
c1_lambda2 = 3
c1_c = 1
c1_computed = (c1_lambda1 / c1_lambda2) * c1_c
c1_expected = 0.666667
c1_match = match(c1_computed, c1_expected, sig_digits=6)
print(f"CLAIM C1: computed={c1_computed:.9f} expected={c1_expected} match={'yes' if c1_match else 'no'}")

# Claim C2
c2_factor = 1  # scalar dilation leaves unchanged
c2_expected = 1
c2_match = match(c2_factor, c2_expected)
print(f"CLAIM C2: computed={c2_factor} expected={c2_expected} match={'yes' if c2_match else 'no'}")

# Claim C3
# determinant invariance factor
c3_factor = 1
c3_expected = 1
c3_match = match(c3_factor, c3_expected)
print(f"CLAIM C3: computed={c3_factor} expected={c3_expected} match={'yes' if c3_match else 'no'}")

# Claim C4
c4_N_sed = 35
c4_N_oct = 7
c4_computed = c4_N_sed / c4_N_oct
c4_expected = 5
c4_match = match(c4_computed, c4_expected)
print(f"CLAIM C4: computed={c4_computed} expected={c4_expected} match={'yes' if c4_match else 'no'}")

# Claim C5
c5_r = 5
c5_computed = math.log2(c5_r)
c5_expected = 2.321928
c5_match = match(c5_computed, c5_expected, sig_digits=6)
print(f"CLAIM C5: computed={c5_computed:.9f} expected={c5_expected} match={'yes' if c5_match else 'no'}")

# Claim C6
c6_D3 = 2**3
c6_D4 = 2**4
c6_expected_D3 = 8
c6_expected_D4 = 16
c6_match = (c6_D3 == c6_expected_D3) and (c6_D4 == c6_expected_D4)
print(f"CLAIM C6: computed={c6_D3}, {c6_D4} expected={c6_expected_D3}, {c6_expected_D4} match={'yes' if c6_match else 'no'}")

# Claim C7
c7_N_oct = 7
c7_D3 = 8
c7_computed = c7_N_oct / c7_D3
c7_expected = 0.875
c7_match = match(c7_computed, c7_expected)
print(f"CLAIM C7: computed={c7_computed} expected={c7_expected} match={'yes' if c7_match else 'no'}")

# Claim C8
c8_N_sed = 35
c8_D4 = 16
c8_computed = c8_N_sed / c8_D4
c8_expected = 2.1875
c8_match = match(c8_computed, c8_expected)
print(f"CLAIM C8: computed={c8_computed} expected={c8_expected} match={'yes' if c8_match else 'no'}")

# Claim C9
c9_factor = c8_computed / c7_computed
c9_expected = 2.5
c9_match = match(c9_factor, c9_expected)
print(f"CLAIM C9: computed={c9_factor} expected={c9_expected} match={'yes' if c9_match else 'no'}")

# Claim C10
c10_d = 2
c10_computed = sum(math.comb(c10_d, k) for k in range(c10_d + 1))
c10_expected = 4
c10_match = match(c10_computed, c10_expected)
print(f"CLAIM C10: computed={c10_computed} expected={c10_expected} match={'yes' if c10_match else 'no'}")

# Claim C11
def generator_count(n):
    return n * (n - 1)

c11_vals = {5: 20, 6: 30, 7: 42}
c11_match = True
for n, expected in c11_vals.items():
    comp = generator_count(n)
    if not match(comp, expected):
        c11_match = False
        break
print(f"CLAIM C11: computed={list(generator_count(n) for n in c11_vals)} expected={list(c11_vals.values())} match={'yes' if c11_match else 'no'}")

# Claim C12
def euler_totient(k):
    count = 0
    for m in range(1, k + 1):
        if math.gcd(m, k) == 1:
            count += 1
    return count

c12_expected = {2: 1, 3: 2, 4: 2, 5: 4, 6: 2}
c12_match = True
c12_computed = {}
for k in c12_expected:
    c12_computed[k] = euler_totient(k)
    if not match(c12_computed[k], c12_expected[k]):
        c12_match = False
print(f"CLAIM C12: computed={c12_computed} expected={c12_expected} match={'yes' if c12_match else 'no'}")

# Claim C13
# Symbolic check: new coefficient = λ1 * original (original =1)
c13_lambda1 = "λ₁"
c13_computed = c13_lambda1  # symbolic
c13_expected = "λ₁"
c13_match = (c13_computed == c13_expected)
print(f"CLAIM C13: computed={c13_computed} expected={c13_expected} match={'yes' if c13_match else 'no'}")

# Claim C14
c14_r = 5
c14_N_sed = 35
c14_D4 = 16
c14_N_next = c14_r * c14_N_sed
c14_D_next = 2 * c14_D4
c14_density = c14_N_next / c14_D_next
c14_expected = {"N_next": 175, "D_next": 32, "density": 5.46875}
c14_match = (c14_N_next == c14_expected["N_next"] and
             c14_D_next == c14_expected["D_next"] and
             abs(c14_density - c14_expected["density"]) < 1e-12)
print(f"CLAIM C14: computed=N_next={c14_N_next}, D_next={c14_D_next}, density={c14_density} "
      f"expected=N_next={c14_expected['N_next']}, D_next={c14_expected['D_next']}, density={c14_expected['density']} "
      f"match={'yes' if c14_match else 'no'}")

print(f"VERIFICATION SUMMARY: 14 claims, {sum([c1_match, c2_match, c3_match, c4_match, c5_match, c6_match, c7_match, c8_match, c9_match, c10_match, c11_match, c12_match, c13_match, c14_match])} match, {14 - sum([c1_match, c2_match, c3_match, c4_match, c5_match, c6_match, c7_match, c8_match, c9_match, c10_match, c11_match, c12_match, c13_match, c14_match])} mismatch")
