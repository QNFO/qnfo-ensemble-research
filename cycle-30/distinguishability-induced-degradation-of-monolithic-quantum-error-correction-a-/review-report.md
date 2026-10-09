{
 "verdict": "revise",
 "hard": [
 {
 "id": "H1",
 "severity": "HARD",
 "claim": "Appendix B contains only a placeholder text instead of the required claim‑attribution table.",
 "reason": "The reconciliation specification mandates a complete claim‑attribution table in Appendix B; a placeholder does not satisfy the structural requirement.",
 "fix": "Replace the placeholder with a markdown table mapping each quantitative claim (C1…Cn) to its originating draft(s) and agreement status (CONVERGENT, DIVERGENT, SINGLE)."
 }
 ],
 "soft": [
 {
 "id": "S1",
 "severity": "SOFT",
 "claim": "The discussion of related work could be deepened with more explicit connections to each cited work.",
 "reason": "Section 2 provides brief one‑sentence contexts; expanding to two sentences per work would improve scholarly depth.",
 "fix": "Add an additional explanatory sentence for each of the eight (or more) cited works, linking their results to the present analysis."
 },
 {
 "id": "S2",
 "severity": "SOFT",
 "claim": "Uncertainty quantification for the projected checking intervals is limited to a single tolerance value.",
 "reason": "Providing a range of plausible tolerances or error bars would strengthen the quantitative analysis.",
 "fix": "Include a brief note in Section 5 indicating how the checking‑interval bound varies with reasonable variations in D_max (e.g., 5×10⁻³ to 2×10⁻²)."
 }
 ]
}