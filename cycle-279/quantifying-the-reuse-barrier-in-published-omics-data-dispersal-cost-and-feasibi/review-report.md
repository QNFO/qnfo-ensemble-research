{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Model‑selection cost considerations from the LiveBench audit [9] and [10] provide a concrete monetary scaling. DeepSeek V4 Pro 0813 achieves the best mathematics‑price performance at a reported $0.044$ USD per benchmark run and supports a $1\\,\\text{M}$‑token context window. Assuming a benchmark run processes the full $1\\,\\text{M}$ tokens, the implied per‑token price is \\[c_{\\text{token}}=\\frac{0.044\\ \\text{USD}}{1\\,000\\,000}=4.4\\times10^{-8}\\ \\text{USD/token}.\\] Applying this rate to the full retrieval cost for $S=10$ gives a monetary estimate of \\[\\text{Cost}_{\\text{USD}}=169\\,400\\times4.4\\times10^{-8}\\approx7.5\\times10^{-3}\\ \\text{USD},\\] i.e. less than one cent per paper.",
      "reason": "The claim about DeepSeek V4 Pro performance and the monetary scaling is not supported by any supplied bibliography entry; [9] and [10] are QNFO links without such details. This violates citation integrity and quantitative honesty.",
      "fix": "Remove the unsupported DeepSeek and LiveBench statements or replace them with a projection explicitly labeled as an assumption without citing [9] or [10]."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The background and related work section discusses only six cited works ([1], [2], [3], [4], [5], [7]), failing to meet the required minimum of eight works.",
      "reason": "Section 2 must discuss at least eight bibliography works with specific points derived from their excerpts. The current text omits works [6] and [8], violating the literature coverage requirement.",
      "fix": "Add concise discussions of works [6] and [8], citing specific methods or results from their excerpts, to reach at least eight works."
    }
  ],
  "soft": []
}