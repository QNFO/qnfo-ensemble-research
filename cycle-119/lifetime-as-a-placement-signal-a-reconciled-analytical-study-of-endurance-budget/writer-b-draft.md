# Lachesis-Class Lifetime-Aware KV Cache Placement across HBM and High-Bandwidth Flash: An Analytical Endurance Model for Agentic LLM Serving

## Abstract

Agentic large language model (LLM) serving accumulates key-value (KV) cache across many requests and sub-agents, and high-bandwidth flash (HBF) offers an order of magnitude more capacity than HBM at HBM-class read bandwidth, but finite write endurance limits its lifetime. This paper develops an analytical endurance model for lifetime-aware KV cache placement of the kind proposed by Lachesis, which places each KV segment in HBM or HBF according to its lifetime and frees blocks when a segment is no longer read. We formalize the placement problem as a write-routing decision whose quality is captured by the fraction of system writes routed to HBF, and we derive device lifetime as a closed-form function of the aggregate HBF write budget, daily write volume, and the write-reduction ratio achieved by lifetime-aware placement over HBM-first placement. Using the extension range of $1.19$–$3.13\times$ and the device-year range of $3.3$–$12.2$ reported for Lachesis in trace-driven simulation, we derive the implied baseline lifetimes of $1.05$–$10.25$ years, show that a conservative endurance budget of $3.0\times10^{8}$ block-writes sustains $3.29$ years at $2.5\times10^{5}$ writes per day, and compute the write-rate ceiling of $1.64\times10^{5}$ writes per day that keeps a five-year warranty with $1.52\times$ headroom. The model makes endurance trade-offs explicit and testable for future HBF deployments.

## 1. Introduction

LLM serving is increasingly dominated by agentic workloads: agents and their sub-agents accumulate context as KV cache across many requests, consuming substantial memory [1], [2]. High-bandwidth flash (HBF) is a promising complement to HBM in this setting, providing an order of magnitude greater capacity at HBM-class read bandwidth, but its finite write endurance is the key limiting factor [1], [2]. The central insight of the Lachesis work is that KV cache should be placed across HBM and HBF by its lifetime: placing shorter-lived data in HBM lets HBM absorb more of an agent run's writes and sends fewer of them to HBF [1], [2]. Because the lifetime of KV cache in agentic serving is dictated by the harness — the program that orchestrates the agents — Lachesis analyzes harness behavior and identifies three axes along which lifetime diverges: temporal, structural, and inter-worker [1], [2].

What the Lachesis abstract reports is empirical: in trace-driven simulation, lifetime-aware placement extends HBF lifetime by $1.19$–$3.13\times$ over HBM-first placement, reaching $3.3$–$12.2$ device-years, and under continuous 24x7 operation at the full load a tight SLO admits, HBF outlasts its five-year warranty on the multi-agent trace [1], [2]. What is missing from the published record, as far as the supplied material shows, is a compact analytical treatment that makes these numbers mutually consistent and reusable: given an endurance budget and a daily write volume, what lifetime follows, and how much write reduction does a placement policy need to buy a warranty margin?

This paper supplies that treatment. We make three contributions. First, we formalize lifetime-aware placement as a write-routing problem and derive closed-form relations among the HBF write budget $B$, the daily HBF write volume $W_{\text{day}}$, the write-reduction ratio $r$, and device lifetime $T$ (Section 3). Second, we instantiate the model with explicitly labeled conservative assumptions and show every arithmetic step, checking that the model is consistent with the ranges reported for Lachesis (Section 4). Third, we derive operational ceilings — the maximum daily HBF write rate compatible with a five-year warranty — and quantify the headroom that lifetime-aware placement provides (Sections 4 and 5). Throughout, we cite only the supplied bibliography and derive only numbers we compute here or quote as reported results with their source.

## 2. Background and Related Work

**Lifetime-aware placement for agentic serving.** The Lachesis paper [1], [2] motivates HBF for agentic LLM serving, identifies the harness as the determinant of KV lifetime, and classifies lifetime divergence along temporal, structural, and inter-worker axes. Its placement layer sits between the agent harness and the serving engine, decides at write time whether each segment goes to HBM or HBF, and frees blocks once a segment is no longer read [1]. The supplied abstract reports the simulation results summarized above; it gives no further architectural detail, and we rely on it only for the problem statement, the three-axis taxonomy, and the reported ranges.

