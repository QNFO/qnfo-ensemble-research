{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The vertex‑count expression $V_d=1+(p+1)\\frac{p^{d}-1}{p-1}$ reported in [12] ...",
      "reason": "The cited work [12] (QNFO: Time as Epistemic Emergence ...) does not contain the quoted vertex‑count formula in its supplied excerpt; the claim is unsupported.",
      "fix": "Remove the citation to [12] or replace it with a citation to a work whose excerpt actually includes the vertex‑count formula, e.g., derive the formula directly without external citation."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Ramanujan graphs attain the optimal bound $\\lambda_1\\le 2\\sqrt{p}$. Translating (3) to the combinatorial Laplacian $\\Delta=(p+1)I-A$ gives the prime lower bound ... proved in [3].",
      "reason": "The excerpt for [3] (Novel performant primality test on a Pell's cubic) does not provide a proof of the Ramanujan bound; the citation is unsupported.",
      "fix": "Delete the citation to [3] for the Ramanujan bound and either provide a self‑contained derivation or cite a work whose excerpt actually contains the bound."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "When $N$ is composite, the automorphism $\\gamma_N$ introduces non‑trivial cycles ... the spectral gap satisfies $\\Gamma_k \\le \\frac{C}{|V_k|}$ ... from [7, §4].",
      "reason": "The excerpt for [7] (On the asymptotic behavior of the spectral gap for discrete Schrödinger operators) is not provided; the specific inequality is not verifiable from the supplied text.",
      "fix": "Remove the citation to [7] and either derive the inequality directly or replace it with a citation to a work whose excerpt includes the stated bound."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The exponential map $\\exp_p(x)=\\sum_{n=0}^{\\infty}\\frac{x^n}{n!}$ ... introduced in the BTZ construction [6] ...",
      "reason": "The excerpt for [6] does not contain the definition or properties of the $p$‑adic exponential function; the citation is unsupported.",
      "fix": "Delete the citation to [6] and either provide the definition without citation or cite a source that actually includes the exponential series."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The QNFO “Spectral Dynamics on Bruhat‑Tits Trees” manuscript reports a multi‑base triangulation experiment ... coefficients $\\alpha\\approx0.40$, $\\beta\\approx0.30$, $\\gamma\\approx0.20$ ... [9].",
      "reason": "The excerpt for [9] does not contain any description of such an experiment or the numerical coefficients; the citation is unsupported.",
      "fix": "Remove the citation to [9] and the associated numerical claim, or replace it with a statement that does not rely on unsupported data."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Perfect‑tensor networks built on the Bruhat‑Tits tree realize holographic quantum error‑correcting codes ... [10].",
      "reason": "The excerpt for [10] does not provide the claimed connection between tensor networks and Laplacian spectra; the citation is unsupported.",
      "fix": "Delete the citation to [10] and the related claim, or replace it with a properly supported statement."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Assuming the smallest non‑zero eigenvalue equals $\\lambda_1 = 0.1721$, which satisfies $\\lambda_1\\ge0.1716$ as required by the universal prime bound (Section 4.2), the test would declare $101$ prime.",
      "reason": "The value $0.1721$ is introduced without derivation or labeling as an assumption/projection; it is a quantitative claim not derived in the paper.",
      "fix": "Label the value as an assumption (e.g., \"We assume $\\lambda_1=0.1721$ for illustration\") or provide a derivation; otherwise remove the specific numeric claim."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Using the exponential mixing result of [1] (decay rate $\\exp(-\\kappa D)$) and the branch description of [2], one obtains $\\lambda_1 \\le \\frac{C}{D}$ ...",
      "reason": "No arithmetic steps are shown to derive the bound $\\lambda_1 \\le C/D$; the claim is quantitative but not derived nor labeled as a projection.",
      "fix": "Provide the missing arithmetic derivation step‑by‑step, or label the bound as a projection based on the cited results."
    }
  ],
  "soft": []
}