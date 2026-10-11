# Deductive Verification and Topological Invariant Checking for Discrete-Time Quantum Walks: A Computational Cost Analysis

## Abstract

Discrete-time quantum walks are simultaneously a physical protocol, a universal model of quantum computation, and a rich platform for topological phases, which makes them a natural target for formal verification: a walk simulator is a unitary dynamical system whose correctness constraints (unitarity, probability conservation, support bounds, topological invariants) are mathematically explicit. We frame the verification of quantum-walk simulators as a contract-checking problem in the style of deductive verification of library functions, and we analyze the computational cost of the core check — verifying $U^{\dagger}U = I$ for the one-step evolution operator $U$ — in dense and sparse representations. For a Hadamard walk evolved for $t = 10^{3}$ steps, the dense check costs $d^{3} \approx 6.41 \times 10^{10}$ multiply-adds on a state space of dimension $d = 4002$, while exploiting the walk's sparsity (two nonzero entries per row) reduces this to $8d = 32{,}016$ multiply-adds, a speedup factor of $\approx 2.0 \times 10^{6}$. We further derive a floating-point drift bound for probability conservation over $t = 10^{6}$ steps and a discretization error bound for numerical winding-number extraction, showing that a $64$-point Brillouin-zone grid with per-point phase error $10^{-3}$ rad resolves the integer invariant with margin factor $\approx 49$ below the rounding threshold. We connect these checks to topological phenomena in quantum walks and to a thermodynamic reading of quantum mechanics, and we state explicit falsification conditions.

## 1. Introduction

A discrete-time quantum walk is a dynamical protocol for controlling a single quantum particle on a graph: at each step, a coin operation acts on an internal degree of freedom and a conditional shift moves the particle between sites. Despite this simplicity, quantum walks display rich topological phenomena and provide one of the simplest systems in which to study and understand topological phases [1]. The field is now a solid research area of quantum computation, with the walks serving both as algorithmic primitives — they are the quantum counterparts of Markov chains, with emphasis on algorithmic applications [8] — and as a universal model of quantum computation [3].

Two facts motivate the present paper. First, quantum-walk simulators are software, and software that claims to implement a unitary evolution can be checked against explicit mathematical contracts. Deductive verification of unmodified library functions has been benchmarked on conventional code: a benchmark of 26 unmodified Linux kernel library functions implementing memory and string operations had formal contracts extracted from source code as preconditions and postconditions, and the correctness of 23 of the 26 functions was completed [7]. The same contract discipline — extract the precondition/postcondition pair from the mathematical definition of the object, then discharge the proof obligations — applies verbatim to a quantum-walk evolution operator, where the contract is unitarity and the proof obligation is $U^{\dagger}U = I$. Second, the most interesting correctness targets for a quantum walk are not generic matrix properties but topological ones: integer-valued invariants that must be exactly integers if the simulator is faithful. Topological observables elsewhere in physics have this same "must be an exact discrete value" character; for example, in the ZBW-Majorana framework, Zitterbewegung is proposed as a $\mathbb{Z}_2$ topological observable distinguishing Dirac from Majorana fermions at the hardware level [12]. An invariant that is provably integer converts a floating-point question into a rounding question, which is exactly the kind of question verification is good at.

This paper makes three contributions: (i) a formal statement of the verification contracts for a discrete-time quantum walk simulator; (ii) explicit cost derivations for the unitarity contract in dense and sparse representations, with all arithmetic shown; (iii) an error-bound analysis for numerically extracted topological invariants, connecting the verification program to the topological-physics literature on quantum walks [1], [4], [5], [6].

## 2. Background and Related Work

**Quantum walks as a computational model.** Venegas-Andraca's comprehensive review establishes quantum walks as the quantum mechanical counterpart of classical random walks, an advanced tool for building quantum algorithms, and — as it notes — a universal model of quantum computation, with the field full of open problems for physicists, computer scientists, mathematicians and engineers [3]. The algorithmic-applications overview by Ambainis likewise treats quantum walks as quantum counterparts of Markov chains and gives a brief overview with emphasis on their algorithmic applications [8]. Both entries support the premise that a walk simulator is a computational artifact worth verifying: if walks are a universal computational model, errors in a simulator propagate to claims about computational behavior.

