# Deductive Verification of Discrete-Time Quantum-Walk Simulators: Contracts, Cost Bounds, and Periodicity Targets

## Abstract

Discrete-time quantum walks are a universal model of quantum computation, a platform for topological phases, and a standard testbed for quantum algorithms, yet the simulators used to study them are rarely checked with the rigor applied to classical library code. We frame quantum‑walk simulator verification as a contract‑checking problem in the style of deductive verification of library functions, where formal contracts are extracted as preconditions and postconditions and discharged as proof obligations. We define four contracts—unitarity, probability conservation, exact support bounds, and integer‑valued topological invariants—and derive their computational costs with explicit arithmetic. For a Hadamard walk evolved $t = 10^{3}$ steps, the state vector has dimension $d_t = 4002$; a dense unitarity check costs $d_t^{3} = 64{,}096{,}048{,}008$ multiply‑add operations, while a sparse check exploiting two non‑zeros per column costs $4 d_t^{2} = 64{,}064{,}016$, a speedup factor of $d_t/4 = 1000.5$. Naïve direct simulation costs $M_t = 8t(t+2) = 8{,}016{,}000$ real multiplications, so normalization checking adds $50\%$ multiplication overhead per step, independent of $t$, as derived in Section 4 (Derivation 6). We derive a double‑precision drift bound of $8.88 \times 10^{-10}$ after $10^{6}$ steps (projection) and an illustrative periodicity contract on the 3‑cycle with return probability $1/3$ under an explicitly stated uniform‑amplitude assumption. No empirical measurements are reported.

## 1. Introduction

Quantum‑algorithm developers rely on software simulators of discrete‑time quantum walks to prototype, benchmark, and verify algorithmic ideas before committing to costly experimental platforms. A buggy simulator can mislead design choices, waste development time, and obscure genuine algorithmic advantages, thereby blocking progress in quantum‑computing research and engineering. If a formal verification framework could guarantee that a simulator respects the exact mathematical contracts of the underlying walk, developers would gain confidence that their algorithmic conclusions are not artefacts of implementation errors.

Two facts motivate this paper. First, quantum‑walk simulators are software, and software that claims to implement a unitary evolution can be checked against explicit mathematical contracts. Deductive verification of unmodified library functions has been benchmarked on conventional code: a benchmark of 26 unmodified Linux kernel library functions implementing memory and string operations had formal contracts extracted from source code as preconditions and postconditions, and the correctness of 23 of the 26 functions was completed [7]. The same discipline—extract the contract from the mathematical definition of the object, then discharge the proof obligations—applies to a quantum‑walk evolution operator, where the contract is unitarity and the obligation is $U^{\dagger}U = I$.

Second, the most interesting correctness targets for a quantum walk are not generic matrix properties but discrete ones: integer‑valued topological invariants that must be exactly integers if the simulator is faithful, and periodicity claims that are sharp, decidable properties of the implemented update rule. Prior work on cyclic quantum walks starts from the classical result that combining two chaotic random walks can yield an ordered (periodic) walk and seeks a quantum analog, focusing on a periodic quantum walk on a 3‑cycle graph generated via a deterministic combination of two chaotic ones [4]. Such a periodicity statement can be expressed as a postcondition equating the simulator state at step $t$ with the state at step $t + T$ for the claimed period $T$.

**Contributions.**  
- (i) A formal statement of verification contracts for discrete‑time quantum‑walk simulators, including a periodicity contract illustrated on the 3‑cycle (Section 3).  
- (ii) Explicit cost derivations for the unitarity, simulation, and contract‑size obligations, with all arithmetic shown (Section 4).  
- (iii) An error‑bound analysis for floating‑point drift and for numerically extracted topological invariants, with explicit falsification conditions (Section 6).

## 2. Background and Related Work

We discuss the supplied bibliography in its given order. Throughout, “coin” means the internal unitary acting on the walker’s internal degree of freedom, and “support” means the set of graph positions with nonzero amplitude.

