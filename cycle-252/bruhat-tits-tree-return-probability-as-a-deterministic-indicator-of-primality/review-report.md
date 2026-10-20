{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "These works establish that the tree admits a natural coordinate system and a well‑defined Laplacian operator. [3, § 1 Introduction]",
      "reason": "Citation [3] is used without any supporting excerpt from its full text; the bibliography does not provide a quoted passage that confirms this specific point, violating citation integrity.",
      "fix": "Remove the citation to [3] or replace it with a citation that has a supporting excerpt; if the statement is retained, rephrase to cite only works whose excerpts contain the asserted fact."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Spectral properties of $\\mathcal{T}_{p}$ have been studied in various contexts [4].",
      "reason": "Citation [4] is made without any excerpt from its text that substantiates the claim about spectral properties, violating citation integrity.",
      "fix": "Delete the citation to [4] or provide a specific excerpt from [4] that discusses spectral properties; otherwise rephrase the sentence to avoid uncited claims."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The same tree underlies the Cayley‑tree measures of Kolmogorov‑type extensions [5, § 2 Cylindric sets on Cayley trees].",
      "reason": "Citation [5] lacks a supporting excerpt that mentions Cayley‑tree measures or Kolmogorov‑type extensions, violating citation integrity.",
      "fix": "Remove the citation to [5] or replace it with a work that has an excerpt confirming this point; adjust the sentence accordingly."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "and the geodesic bulk diagram calculations of $p$‑adic conformal blocks [6, § I Introduction].",
      "reason": "Citation [6] is used without an excerpt that verifies the claim about geodesic bulk diagram calculations, violating citation integrity.",
      "fix": "Delete or replace the citation to [6] with a source that provides the needed excerpt; modify the sentence to reflect only supported references."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Effective field‑theory calculations on subspaces of $\\mathcal{T}_{p}$ further confirm that the tree’s geometry determines the spectrum of the discrete Laplacian [7, § 2 The Action on $\\mathcal{T}_{p}$].",
      "reason": "Citation [7] lacks an excerpt confirming the stated result about effective field‑theory calculations, violating citation integrity.",
      "fix": "Remove the citation to [7] or supply a supporting excerpt; otherwise rephrase to avoid uncited assertions."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The QNFO study of spectral dynamics on $\\mathcal{T}_{p}$ reports a discrete eigenvalue distribution with mean $\\mu\\approx1.984$ and a collapsed spectral gap for composite structures [9, § 4.7 Summary of Spectral Findings].",
      "reason": "Citation [9] is made without an excerpt that contains the numeric mean $\\mu\\approx1.984$, violating citation integrity.",
      "fix": "Delete the numeric claim or replace it with a statement supported by an available excerpt; if retained, add a proper citation with the required excerpt."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Finally, the QNFO dynamic findings identify a resonance time $t_{\\mathrm{res}}\\approx1.03$ and a maximal localisation probability $P_{\\max}\\approx0.20$ for quantum walks on prime‑induced trees [9, § 5.7 Summary of Dynamic Findings].",
      "reason": "Citation [9] lacks an excerpt that provides the resonance time and localisation probability values, violating citation integrity.",
      "fix": "Remove these quantitative values or replace them with numbers that are supported by an excerpt; otherwise provide the missing excerpt."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "The QNFO study reports that “the prime 2 is structurally minimal via its 3‑regular Bruhat–Tits tree.” [10]",
      "reason": "Citation [10] is used without an excerpt confirming this statement; citation integrity is violated.",
      "fix": "Delete the citation to [10] or supply an excerpt that contains the quoted phrase; adjust the sentence accordingly."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Assuming $O(\\log N)$ arithmetic operations per test and a truncation depth $D=6$, the CPU time on a modern processor is estimated at $<10^{-5}$ s per integer, with memory usage $<1$ MiB.",
      "reason": "This quantitative performance estimate is not derived in the paper nor labeled as a projection with explicit assumptions, violating quantitative honesty.",
      "fix": "Label the statement as a projection and explicitly state the assumptions (e.g., operation count, processor speed) or remove the claim if no supporting derivation is provided."
    }
  ],
  "soft": []
}