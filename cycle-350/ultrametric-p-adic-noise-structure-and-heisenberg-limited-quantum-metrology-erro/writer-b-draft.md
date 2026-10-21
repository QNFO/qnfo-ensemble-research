# Ultrametric $p$-Adic Noise Structure and Heisenberg-Limited Quantum Metrology: Error Resilience by Geometry, Not Overhead

## Abstract

Quantum metrology promises phase sensitivity scaling as $\Delta\theta \propto N^{-1}$ (the Heisenberg limit), but decoherence destroys the entangled probes on which this scaling depends, and the standard remedy — active quantum error correction — carries overhead that near-term sensing platforms cannot afford. We formalize a conjecture from the ultrametric research program: if decoherence on a qubit register is modeled as a $p$-adic (ultrametric) hierarchical stochastic process, the strong triangle inequality $d(x,z) \leq \max\{d(x,y), d(y,z)\}$ forces error events on nested clusters to be nested rather than independent, so the union probability is the maximum of the level probabilities, not their sum. For a hierarchy of $L$ levels with level-$k$ error weight $\varepsilon_k = \varepsilon_0 p^{-k}$, we derive an ultrametric corruption probability $P_{\mathrm{U}} = \varepsilon_0 p^{-L}$ and compare it with the Archimedean union bound $P_{\mathrm{A}}$. For $p=2$, $L=10$, $\varepsilon_0 = 10^{-2}$, the ultrametric probability is $9.765625 \times 10^{-6}$ against an Archimedean bound of $1.9990234375 \times 10^{-2}$, a ratio of exactly $2047$. Propagating this into the quantum Fisher information of an $N$-probe Greenberger–Horne–Zeilinger probe with $L = \log_2 N$ yields Heisenberg scaling $\Delta\theta \propto N^{-1}$ under the ultrametric model, while independent dephasing collapses Greenberger–Horne–Zeilinger coherence exponentially in $N$. Against the strongest competitor, a time-optimized product-probe sensor, the ultrametric advantage at fixed $N$ can vanish; the claim is a scaling claim. All quantitative results are model-derived projections conditional on one explicitly identified conjectural axiom, and we state the falsifiable criteria under which the claim collapses.

## 1. Introduction

Engineers building quantum sensors — magnetometry, atomic clocks, rotation sensing — face a concrete trade-off today. Entangled probe states such as Greenberger–Horne–Zeilinger (GHZ) states promise phase sensitivity scaling as $\Delta\theta \propto N^{-1}$ in the number of probes $N$ (the Heisenberg limit), a factor of $\sqrt{N}$ better than the standard quantum limit (SQL) $\Delta\theta \propto N^{-1/2}$ reached by independent probes. In practice, decoherence erodes this advantage: a GHZ state under independent per-qubit dephasing loses its phase coherence exponentially in $N$, so beyond a modest probe count the entangled strategy is worse than the product strategy, and the working sensor falls back on the SQL with more averaging time. The standard escape is quantum error correction, whose overhead — on the order of $10^3$ to $10^6$ physical qubits per logical qubit, with continuous syndrome extraction, decoding and feedback at cryogenic temperature — is prohibitive for a sensing platform that must remain small, low-power and cheap [9]. A passive mechanism that protected entangled probes without that overhead would change the design calculus directly: it would decide whether a next-generation sensor invests in error-correction hardware or in a differently structured noise environment.

This paper examines one candidate mechanism, proposed in the ultrametric research program [9], [11]: if the decoherence process itself has an ultrametric — equivalently, $p$-adic — hierarchical structure, then the strong triangle inequality constrains how errors combine, and errors living in nested clusters merge rather than accumulate. The slogan is "error resilience by geometry, not overhead": the geometry of the noise model, not an active correction protocol, supplies the protection. The claim is deliberately conditional. This paper derives what follows if decoherence is ultrametrically nested; it does not claim that physical decoherence has been shown to be ultrametric. That identification is the falsifiable hypothesis, and Section 6 states exactly which measurement would refute it.

