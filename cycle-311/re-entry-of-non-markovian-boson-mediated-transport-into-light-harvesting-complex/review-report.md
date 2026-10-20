{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Memory‑ratio spans $[0.26,0.96]$ for fast baths ($\\tau_{B}=0.1\\ \\mathrm{ps}$) and $[2.6,9.6]$ for slow baths ($\\tau_{B}=1\\ \\mathrm{ps}$)",
      "reason": "The abstract gives memory‑ratio ranges that differ from the derived values in Section 4.2 (fast $[0.428,0.589]$, slow $[4.28,5.89]$). The abstract numbers are not derived nor labeled as a projection.",
      "fix": "Replace the abstract ranges with the values derived in Section 4.2 (fast $[0.428,0.589]$, slow $[4.28,5.89]$) or label them as a projection with explicit assumptions."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Transient thermal‑grating (TTG) experiments provide a powerful means of probing material properties and heat‑transport dynamics at small spatiotemporal scales, establishing that sub‑picosecond bath dynamics are experimentally accessible.",
      "reason": "The excerpt for [1] mentions probing at small spatiotemporal scales but does not state that sub‑picosecond bath dynamics are experimentally accessible; the claim extends beyond the supplied text.",
      "fix": "Restrict the statement to what the excerpt supports, e.g., \"TTG experiments provide a powerful means of probing material properties and heat‑transport dynamics at small spatiotemporal scales\"."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Multiplex‑network analysis in [3] shows that layered transport metrics can exhibit sharp transitions; our memory‑ratio plays an analogous role for exciton‑phonon layers.",
      "reason": "The excerpt for [3] describes multiplex networks for urban transport and does not mention sharp transitions or layered transport metrics; the claim is unsupported by the cited work.",
      "fix": "Remove the unsupported claim about sharp transitions or replace it with a statement directly supported by the excerpt, such as describing multiplex networks as a mathematical framework."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The non‑Markovian boson‑mediated framework can achieve efficiencies above $95\\%$ [9].",
      "reason": "The excerpt for [9] states that the framework can achieve high efficiencies but does not specify a quantitative threshold of $95\\%$; the claim overstates the source.",
      "fix": "Modify the claim to reflect the source, e.g., \"can achieve high efficiencies\" without specifying $95\\%$."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The multiplex‑network perspective on transport provides an analogy for exciton‑phonon layered dynamics and motivates our memory‑ratio criterion.",
      "reason": "The excerpt for [3] discusses multiplex networks in the context of urban transportation and does not draw an analogy to exciton‑phonon dynamics; the claim is not derivable from the source.",
      "fix": "Remove the analogy or replace it with a statement directly supported by the excerpt, such as noting that multiplex networks are a mathematical framework for layered systems."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Computational load assumes that a realistic FMO simulation using the non‑Markovian framework requires on the order of $10^{4}$ CPU‑hours (uncertainty factor $\\approx 2$).",
      "reason": "The paper provides no source or derivation for the $10^{4}$ CPU‑hour estimate; it is presented as an assumption without labeling it as a projection with stated assumptions.",
      "fix": "Label the estimate as a projection with the explicit assumption \"We assume a realistic FMO simulation requires $10^{4}$ CPU‑hours\" or remove the specific number."
    }
  ],
  "soft": []
}