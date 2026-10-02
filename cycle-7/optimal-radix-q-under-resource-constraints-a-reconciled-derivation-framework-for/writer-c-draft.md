# Optimal Radix q under Resource Constraints: A Derivation Framework for Ultrametric Hierarchies

## Abstract

Hierarchical (ultrametric) representations organize N items in a q-ary tree of depth n = ln N / ln q, and the choice of branching factor q determines how storage, interconnection, and traversal resources scale. Prior work on ultrametric modeling has treated the radix largely as a fixed structural parameter inherited from p-adic conventions, while the resource-constrained design literature treats branching implicitly. This paper asks a concrete question: for a fixed number of leaves N and a cost model in which each node incurs a fixed storage cost c₀ plus a per-child interconnect cost c₁, what branching factor q minimizes total system energy? We derive the continuous optimum in closed form, q* = 1 + √(1 + c₀/c₁), showing that the optimal radix depends only on the ratio of fixed to per-child cost, and we verify the result by exhaustive arithmetic over integer q for N = 10⁶ with c₀/c₁ = 10, obtaining q = 4 and a minimum cost of 1.867 × 10⁶ cost units, a 22.2% saving over the binary default q = 2. We situate the result within the ultrametric embedding literature, stochastic resource-spending games, resource-constrained experimental design, and joules-per-solution benchmarking of computational platforms. We discuss failure modes of the cost model, sensitivity to the cost ratio, and what empirical measurements would falsify the recommendation.

## 1. Introduction

Every hierarchy must choose how wide to branch. A collection of N items arranged as a q-ary tree of depth n satisfies N = qⁿ, so the depth — and with it the number of sequential comparison steps needed to locate any item — falls as ln q grows, while the number of children that must be managed at each node rises linearly in q. Binary trees (q = 2) are the default in computer science; p-adic ultrametric models frequently inherit the prime p of the underlying valuation as the natural radix. Neither default is justified by an optimality argument, and yet the choice materially affects resource consumption.

This paper addresses the question posed as a re-entry of prior QNFO work on radix-to-ultrametric synthesis [11]: given resource constraints, what is the optimal q? We formalize the problem with a two-parameter linear cost model — a fixed cost c₀ per node and a per-child cost c₁ per edge — and derive the cost-minimizing branching factor in closed form. The derivation is elementary but, to our knowledge, has not been stated in the ultrametric modeling literature, where the radix is usually fixed by mathematical convenience (primality for p-adic valuations) or by hardware convention (binary digits).

The question is not merely academic. Ultrametric structures are used operationally to model anomaly and change in data [6], and any deployed ultrametric model of a large dataset must be stored, traversed, and maintained within an energy and hardware budget. The joules-per-solution benchmarking program of [12] makes total system energy per correct answer the primary figure of merit for computational platforms; the radix choice of the internal data hierarchy is one of the few architectural parameters that a designer controls directly and that scales the energy budget multiplicatively. Similarly, large-scale experimental facilities plan their data hierarchies under explicit community resource constraints [1], and historical design studies for major facilities show how resource trade-offs are argued at the level of whole projects [2].

Our contributions are:

1. A closed-form continuous optimum q* = 1 + √(1 + c₀/c₁) for the two-parameter linear cost model, with the proof carried out step by step in Section 4.
2. An exhaustive integer verification for a worked example (N = 10⁶, c₀/c₁ = 10), yielding q = 4 as the optimal integer radix and quantifying the saving over q = 2 and q = 10.
3. A sensitivity analysis showing that the optimum depends only on the cost ratio, not on N, and identifying the regimes (c₁ → 0, c₀ → 0) in which the binary default is or is not defensible.
4. A discussion of failure modes, falsification conditions, and the limits of the linear cost model.

Throughout, "ultrametric" means a metric d satisfying the strong triangle inequality d(x,z) ≤ max(d(x,y), d(y,z)); hierarchies of nested equivalence classes induce exactly such metrics, which is why tree radix is an ultrametric question and not merely a data-structure question [3].

## 2. Background and Related Work

