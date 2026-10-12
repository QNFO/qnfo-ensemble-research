import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: mixture hazard
h_BPP, h_HARD, pi = 0.10, 0.01, 0.2
h_bar = pi * h_BPP + (1 - pi) * h_HARD
results.append(("Q1", h_bar, 0.028))

# Q2: expected discounted loss for L=10
L, r = 10, 0.05
E_exposed = L * h_bar / (h_bar + r)
results.append(("Q2", E_exposed, 3.589744))

# Q3: loss threshold at pi=0.2
L_star = 1 + r / h_bar
results.append(("Q3", L_star, 2.785714))

# Q4: loss threshold at pi=0
h_bar0 = 0 * h_BPP + 1 * h_HARD
L_star0 = 1 + r / h_bar0
results.append(("Q4", L_star0, 6))

# Q5: loss threshold at pi=1
h_bar1 = 1 * h_BPP + 0 * h_HARD
L_star1 = 1 + r / h_bar1
results.append(("Q5", L_star1, 1.5))

# Q6: critical prior for L=2
L_asset = 2
pi_star = (r / (L_asset - 1) - h_HARD) / (h_BPP - h_HARD)
results.append(("Q6", pi_star, 0.444444))

# Q7: Scenario D discount factor
T = 10
d = math.exp(-r * T)
results.append(("Q7", d, 0.606531))

# Q8: Scenario D expected discounted breach cost
p, C_b = 0.05, 200000000
E_wait_breach = p * C_b * d
results.append(("Q8", E_wait_breach, 6065310))

match_count = 0
for qid, computed, expected in results:
    match = close(computed, expected)
    if match:
        match_count += 1
    print(f"CLAIM {qid}: computed={computed:.6f} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
