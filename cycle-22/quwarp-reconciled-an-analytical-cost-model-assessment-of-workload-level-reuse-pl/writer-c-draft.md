# QuWARP Under the Microscope: A Cost-Model Analysis of Workload-Level Reuse Planning for Quantum Circuit Simulation

## Abstract

Quantum circuit simulation increasingly appears as repeated-run workloads — variational eigensolver sweeps, noisy multishot studies, and error-correction cycles — rather than isolated circuit executions. The QuWARP planner (arXiv:2609.23664v1) proposes workload-level reuse: identifying shared circuit prefixes across related tasks, materializing typed boundary artifacts, and reusing them when a narrow legality guardrail permits, with abstention and EXPLAIN-style auditability when reuse is unprofitable or unsafe. This paper provides an independent analytical treatment of that design. We formalize a two-parameter cost model — shared-prefix fraction f and materialization overhead fraction α — and derive closed-form expressions for per-run and amortized speedup, break-even conditions, and feasibility constraints. We show that the reported speedup range of 2.95x–32.84x implies shared-prefix fractions between roughly 0.66 and 0.97 under small overheads, that any reported speedup above 20x forces materialization overhead below ~3.2% of baseline run cost, and that amortized speedup over R-run workloads grows toward the ceiling 1/(1−f+α). We further analyze failure modes: prefix drift under parameter updates, legality violations at non-Clifford boundaries, and audit-trail overhead. Our results are model-derived characterizations of the published claims, not new measurements; we state this explicitly and identify what experiments would falsify the underlying reuse hypothesis.

## 1. Introduction

Classical simulation of quantum circuits is a foundational tool for the quantum computing stack: it underpins algorithm development, noise studies, and verification of quantum error correction (QEC) decoders before hardware time is spent. The dominant engineering tradition optimizes a single circuit execution — better gate kernels, better parallelism, better memory layouts. Yet practitioners rarely run a circuit once. A variational quantum eigensolver (VQE) experiment evaluates a parameterized ansatz hundreds or thousands of times with slowly changing parameters; a noise study executes the same logical circuit across many shot counts and noise realizations; a QEC study runs many rounds of nearly identical syndrome-extraction structure.

The QuWARP paper [1][2] observes that this repeated-run structure is an optimization opportunity that per-execution simulators leave on the table: closely related tasks share circuit prefixes, and if a simulator can checkpoint the state at the end of a shared prefix — an "exact typed boundary artifact" — later tasks can resume from it instead of re-simulating from the |0…0⟩ state. QuWARP wraps a bounded simulator execution surface (statevector mode and a stabilizer-hybrid mode), performs workload-level planning, guards each reuse with a continuation-legality check, abstains when reuse is unprofitable, and emits EXPLAIN-style traces so every reuse, abstention, or refusal is auditable. The reported headline result is a 2.95x–32.84x speedup over a per-task Qrack-based denominator on reuse-positive workloads.

This paper does not replicate QuWARP. Instead, it does what an adjacent-field expert reviewing a systems claim should do: build a minimal explicit cost model, derive what the reported numbers *require* to be true, characterize the planner's profitability envelope, and enumerate the conditions under which the approach must fail. Our contributions are:

1. A two-parameter analytic model (shared-prefix fraction f, materialization overhead fraction α) with closed-form speedup, break-even, and feasibility conditions (Section 3–4).
2. Explicit arithmetic showing what the reported 2.95x–32.84x range implies about f and α, including a hard feasibility constraint that rules out parameter combinations (Section 4).
3. An amortized multi-run analysis showing how speedup saturates with workload length R, with worked numbers (Section 4).
4. A falsifiability analysis: which measurements would refute the reuse hypothesis, and which structural failure modes (prefix drift, legality gaps, audit overhead) bound the gains (Section 6).

Throughout, we distinguish sharply between numbers we compute here from stated assumptions and numbers quoted from [1][2]. No new simulations or measurements are presented.

## 2. Background and Related Work

