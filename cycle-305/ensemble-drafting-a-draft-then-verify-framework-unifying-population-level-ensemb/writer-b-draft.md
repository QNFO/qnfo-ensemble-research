# Ensemble Drafting: A Draft-Then-Verify Framework Unifying Population-Level Ensemble Control and Speculative Inference

## Abstract

Many computational and control systems share a hidden structure: a cheap, imperfect proposal mechanism produces candidate outputs, and an expensive, authoritative mechanism verifies them in a single pass. We call the abstraction of this structure *ensemble drafting*. It unifies two bodies of work that have developed independently: ensemble control, in which a single input is broadcast to a large population of structurally identical dynamical systems with parametric variations and no individual addressing is possible, and speculative decoding, in which small draft models propose tokens that a large model verifies in parallel. We formalize ensemble drafting with three parameters — the per-unit draft acceptance probability $\alpha$, the draft-to-target cost ratio $\rho$, and the verification cost ratio $\nu$ — and derive the expected accepted throughput $E_k[A] = (1-\alpha^k)/(1-\alpha)$ and the throughput gain $S(k) = E_k[A]/(\rho k + \nu)$. For a strong single drafter ($\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$) we compute the optimal draft length $k^{*} = 7$ and gain $S = 2.324367$. For a pool of $m$ independent drafters we derive the pooled acceptance probability $\alpha_m = 1-(1-\alpha)^m$ and show, for two weak drafters ($\alpha = 0.5$, pooled $\alpha_2 = 0.75$, doubled draft cost), an improvement in optimal gain from $1.346154$ to $1.525391$, a relative gain of $13.3\%$; for three drafters the relative gain ranges from $1.251877$ to $1.330302$ as per-drafter quality falls from $\alpha = 0.6$ to $\alpha = 0.4$. All quantitative results are analytical projections from stated assumptions, with every arithmetic step shown; we identify the independence assumption as the principal failure mode and give explicit falsification criteria.

## 1. Introduction

Engineers who operate large populations of similar systems, and engineers who serve inference from large models, face the same economic problem: the authoritative mechanism is accurate but expensive, and the cheap alternative is fast but wrong some of the time. In ensemble control, a single input signal is broadcast to a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations, and the controller cannot address individual members; the severely underactuated nature of such systems and the inability to avail comprehensive state feedback are the central difficulties [6]. In many applications control can only be implemented at the population level, by broadcasting an input signal to all systems in the population [8]. In speculative decoding, small draft models quickly generate draft tokens that a large model verifies in parallel; the technique has proven effective for accelerating language-model inference but remains largely unexplored for Large Vision-Language Models (LVMs that process both image and text prompts), and existing work benchmarks inference methods with small draft models on 11 datasets across diverse input settings [4]. In legged robotics, a cheap contact classifier decides when the zero-velocity update may correct state drift, and a wrong acceptance corrupts the odometry that downstream mapping and navigation depend on [2]. In each case the operator must choose how much to trust the cheap proposal, how long a block of proposals to accept before checking, and whether to spend resources on a better single proposer or on several cheap ones.

Today these decisions are made separately in each field, with field-specific heuristics and no shared quantitative target. A practitioner tuning a draft length, sizing a drafter ensemble, or deciding whether to pool drafters has no closed-form expression to compare against, and no explicit statement of which assumption, if violated, destroys the benefit. If a common framework holds, the practitioner gains three things: a formula that predicts throughput from three measurable parameters, an optimal operating point computed from those parameters, and a falsification criterion that says exactly which measurement would refute the model.

This paper supplies that framework, which we call *ensemble drafting*: draft at the population level, verify once, accept what survives. The contribution is a framework, not a system. Specifically:

1. We give a minimal formal model of ensemble drafting with three parameters ($\alpha$, $\rho$, $\nu$) and an extension to $m$ independent drafters whose proposals are pooled (Section 3).
2. We derive closed-form expressions for expected accepted throughput and the optimal draft length, and we compute concrete numerical operating points with full arithmetic (Section 4).
3. We quantify the ensemble-diversity trade-off — pooling several weak drafters versus one strong drafter — and state the assumptions whose violation would falsify the results (Sections 4, 5 and 6).

The paper is deliberately conservative: every quantitative claim is either derived here with shown arithmetic or explicitly labeled a projection with stated assumptions. No experiments were run; the value of the framework is that it makes its assumptions falsifiable and gives system builders closed-form targets against which measured performance can be compared.

