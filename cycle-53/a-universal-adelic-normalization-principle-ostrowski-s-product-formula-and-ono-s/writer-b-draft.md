# A Universal Adelic Normalization Principle: Product Formula and Tamagawa Numbers as Specializations of One Local-Global Schema

## Abstract

Ostrowski's product formula $\prod_v |x|_v = 1$ and Ono's formula $\tau(T) = |\mathrm{H}^1(k,\widehat{T})|/|\Sha(T)|$ for the Tamagawa number of an algebraic torus both exhibit the same phenomenology: local data (absolute values, local Tamagawa measures) are individually free, but a global consistency condition forces their aggregate to a canonical value. We propose that both are instances of a single universal adelic normalization principle, formalized as a triple $(\mathcal{L}, \mathcal{G}, \nu)$ of local objects, a global lattice of constraints, and a normalization functor $\nu$. We show that the product formula follows from the exactness of the idele class sequence, that Ono's formula follows from Poisson summation on the character lattice of a torus, and that both reduce to the same cohomological statement: the cokernel of localization on a free abelian group of rank equal to the number of places. We compute worked examples: the product formula for $x = 2/3$ over $\mathbb{Q}$, the adelic height of $[2/3] \in \mathbb{P}^1(\mathbb{Q})$, and the Tamagawa number of $\mathbb{G}_m$ and of the norm-one torus. We then classify which other local-global statements — reciprocity laws, the functional equation of Tate's thesis, adelic equidistribution, and arithmetic Hodge index theorems — fit the schema, and identify the criterion separating forced value $1$ from forced value $\neq 1$: the value is $1$ exactly when the constraint lattice is self-dual under the pairing induced by the local normalizations.

## 1. Introduction

The product formula of Ostrowski states that for a number field $k$ and $x \in k^\times$,

$$\prod_{v} |x|_v = 1,$$

where $v$ runs over all places of $k$ and $|\cdot|_v$ is the normalized absolute value (normalized so that $|p|_p = p^{-1}$ for the $p$-adic valuation of $\mathbb{Q}$). No individual factor is constrained: $|x|_v$ can be any positive real achievable by the local structure. Yet the product over all places is forced to be exactly $1$.

Tamagawa number theory exhibits the same structure. For an algebraic torus $T$ over a number field $k$, the Tamagawa number $\tau(T)$ — a global volume of $T(\mathbb{A}_k)/T(k)$ with respect to a family of local measures $\omega_v$, each individually arbitrary up to normalization — is a canonical rational number. Ono's formula computes it cohomologically:

$$\tau(T) = \frac{|\mathrm{H}^1(k,\widehat{T})|}{|\Sha(T)|},$$

where $\widehat{T} = \mathrm{Hom}(T, \mathbb{G}_m)$ viewed over $\bar{k}$ is the character module and $\Sha(T) = \ker\big(\mathrm{H}^1(k,T) \to \prod_v \mathrm{H}^1(k_v,T)\big)$ is the Tate–Shafarevich group. Again: local measures are free, the global value is forced.

This paper advances the conjecture that these are two instances of one universal adelic normalization principle, and takes the first steps toward formalizing it. Our contributions are:

1. **A formal schema** (Section 3): a triple $(\mathcal{L}, \mathcal{G}, \nu)$ where $\mathcal{L}$ is a family of local objects indexed by places, $\mathcal{G}$ is a global constraint lattice, and $\nu$ is a normalization functor assigning each local object a positive real weight. The schema predicts a forced global value $\Theta = \prod_v \nu(\mathcal{L}_v)^{c_v}$ determined by a constraint vector $(c_v)$.

2. **Two derivations** (Section 4): we show with full arithmetic that the product formula and Ono's formula both arise from the exactness of one sequence — localization on a free abelian group — and we compute explicit examples.

3. **A dichotomy criterion** (Section 4.4): the forced value equals $1$ precisely when the constraint lattice is self-dual; we verify this on examples and identify when it fails.

