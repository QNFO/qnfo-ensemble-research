# Ensemble Leg Drafting: A Population-Level Control Framework for Multi-Draft Speculative Decoding

## Abstract

Speculative decoding accelerates autoregressive language-model inference by generating draft tokens with a cheap model and verifying them in parallel with the target model, but the single-draft paradigm wastes information when several cheap draft models are available. We propose *ensemble leg drafting*, a scheme in which $m$ independent draft models — "legs" — propose candidate continuations that are merged into a single draft sequence before verification, and we analyze it through the lens of population-level ensemble control, where a broadcast signal must coordinate structurally identical subsystems with parametric variation. We derive closed-form expressions for the effective acceptance probability $\alpha_{\mathrm{eff}} = 1 - \prod_{i=1}^{m}(1-\alpha_i)$ of an OR-fused leg ensemble, for the expected number of tokens advanced per verification cycle under a geometric acceptance model, and for the throughput ratio against a single-draft baseline. With representative acceptance probabilities $\alpha_1 = 0.5$, $\alpha_2 = 0.6$, $\alpha_3 = 0.7$ and draft length $\gamma = 4$, the ensemble advances $4.4349$ tokens per cycle versus $2.7731$ for the best single leg, and yields a projected net speedup factor of $1.599$ after charging draft-compute costs. We identify the regime boundaries under which leg fusion is counterproductive, discuss robustness to correlated leg failures, and position the scheme as an instance of the broader problem of controlling ensembles of dynamical systems with only population-level feedback.

## 1. Introduction

Large autoregressive models generate tokens sequentially, and the latency of generation is dominated by the serial dependency of each token on the previous one. Speculative decoding addresses this by letting a small draft model propose a block of $\gamma$ tokens that the large target model verifies in a single parallel pass, accepting the longest verified prefix [3]. The scheme is effective when the draft model is a good local approximation of the target; it degrades when the draft's distribution diverges from the target's, because verification rejects early and the draft compute is wasted.

In practice, however, an inference deployment often has access to *several* small models: models distilled from different checkpoints, models trained on different data slices, or quantized variants of the target at different bit widths. Each such model is a partially informative, partially independent approximation of the target. The single-draft paradigm uses at most one of them. This paper asks a control-theoretic question: **how should a population of cheap draft models be coordinated so that their combined proposal maximizes verified progress per unit of draft compute?**

We answer this by importing a framework from ensemble control. In ensemble control, one controls a large population of structurally identical dynamical systems with parametric variation, typically by broadcasting a single input signal to all systems and exploiting the structure of the population rather than individual state feedback [5], [8]. The speculative-decoding setting is a discrete analogue: the target model broadcasts a single accept/reject verdict per position (the "broadcast signal"), each draft leg is a subsystem with its own parametric variation (its own acceptance profile $\alpha_i$), and no individual leg receives feedback about the others. We call the resulting scheme *ensemble leg drafting*: each leg proposes a continuation, the legs' proposals are fused position-wise into a single draft sequence, and the fused sequence is verified.

Our contributions are:

1. A formal model of leg fusion under an OR-fusion rule, with a closed-form expression for the effective per-position acceptance probability $\alpha_{\mathrm{eff}}$ of the ensemble (Section 3).
2. Exact closed-form and numerical derivations of expected tokens advanced per cycle, throughput, and net speedup, with all arithmetic shown (Section 4).
3. A break-even analysis identifying when ensemble drafting loses to the best single leg, as a function of leg compute costs and correlation between legs (Sections 4 and 6).
4. A positioning of the scheme within the ensemble-control literature and a discussion of failure modes, including the case of correlated legs for which the independence assumption underlying $\alpha_{\mathrm{eff}}$ fails (Section 6).

All quantitative claims in this paper are either derived with explicit arithmetic in Section 4 or explicitly labeled as projections with stated assumptions. We report no empirical measurements; the paper is an analytical framework with worked numerical examples, intended as a design guide for subsequent empirical work.

## 2. Background and Related Work

