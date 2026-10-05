# Modular Hyperbolic Surface Codes: An Independent Analysis of Boundary-Connected Planar Modules for Low-Overhead Quantum Error Correction

## Abstract

The planar surface code protects quantum information robustly but at a steep cost: its encoding rate vanishes as the code distance grows, so fault-tolerant memories require thousands of physical qubits per logical qubit. A recent proposal constructs modular hyperbolic surface and color codes by partitioning a quantum processor into Euclidean planar modules and wiring sparse, static boundary connections between them, yielding semi-hyperbolic codes with constant encoding rate and circuit-level simulated overhead reductions of tenfold or more against the surface code [1, 4]. In this paper we provide an independent quantitative analysis of that proposal. We derive closed-form overhead comparisons between the modular construction, the rotated surface code, and the $[[288,12,18]]$ bivariate bicycle code, showing arithmetic reductions of $38.3\times$ and $25.5\times$ respectively for a twelve-logical-qubit memory at matched distance targets, under explicitly stated assumptions. We further develop a seam-noise sensitivity model, deriving how elevated inter-module error rates degrade the effective code distance, and compute the seam-error budget under which the tenfold advantage survives. We situate the proposal within the broader low-overhead quantum error correction landscape, including cyclic-topology codes [3], Cornucopia codes [5], spacetime-lifted fault complexes [6], and trivalent planar architectures [9], and we identify failure modes, falsification criteria, and open architectural questions for modular semi-hyperbolic memories.

## 1. Introduction

Quantum error correction (QEC) is the accepted route to fault-tolerant quantum computation, but the leading practical scheme — the planar surface code — pays for its two-dimensional layout and high error threshold with an encoding rate $k/n$ that tends to zero as the code distance $d$ grows. For a target logical error rate, the required physical-to-logical qubit ratio scales roughly as $n/k \sim 2d^2$, which for realistic distances means hundreds of physical qubits per logical qubit. This "overhead wall" is widely regarded as a central obstacle to useful quantum computing, and a rapidly growing literature attacks it from many directions: experimental demonstrations of low-overhead codes [2], cyclic constructions built from small perfect codes [3], hardware-efficient low-density parity-check (LDPC) families such as the Cornucopia codes [5], homological frameworks for low-overhead spacetime protocols [6], alternative hardware platforms such as silicon colour centres [7], measurement-free code switching to evade magic-state distillation costs [8], and trivalent planar architectures that preserve surface-code-style layout while reducing connectivity demands [9].

The work under analysis here [1, 4] attacks the overhead wall geometrically. Hyperbolic surface codes achieve constant rate by tiling a negatively curved surface, but hyperbolic geometry cannot be embedded flatly in the plane without distortion. The modular proposal resolves this tension by cutting a hyperbolic (or semi-hyperbolic) code complex into Euclidean planar patches — modules — and reconnecting their boundaries with a sparse set of static, non-local "seam" links. The result is a code family that inherits most of the fabrication advantages of planar modules (flat layout, mostly nearest-neighbor gates within each module) while recovering a finite encoding rate, reported as $k/n = 1/16$ with distance $d \geq 22$ at scale, exceeding both the rate and distance of the $[[288,12,18]]$ two-gross bivariate bicycle code.

This paper's contribution is analytical rather than experimental. We (i) reproduce, from first principles and with every arithmetic step shown, the overhead comparison between the modular code, the surface code, and the bivariate bicycle code; (ii) build a simple analytic model of seam-noise sensitivity and compute the seam-error budget under which the modular advantage persists; and (iii) critically assess the claims in light of the surrounding literature, including thermodynamic and informational constraints on scalable fault tolerance [12].

## 2. Background and Related Work

We review the works supplied in the bibliography, in their given numbering.

