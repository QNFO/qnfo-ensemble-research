{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "[1] presents a formalism for quantifying contextuality in quantum optics, demonstrating that interference visibility can be expressed as a probability difference; this informs our use of outcome distributions.",
      "reason": "The cited work [1] is about a cryptography Olympiad and contains no discussion of quantum optics, contextuality, or interference visibility. The claim is unsupported by the source.",
      "fix": "Remove or replace the citation with a work that actually discusses contextuality in quantum optics, or delete the sentence."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "[2] derives the total‑variation distance for distinguishable versus indistinguishable particles in a beamsplitter, reporting a value of $0.5$, which we adopt as the per‑element divergence.",
      "reason": "The cited work [2] deals with knot invariants and does not contain any analysis of beamsplitters or total‑variation distance for particles.",
      "fix": "Delete the citation and the claim, or replace with a correct source that derives the $0.5$ divergence."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "[3] introduces an operational measure of semantic mismatch in quantum communication protocols, showing how decision‑relevant observables can be mapped to engineering actions.",
      "reason": "The cited work [3] is about classification of unitary elements of C*-algebras and does not discuss semantic mismatch or quantum communication protocols.",
      "fix": "Remove the citation and the unsupported statement, or cite an appropriate source."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "[4] discusses the impact of mode‑matching errors on interference outcomes, providing a quantitative loss model that underlies our independence assumption.",
      "reason": "The cited work [4] concerns conformal structure of quantum wave mechanics and contains no discussion of mode‑matching errors in interferometry.",
      "fix": "Delete or replace the citation with a source that actually addresses mode‑matching errors."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "[5] offers a compositional framework for aggregating independent error sources, yielding the product form used in Eq. (3).",
      "reason": "The cited work [5] is about weak shocks in quantum plasmas; it does not present a compositional error‑aggregation framework.",
      "fix": "Remove the citation and the claim, or provide a correct reference."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "[6] reports experimental benchmarks for photon‑pair sources, establishing realistic values for indistinguishability that motivate our idealised analysis.",
      "reason": "The cited work [6] discusses one‑loop corrections to the photon propagator in curved‑space QED, not experimental photon‑pair source benchmarks.",
      "fix": "Delete the citation and the unsupported statement, or cite an appropriate experimental study."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "[7] critiques the use of particle‑based terminology in circuit models, arguing for vocabulary‑neutral descriptions, which motivates our motivation.",
      "reason": "The cited work [7] is about topological description of Legendrian contact homology and does not address terminology in circuit models.",
      "fix": "Remove the citation and the claim, or replace with a relevant source."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "[8] surveys design‑space‑exploration tools for quantum hardware, highlighting the need for quantitative fidelity metrics such as the one introduced here.",
      "reason": "The cited work [8] concerns families of superintegrable Hamiltonians and does not survey quantum‑hardware design‑space‑exploration tools.",
      "fix": "Delete the citation and the statement, or cite an appropriate survey."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Large‑scale quantum‑computing programmes allocate billions of dollars to hardware that must interoperate across disciplinary boundaries.",
      "reason": "The paper provides no source or derivation for the monetary figure; it is a quantitative claim without support or projection.",
      "fix": "Remove the monetary claim or label it as a projection with a cited source; otherwise provide a verifiable source."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "When these commitments conflict, design teams can pursue architectures that are fundamentally incompatible with the underlying hardware, inflating budgets and delaying commercial delivery.",
      "reason": "The claim about budget inflation and delays is quantitative (implies cost impact) but lacks any source or calculation; it is presented as fact without support.",
      "fix": "Rephrase to a qualitative statement or provide a sourced quantitative estimate."
    }
  ],
  "soft": []
}