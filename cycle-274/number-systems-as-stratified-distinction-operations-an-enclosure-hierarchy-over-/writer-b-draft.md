# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark

## Abstract

The received tower of number systems — ℕ, ℚ, ℝ, ℂ, with the p-adic fields ℚ_p and the adele ring 𝔸 attached to ℚ — is usually presented as a list of completions without a common generative principle. The open question is whether this progression can be derived from a single primitive act rather than inherited as mathematical history. We develop a formal sketch in which each number system is the closure of the previous one under a single distinction operation applied to a Laws-of-Form-style mark: tallying gives ℕ, ratio comparison gives ℚ, convergent sequences give the computable reals, lossy projection of a tree-like limit gives the continuum, phase enclosure gives ℂ, divisibility enclosure gives ℚ_p, and simultaneous valuations give 𝔸. We define an information-loss functional Λ as the base-2 logarithm of the ratio of distinguishable-state counts across adjacent strata and compute it explicitly for the tree-to-continuum projection: at tree depth n = 10 over p = 2 and real precision ε = 2⁻³, the tree carries 2¹⁰ = 1024 states, the real enclosure carries 2³ = 8, and Λ = 7 bits; at fixed precision the loss is exactly linear, Λ(n) = n − 3, and vanishes at matched depth n = 3. Finite simultaneous-valuation products over the primes {2, 3, 5} give 30 states at depth 1 and 900 at depth 2. The result converts a philosophical thesis into a family of countable, falsifiable claims and specifies the computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: ℕ ⊂ ℚ ⊂ ℝ ⊂ ℂ, with ℚ_p and 𝔸 attached to ℚ by a branch that textbooks treat as parallel and independent. The cost of this presentation is concrete. A physicist choosing a number system for a model has no principled way to decide whether the continuum is forced or merely conventional; a logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order; a computer scientist working with finite-precision arithmetic has no theory of what information is destroyed when a tree-structured limit is flattened onto a line. If the progression ℕ → ℚ → ℝ → ℂ → ℚ_p → 𝔸 could be derived from increasingly refined acts of distinction, each of these decisions would acquire a criterion: the choice of number system would become a choice of operator, and the cost of each choice would be measurable.

The thesis has existing advocates. The measurement-stratigraphy program proposes that the history of number systems is a sequence of expanding distinction operations, each era adding a new enclosure — marking, comparing ratios, convergent sequences, lossy projection to the continuum, imaginary enclosure, p-adic enclosure [11]. The Adelic Physics Program argues that the physically accessible base field is ℚ rather than ℝ, and that Ostrowski's theorem then forces every p-adic completion of ℚ to be physically meaningful on par with the Archimedean one [10]. The computable-real-boundary argument supplies the primitive vocabulary: a mark whose repeated indication collapses (Calling: two identical indications are one), an enclosure as the boundary a distinction creates, and the claim that the fixed point of finite enclosure operations is exactly the computable reals ℝ_comp [12]. What none of these supplies is a quantitative layer: a number attached to each step that says what the step costs.

This paper adds that layer. We posit a primitive mark M and a family of enclosure operators E_i, each a closure-type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable-state count. The count supports an information-loss functional Λ, defined as the base-2 logarithm of the ratio of state counts across a projection, which we compute in full arithmetic for the tree-to-continuum step — the projection analogous to the lossy-projection enclosure of [11]. Every number reported in Section 5 is derived by hand in Section 4; no simulation, measurement, or external data is used.

The contributions are:

- Explicit state-count derivations for the tally, real-enclosure, and p-adic strata at finite depth, with every arithmetic step shown (Section 4, Derivations 1–3).
- The Monna-projection loss budget: Λ = 7 bits at (p = 2, n = 10, ε = 2⁻³), the exact linearity Λ(n) = n − 3 at fixed precision, and the vanishing of the loss at matched depth n = 3 (Section 4, Derivations 4–5; Results R1–R2).
- Finite simultaneous-valuation product counts of 30 and 900 over the primes {2, 3, 5} at depths 1 and 2, as a toy model of the adele stratum (Section 4, Derivation 6).
- Falsifiability conditions F1–F3 for the stratification, the loss functional, and the operator list, stated so that a single counterexample kills the corresponding claim (Section 3.4, analyzed in Section 6).