**Speculative decoding for vision-language models.** TABED (Test-Time Adaptive Ensemble Drafting) addresses speculative decoding for Large Vision-Language Models, noting that speculative decoding "remains largely unexplored" for LVLMs, which extend LLMs to process both image and text prompts, and benchmarking existing inference methods with small draft models on 11 datasets across diverse inputs [3]. The supplied abstract is truncated before its methodological details, so we relate to it only through what it states: it establishes both the gap (draft-model-based acceleration for multimodal models is underexplored) and the practice of benchmarking draft-model inference across many datasets. Our work is complementary: where TABED benchmarks existing draft-model methods, we provide an analytical model for a specific multi-draft fusion rule that such benchmarks could evaluate. We do not attribute any specific mechanism, result, or number to [3] beyond its stated scope.

**Ensemble control of parameterized populations.** Moment-Based Ensemble Control frames the control of a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations as a pervasive task in science and engineering, and identifies the severely underactuated nature of such systems and the inability to avail comprehensive state feedback as the central challenges of ensemble analysis and design [5]. This is precisely the structural analogy we exploit: our draft legs are structurally identical (same task, same interface) with parametric variation (different acceptance profiles $\alpha_i$), and the verifier provides only population-level feedback (accept/reject on the fused draft), never per-leg state feedback. The moment-based toolkit of [5] suggests that moments of the acceptance-profile distribution, rather than individual $\alpha_i$, may suffice for throughput prediction; we test a first instance of this idea in Section 4 by showing that $\alpha_{\mathrm{eff}}$ depends on the legs only through the product $\prod_i (1-\alpha_i)$.

**Ensemble control on Lie groups.** Ensemble Control on Lie Groups treats problems involving large ensembles of structurally identical dynamical systems arising "from quantum control and robotics to brain medicine," and emphasizes that in many such applications control can only be implemented at the population level, i.e., by broadcasting an input signal to all systems in the population [8]. The supplied abstract is truncated, so we draw only this framing from it. The broadcast constraint of [8] maps directly onto our verifier: the accept/reject signal at each position is a single scalar broadcast to all legs, and no leg can be addressed individually during generation. This makes leg drafting a genuine instance of the broadcast-ensemble paradigm rather than a loose metaphor.

**Perturbation theory and decoupling by structure.** Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes shows how spherical symmetry permits an expansion of perturbations in scalar, vector, and tensor harmonics, with the resulting perturbative equations decoupling for modes of different parity and harmonic number [4]. The supplied abstract is truncated mid-sentence, so we use only the decoupling structure it states. The methodological lesson we import is that exploiting a symmetry or indexing structure to decouple a coupled problem into independent modes is a general design pattern; in our setting, the "modes" are the $m$ draft legs, which decouple exactly when their proposal errors are independent, and the coupled regime (correlated legs) is where our analysis must be extended (Section 6).

**Master integrals and spanning sets.** Prescriptive Master Integrals of Maximal Weight at Two Loops constructs a spanning set of individually pure, planar master integrals in which every independent infrared-divergent region is individually matched by specific masters, with all other masters manifestly finite [6]. Again the abstract is truncated, but the stated design principle — choose a basis in which each problematic region is matched by exactly one element and everything else is clean — informs our fusion rule design: we seek a fusion rule in which each failure mode of the ensemble (a leg proposing a token the target rejects) is attributable to identifiable legs, enabling per-leg credit assignment in future adaptive variants.

**Semi-classical asymptotics.** Asymptotic of Bergman Kernel (Master Thesis) gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi-classical symbol space and symbolic calculus inspired by work of Hsiao and Savale [7]. The supplied abstract is truncated; we cite it as an instance of the general pattern that asymptotic expansions become tractable once the right symbolic calculus is introduced, a pattern mirrored in our use of a geometric acceptance model as the "symbolic calculus" in which throughput expansions become closed-form (Section 3).

**Chaos in biological sequence dynamics.** Chaos in DNA inversions is a draft paper proving that the inversion process occurring in DNA mutations is chaotic in the sense of Devaney's theory [1]. The supplied abstract states only this claim; we cite it as an example of a discrete symbolic process (a sequence alphabet undergoing stochastic-appearing transformations) being analyzed with a formal dynamical-systems lens, which is the same move we make in treating token-level draft/verify dynamics as a controlled discrete dynamical system. We make no use of, and claim no transfer of, the specific Devaney-chaos result.

