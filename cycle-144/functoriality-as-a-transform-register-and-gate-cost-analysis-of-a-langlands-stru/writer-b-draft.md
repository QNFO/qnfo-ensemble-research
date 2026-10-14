# Functoriality as a Transform: Query-Cost Analysis of a Langlands-Structured Adelic Quantum Register

## Abstract

Computing with automorphic representations is bottlenecked by the absence of a fast algorithm for non-abelian harmonic analysis: for the abelian group $\mathrm{GL}(1)$ the Fast Fourier Transform decomposes functions into irreducible characters in $O(n \log n)$ operations, while for $G(\mathbb{Q})\backslash G(\mathbb{A})$ the corresponding decomposition — the Langlands program — has no known fast algorithm. This paper formalizes a computational toy model in which a hybrid quantum register carries both archimedean and $p$-adic factors, so that local Langlands data at each prime is stored in a $p$-power-dimensional factor and functoriality is expressed as a tensor product of local unitary transforms. We derive the register dimensions, gate counts, and comparison baselines for explicit parameter choices: a radix-$p$ adelic transform on primes $\{2,3,5\}$ with four $p$-adic digits each acts on a register of dimension $810{,}000$ with $2{,}888$ structured radix stages, against a naive dense-transform baseline of $6.561 \times 10^{11}$ operations, a projected separation factor of $2.27 \times 10^{8}$. We further derive the product-formula identity on the example $x = 6$, the group order $|\mathrm{GL}(2,\mathbb{F}_7)| = 2016$ for a finite-field toy model, and Bruhat–Tits tree vertex counts. All results are analytical; the central claim — that the structured transform reproduces Hecke-eigenvalue matches $a_p(E) = a_p(f)$ — remains a conjecture with a stated falsification condition.

## 1. Introduction

Computational number theorists who evaluate and match $L$-functions face a structural cost barrier today. Verifying that an elliptic curve $E$ matches a modular form $f$ requires computing local data $a_p$ on both sides for many primes; the modularity theorem guarantees the identity $a_p(E) = a_p(f)$ for all primes $p$, but each verification is a separate computation, and there is no transform that maps the Galois side of the correspondence to the automorphic side in one structured pass. The obstacle is not a missing constant factor: for the abelian case $\mathrm{GL}(1)$, harmonic analysis on $\mathbb{Z}/n\mathbb{Z}$ is the discrete Fourier transform and the Cooley–Tukey algorithm computes it in $O(n \log n)$ operations, but for a general reductive group $G$, the decomposition of functions on $G(\mathbb{Q})\backslash G(\mathbb{A})$ into automorphic representations — the content of the Langlands program — has no known fast algorithm [8]. Every non-abelian instance is currently computed by bespoke methods.

What would change if functoriality were a transform? A single operator, applied to a register that stores local data at every prime simultaneously, would turn repeated per-prime verification into one structured computation, in the same way the FFT turned per-frequency correlation into a divide-and-conquer recursion. The prerequisite is a computational substrate in which archimedean and non-archimedean data coexist natively — an adelic register — and in which the local correspondences at each prime are unitary maps that compose across primes. Such a substrate is not physically established: $p$-adic and adelic quantum mechanics exist as mathematical formulations with complex-valued wave functions on $p$-adic and adelic argument spaces [1], and the adelic ring is the natural setting for automorphic forms and the Langlands program [2], but no architecture implements registers over $\mathbb{Q}_p$ factors, and the error-correction and threshold properties of any ultrametric platform remain conjectural [9], [10].

This paper does not claim a physical device or a proved correspondence. It does three things that a construction program must do first: it fixes a finite toy model in which every object is exactly computable, it derives the register and gate-count arithmetic that any implementation would face, and it states the specific observation that would falsify the central conjecture. The contributions are:

- A formalization of the adelic toy register as a tensor product $\bigotimes_{p \in S} \mathbb{C}^{p^{k_p}}$ over a finite prime set $S$, with the local Langlands correspondence at each prime represented by a unitary $U_p$ (Section 3).
- A derivation of the product-formula identity $\prod_v |x|_v = 1$ on the explicit example $x = 6$, establishing the consistency convention for adelic norms used throughout (Section 4.1).
- Derived register dimensions, structured radix-stage counts, and naive baselines for the parameter set $S = \{2,3,5\}$, $k_p = 4$: register dimension $810{,}000$, structured stage count $2{,}888$, naive baseline $6.561 \times 10^{11}$, separation factor $\approx 2.27 \times 10^{8}$ (Section 4.4).
- Derived finite-field toy-model data: $|\mathrm{GL}(2,\mathbb{F}_7)| = 2016$ and Bruhat–Tits tree vertex counts $V(2,10) = 3070$ and $V(3,5) = 485$ (Sections 4.2 and 4.3).
- A per-prime Hecke-eigenvalue verification budget: for the six primes up to 13, a naive classical check of $a_p(E) = a_p(f)$ costs 82 field operations under stated assumptions (Section 4.5).
- A falsification criterion and a limitations list for the central conjecture (Section 6).

