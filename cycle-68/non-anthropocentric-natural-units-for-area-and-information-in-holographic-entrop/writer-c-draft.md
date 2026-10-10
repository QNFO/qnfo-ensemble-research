# Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds

## Abstract

Information-theoretic bounds in gravitational physics are conventionally expressed in bits, a unit that presupposes a human-selected logarithm base (base 2) and a human practice of integer counting. This paper asks whether the holographic entropy bound can instead be stated entirely in observer-independent quantities. We work in Planck natural units ($c = \hbar = G = k_B = 1$), in which area $A$ is measured in Planck areas $\ell_P^2$ and is therefore dimensionless, and we take the Bekenstein–Hawking value $S = A/4$ (in nats) as the definition of the entropy of a region's horizon. We show that the bound $D \leq e^{A/4}$ on the Hilbert-space dimension $D$ of a finite region contains no base-dependent constant, that the "bit" is recoverable only as the derived, base-dependent quantity $S/\ln 2$, and that the integer character of $D$ introduces a rounding convention that is itself observer-imposed. We compute worked examples: a horizon patch of area $A = 10^{68}$ in Planck units carries $S = 2.5 \times 10^{67}$ nats, or $3.60674 \times 10^{67}$ bits, and permits $D \leq e^{2.5 \times 10^{67}}$, i.e. $\log_{10} D \leq 1.08574 \times 10^{67}$. We argue that no observable consequence distinguishes the invariant formulation from the conventional one, because the two differ only by a fixed rescaling of units, and we identify the rounding of $D$ to an integer as the genuine open problem.

## 1. Introduction

Physics claims universality, yet its units of information are inherited from engineering. The bit — one bit being the entropy of a two-outcome event, $S = \ln 2$ nats — exists because human communication systems favor two-state symbols. The choice of base 2 is a convention of human computation, not a feature of nature. The same criticism applies, though more weakly, to the practice of counting: Hilbert-space dimension is an integer, but "which integer" is only meaningful once a tensor-product factorization and a normalization convention have been chosen by an observer.

The holographic entropy bound offers an unusual opportunity. In the Bekenstein–Hawking framework, the entropy of a black hole horizon is proportional to its area, and the entanglement entropy of a finite spacetime region is bounded by a quantity of the form $\exp(A/4\ell_P^2)$. If one adopts Planck natural units, in which $c = \hbar = G = k_B = 1$, the Planck length $\ell_P$ becomes the unit of length, area becomes dimensionless, and the bound can be written as

$$D \leq e^{A/4},$$

where $A$ is the dimensionless area and $D$ is the dimension of the Hilbert space associated with the region. Expressed this way, the bound involves exactly two ingredients: a geometric invariant (area in Planck units) and the exponential function, whose base $e$ is not chosen but forced by the requirement that the entropy be additive under composition of independent systems. No logarithm base appears, because the natural logarithm is the unique logarithm whose derivative properties make entropy additive; every other base introduces an arbitrary constant factor.

The conjecture this paper develops is that the entire content of the holographic bound can be restated using only the dimensionless entropy $S = A/4$, with the bit recovered as a derived, base-dependent quantity $b = S/\ln 2$. If correct, information-theoretic bounds in gravitational physics are grounded in observer-independent geometry rather than in human conventions of notation and counting.

The stakes are conceptual but not trivial. A formulation free of anthropocentric units is a formulation in which the bound's constants are fixed by mathematics rather than by history. Conversely, if the program fails — if some irreducibly conventional choice remains — the failure itself is informative, because it locates precisely where observer-dependence enters the foundations of entropy bounds.

Our contributions are: (i) a precise statement of the natural-unit formulation of the Bekenstein–Hawking and covariant entropy bounds; (ii) explicit derivations showing which quantities are base-independent and which are not, with worked numerical examples computed in full; (iii) an analysis of the integer-rounding problem for the Hilbert-space dimension $D$, which we argue is the one genuinely non-derivable convention left in the framework; and (iv) a falsifiability discussion: we show that the invariant formulation and the conventional formulation are related by a fixed change of units and therefore make identical predictions, so the proposal's significance is foundational rather than empirical.

