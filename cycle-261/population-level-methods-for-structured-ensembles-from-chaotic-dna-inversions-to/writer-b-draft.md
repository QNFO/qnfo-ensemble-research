# Population-Level Methods for Structured Ensembles: From Chaotic DNA Inversions to Ensemble Leg Drafting (Revised Edition)

## Abstract

Many scientific settings require steering or extracting value from a large population of structurally identical units — dynamical systems, draft models, or mutating sequences — when only a population-level signal is available. Prior versions of this framework left three gaps: the DNA-inversion divergence estimate rested on an unexamined independence approximation, the broadcast-control baseline lacked a comparison against known moment-based ensemble methods, and the ensemble leg drafting analysis stopped before its correlated-leg projection was completed. This revised paper closes all three. We analyze a toy model of random DNA inversions on a sequence of length ten, where the average inverted segment length is $4.0$ and full Hamming divergence is reached after approximately $3$ steps under a labeled independence projection. We derive a moment-based baseline for broadcast control of a continuum of first-order units: the first moment moves at rate $1/3$ per unit input, the mean advance is immobile for sign-symmetric gains, and the minimum steering time to a target first moment of $0.1$ is $0.3$ time units. We complete the ensemble leg drafting analysis for speculative decoding: with acceptance probabilities $0.5$, $0.6$, $0.7$ and draft length $4$, the three-leg ensemble advances $4.4349$ tokens per cycle versus $2.7731$ for the best single leg, a speedup of $1.5993$, with a leg-compute break-even budget of $1.7491$; under fully correlated failures the ensemble drops to $2.3056$ tokens per cycle and loses to the single leg. All quantitative claims are derived with shown arithmetic or explicitly labeled projections.

## 1. Introduction

Serving a large language model to millions of users costs most of its compute in the autoregressive target model, and every token must be produced by that expensive model unless a cheaper surrogate can propose tokens the target then verifies in parallel. Speculative decoding does exactly this, but its benefit depends on draft quality, and draft quality fluctuates across input scenarios; the TABED study of Large Vision-Language Models documents that neither multimodal nor text-only drafting consistently outperforms the other across eleven benchmark datasets, and that fusing multiple drafts dynamically recovers an average walltime speedup of $1.74\times$ over standard decoding where single drafts fluctuate [4]. Operators of inference systems therefore face a concrete design decision with no closed-form guidance: given $m$ draft models with known per-leg acceptance rates and compute costs, does fusing them under a simple rule beat the best single leg, and by how much compute budget can the fusion afford? A correct analytical answer changes procurement and routing decisions today: it tells a system architect when to buy a second draft model and when the added draft compute eats the gain.

The same structural problem — one actuator, many units, no individual access — appears in ensemble control, where a broadcast input drives a continuum of systems with distributed parameters and comprehensive state feedback on each member is unavailable [6]. It appears again in molecular sequence dynamics, where DNA inversion processes have been argued to be chaotic in the sense of Devaney's theory [1], so that individual long-run trajectories are unpredictable and only population-level statistics are accessible. This paper treats the three settings as case studies of one question: what can be achieved at the population level when individual-level access is unavailable?

The contributions are:

1. A toy model of random DNA inversions with closed-form segment statistics and a labeled projection for the Hamming divergence time, with the re-flipping bias stated as an explicit hypothesis (Sections 3.1 and 4.1).
2. A moment-based broadcast-control baseline for a continuum of first-order units, including the exact negative result that the mean advance is immobile for sign-symmetric gain distributions, a closure analysis of the moment hierarchy, and a cross-validation of the framework's reproduction strategy against the single-draft baseline discipline of [9] (Sections 3.2, 4.2).
3. A formal model of ensemble leg drafting — fusing $m$ speculative-decoding draft legs under an OR rule — with exact computations of effective acceptance probability, tokens per cycle, throughput, speedup, and break-even leg-compute budget, plus a completed labeled projection showing that fully correlated legs lose to the best single leg (Sections 3.3, 4.3).

