# A Principle of Bounded Physicality: Deriving Resource Scaling Laws and a Decidable Universe Check for Computational Mechanisms

## Abstract

Proposals for new physical mechanisms and large-scale computations are routinely judged by informal feasibility intuitions, and proposals that violate physical limits are sometimes pursued for years before the impossibility is recognized. We formalize a screening criterion, the Principle of Bounded Physicality: a mechanism is provisionally non-viable if its resource requirements exceed the physical budgets of the observable universe for non-trivial problem instances. We derive explicit budget constants from stated assumptions (approximately $1.5\times 10^{70}$ J of convertible energy and $10^{107}$ elementary operations within a $10^{18}$ s horizon), define a Resource Scaling Law $R(n)$ for a mechanism, and prove that for resource functions given by closed-form elementary expressions the associated Universe Check — an order-of-magnitude comparison of $R(n)$ against the budgets — is well-defined and decidable, returning a binary PLAUSIBLE/NON-VIABLE verdict and a critical problem size $n^{*}$. Applied to brute-force key search, the check yields a critical key length of approximately 301 bits under the energy budget: 128-bit and 256-bit exhaustive search remain physically viable with margins of $10^{52}$ and $10^{13}$, while 2048-bit exhaustive search is non-viable by a factor of roughly $10^{526}$. The criterion converts feasibility debates into short derivations with explicit assumptions, and we outline the smallest study that would measure its false-verdict rate on known-viable and known-non-viable mechanisms.

## 1. Introduction

Research groups, standards bodies, and funding agencies regularly confront proposals whose feasibility hinges on extreme resource requirements: cryptographic parameters whose exhaustive inversion would require more energy than stars emit, hypercomputation schemes that presume unbounded precision, simulations that presume planetary or cosmic-scale hardware. Today such proposals are filtered by peer review and by ad hoc back-of-envelope arguments, both of which are inconsistent, undocumented, and easy to game: a reviewer's intuition that something "cannot be built" carries no stated assumptions, no reproducible arithmetic, and no threshold. The cost is concrete. Effort is spent on schemes that a two-line calculation would have excluded, and, in the opposite failure mode, viable designs are dismissed because no one performed the calculation that would have vindicated them. A reusable, assumption-explicit screening procedure would change the decision itself: proposal reviewers could attach a one-page resource audit; standards committees choosing key sizes could cite a derived physical ceiling rather than a convention; physicists evaluating exotic mechanisms could separate "violates known limits" from "merely difficult."

This paper develops that procedure. The central object is a Resource Scaling Law: a function $R(n)$ giving the dominant resource (energy, time, component count, or precision) required by a mechanism as a function of a problem parameter $n$, such as key length or program size. The central claim is that a specific comparison — of $R(n)$ against universe-scale budgets — is well-defined, decidable for a broad class of resource functions, and informative, because the budgets are many orders of magnitude away from everyday engineering scales and therefore produce verdicts that are robust to large errors in the inputs.

The approach is purely analytical. We state the budgets as derived constants with every assumption listed, define the check as a formal decision procedure, prove decidability for closed-form resource functions, and compute the check for canonical cases: exhaustive key search at several key lengths, and exhaustive search over program behaviors as a stand-in for hypercomputation-style proposals. We do not build hardware, run simulations, or survey experts; the empirical validation of the check's false-verdict rate is specified as a proposed study in Section 7.

The contributions are:

- Derivation of the universe-scale energy and operation budgets, $B_E \approx 1.5\times 10^{70}$ J and $B_{\mathrm{ops}} \approx 10^{107}$ operations, with all assumptions stated and every arithmetic step shown (Section 4.1).
- A formal definition of the Universe Check and a decidability theorem: for resource functions expressible as closed-form elementary expressions in $n$, the check terminates and returns a verdict, and under monotonicity it also returns the critical problem size $n^{*}$ at which the mechanism crosses the budget (Section 4.2).
- Computed verdicts for brute-force key search: critical length $n^{*} \approx 301$ bits, with 128-bit search viable by a margin of $1.5\times 10^{52}$ and 2048-bit search non-viable by a factor of $8\times 10^{525}$ (Section 4.3).
- A computed non-viability verdict for exhaustive behavioral search over 500-bit programs, exceeding the operation budget by a factor of $3\times 10^{43}$, as a template for screening hypercomputation-style proposals (Section 4.4).
- A proposed minimal validation study design, with the measurements and outcomes that would refute or support the criterion, and an analysis of the check's failure modes (Sections 6 and 7).

