```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Results item 5 states the coherence-check path costs 266.4 pJ/block vs. 768 pJ/block for TMR (35%), and 266.4 nJ/block with a 1000x cryogenic penalty (347x worse than TMR).",
      "reason": "The 266.4 pJ figure appears only in Section 5 and is never derived in Section 4 with shown arithmetic; no inputs or assumptions for it (per-shot energy, shots per block, interface energy) are stated. Per the quantitative-honesty gate, a quantitative claim must either be derived with shown arithmetic or explicitly labeled a projection with stated assumptions; it is neither.",
      "fix": "Add a derivation in Section 4 (e.g., a subsection 'Quantum checking energy per block') showing the component terms that sum to 266.4 pJ, with each input's status, or relabel the figure as a projection with explicit assumptions."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Section 4.5 states the checker-fidelity constraint epsilon_q <= 6.8e-4, i.e., per-gate error <= 5e-5 on a 13-gate circuit; this constraint is repeated in Results, Discussion, and Appendix A (D6) as a headline falsifiable benchmark.",
      "reason": "The 6.8e-4 threshold is never derived: no arithmetic connects it to the accuracy targets (94.96%, lambda = 4.39e-4) or to the 13-gate circuit depth. The only shown step is 6.8e-4/13 ~ 5e-5, which presumes the threshold. A headline falsifiable number without shown derivation violates the quantitative-honesty gate.",
      "fix": "Derive epsilon_q <= 6.8e-4 in Section 4.5 from the fault model (e.g., show how checker error rate combines with p_eff and rho to bound lambda at the value giving A = 94.96%), stating all intermediate steps and input statuses."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Section 3.1 specifies the syndrome circuit at depth <= 14, but Section 4.3 computes per-call latency using depth 50 (t_call = 10 us + 100 x (50 x 20 ns) = 110 us), and Section 4.5 references a 13-gate circuit.",
      "reason": "Three inconsistent depth figures (14, 50, 13) for the same quantum subroutine make the latency and fidelity budgets internally inconsistent; the reader cannot tell which depth the 110 us latency or the epsilon_q constraint applies to.",
      "fix": "Reconcile to a single stated depth (or explicitly distinguish syndrome-circuit depth from alpha-QPE depth), and recompute t_call and the per-gate error bound against the reconciled value."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "The paper uses specialized terms (Chien search, alpha-QPE, amplitude interception, wall-plug penalty, reset-limited shot rate) with limited explanation.",
      "reason": "Several terms are jargon from coding theory and quantum algorithm literature that are not defined for the systems audience the paper targets (cf. its own curriculum-gap argument in Section 2).",
      "fix": "Add one-sentence definitions at first use for Chien search, alpha-QPE, and reset-limited shot rate, or cite a definitional source."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "The literature treatment of classical ECC (Hamming SEC-DED, BCH shortened codes) and of near-threshold soft-error rates relies on 'standard check-bit counts' and 'datasheet-class assumptions' without citations.",
      "reason": "The quantum-classical hybrid literature is well covered, but the classical reliability side (ECC decoder energy, near-threshold SER scaling) is treated entirely from unstated assumptions, weakening the baseline against which the negative result is measured.",
      "fix": "Add citations or an explicit sensitivity table for e_par and the near-threshold SER scaling, beyond the single 10x discussion in Section 6."
    }
  ]
}
```