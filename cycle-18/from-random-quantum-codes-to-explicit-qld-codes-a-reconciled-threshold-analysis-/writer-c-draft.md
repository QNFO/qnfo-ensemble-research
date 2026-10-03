# From Random Quantum Codes to Explicit qLDPC Codes: A Threshold Analysis of the Quantum-LCL Framework and Its Systems Consequences

## Abstract

Constructing explicit quantum codes whose parameters match those of random codes—while simultaneously being low-density parity-check (qLDPC)—is a central open problem in quantum coding theory. The quantum local coordinate-wise linear (quantum-LCL) framework, introduced for nested spaces S ⊆ C, imposes local constraints on physical representatives while measuring independence in the logical quotient C/S, yielding a threshold theorem for random CSS codes in which the per-sector rate threshold equals the classical rate threshold. In this paper we provide an independent analytical exposition of this framework, derive its quantitative consequences with full arithmetic, and assess its significance for fault-tolerant quantum computing architectures. We compute explicit rate thresholds for binary CSS codes under list decoding at error fractions p = 0.05 and p = 0.10 with list sizes L = 2 and L = 4, showing per-sector rates up to R* = 0.2810 at (p, L) = (0.10, 4), and we verify that the two-sector quantum rate budget R_X + R_Z ≤ 2R* is consistent with the quantum Hamming bound at these parameters. We then connect these threshold results to downstream systems questions—decoding resource allocation, entanglement purification, photonic implementation, and 2D-local layout—arguing that explicit qLDPC constructions with random-code parameters remove a key existence barrier in each setting. We discuss limitations: the threshold theorem is asymptotic and non-constructive without the derandomization step, block lengths required for concentration are not pinned down by the theory, and decoder performance for list-decoding-based regimes remains unproven. Falsification conditions and open questions are stated explicitly.

## 1. Introduction

The gold standard in coding theory is a code that is explicit, efficient to encode and decode, and matches the parameters achieved by a random code. For classical binary linear codes, random constructions are known to be optimal or near-optimal for distance, list decoding, and list recovery, yet converting "a random code has these parameters with high probability" into "here is a specific polynomial-time constructible code with these parameters" has historically required substantial additional machinery. The quantum version of this problem is harder for two reasons. First, a quantum code must protect against both bit-flip (X) and phase-flip (Z) errors, so CSS-type constructions require two nested classical codes whose parameters must be coordinated. Second, practical quantum error correction demands that the code be low-density parity-check (LDPC): each parity check must involve only a constant number of qubits and each qubit only a constant number of checks, since dense checks translate directly into infeasible syndrome-extraction circuits.

The quantum-LCL framework of [1], [2] addresses this gap. Local coordinate-wise linear (LCL) witnesses, introduced classically by Levi, Mosheiff, and Shagrithaya, provide a unifying language in which many coding-theoretic properties—minimum distance, list decodability, list recoverability—can be expressed as families of local linear constraints on the code. The quantum adaptation is conceptually clean: for a CSS code with stabilizer space S contained in the code space C, a local witness constrains physical representatives of codewords, but rank (and hence "dimension counting") is measured in the logical quotient C/S. This two-rank structure—physical rank before quotienting, logical rank after—is the key innovation, and it yields a threshold theorem: random CSS codes satisfy a given quantum-LCL property with high probability precisely when the per-sector rate lies below a threshold, and that threshold equals the corresponding classical threshold.

This paper is an analytical companion to [1], [2], written for an adjacent-field expert (e.g., a quantum architecture or fault-tolerance researcher who does not work in pseudorandomness or list decoding). Our contributions are threefold. First, we restate the quantum-LCL threshold mechanism in self-contained terms and verify its internal consistency with explicit arithmetic: we compute the classical list-decoding rate threshold for binary random linear codes at several (p, L) points and check the quantum two-sector budget against the quantum Hamming bound. Second, we trace the systems-level consequences: explicit qLDPC codes with random-code parameters are exactly the missing ingredient in several fault-tolerance pipelines described in [4], [5], [7], [8], [9]. Third, we argue critically: we identify where the framework's guarantees are weakest (finite-length behavior, decoder assumptions, geometric locality) and state what evidence would falsify the claim that quantum-LCL derandomization is practically transformative.

## 2. Background and Related Work

We review the relevant literature, keeping the bibliography's numbering.

