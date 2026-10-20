import math

matches = []

# Q1
factor1 = 10
factor2 = 5
S = factor1 * factor2
expected_Q1 = 50
match = S == expected_Q1
matches.append(match)
print(f"CLAIM Q1: computed={S} expected={expected_Q1} match={'yes' if match else 'no'}")

# Q2
sigma = 0.05
Rhat = 0.5 * math.log(2 * math.pi * sigma**2) + 0.5
abs_Rhat = abs(Rhat)
computed_Q2 = round(abs_Rhat, 2)
expected_Q2 = 1.58
match = abs(computed_Q2 - expected_Q2) < 1e-9
matches.append(match)
print(f"CLAIM Q2: computed={computed_Q2:.2f} expected={expected_Q2:.2f} match={'yes' if match else 'no'}")

# Q3
sigma2 = 0.0025
tau2 = 0.01
n = 100
Z = 1 / math.sqrt(2 * math.pi * (sigma2 + tau2 / n))
negLogZ = -math.log(Z)
computed_Q3 = round(negLogZ, 3)
expected_Q3 = -2.058
match = abs(computed_Q3 - expected_Q3) < 1e-9
matches.append(match)
print(f"CLAIM Q3: computed={computed_Q3:.3f} expected={expected_Q3:.3f} match={'yes' if match else 'no'}")

# Q4
ERS = negLogZ + Rhat
computed_Q4 = round(ERS, 2)
expected_Q4 = -3.64
match = abs(computed_Q4 - expected_Q4) < 1e-9
matches.append(match)
print(f"CLAIM Q4: computed={computed_Q4:.2f} expected={expected_Q4:.2f} match={'yes' if match else 'no'}")

# Q5
VaR_095 = 0.10
VaR_099 = 0.20
RVaR = (VaR_095 + VaR_099) / 2
computed_Q5 = round(RVaR, 2)
expected_Q5 = 0.15
match = abs(computed_Q5 - expected_Q5) < 1e-9
matches.append(match)
print(f"CLAIM Q5: computed={computed_Q5:.2f} expected={expected_Q5:.2f} match={'yes' if match else 'no'}")

# Q6
baselineCPU = 1_000_000
reductionFactor = 50
reducedCPU = baselineCPU // reductionFactor
computed_Q6 = reducedCPU
expected_Q6 = 20000
match = computed_Q6 == expected_Q6
matches.append(match)
print(f"CLAIM Q6: computed={computed_Q6} expected={expected_Q6} match={'yes' if match else 'no'}")

# Q7
costPerHour = 0.02
cost = reducedCPU * costPerHour
computed_Q7 = round(cost, 2)
expected_Q7 = 400
match = int(computed_Q7) == expected_Q7
matches.append(match)
print(f"CLAIM Q7: computed={int(computed_Q7)} expected={expected_Q7} match={'yes' if match else 'no'}")

# Q8
originalCost = baselineCPU * costPerHour
reducedCost = cost
saving = originalCost - reducedCost
computed_Q8 = round(saving, 0)
expected_Q8 = 19600
match = int(computed_Q8) == expected_Q8
matches.append(match)
print(f"CLAIM Q8: computed={int(computed_Q8)} expected={expected_Q8} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(matches)} claims, {sum(matches)} match, {len(matches)-sum(matches)} mismatch")
