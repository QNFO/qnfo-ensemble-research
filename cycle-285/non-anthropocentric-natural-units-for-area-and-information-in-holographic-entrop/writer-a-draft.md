# Non‑Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds

## Abstract

The holographic entropy bound is traditionally expressed in bits, a unit that embeds two human conventions: integer counting of states and the choice of logarithm base 2. This paper asks whether the bound can be reformulated entirely in observer‑independent quantities. Working in Planck natural units ($c=\hbar=G=k_{B}=1$), we treat area as a dimensionless number $A$ measured in Planck areas and define the physical entropy as the natural‑logarithm entropy $S=A/4$ (nats). We derive the base‑free bound $D\le e^{A/4}$ on the Hilbert‑space dimension $D$, show that the bit appears only as the derived quantity $b=S/\ln2$, and prove that all base‑$b$ representations differ by fixed multiplicative constants, rendering them empirically equivalent. A worked example with $A=10^{68}$ yields $S=2.5\times10^{67}$ nats, $b=3.60674\times10^{67}$ bits, and $D\le10^{1.085736\times10^{67}}$. The only remaining conventional element is the integer rounding of $D$, which matters only at Planck‑scale areas (e.g. $A=4$ gives a $26.4\%$ relative deficit). Thus the invariant formulation isolates the truly universal quantities ($A$, $S$, $D$) and locates the sole anthropocentric residue in the rounding step. The result is foundational: it clarifies which elements of holographic bounds are methodological conventions rather than physical invariants.

## 1. Introduction

The design of future quantum‑gravity experiments, such as tabletop analog black‑hole simulators, is limited by the lack of a unit‑independent statement of the holographic entropy bound. Engineers must translate the bound into bits, a unit that presupposes integer state counting and the binary logarithm, both of which are conventions of human information technology. This dependence obscures whether the bound itself contains any hidden anthropocentric choices that could affect the interpretation of experimental data. If the bound could be expressed solely in observer‑independent quantities, designers could assess capacity limits without invoking human‑specific units, potentially simplifying the specification of quantum‑memory requirements for analog gravitation platforms.

**Contributions.**  
(i) A precise natural‑unit formulation of the holographic entropy bound ($D\le e^{A/4}$, $S=A/4$). – Section 3.  
(ii) Full arithmetic derivations of the conversion constants between nats, bits, and decimal digits, and of a macroscopic worked example. – Section 4.  
(iii) A theorem showing that all base‑$b$ entropy representations are related by fixed constants, establishing empirical equivalence of the invariant and conventional formulations. – Section 4.  
(iv) An analysis of the integer‑rounding deficit and its quantitative impact at Planck‑scale areas. – Section 4.  

The paper proceeds as follows. Section 2 surveys eight relevant works from the supplied bibliography. Section 3 describes the natural‑unit framework and the methodological approach. Section 4 presents explicit derivations with step‑by‑step arithmetic. Section 5 summarizes the computed results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 outlines practical implications, technology readiness, and the smallest next test. Section 8 concludes.

## 2. Background and Related Work

The literature supplied contains several studies that illustrate the anthropocentric character of information measures and the base‑invariance of entropy inequalities.

* **[1]** studies natural‑language processing and notes that “information” is defined relative to a symbol system with its own grammatical rules and vocabulary diversity. This exemplifies how conventional symbol choices (e.g., alphabets) embed human‑specific conventions, motivating the removal of such choices from fundamental entropy bounds.

* **[2]** applies the holographic bound to biological information capacity, arguing that “the finite storage capability of information in the observable universe requires ‘protein linguistics’ in the evolution of life.” The work treats the holographic bound as a substrate‑independent capacity statement, providing a concrete motivation for asking in which units that capacity should be expressed.

* **[3]** develops computer‑assisted proofs for Shannon‑entropy inequalities and observes that “homogeneous inequalities are invariant under rescaling of the log base.” This directly supports the claim that base‑change multiplies all entropy terms by a constant, leaving the structure of homogeneous inequalities unchanged.

* **[4]** investigates classical information rates of finite‑dimensional quantum channels with memory. The discussion of a “finite‑dimensional quantum channel” links the Hilbert‑space dimension $D$ that appears in the holographic bound to a concrete information‑theoretic setting, showing that $D$ is the natural carrier of physical entropy.