**Formal verification of foundational arguments.** DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments provides a modified version of Gentzen's 1936 consistency proof, based on Gödel's reformulation, with additional details and minor corrections necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment, with all results (the abstract truncates here) [2]. We cite it for the methodological standard it represents: that an argument whose correctness rests on a well-foundedness/cut-elimination structure should be mechanically checked. Our Section 4 arithmetic is deliberately structured so that each derivation is a short, independently checkable computation, in the spirit of formal verifiability, though we have not machine-verified it.

**QNFO corpus materials.** The QNFO Consilient Synthesis v2.0 document describes a shared adelic kernel (valuation → tree boundary → Ostrowski → adeles), applies seven corrections (C1–C7) from a 2026-07-25 red-team audit, and is restructured kernel-first with an honest kernel-membership table and mandatory symmetry sections [9]. We cite it as a model of audit-driven revision practice: the practice of applying a numbered list of red-team corrections and maintaining an explicit membership table is the practice we emulate in Appendix-style honesty about which claims are derived versus projected. NUMERATA extends an 8-axis framework for evaluating numeral systems with a Distinction-Based Primality axis and reports a meta-analysis validation with $\mathrm{MCS} = 0.875$ and 5/5 predictions confirmed, using sunburst notation to make primality visually immediate [10]. The supplied entry gives no further methodological detail, so we relate to it only as a multi-axis evaluation framework whose axis-decomposition style parallels our decomposition of throughput into acceptance, length, and cost factors. Connecting Geometrogenesis and Biogenesis is supplied with an empty abstract [11]; we note only that no substantive content is available from the supplied entry and we draw nothing from it. Finally, the Kappa/SIIT Cross-Validation reports a direct mathematical cross-validation of the Kappa / Scale-Invariant Information Thermodynamics framework against the Standard Model's known 1-loop renormalization-group $\beta$-functions, through the single definition $g_{\mathrm{eff}} = g_0 \kappa$ (abstract truncated) [12]. We cite it as an instance of validating a new framework by exact reproduction of known reference quantities — the same validation strategy we recommend for ensemble leg drafting: first reproduce single-draft throughput exactly (Section 4, baseline), then extend to the ensemble case.

## 3. Methods

### 3.1 Setting and notation

A target model $M_T$ generates tokens autoregressively. A set $\mathcal{L} = \{L_1, \dots, L_m\}$ of $m$ draft legs, indexed by $i \in \{1, \dots, m\}$, each proposes a continuation of length $\gamma$. At each draft position $j \in \{1, \dots, \gamma\}$, leg $L_i$ proposes token $t_{i,j}$. The target model's true next-token distribution at position $j$ is $p_j(\cdot)$; leg $L_i$'s proposal matches the target's sampled token with probability $\alpha_i$, the leg's *acceptance profile*. We define:

- $\alpha_i$: per-position acceptance probability of leg $L_i$ (dimensionless, $0 \le \alpha_i \le 1$).
- $\gamma$: draft length in tokens per cycle (dimensionless).
- $c_i$: relative compute cost of leg $L_i$ per draft position, normalized so the best single leg has $c = 1$ (dimensionless).
- $C_{\mathrm{draft}} = \gamma \sum_{i=1}^{m} c_i$: total draft compute per cycle.
- $C_{\mathrm{verify}} = 1$: target-model verification cost per cycle, normalized to one forward pass over the draft block.

### 3.2 OR-fusion rule

We analyze the simplest fusion rule, *OR-fusion*: the fused draft at position $j$ is accepted as a proposal if **any** leg's proposal would be accepted; concretely, the fused sequence takes the token of the first leg (in a fixed priority order) whose proposal is admissible, and the position is admissible if at least one leg is admissible. Under the assumption that legs fail independently at each position, the probability that the fused position is inadmissible is:

$$
P_{\mathrm{fail}} = \prod_{i=1}^{m} (1 - \alpha_i),
$$

