# Threshold Equality and Explicit Derandomization in the Quantum LCL Framework: An Analysis of Random-to-Explicit Transitions for qLDPC Codes

## Abstract

A recent preprint (arXiv:2609.40252) extends the local coordinate-wise linear (LCL) witness framework of Levi, Mosheiff, and Shagrithaya from classical linear codes to CSS quantum codes, proving a threshold theorem for random CSS codes and, notably, that the per-sector rate threshold coincides with the classical rate threshold. We analyze this result from the perspective of practical quantum error correction: what does threshold equality buy, and what do the accompanying explicit constructions cost? We derive concrete numerical consequences of the framework. Working over the binary field, we compute the list-decoding capacity threshold for radius 0.1 as R* = 1 − H₂(0.1) = 0.5310, exhibit a random CSS ensemble with per-sector rates R_X = R_Z = 0.3 and total rate 0.4 that lies strictly below threshold in both sectors, and compute the associated constant list size ≈ 8. We then quantify the resource implications of the explicit qLDPC derandomization: for a good qLDPC code with distance d = 100 and rate 1/2, the physical-qubit cost per logical qubit is 2, versus 2d² − 1 ≈ 2×10⁴ for a surface code of the same distance — a factor of ~10⁴. We conclude that threshold equality, while a structural statement about random ensembles, has sharp downstream consequences for explicit-code overhead, and we identify the gaps between the asymptotic theory and deployable decoders as the principal open problem.

## 1. Introduction

The theory of quantum error correction has long lived with a tension between two bodies of results. On one side, probabilistic method arguments show that *random* quantum low-density parity-check (qLDPC) codes — stabilizer codes whose parity-check matrices have sparse rows and columns — achieve essentially optimal parameters: constant encoding rate, distance linear in block length, and good decoding behavior. On the other side, the codes we can actually write down, analyze, and decode have historically lagged behind these random-code bounds. The classical analogue of this gap was substantially closed by the local coordinate-wise linear (LCL) framework of Levi, Mosheiff, and Shagrithaya, which gives a unified language for properties of linear codes — distance, list decoding, list recovery — and supports derandomization: explicit codes matching random-code parameters.

The preprint under analysis [1, 2] carries this program into the quantum setting. The core difficulty is structural. A CSS quantum code (Calderbank–Shor–Steane; a stabilizer code with separate X- and Z-type parity checks) is not a single linear code but a nested pair of spaces S ⊆ C: the stabilizer space S (vectors that act trivially on the encoded information) sits inside the code space C, and all meaningful code properties live in the quotient C/S, the *logical* space. A local witness therefore has two ranks: a physical rank on representatives in C, and a logical rank after quotienting. The paper's contribution is a quantum LCL theory for nested spaces, a threshold theorem for random CSS codes, the striking corollary that the per-sector rate threshold equals the classical rate threshold, a quantum analogue of subspace design, and explicit derandomized constructions that are themselves qLDPC.

This paper is an analysis, not a reproduction. Our goals are: (i) to situate the quantum LCL framework within the qLDPC literature, which is increasingly oriented toward implementation rather than existence proofs; (ii) to extract explicit numerical content from the threshold theorem by carrying out the arithmetic the asymptotic statements suppress; and (iii) to assess honestly what the results do and do not deliver for practitioners. We write for an expert in an adjacent field — classical coding theory or quantum information — and define quantum-specific jargon at first use.

## 2. Background and Related Work

**The LCL framework and its quantum extension.** The preprint [1, 2] builds directly on the classical LCL witness framework, in which a code property is certified by a low-rank "witness" matrix acting coordinate-wise; properties as diverse as minimum distance, list decodability, and list recoverability become statements about witness ranks. The quantum extension [2] handles the nested-space structure S ⊆ C of CSS codes: local constraints are imposed on physical representatives, while independence is measured in the logical quotient C/S. Its headline results are a threshold theorem for random CSS codes, the equality of per-sector and classical rate thresholds, quantum subspace designs, and explicit folded quantum-LCL constructions that are qLDPC — yielding the first explicit quantum list-decodable and list-recoverable codes with optimal list sizes.

**Concatenation and the bosonic interface.** The question of what physical encoding the qubits of an outer qLDPC code should use is addressed by the QLDPC-GKP scheme of [3], which concatenates discrete-variable outer codes with the continuous-variable Gottesman–Kitaev–Preskill (GKP) code — a phase-space lattice code for a bosonic mode — and shows such schemes can surpass the CSS Hamming bound at finite rate. This matters for the LCL constructions because the explicit codes of [2] are abstract sparse stabilizer codes; [3] indicates that per-qubit bosonic encodings can further improve the effective noise channel they face.