The paper proceeds in three steps. First, it formalizes the noise model as a $p$-adic-valued stochastic process on an ultrametric lattice and derives the error-propagation identity directly from the ultrametric inequality (Section 3). Second, it carries out the arithmetic that converts the identity into precision bounds: explicit error probabilities, coherence factors and quantum Fisher information (QFI) values for entangled probes under ultrametric versus Archimedean (independent, dephasing-like) noise, including the strongest time-optimized competitor (Section 4). Third, it extracts the falsifiable prediction — the scaling of $\Delta\theta$ versus $N$ differs qualitatively between the two noise geometries — and states what experimental outcome would collapse the claim (Sections 5 and 6).

The contributions are:

- Derivation of the max-of-levels law $P_{\mathrm{U}} = \varepsilon_0 p^{-L}$ from the nesting of error events implied by the ultrametric inequality, with the exact comparison value $P_{\mathrm{A}}/P_{\mathrm{U}} = 2047$ at $p=2$, $L=10$, $\varepsilon_0 = 10^{-2}$ (Sections 3.3 and 4.1).
- Derivation of Heisenberg scaling $\Delta\theta \propto N^{-1}$ for a GHZ probe under the ultrametric model, with the exact single-shot sensitivity $\Delta\theta_{\mathrm{U}} \approx 9.7657 \times 10^{-4}$ at $N = 1024$, contrasted with the exponential collapse $\Delta\theta_{\mathrm{A}} \approx 9.42 \times 10^{5}$ of the GHZ probe under independent dephasing (Sections 4.2 and 4.3).
- Identification of the honest competitor — the time-optimized product probe with $\Delta\theta^{\mathrm{prod}} \approx 8.4946 \times 10^{-4}$ at $N = 1024$, $\gamma = 10^{-2}$ — showing that the ultrametric advantage is a scaling claim, not a fixed-$N$ claim (Section 4.4).
- A falsifiability protocol: three measurable conditions whose joint satisfaction confirms the model and any one of which refutes it, together with the smallest experiment that would decide the question (Sections 6.2 and 7).

## 2. Background and Related Work

**Ultrametric data analysis.** Reference [1] models anomaly and change in data by embedding the data in an ultrametric space: starting from cross-tabulation counts, Correspondence Analysis endows the information space with a Euclidean metric, and anomaly or change is then modeled by an induced ultrametric, with particular interest in a sequential form of induction. Its conclusions section states the pipeline explicitly: the $\chi^2$ metric is appropriate for frequency-of-occurrence data, points and masses are mapped from the $\chi^2$ distance to a Euclidean space, and on the resulting points a hierarchy associated with an ultrametric can be induced, which is then used to read off changepoints or anomalies at a range of scales. This matters here because it supplies a constructive route from raw experimental records to an ultrametric hypothesis: if a sensor register's error log can be processed the same way, the induced ultrametric becomes an estimated object rather than an assumption (Section 6.3).

**Markov processes on $p$-adic spaces.** Reference [2] proposes a method for describing stationary Markov processes on the class of ultrametric spaces isometrically embeddable in the field $\mathbb{Q}_p$ of $p$-adic numbers, reducing the study of such processes to processes on $\mathbb{Q}_p$ so that the traditional machinery of $p$-adic mathematical physics applies. Its conclusions state the reduction concretely: the Cauchy problem for the Kolmogorov–Feller equation of a stationary Markov process on an ultrametric space reduces to a pseudo-differential equation on $\mathbb{Q}_p$, with all characteristics of the process expressible in terms of the solution. The noise process defined in Section 3 is an object of exactly this class — a stationary hierarchical process on an ultrametric space realized inside $\mathbb{Q}_p$ — so [2] provides the mathematical machinery into which the model slots, and the open questions of Section 6.3 use its framework.

**Noise as a foundational category.** Reference [3] introduces a collection of works on quantum and classical frontiers of noise, using the weather and its butterfly effect as the typical example of why many natural phenomena are not predictable with certainty. Its Section II gives a definition this paper adopts directly: the signal of an experiment is the statistical prediction $\langle A\rangle = \sum_{i=1}^{N} P(a_i) a_i$, and noise is the difference between the measured outcome $a_i$ and that signal. Our claim is a statement about the statistical geometry of that difference, and the falsifiability discussion of Section 6.2 is a proposal for measuring it.

