{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Assuming a 1 GHz microcontroller with $10$ ns instruction latency, counting leading zeros in a 32‑bit word takes at most $5$ ns.",
      "reason": "Quantitative claim is presented without derivation or explicit labeling as a projection with stated assumptions.",
      "fix": "Label the statement as a projection and cite the assumption, e.g., \"Assuming a 1 GHz microcontroller with $10$ ns instruction latency, counting leading zeros in a 32‑bit word is projected to take at most $5$ ns (projection based on typical instruction pipelines).\""
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "For a sampling rate of $10^{6}$ samples s$^{-1}$, the power budget is under $10$ mW, and the hardware cost is below $5 USD$ per unit.",
      "reason": "Quantitative cost and power figures are given without derivation or projection label.",
      "fix": "Label the statement as a projection with assumptions, e.g., \"For a sampling rate of $10^{6}$ samples s$^{-1}$, a projected power budget is under $10$ mW and a projected hardware cost is below $5\\,\\text{USD}$ per unit (projection based on typical microcontroller power consumption and market pricing).\""
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The moduli space of stable coherent sheaves described in [3] shows that $p$‑adic analytic descriptions can encode discrete invariants such as stability, reinforcing the feasibility of transferring primality‑related data across the $p$‑adic–real bridge.",
      "reason": "Citation [3] does not contain an excerpt supporting the claim about encoding discrete invariants; the bibliography entry provides only title and no such statement.",
      "fix": "Remove or rephrase the sentence to avoid an unsupported claim, e.g., \"The moduli space of stable coherent sheaves studied via non‑archimedean geometry provides examples of $p$‑adic analytic descriptions of geometric objects.\""
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The Berkovich projective line $\\mathsf{P}^{1}$, studied in [4], offers a compactification preserving valuation topology, which underpins the continuity of $P_{p}$ on $[0,1]$.",
      "reason": "Citation [4] excerpt does not mention the Berkovich projective line or its compactification; the claim is unsupported by the provided bibliography entry.",
      "fix": "Remove or replace the sentence with a statement supported by the bibliography, e.g., \"Results on non‑archimedean dynamics provide tools for studying valuation‑topological properties of functions on $[0,1]$.\""
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "A recent primality‑testing algorithm based on Pell’s cubic [5] illustrates that algebraic curves can encode prime conditions; our valuation approach mirrors this by encoding divisibility in digit‑wise form.",
      "reason": "Citation [5] excerpt only gives the title and does not provide details about the algorithm or its relation to algebraic curves, making the claim unsupported.",
      "fix": "Remove the specific claim about encoding prime conditions or replace with a generic statement, e.g., \"Recent work on primality testing using algebraic curves demonstrates connections between number‑theoretic properties and geometric structures.\""
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Heights and measures on analytic spaces [6] give a systematic way to associate real‑valued functions to metrized line bundles on non‑Archimedean varieties [6].",
      "reason": "Citation [6] excerpt does not contain the asserted systematic construction; the claim is not supported by the provided text.",
      "fix": "Remove or rephrase the sentence to reflect only what the bibliography states, e.g., \"Heights and measures on analytic spaces are surveyed in [6].\""
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Non‑Archimedean Whittaker functions are identified with characters of representations, linking harmonic analysis on $p$‑adic groups to combinatorial data [7].",
      "reason": "Citation [7] excerpt provides only the title and does not substantiate the identification with characters or the harmonic analysis link.",
      "fix": "Remove the unsupported claim or replace with a neutral description, e.g., \"Non‑Archimedean Whittaker functions are studied in [7].\""
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Finally, the non‑archimedean analogue of Sendov’s conjecture [8] confirms that many classical analytic inequalities survive in valuation settings, supporting the robustness of our valuation‑topological methodology.",
      "reason": "Citation [8] excerpt does not provide evidence that classical analytic inequalities survive; the claim is unsupported by the bibliography entry.",
      "fix": "Remove the claim or rephrase to a verifiable statement, e.g., \"The non‑archimedean analogue of Sendov’s conjecture is discussed in [8].\""
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "All steps use only the independence of digits (a direct consequence of the product structure of the Lebesgue measure) and the definition of $v_{p}$.",
      "reason": "Citation [2] does not contain an excerpt establishing independence of digits under Lebesgue measure; the statement is unsupported.",
      "fix": "Remove the citation or qualify the statement as an assumption, e.g., \"All steps assume independence of digits under the Lebesgue measure, which follows from its product structure (assumption).\""
    }
  ],
  "soft": []
}