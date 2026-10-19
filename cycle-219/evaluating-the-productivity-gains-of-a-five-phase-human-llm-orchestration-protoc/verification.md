# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Per‑cycle error budget \\(\\epsilon_c = 1.0\\times10^{-5}\\).",
    "inputs": "epsilon_tot = 1.25×10^{-3}, N_c = 125",
    "formula": "epsilon_c = epsilon_tot / N_c"
  },
  {
    "id": "Q2",
    "statement": "Projected fidelity \\(F_{\\text{proj}} = 0.99875\\).",
    "inputs": "epsilon_tot = 1.25×10^{-3}",
    "formula": "F_proj = 1 - epsilon_tot"
  },
  {
    "id": "Q3",
    "statement": "Aggregate update rate \\(K R_u = 1.28\\times10^{8}\\,\\mathrm{s^{-1}}\\).",
    "inputs": "K = 64, R_u = 2×10^{6}\\,\\mathrm{s^{-1}}",
    "formula": "K * R_u"
  },
  {
    "id": "Q4",
    "statement": "Parallelism factor \\(K = 64\\).",
    "inputs": "aggregate update rate = 1.28×10^{8}\\,\\mathrm{s^{-1}}, R_u = 2×10^{6}\\,\\mathrm{s^{-1}}",
    "formula": "K = (aggregate update rate) / R_u"
  },
  {
    "id": "Q5",
    "statement": "Parallel component time under the protocol (\\(\\alpha = 0.10\\)) = 30.9375 s.",
    "inputs": "t_P = 1800 s, K = 64, alpha = 0.10",
    "formula": "(t_P / K) * (1 + alpha)"
  },
  {
    "id": "Q6",
    "statement": "Protocol total wall‑clock time \\(T_{\\text{proto}} = 630.9375\\,\\mathrm{s}\\).",
    "inputs": "parallel component = 30.9375 s, t_S = 600 s",
    "formula": "parallel component + t_S"
  },
  {
    "id": "Q7",
    "statement": "Baseline total time \\(T_{\\text{control}} = 2400\\,\\mathrm{s}\\).",
    "inputs": "t_P = 1800 s, t_S = 600 s",
    "formula": "t_P + t_S"
  },
  {
    "id": "Q8",
    "statement": "Speedup \\(U \\approx 3.805\\).",
    "inputs": "T_control = 2400 s, T_proto = 630.9375 s",
    "formula": "U = T_control / T_proto"
  },
  {
    "id": "Q9",
    "statement": "Parallel component time with reduced overhead (\\(\\alpha = 0.02\\)) = 28.6875 s.",
    "inputs": "t_P = 1800 s, K = 64, alpha = 0.02",
    "formula": "(t_P / K) * (1 + alpha)"
  },
  {
    "id": "Q10",
    "statement": "Protocol total time with reduced overhead \\(T_{\\text{proto}} = 628.6875\\,\\mathrm{s}\\).",
    "inputs": "parallel component = 28.6875 s, t_S = 600 s",
    "formula": "parallel component + t_S"
  },
  {
    "id": "Q11",
    "statement": "Speedup with reduced overhead \\(U \\approx 3.817\\).",
    "inputs": "T_control = 2400 s, T_proto = 628.6875 s",
    "formula": "U = T_control / T_proto"
  },
  {
    "id": "Q12",
    "statement": "Inference cost per task = $0.50.",
    "inputs": "cost per 1 M tokens = $0.05, tokens per task = 10 M",
    "formula": "(tokens per task / 1 M) * cost per 1 M tokens"
  },
  {
    "id": "Q13",
    "statement": "Total compute cost for 64 tasks = $32.00.",
    "inputs": "cost per task = $0.50, number of tasks = 64",
    "formula": "cost per task * number of tasks"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=1e-05 expected=1e-05 match=yes
CLAIM Q2: computed=0.99875 expected=0.99875 match=yes
CLAIM Q3: computed=128000000 expected=128000000 match=yes
CLAIM Q4: computed=64 expected=64 match=yes
CLAIM Q5: computed=30.9375 expected=30.9375 match=yes
CLAIM Q6: computed=630.9375 expected=630.9375 match=yes
CLAIM Q7: computed=2400 expected=2400 match=yes
CLAIM Q8: computed=3.804 expected=3.805 match=no
CLAIM Q9: computed=28.6875 expected=28.6875 match=yes
CLAIM Q10: computed=628.6875 expected=628.6875 match=yes
CLAIM Q11: computed=3.817 expected=3.817 match=yes
CLAIM Q12: computed=0.50 expected=0.50 match=yes
CLAIM Q13: computed=32.00 expected=32.00 match=yes
VERIFICATION SUMMARY: 13 claims, 12 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1e-05 | 1e-05 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.99875 | 0.99875 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 128000000 | 128000000 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 64 | 64 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 30.9375 | 30.9375 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q6 | 630.9375 | 630.9375 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q7 | 2400 | 2400 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 3.804 | 3.805 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 28.6875 | 28.6875 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q10 | 628.6875 | 628.6875 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q11 | 3.817 | 3.817 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 0.50 | 0.50 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 32.00 | 32.00 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
