{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "The central experimental anchor is the study of readout failures in superconducting qubits due to TLS defects in tunnel junctions [6]. That work identifies material defects as the origin of parasitic two‑level systems that constitute a major source of decoherence in superconducting qubits, and it studies a strongly coupled TLS residing in the tunnel barrier of a transmon qubit using multi‑photon spectroscopy and TLS strain tuning to explore the spectrum of the interacting three‑partite system of TLS, qubit, and readout resonator. Its discussion reports avoided‑level‑crossing features at $6.2\\ \\mathrm{GHz}$ (single‑photon transition) and $6.08\\ \\mathrm{GHz}$ (two‑photon transition), and it records junction areas of roughly $200\\ \\mathrm{nm}\\times220\\ \\mathrm{nm}$, which set the order of magnitude of the barrier volume used in this paper.",
      "reason": "The paper makes detailed factual claims about the content of work [6] (specific frequencies, junction dimensions, experimental methods) but no excerpt of [6] is provided in the supplied bibliography; therefore the statements are not derivable from the given source and violate the citation integrity rule.",
      "fix": "Remove or substantially re‑phrase the statements about [6] to only include information that can be directly supported by the supplied excerpt, or add a proper excerpt from [6] that contains the claimed details."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "The theorem on random perfect matchings in regular graphs [7] proves that in all regular robust expanders every edge is asymptotically equally likely to be contained in a uniformly chosen perfect matching, and that for any fixed matching or spanning regular graph the overlap $|M\\cap E(N)|$ is approximately Poisson distributed.",
      "reason": "No excerpt for reference [7] is supplied; the paper’s description of the theorem cannot be verified against the provided source material, violating the requirement that citations be grounded in supplied excerpts.",
      "fix": "Either remove the citation to [7] or replace the description with a statement that can be supported by an available excerpt, or provide the necessary excerpt from [7]."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "The review of one‑dimensional stochastic growth and its connection to Gaussian ensembles of random matrices [8] establishes that surface fluctuations of the polynuclear growth model coincide, for both curved and flat growth, with limit distribution functions from Gaussian random‑matrix ensembles, with the connection explained through associated point processes.",
      "reason": "Reference [8] has no supplied excerpt; the claim about its content cannot be verified, breaching citation integrity.",
      "fix": "Delete or rewrite the statement to only reflect information present in an available excerpt, or include the relevant excerpt from [8]."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "The Helol tunnel work [1] targets the combinatorial properties of Client Hello packets in the TLS protocol to build a covert channel for data exfiltration and command‑and‑control, evaluating throughput distributions from fingerprint datasets.",
      "reason": "While an excerpt for [1] is provided, the paper’s claim about “evaluating throughput distributions from fingerprint datasets” is not explicitly present in the excerpt; the excerpt discusses numerical analysis and datasets but does not contain a clear statement that the work evaluates throughput distributions. This overstates the source.",
      "fix": "Adjust the description to match the exact content of the excerpt, e.g., mention that the work formulates throughput and uses datasets to compute distributions, without asserting evaluation if not present."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "The post‑quantum signature placement study [5] examines how signature‑algorithm choice in TLS 1.3 couples with certificate‑hierarchy structure, identifying a decisive variable in the placement of SLH‑DSA.",
      "reason": "No excerpt for reference [5] is supplied; the specific claim about its findings cannot be verified against the provided source material.",
      "fix": "Remove or re‑phrase the statement about [5] to only include verifiable information, or add the appropriate excerpt from [5]."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "The parallel worth noting is methodological: all three treat a large combinatorial space of protocol configurations statistically, asking what a random draw from that space looks like and which aggregate variable dominates the outcome.",
      "reason": "This methodological parallel is asserted for works [1], [3], and [5] without supporting excerpts for [3] and [5]; the claim cannot be substantiated from the supplied bibliography excerpts.",
      "fix": "Limit the parallel discussion to works for which excerpts are available (e.g., only [1]), or provide the necessary excerpts for [3] and [5]."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "The statistical machinery comes from two traditions. The theory of random dynamical systems [2] combines ideas and methods from probability theory and dynamical systems, motivated by inaccurate knowledge of the particular physical system or by computational and theoretical limitations such as insufficient computational power, inefficient algorithms, or insufficiently developed mathematical tools.",
      "reason": "The excerpt for [2] includes a description of random dynamical systems but does not contain the specific phrase about “insufficient computational power, inefficient algorithms, or insufficiently developed mathematical tools”. This overstates the source.",
      "fix": "Edit the sentence to reflect only the content present in the excerpt, e.g., mention that the concept combines probability and dynamical systems and addresses inaccurate knowledge of the system."
    }
  ],
  "soft": []
}