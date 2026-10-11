# Ultrametric $p$-Adic Noise Structure and Heisenberg-Limited Quantum Metrology: Error Resilience by Geometry, Not Overhead

## Abstract

We formalize a conjecture that models decoherence on a qubit register as a $p$-adic (ultrametric) hierarchical stochastic process, and we derive its consequences for quantum metrology. The central structural input is the strong triangle inequality $d(x,z) \leq \max\{d(x,y), d(y,z)\}$, which forces the family of error events on nested clusters to be nested rather than independent; the probability of the union is then the maximum of the level probabilities, not their sum. For a hierarchy of $L$ levels with level-$k$ error weight $\varepsilon_k = \varepsilon_0 p^{-k}$, we derive an ultrametric error probability $P_{\mathrm{U}} = \varepsilon_0 p^{-L}$ and compare it with the Archimedean (independent-event) union bound. For $p=2$, $L=10$, $\varepsilon_0 = 10^{-2}$, the ultrametric probability is $9.77\times 10^{-6}\,\varepsilon_0$-scaled versus an Archimedean bound of $1.999\,\varepsilon_0$, a ratio of $2046$. Propagating this into the quantum Fisher information of an $N$-probe GHZ probe, with $L = \log_2 N$, yields Heisenberg scaling $\Delta\theta \propto N^{-1}$ under the ultrametric model, while independent dephasing yields at best shot-noise scaling $\Delta\theta \propto N^{-1/2}$ for optimized product probes and no $N$-scaling for GHZ probes. We state the falsifiable scaling prediction explicitly and discuss the assumptions on which the claim stands or falls.

## 1. Introduction

Quantum metrology promises phase sensitivity that beats the standard quantum limit (SQL), $\Delta\theta \propto N^{-1/2}$ for $N$ probes, up to the Heisenberg limit $\Delta\theta \propto N^{-1}$. In practice, decoherence erodes this advantage: entangled probes are fragile, and the usual remedy is quantum error correction, whose overhead is prohibitive on near-term devices. The research idea examined here proposes a different route: if the decoherence process itself has an ultrametric — equivalently, $p$-adic — hierarchical structure, then the strong triangle inequality forces errors to cancel across nested clusters, and the register becomes passively resilient. The slogan is "error resilience by geometry, not overhead": the geometry of the noise model, not an active correction protocol, supplies the protection.

This paper does three things. First, it formalizes the noise model as a $p$-adic-valued stochastic process on an ultrametric lattice and derives error-propagation identities directly from the ultrametric inequality (Section 3). Second, it carries out the arithmetic that converts those identities into precision bounds: explicit error probabilities, coherence factors, and quantum Fisher information (QFI) values for entangled probes under ultrametric versus Archimedean (depolarizing-like, independent) noise (Section 4). Third, it extracts a falsifiable prediction — the scaling exponent of $\Delta\theta$ versus $N$ differs qualitatively between the two noise geometries — and states what experimental outcome would collapse the paradigm (Sections 5 and 6).

We emphasize at the outset what this paper does and does not claim. It claims a theorem-level consequence of an assumed noise structure: *if* decoherence on the register is ultrametrically nested in the sense defined below, *then* Heisenberg-limited sensitivity follows without error-correction overhead. It does not claim that physical decoherence has been shown to be ultrametric; that is precisely the falsifiable hypothesis, and Section 6 discusses how it could fail. The framing of near-term quantum advantage as sensing rather than computation, and the programmatic context of ultrametric structure as one invariant across research domains, follow the proposal and program documents cited as [9], [10], and [12].

## 2. Background and Related Work

**Ultrametric data analysis.** Reference [1] models anomaly and change in data by embedding the data in an ultrametric space: starting from cross-tabulation counts (or other input formats), Correspondence Analysis endows the information space with a Euclidean metric, and anomaly or change is then modeled by an induced ultrametric, with particular interest in a sequential form of induction. This is methodologically important for us because it supplies a constructive route from raw experimental records to an ultrametric hypothesis: if a sensor register's error log can be processed the same way, the induced ultrametric becomes an empirical object rather than an assumption.

