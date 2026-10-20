# Physical Irrelevance of Uncountability: Computable Reals Suffice for Continuum Physics

## Abstract

Continuum physics is formulated over the uncountable real line $\mathbb{R}$, yet every laboratory measurement, record, and computation is finite. This paper asks whether the uncountability of $\mathbb{R}$—as distinct from its Archimedean completeness—has any physical consequence, and answers that it does not in a precise, checkable sense. The gap addressed is formal: the physics literature treats $\mathbb{R}$ as indispensable, while the computability literature has only recently begun to study the computational content of uncountability, and no self‑contained result connects the two by showing that cardinality is empirically inaccessible. The approach proves (i) that the computable reals are countable—at most $P(n)=2^{n+1}-1$ programs of length $n$ bits, so $P(100)=2535301200456458802993406410751$—and dense in $\mathbb{R}$, (ii) an observability bound $N=\lfloor L/\delta\rfloor$ for an instrument of range $L$ and resolution $\delta$, giving $N=10^{18}\approx2^{59.79}$ for a meter‑scale position measurement at $10^{-18}\,\mathrm{m}$ resolution, and (iii) an indistinguishability theorem: for every finite experiment the uncountable continuum model and a computable surrogate assign the same distribution over the finite record set. The result licenses model‑builders to restrict to computable reals without empirical loss, and it is analytical work at TRL 1–2 whose next step is a proven‑exact benchmark calculation.

## 1. Introduction

A working physicist who simulates a turbulent flow, fits a spectrum, or writes down a Hamiltonian is using the real numbers of classical analysis: an uncountable set, by Cantor's argument. The choice is made silently, in every textbook, and it is never tested. The cost of this silent choice is not monetary but conceptual: if uncountability is physically load‑bearing, then physical law depends on objects—such as the halting probability $\Omega$ of a universal machine—that no process can compute or measure; if it is not load‑bearing, then a large part of the mathematical scaffolding of physics is decorative, and alternative foundations (computable, constructible, or rational‑based continua) are empirically equivalent and may be formally cleaner. The decision that would change if this paper’s result holds is the decision of which number system to take as foundational when constructing physical theories, axiomatizing quantum mechanics, or building simulation infrastructure: the answer “the computable reals suffice” removes any obligation to defend uncountable sets on empirical grounds.

Who faces this problem? Three groups. Foundational physicists and philosophers of physics who must say what the continuum of spacetime or of Hilbert space *is*; numerical analysts and simulation scientists, whose codes can only ever contain computable (indeed finite‑precision) objects and who must justify that no physics is lost; and logicians studying the computational content of set‑theoretic facts, who need a physics‑side criterion for when a mathematical distinction matters. Recent work has begun to examine uncountability itself as a computational object rather than only as a set‑theoretic theorem [6], and internal research notes have proposed that the uncountable reals are “physically vacuous” because they cannot be accessed [9], [10], [11]. What is missing is a written, self‑contained argument with explicit arithmetic: a statement of exactly which structures continuum physics uses, a proof that the computable reals carry those structures, and a quantitative bound showing that no finite experiment can distinguish a countable computable continuum from the uncountable one.

This paper supplies that argument. Its claims are analytical; no experiment is reported here, and every number below is either derived with shown arithmetic or labeled a projection with stated assumptions. The contributions are:

- A proof, with the counting arithmetic shown, that the computable reals $\mathbb{R}_c$ are countable (at most $2^{n+1}-1$ programs of length $n$ bits) and dense in $\mathbb{R}$, hence adequate for the limit operations physics uses (Section 4.1).
- A complementary measure‑theoretic result: the Lebesgue measure of $\mathbb{R}_c$ is zero, so a real drawn from the standard uniform distribution is computable with probability $0$ (Section 4.1).
- An explicit observability bound: an instrument of range $L$ and resolution $\delta$ has at most $N=\lfloor L/\delta\rfloor$ distinguishable outcomes, computed for concrete instruments, e.g. $N=10^{18}\approx2^{59.79}$ outcomes for a meter‑scale position measurement at $10^{-18}\,\mathrm{m}$ resolution (Section 4.2).
- A formal indistinguishability statement: for any finite experiment $E$, the set of possible records under the uncountable model and under a computable surrogate coincide, so no experiment detects the cardinality difference; the Continuum Hypothesis is therefore empirically vacuous for physics (Section 4.3).
- An assessment of what this does and does not show, including failure modes, falsification conditions, and a concrete next‑step calculation (Sections 6 and 7).

