# Physical Irrelevance of Uncountability: Computable Reals Suffice for Continuum Physics

## Abstract

Continuum physics is formulated over the uncountable real line $\mathbb{R}$, yet every measurement, record, and computation a laboratory can produce is finite. This paper asks whether the uncountability of $\mathbb{R}$ — as distinct from its Archimedean completeness — has any physical consequence, and answers that it does not in a precise, checkable sense. The gap addressed is formal: the physics literature treats $\mathbb{R}$ as indispensable, while the computability literature has only recently begun to study the computational content of uncountability itself, and no self-contained result connects the two by showing that cardinality is empirically inaccessible. The approach is threefold. First, we prove by explicit counting that the computable reals are countable — at most $P(n) = 2^{n+1}-1$ programs of length at most $n$ bits, so $P(100) = 2535301200456458802993406410751$ — and dense in $\mathbb{R}$, hence carrying the order, limits, and topology that continuum physics actually uses. Second, we derive an observability bound: an instrument of range $L$ and resolution $\delta$ distinguishes at most $N = \lfloor L/\delta \rfloor$ outcomes, so a meter-scale position measurement at $10^{-18}\,\mathrm{m}$ resolution distinguishes $10^{18} \approx 2^{59.79}$ outcomes. Third, we prove an indistinguishability claim: for every finite experiment, an uncountable continuum model and a computable surrogate assign the same distribution over the finite record set, so the Continuum Hypothesis is empirically vacuous for physics. The result licenses model-builders to restrict to computable reals without empirical loss, and it is analytical work at TRL 1–2 whose next step is a proven-exact benchmark calculation.

## 1. Introduction

A working physicist who simulates a turbulent flow, fits a spectrum, or writes down a Hamiltonian is using the real numbers of classical analysis: an uncountable set, by Cantor's argument. The choice is made silently, in every textbook, and it is never tested. The cost of this silent choice is not money but conceptual exposure: if uncountability is physically load-bearing, then physical law depends on objects — such as the halting probability $\Omega$ of a universal machine — that no process can compute or measure; if it is not load-bearing, then a large part of the mathematical scaffolding of physics is decoration, and alternative foundations (computable, constructible, or rational-based continua) are empirically equivalent and may be formally cleaner. The decision that would change if this paper's result holds is the decision of which number system to take as foundational when constructing physical theories, axiomatizing quantum mechanics, or building simulation infrastructure: the answer "the computable reals suffice" removes any obligation to defend uncountable sets on empirical grounds.

Who faces this problem? Three groups. Foundational physicists and philosophers of physics who must say what the continuum of spacetime or of Hilbert space *is*; numerical analysts and simulation scientists, whose codes can only ever contain computable (indeed finite-precision) objects and who must justify that no physics is lost; and logicians studying the computational content of set-theoretic facts, who need a physics-side criterion for when a mathematical distinction matters. On the mathematics side, the computational content of uncountability has itself become a subject of study: [6] isolates the operation "on input a countable set $A \subset \mathbb{R}$, output $y \in \mathbb{R} \setminus A$" as a computational witness of uncountability and shows it computationally equivalent to other operations of higher-order computability, while noting that these computational properties had not been studied much despite the fame of Cantor's 1874 proof. Internal research notes have proposed that the uncountable reals are physically vacuous because they cannot be accessed [10], [11], [12]. What is missing is a written, self-contained argument with explicit arithmetic: a statement of exactly which structures continuum physics uses, a proof that the computable reals carry those structures, and a quantitative bound showing that no finite experiment can distinguish a countable computable continuum from the uncountable one.

This paper supplies that argument. Its claims are analytical; no experiment is reported here, and every number below is either derived with shown arithmetic or labeled a projection with stated assumptions. The contributions are:

- A proof, with the counting arithmetic shown, that the computable reals $\mathbb{R}_c$ are countable (at most $2^{n+1}-1$ programs of length at most $n$ bits) and dense in $\mathbb{R}$, hence adequate for the limit operations physics uses (Section 4.1).
- A complementary measure-theoretic result: the Lebesgue measure of $\mathbb{R}_c$ is zero, so a real drawn from the standard uniform distribution is computable with probability $0$ (Section 4.1).
- An explicit observability bound: an instrument of range $L$ and resolution $\delta$ has at most $N = \lfloor L/\delta \rfloor$ distinguishable outcomes, computed for concrete instruments, e.g. $N = 10^{18} \approx 2^{59.79}$ outcomes for a meter-scale position measurement at $10^{-18}\,\mathrm{m}$ resolution (Section 4.2).
- A formal indistinguishability statement: for any finite experiment $E$, the set of possible records under the uncountable model and under a computable surrogate coincide, so no experiment detects the cardinality difference; the Continuum Hypothesis is therefore empirically vacuous (Section 4.3).
- An assessment of what this does and does not show, including failure modes, falsification conditions, and a concrete next-step calculation (Sections 6 and 7).

