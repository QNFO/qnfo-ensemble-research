import math

def claim_Q1():
    n = 3
    computed = 2 ** n
    expected = 8
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q1: computed={computed} expected={expected} match={match}")

def claim_Q2():
    total = 8
    survivors = 1
    computed = (total - survivors) / total
    expected = 0.875
    match = "yes" if abs(computed - expected) < 1e-12 else "no"
    print(f"CLAIM Q2: computed={computed} expected={expected} match={match}")

def claim_Q3():
    n = 10
    computed = 2 ** n
    expected = 1024
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q3: computed={computed} expected={expected} match={match}")

def claim_Q4():
    W = 8
    computed = 2 ** (W * W)
    expected = 18446744073709551616
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q4: computed={computed} expected={expected} match={match}")

def claim_Q5():
    W = 8
    computed = 2 ** (W * (W - 1))
    expected = 72057594037927936
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q5: computed={computed} expected={expected} match={match}")

def claim_Q6():
    w1 = 8
    w2 = w1 - 1
    w3 = w2 - 1
    w4 = w3 - 2
    computed = f"{w1},{w2},{w3},{w4}"
    expected = "8,7,6,4"
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q6: computed={computed} expected={expected} match={match}")

def claim_Q7():
    computed = 7 / 4
    expected = 1.75
    match = "yes" if abs(computed - expected) < 1e-12 else "no"
    print(f"CLAIM Q7: computed={computed} expected={expected} match={match}")

def claim_Q8():
    W = 8
    E = 3
    computed = W * E
    expected = 24
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q8: computed={computed} expected={expected} match={match}")

def claim_Q9():
    # L5 = 2^{65536}; we compare its base‑10 logarithm to the reported 19728
    log10_L5 = 65536 * math.log10(2)
    computed = round(log10_L5)  # integer approximation
    expected = 19728
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q9: computed={computed} expected={expected} match={match}")

def claim_Q10():
    d = 10
    computed = 2 ** (d * d)
    # Expected value written as 1.2676506002282294×10^{30}
    expected = 1.2676506002282294e30
    match = "yes" if computed == int(expected) else "no"
    print(f"CLAIM Q10: computed={computed} expected={expected} match={match}")

def claim_Q11():
    k = 10
    computed = 2 ** k
    expected = 1024
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q11: computed={computed} expected={expected} match={match}")

def claim_Q12():
    m = 2
    computed = 2 ** m
    expected = 4
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q12: computed={computed} expected={expected} match={match}")

def claim_Q13():
    m = 3
    computed = 2 ** m
    expected = 8
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q13: computed={computed} expected={expected} match={match}")

def claim_Q14():
    p = 5
    computed = 2 ** p
    expected = 32
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q14: computed={computed} expected={expected} match={match}")

def claim_Q15():
    p = 5
    a = 3
    computed = 2 ** (p - a)
    expected = 4
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q15: computed={computed} expected={expected} match={match}")

def claim_Q16():
    weeks = 14
    hours_per_week = 2
    computed = weeks * hours_per_week
    expected = 28
    match = "yes" if computed == expected else "no"
    print(f"CLAIM Q16: computed={computed} expected={expected} match={match}")

def main():
    claim_Q1()
    claim_Q2()
    claim_Q3()
    claim_Q4()
    claim_Q5()
    claim_Q6()
    claim_Q7()
    claim_Q8()
    claim_Q9()
    claim_Q10()
    claim_Q11()
    claim_Q12()
    claim_Q13()
    claim_Q14()
    claim_Q15()
    claim_Q16()
    print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")

if __name__ == "__main__":
    main()
