# Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds

## Abstract

Information-theoretic bounds in gravitational physics are conventionally expressed in bits, a unit that presupposes two human choices: the practice of counting states by integers and the selection of logarithm base 2. This paper asks whether the holographic entropy bound can instead be stated entirely in observer-independent quantities. Working in Planck natural units ($c = \hbar = G = k_B = 1$), in which area is measured in Planck areas $\ell_P^2$ and is therefore dimensionless, we take the Bekenstein–Hawking value $S = A/4$ (in nats) as the definition of the entropy of a region's horizon. We show that the bound $D \leq e^{A/4}$ on the Hilbert-space dimension $D$ of a finite region contains no base-dependent constant; that the bit is recoverable only as the derived, base-dependent quantity $S/\ln 2$ with conversion factor $1/\ln 2 = 1.442695$; and that every base-$b$ representation of entropy is a fixed constant multiple of the same invariant, so that no observable at fixed theory content distinguishes the invariant formulation from the conventional one. Worked examples with full arithmetic are given: a horizon patch of assumed area $A = 10^{68}$ in Planck units carries $S = 2.5 \times 10^{67}$ nats, i.e. $3.60674 \times 10^{67}$ bits, and permits $D \leq 10^{1.085736 \times 10^{67}}$. We identify the rounding of $D$ to an integer as the one genuinely open conventional element, quantify its $26.4\%$ relative effect at the minimal area $A = 4$, and derive the reformulation's methodological criteria — explicit falsifiability and pre-specified analysis — from the corrective practice modeled in the QNFO program.

## 1. Introduction

Physics claims universality, yet its units of information are inherited from engineering. The bit — one bit being the entropy of a two-outcome event, $S = \ln 2$ in natural units — exists because human communication systems favor two-state symbols. The choice of base 2 is a convention of human computation, not a feature of nature. The same criticism applies, though more weakly, to the practice of counting: Hilbert-space dimension is an integer, but "which integer" is meaningful only once a tensor-product factorization and a normalization convention have been chosen by an observer.

This question is not merely notational. The same convention-dependence afflicts "information" wherever it appears as a quantity defined relative to a human symbol system: applied language technology defines information relative to a language's own grammatical rules and vocabulary diversity [1]; misinformation research defines informational threats relative to the cognitive layer of users and their preference for narrative-conforming content [4]; and even formally defined information flow in computational systems requires a chosen computational model, a specific message, and a conditional-mutual-information criterion before anything flows [6]. In each case a human-relative choice sits inside the definition of the quantity. The holographic entropy bound offers an unusual opportunity to do better, because its ingredients can be reduced to geometry plus the exponential function.

In the Bekenstein–Hawking framework, the entropy of a black hole horizon is proportional to its area, and the entropy of a finite spacetime region is bounded by a quantity of the form $\exp(A/4\ell_P^2)$. If one adopts Planck natural units, in which $c = \hbar = G = k_B = 1$, the Planck length $\ell_P$ becomes the unit of length, area becomes dimensionless, and the bound can be written as

$$D \leq e^{A/4},$$

where $A$ is the dimensionless area and $D$ is the dimension of the Hilbert space associated with the region. Expressed this way, the bound involves exactly two ingredients: a geometric invariant (area in Planck units) and the exponential function. The base $e$ of the exponential is not chosen but forced by the requirement that entropy be additive under composition of independent systems: if two disjoint regions with areas $A_1$ and $A_2$ have independent Hilbert spaces of dimensions $D_1$ and $D_2$, the composite dimension is $D_{12} = D_1 D_2$, and the entropy $S = \ln D$ defined by the Bekenstein–Hawking relation $S = A/4$ is fixed in nats by geometry. Choosing a different base for its expression introduces the constant factor $1/\ln b$ with no geometric origin.

The conjecture this paper develops, following the prior paper in this program [7], is that the entire content of the holographic bound can be restated using only the dimensionless entropy $S = A/4$, with the bit recovered as a derived, base-dependent quantity $b = S/\ln 2$. The broader program of which this is a part holds that physics is the study of invariant patterns under specified classes of transformations, and that measurement units and the privileged status of the Archimedean real line are anthropocentric conventions to be stripped away [9]; a systematic compilation has already shown that 53 fundamental physics equations across ten disciplines admit clean dimensionless reformulation in Planck units, with no formula resisting the conversion [10]. If the entropy bound joins that list, information-theoretic bounds in gravitational physics are grounded in observer-independent geometry rather than in human conventions of notation and counting. Conversely, if the program fails — if some irreducibly conventional choice remains — the failure itself is informative, because it locates precisely where observer-dependence enters the foundations of entropy bounds.

