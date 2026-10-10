# Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds

## Abstract

The holographic and Bekenstein entropy bounds are conventionally quoted in bits, a unit that presupposes two human choices: the integer counting of distinguishable states and the choice of logarithm base 2. We ask whether the bounds can be restated entirely in observer-independent quantities. Working in Planck natural units ($c = \hbar = G = k_B = 1$), we reformulate the horizon entropy bound as $S \le A/4$, where $A$ is the dimensionless area of the bounding surface in Planck units and $S$ is physical entropy in nats, i.e. the natural logarithm of Hilbert-space dimension. We show that the bound then contains no logarithmic base, no counting convention, and no unit external to the theory; the familiar bit count $A/(4\ln 2)$ is recovered as a derived, base-dependent quantity with conversion factor $1/\ln 2 \approx 1.442695$. We verify that all base-dependent representations differ only by constant rescalings of the same dimensionless entropy, so no observable can distinguish the invariant formulation from the conventional one at fixed theory content; the difference is representational, not empirical. We relate the proposal to prior work on holographic constraints on complexity, information inequalities, quantum channel information rates, and an earlier non-anthropocentric-units program, and we state the conditions under which the claim would fail.

## 1. Introduction

Physics quotes information in bits. A bit is the entropy of a two-outcome system, $S = \ln 2$ in natural units, and the statement "the horizon of a black hole carries $A/(4\ell_P^2)$ bits of entropy" therefore embeds two conventions: that states are counted by integers (so that entropy is a logarithm of a dimension) and that the logarithm is base 2. Neither convention is supplied by physics. The natural logarithm is distinguished only by the choice of $e$ as base; base 2 is distinguished only by binary engineering practice. A bound on entropy, if it is a statement about nature rather than about our bookkeeping, should not depend on either.

This paper develops that observation into a concrete reformulation. The conjecture, taken from the author's research notes and from a prior companion paper [12], is that within the holographic/Bekenstein framework the quantities "area" and "information" admit definitions as universal invariants, free of human-constructed conventions. The proposal is:

1. Work in Planck natural units $c = \hbar = G = k_B = 1$, in which area is already dimensionless: $A$ is measured in multiples of $4\ell_P^2$-scale Planck areas.
2. State the horizon entropy bound as $S \le A/4$ with $S$ the physical entropy, defined as the natural logarithm of the Hilbert-space dimension $d$ of the region: $S = \ln d$.
3. Treat the bit as a derived, explicitly base-dependent quantity: $N_{\text{bit}} = S/\ln 2$.

The reformulation is not a new bound; it is a change of representation of the standard bound. Its interest is foundational: if successful, the information-theoretic content of holography is grounded in observer-independent geometry (a dimensionless area) and observer-independent algebra (an integer Hilbert-space dimension), with all logarithmic bases demoted to unit conversions. We prove a small no-go/consistency result: because every base-$b$ representation is $S/\ln b$ for the same $S$, the family of representations is related by known constants and no experiment at fixed theory content can distinguish among them. The claim "the invariant formulation is the correct one" is therefore methodological, not empirical, and we say so plainly.

The paper is organized as follows. Section 2 reviews the related literature supplied with this project. Section 3 sets up the formal framework. Section 4 carries out the explicit derivations, including all arithmetic. Section 5 reports the computed results and clearly labeled projections. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 concludes.

## 2. Background and Related Work

We discuss the twelve works supplied in the bibliography, in their given order. Several are only loosely connected to holography; we use them for what their supplied summaries actually state, and we note where a summary is thin.

[1] treats natural language processing as a branch of computer science combining artificial intelligence with linguistics, aimed at analyzing language elements such as writing or speech with software and converting them into information, and notes that each language's own grammatical rules and vocabulary diversity make studies in this field complex. The connection to our topic is analogical only: it is a reminder that "information" in applied contexts is defined relative to a symbol system with its own conventions, which is precisely the anthropocentric dependence we seek to remove from entropy bounds. The supplied summary is truncated and gives no further technical detail.

[2] argues that the holographic bound in physics constrains the complexity of life, that the finite storage capability of information in the observable universe requires "protein linguistics" in the evolution of life, and reports finding that the evolution of the genetic code determines the variance of amino acid frequencies and genomic GC content among species, with the linguistic mechanism confirmed by experimental observations (the summary is cut off mid-sentence). This is the closest supplied work to our theme: it takes the holographic bound as a physical constraint on information capacity and applies it outside gravitation. We use it only as evidence that holographic bounds are treated as substrate-independent capacity statements, which motivates asking in what units such a capacity is defined.