**Limit distributions and asymptotics.** The review of the one-dimensional discrete-time quantum walk analytically shows the weak limit theorem — the asymptotic behavior of the walk's position distribution — and connects the limit distribution of the discrete-time walk to the continuous-time walk [5]. For verification purposes this matters because the limit theorem supplies an asymptotic contract: any faithful simulator must reproduce the ballistic (quadratic-in-time) spreading that the theorem guarantees, in contrast to the diffusive spreading of a classical random walk. We use this as a statistical cross-check that complements the exact algebraic checks.

**Topological structure.** The topological review of discrete quantum walks in one and two dimensions establishes that walks display rich topological phenomena and are among the simplest systems for studying topological phases, providing elementary expositions of the physics [1]. This is the source of our second class of verification targets: topological invariants of the walk's band structure. On the dynamical side, the study of cyclic quantum walks shows that a periodic quantum walk on a 3-cycle graph can be generated via a deterministic combination of two chaotic ones, a quantum analog of the classical result that combining two chaotic random walks can yield an ordered (periodic) walk [4]. Periodicity is itself a checkable contract — a simulator claimed to produce a periodic walk on the 3-cycle must return to its initial state after the declared period — and [4] supplies a concrete family of such claims.

**Noise and symmetries.** The symmetries study of unbiased (Hadamard) and biased quantum walks on a line shows that certain discrete symmetries hold even when the walker is subjected to environmental effects, with noise modeled by phase flip, bit flip and generalized amplitude damping channels, and numerical solutions obtained by evolving the density matrix [6]. This entry supports two points for us: first, that symmetry under noise is a legitimate contract clause (a simulator with a noise channel must still preserve the stated symmetries); second, that density-matrix evolution is the established numerical method whose cost profile we should compare against pure-state unitarity checking.

**Alternative computational paradigms.** The discrete-event simulation work studies two models of experimentally realizable quantum walks by discrete-event simulation on a digital computer, with models that comply with Einstein locality, are as "realistic" as the simple random walk in that particles follow well-defined trajectories, avoid particle-wave duality and wave-function collapse, and reproduce the quantum statistics [2]. This is a distinct verification target: a discrete-event simulator does not maintain a state vector, so the unitarity contract does not directly apply; instead the contract is reproduction of the quantum statistics, which is statistical rather than algebraic. Our cost analysis therefore covers the state-vector family, and we flag the discrete-event family as requiring different obligations.

**Deductive verification methodology.** The deductive-verification benchmark of 26 unmodified Linux kernel library functions for memory and string operations, with contracts extracted from source code as preconditions and postconditions and 23 of 26 functions verified [7], is our methodological template. The entry's summary gives no further detail on the verification tooling, but the structure — extract contract, discharge obligation, report verified fraction — is exactly what we import. The verified fraction $23/26$ is itself a quantitative anchor for what "mostly verifiable" means in practice; we compute it explicitly in Section 4.

**Thermodynamic and finite-distinction foundations.** The finite-distinction framework holds that a finite-entropy world is a finite-distinction world in which uncountable precision is unphysical while computable depth and $p$-adic valuation remain physically real, with the state-space geometry of finite distinctions combinatorial and ultrametric, and quantum mechanics read as thermodynamics as a stochastic th[ermodynamics] (the supplied summary is truncated at this point) [9]. To the extent the summary supports it, this motivates our emphasis on exactly checkable, finite, discrete contracts (integer invariants, exact support bounds) over asymptotic floating-point agreement. The adelic-complexity/silent-radix entry [10] has an empty supplied summary; we therefore make no claim about its content and cite it only as part of the same corpus context. The Manifesto for Honest Computation, in its Phase VI final synthesis, states 5 principles, a concrete portfolio, and a Falsification Pledge [11]; we adopt the falsification-pledge posture explicitly in Section 6, stating conditions under which our cost claims would be falsified.

**Topological fermion distinction.** The ZBW-Majorana hypothesis, developed across four companion papers (P1–P4), establishes Zitterbewegung — the rapid trembling motion of Dirac fermions at the Compton scale — as a $\mathbb{Z}_2$ topological observable distinguishing Dirac from Majorana fermions at the hardware level [12]. We use this only as an analogy for the epistemic status of discrete-valued topological observables: like a $\mathbb{Z}_2$ invariant, a winding number is robust to small perturbations and only vulnerable to errors large enough to flip the integer, which is what makes invariant checking a natural verification primitive.

