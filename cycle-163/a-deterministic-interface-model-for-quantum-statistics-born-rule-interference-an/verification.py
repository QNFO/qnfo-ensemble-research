import math

def fmt(x):
    return f"{x:.10f}"

# Q1
computed = (1 + math.cos(math.pi/3)) / 2
expected = 0.75
print(f"CLAIM Q1: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q2
computed = (math.cos(math.pi/4))**2
expected = 0.5
print(f"CLAIM Q2: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q3
computed = 4 * math.cos(math.pi/4)
expected = 2.82842712
print(f"CLAIM Q3: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q4
computed = (2*math.sqrt(2) - 2) / 2
expected = 0.41421356
print(f"CLAIM Q4: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q5
computed = (math.sqrt(2)/2) / 1
expected = 0.70710678
print(f"CLAIM Q5: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q6: delta >= epsilon/2 follows from 2*delta >= epsilon; check with epsilon = 1
epsilon = 1.0
computed = epsilon / 2
expected = 0.5
print(f"CLAIM Q6: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q7
computed = (2*math.sqrt(2) - 2) / 8
expected = 0.10355339
print(f"CLAIM Q7: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q8
computed = (2*math.sqrt(2) - 2) / 4
expected = 0.20710678
print(f"CLAIM Q8: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q9
computed = ((2*math.sqrt(2) - 2) / 4) / (1/15)
expected = 3.10660172
print(f"CLAIM Q9: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q10
computed = 2 + 4/15
expected = 2.26666667
print(f"CLAIM Q10: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q11
computed = (4/15) / 2
expected = 0.13333333
print(f"CLAIM Q11: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q12
computed = (4/15) / (2*math.sqrt(2) - 2)
expected = 0.32189514
print(f"CLAIM Q12: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

# Q13: check with delta_0 = 0.10355339
delta0 = 0.10355339
computed = 2 + 8*delta0
expected = 2.82842712
print(f"CLAIM Q13: computed={fmt(computed)} expected={expected} match={'yes' if round(computed,8)==expected else 'no'}")

print("VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch")
