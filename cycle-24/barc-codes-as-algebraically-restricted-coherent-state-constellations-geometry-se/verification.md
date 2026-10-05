# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For N equally weighted points on a circle of radius r, the maximum minimum chord is d_max = 2r sin(π/N); for N=6, d_max = r.",
    "inputs": "N=6, sin(π/6)=0.5",
    "formula": "d_max = 2*r*sin(pi/N) = 2*r*0.5 = r"
  },
  {
    "id": "Q2",
    "statement": "For the hexagonal constellation, mean photon number n̄ = r², so d_max = √n̄.",
    "inputs": "n̄ = r² (all six points have |αᵢ|=r)",
    "formula": "d_max = sqrt(n̄)"
  },
  {
    "id": "Q3",
    "statement": "At n̄ = 8, radius r = √8 ≈ 2.8284271 and d_max = √8 ≈ 2.8284271.",
    "inputs": "n̄=8",
    "formula": "r = sqrt(8) = 2*sqrt(2) ≈ 2.8284271; d_max = sqrt(8) ≈ 2.8284271"
  },
  {
    "id": "Q4",
    "statement": "Worst-case (adjacent) codeword overlap squared at n̄=8 is e⁻⁴ ≈ 0.01831564.",
    "inputs": "r²=8, θ=π/3, 1−cos(π/3)=0.5",
    "formula": "|⟨αᵢ|αⱼ⟩|² = exp(−r²(1−cos θ)) = exp(−8*0.5) = exp(−4) ≈ 0.01831563888873418"
  },
  {
    "id": "Q5",
    "statement": "Adjacent-point overlap magnitude |⟨αᵢ|αⱼ⟩| = e⁻² ≈ 0.1353353.",
    "inputs": "|⟨αᵢ|αⱼ⟩|² = e⁻⁴",
    "formula": "|⟨αᵢ|αⱼ⟩| = sqrt(e⁻⁴) = e⁻² ≈ 0.1353352832366127"
  },
  {
    "id": "Q6",
    "statement": "Next-nearest (θ=120°) overlap squared at n̄=8 is e⁻¹² ≈ 6.14421×10⁻⁶.",
    "inputs": "r²=8, 1−cos(120°)=1.5",
    "formula": "|⟨αᵢ|αⱼ⟩|² = exp(−8*1.5) = exp(−12) ≈ 6.14421235332821e−6"
  },
  {
    "id": "Q7",
    "statement": "Opposite (θ=180°) overlap squared at n̄=8 is e⁻¹⁶ ≈ 1.12535×10⁻⁷.",
    "inputs": "r²=8, 1−cos(180°)=2",
    "formula": "|⟨αᵢ|αⱼ⟩|² = exp(−8*2) = exp(−16) ≈ 1.1253517471925912e−7"
  },
  {
    "id": "Q8",
    "statement": "Diagonal contribution to ⟨â†â⟩ of the equal superposition is 8.",
    "inputs": "|αᵢ|²=8, N=6",
    "formula": "(1/6)*(6*8) = 8"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: d_max = 2*r*sin(pi/N) for N=6 -> r
N = 6
r = 1.0
d_max = 2 * r * math.sin(math.pi / N)
results.append(check("Q1", d_max, r))

# Q2: d_max = sqrt(nbar) where nbar = r^2
nbar = r ** 2
results.append(check("Q2", math.sqrt(nbar), r))

# Q3: nbar=8 -> r = sqrt(8) ≈ 2.8284271, d_max = sqrt(8)
nbar8 = 8.0
r8 = math.sqrt(nbar8)
d8 = math.sqrt(nbar8)
results.append(check("Q3", r8, 2.8284271))
results.append(check("Q3", d8, 2.8284271))

# Q4: worst-case overlap squared at nbar=8: exp(-8*(1-cos(pi/3)))
theta = math.pi / 3
overlap_sq = math.exp(-nbar8 * (1 - math.cos(theta)))
results.append(check("Q4", overlap_sq, math.exp(-4)))

# Q5: adjacent overlap magnitude = sqrt(e^-4) = e^-2
overlap_mag = math.sqrt(overlap_sq)
results.append(check("Q5", overlap_mag, math.exp(-2)))

# Q6: next-nearest (120 deg) overlap squared: exp(-8*1.5) = exp(-12)
theta2 = 2 * math.pi / 3
overlap_sq2 = math.exp(-nbar8 * (1 - math.cos(theta2)))
results.append(check("Q6", overlap_sq2, math.exp(-12)))

# Q7: opposite (180 deg) overlap squared: exp(-8*2) = exp(-16)
theta3 = math.pi
overlap_sq3 = math.exp(-nbar8 * (1 - math.cos(theta3)))
results.append(check("Q7", overlap_sq3, math.exp(-16)))

# Q8: diagonal contribution to <a†a>: (1/6)*(6*8) = 8
diag = (1.0 / N) * (N * nbar8)
results.append(check("Q8", diag, 8.0))

n = len(results)
m = sum(results)
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.9999999999999999 expected=1.0 match=yes
CLAIM Q2: computed=1.0 expected=1.0 match=yes
CLAIM Q3: computed=2.8284271247461903 expected=2.8284271 match=yes
CLAIM Q3: computed=2.8284271247461903 expected=2.8284271 match=yes
CLAIM Q4: computed=0.018315638888734196 expected=0.01831563888873418 match=yes
CLAIM Q5: computed=0.13533528323661276 expected=0.1353352832366127 match=yes
CLAIM Q6: computed=6.144212353328221e-06 expected=6.14421235332821e-06 match=yes
CLAIM Q7: computed=1.1253517471925912e-07 expected=1.1253517471925912e-07 match=yes
CLAIM Q8: computed=8.0 expected=8.0 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```
