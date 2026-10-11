# Ensemble Drafting: A Draft-Then-Verify Framework Unifying Population-Level Control and Speculative Inference

## Abstract

We introduce *ensemble drafting*, a draft-then-verify computational framework in which a single broadcast signal (the draft) is generated cheaply, propagated to a population of verifiers, and accepted or rejected by a costly authoritative check. The framework abstracts two settings that have developed independently: ensemble control of large populations of structurally identical dynamical systems, where inputs can only be broadcast at the population level, and speculative decoding for large-model inference, where small draft models propose tokens that a large model verifies in parallel. We formalize ensemble drafting as a stochastic process with a draft acceptance probability $\alpha$, a per-token draft cost ratio $\rho$, and a fixed verification cost ratio $\nu$, and we derive the expected number of accepted draft units per round, $E_k[A] = (1-\alpha^k)/(1-\alpha)$, and the throughput gain $S(k)$. For representative parameters ($\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$) we compute the optimal draft length $k^{\ast} = 7$ and gain $S \approx 2.3244$, and we show that a two-member ensemble draft with independent errors ($\alpha = 0.75$ effective, doubled draft cost) improves the gain over a single weak drafter from $1.3462$ to $1.5254$, a relative improvement of $13.3\%$. We position the framework against the ensemble-control and speculative-decoding literatures, state its assumptions and failure modes, and identify the conditions under which the claims would be falsified.

## 1. Introduction

Many computational and control problems share a hidden structure: a cheap, imperfect proposal mechanism produces candidate outputs; an expensive, authoritative mechanism checks them; and the system's throughput is determined by how well the cheap mechanism's errors are managed. In ensemble control, a single input signal is broadcast to a large population of structurally identical dynamical systems, and the controller cannot address individual members [8]; the population-level constraint makes feedback and actuation severely underactuated [5]. In speculative decoding for large vision-language models, small draft models quickly generate draft tokens that a large model verifies in parallel, trading draft errors for verification parallelism [3]. Both are instances of what we call *ensemble drafting*: draft at the population level, verify once, accept what survives.

The contribution of this paper is threefold. First, we give a minimal formal model of ensemble drafting with three parameters: the per-unit draft acceptance probability $\alpha$, the draft-to-target cost ratio $\rho$, and the fixed verification cost ratio $\nu$. Second, we derive closed-form expressions for the expected accepted throughput and the optimal draft length, and we compute concrete numerical results with full arithmetic. Third, we show how ensemble drafting — using multiple independent drafters whose proposals are pooled — changes the optimal operating point, and we quantify the trade-off between the acceptance-probability gain and the multiplied draft cost.

The paper is deliberately conservative: every quantitative claim is either derived here with shown arithmetic or explicitly labeled a projection with stated assumptions. Claims about prior work are restricted to what the supplied abstracts of those works state.

## 2. Background and Related Work

**Speculative decoding and ensemble drafting in inference.** TABED addresses speculative decoding for Large Vision-Language Models (LVLMs), which extend LLMs to process both image and text prompts; its abstract states that speculative decoding has proven effective for accelerating LLM inference by quickly generating draft tokens and verifying them in parallel, that SD remains largely unexplored for LVLMs, and that the work benchmarks existing inference methods with small draft models on 11 datasets across diverse input settings [3]. The supplied abstract is truncated before its methodological details, so we rely on it only for the problem statement (draft-then-verify acceleration for multimodal models) and the benchmark scope (11 datasets). Our framework treats exactly the draft-then-verify loop that [3] benchmarks, but as an abstract stochastic process rather than a system to be measured.

**Ensemble control.** Moment-Based Ensemble Control studies the control of a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations, and identifies the severely underactuated nature of such systems and the inability to avail comprehensive state feedback as the central challenges in analysis and design [5]. Ensemble Control on Lie Groups frames the same population-level setting on Lie groups, noting that in applications from quantum control and robotics to brain medicine, control can only be implemented at the population level by broadcasting an input signal to all systems [8]. Both works supply the conceptual core of our framework: the draft is a broadcast signal, and the verifier plays the role of the population-level constraint that prevents individual addressing. Neither abstract reports quantitative throughput results, so we borrow structure, not numbers, from them.

