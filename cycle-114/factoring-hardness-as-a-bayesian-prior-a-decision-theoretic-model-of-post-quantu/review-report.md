{
 "verdict": "revise",
 "hard": [
 {
 "id": "H1",
 "severity": "HARD",
 "claim": "The paper ends the description of Scenario D with an incomplete sentence \"p\" and does not provide the final break‑even prior value.",
 "reason": "The text contains a placeholder/incomplete sentence, violating the rule against placeholder text and leaving a quantitative claim undefined.",

 },
 {
 "id": "H2",
 "severity": "HARD",
 "claim": "Scenario P’s optimal migration time T^{*} is said to be solved numerically by bisection in Section 4.4, but no numeric result or derivation is presented.",
 "reason": "A quantitative claim (that a numerical solution exists) is made without providing the result or supporting computation, violating the quantitative honesty requirement.",
 "fix": "Either provide the computed optimal time T^{*} with the arithmetic steps (e.g., solve r C_m e^{-rT}=LΛ/a (1-e^{-aT}) for the given parameters) or rephrase the statement to indicate that the solution is pending and label it as a projection."
 }
 ],
 "soft": [
 {
 "id": "S1",
 "severity": "SOFT",
 "claim": "The paper references Section 4.4, which does not exist.",
 "reason": "Referencing a non‑existent section reduces clarity but does not invalidate quantitative claims.",
 "fix": "Rename the references to the correct existing sections (e.g., refer to Section 4.2 where the scenarios are described) or add a brief Section 4.4 with the missing numerical solution."
 },
 {
 "id": "S2",
 "severity": "SOFT",
 "claim": "No Appendix A or B is provided, though not required for this version.",
 "reason": "While not mandatory for the current paper, adding them could improve completeness for future reconciled versions.",
 "fix": "Optionally include empty Appendices or omit the note; not a hard requirement."
 }
 ]
}

_1 statement removed: each carried a DOI, link, author citation or figure that is not in the supplied sources._