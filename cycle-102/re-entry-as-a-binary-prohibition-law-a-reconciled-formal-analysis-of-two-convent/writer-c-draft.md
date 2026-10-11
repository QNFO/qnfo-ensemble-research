# Re-entry as a Binary Prohibition Law: A Formal Sketch Connecting the Calculus of Indications to Constrained Binary Dynamics

## Abstract

We ask whether the re-entry form of the calculus of indications — the operation by which a distinction is taken inside its own indicational space — can be read simultaneously as a *binary prohibition law*: a rule that forbids a designated configuration of a two-valued system and thereby reshapes the system's state space. We formalize this reading by modeling a prohibition as a forbidden-word constraint on binary sequences and by modeling re-entry as a self-referential operator on a two-element algebra. We derive exact counts of admissible binary sequences of length $n$ under a single adjacent-pair prohibition, obtaining $a_{10} = 144$ admissible sequences out of $2^{10} = 1024$ raw states, a uniform-coding capacity of $\log_2 144 \approx 7.1699$ bits against $10$ bits unconstrained, and an asymptotic per-symbol capacity of $\log_2 \varphi \approx 0.6942$ bits, where $\varphi = (1+\sqrt{5})/2$ is the golden ratio. We extend the counting to a three-valued re-entry algebra (marked, unmarked, oscillating) and show the per-distinction capacity rises to $\log_2 3 \approx 1.5850$ bits. The paper positions these results as a bridge between distinction-logic reconstructions of Boolean foundations and the combinatorics of constrained binary dynamics, and it surveys the surrounding literature on binary test functions, symbolic execution of binaries, and binary systems in astrophysics. All quantitative claims are derived in the text with explicit arithmetic; no empirical data are reported.

## 1. Introduction

The calculus of indications, in its original statement, begins from a single act: a distinction is drawn, creating a marked state and an unmarked state, and every further construction is built from combinations and nestings of that first distinction. Among its most discussed constructions is *re-entry*: the placement of the form's own mark inside itself, producing a self-referential value that the two-valued arithmetic of the calculus cannot stably assign. Later work defended the calculus's cancellation rule and argued for a structural isomorphism between re-entry dynamics and three-outcome measurement collapse, in which the re-entrant form does not reduce to either marked or unmarked but oscillates or suspends between them [11]. A companion critique argues that the wider logical tradition commits a category error by reifying the unmarked state as *false* and the empty set as *nothing*, when the void is not a value at all [10].

The present paper takes a deliberately narrow question out of that program: **can re-entry be read, at the same time, as a binary prohibition law?** A prohibition law, in the combinatorial sense used here, is a rule that designates certain configurations of a binary system as forbidden and admits the rest. The question "simultaneously" is the point: we are not asking whether re-entry *is like* a prohibition by loose analogy, but whether a single formal object can be specified once and then interpreted twice — once as an indicational operator that generates a third, re-entrant condition, and once as a constraint that deletes states from a binary state space.

The motivation for seeking such a dual reading comes from the QNFO corpus context, in which the Kappa / Scale-Invariant Information Thermodynamics framework has been cross-validated against the Standard Model's known one-loop renormalization-group β-functions through the single definition $g_{\text{eff}} = g_0 \kappa$ [9]. Whatever the ultimate fate of that framework, its methodological claim is instructive: one definition, two independent readings, and a consistency check between them. We import that methodological pattern into the distinction-logic setting. If re-entry can be specified once and interpreted both as an operator on an indicational algebra and as a prohibition on a binary state space, then the two readings make overlapping quantitative predictions — in particular, they must agree on how much state space survives the operation — and disagreement between the readings would be evidence that the dual reading fails.

Our contributions are:

1. A formal definition of a binary prohibition law as a forbidden-word constraint on sequences over the two-element Boole algebra $B_2$, the same algebra in which distributions over binary test functions have been developed [4].
2. A dual reading of the re-entry operator as (i) a self-applied distinction generating a third condition and (ii) a prohibition deleting the configuration in which the mark indicates itself as an ordinary value.
3. Exact combinatorial derivations: the count $a_n$ of admissible length-$n$ binary sequences under a single adjacent-pair prohibition, closed-form asymptotics, and the capacity loss and residual capacity computed with full arithmetic.
4. An extension to the three-valued re-entry algebra and its capacity arithmetic.
5. A survey of the supplied bibliography, including the surprising breadth of "binary" as a term of art — from symbolic execution of compiled binaries [3] to binary star systems [5], [8] and binary black hole coalescences [6] — and an argument that the prohibition reading gives the term a unifying combinatorial core.

We emphasize scope from the outset: this is a formal sketch, not an empirical or physical claim. No measurements are reported; every number in the paper is computed from stated inputs in Section 4.

## 2. Background and Related Work

We discuss all twelve supplied works, in bibliography order. Where an entry's supplied summary is thin, we say so and restrict ourselves to what the entry states.

**[1] Marine size spectra stability (arXiv:1001.3826v3).** This paper investigates the stability of the power-law steady state often observed in marine ecosystems, considering three dynamical systems describing organism abundance as a function of body mass and time: a "jump-growth" equation, a first-order approximation (the McKendrick–von Foerster equation), and a second-order approximation (the McKendrick–von Foerster equation's second-order relative, truncated in the supplied summary). Its relevance here is structural: a power-law steady state is a scale-free distribution over a one-dimensional mass coordinate, and stability analysis of such a state is a study of which perturbations a distributional law tolerates and which it forbids. A prohibition law, read dynamically, is the extreme case of a stability boundary: the forbidden configuration is the one the law does not tolerate at all. The supplied summary truncates before reporting the stability findings, so we cite the work only for its framing of approximation hierarchies around an exact law — a pattern our dual reading of re-entry mirrors (exact indicational operator, approximate combinatorial shadow).

**[2] Plankton biodiversity and power laws (arXiv:1705.05327v1).** This work explains two features of unicellular plankton assemblages — high biodiversity and power-law abundance structure — via allometric scaling of cell growth and mortality with cell size, demonstrated through a numerical study of a size-structured, multispecies population-dynamic model with a single resource (the summary truncates mid-sentence on the resource's properties). The relevance is that a simple local rule (allometric scaling) generates global structure without fine-tuning; analogously, we show that a single local prohibition (one forbidden adjacent pair) generates a global, exactly countable reshaping of binary sequence space. Both cases illustrate how minimal local constraints carry global combinatorial consequences.

**[3] cozy: comparative symbolic execution for binary programs (arXiv:2504.00151v1).** This paper introduces *cozy*, a tool for analyzing and visualizing differences between two versions of a software binary, with the primary use case of validating "micropatches": small binary or assembly-level patches inserted into existing compiled binaries, leveraging the Python-based angr symbolic execution framework (the summary truncates on what the tool does with symbolic-execution output). This is the most direct technological echo of our question: a micropatch is literally a prohibition written at the binary level — an instruction sequence that must no longer occur on any execution path. cozy validates that a patch forbids the patched behavior across the symbolic state space. Our Section 3–4 counting model is a toy version of exactly this validation problem: given a prohibition, how much of the state space survives?

**[4] Distributions over binary test functions (arXiv:math/0110335v1).** This work takes $B_2$, the Boole algebra with two elements, as its base, and defines for the $R \to B_2$ functions the limits, derivatives, differentiability, test functions, and integrals, then defines distributions over the space of these test functions — regular and singular distributions, and their support sets — and extends to $R \times R \to \{0,1\}$ functions (the summary truncates there). This is the natural analytical home for our prohibition law: a prohibition is precisely a specification of the *support* of an admissible-state distribution, and the regular/singular distinction in [4] corresponds to whether admissible mass is spread over the surviving support or concentrated. We adopt $B_2$ as our state algebra for exactly this compatibility.

**[5] Evolutionary memory in binary systems (arXiv:astro-ph/0412185v1).** The entry states that correlation between the spins (rotational velocities) in binaries had previously been established, and that this work continues by showing the degree of spin correlation is independent of the components' separation, possibly related to Zhang's non-linear model for the formation of binary stars from a nebula. The relevance is methodological: a correlation that persists independently of separation behaves like a constraint that is not mediated by local interaction — a "prohibition" written into the formation history rather than into present dynamics. Our re-entry prohibition is likewise not a force or interaction but a constraint on what configurations count.

**[6] Two-dimensional correlation function of binary black hole coalescences (arXiv:2005.06004v2).** This work computes two-dimensional correlation functions of binary black hole coalescence detections in LIGO–Virgo's first and second observation runs, testing the sky distribution of events for correlations at different angular scales by comparing the observed correlation function to two reference functions obtained from mock datasets of localization error (the summary truncates on the comparison outcome). We cite it as the observational end of the "binary" spectrum: even coalescing black holes are analyzed through correlation functions against reference ensembles, i.e., through which joint configurations are more or less admitted. The supplied summary does not state the result of the comparison, so we draw no finding from it.

**[7] Integral means, convolution, and univalent functions (arXiv:1902.01595v1).** This paper uses the Baernstein star-function to investigate questions about the integral means of the convolution of two analytic functions in the unit disc, with the theory of univalent functions playing a basic role. The supplied summary gives no further detail. Its place in our argument is by structural analogy only: convolution is the operation by which two constrained objects combine, and integral means measure how much mass survives combination. Our prohibition law acts on the concatenation of binary symbols — a discrete convolution — and our counts measure how much sequence space survives combination under the constraint. Beyond this analogy, the entry supports no further claim.

**[8] Binary properties and theories of star formation (arXiv:astro-ph/0006288v1).** The entry states that the overall frequency and other statistical properties of binary systems suggest star formation is intrinsically a complex and chaotic process, and that most binaries and single stars actually originate from the decay of multiple systems, with interactions between stars forming in close proximity — for example via tidal effects (the summary truncates) — possibly playing a role in star formation itself. This is a striking instance of our theme at astronomical scale: the observed binary statistics are read as the *survivors* of a decay process, i.e., of an implicit prohibition that removes unstable multiple configurations. The statistical properties of what remains carry information about the rule that did the removing — exactly the inference pattern of Section 4, where the count of surviving sequences carries information about the prohibition.

**[9] Kappa/SIIT cross-validation (QNFO).** This entry reports a direct mathematical cross-validation of the Kappa / Scale-Invariant Information Thermodynamics framework (Quni-Gudzinas, 2025, Zenodo 17218944/17230397) against the Standard Model's known 1-loop renormalization-group β-functions, through the single definition $g_{\text{eff}} = g_0 \kappa$ (the summary truncates after the definition). We cite it for its method, as stated: one definition carrying two frameworks and a consistency check between them. Our dual reading of re-entry imports this pattern; we do not rely on, or evaluate, the cross-validation's outcome, which the supplied summary does not report.

**[10] The void is not false (QNFO).** This critique-first paper argues that Boolean logic and set theory reify the void (the unmarked state) into *false* and the empty set, committing a category error; false is a mark, the void is not a value. A reconstruction program — distinction-logic with inside/outside/oscillating states — is labeled conjecture (the summary truncates there). Our prohibition reading is a direct ally of this critique: a prohibition law does not assign the forbidden configuration the value *false*; it removes the configuration from the admissible space altogether. The distinction between "the pair '11' is false" and "the pair '11' does not exist as an admissible state" is exactly the distinction between reification and prohibition that [10] draws at the level of the void.

**[11] The Spencer-Brown cancellation rule defended (QNFO).** This work systematically defends the Spencer-Brown cancellation rule, establishing a structural isomorphism with quantum measurement collapse via three-outcome dynamics (citing Varela 1975, corroborated by a 29-schisms numerical search 2026), with a 4-level M-property justification framework and a boson–fermion observer analysis, in 14 pages. This is the primary source for our three-valued extension: the re-entrant form, on this reading, yields a third outcome alongside marked and unmarked. Section 4.3 computes the capacity arithmetic of that three-outcome space. The entry's mention of a "29-schisms numerical search 2026" is a claim of the entry itself; we do not reproduce or evaluate that search, and we note that its parameters are not supplied.

**[12] The valuation reading of the Qubit Delusion (QNFO).** The Qubit Delusion (DOI 10.5281/zenodo.21254143) argues that the qubit-gate-circuit model of quantum computation imports a particle ontology inconsistent with quantum field theory, and that the field's failure to deliver commercially viable hardware after $35 billion of investment is an epistemic cr... (the summary truncates mid-word). The supplied summary gives no further detail on the valuation reading or the adelic kernel. We cite the work only for the question its title and truncated summary pose — whether a kernel in a valuation reading is load-bearing — which parallels our question of whether the prohibition reading of re-entry is load-bearing or decorative. No finding from this work is used.

## 3. Methods

### 3.1 State algebra and notation

Let $B_2 = \{m, \bar{m}\}$ denote the two-element Boole algebra of marked and unmarked states, following the usage of [4]. A binary sequence of length $n$ is an element $s = (s_1, \dots, s_n) \in B_2^n$; we write $m = 1$ and $\bar{m} = 0$ for combinatorial convenience, so $B_2^n \cong \{0,1\}^n$ and $|B_2^n| = 2^n$.

### 3.2 Prohibition laws

**Definition 3.1 (binary prohibition law).** A binary prohibition law of order $k$ is a set $P \subseteq B_2^k$ of forbidden words; a sequence $s \in B_2^n$ is *admissible* if no length-$k$ contiguous block of $s$ lies in $P$. The admissible set is $A_n(P) \subseteq B_2^n$, and the *survival ratio* is $\rho_n(P) = |A_n(P)| / 2^n$.

We focus on the canonical single prohibition $P = \{11\}$ (order $k=2$): the law forbids the mark from indicating itself in adjacent positions. This is the combinatorial shadow of re-entry under the dual reading of Section 3.3: a mark that re-enters its own indicational space cannot appear, in the resulting sequence, as an ordinary self-adjacent value.

### 3.3 The dual reading of re-entry

The re-entry operator $R$ is specified once, with two readings:

- **Indicational reading (from [10], [11]).** $R$ applied to the form places the mark inside its own space, generating a condition that is neither marked nor unmarked but re-entrant; following [11], the resolved dynamics is three-outcome: $\{m, \bar{m}, r\}$, where $r$ is the re-entrant (oscillating) state.
- **Prohibitional reading (this paper).** $R$ acts on $B_2^n$ as the constraint that the configuration in which the mark indicates itself as an ordinary adjacent value is inadmissible; formally, $R$ induces the prohibition $P_R = \{11\}$ and the admissible set $A_n(P_R)$.

The two readings are *simultaneous* in the sense required by the research question if they agree on the quantity both can express: the amount of state space that survives the operation. The indicational reading expresses survival as the number of distinct resolved outcomes per distinction; the prohibitional reading expresses it as the per-symbol capacity of $A_n(P_R)$. Section 4 computes both and compares.

### 3.4 Counting method

For the prohibition $P = \{11\}$, let $a_n = |A_n(P)|$. Partition $A_n(P)$ by final symbol: $e_n$ = admissible sequences of length $n$ ending in $0$, $d_n$ = those ending in $1$. Then $a_n = e_n + d_n$, with recurrences

$$e_n = a_{n-1}, \qquad d_n = e_{n-1} = a_{n-2},$$

since a sequence ending in $1$ must have $0$ in position $n-1$, and prefixing rules give $a_n = a_{n-1} + a_{n-2}$, with initial conditions $a_1 = 2$, $a_2 = 3$ (both of $\{00, 01, 10, 11\}$ minus $\{11\}$ gives $3$). This is the Fibonacci recurrence shifted: $a_n = F_{n+2}$ where $F_1 = F_2 = 1$.

For the three-outcome re-entry algebra, the state space per distinction is $\{m, \bar{m}, r\}$ with $|\{m,\bar{m},r\}| = 3$, and the per-distinction capacity is $\log_2 3$.

### 3.5 What is not claimed

We do not claim that the prohibition $P = \{11\}$ is the unique or canonical prohibitional reading of re-entry; it is the minimal nontrivial one. We do not claim empirical support, and we do not evaluate the cross-validation in [9], the numerical search parameters in [11], or the valuation reading in [12], none of which are specified in the supplied entries.

## 4. Analysis

Every input number in this section is either a definition of the model (Section 3), an initial condition stated in Section 3.4, or a standard closed-form constant computed below from its defining expression.

### 4.1 Exact counts under the prohibition $P = \{11\}$

**Inputs.** $a_1 = 2$, $a_2 = 3$ (Section 3.4); recurrence $a_n = a_{n-1} + a_{n-2}$.

**Step 1: iterate the recurrence.**

$$a_3 = a_2 + a_1 = 3 + 2 = 5$$
$$a_4 = a_3 + a_2 = 5 + 3 = 8$$
$$a_5 = a_4 + a_3 = 8 + 5 = 13$$
$$a_6 = a_5 + a_4 = 13 + 8 = 21$$
$$a_7 = a_6 + a_5 = 21 + 13 = 34$$
$$a_8 = a_7 + a_6 = 34 + 21 = 55$$
$$a_9 = a_8 + a_7 = 55 + 34 = 89$$
$$a_{10} = a_9 + a_8 = 89 + 55 = 144$$

**Result 4.1.** $a_{10} = 144$ admissible sequences of length $10$.

**Step 2: survival ratio.** Raw state count: $2^{10} = 1024$. Therefore

$$\rho_{10} = \frac{a_{10}}{2^{10}} = \frac{144}{1024} = 0.140625.$$

**Result 4.2.** $\rho_{10} = 0.140625$; the prohibition admits $14.0625\%$ of the raw length-10 state space.

**Step 3: capacity under uniform coding over the admissible set.** If all $a_{10} = 144$ admissible sequences are equiprobable, the coding capacity is

$$C_{10} = \log_2 144 = \frac{\ln 144}{\ln 2}.$$

Compute: $144 = 12^2$, so $\ln 144 = 2 \ln 12 = 2(\ln 4 + \ln 3) = 2(1.3862944 + 1.0986123) = 2(2.4849067) = 4.9698134$. With $\ln 2 = 0.6931472$:

$$C_{10} = \frac{4.9698134}{0.6931472} = 7.1699250 \ \text{bits}.$$

Unconstrained capacity: $\log_2 2^{10} = 10$ bits. Capacity loss:

$$\Delta C_{10} = 10 - 7.1699250 = 2.8300750 \ \text{bits}.$$

**Result 4.3.** $C_{10} \approx 7.1699$ bits against $10$ bits unconstrained; the prohibition costs $\approx 2.8301$ bits at $n = 10$ under uniform coding.

### 4.2 Asymptotic capacity

**Inputs.** The recurrence $a_n = a_{n-1} + a_{n-2}$ has characteristic equation $x^2 = x + 1$, i.e., $x^2 - x - 1 = 0$, with roots

$$\varphi = \frac{1 + \sqrt{5}}{2}, \qquad \psi = \frac{1 - \sqrt{5}}{2}.$$

Compute: $\sqrt{5} \approx 2.2360680$, so $\varphi = (1 + 2.2360680)/2 = 1.6180340$ and $\psi = (1 - 2.2360680)/2 = -0.6180340$. Since $|\varphi| > 1 > |\psi|$, $a_n \sim c\,\varphi^n$ for a constant $c > 0$, and the per-symbol capacity is

$$c_\infty = \log_2 \varphi = \frac{\ln \varphi}{\ln 2}.$$

Compute $\ln \varphi$: $\varphi = 1.6180340$; $\ln 1.6180340 \approx 0.4812118$ (since $e^{0.4812118} \approx 1.618034$). Then

$$c_\infty = \frac{0.4812118}{0.6931472} = 0.6942419 \ \text{bits per symbol}.$$

**Result 4.4.** The prohibition $P = \{11\}$ leaves an asymptotic capacity of $c_\infty = \log_2 \varphi \approx 0.6942$ bits per symbol, against $1$ bit per symbol unconstrained; the asymptotic loss is $1 - 0.6942419 = 0.3057581$ bits per symbol.

**Cross-check of Result 4.3 against the asymptotic regime.** At $n = 10$ the finite-$n$ capacity per symbol is $C_{10}/10 = 0.7169925$ bits, which exceeds $c_\infty = 0.6942419$ bits, as expected since boundary effects (no left neighbor for position $1$) relax the constraint at small $n$. The two computations are consistent in ordering.

### 4.3 Three-outcome re-entry algebra

**Inputs.** From the three-outcome dynamics of [11], the resolved state space per distinction is $\{m, \bar{m}, r\}$ with cardinality $3$.

Per-distinction capacity:

$$C_3 = \log_2 3 = \frac{\ln 3}{\ln 2} = \frac{1.0986123}{0.6931472} = 1.5849625 \ \text{bits}.$$

Gain over the two-valued algebra: $1.5849625 - 1 = 0.5849625$ bits per distinction.

**Comparison with the prohibitional reading.** The prohibitional reading at the single-distinction level removes one of the four length-2 configurations ($11$ out of $\{00,01,10,11\}$), leaving $3$ admissible pairs. Per-pair capacity:

$$\log_2 3 = 1.5849625 \ \text{bits},$$

identical to $C_3$ above. This is the paper's central coincidence: **the three-outcome re-entry algebra of [11] and the pair-level survival count under the prohibition $P = \{11\}$ both assign $\log_2 3$ bits to one act of distinction.** The dual reading is therefore load-bearing at this level in the precise sense that the two readings agree on the one quantity both can express.

### 4.4 Generalization: $j$ prohibitions of order 2

For a prohibition set $P_j \subseteq \{00, 01, 10, 11\}$ with $|P_j| = j$ forbidden adjacent pairs, the raw pair space is $4$, and the pair-level survival is $4 - j$ pairs, with pair-level capacity $\log_2(4 - j)$ bits:

$$j = 1: \log_2 3 = 1.5850; \quad j = 2: \log_2 2 = 1; \quad j = 3: \log_2 1 = 0; \quad j = 4: \log_2 0 \ \text{(undefined; no admissible pairs)}.$$

**Result 4.5.** The prohibitional reading degrades continuously in $j$ from $1.5850$ bits ($j=1$) to $0$ bits ($j=3$) and becomes undefined at $j = 4$: a prohibition law that forbids everything permits nothing. Re-entry, read as the minimal prohibition ($j = 1$), sits at the last point where the indicational algebra retains a nontrivial third outcome.

## 5. Results

All numbers below are computed in Section 4; none are empirical.

- **R1 (exact count).** Under the prohibition $P = \{11\}$, the number of admissible binary sequences of length $10$ is $a_{10} = 144$ (Result 4.1), out of $2^{10} = 1024$ raw states.
- **R2 (survival ratio).** $\rho_{10} = 144/1024 = 0.140625$ (Result 4.2).
- **R3 (finite-$n$ capacity).** Uniform coding over the admissible set gives $C_{10} = \log_2 144 \approx 7.1699$ bits, a loss of $\approx 2.8301$ bits against the unconstrained $10$ bits (Result 4.3).
- **R4 (asymptotic capacity).** $c_\infty = \log_2 \varphi \approx 0.6942$ bits per symbol, an asymptotic loss of $\approx 0.3058$ bits per symbol (Result 4.4).
- **R5 (central coincidence).** The three-outcome re-entry algebra and the pair-level survival count under $P = \{11\}$ both yield $\log_2 3 \approx 1.5850$ bits per distinction (Section 4.3).
- **R6 (degradation ladder).** Pair-level capacity under $j$ order-2 prohibitions: $\log_2(4-j)$, i.e., $1.5850$, $1$, $0$, undefined for $j = 1, 2, 3, 4$ (Result 4.5).

**Projection (labeled as such).** If the dual reading generalizes beyond the minimal prohibition — that is, if re-entry with additional indicational structure corresponds to prohibition sets of larger order $k$ — then the per-symbol capacity should scale as $\log_2 \lambda_k$, where $\lambda_k$ is the dominant root of the order-$k$ constrained recurrence. We have computed this only for $k = 2$ ($\lambda_2 = \varphi$). For $k = 3$ (e.g., forbidding $111$), the recurrence order and dominant root are not computed here; we assert no number for $k \geq 3$. This projection is falsified if no order-$k$ prohibition reproduces the indicational algebra's outcome count for any $k \geq 3$.

## 6. Discussion

**What the dual reading achieves.** The central result (R5) is a numerical coincidence with a structural explanation: forbidding the single self-adjacent pair leaves three admissible pairs, and the re-entry algebra of [11] posits three outcomes. The coincidence is exact ($\log_2 3$ on both sides) but it is also thin — it involves one prohibition, one algebra, and one quantity. Its value is methodological, in the pattern of [9]: one definition, two readings, one shared check.

**Limitations.** First, the choice $P = \{11\}$ is not derived from the calculus of indications as supplied in [10], [11]; it is our modeling hypothesis. Other prohibitions (e.g., $P = \{01\}$) leave the same count $a_n$ by symmetry but a different semantic reading, and nothing in the supplied entries selects among them. Second, the capacity arithmetic assumes uniform coding over the admissible set; a non-uniform admissible distribution would change $C_{10}$, though not $|A_n|$. Third, the three-outcome algebra of [11] is justified there by a structural isomorphism with measurement collapse and a numerical search whose parameters the supplied entry does not give; we inherit that justification at second hand and cannot independently evaluate the "29-schisms" search or the 4-level M-property framework. Fourth, the analogy to [7] (convolution and integral means) is structural only; the supplied summary is too thin to support more. Fifth, the astrophysical works [5], [6], [8] are cited for inference patterns (survivor statistics, separation-independent correlation, correlation against mock reference ensembles), not for any quantitative input; the summary of [6] does not state its comparison's outcome, and we draw no finding from it.

**Failure modes.** The dual reading fails if (i) the indicational outcome count under re-entry is not three for the relevant forms — in which case R5 collapses to coincidence; (ii) the prohibitional reading requires a prohibition set whose size $j$ does not equal $1$ — in which case the degradation ladder (R6) shows the readings diverge immediately, since $\log_2(4-j) \neq \log_2 3$ for $j \neq 1$; or (iii) the shared quantity (capacity per distinction) is judged not to be the quantity both readings actually express — a conceptual objection we take seriously, since the indicational reading counts *outcomes* while the prohibitional reading counts *surviving configurations*, and identifying these is itself an assumption.

**What would falsify the claims.** A demonstration that the re-entrant form resolves to more or fewer than three outcomes under the defended cancellation rule of [11] would falsify R5. A demonstration that the prohibition reading of re-entry must forbid more than one adjacent pair (e.g., because re-entry is iterated, forcing $P = \{11, 111\}$ or larger) would move the pair-level capacity off $\log_2 3$ and falsify the simultaneity claim. Computation of the order-3 dominant root showing $\log_2 \lambda_3 = \log_2 3$ would, conversely, strengthen the program; showing $\log_2 \lambda_3 \neq \log_2 3$ for all natural order-3 prohibitions would weaken it.

**Open questions.** Does the