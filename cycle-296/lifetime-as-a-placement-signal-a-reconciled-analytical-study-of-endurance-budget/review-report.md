{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The paper is missing the required Appendix A. Divergence report.",
      "reason": "Structure requirement mandates an Appendix A section for divergence reporting; the manuscript only contains Appendix B.",
      "fix": "Add an Appendix A section titled \"## Appendix A. Divergence report\" with appropriate content."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Citation of [4] claims a 2.91× memory reduction, but no excerpt from [4] is provided to support this specific quantitative statement.",
      "reason": "Citation integrity requires each cited work to be supported by a specific point from its supplied full-text excerpt; [4] lacks such excerpt.",
      "fix": "Remove or replace the unsupported claim about the 2.91× memory reduction, or provide a supported statement derived from the available excerpt."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Citation of [5] claims an LRU‑K policy extends HBF lifetime from ≈1 year to >6 years, but no excerpt from [5] is provided.",
      "reason": "Citation integrity violation; the claim is not grounded in supplied text.",
      "fix": "Remove or replace the unsupported claim about LRU‑K policy extensions."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Citation of [6] asserts that HBM bandwidth is scarce and motivates heterogeneous accelerators, but no excerpt from [6] is provided.",
      "reason": "Citation integrity violation; the statement lacks grounding in the supplied excerpt.",
      "fix": "Remove or replace the unsupported claim about HBM bandwidth scarcity."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Citation of [8] states a 4.20× lifetime improvement with 4 % performance penalty, but no excerpt from [8] is provided.",
      "reason": "Citation integrity violation; the quantitative claim is unsupported by the bibliography excerpts.",
      "fix": "Remove or replace the unsupported claim about cache‑coloring lifetime improvement."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Citation of [9] claims it provides a benchmark suite for isolating placement‑related performance factors, but no excerpt from [9] is provided.",
      "reason": "Citation integrity violation; the claim lacks supporting excerpt.",
      "fix": "Remove or replace the unsupported claim about the benchmark suite."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Citation of [10] describes an earlier version of this analysis and its limitations, but no excerpt from [10] is provided.",
      "reason": "Citation integrity violation; the statement is not grounded in supplied text.",
      "fix": "Remove or replace the unsupported claim about the prior analysis."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Section 7(b) states that according to NASA TRL definitions, purely analytical, unreviewed work resides at TRL 2.",
      "reason": "The claim about NASA TRL definitions is not sourced from any provided bibliography entry; it is an unsupported factual statement.",
      "fix": "Remove the unsourced TRL statement or replace it with a citation to a source that provides this definition."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Section 4G derives a write rate of $5.26\\times10^{4}$ writes/yr per cell from the upper bound of a $4.8$ yr baseline lifetime.",
      "reason": "Arithmetic error: $10^{5}\\,/\\,4.8 = 2.08\\times10^{4}$, not $5.26\\times10^{4}$. The derived number is incorrect and not a labeled projection.",
      "fix": "Correct the derivation to $2.08\\times10^{4}$ writes/yr (or adjust the statement to reflect a proper projection)."
    }
  ],
  "soft": []
}