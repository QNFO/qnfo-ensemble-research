# Ensemble Drafting as Ensemble Control: A Moment-Based Framework for Multi-Draft Speculative Decoding

## Abstract

Speculative decoding accelerates autoregressive language-model inference by generating draft tokens with a small model and verifying them in parallel with a large target model. Recent work has begun to extend this paradigm to multiple simultaneous draft models, but the design of such multi-draft systems lacks a unifying analytical frame. We propose one: we recast ensemble drafting — the aggregation of several independent draft models into a single proposal stream — as an instance of ensemble control, the problem of steering a large population of structurally identical dynamical systems through a broadcast signal. Under an explicit independence assumption on draft errors, we derive closed-form expressions for the ensemble acceptance probability, the expected number of accepted tokens per verification cycle, and the resulting wall-clock speedup as a function of the number of drafts $k$, the single-draft acceptance rate $\alpha$, and the draft length $\gamma$. For representative parameters ($\alpha = 0.6$, $\gamma = 4$, $k = 3$), the framework predicts an ensemble acceptance rate of $0.936$ and a $1.67\times$ gain in expected accepted tokens over a single draft, before verification-overhead corrections. We state the assumptions under which these projections hold, identify the failure modes that violate them (correlated draft errors, verification-cost scaling), and connect the framework to the broader literature on ensemble systems, formal verification of proof drafts, and robustness benchmarking.

## 1. Introduction

Large autoregressive language models are expensive to run at inference time because token generation is inherently sequential: each token requires a full forward pass through the model. Speculative decoding addresses this by letting a cheaper draft model propose a short block of tokens that the large target model then verifies in a single parallel pass, accepting the longest correct prefix [3]. The technique is well established for single-draft text-only systems, but its extension to Large Vision-Language Models (LVLMs) — models that process both image and text prompts — has been far less explored, and the work that does exist reports that naive transfer of text-only methods to the multimodal setting is not straightforward [3].

A natural next step, suggested by the multimodal benchmarking literature, is to use *several* draft models simultaneously and to aggregate their proposals into one stream, so that a token is accepted if any draft's proposal survives verification. We call this configuration **ensemble drafting**. The central difficulty is that ensemble drafting is a control problem in disguise: the aggregator must steer a population of structurally identical stochastic generators (the drafts) using only a broadcast decision signal (accept/reject), without individual state feedback from each draft beyond its proposed tokens. This is precisely the structural situation studied in **ensemble control**, where one controls a large population, in the limit a continuum, of structurally identical dynamical systems with parametric variations, under severe underactuation and without comprehensive state feedback [5], and where in many applications control can only be implemented at the population level by broadcasting an input signal to all systems [8].

The contribution of this paper is a framework, not a system. We:

1. Formalize ensemble drafting as a population-control problem, defining the draft population, the broadcast verification signal, and the aggregation map (Section 3).
2. Derive, under explicitly stated independence assumptions, closed-form projections for the ensemble acceptance rate $\alpha_e(k)$, the expected accepted tokens per cycle $E(k, \alpha, \gamma)$, and the speedup ratio $S(k)$ (Section 4), with every arithmetic step shown.
3. Analyze the sensitivity of these projections to their assumptions and identify the conditions under which the framework fails (Sections 4 and 6).

We emphasize scope honestly: all quantitative results in this paper are *analytical projections* from stated assumptions, not empirical measurements. No experiments were run. The value of the framework is that it makes the assumptions falsifiable and gives system builders closed-form targets against which measured performance can be compared.

## 2. Background and Related Work

We organize the related work into four threads: speculative decoding and ensemble drafting; ensemble control of dynamical-system populations; verification and formalization of "draft" artifacts in other domains; and the methodological question of how multi-component frameworks are validated.