A methodological caution frames the whole paper. An earlier phase of this research program produced claims — alignments between particle masses and class-number-one $j$-invariants within a 3.5% window across roughly 400 unregistered effective trials — that were subsequently retracted after audit as multiple-comparisons artifacts with no physical mechanism [8]. The corrected practice adopted there, and inherited here, is to pre-specify what is being claimed, to state falsification conditions explicitly, and to report representational results as representational rather than as empirical discoveries. This paper accordingly claims no new physics, only a precise account of which quantities in the entropy bound are base-free, which are derived, and which remain conventional.

Our contributions are:
- A precise statement of the natural-unit formulation of the Bekenstein–Hawking entropy bound, $D \leq e^{A/4}$, with the classification of every entering quantity as base-free, derived, or conventional (Sections 3 and 4.1).
- Explicit derivations with full arithmetic showing which quantities are base-independent and which are not: the conversion constants $1/\ln 2 = 1.442695$, $1/\ln 10 = 0.4342945$, and $\log_2 10 = 3.321928$, and the worked example $A = 10^{68} \Rightarrow S = 2.5 \times 10^{67}$ nats, $b = 3.60674 \times 10^{67}$ bits, $\log_{10} D \leq 1.085736 \times 10^{67}$ (Sections 4.3 and 4.4).
- A structural result that all base-$b$ representations are related by known constants and are therefore empirically equivalent, so the proposal's significance is foundational rather than empirical (Section 4.3).
- An analysis of the integer-rounding problem for the Hilbert-space dimension $D$, quantified at the minimal area $A = 4$ where the relative deficit is $0.26424$, which we argue is the one genuinely non-derivable convention left in the framework (Section 4.5).
- A base-audit criterion for entropy-inequality results, tested against the homogeneous Shannon-inequality methods of [2] and the logarithmic-loss rate regions of [5], with the observation that homogeneous inequalities are invariant under base rescaling while mixed entropy-information quantities require case-by-case audit (Section 4.6).

The paper is organized as follows. Section 2 reviews the related literature. Section 3 sets up the formal framework. Section 4 carries out the explicit derivations, including all arithmetic. Section 5 reports the computed results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 gives practical implications and engineering pathways. Section 8 concludes.

## 2. Background and Related Work

This section reviews the works most relevant to the paper's claim, in bibliography order. The corpus is deliberately heterogeneous; each work is cited for a specific point it makes, and the connection to the present question is stated explicitly.

[1] treats natural language processing as a branch of computer science combining artificial intelligence with linguistics, aiming to analyze a language element such as writing or speech with software and convert it into information, and observes that each language's own grammatical rules and vocabulary diversity make studies in this field complex. The point we take from it is structural: in applied contexts, "information" is defined relative to a symbol system with language-specific conventions. That is precisely the anthropocentric dependence this paper seeks to remove from entropy bounds; [1] shows how deeply the dependence is embedded even in engineering definitions of information.

[2] develops computer-assisted proof methods involving non-classical inequalities for Shannon entropy and applies them to secret sharing schemes, in which a random secret value is transformed into shares distributed among participants so that only qualified groups recover it, and to hat guessing games. Its concrete results include improved lower bounds on information ratios of seven access structures — for example $57/50 = 1.14$ and $17/15 = 1.1\overline{3}$ — obtained by combining linear programming, the copy lemma, and symmetry constraints, and an improved upper bound on the guessing number of the graph $R^{-}$. The relevance to our question is that Shannon entropy in these proofs is handled as an abstract quantity obeying inequalities, independent of any particular logarithm base: the inequalities used are homogeneous, and homogeneous inequalities are invariant under rescaling of the log base. This is exactly the invariance structure we formalize in Section 4.3, and [2] supplies a working instance of it at the level of proof technique.

[3] describes the Gamma Ray Large Area Space Telescope (GLAST) Large Area Telescope (LAT), a pair-production high-energy ($> 20$ MeV) gamma-ray telescope built by an international partnership of astrophysicists and particle physicists for a satellite launch in 2006, together with the collaboration's construction of a balloon flight engineering model as part of the development effort. We cite it as a representative of large-scale empirical astrophysics whose observables are reported in human-defined units; it marks the contrast between the empirical enterprise, which must speak in conventional units, and the foundational question of which units could in principle be eliminated.