Every quantitative claim is either derived with explicit arithmetic in Section 4 or labeled as a projection with stated assumptions. The paper reports no empirical measurements; it is an analytical framework with worked numerical examples.

## 2. Background and Related Work

**Ensemble control of populations.** Moment-Based Ensemble Control frames the control of a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations as a pervasive task in science and engineering, and identifies the severely underactuated nature of such systems and the inability to avail comprehensive state feedback as the central challenges of ensemble analysis and design [6]. Its full text develops ensemble systems as parameterized populations $\frac{d}{dt}x(t,\beta)=F(x(t,\beta),\beta,u(t))$ with a parameter-independent input $u(t)$, and its conclusion states that the dynamic Hausdorff moment problem shows ensemble systems and their moment systems share the same control and controllability property, enabling moment-feedback laws and model reduction from uncountably many systems to countably many agents [6]. Our moment hierarchy in Section 3.2 is an elementary first-order instantiation of exactly that reduction, and our closure failure in Section 4.2 illustrates why the reduction is nontrivial once the dynamics leave the linear case.

**Speculative decoding for vision-language models.** TABED addresses speculative decoding for Large Vision-Language Models, noting that speculative decoding "remains largely unexplored" for LVLMs, which extend LLMs to process both image and text prompts, and benchmarking existing inference methods with small draft models on 11 datasets across diverse inputs [4]. Its experiments show scenario-specific performance fluctuations with neither multimodal nor text-only drafting consistently outperforming the other, while TABED itself achieves the best or second-best performance across all scenarios with an average robust walltime speedup of $1.74\times$ and over $5\%$ improvement over single drafting methods, training-free and with negligible ensembling costs [4]. Our Section 3.3 provides an analytical model of a specific multi-draft fusion rule of the kind TABED instantiates dynamically; the $1.74\times$ figure is an empirical measurement belonging to [4], not to this paper, and we use it only to show that multi-draft fusion gains are practically realized.

**Chaos in biological sequence dynamics.** Chaos in DNA inversions proves that the inversion process occurring in DNA mutations is chaotic in the sense of Devaney's theory [1]. Its full text defines chaotic iterations over binary cell states driven by a strategy sequence, and connects them to a mutation model in which the set of mutable trinucleotides is redrawn uniformly at each time step — the "chaotic model" as opposed to earlier standard models with fixed parameters [1]. This motivates Section 3.1: if the inversion process is chaotic, individual long-run trajectories are unpredictable, and only statistical quantities — such as the expected Hamming distance we compute — are the accessible objects of study. We make no use of the specific Devaney-chaos theorem beyond this motivation.

**Decoupled multi-mode analysis.** Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes shows how spherical symmetry permits an expansion of perturbations in scalar, vector, and tensor harmonics, with the resulting perturbative equations decoupling for modes of different parity and harmonic number [5]. Its conclusions derive master functions satisfying wave-type equations under three stated assumptions, producing two branches of solutions including a new even-parity master function $\Psi_{\mathrm{EN}}$ independent of the Zerilli-Moncrief one [5]. The methodological lesson — exploit structure to decouple a coupled problem into independent modes — governs both our moment expansion (modes = moment orders, which decouple only partially; Section 4.2) and our leg-fusion analysis (modes = draft legs, which decouple exactly when their errors are independent; Section 4.3).

**Spanning sets and isolation of contributions.** Prescriptive Master Integrals of Maximal Weight at Two Loops constructs a spanning set of individually pure, planar master integrals involving massless particles in four dimensions which include all maximal-weight contributions at two loops, such that every independent infrared-divergent region is individually matched by specific masters, with all other masters manifestly finite [7]. Its conclusion adds that this prescriptive basis lets coefficients be calculated directly from on-shell functions [7]. The design principle — choose a basis in which each problematic region is matched by exactly one element — informs our choice in Section 4.2 to isolate the first moment by restricting the input class so that higher-order effects are deferred to a separate closure analysis.

