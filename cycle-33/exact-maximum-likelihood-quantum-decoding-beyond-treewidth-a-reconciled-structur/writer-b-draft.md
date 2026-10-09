# Exact Maximum-Likelihood Quantum Decoding beyond Treewidth: An Expository and Analytical Study of Rank-Decomposition Dynamic Programming

## Abstract

Maximum-likelihood (ML) decoding is the optimal decoding rule for quantum error correction under stochastic Pauli noise, but exact evaluation of the logical-class probabilities that define it has long been believed to require time exponential in the treewidth of the associated tensor network. The recent Rank-Decomposition Dynamic Programming (Rank DP) algorithm of arXiv:2609.39556v1 [1] shows that the correct graph parameter is instead the rank-width of the Tanner graph with respect to the fault partition, which can be bounded while treewidth grows. This paper provides a self-contained analytical study of that result for an adjacent-field audience. We rederive the decoding partition functions as quadratic sums of powers, give complete worked arithmetic for the three-qubit repetition code including the exact logical-class posterior and the ML threshold, prove that rank-width never exceeds treewidth plus one so Rank DP is never asymptotically worse than tensor-network contraction, and compute explicit floating-point error bounds for the nonnegative realization: with IEEE double precision ($\varepsilon_{\text{mach}} = 2^{-53} \approx 1.11 \times 10^{-16}$) and $10^{6}$ nonnegative accumulation steps the relative error is at most $1.12 \times 10^{-10}$. We situate the result within the broader maximum-likelihood literature, connect the algebraic structure exploited by Rank DP to ultrametric ($p$-adic) classification programs for quantum codes, and discuss failure modes, falsifiability, and open questions.

## 1. Introduction

Quantum error correction protects quantum information by encoding a logical state into a larger physical system and repeatedly measuring error syndromes. Given a syndrome, a decoder must select a recovery operation. The information-theoretically optimal choice is maximum-likelihood decoding: choose the logical class (equivalence class of fault configurations differing by a stabilizer element) with the largest posterior probability under the assumed noise model. Exact ML decoding of general linear codes is NP-hard [9], and for quantum codes the leading exact method — tensor-network contraction of the decoding graph — costs time exponential in the treewidth of the network, which grows with the geometric connectivity of the code.

The paper under study [1] changes the complexity landscape by observing that decoding partition functions with independent local fault factors can be written as quadratic sums of powers, and that such sums admit efficient dynamic programming over a rank-decomposition of the Tanner graph rather than a tree-decomposition. The resulting evaluator is exact, has arithmetic complexity polynomial in the input size and exponential only in the rank-width (with respect to the fault partition), and yields polynomial-time exact ML decoding for punctured quantum Reed–Muller codes and a Steane-concatenated family with growing code distance — instances for which standard tensor-network contraction is superpolynomial.

This paper has three goals. First, to make the core construction accessible to researchers in classical ML and statistical estimation, where likelihood evaluation is a central computational bottleneck with its own rich algorithmic literature [2], [3], [4], [5], [7], [8], [11]. Second, to provide fully explicit derivations — every input number sourced, every arithmetic step shown — of representative results, including a complete worked example and floating-point error bounds. Third, to connect the algebraic viewpoint of [1] to the QNFO program of ultrametric classification of quantum codes [12], [13], [14], arguing that both lines of work point to non-Archimedean and finite-field algebraic structure, rather than geometric locality, as the operative resource for code analysis.

## 2. Background and Related Work

**The target result.** Reference [1] (identical to [10]) introduces Rank DP for quantum ML decoding. The decoder must compute, for each logical class $L$, the partition function $Z_L = \sum_{e \in L} \prod_i w_i(e_i)$, where $w_i$ are independent local fault weights. The key insight is that these sums can be organized as quadratic sums of powers evaluated by dynamic programming along a rank-decomposition of the Tanner graph, with complexity exponential in rank-width rather than treewidth. For punctured quantum Reed–Muller codes and a Steane-concatenated family, Gaussian elimination on the fault structure reduces rank-width to a constant, giving polynomial-time exact decoding where tensor-network contraction is superpolynomial. A nonnegative realization of the recursion yields relative floating-point error bounds, and the exact likelihoods enable noise-parameter learning, rare-event (postselection) probability evaluation, and quantification of optimality gaps of suboptimal decoders.

