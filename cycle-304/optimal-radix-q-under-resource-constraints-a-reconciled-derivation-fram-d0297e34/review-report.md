[
  {
    "id": "H1",
    "severity": "HARD",
    "claim": "The work demonstrates that implicit relational modeling hinders controllability, and that an explicit semantic graph prior improves synthesis.",
    "reason": "The bibliography entry for [3] provides only title and URL; no excerpt contains this claim, violating citation integrity.",
    "fix": "Remove or replace the sentence with a statement directly supported by the excerpt of [3], or omit the citation."
  },
  {
    "id": "H2",
    "severity": "HARD",
    "claim": "The authors argue that objective‑function quality is crucial for registration tasks and propose a loss that does not require perfectly aligned training data.",
    "reason": "The bibliography entry for [4] lacks any excerpt supporting this specific claim, violating citation integrity.",
    "fix": "Delete the sentence or replace it with a claim that can be directly sourced from the provided excerpt of [4]."
  },
  {
    "id": "H3",
    "severity": "HARD",
    "claim": "The study transfers Tacotron‑based synthesis techniques to piano‑MIDI generation, showing that techniques can be re‑targeted across structurally similar domains.",
    "reason": "No excerpt from the bibliography entry for [7] contains this information; the citation is unsupported.",
    "fix": "Remove the sentence or rewrite it using only information present in the excerpt for [7]."
  },
  {
    "id": "H4",
    "severity": "HARD",
    "claim": "The work models severe uncertainty in breakup events and motivates a “breakup map” that tracks how optimal design choices shift as uncertain parameters vary.",
    "reason": "The bibliography entry for [8] provides only title and URL; the claim is not found in any supplied excerpt, violating citation integrity.",
    "fix": "Delete the sentence or replace it with a verifiable statement from the excerpt of [8]."
  },
  {
    "id": "H5",
    "severity": "HARD",
    "claim": "The paper reports a structured‑transform cost $C_{\\mathrm{str}}=2888$ operations versus a dense baseline $6.561\\times10^{11}$, and a separation factor $\\approx2.27\\times10^{8}$.",
    "reason": "No excerpt from the bibliography entry for [10] contains these quantitative details; the citation is unsupported.",
    "fix": "Remove the quantitative statement or replace it with numbers that are present in the excerpt of [10]."
  },
  {
    "id": "H6",
    "severity": "HARD",
    "claim": "This predecessor states the problem, supplies $F_{1,1}(4)=4.2289$, the threshold $\\beta^{*}=2.286$, and an asymptotic continuous optimum $q\\approx3.65$.",
    "reason": "The bibliography entry for [9] does not include these specific values in its excerpt; the citation is unsupported.",
    "fix": "Delete the sentence or limit the citation to information actually present in the excerpt of [9]."
  },
  {
    "id": "H7",
    "severity": "HARD",
    "claim": "Thus:\n- $\\beta<2.303$: $q=4$ optimal.\n- $\\beta>2.303$: $q=3$ optimal.",
    "reason": "The derived threshold in Section 4.5 is $\\beta^{*}=2.286$; the text incorrectly uses $2.303$, creating a numerical inconsistency.",
    "fix": "Replace \"2.303\" with \"2.286\" in both bullet points."
  },
  {
    "id": "H8",
    "severity": "HARD",
    "claim": "Threshold traversal weight where $q=3$ overtakes $q=4$: $\\beta^{*}=2.303$.",
    "reason": "The correct computed threshold is $\\beta^{*}=2.286$; the value $2.303$ contradicts the arithmetic shown in Section 4.5.",
    "fix": "Change \"2.303\" to \"2.286\"."
  }
]