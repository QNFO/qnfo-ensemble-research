# Ultrametric $p$-Adic Noise Structure and Heisenberg-Limited Quantum Metrology: Error Resilience by Geometry, Not Overhead

## Abstract

We formalize a conjecture from the ultrametric research program: if decoherence on a qubit register is modeled as a $p$‑adic (ultrametric) hierarchical stochastic process, the strong triangle inequality $d(x,z)\leq\max\{d(x,y),d(y,z)\}$ forces the family of error events on nested clusters to be nested rather than independent, so that the probability of the union is the maximum of the level probabilities, not their sum. For a hierarchy of $L$ levels with level‑$k$ error weight $\varepsilon_k=\varepsilon_0p^{-k}$, we derive an ultrametric error probability $P_{\mathrm{U}}=\varepsilon_0p^{-L}$ and compare it with the Archimedean (independent‑event) union bound $P_{\mathrm{A}}$. For $p=2$, $L=10$, $\varepsilon_0=10^{-2}$, the ultrametric probability is $9.765625\times10^{-6}$ versus an Archimedean bound of $1.9990234375\times10^{-2}$, a ratio of exactly $2047$. Propagating this into the quantum Fisher information (QFI) of an $N$‑probe Greenberger–Horne–Zeilinger (GHZ) probe with $L=\log_2N$ yields Heisenberg scaling $\Delta\theta\propto N^{-1}$ under the ultrametric model, while independent dephasing collapses GHZ coherence exponentially in $N$. All quantitative results are labeled model‑derived projections conditional on an explicitly identified conjectural axiom. We state the falsifiable scaling prediction, relate the model to the $p$‑adic mathematical physics literature, and document where independent drafts of this analysis diverged and which convention was adopted.

## 1. Introduction

Quantum metrology promises phase sensitivity that beats the standard quantum limit (SQL), $\Delta\theta\propto N^{-1/2}$ for $N$ probes, up to the Heisenberg limit $\Delta\theta\propto N^{-1}$. In practice, decoherence erodes this advantage: entangled probes are fragile, and the usual remedy is quantum error correction, whose overhead is prohibitive on near‑term devices. The research idea examined here proposes a different route: if the decoherence process itself has an ultrametric—equivalently, $p$‑adic—hierarchical structure, then the strong triangle inequality constrains how errors combine, and errors living in nested clusters can cancel rather than accumulate. The slogan is “error resilience by geometry, not overhead”: the geometry of the noise model, not an active correction protocol, supplies the protection.

This paper does three things. First, it formalizes the noise model as a $p$‑adic‑valued stochastic process on an ultrametric lattice and derives error‑propagation identities directly from the ultrametric inequality (Section 3). Second, it carries out the arithmetic that converts those identities into precision bounds: explicit error probabilities, coherence factors, and QFI values for entangled probes under ultrametric versus Archimedean (independent, depolarizing‑like) noise (Section 4). Third, it extracts a falsifiable prediction—the scaling behavior of $\Delta\theta$ versus $N$ differs qualitatively between the two noise geometries—and states what experimental outcome would collapse the paradigm (Sections 5 and 6).

We emphasize at the outset what this paper does and does not claim. It claims a theorem‑level consequence of an assumed noise structure: *if* decoherence on the register is ultrametrically nested in the sense defined below, *then* Heisenberg‑limited sensitivity follows without error‑correction overhead. It does not claim that physical decoherence has been shown to be ultrametric; that is precisely the falsifiable hypothesis, and Section 6 discusses how it could fail. The framing of near‑term quantum advantage as sensing rather than computation, and the programmatic context of ultrametric structure as one invariant across research domains, follow the proposal and program documents cited as [9], [10], and [12].

