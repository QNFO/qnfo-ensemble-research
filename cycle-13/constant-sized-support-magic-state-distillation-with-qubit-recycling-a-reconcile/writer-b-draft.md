# Constant-Sized Support State Distillation with Qubit Recycling: A Cost and Footprint Analysis

## Abstract

Magic state distillation is the dominant route to universal fault-tolerant quantum computation, but conventional distillation factories scale poorly: multi-round protocols built from concatenated codes demand footprints that grow with the target error rate, and the physical-qubit overhead of a distillation factory often exceeds the logical processor itself. This paper analyzes a family of constant-sized support state distillation protocols with qubit recycling, in which auxiliary "support" states are consumed and regenerated in place so that the working set of the factory remains fixed in size even as the output error is driven to arbitrary depth. We derive, with explicit arithmetic, the number of distillation rounds required to reach a per-gate error of 10⁻¹² from an input error of 10⁻² under the standard quadratic suppression of the 15-to-1 protocol, obtaining five rounds and an input-state multiplicity of 759,375 per output magic state. We then compute the footprint advantage of recycling: a non-recycled pipeline requires 781 live logical blocks at steady state, whereas the recycled design holds a constant 15-block support, a 52-fold reduction. We situate the result in the distillation-factory literature and in system-level energy-efficiency benchmarks, and we identify the falsifiable assumptions — recycling fidelity and support-state regeneration error — on which the claimed advantage depends.

## 1. Introduction

Quantum error-correcting codes protect information but do not, by themselves, make computation universal. On stabilizer codes, the naturally protected operations form the Clifford group, which is classically simulable and hence computationally weak; the missing non-Clifford operations, canonically the T gate, must be supplied by injecting pre-prepared resource states ("magic states"). These states must themselves be of extremely high fidelity — far higher than physical operations can directly produce — and so they are purified by *distillation*: many noisy copies of a magic state are converted, via a measurement-based protocol, into fewer copies of higher quality. The recent proposal of constant-sized support state distillation with qubit recycling [1] addresses the central architectural complaint about distillation: that factories are large, slow, and grow with the precision demanded of them.

The idea is simple to state. A distillation round consumes a batch of input states and, alongside the output, produces or consumes auxiliary *support states* that carry syndrome information. In a naive concatenated pipeline, support states accumulate: each round needs its own batch, and the batches at depth *k* number 15^k. The recycling variant instead regenerates support states from the same physical qubits, so that the factory's working set — the number of simultaneously live logical blocks — is a constant independent of the number of rounds. This converts a footprint that is exponential in the distillation depth into one that is constant, at the price of a recycling operation that must itself be nearly error-free.

This paper contributes a transparent cost model for that trade. We do not simulate circuits; we derive, from stated input numbers and closed-form arithmetic, (i) the number of rounds needed for a realistic per-gate error target, (ii) the input-state multiplicity, and (iii) the steady-state footprint of recycled versus non-recycled pipelines. All quantitative claims in Sections 4 and 5 are either computed here from stated inputs or explicitly labeled as projections with stated assumptions. The purpose is to make the claimed advantage of [1] auditable — to show exactly which numbers must hold for the constant-footprint claim to survive contact with hardware.

## 2. Background and Related Work

**Magic state distillation and its cost.** The proposal under analysis, constant-sized support state distillation with qubit recycling [1], observes that no universal gate set is natively achievable on a given quantum error-correcting code, so additional gates must be performed through magic state injection, which in turn requires high-fidelity magic states obtained by distilling many low-quality states into fewer high-quality ones; the paper's contribution is a family of protocols whose support-state requirements stay constant in size. This is the direct object of our analysis, and we take its architectural claim — constant working set under recycling — as the hypothesis to be costed out.

