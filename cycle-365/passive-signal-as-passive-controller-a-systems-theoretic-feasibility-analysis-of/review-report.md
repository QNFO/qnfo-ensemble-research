{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "## 9. Conclusion",
      "reason": "The required heading for the conclusion is \"## 8. Conclusion\". The paper uses \"## 9. Conclusion\", violating the required structure.",
      "fix": "Rename the heading to \"## 8. Conclusion\"."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "- Not checked: each cited source supports the sentence that cites it beyond the retrieved full‑text excerpts, or derivations other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.",
      "reason": "The sentence contains meta‑commentary about source verification and peer review, which is prohibited.",
      "fix": "Remove the entire meta‑commentary sentence."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "**[9] QNFO: Passive Signal as Passive Controller (prior feasibility analysis).** The predecessor formalized the Signal as a discrete‑time block, derived exact passivity for a pure integrator, strict passivity for a leaky integrator with dissipation rate $\\delta = \\alpha - \\tfrac{\\alpha^{2}}{2}$, and a worst‑case quantization degradation of $5.0$ energy units. The present paper re‑derives those results with full arithmetic, fixes the interpretation of the state‑magnitude condition, extends the treatment with an illustrative example, and adds the engineering pathway the predecessor lacked.",
      "reason": "The paper cites specific technical results from [9] without any supporting excerpt from the bibliography entry; the supplied bibliography provides only a title and URL, so the claim is not verifiable from the source.",
      "fix": "Replace the detailed description of [9] with a statement that only the title is known, e.g., \"[9] is the prior feasibility analysis of the Signal‑Worker ontology. The present work builds on its general approach without citing specific technical details from it.\""
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "**[10] QNFO: Structural vs Driven Quantum Coherence.** The corpus paper proposes the Signal‑Worker ontology, built on the premise that information is physical and that maintaining the order of a quantum state has an irreducible energy cost as quantified by Landauer’s principle, making thermodynamic efficiency the ultimate metric for any stabilization mechanism. It introduces two complexity metrics—Krylov complexity for the dynamical complexity of the Worker state and the Lossless Complexity Index (LCI) for the structural complexity of the Signal scaffold—and applies the framework to classify actively driven systems as thermodynamically inefficient and passive structural systems as efficient. The present paper imports no numerical values from that work; the connection is structural and is developed in Section 6.",
      "reason": "The paper makes detailed claims about the content of [10] that are not supported by any excerpt in the supplied bibliography; only the title and URL are given, so the claim cannot be verified.",
      "fix": "Replace the detailed description with a generic statement, e.g., \"[10] introduces the Signal‑Worker ontology and discusses thermodynamic considerations. The present paper references it conceptually without relying on specific quantitative details.\""
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The literature discussion in Section 2 cites eight works but provides only brief summaries; deeper engagement with each work’s methodology and results would strengthen the background.",
      "reason": "The related‑work section is concise and could elaborate more on how each cited work directly informs the present analysis.",
      "fix": "Expand each citation in Section 2 with an additional sentence that connects a specific method or result from the source to the current paper’s derivations."
    }
  ]
}