## 2. Background and Related Work

We organize related work into four threads: speculative decoding and multimodal drafting; ensemble control; verification and formal proof; and decoupling, reduction and falsification patterns in mathematics and in research practice.

**Speculative decoding and multimodal drafting.** TABED addresses speculative decoding for Large Vision-Language Models. Its introduction frames LVLMs as models specializing in prompts comprised of text and images, attracting attention for applications including multimodal chatbots, visual question answering, and augmented reality [4]. The work benchmarks existing inference methods with small draft models on 11 datasets across diverse input settings, and its experimental section reports that neither multimodal nor text-only drafting consistently outperformed the other: multimodal drafting showed higher block efficiency in single-turn scenarios across most benchmark datasets, while text-only drafting often surpassed it in subsequent turns and significantly in out-of-distribution cases [4]. TABED itself dynamically ensembles multiple drafts obtained via batch inference, achieving the best or second-best performance across all scenarios with an average robust expected walltime speedup of $1.74\times$ and over $5\%$ improvement over single drafting methods, without additional tuning and with negligible ensembling costs [4]. Two points of that work bear directly on our framework. First, the scenario-specific fluctuation of single drafters is exactly the weakness that pooling is meant to address, and TABED's ensemble result is empirical evidence that combining drafters helps; our Section 4.4 gives the analytical counterpart under an independence assumption. Second, TABED's measured $1.74\times$ speedup is a concrete number against which our closed-form gain predictions can be checked once $\alpha$, $\rho$ and $\nu$ are estimated for that system; our framework supplies the prediction, TABED's setup supplies the measurement opportunity.

**Ensemble control.** Moment-Based Ensemble Control studies the control of a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations, identifying the severely underactuated nature of such systems and the inability to avail comprehensive state feedback as the significant challenges in analysis and design [6]. That work defines an ensemble system as a parameterized population $\frac{d}{dt}x(t,\beta)=F(x(t,\beta),\beta,u(t))$ with parameter $\beta$ on a compact set $\Omega$, and the control problem as designing a parameter-independent input $u(t)$ steering the whole ensemble [6]. Crucially for us, it observes that in many applications placing dedicated sensors on individual systems is not feasible but an aggregated, population-level measurement can be obtained, and it develops a moment-based framework that closes the feedback loop using such aggregated measurements, showing through the dynamic Hausdorff moment problem that ensemble systems and their moment systems share the same control and controllability properties [6]. This is the direct inspiration for our use of a single scalar acceptance probability $\alpha$ as the population-level state variable: like a moment, $\alpha$ is one number that summarizes the useful behavior of the whole population, and our Section 3.2 pools drafters exactly at that aggregate level.

Ensemble Control on Lie Groups frames the same population-level setting on Lie-group state spaces, noting that such problems arise in numerous scientific areas from quantum control and robotics to brain medicine, and that in many applications control can only be implemented at the population level, i.e., by broadcasting an input signal to all systems in the population [8]. The broadcast-only constraint of [8] maps onto the verifier's single accept/reject decision in ensemble drafting: one signal governs the whole population, and no element receives an individualized input. We borrow this problem structure, not any solution technique or numbers from it.

**Verification as expensive authority.** A formally verified constructive proof of the consistency of Peano Arithmetic revisits Gentzen's 1936 consistency proof, providing a modified version based on Gödel's reformulation with additional details and minor corrections necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment [3]. That work's background explains why the proof must be staged: Gödel's Second Incompleteness Theorem states that any consistent Hilbert calculus containing Robinson Arithmetic cannot prove its own consistency, so Gentzen had to find an alternative formulation that Peano Arithmetic could not prove consistent but which could prove Peano Arithmetic consistent, and the proof technique was cut elimination over a sequent calculus with a non-consistency-preserving Cut rule [3]. In our vocabulary the cut-elimination argument is the costly check and the ordinal assignment is the draft-side bookkeeping that makes the check tractable — a division of labor between cheap bookkeeping and expensive verification that our framework formalizes. The same work also documents the practical cost of verification: formalizing the proof in Coq required completing an abandoned prior attempt, fixing existing bugs, and rebuilding machinery for ordinals, proof trees and inversion principles [3], which illustrates concretely why verification is the expensive side of the asymmetry.