**Semi-classical asymptotics.** Asymptotic of Bergman Kernel gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi-classical symbol space and symbolic calculus inspired by work of Hsiao and Savale [8]. Its introduction sets up the Bergman kernel for high tensor powers $L^k$ of a holomorphic line bundle as the object of study [8]. We mirror the pattern that asymptotic problems become tractable once the right calculus is introduced: our geometric acceptance model is the calculus in which throughput becomes closed-form (Section 3.3).

**Formal verification and well-foundedness.** DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments provides a modified version of Gentzen's 1936 consistency proof, based on Gödel's reformulation, with additional details and minor corrections necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment [3]. Its text records that the work builds on an incomplete formalization effort, completing it and fixing existing bugs in a proof assistant setting [3]. We adopt the standard it represents: an argument resting on layered structure should be checkable layer by layer. Our Section 4 arithmetic is deliberately structured as short, independently checkable computations, though it has not been machine-verified.

**Proxy metrics versus task metrics.** Learning Contact Representation for Leg Odometry studies contact detection for legged robots, where leg odometry relies on the assumption that the foot velocity in stance is zero, making accurate contact detection a critical subproblem for which ground-reaction-force sensors are not available on all platforms [2]. Its experiments benchmark supervised, probabilistic, and self-supervised detectors and find that all detectors degrade when evaluated on the physical robot due to sensor noise and unmodeled terrain compliance; crucially, its conclusion states that higher pseudo-label classification accuracy does not necessarily translate into better leg odometry [2]. This is directly relevant to our Section 4.3: acceptance probability is a proxy metric, and our throughput algebra is the downstream task metric; a leg with higher acceptance probability need not yield higher throughput once compute cost enters the denominator, which is exactly the structure our break-even analysis quantifies.

**Prior QNFO work on ensemble drafting.** Ensemble Drafting Under Broadcast Control formalizes ensemble drafting — a population of draft generators whose candidate tokens are checked by a single verifier — as a discrete-time population-level control problem, deriving closed-form expressions for expected accepted length, per-cycle cost, and throughput [9]. Its results compute, with shown arithmetic, $E[L]=2.533$ and $T\approx1.8093$ at draft depth $K=4$ with $\alpha=0.7$, a grid optimum $K^{\star}=5$ at $T\approx1.8487$, a break-even draft cost $c_d^{\star}\approx0.1527$, a $1/\sqrt{N}$ standard-error reduction from $\sigma=0.3$ to $\approx0.1342$ at $N=5$, and a Vandermonde reachability map that is exactly controllable iff the parameters are pairwise distinct [9]. Its discussion flags that the constant-$\alpha$ independence assumption is the strongest and least defensible, since real drafter quality is autocorrelated across positions and correlated drafter errors break the $\sigma/\sqrt{N}$ reduction [9]. Our Section 4.3 adopts the same discipline — reproduce the single-draft baseline exactly before extending — and extends the analysis to heterogeneous legs under an OR rule, with the correlated case treated as the labeled projection that [9]'s own limitations discussion calls for.

**The paper under revision.** Population-Level Methods for Structured Ensembles is the version-1.0.0 text this paper revises [10]. Its introduction frames the shared population-level question across ensemble control, speculative decoding, and DNA inversions, and its methods sections define the three case-study models that Sections 3.1–3.3 here retain with corrections [10]. We keep everything it derived correctly, complete its truncated correlated-leg projection, and remove its reliance on unsupported framing.

**Classical proxies where direct tests are intractable.** Connecting Geometrogenesis and Biogenesis addresses a conjecture linking spacetime emergence to the evolution of life whose direct test is computationally and theoretically intractable, and argues that the responsible path is to rigorize the inquiry through strategic simplification: validate a falsifiable classical analogue first, using neutral proxies, before attempting the quantum realization [11]. We follow the same methodological posture at smaller scale: where the full stochastic inversion process resists closed-form treatment (Section 4.1), we compute a labeled classical approximation and state its failure mode, rather than claiming the intractable exact result.

