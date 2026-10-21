{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Derived per‑case constant: $$0.5\\ln(2\\pi\\lambda) = 0.5\\bigl(\\ln(2\\pi) + \\ln\\lambda\\bigr) = 0.5(1.837877 + 4.605170) = 3.221524.$$",
      "reason": "Arithmetic error: 0.5*(1.837877+4.605170) = 3.2210235, not 3.221524.",
      "fix": "Recompute the constant as 3.221024 (rounded to six decimal places) and propagate the corrected value through all subsequent Gaussian log‑density and Δ calculations."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Stable‑but‑Wrong demonstrates that accumulating more data can degrade scientific conclusions when an unobservable drift degrades observation validity, exposing a structural epistemic trap [5].",
      "reason": "Citation [5] is used to support a claim that is not present in the supplied excerpt for that work; no supporting text is available.",
      "fix": "Remove or replace the sentence with a claim that can be directly supported by the excerpt of [5], or omit the citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Position: Certifiable State Integrity argues that local validity specifications are more useful than a single global scale for safety‑critical cyber‑physical systems, and that local evidence boundaries can be traced and composed [7].",
      "reason": "Citation [7] is used without a supporting excerpt; the claim cannot be verified from the provided bibliography.",
      "fix": "Delete or re‑phrase the sentence to reflect only information present in the excerpt of [7], or remove the citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The classification of unitary elements of C*‑algebras shows that representation‑invariant quantities (e.g., K‑theory classes) can be identified across different morphisms [3].",
      "reason": "No excerpt for [3] is provided; the statement is unsupported.",
      "fix": "Remove the sentence or replace it with a claim directly supported by the excerpt of [3] if available."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Improving problem solving by exploiting symmetry demonstrates that changing the representation of a problem (via symmetry transformations) can preserve solution structure while exposing non‑invariant aspects [6].",
      "reason": "Citation [6] lacks a supporting excerpt; the claim is not verifiable.",
      "fix": "Delete or modify the sentence to match the content of the excerpt for [6], or drop the citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The Annotation Scarcity Paradox surveys how evaluation bottlenecks limit epistemic confidence in low‑resource NLP, highlighting a structural limitation on what can be known [9].",
      "reason": "No excerpt for [9] is provided; the claim cannot be substantiated.",
      "fix": "Remove or replace the sentence with a statement that can be directly sourced from the excerpt of [9], or omit the citation."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "The topological description of Legendrian contact homology records a canonical isomorphism between singular and de Rham homology, a clean instance of invariance under a change of chain representation [10].",
      "reason": "Citation [10] lacks a supporting excerpt; the claim is unsupported.",
      "fix": "Delete or adjust the sentence to reflect only what is present in the excerpt of [10], or remove the citation."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Exact reduction under a stated constraint shows that a stationary scalar correlation energy admits an exact one‑mode terminal representation only under a stationarity constraint [11].",
      "reason": "No excerpt for [11] is provided; the claim cannot be verified.",
      "fix": "Remove or replace the sentence with content supported by the excerpt of [11], or drop the citation."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "The prior version of this framework defined local charts, the restricted product, and the invariant core, and reported the Poisson‑to‑Gaussian arithmetic summarized in its Results [12].",
      "reason": "Citation [12] is a QNFO work without a supplied excerpt; the statement cannot be confirmed.",
      "fix": "Delete or re‑write the sentence to avoid unsupported reference to [12]."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "Self‑declared validity domains propose an epistemology that explicitly separates ontological territory from epistemic maps and declares its own domain of validity [13].",
      "reason": "No excerpt for [13] is provided; the claim is unsupported.",
      "fix": "Remove or replace the sentence with a claim that can be sourced from the excerpt of [13], or omit the citation."
    },
    {
      "id": "H11",
      "severity": "HARD",
      "claim": "The validation metric problem identifies the lack of objective validation mechanisms for non‑empirical contributions [14].",
      "reason": "Citation [14] lacks a supporting excerpt; the claim cannot be verified.",
      "fix": "Delete or modify the sentence to align with the excerpt of [14], or drop the citation."
    },
    {
      "id": "H12",
      "severity": "HARD",
      "claim": "In Section 7(a) the paper repeats the unsupported claim that local validity specifications are more useful than a global scale for safety‑critical systems [7].",
      "reason": "Citation [7] is again used without supporting excerpt, violating citation integrity.",
      "fix": "Remove or re‑phrase the sentence to avoid the unsupported citation."
    }
  ],
  "soft": []
}