# Modular Hyperbolic Surface Codes on Boundary-Connected Planar Modules: An Overhead and Fault-Tolerance Analysis

## Abstract

The planar surface code protects quantum information with excellent error thresholds but at a punishing physical-to-logical qubit overhead, since its encoding rate vanishes as $1/(2d^2)$ for distance $d$. Recent work on boundary-connected planar modules [1,4] proposes a route to low overhead: partition a processor into flat Euclidean modules, wire sparse static connections between module boundaries, and thereby realize semi-hyperbolic surface and color codes that combine positive encoding rate with planar fabricability. In this paper we provide an independent quantitative analysis of that proposal. We derive closed-form overhead ratios between modular codes with rate $k/n = 1/16$ and distance $d \geq 22$ and the rotated surface code, obtaining a $57.8\times$ raw qubit-count reduction for a twelve-logical-qubit register, consistent with the $>30\times$ claim of [1,4] under conservative assumptions. We further model elevated inter-module seam error rates as a mixture noise channel and show, via explicit arithmetic on a phenomenological scaling ansatz, that seam rates up to roughly five times the bulk rate degrade the logical error rate by only about $48\times$ at distance $22$ — a cost easily absorbed by the qubit savings. We compare against bivariate bicycle codes, cyclic-topology codes, Cornucopia-style LDPC codes, and entanglement-assisted schemes, and identify the seam-error threshold and decoder generalization as the decisive open questions.

## 1. Introduction

Quantum error correction (QEC) is the accepted path to fault-tolerant quantum computation, but the leading practical code — the planar surface code — encodes logical information at a rate that decays quadratically with distance. For a target logical error rate, the required distance grows logarithmically in the circuit depth of the computation, and the physical qubit count grows as approximately $2d^2$ per logical qubit. At distance $d = 22$, a single logical qubit already costs on the order of $10^3$ physical qubits, and a useful register of many logical qubits multiplies this cost directly since the planar surface code is essentially a rate-$1/d^2$ code.

A family of recent proposals attacks this overhead problem from several directions: low-density parity-check (LDPC) codes with constant or slowly decaying rate [2,3,5], spacetime-optimized fault-tolerance protocols [6], measurement-free code switching [8], trivalent planar architectures [9], entanglement-assisted constructions [11], and continuous-time correction schemes [10]. Among these, the modular approach of [1,4] is architecturally distinctive: it retains the planar, nearest-neighbor-friendly fabrication model of the surface code while recovering a finite encoding rate by gluing many flat modules together through sparse boundary connections, producing codes that live on a hyperbolic-like quotient geometry — "semi-hyperbolic" codes.

The contribution of this paper is not a new code family but an independent, fully explicit numerical analysis of the modular proposal. We ask three questions. First, how large is the qubit-overhead reduction relative to the surface code, and how sensitive is it to assumptions about module size and seam sparsity? Second, how much logical error-rate penalty is incurred when inter-module seam qubits suffer elevated error rates, and does this penalty threaten the overhead advantage? Third, how does the modular design compare quantitatively with competing low-overhead codes such as the $[[288,12,18]]$ bivariate bicycle code and hardware-efficient LDPC families [5]? We answer each with derivations in which every input number is stated and every arithmetic step shown, and we clearly separate computed results from labeled projections.

## 2. Background and Related Work

**The modular semi-hyperbolic proposal [1,4].** The central reference for this analysis demonstrates that partitioning a quantum processor into flat Euclidean modules and wiring sparse, static boundary connections between them yields modular hyperbolic surface and color codes built on new semi-hyperbolic code families. Circuit-level simulations with modular syndrome extraction and neural-network and matching decoders reportedly show a tenfold-or-better overhead reduction over the surface code even with elevated seam error rates, and projections to rate $k/n = 1/16$ and distance $d \geq 22$ exceed both the rate and distance of the $[[288,12,18]]$ two-gross bivariate bicycle code while preserving mostly nearest-neighbor gates within modules. The work also introduces fault-tolerant logical operations via code automorphisms ("walking circuits") and a modular extractor system roughly $4.5\times$ smaller than the code. Our paper takes these claims as inputs and subjects the underlying arithmetic to independent scrutiny.

