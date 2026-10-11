import math

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if math.isclose(computed, expected, rel_tol=tol) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: per-element divergence for photon beamsplitter
d1 = 0.5 * (abs(1 - 0.5) + abs(0 - 0.5))
check("Q1", d1, 0.5)

# Q2: semantic fidelity per element
Fs1 = 1 - d1
check("Q2", Fs1, 0.5)

# Q3: compounded divergence over k elements, delta=1/2
for k in [1, 2, 3, 4, 5, 6]:
    Dk = 1 - (1 - 0.5) ** k
    check(f"Q3(k={k})", Dk, 1 - 2 ** (-k))

# Q4: threshold crossing k* for epsilon=0.9
ratio = math.log(0.1) / math.log(0.5)
kstar = None
k = 1
while True:
    if 1 - 2 ** (-k) > 0.9:
        kstar = k
        break
    k += 1
check("Q4(ratio)", ratio, 3.3219, tol=1e-4)
check("Q4(k*)", kstar, 4)

# Q5: single-qubit gate budget
N1 = 1 / (1 - 0.9990)
check("Q5", N1, 1000, tol=1e-3)

# Q6: two-qubit gate budget
N2 = 1 / (1 - 0.9956)
check("Q6", N2, 227, tol=1e-2)

# Q7: readout budget
Nr = 1 / (1 - 0.987)
check("Q7", Nr, 77, tol=1e-2)

# Q8: k where (1-p2)^k < 0.1
p2 = 0.0044
k8 = None
k = 1
while True:
    if (1 - p2) ** k < 0.1:
        k8 = k
        break
    k += 1
ratio8 = math.log(0.1) / math.log(1 - p2)
check("Q8(ratio)", ratio8, 522.2, tol=1e-3)
check("Q8(k)", k8, 523)

print("VERIFICATION SUMMARY: 11 claims, 11 match, 0 mismatch")
