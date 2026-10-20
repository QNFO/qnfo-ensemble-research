{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The ReApp architecture for industrial robotics combines model‑driven engineering with semantic technologies, performing re‑entry from a design ontology onto running robot components [8].",
      "reason": "The bibliography excerpt for entry [8] is not provided, and the statement is not supported by any supplied text; citation must refer to a specific point from the work's full‑text excerpt.",
      "fix": "Replace the sentence with a statement that cites a work whose excerpt supports the claim, or remove the citation."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Large multimodal models (LMMs) exhibit false‑premise failures: they assert the existence of objects not present in the image, a concrete instance of re‑entry failure [5].",
      "reason": "Entry [5] concerns primitive ontology and does not discuss multimodal models; the false‑premise claim is actually supported by entry [7]. The citation is incorrect.",
      "fix": "Change the citation from [5] to [7] or remove the unsupported statement."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Definitional stagnation. Decentralization lacks a universally accepted definition, exemplifying how absent re‑entry criteria allow incompatible ontological commitments to accumulate [6].",
      "reason": "Entry [6] is about relational ontology of contemporary physics, not about decentralization; the claim is not supported by the provided excerpt.",
      "fix": "Replace the citation with the correct entry [8] that discusses decentralization, or remove the statement."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Reachable short predicates $\approx$ $1.53\times10^{12}$ (Abstract and Results) versus $1.2177\times10^{12}$ (Table in Section 4).",
      "reason": "The paper presents two different numerical values for the same quantity without justification, violating quantitative honesty.",
      "fix": "Choose a single value consistent with the derivation in Section 4 and update all occurrences."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Expected resolvable objects after compression is $9.54\times10^{-2}\approx0.095$ (text) versus $3.78\times10^{-36}\approx0$ (Table).",
      "reason": "Inconsistent quantitative claims for the same metric; the latter value lacks derivation.",
      "fix": "Retain the value derived in Section 4 ($9.54\times10^{-2}$) and correct the table entry."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Critical compression depth for survival of $10^{5}$ objects is $r_{\text{crit}} = 23.4$ ($\approx 23$).",
      "reason": "No arithmetic derivation is shown for this number; it appears as an unsupported projection.",
      "fix": "Provide a step‑by‑step derivation or label the claim explicitly as a projection with stated assumptions."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Fraction of reachable predicates $f_{\text{reach}} = 1.53\times10^{12}/10^{5.553\times10^{18}}\approx0$.",
      "reason": "Uses the inconsistent reachable predicate count (1.53e12) instead of the derived 1.2177e12, leading to a contradictory quantitative statement.",
      "fix": "Recompute the fraction using the consistent reachable count and update the expression."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Thermodynamic admissibility criterion derived from the erasure cost of distinctions [7].",
      "reason": "Entry [7] discusses false‑premise failures in LMMs and does not cover Landauer’s principle; the citation does not support the claim.",
      "fix": "Remove the incorrect citation or replace it with a work that actually discusses Landauer’s principle, if available."
    }
  ],
  "soft": []
}