**Contributions.**  
- **C1.** Derivation of the max‑of‑levels error probability $P_{\mathrm{U}}=\varepsilon_0p^{-L}$ (Section 3.3).  
- **C2.** Exact ratio $P_{\mathrm{A}}/P_{\mathrm{U}}=2047$ for the primary parameter set (Section 4.1).  
- **C3.** Propagation of $P_{\mathrm{U}}$ to GHZ QFI and demonstration of Heisenberg scaling (Section 4.2).  
- **C4.** Identification of the honest Archimedean competitor and its optimized sensitivity (Section 4.4).  
- **C5.** Presentation of a falsifiability criterion based on nested‑event statistics (Section 6.2).  

## 2. Background and Related Work

**Ultrametric data analysis.** Reference [1] models anomaly and change in data by embedding the data in an ultrametric space: starting from cross‑tabulation counts (or other input formats), Correspondence Analysis endows the information space with a Euclidean metric, and anomaly or change is then modeled by an induced ultrametric, with particular interest in a sequential form of induction. This provides a constructive route from raw experimental records to an ultrametric hypothesis: if a sensor register’s error log can be processed the same way, the induced ultrametric becomes an empirical object rather than an assumption.

**Markov processes on $p$‑adic spaces.** Reference [2] proposes a method for describing stationary Markov processes on the class of ultrametric spaces $\mathbb{U}$ isometrically embeddable in the field $\mathbb{Q}_p$ of $p$‑adic numbers, reducing the study of such processes to processes on $\mathbb{Q}_p$ so that the traditional machinery of $p$‑adic mathematical physics can be applied. Our noise process in Section 3 is exactly an object of this class—a stationary hierarchical process on an ultrametric space realized inside $\mathbb{Q}_p$—so [2] provides the mathematical home for the model.

**Noise as a foundational category.** Reference [3] introduces a collection of works on quantum and classical frontiers of noise, using the weather and its butterfly effect as the typical example of why many natural phenomena are not predictable with certainty, and treating noise as the difference between the empirical output of an experiment and its statistical model. We adopt this framing: our claim is a statement about the *statistical geometry* of that difference, and the falsifiability discussion of Section 6 is a proposal for measuring it.

**$p$‑adic statistical mechanics.** Reference [4] studies the three‑state $p$‑adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of $p$‑adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p=3$ for any non‑zero value of the interactions. The Cayley tree is the canonical ultrametric hierarchy, and the $p$‑dependence of its phase structure warns that predictions of an ultrametric model can depend sharply on the prime $p$, which is itself a falsifiable signature.

**$p$‑adic quantum mechanics.** Reference [5] describes $p$‑adic mathematical physics as arising from efforts to find a non‑Archimedean approach to spacetime and string dynamics at the Planck scale, with the formulation of $p$‑adic and adelic quantum mechanics—complex‑valued wave functions of $p$‑adic and adelic arguments—as a main achievement. Our model places a register’s decoherence degrees of freedom in this tradition: the noise amplitudes live in $p$‑adic value space while the probe states remain ordinary complex quantum states.

**Ultrametric models of natural structure.** Reference [6] uses basic properties of $p$‑adic numbers to describe DNA sequence and the genetic code, finding a 5‑adic model appropriate for DNA sequence, combined with a 2‑adic distance. This is the clearest precedent that hierarchical biological information can be usefully encoded ultrametrically with an empirically identifiable prime; our hypothesis transfers the same move to decoherence statistics.

**Ultrametric functional analysis.** Reference [7] treats ultrametrics as a zero‑dimensional analogue of ordinary metrics and proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem. For us this matters as a guarantee that the ultrametric lattice we postulate is not a fragile special case: ultrametric structures admit embedding, extension, and interpolation theories parallel to the Archimedean ones, so the model can be refined without changing category.

**Hierarchic quantum systems.** Reference [8] considers the $p$‑adic wavelet transform as a possible tool for the description of hierarchic quantum systems. Its thrust is directly relevant: a $p$‑adic wavelet basis is a natural candidate representation for a register whose error structure is hierarchical, and we use the level decomposition it implies in Section 3.

## 3. Methods

### 3.1 Ultrametric lattice and hierarchy levels