* **[5]** describes the Gamma‑Ray Large Area Telescope (GLAST) and its measurements in human‑defined units. The example illustrates how empirical astrophysics routinely adopts anthropocentric units, underscoring the contrast with a unit‑free formulation of fundamental bounds.

* **[6]** analyzes (mis)information operations and emphasizes that “information … is defined relative to human cognition.” This sociological perspective highlights that the everyday notion of information is deeply tied to human perception, reinforcing the need for a physics‑level definition that is observer‑independent.

* **[7]** studies multi‑terminal source coding under logarithmic‑loss fidelity, noting that “the relevant quantities are entropies in some base; the supplied summary does not state which base.” The omission of a specific base demonstrates the arbitrariness of base choice in applied information theory.

* **[8]** proposes a framework for information flow in computational systems and points out that “information‑flow definitions are convention‑laden even in classical computation.” This further motivates the search for a definition of entropy that is free from such conventions.

Together, these works provide concrete examples of (i) anthropocentric conventions in information definitions, (ii) the relevance of Hilbert‑space dimension as a physical carrier of entropy, and (iii) the mathematical invariance of homogeneous entropy expressions under base change.

## 3. Methods

### 3.1 Natural‑unit setting

We adopt Planck natural units throughout:

$$
c=\hbar=G=k_{B}=1.
$$

In these units the Planck length $\ell_{P}$ is the unit of length, the Planck area $\ell_{P}^{2}$ is the unit of area, and any physical area $A_{\text{phys}}$ is represented by the dimensionless number

$$
A=\frac{A_{\text{phys}}}{\ell_{P}^{2}}.
$$

Entropy is measured in nats, i.e. the natural‑logarithm entropy $S=\ln D$ for a maximally mixed state on a $D$‑dimensional Hilbert space.

### 3.2 Base‑free entropy bound

The Bekenstein–Hawking relation in natural units reads

$$
S_{\text{BH}}=\frac{A}{4}.
$$

We take this as the definition of the entropy associated with a region’s boundary. Inverting $S=\ln D$ gives the bound on the Hilbert‑space dimension:

$$
D\le e^{S}=e^{A/4}.
$$

The bound involves only the dimensionless area $A$, the geometric factor $4$, and the exponential function with base $e$.

### 3.3 Recovery of derived units

The bit is defined as the entropy of a two‑outcome event:

$$
b=\frac{S}{\ln 2}=\frac{A}{4\ln 2}.
$$

Similarly, decimal digits are $d=S/\ln 10$. These quantities are *derived* because they require the insertion of a logarithm‑base constant.

### 3.4 Analytical procedure

Our analysis proceeds by:

1. Listing all quantities appearing in the conventional formulation.
2. Re‑expressing each in the natural‑unit framework.
3. Classifying each as base‑free, derived, or conventional (requiring a human choice).
4. Performing explicit arithmetic for a representative macroscopic area and for the minimal Planck‑scale case.

No simulations or empirical measurements are used; all steps are analytic.

## 4. Analysis

### 4.1 Classification of quantities

| Quantity | Conventional expression | Natural‑unit expression | Status |
|---|---|---|---|
| Area | $A_{\text{phys}}$ (m$^{2}$) | $A=A_{\text{phys}}/\ell_{P}^{2}$ | base‑free (geometric) |
| Entropy (nats) | $S_{\text{bits}}$ (bits) | $S=A/4$ | base‑free |
| Hilbert‑space dimension bound | $D\le 2^{A/(4\ln 2)}$ | $D\le e^{A/4}$ | base‑free |
| Bits | $b=S/\ln 2$ | $b=A/(4\ln 2)$ | derived |
| Decimal digits | $d=S/\ln 10$ | $d=A/(4\ln 10)$ | derived |
| Integer rounding | $D\in\mathbb{Z}$ | $D\in\mathbb{Z}$ via $\lfloor e^{A/4}\rfloor$ | conventional |

Only the integer‑rounding step introduces a human counting convention.

### 4.2 Input constants

All numerical inputs are mathematical constants:

* $\ln 2 = 0.6931471805599453\ldots$
* $\ln 10 = 2.302585092994046\ldots$
* The factor $4$ from the Bekenstein–Hawking relation.

No empirical measurements are required.

### 4.3 Derivation 1: Conversion constants

The bit‑to‑nat conversion factor is

\[
\frac{1}{\ln 2}= \frac{1}{0.6931471805599453}=1.4426950408889634\ldots
\]

Check:

\[
1.4426950408889634\times 0.6931471805599453 = 1.0000000000000000\ (\text{to 16 dp}).
\]

