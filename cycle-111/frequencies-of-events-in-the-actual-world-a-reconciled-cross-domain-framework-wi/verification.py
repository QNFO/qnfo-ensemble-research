import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

two_pi = 6.283185
ln2 = 0.693147
ln3 = 1.098612
ln5 = 1.609438
ln7 = 1.945910

# Q1: omega_2 = 2*pi / ln(2)
w2 = two_pi / ln2
print(f"CLAIM Q1: computed={w2:.6f} expected=9.064722 match={'yes' if close(w2, 9.064722) else 'no'}")

# Q2: omega_3 = 2*pi / ln(3)
w3 = two_pi / ln3
print(f"CLAIM Q2: computed={w3:.6f} expected=5.719203 match={'yes' if close(w3, 5.719203) else 'no'}")

# Q3: omega_5 = 2*pi / ln(5)
w5 = two_pi / ln5
print(f"CLAIM Q3: computed={w5:.6f} expected=3.903962 match={'yes' if close(w5, 3.903962) else 'no'}")

# Q4: omega_7 = 2*pi / ln(7)
w7 = two_pi / ln7
print(f"CLAIM Q4: computed={w7:.6f} expected=3.228919 match={'yes' if close(w7, 3.228919) else 'no'}")

# Q5: mean of omega_p
mean_w = (w2 + w3 + w5 + w7) / 4
print(f"CLAIM Q5: computed={mean_w:.6f} expected=5.479201 match={'yes' if close(mean_w, 5.479201) else 'no'}")

# Q6: omega_2/omega_3 = ln3/ln2
r23 = ln3 / ln2
print(f"CLAIM Q6: computed={r23:.6f} expected=1.584962 match={'yes' if close(r23, 1.584962) else 'no'}")

# Q7: omega_2/omega_5 = ln5/ln2
r25 = ln5 / ln2
print(f"CLAIM Q7: computed={r25:.6f} expected=2.321929 match={'yes' if close(r25, 2.321929) else 'no'}")

# Q8: omega_3/omega_5 = ln5/ln3
r35 = ln5 / ln3
print(f"CLAIM Q8: computed={r35:.6f} expected=1.464974 match={'yes' if close(r35, 1.464974) else 'no'}")

claims = [close(w2,9.064722), close(w3,5.719203), close(w5,3.903962), close(w7,3.228919),
          close(mean_w,5.479201), close(r23,1.584962), close(r25,2.321929), close(r35,1.464974)]
n = len(claims)
m = sum(claims)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
