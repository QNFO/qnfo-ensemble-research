# When Is a Property "Genuinely Natural"? A Formal Framework for Naturalness Claims in Measurement, Information, and Modelling

## Abstract

The word "natural" appears across the quantitative sciences in at least three distinct senses: natural language as an object of processing, natural images as a domain of learning, and the natural logarithm as a choice of measurement base. Claims that a quantity, unit, or property is "genuinely natural" — most recently revived by the observation that Shannon himself measured discrete information in bits but continuous information in nats — are usually defended informally. We formalize naturalness as a testable property of a measurement convention, proposing three criteria: base-invariance of ratios, dimensionlessness of derived constants, and absence of correction factors in analytic operations such as differentiation. We derive the base-conversion identity for entropy, show that the ratio of entropies in nats and bits equals $\ln 2 \approx 0.6931471808$ for every distribution, and therefore that no distribution can distinguish the two conventions by ratio alone. We then quantify the departure of a base-$b$ convention from the natural base via $\Delta(b) = |\ln b - 1|$, obtaining $\Delta(2) = 0.3068528192$, $\Delta(e) = 0$, and $\Delta(10) = 1.3025850929$, and compute the differential entropy of a unit-variance Gaussian as $1.4189385333$ nats $= 2.0470956$ bits. The framework shows that the "genuinely natural" claim for nats is analytic rather than empirical, and we discuss its circularity, falsifiability, and transfer to adjacent domains.

## 1. Introduction

Quantitative claims about the world require conventions: units, bases, reference classes, and scales. Some conventions are arbitrary, and some are argued to be privileged — "natural." The question posed by the present work, motivated by the re-entry of a prior artefact (Zenodo record $10.5281/\text{zenodo.17204355}$) asking whether certain properties are "genuinely natural," is: what would it mean, precisely, for a property or measurement convention to be genuinely natural rather than merely conventional?

The trigger for this question is the observation in [6] that Shannon's mathematical theory of communication introduced entropy measured in bits, yet in the same context chose to measure information in continuous systems in nats, which differ from bits only by the use of the natural rather than the binary logarithm. The authors of [6] point out an asymmetry in this choice and argue for a "genuinely natural" information measure. That argument, as summarized in the supplied abstract, is a claim about the naturalness of a measurement convention — exactly the kind of claim this paper seeks to make precise.

The word "natural" is heavily overloaded in the surrounding literature. Natural language processing studies the analysis of human language by software [1]; natural-language text is the input to code generation systems [2]; "natural images" are contrasted with medical images in studies of how dataset properties affect generalization [8]. In each case, "natural" denotes a domain or reference class, not a property of a logarithm. Meanwhile, in quantitative imaging, "quantitative tissue magnetic susceptibility" is a property whose meaningfulness depends on repeatability, reproducibility, and consensus implementation standards [7]. The terminological overlap is not merely lexical: in all these cases, a community must decide whether a quantity is a property of the world or an artefact of a convention, and the answer determines how results transfer across studies.

This paper makes three contributions. First, we propose a three-criterion definition of genuine naturalness for a measurement convention (Section 3). Second, we carry out explicit derivations on the bits-versus-nats case, computing the conversion constants, the distribution-independence of entropy ratios, the differentiation penalty of non-natural bases, and a concrete entropy value for the Gaussian (Section 4). Third, we use the resulting framework to classify naturalness claims found in the related literature and to articulate what would falsify the "genuinely natural" thesis (Sections 5 and 6).

## 2. Background and Related Work

We discuss the eight supplied works in their given order, extracting from each only what its supplied summary supports.

**[1] Challenges Encountered in Turkish Natural Language Processing Studies.** This work defines natural language processing as a branch of computer science combining artificial intelligence with linguistics, aiming to analyze language elements such as writing or speech with software and convert them into information. It notes that each language has its own grammatical rules and vocabulary diversity, making complexity in this field understandable. For our purposes it supplies the first sense of "natural": natural language as a domain whose per-language structure resists uniform treatment — a reminder that "natural" often names a heterogeneous reference class rather than a canonical object.

**[2] A Comprehensive Review of State-of-The-Art Methods for Java Code Generation from Natural Language Text.** This review frames Java code generation as automatically generating Java code from natural language text, an NLP task aimed at increasing programmer productivity for simple and repetitive tasks, and identifies the challenge as arising from hard syntactic rules and the need for deep semantic understanding of the programming language. It illustrates a second sense of "natural": natural language as an *input interface* to a formally rigid target system. The contrast between "hard syntactic rules" and semantic understanding prefigures our criterion of analytic convenience: formal systems admit canonical choices; natural-language interfaces do not.

**[3] An Automated Multiple-Choice Question Generation Using Natural Language Processing Techniques.** This work presents an NLP-based system for automatic multiple-choice question generation (MCQG), described as a useful yet challenging task of generating correct and relevant questions from textual data, motivated by the time-consuming nature of manually creating sizeable, meaningful question sets for teachers. It contributes a third sense of "natural": generated artifacts must be judged *relevant* to a human purpose, i.e., naturalness as fitness for a reference use rather than as a formal property.

