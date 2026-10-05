```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1-overlap-formula-factor-2",
      "severity": "HARD",
      "claim": "Eq. (M2): |⟨α|β⟩|² = exp(−r²(1 − cos θ)); headline result |⟨αᵢ|αⱼ⟩|² = e⁻⁴ ≈ 0.0183 for adjacent hexagon points at n̄ = 8.",
      "reason": "The formula is wrong by a factor of 2. From (M1), |⟨α|β⟩| = exp(−r² + r²cos θ) = exp(−r²(1−cos θ)), so the squared modulus is exp(−2r²(1−cos θ)) = exp(−|α−β|²). Equivalently, the paper's own Step 5 computation ⟨αᵢ|αⱼ⟩ = exp(−8 + 4 + 6.928i) has magnitude e⁻⁴ = 0.0183, contradicting its claim elsewhere that |⟨αᵢ|αⱼ⟩| = e⁻² = 0.1353. The correct adjacent-point squared overlap at n̄ = 8 is e⁻⁸ ≈ 3.35×10⁻⁴, not e⁻⁴ ≈ 0.0183.",
      "fix": "Correct (M2) to |⟨α|β⟩|² = exp(−2r²(1 − cos θ)) and recompute every downstream number: worst-case overlap e⁻⁸, next-nearest e⁻²⁴, opposite e⁻³², post-loss values exp(−2ηr²(1−cos θ)) (adjacent: e⁻⁷·⁶), the four-point contrast (e⁻¹⁶ pre-loss), and the hexagon/square ratio."
    },
    {
      "id": "H2-KL-ratio-wrong",
      "severity": "HARD",
      "claim": "Off-diagonal-to-diagonal KL deviation for the loss error is ~13.5% (ratio 0.1353353 = 8·e⁻²/8), quoted in abstract, Step 7, Results 3/abstract, and Discussion.",
      "reason": "The ratio uses |⟨αᵢ|αⱼ⟩| = e⁻², which follows from the erroneous (M2). With the correct overlap magnitude |⟨αᵢ|αⱼ⟩| = e⁻⁴ (as computed in the paper's own Step 5 phase calculation), the off-diagonal magnitude is 8·e⁻⁴ ≈ 0.1465 and the ratio is e⁻⁴ ≈ 1.83%, not 13.5%. The paper is internally inconsistent: Step 5 and Step 7 use two different values for the same overlap magnitude.",
      "fix": "Recompute the off-diagonal KL ratio consistently from the corrected overlap identity; replace 13.5% with the corrected value everywhere (abstract, Step 7, Results, Discussion, Conclusion) and reconcile Step 5's phase calculation with Step 7's magnitude claim."
    },
    {
      "id": "H3-postloss-and-derived-numbers",
      "severity": "HARD",
      "claim": "Post-loss adjacent overlap squared e^(−3.8) ≈ 0.02237 at η = 0.95 (abstract, Step 6, Result 5), and the claim that loss increases worst-case overlap by +22.1%.",
      "reason": "Derived from the erroneous (M3)/(M2). Correct value is exp(−2·0.95·8·0.5) = e⁻⁷·⁶ ≈ 5.00×10⁻⁴. The qualitative claim that loss increases overlap also flips: with the correct formula the post-loss squared overlap e⁻⁷·⁶ is smaller than... it remains larger than the pre-loss e⁻⁸ but the stated magnitudes and the +22.1% figure are wrong; next-nearest (e⁻¹¹·⁴ → e⁻²²·⁸) and opposite (e⁻¹⁵·² → e⁻³⁰·⁴) post-loss values are likewise wrong.",
      "fix": "Recompute all post-loss overlaps with the corrected exponent −2ηr²(1−cos θ); update abstract, Step 6, Results 5, and the labeled projection in Result 7 accordingly."
    },
    {
      "id": "H4-step5-inconsistent",
      "severity": "HARD",
      "claim": "True mean photon number ⟨â†â⟩ = 7.7871 ± 0.0012 (Eq. A5, Result 3), with adjacent off-diagonal terms of magnitude 8 × e⁻² = 1.0826824 per pair.",
      "reason": "The derivation is internally inconsistent: it first asserts per-pair magnitude 8 × e⁻² = 1.0827 (from the wrong M2), then evaluates the real part using 8 × 0.0183156 × cos(·) (i.e., magnitude e⁻⁴). Only one of these can be correct; with the correct overlap magnitude e⁻⁴ the per-pair real part is ≈ −0.0177 and the 12-pair sum ≈ −0.213, which happens to match the reported total, but the stated per-pair magnitude and the intermediate narrative are wrong and the result is not reliably derived as written.",
      "fix": "Redo Step 5 with a single, correct value of |⟨αᵢ|αⱼ⟩| = e⁻⁴ throughout; show the phase sum explicitly (or exploit hexagon symmetry to sum exactly) and restate A5 with a defensible error bound."
    }
  ],
  "soft": [
    {
      "id": "S1-gain-errors-uncomputed",
      "severity": "SOFT",
      "claim": "Photon-gain errors treated only via mean photon number; gain-error KL quantities not computed.",
      "reason": "Acknowledged as limitation (iv), but for a paper whose motivating error model is gain-and-loss symmetry, the absence of any gain-side quantity weakens the claimed connection to the BARC framework's KL mechanism.",
      "fix": "Either compute at least the diagonal gain-error quantity ⟨αᵢ|(ââ†)|αᵢ⟩ = n̄+1 (trivially uniform here) or strengthen the limitation discussion with the n̄-scaling of gain probability."
    },
    {
      "id": "S2-cautionary-citation-padding",
      "severity": "SOFT",
      "claim": "Six of thirteen references [3],[5]–[9] are withdrawn/removed arXiv records cited only as 'methodological context'.",
      "reason": "Nearly half the bibliography consists of retracted submissions with no scientific content related to bosonic coding; this dilutes the literature treatment and reads as citation padding, even though the paper is transparent about it.",
      "fix": "Trim or move the withdrawn-record discussion to a footnote/appendix and cite substantive literature on coherent-state/bosonic codes (cat, binomial, GKP codes) to substantiate the related-work claims."
    },
    {
      "id": "S3-ref10-doi-pending",
      "severity": "SOFT",
      "claim": "Reference [10] carries 'DOI pending' and quantitative claims (5–40× fewer photons, ~100× fewer modes) sourced to an unpublished QNFO corpus item.",
      "reason": "The resource-comparison framing of Section 2 and the n̄ = 8 design-point justification rest on an unverifiable, DOI-pending source.",
      "fix": "Replace with a published, verifiable resource-comparison reference or explicitly downgrade the 5–40×/100× figures to secondhand qualitative context."
    },
    {
      "id": "S4-superficial-related-work",
      "severity": "SOFT",
      "claim": "Related-work section covers cat/binomial/GKP codes only by name; no quantitative comparison of hexagonal BARC overlaps against published cat-code or GKP-code KL quantities.",
      "reason": "The four-point contrast is internal; the promised placement 'on the same photon-count axis' against established bosonic codes is asserted but never performed, leaving the literature treatment superficial.",
      "fix": "Add at least one computed comparison (e.g., cat-code |⟨α|−α⟩|² at n̄ = 8) so the related-work claims are grounded in the paper's own derivable numbers."
    }
  ]
}
```