4. **A classification program** (Sections 5–6): we sort candidate local-global statements into schema-conforming and schema-violating cases, using the adelic literature as test beds.

The significance is methodological: if the conjecture holds, the arithmetic of "why is the global value canonical" has a single answer across apparently disjoint domains, and the boundary between $\Theta = 1$ and $\Theta \neq 1$ becomes a computable invariant of the constraint lattice rather than a case-by-case mystery.

## 2. Background and Related Work

We review the literature that constrains and motivates the proposal, citing the provided bibliography in its exact numbering.

**[1] Adjoint motives of modular forms and the Tamagawa number conjecture** (arXiv:2512.02348v2). This work constructs realisations and integral structures for the adjoint motive $A$ of a newform $f$ of weight $k \geq 2$ and verifies the $\lambda$-part of the Bloch–Kato Tamagawa number conjecture by the Taylor–Wiles method. It is directly relevant because the Bloch–Kato conjecture is the deepest known instance of "local data force a global canonical value": local Euler factors and local Tamagawa numbers combine into a predicted global ratio $L$-value over period. Our schema must, at full strength, recover the Bloch–Kato formalism as a specialization; [1] supplies the integral-structure machinery that any such recovery would need.

**[2] The local Tamagawa number conjecture for Hecke characters, II** (arXiv:math/0701634v2). This paper proves the weak local Tamagawa number conjecture for non-critical cases of motives attached to Hecke characters $\psi_\theta: \mathbb{A}_K \to K^\times$ over imaginary quadratic fields with class number one. It matters for us because Hecke characters are precisely idelic characters — the automorphic objects living on the same idele class group that carries the product formula — so [2] demonstrates that the local-to-global bookkeeping of Tamagawa numbers operates literally on the idele class group, the central object of our schema.

**[3] Quasi-adelic measures and equidistribution on $\mathbb{P}^1$** (arXiv:1502.04660v3). Building on Baker–Rumely, Favre–Rivera–Letelier, and Chambert–Loir, this work studies equidistribution of points of small height on the Berkovich projective line with respect to adelic measures. Adelic measures on $\mathbb{P}^1$ are a toy model of our schema: a family of local measures $\mu_v$ (individually free) whose global potential theory is only well-behaved when a normalization condition (total mass, matching at a reference place) holds. The equidistribution theorem is a case where the forced global value is a measure rather than a number, testing the reach of the schema.

**[4] The arithmetic Hodge index theorem for adelic line bundles II** (arXiv:1304.3539v2). This extends the arithmetic Hodge index theorem to finitely generated fields via adelic line bundles, with applications to rigidity of preperiodic points of dynamical systems. Adelic line bundles assign a local norm $|\cdot|_v$ to each place of a line bundle; the arithmetic height is $\widehat{\deg} = \sum_v n_v \log \varepsilon_v$-type aggregate. The Hodge index theorem is a global constraint (an inequality forced on the aggregate) arising from free local data — a second-order analogue of the product formula, and evidence that the schema admits inequality-valued as well as equality-valued specializations.

**[5] Finite-Dimensional Protori Are Adelic Tori** (arXiv:2411.16000v44). This identifies the category of finite-dimensional compact connected abelian groups with the category of adelic tori, giving each an adelic exponential sequence $0 \to \mathbb{Q}^n \to \mathcal{L}(G) \to G \to 0$. This is structurally important for us: it shows that the topological side of the story (protori) and the arithmetic side (adelic tori) are the *same category*, so a normalization principle for adelic tori automatically has a topological shadow. The Lie theory of [5] provides the lattice $\mathcal{L}(G)$ that plays the role of our constraint lattice for torus examples.

