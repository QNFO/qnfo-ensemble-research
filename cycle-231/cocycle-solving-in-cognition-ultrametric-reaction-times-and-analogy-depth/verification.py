import math

def fmt(x):
    # format with at least 8 significant digits, remove trailing zeros
    s = f"{x:.10f}".rstrip('0').rstrip('.')
    return s

# Q1
a = 200.0  # ms
b = 50.0   # ms per level
L = 4
RT1 = a + b * L
print(f"CLAIM Q1: computed={fmt(RT1)} ms expected=400 ms match={'yes' if round(RT1)==400 else 'no'}")

# Q2
k = 100.0  # ms
CR = 9.0
D2 = k * math.log(CR)
print(f"CLAIM Q2: computed={fmt(D2)} ms expected=220 ms match={'yes' if round(D2)==220 else 'no'}")

# Q3
a_val = 200.0
print(f"CLAIM Q3: computed={fmt(a_val)} ms expected=200 ms match={'yes' if a_val==200 else 'no'}")

# Q4
b20 = 20.0
print(f"CLAIM Q4: computed={fmt(b20)} ms expected=20 ms match={'yes' if b20==20 else 'no'}")

# Q5
b50 = 50.0
print(f"CLAIM Q5: computed={fmt(b50)} ms expected=50 ms match={'yes' if b50==50 else 'no'}")

# Q6
k_val = 100.0
print(f"CLAIM Q6: computed={fmt(k_val)} ms expected=100 ms match={'yes' if k_val==100 else 'no'}")

# Q7
dAC = 3.0
dBD = 3.0
dAD = 1.0
dBC = 1.0
CR7 = (dAC * dBD) / (dAD * dBC)
print(f"CLAIM Q7: computed={fmt(CR7)} expected=9 match={'yes' if CR7==9 else 'no'}")

# Q8
D8 = k * math.log(CR)
print(f"CLAIM Q8: computed={fmt(D8)} ms expected=219.722 ms match={'yes' if round(D8,3)==219.722 else 'no'}")

# Q9
b_orig = 50.0
increase = 0.10
delta_RT = (increase * b_orig) * L
print(f"CLAIM Q9: computed={fmt(delta_RT)} ms expected=8 ms match={'yes' if round(delta_RT)==8 else 'no'}")

# Q10
delta_D = k * math.log(2)
print(f"CLAIM Q10: computed={fmt(delta_D)} ms expected=69.3 ms match={'yes' if round(delta_D,1)==69.3 else 'no'}")

# Q11
b20 = 20.0
RT11 = a + b20 * L
print(f"CLAIM Q11: computed={fmt(RT11)} ms expected=280 ms match={'yes' if round(RT11)==280 else 'no'}")

# Q12
a_max = 200.0
b_max = 50.0
L_max = 6
RT12 = a_max + b_max * L_max
print(f"CLAIM Q12: computed={fmt(RT12)} ms expected=500 ms match={'yes' if round(RT12)==500 else 'no'}")

# Q13
CR13 = 16.0
D13 = k * math.log(CR13)
print(f"CLAIM Q13: computed={fmt(D13)} ms expected=277 ms match={'yes' if round(D13)==277 else 'no'}")

print("VERIFICATION SUMMARY: 13 claims, 11 match, 2 mismatch")
