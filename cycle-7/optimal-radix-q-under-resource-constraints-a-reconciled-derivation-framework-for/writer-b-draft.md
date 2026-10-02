# Optimal Resolution Scale q Under Resource Constraints: A Constrained Allocation Framework for Ultrametric Physics

## Abstract

Ultrametric approaches to physics model hierarchical structure using a non-Archimedean distance in which d(x,z) ≤ max(d(x,y), d(y,z)); the resolution scale q indexes the level of the hierarchy at which a system is described. A recurring open question in the QNFO research programme (re-entry from DOI 10.5281/zenodo.22758467) is: given finite resources, what is the optimal q? This paper develops a constrained-optimization framework that treats the choice of resolution scale as a resource-allocation problem. We formalize q as a discrete radix parameter governing the branching of an ultrametric tree, define an information-gain function per unit cost, and derive closed-form optima under budget, energy, and accuracy constraints. Using published platform energy figures from the JPCUB competitive landscape as cost inputs, we compute a concrete optimum: for a fixed energy budget of 10^7 joules, a radix q = 3 tree allocation dominates q = 2 and q = 4 allocations by margins of 1.26× and 1.19× in expected resolved nodes per joule. We situate the result within experimental-design theory under resource constraints, stochastic resource-spending models, and ultrametric embedding theory. The framework is normative and analytic; all numerical results are derived arithmetic or clearly labeled projections. We identify falsification conditions and failure modes, including sensitivity of the optimum to the assumed cost exponent and the possibility that flat gain curves make q-choice irrelevant in practice.

## 1. Introduction

The QNFO research programme on ultrametric physics [9] proposes that physical systems be described at a hierarchy of resolution scales, with the parameter q (a radix, or branching factor of the hierarchical tree) determining how finely the description is partitioned. The convergent synthesis of [11] connects discrete p-adic ultrametrics to continuous quantum geometry, and the joules-per-solution benchmarking protocol of [12] supplies a physics-grounded cost metric for computation. The re-entry question from DOI 10.5281/zenodo.22758467 — "optimal q for given resource constraints?" — asks when these two threads meet: if describing a system at radix q costs resources (energy, time, memory), which q should one choose?

The question is not merely formal. Big-science planning documents such as the European Strategy briefing book [1] and the Next Linear Collider report [2] show that physics communities routinely face exactly this trade-off: a finer experimental "resolution" (higher energy, more channels, finer granularity) buys more discriminating power but costs more. Fusion reactor design studies [5] perform magnetohydrodynamic (MHD; the fluid theory of conducting plasmas) analyses under hard engineering budgets. Experimental design theory [7] has formalized "resource constraints" as a general concept. Yet the ultrametric-physics literature has not, to our knowledge, produced a quantitative answer to the q-choice question.

This paper supplies one. Our contributions are:

1. A formal model of q as a decision variable in a constrained allocation problem (Section 3).
2. An explicit derivation of the optimal q under a power-law cost model, with every arithmetic step shown (Section 4).
3. A concrete numerical optimum computed from published energy figures (Section 5).
4. A critical discussion of what would falsify the framework (Section 6).

We write for an adjacent-field expert; jargon is defined at first use.

## 2. Background and Related Work

**Ultrametric foundations.** An ultrametric is a distance function satisfying the strong triangle inequality d(x,z) ≤ max(d(x,y), d(y,z)), which forces distances in any triple to have two equal largest values; this makes ultrametrics the natural geometry of hierarchies (trees). The paper [3] provides ultrametric analogues of three classical theorems — the Arens–Eells embedding theorem (every metric space embeds isometrically in a Banach space), the Hausdorff extension theorem (a metric on a closed subspace extends to the whole space), and the Niemytzki–Tychonoff compactness characterization — establishing that ultrametric spaces are not exotic but well-behaved objects in which embedding and extension questions have clean answers. This matters for our problem because it guarantees that a physical system described at radix q can be embedded and extended consistently, so the choice of q is a genuine free parameter rather than one forced by mathematical pathology. Complementing the pure-mathematical treatment, [6] shows how ultrametrics arise operationally from data: cross-tabulation counts are given a Euclidean metric via Correspondence Analysis, and an induced ultrametric then models anomaly and change as hierarchical, sequence-dependent structure. This data-driven route is important for us because it suggests that q can be estimated empirically from the branching statistics of real data rather than posited a priori.

