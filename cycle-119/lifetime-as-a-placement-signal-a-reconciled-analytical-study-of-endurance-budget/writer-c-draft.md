# Lifetime as a Placement Signal: An Analytical Study of Endurance Budgets for KV Cache Tiering across HBM and High-Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large language model (LLM) serving accumulates key-value (KV) cache across many orchestrated requests, and high-bandwidth flash (HBF) offers an order of magnitude more capacity than HBM at HBM-class read bandwidth, but its finite write endurance constrains how much write traffic it can absorb. This paper develops an analytical treatment of the lifetime-aware placement principle underlying Lachesis, a placement layer that assigns KV segments to HBM or HBF by expected lifetime and frees blocks at last read. We formalize the placement decision as a lifetime-threshold rule, derive the relationship between write-diversion fraction and achievable lifetime extension, and audit the reported simulation results — a $1.19$–$3.13\times$ extension over HBM-first placement and $3.3$–$12.2$ device-years of HBF lifetime — with fully shown arithmetic. We compute warranty margins of $2.44\times$ and $0.66\times$ against a five-year warranty, infer implied baseline lifetimes of $1.05$–$10.25$ device-years, and show that the reported extensions correspond to diverting $15.97\%$–$68.05\%$ of HBF-bound write traffic back to HBM. The analysis clarifies when lifetime-aware placement suffices, when it fails, and what evidence a production deployment would require.

## 1. Introduction

LLM serving is increasingly dominated by agentic workloads: harnesses orchestrate agents and sub-agents that accumulate context as KV cache across many requests, consuming substantial memory [1]. High-bandwidth flash (HBF), an on-package 3D-NAND memory class, promises an order of magnitude greater capacity than HBM at HBM-class read bandwidth, making it a natural tier for context that exceeds HBM capacity. The obstacle is endurance: flash devices tolerate a finite number of program/erase cycles, so every write sent to HBF consumes a non-renewable budget.

The insight examined in this paper is that KV cache should be placed across HBM and HBF by its *lifetime* — the interval between a segment's first write and its last read. Placing shorter-lived data in HBM lets HBM absorb more of an agent run's writes indirectly (through HBM churn and freeing) and sends fewer of them to HBF. Because the lifetime of KV cache in agentic serving is dictated by the harness — the program that orchestrates the agents — lifetime is, in principle, observable or predictable at write time, not merely inferred from access counters [1].

The contribution of this paper is not a new system but an analytical companion to the Lachesis design [1], [2]. We (i) formalize the placement rule and its three lifetime axes (temporal, structural, inter-worker), (ii) derive the algebra connecting write diversion, endurance, and device lifetime, and (iii) audit the reported trace-driven results with explicit arithmetic, converting headline factors into warranty margins, implied baselines, and write-diversion percentages. Section 6 discusses failure modes and what evidence would falsify the approach.

## 2. Background and Related Work

We review the works supplied in the bibliography, in their exact numbering.

**[1], [2] Lachesis.** The arXiv query entry [1] and its abstract record [2] describe the same system: a lifetime-aware KV cache placement layer between the agent harness and the serving engine. At write time it places each segment in HBM or HBF according to its lifetime, and frees blocks once the segment is no longer read. The abstract identifies three axes along which lifetime diverges in agentic serving — temporal, structural, and inter-worker — and reports trace-driven results: a $1.19$–$3.13\times$ HBF lifetime extension over HBM-first placement, reaching $3.3$–$12.2$ device-years, with HBF outlasting a five-year warranty under continuous 24x7 operation at full SLO-admissible load on the multi-agent trace. This paper takes [1] as its grounding object of study.

**[3] Congestion-aware routing and content placement in elastic cache networks.** This work addresses, for networks with arbitrary topology and congestion-dependent nonlinear cost functions, the joint determination of cache deployment, content placement, and hop-by-hop routing, noting that the optimal tradeoff between routing cost and cache deployment cost remains open. It supplies the general framing that placement is a cost-coupled optimization, not a local heuristic; our lifetime-threshold rule is a single-tier special case of such placement problems.

**[4] PolyKV.** PolyKV lets multiple concurrent inference agents share a single, asymmetrically compressed KV cache pool rather than allocating a separate cache per agent, writing a compressed cache once and injecting it into $N$ independent agent contexts via HuggingFace DynamicCache objects, with keys quantized at int8 ($\text{q8\_0}$). PolyKV attacks the *size* of agentic KV state; Lachesis attacks its *placement and wear*. The two are complementary: compression reduces the write volume that reaches any tier, which also stretches HBF endurance, though the supplied entry does not quantify endurance effects.

