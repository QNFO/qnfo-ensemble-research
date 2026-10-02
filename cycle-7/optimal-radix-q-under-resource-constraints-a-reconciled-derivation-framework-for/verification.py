import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

def check(cid, computed, expected):
    if expected is None:
        m = "no"
    elif isinstance(computed, int) and isinstance(expected, int):
        m = "yes" if computed == expected else "no"
    else:
        m = "yes" if close(float(computed), float(expected)) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={m}")
    return m == "yes"

results = []

# Q1: continuous optimum
c0, c1 = 1.0, 0.1
qstar = 1 + math.sqrt(1 + c0 / c1)
results.append(check("Q1", round(qstar, 8), 4.31662479))

# Q2..Q7: exact integer evaluation for various q
N = 1000000
def evaluate(q):
    n = math.ceil(math.log(N) / math.log(q))
    M = (q ** (n + 1) - 1) // (q - 1)
    E = (c0 + c1 * q) * M
    return n, M, E

expected = {
    2: (20, 2097151, 2516581.2),
    3: (13, 2391484, 3108929.2),
    4: (10, 1398101, 1957341.4),
    5: (9, 2441406, 3662109.0),
    7: (8, 6725601, 11433521.7),
    10: (6, 1111111, 2222222.0),
}
ids = {2: "Q2", 3: "Q3", 4: "Q4", 5: "Q5", 7: "Q6", 10: "Q7"}
Evals = {}
for q in [2, 3, 4, 5, 7, 10]:
    n, M, E = evaluate(q)
    Evals[q] = E
    en, eM, eE = expected[q]
    ok = (n == en) and (M == eM) and close(E, eE)
    print(f"CLAIM {ids[q]}: computed=n={n},M={M},E={E} expected=n={en},M={eM},E={eE} match={'yes' if ok else 'no'}")
    results.append(ok)

# Q8: saving of q=4 over q=2
saving = (Evals[2] - Evals[4]) / Evals[2]
results.append(check("Q8", round(saving, 3), 0.222))

n_match = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results) - n_match} mismatch")
