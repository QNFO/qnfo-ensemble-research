import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def format_scientific(x, sig):
    # format with given significant figures in scientific notation
    fmt = "{:." + str(sig-1) + "e}"
    return fmt.format(x)

def main():
    # Q1
    epsilon_tot = 1.25e-3
    N_c = 125
    epsilon_c = epsilon_tot / N_c
    exp1 = 1.0e-5
    match1 = "yes" if round_sig(epsilon_c, 2) == exp1 else "no"
    print(f"CLAIM Q1: computed={epsilon_c:.10g} expected={exp1:.10g} match={match1}")

    # Q2
    F_proj = 1 - epsilon_tot
    exp2 = 0.99875
    match2 = "yes" if round_sig(F_proj, 5) == exp2 else "no"
    print(f"CLAIM Q2: computed={F_proj:.10g} expected={exp2:.10g} match={match2}")

    # Q3
    K = 64
    R_u = 2e6
    agg_rate = K * R_u
    exp3 = 1.28e8
    match3 = "yes" if round_sig(agg_rate, 3) == exp3 else "no"
    print(f"CLAIM Q3: computed={agg_rate:.10g} expected={exp3:.10g} match={match3}")

    # Q4
    agg_rate_given = 1.28e8
    K_calc = agg_rate_given / R_u
    exp4 = 64
    match4 = "yes" if round(K_calc) == exp4 else "no"
    print(f"CLAIM Q4: computed={K_calc:.10g} expected={exp4} match={match4}")

    # Q5
    t_P = 1800
    alpha = 0.10
    parallel_time = (t_P / K) * (1 + alpha)
    exp5 = 30.9375
    match5 = "yes" if abs(parallel_time - exp5) < 1e-9 else "no"
    print(f"CLAIM Q5: computed={parallel_time:.10g} expected={exp5:.10g} match={match5}")

    # Q6
    t_S = 600
    T_proto = parallel_time + t_S
    exp6 = 630.9375
    match6 = "yes" if abs(T_proto - exp6) < 1e-9 else "no"
    print(f"CLAIM Q6: computed={T_proto:.10g} expected={exp6:.10g} match={match6}")

    # Q7
    T_control = t_P + t_S
    exp7 = 2400
    match7 = "yes" if T_control == exp7 else "no"
    print(f"CLAIM Q7: computed={T_control} expected={exp7} match={match7}")

    # Q8
    U = T_control / T_proto
    exp8 = 3.805
    # round to three decimal places as paper reports
    U_rounded = round(U, 3)
    match8 = "yes" if U_rounded == exp8 else "no"
    print(f"CLAIM Q8: computed={U_rounded:.3f} expected={exp8:.3f} match={match8}")

    # Q9
    alpha2 = 0.02
    parallel_time2 = (t_P / K) * (1 + alpha2)
    exp9 = 28.6875
    match9 = "yes" if abs(parallel_time2 - exp9) < 1e-9 else "no"
    print(f"CLAIM Q9: computed={parallel_time2:.10g} expected={exp9:.10g} match={match9}")

    # Q10
    T_proto2 = parallel_time2 + t_S
    exp10 = 628.6875
    match10 = "yes" if abs(T_proto2 - exp10) < 1e-9 else "no"
    print(f"CLAIM Q10: computed={T_proto2:.10g} expected={exp10:.10g} match={match10}")

    # Q11
    U2 = T_control / T_proto2
    exp11 = 3.817
    U2_rounded = round(U2, 3)
    match11 = "yes" if U2_rounded == exp11 else "no"
    print(f"CLAIM Q11: computed={U2_rounded:.3f} expected={exp11:.3f} match={match11}")

    # Q12
    cost_per_M = 0.05
    tokens = 10e6
    cost_task = (tokens / 1e6) * cost_per_M
    exp12 = 0.50
    match12 = "yes" if abs(cost_task - exp12) < 1e-9 else "no"
    print(f"CLAIM Q12: computed={cost_task:.2f} expected={exp12:.2f} match={match12}")

    # Q13
    num_tasks = 64
    total_cost = cost_task * num_tasks
    exp13 = 32.00
    match13 = "yes" if abs(total_cost - exp13) < 1e-9 else "no"
    print(f"CLAIM Q13: computed={total_cost:.2f} expected={exp13:.2f} match={match13}")

    # Summary
    total = 13
    matches = sum(1 for m in [match1,match2,match3,match4,match5,match6,match7,match8,match9,match10,match11,match12,match13] if m=="yes")
    mismatches = total - matches
    print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {mismatches} mismatch")

if __name__ == "__main__":
    main()
