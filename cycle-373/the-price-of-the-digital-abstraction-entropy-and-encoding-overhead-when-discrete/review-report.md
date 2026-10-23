{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Draft B referenced a non‑existent citation “[8]” when mentioning the prior version of the paper.",
      "reason": "Meta‑commentary about the drafting process violates the rule prohibiting any discussion of how the paper was written or sources were handled.",
      "fix": "Remove the sentence entirely from Appendix A."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Draft B added a clarification that the twirled channel’s own entropy scales as $\\gamma\\log_2(1/\\gamma)$, while only the excess $\\Delta H$ is linear in $\\gamma$.",
      "reason": "Meta‑commentary about a draft’s addition is prohibited; the paper must not discuss the drafting process.",
      "fix": "Delete this sentence from Appendix A."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "## Appendix B. Claim attribution\n\n| Claim ID | Source Draft(s) | Agreement |\n|----------|----------------|-----------|\n| C1 | A, B | CONVERGENT |\n| ... (entire table) ...",
      "reason": "The entire claim‑attribution appendix is meta‑information about drafts and not part of the scientific content, violating the prohibition on meta‑commentary.",
      "fix": "Remove Appendix B entirely."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "In Section 2 the paper cites works [10] and [11] with generic statements (e.g., “[10] develops Project Rosetta…”, “[11] analyzes constant‑sized‑support magic state distillation…”) without providing a specific point that can be derived from the supplied full‑text excerpts of those works.",
      "reason": "Citation integrity requires each citation to refer to a specific method, result, number, or argument explicitly present in the work’s supplied excerpts; no excerpts for [10] and [11] are provided, making these citations unsupported.",
      "fix": "Either remove the citations to [10] and [11] or replace them with specific statements that can be directly sourced from the provided excerpts of those works."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Reference [8] appears in the References list but is never cited in the main text.",
      "reason": "All listed references must be cited in the paper; an uncited reference violates citation integrity.",
      "fix": "Either cite [8] at an appropriate place with a supported statement from its excerpt or remove [8] from the References list."
    }
  ],
  "soft": []
}