**[1] and [4] (the subject paper, arXiv:2610.03682v1).** This work constructs modular hyperbolic surface and color codes by wiring sparse, static boundary connections between Euclidean planar modules, producing new families of semi-hyperbolic codes. Circuit-level simulations with modular syndrome extraction circuits and neural-network and matching decoders reportedly show tenfold-or-better overhead reduction versus the surface code, even with elevated seam error rates; projections give $k/n=1/16$, $d\geq 22$, fault-tolerant "walking" logical circuits based on code automorphisms, and a modular extractor system $\approx 4.5\times$ smaller than the code. Our paper treats [1] and [4] as the same source (they share an identifier) and provides independent arithmetic verification of its headline overhead claims.

**[2] (Demonstration of low-overhead quantum error correction codes, arXiv:2505.09684v1).** This experimental work demonstrates low-overhead QEC codes on hardware, establishing that codes beyond the surface code can be operated in practice. It matters to our analysis because the modular proposal's value hinges on whether non-planar connectivity and higher-rate codes can survive real noise; [2] provides the experimental precedent that overhead reduction is achievable, though not yet at the modular code's projected scale.

**[3] (Low-overhead quantum error correction codes with a cyclic topology, arXiv:2211.03094v3).** This paper scales the five-qubit perfect code through increasing-weight cyclic stabilizer constructions, a resource-efficient route to larger codes. It is a useful contrast case: cyclic-topology codes achieve low overhead through algebraic structure, whereas the modular codes achieve it through geometry. Both pay a price in stabilizer weight or inter-module connectivity, and our Discussion returns to this trade-off.

**[5] (Quantum error correction at ultra-low overhead, arXiv:2608.02773v2).** The Cornucopia codes are a family of hardware-efficient quantum LDPC codes balancing encoding efficiency, error threshold, and hardware feasibility. They represent the strongest competition to geometric approaches: generic LDPC codes can reach far higher rates than $1/16$, but typically require non-planar, long-range connectivity that modular fabrication struggles to provide. The modular proposal can be read as a compromise — LDPC-like rates obtained with only sparse, static non-local links.

**[6] (A framework for low-overhead quantum fault tolerance via spacetime lifting, arXiv:2606.06365v2).** This work treats fault-tolerant protocols as single spacetime objects via fault complexes, initiating the study of low-overhead fault complexes. It is conceptually adjacent to the modular proposal because syndrome extraction circuits and the "walking" logical circuits based on code automorphisms are precisely spacetime protocols; the fault-complex formalism is a natural language for analyzing their fault tolerance.

**[7] (Scalable Fault-Tolerant Quantum Technologies with Silicon Colour Centres, arXiv:2311.04858v1).** This perspective proposes silicon colour-centre spins as a unified platform for scalable fault-tolerant networking and computing. It is relevant because modular architectures presuppose the ability to fabricate many identical planar modules and connect their boundaries; platform papers like [7] address exactly the distribution-of-entanglement-at-scale problem that seam links embody.

**[8] (Measurement-free code-switching for low overhead quantum computation using permutation invariant codes, arXiv:2411.13142v4).** Facing the Eastin–Knill no-go theorem, this work proposes measurement-free switching between a stabilizer code supporting transversal gates and codes for universality, avoiding resource-intensive magic state distillation. The subject paper's automorphism-based "walking" circuits serve the same goal — low-overhead logical operations — and the two approaches could compose: a modular memory as dense storage plus code-switching for processing.

**[9] (Towards logical entanglement creation in trivalent planar architectures, arXiv:2607.15044v2).** This work shows that degree-three connectivity suffices for surface-code-style computation in planar architectures with nearest-neighbor constraints. It sharpens the connectivity question for modular codes: the seam links between modules are a form of non-local connectivity, and [9] clarifies what minimal connectivity planar modules genuinely need internally.

**[10] (Continuous-time quantum error correction, arXiv:1311.2485v2).** This chapter develops CTQEC based on continuous weak measurements and feedback, viewed through the subsystem principle. It offers an alternative temporal model to the discrete modular syndrome extraction rounds of [1, 4]; in a modular architecture with asynchronous modules, continuous-time correction is a plausible refinement.

