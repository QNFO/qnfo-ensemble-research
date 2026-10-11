# Adelic Factorization of Quantum Dynamics Across All Completions of $\mathbb{Q}$: Consistency Conditions, Local Factors, and a Resource Estimate for Numerical Testability

## Abstract

Ostrowski's theorem partitions the non-trivial completions of $\mathbb{Q}$ into exactly one Archimedean place ($\mathbb{R}$) and infinitely many $p$-adic places ($\mathbb{Q}_p$), yet standard quantum mechanics is formulated exclusively over $\mathbb{R}$ (and $\mathbb{C}$). We treat the choice of $\mathbb{R}$ as a convention to be tested rather than a necessity, and propose that a physically consistent quantum theory should admit local factors at every place of $\mathbb{Q}$, constrained by a global adelic product structure analogous to the role of Poisson summation and the functional equation in Tate's thesis. We formalize this as a factorization conjecture for spectral zeta functions and amplitudes, verify the underlying arithmetic product formula by explicit computation at representative rationals, quantify the truncation error of finite-prime adelic Euler products (partial product over primes $p \leq 13$ at $s=2$: $\approx 1.617917$ versus $\zeta(2) \approx 1.644934$, tail $0.016561$ within a proven bound of $1/13 \approx 0.076923$), and derive a hardware resource estimate for numerical tests on current superconducting hardware: approximately $157$ two-qubit gates at $99.56\%$ fidelity before a $50\%$ circuit success threshold. We state falsification criteria and open problems.

## 1. Introduction

Standard quantum mechanics is written over the real numbers: Hilbert spaces over $\mathbb{C} \cong \mathbb{R}^2$, observables as self-adjoint operators, amplitudes as complex phases. The choice of $\mathbb{R}$ as the underlying number field is rarely questioned, because $\mathbb{R}$ is the completion of $\mathbb{Q}$ with respect to the usual absolute value, and the usual absolute value is the one under which physical distances and probabilities appear naturally. But Ostrowski's theorem — as recalled in [11] — states that every non-trivial completion of $\mathbb{Q}$ is either the Archimedean completion $\mathbb{R}$ (the $\infty$-place) or one of the infinitely many non-Archimedean completions $\mathbb{Q}_p$, one for each prime $p$. The entry [11] further records that these topologies are mutually singular: no sequence converges simultaneously in two distinct completions unless it is eventually constant. There is therefore no purely topological reason to privilege $\mathbb{R}$ over $\mathbb{Q}_p$; the privilege, if real, must be dynamical or structural.

This paper develops the conjecture that the Archimedean choice is a convention, and that a fully consistent quantum dynamics should factorize into local contributions at every place $v$ of $\mathbb{Q}$ ($v = \infty, 2, 3, 5, \dots$). The analogy guiding the proposal is Tate's 1950 thesis, which — as summarized in [9] — provides an explicit structural template in which global zeta functions emerge from local factors at all places, with the functional equation forced by adelic Poisson summation. If quantum dynamics admits an analogous local-global structure, then global consistency conditions should force an adelic product form on the theory, and the apparent necessity of $\mathbb{R}$ would be reinterpreted as an "Archimedean artifact": one factor of a larger product, singled out by our measurement apparatus rather than by the theory.

The contributions of this paper are deliberately modest and verifiable:

1. **A precise factorization conjecture** (Section 3) for quantum dynamics: local Hilbert-space data $\mathcal{H}_v$, local evolution operators $U_v(t)$, and a global consistency condition $\mathcal{Z}(s) = \prod_v \mathcal{Z}_v(s)$ on spectral zeta functions, together with a recovery condition stating when the adelic product reduces to standard real-valued quantum mechanics.
2. **Explicit arithmetic verification of the product-formula substrate** (Section 4): we compute the adelic product formula for representative rationals, evaluate a truncated adelic Euler product against $\zeta(2)$ with a proven tail bound, and quantify how many finite places must be retained to reach a target accuracy.
3. **A hardware resource estimate** (Sections 4 and 5) for the numerical test programme, using published gate fidelities of a current superconducting quantum processor [2], with all arithmetic shown.
4. **Falsification criteria and limitations** (Section 6), including the specific observations that would refute the factorization conjecture.

We emphasize at the outset what this paper does *not* claim: it does not construct a full $p$-adic quantum mechanics, does not claim that $\mathbb{R}$-based physics is wrong, and does not report any new experimental data. All quantitative claims are either computed explicitly in Section 4 from stated inputs or labeled as projections with stated assumptions.

## 2. Background and Related Work