**Decoupling and reduction patterns.** Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes shows that spherical symmetry allows an expansion of perturbations in scalar, vector, and tensor harmonics under which the perturbative equations decouple for modes with different parity and different harmonic numbers [5]. Our independence analysis in Section 3.2 exploits the same decoupling idea: under independence, the joint behavior of the drafter pool factorizes into per-drafter terms, exactly as harmonic modes decouple in [5]. That work also demonstrates the discipline we apply to our own assumptions: its conclusions state exactly which assumptions were made (linear combinations of metric perturbations, coefficients depending only on the radial coordinate, wave-type equations) and which branch of results is new versus already known [5], a model of assumption bookkeeping that our Section 3.4 imitates.

Prescriptive Master Integrals of Maximal Weight at Two Loops constructs a spanning set of individually pure, planar master integrals involving massless particles in four dimensions, including all maximal-weight contributions at two loops, such that every independent region associated with infrared divergence is individually matched by specific masters while all other masters are manifestly finite [7]. This "one region, one responsible component" design is the ideal we adopt for the aggregator in Section 3.2: each acceptance outcome should be attributable to a specific, local event (all drafters failed at a position), so failure analysis stays local. That work's conclusion adds that a key advantage of a prescriptive basis is that coefficients can be directly calculated in terms of on-shell functions [7] — the same benefit a closed-form gain formula offers over empirical tuning.

The Asymptotic of Bergman Kernel master thesis gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle at points where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi-classical symbol space and related symbolic calculus inspired from recent work of Hsiao and Savale [8]. We use it as an instance of the discipline that asymptotic reductions are valid only where their hypotheses hold — the expansion holds at points where the curvature is positive and satisfies the spectral gap condition, not everywhere — a discipline we apply to the validity region of our own independence assumption in Section 6.

**Cheap proposals gating expensive updates in robotics.** Learning Contact Representation for Leg Odometry addresses the subproblem that leg odometry relies on the assumption that the velocity of a foot in stance is zero with respect to the world, making accurate contact detection critical; many approaches classify contact using ground reaction force sensors, yet these sensors are not available on all legged robots and remain unresponsive to disturbances such as slippage while the foot is stationary [2]. Its experiments show that supervised CNN and GRU contact classifiers achieve the highest classification scores in simulation (F1 up to $0.998$) but degrade on the physical robot (F1 down to $0.868$–$0.921$), and — most relevant here — that higher pseudo-label classification accuracy does not necessarily translate into better leg odometry; instead, the zero-velocity update reduces state estimation drift when its covariance is scaled by the posterior of a Gaussian mixture model fitted in a learned latent space [2]. This is a physical instantiation of draft-then-verify with a lesson our framework encodes: the acceptance decision (apply the zero-velocity update) should be gated by a calibrated confidence, not by raw proposal accuracy, because the cost of a wrong acceptance is paid by the expensive downstream mechanism. It also supplies measured numbers showing that proposal quality is domain-shift sensitive — a concrete warning for our assumption that $\alpha$ is a stable parameter.

**Chaos as a failure mode of drafting.** A draft paper on chaos in DNA inversions proves that the inversion process occurring in DNA mutations is chaotic as defined by Devaney's theory [1]. The work builds this on a model in which the set of trinucleotides is divided at each time $t$ into a subset that can possibly mutate and a subset that cannot, with mutating trinucleotides picked uniformly at random, a model the original authors called a "chaotic model" [1]. We invoke it as a cautionary instance: if a proposal mechanism is chaotic in this sense, small errors in drafted proposals can amplify, and the accept-what-survives strategy degrades. The work gives the mechanism qualitatively rather than quantitative amplification rates, so we use it qualitatively only.

**Falsification-oriented methodology.** The Kappa/SIIT cross-validation paper documents a research program that proposed a bold, falsifiable unifying mechanism, tested it against known physics, found it wanting, retracted it, and in the process cross-validated a framework that correctly reproduced the gauge-coupling β-functions the original mechanism could not [10]. Its own account of the retraction is instructive for our Section 6: version 3.0 retracted the central logistic β-function ansatz after direct calculation showed it incompatible with the textbook 1-loop QED β-function — a difference in universality class, not just a numerical mismatch [10]. We adopt the same standard: our framework states its assumptions so that a single calculation or measurement can refute them, and Section 6 names the specific observations that would do so.

