# The Adele Analogy for Epistemic Boundaries: Local Models, a Restricted Product of Representations, and a Quantified Validity Radius

## Abstract

Scientific and engineering practice routinely deploys models outside the domains in which they were validated, and the resulting failures are usually discovered only after the fact. Existing treatments of epistemic uncertainty flag that a prediction is uncertain but do not say where a validated model stops being valid or which parts of its content survive a change of representation. This paper develops a formal framework, modeled on the adele ring, in which each validated model is a "local completion" of an underlying phenomenon, each carries an explicit validity boundary, and the robust content of a model class is exactly what is invariant under changes of representation. Models are formalized as local charts with validation domains, combined in a restricted product over representations, and the framework is tested on the Poisson-to-Gaussian max-entropy bridge. With full arithmetic, the paper shows that at $\lambda = 100$ the Gaussian local model reproduces Poisson probabilities to within $3.3\%$ in log-space at one standard deviation but fails by a factor of $1.30$ at three standard deviations, locating the $5\%$ log-tolerance validity radius between $2\sigma$ and $2.5\sigma$, and identifies the skewness $1/\sqrt{\lambda} = 0.1$ as the leading representation-dependent quantity excluded from the invariant core. The framework turns "we do not know" into a measured radius, applicable to out-of-distribution risk assessment.

## 1. Introduction

Deep-learning models and statistical models are now validated on a dataset or a regime and then deployed on inputs that lie outside that regime, and the point at which they stop being trustworthy is not marked anywhere in the deployed artifact. Clinicians who use automated contouring of organs at risk in radiotherapy planning face exactly this problem: deep-learning contouring has improved markedly, yet reliability under out-of-distribution scenarios remains a stated clinical concern, and the consequence of an unnoticed validity failure is a treatment plan that harms a patient [7]. The same structure appears wherever a model certified in one regime is extrapolated: the failure is not random noise but a systematic breakdown at a boundary nobody drew.

The cost of not drawing the boundary is concrete. A radiotherapy team that cannot distinguish "the model is interpolating within its validated domain" from "the model is extrapolating" must either apply costly manual review everywhere or accept unquantified risk [7]. An autonomous reasoning system that aggregates scientific claims needs to know when a well-supported local consensus stops supporting a global conclusion, a need that formal architectures for truth-promoting autonomous scientific reasoning already recognize by making belief a dynamic function over structured claims [1]. In both cases, the missing capability is the same: an explicit, computable statement of where a validated model's guarantees end.

If the framework proposed here holds, that capability becomes available in a specific form. Every model would carry a machine-readable validity boundary, stated as a radius in the space of deviations from the validation regime, calibrated by explicit arithmetic of the kind performed in Section 4. Incompatibilities between well-validated models, such as the standing tension between quantum mechanics and general relativity, would be classified not as defects but as structured edges of ignorance that indicate where a deeper global object is missing. And the robust content of a model class would be identified by an invariance test: what survives a change of representation is what one is entitled to extrapolate.

The analogy that organizes the framework is the adele ring of number theory. The adele ring $\mathbb{A}$ combines, for every prime $p$, a local field $\mathbb{Q}_p$ with the real completion $\mathbb{R}$, in a restricted product: an element of $\mathbb{A}$ is a tuple of local elements that is a $p$-adic integer for all but finitely many $p$. No single local field contains the arithmetic of the rationals; the global object is recovered only by imposing coherence across all local completions simultaneously. Arithmetic transfer conjectures in the Langlands program make this coherence principle precise by relating local data attached to $p$-divisible groups across places, and have been proved in low-dimensional cases [4]. A related research program has proposed adelic consistency conditions across primes as a candidate selection principle for physical constants, formulated as a testable conjecture with a negative control and toy dynamics [11]. The present paper transfers the same structural idea from arithmetic to epistemology: each validated model is a local completion, the unknown is the missing global object, and the boundary of a model is the region where its local coherence with other validated models fails.

The paper's contributions are:

- A formal definitions layer: models as local charts with explicit validation domains, a compatibility relation, and an adele-like restricted product over representations, given in Section 3.
- An invariance criterion for robust knowledge: the invariant core of a model class is what is unchanged under admissible changes of representation, with the first non-invariant term computable as a cumulant ratio, derived in Section 4.
- A quantified validity radius for the Poisson-to-Gaussian max-entropy bridge: log-probability errors of $3.2\%$ at $1\sigma$, $3.0\%$ at $2\sigma$, $12.0\%$ at $2.5\sigma$, and a factor of $1.30$ at $3\sigma$, all computed with shown arithmetic in Section 4 and reported in Section 5.
- A mapping of the framework onto existing epistemic-uncertainty practice and its users, with technology-readiness assessment and the smallest falsifying experiment, given in Sections 6 and 7.