**Experimental demonstrations of low-overhead QEC [2].** Recent experiments have demonstrated QEC codes beyond the surface-code paradigm, motivated by the same fragility-and-overhead argument that motivates [1,4]. The experimental context matters for our analysis because modular codes require inter-module wiring whose fidelity has no direct surface-code analogue; experimental platforms demonstrating non-planar or long-range connectivity, even at small scale, are the natural testbeds for seam-error models of the kind we formalize in Section 3.

**Cyclic-topology codes [3].** This work scales the five-qubit perfect code through increasing-weight cyclic stabilizers, obtaining resource-efficient small-block codes. These occupy the opposite design point from modular semi-hyperbolic codes: small $n$ with growing stabilizer weight versus large $n$ with bounded weight. Our Section 4 comparison makes explicit that the two approaches trade decoder complexity and stabilizer measurement depth against raw qubit count, and that modular codes win decisively on the latter for multi-logical-qubit registers.

**Cornucopia codes [5].** The Cornucopia family targets the same trade-off triangle — encoding efficiency, error threshold, hardware feasibility — that [1,4] navigates geometrically. Cornucopia codes achieve very low overhead as LDPC codes but generally require qubit connectivity that planar platforms do not natively provide. The modular proposal can be read as a hardware-constrained answer to the same question Cornucopia answers code-theoretically: how to get high rate without abandoning planar fabrication. Our analysis in Section 5 quantifies how much rate the modular approach sacrifices relative to unconstrained LDPC designs in exchange for near-planarity.

**Spacetime lifting and fault complexes [6].** Fault tolerance is a spacetime problem, and fault complexes treat correction protocols as single homological spacetime objects. This viewpoint is directly relevant to modular codes: the seam connections are static in space but their syndrome-extraction schedule determines whether seam errors propagate as correlated spacetime faults. Our mixture-noise model in Section 3 is a coarse-grained version of the spacetime error analysis that a fault-complex treatment would make precise, and we flag this as a limitation.

**Silicon colour centre architectures [7].** A platform-level perspective: silicon colour centres propose distributing high-quality entanglement at scale on a single technological platform. Modular QEC codes presuppose exactly such a distribution primitive — reliable inter-module links — whether implemented as wired couplers or photonic channels. The architectural fit between [7] and [1,4] suggests that seam error rates are a platform parameter that must be characterized empirically before the overhead projections of Section 5 can be trusted.

**Measurement-free code switching [8].** Universal computation with transversal gates is blocked by the Eastin–Knill theorem, and magic-state distillation is expensive. The measurement-free code-switching protocol of [8] offers a low-overhead route to universality that is complementary to the modular memory of [1,4]: the latter provides dense logical storage, the former provides low-overhead logical processing. The walking-circuit automorphism gates of [1,4] similarly sidestep distillation for a restricted gate set; combining the two is an open architectural question we return to in Section 6.

**Trivalent planar architectures [9].** This work shows that degree-three connectivity suffices for surface-code-style logical operations on planar registers with multiple logical qubits. It sharpens the connectivity question for modular codes: the intra-module gates in [1,4] are mostly nearest-neighbor, and the inter-module seams add a small number of additional connections per boundary qubit. Whether the resulting maximum degree stays within trivalent constraints determines whether modular codes inherit the layout results of [9]; our seam-sparsity model in Section 3 is designed to make this checkable.

**Continuous-time QEC [10].** Treating noise and correction as continuous processes with weak measurement and feedback offers an alternative to the discrete syndrome-extraction rounds assumed in [1,4]. In a modular architecture, continuous-time correction could in principle ameliorate seam faults by localizing them in time, but it also changes the decoder problem fundamentally; we treat it as an out-of-scope alternative and note it as a sensitivity of our circuit-level assumptions.

**Entanglement-assisted QEC [11].** Entanglement-assisted codes use pre-shared entanglement with a reference to build codes from arbitrary classical quaternary codes. This is conceptually adjacent to the modular approach: an inter-module seam connection that distributes entanglement between modules plays a resource role analogous to ebits in entanglement-assisted constructions. If seam links are noisy, the entanglement-assisted formalism [11] provides a principled way to budget their imperfection, which we adopt heuristically in our mixture model.

**QNFO corpus context [12,13,14].** Prior QNFO analyses of thermodynamic and informational bottlenecks in scalable fault tolerance [12], thermodynamic and topological constraints [13], and geometric orientation codes [14] frame overhead reduction as an information-thermodynamic problem: every physical qubit carries a maintenance cost, and topological code families differ in how efficiently they convert physical resources into protected logical information. The modular codes analyzed here are a concrete instantiation of the topological lever identified in [13]: changing the underlying geometry from Euclidean to semi-hyperbolic changes the rate–distance scaling itself rather than optimizing within fixed scaling.

