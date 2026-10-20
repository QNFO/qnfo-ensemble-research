{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "False‑premise failures in multimodal models. Large multimodal models (LMMs) exhibit false‑premise failures: they assert the existence of objects not present in the image, a concrete instance of re‑entry failure [7].",
      "reason": "Citation [7] refers to a work about comparing pre‑print versions, not to multimodal models or false‑premise failures.",
      "fix": "Remove the citation and either delete the sentence or rewrite it without a citation, e.g., \"False‑premise failures in multimodal models have been reported, where models assert the existence of objects not present in the image.\""
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Definitional stagnation in decentralisation. Decentralisation lacks a universally accepted definition, exemplifying how absent re‑entry criteria allow incompatible ontological commitments to accumulate [8].",
      "reason": "Citation [8] is a paper on Energy Complexity of Regular Languages, unrelated to decentralisation definitions.",
      "fix": "Delete the citation and, if needed, remove the sentence or keep it without a citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Language‑model ontologies with bounded retrieval. Fine‑tuning LLMs with Retrieval‑Augmented Generation for legal regulation demonstrates an engineering pattern where a high‑level ontology (legal concepts) is re‑entered onto human conduct via a bounded retrieval mechanism [4].",
      "reason": "Citation [4] discusses predicted class correction, not retrieval‑augmented generation for legal regulation.",
      "fix": "Remove the citation and rewrite the sentence without it, e.g., \"Fine‑tuning LLMs with Retrieval‑Augmented Generation for legal regulation demonstrates an engineering pattern where a high‑level ontology is re‑entered onto human conduct via a bounded retrieval mechanism.\""
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "only $\\approx1.53\\times10^{12}$ are reachable by short Boolean formulas",
      "reason": "The analysis in Section 4.2 computes $N_{\\text{short}} \\approx 1.39\\times10^{15}$, not $1.53\\times10^{12}$; the abstract and results present an unsupported number.",
      "fix": "Replace the number with $1.39\\times10^{15}$ throughout the abstract and Section 5, and adjust any related statements."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Thus the fraction of reachable predicates is $f_{\\text{reach}} = \\frac{1.53\\times10^{12}}{10^{5.553\\times10^{18}}}\\approx 0$.",
      "reason": "The numerator should be the computed reachable count $1.39\\times10^{15}$, not $1.53\\times10^{12}$.",
      "fix": "Update the fraction to $f_{\\text{reach}} = \\frac{1.39\\times10^{15}}{10^{5.553\\times10^{18}}}\\approx 0$."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "failure modes, including false‑premise commitments observed for multimodal models [7]",
      "reason": "Citation [7] does not discuss multimodal models; it is about comparing pre‑print versions.",
      "fix": "Remove the citation and keep the statement without a reference, or delete the sentence if no source supports it."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "definitional fragmentation documented for decentralization [8]",
      "reason": "Citation [8] is unrelated to decentralization; it covers Energy Complexity of Regular Languages.",
      "fix": "Delete the citation and retain the sentence without a reference, or remove the sentence if unsupported."
    }
  ],
  "soft": []
}