**$p$-adic statistical mechanics.** Reference [4] studies the three-state $p$-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of $p$-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p = 3$ for any nonzero value of the interactions, also solving the uniqueness problem. Its conclusions emphasize that the phase transition depends only on the value of $p$, a result "totally different from the real case." The Cayley tree is the canonical ultrametric hierarchy, and the sharp $p$-dependence of its phase structure is both a warning and an opportunity for this paper: predictions of an ultrametric model can depend discontinuously on the prime $p$, which is itself a falsifiable signature (Section 6.2, criterion (iii)).

**$p$-adic quantum mechanics.** Reference [5] describes $p$-adic mathematical physics as arising from efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, with $p$-adic and adelic quantum mechanics — complex-valued wave functions of $p$-adic and adelic arguments — as a main achievement. Its Section 3 distinguishes two approaches to quantum mechanics on $\mathbb{Q}_p^D$, with $p$-adic-valued and with complex-valued wave functions, and notes that the complex-valued approach is more suitable for connection with ordinary quantum mechanics. Our model follows that choice: the noise amplitudes live in $p$-adic value space while the probe states remain ordinary complex quantum states, so the QFI formalism of Section 3.4 applies unchanged.

**Ultrametric models of natural structure.** Reference [6] uses basic properties of $p$-adic numbers to describe DNA sequence and the genetic code, with a central ultrametric $p$-adic information space whose basic elements are nucleotides, codons and genes. Its concluding remarks state the empirical outcome: a 5-adic model is attached to the sequence of codons, and using 5-adic and 2-adic distances between codons yields their classification into quadruplets and doublets respectively, giving the principle that $p$-adically close codons correspond to the same amino acid. This is the clearest precedent that hierarchical biological information can be usefully encoded ultrametrically with an empirically identifiable prime; our hypothesis transfers the same move to decoherence statistics, and the precedent warns that the effective prime is an empirical quantity, not a free aesthetic choice (Section 6.1).

**Ultrametric functional analysis.** Reference [7] treats ultrametrics as a zero-dimensional analogue of ordinary metrics and proves ultrametric versions of the Arens–Eells isometric embedding theorem of metric spaces, the Hausdorff extension theorem of metrics, and the Niemytzki–Tychonoff characterization theorem. Its Section 4 develops the extension theorem by adapting Toruńczyk's and Hausdorff's methods to ultra-normed modules over commutative rings. For this paper the point is that the ultrametric lattice postulated in Section 3 is not a fragile special case: ultrametric structures admit embedding, extension and interpolation theories parallel to the Archimedean ones, so the model can be refined — for example by extending the noise process off a finite lattice — without leaving the category.

**Hierarchic quantum systems.** Reference [8] considers the $p$-adic wavelet transform as a possible tool for the description of hierarchic quantum systems. Its introduction motivates the wavelet transform by its mutual locality in coordinate and momentum — a local disturbance of wavelet coefficients affects the reconstructed signal only locally — and its conclusion points to multiscale methods based on the $p$-adic generalization of the wavelet transform and to quantum systems with $p > 2$ orthogonal states. A $p$-adic wavelet basis is therefore a natural candidate representation for a register whose error structure is hierarchical, and the level decomposition used in Section 3 is the one such a basis implies.

**Program documents.** Reference [9] is the originating proposal for $p$-adic quantum metrology under the title "Passive Error Resilience Through Ultrametric Geometry." Its argument runs through thermodynamics: each round of active error correction requires syndrome measurement, decoding and feedback, each of which erases information, and by Landauer's principle erasing one bit at temperature $T$ dissipates at least $kT\ln 2$ of energy; the proposal reports that no peer-reviewed system-level thermodynamic budget for utility-scale fault-tolerant quantum computation has been found in the literature, and its Section 2.3 argues that quantum metrology escapes this wall because a sensor needs to maintain entanglement across a small number of probes for a single measurement cycle rather than coherence across millions of qubits for thousands of gate operations. This supplies the motivation for seeking passive rather than active protection, which is exactly the role the ultrametric noise structure plays in Section 3. Reference [11] states the program-level claim that seven research domains are seven vocabularies for one structural object — nested hierarchical partition logic defined by the ultrametric inequality $d(x,z) \leq \max(d(x,y), d(y,z))$, with $p$-adic/adelic arithmetic as one realization and the hierarchy as the invariant — and lists three falsifiable hypotheses, of which H3 is a structured-noise decoherence measurement showing the $p$-adic scaling signature. The present paper is a deepening of the H3-type test for the metrology domain: it derives what the scaling signature must be if the structural claim holds for a sensing register.

