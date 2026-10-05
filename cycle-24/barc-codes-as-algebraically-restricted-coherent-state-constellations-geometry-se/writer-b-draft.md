# Geometric Separation, Energy Trade-offs, and Literature Provenance in Bosonic Algebraically-Restricted Constellation (BARC) Codes: A Triage Analysis

## Abstract

Bosonic algebraically-restricted constellation (BARC) codes, introduced in arXiv:2610.03663, construct quantum error-correcting codes as finite superpositions of coherent states whose constellation geometry is constrained by the symmetry groups of solution sets to multivariate complex polynomial systems. This paper provides an independent triage analysis of the BARC framework for integration into a bosonic-codes research program. We reconstruct the core geometric machinery: we derive an explicit packing-type upper bound on the minimum separation of N equally-weighted constellation points, d ≤ 2R/(√N − 1), and evaluate it for triangular, square, and hexagonal constellations, finding that the hexagonal configuration achieves 72.5% of the bound, the best of the three. We then compute, with full arithmetic, the coherent-state overlap and the associated Knill–Laflamme leakage ingredients for hexagonal constellations at mean photon number n̄ = 4, obtaining an adjacent-vertex overlap of e⁻² ≈ 0.135 and a raw loss-error matrix element of 0.541, versus 3.35 × 10⁻⁴ and 1.34 × 10⁻³ for a two-point cat constellation at equal energy — a factor-403 penalty that quantifies the energy cost of richer constellations. We project that matching cat-code separation requires a 4× photon-number overhead for the hexagonal family. Finally, we audit the citation graph surrounding the preprint and find a high rate of withdrawn or fraudulent adjacent records, which we treat as a first-class methodological finding for automated literature triage.

## 1. Introduction

Bosonic quantum error-correcting codes encode a logical qubit (or qudit) into the infinite-dimensional Hilbert space of one or more harmonic-oscillator modes, using as their logical basis states superpositions of distinguishable classical-like states. The dominant families — cat, binomial, GKP, and rotation-symmetric codes — each impose a different symmetry on the constellation of phase-space points that make up the codewords. The BARC proposal [1, 2] generalizes this idea: instead of hand-designing constellations, it derives them from the solution sets of multivariate complex polynomial systems, whose orthogonal-group symmetries automatically align the code with the dominant physical noise operators (photon loss a and photon gain a†). The claim is that this algebraic restriction imposes approximate Knill–Laflamme (KL) conditions — the requirement that errors act identically (up to a unitary on the code space) on all codewords — for loss and gain channels, and that the framework yields explicit new families, including ellipsoidal and hexagonal single-mode codes benchmarked against spherical and cubature codes via entanglement fidelity under pure-loss noise.

This paper has three goals. First, to assess whether BARC codes are a genuine methodological advance or a reparametrization of known rotation-symmetric codes (Sections 3–5). Second, to extract the quantitative content of the framework — separation bounds, overlap scaling, energy trade-offs — and re-derive it independently, with every arithmetic step shown, so that downstream researchers can verify the claims without trusting the original benchmark numbers (Section 4). Third, to document an unusual and methodologically important feature of the source material: the daily research scan that surfaced this preprint also surfaced a citation neighborhood with an extraordinary density of withdrawn, plagiarized, and fraudulently affiliated records. We treat this not as noise but as data about the reliability of automated triage pipelines (Sections 2 and 6).

Our headline quantitative findings are: (i) the hexagonal constellation is near-optimal among small regular constellations with respect to the separation bound we derive; (ii) at fixed mean photon number n̄ = 4, the hexagonal constellation's adjacent-point overlap exceeds the cat code's antipodal overlap by a factor of ≈ 403, implying that BARC hexagonal codes pay a substantial KL-approximation penalty per unit energy unless the photon number is scaled up; and (iii) a clearly-labeled projection suggests a 4× energy overhead for the hexagonal family to reach cat-code pairwise distinguishability, with stated assumptions and uncertainty.

## 2. Background and Related Work

**The BARC framework.** The source preprint appears twice in the bibliography with different metadata records: [1] is the raw arXiv API query record and [2] is the versioned identifier arXiv:2610.03663v1. Both carry the same abstract; the substantive object is the framework itself. The authors introduce bosonic algebraically-restricted constellation codes, in which code states are finite superpositions of coherent states |α⟩ (eigenstates of the annihilation operator, a|α⟩ = α|α⟩) whose constellation points are constrained to lie in the solution set of a multivariate complex polynomial system. The key structural insight is that photon-loss and photon-gain errors correspond to algebraic operations on the constellation (multiplication by coordinates and their conjugates), so polynomial symmetry groups automatically enforce approximate KL conditions for those errors. The paper derives upper bounds on minimum geometric separation for equally-weighted constellations and, in the single-mode degree-two case, uses an orthogonal-group classification of quadratic solution sets to produce explicit ellipsoidal and hexagonal codes, benchmarked by entanglement fidelity with optimal recovery under pure-loss noise [1, 2]. This is the object under triage, and Sections 3–5 are devoted to it.

**Coherent-state resources in optical QIP.** The BARC construction sits in a broader tradition of using superpositions of coherent states as computational and communication resources. Jeong and colleagues [4] review Bell-state measurement and teleportation schemes using linear optics with three resource types — two-photon pairs, entangled coherent states, and hybrid entanglement — and show that perfect linear-optical teleportation is in principle achievable via a hybrid approach. This matters for triage because it establishes that coherent-state superpositions are not merely a coding-theoretic curiosity but an operational resource with known state-preparation and measurement protocols; any BARC code that reduces to known entangled-coherent-state structures inherits this operational pathway, which is a point in favor of practicality.

**Resource-commensurable code comparison.** The QNFO corpus includes a resource-commensurable comparison of cat, GKP, binomial, and surface codes using a photons-per-logical-qubit metric at target logical error rate p_L = 10⁻⁶, concluding that bosonic codes require 5–40× fewer photons and roughly 100× fewer modes than surface-code encodings, and advancing the structural claim that the harmonic oscillator is an infrared attractor of quantum mechanics and hence that bosonic codes are the "native encoding" [10]. Whatever one thinks of the attractor argument, the photons-per-logical-qubit metric is exactly the right yardstick for BARC codes, and we adopt it in Section 4: a new code family is only interesting if it improves this metric, not merely the fidelity at fixed energy.

**Qudit and structural extensions.** The QNFO qudit quantum error correction work [11] extends an ultrametric foundation thesis to quantum computing, formalizing geometric error confinement on tree-topology quantum processors. Its relevance here is the shared intuition that error structure is geometric: BARC confines loss/gain errors through phase-space geometry, [11] through tree topology; both claim that matching code geometry to error geometry beats generic encodings. Separately, the reconciled threshold analysis of the quantum-LCL framework [12] examines the extension of local coordinate-wise linear witnesses from classical linear codes to CSS quantum codes, highlighting the nested-pair difficulty (S ⊆ C) that a local witness must resolve. BARC sidesteps exactly this difficulty by working in the bosonic (unbounded-dimensional) setting where the KL conditions can be imposed continuously and approximately rather than discretely — a contrast worth making explicit. Finally, the number-theoretic ultrametric classification [13] proposes a unified p-adic framework (Mahler expansions, Amice transform, Kodaira–Néron fibers) for classifying error-correcting codes, with computational verification across four code families at 83% classification accuracy. BARC's polynomial-solution-set taxonomy is a competing classification principle for the bosonic sector; whether the two taxonomies intersect — e.g., whether rotation-symmetric codes correspond to distinguished p-adic classes — is an open question we flag in Section 6.

**Provenance failures in the adjacent citation graph.** A striking feature of the source material is that six of the thirteen bibliography entries are administratively withdrawn or removed records. Reference [3] (a "Simulation and Modeling of Access Points with Definition Language") was withdrawn for fictitious content submitted under a pseudonym; [5] (superconductivity from electron-gas zero-point oscillations) was withdrawn as a duplicate of another arXiv record; [6] (intuitionistic fuzzy ideals in Γ-semirings) was withdrawn for plagiarism; [7] (an RFID-based indoor location system) was withdrawn for plagiarism; [8] (a comment on Lense–Thirring systematic errors, attributed to "G. Felici") was removed for pseudonymous submission; and [9] (explicit estimates on prime numbers) was withdrawn for fraudulent affiliation claims. None of these is technically related to BARC codes. We nonetheless cite and discuss them because they are part of the provided bibliography and, more importantly, because their density in a single automated scan is itself a finding: automated research-triage pipelines that fetch records by identifier adjacency or keyword overlap will routinely surface such records, and any downstream synthesis must carry provenance metadata as a first-class field. In our case, the BARC preprint itself [1, 2] shows no signs of any of these failure modes, but the burden of demonstrating that falls on the triage process, not on the reader.

## 3. Methods

Our method is analytic reconstruction plus explicit audit, chosen because the BARC preprint's benchmark numbers (entanglement fidelities under pure loss) cannot be independently reproduced without the full manuscript, whereas its structural claims — separation bounds and KL-approximation scaling — follow from standard coherent-state identities that we can re-derive from first principles.

**Coherent-state identities.** For coherent states |α⟩, |β⟩ in a single mode, the overlap is

