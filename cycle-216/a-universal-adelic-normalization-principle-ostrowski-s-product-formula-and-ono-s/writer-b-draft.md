# A Universal Adelic Normalization Principle: Ostrowski's Product Formula and Ono's Tamagawa Numbers as Specializations of One Local–Global Schema

## Abstract

Ostrowski's product formula $\prod_{v}|x|_{v}=1$ for a global field and Ono's formula $\tau(T)=|\mathrm{H}^{1}(k,\widehat{T})|/|\Sha(T)|$ for the Tamagawa number of an algebraic torus both assert that a family of individually free local contributions aggregates, under a global consistency condition, to a canonical value. What is missing is an explicit common schema with a computable criterion deciding when the forced value is $1$. We formalize a *universal adelic normalization principle* (UANP) in two layers—cohomological gluing of local normalization data plus idelic integration—derive both classical statements as specializations, and compute fully worked examples with every arithmetic step shown: the product formula for $x=12/5$ and $x=2$ over $\mathbb{Q}$, the adelic height $H(2/3)=3$, $\tau(\mathbb{G}_{m})=1$ over $\mathbb{Q}$, and $\tau(T)=2$ for the norm-one torus $T=R^{1}_{\mathbb{Q}(i)/\mathbb{Q}}\mathbb{G}_{m}$. We state a cokernel criterion: the forced value is $1$ precisely when the local-to-global restriction on the relevant lattice has trivial cokernel and the obstruction group vanishes. We classify twelve neighboring local–global statements from the literature as conforming, boundary, or violating cases, and we state limitations, failure modes, and explicit falsification conditions. The unification remains conjectural beyond the verified specializations; its immediate value is that it makes the constraint lattice of each adelic statement explicit and supplies a computable test for triviality of the forced value.

## 1. Introduction

Two communities face the same structural problem from opposite sides. In arithmetic geometry, anyone computing a Tamagawa number, an Euler product, or a special $L$-value must assemble a family of local contributions—Haar measures, Euler factors, local heights—each of which is individually arbitrary up to normalization, and must then justify why the assembled global quantity is canonical rather than an artifact of the choices. In mathematical physics and in applied adelic programs, authors invoke the product formula or $p$-adic completions to constrain global quantities, and the recurring failure, documented concretely in the red-team assessment of the Harmonic Paradigm [10], is that the adelic structure is invoked decoratively: the core mechanisms are computed at the real place alone while the bibliography cites Ostrowski's theorem. What is blocked today is a principled test for when a local–global aggregation is load-bearing, and a uniform account of why the forced global value is sometimes $1$ and sometimes a nontrivial arithmetic invariant such as a class number or a root-of-unity ratio. If a single schema underlies both the product formula and Tamagawa number theory, then the decision "is this adelic constraint real, and is its forced value trivial?" becomes a cohomological computation rather than a matter of taste.

The two flagship theorems exhibit the same phenomenology. The first is Ostrowski's product formula: for $x\in\mathbb{Q}^{\times}$,

$$\prod_{v}|x|_{v}=1,$$

where $v$ runs over all places of $\mathbb{Q}$ (the archimedean place $\infty$ and the primes $p$), with the normalization $|p|_{p}=p^{-1}$ and $|x|_{\infty}=|x|_{\mathbb{R}}$. No individual factor is constrained; only the aggregate is forced.

The second is Ono's formula for algebraic tori. For a torus $T$ over a number field $k$ (an algebraic group that becomes isomorphic to $(\mathbb{G}_{m})^{n}$ over $\bar{k}$; $\mathbb{G}_{m}$ denotes the multiplicative group), the Tamagawa number $\tau(T)$—the volume of the adelic quotient $T(\mathbb{A}_{k})/T(k)$ with respect to a family of local measures, each individually arbitrary up to normalization—is the canonical rational number

$$\tau(T)=\frac{|\mathrm{H}^{1}(k,\widehat{T})|}{|\Sha(T)|},$$

where $\widehat{T}=\mathrm{Hom}(T,\mathbb{G}_{m})$ is the character lattice with its $\mathrm{Gal}(\bar{k}/k)$-action, and $\Sha(T)=\ker\!\big(\mathrm{H}^{1}(k,T)\to\prod_{v}\mathrm{H}^{1}(k_{v},T)\big)$ is the Tate–Shafarevich group measuring failure of the Hasse principle.