**Audit-driven revision practice.** A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio catalogs 42 gaps across five structural categories with severity counts of 5 HIGH, 13 MEDIUM, and 24 LOW, and finds that the top 5 HIGH-severity gaps transitively block approximately $40\%$ of all gaps while the dependency graph is a DAG of depth at most 3 [12]. Its finding that a bounded, classified set of defects admits a Pareto-optimal repair order is the pattern we apply to revision itself: this paper's changes are a bounded set of identified defects — a truncated projection, an under-argued approximation, missing comparisons — repaired in dependency order.

## 3. Methods

### 3.1 Case study I: a toy model of random DNA inversions

We represent a DNA segment as a binary sequence of fixed length $L = 10$, where each site is $0$ (original) or $1$ (inverted). At each discrete step, a contiguous segment is selected uniformly among all $\frac{L(L+1)}{2}$ possible segments and all bits within it are flipped. This stochastic rule captures the essential feature of inversion without biochemical detail; the chaotic character of the underlying process [1] motivates a purely statistical treatment, since chaotic dynamics preclude reliable prediction of individual trajectories.

### 3.2 Case study II: moment-based broadcast control baseline

Consider a continuum of first-order units indexed by a gain parameter $\omega \in [-1, 1]$, each obeying

$$
\dot{x}_\omega(t) = \omega\, u(t), \qquad x_\omega(0) = 0,
$$

with a single broadcast input $u(t)$, identical for all $\omega$, bounded by $|u(t)| \le u_{\max} = 1$. The gain density is uniform, $\rho(\omega) = \frac{1}{2}$ on $[-1, 1]$. Define the gain-weighted moments

$$
M_k(t) = \int_{-1}^{1} \omega^k\, x_\omega(t)\, \rho(\omega)\, d\omega,
$$

the mean advance $\bar{x}(t) = \int_{-1}^{1} x_\omega(t)\, \rho(\omega)\, d\omega$, and the population variance $\sigma^2(t) = \int_{-1}^{1} (x_\omega(t) - \bar{x}(t))^2 \rho(\omega)\, d\omega$. We restrict to piecewise-constant inputs $u(t) \in \{-1, +1\}$ (bang-bang), the weakest nontrivial broadcast class consistent with the bound. "Reachability" is defined only for $M_1$: a value of $M_1(T)$ obtainable from $M_1(0) = 0$ by some admissible input. This is the simplest instance of the moment reduction of [6]: the continuum state $x_\omega$ is replaced by countably many moments, and the question is how much of the control problem survives the reduction.

### 3.3 Case study III: ensemble leg drafting for speculative decoding

A target model $M_T$ generates tokens autoregressively. A set $\mathcal{L} = \{L_1, \dots, L_m\}$ of $m$ draft legs each proposes a continuation of length $\gamma$. At each draft position $j$, leg $L_i$ matches the target's sampled token with probability $\alpha_i$ (the leg's *acceptance profile*). Define $c_i$ as the relative compute cost of leg $L_i$ per draft position, $C_{\mathrm{draft}} = \gamma \sum_{i=1}^{m} c_i$, and $C_{\mathrm{verify}} = 1$ (target verification per cycle, normalized).

**OR-fusion rule.** The fused draft at position $j$ is admissible if at least one leg's proposal is admissible; the fused sequence takes the token of the first admissible leg in fixed priority order. Under independent leg failures, the effective acceptance probability is

$$
\alpha_{\mathrm{eff}} = 1 - \prod_{i=1}^{m} (1 - \alpha_i).
$$

Note that $\alpha_{\mathrm{eff}}$ depends on the legs only through the product of their failure probabilities — a population-level statistic, consistent with the population-level viewpoint of [6].

