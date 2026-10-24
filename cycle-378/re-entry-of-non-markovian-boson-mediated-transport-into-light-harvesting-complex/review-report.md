{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "References list entries are placeholders \"Full citation needed.\" instead of actual bibliography entries.",
      "reason": "Citation integrity requires that every reference in the References section matches a bibliography entry with exact title and identifier. Placeholders do not satisfy this.",
      "fix": "Replace each placeholder with the full citation from the provided bibliography, preserving the exact numbering and formatting."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The paper claims that transient‑thermal‑grating studies emphasize the necessity of dimensional consistency when relating wavenumber‑based couplings to temporal rates [1].",
      "reason": "The excerpt for [1] discusses the need for forward models connecting energy deposition, heat transport, and detection, but does not explicitly mention dimensional consistency of transfer‑time expressions.",
      "fix": "Either remove or rephrase the claim to reflect only what the excerpt states, or replace it with a supported statement about TTG requiring consistent forward modeling."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The paper cites a prior applicability analysis [9] that employed broader parameter ranges and a dimensionally inconsistent transfer‑time formula.",
      "reason": "No excerpt from the bibliography entry [9] is provided, so the claim cannot be verified against the source text.",
      "fix": "Remove the citation to [9] or replace it with a statement that does not rely on unsupported details, ensuring any remaining citation is supported by the provided excerpt."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The discussion briefly mentions vibronic effects and references [11] without detailed explanation.",
      "reason": "The paper could benefit from a more thorough explanation of how vibronic coupling might affect the presented analysis.",
      "fix": "Add a concise explanation of the potential impact of vibronic modes on transfer times and memory ratios, citing the specific point from [11] that supports it."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "The paper states thresholds for the memory ratio R are chosen for falsifiability but does not justify the specific numeric values.",
      "reason": "Providing a brief rationale for the chosen thresholds would strengthen the argument.",
      "fix": "Include a short justification (e.g., based on typical error margins in similar studies) for the R thresholds."
    }
  ]
}