{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The paper cites [9] to claim that \"A Post‑Quantum Associative Memory establishes that content‑addressable memory can achieve capacities far beyond classical limits\".",
      "reason": "No excerpt from the bibliography entry [9] is provided; the claim cannot be verified against the source, violating citation integrity.",
      "fix": "Remove the citation of [9] or replace it with a citation to a work whose excerpt supports the claim (e.g., [1] or [2])."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The paper cites [10] to state that \"Modern Methods in Associative Memory surveys dense associative networks, their energy formulations, and implementation toolkits\".",
      "reason": "No excerpt from entry [10] is supplied; the statement is not grounded in the provided text, violating citation integrity.",
      "fix": "Delete the citation of [10] or find a supported claim from an excerpted source."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The paper cites [11] to note that \"Associative Memory and Dead Neurons identifies flat energy regions caused by saturated activations\".",
      "reason": "No excerpt from entry [11] is provided; the claim lacks source support.",
      "fix": "Remove the citation of [11] or replace with a supported citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The paper cites [13] (QNFO) to argue that \"semantic memory relies on ultrametric topologies and proposes validation strategies for such structures\".",
      "reason": "No excerpt from entry [13] is supplied; the claim cannot be verified and violates the rule for QNFO works.",
      "fix": "Delete the citation of [13] or ensure the claim matches an explicitly provided excerpt."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The paper cites [14] (QNFO) to state that \"QNFO: Projective Geometric Frameworks for Semantic Structures synthesizes ultrametric spaces and verifies equivalence metrics\".",
      "reason": "No excerpt from entry [14] is provided; the citation is unsupported.",
      "fix": "Remove the citation of [14] or replace with a supported source."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "In Section 5 the paper references the Hopfield loading limit α≈0.138 [7] as a comparison.",
      "reason": "No excerpt from entry [7] is supplied; the citation lacks source support.",
      "fix": "Delete the citation of [7] or replace with a supported citation."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "In Section 3.3 the paper cites [8] for an energy‑guarantee analogy.",
      "reason": "No excerpt from entry [8] is supplied; the citation is unsupported.",
      "fix": "Remove the citation of [8] or provide a supported claim from an excerpted source."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Abstract states a speedup of 4.2×10⁴ over linear scan.",
      "reason": "Derived speedup in Section 4 is 4.17×10⁴; the abstract value is neither derived nor labeled as a projection, constituting an unjustified quantitative claim.",
      "fix": "Replace the abstract speedup with the derived value 4.17×10⁴ or label it as a projection with explicit assumptions."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Section 7 provides projected compute cost (≈$0.0002 per 1 k queries), storage cost (≈$0.023 per month), and latency (≤5 ms) without showing arithmetic or labeling them as projections.",
      "reason": "Quantitative projections lack derivation and are not marked as projections with stated assumptions, violating quantitative honesty.",
      "fix": "Label these figures as projections, cite the assumptions used, or remove/adjust them to reflect derived values."
    }
  ],
  "soft": []
}