**Assumption auditing as maintenance.** The QNFO consilient gap synthesis catalogs 42 gaps across 5 structural categories and finds that the gap dependency graph is a directed acyclic graph with depth at most 3, so a bounded number of phases can resolve all gaps, with the top 5 high-severity gaps transitively blocking approximately 40% of all gaps [9]. We use this as a structural analogy for assumption auditing: the assumptions A1–A4 of Section 3.4 form a small dependency graph, and A2 (drafter independence) is the keystone — the analogue of a high-severity gap that transitively blocks the most downstream claims. The consilient synthesis v2.0, which incorporates all 7 corrections mandated by a red-team audit and is restructured around a kernel-first spine, exemplifies the practice of restructuring a framework around its load-bearing core after adversarial review [11]; our Section 6 performs the same reorganization in miniature by making A2 the explicit center of the failure analysis.

## 3. Methods

### 3.1 The ensemble drafting process

Fix a target system $T$ (the authoritative verifier) and a draft mechanism $D$. One *round* proceeds as follows:

1. $D$ proposes a draft block of $k$ units (tokens, control inputs, proof steps).
2. $T$ verifies the block in a single parallel pass of fixed cost.
3. The maximal prefix of correct units is accepted; the round ends at the first rejection.

The model has three parameters:

- $\alpha \in (0,1)$: the probability that any single drafted unit is correct, assumed independent across units.
- $\rho > 0$: the cost of drafting one unit, measured in units of the target's per-unit cost.
- $\nu > 0$: the cost of one verification pass, likewise normalized.

This mirrors the population-level broadcast of ensemble control [6, 8]: the draft is broadcast to all would-be consumers, and only the verifier has individual addressing. It also mirrors the gated-update structure of leg odometry [2], where a cheap per-step classification decides whether the expensive state-correction mechanism acts.

### 3.2 Ensemble drafting with $m$ independent drafters

With $m$ independent drafters, we assume the pooled proposal is accepted if at least one drafter's unit is correct. Under independence of drafter errors, the effective acceptance probability is

$$\alpha_m = 1 - (1-\alpha)^m.$$

The draft cost multiplies: $\rho_m = m\rho$. This is the ensemble analogue of broadcasting to a population: diversity in the draft pool substitutes for individual drafter quality. The pooled acceptance probability $\alpha_m$ plays the role of the aggregated measurement in moment-based ensemble control [6] — a single scalar sufficient statistic for the population's useful behavior — and its factorized form rests on the same decoupling structure exemplified by the harmonic decomposition of [5]. The aggregator follows the prescriptive ideal of [7]: an acceptance failure is attributable to one local event (all $m$ drafters failed at that position), so diagnosis stays local.

### 3.3 Objective

Let $A_k$ be the number of accepted units in a round with draft length $k$. The throughput gain is

$$S(k) = \frac{E_k[A]}{\rho\,k + \nu},$$

i.e., accepted units per unit of normalized cost. The optimal draft length is $k^{*} = \arg\max_{k \ge 1} S(k)$. When comparing a multi-drafter configuration to a single-drafter baseline, we also report the *relative gain* $S_{\text{rel}} = S_{\text{ens}}/S_{\text{single}}$, evaluated at each configuration's own optimal draft length.

### 3.4 Assumptions

- **A1 (per-unit acceptance).** Each drafted unit is correct with probability $\alpha$, independently across units.
- **A2 (drafter independence).** Drafter errors are independent across the $m$ drafters, so $\alpha_m = 1-(1-\alpha)^m$. This is the strongest assumption and the main target of Section 6.
- **A3 (fixed verification cost).** One verification pass costs $\nu$ regardless of $k$ and $m$.
- **A4 (linear draft cost).** Drafting $k$ units with $m$ drafters costs $m\rho k$.

Results derived under A1 alone are marked *combinatorial*; results using A2–A4 are marked *cost-dependent*. As in the assumption bookkeeping of [5], each result below carries the assumptions it uses, so a violation of any one assumption can be traced to the specific claims it invalidates.

## 4. Analysis

All arithmetic in this section is shown step by step; inputs are stated at each use. All results are analytical projections under A1–A4, not measurements.

### 4.1 Expected accepted units

