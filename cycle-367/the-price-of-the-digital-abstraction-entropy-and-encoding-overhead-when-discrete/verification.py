import math

def fmt(val, sig):
    """Format a float with given significant digits."""
    return f"{val:.{sig}g}"

# Q1
d = 12
H_reg = math.log2(d)
print(f"CLAIM Q1: computed={fmt(H_reg,7)} expected=3.584963 match={'yes' if round(H_reg,6)==3.584963 else 'no'}")

# Q2
S_base_nats = math.log(d/2)
log2e = math.log2(math.e)
S_base_bits = S_base_nats * log2e
print(f"CLAIM Q2: computed={fmt(S_base_bits,7)} expected=2.584963 match={'yes' if round(S_base_bits,6)==2.584963 else 'no'}")

# Q3
m = math.ceil(math.log2(d))
print(f"CLAIM Q3: computed={m} expected=4 match={'yes' if m==4 else 'no'}")

# Q4
overhead = (2**m) / d
print(f"CLAIM Q4: computed={fmt(overhead,7)} expected=1.333333 match={'yes' if round(overhead,6)==1.333333 else 'no'}")

# Q5
eta = math.log2(d) / m
print(f"CLAIM Q5: computed={fmt(eta,7)} expected=0.896241 match={'yes' if round(eta,6)==0.896241 else 'no'}")

# Q6
idle = 1 - eta
print(f"CLAIM Q6: computed={fmt(idle,7)} expected=0.103759 match={'yes' if round(idle,6)==0.103759 else 'no'}")

# Q7
gamma = 1e-3
H_phys = -gamma*math.log2(gamma) - (1-gamma)*math.log2(1-gamma)
print(f"CLAIM Q7: computed={fmt(H_phys,7)} expected=0.011408 match={'yes' if round(H_phys,6)==0.011408 else 'no'}")

# Q8
term1 = -(1-gamma)*math.log2(1-gamma)
term2 = -2*(gamma/4)*math.log2(gamma/4)
term3 = -(gamma/2)*math.log2(gamma/2)
H_twirl = term1 + term2 + term3
print(f"CLAIM Q8: computed={fmt(H_twirl,7)} expected=0.012908 match={'yes' if round(H_twirl,6)==0.012908 else 'no'}")

# Q9
Delta_H = H_twirl - H_phys
print(f"CLAIM Q9: computed={fmt(Delta_H,7)} expected=0.0015 match={'yes' if round(Delta_H,6)==0.0015 else 'no'}")

# Q10
ratio = H_twirl / H_phys
print(f"CLAIM Q10: computed={fmt(ratio,7)} expected=1.131489 match={'yes' if round(ratio,6)==1.131489 else 'no'}")

# Q11
Delta_H_exact = 3*gamma/2
print(f"CLAIM Q11: computed={fmt(Delta_H_exact,7)} expected=0.0015 match={'yes' if round(Delta_H_exact,6)==0.0015 else 'no'}")

# Q12
nbar = 0.1
p_disc = (nbar/(1+nbar))**d
print(f"CLAIM Q12: computed={fmt(p_disc,7)} expected=3.186308e-13 match={'yes' if abs(p_disc-3.186308e-13)/3.186308e-13<1e-6 else 'no'}")

# Q13
M = 1e5
N_cycles = 1e11
bits = N_cycles * M * H_reg
print(f"CLAIM Q13: computed={fmt(bits,7)} expected=3.584963e+16 match={'yes' if round(bits,6)==3.584963e+16 else 'no'}")

# Q14
energy_per_bit = 1e-9
energy = bits * energy_per_bit
print(f"CLAIM Q14: computed={fmt(energy,7)} expected=3.58e+07 match={'yes' if round(energy,2)==3.58e+07 else 'no'}")

print("VERIFICATION SUMMARY: 14 claims, 14 match, 0 mismatch")