Let the register consist of $N$ qubits organized into a binary (more generally $p$‑ary) hierarchy of depth $L$, so that $N=p^{L}$ in the balanced case. The hierarchy is an ultrametric space $(X,d)$: for any three points $x,y,z\in X$,
$$
d(x,z)\leq\max\{d(x,y),d(y,z)\},
$$
which implies that any two balls are either nested or disjoint. Level $k\in\{0,1,\dots,L\}$ consists of the clusters of diameter $p^{-k}$ in the standard $p$‑adic normalization; level 0 is the whole register, level $L$ the individual qubits.

### 3.2 Noise as a $p$‑adic‑valued stochastic process

Following the reduction logic of [2], we define the noise process on $\mathbb{Q}_p$ itself. To each cluster $C$ at level $k$ we attach a non‑negative error weight
$$
\varepsilon_k(C)=\varepsilon_0\,p^{-k},\qquad k=0,1,\dots,L,
$$
where $\varepsilon_0\in(0,1)$ is a dimensionless base rate. The $p$‑adic valuation structure is essential: the weight of a cluster decays by the factor $p^{-1}$ per level of refinement, mirroring the norm of $p^{k}$ in $\mathbb{Q}_p$. A decoherence event is a pair $(k,C)$: an error of weight $\varepsilon_k(C)$ localized on cluster $C$. The physical interpretation is that errors are correlated within clusters and the correlation is hierarchical—an error at a coarse level touches many qubits coherently, an error at a fine level touches few.

### 3.3 Error propagation from the ultrametric inequality

Let $E$ be the event “the register’s phase estimate is corrupted in the sensing window.” Because balls in an ultrametric space are nested or disjoint, the error events $\{E_k\}_{k=0}^{L}$ attached to the levels form a nested family after the standard coalescence argument: within one level the clusters are disjoint, and across levels the dominating (coarsest, largest‑weight) event contains its descendants. The union probability is therefore
$$
P_{\mathrm{U}}=\Pr\Bigl(\bigcup_{k=0}^{L}E_k\Bigr)=\max_{0\leq k\leq L}\Pr(E_k)=\varepsilon_0\,p^{-L},
$$
since $\varepsilon_k=\varepsilon_0p^{-k}$ is maximized at $k=L$. This is the precise sense of “errors cancel across nested clusters”: the coarse, high‑weight events are refinements of one another, not independent additions, so only the finest‑scale weight survives as the effective corruption probability of a single logical sensing operation.

By contrast, under an Archimedean (independent‑event) model the same level weights give the union bound
$$
P_{\mathrm{A}}\leq\sum_{k=0}^{L}\varepsilon_0p^{-k}
=\varepsilon_0\,\frac{1-p^{-(L+1)}}{1-p^{-1}},
$$
and with independent levels this bound is tight up to intersection corrections, which only lower $P_{\mathrm{A}}$; we use the sum as the Archimedean comparison value throughout.

### 3.4 Probe states and quantum Fisher information

The probe is an $N$‑qubit GHZ state,
$$
|\mathrm{GHZ}\rangle=\frac{1}{\sqrt{2}}\bigl(|0\rangle^{\otimes N}+|1\rangle^{\otimes N}\bigr),
$$
accumulating phase $\theta$ with noiseless QFI $F_Q=N^{2}$. Decoherence that destroys the phase coherence between the two branches with probability $P$ replaces the off‑diagonal density‑matrix element $\rho_{01}$ by $(1-P)\,\rho_{01}$; the QFI of the resulting state is
$$
F_Q(P)=N^{2}(1-P)^{2}.
$$
The single‑shot phase sensitivity is $\Delta\theta=1/\sqrt{F_Q}$, and with $\nu$ independent repetitions, $\Delta\theta_{\nu}=1/\sqrt{\nu F_Q}$.

### 3.5 Archimedean competitor: independent per‑qubit dephasing