[3] develops computer-assisted proof methods involving non-classical inequalities for Shannon entropy and applies them to secret sharing schemes, in which a random secret value is transformed into shares distributed among participants so that only qualified groups recover it, and to hat guessing games. Its relevance is that Shannon entropy there is handled as an abstract quantity obeying inequalities, independent of any particular logarithm base; the inequalities are homogeneous under rescaling of the log base, exactly the invariance structure we formalize in Section 4.

[4] considers classical communication over a finite-dimensional quantum channel with memory using a separable-state input ensemble and local output measurements, and proposes algorithms for estimating and bounding the information rate of such setups, some based on so-called auxiliary channels, extending prior algorithms. The finite-dimensional quantum channel is the same algebraic object whose Hilbert-space dimension $\dim\mathcal{H}$ enters our definition of physical entropy; the supplied summary gives no further detail on the bounds' forms.

[5] describes the Gamma Ray Large Area Space Telescope (GLAST) Large Area Telescope (LAT), a pair-production high-energy ($>20$ MeV) gamma-ray telescope built by an international partnership for a satellite launch in 2006, and the collaboration's construction of a balloon flight engineering model. We cite it as an example of area entering physics as an operational, instrument-defined quantity ($A_{\text{eff}}$-style collecting area); the summary supplies no numerical effective area, so we draw no quantitative comparison.

[6] analyzes (mis)information operations: the massive diffusion of social media fosters disintermediation, changes how users are informed and engage in public debate, and the cognitive layer of users and related social dynamics define the nature and dimension of informational threats, with users tending to interact with information adhering to their preferred narrative. Its relevance is sociological contrast: "information" as threat vector is defined relative to human cognition, the extreme opposite of the observer-independent entropy we define below.

[7] investigates a multi-terminal source coding problem under logarithmic loss fidelity, which does not necessarily lead to an additive distortion measure, motivated by extending the Information Bottleneck method to a multi-source scenario where several encoders cooperatively build rate-limited descriptions to maximize information. Logarithmic loss is the unique common fidelity measure under which the relevant quantities are entropies in some base; the supplied summary does not state which base, which itself illustrates the base-convention arbitrariness we study.

[8] develops a theoretical framework for defining and identifying flows of information in computational systems, modeling a computational system as a directed graph with "clocked" nodes that send transmissions along edges at discrete times, seeking a definition capturing dynamic flow of information about a specific message. The summary is truncated; we use it only as evidence that information flow definitions are convention-laden even in classical computation.

[9] (QNFO: Ten-Fingered Trap) has an empty supplied summary; it gives no content we can use, and we cite it only to acknowledge the corpus from which this project arises.

[10] (QNFO: The Threshold of Meaning, DOI 10.5281/zenodo.19202950) likewise has an empty supplied summary; no statement about its content can be made here.

[11] (QNFO: Super-Universe, DOI 10.5281/zenodo.19347807) likewise has an empty supplied summary; no statement about its content can be made here.

