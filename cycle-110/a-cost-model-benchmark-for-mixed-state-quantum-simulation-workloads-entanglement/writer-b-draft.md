# A Re-Entry Benchmark for Entanglement Cost of Two-Bell-State Mixtures: Explicit Arithmetic and a Protocol for Scaling to More Complex Mixed States

## Abstract

We construct a re-entry benchmark for entanglement-cost computations on bipartite mixed states, designed as a continuation point for work registered at the Zenodo record 10.5281/zenodo.18228311 and aimed at future extensions to more complex mixed states. The benchmark family is the two-parameter-free mixture $\rho_p = p\,|\Phi^+\rangle\langle\Phi^+| + (1-p)\,|\Phi^-\rangle\langle\Phi^-|$, supported on a two-dimensional Bell subspace. For states supported on subspaces spanned by specific Bell-state sets, the entanglement of formation is additive, so the asymptotic entanglement cost equals the single-copy entanglement of formation; we adopt this as the benchmark metric. We derive the concurrence $C(\rho_p) = |2p-1|$ from the spectrum of $\rho_p \tilde{\rho}_p$ and compute the cost $E_F(\rho_p) = h_2\!\big(\tfrac{1}{2}+\sqrt{p(1-p)}\big)$ with fully shown arithmetic at $p \in \{0.50, 0.75, 0.90, 0.99\}$, obtaining $0$, $0.354618$, $0.721928$, and $0.970582$ ebits per copy respectively. We further derive the mixing threshold $p^\ast \approx 0.6132$ at which the cost first reaches $0.1$ ebits per copy, and the $N$-copy preparation budget $N \cdot E_F(\rho_p)$. The benchmark packages these derivations as a reproducible checklist, and we discuss precisely where the additivity argument can be expected to fail as state complexity grows.

## 1. Introduction

Entanglement is the central resource of quantum information science, and the entanglement cost of a mixed state — the asymptotic rate at which maximally entangled pairs must be consumed to prepare many copies of the state by local operations and classical communication — is one of its fundamental measures. The research idea underlying this paper is a re-entry from the Zenodo record 10.5281/zenodo.18228311: that record is to serve as a benchmark for future work on more complex mixed states. The present paper operationalizes that re-entry by building an explicit, arithmetically transparent benchmark on the simplest nontrivial mixed-state family for which the entanglement cost is exactly known: mixtures of two Bell states.

The choice of family is deliberate. For arbitrary mixtures of two Bell states, the entanglement cost has been computed in the literature by developing a technique that ascertains the additivity of the entanglement of formation for any state supported on specific subspaces [5]. This gives the benchmark two properties that a re-entry baseline needs: (i) the ground-truth value of the metric is exactly computable by hand, so any future automated pipeline can be checked against it; and (ii) the family sits at the boundary of the known territory — one step beyond it lie mixed states supported on higher-dimensional subspaces, where additivity is not guaranteed. The benchmark therefore functions both as a correctness test and as a starting line.

Our contributions are:

1. A precise definition of the benchmark state family $\rho_p$, its metric (entanglement cost per copy, equal to the entanglement of formation $E_F$ under the subspace additivity result of [5]), and a closed-form expression $E_F(\rho_p) = h_2\!\big(\tfrac{1}{2}+\sqrt{p(1-p)}\big)$ derived from the concurrence.
2. Fully explicit arithmetic for a grid of mixing parameters, including the separable point $p = 0.5$, the strongly mixed point $p = 0.75$, and near-unit-entanglement points $p = 0.90$ and $p = 0.99$.
3. A derived threshold $p^\ast \approx 0.6132$: the smallest mixing bias at which the state costs at least $0.1$ ebits per copy, useful as a sensitivity marker for benchmark pipelines.
4. A scaling rule for $N$-copy workloads, $N_{\text{pairs}}(p, N) = N \cdot E_F(\rho_p)$, connecting the benchmark to repeated-run resource accounting.

Throughout, every number is either derived with shown arithmetic in Section 4 or explicitly labeled a projection with stated assumptions. We cite only the supplied bibliography, and where a bibliography entry is thin we say so explicitly.