[4] analyzes (mis)information operations: the massive diffusion of social media fosters disintermediation, changes how users are informed and how they engage in public debate, and the cognitive layer of users and related social dynamics define the nature and dimension of informational threats, with users tending to interact with information adhering to their preferred narrative. The relevance is a sociological contrast at the opposite extreme from [3]: here "information" is constituted by human cognition itself. Between [1], [4] and the entropy bound lies a spectrum of convention-dependence, and the holographic bound sits at the end where the residual conventions are fewest — which is why it is the right test case for the non-anthropocentric program.

[5] investigates a multi-terminal source coding problem under logarithmic loss fidelity, which does not necessarily lead to an additive distortion measure, motivated by extending the Information Bottleneck method to a multi-source scenario where several encoders cooperatively build rate-limited descriptions to maximize information. Its technical content includes converse proofs for the achievable rate-relevance tuples, establishing characterizations of complexity-relevance regions via auxiliary random variables satisfying Markov conditions. The relevance is twofold. First, logarithmic loss is a fidelity measure under which the relevant quantities are entropies in some base, and the base is a free convention of the analysis — an instance of the arbitrariness we study. Second, the rate quantities $R_1, R_2$ in its converse bounds are not pure entropies but mutual informations mixed with channel structure, so a base rescaling multiplies them uniformly; whether the resulting region is base-covariant is a checkable instance of our audit criterion (Section 4.6).

[6] develops a theoretical framework for defining and identifying flows of information in computational systems, modeling a system as a directed graph with "clocked" nodes that send transmissions along edges at discrete times, and seeking a definition capturing the dynamic flow of information about a specific message. Its discussion reports that the core contribution is a definition of information flow grounded in the computational task and tied to a specific message, based on positivity of a conditional mutual information expression, and that the framework aids neuroscientists in designing experiments, for instance by establishing that at least two different stimuli are needed to obtain any determination about information flow. We use [6] for a specific structural lesson: even a rigorously defined information quantity requires chosen primitives — a model, a message, a factorization — before it is well-defined. Our Section 4.5 identifies the analogous residual choice in the holographic setting as the integer rounding of the Hilbert-space dimension.

[7] is the direct predecessor of this paper within the QNFO program. It states that the bit presupposes two human choices — integer state counting and the selection of logarithm base 2 — and reformulates the holographic bound in Planck natural units as $D \leq e^{A/4}$ with $S = A/4$, reporting the conversion constants $1/\ln 2 = 1.442695$, $1/\ln 10 = 0.4342945$, and $\log_2 10 = 3.321928$, the worked example $A = 10^{68}$ giving $S = 2.5 \times 10^{67}$ nats and $b = 3.60674 \times 10^{67}$ bits, and the conclusion that the bit is demoted to a derived unit so that only $\{A, S, D\}$ are candidate invariants. The present paper goes beyond [7] in three ways: it grounds the empirical-equivalence claim in the concrete behavior of homogeneous entropy inequalities as used in [2]; it adds the base-audit criterion for mixed entropy-information quantities of the kind appearing in [5]; and it connects the rounding problem to the Ostrowski-theoretic thread of the program [9, 10] rather than leaving it as an isolated observation.

[8] documents the corrective methodology of the broader program. It reports that an earlier "Adelic Theory of Everything" phase claimed three alignments between Standard Model particle masses and class-number-one CM $j$-invariants within 3.5% in decimal ratio, produced by blindly fitting decimal PDG masses across roughly 400 unregistered effective trials (17 particle species $\times$ 4 $j$-invariant targets $\times$ 3 comparison methods $\times$ 2 denominator cutoffs), for which the look-elsewhere-corrected expected number of chance hits is about 2.5, and with no mechanism connecting the Standard Model to the number-theoretic objects; it also reports the retraction of an unconstrained grid-search claim of a "$4.8\times$ improvement over random" after a red-team audit found the optimizer had converged to a degenerate solution. The corrected practice it adopts — Compton frequencies rather than decimal masses, cross-ratios rather than single ratios, exactly 15 pre-specified tests, an honestly reported null, and explicit falsifiability — is the methodological standard this paper imports: our claims are representational, pre-specified, and accompanied by falsification conditions (Section 6).

