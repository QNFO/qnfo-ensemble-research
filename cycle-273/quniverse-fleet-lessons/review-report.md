{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "[3] describes a collaborative autonomous‑research framework where agents employ an automatic repair mechanism, justifying the inclusion of a mitigation factor $\\alpha$.",
      "reason": "The excerpt for reference [3] does not contain any mention of an automatic repair mechanism or a mitigation factor; the statement is not supported by the supplied full‑text excerpt.",
      "fix": "Remove the unsupported claim or replace it with a statement that does not cite [3] for the mitigation factor."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "[5] introduces a claim‑integrity taxonomy that classifies quantitative statements by provenance and unit‑dimension validation; we adopt a streamlined version of this taxonomy for auditing the retracted claims.",
      "reason": "No excerpt from reference [5] is provided; the paper cannot assert that [5] introduces such a taxonomy without supporting text.",
      "fix": "Delete the sentence or rephrase without citing [5], stating that a claim‑integrity taxonomy is used without attributing it to [5]."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "[7] presents reliability‑analysis techniques based on hazard functions and survival probabilities, offering a natural extension of our Bernoulli formulation should timestamp data become available.",
      "reason": "The supplied excerpt for [7] does not mention hazard functions, survival probabilities, or any extension of Bernoulli models; the claim is unsupported.",
      "fix": "Remove the citation to [7] and the unsupported description, or replace with a supported point from the excerpt."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "[9] models microservice reliability with Poisson‑process assumptions and shows that mitigation interventions can reduce failures by up to $29\\%$; our assumed $50\\%$ reduction is therefore a conservative, optimistic scenario relative to that benchmark.",
      "reason": "The excerpt for [9] is not provided; the paper cannot claim a $29\\%$ reduction result without source support.",
      "fix": "Delete the sentence or replace it with a statement that does not rely on unsupported data from [9]."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "[10] integrates weighted sub‑scores into a composite reliability metric via linear combination, which we replicate for the composite autonomy score.",
      "reason": "No excerpt from reference [10] is supplied; the claim about weighted sub‑scores is not verifiable from the provided material.",
      "fix": "Remove the citation to [10] and the unsupported claim, or rephrase without attributing the method to [10]."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "[11] details an integrity‑audit pipeline that flags unit‑dimension mismatches and phantom results; this reinforces our emphasis on unit‑dimension verification for billing feeds.",
      "reason": "The excerpt for [11] is not provided; the statement cannot be substantiated from the given bibliography entries.",
      "fix": "Delete the sentence or rewrite it without citing [11]."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Inputs: $N_w=36$ (inventory from [12]), $p_f=0.12$ (assumption), $\\alpha=0.5$ (assumption).",
      "reason": "Reference [12] is a QNFO report but no excerpt is supplied; the claim that the inventory provides $N_w=36$ cannot be verified from the provided text.",
      "fix": "Remove the citation to [12] for the inventory count and state $N_w=36$ as an assumption or derived from internal data without citation."
    }
  ],
  "soft": []
}