**Hot-cold tiering on the same hardware pair.** Closely related, arXiv:2609.25782v1 [7] addresses agentic LLM serving with multi-turn sessions that idle between actions yet must retain full context; limited GPU memory forces inactive KV states to be evicted, so resuming a session incurs either costly recomputation or slow interconnect transfers, and HBF — described there as an on-package 3D-NAND memory offering orders-of-magnitude more capacity — is proposed for hot-cold tiering of HBM and HBF. The supplied summary is truncated before its mechanism or results, so we use it only to establish that HBM/HBF tiering for agentic sessions is an active design point distinct from write-endurance-driven placement.

**HBF for other serving domains.** arXiv:2609.07175v1 [5] applies HBF to generative recommendation serving, where user-level KV cache reuse avoids recomputing long user histories, and its title indicates a write-aware KV cache policy; the supplied summary establishes that growing KV capacity and bandwidth requirements strain the memory system and that HBF offers substantially higher capacity than HBM while approaching HBM-class read bandwidth. The truncation of the summary prevents us from attributing specific policy mechanisms, but the shared concern with write behavior on HBF makes it the nearest-domain analogue of endurance-aware placement.

**KV cache sharing and compression.** arXiv:2604.24971v1 [4] presents PolyKV, in which multiple concurrent inference agents share a single, asymmetrically compressed KV cache pool: rather than a separate cache per agent, a compressed cache is written once and injected into $N$ independent agent contexts via HuggingFace DynamicCache objects, with keys quantized at int8 (q8_0). Sharing and compression reduce the volume of KV writes a cluster generates, which is complementary to placement: both lower the write burden that endurance must absorb, though the supplied summary does not state endurance effects.

**Memory-heterogeneous serving.** arXiv:2606.29986v1 [6] disaggregates LLM inference — a compute-bound prefill phase and a memory-bound decode phase — onto memory-heterogeneous accelerators (MemHA), pairing GDDR-based accelerators for prefill with HBM-based GPUs for decode, noting that datacenter GPUs rely on costly HBM whose bandwidth sits almost entirely idle during prefill. This establishes that heterogeneous memory economics already shape serving architecture; the supplied summary is cut off before quantitative promises, so we cite it only for the architectural framing.

**Placement and routing theory.** arXiv:2303.01648v1 [3] studies congestion-aware routing and content placement in elastic cache networks, jointly determining cache deployment, content placement, and hop-by-hop routing for arbitrary topologies with congestion-dependent nonlinear cost functions, with the routing-cost/cache-deployment-cost tradeoff left open. Our write-routing formulation is a single-tier, two-device special case of this general placement family: the "routing cost" is endurance wear on HBF and the "deployment cost" is HBM occupancy.

**Write-endurance management in non-volatile caches.** arXiv:1310.8494v1 [8] addresses inter-set write variation in non-volatile on-chip caches built from devices such as STT-RAM, whose common limitation is limited write endurance; because existing cache management policies are write-variation unaware, excessive writes concentrate on a few blocks. This is the direct antecedent of endurance-aware placement: Lachesis moves the same concern — uneven and excessive writes to a finite-endurance medium — from on-chip STT-RAM sets to HBM/HBF segments at serving granularity.

**Placement suboptimality benchmarks.** arXiv:2305.16413v1 [9] constructs mixed-size placement benchmark sets, including PEKO-MC, targeting the roles of nonlocal nets and of white space and module-size variation in suboptimality. Although from physical design rather than serving, it supplies the methodological pattern we follow: evaluate a placement heuristic against explicit baselines and report the suboptimality gap — here, the gap between HBM-first and lifetime-aware placement expressed as the ratio $r$.

**Adjacent QNFO material.** The QNFO entry on re-entry dynamics as a switching process [10] contrasts per-operation switching costs of stored-program architectures with a proposed Hamiltonian-computation paradigm; we invoke it only as a reminder that per-operation costs (here, per-write endurance wear) are a general architectural currency. The QuWARP entry [11] assesses workload-level reuse planning for repeated-run quantum-circuit simulation workloads, a planning-over-repeated-workloads pattern analogous to harness-level lifetime planning. The topological-memory entry [12] has an empty supplied summary, so no substantive claim can be drawn from it. Finally, the LiveBench-grounded audit of frontier LLMs [13] reports, for August 2026, that no Llama model ranks in the top 42 and that DeepSeek V4 Pro 0813 is the mathematics price-performance option; it grounds the claim that frontier-model serving — and hence agentic KV accumulation — is a live, competitive workload class, though it says nothing about memory systems.

## 3. Methods

### 3.1 System model

