{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Consequently, the cooling infrastructure required for a surface‑code processor with ≈ $10^{6}$ physical qubits would exceed the available power by a factor of ≈ 2 × $10^{4}$, making deployment prohibitively expensive.",
      "reason": "Quantitative claim lacks derivation or explicit projection label; no arithmetic is shown to support the factor of 2 × 10⁴.",
      "fix": "Provide a detailed calculation of the cooling‑power ratio or rephrase as a projection with stated assumptions."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "If a passive error‑correction scheme could tolerate depolarizing error rates on the order of 75 % without syndrome extraction, the same logical performance could be achieved at 4 K, eliminating the cooling‑power bottleneck and dramatically lowering system cost.",
      "reason": "Quantitative claim of tolerating 75 % error rate is not derived, nor labeled as a projection; the analysis shows this cannot be achieved with the presented model.",
      "fix": "Either remove the 75 % claim or label it as a speculative projection with clear assumptions, and reconcile with the analytical results."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The cooling‑power gap of $2\\times10^{4}$ (Eq. 5) demonstrates that the passive scheme can operate at 4 K without the massive refrigeration infrastructure required by active surface‑code implementations.",
      "reason": "Equation (5) yields a factor of ≈ 92, not 2 × 10⁴; the statement is inconsistent with the derived value.",
      "fix": "Correct the statement to reflect the computed factor (~92) or provide a separate derivation that justifies the 2 × 10⁴ figure."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Low‑overhead transversal fault tolerance. The concept aims to reduce syndrome extraction overhead, though specific quantitative results are not addressed here.",
      "reason": "Citation [4] is used without a specific supporting excerpt from its full text; the statement is not verifiable from the supplied bibliography entry.",
      "fix": "Replace the citation with a statement directly supported by the excerpt from [4] or remove the citation."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Byzantine fault tolerance in cloud clusters. High fault rates in critical applications motivate architectures that minimize detection infrastructure.",
      "reason": "Citation [5] is used without a specific supporting excerpt; the claim cannot be traced to the provided bibliography entry.",
      "fix": "Provide a concrete point from [5] that supports the claim or delete the citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Flag‑based error correction. Flag techniques aim to lower ancilla overhead by detecting high‑weight errors with few extra qubits.",
      "reason": "Citation [6] is used without a specific supporting excerpt; the statement is not grounded in the supplied text.",
      "fix": "Cite a specific result from [6] that matches the claim or remove the citation."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Decentralized validation for arbitrary faults. Distributed systems can tolerate arbitrary (Byzantine) faults by validating state changes locally.",
      "reason": "Citation [7] is used without a specific supporting excerpt; the claim lacks grounding in the bibliography entry.",
      "fix": "Add a concrete citation from [7] that supports the claim or omit the citation."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "SignSGD robustness. SignSGD remains stable in the presence of blind Byzantine adversaries, illustrating that algorithmic designs can be inherently fault‑tolerant.",
      "reason": "Citation [8] is used without a specific supporting excerpt; the claim is not verifiable from the provided bibliography entry.",
      "fix": "Reference a specific passage from [8] that substantiates the claim or remove the citation."
    }
  ],
  "soft": []
}