# The Adele Analogy for Epistemic Boundaries: Local Models, a Restricted Product of Representations, and a Quantified Validity Radius

## Abstract

Scientific and engineering practice routinely deploys models outside the domains in which they were validated, leading to failures that are discovered only after costly consequences. Existing treatments of epistemic uncertainty flag that a prediction is uncertain but do not specify where a validated model stops being valid or which of its contents survive a change of representation. This paper fills that gap by formalizing an adele‑like framework in which each validated model is a “local completion” of an underlying phenomenon, carries an explicit validity boundary, and the robust core of a model class is exactly the set of quantities invariant under admissible changes of representation. Models are defined as local charts with validation domains, combined in a restricted product over representations, and the framework is tested on the Poisson‑to‑Gaussian max‑entropy bridge. With full arithmetic we show that at λ = 100 the Gaussian local model reproduces Poisson probabilities to within 3.3 % in log‑space at one standard deviation but underestimates the tail by a factor of 1.30 at three standard deviations. The 5 % log‑tolerance validity radius lies between 2σ and 2.5σ, and the leading non‑invariant quantity is the standardized skewness 1/√λ = 0.1. The result turns “we do not know” into a measured radius, applicable to out‑of‑distribution risk assessment.

## 1. Introduction

Clinicians who use automated contouring of organs at risk in radiotherapy planning face a concrete problem: deep‑learning contouring improves efficiency, yet reliability under out‑of‑distribution scenarios remains a stated clinical concern, and an unnoticed validity failure can produce a treatment plan that harms a patient [7]. The cost of not drawing a model’s validity boundary is twofold. First, a radiotherapy team must either apply costly manual review everywhere or accept unquantified risk [7]. Second, autonomous reasoning systems that aggregate scientific claims need to know when a well‑supported local consensus stops supporting a global conclusion, a need already recognized by belief‑aggregation architectures [1]. If the framework proposed here holds, every model would carry a machine‑readable validity boundary expressed as a radius in a deviation coordinate, calibrated by explicit arithmetic (Section 4). Incompatibilities between well‑validated models would be classified as structured edges of ignorance rather than defects, and the robust content of a model class would be identified by an invariance test: what survives a change of representation is what one may safely extrapolate.

**Contributions.**
- Formal definitions: models as local charts with explicit validation domains, a compatibility relation, and an adele‑like restricted product over representations (Section 3).  
- Invariance criterion: the invariant core of a model class is the set of quantities unchanged under admissible representation changes, with the first non‑invariant term computable as a cumulant ratio (Section 4).  
- Quantified validity radius for the Poisson‑to‑Gaussian max‑entropy bridge: log‑probability discrepancies of 0.0325 nats at 1σ, 0.0296 nats at 2σ, 0.1197 nats at 2.5σ, and a factor 1.30 underestimate at 3σ; the 5 % log‑tolerance radius is bracketed by 2σ < R < 2.5σ (Sections 4–5).  
- Mapping of the framework onto existing epistemic‑uncertainty practice, technology‑readiness assessment, and the smallest falsifying experiment (Sections 6–7).

## 2. Background and Related Work

Formal epistemic architectures such as Bayesian Epistemology with Weighted Authority (BEWA) operationalise belief as a dynamic, probabilistically coherent function over structured scientific claims [1]. BEWA supplies the aggregation layer that a science of epistemic boundaries would sit on top of: aggregation tells how to combine validated local models, while the present framework tells where each local model’s validity ends.

Task‑vector interference research characterises “validity boundaries” as measurable functional quantities that depend jointly on task pairs and input distributions, and shows that these boundaries are exposed when models are evaluated under format changes [1]. This provides an empirical analogue of the boundary concept that the present framework formalises.

The Decision‑Oriented Technique (DOTechnique) defines model validity as the region in which a surrogate model yields decisions equivalent to a high‑validity model, and warns that applying a model beyond its defined region introduces significant risk [4]. This directly motivates the need for a quantified validity radius.

Stable‑but‑Wrong demonstrates that accumulating more data can degrade scientific conclusions when an unobservable drift degrades observation validity, exposing a structural epistemic trap [5]. This illustrates why a formal boundary, rather than a naïve data‑quantity heuristic, is essential.

Position: Certifiable State Integrity argues that local validity specifications are more useful than a single global scale for safety‑critical cyber‑physical systems, and that local evidence boundaries can be traced and composed [7]. This supports the adele‑like restricted product idea, where each local chart contributes coherent evidence.

