import math

def check(cid, computed, expected, is_float=True):
    if expected is None:
        match = "no"
    elif is_float:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1
F1 = 1 - 25/100
results.append(check("Q1", F1, 0.75))

# Q2
F2 = 1 - 16/100
results.append(check("Q2", F2, 0.84))

# Q3
m3 = math.ceil(5/2)
v3 = (1/F1)**(1/m3)
results.append(check("Q3", v3, 1.100642416298209))

# Q4
m4 = math.ceil(7/2)
v4 = (1/F1)**(1/m4)
results.append(check("Q4", v4, 1.074569931823542))

# Q5
m5 = math.ceil(9/2)
v5 = (1/F1)**(1/m5)
results.append(check("Q5", v5, 1.0592238410488122))

# Q6
v6 = math.log(F1)/math.log(0.5)
results.append(check("Q6", v6, 0.4150374992788438))

# Q7
m7 = math.ceil(6/2)
v7 = (1/F2)**(1/m7)
results.append(check("Q7", v7, 1.0598398329483265))

# Q8
v8 = 4/130
results.append(check("Q8", v8, 0.03076923076923077))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n-m} mismatch")
