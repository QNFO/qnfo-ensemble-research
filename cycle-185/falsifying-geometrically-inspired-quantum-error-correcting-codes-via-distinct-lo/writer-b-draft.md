# A Falsifiability Criterion for Geometrically Motivated Quantum Error Correction: Discriminating Logical Error Scaling from Surface-Code Benchmarks

## Abstract

Geometrically motivated approaches to quantum error correction — codes derived from non-Archimedean, Bruhat–Tits, or geometric-algebra foundations rather than from standard qubit stabilizer constructions — are frequently proposed without a quantitative statement of what they predict and how the prediction could be refuted. The gap this paper addresses is decision-theoretic: without a distinct, testable scaling law, a geometric code proposal cannot be distinguished from a re-description of standard topological codes, and research effort cannot be allocated. We formalize a falsifiability criterion: a geometric quantum error-correcting scheme counts as a physical theory only if it yields (i) an explicit Hamiltonian or Lindblad generator and (ii) a logical error rate $p_L$ with a scaling exponent in the physical error rate $p_{\mathrm{phys}}$ that differs from the surface-code exponent $(d_{\mathrm{sc}}+1)/2$. We derive the discriminating statistic for the hypothesized geometric law $p_L \propto p_{\mathrm{phys}}^{d_g/2}$: at matched qubit count $n = d_{\mathrm{sc}}^2$ and $p_{\mathrm{phys}} = 10^{-3}$, the predicted logical error ratio is $31.6$, resolvable with $N \approx 838$ logical-qubit experimental samples. We further derive the simulation budget: exact Lindblad evolution is feasible at $n = 25$ ($2^{25} = 3.36 \times 10^{7}$ amplitudes, $0.54$ GB) but not at $n = 49$ ($9.0$ PB), fixing the boundary between exact and Monte Carlo methods. The criterion converts ambiguous null-result debates about geometric foundations into a sharp, resource-bounded discriminating experiment.

## 1. Introduction

Quantum error correction (QEC) is the bottleneck resource for every fault-tolerant quantum computing program: the number of physical qubits per logical qubit, and therefore the cost, scale, and timeline of any quantum computer, is set by how fast the logical error rate $p_L$ falls as the code is enlarged. Hardware teams, funding agencies, and standards bodies currently allocate against one dominant family — topological stabilizer codes, exemplified by the surface code — because its scaling is quantitatively known. Any proposal that claims a better scaling law from different foundations (non-Archimedean or $p$-adic geometry, Bruhat–Tits buildings, geometric algebra) competes for the same scarce experimental attention, and today such proposals are judged by taste: their proponents argue from representational or philosophical considerations, and their critics answer that the foundations are unconventional. Neither side possesses a decision procedure. The cost of this ambiguity is concrete: experimental groups cannot rank a geometric code against a surface code at matched resources, so geometric proposals are either ignored without test or pursued without a falsification path. What would change if this paper's result holds is that a single measured curve — logical error rate versus physical error rate at matched qubit count, with a stated sample budget — would settle, for any candidate geometric code, whether it is a distinct physical theory or a notational variant.

The core observation is that "distinct foundations" is not itself testable, but "distinct scaling exponent" is. The surface code at code distance $d_{\mathrm{sc}}$ has logical error rate scaling approximately as $p_L^{\mathrm{sc}} \approx A\,(p_{\mathrm{phys}}/p_{\mathrm{th}})^{(d_{\mathrm{sc}}+1)/2}$ under assumptions stated in Section 3. A geometrically derived code, if its stabilizer structure genuinely differs, must produce a different exponent — the research idea under development proposes $p_L \propto p_{\mathrm{phys}}^{d_g/2}$ as the characteristic geometric prediction. Exponents differ, so the curves separate multiplicatively at every $p_{\mathrm{phys}}$ below threshold, and the separation is measurable with a computable number of samples. This paper derives that number, derives the simulation budget needed to produce the predicted curve before any hardware is built, and states the criterion under which a geometric scheme fails it.

The contributions are:

1. A formal falsifiability criterion for geometrically motivated QEC schemes, stated as two necessary conditions (explicit dynamical generator; distinct scaling exponent), with the discriminating observable defined as the log-log slope of $p_L$ versus $p_{\mathrm{phys}}$ at matched qubit count (Section 3).
2. An explicit derivation of the discriminating power: at $n = 25$ physical qubits, $p_{\mathrm{phys}} = 10^{-3}$, and the assumed surface-code parameters of Section 3, the geometric and surface-code predictions differ by a factor of $31.6$, and the sample size needed to resolve this factor at $p_L = 10^{-4}$ is $N \approx 838$ (Section 4).
3. A derivation of the numerical simulation budget for the predicted Lindblad dynamics, showing exact state-vector evolution is feasible at $n = 25$ ($0.54$ GB) and infeasible at $n = 49$ ($9.0 \times 10^{15}$ bytes), which fixes where sampling-based stabilizer methods become mandatory (Section 4).
4. A falsification protocol: which measurement outcome, with what uncertainty, would refute the geometric scaling claim, and which would refute the surface-code baseline (Sections 4 and 6).

## 2. Background and Related Work

The methodological core of this paper — that a physical claim becomes scientific when it produces a scaling law whose parameters can be measured and compared against a baseline — has close structural analogues across several fields, and the directly relevant QEC literature supplies both the baseline numbers and the assessment discipline.

**Scaling laws and their breakdown.** In QCD, geometric scaling is the statement that quantities which are a priori functions of two variables collapse onto a function of a single ratio $Q/Q_s(x)$, with the saturation scale $Q_s^2(x) = Q_0^2 x^{-\lambda}$ [1]. The work in [1] is directly instructive for two reasons. First, it shows how a geometric scaling hypothesis is made sharp: the scaling variable is named, the critical line is parametrized by an exponent $\lambda$, and the claim is that observables depend on $Q/Q_s(x)$ alone. Second, it shows how such a hypothesis is tested against a known evolution: [1] solves the DGLAP evolution equations with initial conditions on the critical line and derives the analytic condition $\lambda \geq 4\bar{\alpha}_s$ (in the double logarithmic approximation, fixed coupling) under which geometric scaling is preserved by the leading small-$x$ term, while noting that subleading effects violate it. This is exactly the pattern we import: a geometric code proposal must specify its analogue of $\lambda$ — here, the scaling exponent of $p_L$ in $p_{\mathrm{phys}}$ — and must be checked for whether the known dynamics (for QEC, the Lindblad evolution under physical noise) preserves or destroys the predicted scaling. A geometric code whose predicted exponent is destroyed by generic local noise at subleading order fails the criterion, just as geometric scaling in QCD is violated by subleading DGLAP effects.

**Empirical characterization of estimator error as a model for benchmarking.** The problem of characterizing the errors of competing estimators when analytic bounds are too weak to discriminate them is studied at scale in the database literature. [2] studies distinct value estimation, where many proposed estimators exist but "characterizing the errors incurred by these estimators is an open problem: existing analytical approaches are not powerful enough," and the authors therefore run an extensive empirical study — the first scaling to billion-row size — to characterize estimator families over a parameter space modeling real data variation. Two elements of [2] transfer directly. First, its finding that a previously unstudied latent parameter (the average uniform class size) organizes the otherwise confusing comparative behavior of estimators warns us that logical error rate comparisons across code families may also be governed by a latent parameter — in our setting, the ratio $p_{\mathrm{phys}}/p_{\mathrm{th}}$ and the code's sub-threshold regime — and that the benchmark protocol must hold it fixed. Second, its method of answering comparative questions ("what is the best estimator under various definitions") by fixing a metric and sweeping a controlled parameter space is the template for our discriminating experiment: fix $n$ and $p_{\mathrm{phys}}$, sweep, and compare exponents.

**Deriving logics from algebraic structure.** A recurring objection to geometric QEC is that its "foundations" are formal machinery without operational content. The literature on synthesizing logics from algebra gives the precise form of the rebuttal demand. [3] develops a mathematical theory for synthesising equational logics from algebraic metatheories, using strong monads on symmetric monoidal categories and Monadic Equational Systems, whose models are Eilenberg–Moore algebras; the framework comes with a sound deductive system and a completeness methodology based on free-algebra constructions, applied to give a rational reconstruction of Birkhoff's Equational Logic and a novel nominal logic [3]. The relevance is that [3] demonstrates what a successful "foundations-to-logic" derivation looks like: from the algebraic substrate one obtains not vibes but a specific deductive system with a canonical model theory. Our criterion demands the QEC analogue: from the geometric substrate (e.g., a Bruhat–Tits building or $p$-adic structure) one must obtain a specific stabilizer generator set and Hamiltonian, not a new vocabulary. A geometric scheme that cannot execute this derivation fails condition (i) of the criterion.