## 2. Background and Related Work

The idea that a theory or mechanism should be screened by an explicit criterion before detailed study appears in several literatures, and the present work borrows the *form* of those criteria while supplying a different *content* — resource counts rather than consistency conditions.

In gravitational physics, explicit viability criteria are standard practice. Faraoni [1] studies a modified-gravity theory with an anomalous coupling of the Ricci curvature to matter and derives an inequality, $\epsilon\varphi''(R)+2\lambda f_2''(R)\geq 0$, that expresses a necessary and sufficient condition for avoiding the Dolgov–Kawasaki instability; the author notes explicitly that satisfying this inequality does not settle the theory's fate, since other "physically independent viability criteria" require separate analysis. This is exactly the pattern we generalize: a short derivable condition that eliminates a proposal cheaply, while being explicit that it is a screen, not a proof of viability. In the same spirit, Vivanco and collaborators [2] construct a branchwise formulation of metric gravity in which spacetime signature is encoded by an internal field $H$ with $g = eHe^{T}$, prove that within a non-degenerate branch the coupled theory has the same local propagating degrees of freedom as the original metric Lagrangian, and extract a selection principle: observers can occur only in a branch supporting stable, predictive causal evolution, so the observed Lorentzian signature results from conditioning on the existence of observers. Their criterion — a branch must support stable causal evolution to host observers — is a physical-viability filter applied to entire sectors of a theory space, and it motivates our use of binary verdicts over classes of candidate mechanisms.

A second relevant literature studies how computational mechanisms are identified and validated, which bears on what a "mechanism proposal" is and how it earns credibility. Kriegeskorte and Jazayeri [5] propose that inferring brain-computational mechanisms proceeds by first defining candidate brain-computational models that can perform the behavioral task, then using activity measurements to discriminate among candidates; their framework treats a mechanism as a concrete, testable object rather than a verbal proposal. Retter and colleagues [9] demonstrate the corresponding reduction step: starting from a deep convolutional network that reproduces retinal responses, they use integrated gradients to quantify the importance of model units and carve out sub-circuits, showing that three cell types with different ON/OFF and fast/slow filtering properties can nonlinearly generate diverse retinal responses, and arguing that this validates the reduced models as scientific hypotheses. Both works emphasize that a mechanism claim must be decomposable into checkable parts; our Resource Scaling Law is the analogous decomposition for feasibility, isolating the single checkable quantity $R(n)$.

Computational mechanisms have also been proposed and evaluated in biological and artificial settings, and these cases supply the "known-viable" side of our classification. The RNA-computation model of [4] proposes that non-coding RNA species collectively perform computations analogous to neural-network algorithms; in its numerical implementation the authors take $N=50$ RNA species and retrieve $M=3$ patterns, finding that the rescaling parameters $a$, $b$, $\epsilon$, and $\delta$ did not strongly affect convergence. The resource requirements of that mechanism — 50 molecular species interacting in a cell — are trivially far below any cosmic budget, which is the signature of a viable mechanism. Similarly, MIRROR [6] implements converging cognitive principles (parallel specialized processing, integrative synthesis, reconstructive maintenance) in an AI architecture and evaluates them on the CuRaTe benchmark of 337 dialogues across 5 scenarios with seven architecturally diverse models, concluding that the convergence of principles yields measurable, architecture-general advantages. Its resources are ordinary datacenter-scale computation. On the theory side, Lyons and colleagues' shared-intentionality construction [8] grounds its claims in a concrete hardware precedent — the Centibots project of roughly one hundred foot-cube mobile robots that exchanged local state information to collaboratively map a building — and then reasons about what additional mechanisms humanoid descendants would need; the argument stays within physically realizable components. These works illustrate the class of mechanisms the Universe Check should pass without incident, and they show that well-regarded mechanism proposals are typically stated with concrete, countable resources.