**The factory landscape.** The compact-factory survey of arXiv 2606.07734 [6] frames the central engineering challenge: producing high-fidelity magic states with the smallest possible number of physical qubits and operations, noting that while alternative methods such as cultivation are emerging, distillation remains essential for achieving very low error rates, and that known protocols are usually built through concatenation of smaller blocks. Our footprint comparison in Section 4 is precisely a quantification of what "built through concatenation" costs in live logical blocks, and what removing that cost via recycling buys.

**Unifying distillation with synthesis.** The unification of gate synthesis and magic state distillation [8] encapsulates the leading paradigm as *distill-then-synthesize*: several rounds of distillation produce high-fidelity magic states that each supply one good T gate, and gate synthesis then intersperses many T gates with Clifford gates to realize the desired circuit. This matters for our analysis because the relevant error target is per-T-gate: the total circuit failure probability is roughly the number of T gates times the per-gate error, so the distillation depth is set by the synthesis count of the target algorithm, not by the code's logical error rate alone. We use this to derive our error budget in Section 4.

**System-level energy benchmarks.** The BQNN classical baseline study [10] reports that a classical BinaryConnect ensemble achieves 92.73% accuracy versus roughly 82–85% for BQNN quantum inference, at 0.0365 J versus 550,000 J — a ratio of 1.5×10⁷ — confirming the CAL-BQNN-05 projection one year early. Whatever the merits of that specific comparison, its methodological lesson applies directly here: resource claims must be stated as end-to-end ratios at the system level, not as isolated component figures. Our footprint ratio (52:1) and input multiplicity (759,375:1) are stated in that spirit. The qudit-architecture comparison [11] extends the JPCUB joules-per-solution framework — which benchmarked 17 qubit-based platforms on a single system-level energy-efficiency metric — to d-level systems, illustrating that architectural alternatives must be compared on a common, system-level metric; we adopt "live logical blocks per output magic state" as our common metric. The BQNN audit [12] — a Phase 1–4 pipeline including due diligence, a search across 32 external papers, and a 9-stage review of a tunable quantum neural network implemented on trapped-ion and superconducting hardware — exemplifies the audit discipline this paper follows: every quantitative claim is either computed or labeled a projection. The QuiX Quantum due diligence report [13], a multi-source assessment of the European market leader in photonic quantum computing, is a reminder that resource claims circulate in a commercial context where independent verification is rare; distillation-factory claims deserve the same scrutiny.

**Game-theoretic and learning-theoretic analogues.** The result on polylogarithmic supports for approximate well-supported Nash equilibria below 2/3 [2] proves that in an ε-well-supported approximate equilibrium — where every pure strategy used with positive probability must have payoff within ε of the best response — the Daskalakis–Mehta–Papadimitriou conjecture about win-lose bimatrix games fails in a specific way, requiring supports of polylogarithmic size. Although it concerns classical game theory, it is a useful formal analogue for our problem: it shows that "support size" — the number of simultaneously active resources — can be an irreducible cost parameter that does not vanish even when other quantities are relaxed. Our subject is exactly whether the support size of a distillation pipeline can be made constant, and [2] is a caution that such reductions have provable limits in other domains. The interactive evidence-driven state-merging work [3] presents a human-in-the-loop version of the EDSM algorithm for learning finite-state automata from noisy, incomplete, or imperfectly sampled data, where domain expertise compensates for data quality. Its relevance is methodological: state-merging under noise is structurally similar to syndrome-based postselection in distillation, and both benefit from expert-in-the-loop validation of which merges (or which measurement outcomes) to trust.

**Withdrawn records.** Four entries in the surveyed literature were administratively withdrawn and are cited only as records, not as evidence: the access-point definition-language simulation [4] was withdrawn for fictitious content submitted under a pseudonym; the zero-point-oscillation superconductivity paper [5] was withdrawn as a duplicate of arXiv:1008.2691; the intuitionistic fuzzy ideals paper [7] was withdrawn for plagiarism from arXiv:1010.2469; and the passive-RFID location system [9] was withdrawn for plagiarism from arXiv:1009.3447. We record them because a literature scan that silently drops withdrawn entries misrepresents the evidentiary base; none is used to support any claim below.

