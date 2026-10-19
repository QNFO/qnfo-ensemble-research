{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "error‑correction overhead range of $10^{2}$–$10^{3}$ physical operations per logical operation reported in the physics‑of‑computation literature [12].",
      "reason": "The bibliography provides no excerpt for reference [12]; the claim about the overhead range cannot be verified from the supplied source text.",
      "fix": "Remove or re‑label the statement as a projection with an explicit assumption, without citing [12]."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The present paper takes its cue from a question posed in the QNFO programme: after the critique of qubit‑centred ontology, what is the *actually demanded* role of a computational substrate [9]?",
      "reason": "Reference [9] has no supplied excerpt; the paper cannot substantiate that it poses the quoted question.",
      "fix": "Delete the citation to [9] and rephrase the sentence to state the question without attributing it to an unsupported source."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "Accurate assessment of capability levels $s_k$ (e.g., control‑readout fidelity) | Relies on the operational vocabulary defined in [10].",
      "reason": "Reference [10] has no supplied excerpt; the claim about its operational vocabulary cannot be verified.",
      "fix": "Remove the citation to [10] and present the statement as an assumption or general observation without unsupported attribution."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "Determination of the error‑correction overhead factor $r$ | Directly taken from the quantitative statement in [12] ($r\\in[10^{2},10^{3}]$).",
      "reason": "Reference [12] lacks an excerpt; the quantitative statement about $r$ is not supported by the provided source.",
      "fix": "Delete the citation to [12] and treat the overhead range as an assumed parameter, clearly labeled as a projection."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "Energy‑floor projection for a workload of $N_L$ logical operations | Computed in Section 4.3 using $E_{\\text{logical}}(r)$ from [12].",
      "reason": "Reference [12] provides no excerpt; the claim that the computation uses a value taken from [12] is unsupported.",
      "fix": "Remove the citation to [12] and keep the projection as derived from the assumed overhead range introduced in the paper."
    }
  ],
  "soft": []
}