**[5] HBF for generative recommendation serving.** This work applies HBF to generative recommendation systems that reuse user-level KV cache to avoid recomputing long user histories, and introduces a write-aware KV cache policy; the entry notes HBF offers substantially higher capacity than HBM while approaching HBM-class read bandwidth. It is the closest antecedent in spirit: write-awareness as a first-class policy concern on the same device class, though in a recommendation rather than agent-orchestration context.

**[6] HBM Is Not All You Need.** This work observes that LLM inference splits into a compute-bound prefill phase and a memory-bound decode phase, that disaggregated systems separate them onto distinct hardware, and that datacenter GPUs' costly HBM bandwidth sits almost entirely idle during prefill; it proposes memory-heterogeneous accelerators (MemHA) pairing GDDR-based accelerators for prefill with HBM-based GPUs for decode. It supports the broader thesis that HBM is a scarce resource to be spent deliberately — the same scarcity logic that motivates spending HBM *writes* rather than HBF writes in Lachesis.

**[7] Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving.** This work describes agentic serving with multi-turn sessions that idle between actions yet must retain full context, where limited GPU memory forces eviction of inactive KV states so that resuming a session incurs costly recomputation or slow interconnect transfers, and proposes HBF — described as an on-package 3D-NAND memory — for tiering. It establishes the HBM/HBF two-tier substrate for agentic serving; the supplied entry is truncated and gives no detail on its placement policy or endurance treatment, so we relate it to our argument only through the tiering problem it states.

**[8] Cache-coloring for non-volatile caches.** This work studies non-volatile on-chip caches such as STT-RAM, noting their density and low leakage power but limited write endurance, and that existing cache management policies are write-variation unaware, causing excessive writes to a few blocks. It is the classical precedent for endurance-aware cache management: the inter-set write-variation problem it addresses is the same *wear concentration* phenomenon that lifetime-aware placement mitigates at the HBM/HBF boundary.

**[9] Locality and Utilization in Placement Suboptimality.** This book chapter constructs mixed-size placement benchmark sets — including PEKO-MC, a set of standard examples — targeting the role of nonlocal nets and of white space and module-size variation in suboptimality. Its relevance is methodological: benchmarks constructed to expose specific sources of suboptimality. Our audit of Lachesis against an HBM-first baseline plays the analogous role for placement policies, though we construct no new benchmark suite.

**[11] QuWARP Reconciled.** This QNFO entry notes that classical quantum-circuit simulation increasingly appears as repeated-run workloads — variational quantum eigensolver sweeps, noisy multishot studies, and quantum error-correction cycles — and discusses the QuWARP planner's workload-level reuse planning. The analogy is structural: both works treat *reuse across repeated invocations* as a plannable resource, as Lachesis treats harness-dictated KV lifetime. The entry is truncated and supports no quantitative claim here.

**[13] LiveBench-grounded LLM audit.** This entry audits the frontier LLM landscape (August 2026) for mathematics-heavy scientific research and agentic AI, grounded in the LiveBench 2026-06-25 contamination-free benchmark, finding no Llama model in the top 42 and identifying a mathematics price-performance leader. We cite it only as evidence that agentic AI is an active evaluation target, motivating serving-efficiency work; its findings bear no arithmetic on our results.

We do not cite [10] or [12]: the former concerns Hamiltonian-computation switching costs with no memory-endurance content derivable from its entry, and the latter's supplied summary is empty, so no substantive statement about it can be grounded.

## 3. Methods

### 3.1 System model

A serving engine holds KV cache in two tiers: HBM with capacity $C_{\text{HBM}}$ bytes and effectively unlimited write endurance within a device service life, and HBF with capacity $C_{\text{HBF}} \gg C_{\text{HBM}}$ (the abstract of [1] states an order-of-magnitude capacity advantage) and a finite write-endurance budget of $E_{\text{HBF}}$ program/erase-equivalent cycles per cell.

A KV *segment* $s$ is the unit of placement. It has a write time $t_w(s)$, a last-read time $t_r(s)$, and a lifetime

$$\tau_s = t_r(s) - t_w(s).$$

