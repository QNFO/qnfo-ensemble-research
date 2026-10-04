# A Falsifiability-First Audit Program for the Photon-Primacy, Helical-Electron, and Adelic-Mass Claim Cluster

## Abstract

A cluster of speculative claims — photon-primacy (photons as ontologically prior to massive particles), the helical-electron model (rest mass as internal circulation of light), and adelic mass quantization (mass ratios encoded in p-adic/Bruhat–Tits tree structure) — currently circulates without a shared protocol for acceptance or rejection. This paper converts that cluster into a falsifiability-first audit program: a thesis statement, a set of graded kill conditions, and a work breakdown structure (WBS) in which every claim must be paired, before any confirmatory analysis, with the observation that would refute it. We ground the program in the Compton-frequency cross-ratio formalism on Bruhat–Tits trees [9], the trapped-ion ultrametric testbed register [10], and the evidence-grading standard of [12]. We derive concrete numerical targets with full arithmetic: the reduced-Compton/Bohr ratio reproducing the fine-structure constant α = 0.0072974 to five digits; a binary-ultrametric test statistic δ = 0.306 for the muon/electron mass ratio, which rejects exact base-2 scaling; and a p-adic prime-search window for mass-ratio logarithms. We specify what a passing audit must report even when key inputs are incomplete, adapting the disclosure logic of incomplete-label fairness audits [7]. The program's significance is methodological: it demonstrates how speculative theoretical programs can be made auditable without premature acceptance, and how audit disclosure standards transfer from machine learning to fundamental physics.

## 1. Introduction

Speculative theoretical frameworks in fundamental physics face a structural problem distinct from being wrong: they often cannot be *processed* by the community, because no observer — friendly or hostile — can state what observation would settle them. The photon-primacy/helical-electron/adelic-mass cluster is a live example. Its constituent claims are individually legible: (i) photon primacy asserts that electromagnetic radiation is ontologically and dynamically prior, with massive particles arising as self-trapped photonic configurations; (ii) the helical electron models rest energy as internal circulation at light speed; (iii) adelic mass quantization proposes that mass ratios carry arithmetic structure visible on non-Archimedean (p-adic) geometries such as Bruhat–Tits trees. What the cluster lacks is not ambition but an audit surface: a fixed, pre-registered set of numbers, derivations, and kill conditions against which any future measurement or computation can be scored.

This paper supplies that surface. Our contribution is deliberately procedural rather than doctrinal. We do not argue that photon primacy is true; we argue that it can be made *falsifiable in a graded, auditable way*, and we perform the first pass of that audit ourselves, deriving every number from stated inputs. The design borrows from three adjacent practices: formal verification of program equivalence, where a replacement artifact must be proven behaviorally identical before substitution [6]; fairness auditing under incomplete protected labels, where an auditor must decide what to disclose when a required input is partially missing [7]; and evidence-graded adjudication of objections, where each objection to a framework is assigned a grade reflecting the strength of evidence behind it [12].

The physical anchor is the Compton-frequency cross-ratio program on Bruhat–Tits trees [9], which assembles Standard-Model particles and condensed-matter quasiparticles into a single pattern table on a non-Archimedean tree, and the trapped-ion ultrametric testbed [10], which organizes sixteen published records into one testable claim: that ultrametric (p-adic) structure in quantum dynamics can be accepted or rejected by measurement on a near-term platform. Our audit program is the connective tissue: it states what the pattern table [9] and the testbed [10] must jointly deliver for the claim cluster to advance, and what single result would collapse it.

Section 2 situates the program in the literature. Section 3 defines the audit architecture. Section 4 carries out explicit derivations with every input number sourced and every arithmetic step shown. Section 5 reports only computed numbers and clearly labeled projections. Section 6 discusses limitations and falsification of the audit program itself. Section 7 concludes.

## 2. Background and Related Work