## 3. Methods

### 3.1 Code and architecture model

We model the modular architecture of [1,4] as follows. The processor consists of $M$ identical square modules, each a flat patch of $s \times s$ data-qubit sites supporting a local surface-code-like tiling. Boundary qubits of adjacent modules are joined by sparse static two-qubit connections ("seams"). The quotient of the resulting cellulation has negative scalar curvature in the large, so the joined code behaves semi-hyperbolically: its encoding rate $k/n$ approaches a positive constant while its distance $d$ grows with linear system size.

We assume the reported target parameters of [1,4] as inputs: encoding rate $k/n = 1/16$ and distance $d \geq 22$ at the projection scale, with $k = 12$ logical qubits as the comparison register (matching the $[[288,12,18]]$ bivariate bicycle code).

### 3.2 Seam-error mixture model

Let the bulk physical error rate be $p$ and the seam error rate be $p_{\mathrm{seam}}$, with $p_{\mathrm{seam}} = \lambda p$ where $\lambda \geq 1$ is the seam penalty factor. Let $f$ be the fraction of physical qubits that lie on seams. The effective error rate experienced by a randomly chosen qubit is the mixture

$$p_{\mathrm{eff}} = p(1-f) + p_{\mathrm{seam}} f = p\bigl(1 - f + \lambda f\bigr) = p\bigl(1 + (\lambda - 1)f\bigr).$$

We estimate $f$ from module geometry. A square module of side $s$ has $4s$ boundary qubits out of $s^2$ total; if a fraction $\rho$ of boundary qubits carry seam connections, then

$$f = \frac{4\rho s}{s^2} = \frac{4\rho}{s}.$$

For our numerical work we take $s = 10$ and $\rho = 0.25$, giving $f = 4 \times 0.25 / 10 = 0.1$; we state this as an assumption, not a measurement.

### 3.3 Logical error scaling ansatz

For circuit-level noise below threshold, the logical error rate per syndrome round of a topological code at distance $d$ is well fit by

$$p_L(d, p_{\mathrm{eff}}) \approx A \left(\frac{p_{\mathrm{eff}}}{p_{\mathrm{th}}}\right)^{(d+1)/2},$$

with threshold $p_{\mathrm{th}} = 10^{-2}$ and prefactor $A$ of order $0.1$ for surface-code-like circuits. We use $A = 0.1$ throughout and hold it fixed across architectures so that architecture comparisons depend only on the exponent and the effective rate; absolute values should be read as order-of-magnitude estimates, which we label as such.

### 3.4 Overhead accounting

For the rotated surface code, the number of physical qubits per logical qubit at distance $d$ is

$$n_{\mathrm{surf}}(d) = d^2 + (d-1)^2.$$

For a modular code with rate $k/n = 1/16$, the physical count for $k$ logical qubits is $n_{\mathrm{mod}} = 16k$. The overhead ratio is $R = k \cdot n_{\mathrm{surf}}(d) / n_{\mathrm{mod}}$.

## 4. Analysis

### 4.1 Surface-code overhead at distance 22

Input: $d = 22$ (target distance from [1,4], chosen to exceed the $d = 18$ of the two-gross bivariate bicycle code).

$$n_{\mathrm{surf}}(22) = 22^2 + 21^2 = 484 + 441 = 925.$$

So one distance-$22$ surface-code logical qubit costs $925$ physical qubits. For a $k = 12$ register:

$$N_{\mathrm{surf}} = 12 \times 925 = 11100.$$

### 4.2 Modular overhead at rate $1/16$

Input: $k/n = 1/16$ and $k = 12$ (both from [1,4]).

$$n_{\mathrm{mod}} = \frac{k}{k/n} = \frac{12}{1/16} = 12 \times 16 = 192.$$

Raw overhead ratio:

$$R = \frac{11100}{192} = 57.8125 \approx 57.8\times.$$

This exceeds the $>30\times$ claim of [1,4]; the discrepancy is attributable to their accounting including the modular extractor system (reported $\approx 4.5\times$ smaller than the code, i.e., ancilla overhead not included in our $n_{\mathrm{mod}} = 192$ data-qubit count) and to per-logical-qubit distance variation in the modular code. As a conservative bound: the ratio stays at or above $30\times$ provided

