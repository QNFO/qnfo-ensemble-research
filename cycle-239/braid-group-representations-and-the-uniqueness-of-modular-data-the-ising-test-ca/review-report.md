{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "## References\n\n[5] (reference details not provided in source).\n[12] (reference details not provided in source).\n[13] (reference details not provided in source).\n[14] (reference details not provided in source).",
      "reason": "Citation entries are incomplete or missing; required to copy titles and identifiers exactly from the provided bibliography. Entries [13] and [14] do not exist in the bibliography at all, and [5] and [12] lack the required details.",
      "fix": "Replace each reference with a correct entry copied verbatim from the bibliography, e.g., for [5] use \"[5] arXiv:1907.02664v2 | Data Encoding for Byzantine-Resilient Distributed Optimization\" and for [12] use \"[12] QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors | https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero\". Remove references [13] and [14] entirely."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Interferometric braiding of non‑Abelian anyons [7] proposes a concrete protocol to “experimentally measure the matrix elements of the $R$‑symbols” using mobile impurities with addressable spin states.",
      "reason": "The bibliography entry for [7] does not contain any excerpt supporting this specific claim; the paper cites a detail that cannot be derived from the supplied source.",
      "fix": "Either remove the claim or replace it with a statement directly supported by the excerpt of [7] (if any). If no supporting text exists, delete the sentence."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Majorana braid representation fixes local $F$ and $R$ symbols [12] asserts that “the braid representation $\rho(\sigma_i)=\\frac{1}{\\sqrt{2}}(1+\\gamma_{i+1}\\gamma_i)$ uniquely fixes the local $F$ and $R$ symbols of the Ising category, thereby determining the $T$‑matrix.”",
      "reason": "No excerpt for [12] is provided; the statement cannot be verified against the source and thus violates source‑support rule.",
      "fix": "Delete or re‑phrase the sentence to only include information that is present in the excerpt for [12]; if none, remove the citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The infinite family of braid‑group representations constructed from the spherical double affine Hecke algebra of type $C^{\\vee}C_{1}$ provides a concrete source of non‑dense images, as demonstrated by the correspondence between Lagrangian $A$‑branes and finite‑dimensional DAHA modules [4].",
      "reason": "No excerpt for [4] is supplied; the claim cannot be substantiated from the bibliography.",
      "fix": "Remove the sentence or replace it with a claim that is directly supported by the excerpt of [4]; if no excerpt exists, delete the citation."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Defect‑operator analyses in the AdS/CFT correspondence show that braid representations can be embedded in holographic settings, linking topological data to conformal field theory operators [6].",
      "reason": "No excerpt for [6] is provided; the statement is unsupported.",
      "fix": "Delete the sentence or replace it with a claim supported by the excerpt for [6]; if none, remove the citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Numerical extraction of $S$ and $T$ from simulated braid matrices has been achieved with anyonic tensor‑network algorithms, confirming that the analytical pipeline matches independent computational approaches [11].",
      "reason": "The bibliography entry for [11] does not contain an excerpt that supports this specific claim; thus it violates source‑support rule.",
      "fix": "Remove or re‑write the sentence to reflect only what is present in the excerpt for [11]; if no supporting text, delete the citation."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "## 6.1 Extended Derivations and Worked Examples\n\n... (section heading and content)",
      "reason": "The required section heading after Results is \"## 6. Discussion\". Introducing sub‑sections \"6.1\" and \"6.2\" before the mandated \"6. Discussion\" breaks the required structure and ordering of sections.",
      "fix": "Replace the sub‑section headings with a single section \"## 6. Discussion\" that incorporates the extended derivations, and renumber subsequent sections accordingly."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "## 10. Conclusion\n\n... (conclusion text)",
      "reason": "The required heading for the concluding section is \"## 8. Conclusion\". Using \"## 10. Conclusion\" violates the prescribed section order and numbering.",
      "fix": "Rename the heading to \"## 8. Conclusion\" and adjust the numbering of any following sections so that the overall order matches the specification."
    }
  ],
  "soft": []
}