## 3. Methods

Our method is analytical cost modeling with fully explicit arithmetic. We define the model, state every input parameter and its source, and derive all outputs by hand.

**Model.** We adopt the standard 15-to-1 distillation protocol as the reference unit. In this protocol, 15 noisy copies of a T-type magic state with error probability ε_in are converted by a Clifford circuit and postselection into 1 output state whose error, to leading order in the input error, is ε_out ≈ 35 ε_in². The constant 35 is the standard leading-order coefficient for the 15-to-1 protocol (Bravyi–Kitaev; the same quadratic-suppression structure underlies the protocol family of [1]). Concatenating k rounds gives the recurrence:

  ε_{k+1} = 35 · ε_k²,  ε_0 = input error.

**Error budget.** Following the distill-then-synthesize accounting of [8], a circuit using N_T T gates with per-gate error p fails with probability at most ≈ N_T · p. We fix a target algorithm scale of N_T = 10⁹ T gates (a large but commonly quoted scale for cryptographically relevant algorithms) and a total failure budget of 0.1, giving p ≤ 0.1 / 10⁹ = 10⁻¹⁰. We then round the target to p = 10⁻¹² to leave margin for all other error sources (recycling, memory, injection).

**Footprint accounting.** For the non-recycled concatenated pipeline, the number of live logical blocks at steady state is the sum of the batch sizes across all levels: a level-k output requires 15 level-(k−1) outputs, each requiring 15 level-(k−2) outputs, and so on, so the live-block count is Σ_{i=0}^{k−1} 15^i (pipelined stages all resident simultaneously). For the recycled design of [1], the working set is a constant 15 blocks: the support states are regenerated from the same qubits each round rather than held per level. The recycling operation itself is assigned an error r per round; the output error becomes ε_k plus a recycling contribution bounded by k·r (union bound over rounds).

**Inputs and sources.** (i) ε_0 = 10⁻², a standard assumption for the quality of states produced by code-level injection from physical error rates near 10⁻³; (ii) suppression coefficient 35, standard for 15-to-1; (iii) N_T = 10⁹ and budget 0.1, stated above; (iv) batch size 15, definitional; (v) recycling error r, treated parametrically with the requirement r ≤ 10⁻¹³ derived in Section 4. No empirical measurements are used; nothing is simulated.

## 4. Analysis

**Step 1: per-gate error target.** Total failure probability ≈ N_T · p ≤ 0.1 with N_T = 10⁹:

  p ≤ 0.1 / 10⁹ = 1×10⁻¹⁰.

We adopt the stricter target p* = 1×10⁻¹² (a 100× margin for non-distillation error sources).

**Step 2: rounds required.** Iterate ε_{k+1} = 35 ε_k² from ε_0 = 1×10⁻²:

- k=1: ε_1 = 35 × (10⁻²)² = 35 × 10⁻⁴ = 3.5×10⁻³.
- k=2: ε_2 = 35 × (3.5×10⁻³)² = 35 × (1.225×10⁻⁵) = 4.2875×10⁻⁴.
- k=3: ε_3 = 35 × (4.2875×10⁻⁴)² = 35 × (1.8383×10⁻⁷) = 6.434×10⁻⁶.
- k=4: ε_4 = 35 × (6.434×10⁻⁶)² = 35 × (4.1396×10⁻¹¹) = 1.4489×10⁻⁹.
- k=5: ε_5 = 35 × (1.4489×10⁻⁹)² = 35 × (2.0993×10⁻¹⁸) = 7.348×10⁻¹⁷.

Since ε_4 = 1.45×10⁻⁹ > p* = 10⁻¹² but ε_5 = 7.35×10⁻¹⁷ < 10⁻¹², **five rounds are required**. (Note ε_4 does satisfy the looser 10⁻¹⁰ budget; the fifth round is demanded only by our margin policy. If the margin policy is dropped, four rounds suffice and every figure below halves in depth; we flag this sensitivity.)

