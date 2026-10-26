{
  "verdict": "revise",
  "hard": [
    {
      "id": "C1",
      "severity": "HARD",
      "claim": "Lithium‑niobate on insulator (LNOI) devices have demonstrated $Q>10^{8}$ at $1550\\,$nm [5].",
      "reason": "Citation [5] is used to support a quantitative claim, but no excerpt from the bibliography entry for [5] is provided; thus the claim is not verifiable from the supplied source.",
      "fix": "Replace the claim with a statement supported by an available excerpt, or remove the citation to [5]."
    },
    {
      "id": "C2",
      "severity": "HARD",
      "claim": "A $70\\,\\mu\\text{m}$ radius LNOI microring exhibits a $3\\,$pm V$^{-1}$ tuning slope and a $300\\,$nm bus‑ring gap that yields strong over‑coupling [4].",
      "reason": "Citation [4] is used without any supporting excerpt in the provided bibliography; the claim cannot be substantiated.",
      "fix": "Either provide a supported quantitative description from an available source or remove the unsupported details and citation."
    },
    {
      "id": "C3",
      "severity": "HARD",
      "claim": "Electro‑optic tunable LNOI resonators fabricated with high index contrast achieve low bending loss and maintain high $Q$ for radii down to a few microns [10].",
      "reason": "Citation [10] is made without any excerpt from its entry; the statement lacks grounding in the supplied text.",
      "fix": "Delete or rephrase the sentence to rely only on sources with available excerpts."
    },
    {
      "id": "C4",
      "severity": "HARD",
      "claim": "Finally, the synthetic‑dimension architecture proposed in [12] and the thermal‑photon occupation analysis in [13] provide the thermodynamic and topological context for operating a 4‑D lattice at cryogenic temperatures.",
      "reason": "Citations [12] and [13] are used without any excerpt from their entries; the claim is not verifiable from the supplied bibliography.",
      "fix": "Remove the unsupported citations or replace with statements that can be supported by available excerpts."
    },
    {
      "id": "C5",
      "severity": "HARD",
      "claim": "The terahertz‑driven analysis in [13] gives a synthetic hopping rate $J = 36.06\\,$GHz under this field.",
      "reason": "Citation [13] is used to provide a quantitative hopping rate, but no excerpt from [13] is supplied; the claim cannot be verified.",
      "fix": "Either supply a supported quantitative statement from an available source or label the value as an assumption/projection with a clear source."
    },
    {
      "id": "C6",
      "severity": "HARD",
      "claim": "Generating the field $E_{\\text{THz}}=10^{7}\\,$V m$^{-1}$ over a 1 mm interaction length requires a projected source power of $12.5\\,$W, as listed in [13].",
      "reason": "Citation [13] is used for a quantitative projection without an excerpt; the claim lacks grounding.",
      "fix": "Remove the citation or qualify the projection as an assumption without attributing to [13]."
    },
    {
      "id": "C7",
      "severity": "HARD",
      "claim": "For a rational flux $\\phi=2\\pi p/q$ the invariant reduces to $C_{2}=p^{2}$ [2].",
      "reason": "Citation [2] does not contain the statement that the second Chern number reduces to $p^{2}$; the excerpt deals with Hopf insulators and Chern numbers, not this specific formula.",
      "fix": "Replace the citation with a source that actually provides this relation, or remove the unsupported claim."
    },
    {
      "id": "C8",
      "severity": "HARD",
      "claim": "Higher‑order nonlinear processes (e.g., four‑wave mixing) are omitted, although the Hamiltonian framework in [8] shows they can modify effective hopping.",
      "reason": "Citation [8] is used to support a claim about nonlinear processes, but no excerpt from [8] is provided; the claim cannot be verified.",
      "fix": "Delete the citation or rephrase the statement without attributing to [8]."
    }
  ],
  "soft": [
    {
      "id": "S1",
      "severity": "SOFT",
      "claim": "The paper discusses at least eight bibliography works with specific points.",
      "reason": "While eight works are cited, several lack supporting excerpts, reducing the depth of literature treatment.",
      "fix": "Ensure all cited works have supporting excerpts or replace with adequately supported citations."
    },
    {
      "id": "S2",
      "severity": "SOFT",
      "claim": "Appendix A is present and documents divergences.",
      "reason": "Appendix A exists, satisfying the requirement.",
      "fix": "No action needed."
    }
  ]
}