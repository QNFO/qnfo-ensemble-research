{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "Reference [5] treats exponential input‑to‑state stabilization of diagonal infinite‑dimensional systems with uncertain, time‑varying input delays, using a constant‑delay predictor feedback controller designed on a truncated finite‑dimensional model; its Theorem 2 requires the closed‑loop matrix to be Hurwitz, and its conclusion derives an ISS estimate, exactly as leakage out of the two‑level abstraction must be bounded in our model.",
      "reason": "The bibliography excerpt for [5] is not provided; the statement cannot be verified from the supplied source text.",
      "fix": "Remove or replace the sentence with a statement that does not rely on unsupported citation."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Reference [6] proposes a control‑oriented notion of finite‑state approximation, approximating discrete‑time plants with finite‑valued sensors and actuators by deterministic finite‑memory systems for certified‑by‑design controller synthesis; its framing that the approximation is built for the controller rather than derived from physics is the control‑theoretic statement of our claim that the qubit ontology is defined by the control loop.",
      "reason": "No excerpt for [6] is supplied; the claim is not grounded in the provided source.",
      "fix": "Remove or replace the sentence without citing [6]."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Reference [4] introduces Input‑Constrained Control Barrier Functions for synthesizing safety‑critical controllers for nonlinear control‑affine systems with input constraints; it identifies a subset of the safe set and constructs a controller rendering that subset forward‑invariant. We borrow the forward‑invariance idea as a question we pose—whether a forward‑invariant “ontological safe set’’ exists—but do not resolve it.",
      "reason": "The bibliography excerpt for [4] is not provided; the statement cannot be substantiated.",
      "fix": "Remove or replace the sentence without citing [4]."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Reference [7] formulates network epidemic control—isolating locations by banning movement, modeled as link removal—on discrete‑time SIS and SIR network models, proves the control problem can be cast as a QUBO solvable by quantum annealing, and benchmarks solvers on case studies. Its relevance is methodological: it shows the quantum formalism applied as a modeling layer to a non‑quantum control loop, supporting the view that the closure of the calibration chain, not the quantum‑classical distinction, generates the self‑referential structure.",
      "reason": "No excerpt for [7] is supplied; the claim is not supported by the provided source.",
      "fix": "Remove or replace the sentence without citing [7]."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The corpus document “No Thing There’’ [8] states that a qubit is a constrained two‑level subspace of a physical degree of freedom, that control pulses manipulate that degree of freedom, and that readout measures a macroscopic observable correlated with the qubit state.",
      "reason": "The bibliography excerpt for [8] is not provided; the statement cannot be verified.",
      "fix": "Remove or replace the sentence without citing [8]."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Input 1 (from [9]). Average readout fidelity $f_{\\mathrm{ro}}=99.991\\% = 0.99991$ for a trapped‑ion qubit, over $N_{\\mathrm{trials}}=10^{6}$ trials.",
      "reason": "No excerpt for [9] is supplied; the numerical value cannot be confirmed from the provided source.",
      "fix": "Remove the citation to [9] or replace with a statement that does not rely on an unsupported source."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Reference [10] reports mean‑squared errors (MSE) for readout architectures: latching readout MSE $0.254$ at noise $\\sigma=0.2$, raw continuous TWPA output MSE $0.042$ at $\\sigma=0.2$, and TWPA output with Kalman filtering MSE $0.015$ at $\\sigma=0.2$.",
      "reason": "No excerpt for [10] is supplied; the quantitative comparison is not grounded in the provided source.",
      "fix": "Remove or replace the sentence without citing [10]."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "k\\ge\\frac{\\ln(9\\times10^{-4})}{\\ln(0.5)} =\\frac{-7.01312}{-0.69315}\\approx10.118.",
      "reason": "Arithmetic error: the correct value of \\frac{\\ln(9\\times10^{-4})}{\\ln(0.5)} is approximately 10.112, not 10.118.",
      "fix": "Replace the numerical approximation with the correct value 10.112 and adjust any dependent statements accordingly."
    }
  ],
  "soft": []
}