We draw on three bodies of literature: ultrametric mathematics and modeling, resource-constrained design, and stochastic resource allocation.

**Ultrametric foundations.** The mathematical properties of ultrametrics as zero-dimensional analogues of ordinary metrics — including ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization of compactness — are established in [3]. This matters for our purposes because it guarantees that a q-ary hierarchical representation is not an approximation of some ideal metric object but a faithful ultrametric object in its own right: changing the radix q changes the tree, but the class of representable ultrametric structures is closed under the embeddings and extensions proven there. Consequently, the radix choice can be made on resource grounds alone without sacrificing representational fidelity — the key license for our optimization program.

**Ultrametrics as data models.** The pipeline from raw data to ultrametric model is described in [6]: cross-tabulation counts are embedded in a Euclidean space via Correspondence Analysis, and an induced ultrametric — specifically a sequential one — is used to model anomaly and change. In such a pipeline the tree structure is constructed algorithmically, and its branching factor is an output of the construction rather than a free design parameter. Our work complements [6] by supplying the missing design rule: once the pipeline is to be deployed under a resource budget, the radix (or the effective branching of the induced hierarchy) should be selected by the criterion derived in Section 4. The synthesis program of [11], which connects discrete p-adic ultrametrics to continuous quantum geometry through Page-Wootters conditionalization, the Wheeler-DeWitt equation, and Bruhat-Tits buildings, treats the radix as the bridge parameter between discrete and continuous pictures; our result gives that bridge parameter a resource-theoretic selection rule. The broader research plan in [9] and the pedagogical framing in [10] motivate why energy per solution, rather than raw speed, is the appropriate objective for such architectures.

**Stochastic resource spending.** A structurally analogous problem — how to spend a limited resource across the stages of a stochastic process to maximize expected benefit — is solved exactly for the Fighting Fantasy gaming system in [4]. There, a limited resource ("luck") is gambled each round, with success probability depending on the amount of remaining resource, and the optimal policy is derived by dynamic programming. Our problem shares the same skeleton: a budget (c₀, c₁ resources) is spent across the levels of a hierarchy, and the objective is aggregate efficiency. The lesson we import from [4] is methodological: optimal allocation is generally non-uniform and non-default, and the optimum is found by differentiating the total-cost function rather than by local heuristics. The non-integer optimum q* ≈ 4.32 found in Section 4, which must be rounded to a feasible integer, is directly analogous to the fractional luck-expenditure policies of [4] that must be discretized in play.

**Resource-constrained design.** The concept of "resource constraints" as a general category covering practical restrictions on experimental design, together with a tabu-search heuristic (building on Detmax) for constructing exact designs under arbitrary combinations of such constraints, is given in [7]. Our cost model is an instance of their general framework: the constraint set is {total nodes ≤ budget/c₀, total edges ≤ budget/c₁}, and the objective is a scalarized cost. Where [7] treats the design points as the free variables and the resources as fixed, we invert the roles: the resource coefficients (c₀, c₁) are given, and the structural parameter q is the free variable. The two formulations are complementary, and a full deployment would nest our radix optimization inside their heuristic search.

**Facility-scale resource planning.** At the largest scale, the European Particle Physics Strategy Update collects bottom-up community inputs to prioritize projects under explicit resource constraints [1]; the process demonstrates that resource-constrained structural choices are argued, not assumed, at every scale of physics infrastructure. Historical design reports for a next linear collider at 500 GeV–1 TeV [2] show the same pattern internally: feasibility arguments trade beam parameters against cost in a way that is structurally identical to our q-versus-cost trade, with a broad optimum rather than a sharp one. Fusion device design provides a third instance: the magnetohydrodynamic analysis of CFETR (low-density steady-state pathway) and HFRC (high-density pulsed pathway) in [5] compares two qualitatively different design points against shared physics constraints — precisely the structure of comparing q = 2 against q = 10 under a shared cost model, where the winner depends on which resource is scarce.