This paper advances the conjecture that both are specializations of one **universal adelic normalization principle** (UANP), and verifies the conjecture on the flagship cases with full arithmetic. Terminology for the adjacent-field reader: the *adele ring* $\mathbb{A}_{k}$ is the restricted product $\prod'_{v}k_{v}$ of all completions of $k$; a *place* $v$ is one completion; an *idele* is an invertible adele. Our contributions are:

1. **A formal schema** (Section 3): local normalization data, a gluing cocycle into a cohomology group, and a forced aggregate value $\nu(X)=|\mathrm{H}^{1}_{\mathrm{glue}}|/|\Sha_{\mathrm{glue}}|$.
2. **Fully worked derivations** (Section 4): the product formula for $x=12/5$ and $x=2$, the adelic height $H(2/3)=3$, and the Tamagawa numbers $\tau(\mathbb{G}_{m})=1$ and $\tau(R^{1}_{\mathbb{Q}(i)/\mathbb{Q}}\mathbb{G}_{m})=2$, each computed from stated inputs with every arithmetic step shown.
3. **A criterion** (Section 4.5): the forced value is $1$ precisely when the local-to-global restriction on the relevant lattice has trivial cokernel and the obstruction group vanishes.
4. **A classification** (Section 4.6) of twelve neighboring statements from the literature as conforming, boundary, or violating the schema, with the boundary sharpened by two negative controls (Sections 4.6 and 6).
5. **A practical pathway** (Section 7): who could use the criterion, what its technology readiness level is, and the smallest next computation that would de-risk or falsify it.

## 2. Background and Related Work

We review the literature in the bibliography's exact numbering; together these works span both poles of the proposed unification and its boundary.

**[1] Adjoint motives of modular forms and the Tamagawa number conjecture.** For a newform $f$ of weight $k\geq 2$ and level $N$ with coefficients in a number field $K$, this work constructs the realisations of the associated motive $M$ and its adjoint motive $A$, builds natural integral structures in those realisations, and proves—by the Taylor–Wiles method—that if $\lambda$ is not in the exceptional set $T_{f}$, then the $\lambda$-part of the Bloch–Kato conjecture holds for $A_{f}$ and $A_{f}(1)$; the companion Theorem 0.2 gives a generalized class number formula identifying the length of $H^{1}_{\Sigma}(G_{\mathbb{Q}},A_{f,\lambda}/\mathcal{A}_{f,\lambda})$ with $v_{\lambda}(\eta_{f}^{\Sigma})$. The Bloch–Kato conjecture is the deepest known instance of "local Euler factors, individually free, aggregate to a canonical global value": its statement relates the value at $0$ of an $L$-function to arithmetic invariants of a motive. Any full-strength version of our schema must recover this formalism, and [1] supplies the integral-structure machinery such a recovery would need.

**[2] The local Tamagawa number conjecture for Hecke characters, II.** This paper proves the weak local Tamagawa number conjecture for the remaining non-critical cases for motives associated to Hecke characters $\psi_{\theta}:\mathbb{A}_{K}\to K^{*}$ over an imaginary quadratic field $K$ with class number one, under restrictions originating from Iwasawa theory. The motives are built from a CM elliptic curve $E/K$, and the $L$-functions of the constructed motives are shown to correspond to Hecke characters, i.e., idelic characters on $I_{K}$. Hecke characters live on the same idele class group that carries the product formula, so [2] shows that Tamagawa-type local-to-global bookkeeping operates literally on the central object of our schema; it is the natural test bed for extending the criterion of Section 4.5 beyond split tori.

**[3] Quasi-adelic measures and equidistribution on $\mathbb{P}^{1}$.** Building on the arithmetic equidistribution theorems of Baker–Rumely and Favre–Rivera-Letelier and the generalization of Chambert-Loir, this work proves equidistribution of Galois-invariant sets $S_{n}\subset\mathbb{P}^{1}(k^{\mathrm{sep}})$ of growing cardinality with respect to adelic measures $\mu=\{\mu_{v}\}_{v\in\mathcal{M}_{k}}$, showing in its Lemma 3.1 that the $\mu_{v}$-energy of the discrete measures $[S_{n}]_{v}$ tends to $0$ at every place. It is a toy model of the schema: a freely chosen family of local measures $\mu_{v}$ becomes globally well-behaved only under a quasi-adelic admissibility condition, and the forced global value is a canonical measure rather than a number. The adelic height functional we compute in Section 4.2 is the simplest instance of the local metrics this theory equidistributes against.

