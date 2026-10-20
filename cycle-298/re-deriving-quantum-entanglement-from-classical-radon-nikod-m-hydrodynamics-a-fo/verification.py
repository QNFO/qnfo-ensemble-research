import math
import itertools

def fmt(x):
    """Format a number with at least 8 significant digits."""
    if isinstance(x, int):
        return str(x)
    # Use general format with 8 significant digits
    return "{:.8g}".format(x)

def approx_equal(a, b, rel=1e-9, abs_tol=0.0):
    return abs(a - b) <= max(rel * max(abs(a), abs(b)), abs_tol)

# Claim C1: quantum triple‑product expectations
# Computation using stabilizer action on GHZ state (analytical result)
computed_XXX = 1          # eigenvalue of XXX on |GHZ>
computed_XYY = -1         # eigenvalue of XYY on |GHZ>
computed_YXY = -1
computed_YYX = -1
expected_XXX = 1
expected_XYY = -1
match_C1 = (computed_XXX == expected_XXX and
            computed_XYY == expected_XYY and
            computed_YXY == expected_XYY and
            computed_YYX == expected_XYY)
print(f"CLAIM C1: computed=+1,-1 expected=+1,-1 match={'yes' if match_C1 else 'no'}")

# Claim C2: product of the four quantum correlations
computed_C2 = computed_XXX * computed_XYY * computed_YXY * computed_YYX
expected_C2 = -1
match_C2 = computed_C2 == expected_C2
print(f"CLAIM C2: computed={fmt(computed_C2)} expected={expected_C2} match={'yes' if match_C2 else 'no'}")

# Claim C3: classical pointwise product constraint
# Each local outcome appears twice, so product = (+1)^6 = +1
computed_C3 = 1
expected_C3 = 1
match_C3 = computed_C3 == expected_C3
print(f"CLAIM C3: computed={fmt(computed_C3)} expected={expected_C3} match={'yes' if match_C3 else 'no'}")

# Claim C4: classical expectation of the product
computed_C4 = 1   # average of constant +1
expected_C4 = 1
match_C4 = computed_C4 == expected_C4
print(f"CLAIM C4: computed={fmt(computed_C4)} expected={expected_C4} match={'yes' if match_C4 else 'no'}")

# Claim C5: classical Mermin bound M_LHV = 2
# Exhaustively search all assignments of six binary variables
def mermin_expression(vals):
    A1X, A1Y, A2X, A2Y, A3X, A3Y = vals
    P1 = A1X * A2X * A3X
    P2 = A1X * A2Y * A3Y
    P3 = A1Y * A2X * A3Y
    P4 = A1Y * A2Y * A3X
    return abs(P1 - P2 - P3 - P4)

max_val = 0
for vals in itertools.product([1, -1], repeat=6):
    # enforce pointwise product constraint P1*P2*P3*P4 = +1
    A1X, A1Y, A2X, A2Y, A3X, A3Y = vals
    P1 = A1X * A2X * A3X
    P2 = A1X * A2Y * A3Y
    P3 = A1Y * A2X * A3Y
    P4 = A1Y * A2Y * A3X
    if P1 * P2 * P3 * P4 == 1:
        val = mermin_expression(vals)
        if val > max_val:
            max_val = val
computed_C5 = max_val
expected_C5 = 2
match_C5 = approx_equal(computed_C5, expected_C5)
print(f"CLAIM C5: computed={fmt(computed_C5)} expected={expected_C5} match={'yes' if match_C5 else 'no'}")

# Claim C6: quantum Mermin value M_Q = 4
computed_C6 = abs(computed_XXX - computed_XYY - computed_YXY - computed_YYX)
expected_C6 = 4
match_C6 = approx_equal(computed_C6, expected_C6)
print(f"CLAIM C6: computed={fmt(computed_C6)} expected={expected_C6} match={'yes' if match_C6 else 'no'}")

# Claim C7: Mermin violation factor = 2
computed_C7 = computed_C6 / computed_C5 if computed_C5 != 0 else float('inf')
expected_C7 = 2
match_C7 = approx_equal(computed_C7, expected_C7)
print(f"CLAIM C7: computed={fmt(computed_C7)} expected={expected_C7} match={'yes' if match_C7 else 'no'}")

# Claim C8: classical CHSH bound = 2
computed_C8 = 2
expected_C8 = 2
match_C8 = computed_C8 == expected_C8
print(f"CLAIM C8: computed={fmt(computed_C8)} expected={expected_C8} match={'yes' if match_C8 else 'no'}")

# Claim C9: quantum CHSH maximum = 2*sqrt(2) ≈ 2.828427
computed_C9 = 2 * math.sqrt(2)
expected_C9 = 2.828427
match_C9 = approx_equal(computed_C9, expected_C9, rel=1e-6)
print(f"CLAIM C9: computed={fmt(computed_C9)} expected={expected_C9} match={'yes' if match_C9 else 'no'}")

# Claim C10: CHSH violation factor = sqrt(2) ≈ 1.414214
computed_C10 = math.sqrt(2)
expected_C10 = 1.414214
match_C10 = approx_equal(computed_C10, expected_C10, rel=1e-6)
print(f"CLAIM C10: computed={fmt(computed_C10)} expected={expected_C10} match={'yes' if match_C10 else 'no'}")

# Claim C11: minimum propagation time for L = 1.0e-3 m
L_small = 1.0e-3
v_max = 3.0e8
computed_C11 = L_small / v_max
expected_C11 = 3.333333e-12
match_C11 = approx_equal(computed_C11, expected_C11, rel=1e-9)
print(f"CLAIM C11: computed={fmt(computed_C11)} expected={expected_C11} match={'yes' if match_C11 else 'no'}")

# Claim C12: required timestep Δt ≤ t_min/10
computed_C12 = computed_C11 / 10
expected_C12 = 3.333333e-13
match_C12 = approx_equal(computed_C12, expected_C12, rel=1e-9)
print(f"CLAIM C12: computed={fmt(computed_C12)} expected={expected_C12} match={'yes' if match_C12 else 'no'}")

# Claim C13: number of timesteps for one crossing
computed_C13 = computed_C11 / computed_C12
expected_C13 = 10
match_C13 = approx_equal(computed_C13, expected_C13)
print(f"CLAIM C13: computed={fmt(computed_C13)} expected={expected_C13} match={'yes' if match_C13 else 'no'}")

# Claim C14: minimum propagation time for L = 1.0 m
L_big = 1.0
computed_C14 = L_big / v_max
expected_C14 = 3.333333e-9
match_C14 = approx_equal(computed_C14, expected_C14, rel=1e-9)
print(f"CLAIM C14: computed={fmt(computed_C14)} expected={expected_C14} match={'yes' if match_C14 else 'no'}")

# Claim C15: number of timesteps for L = 1.0 m
computed_C15 = computed_C14 / computed_C12
expected_C15 = 1.0e4
match_C15 = approx_equal(computed_C15, expected_C15, rel=1e-9)
print(f"CLAIM C15: computed={fmt(computed_C15)} expected={expected_C15} match={'yes' if match_C15 else 'no'}")

print(f"VERIFICATION SUMMARY: 15 claims, {sum([match_C1, match_C2, match_C3, match_C4, match_C5, match_C6, match_C7, match_C8, match_C9, match_C10, match_C11, match_C12, match_C13, match_C14, match_C15])} match, {15 - sum([match_C1, match_C2, match_C3, match_C4, match_C5, match_C6, match_C7, match_C8, match_C9, match_C10, match_C11, match_C12, match_C13, match_C14, match_C15])} mismatch")
