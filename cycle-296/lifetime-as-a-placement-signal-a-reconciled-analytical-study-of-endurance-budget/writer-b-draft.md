# Lifetime as a Placement Signal: A Corrected Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High-Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large-language-model (LLM) serving accumulates key-value (KV) cache across many orchestrated requests, and high-bandwidth flash (HBF) offers an order-of-magnitude more capacity than high-bandwidth memory (HBM) at comparable read bandwidth, but its finite program/erase (P/E) endurance caps how much write traffic it can absorb. Prior analytical audits of the Lachesis placement system propagated headline numbers that conflict with the system's own evaluation table, producing baseline lifetimes inconsistent with the reported per-configuration data. This paper re-derives the endurance algebra from the per-configuration evaluation results of Lachesis and from the HBF device specification. Using the evaluation-reported extensions of $1.50$–$2.95\times$ (tight SLO) and $1.19$–$1.89\times$ (loose SLO), Lachesis lifetimes of $3.3$–$9.3$ device-years against HBM-first baselines of $1.9$–$4.8$ device-years, and the $10^{5}$-cycle P/E rating with write-amplification factor $\mathrm{WAF}\approx 1.02$, we compute: warranty margins of $0.66$–$1.86$ for Lachesis and $0.38$–$0.96$ for HBM-first; write-diversion fractions of $15.97\%$–$66.10\%$; annualized HBF write budgets of $1.08\times 10^{4}$–$3.03\times 10^{4}$ writes per cell per year ($1.23$–$3.46$ writes per hour) for Lachesis and up to $5.26\times 10^{4}$ writes per cell per year ($6.01$ writes per hour) for HBM-first; and geometric-mean extensions of $2.10\times$ (tight) and $1.50\times$ (loose). The corrected baselines remove the contradiction between derived and reported lifetimes, and the audit now shows that Lachesis clears a five-year warranty at every evaluated multi-agent configuration while HBM-first placement generally does not.

## 1. Introduction

Operators of LLM-serving infrastructure face a capacity endgame driven by agentic workloads: harnesses orchestrate agents and sub-agents across many requests, so KV cache accumulates over entire multi-turn sessions instead of resetting per query. Limited GPU memory forces eviction of inactive KV states, and resuming a session then costs either recomputation or slow interconnect transfers. High-bandwidth flash (HBF), an on-package 3D-NAND class, provides an order-of-magnitude capacity advantage over HBM while preserving HBM-class read bandwidth, which makes it a natural tier for retained context. The obstacle is endurance: flash tolerates only a finite number of program/erase (P/E) cycles, so every write to HBF consumes a non-renewable budget that can be exhausted before the device's five-year warranty expires.

If a placement policy can predict a segment's lifetime — the interval between its first write and its last read — then short-lived segments stay in HBM, whose endurance is effectively unlimited for the service life, while long-lived segments are diverted to HBF. Lachesis implements this idea: it places each KV segment in HBM or HBF at write time according to its lifetime and frees its blocks once the segment is no longer read [1], [2]. The stakes for an operator are concrete. An HBF tier is only worth provisioning if the projected device lifetime clears the warranty horizon under the workload's write rate; the amount of HBM headroom that must be reserved for diverted writes determines the GPU-memory partition; and the per-cell write budget determines whether endurance telemetry and wear-leveling are needed. Wrong numbers on any of these lead to either wasted HBF capacity or field failures inside the warranty period.