## 3. Methods

### 3.1 Ultrametric lattice and hierarchy levels

Let the register consist of $N$ qubits organized into a binary (more generally $p$-ary) hierarchy of depth $L$, so that $N = p^L$ in the balanced case. The hierarchy is an ultrametric space $(X, d)$: for any three points $x, y, z \in X$,

$$d(x,z) \leq \max\{d(x,y), d(y,z)\},$$

which implies that any two balls are either nested or disjoint. Level $k \in \{0, 1, \dots, L\}$ consists of the clusters of diameter $p^{-k}$ in the standard $p$-adic normalization; level $0$ is the whole register, level $L$ the individual qubits. This is the same nested-partition structure that [11] identifies as the program's invariant object and that [4] realizes on the Cayley tree.

### 3.2 Noise as a $p$-adic-valued stochastic process

Following the reduction logic of [2], we define the noise process on $\mathbb{Q}_p$ itself. To each cluster $C$ at level $k$ we attach a nonnegative error weight

$$\varepsilon_k(C) = \varepsilon_0\, p^{-k}, \qquad k = 0, 1, \dots, L,$$

where $\varepsilon_0 \in (0,1)$ is a dimensionless base rate. The $p$-adic valuation structure is essential: the weight of a cluster decays by the factor $p^{-1}$ per level of refinement, mirroring the norm of $p^k$ in $\mathbb{Q}_p$ as defined, for example, in [4] and [6]. A decoherence event is a pair $(k, C)$: an error of weight $\varepsilon_k(C)$ localized on cluster $C$. The physical interpretation is that errors are correlated within clusters and the correlation is hierarchical — an error at a coarse level touches many qubits coherently, an error at a fine level touches few.

### 3.3 Error propagation from the ultrametric inequality

Let $E$ be the event "the register's phase estimate is corrupted in the sensing window." Because balls in an ultrametric space are nested or disjoint, the error events $\{E_k\}_{k=0}^{L}$ attached to the levels form a nested family after the standard coalescence argument: within one level the clusters are disjoint, and across levels the dominating (coarsest, largest-weight) event contains its descendants. The union probability is therefore

$$P_{\mathrm{U}} = \Pr\Big(\bigcup_{k=0}^{L} E_k\Big) = \max_{0 \leq k \leq L} \Pr(E_k) = \varepsilon_0\, p^{-L},$$

since $\varepsilon_k = \varepsilon_0 p^{-k}$ is maximized at $k = L$. This is the precise sense of "errors cancel across nested clusters": the coarse, high-weight events are refinements of one another, not independent additions, so only the finest-scale weight survives as the effective corruption probability of a single logical sensing operation.

By contrast, under an Archimedean (independent-event) model the same level weights give the union bound

$$P_{\mathrm{A}} \leq \sum_{k=0}^{L} \varepsilon_0 p^{-k} = \varepsilon_0\, \frac{1 - p^{-(L+1)}}{1 - p^{-1}},$$

and with independent levels this bound is tight up to intersection corrections, which only lower $P_{\mathrm{A}}$; we use the sum as the Archimedean comparison value throughout. Section 6.1 discusses the effect of this convention on the strength of the claim.

### 3.4 Probe states and quantum Fisher information

The probe is an $N$-qubit GHZ state,

$$|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\big(|0\rangle^{\otimes N} + |1\rangle^{\otimes N}\big),$$

accumulating phase $\theta$ with noiseless QFI $F_Q = N^2$. Decoherence that destroys the phase coherence between the two branches with probability $P$ replaces the off-diagonal density-matrix element $\rho_{01}$ by $(1 - P)\,\rho_{01}$; the QFI of the resulting state is

$$F_Q(P) = N^2 (1 - P)^2.$$

