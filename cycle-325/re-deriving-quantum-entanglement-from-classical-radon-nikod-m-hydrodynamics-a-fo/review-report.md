{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "**Ensemble‑statistical view of quantum dynamics.** Statistical‑mechanics mappings can relate random quantum circuit properties to classical spin models, suggesting connections to domain‑wall free energies. This demonstrates that classical statistical descriptions can capture ensemble‑level quantum information, motivating the ensemble‑focused phrasing of the axioms in Section 3.1.",
      "reason": "Section 2 contains uncited statements about works without any citation, violating the requirement to discuss at least eight works and to cite each specific point to a bibliography entry.",
      "fix": "Add explicit citations to at least eight bibliography entries, each supporting a specific point, and ensure every statement about a work is tied to a citation that matches the supplied excerpt."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "**Multipartite entanglement as a network resource.** Algorithms for generating multipartite entanglement over noisy networks typically consider fidelity and distribution rate as performance metrics. Any classical foundation that claims to reproduce quantum statistics must match these fidelity and rate metrics; the GHZ correlations examined here constitute the smallest multipartite instance of that requirement.",
      "reason": "Same issue as H1: uncited discussion of a work without a supporting bibliography citation.",
      "fix": "Cite a specific bibliography entry that provides the stated information, or remove the paragraph if no supporting source exists."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Reference [10] proposes HSH as a local‑realist, measure‑theoretic reconstruction of quantum mechanics, introducing basins of attraction of classical probability measures and a locally bounded hydrodynamic flow as the mechanism for wavefunction relaxation.",
      "reason": "No excerpt from the bibliography for entry [10] is provided, so the claim cannot be verified against the source; this violates citation integrity.",
      "fix": "Either provide a citation to a bibliography entry that contains this specific claim or remove/modify the statement to reflect only supported information."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Reference [11] proves a No‑Spooky‑Action theorem (local operations on one system leave the spatially separated marginal unchanged) and a Correlation History theorem expressing joint statistics as \\(P(o_{1},o_{2})=\\sum_{i}|c_{i}|^{2}P_{1}(o_{1}|\\phi_{1}^{i})P_{2}(o_{2}|\\phi_{2}^{i})\\).",
      "reason": "No excerpt from the bibliography for entry [11] is provided, making the claim unsupported.",
      "fix": "Either supply a supporting citation from the bibliography that contains this theorem statement or remove the claim."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Reference [12] documents an independent audit of PQS, confirming the derivations of the No‑Spooky‑Action and Correlation History theorems and highlighting that any model with local binary response functions and setting‑independent hidden variables must satisfy the same Bell constraints analyzed here.",
      "reason": "No excerpt from the bibliography for entry [12] is provided; the claim cannot be verified and violates citation integrity.",
      "fix": "Provide a citation to a bibliography entry that includes this audit description, or delete/adjust the statement."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The paper lacks the required \"## Appendix B. Claim attribution\" section.",
      "reason": "The required structure includes an Appendix B for claim attribution; its absence violates the mandatory section requirement.",
      "fix": "Add an Appendix B that lists each substantive claim with its source draft attribution and agreement status."
    }
  ],
  "soft": []
}