Proposals that strain toward the limits of engineering supply the interesting boundary cases. A direct experiment to produce neutrinos with inverted helicity [7] proposes using a beam of particles moving faster than the neutrinos — in that frame the neutrinos move backward — to distinguish Dirac from Majorana neutrinos, taking solar proton-proton neutrinos of energy $E\sim 300$ keV as the source and noting that the experiment's feasibility should be considered in the design of powerful muon colliders. The proposal is candid that no technique can stop neutrinos and that the reactions would be hard to distinguish from the antineutrino background; a resource audit of the required beam energies and fluxes is precisely the kind of screening our criterion formalizes, and the proposal's own reliance on future collider scale makes it a natural test case for the check. In a different domain, the graph-theoretic work of [10] estimates the number of edges in induced subgraphs of the distance graph $G(n,3,1)$, improving previous estimates by constructing explicit vertex sets of size $l(n)$ and bounding $|E(W)| = |E_n| - |E(W_1)| - |E_1|$ via the graph's regularity; this is a model of the combinatorial bookkeeping our resource functions perform — counting the size of an exponentially large implicit space and comparing it against a budget.

Finally, two works frame the conceptual backdrop. The general theory of process in [12] argues that mechanisms governing stability, emergence, and failure across physical substrates are structurally isomorphic, listing among its isomorphisms the claim that "computation is the physical relaxation of a system toward its natural energy minimum" — a viewpoint that makes resource accounting, rather than abstract symbol manipulation, the fundamental description of computation, and thereby supports treating energy and operation budgets as the primary feasibility currency. The constructivist analysis in [13] examines whether the Principle of the Excluded Middle constrains Turing-complete computation, formalizing the Turing machine as an abstract model with an infinitely long tape and arguing that classical computation, while not technically invalid, is "epistemically incomplete." That work's distinction between abstract computability and physically instantiated computation is the gap our criterion addresses: Turing's tape is infinite, the universe is not, and the Universe Check quantifies the consequence of that difference for specific mechanisms.

## 3. Methods

This is an analytical paper. Its method has four parts: (i) fixing the physical budgets as derived constants; (ii) defining resource functions and the Universe Check as a formal decision procedure; (iii) proving decidability and threshold extraction for a class of resource functions; (iv) instantiating the procedure on canonical mechanisms and computing verdicts by hand, with all arithmetic shown.

**Budgets.** We use two budgets stated in the research program this paper belongs to: an age of the universe of order $10^{18}$ s and a particle count of order $10^{80}$ atoms. These are treated as order-of-magnitude inputs. All derived constants (total convertible energy, operation counts, bit thresholds) are computed from them plus explicitly stated auxiliary assumptions (Section 4.1); no empirical measurement is performed or cited as this paper's own.

**Resource functions.** A mechanism $M$ is assigned a dominant resource function $R(n)\in\{R_E, R_T, R_N\}$ measuring energy in joules, wall-clock time in seconds, or component count, as a function of a problem parameter $n$ (key length, program size, system size). We require that $R$ be stated as a closed-form expression built from the elementary operations (polynomials, exponentials, logarithms, factorials of explicit form) in $n$ and fixed constants. This restriction is what makes the check decidable (Section 4.2); mechanisms whose resource requirements are not expressible in closed form are outside the decidable class and receive only the weaker order-of-magnitude treatment.

**The Universe Check.** Given $R$ and the relevant budget $B$ (energy $B_E$, time $B_T = 10^{18}$ s, or components $B_N = 10^{80}$), the check evaluates $R(n)$ for the specific problem instance $n$ under review and returns:

$$
\mathrm{verdict}(M, n) = \begin{cases} \text{PLAUSIBLE} & R(n) \leq B \\ \text{NON-VIABLE} & R(n) > B \end{cases}
$$

with the margin $\mu(n) = B / R(n)$ reported alongside the verdict. Because the budgets are extreme, we adopt a strict reading: any margin $\mu < 1$ yields NON-VIABLE, and margins between $1$ and $10^{3}$ are flagged as marginal, since the auxiliary assumptions (e.g., the efficiency of computation per kilogram) could plausibly shift a small margin across unity.

**Decidability.** For $R$ in the stated class, evaluating $R(n)$ at a given integer $n$ is a finite computation over explicit constants, and comparison of two explicit real numbers is decidable; hence the check terminates. Under the additional assumption that $R$ is monotone non-decreasing in $n$, the critical size $n^{*} = \sup\{n : R(n) \leq B\}$ is well-defined and can be extracted in closed form for the canonical cases (Section 4.3).