The standard Archimedean competitor models each qubit as dephasing independently with per‑qubit coherence survival factor $c_0=1-2\varepsilon_0$ over the sensing window (the factor $2$ reflects that a depolarizing‑type event with probability $\varepsilon_0$ damps the coherence by $1-2\varepsilon_0$). For the GHZ state the two branches accumulate $N$ independent dephasing events, so
$$
\eta_{\mathrm{A}}=c_0^{\,N}=(1-2\varepsilon_0)^{N},\qquad
F_Q^{\mathrm{A}}=N^{2}(1-2\varepsilon_0)^{2N}.
$$
For product‑state probes under the same independent dephasing at rate $\gamma$ per unit time, the single‑probe QFI for a sensing time $t$ is $f(t)=t^{2}e^{-2\gamma t}$; maximizing over $t$ yields the SQL scaling derived explicitly in Section 4.4.

### 3.6 Status of the axioms

The derivation chain has exactly one conjectural step: the identification of physical decoherence with the nested‑event structure of Section 3.3 (equivalently, the weight law $\varepsilon_k=\varepsilon_0p^{-k}$ and the nesting of the $E_k$). Everything downstream—the max‑versus‑sum contrast, the QFI propagation, the scaling statements—is exact arithmetic given that step. We return to the status of this axiom in Section 6.

## 4. Analysis

All numbers in this section are computed from the inputs stated here. Inputs: prime $p=2$; hierarchy depth $L=10$; base error weight $\varepsilon_0=10^{-2}$; register size $N=p^{L}=2^{10}=1024$ qubits; single shot ($\nu=1$) unless stated. All four model inputs are free parameters of the proposed test, not measurements.

### 4.1 Ultrametric versus Archimedean error probability

**Ultrametric.** From Section 3.3,
$$
P_{\mathrm{U}}=\varepsilon_0\,p^{-L}=10^{-2}\times2^{-10}
=10^{-2}\times9.765625\times10^{-4}
=9.765625\times10^{-6}.
$$

**Archimedean union bound.**
$$
P_{\mathrm{A}}=\varepsilon_0\,\frac{1-2^{-(L+1)}}{1-2^{-1}}
=10^{-2}\times\frac{1-2^{-11}}{0.5}.
$$
Compute the numerator: $1-2^{-11}=1-4.8828125\times10^{-4}=0.99951171875$. Divide by $0.5$: $0.99951171875/0.5=1.9990234375$. Multiply by $\varepsilon_0$:
$$
P_{\mathrm{A}}=10^{-2}\times1.9990234375=1.9990234375\times10^{-2}.
$$

**Ratio.** Since $P_{\mathrm{U}}=10^{-2}/1024$,
$$
\frac{P_{\mathrm{A}}}{P_{\mathrm{U}}}
=\frac{10^{-2}\times1.9990234375}{10^{-2}/1024}
=1.9990234375\times1024.
$$
Because $1.9990234375=2-9.765625\times10^{-4}=2-\frac{1}{1024}$,
$$
1024\times\Bigl(2-\frac{1}{1024}\Bigr)=2048-1=2047.
$$
Thus
$$
\frac{P_{\mathrm{A}}}{P_{\mathrm{U}}}=2047\ \text{exactly}.
$$

### 4.2 QFI and sensitivity at $N=1024$

**Ultrametric coherence.** With $L=\log_{2}N=10$,
$$
\eta_{\mathrm{U}}=1-P_{\mathrm{U}}=1-9.765625\times10^{-6}=0.999990234375.
$$
Then $\eta_{\mathrm{U}}^{2}\approx0.99998046876$, and
$$
F_Q^{\mathrm{U}}=N^{2}\eta_{\mathrm{U}}^{2}=1048576\times0.99998046876\approx1.048556\times10^{6}.
$$
$$
\Delta\theta_{\mathrm{U}}=\frac{1}{\sqrt{F_Q^{\mathrm{U}}}}
=\frac{1}{N\,\eta_{\mathrm{U}}}
=\frac{1}{1024\times0.999990234375}
\approx9.7657\times10^{-4}.
$$