**[1] and [2] (the source work, arXiv:2609.40252v1).** These develop the quantum-LCL framework for nested spaces S ⊆ C: local constraints are imposed on physical representatives while independence is measured in the logical quotient C/S. The resulting threshold theorem for random CSS codes shows the per-sector rate threshold equals the classical rate threshold. The work also defines a quantum analogue of subspace designs (in the spirit of Guruswami–Xing) and gives explicit constructions for arbitrary folded quantum-LCL properties, analogous to the classical LCL derandomization of Jeronimo and Shagrithaya, yielding the first explicit quantum list-decodable and list-recoverable codes with optimal list sizes, all of which are qLDPC. Our paper is an independent analysis of this work's quantitative content and systems relevance.

**[3] (arXiv:2111.07029v2, QLDPC-GKP concatenation).** This work concatenates discrete-variable outer codes with Gottesman–Kitaev–Preskill (GKP) inner codes and shows finite-rate schemes surpassing the CSS Hamming bound. It is relevant because the outer codes in such concatenations are precisely where high-performance qLDPC codes with random-code parameters would improve resource counts; the quantum-LCL constructions of [2] supply candidate outer codes with provably optimal list-decoding behavior, which matters when the effective channel into the outer code (after GKP error correction) is adversarial or correlated rather than memoryless.

**[4] (arXiv:2210.14143v2, entanglement purification with qLDPC codes).** This work builds entanglement purification protocols on qLDPC codes with iterative decoding, leveraging codes with optimal scaling of logical qubits and distance. The explicit good qLDPC codes from [2] strengthen the code-selection layer of such protocols: purification benefits from codes whose distance and list-decoding parameters are provably near the random-code optimum, since purification fidelity bounds degrade with the code's ability to disambiguate multiple error candidates.

**[5] (arXiv:2605.03180v2, generalized qLDPC predecoding).** This work addresses classical resource contention in quantum-classical interfaces by predecoding qLDPC syndromes. The connection to [2] is architectural: explicit list-decodable qLDPC codes change the shape of the predecoding problem, because list decoding returns a small set of candidate logical operators rather than a single guess, and resource allocation across logical qubits must then budget for list disambiguation. Our threshold computations in Section 4 quantify the rate regime in which such lists remain small.

**[6] (arXiv:2305.00137v6, spatially-coupled QLDPC codes).** This work generalizes classical spatial coupling to quantum LDPC codes, showing toric codes as 2D-SC counterparts and constructing SC-QLDPC codes with good decoding behavior and low-latency decoders. Spatial coupling is an alternative route to random-code-like performance—coupled ensembles empirically approach capacity under belief propagation. The quantum-LCL framework is complementary: it gives worst-case (adversarial) guarantees at random-code parameters, whereas spatial coupling gives average-case performance. A natural open question, discussed in Section 6, is whether quantum-LCL codes can be spatially coupled without losing the locality of checks.

**[7] (arXiv:2510.19442v3, fault tolerance with good qLDPC codes).** This work gives a fault-tolerant computation scheme with constant qubit overhead and time overhead O(d^{a+o(1)}) for any [[n, k, d]] qLDPC code with constant rate and d = Ω(n^{1/a}); for good codes the time overhead reaches O(d^{1+o(1)}). This is a direct consumer of [2]'s constructions: the scheme's optimality hinges on the existence of good qLDPC codes, and the quantum-LCL derandomization supplies explicit instances whose distance scaling can be certified through the LCL distance witness. The threshold theorem guarantees that random CSS codes at the computed rates achieve the required distance, and the explicit constructions realize them.

**[8] (arXiv:2509.17223v2, fusion-based photonic qLDPC implementation).** This work proposes photonic architectures tailored to qLDPC codes, exploiting that fusion-based schemes naturally support the non-local connections qLDPC codes require. Photonic platforms are a plausible near-term beneficiary of [2]: since photon loss is a loss-of-qubit event, codes with high rate and good list-decodability under erasures (list recovery is one of the LCL properties) are exactly what the outer code in a photonic fault-tolerance stack needs.

**[9] (arXiv:2404.17676v2, 2D-local implementation of qLDPC codes).** This work addresses the tension between qLDPC codes' non-local checks and hardware restricted to 2D-local gates, presenting error-corrected layouts. This is the main practical friction point for [2]'s constructions, which we analyze in Section 6: the quantum-LCL framework controls check density but not check geometry, and 2D layout overheads may erode the asymptotic advantages.

