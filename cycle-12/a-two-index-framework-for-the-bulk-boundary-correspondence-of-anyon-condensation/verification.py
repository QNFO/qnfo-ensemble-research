import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, complex):
        match = "yes" if abs(computed - expected) < 1e-6 else "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: Ising D_C^2 = 4, D_C = 2
d1, dsig, dpsi = 1.0, math.sqrt(2), 1.0
DC2 = d1**2 + dsig**2 + dpsi**2
DC = math.sqrt(DC2)
results.append(check("Q1", DC, 2.0))

# Q2: dim(A) = 2 for A = 1 + psi
dimA = d1 + dpsi
results.append(check("Q2", dimA, 2.0))

# Q3: kappa = dim(A)^2 = 4
kappa = dimA**2
results.append(check("Q3", kappa, 4.0))

# Q4: D_D = D_C/dim(A) = 1
DD = DC / dimA
results.append(check("Q4", DD, 1.0))

# Q5: Gauss-Milgram: sum d_a^2 theta_a = 2 e^{i pi/8} = D_C e^{2 pi i c/8} => c_C = 1/2
theta1, thetasig, thetapsi = 1.0, math.exp(1j*math.pi/8), -1.0
S = d1**2*theta1 + dsig**2*thetasig + dpsi**2*thetapsi
# S = D_C e^{2 pi i c/8}; solve for c mod 8
ratio = S / DC
cC = (math.atan2(ratio.imag, ratio.real) / (2*math.pi)) * 8
cC = cC % 8
results.append(check("Q5", cC, 0.5))

# Q6: mu = 2(c_C - c_D), c_D = 0
cD = 0.0
mu = 2*(cC - cD)
results.append(check("Q6", mu, 1.0))

# Q7: Toric code D_C = 2
toric = [1.0, 1.0, 1.0, 1.0]
DC2t = sum(d**2 for d in toric)
DCt = math.sqrt(DC2t)
results.append(check("Q7", DCt, 2.0))

# Q8: Toric code dim(A) = 2, kappa = 4
dimA_t = 1.0 + 1.0
kappa_t = dimA_t**2
results.append(check("Q8", kappa_t, 4.0))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n-m} mismatch")