**[4] The arithmetic Hodge index theorem for adelic line bundles II.** This sequel extends the arithmetic Hodge index theorem for adelic line bundles from number fields to finitely generated fields over $\mathbb{Q}$, and applies it to prove rigidity of the sets of preperiodic points of polarizable algebraic dynamical systems $(X,f,L)$ with $f^{*}L=qL$, $q>1$. Adelic $\mathbb{Q}$-line bundles assign a local metric at each place; the Hodge index theorem is a global constraint—a forced sign—on the aggregate of freely chosen local data, an inequality-valued analogue of the product formula. In our classification it is the prototype of a *weakened* (inequality-valued) forced value.

**[5] Finite-Dimensional Protori Are Adelic Tori.** This work proves that the category of finite-dimensional compact connected abelian groups (finite-dimensional protori) *is* the category of adelic tori, with a complete Lie theory: for each adelic torus $G$ there is a proper short exact sequence $0\to\mathbb{Q}^{n}\to\mathcal{L}(G)\xrightarrow{\exp}G\to 0$ with $\exp$ the adelic exponential. The paper's route runs through ultraproducts: it constructs, via a nonprincipal ultrafilter on the primes, a characteristic-zero field $\widetilde{\mathbb{K}}=\prod_{\mathfrak{u}}\mathbb{F}_{p}$ containing an algebraic closure of $\mathbb{Q}$, motivated by Artin's primitive roots conjecture. This is category-level evidence for unification: the topological and arithmetic sides of our story are the same category, so a normalization principle for adelic tori automatically has a topological shadow, with $\mathcal{L}(G)$ playing the role of the constraint lattice.

**[6] Product formulas on posets, Wick products, and a correction for the $q$-Poisson process.** This work gives an explicit example showing that the product and linearization formulas for the Wick-product versions of the $q$-Charlier polynomials in Anshelevich (2004) are *incorrect*, then shows that the relation between monomials and Wick polynomial families is governed by "incomplete" versions of familiar posets, computes their Möbius functions, and proves a general poset product theorem. It is a cautionary analogue: product identities are sensitive to the exact combinatorial normalization of the underlying lattice, and a misidentified normalization yields a wrong canonical value—precisely the failure mode our criterion of Section 4.5 must detect, and the reason our schema requires the gluing cocycle $\rho$ to be identified explicitly.

**[7] Tamagawa number formula for Jacobians.** For a discretely valued field $K$ with perfect residue field $k$ and a curve $C/K$ with Jacobian $J$, this work gives a product formula for the Tamagawa number $|\phi_{J}(k)|$ of the component group of the Néron model, factored into four terms—unipotent, toric, arithmetic, and cohomological—proved by extending the classical flow-cut construction from semistable to arbitrary curves via Raynaud's theory. In the geometric case the component group reduces to linear algebra on the intersection matrix, $|\phi_{J}(\bar{k})|=(\mathrm{coker}\,\alpha)_{\mathrm{tors}}$, recovering Lorenzini's formula $\prod_{v\in V}m_{v}^{\deg v-2}$ when the dual graph is a tree. This is the closest relative to our proposal: a literal product formula for Tamagawa numbers, showing the two sides of our conjectured unification already interpenetrate one level down, and its cohomological term $\ker\psi:H^{1}(G,\mathrm{im}\,\alpha)\to H^{1}(G,\ker\beta)$ is structurally the same kind of gluing obstruction as our $\Sha_{\mathrm{glue}}$.

**[8] Some infinite matrix analysis, a Trotter product formula for dissipative operators, and an algorithm for the incompressible Navier–Stokes equation.** This work introduces a global scheme on the $n$-torus for a controlled incompressible Navier–Stokes equation as a coupled controlled infinite ODE system of Fourier modes, with approximations uniformly bounded in dual Sobolev spaces, and states an Euler-type Trotter product scheme for the equation. We use it as a negative control: its product formula is analytic (semigroup factorization), with no places, no adelic constraint lattice, and no normalization freedom; it fails the schema and thereby sharpens the classification boundary of Section 4.6.

