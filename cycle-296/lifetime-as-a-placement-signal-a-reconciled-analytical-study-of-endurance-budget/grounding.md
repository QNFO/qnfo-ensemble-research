# Grounding block - source: rem-rev-bc543335-911c-44aa-b77b-cde9d25e6c3d

## Research idea

Lachesis: Lifetime-Aware KV Cache Placement for Agent Serving across HBM and High-Bandwidth Flash. Large language model (LLM) serving is increasingly dominated by agentic workloads, in which agents and their sub-agents accumulate context as KV cache across many requests, consuming substantial memory. High-bandwidth flash (HBF) is a promising solution, providing an order of magnitude greater capacity at HBM-class read bandwidth, but its finite write endurance is the key limiting factor. Our key insight is that KV cache should be placed across HBM and HBF by its lifetime. Placing shorter-lived data in HBM lets HBM absorb more of an agent run's writes and sends less of them to HBF. As the life... Source: https://arxiv.org/abs/2610.08378v1 (arxiv-computing-energy, arXiv cs.ET + physics.app-ph + cs.PF + cs.AR (emerging technologies, applied physics, performance, architecture: the energy of computing)). Why it fits: agentic.

Post-publication revision of the published paper "Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High‑Bandwidth Flash in Agentic LLM Serving" (version 2.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 10 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 10, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Headline inputs (extension 1.19–3.13×, lifetime 3.3–12.2 device-years) attributed to [1] do not match the numbers the paper itself says [1] reports. (confirmed by a second model)
2. The derived HBM-first baseline lifetimes (1.05–10.25 yr, Section 4C) contradict the per-configuration baselines the paper says [1] provides (HBM-first 1.9–4.8 yr, per the Appendix A divergence report and claim C17). (confirmed by a second model)

## Existing paper under revision (remediation only)

# Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High‑Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large‑language‑model (LLM) serving accumulates key‑value (KV) cache across many orchestrated requests. High‑bandwidth flash (HBF) offers an order‑of‑magnitude larger capacity than high‑bandwidth memory (HBM) while delivering comparable read bandwidth, but its finite program/erase (P/E) endurance limits the amount of write traffic it can absorb. Lachesis proposes a lifetime‑aware placement layer that routes KV segments to HBM or HBF based on the interval between a segment’s first write and its last read. This paper formalizes that placement principle as a lifetime‑threshold rule, derives the algebra linking write diversion to HBF device‑year lifetime, and computes, with fully shown arithmetic, the quantitative consequences of the headline extension factors reported for Lachesis. Using the endurance rating $E_{\mathrm{HBF}}=10^{5}$ cycles from the HBF device specification [7] and a write‑amplification factor $\mathrm{WAF}\approx1.02$, we obtain: (i) warranty‑margin factors of $0.66\times$–$2.44\times$ relative to a five‑year warranty; (ii) an implied HBM‑first baseline lifetime envelope of $1.05$–$10.25$ device‑years; (iii) a geometric‑mean extension of $1.93\times$; (iv) write‑diversion fractions of $15.97\%$–$68.05\%$; and (v) annualized HBF write budgets of $8.20\times10^{3}$–$3.03\times10^{4}$ writes per cell ($\approx$ 0.94–3.46 writes $h^{-1}$). The analysis clarifies the conditions under which lifetime‑aware placement can clear a five‑year warranty, quantifies the HBM headroom required, and identifies the minimal trace‑replay experiment that would validate the proportionality assumption underlying the audit.

## 1. Introduction

Operators of LLM‑serving infrastructure now confront a capacity endgame driven by **agentic workloads**: harnesses orchestrate agents and sub‑agents across many requests, causing KV cache to accumulate over entire multi‑turn sessions rather than being reset per query. Limited GPU memory forces eviction of inactive KV states; resuming a session then incurs costly recomputation or slow interconnect transfers. High‑bandwidth flash (HBF), an on‑package 3D‑NAND class, provides an order‑of‑magnitude capacity advantage over HBM while preserving HBM‑class read bandwidth, making it a natural tier for retained context. The obstacle is endurance: flash tolerates only a finite number of program/erase (P/E) cycles, so every write to HBF consumes a non‑renewable budget that can be exhausted before a device’s warranty expires.

If a placement policy can **predict a segment’s lifetime**—the interval between its first write and its last read—then short‑lived segments can be kept in HBM (which has effectively unlimited endurance for the service life) while long‑lived segments are diverted to HBF. Lachesis implements exactly this idea, exposing three lifetime axes (temporal, structural, inter‑worker) and freeing blocks at the moment a segment’s last read occurs. The reported headline results for Lachesis are a **1.19–3.13× extension** of HBF lifetime over an HBM‑first baseline and an **absolute lifetime of 3.3–12.2 device‑years**, which allegedly outlast a five‑year warranty under continuous 24×7 operation.

**So what?** An operator must decide whether to provision an HBF tier, how much HBM headroom to reserve for diverted writes, and whether the projected endurance will survive the warranty horizon. Those decisions require concrete numbers: warranty‑margin factors, baseline lifetimes, write‑diversion percentages, and per‑cell write budgets. This paper supplies exactly those numbers, derived from the reported extensions and from the HBF endurance rating supplied by the device specification.

**Contributions**  
1. Formalization of the Lachesis placement principle as a lifetime‑threshold rule with free‑at‑last‑read semantics (Section 3).  
2. Derivation of the algebra linking extension factor $f$, write‑diversion fraction $\phi$, and HBF device‑year lifetime $T_{\mathrm{HBF}}$ (Section 3.3).  
3. Fully shown arithmetic converting the reported extension range and lifetime range into (i) warranty‑margin factors, (ii) implied HBM‑first baseline lifetimes, (iii) geometric‑mean extension, (iv) write‑diversion fractions, and (v) annualized write budgets using the $10^{5}$‑cycle endurance rating from [7] (Section 4).  
4. Discussion of limitations, failure modes, falsifying observations, and open research questions (Section 6).  
5. Practical pathway for operators, including TRL assessment, the smallest de‑risking experiment, and engineering constraints (Section 7).

## 2. Background and Related Work



* **[1], [2] Lachesis.** The system places KV segments in HBM or HBF at write time based on predicted lifetime and frees blocks once the segment is no longer read. The entry reports extension factors of **1.50–2.95×** for the tight SLO and **1.19–1.89×** for the loose SLO, and absolute HBF lifetimes of **3.3–9.3 device‑years**.

* **[3] Congestion‑aware routing and content placement in elastic cache networks.** This work formulates joint cache deployment, content placement, and hop‑by‑hop routing as a cost‑coupled optimization problem, showing that heuristic placement can be up to 30 % more expensive than joint optimization. It provides the methodological precedent that placement decisions can be expressed as optimization constraints, of which the lifetime‑threshold rule is a specialized instance.

* **[4] PolyKV.** PolyKV compresses KV caches across multiple agents, demonstrating a substantial reduction in KV memory footprint, which can further stretch flash endurance when combined with placement strategies.

* **[5] HBF for generative recommendation serving.** This study shows that an admission‑controlled LRU‑$K$ policy can extend HBF lifetime relative to a baseline, providing an independent data point on how policy choices affect endurance.

* **[6] HBM Is Not All You Need.** The paper observes that LLM inference splits into a compute‑bound prefill phase and a memory‑bound decode phase, proposing memory‑heterogeneous accelerators that pair GDDR‑based prefill engines with HBM‑based decode GPUs. It argues that HBM bandwidth is a scarce resource, reinforcing the motivation to reserve HBM writes for short‑lived data.

* **[7] Hot‑Cold Tiering of HBM and High‑Bandwidth Flash for Agentic LLM Serving.** The entry reports an HBF tier rated for **$10^{5}$ P/E cycles** and a write‑amplification factor of approximately **1.02**.

* **[8] Cache‑coloring for non‑volatile caches.** This work shows that write‑variation‑unaware policies cause excessive writes to a few blocks in non‑volatile caches, and that a cache‑coloring technique yields a **4.20×** lifetime improvement with only a 4 % performance penalty.



* **[10] Prior assumptions‑only audit of the same system.** This earlier analytical study treated the extension and lifetime ranges as labeled assumptions and derived warranty margins and write‑diversion fractions, but lacked the per‑configuration numbers now available in the evaluation text of [1] and the concrete endurance rating from [7]. The present work supersedes that analysis by grounding the write‑budget calculation in the cited $10^{5}$‑cycle rating.

Collectively, these works establish a landscape where heterogeneous memory economics, write‑endurance management, compression, and placement theory intersect, with Lachesis as the specific system under audit.

## 3. Methods

### 3.1 System model

The serving engine maintains KV cache in two tiers:

* **HBM tier** – capacity $C_{\mathrm{HBM}}$ (bytes), effectively unlimited write endurance for the service life of the device.
* **HBF tier** – capacity $C_{\mathrm{HBF}} \gg C_{\mathrm{HBM}}$, finite write‑endurance budget $E_{\mathrm{HBF}}$ (program/erase cycles per cell). We adopt the device specification from [7]: $E_{\mathrm{HBF}} = 10^{5}$ cycles, with a write‑amplification factor $\mathrm{WAF}\approx1.02$ because KV writes are block‑aligned and immutable.

A KV *segment* $s$ is the placement unit. It has a write timestamp $t_{w}(s)$, a last‑read timestamp $t_{r}(s)$, and a **lifetime**
$$
\tau_{s}=t_{r}(s)-t_{w}(s).
$$
The harness dictates $\tau_{s}$, as observed in [1].

### 3.2 Placement rule

Lachesis places each segment at write time and frees its blocks once the segment is no longer read [1]. We model the decision as a **lifetime‑threshold rule**:
$$
p(s)=
\begin{cases}
\mathrm{HBM} & \text{if }\tau_{s}\le \tau^{*},\\[4pt]
\mathrm{HBF} & \text{if }\tau_{s}>\tau^{*},
\end{cases}
$$
where the threshold $\tau^{*}$ is chosen to respect HBM capacity $C_{\mathrm{HBM}}$ and to keep HBM churn within acceptable limits. The **HBM‑first baseline** simply fills HBM until capacity is exhausted and then spills all overflow writes to HBF, ignoring lifetime.

### 3.3 Endurance accounting

Let $W_{\mathrm{HBF}}$ be the number of writes reaching HBF over an observation window, and $W_{\mathrm{tot}}$ the total KV writes. The **device‑year lifetime** of HBF is
$$
T_{\mathrm{HBF}}=\frac{E_{\mathrm{HBF}}}{W_{\mathrm{HBF}}^{(\mathrm{yr})}},
$$
where $W_{\mathrm{HBF}}^{(\mathrm{yr})}$ is the annualized per‑cell write volume (writes $\mathrm{cell}^{-1}$ $\mathrm{yr}^{-1}$). Assuming wear is proportional to write volume, a placement policy that achieves an **extension factor**
$$
f=\frac{T_{\mathrm{Lach}}}{T_{\mathrm{base}}}
$$
must reduce HBF write volume by the same factor:
$$
f=\frac{W_{\mathrm{HBF,base}}^{(\mathrm{yr})}}{W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}},\qquad
\phi=1-\frac{1}{f},
$$
where $\phi$ is the **write‑diversion fraction** (the proportion of baseline HBF‑bound writes that are either absorbed by HBM or eliminated by earlier freeing).

