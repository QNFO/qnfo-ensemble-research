# Direction of Epistemic Risk as a Criterion Distinguishing Science from Numerology

## Abstract

Scientific institutions routinely reward mathematical elegance and formal sophistication even when a research program produces no new testable predictions, while genuinely predictive programs compete for the same resources without a common yardstick. This paper proposes **direction of epistemic risk**—the propensity of a framework to generate novel falsifiable predictions—as a quantitative criterion separating science from numerology, and formalizes it as a composite Epistemic-Risk Score (ERS) combining Bayesian model evidence with out-of-sample predictive scoring. The gap addressed is operational: existing tools either measure fit to past data (value-at-risk estimators, loss-distribution approaches) or measure forecast quality (elicitable scoring functions), but no standard metric ranks frameworks by their direction of epistemic risk. We derive the score, illustrate it on a conjugate Gaussian model (ERS $\approx -3.64$ for a well-specified predictive model), and show that the computational burden of the required out-of-sample validation is tractable: sequential design and spatial modeling for portfolio tail risk yield a combined $50\times$ reduction in nested-simulation budget ($10\times$ from adaptive allocation, $5\times$ from spatial modeling). A sensitivity derivation shows that for model pairs whose predictive-risk gap is at most $0.08$, varying the fit-versus-prediction weight $\lambda$ over $[0.5,2]$ changes the score gap by at most $0.12$, leaving rankings stable. The score gives funding agencies, editorial boards, and research managers a computable, falsifiable criterion for prioritizing predictive frameworks over retrodictive ones.

## 1. Introduction

Funding agencies, regulatory bodies, and research leaders must repeatedly decide which theoretical programs deserve scarce resources, and the decision is currently made largely on judgments of elegance, pedigree, and mathematical sophistication. In insurance and banking regulation, the Solvency II framework requires computation of the $99.5\%$-level value-at-risk (VaR) for a one-year horizon, and Basel III requires the related tail value-at-risk [1]; the models that produce these numbers are judged by how well they reproduce historical loss data, not by whether they generate out-of-sample predictions that could fail. In fundamental physics, instruments such as the Large Synoptic Survey Telescope are justified by explicit predictive programs—constraining dark energy through weak-lensing shear, galaxy clustering, and supernova distances [7]—while competing frameworks that retrofit existing observations with no possibility of differential prediction absorb attention and talent. The cost of the current arrangement is concrete: capital is reserved against models that may fail silently on tomorrow's data, and research careers are built on frameworks that cannot lose an argument with nature.

The problem this paper bears on is therefore a resource-allocation problem with an epistemic core. If a computable score existed that ranks frameworks by their *direction of epistemic risk*—whether the framework's next commitment is a novel falsifiable prediction or another retrodiction of already-known data—then a funding committee could demand the score alongside impact statements, an editorial board could flag submissions whose predictive content is empty, and a research manager could detect when a program has drifted from prediction into numerology. The historical record supplies the intuition: the 3-4-5 rope rule earned its place by surviving use, while numerological systems that attached cosmic significance to the same numbers earned none; the observation that in any base $b \geq 2$ the digit string "10" denotes $b$ shows how a numerically striking fact can be simultaneously true and epistemically inert [9]. What is missing is the quantitative version of that distinction.

This paper supplies the formal criterion and demonstrates its computational feasibility. The central claim is that "direction of epistemic risk" can be measured: a framework scores well when its posterior predictive distribution, trained only on past data, is scored on data it has not seen, and poorly when its only successes are in-sample. The claim is testable in the ordinary way—if low-scoring frameworks systematically outperform high-scoring ones on future data, the criterion is falsified.

**Contributions**

1. A formal definition of predictive epistemic risk, combining Bayesian model evidence with out-of-sample log-likelihood scoring into a composite Epistemic-Risk Score (Section 3).
2. A derivation of the simulation-budget reduction factor $S = 10 \times 5 = 50$ for the nested-simulation workload the score requires, from the reported gains of adaptive allocation and spatial modeling in sequential Gaussian-process emulation [1] (Section 4.1).
3. A fully worked numerical ERS computation for a conjugate Gaussian model, yielding $\text{ERS} \approx -3.64$, with every arithmetic step shown (Section 4.2).
4. A derivation of the sensitivity bound that varying $\lambda \in [0.5,2]$ changes the ERS gap between model pairs by at most $0.12$ when their predictive-risk gap is at most $0.08$ (Section 4.4).
5. A worked RVaR projection ($\text{RVaR}_{0.95,0.99} = 0.15$ under stated assumptions) illustrating the scoring targets the criterion consumes (Section 4.3).
6. A practical pathway—users, readiness level, minimal falsifying experiment, binding constraints, and projected cost bounds—for adopting the score in review and funding pipelines (Section 7).

## 2. Background and Related Work

The literature relevant to this criterion falls into four groups: computational machinery for out-of-sample risk evaluation, risk measures and their scoring, examples of strongly predictive programs, and analyses of the institutional bias the criterion is designed to counter.