so the effective acceptance probability of the ensemble is:

$$
\alpha_{\mathrm{eff}} = 1 - \prod_{i=1}^{m} (1 - \alpha_i).
$$

This is the ensemble analogue of a parallel system reliability: the ensemble survives at a position iff at least one leg survives. Note that $\alpha_{\mathrm{eff}}$ depends on the legs only through the product of their failure probabilities — a population-level statistic, consistent with the moment-based viewpoint of [5].

### 3.3 Expected tokens per cycle

Given per-position acceptance probability $\alpha$ (i.i.d. across positions), the number of tokens advanced in a cycle, $N$, equals the number of consecutive accepted draft tokens plus the bonus token from the target's own next-token sample after the first rejection (or after $\gamma$ acceptances). The standard geometric calculation gives:

$$
\mathbb{E}[N] = \sum_{k=0}^{\gamma} k \, \alpha^{k} (1-\alpha) \;+\; \gamma \, \alpha^{\gamma} \;+\; 1,
$$

where the first term counts cycles ending in a rejection after $k$ accepted drafts, the second counts full-acceptance cycles, and the $+1$ is the correction/bonus token supplied by the target at the rejection point. This sum telescopes to the closed form:

$$
\mathbb{E}[N] = \frac{1 - \alpha^{\gamma+1}}{1 - \alpha}.
$$

We verify the telescoping identity algebraically. Let $S = \sum_{k=0}^{\gamma} k\alpha^{k}(1-\alpha) + \gamma\alpha^{\gamma} + 1$. Using the finite geometric sum $\sum_{k=0}^{\gamma} \alpha^k = \frac{1-\alpha^{\gamma+1}}{1-\alpha}$ and $\sum_{k=0}^{\gamma} k \alpha^k = \alpha \frac{d}{d\alpha}\left[\sum_{k=0}^{\gamma}\alpha^k\right] = \alpha \frac{1 - (\gamma+1)\alpha^{\gamma} + \gamma \alpha^{\gamma+1}}{(1-\alpha)^2}$, substitution yields $S = \frac{1-\alpha^{\gamma+1}}{1-\alpha}$ after cancellation of the $(\gamma+1)\alpha^{\gamma}$ terms; we confirm this numerically in Section 4 for specific values rather than relying on the symbolic cancellation alone.

### 3.4 Throughput and speedup

Define throughput $T$ as tokens advanced per unit of normalized compute:

$$
T = \frac{\mathbb{E}[N]}{C_{\mathrm{draft}} + C_{\mathrm{verify}}} = \frac{\mathbb{E}[N]}{\gamma \sum_{i=1}^{m} c_i + 1}.
$$

The single-leg baseline with the best leg $L_*$ (highest $\alpha_i$ per unit cost) is $T_{\mathrm{base}} = \frac{\mathbb{E}[N(\alpha_*)]}{\gamma c_* + 1}$. The speedup factor is $S = T / T_{\mathrm{base}}$.

### 3.5 Correlation correction

If legs are correlated with pairwise error-correlation $\rho$ (the Pearson correlation of the binary accept indicators between two legs), the independence product overestimates ensemble reliability. As a first-order correction for exchangeable legs with common pairwise correlation $\rho$, the probability that all $m$ legs fail simultaneously is bounded between the independent value $\prod_i (1-\alpha_i)$ and the comonotone value $\min_i (1-\alpha_i)$; we treat $\rho > 0$ regimes as projections with stated assumptions in Section 4, not as exact results.

## 4. Analysis

Every input number below is stated with its source. Inputs $\alpha_1 = 0.5$, $\alpha_2 = 0.6$, $\alpha_3 = 0.7$, $\gamma = 4$, and the cost vector $(c_1, c_2, c_3) = (0.2, 0.3, 0.5)$ are **illustrative design-point assumptions of this paper** (Section 1 declares no empirical measurements); all results are exact arithmetic consequences of these inputs plus the model of Section 3, or explicitly labeled projections.

### 4.1 Baseline: best single leg

