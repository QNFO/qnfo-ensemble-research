{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The three independent drafts presented conflicting conclusions regarding the Majorana nature of the Wheeler–DeWitt zero‑mode. Draft A argued that the hidden $U(1,1)$ symmetry implements a particle‑hole‑like involution, computes a finite‑volume scale $F L\\approx36.6$, and concludes that the WDW zero‑mode can be interpreted as a Majorana‑type topological zero mode. Draft B performed a structural test and concluded that the WDW zero‑mode **fails** all three defining criteria of a Majorana zero mode (particle–hole symmetry, non‑zero index, spectral isolation). Draft C (not provided) did not introduce additional divergent claims.",
      "reason": "The paper includes meta‑commentary about the drafting process, which is prohibited by the style rules.",
      "fix": "Remove the discussion of drafts and replace Appendix A with a neutral summary of any genuine scientific divergences, without referencing draft identities."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Ref. [3] studies the complexified Virasoro zero‑mode flow and the logarithmic graviton at the chiral point of topologically massive gravity. Its subject is a symmetry construction built around zero‑mode generators, which makes it a relevant reference point for our question of whether a zero mode can carry a symmetry structure analogous to particle–hole conjugation.",
      "reason": "The citation is not tied to a specific statement present in the supplied excerpt of [3]; the paper cites the work only for its existence and general topic, violating citation integrity.",
      "fix": "Delete or replace the sentence with a citation to a work whose excerpt directly supports the claim, or rephrase to omit the unsupported citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Ref. [4] analyses the Virasoro zero‑mode flow in critical topologically massive gravity, treating logarithmic correlators and the grading of the partition function. Like Ref. [3], it develops a symmetry algebra organised by zero‑mode generators, and we use it only as evidence that zero‑mode structures can be organised into algebraic flows, not as a source for any particle–hole analogy.",
      "reason": "The citation lacks a supporting excerpt; the paper cites the work without a specific point derived from its full text.",
      "fix": "Remove the citation or replace it with a supported reference; ensure any remaining statement is backed by an excerpt."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Ref. [5] examines the role of zero‑mode contributions in the matching for the twist‑3 parton distribution functions $e(x)$ and $h_{L}(x)$. Its subject shows that zero modes enter quantitative matching relations in an entirely different field, which motivates testing zero‑mode claims by structural criteria rather than by the shared label alone.",
      "reason": "No excerpt from [5] is provided that substantiates this claim; the citation is used only to note a general relevance, violating the rule that citations must refer to specific points in the source text.",
      "fix": "Delete or replace the sentence with a citation that has a supporting excerpt, or rephrase to omit the unsupported reference."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Ref. [6] studies Majorana zero mode–soliton duality and in‑gap and bound‑state‑in‑continuum bound states in a modified Toda model coupled to a fermion. Its title indicates a setting in which Majorana zero modes are tied to solitonic configurations, and we take from it the requirement that a claimed Majorana zero mode be tied to a specific topological or solitonic structure, a requirement the Wheeler–DeWitt kernel is tested against in Section 4.",
      "reason": "The citation is not supported by any excerpt from [6]; the paper cites it only for a general claim, which is prohibited.",
      "fix": "Remove the citation or replace it with a supported statement; ensure any claim about [6] is directly backed by its excerpt."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Ref. [7] reports an emergent vortex Majorana zero mode in iron‑based superconductors. We adopt it as the condensed‑matter reference system whose zero modes exhibit the three hallmarks we test for — self‑conjugation under particle–hole conjugation, a non‑trivial topological index, and exponential splitting $\\Delta E\\sim e^{-L/\\xi}$ — while noting that the detailed statement of these hallmarks is our own operationalisation, stated explicitly in Section 3.",
      "reason": "No excerpt from [7] is provided that confirms these specific hallmarks; the citation is used without a supporting textual basis.",
      "fix": "Delete or replace the sentence with a citation that includes a supporting excerpt, or rephrase to avoid the unsupported reference."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Ref. [8] advances the hypothesis that a vanishing Zitterbewegung (ZBW) signal can serve as a unified framework for distinguishing topological fermion classes, including a ZBW–Majorana correspondence. We cite it as an example of proposed zero‑mode‑linked observables; since the hypothesis concerns fermionic signals rather than gravitational constraint operators, it plays no role in the derivations of Section 4.",
      "reason": "The paper cites [8] without any excerpt that substantiates the described hypothesis; this violates the rule that citations must be tied to specific points in the source text.",
      "fix": "Remove the citation or replace it with a statement supported by an excerpt; ensure any remaining mention of [8] is directly backed by its text."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Collectively, these works establish that (i) constrained zero modes can alter spectral properties, (ii) zero modes may appear in symmetry algebras, (iii) topological protection is tied to non‑trivial indices and exponential splitting, (iv) zero‑mode signatures can serve as topological markers.",
      "reason": "The synthesis attributes multiple specific conclusions to the cited works, but the required supporting excerpts for many of these points are missing, making the statement unsupported.",
      "fix": "Rewrite the paragraph to only include points that are directly supported by the available excerpts, or remove unsupported assertions."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The literature review in Section 2 treats a broad range of topics but does not deeply engage with the technical details of each cited work.",
      "reason": "The treatment is relatively superficial and could be expanded for greater depth.",
      "fix": "Add more detailed discussion of each work's methodology and results, using the provided excerpts."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "The paper does not explicitly list all assumptions underlying the Fredholm index regularisation.",
      "reason": "Clarifying these assumptions would improve transparency.",
      "fix": "Include a brief enumeration of the regularisation assumptions in Section 4.2."
    }
  ]
}