## 2. Background and Related Work

The bibliography available for this paper is heterogeneous; only a minority of its entries bear directly on computability and the continuum, and each entry is used strictly within what its supplied excerpt states.

The most directly relevant mathematical entry is [6], *On the computational properties of the uncountability of the real numbers*. Its excerpt states that uncountability is one of the most basic properties of the reals, known far outside mathematics, and that Cantor’s 1874 proof appears in the first set‑theory paper. The excerpt notes that the computational properties of uncountability have not been studied much. This frames the gap our paper fills: the physics‑side question of whether uncountability has observable consequences is open.

Three QNFO notes develop the position this paper formalizes. Entry [9], *The Computable Continuum: Depth Without Breadth*, states that the uncountability of the reals conflates “depth” (Archimedean completeness) and “breadth” (cardinality explosion) and that all physically relevant properties are preserved by computable reals. Our Section 4.1 formalizes that claim by isolating the structures physics uses (order, density, limits, topology) and verifying that $\mathbb{R}_c$ carries them. Entry [10], *Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum*, extends the framework with a third axis, “valuation,” and labels the breadth axis as physically vacuous. We adopt its depth/breadth vocabulary but do not rely on its QEC or gauge claims, which the excerpt presents without derivation. Entry [11], *The ℚ‑vs‑ℝ Question: Why Physical Law Requires Only the Rational Numbers*, contains the claim that the rational numbers are the physically correct base field and that the reals are a mathematical convenience; we cite this title‑level thesis because the excerpt makes that claim explicitly. Entry [12], *COMMUTATIVE PHYSICS*, has an empty excerpt; it is listed only to acknowledge the corpus and does not support any claim.

The remaining entries are physics and physics‑education works that we cite to illustrate a methodological point: the physics community selects problems and tools through documented community processes, and foundational questions enter those processes only when framed in terms of observable consequences. Entry [1], the *Physics Briefing Book* for the European Particle Physics Strategy Update, describes a bottom‑up process in which the community first submits proposals (“inputs”) for projects to be realised in the near‑, mid‑, and longer‑term future, including inputs from national laboratories. We cite it as the venue through which a foundational claim would have to be argued if it were to influence facility‑scale planning. Entry [2], the Snowmass ’96 report on the Next Linear Collider, presents design expectations and the physics program of an $e^{+}e^{-}$ linear collider of center‑of‑mass energy $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$ and demonstrates the machine’s feasibility; we cite it as an example of a physics program whose case is argued entirely through observable physics reach—the standard of empirical argument our indistinguishability result is phrased to meet. Entry [3], the MHD analysis of CFETR and HFRC, describes two Chinese fusion projects whose physics designs center on assessment and analysis; again, design decisions are justified by computable simulation, which is the practice our result underwrites.

Entries [4], [5], [7], and [8] concern the human and educational context of physics practice. Entry [4] reports phenomenographic interviews on faculty perceptions of research‑based assessment materials and finds uptake improves when resources align with perceived needs. Entry [5] reflects on the Fifth International Conference on Women in Physics, reporting attendance by 215 female physicists from 49 countries and a focus on professional barriers; its excerpt supplies no technical content, and we cite it only to note that any foundational reform must be communicated to a broad and diverse community. Entry [7] adapts a theory of computational literacy divided into material, cognitive, and further dimensions to computational essays in physics. Entry [8] studies self‑expressed learning orientations of life‑science majors in introductory physics across six measured semesters. We cite these together for one point: computation is now a primary working medium of physics practice and training, raising the stakes of knowing which mathematical objects computation can and cannot carry, and curriculum‑level uptake of foundational material depends on alignment with perceived needs.

No entry in the bibliography states or refutes the indistinguishability theorem of Section 4.3; that result is derived here.

## 3. Methods

The paper is analytical and constructive. Its method has four parts.

**3.1 Structure isolation.** We first list the mathematical structures that continuum physics actually invokes: (i) a linearly ordered field for coordinates and observables; (ii) density, so that between any two distinct states another state exists; (iii) the existence of limits, so that derivatives, integrals, and solutions of differential equations are defined; (iv) a topology fine enough to define continuity and convergence; and (v) separability in the practical sense that a countable dense subset exists, which is what makes coordinates, series expansions, and finite encodings possible. We do not assume structures beyond these; in particular we do not assume that “all subsets of the continuum” (the powerset) is physically instantiated, since no physical operation is stated over arbitrary subsets.