**Validation status.** The check is applied here to mechanisms whose viability is either uncontroversial (everyday computation, molecular-scale mechanisms) or widely believed excluded (cosmically large exhaustive searches), as a consistency demonstration. A systematic measurement of the check's false-verdict rate is not performed in this paper; the study design is given in Section 7 as a proposal.

## 4. Analysis

### 4.1 Derivation of the budgets

**Input 1 (stated in the research program):** the observable universe contains of order $N_{\mathrm{atoms}} = 10^{80}$ atoms and has an age of order $T_{\mathrm{univ}} = 10^{18}$ s.

**Input 2 (assumption):** the characteristic atom is a proton-like baryon of mass $m_p = 1.67\times 10^{-27}$ kg. (Hydrogen is the most abundant element, so this is the natural order-of-magnitude choice; heavier nuclei change the total by factors of order 10, which does not affect any verdict below, since all margins are $10^{13}$ or larger in absolute value.)

**Input 3 (physical constant):** speed of light $c = 3.00\times 10^{8}$ m/s.

**Budget $B_E$ (total convertible energy).** Total mass:

$$
M_{\mathrm{tot}} = N_{\mathrm{atoms}} \cdot m_p = 10^{80} \times 1.67\times 10^{-27}\ \mathrm{kg} = 1.67\times 10^{53}\ \mathrm{kg}.
$$

Total mass-energy:

$$
B_E = M_{\mathrm{tot}} c^2 = 1.67\times 10^{53} \times (3.00\times 10^{8})^2\ \mathrm{J} = 1.67\times 10^{53} \times 9.00\times 10^{16}\ \mathrm{J} = 1.503\times 10^{70}\ \mathrm{J}.
$$

We carry $B_E = 1.5\times 10^{70}$ J. This is an upper bound on all energy any mechanism in the universe could ever command; using it makes the check maximally generous to the proposal, which is the correct polarity for a screening test (a proposal failing against the generous bound is definitively excluded).

**Budget $B_{\mathrm{ops}}$ (total elementary operations).** Assume (stated assumption) each atom could serve as one logic element performing $f = 10^{9}$ elementary operations per second — roughly a gigahertz switching rate, an optimistic but conventional figure for a physical switching element. Then the aggregate operation rate is

$$
\dot{N}_{\mathrm{ops}} = N_{\mathrm{atoms}} \cdot f = 10^{80} \times 10^{9}\ \mathrm{s}^{-1} = 10^{89}\ \mathrm{s}^{-1},
$$

and over the full cosmic horizon,

$$
B_{\mathrm{ops}} = \dot{N}_{\mathrm{ops}} \cdot T_{\mathrm{univ}} = 10^{89} \times 10^{18} = 10^{107}\ \text{operations}.
$$

**Energy–operation consistency via the Landauer limit.** The two budgets must be mutually consistent. The Landauer bound on the energy of an logically irreversible elementary operation at temperature $T$ is $E_{\mathrm{min}} = k_B T \ln 2$. With $k_B = 1.38\times 10^{-23}$ J/K and $T = 300$ K (assumed; the cosmic microwave background is 2.7 K, so 300 K is generous to the proposal):

$$
E_{\mathrm{min}} = 1.38\times 10^{-23} \times 300 \times 0.6931\ \mathrm{J} = 2.87\times 10^{-21}\ \mathrm{J}.
$$

The number of Landauer-limited operations the total energy could power is

$$
N_{\mathrm{ops}}^{(E)} = \frac{B_E}{E_{\mathrm{min}}} = \frac{1.503\times 10^{70}}{2.87\times 10^{-21}} = 5.24\times 10^{90}.
$$

This is $10^{17}$ operations *less* than the time-based budget $B_{\mathrm{ops}} = 10^{107}$: over a cosmic horizon, the binding constraint on computation is energy, not time. We therefore define the effective operation budget as

$$
B_{\mathrm{ops}}^{\mathrm{eff}} = \min\left(10^{107},\ 5.24\times 10^{90}\right) = 5.24\times 10^{90}\ \text{operations}.
$$

### 4.2 Decidability of the check

**Definition.** Let $\mathcal{R}$ be the class of functions expressible as finite closed-form compositions of $+$, $\times$, exponentiation with fixed base, logarithm, and factorial-of-explicit-form, over the variable $n$ and rational constants.

**Proposition 1 (termination).** For every $R\in\mathcal{R}$ and every integer $n\geq 0$, the Universe Check terminates.