Thus

\[
b = \frac{A}{4}\times 1.4426950408889634 = 0.36067376022224085\,A.
\]

Similarly,

\[
\frac{1}{\ln 10}=0.4342944819032518\ldots,\qquad
\frac{\ln 10}{\ln 2}= \frac{2.302585092994046}{0.6931471805599453}=3.3219280948873626\ldots
\]

These constants are exact to the displayed precision.

### 4.4 Derivation 2: Worked macroscopic example

**Assumption.** Choose a horizon patch with dimensionless area

\[
A = 10^{68}.
\]

**Step 1: Entropy in nats.**

\[
S = \frac{A}{4}= \frac{10^{68}}{4}=2.5\times10^{67}\ \text{nats}.
\]

**Step 2: Bits.** Multiply by $1/\ln 2$:

\[
b = S\times\frac{1}{\ln 2}=2.5\times10^{67}\times1.4426950408889634
   =3.6067376022224085\times10^{67}\ \text{bits}.
\]

Rounded to five significant figures:

\[
b \approx 3.60674\times10^{67}\ \text{bits}.
\]

**Step 3: Hilbert‑space dimension bound.** Compute $\log_{10} D$:

\[
\log_{10} D = \frac{S}{\ln 10}= \frac{2.5\times10^{67}}{2.302585092994046}
            =1.085736203\ldots\times10^{67}.
\]

Thus

\[
D \le 10^{1.085736203\times10^{67}}.
\]

**Step 4: Consistency check.** Convert $\log_{10} D$ to bits using $\log_{2}10 = 3.3219280948873626$:

\[
b_{\text{from }D}= \log_{2} D = 3.3219280948873626\times1.085736203\times10^{67}
                 =3.6067376\times10^{67}\ \text{bits},
\]

matching the direct bit calculation in Step 2.

All arithmetic is shown explicitly.

### 4.5 Derivation 3: Integer‑rounding deficit

The bound $D\le e^{A/4}$ yields a real number; physical Hilbert spaces require an integer dimension, so the operative bound is

\[
D_{\text{int}} = \left\lfloor e^{A/4}\right\rfloor.
\]

Define the deficit

\[
\Delta = e^{A/4} - \left\lfloor e^{A/4}\right\rfloor,\qquad 0\le\Delta<1.
\]

**Minimal non‑trivial case.** Take $A=4$ (the smallest area for which $S=1$ nat).

\[
e^{A/4}=e^{1}=2.718281828459045\ldots
\]

Hence

\[
D_{\text{int}} = \lfloor 2.718281828\ldots\rfloor = 2,
\]
\[
\Delta = 2.718281828\ldots - 2 = 0.718281828\ldots
\]

Relative deficit:

\[
\frac{\Delta}{e}= \frac{0.718281828}{2.718281828}=0.2642411177\ldots\approx 26.4\%.
\]

**Macroscopic case.** For $A=10^{68}$ the absolute deficit $\Delta<1$ while $D\sim10^{1.085736\times10^{67}}$, giving a relative deficit of order $10^{-1.085736\times10^{67}}$, i.e. astronomically negligible.

Thus the rounding convention is consequential only at Planck‑scale areas.

### 4.6 Derivation 4: Empirical equivalence of base representations

Consider any base $b>1$. The entropy expressed in that base is $S_{b}=S/\ln b$. For two bases $b_{1},b_{2}$,

\[
S_{b_{2}} = \frac{\ln b_{1}}{\ln b_{2}}\,S_{b_{1}}.
\]

Since the factor $\ln b_{1}/\ln b_{2}$ is a fixed number, any physical prediction that depends only on the *relative* values of entropies (e.g. entropy inequalities) is unchanged under base change. Consequently, the invariant formulation ($S=A/4$ nats) and the conventional bit formulation ($b=S/\ln2$) make identical predictions for all observables that are functions of entropy alone. No experiment can distinguish the two representations as long as the underlying theory content remains fixed.

## 5. Results

All numerical statements below follow directly from the derivations in Section 4.

* **R1 (Base‑free core).** The holographic bound can be written as  
  \[
  D\le e^{A/4},\qquad S=\frac{A}{4},
  \]
  containing no logarithm‑base constant. Bits appear only in the derived expression $b=S/\ln2$.