**3.2 Counting and density arguments.** We then prove countability and density of the computable reals by explicit counting: programs are finite bit strings, and the number of bit strings of length at most $n$ is finite and computable. Density follows because rationals are computable and dense. As a complementary measure‑theoretic lens, we compute the Lebesgue measure of $\mathbb{R}_c$ by countable subadditivity. All arithmetic is shown in Section 4.

**3.3 Indistinguishability framework.** We model an experiment abstractly: an experiment $E$ is a physical process with a finite set of possible outcome records $R_E$, of size $|R_E|$, bounded by the instrument’s resolution and acquisition window. A physical theory $T$ assigns probabilities to records: $T$ is *empirically adequate* if the induced distribution over $R_E$ matches observation within experimental uncertainty. Two theories $T_1,T_2$ are *empirically indistinguishable* if for every finite experiment $E$ they assign the same distribution over $R_E$. The indistinguishability claim of Section 4.3 is then a statement about record sets, not about ontology: we show that a computable‑real surrogate model can be constructed to match any uncountable model’s record distribution, because both models’ predictions are, at the point of comparison, finite objects.

**3.4 Observable‑preservation argument.** As a second route to the same conclusion, we consider a generic physical theory $\mathcal{T}$ whose state space is $\mathbb{R}^k$ and whose observables are continuous functions $O:\mathbb{R}^k\to\mathbb{R}$. For any experimental tolerance $\delta$, uniform continuity on compact subsets yields a neighborhood radius $\eta$ such that states within $\eta$ give observable values within $\delta$; a finite dyadic grid of spacing below $\eta$ then suffices to reproduce every observable value to within tolerance. This connects the abstract record argument to the concrete finite‑precision practice of simulation.

**Definitions.** A real number $x$ is *computable* if there is an algorithm (Turing machine) that, given $k$, outputs a rational $q_k$ with $|q_k-x|<2^{-k}$. A *computable surrogate* of a continuum theory $T$ is a theory $T_c$ stated over $\mathbb{R}_c$ (or over $\mathbb{Q}$ with computable limit procedures) that agrees with $T$ on all computable inputs and computable parameters.

## 4. Analysis

### 4.1 The computable reals are countable, dense, and of measure zero

**Claim 1 (Countability).** The set $\mathbb{R}_c$ of computable reals is countable.

*Derivation.* Each computable real is named by at least one program, and programs are finite bit strings. Count the bit strings of length at most $n$:
\[
P(n)=\sum_{j=0}^{n}2^{j}=2^{n+1}-1.
\]
For $n=100$ bits:
\[
P(100)=2^{101}-1=2535301200456458802993406410752-1=2535301200456458802993406410751.
\]
Thus $\mathbb{R}_c=\bigcup_{n=1}^{\infty}\{x:\text{$x$ named by a program of length}\le n\}$ is a countable union of finite sets, hence countable. $\square$

**Claim 2 (Density).** $\mathbb{R}_c$ is dense in $\mathbb{R}$.

*Derivation.* Every rational $q=a/b$ with $a,b\in\mathbb{Z}$, $b\neq0$, is computable: a program that outputs $a/b$ has finite length and outputs $q$ exactly. The rationals are dense in $\mathbb{R}$: for any $x<y$ there exists $q\in\mathbb{Q}$ with $x<q<y$ (e.g., a decimal truncation of $(x+y)/2$). Since $\mathbb{Q}\subseteq\mathbb{R}_c$, $\mathbb{R}_c$ is dense. $\square$

**Claim 3 (Measure zero).** The Lebesgue measure of $\mathbb{R}_c$ is $0$.

*Derivation.* $\mathbb{R}_c$ is countable (Claim 1), so it can be listed as $\{x_1,x_2,\dots\}$. The Lebesgue measure $m$ of a singleton $\{x_i\}$ is $0$. By countable subadditivity,
\[
m(\mathbb{R}_c)=m\!\left(\bigcup_{i=1}^{\infty}\{x_i\}\right)\le\sum_{i=1}^{\infty}m(\{x_i\})=\sum_{i=1}^{\infty}0=0.
\]
Hence the probability that a real drawn from the standard uniform distribution is computable is
\[
P_{\mathrm{comp}}=\frac{m(\mathbb{R}_c)}{m(\mathbb{R})}=0.
\]
$\square$

