{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Consequently,\n\\theta_\\sigma = (R^{\\sigma\\sigma}_1)^2 = e^{-i\\pi/4},\nwhere we used the fact that \\theta_1=1 and $d_1=1$.\n...\nWe have $\\theta_1=1$, $\\theta_\\psi=-1$, and $\\theta_\\sigma=e^{-i\\pi/4}$ (from Section 4.2).\n...\n\\frac{1}{\\mathcal{D}}\\sum_a d_a^2\\theta_a = \\frac{1}{2}\\bigl(1 - 1 + 2\\,e^{i\\pi/8}\\bigr) = e^{i\\pi/8}.",
      "reason": "The paper gives contradictory values for the topological spin $\\theta_\\sigma$: first $e^{-i\\pi/4}$, then uses $e^{i\\pi/8}$ in the Gauss–Milgram sum, and later states $\\theta_\\sigma = e^{i\\pi/8}$ in the Results. This inconsistency invalidates the quantitative conclusions.",
      "fix": "Choose a single consistent value for $\\theta_\\sigma$ derived from the hexagon solution (i.e., $\\theta_\\sigma = e^{-i\\pi/4}$) and recompute the Gauss–Milgram sum accordingly, updating all downstream statements (Results, Discussion, Practical Implications) to reflect the corrected value."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Ref. [5] provides a review of Ising anyons in spinless $p$‑wave superconductors. This review supplies the categorical framework used throughout our derivations.",
      "reason": "No excerpt from the bibliography entry for [5] is provided, so the citation lacks a verifiable source. Citation integrity requires that every cited work be supported by supplied text.",
      "fix": "Remove the citation to [5] or replace it with a citation to a work whose excerpt is available and that explicitly contains the needed categorical framework."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The literature on Majorana‑based topological superconductivity provides concrete models, experimental protocols, and theoretical tools that inform our analysis.\n\n1. **Braiding of Majorana corner states.** Ref. [1] ...\n2. **Intervortex tunneling and energy splitting.** Ref. [2] ...\n3. **Majorana modes on Josephson vortices.** Ref. [3] ...\n4. **Ising anyon theory and modular data.** Ref. [5] ...\n5. **Electrical detection of the Majorana fusion rule.** Ref. [6] ...\n6. **Explicit braid matrix from tunneling networks.** Ref. [7] ...\n7. **Spontaneous surface currents in chiral $p$‑wave superconductors.** Ref. [8] ...\n8. **Topological invariants via Wilson loops.** Ref. [1] also ...",
      "reason": "Only seven distinct bibliography entries ([1],[2],[3],[5],[6],[7],[8]) are discussed, but the requirement is to discuss at least eight works. Moreover, [5] lacks an excerpt, violating citation rules.",
      "fix": "Add a discussion of an additional distinct work (e.g., [4] or another available entry) with a specific point supported by its excerpt, and ensure all cited works have supporting excerpts."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "## 7. Practical Implications and Engineering Pathways\n...\n## 8. Conclusion\n...\n## References\n...\n## Appendix A. Divergence report\n...\n## Appendix B. Claim attribution",
      "reason": "The required section order ends with ## 8. Conclusion followed by ## References. The paper inserts an extra ## 10. Conclusion later, creating duplicate conclusion sections and breaking the prescribed structure.",
      "fix": "Remove the extra ## 10. Conclusion section, renumber sections to follow the required order, and ensure the paper ends after the Conclusion and References."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "We compute\n\\kappa_{xy}= \\frac{\\pi^{2}k_{B}^{2}}{6h}\\,c\\,T,\nwhere $T$ is the temperature. Inserting $c=1/2$ yields\n\\kappa_{xy}= \\frac{\\pi^{2}k_{B}^{2}}{12h}.\nFor a typical dilution‑refrigerator temperature $T=20\\,$mK, the numerical value is\n\\kappa_{xy}\\approx \\frac{\\pi^{2}(1.38\\times10^{-23}\\,\\text{J/K})^{2}}{6(6.626\\times10^{-34}\\,\\text{J·s})}\\times 20\\times10^{-3}\\,\\text{K}\n\\approx 9.5\\times10^{-15}\\,\\text{W/K},\nproviding a concrete target for the experiment described in Section 8(c).",
      "reason": "The derivation uses $c=1/2$, which contradicts the corrected $\\theta_\\sigma$ value (see H1). The numerical result depends on the inconsistent $c$, making the quantitative claim unsupported.",
      "fix": "Recalculate $\\kappa_{xy}$ using the correct $c$ derived from the consistent $\\theta_\\sigma$, or label the result as a projection with explicit assumptions if the correct $c$ is uncertain."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The MAJORANA collaboration, described in \\cite{4}, plans a 40 kg germanium detector array for neutrinoless double‑beta decay searches. Although unrelated to braiding, this illustrates the scale of modern low‑background cryogenic experiments and underscores the feasibility of building large‑scale, ultra‑clean platforms that could eventually host the thermal‑Hall measurement outlined above.",
      "reason": "The statement attributes capabilities (large‑scale, ultra‑clean platforms) to the MAJORANA collaboration without direct support from the excerpt of [4]; the excerpt does not contain such claims, violating citation integrity.",
      "fix": "Remove or rephrase the claim to only reflect information explicitly present in the excerpt of [4], or replace the citation with a work whose excerpt supports the statement."
    }
  ],
  "soft": []
}