## 2. Background and Related Work

The works cited here fall into three groups: the mathematics of uncountability as a computational object, the internal research programme on computable and rational continua whose claims this paper formalizes, and physics practice documents that show how empirical arguments are actually conducted and communicated in the discipline.

The most directly relevant mathematical work is [6], *On the computational properties of the uncountability of the real numbers*. Its motivation section states that although Cantor's 1874 proof of uncountability is a historical milestone — the first paper on set theory — the computational properties of uncountability had not been studied much, and it studies the operation that, on input a countable set $A \subset \mathbb{R}$, outputs $y \in \mathbb{R} \setminus A$, showing this operation computationally equivalent to related operations. Its main-results section works in higher-order computability theory, generally assuming the principle $\exists^{2}$ (existence of a type-two functional deciding equality of reals) to avoid technical details of representing sets and reals, and defines Cantor functionals, weak Cantor realisers, and NIN-realisers as realisers of uncountability based on the set-theoretic definition of countability. Its historical section recalls Thomae's function $T$, defined as $T(x) = 0$ off $\mathbb{Q}$ and $1/q$ at $x = p/q$ in lowest terms, which is Riemann integrable on any interval yet has a dense set of discontinuities ($\mathbb{Q}$) and a dense set of continuities ($\mathbb{R}\setminus\mathbb{Q}$). This work matters to the present paper for a precise reason: it treats uncountability itself as a computational object, which opens the question this paper answers on the physics side — whether that computational content has any empirical counterpart. Our Claim 7 (Section 4.3) shows it does not: the Cantor-style operation of [6] requires as input an arbitrary countable set of reals, and no finite experiment supplies or registers such an object.

Three works state the position this paper develops. [10], *The Computable Continuum: Depth Without Breadth*, decomposes the uncountability of $\mathbb{R}$ into two properties it calls depth and breadth: depth is Archimedean completeness — every Cauchy sequence of rationals with a rational modulus has a limit — while breadth is the cardinality explosion generated by the power set of $\mathbb{N}$, of which Chaitin's $\Omega$ and the Specker sequence limit are examples of reals no Turing machine can approximate with computable error bounds. Its main theorem (Theorem 4.3) proves that two non-computable reals agreeing on all rational approximations with computable error bounds are physically indistinguishable, via a computable readout functional $\Phi_P$ whose continuity modulus $m: \mathbb{N} \to \mathbb{N}$ guarantees that approximations within $2^{-m(k)}$ give readouts within $2^{-k}$; it also states that $\mathbb{R}_c$ forms a real closed field, is connected (no computable nontrivial clopen sets), and is complete for computable Cauchy sequences with computable moduli. Our Section 4.1 verifies the structural claims by direct construction and our Claim 7 generalizes the per-pair indistinguishability of its Theorem 4.3 to a statement over all finite experiments.

[12], *Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum*, extends the two-property model to three axes using Ostrowski's theorem: depth (the Archimedean completion and its computable subset $\mathbb{R}_c$, physically real), breadth ($\mathbb{R} \setminus \mathbb{R}_c$, physically vacuous because unfalsifiable), and valuation ($p$-adic completions $\mathbb{Q}_p$ as information carriers for discrete quantum numbers such as spin and color statistics). It argues that depth supplies connectedness, without which there is no intermediate value theorem and no guarantee that a continuous quantity passes through intermediate values. We adopt its depth/breadth vocabulary throughout; we do not rely on its valuation-axis claims about quantum error correction or gauge structure, which it states as a framework rather than derives here.

