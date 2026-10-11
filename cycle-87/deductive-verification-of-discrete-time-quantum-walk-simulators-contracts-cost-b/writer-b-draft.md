# Deductive Verification of Discrete-Time Quantum-Walk Simulators: Contracts, Cost Bounds, and a Finite-Distinction Extension

## Abstract

Discrete-time quantum walks are a universal model of quantum computation and a standard testbed for quantum algorithms, yet the simulators used to study them are rarely verified with the same rigor applied to classical library code. We propose a contract-based deductive verification methodology for quantum-walk simulators, in which each simulation step carries explicit preconditions and postconditions encoding unitarity, probability conservation, and support bounds. We derive the exact state-space size of the one-dimensional Hadamard walk after $t$ steps, $N_t = 2(2t+1)$, and compute the exact arithmetic cost of a naive direct simulation: for $t = 1000$ steps the total real multiplication count is $8{,}024{,}000$. We further derive the number of contract clauses required for step-wise verification, $5t$ for a minimal contract, giving $5{,}000$ clauses at $t = 1000$, and we show that the per-step verification obligation is constant while the aggregate obligation grows linearly in $t$. As an extension, we connect the verified simulator to a finite-distinction reading of quantum mechanics, in which state spaces are combinatorial and ultrametric rather than continuum-valued, and we argue that verified integer-indexed amplitude bookkeeping is the natural artifact of such a reading. All numerical results in this paper are derived with explicit arithmetic from stated inputs; no empirical measurements are reported, and all scaling claims beyond the computed instances are labeled projections with stated assumptions.

## 1. Introduction

Quantum walks are the quantum mechanical counterparts of classical random walks and have become both an algorithmic tool and a universal computational model [3], [8]. A discrete-time quantum walk evolves a single quantum particle on a graph by alternating a local unitary "coin" operation with a conditional shift; despite this simplicity, the resulting dynamics exhibit rich structure, including topological phenomena in one and two dimensions [1], order-from-chaos effects on cyclic graphs [4], and analytically tractable limit distributions [5].

The simulators that produce these results are, however, ordinary programs. As quantum-walk research grows, so does the risk that a published distribution, a claimed periodicity, or a reported topological invariant rests on an unverified implementation artifact: an off-by-one in the shift, a coin matrix whose normalization has drifted, a boundary condition that silently absorbs probability. Classical software engineering has developed a mature answer to this class of risk in the form of deductive verification, in which a program is accompanied by formal preconditions and postconditions and a proof that the code satisfies them. A recent benchmark of this approach verified unmodified Linux kernel library functions: formal contracts were extracted from source code as preconditions and postconditions, and the correctness of 23 of 26 functions was completed within the benchmark's effort budget [7]. That result demonstrates that contract-based verification of real, unmodified code is practical at meaningful scale.

This paper makes three contributions. First, we specify a contract-based verification methodology for discrete-time quantum-walk simulators, identifying the invariants that a correct walker must maintain (unitarity of the step, conservation of total probability, and a support bound that grows linearly in the step count). Second, we derive exact quantitative cost figures for both simulation and verification on the canonical one-dimensional Hadamard walk, with all arithmetic shown. Third, we propose an extension motivated by the finite-distinction program in quantum foundations, which holds that a finite-entropy world is a world of finite distinctions, that uncountable precision is unphysical, and that the geometry of finite distinctions is combinatorial and ultrametric [9]. Under that reading, a verified simulator whose amplitudes are tracked as explicit, finitely many, integer-indexed quantities is not merely an approximation to a continuum theory but a candidate for the physically meaningful object itself.

The paper is organized as follows. Section 2 reviews the related literature. Section 3 specifies the model and the verification methodology. Section 4 carries out the derivations with full arithmetic. Section 5 states the results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 concludes.

## 2. Background and Related Work

We discuss the supplied bibliography in its given order. Throughout, "quantum walk" means the discrete-time or continuous-time quantum analogue of a classical random walk; "coin" means the internal unitary acting on the walker's internal degree of freedom; "support" means the set of graph positions with nonzero amplitude.

**Topological phases in quantum walks.** The review of topological phenomena in quantum walks [1] presents discrete quantum walks as dynamical protocols for controlling a single quantum particle and argues that, despite their simplicity, they display rich topological phenomena and constitute one of the simplest systems in which to study and understand topological phases, with an elementary treatment of one and two dimensions. For verification purposes this matters because topological invariants are exactly the kind of quantity that a buggy simulator can corrupt silently: an invariant computed from a wrong dispersion relation may still look "quantum." Our contracts therefore include the support and normalization invariants that any downstream invariant computation presupposes.