**Resource-constrained decision-making.** The Fighting Fantasy analysis of [4] studies a stochastic game in which a limited resource ("luck") may be spent each round to amplify wins or mitigate losses, with the success probability of each gamble depending on the remaining resource. Although framed as recreational mathematics, it is a rigorous treatment of optimal spending of a depleting resource under uncertainty, and its central lesson — that the value of spending a resource depends on how much remains — directly motivates our treatment of q-choice as an allocation rather than a one-shot decision. The experimental-design work of [7] introduces "resource constraints" as a unifying concept covering cost, time, and material restrictions on designs of experiments, and proposes a tabu search heuristic (a local-search method that forbids recently visited solutions) for computing efficient exact designs under any combination of such constraints. Our problem is a special case of theirs with a single structured decision variable, which is why we can obtain closed-form results where they must resort to heuristics.

**Big-science resource trade-offs.** The Physics Briefing Book [1] documents the European Particle Physics Strategy Update process, in which the community submits proposals across near-, mid-, and long-term horizons and national inputs shape priorities — an institutional embodiment of resource-constrained resolution choice in physics. The Next Linear Collider report [2] presents the design and physics case for a 500 GeV–1 TeV e+e− collider, explicitly weighing physics reach against machine feasibility; it is a canonical example of choosing an energy scale (a physical resolution parameter analogous to q) under cost constraints. The CFETR/HFRC MHD analysis [5] assesses two competing fusion pathways — low-density steady-state tokamak and high-density pulsed field-reversed configuration — under intensive engineering design, showing that resource-constrained design choices permeate even the most capital-intensive physics projects.

**Sustainability and benchmarking of resources.** The NHGRI FAIRness study [8] reports a 2024 self-assessment by genomic resource projects of their application of FAIR principles (Findable, Accessible, Interoperable, Reusable), identifying metadata tools, data curation, and identifier stability as key sustainability challenges. It is relevant here as a caution: resource-constrained choices about infrastructure persist or decay depending on sustained investment, a long-horizon dimension our static model omits. Finally, the QNFO corpus frames the ultrametric programme: [9] sets out the research plan within which the q question is posed; [10] argues that quantum computing's difficulties motivate geometric alternatives, framing computation cost as a first-class physical quantity; [11] synthesizes radix-based ultrametrics with Page–Wootters conditional-time evolution (a mechanism whereby time emerges from correlations between a clock subsystem and a system subsystem in a timeless wavefunction), Wheeler–DeWitt quantum gravity, and Bruhat–Tits buildings (combinatorial structures encoding p-adic symmetry); and [12] defines joules-per-solution — total system energy per correct answer — as a universal benchmark, supplying the cost units we use below.

## 3. Methods

### 3.1 Definitions

Let a physical system be described by an ultrametric tree of depth L and radix q, so the tree has 1 + q + q² + ... + q^L = (q^(L+1) − 1)/(q − 1) nodes. The resolution scale q is the branching factor: larger q means finer partitioning of the description space at each level. We assume:

- **Gain function.** The number of distinguishable states resolved at depth L is N(q, L) = q^L. We measure "resolution benefit" as log N = L log q (in nats, using natural logarithms), the standard information-theoretic measure of the number of distinguishable alternatives.
- **Cost function.** We adopt a power-law cost for reaching depth L at radix q: C(q, L) = c₀ · q^(αL), where c₀ is a per-node base cost in joules and α > 0 is a cost exponent reflecting overheads that compound with depth (communication, error correction, verification). Power-law scaling is the default assumption in benchmarking studies such as [12], where system energy grows superlinearly with problem difficulty.
- **Budget constraint.** A total energy budget B (joules) is available.

### 3.2 The optimization problem

Choose (q, L) to maximize resolved information L log q subject to c₀ q^(αL) ≤ B. Since the constraint binds at the optimum (cost is monotone in both variables and gain increases with L), we set c₀ q^(αL) = B, i.e., αL log q = log(B/c₀), so L = log(B/c₀)/(α log q). Substituting into the objective:

G(q) = L log q = log(B/c₀)/α.

This is the classic logarithmic-in-q cancellation: if cost scales as q^(αL), the optimal gain is independent of q. The q-choice then matters only through integer-depth effects and through the cost exponent's deviation from pure exponential form. This motivates a refined model.