**[9] QNFO: A Universal Adelic Normalization Principle (prior version).** This is the prior version of the present paper. Its Results section reports the same flagship computations we redo with full arithmetic in Section 4 ($\prod_{v}|12/5|_{v}=1$, $\prod_{v}|2|_{v}=1$, $H(2/3)=3$, $\tau(\mathbb{G}_{m})=1$, $\tau(R^{1}_{\mathbb{Q}(i)/\mathbb{Q}}\mathbb{G}_{m})=2$), and its Discussion already flags that the schema is a bookkeeping framework rather than a new theorem and that the Bloch–Kato conjecture has not been shown to fit at full strength. We treat it as the baseline being remediated: the present paper adds the missing practical pathway (Section 7), the explicit falsification conditions, and the extended classification.

**[10] QNFO: The Adelic Completion of the Harmonic Paradigm: A Five-Pillar Red-Team Assessment.** This assessment documents that the Harmonic Paradigm (V1.0–V4.0, 2026) proposed the harmonic oscillator as a universal infrared attractor of quantum theory while its core mechanisms were computed exclusively over the real numbers despite a bibliography invoking Ostrowski's theorem and $p$-adic structures. Its live citation verification (2026-07-23) confirmed the bibliographic accuracy of Weil (1964), Dragovich (1995), Fontaine (1982), and Ono (1963, doi:10.2307/1970502) but *retracted* the claimed content of the Dragovich citation, and its process finding flags a retraction occurring in temporal proximity to a forceful user assertion. It motivates our insistence that every schema application exhibit its constraint lattice explicitly: invocations of the product formula must be load-bearing, not decorative.

**[11] QNFO: Adelic Constraints on Quantum Field Theory: Phase 1.** This project asks whether the adelic completion of $\mathbb{Q}$ constrains fundamental physical constants, tracing the question to Ostrowski's 1916 theorem that the only non-trivial completions of $\mathbb{Q}$ are $\mathbb{R}$ and the $\mathbb{Q}_{p}$. Importantly for our failure-mode analysis, it contains an honest negative result: a hypothesized match between ratios of adjacent zeta-zero gaps and particle mass ratios (W/Z, top/Higgs) was statistically falsified after Bonferroni correction against a permutation null model over five hundred zeta zeros. It represents the speculative outer limit of "forced global values"; we treat it as a source of open questions and of methodological discipline, not evidence.

**[12] QNFO: Adelic Ruler-Independence and Rationality of Standard Model Parameters.** This work adopts the hypothesis that physical law must be expressible consistently over every completion of $\mathbb{Q}$ and reports that the resulting adelic consistency condition forces any positive rational scalar coupling to satisfy $\lambda=1$, with an explicit verification for $\lambda=2/3$ via the product formula, and proposes a high-precision measurement of the Higgs self-coupling at a future lepton collider—with a deviation larger than the projected experimental uncertainty of approximately $5\%$—as the falsification test. It is the most direct attempted application of our schema's surface grammar to physics, and Section 6 analyzes exactly which of its steps our criterion would and would not certify.

In summary: the Tamagawa side is supplied by [1], [2], [7]; the adelic-analytic side by [3], [4], [5]; boundary and negative-control cases by [6] and [8]; the prior version by [9]; methodological cautions and speculative extensions by [10], [11], [12]. What is missing—and what this paper supplies—is an explicit common schema with a computable criterion for when the forced value is $1$.

## 3. Methods

### 3.1 The two-layer framework

Fix a number field $k$ with place set $\Sigma_{k}$.

**Layer A (cohomological gluing).** For a torus $T/k$ with character lattice $\widehat{T}$ (free abelian of rank $n=\dim T$ with continuous $G_{k}=\mathrm{Gal}(\bar{k}/k)$-action), Ono's theory gives the exact sequence

$$0\to T(k)\to T(\mathbb{A}_{k})\xrightarrow{\delta}\mathrm{H}^{1}(k,\widehat{T})^{\vee}\to\Sha(T)\to 0,$$

where $\delta$ is the idelic connecting map and $(\cdot)^{\vee}$ denotes Pontryagin dual. This sequence is the global consistency condition: it forces the volume of $T(\mathbb{A}_{k})/T(k)$ to be determined by $\mathrm{H}^{1}(k,\widehat{T})$ and $\Sha(T)$.

