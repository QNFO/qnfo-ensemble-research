# The Adele Analogy for Epistemic Boundaries: Local Models, a Restricted Product of Representations, and a Quantified Validity Radius

## Abstract

Scientific and engineering practice routinely deploys models outside the domains in which they were validated, and the resulting failures are usually discovered only after the fact. Existing treatments of epistemic uncertainty flag that a prediction is uncertain but do not say where a validated model stops being valid, or which parts of its content survive a change of representation. This paper develops a formal framework, modeled on the adele ring, in which each validated model is a "local completion" of an underlying phenomenon, each carries an explicit validity boundary, and the robust content of a model class is exactly what is invariant under changes of representation. Models are formalized as local charts with validation domains, combined in a restricted product over representations, and the framework is tested on the Poisson-to-Gaussian max-entropy bridge. With full arithmetic, the paper shows that at $\lambda = 100$ the Gaussian local model reproduces Poisson probabilities to within $3.3\%$ in log-space at one standard deviation but fails by a factor of $1.30$ at three standard deviations, locating the $5\%$ log-tolerance validity radius between $2\sigma$ and $2.5\sigma$ with a projected value near $2.1\sigma$, and identifies the skewness $1/\sqrt{\lambda} = 0.1$ as the leading representation-dependent quantity excluded from the invariant core. The framework turns "we do not know" into a measured radius, applicable to out-of-distribution risk assessment.

## 1. Introduction

Deep-learning models and statistical models are now validated on a dataset or a regime and then deployed on inputs that lie outside that regime, and the point at which they stop being trustworthy is not marked anywhere in the deployed artifact. Engineers who certify models for safety-critical cyber-physical systems face exactly this problem: globally parameterized dynamics models must remain valid through regime shifts, degradation, and lifecycle updates, and a misapplied model can invalidate results or decisions [4], [7]. The cost of not drawing the boundary is concrete. A team that cannot distinguish "the model is interpolating within its validated domain" from "the model is extrapolating" must either apply costly review everywhere or accept unquantified risk; [4] motivates its own technique with the observation that applying a model beyond the region where it reliably predicts introduces significant risks, because accuracy and reliability are no longer guaranteed.

The problem is not confined to engineering. [5] shows a regime in which standard inference procedures converge smoothly, remain well calibrated, and yet systematically diverge from the truth when the validity of observations degrades in a way that cannot be internally diagnosed; in that regime, additional data amplify rather than correct the error. Stability inside a model's working regime is therefore not evidence about what happens across its boundary, and a science that reads stability as correctness inherits a structural failure mode. In a different direction, [9] documents that the human expertise needed to evaluate increasingly complex generative systems trails far behind the capacity to generate model outputs, so the validated domain of any model is itself a scarce resource: every query spent re-validating inside the known domain is a query not spent mapping the boundary. All three situations call for the same missing capability: an explicit, computable statement of where a validated model's guarantees end, and of which parts of the model's content survive a change of representation.

If the framework proposed here holds, that capability becomes available in a specific form. Every model would carry a machine-readable validity boundary, stated as a radius in the space of deviations from the validation regime, calibrated by explicit arithmetic of the kind performed in Section 4. Incompatibilities between well-validated models would be classified not as defects but as structured edges of ignorance that indicate where a deeper global object is missing. And the robust content of a model class would be identified by an invariance test: what survives a change of representation is what one is entitled to extrapolate.

The analogy that organizes the framework is the adele ring of number theory. The adele ring $\mathbb{A}$ combines, for every prime $p$, a local field $\mathbb{Q}_p$ with the real completion $\mathbb{R}$, in a restricted product: an element of $\mathbb{A}$ is a tuple of local elements that is a $p$-adic integer for all but finitely many $p$. No single local field contains the arithmetic of the rationals; the global object is recovered only by imposing coherence across all local completions simultaneously. The present paper transfers this structural idea from arithmetic to epistemology: each validated model is a local completion, the unknown is the missing global object, and the boundary of a model is the region where its local coherence with other validated models fails. A prior statement of the framework [12] defined the local charts, the restricted product, and the validity radius, and computed the Poisson-to-Gaussian worked example; this paper carries that arithmetic forward in full, strengthens the connection between the invariant core and the boundary failure, and maps the framework onto current practice in model validation.

The paper's contributions are:

- A formal definitions layer: models as local charts with explicit validation domains, a compatibility relation, and an adele-like restricted product over representations, given in Section 3.
- An invariance criterion for robust knowledge: the invariant core of a model class is what is unchanged under admissible changes of representation, with the first non-invariant term computable as a cumulant ratio, derived in Section 4.
- A quantified validity radius for the Poisson-to-Gaussian max-entropy bridge: log-probability discrepancies of $0.0325$ nats at $1\sigma$, $0.0296$ nats at $2\sigma$, $0.1197$ nats at $2.5\sigma$, and a factor of $1.30$ at $3\sigma$, all computed with shown arithmetic in Section 4 and reported in Section 5.
- A mapping of the framework onto existing model-validation practice and its users, with a technology-readiness assessment and the smallest falsifying experiment, given in Sections 6 and 7.

## 2. Background and Related Work

This section reviews the works it draws on and states, for each, the specific contribution its text supports.

**Measured validity boundaries in model composition.** [1] studies task arithmetic, which composes skills by adding weight displacements, and measures when that composition is functionally additive. Its results establish that task-vector interference is a measurable, seed-stable functional quantity that is jointly determined by the task pair and the input distribution, that its coarse ordering is predictable for unseen pairs before their adapters exist, and that its expression is gated by training-format serialization, so that a training-format wrapper can hide a twenty-fold contrast that execution benchmarks inherit. The phrase "measured validity boundaries" appears in its own conclusion, for additive composition specifically. This is the closest existing instance of the present framework's program executed end to end on a concrete model class: a validity boundary defined, measured, and shown to be invisible to the evaluations most commonly run. The present paper supplies the general definitions and the analytic worked example that such measurements instantiate.

**Coherence data across a space of local pictures.** [2] proves a conjecture of Thomas Fiedler that a formula based on the Vassiliev invariant $v_3$ defines a $1$-cocycle in a moduli space of knots in the solid torus, so that evaluating the cocycle on canonical loops yields new, nontrivial knot invariants; the construction proceeds through Gauss diagram formulas and an explicit contribution correspondence under Reidemeister move III. The structural relevance is exact: a cocycle is precisely the datum that certifies whether locally defined contributions glue to a globally consistent object, and [2] is a worked case in which the gluing condition is checked contribution by contribution under a local move. The restricted product of Section 3.2 plays the analogous role for model classes: the compatibility condition is the cocycle condition, and incompatibilities between well-validated charts are the obstructions to gluing.

**Invariants that classify, and where they stop.** [3] proves the existence part of the conjecture that the Cuntz semigroup classifies unitary elements of unital AF-algebras, under a mild adjustment of the functor, by constructing lifts of weakly semiprojective $\mathrm{Cu}$-morphisms; beyond the AF case it exhibits two unitary elements in $\mathcal{C}([0,1])\otimes M_{2^\infty}$ that agree at the level of the classifying invariant yet fail to be approximately unitarily equivalent. This pair of results is an invariant core with a validity boundary in pure mathematics: inside the AF domain the invariant is complete, and the first step outside it the invariant core demonstrably fails to determine the object. The framework of Section 3.3 generalizes the pattern: an invariant core is complete on a validated domain and its first failure marks the boundary.

**Validity found through decisions, not outputs.** [4] introduces the Decision Oriented Technique (DOTechnique), which determines model validity by decision consistency rather than output similarity: surrogate models are compared to a high-validity model by whether they yield equivalent decisions, which allows validity regions to be discovered even when traditional predefined validity frames are absent. Its motivating example is a lane-change control algorithm with a computationally expensive high-validity model and cheaper surrogates, and its conclusion acknowledges that a single case study may not support broader generalization. DOTechnique is an empirical, decision-level procedure for tracing the boundary $D_M$ that Section 3.1 defines abstractly; the two are complementary, with [4] supplying the measurement protocol and the present framework the formal object being measured.