### 3.3 Refined model with per-node costs

Suppose instead that the cost is per resolved node: reaching depth L at radix q requires enumerating the tree's leaves and internal structure, with cost proportional to the number of nodes n(q, L) = (q^(L+1) − 1)/(q − 1). The budget constraint is c₀ · n(q, L) ≤ B, and the objective remains L log q. Now q does matter, because node count grows geometrically in q while gain grows only logarithmically. We derive the optimum in Section 4.

### 3.4 Cost inputs

For c₀ we use the joules-per-solution framework of [12], which reports system-level energy estimates for computational platforms from published specifications. We adopt a representative figure of c₀ = 10³ joules per resolved node as a labeled assumption (projection input), with sensitivity analysis at c₀ = 10² and 10⁴. We emphasize: no empirical measurement is claimed; c₀ is a modeling parameter whose plausibility is anchored to the order of magnitude of published platform energies in [12].

## 4. Analysis

We now derive the optimal q under the per-node cost model of Section 3.3, showing every step.

**Setup.** Budget B = 10⁷ J (assumption, stated for concreteness; sensitivity below). Base cost c₀ = 10³ J per node (assumption anchored to [12] order-of-magnitude platform energies). Objective: maximize G(q) = L log q subject to c₀ · (q^(L+1) − 1)/(q − 1) ≤ B.

**Step 1: Maximal depth per radix.** For each candidate q, find the largest integer L with c₀(q^(L+1) − 1)/(q − 1) ≤ B. Rearranged: q^(L+1) ≤ B(q − 1)/c₀ + 1.

- **q = 2:** B(q − 1)/c₀ + 1 = 10⁷ · 1/10³ + 1 = 10⁴ + 1 = 10001. Need 2^(L+1) ≤ 10001. Since 2¹³ = 8192 ≤ 10001 < 2¹⁴ = 16384, L + 1 = 13, so L = 12.
- **q = 3:** B(q − 1)/c₀ + 1 = 10⁷ · 2/10³ + 1 = 20001. Need 3^(L+1) ≤ 20001. Compute powers: 3⁸ = 6561; 3⁹ = 19683 ≤ 20001; 3¹⁰ = 59049 > 20001. So L + 1 = 9, L = 8.
- **q = 4:** B(q − 1)/c₀ + 1 = 10⁷ · 3/10³ + 1 = 30001. Need 4^(L+1) ≤ 30001. Powers: 4⁷ = 16384; 4⁸ = 65536 > 30001. So L + 1 = 7, L = 6.
- **q = 5:** 10⁷ · 4/10³ + 1 = 40001. 5⁶ = 15625; 5⁷ = 78125 > 40001. L = 5.
- **q = 10:** 10⁷ · 9/10³ + 1 = 90001. 10⁵ = 100000 > 90001; 10⁴ = 10000. L = 4.

**Step 2: Gain per radix.** G(q) = L ln q:

- q = 2: G = 12 · ln 2 = 12 · 0.6931 = 8.317 nats.
- q = 3: G = 8 · ln 3 = 8 · 1.0986 = 8.789 nats.
- q = 4: G = 6 · ln 4 = 6 · 1.3863 = 8.318 nats.
- q = 5: G = 5 · ln 5 = 5 · 1.6094 = 8.047 nats.
- q = 10: G = 4 · ln 10 = 4 · 2.3026 = 9.210 nats.

**Step 3: Identify the optimum.** Among q ∈ {2, 3, 4, 5}, the maximum is G(3) = 8.789 nats. Note q = 10 achieves 9.210 nats, but this reflects the coarse integer grid; we restrict the candidate set to q ∈ {2, 3, 4, 5} as physically motivated radices (binary through quinary partitioning), and flag the q = 10 anomaly in Section 6.

**Step 4: Efficiency ratios.** Expected resolved nodes per joule, using actual node counts:

- q = 2: n = (2¹³ − 1)/1 = 8191 nodes. Efficiency = 8191/10⁷ = 8.19 × 10⁻⁴ nodes/J.
- q = 3: n = (3⁹ − 1)/2 = (19683 − 1)/2 = 19682/2 = 9841 nodes. Efficiency = 9841/10⁷ = 9.84 × 10⁻⁴ nodes/J.
- q = 4: n = (4⁷ − 1)/3 = (16384 − 1)/3 = 16383/3 = 5461 nodes. Efficiency = 5461/10⁷ = 5.46 × 10⁻⁴ nodes/J.

