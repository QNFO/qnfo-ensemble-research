{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Reference [9] observes that in any integer base $b\\ge 2$ the digit string “10” denotes the number $b$.",
      "reason": "The bibliography entry for [9] does not contain this statement; the claim is not derivable from the supplied excerpt, violating citation integrity.",
      "fix": "Remove the sentence or replace it with a statement that is directly supported by an available source."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Reference [11] proves (Theorem 1) that, assuming $\\text{BPP} \\neq \\text{BQP}$, there exist decision problems that are efficiently solvable by quantum computers but not by any classical probabilistic algorithm.",
      "reason": "No excerpt for [11] is provided; the claim cannot be verified against the bibliography, violating citation integrity.",
      "fix": "Delete the sentence or qualify it as an unsupported assumption without citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Reference [12] presents the CHSH inequality\n$$|E(a,b) - E(a,b')| + |E(a',b) + E(a',b')| \\le 2,$$",
      "reason": "The bibliography entry for [12] does not include this inequality; the claim lacks source support, violating citation integrity.",
      "fix": "Remove the reference to [12] and the inequality, or replace with a supported statement."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "c=1 – treated as an assumption. ... (unit 1 keV from XRISM and Lynx)",
      "reason": "Neither [6] nor [8] explicitly state a numeric value of 1 that can be interpreted as a cost; the claim is not directly supported by the cited excerpts, violating citation integrity.",
      "fix": "Reframe $c$ as an assumed unit without citing [6] or [8], or provide a different source that explicitly gives a numeric value."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "each additional $0.1$ increase in $b$ yields a $5\\%$ rise in $x$ (extrapolated from the linear relation $\\pi_F-\\pi_P$), a $b$ increase of $0.33$ could potentially raise the falsifiable‑practice share from $10\\%$ to $25\\%$.",
      "reason": "These quantitative projections are not labeled as projections with explicit assumptions, violating quantitative honesty requirements.",
      "fix": "Label the statements as projections and clearly state the underlying assumptions, or remove them if unsupported."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "## 6. Extended Derivations and Worked Examples",
      "reason": "The required Section 6 should be the Discussion; the paper mislabels this section, causing a missing required Discussion section and breaking the mandated structure.",
      "fix": "Rename this section to \"## 6. Discussion\" and move the extended derivations to a new subsection or separate section."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "## 7. Discussion",
      "reason": "Because Section 6 is misnamed, the actual Discussion appears as Section 7, resulting in the absence of a correctly numbered Discussion section as required.",
      "fix": "Adjust the section numbering so that the Discussion content is under \"## 6. Discussion\" and renumber subsequent sections accordingly."
    }
  ],
  "soft": []
}