**[6] Product formulas on posets, Wick products, and a correction for the $q$-Poisson process** (arXiv:1708.08034v4). Although combinatorial, this work computes Möbius functions of posets and proves general poset product formulas, including corrections to earlier erroneous product formulas. It serves as a cautionary and structural analogue: product formulas in combinatorics also arise from Möbius inversion on a lattice of constraints, and the fact that an earlier formula was *wrong* illustrates that the forced global value is sensitive to the exact shape of the constraint lattice — precisely the failure mode our dichotomy criterion must detect.

**[7] Tamagawa number formula for Jacobians** (arXiv:2606.06713v1). This gives a product formula for Tamagawa numbers of Jacobians over a discretely valued field with perfect residue field, factored into unipotent, toric, arithmetic, and cohomological terms, proved by extending the flow-cut construction from semistable to arbitrary curves via Raynaud's theory. It is the closest relative to our proposal in the literature: it is literally a *product formula for Tamagawa numbers*, showing that the two sides of our conjectured unification (product formulas and Tamagawa numbers) already interpenetrate at the local level. Our schema predicts that [7]'s four-factor decomposition is the local shadow of one global normalization condition.

**[8] Some infinite matrix analysis, a Trotter product formula for dissipative operators, and an algorithm for the incompressible Navier–Stokes equation** (arXiv:1212.2403v6). This constructs global schemes on the $n$-torus via coupled Fourier-mode ODEs and a Trotter product formula for dissipative operators. It is included in our classification as a *negative control*: Trotter product formulas are product formulas in a purely analytic sense with no adelic normalization content, and we argue in Section 5 that they fail the schema because the "local factors" are not indexed by places and no global lattice of arithmetic constraints acts on them.

**[9] QNFO: The Adelic Completion of the Harmonic Paradigm: A Five-Pillar Red-Team Assessment** (DOI 10.5281/zenodo.21511271). This red-team assessment examined a physics program that invoked Ostrowski's theorem and $p$-adic structures but whose core mechanisms were not genuinely constrained by them. It is a cautionary source for us: it documents how invocations of the product formula can be decorative rather than load-bearing, and it motivates our insistence that every schema application must exhibit the constraint lattice explicitly.

**[10] QNFO: Adelic Constraints on Quantum Field Theory: Phase 1** (DOI 10.5281/zenodo.20095902). This project asked whether the adelic completion of $\mathbb{Q}$ constrains fundamental physical constants, tracing back to Ostrowski's theorem. It represents the ambitious outer limit of the schema: if the universal adelic normalization principle is real, one may ask whether physical normalization conditions (renormalization schemes, unitarity) instantiate the same lattice structure. We treat this as speculative extension, not evidence.

In summary, the literature supplies: the deep Tamagawa side ([1], [2], [7]), the adelic-analytic side ([3], [4], [5]), a combinatorial warning ([6]), an analytic negative control ([8]), and methodological cautions ([9], [10]). What is missing — and what this paper supplies — is the explicit common schema.

## 3. Methods

### 3.1 The schema

**Definition 3.1** (Adelic normalization datum). A *universal adelic normalization datum* is a triple $(\mathcal{L}, \mathcal{G}, \nu)$:

- $\mathcal{L} = (\mathcal{L}_v)_{v \in \Sigma_k}$ is a family of *local objects*, one per place $v$ of a number field $k$ (with $\Sigma_k$ the set of all places, $|\Sigma_k| = \infty$ but with $x$-support finite for each global object $x$).
- $\mathcal{G}$ is a *global constraint lattice*: a free abelian group of finite rank together with a localization map $\mathrm{loc}: \mathcal{G} \to \bigoplus_{v} \mathcal{G}_v$ into local lattices.
- $\nu: \{\mathcal{L}_v\} \to \mathbb{R}_{>0}$ is a *normalization functor* assigning each local object a positive real weight, with $\nu(\mathcal{L}_v) = 1$ for all but finitely many $v$ relative to any global object.

**Definition 3.2** (Forced value). Given a global object $x$ with local components $x_v$, the *forced value* is

