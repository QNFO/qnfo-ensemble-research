```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "References [4], [5], [6], [7], [8], [9], [10], [11] (e.g. '## References ... [4] Pitch Controls the Flexibility of Helical Ribbons. arXiv:2208.09321v1 ... [9] https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation ... [11] ... Fine-Structure Constant as a Cross-Ratio')",
      "reason": "Citation integrity: the provided BIBLIOGRAPHY contains only entries [1] (arXiv:2011.06396v2) and [2] (arXiv:2607.29086v1). Eight of the ten listed references, including all three QNFO works, do not appear in the provided bibliography with machine identifiers and are therefore unverifiable; per the audit rules these are invented/unsourced references. This also makes the required QNFO consistency check impossible: the paper's uses of [9] (identity alpha = r_e/lambda_bar_C), [10] (resonance condition d/v = pi*hbar/(m c^2)) and [11] (alpha^{-1} = 137.035999084) cannot be confirmed against those works' own texts.",
      "fix": "Remove references [4]-[11] and every sentence citing them, or supply their bibliography entries; retain only [1] and [2] and state the limitation in the Discussion. All quantitative inputs currently sourced to [11] (alpha^{-1} = 137.035999084) must be restated as the paper's own assumption."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "'The measured electron anomaly agrees with point-particle QED to within the experimental uncertainty at the level implied by the alpha precision reported in [11].' and 'the existing agreement between the g-2 and atom-recoil determinations of alpha in [11] already implies' (Sections 6, 7c, 8)",
      "reason": "Source support: these are claims about the outside world (the measured value of the electron anomaly and the agreement between two determinations of alpha) attributed to [11], which is not present in the provided bibliography; no supplied source states them.",
      "fix": "Restate as an explicit assumption of this work ('We assume the measured anomaly agrees with point-particle QED at ...') or remove; do not attribute the fact to [11]."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "'enormously larger than the part-per-billion precision of existing g-factor measurements' (Section 1) and 'precision electron g-factor measurement — already exists at the required precision' (Section 7b)",
      "reason": "Quantitative honesty / source support: the part-per-billion precision of existing electron g-factor measurements is a quantitative claim about the world that is neither derived in the paper nor stated in any provided bibliography entry.",
      "fix": "Label it as an assumption with a stated uncertainty bound, or remove the specific precision figure and keep only the derived comparison against the paper's assumed 10^-9 uncertainty."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Absence of '## Appendix A. Divergence report' and '## Appendix B. Claim attribution'",
      "reason": "Divergence honesty: no divergence report is present; if the source drafts diverged on any claim (e.g. the treatment of the r_e identity as confirmation vs. cross-check), the required appendix is missing.",
      "fix": "Add Appendix A documenting any draft divergences and the convention chosen, and Appendix B with the claim-attribution table."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Section 2 discusses eight works, but only [1] and [2] are verifiable against the provided bibliography",
      "reason": "Depth: the literature treatment cannot be audited for eight of the cited works; after removing unverifiable citations the related-work section may fall below the required substantive treatment.",
      "fix": "Deepen the discussion of [1] (pitch balance as a stability condition for embedded helical motifs in lamellar minimal surfaces) and [2] (helical embedding of pitch in model representations) with additional specific points from their full texts."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "'the tolerance budget is an open question' (Section 7d)",
      "reason": "Depth: the channeling-test constraints are left qualitative; the paper could at least state the resonance condition's dimensional structure and what quantities a tolerance budget would need to specify.",
      "fix": "State explicitly which parameters (plane spacing d, velocity spread delta-v/v) a tolerance budget must cover, even if numerical values are deferred."
    }
  ]
}
```