Since acceptance of the first $i$ units requires $i-1$ consecutive correct drafts, $\Pr(A_k \ge i) = \alpha^{i-1}$ for $1 \le i \le k$ and $\Pr(A_k \ge i) = 0$ for $i > k$. Therefore

$$E_k[A] = \sum_{i=1}^{k} \Pr(A_k \ge i) = \sum_{i=1}^{k} \alpha^{i-1} = \frac{1-\alpha^k}{1-\alpha}.$$

**Check with explicit numbers.** Take $\alpha = 0.8$ (chosen representative value; no external source claims it), $k = 7$:

$$\alpha^7 = 0.8^7 = 0.2097152,$$
$$E_7[A] = \frac{1 - 0.2097152}{1 - 0.8} = \frac{0.7902848}{0.2} = 3.951424.$$

### 4.2 Optimal draft length: continuous condition

Maximize $f(k) = (1-\alpha^k)/(\rho k + \nu)$ over real $k > 0$. Setting $f'(k) = 0$:

$$\frac{(-\alpha^k \ln \alpha)(\rho k + \nu) - \rho(1-\alpha^k)}{(\rho k + \nu)^2} = 0,$$

which rearranges to the implicit condition

$$\alpha^k = \frac{\rho}{\rho + (-\ln\alpha)(\rho k + \nu)}.$$

**Consistency check.** With $\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$: $-\ln 0.8 = 0.22314355$. At $k = 7$:

- Left side: $\alpha^7 = 0.2097152$.
- Right side: $\dfrac{0.1}{0.1 + 0.22314355 \times (0.1 \times 7 + 1)} = \dfrac{0.1}{0.1 + 0.22314355 \times 1.7} = \dfrac{0.1}{0.47934404} = 0.208618$.

Left and right agree to within $|0.2097152 - 0.208618| = 0.001097$, confirming $k^{*} \approx 7$.

### 4.3 Discrete optimum and gain (single drafter)

Compute $S(k) = E_k[A]/(0.1k + 1)$ for $\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$:

| $k$ | $\alpha^k$ | $E_k[A] = (1-\alpha^k)/0.2$ | $\rho k + \nu$ | $S(k)$ |
|---|---|---|---|---|
| 4 | 0.4096 | 2.952000 | 1.4 | 2.108571 |
| 5 | 0.32768 | 3.361600 | 1.5 | 2.241067 |
| 6 | 0.262144 | 3.689280 | 1.6 | 2.305800 |
| 7 | 0.2097152 | 3.951424 | 1.7 | 2.324367 |
| 8 | 0.16777216 | 4.1611392 | 1.8 | 2.311744 |
| 9 | 0.134217728 | 4.32891136 | 1.9 | 2.278374 |

Sample arithmetic: $S(7) = 3.951424 / 1.7 = 2.324367$; $S(8) = 4.1611392 / 1.8 = 2.311744$. The discrete maximum is at $k^{*} = 7$ with $S_{\max} = 2.324367$.

### 4.4 Ensemble of two drafters versus one weak drafter

Take a single weak drafter with $\alpha = 0.5$, $\rho = 0.1$, $\nu = 1$.

**Single drafter.** $E_k[A] = (1 - 0.5^k)/0.5 = 2(1 - 0.5^k)$:

- $k=2$: $E = 2(1-0.25) = 1.5$; $S = 1.5/1.2 = 1.250000$.
- $k=3$: $E = 2(1-0.125) = 1.75$; $S = 1.75/1.3 = 1.346154$.
- $k=4$: $E = 2(1-0.0625) = 1.875$; $S = 1.875/1.4 = 1.339286$.

Optimum $k^{*} = 3$, $S_{\text{single}} = 1.346154$.

**Two-drafter ensemble.** Pooled acceptance probability:

$$\alpha_2 = 1 - (1-0.5)^2 = 1 - 0.25 = 0.75.$$

Draft cost doubles: $\rho_2 = 0.2$. Then $E_k[A] = (1 - 0.75^k)/0.25 = 4(1 - 0.75^k)$:

- $k=3$: $0.75^3 = 0.421875$; $E = 4 \times 0.578125 = 2.3125$; $S = 2.3125/(0.2 \times 3 + 1) = 2.3125/1.6 = 1.445313$.
- $k=4$: $0.75^4 = 0.31640625$; $E = 4 \times 0.68359375 = 2.734375$; $S = 2.734375/1.8 = 1.519097$.
- $k=5$: $0.75^5 = 0.2373046875$; $E = 4 \times 0.7626953125 = 3.05078125$; $S = 3.05078125/2.0 = 1.525391$.
- $k=6$: $0.75^6 = 0.177978515625$; $E = 4 \times 0.822021484375 = 3.2880859375$; $S = 3.2880859375/2.2 = 1.494585$.

Optimum $k^{*} = 5$, $S_{\text{ens}} = 1.525391$.

**Relative improvement.**

$$\frac{S_{\text{ens}}}{S_{\text{single}}} = \frac{1.525391}{1.346154} = 1.133147,$$

i.e., a $13.3\%$ relative gain. The optimal draft length lengthens from $k^{*} = 3$ to $k^{*} = 5$ because the higher pooled acceptance probability makes longer drafts worthwhile despite the doubled draft cost.

### 4.5 Three drafters at moderate quality

Take $m = 3$ drafters each with $\alpha = 0.6$, per-drafter unit cost $\rho = 0.05$, $\nu = 1$, and fix the draft length $k = 4$ (this parameter choice is an illustrative assumption, not a measurement).

**Pooled acceptance probability.**

$$\alpha_3 = 1 - (1-0.6)^3 = 1 - 0.4^3 = 1 - 0.064 = 0.936.$$

Intermediate values: $0.4^2 = 0.16$; $0.4^3 = 0.064$.

**Expected accepted units at $k = 4$.**

$$E_4[A] = \frac{1 - 0.936^4}{1 - 0.936}.$$

Compute: $0.936^2 = 0.876096$; $0.936^4 = 0.876096^2 = 0.767544169216$. Then

$$E_4[A] = \frac{1 - 0.767544169216}{0.064} = \frac{0.232455830784}{0.064} = 3.632122356.$$

**Single-drafter baseline** ($\alpha = 0.6$, $\rho = 0.05$, $k = 4$):

$$E_4[A] = \frac{1 - 0.6^4}{1 - 0.6} = \frac{1 - 0.1296}{0.4} = \frac{0.8704}{0.4} = 2.176.$$

**Absolute throughputs.** Ensemble: $S_{\text{ens}} = 3.632122356/(0.15 \times 4 + 1) = 3.632122356/1.6 = 2.270076473$. Single: $S_{\text{single}} = 2.176/(0.05 \times 4 + 1) = 2.176/1.2 = 1.813333$.

**Relative gain.**

$$S_{\text{rel}} = \frac{2.270076473}{1.813333} = 1.251877.$$

### 4.6 Sensitivity to single-drafter quality

Recompute the relative gain of Section 4.5 at $\alpha = 0.4$, $m = 3$, $k = 4$, $\rho = 0.05$, $\nu = 1$:

$$\alpha_3 = 1 - 0.6^3 = 1 - 0.216 = 0.784.$$

$0.784^2 = 0.614656$; $0.784^4 = 0.614656^2 = 0.377802$ (to six decimals). Then

$$E_4[A] = \frac{1 - 0.377802}{0.216} = \frac{0.622198}{0.216} = 2.880546.$$

**Ensemble throughput.** With $m = 3$ drafters the draft cost is $\rho_3 = 3 \times 0.05 = 0.15$, so

$$S_{\text{ens}} = \frac{2.880546}{0.15 \times 4 + 1} = \frac{2.880546}{1.6} = 1.800341.$$

**Single-drafter baseline** at $\alpha = 0.4$, $\rho = 0.05$, $k = 4$: $0.4^4 = 0.0256$, so

$$E_4[A] = \frac{1 - 0.0256}{1 - 0.4} = \frac{0.9744}{0.6} = 1.624,$$

$$S_{\text{single}} = \frac{1.624}{0.05 \times 4 + 1} = \frac{1.624}{1.2} = 1.353333.$$

**Relative gain.**

$$S_{\text{rel}} = \frac{1.800341}{1.353333} = 1.330302.$$

Thus lowering per-drafter quality from $\alpha = 0.6$ to $\alpha = 0.4$ changes the three-drafter relative gain from $1.251877$ (Section 4.5) to $1.330302$: weaker individual drafters make pooling more valuable, because the pooled probability $\alpha_m = 1-(1-\alpha)^m$