**Markov processes on $p$-adic spaces.** Reference [2] proposes a method for describing stationary Markov processes on the class of ultrametric spaces isometrically embeddable in the field $\mathbb{Q}_p$ of $p$-adic numbers, reducing the study of such processes to processes on $\mathbb{Q}_p$ so that the traditional machinery of $p$-adic mathematical physics can be applied. Our noise process in Section 3 is exactly an object of this class — a stationary hierarchical process on an ultrametric space realized inside $\mathbb{Q}_p$ — so [2] provides the mathematical home for the model.

**Noise as a foundational category.** Reference [3] introduces a special issue on quantum and classical frontiers of noise, using the weather and its butterfly effect as the typical example of why many natural phenomena are not predictable with certainty, and treating noise as the difference between the empirical output of an experiment and its statistical model. We adopt this framing: our claim is a statement about the *statistical geometry* of that difference, and the falsifiability register of Section 6 is a proposal for measuring it.

**$p$-adic statistical mechanics.** Reference [4] studies the three-state $p$-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of $p$-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p = 3$ for any nonzero value of the interactions, also solving the uniqueness problem. The Cayley tree is the canonical ultrametric hierarchy, and the $p$-dependence of its phase structure is a warning and an opportunity for us: the predictions of an ultrametric model can depend sharply on the prime $p$, which is itself a falsifiable signature.

**$p$-adic quantum mechanics.** Reference [5] describes $p$-adic mathematical physics as arising from efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, with the formulation of $p$-adic and adelic quantum mechanics — complex-valued wave functions of $p$-adic and adelic arguments — as a main achievement. Our model places a register's decoherence degrees of freedom in this tradition: the noise amplitudes live in $p$-adic value space while the probe states remain ordinary complex quantum states.

**Ultrametric models of natural structure.** Reference [6] uses basic properties of $p$-adic numbers to describe DNA sequence and the genetic code, with a central ultrametric $p$-adic information space whose basic elements are nucleotides, codons, and genes, finding a 5-adic model appropriate for DNA sequence, combined with a 2-adic distance. This is the clearest precedent that hierarchical biological information can be *usefully* encoded ultrametrically with an empirically identifiable prime; our hypothesis transfers the same move to decoherence statistics.

**Ultrametric functional analysis.** Reference [7] treats ultrametrics as a zero-dimensional analogue of ordinary metrics and proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem. For us this matters as a guarantee that the ultrametric lattice we postulate is not a fragile special case: ultrametric structures admit embedding, extension, and interpolation theories parallel to the Archimedean ones, so the model can be refined without changing category.

**Hierarchic quantum systems.** Reference [8] considers the $p$-adic wavelet transform as a possible tool for the description of hierarchic quantum systems. This is the closest antecedent to our technical program: a $p$-adic wavelet basis is a natural basis for a register whose error structure is hierarchical, and we use the level decomposition it implies in Section 3.

**Program documents.** Reference [9] is the direct proposal for $p$-adic quantum metrology under the title "Passive Error Resilience Through Ultrametric Geometry"; the summary supplied in the bibliography gives no further detail, so we relate to it only as the originating statement of the conjecture tested here. Reference [11], "Adelic Cross-Ratio," likewise has no supplied summary text, and we use it only as a pointer to the adelic vocabulary used in passing in Section 6. Reference [10] organizes sixteen published records from a single research program, spanning December 2025 to August 2026, into one testable claim: that trapped-ion quantum simulators are the first near-term platform on which ultrametric ($p$-adic) structure in quantum dynamics can be accepted or rejected by measurement. This supplies the experimental platform context for the falsifiable prediction of Section 5. Reference [12] claims that seven research domains are seven vocabularies for one structural object — nested hierarchical partition logic defined by the ultrametric inequality, with $p$-adic/adelic arithmetic as one realization and the hierarchy as the invariant — and lists three falsifiable hypotheses (H1 compression prior, H2 Archimedean comparison, and a third truncated in the supplied summary). Our paper is a deepening of H2-type comparison for the metrology domain.

## 3. Methods

### 3.1 Ultrametric lattice and hierarchy levels

