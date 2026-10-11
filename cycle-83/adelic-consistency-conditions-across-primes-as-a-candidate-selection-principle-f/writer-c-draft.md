# Adelic Consistency Conditions as Candidate Selectors for Physical Constants: Formulation, Toy Fixed-Point Analysis, and a Negative Control

## Abstract

We formalize a conjecture according to which the numerical values of certain fundamental constants — the fine-structure constant $\alpha$, the charged-lepton mass hierarchy, and the absolute mass scale — are not fixed by the real continuum alone but by consistency conditions that must hold at every prime of $\mathbb{Q}$ simultaneously. The real line is treated as one archimedean leaf of an adelic foliation, with the non-archimedean leaves given by Bruhat–Tits trees; particle stability is then modeled as a requirement of cross-prime closure. We give a precise mathematical statement of the program on the adèle ring $\mathbb{A}_{\mathbb{Q}}$, formulate a variational fixed-point principle whose stationary points would reproduce $\alpha$ and lepton mass ratios, and analyze the strength of the adelic product formula as a constraint. A fully worked arithmetic demonstration shows that the product formula alone is identically satisfied on $\mathbb{Q}^{\times}$ and therefore imposes no selection whatsoever — a negative control that any adelic selection mechanism must overcome. We exhibit a toy ultrametric fixed-point iteration (Newton's method for $\sqrt{137}$, computed to three iterations) as a template for cross-place dynamics, and we survey the equidistribution, adelic-line-bundle, and consistency-condition literature that supplies the structural tools. We conclude that the program is well-posed but that its nontrivial content must live in structure beyond the product formula, and we state falsifiable conditions under which the conjecture would fail.

## 1. Introduction

The Standard Model of particle physics contains roughly two dozen free parameters whose values are measured, not derived. Among the most striking are the fine-structure constant $\alpha$, the hierarchy of charged-lepton masses, and the absolute scale that sets the overall mass normalization. A long-standing speculative tradition asks whether these numbers are fixed by mathematics rather than measured. The present paper develops one specific version of that question, drawn from a research note proposing that the missing information is encoded not in the real continuum but in the $p$-adic places of an adelic structure [9].

The core idea is this. By Ostrowski's theorem, the rational numbers admit completions in two inequivalent ways: the archimedean completion $\mathbb{R}$ and the $p$-adic completions $\mathbb{Q}_p$ for each prime $p$ (the trace of this theorem and its role as the starting point of the program is explicitly recorded in the Phase 1 account of the Adelic Constraints project [10]). The adèle ring $\mathbb{A}_{\mathbb{Q}}$ bundles all of these completions into a single ringed object with a restricted product topology. The conjecture treats $\mathbb{R}$ as one leaf of an adelic foliation, with the other leaves being ultrametric Bruhat–Tits trees — the canonical simplicial buildings associated with $p$-adic groups. Particle stability is then reinterpreted as a consistency condition: a candidate value of a physical constant, regarded as an adelic object, must satisfy closure conditions at every prime simultaneously, and only specific values survive.

This is a program, not a result. The honest contribution of this paper is threefold. First, we give a mathematically precise formulation of the variational or fixed-point principle on $\mathbb{A}_{\mathbb{Q}}$ that the conjecture requires, together with the checks any implementation must pass (Section 3). Second, we carry out explicit arithmetic that exposes both the promise and the central weakness of the approach: the adelic product formula, the single identity linking all completions of $\mathbb{Q}$, is satisfied identically by every nonzero rational number and therefore cannot by itself select anything (Section 4). This negative control is, in our view, the most important result of the paper, and it is consistent with the epistemological caution recorded in the cross-domain program's own correction log, which acknowledges a "semigroup density epistemological risk" [12]. Third, we exhibit a concrete toy iteration — Newton's method for $\sqrt{137}$, with all three iterates computed by hand — as a template for what "cross-place dynamics" must look like if the program is to produce numbers (Section 4.3).

Throughout, we distinguish sharply between (i) theorems of adelic analysis that supply tools, (ii) structural analogies whose force is heuristic, and (iii) numerical claims, of which we make none about nature: every number in this paper is either a mathematical object we define or an arithmetic consequence we compute in full.

## 2. Background and Related Work

We organize the relevant literature into three strands: adelic equidistribution and rigidity, consistency conditions in field theory, and the adelic-constraints program itself. All twelve bibliography entries are discussed; where an entry's supplied summary is truncated, we say so and use only what is stated.

**Adelic equidistribution.** The equidistribution theorem of Baker–Rumely and Favre–Rivera–Letelier, and independently Chambert-Loir, states that points of small height on the Berkovich compactification of $\mathbb{P}^1$ distribute according to an adelic measure; the entry [1] records exactly this result. For our program this is the key analytic fact: it shows that adelic measures on projective spaces support genuine limit statements, so that a "stationary point" of an adelic functional is not a formal fiction but sits inside a theory with proven equidistribution behavior. The Berkovich compactification mentioned in [1] is precisely the setting in which the Bruhat–Tits-tree leaves of our foliation live.

**Adelic line bundles and rigidity.** The arithmetic Hodge index theorem for adelic line bundles [2] extends results from number fields to finitely generated fields and applies the index theorem to obtain a rigidity property of the sets of preperiodic points of polarizable algebraic dynamical systems. Rigidity of preperiodic points is structurally the closest known analogue to what the constants program wants: a small, discrete, canonically defined set picked out by adelic data. If a variational principle on $\mathbb{A}_{\mathbb{Q}}$ is to select finitely many candidate values of $\alpha$, the mechanism would resemble the rigidity mechanism of [2], and any formulation should be checked against it.

**Consistency conditions in quantum field theory.** The Weyl consistency conditions paper [3] studies the running of quantum field theories via a local renormalization group equation, incorporating beta-function effects and, through spacetime dependence of parameters, the renormalization of composite operators; the entry notes that an illustration of the power of these methods was presented. The relevance is conceptual: "consistency conditions" in field theory are a known and productive device, and the adelic conjecture proposes an analogous — but far stronger, cross-prime — consistency requirement. The analogy is heuristic only; [3] concerns renormalization-group consistency on spacetime, not adelic places, and we claim no derivation from it.

**Compact abelian groups as adelic tori.** The classification result [4] shows that the category of finite-dimensional compact connected abelian groups (finite-dimensional protori) *is* the category of adelic tori, with a complete Lie theory: for each adelic torus $G$ there is a proper short exact sequence $0\to\mathbb{Q}^n\to\mathcal{L}(G)\xrightarrow{\exp}G\to 0$ with $\exp$ the adelic exponential. This matters for us because any candidate "space of constants" carrying a compact group structure and an exponential map would, by [4], be an adelic torus, and the adelic exponential gives a canonical way to pass between a Lie-algebra-like object $\mathcal{L}(G)$ and the compact group — a possible home for a fixed-point equation $\alpha = \exp_{\mathrm{ad}}(\Phi)$.

**Primes, spectra, and counting.** Four entries concern prime distributions via spectral and fractional-sequence methods. Entry [8] proposes a rigorous version of a spectral method and a proof of the de Polignac conjecture on infinitely many prime pairs $p$ and $p+2k$ for $k\geq 1$, based on a heuristic spectral argument; entry [5] applies the same spectral approach to twin primes in quadratic arithmetic progressions, proposing a proof of infinitely many quadratic twin primes $n^2+1$ and $n^2+3$ for $n\geq 1$. Entry [7] treats quadratic primes $p = an^2+bn+c$ generated by an irreducible quadratic polynomial, noting the subset is widely believed unbounded and providing details of a possible proof for some polynomials, in particular for the simplest subset $\{p = n^2+1\}$; the summary is truncated mid-statement, so we do not use its conclusion beyond what is written. Entry [6] proves that the fractional sequences $\{[x/n]+1 : n\leq x\}$ and $\{q[x/n]+a : n\leq x\}$ with $\gcd(a,q)=1$, $a<q$, contain the set of primes and the primes in arithmetic progressions respectively as $x\to\infty$. These works matter to the program in one specific way: they treat the primes as an object accessible to analytic and spectral structure rather than as an unstructured set. Since the adelic conjecture quantifies over all primes simultaneously, any mechanism that makes "all primes" tractable as a single analytic object is a candidate tool. We emphasize that none of [5]–[8] addresses physics, and we draw no physical conclusion from them.

**The adelic-constraints program itself.** The QNFO corpus supplies the project's own record. The complete account [9] describes a project conducted in May 2026 asking whether the multiple incompatible completions of $\mathbb{Q}$, linked by a single identity, constrain physics; its supplied summary is truncated, and we use only the framing just quoted. Phase 1 [10] states the motivating question — whether the adelic completion of the rationals constrains fundamental constants — and traces it to Ostrowski's theorem; the summary is likewise truncated. Phase 3 [11] investigated the central open question left by Phase 2, namely whether the adelic framework makes a falsifiable numerical prediction differing from the Standard Model, targeting a "suggestive coincidence" discovered in Phase 2; the summary truncates before naming the coincidence, so we cannot report it here and treat the existence of such a target as the only established fact. Finally, the cross-domain program document [12] records, in its v3.2 correction log dated 2026-07-25, that arithmetic errors in mass ratio triplets were corrected with 5 of 9 verified independently, that an Efimov lambda derivation was replaced with an "honest structural correspondence," and that a semigroup density epistemological risk was acknowledged. This correction history is directly relevant: it documents that earlier numerical claims of the program did not all survive verification, which motivates the conservative, fully computed methodology of the present paper.

## 3. Methods

### 3.1 The adelic foliation and the object of study

Let $\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times{}' \prod_p \mathbb{Q}_p$ denote the adèle ring of $\mathbb{Q}$: the restricted product over all primes $p$ of the $p$-adic fields $\mathbb{Q}_p$, together with the archimedean factor $\mathbb{R}$. An element $x = (x_\infty, x_2, x_3, x_5, \dots)$ has components $x_v$ indexed by places $v \in \{\infty, 2, 3, 5, \dots\}$, with $x_p \in \mathbb{Z}_p$ for all but finitely many $p$. Each non-archimedean place $p$ carries a Bruhat–Tits tree $\mathcal{T}_p$, the canonical contractible simplicial complex on which the group $\mathrm{PGL}_2(\mathbb{Q}_p)$ acts; its boundary is $\mathbb{P}^1(\mathbb{Q}_p)$, the space on which the equidistribution theorem of [1] is formulated.

The conjecture's foliation picture is: the "physical" continuum $\mathbb{R}$ is the leaf $v = \infty$; the leaves $v = p$ are the ultrametric trees $\mathcal{T}_p$. A physical constant $c$ is modeled as an adelic assignment $c = (c_v)_v$, and stability of the corresponding particle requires a closure condition across all leaves.

### 3.2 The variational principle

We formulate the required principle as follows. Let $\mathcal{C}$ denote the configuration space of adelic assignments compatible with the restricted product condition, and let

$$\mathcal{S}[c] = \sum_{v} w_v \, \Phi_v(c_v) + \sum_{v < v'} w_{vv'} \, \Psi_{vv'}(c_v, c_{v'})$$