## 2. Background and Related Work

The direct ancestor of this paper is the earlier formal sketch of the same conjecture [9], which introduced the seven-operator hierarchy over a mark, the state-count table for the first strata, and the loss functional Λ, while leaving the recovery claims for the continuum, complex, and adele strata as conjectures. We adopt its operator list and its arithmetic and deepen the analysis of what the loss functional does and does not measure.

The stratigraphy thesis itself comes from the measurement-stratigraphy framework [11], which reinterprets the history of number systems as a sequence of expanding distinction operations, each era adding a new enclosure: marking (giving ℕ), comparing ratios (giving ℚ), convergent sequences (giving ℝ_comp), lossy projection to the continuum (giving ℝ), imaginary enclosure (giving ℂ), and p-adic enclosure. That framework also articulates the guiding principle that prior frameworks are "not wrong, but incomplete" — locally validated within a bounded domain yet globally partial — and it maps the same structural pattern (completion, lossy projection, invariant) across physics, computer science, cognitive science, information theory, biology, and sociology. Our contribution relative to [11] is quantitative: where it names the enclosures, we count the distinguishable states each enclosure creates and destroys.

The physical stakes are set by the Adelic Physics Program [10], which argues that the choice of ℝ as the base field of physics is an unjustified assumption: every measurement produces a rational number to finite precision, every simulation operates on finite-precision rationals, and no experiment distinguishes a real number from a rational approximation to it. Its anchor is Ostrowski's theorem, stated there as the classification of every non-trivial absolute value on ℚ as either the Archimedean one or a p-adic one, from which it concludes that ℝ and every ℚ_p are equally legitimate completions of the physical number system. If that thesis holds, our stratification question — how each completion of ℚ arises from a distinct act of distinction — becomes foundational rather than classificatory, because all completions then demand a generative account.

The primitive vocabulary is supplied by the computable-real-boundary work [12], which builds number systems from two primitives of Spencer-Brown's Laws of Form: the mark, whose repeated indication collapses under the Calling rule (two identical indications are one distinction, not two), and the enclosure, the boundary a distinction creates. Its "LoF Number Builder" derives ℕ by iterated marking, positional notation by grouping nested enclosures, and ℚ by enclosing groups for ratios; its central claim is that the fixed point of finite enclosure operations is exactly ℝ_comp, with everything beyond that closure lacking external verifiability. We take over its mark, its Calling rule as the idempotence of the mark (MM = M), and its identification of ℝ_comp as the operationally reachable stratum — which is why our hierarchy contains ℝ_comp as a distinct stratum before the full continuum.

That the tally stratum admits non-canonical realizations is shown by the theory of noncanonical number systems [6], which studies whether every integer has a finite expansion ∑_{i=0}^{ℓ} d_i b^i on an integer base b when the digit set does not contain 0; it proves such digit sets exist and gives infinitely many examples for every base with |b| ≥ 4, including the concrete case that {1, 2} is a valid digit set for base −2. For our hierarchy this is evidence that the enclosure operator E₁, not the particular digit set, is the invariant of the tally stratum — a point we return to as the strongest internal threat to the thesis in Section 6.

The word "stratified" in our title has a precise precedent in the theory of stratified β-numbers [3], which modifies Jones's β-numbers for Carnot groups — numbers β_E(x, r) measuring how closely a set E near a ball sits to an affine line — and proves that an analogue of Jones's traveling salesman theorem on 1-rectifiability holds in any Carnot group when the β-numbers are replaced by stratified ones, generalizing both directions of the theorem. The methodological parallel is exact: in both settings a stratified quantity supplies the correct scale-sensitive measure of how well a discrete object fits a smooth one. Our loss functional Λ plays the analogous role for number systems, measuring how well a tree-like limit fits a line, though [3] operates in Carnot groups and makes no claim about number-system foundations.