**Adelic equidistribution and measures.** The arithmetic equidistribution theorem of Baker–Rumely and Favre–Rivera–Letelier, and independently Chambert-Loir, establishes equidistribution of points of small height on the Berkovich compactification of $\mathbb{P}^1$ with respect to an adelic measure [1]. This is the key precedent for treating "adelic measures" as coherent mathematical objects rather than bookkeeping devices: a measure distributed across all places of a number field, with the Archimedean and non-Archimedean contributions on an equal footing. Our conjecture transfers exactly this egalitarian attitude from measures on $\mathbb{P}^1$ to dynamical data of quantum systems. The supplied summary of [1] does not state the equidistribution theorem's quantitative error terms, so we use it only at the level of structural precedent.

**Adelic line bundles and rigidity.** The arithmetic Hodge index theorem for adelic line bundles [4] extends results from number fields to finitely generated fields and applies the theorem to obtain a rigidity property of the sets of preperiodic points of polarizable algebraic dynamical systems. This is a second and stronger precedent: adelic global objects imposing *rigidity* — global constraints that local data cannot evade. Our programme hypothesizes an analogous rigidity: that the requirement of adelic factorization constrains the spectrum and amplitudes of quantum dynamics, which is precisely the content of the "consistency conditions" of Section 3.

**Adelic topological groups.** The theorem that finite-dimensional protori (finite-dimensional compact connected abelian groups) *are* adelic tori, with a complete Lie theory including a proper short exact sequence $0 \to \mathbb{Q}^n \to \mathcal{L}(G) \xrightarrow{\exp} G \to 0$ with $\exp$ the adelic exponential [6], supplies the candidate global phase space for an adelic quantum theory. If the adelic analogue of the phase space of classical mechanics is an adelic torus, then the adelic exponential plays the role that the ordinary exponential plays in Lie theory over $\mathbb{R}$, and quantization over such a group is a natural next step. The supplied summary of [6] does not detail the nonarchimedean dimension theory it extends, so we rely on it only for the categorical identification and the exact sequence.

**Tate's thesis as template, and prior adelic quantum programmes.** Reference [9] proposes that Tate's 1950 thesis provides an explicit structural template for constructing adelic quantum mechanics, records that the Dragovich programme has realized this template for free theories, and cites Huang, Stoica, and Zhong (2022) as an independent proof-of-concept in conformal field theory. This is the closest prior art to our conjecture: it establishes local-global structure for *free* theories and one interacting (CFT) proof-of-concept, leaving open exactly the question we address — whether the template extends to general dynamics and what consistency conditions it imposes. Reference [11] frames the same programme at the level of foundations, naming the "completion problem" and the adelic restructuring of fundamental physics, and supplies the Ostrowski partition and mutual singularity of topologies that we take as our starting point. Reference [10], "Ratio-Based Adelic Physics," is part of the same research corpus; its supplied summary is empty, so we cannot state what it contains and use it only to acknowledge that ratio-based formulations exist in the programme's internal literature.

**Ontology of completions.** Reference [12] proposes a three-axis framework — Depth (computable reals), Breadth (non-computable reals, termed physically vacuous), and Valuation ($p$-adic completions as information carriers) — with falsifiable predications for quantum error correction and gauge structure. Our proposal is complementary: where [12] assigns the $p$-adic axis an informational role, we ask whether dynamics itself factorizes across that axis.

**Quantum hardware and simulation.** The Tianyan Quantum Cloud Platform offers cloud services demonstrating quantum advantage with a superconducting processor named Tianyan-287, featuring $105$ qubits and single-qubit, two-qubit, and readout fidelities of $99.90\%$, $99.56\%$, and $98.7\%$ respectively [2]. This is the concrete hardware context for the numerical test programme of Section 4.4: any simulation of $p$-adic local dynamics or of adelic zeta consistency conditions on a quantum processor inherits these fidelity budgets. For the *simulation methodology*, the quantum sawtooth map work [7] shows that a quantum computer can efficiently extract physical information from a complex dynamical system, simulating dynamical localization of classical chaos and extracting the localization length with quadratic speedup over classical computation. Dynamical localization is precisely the phenomenon one expects to study first in $p$-adic dynamics (where the role of chaos and localization is unexplored), so [7] is the direct methodological template. Finally, the parametric and feasibility study of data sampling for Dynamic Mode Decomposition (DMD) [3] — a Koopman-based technique that dissects high-dimensional nonlinear systems into periodically distinct constituents on reduced-order subspaces, with the study addressing range, resolution, and universal convergence states of the data sampling — offers the classical counterpart we propose for post-processing simulated adelic dynamics: decomposing simulated trajectories into their local-periodic constituents, one per place.

**Hybrid dynamics as a coupling model.** Reference [8] establishes that consistent dynamics coupling classical and quantum degrees of freedom exists provided it is stochastic, with dynamics linear in the hybrid state and completely positive and trace preserving (CPTP), with applications including the back-reaction of quantum fields on spacetime free of the pathologies of semi-classical equations. This matters for us because any adelic theory must couple the Archimedean sector (where measurements happen) to non-Archimedean sectors (where the conjectured local factors live); the result of [8] shows that such hybrid coupling can be made consistent if stochastic, suggesting that the $\mathbb{R}$–$\mathbb{Q}_p$ interface should be modeled as a stochastic CPTP channel rather than a deterministic unitary.