**Topological phases in quantum walks [1].** The review presents discrete quantum walks as dynamical protocols for controlling a single quantum particle and argues that, despite their simplicity, they display rich topological phenomena and constitute one of the simplest systems to study topological phases. For verification this matters because topological invariants are exactly the quantity a buggy simulator can corrupt silently; our contracts include the support and normalization invariants that any downstream invariant computation presupposes.

**Discrete‑event simulation [2].** This work simulates two models of experimentally realizable quantum walks on a digital computer using models that comply with Einstein locality, in which particles follow well‑defined trajectories and avoid concepts such as particle‑wave duality and wave‑function collapse, reproducing the quantum‑theoretical results. This is a distinct verification target: a discrete‑event simulator does not maintain a state vector, so the unitarity contract does not directly apply; the contract becomes statistical reproduction of quantum statistics rather than an algebraic identity.

**Comprehensive review [3].** The review describes quantum walks as the quantum mechanical counterpart of classical random walks, an advanced tool for building quantum algorithms, and states that quantum walks have been shown to constitute a universal model of quantum computation. Universality raises the stakes of verification: a verified quantum‑walk simulator is a verified simulator for a universal family of computations.

**Order from chaos on cyclic graphs [4].** This study starts from the classical result that combining two chaotic random walks can yield an ordered (periodic) walk and seeks a quantum analog; it studies chaotic and periodic behavior of cyclic quantum walks and focuses on a periodic quantum walk on a 3‑cycle graph generated via a deterministic combination of two chaotic ones. Periodicity is a canonical verification target, and [4] supplies a concrete family of such claims; we use it in Section 4 as an illustrative contract instance.

**Limit distributions [5].** This work analytically shows the weak limit theorem—the asymptotic behavior—of the one‑dimensional discrete‑time quantum walk, and discusses the relation between the limit distribution of the discrete‑time walk and the continuous‑time walk. Limit theorems supply asymptotic reference distributions against which finite‑$t$ simulations can be statistically cross‑checked, complementing the exact algebraic contracts.

**Symmetries and noise [6].** This study examines discrete symmetries of unbiased (Hadamard) and biased quantum walks on a line and shows that these symmetries hold even when the walker is subjected to environmental effects, with noise modeled by phase‑flip, bit‑flip, and generalized amplitude‑damping channels, and numerical solutions obtained by evolving the density matrix. This is the natural bridge from verified unitary simulators to verified open‑system simulators: the density‑matrix loop has the same contract structure with trace conservation replacing probability conservation, and the named noise channels are the first operations whose contract clauses one would write.

**Deductive verification of systems code [7].** The benchmark consists of 26 unmodified Linux kernel library functions implementing conventional memory and string operations; formal contracts were extracted from the functions’ source code as preconditions and postconditions, and the correctness of 23 functions was completed. We use this as the methodological template—contracts extracted from the code as written, applied to unmodified functions, with a partial but high completion rate—and compute the verified fraction $23/26$ explicitly in Section 4.

**Algorithmic applications [8].** This overview characterizes quantum walks as quantum counterparts of Markov chains and gives a brief overview with emphasis on their algorithmic applications. It supplies the consumer‑side motivation: every algorithmic application downstream of a walk simulation inherits the simulator’s correctness.

**Finite‑distinction quantum mechanics [9].** The QNFO program argues that a finite‑entropy world is a finite‑distinction world, that uncountable precision is unphysical while computable depth and $p$‑adic valuation remain physically real, and that the state‑space geometry of finite distinctions is combinatorial and ultrametric, with quantum mechanics read as thermodynamics. We use only what the summary states: the finiteness thesis, the combinatorial‑ultrametric geometry claim, and the thermodynamic reading. This motivates our emphasis on exactly checkable, finite, discrete contracts (integer invariants, exact support bounds) over asymptotic floating‑point agreement.

## 3. Methods

### 3.1 Model

We consider the standard one‑dimensional discrete‑time Hadamard walk. The Hilbert space is $\mathcal{H}_p \otimes \mathcal{H}_c$, where $\mathcal{H}_p = \mathrm{span}\{|x\rangle : x \in \mathbb{Z}\}$ and $\mathcal{H}_c = \mathrm{span}\{|0\rangle, |1\rangle\}$ has dimension $d_c = 2$. The state at step $t$ is

$$
|\psi_t\rangle = \sum_{x \in \mathbb{Z}} \left( \alpha_{x,0}^{(t)} |x,0\rangle + \alpha_{x,1}^{(t)} |x,1\rangle \right),
$$

with $\sum_{x} \left( |\alpha_{x,0}^{(t)}|^2 + |\alpha_{x,1}^{(t)}|^2 \right) = 1$. One step is

$$
|\psi_{t+1}\rangle = \hat{U} |\psi_t\rangle, \qquad \hat{U} = \hat{S}\left(\hat{I} \otimes \hat{C}\right),
$$

where $\hat{C}$ is the Hadamard coin

$$
\hat{C} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix},
$$

and $\hat{S}|x,0\rangle = |x-1,0\rangle$, $\hat{S}|x,1\rangle = |x+1,1\rangle$. The walk starts at $x_0 = 0$ with $\alpha_{0,0}^{(0)} = 1$ and all other amplitudes zero. After $t$ steps the support is contained in $\{-t, \ldots, t\}$, of size $N_t = 2t + 1$, and the state‑vector dimension is

$$
d_t = d_c \, N_t = 2(2t+1).
$$

### 3.2 Contracts

In the extract‑then‑discharge style of [7], we attach to the step function $\texttt{step}(\psi_t) \to \psi_{t+1}$ the following contracts:

- **(K1) Unitarity:** $\hat{U}^{\dagger}\hat{U} = I_{d_t}$, i.e., $d_t(d_t + 1)$ real constraints.  
- **(K2) Probability conservation:** $\sum_{x} \left( |\alpha_{x,0}^{(t)}|^2 + |\alpha_{x,1}^{(t)}|^2 \right) = 1$ within tolerance $\varepsilon$, at every step.  
- **(K3) Exact support bound:** $\mathrm{supp}(\psi_t) \subseteq \{-t, \ldots, t\}$, checkable with zero floating‑point error.  
- **(K4) Topological invariant:** the winding number $w \in \mathbb{Z}$ extracted from the walk’s band structure equals its model value exactly.  
- **(K5) Periodicity (illustrative, from [4]):** for a walk claimed periodic with period $T$, the state at step $t + T$ equals the state at step $t$.

Clauses K1 and K2 follow from unitarity of $\hat{U}$: since $\hat{C}^{\dagger}\hat{C} = \hat{I}$ and $\hat{S}^{\dagger}\hat{S} = \hat{I}$, we have $\hat{U}^{\dagger}\hat{U} = \hat{I}$, so $\langle \psi_{t+1} | \psi_{t+1} \rangle = \langle \psi_t | \psi_t \rangle$. Clause K3 holds because one step moves each amplitude by at most one position. Each clause is a decidable predicate over the simulator’s data structures, checkable by an SMT‑backed verifier of the kind used in the benchmark of [7].

### 3.3 Cost model

We count multiply‑add operations, not wall‑clock time; where we convert to time we state the assumed machine rate explicitly as a projection. A dense unitarity check computes all $d_t$ row inner products of $\hat{U}$ (each of length $d_t$), costing $d_t^{3}$ multiply‑adds. A sparse unitarity check exploits that each column of $\hat{U}$ has exactly $k = 2$ nonzero entries, so each of the $d_t^{2}$ entries of $\hat{U}^{\dagger}\hat{U}$ costs $k^{2} = 4$ multiply‑adds, giving total cost $4 d_t^{2}$ (Derivation 3). A cheaper $8 d_t$ check computes only the $d_t$ row norms and verifies normalization, not orthogonality, so it does not discharge K1. For the periodicity illustration (K5) we use the 3‑cycle of [4]: vertices $v_{0}, v_{1}, v_{2}$ with edges $(v_{0},v_{1})$, $(v_{1},v_{2})$, $(v_{2},v_{0})$, evolved by a deterministic combination of two constituent walks in the spirit of [4]; the specific interleaving schedule is an illustrative assumption of this paper, not a detail reported by [4].

