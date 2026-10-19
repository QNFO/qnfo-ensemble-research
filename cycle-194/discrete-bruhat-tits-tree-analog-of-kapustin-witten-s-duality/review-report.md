{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The adjacency spectral radius for $p=2$ is $\\rho(A)=2.8284271\\ldots$, confirming the tree’s ultrametric spectral bound [11].",
      "reason": "The bibliography entry [11] does not contain any excerpt supporting a claim about the spectral radius or an ultrametric spectral bound; the citation is therefore unsupported.",
      "fix": "Remove the citation to [11] or replace it with a statement labeled as a projection without a bibliography reference."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Eq. (4.11)",
      "reason": "The paper references equation (4.11), but no such equation is defined anywhere in the manuscript; this is a broken cross‑reference.",
      "fix": "Delete the reference to Eq. (4.11) and rephrase the sentence to avoid the nonexistent equation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Discrete‑time analog transmission and high PAPR. DeepJSCC‑based semantic communications employ discrete‑time analog transmission, which yields continuous‑amplitude signals with high peak‑to‑average power ratio [3]. The analogy between continuous amplitudes on a tree edge and analog signal amplitudes informs our interpretation of Wilson line phases.",
      "reason": "The excerpt from bibliography entry [3] discusses peak‑to‑average power ratio in semantic communications and does not provide any statement about an analogy between tree‑edge amplitudes and analog signal amplitudes; the citation is unsupported.",
      "fix": "Remove the citation to [3] and rephrase the sentence as an informal analogy without a bibliography reference."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "reproducing known p‑adic geometric Langlands statements [8]",
      "reason": "Bibliography entry [8] is titled about Archimedean place measure‑theoretic artifacts and does not contain any excerpt stating p‑adic geometric Langlands results; the citation is unsupported.",
      "fix": "Delete the citation to [8] or replace it with a projection label indicating the claim is not directly sourced."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "matching the p‑adic geometric Langlands eigen‑sheaf condition [8]",
      "reason": "As with H4, entry [8] does not provide an excerpt supporting a claim about p‑adic geometric Langlands eigen‑sheaf conditions; the citation is unsupported.",
      "fix": "Remove the citation to [8] and label the statement as a projection or hypothesis without a bibliography reference."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The literature discussion in Section 2 provides only brief one‑sentence summaries of each work.",
      "reason": "The background treatment could be expanded to give deeper context for each cited work.",
      "fix": "Add one or two additional sentences per citation that elaborate on the specific methods or results drawn from the excerpts."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "The paper does not explicitly restate the real‑world problem in the Introduction after the contributions list.",
      "reason": "While the problem is introduced, a concise statement of the practical impact could be clearer.",
      "fix": "Insert a brief concluding sentence in the Introduction summarizing the ‘so what?’ impact."
    }
  ]
}