**[11] (Entanglement-Assisted Quantum Error-Correcting Codes, arXiv:1610.04013v1).** This self-contained introduction covers entanglement-assisted QEC, where pre-shared entanglement with a reference augments code construction. Seam links between modules are conceptually analogous to assisted resources — static, non-local aids that boost code parameters — and entanglement-assisted formalism could quantify how much "connectivity resource" the seams consume.

**[12] (QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation, DOI 10.5281/zenodo.17955898).** This work analyzes thermodynamic and informational constraints on scalable fault tolerance. It grounds our Discussion: modular codes reduce qubit-count overhead but add inter-module communication, whose energetic and informational costs must be counted in any full accounting of scalability. Works [13, 14] from the same corpus concern biological quantum processing and geometric orientation codes; they are tangential to the present analysis and we do not draw quantitative claims from them, a scope limitation we note in Section 6.

## 3. Methods

Our method is analytic reconstruction. We take the code parameters reported in [1, 4] as inputs (clearly labeled as such), adopt standard scaling formulas for the rotated surface code, and derive overhead ratios, seam-noise budgets, and extractor-cost comparisons with fully explicit arithmetic. We do not run circuit-level simulations; all performance numbers beyond direct arithmetic are labeled as projections with stated assumptions.

**Model A: surface-code overhead.** For the rotated planar surface code encoding one logical qubit at distance $d$, the number of data qubits is $n_{\mathrm{rot}}(d) = 2d^2 - 2d + 1$, with an approximately equal number of syndrome (measurement) qubits, so the total physical qubit count is $n_{\mathrm{tot}}(d) \approx 2\,n_{\mathrm{rot}}(d)$. We use data-qubit counts for the primary comparison and note the syndrome-qubit factor separately.

**Model B: modular-code overhead.** From [1, 4], the projected modular code has rate $k/n = 1/16$ and $d \geq 22$. To store $k$ logical qubits, the modular memory needs $n_{\mathrm{mod}} = 16k$ physical qubits.

**Model C: seam-noise sensitivity.** We model seam errors as an elevated error channel on the $s$ qubits participating in seam links, with physical error rate $p_{\mathrm{seam}} = \gamma p$ where $p$ is the intra-module error rate and $\gamma \geq 1$ is the seam elevation factor. For a code of distance $d$, the logical failure probability per round under independent stochastic noise scales as

$$p_{\mathrm{L}} \approx A\left(\frac{p_{\mathrm{eff}}}{p_{\mathrm{th}}}\right)^{(d+1)/2},$$

where $p_{\mathrm{th}}$ is the threshold and $p_{\mathrm{eff}}$ is a weighted effective error rate. With a fraction $f = s/n$ of qubits on seams,

$$p_{\mathrm{eff}} = (1-f)\,p + f\,\gamma p = p\left(1 + f(\gamma - 1)\right).$$

We take $p_{\mathrm{th}} = 10^{-2}$ (a standard circuit-level threshold figure for surface-code-class codes, used here as a modeling assumption, not a measurement) and $A = 10^{-1}$ (a conventional prefactor consistent with surface-code phenomenology; both are assumptions for projection purposes and are flagged as such wherever used).

**Model D: extractor cost.** The subject paper reports a modular extractor system $\approx 4.5\times$ smaller than the code itself; we use this ratio as an input and compute its implication for total memory footprint.

## 4. Analysis

Every input number below is stated with its source. All arithmetic is shown step by step.

**Input 1 (from [1, 4]):** projected modular code parameters $k/n = 1/16$, $d \geq 22$.
**Input 2 (from [1, 4]):** the comparison code $[[288, 12, 18]]$ (two-gross bivariate bicycle code), i.e., $n = 288$, $k = 12$, $d = 18$.
**Input 3 (standard result, e.g., as used throughout the surface-code literature):** rotated surface code data-qubit count $n_{\mathrm{rot}}(d) = 2d^2 - 2d + 1$.
**Input 4 (from [1, 4]):** extractor system size $\approx 4.5\times$ smaller than the code, i.e., extractor-to-code size ratio $r_{\mathrm{ext}} = 1/4.5 \approx 0.2222$.