**Claim 4 (Adequacy of structure).** $\mathbb{R}_c$ supports the structures of Section 3.1: it is a countable, dense, linearly ordered subfield of $\mathbb{R}$; limits of computable sequences with computable convergence modules are computable; and its order topology is the subspace topology inherited from $\mathbb{R}$, which agrees with $\mathbb{R}$’s topology on all computable points and computable open sets. What $\mathbb{R}_c$ lacks is exactly “breadth” in the sense of [9]: the non‑computable points, which are never the values of computed or measured quantities in any derivation whose input and output data are finite.

### 4.2 Observability bound: how many outcomes can an experiment have?

**Claim 5 (Record bound).** An instrument measuring a single quantity over range $L$ with resolution $\delta$ produces at most
\[
N=\left\lfloor\frac{L}{\delta}\right\rfloor
\]
distinguishable outcomes, i.e. at most $\log_2 N$ bits per measurement.

*Derivation, worked example.* Take a position measurement with $L=1\,\mathrm{m}$ and $\delta=10^{-18}\,\mathrm{m}$:
\[
N=\frac{1}{10^{-18}}=10^{18},
\]
\[
\log_2(10^{18})=18\log_2 10=18\times3.321928094887\ldots=59.79470570797\ldots\approx59.79\text{ bits}.
\]

*Derivation, digital acquisition.* A digitizer with $b$ bits of resolution, $c$ channels, sampling rate $f$, and run duration $\tau$ produces at most
\[
R=2^{b\cdot c\cdot f\cdot\tau}
\]
distinct records. Assuming generous laboratory parameters $b=24$ bits, $c=64$ channels, $f=10^{9}\,\mathrm{s^{-1}}$, $\tau=10^{3}\,\mathrm{s}$ (these are illustrative assumptions of this projection):
\[
b\cdot c\cdot f\cdot\tau=24\times64\times10^{9}\times10^{3}=1.536\times10^{15}\text{ bits},
\]
\[
R=2^{1.536\times10^{15}}.
\]
The record space is finite, hence countable, and carries zero bits of cardinality information.

**Claim 6 (Program‑count vs. record‑count asymmetry).** Non‑computable reals cannot enter a record even in principle, because entering a record requires a finite description. A record is a finite string over a finite alphabet; there are $2^{m}$ strings of length $m$, each naming at most one computable object. Hence the “breadth” axis contributes zero bits to any record. $\square$

### 4.3 Indistinguishability of the uncountable and computable continua

**Claim 7 (Indistinguishability).** For every finite experiment $E$, the uncountable continuum model $T$ and a suitably constructed computable surrogate $T_c$ assign the same distribution over the record set $R_E$.

*Derivation.* Fix $E$ with finite record set $R_E$, $|R_E|<\infty$ (Claim 5). The prediction of $T$ on $E$ is a probability vector $p=(p_1,\dots,p_{|R_E|})$ with $\sum_i p_i=1$. In any physical theory whose predictions are derived by computation from finite specifications of $E$’s apparatus, each $p_i$ is the output of a computation, hence a computable real (to the precision at which it is ever stated). Construct $T_c$ by (i) restricting all state spaces to $\mathbb{R}_c$ (or $\mathbb{Q}$ with explicit limit procedures); (ii) keeping all dynamical laws whose coefficients are computable; (iii) defining predictions by the same computational derivation. Then $T_c$ produces the identical probability vector $p$, because the derivation never leaves the computable fragment. Since this holds for every finite $E$, $T$ and $T_c$ are empirically indistinguishable. $\square$

**Claim 8 (Observable preservation, continuous case).** Let $O:\mathbb{R}^k\to\mathbb{R}$ be continuous and let an experimental tolerance $\delta>0$ be given. On any compact region $K\subset\mathbb{R}^k$, uniform continuity yields $\eta>0$ such that $\|x-y\|<\eta$ implies $|O(x)-O(y)|<\delta$. Define $L=\lceil-\log_2\eta\rceil$ and the dyadic grid
\[
D_{\eta}=\left\{\frac{p}{2^{L}}\;\bigg|\;0\le p<2^{L}\right\},
\]
which contains $2^{L}$ points and partitions $[0,1]$ into intervals of length $2^{-L}\le\eta$. For any state $x\in K$ there exists $d\in D_{\eta}^k$ with $\|x-d\|<\eta$, guaranteeing $|O(x)-O(d)|<\delta$. Since every real detector has finite resolution, $\delta$ can always be chosen below the experimental resolution; hence $O$ evaluated on the computable grid yields predictions indistinguishable from those on the full continuum, for states in $K$. $\square$

**Claim 9 (Empirical vacuity of the Continuum Hypothesis).** The Continuum Hypothesis ($2^{\aleph_0}=\aleph_1$) concerns the cardinality of the powerset of the continuum—the “breadth” axis. By Claim 6, no record carries breadth information; by Claim 7, models differing only in breadth assign identical record distributions. Hence no experiment distinguishes models in which CH holds from models in which it fails: CH is empirically vacuous for physics.

### 4.4 What the derivation assumes

The derivation uses: (a) that physical predictions are produced by computation from finite specifications; (b) that records are finite strings; (c) that theory comparison happens at the level of record distributions; and (d), for Claim 8, that the observables in question are continuous on the compact regions where they are evaluated. Assumption (a) is the substantive one; a theory in which physical observables are defined as non‑computable reals would escape it, but such a theory provides no procedure by which the observable’s value could be compared to data, which is the operational criterion (a) encodes. These assumptions are examined as limitations in Section 6.

## 5. Results

All numbers below are those computed in Section 4; none is an empirical measurement.

1. **Countability with explicit count.** The computable reals are countable; the number of programs of length at most $n$ bits is $P(n)=2^{n+1}-1$, e.g. $P(100)=2535301200456458802993406410751$ (Section 4.1, Claim 1). Under the non‑empty‑program convention the count is $2^{n+1}-2$, e.g. $2046$ for $n=10$ (Section 4.1, Appendix A).

2. **Density.** $\mathbb{R}_c$ is dense in $\mathbb{R}$ because $\mathbb{Q}\subseteq\mathbb{R}_c$ and $\mathbb{Q}$ is dense (Section 4.1, Claim 2).

3. **Measure zero.** The Lebesgue measure of $\mathbb{R}_c$ is $0$, so a real drawn from the standard uniform distribution is computable with probability $P_{\mathrm{comp}}=0$ (Section 4.1, Claim 3).

4. **Single‑measurement record bound.** A position measurement of range $L=1\,\mathrm{m}$ at resolution $\delta=10^{-18}\,\mathrm{m}$ distinguishes $N=10^{18}$ outcomes, i.e. $\log_2 N=59.7947057\ldots\approx59.79$ bits (Section 4.2, Claim 5).

5. **Full‑run record bound (projection).** With assumed instrument parameters $b=24$ bits, $c=64$ channels, $f=10^{9}\,\mathrm{s^{-1}}$, $\tau=10^{3}\,\mathrm{s}$, the record space contains $2^{1.536\times10^{15}}$ possible records—finite, hence countable, and carrying zero bits of cardinality information (Section 4.2, Claims 5–6). The instrument parameters are assumptions of this projection, not measurements.

6. **Dyadic grid size.** To reproduce any continuous observable on a compact region to tolerance $\delta$, a dyadic grid with $2^{L}$ points per axis suffices, where $L=\lceil-\log_2\eta\rceil$ and $\eta$ is the uniform‑continuity modulus at tolerance $\delta$ (Section 4.3, Claim 8).

7. **Indistinguishability theorem.** For every finite experiment $E$, an uncountable continuum model and its computable surrogate assign the same distribution over $R_E$; consequently no experiment detects the cardinality difference, and the Continuum Hypothesis is empirically vacuous for physics (Section 4.3, Claims 7 and 9).

8. **Zero‑bit contribution of breadth.** Non‑computable reals contribute exactly $0$ bits to any physical record, because record entry requires finite naming and finite strings name only computable reals (Section 4.2, Claim 6).

## 6. Discussion

The result is a statement about empirical equivalence, not about mathematical truth. Cantor’s theorem stands; $\mathbb{R}$ is uncountable; nothing here disputes set theory. The claim is that the *difference* between the countable computable fragment and the full uncountable continuum is not the kind of difference any experiment can register, because experiments register finite records and finite records cannot encode cardinality. This formalizes the depth/breadth distinction of [9] and the “physically vacuous” designation of [10].

