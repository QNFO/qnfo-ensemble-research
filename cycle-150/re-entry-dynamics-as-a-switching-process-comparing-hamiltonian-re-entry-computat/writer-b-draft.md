# The Switching Economics of Hamiltonian Re-Entry Computation: A Cost-Model Comparison with Stored-Program Architectures

## Abstract

Stored-program (von Neumann) architectures pay a per-operation switching cost for instruction fetch, decode, and memory traffic, while a proposed Hamiltonian-computation paradigm identifies computation with continuous dynamical trajectories that re-enter a designated operating region of phase space. The specific gap addressed here is that the re-entry proposal has no explicit, parameterized cost accounting against the switching economics of the stored-program regime, so its economic case cannot be evaluated or falsified. This paper adopts the minimal two-model cost formalism of the prior re-entry analysis — an explicit-controller model with per-operation switching cost $c_{\mathrm{sw}}$ and an autonomous re-entry model with per-operation cost $c_{\mathrm{re}}$ — and extends it with a cache-aware break-even derivation and a cross-convention figure of merit. Under the stated illustrative assumptions ($k_{\mathrm{acc}} = 4$ memory accesses per operation, $t_{\mathrm{mem}} = 16$ time units per access, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$), the switching cost per operation is $c_{\mathrm{sw}} = 65$ time units against a re-entry cost $c_{\mathrm{re}} = 5$, a ratio of $13.0$; the switching overhead fraction is $f_{\mathrm{sw}} = 64/65 = 0.984615\ldots$ versus $f_{\mathrm{re}} = 0.2$. Break-even occurs at $t_{\mathrm{mem}}^{*} = 1$ time unit, the verdict tolerates re-entry overheads up to $t_{\mathrm{re}}^{*} = 61$ time units, and the new cache-aware analysis gives a break-even hit rate $h^{*} = 15/15.5 = 0.967741\ldots$ for a cache access costing half a time unit. The comparison is placed inside the von Neumann-algebra and switching-hardware literatures. All quantitative results are model projections with stated assumptions; no empirical measurements are claimed.

## 1. Introduction

Every computing architecture pays a price for moving state from where it is stored to where it is transformed. In a stored-program (von Neumann) architecture this price appears as the fetch-decode-execute cycle: before any arithmetic happens, the machine must switch its control and data paths to bring an instruction into the processing unit. John Backus identified two levels of this cost. The "von Neumann bottleneck" is the limited throughput between CPU and memory, much smaller than the rate at which the CPU can work; the "intellectual von Neumann bottleneck" is that programming cannot go beyond planning the enormous traffic of words through that bottleneck; and the "von Neumann vicious circle" is that non-von Neumann architectures cannot be developed for lack of effective non-von Neumann languages, which cannot be created for lack of conceptual foundations for such architectures [2]. Any proposal for a fundamentally different computational substrate must therefore be evaluated not only for physical plausibility but for its switching economics, stated in terms that survive the language-architecture lock-in the vicious circle describes.

The proposal evaluated here is the Hamiltonian-computation paradigm: the identification of computation with continuous dynamical trajectories that re-enter a designated operating region of phase space, so that one act of dynamical setup is reused many times without an external controller re-issuing it. A prior analysis, which this paper takes as its starting point, constructed a minimal two-model cost comparison of this re-entry paradigm against von Neumann switching costs [10]. That analysis derived a per-operation switching cost of $65$ time units against a re-entry cost of $5$ under explicitly memory-bound assumptions, a ratio of $13.0$, and identified the parameters on which the case turns. What remains missing is threefold. First, the prior model assumes fully serialized, uncached memory, and no cache-aware break-even condition has been derived; since real hierarchies cache aggressively, this is the assumption most likely to overturn the verdict. Second, the two cost conventions used in the prior work (time units and abstract cost units) have not been combined into a single cross-convention figure of merit. Third, the comparison has not been connected to the mathematical literature on von Neumann algebras, ergodic theory, and entropy, which supplies the natural language for the long-time statistics of re-entering dynamical systems and for the entropy bookkeeping of the loop.

