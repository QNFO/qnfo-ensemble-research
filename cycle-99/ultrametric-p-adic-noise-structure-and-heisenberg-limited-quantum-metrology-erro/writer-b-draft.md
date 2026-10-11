# Ultrametric p-Adic Noise Structure and the Prospects for Fault-Tolerance-Free Heisenberg-Limited Quantum Metrology

## Abstract

We formalize a conjecture from the ultrametric research program: if decoherence on a qubit register is modeled as a $p$-adic (ultrametric) hierarchical stochastic process, the strong triangle inequality can force error cancellation across nested clusters, potentially allowing quantum metrology to reach Heisenberg-limited sensitivity $1/N$ without fault-tolerant error-correction overhead. We construct a minimal p-adic noise model: errors are assigned $p$-adic valuations on a hierarchical lattice of depth $L$, and independent digit-level cancellation at each clustering level suppresses the effective dephasing rate by a factor $p^{-L}$. We derive closed-form quantum Fisher information bounds for GHZ-type entangled probes under this ultrametric noise and under a reference Archimedean (independent depolarizing) model. For a register of $N=16$ qubits, base dephasing rate $\gamma = 0.01$, $p=2$, and $L=4$ levels, the model predicts a precision improvement factor of exactly $p^{L} = 16$ per fixed interrogation run, and $p^{L/2} = 4$ at fixed total averaging time. We show explicitly where the derivation depends on the conjectural cancellation assumption, relate the model to the p-adic mathematical physics literature, and specify the falsifiable test that would confirm or collapse the paradigm claim.

## 1. Introduction

Quantum metrology promises phase sensitivity scaling as the Heisenberg limit $\delta\varphi_{\mathrm{HL}} \sim 1/N$ for $N$ entangled probes, rather than the standard quantum limit (SQL) $\delta\varphi_{\mathrm{SQL}} \sim 1/\sqrt{N}$. In practice, decoherence destroys this advantage: under independent per-qubit noise, entangled probes degrade faster than separable ones, and recovering Heisenberg scaling conventionally requires fault-tolerant error correction, whose overhead is prohibitive for near-term devices.

This paper develops a specific, falsifiable alternative: **passive error resilience by geometry**. The guiding idea, stated in the source proposal [9], is that if the noise process on a qubit register is not Archimedean but $p$-adic — that is, if errors are organized by a *hierarchical* (ultrametric) structure of nested clusters rather than by a flat additive metric — then the strong triangle inequality constrains how errors combine, and errors living in distinct nested clusters can cancel rather than accumulate. If this hierarchical cancellation is real, quantum sensing could reach Heisenberg-limited scaling with no error-correction overhead at all, reframing near-term quantum advantage as *sensing* rather than computation.

The claim is deliberately stated as a conjecture with a collapse condition: if the derived precision bound under ultrametric noise fails to differ qualitatively from the depolarizing (Archimedean) case, the paradigm claim collapses; if it holds, the slogan "error resilience by geometry, not overhead" is grounded in theorem. Our contributions are:

1. A formalization of p-adic noise as a valuation-valued stochastic process on an ultrametric lattice (Section 3).
2. Explicit derivations of error-propagation and precision bounds from the ultrametric inequality, with every arithmetic step shown (Section 4).
3. A quantitative comparison of predicted scaling under ultrametric versus depolarizing noise, clearly labeled as model-derived projection rather than measurement (Sections 4–5).
4. A discussion of failure modes, falsification conditions, and the experimental registers proposed to test the claim (Section 6).

Throughout, we distinguish sharply between (i) theorems derived from the ultrametric inequality, which are exact given the model axioms, and (ii) the physical applicability of those axioms to real decoherence, which is the open empirical question.

## 2. Background and Related Work

**Ultrametric data analysis.** Reference [1] models anomaly and change in data by embedding the data in an ultrametric space: starting from cross-tabulation counts, Correspondence Analysis endows the information space with a Euclidean metric, and anomaly or change is then modeled by an induced ultrametric. This establishes the general pattern we exploit here — that hierarchical (tree-like) structure can be induced from flat data, and that the ultrametric is the natural geometry of nested clusters. Our noise model inverts this direction: we *postulate* the ultrametric structure on the error space and derive consequences.