Let the register consist of $N$ qubits organized into a binary (more generally $p$-ary) hierarchy of depth $L$, so that $N = p^L$ in the balanced case. The hierarchy is an ultrametric space $(X, d)$: for any three points $x, y, z \in X$,

$$d(x,z) \leq \max\{d(x,y), d(y,z)\},$$

which implies that any two balls are either nested or disjoint. Level $k \in \{0, 1, \dots, L\}$ consists of the clusters of diameter $p^{-k}$ in the standard $p$-adic normalization; level $0$ is the whole register, level $L$ the individual qubits.

### 3.2 Noise as a $p$-adic-valued stochastic process

Following the reduction logic of [2], we define the noise process on $\mathbb{Q}_p$ itself. To each cluster $C$ at level $k$ we attach a nonnegative error weight

$$\varepsilon_k(C) = \varepsilon_0\, p^{-k}, \qquad k = 0, 1, \dots, L,$$

where $\varepsilon_0 \in (0,1)$ is a dimensionless base rate. The $p$-adic valuation structure is essential: the weight of a cluster decays by the factor $p^{-1}$ per level of refinement, mirroring the norm of $p^k$ in $\mathbb{Q}_p$. A decoherence event is a pair $(k, C)$: an error of weight $\varepsilon_k(C)$ localized on cluster $C$. The physical interpretation is that errors are correlated within clusters and the correlation is hierarchical — an error at a coarse level touches many qubits coherently, an error at a fine level touches few.

### 3.3 Error propagation from the ultrametric inequality

Let $E$ be the event "the register's phase estimate is corrupted in the sensing window." Because balls in an ultrametric space are nested or disjoint, the error events $\{E_k\}_{k=0}^{L}$ attached to the levels form a nested family after the standard coalescence argument: within one level the clusters are disjoint, and across levels the dominating (coarsest, largest-weight) event contains its descendants. The union probability is therefore

$$P_{\mathrm{U}} = \Pr\Big(\bigcup_{k=0}^{L} E_k\Big) = \max_{0 \leq k \leq L} \Pr(E_k) = \varepsilon_0\, p^{-L},$$

since $\varepsilon_k = \varepsilon_0 p^{-k}$ is maximized at $k = L$. This is the precise sense of "errors cancel across nested clusters": the coarse, high-weight events are the *same* events as refinements of one another, not independent additions, so only the finest-scale weight survives as the effective corruption probability of a single logical sensing operation.

By contrast, under an Archimedean (independent-event) model the same level weights give the union bound

$$P_{\mathrm{A}} \leq \sum_{k=0}^{L} \varepsilon_0 p^{-k} = \varepsilon_0\, \frac{1 - p^{-(L+1)}}{1 - p^{-1}},$$

and with independent levels this bound is tight up to intersection corrections, which only lower $P_{\mathrm{A}}$; we use the sum as the Archimedean comparison value throughout, which is conservative for our claim (it is the *largest* reasonable Archimedean competitor only in the sense of an upper bound; see Section 6 for the effect of this choice).

### 3.4 Probe states and quantum Fisher information

The probe is an $N$-qubit GHZ state,

$$|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\big(|0\rangle^{\otimes N} + |1\rangle^{\otimes N}\big),$$

accumulating phase $\theta$ with QFI $F_Q = N^2$ in the noiseless case. Decoherence that destroys the phase coherence between the two branches with probability $P$ replaces the off-diagonal density-matrix element $\rho_{01}$ by $(1 - P)\,\rho_{01}$; the QFI of the resulting state is

$$F_Q(P) = N^2 (1 - P)^2.$$

The single-shot phase sensitivity is $\Delta\theta = 1/\sqrt{F_Q}$, and with $\nu$ independent repetitions, $\Delta\theta_\nu = 1/\sqrt{\nu F_Q}$.

### 3.5 Archimedean competitor: independent per-qubit dephasing

The standard Archimedean competitor models each qubit as dephasing independently with per-qubit coherence survival factor $c_0 = 1 - 2\varepsilon_0$ over the sensing window (the factor $2$ reflects that a depolarizing-type event with probability $\varepsilon_0$ damps the coherence by $1 - 2\varepsilon_0$). For the GHZ state the two branches accumulate $N$ independent dephasing events, so

