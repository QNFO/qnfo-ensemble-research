{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The immediate ancestor of this work is the silent‑radix proposal itself. The Silent‑Radix Cryptography note states the core observation—that a positional numeral cannot internally specify its own base, so the base is “silent”—and proposes Silent Radix Encryption (SRE), which uses a secret base $b$ as a trapdoor for key encapsulation and claims that security reduces to an unknown‑weight integer knapsack problem [9].",
      "reason": "Citation [9] is used to assert specific details about the silent‑radix proposal, but no excerpt from the bibliography for [9] is provided, violating source‑support requirement.",
      "fix": "Replace the detailed description with a generic statement that the proposal claims secrecy of the base, and label the specifics as an assumption without citing [9]."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "A third paper, HM‑LWE v3.0, proposes hidden‑modulus Learning With Errors as a novel hardness assumption: standard lattice‑based cryptography operates over a publicly known modulus, and the paper asks what happens when the modulus itself is secret, forcing the adversary into a joint search over modulus and key [10].",
      "reason": "Citation [10] lacks any supporting excerpt; the claim cannot be verified against the provided bibliography.",
      "fix": "Remove the specific claim about HM‑LWE or replace it with a generic statement about hidden‑modulus ideas without citing [10]."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The broader literature supplies the evaluation standards against which any new primitive must be judged. Kerckhoffs’s principle— the system must remain secure even if everything about it except the key is public— is operationalized in modern formal methods: the first formal model of Bitcoin’s Payment Protocol (BIP70) formalised the previously shown refund‑attack vulnerability ... [4].",
      "reason": "Citation [4] is used to support a claim about formal modeling of Bitcoin’s payment protocol, but no excerpt for [4] is provided.",
      "fix": "Remove the citation to [4] and rephrase the sentence to state the principle without referencing the specific work."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "If a mechanism such as unknown‑radix encoding were believed to be a viable lightweight cipher or key‑encapsulation trapdoor, it could enter that inventory as a candidate; if it is in fact breakable by classical statistical attacks on a single ciphertext, it must be excluded before it is ever deployed. Today no formal analysis exists that lets an architect, a standards body, or a protocol designer make that decision with confidence: the proposal circulates as an informal conjecture that a secret base $B$—the observation that a positional numeral cannot specify its own base—could act as a cryptographic trapdoor [9].",
      "reason": "Citation [9] again used without supporting excerpt.",
      "fix": "Replace the citation with an assumption statement and remove the specific reference to [9]."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The primary users are security architects and standards reviewers who maintain Cryptographic Bills of Materials (CBOMs). [5] describes CBOM methodology as the mechanism by which organisations decide which deployed cryptographic mechanisms to trust and which to retire.",
      "reason": "Citation [5] lacks an excerpt; the claim about CBOM methodology cannot be verified.",
      "fix": "Remove the citation to [5] and state the role of CBOMs without referencing the specific work."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The broader literature supplies the evaluation standards against which any new primitive must be judged. ... The Multi‑Factor Key Derivation Function (MFKDF) construction extends password‑based key derivation with additional authentication factors such as TOTP, HOTP, and hardware tokens [6].",
      "reason": "Citation [6] is not supported by any provided excerpt.",
      "fix": "Delete the citation to [6] and keep the general statement about key‑management without referencing the work."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "A device‑centric analysis of Extended Reality (XR) devices surveys security and privacy attacks and defenses [7]. The lesson we draw is about evaluation culture: mechanisms deployed on consumer hardware are examined adversarially after deployment, so a mechanism whose security depends on a subtle parameter is a liability regardless of platform.",
      "reason": "Citation [7] lacks supporting excerpt; the claim cannot be verified.",
      "fix": "Remove the citation to [7] and keep the general observation without referencing the specific study."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "The work on cryptographically verifiable authorization for autonomous AI agents proposes a falsifiable hypothesis and proof of concept for giving agents’ requests cryptographic evidence of policy compliance ... [1].",
      "reason": "Citation [1] excerpt does not contain a claim about falsifiable hypotheses; the citation is unsupported.",
      "fix": "Delete the citation to [1] or replace with a statement that does not rely on that work."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "Biometric key‑generation work makes the same point from another direction: two closely related papers on generating cryptographic keys from multimodal biometric feature‑level fusion of fingerprint and iris address the problem ... [2], [3].",
      "reason": "Citations [2] and [3] lack excerpts supporting the described contributions; unsupported citations.",
      "fix": "Remove citations [2] and [3] and keep the general statement without referencing them."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "the gap between the two hypotheses is therefore at least $$\\frac{0.12}{10^{-3}}=7864.32.$$",
      "reason": "Arithmetic error: 0.12 / 0.001 = 120, not 7864.32.",
      "fix": "Correct the calculation to state the gap is at least 120."
    },
    {
      "id": "H11",
      "severity": "HARD",
      "claim": "R4 (discrimination gap, projection). Under the uniformity heuristic, the maximum‑digit‑frequency gap between correct and wrong base is a factor of at least $120$ for $n=1000$ and $B'\\ge2^{16}$ (Section 4.4).",
      "reason": "Inconsistent with earlier claim that the gap is at least 7864.32; the paper presents contradictory numbers without clarification.",
      "fix": "Align both statements to the same corrected value (120) and remove the contradictory earlier claim."
    },
    {
      "id": "H12",
      "severity": "HARD",
      "claim": "## Appendix A. Divergence report\n\nNo divergent claims were identified among the source drafts; all substantive claims converge on the same quantitative values and logical arguments.",
      "reason": "The paper contains divergent claims (e.g., gap factor inconsistency), making this statement false.",
      "fix": "Update the appendix to acknowledge the identified divergence and describe it."
    },
    {
      "id": "H13",
      "severity": "HARD",
      "claim": "## Provenance and AI Involvement\n\n- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline ... Models: drafting by openai/gpt‑oss‑120b, ...",
      "reason": "Meta‑commentary about AI involvement and the drafting process is prohibited.",
      "fix": "Remove the entire Provenance and AI Involvement section."
    },
    {
      "id": "H14",
      "severity": "HARD",
      "claim": "All quantitative results were independently verified by recomputation scripts, and no external peer review or manual validation has been applied to this version of the manuscript.",
      "reason": "Claims verification by scripts without providing the scripts constitute an unsupported empirical claim.",
      "fix": "Delete the claim about independent verification or provide the script (which is not present)."
    }
  ],
  "soft": []
}