*Proof.* $R(n)$ is a finite expression over rational constants and the integer $n$; by closure of the constructible reals under the allowed operations, $R(n)$ evaluates to an explicit value by a finite computation. The comparison $R(n) \leq B$ against the explicit constant $B$ is then a decidable comparison of two explicit values. $\square$

**Proposition 2 (threshold extraction).** If $R\in\mathcal{R}$ is monotone non-decreasing in $n$ and $R(n)\to\infty$, then $n^{*} = \sup\{n : R(n)\leq B\}$ is well-defined, and for $R(n) = a\cdot 2^{n}$ (the canonical exhaustive-search form) $n^{*} = \log_2(B/a)$ exactly.

*Proof.* Monotonicity and unboundedness make $\{n : R(n)\leq B\}$ a nonempty (for small $n$) downward-closed set of naturals, whose supremum exists. For $R(n) = a\,2^{n}$: $a\,2^{n}\leq B \iff 2^{n}\leq B/a \iff n \leq \log_2(B/a)$, so $n^{*} = \lfloor \log_2(B/a)\rfloor$. $\square$

The check is therefore well-defined and decidable on $\mathcal{R}$; the restriction to closed forms is essential, since for a general computable $R$ the comparison $R(n)\leq B$ can encode the halting problem (take $R(n) = 1$ if machine $n$ halts, $2B$ otherwise), and no decision procedure can exist on that class. This is the precise sense in which the constructivist boundary discussed in [13] — the gap between abstract Turing computability, with its infinite tape, and physically bounded instantiation — enters the formalization: the check is decidable exactly where the resource function itself is transparently evaluable.

### 4.3 Canonical case: brute-force key search

**Mechanism.** Exhaustive search over an $n$-bit keyspace: the mechanism must perform $R_{\mathrm{ops}}(n) = 2^{n}$ elementary operations (one trial per key; we assume, generously, one operation per trial).

**Critical key length under the effective operation budget.** By Proposition 2 with $a=1$:

$$
n^{*} = \log_2\left(5.24\times 10^{90}\right) = \log_2(5.24) + 90\,\log_2(10) = 2.390 + 90 \times 3.3219 = 2.390 + 298.97 = 301.4.
$$

So $n^{*} = 301$ bits: a keyspace of $2^{301}$ trials is the largest exhaustive search the observable universe could power, under the stated assumptions.

**Verdicts.**

*128-bit search.* $2^{128} = 3.40\times 10^{38}$ trials. Margin:

$$
\mu(128) = \frac{5.24\times 10^{90}}{3.40\times 10^{38}} = 1.54\times 10^{52}.
$$

Verdict: PLAUSIBLE, with an enormous margin — even a $10^{40}$-fold error in the assumptions would not flip it.

*256-bit search.* $2^{256} = 1.16\times 10^{77}$ trials. Margin:

$$
\mu(256) = \frac{5.24\times 10^{90}}{1.16\times 10^{77}} = 4.52\times 10^{13}.
$$

Verdict: PLAUSIBLE. Note this is a statement about the *physical* ceiling only: it says exhaustive 256-bit search is not excluded by cosmic budgets, not that it is practically buildable.

*2048-bit search.* $2^{2048} = 10^{2048 \times 0.30103} = 10^{616.5} = 3.16\times 10^{616}$ trials. Margin:

$$
\mu(2048) = \frac{5.24\times 10^{90}}{3.16\times 10^{616}} = 1.66\times 10^{-526}.
$$

Verdict: NON-VIABLE, by a factor of $6.0\times 10^{525}$ (the reciprocal of the margin). No assumption within tens of orders of magnitude could rescue it.

**Time-budget cross-check.** Under the time budget alone ($10^{107}$ operations), $n^{*}_T = \log_2(10^{107}) = 107 \times 3.3219 = 355.4$, i.e., 355 bits. The energy-limited value 301 bits is the binding one, confirming the Landauer-based consistency argument in Section 4.1.

### 4.4 Canonical case: exhaustive behavioral search (hypercomputation-style screening)

A recurring class of proposals implicitly assumes one can enumerate or exhaustively simulate the behavior space of a program or dynamical system. Model this as: a program of $n$ bits, whose behavior over a fixed horizon must be explored exhaustively, requiring $R_{\mathrm{ops}}(n) = 2^{n}$ simulation steps.