**Discrete-event simulation.** The discrete-event simulation study [2] simulates two models of experimentally realizable quantum walks on a digital computer using models that comply with Einstein locality, in which particles follow well-defined trajectories, avoid concepts such as particle-wave duality and wave-function collapse, and reproduce the quantum-theoretical results (the supplied summary is truncated at this point, so we do not attribute further specific findings to it). This work is directly relevant to our extension: it demonstrates that trajectory-based, locally causal simulation can reproduce quantum-walk statistics, which is precisely the situation in which a reader might ask whether the simulator or the theory is being tested. Contract-based verification answers a complementary question: whether the simulator implements the intended model at all.

**Comprehensive review.** The comprehensive review of quantum walks [3] describes quantum walks as the quantum mechanical counterpart of classical random walks, an advanced tool for building quantum algorithms, and states that quantum walks have been shown to constitute a universal model of quantum computation, and that the field is now solid, with open problems for physicists, computer scientists, mathematicians, and engineers (the summary is truncated, so further specifics of its coverage are not attributed here). Universality raises the stakes of verification: if quantum walks are a universal computational model, then a verified quantum-walk simulator is a verified simulator for a universal family of computations, and simulator bugs propagate to every algorithm studied through it.

**Order from chaos on cyclic graphs.** The study of cyclic quantum walks [4] starts from the classical result that combining two chaotic random walks can yield an ordered (periodic) walk, and seeks a quantum analog; it studies chaotic and periodic behavior of cyclic quantum walks and focuses on a situation in which a periodic quantum walk on a 3-cycle graph is generated via a deterministic combination of two chaotic ones (the summary is truncated beyond this). Periodicity claims are a canonical target for verification: a periodicity statement is a sharp, decidable property of the implemented update rule, and our postcondition scheme can express it as an equality between the state at step $t$ and the state at step $t + T$ for the claimed period $T$.

**Limit distributions.** The review of limit theorems [5] analytically shows the weak limit theorem, i.e., the asymptotic behavior, of the one-dimensional discrete-time quantum walk, and discusses the relation between the limit distribution of the discrete-time walk and the continuous-time walk (the summary is truncated at this point). Limit theorems give the reference distributions against which finite-$t$ simulations are checked; a verified simulator is a prerequisite for trusting that an observed convergence to the limit distribution is a property of the walk rather than of the code.

**Noise and symmetries.** The study of symmetries and noise [6] examines discrete symmetries of unbiased (Hadamard) and biased quantum walks on a line and shows that these symmetries hold even when the walker is subjected to environmental effects, using noise models of phase flip, bit flip, and generalized amplitude damping channels, with numerical solutions obtained by evolving the density matrix (the summary is truncated beyond this). This is the natural bridge from verified unitary simulators to verified open-system simulators: the density-matrix evolution loop has the same contract structure (trace conservation replaces probability conservation), and the noise channels named in [6] are exactly the operations whose contract clauses one would write first.

**Deductive verification of systems code.** The deductive verification benchmark [7] consists of 26 unmodified Linux kernel library functions implementing conventional memory and string operations; the formal contracts were extracted from the functions' source code and represented as preconditions and postconditions, and the correctness of 23 functions was completed (the summary is truncated at this point, so we do not attribute further details of the verification tooling or effort accounting). We use this work as the methodological template: contracts extracted from the code as written, applied to unmodified functions, with a partial but high completion rate. Our proposal transfers this template from memory-and-string operations to unitary update loops.

**Algorithmic applications.** The overview of algorithmic applications [8] characterizes quantum walks as quantum counterparts of Markov chains and gives a brief overview with emphasis on their algorithmic applications (the summary is short, and we attribute nothing further to it). It supplies the motivation from the consumer side: every algorithmic application downstream of a walk simulation inherits the simulator's correctness.

**Finite-distinction quantum mechanics.** The QNFO program [9] argues that a finite-entropy world is a finite-distinction world, that uncountable precision is unphysical while computable depth and $p$-adic valuation remain physically real, and that the state-space geometry of finite distinctions is combinatorial and ultrametric, with quantum mechanics read as thermodynamics (the summary is truncated mid-sentence). We use only what the summary states: the finiteness thesis, the combinatorial-ultrametric geometry claim, and the thermodynamic reading. Our extension in Section 3.3 connects verified integer-indexed amplitude bookkeeping to this program.