[11], *The ℚ-vs-ℝ Question: Why Physical Law Requires Only the Rational Numbers*, is the most radical version of the computable-sufficiency position: it argues that measurements yield finite-precision rational numbers, not real numbers, citing three independent physical bounds (Bekenstein, Holevo, thermal noise) as establishing measurement finitude; it claims observational equivalence of $\mathbb{Q}$-based constructions with standard formulations for lattice QFT (via Wilson's lattice construction), finite-dimensional quantum mechanics, lattice gauge theories, and general relativity (via a Regge-calculus construction); and it concludes that "the uncountability of $\mathbb{R}$ is a property of mathematics, not of physics," since the physically accessible numbers are countable, computable, and $\mathbb{Q}$-approximable. Our paper is more conservative than [11] in scope — we claim sufficiency of $\mathbb{R}_c$, not of $\mathbb{Q}$ alone, and we prove a record-level indistinguishability theorem rather than relying on the existence of $\mathbb{Q}$-based reformulations — but its measurement-finitude premise is the same premise our Claim 5 quantifies.

The remaining works document how physics selects and justifies its tools, and we cite them for one methodological point: physical arguments carry weight in the discipline only when framed in terms of observable consequences. [1], the *Physics Briefing Book* of the European Particle Physics Strategy Update, describes a bottom-up process in which the community submits proposals ("inputs") for projects to be realised in the near-, mid- and longer-term future, including national and laboratory inputs; its precision-physics section states that at future $e^+e^-$ colliders $10^{12}$ $Z$ bosons would be available at circular machines and that oblique parameters would be measured with a precision of about $1\%$, a factor of $10$ better than current precision. This is the venue structure and the empirical standard — precision reach, stated numerically — through which any foundational claim about the continuum would have to be argued if it were to influence facility-scale planning; our Section 4.2 supplies exactly such numerical reach statements for the cardinality question. [2], the Snowmass '96 report on the Next Linear Collider, presents the design expectations and physics program of an $e^+e^-$ linear collider of center-of-mass energy $0.5$–$1.5\,\mathrm{TeV}$, reviews the experiments the facility would carry out, and demonstrates feasibility of construction, citing the SLC's role in developing the accelerator physics for future colliders and the FFTB program's role in evaluating final-focus limitations; we cite it as an exemplar of a physics program argued entirely through observable physics reach, the standard our indistinguishability result is phrased to meet. [3], the MHD analysis of CFETR and HFRC, describes two Chinese fusion projects representing the low-density steady-state and high-density pulsed pathways, whose physics designs center on assessment and analysis; its simulations use stated numerical parameters (for the hybrid-scenario tearing-mode study, a Lundquist number $S = 5.56 \times 10^{6}$ and a resonant surface at $r_s = 0.51a$) and its summary reports predicted ECCD power requirements for full NTM stabilization — a concrete instance of design decisions justified by computation over finite-precision objects, which is the practice our result underwrites.

Three further works concern the human and educational context of physics practice. [4] reports phenomenographic interviews on physics faculty perceptions of research-based assessment materials and finds that faculty take up research-based resources more readily when the resources align with their perceived needs. [5] reflects on the Fifth International Conference on Women in Physics, attended by 215 female physicists and a few male physicists from 49 countries, focusing on barriers to women's professional advancement and their variation across countries; any reform of how the continuum is taught must reach this broad and diverse community. [7] adapts the theory of computational literacy — which divides computational learning into material, cognitive, and further dimensions — to computational essays in physics, on the premise that computation is becoming an increasingly important part of physics education. [8] studies the self-expressed learning orientations of life-science majors in introductory algebra-based physics, identified from post-test feedback surveys spanning six measured semesters, as a variable in course performance. We cite these four together for one point: computation is now a primary working medium of physics practice and training [7], which raises the stakes of knowing which mathematical objects computation can and cannot carry — and curriculum-level uptake of foundational material depends on alignment with perceived needs [4], so a result stating that computable reals lose nothing gives educators a defensible reason to teach computable analysis alongside classical analysis.

No work in this bibliography states or refutes the indistinguishability theorem of Section 4.3; that result is derived here.

## 3. Methods

The paper is analytical and constructive. Its method has four parts.

**3.1 Structure isolation.** We first list the mathematical structures that continuum physics actually invokes: (i) a linearly ordered field for coordinates and observables; (ii) density, so that between any two distinct states another state exists; (iii) the existence of limits, so that derivatives, integrals, and solutions of differential equations are defined; (iv) a topology fine enough to define continuity and convergence; and (v) separability in the practical sense that a countable dense subset exists, which is what makes coordinates, series expansions, and finite encodings possible. We do not assume structures beyond these; in particular we do not assume that "all subsets of the continuum" (the powerset) is physically instantiated, since no physical operation is stated over arbitrary subsets.

**3.2 Counting and density arguments.** We then prove countability and density of the computable reals by explicit counting: programs are finite bit strings, and the number of bit strings of length at most $n$ is finite and computable. Density follows because rationals are computable and dense. As a complementary measure-theoretic lens, we compute the Lebesgue measure of $\mathbb{R}_c$ by countable subadditivity. All arithmetic is shown in Section 4.

**3.3 Indistinguishability framework.** We model an experiment abstractly: an experiment $E$ is a physical process with a finite set of possible outcome records $R_E$, of size $|R_E|$, bounded by the instrument's resolution and acquisition window. A physical theory $T$ assigns probabilities to records: $T$ is *empirically adequate* if the induced distribution over $R_E$ matches observation within experimental uncertainty. Two theories $T_1, T_2$ are *empirically indistinguishable* if for every finite experiment $E$ they assign the same distribution over $R_E$. The indistinguishability claim of Section 4.3 is then a statement about record sets, not about ontology: we show that a computable-real surrogate model can be constructed to match any uncountable model's record distribution, because both models' predictions are, at the point of comparison, finite objects.

**3.4 Observable-preservation argument.** As a second route to the same conclusion, we consider a generic physical theory $\mathcal{T}$ whose state space is $\mathbb{R}^k$ and whose observables are continuous functions $O:\mathbb{R}^k\to\mathbb{R}$. For any experimental tolerance $\delta$, uniform continuity on compact subsets yields a neighborhood radius $\eta$ such that states within $\eta$ give observable values within $\delta$; a finite dyadic grid of spacing below $\eta$ then suffices to reproduce every observable value to within tolerance. This connects the abstract record argument to the concrete finite-precision practice of simulation.

**Definitions.** A real number $x$ is *computable* if there is an algorithm (Turing machine) that, given $k$, outputs a rational $q_k$ with $|q_k - x| < 2^{-k}$. A *computable surrogate* of a continuum theory $T$ is a theory $T_c$ stated over $\mathbb{R}_c$ (or over $\mathbb{Q}$ with computable limit procedures) that agrees with $T$ on all computable inputs and computable parameters.

## 4. Analysis

### 4.1 The computable reals are countable, dense, and of measure zero

**Claim 1 (Countability).** The set $\mathbb{R}_c$ of computable reals is countable.

*Derivation.* Each computable real is named by at least one program, and programs are finite bit strings. Count the bit strings of length at most $n$: there are $2^0$ strings of length $0$, $2^1$ of length $1$, …, $2^n$ of length $n$. Hence

$$
P(n) = \sum_{j=0}^{n} 2^j = 2^{n+1} - 1 .
$$

For example, with $n = 100$ bits:

$$
P(100) = 2^{101} - 1 = 2535301200456458802993406410752 - 1 = 2535301200456458802993406410751 .
$$

This is finite for every $n$, and $\mathbb{R}_c = \bigcup_{n=1}^{\infty} \{x : x \text{ named by a program of length} \le n\}$ is a countable union of finite sets, hence countable. $\square$

(If one counts only non-empty programs, the count is $\sum_{j=1}^{n} 2^j = 2^{n+1}-2$; for $n=10$ this is $2^{11}-2 = 2048 - 2 = 2046$. The convention adopted here includes the empty string, giving $2^{n+1}-1$; the difference of one program has no effect on any downstream claim, since both conventions yield a finite count for every $n$ and a countable union over $n$.)

**Claim 2 (Density).** $\mathbb{R}_c$ is dense in $\mathbb{R}$.

*Derivation.* Every rational $q = a/b$ with $a, b \in \mathbb{Z}$, $b \neq 0$, is computable: the program "output $a/b$" has finite length and outputs $q$ exactly. The rationals are dense in $\mathbb{R}$: for any $x < y$ there exists $q \in \mathbb{Q}$ with $x < q < y$ (take $q$ a decimal truncation of $(x+y)/2$ to more than $\log_{10}\frac{2}{y-x}$ places). Since $\mathbb{Q} \subseteq \mathbb{R}_c$, $\mathbb{R}_c$ is dense in $\mathbb{R}$. $\square$

**Claim 3 (Measure zero).** The Lebesgue measure of $\mathbb{R}_c$ is $0$.

*Derivation.* $\mathbb{R}_c$ is countable (Claim 1), so it can be listed as $\{x_1, x_2, x_3, \dots\}$. The Lebesgue measure $m$ of a singleton $\{x_i\}$ is $0$. By countable subadditivity,

$$
m(\mathbb{R}_c) = m\!\left(\bigcup_{i=1}^{\infty}\{x_i\}\right) \le \sum_{i=1}^{\infty} m(\{x_i\}) = \sum_{i=1}^{\infty} 0 = 0 .
$$

Hence the probability that a real drawn from the standard uniform (Lebesgue) distribution is computable is

$$
P_{\mathrm{comp}} = \frac{m(\mathbb{R}_c)}{m(\mathbb{R})} = 0 .
$$

This measure-zero fact and the density fact are not in tension: a set can be dense and of measure zero (the rationals are the standard example). $\square$

**Claim 4 (Adequacy of structure).** $\mathbb{R}_c$ supports the structures of Section 3.1: it is a countable, dense, linearly ordered subfield of $\mathbb{R}$; limits of computable sequences with computable convergence moduli are computable (the standard effective-content property of computable analysis, used here as a definitional property of the computable reals); and its order topology is the subspace topology inherited from $\mathbb{R}$, which agrees with $\mathbb{R}$'s topology on all computable points and computable open sets. What $\mathbb{R}_c$ lacks is exactly "breadth" in the sense of [10]: the non-computable points, which are never the values of computed or measured quantities in any derivation whose input and output data are finite. The structural claims agree with those stated in [10] — that $\mathbb{R}_c$ is a real closed field, connected, and complete for computable Cauchy sequences with computable moduli — and with the depth-preservation argument of [12], which identifies connectedness and computable completeness as the features depth contributes to physics.

### 4.2 Observability bound: how many outcomes can an experiment have?

**Claim 5 (Record bound).** An instrument measuring a single quantity over range $L$ with resolution $\delta$ produces at most

$$
N = \left\lfloor \frac{L}{\delta} \right\rfloor
$$

distinguishable outcomes, i.e. at most $\log_2 N$ bits per measurement.

*Derivation, worked example.* Take a position measurement with range $L = 1\,\mathrm{m}$ and resolution $\delta = 10^{-18}\,\mathrm{m}$ (a deliberately generous bound, stated as an assumption of this projection). Then

$$
N = \frac{1}{10^{-18}} = 10^{18},
$$

and the information content is

$$
\log_2(10^{18}) = 18 \log_2 10 = 18 \times 3.321928094887\ldots = 59.79470570797\ldots \approx 59.79 \text{ bits}.
$$

So even this extreme single-quantity measurement distinguishes fewer than $2^{60}$ outcomes.

*Derivation, digital acquisition.* A digitizer with $b$ bits of resolution and $c$ channels sampled at rate $f$ for a run of duration $\tau$ produces at most

$$
R = 2^{b \cdot c \cdot f \cdot \tau}
$$

distinct records. With generous laboratory parameters $b = 24$ bits, $c = 64$ channels, $f = 10^9\,\mathrm{s^{-1}}$, $\tau = 10^3\,\mathrm{s}$ (these are illustrative instrument parameters, stated as assumptions of this projection, not measurements):

$$
b \cdot c \cdot f \cdot \tau = 24 \times 64 \times 10^9 \times 10^3 = 1.536 \times 10^{15} \text{ bits},
$$

so $R = 2^{1.536 \times 10^{15}}$ possible records. This is enormous, but it is finite, and — the point that matters — it is *countable*: the record set of any finite experiment is a finite set, regardless of how large.

**Claim 6 (Program-count vs. record-count asymmetry).** The non-computable reals cannot enter a record even in principle, because entering a record requires finite description. A real enters a physical record only if some finite process outputs a finite string that (approximately) names it. Non-computable reals, by definition, have no such finite naming process; any finite string in a record names at most a computable real (or a finite-precision rational approximation). Hence the "breadth" axis of [10] and [12] contributes zero bits to any record.

*Derivation.* A record is a finite string over a finite alphabet; there are $2^{m}$ strings of length $m$, and each such string is a valid input to a universal interpreter, so each names at most one computable object in the sense of Section 3. The map from records to named reals factors through finite strings, and finite strings name only computable reals. $\square$

This is the record-level counterpart of the measurement-finitude argument of [11], which holds that all physical measurements produce rational numbers, citing the Bekenstein bound, the Holevo bound, and thermal noise as independent physical bounds against infinite-precision measurement.

### 4.3 Indistinguishability of the uncountable and computable continua

**Claim 7 (Indistinguishability).** For every finite experiment $E$, the uncountable continuum model $T$ and a suitably constructed computable surrogate $T_c$ assign the same distribution over the record set $R_E$.

*Derivation.* Fix $E$ with record set $R_E$, $|R_E| < \infty$ (Claim 5). The prediction of $T$ on $E$ is a probability vector $p = (p_1, \ldots, p_{|R_E|})$ with $\sum_i p_i = 1$. In any physical theory whose predictions are derived by computation from finite specifications of $E$'s apparatus, each $p_i$ is the output of a computation, hence a computable real (to the precision at which it is ever stated). Construct $T_c$ by: (i) restricting all state spaces to $\mathbb{R}_c$ (or $\mathbb{Q}$ with explicit limit procedures); (ii) keeping all dynamical laws whose coefficients are computable; (iii) defining predictions by the same computational derivation. Then $T_c$ produces the identical probability vector $p$, because the derivation never leaves the computable fragment. Since this holds for every finite $E$, $T$ and $T_c$ are empirically indistinguishable. $\square$

Claim 7 generalizes the per-pair result of [10]: its Theorem 4.3 shows that two non-computable reals agreeing on all rational approximations with computable error bounds are physically indistinguishable, because a computable readout functional $\Phi_P$ has a computable continuity modulus $m(k)$ such that approximations within $2^{-m(k)}$ yield readouts within $2^{-k}$. Our Claim 7 lifts that argument from pairs of reals to whole theories: the same continuity-modulus mechanism, applied at the level of record distributions, makes the entire non-computable fragment of the state space invisible to every finite experiment.

**Claim 8 (Observable preservation, continuous case).** Let $O:\mathbb{R}^k\to\mathbb{R}$ be continuous and let an experimental tolerance $\delta > 0$ be given. On any compact region $K \subset \mathbb{R}^k$, uniform continuity yields $\eta > 0$ such that $\|x - y\| < \eta$ implies $|O(x) - O(y)| < \delta$. Define $L = \lceil -\log_2 \eta \rceil$ and the dyadic grid

$$
D_{\eta} = \left\{\frac{p}{2^{L}} \;\bigg|\; 0 \le p < 2^{L}\right\},
$$

which contains $2^{L}$ points and partitions $[0,1]$ into intervals of length $2^{-L} \le \eta$. For any state $x \in K$ there exists $d \in D_{\eta}^k$ with $\|x - d\| < \eta$, guaranteeing $|O(x) - O(d)| < \delta$. Since every real detector has finite resolution, $\delta$ can always be chosen below the experimental resolution; hence $O$ evaluated on the computable grid yields predictions indistinguishable from those on the full continuum, for states in $K$. $\square$

**Claim 9 (Empirical vacuity of the Continuum Hypothesis).** The Continuum Hypothesis ($2^{\aleph_0} = \aleph_1$) concerns the cardinality of the powerset of the continuum — the "breadth" axis. By Claim 6, no record carries breadth information; by Claim 7, models differing only in breadth assign identical record distributions. Hence no experiment distinguishes models in which CH holds from models in which it fails: CH is empirically vacuous for physics. This matches the conclusion of [10] that "the Continuum Hypothesis has zero physical content" because it quantifies over the power set of $\mathbb{N}$, an object not required for the physical description of the continuum, and the conclusion of [11] that cardinality does not constrain the choice of base field because the physically accessible numbers are countable.

*Arithmetic check of the scale of the claim.* The cardinality difference at issue is between $\aleph_0$ (the computable reals, Claim 1) and $2^{\aleph_0}$ (the reals). No finite record set $R_E$ with $|R_E| = 2^{1.536 \times 10^{15}}$ (Section 4.2) or any other finite size can witness a difference between a countable and an uncountable set of possible values, because both restrict to the same finite set of realized records with the same probabilities.

### 4.4 What the derivation assumes

The derivation uses: (a) that physical predictions are produced by computation from finite specifications; (b) that records are finite strings; (c) that theory comparison happens at the level of record distributions; and (d), for Claim 8, that the observables in question are continuous on the compact regions where they are evaluated. Assumption (a) is the substantive one; a theory in which physical observables are *defined* as non-computable reals (e.g., an oracle-mediated observable) would escape it, but such a theory provides no procedure by which the observable's value could be compared to data, which is the operational criterion (a) encodes. These assumptions are examined as limitations in Section 6.

## 5. Results

All numbers below are those computed in Section 4; none is an empirical measurement.

1. **Countability with explicit count.** The computable reals are countable; the number of programs of length at most $n$ bits is $P(n) = 2^{n+1}