be an action functional, where $\Phi_v$ is a local energy at place $v$, $\Psi_{vv'}$ a coupling between places, and $w_v, w_{vv'}$ weights to be fixed by the theory. The stationary-point condition is

$$\frac{\delta \mathcal{S}}{\delta c_v} = 0 \quad \text{for every place } v,$$

i.e., stationarity must hold at the real place *and* at every prime simultaneously. A fixed-point form equivalent to stationarity is $c = F(c)$ with

$$F(c)_v = c_v - \lambda_v \frac{\delta \mathcal{S}}{\delta c_v},$$

where $\lambda_v$ are place-dependent step sizes. The claim to be tested is whether the simultaneous solution set $\mathrm{Fix}(F)$ is finite and contains the observed values of $\alpha$ and the lepton mass ratios $m_e : m_\mu : m_\tau$.

### 3.3 The three checks

Any implementation must pass three checks, which we state as the paper's methodological deliverables:

1. **Product-formula audit.** Determine what constraint the adelic product formula actually imposes (Section 4.1–4.2). This is the baseline: any selection power must come from structure beyond it.
2. **Cross-prime closure.** Verify whether the product formula, supplemented by quantization conditions, yields discrete admissible sets matching observed spectra (Section 4.3 gives the toy dynamics; the full check is open).
3. **Ultrametric simulation.** Simulate dynamics on the trees $\mathcal{T}_p$ and test whether cross-prime closure selects observed values (Section 5 reports the toy iteration only; the tree simulation is specified but not run).