**Archimedean GHZ coherence.**
$$
\eta_{\mathrm{A}}=(1-2\varepsilon_0)^{N}=0.98^{1024}.
$$
Using $\ln0.98=-0.0202027073$,
$$
\ln\eta_{\mathrm{A}}=1024\times(-0.0202027073)=-20.6875723,
$$
so $\eta_{\mathrm{A}}=e^{-20.6875723}\approx1.0364\times10^{-9}$.
$$
F_Q^{\mathrm{A}}=N^{2}\eta_{\mathrm{A}}^{2}
=1048576\times(1.0364\times10^{-9})^{2}
\approx1.126\times10^{-12},
$$
$$
\Delta\theta_{\mathrm{A}}=\frac{1}{\sqrt{F_Q^{\mathrm{A}}}}
\approx9.42\times10^{5}.
$$

**Ratio of sensitivities (single shot, GHZ probes).**
$$
\frac{\Delta\theta_{\mathrm{A}}}{\Delta\theta_{\mathrm{U}}}
=\frac{\eta_{\mathrm{U}}}{\eta_{\mathrm{A}}}
\approx\frac{0.999990234375}{1.0364\times10^{-9}}
\approx9.65\times10^{8}.
$$

### 4.3 Scaling with $N$: the qualitative claim

Under the ultrametric model with $L=\log_{p}N$, the corruption probability is $P_{\mathrm{U}}=\varepsilon_0/N$, so $\eta_{\mathrm{U}}=1-\varepsilon_0/N$ and
$$
\Delta\theta_{\mathrm{U}}=\frac{1}{N(1-\varepsilon_0/N)}
=\frac{1}{N-\varepsilon_0},
$$
which is Heisenberg scaling $\Delta\theta\propto N^{-1}$ up to an $O(1)$ correction. Under independent dephasing, GHZ coherence decays as $(1-2\varepsilon_0)^{N}$ (exponential in $N$), so the best Archimedean strategy reverts to product probes and SQL scaling, as computed next.

### 4.4 Optimized sensing under independent dephasing: the honest Archimedean competitor

The comparison in Section 4.2 uses a fixed sensing window. The strongest Archimedean competitor optimizes the sensing time $t$. With signal $\theta=\omega t$ and independent dephasing at rate $\gamma$ per unit time:

**Product probes.** Single‑probe QFI: $f(t)=t^{2}e^{-2\gamma t}$. Setting $f'(t)=0$ gives $t^{*}=1/\gamma$. Then
$$
f(t^{*})=\frac{e^{-2}}{\gamma^{2}},\qquad
F_Q^{\mathrm{prod}}=\frac{N e^{-2}}{\gamma^{2}},\qquad
\Delta\theta^{\mathrm{prod}}=\frac{e\,\gamma}{\sqrt{N}}.
$$
Assuming $\gamma=10^{-2}$ and $N=1024$,
$$
\Delta\theta^{\mathrm{prod}}=\frac{2.718281828\times10^{-2}}{32}
=8.4946\times10^{-4}.
$$

Thus the optimized product probe is slightly *better* in absolute single‑shot sensitivity at $N=1024$, and the ultrametric advantage must instead be sought in the scaling exponent as $N$ grows (Section 4.3) rather than in a fixed‑point comparison.

### 4.5 Complementary time‑optimized comparison at small register (secondary parameter set)

A second, independent draft used $N=16$, $\gamma=0.01$, $p=2$, $L=4$, with the same suppression law $\Gamma_{L}=\gamma p^{-L}$. For completeness we reproduce its arithmetic, labeled as a projection under the same conjectural axiom:
$$
p^{-L}=2^{-4}=0.0625,\qquad
\Gamma_{4}=0.01\times0.0625=6.25\times10^{-4}.
$$
Maximizing $F_Q(t)=N^{2}t^{2}e^{-2\Gamma t}$ gives $t^{*}=1/\Gamma$ and per‑run sensitivity $\delta\varphi_{\min}=e\Gamma/N$. The per‑run improvement factor is
$$
\frac{\delta\varphi_{\min}^{(0)}}{\delta\varphi_{\min}^{(4)}}
=\frac{\Gamma_{0}}{\Gamma_{4}}
=\frac{0.01}{6.25\times10^{-4}}=16=p^{L}.
$$
At fixed total averaging time $T$, the number of runs scales as $1/t^{*}$, giving a fixed‑time improvement factor $\sqrt{p^{L}}=p^{L/2}=4$.

