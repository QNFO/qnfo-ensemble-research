{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Our spuriousness criterion explicitly checks that structural‑overlap scores are invariant under lexical perturbations, directly addressing the stability concerns raised in these works.",
      "reason": "The cited works [1]–[8] excerpts do not mention any stability concerns; the claim attributes a concern to them without source support.",
      "fix": "Remove the phrase \"directly addressing the stability concerns raised in these works\" or replace with a statement supported by the cited literature."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The approach in [4] introduces a domain‑adaptive density estimator [4]. This empirical speed‑up justifies the assumption in Section 4.1 that the synthesis‑phase beam search (10 min per candidate) is feasible even when many lexicons are involved.",
      "reason": "The excerpt for [4] only provides the title; it does not contain evidence of an empirical speed‑up or justification for beam‑search feasibility.",
      "fix": "Delete the justification sentence or rephrase to avoid unsupported claim about empirical speed‑up."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The approach in [6] uses a single shared discriminator between two GANs, which simplifies the validation component across multiple crosswalks.",
      "reason": "The excerpt for [6] only states the use of a shared discriminator; it does not claim simplification of validation across crosswalks.",
      "fix": "Remove the unsupported claim about simplifying validation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The approach in [7] learns priors for adversarial autoencoders, emphasizing the need for stable latent representations, which motivates our lexical‑perturbation invariance check (Section 3.3) and the tolerance ε=0.02.",
      "reason": "The excerpt for [7] does not mention stable latent representations; the connection is unsupported.",
      "fix": "Delete or rephrase the sentence to avoid attributing a claim not present in the source."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The study in [10] investigates bijections between unitary elements of C*-algebras and *‑homomorphisms, supporting the use of bijective mappings φij in our truth‑preservation condition.",
      "reason": "No excerpt from [10] is provided; the claim about supporting bijective mappings lacks source evidence.",
      "fix": "Remove the reference to [10] or replace with a supported statement."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The projected statistical power for detecting a novelty increase from 5 % to 15 % is z ≈ 2.728, corresponding to a power of roughly 0.90.",
      "reason": "The power value (≈0.90) is not derived or labeled as a projection; no arithmetic is shown for this quantitative claim.",
      "fix": "Either provide a derivation for the power estimate or remove the statement about power ≈0.90."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "by bridging the engineering lessons of cross‑domain machine‑learning literature [1]–[8] with the ideation vision of the QNFO Consilience Framework [9]–[12]",
      "reason": "The excerpts for references [9]–[12] are not provided; the claim about their content is unsupported.",
      "fix": "Remove the unsupported reference to the QNFO Consilience Framework or provide a supported statement based on available excerpts."
    }
  ],
  "soft": []
}