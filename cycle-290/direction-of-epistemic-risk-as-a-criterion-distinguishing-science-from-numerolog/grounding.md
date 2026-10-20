# Grounding block - source: rem-rev-64b9f286-9fcb-47e4-b026-e40a37a3d023

## Research idea

Direction of Epistemic Risk as a Criterion Distinguishing Science from Numerology. The author conjectures that the line between numerology and science is set not by mathematical abstraction or elegance but by 'direction of epistemic risk': frameworks that generate novel falsifiable predictions are knowledge, while those offering only post-hoc fits to known data are numerology—regardless of sophistication (string theory and Kewitsch's base-60 story being structurally identical). This matters because it yields a graded, operational taxonomy (knack, theorem, elegant retrodiction, falsified theory) applicable to historiography of science and to current theory assessment. A formal paper could test the criterion by (1) formalizing 'predictive risk' via Bayesian model comparison or out-of-sample predictive scoring, (2) applying it quantitatively to historical cases (3-4-5 rope vs. Pythagoras; base-60 utility vs. cosmic-significance claims), and (3) simulating model-selection dynamics to show whether elegance-weighted, unfalsifiable frameworks accumulate spurious credibility, thereby validating or refining the proposed gradient of epistemic legitimacy.

Source: owner notebook notes/v1/2026/06/27/_26178093853.md

Post-publication revision of the published paper "Direction of Epistemic Risk as a Criterion Distinguishing Science from Numerology" (version 1.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 8 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 6 references (70 percent of 8, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Section 4.2 Step 3 computes ERS ≈ (-2.058) + (-1.58) = -3.64. (confirmed by a second model)
2. Appendix B, C7: 'Sensitivity of ERS to λ ∈ [0.5, 2] changes scores by ≤ 0.12.' (confirmed by a second model)

## Existing paper under revision (remediation only)

# Direction of Epistemic Risk as a Criterion Distinguishing Science from Numerology

## Abstract
The practice of scientific theory assessment often conflates methodological elegance with epistemic legitimacy, allowing unfalsifiable frameworks to accrue credibility. This paper proposes **direction of epistemic risk**—the propensity of a framework to generate novel falsifiable predictions—as a quantitative criterion separating science from numerology. We formalize predictive risk using Bayesian model comparison and out‑of‑sample scoring, then apply the formalism to three historical case studies: the 3‑4‑5 rope argument versus Pythagorean geometry, the adoption of base‑60 time‑keeping versus cosmological numerology, and the emergence of modern cosmological surveys. A simple analytical example demonstrates that adaptive allocation (10×) and spatial modeling (5×) together yield a 50‑fold reduction in simulation budget relative to plain nested Monte Carlo, confirming the computational feasibility of the proposed metric. Sensitivity analysis shows that the criterion is robust to reasonable variations in prior weight and scoring horizon. The result implies that policy makers, funding agencies, and research teams can employ the epistemic‑risk score to prioritize theories that are genuinely predictive, thereby curbing the institutional reinforcement of numerology.

## 1. Introduction
Policy makers, funding agencies, and research teams repeatedly allocate scarce resources to theoretical programs that appear mathematically sophisticated but produce no new testable predictions. In finance, regulators such as Solvency II require a 99.5 % value‑at‑risk (VaR) calculation for a one‑year horizon, yet many risk‑management models rely on static calibrations that merely fit historical loss data without generating out‑of‑sample forecasts [1]. In fundamental physics, large‑scale observatories such as the LSST are funded on the promise of transformative discoveries, while competing theories that lack testable predictions continue to attract substantial attention. If a quantitative measure could distinguish frameworks that *reduce* epistemic uncertainty from those that merely *re‑package* existing data, decision makers could redirect investment toward genuinely predictive science.

The **so‑what** of this work is that a rigorously defined epistemic‑risk score can be computed from publicly available model outputs and prior specifications, and that the score correlates with historical judgments of scientific legitimacy. A high score indicates that a framework is likely to produce novel falsifiable predictions; a low score flags a numerological approach that may be aesthetically appealing but epistemically inert.

**Contributions**
1. Formal definition of *predictive epistemic risk* using Bayesian model evidence and out‑of‑sample scoring (Section 3).  
2. Derivation of a concrete simulation‑budget reduction factor (10 × adaptive allocation + 5 × spatial modeling = 50 × total savings) based on empirical results from sequential Gaussian‑process emulation [1] (Section 4).  
3. Application of the metric to three historical case studies, demonstrating alignment with accepted historiography (Section 5).  
4. Sensitivity analysis showing robustness of the score to prior hyper‑parameters and scoring windows (Section 6).  
5. Practical pathway for integrating the epistemic‑risk score into funding‑allocation pipelines and peer‑review criteria (Section 7).

## 2. Background and Related Work
The literature on quantitative risk measurement provides the methodological foundation for our epistemic‑risk formalism.

* **Sequential design for tail risk** [1] introduces nested simulation of portfolio losses and reports a two‑order‑of‑magnitude computational saving relative to plain Monte Carlo, with a 10× gain from adaptive allocation and a 5× gain from spatial modeling. These savings demonstrate that sophisticated surrogate models can dramatically reduce the cost of out‑of‑sample prediction, a prerequisite for computing epistemic‑risk scores.

* **Frictive Policy Optimization (FPO)** [2] treats epistemic regulation as a reward‑shaping problem. The discussion notes that inappropriate scaling of friction parameters (α, β) can either suppress epistemic behavior or cause excessive intervention, highlighting the sensitivity of epistemic‑risk measures to hyper‑parameter choice.

* **Non‑parametric VaR estimator for high dimensions** [3] presents a decomposition of portfolio exposure $\mathrm{expo}_{k,i-1}$ and recent volatility $\sigma_{k,i-1}^{14}$ to construct a high‑dimensional loss distribution. The algorithm relies on historical data without out‑of‑sample validation.

* **Operational risk loss‑severity selection** [4] describes the loss‑distribution approach (LDA) that computes the 99.9 % quantile of annual operational loss. The method emphasizes fitting to historical loss severity, but does not address predictive validation beyond the calibration dataset.

* **Pulsar science with the SKA Observatory** [5] highlights the potential of new instrumentation to expand observational capabilities, serving as an example of a framework that can generate novel predictions.

* **Statistical emulators for longevity risk** [6] discusses experimental designs for surrogate modeling of complex stochastic processes, emphasizing validation against a gold‑standard Monte Carlo estimate, which parallels our requirement for out‑of‑sample scoring.

* **LSST Dark Energy Science Collaboration** [7] outlines a program that leverages weak‑lensing shear measurements to constrain cosmological parameters. The collaboration’s reliance on large‑scale statistical inference underscores the importance of predictive power in modern astrophysics.

* **Range Value‑at‑Risk (RVaR) forecasts** [8] formalizes RVaR as an interpolation between VaR and Expected Shortfall, and provides an elicitability framework for scoring forecasts. The definition of $\mathrm{VaR}_{(}α_{)}$ as the infimum of the α‑quantile set is used in our derivations of predictive risk scores.

These works collectively illustrate the spectrum from purely predictive, empirically validated models to historically fitted, potentially numerological frameworks. Our contribution builds on their quantitative tools while introducing a unified epistemic‑risk criterion.

## 3. Methods
### 3.1 Predictive Epistemic Risk Formalism
Let **M** denote a candidate theoretical framework with parameter vector **θ** and prior density *p(θ|M)*. Observations up to time *t* are denoted **$D_{t}$**. The posterior predictive distribution for a future datum *y* is

$$
p(y \mid D_t, M) = \int p(y \mid \theta, M)\, p(\theta \mid D_t, M)\, d\theta .
$$

We define the **predictive epistemic risk** of *M* as the expected Kullback–Leibler (KL) divergence between the posterior predictive and the true data‑generating distribution *p\*(y)*, weighted by a scoring horizon *H*:

$$
\mathcal{R}(M) = \frac{1}{H}\sum_{h=1}^{H} \mathbb{E}_{y_h \sim p^*}\!\left[ \log\frac{p^*(y_h)}{p(y_h \mid D_{t+h-1}, M)} \right].
$$

A lower value of $\mathcal{R}(M)$ indicates that the model’s predictions are closer to reality, i.e., the model carries **lower epistemic risk**. Because *p\** is unknown, we approximate it using a held‑out validation set **V** and compute the empirical score

$$
\widehat{\mathcal{R}}(M) = -\frac{1}{|V|}\sum_{y \in V} \log p(y \mid D_{\text{train}}, M).
$$

This is precisely the out‑of‑sample log‑likelihood used in Bayesian model comparison.

### 3.2 Bayesian Model Evidence as a Baseline
The marginal likelihood (model evidence)

$$
\mathcal{Z}(M) = \int p(D_{\text{train}} \mid \theta, M)\, p(\theta \mid M)\, d\theta
$$

provides a prior‑averaged measure of fit. We compute the **Bayes factor** between two models *$M_{1}$* and *$M_{2}$* as

$$
\text{BF}_{12} = \frac{\mathcal{Z}(M_1)}{\mathcal{Z}(M_2)}.
$$

A Bayes factor greater than 1 favors *$M_{1}$*; however, Bayes factors do not penalize lack of predictive novelty. Therefore we combine $\widehat{\mathcal{R}}(M)$ with $\log\mathcal{Z}(M)$ to obtain a composite **Epistemic‑Risk Score (ERS)**:

$$
\text{ERS}(M) = -\log\mathcal{Z}(M) + \lambda\,\widehat{\mathcal{R}}(M),
$$

where $\lambda>0$ balances fit and predictive risk. The ERS is lower for models that both fit the data and make accurate out‑of‑sample predictions.

### 3.3 Computational Procedure
1. **Training**: Fit each candidate model to the training set using Markov‑chain Monte Carlo (MCMC) or variational inference.  
2. **Evidence Estimation**: Approximate $\mathcal{Z}(M)$ via thermodynamic integration (TI) or nested sampling, as demonstrated in sequential GP emulation [1].  
3. **Predictive Scoring**: Evaluate the held‑out log‑likelihood $\widehat{\mathcal{R}}(M)$ on validation data.  
4. **Composite Score**: Compute ERS with $\lambda=1$ (baseline) and explore sensitivity to $\lambda\in[0.5,2]$.

### 3.4 Historical Case Study Design
For each historical case we construct a minimal probabilistic model:

* **3‑4‑5 rope vs. Pythagoras**: Model the probability that a civilization adopts the 3‑4‑5 rule given prior knowledge of Euclidean geometry.  
* **Base‑60 time‑keeping**: Model the adoption of a sexagesimal calendar as a function of astronomical observability versus numerological appeal.  
* **Modern cosmological surveys**: Model the expected detection rate of dark‑energy signatures as a function of survey depth and sky coverage.

In each case we assign priors reflecting contemporary knowledge and compute ERS using synthetic validation data generated from the historically accepted theory (e.g., Euclidean geometry for the rope case). The procedure mirrors the out‑of‑sample validation employed in risk‑measure forecasting [8].

## 4. Analysis
### 4.1 Derivation of Simulation‑Budget Savings
Section 7.1 of [1] reports two independent sources of computational savings:

* Adaptive allocation yields a **10×** reduction in required simulation runs.  
* Spatial modeling yields a **5×** reduction.

Assuming the two techniques are applied sequentially and independently, the total reduction factor **S** is the product:

\[
S = 10 \times 5 = 50.
\]

Thus, the combined approach requires only $1/50$ of the simulation budget of a plain nested Monte Carlo implementation. This arithmetic is straightforward multiplication of the two reported factors.

### 4.2 Numerical Example of ERS Calculation
We illustrate the ERS computation with a simple Gaussian predictive model. Assume a one‑dimensional loss variable $Y$ with prior $Y\sim\mathcal{N}(0,\sigma^2)$, $\sigma=0.05$ (5 % of portfolio value). Training data consist of $n=100$ observations drawn from the true distribution $Y\sim\mathcal{N}(0,0.05^2)$. The posterior predictive distribution remains $\mathcal{N}(0,0.05^2)$ because the prior is conjugate.

**Step 1: Log‑likelihood on validation set**  
Take a held‑out set of $m=20$ observations $\{y_j\}$. The log‑likelihood for a single observation under $\mathcal{N}(0,\sigma^2)$ is

\[
\log p(y_j) = -\frac{1}{2}\log(2\pi\sigma^2) - \frac{y_j^2}{2\sigma^2}.
\]

Averaging over the validation set yields

\[
\widehat{\mathcal{R}} = -\frac{1}{m}\sum_{j=1}^{m}\log p(y_j).
\]

Because the validation data are generated from the same distribution, the expected value of $y_j^2$ equals $\sigma^2$, giving

\[
\mathbb{E}[\widehat{\mathcal{R}}] = -\left[-\frac{1}{2}\log(2\pi\sigma^2) - \frac{1}{2}\right] = \frac{1}{2}\log(2\pi\sigma^2) + \frac{1}{2}.
\]

Plugging $\sigma=0.05$:

\[
2\pi\sigma^2 = 2\pi(0.05)^2 = 2\pi(0.0025) \approx 0.015708,
\]
\[
\log(0.015708) \approx -4.155,
\]
\[
\frac{1}{2}\log(2\pi\sigma^2) \approx -2.0775,
\]
\[
\mathbb{E}[\widehat{\mathcal{R}}] \approx -2.0775 + 0.5 = -1.5775.
\]

Thus the empirical predictive risk estimate is $\widehat{\mathcal{R}}\approx 1.58$ (absolute value).

**Step 2: Model evidence**  
For a conjugate Gaussian model, the marginal likelihood is

\[
\mathcal{Z} = \frac{1}{\sqrt{2\pi(\sigma^2 + \tau^2/n)}} \exp\!\left(-\frac{\bar{y}^2}{2(\sigma^2 + \tau^2/n)}\right),
\]

where $\tau^2$ is the prior variance (assume $\tau^2=0.01$) and $\bar{y}=0$ (sample mean). Substituting $n=100$, $\sigma^2=0.0025$, $\tau^2=0.01$:

\[
\sigma^2 + \frac{\tau^2}{n} = 0.0025 + \frac{0.01}{100} = 0.0025 + 0.0001 = 0.0026,
\]
\[
\sqrt{2\pi(0.0026)} \approx \sqrt{0.01634} \approx 0.1278,
\]
\[
\mathcal{Z} = \frac{1}{0.1278} \approx 7.825,
\]
\[
-\log\mathcal{Z} = -\log(7.825) \approx -2.058.
\]

**Step 3: ERS**  
With $\lambda=1$:

\[
\text{ERS} = -\log\mathcal{Z} + \widehat{\mathcal{R}} \approx (-2.058) + (-1.58) = -3.64.
\]

A negative ERS indicates that the model’s predictive performance outweighs the penalty from model complexity, placing it in the “low epistemic risk” region.

### 4.3 RVaR Projection Example
Using the definition of RVaR from [8], let $\alpha=0.95$, $\beta=0.99$, and assume linear interpolation between VaR$_{0.95}=0.10$ and VaR$_{0.99}=0.20$ (these are **assumed** for illustration). The RVaR is

\[
\text{RVaR}_{\alpha,\beta} = \frac{1}{\beta-\alpha}\int_{\alpha}^{\beta}\text{VaR}_u\,du.
\]

With linear interpolation, the integral equals the area of a trapezoid:

\[
\int_{0.95}^{0.99}\text{VaR}_u\,du = \frac{0.99-0.95}{2}\bigl(\text{VaR}_{0.95}+\text{VaR}_{0.99}\bigr)
= 0.04 \times \frac{0.10+0.20}{2}
= 0.04 \times 0.15 = 0.006.
\]

Dividing by $\beta-\alpha = 0.04$ yields

\[
\text{RVaR}_{0.95,0.99} = \frac{0.006}{0.04}=0.15.
\]

Thus, under the stated assumptions, the RVaR equals 0.15 (15 % loss). This projection illustrates how the RVaR bridges VaR and Expected Shortfall, providing a richer target for out‑of‑sample scoring.

## 5. Results
### 5.1 Simulation‑Budget Savings
Applying the combined adaptive‑allocation and spatial‑modeling approach described in [1] reduces the required simulation budget by a factor of **50** (Section 4.1). This reduction makes the extensive out‑of‑sample validation needed for ERS computation tractable even for high‑dimensional risk models.

### 5.2 ERS Values for Historical Cases (Projection)
The following ERS values are **projected** based on synthetic validation data generated under the historically accepted theory for each case. The assumptions are explicitly stated: uniform priors over simple parameter spaces and validation data drawn from the accepted model.

The three historical cases are qualitatively ranked as follows: the 3‑4‑5 rope framework exhibits the lowest epistemic risk, followed by the base‑60 time‑keeping framework, and then the modern cosmological survey framework, reflecting their relative predictive novelty under the synthetic assumptions.

All three cases are projected to yield ERS values (under the synthetic assumptions) that reflect their relative predictive novelty, but no specific numeric values are presented.

### 5.3 Sensitivity to λ
Varying the weighting parameter $\lambda$ between 0.5 and 2 changes ERS, but the exact magnitude of change is not quantified here; the ranking of models appears qualitatively stable under reasonable re‑weightings of fit versus predictive risk.

## 6. Discussion
### 6.1 Limitations
1. **Prior Specification** – The ERS depends on the choice of prior $p(\theta|M)$. While we explored a range of hyper‑parameters, alternative priors could shift absolute scores.  
2. **Validation Data Generation** – Historical case studies rely on synthetic validation data constructed from the accepted theory; real‑world validation may be unavailable.  
3. **Computational Approximation** – Evidence estimation via thermodynamic integration introduces numerical error; however, the 50× simulation‑budget reduction mitigates this concern.  
4. **Model Class Restriction** – The analysis assumes models admit a tractable likelihood; black‑box machine‑learning models may require alternative scoring (e.g., proper scoring rules).  

If any of these assumptions were violated—e.g., if the prior were misspecified to heavily favor a numerological model—the ERS could incorrectly rank a numerology as low‑risk. Empirical falsification would occur if out‑of‑sample performance deteriorated sharply relative to the training fit, causing $\widehat{\mathcal{R}}$ to increase and ERS to rise.

### 6.2 Failure Modes and Falsification
A single observation that would falsify the main claim is the systematic failure of low‑ERS models to outperform high‑ERS models on truly independent future data. For instance, if a theory with ERS = 0.3 consistently yields predictions with higher realized loss than a theory with ERS = 0.8 across multiple domains, the epistemic‑risk criterion would be invalidated.

### 6.3 Open Questions
* How does the ERS behave for models that generate *qualitative* predictions (e.g., existence of a new particle) rather than quantitative forecasts?  
* Can the ERS be integrated with existing peer‑review scoring systems without imposing excessive computational burdens?  
* What is the impact of model misspecification on the Bayes factor component of ERS?

## 7. Practical Implications and Engineering Pathways
### (a) Intended Users and Decision Impact
Funding agencies, research‑institution steering committees, and journal editorial boards can adopt the epistemic‑risk score to prioritize proposals that demonstrate low ERS. A low ERS would justify allocating larger budgets, longer timelines, or higher reviewer weighting to a project, whereas a high ERS would trigger a request for additional predictive validation.

### (b) Technology Readiness Level
The methodology is purely analytical, based on Bayesian inference and out‑of‑sample scoring, and has not undergone peer review. Accordingly, it resides at **TRL 2** (technology concept and/or application formulated).

### (c) Minimal Next Experiment
A pilot study could be conducted on a publicly available risk‑modeling dataset (e.g., the insurance loss data used in [1]). The steps would be:
1. Fit two competing models (one predictive, one numerological).  
2. Compute ERS for each using a held‑out 20 % validation split.  
3. Compare ERS rankings to subsequent out‑of‑sample performance on a later data release.  
If the predictive model’s ERS remains lower while its realized loss predictions are more accurate, the result supports the criterion; a reversal would falsify it.

### (d) Engineering Constraints
* **Computational Resources** – Accurate evidence estimation requires nested sampling or thermodynamic integration; the 50× budget reduction from [1] alleviates this constraint.  
* **Data Availability** – Sufficient historical data for validation are needed; in domains lacking such data, surrogate validation (e.g., cross‑validation) must be employed.  
* **Software** – Existing probabilistic programming frameworks (Stan, PyMC) can implement the required inference pipelines.

### (e) Projected Cost Bounds
Assuming a baseline nested Monte Carlo simulation budget of $10^6$ CPU‑hours for a high‑dimensional risk model, the combined adaptive and spatial approach reduces this to $2\times10^4$ CPU‑hours (50× reduction). At a cloud compute rate of \$0.02 per CPU‑hour, the projected cost drops from \$20,000 to \$400, representing a **\$19,600** saving (projection based on the savings factor from [1]).

### (f) Risks and Misuse
If the ERS is applied without careful prior elicitation, stakeholders might manipulate priors to artificially lower scores, leading to “gaming” of the metric. Transparent reporting of priors and sensitivity analyses are essential safeguards.

## 8. Conclusion
We have introduced a quantitative **epistemic‑risk** framework that combines Bayesian model evidence with out‑of‑sample predictive scoring to distinguish scientifically predictive theories from numerological constructions. Empirical evidence from sequential Gaussian‑process emulation demonstrates that the required computational effort is tractable, with a 50‑fold simulation‑budget reduction. Application to three historical case studies yields ERS rankings consistent with accepted historiography, and sensitivity analysis confirms robustness to reasonable hyper‑parameter variations. The proposed metric offers a practical tool for funding agencies, reviewers, and research managers to allocate resources toward genuinely predictive science, thereby reducing the institutional reinforcement of numerology.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.1-proportionate-notice). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 8 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Sequential Design and Spatial Modeling for Portfolio Tail Risk Measurement. arXiv:1710.05204v2. https://arxiv.org/abs/1710.05204v2
[2] Frictive Policy Optimization for LLMs: Epistemic Intervention, Risk-Sensitive Control, and Reflective Alignment. arXiv:2604.25136v1. https://arxiv.org/abs/2604.25136v1
[3] A generic nonparametric value-at-risk estimator for high dimensions. arXiv:2608.17481v1. https://arxiv.org/abs/2608.17481v1
[4] On the Selection of Loss Severity Distributions to Model Operational Risk. arXiv:2107.03979v1. https://arxiv.org/abs/2107.03979v1
[5] Pulsar Science with the SKA Observatory. arXiv:2512.16152v1. https://arxiv.org/abs/2512.16152v1
[6] Statistical Emulators for Pricing and Hedging Longevity Risk Products. arXiv:1508.00310v2. https://arxiv.org/abs/1508.00310v2
[7] Large Synoptic Survey Telescope: Dark Energy Science Collaboration. arXiv:1211.0310v1. https://arxiv.org/abs/1211.0310v1
[8] Evaluating Range Value at Risk Forecasts. arXiv:1902.04489v3. https://arxiv.org/abs/1902.04489v3

## Appendix A. Divergence report
*No divergent claims were identified among the independent drafts; all substantive statements converged.*

## Appendix B. Claim attribution
| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | Adaptive allocation yields a 10× simulation‑budget reduction (from [1]). | A, B, C | Convergent |
| C2 | Spatial modeling yields a 5× simulation‑budget reduction (from [1]). | A, B, C | Convergent |
| C3 | Combined savings factor S = 10 × 5 = 50. | A, B, C | Convergent |
| C4 | ERS for Gaussian predictive model equals –0.478 (derived in Section 4). | A, B, C | Convergent |
| C5 | RVaR under linear interpolation equals 0.15 (projection, assumptions stated). | A, B, C | Convergent |
| C6 | Historical case ERS values (projected) (synthetic validation assumptions). | A, B, C | Convergent |
| C7 | Sensitivity of ERS to $λ \in$ [0.5, 2] changes scores by $\le$ 0.12. | A, B, C | Convergent |
| C8 | Simulation‑budget projection: \$20,000 → \$400 (based on 50× reduction). | A, B, C | Convergent |
| C9 | Limitations list (prior, validation data, evidence approximation, model class). | A, B, C | Convergent |
| C10 | Minimal pilot experiment design (compare two models on public dataset). | A, B, C | Convergent |
| C11 | TRL assessment: analytical work at TRL 2. | A, B, C | Convergent |
| C12 | Risks of prior manipulation and need for transparency. | A, B, C | Convergent |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1710.05204v2 | Sequential Design and Spatial Modeling for Portfolio Tail Risk Measurement
arXiv:2604.25136v1 | Frictive Policy Optimization for LLMs: Epistemic Intervention, Risk-Sensitive Control, and Reflective Alignment
arXiv:2608.17481v1 | A generic nonparametric value-at-risk estimator for high dimensions
arXiv:2107.03979v1 | On the Selection of Loss Severity Distributions to Model Operational Risk
arXiv:2512.16152v1 | Pulsar Science with the SKA Observatory
arXiv:1508.00310v2 | Statistical Emulators for Pricing and Hedging Longevity Risk Products
arXiv:1211.0310v1 | Large Synoptic Survey Telescope: Dark Energy Science Collaboration
arXiv:1902.04489v3 | Evaluating Range Value at Risk Forecasts

## QNFO corpus context (Vectorize)

QNFO: The Ultrametric Foundation: A Unified Thesis on Number, Time, Knowledge, and Computation | https://papers.qnfo.org/papers/the-ultrametric-foundation-a-unified-thesis-on-number-time-knowledge-and-computa
QNFO: Deterministic Unified Theory | https://papers.qnfo.org/papers/a-deterministic-unified-theory
QNFO: Head Over Hands | https://papers.qnfo.org/papers/head-over-hands
QNFO: Physics, Solved | https://papers.qnfo.org/papers/ultrametric-physics-m6-quantum-gate-theory

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1710.05204v2 | Sequential Design and Spatial Modeling for Portfolio Tail Risk Measurement
  We consider calculation of capital requirements when the underlying economic scenarios are determined by simulatable risk factors. In the respective nested simulation framework, the goal is to estimate portfolio tail risk, quantified via VaR or TVaR of a given collection of future economic scenarios representing factor levels at the risk horizon. Traditionally, evaluating portfolio losses of an ou
  Full text (https://arxiv.org/html/1710.05204v2), excerpts of its own sections:
  § 1 Introduction: The latest insurance and financial regulations mandate estimation of quantile-based portfolio risk measures. The Solvency II [ 17 ] framework calls for computing the $99.5\%$ -level value-at-risk ( $\VaR$ ) for a 1-year horizon, while the Basel III regulations in banking [ 2 ] require to report the related tail value-at-risk ( $\TVaR$ ). In practice, these quantities are calculated by first generating a representative set $\mathcal{Z}$ of future economic scenarios and then evaluating the empirical loss quantile based on $\mathcal{Z}$ . However, due to the underlying cashflow and valuation complexity, directly computing future portfolio value is usually not feasible and instead approximations are used. This is done for each scenario by a Monte Carlo evaluation of the conditional expectation that probabilistically defines portfolio value, leading to a nested simulation problem. [...]
  § 2 Objective: Given a probability space $(\Omega,\mathcal{F},\mathbb{P})$ , we consider a stochastic system with Markov state process $Z=(Z_{t})$ . Both continuous- and discrete-time models can be treated. Typically, $Z$ is a multivariate stochastic process based on either a stochastic differential equation ( $t\in\mathbb{R}_{+}$ ) or time-series ARIMA framework ( $t\in\mathbb{N}$ ). Based on the realizations of $Z,$ the modeler needs to assess the resulting capital $f(Z_{T})$ at an intermediate horizon $T$ . The portfolio value $f(Z_{T})$ is computed as the conditional expected value of discounted cashflows $Y_{t}$ given $\mathcal{F}_{T},$ the information at time $T$ . [...]
  § 7.1 Results: For the remainder of this section, we consider the horizon $T=1$ and analyze $f(Z_{1})$ in Equation ( 37 ), the net present value of the life annuity one year into the future. We take $x=55$ and annuity start date of $S=10$ , when the individual retires at age $x=65$ . As before, we simulate $Z_{1}$ via Algorithm 1 in Appendix  B to determine a scenario set $\mathcal{Z}$ with $N=10^{4}$ . The interest rate parameters in Equation ( 39 ) are $\bar{\beta}=0.04,\bar{\alpha}=0.04,\bar{\zeta}=0.02,\phi=0.05$ , with the E&W mortality model fitted over the age range $x\in[55,89]$ using the StMoMo package [ 37 ] . As in the previous case study, the GP hyperparameters are refitted after stages $10,20,\ldots,100$ , and after each round for A3-GP and U2-GP. For the mean function, we fit the constant $\mu(z)\equiv\beta_{0}$ . [...]
  § 8 Conclusion: We provided the first comprehensive examination of sequential methods for estimating $\VaR_{\alpha}$ and $\TVaR_{\alpha}$ using Gaussian process emulators and nested simulations over a fixed set of outer scenarios. Existing approaches in the simulation literature fall short for this application, whether it be assuming the level ( $\VaR_{\alpha}$ ) is known [ 30 , 4 , 15 ] and/or non-noisy outputs [ 26 ] , using a non sequential algorithm [ 27 ] , or not using a spatial model for smoothing [ 8 ] . We document a two orders-of-magnitude savings relative to plain nested Monte Carlo, with about 10x savings thanks to adaptive allocation and 5x savings due to spatial modeling. These gains are strongest for small simulation budgets $\mathcal{N}\approx N$ where existing approaches essentially fail or are not applicable. As a further advantage, employing a GP emulator also leads to essentially unbiased risk estimators (in contrast to biased unsmoothed versions) and provides a reliable estimate of standard error. [...]
[2] arXiv:2604.25136v1 | Frictive Policy Optimization for LLMs: Epistemic Intervention, Risk-Sensitive Control, and Reflective Alignment
  We propose Frictive Policy Optimization (FPO), a framework for learning language model policies that regulate not only what to say, but when and how to intervene in order to manage epistemic and normative risk. Unlike standard alignment methods that optimize surface-level preference or task utility, FPO treats clarification, verification, challenge, redirection, and refusal as explicit control act
  Full text (https://arxiv.org/html/2604.25136v1), excerpts of its own sections:
  § Discussion.: Friction-Augmented Rewards is the simplest member of the FPO family and is directly compatible with existing RLHF and actor–critic pipelines ( Christiano et al., 2017 ; Ouyang et al., 2022 ) . It requires no change to the policy architecture and treats epistemic regulation as a form of reward shaping. The main advantage of FAR is its generality: any reinforcement learning algorithm that optimizes a scalar reward can incorporate friction with minimal modification. This makes FAR attractive as a baseline method and as a drop-in extension of standard alignment pipelines. However, FAR inherits the known limitations of reward shaping. First, it is sensitive to reward scaling: inappropriate choices of $\alpha$ and $\beta$ can lead either to excessive intervention or to complete suppression of epistemic behavior. Second, its effectiveness depends critically on the quality and calibration of the surrogate friction signal $F(h,y)$ . Noise or bias in $F$ is directly propagated into the learning signal, potentially destabilizing training. [...]
  § Discussion.: Friction Preference Pairing represents a fundamentally different learning signal from reward shaping. Rather than inducing epistemic behavior indirectly through scalar returns, FPP trains the policy to satisfy a structured preference ordering over interventions. The main advantage of FPP is that it avoids explicit reward modeling. This makes it robust to reward hacking and miscalibration, and well-suited to settings in which epistemic judgments are qualitative, comparative, or context-dependent. Because preferences are defined over pairs, FPP naturally handles intransitive and non-additive notions of epistemic quality that cannot be captured by a single scalar friction score. Critically, because FPP and GRFR rely on ordinal ranking rather than cardinal maximization, they mitigate the risk of exploiting holes in the underlying classifiers. The policy is driven to find ’better’ interventions relative to a baseline, rather than exploiting the unbounded upper limits of a scalar reward model. [...]
  § Discussion.: Group-Relative Frictive Ranking optimizes relative epistemic quality across full dialogue trajectories rather than absolute returns. By learning from comparative performance within each context, GRFR avoids dependence on the global calibration of the trajectory score and directly targets the ordering of epistemic strategies. The main advantage of GRFR is that it captures long-horizon epistemic phenomena that cannot be reduced to local reward shaping or single-turn preferences: delayed clarification, cumulative contradiction, progressive misalignment, and escalation into unsafe regimes. Because updates are driven by relative ranking, GRFR remains robust to monotonic transformations of the trajectory score and to moderate miscalibration of the friction surrogate. The primary cost of GRFR is computational: it requires grouped rollouts and trajectory-level evaluation, and its performance depends on sufficient diversity within each cohort. [...]
  § Discussion.: FTR is orthogonal to the other FPO methods. While FAR, FPP, and GRFR shape what the policy is optimized to prefer, FTR shapes where in policy space the optimizer is allowed to move. As a result, FTR can be combined with any of the other methods as a risk-sensitive regularizer. [...]
  § Summary.: This multimodal running example illustrates how epistemic friction arises naturally from referential ambiguity, shared visual context, and multi-agent coordination. [...]
[3] arXiv:2608.17481v1 | A generic nonparametric value-at-risk estimator for high dimensions
  We present in this article a non-parametric value-at-risk (VaR+CVaR) algorithm that remains accurate for an arbitrarily large number of underlying positions. The algorithm solves the two inherent problems of VaR estimation. First, past history is not directly applicable to the future, but all predictions of the future are based on the past. Second, VaR estimation is equivalent to modeling a single
  Full text (https://arxiv.org/html/2608.17481v1), excerpts of its own sections:
  § 1 Introduction: We present in this article a computationally simple, generic value-at-risk (VaR and CVaR) algorithm that remains accurate for an arbitrarily large number of different underlying positions. The algorithm tackles the two fundamental issues inherent to all tail risk estimation: • Long-term risk is inherently not the same as short-term risk, but we need long-term history (which is not directly applicable) to say anything about future risk • Tail-risk describes the case when all our bets go against us at the same time. Once we have 100+ different positions, this is equivalent to modeling a single corner of a high-dimensional space, which is mathematically difficult. The algorithm breaks down the probability density function of the total portfolio return into 3 constituent parts: • $expo_{k,i-1}$ : the exposure to financial instrument $k$ as measured by market value / AUM at the close of day $i-1$ . • $\sigma^{14}_{k,i-1}$ : the recent volatility (root-mean-squared of the daily true range percentage) of $k$ in the most recent (configurable) 14 days before day $i$ . [...]
  § 2 The Probability Density Function (PDF) of Tomorrow’s Portfolio Return: We begin with the time series of daily returns for each underlying financial instrument $k$ as shown in 1 . We are currently at the end of day $i-1$ . $r_{k,i}$ is the unknown return of $k$ for tomorrow, day $i$ . $\centering...~...~...~r_{k,j-14}~...~...~...~r_{k,j-1}~r_{k,j}~...~...~...~r_{k,i-14}~...~...~...~r_{k,i-1}~[r_{k,i}]\@add@centering$ (1) We can also compute the time series of the daily true range percentage (TRP) of the instrument $k$ in 3 using Equation 2 . [...]
  § 6 Ensemble of Portfolio Back Test Results: We compute the 99% daily VaR estimator for each day $i$ using the exposures of each instrument on day $i-1$ and each instrument’s historical data up to day $i-1$ using Equation 5 . We also compute the portfolio’s total return on day $i$ according to Equation 10 . $total~portfolio~r_{i}=\sum_{k}expo_{k,i-1}*r_{k,i}$ (10) We compare the portfolio’s daily return and the 99% daily VaR estimation and identify the days when the portfolio loss exceeds the VaR estimation as shown in Figure 4 . The blue represent the portfolio’s daily total return. The orange is the 99% daily VaR estimated using the procedure in Section 2 . The red tags the days when the portfolio return is more negative than the estimated 99% daily VaR. Figure 4: Example portfolio’s daily return vs 99% VaR. [...]
  § 9 Conclusion: We presented a computationally simple, generic value-at-risk algorithm that works for an arbitrarily high number of dimensions. The algorithm breaks down the probability density function of the portfolio’s total return into 3 components: • $expo_{k,i-1}$ : the exposure to financial instrument $k$ as measured by market value / AUM at the close of day $i-1$ . • $\sigma^{14}_{k,i-1}$ : the recent volatility of $k$ in the most recent 14 days before day $i$ . • $\frac{r_{k,j}}{\sigma^{14}_{k,j-1}}$ : how much $k$ ’s return on each past day $j$ deviated from the recent volatility before day $j$ . The portfolio total return PDF can then be used to calculate the VaR at any confidence, and the expected shortfall of the user’s choice. The recent volatility $\sigma^{14}_{k,i-1}$ rapidly adapts to the recent condition. The historical $r_{k,j}/\sigma^{14}_{k,j-1}$ ratio captures the non-Gaussian skew within a single instrument and all relations in the past between different instruments $k$ . [...]
[4] arXiv:2107.03979v1 | On the Selection of Loss Severity Distributions to Model Operational Risk
  Accurate modeling of operational risk is important for a bank and the finance industry as a whole to prepare for potentially catastrophic losses. One approach to modeling operational is the loss distribution approach, which requires a bank to group operational losses into risk categories and select a loss frequency and severity distribution for each category. This approach estimates the annual ope
  Full text (https://arxiv.org/html/2107.03979v1), excerpts of its own sections:
  § 1 Introduction: The bcbs ( bcbs ) defines or ( or ) in b2 ( b2 ) as “the risk of a loss resulting from inadequate or failed internal processes, people and systems, or from external events. This definition includes legal risk but excludes strategic and reputational risk.” ( BCBS, 2006, 2006 ) To mitigate potential operational losses, regulators require that a bank set aside a minimum amount of capital for one year called rc ( rc ). The ama ( ama ) presented in b2 calculates rc as the $99.9\%$ quantile of the estimated firm-wide annual operational loss distribution. This distribution is commonly estimated using the lda ( lda ), which requires a bank to estimate and select the loss frequency and loss severity distributions for each rrc ( rrc ) and treat firm-wide annual operational loss as a compound sum of the annual losses from each rrc . A major obstacle facing banks using the ama is to develop a procedure that provides stable rc calculations year-to-year. [...]
  § 2 Loss Distribution Approach: Under the b2 ama guidelines, operational loss events are partitioned into eight business lines and seven event types. When an operational loss occurs, it is mapped to one of 56 business line/event type intersections, called a rrc ( rrc ). This mapping process is further explained in BCBS, (2006) . Each loss event must be assigned a time stamp, a loss amount, and a rrc . The time stamp is usually a fiscal quarter or year and the loss amount is a positive value. The number of loss events that occur in a particular rrc over a given time period is called the loss frequency, and each loss amount is called the loss severity . Historical loss data are used to estimate the loss frequency and severity distributions by interpreting the historical loss data as realizations of random variables. Under an ama , the historical loss data should reflect all current, material activities, risk exposures, and loss events whose loss severities exceed a minimum threshold. For example, a bank that sells off or discontinues a business line should no longer use those losses in their ama . [...]
  § 3 Loss Severity Estimation and Selection: Regulations require that a bank’s internal operational loss data include all loss events whose severities exceed a minimum threshold, so we assume that we have no information about the loss events that occur below the threshold. As a result, the datasets are treated as left-truncated. [...]
  § 6 Conclusion: In conclusion, we feel that the qs and truncation probability estimate should be used in conjunction with likelihood and goodness-of-fit measures when selecting a severity distribution. While we used mle to estimate each candidate distribution, one may want to explore using the qs as an objective function to minimize for parameter estimation. We prefer lsas to gnh as a loss severity candidate due to its ability to model various tail behaviors and ease of numerical derivation. However, both distributions can be added as candidates. The gnh log-likelihood function is numerically more difficult to work with than the lsas log-likelihood function, with more instances of non-convergence of numerical maximum likelihood for gnh . Including both gnh and lsas as candidate distribution may preserve at least one of the four-parameter candidates when the numerical maximum likelihood is unable to converge for gnh . Future research should investigate penalized maximum likelihood approaches for gnh to minimize the probability of negative losses. [...]
[5] arXiv:2512.16152v1 | Pulsar Science with the SKA Observatory
  The large instantaneous sensitivity, a wide frequency coverage and flexible observation modes with large number of beams in the sky are the main features of the SKA observatory's two telescopes, the SKA-Low and the SKA-Mid, which are located on two different continents. Owing to these capabilities, the SKAO telescopes are going to be a game-changer for radio astronomy in general and pulsar astrono
  Full text (https://arxiv.org/html/2512.16152v1), excerpts of its own sections:
  § 1 Introduction: The SKA Observatory (SKAO) is going to be a game-changer for radio astronomy in the coming decade. The construction of this unique instrument, comprising of two telescopes in two different continents, has already commenced with the phase 1 of these telescopes providing an unprecedented seamless frequency coverage from 50 MHz to 15 GHz with unmatched sensitivities in highly flexible interferometric configurations. Therefore, the SKAO is expected to enable a range of diverse astronomical investigations with significant impact on fundamental aspects of astrophysics. One such area of radio astronomy, where the SKAO is expected to make fundamental discoveries, is pulsar astronomy. Historically, new instruments have accelerated the pace of progress in pulsar astronomy (Figure 1 ) and the SKAO telescopes are likely to drive significant progress in this field in the next decade. The phase 1 of the rollout of the SKAO telescope, called AA4 (Array Assembly 4), is likely to double the known pulsar population in new surveys ( Keane et al., 2025 ; Abbate et al., 2025 ; Bagchi et al., 2025 ) . [...]
  § 2 The SKAO telescopes and pulsar observations: The SKAO telescopes are conceived as two telescopes geographically stationed on different continents and with different designs. The SKA-Low telescope is located in Australia, whereas the SKA-Mid is coming up in South Africa. Together, the two telescopes cover an observing frequency range of 50 MHz to 15 GHz. The two telescopes will be commissioned and operated by an inter-governmental organisation bringing together more than 13 nations from around the world in a unique collaborative international effort. The construction plan of the SKAO telescopes is envisaged as a staged delivery of evolving array assembly (AA). The earliest milestone, AA*, is likely be delivered between 2029 to 2031, and the design baseline AA4 will follow depending on funding 1 1 1 Please refer to https://www.skao.int/en/science-users/599/scientific-timeline for details. . [...]
  § 3 State of the art and expected SKAO discoveries: There have been significant advances in pulsar astronomy since the pulsar science case for the SKAO was drafted two decades ago, particularly since its update a decade back ( Kramer and Stappers, 2015 ) . The gravitational waves at high frequencies have been detected from more than 200 sources and the pulsar timing arrays are close to a significant detection of nano-Hertz gravitational waves opening up a messenger that the SKAO telescope can explore in earnest. More exotic binary systems have been discovered and mass and radius for several NS are measured to a good precision motivating investigations in fundamental physics using pulsars as probes. The large instantaneous sensitivity and flexibility of the SKAO telescope will make a significant impact on the pulsar science case with doubling the pulsar population in a pulsar survey, which forms the basis for fundamental physics studies interconnected with other areas of pulsar astronomy as illustrated in Figure 2 . [...]
  § Summary: Together, these studies define the pulsar and neutron-star science programme for the SKA Observatory. The AA* arrays will provide an immediate leap in discovery power and precision, while the full AA4 configurations of SKA-Low and SKA-Mid will deliver transformative, population-level insights into neutron-star physics, plasma astrophysics, Galactic structure, and gravitation.
[6] arXiv:1508.00310v2 | Statistical Emulators for Pricing and Hedging Longevity Risk Products
  We propose the use of statistical emulators for the purpose of valuing mortality-linked contracts in stochastic mortality models. Such models typically require (nested) evaluation of expected values of nonlinear functionals of multi-dimensional stochastic processes. Except in the simplest cases, no closed-form expressions are available, necessitating numerical approximation. Rather than building a
  Full text (https://arxiv.org/html/1508.00310v2), excerpts of its own sections:
  § 3.3 Experimental Design: Several approaches are possible for constructing the training design $\mathcal{D}$ . First, one may generate an empirical design by independently sampling $z^{(n)}\sim Z(T)|Z(0)$ . This allows to emulate the conditional density $p_{T}(z|Z(0))$ which is advantageous for computing an expectation like in ( 3 ). Second, one may generate a random $\mathcal{D}$ using some other proposal density $z^{(n)}\sim Q$ . For example, a uniform proposal density (i.e.  $z^{(n)}$ i.i.d. uniform in some domain $D\subseteq\mathbb{R}^{d}$ ) yields a basic attempt in having a space filling experimental design of arbitrary size. A more structured (but still random) design can be obtained via Latin Hypercube Sampling (LHS) techniques [ 38 ] . Roughly speaking, LHS builds a regular $d$ -dimensional lattice and then attempts to equidistribute $N_{tr,1}$ sites among the resulting hypercubes. Within each selected hypercube the design site is placed uniformly. Third, one can use a deterministic design, such as a latticed grid, or a quasi-Monte Carlo (QMC) sequence. [...]
  § 3.4 Fitting and Evaluation of Emulators: To fit an emulator for a given simulation budget $N_{tr}$ , we first decompose $N_{tr}=N_{tr,1}\times N_{tr,2}$ and then construct an experimental design $\mathcal{D}$ of size $N_{tr,1}$ using one of the methods in Section 3.3 . Each site in $\mathcal{D}$ then spawns $N_{tr,2}$ trajectories that are batched together as in ( 25 ). Fitting is done in R using the mentioned publicly available packages. For kriging, we use the default setting of the km function in DiceKriging package. Given $\hat{a}(z,T,x)$ we evaluate its performance across a test set $\mathcal{D}^{test}=(z^{(1)},\ldots,z^{(N_{out})})$ of $N_{out}$ locations. Note that $\mathcal{D}^{test}$ is distinct from the training set $\mathcal{D}$ . In line with ( 3 ) we use an empirical testing set $\mathcal{D}^{test}$ : $z^{(n)}\sim Z(T)|Z(0)$ . Since the true values $a(z,T,x)$ are not available, we benchmark against an (expensive) gold standard estimate $\hat{a}^{MC}(z,T,x)$ that is described below. [...]
  § 4.1 Results: We follow Chen and Cox [14] in using US mortality data obtained from the National Center for Health Statistics (NCHS) 1 1 1 Source: http://www.cdc.gov/nchs/nvss/mortality_tables.htm . This dataset contains yearly age specific death rates for overall US population over 1900–2003. Fitting yields the random-walk parameters $\mu^{(1)}=-0.2173,\sigma^{(1)}=0.3733$ in ( 31 ), as well as the estimated probability of shock as $p=0.0436$ , with jump distribution $(\mu^{(2)},\sigma^{(2)})=(0.8393,1.4316)$ . As expected, $\mu^{(2)}\gg 0$ is large and positive, so shocks correspond to large temporary increases in mortality. The goal is to analyze and compare the ability of kriging models and analytic estimates to predict $T=10$ -year deferred annuity values for unisex $x=65$ year olds. Payments are cut-off at age $\bar{x}=94$ . We use a discount rate of $r=4\%$ . [...]
  § 5.3 Results: $N_{tr}=1000$ $N_{tr}=8000$ Type Bias $\sqrt{\text{IMSE}}$ Bias $\sqrt{\text{IMSE}}$ Analytic A1 from ( 37 ) -2.101e-02 3.460e-02 -2.101e-02 3.460e-02 Analytic A2 from ( 39 ) 4.480e-03 5.321e-03 4.480e-03 5.321e-03 Thin Plate Spline 2.577e-03 1.304e-02 5.803e-04 5.095e-03 Universal Kriging 4.363e-04 1.856e-02 1.857e-03 1.289e-02 Simple Kriging -1.334e-03 3.280e-03 9.390e-04 3.043e-03 Table 2: Performance of analytic estimates and surrogate models for hedge portfolio values in the two-population model case study. [...]
[7] arXiv:1211.0310v1 | Large Synoptic Survey Telescope: Dark Energy Science Collaboration
  This white paper describes the LSST Dark Energy Science Collaboration (DESC), whose goal is the study of dark energy and related topics in fundamental physics with data from the Large Synoptic Survey Telescope (LSST). It provides an overview of dark energy science and describes the current and anticipated state of the field. It makes the case for the DESC by laying out a robust analytical framewor
  Full text (https://arxiv.org/html/1211.0310v1), excerpts of its own sections:
  § 1 Introduction and overview: The Large Synoptic Survey Telescope (LSST) is a wide-field, ground-based telescope, designed to image a substantial fraction of the sky in six optical bands every few nights. It is planned to operate for a decade allowing the stacked images to detect galaxies to redshifts well beyond unity. The LSST and the survey are designed to meet the requirements ( Ivezić & the LSST Science Collaboration 2011 ) of a broad range of science goals in astronomy, astrophysics and cosmology, including the study of dark energy – the accelerating expansion of the Universe. [...]
  § 4 Overview of dark energy science: Observations reveal that the expansion of the Universe is accelerating, a result that poses a direct challenge to current theories of cosmology and fundamental physics. The 2011 Nobel Prize in Physics was awarded for the 1998 discovery of the accelerating Universe using distance measurements of Type Ia supernovae (SNe). In the thirteen years since that discovery, astronomical observations ranging from the cosmic microwave background (CMB) to the spatial distribution of galaxies have validated and refined what we know about the expansion history of the Universe. Acceleration represents a serious dilemma for fundamental physics. The most prosaic explanation is that vacuum energy, which constitutes about three quarters of the energy density in the Universe, is driving the acceleration; however, naive predictions based on the Planck scale would predict vacuum energy densities roughly 100 orders of magnitude larger than observed, implying that some unknown physics suppresses such predicted vacuum energy, but leaves a very small residual that is driving the current expansion rate. [...]
  § 1 Overview: Gravitational lensing ( Schneider 2006 ; Bartelmann 2010 ) , the deflection of light from distant “sources” due to the bending of space-time by masses (“lenses”) along the line of sight, is a useful cosmological probe because it is sensitive to all matter, whether baryonic or dark. Weak lensing (WL) is gravitational lensing in the limit that the deflections are very small, causing tiny distortions, or “shear”, in galaxy shapes ( Bartelmann & Schneider 2001 ; Refregier 2003 ) . In the absence of lensing, galaxy orientations are assumed to be random, so they should not exhibit statistically significant, coherent alignments. Lensing induces small ( $\lesssim 1$ %) but coherent shears ( $\gamma$ ), in background galaxy images, which have typical ellipticities that are far larger (RMS ellipticity $\sim 0.36$ ). Thus, WL is detected statistically by averaging over many lensed galaxies, for which shapes have been measured in a way that eliminates contributions from observational effects that also distort galaxy shapes (e.g., the point-spread function, or PSF). [...]
  § 1 Overview: Measurements of galaxy clustering constrain the cosmic expansion history, the cosmological distance scale, the growth rate of structure, the mass of the neutrinos and the abundance of dark matter. Baryon acoustic oscillations (BAO) in the early Universe imprint a standard ruler in the power-spectrum (or the two-point correlation function), which measures the angular-diameter distance and the Hubble parameter. BAO is a special case of using the full shape of galaxy clustering data to constrain cosmological models. The BAO feature has now been observed in the SDSS, 2dF, and BOSS surveys, using both spectroscopic ( Eisenstein et al. 2005a ; Anderson et al. 2012 ; Xu et al. 2012 , e.g.,) and photometrically selected galaxy samples ( Padmanabhan et al. [...]
[8] arXiv:1902.04489v3 | Evaluating Range Value at Risk Forecasts
  The debate of what quantitative risk measure to choose in practice has mainly focused on the dichotomy between Value at Risk (VaR) -- a quantile -- and Expected Shortfall (ES) -- a tail expectation. Range Value at Risk (RVaR) is a natural interpolation between these two prominent risk measures, which constitutes a tradeoff between the sensitivity of the latter and the robustness of the former, tur
  Full text (https://arxiv.org/html/1902.04489v3), excerpts of its own sections:
  § 1 Introduction: In the field of quantitative risk management, the last one or two decades have seen a lively debate about which monetary risk measure ( Artzner et al., 1999 ) be best in (regulatory) practice. The debate mainly focused on the dichotomy between Value at Risk ( $\operatorname{VaR}_{\beta}$ ) on the one hand and Expected Shortfall ( $\operatorname{ES}_{\beta}$ ) on the other hand, at some probability level $\beta\in(0,1)$ (see Section 2 for definitions). Mirroring the historical joust between median and mean as centrality measures in classical statistics, $\operatorname{VaR}_{\beta}$ , basically a quantile, is esteemed for its robustness, while $\operatorname{ES}_{\beta}$ , a tail expectation, is deemed attractive due to its sensitivity and the fact that it satisfies the axioms of a coherent risk measure ( Artzner et al., 1999 ) . We refer the reader to Embrechts et al. (2014) and Emmer et al. (2015) for comprehensive academic discussions, and to Bank for International Settlements (2014) for a regulatory perspective in banking. Cont et al. [...]
  § 2.1 Definition of Range Value at Risk: There are different sign conventions in the literature on risk measures. In this paper we use the following convention: If a random variable $Y$ models the losses and gains, then positive values of $Y$ represent gains and negative values of $Y$ losses. Moreover, if $\rho$ is a risk measure, we assume that $\rho(Y)\in\mathbb{R}$ corresponds to the maximal amount of money one can withdraw such that the position $Y-\rho(Y)$ is still acceptable. Hence, negative values of $\rho$ correspond to risky positions. In the sequel, let $\mathcal{F}_{0}$ be the class of probability distribution functions on $\mathbb{R}$ . Recall that the $\alpha$ -quantile, $\alpha\in[0,1]$ of $F\in\mathcal{F}_{0}$ is defined as the set $q_{\alpha}(F)=\{x\in\mathbb{R}\,|\,F(x-)\leq\alpha\leq F(x)\}$ , where $F(x-):=\lim_{t\uparrow x}F(t)$ . Definition 2.1 . Value at Risk of $F\in\mathcal{F}_{0}$ at level $\alpha\in[0,1]$ is defined as $\operatorname{VaR}_{\alpha}(F)=\inf q_{\alpha}(F)$ . [...]
  § 2.2 Elicitability and scoring functions: Using the decision-theoretic framework of Fissler and Ziegel (2016) and Gneiting (2011) , we introduce the following notation. Let $\mathcal{F}\subseteq\mathcal{F}_{0}$ be some generic subclass, and $\mathsf{A}\subseteq\mathbb{R}^{k}$ be an action domain . [...]
  § 3 Elicitability and identifiability results: Wang and Wei (2020, Theorem 5.3) show that for $0 triplet $(\operatorname{VaR}_{\alpha},\operatorname{VaR}_{\beta},\operatorname{RVaR}_{\alpha,\beta})$ , however, is elicitable and identifiable, subject to mild conditions. We use the notation $S_{\alpha}(x,y)=(\mathds{1}\{y\leq x\}-\alpha)x-\mathds{1}\{y\leq x\}y$ , and recall that $S_{\alpha}$ is $\mathcal{F}$ -consistent for $\operatorname{VaR}_{\alpha}$ if $\int_{-\infty}^{0}|y|\,\mathrm{d}F(y) ( Gneiting, 2011 ) . Proposition 3.1 . For $0 $\displaystyle V(x_{1},x_{2},x_{3},y)\ =\begin{pmatrix}\mathds{1}\{y\leq x_{1}\}-\alpha\\ \mathds{1}\{y\leq x_{2}\}-\beta\\ x_{3}+\frac{1}{\beta-\alpha}\big(S_{\beta}(x_{2},y)-S_{\alpha}(x_{1},y)\big)\end{pmatrix}$ (3.1) is an $\mathcal{F}^{(\alpha)}\cap\mathcal{F}^{(\beta)}$ -identification function for $(\operatorname{VaR}_{\alpha},\operatorname{VaR}_{\beta},\operatorname{RVaR}_{\alpha,\beta})$ , which is strict on $\mathcal{F}^{\alpha}\cap\mathcal{F}^{(\alpha)}\cap\mathcal{F}^{\beta}\cap\mathcal{F}^{(\beta)}$ . Proof. [...]
[9] QNFO: The Ultrametric Foundation: A Unified Thesis on Number, Time, Knowledge, and Computation | https://papers.qnfo.org/papers/the-ultrametric-foundation-a-unified-thesis-on-number-time-knowledge-and-computa
  Positional notation is inherently an ultrametric tree of nested cycles. The Archimedean line is a derived abstraction. Recovering the native ultrametric resolves cascading errors across mathematics, physics, epistemology, education, quantum computing, and interface design.
  Full text (https://papers.qnfo.org/papers/the-ultrametric-foundation-a-unified-thesis-on-number-time-knowledge-and-computa), excerpts of its own sections:
  § A Unified Thesis on Number, Time, Knowledge, and Computation: **Author:** QNFO **Date:** 2026-06-27 **Version:** 1.0-draft **License:** QNFO Unified License Agreement (QNFO-ULA): https://legal.qnfo.org/ ---
  § Author's Note `[my conjecture — the synthesis is my own; individual component claims carry their own certainty labels]`: This thesis synthesizes a 67-minute intellectual progression recorded across 21 sequential notes on June 27, 2026. It begins with a deceptively simple observation about the numeral "10" and traces its implications through mathematics, physics, epistemology, education, quantum computing, and interface design, revealing a single unifying structure: **the ultrametric tree that underlies all quantitative representation was systematically flattened into an Archimedean line, and recovering it resolves a cascade of otherwise disconnected errors across every domain of human knowledge** `[my conjecture — this is the central synthetic claim this document argues for]`.
  § Certainty Calibration Conventions: Throughout this thesis, every claim beyond textbook consensus carries an explicit certainty label: | Label | Meaning | |:------|:--------| | `[established]` | Supported by multiple independent experiments or peer-reviewed proofs; no serious dispute | | `[mainstream interpretation]` | Most widely held view among specialists, though not directly proven | | `[speculative]` | Theoretical motivation exists, but no direct experimental support | | `[my conjecture]` | The author's own idea — not yet subjected to independent peer review | | `[debated]` | Active disagreement among specialists; no clear consensus | | `[not yet falsifiable]` | Cannot currently state what experimental result would disprove this | | `[LLM-INFERRED]` | Derived from the model's reasoning or training data; not independently verified | ---
  § 1.1 The Primal Observation: In any integer base $b \geq 2$, the digit string "10" denotes the number $b$. This holds universally: binary "10" = two, decimal "10" = ten, sexagesimal "10" = sixty. Therefore every base, when named using its own numeral system, calls itself "base‑10." This is not a joke. It is a concrete demonstration that **a numeral string cannot internally specify its own rule of interpretation.** The radix is always a silent parameter, supplied by an external meta‑language — a human convention, a hardware specification, a cultural default. The efficiency of positional notation is purchased at the permanent cost of latent ambiguity. The crack this opens is the fault line running through all formal symbolism: - Any numeral string is radically underdetermined without context. - The base cannot be named from within — an echo of Gödelian incompleteness and the use/mention boundary. [...]
  § 1.2 The Silent Partner: The Silent Metric: The radix is not alone in its silence. The equal‑interval assumption is the second great hidden parameter. Integers possess a natural order (the successor function) but no intrinsic distance. The picture of equally spaced points on a straight line is a geometric import from Descartes and analytic geometry — an epistemological tool reified into an ontological property. [...]
  § 12.5 Falsification Experiment: A minimal experiment: build a depth‑2 tree (8 qubits) of transmon qubits connected via coaxial cavities enforcing tree‑only gates. Compare logical error rate against a 2D nearest‑neighbour layout with identical qubit parameters. The central claim is falsified if the tree geometry does not yield a statistically significant improvement in logical error rate. ---
[10] QNFO: Deterministic Unified Theory | https://papers.qnfo.org/papers/a-deterministic-unified-theory
  URL: https://papers.qnfo.org/papers/a-deterministic-unified-theory/ Date: 2026-03-12 Version: 1.0 This manuscript confronts a challenge embedded deeply within the structure of human language. We intend to describe a universe consisting entirely of dynamic, interconnected processes. However, our grammar compels us to speak constantly in terms of static things. This subject-predicate foundation forc
  Full text (https://papers.qnfo.org/papers/a-deterministic-unified-theory), excerpts of its own sections:
  § A DETERMINISTIC UNIFIED: THEORY **Author:** Rowan Brad Quni-Gudzinas **Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com) **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000000526456062 **URL:** https://papers.qnfo.org/papers/a-deterministic-unified-theory/ **Date:** 2026-03-12 **Version:** 1.0 **CHAPTER 1: REFRAMING REALITY: BEYOND OBJECTS AND RANDOMNESS**
  § 1.1 The Linguistic Challenge of Process Ontology: This manuscript confronts a challenge embedded deeply within the structure of human language. We intend to describe a universe consisting entirely of dynamic, interconnected processes. However, our grammar compels us to speak constantly in terms of static things. This subject-predicate foundation forces us to reify processes into objects during description. Stating that an electron travels suggests a distinct entity separate from the traveling. What our models actually describe are stable, localized patterns of energetic oscillation. These patterns exist within a continuous, universal field rather than as isolated objects. Therefore, this text consciously works against the grain of its own linguistic medium. We use nouns like electron or cell merely as necessary, temporary communicative shorthands. Readers are asked to hold these conventional labels lightly throughout the following chapters. These words represent observable, repeating processes rather than names for static, independent objects. The goal involves using these familiar terms as bridges toward a deeper understanding. [...]
  § 1.3 Reinterpreting Error Terms and Randomness: The assumption of randomness deeply infects how we interpret experimental data across disciplines. When an experiment yields unexpected variance, researchers frequently attribute it to systemic noise. This categorization allows scientists to maintain the validity of their simplified parametric models. However, this practice actively suppresses the discovery of subtle, underlying deterministic processes. The variance is not a mistake; it is the system expressing its full complexity. By smoothing out the data, we erase the intricate signatures of correlated history. We must learn to read the noise rather than simply filtering it out. Consider the standard approach to modeling complex biological or physical interactions mathematically. Equations are constructed to isolate a few variables while holding all others constant. The inevitable discrepancies between the model and the observation are swept into the error term. This error term becomes a conceptual dumping ground for everything we do not understand. [...]
  § 1.5 Scale-Invariant Patterning: The distinction between microscopic and macroscopic worlds represents another misleading linguistic and conceptual convenience. We artificially divide reality into different scales based on the limitations of human perception. We assume that the rules governing subatomic processes differ fundamentally from those governing large objects. This assumption creates a fractured view of physics, requiring different theories for different sizes. However, a process-based, deterministic universe should exhibit consistent patterning across all scales of observation. The universe does not change its fundamental operating principles based on how closely we look. Reality is scale-invariant, exhibiting fractal-like consistency from the smallest to the largest observable phenomena. The principles that govern interactions within an atom do not vanish in a collection of atoms. [...]
[11] QNFO: Head Over Hands | https://papers.qnfo.org/papers/head-over-hands
  This provides a systemic analysis of a recurring philosophical and institutional bias that privileges abstract, elegant, and a priori theoretical constructs over messy, inconvenient, and empirical evidence. This pattern is defined here as the Head Over Hands Fallacy. This new term is introduced because existing concepts such as confirmation bias or paradigm rigidity are insufficient. Confirmation 
  Full text (https://papers.qnfo.org/papers/head-over-hands), excerpts of its own sections:
  § “HEAD OVER HANDS” - A Systemic Analysis of the Prioritization of Conceptual Elegance (Head) Over Empirical Reality (Hands): **Author**: Rowan Brad Quni-Gudzinas **Affiliation**: QNFO **Email**: rowan.quni@qnfo.org **ORCID**: 0009-0002-4317-5604 **ISNI**: 0000000526456062 **URL:** https://papers.qnfo.org/papers **Version**: 1.0.1 **Date**: 2025-09-15 >*“A very coarse experimenter... almost always found the results he required, trusting to his head rather than his hands.”* — Sir Humphry Davy’s assessment of John Dalton
  § 1.0 Executive Summary: Defining the Fallacy: This provides a systemic analysis of a recurring philosophical and institutional bias that privileges abstract, elegant, and *a priori* theoretical constructs over messy, inconvenient, and empirical evidence. This pattern is defined here as the **Head Over Hands Fallacy**. This new term is introduced because existing concepts such as confirmation bias or paradigm rigidity are insufficient. *Confirmation bias* typically describes an individual cognitive flaw, while “paradigm rigidity” denotes a static condition of a scientific field. Neither term fully captures the active, systemic, and often pathological *process* of defending a cherished theory (*the “Head”*) against the verdict of observed reality (*the “Hands”*). The indispensability of this term lies in its ability to encapsulate a complete, cyclical pattern of behavior—spanning individual psychology, institutional incentives, and philosophical predispositions—that actively suppresses contradictory data to preserve conceptual elegance. [...]
  § 1.1 Nature of the Flaw and Summary of Consequences: The **Head Over Hands Fallacy** is identified not as a formal logical fallacy, but as a recurring pathological pattern of scientific and societal behavior rooted in a lack of epistemic humility. This will demonstrate how this fallacy has led to decades of scientific stagnation, the active suppression of truth and persecution of dissenters, the entrenchment of social and racial injustice, devastating and lethal public policy failures, and a distorted, fragmented understanding of reality.
  § 1.2 Central Thesis: The Humility of Scientific Truth: The central thesis of this work posits that the greatest intellectual triumphs are born not from the solo genius of the *Head*, but from its tense, dynamic, and ultimately humble subservience to the verdict of the *Hands*. This perspective emphasizes that genuine scientific progress arises from the rigorous and iterative interaction between theoretical constructs and empirical observation, demanding intellectual flexibility and a profound respect for the data.
  § 8.0 Conclusion: The Enduring Structure of Chemical Thought and the Harmony of Matter: The conceptual chaos of nineteenth-century chemistry compelled a shift toward structural and relational thinking, exemplified by Mendeleev’s periodic table and its underlying proto-categorical logic, and most strikingly by de Chancourtois’s Telluric Screw. Re-contextualized through modern quantum mechanics and the helical electron model, the Telluric Screw transforms from a historical artifact into a physical map of quantum resonance, charting the progression of Compton frequencies and the harmonic recurrence of electron standing wave patterns that define elemental properties. This journey from empirical observation to abstract formalism, and the historical resistance encountered, underscores the deep continuity in scientific thought and the enduring challenge posed by the Head Over Hands Fallacy. [...]
[12] QNFO: Physics, Solved | https://papers.qnfo.org/papers/ultrametric-physics-m6-quantum-gate-theory
  The canonical unsolved problems in physics are reframed as diagnostic signatures of an incomplete descriptive paradigm. This paper proposes a generative framework in which physical reality emerges from a deterministic computational process on a topological substrate—the circle \(S^1\). Its first homotopy group, \(\pi_1(S^1) \cong \mathbb{Z}\), yields integer winding numbers that serve as complete 
  Full text (https://papers.qnfo.org/papers/ultrametric-physics-m6-quantum-gate-theory), excerpts of its own sections:
  § Rethinking: Wikipedia’s “List of Unsolved Problems in Physics” **Author:** Rowan Brad Quni-Gudzinas **Affiliation:** QNFO **Contact:** rowan.quni@qnfo.org **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000 0005 2645 6062 **DOI:** https://papers.qnfo.org/papers/ultrametric-physics-m6-quantum-gate-theory/ **Publication Date:** 2025-10-16 **Version:** 1.0 The canonical unsolved problems in physics are reframed as diagnostic signatures of an incomplete descriptive paradigm. This paper proposes a generative framework in which physical reality emerges from a deterministic computational process on a topological substrate—the circle \(S^1\). Its first homotopy group, \(\pi_1(S^1) \cong \mathbb{Z}\), yields integer winding numbers that serve as complete information carriers: magnitude sets mass-energy, while prime factorization encodes quantum charges. A topological resonance condition, governed by the golden ratio, selects a sparse spectrum of stable states, explaining the hierarchy problem and the existence of exactly three fermion generations. [...]
  § 1.0: The Problem Landscape: A Survey of Physics’ Great Unsolved Questions At the heart of scientific progress lies the candid acknowledgment of the unknown. In the field of fundamental physics, this frontier of ignorance is famously cataloged in what is colloquially known as the “List of unsolved problems in physics,” a living document curated by the scientific community and popularly hosted on platforms like Wikipedia (Wikipedia, 2025). This list is not a testament to the failure of physics, but rather to its vitality and ambition. It serves as a roadmap for future research, a benchmark against which new theories are measured, and a humbling reminder of the vast conceptual territories that remain unexplored. To solve even a single problem on this list would represent a monumental achievement, likely worthy of a Nobel Prize, as it would fundamentally alter our understanding of the universe. [...]
  § 2.0: The Foundational Crisis: Unsolved Problems as Signatures of a Paradigm Limit Modern physics is defined by an extraordinary paradox: the unprecedented success of its two foundational theories, general relativity and the Standard Model of particle physics, is matched only by the profound, seemingly irreconcilable chasm that separates them. This schism is not a minor academic dispute but a deep conceptual crisis that manifests as a persistent list of unsolved problems. These challenges, ranging from the nature of dark matter to the fine-tuning of the cosmos, are often treated as disparate mysteries. However, a more incisive perspective suggests they are not independent failures but rather interconnected symptoms of a single, underlying issue: our current theoretical frameworks are descriptive rather than generative. They provide an extraordinarily precise catalog of *what* happens but offer little insight into *why* the universe is structured in this particular way. [...]
  § 2.1: The Symptomatic Nature of Foundational Incompatibility The primary symptoms of this foundational crisis are twofold. First is the direct ontological conflict between our theories of gravity and quantum phenomena. Second is the descriptive limit of the Standard Model, which relies on a host of unexplained, empirically measured parameters to function. These incompatibilities are not flaws to be patched within their respective domains but are clues to be deciphered, pointing toward a more fundamental structure from which both theories emerge as approximations. [...]