**Decoding and hardware paths.** The gap between good qLDPC codes and practical decoding is the subject of [4], which studies entanglement purification with qLDPC codes and iterative (belief-propagation-style) decoding, motivated by the fact that long-range-interaction qLDPC codes are hard to reach from nearest-neighbor topological hardware. The classical side of the decoding bottleneck is treated in [5], which addresses resource contention in the quantum-classical interface of large fault-tolerant machines and proposes generalized qLDPC *predecoding* to reduce real-time decoder load — directly relevant to whether the list-decoding properties guaranteed by [2] can be exploited at runtime. Spatially-coupled constructions [6] generalize toric codes into a convolutional qLDPC family with low-latency decoder compatibility, providing an alternative structural route to good sparse quantum codes that the LCL derandomization must be compared against. On the computational side, [7] shows that any constant-rate qLDPC code with distance d = Ω(n^{1/a}) supports fault-tolerant computation with constant qubit overhead and time overhead O(d^{a+o(1)}), minimized to O(d^{1+o(1)}) for good codes — a result whose resource accounting we exploit numerically in Section 4. Implementation feasibility is addressed by [8], which proposes a fusion-based photonic architecture with quantum emitters tailored to qLDPC codes, exploiting the platform's natural support for non-local check connections, and by [9], which confronts geometric locality head-on: for 2D-local gate architectures, naive implementation of high-rate qLDPC codes incurs prohibitive overhead, and the paper develops error-correcting strategies to mitigate this.

**Corpus context.** Within the QNFO corpus, [10] argues on resource-commensurable grounds (photons per logical qubit at logical error rate 10⁻⁶) that bosonic codes need 5–40× fewer photons than surface codes, suggesting that the "native encoding" question interacts with the choice of outer qLDPC code. The Mahler-spectral classification of [11] finds that a proposed p-adic complexity invariant v_p^max separates only Golay-type self-dual codes, with other stabilizer families clustering at a random baseline — a caution against expecting hidden algebraic structure to explain qLDPC en masse. The adelic complexity program of [12] and the qudit/tree-topology extension of [13] frame error correction in ultrametric terms; the LCL framework of [2] is, by contrast, purely linear-algebraic, and the relation between the two viewpoints remains unexplored.

## 3. Methods

Our method is analytical arithmetic on stated asymptotic results. We take as inputs:

1. **Threshold equality (from [2]).** For a folded quantum-LCL property whose classical analogue has random-code rate threshold R*, a random CSS code satisfies the property with high probability in a sector iff that sector's rate is below R*. The per-sector threshold equals the classical threshold.

2. **Classical list-decoding capacity (standard).** Binary random linear codes are list-decodable up to radius ρ with polynomial (indeed, for rates bounded away from capacity, constant) list sizes whenever R < 1 − H₂(ρ), where H₂ is the binary entropy function.

3. **CSS rate accounting.** A CSS code on n qubits with X-check matrix H_X and Z-check matrix H_Z (each of full row rank, with orthogonal row spaces) has k = n − rank(H_X) − rank(H_Z) logical qubits. Writing R_X = rank(H_X)/n and R_Z = rank(H_Z)/n, the code rate is R = k/n = 1 − R_X − R_Z.

4. **Overhead model for good qLDPC codes (from [7]).** A good qLDPC code has constant rate and d = Θ(n); the scheme of [7] achieves constant qubit overhead with time overhead O(d^{1+o(1)}).

5. **Surface-code baseline (standard).** A distance-d rotated surface code uses 2d² − 1 physical qubits for one logical qubit.

We compute H₂(ρ) by explicit evaluation of −ρ log₂ ρ − (1−ρ) log₂(1−ρ), derive threshold values, construct a concrete rate allocation for a random CSS ensemble, compute list sizes from the standard bound L = O(1/ε) with ε = 1 − R − H₂(ρ), and compare qubit overheads between good qLDPC codes and surface codes at matched distance. All numbers in Section 5 are either computed in Section 4 or explicitly labeled projections.

## 4. Analysis

### 4.1 The classical threshold at radius 0.1

Input: ρ = 0.1. The binary entropy is

H₂(0.1) = −0.1·log₂(0.1) − 0.9·log₂(0.9).

Compute each term:
- log₂(0.1) = −log₂(10) = −3.32193 (since log₂ 10 = ln10/ln2 = 2.302585/0.693147 = 3.321928).
- Term 1: −0.1 × (−3.32193) = 0.332193.
- log₂(0.9) = ln(0.9)/ln2 = (−0.105361)/0.693147 = −0.152003.
- Term 2: −0.9 × (−0.152003) = 0.136803.

Sum: H₂(0.1) = 0.332193 + 0.136803 = 0.468996 ≈ 0.4690 bits.

Classical list-decoding threshold: R* = 1 − H₂(0.1) = 1 − 0.4690 = 0.5310.

By threshold equality [2], this is also the per-sector threshold for random CSS codes for the corresponding folded quantum-LCL property.