⟨α|β⟩ = exp(−(|α|² + |β|²)/2 + α*β),

with magnitude |⟨α|β⟩| = exp(−|α − β|²/2). The annihilation operator acts as a|α⟩ = α|α⟩, and the number operator n̂ = a†a satisfies ⟨α|n̂|β⟩ = α*β ⟨α|β⟩. The mean photon number of |α⟩ is ⟨n̂⟩ = |α|².

**Error model.** The pure-loss channel with transmittance η has Kraus operators E_m = √((1−η)^m / m!) a^m for m = 0, 1, 2, …. The KL conditions require ⟨ψ_i|E_m†E_n|ψ_j⟩ = c_mn δ_ij for all codewords |ψ_i⟩, |ψ_j⟩. Because E_m†E_n ∝ (a†)^m a^n, the leading off-diagonal leakage for small loss comes from m = n = 1, i.e., from the matrix elements ⟨ψ_i|a†a|ψ_j⟩, which are built from the coherent-state ingredients above.

**Constellation model.** A codeword is an equally-weighted superposition |ψ⟩ ∝ Σ_{k=1}^{N} |α_k⟩ over N constellation points. For a regular polygonal constellation on a circle of radius r in phase space, α_k = r e^{iθ_k} with θ_k = 2πk/N. The mean photon number of the constellation (ignoring the small normalization correction from mutual overlaps, valid when overlaps are ≪ 1) is n̄ ≈ r².

**Audit method.** Each bibliography entry was classified as (a) substantive and relevant, (b) substantive but tangential, or (c) withdrawn/removed, based on the metadata in the source block. No external claims about the withdrawn records are made beyond their stated withdrawal reasons.

## 4. Analysis

We now derive every number we report. All inputs are either standard identities (Section 3) or explicit assumptions stated inline.

**Step 1: A packing-type upper bound on minimum separation.** Let N equally-weighted constellation points lie within a phase-space disk of radius R, and let d be the minimum pairwise Euclidean separation. Draw a closed disk of radius d/2 around each point. These disks are disjoint (by minimality of d) and all lie within the enlarged disk of radius R + d/2. Comparing areas:

N · π(d/2)² ≤ π(R + d/2)²
⟹ N d²/4 ≤ R² + R d + d²/4
⟹ (N − 1) d²/4 ≤ R² + R d.

Solving the quadratic in d: (N−1)d² − 4Rd − 4R² ≤ 0, so

d ≤ [4R + √(16R² + 16R²(N−1))] / (2(N−1)) = [4R + 4R√N]/(2(N−1)) = 2R(1 + √N)/(N − 1) = 2R/(√N − 1).

This is the bound we use; it is the natural container-aware version of the naive area bound (which fails for boundary points, as we verified by finding the naive bound d ≤ 2R/√N violated by the regular hexagon).

**Step 2: Evaluate the bound for regular constellations.** For a regular N-gon inscribed in the circle of radius R = r, the actual minimum separation is the side length d_actual = 2r sin(π/N).

- N = 3 (triangle): √3 = 1.73205, so d ≤ 2r/(1.73205 − 1) = 2r/0.73205 = 2.7321r. Actual: d = 2r sin(60°) = 2r(0.86603) = 1.7321r. Efficiency: 1.7321/2.7321 = 0.6340, i.e., 63.4% of the bound.
- N = 4 (square): √4 = 2, so d ≤ 2r/(2 − 1) = 2r. Actual: d = 2r sin(45°) = 2r(0.70711) = 1.4142r. Efficiency: 1.4142/2 = 0.7071, i.e., 70.7%.
- N = 6 (hexagon): √6 = 2.44949, so d ≤ 2r/(2.44949 − 1) = 2r/1.44949 = 1.3801r. Actual: d = 2r sin(30°) = 2r(0.5) = r. Efficiency: 1/1.3801 = 0.7246, i.e., 72.5%.
- N = 2 (cat pair): √2 = 1.41421, so d ≤ 2r/0.41421 = 4.8284r. Actual: d = 2r sin(90°) = 2r. Efficiency: 2/4.8284 = 0.4142, i.e., 41.4%.

The hexagon is the most bound-efficient of these regular configurations — consistent with the BARC paper's choice of the hexagonal family as a headline construction [1, 2].

**Step 3: Overlap and leakage at fixed energy.** Fix the mean photon number n̄ = r² = 4, i.e., r = 2, for both the hexagonal BARC-type constellation and the two-point cat constellation.

Hexagon (r = 2): adjacent-vertex separation d = r = 2. Overlap magnitude between adjacent vertices:
|⟨α_k|α_{k+1}⟩| = exp(−d²/2) = exp(−2²/2) = exp(−2) = 0.13534.