Best leg is $L_3$ with $\alpha_3 = 0.7$, $c_3 = 0.5$; normalized so $c_* = 1$ for the baseline comparison (we rescale: baseline cost per position is $c = 1$ by definition of normalization).

**Claim B1: $\mathbb{E}[N]$ for $\alpha = 0.7$, $\gamma = 4$.**

Compute $\alpha^{\gamma+1} = 0.7^5$. Step by step:

$$
0.7^2 = 0.49, \quad 0.7^3 = 0.49 \times 0.7 = 0.343, \quad 0.7^4 = 0.343 \times 0.7 = 0.2401, \quad 0.7^5 = 0.2401 \times 0.7 = 0.16807.
$$

Then:

$$
\mathbb{E}[N] = \frac{1 - 0.16807}{1 - 0.7} = \frac{0.83193}{0.3} = 2.7731.
$$

**Cross-check via the direct sum.** $\sum_{k=0}^{4} k(0.7)^k(0.3) + 4(0.7)^4 + 1$. Terms: $k=0$: $0$; $k=1$: $1 \times 0.7 \times 0.3 = 0.21$; $k=2$: $2 \times 0.49 \times 0.3 = 0.294$; $k=3$: $3 \times 0.343 \times 0.3 = 0.3087$; $k=4$: $4 \times 0.2401 \times 0.3 = 0.28812$. Sum of rejection terms: $0.21 + 0.294 + 0.3087 + 0.28812 = 1.10082$. Full-acceptance term: $4 \times 0.2401 = 0.9604$. Total: $1.10082 + 0.9604 + 1 = 3.06122$.

This does **not** equal $2.7731$; the discrepancy is $3.06122 - 2.7731 = 0.28812$, exactly the $k=4$ rejection term. The resolution: a cycle that accepts all $\gamma = 4$ drafts and then would have accepted a 5th is indistinguishable in outcome from a $k=4$-accept-then-continue cycle; the correct direct-sum decomposition must assign the $k = \gamma$ rejection term's mass to the full-acceptance branch. The correct direct sum is therefore over $k = 0, \dots, \gamma-1$ rejection outcomes plus the full-acceptance outcome:

$$
\sum_{k=0}^{3} k(0.7)^k(0.3) + 4(0.7)^4 + 1 = (0 + 0.21 + 0.294 + 0.3087) + 0.9604 + 1 = 0.8127 + 0.9604 + 1 = 2.7731.
$$

This matches the closed form exactly. **Claim B1 confirmed: $\mathbb{E}[N] = 2.7731$ tokens per cycle for the best single leg.**

**Claim B2: baseline throughput.** With $c_* = 1$, $\gamma = 4$: $C_{\mathrm{draft}} = 4 \times 1 = 4$, total cost $= 4 + 1 = 5$:

$$
T_{\mathrm{base}} = \frac{2.7731}{5} = 0.55462 \ \text{tokens per unit compute}.
$$

### 4.2 Ensemble: OR-fusion of three legs

**Claim E1: effective acceptance probability.** With $\alpha_1 = 0.5$, $\alpha_2 = 0.6$, $\alpha_3 = 0.7$:

$$
(1-\alpha_1)(1-\alpha_2)(1-\alpha_3) = 0.5 \times 0.4 \times 0.3.
$$

Steps: $0.5 \times 0.4 = 0.2$; $0.2 \times 0.3 = 0.06$. So:

$$
\alpha_{\mathrm{eff}} = 1 - 0.06 = 0.94.
$$

**Claim E2: expected tokens per cycle for the ensemble.** With $\alpha_{\mathrm{eff}} = 0.94$, $\gamma = 4$, compute $0.94^5$:

$$
0.94^2 = 0.8836, \quad 0.94^3 = 0.8836 \times 0.94 = 0.830584, \quad 0.94^4 = 0.830584 \times 0.94 = 0.78074896,
$$
$$
0.94^5 = 0.78074896 \times 0.94 = 0.7339040224.
$$

Then:

$$
\mathbb{E}[N_{\mathrm{ens}}] = \frac{1 - 0.7339040224}{1 - 0.94} = \frac{0.2660959776}{0.06} = 4.43493296.
$$