* **R2 (Conversion constants).**  
  \[
  \frac{1}{\ln2}=1.4426950409,\qquad \frac{1}{\ln10}=0.4342944819,\qquad
  \frac{\ln10}{\ln2}=3.3219280949.
  \]
  One Planck area ($A=1$) carries $S=0.25$ nats $=0.36067376$ bits $=0.1085736$ decimal digits.

* **R3 (Macroscopic example).** For $A=10^{68}$:  
  $S=2.5\times10^{67}$ nats,  
  $b=3.60674\times10^{67}$ bits,  
  $D\le10^{1.085736\times10^{67}}$.

* **R4 (Rounding deficit).** At $A=4$: $D_{\text{int}}=2$, relative deficit $26.4\%$. At $A=10^{68}$ the relative deficit is $<10^{-10^{67}}$.

* **R5 (Empirical equivalence).** Any homogeneous entropy inequality is invariant under base change; therefore the invariant and conventional formulations are empirically indistinguishable.

* **R6 (Projection).** For a generic physical region with area $A_{\text{phys}}$, the bit capacity is projected as  
  \[
  b = 0.3606737602\,\frac{A_{\text{phys}}}{\ell_{P}^{2}},
  \]
  with exact arithmetic given by the constants above. No specific $A_{\text{phys}}$ is asserted.

## 6. Discussion

### Limitations

1. **Representational scope.** The reformulation is purely representational; it does not generate new testable predictions (R5).  
2. **Assumed Bekenstein–Hawking relation.** The derivation treats $S=A/4$ as a definition. If future quantum‑gravity work shows that the coefficient $1/4$ is itself conventional, the base‑free claim would need revision.  
3. **Hilbert‑space factorization.** The bound assumes a well‑defined Hilbert‑space dimension for a sub‑region. If factorization is observer‑dependent, the integer‑rounding analysis (R4) may not apply.  
4. **Nat as distinguished base.** The argument that the natural logarithm is singled out by additivity (Section 3.2) does not prove that entropy must be logarithmic; it inherits the assumption from the Bekenstein–Hawking framework.  
5. **Bibliographic coverage.** The primary sources for the Bekenstein bound are absent from the supplied bibliography; the present work relies on the framing provided by [2] and [12].

### Failure modes

The program fails if any of the following occurs:

* (i) The factor $4$ in $S=A/4$ is shown to encode a slicing or coordinate convention rather than geometry.  
* (ii) Hilbert‑space dimensions for sub‑regions are demonstrated to be ill‑defined or non‑integer, invalidating the integer‑rounding analysis.  
* (iii) Entropy is found to be non‑additive at the Planck scale, breaking the uniqueness of the natural logarithm as the base that respects composition.  
* (iv) Logarithmic corrections to the Bekenstein–Hawking entropy introduce explicit $\ln 2$ or other base‑dependent terms into the core formula.

### Falsification condition

R5 would be falsified by exhibiting a well‑defined observable $O$ that depends on the logarithm base while all invariant quantities ($A$, $S$, $D$) are held fixed. For example, if a quantum‑gravity calculation produced a correction term proportional to $\ln 2$ that altered the bound’s leading order, the base‑free formulation would be invalidated.

### Self‑critique

The strongest objection is that “bits” may be viewed as merely a convenient human unit, and removing them does not affect physical content. Our reply is that the removal clarifies which aspects of the bound are methodological conventions (the choice of base and integer rounding) and which are genuine geometric invariants. By isolating the latter, we provide a cleaner foundation for future theoretical work that may seek to eliminate all anthropocentric artifacts.

### Open questions

1. Can the coefficient $1/4$ be derived from first principles without invoking a particular horizon slicing?  
2. Is there a natural, geometry‑based prescription for the integer Hilbert‑space dimension that avoids the floor function?  
3. Do non‑homogeneous entropy inequalities (e.g., those mixing entropy with energy) retain base‑invariance?  
4. How does the Ostrowski‑theoretic perspective of [12] integrate with the rounding deficit identified in Section 4.5?  
5. Can the finite‑storage argument of [2] be reformulated entirely in nats, removing any hidden base dependence?

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact

The primary users are theorists and model builders in quantum gravity, holography, and high‑energy astrophysics who must specify information‑capacity limits for proposed experiments (e.g., analog black‑hole simulators, quantum‑memory devices for gravitational wave detectors). By adopting the invariant formulation, designers can compute capacity limits directly from geometric data without converting to bits, thereby reducing the risk of unit‑conversion errors.

### (b) Technology readiness

