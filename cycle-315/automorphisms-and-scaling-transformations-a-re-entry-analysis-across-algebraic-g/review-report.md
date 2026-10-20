{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "References section lists only \"[1]\" and does not include all works cited in the paper such as [2], [3], [4], [6], [7], [8], [9].",
      "reason": "Citation integrity violation: every cited work must appear in the References list.",
      "fix": "Add full reference entries for [2]–[9] in the References section, preserving exact titles and identifiers."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The paper provides fewer than eight reference entries.",
      "reason": "Structure requirement: the paper must cite at least eight works in the References.",
      "fix": "Include at least eight reference entries, i.e., all cited works."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The paper lacks Appendix A. Divergence report and Appendix B. Claim attribution sections.",
      "reason": "Structure requirement: required appendices are missing.",
      "fix": "Add sections \"## Appendix A. Divergence report\" and \"## Appendix B. Claim attribution\" with appropriate content."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Citation of [7] is used to support the statement \"Non‑linear automorphisms may behave differently (see [7])\" but the supplied excerpt for [7] does not contain any such claim.",
      "reason": "Source support violation: the statement is not derivable from the provided excerpt of [7].",
      "fix": "Remove or rephrase the statement to avoid unsupported claim, or replace with a supported citation."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Citation of [9] is used to motivate the test, but the provided excerpt for [9] does not contain the claimed motivation.",
      "reason": "Source support violation: the claim about practitioners lacking a uniform test is not supported by the excerpt of [9].",
      "fix": "Remove or rephrase the motivation sentence, or replace with a supported citation."
    }
  ],
  "soft": []
}