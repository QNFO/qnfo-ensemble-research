```json
{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Under the alternative (per-node geometric cost) convention, q = 3 is the optimal radix at baseline assumptions (B = 10^7 J, c0' = 10^3 J/node), yielding 8.789 nats (Sections 4.3, 5 item 6, Abstract, Conclusion).",
      "reason": "The candidate set omits q = 6. With nodes ≤ 10^4: 6^(L+1) ≤ 60001 gives 6^6 = 46656 ≤ 60001 < 6^7, so L = 5 and G = 5 ln 6 = 8.959 nats, with node count (6^6 − 1)/5 = 9331 ≤ 10000. This strictly dominates the claimed optimum q = 3 (8.789 nats). The headline 'q = 3 optimal' result of the alternative convention is therefore an arithmetic/search error, and it propagates to the Abstract, Results, and Conclusion ('q = 3 optimal at baseline assumptions').",
      "fix": "Extend the exhaustive integer search in Section 4.3 to all q ≥ 2 (at least through q where q^(L+1) first exceeds the node budget), recompute the ranking, and correct the Abstract, Section 4.3, Results item 6, and Conclusion. If q = 6 (or another radix) becomes the optimum, restate the 5.7%-over-binary advantage and the 'sub-1% margins' characterization accordingly."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The reconciliation of the two cost conventions 'is documented explicitly in Appendix A' (Abstract, Section 3).",
      "reason": "No Appendix A appears in the manuscript; the referenced divergence documentation is missing.",
      "fix": "Add Appendix A containing the draft-divergence reconciliation, or remove the references to it."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Discussion states 'in the alternative convention the integer grid can produce spurious winners (e.g., q = 10 achieving 9.210 nats there)'.",
      "reason": "Under the per-node geometric cost model actually used in Section 4.3, q = 10 yields L = 3 and G = 3 ln 10 = 6.908 nats, not 9.210; the 9.210 figure belongs to the exponential-cost bound where q drops out entirely. The example as stated is internally inconsistent.",
      "fix": "Correct or replace the q = 10 example with a case where the integer grid genuinely produces a counterintuitive winner under the geometric cost model."
    },
    {
      "id": "S3",
      "severity": "SOFT",
      "claim": "The primary-convention cost model prices only build-time node and interconnect costs.",
      "reason": "The paper itself concedes (Section 6, falsification condition (b)) that traversal energy — the quantity the joules-per-solution framework would measure — is excluded, yet the Abstract and Conclusion present the 22.2% saving without that caveat attached inline.",
      "fix": "State the build-cost-only scope of the 22.2% figure explicitly at first mention in the Abstract and Conclusion."
    }
  ]
}
```