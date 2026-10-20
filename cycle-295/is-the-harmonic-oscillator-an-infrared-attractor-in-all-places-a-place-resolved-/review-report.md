{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "References list skips [2] and misorders numbers, e.g., it starts with [1] then [3], [4]..., violating citation integrity.",
      "reason": "The bibliography contains entry [2] but the reference list omits it and reorders subsequent entries, breaking the required one‑to‑one correspondence and sequential numbering.",
      "fix": "Reorder the reference list to follow the bibliography order and include all cited works with correct numbering, inserting [2] in its proper place."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The paper cites [14] in the background section, but the provided bibliography contains only entries up to [13].",
      "reason": "Citation refers to a non‑existent bibliography entry, violating citation integrity.",
      "fix": "Remove the citation to [14] or replace it with a valid bibliography entry that supports the statement."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Background claim \"Universal bosonic mass scale for all $q$‑form fields is reported\" cites [11], but the excerpt for the universal mass scale is in entry [8].",
      "reason": "Incorrect citation number; the statement is not supported by the cited work.",
      "fix": "Change the citation from [11] to [8] to correctly reference the universal mass scale source."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Background claim \"At $p_L=10^{-6}$, bosonic codes require 5–40 × fewer photons and ≈100 × fewer modes than surface codes\" cites [12], but entry [12] is a QNFO link unrelated to this claim.",
      "reason": "Citation does not support the quantitative resource claim.",
      "fix": "Replace the citation with the correct source that contains this claim, or remove the claim if no supporting source exists."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Background claim \"The program maps physical architecture onto Bruhat–Tits trees, connecting the fine‑structure constant, RG, quantum error correction, and the Efimov effect\" cites [13], but entry [13] is a QNFO link not containing this content.",
      "reason": "Citation mismatch; the statement lacks a supporting source.",
      "fix": "Provide a correct citation to a source that discusses the Adelic Cross‑Domain Program, or delete the claim."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Background claim \"The adelic oscillator exists and softens the uncertainty relation\" cites [8], but the excerpt for [8] discusses a universal mass scale, not an adelic oscillator or uncertainty relation.",
      "reason": "The cited work does not contain the asserted content.",
      "fix": "Remove or rephrase the claim to reflect only what the cited source actually states."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Background claim \"General solution of the quantum damped HO is given\" cites [1], yet the excerpt for [1] describes quantum batteries and does not mention damped harmonic oscillators.",
      "reason": "Unsupported citation; the source does not provide the claimed information.",
      "fix": "Delete the claim or replace it with a citation to a source that actually presents the damped HO solution."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "Background claim \"Anti‑PT‑symmetric oscillator replacement ω→iω leads to unbounded eigenvectors\" cites [7], but entry [7] concerns measurement precision and uncertainty principle, not anti‑PT symmetry.",
      "reason": "Citation does not support the statement.",
      "fix": "Replace the citation with the correct source ([6]) that discusses anti‑PT‑symmetric oscillators, or remove the claim."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Background claim \"Semi‑classical measures depend on arithmetic frequency relations\" cites [4], but the excerpt for [4] deals with non‑commutative spaces, not semi‑classical measures.",
      "reason": "Unsupported citation; the source does not contain the asserted point.",
      "fix": "Delete or modify the claim to align with what [4] actually states."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "Background claim \"Universal bosonic mass scale for $q$‑forms reported\" cites [11], but entry [11] is a QNFO link unrelated to the mass‑scale result.",
      "reason": "Incorrect citation; the source does not contain the claimed result.",
      "fix": "Change the citation to [8] which actually reports the universal mass scale, or remove the claim."
    },
    {
      "id": "H11",
      "severity": "HARD",
      "claim": "Background claim \"Bosonic codes require 5–40 × fewer photons and ≈100 × fewer modes at $p_L=10^{-6}$\" cites [12], but entry [12] is a QNFO link that does not provide these numbers.",
      "reason": "Citation does not support the quantitative resource claim.",
      "fix": "Replace the citation with a proper source that contains these figures, or delete the claim."
    },
    {
      "id": "H12",
      "severity": "HARD",
      "claim": "Background claim \"Red‑team assessment notes that the Paradigm’s bibliography invokes Ostrowski’s theorem and $p$‑adic structures, but its core mechanisms are confined to the Archimedean place\" cites [14], which is not present in the bibliography.",
      "reason": "Citation to a non‑existent bibliography entry violates citation integrity.",
      "fix": "Remove the citation or provide a valid source that makes this assessment."
    }
  ],
  "soft": []
}