**Verification and formal proof.** The formally verified constructive proof of the consistency of Peano Arithmetic modifies Gentzen's 1936 proof using Gödel's reformulation, adding details and corrections necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment [2]. This is a second sense of "verification as expensive authority": the cut-elimination argument is the costly check, and the ordinal assignment is the draft-side bookkeeping that makes the check tractable. The abstract is truncated before reporting the verification tooling, so we cite it only for its stated content.

**Decoupling and reduction patterns.** Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes shows how spherical symmetry allows an expansion in scalar, vector, and tensor harmonics under which the perturbative equations decouple for modes of different parity and harmonic number [4]. Prescriptive Master Integrals of Maximal Weight at Two Loops constructs a spanning set of individually pure, planar master integrals in which every independent infrared-divergent region is matched by specific masters while all other masters are manifestly finite in four dimensions [6]. Both exemplify the pattern our framework exploits: isolate the expensive (divergent, coupled) part so that the cheap part can be drafted and the expensive part verified once. The Asymptotic of Bergman Kernel master thesis gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle where the curvature is positive and satisfies a local spectral gap condition, introducing a semi-classical symbol space and symbolic calculus inspired by recent work of Hsiao and Savale [7]; the abstract is truncated, so we use it only as an instance of asymptotic reduction as pre-verification simplification.

**Chaos as a failure mode of drafting.** The draft paper on chaos in DNA inversions proves that the inversion process occurring in DNA mutations is chaotic in the sense of Devaney's theory [1]. We invoke it as a cautionary instance: if the proposal mechanism is chaotic, small draft errors amplify, and the accept-what-survives strategy degrades. The abstract states the claim and the Devaney criterion but no quantitative rates.

**QNFO corpus context.** The QNFO Consilient Synthesis v2.0 document describes a shared adelic kernel (valuation → tree boundary → Ostrowski → adeles) and applies seven corrections (C1–C7) from a 2026-07-25 red-team audit, restructured kernel-first with an honest kernel-membership table and mandatory symmetry sections [9]. NUMERATA extends an 8-axis framework for evaluating numeral systems with Distinction-Based Primality as a ninth axis and reports meta-analysis validation with MCS = 0.875 and 5/5 predictions confirmed, using sunburst notation to make primality visually immediate [10]. Connecting Geometrogenesis and Biogenesis is listed in the corpus without a supplied abstract, so no substantive claim about its content can be made here [11]. The Kappa/SIIT cross-validation reports a direct mathematical cross-validation of the Kappa / Scale-Invariant Information Thermodynamics framework (Quni-Gudzinas, 2025, Zenodo 17218944/17230397) against the Standard Model's known 1-loop renormalization-group β-functions through the single definition $g_{\text{eff}} = g_0 \kappa$ [12]; the abstract is truncated mid-definition, so we cite it only as an instance of cross-validation of a draft framework against an authoritative reference computation — precisely the draft-then-verify pattern of Section 3.

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

This mirrors the population-level broadcast of ensemble control [5, 8]: the draft is broadcast to all would-be consumers, and only the verifier has "individual addressing."

### 3.2 Ensemble drafting with $m$ independent drafters

With $m$ independent drafters, we assume the pooled proposal is accepted if at least one drafter's unit is correct; under independence the effective acceptance probability is

$$\alpha_m = 1 - (1-\alpha)^m.$$

The draft cost multiplies: $\rho_m = m\rho$. This is the ensemble analogue of broadcasting to a population: diversity in the draft pool substitutes for individual drafter quality.

### 3.3 Objective

Let $A_k$ be the number of accepted units in a round with draft length $k$. The throughput gain is