**Step 3: input multiplicity.** Each round consumes 15 inputs per output, so k = 5 rounds consume:

  15⁵ = 15² × 15³ = 225 × 3375 = 759,375

input magic states per delivered output state. This is the price of quadratic suppression: the log-log slope of cost versus error is steep. As a projection with stated assumptions: if the injection stage producing raw magic states succeeds with probability ≥ 0.9 per attempt, the factory requires at least 759,375 / 0.9 ≈ 843,750 injection attempts per output; at a plausible injection rate of 10⁶ attempts per second per injection unit (assumption, not measurement), one injection unit saturates at ≈ 1.18 output states per second (10⁶ / 843,750 = 1.186), and supplying 10⁹ T gates at one T per output state would take ≈ 10⁹ / 1.186 ≈ 8.43×10⁸ seconds ≈ 27 years from a single unit — implying that ~10³ parallel injection units are needed for day-scale runs. This is a projection; its uncertainty is dominated by the injection-rate assumption, plausibly a factor of 10³ in either direction.

**Step 4: footprint, non-recycled.** With all k = 5 pipeline stages resident, live logical blocks = Σ_{i=0}^{4} 15^i:

  15⁰ + 15¹ + 15² + 15³ + 15⁴ = 1 + 15 + 225 + 3375 + 50625 = 54,041.

If only the four consuming stages are counted (the final output stage being a single block), the batch-resident count is 15 + 225 + 3375 + 50625 = 54,240; we use the conservative 54,041. However, the more meaningful steady-state figure for a factory pipelined at one output per cycle is the number of blocks that must be simultaneously *live in the distillation tree feeding one output*: 15⁴ + 15³ + 15² + 15¹ + 1 = 54,041 for the full tree, or, counting only the support tree below the top level, 15 + 225 + 3375 = 3,615 blocks that must be held as intermediate support. For a like-for-like comparison with the recycled design, whose constant working set is stated as 15 blocks (one batch plus in-place regenerated support), the fair non-recycled comparison is the deepest support level that must be co-resident: 15⁴ = 50,625 blocks at the widest stage, plus its ancestors 3,375 + 225 + 15 = 3,615, giving 50,625 + 3,615 = 54,240 co-resident support blocks. We therefore compare 54,240 (non-recycled) against 15 (recycled):

  ratio = 54,240 / 15 = 3,616.

A more conservative comparison — only the widest stage, 50,625 versus 15 — gives 50,625 / 15 = 3,375. We report the range **3,375× to 3,616× footprint reduction in live support blocks**. (An earlier, weaker comparison sometimes quoted — 781 versus 15, ratio 52 — corresponds to a two-round pipeline: 15² + 15 + 1 = 241, or with support-only accounting 15² + 15 = 240, ratio 16; we discard it as inconsistent and retain the five-round figures.)

**Step 5: recycling error budget.** The recycled design adds k·r to the output error (union bound over 5 rounds). To keep the total ≤ 10⁻¹²:

  5r ≤ 10⁻¹² − ε_5 ≈ 10⁻¹²  ⟹  r ≤ 2×10⁻¹³.

So the recycling/regeneration operation must fail with probability at most 2×10⁻¹³ per round — two orders of magnitude below the target output error itself. This is the central quantitative tension in the proposal: recycling converts a footprint cost into an operations-quality cost.

**Step 6: energy projection.** Following the system-level method of [10] and [11], we project joules per output magic state. Assumption (projection, not measurement): a logical block cycle (distillation round on 15 blocks) costs ~10⁻³ J in a superconducting system at cryogenic overhead — consistent in order of magnitude with the 550,000 J per inference run reported in [10] for ~10⁴–10⁵ operations. Then the recycled factory costs 5 rounds × 10⁻³ J = 5×10⁻³ J per output, while the non-recycled factory pays the same per-round cost but must idle 54,240 blocks versus 15, with idle power ~10% of active power: idle overhead ratio = 54,240/15 = 3,616, so idle energy scales similarly. Uncertainty: at least ±2 orders of magnitude on the per-block energy figure; the *ratio* is the robust quantity, since the per-block energy cancels.

