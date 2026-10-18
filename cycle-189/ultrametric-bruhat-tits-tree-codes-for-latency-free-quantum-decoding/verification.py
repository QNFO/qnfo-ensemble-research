import math

def fmt(x):
    # format with at least 8 significant digits
    return f"{x:.8g}"

# Q1: code size for p=3, t=1
p = 3
t = 1
n = 1 + ((p + 1) * (p**t - 1)) / (p - 1)
print(f"CLAIM Q1: computed={fmt(n)} expected=5 match={'yes' if abs(n - 5) < 1e-12 else 'no'}")

# Q2: conditional distance for t=1
d = 2 * t + 1
print(f"CLAIM Q2: computed={fmt(d)} expected=3 match={'yes' if d == 3 else 'no'}")

# Q3: passive logical failure probability for p=3, t=1, ε=10⁻³
n = 5
eps = 1e-3
P = 0.0
for k in range(t + 1, n + 1):
    P += math.comb(n, k) * (eps**k) * ((1 - eps)**(n - k))
print(f"CLAIM Q3: computed={fmt(P)} expected=9.98×10^{-6} match={'yes' if abs(P - 9.98e-6) / 9.98e-6 < 1e-3 else 'no'}")

# Q4: logical error suppression factor
S = eps / P
print(f"CLAIM Q4: computed={fmt(S)} expected=100.2 match={'yes' if abs(S - 100.2) / 100.2 < 1e-3 else 'no'}")

# Q5: code size for p=3, t=2
t = 2
n2 = 1 + ((p + 1) * (p**t - 1)) / (p - 1)
print(f"CLAIM Q5: computed={fmt(n2)} expected=17 match={'yes' if n2 == 17 else 'no'}")

# Q6: passive logical failure probability for p=3, t=2, ε=10⁻³
n = int(n2)
P2 = 0.0
for k in range(t + 1, n + 1):
    P2 += math.comb(n, k) * (eps**k) * ((1 - eps)**(n - k))
print(f"CLAIM Q6: computed={fmt(P2)} expected=6.73×10^{-7} match={'yes' if abs(P2 - 6.73e-7) / 6.73e-7 < 1e-2 else 'no'}")

# Q7: decoder depth for n=5 (log_4 5)
L = math.log(5, 4)
print(f"CLAIM Q7: computed={fmt(L)} expected=1.16 match={'yes' if abs(L - 1.16) / 1.16 < 1e-2 else 'no'}")

# Q8: decoder depth for n=17 (log_4 17)
L2 = math.log(17, 4)
print(f"CLAIM Q8: computed={fmt(L2)} expected=2.04 match={'yes' if abs(L2 - 2.04) / 2.04 < 1e-2 else 'no'}")