The single-shot phase sensitivity is $\Delta\theta = 1/\sqrt{F_Q}$, and with $\nu$ independent repetitions, $\Delta\theta_\nu = 1/\sqrt{\nu F_Q}$. Because the probe state and the measurement are ordinary complex quantum objects, this step is standard quantum metrology; the $p$-adic structure enters only through the value of $P$, in the tradition of complex-valued wave functions on $p$-adic argument spaces [5].

### 3.5 Archimedean competitor: independent per-qubit dephasing

The standard Archimedean competitor models each qubit as dephasing independently with per-qubit coherence survival factor $c_0 = 1 - 2\varepsilon_0$ over the sensing window (the factor $2$ reflects that a depolarizing-type event with probability $\varepsilon_0$ damps the coherence by $1 - 2\varepsilon_0$). For the GHZ state the two branches accumulate $N$ independent dephasing events, so

$$\eta_{\mathrm{A}} = c_0^{\,N} = (1 - 2\varepsilon_0)^N, \qquad F_Q^{\mathrm{A}} = N^2 (1 - 2\varepsilon_0)^{2N}.$$

For product-state probes under the same independent dephasing at rate $\gamma$ per unit time, the single-probe QFI for a sensing time $t$ is $f(t) = t^2 e^{-2\gamma t}$; maximizing over $t$ yields the SQL scaling derived explicitly in Section 4.4.

### 3.6 Status of the axioms

The derivation chain has exactly one conjectural step: the identification of physical decoherence with the nested-event structure of Section 3.3 (equivalently, the weight law $\varepsilon_k = \varepsilon_0 p^{-k}$ and the nesting of the $E_k$). Everything downstream — the max-versus-sum contrast, the QFI propagation, the scaling statements — is exact arithmetic given that step. This is the H3-type hypothesis of [11] specialized to a sensing register, and Section 6.2 states its disconfirmation criteria.

## 4. Analysis

All numbers in this section are computed from the inputs stated here. Inputs: prime $p = 2$; hierarchy depth $L = 10$; base error weight $\varepsilon_0 = 10^{-2}$; register size $N = p^L = 2^{10} = 1024$ qubits; single shot ($\nu = 1$) unless stated; dephasing rate $\gamma = 10^{-2}$ per unit time for the time-optimized comparison of Section 4.4. All model inputs are free parameters of the proposed test, not measurements.

### 4.1 Ultrametric versus Archimedean error probability

**Ultrametric.** From Section 3.3,

$$P_{\mathrm{U}} = \varepsilon_0\, p^{-L} = 10^{-2} \times 2^{-10} = 10^{-2} \times 9.765625 \times 10^{-4} = 9.765625 \times 10^{-6}.$$

**Archimedean union bound.**

$$P_{\mathrm{A}} = \varepsilon_0\, \frac{1 - 2^{-(L+1)}}{1 - 2^{-1}} = 10^{-2} \times \frac{1 - 2^{-11}}{0.5}.$$

Compute the numerator: $1 - 2^{-11} = 1 - 4.8828125 \times 10^{-4} = 0.99951171875$. Divide by $0.5$: $0.99951171875 / 0.5 = 1.9990234375$. Multiply by $\varepsilon_0$:

$$P_{\mathrm{A}} = 10^{-2} \times 1.9990234375 = 1.9990234375 \times 10^{-2}.$$

**Ratio.** Since $P_{\mathrm{U}} = \varepsilon_0 2^{-10} = 10^{-2}/1024$,

$$\frac{P_{\mathrm{A}}}{P_{\mathrm{U}}} = \frac{10^{-2} \times 1.9990234375}{10^{-2}/1024} = 1.9990234375 \times 1024.$$

Compute exactly: $1.9990234375 = 2 - 9.765625 \times 10^{-4} = 2 - 1/1024$. Then

$$1024 \times \left(2 - \frac{1}{1024}\right) = 2048 - 1 = 2047.$$

Therefore

$$\frac{P_{\mathrm{A}}}{P_{\mathrm{U}}} = 2047 \text{ exactly.}$$

### 4.2 QFI and sensitivity at $N = 1024$

**Ultrametric coherence.** With $L = \log_2 N = 10$,

$$\eta_{\mathrm{U}} = 1 - P_{\mathrm{U}} = 1 - 9.765625 \times 10^{-6} = 0.999990234375.$$

