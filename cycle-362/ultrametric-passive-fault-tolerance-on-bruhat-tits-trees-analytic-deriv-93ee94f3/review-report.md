{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "- **C6.** Passive logical failure $P_{\\mathrm{pass}}=9.97\\times10^{-6}$ for $\\varepsilon=10^{-3}$.",
      "reason": "The paper presents a specific numerical value for the passive logical failure probability that is not derived in the analysis nor labeled as a projection with stated assumptions. The derived value in Section 4 is $5.992003\\times10^{-6}$, so this claim is unsupported.",
      "fix": "Replace the unsupported value with the derived result $5.992003\\times10^{-6}$ and adjust the contribution description accordingly."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "- **C4.** Quantitative comparison of logical error suppression with surface‑code benchmarks, showing a suppression factor $S\\approx100$ (Section 5).",
      "reason": "The suppression factor $S\\approx100$ is presented without derivation or projection label, while the analytic calculation yields $S\\approx166.9$. This quantitative claim is unsupported.",
      "fix": "Replace the unsupported suppression factor with the derived value $S\\approx166.9$ and reference the appropriate section."
    }
  ],
  "soft": []
}