Who faces this problem, and what does it cost them? Researchers proposing non-von Neumann substrates — dynamical-systems, neuromorphic, and quantum-computing groups — currently must argue their case against an architecture whose switching economics are entrenched, without a shared parameter vocabulary in which the argument can be settled by measurement. If the cost model developed here holds as a framing, the debate reduces to a small set of measurable quantities: the effective memory time $t_{\mathrm{mem}}^{\mathrm{eff}}$, the re-entry overhead $t_{\mathrm{re}}$, the per-pass loop cost $c_p$, and the reuse factor $n$. If it fails — for example, if the cache-aware break-even hit rate turns out to be unreachable in practice — the re-entry proposal loses its economic case in the regime that matters, and resources shift accordingly.

The contributions are:

1. A restatement and verification, with fully shown arithmetic, of the two-model cost formalism and its headline results ($c_{\mathrm{sw}} = 65$, $c_{\mathrm{re}} = 5$, ratio $13.0$, break-even $t_{\mathrm{mem}}^{*} = 1$, robustness threshold $t_{\mathrm{re}}^{*} = 61$), drawn from the prior analysis [10] and re-derived in Section 4.
2. A new cache-aware break-even derivation giving the critical cache hit rate $h^{*} = 15/15.5 = 0.967741\ldots$ at which the re-entry advantage vanishes for a cache access costing $0.5$ time units (Section 4, Derivation 8).
3. A cross-convention figure of merit $\sqrt{13.0 \times 3.125} = 6.3738\ldots$ combining the time-unit and cost-unit parameterizations (Section 4, Derivation 9).
4. A literature synthesis placing the comparison inside the switching-fabric literature [1], the Backus critique [2], and the von Neumann-algebra tradition of entropy [3], spectral graph complexity [4], ergodic theory [5], regularity [6], embedding and amenability [7], spectral theory of positive maps [8], and rigidity [9] (Section 2).
5. An explicit falsification criterion and limitations list for the claimed advantage (Section 6).

No empirical measurements are reported. Every number in Sections 4 and 5 is either derived by shown arithmetic from parameters declared in Section 3, or is a projection whose assumptions are stated inline.

## 2. Background and Related Work

**Switching fabrics and the cost of redirection.** The throughput of input-queued packet switches is limited by head-of-line blocking, and at each time-slot a traffic scheduler must configure a connection pattern for the switch fabric to avoid output contentions and maximize throughput; a good scheduler improves throughput and reduces end-to-end delay at low computation complexity [1]. Input scheduling based on Birkhoff-von-Neumann (BvN) decomposition achieves high throughput and low complexity, but the performance of the BvN switch becomes less predictable when the input traffic is bursty; the deflection-compensated BvN (D-BvN) switch architecture was proposed to enhance the quasi-static scheduling based on BvN decomposition, and its simulation compares average end-to-end delay against an ideal-deflection analytical lower bound, with the required critical VOQ size for a loss rate of $P_l = 10^{-5}$ entering the comparison and the average delay increasing linearly with burstiness [1]. This literature supplies the precedent for treating a switching event as the atomic unit of cost: in [1] the switching fabric's schedule is the bottleneck resource, exactly as the fetch-decode-execute cycle is in the stored-program model of Section 3. The re-entry paradigm's claim, in this vocabulary, is that a closed dynamical loop removes the per-slot scheduling act altogether.

**The Backus critique and the vicious circle.** The "von Neumann vicious circle" is the fact that non-von Neumann computer architectures cannot be developed because of the lack of widely available and effective non-von Neumann languages, and new languages cannot be created because of lack of conceptual foundations for non-von Neumann architectures, the reason being that programming languages are high-level abstract isomorphic copies of von Neumann computers [2]. The same source develops the functional-programming counter-tradition: primitive recursion as the basic schema for computing on natural numbers, higher-order primitive recursion via the Grzegorczyk iterator $R^{A}$ with $R^{A}(1)(c)(a) = a$ and $R^{A}(n+1)(c)(a) = c(n)(R^{A}(n)(c)(a))$, and the observation that the C$\lambda$aSH approach — from Haskell through term rewriting to a standard HDL — remains "still unsatisfactory" because the rewritten term ends as imperative code [2]. This matters here in two ways. It explains why a cost comparison must be stated in architecture-neutral parameters rather than in the vocabulary of either regime; and it shows that the loop-reuse structure of the re-entry model has a functional analogue, since the iterator $R^{A}$ re-uses the step function $c$ across $n$ applications just as the re-entry loop re-uses one dynamical segment across $n$ passes.

**Von Neumann entropy as bookkeeping.** Von Neumann associated an entropy quantity to a statistical operator in 1927, by a gedanken experiment on the ground of phenomenological thermodynamics, and the discussion was extended in his 1932 book *Mathematische Grundlagen der Quantenmechanik*; the historical reconstruction stresses the role of superselection sectors [3]. The same historical account records Shannon's derivation that the only uncertainty measure $H$ satisfying three reasonable requirements is $H = -K\sum_{i=1}^{n}p_i \log p_i$, with $K$ a positive constant [3]. For the re-entry model this supplies the bookkeeping functional: when the paper of Section 4 computes a dimensionless overhead quantity $\eta = \ln(5/4)$, it is a logarithmic ratio of the same kind that the Gibbs-von Neumann and Shannon functionals make meaningful, and any future thermodynamic interpretation of re-entry cost would be written in this currency.

**Entropy as a spectral complexity measure.** The von Neumann entropy of a graph is a spectral complexity measure applied in complex-network analysis and pattern recognition, with two variants based on the graph Laplacian and the normalized graph Laplacian; because of its computational complexity, previous works approximated it, and experiments on path graphs, random graphs with small-world structure, and real-world networks showed that the Laplacian and normalized Laplacian entropies capture related yet different structural patterns, that the quadratic approximations fail to explain non-trivial structures for the Laplacian case, and that the quality of approximation depends on graph topology [4]. This is directly relevant to the re-entry loop: a re-entry structure is a graph of dynamical transitions, and [4] establishes both that entropy-style measures characterize such structure and that cheap approximations of them can mislead in a topology-dependent way — a caution for any attempt to certify a re-entry loop's cost by an approximate spectral quantity.

**Long-time statistics of dynamical cocycles.** The classical Multiplicative Ergodic Theorem of Oseledets has been generalized to cocycles taking values in a semi-finite von Neumann algebra, allowing a continuous Lyapunov distribution; in the finite-dimensional version, for a measure-preserving transformation $f$ and a measurable cocycle $c$ satisfying a first-moment condition, the limit operator $\Lambda(x) := \lim_{n \to \infty}[c(n,x)^{*}c(n,x)]^{1/2n}$ exists almost everywhere and its eigenvalues $e^{\lambda_1(x)} > \cdots > e^{\lambda_k(x)}$ are the Lyapunov exponents, invariant under $f$ [5]. The proof technique builds the pointwise ergodic theorem into the von Neumann-algebra setting, with the cocycle uniformly bounded and averages $A_n(x,y) = \frac{1}{n}\sum_{k=0}^{n-1}\phi(F^k(x,y))$ converging [5]. For re-entry computation this is the rigorous language for the question the model assumes away: whether the mean re-entry time $t_{\mathrm{re}}$ exists and is stable is a statement about the asymptotic statistics of a dynamical cocycle, and [5] shows both that such statistics can be controlled by ergodic-theoretic hypotheses and that the control requires moment and boundedness conditions that a physical re-entry loop would have to be verified against.

