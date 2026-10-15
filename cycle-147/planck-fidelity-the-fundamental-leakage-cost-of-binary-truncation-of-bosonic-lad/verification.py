import math

def sig(x, n):
    if x == 0:
        return 0.0
    from decimal import Decimal
    return round(x, n - 1 - int(math.floor(math.log10(abs(x)))))

results = []

# Q1: L = theta^4/2, theta = pi/2, expected 3.0440341
theta = math.pi / 2
q1 = theta**4 / 2
results.append(("Q1", q1, "3.0440341", 8))

# Q2: L2 = 8*(0.05)^2*sin^2(pi/2) = 0.02
q2 = 8 * (0.05)**2 * math.sin(math.pi / 2)**2
results.append(("Q2", q2, "0.02", 2))

# Q3: L2_avg = 8*(0.05)^2*(1/2) = 0.01
q3 = 8 * (0.05)**2 * 0.5
results.append(("Q3", q3, "0.01", 2))

# Q4: L2_avg = 4*(0.10)^2 = 0.04
q4 = 4 * (0.10)**2
results.append(("Q4", q4, "0.04", 2))

# Q5: P2_max = 2*r^2/(1+2*r^2), r=0.1, expected 1.96e-2
r = 0.1
q5 = 2 * r**2 / (1 + 2 * r**2)
results.append(("Q5", q5, "0.0196", 3))

# Q6: P2_avg = r^2/(1+2*r^2), expected 9.80e-3
q6 = r**2 / (1 + 2 * r**2)
results.append(("Q6", q6, "0.0098", 3))

# Q7: t_pi = 1/(2*f_Omega), f=20 MHz, expected 25 ns
f = 20e6
q7 = 1 / (2 * f) * 1e9  # in ns
results.append(("Q7", q7, "25", 2))

# Q8: S_Base(12) = ln(6), expected 1.7917595 nats
q8 = math.log(12 / 2)
results.append(("Q8", q8, "1.7917595", 8))

# Q9: bits = S_Base/ln(2), expected 2.5849625
q9 = math.log(6) / math.log(2)
results.append(("Q9", q9, "2.5849625", 8))

# Q10: f_disc = ln(6)/ln(12), expected 0.721057
q10 = math.log(6) / math.log(12)
results.append(("Q10", q10, "0.721057", 6))

# Q11: log2(12) = ln(12)/ln(2), expected 3.5849625
q11 = math.log(12) / math.log(2)
results.append(("Q11", q11, "3.5849625", 8))

# Q12: eta = 1 - f_disc, expected 0.278943
q12 = 1 - math.log(6) / math.log(12)
results.append(("Q12", q12, "0.278943", 6))

# Q13: S_Base(6) = ln(3) nats = ln(3)/ln(2) bits, expected 1.0986123 nats / 1.5849625 bits
q13n = math.log(3)
q13b = math.log(3) / math.log(2)
results.append(("Q13", q13n, "1.0986123", 8))
results.append(("Q13b", q13b, "1.5849625", 8))

# Q14: S_Base(4) = ln(2) nats = 1 bit
q14n = math.log(2)
q14b = math.log(2) / math.log(2)
results.append(("Q14", q14n, "0.6931472", 8))
results.append(("Q14b", q14b, "1", 1))

# Q15: f_disc(6) = ln(3)/ln(6), expected 0.613147
q15 = math.log(3) / math.log(6)
results.append(("Q15", q15, "0.613147", 6))

# Q16: crude projection (Omega/alpha)^2 at 0.1, 0.05, 0.2 -> 1.0e-2, 2.5e-3, 4.0e-2
q16a = 0.1**2
q16b = 0.05**2
q16c = 0.2**2
results.append(("Q16a", q16a, "0.01", 2))
results.append(("Q16b", q16b, "0.0025", 2))
results.append(("Q16c", q16c, "0.04", 2))

match_count = 0
for rid, computed, expected_str, nsig in results:
    expected = float(expected_str)
    match = "yes" if sig(computed, nsig) == expected else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {rid}: computed={computed:.8g} expected={expected_str} match={match}")

total = len(results)
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")
