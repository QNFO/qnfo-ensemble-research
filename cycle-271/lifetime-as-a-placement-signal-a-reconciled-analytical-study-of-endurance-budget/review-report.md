{
  "verdict": "revise",
  "hard": [
    {
      "id": "H1",
      "severity": "HARD",
      "claim": "* [1], [2] Lachesis. The system places KV segments in HBM or HBF at write time based on predicted lifetime and frees blocks once the segment is no longer read. The entry reports extension factors of **1.50–2.95×** for the tight SLO and **1.19–1.89×** for the loose SLO, and absolute HBF lifetimes of **3.3–9.3 device‑years**.",
      "reason": "The excerpt for reference [2] does not contain the reported extension factors or lifetime numbers; only reference [1] provides those details. Citing [2] for this specific quantitative claim is unsupported.",
      "fix": "Remove the citation to [2] (retain citation to [1] only) or replace it with a statement that is directly supported by the excerpt of [2]."
    },
    {
      "id": "H2",
      "severity": "HARD",
      "claim": "* **[3] Congestion‑aware routing and content placement in elastic cache networks.** This work formulates joint cache deployment, content placement, and hop‑by‑hop routing as a cost‑coupled optimization problem, showing that heuristic placement can be up to 30 % more expensive than joint optimization.",
      "reason": "No excerpt from reference [3] is provided in the bibliography, so the specific claim about a 30 % cost increase cannot be derived from the supplied text.",
      "fix": "Delete the citation to [3] or replace the sentence with a claim that is directly supported by the available excerpt of [3] (if any)."
    },
    {
      "id": "H3",
      "severity": "HARD",
      "claim": "* **[4] PolyKV.** PolyKV compresses KV caches across multiple agents, demonstrating a substantial reduction in KV memory footprint, which can further stretch flash endurance when combined with placement strategies.",
      "reason": "The bibliography does not include any excerpt from reference [4] containing the described compression results; therefore the statement is unsupported.",
      "fix": "Remove the citation to [4] or replace the sentence with a point that is explicitly present in the excerpt of [4]."
    },
    {
      "id": "H4",
      "severity": "HARD",
      "claim": "* **[5] HBF for generative recommendation serving.** This study shows that an admission‑controlled LRU‑$K$ policy can extend HBF lifetime relative to a baseline, providing an independent data point on how policy choices affect endurance.",
      "reason": "No excerpt from reference [5] is supplied, so the claim about the LRU‑$K$ policy’s effect on lifetime is not verifiable from the provided source.",
      "fix": "Delete the citation to [5] or replace the claim with a statement directly supported by the excerpt of [5] (if any)."
    },
    {
      "id": "H5",
      "severity": "HARD",
      "claim": "* **[6] HBM Is Not All You Need.** The paper observes that LLM inference splits into a compute‑bound prefill phase and a memory‑bound decode phase, proposing memory‑heterogeneous accelerators that pair GDDR‑based prefill engines with HBM‑based decode GPUs. It argues that HBM bandwidth is a scarce resource, reinforcing the motivation to reserve HBM writes for short‑lived data.",
      "reason": "The supplied excerpts for reference [6] do not contain the described observations or arguments; thus the citation is unsupported.",
      "fix": "Remove the citation to [6] or replace the sentence with a claim that is explicitly present in the excerpt of [6]."
    },
    {
      "id": "H6",
      "severity": "HARD",
      "claim": "* **[8] Cache‑coloring for non‑volatile caches.** This work shows that write‑variation‑unaware policies cause excessive writes to a few blocks in non‑volatile caches, and that a cache‑coloring technique yields a **4.20×** lifetime improvement with only a 4 % performance penalty.",
      "reason": "No excerpt from reference [8] is provided, so the specific quantitative improvement claim cannot be sourced.",
      "fix": "Delete the citation to [8] or replace the claim with a point directly supported by the excerpt of [8] (if any)."
    },
    {
      "id": "H7",
      "severity": "HARD",
      "claim": "* What benchmark suite (inspired by [9]) can isolate each of the three lifetime axes for reproducible extension‑factor measurement?",
      "reason": "The bibliography does not include any excerpt from reference [9]; therefore the suggestion of a benchmark suite inspired by it is unsupported.",
      "fix": "Remove the citation to [9] or replace the sentence with a reference to a work whose excerpt actually discusses such a benchmark suite."
    }
  ],
  "soft": []
}