$$n_{\mathrm{mod}} \leq \frac{11100}{30} = 370,$$

i.e., provided the true modular implementation uses no more than $370$ physical qubits for $12$ logical qubits at $d \geq 22$ — nearly twice our nominal $192$, leaving substantial slack for ancillas and extractors.

### 4.3 Comparison with the bivariate bicycle code

Input: the $[[288,12,18]]$ code (cited in [1,4]). Its rate is

$$\frac{k}{n} = \frac{12}{288} = \frac{1}{24} \approx 0.0417,$$

versus the modular rate $1/16 = 0.0625$; the modular code is $24/16 = 1.5\times$ more efficient in rate. Its distance is $18$ versus the modular $d \geq 22$. For equal logical protection one would compare physical counts at matched logical error rate rather than matched $n$; at matched $n = 288$ the modular code would encode $288/16 = 18$ logical qubits, i.e., $18/12 = 1.5\times$ more logical qubits than the bicycle code, at higher distance. The bicycle code's advantage is its fully translational, weight-bounded structure; the modular code's advantage is planar fabricability.

### 4.4 Seam-error penalty

Inputs: $p = 10^{-3}$ (representative bulk physical error rate for circuit-level noise), $\lambda = 5$ (elevated seam rate, i.e., $p_{\mathrm{seam}} = 5 \times 10^{-3}$), $f = 0.1$ (Section 3.2), $p_{\mathrm{th}} = 10^{-2}$, $A = 0.1$, $d = 22$.

Step 1 — effective rate:

$$p_{\mathrm{eff}} = p\bigl(1 + (\lambda - 1)f\bigr) = 10^{-3} \times \bigl(1 + 4 \times 0.1\bigr) = 10^{-3} \times 1.4 = 1.4 \times 10^{-3}.$$

Step 2 — modular logical error rate per round:

$$p_L^{\mathrm{mod}} = 0.1 \times \left(\frac{1.4 \times 10^{-3}}{10^{-2}}\right)^{11.5} = 0.1 \times \left(0.14\right)^{11.5}.$$

Compute $\ln(0.14) = \ln(14) - \ln(100) = 2.6391 - 4.6052 = -1.9661$. Then $11.5 \times (-1.9661) = -22.610$, and $e^{-22.610} \approx 1.51 \times 10^{-10}$. Hence

$$p_L^{\mathrm{mod}} \approx 0.1 \times 1.51 \times 10^{-10} = 1.51 \times 10^{-11}.$$

Step 3 — surface-code baseline at the same $d = 22$, $p = 10^{-3}$, no seams:

$$p_L^{\mathrm{surf}} = 0.1 \times \left(0.1\right)^{11.5} = 0.1 \times 10^{-11.5} = 0.1 \times 3.16 \times 10^{-12} = 3.16 \times 10^{-13}.$$

Step 4 — penalty ratio:

$$\frac{p_L^{\mathrm{mod}}}{p_L^{\mathrm{surf}}} = \frac{1.51 \times 10^{-11}}{3.16 \times 10^{-13}} = 47.8.$$

So a fivefold seam-rate penalty on $10\%$ of qubits costs a factor of about $48$ in logical error rate at $d = 22$ — while saving $57.8\times$ in qubits. Equivalently, one could raise the modular distance slightly to recover the logical rate and still dominate the surface code in overhead (see Section 5 projection).

### 4.5 Seam tolerance bound

For the modular code to match the surface-code logical rate, we need $(p_{\mathrm{eff}}/p_{\mathrm{th}})^{11.5} \leq (p/p_{\mathrm{th}})^{11.5}$, i.e., $p_{\mathrm{eff}} \leq p$, i.e., $\lambda = 1$ — impossible with seams. Instead, ask what distance $d_{\mathrm{mod}}$ restores parity:

$$0.1\,(0.14)^{(d_{\mathrm{mod}}+1)/2} = 3.16 \times 10^{-13} \implies (0.14)^{(d_{\mathrm{mod}}+1)/2} = 3.16 \times 10^{-12}.$$

Taking $\log_{10}$: $\log_{10}(0.14) = -0.8561$, so