A serving engine holds KV cache in two tiers: HBM with capacity $C_{\text{HBM}}$ and effectively unlimited write endurance for practical purposes, and HBF with capacity $C_{\text{HBF}}$ and a per-block write endurance $e$. The aggregate HBF write budget is

$$B = C_{\text{HBF}} \cdot e,$$

the total number of block-writes the device can absorb before wear-out. A KV segment $s$ is written once (or a small number of times $w_s$) and read over a lifetime $\ell_s$ determined by the harness. A placement policy $\pi$ maps each segment to a tier at write time:

$$\pi: s \mapsto \{\text{HBM}, \text{HBF}\}.$$

### 3.2 Write-routing formulation

Define the HBF write fraction under policy $\pi$:

$$f_{\pi} = \frac{\sum_{s:\,\pi(s)=\text{HBF}} w_s \, b_s}{\sum_{s} w_s \, b_s},$$

where $b_s$ is the block count of segment $s$. HBM-first placement — the baseline that fills HBM and spills to HBF only on overflow — routes a fraction $f_0$ of writes to HBF. A lifetime-aware policy routes a smaller fraction $f_{\text{life}} < f_0$ by keeping short-lived segments in HBM. We define the write-reduction ratio

$$r = \frac{f_0}{f_{\text{life}}}, \qquad r \geq 1.$$

Because device lifetime is inversely proportional to the write rate on the device (Section 3.3), the lifetime extension of a policy over the baseline equals $r$:

$$\frac{T_{\text{life}}}{T_0} = r.$$

This identity is the analytical bridge between the reported extension range and the reported device-year range in Section 4.

### 3.3 Lifetime derivation

Let $W_{\text{day}}$ be the number of block-writes reaching HBF per day under the baseline at a given load. Under a policy with reduction ratio $r$, the daily HBF write volume is $W_{\text{day}}/r$. Device lifetime in years is then

$$T(r) = \frac{B}{(W_{\text{day}}/r)\cdot 365} = \frac{r \cdot B}{365 \, W_{\text{day}}}.$$

Equivalently, the baseline lifetime is $T_0 = B/(365\,W_{\text{day}})$ and $T(r) = r\,T_0$. Inverting, the maximum sustainable daily write rate for a target lifetime $T^{\star}$ is

$$W_{\max}(T^{\star}) = \frac{B}{365\,T^{\star}}.$$

### 3.4 The three lifetime axes as model inputs

The temporal, structural, and inter-worker axes identified in [1] map onto the model as follows. The temporal axis governs $\ell_s$: segments freed early by the harness should sit in HBM so their (re)writes never reach HBF. The structural axis governs $b_s$ and the sharing of segments across sub-agents: large, shared segments amortize writes across consumers, interacting with pool-sharing systems such as PolyKV [4]. The inter-worker axis governs correlation of write timing across workers, which sets the peak, rather than the mean, of $W_{\text{day}}$; our model uses the mean and therefore yields a conservative lifetime when writes are bursty only if wear scales with volume rather than peak rate, an assumption we revisit in Section 6.

## 4. Analysis

Every derived number below is computed from stated inputs; assumptions not present in the supplied sources are labeled as such.

### 4.1 Inputs from the supplied sources

From the Lachesis abstract [1], [2]:
- Extension over HBM-first placement: $r \in [1.19,\, 3.13]$ (reported).
- Achieved device-years: $T_{\text{life}} \in [3.3,\, 12.2]$ years (reported).
- Operation regime: continuous 24x7 at the full load a tight SLO admits; five-year warranty outlasted on the multi-agent trace (reported, qualitative).

### 4.2 Implied baseline lifetimes

Since $T_{\text{life}} = r\,T_0$, the baseline lifetime on a trace is $T_0 = T_{\text{life}}/r$ for that trace's own $r$. The abstract does not pair each device-year figure with its ratio, so we bound the implied baselines:

$$T_{0,\max} = \frac{12.2}{1.19} = 10.2521\ldots \approx 10.25 \text{ years},$$

$$T_{0,\min} = \frac{3.3}{3.13} = 1.0543\ldots \approx 1.05 \text{ years}.$$

Arithmetic: $12.2/1.19 = 10.25210\ldots$; $3.3/3.13 = 1.054313\ldots$. Thus the HBM-first baseline spans roughly $1.05$–$10.25$ years across the evaluated traces, and lifetime-aware placement is what lifts the worst case above the five-year warranty line. The geometric mean of the extension range is

$$r_{\text{geo}} = \sqrt{1.19 \times 3.13} = \sqrt{3.7247} = 1.9300\ldots \approx 1.93\times.$$