[9] proposes a systematic refactoring of fundamental physics around a single organizing principle: physics is the study of invariant patterns under specified classes of transformations, and stripping away anthropocentric conventions — measurement units and the privileged status of Archimedean real numbers — reveals dimensionless ratios such as the fine-structure constant $\alpha$ and the proton-to-electron mass ratio $m_p/m_e$ as the true invariants, with Planck units ($\hbar = c = G = k_B = 1$) rendering every physical quantity a dimensionless number. It further states Ostrowski's theorem as a physical principle: every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the standard real absolute value or to a $p$-adic one, so that the real numbers are one leaf among an infinite family of completions, and a non-anthropocentric physics would treat all places equally. We use [9] for two specific points: it supplies the invariance-under-transformations definition of "non-anthropocentric" that our base-rescaling group of Section 4.3 instantiates, and its Ostrowski framing explains why the Archimedean choice of real-valued entropy is itself a convention to be made explicit.

[10] compiles and reformulates 53 fundamental physics equations across ten disciplines into dimensionless equivalents in Planck units, proving via the Buckingham Pi theorem that any dimensionally homogeneous law among quantities with Planck-scale counterparts $x_i^{(P)}$ admits an equivalent dimensionless form $\tilde{F}(\tilde{x}_1, \ldots, \tilde{x}_n) = 0$ containing no dimensional constants, and finding that no formula resists reformulation. It also records the place-democracy constraint that a formula containing dimensional constants can be evaluated only at the Archimedean place, since a real number like $\hbar$ has no well-defined meaning in a $p$-adic completion. We use [10] to justify the standing of our natural-unit setting: the conversion $A = A_{\text{phys}}/\ell_P^2$ is an instance of the general dimensionless correspondence, and the finding that all 53 equations convert cleanly supports the expectation that the entropy bound should as well — which Section 4 confirms.

Notably absent from the bibliography are the primary sources for the Bekenstein bound, Bekenstein–Hawking thermodynamics, and the covariant entropy bound. We therefore treat the relation $S = A/4$ as a framework assumption of this paper, stated as such in Section 3, rather than as a cited result; this is a genuine limitation of the available literature, acknowledged in Section 6 rather than hidden.

## 3. Methods

### 3.1 Natural-unit setting

We adopt Planck natural units throughout:

$$c = \hbar = G = k_B = 1.$$

In these units the Planck length $\ell_P$ is the unit of length, the Planck area $\ell_P^2$ is the unit of area, and any physical area $A_{\text{phys}}$ is represented by the dimensionless number

$$A = \frac{A_{\text{phys}}}{\ell_P^2}.$$

This conversion is an instance of the general dimensionless correspondence proved in [10]: because the Planck system $(\hbar, c, G, k_B)$ spans the physical dimensions of mass, length, time, and temperature, every physical quantity has a unique Planck-scale counterpart and the dimensionless ratio is always well-defined. The Boltzmann constant $k_B$, which converts temperature to energy, is set to 1, so entropy is measured in nats: one nat is the entropy of an event with Hilbert-space dimension $e$.

### 3.2 The base-free entropy bound

We assume, as the framework of this paper, the Bekenstein–Hawking relation for the entropy of a horizon of physical area $A_{\text{phys}}$:

$$S_{\text{BH}} = \frac{k_B\, A_{\text{phys}}}{4\,\ell_P^2},$$

which in natural units becomes

$$S_{\text{BH}} = \frac{A}{4}.$$

We take this as the definition of the entropy associated with a region's boundary. The corresponding bound on the Hilbert-space dimension $D$ of the region is obtained by inverting the thermodynamic relation $S = \ln D$, valid for a maximally mixed state on a $D$-dimensional Hilbert space:

$$D \leq e^{S} = e^{A/4}.$$

This is the central object of the paper. Its ingredients are the dimensionless area $A$, the integer 4 (a geometric factor from the assumed Bekenstein–Hawking relation), and the exponential function. The nat is thus distinguished among logarithm bases by the additivity of $S = \ln D$ under composition and by the geometric fixing of $S = A/4$; any other base introduces the constant $1/\ln b$ with no geometric origin.

### 3.3 Recovery of the bit as a derived quantity

The bit is defined by

$$b = \frac{S}{\ln 2} = \frac{A}{4 \ln 2}.$$