$$(d_{\mathrm{mod}}+1)/2 = \frac{-11.5}{-0.8561} = 13.433 \implies d_{\mathrm{mod}} = 25.9 \approx 26.$$

At rate $1/16$, distance $26$ requires linear scale-up by $26/22 = 1.18$, hence roughly $n_{\mathrm{mod}} \approx 192 \times (26/22)^2 = 192 \times 1.397 = 268$ physical qubits (area scaling assumption), still giving

$$\frac{11100}{268} = 41.4\times$$

overhead reduction with parity in logical error rate. All numbers in this subsection are projections under the stated ansatz and geometry assumptions.

## 5. Results

**Computed results (Sections 4.1–4.4).**

- A distance-$22$ rotated surface code logical qubit costs $n_{\mathrm{surf}} = 925$ physical qubits; a $12$-logical-qubit register costs $11100$.
- A modular code at $k/n = 1/16$, $k = 12$ uses $n_{\mathrm{mod}} = 192$ physical qubits, a raw overhead ratio of $57.8\times$.
- The ratio remains $\geq 30\times$ for any modular implementation up to $370$ physical qubits, giving headroom for ancillas.
- The $[[288,12,18]]$ bicycle code has rate $1/24 \approx 0.0417$ and $d = 18$; the modular code is $1.5\times$ higher-rate and at least $4$ higher in distance.
- Under the mixture model with $p = 10^{-3}$, $\lambda = 5$, $f = 0.1$: $p_{\mathrm{eff}} = 1.4 \times 10^{-3}$, $p_L^{\mathrm{mod}} \approx 1.51 \times 10^{-11}$ per round versus $p_L^{\mathrm{surf}} \approx 3.16 \times 10^{-13}$, a $47.8\times$ logical penalty — smaller than the $57.8\times$ qubit saving.

**Labeled projections (Section 4.5, assumptions: ansatz of Section 3.3 with $A = 0.1$, $p_{\mathrm{th}} = 10^{-2}$; area scaling of module count; $f = 0.1$; uncertainty at least a factor of a few from the unknown prefactor $A$ and from unmodeled correlated seam faults).**

- Distance parity with the seam-free surface code is recovered at $d_{\mathrm{mod}} \approx 26$, costing $n_{\mathrm{mod}} \approx 268$ qubits and yielding a $41.4\times$ overhead reduction at equal logical error rate.
- The seam penalty grows linearly in $(\lambda - 1)f$ in $p_{\mathrm{eff}}$; at $\lambda = 10$, $f = 0.1$, $p_{\mathrm{eff}} = 1.9 \times 10^{-3}$, the same arithmetic gives $p_L^{\mathrm{mod}} \approx 0.1 \times (0.19)^{11.5}$; with $\ln(0.19) = -1.6607$, $11.5 \times (-1.6607) = -19.10$, $e^{-19.10} \approx 5.0 \times 10^{-9}$, so $p_L^{\mathrm{mod}} \approx 5.0 \times 10^{-10}$, a $1580\times$ penalty — still recoverable by modest distance increase but indicating that seam quality, not bulk quality, is the binding constraint.

## 6. Discussion

**Limitations.** Our analysis inherits the phenomenological ansatz of Section 3.3, whose prefactor $A$ and exponent are approximations valid below threshold and away from $d$-dependent crossover effects; the modular semi-hyperbolic codes of [1,4] are not surface codes, and their true circuit-level constants may differ by factors we cannot compute without their simulation data. The seam fraction $f = 0.1$ is a modeling assumption, not a measurement; real module layouts with routing constraints could have $f$ several times larger, and the penalty scales linearly in $f$. Correlated errors along seams — a single seam defect producing multi-qubit faults — are entirely absent from our mixture model, yet they are precisely the failure mode that decoders trained on bulk noise handle worst; the neural-network decoders of [1,4] must be demonstrably seam-aware for our conclusions to hold.

**Failure modes.** The overhead advantage collapses if (i) seam error rates exceed roughly an order of magnitude of bulk rates at $f \approx 0.1$, as the $\lambda = 10$ projection shows; (ii) the modular extractor system, though $4.5\times$ smaller than the code, still consumes ancilla qubits that erode the $370$-qubit slack budget of Section 4.2; (iii) walking-circuit automorphism gates require temporary non-planar connectivity or measurement depths that dominate the memory-cycle cost. A fault-complex spacetime analysis [6] would be required to bound gate-induced seam faults, and we have not performed one.

