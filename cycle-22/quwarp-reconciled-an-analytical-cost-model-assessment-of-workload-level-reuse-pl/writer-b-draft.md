# Workload-Level Reuse Planning in Quantum Circuit Simulation: An Analytical Triage of QuWARP

## Abstract

Classical simulation of quantum circuits is increasingly dominated by repeated-run workloads — variational eigensolver sweeps, multishot noise studies, and error-correction cycle rehearsals — in which many executions share substantial circuit structure. The QuWARP system (arXiv 2609.23664) claims 2.95x–32.84x speedups over a per-task Qrack baseline by planning reuse of shared circuit prefixes across tasks, materializing typed boundary artifacts only when profitable, and abstaining otherwise. This paper provides an independent analytical triage of that claim: we construct a simple amortized-cost model of prefix reuse, derive closed-form expressions for speedup as a function of prefix-sharing fraction, task count, and materialization overhead, and check whether the reported speedup range is consistent with plausible workload parameters. We find that the claimed interval corresponds to shared-prefix fractions of roughly 0.67 to 0.98 at a 100-task workload scale, and that reuse remains profitable down to small task counts only when artifact materialization cost is a small multiple of per-task prefix cost. We also assess the auditability design (EXPLAIN-style planner traces) as a correctness guardrail, and identify memory-footprint and legality-checking costs as the principal failure modes. The analysis is arithmetic and model-based; no new simulations are performed, and all projected figures are labeled as such with stated assumptions.

## 1. Introduction

Quantum circuit simulators — programs that compute the classical description (e.g., a full statevector, or a stabilizer tableau) of a quantum circuit's output — are the workhorse of quantum algorithm development. A statevector simulator stores the full complex amplitude vector of an *n*-qubit system, which contains 2^n amplitudes; a stabilizer simulator exploits the Gottesman–Knill structure of Clifford circuits to represent certain states in polynomial space. Most simulator engineering optimizes a *single* execution: gate fusion, kernel tuning, GPU offload, and circuit rewriting all target one circuit at a time.

Yet real usage is rarely one circuit at a time. A variational quantum eigensolver (VQE) sweep evaluates the same ansatz circuit at hundreds of parameter settings; a noisy multishot study repeats a circuit under sampled noise realizations; quantum error correction (QEC) cycle simulations repeat stabilizer-measurement rounds with small variations. Across these runs, large circuit prefixes — the gates before the first parameterized or noise-dependent gate — are bit-identical, and their simulated state is deterministic. Re-executing them is redundant work.

QuWARP [1, 2] proposes a planner that sits above a bounded simulator execution surface (statevector and stabilizer-hybrid modes of Qrack), identifies shared prefixes across a workload, and decides per task whether to (a) materialize an exact typed boundary artifact — a saved intermediate state with metadata — for later reuse, (b) reuse an existing artifact, or (c) abstain and execute directly. Crucially, the planner treats "continuation legality" (whether a saved state can be correctly continued into a given task) as a narrow correctness guardrail, and emits auditable traces for every decision.

This paper does not re-implement QuWARP. Instead, it performs an analytical triage: is the claimed 2.95x–32.84x speedup range *arithmetically consistent* with a simple, transparent cost model of prefix reuse? What parameter regimes does it imply? Where are the failure modes? The contribution is threefold: (i) a closed-form amortized-cost model for prefix-reuse planning; (ii) explicit numerical reconciliation of the reported speedup interval with model parameters; (iii) a critical assessment of the auditability and abstention design, including what evidence would falsify the claims.

## 2. Background and Related Work

QuWARP itself is described in the arXiv query record and the paper entry [1, 2], which report a planner-based workload optimiser performing workload-level planning over related tasks, identifying shared prefixes, and choosing when to materialize exact typed boundary artifacts for reuse across statevector and stabilizer-hybrid modes, with EXPLAIN-style auditable traces and reported 2.95x–32.84x speedups over a direct per-task Qrack denominator on reuse-positive workloads. The qualifier "reuse-positive" is important: it conditions the headline numbers on workloads where reuse is profitable, a selection we examine critically in Section 6.

Structure optimization for parameterized quantum circuits [3] is complementary: it co-optimizes circuit structure and parameter values for NISQ devices at small overhead. Its relevance here is that structure-optimized ansätze tend to be *shallow and repetitive across parameter settings*, which is precisely the regime where large shared prefixes arise; QuWARP's reuse planning targets the simulation cost of exactly such sweeps.