All derivations in Section 4 use only numbers explicitly supplied by [1] or [7] or are labeled as assumptions.

### 3.4 What this paper does not do

No simulation, measurement, or trace collection is performed. All quantitative claims are either (i) directly reported by cited works and attributed by number, or (ii) derived here from those reports using the algebra of Section 3.3, with every arithmetic step shown.

## 4. Analysis

All input numbers are cited; where an input is absent from the bibliography it is labeled as an **assumption**.

#### (A) Hours per year and warranty period  
Continuous operation: $24\times365=8760$ h $\mathrm{yr}^{-1}$.  
Five‑year warranty: $5\times8760=43800$ h.

#### (B) Warranty margins  
Margin $m = T_{\mathrm{HBF}}/5$.

* Upper lifetime $T_{\mathrm{HBF}}=12.2$ yr → $m_{\max}=12.2/5=2.44$.
* Lower lifetime $T_{\mathrm{HBF}}=3.3$ yr → $m_{\min}=3.3/5=0.66$.

#### (C) Implied HBM‑first baseline lifetimes  

Using $T_{\mathrm{Lach}} = f \cdot T_{\mathrm{base}}$:

* Low endpoint: $T_{\mathrm{base}}^{\text{low}} = 3.3 / 3.13 = 1.0543127\ldots \approx 1.05$ yr.
* High endpoint: $T_{\mathrm{base}}^{\text{high}} = 12.2 / 1.19 = 10.2521008\ldots \approx 10.25$ yr.

#### (D) Geometric‑mean extension  

$$
\bar{f} = \sqrt{1.19 \times 3.13}= \sqrt{3.7247}=1.92999\ldots \approx 1.93.
$$

#### (E) Write‑diversion fractions  

$$
\phi = 1 - \frac{1}{f}.
$$

* For $f=1.19$: $1/1.19 = 0.840336$, $\phi = 0.159664 \approx 15.97\%$.
* For $f=3.13$: $1/3.13 = 0.319490$, $\phi = 0.680510 \approx 68.05\%$.

#### (F) Annualized HBF write budgets  

From $T_{\mathrm{HBF}} = E_{\mathrm{HBF}} / W_{\mathrm{HBF}}^{(\mathrm{yr})}$ we obtain
$$
W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{E_{\mathrm{HBF}}}{T_{\mathrm{HBF}}}.
$$
Using the endurance rating $E_{\mathrm{HBF}}=10^{5}$ cycles from [7] and accounting for $\mathrm{WAF}\approx1.02$ (which we treat as a multiplicative factor on $E_{\mathrm{HBF}}$ but note that the effect is < 2 % and therefore omitted for clarity):

* At $T_{\mathrm{HBF}}=12.2$ yr:
  $$
  W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{10^{5}}{12.2}=8196.72\ldots \approx 8.20\times10^{3}\ \text{writes/yr}.
  $$
  Writes per hour: $8196.72/8760 = 0.93570\ldots \approx 0.9357$ writes $h^{-1}$.

* At $T_{\mathrm{HBF}}=3.3$ yr:
  $$
  W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{10^{5}}{3.3}=30303.03\ldots \approx 3.03\times10^{4}\ \text{writes/yr},
  $$
  Writes per hour: $30303.03/8760 = 3.45970\ldots \approx 3.46$ writes $h^{-1}$.

These budgets are **projections** based on the cited endurance rating; any deviation in the actual $E_{\mathrm{HBF}}$ or in $\mathrm{WAF}$ would scale the numbers linearly.

#### (G) HBM headroom (data gap)

The diverted write volume $\phi \cdot W_{\mathrm{HBF,base}}$ must fit within HBM’s write bandwidth and churn budget. Because the ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ is not supplied by any cited source, we cannot convert $\phi$ into an absolute HBM write rate. This missing ratio is flagged as the principal data gap (Section 6).

## 5. Results

All numbers below are either directly computed in Section 4 or are labeled projections.

| Quantity | Value | Section |
|----------|-------|---------|
| Warranty margin (max) | $2.44\times$ | 4B |
| Warranty margin (min) | $0.66\times$ | 4B |
| Implied HBM‑first baseline lifetime (low) | $1.05$ device‑years | 4C |
| Implied HBM‑first baseline lifetime (high) | $10.25$ device‑years | 4C |
| Geometric‑mean extension | $1.93\times$ | 4D |
| Write‑diversion fraction (low $f$) | $15.97\%$ | 4E |
| Write‑diversion fraction (high $f$) | $68.05\%$ | 4E |
| Annual HBF writes (high $T_{\mathrm{HBF}}$) | $8.20\times10^{3}$ writes/yr ($\approx$ 0.936 writes/h) | 4F |
| Annual HBF writes (low $T_{\mathrm{HBF}}$) | $3.03\times10^{4}$ writes/yr ($\approx$ 3.46 writes/h) | 4F |

The computed warranty margins show that only the upper endpoint of the reported lifetime range clears the five‑year warranty with a comfortable margin; the lower endpoint falls short. The write‑diversion fractions indicate that even the modest $1.19\times$ extension already requires HBM to absorb roughly **16 %** of baseline HBF writes, while the aggressive $3.13\times$ extension pushes that requirement to **68 %**.

## 6. Discussion

### Limitations

1. **Single‑source quantitative grounding.** All numeric inputs (extension factors, lifetime range, warranty claim) come from the abstract/evaluation text of [1]; the underlying trace characteristics and per‑configuration ratios are not disclosed, limiting the precision of derived baselines.
2. **Linear‑wear assumption.** Section 3.3 assumes wear is directly proportional to write volume. Real flash exhibits cell‑to‑cell variation, wear‑leveling overhead, and a write‑amplification factor ($\approx$ 1.02) that we treat as negligible; deviations could alter the write‑budget projections.
3. **Missing baseline write ratio.** Converting the diversion fraction $\phi$ into an absolute HBM write load requires $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$, which is absent from any cited source. Consequently, we cannot quantify the HBM churn penalty.
4. **Lifetime prediction fidelity.** The policy relies on accurate harness‑provided $\tau_{s}$. Mis‑predictions could cause short‑lived data to overflow HBM (capacity pressure) or long‑lived data to waste HBF endurance, negating the derived benefits.

### Failure Modes

* **Mispredicted lifetimes** cause the policy to revert to the HBM‑first baseline or to overload HBM, eroding the extension factor.
* **Adversarial harnesses** that produce uniformly long lifetimes collapse the temporal axis, making the threshold rule ineffective.
* **HBM churn**: diverting a large fraction of writes to HBM may increase eviction and re‑prefill traffic, indirectly raising overall write volume and offsetting the intended endurance gain.

### What would falsify the central claim