That the p-adic stratum carries deep, still-active structure is witnessed by three congruence papers. The first proves, for every prime p ≥ 7, the congruence ∑_{k=1}^{p-1} H_k²/k² ≡ (4/5) p B_{p-5} (mod p²) for harmonic numbers H_n = ∑_{k=1}^{n} 1/k, confirming a conjecture of Z.-W. Sun, along with two similar congruences modulo p² [2]. A second poses many conjectures on congruences involving binomial coefficients and Apéry-like numbers modulo p², with case distinctions governed by representations such as 4p = x² + 27y² [4]. A third extends this program to congruences modulo p³ for the same families of sums, with cases governed by quadratic representations of p modulo 8 [7]. These results show that mod-p^k arithmetic — the internal structure of the divisibility enclosure E₆ — is a live research frontier, which constrains our claim that one operator suffices for the p-adic stratum: the operator generates the field, but the field's internal arithmetic plainly outstrips any single generative act.

Two further works bear on generation and valuation structure. The expository treatment of the Caccetta–Hággkvist conjecture — that a finite directed graph with at least n/k edges out of each vertex contains a directed cycle of length at most k — surveys Hamidoune's proofs of the conjecture for Cayley graphs and vertex-transitive graphs using additive number theory, resting on Kemperman's theorem bounding the growth of product sets in groups [5]. Iterated product-set growth is the combinatorial shadow of our tally operator: repeated application of a generator to a set, and the theorem constrains how fast the reachable set expands. Finally, the super-powers paper proves an equivalence concerning the number ω(s_n) of distinct prime factors of sequences s_n = ∑_{i=1}^{k} ∏_{j=0}^{ℓ} x_{i,j}^{n^j}, showing when ω(s_n) exceeds a super-logarithmic bound for infinitely many n, with the analysis conducted through p-adic valuations υ_p [8]. It is a witness that the valuation-theoretic structure of sequences — the raw material of our E₆ and E₇ strata — is quantitatively accessible.

One further connection: the Tate conjectures paper proves both Tate conjectures for algebraic cycles on products of elliptic curves and abelian surfaces over number fields, via the Hodge and Mumford–Tate conjectures and potential automorphy of ℓ-adic representations [1]. Its objects live over number fields — ℚ and its finite extensions — which is exactly the stratum our hierarchy treats as the pivot; the ℓ-adic cohomology through which the proof runs is itself a valuation-selective theory, one ℓ at a time, echoing the one-prime-at-a-time character of E₆.

## 3. Methods

### 3.1 The mark and the distinction operation

We begin with an undifferentiated mark M satisfying the idempotent law MM = M, the Calling rule of the Laws of Form calculus: re-marking does not double [12]. A distinction operation D is any act that partitions a structure into distinguishable classes. An enclosure operator E is a closure-type operator on structures satisfying S ⊆ E(S), E(E(S)) = E(S), and monotonicity. Each stratum is defined as S_i = E_i(S_{i−1}); the operators are indexed by their target stratum.

### 3.2 The strata

**Stratum 0 (the mark).** S₀ = {M} with MM = M. Distinguishable states: N₀ = 1.

**Stratum 1 (tallying, ℕ).** E₁ is the tally enclosure: iterated juxtaposition of marks, each new mark distinguishable by position in the pile. The generated structure is ℕ with addition. At tally depth n the distinguishable counts are 0, 1, …, n, so N₁(n) = n + 1.

**Stratum 2 (ratio comparison, ℚ).** E₂ encloses pairs of tallies under the equivalence (a, b) ~ (c, d) iff ad = bc. The minimal field of fractions of ℤ is ℚ.

