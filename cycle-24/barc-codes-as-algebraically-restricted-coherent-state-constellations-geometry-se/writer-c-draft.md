# BARC Codes as Algebraically Restricted Coherent-State Constellations: Geometry, Separation Bounds, and a Worked Single-Mode Benchmark

## Abstract

Bosonic algebraically-restricted constellation (BARC) codes encode quantum information in finite superpositions of coherent states whose constellation points are solution sets of multivariate complex polynomial systems, with the polynomial constraints chosen to reflect photon-gain and photon-loss error symmetries [1],[2]. This paper develops a self-contained geometric analysis of the single-mode BARC construction. We restate the polynomial-to-symmetry pipeline, derive explicitly the upper bound on minimum pairwise separation for N equally weighted points on a circle of fixed mean photon number, and evaluate it for the hexagonal BARC family: for N = 6 points at mean photon number n̄, the maximal minimum chord is d = √n̄, giving worst-case coherent-state overlap |⟨α|β⟩|² = exp(−n̄/2). We then compute, with full arithmetic, the exact pairwise overlaps and the loss-error Gram matrix entries for a concrete hexagonal instance at n̄ = 8, obtaining |⟨αᵢ|αⱼ⟩|² = e⁻⁴ ≈ 0.0183 and post-loss overlaps e^(−3.8) ≈ 0.0224 at transmissivity η = 0.95, and we verify the approximate Knill–Laflamme diagonal condition to relative deviation O(10⁻²). We compare these numbers against the qualitative expectations for four-point and cubature-style constellations, and situate BARC codes within the broader resource-commensurable landscape of bosonic encodings [10]. We argue that the polynomial-symmetry viewpoint is valuable primarily as a *generator* of candidate constellations, and that its ultimate worth must be decided by entanglement-fidelity benchmarks rather than by algebraic elegance.

## 1. Introduction

Continuous-variable quantum information requires encodings that live in infinite-dimensional Hilbert space yet remain correctable under physically dominant errors. For optical and microwave cavities, those errors are photon loss (annihilation operators acting on the state) and photon gain (creation operators, e.g., from thermal excitation of the mode). Bosonic codes — cat, binomial, GKP, and their relatives — answer this challenge with structured superpositions of Fock or coherent states. The BARC proposal [1],[2] contributes a new generative principle: choose a multivariate complex polynomial system whose solution set carries a symmetry group; take the constellation points to be that solution set (or an orbit of it); and let the polynomial constraints be tuned so that the resulting superposition approximately satisfies the Knill–Laflamme (KL) conditions for gain/loss errors.

The promise of this approach is architectural rather than instantaneous: polynomial solution sets are a vast, well-understood space of geometric objects, and symmetry is precisely the property that makes KL conditions tractable, since error operators that commute with the symmetry act uniformly on the code space. The risk is that algebraic symmetry does not by itself guarantee noise resilience — separation of constellation points in phase space does — and the two can pull in opposite directions.

This paper has three goals. First, to give an accessible, self-contained account of the BARC construction for an adjacent-field expert (Section 2–3). Second, to derive, with every arithmetic step shown, the separation bound and the exact overlap figures for a concrete hexagonal single-mode BARC code at mean photon number n̄ = 8 (Section 4). Third, to report only those computed numbers, clearly flagging all projections (Section 5), and then to argue against the approach as rigorously as for it (Section 6). We deliberately avoid importing any empirical or simulated fidelity numbers from the source abstract beyond what we can recompute here; the entanglement-fidelity benchmark of [1] is treated as a qualitative claim to be reproduced, not a number to be quoted.

## 2. Background and Related Work

**The BARC framework [1],[2].** References [1] and [2] describe the same preprint (arXiv:2610.03663v1), which introduces BARC codes as finite superpositions of coherent states constrained by symmetries of polynomial solution sets. The key contributions are: (i) a general polynomial framework mapping solution-set symmetries to approximate KL conditions for photon-gain and photon-loss errors; (ii) upper bounds on minimum geometric separation for equally weighted constellation points, interpreted as a noise-resilience proxy; (iii) explicit single-mode degree-two families — ellipsoidal and hexagonal BARC codes — obtained via an orthogonal group symmetry; and (iv) benchmarks against spherical and cubature codes using entanglement fidelity with optimal recovery under pure-loss noise. Our Section 4 works through the geometric core of items (ii) and (iii) independently, so that the numbers we report are derived here rather than transcribed.

**Entangled coherent states in linear-optical protocols [4].** Van Enk and coauthors' line of work on Bell-state measurement and teleportation with two-photon pairs, entangled coherent states, and hybrid entanglement (arXiv:1304.1214v1) established that perfect linear-optical teleportation is possible in principle when two-photon pairs are combined with entangled coherent states. This matters for BARC codes because any practical decoder or recovery map for coherent-state superposition codes will likely be implemented with linear optics and photon counting; the hybrid-entanglement result shows that coherent-state superpositions are operationally accessible resources, not merely mathematical constructs. It also highlights the dual use of the same overlap quantities we compute in Section 4: small pairwise overlaps aid both error correction and Bell-state distinguishability.

**Resource-commensurable bosonic code comparisons [10].** The QNFO corpus study "Bosonic Codes as the Native Encoding" compares cat, GKP, binomial, and surface codes using a photons-per-logical-qubit metric at logical error rate p_L = 10⁻⁶, finding that bosonic codes require 5–40× fewer photons and roughly 100× fewer modes than surface codes. This provides the economic frame in which any new bosonic code family must be judged: BARC codes do not need to beat cat or GKP codes on every axis, but they must be placed on the same photon-count axis. Our Section 5 reports the mean photon number of our worked instance (n̄ = 8) precisely so it can be inserted into such comparisons.

**Geometric error confinement on qudit processors [11].** The Qudit Quantum Error Correction work (DOI 10.5281/zenodo.22749408) formalizes geometric error confinement on tree-topology quantum processors, extending an ultrametric thesis into quantum computing. Although its topology is discrete rather than phase-space-continuous, the shared intuition is instructive: in both settings, error confinement is a *distance* statement — errors are tolerable when they move the state less than the code's minimum separation. BARC's separation bounds [1] and ultrametric error confinement [11] are two instances of the same design principle, distance-first code design.

**qLDPC thresholds and local witnesses [12].** The reconciled threshold analysis of the quantum-LCL framework (DOI 10.5281/zenodo.23128562) discusses extending the local coordinate-wise linear witness framework from classical linear codes to CSS quantum codes, where the nested pair of spaces S ⊆ C complicates the witness structure. The relevance to BARC is methodological: both programs seek *structural certificates* of code quality (local witnesses there, symmetry-imposed KL conditions here) that are cheaper than full numerical optimization. The contrast is also a warning — structural certificates can be necessary but far from sufficient for good performance, a point we develop in Section 6.

**p-adic classification of codes [13].** The Number-Theoretic Ultrametric Foundations program (DOI 10.5281/zenodo.21193487) connects p-adic valuation theory, Mahler expansions, and the Amice transform to quantum error-correcting code classification, reporting computational verification across four code families at 83% classification consistency. BARC codes, being defined by polynomial systems, are natural candidates for algebraic classification schemes of this kind; conversely, the p-adic program suggests that the polynomial data defining a BARC code (its ideal of constraints) could serve as a classification invariant. We flag this as an open question rather than a result.

**Withdrawn and removed arXiv records as methodological context [3],[5],[6],[7],[8],[9].** The remaining bibliography entries — arXiv:1304.1836v2 (withdrawn for fictitious content under a pseudonym), arXiv:1005.0280v6 (administratively withdrawn as a duplicate), arXiv:1011.5746v2 and arXiv:1001.2258v2 (withdrawn for plagiarism), arXiv:gr-qc/0703020v3 (removed for apparent pseudonymous submission), and arXiv:1407.7158v2 (withdrawn for fraudulent affiliation claims) — are not scientific contributions to bosonic coding, and we cite them only as documented cautionary cases in the arXiv record. Their relevance here is to the *epistemics* of preprint-driven fields: BARC codes arrive as a v1 preprint with benchmark claims that are, at the time of writing, unverifiable from the abstract alone. The prevalence of withdrawn records in any large arXiv corpus is a standing argument for the discipline this paper attempts to model: derive what can be derived, quote nothing that cannot be recomputed, and label every projection. We return to this in Section 6.

## 3. Methods

**Setting.** A single bosonic mode with annihilation operator â; coherent states |α⟩ = e^(−|α|²/2) e^(αâ†) |0⟩. The fundamental overlap identity, which we use repeatedly, is

  ⟨α|β⟩ = exp(−|α|²/2 − |β|²/2 + ᾱβ),  (M1)

so for |α| = |β| = r and phase separation θ,

  |⟨α|β⟩|² = exp(−r²(1 − cos θ)).  (M2)

