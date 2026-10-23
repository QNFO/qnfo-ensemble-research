import math

# Q1
H_reg = math.log2(12)
print(f"CLAIM Q1: computed={H_reg:.9g} expected=3.584963 match={'yes' if round(H_reg,6)==3.584963 else 'no'}")

# Q2
S_base = math.log(12/2)
print(f"CLAIM Q2: computed={S_base:.9g} expected=1.791759 match={'yes' if round(S_base,6)==1.791759 else 'no'}")

# Q3
bits = S_base * (1/math.log(2))  # log2(e) = 1/ln2
print(f"CLAIM Q3: computed={bits:.9g} expected=2.584963 match={'yes' if round(bits,6)==2.584963 else 'no'}")

# Q4
m = math.ceil(math.log2(12))
print(f"CLAIM Q4: computed={m} expected=4 match={'yes' if m==4 else 'no'}")

# Q5
dim = 2**m
print(f"CLAIM Q5: computed={dim} expected=16 match={'yes' if dim==16 else 'no'}")

# Q6
wasted = dim - 12
print(f"CLAIM Q6: computed={wasted} expected=4 match={'yes' if wasted==4 else 'no'}")

# Q7
overhead = dim / 12
print(f"CLAIM Q7: computed={overhead:.9g} expected=1.333333 match={'yes' if round(overhead,6)==1.333333 else 'no'}")

# Q8
eta = math.log2(12) / m
print(f"CLAIM Q8: computed={eta:.9g} expected=0.896241 match={'yes' if round(eta,6)==0.896241 else 'no'}")

# Q9
idle = 1 - eta
print(f"CLAIM Q9: computed={idle:.9g} expected=0.103759 match={'yes' if round(idle,6)==0.103759 else 'no'}")

# Q10
gamma = 1e-3
p_X = p_Y = gamma/4
p_Z = gamma/2
p_I = 1 - gamma
print(f"CLAIM Q10: computed=p_X={p_X:.9g},p_Y={p_Y:.9g},p_Z={p_Z:.9g},p_I={p_I:.9g} expected=p_X=2.5e-4,p_Y=2.5e-4,p_Z=5e-4,p_I=0.999 match={'yes' if (abs(p_X-2.5e-4)<1e-12 and abs(p_Z-5e-4)<1e-12 and abs(p_I-0.999)<1e-12) else 'no'}")

# Q11
H_phys = -gamma*math.log2(gamma) - (1-gamma)*math.log2(1-gamma)
print(f"CLAIM Q11: computed={H_phys:.9g} expected=1.140776e-2 match={'yes' if abs(H_phys-1.140776e-2)<1e-9 else 'no'}")

# Q12
H_twirl = -(p_I*math.log2(p_I) + 2*p_X*math.log2(p_X) + p_Z*math.log2(p_Z))
print(f"CLAIM Q12: computed={H_twirl:.9g} expected=1.290776e-2 match={'yes' if abs(H_twirl-1.290776e-2)<1e-9 else 'no'}")

# Q13
Delta = H_twirl - H_phys
ratio = H_twirl / H_phys
print(f"CLAIM Q13: computed=Delta={Delta:.9g},ratio={ratio:.9g} expected=Delta=1.500000e-3,ratio=1.131489 match={'yes' if (abs(Delta-1.5e-3)<1e-9 and abs(ratio-1.131489)<1e-6) else 'no'}")

# Q14
Delta_exact = 3*gamma/2
print(f"CLAIM Q14: computed={Delta_exact:.9g} expected=1.5e-3 match={'yes' if abs(Delta_exact-1.5e-3)<1e-12 else 'no'}")

# Q15
n_bar = 0.1
d = 12
p_disc = (n_bar/(1+n_bar))**d
print(f"CLAIM Q15: computed={p_disc:.9g} expected=3.186308e-13 match={'yes' if abs(p_disc-3.186308e-13)<1e-20 else 'no'}")

# Q16
M = 1e4
N_cycles = 1e10
total = N_cycles * M * H_reg
print(f"CLAIM Q16: computed={total:.9g} expected=3.584963e14 match={'yes' if abs(total-3.584963e14)<1e5 else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, X match, Y mismatch")
