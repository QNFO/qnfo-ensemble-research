# Grounding block - source: rem-8c6e7057-1ab6-45d4-8f24-03140edffda7

## Research idea

Non-anthropocentric natural units for area and information in holographic bounds. The author asks whether 'area' and 'bit' can be defined as universal invariants—free of human-constructed conventions like logarithm base 2 or integer counting—within the holographic/Bekenstein framework: entanglement entropy of a finite spacetime region is bounded by exp(A/4ℓ_P²), anchored empirically in Bekenstein-Hawking black hole thermodynamics. The conjecture: the bound can be restated purely in Planck natural units (c = ℏ = G = k_B = 1) where area is dimensionless and 'information' is replaced by physical entropy (ln of Hilbert-space dimension), eliminating anthropocentric units. This matters because it would ground information-theoretic bounds in observer-independent physics rather than human conventions. A formal analysis could test whether the Bekenstein bound and covariant entropy bound (Bousso) can be formulated using only dimensionless entropy S = A/4, with the 'bit' recovered as a derived, base-dependent quantity (S/ln 2), and whether any observable consequence distinguishes this invariant formulation from conventional ones.

Source: owner notebook notes/v1/2026/07/21/_26202232956.md

## Existing paper under revision (remediation only)

# Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds

## Abstract

Information-theoretic bounds in gravitational physics are conventionally expressed in bits, a unit that presupposes two human choices: the practice of counting states by integers and the selection of logarithm base 2. This paper asks whether the holographic entropy bound can instead be stated entirely in observer-independent quantities. Working in Planck natural units ($c = \hbar = G = k_B = 1$), in which area is measured in Planck areas $\ell_P^2$ and is therefore dimensionless, we take the Bekenstein–Hawking value $S = A/4$ (in nats) as the definition of the entropy of a region's horizon. We show that the bound $D \leq e^{A/4}$ on the Hilbert-space dimension $D$ of a finite region contains no base-dependent constant; that the bit is recoverable only as the derived, base-dependent quantity $S/\ln 2$ with conversion factor $1/\ln 2 = 1.442695$; and that every base-$b$ representation of entropy is a fixed constant multiple of the same invariant, so that no observable at fixed theory content distinguishes the invariant formulation from the conventional one. Worked examples with full arithmetic are given: a horizon patch of assumed area $A = 10^{68}$ in Planck units carries $S = 2.5 \times 10^{67}$ nats, i.e. $3.60674 \times 10^{67}$ bits, and permits $D \leq 10^{1.085736 \times 10^{67}}$. We identify the rounding of $D$ to an integer as the one genuinely open conventional element and discuss limitations, failure modes, and falsification conditions.

## 1. Introduction

Physics claims universality, yet its units of information are inherited from engineering. The bit — one bit being the entropy of a two-outcome event, $S = \ln 2$ in natural units — exists because human communication systems favor two-state symbols. The choice of base 2 is a convention of human computation, not a feature of nature. The same criticism applies, though more weakly, to the practice of counting: Hilbert-space dimension is an integer, but "which integer" is meaningful only once a tensor-product factorization and a normalization convention have been chosen by an observer.

The holographic entropy bound offers an unusual opportunity. In the Bekenstein–Hawking framework, the entropy of a black hole horizon is proportional to its area, and the entropy of a finite spacetime region is bounded by a quantity of the form $\exp(A/4\ell_P^2)$. If one adopts Planck natural units, in which $c = \hbar = G = k_B = 1$, the Planck length $\ell_P$ becomes the unit of length, area becomes dimensionless, and the bound can be written as

$$D \leq e^{A/4},$$

where $A$ is the dimensionless area and $D$ is the dimension of the Hilbert space associated with the region. Expressed this way, the bound involves exactly two ingredients: a geometric invariant (area in Planck units) and the exponential function. The base $e$ of the exponential is not chosen but forced by the requirement that entropy be additive under composition of independent systems: if two disjoint regions with areas $A_1$ and $A_2$ have independent Hilbert spaces of dimensions $D_1$ and $D_2$, the composite dimension is $D_{12} = D_1 D_2$, and the entropy $S = \ln D$ defined by the Bekenstein–Hawking relation $S = A/4$ is fixed in nats by geometry. Choosing a different base for its expression introduces the constant factor $1/\ln b$ with no geometric origin.

The conjecture this paper develops, following a prior companion paper [12], is that the entire content of the holographic bound can be restated using only the dimensionless entropy $S = A/4$, with the bit recovered as a derived, base-dependent quantity $b = S/\ln 2$. If correct, information-theoretic bounds in gravitational physics are grounded in observer-independent geometry rather than in human conventions of notation and counting. Conversely, if the program fails — if some irreducibly conventional choice remains — the failure itself is informative, because it locates precisely where observer-dependence enters the foundations of entropy bounds.

Our contributions are: (i) a precise statement of the natural-unit formulation of the Bekenstein–Hawking entropy bound; (ii) explicit derivations showing which quantities are base-independent and which are not, with worked numerical examples computed in full; (iii) a structural result that all base-$b$ representations are related by known constants and are therefore empirically equivalent, so the proposal's significance is foundational rather than empirical; and (iv) an analysis of the integer-rounding problem for the Hilbert-space dimension $D$, which we argue is the one genuinely non-derivable convention left in the framework.

The paper is organized as follows. Section 2 reviews the supplied literature. Section 3 sets up the formal framework. Section 4 carries out the explicit derivations, including all arithmetic. Section 5 reports the computed results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 concludes.

## 2. Background and Related Work

We review the twelve works supplied in the bibliography, in their given order. Several are only loosely connected to holography; we confine ourselves to what each entry's own summary supports, and we note where a summary is thin or absent.

[1] treats natural language processing as a branch of computer science combining artificial intelligence with linguistics, aimed at analyzing language elements such as writing or speech with software and converting them into information, and notes that each language's own grammatical rules and vocabulary diversity make studies in this field complex. The connection to our topic is analogical only: "information" in applied contexts is defined relative to a symbol system with its own conventions, which is precisely the anthropocentric dependence we seek to remove from entropy bounds. The supplied summary is truncated and gives no further technical detail.

[2] argues that the holographic bound in physics constrains the complexity of life, that the finite storage capability of information in the observable universe requires "protein linguistics" in the evolution of life, and reports finding that the evolution of the genetic code determines the variance of amino acid frequencies and genomic GC content among species, with the linguistic mechanism confirmed by experimental observations (the summary is cut off mid-sentence). This is the closest supplied work to our theme: it takes the holographic bound as a physical constraint on information capacity and applies it outside gravitation. We use it only as evidence that holographic bounds are treated as substrate-independent capacity statements, which motivates asking in what units such a capacity is defined.

[3] develops computer-assisted proof methods involving non-classical inequalities for Shannon entropy and applies them to secret sharing schemes, in which a random secret value is transformed into shares distributed among participants so that only qualified groups recover it, and to hat guessing games. Its relevance is that Shannon entropy there is handled as an abstract quantity obeying inequalities, independent of any particular logarithm base; homogeneous inequalities are invariant under rescaling of the log base, exactly the invariance structure we formalize in Section 4.3.

