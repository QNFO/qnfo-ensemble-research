[
  {
    "id": "H1",
    "severity": "HARD",
    "claim": "Synthetic dimensions are provided by frequency and orbital‑angular‑momentum (OAM) modes, yielding a second Chern number $C_{2}=1$ and a topological mass gap $\\Delta\\approx14.5\\;\\text{meV}$.",
    "reason": "The paper presents $\\Delta\\approx14.5\\;\\text{meV}$ as a derived result, but Section 3 shows the actual derived gap is $5.2\\times10^{-5}\\;\\text{meV}$; the 14.5 meV value is an assumed target and is not labeled as a projection.",
    "fix": "Rephrase to indicate the value is an assumed target, e.g., \"... yielding a second Chern number $C_{2}=1$ and we assume a target topological mass gap $\\Delta\\approx14.5\\;\\text{meV}$ for the subsequent analysis.\""
  },
  {
    "id": "H2",
    "severity": "HARD",
    "claim": "1. **Topological gap**: $\\Delta = 14.5\\;\\text{meV}$ (derived from the Floquet commutator term).",
    "reason": "This statement contradicts the explicit derivation in Section 3, where the commutator term yields $\\Delta \\approx 5.2\\times10^{-5}\\;\\text{meV}$. The 14.5 meV value is not derived and should be presented as an assumed design parameter.",
    "fix": "Replace with \"1. **Topological gap**: $\\Delta = 14.5\\;\\text{meV}$ (assumed target gap for the quantitative analysis).\""
  },
  {
    "id": "H3",
    "severity": "HARD",
    "claim": "Byzantine fault tolerance in cloud clusters highlights the importance of checkpointing and rapid fault detection for mission‑critical applications such as air‑traffic control [5].",
    "reason": "The excerpt of reference [5] does not mention air‑traffic control; the claim is unsupported by the supplied text.",
    "fix": "Remove the unsupported phrase \"as such as air‑traffic control\" or replace the sentence with a claim directly supported by the excerpt, e.g., \"Byzantine fault tolerance in cloud clusters highlights the importance of checkpointing and rapid fault detection for mission‑critical applications [5].\""
  },
  {
    "id": "H4",
    "severity": "HARD",
    "claim": "Assuming a foundry cost of $5 k per 1 cm² photonic chip, plus $2 k for THz drive electronics and $1 k for cryogenic packaging, the total prototype cost is projected at **≈ $8 k**.",
    "reason": "The cost estimate is a projection based on assumptions but is not labeled as such, violating the requirement that projections be explicitly identified.",
    "fix": "Add a projection label, e.g., \"(projection, based on the stated assumptions) the total prototype cost is estimated at ≈ $8 k.\""
  },
  {
    "id": "H5",
    "severity": "HARD",
    "claim": "using $\\hbar=4.135668\\;\\text{meV·ps}$",
    "reason": "The value given for $\\hbar$ is incorrect (it is the Planck constant $h$); the correct reduced Planck constant is $\\hbar\\approx0.658212\\;\\text{meV·ps}$. This error propagates to the drive‑frequency bound.",
    "fix": "Replace the value with the correct one: \"using $\\hbar=0.658212\\;\\text{meV·ps}$\"."
  },
  {
    "id": "H6",
    "severity": "HARD",
    "claim": "$\\nu_{\\min}=7.01\\;\\text{THz}$",
    "reason": "This minimum drive frequency is computed using the incorrect $\\hbar$ value, resulting in an underestimate; with the correct $\\hbar$ the bound is $\\nu_{\\min}\\approx66.9\\;\\text{THz}$.",
    "fix": "Re‑compute using the correct $\\hbar$: \"$\\nu_{\\min}=\\frac{2\\Delta}{\\hbar}=\\frac{2\\times14.5\\;\\text{meV}}{0.658212\\;\\text{meV·ps}}\\approx66.9\\;\\text{THz}$\"."
  }
]