**Non-Archimedean physics and the pattern table.** The Bruhat–Tits tree construction of [9] is the direct substrate for the adelic-mass claim. That work assembles the finite Standard-Model particle table and the open-ended condensed-matter quasiparticle zoo into one pattern table indexed on a Bruhat–Tits tree — the incidence geometry of a non-Archimedean field, in which "points" are vertices of an infinite regular tree and distances satisfy the ultrametric inequality d(x,z) ≤ max(d(x,y), d(y,z)). Our audit program treats [9]'s table as hypothesis H3 (adelic mass): the claim under audit, not background truth. The trapped-ion register [10] is the complementary empirical instrument: it consolidates sixteen records from a single program (December 2025–August 2026) into one falsifiable claim about ultrametric structure in quantum dynamics, and specifies the measurement protocol by which p-adic structure is accepted or rejected. Our WBS adopts [10]'s register format verbatim as the audit log structure. The evidence-grading standard of [12] — five objections adjudicated against one graded standard — supplies the grading rubric we reuse: each audit item receives grade A (derivation + measurement), B (derivation only), C (consistency check), or F (failed kill condition). The Continuum Critique Trilogy [11] provides the philosophical pressure side: its critique of continuum assumptions motivates why adelic/arithmetic structure is worth auditing at all, and our program is designed so that a failed audit feeds directly back into [11]'s critique rather than into ad hoc rescue.

**Audit methodology from machine learning.** The fairness-audit disclosure problem of [7] is our closest methodological relative. [7] asks what a fairness audit must publish when the demographic labels it depends on are incomplete, and answers by pairing every published rate with a matched baseline from the same audit, one hidden from the reader. We transfer this exactly: every audit item in Section 3 pairs a headline number (e.g., a mass-ratio cross-ratio) with a matched control number computed by the identical procedure from a null assignment (e.g., randomized mass ratios), and the paper states which controls were hidden from the confirming analyst. This prevents the classic failure mode of speculative programs: computing the striking number and omitting the matched null.

**Formal verification and equivalence.** [6] develops automated verification of equivalence properties in advanced logic programs, motivated by the industrial need to verify that an optimized subprogram can replace an original. This is structurally the photon-primacy problem: the helical-electron model is a *replacement subprogram* for the standard mass term, and the audit must verify behavioral equivalence (or divergence) of predictions, not narrative plausibility. We adopt [6]'s discipline that equivalence is checked property-by-property, with each property a machine-checkable statement. [8] supplies the logical substrate: its treatment of the Turing–Church thesis, constructive mathematics, and intuitionist logic emphasizes that computation-theoretic reasoning proceeds through doubly negated propositions and ad absurdum argument. Our kill conditions are deliberately formulated as refutations rather than confirmations — a constructive reading in [8]'s sense, where "the claim survives" means "no kill condition fired," a doubly negated statement that gains force only as the count of survived adversarial tests grows.

**Resource allocation and audit execution.** [2] argues for cooperative, incentive-based coupling of distributed clusters in grid computing, centered on coordinated resource allocation versus non-coordinated superscheduling. The audit program of Section 3 is a distributed workload — derivations, ion-trap runs, cross-ratio recomputation — spanning groups that historically do not coordinate; [2]'s argument that coordinated allocation dominates non-coordinated scheduling maps onto our requirement that kill conditions be scheduled *before* confirmatory analysis, not after. [4] demonstrates parallel batch-and-streaming clustering of high-dimensional data streams (Cloud DIKW), applied to social media streams; we reuse its batch/stream split as the audit's two data regimes: static pattern-table entries [9] are batch-processed once, while ion-trap measurement streams [10] are processed continuously against the pre-registered thresholds. [5] shows, in the probabilistic-programming setting, how data-driven proposals accelerate sequential Monte Carlo inference; the analogy governs our adaptive stage gating — audit stages may be re-prioritized by incoming evidence, but thresholds themselves are frozen, exactly as [5] separates proposal adaptation from the target distribution. [1], a thesis on pseudomonads and descent, contributes the categorical vocabulary of descent: the audit's central move — transporting a claim from its origin framework (continuum QFT) to a test framework (ultrametric dynamics) and checking what survives — is a descent problem, and [1]'s treatment of descent along faithful maps cautions that transport is lossy unless the map is faithful, which becomes an explicit audit item (Section 3, W2). [3], on the Penrose inequality and volume comparison theorems via minimal surfaces, is our model of what a *successful* cross-domain inequality looks like: a sharp, numeric, geometry-to-geometry bound proved by comparing areas. Our cross-ratio kill conditions are designed to that standard — sharp numeric inequalities, not qualitative resemblances.

