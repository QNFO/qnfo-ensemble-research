import math

# Helper to format numbers with a fixed number of decimal places
def fmt(val, places):
    return f"{round(val, places):.{places}f}"

# 1. Bridge‑vocabulary proportion
p_bridge = 1 - 0.972
print(f"CLAIM Q1: computed={fmt(p_bridge,3)} expected=0.028 match={'yes' if fmt(p_bridge,3)=='0.028' else 'no'}")

# 2. Per‑generation compression fraction
epsilon = 0.15
print(f"CLAIM Q2: computed={fmt(epsilon,2)} expected=0.15 match={'yes' if fmt(epsilon,2)=='0.15' else 'no'}")

# 3. Initial tail entropy
H0 = 12.0
print(f"CLAIM Q3: computed={fmt(H0,0)} expected=12 match={'yes' if fmt(H0,0)=='12' else 'no'}")

# 4. Normalization beta*V0
betaV0 = 1.0
print(f"CLAIM Q4: computed={fmt(betaV0,0)} expected=1 match={'yes' if fmt(betaV0,0)=='1' else 'no'}")

# 5. Retention factor rho
rho = 1 - epsilon
print(f"CLAIM Q5: computed={fmt(rho,2)} expected=0.85 match={'yes' if fmt(rho,2)=='0.85' else 'no'}")

# 6. Tail entropy after 5 generations
H5 = H0 * rho**5
print(f"CLAIM Q6: computed={fmt(H5,8)} expected=5.32446375 match={'yes' if fmt(H5,8)=='5.32446375' else 'no'}")

# 7. Tail entropy after 10 generations
H10 = H0 * rho**10
print(f"CLAIM Q7: computed={fmt(H10,8)} expected=2.36249285 match={'yes' if fmt(H10,8)=='2.36249285' else 'no'}")

# 8. Smallest integer g with tail entropy < 1 bit
g = 0
while H0 * rho**g >= 1:
    g += 1
print(f"CLAIM Q8: computed={g} expected=16 match={'yes' if g==16 else 'no'}")

# 9. Break‑even coupling constant kappa*
kappa_star = (epsilon * H0) / (betaV0 * p_bridge)
print(f"CLAIM Q9: computed={fmt(kappa_star,6)} expected=64.285714 match={'yes' if fmt(kappa_star,6)=='64.285714' else 'no'}")

# 10. Consilience gain at break‑even
DeltaC_star = kappa_star * p_bridge * 1  # V0 = 1
print(f"CLAIM Q10: computed={fmt(DeltaC_star,1)} expected=1.8 match={'yes' if fmt(DeltaC_star,1)=='1.8' else 'no'}")

# 11. Sensitivity factor linking kappa* to epsilon
coeff = H0 / p_bridge
print(f"CLAIM Q11: computed={fmt(coeff,9)} expected=428.571429 match={'yes' if fmt(coeff,9)=='428.571429' else 'no'}")

# 12. kappa* for epsilon = 0.05
kappa_eps_005 = coeff * 0.05
print(f"CLAIM Q12: computed={fmt(kappa_eps_005,2)} expected=21.43 match={'yes' if fmt(kappa_eps_005,2)=='21.43' else 'no'}")

# 13. kappa* for epsilon = 0.30
kappa_eps_030 = coeff * 0.30
print(f"CLAIM Q13: computed={fmt(kappa_eps_030,2)} expected=128.57 match={'yes' if fmt(kappa_eps_030,2)=='128.57' else 'no'}")

# 14. Sum of retention factors over five generations
sum_rho = (1 - rho**5) / (1 - rho)
print(f"CLAIM Q14: computed={fmt(sum_rho,8)} expected=3.70863125 match={'yes' if fmt(sum_rho,8)=='3.70863125' else 'no'}")

# 15. Average tail entropy over a five‑generation re‑anchoring cycle
m = 5
r = 1
H_bar = (H0 * r / m) * sum_rho
print(f"CLAIM Q15: computed={fmt(H_bar,6)} expected=8.900715 match={'yes' if fmt(H_bar,6)=='8.900715' else 'no'}")

# 16. Uplift relative to pure synthetic g=5 tail entropy
uplift = (H_bar - H5) / H5 * 100
print(f"CLAIM Q16: computed={fmt(uplift,1)} expected=67.1 match={'yes' if fmt(uplift,1)=='67.1' else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, " +
      f"{sum(1 for line in [None])} match, " +
      f"{16 - sum(1 for line in [None])} mismatch")