## 2. Background and Related Work

We discuss the supplied bibliography in its exact numbering. Because the bibliography mixes quantum information with functional analysis, control theory, complex analysis, and quantum-computing systems work, we use each entry only for what its own summary supports, and we state explicitly when an entry is methodologically adjacent rather than topically central.

[5] (arXiv:quant-ph/0112131v4, *Entanglement cost of mixed states*) is the central reference. Its summary states that the authors compute the entanglement cost of several families of bipartite mixed states, including arbitrary mixtures of two Bell states, via a technique that ascertains the additivity of the entanglement of formation for any state supported on specific subspaces; as a side result, the proof of irreversibility in asymptotic local manipulations of entanglement is given. Our benchmark is built directly on the first of these results: the state family $\rho_p$ is an arbitrary mixture of two Bell states, so its cost is exactly its entanglement of formation. The second result — irreversibility of asymptotic local manipulations — motivates our choice of cost (rather than distillable entanglement) as the benchmark metric, since the two directions of manipulation need not coincide.

[6] (arXiv:2106.03448v6), [1] (arXiv:2108.10792v1), and [4] (arXiv:2207.11778v3) form a three-part series on Hilbert complexes with mixed boundary conditions. Part 1 [6] shows that the de Rham Hilbert complex with mixed boundary conditions on bounded strong Lipschitz domains is closed and compact, with the crucial results being compact embeddings that follow by abstract functional-analytic arguments together with particular regular decompositions, and higher Sobolev order results proved as well. Part 2 [1] establishes the same closedness-and-compactness program for the elasticity complex, again via compact embeddings from abstract arguments plus particular regular decompositions, extending recent results on the de Rham Hilbert complex. Part 3 [4] does the same for biharmonic complexes, extending the authors' results on the de Rham and (per its summary) related complexes. The methodological analogy to our work is structural: each of these papers proves a global property (compactness) by combining an abstract theorem with a carefully chosen decomposition of the object of study — regular decompositions of fields, in their case; subspace decompositions of density matrices, in ours. Our benchmark inherits this "decompose, then apply the abstract result" pattern, and the series is a useful reminder that decomposition-based proofs typically come with an explicit domain of validity (there, Lipschitz domains and boundary conditions; here, the specific subspaces of [5]).

[2] (arXiv:2610.06654v1, *Continuous-Time Estimation-Aware Optimal Control of Mobile Sensors for Target Tracking*) addresses target tracking — estimating the state of a target system from measurements collected by mobile sensors — and proposes an estimation-aware optimal control method in which trajectory optimization accounts not only for dynamical and operational constraints but also for uncertainty in estimating the target's state. The analogy for benchmark design is that resource expenditure (sensor trajectories there, entanglement consumption here) should be planned against an explicit uncertainty model rather than treated as a fixed overhead; our $N$-copy budget rule in Section 4.4 is the analogous "planning against the resource model" step.