The constant $\ln 2 \approx 0.693147$ is a pure mathematical constant, so the bit is well-defined — but its presence in any formula marks exactly where a human convention (binary representation) has been imported. Our method is to carry $S$ (nats) through all derivations and convert to bits only at the output stage, so that every intermediate statement is base-free.

### 3.4 Method of analysis

We proceed in four steps. (a) State each quantity in the conventional formulation. (b) Rewrite it in natural units. (c) Classify it as base-free (expressible via $S = A/4$ alone), derived (expressible only with an explicit base constant such as $\ln 2$ or $\ln 10$), or conventional (requiring a choice not fixed by mathematics or geometry, such as integer rounding of $D$). (d) Compute worked numerical examples with full arithmetic, stating every input number and its source. As an additional check on the classification, we apply a base-audit criterion to entropy-inequality structures from the literature: a quantity or inequality is base-covariant if and only if it is homogeneous of degree 1 in the entropy variables, since a base change acts as $S \mapsto S/\ln b$, a uniform rescaling. We use no simulation and no empirical input beyond the structural assumptions stated above; all numerical inputs are mathematical constants or labeled illustrative choices.

## 4. Analysis

### 4.1 Classification of quantities

| Quantity | Expression | Status |
|---|---|---|
| Area | $A = A_{\text{phys}}/\ell_P^2$ | base-free (geometric) |
| Entropy | $S = A/4$ | base-free (nats) |
| Hilbert dimension bound | $D \leq e^{A/4}$ | base-free |
| Bits | $b = S/\ln 2$ | derived (base 2) |
| Decimal digits | $d = S/\ln 10$ | derived (base 10) |
| Integer dimension | $D \in \mathbb{Z}$ | conventional (rounding) |

The only conventional entry is the last: the bound $D \leq e^{A/4}$ constrains a real number, but physical Hilbert spaces have integer dimension, so the operative bound is

$$D \leq \lfloor e^{A/4} \rfloor,$$

and the floor function is a counting convention imported from human mathematics. We quantify this in Section 4.5.

### 4.2 Input numbers and their sources

The numerical inputs are of three kinds, each stated explicitly:

- Mathematical constants of the standard real functions: $\ln 2 = 0.693147\ldots$ and $\ln 10 = 2.302585\ldots$, from the definition of the natural logarithm. These are not empirical measurements.
- The structural constant $4$, from the assumed relation $S = A/4$ (Section 3.2).
- Illustrative areas chosen for the worked examples, labeled as assumptions: $A = 10^{68}$ (Section 4.4) and $A = 4$ (Section 4.5). No empirical claim is made about any specific physical system.

All arithmetic below is shown step by step.

### 4.3 Derivation 1: conversion constants and the bit as a derived quantity

The horizon entropy in invariant form is $S = A/4$ nats. The bit count is

$$b = \frac{S}{\ln 2} = \frac{A}{4\ln 2}.$$

Compute the conversion constant:

$$\frac{1}{\ln 2} = \frac{1}{0.693147} = 1.442695\ldots$$

Check: $1.442695 \times 0.693147 = 1.000000$ to six decimals. Therefore

$$b = 1.442695 \times \frac{A}{4} = 0.360674\,A,$$

since $1.442695/4 = 0.360674$ (check: $0.360674 \times 4 = 1.442696$, consistent to the displayed precision). So each Planck area unit ($A = 1$) carries $S = 1/4 = 0.25$ nats $= 0.360674$ bits. The factor $0.360674$ is a pure unit conversion, exactly as $1\ \text{meter} = 100\ \text{cm}$; it encodes no physics.

For the three common bases:

$$\frac{1}{\ln 2} = 1.442695, \qquad \frac{1}{\ln e} = 1, \qquad \frac{1}{\ln 10} = \frac{1}{2.302585} = 0.4342945.$$

Check the last: $0.4342945 \times 2.302585 = 1.000000\ldots$ (the standard identity $\log_{10} e = 0.4342945\ldots$). The ratio between representations is

$$\frac{b}{d} = \frac{\ln 10}{\ln 2} = \frac{2.302585}{0.693147} = 3.321928,$$

which is $\log_2 10$ (check: $2^{3.321928} = 10$ by construction of the logarithm). Every member of the family $\{S/\ln b\}$ is a fixed constant multiple of $S$; the family has one degree of freedom, and that degree of freedom is the convention.