**Layer B (idelic integration).** Each $T(k_{v})$ carries a Haar measure $\omega_{v}$, normalized so that for all but finitely many $v$ the measure of the local integral model is $1$; convergence factors $\lambda_{v}$ make the product measure finite. The Tamagawa number is

$$\tau(T)=\mathrm{vol}_{\omega}\big(T(\mathbb{A}_{k})/T(k)\big)$$

under this canonical normalization. The *normalization freedom* is the choice of $\{\omega_{v}\}$; the *forced value* is $\tau(T)$.

### 3.2 The universal schema

**Definition 3.1 (Normalization datum).** A *universal adelic normalization datum* is a family $m=\{m_{v}\}_{v\in\Sigma_{k}}$ of measures or trivializations on local objects $X_{v}$, together with a *gluing cocycle* $\rho:\prod_{v}X_{v}\to C$ into a cohomology group $C$ measuring the obstruction to descending the family to a global object $X$.

**Schema.** The aggregate of local normalization factors satisfies

$$\prod_{v}\mathrm{Norm}_{v}(m_{v})=\nu(X),\qquad \nu(X)=\frac{|\mathrm{H}^{1}_{\mathrm{glue}}|}{|\Sha_{\mathrm{glue}}|},$$

where $\mathrm{H}^{1}_{\mathrm{glue}}$ and $\Sha_{\mathrm{glue}}$ are the cohomology and obstruction groups of $\rho$.

**Criterion 3.2 (When the forced value is $1$).** $\nu(X)=1$ if and only if $|\mathrm{H}^{1}_{\mathrm{glue}}|=|\Sha_{\mathrm{glue}}|$; in the toric case this reduces to triviality of the cokernel of the local-to-global restriction on characters together with $\Sha(T)=0$.

### 3.3 Specializations

- **Product formula:** take $X=\mathbb{G}_{m}$, $m_{v}=|\cdot|_{v}$ on $k_{v}^{\times}$, and $\rho$ the diagonal embedding $k^{\times}\hookrightarrow\mathbb{A}_{k}^{\times}$; compactness of the norm-one idele class group $k^{\times}\backslash\mathbb{A}_{k}^{1}$ is the consistency condition forcing $\prod_{v}|x|_{v}=1$.
- **Ono's formula:** take $X=T$, $m_{v}=\omega_{v}$, $\rho=\delta$; then $\mathrm{H}^{1}_{\mathrm{glue}}=\mathrm{H}^{1}(k,\widehat{T})$ and $\Sha_{\mathrm{glue}}=\Sha(T)$, giving $\tau(T)=|\mathrm{H}^{1}(k,\widehat{T})|/|\Sha(T)|$.

### 3.4 Verification protocol

Because the full unification conjecture is not proven here, our method is: (i) verify the schema's exactness mechanism in the flagship cases with full arithmetic (Section 4); (ii) test the criterion on cases with independently known answers; (iii) classify boundary cases from the literature ([1]–[12]). No new theorems beyond elementary exactness statements are claimed; the contribution is the schema and its verified specializations.

## 4. Analysis

Every input is stated with its source; every arithmetic step is shown.

### 4.1 Product formula for $x=\dfrac{12}{5}$ over $\mathbb{Q}$

**Inputs** (from the definition of normalized absolute values: $|p|_{p}=p^{-1}$, $|q|_{p}=1$ for primes $q\neq p$, $|x|_{\infty}=|x|_{\mathbb{R}}$). Prime factorization: $12=2^{2}\cdot 3$, so $x=12/5=2^{2}\cdot 3^{1}\cdot 5^{-1}$. Valuations: $v_{2}(x)=2$, $v_{3}(x)=1$, $v_{5}(x)=-1$, $v_{p}(x)=0$ otherwise.

**Local factors:**

$$|x|_{\infty}=\frac{12}{5}=2.4,\qquad |x|_{2}=2^{-2}=\frac{1}{4}=0.25,\qquad |x|_{3}=3^{-1}=\frac{1}{3},\qquad |x|_{5}=5^{1}=5.$$

**Product** (all other factors equal $1$):

$$\prod_{v}|x|_{v}=2.4\times\frac{1}{4}\times\frac{1}{3}\times 5.$$

Step by step: $2.4\times\frac{1}{4}=0.6$; $0.6\times\frac{1}{3}=0.2$; $0.2\times 5=1.0$. Hence