This revision exists because the previously published audit propagated two numerical errors. First, it attributed the headline extension range $1.19$–$3.13\times$ and lifetime range $3.3$–$12.2$ device-years to [1]; the evaluation section of [1] in fact reports extensions of $1.50$–$2.95\times$ at the tight SLO and $1.19$–$1.89\times$ at the loose SLO, with Lachesis reaching $3.3$–$9.3$ device-years against HBM-first baselines of $1.9$–$4.8$ device-years at the four configurations that give HBM one to four of eight slots. Second, the earlier audit derived implied HBM-first baselines of $1.05$–$10.25$ years by dividing mismatched endpoint pairs, contradicting the per-configuration baselines of $1.9$–$4.8$ years that [1] itself reports; the derived values are an artifact of pairing a minimum with a maximum that come from different configurations, and this paper replaces them with the reported baselines. Every downstream quantity — warranty margins, diversion fractions, write budgets — is recomputed here from the corrected inputs, with all arithmetic shown.

**Contributions**
1. A reconciliation of the conflicting headline figures for Lachesis, adopting the per-configuration evaluation numbers of [1] over the abstract-level ranges, with the discrepancy documented (Section 2).
2. The algebra linking an extension factor $f$, the write-diversion fraction $\phi$, and HBF device-year lifetime $T_{\mathrm{HBF}}$, under an explicit linear-wear assumption (Section 3).
3. Fully shown arithmetic converting the corrected extension and lifetime ranges into warranty margins, reported baselines, geometric-mean extensions, diversion fractions, and annualized per-cell write budgets using the $10^{5}$-cycle rating from [7], including a consistency check of the diversion model against the absorption percentages reported in [1] (Section 4).
4. A discussion of limitations, failure modes, the observation that would falsify the central claim, and open questions (Section 6).
5. A practical pathway for operators and harness developers, including a TRL assessment, the smallest de-risking experiment, engineering constraints, and labeled projections (Section 7).

## 2. Background and Related Work

**[1], [2] Lachesis.** Lachesis is a lifetime-aware KV cache placement layer between the agent harness and the serving engine: at write time it places each segment in HBM or HBF according to its lifetime, and it frees blocks once the segment is no longer read [1], [2]. Its evaluation reports that at the four GPU-memory configurations giving HBM one to four of eight slots, Lachesis reaches $3.3$–$9.3$ device-years against HBM-first's $1.9$–$4.8$, extending HBF lifetime by $1.50$–$2.95\times$ at a tight SLO and $1.19$–$1.89\times$ at a loose one, and that at a tight SLO HBF outlasts the five-year warranty under Lachesis at every configuration and on both evaluated models [1]. The same section attributes the gain to a single ratio, HBM capacity against the short-lived KV live at one time, and reports that moving from one HBM slot in four to four absorbs $12\%$ of HBM-first's flash writes and $54$–$56\%$ of Lachesis's [1]. These per-configuration numbers are the quantitative backbone of this audit; the abstract-level ranges $1.19$–$3.13\times$ and $3.3$–$12.2$ device-years stated in [2] do not appear in the evaluation results and are treated here as superseded.

**[3] Congestion-aware routing and content placement in elastic cache networks.** This work formulates joint cache deployment, content placement, and hop-by-hop routing as a cost-minimization problem and shows in simulation that a jointly optimized online algorithm achieves a total cost up to $30\%$ lower than the second-best method, while heuristic utility-based deployment falls between no optimization and joint optimization [3]. It establishes the precedent that placement decisions are properly expressed as constrained optimization rather than fixed heuristics; the lifetime-threshold rule audited here is a specialized, single-node instance of that framing.

**[4] PolyKV.** PolyKV lets multiple concurrent inference agents share one asymmetrically compressed KV pool, writing the cache once and distributing it to $N$ agents, with a stable $2.91\times$ compression ratio across model architectures and a $97.7\%$ KV-memory reduction ($19.8$ GB to $0.45$ GB) at 15 agents sharing a 4K context on Llama-3-8B, at $+0.57\%$ PPL degradation [4]. Compression reduces the byte volume of every KV write, so it multiplies with placement-based diversion when both are applied to the same workload; Section 6 treats the interaction as an open multiplicative question rather than assuming independence.

