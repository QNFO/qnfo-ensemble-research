{
  "verdict": "revise",
  "hard": [
    {
      "id": "C1",
      "severity": "HARD",
      "claim": "the surface‑code threshold around $p_{\\text{th}}\\approx1.78\\times10^{-1}$ under depolarising noise [3].",
      "reason": "The excerpt for reference [3] does not contain any numerical threshold value; the claim is not supported by the cited source.",
      "fix": "Remove the specific numerical threshold or label it as a projection with an explicit assumption."
    },
    {
      "id": "C2",
      "severity": "HARD",
      "claim": "where $p_{\\mathrm{th}}=10^{-2}$ is the canonical surface‑code threshold [1]",
      "reason": "The excerpt for reference [1] provides a general description of QEC but does not give a threshold value of $10^{-2}$.",
      "fix": "Replace the citation with an assumption statement, e.g., \"we assume $p_{\\mathrm{th}}=10^{-2}$\"."
    },
    {
      "id": "C3",
      "severity": "HARD",
      "claim": "A $\\approx0.1$ is a constant fitted to Monte‑Carlo data in the literature [1].",
      "reason": "The excerpt for reference [1] does not contain any information about a constant $A\\approx0.1$.",
      "fix": "Remove the citation and treat $A$ as an assumed parameter."
    },
    {
      "id": "C4",
      "severity": "HARD",
      "claim": "temperature‑sensitivity coefficient $\\alpha=0.1\\,\\mathrm{K^{-1}}$ ... motivated by perturbative QEC theory [5].",
      "reason": "The excerpt for reference [5] is not provided; the paper cannot verify that $\\alpha$ is stated there.",
      "fix": "Label $\\alpha$ as an assumed value without citation."
    },
    {
      "id": "C5",
      "severity": "HARD",
      "claim": "thermal resistance $R_{\\mathrm{th}}=5\\,\\mathrm{K\\,W^{-1}}$ ... [7].",
      "reason": "The excerpt for reference [7] does not contain this numerical thermal resistance; the claim is unsupported.",
      "fix": "Remove the citation and present $R_{\\mathrm{th}}$ as an assumed parameter."
    },
    {
      "id": "C6",
      "severity": "HARD",
      "claim": "volumetric heat capacity $c=2\\times10^{-3}\\,\\mathrm{J\\,K^{-1}\\,cm^{-3}}$ ... [4].",
      "reason": "The excerpt for reference [4] does not provide this heat‑capacity value; the citation is unsupported.",
      "fix": "Treat $c$ as an assumed value without citing [4]."
    },
    {
      "id": "C7",
      "severity": "HARD",
      "claim": "activation energy $\\Delta E = 5\\times10^{-20}\\,\\mathrm{J}$ ... [4].",
      "reason": "The excerpt for reference [4] does not mention this activation energy; the citation is unsupported.",
      "fix": "Remove the citation and label $\\Delta E$ as an assumed parameter."
    },
    {
      "id": "C8",
      "severity": "HARD",
      "claim": "toric‑code threshold $p_{\\text{th}}=0.178$ reported in [3].",
      "reason": "The excerpt for reference [3] does not contain this numerical threshold; the claim is not supported by the cited source.",
      "fix": "Replace the citation with an assumption or remove the specific value."
    },
    {
      "id": "C9",
      "severity": "HARD",
      "claim": "Nonlinear QEC introduces the concept ... [9].",
      "reason": "No excerpt for reference [9] is provided; the paper cannot verify that this statement is supported.",
      "fix": "Either provide a supported statement from the excerpt or remove the citation."
    },
    {
      "id": "C10",
      "severity": "HARD",
      "claim": "baseline error probability $p_{0}=10^{-3}$ ... later used $p_{0}=10^{-4}$ in the heat‑capacity scenario without labeling as an assumption.",
      "reason": "Inconsistent use of $p_{0}$ creates a quantitative inconsistency; the later value is not derived or labeled as a projection.",
      "fix": "Use a single consistent $p_{0}$ value throughout or label the alternative value as an explicit assumption."
    },
    {
      "id": "C11",
      "severity": "HARD",
      "claim": "logical error probability $p_{\\mathrm{L}} \\approx 10^{-501}$ after substituting $d_{\\max}=1000$.",
      "reason": "Arithmetic yields $p_{\\mathrm{L}} = 0.1\\times10^{-500.5}=10^{-501.5}$; the reported exponent is off by a factor of $10^{0.5}$.",
      "fix": "Correct the reported value to $p_{\\mathrm{L}} \\approx 10^{-501.5}$ or adjust the calculation accordingly."
    }
  ],
  "soft": []
}