## 3. Methods

**Model.** We consider the standard one-dimensional discrete-time quantum walk (Hadamard walk). The Hilbert space is $\mathcal{H}_t = \mathcal{H}_p \otimes \mathcal{H}_c$ with coin space $\mathcal{H}_c$ of dimension $d_c = 2$ and, after $t$ steps from the origin, position support $\{-t, \ldots, t\}$ of size $N_t = 2t + 1$. The one-step operator is

$$U = S \,(I_{N} \otimes H), \qquad H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix},$$

where $S$ is the conditional shift and $H$ the Hadamard coin. The state-vector dimension after $t$ steps is

$$d_t = d_c \, N_t = 2(2t+1).$$

**Contracts.** We define four verification contracts for a walk simulator, in the extract-then-discharge style of [7]:

- (C1) *Unitarity*: $U^{\dagger}U = I_{d_t}$, i.e., $d_t(d_t+1)$ real constraints.
- (C2) *Probability conservation*: for every step, $\sum_x (|a_{x,L}|^2 + |a_{x,R}|^2) = 1$.
- (C3) *Support bound*: $\text{supp}(\psi_t) \subseteq \{-t,\ldots,t\}$, exactly.
- (C4) *Topological invariant*: the winding number $w \in \mathbb{Z}$ extracted from the walk's band structure equals its model value exactly.

**Cost model.** We count multiply-add operations. A dense unitarity check computes all $d_t$ row inner products of $U$ (each of length $d_t$), costing $d_t^{3}$ multiply-adds. A sparse check exploits that each row of $U$ has exactly $k = 2$ nonzero entries (each site connects to two coin-resolved neighbors), so each row inner product costs at most $k^{2} = 4$ multiply-adds over vectors of length $k$, and there are $d_t$ rows, giving cost $4 d_t \cdot 2 = 8 d_t$ (the factor 2 accounts for the two accumulated products per inner product). All costs are operation counts, not wall-clock times; where we convert to time we state the assumed machine rate explicitly as a projection.

**Invariant extraction.** Following the topological framework of [1], we extract a winding number from a two-band structure with phase $\varphi(k)$ over the Brillouin zone:

$$w = \frac{1}{2\pi} \oint \nabla_k \varphi \cdot dk = \frac{1}{2\pi} \sum_{j=0}^{M-1} \Delta\varphi_j,$$

on a grid of $M$ points, where $\Delta\varphi_j = \varphi(k_{j+1}) - \varphi(k_j)$ taken on the principal branch.

## 4. Analysis

All inputs below are either model definitions from Section 3 or stated assumptions; every arithmetic step is shown.

**D1. State-space dimension.** For $t = 10^{3}$: $N_t = 2t + 1 = 2(10^{3}) + 1 = 2001$, and $d_t = 2 N_t = 4002$.

**D2. Dense unitarity cost.** With $d_t = 4002$:

$$d_t^{2} = 4002 \times 4002 = 16{,}016{,}004,$$
$$d_t^{3} = 16{,}016{,}004 \times 4002 = 64{,}096{,}064{,}008 \approx 6.41 \times 10^{10} \text{ multiply-adds}.$$

Converting to time under the stated assumption of $r = 10^{9}$ multiply-adds per second:

$$T_{\text{dense}} = \frac{6.4096 \times 10^{10}}{10^{9}} \approx 64.1 \text{ s}.$$

**D3. Sparse unitarity cost.** With $k = 2$ nonzeros per row: cost $= 8 d_t = 8 \times 4002 = 32{,}016$ multiply-adds. The speedup factor is

$$\frac{d_t^{3}}{8 d_t} = \frac{64{,}096{,}064{,}008}{32{,}016} \approx 2.002 \times 10^{6}.$$

Check: $32{,}016 \times 2 \times 10^{6} = 6.4032 \times 10^{10}$, which is within $0.1\%$ of $6.4096 \times 10^{10}$, consistent with the quotient.

**D4. Constraint count.** The unitarity contract (C1) imposes $d_t(d_t + 1)$ real constraints: $4002 \times 4003 = 16{,}024{,}006$ real equations for the $t = 10^{3}$ case.