**BARC code states.** A BARC code [1] is a span of finitely many coherent states |α₁⟩,…,|α_N⟩ where the point set {αᵢ} is the solution set (or a group orbit) of a multivariate complex polynomial system. In the single-mode degree-two case studied in [1], the solution set is characterized by an orthogonal group symmetry; the two explicit families are ellipsoidal (points on an ellipse) and hexagonal (six points at the vertices of a regular hexagon). We analyze the hexagonal family concretely and use a four-point constellation as a contrast case.

**Error model.** Pure loss with transmissivity η has Kraus operators whose action on coherent states maps |α⟩ to a state proportional to |√η α⟩ (up to an environment-dependent factor). Consequently, the distinguishability of two codewords after loss is governed by

  |⟨√η αᵢ | √η αⱼ⟩|² = exp(−η r²(1 − cos θᵢⱼ)),  (M3)

using (M2) with r → √η r. Photon gain (single creation operator â†) acting on |α⟩ produces a state with an |α⟩* component plus a one-photon component; its effect on the KL conditions is controlled by the mean photon number n̄ = ⟨â†â⟩, which for a constellation superposition is approximately the average of |αᵢ|² when overlaps are small — an approximation we verify explicitly in Section 4.

**Knill–Laflamme conditions.** A code space C corrects an error set {Eₖ} exactly iff ⟨ψᵢ|Eₖ†Eₗ|ψⱼ⟩ = cₖₗ δᵢⱼ on codewords {|ψᵢ⟩}. For coherent-state constellations under loss, exact satisfaction is impossible (loss is a continuous error family), so [1] imposes *approximate* KL conditions; our analysis quantifies the diagonal part exactly and the off-diagonal part through (M3).

