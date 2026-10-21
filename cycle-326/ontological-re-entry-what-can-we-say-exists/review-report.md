{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Retrieval‑augmented generation is used to connect high‑level legal concepts to concrete textual evidence, providing a concrete instance of a re‑entry map [3].",
      "reason": "Citation [3] is not supported by any supplied excerpt; the statement cannot be derived from the bibliography entry.",
      "fix": "Remove the sentence or replace it with a statement that does not cite [3]."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Primitive ontology in quantum foundations ... [5] argues that ontological clarity is required for theoretical frameworks.",
      "reason": "Citation [5] lacks a supplied excerpt; the claim is not verifiable from the provided bibliography.",
      "fix": "Delete the sentence or rephrase without citing [5]."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Landauer’s principle, stating that erasing a bit at temperature $T_{\\mathrm{env}}$ costs at least $E_{\\mathrm{bit}}=k_{B}T_{\\mathrm{env}}\\ln2$, is presented in [7] as a bound on the energy consumption of distinction maintenance.",
      "reason": "Citation [7] is not supported by any excerpt; the statement cannot be sourced from the bibliography.",
      "fix": "Remove the citation to [7] and keep the derived formula as an internal result, or provide a supported citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Energy complexity of regular languages ... provides bounds that are relevant to the cost of maintaining binary distinctions [8].",
      "reason": "Citation [8] lacks a supplied excerpt; the claim is unsupported.",
      "fix": "Delete the sentence or replace it with a supported claim."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Operational closure and measurement cost ... introduced by [9] linking computable approximation protocols to measurement energy cost $E\\cdot\\mu(-\\log_{2}\\varepsilon)$.",
      "reason": "Citation [9] is not backed by any excerpt; the statement cannot be verified.",
      "fix": "Remove the citation to [9] and keep the discussion if needed without referencing the work."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The finite‑distinction program defining admissible existence claims and deriving combinatorial and thermodynamic bounds is described in [10].",
      "reason": "Citation [10] lacks a supplied excerpt; the claim cannot be substantiated.",
      "fix": "Delete the citation to [10] or replace with a statement that does not reference the work."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Reachable short predicates (≤ 9 literals) | $N_{\\text{short}}$ | $1.53\\times10^{12}$",
      "reason": "The numeric value contradicts the derived sum $1.53184461288\\times10^{13}$ shown in Section 5.2; the table entry is incorrect.",
      "fix": "Replace $1.53\\times10^{12}$ with $1.53\\times10^{13}$."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Fraction of reachable predicates $f_{\\text{reach}} = \\frac{1.53\\times10^{12}}{10^{5.553\\times10^{18}}}\\approx 0$.",
      "reason": "The numerator uses the incorrect value $1.53\\times10^{12}$ instead of $1.53\\times10^{13}$, making the quantitative claim inconsistent with the derivation.",
      "fix": "Replace the numerator with $1.53\\times10^{13}$."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Critical compression depth for survival of $10^{5}$ objects (projection, assuming uniform distribution and Poisson model) | $r_{\\text{crit}} \\approx 23$",
      "reason": "The claim is presented as a result but no derivation, calculation, or projection label is provided; it is an unsupported quantitative assertion.",
      "fix": "Either provide a full derivation with shown arithmetic or label the statement as a projection with explicit assumptions, or remove it."
    }
  ],
  "soft": []
}