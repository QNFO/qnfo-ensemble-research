# What Makes a Measure "Natural"? Bits, Nats, and the Rhetoric of Naturalness in Quantitative Science

## Abstract

The word "natural" carries unusual persuasive weight in quantitative science: it appears in "natural logarithm," "natural language," "natural images," and, in a recent information-theoretic proposal, the claim that the nat — the information unit based on the natural logarithm — is a "genuinely natural" measure, in contrast to Shannon's bit. This paper asks whether such naturalness claims are substantive or rhetorical. We formalize three candidate criteria for a measure being natural — invariance under relabeling or reparameterization, additivity across independent systems, and independence from arbitrary representational constants — and audit the bit-versus-nat question against them. All quantitative content is derived explicitly: we compute the conversion factor $1/\ln 2 \approx 1.4427$ bits per nat, entropies of uniform and Gaussian distributions in both units, and the scaling failure of differential entropy under coordinate change. We find that the choice between bits and nats is a multiplicative constant with no invariance-theoretic consequence, so "genuine" naturalness in the mathematical sense does not discriminate the two; what does differ is convenience for calculus-based derivations. We then contrast this mathematical sense of "natural" with the sociolinguistic and dataset-geometric senses in which the term appears across natural-language processing and computer-vision literature, arguing that conflating the three senses inflates the rhetorical force of naturalness claims. We close with falsification conditions and open questions.

## 1. Introduction

Quantitative science is full of units, and units are conventions. Yet some conventions are advertised as more than conventional: they are called *natural*. The natural logarithm, the natural units of physics, natural language, natural images — in each case the adjective suggests that the quantity in question is anchored to something less arbitrary than human choice. Whether that suggestion is ever mathematically justified is the subject of this paper.

Our focal case is a recent information-theoretic proposal, arXiv:2103.16662v1, titled "A genuinely natural information measure" [6]. The supplied abstract of that work states that Shannon, in his mathematical theory of communication, proposed entropy measured in bits, but "in the same paper, Shannon also chose to measure the information in continuous systems in nats, which differ from bits by the use of the natural rather than the binary logarithm," and that the authors "point out tha[t]" something further — the supplied text is truncated at exactly the point where the paper's central claim would be stated. This truncation is itself instructive: we can audit the *framing* of the naturalness claim (bits versus nats, discrete versus continuous) without importing any memory of the full argument, and we do so here using only what the supplied entry states.

The question generalizes. In the same literature ecosystem, "natural" appears in at least three distinct senses:

1. **Mathematical naturalness**: a quantity or unit is natural if it is invariant under the symmetries of the problem, or arises without arbitrary constants (the sense invoked by [6] for the nat).
2. **Sociolinguistic naturalness**: a language is "natural" if it is acquired organically by a speech community — the sense underlying "natural language processing" [1], [2], [3], [4], [5].
3. **Distributional naturalness**: an image dataset is "natural" if it comes from everyday photographs rather than a specialized domain — the sense in "natural and medical images" [8].

These senses are logically independent. A natural language is not a natural unit; a natural image distribution need not have natural information content. Our contribution is (a) a precise, fully derived analysis of what the bit–nat choice does and does not settle mathematically, and (b) a taxonomy showing how naturalness rhetoric migrates between the three senses, using the eight supplied works as documented instances of senses 2 and 3.

The plan of the paper is as follows. Section 2 reviews the eight supplied works. Section 3 sets up the formal criteria and notation. Section 4 carries out all derivations with explicit arithmetic. Section 5 reports the computed results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 concludes.

## 2. Background and Related Work

We discuss all eight supplied bibliography entries, in their exact numbering. Because several entries are truncated abstracts with limited substantive content, we state explicitly what each entry supports and no more.

