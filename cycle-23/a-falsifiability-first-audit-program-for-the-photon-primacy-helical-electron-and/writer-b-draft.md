# Falsifiability First: An Audit Program for the Photon-Primacy, Helical-Electron, and Adelic-Mass Claim Cluster

## Abstract

The photon-primacy/helical-electron/adelic-mass cluster of claims asserts that particle masses derive from photon-frequency structure on the Bruhat-Tits tree, that the electron's intrinsic angular momentum arises from helical motion at twice the Compton frequency, and that lepton mass ratios encode adelically meaningful rational or near-integer patterns. These claims have been presented alongside the Compton Frequency Cross-Ratios construction, but no systematic falsifiability audit exists. This paper supplies one. We decompose the claim cluster into eleven individually testable sub-claims, assign each a falsifier class (already-falsified, near-term testable, currently untestable, or structurally unfalsifiable), and derive explicit numerical thresholds. Using CODATA 2022 values we show that the near-integer reading of the muon-electron mass ratio as 207 is already excluded at roughly five orders of magnitude beyond its experimental uncertainty, while the tau-electron ratio 3477.21 versus a hypothetical integer 3477 remains within present error bars and requires only a factor-of-six improvement in tau-mass precision to adjudicate. We further compute the zitterbewegung-scale frequency budget for the helical-electron claim and show it implies a spatial radius below current direct-probe resolution, rendering that sub-claim testable only through indirect spectroscopic signatures. The result is a work-breakdown structure that converts a speculative synthesis into a ranked experimental queue.

## 1. Introduction

Speculative frameworks in fundamental physics often fail not by being wrong but by being structured so that wrongness cannot be demonstrated. The claim cluster under audit here — photon primacy (all rest mass originates as photon-frequency structure), the helical electron (spin-1/2 as literal helical motion), and adelic mass (mass ratios as rational patterns meaningful simultaneously over the reals and the p-adics) — has been developed in the QNFO corpus alongside a Bruhat-Tits-tree pattern table unifying Standard Model particles and condensed-matter excitations [9]. The companion ultrametric testbed program [10] argues that trapped-ion simulators can accept or reject p-adic dynamical structure empirically, which creates both an opportunity and an obligation: if the platform exists, the claims must be stated in a form the platform can kill.

This paper is a falsifiability-first audit. Its thesis is that the claim cluster is not monolithic: it contains sub-claims spanning the entire spectrum from already falsified by existing data to structurally incapable of disconfirmation. An honest research program must separate these regimes and allocate effort accordingly, rather than defending the cluster as a whole. We adopt the stance of the fairness-audit literature [7], which insists that a report must disclose not only its headline rates but the matched baselines and data-completeness conditions under which those rates were computed; here, every numerical claim must carry its uncertainty budget and its falsifier.

Section 2 situates the audit methodologically. Section 3 specifies the claim decomposition and the audit protocol. Section 4 performs the explicit arithmetic. Section 5 reports only what Section 4 computes. Section 6 argues against the paper itself.

## 2. Background and Related Work

The audit draws on several methodological traditions that, while heterogeneous, converge on the demand that claims be paired with decision procedures.

Formal verification of program equivalence [6] provides the closest structural analogue: when an optimised subprogram must be shown interchangeable with an original, one needs automated verification of equivalence properties, and the answer must be decidable from stated axioms. Our audit treats each adelic-mass claim as a program whose "equivalence" to an integer pattern must be verifiable or refutable by finite computation on measured inputs. The pseudomonad and descent framework [1], though originating in categorical algebra, contributes the descent-theoretic viewpoint that structure specified locally (at each prime p) must glue to global structure; the adelic-mass claim is precisely a descent claim, that mass data specified p-adically and real-analytically agree on overlaps, and descent theory tells us such claims carry nontrivial gluing obstructions that are themselves checkable.