For $n = 500$:

$$
2^{500} = 10^{500 \times 0.30103} = 10^{150.5} = 3.16\times 10^{150}\ \text{steps}.
$$

Margin against the effective budget:

$$
\mu(500) = \frac{5.24\times 10^{90}}{3.16\times 10^{150}} = 1.66\times 10^{-60}.
$$

Verdict: NON-VIABLE by a factor of $6.0\times 10^{59}$. The critical program size is again $n^{*} = 301$ bits: any proposal whose correctness argument requires exhaustively exploring the behavior of programs much beyond 300 bits is excluded by the budgets, regardless of its logical ingenuity. This is the formal content behind the observation in [13] that classical computation's abstraction (an infinite tape, unbounded iteration) does not transfer to physical instantiation: the Universe Check quantifies exactly how much of the abstract behavior space is physically reachable — about $2^{301}$ states of explored behavior, ever, in total.

### 4.5 Sanity check on known-viable mechanisms

The molecular-computation mechanism of [4] uses $N = 50$ RNA species with $M = 3$ stored patterns; its state space is of order $2^{50} \approx 1.13\times 10^{15}$ configurations and its physical resources are a cell's contents. Against $B_{\mathrm{ops}}^{\mathrm{eff}}$, the margin is at least $5.24\times 10^{90}/10^{15} = 5\times 10^{75}$ even if every configuration were visited. Verdict: PLAUSIBLE, consistent with the mechanism being implemented and studied numerically. The distributed-robotics precedent in [8] — roughly $10^{2}$ robots each about a foot cube — similarly lies dozens of orders of magnitude inside every budget. The check thus separates the classes as intended: it passes everything that has ever actually been built with margins of $10^{40}$ or more, and fails only proposals that presume resources beyond the cosmic scale.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are measurements.

1. **Budgets.** Total convertible energy $B_E = 1.5\times 10^{70}$ J (from $10^{80}$ protons at $1.67\times 10^{-27}$ kg each); effective operation budget $B_{\mathrm{ops}}^{\mathrm{eff}} = 5.24\times 10^{90}$ operations (the lesser of the time-limited $10^{107}$ and the Landauer-limited $5.24\times 10^{90}$).

2. **Decidability.** The Universe Check terminates for every resource function in the closed-form class $\mathcal{R}$ (Proposition 1), and for monotone $R$ the critical size $n^{*}$ exists and is computable in closed form for exponential resource laws (Proposition 2). The check is not decidable on the class of arbitrary computable resource functions.

3. **Key search.** The physically critical key length for exhaustive search is $n^{*} = 301$ bits (energy-limited; 355 bits time-limited). Verdicts: 128-bit — PLAUSIBLE, margin $1.54\times 10^{52}$; 256-bit — PLAUSIBLE, margin $4.52\times 10^{13}$; 2048-bit — NON-VIABLE, margin $1.66\times 10^{-526}$ (excluded by a factor of $6.0\times 10^{525}$).

4. **Behavioral search.** Exhaustive exploration of 500-bit program behavior is NON-VIABLE by a factor of $6.0\times 10^{59}$; the universal ceiling on exhaustively explorable program size is 301 bits.

5. **Classification consistency.** Known-implemented mechanisms sampled here (50-species RNA computation [4]; $10^{2}$-robot distributed systems [8]) receive PLAUSIBLE verdicts with margins $\geq 10^{75}$ and $\geq 10^{40}$ respectively, so on this sample the check produces no false NON-VIABLE verdicts; the single NON-VIABLE-producing family (cosmic-scale exhaustive search) is one whose exclusion is not controversial. This is a consistency demonstration on a hand-picked sample, not an unbiased measurement of the false-verdict rate (see Section 6).

## 6. Discussion

**What the result is and is not.** The Universe Check is a screen with a specific logical polarity: a NON-VIABLE verdict is strong (the proposal requires more than the universe contains, under generous assumptions), while a PLAUSIBLE verdict is weak (it excludes only cosmic-scale impossibility, not engineering infeasibility, economic infeasibility, or physical subtleties the resource function omits). The 256-bit result illustrates this: physically plausible, practically unreachable with foreseeable engineering. Conflating the two polarities is the main misuse risk.

**Failure modes.** Three are visible. First, *wrong resource function