**[6] A genuinely natural information measure (arXiv:2103.16662v1).** This is the direct trigger for our study. The entry states that Shannon initiated the theoretical measuring of information in his mathematical theory of communication, proposing "a now widely used quantity, the entropy, measured in bits," and that "in the same paper, Shannon also chose to measure the information in continuous systems in nats, which differ from bits by the use of the natural rather than the binary logarithm." The entry then begins "We point out tha—" and truncates. The entry therefore supports exactly three claims: (i) bits are the standard unit for discrete entropy, (ii) nats, using the natural logarithm, were used by Shannon for continuous systems, (iii) the authors of [6] argue something further about this situation that the supplied text does not disclose. Our analysis in Sections 3–5 is an independent audit of the mathematical substance available behind framing (i)–(iii); we do not attribute to [6] any specific argument beyond what its title and supplied text state.

**[1] Challenges Encountered in Turkish Natural Language Processing Studies (arXiv:2101.11436v1).** The entry defines natural language processing as "a branch of computer science that combines artificial intelligence with linguistics" aiming to "analyze a language element such as writing or speaking with software and convert it into information," and notes that "each language has its own grammatical rules and vocabulary diversity," making the complexity of studies in the field "somewhat understandable." This supports our taxonomy's sense 2: here "natural" modifies *language* in a sociolinguistic sense, and the entry's own point is that the difficulty of processing a language is language-dependent — grammatical rules and vocabulary diversity vary per language, so there is no single invariant difficulty measure across natural languages.

**[2] A Comprehensive Review of State-of-The-Art Methods for Java Code Generation from Natural Language Text (arXiv:2306.06371v1).** The entry describes Java code generation as automatically producing Java code from natural-language text, an NLP task that "helps in increasing programmers' productivity by providing them with immediate solutions to the simplest and most repetitive tasks," and notes the challenge arises "because of the hard syntactic rules and the necessity of a deep understanding of the semantic aspect of the programmin[g]" language. The entry is useful to us because it places "natural language" and a *formal* language (Java) in a single pipeline, making the natural/formal contrast explicit: the natural side supplies intent, the formal side supplies hard syntax. The supplied text gives no quantitative results, and we claim none from it.

**[3] An Automated Multiple-Choice Question Generation Using Natural Language Processing Techniques (arXiv:2103.14757v1).** The entry states that automatic multiple-choice question generation (MCQG) is "a useful yet challenging task" in NLP, defined as generating correct and relevant questions from textual data, and that manually creating sizeable, meaningful questions is "time-consuming and challenging" for teachers; the authors present an NLP-based system (the description truncates before details). We use this entry only as a further instance of sense-2 "natural language" terminology and of task difficulty being motivated by human labor costs; the truncated text supports no methodological detail.

**[4] Time, Tense and Aspect in Natural Language Database Interfaces (arXiv:cmp-lg/9803002v1).** The entry states that most existing natural language database interfaces (NLDBs) were designed for database systems with "very limited facilities for manipulating time-dependent data" and "do not support adequately temporal linguistic mechanisms (verb tenses, temporal adverbials, temporal subordinate clauses, etc.)," while the database community is becoming increasingly interested in temporal databases (text truncates). This entry is valuable for our argument because it shows a mismatch between the structure of a natural language (temporal mechanisms) and the structure of a formal representation (limited temporal facilities) — an early documented case where "naturalness" of language resists capture by a chosen formal system, prefiguring our point that naturalness is a property of a fit between representation and phenomenon, not of the representation alone.

**[5] An Open Natural Language Processing Development Framework for EHR-based Clinical Research (arXiv:2110.10780v3).** The entry reports "some resistance in the clinical and translational research community to adopt NLP models due to limited transparency, interpretability, and usability," and that the authors "proposed an open natural language processing development framework," evaluated "through the implementation of NLP algori[thms]" (text truncates; the case demonstration involves the National COVID Cohort Collaborative, N3C, per the title). For our purposes this entry documents that adoption of NLP technology depends on transparency and interpretability rather than on any intrinsic naturalness of the underlying language — a social, not mathematical, criterion of adequacy.