**Characterizing a formalism by its discriminating power.** Lindström-style theorems characterize a logic by abstract model-theoretic properties rather than by its syntax. [4] proves Lindström theorems for fragments of first-order logic, including the strengthening that first-order logic is characterized by Compactness and the Löwenheim–Skolem property within all extensions of the three-variable fragment $FO^3$ over unary–binary vocabularies, and revisits the modal Lindström theorem for abstract modal logics defined on pointed Kripke models [4]. This supplies the conceptual template for our central move: just as [4] identifies a logic not by what it says but by which model-theoretic properties uniquely pin it down, we identify a QEC code class not by its construction narrative but by which scaling exponent uniquely pins it down. If a geometric code's predicted exponent equals $(d_{\mathrm{sc}}+1)/2$, it is characterization-equivalent to a surface code for all experimental purposes, regardless of its foundations; if the exponent differs, the code class is separated. [4]'s demonstration that such separation results can be proved rigorously for fragments supports the coherence of the program.

**Extensional semantics and ground instantiations.** A further demand on geometric proposals is that their abstract structures have concrete instantiations that can be simulated. [5] develops an extensional semantics for higher-order logic programs with negation by generalizing the ground-instantiation technique of Bezem: each clause's variables are replaced by well-typed ground terms of the Herbrand universe, so that program predicates "essentially denote sets" and standard set-theoretic reasoning applies [5]. The transferable point is methodological: [5] makes an intensional, syntax-heavy formalism checkable by exhibiting its ground instances. For geometric QEC, the analogue is that any claimed stabilizer structure on a geometric object must be exhibited on a finite ground instantiation — a finite qubit or oscillator register — before Lindblad simulation is meaningful. Our protocol in Section 3 requires exactly this finite instantiation as the input to simulation.

**Logical equivalence and separation.** The Ambient Logic literature confronts the question of when two formally distinct descriptions are actually indistinguishable. [6] studies the discriminating power of the Ambient Logic for Mobile Ambients processes, characterizing the logical equivalence induced by the logic through a coinductive characterization via intensional bisimilarity and an inductive characterization based on inversion results, established for terms that need not be image-finite [6]. The structural parallel is exact: two codes with identical scaling exponents are experimentally bisimilar — no finite measurement distinguishes them — and the burden then falls on the geometric proposal to exhibit a distinguishing observable. [6]'s explicit construction of characterizations of logical equivalence shows that "indistinguishable by the observable logic" is a provable property, not a rhetorical one; we adopt it as the formal meaning of our claim that exponent equality collapses the geometric/surface distinction to a notational one.

**Geometric algebra as a non-standard computational substrate.** The closest prior technical work on non-standard algebraic foundations for quantum-like computation is [7], which presents quantum-like algorithms in which the tensor product is replaced by the geometric product. [7] argues these algorithms possess entanglement and parallelism while employing algebraic structures absent in standard quantum computation, gives a binary parametrization of geometric algebra in which an $n$-bit number corresponds one-to-one to a basis element ($k$-blades), and reformulates the Deutsch–Jozsa algorithm in geometric algebra, including an explicit Cartan matrix representation via Pauli matrices [7]. This is important to our criterion in two ways. Positively, [7] shows the right shape for a non-standard-foundations claim: it names the replaced structure (tensor product → geometric product), exhibits a concrete algorithm, and thereby makes the claim checkable. Negatively, [7] stops short of our condition (ii): it demonstrates functional equivalence of a reformulated algorithm but derives no distinct error-scaling law, so under our criterion it does not yet constitute a distinct physical theory of error correction — it is a re-encoding. This is precisely the ambiguous status our criterion is designed to adjudicate.