## 2. Background and Related Work

We review the supplied literature, noting at the outset that several entries are tangential to gravitational entropy bounds and that we confine ourselves to what each entry's own summary supports.

[2] is the closest antecedent. Its summary states that the holographic bound in physics constrains the complexity of life, that the finite storage capability of information in the observable universe requires "protein linguistics" in the evolution of life, and that the evolution of the genetic code determines the variance of amino acid frequencies and genomic GC content among species. This is directly relevant to our project in two ways. First, it applies a holographic storage bound as a physical constraint on real systems, illustrating how the bound is used operationally. Second, its subject matter — genetic codes and amino-acid frequencies — is a domain where information is measured in bits and bases chosen for biological convenience, exactly the convention-laden setting our program aims to bypass. We use [2] as evidence that holographic bounds are treated as physically binding constraints on information content, which motivates asking in what units those constraints are most naturally stated.

[12] is the direct predecessor of this paper within the QNFO corpus. Its summary states that it strips away anthropocentric constructions from the Bekenstein–Hawking entropy bound, treats area as a dimensionless geometric invariant, defines the exponential bound without logarithmic base, and takes the integer Hilbert-space dimension as a universal invariant; it further connects the program to Ostrowski's theorem, stating that the theorem "reveals the Archimedean completion is" (the summary is truncated at this point, so we cannot report what the completion is claimed to reveal). Our paper takes [12]'s program as its starting point and contributes what [12]'s summary does not contain: explicit numerical derivations, a systematic separation of base-dependent from base-independent quantities, and an analysis of the integer-rounding problem, which [12]'s summary does not address.

[3] develops computer-assisted proof methods involving non-classical inequalities for Shannon entropy, applied to secret sharing schemes and hat guessing games; in the former a random secret value is transformed into shares distributed among participants so that only qualified groups can recover it. This matters for us because Shannon entropy is the canonical example of a quantity whose numerical value depends on the logarithm base: the inequalities of [3] are stated in whatever base the Shannon formalism fixes, and our program asks whether the physical content of such inequalities survives a change to base-free (natural-log) form. Since rescaling entropy by a constant preserves the truth of homogeneous inequalities, we expect the answer to be yes for homogeneous statements — a point we return to in Section 4.

[4] considers classical communication over a finite-dimensional quantum channel with memory, using separable-state input ensembles and local output measurements, and proposes algorithms for estimating and bounding the information rate of such setups, some based on auxiliary channels. The relevance is that "information rate" is itself a derived, convention-dependent quantity: it is an entropy per unit time or per channel use, and its numerical value inherits the base of the underlying entropy. [4]'s finite-dimensional channel setting is also the discrete setting in which our Hilbert-space dimension $D$ lives.

[7] investigates a multi-terminal source coding problem under logarithmic loss fidelity, noting that this loss does not necessarily lead to an additive distortion measure, as an extension of the Information Bottleneck method to multi-source scenarios. Logarithmic loss is the unique fidelity measure under which entropy and mutual information arise naturally as distortion quantities, and its definition again fixes a logarithm base by convention. [7] is useful to us as an example of a coding framework whose distortion metric is logarithmic and therefore base-sensitive, reinforcing that base choice pervades information theory, not just gravitational bounds.

[8] develops a theoretical framework for defining and identifying flows of information in computational systems, modeling a computational system as a directed graph with "clocked" nodes that send transmissions along edges at discrete times, and seeking a definition that captures dynamic flow of information about a specific message. This is relevant because "information flow" is an informal notion that must be made precise through some quantitative definition; [8] supplies one for computational systems, and our paper asks the parallel question for physical systems bounded by holographic entropy.

[1] concerns natural language processing, described in its summary as a branch of computer science combining artificial intelligence with linguistics, aiming to analyze language elements such as writing or speech with software and convert them into information, with complexity arising because each language has its own grammatical rules and vocabulary diversity. We cite [1] for a structural analogy: just as each natural language imposes its own vocabulary and rules on the analysis of "information" in text, each unit system (bits, nats, digits) imposes its own base on the analysis of entropy. The analogy is illustrative only; [1]'s summary contains nothing about entropy bounds.