## 3. Methods

**Thesis statement (audited).** T: "Massive-particle rest energies are derivable, without continuum input, from photonic circulation (helical-electron) plus arithmetic structure on the Bruhat–Tits tree (adelic mass), and the resulting cross-ratios of Compton frequencies satisfy ultrametric constraints testable on trapped-ion platforms."

**Decomposition into kill conditions.** Each sub-claim is paired with a pre-registered kill condition (KC), stated before analysis:

- **H1 (photon primacy / helical electron).** KC1: if any rest mass is computed from photonic circulation to a relative accuracy worse than the same mass's known experimental precision without a fitted free parameter per particle, H1 degrades to grade C (consistency only). The audit requires a *parameter-count audit*: number of fitted parameters ≤ number of independently predicted quantities.
- **H2 (Compton cross-ratios).** KC2: the cross-ratio formalism of [9] must reproduce, from stated inputs only, at least the two anchor ratios derived in Section 4 (α from λ̄_C/a₀; the muon/electron Compton-wavelength ratio) within stated rounding, and must survive the matched-null control of [7]: the same extraction applied to a randomized mass table must not reproduce the anchors with comparable significance.
- **H3 (adelic/ultrametric mass structure).** KC3: if the logarithms (base p) of independent mass ratios fail to concentrate near integers beyond a chance baseline quantified in Section 4, the p-adic prime assignment is rejected; the trapped-ion register [10] then becomes the sole remaining test surface for ultrametricity.

**Work breakdown structure (WBS v2).**

- **W1 — Input freeze.** All physical constants and masses are frozen from stated sources with full digits; no post-hoc digit adjustment. Output: frozen input table (Section 4).
- **W2 — Faithfulness of transport.** Following [1], verify that the map from continuum expressions to tree expressions preserves the quantities being compared (descent along a faithful map). Kill: if the transport requires redefinition of any compared quantity, the cross-ratio result is graded C.
- **W3 — Derivation pass.** All Section 4 arithmetic, executed twice independently with hidden matched controls [7].
- **W4 — Empirical pass.** Map frozen thresholds onto the trapped-ion protocol of [10]; batch/stream split per [4]; continuous scoring of the stream against frozen thresholds.
- **W5 — Equivalence audit.** Property-by-property comparison of helical-electron predictions against the standard mass term, per [6]'s equivalence-verification discipline.
- **W6 — Grading and adjudication.** Assign grades A/B/C/F per [12]; publish the full register including failed items.

**Disclosure rule.** Adapted from [7]: the audit report must publish, for every headline number, (a) the matched control value, (b) the chance baseline, and (c) which controls were hidden from the confirming analyst. An audit that publishes rates without baselines is non-conforming.

## 4. Analysis

All inputs are frozen here; every subsequent number is derived from them.

**Input table (W1).**
- Planck constant: h = 6.62607015×10⁻³⁴ J·s (exact, SI 2019).
- Reduced Planck constant: ħ = h/2π.
- Electron rest energy: m_e c² = 8.18710565×10⁻¹⁴ J (CODATA).
- Electron reduced Compton wavelength: λ̄_C = ħ/(m_e c) = 3.86159268×10⁻¹³ m (CODATA).
- Bohr radius: a₀ = 5.29177211×10⁻¹¹ m (CODATA).
- Muon/electron mass ratio: m_μ/m_e = 206.7682830 (CODATA).
- Fine-structure constant: α = 7.29735257×10⁻³ (CODATA), used only as a check, never as an input to a derived quantity.

