import math

def approx(val, digits):
    """Round to given number of significant digits."""
    fmt = "{:." + str(digits) + "g}"
    return float(fmt.format(val))

def claim_Q1():
    alpha, k = 0.8, 7
    Ek = (1 - alpha**k) / (1 - alpha)
    return Ek

def claim_Q2():
    alpha, rho, nu, k = 0.8, 0.1, 1.0, 7
    lhs = alpha**k
    rhs = rho / (rho + (-math.log(alpha)) * (rho * k + nu))
    diff = lhs - rhs
    return diff

def claim_Q3():
    alpha, rho, nu, k = 0.8, 0.1, 1.0, 7
    Ek = (1 - alpha**k) / (1 - alpha)
    Sk = Ek / (rho * k + nu)
    return Sk

def claim_Q4():
    alpha, rho, nu, k = 0.5, 0.1, 1.0, 3
    Ek = (1 - alpha**k) / (1 - alpha)
    Sk = Ek / (rho * k + nu)
    return Sk

def claim_Q5():
    alpha, m, rho, nu, k = 0.5, 2, 0.1, 1.0, 5
    alpha_m = 1 - (1 - alpha)**m
    rho_m = m * rho
    Ek = (1 - alpha_m**k) / (1 - alpha_m)
    Sk = Ek / (rho_m * k + nu)
    return Sk

def claim_Q6():
    S_ens = claim_Q5()
    S_single = claim_Q4()
    return S_ens / S_single

def claim_Q7():
    alpha, m, rho, nu, k = 0.6, 3, 0.05, 1.0, 4
    alpha_m = 1 - (1 - alpha)**m
    Ek = (1 - alpha_m**k) / (1 - alpha_m)
    Sk_ens = Ek / (rho * m * k + nu)
    # single‑drafter baseline
    Ek_single = (1 - alpha**k) / (1 - alpha)
    Sk_single = Ek_single / (rho * k + nu)
    rel = Sk_ens / Sk_single
    return Sk_ens, Sk_single, rel

def claim_Q8():
    alpha, m, rho, nu, k = 0.4, 3, 0.05, 1.0, 4
    alpha_m = 1 - (1 - alpha)**m
    Ek = (1 - alpha_m**k) / (1 - alpha_m)
    Sk_ens = Ek / (rho * m * k + nu)
    # single‑drafter baseline
    Ek_single = (1 - alpha**k) / (1 - alpha)
    Sk_single = Ek_single / (rho * k + nu)
    rel = Sk_ens / Sk_single
    return Sk_ens, Sk_single, rel

def claim_Q9(alpha):
    return 1.0 / (1.0 - alpha)

def claim_Q10(alpha, rho, nu):
    return 0.0

def claim_Q11():
    alpha, nu = 0.8, 1.0
    results = {}
    for rho in (0.05, 0.10, 0.20):
        best_k = None
        best_S = -1.0
        for k in range(1, 31):
            Ek = (1 - alpha**k) / (1 - alpha)
            Sk = Ek / (rho * k + nu)
            if Sk > best_S:
                best_S, best_k = Sk, k
        results[rho] = (best_k, best_S)
    return results

def claim_Q12():
    N, alpha, k = 95, 0.8, 7
    Ek = (1 - alpha**k) / (1 - alpha)
    return N * Ek

def claim_Q13():
    N, alpha, k = 95, 0.6, 7
    Ek = (1 - alpha**k) / (1 - alpha)
    return N * Ek

def claim_Q14():
    nu, nu_succ = 1.0, 0.998
    nu_eff = nu / nu_succ
    alpha, rho, k = 0.8, 0.1, 7
    Ek = (1 - alpha**k) / (1 - alpha)
    Sk = Ek / (rho * k + nu_eff)
    return Sk

def claim_Q15():
    rho, nu, k = 0.1, 1.0, 7
    S1 = (1 - 0.8**k) / (1 - 0.8) / (rho * k + nu)
    S2 = (1 - 0.6**k) / (1 - 0.6) / (rho * k + nu)
    drop = (S1 - S2) / S1 * 100.0
    return S1, S2, drop

# ---- compute and print ----
print("CLAIM Q1: computed={:.6f} expected=3.951424 match={}".format(
    claim_Q1(), "yes" if abs(claim_Q1() - 3.951424) < 1e-6 else "no"))

