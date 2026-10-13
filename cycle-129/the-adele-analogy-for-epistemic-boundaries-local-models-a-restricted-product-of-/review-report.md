```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "\"$$\\Delta_{3\\sigma} = -7.4607 - (-7.721524) = +0.2609.$$\" (Section 4.2, Case k = 130) and downstream uses in Section 5 R1, R2 (residual 0.0391), and the Abstract.",
      "reason": "Arithmetic error in a headline number. -7.4607 - (-7.721524) = 0.260824, which rounds to 0.2608 at four decimal places, not 0.2609. The propagated residual in the Section 4.3 table is 0.3000 - 0.2608 = 0.0392, not 0.0391.",
      "fix": "Replace 0.2609 with 0.2608 throughout (Section 4.2, Section 4.3 residual table, Section 5 R1 and R2, Abstract if repeated), and change the x = 3 residual from 0.0391 to 0.0392. The factor e^{0.2608} = 1.298, so the reported factor of 1.30 is unaffected."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "\"whose relative error in $\\ln n!$ is of order $1/(360 n^4)$, negligible at the digit level used here.\" (Section 3.4) and \"whose next term is of order $1/(360 n^4)$; at $n = 110$ this is below $2 \\times 10^{-9}$ nats\" (Section 6, Limitations).",
      "reason": "Incorrect order stated for the Stirling remainder. The next term of the Stirling series for ln n! after 1/(12n) is of order 1/(360 n^3), not 1/(360 n^4). The paper's own magnitude estimate confirms this: 1/(360 x 110^3) = 2.09 x 10^-9, matching the quoted 'below 2 x 10^-9' bound, whereas 1/(360 x 110^4) = 1.9 x 10^-11 would not. The exponent and the numeric bound are mutually inconsistent as written.",
      "fix": "Replace 1/(360 n^4) with 1/(360 n^3) in both Section 3.4 and Section 6, and restate the n = 110 magnitude as approximately 2.1 x 10^-9 nats (or 'of order 10^-9 nats') so the exponent and the number agree."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "\"at $n = 110$ this is below $2 \\times 10^{-9}$ nats, so it cannot move any reported digit.\" (Section 6, Limitations, first bullet).",
      "reason": "Quantitative claim not consistent with its own inputs: with the corrected remainder 1/(360 n^3), the value at n = 110 is 1/(360 x 1331000) = 2.086 x 10^-9, which is above, not below, 2 x 10^-9. As written the bound is an underived and incorrect numeric claim.",
      "fix": "State the value as approximately 2.1 x 10^-9 nats at n = 110 (or 'of order 10^-9 nats'), which still supports the conclusion that no reported digit moves, since the smallest reported residual is 0.0008 nats."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "References list omits bibliography entry [2] (arXiv:2604.14837v1, Alzheimer's supervertex vision transformer) while including all other entries.",
      "reason": "Not a rule violation (at least 8 entries are present and Section 2 discusses 11 works), but the asymmetry of listing 11 of 12 supplied entries without comment is unexplained.",
      "fix": "Either add one sentence in Section 2 noting that entry [2]'s supplied summary concerns a domain (neurodegeneration detection) unrelated to the framework and is therefore not discussed, or omit it consistently with a stated selection note."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "\"At $1\\sigma$ ($k = 110$), $\\Delta = -0.0325$ nats, a $3.25\\%$ log-space error\" (Section 5, R1).",
      "reason": "Terminology: a difference of 0.0325 nats is not literally a '3.25% log-space error'; the probability relative error is e^{0.0325} - 1 = 3.30%, as correctly computed in Section 4.2. The two percentages are conflated in R1.",
      "fix": "In R1, distinguish the log-space discrepancy (0.0325 nats) from the probability relative error (3.30% at 1 sigma, 3.0% at 2 sigma as e^{0.0296} - 1 = 3.00%)."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "\"the consequence of an unnoticed validity failure is a treatment plan that harms a patient [7]\" (Section 1).",
      "reason": "The supplied entry for [7] states that contouring precision is crucial for treatment efficacy and patient safety; it does not state that an unnoticed failure produces a harmful plan. The sentence is a mild over-extrapolation beyond the entry's own text.",
      "fix": "Reword to what the entry supports, e.g. 'contouring precision is crucial for treatment efficacy and patient safety, so an unnoticed validity failure bears directly on patient safety [7]'."
    }
  ]
}
```