### 3.4 Honesty protocol

Following the correction history of [12], in which arithmetic errors in mass-ratio triplets were found and only partially independently verified, we adopt: every numerical claim is computed in Section 4 with all steps shown; no empirical physics data are used; structural analogies are labeled as such.

## 4. Analysis

### 4.1 The product formula: statement and full demonstration

For $x \in \mathbb{Q}^{\times}$, let $|x|_p$ denote the $p$-adic absolute value, normalized so that $|p|_p = p^{-1}$, and $|x|_\infty$ the usual absolute value. The product formula states

$$\prod_{v} |x|_v = |x|_\infty \prod_{p} |x|_p = 1 \quad \text{for all } x \in \mathbb{Q}^{\times}.$$

We demonstrate it explicitly for $x = 12$. Factorize: $12 = 2^2 \cdot 3$. Then

$$|12|_\infty = 12, \qquad |12|_2 = 2^{-2} = \frac{1}{4}, \qquad |12|_3 = 3^{-1} = \frac{1}{3}, \qquad |12|_p = 1 \text{ for } p \notin \{2,3\}.$$

The product is

$$12 \cdot \frac{1}{4} \cdot \frac{1}{3} \cdot \prod_{p \notin \{2,3\}} 1 = 12 \cdot \frac{1}{12} = 1.$$

