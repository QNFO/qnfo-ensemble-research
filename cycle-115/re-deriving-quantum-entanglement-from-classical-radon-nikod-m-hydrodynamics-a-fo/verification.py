import math
from fractions import Fraction

results = []

# Q1: eigenvalues of Pauli strings on GHZ
# Represent basis states |abc> as tuples; GHZ = (|000> + |111>)/sqrt2.
# Pauli action: X flips bit with phase +1; Y flips bit with phase i on 0->1, -i on 1->0.
def pauli_string_action(bits, ops):
    phase = 1 + 0j
    new_bits = list(bits)
    for idx, op in enumerate(ops):
        if op == 'X':
            new_bits[idx] = 1 - new_bits[idx]
        elif op == 'Y':
            if new_bits[idx] == 0:
                new_bits[idx] = 1
                phase *= 1j
            else:
                new_bits[idx] = 0
                phase *= -1j
    return tuple(new_bits), phase

GHZ_basis = [(0, 0, 0), (1, 1, 1)]
strings = ['XXX', 'XYY', 'YXY', 'YYX']
eigs = {}
for s in strings:
    terms = []
    for b in GHZ_basis:
        nb, ph = pauli_string_action(b, s)
        terms.append((nb, ph))
    # S|GHZ> = (1/sqrt2) * sum terms; check if equals +|GHZ> or -|GHZ>
    # term for |000> maps to (nb0, ph0), term for |111> maps to (nb1, ph1)
    (nb0, ph0), (nb1, ph1) = terms
    # eigenvalue +1 if nb0 == (1,1,1) and ph0 == ph1 == +1... general check:
    # S|GHZ> = (1/sqrt2)(ph0 |nb0> + ph1 |nb1>)
    # equals +|GHZ> iff nb0=(1,1,1), nb1=(0,0,0), ph0=ph1=+1
    # equals -|GHZ> iff same mapping with ph0=ph1=-1
    if nb0 == (1, 1, 1) and nb1 == (0, 0, 0) and ph0 == ph1 == 1:
        eigs[s] = 1
    elif nb0 == (1, 1, 1) and nb1 == (0, 0, 0) and ph0 == ph1 == -1:
        eigs[s] = -1
    else:
        eigs[s] = None  # not an eigenvector

computed_q1 = eigs
expected_q1 = {'XXX': 1, 'XYY': -1, 'YXY': -1, 'YYX': -1}
match_q1 = all(computed_q1[k] == expected_q1[k] for k in strings)
results.append(("Q1", computed_q1['XXX'], expected_q1['XXX'], match_q1))

# Q2: pointwise product constraint
# Each A_i^s in {-1,+1}; product P1P2P3P4 = product of squares = 1
# Verify symbolically: each of the 6 factors appears exactly twice.
# Enumerate all 2^6 assignments to confirm.
count = 0
all_ok = True
for bits in range(64):
    vals = [1 if (bits >> k) & 1 == 0 else -1 for k in range(6)]
    A1X, A1Y, A2X, A2Y, A3X, A3Y = vals
    P1 = A1X * A2X * A3X
    P2 = A1X * A2Y * A3Y
    P3 = A1Y * A2X * A3Y
    P4 = A1Y * A2Y * A3X
    if P1 * P2 * P3 * P4 != 1:
        all_ok = False
    count += 1
computed_q2 = 1 if all_ok else None
results.append(("Q2", computed_q2, 1, computed_q2 == 1))

# Q3: quantum product of four correlations
P1q, P2q, P3q, P4q = 1, -1, -1, -1
computed_q3 = P1q * P2q * P3q * P4q
results.append(("Q3", computed_q3, -1, computed_q3 == -1))

# Q4: Mermin classical bound via exhaustive enumeration
max_val = 0
for bits in range(64):
    vals = [1 if (bits >> k) & 1 == 0 else -1 for k in range(6)]
    A1X, A1Y, A2X, A2Y, A3X, A3Y = vals
    P1 = A1X * A2X * A3X
    P2 = A1X * A2Y * A3Y
    P3 = A1Y * A2X * A3Y
    P4 = A1Y * A2Y * A3X
    m = abs(P1 - P2 - P3 - P4)
    if m > max_val:
        max_val = m
computed_q4 = max_val
results.append(("Q4", computed_q4, 2, computed_q4 == 2))

# Q5: Mermin quantum value
computed_q5 = abs(P1q - P2q - P3q - P4q)
results.append(("Q5", computed_q5, 4, computed_q5 == 4))

# Q6: gap and factor
computed_gap = computed_q5 - computed_q4
computed_factor = computed_q5 / computed_q4
results.append(("Q6a", computed_gap, 2, computed_gap == 2))
results.append(("Q6b", computed_factor, 2, math.isclose(computed_factor, 2, rel_tol=1e-6)))

# Q7: CHSH classical bound via exhaustive enumeration
max_s = 0
for bits in range(16):
    a = 1 if (bits >> 0) & 1 == 0 else -1
    b = 1 if (bits >> 1) & 1 == 0 else -1
    ap = 1 if (bits >> 2) & 1 == 0 else -1
    bp = 1 if (bits >> 3) & 1 == 0 else -1
    s = abs(a * b + a * bp + ap * b - ap * bp)
    if s > max_s:
        max_s = s
computed_q7 = max_s
results.append(("Q7", computed_q7, 2, computed_q7 == 2))

# Q8: CHSH quantum maximum (projection)
sqrt2 = math.sqrt(2)
computed_q8 = 2 * sqrt2
expected_q8 = 2.828427
results.append(("Q8", computed_q8, expected_q8, math.isclose(computed_q8, expected_q8, rel_tol=1e-6)))

n = len(results)
m = sum(1 for _, c, e, ok in results if ok)
k = n - m
for cid, c, e, ok in results:
    print(f"CLAIM {cid}: computed={c} expected={e} match={'yes' if ok else 'no'}")
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