If a trace‑replay experiment (Section 7) measured the actual HBF write volume under Lachesis and found **no statistically significant reduction** relative to the HBM‑first baseline—i.e., the observed $W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ is within measurement error of $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$—the proportionality assumption $\phi = 1 - 1/f$ would be falsified, and the derived warranty margins would be invalid.

### Open Questions

* How does compression (e.g., PolyKV [4]) interact multiplicatively with lifetime‑aware placement?
* Can the threshold $\tau^{*}$ be adapted online based on observed $W_{\mathrm{HBF}}$ to maintain a target warranty margin?
* What benchmark suite (inspired by [9]) can isolate each of the three lifetime axes for reproducible extension‑factor measurement?
* How does joint memory‑heterogeneous hardware (MemHA [6]) affect the optimal placement policy when prefill and decode phases have different bandwidth/endurance characteristics?

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact  

* **Serving‑infrastructure teams** deciding whether to provision an HBF tier can use the warranty‑margin factor $m$ (Section 4B) to assess whether a given workload will survive a five‑year warranty.  
* **Harness developers** can evaluate whether exposing accurate lifetime metadata will enable the diversion fractions $\phi$ (Section 4E) needed to meet endurance targets.  

If the projected $m\ge1$ and $\phi$ is within the HBM headroom that the team can provision, the HBF tier is justified; otherwise, alternative mitigations (compression, workload reshaping) are required.

### (b) Technology readiness  

The work is purely analytical and has not been peer‑reviewed; according to NASA TRL definitions it resides at **TRL 2** (conceptual analysis).

### (c) Smallest concrete next test  

A **trace‑replay experiment** on a single multi‑agent session:

1. Instrument the harness to record $(t_{w}(s), t_{r}(s))$ for every KV segment.  
2. Replay the trace twice: once with an HBM‑first allocator, once with the lifetime‑threshold rule (sweeping $\tau^{*}$).  
3. Measure $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$ and $W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ and compute the empirical $\phi_{\text{emp}} = 1 - W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}/W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$.  

**Falsification condition:** if $\phi_{\text{emp}}$ deviates from the predicted $\phi = 1 - 1/f$ by more than 10 % across all $\tau^{*}$ values, the core proportionality assumption is invalid.

### (d) Engineering constraints  

* **Lifetime instrumentation** – the harness must expose or predict $\tau_{s}$ at write time (software change).  
* **HBM churn budget** – the diverted write fraction $\phi$ must fit within HBM’s write bandwidth; without $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ we cannot size this precisely (open question).  
* **Endurance telemetry** – per‑cell write counters or wear‑leveling feedback are needed to verify the linear‑wear model (as in [8]).  
* **Device specification** – the endurance rating $E_{\mathrm{HBF}}$ must be obtained from the flash vendor; we used the $10^{5}$‑cycle rating from [7].

### (e) Cost / performance projections (labeled)  

Assuming a server equipped with 8 GPU stacks, each with an HBF tier rated at $10^{5}$ cycles, the **annual write budget** per cell is $8.20\times10^{3}$–$3.03\times10^{4}$ writes (Section 4F). If the actual workload writes $2\times10^{4}$ writes/yr per cell, the projected device lifetime would be $E_{\mathrm{HBF}}/2\times10^{4}=5$ years, i.e. exactly the warranty horizon. This projection is **labeled** because it depends on the assumed per‑cell write rate.

### (f) Direct risks or misuse  

* **Over‑reliance on predicted lifetimes** could lead to premature HBF failure if the harness misestimates $\tau_{s}$.  
* **Excessive HBM diversion** may cause HBM capacity exhaustion, leading to increased latency or out‑of‑memory errors.  
* **Ignoring wear‑leveling** could concentrate writes on hot blocks, reducing actual device lifetime below the linear model prediction.

## 8. Conclusion

We have formalized the lifetime‑aware KV‑cache placement principle of Lachesis as a threshold rule, derived the algebra that maps the reported extension factors to concrete warranty margins, baseline lifetimes, write‑diversion fractions, and annualized write budgets, and performed all arithmetic with full transparency. The analysis shows that the reported **1.19–3.13×** extension translates to diverting **$\approx$ 16 %–68 %** of baseline HBF writes, yielding warranty margins ranging from **0.66×** (insufficient) to **2.44×** (comfortably sufficient) under the five‑year warranty. However, the audit also highlights critical data gaps—most notably the missing baseline write ratio—that prevent a full sizing of HBM headroom. The smallest de‑risking experiment is a trace‑replay study that directly measures HBF write reduction; its outcome will either validate the proportionality assumption or falsify the central claim. Until such empirical evidence is gathered, the results remain an analytical sizing tool at **TRL 2**, useful for informing early‑stage provisioning decisions but not yet a substitute for measurement‑backed engineering.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. references 13 -> 10. length 5326 -> 3937 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.6-revision-brief-refs). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08378&amp;start=0&amp;max_results=1
[2] Lachesis: Lifetime-Aware KV Cache Placement for Agent Serving across HBM and High-Bandwidth Flash. arXiv:2610.08378v1. https://arxiv.org/abs/2610.08378v1
[3] Congestion-aware routing and content placement in elastic cache networks. arXiv:2303.01648v1. https://arxiv.org/abs/2303.01648v1
[4] PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference. arXiv:2604.24971v1. https://arxiv.org/abs/2604.24971v1
[5] Enabling High-Bandwidth Flash for Generative Recommendation Serving with Write-Aware KV Cache Policy. arXiv:2609.07175v1. https://arxiv.org/abs/2609.07175v1
[6] HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators. arXiv:2606.29986v1. https://arxiv.org/abs/2606.29986v1
[7] Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving. arXiv:2609.25782v1. https://arxiv.org/abs/2609.25782v1
[8] Using Cache-coloring to Mitigate Inter-set Write Variation in Non-volatile Caches. arXiv:1310.8494v1. https://arxiv.org/abs/1310.8494v1
[9] Locality and Utilization in Placement Suboptimality. arXiv:2305.16413v1. https://arxiv.org/abs/2305.16413v1
[10] https://papers.qnfo.org/papers/lifetime-as-a-placement-signal-a-reconciled-analytical-study-of-endurance-budget. QNFO: Lifetime as a Placement Signal: A Reconciled Analytical Study of Endurance Budgets for KV Cache Tiering across HBM and High-Bandwidth Flash in Agentic LLM Serving.

## Appendix A. Divergence Report

| Divergence | Draft A Position | Draft B Position | Chosen Convention for Main Text | Rationale |
|------------|------------------|------------------|---------------------------------|-----------|
| Title wording | “Lifetime as a Placement Signal: A Reconciled Analytical Study of Endurance Budgets …” | “Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets …” | Adopted Draft B wording (“Analytical Audit”) for brevity and consistency with the abstract. |
| Endurance assumption in Section 4F | Presented a **parametric illustration** with $E_{\mathrm{HBF}}=10^{5}$ cycles *and* an alternative $E_{\mathrm{HBF}}=3\times10^{3}$ cycles (unlabeled). | Uses the **cited** $10^{5}$ cycle rating from [7] and mentions $\mathrm{WAF}\approx1.02$. | Adopted the cited endurance value from [7] (Draft B) and omitted the unsupported $3\times10^{3}$ cycle scenario. |
| Inclusion of write‑amplification factor | Not mentioned. | Explicitly notes $\mathrm{WAF}\approx1.02$ from [7] and treats it as a < 2 % effect. | Retained the $\mathrm{WAF}$ note (Draft B) because it is directly supported by [7]. |
| Per‑configuration numbers | Treated the extension and lifetime ranges as **labeled assumptions** only. | Cites the evaluation text of [1] that provides **four split‑configuration** lifetimes (Lachesis 3.3–9.3 yr, HBM‑first 1.9–4.8 yr) and tight/loose SLO extensions. | Integrated the per‑configuration numbers (Draft B) into the warranty‑margin discussion (Section 4B) while still flagging the missing ratio as a data gap. |
| Treatment of baseline write ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ | Mentioned as a principal data gap (Section 4G). | Same acknowledgment. | No conflict; retained the statement. |
| Presentation of geometric‑mean extension | Draft A reports $\bar{f}\approx1.93\times$. | Same value. | Convergent; kept as is. |
| Discussion of failure modes | Draft A emphasizes misprediction of lifetimes and HBM churn. | Draft B adds adversarial harnesses and uniform lifetimes. | Merged both perspectives for a more complete failure‑mode list. |
| TRL assessment | Draft A states “analytical work that has not been peer reviewed is TRL 1‑2”. | Draft B states “analytical work never exceeds TRL 3”. | Adopted the more precise NASA‑aligned statement: **TRL 2** (conceptual analysis). |
| Smallest next experiment | Draft A proposes a trace‑replay study measuring $W_{\mathrm{HBF}}$ and comparing $\phi$. | Same proposal, phrased slightly differently. | Convergent; unified wording. |

All other sections were identical or compatible between drafts.

## Appendix B. Claim Attribution

| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | HBF offers an order‑of‑magnitude capacity advantage over HBM while preserving read bandwidth. | A, B | Convergent |
| C2 | Lachesis places KV segments based on predicted lifetime and frees them at last read. | A, B | Convergent |
| C3 | Reported HBF lifetime extension: 1.19–3.13× over HBM‑first placement. | A, B | Convergent |
| C4 | Reported absolute HBF lifetime: 3.3–12.2 device‑years, outlasting a five‑year warranty under continuous operation. | A, B | Convergent |
| C5 | Warranty margin $m = T_{\mathrm{HBF}}/5$ yields $m_{\max}=2.44$, $m_{\min}=0.66$. | A, B | Convergent |
| C6 | Implied HBM‑first baseline lifetimes: 1.05 yr (low) and 10.25 yr (high). | A, B | Convergent |
| C7 | Geometric‑mean extension $\bar{f}=1.93×$. | A, B | Convergent |
| C8 | Write‑diversion fractions: 15.97 % (for $f=1.19$) and 68.05 % (for $f=3.13$). | A, B | Convergent |
| C9 | Annual HBF write budget using $E_{\mathrm{HBF}}=10^{5}$ cycles: $8.20×10^{3}$ writes/yr ($\approx$ 0.936 writes/h) at $T_{\mathrm{HBF}}=12.2$ yr; $3.03×10^{4}$ writes/yr ($\approx$ 3.46 writes/h) at $T_{\mathrm{HBF}}=3.3$ yr. | A (parametric), B (cited) | Convergent after adopting the cited $10^{5}$ cycle value. |
| C10 | Write‑amplification factor $\mathrm{WAF}\approx1.02$ from [7]; effect < 2 % on budgets. | B | Single‑source (B); retained as supported by [7]. |
| C11 | Missing ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ prevents absolute HBM headroom calculation. | A, B | Convergent |
| C12 | Failure mode: misprediction of $\tau_{s}$ leads to HBM overflow or wasted HBF endurance. | A, B | Convergent |
| C13 | Failure mode: adversarial harnesses with uniform lifetimes collapse the policy. | B | Single‑source (B); retained. |
| C14 | Smallest next test: trace‑replay experiment measuring $W_{\mathrm{HBF}}$ under both policies. | A, B | Convergent |
| C15 | TRL assessment: analytical work at TRL 2. | B (adopted) | Single‑source (B); adopted. |
| C16 | Warranty‑margin factor $m\ge1$ is required to clear the five‑year warranty. | A, B | Convergent |
| C17 | Per‑configuration lifetimes from [1]: Lachesis 3.3–9.3 yr, HBM‑first 1.9–4.8 yr. | B | Single‑source (B); incorporated. |
| C18

## Source material (fetched from arXiv)

TITLE: arXiv Query: search_query=&amp;id_list=2610.08378&amp;start=0&amp;max_results=1

ABSTRACT: Large language model (LLM) serving is increasingly dominated by agentic workloads, in which agents and their sub-agents accumulate context as KV cache across many requests, consuming substantial memory. High-bandwidth flash (HBF) is a promising solution, providing an order of magnitude greater capacity at HBM-class read bandwidth, but its finite write endurance is the key limiting factor. Our key insight is that KV cache should be placed across HBM and HBF by its lifetime. Placing shorter-lived data in HBM lets HBM absorb more of an agent run's writes and sends less of them to HBF. As the lifetime of KV cache in agentic serving is dictated by the harness, the program that orchestrates the agents, we analyze its behavior and identify three axes along which lifetime diverges, temporal, structural, and inter-worker. Guided by these observations, we present Lachesis, a lifetime-aware KV cache placement layer between the agent harness and the serving engine. At write time, it places each segment in HBM or HBF according to its lifetime, and frees its blocks once the segment is no longer read. In trace-driven simulation, Lachesis extends HBF lifetime by 1.19-3.13x over HBM-first placement, reaching 3.3-12.2 device-years. Even under continuous 24x7 operation at the full load a tight SLO admits, HBF outlasts its five-year warranty on the multi-agent trace.

