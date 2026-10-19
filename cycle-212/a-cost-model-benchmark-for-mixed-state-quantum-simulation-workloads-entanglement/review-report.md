{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Entries [11] and [12] lack substantive excerpts; future work could integrate their benchmarking and coherence‑taxonomy material once full texts are available.",
      "reason": "The paper references a bibliography entry [12] that does not exist in the provided bibliography, violating citation integrity. Additionally, the sentence comments on the availability of source excerpts, which is prohibited meta‑commentary about sources.",
      "fix": "Remove the entire sentence or replace it with a statement that does not reference missing entries or discuss source availability."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Entries [11] and [12] lack substantive excerpts; future work could integrate their benchmarking and coherence‑taxonomy material once full texts are available.",
      "reason": "The sentence discusses the lack of excerpts for bibliography entries, which is disallowed meta‑commentary about how the sources were obtained.",
      "fix": "Delete the sentence or rephrase to omit any mention of source availability."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Background and Related Work provides only high‑level analogies without detailed explanation of how each cited work directly supports the benchmark design.",
      "reason": "The literature review could be deepened by explicitly linking each cited result to specific components of the benchmark methodology.",
      "fix": "Add brief explanations for each cited work showing the concrete method or result it contributes to the benchmark."
    }
  ]
}