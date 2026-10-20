{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Moment‑Based Ensemble Control frames the control of a large population—formally a continuum—of structurally identical dynamical systems with parametric variations as a pervasive task and identifies the severely under‑actuated nature of such systems and the inability to avail comprehensive state feedback as the central challenges [6]. Its full text develops ensemble systems as parameterized populations $\\frac{d}{dt}x(t,\\beta)=F(x(t,\\beta),\\beta,u(t))$ with a parameter‑independent input $u(t)$, and proves that the dynamic Hausdorff moment problem guarantees that ensemble systems and their moment systems share the same controllability properties, enabling moment‑feedback laws and model reduction from uncountably many systems to countably many agents [6].",
      "reason": "No excerpt for reference [6] is provided in the supplied bibliography, so the statement about its content cannot be derived from the allowed source material.",
      "fix": "Remove the citation and any unsupported description of the work, or replace with a statement that is directly supported by an available excerpt."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "TABED addresses speculative decoding for large vision‑language models, noting that speculative decoding “remains largely unexplored” for LVLMs and benchmarking existing inference methods with small draft models on eleven datasets [4]. Its experiments show scenario‑specific performance fluctuations with neither multimodal nor text‑only drafting consistently outperforming the other, while TABED itself achieves the best or second‑best performance across all scenarios with an average robust wall‑time speedup of $1.74\\times$ and over $5\\%$ improvement over single‑draft methods, training‑free and with negligible ensembling costs [4].",
      "reason": "No excerpt for reference [4] is provided; the claims about its experimental results are not supported by the allowed source material.",
      "fix": "Delete the citation and the specific performance numbers, or replace with a claim that can be supported by an available excerpt."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Master Functions and Equations for Perturbations of Vacuum Spherically‑Symmetric Spacetimes shows how spherical symmetry permits an expansion of perturbations in scalar, vector, and tensor harmonics, with the resulting perturbative equations decoupling for modes of different parity and harmonic number [5]. Its conclusions derive master functions satisfying wave‑type equations under three stated assumptions, producing two branches of solutions including a new even‑parity master function $\\Psi_{\\mathrm{EN}}$ independent of the Zerilli‑Moncrief one [5].",
      "reason": "Reference [5] has no supplied excerpt; the description of its content cannot be verified from the allowed sources.",
      "fix": "Remove the citation and the detailed description, or replace with a statement supported by an available excerpt."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Prescriptive Master Integrals of Maximal Weight at Two Loops constructs a spanning set of individually pure, planar master integrals involving massless particles in four dimensions which include all maximal‑weight contributions at two loops, such that every independent infrared‑divergent region is individually matched by specific masters, and all other masters are manifestly finite [7]. Its conclusion adds that this prescriptive basis lets coefficients be calculated directly from on‑shell functions [7].",
      "reason": "No excerpt for reference [7] is provided; the statements about its methodology and conclusions are unsupported.",
      "fix": "Delete the citation and the unsupported description, or replace with a claim that can be sourced from an available excerpt."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Asymptotic of Bergman Kernel gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi‑classical symbol space and symbolic calculus inspired by work of Hsiao and Savale [8]. Its introduction sets up the Bergman kernel for high tensor powers $L^{k}$ of a holomorphic line bundle as the object of study [8].",
      "reason": "Reference [8] lacks a supplied excerpt; the description cannot be verified against the allowed source material.",
      "fix": "Remove the citation and the detailed claim, or replace with a statement supported by an available excerpt."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Formal verification and well‑foundedness. DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments provides a modified version of Gentzen’s 1936 consistency proof, based on Gödel’s reformulation, with additional details and minor corrections necessary to definitively prove the well‑foundedness of the cut‑elimination argument in a constructive environment [3]. Its text records that the work builds on an incomplete formalization effort, completing it and fixing existing bugs in a proof‑assistant setting [3].",
      "reason": "No excerpt for reference [3] is provided; the summary of its contributions is not supported by the allowed source material.",
      "fix": "Delete the citation and the unsupported summary, or replace with a claim that can be sourced from an available excerpt."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Prior QNFO work on ensemble drafting. Ensemble Drafting Under Broadcast Control formalizes ensemble drafting — a population of draft generators whose candidate tokens are checked by a single verifier — as a discrete‑time population‑level control problem, deriving closed‑form expressions for expected accepted length, per‑cycle cost, and throughput [9]. Its results compute, with shown arithmetic, $E[L]=2.533$ and $T\\approx1.8093$ at draft depth $K=4$ with $\\alpha=0.7$, a grid optimum $K^{\\star}=5$ at $T\\approx1.8487$, a break‑even draft cost $c_{d}^{\\star}\\approx0.1527$, a $1/\\sqrt{N}$ standard‑error reduction from $\\sigma=0.3$ to $\\approx0.1342$ at $N=5$, and a Vandermonde reachability map that is exactly controllable iff the parameters are pairwise distinct [9]. Its discussion flags that the constant‑$\\alpha$ independence assumption is the strongest and least defensible, since real drafter quality is autocorrelated across positions and correlated drafter errors break the $\\sigma/\\sqrt{N}$ reduction [9].",
      "reason": "Reference [9] has no supplied excerpt; the detailed quantitative results and discussion cannot be verified from the allowed source material.",
      "fix": "Remove the citation and the specific quantitative claims, or replace with a statement that is supported by an available excerpt."
    }
  ],
  "soft": []
}