The harness dictates $\tau_s$ in agentic serving [1]; Lachesis observes harness behavior along three axes — temporal (when segments die), structural (which segments belong to which agent or sub-agent), and inter-worker (how lifetime differs across workers) [1].

### 3.2 Placement rule

Lachesis places each segment at write time and frees its blocks once the segment is no longer read [1]. We model the decision as a lifetime-threshold rule:

$$p(s) = \begin{cases} \text{HBM} & \text{if } \tau_s \leq \tau^*, \\ \text{HBF} & \text{if } \tau_s > \tau^*, \end{cases}$$

where $\tau^*$ is chosen so that HBM's capacity and churn constraints are respected. The HBM-first baseline, by contrast, fills HBM first and spills all overflow writes to HBF regardless of lifetime.

### 3.3 Endurance accounting

Let $W_{\text{HBF}}$ be the number of writes reaching HBF over an observation window and $W_{\text{tot}}$ the total KV writes. The HBF lifetime in device-years is

$$T_{\text{HBF}} = \frac{E_{\text{HBF}}}{W_{\text{HBF}}^{(\text{yr})}},$$

where $W_{\text{HBF}}^{(\text{yr})}$ is the annualized HBF write volume. Under the standard assumption that wear is proportional to HBF write volume, a placement policy that extends lifetime by a factor $f$ must reduce HBF write volume by the same factor:

$$f = \frac{W_{\text{HBF,base}}^{(\text{yr})}}{W_{\text{HBF,Lach}}^{(\text{yr})}}, \qquad \phi = 1 - \frac{1}{f},$$

where $\phi$ is the fraction of baseline HBF-bound write traffic diverted to HBM (or eliminated by earlier freeing). All derivations below use only numbers stated in [1] and arithmetic shown in Section 4; where an endurance figure is needed that [1] does not supply, we use explicitly labeled illustrative assumptions.

## 4. Analysis

Every input number below is stated with its source. Inputs from the literature: extension factor range $f \in [1.19,\, 3.13]$ and HBF lifetime range $T_{\text{HBF}} \in [3.3,\, 12.2]$ device-years, both reported in the abstract of [1]; warranty duration $5$ years, stated in [1]; continuous 24x7 operation, stated in [1].

**(A) Hours in a year and in a warranty period.** Continuous operation gives $24 \times 365 = 8760$ hours per year, and a five-year warranty spans $5 \times 8760 = 43800$ hours.

**(B) Warranty margins.** The margin against the five-year warranty is

$$m = \frac{T_{\text{HBF}}}{5}.$$

For the upper reported lifetime: $m_{\max} = 12.2 / 5 = 2.44$. For the lower: $m_{\min} = 3.3 / 5 = 0.66$. The lower endpoint lies *below* the warranty threshold; the abstract of [1] states that HBF outlasts the warranty specifically *on the multi-agent trace*, so the multi-agent trace must correspond to a lifetime above $5$ device-years within the reported range, and the $3.3$ device-year endpoint must arise from a different trace in the evaluation. This is an inference from the stated numbers, not an additional reported fact.

**(C) Implied baseline (HBM-first) lifetimes.** Since $T_{\text{Lach}} = f \cdot T_{\text{base}}$, the baseline lifetime implied by each reported pair is $T_{\text{base}} = T_{\text{Lach}} / f$. Taking the reported endpoints at face value:

$$T_{\text{base}}^{(\text{low})} = \frac{3.3}{3.13} = 1.05431\ldots \approx 1.05 \text{ device-years},$$

$$T_{\text{base}}^{(\text{high})} = \frac{12.2}{1.19} = 10.25210\ldots \approx 10.25 \text{ device-years}.$$

(Computations: $3.3/3.13 = 1.0543127...$; $12.2/1.19 = 10.2521008...$.) The implied baseline range $[1.05, 10.25]$ device-years is an envelope, not a claim that any single trace produced both endpoints; pairing within a trace would require per-trace data that [1]'s abstract does not supply.

**(D) Geometric-mean extension.** The geometric mean of the reported extension range is

$$\bar{f} = \sqrt{1.19 \times 3.13} = \sqrt{3.7247} = 1.92999\ldots \approx 1.93\times.$$

**(E) Write-diversion fraction.** Under the proportionality assumption of Section 3.3,

$$\phi = 1 - \frac{1}{f}.$$