## 2. Background and Related Work

This section reviews the works supplied in the bibliography and states, for each, what its own summary supports. Eight of the twelve entries carry substantive summaries; entries [9], [10] and [12] are supplied with empty or minimal summaries and are discussed only through what is stated.

Formal epistemic architectures. Bayesian Epistemology with Weighted Authority (BEWA) responds to the exponential expansion of scientific literature, which its summary states has surpassed the epistemic processing capabilities of both human experts and current artificial intelligence systems; it operationalises belief as a dynamic, probabilistically coherent function over structured scientific claims [1]. BEWA supplies the aggregation layer that a science of epistemic boundaries would sit on top of: aggregation says how to combine validated local models, while the present framework says where each local model's validity ends. The two are complementary, and Section 7 uses BEWA-style structured claims as the natural carrier format for validity-boundary metadata.

Epistemic intervention in learned systems. Frictive Policy Optimization (FPO) treats clarification, verification, challenge, redirection, and refusal as explicit control actions that a language-model policy can take in order to manage epistemic and normative risk, rather than optimizing only surface-level preference or task utility [6]. FPO's refusal and clarification actions are exactly the behavioral outputs a validity boundary should trigger: when a query falls outside a model's validated chart, the framework of this paper provides the formal condition under which refusal is the correct action. The connection is one of interface, not of proof.

Out-of-distribution risk in a deployed clinical system. The radiotherapy workflow paper states that precision of contouring target structures and organs at risk is crucial for treatment efficacy and patient safety, that deep learning has significantly improved organ-at-risk contouring, and that reliability under out-of-distribution scenarios remains a concern in clinical settings [7]. This is the clearest supplied instance of the real-world problem of Section 1: a validated model deployed near the edge of its domain, with no formal boundary drawn. The summary supplied gives no quantitative OOD results, so no performance figure from that work is used here.

Formal specification and the limits of checking intent. For verification-aware programming languages such as Dafny and F*, the summary states that although checking an implementation against a specification is mechanical, there is no algorithmic way of ensuring the correctness of the user-intent formalization itself, because intent is not mechanically checkable against the informal wish [5]. This is an epistemic boundary in miniature: the validated object is the implementation-relative-to-specification, and the boundary is the unformalized gap between specification and intent. The present framework would represent the specification as a local chart whose validation domain excludes the intent relation.

Model interpretability as boundary probing. The white-box analysis of ColBERT dissects the matching process of a transformer-based ad-hoc information retrieval model through term importance and exact and soft matching patterns, in a setting where the summary notes that transformer models are state of the art but their behavior is far from understood, and that claims have been made that BERT does not satisfy the classical IR axioms, while the traditional axioms are not formally violated in the way claimed [3]. Axiom violations and their precise non-violations are boundary phenomena: the analysis locates where an opaque model's behavior departs from, and merely appears to depart from, a classical axiomatic local model. White-box dissection of this kind is a concrete technique for measuring a validation domain empirically.

Logical validity boundaries. The epistemic ATL work gives a validity-preserving translation from a subset of epistemic Alternating-time Temporal Logic to epistemic Computation Tree Logic; the subset has the finite model property and decidable model-checking, so validity is decidable, but the implied algorithm is unfeasible, and the reduction targets a corresponding CTL validity problem [8]. This supplies a precedent for the framework's central move: a property (validity) is preserved under a change of representation (the translation), and the cost of deciding it in one representation versus another is itself part of the epistemic geometry. The unfeasibility caveat is a boundary on the practical side of the reduction.

Arithmetic coherence across places. The regular formal moduli spaces paper defines formal moduli spaces of $p$-divisible groups that are regular, with morphisms between them, formulates arithmetic transfer conjectures as variants of the arithmetic fundamental lemma conjecture in the presence of ramification, and proves these conjectures in low-dimensional cases [4]. This is the mathematical source of the restricted-product analogy: local objects at different places, coherence conditions across them, and theorems that hold place by place before they hold globally. The summary supplied gives no further technical detail usable here, so the analogy is drawn only at the structural level stated.

Adelic selection principles for physics. The adelic consistency conditions program addresses the three constants problem, namely why the fine-structure constant takes its observed value, why charged-lepton masses are hierarchically spaced, and what fixes the absolute mass scale, for which there is no accepted resolution within the Standard Model; it develops the adelic idea as a testable conjecture with a negative control and toy dynamics [11]. This is the closest prior statement of the adele analogy applied to empirical science, and the present paper differs in scope: [11] applies adelic coherence to the selection of physical constants, while this paper applies it to the validity boundaries of models in general and quantifies a worked example.