[6] examines (mis)information operations from an integrated perspective, arguing that the massive diffusion of social media fosters disintermediation, changes how users are informed and process reality, and that the cognitive layer of users and related social dynamics define the nature and dimension of informational threats, with users tending to interact with information adhering to their preferred narratives. We cite [6] as a study in which "information" is defined through human cognition — the extreme opposite pole from our program, which seeks a definition of information through observer-independent geometry. The contrast clarifies what "non-anthropocentric" means in our title.

[5] describes the Gamma ray Large Area Space Telescope (GLAST) Large Area Telescope (LAT), a pair-production high-energy (>20 MeV) gamma-ray telescope built by an international partnership for a satellite launch in 2006, and notes that the collaboration built a balloon flight engineering model as part of the development effort. Its summary gives no further detail bearing on entropy bounds; we cite it only as an example of large-scale empirical astrophysics whose measurements are reported in human-defined units, the practice our natural-unit program would ideally replace at the level of fundamental bounds.

[9], [10], and [11] are QNFO corpus works whose supplied summaries are empty; we therefore cannot state what they contain and relate them to our argument only through their titles and identifiers. We note this limitation explicitly rather than attributing content to them.

## 3. Methods

### 3.1 Natural-unit setting

We adopt Planck natural units throughout:

$$c = \hbar = G = k_B = 1.$$

In these units the Planck length $\ell_P$ is the unit of length, the Planck area $\ell_P^2$ is the unit of area, and any physical area $A_{\text{phys}}$ is represented by the dimensionless number

$$A = \frac{A_{\text{phys}}}{\ell_P^2}.$$

Temperature is measured in energy units and entropy is dimensionless. The Boltzmann constant $k_B$, which converts temperature to energy, is set to 1, so entropy is measured in nats: one nat is the entropy of an event with Hilbert-space dimension $e$.

### 3.2 The base-free entropy bound

The Bekenstein–Hawking entropy of a horizon of area $A_{\text{phys}}$ is

$$S_{\text{BH}} = \frac{k_B\, A_{\text{phys}}}{4\,\ell_P^2},$$

which in natural units becomes

$$S_{\text{BH}} = \frac{A}{4}.$$

We take this as the definition of the entropy associated with a region's boundary. The corresponding bound on the Hilbert-space dimension $D$ of the region is obtained by inverting the thermodynamic relation $S = \ln D$ (valid for a maximally mixed state on a $D$-dimensional Hilbert space):

$$D \leq e^{S} = e^{A/4}.$$

This is the central object of the paper. Note its ingredients: the dimensionless area $A$, the integer 4 (a geometric factor from the Bekenstein–Hawking relation), and the exponential function. The base $e$ of the exponential is not a convention: it is forced by additivity of entropy under composition. If two disjoint regions with areas $A_1$ and $A_2$ have independent Hilbert spaces of dimensions $D_1$ and $D_2$, the composite dimension is $D_{12} = D_1 D_2$, and only the natural logarithm satisfies

$$\ln(D_1 D_2) = \ln D_1 + \ln D_2.$$

Any other base $b$ would give $\log_b(D_1 D_2) = \log_b D_1 + \log_b D_2$ as well — all logarithms are additive — but the *physical* entropy defined by the Bekenstein–Hawking relation $S = A/4$ is fixed in nats by geometry; choosing a different base for its expression introduces the constant factor $1/\ln b$ with no geometric origin. The nat is thus distinguished, not chosen.

### 3.3 Recovery of the bit as a derived quantity

The bit is defined by

$$b = \frac{S}{\ln 2} = \frac{A}{4 \ln 2}.$$

The constant $\ln 2 \approx 0.693147$ is a pure mathematical constant, so the bit is well-defined — but its presence in any formula marks exactly where a human convention (binary representation) has been imported. Our method is to carry $S$ (nats) through all derivations and convert to bits only at the output stage, so that every intermediate statement is base-free.