### 3.4 Finite‑distinction alignment

The finite‑distinction program [9] holds that uncountable precision is unphysical and that finite‑distinction state spaces are combinatorial and ultrametric. We operationalize this as follows: the verified artifact is a finite map from integer pairs $(x, c)$ with $|x| \leq t$ and $c \in \{0,1\}$ to amplitude records — exactly $N_t = 2(2t+1)$ records at step $t$. No continuum object appears in the verified artifact. We stress that this is a methodological alignment, not a derivation of quantum mechanics from [9]; the summary of [9] supports the finiteness and geometry claims we invoke and nothing more.

## 4. Analysis

Every input number below is either a model definition (Section 3), a structural fact derived from it, or an explicitly labeled projection. All arithmetic is shown.

**Derivation 1 (state‑space dimension).** Inputs: $d_c = 2$ (Section 3.1); support size $N_t = 2t + 1$ (each step moves the walker by exactly one position, so the support after $t$ steps lies in $\{-t,\ldots,t\}$, which has $2t+1$ integer points). Hence

$$
d_t = d_c(2t+1) = 2(2t+1).
$$

For $t = 10^{3}$: $2t + 1 = 2001$, so $d_{1000} = 2 \times 2001 = 4002$. For $t = 10^{6}$: $2t+1 = 2{,}000{,}001$, so $d_{10^6} = 4{,}000{,}002$.

**Derivation 2 (dense unitarity‑check cost).** Input: $d_t = 4002$ (Derivation 1).

$$
d_t^{2} = 4002 \times 4002 = 16{,}016{,}004,
$$
$$
d_t^{3} = 16{,}016{,}004 \times 4002 = 16{,}016{,}004 \times 4000 + 16{,}016{,}004 \times 2 = 64{,}064{,}016{,}000 + 32{,}032{,}008 = 64{,}096{,}048{,}008.
$$

So the dense check costs $64{,}096{,}048{,}008 \approx 6.41 \times 10^{10}$ multiply‑adds. Converting to time under the stated assumption of $r = 10^{9}$ multiply‑adds per second (projection; the operation count itself is exact):

$$
T_{\mathrm{dense}} = \frac{64{,}096{,}048{,}008}{10^{9}} = 64.096048008 \ \mathrm{s} \approx 64.1 \ \mathrm{s}.
$$

**Derivation 3 (sparse unitarity‑check cost).** Verifying $\hat{U}^{\dagger}\hat{U} = I$ requires evaluating all $d_t^{2}$ entries of $\hat{U}^{\dagger}\hat{U}$, each an inner product of two columns of $\hat{U}$. Each column has $k = 2$ nonzero entries, so each entry costs $k^{2} = 4$ multiply‑adds, giving total cost

$$
4 d_t^{2} = 4 \times 16{,}016{,}004 = 64{,}064{,}016 \ \text{multiply‑adds},
$$

using $d_t^{2} = 16{,}016{,}004$ from Derivation 2. The speedup factor over the dense check is

$$
\frac{d_t^{3}}{4 d_t^{2}} = \frac{d_t}{4} = \frac{4002}{4} = 1000.5.
$$

A cheaper check computing only the $d_t$ row norms costs $8 d_t = 8 \times 4002 = 32{,}016$ multiply‑adds, but it verifies only normalization of rows, not orthogonality, and therefore discharges K2‑style normalization clauses rather than K1.

**Derivation 4 (unitarity constraint count).** The contract K1 imposes $d_t(d_t + 1)$ real constraints. For $d_t = 4002$:

$$
d_t(d_t+1) = 4002 \times 4003 = 4002 \times 4000 + 4002 \times 3 = 16{,}008{,}000 + 12{,}006 = 16{,}020{,}006.
$$

**Derivation 5 (simulation multiplication count).** Input: the coin entries have magnitude $2^{-1/2}$ (Section 3.1). Applying $\hat{C}$ at one site computes two output amplitudes,

