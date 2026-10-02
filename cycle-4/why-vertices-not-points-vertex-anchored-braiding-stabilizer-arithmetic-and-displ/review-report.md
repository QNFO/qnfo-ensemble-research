```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "CIT-1",
      "severity": "HARD",
      "claim": "References [5] Serre 'Trees', [6] Temperley–Lieb 1971, [7] Jones 1985, [8] Hardy & Wright are cited throughout (Sections 2, 4.6, 4.7) and listed in '## References'.",
      "reason": "The provided BIBLIOGRAPHY contains only four entries ([1]–[4], the QNFO corpus with Zenodo DOIs). References [5]–[8] do not appear in the bibliography with machine identifiers and are therefore unverifiable/unsourced in this audit context. The paper itself concedes 'no page-level verification against [5]–[8] was performed', which does not cure the citation-integrity violation.",
      "fix": "Remove references [5]–[8] from the reference list and either (a) re-anchor the classical material (Serre trees, TL/Jones, Fibonacci congruences, p-adic topology) solely to in-text derivations and to corpus references [1]–[3], explicitly stating they are derived, not cited; or (b) obtain a bibliography that includes these works with verifiable identifiers. Renumber remaining references to match the required bibliography order."
    }
  ],
  "soft": [
    {
      "id": "DEP-1",
      "severity": "SOFT",
      "claim": "Section 2 presents four 'classical background' bodies of work anchored to [5]–[8] as the literature survey.",
      "reason": "The literature treatment of the classical material is thin: standard results (building structure, rank of apparition, Catalan bound) are asserted and attributed to references that are not verifiable in this corpus, so the survey's independent anchoring rests entirely on the paper's own derivations.",
      "fix": "Strengthen by fully deriving each classical input used (the rank-of-apparition theorem in particular is used as a black box in Section 4.6) or clearly marking them as external standard results whose proofs are outside scope, with an explicit statement of which claims are derived vs. imported."
    },
    {
      "id": "DEP-2",
      "severity": "SOFT",
      "claim": "Projection P3 (Section 4.8): an 'additive shell-grading rule' k1 + k2 = k_fusion yields 12 fusion outcomes at p = 2.",
      "reason": "The modeling rule is admittedly not derived from [2]'s fusion rules and its physical/combinatorial meaning is unexplained; the projection is labeled but its motivation is superficial.",
      "fix": "Either derive the grading rule from the fusion rules of [2] or expand the discussion of what the rule models, why the shell-3 count is the relevant outcome space, and how it would be tested."
    },
    {
      "id": "DEP-3",
      "severity": "SOFT",
      "claim": "Section 4.1 claims π₁(Q_p \\ {x}) is trivial via a deformation retraction onto clopen annuli.",
      "reason": "The argument is correct in substance (continuous images of intervals in Q_p are points), but the paper's stated route ('deformation-retracts onto the disjoint union of clopen annuli') is loosely phrased — a deformation retraction onto a totally disconnected union needs justification, and the paper itself flags in Section 6 that readers should verify this against standard treatments it does not cite verifiably.",
      "fix": "Replace the deformation-retraction phrasing with the direct argument: any loop is a continuous map from the connected interval [0,1] into Q_p \\ {x}, whose image is connected and hence a single point, so every loop is constant."
    }
  ]
}
```