### 3.4 Method of analysis

We proceed by: (a) stating each quantity in the conventional formulation; (b) rewriting it in natural units; (c) classifying it as base-free (expressible via $S = A/4$ alone), derived (expressible only with an explicit base constant such as $\ln 2$ or $\ln 10$), or conventional (requiring a choice not fixed by mathematics or geometry, such as integer rounding of $D$); and (d) computing worked numerical examples with full arithmetic.

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

### 4.2 Worked example: a macroscopic horizon patch

**Input numbers.** We assume, as a labeled illustrative choice, a horizon patch with dimensionless area

$$A = 10^{68} \quad (\text{assumption: patch area in Planck units}).$$

This magnitude is chosen for illustration only; no empirical claim is made about any specific physical system.

**Step 1: entropy in nats.**

$$S = \frac{A}{4} = \frac{10^{68}}{4} = 2.5 \times 10^{67} \ \text{nats}.$$

**Step 2: bits.** Using $\ln 2 = 0.693147\ldots$ and $1/\ln 2 = 1.442695\ldots$:

$$b = \frac{S}{\ln 2} = 2.5 \times 10^{67} \times 1.442695 = 3.60674 \times 10^{67} \ \text{bits}.$$

Arithmetic check: $2.5 \times 1.442695 = 3.6067375$, so $b = 3.60674 \times 10^{67}$ (5 significant figures).

**Step 3: Hilbert-space dimension bound.**

$$D \leq e^{S} = e^{2.5 \times 10^{67}}.$$

This number is too large to write directly; we express it via its base-10 logarithm. Using $\ln 10 = 2.302585\ldots$:

$$\log_{10} D \leq \frac{S}{\ln 10} = \frac{2.5 \times 10^{67}}{2.302585} = 1.08574 \times 10^{67}.$$

Arithmetic check: $2.5 / 2.302585 = 1.085736\ldots$, so $\log_{10} D \leq 1.08574 \times 10^{67}$, i.e.

$$D \leq 10^{1.08574 \times 10^{67}}.$$

**Step 4: base-dependence audit.** The statements $S = 2.5 \times 10^{67}$ nats and $D \leq e^{2.5 \times 10^{67}}$ contain no chosen base. The statements $b = 3.60674 \times 10^{67}$ bits and $\log_{10} D \leq 1.08574 \times 10^{67}$ each contain an explicit base constant ($\ln 2$, $\ln 10$). The audit confirms the classification of Section 4.1.

### 4.3 Invariance of the bound under base change

Suppose an alternative formulation expresses entropy in base $b$: $\tilde{S} = \log_b D = S/\ln b$. The bound $D \leq e^{A/4}$ becomes

$$\tilde{S} \leq \frac{A}{4 \ln b}.$$

This is the same constraint multiplied by the constant $1/\ln b$. For any homogeneous inequality — one in which every term is an entropy multiplied by fixed coefficients — the truth value is unchanged, because multiplying both sides by the same positive constant preserves the inequality. This is the formal reason we expect the non-classical Shannon inequalities of [3] to be robust to base choice: their summaries describe inequalities for Shannon entropy, and homogeneous entropy inequalities are invariant under rescaling of the entropy unit. (We emphasize this is our structural argument, not a finding of [3].)

### 4.4 The integer-rounding deficit

The floor function introduces a loss:

$$\Delta = e^{A/4} - \lfloor e^{A/4} \rfloor \in [0, 1).$$

For small areas this matters proportionally. Take the minimal nontrivial case $A = 4$ (one Planck area times the geometric factor 4):

$$e^{A/4} = e^{1} = 2.71828\ldots,$$

so

$$D \leq \lfloor e \rfloor = 2, \qquad \Delta = 2.71828 - 2 = 0.71828.$$

The relative deficit is

$$\frac{\Delta}{e} = \frac{0.71828}{2.71828} = 0.26424,$$

i.e. the integer bound discards about $26.4\%$ of the allowed dimension at $A = 4$. Arithmetic check: $0.71828/2.71828 = 0.264241\ldots$.

