```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "κ = dim(A)² is 'equivalently' κ = D_C²/D_D² (Abstract, §1, §3), and Case III reports κ via dim(A) while giving D_D/D_C = √(3/7).",
      "reason": "Internal inconsistency / arithmetic contradiction: in Case III, dim(A)² = 4 but D_C²/D_D² = 14/6 = 7/3 ≈ 2.333. The two definitions the paper asserts to be equivalent disagree by a factor of 12/7. The paper even flags the cause (each survivor admits one simple A-module, so D_D ≠ D_C/dim(A) here) but never reconciles it with the claimed equivalence. The Abstract compounds this by calling √(3/7) the 'index' for Case III, which matches neither definition of κ.",
      "fix": "State explicitly that κ = dim(A)² and κ = D_C²/D_D² coincide only when the condensate is 'normal' in the sense that every local A-module sector contributes once (as in Cases I and II); for Case III report κ = 4 = dim(A)² and give D_C²/D_D² = 7/3 as a separate diagnostic, or redefine κ consistently. Correct the Abstract's 'index √(3/7)' to name the quantity (child/parent dimension ratio) explicitly."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Appendix A, item D2 ('Child category of the Ising ψ-condensation') is present as a heading with no content.",
      "reason": "The divergence report is truncated mid-document: the D2 heading is followed by no text. This is placeholder/incomplete text, a prose-gate violation, and it leaves a documented divergence (the child category of the fermionic Ising condensation, which §6 says 'is documented as a divergence in Appendix A') actually undocumented.",
      "fix": "Complete the D2 entry, describing the draft divergence over whether the child of the ψ-condensation is trivial, a p+ip superconductor (c = 1/2 with no intrinsic topological order), or something else, and how the main text resolved it."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "References [11], [12], [13] are cited with explicitly no technical content drawn from them.",
      "reason": "Citing sources while stating 'we draw no technical content from it' / 'no available abstracts' is citation padding; it inflates the reference list without scholarly contribution.",
      "fix": "Remove [11]–[13] or integrate genuine technical/methodological use; a 'corpus completeness' rationale is not a citation justification."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Boundary fusion rule 'σ × σ → 1 ⊕ 1' is derived by a heuristic identification of condensed summands with the vacuum.",
      "reason": "The central physical prediction (two-channel boundary fusion) rests on an admitted heuristic, not on module-category (C_A) computation; the paper flags this but the headline claim in the Abstract is stated without the caveat.",
      "fix": "Carry the heuristic caveat into the Abstract and Results, or sketch the actual C_A-module computation for at least Case I."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "μ = 2Δc is interpreted as a Majorana mode count.",
      "reason": "μ is defined mod 16 and the interpretation is admitted to fail for irrational Δc; the restriction is stated in §6 but the Abstract and Conclusion present μ = 1 as an unconditional Majorana count.",
      "fix": "Qualify μ's interpretation at first definition, not only in Discussion."
    },
    {
      "id": "S4",
      "severity": "SOFT",
      "claim": "Literature treatment of anyon condensation relies almost entirely on [2] and [8].",
      "reason": "The condensation side of the related-work survey is thin: foundational condensation literature beyond the two cited category-theory papers (e.g., earlier anyon-condensation results in concrete models) is not discussed, making the 'standard category data' inputs under-sourced.",
      "fix": "Add treatment of the concrete-model condensation literature underlying the standard Ising/toric-code data used in §4."
    }
  ]
}
```