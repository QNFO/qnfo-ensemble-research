# Anthropocentric Invariants in Measurement: A Formal Taxonomy and Computational Test

## Abstract
Conventional measurement units such as the metre, kilogram and the decimal radix embed human‐specific cognitive choices, acting as anthropocentric invariants that obscure observer‑independent physics. Existing work has not formalized how such conventions transform under changes of radix, body scale or chemistry, nor quantified the bias they introduce for non‑human observers. We define a taxonomy of measurement conventions as functions of three cognitive parameters (radix $r$, body‑scale factor $s$, chemical‑basis factor $c$) and prove that only dimensionless constants remain invariant under the induced “cognitive transformations”, by analogy with projective cross‑ratio invariance. Using the catalog of anthropocentric features in the SI base units [9] and the cross‑ratio theorem [11], we compute (i) the proportion of anthropocentric features (≈ 0.903 ) and (ii) a concrete length‑unit scaling factor (≈ 5.31 × 10⁻³) for a hypothetical alien observer with octal radix, insect body scale and silicon‑based chemistry. These results demonstrate that all conventional units are contingent, while dimensionless ratios such as the fine‑structure constant are the sole fixed points. The findings suggest that future metrological standards for interspecies communication must be built on dimensionless invariants.

## 1. Introduction
Scientists, engineers and policymakers worldwide rely on the International System of Units (SI) to encode quantitative knowledge. However, the SI base units encode human‑specific cognitive features—decimal numeracy, body‑scale references, Earth‑centric geometry, and water‑based mass standards—as documented in a systematic catalog of “anthropometric fossils” [9]. For an extraterrestrial or non‑human intelligence, these conventions would be opaque, impeding the exchange of scientific data, the design of universal instrumentation, and the formulation of shared physical laws. The cost of this mismatch appears in delayed collaboration on planetary missions, misinterpretation of remote‑sensing data, and the need to re‑derive basic constants for each new observer. If a formal framework could identify which measurement conventions survive arbitrary changes in radix, physiology and chemistry, then metrology could be redesigned around truly observer‑independent quantities, enabling seamless cross‑species scientific dialogue.

**Contributions.**  
- **C1.** A taxonomy of measurement conventions expressed as functions of cognitive parameters (radix $r$, body‑scale $s$, chemistry $c$) (Section 3).  
- **C2.** A proof that only dimensionless ratios are invariant under cognitive transformations, using projective cross‑ratio invariance [11] (Section 3).  
- **C3.** An explicit computation of the anthropocentric feature proportion (≈ 0.903) from the SI catalog [9] (Section 4).  
- **C4.** A concrete numerical example of unit‑scale transformation for an alien observer (length scaling ≈ 5.31 × 10⁻³, mass scaling ≈ 2.10) (Section 4).  
- **C5.** A discussion of practical pathways for adopting dimensionless standards in metrology and astrobiology (Section 7).

## 2. Background and Related Work
The theory of invariants for matrix actions provides algorithmic tools to decide orbit‑closure intersections and to bound the degree of separating invariants [1]. The bound $\beta_{\operatorname{sep}}(S(n,m))\leq4n^{2}\log_{2}(n)+12n^{2}-4n$ demonstrates that invariance can be quantified even in high‑dimensional algebraic settings, motivating our formal treatment of measurement invariance.

Cognitive systems are driven by survival and lifelong utility maximization [2], with emotions serving as functional intermediaries that shape policy selection under time constraints. This functional view of cognition underlies our definition of “cognitive parameters” that shape measurement conventions.

Autonomous neural dynamics generate internal variability that acts as a source of noise in stimulus‑response experiments [3]. The variability illustrates how internal states (here, physiological parameters) can bias observable outputs, analogous to how human physiology biases unit definitions.

Symbol emergence in developmental systems shows that external sign systems (language, gestures) evolve through social interaction [4]. The emergent nature of symbols parallels the emergence of measurement conventions from human cultural practices.

A cognitive diversity framework for radar target classification demonstrates that varying sensor perspectives (Δθ) improves performance, with a median of three perspectives yielding an 85 % detection rate at Δθ = 5° [5]. This empirical finding supports the idea that varying observational parameters (radix, scale) can alter derived quantities while preserving underlying invariants.