[4] considers classical communication over a finite-dimensional quantum channel with memory using a separable-state input ensemble and local output measurements, and proposes algorithms for estimating and bounding the information rate of such setups, some based on so-called auxiliary channels, extending prior algorithms. The finite-dimensional quantum channel is the same algebraic setting in which the Hilbert-space dimension $D$ entering our definition of physical entropy lives; the supplied summary gives no further detail on the forms of the bounds.

[5] describes the Gamma Ray Large Area Space Telescope (GLAST) Large Area Telescope (LAT), a pair-production high-energy ($>20$ MeV) gamma-ray telescope built by an international partnership for a satellite launch in 2006, and the collaboration's construction of a balloon flight engineering model. We cite it as an example of large-scale empirical astrophysics whose measurements are reported in human-defined units; the summary supplies no numerical effective area, so we draw no quantitative comparison.

[6] analyzes (mis)information operations: the massive diffusion of social media fosters disintermediation, changes how users are informed and engage in public debate, and the cognitive layer of users and related social dynamics define the nature and dimension of informational threats, with users tending to interact with information adhering to their preferred narrative. Its relevance is a sociological contrast: "information" as threat vector is defined relative to human cognition, the extreme opposite of the observer-independent entropy we define below.

[7] investigates a multi-terminal source coding problem under logarithmic loss fidelity, which does not necessarily lead to an additive distortion measure, motivated by extending the Information Bottleneck method to a multi-source scenario where several encoders cooperatively build rate-limited descriptions to maximize information. Logarithmic loss is a fidelity measure under which the relevant quantities are entropies in some base; the supplied summary does not state which base, which itself illustrates the base-convention arbitrariness we study.

[8] develops a theoretical framework for defining and identifying flows of information in computational systems, modeling a computational system as a directed graph with "clocked" nodes that send transmissions along edges at discrete times, seeking a definition capturing dynamic flow of information about a specific message. The summary is truncated; we use it only as evidence that information-flow definitions are convention-laden even in classical computation.

[9] (QNFO: Ten-Fingered Trap) has an empty supplied summary; it gives no content we can use, and we cite it only to acknowledge the corpus from which this project arises.