**Why stability inside the chart proves nothing across it.** [5] constructs a minimal synthetic setting with observations $y_t = \theta^* + \epsilon_t + b_t$, where $\epsilon_t \sim \mathcal{N}(0,1)$ is noise and $b_t$ is an unobservable bias following linear drift, random-walk drift, or no drift, and shows that inference with a stationary Gaussian likelihood that does not model drift can remain stable, convergent, and diagnostically normal while systematically diverging from the truth; crucially, additional data amplify the error rather than correcting it. The authors state the diagnosis precisely: when the validity of observations degrades in a manner that cannot be internally diagnosed, inference stability ceases to be a reliable indicator of correctness. This is the strongest available argument for the present framework's central bookkeeping move: the validation domain must be an explicit part of the model, because behavior inside the domain carries no information about the domain's edge.

**Local validity as an architectural principle.** [7] argues that certifiable state integrity in safety-critical cyber-physical systems should be built from local validity rather than global scale. It identifies structural challenges of global parameterization — regime separation at transitions, where global reduced representations converge slowly while local reduced-order models improve approximation efficiency — and proposes a Local Compressibility Condition as a testable precondition, together with a falsifiable evaluation plan that names its claims, its disconfirming results, and its minimum reported measurements, including Time-to-Uncertainty for coverage rejection. The present framework shares the architecture: local charts with explicit validity, a compatibility condition at their overlaps, and a monitor that turns unsupported operation into a testable event. Section 7 uses the evaluation vocabulary of [7] as one template for how a validity radius would be tested in deployment.

**Validity domains as explicit hypotheses.** [8] proves an existence theorem for two-phase two-component flow in porous media under explicitly stated assumptions, including bounded porosity $\phi_m \leq \Phi(x) \leq \phi_M$ and uniform ellipticity bounds on the permeability tensor, with the proof passing to the limit in regularizations and closing through the Leray-Schauder fixed point theorem. The example shows the standard form in which mathematics itself encodes validity: a theorem is valid on exactly the domain its hypotheses delimit, and the hypotheses are the theorem's validation domain. The framework of Section 3 asks that empirical and learned models carry the same explicit hypothesis structure.

**The scarcity of the validated domain itself.** [9] documents the Annotation Scarcity Paradox: over a decade, low-resource NLP evaluation has been bottlenecked not by training data but by the availability of qualified humans to verify outputs, and the authors argue this is a structural feature of the evaluation ecosystem that shapes what can be known. Read through the present framework, the validation domain $D_M$ is expensive to extend precisely because validation requires scarce expert judgment; a framework that predicts where the boundary lies, from structure alone as in Section 4, targets expert effort at the boundary instead of spreading it uniformly.

**Invariance under a change of chain representation.** [10] works toward a topological description of the Legendrian contact homology of unit conormal bundles, and its background material records the canonical isomorphism $\Psi_M$ between the singular homology $H^{\mathrm{sing}}_*(M)$ and the de Rham homology $H^{\mathrm{dR}}_*(M)$ of an oriented manifold, natural under smooth maps. This is the cleanest mathematical instance of the invariance principle of Section 3.3: the same invariant object is computed in two different chain representations, and the canonical natural isomorphism is the statement that the invariant core survives the change of representation exactly.

**Exact reduction under a stated constraint.** [11] shows that a stationary scalar correlation energy admits an exact one-mode terminal representation even when the microscopic correlated return is strongly multimode, tested in two two-electron systems with the same Coulomb repulsion but different confinement, He-like ions and harmonium. The reduction is exact only under the stationarity constraint; the constraint is the validity boundary of the reduced representation. This is the same shape as the Poisson-to-Gaussian bridge of Section 3.4: a reduced representation is faithful on a domain fixed by a stated condition and degrades off it.

**The prior version of this framework.** [12] is the paper under revision: it defines local charts and validation domains, the restricted product over representations, and the invariant core, and reports the Poisson-to-Gaussian arithmetic summarized in its Results section, including the discrepancies $-0.0325$, $+0.0296$, $+0.1197$, and $+0.2608$ nats and the bracket $2\sigma < R_{0.05} < 2.5\sigma$. The present paper is a remediation of [12]: the definitions and arithmetic of Sections 3 and 4 carry its content forward, and the related-work mapping is rebuilt around the works discussed above.

**Self-declared validity domains.** [13] proposes an epistemology, Epistemic Cartography, built on an axiom of strict separation between an ontological territory and epistemic maps, and — notably — includes a section in which the framework declares its own domain of validity, restricting itself to regimes where a stable statistical projection from territory to map is meaningful and predicting its own collapse near Planck-scale probes. A framework that states where it stops is itself an instance of the present framework's program; the present paper differs by making the boundary quantitative rather than declarative.