**[4] Time, Tense and Aspect in Natural Language Database Interfaces.** This work observes that most existing natural language database interfaces (NLDBs) were designed for database systems with very limited facilities for manipulating time-dependent data and do not adequately support temporal linguistic mechanisms such as verb tenses, temporal adverbials, and temporal subordinate clauses, while noting growing database-community interest in temporal databases. It is directly relevant to our theme: a mismatch between a natural (linguistic) convention — tense and aspect — and a formal (database) convention. The supplied summary gives no quantitative results, and we use it only as evidence that aligning natural and formal conventions is a long-standing, unsolved design problem.

**[5] An Open Natural Language Processing Development Framework for EHR-based Clinical Research (N3C).** This study notes resistance in the clinical and translational research community to adopting NLP models due to limited transparency, interpretability, and usability, and proposes an open NLP development framework evaluated through implementation of NLP algorithms. It supplies the methodological bridge for our argument: whether a quantity or model is trusted as reflecting a real property depends on transparency and reproducibility of the measurement pipeline, not on the label attached to the quantity.

**[6] A genuinely natural information measure.** This is the anchor work. Its summary states that the theoretical measuring of information was initiated by Shannon in his mathematical theory of communication, in which he proposed the now widely used entropy measured in bits, yet in the same paper chose to measure information in continuous systems in nats, which differ from bits by the use of the natural rather than the binary logarithm; the authors point out [an issue with this choice, per the truncated summary]. The supplied abstract is truncated mid-sentence ("We point out tha…"), so we cannot attribute to it any specific remedy beyond the identification of the bits/nats asymmetry. We therefore treat [6] as posing the naturalness question, and our Sections 3–5 as an independent formalization and quantification of that question, not as a restatement of its solution.

**[7] Recommended Implementation of Quantitative Susceptibility Mapping for Clinical Research in The Brain (ISMRM consensus).** This consensus article of the ISMRM Electro-Magnetic Tissue Properties Study Group provides recommendations for implementing quantitative susceptibility mapping (QSM) in clinical brain research, and states that current QSM methods have been demonstrated to be repeatable and reproducible for generating quantitative tissue magnetic susceptibility [values]. It offers the strongest external analogy for our thesis: a "quantitative tissue property" becomes scientifically usable only after a community reaches consensus on implementation, and its claim to measure a real property is grounded in demonstrated repeatability and reproducibility. Naturalness claims about units deserve the same standard of community validation.

**[8] The Effect of Intrinsic Dataset Properties on Generalization: Unraveling Learning Differences Between Natural and Medical Images.** This work investigates discrepancies in how neural networks learn from different imaging domains, commonly overlooked when adopting computer vision techniques from natural images to specialized domains such as medical images, and reports that recent works find the generalization error of a trained network typically increases with the intrinsic dimension ($d_{data}$) of the dataset. It supplies the fourth sense of "natural": natural images as a reference domain whose intrinsic properties ($d_{data}$) measurably affect learning. The summary provides no numerical values for $d_{data}$ or error, so we use it qualitatively: even "natural" here is a domain-relative qualifier, and the property that matters (intrinsic dimension) is defined relative to the dataset, not absolutely.

Across [1]–[8], "natural" consistently denotes either a domain ([1], [2], [3], [8]), a linguistic convention ([4]), or a logarithm base ([6]), while the credibility of any quantitative-property claim rests on transparency and reproducibility ([5], [7]). None of the supplied entries other than [6] makes a naturalness claim about a measurement convention; our framework is therefore built on [6]'s question and tested against the others as contrast cases.

## 3. Methods

### 3.1 Setting

Let $P$ be a discrete probability distribution over outcomes $i \in \{1, \dots, n\}$ with probabilities $p_i > 0$, $\sum_{i=1}^{n} p_i = 1$. The Shannon entropy of $P$ in base $b > 1$, $b \neq 1$, is

$$H_b(P) = -\sum_{i=1}^{n} p_i \log_b p_i.$$

The two dominant conventions are $b = 2$ (bits) and $b = e$ (nats). For continuous variables with density $f_X(x)$, the differential entropy is

$$h_b(X) = -\int_{-\infty}^{\infty} f_X(x) \log_b f_X(x)\, dx.$$

### 3.2 Proposed criteria for genuine naturalness

We propose that a measurement convention $c$ (here, a logarithm base) is *genuinely natural* relative to a class of operations $\mathcal{O}$ if it satisfies:

- **N1 (Ratio invariance):** For any two quantities $Q_1, Q_2$ measured under $c$, the ratio $Q_1 / Q_2$ is independent of the choice among the candidate conventions being compared, whenever the quantities purport to describe the same underlying object.
- **N2 (Dimensionless derived constants):** Constants introduced by the convention into derived expressions (derivatives, integrals, bounds) equal $1$, so that no scale factor attributable purely to the convention appears.
- **N3 (Reference-class independence):** The convention does not presuppose a particular domain or reference class (e.g., a binary communication channel, a decimal arithmetic tradition, or an imaging domain).

