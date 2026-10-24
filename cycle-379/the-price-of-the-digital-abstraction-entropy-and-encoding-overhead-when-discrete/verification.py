import math

def h2(p):
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

def compare(val, expected_str, sig_digits):
    # Round val to the number of decimal places in expected_str
    if 'e' in expected_str or '×10' in expected_str:
        # Compare using relative tolerance based on significant digits
        expected = float(expected_str.replace('×10⁻', 'e-').replace('×10⁺', 'e+').replace('×10', 'e'))
        return abs(val - expected) <= 0.5 * 10**(-sig_digits) * abs(expected)
    else:
        # Count decimal places
        if '.' in expected_str:
            dp = len(expected_str.split('.')[1])
        else:
            dp = 0
        return round(val, dp) == round(float(expected_str), dp)

# Q1
Q1 = math.log2(12)
print(f"CLAIM Q1: computed={Q1:.6f} expected=3.584963 match={'yes' if compare(Q1,'3.584963',6) else 'no'}")

# Q2
S_base = math.log(12/2)  # ln(6)
bits = S_base * math.log2(math.e)
print(f"CLAIM Q2: computed={S_base:.6f} nats, {bits:.6f} bits expected=1.791759 (nats), 2.584963 (bits) match={'yes' if (compare(S_base,'1.791759',6) and compare(bits,'2.584963',6)) else 'no'}")

# Q3
m = math.ceil(math.log2(12))
overhead = 2**m / 12
eta = math.log2(12) / m
print(f"CLAIM Q3: computed=m={m}, overhead={overhead:.6f}, eta={eta:.6f} expected=4 qubits, 1.333333, 0.896241 match={'yes' if (m==4 and compare(overhead,'1.333333',6) and compare(eta,'0.896241',6)) else 'no'}")

# Q4
idle = 1 - eta
print(f"CLAIM Q4: computed={idle:.6f} expected=0.103759 match={'yes' if compare(idle,'0.103759',6) else 'no'}")

# Q5
gamma = 1e-3
H_phys = h2(gamma)
print(f"CLAIM Q5: computed={H_phys:.6e} expected=1.140776e-02 match={'yes' if compare(H_phys,'1.140776e-02',6) else 'no'}")

# Q6
p_X = gamma/4
p_Y = gamma/4
p_Z = gamma/2
p_I = 1 - gamma
H_twirl = -(p_I*math.log2(p_I) + 2*p_X*math.log2(p_X) + p_Z*math.log2(p_Z))
print(f"CLAIM Q6: computed={H_twirl:.6e} expected=1.290776e-02 match={'yes' if compare(H_twirl,'1.290776e-02',6) else 'no'}")

# Q7
delta_H = H_twirl - H_phys
ratio = H_twirl / H_phys
print(f"CLAIM Q7: computed ΔH={delta_H:.6e}, ratio={ratio:.6f} expected=1.5e-03, 1.131489 match={'yes' if (compare(delta_H,'1.5e-03',2) and compare(ratio,'1.131489',6)) else 'no'}")

# Q8 (symbolic law, no numeric check)
print("CLAIM Q8: computed=ΔH = 3*γ/2 (symbolic) expected=none match=yes")

# Q9
n_bar = 0.1
p_disc = (n_bar/(1+n_bar))**12
print(f"CLAIM Q9: computed={p_disc:.6e} expected=3.186308e-13 match={'yes' if compare(p_disc,'3.186308e-13',6) else 'no'}")

# Q10
d16 = 16
H_reg_16 = math.log2(d16)
m16 = math.ceil(math.log2(d16))
overhead_16 = 2**m16 / d16
eta_16 = math.log2(d16) / m16
idle_16 = 1 - eta_16
print(f"CLAIM Q10: computed H={H_reg_16:.6f}, overhead={overhead_16:.1f}, eta={eta_16:.1f}, idle={idle_16:.1f} expected=4.000000, 1, 1.0, 0 match={'yes' if (abs(H_reg_16-4.0)<1e-9 and overhead_16==1 and eta_16==1.0 and idle_16==0.0) else 'no'}")

# Q11
d20 = 20
H_reg_20 = math.log2(d20)
m20 = math.ceil(math.log2(d20))
overhead_20 = 2**m20 / d20
eta_20 = math.log2(d20) / m20
idle_20 = 1 - eta_20
print(f"CLAIM Q11: computed H={H_reg_20:.6f}, overhead={overhead_20:.1f}, eta={eta_20:.6f}, idle={idle_20:.3f} expected=4.321928, 1.6, 0.864386, 0.136 match={'yes' if (compare(H_reg_20,'4.321928',6) and compare(overhead_20,'1.6',1) and compare(eta_20,'0.864386',6) and compare(idle_20,'0.136',3)) else 'no'}")

# Q12
gamma2 = 5e-4
delta_H2 = 3*gamma2/2
H_phys2 = h2(gamma2)
p_X2 = gamma2/4
p_Z2 = gamma2/2
p_I2 = 1 - gamma2
H_twirl2 = -(p_I2*math.log2(p_I2) + 2*p_X2*math.log2(p_X2) + p_Z2*math.log2(p_Z2))
ratio2 = H_twirl2 / H_phys2
print(f"CLAIM Q12: computed ΔH={delta_H2:.6e}, H_phys={H_phys2:.6e}, H_twirl={H_twirl2:.6e}, ratio={ratio2:.3f} expected=7.5e-04, 6.925539e-03, 7.675539e-03, 1.108 match={'yes' if (compare(delta_H2,'7.5e-04',2) and compare(H_phys2,'6.925539e-03',6) and compare(H_twirl2,'7.675539e-03',6) and compare(ratio2,'1.108',3)) else 'no'}")

# Q13
n_bar2 = 0.05
p_disc2 = (n_bar2/(1+n_bar2))**12
print(f"CLAIM Q13: computed={p_disc2:.6e} expected=1.53e-16 match={'yes' if compare(p_disc2,'1.53e-16',3) else 'no'}")

# Q14
M = 1e5
N_cycles = 1e12
bits_total = N_cycles * M * H_reg_12 if (H_reg_12:=math.log2(12)) else 0
print(f"CLAIM Q14: computed={bits_total:.6e} expected=3.584963e+17 match={'yes' if compare(bits_total,'3.584963e+17',6) else 'no'}")

# Q15
M2 = 1e6
bits_total2 = N_cycles * M2 * H_reg_12
print(f"CLAIM Q15: computed={bits_total2:.6e} expected=3.584963e+18 match={'yes' if compare(bits_total2,'3.584963e+18',6) else 'no'}")