Then $\eta_{\mathrm{U}}^2 = (1 - 9.765625 \times 10^{-6})^2 = 1 - 1.953125 \times 10^{-5} + 9.5367 \times 10^{-11} \approx 0.99998046876$, and

$$F_Q^{\mathrm{U}} = N^2 \eta_{\mathrm{U}}^2 = 1048576 \times 0.99998046876 \approx 1.048556 \times 10^{6}.$$

$$\Delta\theta_{\mathrm{U}} = \frac{1}{\sqrt{F_Q^{\mathrm{U}}}} = \frac{1}{N\,\eta_{\mathrm{U}}} = \frac{1}{1024 \times 0.999990234375} = \frac{1}{1023.99} \approx 9.766 \times 10^{-4}.$$

**Archimedean GHZ coherence.**

$$\eta_{\mathrm{A}} = (1 - 2\varepsilon_0)^N = 0.98^{1024}.$$

Compute via the exponential: $\ln 0.98 = -0.0202027073$; $1024 \times (-0.0202027073) = -20.6875723$. Then, using $e^{-20} = 2.06115 \times 10^{-9}$ and $e^{-0.6875723} = 0.50279$,

$$\eta_{\mathrm{A}} = e^{-20.6875723} \approx 1.0364 \times 10^{-9}.$$

$$F_Q^{\mathrm{A}} = N^2 \eta_{\mathrm{A}}^2 = 1048576 \times (1.0364 \times 10^{-9})^2 = 1048576 \times 1.0741 \times 10^{-18} \approx 1.126 \times 10^{-12}.$$

$$\Delta\theta_{\mathrm{A}} = \frac{1}{\sqrt{F_Q^{\mathrm{A}}}} = \frac{1}{\sqrt{1.126 \times 10^{-12}}} = \frac{1}{1.0611 \times 10^{-6}} \approx 9.42 \times 10^{5}.$$

**Ratio of sensitivities (single shot, GHZ probes).**
The inputs are the Archimedean GHZ sensitivity $\Delta\theta_{\mathrm{A}}$ computed above as $1/(N\,\eta_{\mathrm{A}})$ with $\eta_{\mathrm{A}} = 0.98^{1024} \approx 1.0364 \times 10^{-9}$, and the ultrametric GHZ sensitivity $\Delta\theta_{\mathrm{U}} = 1/(N\,\eta_{\mathrm{U}})$ with $\eta_{\mathrm{U}} = 1 - P_{\mathrm{U}} = 1 - 9.765625 \times 10^{-6} \approx 0.999990234375$. Thus

$$\frac{\Delta\theta_{\mathrm{A}}}{\Delta\theta_{\mathrm{U}}}
= \frac{1/(N\,\eta_{\mathrm{A}})}{1/(N\,\eta_{\mathrm{U}})}
= \frac{\eta_{\mathrm{U}}}{\eta_{\mathrm{A}}}
\approx \frac{0.999990234375}{1.0364 \times 10^{-9}}
\approx 9.65 \times 10^{8}.$$

This ratio is a within-model statement: it reflects the exponential collapse $c_0^N$ of GHZ coherence under independent noise versus the $N$-independent survival $\eta_{\mathrm{U}}$ under the ultrametric model. It should not be read as an experimental prediction (Section 6.1).

### 4.3 Scaling with $N$: the qualitative claim

Under the ultrametric model with $L = \log_2 N$, the corruption probability is $P_{\mathrm{U}} = \varepsilon_0 / N$, so $\eta_{\mathrm{U}} = 1 - \varepsilon_0/N$ and

$$\Delta\theta_{\mathrm{U}} = \frac{1}{N(1 - \varepsilon_0/N)} = \frac{1}{N - \varepsilon_0},$$

which is Heisenberg scaling $\Delta\theta \propto N^{-1}$ up to an $O(1)$ correction. Under independent dephasing, GHZ coherence decays as $(1-2\varepsilon_0)^N$, i.e., exponentially in $N$, so the GHZ advantage is destroyed; the best Archimedean strategy reverts to product probes and SQL scaling, as computed next.

### 4.4 Optimized sensing under independent dephasing: the honest Archimedean competitor