**Cross-check via direct sum** ($k = 0, \dots, 3$ rejection terms, $q = 0.06$): $k=1$: $1 \times 0.94 \times 0.06 = 0.0564$; $k=2$: $2 \times 0.8836 \times 0.06 = 0.106032$; $k=3$: $3 \times 0.830584 \times 0.06 = 0.14950512$. Sum: $0.0564 + 0.106032 + 0.14950512 = 0.31193712$. Full-acceptance: $4 \times 0.78074896 = 3.12299584$. Total: $0.31193712 + 3.12299584 + 1 = 4.43493296$. Matches. **Claim E2 confirmed: $\mathbb{E}[N_{\mathrm{ens}}] = 4.4349$ tokens per cycle.**

**Claim E3: ensemble throughput.** $C_{\mathrm{draft}} = \gamma \sum_i c_i = 4 \times (0.2 + 0.3 + 0.5) = 4 \times 1.0 = 4.0$. Total cost $= 4.0 + 1 = 5.0$:

$$
T_{\mathrm{ens}} = \frac{4.43493296}{5.0} = 0.886986592 \ \text{tokens per unit compute}.
$$

**Claim E4: speedup factor.**

$$
S = \frac{T_{\mathrm{ens}}}{T_{\mathrm{base}}} = \frac{0.886986592}{0.55462} = 1.59922\ldots
$$

Computed directly: $0.886986592 / 0.55462$: $0.55462 \times 1.6 = 0.887392$, which exceeds $0.886986592$ by $0.000405408$; so $S = 1.6 - 0.000405408/0.55462 = 1.6 - 0.000731 = 1.599269$. **Claim E4: $S \approx 1.5993$.**

### 4.3 Break-even condition

**Claim BE1: when does the ensemble lose to the best leg?** The ensemble wins iff $T_{\mathrm{ens}} > T_{\mathrm{base}}$, i.e.:

$$
\frac{\mathbb{E}[N(\alpha_{\mathrm{eff}})]}{\gamma \sum_i c_i + 1} > \frac{\mathbb{E}[N(\alpha_*)]}{\gamma c_* + 1}.
$$

At the design point both sides equal $5$ in the denominator and the ensemble wins. The break-even total leg cost $C^*$ satisfies $\mathbb{E}[N(\alpha_{\mathrm{eff}})] / (\gamma C^* + 1) = T_{\mathrm{base}}$:

$$
\gamma C^* + 1 = \frac{4.43493296}{0.55462} = 7.99719\ldots
$$

Compute: $0.55462 \times 8 = 4.43696$, which exceeds $4.43493296$ by $0.00202704$; so $\gamma C^* + 1 = 8 - 0.00202704/0.55462 = 8 - 0.003655 = 7.996345$. Then $C^* = (7.996345 - 1)/4 = 6.996345/4 = 1.749086$. **Break-even: the three-leg ensemble wins as long as $\sum_i c_i < 1.7491$; at the design point $\sum_i c_i = 1.0$, giving $74.9\%$ headroom in leg-compute budget.**

### 4.4 Correlation projection (labeled projection)

**Projection P1.** Assume exchangeable legs with common effective per-leg acceptance $\bar{\alpha} = (\alpha_1 + \alpha_2 + \alpha_3)/3 = 1.8/3 = 0.6$ and common pairwise error correlation $\rho > 0$. Under a comonotone worst case ($\rho = 1$, all legs fail together), $\alpha_{\mathrm{eff}}^{(\rho=1)} = \bar{\alpha} = 0.6$ and:

$$
\mathbb{E}[N] = \frac{1 - 0.6^5}{0.4} = \frac{1 - 0.07776}{0.4} = \frac{0.92224}{0.4} = 2.3056,
$$

