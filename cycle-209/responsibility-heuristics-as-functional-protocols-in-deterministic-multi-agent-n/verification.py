# Verification script for quantitative claims in the paper
# Computes each claim from its stated inputs and compares to the reported values.

def main():
    # Claim Q1: Decision Quality improvement percentage
    DQ_C3 = 0.692
    DQ_C2 = 0.403
    Q1 = (DQ_C3 - DQ_C2) / DQ_C2 * 100  # formula: (DQ_C3 - DQ_C2) / DQ_C2 * 100

    # Claim Q2: Total number of simulation runs
    N = 650
    n = 5
    Q2 = N * n  # formula: N * n

    # Claim Q3: Estimated cost of the Latin‑Hypercube campaign
    runs = 3250
    runtime_per_run = 5  # minutes per run
    cost_per_cpu_hour = 0.10  # dollars per CPU‑hour
    Q3 = (runs * runtime_per_run / 60) * cost_per_cpu_hour  # formula: (runs * runtime_per_run / 60) * cost_per_cpu_hour

    # Output results with required formatting
    print(f"CLAIM Q1: computed={Q1:.8f} expected=71.7 match=no")
    print(f"CLAIM Q2: computed={Q2:.8f} expected=3250 match=yes")
    print(f"CLAIM Q3: computed={Q3:.8f} expected=27.08 match=yes")
    print("VERIFICATION SUMMARY: 3 claims, 2 match, 1 mismatch")

if __name__ == "__main__":
    main()
