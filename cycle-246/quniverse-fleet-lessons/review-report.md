{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "and exceeds the documented $90 per 30 days gate by $22.2 %$.",
      "reason": "The 22.2 % exceedance is not derived in any section nor labeled as a projection with assumptions; no arithmetic is shown.",
      "fix": "Either provide a full derivation showing (110‑90)/90 = 0.222 ≈ 22.2 % and label it as a projection, or remove the statement."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "Incorporating a 50 % reduction in per‑worker failure probability raises the composite autonomy score from the reported **3.6** to **4.66**",
      "reason": "The baseline autonomy score of 3.6 is never derived; Section 4 computes a baseline of 4.26. The claim is unsupported by the paper’s arithmetic.",
      "fix": "Replace the baseline value with the derived 4.26 (or label the 3.6 figure as an external assumption with citation) and adjust the sentence accordingly."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Federated‑learning testbeds address how distributed research infrastructure can be evaluated in a controlled, reproducible setting before deployment [3].",
      "reason": "No excerpt from source [3] is provided in the bibliography; the statement cannot be verified from the supplied text.",
      "fix": "Remove the sentence or replace it with a specific point that is present in the supplied excerpt of [3]."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Control strategies for autonomous vehicles treat the vehicle as a plant driven by a dedicated control system that must track a prescribed trajectory [4].",
      "reason": "The bibliography does not contain an excerpt supporting this claim; therefore it is not grounded.",
      "fix": "Delete the sentence or substitute a verifiable claim from the provided excerpt of [4]."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "FLEET for text generation studies how generation trajectories can be improved by exploiting logit entropy during decoding [5].",
      "reason": "No supporting excerpt from source [5] is supplied; the claim is unsubstantiated.",
      "fix": "Remove the sentence or replace it with a statement directly supported by the excerpt of [5] (if any)."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "Intersection‑focused verification develops a situation‑coverage verification and validation framework for autonomous vehicles, implemented in the CARLA simulator [6].",
      "reason": "The bibliography does not provide an excerpt confirming this description; the claim lacks source support.",
      "fix": "Delete the sentence or rewrite it using only information present in the excerpt of [6]."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "Topological photonics is written as a community roadmap connecting topological modes to future technologies [7].",
      "reason": "No excerpt from source [7] is given; the claim cannot be verified.",
      "fix": "Remove the sentence or replace it with a verifiable point from the excerpt of [7]."
    },
    {
      "id": "H8",
      "severity": "HARD",
      "claim": "QNFO funding strategy documents a monthly AI‑stack spend of **$400–$600** and a target of **$100–$200** per month, providing the cost baseline for our economic analysis [8].",
      "reason": "The supplied excerpt for [8] does not contain these figures; the claim is unsupported.",
      "fix": "Delete the sentence or cite the actual numbers present in the excerpt of [8] (if any)."
    },
    {
      "id": "H9",
      "severity": "HARD",
      "claim": "QNFO gap synthesis enumerates **42** gaps, of which **5** are high severity, and reports a DAG depth $\le$ 3 for dependency resolution [9].",
      "reason": "The bibliography excerpt for [9] does not provide these statistics; the claim lacks grounding.",
      "fix": "Remove the sentence or replace it with a claim directly supported by the excerpt of [9]."
    },
    {
      "id": "H10",
      "severity": "HARD",
      "claim": "Claim‑integrity taxonomy demonstrates how to register dated, falsifiable predictions with explicit disconfirmation criteria [10].",
      "reason": "No excerpt from source [10] is supplied; the statement cannot be verified.",
      "fix": "Delete the sentence or rewrite it using only information present in the excerpt of [10]."
    }
  ],
  "soft": []
}