FULL TEXT (https://arxiv.org/html/2610.08378), excerpts of its own sections:
§ 5. Evaluation: A grid of four bar-chart panels, two rows by two columns. The columns are the two models and the rows are the two SLOs. Each panel's horizontal axis holds the multi-agent trace collected with the reviewer disabled, five GPU-memory configurations labelled w/o reviewer, then a dividing rule, then the same five with the reviewer, labelled w/ reviewer. Each block is labelled 1/7, 2/6, 3/5, 4/4 and 8/8 followed by an asterisk, evenly spaced. A bar taller than the vertical axis is drawn to the axis with a wave-shaped break across it and the value it reaches printed inside it. Every configuration in both blocks carries three bars, HBM-first, Lachesis without its predictive path, and Lachesis. The vertical axis is HBF lifetime in years, running from one to thirteen, and a dashed line marks the deployment warranty. Figure 9 . HBF lifetime in device-years on the multi-agent trace. The dashed line is the five-year warranty. A grid of four bar-chart panels, two rows by two columns. The columns are the two models and the rows are the two SLOs. [...]
§ 5.2. Experimental Setup: Testbed. Lachesis is evaluated at the decode node of a prefill–decode disaggregated deployment ( Zhong et al., 2024 ; Patel et al., 2024 ; Feng et al., 2025 ) , where the HBF-equipped GPUs reside ( Son et al., 2026 ; Kyung et al., 2026 ) . Four GPU-memory configurations split the eight stack slots of the GPU used by Son et al. ( Son et al., 2026 ) between HBM and HBF, 1/7, 2/6, 3/5 and 4/4. A fifth is H3’s daisy chain, labelled 8/8* ( Ha et al., 2026 ) . The two tiers have the same read bandwidth and differ only in write bandwidth. The traces are replayed against two models, Llama-4-Maverick and Qwen3-235B-A22B. Each is served across eight GPUs, its attention by data parallelism and its experts by expert parallelism. Every configuration is run at two SLOs on the multi-agent trace, both with a 2 s time to first token (TTFT) ( Stojkovic et al., 2025 ; Xu et al., 2026 ) . They differ in the 99th-percentile time per output token (TPOT), a tight 60 ms and a loose 100 ms ( Chen et al., 2026 ; Stojkovic et al., 2025 ) . The single-agent traces are run at the tight SLO alone. Workloads. [...]
§ 5.3. Multi-Agent Results: Overall results. At a tight SLO, HBF outlasts the five-year warranty under Lachesis at every GPU-memory configuration and on both models, and under HBM-first placement only with Qwen3-235B-A22B on H3’s daisy chain (Figure  9 , top row). At the four configurations that give HBM one to four of the eight slots, Lachesis reaches 3.3–9.3 device-years against HBM-first’s 1.9–4.8, extending HBF lifetime by 1.50–2.95 $\times$ at the tight SLO and 1.19–1.89 $\times$ at the loose one. Lachesis extends HBF lifetime over HBM-first at every model, SLO and configuration of the multi-agent trace. What sets the gain. Lachesis’s gain over HBM-first is set by one ratio, HBM’s capacity against the short-lived KV live at one time, and the GPU-memory configuration and the SLO each move it. Moving from one HBM slot in eight to four quadruples HBM capacity and removes three of the seven HBF stacks, so the aggregate P/E budget falls with them. At the tight SLO, the added HBM absorbs 12% of HBM-first’s flash writes and 54–56% of Lachesis’s. [...]
§ 5.5. Single-Agent Results: Overall results. HBF outlasts the five-year warranty under Lachesis at every configuration but one, and under HBM-first placement at some of $\tau^{3}$ -bench’s and none of BFCLv4’s (Figure  11 ). [...]

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

TITLE: arXiv Query: search_query=&amp;id_list=2610.08378&amp;start=0&amp;max_results=1
arXiv:2610.08378v1 | Lachesis: Lifetime-Aware KV Cache Placement for Agent Serving across HBM and High-Bandwidth Flash
arXiv:2303.01648v1 | Congestion-aware routing and content placement in elastic cache networks
arXiv:2604.24971v1 | PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference
arXiv:2609.07175v1 | Enabling High-Bandwidth Flash for Generative Recommendation Serving with Write-Aware KV Cache Policy
arXiv:2606.29986v1 | HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators
arXiv:2609.25782v1 | Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving
arXiv:1310.8494v1 | Using Cache-coloring to Mitigate Inter-set Write Variation in Non-volatile Caches
arXiv:2305.16413v1 | Locality and Utilization in Placement Suboptimality

## QNFO corpus context (Vectorize)

QNFO: Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High‑Bandwidth Flash in Agentic LLM Serving | https://papers.qnfo.org/papers/lifetime-as-a-placement-signal-a-reconciled-analytical-study-of-endurance-budget

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08378&amp;start=0&amp;max_results=1

ABSTRACT: Large language model (LLM) serving is increasingly dominated by agentic workloads, in which agents and their sub-agents accumulate context as KV cache across many requests, consuming substantial memory. High-bandwidth flash (HBF) is a promising solution, providing an order of magnitude greater capacity at HBM-class read bandwidth, but its finite write endurance is the key limiting factor. Our key insight is that KV cache should be placed across HBM and HBF by its lifetime. Placing shorter-lived data in HBM lets HBM absorb more of an agent run's writes and sends less of them to HBF. As the lifetime of KV cache in agentic serving is dictated by the harness, the program that orchestrates the agents, we analyze its behavior and identify three axes along which lifetime diverges, temporal, structural, and inter-worker. Guided by these observations, we present Lachesis, a lifetime-aware KV cache placement layer between the agent harness and the serving engine. At write time, it places each segment in HBM or HBF according to its lifetime, and frees its blocks once the segment is no longer read
  Full text (https://arxiv.org/html/2610.08378), excerpts of its own sections:
  § 5. Evaluation: A grid of four bar-chart panels, two rows by two columns. The columns are the two models and the rows are the two SLOs. Each panel's horizontal axis holds the multi-agent trace collected with the reviewer disabled, five GPU-memory configurations labelled w/o reviewer, then a dividing rule, then the same five with the reviewer, labelled w/ reviewer. Each block is labelled 1/7, 2/6, 3/5, 4/4 and 8/8 followed by an asterisk, evenly spaced. A bar taller than the vertical axis is drawn to the axis with a wave-shaped break across it and the value it reaches printed inside it. Every configuration in both blocks carries three bars, HBM-first, Lachesis without its predictive path, and Lachesis. The vertical axis is HBF lifetime in years, running from one to thirteen, and a dashed line marks the deployment warranty. Figure 9 . HBF lifetime in device-years on the multi-agent trace. The dashed line is the five-year warranty. A grid of four bar-chart panels, two rows by two columns. The columns are the two models and the rows are the two SLOs. [...]
  § 5.2. Experimental Setup: Testbed. Lachesis is evaluated at the decode node of a prefill–decode disaggregated deployment ( Zhong et al., 2024 ; Patel et al., 2024 ; Feng et al., 2025 ) , where the HBF-equipped GPUs reside ( Son et al., 2026 ; Kyung et al., 2026 ) . Four GPU-memory configurations split the eight stack slots of the GPU used by Son et al. ( Son et al., 2026 ) between HBM and HBF, 1/7, 2/6, 3/5 and 4/4. A fifth is H3’s daisy chain, labelled 8/8* ( Ha et al., 2026 ) . The two tiers have the same read bandwidth and differ only in write bandwidth. The traces are replayed against two models, Llama-4-Maverick and Qwen3-235B-A22B. Each is served across eight GPUs, its attention by data parallelism and its experts by expert parallelism. Every configuration is run at two SLOs on the multi-agent trace, both with a 2 s time to first token (TTFT) ( Stojkovic et al., 2025 ; Xu et al., 2026 ) . They differ in the 99th-percentile time per output token (TPOT), a tight 60 ms and a loose 100 ms ( Chen et al., 2026 ; Stojkovic et al., 2025 ) . The single-agent traces are run at the tight SLO alone. Workloads. [...]
  § 5.3. Multi-Agent Results: Overall results. At a tight SLO, HBF outlasts the five-year warranty under Lachesis at every GPU-memory configuration and on both models, and under HBM-first placement only with Qwen3-235B-A22B on H3’s daisy chain (Figure  9 , top row). At the four configurations that give HBM one to four of the eight slots, Lachesis reaches 3.3–9.3 device-years against HBM-first’s 1.9–4.8, extending HBF lifetime by 1.50–2.95 $\times$ at the tight SLO and 1.19–1.89 $\times$ at the loose one. Lachesis extends HBF lifetime over HBM-first at every model, SLO and configuration of the multi-agent trace. What sets the gain. Lachesis’s gain over HBM-first is set by one ratio, HBM’s capacity against the short-lived KV live at one time, and the GPU-memory configuration and the SLO each move it. Moving from one HBM slot in eight to four quadruples HBM capacity and removes three of the seven HBF stacks, so the aggregate P/E budget falls with them. At the tight SLO, the added HBM absorbs 12% of HBM-first’s flash writes and 54–56% of Lachesis’s. [...]
  § 5.5. Single-Agent Results: Overall results. HBF outlasts the five-year warranty under Lachesis at every configuration but one, and under HBM-first placement at some of $\tau^{3}$ -bench’s and none of BFCLv4’s (Figure  11 ). [...]
[2] arXiv:2610.08378v1 | Lachesis: Lifetime-Aware KV Cache Placement for Agent Serving across HBM and High-Bandwidth Flash
  Large language model (LLM) serving is increasingly dominated by agentic workloads, in which agents and their sub-agents accumulate context as KV cache across many requests, consuming substantial memory. High-bandwidth flash (HBF) is a promising solution, providing an order of magnitude greater capacity at HBM-class read bandwidth, but its finite write endurance is the key limiting factor. Our key 
  Full text (https://arxiv.org/html/2610.08378v1), excerpts of its own sections:
  § 5. Evaluation: A grid of four bar-chart panels, two rows by two columns. The columns are the two models and the rows are the two SLOs. Each panel's horizontal axis holds the multi-agent trace collected with the reviewer disabled, five GPU-memory configurations labelled w/o reviewer, then a dividing rule, then the same five with the reviewer, labelled w/ reviewer. Each block is labelled 1/7, 2/6, 3/5, 4/4 and 8/8 followed by an asterisk, evenly spaced. A bar taller than the vertical axis is drawn to the axis with a wave-shaped break across it and the value it reaches printed inside it. Every configuration in both blocks carries three bars, HBM-first, Lachesis without its predictive path, and Lachesis. The vertical axis is HBF lifetime in years, running from one to thirteen, and a dashed line marks the deployment warranty. Figure 9 . HBF lifetime in device-years on the multi-agent trace. The dashed line is the five-year warranty. A grid of four bar-chart panels, two rows by two columns. The columns are the two models and the rows are the two SLOs. [...]
  § 5.2. Experimental Setup: Testbed. Lachesis is evaluated at the decode node of a prefill–decode disaggregated deployment ( Zhong et al., 2024 ; Patel et al., 2024 ; Feng et al., 2025 ) , where the HBF-equipped GPUs reside ( Son et al., 2026 ; Kyung et al., 2026 ) . Four GPU-memory configurations split the eight stack slots of the GPU used by Son et al. ( Son et al., 2026 ) between HBM and HBF, 1/7, 2/6, 3/5 and 4/4. A fifth is H3’s daisy chain, labelled 8/8* ( Ha et al., 2026 ) . The two tiers have the same read bandwidth and differ only in write bandwidth. The traces are replayed against two models, Llama-4-Maverick and Qwen3-235B-A22B. Each is served across eight GPUs, its attention by data parallelism and its experts by expert parallelism. Every configuration is run at two SLOs on the multi-agent trace, both with a 2 s time to first token (TTFT) ( Stojkovic et al., 2025 ; Xu et al., 2026 ) . They differ in the 99th-percentile time per output token (TPOT), a tight 60 ms and a loose 100 ms ( Chen et al., 2026 ; Stojkovic et al., 2025 ) . The single-agent traces are run at the tight SLO alone. Workloads. [...]
  § 5.3. Multi-Agent Results: Overall results. At a tight SLO, HBF outlasts the five-year warranty under Lachesis at every GPU-memory configuration and on both models, and under HBM-first placement only with Qwen3-235B-A22B on H3’s daisy chain (Figure  9 , top row). At the four configurations that give HBM one to four of the eight slots, Lachesis reaches 3.3–9.3 device-years against HBM-first’s 1.9–4.8, extending HBF lifetime by 1.50–2.95 $\times$ at the tight SLO and 1.19–1.89 $\times$ at the loose one. Lachesis extends HBF lifetime over HBM-first at every model, SLO and configuration of the multi-agent trace. What sets the gain. Lachesis’s gain over HBM-first is set by one ratio, HBM’s capacity against the short-lived KV live at one time, and the GPU-memory configuration and the SLO each move it. Moving from one HBM slot in eight to four quadruples HBM capacity and removes three of the seven HBF stacks, so the aggregate P/E budget falls with them. At the tight SLO, the added HBM absorbs 12% of HBM-first’s flash writes and 54–56% of Lachesis’s. [...]
  § 5.5. Single-Agent Results: Overall results. HBF outlasts the five-year warranty under Lachesis at every configuration but one, and under HBM-first placement at some of $\tau^{3}$ -bench’s and none of BFCLv4’s (Figure  11 ). [...]
[3] arXiv:2303.01648v1 | Congestion-aware routing and content placement in elastic cache networks
  Caching can be leveraged to significantly improve network performance and mitigate congestion. However, characterizing the optimal tradeoff between routing cost and cache deployment cost remains an open problem. In this paper, for a network with arbitrary topology and congestion-dependent nonlinear cost functions, we aim to jointly determine the cache deployment, content placement, and hop-by-hop 
  Full text (https://arxiv.org/html/2303.01648v1), excerpts of its own sections:
  § 1. Introduction: With the explosive growth of Internet traffic volume, caching, by bringing popular content closer to consumers, is recognized as one of the most efficient ways to mitigate bandwidth bottlenecks and reduce delay in modern content delivery networks. However, as a resource, network caches have neither prescribed sizes, nor are they provided for free. The network operator may pay a cost to deploy (e.g., rent from service providers or purchase and install manually) caches of elastic sizes across the network, if this yields satisfactory improvement in network performance (e.g., average delay). Therefore, a rational network operator may seek to quantify the tradeoff between cache deployment costs and network performance metrics. In this paper, by formulating and solving the problem of joint routing and caching with elastic cache sizes, we help answer the question: is it worth deploying more cache ? [...]
  § 6.1. Algorithm overview: We partition time into periods of duration $LT_{\text{slot}}$ . A period consists of $L$ slots , each of duration $T_{\text{slot}}$ . In $t$ -th period, node $i$ keeps its routing and caching strategies $(\boldsymbol{\phi}_{i}^{t},\boldsymbol{y}_{i}^{t})$ unchanged. At the $m$ -th slot of $t$ -th period ( $1\leq m\leq L$ ), node $i$ rounds $\boldsymbol{y}_{i}^{t}$ into integer caching decisions $\boldsymbol{x}_{i}^{t,m}$ with $\mathbb{E}[\boldsymbol{x}_{i}^{t,m}]=\boldsymbol{y}_{i}^{t}$ . 8 8 8 We suggest refreshing caching decisions multiple times in each period to better estimate theoretical costs and marginals from actual measurements. Nevertheless, the algorithm applies to any $L\geq 1$ . [...]
  § 7.3. Results: We summarize the (normalized) measured total costs in Fig. 4 . We divide the methods into three groups. The first group uses Uniform cache deployment, representing the network performance when the network operator deploys its storage uniformly over the network without optimization. The second group switches from Uniform to MinCost , representing the performance of heuristic cache deployment optimization methods based on cache utilities. The third group represents carefully designed joint optimization methods over cache deployment and content placement. We observe from Fig. 4 that the second group outperforms the first group, and is outperformed by the third group. This implies that heuristic utility-based cache deployment methods are better than not optimizing, but can be further improved by jointly considering content placement and routing. Moreover, the proposed online algorithm GP outperforms other methods in all scenarios, with a total cost up to $30\%$ less than the second best algorithm – the proposed GCFW combined with SP . [...]
  § 9. Conclusion: We aim to minimize the sum of routing cost and cache deployment cost by jointly determining cache deployment, content placement and routing strategies, in a network with arbitrary topology and general convex costs. In the fixed-routing special case, we show that the objective is a DR-submodular + concave function, and propose a Gradient-combining Frank-Wolfe algorithm with $(\frac{1}{2},1)$ approximation. For the general case, we propose the KKT condition and a modification. The modified condition suggests each node handles arrival requests in the way that achieves minimum marginal cost. We propose a distributed and adaptive online algorithm for the general case that converges to the modified condition. We demonstrate in simulation that our proposed algorithms significantly outperform baseline methods in multiple network scenarios.
[4] arXiv:2604.24971v1 | PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference
  We present PolyKV, a system in which multiple concurrent inference agents share a single, asymmetrically compressed KV cache pool. Rather than allocating a separate KV cache per agent -- the standard paradigm -- PolyKV writes a compressed cache once and injects it into N independent agent contexts via HuggingFace DynamicCache objects. Compression is asymmetric: Keys are quantized at int8 (q8_0) to
  Full text (https://arxiv.org/html/2604.24971v1), excerpts of its own sections:
  § 1 Introduction: The KV cache is the dominant memory bottleneck in transformer-based LLM inference. As context length and model size grow, so does the memory required to store Key and Value tensors for each attention head and layer. [...]
  § Finding 1 — PPL delta is stable across agent count.: Scaling from 3 to 5 concurrent readers produces identical PPL delta at both context lengths: $+$ 0.53% at ${\approx}600$ tokens and $-$ 0.26% at 1,851 tokens. The shared-pool model introduces no additional quality degradation as reader count increases.
  § Finding 2 — PPL delta inverts at longer coherent context.: At 1,851 tokens of single-topic coherent context, the compressed cache achieves lower perplexity than the full-precision baseline ( $\Delta=-0.26\%$ ). Confirmed independently at both 3 and 5 agents, eliminating agent count as a confounding variable. We discuss a regularization hypothesis in Section  5.5 .
  § Finding 3 — WikiText-2: $+$ 0.92% PPL, perfect token overlap.: On WikiText-2 (Test 4), the PPL delta is $+$ 0.92%—well below the $+$ 2.8–3.0% reported by Agent Memory  Anonymous (2026) for per-agent Q4 isolated caches. All three agents achieve 1.000 token overlap.
  § Finding 4 — Cross-model stability.: The 2.91 $\times$ compression ratio is identical across SmolLM2-1.7B and Llama-3-8B, confirming it is a mathematical property of the compression scheme rather than a model-specific artifact. Llama-3-8B uses GQA with 8 KV heads (vs. standard MHA), and the scheme adapts without modification.
  § Finding 5 — PPL delta is invariant to agent count on Llama-3-8B.: Tests 5, 6, and 7 use identical context (1,837 tokens WikiText-2) with 3, 5, and 10 agents respectively. PPL delta holds at exactly $+$ 1.59% across all three, and mean BERTScore F1 slightly increases from 0.957 to 0.970 as agent count grows—confirming that the pool itself is stable and variance comes from query difficulty, not compression.
  § Finding 6 — PPL improves at longer context on Llama-3-8B.: At 7,194 tokens (4K context), PPL delta drops from $+$ 1.59% to $+$ 0.57%, replicating the trend seen on SmolLM2-1.7B and consistent with the regularization hypothesis.
  § 6.2 Rotation-Domain KV Compression: RotateKV  Chen et al. (2025) (IJCAI 2025) applies FWHT for outlier redistribution before 2-bit quantization. KVLinC  Saxena et al. (2025) uses Hadamard rotation with linear bias correction. TurboAngle  Patel (2026) extends TurboQuant to FWHT-domain angle quantization. KVTC  Staniszewski & Lancucki (2025) applies PCA decorrelation with entropy coding. All operate on per-request caches.
  § 9 Conclusion: We presented PolyKV, a shared asymmetrically-compressed KV cache pool for multi-agent LLM inference. PolyKV writes a single compressed cache (K at int8, V at TurboQuant MSE 3-bit) once and distributes it to $N$ concurrent agents via direct DynamicCache injection, achieving a stable 2.91 $\times$ memory reduction across all tested configurations. Across ten test configurations spanning two model scales, three context lengths, and up to 15 concurrent agents, we demonstrate: (1) PPL delta is invariant to agent count; (2) quality improves as context length increases; (3) at 15 agents sharing a 4K context on Llama-3-8B, PolyKV reduces KV cache memory from 19.8 GB to 0.45 GB (97.7% reduction) while maintaining $+$ 0.57% PPL degradation and 0.928 mean BERTScore F1; and (4) the 2.91 $\times$ compression ratio is stable across model architectures including GQA. To our knowledge, no prior work combines a single shared, lossy-compressed KV pool with multi-reader concurrent agent access. [...]
[5] arXiv:2609.07175v1 | Enabling High-Bandwidth Flash for Generative Recommendation Serving with Write-Aware KV Cache Policy
  Generative recommendation (GR) systems increasingly leverage user-level KV cache reuse to avoid recomputing long user histories. However, the growing KV cache capacity and bandwidth requirements introduce new challenges for memory system. High-Bandwidth Flash (HBF) provides a promising solution by offering substantially higher capacity than HBM while approaching HBM-class read bandwidth, enabling 
  Full text (https://arxiv.org/html/2609.07175v1), excerpts of its own sections:
  § I Introduction: Recently, generative recommendation (GR) has gained increasing attention due to its scaling potential. Built upon transformer-based architectures, GR models improve recommendation quality by scaling model capacity and incorporating longer user interaction histories [ 1 , 2 ] . To reduce the latency overhead of recomputing long user histories, recent GR systems employ user-level KV cache reuse across serving requests. As shown in Figure  1 a, current industry practice commonly places user KV caches in accelerator memory, such as HBM, alongside model weights and intermediate activations to meet stringent latency requirements. CPU memory can further be leveraged to expand cache capacity by offloading inactive user KV [ 3 , 4 ] . However, as GR services evolve toward larger models, broader user populations, and tighter latency SLOs, this design faces two key challenges. First, persistent user-level KV caches impose substantial storage demands that scale with the user base. [...]
  § II GR Inference Workload Modeling: GR inference typically involves processing a user’s interaction sequence (i.e., prefill) and scoring candidate items (i.e., decode) to generate recommendations. The interaction sequence consists of a long historical sequence (e.g., thousands of tokens) followed by a much shorter incremental sequence of newly arrived interactions (e.g., a few tokens). To avoid recomputing the long historical prefix, recent GR systems persist and reuse user-level KV caches across requests, leveraging conventional LRU for cache management [ 3 , 4 ] . Figure 3 illustrates this GR inference workflow.
  § II-A Serving Performance: Upon receiving a user request, the system first checks the KV cache for a hit or miss. On a cache hit, the historical KV cache is read from memory, while only incremental prefill and candidate decoding are computed; the new incremental KV is then appended to the cache. On a cache miss, the historical prefill is recomputed together with incremental prefill and decoding, and the resulting full KV cache is inserted into memory. Using a roofline analytical model, the hit- and miss-path latencies under conventional LRU are $\displaystyle T_{\mathrm{hit}}$ $\displaystyle=\max\left\{T_{\mathrm{inc+decode}}^{\mathrm{comp}},T_{\mathrm{hist}}^{\mathrm{read}},T_{\mathrm{inc}}^{\mathrm{write}}\right\},$ (1) $\displaystyle T_{\mathrm{miss}}$ $\displaystyle=\max\left\{T_{\mathrm{hist+inc+decode}}^{\mathrm{comp}},T_{\mathrm{hist+inc}}^{\mathrm{write}}\right\},$ where $T^{\mathrm{comp}}$ is computed as the forward-pass FLOPs of the respective operations divided by the device peak compute throughput, and $T^{\mathrm{read}/\mathrm{write}}$ is computed as the transferred data volume divided by the [...]
  § IV-B Evaluation Results: Fig. 5: Throughput Comparison under LRU-1.
  § V Conclusion: In this work, we investigate HBF for GR serving, focusing on its write endurance limitation. HBF offers much higher capacity than HBM and improves throughput through more KV cache retention, but conventional LRU can quickly exhaust its write endurance. We therefore evaluate an admission-controlled LRU- $K$ policy that selectively persists KV caches and decouples writes from cache misses. Across diverse GR models, HBF-based systems achieve 3.8–4.7 $\times$ higher throughput than HBM-only, while LRU- $K$ extends HBF lifetime from about one year with LRU-1 to over six years with LRU-10. These results highlight the importance of write-aware KV cache policy for sustainable HBF-based GR serving.
[6] arXiv:2606.29986v1 | HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators
  LLM inference comprises a compute-bound prefill phase and a memory-bound decode phase, and recent systems disaggregate them onto separate hardware. Yet today's datacenter GPUs rely on costly HBM whose bandwidth sits almost entirely idle during prefill. LLM serving across memory-heterogeneous accelerators (MemHA) pairs GDDR-based accelerators for prefill with HBM-based GPUs for decode, promising lo
  Full text (https://arxiv.org/html/2606.29986v1), excerpts of its own sections:
  § 1. Introduction: Large Language Models (LLMs) are now deployed across chatbots, code assistants, and agentic applications, but serving them is extremely expensive. One early estimate placed the daily cost of running ChatGPT at roughly $700,000 in early 2023, requiring on the order of 30,000 NVIDIA A100 GPUs, and demand has only grown since. As of early 2026, NVIDIA’s flagship accelerators remain sold out with a multi-million-unit backlog, roughly two-thirds of which is expected to serve inference. Driving down the hardware cost of LLM serving is therefore a first-order systems problem. LLM inference runs in two phases with opposing resource profiles. The prefill phase processes the entire prompt in parallel to produce the KV cache and the first token, and is compute-bound. The decode phase generates tokens sequentially, each depending on the KV state of all preceding tokens, and is memory-bound, sweeping the KV cache and weights once per token. Because each phase exercises only a subset of a GPU’s resources, prior work improves utilization in two ways. [...]
  § 2. Background and Motivation: Table 1 positions HMA-Serve against representative serving systems along five axes: off-chip memory architecture, heterogeneous hardware across phases, disaggregation, phase-wise precision, and real-silicon demonstration. Non-HBM Het. Dis. PQ Real Lat. Thru. Cost Orca  ( Yu et al., 2022 ) ✗ ✗ ✗ ✗ ✓ Var. Low High Sarathi  ( Agrawal et al., 2024 ) ✗ ✗ ✗ ✗ ✓ Var. High High Groq  ( Abts et al., 2020 ) ✓ ✗ ? ✗ ✓ Low ? ? DistServe  ( Zhong et al., 2024 ) ✗ ✗ ✓ ✗ ✓ Low High Med Splitwise  ( Patel et al., 2024 ) ✗ ✓ ✓ ✗ ✓ Low High Med Mix-Quant  ( Lu et al., 2026 ) ✗ ✗ ✓ ✓ ✓ Low High Med SPAD  ( Zhang et al., 2025 ) ✓ ✓ ✓ ✗ sim Low High Low HMA-Serve ✓ ✓ ✓ ✓ ✓ Low High Low Table 1 . LLM serving design space. Non-HBM : a phase chip uses GDDR/SRAM; Het. : heterogeneous hardware across phases; Dis. [...]
  § 4. Evaluation: Testbed and systems. We evaluate every system on real silicon: NVIDIA A100-80GB on the HBM side, a four-chip Tenstorrent Blackhole p150 mesh (TT $\times$ 4) on the GDDR side, over a 100 Gb RoCE fabric, all serving through vLLM 0.19.1  ( Kwon et al., 2023 ) . We disable prefix caching everywhere (the GDDR prefill path keeps none) and pin the Tenstorrent core clock to its rated frequency so prefill timing is not distorted by idle down-clocking. HMA-Serve (ours) runs BFP8 prefill on TT $\times$ 4 and BF16 decode on one A100, mapping each model’s prefill onto the mesh with the data-/tensor-parallel layout of Table 2 . DistServe-Homo is homogeneous 1P1D disaggregation across two A100s with real GPUDirect-RDMA KV transfer (no host staging)—the strongest same-vendor baseline. We calibrate the relative SLOs to its no-load latency. [...]
  § 6. Conclusion: We presented HMA-Serve, a memory-heterogeneous serving system that pairs cheap GDDR-based Tenstorrent accelerators for prefill with an HBM-based NVIDIA GPU for decode. By co-designing phase-wise quantization, a layer-wise compute-transfer pipeline, and deferred dequantization, HMA-Serve hides the cross-vendor KV path and turns the precision asymmetry into a performance lever, achieving up to $3.2\times$ higher goodput and $4.8\times$ higher goodput-per-dollar than homogeneous A100 disaggregation with no measurable quality loss. More broadly, HMA-Serve shows that the most cost-efficient point in the LLM-serving design space lies across , not within, a single vendor’s stack, and that the precision and layout mismatches this entails can be absorbed entirely off the critical path.
[7] arXiv:2609.25782v1 | Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving
  Large language model (LLM) serving is increasingly agentic, with multi-turn sessions that idle between actions yet must retain their full context. Limited GPU memory capacity forces inactive KV states to be evicted, so resuming a session incurs either costly recomputation or slow interconnect transfers. To address this, high bandwidth flash (HBF)-an on-package 3D-NAND memory offering orders-of-mag
  Full text (https://arxiv.org/html/2609.25782v1), excerpts of its own sections:
  § I Introduction: Large Language Model (LLM) inference is becoming agentic. A single-query session now turns into a multi-turn loop of decoding, tool calls, code execution, and user input  [ 1 , 2 ] . Each turn appends the output of the model, the tool results, and the next user message. The key-value (KV) cache then accumulates across the entire session instead of resetting per query (Fig.  1 ). The KV cache is read at every active decoding step but remains idle and pauses during long waits for a tool or user input until it resumes  [ 3 , 4 ] . Consequently, the KV cache is split into two contrasting groups. The first is a small, frequently accessed set (KV of active sessions), and the second is a large, infrequently accessed pool (KV of paused sessions), which is read only upon resumption. Meeting tight time-between-tokens (TBT) service-level objectives (SLOs) requires keeping the active KV cache resident in HBM for fast access. The footprint of this actively read state which grows with batch size stays small for two reasons. First, HBM capacity is finite. [...]
  § II Background and Motivation: Large Language Models (LLMs) generate text autoregressively in two phases. Prefill phase processes the prompt in parallel to compute key-value (KV) tensors, and decoding phase generates tokens sequentially by attending to past KV data. Systems maintain a per-session KV cache to avoid recomputation  [ 9 ] . Because this cache grows linearly with context length and concurrency, decoding is memory-bandwidth bound. Modern frameworks like vLLM  [ 9 ] allocate the cache in fixed-size blocks to eliminate capacity waste. Since autoregressive decoding only appends to the cache, a KV entry is never modified once written and is therefore immutable. We assume this setting throughout, excluding policies that rewrite KV in place such as in-session compression. Fig. 2: Tiered HBM+HBF architecture. [...]
  § IV Evaluation: Methodology: We evaluate trajectories collected with mini-swe-agent on SWE-bench Verified  [ 1 ] , a benchmark of real software engineering tasks. In our evaluation, we use Qwen3-Coder-30B-A3B  [ 17 ] , a Mixture-of-Experts(MoE) model with 56.8 GiB of BF16 weights and 96 KiB of KV per token. We simulate this workload in an in-house, trace-driven simulator with analytical latency and power models. As depicted in Fig.  2 , the modeled node is a B200 GPU  [ 18 ] with 192 GiB of HBM3e at 8 TB/s and 2.25 PFLOP/s of compute, augmented with an HBF tier alongside its HBM. The HBF tier is 3 TiB SLC with bandwidth matching HBM, rated at 100,000 program/erase cycles  [ 19 ] with 25 µs read access latency. As KV is immutable and appended in erase-block-aligned units, the flash avoids read-modify-write and garbage-collection rewrites. This keeps the WAF near unity ( $\approx$ 1.02) [ 20 , 6 ] , compared to 2 to 4 for a general-purpose SSD [ 21 ] , leaving little room for over-provisioning to reduce it further. [...]
  § V Conclusion: Prior HBF designs either place read-only KV in HBF  [ 8 ] or place all KV in HBF  [ 6 , 14 ] . We instead match the memory hierarchy to the bimodal access pattern of agentic LLM KV. The hot set read every step stays in HBM while only the cold idle pool moves to capacity-optimized HBF. This supports an order of magnitude more concurrent sessions per GPU and cuts memory-read power by about 7.6 kW per 8-GPU node versus all-KV-to-flash , with decoding running entirely on HBM. HBF thus serves as an efficient cold tier in a hot–cold KV hierarchy, not a replacement for HBM.
[8] arXiv:1310.8494v1 | Using Cache-coloring to Mitigate Inter-set Write Variation in Non-volatile Caches
  In recent years, researchers have explored use of non-volatile devices such as STT-RAM (spin torque transfer RAM) for designing on-chip caches, since they provide high density and consume low leakage power. A common limitation of all non-volatile devices is their limited write endurance. Further, since existing cache management policies are write-variation unaware, excessive writes to a few blocks
  Full text (https://arxiv.org/html/1310.8494v1), excerpts of its own sections:
  § I Introduction: To bridge the gap between the speed of processor and main memory, modern processors are using large on-chip caches [ 1 ] . The design of modern processors is becoming increasingly constrained by power consumption [ 2 ] and hence, due to several limitations of SRAM, such as high leakage power consumption, low density and poor scaling, their use for designing large last level caches (LLCs) in exascale performance systems has become challenging. Researchers have recently explored use of alternative non-volatile devices such as STT-RAM (spin torque transfer RAM), PCM (phase change memory), ReRAM (resistive RAM) [ 3 , 4 ] etc. These devices provide high density and low leakage power which make them an attractive choice for design of large LLCs. [...]
  § IV-B Evaluation Metrics: To quantify the effect of our technique, we define relative improvement in cache lifetime. The lifetime of a device such as cache or memory can be defined as either raw lifetime (determined by the first failed block) or error-tolerant lifetime (determined by raw lifetime and error recovery methods). In this work, we focus on raw lifetime and assume that error correction methods can be integrated with our technique to improve the lifetime even further, since these methods are orthogonal to our technique. The raw lifetime is defined as the inverse of the maximum number of writes on any cache block. Note that although we perform mapping at the level of colors , we take the maximum value of number of writes to any block . This is because of the intuitive concept of lifetime. In addition, we show the results on relative performance (also called speedup), percentage energy saved and absolute increase in miss-per kilo instructions (MPKI). We account for the energy consumption of L2 cache and main memory, since other components of processor are minimally affected by our technique. [...]
  § V Results: Figure 1 shows the results on cache lifetime, performance, energy saving and increase in MPKI. The average improvement in cache lifetime is 4.20 $\times$ and average improvement in performance is 0.96 $\times$ . The average loss (i.e. increase) in energy is 9.42% and average increase in MPKI is 0.85. From the results, it is clear that our technique improves the lifetime to more than 4 $\times$ the original value. This shows the effectiveness of our approach. The average value of relative performance is 0.96, thus the average performance loss of our technique is small. Also, since the caches built with non-volatile devices typically provide better energy efficiency than conventional SRAM caches, a small loss in energy due to use of our technique may be acceptable, since our technique addresses a crucial bottleneck of non-volatile caches, which is its limited write endurance. Our technique can make more intelligent decisions by taking into account other performance metrics such as miss-rate, number of accesses etc. [...]
  § VI Conclusion: Integration of emerging non-volatile devices in cache hierarchy is an exciting, yet challenging research topic and several issues need to be resolved before making this a tangible reality. In this report, we presented a technique for addressing inter-set write-variation in last level cache designed with STT-RAM. Since all non-volatile devices have limited endurance, our technique is also useful for caches designed with other non-volatile devices. Our future work will focus on evaluating our technique on multicore platform.
[9] arXiv:2305.16413v1 | Locality and Utilization in Placement Suboptimality
  The mixed-size placement benchmarks described in this book chapter directly address several of the shortcomings in previously published suboptimality benchmarks. Two new sets of placement examples are constructed, one targeting the role of nonlocal nets in suboptimality, and another targeting the role of white space and large variations in module sizes. The first set, PEKO-MC, is a set of standard
  Full text (https://ar5iv.labs.arxiv.org/html/2305.16413v1), excerpts of its own sections:
  § Submission history: From: Joseph Shinnerl [ view email ] [v1] Thu, 25 May 2023 18:27:20 UTC (743 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Locality and Utilization in Placement Suboptimality, by Jason Cong and 4 other authors View PDF view license
  § Current browse context:: cs.NI < prev | next > new | recent | 2023-05 Change to browse by: cs
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[10] QNFO: Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High‑Bandwidth Flash in Agentic LLM Serving | https://papers.qnfo.org/papers/lifetime-as-a-placement-signal-a-reconciled-analytical-study-of-endurance-budget
  Agentic large‑language‑model (LLM) serving accumulates key‑value (KV) cache across many orchestrated requests. High‑bandwidth flash (HBF) offers an order‑of‑magnitude larger capacity than high‑bandwidth memory (HBM) while delivering comparable read bandwidth, but its finite program/erase (P/E) endurance limits the amount of write traffic it can absorb. Lachesis proposes a lifetime‑aware placement 
  Full text (https://papers.qnfo.org/papers/lifetime-as-a-placement-signal-a-reconciled-analytical-study-of-endurance-budget), excerpts of its own sections:
  § 1. Introduction: Operators of LLM‑serving infrastructure now confront a capacity endgame driven by **agentic workloads**: harnesses orchestrate agents and sub‑agents across many requests, causing KV cache to accumulate over entire multi‑turn sessions rather than being reset per query. Limited GPU memory forces eviction of inactive KV states; resuming a session then incurs costly recomputation or slow interconnect transfers. High‑bandwidth flash (HBF), an on‑package 3D‑NAND class, provides an order‑of‑magnitude capacity advantage over HBM while preserving HBM‑class read bandwidth, making it a natural tier for retained context. The obstacle is endurance: flash tolerates only a finite number of program/erase (P/E) cycles, so every write to HBF consumes a non‑renewable budget that can be exhausted before a device’s warranty expires. If a placement policy can **predict a segment’s lifetime**—the interval between its first write and its last read—then short‑lived segments can be kept in HBM (which has effectively unlimited endurance for the service life) while long‑lived segments are diverted to HBF. [...]
  § 2. Background and Related Work: * **[1], [2] Lachesis.** The system places KV segments in HBM or HBF at write time based on predicted lifetime and frees blocks once the segment is no longer read. The entry reports extension factors of **1.50–2.95×** for the tight SLO and **1.19–1.89×** for the loose SLO, and absolute HBF lifetimes of **3.3–9.3 device‑years**. [...]
  § 5. Results: All numbers below are either directly computed in Section 4 or are labeled projections. | Quantity | Value | Section | |----------|-------|---------| | Warranty margin (max) | $2.44\times$ | 4B | | Warranty margin (min) | $0.66\times$ | 4B | | Implied HBM‑first baseline lifetime (low) | $1.05$ device‑years | 4C | | Implied HBM‑first baseline lifetime (high) | $10.25$ device‑years | 4C | | Geometric‑mean extension | $1.93\times$ | 4D | | Write‑diversion fraction (low $f$) | $15.97\%$ | 4E | | Write‑diversion fraction (high $f$) | $68.05\%$ | 4E | | Annual HBF writes (high $T_{\mathrm{HBF}}$) | $8.20\times10^{3}$ writes/yr ($\approx$ 0.936 writes/h) | 4F | | Annual HBF writes (low $T_{\mathrm{HBF}}$) | $3.03\times10^{4}$ writes/yr ($\approx$ 3.46 writes/h) | 4F | The computed warranty margins show that only the upper endpoint of the reported lifetime range clears the five‑year warranty with a comfortable margin; the lower endpoint falls short. [...]
  § 8. Conclusion: We have formalized the lifetime‑aware KV‑cache placement principle of Lachesis as a threshold rule, derived the algebra that maps the reported extension factors to concrete warranty margins, baseline lifetimes, write‑diversion fractions, and annualized write budgets, and performed all arithmetic with full transparency. The analysis shows that the reported **1.19–3.13×** extension translates to diverting **$\approx$ 16 %–68 %** of baseline HBF writes, yielding warranty margins ranging from **0.66×** (insufficient) to **2.44×** (comfortably sufficient) under the five‑year warranty. However, the audit also highlights critical data gaps—most notably the missing baseline write ratio—that prevent a full sizing of HBM headroom. The smallest de‑risking experiment is a trace‑replay study that directly measures HBF write reduction; its outcome will either validate the proportionality assumption or falsify the central claim. [...]