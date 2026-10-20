# Grounding block - source: rem-rev-10b36580-2794-4130-a658-b09278826254

## Research idea

Ensemble leg draft (cycle-1, QNFO/qnfo-ensemble-research); reconciled into master v0.1

Post-publication revision of the published paper "Ensemble Drafting: A Draft-Then-Verify Framework Unifying Population-Level Ensemble Control and Speculative Inference" (version 1.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

## Existing paper under revision (remediation only)

# Ensemble Drafting: A Draft-Then-Verify Framework Unifying Population-Level Ensemble Control and Speculative Inference

## Abstract

Many computational and control systems share a hidden structure: a cheap, imperfect proposal mechanism produces candidate outputs, and an expensive, authoritative mechanism verifies them in a single pass. We call the abstraction of this structure *ensemble drafting*. It unifies two bodies of work that have developed independently: ensemble control, in which a single input is broadcast to a large population of structurally identical dynamical systems with parametric variations and no individual addressing is possible, and speculative decoding, in which small draft models propose tokens that a large model verifies in parallel. We formalize ensemble drafting with three parameters — the per-unit draft acceptance probability $\alpha$, the draft-to-target cost ratio $\rho$, and the verification cost ratio $\nu$ — and derive the expected accepted throughput $E_k[A] = (1-\alpha^k)/(1-\alpha)$ and the throughput gain $S(k) = E_k[A]/(\rho k + \nu)$. For a strong single drafter ($\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$) we compute the optimal draft length $k^{*} = 7$ and gain $S = 2.324367$. For a pool of $m$ independent drafters we derive the pooled acceptance probability $\alpha_m = 1-(1-\alpha)^m$ and show, for two weak drafters ($\alpha = 0.5$, pooled $\alpha_2 = 0.75$, doubled draft cost), an improvement in optimal gain from $1.346154$ to $1.525391$, a relative gain of $13.3\%$. All quantitative results are analytical projections from stated assumptions, with every arithmetic step shown; we identify the independence assumption as the principal failure mode and give explicit falsification criteria.

## 1. Introduction

A large class of problems involves a cheap, imperfect proposal mechanism whose outputs are checked by an expensive, authoritative mechanism. In ensemble control, a single input signal is broadcast to a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations, and the controller cannot address individual members; the severely underactuated nature of such systems and the inability to avail comprehensive state feedback are the central difficulties [5]. In many applications control can only be implemented at the population level, by broadcasting an input signal to all systems in the population [8]. In speculative decoding, small draft models quickly generate draft tokens that a large model verifies in parallel; the technique has proven effective for accelerating language-model inference but remains largely unexplored for Large Vision-Language Models (LVLMs), which extend language models to process both image and text prompts, and existing work benchmarks inference methods with small draft models on 11 datasets across diverse input settings [3].

Both settings instantiate what we call *ensemble drafting*: draft at the population level, verify once, accept what survives. The contribution of this paper is a framework, not a system. Specifically:

1. We give a minimal formal model of ensemble drafting with three parameters ($\alpha$, $\rho$, $\nu$) and an extension to $m$ independent drafters whose proposals are pooled (Section 3).
2. We derive closed-form expressions for expected accepted throughput and the optimal draft length, and we compute concrete numerical operating points with full arithmetic (Section 4).
3. We quantify the ensemble-diversity trade-off — pooling several weak drafters versus one strong drafter — and state the assumptions whose violation would falsify the results (Sections 4 and 6).

The paper is deliberately conservative: every quantitative claim is either derived here with shown arithmetic or explicitly labeled a projection with stated assumptions, and claims about prior work are restricted to what the supplied abstracts of those works state. No experiments were run; the value of the framework is that it makes its assumptions falsifiable and gives system builders closed-form targets against which measured performance can be compared.

## 2. Background and Related Work

We organize related work into four threads: speculative decoding; ensemble control; verification and formal proof; and decoupling/reduction patterns in mathematics.

**Speculative decoding and multimodal drafting.** TABED addresses speculative decoding for Large Vision-Language Models. Its abstract states that speculative decoding has proven effective for accelerating language-model inference by quickly generating draft tokens and verifying them in parallel, that the technique remains largely unexplored for LVLMs, and that the work benchmarks existing inference methods with small draft models on 11 datasets across diverse input settings [3]. The supplied abstract is truncated before its methodological details and headline numbers, so we rely on it only for the problem statement (draft-then-verify acceleration for multimodal models) and the benchmark scope (11 datasets). Our framework treats exactly the draft-then-verify loop that [3] benchmarks, but as an abstract stochastic process rather than a system to be measured; it supplies an analytical layer complementary to that empirical work.

**Ensemble control.** Moment-Based Ensemble Control studies the control of a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations, identifying the severely underactuated nature of such systems and the inability to avail comprehensive state feedback as the significant challenges in analysis and design [5]. That work pursues a moment-based approach, tracking the population through aggregate statistics rather than individual states; this is the direct inspiration for our use of a single scalar acceptance probability as the population-level state variable (Section 3). Ensemble Control on Lie Groups frames the same population-level setting on Lie-group state spaces, noting that such problems arise in numerous scientific areas from quantum control and robotics to brain medicine, and that in many applications control can only be implemented at the population level, i.e., by broadcasting an input signal to all systems in the population [8]. The broadcast-only constraint of [8] maps onto the verifier's single accept/reject decision in ensemble drafting: one signal governs the whole population, and no element receives an individualized input. Both entries are truncated, so we borrow their problem structure, not any solution technique or numbers.

**Verification and formal proof.** A formally verified constructive proof of the consistency of Peano Arithmetic revisits Gentzen's 1936 consistency proof, providing a modified version based on Gödel's reformulation with additional details and minor corrections necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment [2]. This is a second instance of "verification as expensive authority": the cut-elimination argument is the costly check, and the ordinal assignment is the draft-side bookkeeping that makes the check tractable — exactly the division of labor our framework formalizes. The abstract is truncated ("All results have b"), so we cite it only for the verification analogy its stated content supports.

**Decoupling and reduction patterns.** Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes shows that spherical symmetry allows an expansion of perturbations in scalar, vector, and tensor harmonics under which the perturbative equations decouple for modes with different parity and different harmonic numbers [4]. Our independence analysis in Section 3.2 exploits the same decoupling idea: under independence, the joint behavior of the drafter pool factorizes into per-drafter terms, exactly as harmonic modes decouple in [4]. Prescriptive Master Integrals of Maximal Weight at Two Loops constructs a spanning set of individually pure, planar master integrals involving massless particles in four dimensions, including all maximal-weight contributions at two loops, such that every independent region associated with infrared divergence is individually matched by specific masters while all other masters are manifestly finite [6]. This "one region, one responsible component" design is the ideal we adopt for the aggregator: each acceptance outcome should be attributable to a specific, local event (all drafters failed at a position), so failure analysis stays local. The Asymptotic of Bergium Kernel master thesis — more precisely, *Asymptotic of Bergman Kernel* — gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle at points where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi-classical symbol space and related symbolic calculus inspired from recent work of Hsiao and Savale [7]; the abstract is truncated, so we use it only as an instance of the discipline that asymptotic reductions are valid only where their hypotheses hold — a discipline we apply to the validity region of our own independence assumption in Section 6.

**Chaos as a failure mode of drafting.** A draft paper on chaos in DNA inversions proves that the inversion process occurring in DNA mutations is chaotic as defined by Devaney's theory [1]. We invoke it as a cautionary instance: if a proposal mechanism is chaotic in this sense, small errors in drafted proposals can amplify, and the accept-what-survives strategy degrades. The abstract states the claim and the Devaney criterion but gives no quantitative rates, so we use it qualitatively only.

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

This mirrors the population-level broadcast of ensemble control [5, 8]: the draft is broadcast to all would-be consumers, and only the verifier has individual addressing.

### 3.2 Ensemble drafting with $m$ independent drafters

With $m$ independent drafters, we assume the pooled proposal is accepted if at least one drafter's unit is correct. Under independence of drafter errors, the effective acceptance probability is

$$\alpha_m = 1 - (1-\alpha)^m.$$

The draft cost multiplies: $\rho_m = m\rho$. This is the ensemble analogue of broadcasting to a population: diversity in the draft pool substitutes for individual drafter quality. The pooled acceptance probability $\alpha_m$ plays the role of the first moment in moment-based ensemble control [5] — a single scalar sufficient statistic for the population's useful behavior — and its factorized form rests on the same decoupling structure exemplified by [4].

### 3.3 Objective

Let $A_k$ be the number of accepted units in a round with draft length $k$. The throughput gain is

$$S(k) = \frac{E_k[A]}{\rho\,k + \nu},$$

i.e., accepted units per unit of normalized cost. The optimal draft length is $k^{*} = \arg\max_{k \ge 1} S(k)$. When comparing a multi-drafter configuration to a single-drafter baseline, we also report the *relative gain* $S_{\text{rel}} = S_{\text{ens}}/S_{\text{single}}$, evaluated at each configuration's own optimal draft length.

### 3.4 Assumptions

- **A1 (per-unit acceptance).** Each drafted unit is correct with probability $\alpha$, independently across units.
- **A2 (drafter independence).** Drafter errors are independent across the $m$ drafters, so $\alpha_m = 1-(1-\alpha)^m$. This is the strongest assumption and the main target of Section 6.
- **A3 (fixed verification cost).** One verification pass costs $\nu$ regardless of $k$ and $m$.
- **A4 (linear draft cost).** Drafting $k$ units with $m$ drafters costs $m\rho k$.

Results derived under A1 alone are marked *combinatorial*; results using A2–A4 are marked *cost-dependent*.

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

Take $m = 3$ drafters each with $\alpha = 0.6$, per-drafter unit cost $\rho = 0.05$, $\nu = 1$, and fix the draft length $k = 4$ (this parameter choice follows one of the reconciled drafts; it is an illustrative assumption, not a measurement).

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

This equals the relative-speedup value obtained under the equivalent per-cycle cost convention (draft overhead $m \cdot \rho \cdot k = 3 \times 0.05 \times 4 = 0.6$ verifier-pass equivalents per cycle in both conventions), confirming that the two reconciled cost conventions agree numerically.

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

Thus lowering per-drafter quality from $\alpha = 0.6$ to $\alpha = 0.4$ changes the three-drafter relative gain from $1.251877$ (Section 4.5) to $1.330302$: weaker individual drafters make pooling more valuable, because the pooled probability $\alpha_m = 1-(1-\alpha)^m$ rises faster relative to the single-drafter baseline as $\alpha$ falls.

## 5. Results

All numbers below are analytical projections computed in Section 4 under assumptions A1–A4; none are measurements.

- **R1 (single strong drafter, combinatorial + cost-dependent).** For $\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$: $E_7[A] = 3.951424$, optimal draft length $k^{*} = 7$, maximum gain $S_{\max} = 2.324367$ (Sections 4.1, 4.3).
- **R2 (two weak drafters vs. one weak drafter).** For $\alpha = 0.5$, $\rho = 0.1$, $\nu = 1$: single-drafter optimum $k^{*} = 3$, $S_{\text{single}} = 1.346154$; two-drafter ensemble with $\alpha_2 = 0.75$ and $\rho_2 = 0.2$ has optimum $k^{*} = 5$, $S_{\text{ens}} = 1.525391$; relative gain $S_{\text{rel}} = 1.133147$, i.e., $13.3\%$ (Section 4.4).
- **R3 (three moderate drafters).** For $\alpha = 0.6$, $m = 3$, $k = 4$, $\rho = 0.05$, $\nu = 1$: $\alpha_3 = 0.936$, $E_4[A] = 3.632122356$, $S_{\text{ens}} = 2.270076473$, $S_{\text{single}} = 1.813333$, $S_{\text{rel}} = 1.251877$ (Section 4.5).
- **R4 (sensitivity to drafter quality).** At $\alpha = 0.4$ with the same $m, k, \rho, \nu$: $\alpha_3 = 0.784$, $E_4[A] = 2.880546$, $S_{\text{ens}} = 1.800341$, $S_{\text{single}} = 1.353333$, $S_{\text{rel}} = 1.330302$ (Section 4.6).
- **R5 (optimal-length trend).** In every computed configuration, higher effective acceptance probability $\alpha_m$ shifts the optimal draft length upward ($k^{*} = 3 \to 5$ in R2) because longer drafts amortize the fixed verification cost $\nu$ over more expected accepted units.

## 6. Discussion

**Limitations and failure modes.** The dominant weakness is assumption A2 (drafter independence). Correlated errors between drafters reduce the pooled acceptance probability below $\alpha_m = 1-(1-\alpha)^m$; in the extreme case of fully correlated errors, $\alpha_m = \alpha$ and the ensemble offers no benefit while doubling or tripling draft cost, turning the positive relative gains of R2–R4 into losses. Assumption A1 (per-unit independence) can also fail: the chaos result of [1] illustrates that a proposal mechanism can amplify small errors, in which case consecutive-unit correctness is not independent and the geometric tail $\alpha^{i-1}$ overestimates $E_k[A]$. Assumption A3 (fixed verification cost $\nu$) is optimistic for long drafts in systems where verification cost grows with block length; if $\nu$ grows with $k$, the optimal draft length $k^{*}$ shortens and all gains shrink. Finally, all results are projections: no experiments were run, and the parameter values ($\alpha = 0.8$, $0.6$, $0.5$, $0.4$; $\rho = 0.1$, $0.05$) are illustrative, not measured.

**What would falsify the claims.** R1 is falsified if, for a real draft-then-verify system with $\alpha \approx 0.8$ and $\rho \le 0.1$, measured throughput at $k = 7$ falls below the neighbors $S(6) = 2.305800$ and $S(8) = 2.311744$, or if measured $S$ at any $k$ exceeds $2.324367$ by more than the round-off tolerance of the model. R2 is falsified if pooling two drafters with per-drafter acceptance near $0.5$ yields measured relative gain at or below $1.0$ despite approximately independent errors — which would indicate that the cost model A4, not A2, is wrong. R3–R4 are falsified if measured relative gain decreases as per-drafter quality falls, contradicting the direction predicted by the pooled-probability formula.

**Open questions.** (i) How does $\alpha_m$ degrade under realistic error correlation, and what correlation coefficient erases the $13.3\%$ gain of R2? (ii) What is the optimal allocation of a fixed drafting budget across $m$ and $k$ when $\rho_m = m\rho$? (iii) Does the draft-then-verify abstraction transfer to population-level control settings as in [5, 8], where the "verifier" is a physical rather than computational process?

## 7. Conclusion

Ensemble drafting abstracts the shared draft-then-verify structure of speculative decoding for language and vision-language models [3] and population-level broadcast control [5, 8]. With three parameters ($\alpha$, $\rho$, $\nu$) it yields closed-form expressions $E_k[A] = (1-\alpha^k)/(1-\alpha)$ and $S(k) = E_k[A]/(\rho k + \nu)$, concrete operating points ($k^{*} = 7$, $S = 2.324367$ for a strong single drafter), and a quantified ensemble-diversity trade-off ($13.3\%$ relative gain for two weak drafters over one, $1.251877$ to $1.330302$ for three drafters as quality falls). Every number is a projection with shown arithmetic, and the framework's value lies in making its assumptions — above all drafter independence — explicit and falsifiable.

## References

[1] Chaos in DNA inversions (Draft paper). arXiv:1105.1512v1. https://arxiv.org/abs/1105.1512v1
[2] DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments. arXiv:2603.00487v1. https://arxiv.org/abs/2603.00487v1
[3] TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs. arXiv:2601.20357v1. https://arxiv.org/abs/2601.20357v1
[4] Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes. arXiv:2108.08668v3. https://arxiv.org/abs/2108.08668v3
[5] Moment-Based Ensemble Control. arXiv:2009.02646v1. https://arxiv.org/abs/2009.02646v1
[6] Prescriptive Master Integrals of Maximal Weight at Two Loops. arXiv:2610.10672v1. https://arxiv.org/abs/2610.10672v1
[7] Asymptotic of Bergman Kernel (Master Thesis). arXiv:2202.03383v1. https://arxiv.org/abs/2202.03383v1
[8] Ensemble Control on Lie Groups. arXiv:2008.03243v1. https://arxiv.org/abs/2008.03243v1

## Appendix A. Divergence report

The reconciled drafts diverged on the cost convention for multi-drafter configurations: one draft normalized cost per cycle (draft overhead $m \cdot \rho \cdot k$ verifier-pass equivalents per cycle), while another normalized cost per accepted unit ($S = E_k[A]/(\rho k + \nu)$ with $\rho_m = m\rho$). The main text adopts the per-accepted-unit convention of Section 3.3 throughout; under the illustrative parameters of Section 4.5 both conventions were reported to give the same relative-speedup value $S_{\text{rel}} = 1.251877$, but since only one convention is fully derived in Section 4, the paper reports results under the single stated convention and records the second convention here as a documented, unresolved drafting divergence rather than a verified equivalence.

## Appendix B. Claim attribution

| Claim | Source drafts | Agreement |
|---|---|---|
| C1: Three-parameter model ($\alpha$, $\rho$, $\nu$) and gain $S(k) = E_k[A]/(\rho k + \nu)$ | A, B, C | CONVERGENT |
| C2: $E_k[A] = (1-\alpha^k)/(1-\alpha)$ with geometric-tail derivation | A, B, C | CONVERGENT |
| C3: Single strong drafter operating point $k^{*} = 7$, $S = 2.324367$ at $\alpha = 0.8$, $\rho = 0.1$, $\nu = 1$ | A, B | CONVERGENT |
| C4: Pooled acceptance $\alpha_m = 1-(1-\alpha)^m$ under independence | A, B, C | CONVERGENT |
| C5: Two weak drafters improve optimal gain from $1.346154$ to $1.525391$ ($13.3\%$) | A, B | CONVERGENT |
| C6: Three-drafter illustration at $\alpha = 0.6$, $m = 3$, $k = 4$, $\rho = 0.05$, $S_{\text{rel}} = 1.251877$ | B, C | CONVERGENT |
| C7: Cost convention for multi-drafter configurations (per-cycle vs. per-accepted-unit) | B vs. C | DIVERGENT (see Appendix A) |
| C8: Sensitivity recomputation at $\alpha = 0.4$ giving $S_{\text{rel}} = 1.330302$ | C | SINGLE |
| C9: Chaos in DNA inversions [1] invoked as qualitative failure mode of drafting | A | SINGLE |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1105.1512v1 | Chaos in DNA inversions (Draft paper)
arXiv:2606.05501v2 | Learning Contact Representation for Leg Odometry
arXiv:2603.00487v1 | DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments
arXiv:2601.20357v1 | TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs
arXiv:2108.08668v3 | Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes
arXiv:2009.02646v1 | Moment-Based Ensemble Control
arXiv:2610.10672v1 | Prescriptive Master Integrals of Maximal Weight at Two Loops
arXiv:2202.03383v1 | Asymptotic of Bergman Kernel (Master Thesis)

## QNFO corpus context (Vectorize)

QNFO: A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio | https://papers.qnfo.org/papers/consilient-gap-synthesis
QNFO: Kappa/SIIT Cross-Validation: Exact Reproduction of Standard Model 1-Loop β-Functions and Resolution of the Harmonic-Paradigm Tension | https://papers.qnfo.org/papers/harmonische-paradigma-kappa-siit-v4
QNFO: QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel | https://papers.qnfo.org/papers/consilient-synthesis-v2

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1105.1512v1 | Chaos in DNA inversions (Draft paper)
  This is a draft paper, proving that the inversion process that occurs in DNA mutations, is indeed chaotic as it is defined by the Devaney's theory.
  Full text (https://arxiv.org/html/1105.1512v1), excerpts of its own sections:
  § 1 Introduction: Codons are not uniformly distributed into the genome. Over time mutations have introduced some variations in their apparition frequency. It can be attractive to study the genetic patterns (blocs of more than one nucleotide: dinucleotides, trinucleotides…) that appear and disappear depending on mutation parameters. Mathematical models allow the prediction of such an evolution, in such a way that statistical values observed into current genomes can be recovered. A first model for genomes evolution has been proposed in 1969 by Thomas Jukes and Charles Cantor [ 16 ] . This first attempt has been followed up by Motoo Kimura [ 17 ] , Joseph Felsenstein [ 13 ] , Masami Hasegawa, Hirohisa Kishino, and Taka-Aki Yano [ 15 ] respectively. The differences between these models are in the number of parameters they use, but all of these models manipulate constant parameters. However, they are rudimentary as they only allow to study nucleotides evolution, not genetic patterns mutations. [...]
  § 2.1 Chaotic Iterations: Let us consider a system with a finite number $\mathsf{N}\in\mathds{N}^{*}$ of elements (or cells ), so that each cell has a Boolean state . A sequence of length $\mathsf{N}$ of Boolean states of the cells corresponds to a particular state of the system . A sequence which elements belong to $\llbracket 1;\mathsf{N}\rrbracket$ is called a strategy . The set of all strategies is denoted by $\mathbb{S}.$ Definition 1 . The set $\mathds{B}$ denoting $\{0,1\}$ , let $f:\mathds{B}^{\mathsf{N}}\longrightarrow\mathds{B}^{\mathsf{N}}$ be a function and $S\in\mathbb{S}$ be a strategy. The so-called chaotic iterations are defined by $x^{0}\in\mathds{B}^{\mathsf{N}}$ and $\forall n\in\mathds{N}^{\ast},\forall i\in\llbracket 1;\mathsf{N}\rrbracket,x_{i}^{n}=\left\{\begin{array}[]{ll}x_{i}^{n-1}&\text{ if }S^{n}\neq i\\ \left(f(x^{n-1})\right)_{S^{n}}&\text{ if }S^{n}=i.\end{array}\right.$ In other words, at the $n^{th}$ iteration, only the $S^{n}-$ th cell is “iterated”. [...]
  § 2.2 Genes mutations shown as chaotic iterations: When considering the model of 2007 with 9 constant parameters that generalize models of 1998 and 2006, all of the trinucleotides have to mutate at each time. These models do not take into account the low mutability of the stop codons. Additionally, they do not allow to apply mutation strategies on certain given codons, while the other codons do not mutate. This is why a new model with 3 constant parameters has been proposed in [ 8 , 10 ] . In this model, the set of trinucleotides is divided into two subsets at each time $t$ : the first one is constituted by trinucleotides that can possibly mutate at time $t$ , whereas in the second one trinucleotides cannot mutate at the considered time. The trinucleotides that mutate at time $t$ are randomly picked following a uniform distribution. Consequently, the size and the constitution of the subset of mutable trinucleotides change at each time $t$ . This subset is denoted by $J(t)$ , and this new model has been called “chaotic model” by the authors of [ 8 , 10 ] , as opposed to the former “standard model” of 1998. [...]
  § 2.3 Relevance of the CM model: A computation of the frequency of each trinucleotide in the 3 frames of genes, in a large gene population (protein coding region) of both eukariotes and prokaryotes, has established in 1996 that the distribution of trinucleotides in these frames is not uniform. Such a surprising result has led to the definition of 3 subsets of trinucleotides, denoted by $X_{0}$ , $X_{1}$ , and $X_{2}$ . [...]
[2] arXiv:2606.05501v2 | Learning Contact Representation for Leg Odometry
  Leg odometry relies on the assumption that the velocity of a foot in stance is zero with respect to the world, which makes accurate contact detection a critical subproblem. Many approaches classify contact using ground reaction force (GRF) sensors at the foot tip, yet these sensors are not available on all legged robots and remain unresponsive to disturbances such as slippage while the foot is sti
  Full text (https://arxiv.org/html/2606.05501v2), excerpts of its own sections:
  § 1 Introduction: Legged robots exhibit superior mobility in unstructured environments compared to wheeled platforms. However, their morphology complicates state estimation which is a prerequisite for downstream mapping, planning and navigation. Legged odometry relies fundamentally on the assumption that the velocity of the foot in contact with the ground is zero relative to the inertial frame [ 9 , 5 , 4 , 8 ] , during the stance phase, referred to as Zero-Velocity Update (ZUPT) [ 27 , 17 ] . This constraint allows kinematic chains to correct main-body velocity drift. [...]
  § 4 Experiments: All contact detection frameworks are evaluated across their classification performance and downstream impact on quadruped leg odometry. We further conduct ablation studies to reveal intrinsic properties of the contact kinematics. For the experiments, TartanGround [ 23 ] simulation dataset and our real-world dataset on diverse terrain such as concrete, grass and rock are utilized. The models are trained per dataset so a single model is shared across all terrains of a dataset. (See Appendix D for details on datasets, default hyperparameter set and additional experiments.) We benchmark the following contact estimation pipelines: i) GRF-Thresholding (Baseline): Hard thresholding on $F_{z}$ . ii) HMM-GMM (Offline and Online): Our unsupervised probabilistic detector, which models continuous probability on raw kinematic inputs. iii) Supervised NN (CNN [ 20 ] and GRU [ 35 ] ): Discriminative models trained on GRF pseudo-labels. iv) Self-supervised DAE-GMM (CNN and GRU): The proposed label-free representation learning pipelines. [...]
  § 4.1 Classification Accuracy and Domain Shift: Standard evaluation protocols for leg odometry contact detection rely on classification metrics against heuristic pseudo-labels [ 20 , 31 ] . We establish this comparison by evaluating isolated contact classification performance, detailed in Table 1 . Supervised CNN and GRU models achieve the highest scores on both datasets. However, all detectors exhibit performance degradation when evaluated on the physical robot due to sensor noise and unmodeled terrain compliance in the real world. Table 1: Contact Classification Metrics Across Domains $\uparrow$ ( Best , Second Best ) TartanGround (Sim) Real-World (Physical) Method Precision Recall F1 Precision Recall F1 Supervised CNN [ 20 ] 0.996 0.999 0.998 0.935 0.895 0.907 Supervised GRU [ 35 ] 0.997 0.999 0.998 0.924 0.929 0.921 HMM-GMM (Offline) 0.995 0.980 0.988 0.916 0.922 0.906 HMM-GMM (Online) 0.994 0.937 0.964 0.917 0.868 0.886 DAE-GMM (CNN) 0.983 0.994 0.988 0.809 0.967 0.868 DAE-GMM (GRU) 0.985 0.992 0.989 0.844 0.994 0.900 Crucially, ground truth pseudo-labels rely on heuristics. [...]
  § 6 Conclusion: This study proposes a self-supervised representation learning framework for contact modeling in legged odometry that requires neither force sensors nor contact labels. Evaluations against supervised and probabilistic unsupervised baselines in simulation and on hardware show that ZUPT reduces state estimation drift when its covariance is scaled by the posterior of a GMM fitted in the DAE latent space, where stance and swing appear as two dominant modes, rather than in the raw kinematic space. We further show that higher pseudo-label classification accuracy does not necessarily translate into better leg odometry. Finally, longer temporal context biases the latent representation toward periodic gait dynamics, which could serve as priors within Bayesian filtering architectures.
