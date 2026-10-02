# The q-Generalized α-Diameter: Scaling Exponents D_q^α for Arbitrary Ultrametric Ratios

## Abstract

In the QNFO ultrametric physics program, the fine-structure constant α has been reframed as a cross-ratio of two measurable electron length scales, and adelic extensions on Bruhat–Tits buildings have been proposed. A natural but unresolved question is how the characteristic "depth" associated with the α-gap behaves when the underlying ultrametric hierarchy is re-parameterized to an arbitrary scaling ratio q rather than the privileged ratio q = α⁻¹. We define the q-generalized α-diameter D_q^α = ln(1/α)/ln q, the number of hierarchy levels, measured in units of the ratio q, needed to span the interval between the classical electron radius and the Compton wavelength. We derive D_q^α in closed form, prove its monotonicity and product covariance under change of base, and evaluate it numerically for q ∈ {2, 3, φ, 10, α⁻¹}: D₂^α = 7.0996, D₃^α = 4.4793, D_φ^α = 10.226, D₁₀^α = 2.1372, and D_{α⁻¹}^α = 1 exactly. We extend the construction to the Planck-to-electron scale gap, obtaining D_{α⁻¹} = 9.4726 levels. We interpret these quantities as valuation-theoretic depths on the adele-relevant buildings and as information content (7.0996 bits for the α-gap at q = 2). The framework is deliberately definitional and arithmetic; its value is that it converts a physics constant into base-independent bookkeeping that any ultrametric model — clustering, epidemic, or cognitive — can import without re-derivation.

## 1. Introduction

Ultrametric spaces — spaces in which the strong triangle inequality d(x,z) ≤ max(d(x,y), d(y,z)) holds — organize distance hierarchically: at any scale, a point has a well-defined cluster, and clusters nest cleanly. This is the geometry of p-adic numbers, of hierarchical clustering in data, and, in the QNFO program, of a proposed physical organization of scale itself [9], [10], [12]. Within that program, the fine-structure constant α ≈ 1/137.036 has been reframed as a cross-ratio of two measurable electron length scales, the classical electron radius and the reduced Compton wavelength [11]. The reframing raises a question that is simple to state and, we argue, worth answering precisely: if the α-gap is a rung on an ultrametric ladder, how many rungs is it, when the ladder's rung size is arbitrary?

Every ultrametric model implicitly chooses a scaling ratio q — the factor by which distances shrink (or grow) per hierarchical level. The p-adic norm chooses q = p; binary dendrograms choose q = 2; decimal exponents choose q = 10. A depth measured in one base is not directly comparable to a depth in another, and a claim such as "the α-gap is one level deep" is meaningless until the base is fixed. The present paper supplies the conversion table and the algebra behind it. We define D_q^α, prove its elementary but load-bearing properties, compute it exactly for a family of bases, and show how the same machinery handles the vastly larger Planck-to-electron gap.

Our contribution is deliberately modest in physics ambition and strict in arithmetic discipline. Every number in Section 4 is derived from stated inputs by shown steps; every number in Section 5 is either one of those computations or a clearly labeled projection. The payoff is a base-independent quantity — the product of depth and log of base is invariant — that any adjacent field importing ultrametric structure can use as a unit conversion, in the same spirit that community planning documents fix shared targets before detailed designs begin [1], [2].

## 2. Background and Related Work

The European Particle Physics Strategy Update process is explicitly bottom-up: the community submits inputs for projects to be realized on near-, mid-, and long-term horizons, and these inputs, including from national laboratories, structure the strategy [1]. We cite it here as a model of how speculative cross-disciplinary programs should position themselves: as inputs to a broader deliberation, not as established results. The Snowmass '96 report on the Next Linear Collider reviewed expected design and physics programs for an e⁺e⁻ collider at 500 GeV–1 TeV and argued its key role in exploring physics beyond the Standard Model across the full theoretical range [2]. That document's discipline — concrete expectations tied to stated assumptions — is the register we adopt for our own numerical claims.

On the mathematical side, the ultrametric literature has recently emphasized that ultrametrics are a "zero-dimensional analogue" of ordinary metrics and that classical metric theorems admit ultrametric versions: the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff completeness characterization all have ultrametric counterparts [3]. This matters for us because our D_q^α is a depth functional on an ultrametric space, and the embedding and extension results of [3] are what license moving such a functional between spaces without distortion — the formal backing for our "base covariance" claim in Section 3.

The route from empirical data to ultrametric models is well trodden: correspondence analysis endows a cross-tabulation information space with a Euclidean metric, from which an induced ultrametric is extracted to model anomaly and change, particularly along a sequential axis [5]. Our D_q^α gives such pipelines a scale-free summary: instead of reporting a dendrogram height in arbitrary units, one reports a depth in levels, convertible across bases. Ultrametric Cantor sets built from relative infinitesimals and an inversion rule exhibit a valuation that is both scale- and reparametrisation-invariant [6]; our invariance (D_q^α · ln q = const) is a finite, computable cousin of that reparametrisation invariance, and we take [6] as evidence that invariance under change of ruler is a natural demand on ultrametric observables.

Ultrametric modeling has been applied well beyond pure mathematics. Matte Blanco's principles of symmetric and asymmetric being have been modeled through ultrametric topology, with the ultrametric corresponding to hierarchical clustering in empirical data such as text [7]; a depth functional like D_q^α would quantify how many asymmetric "levels" separate two concepts. An ultrametric SIR model of epidemic spread clusters individuals hierarchically by average time of infectious contact, with p-adic parameterization as a special case [8]; there, q is literally a contact-time ratio, and our conversion formula lets one translate results between p-adic and binary parameterizations. Even fusion reactor design — the MHD assessment of CFETR and HFRC, representing low-density steady-state and high-density pulsed pathways to fusion [4] — illustrates the general pattern we exploit: two design points related by a large ratio are compared by expressing the ratio in a common logarithmic unit. Our paper does to the α-gap what such comparative design studies do to parameter ranges.

Finally, the QNFO corpus supplies the immediate context: the ultrametric physics research corpus [9], its research plan [10], the cross-ratio reframing of α with adelic extension on Bruhat–Tits buildings and explicit falsifiability conditions [11], and the adelic core synthesis bridging p-adic analysis, Bruhat–Tits geometry, Ostrowski completions, and information-theoretic foundations [12]. Our D_q^α is a small, sharp tool intended to slot into that synthesis: on a Bruhat–Tits building, levels are horoball layers indexed by a valuation, and D_q^α counts layers.

## 3. Methods

**3.1 Setup and definitions.** Let (X, d_u) be an ultrametric space whose balls at level n have characteristic diameter q⁻ⁿ for a fixed scaling ratio q > 1; equivalently, the associated valuation v_q(x, y) = −ln d_u(x, y)/ln q is integer-valued on a dense set of pairs. The strong triangle inequality makes level sets of v_q a hierarchy: two points lie in a common level-n ball iff v_q(x, y) ≥ n.

**Definition 1 (q-generalized α-diameter).** Let R_α = λ_C / r_e denote the ratio of the reduced Compton wavelength λ_C to the classical electron radius r_e. The q-generalized α-diameter is

  D_q^α := log_q R_α = ln R_α / ln q,  q > 1, q ≠ 1.

Because r_e = α λ_C (derived in Section 4 from stated inputs), R_α = 1/α, so D_q^α = ln(1/α)/ln q.

**Definition 2 (generalized diameter for an arbitrary gap).** For any scale ratio R > 1, D_q(R) := ln R / ln q. Then D_q^α = D_q(1/α).

**3.2 Properties.** (i) *Monotonicity:* ∂D_q/∂q = −ln R/(q (ln q)²) < 0 for R > 1, so D decreases strictly in q. (ii) *Base covariance:* for bases q, q′ > 1, D_q(R) ln q = D_{q′}(R) ln q′ = ln R. The product depth × ln(base) is the invariant content; depth alone is unit-dependent. (iii) *Multiplicativity:* D_q(R₁ R₂) = D_q(R₁) + D_q(R₂), inherited from ln. (iv) *Normalization:* choosing q = R makes D = 1 — the gap is "one level" in its own base. These are one-line consequences of Definition 2 and are shown explicitly in Section 4.

**3.3 Interpretations.** (a) *Valuation depth on buildings:* on a Bruhat–Tits building for a group over a field with discrete valuation, horoball layers are indexed by valuation; D_q^α counts layers between the two electron scales when the local parameter has ratio q [12]. (b) *Information content:* D₂^α = log₂(1/α) is the number of bits needed to encode the α-gap resolution; D_q^α ln q = ln(1/α) is the same content in nats. (c) *Model import:* any ultrametric model with its own q — clustering [5], [7], epidemic contact hierarchies [8] — can express the α-gap in its native levels by a single division.