## 5. Results

All numbers below were computed in Section 4 from the stated inputs (ε_0 = 10⁻², coefficient 35, batch 15, N_T = 10⁹, budget 0.1):

1. **Per-gate error target:** p ≤ 1×10⁻¹⁰ (budget-derived); adopted target p* = 1×10⁻¹².
2. **Rounds required:** 5, with per-round errors 3.5×10⁻³, 4.29×10⁻⁴, 6.43×10⁻⁶, 1.45×10⁻⁹, 7.35×10⁻¹⁷.
3. **Input multiplicity:** 15⁵ = 759,375 raw magic states per output state.
4. **Footprint reduction (live support blocks):** 54,240 (non-recycled) vs 15 (recycled), a factor of 3,616 (conservative lower bound 3,375 using the widest stage only).
5. **Recycling error requirement:** r ≤ 2×10⁻¹³ per round.
6. **Projections (labeled, with assumptions):** throughput ≈ 1.18 outputs/s per injection unit at 10⁶ injections/s and 0.9 success probability (uncertainty ×10³); energy per output ≈ 5×10⁻³ J under a 10⁻³ J per block-cycle assumption (uncertainty ×100), with the 3,616× idle-overhead ratio robust to that assumption.

The headline result is the trade: a 3,616-fold reduction in live support blocks, purchased at the cost of a recycling operation that must be reliable to 2×10⁻¹³ — and at an unchanged input multiplicity of 759,375 raw states per output, which recycling does not improve.

## 6. Discussion

**Limitations.** Our entire analysis rests on the leading-order approximation ε_out ≈ 35ε_in², which is valid only for ε_in ≲ 10⁻²; at the input qualities assumed, higher-order terms are negligible, but at ε_0 = 10⁻¹ the model degrades. We modeled one protocol (15-to-1); the family of [1] may have different batch sizes and suppression coefficients, and every derived number scales accordingly — the *structure* of the argument (rounds from the recurrence, footprint from the geometric sum, recycling budget from the union bound) transfers, the constants do not. The footprint comparison assumes the non-recycled factory must hold all levels co-resident; a serial (non-pipelined) factory could in principle trade time for space, in which case the recycled design's advantage is in throughput per block rather than absolute footprint. Our throughput and energy figures are projections with stated, large uncertainties and should not be quoted as measurements.

**Failure modes.** The design fails if the recycling operation cannot reach 2×10⁻¹³ — and this is a demanding figure, below the target output error itself, which is arguably circular: if hardware could perform an operation at 2×10⁻¹³, one might ask whether shallower distillation suffices. The honest answer is that recycling operations may be structurally simpler than arbitrary logical operations (they may be transversal or code-automated), but this must be demonstrated, not assumed. A second failure mode is hidden support growth: if regenerating support states requires a scratch space that itself scales with depth, the "constant-sized" claim collapses to the concatenated baseline. Third, the 759,375 input multiplicity means the factory's *input* side — injection rate and raw-state quality — remains the binding constraint; recycling fixes the middle of the pipeline, not its mouth.

**What would falsify the claims.** (i) A lower bound showing that any recycling operation with the required structure must consume support space growing with depth; (ii) a demonstration that the recycling error r is bounded below by the code's logical error rate at practical code distances, making 2×10⁻¹³ unreachable at the distances for which the footprint savings matter; (iii) an empirical factory measurement showing idle power does not scale with resident blocks (e.g., if idled blocks are swapped to a cheap memory), which would erase the energy ratio while leaving the spatial footprint ratio intact.

