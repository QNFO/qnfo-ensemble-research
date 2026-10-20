{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "In Section 2 the sentence ends abruptly with \"[5] Finally,\" and no further text follows.",
      "reason": "The paper contains an incomplete sentence, violating the required structural completeness.",
      "fix": "Complete the sentence by adding a concise statement that summarizes the point from reference [5] or remove the dangling fragment."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The single‑shot readout fidelity $F=99.991\\%$ (error probability $p_{e}=9\\times10^{-5}$) is attributed to reference [4].",
      "reason": "Reference [4] (\"How do Ontology Mappings Change in the Life Sciences?\") does not contain any information about qubit readout fidelity; the claim lacks source support.",
      "fix": "Replace the citation [4] with a statement that the fidelity value is an assumption, e.g., \"We assume a single‑shot readout fidelity $F=99.991\\%$ (error probability $p_{e}=9\\times10^{-5}$) as an illustrative value.\""
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The paper states that [9] discusses self‑referential metrology across transmon, trapped‑ion, and spin platforms; that [10] critiques the particle‑ontology view; and that [11] provides a falsification pledge.",
      "reason": "No excerpts from references [9], [10], [11] are provided in the bibliography, so these specific claims cannot be verified from the supplied source text.",
      "fix": "Remove or rephrase these statements to avoid attributing specific content to those works, or replace them with a generic citation that does not assert unsupported details."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The manuscript lacks the required Appendix A (Divergence report) and Appendix B (Claim attribution) sections.",
      "reason": "The paper does not include the mandated appendices, violating the required structure.",
      "fix": "Add empty placeholder sections titled \"## Appendix A. Divergence report\" and \"## Appendix B. Claim attribution\" (or populate them if appropriate) after the References."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The statement \"The methodological stance—falsifiability as a pledge rather than a slogan—is adopted from [11]\" attributes a specific methodological claim to reference [11] without supporting excerpt.",
      "reason": "Reference [11] excerpts are not provided; the claim cannot be verified from the supplied source text.",
      "fix": "Rephrase to avoid attributing the methodological stance to [11], e.g., \"The methodological stance of adopting falsifiability as a pledge is consistent with the principles discussed in the literature.\" and remove the citation."
    }
  ],
  "soft": []
}