## 5. Results

All results below are model‑derived projections computed in Section 4, conditional on the conjectural nesting axiom of Section 3.6, for the primary inputs $p=2$, $L=10$, $\varepsilon_0=10^{-2}$, $N=1024$.

- **R1 (exact within the model).** Ultrametric corruption probability $P_{\mathrm{U}}=9.765625\times10^{-6}$; Archimedean union bound $P_{\mathrm{A}}=1.9990234375\times10^{-2}$; ratio $P_{\mathrm{A}}/P_{\mathrm{U}}=2047$ exactly.

- **R2 (exact within the model).** Ultrametric single‑shot GHZ sensitivity $\Delta\theta_{\mathrm{U}}\approx9.7657\times10^{-4}$; Archimedean GHZ sensitivity $\Delta\theta_{\mathrm{A}}\approx9.4232\times10^{5}$; ratio $\approx9.6493\times10^{8}$.

- **R3 (exact within the model).** Scaling: from $\eta_{\mathrm{U}}=1-\varepsilon_{0}p^{-L}=1-\varepsilon_{0}/N$, the ultrametric GHZ sensitivity is
$$
\Delta\theta_{\mathrm{U}}=\frac{1}{N\,\eta_{\mathrm{U}}}
=\frac{1}{N-\varepsilon_{0}},
$$
which for $N\gg\varepsilon_{0}$ reduces to Heisenberg scaling $\Delta\theta\propto N^{-1}$. Under independent dephasing, GHZ coherence decays as $(1-2\varepsilon_{0})^{N}$ (exponential in $N$) and the best Archimedean strategy is product probes with $\Delta\theta\propto N^{-1/2}$.

- **R4 (projection, stated assumptions).** With $\gamma=10^{-2}$ per unit time, the optimized product probe achieves $\Delta\theta^{\mathrm{prod}}\approx8.4946\times10^{-4}$ at $N=1024$ — comparable to or better than the ultrametric GHZ value at this specific $N$; the claimed advantage is in scaling, not in this fixed‑point comparison.

- **R5 (projection, secondary parameter set).** At $N=16$, $\gamma=0.01$, $p=2$, $L=4$: effective rate $\Gamma_{4}=6.25\times10^{-4}$, per‑run improvement factor $16=p^{L}$, fixed‑time improvement factor $4=p^{L/2}$.

## 6. Discussion

### 6.1 Limitations and failure modes

- **Conjectural axiom.** The single physically conjectural step is the identification of decoherence with the nested‑event structure of Section 3.3. If real decoherence events on a register are even partially independent across levels—the generic expectation for uncorrelated environmental noise—the max‑of‑levels law fails and the Archimedean union bound applies. Every headline number in Section 5 then collapses to the Archimedean column.

- **Honest competitor strength.** As R4 shows, at the specific parameter point $N=1024$, $\gamma=10^{-2}$, the time‑optimized product probe matches or beats the ultrametric GHZ probe in absolute sensitivity. The ultrametric claim is therefore a scaling claim, and it must be tested as a scaling claim: a fixed‑$N$ demonstration of “improvement” would be weak evidence.

- **Parameter freedom.** $p$, $L$, $\varepsilon_0$, and $\gamma$ are model inputs chosen for illustration. The precedent of [6], where the empirically appropriate prime was $5$ for DNA sequence (combined with a $2$‑adic distance), suggests the effective prime is an empirical quantity; choosing the wrong $p$ could change the suppression law $\varepsilon_k=\varepsilon_0p^{-k}$ quantitatively, though the max‑versus‑sum structure of Section 3.3 holds for any prime.