The Krotov-algorithm monotonicity analysis [4] addresses open-quantum-system variational control, proving monotonic convergence of a widely used optimal-control method. Open-system dynamics underlie noisy multishot simulation workloads: each noise realization perturbs the circuit, and the shared prefix is the portion before the first noise insertion. The more control/noise structure repeats across iterations, the more reuse planning pays.

The withdrawn submission [5] — withdrawn by arXiv administrators for fictitious content and pseudonymous submission — serves as a cautionary datapoint for this literature scan: automated research triage must be alert to retracted or fabricated entries in bibliographic feeds, and we cite it here only to document that it was detected and excluded from any substantive reliance.

Multi-strategy quantum cost reduction of Boolean circuits [6] synthesizes low-cost quantum circuits from Positive Polarity Reed-Muller expansions using Multiple-Control Toffoli gates. This is *gate-level* cost reduction — reducing the work per circuit — whereas QuWARP is *workload-level* cost reduction: even an optimally synthesized circuit, when re-executed hundreds of times with a shared prefix, wastes the prefix work. The two are orthogonal and composable.

Hardware-accelerated simulation with general-purpose libraries [7] shows that simulator performance has historically come from exploiting parallelism, often via special-purpose libraries, with a stated focus on ease of use and maintainability in Python-centric software stacks. QuWARP's contribution is deliberately *not* kernel-level speed; it is a planning layer above such kernels, which means its gains should compose with, not compete against, hardware acceleration.

The simulability analysis of [8] frames classical simulation of quantum circuits around the precise notion of "classical simulation" required — exact statevector output versus weak sampling. This matters directly for QuWARP: reuse of an exact typed boundary artifact is only legal when the downstream task's required simulation notion (and mode: statevector vs. stabilizer-hybrid) matches the artifact's type. The "continuation legality" guardrail in [1, 2] operationalizes exactly this typing discipline.

The review of quantum electromagnetic circuits [9] covers Hamiltonian construction for general (possibly dissipative) circuits. While it concerns physical superconducting hardware rather than classical simulation, it contextualizes the QEC and control workloads whose repeated-cycle structure motivates workload-level reuse.

From the QNFO corpus, TETRIS-Q [10] optimizes NISQ qubit mapping by jointly minimizing SWAP overhead and decoherence exposure, criticizing compilers that optimize routing and placement independently. The analogy to QuWARP is direct: both argue that optimizing components independently (per-task, or per-placement) leaves cross-component or cross-task structure unexploited.

The QWAV strategy document [11] and the JPCUB competitive landscape [12] concern energy benchmarking governance — joules-per-solution as a physics-grounded universal metric. They relate here because reuse planning changes the *energy accounting* of simulation workloads: if a workload's energy cost is dominated by redundant prefix execution, workload-level planning is an energy optimization as much as a time optimization, and any claimed speedup should ideally be restated in energy terms under the JPCUB-style protocol. The QuiX Quantum due-diligence report [13] exemplifies multi-source verification practice; we adopt a similar skeptical, source-checking posture toward the single-source speedup claims of [1, 2].

## 3. Methods

Our method is analytical triage: we build a minimal cost model, state every input, and derive results by explicit arithmetic. We define:

- **Task**: one circuit execution within a workload.
- **Prefix**: the maximal initial segment of gates shared bit-for-bit across all tasks in a group.
- **Boundary artifact**: the saved simulator state at the prefix boundary, with type metadata (statevector or stabilizer tableau).
- **Materialization**: the act of writing the artifact to storage (RAM or disk).

**Model inputs** (all stated per experiment below):

- N: number of tasks in the workload.
- C: per-task direct execution cost (time), normalized to 1 unit unless stated.
- f: fraction of per-task cost attributable to the shared prefix (0 ≤ f ≤ 1).
- M: cost of materializing one boundary artifact, expressed as a multiple of C.
- r: cost of loading/restoring an artifact relative to executing the prefix, per reuse (0 ≤ r ≤ 1).
- δ: legality-check overhead per reuse decision, relative to C.

**Direct (no-reuse) total cost**: D = N·C.

**Planned (reuse) total cost**: the prefix is executed once (cost f·C), one artifact is materialized (cost M·C), and each of the N tasks pays the suffix cost (1−f)·C plus a restore cost r·f·C plus legality overhead δ·C. Thus:

P = f·C + M·C + N·[(1−f)·C + r·f·C + δ·C]

**Speedup** S = D / P. With C = 1:

