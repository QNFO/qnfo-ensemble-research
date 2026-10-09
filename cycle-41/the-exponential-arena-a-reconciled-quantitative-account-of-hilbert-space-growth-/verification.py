import math

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = "n/a"
        print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
        return 0, 1  # no expected, count as informational
    if isinstance(computed, int) and isinstance(expected, int):
        match = computed == expected
    else:
        match = math.isclose(computed, expected, rel_tol=tol)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")
    return (1 if match else 0), 1

matched = 0
total = 0

# Q1: real dimension of pure-state arena for n=10: 2^(n+1) - 2
n1 = 10
q1 = 2**(n1 + 1) - 2
m, t = check("Q1", q1, 2046)
matched += m; total += t

# Q2: real dimension for n=50: 2^(n+1) - 2, approximately 2.25e15
n2 = 50
q2 = 2**(n2 + 1) - 2
q2_approx = q2 / 1e15  # express in units of 1e15
m, t = check("Q2", q2_approx, 2.25, tol=1e-2)
matched += m; total += t

# Q3: D_50 = 2^50 via 10^(n*log10(2)), log10(2)=0.301030
n3 = 50
log10_2 = 0.301030
q3 = 10**(n3 * log10_2)
m, t = check("Q3", q3, 1.1259e15, tol=1e-4)
matched += m; total += t

# Q4: D_100 = 2^100 via 10^(100*log10(2))
n4 = 100
q4 = 10**(n4 * log10_2)
m, t = check("Q4", q4, 1.2677e30, tol=1e-4)
matched += m; total += t

# Q5: D_300 = 2^300 via 10^(300*log10(2))
n5 = 300
q5 = 10**(n5 * log10_2)
m, t = check("Q5", q5, 2.037e90, tol=1e-3)
matched += m; total += t

# Q6: mixed-state parameter count for n=10: 4^n - 1
n6 = 10
q6 = 4**n6 - 1
m, t = check("Q6", q6, 1048575)
matched += m; total += t

# Q7: mixed-state parameter count for n=100: 4^100 - 1 = 10^(200*log10(2)) - 1
n7 = 100
q7 = 10**(2 * n7 * log10_2) - 1
m, t = check("Q7", q7, 1.6069e60, tol=1e-4)
matched += m; total += t

# Q8: memory for one n=50 state vector: M_n = 16 * 2^n bytes
bytes_per_amplitude = 16
n8 = 50
q8 = bytes_per_amplitude * 2**n8
m, t = check("Q8", q8, 18014398509481984)
matched += m; total += t

print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {total - matched} mismatch")