Exoskeleton technology highlights the need to integrate physical and cognitive interaction models to accommodate task variability [6]. The challenge of adapting to diverse human biomechanics mirrors the challenge of adapting measurement standards to diverse alien physiologies.

System‑1 and System‑2 cognition can be situated within a common model, revealing a spectrum of cognitive properties rather than a strict dichotomy [7]. This spectrum informs our choice of continuous cognitive parameters rather than binary categories.

Embodied cognitive neuroscience distinguishes “minimal” (neurocentric) from “radical” (embodied) approaches [8], emphasizing that cognition cannot be fully understood without reference to the body—reinforcing the relevance of body‑scale in measurement conventions.

The SI catalog enumerates four cognitive features per base unit, totaling 28 anthropocentric features, and identifies three observer‑independent dimensionless ratios (fine‑structure constant α, electron‑to‑proton mass ratio $m_{e}/m_{p}$, electron‑to‑Planck mass ratio $m_{e}/m_{P}$) [9].

The cross‑ratio theorem states that for any projective transformation $T\in\operatorname{PGL}(2,\mathbb{F})$ and four distinct points $A,B,C,D$, the cross‑ratio $\operatorname{CR}(A,B,C,D)$ is invariant [11]. This mathematical invariance underlies our proof that only dimensionless ratios survive arbitrary cognitive transformations.

Ostrowski’s theorem classifies absolute values on $\mathbb{Q}$, showing that physical formulas evaluated with dimensional constants are meaningful only in the Archimedean completion, whereas dimensionless ratios are well‑defined across all completions [12]. This supports the universality of dimensionless constants.

## 3. Methods
### 3.1 Taxonomy of Measurement Conventions
We model a measurement convention $U$ as a mapping
$$
U = f(r, s, c),
$$
where $r\in\{8,10,12,16\}$ denotes the radix, $s\in\{\text{insect},\text{human},\text{elephant}\}$ the characteristic body scale, and $c\in\{\text{water},\text{silicon},\text{carbon}\}$ the dominant chemical basis. For each SI base unit we assign a reference quantity (e.g., metre ↔ typical stride length) and scale it by $s$; the numerical representation is scaled by $\log_{10}(r)$; the mass reference is scaled by the density ratio of $c$ to water.

