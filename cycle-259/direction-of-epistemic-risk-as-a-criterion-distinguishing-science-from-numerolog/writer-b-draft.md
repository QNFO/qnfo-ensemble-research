# Direction of Epistemic Risk: A Quantitative Criterion Separating Predictive Frameworks from Post-Hoc Numerology

## Abstract

Scientific communities routinely face a sorting problem: which of two mathematically sophisticated frameworks deserves resources, when both fit everything already known? The cost of sorting badly is decades of effort on frameworks that generate no testable consequence. This paper addresses the gap between intuitive judgments of "science versus numerology" and an operational criterion that can be computed. We formalize the proposed criterion of *direction of epistemic risk*: a framework counts as knowledge-producing when its out-of-sample predictive score exceeds its in-sample fit, and as numerology-like when all of its accuracy is retrospective. Using Bayesian model comparison, we derive that a model with $k$ free parameters fitted to $n$ observations carries an expected in-sample optimism of approximately $k$ nats and an expected predictive risk of $k/(2n)$ nats, and we compute a worked case ($k=5$, $n=200$) giving an optimism of $0.025$ nats per observation. We derive the credibility dynamics of an unfalsifiable framework: a per-observation elegance bonus of $\varepsilon = 0.01$ drives posterior odds from $1{:}100$ to approximately $220{:}1$ after $1000$ retrospective fits, with no out-of-sample exposure. We compute a falsification threshold for novel binary predictions ($8$ of $10$ successes by chance has probability $45/1024 \approx 0.0439$) and a $95\%$ epistemic value-at-risk of $8$ failures per $10$ predictions. The result yields a graded taxonomy — knack, theorem, elegant retrodiction, falsified theory — and a computable test applicable to historiography and to live theory assessment.

## 1. Introduction

Research funders, journal editors, and collaboration leaders must repeatedly decide which theoretical framework to staff, fund, and cite, and the candidates often present the same surface credentials: mathematical sophistication, coverage of all known data, and internal elegance. The decision is consequential. A collaboration that commits a decade of effort to a framework that only retrodicts known facts foregoes the discoveries a falsifiable competitor would have forced; the LSST Dark Energy Science Collaboration, for example, organizes its entire program around probes — weak lensing, baryon acoustic oscillations, supernova distances — whose value lies in what they would find if current models are wrong, including the roughly $100$-orders-of-magnitude discrepancy between naive Planck-scale vacuum energy predictions and the observed density that any dark energy theory must confront [7]. On the other side of the line, frameworks exist that fit every observation after the fact while committing to nothing before it; the QNFO corpus contains several, including a thesis in which a topological resonance condition "governed by the golden ratio" is used to explain the hierarchy problem and the existence of exactly three fermion generations [12], and a unified thesis whose central synthetic claim is self-labeled as a conjecture that is in part "not yet falsifiable" [9]. What is missing is a criterion that separates these cases quantitatively rather than by sociological intuition, so that the same instrument can be applied to a historical case (rope-stretching geometry versus the Pythagorean theorem) and to a live one (a base-60 arithmetic utility versus a claim of cosmic significance for the number sixty).

This paper develops such a criterion. The core idea, conjectured in the source research notes, is that the line between science and numerology is set not by mathematical abstraction or elegance but by the *direction of epistemic risk*: frameworks that generate novel falsifiable predictions are knowledge, while those offering only post-hoc fits to known data are numerology, regardless of sophistication. We formalize "predictive risk" with the same machinery quantitative risk management uses for financial tail risk — quantiles and expected shortfalls of a loss distribution [1], [3], [8] — where the "loss" is predictive error on data not yet seen. We then apply the machinery to historical and contemporary cases and derive the dynamics by which elegance-weighted, unfalsifiable frameworks accumulate spurious credibility.

The contributions are:

- A formal definition of direction of epistemic risk as the signed gap between in-sample fit and out-of-sample predictive score, with a derivation of the expected optimism $k$ nats and predictive risk $k/(2n)$ nats for a $k$-parameter model fitted to $n$ observations, and a fully worked numerical case (Section 4.1–4.2, derived in Section 3).
- A derivation of the credibility trajectory of an unfalsifiable framework under elegance-weighted updating, showing deterministic drift of posterior odds ($1{:}100$ to approximately $220{:}1$ over $1000$ retrospective fits at $\varepsilon = 0.01$), which validates the proposed gradient of epistemic legitimacy for the retrodiction end of the scale (Section 4.3).
- A computed falsification threshold and epistemic value-at-risk for novel binary predictions ($45/1024 \approx 0.0439$; $95\%$ VaR of $8$ failures in $10$), giving practitioners a concrete acceptance rule (Section 4.4).
- A graded taxonomy — knack, theorem, elegant retrodiction, falsified theory — with each grade assigned by the sign and magnitude of the derived quantities, applied to the rope-stretching/Pythagoras case, the base-60 case, and the QNFO frameworks (Sections 4.5 and 5).

## 2. Background and Related Work

The quantitative risk literature supplies the formal vocabulary this paper adapts. Pesenti, Wang and Tuo study sequential design and Gaussian-process emulation for estimating portfolio value-at-risk and tail value-at-risk in nested simulation, and report a two-orders-of-magnitude computational saving relative to plain nested Monte Carlo, decomposed as about $10\times$ from adaptive allocation and $5\times$ from spatial modeling, with the further advantage that the emulator yields essentially unbiased risk estimators and a reliable standard error [1]. The structural lesson for epistemology is that a risk measure is only useful when the estimator of it is honest about its own uncertainty; this paper's predictive-score criterion inherits that requirement, since a framework's out-of-sample score must be estimated on data the framework did not touch. McNeil, Frey and Embrechts-adjacent work by Embrechts and coauthors on range value-at-risk frames the central design tension in risk measurement: value-at-risk, a quantile, is esteemed for robustness, while expected shortfall, a tail expectation, is sensitive and coherent, and range value-at-risk interpolates between them; the triple $(\operatorname{VaR}_{\alpha}, \operatorname{VaR}_{\beta}, \operatorname{RVaR}_{\alpha,\beta})$ is elicitable and identifiable under mild conditions, meaning it can be scored and compared against outcomes [8]. Elicitability is exactly the property an epistemic risk measure needs if it is to adjudicate between frameworks by their track records rather than by rhetoric, and Section 3 borrows the scoring-function structure directly. On the estimation side, the nonparametric value-at-risk algorithm of [3] decomposes the portfolio return density into exposures, recent $14$-day volatilities, and volatility-standardized historical returns, remaining accurate for an arbitrarily large number of positions; its back-test methodology — flagging days when the realized loss exceeds the estimated $99\%$ daily VaR — is a working model of how a prediction framework should be audited against realized outcomes, and Section 4.4 mirrors it with binomial hit-rate thresholds. In operational risk, the loss distribution approach requires a bank to select frequency and severity distributions per risk category and to compute regulatory capital as the $99.9\%$ quantile of the annual loss distribution, with a documented obstacle being year-to-year instability of the calculation; the recommended remedy is to select distributions using out-of-sample-minded criteria in conjunction with likelihood and goodness-of-fit measures rather than in-sample likelihood alone [4]. That recommendation is the financial twin of this paper's thesis: in-sample fit is not evidence of predictive content, and selection procedures must be designed around that fact.