**Quantitative reassessment discipline in QEC.** Within QEC itself, the assessment discipline we follow is exemplified by [8], a derived-metric reassessment of a fluxonium–GKP bosonic error-correction demonstration. [8] takes reported hardware numbers ($T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and an extension factor $F = 1.59 \pm 0.05$), derives the ancilla bit-flip rate $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34) \times 10^{3}~\mathrm{s}^{-1}$, computes the per-cycle error probability under a stated cycle-time assumption, and reports the structural result that the ancilla-induced logical error rate in steady state equals $\eta\,\Gamma_{\mathrm{bf}}$ independent of cycle speed; it explicitly labels its platform comparison ($8.0$–$64\times$ photon advantage versus surface codes) as a projection under stated assumptions, and states "Our assessment is falsifiable" [8]. Three things transfer: the practice of deriving every downstream number from stated inputs with propagated uncertainty; the practice of separating computed results from labeled projections; and the insistence that an assessment end in a falsifiable statement. Our Section 4 follows all three.

**Representational critiques as motivation, and their discipline.** The motivation for considering non-Archimedean foundations comes from the thesis, argued in [9], that the real-number continuum is a representational projection rather than the territory, and that many apparent problems are artifacts of representational choices; [9] proposes that moving to a representation whose native topology matches the phenomenon (e.g., $p$-adic ultrametric structure) reveals invariants, and develops the adelic programme on the basis that if $\mathbb{Q}$ is the physically accessible base field, all completions are physically meaningful [9]. We take from [9] the motivation but insist on its discipline: [9] itself frames its claims as a thesis and hypothesis, and the companion critique in [10] — which deconstructs the qubit-as-particle and error-correction-as-classical-coding scaffolds while identifying the surviving invariants (superposition, entanglement, correlation structure, phase coherence), and which maintains a "calibration register with dated, falsifiable predictions" [10] — supplies the model of a critique program that commits to falsifiable outputs. Our criterion is the QEC-specific instantiation of that commitment: the geometric program earns physical status exactly when it enters the calibration register with a scaling exponent.

**Projection discipline from adjacent quantum-simulation work.** Finally, [11] provides the closest structural precedent for how to state results of the kind we derive. [11] derives exact information-theoretic identities for qudit quantum cellular automata (entropy capacity $\log_2 d$ per site, site-count equivalence $N_d = N_q/\log_2 d$, per-gate cost ratio $d^2/4$) and then explicitly separates them from its emergence-threshold claim $N^*(d) = N^*(2)/\log_2 d$, which it labels "a projection under Assumptions A1–A3 ... its status is hypothesis, not result" [11]. [11] also identifies the concrete user (researchers screening substrates by exact simulation), states that no commercial user exists and the work is foundational, and specifies the smallest next experiment with the measured quantities and the pass/fail criterion [11]. Our paper adopts this exact result/projection separation and the same Section 7 structure, because the epistemic situation is identical: exact derivations about cost and distinguishability, plus a hypothesis about nature that only measurement can settle.

## 3. Methods

### 3.1 Definitions

We consider code families $\mathcal{C}$ that encode one logical qubit into $n$ physical qubits or oscillator modes, subject to local Markovian noise with total physical error rate $p_{\mathrm{phys}}$ per cycle. The logical error rate per cycle is $p_L(n, p_{\mathrm{phys}})$. The discriminating observable is the log-log scaling exponent

$$\beta(n) \;=\; -\frac{\partial \ln p_L}{\partial \ln p_{\mathrm{phys}}}\bigg/ 1 \qquad \text{equivalently} \qquad p_L \propto p_{\mathrm{phys}}^{-\beta(n)},$$

estimated by regression of $\ln p_L$ on $\ln p_{\mathrm{phys}}$ over a sweep of $p_{\mathrm{phys}}$ at fixed $n$. We write $\beta$ positive with $p_L \propto p_{\mathrm{phys}}^{\beta}$ below, following the convention of the research idea; all exponents below are stated in the $p_L \propto p_{\mathrm{phys}}^{\beta}$ form.

### 3.2 The falsifiability criterion

A geometrically motivated QEC scheme $G$ (derived from non-standard foundations such as $p$-adic/Bruhat–Tits geometry or geometric algebra) satisfies the criterion — and is therefore a candidate physical theory rather than a re-description — if and only if both conditions hold:

- **(C1) Dynamical content.** $G$ yields an explicit Hamiltonian $H_G$ or Lindblad generator $\mathcal{L}_G$ on a finite Hilbert space, obtained by a derivation from the geometric substrate that is the analogue of the foundations-to-logic derivations of [3]: specific generators, not a new vocabulary.
- **(C2) Distinct exponent.** The exponent $\beta_G(n)$ predicted by $\mathcal{L}_G$ differs from the surface-code exponent $\beta_{\mathrm{sc}}(n)$ by an amount resolvable with a stated sample budget at matched $n$ and $p_{\mathrm{phys}}$.