$$
\beta_0 = 2^{-1/2}(\alpha_0 + \alpha_1), \qquad \beta_1 = 2^{-1/2}(\alpha_0 - \alpha_1).
$$

Each product of a complex amplitude by the real scalar $2^{-1/2}$ costs $2$ real multiplications (real and imaginary parts). There are $2$ output amplitudes $\times\, 2$ input terms each $= 4$ such products, hence $4 \times 2 = 8$ real multiplications per site per step; the shift is data movement and costs none. At step $s$ the occupied support has at most $2s + 1$ sites (worst case), so

$$
M_t = \sum_{s=1}^{t} 8(2s+1) = 16\sum_{s=1}^{t} s + 8t = 16 \cdot \frac{t(t+1)}{2} + 8t = 8t^2 + 16t = 8t(t+2).
$$

Check of the closed form: $\sum_{s=1}^{t}(2s+1) = 2 \cdot \frac{t(t+1)}{2} + t = t^2 + 2t = t(t+2)$; multiplying by $8$ gives $M_t = 8t(t+2)$. For $t = 1000$: $1000 \times 1002 = 1{,}002{,}000$, and $8 \times 1{,}002{,}000 = 8{,}016{,}000$. For $t = 100$: $8 \times 100 \times 102 = 800 \times 102 = 81{,}600$.

**Derivation 6 (verification overhead ratio).** Evaluating clause K2 requires computing $\sum_{x} (|\alpha_{x,0}|^2 + |\alpha_{x,1}|^2)$ over $d_t$ records; each term costs $2$ real multiplications, so one check costs $2 d_t$ real multiplications. Two checks per step (input K2 and output K2) cost $4 d_t$. The simulation itself costs $8 d_t$ per step (Derivation 5, per‑step rate). The overhead ratio is

$$
\frac{4 d_t}{8 d_t} = \frac{1}{2},
$$

i.e., normalization checking adds exactly $50\%$ multiplication overhead per step, independent of $t$. At $t = 1000$: $4 \times 4002 = 16{,}008$ verification multiplications per step versus $8 \times 4002 = 32{,}016$ simulation multiplications per step.

**Derivation 7 (contract clause count).** The minimal per‑step contract of Section 3.2 has, in the clause‑counting convention of Derivation 6’s framework, $2$ preconditions (input normalization, input support) and $3$ postconditions (output normalization, output support, coin correctness), i.e., $5$ clauses per step‑function instance. For a $t$‑step run verified step by step, the aggregate count is

$$
K_t = 5t; \qquad K_{1000} = 5 \times 1000 = 5{,}000, \qquad K_{100} = 500.
$$

If instead the verifier discharges the step lemma once and applies it $t$ times by induction, the aggregate obligation drops to one $5$‑clause lemma plus $t$ applications; we treat $K_t = 5t$ as the upper bound for the naive scheme and the inductive scheme as a projected lower bound with constant lemma cost.

**Derivation 8 (floating‑point drift bound, projection).** Assumptions: IEEE double precision with unit roundoff $\varepsilon_{\mathrm{fp}} = 2^{-52} \approx 2.2204 \times 10^{-16}$; each rounding contributes at most $\varepsilon_{\mathrm{fp}}$ relative error; errors accumulate linearly (no favorable cancellation assumed). Input: the coin update at one site forms each output amplitude from $2$ products (Derivation 5), each product costing $2$ real multiplications, i.e., $4$ roundings per output amplitude per step. The worst‑case relative drift after $t$ steps is therefore

$$
\delta_t \leq 4t\,\varepsilon_{\mathrm{fp}} = 4t \cdot 2^{-52}.
$$

For $t = 10^{6}$:

$$
\delta_{10^6} \leq 4 \times 10^{6} \times 2.2204 \times 10^{-16} = 8.8816 \times 10^{-10} \approx 8.88 \times 10^{-10}.
$$

This is a projection: it assumes the linear‑accumulation model and no error growth beyond per‑step roundoff; it is not an empirical measurement.

