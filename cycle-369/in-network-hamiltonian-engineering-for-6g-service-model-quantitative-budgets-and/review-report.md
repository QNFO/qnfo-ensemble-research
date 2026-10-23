{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Provenance and AI Involvement\n\n- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.\n- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.\n- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.",
      "reason": "The section contains meta‑commentary about how the paper was produced, the involvement of language models, and the provenance of sources, which is prohibited by the citation‑integrity and prose‑gate rules.",
      "fix": "Remove the entire \"Provenance and AI Involvement\" section or replace it with a neutral statement that does not reference the pipeline, models, or source acquisition."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Reference [5] introduces a framework that systematically accounts for higher‑order contributions to the Floquet–Magnus expansion, and shows that sequence‑structure can suppress first‑order cross terms while providing explicit second‑order commutator estimates.",
      "reason": "The bibliography excerpt for [5] only provides the title and does not contain the specific methodological details claimed; thus the statement is not supported by the supplied full‑text excerpt.",
      "fix": "Replace the sentence with a claim that is directly supported by the excerpt, e.g., \"Reference [5] presents higher‑order methods for Hamiltonian engineering pulse‑sequence design.\""
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Reference [8] describes the orders‑of‑magnitude discrepancy between microsecond‑scale network jitter and nanosecond‑scale quantum coherence, establishing the need for timing‑aware quantum control in 6G networks and reporting transverse coherence times $T_{2}^{*}$ of $10$–$100\\,\\mu\\mathrm{s}$ in current solid‑state systems.",
      "reason": "No excerpt from [8] is provided; the claim cannot be verified against the supplied bibliography entry.",
      "fix": "Remove or rephrase the sentence to only state that [8] is a QNFO paper on in‑network Hamiltonian engineering without asserting specific content."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Reference [9] presents the initial service‑model, quantitative budgets, and re‑entry analysis for in‑network Hamiltonian engineering, providing the baseline numbers that are re‑derived and corrected in this work.",
      "reason": "No excerpt from [9] is provided; the specific content claimed is not supported by the supplied bibliography entry.",
      "fix": "Remove the sentence or replace it with a neutral citation that does not assert unsupported details."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Reference [4] maps literature on cognitive biases that affect software‑engineering projects, highlighting systematic human errors that can lead to template‑mismatch failure modes discussed in Section 8.",
      "reason": "The excerpt for [4] is not provided; the specific claim about mapping literature cannot be verified.",
      "fix": "Replace with a statement that only reflects the title, e.g., \"Reference [4] studies cognitive biases in software engineering.\""
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Reference [6] proposes a comprehensive benchmarking infrastructure that quantifies uncertainty in derived metrics, which we adopt to propagate a $5\\%$ relative uncertainty on the per‑cycle error $\\epsilon_{c}$ in Section 8.",
      "reason": "No excerpt from [6] is provided; the claim about its content is unsupported.",
      "fix": "Modify to a generic statement such as \"Reference [6] discusses benchmarking infrastructure for software engineering metrics.\""
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Reference [7] discusses challenges in integrating AI tools into development pipelines, shaping our perspective on automated template generation, verification, and maintenance for the HES library.",
      "reason": "No excerpt from [7] is provided; the specific discussion claimed is not supported by the supplied bibliography entry.",
      "fix": "Replace with a minimal claim like \"Reference [7] addresses AI‑driven software engineering outlook.\""
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Reference [8] documents jitter values of $100$–$500\\,\\mu\\mathrm{s}$ in contemporary 6G packet networks, far exceeding the $8\\,\\mu\\mathrm{s}$ cycle period.",
      "reason": "The excerpt for [8] does not contain jitter values; the claim is unsupported.",
      "fix": "Remove the jitter value claim or qualify it as an assumption without citation."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The paper provides a comprehensive literature review but could elaborate more on how each cited work directly informs the derivations.",
      "reason": "Depth of literature treatment is limited.",
      "fix": "Add brief explanations linking each citation to specific derivations."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Appendix A is present, but Appendix B is missing despite being referenced in the version history.",
      "reason": "Missing Appendix B may affect completeness.",
      "fix": "Either include Appendix B or remove references to it."
    }
  ]
}