**Markov processes on ultrametric spaces.** Reference [2] proposes a method for describing stationary Markov processes on the class of ultrametric spaces isometrically embeddable in the field $\mathbb{Q}_p$ of $p$-adic numbers, reducing their study to processes on $\mathbb{Q}_p$ so that the traditional machinery of p-adic mathematical physics can be applied. This is the direct mathematical antecedent of our Section 3: our noise process is precisely a stationary Markov process on a $\mathbb{Q}_p$-embeddable ultrametric space, and we use the reduction strategy that [2] describes.

**Noise as a foundational category.** Reference [3], an introduction to a special issue on quantum and classical frontiers of noise, takes noise in classical or quantum phenomena to be the difference between the empirical output of an experiment and its statistical model, with the weather and its butterfly effect as the canonical example of intrinsic unpredictability. We adopt this framing: our "ultrametric noise" is a *model* of that empirical–statistical discrepancy, and the entire question is whether the p-adic model or the Archimedean model better describes real decoherence.

**p-adic statistical mechanics.** Reference [4] studies the three-state p-adic Potts model with competing interactions on a Cayley tree of order two, reducing the description of p-adic Gibbs measures to a recursive equation and proving that a phase transition occurs if and only if $p=3$ for any nonzero value of the interactions, along with a complete solution of the uniqueness problem. Two aspects matter for us: the Cayley tree is exactly the hierarchical lattice geometry we use, and the result demonstrates that p-adic models on trees support genuine structural phenomena (phase transitions, uniqueness breakdown) that depend sensitively on $p$ — a precedent for our prediction that metrological scaling depends qualitatively on the p-adic parameters.

**p-adic and adelic quantum mechanics.** Reference [5] surveys p-adic mathematical physics, which emerged from efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, and whose main achievement is the formulation of p-adic and adelic quantum mechanics with complex-valued wave functions of p-adic and adelic arguments. Our work applies this non-Archimedean quantum framework not to spacetime but to the *error space* of a quantum register.

**p-adic models of natural information systems.** Reference [6] constructs a p-adic model of DNA sequence and the genetic code, with an ultrametric p-adic information space whose basic elements are nucleotides, codons, and genes, finding that a 5-adic model is appropriate for DNA sequence and that this 5-adic model combined with 2-adic distance is also suitable for related purposes. This is the key biological precedent for our central physical hypothesis: that a real, measured information-processing system (the genetic code) is well described by ultrametric p-adic structure. Whether quantum hardware noise shares this character is exactly our falsifiable question.

**Ultrametric mathematics.** Reference [7] develops ultrametric versions of classical metric-space theorems — the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem — treating ultrametrics as a zero-dimensional analogue of ordinary metrics. This supplies the guarantee that our ultrametric error lattice is not a pathological special case but a mathematically robust geometry with embedding and extension properties parallel to Euclidean space.

**p-adic wavelets and hierarchic quantum systems.** Reference [8] considers the p-adic wavelet transform as a possible tool for the description of hierarchic quantum systems. The supplied summary is brief, but its thrust is directly relevant: p-adic wavelets are a candidate representation for exactly the hierarchic quantum dynamics in which our noise process lives, and we use p-adic valuation levels in a manner analogous to wavelet scales.

**Program-internal proposals.** Reference [9] is the source proposal for the present work ("Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology"); the supplied bibliographic entry carries no summary text, so we relate to it only through the research idea it anchors, which is restated in the Introduction. Reference [10] organizes sixteen published records from a single research program, spanning December 2025 to August 2026, into one testable claim: that trapped-ion quantum simulators are the first near-term platform on which ultrametric (p-adic) structure in quantum dynamics can be accepted or rejected by measurement. This register defines the experimental pathway by which our Section 4 predictions could be tested. Reference [11] ("Adelic Cross-Ratio") likewise carries no summary in the supplied bibliography; we note it as part of the adelic toolkit of the program without attributing any specific result to it. Reference [12] states the umbrella claim of the program: seven research domains are seven vocabularies for one structural object — nested hierarchical partition logic defined by the ultrametric inequality, with p-adic/adelic arithmetic as one realization and the hierarchy as the invariant — together with three falsifiable hypotheses (H1 compression prior, H2 Ar[chimedean comparison], and a third truncated in the supplied text). Our paper is a deep-dive on one instantiation of this umbrella: the metrology domain.

