{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The paper includes references [3] through [12] in the text and reference list, but the provided bibliography contains only entries [1] and [2].",
      "reason": "Citation integrity violation: references must appear in the supplied bibliography.",
      "fix": "Remove or replace all citations to [3]–[12] with citations to existing bibliography entries or omit them."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The statement \"The adjacency operator $A_{p}$ on $\\mathcal{T}_{p}$ has spectrum $\\sigma(A_{p})=[-2\\sqrt{p},\\,2\\sqrt{p}]\" is cited to [10], but the supplied bibliography does not contain entry [10] nor any excerpt confirming this claim.",
      "reason": "Citation integrity violation: the claim is not supported by any provided source.",
      "fix": "Either provide a supported citation from the existing bibliography that contains this result, or remove the citation and treat the spectrum as derived in the paper without external reference."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Multiple statements throughout the paper (e.g., joint‑fit probability from [11], Efimov factor discussion from [12]) cite works that are not present in the supplied bibliography.",
      "reason": "Citation integrity violation: all cited works must be present in the bibliography.",
      "fix": "Delete or replace citations to [11] and [12] with appropriate references from the bibliography, or rephrase the statements without unsupported citations."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The literature review in Section 2 mentions many works but provides only brief, sometimes generic descriptions, lacking depth and detailed connection to the current analysis.",
      "reason": "The treatment of related work is superficial and could be expanded to better contextualize the contribution.",
      "fix": "Enrich Section 2 with more detailed discussion of each cited work’s specific results that directly support the paper’s arguments, ensuring each point is grounded in the supplied excerpts."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Appendix A states that no divergent claims were identified, but the review found multiple citation inconsistencies that could be considered divergences among drafts.",
      "reason": "The divergence report may be inaccurate given the citation issues.",
      "fix": "Update Appendix A to reflect the citation inconsistencies as a form of divergence, or clarify that the divergences pertain only to substantive quantitative claims."
    }
  ]
}