**[5] HBF for generative recommendation serving.** In generative recommendation, an admission-controlled LRU-$K$ policy that selectively persists KV caches and decouples writes from cache misses extends HBF lifetime from about one year with LRU-1 to over six years with LRU-10, while HBF-based systems reach $3.8$–$4.7\times$ higher throughput than HBM-only [5]. This is an independent confirmation, in a different workload domain, that write-aware policy choices move HBF endurance by factors comparable to the extensions Lachesis reports, and that naive policies (LRU-1) can exhaust HBF in roughly a year.

**[6] HBM Is Not All You Need.** This work observes that LLM inference splits into a compute-bound prefill phase and a memory-bound decode phase, and pairs GDDR-based accelerators for prefill with HBM-based GPUs for decode, achieving up to $3.2\times$ higher goodput and $4.8\times$ higher goodput-per-dollar than homogeneous A100 disaggregation on real silicon [6]. Its argument that HBM bandwidth and capacity are scarce, expensive resources supports this paper's premise that HBM should be reserved for the writes that benefit from it — short-lived data — rather than absorbing arbitrary overflow.

**[7] Hot-cold tiering of HBM and high bandwidth flash.** This work models an HBF tier of $3$ TiB SLC with bandwidth matching HBM, rated at $100{,}000$ program/erase cycles with $25\,\mu\mathrm{s}$ read access latency, and shows that because KV is immutable and appended in erase-block-aligned units, the flash avoids read-modify-write and garbage-collection rewrites, keeping the write-amplification factor near unity ($\approx 1.02$) compared to $2$–$4$ for a general-purpose SSD [7]. It also reports that the hot-cold hierarchy supports an order of magnitude more concurrent sessions per GPU and cuts memory-read power by about $7.6$ kW per 8-GPU node versus an all-KV-to-flash design [7]. This paper adopts its $10^{5}$-cycle endurance rating and its $\mathrm{WAF}\approx 1.02$ as the device-level inputs for all write-budget computations.

**[8] Cache-coloring for non-volatile caches.** For non-volatile caches built from devices such as STT-RAM, write-variation-unaware policies direct excessive writes at a few blocks; a cache-coloring technique that mitigates this inter-set write variation yields an average $4.20\times$ improvement in cache lifetime, defined as the inverse of the maximum number of writes on any block, at an average performance of $0.96\times$, a $9.42\%$ energy increase, and a $0.85$ MPKI increase [8]. Two points carry over: endurance is limited by the hottest block, not the average, so wear-leveling interacts with any placement policy; and policy-level lifetime gains of several times are achievable at small performance cost, which makes the extension factors reported by [1] plausible in magnitude.

**[10] Prior assumptions-only audit.** The earlier version of this analysis treated the extension and lifetime ranges as labeled assumptions and derived warranty margins, implied baselines of $1.05$–$10.25$ device-years, diversion fractions, and write budgets, but it keyed its derivations to the abstract-level ranges and lacked the per-configuration numbers and the concrete endurance rating now used [10]. The present paper supersedes it by re-deriving every quantity from the evaluation results of [1] and the device specification of [7], and by correcting the two errors identified above.

Collectively, these works place the audit at the intersection of placement theory [3], write-aware endurance policy [5], [8], device-level HBF characterization [7], memory-hierarchy economics [6], and KV compression [4], with Lachesis [1], [2] as the system under audit.

## 3. Methods

### 3.1 System model

The serving engine maintains KV cache in two tiers:

- **HBM tier** — capacity $C_{\mathrm{HBM}}$ in bytes, with effectively unlimited write endurance over the service life of the device.
- **HBF tier** — capacity $C_{\mathrm{HBF}} \gg C_{\mathrm{HBM}}$, with a finite endurance budget of $E_{\mathrm{HBF}}$ P/E cycles per cell. Following the device specification in [7], $E_{\mathrm{HBF}} = 10^{5}$ cycles, and because KV entries are immutable and appended in erase-block-aligned units, the write-amplification factor is $\mathrm{WAF} \approx 1.02$ [7].