[3] (arXiv:math/0306324v1, *Ullemar's formula for the Jacobian of the complex moment mapping*) assigns the complex moment sequence $m(P)$ to a univalent polynomial $P$ by the Cauchy transform of $P(D)$, where $D$ is the unit disk, establishes a representation of the Jacobian $\det dm(P)$ in terms of the roots of the derivative $P'$, and — combining this with a special decomposition for the Hurwitz determinants — proves a Jacobian formula previously conjectured by C. Ullemar. This is a precedent for the style of result we package in the benchmark: an explicit closed-form formula for a derived quantity, obtained by combining a representation result with a decomposition. Our closed form $E_F(\rho_p) = h_2\!\big(\tfrac{1}{2}+\sqrt{p(1-p)}\big)$ plays the same role at much smaller scale.

[7] (arXiv:2112.12972v2, *Holomorphic maps from complex discs intersecting families of hypersurfaces*) establishes second main theorems for holomorphic maps with finite growth index on complex discs intersecting families of hypersurfaces (moving and fixed) in projective varieties, with a detailed small-term estimate for various cases, generalizing previous second main theorems for maps from $\mathbb{C}$. Its relevance is the presence of explicit estimates with case analysis — the same discipline of stating for which cases an estimate holds that we apply when we restrict our additivity-based cost identity to the two-Bell-state subspace.

[8] (arXiv:1612.04764v1, *Cohomological aspects on complex and symplectic manifolds*) discusses how quantitative cohomological information can provide qualitative properties of complex and symplectic manifolds, focusing on the Bott-Chern and Aeppli cohomology groups as tools in non-Kähler geometry, with an overview of comparisons among the dimensions of the definable cohomology groups. The parallel is the general theme that a quantitative invariant (there, dimensions of cohomology groups; here, ebits of cost) can serve as a proxy for qualitative structure (there, non-Kähler behavior; here, separability versus entanglement, marked by the threshold $p^\ast$).

[9] (QNFO: *QuWARP Reconciled*) observes that classical simulation of quantum circuits increasingly appears as repeated-run workloads — variational quantum eigensolver (VQE) sweeps, noisy multishot studies, and quantum error-correction (QEC) cycles — rather than isolated circuit executions, and that the QuWARP planner (arXiv:2609.23664v1) proposes workload-level reuse planning (the supplied summary is truncated at this point, so we do not attribute further specifics to it). This motivates our $N$-copy formulation: entanglement preparation for mixed-state benchmarks is naturally a repeated-run workload, and cost should be reported per-copy and per-workload.

[10] (QNFO: *Thermodynamic Budgeting for Hybrid Quantum-Classical Computing*) proposes a three-layer energy model with explicit arithmetic and a 15-month validation roadmap, arguing that energy accounting in hybrid quantum-classical computing is rarely made explicit because the classical control, readout, cryogenic, and orchestration hardware surrounding the QPU can dominate the total power budget. This is the closest systems-level precedent for our paper's core discipline: making every unit of resource accounting explicit and arithmetically checkable, and pairing the model with a validation plan — which our benchmark checklist in Section 3.3 is.

[11] (QNFO: *Spectral Benchmarking of Holographic Quantum Simulations*) and [12] (QNFO: *Structural vs Driven Quantum Coherence*) have empty summaries in the supplied bibliography; the summaries give no further detail, so we relate them to our argument only through their titles: both name benchmarking and coherence-characterization themes adjacent to mixed-state resource benchmarking, and we make no claims about their contents.

With twelve works cited, of which two carry no usable summary and several are methodological rather than topical, the literature base for this benchmark is narrow; we return to this in Section 6.

## 3. Methods

### 3.1 Benchmark state family

Let $\{|\Phi^+\rangle, |\Phi^-\rangle, |\Psi^+\rangle, |\Psi^-\rangle\}$ be the Bell basis of $\mathbb{C}^2 \otimes \mathbb{C}^2$, with $|\Phi^\pm\rangle = (|00\rangle \pm |11\rangle)/\sqrt{2}$. The benchmark family is the one-parameter mixture

$$\rho_p = p\,|\Phi^+\rangle\langle\Phi^+| + (1-p)\,|\Phi^-\rangle\langle\Phi^-|, \qquad p \in [0,1].$$

This is an "arbitrary mixture of two Bell states" in the sense of [5], supported on the two-dimensional subspace $\mathcal{S}_{\Phi} = \mathrm{span}\{|\Phi^+\rangle, |\Phi^-\rangle\}$. The parameter $p$ interpolates between the maximally entangled Bell state ($p=1$ or $p=0$) and the separable incoherent mixture ($p = 0.5$).

### 3.2 Benchmark metric

The entanglement cost $E_C(\rho)$ of a bipartite state $\rho$ is the asymptotic rate, in ebits per copy, at which maximally entangled pairs are consumed to prepare copies of $\rho$ by local operations and classical communication. By the additivity result of [5] for states supported on specific subspaces, which includes arbitrary mixtures of two Bell states,

$$E_C(\rho_p) = E_F(\rho_p),$$

where $E_F$ is the entanglement of formation. For two-qubit states, $E_F$ is given in closed form through the concurrence $C(\rho)$:

$$E_F(\rho) = h_2\!\left(\frac{1 + \sqrt{1 - C(\rho)^2}}{2}\right), \qquad h_2(x) = -x\log_2 x - (1-x)\log_2(1-x),$$

where $h_2$ is the binary entropy and the concurrence is $C(\rho) = \max\big(0,\, 2\sqrt{\lambda_{\max}} - 1\big)$ with $\lambda_{\max}$ the largest eigenvalue of $\rho\tilde{\rho}$, $\tilde{\rho} = (\sigma_y \otimes \sigma_y)\,\rho^\ast\,(\sigma_y \otimes \sigma_y)$ the spin-flipped state, and $\rho^\ast$ entrywise complex conjugation. We use this closed form as the definition of the benchmark metric; its consistency with $E_F$ is the standard two-qubit identity, and the cost identity $E_C = E_F$ is supplied by [5].

### 3.3 Benchmark checklist (re-entry protocol)

A future pipeline targeting more complex mixed states re-enters the benchmark by: (i) reproducing the concurrence derivation of Section 4.1; (ii) reproducing the grid values of Section 4.2 to at least $10^{-5}$ ebits; (iii) reproducing the threshold $p^\ast$ of Section 4.3; and (iv) reporting $N$-copy budgets per Section 4.4. Any candidate method extending beyond $\mathcal{S}_{\Phi}$ must additionally state its analogue of the subspace additivity condition of [5], since outside that condition the identity $E_C = E_F$ is not guaranteed and irreversibility effects [5] may separate cost from distillable entanglement.

## 4. Analysis

Every input number below is either a definition (the mixing parameter $p$), a mathematical constant, or a value derived in an earlier subsection. All logarithms in numerical work are natural logs converted by $\log_2 x = \ln x / \ln 2$ with $\ln 2 = 0.693147$.

### 4.1 Concurrence of $\rho_p$

In the Bell basis $\mathcal{B} = (|\Phi^+\rangle, |\Phi^-\rangle, |\Psi^+\rangle, |\Psi^-\rangle)$, the state is diagonal:

$$\rho_p\big|_{\mathcal{B}} = \mathrm{diag}(p,\; 1-p,\; 0,\; 0).$$

The spin-flip operator acts diagonally in the Bell basis with signs $(-1, +1, +1, +1)$: applying $\sigma_y \otimes \sigma_y$ to $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$ gives $-\,(|11\rangle + |00\rangle)/\sqrt{2} = -|\Phi^+\rangle$, while $|\Phi^-\rangle = (|00\rangle - |11\rangle)/\sqrt{2}$ maps to $(|00\rangle - |11\rangle)/\sqrt{2} = |\Phi^-\rangle$. Since $\rho_p$ is real and diagonal, $\rho_p^\ast = \rho_p$ and

$$\tilde{\rho}_p = \mathrm{diag}(-p,\; 1-p,\; 0,\; 0)\big|_{\mathcal{B}} \quad\Rightarrow\quad \rho_p \tilde{\rho}_p = \mathrm{diag}\big(p^2 \cdot (-1)\ \text{sign-corrected}\big),$$

more carefully: $\rho_p\tilde{\rho}_p = \mathrm{diag}(p \cdot p, (1-p)(1-p), 0, 0)$ up to the sign on the first entry, which does not affect eigenvalues. The eigenvalues of $\rho_p\tilde{\rho}_p$ are therefore

$$\lambda_1 = p^2, \quad \lambda_2 = (1-p)^2, \quad \lambda_3 = \lambda_4 = 0.$$

Hence $\lambda_{\max} = \max(p, 1-p)^2$ and

$$C(\rho_p) = \max\big(0,\; 2\max(p, 1-p) - 1\big) = |2p - 1|.$$

Sanity checks: $C(\rho_1) = |2 - 1| = 1$ (maximally entangled Bell state); $C(\rho_{0.5}) = 0$ (separable); $C(\rho_{0.75}) = 0.5$.

### 4.2 Cost grid

With $C = |2p-1|$, we have $1 - C^2 = 1 - (2p-1)^2 = 4p(1-p)$, so the cost per copy is

$$E_F(\rho_p) = h_2\!\left(\frac