## 2. Background and Related Work

The mathematical physics of $p$-adic and adelic quantum mechanics supplies the Hilbert-space conventions this paper adopts. Vladimirov–Volovich-style $p$-adic quantum mechanics with $p$-adic-valued wave functions was introduced first, but the formulation with complex-valued wave functions on $p$-adic spaces is the one suited to connection with ordinary quantum mechanics, and [1] restricts its development to that case; the same source presents ordinary quantum mechanics on $L_2(\mathbb{R}^D)$ with the Heisenberg commutation relations $[\hat{x}_i, \hat{k}_j] = i\hbar\,\delta_{ij}$ as the template being generalized. This paper takes complex-valued wave functions on $p$-adic and adelic arguments as its register model, following [1]. The adelic argument space itself is defined in [2]: an adele is an infinite sequence $x = (x_\infty, x_2, \ldots, x_p, \ldots)$ with $x_\infty \in \mathbb{R}$ and $x_p \in \mathbb{Q}_p$, restricted so that $x_p \in \mathbb{Z}_p$ for all but finitely many primes; adelic classical cosmology is described there as the generalization of ordinary cosmology that employs all real and $p$-adic completions of $\mathbb{Q}$ on equal footing. The same restricted-product structure is what makes a finite-prime tensor-product register a faithful toy of the adelic setting, since a computational register can only hold finitely many factors.

Two structural obstructions from the physics literature bound what any such register can do. First, [4] records that in $p$-adic quantum mechanics the multiplication operator $\hat{q}\psi \mapsto x\psi$ has no meaning for $x \in \mathbb{Q}_p$ and $\psi(x) \in \mathbb{C}$, and that no $p$-adic "momentum" or "Hamiltonian" operator exists as an infinitesimal generator, because $\mathbb{Q}_p$ is disconnected and infinitesimal translations are meaningless; evolution must therefore be handled through other means, such as the path-integral formalism of [6], which evaluates probability amplitudes $\mathcal{K}(x'', t''; x', t')$ for quadratic Lagrangians on $p$-adic and adelic spaces and observes that the ordinary and $p$-adic path-integral formalisms take the same form at different levels of evaluation — a number-field invariance property that supports treating the archimedean and $p$-adic factors of a register with uniform methods. Second, the wavelet transform of [5] provides the natural multiscale decomposition on $p$-adic spaces: the $p$-adic wavelet transform is developed there as a tool for hierarchic quantum systems, with the Haar wavelet as the evident discrete implementation, and its conclusion explicitly points toward generalizing quantum computing ideas to quantum systems with $p > 2$ orthogonal quantum states — exactly the $p$-dimensional local factors this paper uses. The cosmological literature [2], [4] supplies the precedent that adelic models can be well defined as ordinary applications of adelic quantum mechanics even when a naive adelic generalization (there, of the Hartle–Hawking proposal) fails; [4] states that $p$-adic and adelic minisuperspace quantum cosmology is well defined as an ordinary application of $p$-adic and adelic quantum mechanics, while the adelic Hartle–Hawking proposal does not work in models with matter fields. The broader programmatic motivation — that the choice of $\mathbb{R}$ as the base field of physics is a convention rather than a necessity, because Ostrowski's theorem shows the archimedean and all $p$-adic absolute values exhaust the non-trivial absolute values on $\mathbb{Q}$ — is argued in [11], which states that every measurement produces a rational number to finite precision and that the archimedean completion and every $p$-adic completion are equally legitimate; [10] states the same theorem as the foundation for any structure that must interact with all ways of measuring a rational number.

On the number-theoretic side, the Langlands correspondence and its $p$-adic variants define what the proposed transform must compute. [7] introduces the categorical approach to the $p$-adic Langlands program in Banach and analytic settings, and records that functoriality for automorphic representations would imply the expected analytic properties of automorphic $L$-functions, since the standard $L$-functions on $\mathrm{GL}_d$ constructed by Godement–Jacquet and Tamagawa already admit analytic continuations and functional equations. The functoriality statement itself has been extended to $p$-adic settings: [3] formalizes a notion of $p$-adic Langlands functoriality for the definite unitary group, extending the classical notion to eigenvarieties — the $p$-adic rigid analytic spaces parameterizing $p$-adic automorphic forms constructed by Chenevier — and obtains cases by interpolating known classical cases, with the Artin map normalized to send uniformizers to geometric Frobenii and the local Langlands correspondence normalized as in Harris–Taylor. That functoriality can be carried by $p$-adic analytic spaces of automorphic forms is the precise sense in which "functoriality as a map on a parameter space" already exists mathematically; the open question is whether it can be carried by a unitary map on a quantum register. The proved instance of the correspondence for $\mathrm{GL}(2)$ over $\mathbb{Q}$ is the modularity theorem, which [10] states as: for every elliptic curve $E$ over $\mathbb{Q}$ there is a weight-2 newform $f$ of level $N_E$ with $L(E,s) = L(f,s)$ and consequently $a_p(E) = a_p(f)$ for all primes $p$; [10] also states the Breuil–Colmez theorem giving a canonical bijection between certain two-dimensional $p$-adic Galois representations of $G_{\mathbb{Q}_p}$ and certain unitary Banach-space representations of $\mathrm{GL}(2,\mathbb{Q}_p)$ — a local, $p$-adic correspondence that is functorial and compatible with local class field theory. The Breuil–Colmez bijection is the closest existing analogue of the local unitary $U_p$ this paper posits.

The computational identification that motivates the whole approach is due to [8], which identifies the Fast Fourier Transform as the computational Langlands correspondence for $\mathrm{GL}(1)$: harmonic analysis on a group is decomposition into irreducible representations; for $\mathbb{Z}/n\mathbb{Z}$ the irreducibles are one-dimensional characters, the decomposition is the discrete Fourier transform, and the fast algorithm is Cooley–Tukey at $O(n \log n)$, exploiting the factorization $n = n_1 n_2$; for $G(\mathbb{Q})\backslash G(\mathbb{A})$ the irreducibles are automorphic representations, the decomposition is the Langlands program, and the fast algorithm is not known. [8] further identifies the Bruhat–Tits tree for $\mathrm{GL}(2,\mathbb{Q}_p)$ as the natural hierarchical $p$-adic decomposition — the analog of the Cooley–Tukey factorization — with Hecke operators as the generalized radix-$p$ stages, and records Gauss's unpublished 1805 asteroid-interpolation manuscript as an earlier instance of the same harmonic-analysis operation. The geometric substrate for a $p$-adic register is accordingly a Bruhat–Tits tree; [9] describes $\mathrm{BT}_p$ as the $(p+1)$-regular infinite tree whose boundary is $\mathbb{P}^1(\mathbb{Q}_p)$, in the context of holographic quantum error-correcting codes built from perfect tensors on the tree, and poses — explicitly as an open conjecture — whether adelic combinations of such codes across all primes produce constructions beyond the stabilizer formalism, proposing a phased program beginning with explicit small adelic codes for $p \in \{2,3\}$ at cutoff radius 2. Finally, [10] proposes an ultrametric threshold theorem — that for physical error rate below a threshold $p_{\mathrm{th}}$, logical error rates of a Bruhat–Tits quantum computer can be made arbitrarily small with polynomial overhead in $\log(1/p_L)$ — and lists the falsification conditions for the ultrametric quantum-computation hypothesis, including the failure of coupling strengths to decay exponentially with depth. Both the threshold theorem and the physical platform are conjectural; this paper's results are therefore confined to the register-and-transform level, where everything is exactly computable.

## 3. Methods

### 3.1 The adelic toy register

Fix a finite set of primes $S = \{p_1, \ldots, p_m\}$ and digit depths $k_{p_i} \geq 1$. The toy register is the tensor product

$$\mathcal{H}_S = \bigotimes_{p \in S} \mathbb{C}^{p^{k_p}},$$

with $\dim \mathcal{H}_S = \prod_{p \in S} p^{k_p}$. Each factor $\mathbb{C}^{p^{k_p}}$ carries the radix-$p$ harmonic analysis on the additive group $\mathbb{Z}/p^{k_p}\mathbb{Z}$, which is the finite analogue of the $p$-adic position basis; this is the finite register analogue of the complex-valued $p$-adic Hilbert spaces of [1]. An archimedean factor $\mathbb{C}^{2^{k_\infty}}$ may be appended for problems with a real component, mirroring the adele's archimedean place in the restricted product of [2]; in this paper's derivations the archimedean factor is carried along but not exercised, and we say so explicitly where it matters.

### 3.2 Local transforms and the functoriality conjecture

For each $p \in S$, let $U_p$ be a unitary operator on the local factor $\mathbb{C}^{p^{k_p}}$ intended to represent the local Langlands correspondence at $p$ in the style of the Breuil–Colmez bijection [10]: Galois-side data in, automorphic-side data out, functorially. The global functoriality transform is the tensor product

$$\mathcal{U}_S = \bigotimes_{p \in S} U_p.$$

The central conjecture of this paper is:

**Conjecture (Functoriality as a transform).** There exists a choice of local unitaries $U_p$, constructible by a structured (radix-$p$-like) circuit of $O(k_p \, p^{k_p})$ elementary stages, such that the diagonal matrix elements of $\mathcal{U}_S$ reproduce the Hecke-eigenvalue matches $a_p(E) = a_p(f)$ of the modularity theorem [10] on a finite test family of elliptic curves and newforms.

This is a conjecture, not a result; Section 6 states what observation would refute it. The role of the methods here is to make the cost side of the conjecture exactly computable before any claim about the correspondence side is made.

### 3.3 Structured versus naive transform cost

The cost model has two entries. The structured cost assumes the transform on $\mathbb{C}^{p^k}$ factors through the $k$-level radix-$p$ recursion, in direct analogy with the Cooley–Tukey factorization $n = n_1 n_2$ exploited by the FFT [8] and with the Hecke-as-radix-stage identification of [8] on the Bruhat–Tits tree; each of the $k$ levels applies $p^k$ elementary stage operations, giving $T_{\mathrm{str}}(k,p) = k\,p^k$. The naive cost assumes no factorization is available and the transform is an arbitrary dense unitary on $p^k$ dimensions, requiring on the order of $(p^k)^2 = p^{2k}$ elementary operations; we state this as an assumption (a standard dense-unitary upper bound), not as a derived theorem. The adelic structured cost is additive across factors because the tensor product factorizes:

$$T_{\mathrm{str}}(S) = \sum_{p \in S} k_p \, p^{k_p},$$

while the naive adelic baseline is the dense cost on the full tensor-product space:

$$T_{\mathrm{naive}}(S) = \Big( \prod_{p \in S} p^{k_p} \Big)^{2}.$$

### 3.4 Geometry and finite-field toy data

The $p$-adic geometry of the register is the Bruhat–Tits tree $\mathrm{BT}_p$, the $(p+1)$-regular infinite tree with boundary $\mathbb{P}^1(\mathbb{Q}_p)$ [9]. For a finite cutoff radius $r$, the number of vertices within distance $r$ of a root vertex in a $(p+1)$-regular tree is derived in Section 4.3. The finite-field toy model, in which the local correspondence is exactly computable by finite linear algebra, uses $\mathrm{GL}(2,\mathbb{F}_q)$; its order is derived in Section 4.2. The Hecke-eigenvalue verification budget uses the modularity identity $a_p(E) = a_p(f)$ [10] with a stated naive cost per evaluation.

## 4. Analysis

### 4.1 The product formula on $x = 6$

Every adelic computation must fix a norm convention. Following the $p$-adic norm of [4]: for $0 \neq x \in \mathbb{Q}$ written $x = p^{\nu} \frac{m}{n}$ with $m, n$ not divisible by $p$, the $p$-adic norm is $|x|_p = p^{-\nu}$. The archimedean norm is $|x|_\infty$. The product formula asserts $\prod_v |x|_v = 1$ over all places $v$. We verify it explicitly for $x = 6 = 2 \cdot 3$.

- Archimedean place: $|6|_\infty = 6$.
- Place $p = 2$: write $6 = 2^{1} \cdot 3$, so $\nu = 1$ and $|6|_2 = 2^{-1} = 0.5$.
- Place $p = 3$: write $6 = 3^{1} \cdot 2$, so $\nu = 1$ and $|6|_3 = 3^{-1} \approx 0.333333$.
- Places $p \geq 5$: $6 = p^{0} \cdot 6$ with $6$ not divisible by $p$, so $\nu = 0$ and $|6|_p = p^{0} = 1$ for every prime $p \geq 5$.

The product over all places is

$$\prod_v |6|_v = 6 \times 2^{-1} \times 3^{-1} \times \prod_{p \geq 5} 1 = 6 \times \tfrac{1}{2} \times \tfrac{1}{3} = \frac{6}{6} = 1.$$

The product formula holds exactly on this example. This fixes the convention: local data at each prime enters with $p$-adic weight $p^{-\nu}$, and the archimedean factor compensates. Any register implementation that stores local components must reproduce this compensation if it is to respect the adelic structure that [2] identifies as the natural setting for the Langlands program.

### 4.2 Order of the finite-field toy group

For the finite-field toy model, the group $\mathrm{GL}(2,\mathbb{F}_q)$ consists of invertible $2 \times 2$ matrices over $\mathbb{F}_q$. A $2\times 2$ matrix is invertible exactly when its two columns are linearly independent. The first column is any nonzero vector: $q^2 - 1$ choices. The second column is any vector not in the one-dimensional span of the first: $q^2 - q$ choices. Hence

$$|\mathrm{GL}(2,\mathbb{F}_q)| = (q^2 - 1)(q^2 - q).$$

For $q = 7$:

$$|\mathrm{GL}(2,\mathbb{F}_7)| = (49 - 1)(49 - 7) = 48 \times 42 = 2016.$$

A dense unitary on the group-regular representation of $\mathrm{GL}(2,\mathbb{F}_7)$ therefore acts on a space of dimension $2016$, and a naive dense transform on it costs on the order of $2016^2 = 4{,}064{,}256$ elementary operations (this is the naive baseline; the structured cost depends on the representation decomposition, which the toy model makes exactly computable by finite linear algebra).

### 4.3 Bruhat–Tits tree vertex counts

The tree $\mathrm{BT}_p$ is $(p+1)$-regular [9]. From the root, there are $p+1$ vertices at distance $1$. Each subsequent level multiplies by the branching factor $p$ (each vertex at distance $n \geq 1$ has $p$ children away from the root), so the number of vertices at distance $n \geq 1$ is $(p+1)\,p^{n-1}$. The total within radius $r$ is

$$V(p, r) = 1 + \sum_{n=1}^{r} (p+1)\,p^{n-1} = 1 + (p+1)\,\frac{p^{r} - 1}{p - 1}.$$

For $p = 2$, $r = 10$:

$$V(2,10) = 1 + 3 \times \frac{2^{10} - 1}{2 - 1} = 1 + 3 \times 1023 = 1 + 3069 = 3070.$$

For $p = 3$, $r = 5$:

$$V(3,5) = 1 + 4 \times \frac{3^{5} - 1}{3 - 1} = 1 + 4 \times \frac{242}{2} = 1 + 4 \times 121 = 1 + 484 = 485.$$

These are the finite subtree sizes within which a cutoff-radius register of the kind proposed in the adelic QEC program's Phase 1 [9] — explicit small codes for $p \in \{2,3\}$ at cutoff radius 2 — would be scaled up. At the program's own Phase-1 parameters, $p = 2$, $r = 2$: $V(2,2) = 1 + 3 \times (2^2 - 1) = 1 + 9 = 10$ vertices; $p = 3$, $r = 2$: $V(3,2) = 1 + 4 \times (3^2-1)/2 = 1 + 4 \times 4 = 17$ vertices.

### 4.4 Register dimension and transform costs for $S = \{2,3,5\}$, $k_p = 4$

Take $S = \{2, 3, 5\}$ and $k_p = 4$ for each $p \in S$. The register dimension is

$$\dim \mathcal{H}_S = 2^{4} \times 3^{4} \times 5^{4} = 16 \times 81 \times 625.$$

Step by step: $16 \times 81 = 1296$; $1296 \times 625 = 810{,}000$. So $\dim \mathcal{H}_S = 810{,}000$.

The structured adelic transform cost is

$$T_{\mathrm{str}}(S) = \sum_{p \in S} k_p \, p^{k_p} = 4 \times 2^{4} + 4 \times 3^{4} + 4 \times 5^{4} = 64 + 324 + 2500 = 2888.$$

The naive baseline on the full tensor-product space is

$$T_{\mathrm{naive}}(S) = 810{,}000^{2} = 6.561 \times 10^{11}.$$

The separation factor is

$$\frac{T_{\mathrm{naive}}(S)}{T_{\mathrm{str}}(S)} = \frac{6.561 \times 10^{11}}{2888} \approx 2.27 \times 10^{8}.$$

For a single local factor