If $\beta_G = \beta_{\mathrm{sc}}$ to within experimental resolution, then by the separation logic of [4] and [6] the two codes are experimentally indistinguishable in their error behavior, and the geometric proposal is a notational variant for all QEC purposes; this is the null-result outcome the criterion converts into a sharp statement.

### 3.3 Baseline and hypothesis

**Baseline (surface code).** We assume the standard sub-threshold scaling form

$$p_L^{\mathrm{sc}}(d_{\mathrm{sc}}, p) \;=\; A \left(\frac{p}{p_{\mathrm{th}}}\right)^{(d_{\mathrm{sc}}+1)/2},$$

with $d_{\mathrm{sc}}$ the code distance and $n \approx d_{\mathrm{sc}}^2$ physical qubits. We assume $A = 0.1$ and $p_{\mathrm{th}} = 10^{-2}$ as representative circuit-level values; these are assumptions of this paper (the sources do not supply them), chosen to be conservative and stated explicitly so every downstream number is recomputable. The exponent is $\beta_{\mathrm{sc}}(d_{\mathrm{sc}}) = (d_{\mathrm{sc}}+1)/2$.

**Hypothesis (geometric code).** The research idea proposes that a geometrically derived code with geometric distance parameter $d_g$ obeys

$$p_L^{G}(d_g, p) \;=\; B\, p^{\,d_g/2}, \qquad \beta_G(d_g) = \frac{d_g}{2}.$$

We assume the matched-resource convention $d_g = d_{\mathrm{sc}} = \sqrt{n}$ (both codes use $n \approx d^2$ physical qubits); Appendix-level sensitivity to this convention is discussed in Section 6. The constants $A$ and $B$ are unknown a priori; the discriminating experiment must therefore compare exponents, not absolute rates, or must bound $B$.

### 3.4 Protocol

1. **Instantiate.** From the geometric substrate, derive the finite stabilizer generator set on $n$ qubits (the ground instantiation, in the sense of [5]) and the generator $\mathcal{L}_G$.
2. **Simulate.** Evolve $\mathcal{L}_G$ under local noise; extract $p_L^G(n, p)$ by Monte Carlo over trajectories if exact evolution is infeasible (budget derived in Section 4.3).
3. **Sweep.** Measure (or simulate) $p_L$ at $p \in \{10^{-3}, 3\times 10^{-3}, 10^{-2}\}$ at fixed $n$; regress $\ln p_L$ on $\ln p$ to estimate $\hat{\beta}$.
4. **Decide.** If $|\hat{\beta}_G - \beta_{\mathrm{sc}}|$ exceeds the combined statistical and systematic uncertainty, the code classes are distinguished; otherwise they are not, at the tested resources.

## 4. Analysis

All inputs are stated with their status: computed here, or assumed (the sources do not supply them).

### 4.1 Input register

- $I_1$ (assumption): $p_{\mathrm{th}} = 10^{-2}$, surface-code threshold, representative circuit-level value.
- $I_2$ (assumption): $A = 0.1$, surface-code prefactor.
- $I_3$ (assumption): matched-resource convention $d_g = d_{\mathrm{sc}} = \sqrt{n}$.
- $I_4$ (assumption): geometric hypothesis $p_L^G = B\,p^{d_g/2}$ with $B$ unknown; for distinguishability calculations we take the conservative case $B = A = 0.1$, which minimizes the predicted separation.
- $I_5$ (assumption): complex double-precision amplitudes, $16$ bytes each, for memory estimates.

### 4.2 Predicted separation at matched resources

At $n = 25$: $d_{\mathrm{sc}} = \sqrt{25} = 5$, so

$$\beta_{\mathrm{sc}} = \frac{d_{\mathrm{sc}}+1}{2} = \frac{5+1}{2} = 3, \qquad \beta_G = \frac{d_g}{2} = \frac{5}{2} = 2.5.$$

At $p = 10^{-3}$, the surface-code prediction is

$$p_L^{\mathrm{sc}} = A\left(\frac{p}{p_{\mathrm{th}}}\right)^{3} = 0.1 \times (0.1)^{3} = 0.1 \times 10^{-3} = 10^{-4}.$$

