{
  "verdict": "revise",
  "hard": [
    {
      "id": "CIT5",
      "severity": "HARD",
      "claim": "Learned message passing for classical codes [5]. This work demonstrates that a fully differentiable GNN can learn a generalized message‑passing algorithm over the Tanner graph of a classical error‑correction code, achieving competitive performance on LDPC and BCH codes. The key distinction is that the Tanner graph is fixed per code, whereas the DEM graph varies with both code and noise model, raising the transfer question that POLYMECHANON must answer.",
      "reason": "The bibliography entry for [5] provides only the title and identifier, with no excerpt containing the described findings. The claim cannot be verified from the supplied source.",
      "fix": "Remove or replace the statement with a claim supported by an available excerpt, or cite a work whose excerpt contains the described result."
    },
    {
      "id": "CIT4",
      "severity": "HARD",
      "claim": "Universal graph embeddings via transfer learning [4]. The authors show that existing GNN embeddings do not transfer robustly across graph distributions without deliberate design. POLYMECHANON’s cross‑code model, which degrades on unseen larger codes, exemplifies this structural difficulty of graph transfer learning.",
      "reason": "The bibliography entry for [4] contains only the title and identifier; no excerpt supports the specific claim about transfer robustness.",
      "fix": "Delete or rephrase the claim, or replace with a citation whose excerpt includes the stated observation."
    },
    {
      "id": "CIT7",
      "severity": "HARD",
      "claim": "Sparse defect‑centric decoding [7]. The Sparse Mamba Decoder processes only active detection events, achieving $\mathcal{O}(k)$ complexity in the number of defects $k$, whereas POLYMECHANON processes the full DEM whose size is $O(d^{2}R)$. Their interaction is quantified in Section 4.5.",
      "reason": "The bibliography entry for [7] provides only the title and identifier, lacking any excerpt that states the $\mathcal{O}(k)$ complexity claim.",
      "fix": "Remove the quantitative comparison or cite a source that actually contains the complexity statement."
    },
    {
      "id": "CIT6",
      "severity": "HARD",
      "claim": "Adaptive‑topology graph architectures [6]. GraphFPN shows that multi‑scale feature learning benefits when network topology adapts to the input rather than remaining fixed. This is salient because a DEM decoder must handle graphs of wildly varying size and structure; whether fixed‑depth message passing suffices for long‑range qLDPC correlations is an open question.",
      "reason": "The bibliography entry for [6] includes only title and identifier; the excerpt does not contain the described benefit of multi‑scale feature learning.",
      "fix": "Omit the statement or replace it with a citation that includes the relevant finding."
    },
    {
      "id": "CIT3",
      "severity": "HARD",
      "claim": "Random neural networks [3]. This tutorial frames neural computation as a queuing‑network problem, a perspective useful for interpreting DEM decoding as a probabilistic flow problem.",
      "reason": "The bibliography entry for [3] lacks any excerpt supporting this queuing‑network framing.",
      "fix": "Delete the sentence or cite a source that actually discusses the queuing‑network perspective."
    },
    {
      "id": "CIT8",
      "severity": "HARD",
      "claim": "Transfer learning for recurrent predictors [8]. The LSTM air‑pollutant study illustrates the standard pretrain‑then‑finetune recipe and its degradation on distant target domains, providing a calibration point for POLYMECHANON’s cross‑code claims.",
      "reason": "The bibliography entry for [8] provides only title and identifier; no excerpt confirms the described study or its findings.",
      "fix": "Remove the reference or replace with a source that contains the described experimental result."
    },
    {
      "id": "CIT9",
      "severity": "HARD",
      "claim": "Semi‑supervised graph anomaly detection [9]. Mul‑GAD aggregates multi‑view information for anomaly detection on heterogeneous graphs. Syndrome decoding is formally an anomaly‑localization task on the DEM graph, making the aggregation lessons directly relevant.",
      "reason": "The bibliography entry for [9] includes only title and identifier; the excerpt does not contain the stated claim about multi‑view aggregation relevance.",
      "fix": "Eliminate the claim or cite a work whose excerpt supports it."
    },
    {
      "id": "CIT11",
      "severity": "HARD",
      "claim": "A cheap certificate uses part‑size vectors $(|D|,|M|,|L|)$. For the $d=8$ surface‑code DEM the vector is $(441,1337,1)$. For any $R$‑round $[[130,4,6]]$ DEM under the assumed multiplier it is $(126R,520R,4)$. No integer $R$ satisfies both $126R=441$ and $520R=1337$, so the two DEMs are provably non‑isomorphic by part sizes alone. This structural separation aligns with the reported cross‑family generalization gap [1, 2].",
      "reason": "The claim about isomorphism invariants references [11] for the definition of attributed graph isomorphism, but the bibliography entry for [11] contains only a title and URL, no excerpt defining or discussing isomorphism.",
      "fix": "Remove the citation to [11] or provide a derivation that does not rely on an uncited definition."
    },
    {
      "id": "DERIV1",
      "severity": "HARD",
      "claim": "Result 2 includes the encoding rate $k/n=4/130\approx3.08\%$.",
      "reason": "The paper does not show the arithmetic for this division in Section 4; the quantitative claim lacks a derived computation as required.",
      "fix": "Add a short derivation in Section 4 (e.g., $k/n = 4/130 = 0.030769\approx3.08\%$) or label the statement as a projection with the assumption."
    }
  ],
  "soft": []
}