**Workload-level reuse in simulation.** The direct subject of this study is QuWARP itself [1][2], which frames simulation as a workload-planning problem rather than a per-circuit compilation problem. Its distinctive commitments are threefold: (i) reuse is planned at the workload level, across tasks, not within a single circuit; (ii) continuation legality acts as a narrow correctness guardrail — a reuse is permitted only when resuming from a boundary artifact is provably equivalent to fresh execution; and (iii) every decision is auditable via EXPLAIN-style traces with provenance and realized-cost summaries. The abstract reports 2.95x–32.84x speedups over a per-task Qrack denominator on reuse-positive workloads, across statevector and stabilizer-hybrid modes. Our analysis takes these claims as inputs and derives their internal requirements.

**Per-execution simulation engineering.** The complementary tradition optimizes single runs. De Matteis and de Renzis [7] survey fast quantum circuit simulation built on hardware-accelerated general-purpose libraries, emphasizing ease of use, implementation, and maintainability alongside raw parallelism — a reminder that simulator engineering trades generality against peak throughput, and that a workload planner like QuWARP is orthogonal to (and composable with) kernel-level acceleration. Bravyi et al.-style tractability questions are represented here by Ferris and Poulin's line of work [8], which connects the classical simulability of circuits to the precise notion of "classical simulation" required — sampling versus amplitude estimation — a distinction that matters directly for QuWARP's stabilizer-hybrid mode, where the cheap/simulable fragment must match what the downstream task actually consumes.

**Circuit-structure optimization.** Ostrowski and coauthors' structure-optimization method for parameterized circuits [3] simultaneously optimizes ansatz structure and parameters with small overhead; VQE sweeps of exactly this kind are QuWARP's prime reuse-positive workload, since successive structure/parameter evaluations produce circuits differing only in a few late gates. Ostrowski and Ostrowski's Krotov-control monotonicity proof [4] is a different variational setting (open-system control), but it illustrates the same structural phenomenon: iterative optimizers generate sequences of nearly identical circuit executions, which is precisely the workload shape a reuse planner targets. Cost-reduction work on quantum Boolean circuits [6] — multi-strategy synthesis of Positive-Polarity Reed-Muller expansions into multi-controlled Toffoli gates — operates at the synthesis level; its cost metric (gate count) is analogous to QuWARP's realized-cost summaries, but it rewrites circuits rather than reusing execution state, so the two are complementary layers of the same stack.

**Mapping and physical-level optimization.** TETRIS-Q [10] tackles NISQ circuit mapping with tiling-based transient-fault reduction and parallelism optimization, jointly handling SWAP overhead and decoherence exposure. This is the hardware-mapping analogue of QuWARP's software-simulation planning: both recognize that treating executions in isolation wastes an optimization dimension (fault exposure there, shared computation here). Notably, TETRIS-Q-style noise-aware mapping changes the circuit actually executed per run, which can erode prefix sharing — a failure mode we return to in Section 6.

**Energy accounting as a system metric.** The JPCUB line [11][12] proposes joules-per-solution as a physics-grounded, system-level benchmark across quantum platforms, with a competitive landscape built from published specifications. This matters for QuWARP because reuse planning changes total work performed per solution; a 2.95x–32.84x wall-clock speedup, if it translates to energy, would move a simulator's joules-per-solution proportionally, making workload-level reuse relevant to energy benchmarking, not just latency. The QWAV strategy document [11] frames the governance path for such a benchmark, indicating that reuse-aware simulation cost could become a reportable quantity in consortium settings.

**Scope exclusions.** The remaining bibliography items are outside our technical scope: the quantum electromagnetic circuits review [9] concerns Hamiltonian construction for physical circuits, not gate-level simulation; and the access-point simulation paper [5] was withdrawn by arXiv administrators for fictitious content and is cited here only to record its exclusion from our analysis. This leaves ten substantive sources, all discussed above; we note in Section 6 that the bibliography is thin on independent replications of QuWARP, which constrains how strongly any analysis — including ours — can support the underlying empirical claims.

## 3. Methods

### 3.1 Workload and planner model