The corresponding raw KL ingredient for the single-loss operator pair (m = n = 1) between adjacent vertices:
|⟨α_k|a†a|α_{k+1}⟩| = |α_k* α_{k+1}| · |⟨α_k|α_{k+1}⟩| = r² · e^{−2} = 4 × 0.13534 = 0.54134.

Cat pair (|α| = 2, points at ±α): separation d = |α − (−α)| = 2|α| = 4. Overlap:
|⟨α|−α⟩| = exp(−4²/2) = exp(−8) = 3.3546 × 10⁻⁴.

KL ingredient:
|⟨α|a†a|−α⟩| = |α* · (−α)| · e^{−8} = 4 × 3.3546 × 10⁻⁴ = 1.3418 × 10⁻³.

Ratio of overlaps: 0.13534 / 3.3546 × 10⁻⁴ = 403.4. Ratio of KL ingredients: 0.54134 / 1.3418 × 10⁻³ = 403.4 (identical, since both scale as r² e^{−d²/2} with the same r² prefactor at fixed energy).

Interpretation: at equal mean photon number, the hexagonal constellation's worst-case pairwise loss-leakage ingredient is ≈ 403 times larger than the cat code's. This is the arithmetic expression of the fundamental trade-off: more constellation points at fixed energy means smaller separations, and the leakage scales as the square of the radius times an exponential in minus half the squared separation.

**Step 4: Energy overhead projection (clearly labeled).** Assumption: to match the cat code's pairwise leakage at |α| = 2, the hexagonal constellation must achieve adjacent-vertex separation d = 4. Since d = r for the hexagon, this requires r = 4 and hence n̄ = r² = 16, versus the cat code's n̄ = 4. Overhead: 16/4 = 4×. Uncertainty: this projection assumes (i) leakage is dominated by the m = n = 1 Kraus pair, which degrades at high loss rates where higher-order terms contribute; (ii) equal weighting and negligible normalization corrections; and (iii) that the relevant comparison is worst-case adjacent pairs. If the BARC codewords exploit the polynomial symmetries so that adjacent-vertex coherences cancel in the full superposition (the paper's central claim [1, 2]), the effective overhead could be substantially lower — our 4× is an upper-bound-style projection, not a measured fidelity. Conversely, if the hexagonal code encodes more logical states per mode than the cat code, the photons-per-logical-qubit metric of [10] could still favor it; we cannot evaluate this without the full codeword definitions.

**Step 5: Cross-check against the resource metric.** Reference [10] reports bosonic codes requiring 5–40× fewer photons than surface codes at p_L = 10⁻⁶. If the hexagonal BARC code carries a 4× photon overhead relative to cat codes (Step 4) and cat codes sit at the favorable end of the 5–40× range, the hexagonal BARC family could plausibly remain competitive against surface codes but would likely lose to the best cat-type codes on the photons-per-logical-qubit metric. This is a projection conditioned on the assumptions of Step 4, not a computed benchmark.

## 5. Results

All numbers below were computed in Section 4; projections are labeled.

1. **Separation bound (computed):** d ≤ 2R/(√N − 1), derived by a disjoint-disk area argument with an enlarged container.
2. **Bound efficiencies (computed):** triangle 63.4%, square 70.7%, hexagon 72.5%, two-point cat 41.4%. The hexagon is the most efficient regular constellation examined, supporting the BARC paper's emphasis on the hexagonal family [1, 2].
3. **Overlap at n̄ = 4 (computed):** hexagonal adjacent-vertex overlap e⁻² = 0.13534; cat antipodal overlap e⁻⁸ = 3.3546 × 10⁻⁴.
4. **Single-loss KL ingredients at n̄ = 4 (computed):** hexagon 0.54134; cat 1.3418 × 10⁻³; ratio 403.4.
5. **Energy overhead (projection):** hexagonal BARC-type constellations require r = 4, n̄ = 16, a 4× photon overhead relative to the cat code at |α| = 2, to match cat-code pairwise separation, under the assumptions stated in Section 4, Step 5 — with the explicit caveat that symmetry-induced coherence cancellation in the full codewords could reduce the effective overhead, and we have not computed that cancellation.
6. **Provenance audit (computed from metadata):** 6 of 13 bibliography entries (46%) are withdrawn, removed, or retracted records ([3], [5], [6], [7], [8], [9]); 2 entries ([1], [2]) are duplicate metadata records for the same preprint; 5 entries ([4], [10]–[13]) are substantive.

## 6. Discussion

**Limitations.** Our analysis is deliberately structural: we did not reproduce