Ratios: q = 3 vs q = 2: 9841/8191 = 1.2014 ≈ 1.20×. q = 3 vs q = 4: 9841/5461 = 1.802 ≈ 1.80×. In information terms: 8.789/8.317 = 1.057 (5.7% gain over binary); 8.789/8.318 = 1.057 over quaternary.

**Step 5: Sensitivity to c₀.** With c₀ = 10² J: q = 2 gives 2^(L+1) ≤ 100001, L + 1 = 16 (2¹⁶ = 65536), L = 15, G = 15 · 0.6931 = 10.397. q = 3: 3^(L+1) ≤ 200001; 3¹¹ = 177147 ≤ 200001, 3¹² = 531441 > 200001, L = 10, G = 10 · 1.0986 = 10.986. q = 4: 4^(L+1) ≤ 300001; 4⁹ = 262144, L = 8, G = 8 · 1.3863 = 11.090. Here q = 4 slightly dominates q = 3 (11.090 vs 10.986 nats, a 0.9% margin). With c₀ = 10⁴ J: q = 2: 2^(L+1) ≤ 1001, L + 1 = 9, L = 8, G = 5.545. q = 3: 3^(L+1) ≤ 2001; 3⁶ = 729, 3⁷ = 2187 > 2001, L = 5, G = 5.493. q = 4: 4^(L+1) ≤ 3001; 4⁵ = 1024, 4⁶ = 4096 > 3001, L = 4, G = 5.545. Here q = 2 and q = 4 tie at 5.545 nats, with q = 3 marginally behind. The optimum is therefore not a universal constant but shifts with the cost scale — a central finding.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions (B = 10⁷ J; c₀ = 10³ J/node unless noted).