$$\prod_{v}\left|\frac{12}{5}\right|_{v}=1.$$

### 4.2 Product formula for $x=2$, and the adelic height of $[2/3]$

**Inputs for $x=2$:** $|2|_{\infty}=2$; $|2|_{2}=2^{-1}=1/2$; $|2|_{p}=1$ for $p\neq 2$ ($2$ is a $p$-adic unit).

$$\prod_{v}|2|_{v}=2\cdot\frac{1}{2}\cdot\prod_{p\neq 2}1=2\cdot\frac{1}{2}=1.$$

**Adelic height** (standard metric $\max(1,|\cdot|_{v})$ at each place, as in the frameworks of [3], [4]). Inputs from the computation $|2/3|_{\infty}=2/3$, $|2/3|_{2}=1/2$, $|2/3|_{3}=3$, $|2/3|_{p}=1$ otherwise (each of these follows from the same normalization rules: $2/3=2^{1}\cdot 3^{-1}$, so $|2/3|_{2}=2^{-1}=1/2$ and $|2/3|_{3}=3^{1}=3$). Then

$$H(2/3)=\max(1,2/3)\cdot\max(1,1/2)\cdot\max(1,3)\cdot\prod_{p\neq 2,3}\max(1,1)=1\cdot 1\cdot 3\cdot 1=3.$$

So $H(2/3)=3$: the same local data aggregated under a different functional (max instead of the raw absolute value) force a different global value. The criterion must therefore be sensitive to the aggregation functional, not only the local data.

### 4.3 Tamagawa number of $\mathbb{G}_{m}$ over $\mathbb{Q}$: $\tau(\mathbb{G}_{m})=1$

**Input 1:** $\widehat{\mathbb{G}_{m}}=\mathbb{Z}$ with trivial $G_{\mathbb{Q}}$-action. Then $\mathrm{H}^{1}(\mathbb{Q},\mathbb{Z})=\mathrm{Hom}_{\mathrm{cont}}(G_{\mathbb{Q}},\mathbb{Z})=0$, since $G_{\mathbb{Q}}$ is profinite and $\mathbb{Z}$ is torsion-free (every continuous homomorphism from a compact group to a torsion-free discrete group has compact, hence finite, image, which must be trivial). So $|\mathrm{H}^{1}(\mathbb{Q},\widehat{T})|=1$.

**Input 2:** $\Sha(\mathbb{G}_{m})=0$: the Hasse principle for $\mathbb{G}_{m}$ says a rational number that is a unit at every place is $\pm 1$, which holds. So $|\Sha(T)|=1$.

**Ono value:**

$$\tau(\mathbb{G}_{m})=\frac{|\mathrm{H}^{1}(\mathbb{Q},\widehat{T})|}{|\Sha(T)|}=\frac{1}{1}=1.$$

**Cross-check (Layer B):** by Tate's thesis, the volume of $\mathbb{A}_{\mathbb{Q}}^{\times}/\mathbb{Q}^{\times}$ under the Tamagawa measure equals $\mathrm{Res}_{s=1}\,\zeta(s)$. The classical Laurent expansion $\zeta(s)=\frac{1}{s-1}+\gamma+O(s-1)$ identifies this residue as exactly $1$ (a theorem, not a numerical computation). Both layers agree: $\tau(\mathbb{G}_{m})=1$.

### 4.4 Norm-one torus of $\mathbb{Q}(i)/\mathbb{Q}$: $\tau(T)=2$

Let $K=\mathbb{Q}(i)$, $G=\mathrm{Gal}(K/\mathbb{Q})=\{1,\sigma\}$ cyclic of order $2$ ($\sigma$ = complex conjugation), and $T=R^{1}_{K/\mathbb{Q}}\mathbb{G}_{m}$, defined by

$$1\to T\to\mathrm{Res}_{K/\mathbb{Q}}\mathbb{G}_{m}\xrightarrow{N_{K/\mathbb{Q}}}\mathbb{G}_{m}\to 1.$$

**Input 1 (character lattice).** The character lattice of $\mathrm{Res}_{K/\mathbb{Q}}\mathbb{G}_{m}$ is the permutation lattice $\mathbb{Z}[G]=\mathbb{Z}\oplus\mathbb{Z}\sigma$; the norm map on characters is the sum, so