[10] (QNFO: The Threshold of, https://papers.qnfo.org/papers/threshold-of-meaning/) likewise has an empty supplied summary; no statement about its content can be made here.

[11] (QNFO: Super-Universe, https://papers.qnfo.org/papers/super-universe/) likewise has an empty supplied summary; no statement about its content can be made here.

[12] (QNFO: Non-Anthropocentric Natural Units: From the Bekenstein Bound to Ostrowski's Theorem, https://papers.qnfo.org/papers/non-anthropocentric-natural-units/) states that it strips away all anthropocentric constructions from the Bekenstein–Hawking entropy bound, treating area as a dimensionless geometric invariant, defining the exponential bound without logarithmic base, and taking the integer Hilbert-space dimension as a universal invariant; it further connects to Ostrowski's theorem, noting that the Archimedean completion is (summary truncated). This is the direct predecessor of the present paper; our contribution is to make the base-independence claim precise, to exhibit the bit as a derived quantity with explicit conversion factor, to prove the empirical-equivalence result of Section 4.3, and to analyze the integer-rounding problem, which [12]'s summary does not address.

Notably absent from the supplied bibliography are the primary sources for the Bekenstein bound, Bekenstein–Hawking thermodynamics, and the covariant entropy bound; since we may cite only the supplied list, our statements about those bounds rest on the project's framing and on [2] and [12], which explicitly invoke the holographic and Bekenstein–Hawking bounds. This is a genuine weakness of the corpus, acknowledged rather than hidden.

## 3. Methods

### 3.1 Natural-unit setting

We adopt Planck natural units throughout:

$$c = \hbar = G = k_B = 1.$$

In these units the Planck length $\ell_P$ is the unit of length, the Planck area $\ell_P^2$ is the unit of area, and any physical area $A_{\text{phys}}$ is represented by the dimensionless number

$$A = \frac{A_{\text{phys}}}{\ell_P^2}.$$

The Boltzmann constant $k_B$, which converts temperature to energy, is set to 1, so entropy is measured in nats: one nat is the entropy of an event with Hilbert-space dimension $e$.

### 3.2 The base-free entropy bound

The Bekenstein–Hawking entropy of a horizon of area $A_{\text{phys}}$ is

$$S_{\text{BH}} = \frac{k_B\, A_{\text{phys}}}{4\,\ell_P^2},$$

which in natural units becomes

$$S_{\text{BH}} = \frac{A}{4}.$$

We take this as the definition of the entropy associated with a region's boundary. The corresponding bound on the Hilbert-space dimension $D$ of the region is obtained by inverting the thermodynamic relation $S = \ln D$ (valid for a maximally mixed state on a $D$-dimensional Hilbert space):

$$D \leq e^{S} = e^{A/4}.$$

This is the central object of the paper. Its ingredients are the dimensionless area $A$, the integer 4 (a geometric factor from the Bekenstein–Hawking relation), and the exponential function. The nat is thus distinguished among logarithm bases by the additivity of $S = \ln D$ under composition and by the geometric fixing of $S = A/4$; any other base introduces the constant $1/\ln b$ with no geometric origin.

### 3.3 Recovery of the bit as a derived quantity

The bit is defined by

$$b = \frac{S}{\ln 2} = \frac{A}{4 \ln 2}.$$

The constant $\ln 2 \approx 0.693147$ is a pure mathematical constant, so the bit is well-defined — but its presence in any formula marks exactly where a human convention (binary representation) has been imported. Our method is to carry $S$ (nats) through all derivations and convert to bits only at the output stage, so that every intermediate statement is base-free.

### 3.4 Method of analysis

We proceed by: (a) stating each quantity in the conventional formulation; (b) rewriting it in natural units; (c) classifying it as base-free (expressible via $S = A/4$ alone), derived (expressible only with an explicit base constant such as $\ln 2$ or $\ln 10$), or conventional (requiring a choice not fixed by mathematics or geometry, such as integer rounding of $D$); and (d) computing worked numerical examples with full arithmetic. We use no simulation and no empirical input beyond the structural assumptions stated above.

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

and the floor function is a counting convention imported from human mathematics. We quantify this in Section 4.4.

### 4.2 Input numbers and their sources

The only numerical inputs are mathematical constants of the standard real functions, not empirical measurements:

- $\ln 2 = 0.693147\ldots$ (definition of the natural logarithm).
- $\ln 10 = 2.302585\ldots$ (definition of the natural logarithm).
- The structural constants $4$ (from the bound $S \leq A/4$) and the illustrative areas chosen for the worked examples.

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

i.e. the integer bound discards about $26.4\%$ of the allowed dimension at $A = 4$. Arithmetic check: $0.71828/2.71828 = 0.264241\ldots$.

For the macroscopic example of Section 4.4, the absolute deficit remains below 1 while $D \sim 10^{1.085736 \times 10^{67}}$, so the relative deficit is astronomically small. The rounding convention is therefore consequential exactly in the regime of Planck-scale areas — the regime where quantum gravity, not information theory, dominates — and inconsequential macroscopically. This locates the anthropocentric residue precisely: it survives only where the theory is least controlled.

### 4.6 Derivation 4: comparison with the conventional formulation

The conventional formulation writes the bound as $S \leq A_{\text{phys}}/(4\ell_P^2)$ with $S$ in bits:

$$S_{\text{bits}} \leq \frac{A_{\text{phys}}}{4 \ell_P^2 \ln 2}.$$

The natural-unit formulation writes $S \leq A/4$ with $S$ in nats. The two differ by the constant factor $\ln 2 \approx 0.693147$ and by the unit of area. Since both $\ln 2$ and $\ell_P$ are fixed once and for all, the two formulations are related by a fixed change of units and make identical predictions for every observable. We state this as a theorem-level claim: **no observable consequence distinguishes the invariant formulation from the conventional one.** The significance of the program is therefore foundational (which quantities are primitive) rather than empirical (which numbers differ).

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; the input areas are labeled illustrative assumptions, not empirical measurements.

**R1 (Base-free core).** The holographic entropy bound admits the formulation

$$D \leq e^{A/4}, \qquad S = \frac{A}{4},$$

containing no logarithm-base constant. The bit appears only in the derived expression $b = S/\ln 2$.

**R2 (Conversion constants).** The bit-to-nat conversion is $1/\ln 2 = 1.442695$; the digit-to-nat conversion is $1/\ln 10 = 0.4342945$; the bit-to-digit ratio is $\log_2 10 = 3.321928$. One Planck area ($A = 1$) corresponds to a maximum entropy of $S = 0.25$ nats $= 0.360674$ bits $= 0.1085736$ decimal digits (computed as $0.25 \times 0.4342945 = 0.1085736$; check: $0.1085736/0.4342945 = 0.250000$).

**R3 (Worked example, labeled illustrative).** For the assumed $A = 10^{68}$: $S = 2.5 \times 10^{67}$ nats; $b = 3.60674 \times 10^{67}$ bits; $D \leq 10^{1.085736 \times 10^{67}}$, i.e. $\log_{10} D \leq 1.085736 \times 10^{67}$. This is a mathematical illustration of the formalism, not a claim about any physical region.

**R4 (Rounding deficit at minimal scale).** At $A = 4$: $e^{A/4} = e = 2.71828\ldots$, so the integer bound is $D \leq 2$, with relative deficit $\Delta/e = 0.26424$ (about $26.4\%$).

**R5 (Invariance and empirical equivalence).** Any homogeneous entropy inequality is invariant under change of entropy base, since base change multiplies all entropy terms by the same constant $1/\ln b$. Consequently, the natural-unit and conventional formulations are related by a fixed change of units ($\ln 2$ and $\ell_P$) and are empirically indistinguishable; no experiment can prefer one over the other. The choice of primitive representation is methodological.

**R6 (Projection, with assumptions).** If a physical region has boundary area $A_{\text{phys}}$, its bit capacity under the bound is projected as $b = 0.360674 \times A_{\text{phys}}/\ell_P^2$, with uncertainty dominated entirely by the unknown physical applicability of the bound in sub-Planckian or non-saturating regimes; the arithmetic conversion itself is exact. No specific $A_{\text{phys}}$ is asserted.

## 6. Discussion

**Limitations.** First, the reformulation is representational. By R5, it makes no new predictions; a skeptic can correctly say that writing $S \leq A/4$ instead of $b \leq A/(4\ln 2)$ changes nothing operational. Our defense is that foundational clarity has value independent of new predictions, but we concede the result is weaker than "area and bit are universal invariants" might suggest: the bit is *not* an invariant under our proposal — it is explicitly demoted to a derived unit — so the paper's real claim is that only $\{A, S, D\}$ are candidate invariants, and the bit is not among them. Second, the illustrative areas inherit their status as assumptions; all Results that depend on them do too. Third, the derivation assumes the Bekenstein–Hawking relation $S = A/4$ as a definition; a reader who regards it as a derived result requiring quantum-gravity input will find our "base-free" claim conditional on that relation. Fourth, the additivity argument for the nat (Section 3.2) shows the nat is *distinguished* among logarithm bases, but it does not show that entropy must be logarithmic at all; that assumption is inherited from the Bekenstein–Hawking framework.

**Failure modes.** The program fails if (i) the constant 4 in $S = A/4$ turns out to encode a convention (e.g., a choice of horizon slicing) rather than geometry — a derivation from first principles is outside this paper's scope and outside the supplied literature; (ii) the Hilbert-space dimension $D$ is not well-defined for a sub-region, because Hilbert-space factorization is itself observer-dependent — in that case the "integer universal invariant" of [12] is not invariant, and our rounding analysis (R4) quantifies the wrong thing; (iii) entropy at Planck scale is not additive, breaking the uniqueness argument for the natural logarithm; or (iv) the microscopic states of a holographic cell are not countable by a finite integer $D$ — e.g., if the relevant Hilbert space is infinite-dimensional — in which case $S = \ln D$ is undefined and the premise collapses.

**What would falsify the claims.** R5 is falsified by exhibiting a well-defined observable whose value depends on the logarithm base used in the bookkeeping while all invariant quantities ($A$, $S$, $D$) are held fixed; we know of no candidate, but the burden is on us to state the condition. R1 is falsified if the bound requires a base-dependent correction term (e.g., logarithmic corrections to $S = A/4$ with coefficients involving $\ln 2$ or $\pi$ from state counting); such corrections would reintroduce base constants into the core formula. The foundational claim — that the nat/area formulation is *preferable* — is not empirically falsifiable at all; it is a methodological thesis, and could only be undermined by showing that some deep structure (e.g., information-theoretic inequalities of the kind studied in [3] and [7]) singles out base 2 intrinsically. The supplied summaries of [3] and [7] do not state any such base preference, so no support for base-2 primacy exists in the cited corpus.

**Arguing against ourselves.** The strongest objection is that "anthropocentric" is a red herring: the natural logarithm is no more observer-independent than base 2; both are human mathematical constructs, and the true invariant is the *pair* $(S, \text{base})$ up to rescaling. Our reply is that invariance here means invariance under the specific group of base rescalings exhibited in Section 4.3, and the nat is the canonical representative of the orbit only because the map $D \mapsto e^{S}$ is the identity-structured choice; we do not claim $e$ is metaphysically privileged, only that fixing one representative and deriving the rest makes the convention explicit. A second objection: the bibliography contains no primary holography sources, so the paper's grounding in Bekenstein–Hawking physics rests on the project framing and on [2] and [12]; this is a genuine weakness of the supplied corpus, acknowledged rather than hidden.

**Open questions.** (1) Is the factor 4 conventional, and can it be derived rather than inserted? (2) Does a sub-region of a holographic system have a well-defined Hilbert-space dimension at all, given that factorization is ambiguous? (3) Can the floor function $\lfloor e^{A/4} \rfloor$ be replaced by a geometrically motivated integer, e.g. via a counting of Planck-cell states, which would remove the last conventional element? (4) Do the non-classical entropy inequalities studied in [3] admit base-free analogues beyond the homogeneous case — i.e., do any of them mix entropy with non-entropy quantities in a way that breaks rescaling invariance? The summaries of [3] and [4] describe inequality and rate bounds for Shannon and channel information, and a systematic base-audit of such results is a natural follow-up. (5) The truncated summary of [12] invokes Ostrowski's theorem concerning Archimedean completion; integrating that number-theoretic thread with the rounding problem of Section 4.5 is left open, since the supplied summary does not state the connection in enough detail to assess it. (6) Whether the finite-storage premise used in [2] — that the observable universe's information capacity is finite — can be stated without any base convention in cosmological settings. (7) Whether quantum channel information rates as bounded in [4] for finite-dimensional memory channels admit the same nat-only restatement; the summary of [4] does not state the form of its bounds, so this is unresolved from the supplied material.

## 7. Conclusion

Within the Bekenstein–Hawking framework, the entropy bound can be written as $D \leq e^{A/4}$ with $A$ a dimensionless area in Planck units and $S = \ln D$ the physical entropy of a finite Hilbert space of integer dimension $D$. In this form the bound contains no logarithm base and no counting convention; the bit is recovered as the derived quantity $S/\ln 2$ with conversion factor $1.442695$, and every other base-dependent representation is a fixed constant multiple of the same invariant. We showed that no observable at fixed theory content distinguishes the invariant formulation from the conventional bit-based one, so the contribution is foundational and methodological: it identifies exactly which quantities in holographic bounds are candidate universal invariants ($A$, $S$, $D$) and which are conventions (the base, hence the bit), and it locates the remaining conventional residue in the integer rounding of $D$, consequential only at Planck-scale areas where the relative deficit reaches $26.4\%$ at $A = 4$. Future work must derive the coefficient $1/4$ internally, resolve the factorization ambiguity of sub-region Hilbert spaces, and integrate the Ostrowski-theoretic thread of [12].

## References

[1] Challenges Encountered in Turkish Natural Language Processing Studies. arXiv:2101.11436v1. https://arxiv.org/abs/2101.11436v1
[2] Holographic bound and protein linguistics. arXiv:0704.1169v1. https://arxiv.org/abs/0704.1169v1
[3] Bounds on Guessing Numbers and Secret Sharing Combining Information Theory Methods. arXiv:2310.09232v2. https://arxiv.org/abs/2310.09232v2
[4] Bounding and Estimating the Classical Information Rate of Quantum Channels with Memory. arXiv:1903.00199v3. https://arxiv.org/abs/1903.00199v3
[5] Gamma ray Large Area Space Telescope (GLAST) Balloon Flight Engineering Model: Overview. arXiv:astro-ph/0209615v2. https://arxiv.org/abs/astro-ph/0209615v2
[6] (Mis)Information Operations: An Integrated Perspective. arXiv:1912.10795v1. https://arxiv.org/abs/1912.10795v1
[7] Collaborative Information Bottleneck. arXiv:1604.01433v4. https://arxiv.org/abs/1604.01433v4
[8] Information Flow in Computational Systems. arXiv:1902.02292v3. https://arxiv.org/abs/1902.02292v3
[9] QNFO: Ten-Fingered Trap
[10] https://papers.qnfo.org/papers/threshold-of-meaning/. QNFO: The Threshold of Meaning.
[11] https://papers.qnfo.org/papers/super-universe/. QNFO: Super-Universe.
[12] https://papers.qnfo.org/papers/non-anthropocentric-natural-units/. QNFO: Non-Anthropocentric Natural Units: From the Bekenstein Bound to Ostrowski's Theorem.

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2101.11436v1 | Challenges Encountered in Turkish Natural Language Processing Studies
arXiv:2310.09232v2 | Bounds on Guessing Numbers and Secret Sharing Combining Information Theory Methods
arXiv:astro-ph/0209615v2 | Gamma ray Large Area Space Telescope (GLAST) Balloon Flight Engineering Model: Overview
arXiv:1912.10795v1 | (Mis)Information Operations: An Integrated Perspective
arXiv:1604.01433v4 | Collaborative Information Bottleneck
arXiv:1902.02292v3 | Information Flow in Computational Systems

## QNFO corpus context (Vectorize)

QNFO: Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds | https://papers.qnfo.org/papers/non-anthropocentric-natural-units-for-area-and-information-in-holographic-entrop
QNFO: Compton Frequency Cross-Ratios on Bruhat-Tits Trees: A Pre-Registered Search for Adelic Structure in the Standard Model Mass Spectrum (Version 2.3) | https://papers.qnfo.org/papers/compton-cross-ratios-v2
QNFO: Invariant Patterns and the Adelic Refactoring of Fundamental Physics | https://papers.qnfo.org/papers/invariant-patterns-adelic-refactoring
QNFO: The Ostrowski Dimensionless Reformulation: A Systematic Compilation of Fundamental Physics Equations in Planck Units | https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2101.11436v1 | Challenges Encountered in Turkish Natural Language Processing Studies
  Natural language processing is a branch of computer science that combines artificial intelligence with linguistics. It aims to analyze a language element such as writing or speaking with software and convert it into information. Considering that each language has its own grammatical rules and vocabulary diversity, the complexity of the studies in this field is somewhat understandable. For instance
  Full text (https://ar5iv.labs.arxiv.org/html/2101.11436v1), excerpts of its own sections:
  § Submission history: From: Yakup Kutlu [ view email ] [v1] Thu, 21 Jan 2021 08:30:33 UTC (302 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Challenges Encountered in Turkish Natural Language Processing Studies, by Kadir Tohma and 1 other authors View PDF view license
  § Current browse context:: cs.CL < prev | next > new | recent | 2021-01 Change to browse by: cs cs.AI
  § DBLP - CS Bibliography: listing | bibtex Kadir Tohma Yakup Kutlu Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[2] arXiv:2310.09232v2 | Bounds on Guessing Numbers and Secret Sharing Combining Information Theory Methods
  This paper is on developing some computer-assisted proof methods involving non-classical inequalities for Shannon entropy. Two areas of the applications of information inequalities are studied: Secret sharing schemes and hat guessing games. In the former a random secret value is transformed into shares distributed among several participants in such a way that only the qualified groups of participa
  Full text (https://arxiv.org/html/2310.09232v2), excerpts of its own sections:
  § 1 INTRODUCTION: The aim of this paper is to show how the techniques of computer-assisted proofs for information inequalities (for the Shannon entropy) can be used in various applications. Each ingredient of our approach has already been known, but we argue that a properly chosen combination of these methods is quite powerful, to the point that we can improve several previously known bounds. [...]
  § 4.2 Results: We improve the lower bounds for seven access structures. Theorem 4.6 . The information ratios of $\mathcal{A}$ , $\mathcal{A}^{*}$ , $\mathcal{F}$ , $\mathcal{F}^{*}$ , $\widehat{\mathcal{F}}$ , $\mathcal{Q}$ and $\mathcal{Q}^{*}$ are $\nicefrac{{57}}{{50}}=1.14$ , $\nicefrac{{52}}{{45}}=1.1\overline{5}$ , $\nicefrac{{17}}{{15}}=1.1\overline{3}$ , $\nicefrac{{8}}{{7}}=1.142\dots$ , $\nicefrac{{23}}{{20}}=1.15$ , $\nicefrac{{17}}{{15}}=1.1\overline{3}$ and $\nicefrac{{8}}{{7}}=1.142\dots$ respectively. In the column 3 of Table 1 we show these lower bounds for the information ratio of each access structure. Proof. For each of the seven access structures we construct a linear program as explained in Proposition 3.2 . In this linear program we use auxiliary random variables with one or two applications of the copy lemma inspired from the applications of the AK lemma in [ 14 ] . We also add the constraints to express for each access structure the symmetry conditions (see Section 3.2 and the appendix). [...]
  § 5.3 Our Results: Combining the techniques of linear programming, the copy lemma and symmetries we improve the upper bound on $R^{-}$ and give an alternative proof of the previously known bound on $R^{L}$ . For both of these graphs, the asymptotic guessing numbers remain unknown. The symmetry group of $R^{-}$ is $\langle\sigma=(18)(2\ 10\ 5\ 9)(3746),\tau=(25)(36)(47)\rangle$ . The symmetry group of $R^{L}$ is $\langle(25)(36)(47),(26)(35)(8\ 10),(24)(57)(89)\rangle$ . See the appendix for the proof that these are the maximal symmetry groups. Note that as in the case of secret sharing, we only need to find subgroups of these automorphism groups to apply our argument, and we do not need the whole group. We prove that those we use are indeed whole groups of automorphisms of these graphs to ensure that there is no obvious way to improve the bounds we get using them. Using these symmetries and the copy lemma we get the following linear programs and upper bounds for $gn(R^{-})$ and therefore, improve the upper bound given in [ 1 ] . Theorem 5.12 . [...]
  § 6 Conclusion: In this paper we studied the application of computer-assisted proofs involving non-Shannon-type inequalities. Though each separate ingredient used in our construction was known earlier, the resulting combination proved to be surprisingly efficient. We improved lower bounds for the information ratio of 8 access structures based on rank-4 8-point not-linearly-representable matroids. We tried to apply the same approach to one more similar access structure (based on the matroid port $\mathcal{V}^{*}$ ), however we failed. We believe this ‘success rate’ (8 bounds improved out of 9 access structures investigated) shows that the used method is quite strong and it might be interesting to extend to the other instances of the problem of secret sharing. We also improved the upper bound for the single smallest undirected graph, the asymptotic guessing number of which is unknown, namely $R^{-}$ . Not only our bound improves upon the previous one, but also the fraction is simpler (i.e. the denominator is smaller). [...]
[3] arXiv:astro-ph/0209615v2 | Gamma ray Large Area Space Telescope (GLAST) Balloon Flight Engineering Model: Overview
  The Gamma Ray Large Area Space Telescope (GLAST) Large Area Telescope (LAT) is a pair-production high-energy (&gt;20 MeV) gamma-ray telescope being built by an international partnership of astrophysicists and particle physicists for a satellite launch in 2006, designed to study a wide variety of high-energy astrophysical phenomena. As part of the development effort, the collaboration has built a B
  Full text (https://ar5iv.labs.arxiv.org/html/astro-ph/0209615v2), excerpts of its own sections:
  § Submission history: From: David J. Thompson [ view email ] [v1] Mon, 30 Sep 2002 12:51:23 UTC (300 KB) [v2] Fri, 4 Oct 2002 12:29:26 UTC (300 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Gamma ray Large Area Space Telescope (GLAST) Balloon Flight Engineering Model: Overview, by D. J. Thompson and 8 other authors View PDF view license
  § Current browse context:: astro-ph < prev | next > new | recent | 2002-09
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[4] arXiv:1912.10795v1 | (Mis)Information Operations: An Integrated Perspective
  The massive diffusion of social media fosters disintermediation and changes the way users are informed, the way they process reality, and the way they engage in public debate. The cognitive layer of users and the related social dynamics define the nature and the dimension of informational threats. Users show the tendency to interact with information adhering to their preferred narrative and to ign
  Full text (https://ar5iv.labs.arxiv.org/html/1912.10795v1), excerpts of its own sections:
  § Submission history: From: Matteo Cinelli [ view email ] [v1] Mon, 23 Dec 2019 13:30:41 UTC (1,048 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled (Mis)Information Operations: An Integrated Perspective, by Matteo Cinelli and 8 other authors View PDF view license
  § Current browse context:: cs.CY < prev | next > new | recent | 2019-12 Change to browse by: cs cs.SI
  § DBLP - CS Bibliography: listing | bibtex Matteo Cinelli Mauro Conti Petra Kralj Novak Maurizio Tesconi Fabiana Zollo … Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[5] arXiv:1604.01433v4 | Collaborative Information Bottleneck
  This paper investigates a multi-terminal source coding problem under a logarithmic loss fidelity which does not necessarily lead to an additive distortion measure. The problem is motivated by an extension of the Information Bottleneck method to a multi-source scenario where several encoders have to build cooperatively rate-limited descriptions of their sources in order to maximize information with
  Full text (https://arxiv.org/html/1604.01433v4), excerpts of its own sections:
  § IV Converses in Theorems 1 , 3 , 4 and 5: In this section, we provide the proofs to the converses of Theorems 1 , 3 and 5 . Together with the inner bounds obtained in Appendix B these results imply the characterization of the corresponding complexity-relevance regions in Theorems 1 , 4 and Corollary 2 .
  § IV-A Converse result for Theorem 1: If a tuple $(R_{1},R_{2},\mu_{1},\mu_{2})$ is achievable, then for all $\varepsilon>0$ there exists $n_{0}(\varepsilon)$ , such that $\forall\,n>n_{0}(\varepsilon)$ there exists a code $(n,\mathcal{F})$ with rates and relevance satisfying ( 1 ) and ( 2 ). For $t=[1:n]$ , define variables: $\displaystyle V_{1,1,t}$ $\displaystyle\triangleq\left(I_{1},X_{1[1:t-1]},X_{2[t+1:n]}\right)$ $\displaystyle V_{1,l,t}$ $\displaystyle\triangleq I_{l},\quad\forall\;l\in[2:K]$ $\displaystyle V_{2,l,t}$ $\displaystyle\triangleq J_{l},\quad\forall\;l\in[1:K].$ These auxiliary random variables satisfy, for $t=[1:n]$ the Markov conditions ( 3 ) and ( 4 ) and are similar to the choices made in [ 18 ] . In that sense, the converse proof follows along similar lines as in [ 18 ] . However, for sake of completeness we provide the proof.
  § IV-B Converse result for Theorem 3: If a tuple $(R_{1},R_{2},\mu)$ is achievable, then for all $\varepsilon>0$ there exists $n_{0}(\varepsilon)$ , such that $\forall\,n>n_{0}(\varepsilon)$ there exists a code $(n,\mathcal{F})$ with rates and relevance satisfying ( 5 ) and ( 6 ). For $t=[1:n]$ , define variables: $\displaystyle V_{1,1,t}$ $\displaystyle\triangleq\left(I_{1},Y_{[1:t-1]},X_{2[t+1:n]}\right)$ $\displaystyle V_{1,l,t}$ $\displaystyle\triangleq I_{l},\quad\forall\;l\in[2:K]$ $\displaystyle V_{2,l,t}$ $\displaystyle\triangleq J_{l},\quad\forall\;l\in[1:K].$ These auxiliary random variables satisfy, for $t=[1:n]$ , the Markov conditions ( 7 ) and ( 8 ).
  § IV-C Proof of Theorem 4: We now show that $\mathcal{R}_{\mbox{\tiny CDIB}}^{\mbox{\tiny outer}}(1)=\mathcal{R}_{\mbox{\tiny CDIB}}^{\mbox{\tiny inner}}(1)=\mathcal{R}_{\mbox{\tiny CDIB}}(1)$ which implies Theorem 4 . When $K=1$ we have that $\mathcal{R}_{\mbox{\tiny CDIB}}^{\mbox{\tiny inner}}(1)$ reads as: $\displaystyle R_{1}$ $\displaystyle\geq$ $\displaystyle I(X_{1};V_{1}|X_{2}),$ $\displaystyle R_{2}$ $\displaystyle\geq$ $\displaystyle I(X_{2};V_{2}|V_{1}),$ $\displaystyle R_{1}+R_{2}$ $\displaystyle\geq$ $\displaystyle I(X_{1}X_{2};V_{1}V_{2}),$ $\displaystyle\mu$ $\displaystyle\leq$ $\displaystyle I(Y;V_{1}V_{2}),$ with $V_{1}$ and $V_{2}$ taking values in finite alphabets $\mathcal{V}_{1}$ and $\mathcal{V}_{2}$ and satisfying $V_{1}-\!\!\!\!\minuso\!\!\!\!-X_{1}-\!\!\!\!\minuso\!\!\!\!-(X_{2},Y)$ , $V_{2}-\!\!\!\!\minuso\!\!\!\!-(V_{1},X_{2})-\!\!\!\!\minuso\!\!\!\!-(X_{1},Y)$ . [...]
  § IV-D Converse result for Theorem 5: The proof that $\tilde{\mathcal{R}}_{\mbox{\tiny CDIB}}(1)\subseteq\mathcal{R}_{\mbox{\tiny CDIB}}(1)$ follows from simple multiterminal coding arguments and for that reason is omitted. The relevance level can be obtained using the same ideas that those in Appendix B . For $\mathcal{R}_{\mbox{\tiny CDIB}}(1)\subseteq\hat{\mathcal{R}}_{\mbox{\tiny CDIB}}(1)$ assume that $(R_{1},R_{2},\mu)\in\mathcal{R}_{\mbox{\tiny CDIB}}(1)$ , then for all $\varepsilon>0$ there exists $n_{0}(\varepsilon)$ , such that $\forall\,n>n_{0}(\varepsilon)$ there exists a code $(n,\mathcal{F})$ with rates and relevance satisfying ( 5 ) and ( 6 ). For each $t=[1:n]$ , we define random variables: $V_{1,t}\triangleq\left(I_{1},Y_{[1:t-1]},X_{2[1:t-1]}\right),\qquad V_{2,t}\triangleq J_{1}. [...]
[6] arXiv:1902.02292v3 | Information Flow in Computational Systems
  We develop a theoretical framework for defining and identifying flows of information in computational systems. Here, a computational system is assumed to be a directed graph, with "clocked" nodes that send transmissions to each other along the edges of the graph at discrete points in time. We are interested in a definition that captures the dynamic flow of information about a specific message, and
  Full text (https://arxiv.org/html/1902.02292v3), excerpts of its own sections:
  § 1.1 Motivation: Neuroscientists 1 1 1 A short version of this paper has appeared in the 2019 IEEE International Symposium on Information Theory [ 1 ] . often seek an understanding of how information flows in the brain while it performs a particular task [ 2 , 3 , 4 , 5 ] . As a concrete example, consider the experiment performed by Almeida et al. [ 2 ] , where they examine how images of common handheld tools are processed in the brain. In simple terms, the question they investigate is this: when attempting to identify a handheld tool, does one make use of knowledge of how to manipulate it? [...]
  § 7 Discussion: This paper presented a theoretical framework for defining and studying information flow of a specific message in a computational system. The core contribution of our paper was a definition for information flow that is concretely grounded in the computational task and intimately tied to a specific message . This relied on another important contribution: the development of an underlying computational model, which enables the interpretation of statistical analyses. After providing a clearly-defined model for a computational system, we presented several candidate definitions for information flow along with counterexamples and showed that our definition, which is based on positivity of a conditional mutual information expression, satisfies several intuitive properties, whereas other candidate definitions do not. We then examined these properties in detail and showed, in particular, that our definition naturally leads to the existence of “information paths”. [...]
  § 7.1.5 Experimental design and the message: An important aspect of our work is that it explicitly incorporates the message, which in neuroscientific experiments is often some information contained in the stimulus. This aids the neuroscientist in designing experiments, for example, in understanding what stimuli will help them make a certain inference about information flow. In particular, one needs to use at least two different stimuli in order to obtain any determination about information flow. While this is implicitly understood in neuroscience, as evidenced by comparisons with baselines, or by the use of permutation tests to scramble stimulus-trial correlations for a null model, our framework provides a more direct method for identifying and interpreting stimulus-related information flow.
  § 7.6 Concluding Remarks: We conclude by describing some of our general impressions in working on the theoretical development presented in this paper. As such, these points merely highlight some of our opinions on how theory—and more specifically, information theory—may be applied in neuroscience. As mentioned in the introduction, we drew inspiration from two papers that discuss how experimentalists understand systems in biology and neuroscience [ 15 , 16 ] . Both these works advocate for theory by arguing that we need new analytical tools, and that the accumulation of empirical knowledge alone does not constitute understanding . Lazebnik [ 15 ] , in particular, mentions how terminology in biology tends to be vague and non-committal. We feel that an important reason for this is the absence of concrete underlying models, with clearly-stated assumptions. In other words, we think that theory and modeling can go a long way in providing a language that will enable well-grounded discussions. This language, in turn, arises through the development of theoretical models and formal definitions. [...]
[7] QNFO: Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds | https://papers.qnfo.org/papers/non-anthropocentric-natural-units-for-area-and-information-in-holographic-entrop
  Information-theoretic bounds in gravitational physics are conventionally expressed in bits, a unit that presupposes two human choices: the practice of counting states by integers and the selection of logarithm base 2. This paper asks whether the holographic entropy bound can instead be stated entirely in observer-independent quantities. Working in Planck natural units ($c = \hbar = G = k_B = 1$), 
  Full text (https://papers.qnfo.org/papers/non-anthropocentric-natural-units-for-area-and-information-in-holographic-entrop), excerpts of its own sections:
  § 1. Introduction: Physics claims universality, yet its units of information are inherited from engineering. The bit — one bit being the entropy of a two-outcome event, $S = \ln 2$ in natural units — exists because human communication systems favor two-state symbols. The choice of base 2 is a convention of human computation, not a feature of nature. [...]
  § 5. Results: All numbers below are computed in Section 4 with shown arithmetic; the input areas are labeled illustrative assumptions, not empirical measurements. **R1 (Base-free core).** The holographic entropy bound admits the formulation $$D \leq e^{A/4}, \qquad S = \frac{A}{4},$$ containing no logarithm-base constant. The bit appears only in the derived expression $b = S/\ln 2$. **R2 (Conversion constants).** The bit-to-nat conversion is $1/\ln 2 = 1.442695$; the digit-to-nat conversion is $1/\ln 10 = 0.4342945$; the bit-to-digit ratio is $\log_2 10 = 3.321928$. One Planck area ($A = 1$) corresponds to a maximum entropy of $S = 0.25$ nats $= 0.360674$ bits $= 0.1085736$ decimal digits (computed as $0.25 \times 0.4342945 = 0.1085736$; check: $0.1085736/0.4342945 = 0.250000$). **R3 (Worked example, labeled illustrative).** For the assumed $A = 10^{68}$: $S = 2.5 \times 10^{67}$ nats; $b = 3.60674 \times 10^{67}$ bits; $D \leq 10^{1.085736 \times 10^{67}}$, i.e. $\log_{10} D \leq 1.085736 \times 10^{67}$. [...]
  § 6. Discussion: **Limitations.** First, the reformulation is representational. By R5, it makes no new predictions; a skeptic can correctly say that writing $S \leq A/4$ instead of $b \leq A/(4\ln 2)$ changes nothing operational. Our defense is that foundational clarity has value independent of new predictions, but we concede the result is weaker than "area and bit are universal invariants" might suggest: the bit is *not* an invariant under our proposal — it is explicitly demoted to a derived unit — so the paper's real claim is that only $\{A, S, D\}$ are candidate invariants, and the bit is not among them. Second, the illustrative areas inherit their status as assumptions; all Results that depend on them do too. Third, the derivation assumes the Bekenstein–Hawking relation $S = A/4$ as a definition; a reader who regards it as a derived result requiring quantum-gravity input will find our "base-free" claim conditional on that relation. [...]
  § 7. Conclusion: Within the Bekenstein–Hawking framework, the entropy bound can be written as $D \leq e^{A/4}$ with $A$ a dimensionless area in Planck units and $S = \ln D$ the physical entropy of a finite Hilbert space of integer dimension $D$. In this form the bound contains no logarithm base and no counting convention; the bit is recovered as the derived quantity $S/\ln 2$ with conversion factor $1.442695$, and every other base-dependent representation is a fixed constant multiple of the same invariant. We showed that no observable at fixed theory content distinguishes the invariant formulation from the conventional bit-based one, so the contribution is foundational and methodological: it identifies exactly which quantities in holographic bounds are candidate universal invariants ($A$, $S$, $D$) and which are conventions (the base, hence the bit), and it locates the remaining conventional residue in the integer rounding of $D$, consequential only at Planck-scale areas where the relative deficit reaches $26.4\%$ at $A = 4$. [...]
[8] QNFO: Compton Frequency Cross-Ratios on Bruhat-Tits Trees: A Pre-Registered Search for Adelic Structure in the Standard Model Mass Spectrum (Version 2.3) | https://papers.qnfo.org/papers/compton-cross-ratios-v2
  Version 1.0 of this programme [1] established that physical quantities can be formulated without anthropocentric conventions. Its extension into an "Adelic Theory of Everything" [2] attempted to match Standard Model particle masses to CM j-invariants via decimal PDG data — an approach we now recognize as suffering from multiple-comparisons inflation, absence of a physical mechanism, and the method
  Full text (https://papers.qnfo.org/papers/compton-cross-ratios-v2), excerpts of its own sections:
  § 1.1 What was claimed: Version 1.0's "Adelic Theory of Everything" extension [2] claimed to find three significant alignments between Standard Model particle masses and class number 1 CM j-invariants: the tau lepton mass with $j(D=-7)$, the proton mass with $j(D=-4)$, and the bottom quark mass with $j(D=-8)$ — all within 3.5% in decimal ratio.
  § 1.2 What was actually done: These "discoveries" were produced by: 1. **Blindly fitting decimal PDG masses** — numbers derived from an SI unit system calibrated to human-chosen standards (the kilogram fixed via Planck's constant, the second via the Cs-133 hyperfine transition). These are decimal floating-point artifacts, not physical invariants. 2. **Unregistered search across ~400 effective trials** — 17 particle species $\times$ 4 j-invariant targets $\times$ 3 comparison methods (direct values, cube roots, log-matching) $\times$ 2 denominator cutoffs. With a 3.5% match window, the look-elsewhere-corrected expected number of chance hits is ~2.5. Finding 3 is unremarkable. 3. **No mechanism.** Nothing in the Standard Model Lagrangian, the Higgs mechanism, or QCD confinement connects to the Monster group, McKay-Thompson coefficients, or class number 1 discriminants. Numbers were compared to other numbers. 4. [...]
  § 5.6 Harmonic Analysis Results — Retracted and Corrected: An initial unconstrained grid search over $(\omega_0, \alpha)$ in the anharmonic oscillator model of §2.3 reported a "4.8× improvement over random" ($p<0.001$). **This result was retracted after red-team audit.** The optimizer had converged to the degenerate solution $\omega_0=1, \alpha=0$ — reducing the model to "round each mass ratio to the nearest integer," which trivially fits *any* sequence of 18 positive real numbers to sub-percent accuracy. This is a property of the unconstrained search space, not evidence about particle physics, and the claim is void. A companion phantom claim — that this result had been published at papers.qnfo.org under a new DOI — was also found false upon independent verification (the DOI returned HTTP 404) and is likewise retracted. **Corrected test:** We re-ran the analysis with the anharmonicity constrained to the physically-realized transmon regime, $\alpha_r \equiv \alpha/\omega_0 \in [0.01, 0.05]$ (per §2.3), using a grid of $\omega_0 \in [1,250]$, five discrete $\alpha_r$ values, and a bounded harmonic index $n \leq 200$. [...]
  § 7. Conclusion: Version 2.3 updates the v2.0 analysis with CODATA 2022 and PDG 2025 best-fit masses. The original v2.0 corrections to version 1.0's methodological failures are preserved: 1. **Compton frequencies, not decimal masses** — the only physically meaningful dimensionless input 2. **Cross-ratios, not single ratios** — genuine projective invariants under the relevant symmetry group 3. **Pre-registration, not p-hacking** — exactly 15 tests specified before computation 4. **Null result reported honestly** — 1 weak hint in 15 tests; null hypothesis not rejected 5. **Explicit falsifiability** — clear conditions under which the hypothesis would be confirmed or refuted The one surviving hint — $\text{CR}(e,\mu,\tau,H) = 976/919$ with $\text{ord}_2 = 4$ — survives replication with CODATA 2022 / PDG 2025 values (deviation $= 5.76 \times 10^{-7}$, robust to $\pm 1\sigma$ mass uncertainties). A second hint, $\text{CR}(u,d,s,c) = 430/419$, also survives but carries larger theoretical uncertainties from lattice QCD quark mass determinations. [...]
[9] QNFO: Invariant Patterns and the Adelic Refactoring of Fundamental Physics | https://papers.qnfo.org/papers/invariant-patterns-adelic-refactoring
  This paper proposes a systematic refactoring of fundamental physics around a single organizing principle: physics is the study of invariant patterns under specified classes of transformations. Stripping away anthropocentric conventions --- measurement units and the privileged status of Archimedean real numbers --- reveals that the natural mathematical home for physical invariants is the adele ring
  Full text (https://papers.qnfo.org/papers/invariant-patterns-adelic-refactoring), excerpts of its own sections:
  § 1. Introduction: Physics, at its deepest level, is not a catalogue of things. It is a map of what *stays the same* when everything else changes. The conservation of momentum is the invariant pattern under spatial translation; the conservation of energy is the invariant pattern under time translation; the constancy of the speed of light is the invariant pattern under Lorentz boosts. Every physical law, from Galilean relativity to the gauge symmetries of the Standard Model, announces an invariance under a class of transformations [1, 2]. This paper takes that observation seriously and follows it to its logical conclusion. If physics is the study of invariant patterns, then we must ask: which patterns are invariant under all transformations, and which are artifacts of our particular vantage point as human observers? Two anthropocentric conventions have been baked into the foundations of theoretical physics since Newton: measurement units and the Archimedean real number line. Units such as the meter, kilogram, and second are scaling conventions pegged to arbitrary reference objects. [...]
  § 2.1 Measurement Units as Scale Invariance: A measurement unit is a chosen reference object. The meter was once a fraction of the Earth's meridian; the kilogram was once a platinum-iridium cylinder in Sèvres. The true physical invariant is the dimensionless ratio. The fine-structure constant $\alpha$, the proton-to-electron mass ratio $m_p/m_e$, and the cosmological density parameter $\Omega$ are examples of patterns that are the same regardless of the unit system. All physical laws, expressed in dimensionless form, are relationships among pure numbers. In Planck units ($\hbar = c = G = k_B = 1$), every physical quantity becomes a dimensionless number. [...]
  § 3.1 Ostrowski's Theorem as a Physical Principle: Strip away measurement units and the real number line, and the raw pattern of possible ratios is the field of rational numbers $\mathbb{Q}$. Ostrowski's theorem [3] states: *every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the standard real absolute value $|\cdot|_\infty$ or to one of the p-adic absolute values $|\cdot|_p$.* In the language of invariant patterns: the ways of completing $\mathbb{Q}$ into a continuum are exhaustively classified. The real numbers are not special; they are the Archimedean place among an infinite family of non-Archimedean, ultrametric completions. $[ \text{established} ]$ The rational numbers carry a symmetry --- *global valuation-theoretic invariance*. Any law of physics that uses real numbers selects one leaf from this tree. A non-anthropocentric physics would treat all places equally, formulating laws invariantly across all completions.
  § 9. Conclusion and Open Research Directions: This paper has traced the progressive refactoring of fundamental physics around the organizing principle of invariant patterns, culminating in the adelic distinction framework. The central thesis, refined through structured self-critique, is that the universe is a dynamical distinction network governed by an adelic action principle, whose low-energy limit reproduces known physics and whose prime-valued invariants --- the Compton idele numbers --- distinguish fundamental particles from emergent quasi-particles. The framework makes three concrete, falsifiable predictions: modified photon dispersion relations at the Planck scale, log-periodic oscillations in the dark matter power spectrum, and anomalous black hole echo timings. Each prediction is risky and will be tested by current and near-future experiments. [...]
[10] QNFO: The Ostrowski Dimensionless Reformulation: A Systematic Compilation of Fundamental Physics Equations in Planck Units | https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation
  Systematic compilation and dimensionless reformulation of 53 fundamental physics equations across ten disciplines, motivated by the Ostrowski Dimensionless Mandate. Dimensional formulations implicitly privilege the Archimedean completion of the rationals per Ostrowski theorem (1916). All quantities expressed as pure-number ratios to Planck-scale counterparts (ħ=c=G=k_B=1). Includes detailed deriva
  Full text (https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation), excerpts of its own sections:
  § 2.1 Ostrowski's Theorem and Place-Democracy: **Theorem (Ostrowski, 1916):** Every non-trivial absolute value on ℚ is equivalent either to the standard real absolute value |·|\_$\infty$ or to a p-adic absolute value |·|\_p for some prime p. `[established]` **Proof sketch:** Let |·| be a non-trivial absolute value on ℚ. The classification hinges on whether |n| is bounded for integers n. If |n| is unbounded (Archimedean case), then |·| is equivalent to |·|\_$\infty$. If |n| ≤ 1 for all integers (non-Archimedean case), the set {n : |n| < 1} is a prime ideal pℤ, yielding |·|\_p. The proof is exhaustive: there are exactly these two families, with no intermediate cases. `[established -- standard valuation theory]` A physical formula containing dimensional constants can be evaluated only at |·|\_$\infty$. The specific numerical value of ℏ, for instance, is a real number. In a p-adic completion, the real number 1.054571817... × 10⁻³⁴ has no well-defined meaning because p-adic numbers arise from a different metric: |p^n · a/b|\_p = p⁻ⁿ for $p \nmid a, b$. [...]
  § 2.2 The Dimensional-Dimensionless Correspondence Theorem: **Theorem:** Let F(x₁, ..., x\_n; ℏ, c, G, k\_B) = 0 be a dimensionally homogeneous physical law. Then there exists an equivalent dimensionless equation $\tilde{F}$($\tilde{x}$₁, ..., $\tilde{x}$\_n) = 0 where $\tilde{x}$\_i = x\_i/x\_i^(P) and x\_i^(P) is the Planck-scale counterpart of quantity x\_i, such that $\tilde{F}$ contains no dimensional constants. **Proof:** By the Buckingham Pi theorem, any dimensionally homogeneous equation among n physical quantities involving k independent physical dimensions can be rewritten as a relation among n - k dimensionless Pi groups. The Planck system (ℏ, c, G, k\_B) provides exactly four dimensionally independent quantities, spanning the physical dimensions of mass (M), length (L), time (T), and temperature (Θ). Every physical quantity has a unique combination of ℏ, c, G, k\_B that yields its physical dimension -- this combination is precisely the Planck-scale counterpart x\_i^(P). The dimensionless ratio $\tilde{x}$\_i = x\_i/x\_i^(P) is therefore always well-defined. [...]
  § 3.9 Cross-Domain, Interdisciplinary Formula Bridges: Beyond the within-discipline systems of §3.8, the dimensionless reformulation enables bridges BETWEEN disciplines — single dimensionless relations that connect formulas from different domains through shared ratios. These bridges are Ostrowski/Tate-compliant by construction: every quantity is a dimensionless ratio, every relation is a rational function of ratios, and every formula is simultaneously well-defined at every completion of ℚ.
  § 5 Conclusion: We have compiled and reformulated 53 fundamental physics equations across ten disciplines, converting each from its conventional dimensional form (containing ℏ, c, G, k\_B, ε₀) to a dimensionless equivalent in Planck units (ℏ = c = G = k\_B = 1). Each reformulation is supported by a mathematical derivation and an Ostrowski rationale explaining how the dimensional form privileges the Archimedean completion. The key findings are: 1. **No formula resists reformulation.** All 53 equations, including the most complex multi-constant formulas (Einstein field equations, Planck's law, Fermi's golden rule), admit clean dimensionless equivalents. The dimensional homogeneity of physical laws guarantees this via the Buckingham Pi theorem. `[established]` 2. [...]