**[7] Recommended Implementation of Quantitative Susceptibility Mapping for Clinical Research in The Brain (arXiv:2307.02306v1).** The entry describes consensus recommendations by the ISMRM Electro-Magnetic Tissue Properties Study Group for implementing quantitative susceptibility mapping (QSM), and states that "current QSM methods have been demonstrated to be repeatable and reproducible for generating quantitative tissue magnetic suscepti[bility]" (text truncates). Although this entry does not use the word "natural," it supplies the contrast case for our argument: tissue magnetic susceptibility is a quantitative property whose measurement is made trustworthy not by naturalness of units but by consensus standardization, repeatability, and reproducibility. This is the alternative route to unit credibility that a "genuinely natural" unit claim, if it were substantive, would render unnecessary.

**[8] The Effect of Intrinsic Dataset Properties on Generalization (arXiv:2401.08865v3).** The entry investigates "discrepancies in how neural networks learn from different imaging domains, which are commonly overlooked when adopting computer vision techniques from the domain of natural images to other specialized domains such as medical images," and states that "recent works have found that the generalization error of a trained network typically increases with the intrinsic dimension ($d_{data}$) of its" data (text truncates). This is our anchor for sense 3: "natural images" is a domain label, and the entry's own point is that the label conceals quantitative structure — intrinsic dimension $d_{data}$ — that actually governs generalization. The naturalness of an image distribution is thus a proxy for measurable geometric properties, not a primitive.

In summary: only [6] concerns units of information; [1]–[5] concern natural language in the sociolinguistic sense; [7] concerns standardized quantitative measurement; [8] concerns dataset geometry behind a "natural" domain label. The supplied entries for [2], [3], [4], [5], [7], and [8] are truncated and give no further detail; we relate each to our argument only through what its text states.

## 3. Methods

### 3.1 Notation

Let $X$ be a discrete random variable with probability mass function $p_i = P(X = x_i)$ over outcomes $i \in \{1, \dots, k\}$. The Shannon entropy in base-$b$ logarithms is

$$H_b(X) = -\sum_{i=1}^{k} p_i \log_b p_i.$$

With $b = 2$ the unit is the bit; with $b = e$ the unit is the nat. For a continuous random variable with density $f(x)$ on $\mathbb{R}$, the differential entropy is

$$h_b(X) = -\int_{\mathcal{X}} f(x) \log_b f(x)\, dx.$$

The conversion between bases follows from $\log_b a = \frac{\ln a}{\ln b}$, so for any entropy quantity $Q$,

$$Q_{\text{bits}} = \frac{Q_{\text{nats}}}{\ln 2} = Q_{\text{nats}} \cdot \log_2 e.$$

### 3.2 Criteria for mathematical naturalness

We propose three criteria that a candidate "natural" unit or measure could satisfy. They are chosen to be checkable by explicit computation and are motivated by standard practice in mathematical physics, where "natural" typically means invariant under the symmetries of the problem or free of arbitrary constants.

- **C1 (Relabeling invariance):** the measure of information in a system is unchanged when the outcomes are relabeled by any bijection (for discrete systems) or the coordinate system is changed (for continuous systems).
- **C2 (Additivity):** for independent systems $X$ and $Y$, the information measure of the joint system equals the sum of the individual measures: $I(X, Y) = I(X) + I(Y)$.
- **C3 (Constant-freedom):** the measure does not depend on an arbitrary representational constant — here, the logarithm base $b$ — in a way that changes any qualitative conclusion.

We evaluate both the bit and the nat against C1–C3, and we evaluate the *pair* against a fourth, meta-criterion:

- **C4 (Discrimination):** the choice between the two candidates affects at least one invariance, additivity, or qualitative property.

If C4 fails, the naturalness claim that discriminates bits from nats is rhetorical rather than mathematical, and the credible route to unit credibility is the one exemplified by [7]: standardization, repeatability, reproducibility.

