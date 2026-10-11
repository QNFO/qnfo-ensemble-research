import math

def n_t(p, t):
    return 1 + (p + 1) * (p**t - 1) // (p - 1)

def p_pass(n, eps, t):
    total = 0.0
    for k in range(0, t + 1):
        total += math.comb(n, k) * (eps**k) * ((1 - eps)**(n - k))
    return 1 - total

claims = []

# Q1-Q6: ball sizes
expected_n = {
    (3, 1): 5, (3, 2): 17, (3, 3): 53,
    (2, 1): 4, (2, 2): 10, (2, 3): 22,
}
ids = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]
i = 0
for (p, t) in [(3, 1), (3, 2), (3, 3), (2, 1), (2, 2), (2, 3)]:
    computed = n_t(p, t)
    expected = expected_n[(p, t)]
    match = "yes" if computed == expected else "no"
    print(f"CLAIM {ids[i]}: computed={computed} expected={expected} match={match}")
    claims.append(match)
    i += 1

# Q7: passive failure probability, p=3, t=1, eps=1e-3
eps = 1e-3
n = 5
computed_q7 = p_pass(n, eps, 1)
expected_q7 = 9.98e-6
match_q7 = "yes" if math.isclose(computed_q7, expected_q7, rel_tol=1e-2) else "no"
print(f"CLAIM Q7: computed={computed_q7:.6e} expected={expected_q7:.6e} match={match_q7}")
claims.append(match_q7)

# Q8: suppression factor eps / P_pass
# Use the paper's stated P_pass value as the input for this claim
p_pass_input = 9.98e-6
computed_q8 = eps / p_pass_input
expected_q8 = 100.2
match_q8 = "yes" if math.isclose(computed_q8, expected_q8, rel_tol=1e-2) else "no"
print(f"CLAIM Q8: computed={computed_q8:.6f} expected={expected_q8:.6f} match={match_q8}")
claims.append(match_q8)

n_claims = len(claims)
n_match = sum(1 for m in claims if m == "yes")
n_mismatch = n_claims - n_match
print(f"VERIFICATION SUMMARY: {n_claims} claims, {n_match} match, {n_mismatch} mismatch")