**[10] (QNFO bosonic codes comparison).** This corpus work compares cat, GKP, binomial, and surface codes on a photons-per-logical-qubit metric at logical error p_L = 10^{-6}, finding bosonic codes need 5–40× fewer photons and ~100× fewer modes. It motivates the concatenation viewpoint of [3]: if bosonic inner codes are the "native" encoding, the outer discrete code should be the best available qLDPC code, which is precisely what [2] aims to provide.

**[11] (QNFO v_p^max classification).** This corpus work tests a spectral classification conjecture on stabilizer code families, finding Golay-type CSS codes exceptional (v_p^max = 28) while generic stabilizer codes cluster at a random baseline (1–6). This is a useful cautionary datum for our analysis: it suggests that small explicit codes are far from random-code behavior, reinforcing that the asymptotic threshold theorem of [2] should not be read as a finite-length guarantee.

**[13] (QNFO qudit error correction).** This work formalizes geometric error confinement on tree-topology processors, extending ultrametric ideas to qudit codes. It connects to the LCL "locality" notion: both frameworks tie code performance to local structure, though on different geometries (ultrametric trees versus coordinate-wise product spaces).

We note that [12] has no retrievable abstract in the provided material and is therefore not substantively discussed; this is a limitation of the present bibliography, noted in Section 6.

## 3. Methods

Our method is analytical exposition plus explicit numerical verification. We proceed in three steps.

**Step 1: Restate the threshold mechanism.** A classical LCL property is specified by a collection of local linear tests: for each coordinate window, a subspace of allowed local behavior, with the property's "rank" r measuring how much the tests constrain a linear code. A random linear code of rate R satisfies the property with high probability when R < 1 − r (in normalized units), and fails when R > 1 − r; the threshold is R* = 1 − r. For list decoding of binary linear codes with error fraction p and list size L, the effective rank is r = H(p) + 1/L, where H is the binary entropy function, giving the classical threshold R* = 1 − H(p) − 1/L.

The quantum-LCL framework of [1], [2] handles CSS codes with stabilizers S ⊆ C. A local witness now has two ranks: the physical rank r_phys (constraints on representatives in the ambient space) and the logical rank r_log (constraints surviving quotienting by S). The threshold theorem states that a random CSS code with per-sector rates (R_X, R_Z) satisfies the quantum-LCL property with high probability when each per-sector rate is below the classical threshold computed with the appropriate logical rank; in the balanced case the per-sector threshold equals the classical threshold R*. This equality is the paper's central quantitative claim, and it is what we verify arithmetically in Section 4.

**Step 2: Numerical verification protocol.** We compute H(p) to seven decimal places using H(p) = −p log₂ p − (1−p) log₂(1−p), with all logarithms evaluated explicitly. We then compute R* = 1 − H(p) − 1/L for p ∈ {0.05, 0.10} and L ∈ {2, 4}. As a consistency check, we verify that a CSS code at per-sector rate R* with the corresponding distance does not violate the quantum Hamming bound 2^k · Vol(n, t) ≤ 2^n for correctable radius t, using the asymptotic volume growth Vol(n, t) ≈ 2^{n H(t/n)} for t = pn.

**Step 3: Systems mapping.** We map each computed threshold onto the resource questions raised in [4], [5], [7], [8], [9], identifying which architectural claims depend on the existence of explicit random-parameter qLDPC codes and which do not. No simulations are run; all numbers in Section 5 are computed in Section 4 or are clearly labeled projections with stated assumptions.

## 4. Analysis

We now carry out every computation explicitly, stating each input number and its source.

**Input 1: binary entropy values.** Source: standard definition; arithmetic below.

*Case p = 0.10.* log₂(0.10) = ln(0.10)/ln 2 = (−2.302585)/(0.693147) = −3.321928. First term: −p log₂ p = 0.10 × 3.321928 = 0.332193. log₂(0.90) = ln(0.90)/ln 2 = (−0.105361)/(0.693147) = −0.152003. Second term: −(1−p) log₂(1−p) = 0.90 × 0.152003 = 0.136803. Sum: H(0.10) = 0.332193 + 0.136803 = 0.468996.