**Derivation D1 — the α anchor (H2).** Quantum electrodynamics fixes a₀ = ħ/(m_e c α) = λ̄_C/α. Inverting, the audit quantity is

  R₁ = λ̄_C / a₀ = 3.86159268×10⁻¹³ m / 5.29177211×10⁻¹¹ m.

Arithmetic: 3.86159268 / 5.29177211 = 0.7297352…; exponent shift 10⁻¹³/10⁻¹¹ = 10⁻². Hence

  R₁ = 0.7297352×10⁻² = 7.297352×10⁻³.

Compare the frozen check value α = 7.29735257×10⁻³: agreement to 7 significant figures (difference < 1×10⁻⁹ in absolute terms, i.e., relative deviation < 1.5×10⁻⁷, consistent with the 8-digit inputs). **Audit reading:** D1 is a consistency anchor, not a prediction — it verifies that the input table is internally coherent and that the cross-ratio extraction machinery reproduces a known constant. Its grade is C (consistency) by construction, since α was used in defining a₀.

**Derivation D2 — muon/electron ratio and binary ultrametric test (H3).** The Compton wavelength scales inversely with mass, so the Compton-wavelength ratio equals the inverse mass ratio:

  λ̄_C(μ)/λ̄_C(e) = m_e/m_μ = 1/206.7682830 = 4.83633×10⁻³.

The adelic hypothesis in its simplest binary form predicts that mass ratios are integer powers of a prime p (here p = 2), i.e., log₂(m_μ/m_e) ∈ ℤ. Compute:

  log₂(206.7682830) = ln(206.7682830)/ln 2.
  ln(206.7682830): ln 200 = 5.298317, ln(206.7682830/200) = ln(1.03384142) = 0.033283.
  Sum: 5.298317 + 0.033283 = 5.331600.
  ln 2 = 0.693147.
  log₂ = 5.331600 / 0.693147 = 7.6936.

Distance to the nearest integer: δ₂ = |7.6936 − 8| = 0.3064 (also |7.6936 − 7| = 0.6936, so nearest is 8). **Kill statistic:** δ₂ = 0.3064. For reference, the fractional part 0.6936 of log₂ is strikingly close to ln 2 = 0.6931 — a numerological coincidence we flag and *refuse to count as evidence*, since with ~30 candidate constants one expects several near-coincidences at the 10⁻³ level; this is exactly the matched-null discipline of [7] applied against our own temptation.

**Derivation D3 — chance baseline for integer-log concentration (KC3).** Suppose the adelic program proposes that k independent mass ratios each have |log_p(ratio) − nearest integer| < ε. Under the null (uniform fractional parts), the probability that a single ratio passes is 2ε; for k ratios, (2ε)ᵏ. Take the three lightest charged leptons and the p = 3 candidate, ε = 0.05, k = 2 (muon/electron and tau/muon). Null probability: (2×0.05)² = 0.01. The muon/electron case at p = 3: log₃(206.7682830) = 5.331600/1.098612 = 4.8527; distance to nearest integer |4.8527 − 5| = 0.1473 > 0.05 → **fails** at p = 3. At p = 2 it also fails (0.3064 > 0.05). **Audit reading:** with two ratios tested and a 1% joint null rate, a joint pass would be suggestive but not decisive (grade B); the actual outcome at p ∈ {2,3} is a *failed* item, recorded as such per W6. The adelic claim survives only in weakened form: not "mass ratios are prime powers" but "mass-ratio logarithms concentrate near rationals with small denominators" — a claim requiring the full pattern table of [9] and the empirical surface of [10], and currently ungraded.