**The validation metric problem.** [14] deconstructs scientific progress into Generative (G-Type), Structural Unification (S-Type), and Epistemic Scaffolding (E-Type) contributions and identifies the Validation Metric Problem: S-Type and E-Type contributions lack the objective validation mechanism of direct empirical confrontation that adjudicates G-Type work. The present framework contributes one computable quantity of the kind [14] finds missing, for one class of claims about models: a validity radius with shown arithmetic and a stated falsification condition is a non-empirical claim that nonetheless carries an objective check.

## 3. Methods

### 3.1 Local charts and validation domains

Fix a phenomenon $\Phi$ and a space $X$ of observable outcomes. A local model is a pair

$$M = (f_M, D_M),$$

where $f_M : X \to Y_M$ is a predictive map into an output space $Y_M$ and $D_M \subseteq X$ is the validation domain: the set of inputs on which $f_M$ has been checked against $\Phi$ under a stated protocol and tolerance. The pair $(f_M, D_M)$ is the epistemic analogue of a chart in a manifold atlas: $f_M$ is the coordinate map and $D_M$ is the chart's open set. A model is validated on $D_M$ and silent, in the sense of having no earned guarantee, on $X \setminus D_M$.

The validation protocol is part of the model. Two models with the same $f_M$ but different $D_M$ are different epistemic objects, because the boundary is the object of study here. This bookkeeping requirement is not decorative: [5] demonstrates a regime in which all internal diagnostics of an inference procedure remain normal while the procedure diverges from the truth, so only an externally stated domain can carry the information that internal behavior does not.

### 3.2 Compatibility and the restricted product

Let $\mathcal{R}$ be a set of representations. A representation is a choice of encoding of $X$ and $Y$: radix, metric, parametrization, observer frame, or discretization. For each representation $r \in \mathcal{R}$ there is a family of local models $\{M_{r,i}\}_i$ validated in that representation.

Two local models $M$ and $M'$ are compatible on an overlap $U \subseteq D_M \cap D_{M'}$ if their predictions agree within a stated tolerance $\epsilon$:

$$\sup_{x \in U} d_Y\big(f_M(x), f_{M'}(x)\big) \le \epsilon.$$

The adele-like object is the restricted product

$$\mathbb{M}_{\mathcal{R}} = \prod_{r \in \mathcal{R}}{}' \mathcal{M}_r,$$

the set of tuples $(M_r)_{r \in \mathcal{R}}$ with $M_r$ a validated local model in representation $r$, such that $M_r$ is trivial (identical to a fixed reference model of that representation) for all but finitely many $r$. The restriction is what makes the product manageable, exactly as the restricted product over primes makes the adele ring locally compact where the full direct product would not be. A global statement about $\Phi$ is admissible if it is a property $P$ such that every compatible tuple in $\mathbb{M}_{\mathcal{R}}$ satisfies $P$ on the intersection of its validation domains.

An incompatibility between two well-validated models with overlapping domains is then a pair of charts that cannot be embedded in one compatible tuple. Under the framework's central conjecture, such incompatibilities mark structured edges of ignorance: places where the missing global object would be required to reconcile the local truths, and therefore places where extrapolation is expected to fail. The mathematical template for this conjecture is the cocycle: as [2] shows in the moduli space of knots, whether locally defined contributions glue to a global invariant is decided by a cocycle condition checked under local moves, and the failure of that condition is itself informative geometry.

### 3.3 The invariant core

Define an admissible change of representation as a map $g$ between representations that preserves the validation protocol. The invariant core of a model class $\mathcal{C}$ is

$$\operatorname{Inv}(\mathcal{C}) = \bigcap_{g} \big\{ \text{quantities } q \text{ of } \mathcal{C} : q(gM) = q(M) \text{ for all } M \in \mathcal{C} \big\}.$$

The framework's second claim is that the robust known is exactly $\operatorname{Inv}(\mathcal{C})$: quantities invariant under representation change are exactly those one is entitled to extrapolate beyond $D_M$, while the leading non-invariant quantity measures the distance to the boundary. The pattern has exact precedents. In homology theory the canonical isomorphism between singular and de Rham homology [10] states that the invariant core survives a change of chain representation exactly. In operator algebra, the Cuntz semigroup classifies unitary elements of unital AF-algebras completely [3], and the first step outside that domain the invariant demonstrably fails to determine the object [3]. In reduced quantum descriptions, the one-mode representation of a stationary correlation energy is exact under the stationarity constraint and its domain is fixed by that constraint [11]. Section 4 computes both the invariant core and the leading non-invariant quantity for the worked example.

### 3.4 Worked example: the Poisson-to-Gaussian max-entropy bridge

The test case is the passage from a Poisson counting model to a Gaussian continuous model. Among distributions on $\mathbb{R}$ with fixed mean $\mu$ and variance $\sigma^2$, the Gaussian maximizes differential entropy; among distributions on $\{0,1,2,\dots\}$ with fixed mean $\lambda$, the Poisson is the corresponding max-entropy object for counting processes. The Gaussian with $\mu = \sigma^2 = \lambda$ is therefore the max-entropy continuous representation of the Poisson counting model, and the bridge between them is a change of representation in the sense of Section 3.1. The question the framework must answer quantitatively is: over what region of outcome space does the Gaussian chart remain a valid representation of the Poisson chart, and what is the first quantity that fails to be invariant?

Throughout Section 4 the Poisson parameter is $\lambda = 100$, chosen so that all quantities are computable by hand with Stirling's approximation

$$\ln n! \approx n \ln n - n + \tfrac{1}{2}\ln(2\pi n) + \tfrac{1}{12n},$$

whose relative error in $\ln n!$ is of order $1/(360 n^3)$, negligible at the digit level used here.

## 4. Analysis

Every input number in this section is either a definition (the Poisson parameter $\lambda = 100$, the tolerance levels), a standard mathematical constant, or computed below from the stated formulas. No empirical data are used.

### 4.1 Input constants

The following constants are used, each to at least seven significant figures:

$$\ln 100 = 4.605170, \quad \ln 110 = 4.700480, \quad \ln 120 = 4.787492,$$
$$\ln 125 = 4.828314, \quad \ln 130 = 4.867534,$$
$$\ln(2\pi) = 1.837877, \quad \ln e = 1.$$

Derived per-case constant: $\ln(2\pi \cdot 100) = 1.837877 + \ln 100 = 1.837877 + 4.605170 = 6.443047$, and half of this is $3.221524$. This quantity $0.5\ln(2\pi\lambda) = 3.221524$ enters every Gaussian log-probability below.

### 4.2 Log-probability of the Poisson model at four deviations

The Poisson probability mass is $P(X = k) = e^{-\lambda}\lambda^k / k!$, so

$$\ln P(X = k) = -\lambda + k \ln \lambda - \ln k!.$$

The Gaussian density approximation at $k$ with $\mu = \sigma^2 = \lambda$ gives

$$\ln p_{\mathrm{G}}(k) = -\tfrac{1}{2}\ln(2\pi\lambda) - \frac{(k-\lambda)^2}{2\lambda}.$$

**Case $k = 110$ (one standard deviation, $x = (k-\lambda)/\sqrt{\lambda} = 1$).**

Stirling for $\ln 110!$:

- $110 \ln 110 = 110 \times 4.700480 = 517.0528$
- $-110$ gives $407.0528$
- $\tfrac{1}{2}\ln(2\pi \cdot 110) = \tfrac{1}{2}(1.837877 + 4.700480) = \tfrac{1}{2}(6.538357) = 3.269179$
- $\tfrac{1}{12 \cdot 110} = 1/1320 = 0.000758$

$$\ln 110! = 517.0528 - 110 + 3.269179 + 0.000758 = 410.3227.$$

Then

$$\ln P_{\mathrm{Pois}}(110) = -100 + 110 \times 4.605170 - 410.3227 = -100 + 506.5687 - 410.3227 = -3.7540.$$

Gaussian:

$$\ln p_{\mathrm{G}}(110) = -3.221524 - \frac{10^2}{200} = -3.221524 - 0.5 = -3.721524.$$

Log-difference:

$$\Delta_{1\sigma} = \ln P_{\mathrm{Pois}} - \ln p_{\mathrm{G}} = -3.7540 - (-3.721524) = -0.0325.$$

The Gaussian overestimates the Poisson log-probability by $0.0325$ nats at $1\sigma$, a probability relative error of $e