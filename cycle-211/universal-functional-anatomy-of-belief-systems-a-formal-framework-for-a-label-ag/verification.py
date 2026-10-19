import math

def round_to(value, decimals):
    """Round value to a given number of decimal places."""
    factor = 10 ** decimals
    return round(value * factor) / factor

def format_number(value, decimals):
    """Format number with fixed decimal places (or as int if decimals==0)."""
    if decimals == 0:
        return str(int(value))
    else:
        fmt = "{:." + str(decimals) + "f}"
        return fmt.format(value)

# Q1
P = 5 ** 5
expected_Q1 = 3125
match_Q1 = P == expected_Q1
print(f"CLAIM Q1: computed={P} expected={expected_Q1} match={'yes' if match_Q1 else 'no'}")

# Q2 - binary profiles
P_binary = 2 ** 5
expected_Q2_binary = 32
match_Q2_binary = P_binary == expected_Q2_binary

# Q2 - resolution increase
increase = P / P_binary
expected_Q2_inc = 97.65625
inc_rounded = round_to(increase, 5)
match_Q2_inc = inc_rounded == expected_Q2_inc

print(f"CLAIM Q2 (binary): computed={P_binary} expected={expected_Q2_binary} match={'yes' if match_Q2_binary else 'no'}")
print(f"CLAIM Q2 (increase): computed={format_number(increase,5)} expected={expected_Q2_inc} match={'yes' if match_Q2_inc else 'no'}")

# Q3
instances = 9 * 10
expected_Q3 = 90
match_Q3 = instances == expected_Q3
print(f"CLAIM Q3: computed={instances} expected={expected_Q3} match={'yes' if match_Q3 else 'no'}")

# Q4
indoor = 7 / 9 * 100
expected_Q4 = 77.78
indoor_rounded = round_to(indoor, 2)
match_Q4 = indoor_rounded == expected_Q4
print(f"CLAIM Q4: computed={format_number(indoor,2)} expected={expected_Q4} match={'yes' if match_Q4 else 'no'}")

# Q5
outdoor = 2 / 9 * 100
expected_Q5 = 22.22
outdoor_rounded = round_to(outdoor, 2)
match_Q5 = outdoor_rounded == expected_Q5
print(f"CLAIM Q5: computed={format_number(outdoor,2)} expected={expected_Q5} match={'yes' if match_Q5 else 'no'}")

# Q6
entries = 1800 * 10
expected_Q6 = 18000
match_Q6 = entries == expected_Q6
print(f"CLAIM Q6: computed={entries} expected={expected_Q6} match={'yes' if match_Q6 else 'no'}")

# Q7
E_D = 5 * (1 - 1/5)
expected_Q7 = 4.0
E_D_rounded = round_to(E_D, 1)
match_Q7 = E_D_rounded == expected_Q7
print(f"CLAIM Q7: computed={format_number(E_D,1)} expected={expected_Q7} match={'yes' if match_Q7 else 'no'}")

# Q8
var_D = 5 * (1/5) * (1 - 1/5)
sigma = math.sqrt(var_D)
expected_var = 0.8
expected_sigma = 0.894427
var_rounded = round_to(var_D, 1)
sigma_rounded = round_to(sigma, 6)
match_var = var_rounded == expected_var
match_sigma = sigma_rounded == expected_sigma
print(f"CLAIM Q8 (variance): computed={format_number(var_D,1)} expected={expected_var} match={'yes' if match_var else 'no'}")
print(f"CLAIM Q8 (stddev): computed={format_number(sigma,6)} expected={expected_sigma} match={'yes' if match_sigma else 'no'}")

# Q9
p_e = 5 * (1/5)**2
expected_Q9 = 0.2
p_e_rounded = round_to(p_e, 1)
match_Q9 = p_e_rounded == expected_Q9
print(f"CLAIM Q9: computed={format_number(p_e,1)} expected={expected_Q9} match={'yes' if match_Q9 else 'no'}")

# Q10
p_o = 0.7
kappa = (p_o - p_e) / (1 - p_e)
expected_Q10 = 0.625
kappa_rounded = round_to(kappa, 3)
match_Q10 = kappa_rounded == expected_Q10
print(f"CLAIM Q10: computed={format_number(kappa,3)} expected={expected_Q10} match={'yes' if match_Q10 else 'no'}")

# Q11
comparisons = 4 * 5 * (math.comb(3,2))
expected_Q11 = 60
match_Q11 = comparisons == expected_Q11
print(f"CLAIM Q11: computed={comparisons} expected={expected_Q11} match={'yes' if match_Q11 else 'no'}")

# Q12
configs = 2 ** 5
expected_Q12 = 32
match_Q12 = configs == expected_Q12
print(f"CLAIM Q12: computed={configs} expected={expected_Q12} match={'yes' if match_Q12 else 'no'}")

# Q13
runs = configs * 10
expected_Q13 = 320
match_Q13 = runs == expected_Q13
print(f"CLAIM Q13: computed={runs} expected={expected_Q13} match={'yes' if match_Q13 else 'no'}")

# Q14
C_uniform = 0.5 ** 2
expected_Q14 = 0.25
C_uniform_rounded = round_to(C_uniform, 2)
match_Q14 = C_uniform_rounded == expected_Q14
print(f"CLAIM Q14: computed={format_number(C_uniform,2)} expected={expected_Q14} match={'yes' if match_Q14 else 'no'}")

# Q15
M = 100
# compute components
term1 = 1225 * 0.81
term2 = 2500 * 0.09
term3 = 1225 * 0.01
C_hetero = (term1 + term2 + term3) / 4950
expected_Q15 = 0.248384
C_hetero_rounded = round_to(C_hetero, 6)
match_Q15 = C_hetero_rounded == expected_Q15
print(f"CLAIM Q15: computed={format_number(C_hetero,6)} expected={expected_Q15} match={'yes' if match_Q15 else 'no'}")

# Q16
cost = 5 * 150 + 1200
expected_Q16 = 1950
match_Q16 = cost == expected_Q16
print(f"CLAIM Q16: computed={cost} expected={expected_Q16} match={'yes' if match_Q16 else 'no'}")

# Summary
total = 16
matches = sum([
    match_Q1,
    match_Q2_binary,
    match_Q2_inc,
    match_Q3,
    match_Q4,
    match_Q5,
    match_Q6,
    match_Q7,
    match_var,
    match_sigma,
    match_Q9,
    match_Q10,
    match_Q11,
    match_Q12,
    match_Q13,
    match_Q14,
    match_Q15,
    match_Q16
])
print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {total - matches} mismatch")