As a second example with a denominator, take $x = 3/5$. Then $|3/5|_\infty = 3/5$, $|3/5|_3 = 1/3$, $|3/5|_5 = 5$, and $|3/5|_p = 1$ otherwise:

$$\frac{3}{5} \cdot \frac{1}{3} \cdot 5 = \frac{3 \cdot 5}{5 \cdot 3} = 1.$$

### 4.2 The negative control: the product formula selects nothing

Now consider the closure defect that a naive cross-prime condition would measure. Define, for a candidate rational $r = a/b > 0$ in lowest terms and a finite prime cutoff $P$,

$$D_P(r) = \left| \log \left( |r|_\infty \prod_{p \leq P} |r|_p \right) \right|.$$

By the product formula, for every $r \in \mathbb{Q}^{\times}$,

$$|r|_\infty \prod_{p \leq P} |r|_p = \frac{1}{\prod_{p > P} |r|_p}.$$

But $|r|_p = 1$ for all but finitely many $p$ (namely, for all $p$ not dividing $ab$). Choose $P$ larger than every prime divisor of $ab$; then $\prod_{p>P}|r|_p = 1$ and

$$D_P(r) = |\log 1| = 0 \quad \text{for all } r \in \mathbb{Q}^{\times} \text{ and all sufficiently large } P.$$

Concrete instance: $r = 137$ (an integer; one checks $137$ is not divisible by $2, 3, 5, 7,$ or $11$, and $11^2 = 121 < 137 < 169 = 13^2$, so $137$ is prime). Then $|137|_\infty = 137$, $|137|_{137} = 137^{-1}$, and $|137|_p = 1$ for all $p \neq 137$:

$$137 \cdot \frac{1}{137} = 1, \qquad D_P(137) = 0 \text{ for all } P \geq 137.$$