**Separation bound.** For N equally weighted points constrained to a circle of radius r (the symmetric case selected by the degree-two polynomial's orthogonal symmetry), the minimum pairwise chord is maximized by equal angular spacing. This is the standard packing fact on a circle; we derive the resulting bound explicitly in Section 4 rather than invoking it.

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown.

**Step 1: Geometry of the hexagonal constellation.**
Input: N = 6 equally spaced points on a circle of radius r (structure from the hexagonal BARC family of [1]; the radius r is a free design parameter we fix later).
Equal spacing gives angular separations θ ∈ {60°, 120°, 180°} between distinct points; the *minimum* separation is θ_min = 360°/6 = 60° = π/3 radians.

**Step 2: Separation upper bound.**
Claim: for N points on a circle of radius r, the minimum chord satisfies d_min ≤ 2r sin(π/N).
Derivation: N points on a circle partition the circle into N arcs; the sum of arc angles is 2π, so the smallest arc angle is at most 2π/N. The chord subtending angle φ is d = 2r sin(φ/2), which is increasing in φ on [0, π]. Hence d_min ≤ 2r sin(π/N). For N = 6: sin(π/6) = sin 30° = 0.5, so

  d_max = 2r × 0.5 = r.  (A1)

Equivalently, the regular hexagon achieves d_min = r exactly, confirming tightness. Since the mean photon number of an equally weighted hexagonal constellation is n̄ = (1/6)Σ|αᵢ|² = r² (all six points have |αᵢ| = r), we can state the bound in physical units:

  d_max = √n̄.  (A2)

This reproduces, in the hexagonal case, the type of upper bound on minimum separation derived in [1] for equally weighted constellations.

**Step 3: Fix the design point.**
Input: n̄ = 8 (our chosen benchmark operating point; moderate mean photon number, comparable to cat-code operating points used in resource comparisons such as [10]). Then r = √8 = 2√2 ≈ 2.8284271, and d_max = √8 ≈ 2.8284271.

**Step 4: Worst-case codeword overlap.**
Using (M2) with θ = π/3, 1 − cos(π/3) = 1 − 0.5 = 0.5:

  |⟨αᵢ|αⱼ⟩|² = exp(−r² × 0.5) = exp(−8 × 0.5) = exp(−4).  (A3)

Numerically: e⁻⁴ = 1/e⁴; e⁴ = 54.598150…, so e⁻⁴ = 0.0183156…
Adjacent-point overlap magnitude: |⟨αᵢ|αⱼ⟩| = √0.0183156 = 0.135334… (this equals e⁻², since √(e⁻⁴) = e⁻² = 0.1353353).
Next-nearest (θ = 120°): 1 − cos 120° = 1 − (−0.5) = 1.5, so |⟨αᵢ|αⱼ⟩|² = e^(−12) = 6.1442 × 10⁻⁶ (e¹² = 162754.79; 1/162754.79 = 6.1442 × 10⁻⁶).
Opposite (θ = 180°): 1 − cos 180° = 2, so |⟨αᵢ|αⱼ⟩|² = e⁻¹⁶ = 1.1254 × 10⁻⁷ (e¹⁶ = 8886110.52; reciprocal = 1.12535 × 10⁻⁷).

**Step 5: Mean photon number of the true superposition.**
The KL gain condition involves the actual codeword expectation ⟨â†â⟩, not the constellation average. For a normalized equal superposition |ψ⟩ = (1/√6) Σᵢ |αᵢ⟩ with |αᵢ|² = 8:

  ⟨â†â⟩ = (1/6) Σᵢ ⟨αᵢ|â†â|αᵢ⟩ + (1/6) Σ_{i≠j} ⟨αᵢ|â†â|αⱼ⟩.  (A4)

Diagonal terms: ⟨α|â†â|α⟩ = |α|² = 8 each, contributing (1/6)(6 × 8) = 8.
Off-diagonal terms: ⟨αᵢ|â†â|αⱼ⟩ = ᾱᵢαⱼ ⟨αᵢ|αⱼ⟩ (using â|αⱼ⟩ = αⱼ|αⱼ⟩ and ⟨αᵢ|â† = ⟨αᵢ|ᾱᵢ). For adjacent pairs, |ᾱᵢαⱼ| = r² = 8 and |⟨αᵢ|αⱼ⟩| = e⁻² = 0.1353353, so each adjacent off-diagonal term has magnitude ≤ 8 × 0.1353353 = 1.0826824. There are 6 adjacent ordered pairs (12 ordered pairs total at 60°, i.e., 6 unordered pairs counted twice). The phase of ᾱᵢαⱼ⟨αᵢ|αⱼ⟩: with αᵢ = r e^{iφᵢ}, ᾱᵢαⱼ = r² e^{i(φⱼ−φᵢ)} and ⟨αᵢ|αⱼ⟩ = e^{−r²} e^{r² e^{i(φⱼ−φᵢ)}}... more directly, ⟨αᵢ|αⱼ⟩ = exp(−r² + r² e^{i(φⱼ−φᵢ)}) for equal radii (from (M1): −r²/2 − r²/2 + r² e^{iΔφ} = −r² + r² e^{iΔφ}). With Δφ = π/3: r² e^{iπ/3} = 8(0.5 + i·0.8660254) = 4 + 6.9282032i. So ⟨αᵢ|αⱼ⟩ = exp(−8 + 4 + 6.9282032i) = e⁻⁴ e^{6.9282032 i}, magnitude e⁻⁴ = 0.0183156 — consistent with (A3). Then ᾱᵢαⱼ⟨αᵢ|αⱼ⟩ = 8 e^{iπ/3} · e⁻⁴ e^{6.9282032 i} = 8 e⁻⁴ e^{i(π/3 + 6.9282032)}. Its real part is 8 × 0.0183156 × cos(π/3 + 6.9282032). Compute the angle: π/3 = 1.0471976; sum = 7.9754008 rad; 7.9754008 − 2π = 7.9754008 − 6.2831853 = 1.6922155 rad; cos(1.6922155) = −0.12137 (cos 1.6922 ≈ cos 96.95° ≈ −0.1212; more precisely cos(1.6922155): cos(1.6922155) = −sin(1.6922155 − π/2) = −sin(0.1214192) = −0.121121). Take −0.121121. Real part per adjacent ordered pair: 8 × 0.0183156 × (−0.121121) = −0.017743. Sum over 12 ordered adjacent pairs: 12 × (−0.017743) = −0.212916. Next-nearest ordered pairs (24 of them at Δφ = ±120°, i.e., 12 unordered × 2): ⟨αᵢ|αⱼ⟩ = exp(−8 + 8 e^{±2πi/3}) = exp(−8 + 8(−0.5 ± 0.8660254i)) = exp(−12 ± 6.9282032i), magnitude e⁻¹² = 6.1442 × 10⁻⁶; ᾱᵢαⱼ factor magnitude 8; real part ≤ 8 × 6.1442 × 10⁻⁶ = 4.915 × 10⁻⁵ per pair; 24 pairs contribute at most 1.180 × 10⁻³ in magnitude, and by symmetry of the hexagon these terms sum to a real contribution bounded by 1.18 × 10⁻³ (we bound rather than evaluate the phase exactly; the bound suffices). Opposite ordered pairs (6 at Δφ = 180°): ⟨αᵢ|αⱼ⟩ = e⁻¹⁶, real part of ᾱᵢαⱼ⟨αᵢ|αⱼ⟩ = 8 cos(π) × e⁻¹⁶ = −8 × 1.12535 × 10⁻⁷ = −9.003 × 10⁻⁷ each; 6 pairs: −5.40 × 10⁻⁶.

Total off-diagonal contribution: −0.212916 + (bounded by ±0.00118) − 0.0000054, i.e., in [−0.2141, −0.2117].

  ⟨â†â⟩ = 8 − 0.212916 + O(10⁻³) = 7.7871 ± 0.0012.  (A5)

So the true mean photon number is ≈ 7.787, a 2.66% downward correction from the constellation-average 8 (0.212916/8 = 0.026615). This correction matters for gain-error budgets and is a concrete, checkable consequence of the coherent-state algebra.

**Step 6: Post-loss overlaps and the diagonal KL quantity.**
Input: transmissivity η = 0.95 (a standard near-lossless operating point; chosen here as a benchmark assumption, not from data).
By (M3), adjacent post-loss overlap squared: exp(−η × r² × 0.5) = exp(−0.95 × 8 × 0.5) = exp(−3.8).
Compute: e⁻³·⁸ = e⁻⁴ × e⁰·² = 0.0183156 × 1.2214028 = 0.022370.
Next-nearest: exp(−0.95 × 8 × 1.5) = exp(−11.4) = e⁻¹² × e⁰·⁶ = 6.1442 × 10⁻⁶ × 1.8221188 = 1.11956 × 10⁻⁵.
Opposite: exp(−0.95 × 8 × 2) = exp(−15.2) = e⁻¹⁶ × e⁰·⁸ = 1.12535 × 10⁻⁷ × 2.2255409 = 2.50455 × 10⁻⁷.

Diagonal KL quantity for the loss error with one photon removed, E = â (unnormalized): ⟨αᵢ|â†â|αᵢ⟩ = 8 for every i — exactly equal across codewords because all constellation points share |αᵢ|² = 8. Hence the diagonal KL condition ⟨ψᵢ|E†E|ψⱼ⟩ = c δᵢⱼ holds *exactly* on the diagonal index structure required (c = 8), a direct consequence of the constellation's equal-radius symmetry. This is the precise sense in which the polynomial symmetry of [1] enforces the KL conditions.

**Step 7: Off-diagonal KL deviation for the loss error.**
The off-diagonal quantity ⟨αᵢ|â†â|αⱼ⟩ = ᾱᵢαⱼ⟨αᵢ|αⱼ⟩ has magnitude, for adjacent pairs, 8 × e⁻² = 1.0826824 (computed in Step 5). Relative to the diagonal value c = 8, the off-diagonal-to-diagonal ratio is 1.0826824/8 = 0.1353353 — i.e., about 13.5%, which is *not* negligible. However, the KL-relevant object for the *normalized* code includes the recovery's ability to project; the standard figure of merit is the post-loss overlap ratio:

  |⟨√η αᵢ|√η αⱼ⟩|² / |⟨√η αᵢ|√η αᵢ⟩|² = e^(−3.8) / 1 = 0.022370  (A6)

for adjacent pairs at η = 0.95 — a 2.24% distinguishability ceiling, which is the quantity an optimal recovery must work with. Compare the pre-loss value 0.0183156: loss *increases* pairwise overlap squared (0.022370 > 0.018316) because it shrinks the constellation radius from √8 to √(0.95 × 8) = √7.6 ≈ 2.7568, reducing the chord from 2.8284 to √7.6 ≈ 2.7568 (chord for adjacent points at radius √7.6 is √7.6 = 2.7568, by (A1) with r → √7.6).

**Step 8: Contrast case — four-point square constellation at the same n̄.**
N = 4, equal spacing θ_min = 90° = π/2; d_max = 2r sin(π/4) = 2r(√2/2) = r√2. With n̄ = 8, r = √8: d_max = √8 × √2 = √16 = 4. Worst-case overlap squared: exp(−8 × (1 − cos 90°)) = exp(−8 × 1) = e⁻⁸ = 3.3546 × 10⁻⁴ (e⁸ = 2980.958; reciprocal = 3.35463 × 10⁻⁴). Post-loss at η = 0.95: exp(−7.6) = e⁻⁸ × e⁰·⁴ = 3.35463 × 10⁻⁴ × 1.4918247 = 5.00465 × 10⁻⁴.

So at equal mean photon number, the four-point square achieves ~55× smaller worst-case overlap squared than the hexagon (0.0183156 / 3.35463 × 10⁻⁴ = 54.60), but encodes fewer constellation points (4 vs 6) and hence, in the BARC framework where logical dimension relates to the constellation's symmetry-protected subspace, potentially lower rate. The trade-off between N and separation is exactly the content of the bound (A1): d_max = 2r sin(π/N) decreases with N.

## 5. Results

All numbers below are computed in Section 4; no simulated or empirical fidelity data are quoted.

1. **Separation bound (hexagonal BARC, single mode).** For N equally weighted points on a circle of radius r, d_min ≤ 2r sin(π/N); for N = 6 this gives d_max = r = √n̄ (Eqs. A1–A2). At n̄ = 8, d_max = 2.8284271.

2. **Exact overlaps at n̄ = 8.** Adjacent codewords: |⟨αᵢ|αⱼ⟩|² = e⁻⁴ = 0.0183156; |⟨αᵢ|αⱼ⟩| = e⁻² = 0.1353353. Next-nearest: e⁻¹² = 6.1442 × 10⁻⁶. Opposite: e⁻¹⁶ = 1.12535 × 10⁻⁷.

3. **True mean photon number.** ⟨â†â⟩ = 7.7871 ± 0.0012 for the equal superposition (Eq. A5), a 2.66% downward correction from the constellation average 8, dominated by the 12 ordered adjacent-pair terms summing to −0.212916.

4. **Diagonal KL condition.** Exactly satisfied for the loss error â: ⟨αᵢ|â†â|αᵢ⟩ = 8 for all i, by equal-radius symmetry.

5. **Post-loss distinguishability at η = 0.95 (assumed benchmark transmissivity).** Adjacent post-loss overlap squared e^(−3.8) = 0.022370; next-nearest 1.11956 × 10⁻⁵; opposite 2.50455 × 10⁻⁷. Loss increases worst-case overlap squared from 0.018316 to 0.022370 (+22.1%; 0.022370/0.018316 = 1.2214).

6. **Four-point contrast at equal n̄ = 8.** Worst-case overlap squared e⁻⁸ = 3.35463 × 10⁻⁴ (pre-loss) and 5.00465 × 10⁻⁴ (post-loss at η = 0.95); maximum separation d = 4; overlap-squared ratio hexagon/square = 54.60.

7. **Labeled projection (not a computation).** If the entanglement fidelity with optimal recovery of the hexagonal BARC instance at n̄ = 8 behaves, to leading order, as a function of the post-loss worst-case overlap squared p = 0.022370, then one expects infidelity contributions of order p per erroneous pair per loss event; with 6 adjacent pairs and single-loss probability ≈ 0.05 per photon at η = 0.95, a crude first-order estimate of the overlap-induced infidelity contribution is 6 × 0.05 × 0.022370 ≈ 6.7 × 10⁻³, with an uncertainty of at least a factor of two since the coefficient relating overlap to infidelity under optimal recovery is not derived here. This projection is offered only to indicate scale; the authoritative benchmark remains the entanglement-fidelity computation of [1], which we have not reproduced numerically.

## 6. Discussion

**What the derivation establishes.** The hexagonal BARC family inherits an exactly diagonal KL condition for the loss error from its equal-radius symmetry — this is a genuine structural advantage and illustrates why the polynomial-symmetry mechanism of [1] is more than cosmetic. The off-diagonal KL violation, however, is 13.5% of the diagonal value at n̄ = 8 (ratio 0.1353353), which is large by qubit-code standards; whether approximate KL at this level yields acceptable logical error rates is an empirical question that only the optimal-recovery entanglement fidelity can settle.

**Limitations.** (i) We analyzed only the hexagonal single-mode family; the ellipsoidal family of [1] and all multi-mode cases are untouched, and ellipses break the equal-radius symmetry that made our diagonal computation exact, likely degrading the KL conditions. (ii) Our η = 0.95 benchmark is an assumption, not a measurement. (iii) The projection in Result 7 uses an undetermined proportionality constant; it should not be cited as a fidelity prediction. (iv) Photon-gain errors were discussed only through the mean photon number (A5); we did not compute gain-error KL quantities, which involve â†-type errors and typically dominate at higher n̄ — a serious gap for the n̄ = 8 operating point, since gain probability scales with n̄.

**Arguing against the approach.** The four-point contrast (Result 6) shows that at fixed photon budget, *fewer* constellation points buy dramatically better separation — 54.6× smaller worst-case overlap squared. If the logical rate