**Complexity of exact ML decoding.** Reference [9] establishes the framing in which [1] operates: since Berlekamp, McEliece, and van Tilborg, exact ML decoding of general linear codes is NP-hard, yet [9] shows that for expander codes — an asymptotically good LDPC family — exact ML decoding over the binary symmetric channel becomes tractable. This is the classical precedent for the central theme of [1]: hardness of ML decoding is not uniform across code families, and structural properties of specific families can collapse the complexity. Rank DP identifies rank-width as the property that does the collapsing for quantum codes with algebraically factorizable fault structure.

**Structure-exploiting exact decoding in classical coding.** Reference [6] gives an algorithm for exact ML decoding of polar codes over the binary erasure channel, using matrix triangulation of the sparse parity-check matrix followed by solving a small linear system over $\mathrm{GF}(2)$, with belief propagation assisting the triangulation. The parallel with [1] is direct: both replace generic exponential search with algebraic preprocessing (triangulation there, Gaussian elimination on the fault partition here) that exposes a low-complexity evaluation path. Both results support the thesis that "exact ML" is a family of problems whose difficulty is governed by algebraic, not merely combinatorial, structure.

**Likelihood evaluation as a computational bottleneck in statistics.** The statistical literature has independently developed the theme that exact or near-exact likelihood evaluation can be accelerated by exploiting model structure. Reference [3] shows that while computing the likelihood of an ARMA model requires $O(n)$ flops per evaluation, a likelihood-based AR approximation reduces repeated evaluations to $O(1)$ flops each, with results identical or very close to the exact likelihood. Reference [7] proves that a complete finite-sample likelihood theory survives for drifted multi-sub-fractional Brownian motion at discrete observation, despite the absence of Toeplitz covariance structure or spectral density — a structural obstacle analogous to the loss of geometric locality that defeats tensor-network methods. Reference [2] obtains consistency and strong consistency of ML estimators for drift fractional Brownian motion using Malliavin calculus, illustrating how sophisticated stochastic analysis can substitute for naive likelihood computation. Reference [4] constructs a trigonometrically approximated ML estimator for $\alpha$-stable laws by projecting the score function onto a trigonometric basis, making the approximated likelihood equation explicit. Reference [5] derives a simpler, more direct asymptotic distribution for the exact ML unit-root test statistic and uses response-surface regression for fast computation. Reference [8] critically reviews quasi-ML estimation of high-dimensional factor models, including Kalman-smoother and EM-based approaches — a reminder that when exact likelihoods are infeasible, the field falls back on approximations whose statistical properties require careful audit, precisely the gap that exact evaluators such as [1] eliminate for quantum decoding. Reference [11] bounds the risk of the ML estimator of connection probabilities in sparse network models with missing observations, another instance where ML is well-defined but its computation and statistical behavior hinge on latent structure.

**Ultrametric classification of quantum codes.** The QNFO program [12] connects $p$-adic valuation theory, Mahler spectral expansions, Kodaira–Néron fiber classification, and the Amice transform to the classification of quantum error-correcting codes, with three conjectures, fourteen lemmas, and computational verification across four code families at 83% classification accuracy. Follow-up work [13] tests the Mahler spectral conjecture on eight additional stabilizer code families, confirming $v_p^{\max} = 28$ for the Golay CSS code while other stabilizer codes cluster at a random baseline of 1–6, binding conjecture C7.3 to Golay-type self-dual codes. The umbrella paper [14] argues that five independent QNFO research programs converge on a single structural insight: ultrametric (non-Archimedean) mathematics provides the correct state-space geometry for fundamental physics, quantum computation, and optimization. Rank DP [1] is naturally read in this light: its complexity parameter, rank-width over $\mathrm{GF}(2)$, is a finite-field (hence non-Archimedean) cut-rank function, and its polynomial-time families (Reed–Muller, Steane-concatenated) are exactly codes with deep finite-field hierarchical structure. The connection is suggestive rather than theorem-level, and we flag it as such in Section 6.

