[
  {
    "id": "H1",
    "severity": "HARD",
    "claim": "The former approach can require on the order of $10^{4}$ CPU‑hours for a seven‑site FMO simulation, while the latter can be executed on a laptop in minutes.",
    "reason": "Quantitative claim not derived with shown arithmetic and not labeled as a projection with stated assumptions.",
    "fix": "Label the statement as an assumption or projection, e.g., \"Based on typical reported costs, the former approach can require on the order of $10^{4}$ CPU‑hours for a seven‑site FMO simulation (assumption), while the latter can be executed on a laptop in minutes (assumption).\""
  },
  {
    "id": "H2",
    "severity": "HARD",
    "claim": "The vibronic dimer study [4] reports excitonic couplings between $-50$ and $-75\;\mathrm{cm^{-1}}$ and site‑energy differences between $110$ and $180\;\mathrm{cm^{-1}}$ for the BChl 3–4 pair, providing the experimentally grounded parameter box used throughout this work.",
    "reason": "The bibliography excerpt for [4] is not provided; the claim cannot be verified from the supplied source.",
    "fix": "Replace the claim with a statement that the parameter ranges are assumed for this analysis, e.g., \"We assume excitonic couplings $V\\in[50,75]\\;\\mathrm{cm^{-1}}$ and site‑energy differences $\\Delta\\in[110,180]\\;\\mathrm{cm^{-1}}$, consistent with typical values reported for the BChl 3–4 dimer.\""
  },
  {
    "id": "H3",
    "severity": "HARD",
    "claim": "Single‑molecule pump–probe measurements resolve energy relaxation on sub‑100 fs scales, justifying the assignment of fast solvent‑like bath correlation times $\\tau_{B}=0.1\\;\\mathrm{ps}$ [7].",
    "reason": "The excerpt for [7] does not contain this information; the claim is unsupported by the supplied source.",
    "fix": "Rephrase to indicate it is an assumption, e.g., \"We assume a fast solvent‑like bath correlation time $\\tau_{B}=0.1\\;\\mathrm{ps}$, motivated by typical sub‑100 fs relaxation observed in ultrafast spectroscopy studies.\""
  },
  {
    "id": "H4",
    "severity": "HARD",
    "claim": "Mixed quantum–classical simulations [6] find that treating high‑frequency chromophore vibrations quantum‑mechanically slows transfer rates by less than a factor of two for biologically relevant parameters, supporting the weak‑coupling assumption in the Haken–Strobl rate formula.",
    "reason": "The excerpt for [6] is not provided; the claim cannot be verified.",
    "fix": "Remove the specific quantitative statement or replace it with a generic assumption, e.g., \"We assume the weak‑coupling regime is appropriate for the parameters considered, as suggested by prior mixed quantum–classical studies.\""
  },
  {
    "id": "H5",
    "severity": "HARD",
    "claim": "Transient thermal‑grating experiments highlight the need for dimensionally consistent expressions when converting wavenumber‑based couplings to temporal rates, reinforcing the correction of the transfer‑time formula.",
    "reason": "The excerpt for [1] does not contain this claim; it is unsupported.",
    "fix": "Replace with a statement that dimensional consistency is a general modeling requirement, e.g., \"Ensuring dimensional consistency when converting wavenumber‑based couplings to temporal rates is essential for accurate modeling.\""
  },
  {
    "id": "H6",
    "severity": "HARD",
    "claim": "Values $V\\in[50,75]\\;\\mathrm{cm^{-1}}$ and $\\Delta\\in[110,180]\\;\\mathrm{cm^{-1}}$ are reported in [4].",
    "reason": "No supporting excerpt for [4] is provided; the source claim cannot be verified.",
    "fix": "Treat these ranges as assumptions, e.g., \"We assume $V\\in[50,75]\\;\\mathrm{cm^{-1}}$ and $\\Delta\\in[110,180]\\;\\mathrm{cm^{-1}}$ based on typical reported values for the BChl 3–4 dimer.\""
  },
  {
    "id": "H7",
    "severity": "HARD",
    "claim": "Order‑of‑magnitude cost projection (projection). Assuming a cloud HPC price of $\\$0.10$ per CPU‑hour, the minimal full‑scale simulation costs \\[\\text{Cost}\\approx10^{4}\\ \\text{CPU‑h}\\times\\$0.10/\\text{CPU‑h}= \\$1{,}000\\], with an uncertainty factor of two due to possible variations in parallel efficiency.",
    "reason": "The cost calculation relies on the unsupported $10^{4}$ CPU‑hour figure; without a validated assumption, the quantitative projection is not properly grounded.",
    "fix": "Either provide a clear assumption for the CPU‑hour estimate (e.g., \"Based on typical reported simulation costs, we assume $10^{4}$ CPU‑hours\") or remove the cost projection."
  },
  {
    "id": "H8",
    "severity": "HARD",
    "claim": "Transient thermal‑grating experiments highlight the need for dimensionally consistent expressions when converting wavenumber‑based couplings to temporal rates, reinforcing the correction of the transfer‑time formula.",
    "reason": "Duplicate of H5; ensure removal of redundant unsupported claim.",
    "fix": "Delete the duplicate sentence."
  }
]