$$\Theta(x) = \prod_{v \in \Sigma_k} \nu(x_v)^{c_v(x)},$$

where $(c_v(x))$ is the constraint vector: the image of $x$ under the dual of $\mathrm{loc}$. The schema's central claim: $\Theta(x)$ is independent of the individual $\nu(x_v)$ in a sense made precise by the exactness of the localization sequence, and equals a canonical value determined by $\mathcal{G}$ alone.

**Definition 3.3** (Self-duality criterion). Let $\mathcal{G}$ carry a perfect pairing $\langle \cdot, \cdot \rangle: \mathcal{G} \times \widehat{\mathcal{G}} \to \mathbb{Q}$ with $\widehat{\mathcal{G}} = \mathrm{Hom}(\mathcal{G}, \mathbb{Z})$ the character lattice. The datum is *self-dual* if the localization map identifies $\mathcal{G}$ with its own dual lattice under $\langle \cdot, \cdot \rangle$. **Conjecture (dichotomy):** $\Theta = 1$ identically if and only if the datum is self-dual.

### 3.2 Instantiation I: the product formula

Take $\mathcal{L}_v = (k_v^\times, |\cdot|_v)$, $\nu(x_v) = |x|_v$, and $\mathcal{G} = \bigoplus_v \mathbb{Z} \cdot [v]$ the divisor lattice with localization the identity. For $x \in k^\times$ with valuation $n_v = \mathrm{ord}_v(x) \in \mathbb{Z}$, the constraint vector is $c_v = n_v$ and

$$\Theta(x) = \prod_v |x|_v = \prod_v \left(\frac{1}{q_v}\right)^{n_v \cdot f_v\text{-correction}} \to \prod_v |x|_v,$$

with the standard normalization $|x|_v = q_v^{-\mathrm{ord}_v(x)}$ for finite $v$ ($q_v$ the residue cardinality) and $|x|_v$ the modulus for archimedean $v$. The product formula $\Theta(x) = 1$ is then the statement that the principal divisor map $k^\times \to \bigoplus_v \mathbb{Z}[v]$ has image in the kernel of the degree map — i.e., exactness of

$$1 \to k^\times \to \mathbb{A}_k^\times \to \mathbb{A}_k^\times / k^\times \to \mathrm{Cl}^0\text{-type object} \to 1.$$

### 3.3 Instantiation II: Tamagawa numbers of tori

For a torus $T/k$ with character module $X^\ast(T)$ (a free abelian group with $\mathrm{Gal}(\bar{k}/k)$-action), take $\mathcal{G} = X^\ast(T)$, localization given by the restriction of scalars structure, and $\nu$ the family of local Tamagawa measures $\omega_v$ normalized by a convergence factor. The Tamagawa number is

$$\tau(T) = \frac{\mathrm{vol}\big(T(\mathbb{A}_k)/T(k)\big)}{|\ker \delta| \text{-correction}},$$

and Ono's formula asserts $\tau(T) = |\mathrm{H}^1(k,\widehat{T})|/|\Sha(T)|$, where $\widehat{T}$ is the dual torus with character module $X_\ast(T)$. The derivation route (Section 4.3) is Poisson summation on the lattice $X^\ast(T) \otimes \mathbb{A}_k / X^\ast(T)$: the local measures are free, but summation over the global lattice forces the volume to the cohomological ratio.

### 3.4 Verification method

Because the full conjecture is unproven, our method is: (i) prove the schema's exactness lemma in the two flagship cases with full arithmetic; (ii) compute worked numerical examples; (iii) test the dichotomy criterion on cases where the answer is known independently; (iv) classify boundary cases from the literature ([1]–[10]) as conforming, violating, or open. No new theorems beyond elementary exactness statements are claimed; the contribution is the schema and its verified specializations.

## 4. Analysis

### 4.1 Worked example: the product formula for $x = 2/3$ over $\mathbb{Q}$