**D5. Floating-point drift bound (projection).** Assumptions: IEEE double precision with unit roundoff $\varepsilon = 2^{-52} \approx 2.2204 \times 10^{-16}$; each step applies to each amplitude $c = 4$ arithmetic operations (two coin multiplies, two shift accumulations); errors accumulate linearly in $t$ (no cancellation assumed — a worst-case bound). For $t = 10^{6}$:

$$\Delta_{\max} \leq c \, t \, \varepsilon = 4 \times 10^{6} \times 2.2204 \times 10^{-16} = 8.8818 \times 10^{-10}.$$

So the total probability computed by a double-precision simulator drifts from $1$ by at most $\approx 8.9 \times 10^{-10}$ after $10^{6}$ steps under these assumptions. This is a projection, not a measurement; it assumes linear error accumulation and no renormalization.

**D6. Verified-fraction anchor from [7].** The benchmark of [7] comprises $n = 26$ functions with $v = 23$ verified:

$$\frac{v}{n} = \frac{23}{26} \approx 0.8846.$$

**D7. Winding-number discretization bound.** Assumptions: grid of $M = 64$ points; per-point phase error (from floating-point evaluation of $\varphi$) bounded by $\delta_{\max} = 10^{-3}$ rad. The computed invariant deviates from the true one by at most

$$|w_{\text{comp}} - w| \leq \frac{M \, \delta_{\max}}{2\pi} = \frac{64 \times 10^{-3}}{2\pi} = \frac{0.064}{6.28319} \approx 0.01019.$$

Since $0.01019 \ll 0.5$, rounding $w_{\text{comp}}$ to the nearest integer recovers $w$ exactly under these assumptions, with a safety margin factor of

$$\frac{0.5}{0.01019} \approx 49.1.$$

**D8. Support-bound exactness.** The support contract (C3) is exactly checkable with zero floating-point error: after $t$ steps the support is the integer set $\{-t, \ldots, t\}$ of size $2t + 1$; for $t = 10^{3}$ this is $2001$ sites, and any amplitude found outside this set is a proof of infidelity, independent of precision.

## 5. Results

All numbers below are computed in Section 4 by the cited derivations, or are explicitly labeled projections.

1. **State-space dimension** (D1): a Hadamard walk after $t = 10^{3}$ steps lives on $d_t = 4002$ amplitudes.
2. **Dense unitarity-check cost** (D2): $64{,}096{,}064{,}008 \approx 6.41 \times 10^{10}$ multiply-adds; $\approx 64.1$ s at the assumed rate of $10^{9}$ multiply-adds/s (projection; the operation count itself is exact).
3. **Sparse unitarity-check cost** (D3): $32{,}016$ multiply-adds, a speedup factor of $\approx 2.002 \times 10^{6}$ over the dense check.
4. **Contract size** (D4): $16{,}024{,}006$ real constraints for the unitarity contract at $t = 10^{3}$.
5. **Probability-drift bound** (D5, projection): at most $8.8818 \times 10^{-10}$ total-probability drift after $t = 10^{6}$ steps in double precision, under linear accumulation and no renormalization.
6. **Verification-fraction anchor** (D6): the deductive-verification benchmark of [7] verified $23/26 \approx 0.8846$ of its functions.
7. **Invariant robustness** (D7): a $64$-point grid with per-point phase error $10^{-3}$ rad bounds the winding-number error by $0.01019$, a safety factor of $\approx 49.1$ below the $0.5$ rounding threshold.
8. **Exact support contract** (D8): the support check is exact (zero numerical error) on $2001$ sites for $t = 10^{3}$.

## 6. Discussion

**Limitations.** The cost analysis counts operations for one contract (C1) on one model (1D Hadamard walk). The sparse-cost figure $8d_t$ assumes exactly $k = 2$ nonzeros per row; walks with multi-dimensional coin lattices, time-dependent coins, or noise channels [6] have larger $k$ and the speedup shrinks proportionally. The time conversions assume a uniform $10^{9}$ multiply-adds/s rate; real dense linear-algebra kernels and sparse kernels have very different achievable rates, so the wall-clock figures are projections, not benchmarks. The drift bound (D5) is a worst-case linear-accumulation estimate; actual drift may be smaller (random-walk-like error accumulation would scale as $\sqrt{t}$ rather than $t$) or larger (if the step operator amplifies rounding asymmetries). We have not measured any simulator.