**Stratum 3 (convergent sequences, ℝ_comp).** E₃ encloses Cauchy sequences of rationals under x_n ~ y_n iff |x_n − y_n| → 0. Applied to all Cauchy sequences this gives ℝ; restricted to computable ones it gives ℝ_comp, the stratum that [12] identifies as the fixed point of finite enclosure operations and that [11] names as the third enclosure.

**Stratum 4 (lossy tree projection, the continuum).** E₄ is the Monna-type projection π_M: a rooted tree of nested enclosures, isomorphic at the state-count level to a p-adic ball, is projected onto an ordered line at a real precision ε, discarding the branching metric and keeping linear order. The recovery claim — that π_M applied to the tree limit yields ℝ — is Conjecture C4.

**Stratum 5 (phase enclosure, ℂ).** E₅ encloses the real line with a phase circle: pairs (r, θ) with r ∈ ℝ, θ ∈ ℝ/2πℤ, and multiplication (r, θ) · (r′, θ′) = (rr′, θ + θ′). This matches the imaginary enclosure of [11].

**Stratum 6 (divisibility enclosure, ℚ_p).** E₆ encloses ℚ under a single prime's divisibility: completion with respect to the p-adic absolute value |x|_p = p^{−υ_p(x)}, the valuation υ_p being the exponent of the largest power of p dividing x, in the standard notation of [8]. At depth n the state structure is the residue ring ℤ/p^nℤ with N₆(n) = p^n states.

**Stratum 7 (simultaneous valuations, 𝔸).** E₇ performs all divisibility enclosures at once: 𝔸 = ℝ × ∏_p′ ℚ_p, the restricted product. This is the stratum demanded by the Ostrowski argument of [10]: if the base field is ℚ, every completion is physically meaningful, and the adeles are their simultaneous enclosure.

### 3.3 Morphisms and the loss functional

Between adjacent strata S_i → S_{i+1} we take the canonical map induced by the operator. The information-loss functional is

$$\Lambda_{i \to i+1}(\text{params}) = \log_2 N_i(\text{params}) - \log_2 N_{i+1}(\text{params}),$$

the base-2 logarithm of the ratio of distinguishable-state counts: the number of bits destroyed by the projection. Λ counts states, not structure; this limitation is analyzed in Section 6. For the Monna projection π_M from a depth-n, base-p tree to a line at precision ε, Λ is computed explicitly in Section 4.

### 3.4 Falsifiability conditions

Following the conjecture-with-falsifier discipline that [12] applies to its own fixed-point claim, each recovery claim carries a stated falsifier. **F1** (stratification): exhibit a number system in the sequence that no closure operator over the mark generates. **F2** (loss functional): exhibit a projection whose state-count loss decreases as the source is refined at fixed target precision. **F3** (operator list): exhibit a completion of ℚ outside the list {ℝ, ℚ_p : p prime}.

## 4. Analysis

All inputs are either definitions of Section 3 or stated here; every arithmetic step is shown.

**Input 1.** Tally depth n = 9. Source: chosen parameter.

**Input 2.** Prime p = 2, tree depth n = 10. Source: chosen parameter.

**Input 3.** Real precision ε = 2⁻³: the unit interval partitioned into cells of width 2⁻³. Source: chosen parameter.

**Input 4.** Primes {2, 3, 5} for the finite adele-type product. Source: chosen parameter.

**Derivation 1 (tally states).** With n = 9 marks, the distinguishable counts are {0, 1, …, 9}, so

$$N_1(9) = 9 + 1 = 10.$$

**Derivation 2 (real-enclosure states).** The unit interval [0, 1] partitioned into cells of width ε = 2⁻³ has

$$N_{\mathbb{R}}(\varepsilon) = \frac{1}{\varepsilon} = \frac{1}{2^{-3}} = 2^3 = 8$$

distinguishable cells.

**Derivation 3 (p-adic tree states).** The residue ring ℤ/p^nℤ with p = 2, n = 10 has exactly p^n elements:

$$N_6(10) = 2^{10} = 1024.$$

Equivalently, the rooted binary tree of depth 10 has 2^{10} = 1024 leaves, one per residue class modulo 2^{10}.

**Derivation 4 (Monna loss).** The projection π_M maps the depth-10 binary tree onto the line at precision ε = 2⁻³. The loss is

$$\Lambda_{\text{Monna}} = \log_2 N_6(10) - \log_2 N_{\mathbb{R}}(\varepsilon) = \log_2(1024) - \log_2(8) = 10 - 3 = 7.$$

Check via the ratio form:

$$\Lambda_{\text{Monna}} = \log_2\!\left(\frac{1024}{8}\right) = \log_2(128) = 7,$$

and 2⁷ = 128 confirms the ratio. The projection destroys Λ = 7 bits of distinguishable-state information at these parameters.

**Derivation 5 (linearity and vanishing).** Fix ε = 2⁻³ and vary depth n. Since N₆(n) = 2^n and N_ℝ = 2³,

$$\Lambda_{\text{Monna}}(n) = \log_2(2^n) - \log_2(2^3) = n - 3,$$

which is strictly increasing in n; the loss functional therefore passes falsifiability test F2 at these parameters. At n = 3 the loss is 3 − 3 = 0: a depth-3 binary tree and a precision-2⁻³ real enclosure both have 2³ = 8 states, so the projection is state-count lossless at matched parameters.

**Derivation 6 (finite adele-type product).** With primes {2, 3, 5} at depth n_p = 1 each:

$$N_{\mathbb{A},\text{fin}} = \prod_{p \in \{2,3,5\}} p = 2 \times 3 \times 5 = 30.$$

At depth n_p = 2 each:

$$N_{\mathbb{A},\text{fin}} = 2^2 \times 3^2 \times 5^2 = 4 \times 9 \times 25 = 900.$$

**Derivation 7 (stratum count).** The operator list of Section 3.2 contains seven operators E₁, …, E₇ acting on S₀, producing S₁, …, S₇; total strata including the mark: 7 + 1 = 8.

**Derivation 8 (non-dyadic loss, for the open question of Section 6).** For p = 3, ε = 2⁻³: N₆(n) = 3^n and N_ℝ = 8, so Λ(n) = log₂(3^n) − 3 = n log₂ 3 − 3. Setting Λ = 0 requires n log₂ 3 = 3, i.e., n = 3/log₂ 3 = 3/1.58496… ≈ 1.893, not an integer. Hence no integer depth gives zero loss for p = 3 at ε = 2⁻³: the loss-free matching of Result R2 is a dyadic coincidence, not a general law.

## 5. Results

Every number below is computed in Section 4; no simulation or external measurement is reported.

| Quantity | Value | Source derivation |
|---|---|---|
| Tally states at depth n = 9 | N₁(9) = 10 | Derivation 1 |
| Real cells at ε = 2⁻³ | N_ℝ = 8 | Derivation 2 |
| Binary tree states at depth n = 10 | N₆(10) = 1024 | Derivation 3 |
| Monna loss at (p = 2, n = 10, ε = 2⁻³) | Λ = 7 bits | Derivation 4 |
| Monna loss at depth n, ε = 2⁻³ | Λ(n) = n − 3 | Derivation 5 |
| Loss-free matching depth | n = 3 (Λ = 0) | Derivation 5 |
| Finite adele-type product, depth 1, {2,3,5} | 30 | Derivation 6 |
| Finite adele-type product, depth 2 | 900 | Derivation 6 |
| Total strata (mark + 7 operators) | 8 | Derivation 7 |
| Non-dyadic matching depth for p = 3, ε = 2⁻³ | none (n ≈ 1.893) | Derivation 8 |

**Result R1.** The Monna projection loss is exactly linear in tree depth at fixed real precision: Λ(n) = n − 3 bits for ε = 2⁻³, p = 2.