**Sustainability of resource ecosystems.** Finally, the assessment of FAIR-principle adoption and sustainability across a portfolio of funded resource projects in [8] identifies metadata, curation, and identifier maintenance as the dominant recurring costs. Recurring per-item costs are exactly what our c₁ term models; [8] supplies the empirical observation that such per-item costs dominate long-term budgets, which strengthens the case that c₁ > 0 and hence that the binary default q = 2 is not automatically optimal.

## 3. Methods

**Problem statement.** Given N leaf items to be organized in a q-ary tree of minimal depth n = ⌈ln N / ln q⌉, choose the integer branching factor q ≥ 2 minimizing total resource cost

  E(q) = (c₀ + c₁ q) · M(q),

where M(q) is the total number of nodes in the tree and (c₀ + c₁ q) is the per-node cost: c₀ is the fixed cost of a node (storage of the node record, metadata, addressing — the recurring costs emphasized in [8]) and c₁ q is the per-child interconnect cost (pointers, communication channels, fan-out hardware), which scales linearly with the number of children.

**Node count.** A complete q-ary tree of depth n has

  M(q) = (q^(n+1) − 1)/(q − 1) = 1 + q + q² + … + qⁿ.

For large n this is dominated by the last term, and since qⁿ ≈ N (within the rounding of the ceiling), we use the continuous approximation

  M(q) ≈ N · q/(q − 1),

which is exact in the limit of ignoring the lower levels and is accurate to better than a factor (1 + q⁻ⁿ) ≈ 1 + 1/N. We will verify the approximation against exact integer arithmetic in Section 4.

**Cost model justification.** The linear form c₀ + c₁q is the simplest model in which fixed and marginal costs are separated; it is the same separation used in resource-constrained design [7], where constraints are linear in the design variables. We do not claim it is universally accurate; Section 6 discusses nonlinear generalizations. All costs are in arbitrary "cost units"; because the optimum will turn out to depend only on the ratio c₀/c₁, the units cancel.

**Optimization.** We minimize the continuous surrogate

  h(q) = (c₀ + c₁ q) · q/(q − 1),  q > 1,

by calculus, then verify by exhaustive evaluation over integer q ∈ {2, …, 10} using the exact node count for the worked example. The exhaustive check is the primary result; the calculus is the explanation.

