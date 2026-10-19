{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "## References\n\n[1] ...\n[2] ...\n[4] ...\n[5] ...\n[6] ...\n[7] ...",
      "reason": "The References section contains only six entries, but the paper requires at least eight bibliography entries.",
      "fix": "Add two additional bibliography entries that are present in the supplied bibliography, or if none exist, acknowledge the limitation in the Discussion and adjust the requirement accordingly."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The introductory review of fault‑tolerant architectures notes that current experimental arrays contain at most ten functional qubits, while fully error‑corrected machines would require substantially larger registers [1]. The same source emphasizes that the theoretical framework for fault tolerance has existed for nearly two decades and is well understood, yet hardware constraints dominate.",
      "reason": "Citation [3] is used but there is no entry [3] in the provided bibliography.",
      "fix": "Replace the citation [3] with a valid reference from the bibliography (e.g., [1] or [2]) or remove the citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "It is known that any non‑trivial two‑qubit gate generates a dense subgroup of $U(4)$ [8].",
      "reason": "Citation [8] does not exist in the provided bibliography.",
      "fix": "Replace the citation [8] with a valid reference from the bibliography (e.g., [4]) or remove the citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The adelic synthesis of anyon theory explores extensions to $p$‑adic completions of the rational numbers. This work motivates the exploration of braid groups beyond the continuous $\\mathbb{R}^{2}$ setting.",
      "reason": "The statement cites work [5] but no specific excerpt from that work is provided to support the claim; the claim is not grounded in the supplied bibliography text.",
      "fix": "Either provide a specific supporting excerpt from [5] that makes this claim, or remove/rephrase the statement to avoid an unsupported citation."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Concrete constructions of $p$‑adic braid groups on Bruhat‑Tits trees have been proposed.",
      "reason": "The statement cites work [6] without a supporting excerpt from that work; the claim is not verifiable from the supplied bibliography.",
      "fix": "Either supply a concrete excerpt from [6] that makes this claim, or delete/rewrite the sentence to avoid an unsupported citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Using the empirical surface‑code ratio $r=10^{3}$ [7] and the present experimental limit of ten functional qubits [1], we compute a minimal physical qubit requirement of $N_{\\text{phys}}=10^{3}$ for a single logical qubit...",
      "reason": "The ratio $r=10^{3}$ is attributed to reference [7], but no excerpt from [7] is provided that states this numeric value; the claim is unsupported by the supplied bibliography.",
      "fix": "Provide a specific excerpt from [7] that gives the $10^{3}$ ratio, or remove the citation and treat the ratio as an assumption, clearly labeling it as such."
    }
  ],
  "soft": []
}