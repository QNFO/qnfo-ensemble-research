{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "*Counterfactual knowledge tracing* – [3] reports that the RCKT framework “uses counterfactual reasoning to quantify the response influences” and “outperforms most existing KT methods” (§ VI Conclusion).",
      "reason": "The bibliography does not provide any excerpt from work [3]; therefore the statement cannot be verified from the supplied source and violates citation integrity.",
      "fix": "Delete the sentence or replace it with a claim that can be supported by an available excerpt; for example, remove the citation to [3] entirely."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Draft A reports a concrete asymmetric advantage of **$2.8$ utility units** (Section 4.2) derived from a hidden‑state distribution $P(h_{0})=0.7$, $P(h_{1})=0.3$ and payoffs \\{8,2,1,9\\}. Draft B reports a different advantage of **$2.4$ utility units** (Section 4.2) based on a signal‑accuracy parameter $q=0.8$, prior $p_{0}=0.5$, and payoffs \\{+10,-6,0\\}. Because Draft B also introduces citations [9]–[11] that are absent from the supplied bibliography, the reconciled paper adopts the quantitative framework and citation set of Draft A. The alternative numeric scenario from Draft B is therefore omitted.",
      "reason": "The paragraph discusses internal draft versions, which is meta‑commentary about the paper’s creation and violates the rule prohibiting any mention of drafts, authorship, or AI.",
      "fix": "Remove the entire Appendix A section or rewrite it to report divergence without referring to specific drafts, e.g., simply state that a numerical divergence existed and the chosen numbers are those presented in the main text."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "## Appendix B. Claim attribution\n| Claim ID | Source Draft(s) | Agreement |\n|----------|----------------|-----------|\n| C1 | A, B, C | CONVERGENT |\n| C2 | A, B, C | CONVERGENT |\n| ... (full table) ...",
      "reason": "The appendix lists the internal drafts and their contributions, which is meta‑commentary about the writing process and is prohibited.",
      "fix": "Delete Appendix B entirely, as it is not required by the paper format and violates the no‑meta‑commentary rule."
    }
  ],
  "soft": []
}