Following [1][2], we model a workload as an ordered set of R tasks {T₁, …, T_R}, each task a circuit C_i = P_i · S_i, where S_i is a shared prefix (a gate sequence identical, up to the planner's equivalence notion, to prefixes of other tasks) and P_i is a task-specific suffix. The planner:

1. **Prefix identification:** computes, across the workload, the maximal shared prefixes and their lengths |S_i| relative to full circuit length |C_i|.
2. **Materialization decision:** for the first task executing a given prefix, decides whether to checkpoint the simulator state at the prefix boundary as a typed boundary artifact (exact statevector, or a stabilizer-hybrid boundary representation).
3. **Continuation legality check:** verifies that resuming from the artifact into task i's suffix is equivalent to fresh execution — e.g., the artifact's representation (statevector vs. stabilizer tableau fragment) supports all gates in P_i, and no measurement/adaptivity in P_i depends on information discarded at the boundary.
4. **Profitability test (abstention):** reuses only when the modeled cost of resuming is below the modeled cost of fresh execution; otherwise abstains and runs fresh.
5. **Auditing:** emits an EXPLAIN-style trace recording the decision, its provenance (which prefix, which artifact), and the realized cost.

We define the two model parameters:

- **f ∈ [0,1]: shared-prefix fraction** — the fraction of a representative task's execution cost that is covered by a shared prefix and therefore avoidable via reuse.
- **α ≥ 0: materialization overhead fraction** — the cost of creating (and, where applicable, reading) the boundary artifact, expressed as a fraction of one fresh task execution's cost.

Both are workload- and simulator-dependent; our analysis treats them as free parameters and derives what combinations are consistent with reported outcomes.

### 3.2 Cost model

Let T be the cost of one fresh task execution under the per-task denominator (the Qrack-based baseline of [1][2]). Then:

- **Fresh (no reuse):** each task costs T; workload cost C_fresh = R·T.
- **Reuse, per resumed task:** cost (1−f)·T + α·T = (1−f+α)·T. The first task in a prefix group pays T + α·T (fresh execution plus checkpoint write).

Per-run speedup for a resumed task:

  S_run = T / [(1−f+α)·T] = 1/(1−f+α).  (Eq. 1)

Amortized workload speedup over R tasks with a single prefix group (one materialization, R−1 resumptions):

  S_R = R·T / [T·(1+α) + (R−1)·T·(1−f+α)] = R / [1+α + (R−1)(1−f+α)].  (Eq. 2)

Break-even (reuse no worse than fresh) for a resumed task requires 1−f+α ≤ 1, i.e.:

  **f ≥ α.**  (Eq. 3)

Feasibility requires f ≤ 1 and α ≥ 0, so per-run speedup is bounded: S_run ≤ 1/α (approached as f→1) and S_run ≥ 1 whenever f ≥ α.

### 3.3 Stabilizer-hybrid mode

In stabilizer-hybrid execution, Clifford-fragment gates run in polynomial time on a tableau while non-Clifford gates force statevector expansion on a reduced support. A boundary artifact taken at a Clifford/non-Clifford interface can be exponentially cheaper to materialize than a full statevector artifact when the non-Clifford support is small. We model this qualitatively: the effective α for stabilizer-hybrid artifacts can be far smaller than for dense statevector artifacts, which is consistent with QuWARP evaluating both modes [1][2]; we do not assign it a number, since the source abstract gives no mode-split data.

### 3.4 Validity of the model

The model is deliberately minimal: it assumes homogeneous task costs, a single dominant prefix group, and additive overhead. Real workloads have heterogeneous task costs and multiple prefix groups; Eq. 2 then applies per group with R replaced by group size, and workload speedup is a weighted combination. We use the minimal model because the published abstract of [1][2] provides only a speedup range, and a two-parameter model is the richest model that range can constrain.

## 4. Analysis

All inputs below are either (a) quoted from the QuWARP abstract [1][2] or (b) assumptions we state explicitly. Every arithmetic step is shown.

### 4.1 What the reported speedup range implies

**Input (a):** reported speedups S ∈ {2.95, 32.84} on reuse-positive workloads [1][2].
**Input (b, assumption):** materialization overhead α = 0.05 (5% of a fresh run) as a mid-range guess for dense statevector artifacts; we also test α = 0.01.

From Eq. 1, S = 1/(1−f+α) ⟹ 1−f+α = 1/S ⟹ **f = 1 − 1/S + α**.

**Case S = 2.95, α = 0.05:**
- 1/S = 1/2.95 = 0.33898…
- f = 1 − 0.33898 + 0.05 = 0.71102.
- Interpretation: a 2.95x speedup at 5% overhead requires ~71.1% of each run's cost to sit in the shared prefix.

**Case S = 32.84, α = 0.05:**
- 1/S = 1/32.84 = 0.030451…
- f = 1 − 0.030451 + 0.05 = 1.019549.
- **f > 1 is infeasible.** Therefore, if the 32.84x workload ran in statevector mode with a dense artifact, α cannot be 0.05. Solving for the maximum feasible α with f ≤ 1: from f = 1 − 1/S + α ≤ 1, we need **α ≤ 1/S − 0 = 0.030451**. So the 32.84x result requires materialization overhead below ~3.05% of a fresh run's cost (or a shared-prefix structure even more extreme than f = 1, which is impossible, so the constraint binds on α).

**Case S = 32.84, α = 0.01:**
- f = 1 − 0.030451 + 0.01 = 0.979549.
- Interpretation: with 1% overhead, ~97.95% of the run's cost must be shared-prefix work. This is plausible for QEC-style workloads where the per-round syndrome-extraction structure dominates and only measurement decoding differs — but it is a strong requirement, and it is a *derived requirement*, not a measurement.

**Case S = 2.95, α = 0.01:**
- f = 1 − 0.33898 + 0.01 = 0.67102.
- ~67.1% shared prefix suffices at 1% overhead.

**Summary of the feasible (f, α) region implied by the reported range:** for the low end (2.95x), f ≳ 0.66–0.71 for α ∈ [0.01, 0.05]; for the high end (32.84x), f ≳ 0.98 and α ≤ 0.0305. The reported range is therefore internally consistent only if the best workload has near-total prefix sharing and very cheap artifact materialization — exactly the profile of stabilizer-hybrid QEC cycles, and hard to reach for dense statevector VQE sweeps.

### 4.2 Amortized speedup saturation

**Input (assumption):** R = 100 tasks in one prefix group; f = 0.90; α = 0.02.

Eq. 2: S_R = R / [1 + α + (R−1)(1−f+α)].
- 1−f+α = 1 − 0.90 + 0.02 = 0.12.
- (R−1)(0.12) = 99 × 0.12 = 11.88.
- Denominator = 1 + 0.02 + 11.88 = 12.90.
- S_100 = 100 / 12.90 = 7.7519… ≈ **7.75x**.

Cross-check against the per-run ceiling: S_run = 1/0.12 = 8.3333. As R→∞, S_R → 1/(1−f+α) = 8.33x; at R = 100 we already achieve 7.75/8.33 = 93.0% of the ceiling (7.7519/8.3333 = 0.93023). The one-time materialization cost (the 1+α term) is amortized quickly.

**Smaller workload, same parameters, R = 5:**
- (R−1)(0.12) = 4 × 0.12 = 0.48.
- Denominator = 1.02 + 0.48 = 1.50.
- S_5 = 5/1.50 = **3.3333x**.
So a 5-task sweep with 90% prefix sharing already beats the reported low end (2.95x), while a 100-task sweep approaches 8.33x. This shows the reported 32.84x cannot be explained by R = 100 amortization at f = 0.90; it requires f near 0.98 (Section 4.1) or larger effective prefix groups.

**Sensitivity to α at R = 100, f = 0.90:**
- α = 0.10: 1−f+α = 0.20; denominator = 1.10 + 99×0.20 = 1.10 + 19.80 = 20.90; S = 100/20.90 = 4.7847x.
- α = 0.30: 1−f+α = 0.40; denominator = 1.30 + 39.60 = 40.90; S = 100/40.90 = 2.4449x — **below the reported low end**, i.e., at 30% materialization overhead even 90% prefix sharing fails to reach 2.95x on a 100-task workload.
This is the quantitative core of QuWARP's abstention logic: the planner must refuse reuse whenever f < α (Eq. 3), and near the boundary the gains evaporate.

### 4.3 Break-even and abstention boundary

From Eq. 3, reuse is profitable iff f ≥ α. Concretely: if materializing and reading a boundary artifact costs 20% of a fresh run (α = 0.20), a workload must share at least 20% of its execution cost to break even — and to hit even 2x, from Eq. 1: 1−f+α = 0.5 ⟹ f = 0.5 + α = 0.70. Arithmetic: 1/S = 1/2 = 0.5; f = 1 − 0.5 + 0.20 = 0.70. So at α = 0.20, going from break-even to 2x requires moving from 20% to 70% prefix sharing — the profitability region is steep near the boundary, justifying an explicit abstention mechanism rather than always-reuse.

### 4.4 Legality guardrail as a correctness constraint

The continuation-legality check in [1][2] is a guardrail, not a performance feature, but it has a measurable cost dimension: every refused reuse is a fresh run (speedup 1.0 on that task). If a fraction q of candidate resumptions fails legality, the effective shared fraction becomes f_eff = (1−q)·f, and Eq. 1 applies with f_eff. Worked example: f = 0.90, α = 0.02, q = 0.30 (30% of candidates illegal):
- f_eff = 0.70 × 0.90 = 0.63.
- 1−f_eff+α = 1 − 0.63 + 0.02 = 0.39.
- S_run = 1/0.39 = 2.5641x.
Compare q = 0: S = 1/0.12 = 8.3333x. A 30% legality-failure rate cuts the per-run speedup by a factor of 8.3333/2.5641 = 3.25. This quantifies why the narrowness of the legality guardrail — how aggressively it refuses — is a first-order performance parameter, not merely a safety nicety.

### 4.5 Consistency check of the reported range

The ratio of the reported extremes is 32.84/2.95 = 11.13 (32.84 ÷ 2.95 = 11.1322…). Under our model, per-run speedup ratios between two workloads with the same α are (1−f₂+α)/(1−f₁+α). With α = 0.01 and f₁ = 0.671 (the 2.95x case), matching 32.84x requires 1−f₂+α = 0.030451 ⟹ f₂ = 0.979549 (Section 4.1). The difference f₂ − f₁ = 0.979549 − 0.67102 = 0.30853 — about 31 percentage points of additional shared-prefix fraction — separates the two ends of the reported range. This is a coherent spread across workload classes (VQE sweeps vs. QEC cycles) rather than an anomaly, which supports the plausibility of the reported range *as a range*, while flagging that the top end is achievable only under near-total sharing and sub-3% overhead.

## 5. Results

All numbers in this section are computed in Section 4 from the stated inputs; none are new measurements. Reported speedups (2.95x, 32.84x) are quoted from [1][2]; everything else is model-derived.

**R1. Implied shared-prefix fractions (Eq. 1, α assumed).**
- α = 0.05: S = 2.95 ⟹ f = 0.71102; S = 32.84 ⟹ f = 1.019549, **infeasible**.
- α = 0.01: S = 2.95 ⟹ f = 0.67102; S = 32.84 ⟹ f = 0.979549.

**R2. Hard overhead constraint at the top end.** The 32.84x result requires α ≤ 1/32.84 = 0.030451 (≈3.05% of a fresh run) for any feasible f ≤ 1. Any workload achieving >20x under this model has α < 1/20 = 0.05 by the same derivation (1/S = 0.05 at S = 20).

**R3. Amortization (Eq. 2; f = 0.90, α = 0.02 assumed).**
- R = 5: S = 3.3333x. R = 100: S = 7.7519x. Ceiling S_run = 8.3333x; R = 100 achieves 93.02% of the ceiling.

**R4. Overhead sensitivity (R = 100, f = 0.90).**
- α = 0.10 ⟹ S = 4.7847x. α = 0.30 ⟹ S = 2.4449x, below the reported low end of 2.95x.

**R5. Break-even and steepness (Eq. 3, Eq. 1).** Reuse is profitable iff f ≥ α. At α = 0.20, break-even is f = 0.20 and 2x requires f = 0.70.

**R6. Legality-refusal cost (Section 4.4; f = 0.90, α = 0.02).** A 30% legality-refusal rate (q = 0.30) reduces effective sharing to f_eff = 0.63 and per-run speedup from 8.3333x to 2.5641x — a 3.25x degradation attributable purely to guardrail strictness.

**R7. Range coherence.** The reported extremes differ by a factor of 11.1322 in speedup, which under the model corresponds to ≈0.30853 (≈31 percentage points) of additional shared-prefix fraction at α = 0.01 — a plausible spread across workload classes, contingent on the top-end workload having near-total sharing and sub-3% materialization overhead.

**Projection (labeled as such).** If a future QEC-style workload exhibits f = 0.98 and stabilizer-hybrid materialization at α = 0.005, Eq. 1 projects S_run = 1/(1−0.98+0.005) = 1/0.025 = **40x**, with uncertainty dominated by the assumed f and α; if either parameter is off by 0.01 (f = 0.97 or α = 0.015), the projection drops to 1/0.035 = 28.57x or 1/0.035 = 28.57x respectively — i.e., roughly ±30% sensitivity to one-point parameter errors. This projection is offered as a testable prediction of the model, not a result.

## 6. Discussion

**Limitations of this analysis.** Our model is a two-parameter abstraction. Real workloads have heterogeneous task costs, multiple prefix groups with different f and α, and planner overhead (prefix identification, legality checking, trace emission) that we folded into α but which may scale superlinearly with workload size. The reported speedups in [1][2] are against a specific Qrack-based per-task denominator; a different baseline simulator with different per-run costs changes every derived number in Section 4. Most importantly, we had access only to the abstract of [1][2]; workload details, mode splits, and measurement methodology are unknown to us, so our "implied f and α" are inferences under stated assumptions, not recovered parameters.

**Failure modes.** (1) *Prefix drift:* in VQE-style loops, structure-optimization methods [3] can change the ansatz itself between iterations, splitting prefixes; TETRIS-Q-style noise-aware mapping [10] can insert different SWAPs per run for the same logical circuit, destroying syntactic prefix sharing unless the planner's equivalence notion is robust to commutation-based reordering. (2) *Legality gaps:* stabilizer-hybrid boundaries are only legal when the post-boundary computation consumes exactly what the artifact preserves; adaptive circuits (measurement-dependent branching, decoder feedback in QEC) can make reuse silently wrong if the guardrail is incomplete — the cost of a missed illegality is not slowdown but wrong answers. (3) *Audit overhead:* EXPLAIN-style traces with provenance and realized-cost summaries [1][2] are I/O; at high task counts, trace volume could dominate α, and our α = 0.30 sensitivity case (R4: 2.4449x) shows how quickly large overheads erase the gains. (4) *Abstention miscalibration:* the steep profitability boundary (R5) means a planner that overestimates f by even ~10 percentage points near α ≈ 0.2 can flip from profitable to unprofitable.

**Arguing against ourselves.** A skeptic could say the model is unfalsifiable as stated: any observed speedup maps to some (f, α), so the model "explains" everything. The reply is that the model makes *joint* constraints — R2's α ≤ 0.0305 for 32.84x is a hard, falsifiable requirement: if independent measurement of the 32.84x workload's materialization cost found α > 0.0305 with f ≤ 1, our model (and possibly the reported speedup's attribution to reuse) would be refuted. Second, a skeptic could note that near-total prefix sharing (f ≈ 0.98) makes the "planning" trivial — if 98% of the work is identical, almost any checkpointing scheme wins, and QuWARP's planner machinery is overkill. This is a fair challenge; the planner's real value should show in *intermediate* regimes (f ≈ 0.5–0.8), where abstention and legality checking decide profitability, and in auditability, which a naive checkpoint cache does not provide. Third, the bibliography available to us contains no independent replication of QuWARP's numbers, and one source [5] is a withdrawn, fictitious-content paper we explicitly exclude; our analysis therefore characterizes the *claims* of [1][2] rather than independently corroborating them.

**What would falsify the reuse hypothesis.** (i) Workloads where measured f is high but realized speedup is near 1 — indicating unmodeled overheads dominate. (ii) Speedups exceeding 1/α_measured with f ≤ 1 — impossible under Eq. 1, indicating the denominator baseline was not per-task-fresh. (iii) Legality-refusal rates near zero combined with incorrect simulation outputs — indicating the guardrail is vacuous. (iv) Flat S_R in R (no amortization trend) — indicating per-task reuse decisions are not actually amortizing a one-time materialization.

**Open questions.** What is the measured distribution of f across VQE, noise-study, and QEC workload classes? How does α scale with qubit count for dense vs. stabilizer-hybrid artifacts? Can prefix equivalence be defined compositionally so that mapping-level variations [10] preserve sharing? And does reuse planning improve system-level energy metrics such as joules-per-solution [12], where reduced total work should translate directly, making workload-level reuse a reportable benchmark dimension [11]?

## 7. Conclusion

We presented an independent cost-model analysis of QuWARP's workload-level reuse planning for quantum circuit simulation [1][2]. A two-parameter model — shared-prefix fraction f and materialization overhead fraction α — yields closed-form speedup, break-even (f ≥ α), and feasibility conditions. Applied to the reported 2.95x–32.84x range, the model shows the low end requires ~67–71% prefix sharing at 1–5% overhead, while the high end is feasible only with ~98% sharing and materialization overhead below 3.05% of a fresh run — a profile consistent with stabilizer-hybrid QEC-style workloads and hard to reach with dense statevector artifacts. Amortization analysis shows speedup saturates at 1/(1−f+α) with 100-task workloads already at ~93% of ceiling for representative parameters, and sensitivity analysis shows 30% overhead drives even 90% sharing below the reported low end. The legality guardrail, often framed as pure safety, carries a quantified performance cost: a 30% refusal rate cuts per-run speedup 3.25x in our worked example. The analysis sharpens QuWARP's claims into falsifiable requirements, identifies prefix drift and guardrail strictness as the dominant risks, and frames reuse-aware simulation cost as a candidate dimension for emerging system-level benchmarks. Future work should measure f and α distributions empirically and test the model's projections in intermediate-sharing regimes where planning, rather than trivial sharing, does the work.

## References

[1] TITLE: arXiv Query: search_query=&id_list=2609.23664&start=0&max_results=1 — ABSTRACT: Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error correction (QEC) cycles revisit closely related structure across many runs. Existing simulators optimise individual executions well, but they largely ignore cross-task shared state and therefore repeat work that could be reused safely. We propose QuWARP, a planner-based workload optimiser for a bounded state of the art simulator execution surface: it performs workload-level planning over related tasks, identifies shared prefixes, and chooses when to materialize exact typed boundary artifacts for later reuse across the evaluated statevector mode, and stabilizer-hybrid mode. Its planner treats continuation legality as a narrow correctness guardrail, abstains when reuse is unprofitable, and keeps each reuse, abstention, or refusal decision auditable through EXPLAIN-style traces, meaning inspectable planner reports with provenance and realized-cost summaries. Across real world quantum application workloads

[2] arXiv:2609.23664v1 | QuWARP: A Workload-Aware Reuse Planner for simulating Quantum Circuits — Quantum circuit simulation often appears as repeated-run workloads rather than isolated circuits: variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error correction (QEC) cycles revisit closely related structure across many runs. Existing simulators optimise individual executions well, but they largely ignore cross-task shared state and therefore repeat work that c

[3] arXiv:1905.09692v3 | Structure optimization for parameterized quantum circuits — We propose an efficient method for simultaneously optimizing both the structure and parameter values of quantum circuits with only a small computational overhead. Shallow circuits that use structure optimization perform significantly better than circuits that use parameter updates alone, making this method particularly suitable for noisy intermediate-scale quantum computers. We demonstrate the met

[4] arXiv:2006