Criterion N1 is a consistency condition; N2 is an analytic-convenience condition; N3 is a universality condition. A convention satisfying all three is, under our definition, genuinely natural; one satisfying none is purely conventional.

### 3.3 Evaluation protocol

For the bits-versus-nats comparison we evaluate each criterion by explicit derivation: N1 via the base-conversion identity applied to arbitrary $P$ (Section 4, D1–D2); N2 via the differentiation penalty of base-$b$ logarithms and a proposed penalty functional $\Delta(b)$ (D5–D6); N3 via inspection of which domains motivate each base. We additionally compute a concrete entropy value for the Gaussian as a worked example (D7) and the fair coin as the discrete anchor case (D8).

## 4. Analysis

Every input number below is either a standard mathematical constant stated with its value, or derived here step by step. No empirical data are used.

### D1. Base-conversion identity

Using $\log_b p = \frac{\ln p}{\ln b}$,

$$H_b(P) = -\sum_{i=1}^{n} p_i \frac{\ln p_i}{\ln b} = \frac{1}{\ln b} \left( -\sum_{i=1}^{n} p_i \ln p_i \right) = \frac{H_e(P)}{\ln b}.$$

The same factor $1/\ln b$ converts the differential entropy: $h_b(X) = h_e(X)/\ln b$.

### D2. Ratio invariance (criterion N1)

For any distribution $P$,

$$\frac{H_e(P)}{H_2(P)} = \frac{H_e(P)}{H_e(P)/\ln 2} = \ln 2.$$

The ratio is $\ln 2$ for *every* $P$; it carries no information about $P$. Hence no distribution, and no dataset of entropies, can distinguish bits from nats by ratio alone: the two conventions differ by a global rescaling, which is the signature of a purely conventional difference. Criterion N1 is therefore satisfied equally (and vacuously) by both bases.

### D3. Numerical value of $\ln 2$

We compute $\ln 2$ from the identity $\ln \frac{1+x}{1-x} = 2\,\mathrm{artanh}(x)$ with $x = 1/3$, since $\frac{1 + 1/3}{1 - 1/3} = \frac{4/3}{2/3} = 2$. With $\mathrm{artanh}(x) = \sum_{k=0}^{\infty} \frac{x^{2k+1}}{2k+1}$:

$$\mathrm{artanh}\!\left(\tfrac{1}{3}\right) = \frac{1}{3} + \frac{1}{3 \cdot 3^3} + \frac{1}{5 \cdot 3^5} + \frac{1}{7 \cdot 3^7} + \frac{1}{9 \cdot 3^9} + \frac{1}{11 \cdot 3^{11}} + \frac{1}{13 \cdot 3^{13}} + \frac{1}{15 \cdot 3^{15}}.$$

Term by term:

$$\frac{1}{3} = 0.3333333333; \quad \frac{1}{81} = 0.0123456790; \quad \frac{1}{1215} = 0.0008230453;$$
$$\frac{1}{15309} = 0.0000653218; \quad \frac{1}{177147} = 0.0000056450; \quad \frac{1}{1948617} = 0.0000005132;$$
$$\frac{1}{20726199} = 0.0000000482; \quad \frac{1}{215233605} = 0.0000000046.$$

Cumulative sum: $0.3333333333 + 0.0123456790 = 0.3456790123$; $+ 0.0008230453 = 0.3465020576$; $+ 0.0000653218 = 0.3465673794$; $+ 0.0000056450 = 0.3465730244$; $+ 0.0000005132 = 0.3465735376$; $+ 0.0000000482 = 0.3465735858$; $+ 0.0000000046 = 0.3465735904$. The next term is below $5 \times 10^{-10}$, so

$$\ln 2 = 2 \times 0.3465735904 = 0.6931471808.$$

### D4. Numerical value of $\log_2 e$

$$\log_2 e = \frac{1}{\ln 2} = \frac{1}{0.6931471808}.$$

Check by multiplication: $0.6931471808 \times 1.4426950 = 0.6931471808 \times 1.4 = 0.9704060531$, plus $0.6931471808 \times 0.0426950 = 0.0295939469$; total $= 0.9704060531 + 0.0295939469 = 1.0000000000$ (to the shown precision). Hence

$$\log_2 e = 1.4426950.$$

### D5. Differentiation penalty (criterion N2)

For the natural logarithm, $\frac{d}{dx} \ln x = \frac{1}{x}$: no convention-dependent constant appears. For base 2,

$$\frac{d}{dx} \log_2 x = \frac{d}{dx} \frac{\ln x}{\ln 2} = \frac{1}{x \ln 2} = \frac{1.4426950}{x}.$$

The factor $1/\ln 2 = 1.4426950$ (D4) is a pure convention artefact: it appears in every differentiated expression regardless of the function being studied. Similarly $\frac{d}{dx} 2^x = 2^x \ln 2 = 0.6931471808 \cdot 2^x$, whereas $\frac{d}{dx} e^x = e^x