**Result R2.** There exists a matched-parameter pair (n = 3, ε = 2⁻³) at which the p-adic tree and the real enclosure have identical state counts (2³ = 8), i.e., zero loss. This is the precise sense in which the tree-like limit and the continuum carry "the same information, differently metricized" at matched resolution — and the sense in which any deeper tree carries strictly more information than a fixed-precision continuum.

**Result R3.** The stratum sequence has eight levels including the mark, and the finite simultaneous-valuation product over {2, 3, 5} at depth 1 is 30 states.

**Projection (labeled, not computed as a result).** If the law Λ(n) = log₂(p^n) − log₂(1/ε) holds for general p and ε — an assumption, since we verified state counts only for p = 2 — then for p = 3, n = 5, ε = 10⁻² the projected loss is log₂(243) − log₂(100) ≈ 7.925 − 6.644 ≈ 1.281 bits. The uncertainty is bounded by the unverified generality of the state-count formulas; this figure is a projection under stated assumptions, not a result.

## 6. Discussion

**Limitations.** The recovery claims for strata 4, 5, and 7 are unproven here; state-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth. The loss functional Λ counts states, not structure: two projections can destroy the same number of bits while destroying very different algebra, such as order versus branching. The Monna analysis assumes the tree is exactly a p-adic ball in state count; a general tree-like limit with different branching profiles would change Λ. The finite adele-type product of Derivation 6 is a toy: the true adele ring is a restricted product including the real factor, and the count of 30 says nothing about its topology. Finally, Λ is defined only for finite state counts; at infinite depth both counts diverge and the functional needs a renormalization or a rate formulation.

**Failure modes.** The strongest internal threat comes from the noncanonical number systems of [6]: digit sets without 0 that still give finite expansions for every integer, in infinitely many examples for every base |b| ≥ 4. If E₁ can generate structures other than the canonical ℕ, then "the operator determines the stratum" is false — the operator determines only an equivalence class of digit systems, and a choice point remains inside each stratum. We flag this rather than resolve it. A second threat comes from the congruence literature: the mod-p² harmonic congruences of [2], the mod-p² binomial and Apéry-type conjectures of [4], and the mod-p³ extensions of [7] show that the internal arithmetic of the p-adic stratum involves structures (Bernoulli numbers, Catalan-factor identities, quadratic representation cases) that no single generative act obviously covers; if that depth requires operators beyond E₆, the seven-operator list is incomplete (falsifier F3).

**What would falsify the claims.** F1: exhibit a number system in the historical sequence not generated by any closure operator over the mark. F2: exhibit a projection whose state-count loss decreases with refinement — we proved monotonicity only for the linear family Λ(n) = n − 3 at p = 2. F3: exhibit a completion of ℚ outside {ℝ, ℚ_p : p prime}; by the Ostrowski classification as stated in [10], this should be impossible, which is why the adele stratum is the safest of our conjectures. A fourth falsifier targets Λ itself: if two intuitively different projections have identical Λ but intuitively different information content, Λ is inadequate and must be refined — plausibly along the lines of the stratified β-numbers of [3], which measure fit-to-smooth-object at multiple scales and were introduced precisely because a single non-stratified quantity failed to give sharp two-sided estimates in the Carnot setting.

**Open questions.** (i) Result R2 does not generalize: Derivation 8 shows that for p = 3, ε = 2⁻³, no integer depth gives zero loss, since n = 3/log₂ 3 ≈ 1.893. The general condition is that log₂(p^n) = log₂(1/ε) admit an integer solution, which for dyadic ε requires n log₂ p ∈ ℤ — possible only for p a power of 2, i.e., p = 2. Loss-free matching is therefore a dyadic accident. (ii) Can the simulation program — enumerating distinguishable states, precision, and loss profiles under each operator — be run at scale, and does it reproduce the linearity of R1 beyond p = 2? (iii) What is Λ for the adele stratum, where the product is infinite and restricted? (iv) Does the iterated product-set growth studied via Kemperman's theorem in the additive-combinatorics treatment of Caccetta–Hággkvist [5] give a lower bound on the state growth of E₁, connecting the tally stratum to a proved theorem?