S(N, f, M, r, δ) = N / [f + M + N·(1 − f + r·f + δ)]

We use this model to (i) recover the implied f-range behind the reported 2.95x–32.84x, (ii) compute break-even task counts, and (iii) compute memory footprints for materialized statevector artifacts. We take the reported speedup interval from the abstract of [1, 2] as the only empirical input, treating it as a claim to be checked for consistency, not as verified data.

## 4. Analysis

**Step 1: Baseline memory footprint of a statevector artifact.** An *n*-qubit statevector has 2^n complex amplitudes. Using the standard double-precision complex128 representation (16 bytes per amplitude):

- n = 30: 2^30 = 1,073,741,824 amplitudes; × 16 bytes = 17,179,869,184 bytes = 16 GiB (since 17,179,869,184 / 2^30 = 16).
- n = 36: 2^36 = 68,719,476,736; × 16 = 1,099,511,627,776 bytes = 1 TiB.
- n = 40: 2^40 = 1,099,511,627,776; × 16 = 17,592,186,044,416 bytes = 16 TiB.

So materialized statevector artifacts are feasible in RAM up to roughly n ≈ 32–34 on a large workstation (e.g., n = 34: 2^34 × 16 = 274,877,906,944 bytes ≈ 256 GiB) and require distributed or NVMe storage beyond. This bounds the artifact-materialization strategy: it is a mid-sized-workload tool, not a frontier-n tool.

**Step 2: Recover implied prefix-sharing fraction.** Assume the favorable regime: negligible overheads M = r = δ = 0 (an upper bound on S). Then:

S = N / [f + N(1−f)] = N / [N − f(N−1)]

Solving for f: f = N(1 − 1/S) / (N − 1).

Take N = 100 tasks (a modest VQE sweep).

- Lower reported speedup S = 2.95: 1/S = 0.338983; 1 − 1/S = 0.661017; N × that = 66.1017; divide by (N−1) = 99: f = 66.1017 / 99 = 0.6677.
- Upper reported speedup S = 32.84: 1/S = 0.030451; 1 − 1/S = 0.969549; × 100 = 96.9549; / 99 = 0.9793.

So the reported interval is consistent with shared-prefix cost fractions of roughly 67% to 98% at N = 100 — plausible for VQE sweeps with short parameterized tails and for QEC cycle repetition, but demanding: the suffix plus all overheads must be tiny at the top end.

**Step 3: Sensitivity to N.** Recompute the implied f for S = 2.95 at N = 10: f = 10 × 0.661017 / 9 = 6.61017 / 9 = 0.7345. At N = 1000: f = 1000 × 0.661017 / 999 = 661.017 / 999 = 0.6617. The implied f is only weakly sensitive to N; the reported range cannot be explained by task count alone.

**Step 4: Overhead-adjusted speedup.** Now include realistic overheads: M = 0.5 (materialization costs half a task), r = 0.05 (restore is 5% of prefix cost), δ = 0.01. With f = 0.9, N = 100:

Denominator = f + M + N(1 − f + r·f + δ) = 0.9 + 0.5 + 100 × (0.1 + 0.045 + 0.01) = 1.4 + 100 × 0.155 = 1.4 + 15.5 = 16.9.
S = 100 / 16.9 = 5.917.

So with substantial overheads, a 90%-shared prefix at N = 100 yields ≈ 5.9x, comfortably inside the reported interval. To reach S = 32.84 with these overheads we need the denominator ≤ 100/32.84 = 3.0475. With M = 0.5 fixed: N(1 − f + 0.05f + 0.01) ≤ 2.5475, i.e., 100(1 − 0.95f) ≤ 2.5475 → 1 − 0.95f ≤ 0.025475 → f ≥ 0.9732. So the top of the reported range requires ~97% prefix sharing even with modest overheads — or larger N.

**Step 5: Break-even task count.** Reuse beats direct execution when P < D:
f + M + N(1 − f + r·f + δ) < N
Rearranged: N·[f − r·f − δ] > f + M, i.e., N > (f + M) / (f(1−r) − δ), valid when f(1−r) > δ.