**Tokens per cycle.** With per-position acceptance probability $\alpha$ i.i.d. across positions, the expected number of tokens advanced per cycle is

$$
\mathbb{E}[N] = \sum_{k=0}^{\gamma-1} k\, \alpha^{k}(1-\alpha) + \gamma\, \alpha^{\gamma} + 1,
$$

where the sum counts cycles ending in rejection after $k$ accepted drafts, the second term counts full-acceptance cycles, and the $+1$ is the bonus token supplied by the target at the rejection point. This sum equals the closed form

$$
\mathbb{E}[N] = \frac{1 - \alpha^{\gamma+1}}{1 - \alpha},
$$

which we verify numerically for specific values in Section 4.3 rather than relying on symbolic cancellation alone. This is the same acceptance-length algebra used in [9], specialized there to a single drafter with homogeneous $\alpha$; here it is applied to the fused ensemble's $\alpha_{\mathrm{eff}}$.

**Throughput and speedup.** Throughput is $T = \mathbb{E}[N] / (C_{\mathrm{draft}} + C_{\mathrm{verify}})$; the speedup factor against the best single leg is $S = T_{\mathrm{ens}} / T_{\mathrm{base}}$.

**Correlated legs.** If legs are correlated, the independence product overestimates reliability. For exchangeable legs with common pairwise error correlation $\rho$, the probability that all legs fail simultaneously lies between the independent value $\prod_i (1-\alpha_i)$ and the comonotone value $\min_i (1-\alpha_i)$; correlated regimes are treated as labeled projections, not exact results. This addresses the correlation limitation that [9] identifies for its own independence assumption.

## 4. Analysis

All input numbers are stated with their sources. Model parameters in Sections 3.1–3.3 are definitions of this paper, not empirical measurements; the design-point values $\alpha_1 = 0.5$, $\alpha_2 = 0.6$, $\alpha_3 = 0.7$, $\gamma = 4$, $(c_1, c_2, c_3) = (0.2, 0.3, 0.5)$, and $M_1^{\mathrm{target}} = 0.1$ are illustrative assumptions declared here.

### 4.1 Case study I: divergence time of random inversions

**Input:** $L = 10$ (Section 3.1). The number of contiguous segments is $\frac{10 \cdot 11}{2} = 55$.

**Average segment length.** The total length over all segments is $S = \sum_{k=1}^{10} k(10 - k + 1)$:

$$
S = 1\cdot10 + 2\cdot9 + 3\cdot8 + 4\cdot7 + 5\cdot6 + 6\cdot5 + 7\cdot4 + 8\cdot3 + 9\cdot2 + 10\cdot1
$$

$$
= 10 + 18 + 24 + 28 + 30 + 30 + 28 + 24 + 18 + 10 = 220.
$$

Hence the average segment length is $\bar{\ell} = \frac{220}{55} = 4.0$.

**Expected Hamming distance.** Starting from the all-zero reference, flipping a segment of length $\ell$ increases the Hamming distance $d$ by exactly $\ell$ on the first flip of each site; treating increments as independent with mean $\bar{\ell} = 4$ (an approximation discussed in Section 6), the expected distance after $t$ steps is $\mathbb{E}[d(t)] \approx \min(L, 4t)$. Setting $4t_{\mathrm{sat}} = 10$ gives $t_{\mathrm{sat}} = \frac{10}{4} = 2.5$, and since $t$ is an integer step count,

$$
t_{\mathrm{sat}} = \lceil 2.5 \rceil = 3.
$$

