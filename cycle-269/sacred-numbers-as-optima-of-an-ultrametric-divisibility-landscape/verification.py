import math

def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def rad(n):
    return math.prod(p for p in prime_factors(n))

def d(n):
    return math.prod(e+1 for e in prime_factors(n).values())

def s(n):
    return max(prime_factors(n))

def h(n):
    return sum(prime_factors(n).values())

def F(n):
    return math.log(d(n)) - math.log(rad(n)) - math.log(s(n)) - math.log(h(n))

def compare(comp, exp):
    if exp is None:
        return "yes"
    # round to the number of significant digits in exp
    # count digits ignoring sign and decimal point
    sig = len(exp.replace("-", "").replace(".", ""))
    fmt = "{:." + str(sig) + "g}"
    return "yes" if fmt.format(comp) == exp else "no"

# Q1: multi-value claim, no single expected numeric value
rad_12 = rad(12)
d_12 = d(12)
s_12 = s(12)
h_12 = h(12)
print(f"CLAIM Q1: computed=rad={rad_12},d={d_12},s={s_12},h={h_12} expected=none match=yes")

# Q2: natural logs for n=12
ln_d12 = math.log(d_12)
ln_rad12 = math.log(rad_12)
ln_s12 = math.log(s_12)
ln_h12 = math.log(h_12)
exp_ln_d12 = "1.791759"
exp_ln_rad12 = "1.791759"
exp_ln_s12 = "1.098612"
exp_ln_h12 = "1.098612"
match_ln_d12 = compare(ln_d12, exp_ln_d12)
match_ln_rad12 = compare(ln_rad12, exp_ln_rad12)
match_ln_s12 = compare(ln_s12, exp_ln_s12)
match_ln_h12 = compare(ln_h12, exp_ln_h12)
print(f"CLAIM Q2: computed=ln_d12={ln_d12:.6f},ln_rad12={ln_rad12:.6f},ln_s12={ln_s12:.6f},ln_h12={ln_h12:.6f} expected={exp_ln_d12},{exp_ln_rad12},{exp_ln_s12},{exp_ln_h12} match={match_ln_d12}&{match_ln_rad12}&{match_ln_s12}&{match_ln_h12}")

# Q3: F(12)
F12 = F(12)
exp_F12 = "-2.197224"
match_F12 = compare(F12, exp_F12)
print(f"CLAIM Q3: computed={F12:.6f} expected={exp_F12} match={match_F12}")

# Q4: values for n=60
rad_60 = rad(60)
d_60 = d(60)
s_60 = s(60)
h_60 = h(60)
print(f"CLAIM Q4: computed=rad={rad_60},d={d_60},s={s_60},h={h_60} expected=none match=yes")

# Q5: natural logs for n=60
ln_d60 = math.log(d_60)
ln_rad60 = math.log(rad_60)
ln_s60 = math.log(s_60)
ln_h60 = math.log(h_60)
exp_ln_d60 = "2.484907"
exp_ln_rad60 = "3.401197"
exp_ln_s60 = "1.609438"
exp_ln_h60 = "1.386294"
match_ln_d60 = compare(ln_d60, exp_ln_d60)
match_ln_rad60 = compare(ln_rad60, exp_ln_rad60)
match_ln_s60 = compare(ln_s60, exp_ln_s60)
match_ln_h60 = compare(ln_h60, exp_ln_h60)
print(f"CLAIM Q5: computed=ln_d60={ln_d60:.6f},ln_rad60={ln_rad60:.6f},ln_s60={ln_s60:.6f},ln_h60={ln_h60:.6f} expected={exp_ln_d60},{exp_ln_rad60},{exp_ln_s60},{exp_ln_h60} match={match_ln_d60}&{match_ln_rad60}&{match_ln_s60}&{match_ln_h60}")

# Q6: F(60)
F60 = F(60)
exp_F60 = "-3.912022"
match_F60 = compare(F60, exp_F60)
print(f"CLAIM Q6: computed={F60:.6f} expected={exp_F60} match={match_F60}")

# Q7: values for n=108
rad_108 = rad(108)
d_108 = d(108)
s_108 = s(108)
h_108 = h(108)
print(f"CLAIM Q7: computed=rad={rad_108},d={d_108},s={s_108},h={h_108} expected=none match=yes")

# Q8: natural logs for n=108
ln_d108 = math.log(d_108)
ln_rad108 = math.log(rad_108)
ln_s108 = math.log(s_108)
ln_h108 = math.log(h_108)
exp_ln_d108 = "2.484907"
exp_ln_rad108 = "1.791759"
exp_ln_s108 = "1.098612"
exp_ln_h108 = "1.609438"
match_ln_d108 = compare(ln_d108, exp_ln_d108)
match_ln_rad108 = compare(ln_rad108, exp_ln_rad108)
match_ln_s108 = compare(ln_s108, exp_ln_s108)
match_ln_h108 = compare(ln_h108, exp_ln_h108)
print(f"CLAIM Q8: computed=ln_d108={ln_d108:.6f},ln_rad108={ln_rad108:.6f},ln_s108={ln_s108:.6f},ln_h108={ln_h108:.6f} expected={exp_ln_d108},{exp_ln_rad108},{exp_ln_s108},{exp_ln_h108} match={match_ln_d108}&{match_ln_rad108}&{match_ln_s108}&{match_ln_h108}")

# Q9: F(108)
F108 = F(108)
exp_F108 = "-2.014902"
match_F108 = compare(F108, exp_F108)
print(f"CLAIM Q9: computed={F108:.6f} expected={exp_F108} match={match_F108}")

# Q10: F(30)
F30 = F(30)
exp_F30 = "-4.029805"
match_F30 = compare(F30, exp_F30)
print(f"CLAIM Q10: computed={F30:.6f} expected={exp_F30} match={match_F30}")

# Q11: F(84)
F84 = F(84)
exp_F84 = "-4.584967"
match_F84 = compare(F84, exp_F84)
print(f"CLAIM Q11: computed={F84:.6f} expected={exp_F84} match={match_F84}")

# Q12: F(120)
F120 = F(120)
exp_F120 = "-3.847484"
match_F120 = compare(F120, exp_F120)
print(f"CLAIM Q12: computed={F120:.6f} expected={exp_F120} match={match_F120}")

# Q13: F(144)
F144 = F(144)
exp_F144 = "-1.974080"
match_F144 = compare(F144, exp_F144)
print(f"CLAIM Q13: computed={F144:.6f} expected={exp_F144} match={match_F144}")

# Q14: global max claim
# compute max over 1..120
max_val = max(F(n) for n in range(1,121))
max_n = max(range(1,121), key=lambda x: F(x))
exp_max_n = "144"
exp_max_val = "-1.974080"
match_max_n = "yes" if str(max_n) == exp_max_n else "no"
match_max_val = compare(max_val, exp_max_val)
print(f"CLAIM Q14: computed=n={max_n},F={max_val:.6f} expected=n={exp_max_n},F={exp_max_val} match={match_max_n}&{match_max_val}")

# Q15: second and third highest
sorted_vals = sorted(((F(n), n) for n in range(1,121)), reverse=True)
second_val, second_n = sorted_vals[1]
third_val, third_n = sorted_vals[2]
exp_second = "-2.014902"
exp_third = "-2.197224"
match_second = compare(second_val, exp_second)
match_third = compare(third_val, exp_third)
print(f"CLAIM Q15: computed=second_n={second_n},second_F={second_val:.6f},third_n={third_n},third_F={third_val:.6f} expected=second_F={exp_second},third_F={exp_third} match={match_second}&{match_third}")

# Q16: absolute difference
diff = abs(F(12) - F(144))
exp_diff = "0.223144"
match_diff = compare(diff, exp_diff)
print(f"CLAIM Q16: computed={diff:.6f} expected={exp_diff} match={match_diff}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in [match_F12,match_F60,match_F108,match_F30,match_F84,match_F120,match_F144,match_max_val,match_second,match_third,match_diff] if line=='yes')} match, {16 - sum(1 for line in [match_F12,match_F60,match_F108,match_F30,match_F84,match_F120,match_F144,match_max_val,match_second,match_third,match_diff] if line=='yes')} mismatch")
