{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "[3] observes that “AgentRxiv emphasizes collaboration, enabling agents to incrementally build upon prior findings.”",
      "reason": "The excerpt for citation [3] does not contain this statement; the claim is not derivable from the supplied bibliography entry.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt, e.g., cite the collaborative nature described in the introduction of [3]."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "[4] argues that “the efficiency of the solution‑search process is an equally important dimension of performance.”",
      "reason": "The excerpt for citation [4] only provides the title and does not contain this quoted claim; it is unsupported.",
      "fix": "Delete the sentence or rephrase to reflect only what is stated in the excerpt, such as noting that the paper’s title mentions efficiency."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "[5] reports that “enforcing evidence‑chain validity strengthens reliability and task quality.”",
      "reason": "The excerpt for citation [5] is not provided; the claim cannot be verified against the bibliography entry.",
      "fix": "Remove the sentence or replace it with a statement that can be directly sourced from the provided excerpt for [5] (if any)."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "[9] describes hardware and software failure arrivals as “Poisson processes” in microservice reliability studies.",
      "reason": "The excerpt for citation [9] does not contain this description; the claim is unsupported.",
      "fix": "Delete the sentence or modify it to reflect only the information present in the excerpt (e.g., that the paper deals with network‑aware reliability modeling)."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "[10] introduces a “Cox‑Weibull reliability model via a neural network” for weapon systems.",
      "reason": "The excerpt for citation [10] does not include this phrasing; the claim is not grounded in the supplied text.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt, such as noting that the paper presents a Bayesian weapon system reliability model."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "[14] identifies a “constraint saturation → substrate shift → Wright’s Law cost decline” cycle in computing evolution.",
      "reason": "The excerpt for citation [14] does not contain this specific claim; it is unsupported.",
      "fix": "Delete the sentence or rephrase to a claim that can be verified from the excerpt (e.g., that the paper discusses computing evolution forecasts)."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "[13] defines the JPCUB metric (joules per correct solution) and reports $J_S=0.05\,$J/solution for Google Willow.",
      "reason": "No excerpt for citation [13] is provided; the numeric value and definition cannot be verified against the bibliography entry.",
      "fix": "Remove the sentence or replace it with a statement that does not require unsupported numeric detail."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "## 6. 1 Further Derivations and Comparative Insights",
      "reason": "The required section heading order is violated; the paper must have a section titled exactly \"## 6. Discussion\" after \"## 5. Results\".",
      "fix": "Rename this section to \"## 6. Discussion\" and adjust subsequent section numbers accordingly."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "## 7. Discussion",
      "reason": "Because of the misnumbered preceding section, the required \"## 6. Discussion\" is missing and the ordering of sections does not follow the specification.",
      "fix": "Shift the existing Discussion content to be the \"## 6. Discussion\" section and renumber the following sections to match the required order."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "## 8. Practical Implications and Engineering Pathways",
      "reason": "After correcting the previous numbering, this heading becomes \"## 7. Practical Implications and Engineering Pathways\"; the current heading is off by one, violating the required structure.",
      "fix": "Rename the heading to \"## 7. Practical Implications and Engineering Pathways\" and ensure the subsequent \"## 8. Conclusion\" follows."
    }
  ],
  "soft": []
}