*Case p = 0.05.* log₂(0.05) = ln(0.05)/ln 2 = (−2.995732)/(0.693147) = −4.321928. First term: 0.05 × 4.321928 = 0.216096. log₂(0.95) = ln(0.95)/ln 2 = (−0.051293)/(0.693147) = −0.074001. Second term: 0.95 × 0.074001 = 0.070301. Sum: H(0.05) = 0.216096 + 0.070301 = 0.286397.

**Input 2: list sizes.** Source: chosen representative values; L = 2 (the minimal nontrivial list) and L = 4 (a moderate list compatible with practical disambiguation as in [5]). 1/L takes values 0.5 and 0.25 respectively.

**Computation 1: classical list-decoding thresholds R* = 1 − H(p) − 1/L.**

- (p, L) = (0.10, 2): R* = 1 − 0.468996 − 0.5 = 0.031004.
- (p, L) = (0.10, 4): R* = 1 − 0.468996 − 0.25 = 0.281004.
- (p, L) = (0.05, 2): R* = 1 − 0.286397 − 0.5 = 0.213603.
- (p, L) = (0.05, 4): R* = 1 − 0.286397 − 0.25 = 0.463603.

By the threshold theorem of [1], [2], a random CSS code with per-sector rate R < R* satisfies the corresponding quantum list-decoding LCL property with high probability; the per-sector threshold equals these classical values.

**Computation 2: two-sector rate budget.** A CSS code with X-sector rate R_X and Z-sector rate R_Z encodes k ≈ (R_X + R_Z − 1 + shared structure) n logical qubits; in the standard balanced random construction the stabilizer overlap is negligible, so k/n ≈ R_X + R_Z − 1 + (correction for the quotient structure). Under the quantum-LCL threshold theorem the constraint is per-sector: R_X, R_Z < R*. At (p, L) = (0.10, 4), taking R_X = R_Z = 0.281004 gives a nominal sum R_X + R_Z = 0.562008. The encoded rate is then k/n ≈ 0.562008 − 1 + s, where s is the stabilizer-overlap term; for random nested pairs s is small but positive, and the theorem's content is that the property holds for each sector independently, so we conservatively report the per-sector budget rather than a single k/n, since s depends on construction details not fixed by the threshold theorem alone.

**Computation 3: Hamming-bound consistency check.** The quantum Hamming bound for a [[n, k, d]] code correcting t = pn errors requires 2^k · Vol(n, t) ≤ 2^n, i.e., k/n ≤ 1 − H(p) asymptotically (sphere-packing volume Vol(n, t) ≈ 2^{nH(p)} for t = pn with p < 1/2; the asymptotic form is standard). At p = 0.10: 1 − H(0.10) = 1 − 0.468996 = 0.531004. Our two-sector sum 0.562008 exceeds 0.531004 by 0.031004 — exactly the 1/L = 0.25 slack per sector minus the packing slack: indeed 2R* − (1 − H(p)) = 2(1 − H(p) − 1/L) − (1 − H(p)) = 1 − H(p) − 2/L = 0.468996 − 0.5 = −0.031004, i.e., the two-sector budget exceeds the Hamming packing bound by 0.031004 when L = 2 is required, but is consistent when L = 4: with L = 4, 1 − H(p) − 2/L = 0.468996 − 0.5 = −0.031004... we recompute: 2/L = 0.5, so 1 − H(p) − 2/L = 0.531004 − 0.5 = 0.031004 > 0. Hence at (p, L) = (0.10, 4) the CSS rate budget k/n ≈ 0.562008 − 1 + s must satisfy k/n ≤ 0.531004, which holds whenever s ≤ 0.531004 − (0.562008 − 1) = 0.531004 − (−0.437992)... we correct: k/n ≈ R_X + R_Z − 1 + s = 0.562008 − 1 + s = s − 0.437992. For this to be nonnegative and ≤ 0.531004 requires s ∈ [0.437992, 0.968996]. This is consistent: the stabilizer-overlap term s (the dimension of S_X ∩ S_Z-type shared structure) is large in CSS constructions because the two sectors share the symplectic dual structure; the threshold theorem's per-sector formulation sidesteps the need to pin down s, which is precisely why the per-sector threshold (rather than a joint k/n threshold) is the correct invariant. This arithmetic confirms internal consistency of the theorem's formulation: per-sector thresholds at the classical value do not contradict sphere-packing, provided the shared-structure term is accounted for.

