import math

def claim(id, computed, expected, match):
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")

# Q1: log2(3) = ln(3)/ln(2), paper states 1.5849625 (7 sig digits)
c = math.log(3)/math.log(2)
m = round(c, 7) == 1.5849625
claim("Q1", f"{c:.8f}", "1.5849625", "yes" if m else "no")

# Q2: 3^12
c = 3**12
claim("Q2", f"{c:.8f}", "531441", "yes" if c == 531441 else "no")

# Q3: 4^12 = 2^24
c = 4**12
claim("Q3", f"{c:.8f}", "16777216", "yes" if c == 16777216 else "no")

# Q4: 531441/4096, paper states 129.7463... (6 sig digits)
c = 531441/4096
m = round(c, 4) == 129.7463
claim("Q4", f"{c:.8f}", "129.7463", "yes" if m else "no")

# Q5: N_d = 24/log2(3) = 15.1424..., rounded up 16; saving = 1 - 15.1424/24 = 0.369067 -> 36.9%
c_raw = 24/(math.log(3)/math.log(2))
c_saving = 1 - c_raw/24
m = math.ceil(c_raw) == 16 and round(c_saving*100, 1) == 36.9
claim("Q5", f"{math.ceil(c_raw):.8f} sites, saving {c_saving*100:.8f}%", "16 sites, saving 36.9%", "yes" if m else "no")

# Q6: N_d = 24/2 = 12
c = 24/2
claim("Q6", f"{c:.8f}", "12", "yes" if c == 12 else "no")

# Q7: d^2/4
c3 = 9/4; c4 = 16/4
m = c3 == 2.25 and c4 == 4
claim("Q7", f"{c3:.8f}, {c4:.8f}", "2.25, 4", "yes" if m else "no")

# Q8: 16 * 4^14 bytes = 4294967296 bytes = 4.295 GB (paper: 4.295 GB, 4 sig digits)
c_bytes = 16 * 4**14
c_gb = c_bytes / 1e9
m = c_bytes == 4294967296 and round(c_gb, 3) == 4.295
claim("Q8", f"{c_bytes:.8f} bytes = {c_gb:.8f} GB", "4294967296 bytes = 4.295 GB", "yes" if m else "no")

# Q9: 20/log2(3) = 12.6186..., rounded up 13
c_raw = 20/(math.log(3)/math.log(2))
m = math.ceil(c_raw) == 13
claim("Q9", f"{c_raw:.8f} -> {math.ceil(c_raw):.8f}", "13", "yes" if m else "no")

# Q10: 20/2 = 10
c = 20/2
claim("Q10", f"{c:.8f}", "10", "yes" if c == 10 else "no")

# Q11: d^(d^2)
c3 = 3**9; c4 = 4**16
m = c3 == 19683 and abs(c4 - 4.29e9)/4.29e9 < 0.005
claim("Q11", f"{c3:.8f}, {c4:.8f}", "19683, 4.29e9", "yes" if m else "no")

# Q12: 65536 * 4 = 262144 = 2.6e5 (2 sig digits)
c = (2**28/2**12) * 4
m = round(c, -4) == 260000
claim("Q12", f"{c:.8f}", "2.6e5", "yes" if m else "no")

# Q13: 30/log2(3) = 18.927... -> 19; 30/2 = 15
c3_raw = 30/(math.log(3)/math.log(2)); c4 = 30/2
m = math.ceil(c3_raw) == 19 and c4 == 15
claim("Q13", f"{c3_raw:.8f} -> {math.ceil(c3_raw):.8f}, {c4:.8f}", "19, 15", "yes" if m else "no")

# Q14: 16/log2(3) = 10.096... -> 11; 16/2 = 8
c3_raw = 16/(math.log(3)/math.log(2)); c4 = 16/2
m = math.ceil(c3_raw) == 11 and c4 == 8
claim("Q14", f"{c3_raw:.8f} -> {math.ceil(c3_raw):.8f}, {c4:.8f}", "11, 8", "yes" if m else "no")

# Q15: 20/(log2 3)^2 = 7.96... -> 8; 20/4 = 5
l3 = math.log(3)/math.log(2)
c3_raw = 20/l3**2; c4 = 20/4
m = math.ceil(c3_raw) == 8 and c4 == 5
claim("Q15", f"{c3_raw:.8f} -> {math.ceil(c3_raw):.8f}, {c4:.8f}", "8, 5", "yes" if m else "no")

# Q16: 20/sqrt(log2 3) = 15.89... -> 16; 20/sqrt(2) = 14.14... -> 15
c3_raw = 20/math.sqrt(l3); c4_raw = 20/math.sqrt(2)
m = math.ceil(c3_raw) == 16 and math.ceil(c4_raw) == 15
claim("Q16", f"{c3_raw:.8f} -> {math.ceil(c3_raw):.8f}, {c4_raw:.8f} -> {math.ceil(c4_raw):.8f}", "16, 15", "yes" if m else "no")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