**Remaining entries.** The entry on factoring, adelic complexity, and the silent-radix principle [10] has an empty supplied summary; we therefore make no claim about its content and cite it only as part of the same corpus context as [9] and [11]. The Manifesto for Honest Computation [11] supplies, per its summary, five principles, a concrete portfolio, and a Falsification Pledge; we adopt its falsification stance methodologically (Section 6 states explicit falsification conditions) without attributing specific principles beyond what the summary names. The ZBW-Majorana hypothesis entry [12] establishes, per its summary and across four companion papers (P1–P4), that Zitterbewegung — the rapid trembling motion of Dirac fermions at the Compton scale — is a $\mathbb{Z}_2$ topological observable distinguishing Dirac from Majorana fermions at the hardware level (summary truncated). We cite it as an example of a topological observable claimed to be hardware-level, analogous in spirit to the topological observables of quantum walks [1], but we derive nothing from it.

## 3. Methods

### 3.1 Model

We consider the standard one-dimensional discrete-time Hadamard walk. The Hilbert space is $\mathcal{H}_p \otimes \mathcal{H}_c$, where $\mathcal{H}_p = \mathrm{span}\{|x\rangle : x \in \mathbb{Z}\}$ is the position space and $\mathcal{H}_c = \mathrm{span}\{|0\rangle, |1\rangle\}$ is the two-dimensional coin space. The state at step $t$ is

$$|\psi_t\rangle = \sum_{x \in \mathbb{Z}} \left( \alpha_{x,0}^{(t)} |x,0\rangle + \alpha_{x,1}^{(t)} |x,1\rangle \right),$$

with the normalization $\sum_{x} \left( |\alpha_{x,0}^{(t)}|^2 + |\alpha_{x,1}^{(t)}|^2 \right) = 1$. One step is

$$|\psi_{t+1}\rangle = \hat{S} \left( \hat{I} \otimes \hat{C} \right) |\psi_t\rangle,$$

where $\hat{C}$ is the Hadamard coin

$$\hat{C} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix},$$

and $\hat{S}$ is the conditional shift $\hat{S}|x,0\rangle = |x-1,0\rangle$, $\hat{S}|x,1\rangle = |x+1,1\rangle$. The walk starts at $x = 0$ with coin state $|0\rangle$: $\alpha_{0,0}^{(0)} = 1$, all other amplitudes zero.

### 3.2 Contract-based verification methodology

Following the template of contract extraction from unmodified source code [7], we attach to each simulator function a contract of preconditions and postconditions. For the step function $\texttt{step}(\psi_t) \to \psi_{t+1}$ we require:

- **P1 (input normalization):** $\sum_{x} \left( |\alpha_{x,0}^{(t)}|^2 + |\alpha_{x,1}^{(t)}|^2 \right) = 1$ within tolerance $\varepsilon$.
- **P2 (input support):** $\alpha_{x,c}^{(t)} = 0$ for all $|x| > t$ and $c \in \{0,1\}$.
- **Q1 (output normalization):** $\sum_{x} \left( |\alpha_{x,0}^{(t+1)}|^2 + |\alpha_{x,1}^{(t+1)}|^2 \right) = 1$ within tolerance $\varepsilon$.
- **Q2 (output support):** $\alpha_{x,c}^{(t+1)} = 0$ for all $|x| > t+1$.
- **Q3 (coin correctness):** the coin applied at each site equals $\hat{C}$ up to the declared floating-point tolerance.

Clauses Q1 and Q3 follow from unitarity of the step operator $\hat{U} = \hat{S}(\hat{I} \otimes \hat{C})$: since $\hat{C}^{\dagger}\hat{C} = \hat{I}$ and $\hat{S}^{\dagger}\hat{S} = \hat{I}$, we have $\hat{U}^{\dagger}\hat{U} = \hat{I}$, so $\langle \psi_{t+1} | \psi_{t+1} \rangle = \langle \psi_t | \psi_t \rangle$. Clause Q2 follows because one step moves each amplitude by at most one position. Each clause is a decidable predicate over the simulator's data structures, checkable by an SMT-backed verifier of the kind used in the benchmark of [7].

### 3.3 Finite-distinction extension

