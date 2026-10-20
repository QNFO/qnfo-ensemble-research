{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "I_{\\text{anh}} = -L_{2}\\log_{2}L_{2}-(1-L_{2})\\log_{2}(1-L_{2}) \\approx -0.02\\log_{2}0.02-0.98\\log_{2}0.98 \\approx 0.112\\ \\text{bits}.",
      "reason": "The mutual‑information calculation omits the second term; the correct value is ≈0.141 bits.",
      "fix": "Re‑compute the expression including both terms and report the correct value ≈0.141 bits."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The projected cost to obtain a falsification test is **≈ $25{,}000 USD**.",
      "reason": "The cost figure is presented as a factual result without being labeled as a projection with stated assumptions.",
      "fix": "Label the statement as a projection and cite the assumption that the cost estimate is based on typical engineering rates."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Applying the GUP to a region of size $R$ yields a minimal energy quantum $\\epsilon(R)\\sim\\frac{1}{R}$ and modifies the Bekenstein bound, showing that entropy corrections become relevant at scales $2$–$3\\,L_{\\rm pl}$ [5, § 1].",
      "reason": "The cited work [5] does not contain the quoted statement in its provided excerpt; the claim is unsupported.",
      "fix": "Remove or replace the statement with a claim that is directly supported by the excerpt of [5], or drop the citation."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The theorem of [10] asserts that the existence of a factorised deformation function $\\tilde\\delta(\\Delta x,\\Delta p,\\epsilon)$ implies that one uncertainty can be uniquely determined from the other...",
      "reason": "No excerpt from [10] is provided; the claim cannot be verified against the bibliography.",
      "fix": "Delete the sentence or replace it with a statement supported by an available excerpt."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The GUP commutator derived in [11] reads $[\\hat X,\\hat P]=i\\hbar\\Bigl(1+\\beta\\,\\frac{\\hat P^{2}}{m_{p}^{2}c^{2}}\\Bigr)$...",
      "reason": "The excerpt for [11] does not contain this formula; the citation is unsupported.",
      "fix": "Remove the sentence or replace it with a claim that is directly supported by the provided excerpt of [11] (if any)."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The adelic Shannon framework of [12] defines a channel capacity that factorises over all places $v$ of the rational numbers...",
      "reason": "No excerpt for [12] is supplied; the statement cannot be verified.",
      "fix": "Delete the sentence or re‑phrase it using only information that appears in the supplied excerpt."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "The hidden‑modulus LWE construction of [13] hides a secret prime modulus $p$ from the adversary...",
      "reason": "The bibliography entry for [13] is a QNFO work with no provided excerpt; the claim is unsupported.",
      "fix": "Remove the sentence or qualify it as a projection with explicit assumptions."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "As an illustrative physical leakage model, consider a weakly anharmonic oscillator whose leakage we estimate as $L_{2}=8\\Bigl(\\frac{\\Omega}{|\\alpha|}\\Bigr)^{2}\\sin^{2}\\!\\Bigl(\\frac{\\alpha T_{g}}{2}\\Bigr)$.",
      "reason": "The formula is taken from [14] which has no excerpt; the citation is unsupported.",
      "fix": "Either provide a derivation of the formula within the paper without citing [14], or remove the citation."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "Depth of literature treatment could be expanded.",
      "reason": "The background section touches many works but does not discuss their detailed results in depth.",
      "fix": "Add brief explanations of each cited work's specific quantitative contribution where possible."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Appendix A reports no divergences.",
      "reason": "While no divergent claims were found, a brief statement confirming the convergence process would improve transparency.",
      "fix": "Add a sentence confirming that all drafts converged on the same claims."
    }
  ]
}