**Empirical-equivalence argument.** Any physical prediction of the theory is a statement of the form "the entropy of region $\mathcal{R}$ is at most $A/4$". Suppose an observable $O$ depended on the representation; then $O$ would be a function $f(S/\ln b)$ for some $b$, i.e. a function of $S$ alone with a $b$-dependent rescaling absorbed. Two observers using bases $b_1$ and $b_2$ compute observables related by

$$g_{b_2}(S) = g_{b_1}\!\left(\frac{\ln b_1}{\ln b_2}\, S\right),$$

and $\ln b_1 / \ln b_2$ is a known constant. Hence the representations are empirically equivalent at fixed theory content; the invariant formulation differs from the conventional one only in which representation is taken as primitive. This is the paper's central structural result, and it is a consistency theorem, not an experimental prediction.

**Cross-check against entropy-inequality practice.** The invariance just derived has a concrete instantiation in the literature. The computer-assisted proofs of [2] establish lower bounds on information ratios of secret-sharing access structures — for instance $57/50 = 1.14$ for the structure $\mathcal{A}$ and $17/15 = 1.1\overline{3}$ for $\mathcal{F}$ — by combining linear programming over Shannon-entropy variables with the copy lemma and symmetry constraints. Every such bound is a homogeneous inequality in the entropy variables: each term is an entropy or conditional entropy, so replacing $S$ by $S/\ln b$ multiplies both sides by the same constant $1/\ln b$ and preserves the inequality. The information ratios reported in [2] are themselves ratios of entropies, so the base constants cancel: the number $57/50$ is base-independent. This confirms the empirical-equivalence argument at the level of an existing proof technology: no choice of logarithm base can change which access structures satisfy which ratio bounds.

### 4.4 Derivation 2: worked example, a macroscopic horizon patch

**Input number.** We assume, as a labeled illustrative choice, a horizon patch with dimensionless area

$$A = 10^{68} \quad (\text{assumption: patch area in Planck units}).$$

This magnitude is chosen for illustration only; no empirical claim is made about any specific physical system.

**Step 1: entropy in nats.**

$$S = \frac{A}{4} = \frac{10^{68}}{4} = 2.5 \times 10^{67}\ \text{nats}.$$

**Step 2: bits.** Using $1/\ln 2 = 1.442695$:

$$b = \frac{S}{\ln 2} = 2.5 \times 10^{67} \times 1.442695 = 3.60674 \times 10^{67}\ \text{bits}.$$

Arithmetic check: $2.5 \times 1.442695 = 3.6067375$, so $b = 3.60674 \times 10^{67}$ (5 significant figures).

**Step 3: Hilbert-space dimension bound.**

$$D \leq e^{S} = e^{2.5 \times 10^{67}}.$$

This number is too large to write directly; we express it via its base-10 logarithm. Using $\ln 10 = 2.302585$:

$$\log_{10} D \leq \frac{S}{\ln 10} = \frac{2.5 \times 10^{67}}{2.302585} = 1.085736 \times 10^{67}.$$

Arithmetic check: $2.5 / 2.302585 = 1.085736\ldots$ (check: $1.085736 \times 2.302585 = 2.500000$), so $D \leq 10^{1.085736 \times 10^{67}}$.

**Step 4: consistency relation.** $b = \log_2 10 \times \log_{10} D = 3.321928 \times 1.085736 \times 10^{67} = 3.6067 \times 10^{67}$, agreeing with the direct computation of Step 2.

**Step 5: base-dependence audit.** The statements $S = 2.5 \times 10^{67}$ nats and $D \leq e^{2.5 \times 10^{67}}$ contain no chosen base. The statements $b = 3.60674 \times 10^{67}$ bits and $\log_{10} D \leq 1.08574 \times 10^{67}$ each contain an explicit base constant ($\ln 2$, $\ln 10$). The audit confirms the classification of Section 4.1.

### 4.5 Derivation 3: the integer-rounding deficit

The floor function introduces a loss:

$$\Delta = e^{A/4} - \lfloor e^{A/4} \rfloor \in [0, 1).$$

For small areas this matters proportionally. Take the minimal nontrivial case $A = 4$ (one Planck area times the geometric factor 4):

$$e^{A/4} = e^{1} = 2.71828\ldots,$$

so

$$D \leq \lfloor e \rfloor = 2, \qquad \Delta = 2.71828 - 2 = 0.71828.$$

The relative deficit is

$$\frac{\Delta}{e} = \frac{0.71828}{2.71828} = 0.26424,$$

i.e. the integer