The finite-distinction program [9] holds that uncountable precision is unphysical and that finite-distinction state spaces are combinatorial and ultrametric. We operationalize this for the walk simulator as follows: the verified artifact is a finite map from integer pairs $(x, c)$ with $|x| \leq t$ and $c \in \{0,1\}$ to amplitude records, i.e., exactly $N_t = 2(2t+1)$ records at step $t$ (derived in Section 4). No continuum object appears in the verified artifact; the continuum wave function is a derived, large-distinction description in the sense of [9]. Under this reading, the verification obligation is finite and explicit at every $t$, which is the practical content of the finiteness thesis for simulation. We stress that this is a methodological alignment, not a derivation of quantum mechanics from [9]; the summary of [9] supports the finiteness and geometry claims we invoke and nothing more.

## 4. Analysis

Every input number below is either a definition of the model (Section 3.1), a structural fact derived from it, or an explicitly labeled projection.

**Input 1 (model definition, Section 3.1):** the coin has dimension $d_c = 2$; the walk runs on $\mathbb{Z}$; the initial position is $x_0 = 0$.

**Derivation 1 (state-space size).** After $t$ steps, each step moves the walker by exactly one position, so the support is contained in $\{-t, \ldots, t\}$, which has $2t + 1$ positions. Each position carries $d_c = 2$ coin components. Hence

$$N_t = d_c (2t + 1) = 2(2t+1).$$

For $t = 1000$: $2t + 1 = 2001$, so $N_{1000} = 2 \times 2001 = 4002$ amplitude records. For $t = 10^6$: $2t+1 = 2{,}000{,}001$, so $N_{10^6} = 4{,}000{,}002$ records.

**Input 2 (coin definition, Section 3.1):** $\hat{C} = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$; its entries have magnitude $2^{-1/2}$.

**Derivation 2 (arithmetic cost per site per step).** Applying $\hat{C}$ at one site computes two output amplitudes, each a sum of two products with the scalar $2^{-1/2}$:

$$\beta_0 = 2^{-1/2}(\alpha_0 + \alpha_1), \qquad \beta_1 = 2^{-1/2}(\alpha_0 - \alpha_1).$$

Each product of a complex amplitude by the real scalar $2^{-1/2}$ costs $2$ real multiplications (real and imaginary parts). There are $2$ output amplitudes $\times\, 2$ input terms each $= 4$ such products, hence $4 \times 2 = 8$ real multiplications per site per step. The shift itself is a data movement and costs no multiplications.

**Derivation 3 (total multiplication count for $t = 1000$).** At step $s$ (for $1 \leq s \leq t$), the number of occupied sites is at most $2s + 1$ (the support after $s-1$ steps has at most $2(s-1)+1$ sites, and one step spreads it by at most one on each side; we count the worst case $2s+1$ sites touched at step $s$). The total real multiplication count is

$$M_t = \sum_{s=1}^{t} 8(2s+1) = 16\sum_{s=1}^{t} s + 8t = 16 \cdot \frac{t(t+1)}{2} + 8t = 8t^2 + 16t = 8t(t+2).$$

Check of the closed form: $\sum_{s=1}^{t}(2s+1) = 2 \cdot \frac{t(t+1)}{2} + t = t^2 + 2t = t(t+2)$; multiplying by $8$ gives $M_t = 8t(t+2)$. For $t = 1000$:

$$M_{1000} = 8 \times 1000 \times 1002 = 8{,}000{,}000 + 24{,}000 = 8{,}024{,}000.$$

For $t = 100$: $M_{100} = 8 \times 100 \times 102 = 81{,}600$.

**Derivation 4 (verification cost per step).** Evaluating clause P1 or Q1 requires computing $\sum_{x} (|\alpha_{x,0}|^2 + |\alpha_{x,1}|^2)$ over $N_t$ records; each term costs $2$ real multiplications ($|\alpha|^2$ for a complex number), so the check costs $2 N_t$ real multiplications plus $N_t$ additions. Clauses P2 and Q2 cost $O(N_t)$ comparisons with no multiplications. Clause Q3 costs a constant number of comparisons against the stored coin matrix, independent of $t$. Thus the per-step verification cost is dominated by the two normalization checks: $2 \times 2 N_t = 4 N_t$ real multiplications. At $t = 1000$: $4 N_{1000} = 4 \times 4002 = 16{,}008$ real multiplications per step for verification, versus $8 N_{1000} = 8 \times 4002 = 32{,}016$ real multiplications per step for the simulation itself; the verification overhead ratio is

$$\frac{4 N_t}{8 N_t} = \frac{1}{2},$$