$$S(k) = \frac{E_k[A]}{\rho\,k + \nu},$$

i.e., accepted units per unit of normalized cost. The optimal draft length is $k^{\ast} = \arg\max_{k \ge 1} S(k)$.

## 4. Analysis

All arithmetic in this section is shown step by step. Inputs are stated at each use.

### 4.1 Expected accepted units

Since acceptance of the first $i$ units requires $i-1$ consecutive correct drafts, $\Pr(A_k \ge i) = \alpha^{i-1}$ for $1 \le i \le k$, and $\Pr(A_k \ge i) = 0$ for $i > k$. Therefore

$$E_k[A] = \sum_{i=1}^{k} \Pr(A_k \ge i) = \sum_{i=1}^{k} \alpha^{i-1} = \frac{1-\alpha^k}{1-\alpha}.$$

**Check with explicit numbers.** Take $\alpha = 0.8$ (source: chosen representative value for this derivation; no external source claims this value), $k = 7$:

$$\alpha^7 = 0.8^7 = 0.2097152,$$
$$E_7[A] = \frac{1 - 0.2097152}{1 - 0.8} = \frac{0.7902848}{0.2} = 3.951424.$$

### 4.2 Optimal draft length: continuous condition

Maximize $f(k) = (1-\alpha^k)/(\rho k + \nu)$ over real $k > 0$. Setting $f'(k) = 0$:

$$\frac{(-\alpha^k \ln \alpha)(\rho k + \nu) - \rho(1-\alpha^k)}{(\rho k + \nu)^2} = 0,$$

$$\alpha^k\left[(-\ln\alpha)(\rho k + \nu) + \rho\right] = \rho,$$

$$\boxed{\;\alpha^k = \frac{\rho}{\rho + (-\ln\alpha)(\rho k + \nu)}\;}$$

an implicit equation for $k^{\ast}$.

**Consistency check.** With $\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$: $-\ln 0.8 = 0.22314355$. At $k = 7$:

- Left side: $\alpha^7 = 0.2097152$.
- Right side: $\dfrac{0.1}{0.1 + 0.22314355 \times (0.1 \times 7 + 1)} = \dfrac{0.1}{0.1 + 0.22314355 \times 1.7} = \dfrac{0.1}{0.1 + 0.37934404} = \dfrac{0.1}{0.47934404} = 0.208618$.

Left and right agree to within $|0.2097152 - 0.208618| = 0.0011$, confirming $k^{\ast} \approx 7$.

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

Sample arithmetic: $S(7) = 3.951424 / 1.7 = 2.324367$; $S(8) = 4.1611392 / 1.8 = 2.311744$. The discrete maximum is at $k^{\ast} = 7$ with

$$S_{\max} = 2.324367.$$

### 4.4 Ensemble of two drafters

Take a single weak drafter with $\alpha = 0.5$, $\rho = 0.1$, $\nu = 1$.

**Single drafter.** $E_k[A] = (1 - 0.5^k)/0.5 = 2(1 - 0.5^k)$:

- $k=2$: $E = 2(1-0.25) = 1.5$; $S = 1.5/1.2 = 1.250000$.
- $k=3$: $E = 2(1-0.125) = 1.75$; $S = 1.75/1.3 = 1.346154$.
- $k=4$: $E = 2(1-0.0625) = 1.875$; $S = 1.875/1.4 = 1.339286$.

Optimum $k^{\ast} = 3$, $S_{\text{single}} = 1.346154$.

**Two-drafter ensemble.** Effective acceptance probability:

$$\alpha_2 = 1 - (1-0.5)^2 = 1 - 0.25 = 0.75.$$

Draft cost doubles: $\rho_2 = 0.2$. Then $E_k[A] = (1 - 0.75^k)/0.25 = 4(1 - 0.75^k)$:

- $k=3$: $0.75^3 = 0.421875$; $E = 4 \times 0.578125 = 2.3125$; $S = 2.3125/(0.2 \times 3 + 1) = 2.3125/1.6 = 1.445313$.
- $k=4$: $0.75^4 = 0.31640625$; $E = 4 \times 0.68359375 = 2.734375$; $S = 2.734375/1.8 = 1.519097$.
- $k=5$: $0.75^5 = 0.2373046875$; $E = 4 \times 0.7626953125 = 3.05078125$; $S = 3.05078125/2.0 = 1.525391$.
- $k=6$: $0.75^6 = 0.177978515625$; $E = 4 \times 0.822021484375 = 3.2880859375$; $S = 3.2880859375/2.2 = 1.494585$.

Optimum $k^{\ast} = 5$, $S_{\text{ens}} = 1.525391$.

**Relative improvement.**

$$\frac{S_{\text{ens}}}{S_{\text{single}}} = \frac{1.525391}{1.346154} = 1.133139,$$

i.e., a $13.3\%$ relative gain, and the optimal draft length lengthens from $k^{\ast} = 3$ to $k^{\ast} = 5$ because the higher acceptance probability makes longer drafts worthwhile despite the doubled draft cost.

### 4.5 Break-even drafter quality

The ensemble beats the single strong drafter of Section 4.3 only if $S_{\text{ens}} > S_{\text{single}}$. As a labeled projection (not a measurement): with $m$ drafters each of quality $\alpha$, the ensemble gain is bounded above by the single-drafter gain at $\alpha_m = 1-(1-\alpha)^m$ with cost $m\rho$. For the ensemble to beat the $\alpha = 0.8$ single drafter ($S = 2.324367$), a two-drafter pool of quality $\alpha$ would need $S(k; \alpha_2, 0.2, 1) > 2.324367$; evaluating the best case $\alpha_2 \to 1$ gives $E_k[A] \to k$ and $S \le k/(0.2k+1)$, which is increasing in $k$ but bounded by $1/0.2 = 5$ asymptotically; at $k = 10$, $S = 10/3 = 3.333333 > 2.324367$. Hence a sufficiently good ensemble pool can in principle exceed a strong single drafter, but only when $\alpha_2$ is high enough that the longer optimal draft length compensates the doubled cost; locating the exact threshold $\alpha$ is left as an open numerical problem (Section 6).

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

1. **Expected accepted units.** $E_k[A] = (1-\alpha^k)/(1-\alpha)$; at $\alpha = 0.8$, $k = 7$: $E_7[A] = 3.951424$.
2. **Optimal draft length (single drafter, $\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$).** $k^{\ast} = 7$, with maximum gain $S_{\max} = 2.324367$. The continuous optimality condition $\alpha^k = \rho/[\rho + (-\ln\alpha)(\rho k + \nu)]$ is satisfied at $k = 7$ to within $0.0011$.
3. **Weak single drafter ($\alpha = 0.5$).** $k^{\ast} = 3$, $S_{\text{single}} = 1.346154$.
4. **Two-drafter ensemble ($\alpha_2 = 0.75$, $\rho_2 = 0.2$).** $k^{\ast} = 5$, $S_{\text{ens}} = 1.525391$, a relative improvement of $13.3\%$ ($1.133139\times$) over the weak single drafter.
5. **Projection (labeled, with assumptions).** Under the independence assumption of Section 3.2 and the cost model of Section 3.3, a two-drafter pool can exceed a strong single drafter ($S = 2.324367$) only if its pooled acceptance probability is high enough; the upper envelope $S \le k/(0.2k+1)$ reaches $3.333333$ at $k = 10$, so the threshold exists in principle. The exact threshold value of $\alpha$ is not computed here and is stated as an open quantity.

## 6. Discussion