$$\eta_{\mathrm{A}} = c_0^{\,N} = (1 - 2\varepsilon_0)^N, \qquad F_Q^{\mathrm{A}} = N^2 (1 - 2\varepsilon_0)^{2N}.$$

For product-state probes under the same independent dephasing with rate $\gamma$ per unit time, the standard optimization over sensing time $t$ gives $F_Q = N\, t^2 e^{-2\gamma t}$ per the single-probe QFI $t^2 e^{-2\gamma t}$; maximizing over $t$ yields the SQL scaling derived explicitly in Section 4.3.

## 4. Analysis

All numbers in this section are computed from the inputs stated here. Inputs: prime $p = 2$; hierarchy depth $L = 10$; base error weight $\varepsilon_0 = 10^{-2}$; register size $N = p^L = 2^{10} = 1024$ qubits; single shot ($\nu = 1$) unless stated.

### 4.1 Ultrametric versus Archimedean error probability

**Ultrametric.** From Section 3.3,

$$P_{\mathrm{U}} = \varepsilon_0\, p^{-L} = 10^{-2} \times 2^{-10} = 10^{-2} \times 9.765625 \times 10^{-4} = 9.765625 \times 10^{-6}.$$

So $P_{\mathrm{U}} \approx 9.77 \times 10^{-6}$.

**Archimedean union bound.**

$$P_{\mathrm{A}} = \varepsilon_0\, \frac{1 - 2^{-(L+1)}}{1 - 2^{-1}} = 10^{-2} \times \frac{1 - 2^{-11}}{0.5} = 10^{-2} \times \frac{1 - 4.8828125\times 10^{-4}}{0.5}.$$

Compute the numerator: $1 - 4.8828125 \times 10^{-4} = 0.99951171875$. Divide by $0.5$: $0.99951171875 / 0.5 = 1.9990234375$. Multiply by $\varepsilon_0$:

$$P_{\mathrm{A}} = 10^{-2} \times 1.9990234375 = 1.9990234375 \times 10^{-2} \approx 1.999 \times 10^{-2}.$$

**Ratio.**

$$\frac{P_{\mathrm{A}}}{P_{\mathrm{U}}} = \frac{1.9990234375 \times 10^{-2}}{9.765625 \times 10^{-6}} = \frac{1.9990234375}{9.765625} \times 10^{4} = 0.2046997... \times 10^{4}.$$

Compute exactly: $1.9990234375 / 9.765625 = 0.20469970703...$; times $10^4$ gives $2046.997...$, i.e.

$$\frac{P_{\mathrm{A}}}{P_{\mathrm{U}}} \approx 2.047 \times 10^{3} = 2047 \text{ to three significant figures } (2046.997...).$$

More precisely, $P_{\mathrm{A}}/P_{\mathrm{U}} = p^{L}\,(1 - p^{-(L+1)})/(1 - p^{-1}) = 1024 \times 1.9990234375 = 2046.997...$ Wait — check: $P_{\mathrm{U}} = \varepsilon_0 p^{-L}$, so $P_{\mathrm{A}}/P_{\mathrm{U}} = p^{L} (1 - p^{-(L+1)})/(1-p^{-1}) = 1024 \times 1.9990234375 = 2046.997...$ Indeed $1024 \times 1.9990234375 = 2046.998...$; compute: $1024 \times 2 = 2048$; subtract $1024 \times 4.8828125\times 10^{-4} = 0.5$; so $2048 - 0.5 = 2047.5$? Recompute: $1.9990234375 = 2 - 9.765625\times 10^{-4}$. Then $1024 \times (2 - 9.765625\times10^{-4}) = 2048 - 1.0 = 2047$. Check: $1024 \times 9.765625\times 10^{-4} = 1.0$ exactly, since $9.765625\times10^{-4} = 1/1024$. Therefore

$$\frac{P_{\mathrm{A}}}{P_{\mathrm{U}}} = 2047 \text{ exactly.}$$