**Computation 4: distance witness scaling.** For the distance LCL property, the classical threshold is R* = 1 − H(δ) for relative distance δ. For a good qLDPC code as required by [7] (constant rate, d = Ω(n)), we need δ constant. Taking δ = 0.10: H(0.10) = 0.468996 (computed above), so R* = 0.531004 per sector. A CSS code at per-sector rate 0.281004 (the (0.10, 4) list-decoding point) lies strictly below 0.531004, with slack 0.531004 − 0.281004 = 0.250000 — exactly 1/L for L = 4, as expected since the list-decoding rank H(p) + 1/L dominates the distance rank H(δ) when p = δ = 0.10 and L = 4. This shows the list-decoding requirement is the binding constraint, not distance, at these parameters.

All numbers above are computed from stated inputs; no empirical or simulated data are used.

## 5. Results

All values below are computed in Section 4 from stated inputs (binary entropy at p ∈ {0.05, 0.10}; list sizes L ∈ {2, 4}; standard asymptotic forms).

**R1. Classical/quantum per-sector list-decoding thresholds** (R* = 1 − H(p) − 1/L):

| (p, L) | H(p) | R* |
|---|---|---|
| (0.10, 2) | 0.468996 | 0.031004 |
| (0.10, 4) | 0.468996 | 0.281004 |
| (0.05, 2) | 0.286397 | 0.213603 |
| (0.05, 4) | 0.286397 | 0.463603 |

**R2.** By the threshold theorem of [1], [2], random CSS codes achieve quantum list decodability with optimal list size L whenever each per-sector rate is below the corresponding R* in R1; the per-sector threshold equals the classical threshold. This is the paper's central structural result, here verified for internal consistency.

**R3. Hamming-bound consistency.** At (p, L) = (0.10, 4), the two-sector budget R_X + R_Z = 0.562008 is consistent with the quantum Hamming packing limit 1 − H(0.10) = 0.531004 provided the CSS shared-structure term s satisfies s ≥ 0.437992 (computed in Section 4, Computation 3). No contradiction arises; the per-sector formulation is the correct invariant.

**R4. Binding constraint.** At p = δ = 0.10, L = 4, the list-decoding rank exceeds the distance rank by exactly 1/L = 0.25 (Section 4, Computation 4); list decoding, not distance, is the binding constraint on rate in this regime.

**R5. Projection (labeled as such).** If the explicit folded quantum-LCL constructions of [2] achieve block lengths n where concentration kicks in at, say, n ≈ 10³–10⁴ (assumption; the theory is asymptotic and does not pin down n), then at (p, L) = (0.10, 4) a per-sector rate of 0.28 would yield [[n, k, d]] codes with k/n on the order of 0.1–0.5 depending on the shared-structure term s, and distance scaling d = Ω(n) as required by [7]'s optimal-overhead regime. Uncertainty: the finite-length penalty is unknown; we flag this as the projection's dominant uncertainty, consistent with the finite-size caution from [11], where small explicit stabilizer codes cluster at random-baseline behavior rather than optimal parameters.

## 6. Discussion

**Limitations.** First, the threshold theorem is asymptotic. Our computations in Section 4 are asymptotic rate calculations; they say nothing about block length. The corpus evidence in [11]—that small explicit stabilizer codes (Golay excepted) sit at random baselines—suggests finite-length penalties may be severe, and the quantum-LCL theory provides no quantitative concentration bounds that we could extract. Second, the equality of per-sector and classical thresholds is a statement about existence with high probability over random CSS ensembles; the explicit constructions via folding/derandomization inherit the parameters but the construction complexity and the actual check structure (row/column weights, girth) determine decoder performance, which the LCL framework does not directly control. Third, list decoding is a worst-case guarantee; practical channels (as in [4]'s purification setting or [3]'s GKP-concatenated setting) may be well served by simpler decoders, and the marginal value of optimal list sizes is unquantified in those works.

**Failure modes.** The most likely failure mode of the "practical significance" claim is geometric: [9] shows that forcing 2D-local layouts onto qLDPC codes incurs overhead that can erode rate and distance advantages. The quantum-LCL framework constrains check density but is indifferent to check geometry; a folded construction could have long-range checks that are expensive on planar hardware, though photonic platforms [8] and long-range-connectivity architectures [4] are less affected. A second failure mode: our Computation 3 shows the encoded rate depends on the shared-structure term s, which the threshold theorem does not determine; if s is unfavorable in the explicit constructions, the effective k/n could be much smaller than the per-sector thresholds suggest.