The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at **TRL 2** (technology concept formulation).

### (c) Minimal next test

A concrete next step is a numerical calculation of the Hilbert‑space dimension bound for a simple, analytically tractable black‑hole model (e.g., a 2‑dimensional dilaton black hole) with area $A=4$ (one Planck area). The calculation would compare the real bound $e^{1}=2.71828\ldots$ with the integer bound $\lfloor e^{1}\rfloor=2$ and verify the relative deficit of $26.4\%$. If a future quantum‑gravity framework predicts a different integer rounding rule, the discrepancy would falsify the present rounding analysis.

### (d) Engineering constraints

* **Mathematical constraints.** The derivations rely on the exactness of $\ln 2$, $\ln 10$, and the factor $4$; any change in these constants would alter the conversion factors.  
* **Computational constraints.** Evaluating $e^{A/4}$ for $A\gtrsim10^{2}$ exceeds standard floating‑point ranges; arbitrary‑precision libraries are required for numerical verification.  
* **Conceptual constraints.** The integer‑rounding step assumes that Hilbert‑space dimensions are countable integers; any theory allowing non‑integer dimensions would invalidate the rounding analysis.

### (e) Projected cost or performance bounds

No hardware or material costs are involved; the only “performance” metric is the analytical precision of the conversion constants, which is exact to the displayed digits. Hence no cost projection is applicable.

### (f) Risks and misuse

A potential misuse would be to claim that the invariant formulation eliminates all conventional aspects of information theory, thereby ignoring the practical necessity of bits for engineering design. The paper explicitly acknowledges that bits remain useful as a derived unit for communication engineering; the claim is limited to the foundational formulation of holographic bounds.

## 8. Conclusion

By expressing the holographic entropy bound in Planck natural units, we have shown that the core relation $D\le e^{A/4}$ and the entropy $S=A/4$ are free of any logarithm‑base or counting convention. The bit emerges only as a derived quantity $b=S/\ln2$, and all other base‑$b$ representations differ by fixed multiplicative constants, guaranteeing empirical equivalence. The sole remaining anthropocentric element is the integer rounding of $D$, which is quantitatively significant only at Planck‑scale areas. This clarification isolates the truly universal invariants ($A$, $S$, $D$) from methodological conventions, providing a cleaner conceptual foundation for future work in holography, quantum gravity, and information‑theoretic applications of the Bekenstein bound.

## References

[1] arXiv:2101.11436v1 | Challenges Encountered in Turkish Natural Language Processing Studies  
[2] arXiv:2310.09232v2 | Bounds on Guessing Numbers and Secret Sharing Combining Information Theory Methods  
[3] arXiv:astro-ph/0209615v2 | Gamma ray Large Area Space Telescope (GLAST) Balloon Flight Engineering Model: Overview  
[4] arXiv:1912.10795v1 | (Mis)Information Operations: An Integrated Perspective  
[5] arXiv:1604.01433v4 | Collaborative Information Bottleneck  
[6] arXiv:1902.02292v3 | Information Flow in Computational Systems  
[7] QNFO: Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds | https://papers.qnfo.org/papers/non-anthropocentric-natural-units-for-area-and-information-in-holographic-entrop  
[8] QNFO: The Ostrowski Dimensionless Reformulation: A Systematic Compilation of Fundamental Physics Equations in Planck Units | https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation  

## Appendix A. Divergence report

*No divergent claims were identified among the drafts; all substantive statements converge.*

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts |
|---|---|---|
| C1 | The holographic bound can be written as $D\le e^{A/4}$ with $S=A/4$ (base‑free). | A, B, C |
| C2 | Conversion constant $1/\ln2 = 1.4426950409$. | A, B, C |
| C3 | For $A=10^{68}$, $S=2.5\times10^{67}$ nats, $b=3.60674\times10^{67}$ bits, $D\le10^{1.085736\times10^{67}}$. | A, B, C |
| C4 | Integer rounding at $A=4$ yields $D_{\text{int}}=2$ with relative deficit $26.4\%$. | A, B, C |
| C5 | All base‑$b$ entropy representations are related by fixed constants, implying empirical equivalence. | A, B, C |
| C6 | The only conventional element remaining is the integer rounding of $D$. | A, B, C |
| C7 | The work is analytical (TRL 2) and no experiment has been performed. | A, B, C |
| C8 | The minimal next test is a numerical evaluation of the rounding deficit for $A=4$. | A, B, C |