**Speculative decoding and multimodal drafting.** The foundational observation of the speculative-decoding line is that inference can be accelerated by quickly generating draft tokens and verifying them in parallel [3]. The entry supplying [3] states that speculative decoding "has proven effective for accelerating LLM inference by quickly generating draft tokens and verifying them in parallel," and that the technique "remains largely unexplored for Large Vision-Language Models (LVLMs), which extend LLMs to process both image and text prompts." The same work benchmarks existing inference methods with small draft models on 11 datasets across diverse input settings, establishing the empirical baseline against which any multi-draft extension must be judged. The supplied summary is truncated mid-sentence, so we cannot report its headline numbers from the entry alone; what the entry supports is the gap it identifies (multimodal drafting is underexplored) and the benchmark scope (11 datasets). Our framework is complementary: it supplies the analytical layer that the benchmarking in [3] lacks, and it inherits the gap that [3] documents.

**Ensemble control.** The control-theoretic thread begins with the observation that controlling a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations is pervasive in science and engineering, but that the severely underactuated nature of such ensemble systems and the inability to avail comprehensive state feedback raise significant challenges in analysis and design [5]. That work develops a moment-based approach, in which the population is tracked through its moments rather than through individual states. This is the direct methodological inspiration for Section 3: in ensemble drafting, the aggregator likewise cannot see the internal state of each draft model and must act on population-level statistics (per-token proposal distributions aggregated across drafts). A companion line extends ensemble control to systems whose state spaces are Lie groups, noting that such problems "arise in numerous scientific areas from quantum control and robotics to brain medicine" and that "in many of such applications, control can only be implemented at the population level, i.e., through broadcasting an input signal to all the systems in the population" [8]. The broadcast-only constraint of [8] maps exactly onto the accept/reject broadcast of the verifier in ensemble drafting: the verifier's decision is a single signal sent to the entire draft population, and no draft receives an individualized control input. The entry for [8] is truncated, so we use it only for the problem statement it supplies, not for any solution technique.

**Drafts, verification, and chaos in other domains.** The word "draft" carries productive analogies beyond inference. A draft paper in the DNA-mutation literature proves that the inversion process occurring in DNA mutations is chaotic in the sense of Devaney's theory [1]. The relevance to our framework is methodological: [1] demonstrates that a process long treated informally can be given a precise dynamical-systems characterization, and our Section 3 performs the analogous move for multi-draft inference — showing that the draft population is a controlled dynamical system with a well-defined state space and update rule. Separately, a formally verified constructive proof of the consistency of Peano Arithmetic using ordinal assignments revisits Gentzen's 1936 consistency proof, providing a modified version based on Gödel's reformulation with additional details and minor corrections necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment [2]. The connection to our work is the discipline of *verification*: in [2] the draft (the proof) is only as good as the verification machinery (well-foundedness of cut elimination), exactly as in speculative decoding the draft tokens are only as good as the verifier's acceptance test. The entry for [2] is truncated ("All results have b"), so we cite it only for the verification-analogy it supports.

**Decoupling and basis construction as aggregation strategies.** Two further works illustrate the general principle that complex multi-component systems become tractable when decomposed into individually well-behaved pieces. In perturbation theory of vacuum spherically-symmetric spacetimes — a crucial tool for understanding black-hole perturbation dynamics — spherical symmetry allows an expansion in scalar, vector, and tensor harmonics, and the resulting perturbative equations decouple for modes with different parity and different harmonic numbers [4]. Our aggregation analysis in Section 4 exploits the same decoupling idea: under the independence assumption, the joint behavior of the $k$-draft ensemble factorizes into per-draft terms, exactly as harmonic modes decouple in [4]. In a different domain, the construction of a spanning set of individually pure, planar master integrals involving massless particles in four dimensions, including all maximal-weight contributions at two loops, achieves a basis in which every independent infrared-divergent region is individually matched by specific masters while all other masters are manifestly finite [6]. This "one region, one responsible component" design is the ideal we adopt for the aggregator in Section 3: each acceptance decision should be attributable to a specific draft's contribution, so that failure analysis is local. Finally, a master thesis on the pointwise asymptotic expansion of the Bergman kernel of a hermitian holomorphic line bundle introduces a suitable semi-classical symbol space and related symbolic calculus, applicable where the curvature is positive and satisfies a local spectral gap condition [7]. We cite [7] for a single methodological point its entry supports: asymptotic expansions are valid only on the region where their hypotheses (here, curvature positivity and a local spectral gap) hold — a discipline our Section 6 applies to the validity region of our own independence assumption.

**Framework validation methodology.** The QNFO corpus supplies two entries relevant to how multi-axis frameworks should be validated. NUMERATA v2.0 extends an 8-axis framework for evaluating numeral systems with a Distinction-Based Primality axis and reports meta-analysis validation with $\mathrm{MCS} = 0.875$ and 5 out of 5 predictions confirmed, using sunburst notation to make primality visually immediate [10]. The lesson we take is that a framework's axes (in our case: acceptance rate, expected tokens, speedup, overhead) should each be separately checkable, and that meta-validation against held-out predictions is the standard of evidence a framework should aspire to — a standard our purely analytical paper does not yet meet, as we state in Section 6. The QNFO Consilient Synthesis v2.0 document describes a shared adelic kernel (valuation → tree boundary → Ostrowski → adeles) that applies seven corrections (C1–C7) from a red-team audit and is restructured kernel-first with an honest kernel-membership table and mandatory symmetry sections [9]. We adopt two of its practices explicitly: the *honest membership table* (Section 3 states exactly which results belong to the kernel of our assumptions and which do not) and the *red-team audit* posture (Section 6 is written as an adversarial self-audit). One further QNFO entry, on connecting geometrogenesis and biogenesis, has an empty supplied summary; we note its presence in the corpus but the summary gives no further detail, so we draw no claim from it [11]. A final QNFO entry reports a direct mathematical cross-validation of a Kappa / Scale-Invariant Information Thermodynamics framework against the Standard Model's known 1-loop renormalization-group $\beta$-functions, through the single definition $g_{\text{eff}} = g_0 \kappa$ [12]; the entry is truncated, so we cite it only for the practice it exemplifies — cross-validating a new framework against independently known results — which motivates our comparison of the ensemble-drafting projections against the known single-draft limit in Section 4.

## 3. Methods

### 3.1 System model

Fix a target (verifier) model $\mathcal{M}_v$ and a population of $k$ draft models $\mathcal{M}_{d,1}, \dots, \mathcal{M}_{d,k}$, structurally identical in role but differing in parameters — the ensemble-control situation of structurally identical systems with parametric variations [5]. At each verification cycle $t \in \{1, 2, \dots\}$:

1. Each draft $\mathcal{M}_{d,i}$ proposes a block of $\gamma$ tokens $w_{i,1}, \dots, w_{i,\gamma}$.
2. The aggregator $A$ fuses the $k$ proposals into a single block $\tilde{w}_1, \dots, \tilde{w}_\gamma$ (e.g., per-position majority or any-position acceptance).
3. The verifier $\mathcal{M}_v$ checks the fused block in one parallel pass and accepts the longest correct prefix; the broadcast accept/reject signal is sent back to the whole population, with no individualized control input to any draft — the broadcast-only regime of [8].

The state of the population at cycle $t$ is the vector of per-draft agreement indicators. Following the moment-based philosophy of [5], we do not track the full joint state; we track the first moment only, the per-position ensemble acceptance probability $\alpha_e$.

### 3.2 Assumptions (the honest membership table)

Following the kernel-membership discipline of [9], we state exactly which results rest on which assumptions:

- **A1 (per-draft acceptance).** Each draft $i$ has, at each position $j$, an i.i.d. probability $\alpha$ that its proposed token matches the verifier's target token. This is the single-draft acceptance rate.
- **A2 (independence).** The events $\{\text{draft } i \text{ correct at position } j\}$ are independent across $i$ for fixed $j$. This is the strongest assumption and the main target of Section 6.
- **A3 (position-wise decoupling).** Acceptance events at different positions within a block are conditionally independent given the prefix, so the block behaves as a sequence of i.i.d. Bernoulli trials with parameter $\alpha_e$. This mirrors the mode-decoupling structure of [4].
- **A4 (cost model).** Verification cost per cycle is a constant $c_v$ (one parallel pass), and draft cost per cycle is $k \cdot c_d$ (each draft generates its own block). Wall-clock speedup is defined as the ratio of expected accepted tokens per cycle to expected cycle cost, normalized by the single-draft configuration.

Results derived under A1–A3 alone are marked *combinatorial*; results using A4 are marked *cost-dependent*.

### 3.3 Aggregator

We analyze the **any-accept aggregator**: at position $j$, the fused token is accepted by the verifier if at least one draft proposed the correct token. Under A1–A2 the ensemble acceptance probability is

$$\alpha_e(k) = 1 - (1 - \alpha)^k.$$

This is the ensemble analogue of the first moment in moment-based ensemble control [5]: a single scalar sufficient statistic for the population's useful behavior. The any-accept aggregator has the "one region, one master" locality property admired in [6]: a rejected position is attributable to the event that *all* drafts failed, so failure analysis is a single joint event rather than a tangle of interactions.

## 4. Analysis

Every input number is stated with its provenance; every arithmetic step is shown. All results in this section are analytical projections under A1–A4, not measurements.

**Input numbers and provenance.**
- $\alpha = 0.6$: a representative single-draft acceptance rate, chosen for illustration only (no empirical source; labeled an assumption).
- $\gamma = 4$: a representative draft-block length, chosen for illustration only (labeled an assumption).
- $k \in \{1, 2, 3, 5\}$: the draft-population sizes we evaluate.
- $c_d / c_v = 0.05$: the ratio of one draft's per-token generation cost to the verifier's per-token verification cost in the parallel pass; chosen for illustration (labeled an assumption).

**Step 1: ensemble acceptance rate.** Under A1–A2, with $\alpha = 0.6$:

$$\alpha_e(k) = 1 - (1 - 0.6)^k = 1 - 0.4^k.$$

- $k = 1$: $\alpha_e = 1 - 0.4 = 0.6$.
- $k = 2$: $\alpha_e = 1 - 0.16 = 0.84$.
- $k = 3$: $\alpha_e = 1 - 0.064 = 0.936$.
- $k = 5$: $\alpha_e = 1 - 0.01024 = 0.98976$.

**Step 2: expected accepted tokens per cycle.** Under A3, the number of accepted tokens in a block of length $\gamma$ is a truncated geometric random variable. The expected accepted tokens per cycle is

$$E(k, \alpha, \gamma) = \sum_{j=0}^{\gamma - 1} \alpha_e(k)^j = \frac{1 - \alpha_e(k)^{\gamma}}{1 - \alpha_e(k)}.$$

For $k = 1$, $\alpha_e = 0.6$, $\gamma = 4$:

$$E(1) = \frac{1 - 0.6^4}{1 - 0.6} = \frac{1 - 0.1296}{0.4} = \frac{0.8704}{0.4} = 2.176.$$

For $k = 3$, $\alpha_e = 0.936$, $\gamma = 4$:

$$E(3) = \frac{1 - 0.936^4}{1 - 0.936}.$$

Compute $0.936^2 = 0.876096$; $0.936^4 = 0.876096^2 = 0.767544169...$; precisely: $0.876096^2 = 0.767544169216$. Then

$$E(3) = \frac{1 - 0.767544169216}{0.064} = \frac{0.232455830784}{0.064} = 3.632122356.$$

For $k = 2$, $\alpha_e = 0.84$: $0.84^2 = 0.7056$; $0.84^4 = 0.7056^2 = 0.49787136$;

$$E(2) = \frac{1 - 0.49787136}{0.16} = \frac{0.50212864}{0.16} = 3.138304.$$

For $k = 5$, $\alpha_e = 0.98976$: $0.98976^2 = 0.9796246...$; compute: $0.98976^2 = 0.979624657...$ exactly $0.98976 \times 0.98976 = 0.979624657...$; let us be exact: $0.98976^2 = (0.99 - 0.00024)^2 = 0.9801 - 2 \cdot 0.99 \cdot 0.00024 + 0.00024^2 = 0.9801 - 0.0004752 + 0.0000000576 = 0.9796248576$. Then $0.98976^4 = 0.9796248576^2 = 0.95966489...$; compute: $0.9796248576^2 \approx 0.959664892$. Then

$$E(5) = \frac{1 - 0.959664892}{0.01024} = \frac{0.040335108}{0.01024} \approx 3.938978.$$

**Step 3: token-throughput gain over single draft.**

$$G(k) = \frac{E(k)}{E(1)}.$$

- $G(2) = 3.138304 / 2.176 = 1.442229...$
- $G(3) = 3.632122356 / 2.176 = 1.669169...$
- $G(5) = 3.938978 / 2.176 = 1.810097...$

**Step 4: cost-corrected speedup (uses A4).** Per cycle, the expected cost in verifier-equivalent token-passes is $c_v \cdot 1 + k \cdot c_d \cdot \gamma$, since each draft generates $\gamma$ tokens sequentially while the verifier's pass is parallel. With $c_d / c_v = 0.05$ and $\gamma = 4$, the draft overhead per cycle is $k \cdot 0.05 \cdot 4 = 0.2k$ verifier-passes. Define the cost-corrected speedup

$$S(k) = \frac{E(k)}{E(1)} \cdot \frac{1 + 1 \cdot 0.2}{1 + 0.2k} = G(k) \cdot \frac{1.2}{1 + 0.2k}.$$

(The single-draft configuration pays $1 + 0.2$ verifier-passes per cycle; the $k$-draft configuration pays $1 + 0.2k$.)

- $S(2) = 1.442229 \cdot 1.2 / 1.4 = 1.442229 \cdot 0.857143 = 1.236196...$
- $S(3) = 1.669169 \cdot 1.2 / 1.6 = 1.669169 \cdot 0.75 = 1.251877...$
- $S(5) = 1.810097 \cdot 1.2 / 2.0 = 1.810097 \cdot 0.6 = 1.086058...$

**Step 5: break-even draft count.** The cost-corrected speedup is maximized where the marginal token gain equals the marginal cost. Treating $k$ as continuous and using $G(k) \approx$ increasing but concave in $k$ (from the computed values: $G$ rises by $0.266$ from $k=1\to2$... actually from the computed points $G(2)-G(1) = 0.442$, $G(3)-G(2) = 0.227$, $G(5)-G(3) = 0.141$ over two steps, i.e., diminishing returns), while the cost factor $1.2/(1+0.2k)$ falls linearly, the computed discrete values show $S$ peaking at $k = 3$ among the evaluated points ($S(3) = 1.2519 > S(2) = 1.2362 > S(5) = 1.0861$). Beyond $k = 3$, at the assumed cost ratio, additional drafts cost more than they gain: extrapolating the trend of $G$ (increments shrinking roughly geometrically, ratio $\approx 0.5$), $G(4) \approx G(3) + 0.11 \approx 1.78$, giving $S(4) \approx 1.78 \cdot 1.2/1.8 = 1.187 < S(3)$. This extrapolation is labeled a projection with the stated geometric-decrement assumption; its uncertainty is at least $\pm 0.05$ in $S(4)$.

**Step 6: sensitivity to $\alpha$.** Recompute the headline quantity $S(3)$ at $\alpha = 0.4$: $\alpha_e = 1 - 0.6^3 = 1 - 0.216 = 0.784$; $E(3) = (1 - 0.784^4)/0.216$; $0.784^2 = 0.614656$; $0.784^4 = 0.614656^2 = 0.377802...$; exactly $0.614656^2 = 0.377802...$ compute: $0.614656^2 = 0.377802...$; more precisely $0.614656 \times 0.614656 = 0.3778020...$; take $0.377802$; $E(3) = 0.622198/0.216 = 2.880546$. Single-draft: $E(1) = (1 - 0.4^4)/0.6 = (1 - 0.0256)/0.6 = 0.9744/0.6 = 1.624$. $G(3) = 2.880546/1.624 = 1.773427$; $S(3) = 1.773427 \cdot 0.75 = 1.330070$. So at lower single-draft quality the ensemble *gain* is larger in relative terms, because the union-of-events correction $1-(1-\alpha)^k$ is steepest at small $\alpha$.

## 5. Results

All entries are analytical projections computed in Section 4 under assumptions A1–A4 with the stated illustrative parameters ($\alpha = 0.6$, $\gamma = 4$, $c_d/c_v = 0.05$); none are empirical measurements.

| $k$ | $\alpha_e(k)$ | $E(k)$ | $G(k)$ | $S(k)$ |
|---|---|---|---|---|
| 1 | $0.6$ | $2.176$ | $1.000$ | $1.000$ |
| 2 | $0.84$ | $3.138$ | $1.442$ | $1.236$ |
| 3 | $0.936$ | $3.632$ | $1.669$ | $1.252$ |
| 5 | $0.98976$ | $3.939$ | $1.810$ | $1.086$ |

Headline results:

- **R1 (combinatorial).** Under A1–A2, the ensemble acceptance rate is $\alpha_e(k) = 1 - (1-\alpha)^k$; at $\alpha = 0.6$, $k = 3$, $\alpha_e = 0.936$.
- **R2 (combinatorial).** Expected accepted tokens per cycle at $\alpha = 0.6$, $\gamma = 4$ rises from $E(1) = 2.176$ to $E(3) = 3.632$, a token-throughput gain $G(3) = 1.669$.
- **R3 (cost-dependent).** With draft overhead at $5\%$ of verifier cost per token, the cost-corrected speedup peaks among evaluated points at $k = 3$ with $S(3) = 1.252$, and falls to $S(5) = 1.086$; the projected $S(4) \approx 1.19$ (projection with geometric-decrement assumption, uncertainty $\pm 0.05$).
- **R4 (combinatorial).** The framework is most favorable when single drafts are weak: at $\alpha = 0.4$, $S(3) = 1.330$, exceeding the $\alpha = 0.6$ value.

## 6. Discussion

**Limitations and failure modes.** The framework's weakest point is A2, independence of draft errors. Real draft models trained on overlapping data make correlated errors; if drafts fail together, $\alpha_e(k)$ collapses toward $\alpha$, and every gain in Section 5 evaporates. Formally, if the per-position error events have pairwise correlation $\rho$, the true union probability is bounded away from the independence value; a measured $\alpha_e$ below $1-(1-\alpha)^k$ would directly quantify $\rho$. This gives the framework a clean falsification criterion: **measure $\alpha_e$ for a deployed multi-draft system; if it is materially below the independence prediction, A2 is false and the framework's projections overestimate performance.** A second failure mode is A4: we assumed verification cost is independent of $k$, but if the verifier's parallel pass cost grows with block bookkeeping or if aggregation itself is expensive, the cost factor $1.2/(1+0.2k)$ understates overhead and the optimal $k$ shifts downward. Third, A3 (position-wise decoupling) fails when drafts condition on their own earlier proposals within a block; correlated within-block errors break the truncated-geometric formula for $E(k)$, generally in the pessimistic direction. Fourth, all parameter values ($\alpha = 0.6$, $\gamma = 4$, $c_d/c_v = 0.05$) are illustrative assumptions, not measurements; the multimodal benchmarking context of [3], spanning 11 datasets, is exactly where empirical values of $\alpha$ and its variance should be collected, and the entry for [3] is truncated so we cannot import its numbers here.