**Regularity as an algebraic lens on loops.** A ring is von Neumann regular if for every $a$ there is a $b$ with $aba = a$; the notion was invented by von Neumann in the 1930s in his study of von Neumann algebras, regular rings are precisely the rings for which every module is flat, and regularity is rare — a group ring $RG$ is regular if and only if $R$ is regular, $G$ is locally finite and the order of every finite subgroup of $G$ is invertible in $R$, while Leavitt path algebras are regular if and only if the defining graph is acyclic [6]. The acyclicity criterion is the sharpest connection to this paper's subject: in an algebra built from a graph, regularity fails exactly when cycles exist, and the re-entry loop is precisely a cycle. If one models a re-entry computation's transition structure as an algebra over its loop graph, [6] indicates that the algebraic fingerprint of the loop is a loss of regularity, suggesting that loop-containing computations resist the flat-module algebraic techniques that work for acyclic (feed-forward, straight-line) computations.

**Embeddings, amenability, and tractability of verification.** For tracial von Neumann algebras, self-tracial stability holds if and only if the algebra is amenable, under the Connes Embedding Problem; amenability is defined by every derivation being inner, hyperfiniteness by expression as the $\sigma$-weak closure of an increasing union of finite-dimensional subalgebras, and the tracial ultraproduct construction with microstates — tuples of matrices approximating operators in many moments — makes embeddings into $R^{\mathcal{U}}$ tractable, since satisfying the Connes Embedding Problem is equivalent to "having sufficiently many microstates" [7]. This bears on the re-entry program as a tractability caveat: certifying that a candidate Hamiltonian loop behaves as modeled is an embedding-and-approximation problem of the microstate type, and [7] shows that the corresponding stability properties collapse to amenability, a strong hypothesis not guaranteed for physical loop dynamics.

**Spectral theory of the averaging operator.** For an ergodic semigroup of linear normal positive unital maps on a von Neumann algebra, the eigenvectors are either multiples of a partial isometry, linear combinations of two partial isometries, or multiples of a unitary operator; and by examples, mere positivity of the maps is not sufficient for the Frobenius theory that holds for completely positive maps, in which the point spectrum of an ergodic semigroup forms a group with one-dimensional eigenspaces spanned by unitaries [8]. The fixed-point space $M_1$ of the semigroup — the eigenspace at eigenvalue $1$ — is where an averaged, time-independent description of a repeatedly re-entering system would live [8]. The warning for the re-entry model is concrete: if the per-pass evolution is merely positive rather than completely positive, the clean convergence-to-a-unique-average picture can fail, with eigenspaces of dimension greater than one, so the assumption that repeated re-entries average to a well-defined steady behavior is a spectral hypothesis, not a formality.

**Rigidity of observable subdynamics.** A countable discrete group $\Gamma$ satisfies the invariant von Neumann subalgebras rigidity (ISR) property if every $\Gamma$-invariant von Neumann subalgebra $\mathcal{M}$ in $L(\Gamma)$ is of the form $L(\Lambda)$ for some normal subgroup $\Lambda \lhd \Gamma$; the property is proved for torsion-free non-amenable hyperbolic groups, using the trace-preserving conditional expectation $\mathbb{E}_{\mathcal{M}}$ and Fourier-coefficient equations [9]. The structural moral for re-entry computation is that the sub-dynamics of a large dynamical system that an observer can actually isolate are rigidly constrained: which intermediate algebras exist inside the full system algebra determines which re-entry loops are even definable as separate computations, and [9] shows this can be a severe restriction in negatively curved systems.

**The prior cost analysis.** The immediate predecessor of this paper constructs the two-model comparison in full: an explicit-controller model with per-operation cost $c_{\mathrm{sw}} = k_{\mathrm{acc}} t_{\mathrm{mem}} + t_{\mathrm{alu}}$ and an autonomous re-entry model with $c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}}$, reporting under the assumptions $k_{\mathrm{acc}} = 4$, $t_{\mathrm{mem}} = 16$, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$ the results $c_{\mathrm{sw}} = 65$, $c_{\mathrm{re}} = 5$, overhead fractions $64/65$ and $0.2$, total-time ratio $13.0$ for $N_{\mathrm{op}} = 10^6$, break-even $t_{\mathrm{mem}}^{*} = 1$, and robustness to $t_{\mathrm{re}}^{*} = 61$ [10]. Its discussion already flags the central weakness: if effective memory time drops to $t_{\mathrm{mem}}^{\mathrm{eff}} = 1$ time unit through caching, the models tie exactly at $c_{\mathrm{sw}} = 4 \times 1 + 1 = 5 = c_{\mathrm{re}}$, so the headline ratio holds only in the memory-bound regime [10]. This paper takes that model as given, re-derives its numbers with the arithmetic shown, and extends it where the prior analysis stopped: at the cache.