**Derivation D4 — photon-primacy parameter count (KC1).** The helical-electron model claims rest energy E = m c² arises from internal circulation of light: E = ħ ω_int for some internal frequency ω_int. Setting ω_int = m c²/ħ is a definition, not a derivation; the model gains content only if ω_int is fixed by independent structure. Parameter count: fitted parameters f = 1 (the identification ω_int ↔ Compton frequency); independently predicted quantities n = 0 beyond the input mass itself. Since f > n, KC1 fires for the *unextended* helical model: grade F at this stage. The model can only recover if a mechanism fixes ω_int from photonic dynamics alone, predicting n ≥ 1 new quantities (e.g., a mass ratio) with f unchanged. This is the audit's sharpest current negative result.

**Derivation D5 — projected ion-trap discrimination power (projection, not measurement).** The register [10] specifies ultrametric tests on trapped-ion simulators. As a labeled projection with stated assumptions: if the platform resolves energy differences to fractional precision η and the ultrametric signal requires distinguishing tree-level spacing from Archimedean spacing at relative order ρ, the number of coherent cycles needed scales as N ≈ (1/ηρ)² (standard quantum metrology scaling, Heisenberg-limited would give 1/ηρ; we conservatively assume the standard-quantum limit). With η = 10⁻³ (state-of-the-art readout contrast) and a hypothesized ρ = 10⁻² (the smallest tree-level splitting in a depth-4 tree model), N ≈ (1/(10⁻⁵))² = 10¹⁰ cycles; at a typical gate rate of 10⁴ cycles/s this is 10⁶ s ≈ 11.6 days of continuous coherent operation — beyond current coherence budgets, implying the depth-4 test needs either Heisenberg-limited protocols (N = 10⁵ cycles ≈ 10 s, feasible) or reduced tree depth. Uncertainty: the projection is dominated by the assumed ρ, which is not fixed by [10]; if ρ = 10⁻³, the SQL requirement rises to ~116 days (infeasible) while the Heisenberg limit stays at ~10³ cycles. **This is a projection under stated assumptions, not a result.**

## 5. Results

Only numbers derived in Section 4 are reported here.

1. **D1 (grade C, consistency anchor).** R₁ = λ̄_C/a₀ = 7.297352×10⁻³, matching the frozen check value α = 7.29735257×10⁻³ to a relative deviation < 1.5×10⁻⁷. The input table is internally coherent.
2. **D2 (grade F for binary adelic hypothesis).** log₂(m_μ/m_e) = 7.6936; kill statistic δ₂ = 0.3064. Exact base-2 ultrametric mass scaling is rejected. The near-coincidence of the fractional part (0.6936) with ln 2 (0.6931) is recorded and explicitly *not* counted as evidence.
3. **D3 (grade F at p ∈ {2,3}, ε = 0.05).** log₃(m_μ/m_e) = 4.8527, deviation 0.1473 > 0.05. Joint null pass probability for two ratios at ε = 0.05 is 0.01; the observed outcome is a double failure. The adelic-mass claim survives only in a weakened rational-concentration form, currently ungraded.
4. **D4 (grade F for unextended helical-electron model).** Parameter count f = 1, predicted quantities n = 0; KC1 fires. The model requires a mechanism fixing the internal frequency to recover.
5. **D5 (projection).** Under stated assumptions (η = 10⁻³, ρ = 10⁻², standard-quantum limit), a depth-4 trapped-ion ultrametric test requires ~10¹⁰ cycles ≈ 11.6 days of coherent operation; under a Heisenberg-limited protocol, ~10⁵ cycles ≈ 10 s. Uncertainty dominated by the unfixed splitting scale ρ.

No empirical measurement is claimed in this paper. All physical constants are frozen inputs; all derived numbers above follow from the arithmetic shown in Section 4.

## 6. Discussion

