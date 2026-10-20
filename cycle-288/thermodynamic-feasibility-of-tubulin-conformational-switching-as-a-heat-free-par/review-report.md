{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Dipole‑field state‑energy difference ≈ 7.21 kBT; thermal error probability ≈ 3×10^{-9}.",
      "reason": "The quantitative values are not derived in the analysis nor labeled as projections with stated assumptions; the derivation in Section 4.3 yields 9.28 kBT and a different error probability.",
      "fix": "Replace the claim with the derived value (≈9.28 kBT) and the corresponding error probability (≈9.3×10^{-5}), or label the 7.21 kBT figure explicitly as a projection with its assumptions."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "a dipole‑mediated state‑energy difference of $7.21\\,k_{B}T$, and a screened nearest‑neighbor coupling of $0.17\\,k_{B}T$.",
      "reason": "The dipole‑mediated energy difference of 7.21 kBT is not derived in the paper; Section 4.3 derives a different value. The coupling of 0.17 kBT is presented without labeling it as a projection.",
      "fix": "State the derived coupling value (0.0216 kBT) and, if keeping the 0.17 kBT figure, label it as an upper‑bound projection with explicit assumptions."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Skrzypczak et al. [2] demonstrate a GPU‑accelerated parallel Tabu Search, showing that massive data‑parallel kernels can evaluate local update rules efficiently, a capability required for simulating tubulin‑based automata.",
      "reason": "The excerpt for [2] does not contain any statement about \"massive data‑parallel kernels can evaluate local update rules efficiently\"; the citation is used without a specific supported point.",
      "fix": "Replace the sentence with a statement directly supported by the excerpt, e.g., describing the parallel Tabu Search algorithm itself, or remove the citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Work on the conformational change of tubulin [4] motivates treating the dimer switch as a mechanical displacement; the nanometer magnitude of the displacement is an assumption of this paper, not a measurement.",
      "reason": "No excerpt from [4] is provided; the paper cites it without a specific supported point from its full text.",
      "fix": "Either provide a specific claim from the excerpt of [4] that justifies the mechanical model, or remove the citation."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The Message Passing Fluids abstraction, in which molecules act as processes in a parallel computational fluid [5], motivates our cellular‑automaton view of tubulin dimers as computational agents.",
      "reason": "The excerpt for [5] is not supplied; the citation lacks a directly supported statement.",
      "fix": "Replace with a statement that is directly supported by the excerpt of [5], or drop the citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "GPU‑accelerated parallel implementations of irregular, neighbor‑based computations [8] indicate that local update rules can be executed at high throughput on modern hardware, a capability required for simulating tubulin‑based automata.",
      "reason": "No excerpt for [8] is provided; the citation is used without a specific supported point.",
      "fix": "Remove or replace the sentence with a claim directly supported by the excerpt of [8], if available."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Finally, the map‑territory distinction highlighted by [10] warns against conflating the transistor metaphor (map) with the actual physical substrate (territory); our quantitative budget explicitly tests the map against the territory.",
      "reason": "The excerpt for [10] is not supplied; the citation lacks a directly supported statement.",
      "fix": "Either supply a specific point from the excerpt of [10] that matches the claim, or remove the citation."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "The Bekenstein bound limits the information capacity of a finite region of space [11]; we use this bound to verify that the proposed bit density does not violate fundamental physics.",
      "reason": "No excerpt for [11] is provided; the citation is used without a directly supported statement.",
      "fix": "Provide a specific supported statement from the excerpt of [11] or delete the citation."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Missing Appendix B. Claim attribution section required by the paper template.",
      "reason": "The paper includes Appendix A but omits the required Appendix B, violating the required structure.",
      "fix": "Add an Appendix B that lists each claim (C1…Cn) with source draft attribution and agreement status."
    }
  ],
  "soft": []
}