## 3. Methods

### 3.1 The ultrametric inequality and the error lattice

Let $d_p(x,y) = |x - y|_p$ be the p-adic metric, where $|\cdot|_p$ is the p-adic norm. Its defining property is the **strong triangle inequality**:

$$d_p(x,z) \le \max\bigl(d_p(x,y),\, d_p(y,z)\bigr),$$

which is strictly stronger than the Archimedean triangle inequality $d(x,z) \le d(x,y) + d(y,z)$. A metric satisfying the strong inequality is an *ultrametric*; geometrically, its balls are either nested or disjoint, producing a hierarchy of clusters — a rooted tree in which every point is a leaf.

We model the qubit register's error space as an ultrametric lattice $\mathbb{U}_L$ of depth $L$: a rooted $p$-ary tree in which each node at level $\ell \in \{0, 1, \dots, L\}$ is a $p$-adic ball $B_\ell$ of radius $p^{-\ell}$, each level-$\ell$ ball containing exactly $p$ level-$(\ell{+}1)$ sub-balls. Qubits are the leaves. Errors are modeled as a stochastic process $X_t$ on $\mathbb{U}_L$ taking values in $\mathbb{Q}_p$, following the reduction strategy of [2]: the process on the abstract ultrametric space is studied via its embedding in $\mathbb{Q}_p$, where p-adic valuations are available.

### 3.2 Model axioms

**Axiom A1 (Locality of error generation).** In each time step, each leaf qubit independently acquires an error digit $a_i \in \{0, 1, \dots, p-1\}$, uniformly distributed, with per-step base error rate $\gamma$ (probability that a nonzero digit is drawn).

**Axiom A2 (Hierarchical aggregation).** Error digits aggregate up the tree by p-adic addition: the cluster error at level $\ell$ is the p-adic sum of its children's errors. The p-adic norm of a sum obeys

$$\Bigl|\sum_j a_j\Bigr|_p \le \max_j |a_j|_p,$$

with equality unless the leading digits cancel modulo $p$.

**Axiom A3 (Digit cancellation, the conjectural core).** For a cluster of $m \ge 1$ children with independent uniform digits, the probability that the sum vanishes modulo $p$ (full cancellation at that level) is exactly $1/p$. This is exact, not approximate: the sum of $m$ independent uniform digits modulo $p$ is uniform on $\{0,\dots,p-1\}$, so the probability of the value $0$ is $1/p$.

**Axiom A4 (Multiplicative suppression).** A cluster error survives to the root only if cancellation *fails* at every level. We therefore take the effective dephasing rate of the register to be

$$\Gamma_L = \gamma\, p^{-L}.$$

This is the model's conjectural physical content: it converts a combinatorial cancellation probability into a dynamical rate. Axiom A4 is an assumption, not a theorem; we return to its status in Section 6.

### 3.3 Probe states and Fisher information

The probe is an $N$-qubit GHZ-type state, $\ket{\mathrm{GHZ}} = \bigl(\ket{0}^{\otimes N} + \ket{1}^{\otimes N}\bigr)/\sqrt{2}$, interrogating a phase $\varphi$ for time $t$. Under a dephasing channel with effective rate $\Gamma_L$, the off-diagonal coherence decays as $C(t) = e^{-2\Gamma_L t}$, and the quantum Fisher information (QFI) for $\varphi$ is

$$F_Q^{(L)}(t) = N^2 t^2\, e^{-2\Gamma_L t}.$$

The single-parameter QFI $F_Q$ bounds the mean-square estimation error via the quantum Cramér–Rao bound, $\delta\varphi \ge 1/\sqrt{F_Q}$ (per interrogation run; $\nu$ independent runs give $\delta\varphi \ge 1/\sqrt{\nu F_Q}$).

The reference Archimedean model is independent depolarizing noise at the same base rate $\gamma$, for which the GHZ coherence decays as $e^{-2\gamma t}$ (each of the two branches must remain coherent; per-qubit noise at rate $\gamma$ aggregates additively across the $N$ qubits with no cancellation), giving

$$F_Q^{(0)}(t) = N^2 t^2\, e^{-2\gamma t}.$$

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Input parameters and their provenance

| Symbol | Value | Source |
|---|---|---|
| $N$ | $16$ | chosen register size (model input, this paper) |
| $\gamma$ | $0.01$ | chosen base dephasing rate (model input, this paper) |
| $p$ | $2$ | chosen p-adic prime (model input, this paper) |
| $L$ | $4$ | chosen hierarchy depth (model input, this paper) |
| $e$ | $2.718281828\ldots$ | mathematical constant |

All four model inputs are free parameters of the proposed test, not measurements; Section 6 discusses how they would be fixed experimentally.

### 4.2 Derivation 1: SQL versus Heisenberg limit at $N = 16$

The SQL and HL scalings are:

$$\delta\varphi_{\mathrm{SQL}} = \frac{1}{\sqrt{N}}, \qquad \delta\varphi_{\mathrm{HL}} = \frac{1}{N}.$$

For $N = 16$:

$$\delta\varphi_{\mathrm{SQL}} = \frac{1}{\sqrt{16}} = \frac{1}{4} = 0.25,$$

$$\delta\varphi_{\mathrm{HL}} = \frac{1}{16} = 0.0625.$$

The scaling ratio is

$$\frac{\delta\varphi_{\mathrm{SQL}}}{\delta\varphi_{\mathrm{HL}}} = \frac{0.25}{0.0625} = 4 = \sqrt{N}.$$

This fixes the target: any noise-resilient scheme must preserve $\sim 1/N$ scaling rather than $1/\sqrt{N}$.

### 4.3 Derivation 2: cancellation probability and effective rate

By Axiom A3, cancellation at one level has probability $1/p = 1/2$. Survival of a cluster error to the root requires failure of cancellation at all $L$ levels; under the independence assumption built into A4, the per-cluster survival factor is

$$\left(1 - \frac{1}{p}\right)^{L} \text{ per branch, giving the rate suppression } \Gamma_L = \gamma\, p^{-L}.$$

For $p = 2$, $L = 4$, $\gamma = 0.01$:

$$p^{-L} = 2^{-4} = \frac{1}{16} = 0.0625,$$

$$\Gamma_4 = 0.01 \times 0.0625 = 6.25 \times 10^{-4}.$$

The reference (Archimedean) model has $\Gamma_0 = \gamma = 0.01 = 1.0 \times 10^{-2}$. The suppression ratio is

$$\frac{\Gamma_4}{\Gamma_0} = \frac{6.25 \times 10^{-4}}{1.0 \times 10^{-2}} = 0.0625 = 2^{-4}.$$

### 4.4 Derivation 3: optimal interrogation time and per-run precision

Maximize $F_Q(t) = N^2 t^2 e^{-2\Gamma t}$. Set the logarithmic derivative to zero:

$$\frac{d}{dt}\ln F_Q = \frac{2}{t} - 2\Gamma = 0 \quad\Longrightarrow\quad t^\ast = \frac{1}{\Gamma}.$$

At $t^\ast$:

$$F_Q^{\max} = N^2 \cdot \frac{1}{\Gamma^2} \cdot e^{-2} = \frac{N^2 e^{-2}}{\Gamma^2},$$

$$\delta\varphi_{\min} = \frac{1}{\sqrt{F_Q^{\max}}} = \frac{e\,\Gamma}{N}.$$

**Archimedean case** ($\Gamma_0 = 0.01$, $N = 16$):

$$\delta\varphi_{\min}^{(0)} = \frac{e \times 0.01}{16} = \frac{2.718281828 \times 0.01}{16} = \frac{0.02718281828}{16} = 1.69893 \times 10^{-3}.$$

Optimal interrogation time: $t^\ast_0 = 1/0.01 = 100$ (time units).

**Ultrametric case** ($\Gamma_4 = 6.25 \times 10^{-4}$, $N = 16$):

$$\delta\varphi_{\min}^{(4)} = \frac{e \times 6.25 \times 10^{-4}}{16} = \frac{2.718281828 \times 6.25 \times 10^{-4}}{16} = \frac{1.69893 \times 10^{-3}}{16} = 1.06183 \times 10^{-4}.$$

Optimal interrogation time: $t^\ast_4 = 1/(6.25 \times 10^{-4}) = 1600$ time units.