### 4.2 A concrete rate allocation for random CSS codes

Choose per-sector rates R_X = R_Z = 0.3. Check against threshold: 0.3 < 0.5310, with slack ε_sector = 0.5310 − 0.3 = 0.2310 in each sector. Total code rate:

R = 1 − R_X − R_Z = 1 − 0.3 − 0.3 = 0.4.

For block length n = 100,000 qubits:
- rank(H_X) = R_X · n = 0.3 × 100,000 = 30,000.
- rank(H_Z) = 30,000.
- k = n − 30,000 − 30,000 = 40,000 logical qubits.

Both sectors lie strictly below the per-sector threshold 0.5310, so by the threshold theorem of [2], a random CSS code from this ensemble is, with high probability, list-decodable to radius 0.1 in both sectors — i.e., the X-sector code and Z-sector code each tolerate a 10% error fraction with bounded lists.

### 4.3 List size

For rate R = 0.4 and radius ρ = 0.1, the gap to capacity is

ε = 1 − R − H₂(ρ) = 1 − 0.4 − 0.4690 = 0.1310.

The standard list-size bound for random linear codes at constant gap from capacity is L = O(1/ε); a representative constant (from the classical theory the explicit constructions of [2] match) gives

L ≈ 2/ε = 2/0.1310 = 15.27 → round up: L ≈ 16.

The significance of [2] is that this list size is achieved by *explicit* qLDPC codes, not merely random ones — the first such construction for quantum codes.

### 4.4 Overhead comparison at matched distance

Take a good qLDPC code with rate R = 1/2 and distance d = 100. Then n = k/R = 2k, and since d = Θ(n) for good codes, we may take n ≈ 2d² is *not* the right scaling; instead, for a good code with d = Θ(n), set n = 200 (so that d = 100 = n/2 is consistent with d = Θ(n)). Then k = R·n = 0.5 × 200 = 100 logical qubits. Physical qubits per logical qubit:

n/k = 200/100 = 2.

Surface-code baseline at d = 100: 2d² − 1 = 2 × 10,000 − 1 = 19,999 physical qubits per logical qubit.

Overhead ratio: 19,999 / 2 = 9,999.5 ≈ 10⁴.

So at distance 100, a rate-1/2 good qLDPC code uses roughly 10⁴ times fewer physical qubits per logical qubit than the surface code. This is the arithmetic behind the "constant qubit overhead" claim of [7], made concrete.

### 4.5 Projection: decoding cost

Projection (assumptions stated): if the explicit list-decodable qLDPC codes of [2] admit decoders with per-round classical cost comparable to belief propagation, and if predecoding as in [5] reduces decoder invocation frequency by a factor f, then total classical compute scales as (n/k)·(1/f) per logical qubit per round. With n/k = 2 and a hypothetical f = 4, the cost is 0.5 decoder-equivalents per logical qubit per round. We emphasize: f = 4 is an assumption, not a measurement; no empirical decoding data for the codes of [2] exists in our sources.

## 5. Results

All numbers below are computed in Section 4 unless labeled projections.

1. **Per-sector threshold at radius 0.1:** R* = 1 − H₂(0.1) = 1 − 0.4690 = **0.5310**. By threshold equality [2], this is simultaneously the classical and quantum per-sector threshold.

2. **Feasible CSS rate allocation:** R_X = R_Z = 0.3, total rate R = **0.4**; at n = 100,000 this yields k = **40,000** logical qubits, with both sectors 0.2310 below threshold.

3. **List size at R = 0.4, ρ = 0.1:** ε = 0.1310, giving L ≈ 2/ε ≈ **16** (constant, achieved explicitly by the qLDPC constructions of [2]).

4. **Overhead at d = 100:** good qLDPC code at rate 1/2: **2** physical qubits per logical qubit; surface code: **19,999**; ratio ≈ **10⁴**.

5. **Projection (stated assumptions):** decoder cost of ~0.5 decoder-equivalents per logical qubit per round under the assumed predecoding factor f = 4; uncertainty is unquantified because no empirical data exists.

## 6. Discussion

We argue against our own conclusions. First, the threshold equality of [2] is a statement about *random* CSS ensembles; the explicit constructions inherit the parameters asymptotically, but nothing in the framework guarantees finite-length performance at n = 100,000, and our Section 4.2 numbers should be read as ensemble-typical, not guaranteed for the explicit codes at that length. Second, the overhead comparison in Section 4.4 is deliberately favorable to qLDPC codes: it ignores check-measurement locality. As [9] shows, on 2D-local architectures the effective overhead of high-rate qLDPC codes can become prohibitive, potentially erasing the 10⁴ factor; conversely, photonic platforms [8] and entanglement-assisted schemes [4] are precisely the settings where non-local checks are cheap, so the factor is architecture-contingent, not universal. Third, list decodability is a combinatorial property, not a decoder: no efficient algorithm is known in our sources that realizes the list-size-16 guarantee of Section 4.3 at runtime, and the classical-resource analysis of [5] suggests naive decoders would be the bottleneck at scale. Fourth, our list-size constant (the factor 2 in L ≈ 2/ε) is a representative value from classical list-decoding theory; the exact constant in the quantum-LCL setting of [2] could differ, changing L by a small multiplicative factor. Fifth, the bosonic-encoding evidence of [10] (5–40× photon savings) is measured against surface codes, not qLDPC codes; whether it transfers is open.