i.e., normalization checking adds $50\%$ multiplication overhead per step, independent of $t$.

**Derivation 5 (contract clause count).** The minimal contract of Section 3.2 has $2$ preconditions (P1, P2) and $3$ postconditions (Q1, Q2, Q3), i.e., $5$ clauses per step-function instance. For a $t$-step run verified step by step, the aggregate clause count is

$$K_t = 5t.$$

For $t = 1000$: $K_{1000} = 5 \times 1000 = 5{,}000$ clauses. For $t = 100$: $K_{100} = 500$ clauses. If instead the verifier discharges the step lemma once (proving that one step maps a normalized, $t$-supported state to a normalized, $(t+1)$-supported state) and then applies it $t$ times by induction, the aggregate obligation drops to $O(1)$ lemmas plus $t$ induction applications; we treat the $5t$ figure as the upper bound for the naive per-step scheme and the inductive scheme as the projected lower bound, with the constant (one lemma of $5$ clauses) independent of $t$.

**Derivation 6 (probability-conservation tolerance budget).** Suppose each amplitude is stored with a relative rounding error bounded by $\eta$ per step, and suppose (as a worst-case linear-accumulation model, explicitly a projection) that the normalization error after $t$ steps is bounded by $t \eta$. To guarantee the Q1 check passes with tolerance $\varepsilon = 10^{-9}$ after $t = 1000$ steps, we need $t\eta \leq \varepsilon$, i.e.,

$$\eta \leq \frac{\varepsilon}{t} = \frac{10^{-9}}{1000} = 10^{-12}.$$

This is a projection under the stated linear-accumulation assumption; under random-walk error accumulation ($\sqrt{t}\,\eta$ scaling) the bound would relax to $\eta \leq \varepsilon / \sqrt{t} = 10^{-9}/\sqrt{1000} \approx 3.16 \times 10^{-11}$, since $\sqrt{1000} \approx 31.62$ and $10^{-9}/31.62 \approx 3.16 \times 10^{-11}$. We report both bounds and flag which assumption each rests on.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; the two tolerance figures in Derivation 6 are projections under explicitly stated accumulation models.

- **R1 (exact state-space size).** The one-dimensional Hadamard walk after $t$ steps occupies exactly $N_t = 2(2t+1)$ amplitude records in the worst case; $N_{1000} = 4002$ and $N_{10^6} = 4{,}000{,}002$.
- **R2 (exact simulation cost).** The total real multiplication count of naive direct simulation for $t$ steps is $M_t = 8t(t+2)$; $M_{100} = 81{,}600$ and $M_{1000} = 8{,}024{,}000$.
- **R3 (verification overhead).** Normalization checking (clauses P1, Q1) costs $4N_t$ real multiplications per step, exactly $50\%$ of the simulation's $8N_t$ per-step multiplication cost, independent of $t$.
- **R4 (contract size).** The minimal per-step contract has $5$ clauses; the naive step-by-step scheme requires $K_t = 5t$ clauses ($K_{100} = 500$, $K_{1000} = 5{,}000$), while the inductive scheme requires a single $5$-clause lemma plus $t$ applications (projection: constant lemma cost, linear application cost, no multiplicative blow-up).
- **R5 (tolerance budget, projection).** Under linear error accumulation, storing amplitudes with per-step relative error $\eta \leq 10^{-12}$ suffices to pass a $10^{-9}$ normalization tolerance at $t = 1000$; under $\sqrt{t}$ accumulation, $\eta \leq 3.16 \times 10^{-11}$ suffices. Both figures assume the stated accumulation models and no systematic (bias) component in the rounding error.

No empirical measurements, benchmark timings, or solver success rates are reported in this paper; those require an implementation and are future work.

## 6. Discussion

**Limitations.** First, the cost model counts real multiplications only and ignores additions, memory movement, and sparse-structure overhead; the true runtime gap between verified and unverified simulation may differ from the $50\%$ multiplication-overhead figure of R3, which is exact only for the multiplication count. Second, the $M_t = 8t(t+2)$ figure assumes the worst-case support $2s+1$ sites at every step $s$; for the Hadamard walk with nonzero coin mixing the support is indeed the full $\{-s,\ldots,s\}$ after $s$ steps, but for coins that block propagation (e.g., a coin that leaves one coin state invariant) the occupied set could be smaller, and $M_t$ would then be an overestimate. Third, the tolerance analysis of R5 is a projection under two idealized accumulation models; real floating-point error in a unitary loop can exhibit cancellation or drift outside both models, and only an implemented, measured study can settle it. Fourth, we have specified contracts but not discharged them with a verifier; the benchmark of [7] completed 23 of 26 functions, which is evidence that partial completion is the realistic outcome, and our clause counts (R4) say nothing about solver effort per clause, which is typically the binding resource.

