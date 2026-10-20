{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "We assume bath correlation times $\\tau_{B}$ lie in the $0.1\\!-\!1\\ \\mathrm{ps}$ range.",
      "reason": "Citation [1] does not provide any quantitative statement about bath correlation times; the excerpt only describes TTG experiments generally.",
      "fix": "Remove the specific numerical range or replace it with a statement that the range is an assumption without citation."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "$\\kappa$ = $1\\ \\mathrm{ps^{-1}}$ | Trap rate used in efficiency estimates [5]",
      "reason": "The excerpt for reference [5] is not provided, so the paper cannot substantiate that the trap rate $\\kappa=1\\ \\mathrm{ps^{-1}}$ comes from that work.",
      "fix": "Delete the citation to [5] for the trap rate and treat $\\kappa$ as an assumed parameter."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "$\\tau_{e}$ = $1\\ \\mathrm{ns}$ | Exciton lifetime cited in [5]",
      "reason": "The excerpt for reference [5] is not provided; the paper cannot verify that the exciton lifetime originates from that source.",
      "fix": "Remove the citation to [5] for $\\tau_{e}$ and keep the value as an assumption."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Ref. [6] quantifies that quantum‑mechanical treatment of high‑frequency vibrations can slow transfer rates by up to a factor of two, motivating the inclusion of a non‑Markovian correction in the slow‑bath regime.",
      "reason": "No excerpt for reference [6] is supplied; the claim cannot be verified from the bibliography.",
      "fix": "Delete the citation to [6] or replace the statement with a generic assumption without citation."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Ref. [7] reports sub‑100 fs energy‑relaxation processes observed with single‑molecule pump–probe techniques, confirming the existence of fast solvent‑like bath components ($\\tau_{B}\\approx0.1\\ \\mathrm{ps}$).",
      "reason": "The excerpt for reference [7] is not provided; the paper cannot substantiate the numerical relaxation time or the bath correlation estimate.",
      "fix": "Remove the citation to [7] and treat the fast bath component as an assumed value without citation."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Ref. [8] identifies key mechanisms—destructive‑interference suppression, static disorder, and dephasing‑broadened line overlap—by which dephasing noise enhances transport, providing a theoretical foundation for the dephasing‑based timescale analysis.",
      "reason": "No excerpt for reference [8] is supplied; the specific mechanisms cannot be verified from the bibliography.",
      "fix": "Delete the citation to [8] or rephrase the sentence to state the mechanisms without attributing them to a specific source."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Transient thermal‑grating probing. Transient thermal grating (TTG) experiments provide a powerful means of probing material properties and heat‑transport dynamics at sub‑picosecond relaxation times [1].",
      "reason": "The excerpt for [1] does not contain the phrase “sub‑picosecond relaxation times”; it only mentions probing at small spatiotemporal scales. The specific claim is not supported by the supplied text.",
      "fix": "Modify the sentence to reflect only what the excerpt states (e.g., TTG experiments probe material properties at small spatiotemporal scales) and remove the unsupported sub‑picosecond claim."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Atomistic energy‑funneling models. Ref. [5] presents an atomistic model of the green‑sulfur‑bacteria light‑harvesting complex and shows that sub‑picosecond energy‑funneling timescales are realistic for such systems, justifying the choice of $\\tau_{T}$ on the order of $0.5\\ \\mathrm{ps}$.",
      "reason": "No excerpt for reference [5] is provided; the claim about sub‑picosecond timescales cannot be verified.",
      "fix": "Remove the citation to [5] and keep the justification as an assumption or a generic statement."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Excitonic coupling magnitudes. We consider excitonic couplings $V$ in the range $20$–$75\\ \\mathrm{cm^{-1}}$ and energetic disorder $\\Delta$ in the range $100$–$180\\ \\mathrm{cm^{-1}}$ as representative experimental bounds.",
      "reason": "No citation is provided for these experimental bounds, and the bibliography does not contain an excerpt that supplies these numeric ranges.",
      "fix": "Add a citation to a source that actually provides these ranges, or rephrase the sentence to present the ranges as assumptions without citation."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "Transient thermal‑grating probing. Transient thermal grating (TTG) experiments provide a powerful means of probing material properties and heat‑transport dynamics at sub‑picosecond relaxation times [1]. We assume bath correlation times $\\tau_{B}$ lie in the $0.1\\!-\!1\\ \\mathrm{ps}$ range.",
      "reason": "The sentence combines a claim about TTG capabilities with an unsupported numerical assumption, both attributed to [1] without supporting excerpt.",
      "fix": "Split the sentence: keep the general TTG description (supported) and treat the $\\tau_{B}$ range as an uncited assumption."
    }
  ],
  "soft": []
}