**Derivation 9 (illustrative 3‑cycle return probability).** Assumption (this paper, illustrative): the periodic orbit of the 3‑cycle contract K5 places equal‑amplitude magnitude $3^{-1/2}$ on each of the three vertices at the return step. The probability of finding the walker at the start vertex $v_{0}$ is then

$$
P_{\mathrm{ret}} = \left|3^{-1/2}\right|^{2} = \frac{1}{3} \approx 0.3333.
$$

This follows from the stated uniform‑amplitude assumption only; bibliography entry [4] does not report this number.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none is an empirical measurement.

- State‑vector dimension at $t = 10^{3}$: $d_{1000} = 4002$ (Derivation 1); at $t = 10^{6}$: $d_{10^6} = 4{,}000{,}002$.
- Dense unitarity‑check cost at $t = 10^{3}$: $d_t^{3} = 64{,}096{,}048{,}008$ multiply‑adds $\approx 6.41 \times 10^{10}$; projected time $\approx 64.1\ \mathrm{s}$ at the stated rate $r = 10^{9}\ \mathrm{s^{-1}}$ (Derivation 2).
- Sparse unitarity‑check cost: $4 d_t^{2} = 64{,}064{,}016$ multiply‑adds; speedup factor $d_t/4 = 1000.5$ (Derivation 3). The cheaper row‑norm check $8 d_t = 32{,}016$ verifies normalization only, not unitarity.
- Unitarity constraint count: $d_t(d_t+1) = 16{,}020{,}006$ at $t = 10^{3}$ (Derivation 4).
- Simulation cost: $M_t = 8t(t+2)$; $M_{1000} = 8{,}016{,}000$ and $M_{100} = 81{,}600$ real multiplications (Derivation 5).
- Verification overhead: verification $4 d_t = 16{,}008$ versus simulation $8 d_t = 32{,}016$ multiplications per step at $t = 10^{3}$, ratio $4 d_t / 8 d_t = 1/2$, i.e., $50\%$ multiplication overhead per step, independent of $t$ (Derivation 6).
- Contract clause count: $K_t = 5t$; $K_{1000} = 5{,}000$, $K_{100} = 500$ for the naive scheme (Derivation 7).
- Projected double‑precision drift bound: $\delta_{10^6} \approx 8.88 \times 10^{-10}$ (Derivation 8, projection).
- Illustrative 3‑cycle return probability: $P_{\mathrm{ret}} = 1/3$ under the stated uniform‑amplitude assumption (Derivation 9).

## 6. Discussion

**Limitations.** The cost model counts multiply‑adds, not wall‑clock time; the $64.1\ \mathrm{s}$ figure is a projection at an assumed rate $r = 10^{9}\ \mathrm{s^{-1}}$. The $50\%$ overhead figure is a worst‑case bound resting on the assumption that the support at step $s$ occupies all $2s+1$ sites; the true support of the Hadamard walk is smaller in aggregate, so the realized overhead on actual trajectories may be lower, though the per‑step bound holds. The drift bound of Derivation 8 assumes linear accumulation of roundoff and could be violated by ill‑conditioned amplitude cancellation or by error growth in long runs; it is a projection, not a measurement. The 3‑cycle return probability $1/3$ is an illustrative consequence of a uniform‑amplitude assumption made in this paper; entry [4]’s supplied summary does not state it, and the interleaving schedule of the constituent walks is likewise assumed here, not sourced from [4]. The winding‑number contract K4 is stated but not instantiated against a specific band structure in this paper, so no numerical margin is claimed.

**Failure modes and falsification.** The contract framework is falsified if (i) a faithful simulator violates K1–K3 under exact arithmetic, which would contradict the algebraic derivation of Section 3.2; (ii) the measured drift of a concrete implementation exceeds the projected bound $4t\,\varepsilon_{\mathrm{fp}}$ by a large factor, refuting the linear‑accumulation model; or (iii) the clause‑count convention of Derivation 7 misrepresents real verifier obligation counts. The methodological alignment with the finite‑distinction program [9] is explicitly not a derivation of quantum mechanics and would be misleading if read as one.