**What would falsify the claims.** Our central quantitative claim — a $30\times$–$58\times$ overhead reduction at competitive logical error rates — is falsified if circuit-level simulation of the actual modular codes shows logical error rates worse than the surface code by more than the qubit-saving factor at matched $k = 12$, or if the achieved distance at rate $1/16$ falls below $22$ in practice. It is also falsified empirically if platforms such as silicon colour centres [7] cannot demonstrate seam links with $\lambda \lesssim 5$–$10$.

**Arguing against ourselves.** A skeptic could note that unconstrained LDPC families such as Cornucopia codes [5] achieve comparable or better rates without any seam hardware at all, and that the modular approach pays a real hardware tax (seams, module boundaries, extractor system) to solve a problem — planar fabricability — that may become moot as fabrication matures. The cyclic small-block codes of [3] offer a different escape: many small cheap blocks with classical post-processing. And the entanglement-assisted framework [11] suggests that if inter-module entanglement distribution is the scarce resource, one should spend it deliberately as ebits rather than as fixed geometry. Against this we argue that near-term hardware is overwhelmingly planar, that trivalent-connectivity results [9] show planar layouts are more capable than often assumed, and that a dense modular memory is a natural storage tier complementing measurement-free processing schemes [8] and continuous-time correction variants [10]. The thermodynamic framing of [12,13] supports the same conclusion: reducing physical qubit count reduces the dominant maintenance cost, and geometric innovation [14] is the highest-leverage knob.

**Open questions.** What is the true seam-error threshold $\lambda_{\max}(f, d)$ beyond which modular codes lose to the surface code? Can walking circuits be made fault-tolerant to the same pseudo-threshold as the memory? Do modular codes admit the decoder portability (matching to neural) that [1,4] report, at the projected scale? How do modular memories interface with magic-state factories in a full universal architecture [8]?

## 7. Conclusion

We performed an independent, fully explicit overhead and fault-tolerance analysis of boundary-connected planar modular semi-hyperbolic codes. With every input stated and every step shown, we find a raw $57.8\times$ qubit-count reduction over the distance-$22$ rotated surface code for a twelve-logical-qubit register at rate $1/16$, robust down to $>30\times$ under a doubled ancilla budget; a $47.8\times$ logical error penalty under a fivefold seam-rate penalty on $10\%$ of qubits, which is more than offset by the qubit savings; and a projected $41.4\times$ reduction at full logical-error parity via a modest distance increase to $d \approx 26$. The modular approach dominates the $[[288,12,18]]$ bicycle code on both rate ($1.5\times$) and distance ($\geq 22$ vs $18$) while retaining planar fabrication. The decisive empirical unknown is the seam error rate; the decisive theoretical unknown is correlated seam-fault decoding. Both are tractable, and both are the right next targets for this promising architecture.

## References

[1] arXiv Query: search_query=&id_list=2610.03682&start=0&max_results=1 — "Low-Overhead Quantum Error Correction with Boundary-Connected Planar Modules" (abstract as provided).

[2] arXiv:2505.09684v1 | Demonstration of low-overhead quantum error correction codes.

[3] arXiv:2211.03094v3 | Low-overhead quantum error correction codes with a cyclic topology.

[4] arXiv:2610.03682v1 | Low-Overhead Quantum Error Correction with Boundary-Connected Planar Modules.

[5] arXiv:2608.02773v2 | Quantum error correction at ultra-low overhead.

[6] arXiv:2606.06365v2 | A framework for low-overhead quantum fault tolerance via spacetime lifting.

[7] arXiv:2311.04858v1 | Scalable Fault-Tolerant Quantum Technologies with Silicon Colour Centres.

[8] arXiv:2411.13142v4 | Measurement-free code-switching for low overhead quantum computation using permutation invariant codes.

[9] arXiv:2607.15044v2 | Towards logical entanglement creation in trivalent planar architectures.

[10] arXiv:1311.2485v2 | Continuous-time quantum error correction.

[11] arXiv:1610.04013v1 | Entanglement-Assisted Quantum Error-Correcting Codes.

[12] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898.

[13] QNFO: Thermodynamic and Topological Constraints on Biological Quantum Processing | DOI 10.5281/zenodo.17989524.

[14] QNFO: Computational Simulation of Geometric Orientation Codes | DOI 10.5281/zenodo.19487443.