**Failure modes and what would falsify the claim.** The central result would be falsified by a single concrete counterexample: a physically specifiable experiment $E$ and two models $T$, $T_c$—one over $\mathbb{R}$, one over $\mathbb{R}_c$—that assign *different* distributions over $E$’s finite record set, where both models satisfy the ordinary standards of physical theory (finite specification, computable derivation of predictions). If such a pair existed, the derivation of Claim 7 would have a gap, most likely in assumption (a) of Section 4.4: the counterexample would involve a prediction defined over non‑computable reals yet comparable to data. A second falsification path is operational: a measurement protocol whose outcome is provably a non‑computable real (a “physical oracle” for the halting problem). Within this paper’s grounding, no such protocol is established, and the burden of proof lies with any proposal, since by Claim 6 the record itself can only contain a finite string. A third falsification path targets Claim 8: a physically realized observable that is discontinuous on the region of interest in a way that no finite grid reproduces to tolerance would break the continuous‑observable argument, though the record‑level argument of Claim 7 would still apply.

**Limitations list.** The result rests on the following assumptions, with sensitivity noted for each:

- *Computable derivation of predictions (assumption a).* Total sensitivity; if any accepted physical theory derives data‑comparable predictions via a non‑computable step, the theorem does not cover that theory.
- *Finite records (assumption b).* High sensitivity in idealized settings; in practice every acquisition chain has finite bandwidth, duration, and resolution.
- *Theory comparison at the level of record distributions (assumption c).* Limits the interpretive reach; ontological differences are not addressed.
- *Continuity of observables (assumption d).* Moderate sensitivity; discontinuous idealizations are not covered by Claim 8, though Claim 7 remains valid.
- *Computable coefficients.* If a theory’s parameters are non‑computable reals required empirically, the surrogate construction fails; however such a parameter could never be fixed by data better than a computable approximation, so the surrogate can absorb it.
- *Standard Lebesgue measure.* The probability‑zero statement of Claim 3 assumes the standard Lebesgue measure; alternative measures could assign non‑zero weight to countable sets, but such measures are not used in physical statistics.
- *Bibliographic limitation.* The supplied bibliography contains no dedicated work on computable analysis beyond the QNFO notes [9]–[12] and the uncountability‑computability paper [6]; the mathematical background of Section 4.1 is developed here from definitions rather than cited from a dedicated source.

**Open questions.** Whether the $p$‑adic “valuation” axis of [10] can be given the same computable treatment; whether constructive (intuitionistic) rather than classical computable reals give a cleaner surrogate; whether the indistinguishability theorem extends to theories with non‑computable *sets* of states (e.g., arbitrary subsets of Hilbert space appearing in axioms) — the theorem covers point‑values and record distributions, not arbitrary set‑theoretic structure in the model’s ontology; and whether chaotic systems with sensitive dependence on initial conditions admit a sharper operational version of the bound of Claim 5.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The primary users are foundational physicists and philosophers of physics deciding which number system to take as primitive when axiomatizing a theory; for them, the result removes the empirical obligation to defend uncountable continua and licenses computable‑real formulations as fully adequate. A second user group is the simulation‑science and numerical‑analysis community, whose codes already operate over finite and computable objects; the result states that this restriction is not an approximation forced by hardware but an empirically exact restriction, which changes how the fidelity of simulation to theory is argued—no “uncountable remainder” is lost. A third group is the physics‑education community: since computation is a primary working medium of modern physics training [7] and uptake of new material depends on alignment with perceived faculty needs [4], a result establishing that computable reals lose nothing gives curriculum designers a defensible basis for teaching computable analysis as the primary continuum, with classical analysis as the extension. Beyond these groups the work is foundational: it does not by itself change any instrument design or experimental program.

**(b) Readiness.** This is purely analytical work that has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept formulated). Analytical work never exceeds TRL 3, and nothing here approaches it: no prototype, no simulation study, no experimental program exists yet for this claim.

**(c) The smallest next test.** The smallest calculation that would de‑risk or falsify the central claim is a proven‑exact benchmark: take a standard continuum system with a known closed‑form observable—e.g., the damped harmonic oscillator with computable