With f = 0.9, r = 0.05, δ = 0.01, M = 0.5: numerator = 1.4; denominator = 0.9 × 0.95 − 0.01 = 0.855 − 0.01 = 0.845; N > 1.4/0.845 = 1.657. So break-even is at N = 2 tasks — reuse pays almost immediately when the prefix is large. With f = 0.3 (weak sharing): denominator = 0.3 × 0.95 − 0.01 = 0.275; N > (0.3+0.5)/0.275 = 2.91, so N ≥ 3. With f = 0.1: denominator = 0.095 − 0.01 = 0.085; N > 0.6/0.085 = 7.06, so N ≥ 8. Even pessimistic sharing pays off at realistic sweep sizes; the planner's abstention logic matters mainly when f is small *and* N is small, or when M is large.

**Step 6: When is materialization unprofitable?** If M scales with prefix size (writing a 16 GiB artifact has real cost), say M = 1.0 (equal to a full task), f = 0.5, r = 0.05, δ = 0.01: denominator = 0.5 × 0.95 − 0.01 = 0.465; N > (0.5 + 1.0)/0.465 = 3.23, so N ≥ 4. Materialization cost shifts break-even modestly for large f but dominates for small f: at f = 0.1, M = 1.0: N > 1.1/0.085 = 12.9, so N ≥ 13.

## 5. Results

All numbers below are either (a) computed in Section 4, or (b) clearly labeled projections.

1. **Memory bound (computed)**: statevector artifacts require 16 GiB at 30 qubits, 256 GiB at 34 qubits, 1 TiB at 36 qubits, 16 TiB at 40 qubits. Practical RAM-resident materialization caps out near 32–34 qubits on a single large node.

2. **Implied prefix sharing (computed from the reported 2.95x–32.84x of [1, 2], assuming zero overhead)**: at N = 100, the interval corresponds to f ≈ 0.668 to 0.979. At N = 10, the lower bound implies f ≈ 0.735; at N = 1000, f ≈ 0.662.

3. **Overhead-adjusted projection (stated assumptions: M = 0.5, r = 0.05, δ = 0.01, N = 100)**: f = 0.9 yields S ≈ 5.92x (computed above). Achieving the reported upper bound S = 32.84 under these overheads requires f ≥ 0.973 (computed above). Uncertainty: if r were 0.20 instead of 0.05, the f = 0.9 denominator becomes 0.9 + 0.5 + 100(0.1 + 0.18 + 0.01) = 1.4 + 29 = 30.4, S = 100/30.4 = 3.29x — still within the reported interval's lower half, indicating the interval is robust to order-of-magnitude overhead variation only at high f.

4. **Break-even task counts (computed)**: N = 2 for f = 0.9; N = 3 for f = 0.3; N = 8 for f = 0.1 (with M = 0.5, r = 0.05, δ = 0.01). With M = 1.0: N = 4 at f = 0.5; N = 13 at f = 0.1.

5. **Consistency verdict**: the reported 2.95x–32.84x range is arithmetically consistent with a prefix-reuse model under plausible parameters (large f, N in the tens to hundreds, modest materialization and restore costs). We cannot independently verify the empirical measurements; the interval remains a claim from a single source [1, 2].

## 6. Discussion

**Limitations.** Our model is deliberately minimal. It assumes a single shared prefix per workload group; real workloads (e.g., VQE with multiple parameterized blocks) have a tree of shared segments, and the planner's problem becomes a set-cover-like selection of which artifacts to materialize, which our scalar f abstracts away. It also assumes costs are deterministic and additive, ignoring cache effects, GPU transfer asymmetry, and the fact that in stabilizer-hybrid mode the artifact type may differ per segment. We did not run QuWARP or Qrack; every empirical figure here is quoted from [1, 2], a single-source preprint, and our "verification" is consistency-checking, not replication.

**Failure modes.** (i) *Legality errors*: if the continuation-legality guardrail misclassifies an artifact as reusable when the downstream task diverges from the prefix (e.g., differing mid-circuit measurement patterns), the result is silently wrong simulation — worse than slow simulation. The EXPLAIN-style traces mitigate but do not eliminate this; audits catch errors only if someone reads them. (ii) *Memory blowout*: at ≥ 36 qubits, statevector materialization hits the TiB scale (Section 4, Step 1), and the planner must abstain or spill to storage, where r grows sharply and can erase gains (our r = 0.20 sensitivity case dropped S from 5.92x to 3.29x). (iii) *Selection bias*: the headline interval is conditioned on "reuse-positive workloads." On reuse-negative workloads the speedup is, by construction, ≤ 1 minus planning overhead; the abstract does not quantify this population, so the workload-level average gain is unknown. (iv) *Stale artifacts*: if a workload's circuits drift (parameterized gates migrating earlier in the circuit), f shrinks mid-run and materialized artifacts become dead weight.

**What would falsify the claims.** (a) A replication showing measured f values below ~0.6 on the evaluated workloads while speedups above 3x persist — this would imply the gains come from something other than prefix reuse (e.g., kernel warm-up), contradicting the mechanism. (b) Demonstrated legality violations: any workload where a reused artifact produces amplitudes differing from direct execution beyond floating-point tolerance. (c) Break-even measurements contradicting our Step 5 predictions — e.g., reuse failing to pay at N = 10 with f = 0.9 would indicate hidden overheads (M or δ) an order of magnitude larger than modeled. (d) Energy accounting under a JPCUB-style joules-per-solution protocol [11, 12] showing that artifact materialization and DRAM residency consume more energy than the redundant execution saves.

**Arguing against ourselves.** The most likely benign explanation for the upper bound (32.84x) is not exotic planning but simply very high f with large N — our own model reproduces it trivially at f ≈ 0.98, N = 100. That cuts both ways: it means the result is unsurprising in principle (checkpoint reuse is an old idea in general HPC), and QuWARP's genuine contribution must therefore rest on the *decision machinery* — legality typing, abstention, and auditability — rather than on raw speedup. Conversely, if the decision machinery is the contribution, the right evaluation is not speedup range but decision quality: false-reuse rate, false-abstention rate, and audit-trace completeness, none of which are quantified in the available abstract [1, 2]. A further caveat: our bibliography includes one withdrawn arXiv entry [5], a reminder that automated literature feeds contain unreliable items; and the QNFO corpus items [10–13] are Zenodo-deposited, non-peer-reviewed documents whose claims we used only for framing, not as evidence.

**Open questions.** Does the planner compose with GPU-accelerated kernels [7], or does artifact transfer dominate? Can the model be extended to prefix trees with provably optimal materialization sets? What is the correct legality type system for mixed statevector/stabilizer workloads, drawing on the simulability notions of [8]? And can reuse gains be expressed as energy savings under a standardized protocol [11, 12]?

## 7. Conclusion

We analytically triaged QuWARP's workload-level reuse planning claim. A closed-form amortized-cost model shows the reported 2.95x–32.84x speedups are consistent with shared-prefix cost fractions of ~0.67–0.98 at 100-task scale, that reuse breaks even at 2–13 tasks depending on sharing and materialization cost, and that statevector artifact materialization is memory-bounded near 32–34 qubits on single nodes. The claims are plausible but single-sourced and conditioned on reuse-positive workloads; the durable contribution, if any, lies in the auditable legality-guarding machinery rather than the headline speedups. Independent replication with reported f values, decision-quality metrics, and energy accounting is the necessary next step.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.23664&amp;amp;start=0&amp;amp;max_results=1 — QuWARP abstract record (arXiv 2609.23664).

[2] arXiv:2609.23664v1 | QuWARP: A Workload-Aware Reuse Planner for simulating Quantum Circuits.

[3] arXiv:1905.09692v3 | Structure optimization for parameterized quantum circuits.

[4] arXiv:2006.16817v2 | Proof of monotonic increase in the cost function for Krotov algorithm for open quantum systems.

[5] arXiv:1304.1836v2 | A Simulation and Modeling of Access Points with Definition Language (withdrawn by arXiv administrators).

[6] arXiv:2407.04826v1 | Multi-strategy Based Quantum Cost Reduction of Quantum Boolean Circuits.

[7] arXiv:2106.13995v1 | Fast quantum circuit simulation using hardware accelerated general purpose libraries.

[8] arXiv:1712.02806v3 | From estimation of quantum probabilities to simulation of quantum circuits.

[9] arXiv:1610.03438v2 | Introduction to Quantum Electromagnetic Circuits.

[10] QNFO: TETRIS-Q: Tiling-based Effective Transient-fault Reduction and Parallelism Optimizations for Quantum Circuit Mapping | DOI 10.5281/zenodo.22739633.

[11] QNFO: QWAV Strategy v2.4.1: The Energy-Standard Playbook — Consortium Governance, Verified Precedents, and the JPCUB Road to a Quantum Computing Energy Benchmark | DOI 10.5281/zenodo.21978952.

[12] QNFO: JPCUB Competitive Landscape v2.0: System-Level Joules-per-Solution Estimates for 17 Quantum Computing Platforms from Published Specifications | DOI 10.5281/zenodo.21821767.

[13] QNFO: Due Diligence Report: QuiX Quantum | DOI 10.5281/zenodo.21515894.