Task‑vector interference also notes that validity boundaries can be “seed‑stable” and measurable, reinforcing that boundaries are not merely abstract but can be quantified [1].

The combinatorial one‑cocycle work constructs a 1‑cocycle in a moduli space of knots, providing a concrete example of an invariant structure that survives representation changes [2]. This motivates the invariant‑core notion.

The classification of unitary elements of C*‑algebras shows that representation‑invariant quantities (e.g., K‑theory classes) can be identified across different morphisms [3]. This parallels the identification of invariant quantities across model representations.

Improving problem solving by exploiting symmetry demonstrates that changing the representation of a problem (via symmetry transformations) can preserve solution structure while exposing non‑invariant aspects [6]. This illustrates the relevance of representation change to epistemic boundaries.

The Annotation Scarcity Paradox surveys how evaluation bottlenecks limit epistemic confidence in low‑resource NLP, highlighting a structural limitation on what can be known [9]. This underscores the practical importance of formally delineating knowledge boundaries.

## 3. Methods

### 3.1 Local charts and validation domains

Fix a phenomenon Φ and a space X of observable outcomes. A local model is a pair  

$$M = (f_M, D_M),$$  

where $f_M : X \to Y_M$ is a predictive map into an output space $Y_M$ and $D_M \subseteq X$ is the validation domain: the set of inputs on which $f_M$ has been checked against Φ under a stated protocol and tolerance. The pair $(f_M, D_M)$ is the epistemic analogue of a chart in a manifold atlas: $f_M$ is the coordinate map and $D_M$ is the chart’s open set. A model is validated on $D_M$ and silent on $X \setminus D_M$.

The validation protocol is part of the model. Two models with the same $f_M$ but different $D_M$ are different epistemic objects because the boundary is the object of study.

### 3.2 Compatibility and the restricted product

Let $\mathcal{R}$ be a set of representations (radix, metric, observer frame, etc.). For each $r \in \mathcal{R}$ there is a family of local models $\{M_{r,i}\}_i$ validated in that representation.

Two local models $M$ and $M'$ are compatible on an overlap $U \subseteq D_M \cap D_{M'}$ if their predictions agree within a tolerance $\epsilon$:  