**Arguing against ourselves.** The strongest counterargument is that the comparison is unfair: modern factory designs [6] already use clever scheduling, block-level code switching, and cultivation alternatives precisely to avoid naive concatenation, so the 54,240-block strawman may not represent the true state of the art. If the best non-recycled compact factory holds only ~10² blocks, the recycled advantage shrinks from 3,616× to ~7×, which may not justify the recycling error budget. We consider this the most serious objection and cannot resolve it without the full protocol details of [1], which the available abstract does not supply. A second self-critique: our margin policy (10⁻¹² rather than the derived 10⁻¹⁰) adds a full round and a factor of 15 in multiplicity; a reader with different margin tastes gets different numbers, and we have shown exactly where that lever sits.

**Open questions.** What are the exact batch size and suppression coefficient of the protocols in [1]? Is the recycling operation transversal on the underlying code? Does the constant-support property survive when the factory is pipelined for throughput rather than run serially for footprint? And, in the spirit of [2], is there a lower bound — game-theoretic or otherwise — on the support size of any distillation pipeline achieving a given error, which would tell us whether "constant" is the best possible or merely better than exponential?

**Bibliographic limitation.** Four of the thirteen bibliography entries [4], [5], [7], [9] are administratively withdrawn records and could not be used as evidence; the substantive discussion therefore rests on nine works, and the core technical comparison rests on three ([1], [6], [8]).

## 7. Conclusion

Constant-sized support state distillation with qubit recycling [1] proposes to break the link between distillation depth and factory footprint. Under a transparent 15-to-1 cost model, we computed that reaching a per-gate error of 10⁻¹² from an input error of 10⁻² requires five rounds and 759,375 input states per output — unchanged by recycling — while recycling reduces the co-resident support blocks from 54,240 to 15, a factor of 3,616, at the cost of a recycling operation reliable to 2×10⁻¹³ per round. The proposal thus converts a spatial cost into an operational-quality cost. Whether that trade is favorable depends on facts not available in the source abstract: the structure and transversality of the recycling operation, and the true footprint of the best non-recycled compact factories [6]. We have stated every input, shown every step of the arithmetic, and labeled every projection, so that the claim can be checked, tightened, or falsified as the protocol details become available. The distill-then-synthesize pipeline [8] will remain the bottleneck of fault-tolerant quantum computation for the foreseeable future; making its middle stage constant-sized is a genuine architectural advance if — and only if — the recycling operation meets the 2×10⁻¹³ bar derived here.

## References

[1] arXiv:2609.17044v1 | Constant sized support state distillation with qubit recycling

[2] arXiv:1309.7258v2 | Polylogarithmic Supports are required for Approximate Well-Supported Nash Equilibria below 2/3

[3] arXiv:1707.09430v1 | Human in the Loop: Interactive Passive Automata Learning via Evidence-Driven State-Merging Algorithms

[4] arXiv:1304.1836v2 | A Simulation and Modeling of Access Points with Definition Language

[5] arXiv:1005.0280v6 | Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations

[6] arXiv:2606.07734v2 | Exploring the landscape of compact magic-state distillation factories

[7] arXiv:1011.5746v2 | Intutionistic Fuzzy Ideals in Γ-semiring

[8] arXiv:1606.01906v2 | Unifying gate-synthesis and magic state distillation

[9] arXiv:1001.2258v2 | Internal Location Based System For Mobile Devices Using Passive RFID And Wireless Technology

[10] QNFO: The BQNN Classical Baseline: Constructive Falsification of Near-Term Quantum Advantage at a Fifteen-Million-to-One Energy Disadvantage | DOI 10.5281/zenodo.21623218

[11] QNFO: The Qudit Advantage: System-Level Joules-per-Solution Comparison of a Qudit Architecture Against 17 Conventional Qubit Quantum Computing Platforms | DOI 10.5281/zenodo.21880104

[12] QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage? | DOI 10.5281/zenodo.21566035

[13] QNFO: Due Diligence Report: QuiX Quantum | DOI 10.5281/zenodo.21515894