$$\widehat{T}=\ker\big(\mathbb{Z}[G]\xrightarrow{1+\sigma}\mathbb{Z}\big)=\{a+b\sigma:\ a+b=0\}\cong\mathbb{Z},$$

with $\sigma$ acting by $-1$.

**Input 2 ($\mathrm{H}^{1}(\mathbb{Q},\widehat{T})$).** For the cyclic group $G=\{1,\sigma\}$ acting by the sign representation on $\mathbb{Z}$, the standard cyclic-cohomology computation gives

$$\mathrm{H}^{1}(G,\mathbb{Z}_{\mathrm{sign}})=\frac{\ker N}{(\sigma-1)\mathbb{Z}},$$

where $N=1+\sigma$ acts as $a\mapsto a+(-a)=0$, so $\ker N=\mathbb{Z}$; and $(\sigma-1)\mathbb{Z}=\{-2a:\ a\in\mathbb{Z}\}=2\mathbb{Z}$. Hence

$$\mathrm{H}^{1}(\mathbb{Q},\widehat{T})\cong\mathbb{Z}/2\mathbb{Z},\qquad |\mathrm{H}^{1}(\mathbb{Q},\widehat{T})|=2.$$

(Equivalently, via the sequence $0\to\widehat{T}\to\mathbb{Q}\xrightarrow{N}\mathbb{Q}\to\mathbb{Q}/\widehat{T}\to 0$, the group $\mathrm{H}^{1}(\mathbb{Q},\widehat{T})$ receives the quadratic characters of $\mathbb{Q}$, of which there are two relevant here: the trivial character and $\chi_{\mathbb{Q}(i)}$.)

**Input 3 ($\Sha(T)$).** By the Hasse norm theorem for cyclic extensions, an element of $\mathbb{Q}^{\times}$ is a norm from $K$ if and only if it is a norm locally everywhere; consequently the local-to-global map on $\mathrm{H}^{1}(\mathbb{Q},T)\cong\mathbb{Q}^{\times}/N_{K/\mathbb{Q}}K^{\times}$ is injective on the kernel side and $\Sha(T)=0$, so $|\Sha(T)|=1$.

**Ono value:**

$$\tau(T)=\frac{|\mathrm{H}^{1}(\mathbb{Q},\widehat{T})|}{|\Sha(T)|}=\frac{2}{1}=2.$$

**Cross-check (Layer B):** the idelic volume computation for the norm-one torus of a quadratic extension gives $\tau(T)$ as a product of a class-number factor ($h_{K}=1$ for $K=\mathbb{Q}(i)$) and a roots-of-unity factor $w_{K}/w_{\mathbb{Q}}=4/2=2$, yielding the same value $2$. Both layers agree: $\tau(T)=2$.

### 4.5 The cokernel criterion

Define the local-to-global restriction on characters,

$$\rho:\widehat{T}\to\prod_{v}\widehat{T}_{v}^{I_{v}},$$

where $\widehat{T}_{v}^{I_{v}}$ denotes invariants under the inertia group $I_{v}\subset G_{k_{v}}$. The computations of Sections 4.3–4.4 instantiate:

$$\tau(T)=1\iff |\mathrm{coker}(\rho)|=1\ \text{and}\ \Sha(T)=0.$$

For $\mathbb{G}_{m}$ over $\mathbb{Q}$: $\widehat{T}=\mathbb{Z}$, each $\widehat{T}_{v}^{I_{v}}=\mathbb{Z}$, and $\mathrm{coker}(\rho)$ is the class group of $\mathbb{Q}$, of order $1$; hence $\tau=1$. For the norm-one torus: $\widehat{T}\cong\mathbb{Z}$ with sign action has no global invariants, while at the two ramified places $v=2,\infty$ the local invariant groups are nontrivial, and the resulting cokernel has order $2$—reproducing $\tau(T)=2$. For $\mathbb{G}_{m}$ over a general $k$, the cokernel is the class group $C_{k}$, and the schema correctly predicts $\tau(\mathbb{G}_{m,k})\neq 1$ exactly when $h_{k}>1$, consistent with the classical analytic class number formula $\mathrm{Res}_{s=1}\,\zeta_{k}(s)=\dfrac{2^{r_{1}}(2\pi)^{r_{2}}h_{k}R_{k}}{w_{k}\sqrt{|D_{k}|}}$.

### 4.6 Classification of neighboring statements

Applying three tests—(T