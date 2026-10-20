{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Typical magnitude within the experimentally reported bound $|V|\\le 75\\ \\mathrm{cm^{-1}}$ [4]",
      "reason": "Citation [4] is used to support a numeric bound on V, but the provided excerpt for [4] contains no quantitative statement about a bound on V.",
      "fix": "Remove the citation or replace it with a statement that the bound is an assumption."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Energetic disorder typical for FMO dimers [2]",
      "reason": "Citation [2] does not provide a specific numeric value for the energetic disorder Δ; the excerpt only discusses mechanisms, not a numeric disorder.",
      "fix": "Remove the citation or qualify the statement as an assumption without citation."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Trap rate used in atomistic energy‑funnelling studies [5]",
      "reason": "Citation [5] excerpt does not contain a specific trap rate value; the claim is unsupported by the supplied text.",
      "fix": "Remove the citation and state the trap rate as an assumed parameter."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Exciton lifetime reported for green‑sulfur‑bacteria complexes [5]",
      "reason": "Citation [5] excerpt does not provide the exciton lifetime value of 1 ns; the claim lacks source support.",
      "fix": "Remove the citation and label the lifetime as an assumption."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The boson‑mediated non‑Markovian framework is defined as a model that retains bath memory and can achieve high efficiencies [9]",
      "reason": "Citation [9] excerpt consists only of the title; no definition or claim about memory retention or high efficiencies is present in the supplied text.",
      "fix": "Remove the citation or rephrase the sentence without attributing the definition to [9]."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Mixed quantum–classical simulations further demonstrate that treating high‑frequency chromophore vibrations quantum‑mechanically can slow transfer rates by up to a factor of two [6]",
      "reason": "Citation [6] excerpt states that nuclear quantum effects slow down energy transfer but does not quantify the slowdown as a factor of two.",
      "fix": "Remove the quantitative factor or replace it with a qualitative statement without the unsupported numeric factor."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Recent ultrafast spectroscopy reports sub‑100 fs energy relaxation in single light‑harvesting complexes [7]",
      "reason": "Citation [7] excerpt only gives the title; it does not contain the specific sub‑100 fs timescale.",
      "fix": "Remove the specific timescale or qualify it as an assumption without citation."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "The thresholds for $R$ are conventions; alternative choices would shift the transitional window but not the robust conclusion that slow vibrational modes demand a non‑Markovian treatment.",
      "reason": "The statement about thresholds being conventions is not supported by any cited work; it is an uncited claim about methodology.",
      "fix": "Rephrase to indicate that the thresholds are defined in this work without attributing them to external sources."
    }
  ],
  "soft": []
}