### 3.3 Method for the cross-sense audit

For senses 2 and 3 of "natural," we perform a qualitative audit: for each supplied entry using the term, we extract what property of the system the entry itself identifies as load-bearing (language-dependent rules in [1]; hard syntax versus natural intent in [2]; human labor cost in [3]; temporal mechanisms versus limited formal facilities in [4]; transparency and interpretability in [5]; intrinsic dimension $d_{data}$ in [8]) and check whether that property is invariant in any mathematical sense. No quantitative computation is possible from these entries, as none supplies numbers; we therefore restrict all Section 5 numerical results to the information-theoretic derivations of Section 4.

## 4. Analysis

Every input number below is either a definition, a standard mathematical constant computed here from first principles, or a value derived in a prior step. We show all arithmetic.

### 4.1 The conversion constant

**Input:** the natural logarithm of 2. We compute $\ln 2$ by the convergent series $\ln 2 = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$, which alternates with decreasing terms; summing the first ten terms gives

$$\ln 2 \approx 1 - \tfrac{1}{2} + \tfrac{1}{3} - \tfrac{1}{4} + \tfrac{1}{5} - \tfrac{1}{6} + \tfrac{1}{7} - \tfrac{1}{8} + \tfrac{1}{9} - \tfrac{1}{10} = 0.6456349\ldots$$

with alternating-series error bound less than the next term, $\frac{1}{11} \approx 0.0909$. To obtain the value to six decimals we instead use the rapidly convergent identity $\ln 2 = 2\,\text{artanh}(1/3) = 2\sum_{n=0}^{\infty} \frac{1}{(2n+1)\,3^{2n+1}}$. The first four terms give

$$\ln 2 \approx 2\left(\tfrac{1}{3} + \tfrac{1}{3 \cdot 27} + \tfrac{1}{5 \cdot 243} + \tfrac{1}{7 \cdot 2187}\right) = 2\left(0.3333333 + 0.0123457 + 0.0008230 + 0.0000653\right).$$

The bracket sums to $0.3333333 + 0.0123457 = 0.3456790$; adding $0.0008230$ gives $0.3465020$; adding $0.0000653$ gives $0.3465673$. Doubling: $\ln 2 \approx 0.6931346$, with error below the next term $2/(9 \cdot 3^9) = 2/177147 \approx 1.13 \times 10^{-5}$. Refining with the next two terms, $\frac{1}{9 \cdot 3^9} = \frac{1}{177147} \approx 5.645 \times 10^{-6}$ and $\frac{1}{11 \cdot 3^{11}} = \frac{1}{43046721} \approx 2.323 \times 10^{-8}$, gives $\ln 2 \approx 0.6931346 + 2(5.645 \times 10^{-6} + 2.323 \times 10^{-8}) = 0.6931346 + 0.0000113 = 0.6931459$, consistent with the standard value

$$\ln 2 = 0.693147\ (\text{to } 6 \text{ decimals}).$$

**Derivation 1 (bits per nat).** Since $Q_{\text{bits}} = Q_{\text{nats}} / \ln 2$,

$$\frac{1}{\ln 2} = \frac{1}{0.693147} = 1.442695\ \text{bits per nat},$$

where the division $1/0.693147$: $0.693147 \times 1.44 = 0.998132$; $0.693147 \times 1.4427 = 0.999999 \approx 1$ (check: $0.693147 \times 1.4427 = 0.693147 + 0.693147 \times 0.4427 = 0.693147 + 0.306847 = 1.000$ to six decimals). Hence

$$c \equiv \log_2 e = \frac{1}{\ln 2} = 1.442695.$$

This constant $c$ is the *entire* mathematical difference between bits and nats for any entropy-like quantity: multiplication by a fixed positive constant.

### 4.2 Discrete entropy: the fair coin and the uniform $k$-outcomes case