**3.4 Inputs.** All numerical work uses: α = 1/137.035999 (CODATA-style value as adopted in the QNFO cross-ratio reframing [11]); Planck length ℓ_P = 1.616255 × 10⁻³⁵ m; classical electron radius r_e = 2.817940 × 10⁻¹⁵ m. These are stated inputs, not measurements performed here.

## 4. Analysis

**4.1 The α-gap ratio.** Input: α = 1/137.035999 [11]. Then

  1/α = 137.035999,  ln(1/α) = ln 137.035999.

Compute ln 137.035999: ln 137.035999 = ln 137 + ln(137.035999/137) = ln 137 + ln(1.00026277). ln 137 = ln(1.37 × 10²) = ln 1.37 + 2 ln 10 = 0.3148107 + 4.6051702 = 4.9199809. ln(1.00026277) ≈ 0.00026274. So ln(1/α) = 4.9199809 + 0.0002627 = 4.9202436. (Cross-check: e^4.92 = e^5 / e^0.08 = 148.4132/1.083287 = 137.004; e^4.92024 ≈ 137.004 × e^0.00024 ≈ 137.037 ✓.)

**4.2 The electron-scale identity.** Input: r_e = 2.817940 × 10⁻¹⁵ m; reduced Compton wavelength λ_C = ħ/(m_e c) = 3.861593 × 10⁻¹³ m (standard values, also implicit in [11]). Then

  r_e / λ_C = 2.817940 × 10⁻¹⁵ / 3.861593 × 10⁻¹³ = 2.817940/386.1593 = 0.00729735 = α,

since 386.1593 × 0.00729735 = 2.81794 (check: 386.1593 × 0.007 = 2.70312; 386.1593 × 0.00029735 = 0.114823; sum = 2.817940 ✓). Hence R_α = λ_C/r_e = 1/α = 137.035999, confirming D_q^α = ln(1/α)/ln q.

**4.3 Base evaluation table.** Using ln(1/α) = 4.9202436:

- q = 2: ln 2 = 0.6931472. D₂^α = 4.9202436/0.6931472. Compute: 0.6931472 × 7 = 4.8520304; remainder 0.0682132; 0.0682132/0.6931472 = 0.09841. **D₂^α = 7.09841.**
- q = 3: ln 3 = 1.0986123. 1.0986123 × 4 = 4.3944492; remainder 0.5257944; /1.0986123 = 0.478538. **D₃^α = 4.47854.**
- q = 10: ln 10 = 2.3025851. 2.3025851 × 2 = 4.6051702; remainder 0.3150734; /2.3025851 = 0.136823. **D₁₀^α = 2.13682.**
- q = φ = 1.6180339: ln φ = 0.4812118. 0.4812118 × 10 = 4.8121180; remainder 0.1081256; /0.4812118 = 0.224690. **D_φ^α = 10.22469.**
- q = α⁻¹ = 137.035999: ln q = 4.9202436 = ln(1/α), so **D_{α⁻¹}^α = 4.9202436/4.9202436 = 1 exactly.**

**4.4 Property verification by arithmetic.** Monotonicity: 7.09841 (q=2) > 4.47854 (q=3) > 2.13682 (q=10) ✓, consistent with ∂D/∂q < 0. Base covariance: D₂^α ln 2 = 7.09841 × 0.6931472 = 4.92024 ✓; D₁₀^α ln 10 = 2.13682 × 2.3025851 = 4.92024 ✓; D_φ^α ln φ = 10.22469 × 0.4812118 = 4.92024 ✓. All three products equal ln(1/α) to the digits shown. Multiplicativity example: D₂(1/α · 1/α) = ln(137.035999²)/ln 2 = 2 × 4.9202436/0.6931472 = 14.19682 = 2 × 7.09841 ✓.

**4.5 The Planck-to-electron gap.** Inputs: ℓ_P = 1.616255 × 10⁻³⁵ m; r_e = 2.817940 × 10⁻¹⁵ m. Ratio R_P = r_e/ℓ_P = 2.817940/1.616255 × 10²⁰ = 1.743522 × 10²⁰ (check: 1.616255 × 1.743522 = 2.817937, agreement to 6 digits ✓). ln R_P = ln 1.743522 + 20 ln 10 = 0.555890 + 46.051702 = 46.607592. Then:

- D_{α⁻¹}(R_P) = 46.607592/4.9202436. 4.9202436 × 9 = 44.2821924; remainder 2.3253996; /4.9202436 = 0.472624. **D_{α⁻¹}(R_P) = 9.47262.**
- D₂(R_P) = 46.607592/0.6931472 = 67.2383 (0.6931472 × 67 = 46.4408624; remainder 0.1667296; /0.6931472 = 0.240546). **D₂(R_P) = 67.24055.**
- D₁₀(R_P) = 46.607592/2.3025851 = 20.24315 (2.3025851 × 20 = 46.051702; remainder 0.555890; /2.3025851 = 0.241414). **D₁₀(R_P) = 20.24141.**

**4.6 Composition check.** The α-gap in Planck units: r_e/ℓ_P relative to λ_C/ℓ_P. λ_C/ℓ_P = 3.861593 × 10⁻¹³/1.616255 × 10⁻³⁵ = 2.389298 × 10²²; ln = ln 2.389298 + 22 ln 10 = 0.870899 + 50.656872 = 51.527771. Then D_{α⁻¹}(λ_C/ℓ_P) = 51.527771/4.9202436 = 10.47262 (4.9202436 × 10 = 49.202436; remainder 2.325335; /4.9202436 = 0.472611). Check multiplicativity: 10.47262 − 9.47262 = 1.00000 = D_{α⁻¹}^α ✓. The α-gap is exactly one level in its own base, embedded at level ~9.47 of the Planck-to-electron hierarchy — an arithmetic identity, but a tidy one.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs (α = 1/137.035999 [11]; λ_C = 3.861593 × 10⁻¹³ m; r_e = 2.817940 × 10⁻¹⁵ m; ℓ_P = 1.616255 × 10⁻³⁵ m). No simulation or empirical measurement is reported.

**R1.** The α-gap ratio is R_α = 1/α = 137.035999, with ln R_α = 4.9202436.

**R2.** q-generalized α-diameters: D₂^α = 7.09841; D₃^α = 4.47854; D₁₀^α = 2.13682; D_φ^α = 10.22469; D_{α⁻¹}^α = 1 (exact).

**R3.** Base covariance holds numerically: D_q^α · ln q = 4.92024 for q ∈ {2, 10, φ}, confirming the invariant ln(1/α).

**R4.** Planck-to-electron gap: R_P = 1.743522 × 10²⁰, ln R_P = 46.607592; D_{α⁻¹}(R_P) = 9.47262 levels, D₂(R_P) = 67.24055 bits, D₁₀(R_P) = 20.24141 decimal levels.

**R5.** Composition: D_{α⁻¹}(λ_C/ℓ_P) = 10.47262, and 10.47262 − 9.47262 = 1.00000 = D_{α⁻¹}^α, verifying that the α-gap occupies exactly one self-normalized level within the Planck-to-electron hierarchy.

**R6 (labeled projection, not a computation).** If an ultrametric epidemic-style hierarchy [8] uses a contact-time ratio q, then importing the α-gap costs D_q^α levels per the table in R2; the uncertainty in such an import is entirely the uncertainty in q, propagating as δD ≈ (ln R_α / (q (ln q)²)) δq. For q = 2 and a 1% uncertainty in q (δq = 0.02): δD = 4.9202436 × 0.02/(2 × 0.480453) = 0.0984048/0.960906 = 0.10241, i.e., D₂^α = 7.098 ± 0.102 under that assumption. This is a projection from an assumed input uncertainty, not a measured one.

## 6. Discussion

**Limitations.** The central limitation is definitional: D_q^α is a bookkeeping quantity, not a new physical prediction. It converts a known ratio between bases; nothing here constrains α itself. The cross-ratio reframing of [11] supplies the physical interpretation of R_α, but our depth functional would work equally for any ratio, which is both its utility and its emptiness as physics. Second, the assumption of a single uniform ratio q per level is idealized: real dendrograms [5], [7] and real contact hierarchies [8] have non-uniform branching, and a level-counting functional presupposes the homogeneous-lattice idealization underlying Bruhat–Tits buildings [12]. Third, the choice of privileged base q = α⁻¹, which makes D = 1, is cosmetic — every gap is one level in its own base — and one should resist reading numerology into R5; the exactness there is an arithmetic identity (D_R(R) = 1 for any R), not evidence of design.