**Sequential design for tail risk [1]** frames exactly the computational problem the ERS faces: estimating portfolio tail risk via VaR or TVaR requires a nested simulation in which each of many future economic scenarios is itself evaluated by Monte Carlo, because direct computation of future portfolio value is usually infeasible. Its conclusion reports "a two orders-of-magnitude savings relative to plain nested Monte Carlo, with about 10x savings thanks to adaptive allocation and 5x savings due to spatial modeling," strongest at small simulation budgets, and notes that the Gaussian-process emulator additionally yields essentially unbiased risk estimators with a reliable standard error [1]. These two reported factors are the inputs to the budget derivation in Section 4.1, and the unbiasedness point matters here because a biased surrogate would corrupt the very out-of-sample scores the ERS consumes.

**Frictive Policy Optimization [2]** is, on its face, about language-model alignment, but its discussion of scoring mechanics transfers directly to the gaming problem any epistemic metric faces. Its analysis of friction-augmented rewards warns that inappropriate choices of the scaling parameters $\alpha$ and $\beta$ "can lead either to excessive intervention or to complete suppression of epistemic behavior," and that noise or bias in the surrogate friction signal is propagated directly into the learning signal [2]. Its preference-pairing variant is described as robust to reward hacking because it relies on ordinal ranking rather than cardinal maximization, mitigating exploitation of "holes in the underlying classifiers" [2]. Section 7f borrows this lesson: a cardinal score such as the ERS is gameable, and pairwise or ranked comparisons are a partial defense.

**The generic nonparametric VaR estimator for high dimensions [3]** exemplifies the calibration-only end of the spectrum. Its algorithm decomposes the portfolio return density into exposures $\mathrm{expo}_{k,i-1}$, recent 14-day volatilities $\sigma^{14}_{k,i-1}$, and historical standardized returns $r_{k,j}/\sigma^{14}_{k,j-1}$, and its introduction states the two fundamental problems of tail estimation plainly: long-term history is not directly applicable to the future, yet all predictions of the future are based on the past [3]. The estimator adapts rapidly to recent conditions but is validated by backtests—comparing daily returns against the $99\%$ daily VaR estimate [3]—which is in-sample scoring of past data, precisely the pattern the ERS is designed to flag when it is the *only* evidence offered.

**Operational-risk loss-severity selection [4]** shows the same pattern inside the regulatory pipeline. Under the Advanced Measurement Approach, regulatory capital is the $99.9\%$ quantile of the firm-wide annual operational-loss distribution, estimated by the loss distribution approach over 56 business-line/event-type cells, with severity datasets treated as left-truncated because losses below a threshold are unobserved [4]. Its conclusion recommends using a quantile-score in conjunction with likelihood and goodness-of-fit measures when selecting among candidate severity distributions, preferring the lognormal-SAS over the GNH because of the latter's numerical non-convergence in maximum likelihood [4]. All of these selection criteria are evaluated on historical data; none asks whether the selected distribution predicts future loss regimes, which is the gap the ERS formalizes.

**Pulsar science with the SKA [5]** supplies the contrasting, strongly predictive pole. Its introduction states that the AA4 array assembly "is likely to double the known pulsar population in new surveys," and its science sections tie that population doubling to specific downstream tests: pulsar timing arrays approaching a significant detection of nano-Hertz gravitational waves, mass and radius measurements for several neutron stars motivating fundamental-physics probes [5]. A survey that predicts a doubling of a known population is maximally exposed to falsification—the ERS is designed to reward exactly this exposure.

**Statistical emulators for longevity risk [6]** provides the validation methodology the ERS procedure adopts. Its fitting section is explicit that the test set $\mathcal{D}^{\text{test}}$ is distinct from the training set $\mathcal{D}$, and that because true values are unavailable, emulators are benchmarked against an expensive gold-standard Monte Carlo estimate [6]. Its results table reports biases of order $10^{-3}$ to $10^{-2}$ and root-IMSE values of similar magnitude for kriging and spline surrogates at training budgets $N_{tr} = 1000$ and $8000$ [6]. This is the operational template for Step 3 of the ERS procedure in Section 3.3: score on held-out data, benchmark against the best available gold standard, and report the error.

**The LSST Dark Energy Science Collaboration white paper [7]** shows what a high-stakes predictive program looks like at scale. Its overview of dark energy science records that naive Planck-scale predictions of vacuum energy density exceed the observed value by roughly 100 orders of magnitude, and that weak lensing induces coherent shears of order $\lesssim 1\%$ against intrinsic galaxy ellipticities with RMS $\sim 0.36$, so detection is necessarily statistical, averaging over many lensed galaxies [7]. A program whose target signal is a $1\%$ coherent shear buried in $36\%$ ellipticity noise is a framework that has committed, in advance, to observations that can refute it.

**Range Value-at-Risk forecasts [8]** contributes the scoring theory. It defines $\operatorname{VaR}_{\alpha}(F) = \inf q_{\alpha}(F)$ where $q_{\alpha}(F)$ is the $\alpha$-quantile set, positions RVaR as an interpolation between VaR and Expected Shortfall trading robustness against sensitivity, and establishes—citing Wang and Wei's theorem—that the triple $(\operatorname{VaR}_{\alpha}, \operatorname{VaR}_{\beta}, \operatorname{RVaR}_{\alpha,\beta})$ is elicitable and identifiable, giving an explicit identification function $V(x_1,x_2,x_3,y)$ [8]. Elicitability is the property that makes honest out-of-sample scoring of a forecast possible without systematic distortion; Section 4.3 uses the RVaR definition in a worked projection, and the elicitability result is why forecast-scoring targets of this family are suitable inputs to the ERS.