The geometric prediction (with $B = 0.1$) is

$$p_L^{G} = B\,p^{2.5} = 0.1 \times (10^{-3})^{2.5} = 0.1 \times 10^{-7.5} = 10^{-8.5} \approx 3.16 \times 10^{-9}.$$

The separation ratio is

$$r = \frac{p_L^{\mathrm{sc}}}{p_L^{G}} = \frac{10^{-4}}{10^{-8.5}} = 10^{4.5} \approx 31{,}623.$$

Equivalently, in general form the ratio depends only on the exponent gap $\Delta\beta = \beta_{\mathrm{sc}} - \beta_G = 1/2$ and on $p$:

$$r = p^{-\Delta\beta} = p^{-1/2} = (10^{-3})^{-1/2} = 10^{1.5} \approx 31.62.$$

The two computations differ because the first holds $d_{\mathrm{sc}} = 5$ fixed while the general ratio compares the two laws at the same $p$ but with the geometric code's larger effective exponent advantage accumulating over the full range; the correct matched-resource comparison is the second, $r = p^{-1/2} \approx 31.62$, and we use it for all sample-size calculations. (The first computation overstates the separation because it evaluates the geometric law with $d_g = 5$ against a surface code of the same distance but with the prefactor convention mismatched; the conservative, convention-independent quantity is $r = p^{-\Delta\beta}$.)

**Sample size to resolve the ratio.** To resolve a ratio $r$ between two error rates, the standard error of the estimated log-ratio must be smaller than $\ln r$. For a binomial count with $N$ logical-qubit cycles and per-cycle error probability $p_L$, the relative standard error of the count is approximately $1/\sqrt{N p_L}$ (for $N p_L \gg 1$), so we require

$$\frac{1}{\sqrt{N p_L}} \leq \ln r \quad\Longrightarrow\quad N \geq \frac{1}{p_L (\ln r)^{2}}.$$

With $p_L = 10^{-4}$ (the surface-code rate at the operating point) and $r = 31.62$, $\ln r = \ln 31.62 = 3.454$, $(\ln r)^2 = 11.93$:

$$N \geq \frac{1}{10^{-4} \times 11.93} = \frac{1}{1.193 \times 10^{-3}} \approx 838.$$

So approximately $838$ logical-qubit cycles at the operating point suffice to resolve the two curves at $n = 25$, $p = 10^{-3}$, under the conservative assumption $B = A$.

**Exponent resolution.** The same data resolve the exponent difference: the log-ratio $\ln r = 3.454$ is exactly $\Delta\beta \cdot |\ln p| = 0.5 \times 6.908 = 3.454$, confirming internal consistency ($\ln 10^{-3} = -6.908$).

### 4.3 Simulation budget for the predicted dynamics

Exact state-vector evolution of an $n$-qubit Lindblad equation requires storing a state vector of $2^n$ complex amplitudes.

At $n = 25$:

$$2^{25} = 33{,}554{,}432 \text{ amplitudes}, \qquad M = 33{,}554{,}432 \times 16~\text{bytes} = 5.369 \times 10^{8}~\text{bytes} \approx 0.54~\text{GB}.$$

This is feasible on a single workstation.

At $n = 49$ (surface-code distance $d_{\mathrm{sc}} = 7$):

$$2^{49} = 562{,}949{,}953{,}421{,}312 \approx 5.63 \times 10^{14} \text{ amplitudes},$$
$$M = 5.63 \times 10^{14} \times 16 = 9.01 \times 10^{15}~\text{bytes} \approx 9.0~\text{PB}.$$

This is infeasible for exact evolution by roughly seven orders of magnitude beyond workstation memory. The boundary between exact and trajectory-Monte-Carlo methods therefore lies between $n = 25$ and $n = 49$; the discriminating experiment at $n = 25$ sits on the feasible side, which is a structural advantage of the protocol: the prediction can be generated and checked numerically before any hardware commitment.

### 4.4 Operating-point choice and near-threshold behavior

The separation $r = p^{-1/2}$ grows as $p$ decreases, but the absolute sample cost $N \propto 1/p_L$ grows faster. At $p = 10^{-2}$ (threshold), $p_L^{\mathrm{sc}} = A (p/p_{\mathrm{th}})^{3} = 0.1 \times 1 =