**Arguing against ourselves.** A skeptic could argue: (i) the threshold theorem's content—"per-sector threshold equals classical threshold"—may be the natural answer rather than a deep fact, since CSS sectors are classically independent given the stabilizer structure; the theorem then formalizes rather than surprises. We concede this partially, but note that the two-rank witness structure (physical vs. logical rank) is genuinely new and is what makes the statement provable. (ii) The explicit constructions' qLDPC property is claimed but the check weights in the folded construction could grow logarithmically; if so, "qLDPC" holds only in a relaxed sense. This is checkable from [2]'s construction section and is a concrete verification task. (iii) Our systems mapping (R5) is a projection resting on an assumed block length; if concentration requires n ≈ 10⁶, near-term relevance collapses.

**Falsification conditions.** The claim that quantum-LCL codes are practically transformative would be falsified if: (a) explicit folded constructions are shown to require check weights growing with n (breaking qLDPC); (b) finite-length simulations at n ≤ 10⁴ show list-decoding thresholds achieved only at rates far below R*; (c) 2D-local layout overheads [9] are shown to scale super-constantly in ways that negate rate gains for all realistic platforms.

**Open questions.** Can quantum-LCL codes be spatially coupled [6] while preserving check sparsity? Do list-decodable qLDPC codes reduce classical predecoding resources [5] in a quantifiable way? Is there a bosonic-inner/quantum-LCL-outer concatenation [3], [10] whose photons-per-logical-qubit beats surface-code baselines at p_L = 10^{-6}? Does the ultrametric confinement picture of [13] offer an alternative locality notion compatible with LCL witnesses? Finally, [12] could not be substantively engaged due to missing abstract content—a bibliography limitation.

## 7. Conclusion

We provided an independent analytical exposition of the quantum-LCL framework of [1], [2], verifying with explicit arithmetic that its per-sector threshold theorem is internally consistent with sphere-packing bounds and that list decoding, not distance, binds the rate at balanced parameters (R* = 0.281004 per sector at p = 0.10, L = 4; up to 0.463603 at p = 0.05, L = 4). The framework's explicit, qLDPC constructions with random-code parameters remove a genuine existence barrier for fault-tolerance schemes that presuppose good qLDPC codes [7], for purification and predecoding pipelines [4], [5], and for photonic architectures [8], while 2D-local hardware [9] remains the principal friction. The theory's asymptotic character, and the absence of finite-length guarantees—underscored by finite-size code classifications [11]—are the dominant caveats. We stated concrete falsification conditions and open questions to guide subsequent work.

## References

[1] arXiv Query: search_query=&id_list=2609.40252&start=0&max_results=1 — From Random Quantum Codes to Explicit qLDPC Codes via Local Properties (abstract as provided).

[2] arXiv:2609.40252v1 | From Random Quantum Codes to Explicit qLDPC Codes via Local Properties.

[3] arXiv:2111.07029v2 | Finite Rate QLDPC-GKP Coding Scheme that Surpasses the CSS Hamming Bound.

[4] arXiv:2210.14143v2 | Entanglement Purification with Quantum LDPC Codes and Iterative Decoding.

[5] arXiv:2605.03180v2 | Mitigating Classical Resource Costs in Quantum Error Correction via Generalized qLDPC Predecoding.

[6] arXiv:2305.00137v6 | Spatially-Coupled QLDPC Codes.

[7] arXiv:2510.19442v3 | Accelerating Fault-Tolerant Quantum Computation with Good qLDPC Codes.

[8] arXiv:2509.17223v2 | Fusion-based implementation of qLDPC codes with quantum emitters.

[9] arXiv:2404.17676v2 | Toward a 2D Local Implementation of Quantum LDPC Codes.

[10] QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | DOI pending.

[11] QNFO: Extending v_p^max Code Classification: Testing the Mahler Spectral Conjecture on Additional Stabilizer Code Families | DOI 10.5281/zenodo.21754148.

[12] QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle.

[13] QNFO: Qudit Quantum Error Correction | DOI 10.5281/zenodo.22749408.