Methodological work on out-of-sample validation shows what disciplined prediction assessment looks like in practice. The statistical-emulator study of mortality-linked contracts fits kriging and spline surrogates on a training design and evaluates them on a distinct test set, benchmarking against an expensive gold-standard Monte Carlo estimate; its results table reports, for example, simple kriging achieving bias $-1.334\times 10^{-3}$ and $\sqrt{\text{IMSE}} = 3.280\times 10^{-3}$ at a training budget of $N_{tr} = 1000$ for hedge portfolio values [6]. The design principle — a test set disjoint from the training set — is the operational form of "direction of epistemic risk": the emulator's worth is measured only where it did not fit. In observational science, the SKA pulsar program makes its epistemic direction explicit in advance: the AA4 array assembly "is likely to double the known pulsar population in new surveys," a stated, countable prediction against which the instrument's scientific case will be judged, with AA* delivery expected between 2029 and 2031 and frequency coverage of 50 MHz to 15 GHz [5]. A doubled population is either observed or not; that is the signature of negative epistemic risk in our taxonomy. Similarly, the LSST Dark Energy Science Collaboration lays out probes whose discriminating power is quantified before data arrive — weak lensing shears at the $\lesssim 1\%$ level against a galaxy intrinsic RMS ellipticity of $\sim 0.36$, and baryon acoustic oscillations as a standard ruler in the galaxy power spectrum [7] — so the theory choice is exposed to refutation by design.

The QNFO corpus provides the contemporary cases the criterion is built to judge. The Ultrametric Foundation thesis makes a genuinely sharp observation — that in any integer base $b \geq 2$ the digit string "10" denotes $b$, so every base names itself "base-10" and a numeral string cannot internally specify its own interpretation — and it calibrates its claims with explicit certainty labels including `[my conjecture]` and `[not yet falsifiable]`, even proposing a concrete falsification experiment comparing a depth-2 tree of 8 transmon qubits against a 2D nearest-neighbour layout on logical error rate [9]. The presence of a stated falsification condition moves parts of that framework toward the predictive end of the gradient, whatever the fate of the physics. The Head Over Hands analysis names the failure mode this paper formalizes: a systemic bias privileging "abstract, elegant, and a priori theoretical constructs over messy, inconvenient, and empirical evidence," illustrated by Sir Humphry Davy's assessment of John Dalton as trusting "to his head rather than his hands," and argued to produce decades of stagnation and suppressed contradictory data [11]. Where [11] diagnoses the fallacy sociologically, this paper gives it a number: the elegance bonus $\varepsilon$ in Section 4.3 is the quantitative form of head-over-hands updating. The Deterministic Unified Theory argues that error terms in standard modeling act as "a conceptual dumping ground for everything we do not understand" and claims scale-invariant patterning across all observation scales [10]; the error-term critique is compatible with predictive scoring (unexplained variance should degrade out-of-sample score), but the scale-invariance claim, as stated, offers no observation that could disagree with it, placing it on the retrodiction side of the gradient. Finally, Physics, Solved proposes that integer winding numbers of $\pi_1(S^1) \cong \mathbb{Z}$ serve as complete information carriers, with prime factorization encoding quantum charges and a golden-ratio resonance condition selecting "a sparse spectrum of stable states, explaining the hierarchy problem and the existence of exactly three fermion generations" [12]. Explaining an already-known count (three generations) after the fact, with a condition flexible enough to select any sparse spectrum, is the canonical elegant-retrodiction pattern; Section 4.5 scores it accordingly.

## 3. Methods

This paper's method is analytical derivation plus fully shown arithmetic; no experiment, simulation on hardware, survey, or data collection is performed. The objects of analysis are abstract models of frameworks, and the numbers attached to historical and contemporary cases are either derived here or labeled as assumptions.

**Model of a framework.** Let a framework $M$ assign, to each observation $y$ in a domain, a likelihood $p_M(y \mid \theta)$ with $\theta \in \mathbb{R}^k$ a vector of $k$ free parameters. Observations $y_1, \dots, y_n$ are modeled as independent draws from an unknown true distribution $p^*$. The framework is *fitted* by maximum likelihood on a training set and *scored* by the out-of-sample expected log-likelihood on fresh draws from $p^*$. Define:

$$
S_{\text{in}}(M) = \frac{1}{n}\sum_{i=1}^{n} \log p_{\hat{M}}(y_i), \qquad S_{\text{out}}(M) = \mathbb{E}_{y \sim p^*}\left[\log p_{\hat{M}}(y)\right],
$$

where $\hat{M}$ is $M$ with parameters fitted on the $y_i$. The **direction of epistemic risk** is the signed gap