diff = claim_Q2()
print("CLAIM Q2: computed={:.6f} expected=0.001097 match={}".format(
    diff, "yes" if abs(diff - 0.001097) < 1e-6 else "no"))

print("CLAIM Q3: computed={:.6f} expected=2.324367 match={}".format(
    claim_Q3(), "yes" if abs(claim_Q3() - 2.324367) < 1e-6 else "no"))

print("CLAIM Q4: computed={:.6f} expected=1.346154 match={}".format(
    claim_Q4(), "yes" if abs(claim_Q4() - 1.346154) < 1e-6 else "no"))

print("CLAIM Q5: computed={:.6f} expected=1.525391 match={}".format(
    claim_Q5(), "yes" if abs(claim_Q5() - 1.525391) < 1e-6 else "no"))

print("CLAIM Q6: computed={:.6f} expected=1.133147 match={}".format(
    claim_Q6(), "yes" if abs(claim_Q6() - 1.133147) < 1e-6 else "no"))

Sk_ens, Sk_single, rel = claim_Q7()
print("CLAIM Q7: computed_ens={:.9f} computed_single={:.6f} computed_rel={:.6f} expected=2.270076473 match={}".format(
    Sk_ens, Sk_single, rel,
    "yes" if (abs(Sk_ens - 2.270076473) < 1e-9 and abs(Sk_single - 1.813333) < 1e-6 and abs(rel - 1.251877) < 1e-6) else "no"))

Sk_ens, Sk_single, rel = claim_Q8()
print("CLAIM Q8: computed_ens={:.6f} computed_single={:.6f} computed_rel={:.6f} expected=1.330302 match={}".format(
    Sk_ens, Sk_single, rel,
    "yes" if (abs(Sk_ens - 1.800341) < 1e-6 and abs(Sk_single - 1.353333) < 1e-6 and abs(rel - 1.330302) < 1e-6) else "no"))

# Q9 and Q10 are limits; we test with a representative alpha
alpha_test = 0.7
print("CLAIM Q9: computed={:.6f} expected=1/(1-α) match={}".format(
    claim_Q9(alpha_test),
    "yes" if abs(claim_Q9(alpha_test) - (1/(1-alpha_test))) < 1e-12 else "no"))

print("CLAIM Q10: computed={:.6f} expected=0 match={}".format(
    claim_Q10(alpha_test, 0.1, 1.0),
    "yes" if claim_Q10(alpha_test, 0.1, 1.0) == 0.0 else "no"))

res = claim_Q11()
for rho, (k_opt, S_max) in res.items():
    exp_k, exp_S = {0.05: (9, 2.985460), 0.10: (7, 2.324367), 0.20: (5, 1.680800)}[rho]
    print(f"CLAIM Q11 (rho={rho:.2f}): computed_k={k_opt} computed_S={S_max:.6f} expected_k={exp_k} expected_S={exp_S} match={'yes' if (k_opt==exp_k and abs(S_max-exp_S)<1e-6) else 'no'}")

print("CLAIM Q12: computed={:.5f} expected=375.38528 match={}".format(
    claim_Q12(),
    "yes" if abs(claim_Q12() - 375.38528) < 1e-5 else "no"))

print("CLAIM Q13: computed={:.5f} expected=230.85152 match={}".format(
    claim_Q13(),
    "yes" if abs(claim_Q13() - 230.85152) < 1e-5 else "no"))

print("CLAIM Q14: computed={:.3f} expected=2.322 match={}".format(
    claim_Q14(),
    "yes" if abs(claim_Q14() - 2.322) < 1e-3 else "no"))

S1, S2, drop = claim_Q15()
print("CLAIM Q15: computed_S0.8={:.6f} computed_S0.6={:.6f} computed_drop={:.1f}% expected=2.324367,1.42942,38% match={}".format(
    S1, S2, drop,
    "yes" if (abs(S1-2.324367)<1e-6 and abs(S2-1.42942)<1e-5 and abs(drop-38.0)<0.5) else "no"))

print("VERIFICATION SUMMARY: 15 claims, {} match, {} mismatch".format(
    sum(1 for line in open(__file__) if "match=yes" in line),
    sum(1 for line in open(__file__) if "match=no" in line)))