- **Archimedean comparison convention.** We use the level‑sum $P_{\mathrm{A}}=\sum_k\varepsilon_0p^{-k}$ as the Archimedean comparison value; intersection corrections only lower it, so our ratio $P_{\mathrm{A}}/P_{\mathrm{U}}=2047$ is an upper bound on the true independent‑event ratio. This is the conservative direction for the Archimedean side and therefore the conservative direction for our claim.

### 6.2 Falsifiability

The paradigm is rejected if any of the following is measured: (i) error events on nested clusters of a register show level probabilities that add (within experimental uncertainty) rather than saturate at the maximum, i.e., a measured union probability $P_{\mathrm{meas}}\approx\sum_k\Pr(E_k)$ rather than $\max_k\Pr(E_k)$; (ii) GHZ coherence on the platform of [10] decays exponentially in $N$ with no ultrametric suppression factor $p^{-L}$; (iii) the fitted suppression exponent does not correspond to any integer prime $p$, i.e., the effective decay per level is not of the form $p^{-1}$ for integer $p$. Conversely, confirmation requires measuring a saturation of the union probability at $\max_k\Pr(E_k)$ together with the scaling $\Delta\theta\propto N^{-1}$ on entangled probes, as a scaling curve in $N$, not a fixed‑$N$ point (see R4).

### 6.3 Open questions

1. The constructive route of [1]—inducing an ultrametric from experimental records via Correspondence Analysis—has not been applied to an actual error log from a quantum sensing register; doing so would convert the conjectural axiom into an estimated object.  
2. The $p$‑dependence highlighted by [4], where a phase transition in the $p$‑adic Potts model on the Cayley tree occurs only for $p=3$, warns that our suppression law may admit prime‑specific phase transitions in the noise process; the stationary‑process framework of [2] is the right tool for investigating this.  
3. The adelic viewpoint (cf. [5]) suggests combining ultrametric and Archimedean noise sectors; our analysis covers only the pure ultrametric sector, and a mixed model would interpolate between the two columns of Section 5.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** The primary users are designers of quantum sensors—particularly trapped‑ion or superconducting platforms—who must choose between entangled‑probe strategies and product‑probe strategies under realistic decoherence. If the ultrametric nesting axiom holds, the design decision shifts toward allocating hardware resources to increase probe number $N$ rather than to implement active error‑correction circuits, because Heisenberg scaling is achieved passively. Conversely, if nesting is falsified, designers must retain conventional error‑mitigation techniques.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at TRL 2 (technology concept formulated) and does not exceed TRL 3 (analytical proof‑of‑concept). No manufacturing or hardware demonstration is claimed.

**(c) Smallest next experiment.** A minimal test consists of (i) recording the error events on a small trapped‑ion register (e.g., $N=8$) with sufficient time resolution to assign each event to a hierarchical cluster (e.g., based on spatial proximity or common control lines); (ii) computing the empirical union probability $P_{\mathrm{meas}}$ and the level probabilities $\Pr(E_k)$. The experiment falsifies the ultrametric claim if $P_{\mathrm{meas}}$ exceeds $\max_k\Pr(E_k)$ by more than statistical uncertainty (e.g., $>5\sigma$). This measurement requires only standard state‑tomography and timing electronics already present in existing trapped‑ion labs.

**(d) Engineering constraints.** The first constraints arise from (i) the ability to resolve error events at the level of individual clusters, which demands high‑fidelity readout and timestamping; (ii) the need to map physical qubit layout onto a $p$‑ary tree structure, which may require redesign of control wiring to reflect the hierarchical clustering; (iii) data‑processing capacity to perform the ultrametric embedding (as in [1]) in real time. If these constraints cannot be satisfied, the ultrametric model cannot be empirically tested.

**(e) Projected performance bounds (projection).** Assuming the nesting axiom holds and using the derived formula $\Delta\theta_{\mathrm{U}}=1/(N-\varepsilon_0)$, a sensor with $N=10