## 3. Methods

### 3.1 The two cost models

The formalism is adopted from the prior analysis [10] and restated for completeness.

**Von Neumann switching model.** A stored-program machine executes a program of $N_{\mathrm{op}}$ logical operations. Each operation requires $k_{\mathrm{acc}}$ memory accesses (instruction fetch plus data load/store) before the logical work is done. Let $t_{\mathrm{mem}}$ be the effective time per memory access and $t_{\mathrm{alu}}$ the time for the logical work itself. The per-operation cost is

$$c_{\mathrm{sw}} = k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}},$$

and the total cost is

$$T_{\mathrm{sw}} = N_{\mathrm{op}} \left( k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}} \right).$$

The switching overhead per operation is $k_{\mathrm{acc}}\, t_{\mathrm{mem}}$, with overhead fraction

$$f_{\mathrm{sw}} = \frac{k_{\mathrm{acc}}\, t_{\mathrm{mem}}}{k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}}}.$$

**Hamiltonian re-entry model.** The machine state is a point $x_t$ in phase space evolving under a Hamiltonian $H$. A computation of $N_{\mathrm{op}}$ logical steps corresponds to $N_{\mathrm{op}}$ re-entries of the trajectory into a designated operating region $\mathcal{R} \subset \Omega$. Let $t_{\mathrm{dyn}}$ be the mean time for the trajectory to traverse one useful dynamical segment, and $t_{\mathrm{re}}$ the mean re-entry overhead: the extra time spent steering the trajectory back into $\mathcal{R}$ after each useful segment, including any classical control intervention. The per-re-entry cost is

$$c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}},$$

with total $T_{\mathrm{re}} = N_{\mathrm{op}} (t_{\mathrm{dyn}} + t_{\mathrm{re}})$ and overhead fraction

$$f_{\mathrm{re}} = \frac{t_{\mathrm{re}}}{t_{\mathrm{dyn}} + t_{\mathrm{re}}}.$$

### 3.2 Comparison criterion

The re-entry model beats the switching model on total time when $T_{\mathrm{re}} < T_{\mathrm{sw}}$, i.e. when

$$t_{\mathrm{dyn}} + t_{\mathrm{re}} < k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}}.$$

### 3.3 New methodological elements introduced here

**Cache-aware effective memory time.** To relax the uncached assumption (A2 below), we introduce a two-level memory model. A fraction $h$ (the hit rate) of memory accesses is served by a cache in time $t_{\mathrm{hit}}$; the remaining fraction $1 - h$ is served by main memory in time $t_{\mathrm{mem}}$. The effective memory time is

$$t_{\mathrm{mem}}^{\mathrm{eff}} = h\, t_{\mathrm{hit}} + (1 - h)\, t_{\mathrm{mem}} = t_{\mathrm{mem}} - h\,(t_{\mathrm{mem}} - t_{\mathrm{hit}}),$$

and the cache-aware comparison replaces $t_{\mathrm{mem}}$ by $t_{\mathrm{mem}}^{\mathrm{eff}}$ in $c_{\mathrm{sw}}$. The break-even hit rate $h^{*}$ is the value of $h$ at which $c_{\mathrm{sw}} = c_{\mathrm{re}}$.

**Cross-convention figure of merit.** The prior analysis reports the advantage under two conventions: a time-unit ratio $13.0$ and a cost-unit ratio $R = 3.125$ [10]. To combine them into one scale-free indicator we use the geometric mean $\sqrt{13.0 \times 3.125}$, which is insensitive to which convention is larger and penalizes disagreement between conventions.

**Entropy bookkeeping quantity.** Following the logarithmic form of the entropy functionals discussed in [3], we compute the dimensionless quantity