[3] arXiv:2603.00487v1 | DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments
  Gentzen's 1936 proof of the consistency of Peano Arithmetic was a significant result in the foundations of mathematics. We provide here a modified version of the proof, based on Gödel's reformulation, and including additional details and minor corrections which are necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment. All results have b
  Full text (https://arxiv.org/html/2603.00487v1), excerpts of its own sections:
  § 1.1 A Crisis of Foundations: During the 1930’s mathematics was progressing rapidly, however not all of these developments were positive. Hilbert’s Program, a series of results set forth at the turn of the 20th century that would have solidified mathematics down to an unshakeable logical foundation, suffered it first major defeat. Gödel proved his two famous incompleteness theorems, and Hilbert’s Program as it was originally envisioned was doomed Zach (2005) . Ideas of proving all of mathematics consistent seemed to be doomed if something as simple as the consistency of arithmetic was unable to be proven. Many took Gödel’s results as the end and moved on to other pursuits, however not all gave up hope choosing to reject the impossibility reading Hilbert and Bernays (1934) . Gerhard Gentzen continued to work on his proof, his previous work on sequent calculi Gentzen (1935) giving him unique insights which allowed him to work around the constraints placed by the incompleteness theorem. [...]
  § 1.2 Incompleteness and Consistency: For notational convenience the statement “arithmetic is consistent” is represented as $Cons_{PA}$ , where $PA$ is referring to the Peano Arithmetic, which is one of the most common axiomatisations of arithmetic Fritz (1952) . The main difficulty in proving this result is Gödel’s Second Incompleteness Theorem and its corollaries. Theorem 1 (Gödel’s Second Incompleteness Theorem) . For any Hilbert calculus $L$ , if $L$ contains Robinson Arithmetic and is consistent, then $L$ can not prove $Cons_{L}$ Gödel (1938) . Corollary 2 . Peano Arithmetic can not prove its own consistency. Furthermore, because Peano Arithmetic can prove the consistency of Primitive Recursive Arithmetic we have an additional corollary due to transitivity of consistency. Corollary 3 . Primitive Recursive Arithmetic can not prove the consistency of Peano Arithmetic. As such, it was necessary for Gentzen to find an alternative formulation $L$ , such that Peano Arithmetic could not prove the consistency of $L$ , but $L$ could prove the consistency of PA. [...]
  § 1.3 Finiteness and Formalisation: Gentzen’s method for proving consistency used the now familiar technique of Cut Elimination over a sequent calculus, a method which he had pioneered Gentzen (1969) . He constructed the logic PA ω , which used 7 consistency preserving deductive rules and the Cut rule, which does not preserve consistency. [...]
  § 4.2 Other Attempts at Formalising Gentzen’s Results: The initial inspiration for this work was a masters thesis by Morgan Sinclaire Sinclaire (2019) , which was an incomplete attempt at formalising Gentzen’s proof in Coq as outlined in the book “Introduction to Mathematical Logic” by Elliott Mendelson Mendelson (1964) . Sinclaire had seemingly abandoned the work and was not contactable, so we took the framework that he had provided and completed it, along with fixing some of the existing bugs. Work that had already been done by Sinclaire include: the definition of the language for PA ω and facts about substitution and free variables; a definition of finitely representable ordinals inspired by the work above, some of the machinery associated with the ordinals that would be needed for the later parts of the proof; a definition for theorems of PA ω without decorations; the proof that the Law of the Excluded Middle was on of those theorems; the definition of proof trees for PA ω with decorations; and inversion principles for the Negation and DeMorgan rules. [...]
[4] arXiv:2601.20357v1 | TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs
  Speculative decoding (SD) has proven effective for accelerating LLM inference by quickly generating draft tokens and verifying them in parallel. However, SD remains largely unexplored for Large Vision-Language Models (LVLMs), which extend LLMs to process both image and text prompts. To address this gap, we benchmark existing inference methods with small draft models on 11 datasets across diverse i
  Full text (https://arxiv.org/html/2601.20357v1), excerpts of its own sections:
  § 1 Introduction: Multimodal Large Language Models (MLLMs) Wu et al. (2023) ; Zhang et al. (2024a) ; Jin et al. (2024) ; Song et al. (2023) are an advanced class of LLMs  ( Brown et al., 2020 ; Ouyang et al., 2022 ; Touvron et al., 2023 ; Guo et al., 2025 ) designed to process multiple modalities, such as images, audio, and video, alongside text. In particular, Large Vision Language Models (LVLMs)  Chen et al. (2024c) , also known as Large Multimodal Models  Li et al. (2024b) ; Song et al. (2023) , specialize in handling prompts comprised of text and images. These models have attracted significant attention due to their unique applications, including multimodal chatbots, visual question answering (VQA), and augmented reality (AR)  ( OpenAI, 2023 ; Anthropic, 2024 ; Gemini Team Google: Anil et al., 2023 ) . [...]
  § 4.2 Experimental Results: Table   1 presents the block efficiency results for multimodal (M) and text-only (T) drafting methods. Across all scenarios, neither drafting method consistently outperformed the other. Notably, the multimodal drafting method demonstrated higher block efficiency than the text-only approach in single-turn scenarios across most benchmark datasets. However, the text-only drafting performed comparably or slightly sub-optimally overall in single-turn situations, often surpassing the multimodal drafting in subsequent turns–particularly in tasks dependent on prior responses and independent reasoning tasks, and significantly in OOD cases. This trend continued regardless of the model size or multi-image awareness capabilities. Existing drafting methods, both multimodal and text-only, show scenario-specific performance fluctuations with draft models small enough for SD, with neither method consistently outperforming the other across various input scenarios for LVLM inference. [...]
  § 5.2 Experimental Results: Table   1 presents the block efficiency results for TABED, which is denoted by TABED MT . TABED MT consistently achieved either the best or second-best performance across all input scenarios. These scenarios include turn-taking, image inclusion, prior context relevance, and both benchmark and OOD datasets. Even when TABED MT ranked second, its performance remained close to the best, unlike the larger performance gaps observed for other methods. Without incurring additional costs during training or inference, this resulted in and a 5% improvement compared to existing single drafting methods M and T, when averaged across all benchmark datasets and turns. This leads to an average robust walltime speedup of 1.74×, computed using  Eq.   1 , compared to standard decoding. These consistent gains highlight TABED’s ability to effectively prioritize stronger drafting methods by dynamically assigning optimal weights, even when individual methods exhibit scenario-specific performance fluctuations. [...]
  § 7 Conclusion: We benchmark existing inference methods for LVLM drafting and observe scenario-specific performance fluctuations. To address this, we propose TABED, that dynamically ensembles multiple drafts obtained via batch inference by leveraging deviations of the drafts from past ground truths. TABED consistently achieves the best or second-best performance across all scenarios, with an average robust expected walltime speedup of 1.74× and over 5% improvement over single drafting methods, all without additional tuning. TABED can be further enhanced through advanced verification or alternative drafting methods via its plug-and-play compatibility and remains fully training-free with negligible ensembling costs.
[5] arXiv:2108.08668v3 | Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes
  Perturbation theory of vacuum spherically-symmetric spacetimes is a crucial tool to understand the dynamics of black hole perturbations. Spherical symmetry allows for an expansion of the perturbations in scalar, vector, and tensor harmonics. The resulting perturbative equations are decoupled for modes with different parity and different harmonic numbers. Moreover, for each harmonic and parity, the
  Full text (https://arxiv.org/html/2108.08668v3), excerpts of its own sections:
  § I Introduction: Spacetime perturbation theory is one of the main tools in General Relativity to describe physical systems and make reliable predictions about their characteristics and dynamical behavior. It has been applied essentially to all the main problems in the area of relativistic astrophysics and cosmology: From the origin and growth of cosmological structures and the cosmic microwave background  [ 1 , 2 , 3 , 4 ] to phenomena involving relativistic stars and black holes  [ 5 , 6 , 7 , 8 ] ; including gravitational wave generation and propagation  [ 9 , 10 , 11 , 12 ] (see  [ 13 , 14 , 15 , 16 , 17 , 12 , 18 ] for applications of black hole perturbation theory to gravitational wave astronomy). There are also many applications of black hole perturbation theory that have implications for fundamental physics (see  [ 19 , 20 , 21 ] for reviews). [...]
  § II Relativistic Perturbation Theory of Spherically-Symmetric Spacetimes: In this section we introduce all the ingredients and machinery needed to derive the main results of this work.
  § II.1 Basics of Relativistic Perturbation Theory: Relativistic Perturbation Theory is usually formulated by assuming the existence of a one-parameter family of spacetimes, $(\mathcal{M}_{\lambda},g_{\lambda})$ , in such a way that the perturbations are constructed as a Taylor expansion of this family around the $\lambda=0$ spacetime (see, e.g.  [ 59 , 60 ] ), the background spacetime, which usually represents an idealized gravitational system, typically with a high degree of symmetry as in our case. Here, we assume the background 1 1 1 We use a hat to denote quantities associated with the background spacetime, like $\widehat{Q}$ . to be a vacuum (including the cosmological constant) spherically-symmetric spacetime. [...]
  § II.2 Background Solution: Vacuum spherically symmetric spacetimes: We consider background spacetimes, or regions of spacetimes, that are solutions of the Einstein vacuum equations including a cosmological constant [see Eq. ( 1 )]. These solutions come from a generalization of Birkhoff’s local uniqueness theorem  [ 63 ] (published before by Jebsen  [ 64 , 65 ] ; see also  [ 66 , 67 ] ) to the case of a non-vanishing cosmological constant  [ 68 ] (see  [ 69 ] for details). [...]
  § II.3 Multipolar expansion of the perturbations of vacuum spherically-symmetric spacetimes: The background metric can be written as the warped product of two manifolds: $M^{2}\times_{r}S^{2}$ , where $M^{2}$ is a two-dimensional Lorentzian manifold, $r$ is the radial area coordinate, and $S^{2}$ denotes the [...]
  § IV Conclusions and Future Prospects: In this paper, we have carried out a study of all the possible master functions and equations for the perturbations of vacuum spherically-symmetric spacetimes. The only assumptions made in this study are: (i) The master functions are linear combinations of the metric perturbations and their first-order derivatives. (ii) The coefficients of those linear combinations only depend on the radial areal coordinate. (iii) The master functions satisfy a wave-type equation associated with the two-dimensional metric of the Lorentzian manifold tangent to the spheres of symmetry, and with a potential that is determined by the perturbative Einstein equations. The outcome of this study produces two branches of solutions: (a) The first branch corresponds to the already known results, with the exception of the even-parity case, for which we have found a new master function independent of the Zerilli-Moncrief one, $\Psi_{\rm ZM}$ , and which we have denoted by $\Psi_{\rm EN}$ . [...]
[6] arXiv:2009.02646v1 | Moment-Based Ensemble Control
  Controlling a large population, in the limit, a continuum, of structurally identical dynamical systems with parametric variations is a pervasive task in diverse applications in science and engineering. However, the severely underactuated nature and the inability to avail comprehensive state feedback information of such ensemble systems raise significant challenges in analysis and design of ensembl
  Full text (https://arxiv.org/html/2009.02646v1), excerpts of its own sections:
  § I Introduction: Large populations of uncoupled or interconnected dynamical systems are pervasive in diverse scientific domains, such as quantum science and technology [ 1 , 2 ] , power systems [ 3 ] , neuroscience [ 4 , 5 ] , emergent behaviors [ 6 ] , and robotics [ 7 ] . These population systems, formally referred to as ensemble systems , generally exhibit variations in the parameters characterizing the dynamics of individual dynamic units in the ensemble. Such variations arise either by nature (e.g., different weight and size of birds in a flock), manufacturing (e.g., the variability in the fabrication resulting in different mass, friction coefficients, etc., of robots in a swarm), or design (e.g., the application of gradient fields resulting in Larmor frequency dispersion in magnetic resonance imaging). Owing to their prevalence in diverse emerging applications and rich mathematical structures, ensemble control problems have attracted significant attention and formed a new paradigm in systems and control over past years. [...]
  § II-A Ensemble systems: An ensemble system is a parameterized population of dynamical systems defined on a common manifold $M\subseteq\mathbb{R}^{n}$ of the form $\frac{d}{dt}x(t,\beta)=F(x(t,\beta),\beta,u(t)),$ (1) where $\beta$ is the parameter varying on $\Omega\subset\mathbb{R}^{d}$ . The parameter space $\Omega$ is generally assumed to be compact and it can be finite, countable or uncountable [ 8 , 18 ] . Thus, the state-space of the ensemble system in ( 1 ) is a space of $M$ -valued functions defined on $\Omega$ , denoted by $\mathcal{F}(\Omega,M)$ . The ensemble control problem deals with the design of a parameter-independent control input $u(t)\in\mathbb{R}^{l}$ which steers the ensemble system from an initial profile $x_{0}\in\mathcal{F}(\Omega,M)$ to a desired final profile $x_{F}\in\mathcal{F}(\Omega,M)$ in a finite time $T$ . To understand ensemble control systems, we first introduce the notion of ensemble controllability, which describes the ability of an ensemble control law to manipulate the entire ensemble on its state-space in an approximating sense. [...]
  § II-B Aggregated measurements and labels of ensemble systems: In many emerging applications, though placing dedicated sensors to monitor the evolution of the states of individual systems in a population is not feasible, an aggregated, population-level measurement can be obtained (see Fig. 1 ). [...]
  § VII Conclusions: In this paper, we develop a moment-based ensemble control framework to close the feedback loop in ensemble control systems using population level, aggregated measurements, which are available in many emerging applications. In particular, we integrate the method of moments in probability and statistics into control theory by interpreting deterministic ensemble systems from the probabilistic viewpoint. The major tool developed in this work is the dynamic Hausdorff moment problem, that is, an extension of the classical Hausdorff moment problem from the aspects of differential geometry and dynamical systems theory, through which we show that ensemble systems and their moment systems share the same control and controllability property. These theoretical investigations lay the foundation for the design of moment-feedback control laws for ensemble systems. Furthermore, this controllability-preserving moment transformation simultaneously accomplishes the task of model reduction of ensemble systems containing uncountable many individual systems to networks containing countably many agents. [...]
[7] arXiv:2610.10672v1 | Prescriptive Master Integrals of Maximal Weight at Two Loops
  We describe the construction of a spanning set of individually pure, planar master integrals involving massless particles in four dimensions which include all maximal-weight contributions at two loops. In this basis, every independent region associated with infrared divergence is individually matched by specific masters, with all other masters being manifestly finite in four dimensions.
  Full text (https://arxiv.org/html/2610.10672v1), excerpts of its own sections:
  § 1 Introduction and Overview: We construct a set of individually-pure master Feynman integrals for involving massless propagators at two loops which span all maximal-weight contributions to four-dimensional planar theories. These integrals are defined and constructed prescriptively , as the cohomological duals [ Mastrolia:2018uzb , Frellesvig:2019kgj , Frellesvig:2019uqt , Frellesvig:2020qot , Weinzierl:2020gda , Caron-Huot:2021iev , Caron-Huot:2021xqj , lu2025intersection ] of a spanning set of compact contour integrals [ Gluza:2010ws , Caron-Huot:2012awx ] $\{\Omega^{{\color[rgb]{0.575,0,0.225}j}}\}$ , $\oint\limits_{\Omega^{\color[rgb]{0.575,0,0.225}j}}\hskip-2.0pt\text{\makebox[7.2pt][l]{$\raisebox{4.5pt}{\text{\makebox[0.0pt][l]{$\scalebox{1.5}[0.75]{\hskip 1.25pt\text{-}}$}}}d$}}^{4}\hskip-1.0pt\ell_{1}\text{\makebox[7.2pt][l]{$\raisebox{4.5pt}{\text{\makebox[0.0pt][l]{$\scalebox{1.5}[0.75]{\hskip 1.25pt\text{-}}$}}}d$}}^{4}\hskip-1.0pt\ell_{2}\;\mathcal{I}_{{\color[rgb]{0,0,0.575}i}}=\delta{\hskip [...]
  § 1.1 Organization and Outline: This work is organized as follows. In section 2 we review the construction, structure, and use of master integrals for the representation of perturbative quantities in quantum field theory. In particular, we review the familiar choices of masters in section  2.1 and describe how coefficients may be determined using integration-by-parts ‘projections’ or generalized unitarity in section  2.1 . We define the notion of purity of transcendental functions in section  2.4 and discuss degrees of impurity in section  2.4.1 , and the impurities of scalar Feynman integrals in section  2.4.2 . In section  3 we define masters constructed by power-counting and define the space of masters constructed here in section  3.3 . These masters are chosen prescriptively as the duals of particular choices of (linear combinations of) compact cycles of integration; these choices are elucidated in section  3.4 and section  3.4.1 . In section  4 we conclude with a discussion of future work and applications. [...]
  § 2 Masters Integrals, Integral Reduction, Purity and Rigidity: The Feynman rules for perturbative quantum field theory encode scattering amplitudes as sums over differential forms on a space of internal ‘loop’ momenta, which must be integrated. [...]
  § 4 Conclusions and Future Directions: A key advantage of a prescriptive basis of master integrands is that the coefficients of any amplitude can be directly calculated in terms of on-shell functions. In the case of maximally supersymmetric Yang-Mills theory in the planar limit, the basis we have described here necessarily includes all contributions to all scattering amplitudes at two loops; it would be interesting to compare how amplitudes would be represented in this basis relative to those used in [ Bourjaily:2015jna ] , or to what results from on-shell recursion [ BCF , BCFW ] extended to loop-level [ CaronHuot:2010zt , ArkaniHamed:2010kv , Bourjaily:2023apy ] . This has in fact already been implemented, the details of which will be described in the forthcoming [ bourjaily:amplitudesInNewBasis ] . Besides the fact that leading singularities are individually matched in this basis, the fact that the infrared structure is so carefully refined provides a source of optimism that observables such as the ratio function may be rendered manifestly locally finite in terms of these masters [ Bourjaily:2021ewt ] . [...]
[8] arXiv:2202.03383v1 | Asymptotic of Bergman Kernel (Master Thesis)
  In this master thesis, we give a new proof on the pointwise asymptotic expansion for Bergman kernel of a hermitian holomorphic line bundle on the points where the curvature of the line bundle is positive and satisfy local spectral gap condition. The main point is to introduce a suitable semi-classical symbol space and related symbolic calculus inspired from recent work of Hsiao and Savale. Particu
  Full text (https://arxiv.org/html/2202.03383v1), excerpts of its own sections:
  § Chapter I Introduction: Bergman kernel, first introduced by Stefan Bergman [ Ber22 ] in 1922 for domains in $\mathbb{C}^{n}$ , is a fundamental object in several complex variables and complex geometry, and has been the impetus of many researches in various fields. The main goal of this thesis is to study the asymptotic of Bergman kernel of holomorphic sections for high tensor powers of a holomorphic line bundle over a complex manifold. Let us first define Bergman kernel for a hermitian holomorphic line bundle over a complex manifold. Let $L$ be a holomorphic line bundle over a complex manifold $X$ with $\dim_{\mathbb{C}}X=n$ . If we endow a positive, smooth $(1,1)$ -form $\omega$ on $X$ , which induces a Riemannian volume form $d\nu_{X}=\omega_{n}:=\frac{\omega^{n}}{n!}$ , and a hermitian metric $h^{L}$ on $L$ given by local weight $\phi$ , then they give rise to a scalar product on $C^{\infty}_{c}(X,L)$ , the space of smooth global sections for $L$ with compact supports. We then complete $C^{\infty}_{c}(X,L)$ with respect to the scalar product to get a Hilbert space $L^{2}_{\omega,\phi}(X,L)$ . [...]
  § I.1. Statement of Main Results and Applications: We now formulate the main result presented in the thesis. We refer to chapter II for relevant notations and terminology used here. Let $(X,\omega)$ be a hermitian manifold of complex dimension $n$ , where $\omega$ is a smooth, positive $(1,1)$ -form on $X$ , inducing the hermitian structure on $X$ . We denote $\langle\cdot|\cdot\rangle_{\omega}$ by the hermitian metric on $T^{1,0}X$ induced by $\omega$ . A canonical Riemannian volume form $d\nu_{X}$ for $(X,\omega)$ is given by $d\nu_{X}=\omega_{n}:=\frac{\omega^{n}}{n!}$ . Let $L$ be a holomorphic line bundle on $X$ and set $L^{k}:=L^{\otimes k}$ , for $k\in\mathbb{N}$ . For any hermitian metric $h$ on $L$ , we can define the Chern connection $\nabla$ on $L$ with respect to $h$ with curvature $R^{L}(h)=(\nabla^{L})^{2}\in A^{1,1}(X)$ . We identify $R^{L}(h)$ with the curvature operator $\dot{R}^{L}(h)\in C^{\infty}(X,\operatorname{End}(T^{1,0}X))$ by (I.4) $\sqrt{-1}R^{L}(h)(x)(v\wedge\overline{w})=\langle\dot{R}^{L}(h)(x)v|w\rangle_{\omega},$ for any $x\in X$ , $v,w\in T^{1,0}_{x}X$ . [...]
  § Chapter II Preliminaries on $\bar{\partial}$ -Harmonic Forms and Bergman Kernel: In this chapter, we introduce Bergman kernel. The first three sections introduce some relevant notations and terminology. In section II.4 , we define a suitable extension of Kodaira Laplacians $\square^{(q)}_{\omega,k\phi}$ due to Gaffney for the study of $\bar{\partial}$ -harmonic forms on non-compact case. Finallly, in section II.5 , we introduce Bergman kernel and discuss some fundamental properties of them.
  § II.1. Some Standard Notations: We denote $\mathbb{N}:=\{1,2,\dots\}$ by the set of natural numbers and $\mathbb{N}_{0}:=\mathbb{N}\cup\{0\}$ . We adopt the following two multi-indices notations. For a multi-index $\alpha=(\alpha_{1},\dots,\alpha_{n})\in\mathbb{N}_{0}^{n}$ , we denote $|\alpha|:=\sum_{i=1}^{n}\alpha_{i}$ . We adopt standard notations such as $\alpha!=\alpha_{1}!\cdots\alpha_{n}!$ , $x^{\alpha}$ , and $\partial_{x}^{\alpha}$ . On the other hand, a $n$ -tuple $J=(j_{1},\dots,j_{q})\in\{1,\dots,n\}^{q}$ is called a strictly increasing multi-index if $1\leq j_{1} $\alpha=\sum_{|I|=q}\nolimits^{\prime}\alpha_{I}dx^{I},$ where $\sum^{\prime}_{|I|=q}$ means that summation is over strictly increasing multi-indices $I$ of length $q$ . [...]
[9] QNFO: A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio | https://papers.qnfo.org/papers/consilient-gap-synthesis
  A consilient gap synthesis of the QNFO/QWAV research portfolio cataloging 42 gaps across 5 structural categories (Infrastructure, Content, Physics Validation, Governance, Dissemination) with a phased version roadmap v2.0-v2.4 spanning 8 calendar weeks.
  Full text (https://papers.qnfo.org/papers/consilient-gap-synthesis), excerpts of its own sections:
  § 1.1 The Portfolio at Scale: The QNFO/QWAV research ecosystem operates at a scale where cross-project consistency becomes a first-class maintenance concern. As of 2026-07-29, the ecosystem comprises: - **95** projects tracked in the Knowledge Graph - **3,109** KG nodes with **1,502** edges across **39** node labels - **917** papers in the D1 `living-paper` database (662 published, 254 backfilled from KG) - **25** OpenItems actively tracked - **13** R2 buckets serving as durable storage - **12** active projects with ongoing development Prior portfolio-level audits (KIF-22, KIF-23 in systemwide audit 2026-07-25) identified specific classes of drift: registry-extension mandates that fail silently, KG–D1 dual-write desynchronization (257 of 887 papers missing from KG), and backup schedules that lapse without detection. The DEC-020 initiative reduced the active project count from ~50 to 12, but did not systematically catalog the gaps that remained.
  § 1.2 The Core Claim: > **[C1]:** The QNFO/QWAV research portfolio contains a finite, enumerable set > of gaps that can be classified into exactly five cross-domain structural > categories (Infrastructure, Content/Publication, Physics Validation, > Governance, Dissemination). Sequencing these gaps by blocker-dependency and > expected value produces a Pareto-optimal roadmap where the first two phases > (Infrastructure + Content Remediation) resolve over 60% of known blockers > with less than 25% of total estimated effort, because the dependency graph > is predominantly a directed acyclic graph with depth ≤3. [...]
  § 2.4 Cross-Domain Consilience Gate (KIF-29): A six-domain structural translation was performed (Physics, CS, Cognitive Science, Information Theory, Biology, Sociology) to verify that the five gap categories are not artifacts of a single domain's lexicon but represent invariant structural patterns — see §5 and `artifacts/consilience-gate.md`.
  § 3.1 Summary Statistics: | Category | Count | HIGH | MEDIUM | LOW | |:---------|:------|:-----|:-------|:-----| | Infrastructure (I) | 16 | 2 | 4 | 10 | | Content/Publication (C) | 14 | 2 | 5 | 7 | | Physics Validation (P) | 5 | 0 | 1 | 4 | | Governance (G) | 4 | 1 | 1 | 2 | | Dissemination (D) | 3 | 0 | 2 | 1 | | **TOTAL** | **42** | **5** | **13** | **24** |
  § §5. Cross-Domain Consilience: The structural patterns identified in this gap synthesis — classification into a small set of invariant failure modes, dependency graph as a DAG, topological sort producing Pareto-optimal phases, keystone identification — recur across disciplines. A full cross-domain translation is provided in `artifacts/consilience-gate.md`. We summarize the key isomorphisms:
  § 6.1 Findings: 1. **The portfolio is not in crisis.** Zero gaps are currently BLOCKING any active project. All 12 active projects can proceed independently while the cross-project consistency layer is hardened. 2. **The portfolio has drifted into maintenance debt.** 42 gaps exist, of which 5 are HIGH severity, 13 MEDIUM, and 24 LOW. The root cause is the absence of a systematic consistency verification layer (OI-003, Consistency Engine). 3. **The dependency structure is favorable.** The gap dependency graph is a DAG with depth ≤3, meaning a bounded number of phases can resolve all gaps. 4. **The Pareto distribution is extreme.** The top 5 HIGH-severity gaps (12% of total) transitively block approximately 40% of all gaps.
[10] QNFO: Kappa/SIIT Cross-Validation: Exact Reproduction of Standard Model 1-Loop β-Functions and Resolution of the Harmonic-Paradigm Tension | https://papers.qnfo.org/papers/harmonische-paradigma-kappa-siit-v4
  We report a direct mathematical cross-validation of the Kappa / Scale-Invariant Information Thermodynamics framework (Quni-Gudzinas, 2025, the QNFO archive 17218944/17230397) against the Standard Model's known 1-loop renormalization-group β-functions. Through the single definition $g_{\text{eff}} = g_0 \kappa(x)$ — the Kappa framework's postulate that effective gauge couplings are the bare couplin
  Full text (https://papers.qnfo.org/papers/harmonische-paradigma-kappa-siit-v4), excerpts of its own sections:
  § 1. Introduction: The Harmonic Paradigm (V1.0–V3.0, DOIs https://papers.qnfo.org/papers, https://papers.qnfo.org/papers, https://papers.qnfo.org/papers, https://papers.qnfo.org/papers) proposed that eight physically unrelated bosonic systems — from superconducting transmon qubits to quantum gravity — share a universal renormalization-group β-function governing deviations from exact harmonic-oscillator behavior. Version 3.0 [@qnfo-harmonic-v3] retracted the central logistic β-function ansatz $\beta(\alpha) = B\cdot\alpha(1-\alpha)$ after direct calculation showed it incompatible with the known, textbook 1-loop QED β-function $\beta_{\text{QED}}(\alpha) = \frac{2}{3\pi}\alpha^2 + O(\alpha^3)$: the logistic ansatz is linear at leading order near the infrared fixed point, while real QED is quadratic — a difference in universality class, not just a numerical mismatch. [...]
  § 2. The Kappa/SIIT Framework — Key Equation: The Kappa/SIIT framework [@qnfo-kappa-derivation] postulates a scale-invariant information field $\kappa(x)$ as the fundamental substrate. [...]
  § 3.4 Result: The Kappa framework, through nothing more than $g_{\text{eff}} = g_0\kappa$ and the standard 1-loop QED β-function, produces $\beta(\alpha) = (2/3\pi)\alpha^2$ — **identical to the real, measured, textbook 1-loop QED β-function.** The unknown bare coupling $g_0$ cancels exactly; the result is independent of any free parameters. ---
  § 4.4 Result: **Exact match** to the standard 1-loop QCD β-function. For $n_f = 6$ (Standard Model): $b_0 = 11 - 4 = 7$, and $\beta(\alpha_s) = -7/(2\pi)\alpha_s^2 \approx -1.114\,\alpha_s^2$. Again, $g_0$ cancels identically. ---
  § 7.2 Results: | Quantity | Value | |:---|:---| | $T_{\text{obs}}$ (rungs) | 0.773 | | Null mean $T$ | 0.995 | | Null median $T$ | 0.986 | | Null 5th percentile $T$ | 0.484 | | Null 95th percentile $T$ | 1.577 | | **p-value** (fraction of null draws with $T \leq T_{\text{obs}}$) | **0.297** | Additionally: 32% of random 8-draws span an equal or wider energy range than the rungs' 33 ln-units, confirming that the ladder's coverage of 28 orders of magnitude is not itself unusual for a set of 8 distinct physics scales.
  § 8.1 Summary of Findings (V1.0 → V4.0): | Version | Year | DOI | Contribution | |:---|:---|:---|:---| | V1.0 | 2026-07 | https://papers.qnfo.org/papers | Unstructured research synthesis; 8-rung ladder proposed; 4 theses | | V2.0 | 2026-07 | https://papers.qnfo.org/papers | Formal paper; tautological criterion; BF cited without documentation | | V2.1 | 2026-07 | https://papers.qnfo.org/papers | Tautology replaced with logistic β-function ansatz; CAL-05 fabricated | | V3.0 | 2026-07 | https://papers.qnfo.org/papers | Structural retraction of logistic ansatz; transmon category error; CAL-05 retracted | | **V4.0** | **2026-07** | **https://papers.qnfo.org/papers** (this paper) | **Kappa cross-validation; order-statistics test; formal closeout** |
  § 9. Conclusion: The Harmonic Paradigm research program proposed a bold, falsifiable unifying mechanism, tested it against known physics, found it wanting, retracted it, and — in the process — cross-validated a previously uncited QNFO framework (Kappa/SIIT) that correctly reproduces the gauge-coupling β-functions the Harmonic Paradigm's mechanism could not. This is a successful outcome of a falsification-oriented methodology: a wrong mechanism was identified as wrong, documented as wrong, and replaced with a better answer for the domain where the better answer applies. [...]
[11] QNFO: QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel | https://papers.qnfo.org/papers/consilient-synthesis-v2
  QNFO Consilient Synthesis v2.0: the shared adelic kernel (valuation → tree boundary → Ostrowski → adeles). Applies all 7 corrections (C1–C7) from the 2026-07-25 red-team audit, restructured kernel-first with honest kernel-membership table and mandatory symmetry sections.
  Full text (https://papers.qnfo.org/papers/consilient-synthesis-v2), excerpts of its own sections:
  § QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel: **Author:** Rowan Brad Quni-Gudzinas (QNFO Research) | **Date:** 2026-07-31 **Version:** 2.0 | **Supersedes:** 2026-07-24 synthesis (v1.0) **License:** QNFO-ULA **Correction provenance:** This v2.0 synthesis incorporates all 7 corrections (C1–C7) mandated by the 2026-07-25 red-team audit of the "Shared Mathematical Kernel: The Adelic Core" note (R2: `qnfo-releases/audits/2026/07/adelic-core-note-redteam-2026-07-25.md`), and is restructured around the kernel-first spine the audit judged superior: **valuation → tree boundary → Ostrowski → adeles**. ---
  § Executive Summary: QNFO research in 2025–2026 converges on a single structural insight: **non-Archimedean (ultrametric) mathematics — p-adic valuations, Bruhat–Tits trees, Ostrowski's theorem — provides the correct state-space geometry for fundamental physics, quantum computation, and optimization.** The Archimedean (real-number, continuous) description is the ∞-place readout of a richer ultrametric structure. Four research programs engage the shared kernel directly; one (Qubit Delusion) connects by consilient interpretation. This synthesis presents the kernel as the organizing spine — each of its four elements (valuation, tree boundary, Ostrowski, adeles) examined once, with per-pillar evidence beneath it — rather than the v1.0 program-by-program layout. [...]
  § Element 3 — Ostrowski's Theorem: **Theorem (Ostrowski, with the C2 qualifier).** Every **non-trivial** absolute value on $\mathbb{Q}$ is equivalent either to the Archimedean absolute value |·|_∞ or to a p-adic absolute value |·|_p for a unique prime p. **Where the pillars use it:** - **Adelic QEC (P5):** no Archimedean perturbation can move a p-adic fixed point → intrinsic qubit protection with O(1) overhead. `[my conjecture — formal proof sketch provided]` The Adelic QEC paper states Ostrowski correctly with the "non-trivial" qualifier and builds the mutual-singularity argument on it. `[verified]` - **Ultrametric Foundations:** the completeness of each |·|_p determines the code-classification spectrum. - **Silent Radix — WEAKER KERNEL (correction C2):** for **composite base b**, $\mathbb{Q}$ with the b-adic metric completes to $\mathbb{Z}_b$ ≅ $\prod_{p|b}$ $\mathbb{Z}_p$ — a ring with zero divisors, **not a field, and not one of Ostrowski's completions.** v_b for composite b is not even a valuation (it fails multiplicativity). [...]
  § Part VI. Summary: Kernel → Pillars → Deliverables: | Kernel element | Fully engages | Weakly engages | Interpretive | |:---------------|:--------------|:---------------|:-------------| | Valuation v_p / v_b | Adelic Physics, Ultrametric Found. | Silent Radix (v_b) | — | | Tree boundary $\partial\infty\mathcal{T}$ | Adelic Physics, Ultrametric Found. | — | QLoF (Ch. 17 argument) | | Ostrowski | Adelic QEC (P5) | — | — | | Adeles $\mathbb{A}_{\mathbb{Q}}$ | Adelic Anyons, ATQC | — | — | **Program-level next actions (ACRP):** 1. **ACRP-01** (this document) → corrections applied, kernel-first restructure, publication pipeline. 2. **ACRP-04** (parallel-eligible, P0): Pythagorean semigroup mass-ratio statistical audit — outcome-neutral; may strengthen or bound the v3.2 claim. 3. **ACRP-02/03** (P1, after ACRP-01): boundary ultrametricity formalization; composite-radix theory repair. 4. **ACRP-08** (P2): paradigm forecast superseding the provisional priority table. ---