(The earlier decimal $2046.997$ was an arithmetic slip; the exact value is $2047$, because $1 - 2^{-11} = 1 - \tfrac{1}{2048}$ and $\frac{1-1/2048}{1/2} \cdot 2^{10} = 2^{11} - 1 = 2047$.)

### 4.2 QFI and sensitivity at $N = 1024$

**Ultrametric coherence.** With $L = \log_2 N = 10$,

$$\eta_{\mathrm{U}} = 1 - P_{\mathrm{U}} = 1 - 9.765625\times 10^{-6} = 0.999990234375.$$

$$F_Q^{\mathrm{U}} = N^2 \eta_{\mathrm{U}}^2 = 1024^2 \times (0.999990234375)^2 = 1048576 \times 0.99998046886...$$

Compute $\eta_{\mathrm{U}}^2 = (1 - 9.765625\times10^{-6})^2 = 1 - 2\times 9.765625\times10^{-6} + 9.54\times10^{-11} = 1 - 1.953125\times10^{-5} + 9.54\times10^{-11} \approx 0.99998046887$. Then

$$F_Q^{\mathrm{U}} = 1048576 \times 0.99998046887 \approx 1048555.5.$$

$$\Delta\theta_{\mathrm{U}} = \frac{1}{\sqrt{F_Q^{\mathrm{U}}}} = \frac{1}{\sqrt{1048555.5}} \approx \frac{1}{1023.99} \approx 9.766 \times 10^{-4}.$$

(More directly, $\Delta\theta_{\mathrm{U}} = 1/(N\eta_{\mathrm{U}}) = 1/(1024 \times 0.99999023) = 1/1023.99 = 9.7656\times10^{-4}$, agreeing.)

**Archimedean GHZ coherence.**

$$\eta_{\mathrm{A}} = (1 - 2\varepsilon_0)^N = 0.98^{1024}.$$

Compute via the exponential: $\ln 0.98 = -0.020202707...$; $1024 \times (-0.020202707) = -20.687572$. Then

$$\eta_{\mathrm{A}} = e^{-20.687572} \approx 1.036 \times 10^{-9}.$$

(Compute: $e^{-20} = 2.0612\times10^{-9}$; $e^{-0.687572} = 0.5028$; product $= 1.0364\times10^{-9}$.)

$$F_Q^{\mathrm{A}} = N^2 \eta_{\mathrm{A}}^2 = 1048576 \times (1.0364\times10^{-9})^2 = 1048576 \times 1.0741\times10^{-18} \approx 1.126\times10^{-12}.$$

$$\Delta\theta_{\mathrm{A}} = \frac{1}{\sqrt{F_Q^{\mathrm{A}}}} = \frac{1}{\sqrt{1.126\times10^{-12}}} = \frac{1}{1.0611\times10^{-6}} \approx 9.42\times10^{5}.$$

**Ratio of sensitivities (single shot, GHZ probes).**

$$\frac{\Delta\theta_{\mathrm{A}}}{\Delta\theta_{\mathrm{U}}} = \frac{9.42\times10^{5}}{9.766\times10^{-4}} \approx 9.65\times10^{8}.$$

This enormous ratio is a within-model statement: it reflects the exponential collapse $c_0^N$ of GHZ coherence under independent noise versus the $N$-independent survival under the ultrametric model. It should not be read as an experimental prediction (Section 6).

### 4.3 Optimized sensing under independent dephasing: the honest Archimedean competitor

The comparison in Section 4.2 uses a fixed sensing window. The strongest Archimedean competitor optimizes the sensing time $t$. With signal $\theta = \omega t$ and independent dephasing at rate $\gamma$:

**Product probes.** Single-probe QFI: $f(t) = t^2 e^{-2\gamma t}$. Maximize: $f'(t) = e^{-2\gamma t}(2t - 2\gamma t^2) = 0 \Rightarrow t^* = 1/\gamma$. Then

$$f(t^*) = \frac{1}{\gamma^2} e^{-2}, \qquad F_Q^{\mathrm{prod}} = \frac{N}{\gamma^2} e^{-2}, \qquad \Delta\theta^{\mathrm{prod}} = \sqrt{\frac{\gamma^2 e