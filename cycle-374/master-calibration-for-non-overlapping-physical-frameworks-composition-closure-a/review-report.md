{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The European Particle Physics Strategy Update reports that future $e^{+}e^{-}$ colliders will measure oblique parameters with $\\sim1\\%$ precision, about a factor ten better than current precision, and that $10^{12}$ $Z$ bosons would be available at circular colliders [1].\nThe next linear collider report specifies a centre‑of‑mass energy window of $500\\ \\mathrm{GeV}$ to $1\\ \\mathrm{TeV}$ in its abstract and $0.5$–$1.5\\ \\mathrm{TeV}$ in its preface, providing the numerical factors used in Derivation 6 [2].\nRoad‑marking mediated calibration enables targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap, reporting positional accuracy $\\approx0.02\\ \\mathrm{m}$ and angular accuracy $\\approx0.086^{\\circ}$ without manual operation; the work also flags a fragile auxiliary assumption (locally accurate odometry) that becomes structural when the auxiliary capability fails [3].\nMHD analysis of CFETR and HFRC shows that for CFETR active control methods may be required for resistive‑wall‑mode stabilization in $80\\%$ of steady‑state‑operation scenarios, highlighting a domain‑specific calibration challenge [4].\n*   *   *   *   *   *   *   *",
      "reason": "Section 2 discusses only four bibliography works and then contains placeholder bullet points. The required background must discuss at least eight works with specific points drawn from their supplied excerpts; placeholders and missing citations violate the literature‑review requirement.",
      "fix": "Expand Section 2 to include specific, citation‑backed statements for at least four additional works ([5]–[8] or others), removing the placeholder bullet lines. Each added sentence must cite a concrete point that appears in the provided excerpt for that work."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "A systematic inventory of such fractures enumerates 29 distinct unresolved bifurcations, spanning topics from the nature of the continuum to the status of the observer, and argues that they are interconnected rather than isolated puzzles [10].",
      "reason": "The bibliography excerpt for [10] does not contain the specific claim that there are exactly 29 unresolved bifurcations; citing this number without supporting text violates citation integrity.",
      "fix": "Either provide a citation to a source whose excerpt includes the exact number 29, or qualify the statement as an assumption (e.g., \"We assume N_{schism}=29 based on the synthesis in [10]\") and note that the number is not directly supported by the supplied excerpt."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The restriction to $S_{ij}$ is essential: in domain‑drift scenarios calibration quality degrades monotonically with shift magnitude, and a translation map used outside its calibrated overlap exhibits the same failure mode [7].",
      "reason": "The excerpt for [7] (Post‑hoc Uncertainty Calibration for Domain Drift Scenarios) does not contain the quoted statement about the essential nature of restricting to $S_{ij}$; the citation therefore lacks grounding.",
      "fix": "Replace the unsupported claim with a statement that is directly supported by the excerpt of [7], or re‑cite a work whose excerpt includes the needed point. If no such source exists, rephrase as an assumption and remove the citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The version history above documents the iterative refinement of the manuscript, highlighting the incorporation of new literature, the correction of derivations, and the consolidation of convergent claims across drafts.",
      "reason": "This sentence is meta‑commentary about the drafting process, which is prohibited by the prose‑gate rule.",
      "fix": "Delete the sentence entirely or move it to an appendix that is explicitly labeled as a draft history, ensuring it does not appear in the main body of the paper."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "*   *   *   *   *   *   *   *",
      "reason": "Placeholder bullet points constitute unfinished content and violate the requirement that the paper contain no placeholder text.",
      "fix": "Remove the placeholder line and replace it with substantive, citation‑backed discussion of additional bibliography works as required by Section 2."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The paper provides a high‑level discussion of limitations but does not present a concise bullet‑list of all assumptions underlying the main results.",
      "reason": "Explicitly enumerating each assumption would improve clarity and aid reproducibility.",
      "fix": "Add a brief bullet‑list of limitations in Section 6, naming each assumption (e.g., independence of constraints, uniform error floor, first‑order composition model)."
    }
  ]
}