{
  "verdict": "revise",
  "hard": [
    {
      "id": "CIT1",
      "severity": "HARD",
      "claim": "Tianyan‑287 superconducting processor (105 qubits; single‑qubit gate fidelity 99.90 %, two‑qubit gate fidelity 99.56 %, readout fidelity 98.7 %) [2].",
      "reason": "Citation [2] refers to \"Structure of the Standard Model\" in the provided bibliography, which does not contain any information about the Tianyan‑287 hardware. The reference is therefore incorrect.",
      "fix": "Remove the citation or replace it with a bibliography entry that actually describes the hardware; if none exists, delete the citation marker."
    },
    {
      "id": "CIT2",
      "severity": "HARD",
      "claim": "**[8]** introduces dagger Frobenius algebras as a categorical encoding of compositional structure [8]; this provides a formal language for expressing the compositional productivity condition of a Base State.",
      "reason": "Bibliography entry [8] is \"ConFuzzius: A Data Dependency‑Aware Hybrid Fuzzer for Smart Contracts\", which does not discuss dagger Frobenius algebras. The citation is unsupported.",
      "fix": "Remove the citation or replace it with a correct bibliography entry that discusses dagger Frobenius algebras; if none exists, delete the citation marker."
    },
    {
      "id": "CIT3",
      "severity": "HARD",
      "claim": "**[9]** defines the Base State hypothesis and audits feasibility against the Tianyan‑287 platform, deriving per‑operation error rates and fidelity budgets [9].",
      "reason": "Bibliography entry [9] is a QNFO page titled \"The Base State Hypothesis: A Falsification Protocol for a Substrate Capable of Hosting the Standard Model, Audited Against Contemporary Quantum Platforms\". This matches the claim, but the URL provided in the bibliography does not contain the detailed quantitative derivations referenced; the paper treats it as a source of those derivations without evidence from the supplied excerpt.",
      "fix": "Verify that the cited QNFO page actually contains the stated derivations; if not, replace the citation with a source that does, or label the statements as projections."
    },
    {
      "id": "CIT4",
      "severity": "HARD",
      "claim": "**[10]** articulates a constructive critique of the qubit‑gate model and asks what comes next [10]; the Base State hypothesis directly answers this “what comes next” question.",
      "reason": "Bibliography entry [10] is \"The Trapped‑Ion Ultrametric Testbed: A Falsifiability Register for Testing p‑Adic Structure in Quantum Dynamics\", which does not contain a critique of the qubit‑gate model. The citation is unsupported.",
      "fix": "Remove the citation or replace it with a bibliography entry that actually provides the claimed critique."
    },
    {
      "id": "CIT5",
      "severity": "HARD",
      "claim": "**[11]** offers a position statement on emergent correlation in a deterministic universe [11]; it is cited only to acknowledge the broader philosophical context.",
      "reason": "Bibliography entry [11] is \"Base State–Disturbance (BS‑D) Ontology\", which does not discuss emergent correlation in a deterministic universe. The citation is unsupported.",
      "fix": "Remove the citation or replace it with a correct source; if none exists, delete the citation marker."
    },
    {
      "id": "CIT6",
      "severity": "HARD",
      "claim": "**[12]** outlines the Falsification Pledge and methodological stance of honest computation [12]; our protocol adopts its principle that every claim must be derived or explicitly labeled as a projection.",
      "reason": "Bibliography entry [12] is \"Standard Model\" and does not describe a Falsification Pledge or honest computation methodology. The citation is unsupported.",
      "fix": "Remove the citation or replace it with a bibliography entry that actually defines the Falsification Pledge."
    },
    {
      "id": "CIT7",
      "severity": "HARD",
      "claim": "References list includes entries such as \"Tianyan: Cloud services with quantum advantage\" (arXiv:2512.10504v2) labelled as [2] which is not present in the provided bibliography.",
      "reason": "Citation [2] in the References does not correspond to any entry in the supplied bibliography; this violates citation integrity.",
      "fix": "Delete the entry or replace it with a bibliography entry that exists."
    },
    {
      "id": "CIT8",
      "severity": "HARD",
      "claim": "References list includes \"Bell‑state measurement and quantum teleportation using linear optics...\" (arXiv:1304.1214v1) labelled as [3] which is not present in the provided bibliography.",
      "reason": "Citation [3] in the References does not correspond to any entry in the supplied bibliography; this violates citation integrity.",
      "fix": "Delete the entry or replace it with a bibliography entry that exists."
    },
    {
      "id": "CIT9",
      "severity": "HARD",
      "claim": "References list includes \"Searching for Coherent States: From Origins to Quantum Gravity\" (arXiv:2003.11810v4) labelled as [4] which is not present in the provided bibliography.",
      "reason": "Citation [4] in the References does not correspond to any entry in the supplied bibliography; this violates citation integrity.",
      "fix": "Delete the entry or replace it with a bibliography entry that exists."
    },
    {
      "id": "CIT10",
      "severity": "HARD",
      "claim": "References list includes \"A full circuit‑based quantum algorithm for excited‑states in quantum chemistry\" (arXiv:2112.14193v3) labelled as [5] which is not present in the provided bibliography.",
      "reason": "Citation [5] in the References does not correspond to any entry in the supplied bibliography; this violates citation integrity.",
      "fix": "Delete the entry or replace it with a bibliography entry that exists."
    },
    {
      "id": "CIT11",
      "severity": "HARD",
      "claim": "References list includes \"Interaction of light and semiconductor can generate quantum states required for solid state quantum computing...\" (arXiv:1811.09849v1) labelled as [6] which is not present in the provided bibliography.",
      "reason": "Citation [6] in the References does not correspond to any entry in the supplied bibliography; this violates citation integrity.",
      "fix": "Delete the entry or replace it with a bibliography entry that exists."
    },
    {
      "id": "CIT12",
      "severity": "HARD",
      "claim": "References list includes \"Unraveling the emergence of quantum state designs in systems with symmetry\" (arXiv:2402.08949v3) labelled as [7] which is not present in the provided bibliography.",
      "reason": "Citation [7] in the References does not correspond to any entry in the supplied bibliography; this violates citation integrity.",
      "fix": "Delete the entry or replace it with a bibliography entry that exists."
    },
    {
      "id": "CIT13",
      "severity": "HARD",
      "claim": "References list includes \"Quantum games and synchronicity\" (arXiv:2408.15444v4) labelled as [8] which is not present in the provided bibliography.",
      "reason": "Citation [8] in the References does not correspond to any entry in the supplied bibliography; this violates citation integrity.",
      "fix": "Delete the entry or replace it with a bibliography entry that exists."
    },
    {
      "id": "CIT14",
      "severity": "HARD",
      "claim": "References list includes \"The Base State Hypothesis (prior version)\" (QNFO URL) labelled as [9] which is present in the bibliography, but the paper treats it as a source of quantitative derivations not evident in the supplied excerpt.",
      "reason": "The bibliography excerpt for [9] does not contain the detailed quantitative derivations cited; using it to support those derivations is unsupported.",
      "fix": "Label the statements derived from [9] as projections with explicit assumptions, or provide a supporting excerpt."
    },
    {
      "id": "CIT15",
      "severity": "HARD",
      "claim": "References list includes \"The Trapped‑Ion Ultrametric Testbed...\" (QNFO URL) labelled as [10] which is present in the bibliography, but the paper cites it for a critique of the qubit‑gate model, which the excerpt does not contain.",
      "reason": "Citation [10] does not support the claimed critique; the citation is unsupported.",
      "fix": "Remove the claim or replace with a correct citation."
    },
    {
      "id": "CIT16",
      "severity": "HARD",
      "claim": "References list includes \"Base State–Disturbance (BS‑D) Ontology\" (QNFO URL) labelled as [11] which is present in the bibliography, but the paper cites it for a position statement on emergent correlation, which the excerpt does not contain.",
      "reason": "Citation [11] does not support the claimed content; the citation is unsupported.",
      "fix": "Remove the claim or replace with a correct citation."
    },
    {
      "id": "CIT17",
      "severity": "HARD",
      "claim": "References list includes \"QNFO: Manifesto for Honest Computation\" (QNFO URL) labelled as [12] which is present in the bibliography, but the paper cites it for outlining the Falsification Pledge, which the excerpt does not contain.",
      "reason": "Citation [12] does not support the claimed content; the citation is unsupported.",
      "fix": "Remove the claim or replace with a correct citation."
    }
  ],
  "soft": []
}