The Turing-Church thesis analysis [8] is directly relevant because it examines how a foundational thesis functions when it is not a theorem: it argues that the theory of computation proceeds through doubly negated propositions and reductio reasoning, i.e., through falsification-shaped logic even where direct proof is unavailable. Our audit adopts the same posture toward photon primacy: we cannot prove it, but we can state what would refute it. The Penrose inequality work [3] demonstrates the gold standard we aim for in physics claims: a conjecture (mass contained by apparent horizons) tied to minimal-surface techniques that yield quantitative, checkable inequalities for specific manifold classes; the audit asks each adelic claim to state an analogous inequality with numbers attached.

On the systems side, cooperative incentive-based coupling of distributed clusters [2] shows that resource allocation across non-coordinated schedulers determines total system utility — a lesson for how a falsifiability program should allocate scarce experimental resources across competing sub-claims rather than testing opportunistically. The Cloud DIKW streaming-clustering environment [4] illustrates how high-dimensional pattern discovery can manufacture spurious clusters when representation choices are unconstrained; this is the central epistemic risk of the Bruhat-Tits pattern table [9], where a sufficiently flexible tree representation may accommodate any particle catalog, and it motivates our requirement of pre-registered numeric predictions. Probabilistic programming [5] supplies the inference machinery for the audit's statistical layer: sequential Monte Carlo with data-driven proposals is exactly the tool needed to evaluate whether observed mass ratios are better explained by integer patterns or by smooth priors, and the thesis's linear-Gaussian experiments establish the baseline methodology. The fairness-audit incompleteness paper [7] contributes the matched-baseline discipline: every published rate must be paired with a baseline computed under identical conditions, which we translate into the requirement that every cross-ratio "hit" be compared against the hit rate expected from chance under a stated null.

Within the QNFO corpus itself, the pattern-table paper [9] is the object of audit; the trapped-ion register [10] supplies the near-term experimental platform and its sixteen-record evidence base; the Continuum Critique Trilogy [11] collects the standing objections to continuum-based physics that the adelic program claims to answer; and the evidence-graded adjudication [12] establishes the five-objection, one-standard rubric that this audit extends from a single critique to the full claim cluster. The present paper is the falsifiability register those works call for but do not themselves construct.

## 3. Methods

The audit protocol has five steps.

**Step 1: Claim decomposition.** The cluster is split into eleven atomic sub-claims C1–C11, each of which is individually falsifiable or explicitly flagged as not falsifiable. Examples: C1, "the muon-electron mass ratio equals the integer 207"; C2, "the tau-electron mass ratio equals the integer 3477"; C3, "electron rest mass equals hν/c² for a photon frequency ν_C (Compton frequency)"; C4, "electron spin arises from helical circulation at frequency 2ν_C"; C5–C8, p-adic gluing conditions for primes p = 2, 3, 5, 7 on the mass data; C9, the cross-ratio closure condition (m_τ/m_μ)/(m_μ/m_e) ∈ ℚ with small denominator; C10, photon-primacy priority claim (mass is derivative on frequency); C11, the Bruhat-Tits pattern-table uniqueness claim.

**Step 2: Falsifier assignment.** Each claim receives one of four labels: F0 (already falsified by published data), F1 (falsifiable with a stated factor-of-improvement in existing measurements), F2 (falsifiable only with new apparatus, e.g., the trapped-ion testbed [10]), F3 (no known falsifier; quarantined from the empirical queue).

**Step 3: Threshold derivation.** For each F0/F1 claim we compute the deviation between the claimed value and the measured value, compare it to the one-sigma experimental uncertainty, and derive the improvement factor k needed for a five-sigma adjudication.

**Step 4: Null-model baselines.** Following [7], each near-integer "hit" is scored against the chance probability that a random ratio drawn from a smooth prior on the plausible range lands within the same tolerance of an integer.