$$\eta = \ln\!\left(\frac{t_{\mathrm{re}} + t_{\mathrm{dyn}}}{t_{\mathrm{dyn}}}\right),$$

a model construct, not a thermodynamic entropy measurement.

### 3.4 Assumptions

(A1) Both machines perform the same $N_{\mathrm{op}}$ logical operations; the models differ only in update overhead. (A2) In the baseline model, memory accesses are serialized and no caching removes them; the cache-aware extension of Section 3.3 relaxes this with the stated two-level model. (A3) The re-entry overhead $t_{\mathrm{re}}$ is a fixed parameter, not derived from first principles; deriving it from the ergodic theory of the loop cocycle along the lines of [5] is left open. (A4) Mixing is adequate that the mean re-entry time exists; the spectral hypotheses behind such averaging are discussed via [8] in Section 6. (A5) All time and cost values are illustrative assumptions, stated in Section 4; none is a measurement.

## 4. Analysis

Every number in this section is derived from stated inputs. Inputs are of two kinds: structural integers of the model ($k_{\mathrm{acc}}$) and illustrative parameter values stated explicitly as assumptions. The baseline parameter set is taken from the prior analysis [10], which states the assumptions $k_{\mathrm{acc}} = 4$, $t_{\mathrm{mem}} = 16$, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$ and the results derived from them; no value is taken from measurement.

**Input 1 (structural).** $k_{\mathrm{acc}} = 4$ memory accesses per operation: one instruction fetch, one operand load, one store, one next-instruction prefetch. Source: model definition in [10].

**Input 2 (assumed, labeled).** $t_{\mathrm{alu}} = 1$ time unit (normalization). $t_{\mathrm{mem}} = 16$ time units per access, representing a memory hierarchy much slower than the arithmetic unit. $t_{\mathrm{dyn}} = 4$ time units per useful dynamical segment. $t_{\mathrm{re}} = 1$ time unit per re-entry. Source: [10], where all are declared as illustrative assumptions.

**Derivation 1: switching cost per operation.**

$$c_{\mathrm{sw}} = k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}} = 4 \times 16 + 1 = 64 + 1 = 65 \text{ time units}.$$

**Derivation 2: switching overhead fraction.**

$$f_{\mathrm{sw}} = \frac{64}{65} = 0.9846153846\ldots$$

Under the assumed parameters, $100 \times f_{\mathrm{sw}} = 98.4615\ldots\%$ of the stored-program machine's per-operation time is switching overhead.

**Derivation 3: re-entry cost per operation.**

$$c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}} = 4 + 1 = 5 \text{ time units}.$$

**Derivation 4: re-entry overhead fraction.**

$$f_{\mathrm{re}} = \frac{1}{5} = 0.2000.$$

**Derivation 5: total-time comparison for $N_{\mathrm{op}} = 10^{6}$ operations.**

$$T_{\mathrm{sw}} = 10^{6} \times 65 = 6.5 \times 10^{7} \text{ time units},$$
$$T_{\mathrm{re}} = 10^{6} \times 5 = 5.0 \times 10^{6} \text{ time units}.$$

The ratio is

$$\frac{T_{\mathrm{sw}}}{T_{\mathrm{re}}} = \frac{65}{5} = 13.0.$$

**Derivation 6: the break-even memory time.** The re-entry model wins when $c_{\mathrm{re}} < c_{\mathrm{sw}}$. Solve for the memory time $t_{\mathrm{mem}}$ at equality, holding the other assumed values fixed:

$$k_{\mathrm{acc}}\, t_{\mathrm{mem}}^{*} = t_{\mathrm{dyn}} + t_{\mathrm{re}} - t_{\mathrm{alu}} = 4 + 1 - 1 = 4,$$
$$t_{\mathrm{mem}}^{*} = \frac{4}{4} = 1 \text{ time unit}.$$

So under these assumptions the re-entry model wins whenever $t_{\mathrm{mem}} > 1$ time unit, i.e. whenever memory is slower than the arithmetic unit at all.

**Derivation 7: robustness of