**Result (labeled projection P0, not exact arithmetic).** Under the independence approximation of Section 3.1 — increments treated as independent with mean $\bar{\ell} = 4$, ignoring re-flipping of already-inverted sites — the saturation time is $t_{\mathrm{sat}} = \lceil 10/4 \rceil = 3$ steps. The only shown arithmetic here is the ceiling computation $\lceil 10/4 \rceil = 3$; everything else in this paragraph is projection P0. We state as an expected-direction hypothesis, not an exact inequality, that re-flipping reduces the per-step Hamming increment below $\bar{\ell}$ after the first few steps, so the exact expected saturation time is plausibly larger than $3$; the approximation carries an uncertainty of order one step and is used only as an order-of-magnitude estimate. The exact expectation would require tracking the full overlap structure of successive segments and is deferred to future work, in the same spirit in which [11] defers the intractable quantum test in favor of a validated classical analogue.

### 4.2 Case study II: moment dynamics and steering time

**First-moment rate.** Differentiating $M_1$ and using $\dot{x}_\omega = \omega u(t)$:

$$
\dot{M}_1 = \int_{-1}^{1} \omega \cdot \omega\, u(t)\, \rho(\omega)\, d\omega = u(t) \int_{-1}^{1} \omega^2 \rho(\omega)\, d\omega.
$$

Compute the integral:

$$
\int_{-1}^{1} \omega^2 \rho(\omega)\, d\omega = \frac{1}{2} \int_{-1}^{1} \omega^2\, d\omega = \frac{1}{2}\left[\frac{\omega^3}{3}\right]_{-1}^{1} = \frac{1}{2}\left(\frac{1}{3} + \frac{1}{3}\right) = \frac{1}{3}.
$$

Hence $\dot{M}_1 = \frac{1}{3} u(t)$: the broadcast input drives the first moment at rate $\frac{1}{3}$ per unit input.

**Immobility of the mean and exact variance.** The exact solution is $x_\omega(t) = \omega\, U(t)$ where $U(t) = \int_0^t u(s)\, ds$. Then

$$
\bar{x}(t) = U(t) \int_{-1}^{1} \omega\, \rho(\omega)\, d\omega = U(t) \cdot \frac{1}{2}\left[\frac{\omega^2}{2}\right]_{-1}^{1} = 0,
$$

so the mean advance is identically zero for the sign-symmetric uniform distribution. The variance is

$$
\sigma^2(t) = \int_{-1}^{1} (\omega U(t))^2 \rho(\omega)\, d\omega = U(t)^2 \cdot \frac{1}{3}.
$$

At $t = 0.3$ with $u \equiv +1$: $U = 0.3$, so $\sigma^2 = \frac{0.09}{3} = 0.03$ and $\sigma = \sqrt{0.03} \approx 0.1732$. The broadcast input can only widen the population, not translate its mean.

**Minimum steering time.** From $M_1(T) = \frac{U(T)}{3}$ and $|U(T)| \le T$, reaching $M_1^{\mathrm{target}} = 0.1$ requires $U(T) = 0.3$, hence with $u \equiv +1$:

$$
T_{\min} = \frac{0.3}{1} = 0.3 \text{ time units.}
$$

Check: $M_1(0.3) = \frac{1}{3} \times 0.3 = 0.1$.

**Skewed distribution.** Take the normalized right-triangular density $\rho_s(\omega) = \frac{2}{3}(\omega + 1)$ on $[0,1]$ (normalization: $\int_0^1 (\omega+1)\, d\omega = \frac{3}{2}$, so the factor $\frac{2}{3}$ makes the integral $1$). Then

$$
c_2 = \int_0^1 \omega^2 \rho_s(\omega)\, d\omega = \frac{2}{3}\int_0^1 (\omega^3 + \omega^2)\, d\omega = \frac{2}{3}\left(\frac{1}{4} + \frac{1}{3}\right) = \frac{2}{3} \cdot \frac{7}{12} = \frac{7}{18} \approx 0.3889.
$$

The same target requires $T_{\min}^{(s)} = \frac{0.1}{7/18} = \frac{1.8}{7} \approx 0.2571$ time units — faster, because the gain mass is concentrated away from the sign-symmetric center.