## 7. Practical Implications and Engineering Pathways

**(a) Users and what changes.** This is foundational work; no engineering system changes if it holds today. The proximate users are researchers in foundations of mathematics, mathematical physics, and constructive mathematics, for whom the framework converts the thesis "the number systems are a sequence of distinction operations" from a philosophical position into a countable family of checkable claims: if the result holds, the choice of a number system for a physical model becomes, in principle, a choice among enclosure operators with a measurable loss attached to each, and the Adelic thesis that ℚ_p completions are physically on par with ℝ [10] acquires a bookkeeping tool rather than a slogan.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is TRL 1–2: it is purely analytical, has observed and systematized the basic principles (the state-count and loss definitions), and has not been peer reviewed. Analytical work never exceeds TRL 3; no experimental validation, prototype, or simulation result exists here, and none is claimed.

**(c) The smallest next experiment.** A computational study would enumerate, for each operator E_i and a range of parameters (p ∈ {2, 3, 5, 7}, n ≤ 20, ε ∈ {2^{−m} : m ≤ 16}), the exact distinguishable-state count of source and target and the resulting Λ, and would test the projected law Λ(n) = n log₂ p − log₂(1/ε) against the enumerated counts. The outcome that refutes the framework is a documented case where the enumerated loss decreases as depth increases at fixed precision — a violation of F2 — or where an operator's generated structure is not the intended one, violating F1. The enumeration is finite, exact, and requires only integer arithmetic and exact logarithms at rational arguments.

**(d) Binding constraints.** For the proposed enumeration the constraints are modest: exact-integer computation of p^n for n ≤ 20 is trivial, and the only subtlety is defining "distinguishable states" for strata 4 and 5, where the structures are infinite and a finite-depth truncation must be chosen — that choice is itself an open question flagged in Section 6, not a solved engineering parameter. No materials, manufacturing, or regulatory constraints apply at this stage.

**(e) Order-of-magnitude bounds.** The only quantitative projection available is the one labeled in Section 5: under the assumed general law, p = 3, n = 5, ε = 10⁻² gives Λ ≈ 1.281 bits. No cost, market, or performance figures are derivable from this work, and none is offered.

**(f) Risks and misuse.** The framework could be misused as rhetorical cover for presenting the Adelic thesis as established physics; it is not. It supplies a counting formalism for a conjecture, and the conjecture's physical claims rest on arguments external to this paper [10]. A reader should treat every Λ value here as a statement about idealized finite state counts, not about any physical measurement.

## 8. Conclusion

We have sketched a stratified-hierarchy formalization of the conjecture that ℕ, ℚ, ℝ, ℂ, ℚ_p, and 𝔸 arise from seven successive distinction operations over a mark, aligned with the stratigraphy program [11], the Adelic base-field thesis [10], and the Laws-of-Form-derived account of the computable real boundary [12], and extending the earlier formal sketch [9]. We derived in full arithmetic the finite-depth state counts for the tally, real-enclosure, and p-adic strata; established the exact linearity Λ(n) = n − 3 and the vanishing of the Monna-projection loss at matched depth; showed by explicit computation that loss-free matching is a dyadic accident, failing already at p = 3; and stated the remaining recovery claims as conjectures with explicit falsifiability conditions. The framework is offered as a research program, not a completed theory: its value lies in making the discipline "one stratum, one operator, one measurable loss" precise enough to be attacked.

## References

[1] A note on Tate's conjectures for abelian varieties. arXiv:2112.15164v2. https://arxiv.org/abs/2112.15164v2
[2] Proof of a congruence for harmonic numbers conjectured by Z.-W. Sun. arXiv:1108.1171v2. https://arxiv.org/abs/1108.1171v2
[3] Stratified $