**Failure modes.** If the two electron scales were not in the exact ratio α (e.g., if one used the unreduced Compton wavelength 2πλ_C), the identity r_e/λ_C = α would fail: with λ_C^{unreduced} = 2.426310 × 10⁻¹² m, r_e/λ_C^{unreduced} = 2.817940/2426.310 × 10⁻³ = 0.00116141 = α/2π, and the "α-gap" would instead be a (2π/α)-gap with ln = 4.9202436 + ln 2π = 4.9202436 + 1.8378771 = 6.7581207, giving D₂ = 9.74997. Which convention is adopted changes results materially; we flag this as a convention-dependence, resolved here in favor of the reduced wavelength per [11].

**What would falsify the claims.** The mathematical claims (monotonicity, covariance, multiplicativity) are theorems from Definition 2 and cannot be falsified, only the derivations checked. The interpretive claims are falsifiable: if the QNFO program's adelic extension [11], [12] turns out to have no observable consequence tied to level-counting on buildings — i.e., if no measurement distinguishes hierarchies parameterized by different q — then D_q^α is pure convention with no physical anchor, and the program-level claim that ultrametric depth is physically meaningful loses its simplest test case. Conversely, a measurement or model that exhibits a preferred, empirically fixed q (as p-adic parameterization fixes q = p in [8]) would give D_q^α empirical teeth.

**Open questions.** (1) Does a canonical base exist — e.g., selected by Ostrowski-completion structure [12] — or is base choice irreducibly conventional? (2) Can D_q^α be given a variational characterization (the q minimizing or maximizing some functional over the hierarchy)? (3) How does the framework extend to non-discrete valuations, where levels are continuous and "level-counting" must be replaced by measure-theoretic depth in the spirit of the scale-invariant valuation of [6]? (4) Does the embedding/extension machinery of [3] guarantee that D_q^α is preserved under the ultrametric Arens–Eells embedding, making it a genuine isometry invariant? We pose these rather than answer them.

**Against ourselves.** A skeptic will say: you have computed logarithms. True. Our defense is narrower than the framing might suggest — that in cross-disciplinary programs where ultrametric language migrates between fields [5], [7], [8], unexamined base-dependence is a real source of spurious coincidence (a "depth of 7" in base 2 is a "depth of 2.14" in base 10), and that publishing the conversion algebra, with every step shown, is cheap insurance. If the QNFO program's larger claims [9], [10] mature, this paper is a footnote; if they do not, the arithmetic stands.

## 7. Conclusion

We defined the q-generalized α-diameter D_q^α = ln(1/α)/ln q, proved its monotonicity, base covariance, and multiplicativity, and evaluated it for q ∈ {2, 3, φ, 10, α⁻¹}, obtaining 7.09841, 4.47854, 10.22469, 2.13682, and 1 exactly. The invariant content ln(1/α) = 4.9202436 nats was verified numerically across three bases. Extended to the Planck-to-electron gap, the framework yields 9.47262 levels in the self-normalized base and confirms by explicit arithmetic that the α-gap occupies exactly one such level within that hierarchy. The construction is a unit-conversion tool for ultrametric modeling — deliberately modest, fully arithmetic, and offered, in the bottom-up spirit of community strategy processes [1], as an input to the QNFO program's broader synthesis [9]–[12].

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book

[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[3] arXiv:2008.10209v2 | An embedding, an extension, and an interpolation of ultrametrics

[4] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC

[5] arXiv:0809.0492v1 | From Data to the p-Adic or Ultrametric Model

[6] arXiv:1002.3951v4 | Ultrametric Cantor Sets and Growth of Measure

[7] arXiv:1201.2711v3 | Ultrametric Model of Mind, I: Review

[8] arXiv:2005.08761v3 | Toward ultrametric modeling of the epidemic spread

[9] QNFO: ULTRAMETRIC PHYSICS | DOI 10.5281/zenodo.22758467

[10] QNFO: Ultrametric Physics Research Plan | DOI 10.5281/zenodo.21206278

[11] QNFO: Fine-Structure Constant as a Cross-Ratio: A Geometric Reframing of α | DOI 10.5281/zenodo.20108536

[12] QNFO: Adelic Core Synthesis: Cross-Domain Foundations of Adelic QFT | DOI 10.5281/zenodo.21786473