**The QNFO corpus supplies both case material and the diagnosis.** The Ultrametric Foundation thesis observes that in any integer base $b \geq 2$ the numeral "10" denotes $b$—binary "10" is two, sexagesimal "10" is sixty—so every base names itself "base-10," demonstrating that a numeral string cannot specify its own interpretation and that numerically striking facts can be context-dependent and epistemically empty [9]. Notably, that thesis attaches explicit certainty labels to its claims, including a category "[not yet falsifiable]" for claims for which no experimental result can currently be stated as disproof [9]; the ERS is, in effect, a numeric version of that self-audit. The Head Over Hands analysis names the institutional failure this paper targets: a recurring pattern that privileges "abstract, elegant, and *a priori* theoretical constructs over messy, inconvenient, and empirical evidence," illustrated by Sir Humphry Davy's assessment of John Dalton as an experimenter who "trusting to his head rather than his hands... almost always found the results he required" [11]. Its central thesis—that scientific triumphs come from the "Head's" humble subservience to the verdict of the "Hands" [11]—is the qualitative claim the ERS attempts to quantify. The Deterministic Unified Theory [10] and the ultrametric physics framework [12] serve as live test cases for the score: the former argues that smoothing discrepancies into error terms suppresses discovery of underlying deterministic structure [10], a claim about model misspecification that the ERS's evidence term is sensitive to; the latter proposes that a golden-ratio-governed topological resonance condition selects a sparse stable spectrum, explaining the hierarchy problem and exactly three fermion generations [12]—an elegant, unified account whose epistemic direction (novel prediction versus retrodiction) is exactly the question the ERS is built to adjudicate rather than presume.

## 3. Methods

### 3.1 Predictive Epistemic Risk Formalism

Let $M$ denote a candidate theoretical framework with parameter vector $\boldsymbol{\theta}$ and prior density $p(\boldsymbol{\theta} \mid M)$. Observations up to time $t$ are denoted $D_t$. The posterior predictive distribution for a future datum $y$ is

$$
p(y \mid D_t, M) = \int p(y \mid \boldsymbol{\theta}, M)\, p(\boldsymbol{\theta} \mid D_t, M)\, d\boldsymbol{\theta}.
$$

We define the **predictive epistemic risk** of $M$ as the expected Kullback–Leibler divergence between the posterior predictive and the true data-generating distribution $p^*(y)$, averaged over a scoring horizon $H$:

$$
\mathcal{R}(M) = \frac{1}{H}\sum_{h=1}^{H} \mathbb{E}_{y_h \sim p^*}\!\left[ \log\frac{p^*(y_h)}{p(y_h \mid D_{t+h-1}, M)} \right].
$$

A lower value of $\mathcal{R}(M)$ indicates predictions closer to reality, i.e., lower epistemic risk. Because $p^*$ is unknown, we approximate it with a held-out validation set $V$ and compute the empirical score

$$
\widehat{\mathcal{R}}(M) = -\frac{1}{|V|}\sum_{y \in V} \log p(y \mid D_{\text{train}}, M),
$$

the negative out-of-sample mean log predictive density. Two sign conventions follow and are used consistently throughout: $\widehat{\mathcal{R}}$ is the negative of the average log predictive density, so a model whose predictive density exceeds unity on average (possible for sharply concentrated distributions) yields a negative $\widehat{\mathcal{R}}$, and lower (more negative) $\widehat{\mathcal{R}}$ is better.

### 3.2 Bayesian Model Evidence as a Baseline

The marginal likelihood (model evidence)

$$
\mathcal{Z}(M) = \int p(D_{\text{train}} \mid \boldsymbol{\theta}, M)\, p(\boldsymbol{\theta} \mid M)\, d\boldsymbol{\theta}
$$

is a prior-averaged measure of fit. For the conjugate Gaussian illustration of Section 4.2, $\mathcal{Z}$ reduces to the marginal density of the sample mean under the conjugate model, evaluated at the observed $\bar{y}$; we use this closed form for transparency. The Bayes factor between models $M_1$ and $M_2$ is

$$
\text{BF}_{12} = \frac{\mathcal{Z}(M_1)}{\mathcal{Z}(M_2)}.
$$

A Bayes factor above 1 favors $M_1$, but Bayes factors reward fit without rewarding predictive novelty: a framework that fits known data with many parameters can dominate one that predicts new data with few. We therefore combine the two terms into a composite **Epistemic-Risk Score (ERS)**:

$$
\text{ERS}(M) = -\log\mathcal{Z}(M) + \lambda\,\widehat{\mathcal{R}}(M),
$$

with $\lambda > 0$ balancing fit against predictive risk. The ERS is lower for models that both fit the training data and score well out of sample. A framework that only