Corpus-level context. The QNFO entries for Philosophy of Science [9] and Epistemic Dynamics [10] are supplied without summary text; no claim about their content is made here, and they are cited only to mark the corpus context in which the research idea arose. Scale-Invariant Reality [12] is likewise supplied without a usable summary; its title indicates the invariance-under-representation theme that Section 3 formalizes, and nothing more is attributed to it.

## 3. Methods

### 3.1 Local charts and validation domains

Fix a phenomenon $\Phi$ and a space $X$ of observable outcomes. A local model is a pair

$$M = (f_M, D_M),$$

where $f_M : X \to Y_M$ is a predictive map into an output space $Y_M$ and $D_M \subseteq X$ is the validation domain: the set of inputs on which $f_M$ has been checked against $\Phi$ under a stated protocol and tolerance. The pair $(f_M, D_M)$ is the epistemic analogue of a chart in a manifold atlas: $f_M$ is the coordinate map and $D_M$ is the chart's open set. A model is validated on $D_M$ and silent, in the sense of having no earned guarantee, on $X \setminus D_M$.

The validation protocol is part of the model. Two models with the same $f_M$ but different $D_M$ are different epistemic objects, because the boundary is the object of study here.

### 3.2 Compatibility and the restricted product

Let $\mathcal{R}$ be a set of representations. A representation is a choice of encoding of $X$ and $Y$: radix, metric, parametrization, observer frame, or discretization. For each representation $r \in \mathcal{R}$ there is a family of local models $\{M_{r,i}\}_i$ validated in that representation.

Two local models $M$ and $M'$ are compatible on an overlap $U \subseteq D_M \cap D_{M'}$ if their predictions agree within a stated tolerance $\epsilon$:

$$\sup_{x \in U} d_Y\big(f_M(x), f_{M'}(x)\big) \le \epsilon.$$

The adele-like object is the restricted product

$$\mathbb{M}_{\mathcal{R}} = \prod_{r \in \mathcal{R}}{}' \mathcal{M}_r,$$

the set of tuples $(M_r)_{r \in \mathcal{R}}$ with $M_r$ a validated local model in representation $r$, such that $M_r$ is trivial (identical to a fixed reference model of that representation) for all but finitely many $r$. The restriction is what makes the product manageable, exactly as the restricted product over primes makes the adele ring locally compact where the full direct product would not be. A global statement about $\Phi$ is admissible if it is a property $P$ such that every compatible tuple in $\mathbb{M}_{\mathcal{R}}$ satisfies $P$ on the intersection of its validation domains.

An incompatibility between two well-validated models with overlapping domains, such as the standing tension between quantum mechanics and general relativity, is then a pair of charts that cannot be embedded in one compatible tuple. Under the framework's central conjecture, such incompatibilities mark structured edges of ignorance: places where the missing global object would be required to reconcile the local truths, and therefore places where extrapolation is expected to fail.

### 3.3 The invariant core

Define an admissible change of representation as a map $g$ between representations that preserves the validation protocol. The invariant core of a model class $\mathcal{C}$ is

$$\operatorname{Inv}(\mathcal{C}) = \bigcap_{g} \big\{ \text{quantities } q \text{ of } \mathcal{C} : q(gM) = q(M) \text{ for all } M \in \mathcal{C} \big\}.$$

The framework's second claim is that the robust known is exactly $\operatorname{Inv}(\mathcal{C})$: quantities invariant under representation change are exactly those one is entitled to extrapolate beyond $D_M$, while the leading non-invariant quantity measures the distance to the boundary. Section 4 computes both for the worked example.

### 3.4 Worked example: the Poisson-to-Gaussian max-entropy bridge

The test case is the passage from a Poisson counting model to a Gaussian continuous model. Among distributions on $\mathbb{R}$ with fixed mean $\mu$ and variance $\sigma^2$, the Gaussian maximizes differential entropy; among distributions on $\{0,1,2,\dots\}$ with fixed mean $\lambda$, the Poisson is the corresponding max-entropy object for counting processes. The Gaussian with $\mu = \sigma^2 = \lambda$ is therefore the max-entropy continuous representation of the Poisson counting model, and the bridge between them is a change of representation in the sense of Section 3.1. The question the framework must answer quantitatively is: over what region of outcome space does the Gaussian chart remain a valid representation of the Poisson chart, and what is the first quantity that fails to be invariant?

Throughout Section 4 the Poisson parameter is $\lambda = 100$, chosen so that all quantities are computable by hand with Stirling's approximation

$$\ln n! \approx n \ln n - n + \tfrac{1}{2}\ln(2\pi n) + \tfrac{1}{12n},$$

whose relative error in $\ln n!$ is of order $1/(360 n^4)$, negligible at the digit level used here.

## 4. Analysis

Every input number in this section is either a definition (the Poisson parameter $\lambda = 100$, the tolerance levels), a standard mathematical constant, or computed below from the stated formulas. No empirical data are used.

### 4.1 Input constants

The following constants are used, each to at least seven significant figures:

$$\ln 100 = 4.605170, \quad \ln 110 = 4.700480, \quad \ln 120 = 4.787492,$$
$$\ln 125 = 4.828314, \quad \ln 130 = 4.867534,$$
$$\ln(2\pi) = 1.837877, \quad \ln e = 1.$$

Derived per-case constants: $\ln(2\pi \cdot 100) = \ln(628.3185) = 1.837877 + \ln 100 = 1.837877 + 4.605170 = 6.443047$, and half of this is $3.221524$. This quantity $0.5\ln(2\pi\lambda) = 3.221524$ enters every Gaussian log-probability below.

### 4.2 Log-probability of the Poisson model at four deviations

The Poisson probability mass is $P(X = k) = e^{-\lambda}\lambda^k / k!$, so

$$\ln P(X = k) = -\lambda + k \ln \lambda - \ln k!.$$

The Gaussian density approximation at $k$ with $\mu = \sigma^2 = \lambda$ gives

$$\ln p_{\mathrm{G}}(k) = -\tfrac{1}{2}\ln(2\pi\lambda) - \frac{(k-\lambda)^2}{2\lambda}.$$

**Case $k = 110$ (one standard deviation, $x = (k-\lambda)/\sqrt{\lambda} = 1$).**

Stirling for $\ln 110!$:

- $110 \ln 110 = 110 \times 4.700480 = 517.0528$
- $-110$ gives $407.0528$
- $\tfrac{1}{2}\ln(2\pi \cdot 110) = \tfrac{1}{2}\ln(691.1504) = \tfrac{1}{2}(1.837877 + \ln 110) = \tfrac{1}{2}(1.837877 + 4.700480) = \tfrac{1}{2}(6.538357) = 3.269179$
- $\tfrac{1}{12 \cdot 110} = 1/1320 = 0.000758$

$$\ln 110! = 517.0528 - 110 + 3.269179 + 0.000758 = 410.3227.$$

Then

$$\ln P_{\mathrm{Pois}}(110) = -100 + 110 \times 4.605170 - 410.3227 = -100 + 506.5687 - 410.3227 = -3.7540.$$

Gaussian:

$$\ln p_{\mathrm{G}}(110) = -3.221524 - \frac{10^2}{200} = -3.221524 - 0.5 = -3.721524.$$

Log-difference:

$$\Delta_{1\sigma} = \ln P_{\mathrm{Pois}} - \ln p_{\mathrm{G}} = -3.7540 - (-3.721524) = -0.0325.$$

The Gaussian overestimates the Poisson log-probability by $0.0325$ nats at $1\sigma$, a relative error of $3.25\%$ in probability.

**Case $k = 120$ (two standard deviations, $x = 2$).**

- $120 \ln 120 = 120 \times 4.787492 = 574.4990$
- $-120$ gives $454.4990$
- $\tfrac{1}{2}\ln(2\pi \cdot 120) = \tfrac{1}{2}(1.837877 + 4.787492) = \tfrac{1}{2}(6.625369) = 3.312685$
- $1/1440 = 0.000694$

$$\ln 120! = 574.4990 - 120 + 3.312685 + 0.000694 = 457.8124.$$

$$\ln P_{\mathrm{Pois}}(120) = -100 + 120 \times 4.605170 - 457.8124 = -100 + 552.6204 - 457.8124 = -5.1920.$$

$$\ln p_{\mathrm{G}}(120) = -3.221524 - \frac{20^2}{200} = -3.221524 - 2 = -5.221524.$$

$$\Delta_{2\sigma} = -5.1920 - (-5.221524) = +0.0296.$$

At $2\sigma$ the Gaussian underestimates the Poisson log-probability by $0.0296$ nats, a relative error of $3.0\%$ in the opposite direction from the $1\sigma$ case.

**Case $k = 125$ ($x = 2.5$).**

- $125 \ln 125 = 125 \times 4.828314 = 603.5393$
- $-125$ gives $478.5393$
- $\tfrac{1}{2}\ln(2\pi \cdot 125) = \tfrac{1}{2}(1.837877 + 4.828314) = \tfrac{1}{2}(6.666191) = 3.333096$
- $1/1500 = 0.000667$

$$\ln 125! = 603.5393 - 125 + 3.333096 + 0.000667 = 481.8731.$$

$$\ln P_{\mathrm{Pois}}(125) = -100 + 125 \