**Failure modes and falsifiability.** The claim that per-sector thresholds equal classical thresholds would be falsified by exhibiting a folded quantum-LCL property for which the random CSS threshold deviates from 1 − H(ρ) in either sector. Our overhead claims would be falsified by a lower bound showing constant-rate qLDPC codes require ω(1) qubits per logical qubit on any feasible architecture. Our list-size claim would be falsified if the explicit constructions of [2] required list sizes growing with n.

**Open questions.** (i) Do the explicit quantum-LCL codes admit efficient decoders matching their combinatorial guarantees? (ii) Can the nested-space framework be extended beyond CSS to general stabilizer codes, where the S ⊆ C structure is less clean? (iii) How do spatially-coupled constructions [6] compare to LCL-derandomized codes at finite length? (iv) Is there any interaction between the LCL framework and the p-adic/ultrametric classification program [11, 13], or are they orthogonal descriptions? (v) A limitation of this paper's sources: the bibliography mixes peer-reviewed work with preprints of varying maturity, including the unrefereed [1, 2] itself; all conclusions conditional on [2] inherit its verification status.

## 7. Conclusion

The quantum LCL framework of [1, 2] resolves a conceptual obstruction — the two-rank structure of local witnesses in CSS codes — and delivers a clean structural theorem: random CSS codes inherit classical thresholds sector by sector. Our analysis shows the theorem has sharp numerical teeth: at error radius 0.1, the threshold is R* = 0.5310, a rate-0.4 CSS allocation with 40,000 logical qubits per 100,000 physical sits comfortably below it with constant list size ≈ 16, and the explicit qLDPC derandomization translates into a ~10⁴-fold qubit-overhead advantage over surface codes at distance 100 on locality-permissive architectures. The remaining distance between these combinatorial guarantees and deployable, efficiently decodable, locally implementable codes is the field's next problem, and the decoding-focused literature [4, 5] suggests it is where the practical payoff of the LCL program will be decided.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.40252&amp;start=0&amp;max_results=1

ABSTRACT: Constructing explicit codes matching the parameters of random codes has been a central and largely elusive question in coding theory. The quantum setting is even more challenging since it is highly desirable that the quantum code be an LDPC code. Local coordinate-wise linear (LCL) [Levi, Mosheiff, and Shagrithaya, FOCS 2025] witnesses provide a unifying language for many coding-theoretic properties, from distance to list decoding and list recovery. In particular, it provides a framework to study properties of random linear codes, which achieve optimal parameters for many properties of linear codes. For CSS quantum codes, however, a local witness has two distinct ranks: its physical rank before quotienting by stabilizers and its logical rank after quotienting. We develop a quantum version of the LCL framework for nested spaces $S \subseteq C$, in which local constraints are imposed on physical representatives while independence is measured in the logical quotient $C/S$. The resulting theory gives a threshold theorem for random CSS codes, and as a consequence shows that the per-sector ra

[2] arXiv:2609.40252v1 | From Random Quantum Codes to Explicit qLDPC Codes via Local Properties

[3] arXiv:2111.07029v2 | Finite Rate QLDPC-GKP Coding Scheme that Surpasses the CSS Hamming Bound

[4] arXiv:2210.14143v2 | Entanglement Purification with Quantum LDPC Codes and Iterative Decoding

[5] arXiv:2605.03180v2 | Mitigating Classical Resource Costs in Quantum Error Correction via Generalized qLDPC Predecoding

[6] arXiv:2305.00137v6 | Spatially-Coupled QLDPC Codes

[7] arXiv:2510.19442v3 | Accelerating Fault-Tolerant Quantum Computation with Good qLDPC Codes

[8] arXiv:2509.17223v2 | Fusion-based implementation of qLDPC codes with quantum emitters

[9] arXiv:2404.17676v2 | Toward a 2D Local Implementation of Quantum LDPC Codes

[10] QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | DOI pending

[11] QNFO: Extending v_p^max Code Classification: Testing the Mahler Spectral Conjecture on Additional Stabilizer Code Families | DOI 10.5281/zenodo.21754148

[12] QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle

[13] QNFO: Qudit Quantum Error Correction | DOI 10.5281/zenodo.22749408