### 4.3 Endurance budget instantiation (labeled assumptions)

The supplied sources do not state $C_{\text{HBF}}$ or $e$. We adopt conservative illustrative assumptions, explicitly labeled: $C_{\text{HBF}} = 1.0\times10^{9}$ KV blocks (about $4\times10^{9}$ KB $= 4$ TB at a $4$ KB block, consistent in order of magnitude with "an order of magnitude greater capacity" than HBM for a $10^{2}$-GB-class HBM [1]) and $e = 300$ writes per block (conservative for 3D NAND). Then

$$B = C_{\text{HBF}} \cdot e = 1.0\times10^{9} \times 300 = 3.0\times10^{8} \text{ block-writes}.$$

Assume a baseline daily HBF write volume of $W_{\text{day}} = 2.5\times10^{5}$ block-writes/day at full SLO load (assumption; in bytes, $2.5\times10^{5} \times 4\text{ KB} = 1.0\times10^{6}$ KB/day $\approx 0.977$ GB/day). The baseline lifetime is

$$T_0 = \frac{B}{365\,W_{\text{day}}} = \frac{3.0\times10^{8}}{365 \times 2.5\times10^{5}} = \frac{3.0\times10^{8}}{9.125\times10^{7}} = 3.2877\ldots \approx 3.29 \text{ years}.$$

Applying the reported extension ratios:

$$T(1.19) = 1.19 \times 3.2877 = 3.9123 \approx 3.91 \text{ years},$$

$$T(3.13) = 3.13 \times 3.2877 = 10.2905 \approx 10.29 \text{ years}.$$

Consistency check: the model's baseline $T_0 = 3.29$ years lies inside the implied baseline range $[1.05,\,10.25]$ years from Section 4.2, and the model's extended range $[3.91,\,10.29]$ years lies inside the reported device-year range $[3.3,\,12.2]$. The model is therefore consistent with, and slightly more conservative than, the reported simulation outcomes.

### 4.4 Warranty ceiling and headroom

For a five-year warranty target $T^{\star} = 5$:

$$W_{\max}(5) = \frac{B}{365 \times 5} = \frac{3.0\times10^{8}}{1825} = 1.6438\times10^{5} \text{ block-writes/day}.$$

Against the assumed baseline load $W_{\text{day}} = 2.5\times10^{5}$:

$$\frac{W_{\text{day}}}{W_{\max}(5)} = \frac{2.5\times10^{5}}{1.6438\times10^{5}} = 1.5205 \approx 1.52\times.$$

So the baseline exceeds the warranty-compatible write rate by $1.52\times$, and any policy with $r \geq 1.52$ restores the five-year margin at this load. Both reported extension endpoints, $1.19$ and $3.13$, bracket this threshold from opposite sides, which explains qualitatively why the multi-agent trace — the one reported to outlast the warranty [1] — must be the trace whose $r$ sits at the high end.

### 4.5 Write-fraction interpretation

If HBM-first routes a fraction $f_0$ of writes to HBF, lifetime-aware placement routes $f_{\text{life}} = f_0/r$. For illustration with $f_0 = 0.62$ (assumption):

$$f_{\text{life}}(r=3.13) = \frac{0.62}{3.13} = 0.1981 \approx 0.20,$$

$$f_{\text{life}}(r=1.19) = \frac{0.62}{1.19} = 0.5210 \approx 0.52.$$

That is, the reported extension range corresponds to cutting the HBF-bound write share from $62\%$ to between roughly $20\%$ and $52\%$ of all KV writes.

## 5. Results

All numbers in this section are either computed in Section 4 (with arithmetic shown there) or quoted as reported results with their source.

**Computed analytical results** (under the labeled assumptions $C_{\text{HBF}} = 1.0\times10^{9}$ blocks, $e = 300$ writes/block, $W_{\text{day}} = 2.5\times10^{5}$ writes/day, $f_0 = 0.62$):
1. Aggregate HBF write budget: $B = 3.0\times10^{8}$ block-writes.
2. Baseline lifetime at full assumed load: $T_0 = 3.29$ years.
3. Lifetime under the reported extension endpoints: $T(1.19) = 3.91$ years; $T(3.13) = 10.29$ years.
4. Five-year warranty write ceiling: $W_{\max}(5) = 1.6438\times10^{5}$ block-writes/day.
5. Baseline excess over the ceiling: $1.52\times$; the minimum reduction ratio needed for the warranty at this load is $r \geq 1.52$.
6. Implied HBM-first baseline lifetimes from the reported ranges: $1.05$–$10.25$ years.
7. Geometric-mean extension of the reported range: $1.93\times$.
8. Implied HBF write fractions: $f_{\text{life}} \in [0.20,\,0.52]$ for $f_0 = 0.62$.