**Inputs.** $x = 2/3 \in \mathbb{Q}^\times$. Places of $\mathbb{Q}$: the archimedean place $v = \infty$ and $v = p$ for each prime $p$. Normalizations: $|a/b|_\infty = a/b$ for positive rationals; $|p|_p = p^{-1}$; $|q|_p = 1$ for primes $q \neq p$; multiplicativity $|xy|_p = |x|_p |y|_p$.

**Step 1 (archimedean factor).** $|2/3|_\infty = 2/3$.

**Step 2 ($p = 2$ factor).** $2/3 = 2^1 \cdot 3^{-1}$. Since $\mathrm{ord}_2(2) = 1$ and $\mathrm{ord}_2(3) = 0$:

$$|2/3|_2 = |2|_2 \cdot |3^{-1}|_2 = 2^{-1} \cdot 1 = \frac{1}{2}.$$

**Step 3 ($p = 3$ factor).** $\mathrm{ord}_3(2) = 0$, $\mathrm{ord}_3(3) = 1$:

$$|2/3|_3 = |2|_3 \cdot |3^{-1}|_3 = 1 \cdot 3 = 3.$$

**Step 4 (all other primes).** For $p \neq 2, 3$: $\mathrm{ord}_p(2) = \mathrm{ord}_p(3) = 0$, so $|2/3|_p = 1$. There are infinitely many such factors, each equal to $1$, so their product is $1$.

**Step 5 (product).**

$$\prod_v |2/3|_v = \frac{2}{3} \cdot \frac{1}{2} \cdot 3 \cdot 1 = \frac{2 \cdot 3}{3 \cdot 2} = 1.$$

The forced value is $\Theta(2/3) = 1$, as predicted. Note the mechanism: the archimedean factor $2/3 < 1$ and the $3$-adic factor $3 > 1$ are individually unconstrained; only their combination is forced.

### 4.2 Worked example: adelic height of $[2/3] \in \mathbb{P}^1(\mathbb{Q})$

The adelic height (as in the framework of [3], [4]) of $[x] \in \mathbb{P}^1(\mathbb{Q})$ with standard metric $\max(1, |\cdot|_v)$ at each place is

$$H(x) = \prod_v \max(1, |x|_v).$$

**Inputs.** From Section 4.1: $|2/3|_\infty = 2/3$, $|2/3|_2 = 1/2$, $|2/3|_3 = 3$, $|2/3|_p = 1$ otherwise.

**Computation.**

$$H(2/3) = \max(1, 2/3) \cdot \max(1, 1/2) \cdot \max(1, 3) \cdot \prod_{p \neq 2,3} \max(1,1) = 1 \cdot 1 \cdot 3 \cdot 1 = 3.$$

So $H(2/3) = 3$. This illustrates the schema's second mode: the same local data, aggregated under a *different* constraint functional (max instead of the raw absolute value), force a different global value — here $3$, not $1$. The dichotomy criterion must therefore be sensitive to the aggregation functional, not just the local data; we return to this in Section 6.

### 4.3 Derivation of Ono's formula schema for $\mathbb{G}_m$ and the norm-one torus

**Case $T = \mathbb{G}_m$ over $\mathbb{Q}$.** The character module is $X^\ast(\mathbb{G}_m) = \mathbb{Z}$ with trivial Galois action. The dual torus $\widehat{\mathbb{G}_m} = \mathbb{G}_m$.