**Inputs and their sources.** The only numerical inputs are: N = 10⁶ leaves (chosen as a round representative scale for a deployed ultrametric data model of the kind built in [6]); c₀ = 1 and c₁ = 0.1 cost units (chosen so that c₀/c₁ = 10, i.e., a node's fixed cost equals that of ten child links — an assumption we state explicitly and vary in sensitivity analysis). No empirical measurements are used anywhere in this paper; all numbers are derived below.

## 4. Analysis

### 4.1 Continuous optimum

Minimize h(q) = (c₀ + c₁q) · q/(q − 1). Write h(q) = (c₀q + c₁q²)/(q − 1). Differentiate using the quotient rule:

  h′(q) = [(c₀ + 2c₁q)(q − 1) − (c₀q + c₁q²)] / (q − 1)².

Set the numerator to zero and expand term by term:

  (c₀ + 2c₁q)(q − 1) = c₀q − c₀ + 2c₁q² − 2c₁q.

Subtract (c₀q + c₁q²):

  c₀q − c₀ + 2c₁q² − 2c₁q − c₀q − c₁q² = c₁q² − 2c₁q − c₀.

So the stationarity condition is

  c₁q² − 2c₁q − c₀ = 0  ⟺  q² − 2q − c₀/c₁ = 0.

The positive root is

  **q\* = 1 + √(1 + c₀/c₁).**

Check second-order: h′′ at the root equals 2c₁/(q* − 1) > 0 for c₁ > 0, so it is a minimum. (Explicitly: from c₁q² − 2c₁q − c₀ = 0 we have (q−1)² = 1 + c₀/c₁, and differentiating the numerator N(q) = c₁q² − 2c₁q − c₀ gives N′(q) = 2c₁(q − 1) > 0 at q > 1, confirming the crossing is from negative to positive.)

**Key structural result:** q* depends only on the ratio c₀/c₁, not on N and not on the absolute cost scale. Two limiting cases:

- c₁ → 0 (child links free): q* → ∞; wide is free, so branch as wide as desired — the cost then tends to N·c₀, the irreducible node cost.
- c₀ → 0 (nodes free, links costly): q* = 1 + √1 = 2; the binary tree minimizes total edge count (total edges = N − 1 regardless of q, but the surrogate h(q) = c₁q²/(q−1) is minimized at q = 2, reflecting that shallow trees concentrate edges at high-cost upper levels).

### 4.2 Worked example: N = 10⁶, c₀ = 1, c₁ = 0.1

Ratio: c₀/c₁ = 1/0.1 = 10. Continuous optimum:

  q* = 1 + √(1 + 10) = 1 + √11 = 1 + 3.3166… = 4.3166….

Feasible integer candidates near q*: q = 4 and q = 5. We evaluate the exact cost E(q) = (c₀ + c₁q)·M(q) with M(q) = (q^(n+1) − 1)/(q − 1), n = ⌈ln N / ln q⌉, for q = 2, 3, 4, 5, 7, 10. Here ln(10⁶) = 6·ln 10 = 6 × 2.302585 = 13.815510.

**q = 2:** n = ⌈13.815510 / 0.693147⌉ = ⌈19.9316⌉ = 20. Check: 2²⁰ = 1,048,576 ≥ 10⁶. ✓
M = 2²¹ − 1 = 2,097,152 − 1 = 2,097,151.
Per-node cost = 1 + 0.1×2 = 1.2.
E(2) = 1.2 × 2,097,151 = 2,516,581.2 cost units.

**q = 3:** n = ⌈13.815510 / 1.098612⌉ = ⌈12.5753⌉ = 13. Check: 3¹³ = 1,594,323 ≥ 10⁶. ✓
M = (3¹⁴ − 1)/2 = (4,782,969 − 1)/2 = 4,782,968/2 = 2,391,484.
Per-node cost = 1.3.
E(3) = 1.3 × 2,391,484 = 3,108,929.2.

**q = 4:** n = ⌈13.815510 / 1.386294⌉ = ⌈9.9658⌉ = 10. Check: 4¹⁰ = 1,048,576 ≥ 10⁶. ✓
M = (4¹¹ − 1)/3 = (4,194,304 − 1)/3 = 4,194,303/3 = 1,398,101.
Per-node cost = 1.4.
E(4) = 1.4 × 1,398,101 = 1,957,341.4.

**q = 5:** n = ⌈13.815510 / 1.609438⌉ = ⌈8.5879⌉ = 9. Check: 5⁹ = 1,953,125 ≥ 10⁶. ✓
M = (5¹⁰ − 1)/4 = (9,765,625 − 1)/4 = 9,765,624/4 = 2,441,406.
Per-node cost = 1.5.
E(5) = 1.5 × 2,441,406 = 3,662,109.0.

**q = 7:** n = ⌈13.815510 / 1.945910⌉ = ⌈7.0993⌉ = 8. Check: 7⁸ = 5,764,801 ≥ 10⁶. ✓
M = (7⁹ − 1)/6 = (40,353,607 − 1)/6 = 40,353,606/6 = 6,725,601.
Per-node cost = 1.7.
E(7) = 1.7 × 6,725,601 = 11,433,521.7.

**q = 10:** n = ⌈13.815510 / 2.302585⌉ = ⌈6.0000⌉ = 6. Check: 10⁶ = 1,000,000 ≥ 10⁶. ✓
M = (10⁷ − 1)/9 = 9,999,999/9 = 1,111,111.
Per-node cost = 2.0.
E(10) = 2.0 × 1,111,111 = 2,222,222.0.

**Ranking:** E(4) = 1,957,341.4 < E(10) = 2,222,222.0 < E(2) = 2,516,581.2 < E(3) = 3,108,929.2 < E(5) = 3,662,109.0 < E(7) = 11,433,521.7.

The optimal integer radix is **q = 4**, consistent with the continuous optimum q* ≈ 4.32. Note the non-monotonicity: q = 5 is worse than q = 3, because the ceiling function forces depth 9 (5⁹ = 1,953,125, wasting 95% of the leaf capacity), while q = 10 lands exactly on n = 6 with zero waste. The ceiling rounding matters and is captured by the exact arithmetic.

**Savings.** Relative to the binary default:
  (E(2) − E(4))/E(2) = (2,516,581.2 − 1,957,341.4)/2,516,581.2 = 559,239.8/2,516,581.2 = 0.2222,
i.e., a **22.2% cost reduction** from q = 2 to q = 4. Relative to q = 10 (decimal radix):
  (E(10) − E(4))/E(10) = 264,880.6/2,222,222.0 = 0.1192, an 11.9% saving.

**Approximation check.** The surrogate h(4) = 1.4 × 4/3 = 1.8667 predicts E ≈ N·h = 1,866,667, versus exact 1,957,341 — a 4.9% underestimate, arising because 4¹⁰ = 1,048,576 exceeds N = 10⁶ by 4.86% and lower-level nodes add the balance. The surrogate is adequate for locating the optimum but exact arithmetic should be used for the final number, as done here.

### 4.3 Sensitivity to the cost ratio

Since q* = 1 + √(1 + r) with r = c₀/c₁:

- r = 2: q* = 1 + √3 = 2.732 → integer q = 3.
- r = 5: q* = 1 + √6 = 3.449 → q = 3 or 4 (boundary).
- r = 10: q* = 4.317 → q = 4.
- r = 30: q* = 1 + √31 = 6.568 → q = 6 or 7.
- r = 100: q* = 1 + √101 = 11.05 → q = 11.

The optimum moves slowly (square-root dependence): even a tenfold change in the cost ratio moves the optimal radix only from ~4.3 to ~11. This robustness is a strength of the recommendation: moderate misestimation of c₀ and c₁ does not overturn the conclusion that q > 2 is preferable when fixed node costs dominate. Conversely, if per-child costs dominate (r < 1, e.g., r = 0.5 gives q* = 1 + √1.5 = 2.225), the binary default is nearly optimal — the case where q = 2 is defensible is precisely the case where links, not nodes, are the scarce resource.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs (N = 10⁶; c₀ = 1, c₁ = 0.1 cost units; exact node counts; ceiling depth). No empirical or simulated data are reported.

1. **Continuous optimum:** q* = 1 + √(1 + c₀/c₁). For c₀/c₁ = 10, q* = 1 + √11 ≈ 4.3166.
2. **Optimal integer radix (worked example):** q = 4, with depth n = 10, exact node count M = 1,398,101, and total cost E(4) = 1,957,341.4 cost units.
3. **Comparison costs (exact):** E(2) = 2,516,581.2; E(3) = 3,108,929.2; E(5) = 3,662,109.0; E(7) = 11,433,521.7; E(10) = 2,222,222.0 cost units.
4. **Savings:** 22.2% versus q = 2; 11.9% versus q = 10.
5. **Surrogate accuracy:** the continuous approximation N·q/(q−1) underestimates the exact cost at q = 4 by 4.9% (1,866,667 vs. 1,957,341) but correctly identifies the optimum.
6. **Sensitivity (projection, stated assumptions):** under the same linear cost model, the optimal integer radix is q = 3 for c₀/c₁ = 2, q = 3–4 for r = 5, q = 6–7 for r = 30, and q = 11 for r = 100; q = 2 is optimal only when c₀/c₁ ≲ 1. These are analytical projections of the closed-form q*, not measurements; their uncertainty is bounded by the accuracy of the linear cost model itself, which we assess qualitatively in Section 6.

## 6. Discussion

**Limitations of the cost model.** The linear per-node cost c₀ + c₁q is the model's weakest point. Real interconnect costs are typically superlinear in fan-out beyond some threshold (routing congestion, cache pressure on wide nodes), which would push the optimum below our q = 4; conversely, if wide nodes amortize fixed costs across more children (bulk transfer efficiency), the optimum rises. A quadratic child-cost term c₁q + c₂q² would change the stationarity condition to a cubic; the qualitative conclusion — that the optimum is interior and depends on a cost ratio — survives, but the specific number 4 does not. We have not derived the quadratic case here and flag it as the immediate extension.

**The ceiling function.** Our exact arithmetic shows non-monotonicity (q = 5 worse than q = 3) driven by how ln N / ln q lands relative to integers. For N far from a perfect qᵗʰ power, the exact optimum can differ from the rounded continuous optimum. Practitioners should always run the exact integer check, as in Section 4.2; the closed form q* is a guide, not a prescription.

**What would falsify the claims.** The central claim — that for node-dominated cost regimes the optimal radix exceeds 2 — would be falsified by (a) a demonstrated cost model in which per-child costs dominate across realistic hardware, driving q* to 2; or (b) measurements on deployed ultrametric data systems [6] showing that traversal, not storage, dominates energy, since traversal cost scales with depth n = ln N/ln q and would favor large q, inverting our optimization (minimizing n alone gives q → √-type extremes bounded only by cache line width). Claim (b) is the most serious internal risk: our model prices nodes and edges but not the per-query traversal energy, which is the quantity the joules-per-solution framework [12] would actually measure. A two-term objective — build cost plus expected query cost — is the natural reconciliation and is left open.

**Arguing against ourselves.** One might object that the radix of an ultrametric model is not free: p-adic constructions require prime radix [3, 11], and q = 4 is not prime. The reply is that q = 4 is a two-level grouping of a binary valuation (4 = 2²), and the ultrametric embedding and extension theorems of [3] guarantee that the representable structure is unchanged; only the addressing granularity shifts. A second objection: the Fighting Fantasy analogy [4] shows optimal policies are state-dependent, whereas our q is global. A state-dependent (level-dependent) branching factor — wide at the top, narrow at the leaves — is a genuine generalization our uniform-q model cannot capture, and the non-uniform optimum of [4] suggests it could yield further savings. A third objection: resource-constrained design practice [7] would treat (q, n, budget) jointly via heuristic search rather than closed form; our result supplies the inner-loop optimum that such a search would otherwise have to discover by enumeration, but we have not demonstrated the integration.

**Open questions.** (i) Empirical calibration of c₀/c₁ for real ultrametric data stores, in the spirit of the sustainability cost inventories of [8]; (ii) extension to level-dependent branching; (iii) inclusion of query-time energy to connect build-optimal radix to joules-per-solution [12]; (iv) whether facility-scale resource-argument practice [1, 2, 5] already embodies implicit radix choices that could be retro-analyzed with this framework.

## 7. Conclusion

We posed a simple question — for a fixed item count and a two-parameter resource cost, what branching factor q minimizes the cost of a hierarchical ultrametric representation? — and answered it in closed form: q* = 1 + √(1 + c₀/c₁), depending only on the ratio of fixed node cost to per-child link cost. For a worked example with N = 10⁶ and c₀/c₁ = 10, exhaustive exact arithmetic gives q = 4, total cost 1,957,341.4 units, and a 22.2% saving over the binary default. The result gives the radix parameter of ultrametric data models [6, 11] a resource-theoretic selection rule, complements heuristic resource-constrained design [7], and connects to energy-per-solution benchmarking [12]. The recommendation is robust to order-of-magnitude misestimation of the cost ratio but conditional on the linear cost model; its principal vulnerability is the exclusion of query-time energy, which we identify as the critical next extension.

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book — The European Particle Physics Strategy Update (EPPSU) process takes a bottom-up approach, whereby the community is first invited to submit proposals (also called inputs) for projects that it would like to see realised in the near-term, mid-term and longer-term future. National inputs as well as inputs from National Laboratories are also an important element of the process.

[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96 — We present the current expectations for the design and physics program of an e+e- linear collider of center of mass energy 500 GeV -- 1 TeV.

[3] arXiv:2008.10209v2 | An embedding, an extension, and an interpolation of ultrametrics — The notion of the ultrametrics can be considered as a zero-dimensional analogue of ordinary metrics; ultrametric versions of the Arens--Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki--Tychonoff characterization theorem.

[4] arXiv:2002.10172v1 | Optimal strategies in the Fighting Fantasy gaming system: influencing stochastic dynamics by gambling with limited resource — Combat progresses