## 3. Methods

### 3.1 Decoding as partition-function evaluation

Let a quantum code have stabilizer group $S$, and let a fault configuration be a binary vector $e \in \{0,1\}^{n}$ (for one Pauli component; the full Pauli case factors across components). Under independent single-qubit noise with fault probability $p$, the likelihood of $e$ is

$$
\Pr(e) = p^{|e|} (1-p)^{n - |e|} = \prod_{i=1}^{n} w_i(e_i), \qquad w_i(0) = 1-p, \quad w_i(1) = p .
$$

Fault configurations split into logical classes $L_0, L_1, \dots$ according to their action on the encoded qubits modulo the stabilizer. The ML decoder selects $\arg\max_L Z_L$ where

$$
Z_L = \sum_{e \in L} \prod_{i=1}^{n} w_i(e_i).
$$

Because classes are cosets of the stabilizer, $Z_L = Z_{L_0} \cdot R_L$ where $R_L$ is a coset sum; computing all $Z_L$ reduces to computing base partition functions of quadratic-sum-of-powers form. The construction of [1] writes each $Z_L$ as

$$
Z_L = \sum_{x \in \{0,1\}^{k}} \Big( \sum_{j} c_j \, \beta_j(x)^{2} \Big)^{m_j}
$$

for suitable coefficients $c_j$, exponents $m_j$, and local linear forms $\beta_j$ — a "quadratic sum of powers" — and evaluates it by dynamic programming over a rank-decomposition.

### 3.2 Rank-width and the cut-rank function

For a graph $G = (V, E)$ and a vertex subset $S \subseteq V$, the cut-rank is

$$
\rho_G(S) = \operatorname{rank}_{\mathrm{GF}(2)} A_G[S, \bar{S}],
$$

the rank over the two-element field of the biadjacency matrix across the cut $(S, \bar{S})$. A rank-decomposition is a subtree $T$ with leaves bijecting $V$; its width is $\max_{e \in E(T)} \rho_G(V_e)$ where $V_e$ is the leaf set of one component of $T - e$. The rank-width $\mathrm{rw}(G)$ is the minimum such width. The Rank DP of [1] processes $T$ bottom-up, combining boundary states of size at most $2^{\mathrm{rw}(G)}$ per bag, giving arithmetic complexity

$$
T_{\text{RankDP}} = n^{O(1)} \cdot 2^{O(\mathrm{rw}(G))}
$$

including decomposition construction, polynomial in input size whenever $\mathrm{rw}(G)$ is $O(\log n)$.

### 3.3 Comparison parameter: treewidth

Tensor-network contraction costs $2^{O(\mathrm{tw})}$ where $\mathrm{tw}$ is treewidth of the decoding graph. We use the standard inequality (proved in Section 4) that $\mathrm{rw}(G) \le \mathrm{tw}(G) + 1$, so Rank DP is never asymptotically worse, and is strictly better on families where rank-width is bounded but treewidth grows.

### 3.4 Numerical realization

The nonnegative realization of [1] evaluates the recursion using only additions and multiplications of nonnegative reals. If each arithmetic op incurs relative error at most $\varepsilon_{\text{mach}}$ and the evaluation performs $N$ accumulation steps, the propagated relative error satisfies a standard product bound, computed explicitly in Section 4.

## 4. Analysis

All numbers in this section are either standard constants, derived here step by step, or explicitly labeled projections with stated assumptions.

### 4.1 Worked example: three-qubit repetition code

Take the classical repetition code of length $n = 3$ embedded in the decoding problem (the $[[3,1]]$-type repetition layer of a CSS code), with independent bit-flip probability $p = 0.1$ (an assumed, stated channel parameter). Logical class $0$ = even-weight faults, class $1$ = odd-weight faults.

Class $0$ configurations: weights $0$ and $2$.

$$
Z_0 = (1-p)^{3} + \binom{3}{2} p^{2}(1-p).
$$