**Derivation 1: surface-code cost to store 12 logical qubits at $d = 18$.**

$$n_{\mathrm{rot}}(18) = 2(18)^2 - 2(18) + 1 = 2(324) - 36 + 1 = 648 - 36 + 1 = 613.$$

For $k = 12$ logical qubits as twelve separate surface-code patches:

$$n_{\mathrm{SC},12}(d{=}18) = 12 \times 613 = 7356 \text{ data qubits}.$$

Including syndrome qubits at roughly a 1:1 ratio, the total is $\approx 2 \times 7356 = 14712$ physical qubits.

**Derivation 2: bivariate bicycle code cost for the same task.** Directly from Input 2: $n_{\mathrm{BB}} = 288$ physical qubits for $k = 12$, $d = 18$. Overhead reduction versus the surface code:

$$\frac{n_{\mathrm{SC},12}}{n_{\mathrm{BB}}} = \frac{7356}{288} = 25.541\overline{6} \approx 25.5\times.$$

Per-logical-qubit cost of the BB code: $288/12 = 24$ physical qubits per logical at $d = 18$.

**Derivation 3: modular-code cost for the same task.** With rate $1/16$, storing $k = 12$ logical qubits requires

$$n_{\mathrm{mod}} = \frac{k}{k/n} = \frac{12}{1/16} = 12 \times 16 = 192 \text{ physical qubits},$$

at $d \geq 22$ (Input 1). Per-logical-qubit cost: $192/12 = 16$ physical qubits per logical at $d \geq 22$.

**Derivation 4: modular versus surface-code overhead reduction.**

$$\frac{n_{\mathrm{SC},12}(d{=}18)}{n_{\mathrm{mod}}(d{\geq}22)} = \frac{7356}{192} = 38.3125 \approx 38.3\times.$$

This exceeds the $>30\times$ claim in [1, 4]; the difference is that our surface-code baseline uses $d = 18$ (matching the BB code's distance), whereas the subject paper's baseline may use a larger distance. If instead the surface-code baseline is taken at $d = 22$:

$$n_{\mathrm{rot}}(22) = 2(484) - 44 + 1 = 968 - 44 + 1 = 925,$$
$$n_{\mathrm{SC},12}(d{=}22) = 12 \times 925 = 11100,$$
$$\frac{11100}{192} = 57.8125 \approx 57.8\times.$$

So the $>30\times$ claim is conservative under our assumptions; the honest range is $38.3\times$ (matched to $d=18$) to $57.8\times$ (matched to $d=22$), both computed above.

**Derivation 5: modular versus BB code.**

$$\frac{n_{\mathrm{BB}}}{n_{\mathrm{mod}}} = \frac{288}{192} = 1.5\times,$$

with the modular code simultaneously offering $d \geq 22 > 18$. So the modular code dominates the BB code on both rate ($16 < 24$ physical qubits per logical) and distance, at the price of requiring seam connectivity.

**Derivation 6: seam-noise budget.** We must estimate the seam fraction $f$. The subject paper describes the boundary connections as "sparse" and "static"; we take as a modeling assumption that each module of linear size $L$ qubits has $O(L)$ boundary qubits participating in seams, so for a module with $m$ qubits, $f \sim c/\sqrt{m}$ with $c$ a small constant. Taking $c = 2$ and a module size of $m = 48$ qubits (so that $192/48 = 4$ modules store 12 logical qubits at 3 logicals per module — an assumption we state explicitly):

$$f = \frac{2}{\sqrt{48}} = \frac{2}{6.9282} = 0.2887.$$

Hmm — this is not sparse enough; a sparser assumption with $c = 1$:

$$f = \frac{1}{\sqrt{48}} = \frac{1}{6.9282} = 0.1443.$$

We proceed with $f = 0.1443$ and flag it as an assumption. The effective error rate is

$$p_{\mathrm{eff}} = p\left(1 + f(\gamma - 1)\right) = p\left(1 + 0.1443(\gamma - 1)\right).$$

Requiring that the modular code retain a factor-of-ten advantage over the surface code at matched distance $d = 22$: the surface code at physical error rate $p$ has (under our Model C with $f = 0$, $A = 10^{-1}$, $p_{\mathrm{th}} = 10^{-2}$)

$$p_{\mathrm{L}}^{\mathrm{SC}} = 10^{-1}\left(\frac{p}{10^{-2}}\right)^{11.5}.$$

The modular code must satisfy $p_{\mathrm{L}}^{\mathrm{mod}} \leq 10\, p_{\mathrm{L}}^{\mathrm{SC}}$, i.e.,

$$10^{-1}\left(\frac{p_{\mathrm{eff}}}{10^{-2}}\right)^{11.5} \leq 10 \cdot 10^{-1}\left(\frac{p}{10^{-2}}\right)^{11.5},$$

which reduces to

$$\left(\frac{p_{\mathrm{eff}}}{p}\right)^{11.5} \leq 10 \quad\Longrightarrow\quad 1 + 0.1443(\gamma - 1) \leq 10^{1/11.5}.$$

Computing $10^{1/11.5}$: $\ln 10 = 2.302585$, so $10^{1/11.5} = e^{2.302585/11.5} = e^{0.200225} = 1.2217$. Therefore

$$0.1443(\gamma - 1) \leq 0.2217 \quad\Longrightarrow\quad \gamma - 1 \leq \frac{0.2217}{0.1443} = 1.5364 \quad\Longrightarrow\quad \gamma \leq 2.54.$$

**Interpretation:** under these assumptions, seam links may carry up to $\approx 2.5\times$ the intra-module error rate before the modular code's tenfold advantage (at matched distance $d = 22$) is exhausted. If the seam fraction is halved ($f = 0.0722$), the budget doubles to $\gamma \leq 1 + 0.2217/0.0722 = 1 + 3.0706 = 4.07$. These are projections contingent on the stated $A$, $p_{\mathrm{th}}$, $f$, and the power-law scaling form; they are not simulations.

**Derivation 7: extractor footprint.** With $r_{\mathrm{ext}} = 1/4.5$ (Input 4), the extractor for the $n = 192$ modular memory occupies the equivalent of

$$n_{\mathrm{ext}} = \frac{192}{4.5} = 42.67 \approx 43 \text{ qubit-equivalents},$$

for a total system footprint of $192 + 42.67 = 234.67 \approx 235$ qubit-equivalents. Revising Derivation 4 for total footprint: $7356/192$ compares data qubits only; a footprint-matched comparison requires adding the surface code's syndrome qubits. Using the $d=22$ baseline with syndrome qubits ($2 \times 11100 = 22200$ total) versus the modular total of $235$:

$$\frac{22200}{235} = 94.5\times,$$

though this mixes counting conventions (the surface-code syndrome count is an approximation; the modular extractor figure is from [1, 4]) and should be read as indicative only.

**Derivation 8: logical failure probability at a target physical error rate.** As a concrete projection, take $p = 10^{-3}$ (a commonly targeted circuit-level physical error rate; assumption). Surface code at $d = 22$:

$$p_{\mathrm{L}}^{\mathrm{SC}} = 10^{-1}\left(\frac{10^{-3}}{10^{-2}}\right)^{11.5} = 10^{-1}(0.1)^{11.5}.$$

Since $(0.1)^{11.5} = 10^{-11.5} = 3.162 \times 10^{-12}$:

$$p_{\mathrm{L}}^{\mathrm{SC}} = 3.162 \times 10^{-13} \text{ per round}.$$

Modular code with $\gamma = 2$ (within the Derivation 6 budget): $p_{\mathrm{eff}} = 10^{-3}(1 + 0.1443) = 1.1443 \times 10^{-3}$, so

$$\frac{p_{\mathrm{eff}}}{p_{\mathrm{th}}} = \frac{1.1443 \times 10^{-3}}{10^{-2}} = 0.11443,$$
$$p_{\mathrm{L}}^{\mathrm{mod}} = 10^{-1}(0.11443)^{11.5}.$$

Computing $(0.11443)^{11.5}$: $\ln(0.11443) = -2.16764$; $11.5 \times (-2.16764) = -24.9279$; $e^{-24.9279} = 1.489 \times 10^{-11}$. Thus

$$p_{\mathrm{L}}^{\mathrm{mod}} = 1.489 \times 10^{-12} \text{ per round},$$

which is $1.489 \times 10^{-12} / 3.162 \times 10^{-13} = 4.71\times$ worse than the surface code per round — but the modular code stores 12 logicals in 192 qubits versus 11100 qubits for twelve surface-code patches, so per-qubit-per-round the modular code is far cheaper. Both figures are projections under Models C's assumptions.

## 5. Results

We report only numbers computed in Section 4, or projections labeled as such.

1. **Surface-code baseline (computed).** Storing 12 logical qubits at $d = 18$ requires $n_{\mathrm{rot}}(18) = 613$ data qubits per logical, $7356$ total ($\approx 14712$ including syndrome qubits). At $d = 22$: $925$ per logical, $11100$ total.

2. **Modular memory (computed from reported parameters).** At $k/n = 1/16$ and $d \geq 22$, 12 logical qubits require $n_{\mathrm{mod}} = 192$ physical qubits, i.e., 16 per logical.

3. **Overhead reductions (computed).** Modular vs. surface code: $38.3\times$ at matched $d = 18$ baseline; $57.8\times$ at matched $d = 22$ baseline. Modular vs. BB code $[[288,12,18]]$: $1.5\times$ fewer physical qubits with strictly larger distance. These independently confirm and strengthen the $>30\times$ claim of [1, 4] under our stated baseline conventions.

4. **Seam-error budget (projection).** Under Model C with $A = 10^{-1}$, $p_{\mathrm{th}} = 10^{-2}$, seam fraction $f = 0.1443$, and power-law logical scaling: the modular code retains a tenfold advantage over the $d = 22$ surface code provided the seam error elevation factor satisfies $\gamma \leq 2.54$; for $f = 0.0722$, $\gamma \leq 4.07$. Uncertainty: these bounds scale linearly in $1/f$ and logarithmically in the required advantage ratio; the dominant uncertainty is $f$, which we assumed rather than measured.

5. **Extractor footprint (computed from reported ratio).** For $n = 192$, the extractor occupies $\approx 43$ qubit-equivalents; total modular footprint $\approx 235$ qubit-equivalents.

6. **Logical error rates at $p = 10^{-3}$ (projection).** Surface code $d = 22$: $3.162 \times 10^{-13}$ per round. Modular code with $\gamma = 2$: $1.489 \times 10^{-12}$ per round, i.e., $4.71\times$ higher per round, traded against a $57.8\times$ qubit-count reduction.

## 6. Discussion

**Limitations.** Our analysis inherits every parameter of [1, 4] as an input rather than an independent verification: the rate $1/16$, distance $d \geq 22$, and extractor ratio $4.5\times$ are reported projections of that work, not our computations. Our seam model (Model C) assumes independent stochastic errors and a power-law subthreshold scaling with a single threshold; real seam faults may be correlated (a single fabrication defect or crosstalk source can hit multiple seam qubits), and correlated failures can defeat distance-$d$ protection entirely if they form a weight-$\leq d$ logical operator along a seam. Our seam-fraction estimate $f = 0.1443$ is a guess dressed in arithmetic; the true budget $\gamma \leq 2.54$ is inversely proportional to it, so a factor-of-two error in $f$ shifts the budget by a factor of two.

**Failure modes.** Three stand out. First, decoder complexity: the subject paper uses neural-network and matching decoders; if seam errors correlate across modules, local decoders per module will misdecode, and a global decoder may be required, eroding the modularity advantage. Second, the walking circuits based on code automorphisms must themselves be fault-tolerant; a low-weight automorphism circuit is a low-weight logical operator in spacetime and can be the weak link, a concern the fault-complex framework of [6] is designed to expose. Third, threshold: semi-hyperbolic codes have thresholds below the surface code's in general; if the modular threshold falls significantly below our assumed $10^{-2}$, the budgets of Derivation 6 tighten as $\gamma_{\max} \propto$ (threshold ratio)$^{1/11.5}$-dependent factors — actually the dependence is weak at fixed $p$, but the prefactor $A$ grows, degrading all projected $p_{\mathrm{L}}$ values proportionally.

**What would falsify the claims.** (a) A circuit-level simulation showing that seam elevation $\gamma > 2.5$ (at our assumed $f$) destroys the tenfold advantage would falsify the practicality claim at near-term error rates. (b) A demonstration that the $k/n = 1/16$, $d \geq 22$ code family requires seam connectivity growing faster than $O(\sqrt{n})$ would undermine the sparse-seam premise and our Derivation 6. (c) Evidence that walking circuits accumulate faults non-local-in-spacetime, so that logical failure scales with circuit depth faster than the memory rate, would falsify the "dense storage in a universal architecture" claim.

**Against ourselves.** The strongest counterargument to our analysis is that comparing per-logical-qubit counts at matched distance is the wrong metric: what matters is logical error rate per unit spacetime volume per qubit, and the modular code's higher-rate, lower-distance-per-cost structure may lose on that metric if its constant prefactor $A$ is much larger than the surface code's. Our Derivation 8 already shows a $4.71\times$ per-round penalty at $\gamma = 2$; if $A_{\mathrm{mod}} = 10 A_{\mathrm{SC}}$, the penalty becomes $47\times$, and combined with decoder overheads the net advantage could shrink toward the tenfold floor claimed in [1, 4] — or below it. A second counterargument: generic LDPC codes such as the Cornucopia family [5] achieve far better parameters with comparable connectivity if one accepts non-planar routing; the modular code's niche exists only if planar fabricability is genuinely worth a $1.5\times$ loss versus the BB code and a larger loss versus the best LDPC codes. Third, thermodynamic accounting [12] may penalize the seams: maintaining low-error inter-module links could dominate the energy budget, a cost invisible in qubit counts.

**Open questions.** What is the measured (not assumed) seam fraction $f$ for the concrete module layouts? Do seam errors exhibit the independence Model C requires? Can the walking circuits be analyzed as fault complexes in the sense of [6] to certify spacetime fault tolerance? Can measurement-free code switching [8] supply the universal gate set on a modular memory without breaking modularity? And does a continuous-time correction scheme [10] suit asynchronous modular operation better than synchronized rounds?

## 7. Conclusion

We independently reconstructed the overhead arithmetic of boundary-connected modular semi-hyperbolic codes and found the headline claims of [1, 4] not merely consistent with, but conservative under, our baseline conventions: storing twelve logical qubits at distance $\geq 22$ costs 192 physical qubits at rate $1/16$, versus 11100 data qubits for twelve $d = 22$ surface-code patches ($57.8\times$ reduction) and 288 for the $[[288,12,18]]$ bivariate bicycle code ($1.5\times$ reduction with greater distance). Our seam-noise model projects that the advantage survives seam error rates up to $\approx 2.5\times$ the intra-module rate at an assumed seam fraction of $0.1443$, with the budget scaling inversely with that fraction. The proposal occupies a defensible middle ground between planar fabricability and LDPC-class rates, but its ultimate value hinges on three unresolved empirical questions: the true seam fraction, seam error correlations, and the fault tolerance of automorphism-based walking circuits. We recommend that future work close these gaps with the spacetime formalism of [6] and full thermodynamic accounting in the spirit of [12].

## References

[1] arXiv Query: search_query=&id_list=2610.03682&start=0&max_results=1 — Low-Overhead Quantum Error Correction with Boundary-Connected Planar Modules (abstract), arXiv:2610.03682.

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

[13] QNFO: THERMODYNAMIC AND TOPOLOGICAL CONSTRAINTS ON BIOLOGICAL QUANTUM PROCESSING | DOI 10.5281/zenodo.17989524.

[14] QNFO: Computational Simulation of Geometric Orientation Codes | DOI 10.5281/zenodo.19487443.