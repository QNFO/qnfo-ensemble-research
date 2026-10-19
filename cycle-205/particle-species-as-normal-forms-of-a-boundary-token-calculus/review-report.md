{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The count of particle‑type classes $N_{\\!sp}=5$ satisfies the species‑entropy relation ${\\cal S}_{\\!sp}\\simeq N_{\\!sp}$ reported in [3].",
      "reason": "The bibliography entry [3] provides only a general analysis of particle species and the species scale in quantum gravity; it does not state a specific relation ${\\cal S}_{\\!sp}\\simeq N_{\\!sp}$ linking entropy to the count of species.",
      "fix": "Remove or rephrase the statement to avoid asserting a specific relation not present in [3]; alternatively, label it as a projection with explicit assumptions."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The Getzler‑type rescaling calculus for foliations is discussed in [4]; we note that the BTC’s graded rewrite rules share a similar hierarchical structure.",
      "reason": "The excerpt from bibliography [4] describes a symbol calculus for foliations but does not mention any hierarchical structure or similarity to BTC rewrite rules.",
      "fix": "Delete the unsupported comparison or replace it with a statement directly supported by the excerpt, e.g., simply cite [4] for its discussion of a symbol calculus without drawing similarity."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The spin‑statistics theorem emerges in the STC from the geometry of the cross‑ratio: symmetric patterns reduce under Calling, antisymmetric patterns persist under Crossing, reproducing bosonic and fermionic exchange behavior respectively [7].",
      "reason": "Bibliography entry [7] provides only a URL with no excerpt; no specific claim about the spin‑statistics theorem or cross‑ratio geometry is supplied, so the citation lacks grounding.",
      "fix": "Remove the citation or replace it with a statement that does not rely on unsupported content; if retained, label the claim as a projection with assumptions."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "We reference [8] for context but do not claim exclusivity of the Syntactic Token Calculus in predicting Higgs resonances or providing falsifiable predictions.",
      "reason": "Bibliography entry [8] contains only a URL with no excerpt; the paper does not provide a specific point from that work to justify the citation.",
      "fix": "Delete the citation or replace it with a statement supported by an excerpt; if kept, ensure it only mentions that the work exists without asserting any specific content."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The computational‑syntax manuscript argues that the primitives “Mark” and “Void” generate all observable structure, motivating the BTC’s minimal token set [9].",
      "reason": "Bibliography entry [9] provides only a URL with no excerpt; the paper does not present a specific claim from that source to justify the citation.",
      "fix": "Remove the citation or rephrase the sentence to avoid attributing a specific claim to [9] without supporting excerpt."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Using a standard workstation, the implementation cost is negligible (order of $1\\,\\text{k}$).",
      "reason": "The cost estimate is a quantitative claim not derived in the analysis, not labeled as a projection, and lacks any source or arithmetic justification.",
      "fix": "Label the cost as a projection with explicit assumptions or remove the specific dollar amount."
    }
  ],
  "soft": []
}