**Arguing against ourselves.** A skeptic could object that the framework is trivial: $1-(1-\alpha)^k$ is elementary probability, and the ensemble-control framing [5, 8] is decorative. The rebuttal is partial: the framing earns its keep in two places — the broadcast-only constraint of [8] explains *why* per-draft feedback (e.g., letting drafts see each other) changes the problem class, and the moment-based philosophy of [5] justifies tracking only $\alpha_e$ rather than the full joint distribution, which is what makes closed forms possible at all. But the skeptic is right that without empirical validation the paper is a modeling exercise. The standard to aspire to is the meta-analytic validation discipline reported for NUMERATA, with $\mathrm{MCS} = 0.875$ and 5 of 5 predictions confirmed [10]: our framework should generate pre-registered predictions (e.g., $\alpha_e$ values on held-out datasets) that are then checked. We have not done this, and we say so. A second self-criticism: the analogy to verification-as-well-foundedness in [2] and to chaos characterization in [1] is suggestive but loose; we claim from [1] only the methodological precedent of giving an informal process a precise dynamical characterization, and from [2] only the verification-discipline analogy — the entries do not support stronger claims, and [2]'s entry is truncated. Similarly, the cross-validation practice exemplified by [12] — checking a new framework against independently known results — is one we partially honor (Section 4's $k=1$ row reproduces the single-draft baseline by construction) but the entry for [12] is truncated, so we cite it for practice, not content. The empty-summary entry [11] contributes nothing and is listed only for corpus completeness.

**Open questions.** (i) What is the optimal aggregator under correlated draft errors, and does the "one region, one master" locality of [6] survive correlation? (ii) Does the moment-based reduction of [5] extend to tracking the second moment $E[\alpha_e^2]$, which would bound the variance of throughput? (iii) In the multimodal setting of [3], do image-conditioned drafts exhibit lower error correlation than text-only drafts, and if so is the validity region of A2 wider — the analogue of the curvature-positivity region in [7], where the asymptotic analysis is valid only where its hypotheses hold? (iv) What is the empirical $\alpha$ distribution across the 11 benchmark datasets of [3], and does any single $(\alpha, \gamma)$ summarize it?

## 7. Conclusion

We have recast multi-draft speculative decoding as an ensemble-control problem: a population of structurally identical draft generators steered by a broadcast verification signal, tracked through a single moment statistic. Under explicit, falsifiable assumptions, the framework yields closed-form projections — ensemble acceptance $\alpha_e(k) = 1-(1-\alpha)^k$, expected accepted tokens per cycle, and cost-corrected speedup — with all arithmetic shown. At illustrative parameters, three drafts yield a projected $1.67\times$ token-throughput gain and $1.25\times$ cost-corrected speedup over a single draft, with diminishing returns beyond. The framework's value is its falsifiability: a single measured ensemble acceptance rate tests its central independence assumption. Future work must supply the empirical validation the framework itself prescribes.

## References

[1] arXiv:1105.1512v1 | Chaos in DNA inversions (Draft paper)

[2] arXiv:2603.00487v1 | DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments

[3] arXiv:2601.20357v1 | TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs

[4] arXiv:2108.08668v3 | Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes

[5] arXiv:2009.02646v1 | Moment-Based Ensemble Control

[6] arXiv:2610.10672v1 | Prescriptive Master Integrals of Maximal Weight at Two Loops

[7] arXiv:2202.03383v1 | Asymptotic of Bergman Kernel (Master Thesis)

[8] arXiv:2008.03243v1 | Ensemble Control on Lie Groups

[9] QNFO: QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel

[10] QNFO: NUMERATA: A Multi-Axis Framework for Evaluating Numeral Systems

[11] QNFO: Connecting Geometrogenesis and Biogenesis

[12] QNFO: Kappa/SIIT Cross-Validation: Exact Reproduction of Standard Model 1-Loop β-Functions and Resolution of the Harmonic-Paradigm Tension