**Step 5: Work-breakdown structure.** Sub-claims are ranked by (falsifiability class) × (deviation-to-uncertainty ratio), producing the experimental queue of Section 5.

Constants used (CODATA 2022 / PDG 2024): electron mass m_e = 9.1093837×10⁻³¹ kg; c = 2.99792458×10⁸ m/s; h = 6.62607015×10⁻³⁴ J·s; muon-electron mass ratio m_μ/m_e = 206.7682830 with relative uncertainty 1.1×10⁻⁸; tau mass m_τ = 1776.86 ± 0.12 MeV/c²; electron mass uncertainty negligible at the relevant level.

## 4. Analysis

**Derivation 1: electron Compton frequency (C3).** Photon primacy requires m_e = hν/c², so ν_C = m_e c²/h.

m_e c² = (9.1093837×10⁻³¹ kg)(2.99792458×10⁸ m/s)²
= (9.1093837×10⁻³¹)(8.98755179×10¹⁶) J
= 8.1871057×10⁻¹⁴ J.

ν_C = 8.1871057×10⁻¹⁴ / 6.62607015×10⁻³⁴ Hz
= 1.23558996×10²⁰ Hz.

The helical-electron doubling (C4) gives ν_zit = 2ν_C = 2.47117992×10²⁰ Hz. The corresponding circulation radius, if the helix is traced at speed c, is r = c/(2πν_zit) = (2.99792458×10⁸)/(2π × 2.47117992×10²⁰) m = 2.99792458×10⁸ / 1.5527×10²¹ = 1.9308×10⁻¹³ m. This is about 193 fm, i.e., roughly 146 electron classical radii — far *above* the Planck scale but *below* the de Broglie wavelength of any direct spatial probe at accessible energies, so C4 is testable only via spectroscopic sidebands, not imaging.

**Derivation 2: C1, muon ratio versus integer 207.** Claimed value N = 207. Measured R_μ = 206.7682830.

Absolute deviation: Δ_μ = 207 − 206.7682830 = 0.2317170.
Relative deviation: 0.2317170 / 206.7682830 = 1.1206×10⁻³.
One-sigma relative uncertainty: σ_rel = 1.1×10⁻⁸.
Exclusion significance: 1.1206×10⁻³ / 1.1×10⁻⁸ ≈ 1.02×10⁵ sigma.

C1 is falsified at roughly one hundred thousand sigma. No improvement in measurement is needed; the claim is dead as stated.

**Derivation 3: C2, tau ratio versus integer 3477.** First compute the ratio. m_τ/m_e = 1776.86 MeV / 0.51099895 MeV.

1776.86 / 0.51099895: 0.51099895 × 3477 = 1776.7454. Remainder: 1776.86 − 1776.7454 = 0.1146. 0.1146 / 0.51099895 = 0.2243. So R_τ = 3477.224 (to four decimals; call it 3477.22).

Deviation from N = 3477: Δ_τ = 0.224.
Relative uncertainty of R_τ, dominated by the tau mass: 0.12 / 1776.86 = 6.75×10⁻⁵, giving σ(R_τ) = 3477.22 × 6.75×10⁻⁵ = 0.2347.
Exclusion significance: 0.224 / 0.2347 ≈ 0.95 sigma.

C2 is not yet adjudicated. For a five-sigma adjudication we need σ(R_τ) ≤ Δ_τ/5 = 0.224/5 = 0.0448, i.e., relative uncertainty 0.0448/3477.22 = 1.29×10⁻⁵. Required improvement factor: 6.75×10⁻⁵ / 1.29×10⁻⁵ ≈ 5.2. Equivalently, the tau mass must be measured to ±0.023 MeV, versus the current ±0.12 MeV.

**Derivation 4: C9, cross-ratio closure.** (m_τ/m_μ)/(m_μ/m_e) = R_τ/R_μ = 3477.22 / 206.7682830.