For $f = 1.19$: $1/1.19 = 0.840336\ldots$, so $\phi = 0.159664\ldots \approx 15.97\%$. For $f = 3.13$: $1/3.13 = 0.319490\ldots$, so $\phi = 0.680510\ldots \approx 68.05\%$. Thus the reported extensions correspond to diverting between roughly $16\%$ and $68\%$ of baseline HBF-bound write traffic.

**(F) Annualized write budget (parametric, labeled projection).** The abstract of [1] does not state $E_{\text{HBF}}$ or the absolute write rate. We therefore give a parametric inversion: from $T_{\text{HBF}} = E_{\text{HBF}} / W_{\text{HBF}}^{(\text{yr})}$,

$$W_{\text{HBF}}^{(\text{yr})} = \frac{E_{\text{HBF}}}{T_{\text{HBF}}}.$$

*Illustrative assumption (labeled projection, not a reported result):* if $E_{\text{HBF}} = 10^{5}$ cycles, then at $T_{\text{HBF}} = 12.2$ device-years,

$$W_{\text{HBF}}^{(\text{yr})} = \frac{10^{5}}{12.2} = 8196.72\ldots \approx 8.20 \times 10^{3} \text{ writes/year},$$

which under 24x7 operation is $8196.72 / 8760 = 0.93574\ldots \approx 0.94$ HBF writes per hour. At the low endpoint $T_{\text{HBF}} = 3.3$: $10^{5}/3.3 = 30303.03\ldots \approx 3.03 \times 10^{4}$ writes/year, i.e. $30303.03/8760 = 3.45970\ldots \approx 3.46$ writes/hour. If instead $E_{\text{HBF}} = 3 \times 10^{3}$ cycles, the budgets scale down by $3 \times 10^{3}/10^{5} = 0.03$: about $245.90$ and $909.09$ writes/year respectively. These figures quantify how tight the HBF write budget is; they are conditional on the assumed endurance and inherit the linearity assumption of Section 3.3.

**(G) HBM headroom required.** The diverted traffic of (E) must fit in HBM's write bandwidth and churn budget. As a fraction of total KV writes $W_{\text{tot}}$, the diverted volume is $\phi \cdot W_{\text{HBF,base}}$; without the ratio $W_{\text{HBF,base}}/W_{\text{tot}}$ — not stated in [1] — we cannot convert this to an absolute HBM load, and we flag this as the principal data gap in the audit.

## 5. Results

We report (i) numbers computed in Section 4 from inputs stated in [1], and (ii) the reported results of [1] themselves, attributed as such. No simulation or measurement was performed for this paper.

**Reported in [1] (attributed):** HBF lifetime extension of $1.19$–$3.13\times$ over HBM-first placement; HBF lifetime of $3.3$–$12.2$ device-years; HBF outlasting the five-year warranty under continuous 24x7 operation at full SLO-admissible load on the multi-agent trace.

**Computed here:**

- Warranty margins: $m_{\max} = 2.44\times$ and $m_{\min} = 0.66\times$ against the five-year warranty (Section 4B).
- Implied HBM-first baseline lifetime envelope: $1.05$–$10.25$ device-years (Section 4C).
- Geometric-mean extension: $\bar{f} \approx 1.93\times$ (Section 4D).
- Write-diversion fraction implied by the extension range: $\phi \approx 15.97\%$ to $68.05\%$ of baseline HBF-bound writes (Section 4E).
- Parametric annualized HBF write budgets under the labeled illustrative assumption $E_{\text{HBF}} = 10^{5}$ cycles: $8.20 \times 10^{3}$ writes/year ($0.94$/hour) at $12.2$ device-years and $3.03 \times 10^{4}$ writes/year ($3.46$/hour) at $3.3$ device-years; scaled by $0.03$ if $E_{\text{HBF}} = 3 \times 10^{3}$ (Section 4F, projections).
- Continuous-operation arithmetic: $8760$ hours/year; $43800$ hours in a five-year warranty (Section 4A).

The headline qualitative result of the audit: the reported extension range is large enough that even its lower endpoint ($1.19\times$, i.e., a $15.97\%$ write diversion) is meaningful, but only the upper portion of the reported lifetime range clears the five-year warranty with margin, and the $3.3$ device-year endpoint falls $0.66\times$ short of it.

## 6. Discussion