A KV **segment** $s$ is the placement unit. It has a write timestamp $t_{w}(s)$, a last-read timestamp $t_{r}(s)$, and a lifetime

$$
\tau_{s} = t_{r}(s) - t_{w}(s).
$$

The harness dictates $\tau_{s}$ in agentic serving, as analyzed in [1], which identifies temporal, structural, and inter-worker axes along which lifetime diverges.

### 3.2 Placement rule

Lachesis places each segment at write time and frees its blocks once the segment is no longer read [1]. The decision is modeled as a lifetime-threshold rule:

$$
p(s) =
\begin{cases}
\mathrm{HBM} & \text{if } \tau_{s} \le \tau^{*},\\[4pt]
\mathrm{HBF} & \text{if } \tau_{s} > \tau^{*},
\end{cases}
$$

where the threshold $\tau^{*}$ is chosen to respect HBM capacity $C_{\mathrm{HBM}}$ and to keep HBM churn within acceptable limits. The **HBM-first baseline** fills HBM until capacity is exhausted and then spills all overflow writes to HBF, ignoring lifetime.

### 3.3 Endurance accounting

Let $W_{\mathrm{HBF}}$ be the number of writes reaching HBF over an observation window and $W_{\mathrm{tot}}$ the total KV writes. The device-year lifetime of HBF is

$$
T_{\mathrm{HBF}} = \frac{E_{\mathrm{HBF}}}{W_{\mathrm{HBF}}^{(\mathrm{yr})}},
$$

where $W_{\mathrm{HBF}}^{(\mathrm{yr})}$ is the annualized per-cell write volume in writes per cell per year. Under the linear-wear assumption — wear proportional to write volume, uniform across cells — a placement policy that achieves an extension factor

$$
f = \frac{T_{\mathrm{Lach}}}{T_{\mathrm{base}}}
$$

must reduce HBF write volume by the same factor:

$$
f = \frac{W_{\mathrm{HBF,base}}^{(\mathrm{yr})}}{W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}}, \qquad
\phi = 1 - \frac{1}{f},
$$

where $\phi$ is the write-diversion fraction: the proportion of baseline HBF-bound writes that are either absorbed by HBM or eliminated by earlier freeing. The write-amplification factor enters as an effective endurance $E_{\mathrm{HBF}}^{\mathrm{eff}} = E_{\mathrm{HBF}} / \mathrm{WAF}$; since $\mathrm{WAF} \approx 1.02$ [7], the effect on every derived lifetime is under $2\%$ and is carried as a stated bound rather than applied to each number.

### 3.4 Input reconciliation

Two families of numbers exist for Lachesis. The abstract of [2] states an extension of $1.19$–$3.13\times$ and lifetimes of $3.3$–$12.2$ device-years. The evaluation section of [1] states, for the four configurations giving HBM one to four of eight slots, extensions of $1.50$–$2.95\times$ (tight SLO) and $1.19$–$1.89\times$ (loose SLO), Lachesis lifetimes of $3.3$–$9.3$ device-years, and HBM-first baselines of $1.9$–$4.8$ device-years. This paper adopts the evaluation numbers as primary, because they are per-configuration, internally consistent, and accompanied by baselines; the abstract-level ranges are recorded as a discrepancy and not used in any derivation. All derivations in Section 4 use only numbers stated in [1], [2], or [7], or are labeled as assumptions.

### 3.5 What this paper does not do

No simulation, measurement, or trace collection is performed. All quantitative claims are either (i) reported by cited works and attributed by number, or (ii) derived here from those reports using the algebra of Section 3.3, with every arithmetic step shown.

## 4. Analysis

All input numbers are cited to [1], [2], or [7]; where an input is absent from the cited works it is labeled as an assumption.

### (A) Hours per year and warranty period