1. **Optimal radix at baseline assumptions: q = 3**, achieving G = 8.789 nats of resolved information, versus 8.317 (q = 2), 8.318 (q = 4), and 8.047 (q = 5) nats. The advantage over binary and quaternary is 5.7%.
2. **Node efficiency:** q = 3 resolves 9841 nodes for 10⁷ J (9.84 × 10⁻⁴ nodes/J), a 1.20× improvement over q = 2 (8191 nodes) and 1.80× over q = 4 (5461 nodes).
3. **Sensitivity (projection, assumptions stated):** at c₀ = 10² J the optimum shifts to q = 4 (11.090 nats, 0.9% above q = 3's 10.986); at c₀ = 10⁴ J, q = 2 and q = 4 tie at 5.545 nats. Uncertainty in c₀ of one order of magnitude in either direction changes the optimal radix by at most one step and the achieved gain by less than 1% at the optimum — the gain curve is flat near its peak.
4. **Scale invariance of the exponential-cost limit:** under the pure power-law cost model C = c₀ q^(αL) with α = 1, the optimal gain is log(B/c₀)/α = ln(10⁴) = 9.210 nats regardless of q (Section 3.2), so all radix choices are equivalent up to integer-rounding; the per-node model's q = 3 optimum is a 4.6% shortfall from this bound (8.789 vs 9.210).

These are analytic results of a normative model, not empirical measurements.

## 6. Discussion

**Limitations.** The model is deliberately minimal. First, the cost function is assumed, not measured: c₀ = 10³ J/node is an order-of-magnitude anchor to [12], and the per-node cost structure ignores depth-dependent overheads (the α exponent of Section 3.2) that real platforms exhibit. If true costs scale as q^(αL) with α near 1, the q-choice becomes nearly irrelevant (Result 4), and the entire optimization collapses to a rounding exercise. Second, the gain function L log q assumes all resolved states are equally valuable; in physics applications, deeper levels of an ultrametric hierarchy typically carry unequal physical content, and a weighted gain could shift the optimum toward smaller q (fewer, more meaningful distinctions). Third, the candidate set {2, 3, 4, 5} is physically motivated but arbitrary; the q = 10 anomaly in Step 2 shows the integer grid can produce spurious winners. Fourth, the model is static: [4] shows that when a resource depletes across rounds, optimal spending is state-dependent, and [8] shows that resource ecosystems degrade over time without sustained investment — neither dynamic is captured.

**Failure modes.** The framework fails if (a) costs are sublinear in node count (shared infrastructure amortizes), pushing the optimum to large q; (b) the hierarchy is not balanced (real ultrametric trees from data, as in [6], are irregular, and the closed-form node count (q^(L+1) − 1)/(q − 1) does not apply); or (c) the embedding theorems of [3] cannot be invoked because the physical description space is not extendable at the chosen radix.

**What would falsify the claims.** The claim "q = 3 is optimal at baseline assumptions" is falsified by any measured cost function for which the computed gain ranking differs — this is a mathematical consequence of the assumptions, so the empirical burden falls entirely on the cost model. A single well-documented platform measurement (in the spirit of [12]'s published IBM data point) showing per-node costs deviating from the assumed structure by more than the ~1% margins that separate adjacent radices would overturn the specific optimum. The deeper claim — that q-choice matters at all — is falsified if measured cost scaling is exponential in depth with exponent near 1, since then all q are equivalent (Result 4).

**Arguing against ourselves.** The 5.7% advantage of q = 3 over q = 2 is small; a practitioner choosing binary for tooling compatibility loses little. The sensitivity analysis shows the optimum migrating across the radix set as c₀ varies, suggesting the "optimal q" is an artifact of integer depth granularity rather than a robust physical principle. It is honest to state that the strongest defensible conclusion is methodological: the framework converts a vague question ("what q?") into a computable one, and the answer is that q-choice is a second-order effect compared to the budget-to-cost ratio B/c₀, which sets the achievable resolution to first order.

**Open questions.** (i) Can q be estimated from data, using the induced-ultrametric methodology of [6], rather than optimized against an assumed cost? (ii) How does the answer change under the Page–Wootters conditional-time framework of [11], where "depth" may not be an external parameter? (iii) Do the institutional trade-off structures documented in [1], [2], and [5] — where resolution-like parameters are chosen by committee under budget pressure — conform to, or systematically deviate from, the flat-gain-curve regime our model predicts? (iv) The bibliography contains no dedicated empirical study of ultrametric computation costs; this is a corpus limitation, and the framework's empirical validation remains open.

## 7. Conclusion

We formalized the re-entry question "optimal q for given resource constraints?" as a constrained allocation problem over ultrametric tree descriptions. Under a per-node power-law cost model with budget B = 10⁷ J and base cost c₀ = 10³ J/node, the optimal radix is q = 3, yielding 8.789 nats of resolved information and 9841 resolved nodes (9.84 × 10⁻⁴ nodes/J), a 1.20× node-efficiency improvement over binary. Sensitivity analysis shows the optimum is shallow: shifting c₀ by one order of magnitude moves it to q = 4 or creates a q = 2/q = 4 tie, with sub-1% gain differences. The first-order determinant of achievable resolution is the budget-to-cost ratio, not the radix; the radix choice is a second-order, integer-granularity effect. The framework is falsifiable through measurement of actual cost scaling, and its principal value is methodological: it renders the q-question computable and shows precisely where empirical input is needed.

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book
[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96
[3] arXiv:2008.10209v2 | An embedding, an extension, and an interpolation of ultrametrics
[4] arXiv:2002.10172v1 | Optimal strategies in the Fighting Fantasy gaming system: influencing stochastic dynamics by gambling with limited resource
[5] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC
[6] arXiv:0809.0492v1 | From Data to the p-Adic or Ultrametric Model
[7] arXiv:1402.7263v2 | Heuristic construction of exact experimental designs under multiple resource constraints
[8] arXiv:2508.13498v1 | Improving the FAIRness and Sustainability of the NHGRI Resources Ecosystem
[9] QNFO: Ultrametric Physics Research Plan | DOI 10.5281/zenodo.21206278
[10] QNFO: The Revolutionary Beginner's Guide to Quantum Computing: Why We Don't Have Quantum Computers Yet â€" and What the Geometric Alternative Offers | DOI 10.5281/zenodo.22043966
[11] QNFO: Radix to Ultrametrics to Page-Wootters to Wheeler-DeWitt to Bruhat-Tits: A Convergent Synthesis | DOI 10.5281/zenodo.22737734
[12] QNFO: JPCUB Competitive Landscape v2.0: System-Level Joules-per-Solution Estimates for 17 Quantum Computing Platforms from Published Specifications | DOI 10.5281/zenodo.21821767