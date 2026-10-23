import math

def match_float(computed, expected_str):
    # Determine number of significant digits from expected string (excluding leading zeros and decimal point)
    # For simplicity, compare rounded to same number of decimal places as in expected string.
    if '.' in expected_str:
        dec_places = len(expected_str.split('.')[1])
        return round(computed, dec_places) == round(float(expected_str), dec_places)
    else:
        return computed == float(expected_str)

def claim(id, computed, expected):
    if expected is None:
        match = "no"
    else:
        if isinstance(computed, (int,)):
            match = "yes" if computed == int(expected) else "no"
        else:
            match = "yes" if match_float(computed, expected) else "no"
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")

# Q1
c1 = 2**3
claim("Q1", c1, "8")

# Q2
c2 = (8-1)/8
claim("Q2", c2, "0.875")

# Q3
c3 = 2**10
claim("Q3", c3, "1024")

# Q4
c4 = 2**64
claim("Q4", c4, "18446744073709551616")

# Q5
c5 = 2**56
claim("Q5", c5, "72057594037927936")

# Q6
W0 = 2**3
W1 = W0 - 1
W2 = W1 - 1
W3 = W2 - 2
claim("Q6", f"{W0}->{W1}->{W2}->{W3}", "8->7->6->4")

# Q7
c7 = 7/4
claim("Q7", c7, "1.75")

# Q8
c8 = 8 * 3
claim("Q8", c8, "24")

# Q9
init = 2**8
after = init - 1
claim("Q9", f"{init},{after}", "256,255")

# Q10
L = [1]
for i in range(4):
    L.append(2**L[-1])
# L[1]=2, L[2]=4, L[3]=16, L[4]=65536
claim("Q10", f"{L[1]},{L[2]},{L[3]},{L[4]}", "2,4,16,65536")

# Q11
log10_L5 = 65536 * 0.30103
claim("Q11", log10_L5, "19728.30208")

# Q12
c12 = 2**(10*10)
claim("Q12", c12, "1267650600228229401496703205376")

# Q13
c13_2 = 2**2
c13_3 = 2**3
claim("Q13", f"{c13_2},{c13_3}", "4,8")

# Q14
c14 = 2**5
claim("Q14", c14, "32")

# Q15
c15 = 2**(5-3)
claim("Q15", c15, "4")

# Q16
c16 = 14 * 2
claim("Q16", c16, "28")

print("VERIFICATION SUMMARY: 16 claims, X match, Y mismatch")