Arithmetic: $(1 - 0.1)^{3} = 0.9^{3} = 0.729$. Next, $\binom{3}{2} = 3$; $p^{2} = 0.1^{2} = 0.01$; $p^{2}(1-p) = 0.01 \times 0.9 = 0.009$; $3 \times 0.009 = 0.027$. Hence

$$
Z_0 = 0.729 + 0.027 = 0.756 .
$$

Class $1$ configurations: weights $1$ and $3$.

$$
Z_1 = \binom{3}{1} p (1-p)^{2} + p^{3}.
$$

Arithmetic: $p(1-p)^{2} = 0.1 \times 0.81 = 0.081$; $3 \times 0.081 = 0.243$; $p^{3} = 0.001$. Hence

$$
Z_1 = 0.243 + 0.001 = 0.244 .
$$

Sanity check: $Z_0 + Z_1 = 0.756 + 0.244 = 1.000$, as required since the classes partition all $2^{3} = 8$ fault configurations. The ML posterior of class $0$ is

$$
\Pr(L_0 \mid \text{syndrome-free}) = \frac{Z_0}{Z_0 + Z_1} = \frac{0.756}{1.000} = 0.756 .
$$

The ML threshold is where $Z_0 = Z_1$. For the length-$n$ repetition code, $Z_0 = \sum_{j \text{ even}} \binom{n}{j} p^{j}(1-p)^{n-j}$ and $Z_1$ the odd sum; both equal $\tfrac{1}{2}$ exactly when $p = \tfrac{1}{2}$ by the binomial symmetry $\binom{n}{j} = \binom{n}{n-j}$, so the exact ML threshold is $p^{\ast} = 0.5$, independent of $n$ — a trivial but fully verified instance of exact likelihood evaluation of the type Rank DP automates at scale.

### 4.2 Rank-width versus treewidth

**Claim.** For any graph $G$, $\mathrm{rw}(G) \le \mathrm{tw}(G) + 1$.

*Derivation.* Let $(T, \mathcal{B})$ be a tree-decomposition of $G$ of width $\mathrm{tw}$, so every bag has $|\mathcal{B}_t| \le \mathrm{tw} + 1$ vertices. Construct a rank-decomposition whose decomposition tree is $T$ by attaching each vertex $v \in V$ to the leaf of $T$ corresponding to a bag containing $v$ (standard bag-to-leaf assignment). For an edge $e$ of $T$, the cut $(V_e, \bar{V}_e)$ separates leaf sets; every edge of $G$ crossing this cut has both endpoints in the bag(s) along the boundary, and the biadjacency matrix $A_G[V_e, \bar{V}_e]$ is a submatrix of the bag adjacency structure of size at most $(\mathrm{tw}+1) \times (\mathrm{tw}+1)$. The $\mathrm{GF}(2)$-rank of a matrix is at most its smaller dimension, so

$$
\rho_G(V_e) \le \min(|V_e \cap N(\bar{V}_e)|, |\bar{V}_e \cap N(V_e)|) \le \mathrm{tw} + 1 .
$$

Hence the induced rank-decomposition has width at most $\mathrm{tw} + 1$, i.e. $\mathrm{rw}(G) \le \mathrm{tw}(G) + 1$. $\blacksquare$

Consequence: the Rank DP complexity $n^{O(1)} \cdot 2^{O(\mathrm{rw})}$ never exceeds the tensor-network complexity $2^{O(\mathrm{tw})}$ up to polynomial factors, and strictly beats it on the families of [1] where $\mathrm{rw}$ is constant after Gaussian elimination but $\mathrm{tw} = \omega(1)$.

### 4.3 Floating-point error bound

Assumption (from [1], nonnegative realization): each of $N$ accumulation operations introduces relative error at most $\varepsilon_{\text{mach}}$; all intermediate values are nonnegative, so no cancellation amplification occurs. The standard product bound gives

$$
\frac{|\hat{Z} - Z|}{Z} \le (1 + \varepsilon_{\text{mach}})^{N} - 1 \le N \, \varepsilon_{\text{mach}} \quad \text{for } N \varepsilon_{\text{mach}} \ll 1 .
$$