For the macroscopic example of Section 4.2, the absolute deficit remains below 1 while $D \sim 10^{1.08574 \times 10^{67}}$, so the relative deficit is astronomically small. The rounding convention is therefore consequential exactly in the regime of Planck-scale areas — the regime where quantum gravity, not information theory, dominates — and inconsequential macroscopically. This locates the anthropocentric residue precisely: it survives only where the theory is least controlled.

### 4.5 Comparison with the conventional formulation

The conventional formulation writes the bound as $S \leq A/(4\ell_P^2)$ with $S$ in bits:

$$S_{\text{bits}} \leq \frac{A_{\text{phys}}}{4 \ell_P^2 \ln 2}.$$

The natural-unit formulation writes $S \leq A/4$ with $S$ in nats. The two differ by the constant factor $\ln 2 \approx 0.693147$ and by the unit of area. Since both $\ln 2$ and $\ell_P$ are fixed once and for all, the two formulations are related by a fixed change of units and make identical predictions for every observable. We state this as a theorem-level claim of this paper: **no observable consequence distinguishes the invariant formulation from the conventional one.** The significance of the program is therefore foundational (which quantities are primitive) rather than empirical (which numbers differ).

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; the input area $A = 10^{68}$ is a labeled illustrative assumption, not an empirical measurement.

**R1 (Base-free core).** The holographic entropy bound admits the formulation

$$D \leq e^{A/4}, \qquad S = \frac{A}{4},$$

containing no logarithm-base constant. The bit appears only in the derived expression $b = S/\ln 2$.

**R2 (Worked example).** For $A = 10^{68}$ (assumed):
- $S = 2.5 \times 10^{67}$ nats;
- $b = 3.60674 \times 10^{67}$ bits;
- $D \leq 10^{1.08574 \times 10^{67}}$, i.e. $\log_{10} D \leq 1.08574 \times 10^{67}$.

**R3 (Rounding deficit at minimal scale).** At $A = 4$: $e^{A/4} = e = 2.71828\ldots$, so the integer bound is $D \leq 2$, with relative deficit $\Delta/e = 0.26424$ (about $26.4\%$).

**R4 (Invariance).** Any homogeneous entropy inequality is invariant under change of entropy base, since base change multiplies all entropy terms by the same constant $1/\ln b$.

**R5 (Empirical equivalence).** The natural-unit and conventional formulations are related by a fixed change of units ($\ln 2$ and $\ell_P$) and are empirically indistinguishable; no experiment can prefer one over the other.

## 6. Discussion

**Limitations.** First, the input $A = 10^{68}$ is illustrative; we make no claim that any particular physical region has this area, and all Results that depend on it inherit that status. Second, the derivation assumes the Bekenstein–Hawking relation $S = A/4$ as a definition; a reader who regards it as a derived result requiring quantum-gravity input will find our "base-free" claim conditional on that relation. Third, the additivity argument for the nat (Section 3.2) shows the nat is *distinguished* among logarithm bases, but it does not show that entropy must be logarithmic at all; that assumption is inherited from the Bekenstein–Hawking framework.

**Failure modes.** The program fails if (i) the constant 4 in $S = A/4$ turns out to encode a convention (e.g., a choice of horizon slicing) rather than geometry; (ii) the Hilbert-space dimension $D$ is not well-defined for a sub-region, because Hilbert-space factorization is itself observer-dependent — in that case the "integer universal invariant" of [12] is not invariant, and our rounding analysis (R3) quantifies the wrong thing; or (iii) entropy at Planck scale is not additive, breaking the uniqueness argument for the natural logarithm.

**What would falsify the claims.** R5 (empirical equivalence) is falsified if any observable is found that depends on the entropy base — which would require a physical coupling to the *representation* of entropy rather than its value; we know of no mechanism for this, and the claim stands as a structural consequence of unit-change equivalence. R1 is falsified if the bound requires a base-dependent correction term (e.g., logarithmic corrections to $S = A/4$ with coefficients involving $\ln 2$ or $\pi$ from counting); such corrections would reintroduce base constants into the core formula.