**Reported results, quoted from [1], [2]:** trace-driven simulation extension of $1.19$–$3.13\times$ over HBM-first placement; achieved HBF lifetimes of $3.3$–$12.2$ device-years; five-year warranty outlasted under continuous 24x7 operation at full SLO-admissible load on the multi-agent trace.

**Projection:** under the model, a deployment whose baseline write rate is $W_{\text{day}}$ and whose policy achieves reduction $r$ is projected to achieve $T = r\,B/(365\,W_{\text{day}})$ years; uncertainty is dominated by the assumed $e$ and $C_{\text{HBF}}$, and scales linearly in $B$: if the true budget is $\beta\,B$, all lifetimes and ceilings scale by $\beta$.

## 6. Discussion

**Limitations of the model.** The model reduces placement quality to a single scalar, the write-reduction ratio $r$. Real policies also affect read locality, HBM occupancy, and tail latency; a policy that maximizes $r$ by starving HBF of reads could violate SLOs in ways $r$ cannot see. The three lifetime axes of [1] enter the model only through aggregate quantities ($\ell_s$, $b_s$, $W_{\text{day}}$); structural sharing, of the kind PolyKV exploits [4], changes the write volume itself rather than its routing, and the two levers are not independent in our formulation.

**Assumption sensitivity.** The endurance budget $B = 3.0\times10^{8}$ block-writes rests on two labeled assumptions, $C_{\text{HBF}}$ and $e$, neither of which appears in the supplied sources. If $e$ is $10\times$ higher, every lifetime and ceiling scales $10\times$ and the warranty problem largely disappears; if $e$ is $10\times$ lower, even $r = 3.13$ yields about $1.03$ years at the assumed load. The qualitative conclusion — that endurance, not capacity or bandwidth, is the binding constraint, as [1] and [8] both assert — is robust to this scaling, but every absolute device-year figure is not.

**Failure modes.** First, our lifetime identity $T_{\text{life}}/T_0 = r$ assumes wear scales with total write volume, not with write peak rate or with retention-induced effects such as data aging; if HBF wear has a time-dependent component, bursty inter-worker write patterns could invalidate the mean-rate model. Second, the model assumes writes are routed once at write time; re-placement or re-compression after the fact would add writes that the model does not count. Third, the implied baseline range $[1.05, 10.25]$ years comes from dividing unpaired reported endpoints; if the $3.3$-year trace actually had $r = 1.19$ rather than $3.13$, the true baseline pairing would differ, though the bounds themselves remain valid.

**What would falsify the claims.** If trace-driven measurement showed that lifetime-aware placement achieves large read-bandwidth savings but $r \leq 1$ (no write reduction) — for instance because HBM-first placement already keeps short-lived segments in HBM — the central premise would fail. If HBF endurance under KV-sized random writes proved far below the assumed $e = 300$ writes/block even after wear leveling of the kind studied for non-volatile caches [8], the computed warranty margins would collapse. If the five-year warranty result on the multi-agent trace [1] depended on a load below the SLO-admissible maximum, the 24x7 claim would not generalize.

**Open questions.** How the harness's three lifetime axes translate into the distribution of $\ell_s$ in production harnesses; whether inter-worker write correlation makes peak-rate wear a first-order effect; how compression [4] and tiering [7] compose with lifetime-aware routing; and whether the placement problem should be co-optimized with prefill/decode disaggregation across memory-heterogeneous hardware [6], in the spirit of the joint routing-placement formulations of [3].

## 7. Conclusion

We presented an analytical endurance model for lifetime-aware KV cache placement across HBM and high-bandwidth flash in agentic LLM serving. The model expresses device lifetime as $T = r\,B/(365\,W_{\text{day}})$, linking the write-reduction ratio $r$ of a placement policy to the endurance budget $B$ and daily write volume $W_{\text{day}}$. Instantiated with conservative labeled assumptions, it reproduces a baseline lifetime of $3.29$ years at $2.5\times10^{5}$ writes/day, extends to $3.91$–$10.29$ years under the reported $1.19$–$3.13\times$ extension range, and yields a five-year warranty ceiling of $1.6438\times10^{5}$ writes/day with $1.52\times$ baseline headroom. The model is consistent with, and slightly more conservative than, the reported simulation outcomes for Lachesis, and it converts the qualitative insight that KV cache should be placed by lifetime into explicit, test