**Failure modes.** The winding-number result (D7) fails if the true band structure has near-degeneracies where $\Delta\varphi_j$ is ill-defined; the principal-branch sum then miscounts, and no grid refinement within the same branch convention repairs it. The sparse check verifies orthonormality of rows but, if the implementation stores $U$ implicitly (as a function rather than a matrix), the check must be re-derived against the implicit application, and the cost model changes. The support contract (C3) is exact only for the ideal walk; with a noise channel as in [6], the support strictly speaking spreads beyond $\{-t,\ldots,t\}$ through damping tails, and the contract must be restated probabilistically.

**What would falsify the claims.** The operation-count claims (D2, D3) are falsified by exhibiting a correct dense or sparse unitarity check with asymptotic cost below $d_t^{3}$ or $8d_t$ respectively for this walk structure. The drift bound (D5) is falsified by a double-precision simulator whose total probability departs from $1$ by more than $8.9 \times 10^{-10}$ after $10^{6}$ steps without renormalization. The invariant-robustness claim (D7) is falsified by a band structure where a $64$-point, $10^{-3}$-rad-accurate grid yields a non-integer rounded winding number while the true invariant is integer. The methodological claim — that contract-based verification transfers from conventional library functions [7] to walk simulators at a comparable verified fraction near $0.88$ — is falsified by a benchmark on walk simulators whose verified fraction is substantially lower for reasons intrinsic to the quantum setting (e.g., obligations requiring quantifier alternation over the position lattice).

**Arguing against ourselves.** One may object that unitarity of the one-step operator is trivially true by construction (a product of unitaries) and needs no numerical check. This is correct for a verified-by-construction implementation, but the check is not redundant for simulators that compose hand-written kernels, use approximate arithmetic, or implement $S$ and $H$ separately with indexing bugs — the historical failure mode of sparse stencil codes. A stronger objection: the topological-invariant check (C4) presupposes that the simulator's band structure is well-defined, which requires an infinite (thermodynamic) position lattice, whereas our cost analysis used the finite support $\{-t,\ldots,t\}$; reconciling the finite-support simulator with the infinite-lattice invariant requires a finite-size scaling argument we have not supplied. Finally, the finite-distinction perspective [9] — that uncountable precision is unphysical while computable depth remains real — suggests the drift bound (D5) may be the wrong target entirely: if precision beyond $\sim 10^{-16}$ is physically meaningless, contracts should be stated at finite resolution, and our exact/integer contracts (C3, C4) are the right ones while (C2) as stated is not. We leave this as an open question. The discrete-event paradigm [2] evades the unitarity contract altogether by design; whether its statistical reproduction contract can be discharged deductively rather than empirically is open. Whether the periodicity contracts arising from deterministic combinations of chaotic walks on cyclic graphs [4] can be verified more cheaply than generic unitarity is also open. The truncated summary of [9] and the empty summary of [10] limit how much of the corpus's thermodynamic apparatus we can responsibly invoke; extending the cost analysis to an ultrametric state-space geometry, as [9] suggests, is untested here.

## 7. Conclusion

We have framed discrete-time quantum-walk simulators as verification targets with four explicit contracts — unitarity, probability conservation, exact support, and integer topological invariant — importing the contract-extraction methodology benchmarked on conventional library functions, where 23 of 26 functions were verified [7]. Explicit arithmetic shows that exploiting the walk's two-nonzeros-per-row sparsity reduces the unitarity-check cost from $d_t^{3} \approx 6.41 \times 10^{10}$ to $8d_t = 32{,}016$ multiply-adds at $t = 10^{3}$, a factor $\approx 2.0 \times 10^{6}$, making full algebraic verification of the step operator cheap for realistic step counts. The topological contract is protected by a large robustness margin (safety factor $\approx 49$ under stated grid assumptions), consistent with the general robustness of discrete topological observables [1], [12]. The exact, integer-valued contracts are, on this analysis, the most verification-friendly targets, in line with the finite-distinction view that computable, discrete structure is what remains physically real [9]. Future work: deductive benchmarks on actual walk simulators, cost analysis for noisy walks [6], periodicity contracts on cyclic graphs [4], and statistical-contract discharge for discrete-event simulators [2].

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