**Open questions.** Whether the inductive verification scheme of Derivation 7 achieves the projected constant lemma cost in practice; how the statistical contracts appropriate to discrete‑event simulators [2] compose with the algebraic contracts used here; and how trace‑conservation contracts for open‑system evolution [6] relate to the unitarity contract K1.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Quantum‑algorithm developers, quantum‑software library maintainers, and hardware‑control engineers who rely on classical simulators of discrete‑time quantum walks would use the verification framework to certify that their simulation code respects the exact mathematical contracts. If the contracts hold, developers can proceed to algorithmic benchmarking, resource estimation, and hardware‑control design with confidence that observed behaviours stem from the intended quantum dynamics rather than implementation bugs.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer‑review; according to NASA Technology Readiness Level definitions, it resides at TRL 2 (concept formulation) and does not exceed TRL 3 because no prototype or experimental validation is presented.

**(c) Minimal next experiment.** Implement the sparse unitarity‑check routine on an existing quantum‑walk simulation library (e.g., a Python or C++ implementation of the Hadamard walk). Measure the wall‑clock time for the dense check, the sparse check, and the row‑norm check at $t = 10^{3}$, and compare the observed speedup to the predicted factor $d_t/4 = 1000.5$. A measured speedup significantly below this factor would falsify the sparse‑check cost model, indicating hidden overheads (e.g., memory‑access patterns) not captured by the multiply‑add count.

**(d) Engineering constraints.** The primary constraints are:
- Availability of a processor capable of $10^{9}$ multiply‑adds per second for the projected time estimate (a high‑performance CPU or GPU).
- Memory layout that stores the sparse representation of $\hat{U}$ with exactly two non‑zeros per column to achieve the $4 d_t^{2}$ cost.
- Accurate floating‑point arithmetic conforming to IEEE double precision to validate the drift bound projection.

If any of these constraints cannot be satisfied, the projected performance figures become open questions.

**(e) Cost and performance projections.** Assuming a processor delivering $r = 10^{9}$ multiply‑adds per second, the dense unitarity‑check for $t = 10^{3}$ would take approximately $64.1$ seconds, while the sparse check would take $0.064$ seconds, reflecting the speedup factor $1000.5$. These numbers are direct projections from the arithmetic in Derivations 2 and 3.

**(f) Risks and misuse.** The framework could be misapplied to certify simulators that implement approximations (e.g., Trotter‑Suzuki decompositions) without adapting the contracts to reflect approximation error, leading to a false sense of correctness. Users must ensure that the contracts match the actual algorithmic semantics of their simulator.

## 8. Conclusion

We framed discrete‑time quantum‑walk simulator verification as contract extraction and discharge, following the template of deductive verification of unmodified library functions [7]. We stated five contracts (K1–K5), derived their costs with explicit arithmetic—a sparse‑over‑dense unitarity‑check speedup of $d_t/4 = 1000.5$ at $t = 10^{3}$, a worst‑case $50\%$ normalization‑check overhead, and a naive clause count $K_t = 5t$—and gave a projected double‑precision drift bound $\delta_{10^6} \approx 8.88 \times 10^{-10}$ plus an illustrative 3‑cycle periodicity contract with return probability $1/3$ under stated assumptions. The framework favors exactly checkable, finite, discrete contracts, in line with the finite‑distinction emphasis of [9], and every quantitative claim is either computed here with shown arithmetic or explicitly labeled a projection.

## References

[1] arXiv:1112.1882v1 | Topological phenomena in quantum walks; elementary introduction to the physics of topological phases  
[2] arXiv:2005.03401v1 | Discrete-event simulation of quantum walks  
[3] arXiv:1201.4780v2 | Quantum walks: a comprehensive review  
[4] arXiv:2008.00316v3 | Order from chaos in quantum walks on cyclic graphs  
[5] arXiv:1307.3384v1 | From Discrete Time Quantum Walk to Continuous Time Quantum Walk in Limit Distribution  
[6] arXiv:quant-ph/0607188v3 | Symmetries and noise in quantum walk  
[7] arXiv:1809.00626v1 | Deductive Verification of