$$\sup_{x \in U} d_Y\bigl(f_M(x), f_{M'}(x)\bigr) \le \epsilon.$$

The adele‑like object is the restricted product  

$$\mathbb{M}_{\mathcal{R}} = \prod_{r \in \mathcal{R}}{}' \mathcal{M}_r,$$  

the set of tuples $(M_r)_{r \in \mathcal{R}}$ with $M_r$ a validated local model in representation $r$, such that $M_r$ is trivial (identical to a fixed reference model of that representation) for all but finitely many $r$. The restriction makes the product manageable, exactly as the restricted product over primes makes the adele ring locally compact.

A global statement about Φ is admissible if it is a property $P$ such that every compatible tuple in $\mathbb{M}_{\mathcal{R}}$ satisfies $P$ on the intersection of its validation domains. An incompatibility between two well‑validated models with overlapping domains is then a pair of charts that cannot be embedded in one compatible tuple. Under the central conjecture, such incompatibilities mark structured edges of ignorance: places where the missing global object would be required to reconcile the local truths, and therefore places where extrapolation is expected to fail.

### 3.3 The invariant core

Define an admissible change of representation as a map $g$ between representations that preserves the validation protocol. The invariant core of a model class $\mathcal{C}$ is  

$$\operatorname{Inv}(\mathcal{C}) = \bigcap_{g} \bigl\{ q \text{ of } \mathcal{C} : q(gM) = q(M) \text{ for all } M \in \mathcal{C} \bigr\}.$$

The second claim of the framework is that the robust known is exactly $\operatorname{Inv}(\mathcal{C})$: quantities invariant under representation change are those one is entitled to extrapolate beyond $D_M$, while the leading non‑invariant quantity measures the distance to the boundary. Section 4 computes both for the worked example.

### 3.4 Worked example: the Poisson‑to‑Gaussian max‑entropy bridge

The test case is the passage from a Poisson counting model to a Gaussian continuous model. Among distributions on $\mathbb{R}$ with fixed mean $\mu$ and variance $\sigma^2$, the Gaussian maximises differential entropy; among distributions on $\{0,1,2,\dots\}$ with fixed mean $\lambda$, the Poisson is the corresponding max‑entropy object. Setting $\mu = \sigma^2 = \lambda$ yields the Gaussian as the max‑entropy continuous representation of the Poisson counting model. The question is: over what region of outcome space does the Gaussian chart remain a valid representation of the Poisson chart, and what is the first quantity that fails to be invariant?

Throughout Section 4 the Poisson parameter is $\lambda = 100$, chosen so that all quantities are computable by hand with Stirling’s approximation  

$$\ln n! \approx n \ln n - n + \tfrac12 \ln(2\pi n) + \tfrac{1}{12n},$$  

whose relative error is $O(1/(360 n^3))$, negligible at the digit level used here.

## 4. Analysis

Every input number in this section is either a definition (the Poisson parameter $\lambda = 100$, the tolerance levels), a standard mathematical constant, or computed below from the stated formulas. No empirical data are used.

### 4.1 Input constants

The following constants are used, each to at least seven significant figures:

$$\ln 100 = 4.605170,\quad \ln 110 = 4.700480,\quad \ln 120 = 4.787492,$$
$$\ln 125 = 4.828314,\quad \ln 130 = 4.867534,$$
$$\ln(2\pi) = 1.837877,\quad \ln e = 1.$$

Derived per‑case constant:  

$$0.5\ln(2\pi\lambda) = 0.5\bigl(\ln(2\pi) + \ln\lambda\bigr) = 0.5(1.837877 + 4.605170) = 3.221524.$$

### 4.2 Log‑probability of the Poisson model at four deviations

The Poisson probability mass is  

$$P(X = k) = e^{-\lambda}\lambda^k / k!,$$  

so  

$$\ln P(X = k) = -\lambda + k\ln\lambda - \ln k!.$$

The Gaussian density approximation at $k$ with $\mu = \sigma^2 = \lambda$ gives  

$$\ln p_{\mathrm{G}}(k) = -\tfrac12\ln(2\pi\lambda) - \frac{(k-\lambda)^2}{2\lambda}.$$

#### Case $k = 110$ ($x = 1$)

Stirling for $\ln 110!$:

- $110\ln110 = 110 \times 4.700480 = 517.0528$  
- $-110$ gives $407.0528$  
- $\tfrac12\ln(2\pi\cdot110) = \tfrac12(1.837877 + 4.700480) = 3.269179$  
- $\tfrac{1}{12\cdot110}=0.000758$

$$\ln 110! = 517.0528 - 110 + 3.269179 + 0.000758 = 410.3227.$$

Then  

$$\ln P_{\mathrm{Pois}}(110) = -100 + 110\times4.605170 - 410.3227 = -3.7540.$$

Gaussian:  

$$\ln p_{\mathrm{G}}(110) = -3.221524 - \frac{10^2}{200} = -3.721524.$$

Log‑difference  

$$\Delta_{1\sigma} = -3.7540 - (-3.721524) = -0.0325.$$

The Gaussian overestimates the Poisson log‑probability by 0.0325 nats, a relative error of $e^{0.0325}-1 = 0.0330$ (3.3 %).

#### Case $k = 120$ ($x = 2$)

- $120\ln120 = 120 \times 4.787492 = 574.4990$  
- $-120$ gives $454.4990$  
- $\tfrac12\ln(2\pi\cdot120) = \tfrac12(1.837877 + 4.787492) = 3.312685$  
- $1/(12\cdot120)=0.000694$

$$\ln 120! = 574.4990 - 120 + 3.312685 + 0.000694 = 457.8124.$$

$$\ln P_{\mathrm{Pois}}(120) = -100 + 120\times4.605170 - 457.8124 = -5.1920.$$

$$\ln p_{\mathrm{G}}(120) = -3.221524 - \frac{20^2}{200} = -5.221524.$$

$$\Delta_{2\sigma} = -5.1920 - (-5.221524) = +0.0296.$$

The Gaussian underestimates the Poisson log‑probability by 0.0296 nats (≈3.0 % relative error).

#### Case $k = 125$ ($x = 2.5$)

- $125\ln125 = 125 \times 4.828314 = 603.5393$  
- $-125$ gives $478.5393$  
- $\tfrac12\ln(2\pi\cdot125) = \tfrac12(1.837877 + 4.828314) = 3.333096$  
- $1/(12\cdot125)=0.000667$

$$\ln 125! = 603.5393 - 125 + 3.333096 + 0.000667 = 481.8731.$$

$$\ln P_{\mathrm{Pois}}(125) = -100 + 125\times4.605170 - 481.8731 = -6.2268.$$

$$\ln p_{\mathrm{G}}(125) = -3.221524 - \frac{25^2}{200} = -6.346524.$$

$$\Delta_{2.5\sigma} = -6.2268 - (-6.346524) = +0.1197.$$

Relative error $e^{0.1197}-1 = 0.127$ (12.7 %).

#### Case $k = 130$ ($x = 3$)

- $130\ln130 = 130 \times 4.867534 = 632.7794$  
- $-130$ gives $502.7794$  
- $\tfrac12\ln(2\pi\cdot130) = \tfrac12(1.837877 + 4.867534) = 3.352706$  
- $1/(12\cdot130)=0.000641$

$$\ln 130! = 632.7794 - 130 + 3.352706 + 0.000641 = 506.1328.$$

$$\ln P_{\mathrm{Pois}}(130) = -100 + 130\times4.605170 - 506.1328 = -7.4607.$$

$$\ln p_{\mathrm{G}}(130) = -3.221524 - \frac{30^2}{200} = -7.721524.$$

$$\Delta_{3\sigma} = -7.4607 - (-7.721524) = +0.2608.$$

Probability ratio $e^{0.2608}=1.298$, i.e. a factor 1.30 underestimate.

### 4.3 Leading‑order asymptotics and the residual pattern

Substituting $k = \lambda + x\sqrt{\lambda}$ into the Stirling‑based log‑probability and expanding yields  

$$\ln P_{\mathrm{Pois}}(k) = -\frac{x^2}{2} - \tfrac12\ln(2\pi\lambda) + \frac{x^3 - 3x}{6\sqrt{\lambda}} + O(\lambda^{-1}).$$  

The first two terms equal the Gaussian log‑density $\ln p_{\mathrm{G}}(k)$. Hence the leading discrepancy is  

$$\Delta(x) \approx \frac{x^3 - 3x}{6\sqrt{\lambda}}.$$

Evaluating this cubic law at the four computed $x$ values gives the table below (all numbers in nats):

| $x$ | cubic prediction $(x^3-3x)/60$ | computed $\Delta$ | residual |
|---|---|---|---|
| $1$ | $-0.0333$ | $-0.0325$ | $0.0008$ |
| $2$ | $+0.0333$ | $+0.0296$ | $0.0037$ |
| $2.5$ | $+0.1354$ | $+0.1197$ | $0.0157$ |
| $3$ | $+0.3000$ | $+0.2608$ | $0.0392$ |

Residuals grow with $x$ because omitted $O(\lambda^{-1})$ terms are of order $x^4/\lambda$ and $x^6/\lambda^2$.

### 4.4 The invariant core: cumulants under the representation change

For the Poisson distribution with parameter $\lambda$, the cumulant generating function is $\ln E[e^{tX}] = \lambda(e^t - 1)$, so every cumulant equals $\lambda = 100$:

$$\kappa_1 = \kappa_2 = \kappa_3 = \kappa_4 = \dots = 100.$$

For the Gaussian $\mathcal{N}(\lambda,\lambda)$, the cumulant generating function is $\ln E[e^{tY}] = \lambda t + \lambda t^2/2$, giving  

$$\kappa_1 = 100,\quad \kappa_2 = 100,\quad \kappa_n = 0 \text{ for } n\ge 3.$$

Thus the representation‑invariant quantities are the mean and variance (both 100). The first non‑invariant quantity is the third cumulant, i.e. the skewness  

$$\gamma_1 = \frac{\kappa_3}{\kappa_2^{3/2}} = \frac{1}{\sqrt{\lambda}} = 0.1,$$

which is zero for the Gaussian. The excess kurtosis $1/\lambda = 0.01$ is the next excluded quantity. The coefficient $\gamma_1/6$ appears in the cubic discrepancy law, confirming that the leading non‑invariant cumulant predicts the shape and scale of the out‑of‑domain error.

### 4.5 The validity radius

Fix a log‑tolerance $\epsilon = 0.05$. The Gaussian chart is declared valid at deviation $x$ if $|\Delta(x)| \le \epsilon$. From the computed points:

- $|\Delta(1)| = 0.0325 \le 0.05$ (valid)  
- $|\Delta(2)| = 0.0296 \le 0.05$ (valid)  
- $|\Delta(2.5)| = 0.1197 > 0.05$ (invalid)

Hence the 5 % log‑tolerance radius lies strictly between $2\sigma$ and $2.5\sigma$. Two labeled projections refine the estimate.

**Projection 1 (linear interpolation).**  

$$x_{\epsilon} = 2 + 0.5 \times \frac{0.05 - 0.0296}{0.1197 - 0.0296}
= 2 + 0.5 \times \frac{0.0204}{0.0901}
= 2.113.$$

**Projection 2 (cubic law).** Solve $(x^3 - 3x)/60 = 0.05$, i.e. $x^3 - 3x - 3 = 0$. Linear interpolation between $x=2.10$ (value $-0.039$) and $x=2.11$ (value $+0.064$) yields  

$$x \approx 2.10 + 0.01 \times \frac{0.039}{0.103} = 2.104.$$

Both projections give $R \approx 2.1\sigma$, with the exact bracket $2\sigma < R_{0.05} < 2.5\sigma$ remaining rigorous. The cubic law predicts a scaling $R \propto \lambda^{1/6}$ for large $\lambda$; for $\lambda=100$ this gives $R \approx 1.44\sigma$, underestimating the true root because the $-3x$ term is non‑negligible.

## 5. Results

All numbers below are those computed with shown arithmetic in Section 4; the two interpolated radii are labeled projections with their assumptions stated in Section 4.5.

**R1. Log‑probability discrepancies ($\lambda=100$).**  
- $1\sigma$: $\Delta = -0.0325$ nats (Gaussian overestimates by factor $e^{0.0325}=1.033$).  
- $2\sigma$: $\Delta = +0.0296$ nats (Gaussian underestimates by factor $e^{0.0296}=1.030$).  
- $2.5\sigma$: $\Delta = +0.1197$ nats (relative error $12.7\%$).  
- $3\sigma$: $\Delta = +0.2608$ nats (factor 1.30 underestimate).

**R2. Deterministic cubic law.** The discrepancies follow $\Delta(x) \approx (x^3-3x)/(6\sqrt{\lambda})$ with residuals $0.0008$, $0.0037$, $0.0157$, $0.0392$ at $x=1,2,2.5,3$, consistent with the $O(\lambda^{-1})$ remainder.

**R3. Invariant core and first excluded quantity.** The invariant core consists of mean $\kappa_1=100$ and variance $\kappa_2=100$. The first non‑invariant quantity is the skewness $\gamma_1=0.1$, whose coefficient $\gamma_1/6$ appears in the cubic discrepancy law.

**R4. Validity radius.** The $5\%$ log‑tolerance radius is bracketed by $2\sigma < R_{0.05} < 2.5\sigma$. Linear interpolation gives $R_{0.05}=2.113\sigma$, the cubic law gives $R_{0.05}=2.104\sigma$, and both agree on $R \approx 2.1\sigma$. The scaling prediction $R \propto \lambda^{1/6}$ implies a hundredfold increase in $\lambda$ widens the radius by a factor $100^{1/6}=2.154$.

**R5. Shape of the failure.** The Gaussian chart underestimates right‑tail Poisson probabilities beyond $x\approx\sqrt{3}=1.732$, and the underestimate grows cubically, reaching a 30 % tail error at $3\sigma$.

## 6. Discussion

The worked example supports the framework’s two operational claims in a limited but precise way. The invariant‑core claim survived its first test in the strong sense: the excluded skewness $0.1$ is not merely correlated with the boundary failure but is the coefficient that predicts the cubic error law. The validity‑radius claim survived in the weaker sense: the radius is bracketed rather than exactly computed; the fine value rests on interpolation.

### Limitations

- **Stirling truncation.** Using Stirling through the $1/(12n)$ term introduces a next‑order error of $O(1/(360 n^3))$, which at $n=110$ is $2.1\times10^{-9}$ nats, negligible for all reported digits.  
- **Input log constants.** Logarithms are given to six decimal places; the induced uncertainty is at most $6\times10^{-5}$ nats, below the smallest residual ($0.0008$ nats).  
- **Single parameter value.** All computations use $\lambda=100$. The cubic law and $\lambda^{1/6}$ scaling are derived asymptotically but tested at only one point; the generality of the pattern remains a conjecture.  
- **Interpolated radius.** The fine radius $R\approx2.1\sigma$ is a projection from two interpolation schemes; the exact radius could shift by a few hundredths of σ.  
- **Tolerance choice.** The radius depends on the chosen $\epsilon=0.05$; different tolerances move the radius by construction.  
- **Single worked example.** Demonstrating the link between the first non‑invariant cumulant and the leading error term for one representation change does not prove the claim for arbitrary model classes.

### What would falsify the main result

1. Evaluating $\Delta$ at a new deviation, e.g. $x=2.25$ ($k=122$ or 123), and obtaining a value that deviates from the cubic prediction $(x^3-3x)/60$ by more than the established residual trend would falsify the deterministic law.  
2. Computing exact Poisson log‑probabilities with full‑precision arithmetic and finding discrepancies larger than $10^{-4}$ nats relative to the hand‑computed values would invalidate the derivations.  
3. Repeating the computation at a different $\lambda$ (e.g. $\lambda=400$) and observing that $\Delta(3)$ does not scale as $1/\sqrt{\lambda}$ (the cubic law predicts $\Delta(3)=0.15$ nats) would falsify the claimed scaling and the identification of skewness as the governing quantity.

### Open questions

- Does the restricted‑product structure of Section 3.2 support a locality theorem analogous to local compactness for model classes?  
- Are incompatibilities between well‑validated models always recoverable as a missing global object, or can they indicate genuine inconsistency?  
- Can the invariant‑core criterion be extended beyond cumulant‑based probes to models lacking an exponential‑family structure?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.**  
- **Clinical‑ML deployment teams** (e.g. radiotherapy contouring) would replace a binary “in‑distribution / out‑of‑distribution” flag with a measured validity radius $R_\epsilon$ in a deviation coordinate; manual review would be triggered only when the operating point approaches $R_\epsilon$.  
- **Belief‑aggregation architectures** such as BEWA would consume the radius as structured metadata, weighting claims by their distance from the validation boundary.  
- **Language‑model policy systems** employing Frictive Policy Optimization would use the radius as the formal trigger for refusal or clarification actions.  
- For users that cannot yet be named, the work is foundational: it provides a definition of epistemic boundaries and a concrete method to compute them, enabling future tooling.

**(b) Current readiness.** Analytical work that has not been peer reviewed resides at TRL 1–2 (basic principles observed and formulated; concept stated without feasibility proof). Analytical work never exceeds TRL 3; no claim of implementation, manufacturing, or deployment readiness is made.

**(c) The smallest next experiment.** Compute the log‑probability discrepancy at a new deviation $x=2.25$ for $\lambda=100$ and at $x=3$ for $\lambda=400$. Measure $\Delta$ and compare to the cubic predictions $0.0773$ nats (first case) and $0.15$ nats (second case). A result inconsistent with the cubic law beyond the residual trend would falsify the main claim. This requires only a one‑line script and no data collection.

**(d) Binding constraints.**  
1. **Design of deviation coordinate** for real model classes (e.g. neural networks) where an analogue of $(k-\lambda)/\sqrt{\lambda}$ is not given.  
2. **Calibration of tolerance $\epsilon$** per application; this is a policy input, not derivable from the framework.  
3. **Empirical calibration** of $R_\epsilon$ on real validation sets, requiring data and compute.  
4. **Regulatory acceptance** of a radius‑based review trigger in safety‑critical domains, an open question not addressed by the supplied grounding.

**(e) Order‑of‑magnitude performance bound (projection).** Under the cubic law with the pure‑cubic regime $x^3 \gg 3x$, the validity radius scales as $R \propto \lambda^{1/6}$. Thus a hundredfold increase in the sample‑size‑like parameter $\lambda$ widens the radius by a factor $100^{1/6}=2.154$. Assumptions: large $\lambda$, fixed tolerance $\epsilon=0.05$, exponential‑family setting.

**(f) Risks and misuse paths.** A team could misrepresent the interpolated radius $R\approx2.1\sigma$ as an exact, validated boundary, thereby reducing manual review below a safe level. Because the radius is tolerance‑relative, choosing a looser $\epsilon$ artificially inflates the radius without improving model fidelity. Mitigation requires disclosing the tolerance,