**Limitations.** First, all quantitative grounding comes from a single source, the abstract of [1]; the underlying trace characteristics, per-trace extension factors, endurance figure, and write-rate measurements are not supplied, so several of our quantities (the baseline envelope, the diversion fractions) are bounds or envelopes rather than per-trace values. Second, the endurance-to-lifetime inversion in Section 4F rests on a labeled illustrative endurance assumption and on linear wear accumulation; real flash wear exhibits cell-to-cell variation and wear-leveling effects, and the write-variation problem documented for non-volatile caches [8] suggests concentration effects that a uniform-rate model misses. Third, the proportionality between lifetime extension and write diversion (Section 3.3) holds only if the policy does not otherwise change read traffic or HBM churn; if lifetime-aware placement increases HBM eviction and re-prefill traffic, some diverted writes return indirectly.

**Failure modes.** Lifetime-aware placement fails when the harness cannot expose or the layer cannot predict segment lifetime: mispredicting a long-lived segment as short-lived sends it to HBM (capacity pressure, eviction churn), while mispredicting a short-lived segment as long-lived sends it to HBF (wasted endurance, exactly the pathology the policy exists to prevent). It also fails under adversarial or degenerate harnesses in which all segments have similar lifetime, collapsing the temporal axis and reducing the policy to the baseline; the $1.19\times$ lower endpoint of [1] may reflect precisely such a trace, though the abstract does not say. Finally, the warranty result is trace-specific: our computed $m_{\min} = 0.66$ shows that at least one evaluated configuration does *not* clear five years, so "outlasts the warranty" cannot be generalized across workloads.

**What would falsify the claims.** The central claim — that lifetime-aware placement materially extends HBF life — would be falsified if per-trace data showed the extension factors to be artifacts of baseline pathology (e.g., an HBM-first baseline that spills gratuitously), if measured HBF wear under Lachesis did not scale with the computed diversion fractions $\phi$, or if harness-predicted lifetimes proved no better than access-frequency heuristics at comparable cost. The warranty claim would be falsified by any workload class where the implied baseline envelope's low end ($1.05$ device-years) is typical and the extension stays near $1.19\times$, yielding roughly $1.25$ device-years — far below warranty.

**Open questions.** What is the joint optimization of placement with compression, given that pools like PolyKV [4] shrink write volume before it reaches any tier? How should $\tau^*$ adapt online when harness behavior shifts along the inter-worker axis [1]? And can the placement-suboptimality benchmark methodology of [9] be adapted to build standard traces that isolate each lifetime axis, so that extension factors become comparable across systems?

## 7. Conclusion

We presented an analytical audit of lifetime-aware KV cache placement across HBM and high-bandwidth flash for agentic LLM serving. Formalizing the Lachesis placement principle [1] as a lifetime-threshold rule with free-at-last-read semantics, we derived the algebra linking write diversion to endurance lifetime and computed, with fully shown arithmetic, that the reported $1.19$–$3.13\times$ extension corresponds to diverting $15.97\%$–$68.05\%$ of HBF-bound writes, that the reported $3.3$–$12.2$ device-year lifetimes imply warranty margins of $0.66\times$ to $2.44\times$, and that the implied HBM-first baseline spans $1.05$–$10.25$ device-years. The analysis supports lifetime as a placement signal of substantial but workload-dependent value, and identifies the missing per-trace and endurance data that a production claim would require.

## References

[1] TITLE: arXiv Query: search_query=&id_list=2610.08378&start=0&max_results=1. ABSTRACT: Large language model (LLM) serving is increasingly dominated by agentic workloads... (Lachesis abstract, arXiv:2610.08378).

[2] arXiv:2610.08378v1 | Lachesis: Lifetime-Aware KV Cache Placement for Agent Serving across HBM and High-Bandwidth Flash.

[3] arXiv:2303.01648v1 | Congestion-aware routing and content placement in elastic cache networks.

[4] arXiv:2604.24971v1 | PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference.

[5] arXiv:2609.07175v1 | Enabling High-Bandwidth Flash for Generative Recommendation Serving with Write-Aware KV Cache Policy.

[6] arXiv:2606.29986v1 | HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators.

[7] arXiv:2609.25782v1 | Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving.

[8] arXiv:1310.8494v1 | Using Cache-coloring to Mitigate Inter-set Write Variation in Non-volatile Caches.

[9] arXiv:2305.16413v1 | Locality and Utilization in Placement Suboptimality.

[11] QNFO: QuWARP Reconciled: An Analytical Cost-Model Assessment of Workload-Level Reuse Planning for Quantum Circuit Simulation.

[13] QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026).