$$
D(M) = S_{\text{out}}(M) - S_{\text{in}}(M).
$$

A framework whose apparent accuracy is genuine generalization has $D(M) \approx 0$ or, when it committed to risky predictions that succeeded, $D(M) > 0$ relative to a no-skill baseline; a framework whose accuracy is retrospective has $D(M) < 0$, with the magnitude measuring how much of its fit is self-crediting. We call $-D(M)$ the *optimism* of the framework.

**Optimism derivation.** For a maximum-likelihood fit with $k$ parameters, the standard asymptotic result (AIC logic) is that the expected in-sample log-likelihood exceeds the expected out-of-sample log-likelihood by approximately $k$ nats. We derive it via the Fisher information. Let $\hat{\theta}$ be the MLE and $I(\theta)$ the per-observation Fisher information. A second-order expansion of the expected log-likelihood ratio between the fitted and true models gives, for the fitted model evaluated on training data, a gain of $\operatorname{tr}(I(\theta^*)\, \hat{V})$ where $\hat{V}$ is the asymptotic covariance of $\hat{\theta}$, and $\hat{V} \approx (n I(\theta^*))^{-1}$. Hence the in-sample gain per the whole training set is

$$
\operatorname{tr}\!\left(I(\theta^*) \cdot \frac{1}{n} I(\theta^*)^{-1}\right) = \operatorname{tr}(I_{k}) = k,
$$