**Limitations of the model.** The independence assumption behind $\alpha_m = 1-(1-\alpha)^m$ is the framework's weakest point: real drafters trained on similar data make correlated errors, which inflates $\alpha_m$ relative to reality and biases the ensemble result of Section 4.4 optimistically. The prefix-rejection rule assumes verification is all-or-nothing per unit and that a single parallel pass costs $\nu$ regardless of $k$; if verification cost grows with draft length, the denominator $\rho k + \nu$ becomes $\rho k + \nu(k)$ and the optimal $k^{\ast}$ shortens. The cost normalization treats draft and target units as commensurable, which is exact in the token-cost abstraction but not necessarily in wall-clock terms on specific hardware.

**Failure modes.** If the draft mechanism is chaotic in the sense of Devaney's theory — as the DNA-inversion draft paper argues for that biological process [1] — small proposal errors amplify and the prefix-acceptance throughput collapses; our model has no chaos parameter and would silently misestimate performance in such regimes. If the verifier itself is imperfect (false accepts), the framework's gain is overstated because accepted-but-wrong units are counted as throughput.

**What would falsify the claims.** The claim that ensemble drafting with $m = 2$ improves throughput by $13.3\%$ over a weak single drafter is a consequence of three assumptions: independence, doubled-but-linear draft cost, and fixed verification cost. Measuring correlated-error rates high enough that $\alpha_2 < 0.75$ in practice, or superlinear draft costs, would falsify the sign of the improvement. The claim that $k^{\ast} = 7$ at $\alpha = 0.8$ is falsified if verification cost scales with $k$ strongly enough that the discrete maximum moves below 7; the sensitivity shown in the table ($S(6) = 2.305800$ vs. $S(8) = 2.311744$) indicates the optimum is shallow, so modest model misspecification can move $k^{\ast}$ by $\pm 1$ without large loss.

**Open questions.** (i) Compute the exact break-even acceptance probability $\alpha$ at which a two-drafter pool beats a strong single drafter (Section 4.5 gives bounds only). (ii) Extend the model to correlated drafters via a mixture model and re-derive $\alpha_m$. (iii) Test whether the decoupling pattern seen in perturbation theory [4] and master-integral bases [6] admits a formal statement within the drafting framework. (iv) The QNFO corpus items [9, 10, 12] suggest cross-validation patterns (e.g., validating a framework against Standard Model 1-loop β-functions [12]) that could serve as case studies; the truncated abstract of [12] prevents a deeper comparison here, and [11] has no supplied abstract at all, so no claim about its content is made.

**Arguing against ourselves.** A skeptic could say the framework merely renames the well-known draft-then-verify loop of speculative decoding [3] and the broadcast-control structure of ensemble control [5, 8], adding algebra without new empirical content. The response is that the value is in the shared parameterization: it makes the ensemble-diversity trade-off (Section 4.4) computable across domains, and it generates falsifiable thresholds (Section 4.5) rather than qualitative analogies. But until the thresholds are checked against measured systems, the framework's contribution remains structural, not empirical.

## 7. Conclusion

We presented ensemble drafting, a three-parameter draft-then-verify framework unifying population-level ensemble control and speculative inference. We derived the expected accepted throughput $E_k[A] = (1-\alpha^k)/(1-\alpha)$, the implicit optimality condition for the draft length, and computed concrete operating points: $k^{\ast} = 7$ and $S = 2.324367$ for a strong single drafter, and a $13.3\%$ ensemble improvement over a weak single drafter under stated independence assumptions. The framework's claims are falsifiable through its three assumptions, and its open problems — correlated drafters, break-even thresholds, and cross-domain case studies — are stated explicitly.

## References

[1] arXiv:1105.1512v1 | Chaos in DNA inversions (Draft paper)
[2] arXiv:2603.00487v1 | DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments
[3] arXiv:2601.20357v1 | TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs
[4] arXiv:2108.08668v3 | Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes
[5] arXiv:2009.02646v1 | Moment-Based Ensemble Control
[6] arXiv:2610.10672v1 | Prescriptive Master Integrals of Maximal Weight at Two Loops
[7] arXiv:2202.03383v1 | Asymptotic of Bergman Kernel (Master Thesis)
[8] arXiv: