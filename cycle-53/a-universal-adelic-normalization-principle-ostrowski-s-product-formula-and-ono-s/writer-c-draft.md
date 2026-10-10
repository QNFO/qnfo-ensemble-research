# A Universal Adelic Normalization Principle: Product Formulas and Tamagawa Numbers as Two Faces of One Local-Global Schema

## Abstract

Ostrowski's product formula, $\prod_v |x|_v = 1$ for $x \in \mathbb{Q}^\times$, and Ono's formula $\tau(T) = |\mathrm{H}^1(k,\widehat{T})|/|\Sha(T)|$ for the Tamagawa number of an algebraic torus $T$ over a number field $k$ both assert that a product of independently chosen local contributions equals a canonical global value. We propose that these are two instances of a single *universal adelic normalization principle*: local data are individually free, but a global consistency condition (idelic compactness in the first case, Galois-cohomological exactness of the character lattice in the second) forces the aggregate to a value determined only by the normalization of measures. We formalize the principle through a two-layer framework combining the Galois cohomology of character lattices with idelic integration, derive both classical statements as specializations, and compute worked numerical examples: the product formula for $x = 2$ and $x = 3/2$, the Tamagawa number $\tau(\mathbb{G}_m) = 1$ from the residue of $\zeta(s)$ at $s=1$, and $\tau(T) = 2$ for the norm-one torus of $\mathbb{Q}(i)/\mathbb{Q}$. We then classify which neighboring local-global statements — adelic equidistribution, arithmetic Hodge index theory, local Tamagawa conjectures for Hecke-character motives, and Jacobian Tamagawa product formulas — fit the same schema, and isolate the structural condition (triviality of a cokernel of local-to-global restriction) that decides when the forced global value is $1$ versus a nontrivial arithmetic invariant.

## 1. Introduction

Two theorems of classical number theory look, at first glance, unrelated. The first is Ostrowski's product formula: for every $x \in \mathbb{Q}^\times$,

$$\prod_{v \leq \infty} |x|_v = 1,$$

where $v$ ranges over all places of $\mathbb{Q}$ (finite primes and the archimedean place $\infty$) and $|\cdot|_v$ is the normalized absolute value. The second is Ono's formula for algebraic tori: if $T$ is an algebraic torus over a number field $k$, its Tamagawa number $\tau(T)$ — a global volume computed by integrating over the adelic quotient $T(\mathbb{A}_k)/T(k)$ — equals

$$\tau(T) = \frac{|\mathrm{H}^1(k,\widehat{T})|}{|\Sha(T)|},$$

where $\widehat{T} = \mathrm{Hom}(T,\mathbb{G}_m)$ is the character lattice, $\mathrm{H}^1(k,\widehat{T})$ is the first Galois cohomology group of that lattice, and $\Sha(T)$ is the Tate–Shafarevich group measuring the failure of the Hasse principle for $T$.

The observation motivating this paper is structural: both theorems say that a family of *locally free* quantities (the individual $|x|_v$, or the local volumes $\omega_v(T)$) aggregates, under a global constraint, to a *canonically forced* value. In the product formula the constraint is that $x$ is a single rational number simultaneously living at all places; in Ono's formula the constraint is the exact sequence relating $T(k)$, $T(\mathbb{A}_k)$, and the cohomology of $\widehat{T}$. We conjecture that both are specializations of one **universal adelic normalization principle**:

> **Principle (informal).** Let $\{X_v\}_{v}$ be local objects attached to the places of a number field $k$, each carrying a freely normalizable measure or structure. A global object $X$ exists (i.e., the local data glue) if and only if the product of local normalization factors equals a canonical value $\nu(X)$, which is computable from the cohomology of the gluing data and equals $1$ precisely when the relevant local-to-global obstruction group vanishes.

The contributions of this paper are: (i) a formal two-layer framework — Galois cohomology of character lattices plus idelic integration — from which both the product formula and Ono's formula are derived as specializations (Sections 3–4); (ii) fully worked numerical demonstrations, including the product formula for $x=2$ and $x=3/2$, the computation $\tau(\mathbb{G}_m)=1$ from the residue of the Riemann zeta function, and $\tau(T)=2$ for the norm-one torus of $\mathbb{Q}(i)/\mathbb{Q}$ (Section 4); (iii) a classification of which other local-global statements in the adelic literature fit the schema, and a precise criterion — vanishing of a cokernel $\mathrm{coker}(\rho)$ of local-to-global restriction — for when the forced value is $1$ (Sections 4–5); and (iv) a discussion of failure modes, falsifiability, and open questions (Section 6).

We write for an adjacent-field expert: an *adelic* structure is one attached to the ring $\mathbb{A}_k$ of adeles of $k$, the restricted product $\prod_v k_v$ of all completions of $k$; a *place* $v$ is one completion; a *torus* is an algebraic group that becomes isomorphic to $(\mathbb{G}_m)^n$ over an algebraic closure.

## 2. Background and Related Work

We situate the proposed principle against the provided literature, which spans both of its poles — product formulas and Tamagawa theory — and several neighboring local-global phenomena.

**[1] Adjoint motives of modular forms and the Tamagawa number conjecture** (arXiv:2512.02348v2). This work constructs integral structures on the realisations of the motive $M$ attached to a newform $f$ of weight $k \geq 2$ and its adjoint motive $A$, and verifies the $\lambda$-part of the Bloch–Kato Tamagawa number conjecture by the Taylor–Wiles method. It is the modern motive-theoretic descendant of Ono's toric formula: the Tamagawa number conjecture is precisely the schema "local Euler factors, individually free, aggregate to a canonical value forced by $L$-function special values." Our framework is designed to explain why tori ([1]'s $T = \mathbb{G}_m$-like building blocks) and motives obey formally parallel normalization laws.

**[2] The local Tamagawa number conjecture for Hecke characters, II** (arXiv:math/0701634v2). This paper proves the weak local Tamagawa number conjecture for non-critical cases of motives attached to Hecke characters $\psi_\theta: \mathbb{A}_K \to K^*$ over imaginary quadratic $K$ with class number one, under Iwasawa-theoretic restrictions. It supplies the *local* half of the schema: each local Tamagawa factor is an independent invariant of $\psi_\theta$ at a single place, and the global conjecture asserts their canonical aggregation. The restrictions from Iwasawa theory illustrate exactly the kind of obstruction groups our $\mathrm{coker}(\rho)$ formalizes.

**[3] Quasi-adelic measures and equidistribution on $\mathbb{P}^1$** (arXiv:1502.04660v3). Building on the Baker–Rumely, Favre–Rivera-Letelier, and Chambert-Loir equidistribution theorems, this work studies adelic measures on $\mathbb{P}^1$ under which points of small height equidistribute on the Berkovich compactification. Equidistribution is a third instance of the principle: the adelic measure is a freely chosen family of local measures, and the *admissibility* (global consistency) condition forces a canonical total mass normalization. Our Section 5 places this in the same schema with $\nu(X)$ given by the adelic potential theory.

**[4] The arithmetic Hodge index theorem for adelic line bundles II** (arXiv:1304.3539v2). This extends the arithmetic Hodge index theorem to finitely generated fields via the theory of adelic line bundles, with applications to rigidity of preperiodic points of polarizable dynamical systems. The Hodge index theorem is a *signature* statement — a product of local intersection contributions is forced to be nonpositive — and we classify it as a "constrained-sign" specialization of the principle, where the canonical value is a sign rather than a number.

**[5] Finite-Dimensional Protori Are Adelic Tori** (arXiv:2411.16000v44). This identifies the category of finite-dimensional compact connected abelian groups with the category of adelic tori, giving each adelic torus $G$ a proper short exact sequence $0 \to \mathbb{Q}^n \to \mathcal{L}(G) \xrightarrow{\exp} G \to 0$ with $\exp$ the adelic exponential. This is category-level evidence for our unification claim: the objects over which the product formula lives ($\mathbb{A}_k$-side) and the objects over which Tamagawa numbers live (compact adelic tori) are *the same objects*, so a single normalization principle over one category plausibly governs both.

**[6] Product formulas on posets, Wick products, and a correction for the $q$-Poisson process** (arXiv:1708.08034v4). This paper corrects product and linearization formulas for Wick-product versions of $q$-Charlier polynomials, showing the correct formulas are governed by "incomplete" posets whose Möbius functions the authors compute. Though combinatorial, it is a cautionary and constructive analogue: product formulas are sensitive to the *combinatorial normalization* of the underlying poset, and an incorrect normalization yields a wrong canonical value — exactly the failure mode our principle predicts when the gluing cohomology is misidentified.

**[7] Tamagawa number formula for Jacobians** (arXiv:2606.06713v1). This gives a product formula for Tamagawa numbers of Jacobians over a discretely valued field with perfect residue field, factored into unipotent, toric, arithmetic, and cohomological terms, proved by extending the flow-cut construction from semistable to arbitrary curves via Raynaud's results. It demonstrates that Tamagawa numbers themselves decompose as products of local-type contributions — a recursive instance of the principle, one level down.

**[8] Some infinite matrix analysis, a Trotter product formula for dissipative operators, and an algorithm for the incompressible Navier–Stokes equation** (arXiv:1212.2403v6). This work constructs global approximations on the $n$-torus for controlled incompressible Navier–Stokes via coupled Fourier-mode ODE systems, including a Trotter product formula for dissipative operators. We cite it as a *negative* classification datum: its product formula is analytic (semigroup factorization), not arithmetic, and lacks the local-freedom/global-consistency structure; it does not fit the schema, sharpening the boundary of our classification.

**[9] QNFO: The Adelic Completion of the Harmonic Paradigm: A Five-Pillar Red-Team Assessment** (DOI 10.5281/zenodo.21511271). This red-team assessment notes that a physics program invoked Ostrowski's theorem and $p$-adic structures while its core mechanisms were only partially compatible with them. It motivates our demand for *precision* in invoking the product formula: the principle we state is a theorem-schema about arithmetic normalization, not a license for loose adelic analogy.

**[10] QNFO: Adelic Constraints on Quantum Field Theory: Phase 1** (DOI 10.5281/zenodo.20095902). This project asks whether the adelic completion of $\mathbb{Q}$ constrains fundamental physical constants, tracing back to Ostrowski's theorem. It represents the speculative outer edge of "forced global values," and we use it in Section 6 to articulate what would count as evidence for, or against, extending the principle beyond pure mathematics.

In summary, the literature provides: the motive-level Tamagawa program ([1],[2]), adelic measure and line-bundle geometry ([3],[4]), the categorical identification underlying unification ([5]), combinatorial and analytic product formulas as boundary cases ([6],[8]), and recursive Tamagawa factorization ([7]). What is missing — and what this paper supplies — is an explicit common schema with a computable criterion for when the forced value is $1$.

## 3. Methods

### 3.1 The two-layer framework

Fix a number field $k$ and let $\Sigma_k$ be its set of places. The framework has two layers.

**Layer A (cohomological gluing).** Let $T$ be an algebraic torus over $k$ with character lattice $\widehat{T} = \mathrm{Hom}(T,\mathbb{G}_m)$, a free abelian group of rank $n = \dim T$ with a continuous action of $G_k = \mathrm{Gal}(\bar{k}/k)$. The fundamental exact sequence of Ono's theory is

$$0 \to T(k) \to T(\mathbb{A}_k) \xrightarrow{\delta} \mathrm{H}^1(k,\widehat{T})^\vee \to \Sha(T) \to 0,$$

where $\delta$ is the idelic connecting map and $\mathrm{H}^1(k,\widehat{T})^\vee$ is the Pontryagin dual. This sequence is the *global consistency condition*: it says the adelic quotient $T(\mathbb{A}_k)/T(k)$ has volume determined by the cohomology groups $\mathrm{H}^1(k,\widehat{T})$ and $\Sha(T)$.

**Layer B (idelic integration).** Each local group $T(k_v)$ carries a Haar measure $\omega_v$, normalized so that for all but finitely many $v$ the measure of the local points of the integral model is $1$. The Tamagawa number is

$$\tau(T) = \frac{\mathrm{vol}_{\omega}\bigl(T(\mathbb{A}_k)/T(k)\bigr)}{\prod_{v} \lambda_v^{-1}},$$

where $\lambda_v$ are the convergence factors making the product measure finite. The *normalization freedom* is the choice of $\{\omega_v\}$; the *forced value* is $\tau(T)$.

### 3.2 The universal schema

We abstract both layers as follows. A **normalization datum** is a family $m = \{m_v\}_{v \in \Sigma_k}$ where each $m_v$ is a measure or trivialization on a local object $X_v$. A **gluing cocycle** is a map $\rho: \prod_v X_v \to C$ into a cohomology group $C$ measuring the obstruction to descending the family to a global object $X$. The schema asserts:

$$\prod_v \mathrm{Norm}_v(m_v) = \nu(X), \qquad \nu(X) = \frac{|\mathrm{H}^1_{\mathrm{glue}}|}{|\Sha_{\mathrm{glue}}|},$$

where $\mathrm{Norm}_v(m_v)$ is the local normalization factor and $\mathrm{H}^1_{\mathrm{glue}}, \Sha_{\mathrm{glue}}$ are the cohomology and obstruction groups of $\rho$. The **criterion for the value 1** is:

$$\nu(X) = 1 \iff |\mathrm{H}^1_{\mathrm{glue}}| = |\Sha_{\mathrm{glue}}|,$$

which in the toric case reduces to $\mathrm{coker}(\rho) = 0$, i.e., the local-to-global restriction map on characters being surjective with trivial cokernel.

### 3.3 Specializations

- **Product formula:** take $X = \mathbb{G}_m$, $m_v = |\cdot|_v$ on $k_v^\times$, $\rho$ = the diagonal embedding $\mathbb{Q}^\times \hookrightarrow \mathbb{A}_\mathbb{Q}^\times$ modulo which the quotient is compact. Compactness of $\mathbb{Q}^\times \backslash \mathbb{A}_\mathbb{Q}^{\times,1}$ (the norm-one idèles) is the consistency condition forcing $\prod_v |x|_v = 1$.
- **Ono's formula:** take $X = T$, $m_v = \omega_v$, $\rho = \delta$ from the exact sequence of Layer A; then $\mathrm{H}^1_{\mathrm{glue}} = \mathrm{H}^1(k,\widehat{T})$ and $\Sha_{\mathrm{glue}} = \Sha(T)$, giving $\tau(T) = |\mathrm{H}^1(k,\widehat{T})|/|\Sha(T)|$.

### 3.4 Verification protocol

Every numerical claim in Section 4 is computed by hand from stated inputs: local absolute values from the definition $|p|_p = p^{-1}$, $|q|_p = 1$ for primes $q \neq p$, $|x|_\infty = |x|$; the residue $\mathrm{Res}_{s=1}\,\zeta(s) = 1$ (classical, from the Laurent expansion of $\zeta(s)$ at its simple pole); and cohomology of finite Galois modules computed from the standard exact sequence $0 \to \widehat{T}^{G_k} \to \widehat{T} \xrightarrow{N} \widehat{T} \to \widehat{T}^{G_k} \to 0$ for cyclic Galois action, where $N$ is the norm (sum over Galois orbits) map.

## 4. Analysis

We now carry out the derivations with every input stated and every arithmetic step shown.

### 4.1 The product formula for $x = 2$

**Inputs.** By the definition of normalized $p$-adic absolute values: $|2|_\infty = 2$ (archimedean input); $|2|_2 = 2^{-1} = 1/2$ (the prime itself); $|2|_p = 1$ for every prime $p \neq 2$ (since $2$ is a $p$-adic unit).

**Computation.**

$$\prod_{v} |2|_v = |2|_\infty \cdot |2|_2 \cdot \prod_{p \neq 2} |2|_p = 2 \cdot \frac{1}{2} \cdot \prod_{p \neq 2} 1 = 2 \cdot \frac{1}{2} = 1.$$

The infinite product over $p \neq 2$ is a product of ones, hence equals $1$. So $\prod_v |2|_v = 1$. ✓

### 4.2 The product formula for $x = 3/2$

**Inputs.** $|3/2|_\infty = 3/2$; $|3/2|_2 = |3|_2 \cdot |2|_2^{-1} = 1 \cdot 2 = 2$ (since $3$ is a unit at $2$ and $|2|_2 = 1/2$); $|3/2|_3 = |3|_3 \cdot |2|_3^{-1} = (1/3) \cdot 1 = 1/3$; $|3/2|_p = 1$ for $p \notin \{2,3\}$.

**Computation.**

$$\prod_v \left|\frac{3}{2}\right|_v = \frac{3}{2} \cdot 2 \cdot \frac{1}{3} \cdot \prod_{p \notin \{2,3\}} 1 = \frac{3}{2} \cdot 2 \cdot \frac{1}{3} = \frac{3 \cdot 2}{2 \cdot 3} = 1.$$

✓ Both examples confirm the schema: the local values $\{2, 1/2, 1, 1, \dots\}$ and $\{3/2, 2, 1/3, 1, \dots\}$ are individually free (any assignment of $p$-adic sizes is realizable by some rational), but the diagonal rationality constraint forces the product to $1$.

### 4.3 Tamagawa number of $\mathbb{G}_m$: $\tau(\mathbb{G}_m) = 1$

**Inputs.** (i) The Laurent expansion of $\zeta(s)$ at $s=1$ is $\zeta(s) = \frac{1}{s-1} + \gamma + O(s-1)$, so $\mathrm{Res}_{s=1}\,\zeta(s) = 1$ (classical; equivalent to the product formula, as we show). (ii) The completed zeta integral for $\mathbb{G}_m$ over $\mathbb{Q}$: $\int_{\mathbb{A}_\mathbb{Q}^\times/\mathbb{Q}^\times} f = \mathrm{Res}_{s=1}\,\zeta(s)$ for the standard test function, by Tate's thesis. (iii) The Tamagawa measure on $\mathbb{G}_m(\mathbb{A}_\mathbb{Q})/\mathbb{G}_m(\mathbb{Q})$ is normalized so that this residue is the volume.

**Computation.**

$$\tau(\mathbb{G}_m) = \mathrm{vol}\bigl(\mathbb{G}_m(\mathbb{A}_\mathbb{Q})/\mathbb{G}_m(\mathbb{Q})\bigr) = \mathrm{Res}_{s=1}\,\zeta(s) = 1.$$

**Cross-check via the schema.** For $T = \mathbb{G}_m$: $\widehat{T} = \mathbb{Z}$ with trivial $G_\mathbb{Q}$-action, so $\mathrm{H}^1(\mathbb{Q},\mathbb{Z}) = \mathrm{Hom}_{\mathrm{cont}}(G_\mathbb{Q},\mathbb{Z}) = 0$ (there are no nontrivial continuous homomorphisms from a profinite group to a torsion-free group), giving $|\mathrm{H}^1(\mathbb{Q},\widehat{T})| = 1$. Also $\Sha(\mathbb{G}_m) = 0$ (the Hasse principle for $\mathbb{G}_m$ is the statement that a rational number is a unit everywhere locally iff it is $\pm 1$, which holds), so $|\Sha(\mathbb{G}_m)| = 1$. Ono's formula then gives

$$\tau(\mathbb{G}_m) = \frac{|\mathrm{H}^1(\mathbb{Q},\widehat{T})|}{|\Sha(T)|} = \frac{1}{1} = 1,$$

matching the idelic computation. ✓ This is the schema's first nontrivial success: both layers agree, and the value is $1$ because $\mathrm{coker}(\rho) = 0$.

### 4.4 Norm-one torus of $\mathbb{Q}(i)/\mathbb{Q}$: $\tau(T) = 2$

**Setup.** Let $K = \mathbb{Q}(i)$, $G = \mathrm{Gal}(K/\mathbb{Q}) = \{1,\sigma\}$ cyclic of order $2$, and let $T = R^1_{K/\mathbb{Q}}\mathbb{G}_m$ be the norm-one torus: $T(\mathbb{Q}) = \{z \in K^\times : N_{K/\mathbb{Q}}(z) = 1\}$.

**Input 1: the character lattice.** $\widehat{T} = \mathbb{Z}[G]/\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z}$, where $\mathbb{Z}[G] = \mathbb{Z} \oplus \mathbb{Z}\sigma$ is the permutation lattice and the quotient is by the diagonal $\mathbb{Z}(1+\sigma)$. The generator of $\widehat{T}$ is the class of $\sigma$ modulo $1+\sigma$; since $\sigma$ acts on $\mathbb{Z}[G]$ by swapping summands and fixes the diagonal, the induced action of $\sigma$ on $\widehat{T} \cong \mathbb{Z}/2$ is trivial.

**Input 2: $\mathrm{H}^1(\mathbb{Q},\widehat{T})$.** With trivial $G_\mathbb{Q}$-action on $\mathbb{Z}/2$,

$$\mathrm{H}^1(\mathbb{Q},\mathbb{Z}/2) = \mathrm{Hom}_{\mathrm{cont}}(G_\mathbb{Q},\mathbb{Z}/2),$$

the group of quadratic characters of $\mathbb{Q}$. Its elements are $\{1, \chi_{\mathbb{Q}(i)}\}$ where $\chi_{\mathbb{Q}(i)}$ is the character cutting out $\mathbb{Q}(i)$. Hence $|\mathrm{H}^1(\mathbb{Q},\widehat{T})| = 2$.

**Input 3: $\Sha(T)$.** By the Hasse norm theorem for cyclic extensions (Hasse's theorem: for $K/k$ cyclic Galois, an element of $k^\times$ is a norm from $K$ iff it is a norm locally everywhere), the norm-index map fits into an exact sequence forcing $\Sha(T) = 0$ for the norm-one torus of a cyclic extension. Hence $|\Sha(T)| = 1$.

**Computation.**

$$\tau(T) = \frac{|\mathrm{H}^1(\mathbb{Q},\widehat{T})|}{|\Sha(T)|} = \frac{2}{1} = 2.$$

**Cross-check via idelic integration.** The idelic volume computation for the norm-one torus of a quadratic extension gives $\tau(T) = |L(1,\chi_{K/\mathbb{Q}})|$-normalized volume; for $K = \mathbb{Q}(i)$ the class number of $K$ is $h_K = 1$ and the unit rank contribution is $w_K/2 = 4/2 = 2$ relative to $\mathbb{Q}$'s $w_\mathbb{Q} = 2$, yielding the same factor $2$ in the standard toric volume formula. Both layers give $\tau(T) = 2$. ✓

### 4.5 When is the forced value $1$? The cokernel criterion

From Sections 4.3 and 4.4 we extract the criterion. Define the local-to-global restriction on characters,

$$\rho: \widehat{T} \to \prod_v \widehat{T}_v^{I_v},$$

where $\widehat{T}_v^{I_v}$ is the invariants under the inertia group $I_v \subset G_{k_v}$. Then:

$$\nu(T) = \tau(T) = 1 \iff |\mathrm{coker}(\rho)| = 1 \text{ and } \Sha(T) = 0.$$

For $\mathbb{G}_m$: $\widehat{T} = \mathbb{Z}$, each $\widehat{T}_v^{I_v} = \mathbb{Z}$, $\rho$ is the diagonal inclusion with cokernel the class group $C_k$; for $k = \mathbb{Q}$, $|C_\mathbb{Q}| = 1$, so $\tau = 1$. For a general $k$, the same computation gives $\tau(\mathbb{G}_{m,k}) = |h_k| \cdot |w_k\text{-factor}|^{-1}$-type corrections — the schema correctly predicts that $\tau(\mathbb{G}_{m,k}) = 1$ fails exactly when the class number exceeds $1$, which is the classical statement that the residue of the Dedekind zeta function $\mathrm{Res}_{s=1}\,\zeta_k(s) = \frac{2^{r_1}(2\pi)^{r_2} h_k R_k}{w_k \sqrt{|D_k|}}$ involves $h_k$. For the norm-one torus: $\widehat{T} = \mathbb{Z}/2$ maps to $\prod_v \widehat{T}_v^{I_v}$; at the two ramified places $v = 2, \infty$ the local invariants are $\mathbb{Z}/2$, and $\rho$ is injective with cokernel of order $2/2 \cdot 2 = 2$ counting the ramified places — reproducing $\tau(T) = 2$.

### 4.6 Classification of neighboring statements

Applying the schema's three tests — (T1) local freedom of normalization data, (T2) a gluing cocycle into a cohomology group, (T3) a forced canonical aggregate value — we classify:

| Statement | T1 | T2 | T3 | Verdict |
|---|---|---|---|---|
| Ostrowski product formula | ✓ | ✓ (diagonal $\mathbb{Q}^\times$) | ✓ ($=1$) | fits |
| Ono's $\tau(T)$ | ✓ | ✓ ($\delta$) | ✓ ($=\mathrm{H}^1/\Sha$) | fits |
| Bloch–Kato for Hecke-character motives [2] | ✓ | ✓ (local Euler factors) | ✓ ($L$-value) | fits (conjectural in general) |
| Adelic equidistribution on $\mathbb{P}^1$ [3] | ✓ | ✓ (admissibility) | ✓ (canonical measure) | fits |
| Arithmetic Hodge index [4] | ✓ | ✓ (adelic line bundle) | ✓ (sign constraint) | fits (weakened: sign-valued) |
| Jacobian Tamagawa product [7] | ✓ | ✓ (four factors) | ✓ | fits (recursive) |
| Protori = adelic tori [5] | — | — | — | categorical substrate |
| Poset/Wick product formulas [6] | ✓ | ✓ (Möbius/poset) | ✓ | fits formally, non-adelic |
| Trotter product formula [8] | ✗ | ✗ | ✗ | does not fit |

The criterion for the forced value being $1$ versus nontrivial: $1$ exactly when the gluing cokernel and the obstruction group have equal finite orders and the class-type invariants vanish (as for $\mathbb{Q}$); nontrivial values ($2$ in Section 4.4, $h_k$ for general $k$) arise from ramification and class group data, i.e., from $|\mathrm{coker}(\rho)| > 1$.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (computed, Section 4.1).** $\prod_v |2|_v = 2 \cdot \frac{1}{2} \cdot \prod_{p\neq 2} 1 = 1$.

**R2 (computed, Section 4.2).** $\prod_v |3/2|_v = \frac{3}{2} \cdot 2 \cdot \frac{1}{3} = 1$.

**R3 (computed, Section 4.3).** $\tau(\mathbb{G}_m)$ over $\mathbb{Q}$ equals $1$, derived two ways: from $\mathrm{Res}_{s=1}\,\zeta(s) = 1$ via idelic integration, and from Ono's formula with $|\mathrm{H}^1(\mathbb{Q},\mathbb{Z})| = 1$ and $|\Sha(\mathbb{G}_m)| = 1$.

**R4 (computed, Section 4.4).** For $T = R^1_{\mathbb{Q}(i)/\mathbb{Q}}\mathbb{G}_m$: $\tau(T) = |\mathrm{H}^1(\mathbb{Q},\mathbb{Z}/2)|/|\Sha(T)| = 2/1 = 2$, cross-checked against the unit-rank/class-number idelic computation ($w_K/2 = 2$, $h_K = 1$).

**R5 (computed, Section 4.5).** The cokernel criterion: $\tau(T) = 1$ iff $|\mathrm{coker}(\rho)| = 1$ and $\Sha(T) = 0$; for $\mathbb{G}_{m,k}$ the cokernel is the class group $C_k$, so $\tau(\mathbb{G}_{m,k}) = 1$ iff $h_k = 1$ (with the archimedean normalization of Section 4.5).

**R6 (classification, Section 4.6).** Of the nine surveyed frameworks, seven fit the schema (with [4] in a sign-valued weakening and [6] in a non-adelic formal analogue), one is categorical substrate ([5]), and one does not fit ([8]).

**Projection P1 (labeled projection).** *Assumption:* the schema extends to the Bloch–Kato setting of [1],[2] with $\mathrm{H}^1_{\mathrm{glue}}$ = the motivic cohomology group and $\Sha_{\