The comparison in Section 4.2 uses a fixed sensing window. The strongest Archimedean competitor optimizes the sensing time $t$. With signal $\theta = \omega t$ and independent dephasing at rate $\gamma$ per unit time:

**Product probes.** Single-probe QFI: $f(t) = t^2 e^{-2\gamma t}$. Setting the derivative $f'(t) = e^{-2\gamma t}(2t - 2\gamma t^2) = 0$ gives $t^* = 1/\gamma$. Then

$$f(t^*) = \frac{e^{-2}}{\gamma^2}, \qquad F_Q^{\mathrm{prod}} = \frac{N e^{-2}}{\gamma^2}, \qquad \Delta\theta^{\mathrm{prod}} = \frac{e\,\gamma}{\sqrt{N}}.$$

With the stated assumption $\gamma = 10^{-2}$ and $N = 1024$ we obtain

$$\Delta\theta^{\mathrm{prod}}=\frac{2.718281828 \times 10^{-2}}{32}=8.4946 \times 10^{-4}.$$

This is the number any ultrametric claim must beat: the honest comparison at $N = 1024$ is $\Delta\theta_{\mathrm{U}} \approx 9.7657 \times 10^{-4}$ versus $\Delta\theta^{\mathrm{prod}} \approx 8.4946 \times 10^{-4}$ — the optimized product probe is, within this parameter choice, slightly better in absolute single-shot sensitivity, and the ultrametric advantage must instead be sought in the scaling exponent as $N$ grows (Section 4.3) rather than in a fixed-point comparison.

### 4.5 Complementary comparison at a small register (secondary parameter set)

A second parameter set, retained for completeness, uses $N = 16$, $\gamma = 0.01$, $p = 2$, $L = 4$, with the same suppression law $\Gamma_L = \gamma p^{-L}$. Its arithmetic, labeled as a projection under the same conjectural axiom, is:

$$p^{-L} = 2^{-4} = 0.0625, \qquad \Gamma_4 = 0.01 \times 0.0625 = 6.25 \times 10^{-4}.$$

Maximizing $F_Q(t) = N^2 t^2 e^{-2\Gamma t}$ gives $t^* = 1/\Gamma$ and per-run sensitivity $\delta\varphi_{\min} = e\Gamma/N$. Per-run improvement factor:

$$\frac{\delta\varphi_{\min}^{(0)}}{\delta\varphi_{\min}^{(4)}} = \frac{\Gamma_0}{\Gamma_4} = \frac{0.01}{6.25 \times 10^{-4}} = 16 = p^{L}.$$

At fixed total averaging time $T$, the number of runs scales as $1/t^*$, giving a fixed-time improvement factor of $\sqrt{p^{L}} = p^{L/2} = 4$. These are the per-run and fixed-time versions of the same suppression law computed in Section 4.1.

## 5. Results

All results below are model-derived projections computed in Section 4, conditional on the conjectural nesting axiom of Section 3.6, for the primary inputs $p = 2$, $L = 10$, $\varepsilon_0 = 10^{-2}$, $N = 1024$.

**R1 (exact within the model).** Ultrametric corruption probability $P_{\mathrm{U}} = 9.765625 \times 10^{-6}$; Archimedean union bound $P_{\mathrm{A}} = 1.9990234375 \times 10^{-2}$; ratio $P_{\mathrm{A}}/P_{\mathrm{U}} = 2047$ exactly.

**R2 (exact within the model).** Ultrametric single-shot GHZ sensitivity $\Delta\theta_{\mathrm{U}} \approx 9.7657 \times 10^{-4}$; Archimedean GHZ sensitivity $\Delta\theta_{\mathrm{A}} \approx 9.42 \times 10^{5}$; ratio $\approx 9.65 \times 10^{8}$.

**R3 (exact within the model).** Scaling: from $\eta_{\mathrm{U}} = 1 - \varepsilon_{0}p^{-L}=1-\varepsilon_{0}/N$, the ultrametric GHZ sensitivity is

$$\Delta\theta_{\mathrm{U}}=\frac{1}{N\,\eta_{\mathrm{U}}}=\frac{1}{N\,(1-\varepsilon_{0}/N)}=\frac{1}{N-\varepsilon_{0}}\,