**Derivation 2 (fair coin).** For $k = 2$, $p_1 = p_2 = \frac{1}{2}$:

$$H_e(X) = -\left(\tfrac{1}{2}\ln\tfrac{1}{2} + \tfrac{1}{2}\ln\tfrac{1}{2}\right) = -\ln\tfrac{1}{2} = \ln 2 = 0.693147\ \text{nats}.$$

In bits: $H_2(X) = 0.693147 \times 1.442695 = 1.000000$ bit (check: $0.693147 \times 1.442695 = 0.693147 \times 1 + 0.693147 \times 0.442695 = 0.693147 + 0.306853 = 1.000000$, using $0.693147 \times 0.442695 \approx 0.306853$). So one bit $= \ln 2 = 0.693147$ nats exactly, by definition of the units.

**Derivation 3 (uniform over $k$ outcomes).** For $p_i = \frac{1}{k}$:

$$H_e(X) = -\sum_{i=1}^{k} \frac{1}{k} \ln \frac{1}{k} = \ln k.$$

For $k = 3$: $H_e = \ln 3$. Computing $\ln 3 = \ln 2 + \ln(3/2) = 0.693147 + \ln 1.5$; and $\ln 1.5 = \ln\frac{1 + 1/5}{1 - 1/5} = 2\left(\frac{1}{5} + \frac{1}{3 \cdot 125} + \frac{1}{5 \cdot 3125}\right) = 2(0.2 + 0.0026667 + 0.000064) = 2 \times 0.2027307 = 0.4054614$. Hence $\ln 3 = 0.693147 + 0.405461 = 1.098608 \approx 1.098612$ nats (small residual from truncated series). In bits:

$$H_2 = \frac{1.098612}{0.693147} = 1.584963\ \text{bits},$$

check: $0.693147 \times 1.584963 = 0.693147 \times 1.5 = 1.039721$; $0.693147 \times 0.084963 = 0.058891$; sum $= 1.098612$. ✓

**Criterion check (C2, additivity).** For independent $X, Y$ with distributions $p_i, q_j$:

$$H_e(X, Y) = -\sum_{i,j} p_i q_j \ln (p_i q_j) = -\sum_{i,j} p_i q_j (\ln p_i + \ln q_j) = H_e(X) + H_e(Y),$$

since $\sum_j q_j = 1$ and $\sum_i p_i = 1$. The same computation with $\ln$ replaced by $\log_2$ holds verbatim. **Both bits and nats satisfy C2**, and the proof is base-independent — the base never enters the additivity argument except as a constant prefactor.

**Criterion check (C1, relabeling invariance, discrete).** A bijection $\pi$ of outcomes permutes the summands $-p_i \log_b p_i$; a finite sum is invariant under permutation of its terms. **Both units satisfy C1 for discrete systems.**

### 4.3 Continuous entropy: the Gaussian and the scaling failure

**Derivation 4 (Gaussian differential entropy).** For $f(x) = \frac{1}{\sqrt{2\pi}\,\sigma} e^{-x^2/(2\sigma^2)}$ with $\sigma = 1$:

$$h_e(X) = -\int f \ln f\, dx = \ln\left(\sqrt{2\pi}\,\sigma\right) + \frac{1}{2} = \frac{1}{2}\ln(2\pi e\,\sigma^2).$$

With $\sigma = 1$: we need $\ln(2\pi)$. Using $\pi = 3.141593$ and $e = 2.718282$: $2\pi e = 2 \times 3.141593 \times 2.718282$. First $3.141593 \times 2.718282$: $3 \times 2.718282 = 8.154846$; $0.141593 \times 2.718282 = 0.384936$; total $= 8.539782$. Then $2 \times 8.539782 = 17.079564$. So

$$h_e = \tfrac{1}{2}\ln(17.079564) = \tfrac{1}{2} \times 2.837877 = 1.418939\ \text{nats},$$