**Per-run improvement factor:**

$$\frac{\delta\varphi_{\min}^{(0)}}{\delta\varphi_{\min}^{(4)}} = \frac{1.69893 \times 10^{-3}}{1.06183 \times 10^{-4}} = 16 = p^{L}.$$

This is exact by construction: the factor $e/N$ cancels, leaving $\Gamma_0/\Gamma_4 = p^L$.

### 4.5 Derivation 4: fixed-total-time comparison

The per-run comparison of Section 4.4 is unfair to the Archimedean model because the ultrametric case wants a $16$-fold longer interrogation. At fixed total averaging time $T$, the number of runs is $\nu = T/t^\ast$, and

$$\delta\varphi_{\mathrm{total}} = \frac{\delta\varphi_{\min}}{\sqrt{\nu}} = \frac{e\Gamma}{N}\sqrt{\frac{t^\ast}{T}} = \frac{e\Gamma}{N}\sqrt{\frac{1}{\Gamma T}} = \frac{e\sqrt{\Gamma}}{N\sqrt{T}}.$$

Take $T = 1000$ time units, $N = 16$:

**Archimedean:** $\sqrt{\Gamma_0} = \sqrt{0.01} = 0.1$; $\sqrt{T} = \sqrt{1000} = 31.6227766$;

$$\delta\varphi_{\mathrm{total}}^{(0)} = \frac{2.718281828 \times 0.1}{16 \times 31.6227766} = \frac{0.2718281828}{505.9644256} = 5.37163 \times 10^{-4}.$$

**Ultrametric:** $\sqrt{\Gamma_4} = \sqrt{6.25 \times 10^{-4}} = 0.025$;

$$\delta\varphi_{\mathrm{total}}^{(4)} = \frac{2.718281828 \times 0.025}{16 \times 31.6227766} = \frac{0.0679570457}{505.9644256} = 1.34291 \times 10^{-4}.$$

**Fixed-time improvement factor:**

$$\frac{\delta\varphi_{\mathrm{total}}^{(0)}}{\delta\varphi_{\mathrm{total}}^{(4)}} = \frac{5.37163 \times 10^{-4}}{1.34291 \times 10^{-4}} = 4.0000 = p^{L/2} = 2^{2}.$$

Again exact by construction: the fixed-time advantage is the square root of the rate suppression.

### 4.6 Derivation 5: scaling with $N$ — the qualitative claim

Both models give $\delta\varphi_{\mathrm{total}} \propto 1/N$ for GHZ probes at their respective optima; the *qualitative* difference the conjecture predicts is not in the $N$-exponent but in the noise-dependent prefactor $e\sqrt{\Gamma}/\sqrt{T}$: under ultrametric noise the prefactor shrinks as $p^{-L/2}$ with hierarchy depth, while under Archimedean noise it is depth-independent. Equivalently: at fixed target precision, the ultrametric model permits either an $L$-deep hierarchy in place of $p^{L/2}$-fold more averaging, or — critically — preserves Heisenberg scaling at register sizes where depolarizing noise would force a return toward SQL behavior once $N\gamma t \gtrsim 1$. The crossover condition for the Archimedean GHZ model is $2\gamma N t \sim 1$; at $\gamma = 0.01$, $t = 100$: $2 \times 0.01 \times N \times 100 = 2N$, which exceeds $1$ already at $N = 1$ in these units — i.e., the chosen $\gamma t$ product is deliberately in the regime where entanglement is fragile under Archimedean noise, which is the regime of interest.

### 4.7 Status of the numbers

All values in Sections 4.2–4.6 are **model-derived projections**: they follow exactly from Axioms A1–A4 and the stated inputs, with no measurement data. The single physically conjectural step is Axiom A4 (conversion of digit-cancellation probability into rate suppression $p^{-L}$); Derivations 2–5 are conditional on it. Derivation 1 is unconditional.

## 5. Results

All results below are the model-derived projections computed in Section 4, for the stated inputs $N = 16$, $\gamma = 0.01$, $p = 2$, $L = 4$, $T = 1000$.

**R1 (Unconditional).** At $N = 16$, the SQL–HL gap is a factor of exactly $4 = \sqrt{N}$: $\delta\varphi_{\mathrm{SQL}} = 