Continuous operation gives $24 \times 365 = 8760$ hours per year. A five-year warranty corresponds to $5 \times 8760 = 43800$ hours of continuous operation. The five-year warranty horizon is the dashed line used in the evaluation of [1].

### (B) Warranty margins

The warranty margin is $m = T_{\mathrm{HBF}} / 5$, dimensionless.

For Lachesis, using the evaluation lifetimes of [1]:

- Upper endpoint: $m_{\max} = 9.3 / 5 = 1.86$.
- Lower endpoint: $m_{\min} = 3.3 / 5 = 0.66$.

For the HBM-first baseline, using the baselines of [1]:

- Upper endpoint: $m_{\mathrm{base,max}} = 4.8 / 5 = 0.96$.
- Lower endpoint: $m_{\mathrm{base,min}} = 1.9 / 5 = 0.38$.

Every Lachesis margin at the evaluated multi-agent configurations lies at or above $0.66$, and [1] reports that at a tight SLO HBF outlasts the five-year warranty under Lachesis at every configuration and on both models; the HBM-first margins never exceed $0.96$, consistent with [1]'s report that HBM-first clears the warranty only in one configuration (Qwen3-235B-A22B on H3's daisy chain).

### (C) Baseline lifetimes: correction of the earlier derivation

The earlier audit [10] derived implied HBM-first baselines by dividing the lifetime endpoints by the extension endpoints: $3.3 / 3.13 = 1.054$ years and $12.2 / 1.19 = 10.252$ years. That derivation is incorrect on two counts. First, its inputs ($3.13\times$, $12.2$ years) do not match the evaluation results of [1]. Second, even with correct inputs, dividing a minimum lifetime by a maximum extension pairs values from different configurations and SLOs; the quotient is not the baseline of any evaluated configuration. The evaluation section of [1] reports the baselines directly: HBM-first reaches $1.9$–$4.8$ device-years at the four constrained configurations. This paper therefore uses the reported baselines and drops the derived $1.05$–$10.25$ year envelope.

As a consistency check rather than a derivation, the lifetime ratios of the reported endpoint pairs are:

- Lower pair: $3.3 / 1.9 = 1.7368421\ldots \approx 1.74$.
- Upper pair: $9.3 / 4.8 = 1.9375$.

Both lie inside the reported extension range $1.19$–$2.95\times$ of [1], which is the expected relation: the endpoint pairs of a min–max envelope need not coincide with any single configuration's extension, but they must fall within its range. They do.

### (D) Geometric-mean extensions

Using the per-SLO extension ranges of [1]:

- Tight SLO: $\bar{f}_{\mathrm{tight}} = \sqrt{1.50 \times 2.95} = \sqrt{4.4250} = 2.10376\ldots \approx 2.10$.
- Loose SLO: $\bar{f}_{\mathrm{loose}} = \sqrt{1.19 \times 1.89} = \sqrt{2.24910} = 1.49970\ldots \approx 1.50$.
- Across both SLOs (endpoints $1.19$ and $2.95$): $\bar{f} = \sqrt{1.19 \times 2.95} = \sqrt{3.51050} = 1.87363\ldots \approx 1.87$.

The earlier audit's geometric mean of $1.93$ was computed from the unsupported pair $1.19 \times 3.13$ and is superseded.

### (E) Write-diversion fractions

From $\phi = 1 - 1/f$:

- $f = 1.19$: $1/1.19 = 0.840336\ldots$, so $\phi = 0.159664 \approx 15.97\%$.
- $f = 1.50$: $1/1.50 = 0.666667\ldots$, so $\phi = 0.333333 \approx 33.33\%$.
- $f = 1.89$: $1/1.89 = 0.529101\ldots$, so $\phi = 0.470899 \approx 47.09\%$.
- $f = 2.95$: $1/2.95 = 0.338983\ldots$, so $\phi = 0.661017 \approx 66.10\%$.

The loose-SLO extensions therefore imply diverting $15.97\%$–$47.09\%$ of baseline