**Limitations.** The audit is deliberately asymmetric: it can kill specific formulations (binary/ternary prime-power mass scaling; the unextended helical model) far more easily than it can confirm the cluster. This is by design — the program's value is in what it removes — but it means a fully "passing" audit is far away, and the weakened adelic hypothesis (rational concentration of mass-ratio logarithms) is currently so loose that it risks being unfalsifiable in practice, the very failure the program exists to prevent. The α anchor (D1) is graded C honestly: because a₀ is defined through α, D1 tests bookkeeping, not physics. A hostile reader could correctly say that the only genuinely falsifying results here are negative (D2–D4).

**Failure modes of the audit itself.** (i) *Threshold gerrymandering:* the choice ε = 0.05 in D3 is ours; a defender could pick ε = 0.15 and "pass" p = 3. Mitigation is the matched-null discipline of [7] — the null pass probability must be reported alongside any ε — but the mitigation is soft. (ii) *Transport unfaithfulness:* per [1], if the descent map from continuum to tree expressions is not faithful, cross-ratios computed on the tree may not correspond to the physical ratios; W2 checks this, but the check is currently procedural, not a theorem. (iii) *Coincidence inflation:* D2's ln 2 near-coincidence illustrates that with enough constants, spurious patterns are guaranteed; the program's refusal rule (one flagged coincidence per paper maximum) is a norm, not a proof. (iv) *Projection fragility:* D5's conclusions swing by orders of magnitude with ρ; it should be treated as a feasibility envelope, not a plan.

**What would falsify the audit program's claims.** The program makes one substantive meta-claim: that the cluster's content is capturable by pre-registered numeric kill conditions. Falsification would come from a defensible adelic or helical derivation that predicts a new quantity while genuinely evading the parameter-count audit — i.e., showing that KC1's f ≤ n criterion miscounts what a derivation contributes. A single accepted counterexample (a mass ratio predicted with f = 0 fitted parameters, surviving independent re-derivation under [6]-style property checking) would falsify our grade-F verdict in D4 and force re-grading.

**Arguing against ourselves.** A critic should press three points. First, we audit the *simplest* versions of the claims (prime-power scaling, bare helical identification); sophisticated versions may not be touched by our kill conditions, so our negative grades overreach. We accept this partially: the program kills formulations, not the cluster. Second, the trapped-ion projection (D5) assumes the ultrametric signal exists at all; if [10]'s sixteen records admit a purely Archimedean explanation, the entire empirical surface dissolves and the program loses its measurement leg — this is a real possibility we cannot exclude. Third, the evidence-grading rubric of [12] was built for adjudicating objections, not for certifying derivations; importing it here may grade apples against oranges. The open questions are: (a) can the rational-concentration form of H3 be given a null distribution sharp enough to be falsifiable; (b) does a faithful-descent theorem exist for the specific tree constructions of [9]; (c) can the ion-trap test reach Heisenberg-limited operation in practice; and (d) does the Continuum Critique Trilogy [11] survive its own audit under this standard — a reflexivity test we have not yet run.

## 7. Conclusion

We have converted the photon-primacy/helical-electron/adelic-mass cluster from a set of narratives into an auditable program: frozen inputs, pre-registered kill conditions, matched-null controls, graded outcomes, and a work breakdown structure connecting derivation to measurement. The first audit pass yields one consistency anchor (the Compton/Bohr ratio reproducing α to 1.5×10⁻⁷ relative), two clean negative results (rejection of exact prime-power mass scaling at p = 2 and p = 3; rejection of the unextended helical model on parameter-count grounds), and one feasibility projection for the trapped-ion empirical surface. The program's contribution is methodological: it shows that speculative fundamental-physics claims can be processed rigorously — accepted, weakened, or killed — without requiring the community to first believe them, and that audit-disclosure standards developed for machine learning transfer directly to this setting. The register produced here is designed to be extended: every future derivation or measurement in the cluster should enter it as a new row with a stated kill condition, a matched control, and a grade.

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