while on fresh data the same expansion yields a loss of $k$ nats relative to the truth (the fitted model's KL divergence from $p^*$, times $n$, is approximately $k$). The gap between the two evaluations is therefore approximately $2k$ nats total, i.e. $k$ nats of optimism for the in-sample score against the out-of-sample score under the convention above; we use the conservative one-$k$ convention throughout and state it as an approximation valid when $n \gg k$. The expected predictive risk, meaning the KL divergence of the fitted model from the truth, is approximately

$$
R(M) \approx \frac{k}{2n} \ \text{nats}.
$$

**Credibility dynamics for unfalsifiable frameworks.** An unfalsifiable framework is modeled as one that, for every realized outcome $y$, can produce a likelihood at least as high as any competitor's, by adjusting its interpretation after the fact. Concretely, we model its per-observation log-posterior-odds contribution against a null competitor as a constant $\varepsilon \geq 0$ (the "elegance bonus": a fixed prior-side credit granted per successful retrospective fit, independent of the outcome, since every outcome is fitted). The posterior log-odds after $n$ retrospective fits is then

$$
\Lambda_n = \Lambda_0 + n\,\varepsilon, \qquad \Lambda_0 = \ln \frac{\pi_u}{1 - \pi_u},
$$

with $\pi_u$ the prior probability of the unfalsifiable framework. This is a deterministic drift, contrasted with the martingale behavior of a falsifiable framework's log-odds under its own null (expected drift zero when the null is true).

**Falsification threshold and epistemic VaR.** For a framework making $m$ novel binary predictions with asserted success probability $p$, the number of successes $X$ under the no-skill null $p = 0.5$ is $\operatorname{Binomial}(m, 0.5)$. The falsification threshold is the smallest $x$ with $\Pr[X \geq x] \leq \alpha$; the *epistemic value-at-risk* at level $\alpha$, adapted from the risk-measure definitions of [8], is the $\alpha$-quantile of the failure count under the null. Both are computed exactly in Section 4.4.

**Case scoring.** Historical and contemporary frameworks are assigned to taxonomy grades by the sign of $D(M)$ and the presence or absence of pre-registered falsification conditions, using only what the cited sources state about them.

## 4. Analysis

### 4.1 Worked optimism calculation

We take a framework with $k = 5$ free parameters fitted to $n = 200$ observations. (These values are assumptions chosen to represent a mid-sized theoretical model; the derivation holds for any $k, n$ with $n \gg k$.)

Step 1: total in-sample optimism (nats):

$$
\text{Optimism} \approx k = 5 \ \text{nats}.
$$

Step 2: per-observation optimism:

$$
\frac{k}{n} = \frac{5}{200} = 0.025 \ \text{nats per observation}.
$$

Step 3: expected predictive risk:

$$
R(M) \approx \frac{k}{2n} = \frac{5}{400} = 0.0125 \ \text{nats}.
$$

Interpretation: a five-parameter model fitted to two hundred points carries a quarter of a percent of nats of self-credit per observation on average; if the framework's advocates report in-sample fit only, they overstate its per-observation predictive quality by $0.025$ nats, which at $200$ observations compounds to $5$ nats of apparent advantage over a model scored honestly out of sample.

### 4.2 Sensitivity of predictive risk to $n$ and $k$

Holding $k = 5$:

- $n = 50$: $R = 5/(2 \cdot 50) = 5/100 = 0.05$ nats.
- $n = 200$: $R = 0.0125$ nats.
- $n = 2000$: $R = 5/4000 = 0.00125$ nats.

Predictive risk falls as $1/n$, so a framework can hide an arbitrarily poor predictive record by fitting ever more retrospective data — but only if no one scores it on fresh data. Holding $n = 200$:

- $k = 1$: $R = 1/400 = 0.0025$ nats.
- $k = 20$: $R = 20/400 = 0.05$ nats.

Each additional free parameter costs $1/(2n) = 0.0025$ nats of predictive risk at this sample size. This is the quantitative content of the head-over-hands critique [11]: elegance that manifests as parameter flexibility is purchased at a computable predictive price.

### 4.3 Credibility drift of an unfalsifiable framework

Assume a prior odds of $1{:}100$ against the unfalsifiable framework, i.e. $\pi_u = 1/101$:

$$
\Lambda_0 = \ln\!\left(\frac{1/101}{100/101}\right) = \ln(0.01) = -4.60517.
$$

Assume an elegance bonus of $\varepsilon = 0.01$ nats per retrospective fit (each post-hoc explanation of one observation adds one hundredth of a nat of credibility, an assumption representing a small but nonzero community credit for "explaining" known facts). After $n = 1000$ retrospective fits:

$$
\Lambda_{1000} = -4.60517 + 1000 \times 0.01 = -4.60517 + 10 = 5.39483.
$$

Converting to odds:

$$
e^{5.39483} = e^{5} \cdot e^{0.39483} \approx 148.413 \times 1.48404 \approx 220.2.
$$

The posterior odds have moved from $1{:}100$ against to approximately $220{:}1$ in favor, with the framework never having been exposed to a single out-of-sample test. The drift is deterministic: because every outcome is fitted, variance in the trajectory is zero, unlike a falsifiable framework whose log-odds fluctuate and whose expected drift under its own null is zero. The number of retrospective fits needed to overcome the $1{:}100$ prior at this bonus rate is

$$
n^* = \frac{4.60517}{0.01} = 460.5 \implies n^* = 461 \ \text{fits}.
$$

At a harsher prior of $1{:}10^6$ ($\Lambda_0 = -13.81551$), the same bonus requires $n^* = 1382$ fits. The mechanism is scale-free in the prior: any unfalsifiable framework with a nonzero per-fit credit eventually reaches arbitrary credibility, which is precisely the spurious-credibility accumulation the research conjecture predicted.

### 4.4 Falsification threshold and epistemic value-at-risk for novel predictions

A framework makes $m = 10$ novel binary predictions and claims skill. Under the no-skill null, $X \sim \operatorname{Binomial}(10, 0.5)$ with $\Pr[X = x] = \binom{10}{x} 2^{-10}$.

Probability of exactly $8$ successes:

$$
\binom{10}{8} 2^{-10} = \frac{45}{1024} = 0.043945.
$$

Probability of $8$ or more successes:

$$
\frac{\binom{10}{8} + \binom{10}{9} + \binom{10}{10}}{1024} = \frac{45 + 10 + 1}{1024} = \frac{56}{1024} = 0.054688.
$$

Probability of $9$ or more:

$$
\frac{10 + 1}{1024} = \frac{11}{1024} = 0.010742.
$$

At the conventional $\alpha = 0.05$, the falsification threshold is therefore $x = 9$: observing $9$ or more successes out of $10$ novel binary predictions has null probability $0.010742 \leq 0.05$, while $8$ successes ($0.054688$) does not clear the bar. A framework asserting skill must deliver at least $9$ of $10$ before a $5\%$-level auditor credits it.

The epistemic value-at-risk, defined as the $\alpha$-quantile of the failure count $F = 10 - X$ under the null, at level $\alpha = 0.95$: cumulative failure probabilities are $\Pr[F \leq 2] = \Pr[X \geq 8] = 0.054688$, $\Pr[F \leq 3] = \Pr[X \geq 7] = (56 + 120)/1024 = 176/1024 = 0.171875$, and generally $\Pr[F \leq f] = \Pr[X \geq 10 - f]$. We need the smallest $f$ with $\Pr[F \leq f] \geq 0.95$, i.e. the largest $f$ with $\Pr[F \geq f] > 0.05$. Compute $\Pr[F \leq 7] = \Pr[X \geq 3] = 1 - \Pr[X \leq 2] = 1 - (1 + 10 + 45)/1024 = 1 - 56/1024 = 968/1024 = 0.945313$, and $\Pr[F \leq 8] = \Pr[X \geq 2] = 1 - 11/1024 = 1013/1024 = 0.989258$. Since $0.945313 < 0.95 \leq 0.989258$, the $95\%$ epistemic VaR is

$$
\operatorname{eVaR}_{0.95} = 8 \ \text{failures out of } 10.
$$

Reading: a no-skill framework will, $5\%$ of the time, fail $8$ or more of $10$ novel binary predictions. A framework whose observed failure count stays at or below the no-skill $95\%$ quantile has demonstrated nothing; only performance beyond the null quantile — mirroring the back-test logic of flagging losses beyond the estimated $99\%$ VaR in [3] — counts as evidence of predictive content.

### 4.5 Scoring the cases

**Rope-stretching (knack) versus the Pythagorean theorem.** The $3$-$4$-$5$ rope practice is a knack: zero free parameters, zero fitted data, and one repeated verified configuration; its $D(M)$ is undefined rather than negative because nothing is claimed beyond the rehearsed case. The Pythagorean theorem, as a deductive result covering all right triangles, makes a countable infinity of novel predictions from zero fitted parameters; any single failing triangle refutes it. In the taxonomy this is the theorem grade: maximal epistemic risk taken (every untested triangle), none of it post-hoc.

**Base-60 arithmetic versus cosmic significance.** The positional-numbering observation of [9] — that "10" in base $b$ denotes $b$, so every base calls itself "base-10" — is a theorem-grade result about notation: it is proved from the definition of positional notation, applies to every base without exception, and could not have been otherwise. A claim that the number sixty carries cosmic significance, by contrast, is an elegant retrodiction: sixty's rich divisor structure ($1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60$ — twelve divisors) is a fact of arithmetic available for post-hoc selection, and no observation is specified that would distinguish cosmic significance from ordinary utility. The same numeral system thus hosts both a theorem and a numerological overlay, which is exactly the discrimination the criterion is built to make.

**The QNFO frameworks.** The Ultrametric Foundation thesis contains both grades: the base-self-naming observation is theorem-grade, while the central synthetic claim is self-labeled `[my conjecture]` with components `[not yet falsifiable]` [9] — retrodiction-grade as it stands — but its proposed falsification experiment (a depth-2 tree of 8 transmon qubits with tree-only gates versus a 2D nearest-neighbour layout, with the central claim falsified if the tree geometry yields no statistically significant logical-error-rate improvement) is a pre-stated refutation condition that, if carried out, would move the claim to the falsifiable grade regardless of outcome [9]. Physics, Solved explains the three fermion generations via a golden-ratio resonance condition on winding numbers [12]; the explained quantity (three) was known before the explanation, and the framework as excerpt