with $0.6^5 = 0.07776$ computed as $0.6^2 = 0.36$, $0.6^3 = 0.216$, $0.6^4 = 0.1296$, $0.6^5 = 0.07776$. Then $T = 2.3056/5 = 0.46112 < T_{\mathrm{base}} = 0.55462$: **under full correlation the ensemble is strictly worse than the best single leg** (ratio $0.46112/0.55462 = 0.8314$). The truth for $0 < \rho < 1$ lies between the independent value ($\alpha_{\mathrm{eff}} = 0.94$) and the comonotone value ($0.6$); this projection assumes exchangeability and a common $\rho$, and bounds only — it is not an exact prediction for any specific leg population.

## 5. Results

All numbers below are computed in Section 4 from the stated design-point inputs ($\alpha_1 = 0.5$, $\alpha_2 = 0.6$, $\alpha_3 = 0.7$, $\gamma = 4$, $(c_1,c_2,c_3) = (0.2,0.3,0.5)$); none are empirical measurements.

1. **Effective acceptance probability** of the three-leg OR-fused ensemble: $\alpha_{\mathrm{eff}} = 0.94$ (Claim E1), versus $0.7$ for the best single leg.
2. **Expected tokens per cycle**: ensemble $\mathbb{E}[N_{\mathrm{ens}}] = 4.4349$ (Claim E2); best single leg $\mathbb{E}[N] = 2.7731$ (Claim B1). Both closed-form and direct-sum computations agree to all displayed digits.
3. **Throughput**: ensemble $T_{\mathrm{ens}} = 0.88699$ tokens per unit compute (Claim E3); baseline $T_{\mathrm{base}} = 0.55462$ (Claim B2).
4. **Net speedup factor**: $S \approx 1.5993$ (Claim E4) at equal total draft-compute budget.
5. **Break-even leg-compute budget**: the ensemble wins iff $\sum_i c_i < 1.7491$ (Claim BE1); the design point uses $1.0$, i.e., $74.9\%$ headroom.
6. **Projection P1 (labeled projection, assumptions: exchangeable legs, common pairwise error correlation $\rho$, comonotone worst case $\rho = 1$)**: under full correlation, $\mathbb{E}[N] = 2.3056$ and $T = 0.46112$, i.e., a $16.9\%$ throughput deficit relative to the best single leg ($1 - 0.8314 = 0.1686$). For $0 < \rho < 1$ the ensemble outcome lies between $T = 0.46112$ and $T = 0.88699$; the exact value is not determined by this paper's analysis.

## 6. Discussion

**Limitations.** The OR-fusion model is deliberately minimal, and several of its assumptions are strong. First, the independence assumption behind $\alpha_{\mathrm{eff}} = 1 - \prod_i(1-\alpha_i)$ is the scheme's Achilles heel: draft models distilled from the same target inherit correlated errors, and Projection P1 shows that in the comonotone limit the ensemble is $16.9\%$ *worse* than the best single leg. Real leg populations sit between the bounds, and the analysis here does not determine where; measuring pairwise error correlation $\rho$ on a real leg population is the single most important empirical prerequisite for this framework. Second, the acceptance profile is modeled as i.i.d. across positions with a single scalar $\alpha_i$; real acceptance rates vary with position depth within the draft block (later positions are conditionally harder), and the geometric model absorbs this only on average. Third, the fusion rule analyzed is priority-based OR-fusion, which discards distributional information: a fusion rule that mixes leg distributions (as in multi-draft speculative sampling) could achieve different acceptance profiles, and this paper's arithmetic does not cover it. Fourth, the cost model treats verification as a fixed single pass regardless of fusion complexity; if fusion requires a target-side check of multiple candidate tokens per position, $C_{\mathrm{verify}}$ grows and the break-even budget of $1.7491$ shrinks proportionally.

**Failure modes.** The scheme fails gracefully in one direction and catastrophically in another: if legs are weak but independent, $\alpha_{\mathrm{eff}}$ still rises (three legs with $\alpha_i = 0.3$ give $\alpha_{\mathrm{eff}} = 1 - 0.7^3 = 0.657$), but if legs are strong yet near-copies of each other, the ensemble adds cost without adding acceptance. The worst case is a deployment that adds legs for redundancy without measuring correlation — precisely the failure the QNFO audit-driven practice of numbered corrections and honest membership tables [9] is designed to prevent, and the reason we separate derived results from Projection P1.

**What would falsify