206.7682830 × 16 = 3308.2925. 3477.22 − 3308.2925 = 168.9275. 168.9275 / 206.7682830 = 0.8171. So the cross-ratio is 16.8171. Its distance from the nearest integer (17) is 0.183, with propagated relative uncertainty sqrt((6.75×10⁻⁵)² + (1.1×10⁻⁸)²) ≈ 6.75×10⁻⁵, giving σ = 16.8171 × 6.75×10⁻⁵ = 1.14×10⁻³. Deviation 0.183 / 0.00114 ≈ 161 sigma. C9, in its small-denominator rational form near 17, is falsified.

**Derivation 5: null baseline for C2.** Under a uniform null on [3000, 4000], the chance of landing within 0.224 of an integer is (2 × 0.224)/100 per integer draw ≈ 4.5×10⁻⁴ — but the integer 3477 was selected after seeing the data, so the effective tolerance was chosen post hoc. The audit therefore scores C2 not as a hit but as unadjudicated, pending the pre-registered test at ±0.023 MeV precision.

## 5. Results

All numbers below are computed in Section 4 from stated CODATA/PDG inputs; no simulations or new measurements are reported.

1. **Electron Compton frequency (C3):** ν_C = 1.2356×10²⁰ Hz; helical doubling ν_zit = 2.4712×10²⁰ Hz; implied helix radius 1.93×10⁻¹³ m (193 fm). C3 is confirmed as an identity by definition of the Compton frequency; it is not evidence for photon primacy (C10) unless an independent consequence is derived.

2. **C1 (muon ratio = 207): FALSIFIED (class F0).** Measured 206.7682830; deviation 0.2317; exclusion ≈ 1.0×10⁵ sigma.

3. **C2 (tau ratio = 3477): UNADJUDICATED (class F1).** Measured 3477.22 ± 0.23; deviation 0.95 sigma. Five-sigma adjudication requires tau-mass precision of ±0.023 MeV, an improvement factor of 5.2 over the current ±0.12 MeV. Projection: assuming tau-mass measurements scale as 1/√N in statistics, this needs roughly 27 times the current dataset; uncertainty on this projection is at least a factor of two since systematics may dominate.

4. **C9 (cross-ratio rationality near 17): FALSIFIED (class F0).** Cross-ratio = 16.8171 ± 0.0011; deviation from 17 is ≈ 161 sigma.

5. **C4 (helical electron): class F2.** The 193 fm radius is below direct-probe resolution; falsification requires either detection or bounded absence of the predicted spectroscopic sidebands at 2ν_C in a suitable system, or the trapped-ion ultrametric signatures registered in [10].

6. **C5–C8 (p-adic gluing), C10 (photon primacy), C11 (pattern-table uniqueness): class F3 pending reformulation.** No numeric falsifier exists in the current literature; the audit quarantines them.

The ranked experimental queue is: (i) tau-mass precision program targeting ±0.023 MeV (cheapest, decisive for C2); (ii) trapped-ion ultrametric tests per [10] (decisive for C5–C8 if reformulated as dynamical predictions); (iii) spectroscopic sideband searches for C4; (iv) no further effort on C1 and C9 as stated.

## 6. Discussion

**Limitations.** The audit's strongest results — the ten-thousand-sigma falsifications of C1 and C9 — depend on the claim being read literally as "the ratio equals the integer." Defenders will say the intended claim was always "near-integer with adelic corrections," which converts an F0 falsification into an F3 unfalsifiable claim by adding a free parameter. This is the standard immunization move, and the audit's only defense is procedural: pre-registration. If the corrected-integer version of C2 is to be tested, the correction term must be specified before the improved tau-mass measurement, with its sign and magnitude, or the test is vacuous.