Inputs: $\varepsilon_{\text{mach}} = 2^{-53}$ (IEEE 754 double precision). Compute $2^{-53}$: $2^{10} = 1024 \approx 10^{3}$, so $2^{-53} = 2^{-3} \cdot 2^{-50} = \tfrac{1}{8} \cdot (2^{-10})^{5} \approx \tfrac{1}{8} \cdot 10^{-15} = 1.25 \times 10^{-16}$; the exact value is $2^{-53} = 1.1102230246251565 \times 10^{-16}$.

For $N = 10^{6}$ accumulation steps:

$$
N \varepsilon_{\text{mach}} = 10^{6} \times 1.1102230246251565 \times 10^{-16} = 1.1102230246251565 \times 10^{-10} .
$$

The exact bound $(1 + \varepsilon)^{N} - 1$ exceeds $N\varepsilon$ by a second-order correction $\binom{N}{2}\varepsilon^{2} \approx \tfrac{N^{2}\varepsilon^{2}}{2} = \tfrac{10^{12} \times 1.2326 \times 10^{-32}}{2} = 6.16 \times 10^{-21}$, negligible. So the relative error is at most

$$
1.12 \times 10^{-10} \quad (N = 10^{6}), \qquad \text{and} \quad 1.12 \times 10^{-7} \quad (N = 10^{9}),
$$

the latter computed as $10^{9} \times 1.1102 \times 10^{-16} = 1.1102 \times 10^{-7}$. These bounds certify that the exact likelihoods used for downstream tasks in [1] (noise learning, rare-event evaluation) are numerically trustworthy at double precision for realistic operation counts.

### 4.4 Complexity projection for the Steane-concatenated family

Projection with stated assumptions. The Steane $[[7,1,3]]$ code concatenated $t$ times has $n = 7^{t}$ qubits and distance $d = 3^{t}$. Assume (as in [1]) that after Gaussian elimination on the fault partition the rank-width is bounded by a constant $k_{\ast}$ independent of $t$, and that the Rank DP constant-factor cost is $c \cdot n \cdot 2^{k_{\ast}}$ arithmetic operations with $c = 10$ and $k_{\ast} = 4$ (illustrative constants, not measured). Then for $t = 3$ ($n = 343$, $d = 27$):

$$
T_{\text{RankDP}} = 10 \times 343 \times 2^{4} = 10 \times 343 \times 16 = 54{,}880 \text{ ops}.
$$

For $t = 5$ ($n = 16{,}807$, $d = 243$):

$$
T_{\text{RankDP}} = 10 \times 16{,}807 \times 16 = 2{,}688{,}912 \text{ ops} \approx 2.69 \times 10^{6}.
$$

By contrast, a tensor network whose treewidth grows linearly in $t$, say $\mathrm{tw} = 2t$, would cost $2^{2t}$ boundary combinations: for $t = 5$, $2^{10} = 1024$ combinations per bond dimension unit — superpolynomial in $t$ once bond dimensions are included, versus the linear-in-$n$ Rank DP count above. These are structural projections under stated assumptions, not benchmark measurements; [1] reports runtime advantages empirically on selected instances, which we do not reproduce.

## 5. Results

**R1 (Worked exact likelihoods).** For the three-qubit repetition code at $p = 0.1$: $Z_0 = 0.756$, $Z_1 = 0.244$, $\Pr(L_0) = 0.756$, with the partition verified ($Z_0 + Z_1 = 1.000$). The exact ML threshold is $p^{\ast} = 0.5$ for all lengths $n$, proved by binomial symmetry.

**R2 (Parameter dominance).** $\mathrm{rw}(G) \le \mathrm{tw}(G) + 1$ for all graphs $G$, derived in Section 4.2. Consequently Rank DP [1] is never asymptotically worse than tensor-network contraction and is strictly superior (exponential in a constant versus exponential in a growing parameter) on the punctured Reed–Muller and Steane-concatenated families.

**R3 (Numerical certification).** Under the nonnegative realization with IEEE double precision ($\varepsilon_{\text{mach}} = 1.1102230246251565 \times 10^{-16}$): relative error $\le 1.12 \times 10^{-10}$ for $N = 10^{6}$ accumulation steps and $\le 1.12 \times 10^{-7}$ for $N = 10^{9}$ steps, computed in Section 4.3.

**R4 (Projected operation counts, labeled projections).** Under the stated illustrative assumptions ($c = 10$, $k_{\ast} = 4$, bounded rank-width after elimination): $T_{\text{RankDP}} = 54{,}880$ ops for the $t=3$ Steane-concatenated code ($n = 343$, $d = 27$) and $\approx 2.69 \times 10^{6}$ ops for $t = 5$ ($n = 16{,}807$, $d = 243$). Uncertainty: these scale linearly in $n$ and in the constants $c, 2^{k_{\ast}}$; if the true rank-width after elimination is $k_{\ast} \le 8$, the counts multiply by at most a factor $2^{8}/2^{4} = 16$, i.e. remain under $4.4 \times 10^{7}$ ops for $t = 5$. No empirical runtimes are claimed here; empirical advantages over tested tensor-network implementations are reported in [1] itself.

## 6. Discussion

**Limitations.** First, our quantitative results beyond R1–R3 are projections under illustrative constants; the honest empirical content of [1] — runtime wins on selected code-capacity and circuit-level instances, full likelihood evaluation for Reed–Muller codes up to $1{,}023$ qubits — is reported by the original authors and not independently verified here. Second, the rank-width bound after Gaussian elimination is established in [1] for specific families (punctured quantum Reed–Muller, Steane-concatenated); whether broad code classes of practical interest (e.g., surface codes at circuit level) admit bounded fault-partition rank-width is open, and for generic LDPC-like Tanner graphs rank-width can itself be large, recovering exponential complexity. Third, the bibliography available for this preprint is dominated by maximum-likelihood estimation in statistics and time series [2]–[8], [11]; the analogies drawn in Section 2 are structural, not theorem-level transfers.

**Failure modes.** The nonnegative realization's error bound relies on absence of cancellation; if an implementation rewrites the recursion with signed intermediates (e.g., for speed), the $N\varepsilon_{\text{mach}}$ bound is void and catastrophic cancellation is possible when $Z_L$ is a small difference of large sums — exactly the rare-event regime the method targets. Decomposition construction is included in the complexity claim of [1], but heuristic rank-decomposition algorithms can fail to find the optimal width on unfamiliar graphs, silently degrading to exponential behavior; a practitioner without a width certificate cannot distinguish "hard instance" from "bad decomposition."

**What would falsify the claims.** R2 is a theorem and is falsified only by an error in the derivation of Section 4.2 (a counterexample graph with $\mathrm{rw} > \mathrm{tw} + 1$). The practical significance claim would be falsified if the constant factors of Rank DP, or the cost of constructing good rank-decompositions in practice, dominate so heavily that tensor-network contraction wins on all instances of interest despite the asymptotic advantage. The algebraic-structure thesis would be weakened if the polynomial-time families of [1] proved to be isolated curiosities with no common generalization.

**Arguing against ourselves.** One may object that ML decoding is rarely the binding constraint in practice: near-optimal decoders (union-bound, belief propagation with matching) suffice below threshold, and the optimality gaps measured via exact likelihoods in [1] may be negligible at operating points of interest. If so, exact evaluation is a diagnostic tool, not a deployment tool — valuable for noise characterization and decoder auditing, but not for the decoding hot path. We accept this framing partially: the noise-learning and rare-event applications of [1] are uses that approximations cannot certify, so even under this objection the exact evaluator retains distinct value.

**Connection to ultrametric structure.** The QNFO program [12], [13], [14] holds that non-Archimedean mathematics is the correct geometry for quantum code classification, with [13] finding sharp structure ($v_p^{\max} = 28$) only for Golay-type self-dual codes and random-baseline behavior elsewhere. Rank DP exhibits a parallel selectivity: algebraic structure collapses complexity for Reed–Muller and concatenated families, while generic graphs retain hardness [9]. Both programs suggest that "which code families are special" is answered by finite-field algebra rather than geometry. A concrete open question is whether the cut-rank function $\rho_G$ of Section 3.2 admits a $p$-adic or valuation-theoretic refinement aligned with the Mahler spectral invariants of [12], which could turn the suggestive analogy into a predictive classification tool: codes with low ultrametric complexity might be provably low rank-width, hence exactly decodable.

**Open questions.** (i) Tighten the relationship between fault-partition rank-width and code distance for concatenated families: is bounded rank-width compatible with $d \to \infty$ at constant rate? (ii) Do the statistical-estimation acceleration techniques [3], [4], [5] transfer to the noise-learning application of [1], e.g., $O(1)$-cost likelihood re-evaluations across a parameter sweep? (iii) Can the high-dimensional quasi-ML machinery [8] and missing-data risk bounds [11] formalize the syndrome-based noise learning as a well-posed estimation problem with known risk?

## 7. Conclusion

We have provided an analytical exposition of Rank-Decomposition Dynamic Programming for exact maximum-likelihood quantum decoding [1], with complete worked derivations: exact logical-class likelihoods for the three-qubit repetition code ($Z_0 = 0.756$, $Z_1 = 0.244$ at $p = 0.1$), the theorem $\mathrm{rw}(G) \le \mathrm{tw}(G) + 1$ establishing that Rank DP dominates tensor-network contraction asymptotically, certified floating-point error bounds ($\le 1.12 \times 10^{-10}$ relative for $10^{6}$ double-precision accumulations), and clearly labeled projected operation counts for Steane-concatenated instances. Situating the result among exact and approximate ML methods in coding theory [6], [9] and statistical estimation [2]–[5], [7], [8], [11], and connecting it to the ultrametric classification program [12]–[14], we conclude that the operative resource for exact decoding is algebraic — finite-field rank structure — rather than geometric locality. The principal open challenge is breadth: determining how far beyond the known polynomial-time families the rank-width collapse extends.

## References

[1] arXiv Query: search_query=&id_list=2609.39556&start=0&max_results=1 — "Exact Maximum Likelihood Decoding beyond Treewidth via Rank-Decomposition Dynamic Programming" (arXiv:2609.39556v1).

[2] arXiv:0904.4186v1 | Exact maximum likelihood estimators for drift fractional Brownian motions

[3] arXiv:1611.00965v1 | Faster ARMA maximum likelihood estimation

[4] arXiv:2209.08980v1 | Trigonometrically approximated maximum likelihood estimation for stable law

[5] arXiv:1611.00819v1 | Developments in Maximum Likelihood Unit Root Tests

[6] arXiv:2106.14753v1 | Efficient Maximum Likelihood Decoding of Polar Codes Over the Binary Erasure Channel

[7] arXiv:2609.22617v1 | Exact maximum likelihood inference for drifted multi-sub-fractional Brownian motion at discrete observation

[8] arXiv:2303.11777v5 | Quasi Maximum Likelihood Estimation of High-Dimensional Factor Models: A Critical Review

[9] arXiv:cs/0702147v1 | On the Complexity of Exact Maximum-Likelihood Decoding for Asymptotically Good Low Density Parity Check Codes

[10] arXiv:2609.39556v1 | Exact Maximum Likelihood Decoding beyond Treewidth via Rank-Decomposition Dynamic Programming

[11] arXiv:1902.10605v2 | Maximum Likelihood Estimation of Sparse Networks with Missing Observations

[12] QNFO: Number-Theoretic Ultrametric Foundations: A Unified p-adic Framework for Error-Correcting Code Classification | DOI 10.5281/zenodo.21193487

[13] QNFO: Extending v_p^max Code Classification: Testing the Mahler Spectral Conjecture on Additional Stabilizer Code Families | DOI 10.5281/zenodo.21754148

[14] QNFO: Five Pillars, One Structure: Consilient Convergence in QNFO Research | DOI 10.5281/zenodo.21603374