**Counting complexity.** Reference [5] studies how Ehrhart theory helps compute probabilities of voting situations by counting integral points in polyhedra under the Impartial Anonymous Culture assumption, but notes that the dimension and complexity of the involved polyhedra grows rapidly. We cite it as a cautionary analogy: our truncation analysis in Section 4.3 involves counting and bounding contributions over many primes, and lattice-point-style complexity growth is the expected obstacle when adelic truncations are made combinatorially explicit.

## 3. Methods

### 3.1 The local-global template

Fix the number field $K = \mathbb{Q}$. Its places are $v = \infty$ (Archimedean, completion $\mathbb{R}$) and $v = p$ for primes $p$ (completions $\mathbb{Q}_p$), per Ostrowski's theorem as stated in [11]. For each place $v$, let $|\cdot|_v$ denote the normalized absolute value: $|x|_\infty = $ the usual absolute value, and $|x|_p = p^{-v_p(x)}$ where $v_p(x)$ is the $p$-adic valuation (the exponent of $p$ in the factorization of $x$).

The structural template from Tate's thesis, as described in [9], is: global objects (zeta functions, Poisson summation, functional equations) factor as products of local objects over all places, and the global consistency (the functional equation) is *forced* by the adelic structure rather than imposed by hand. We conjecture the same shape for quantum dynamics:

**Conjecture 3.1 (Adelic factorization of quantum dynamics).** There exist, for each place $v$ of $\mathbb{Q}$: a local Hilbert space $\mathcal{H}_v$, a local Hamiltonian $H_v$ (self-adjoint on $\mathcal{H}_v$ in the topology of the completion $K_v$), and a local evolution $U_v(t) = e^{-i H_v t / \hbar_v}$, such that the physical amplitude for any process factors as

$$\mathcal{A} = \prod_{v} \mathcal{A}_v,$$

and the spectral zeta function $Z_{\mathcal{H}}(s) = \sum_n \lambda_n^{-s}$ of the global spectrum $\{\lambda_n\}$ factors as

$$Z_{\mathcal{H}}(s) = \prod_v Z_v(s), \qquad Z_v(s) = \sum_{n} \lambda_{v,n}^{-s},$$

with a functional equation relating $Z_{\mathcal{H}}(s)$ to $Z_{\mathcal{H}}(1-s)$ (or to a dual), analogous to the zeta functional equation emerging from adelic Poisson summation in Tate's thesis [9].

### 3.2 The recovery condition

The conjecture must explain why real quantum mechanics works. We posit:

**Condition 3.2 (Archimedean recovery).** There is a class of states and observables (the "accessible" class, defined by the measurement apparatus) for which the product $\prod_v \mathcal{A}_v$ is dominated by the $v = \infty$ factor, the finite-place factors contributing only sub-dominant corrections. In this class, the theory reduces to standard real-valued QM up to corrections bounded by the tail of the adelic product.

This is where the arithmetic of Section 4 becomes load-bearing: the product formula and Euler-product truncation bounds tell us exactly how fast finite-place contributions can decay, hence how good the Archimedean-only approximation can be.

### 3.3 Consistency conditions as testable structure

Following the rigidity pattern of [4] (adelic line bundles forcing rigidity of preperiodic point sets) and the equidistribution structure of [1], we extract three consistency conditions that any factorization must satisfy:

(C1) **Product formula compatibility.** For every rational scale factor $x \in \mathbb{Q}^\times$ appearing in a normalization of amplitudes, the local factors must satisfy $\prod_v |x|_v = 1$; otherwise the factorization is scale-dependent, which is unphysical.

(C2) **Zeta identity.** The global spectral zeta must equal the adelic product of local zetas, and both sides must have the same analytic continuation and functional equation.

(C3) **Truncation stability.** Physical predictions must be stable under enlarging the set of retained finite places; formally, the tail $\prod_{p > P} Z_p(s)$ must tend to $1$ as $P \to \infty$ in the regime of interest.

### 3.4 Numerical test programme

The test programme has three arms, per the source idea: (i) formal derivation of an adelic path integral or spectral zeta identity; (ii) construction of $p$-adic quantum models and checking whether their adelic product recovers real QM in an appropriate limit; (iii) numerical study of adelic zeta identities as consistency conditions on spectra. Arms (ii) and (iii) require quantum or classical simulation resources; we estimate these in Section 4.4 using the hardware parameters of [2] and the simulation methodology of [7], with classical post-processing modeled on the decomposition philosophy of DMD [3].

## 4. Analysis

All arithmetic in this section is shown step by step. Inputs are stated with their sources.

### 4.1 The adelic product formula (consistency condition C1)

**Input:** the normalized absolute values $|x|_\infty$ and $|x|_p = p^{-v_p(x)}$ (standard definitions, as used in [1],