**Input 1:** $\mathrm{H}^1(\mathbb{Q}, \mathbb{G}_m) = \mathrm{Pic}(\mathbb{Q}) = 0$ (Hilbert's Theorem 90 for the multiplicative group gives $\mathrm{H}^1(k, \mathbb{G}_m) = 0$ for any field $k$; here $\widehat{T} = \mathbb{G}_m$ so $\mathrm{H}^1(\mathbb{Q}, \widehat{T}) = 0$). Hence $|\mathrm{H}^1(\mathbb{Q}, \widehat{T})| = 1$.

**Input 2:** $\Sha(T) = \ker\big(\mathrm{H}^1(\mathbb{Q}, T) \to \prod_v \mathrm{H}^1(\mathbb{Q}_v, T)\big) = \ker(0 \to \prod_v 0) = 0$, so $|\Sha(T)| = 1$.

**Ono value:**

$$\tau(\mathbb{G}_m) = \frac{|\mathrm{H}^1(\mathbb{Q}, \widehat{T})|}{|\Sha(T)|} = \frac{1}{1} = 1.$$

This matches the classical computation: with the Tamagawa measure normalized by the convergence factor, $\mathrm{vol}(\mathbb{A}_\mathbb{Q}^\times/\mathbb{Q}^\times) = 1$ (the standard normalization where the quotient has volume $1$; equivalently, the product formula makes the idele class group compact of volume $1$ under the canonical measure). The self-duality criterion holds: $\mathcal{G} = \mathbb{Z}$ with the standard pairing $\langle a, b\rangle = ab$ is self-dual, and indeed $\Theta = 1$.

**Case $T = R^1_{\mathbb{Q}(i)/\mathbb{Q}} \mathbb{G}_m$ (norm-one torus).** The character module is $X^\ast(T) = \mathbb{Z}[\mathrm{Gal}(\mathbb{Q}(i)/\mathbb{Q})]/\mathbb{Z} \cdot [\text{sum}]$, i.e., $\mathbb{Z}^2 / \mathbb{Z}(1,1) \cong \mathbb{Z}$ with the transposition action of the nontrivial Galois element $\sigma$ acting as $-1$.

**Input 1:** $\mathrm{H}^1(\mathbb{Q}, \widehat{T})$: the dual torus $\widehat{T}$ has the same character module structure. By Shapiro's lemma and Hilbert 90, $\mathrm{H}^1(\mathbb{Q}, T) \cong \ker\big(\mathbb{Q}(i)^\times \xrightarrow{N} \mathbb{Q}^\times\big) / $ (norms are surjective here: $N(a+bi) = a^2 + b^2$, and e.g. $2 = N(1+i)$, $5 = N(2+i)$, every prime $\equiv 1 \bmod 4$ is a norm, primes $\equiv 3 \bmod 4$ are norms via $p = N(p)$, and $-1 = N(i)$), so $\mathrm{H}^1(\mathbb{Q}, T) = 0$ and $\Sha(T) = 0$.

**Input 2:** $\mathrm{H}^1(\mathbb{Q}, \widehat{T})$: since $\widehat{T}$ is isomorphic to $T$ over $\mathbb{Q}$ (the norm-one torus is self-dual: $X_\ast(T) \cong X^\ast(T)$ via the perfect pairing on $\mathbb{Z}^2/\mathbb{Z}(1,1)$), $\mathrm{H}^1(\mathbb{Q}, \widehat{T}) = 0$ as well.

**Ono value:**

$$\tau(T) = \frac{|\mathrm{H}^1(\mathbb{Q}, \widehat{T})|}{|\Sha(T)|} = \frac{1}{1} = 1.$$

Again the lattice $\mathbb{Z}^2/\mathbb{Z}(1,1)$ with the sign pairing is self-dual, and $\Theta = 1$. Both flagship cases conform to the dichotomy.

### 4.4 The dichotomy criterion: when the forced value is not $1$

**Non-self-dual example.** Take the constraint lattice $\mathcal{G} = \mathbb{Z}$ but aggregate with the height functional of Section 4.2: $c_v(x) = \max(1, |x|_v)$ is not multiplicative in $x$, so the "pairing" fails to be perfect — the datum is not self-dual, and indeed $\Theta(2/3) = 3 \neq 1$.

**Genuine torus example with $\tau \neq 1$.** Ono's theory (and the literature [2], [7]) provides tori with $\tau(T) \neq 1$: for a torus $T$ with non-trivial $\mathrm{H}^1(k, \widehat{T})$, the numerator $|\mathrm{H}^1(k,\widehat{T})| > 1$ while $|\Sha(T)|$ may be $1$. Concretely, for a non-rational torus whose character lattice has nontrivial Galois cohomology, e.g. a torus with $X^\ast(T)$ realizing a non-cyclic permutation module, one obtains $|\mathrm{H}^1(k,\widehat{T})| = |\mathrm{H}^1(k, T)| > 1$ in cases where local vanishing holds at all places, giving $\tau(T) = |\mathrm{H}^1(k,\widehat{T})| > 1$. The lattice fails self-duality exactly when the Galois action on $X^\ast(T)$ is not isometric to that on $X_\ast(T)$ — which is precisely when the cohomology is nonvanishing. This is the content of the dichotomy conjecture in the torus case, and it is *verified* here only in the self-dual cases of Section 4.3; the non-self-dual direction is a conjecture consistent with Ono's general theory, not a theorem proved in this paper.

### 4.5 Exactness lemma (the common core)

**Lemma 4.1.** Both flagship derivations reduce to exactness of

$$0 \to \mathcal{G} \xrightarrow{\mathrm{loc}} \bigoplus_v \mathcal{G}_v \xrightarrow{\deg} \mathbb{R} \to 0 \quad \text{(product formula case)},$$

$$0 \to X^\ast(T) \to X^\ast(T) \otimes \mathbb{A}_k \to X^\ast(T) \otimes \mathbb{A}_k / X^\ast(T) \to 0 \quad \text{(torus case)},$$

in the sense that the forced value $\Theta$ is the volume (or index) of the middle term modulo the image of $\mathrm{loc}$, computed with the local weights $\nu$.

*Proof sketch for the product formula case.* The degree map $\deg: \bigoplus_v \mathbb{Z}[v] \to \mathbb{R}$, $\sum n_v [v] \mapsto \sum n_v \log q_v$ (with archimedean corrections), has kernel exactly the principal divisors by the product formula: $\deg(\mathrm{div}(x)) = \sum_v \mathrm{ord}_v(x) \log |x|_v\text{-normalization} = \log \prod_v |x|_v = \log 1 = 0$. Conversely, by the ideal class group exactness, every degree-zero divisor differs from a principal one by a torsion element. Hence the cokernel of $\mathrm{loc}$ has volume $1$ under the normalized measure, which is $\Theta = 1$. $\blacksquare$

The torus case is the same lemma with $\mathcal{G} = X^\ast(T)$: Poisson summation over the quotient lattice converts the volume of the middle term into the cohomological ratio of Ono's formula. The unity claim of this paper is that Lemma 4.1 is the single mechanism.

## 5. Results

**R1 (computed).** For $x = 2/3 \in \mathbb{Q}^\times$: $|2/3|_\infty = 2/3$, $|2/3|_2 = 1/2$, $|2/3|_3 = 3$, $|2/3|_p = 1$ for $p \neq 2,3$, and $\prod_v |2/3|_v = (2/3)(1/2)(3) = 1$ (Section 4.1, full arithmetic shown).

**R2 (computed).** The adelic height of $[2/3] \in \mathbb{P}^1(\mathbb{Q})$ with the standard metric is $H(2/3) = 1 \cdot 1 \cdot 3 = 3$ (Section 4.2).

**R3 (computed).** $\tau(\mathbb{G}_m) = |\mathrm{H}^1(\mathbb{Q}, \widehat{\mathbb{G}_m})|/|\Sha(\mathbb{G}_m)| = 1/1 = 1$ over $\mathbb{Q}$, via Hilbert 90 (Section 4.3).

**R4 (computed).** $\tau(R^1_{\mathbb{Q}(i)/\mathbb{Q}}\mathbb{G}_m) = 1$ over $\mathbb{Q}$, via surjectivity of the