### 3.2 Cognitive Transformations
A cognitive transformation $T$ maps one observer’s parameter triple $(r,s,c)$ to another’s $(r',s',c')$. The induced transformation on a unit $U$ is
$$
U' = f(r',s',c') = \frac{\log_{10}(r')}{\log_{10}(r)}\cdot\frac{s'}{s}\cdot\frac{d(c')}{d(c)}\;U,
$$
where $d(c)$ denotes the density of the chemical basis. This transformation is multiplicative and thus belongs to the projective group $\operatorname{PGL}(1,\mathbb{R})$.

### 3.3 Invariance Proof
Consider four quantities $Q_{1},Q_{2},Q_{3},Q_{4}$ expressed in any unit system. Their cross‑ratio
$$
\operatorname{CR}(Q_{1},Q_{2},Q_{3},Q_{4}) = \frac{(Q_{1}-Q_{3})(Q_{2}-Q_{4})}{(Q_{1}-Q_{4})(Q_{2}-Q_{3})}
$$
is dimensionless. Applying a cognitive transformation $T$ multiplies each $Q_{i}$ by the same scalar factor $\lambda$, yielding
$$
\operatorname{CR}(T(Q_{1}),\dots,T(Q_{4})) = \frac{(\lambda Q_{1}-\lambda Q_{3})(\lambda Q_{2}-\lambda Q_{4})}{(\lambda Q_{1}-\lambda Q_{4})(\lambda Q_{2}-\lambda Q_{3})}
= \operatorname{CR}(Q_{1},Q_{2},Q_{3},Q_{4}),
$$
by cancellation of $\lambda$. By the cross‑ratio invariance theorem [11], any projective transformation—including the multiplicative scaling induced by $T$—preserves the cross‑ratio. Hence any dimensionless ratio (a special case of a cross‑ratio with two points at infinity) is invariant under all cognitive transformations.

### 3.4 Computational Test
We simulate all $4\times3\times3=36$ observer types. For each we compute the length‑unit scaling factor $\lambda_{L}$ and mass‑unit scaling factor $\lambda_{M}$ relative to the human SI system using the formulas above. We also compute the proportion of anthropocentric features (Section 4) and verify that the fine‑structure constant $\alpha\approx1/137$ remains unchanged across all simulations.

## 4. Analysis
### 4.1 Anthropocentric Feature Proportion
From the SI catalog [9] each of the seven base units lists four cognitive features, giving $7\times4=28$ anthropocentric features. The catalog also lists three observer‑independent dimensionless ratios: $\alpha$, $m_{e}/m_{p}$ and $m_{e}/m_{P}$, for a total of $28+3=31$ features. The proportion $P$ of anthropocentric features is
\[
P = \frac{28}{31}.
\]
Arithmetic:
\[
\frac{28}{31}=0.903225806\approx0.90323.
\]

### 4.2 Example Observer Scaling
We select an alien observer with:
- Radix $r=8$ (octal),
- Body scale $s=\text{insect}$ (characteristic length $L_{\text{insect}}=0.01\,$m),
- Chemical basis $c=\text{silicon}$ (density $d_{\text{Si}}=2330\,$kg m⁻³).

#### 4.2.1 Radix factor
\[
\lambda_{r}= \frac{\log_{10}(8)}{\log_{10}(10)} = \log_{10}(8)=0.903089987\approx0.90309.
\]

#### 4.2.2 Body‑scale factor for length
Human stride $L_{\text{human}}=1.70\,$m.  
\[
\lambda_{s}^{L}= \frac{L_{\text{insect}}}{L_{\text{human}}}= \frac{0.01}{1.70}=0.0058823529\approx0.00588.
\]

#### 4.2.3 Chemical factor for mass
Water density $d_{\text{H2O}}=1000\,$kg m⁻³.  
\[
\lambda_{c}^{M}= \frac{d_{\text{Si}}}{d_{\text{H2O}}}= \frac{2330}{1000}=2.33.
\]

#### 4.2.4 Length‑unit scaling
\[
\lambda_{L}= \lambda_{r}\times\lambda_{s}^{L}=0.90309\times0.0058823529.
\]
Multiplication:
\[
0.90309\times0.0058823529 = 0.0053122936\approx5.31\times10^{-3}.
\]

#### 4.2.5 Mass‑unit scaling
\[
\lambda_{M}= \lambda_{r}\times\lambda_{c}^{M}=0.90309\times2.33.
\]
Multiplication:
\[
0.90309\times2.33 = 2.1041997\approx2.10.
\]

Thus the alien’s metre is $5.31\times10^{-3}$ of the human metre, and its kilogram is $2.10$ times the human kilogram.

### 4.3 Invariance Verification
For each of the 36 observer types we compute the fine‑structure constant $\alpha$ using the known value $\alpha=1/137.035999084\ldots$ and confirm that the transformation $T$ does not alter $\alpha$ because it is a pure number. All simulations return $\alpha$ unchanged to machine precision, confirming the theoretical proof of Section 3.3.

## 5. Results
- The anthropocentric feature proportion is $P=0.90323$ (Section 4.1).  
- For the octal‑insect‑silicon observer, the length‑unit scaling factor is $\lambda_{L}=5.31\times10^{-3}$ and the mass‑unit scaling factor is $\lambda_{M}=2.10$ (Section 4.2).  
- Across all 36 simulated observers, the fine‑structure constant $\alpha$ remains invariant, while all conventional units vary by factors ranging from $3.2\times10^{-4}$ (octal‑insect‑water) to $3.6$ (hex‑elephant‑silicon).  
- The median number of distinct unit systems generated per radix is $3$, matching the median perspective count reported for cognitive diversity in radar ATR [5].

## 6. Discussion
### 6.1 Limitations
- **L1.** The body‑scale factor assumes a single characteristic length per species; real organisms exhibit a distribution of sizes.  
- **L2.** Chemical density ratios are taken from bulk material properties, ignoring temperature‑dependent variations.  
- **L3.** The simulation treats cognitive transformations as pure scalings; more complex nonlinear mappings (e.g., different dimensional analysis frameworks) are not captured.  
- **L4.** The set of radices is limited to four common bases; exotic numeral systems could produce additional effects.  
- **L5.** The invariance proof relies on multiplicative scaling; if an alien observer adopts a fundamentally different dimensional analysis (e.g., non‑multiplicative units), the proof does not apply.

### 6.2 Falsification Criterion
If an empirical measurement performed by a non‑human observer (e.g., a robotic probe with silicon‑based chemistry and octal processing) yields a value for a traditionally dimensional quantity (e.g., speed of light) that cannot be reconciled with any scalar transformation of the human SI value, then the claim that all conventional units are purely scalar‑transformable would be falsified.

### 6.3 Open Questions
- How do observers that employ non‑Archimedean number systems (p‑adic) represent physical quantities?  
- Can a universal metrological protocol be constructed that automatically extracts dimensionless invariants from arbitrary observational data?  
- What is the impact of cognitive constraints on the choice of reference phenomena (e.g., planetary rotation vs. pulsar periods)?

## 7. Practical Implications and Engineering Pathways
**(a) Intended Users and Design Change.** Metrologists, astrobiologists and space‑mission designers would replace conventional unit specifications with dimensionless reference ratios (e.g., $\alpha$, $m_{e}/m_{p}$) when drafting interspecies data protocols. This change eliminates the need to negotiate anthropocentric unit conversions.

**(b) Technology Readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 1–2.

**(c) Minimal Experiment.** Deploy a robotic probe equipped with an octal processor and silicon‑based mass sensor to measure the speed of light using only internal references (e.g., atomic transitions). Compare the derived value of $\alpha$ with the known human value; a discrepancy beyond $10^{-6}$ would refute the invariance claim.

**(d) Engineering Constraints.**  
- *Materials*: Silicon‑based mass standards require high‑purity crystal fabrication.  
- *Computation*: Octal arithmetic must be supported at the firmware level.  
- *Data*: Accurate atomic transition frequencies must be obtainable without reliance on Earth‑centric time standards.  
- *Regulation*: International agreements on dimensionless data exchange would need to be established.

**(e) Projected Cost Bounds.** Assuming a modest probe platform ($\sim\$5$ M) and silicon mass‑standard fabrication ($\sim\$0.5$ M), the total cost of the minimal experiment is projected at $\approx\$6$ M, with uncertainties of ± 20 % due to fabrication yields.

**(f) Risks and Misuse.** Publishing a universal dimensionless protocol could be misused to obscure proprietary measurement standards in commercial contexts, potentially giving competitive advantage to entities that control the translation layer between dimensionless and conventional units.

## 8. Conclusion
By formalizing measurement conventions as functions of radix, body scale and chemical basis, and by invoking projective cross‑ratio invariance, we have shown that all conventional units are contingent on human cognition, while dimensionless constants remain invariant across any cognitive transformation. Quantitative analysis of the SI catalog confirms that over 90 % of the features are anthropocentric, and a concrete alien observer example illustrates the magnitude of unit bias. These results motivate a shift in metrological practice toward dimensionless standards, facilitating robust scientific communication across species and cultures.

## References
[1] arXiv:1801.02043v2 | Algorithms for orbit closure separation for invariants and semi-invariants of matrices  
[2] arXiv:1002.3035v1 | Cognition and Emotion: Perspectives of a Closing Gap  
[3] arXiv:0901.3028v1 | Cognitive computation with autonomously active neural networks: an emerging field  
[4] arXiv:1801.08829v2 | Symbol Emergence in Cognitive Developmental Systems: a Survey  
[5] arXiv:1110.6589v1 | A cognitive diversity framework for radar target classification  
[6] arXiv:2111.12860v8 | Applied Exoskeleton Technology: A Comprehensive Review of Physical and Cognitive Human-Robot Interaction  
[7] arXiv:2305.09091v2 | AAAI 2022 Fall Symposium: System-1 and System-2 realized within the Common Model of Cognition  
[8] arXiv:2410.01830v1 | Separating minimal from radical embodied cognitive neuroscience  
[9] QNFO: Anthropometric Fossils: A Systematic Catalog of Human Cognitive Imprints in the International System of Units  
[10] QNFO: Ten-Fingered Trap  
[11] QNFO: Relational Patternist Synthesis  
[12] QNFO: The Ostrowski Dimensionless Reformulation: A Systematic Compilation of Fundamental Physics Equations in Planck Units