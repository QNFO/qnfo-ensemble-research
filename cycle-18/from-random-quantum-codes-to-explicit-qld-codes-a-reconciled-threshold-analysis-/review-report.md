```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Appendix B claim-attribution table, row C21",
      "reason": "The final table row is truncated mid-sentence ('...check weights growing with n, ω(1)'), leaving the claim text, attribution columns, and status incomplete. This is placeholder/incomplete text in the delivered manuscript and violates the prose-completeness gate.",
      "fix": "Complete row C21 with the full falsification-condition claim, its draft attributions, and a status label; verify the table renders fully."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "List size L ≈ 2/ε ≈ 16 (Section 4.3)",
      "reason": "The multiplicative constant 2 is asserted as 'a representative value from classical list-decoding theory' without a citation to a specific theorem or derivation; although a constant-factor caveat is stated, the headline number L ≈ 16 rests on an unsourced constant.",
      "fix": "Cite the specific random-linear-code list-size bound (e.g., a theorem from the LCL/classical literature) that yields the constant, or present L only as O(1/ε) with 16 given as an illustrative order-of-magnitude."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Reference [12] is listed but has no retrievable abstract and is not substantively discussed",
      "reason": "Including an entry the paper itself declares undiscussable adds no scholarly value and leaves the bibliography partially unverifiable in content.",
      "fix": "Either remove [12] from the References or obtain and summarize its abstract."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "Depth of treatment of the quantum-LCL threshold theorem",
      "reason": "The threshold theorem and the two-rank witness mechanism are restated at a high level but never worked through in even one concrete witness example (e.g., distance or list-decoding witness ranks), so the reader cannot independently sanity-check the per-sector equality beyond trusting [2].",
      "fix": "Add a worked toy example of a quantum-LCL witness showing physical vs. logical rank computation on a small CSS family."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "Limitations of source maturity",
      "reason": "The paper flags that [1], [2] are unrefereed preprints only in an open-questions footnote (Section 6, item v); this caveat should also qualify the abstract's headline claims ('first explicit quantum list-decodable codes').",
      "fix": "Add a one-line verification-status qualifier to the abstract or Section 2 discussion of [2]."
    }
  ]
}
```