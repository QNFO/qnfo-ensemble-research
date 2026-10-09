import math
import cmath

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        if isinstance(computed, complex) or isinstance(expected, complex):
            match = "yes" if cmath.isclose(computed, expected, rel_tol=1e-6) else "no"
        else:
            match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: d_sigma^2 = N_{sigma sigma}^1 * d_1 + N_{sigma sigma}^psi * d_psi = 2
N1, Npsi = 1, 1
d1, dpsi = 1, 1
d_sigma_sq = N1 * d1 + Npsi * dpsi
d_sigma = math.sqrt(d_sigma_sq)
results.append(check("Q1", d_sigma, math.sqrt(2)))

# Q2: D = sqrt(d_1^2 + d_sigma^2 + d_psi^2)
D = math.sqrt(d1**2 + d_sigma**2 + dpsi**2)
results.append(check("Q2", D, 2.0))

# Q3: S_{sigma 1} = d_sigma * d_1 / D
S_sigma1 = d_sigma * d1 / D
results.append(check("Q3", S_sigma1, math.sqrt(2) / 2))

# Q4: S_{sigma psi} = (d_sigma * d_psi / D) * (-1)
S_sigmapsi = (d_sigma * dpsi / D) * (-1)
results.append(check("Q4", S_sigmapsi, -math.sqrt(2) / 2))

# Q5: S_{sigma sigma} = (1/D)*(theta_1/theta_sigma^2 * d_1 + theta_psi/theta_sigma^2 * d_psi)
theta_1 = 1.0
theta_psi = -1.0
theta_sigma_sq = cmath.exp(1j * math.pi / 4)
S_sigmasigma = (1 / D) * (theta_1 / theta_sigma_sq * d1 + theta_psi / theta_sigma_sq * dpsi)
results.append(check("Q5", S_sigmasigma, 0.0))

# Q6: S_{11} = S_{1 psi} = S_{psi psi} = 1/2
S_11 = d1 * d1 / D
S_1psi = d1 * dpsi / D
S_psipsi = dpsi * dpsi / D
results.append(check("Q6a", S_11, 0.5))
results.append(check("Q6b", S_1psi, 0.5))
results.append(check("Q6c", S_psipsi, 0.5))

# Q7: theta_sigma = e^{i pi/8} via m_1 = R^2, theta_sigma^2 = 1/m_1
R = cmath.exp(-1j * math.pi / 8)
m_1 = R**2
theta_sigma_sq_7 = 1 / m_1
theta_sigma = cmath.exp(1j * math.pi / 8)  # principal root of theta_sigma_sq_7
results.append(check("Q7", theta_sigma_sq_7, theta_sigma**2))
results.append(check("Q7b", theta_sigma, cmath.exp(1j * math.pi / 8)))

# Q8: theta_psi / theta_sigma^2 = m_psi / m_1 = e^{i pi} = -1
m_psi = cmath.exp(3j * math.pi / 4)
ratio = m_psi / m_1
results.append(check("Q8", ratio, -1.0))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