**Open questions.** (1) Is the factor 4 conventional? (2) Does a sub-region of a holographic system have a well-defined Hilbert-space dimension at all, given that factorization is ambiguous? (3) Can the floor function $\lfloor e^{A/4} \rfloor$ be replaced by a geometrically motivated integer, e.g. via a counting of Planck-cell states, which would remove the last conventional element? (4) Do the non-classical entropy inequalities studied in [3] admit base-free analogues beyond the homogeneous case — i.e., do any of them mix entropy with non-entropy quantities in a way that breaks rescaling invariance? The summaries of [3] and [4] describe inequality and rate bounds for Shannon and channel information, and a systematic base-audit of such results is a natural follow-up. (5) The truncated summary of [12] invokes Ostrowski's theorem concerning Archimedean completion; integrating that number-theoretic thread with the rounding problem of Section 4.4 is left open, since the supplied summary does not state the connection in enough detail to build on.

**Arguing against ourselves.** A critic may say the whole program is trivial: changing units never changes physics, so "non-anthropocentric units" is a relabeling. Our reply is that the program is not about predictions but about primitiveness — identifying which quantities in a foundational bound are forced (area, $e$, the factor 4, given the framework) and which are chosen (base 2, integer counting). The rounding analysis of R3 shows the residue is not zero: at Planck-scale areas, the integer convention discards $26.4\%$ of the allowed dimension, a concrete, computed marker of where human counting still enters. A further critic may note that the nat itself is named after a human practice (natural logarithms); we concede the naming but not the dependence — the additivity argument fixes the base mathematically.

## 7. Conclusion

Within the Bekenstein–Hawking framework, expressed in Planck natural units, the holographic entropy bound takes the base-free form $D \leq e^{A/4}$ with $S = A/4$ nats. The bit is recoverable only as the derived quantity $b = S/\ln 2$, and every base-dependent statement in the conventional formulation carries an explicit base constant. Worked examples confirm the classification: for an assumed area $A = 10^{68}$, the bound is $S = 2.5 \times 10^{67}$ nats, $b = 3.60674 \times 10^{67}$ bits, $D \leq 10^{1.08574 \times 10^{67}}$. The one irreducibly conventional element is the integer rounding of the Hilbert-space dimension, which at minimal area $A = 4$ discards a computed relative deficit of $0.26424$ of the allowed dimension and is negligible macroscopically. The invariant and conventional formulations are empirically indistinguishable, so the contribution is foundational: it maps exactly where observer-independent physics ends and human convention begins in one of the deepest bounds in physics. The literature reviewed shows both the reach of holographic constraints into biology and complexity [2], [12] and the pervasiveness of base-dependent information measures across information theory [3], [4], [7], [8]; the program of this paper is to make the former independent of the latter's conventions.

## References

[1] arXiv:2101.11436v1 | Challenges Encountered in Turkish Natural Language Processing Studies

[2] arXiv:0704.1169v1 | Holographic bound and protein linguistics

[3] arXiv:2310.09232v2 | Bounds on Guessing Numbers and Secret Sharing Combining Information Theory Methods

[4] arXiv:1903.00199v3 | Bounding and Estimating the Classical Information Rate of Quantum Channels with Memory

[5] arXiv:astro-ph/0209615v2 | Gamma ray Large Area Space Telescope (GLAST) Balloon Flight Engineering Model: Overview

[6] arXiv:1912.10795v1 | (Mis)Information Operations: An Integrated Perspective

[7] arXiv:1604.01433v4 | Collaborative Information Bottleneck

[8] arXiv:1902.02292v3 | Information Flow in Computational Systems

[9] QNFO: Ten-Fingered Trap

[10] QNFO: The Threshold of Meaning | DOI 10.5281/zenodo.19202950

[11] QNFO: Super-Universe | DOI 10.5281/zenodo.19347807

[12] QNFO: Non-Anthropocentric Natural Units: From the Bekenstein Bound to Ostrowski's Theorem | DOI 10.5281/zenodo.21480756