**Failure modes of the audit itself.** First, the null baseline in Derivation 5 is crude: a uniform prior on [3000, 4000] is not the right chance model for mass ratios, and a log-uniform or physical-prior null could shift the chance-hit probability by an order of magnitude. Second, the projection of a 5.2× precision improvement assumes statistical scaling that may not hold; tau-mass measurements at B-factories and the LHC are systematics-limited in parts, so the factor-of-two uncertainty stated in Section 5 may be optimistic. Third, the audit inherits its input uncertainties from CODATA/PDG; a correlated-error structure between the muon and electron masses, small as it is, is not propagated through Derivation 4 beyond the quadrature sum.

**What would falsify the audit's conclusions.** The C1 falsification would be overturned only by a revision of the muon-electron mass ratio at the 10⁻³ level — five orders of magnitude beyond its current uncertainty — which would itself be a physics revolution. The C2 "unadjudicated" verdict would become "confirmed" if the improved measurement lands within the pre-registered tolerance of 3477; the audit explicitly accepts this outcome as a success of the method, not a failure.

**Open questions.** Can C10 (photon primacy) be given any falsifier at all, or is it a metaphysical priority claim? The descent-theoretic reading of [1] suggests a testable gluing obstruction for C5–C8, but no one has computed it. And the pattern-table uniqueness claim C11 may be testable by the null-model discipline of [4] and [7] — by asking how many alternative tree embeddings fit the same catalogs — but that computation has not been done. Finally, the bibliography available to this audit is dominated by methodological rather than physics literature; a dedicated audit would need the p-adic and zitterbewegung physics literature directly, which is a stated limitation of the present evidence base.

## 7. Conclusion

The photon-primacy/helical-electron/adelic-mass cluster does not survive contact with a falsifiability-first audit as a whole, but it does not die as a whole either. Two of its literal sub-claims (C1, C9) are falsified at 10²–10⁵ sigma by existing data; one (C2) sits at 0.95 sigma from its integer reading and is adjudicable with a modest, quantified improvement in tau-mass precision (factor 5.2, to ±0.023 MeV); one (C4) is testable only indirectly; and three (C5–C8, C10, C11) currently lack falsifiers and must be quarantined or reformulated. The audit's central numbers — ν_C = 1.2356×10²⁰ Hz, R_μ = 206.7682830, R_τ = 3477.22 ± 0.23, cross-ratio 16.8171 ± 0.0011 — are all derived in full arithmetic from CODATA/PDG inputs. The program's value is not that it kills the synthesis but that it tells the synthesis exactly which of its organs are viable, which are dead, and what instrument would perform the next examination.

## References

[1] arXiv:1802.01767v3 | Pseudomonads and Descent, PhD Thesis (Chapter 1)
[2] arXiv:cs/0605060v1 | A Case for Cooperative and Incentive-Based Coupling of Distributed Clusters
[3] arXiv:0902.3241v1 | The Penrose inequality in general relativity and volume comparison theorems involving scalar curvature (thesis)
[4] arXiv:1502.00316v1 | Parallel clustering of high-dimensional social media data streams
[5] arXiv:1606.00075v2 | Applications of Probabilistic Programming (Master's thesis, 2015)
[6] arXiv:2310.19806v6 | Automated Verification of Equivalence Properties in Advanced Logic Programs -- Bachelor Thesis
[7] arXiv:2506.23033v5 | What Must a Fairness Audit Report When Demographic Data Is Incomplete?
[8] arXiv:2101.05387v1 | Turing-Church thesis, constructve mathematics and intuitionist logic
[9] QNFO: One Table, Two Regimes: Standard-Model Particles and Condensed-Matter Excitations as Patterns on the Bruhat-Tits Tree | DOI 10.5281/zenodo.22024856
[10] QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics | DOI 10.5281/zenodo.22025544
[11] QNFO: The Continuum Critique Trilogy | DOI 10.5281/zenodo.21691415
[12] QNFO: Five Objections, One Standard: An Evidence-Graded Adjudication of a Critique of Post-Quantum Synthesis | DOI 10.5281/zenodo.22010489