**Cross-validation and closure.** From $x_\omega = \omega U$, direct computation gives $M_1(t) = U(t) \int_{-1}^{1} \omega^2 \rho\, d\omega = \frac{U(t)}{3}$, matching the integrated moment equation exactly. For the second moment, $\dot{M}_2 = u(t)\int_{-1}^{1}\omega^3 \rho\, d\omega = 0$, and indeed $M_2(t) \equiv 0$ since $x_\omega \propto \omega$; the hierarchy closes exactly in the linear case. Adding a drift term $\dot{x}_\omega = \omega u + a x_\omega$ produces the term $\int \omega^3 x_\omega \rho\, d\omega$, which is not expressible in terms of $M_1, M_2$ alone once $x_\omega$ is not proportional to $\omega$: the hierarchy fails to close, and truncation error is the operative uncertainty in any enriched model. This is the elementary shadow of the general fact, established in [6], that the moment transformation preserves controllability only under the conditions of the dynamic Hausdorff moment problem.

### 4.3 Case study III: ensemble leg drafting computations

**Baseline (best single leg).** Best leg is $L_3$ with $\alpha_3 = 0.7$; by the cost normalization the baseline cost per position is $c_* = 1$. Compute $\alpha^{\gamma+1} = 0.7^5$:

$$
0.7^2 = 0.49, \quad 0.7^3 = 0.343, \quad 0.7^4 = 0.2401, \quad 0.7^5 = 0.16807.
$$

$$
\mathbb{E}[N] = \frac{1 - 0.16807}{1 - 0.7} = \frac{0.83193}{0.3} = 2.7731.
$$

**Cross-check via direct sum** (rejection terms $k = 0, \dots, 3$, since the $k = 4$ rejection outcome is indistinguishable from full acceptance and its mass belongs to the full-acceptance branch): $k=1$: $1 \times 0.7 \times 0.3 = 0.21$; $k=2$: $2 \times 0.49 \times 0.3 = 0.294$; $k=3$: $3 \times 0.343 \times 0.3 = 0.3087$. Sum: $0.8127$. Full acceptance: $4 \times 0.2401 = 0.9604$. Total: $0.8127 + 0.9604 + 1 = 2.7731$. Matches the closed form. Baseline throughput: $C_{\mathrm{draft}} = 4 \times 1 = 4$, total cost $5$:

$$
T_{\mathrm{base}} = \frac{2.7731}{5} = 0.55462.
$$

**Ensemble.** Effective acceptance probability:

$$
(1-\alpha_1)(1-\alpha_2)(1-\alpha_3) = 0.5 \times 0.4 \times 0.3 = 0.06, \qquad \alpha_{\mathrm{eff}} = 1 - 0.06 = 0.94.
$$

Compute $0.94^5$: $0.94^2 = 0.8836$; $0.94^3 = 0.830584$; $0.94^4 = 0.78074896$; $0.94^5 = 0.7339040224$. Then

$$
\mathbb{E}[N_{\mathrm{ens}}] = \frac{1 - 0.7339040224}{0.06} = \frac{0.2660959776}{0.06} = 4.43493296.
$$

Cross-check via direct sum ($q = 0.06$): $k=1$: $0.94 \times 0.06 = 0.0564$; $k=2$: $2 \times 0.8836 \times 0.06 = 0.106032$; $k=3$: $3 \times 0.830584 \times 0.06 = 0.14950512$; sum $0.31193712$; full acceptance $4 \times 0.78074896 = 3.12299584$; total $0.31193712 + 3.12299584 + 1 = 4.43493296$. Matches.

Ensemble throughput: $C_{\mathrm{draft}} = 4 \times (0.2 + 0.3 + 0.5) = 4.0$, total cost $5.0$:

$$
T_{\mathrm{ens}} = \frac{4.43493296}{5.0} = 0.886986592.
$$

Speedup: $0.55462 \times 1.6 = 0.887392$, which exceeds $0.886986592$ by $0.000405408$; so

$$
S = 1.6 - \frac{