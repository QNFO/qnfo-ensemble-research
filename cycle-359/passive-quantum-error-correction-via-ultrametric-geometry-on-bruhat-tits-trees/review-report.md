[
  {
    "id": "H1",
    "severity": "HARD",
    "claim": "Surface‑code implementations require millions of physical qubits per logical qubit, continuous syndrome extraction, and fast classical decoding, which together dominate the energy budget and limit scalability [1, 2].",
    "reason": "Citations [1] and [2] do not contain any statements about surface‑code overhead; their excerpts discuss photon‑loss AQEC and thermodynamically trivial quantum memory, respectively. The claim is unsupported by the cited sources.",
    "fix": "Remove the citation or replace it with a source that explicitly discusses surface‑code overhead, or rephrase the sentence without unsupported citations."
  },
  {
    "id": "H2",
    "severity": "HARD",
    "claim": "Energy barriers associated with moving an error across hierarchical levels grow exponentially with depth, yielding a scaling $E_{\\text{barrier}}(d)\\propto2^{d}$ for odd $p$ [13, 14].",
    "reason": "Citations [13] and [14] have no provided excerpts; the paper cannot assert their specific claim about the exponential barrier scaling.",
    "fix": "Remove the citations or provide a derivation without referencing unsupported sources."
  },
  {
    "id": "H3",
    "severity": "HARD",
    "claim": "The ultrametric norm $\\|\\cdot\\|_p$ induces the strong triangle inequality $\\|x+y\\|_p\\le\\max(\\|x\\|_p,\\|y\\|_p)$, guaranteeing that any two balls of equal radius are either nested or disjoint [12].",
    "reason": "Citation [12] has no excerpt supplied; the statement cannot be verified against the source.",
    "fix": "Remove the citation or replace it with a source that explicitly states this property, or keep the statement without citation."
  },
  {
    "id": "H4",
    "severity": "HARD",
    "claim": "Linear‑optics passive encoding. The passive linear‑optical scheme of [4] demonstrates that a passive error‑averaging protocol can be realised for polarization‑encoded photons.",
    "reason": "Citation [4] is listed but no excerpt is provided; the claim about the scheme cannot be substantiated from the supplied text.",
    "fix": "Remove the citation or rephrase the sentence to avoid an unsupported reference."
  },
  {
    "id": "H5",
    "severity": "HARD",
    "claim": "Passive GKP encoding. In [5] a superconducting circuit implements a passive version of the Gottesman‑Kitaev‑Preskill code, where the energy gap between logical states is exponentially small in a tunable parameter $\\omega_{0}$.",
    "reason": "Citation [5] lacks an excerpt; the specific claim about passive GKP encoding is not supported by the provided source.",
    "fix": "Delete the citation or adjust the statement to reflect only what is supported."
  },
  {
    "id": "H6",
    "severity": "HARD",
    "claim": "Symmetry‑based passive protection. The discussion in [6] emphasises that passive protection can arise from symmetries of the noise channel.",
    "reason": "Citation [6] has no excerpt; the assertion about symmetry‑based protection cannot be verified.",
    "fix": "Remove the citation or modify the claim to avoid unsupported reference."
  },
  {
    "id": "H7",
    "severity": "HARD",
    "claim": "Continuous‑time quantum error correction (CTQEC) in [7] relies on weak measurements and feedback, which are active operations albeit applied continuously.",
    "reason": "Citation [7] lacks an excerpt; the description of CTQEC is not grounded in the supplied source.",
    "fix": "Delete the citation or rephrase without unsupported reference."
  },
  {
    "id": "H8",
    "severity": "HARD",
    "claim": "Entanglement‑assisted quantum error‑correcting codes (EAQECCs) in [8] increase the correctable error set by sharing ebits.",
    "reason": "Citation [8] has no excerpt; the claim about EAQECCs is unsupported.",
    "fix": "Remove the citation or adjust the statement."
  },
  {
    "id": "H9",
    "severity": "HARD",
    "claim": "The standard active surface‑code paradigm described in [10] incurs a thermodynamic overhead due to repeated measurements and decoding.",
    "reason": "Citation [10] has no excerpt; the statement about surface‑code thermodynamic overhead is not supported by the provided source.",
    "fix": "Delete the citation or rewrite the sentence without it."
  },
  {
    "id": "H10",
    "severity": "HARD",
    "claim": "The energy‑gap protection strategy in adiabatic quantum computation (AQC) discussed in [11] relies on a large spectral gap to suppress transitions.",
    "reason": "Citation [11] lacks an excerpt; the claim cannot be verified against the source.",
    "fix": "Remove the citation or modify the claim."
  },
  {
    "id": "H11",
    "severity": "HARD",
    "claim": "Classical LDPC codes can improve distance but reduce rate, as reviewed in [9].",
    "reason": "Citation [9] has no excerpt; the specific statement about LDPC trade‑off is unsupported.",
    "fix": "Delete the citation or rephrase without it."
  },
  {
    "id": "H12",
    "severity": "HARD",
    "claim": "Section numbering is incorrect: the required heading \"## 6. Discussion\" is missing; the paper uses \"## 7. Discussion\" after an extra \"## 6. Extended Derivations and Worked Examples\" section.",
    "reason": "The paper does not follow the required section order, violating structural requirements.",
    "fix": "Rename sections to match the required order: make the extended derivations a subsection of Results or insert it as a separate required section, and ensure Discussion is labeled \"## 6. Discussion\"."
  },
  {
    "id": "H13",
    "severity": "HARD",
    "claim": "Section numbering is incorrect: the required heading \"## 7. Practical Implications and Engineering Pathways\" is labeled \"## 8. Practical Implications and Engineering Pathways\".",
    "reason": "The paper deviates from the mandated heading order, causing a structural violation.",
    "fix": "Rename the heading to \"## 7. Practical Implications and Engineering Pathways\" and adjust subsequent headings accordingly."
  }
]