where $\ln 17.079564 = \ln 17 + \ln(1.004680) \approx 2.833213 + 0.004669 = 2.837882$ (using $\ln 17 = \ln 16 + \ln(17/16) = 4\ln 2 + \ln 1.0625 = 2.772588 + 0.060625 = 2.833213$; and $\ln 1.004680 \approx 0.004669$). In bits:

$$h_2 = 1.418939 \times 1.442695 = 2.047100\ \text{bits},$$

check: $1.418939 \times 1.442695 = 1.418939 + 1.418939 \times 0.442695 = 1.418939 + 0.628161 = 2.047100$. ✓

**Derivation 5 (scaling failure — the key asymmetry).** Let $X$ be uniform on $[0, 1]$, with density $f(x) = 1$ on $[0,1]$. Then

$$h_e(X) = -\int_0^1 1 \cdot \ln 1\, dx = 0\ \text{nats}.$$

Now let $Y = 2X$, uniform on $[0, 2]$, density $g(y) = \frac{1}{2}$. Then

$$h_e(Y) = -\int_0^2 \tfrac{1}{2} \ln \tfrac{1}{2}\, dy = -\ln\tfrac{1}{2} = \ln 2 = 0.693147\ \text{nats} = 1.000000\ \text{bit}.$$

In general, for $Y = aX$ with $a > 0$, the density transforms as $g(y) = \frac{1}{a} f(y/a)$, so

$$h_e(Y) = h_e(X) + \ln a.$$

**Differential entropy shifts by $\ln a$ under rescaling** — it is not invariant under coordinate change, in either bits or nats (in bits the shift is $\log_2 a$, still nonzero). This is the one place where the supplied text of [6] points: Shannon "chose to measure the information in continuous systems in nats," and the continuous setting is precisely where the measure is coordinate-dependent. But note: the coordinate dependence is identical in structure for both bases. The failure of C1 for continuous systems is a property of differential entropy as such, not of the nat.

### 4.4 Criterion C4: does the bit–nat choice discriminate anything?

Assembling the checks:

| Criterion | Bit | Nat | Discriminates? |
|---|---|---|---|
| C1 (discrete relabeling) | yes | yes | no |
| C1 (continuous rescaling) | no | no | no |
| C2 (additivity) | yes | yes | no |
| C3 (base is a constant) | fails by construction | fails by construction | no |

For C3: both bit and nat are defined *by* a choice of base ($b = 2$ vs. $b = e$); the base $e$ is distinguished only by calculus convenience — $\frac{d}{dx}\ln x = \frac{1}{x}$, whereas $\frac{d}{dx}\log_2 x = \frac{1}{x \ln 2}$, introducing the constant $c = 1.442695$ from Derivation 1 into every derivative. This is a convenience argument, not an invariance argument: the constant $c$ never changes the sign, zero set, or ordering of any entropy quantity, since $c > 0$.

**Conclusion of the audit: C4 fails.** No criterion in $\{C1, C2, C3\}$ is satisfied by one unit and violated by the other. The mathematical content of "bits versus nats" is exactly the scalar $c = 1.442695$.

### 4.5 A worked aggregate: information in a megabit message

**Derivation 6.** A message of $n = 10^6$ fair coin flips carries $H = n$ bits $= 10^6 \times \ln 2 = 6.93147 \times 10^{5}$ nats. Conversely, a continuous Gaussian channel statement with $h_e = 1.418939$ nats (Derivation 4) corresponds to $2.047100$ bits (Derivation 4). Any statement expressible in one unit is expressible in the other by multiplying or dividing by $c$; no proposition changes truth value.

### 4.6 Cross-sense audit (qualitative, no computation possible)

The entries [1]–[5], [7], [8] supply no numbers (their texts truncate before any quantitative content), so no arithmetic is possible; we record the qualitative finding only. In [1], the load-bearing property is per-language variation in "grammatical rules and vocabulary diversity" — not