**Failure modes.** The contract scheme as specified does not catch all plausible bugs: a simulator that applies the coin with the wrong sign convention on $|1\rangle$ still preserves normalization and support (Q1, Q2, P1, P2 all pass); only Q3 catches it, and Q3 checks the coin against a stored reference, which itself must be verified. Similarly, a shift implemented as $\hat{S}|x,0\rangle = |x+1,0\rangle$ (direction flipped) passes every normalization and support clause; it would be caught only by a stronger postcondition fixing the full step map, whose clause count grows with $N_t$ and would change R4. This is a genuine gap: our minimal contract verifies conservation structure, not the direction of dynamics.

**What would falsify the claims.** R1–R4 are exact consequences of the model definitions in Section 3.1 and would be falsified only by an error in the derivations (each is one line of arithmetic and can be checked directly). R5 would be falsified by an implemented experiment in which the normalization error at $t = 1000$ exceeds $10^{-9}$ despite per-step rounding at or below the stated $\eta$ bounds, which would refute the accumulation models. The methodological claim — that contract-based verification of quantum-walk simulators is practical — would be falsified if a step-function contract of the R4 size routinely failed to verify within reasonable effort, in contrast to the high completion rate observed for classical library functions in [7].

**Open questions.** (i) What is the minimal contract that pins down the step map exactly, and what is its clause count as a function of $N_t$? (ii) Do the symmetry properties of the noisy walk studied in [6] admit contract formulations (e.g., symmetry of the density-matrix evolution as a postcondition), and at what verification cost? (iii) Can periodicity claims of the kind studied on cyclic graphs in [4] be verified by SMT directly, i.e., is the equality $\psi_{t+T} = \psi_t$ over floating-point amplitudes decidable in practice, or must it be verified over exact symbolic amplitudes? (iv) Under the finite-distinction reading of [9], is there a natural ultrametric tolerance structure that replaces the ad hoc $\varepsilon$ of our normalization clauses — the corpus context of [10] and [11] suggests such a program exists, but the supplied summaries do not state its technical content, so we leave this as a question rather than a claim.

## 7. Conclusion

We have specified a contract-based deductive verification methodology for discrete-time quantum-walk simulators, derived exact state-space sizes ($N_t = 2(2t+1)$), exact simulation costs ($M_t = 8t(t+2)$, giving $8{,}024{,}000$ real multiplications at $t = 1000$), an exact $50\%$ multiplication overhead for normalization checking, and exact contract sizes ($5t$ clauses for the naive scheme). The methodology transfers a template proven on classical systems code to the quantum-simulation setting, and aligns naturally with the finite-distinction view in which the verified artifact — a finite map of integer-indexed amplitude records — is the physically meaningful object. The immediate next step is an implementation: discharge the $5$-clause step contract with an existing verifier, measure solver effort, and test the tolerance projections of R5 empirically.

## References

[1] arXiv:1112.1882v1 | Topological phenomena in quantum walks; elementary introduction to the physics of topological phases
[2] arXiv:2005.03401v1 | Discrete-event simulation of quantum walks
[3] arXiv:1201.4780v2 | Quantum walks: a comprehensive review
[4] arXiv:2008.00316v3 | Order from chaos in quantum walks on cyclic graphs
[5] arXiv:1307.3384v1 | From Discrete Time Quantum Walk to Continuous Time Quantum Walk in Limit Distribution
[6] arXiv:quant-ph/0607188v3 | Symmetries and noise in quantum walk
[7] arXiv:1809.00626v1 | Deductive Verification of Unmodified Linux Kernel Library Functions
[8] arXiv:quant-ph/0403120v3 | Quantum walks and their algorithmic applications
[9] QNFO: Finite-Distinction Quantum Mechanics: Unitary Evolution and Superposition as the Large-Distinction Limit of Stochastic Thermodynamics
[10] QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle
[11] QNFO: Manifesto for Honest Computation
[12] QNFO: Vanishing ZBW Signal: The ZBW-Majorana Hypothesis as a Unified Framework for Topological Fermion Distinction