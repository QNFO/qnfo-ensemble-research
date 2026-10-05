{
 "verdict": "revise",
 "hard": [
 {
 "id": "CIT01",
 "severity": "HARD",
 "claim": "References [6]–[14] do not correspond to any entry in the provided Bibliography; the arXiv identifiers, titles, and years differ.",
 "reason": "Citation integrity requires every reference in the References list to appear verbatim (including identifier) in the Bibliography. Mismatched IDs constitute invented or unverifiable citations.",
 "fix": "Replace each mismatched reference with the exact Bibliography entry (or add the missing Bibliography entries) so that IDs, arXiv numbers, titles, and authors match one‑to‑one."
 },
 {
 "id": "ARITH01",
 "severity": "HARD",
 "claim": "The standard error of \\(\\hat{P}_L\\) is reported as \\(3.16\\times10^{-6}\\) for \\(P_L=10^{-3}\\) and \\(N=10^6\\).",
 "reason": "Correct calculation: \\(\\mathrm{Var}=P_L(1-P_L)/N = 9.99\\times10^{-10}\\); the square root is \\(3.16\\times10^{-5}\\), an order of magnitude larger. Consequently the quoted relative precision (0.32 %) is off by a factor of ten.",
 "fix": "Re‑compute the variance and propagate the corrected standard error (\\(3.16\\times10^{-5}\\)) through all subsequent statements (e.g., relative precision becomes ~3 %). Update the manuscript accordingly."
 }
 ],
 "soft": [
 {
 "id": "SOFT01",
 "severity": "SOFT",
 "claim": "The text repeatedly refers to an \"Appendix A\" that is absent from the document.",
 "reason": "Omitting a promised appendix leaves a gap in the logical flow and may hide important derivations or alternative readings.",
 "fix": "Either provide the missing Appendix A with the referenced material or remove all citations to it."
 },
 {
 "id": "SOFT02",
 "severity": "SOFT",
 "claim": "The literature review in Section 2 treats many related works superficially and does not critically compare methodologies.",
 "reason": "Depth criterion requires a more thorough synthesis of prior art, especially given the breadth of cited QEC optimization approaches.",
 "fix": "Expand Section 2 to include concise summaries of each cited work, highlight differences with the present approach, and discuss limitations of those prior methods."
 }
 ]
}