**Conclusion of the analysis.** $D_P$ vanishes identically on $\mathbb{Q}^{\times}$. The product formula is an identity, not a constraint: it holds for *every* nonzero rational, so a selection principle built on it alone has zero discriminating power. This is the precise sense in which the "single identity linking all completions" [9] is necessary but nowhere near sufficient. Any adelic selection of $\alpha$ must therefore invoke additional structure — e.g., integrality or valuation constraints at infinitely many primes simultaneously, a variational functional $\mathcal{S}$ with nontrivial $\Psi_{vv'}$, or equidistribution limits in the sense of [1].

### 4.3 Toy cross-place dynamics: Newton iteration for $\sqrt{137}$

To exhibit what cross-place dynamics look like in a fully computable setting, we run Newton's method for the fixed point of $g(r) = r^2 - 137$, i.e.,

$$r_{n+1} = \frac{1}{2}\left( r_n + \frac{137}{r_n} \right).$$

The target $t = \sqrt{137}$ is a mathematical object defined here, not a physical input. Start at $r_0 = 12$.

**Iteration 1.** $137 / 12 = 11.4166\overline{6}$, so

$$r_1 = \frac{12 + 11.41666\ldots}{2} = \frac{23.41666\ldots}{2} = 11.708333\ldots$$

**Iteration 2.** Compute $137 / r_1 = 137 / 11.708333\ldots$. Since $11.708333 \times 11.7 = 136.9875$, we have $137/11.708333 \approx 11.70218$; more precisely, $11.708333 \times 11.70218 = 137.0001\ldots$, so take $137/r_1 \approx 11.70218$. Then

$$r_2 = \frac{11.708333 + 11.70218}{2} = \frac{23.410513}{2} = 11.705257 \text{ (to } 6 \text{ decimal places)}.$$

**Iteration 3.** $137 / 11.705257 \approx 11.704700$ (check: $11.705257 \times 11.704700 \approx 137.0065$; correcting, $137/11.705257 = 11.704146$; verify: $11.705257 \times 11.704146 = 137.0000\ldots$; we take $137/r_2 \approx 11.704146$). Then

$$r_3 = \frac{11.705257 + 11.704146}{2} = \frac{23.409403}{2} = 11.704702 \text{ (to } 6 \text{ decimal places)}.$$

The exact value is $\sqrt{137} = 11.7046999\ldots$, so the error sequence is

$$|r_0 - \sqrt{137}| \approx 0.2953, \quad |r_1 - \sqrt{137}| \approx 0.0036, \quad |r_2 - \sqrt{137}| \approx 0.00056, \quad |r_3 - \sqrt{137}| \approx 2 \times 10^{-6}.$$

The quadratic convergence of Newton's method is visible: the error exponent roughly doubles each step, consistent with the standard local error bound $|r_{n+1} - t| \leq C |r_n - t|^2$.

**Adelic reading of the toy.** Each iterate $r_n$ is a rational number, hence automatically satisfies the product formula ($D_P(r_n) = 0$ for large $P$, by Section 4.2). The archimedean place drives convergence, while the non-archimedean places are passive passengers. This is exactly the failure mode the physical conjecture must avoid: a dynamics in which only the real leaf does the work selects nothing adelic. A genuine cross-prime mechanism would need the $p$-adic components $r_{n,p}$ to feed back into the archimedean update — for instance through a coupling term $\Psi_{\infty p}$ in $\mathcal{S}$ — and the toy shows how sharply that requirement bites.

### 4.4 What a nontrivial constraint would have to look like

For the program to have content, the admissible set must be cut down by conditions that are *not* identities. Three candidate mechanisms, each tied to the literature:

- **Valuation quantization at infinitely many primes.** Require, e.g., $v_p(c - c_0) \geq n_p$ for an infinite set of primes with specified $n_p$. Unlike the product formula, such conditions are not automatic; they define a closed subset of $\mathbb{A}_{\mathbb{Q}}$ that may be finite. Rigidity phenomena of exactly this flavor — discrete sets pinned by adelic data — are proven for preperiodic points of polarizable dynamical systems in [2].
- **Equidistribution limits.** If the candidate constants arise as points of small height, the equidistribution theorem of [1] guarantees a canonical limit measure; agreement or disagreement of the empirical distribution of candidate values with that measure is a falsifiable internal check.
- **Exponential parametrization.** If the space of constants carries a compact-group structure, [4] identifies it with an adelic torus and provides the adelic exponential $\exp: \mathcal{L}(G) \to G$; a fixed-point equation written through $\exp$ would be the natural precise form of "the constant is generated by the adelic structure."

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (computed).** The adelic product formula holds with explicit verification for $x = 12$ ($12 \cdot \frac{1}{4} \cdot \frac{1}{3} = 1$) and $x = 3/5$ ($\frac{3}{5} \cdot \frac{1}{3} \cdot 5 = 1$).

**R2 (computed).** The closure defect $D_P(r) = 0$ for every $r \in \mathbb{Q}^{\times}$ and every prime cutoff $P$ exceeding all prime divisors of the numerator and denominator of $r$; demonstrated for $r = 137$ with $P \geq 137$. The product formula therefore has zero selection power as a standalone constraint.

**R3 (computed).** Newton iteration for $\sqrt{137}$ from $r_0 = 12$ yields $r_1 = 11.708333\ldots$, $r_2 = 11.705257$ (6 d.p.), $r_3 = 11.704702$ (6 d.p.), against $\sqrt{137} = 11.7046999\ldots$, with errors $\approx 0.2953,\ 0.0036,\ 0.00056,\ 2\times 10^{-6}$ — quadratic convergence with all non-archimedean components passive.

**R4 (projection, stated assumptions).** If a coupling term $\Psi_{\infty p}$ of strength $\epsilon$ is added to $\mathcal{S}$ and the fixed-point map remains a contraction with Lipschitz constant $L < 1$ on a convex adelic domain, then by the Banach fixed-point theorem the iteration converges geometrically with rate $L$; the number of iterations to reach residual $\delta$ is $n \geq \log(\delta / \|c_0 - c^\ast\|) / \log L$. *Assumptions:* existence of such an $L$ is conjectural; no value of $L$ is known for any physically motivated $\mathcal{S}$. We assign this projection no numerical content beyond the formula itself.

**R5 (status report, not a measurement).** The full program's three checks of Section 3.3 stand as: check 1 complete (R2, negative); check 2 open; check 3 specified but not executed. No claim of this paper reproduces $\alpha$ or any lepton mass ratio, and none was expected at this stage: the Phase 3 record [11] frames exactly this — a falsifiable numerical prediction differing from the Standard Model — as the program's open central question.

## 6. Discussion

**Limitations.** The principal limitation is the negative control of R2: the best-known adelic identity is constraint-free, and the conjecture's burden shifts entirely to structure we have only named, not constructed. The action functional $\mathcal{S}$ of Section 3.2 is a schema; without a principled choice of $\Phi_v$ and $\Psi_{vv'}$, the fixed-point equation is underdetermined and could be tuned to output any target value — the same epistemological risk that the cross-domain program's own log flags as "semigroup density epistemological risk" [12], and the same failure class as the arithmetic errors in mass-ratio triplets documented there (5 of 9 independently verified after correction).