[12] (QNFO: Non-Anthropocentric Natural Units: From the Bekenstein Bound to Ostrowski's Theorem, DOI 10.5281/zenodo.21480756) states that it strips away all anthropocentric constructions from the Bekenstein-Hawking entropy bound, treating area as a dimensionless geometric invariant, defining the exponential bound without logarithmic base, and taking the integer Hilbert-space dimension as a universal invariant; it further connects to Ostrowski's theorem, noting that the Archimedean completion is (summary truncated). This is the direct predecessor of the present paper; our contribution is to make the base-independence claim precise, to exhibit the bit as a derived quantity with explicit conversion factor, and to prove the no-distinguishing result of Section 4.

Notably absent from the supplied bibliography are the primary sources for the Bekenstein bound, Bekenstein-Hawking thermodynamics, and the covariant entropy bound; the research idea references them conceptually, but since we may cite only the supplied list, our statements about those bounds rest on the idea text and on [2] and [12], which explicitly invoke the holographic and Bekenstein-Hawking bounds.

## 3. Methods

### 3.1 Natural units and dimensionless area

Set $c = \hbar = G = k_B = 1$. The Planck length is $\ell_P = \sqrt{\hbar G / c^3}$, which in these units is $\ell_P = 1$. Any physical area $A_{\text{phys}}$ is then represented by the dimensionless number

$$a = \frac{A_{\text{phys}}}{\ell_P^2},$$

and the entropy bound on a region whose boundary has area $A_{\text{phys}}$ is stated as

$$S \le \frac{a}{4},$$

with $S$ dimensionless. No unit, base, or counting convention appears.

### 3.2 Physical entropy versus information

Define the physical entropy of a finite-dimensional system with Hilbert space $\mathcal{H}$, $\dim\mathcal{H} = d$, as

$$S_{\text{phys}} = \ln d.$$

This is the quantity that appears in thermodynamics and in the microstate counting underlying the Bekenstein-Hawking value. Define the *information representation* at base $b$ as

$$I_b = \frac{S_{\text{phys}}}{\ln b} = \log_b d.$$

The bit is the special case $b = 2$; the nat is $b = e$; the Hartley (decimal digit) is $b = 10$. The family $\{I_b\}$ is the complete set of base-dependent re-expressions of the single invariant $S_{\text{phys}}$.

### 3.3 Method of analysis

The method is purely deductive: (i) state the bound in invariant form; (ii) derive the base-dependent forms and their conversion constants; (iii) check whether any observable quantity can depend on the base (Section 4.4); (iv) compute worked numerical examples entirely within the dimensionless framework. We use no simulation and no empirical input beyond the structural assumptions stated above.

## 4. Analysis

### 4.1 Input numbers and their sources

The only numerical inputs are mathematical constants of the standard real functions, not empirical measurements:

- $\ln 2 = 0.693147\ldots$ (definition of the natural logarithm).
- $\ln 10 = 2.302585\ldots$ (definition of the natural logarithm).
- The structural constants $4$ (from the bound $S \le a/4$) and the exponents chosen for the worked examples.

All arithmetic below is shown step by step.

### 4.2 Derivation 1: the bit as a derived quantity

The horizon entropy in invariant form is $S = a/4$ nats. The bit count is

$$N_{\text{bit}} = \frac{S}{\ln 2} = \frac{a}{4\ln 2}.$$

Compute the conversion constant:

$$\frac{1}{\ln 2} = \frac{1}{0.693147} = 1.442695\ldots$$

Check: $1.442695 \times 0.693147 = 1.000000$ (to six decimals: $1.442695 \times 0.693147 \approx 1.000000$). Therefore

$$N_{\text{bit}} = 1.442695 \times \frac{a}{4} = 0.360674\,a,$$

since $1.442695/4 = 0.360674$ (check: $0.360674 \times 4 = 1.442696$, consistent to the displayed precision). So each Planck area unit $a = 1$ (i.e. $A_{\text{phys}} = \ell_P^2$) carries $S = 1/4 = 0.25$ nats $= 0.360674$ bits. The factor $0.360674$ is a pure unit conversion, exactly as $1\ \text{meter} = 100\ \text{cm}$; it encodes no physics.

### 4.3 Derivation 2: base-dependence of all representations

For any base $b > 1$,

$$I_b = \frac{S}{\ln b}.$$

Compute the conversion constants for the three common bases:

$$\frac{1}{\ln 2} = 1.442695, \qquad \frac{1}{\ln e} = 1, \qquad \frac{1}{\ln 10} = \frac{1}{2.302585} = 0.434294.$$

Check the last: $0.434294 \times 2.302585 = 0.999999\ldots \approx 1$ (this is the standard identity $\log_{10} e = 0.434294\ldots$). The ratios between representations are:

$$\frac{I_2}{I_{10}} = \frac{\ln 10}{\ln 2} = \frac{2.302585}{0.693147} = 3.321928,$$

which is $\log_2 10$ (check: $2^{3.321928} = 10$ by construction of the logarithm). Every member of the family is a fixed constant multiple of $S$; the family has one degree of freedom, and that degree of freedom is the convention.

### 4.4 Derivation 3: no observable distinguishes the representations

Any physical prediction of the theory is a statement of the form "the entropy of region $\mathcal{R}$ is at most $a/4$". Suppose an observable $O$ depended on the representation. Then $O$ would be a function $f(I_b)$ for some $b$. But $I_b = S/\ln b$, so

$$f(I_b) = f\!\left(\frac{S}{\ln b}\right) = g_b(S),$$

i.e. $O$ is a function of $S$ alone with a $b$-dependent rescaling absorbed into $g_b$. Since $S$ is the invariant, two observers using bases $b_1$ and $b_2$ compute observables related by

$$g_{b_2}(S) = g_{b_1}\!\left(\frac{\ln b_1}{\ln b_2}\, S\right),$$

and $\ln b_1 / \ln b_2$ is a known constant. Hence the representations are empirically equivalent at fixed theory content; the invariant formulation differs from the conventional one only in which representation is taken as primitive. This is the paper's central structural result, and it is a consistency theorem, not an experimental prediction.

### 4.4b Derivation 4: Hilbert-space dimension from the bound

Given the bound $S \le a/4$ and $S = \ln d$, the maximal Hilbert-space dimension saturating the bound is

$$d_{\max} = e^{a/4}.$$

For a worked example, take a region with $a = 10^{8}$ Planck areas (the number is chosen for illustration; nothing empirical is claimed about such a region). Then

$$\ln d_{\max} = \frac{10^{8}}{4} = 2.5 \times 10^{7} \text{ nats}.$$

In decimal digits:

$$\log_{10} d_{\max} = \frac{2.5 \times 10^{7}}{\ln 10} = \frac{2.5 \times 10^{7}}{2.302585} = 1.0857 \times 10^{7}.$$

Arithmetic: $2.5/2.302585 = 1.085736\ldots$ (check: $1.085736 \times 2.302585 = 2.500000$). In bits:

$$N_{\text{bit}} = \frac{2.5 \times 10^{7}}{0.693147} = 3.6067 \times 10^{7} \text{ bits}.$$

Arithmetic: $2.5/0.693147 = 3.606738\ldots$ (check: $3.606738 \times 0.693147 = 2.500000$). Note the consistency relation $N_{\text{bit}} = \log_2 10 \times \log_{10} d_{\max} = 3.321928 \times 1.085736 \times 10^{7} = 3.6067 \times 10^{7}$, agreeing with the direct computation.

### 4.5 Derivation 5: the Bekenstein bound in invariant form

The Bekenstein bound constrains entropy of energy $E$ confined to radius $R$; in conventional units it is written $S \le 2\pi E R / (\hbar c)$ (in nats, per the idea text's framing of the Bekenstein-Hawking anchoring). In Planck units $E$ is measured in Planck energies $E_P = \sqrt{\hbar c^5/G}$ and $R$ in Planck lengths, so

$$S \le 2\pi\, \epsilon\, \rho,$$

where $\epsilon = E/E_P$ and $\rho = R/\ell_P$ are dimensionless. No base, no $\hbar$, no $k_B$ appears. The bound is a relation among three dimensionless numbers, which is the sense in which it is convention-free. The covariant (holographic) version replaces $(E, R)$ by the boundary area $a$, giving $S \le a/4$ as above; the idea text anchors both in black hole thermodynamics, and [2] and [12] both treat the holographic bound as a physical capacity constraint, consistent with this reading.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

**R1 (conversion constants).** The bit-to-nat conversion is $1/\ln 2 = 1.442695$; the digit-to-nat conversion is $1/\ln 10 = 0.434294$; the bit-to-digit ratio is $\log_2 10 = 3.321928$. These are exact mathematical constants to the displayed precision.

**R2 (entropy per Planck area).** One Planck area ($a = 1$) corresponds to a maximum entropy of $S = 0.25$ nats $= 0.360674$ bits $= 0.108574$ decimal digits (computed as $0.25 \times 0.434294 = 0.108574$; check: $0.108574/0.434294 = 0.250000$).

**R3 (worked example, labeled illustrative).** For a hypothetical region with $a = 10^{8}$: $S_{\max} = 2.5 \times 10^{7}$ nats, $d_{\max} = e^{2.5\times 10^{7}}$, $\log_{10} d_{\max} = 1.0857 \times 10^{7}$, $N_{\text{bit}} = 3.6067 \times 10^{7}$ bits. This is a mathematical illustration of the formalism, not a claim about any physical region.

**R4 (structural result).** All base-$b$ information representations of a given entropy are related by known constant factors (Section 4.4); consequently, no observable at fixed theory content distinguishes the invariant (nat/area) formulation from the conventional (bit) formulation. The choice of primitive representation is methodological.

**R5 (projection, with assumptions).** If a physical region has boundary area $A_{\text{phys}}$, its bit capacity under the bound is projected as $N_{\text{bit}} = 0.360674 \times A_{\text{phys}}/\ell_P^2$, with uncertainty dominated entirely by the unknown physical applicability of the bound at sub-Planckian or non-saturating regimes; the arithmetic conversion itself is exact. No specific $A_{\text{phys}}$ is asserted.

## 6. Discussion

**Limitations.** First, the reformulation is representational. By R4, it makes no new predictions; a skeptic can correctly say that writing $S \le a/4$ instead of $N_{\text{bit}} \le a/(4\ln 2)$ changes nothing operational. Our defense is that foundational clarity has value independent of new predictions, but we concede the result is weaker than "area and bit are universal invariants" might suggest: the bit is *not* an invariant under our proposal—it is explicitly demoted to a derived unit—so the paper's real claim is that only $\{a, S, d\}$ are candidate invariants, and the bit is not among them.

**Failure modes.** The invariant formulation fails if any of the following hold. (i) If the microscopic states of a holographic cell are not countable by a finite integer $d$—e.g., if the relevant Hilbert space is infinite-dimensional or the entropy is not $\ln d$ of any finite system—then $S = \ln d$ is undefined and the "integer Hilbert-space dimension as universal invariant" premise collapses. (ii) If the coefficient $1/4$ in $S \le a/4$ is itself convention-dependent (it is not, being fixed by the Bekenstein-Hawking value in nats, but a derivation from first principles is outside this paper's scope and outside the supplied literature), the bound's convention-freedom would be incomplete. (iii) If future theory replaces the area law with a different geometric functional, the identification of "area" as the primitive invariant fails.

**What would falsify the claims.** R4 is falsified by exhibiting a well-defined observable whose value depends on the logarithm base used in the bookkeeping while all invariant quantities ($a$, $S$, $d$) are held fixed; we know of no candidate, but the burden is on us to state the condition. The foundational claim—that the nat/area formulation is *preferable*—is not empirically falsifiable at all; it is a methodological thesis, and could only be undermined by showing that some deep structure (e.g., information-theoretic inequalities of the kind studied in [3] and [7]) singles out base 2 intrinsically. The supplied summaries of [3] and [7] do not state any such base preference, so no support for base-2 primacy exists in the cited corpus.

**Open questions.** (1) Does the covariant entropy bound admit a formulation in which even the coefficient $1/4$ is derived rather than inserted? (2) The predecessor work [12] connects the program to Ostrowski's theorem and the Archimedean completion of the rationals; its supplied summary is truncated mid-sentence, so we cannot assess that connection here, and integrating it is open. (3) Whether the finite-storage premise used in [2]—that the observable universe's information capacity is finite—can be stated without any base convention in cosmological settings. (4) Whether quantum channel information rates as bounded in [4] for finite-dimensional memory channels admit the same nat-only restatement; the summary of [4] does not state the form of its bounds, so this is unresolved from the supplied material.

**Arguing against ourselves.** The strongest objection is that "anthropocentric" is a red herring: the natural logarithm is no more observer-independent than base 2; both are human mathematical constructs, and the true invariant is the *pair* $(S, \text{base})$ up to rescaling. Our reply is that invariance here means invariance under the specific group of base rescalings exhibited in Section 4.3, and the nat is the canonical representative of the orbit only because the exponential map $d \mapsto e^{S}$ is the identity-structured choice; we do not claim $e$ is metaphysically privileged, only that fixing one representative and deriving the rest makes the convention explicit. A second objection: the bibliography contains no primary holography sources, so the paper's grounding in Bekenstein-Hawking physics rests on the idea text and on [2] and [12]; this is a genuine weakness of the supplied corpus, acknowledged rather than hidden.

## 7. Conclusion

Within the Bekenstein-holographic framework, the entropy bound can be written as $S \le a/4$ with $a$ a dimensionless area in Planck units and $S = \ln d$ the physical entropy of a finite Hilbert space of integer dimension $d$. In this form the bound contains no logarithm base and no counting convention; the bit is recovered as the derived quantity $S/\ln 2$ with conversion factor $1.442695$, and every other base-dependent representation is a fixed constant multiple of the same invariant. We proved that no observable at fixed theory content distinguishes the invariant formulation from the conventional bit-based one, so the contribution is foundational and methodological: it identifies exactly which quantities in holographic bounds are candidate universal invariants ($a$, $S$, $d$) and which are conventions (the base, hence the bit). Future work must derive the coefficient $1/4$ internally, integrate the Ostrowski-theoretic program of [12], and test whether the finite-dimensional premise survives in quantum-gravitational settings where Hilbert spaces may fail to be finite.

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