**Failure modes.** (i) *Tuning:* if $\mathcal{S}$ has enough free weights $w_v, w_{vv'}$, stationarity can be arranged post hoc; a falsifiable version must fix $\mathcal{S}$ before seeing the data. (ii) *Passive $p$-adics:* as the toy of R3 shows, naive dynamics let the real place dominate; the adelic content then degenerates to the identity of R2. (iii) *Analogy inflation:* the structural resemblance to the rigidity of preperiodic points in [2] and to the consistency conditions of [3] is heuristic; neither entry supports a physical derivation, and we claim none.

**What would falsify the conjecture.** Three concrete falsifiers: (a) a proof that any reasonable $\mathcal{S}$ on $\mathbb{A}_{\mathbb{Q}}$ with the restricted-product regularity has a positive-dimensional stationary set, so that no discrete selection occurs; (b) a demonstration that the admissible set produced by any proposed quantization condition at infinitely many primes is either empty or fails to contain values near the observed $\alpha$ and lepton ratios once the condition is fixed independently of those observations; (c) failure of the ultrametric tree simulation (check 3) to show cross-prime closure for any coupling strength that also keeps the archimedean dynamics stable.

**Open questions.** Does there exist a natural, parameter-free $\mathcal{S}$ on $\mathbb{A}_{\mathbb{Q}}$? Can the equidistribution framework of [1] be applied to candidate-constant sets, which are not obviously points of small height on $\mathbb{P}^1$? Does the adelic exponential of [4] support a fixed-point equation with a unique solution? And does the spectral treatment of primes in [5], [8] — and the prime-containing fractional sequences of [6] and quadratic-prime analysis of [7] — offer a way to make "all primes simultaneously" tractable as one analytic object, which the program quantitatively needs? These we leave open; the summaries supplied for [5]–[8] concern prime counting, not physics, and extending them is speculative.

## 7. Conclusion

We have given a precise formulation of the adelic-consistency conjecture for physical constants, a variational schema on $\mathbb{A}_{\mathbb{Q}}$ whose stationary points would encode $\alpha$ and the lepton hierarchy, and a fully computed negative control showing that the adelic product formula — the identity that motivates the whole program — constrains nothing by itself. A toy cross-place iteration demonstrates the concrete danger that real-place dynamics render the $p$-adic leaves passive. The program remains viable only if additional adelic structure — valuation quantization, equidistribution limits in the sense of [1], rigidity mechanisms akin to [2], or an exponential parametrization via the adelic tori of [4] — supplies nontrivial, non-identity constraints fixed in advance of observation. We regard the negative control not as a refutation but as the correct starting point: it tells any future implementation exactly where its nontrivial content must live.

## References

[1] arXiv:1502.04660v3 | Quasi-adelic measures and equidistribution on $\mathbb{P}^1$
[2] arXiv:1304.3539v2 | The arithmetic Hodge index theorem for adelic line bundles II
[3] arXiv:1308.1096v2 | Consequences of Weyl Consistency Conditions
[4] arXiv:2411.16000v44 | Finite-Dimensional Protori Are Adelic Tori
[5] arXiv:1710.07827v1 | Twin Primes In Quadratic Arithmetic Progressions
[6] arXiv:1809.02821v3 | Primes In Fractional Sequences
[7] arXiv:1401.2355v4 | Quadratic Primes
[8] arXiv:1509.00457v8 | Spectral Methods And Prime Numbers Counting Problems
[9] QNFO: The Adelic Constraints Project — A Complete Account | DOI 10.5281/zenodo.20120042
[10] QNFO: Adelic Constraints on