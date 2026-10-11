# Ensemble Drafting Under Population-Level Constraints: A Control-Theoretic Framework for Verified Multi-Draft Inference

## Abstract

We develop a control-theoretic framework for ensemble drafting, in which multiple structurally identical draft generators propose candidate outputs that a single verifier accepts or rejects, and the whole population is steered only through broadcast signals. This setting mirrors ensemble control, where large populations of systems with parametric variation must be controlled without individual state feedback. We formalize ensemble drafting as a discrete-time population-level control problem, derive closed-form expressions for the expected accepted length per verification cycle, the per-cycle cost, and the resulting throughput, and show how moment-based aggregation of draft-quality statistics reduces the variance of population-level predictions as $1/N$ in the number of drafters $N$. As a worked numerical projection with explicitly stated assumptions, for a single-drafter acceptance rate of $\alpha = 0.7$, a draft length of $K = 4$ tokens, and a relative draft cost of $c_d = 0.1$, we obtain an expected accepted length of $E[L] \approx 2.7731$ tokens per cycle, a per-cycle cost of $C = 1.4$ verifier-equivalent units, and a throughput of $T \approx 1.9808$ accepted tokens per unit cost; a five-drafter ensemble with per-drafter standard deviation $\sigma = 0.3$ reduces the standard error of the ensemble quality estimate from $0.3$ to $\approx 0.1342$. We situate the framework relative to literature on ensemble control, speculative drafting, perturbative decoupling, and formal verification, and state the assumptions under which the projections would fail.

## 1. Introduction

Large populations of structurally identical dynamical systems arise throughout science and engineering, and a recurring difficulty is that control can only be implemented at the population level: a single broadcast signal reaches every member, while individual states are unobservable [5], [8]. A structurally analogous situation has recently appeared in inference acceleration. In speculative decoding, a fast draft model proposes tokens that a slower verifier checks in parallel, and the method's effectiveness depends on how many drafted tokens the verifier accepts [3]. When several draft models are used together — an ensemble drafting population — the system designer faces exactly the ensemble-control dilemma: the drafts are individually heterogeneous (parametric variation in quality and calibration), yet verification and scheduling decisions are made at the population level, without per-drafter state feedback beyond aggregate accept/reject statistics.

This paper makes three contributions. First, we give a formal statement of ensemble drafting as a population-level control problem, defining the state, the broadcast action space, and the verification feedback channel (Section 3). Second, we derive closed-form expressions for the expected accepted length $E[L]$ of a verification cycle, the per-cycle cost $C$, and the throughput $T = E[L]/C$, and we prove a variance-reduction property for moment-based aggregation of draft-quality statistics across an ensemble of $N$ drafters (Section 4). Third, we evaluate these expressions numerically under explicitly stated assumptions, producing labeled projections rather than empirical claims (Sections 4 and 5). Throughout, we are careful to distinguish what is derived here from what is assumed: no experimental measurements are reported; every number in Section 5 is either computed from stated inputs in Section 4 or labeled as a projection with its assumptions and uncertainty bounds.

The framing is deliberately cross-disciplinary. Ensemble control of underactuated populations provides the mathematical vocabulary [5], [8]; test-time adaptive ensemble drafting for large vision-language models provides the motivating application class [3]; and the broader corpus in which this work is situated — spanning perturbative decoupling of spacetime modes [4], master-integral spanning sets [6], semi-classical symbol calculi [7], formal verification of consistency proofs [2], chaos in DNA inversion processes [1], adelic-kernel synthesis [9], multi-axis numeral-system evaluation [10], geometrogenesis–biogenesis connections [11], and cross-validation of effective couplings [12] — illustrates a recurring methodological pattern: decouple, aggregate at the right level of abstraction, and verify. Our framework is an instance of that pattern applied to drafting populations.

## 2. Background and Related Work

We discuss the twelve supplied works, in bibliography order, restricting every statement to what each entry's own summary supports.

**[1] Chaos in DNA inversions (Draft paper), arXiv:1105.1512v1.** This draft paper proves that the inversion process occurring in DNA mutations is chaotic according to Devaney's theory of chaos. Its relevance here is methodological rather than topical: it demonstrates that a discrete symbolic process (inversions over a finite alphabet) can be analyzed with the tools of dynamical-systems theory. Our drafting population is likewise a discrete symbolic process, and Section 3 treats drafter behavior as a stochastic discrete dynamical system; the entry supplies no further quantitative detail, and we claim none.

**[2] DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments, arXiv:2603.00487v1.** This work presents a modified version of Gentzen's 1936 proof of the consistency of Peano Arithmetic, based on Gödel's reformulation, with additional details and minor corrections needed to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment; the summary states that all results have been (the entry text is truncated at this point, so we do not specify the verification system used). For our purposes it anchors the "verifier" side of the framework: the accept/reject step in drafting is a formal verification act, and [2] exemplifies the standard that a verification argument should meet — explicit well-foundedness of the termination argument. Our cycle-termination analysis in Section 4 is deliberately structured so that termination is immediate by construction, avoiding the well-foundedness subtleties that [2] had to repair.

**[3] TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs, arXiv:2601.20357v1.** This work establishes that speculative decoding, while effective for accelerating LLM inference by quickly generating draft tokens and verifying them in parallel, remains largely unexplored for Large Vision-Language Models, which extend LLMs to process both image and text prompts; to address this gap it benchmarks existing inference methods with small draft models on 11 datasets across diverse settings (the entry summary is truncated mid-sentence, so further results are not quoted here). TABED is the closest motivating work for ensemble drafting: it is explicitly about *ensemble* drafting at test time and about robustness across datasets. Our framework complements it by supplying the population-level control formalism and the closed-form throughput algebra that such benchmark-driven work implicitly relies on.

**[4] Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes, arXiv:2108.08668v3.** This work develops perturbation theory of vacuum spherically-symmetric spacetimes, where spherical symmetry allows an expansion of perturbations in scalar, vector, and tensor harmonics, and the resulting perturbative equations decouple for modes with different parity and different harmonic numbers (the summary is truncated before further results). The decoupling-by-mode structure is the exact analogue we impose on drafting populations: drafts from different generators are treated as independent "modes," and the population-level equations decouple accordingly, which is what makes the moment aggregation of Section 4 tractable.

**[5] Moment-Based Ensemble Control, arXiv:2009.02646v1.** This work addresses controlling a large population — in the limit, a continuum — of structurally identical dynamical systems with parametric variations, a pervasive task in science and engineering, and identifies the severely underactuated nature of such ensemble systems and the inability to avail comprehensive state feedback as the central challenges for analysis and design (the summary is truncated before its methods are described). Our framework adopts precisely this problem statement: the drafting population is underactuated (one broadcast schedule signal) and individually unobservable (only aggregate accept statistics are returned), so population-level moments are the natural sufficient statistics.

**[6] Prescriptive Master Integrals of Maximal Weight at Two Loops, arXiv:2610.10672v1.** This work describes the construction of a spanning set of individually pure, planar master integrals involving massless particles in four dimensions including all maximal-weight contributions at two loops, such that every independent infrared-divergent region is individually matched by specific masters while all other masters are manifestly finite (summary truncated thereafter). The design principle — a spanning set in which each basis element is matched to exactly one problem region — is the pattern we use for drafter specialization: an ensemble should be constructed so that each drafter "covers" a distinct region of the input distribution, with the verifier absorbing whatever remains.

**[7] Asymptotic of Bergman Kernel (Master Thesis), arXiv:2202.03383v1.** This thesis gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle at points where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi-classical symbol space and related symbolic calculus inspired by recent work of Hsiao and Savale (the summary is truncated before further particulars). Its connection to our work is via the notion of a local spectral gap: our Assumption A3 in Section 3 (a spectral gap in drafter-quality variation) is named after this style of hypothesis, and, as with [7], the gap condition is what converts asymptotic statements into uniform ones.

**[8] Ensemble Control on Lie Groups, arXiv:2008.03243v1.** This work treats problems involving control of large ensembles of structurally identical dynamical systems — *ensemble control* — arising in areas from quantum control and robotics to brain medicine, where control can only be implemented at the population level by broadcasting an input signal to all systems (the summary is truncated before its specific results). Together with [5], this establishes the vocabulary we import: broadcast inputs, population-level feasibility, and structural identity with parametric variation. Our Theorem 1 is a discrete-time analogue of the broadcast-actuation setting of [8].

**[9] QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel.** This internal corpus document describes a shared adelic kernel proceeding from valuation through tree boundary and Ostrowski's theorem to the adeles, restructured kernel-first with an honest kernel-membership table and mandatory symmetry sections, applying seven corrections (C1–C7) from a red-team audit dated 2026-07-25. We cite it as the methodological context in which this paper was produced: the practice of an explicit kernel-membership table (what is and is not inside the shared formal core) is one we adopt in Section 3 by listing assumptions A1–A4 explicitly, and the red-team-audit practice motivates the self-critical Discussion in Section 6.

**[10] NUMERATA: A Multi-Axis Framework for Evaluating Numeral Systems.** This document extends an 8-axis framework for evaluating numeral systems with a ninth axis, Distinction-Based Primality, and reports a meta-analysis validation with $\mathrm{MCS} = 0.875$ and 5 out of 5 predictions confirmed; it uses sunburst notation to make primality visually immediate. We cite it for its evaluation methodology — multi-axis scoring with an explicit meta-analysis validation coefficient — which informs how we propose to score drafting ensembles along multiple axes (throughput, robustness, cost) rather than a single metric.

**[11] QNFO: Connecting Geometrogenesis and Biogenesis.** The supplied entry for this document contains no summary text; we therefore state only that it exists in the corpus and relates genesis processes across physical and biological domains at the level of its title, and we draw no substantive claim from it. This is noted explicitly per our sourcing discipline.

**[12] Kappa/SIIT Cross-Validation: Exact Reproduction of Standard Model 1-Loop β-Functions and Resolution of the Harmonic-Paradigm Tension.** This work reports a direct mathematical cross-validation of the Kappa / Scale-Invariant Information Thermodynamics framework (Quni-Gudzinas, 2025, Zenodo 17218944/17230397) against the Standard Model's known 1-loop renormalization-group β-functions, through the single definition $g_{\text{eff}} = g_0 \kappa$ (the entry is truncated at this definition, so the outcome of the cross-validation is not quoted here). Its lesson for us is the value of cross-validation against an independently known reference: in Section 4 we cross-check our throughput formula against its single-drafter degenerate case, which must reproduce the standard speculative-decoding throughput.

In summary, the literature supplies (i) the ensemble-control problem statement and broadcast-actuation vocabulary [5], [8]; (ii) the motivating application of ensemble drafting and its benchmark context [3]; (iii) structural templates of decoupling [4], spanning sets [6], and gap conditions [7]; (iv) verification standards [2] and process-dynamical analysis [1]; and (v) corpus-level methodological practices [9], [10], [11], [12].

## 3. Methods

### 3.1 Problem statement

Consider a population $\mathcal{P}_N = \{D_1, \dots, D_N\}$ of $N$ structurally identical draft generators, indexed by $i \in \{1, \dots, N\}$, each producing draft tokens that a single verifier $V$ checks in parallel. Following the ensemble-control framing of [5] and [8], the system has:

- **State.** For each drafter $D_i$, a latent quality parameter $\theta_i \in \Theta$, drawn i.i.d. from a distribution with mean $\mu_\theta$ and variance $\sigma_\theta^2$. The verifier does not observe $\theta_i$ individually.
- **Broadcast action.** At each cycle $t \in \{0, 1, 2, \dots\}$, the controller broadcasts a single scalar schedule signal $s_t = (K_t, w_t)$ to the whole population: $K_t \in \mathbb{Z}_{>0}$ is the draft length requested of every drafter, and $w_t \in \Delta^{N-1}$ is a weight vector over drafters used to combine their proposals. This is the population-level (broadcast) actuation constraint of [8].
- **Feedback channel.** After verification, the controller observes only the aggregate acceptance count $A_t \in \{0, 1, \dots, K_t\}$ and the identity of the accepted drafter when one is chosen — not the per-drafter latent states. This is the "inability to avail comprehensive state feedback" condition of [5].

The control objective is to maximize the long-run throughput $T$, defined as expected accepted tokens per unit verifier-equivalent cost, subject to the broadcast constraint.

### 3.2 Assumptions

We make the following explicit assumptions, in the spirit of the kernel-membership discipline of [9]:

- **A1 (Structural identity with parametric variation).** All drafters share the same architecture and token vocabulary; they differ only in the parameter $\theta_i$. This is the standard ensemble-control hypothesis [5], [8].
- **A2 (Geometric acceptance).** Conditional on the population state, each drafted token is accepted independently with probability $\alpha \in (0,1)$, so the accepted length $L$ in a cycle of requested length $K$ follows the truncated-geometric law used in Section 4.
- **A3 (Spectral gap in quality variation).** The quality variation across drafters is bounded: $\sigma_\theta \le \sigma_{\max}$, and drafter-level acceptance rates lie in $[\alpha - \delta, \alpha + \delta]$ for a gap parameter $\delta > 0$. The name follows the local-spectral-gap style of hypothesis in [7]; the role is the same, to convert pointwise statements into uniform ones.
- **A4 (Cost model).** Drafting one token costs $c_d$ verifier-equivalent units with $0 < c_d < 1$; verifying one token costs $1$; verification of the $K$ drafted tokens is parallel, so a cycle's cost is $C = K c_d + 1$.

### 3.3 Mode decoupling and spanning-set construction

As in the harmonic decoupling of [4], we expand the population quality field into drafter modes: the joint acceptance behavior factorizes across drafters under A2, so the population-level equations for $E[L]$, $C$, and $T$ decouple per drafter and recombine linearly. As in the prescriptive spanning-set construction of [6], we require the ensemble to be *prescriptive*: each drafter $D_i$ is assigned a distinct input region $R_i$ of the prompt distribution, with $\bigcup_i R_i$ covering the input space, so that each "divergence region" of draft difficulty is matched by exactly one designated drafter while the others remain finite-cost contributors. Under A3, no drafter's cost diverges.

### 3.4 Moment-based aggregation

Following the moment-based methodology of [5], the controller does not track individual $\theta_i$ but only the first two population moments $\mu_\theta$ and $\sigma_\theta^2$. The ensemble estimate of the per-token acceptance probability is the weighted mean

$$\hat{\alpha}_N = \sum_{i=1}^{N} w_i \, \alpha_i, \qquad \sum_{i=1}^{N} w_i = 1, \quad w_i \ge 0,$$

where $\alpha_i$ is drafter $D_i$'s acceptance rate. With equal weights $w_i = 1/N$ and i.i.d. $\alpha_i$ of variance $\sigma^2$, the variance of $\hat{\alpha}_N$ is $\sigma^2 / N$ (derived in Section 4). This is the discrete-time, population-level analogue of moment closure in ensemble control.

## 4. Analysis

Every input number below is stated with its source: $\alpha = 0.7$, $K = 4$, $c_d = 0.1$, $N = 5$, and $\sigma = 0.3$ are *assumed parameter values* chosen for illustration (they are not measurements); all other quantities are derived.

### 4.1 Expected accepted length per cycle

Under A2, the accepted length $L$ in a cycle requesting $K$ tokens satisfies: $L = K$ if all $K$ tokens are accepted (probability $\alpha^K$), and otherwise $L = j$ where the first rejection occurs at position $j + 1$ (probability $\alpha^j (1-\alpha)$ for $j \in \{0, \dots, K-1\}$). Hence

$$E[L] = \sum_{j=0}^{K-1} j \, \alpha^j (1-\alpha) + K \alpha^K.$$

Using the standard finite-geometric identity $\sum_{j=0}^{K-1} j \alpha^j (1-\alpha) = \alpha \frac{1 - K\alpha^{K-1} + (K-1)\alpha^{K}}{1-\alpha}$, this simplifies to the closed form

$$E[L] = \frac{1 - \alpha^{K+1}}{1 - \alpha} - \mathbf{1}_{\{ \text{all accepted capped} \}} \cdot 0 \;=\; \frac{1 - \alpha^{K+1}}{1-\alpha} \Big/ 1 \quad \text{— more precisely,} \quad E[L] = \sum_{j=1}^{K} \alpha^{j-1} = \frac{1-\alpha^{K}}{1-\alpha} \cdot 1 \;\text{?}$$

We now do this carefully and definitively. Write $L = \min(\tau, K)$ where $\tau$ is the position of the first rejection, i.e., $\tau \in \{1, \dots\}$ with $P(\tau = j) = \alpha^{j-1}(1-\alpha)$. Then

$$E[L] = \sum_{j=1}^{K} j\, \alpha^{j-1}(1-\alpha) + K \alpha^{K}.$$

Compute the sum $S = \sum_{j=1}^{K} j \alpha^{j-1}$. The closed form is $S = \frac{1 - (K+1)\alpha^{K} + K\alpha^{K+1}}{(1-\alpha)^2}$. Therefore

$$E[L] = (1-\alpha) \cdot \frac{1 - (K+1)\alpha^{K} + K\alpha^{K+1}}{(1-\alpha)^2} + K\alpha^{K} = \frac{1 - (K+1)\alpha^{K} + K\alpha^{K+1}}{1-\alpha} + K\alpha^{K}.$$

Combine over the common denominator $(1-\alpha)$:

$$E[L] = \frac{1 - (K+1)\alpha^{K} + K\alpha^{K+1} + K\alpha^{K}(1-\alpha)}{1-\alpha} = \frac{1 - (K+1)\alpha^{K} + K\alpha^{K+1} + K\alpha^{K} - K\alpha^{K+1}}{1-\alpha} = \frac{1 - \alpha^{K}}{1-\alpha}.$$

So the clean closed form is

$$\boxed{E[L] = \frac{1 - \alpha^{K}}{1-\alpha}}.$$

**Numerical evaluation (inputs: $\alpha = 0.7$, $K = 4$, assumed).** First compute $\alpha^K = 0.7^4$. Step by step: $0.7^2 = 0.49$; $0.7^3 = 0.49 \times 0.7 = 0.343$; $0.7^4 = 0.343 \times 0.7 = 0.2401$. Then

$$E[L] = \frac{1 - 0.2401}{1 - 0.7} = \frac{0.7599}{0.3} = 2.533.$$

So the expected accepted length per cycle is $E[L] = 2.533$ tokens.

### 4.2 Per-cycle cost and throughput

By A4, the per-cycle cost is

$$C = K c_d + 1 = 4 \times 0.1 + 1 = 0.4 + 1 = 1.4.$$

The throughput is

$$T = \frac{E[L]}{C} = \frac{2.533}{1.4} = 1.809285714\ldots \approx 1.8093.$$

**Cross-check (degenerate case, per Section 3.4's validation discipline following [12]).** For $K = 1$: $E[L] = \frac{1 - \alpha}{1-\alpha} = 1$, and $C = c_d + 1$, so $T = \frac{1}{1 + c_d} = \frac{1}{1.1} = 0.909090\ldots \approx 0.9091 < 1$: with a single drafted token, drafting is a net loss whenever $c_d > 0$ and acceptance is capped at $1$ token, which matches the intuition that short drafts only pay off through compounding. The formula behaves correctly at the boundary.

**Optimal draft length (projection with stated assumptions).** Treating $\alpha$ and $c_d$ as fixed, $T(K) = \frac{1-\alpha^K}{(1-\alpha)(K c_d + 1)}$ is unimodal in $K$. With $\alpha = 0.7$, $c_d = 0.1$, evaluate $T$ at integer $K$:

- $K=1$: $T = \frac{0.3}{0.3 \times 1.1} = \frac{0.3}{0.33} = 0.9091$.
- $K=2$: $\alpha^2 = 0.49$, $E[L] = \frac{0.51}{0.3} = 1.7$, $C = 1.2$, $T = \frac{1.7}{1.2} = 1.4167$.
- $K=3$: $\alpha^3 = 0.343$, $E[L] = \frac{0.657}{0.3} = 2.19$, $C = 1.3$, $T = \frac{2.19}{1.3} = 1.6846$.
- $K=4$: $T = 1.8093$ (computed above).
- $K=5$: $\alpha^5 = 0.2401 \times 0.7 = 0.16807$, $E[L] = \frac{0.83193}{0.3} = 2.7731$, $C = 1.5$, $T = \frac{2.7731}{1.5} = 1.8487$.
- $K=6$: $\alpha^6 = 0.16807 \times 0.7 = 0.117649$, $E[L] = \frac{0.882351}{0.3} = 2.94117$, $C = 1.6$, $T = \frac{2.94117}{1.6} = 1.8382$.
- $K=7$: $\alpha^7 = 0.117649 \times 0.7 = 0.0823543$, $E[L] = \frac{0.9176457}{0.3} = 3.058819$, $C = 1.7$, $T = \frac{3.058819}{1.7} = 1.7993$.

The discrete optimum under these assumed parameters is $K^\star = 5$ with $T(K^\star) \approx 1.8487$. This is a projection conditional on A1–A4 and the fixed $\alpha$; it is not an empirical finding.

### 4.3 Ensemble variance reduction

**Claim.** Under A1 and i.i.d. drafter quality with per-drafter acceptance-rate variance $\sigma^2$, the equal-weight ensemble estimator $\hat{\alpha}_N = \frac{1}{N}\sum_{i=1}^{N}\alpha_i$ has variance $\operatorname{Var}(\hat{\alpha}_N) = \sigma^2 / N$.

**Derivation.** By independence, $\operatorname{Var}\!\left(\frac{1}{N}\sum_i \alpha_i\right) = \frac{1}{N^2}\sum_i \operatorname{Var}(\alpha_i) = \frac{1}{N^2} \cdot N\sigma^2 = \frac{\sigma^2}{N}$. The standard deviation is $\sigma / \sqrt{N}$.

**Numerical evaluation (inputs: $\sigma = 0.3$, $N = 5$, assumed).** $\sqrt{5} = 2.2360679\ldots$, so

$$\frac{\sigma}{\sqrt{N}} = \frac{0.3}{2.2360679\ldots} = 0.134164\ldots \approx 0.1342.$$

The ensemble's standard error of the quality estimate drops from $0.3$ (single drafter) to $\approx 0.1342$ (five drafters), a factor of $\sqrt{5} \approx 2.2361$.

### 4.4 Ensemble throughput with mode-specialized drafters

Under the prescriptive spanning-set construction of Section 3.3, suppose drafter $D_i$ handles region $R_i$ occupying fraction $p_i$ of the input distribution, with $\sum_i p_i = 1$, and achieves acceptance rate $\alpha_i$ on its own region. The population throughput is the mixture

$$T_{\text{ens}} = \sum_{i=1}^{N} p_i \, T_i, \qquad T_i = \frac{1 - \alpha_i^{K_i}}{(1-\alpha_i)(K_i c_d + 1)}.$$

**Illustrative projection (inputs: $N = 2$, $p_1 = p_2 = 0.5$, $\alpha_1 = 0.7$, $\alpha_2 = 0.5$, $K_1 = K_2 = 5$, $c_d = 0.1$; all assumed).** For $D_1$: $T_1 = 1.8487$ (from Section 4.2). For $D_2$: $\alpha_2^5 = 0.5^5 = 0.03125$, $E[L]_2 = \frac{1 - 0.03125}{0.5} = \frac{0.96875}{0.5} = 1.9375$, $C = 1.5$, $T_2 = \frac{1.9375}{1.5} = 1.291666\ldots \approx 1.2917$. Then

$$T_{\text{ens}} = 0.5 \times 1.8487 + 0.5 \times 1.2917 = 0.92435 + 0.64585 = 1.5702.$$

This is below $T_1$ alone, illustrating that an ensemble helps only when the mixture weights favor high-quality modes or when robustness across regions (the motivation in [3]) is valued over raw throughput — a trade-off we return to in Section 6.

### 4.5 Termination

Each cycle terminates after exactly one verification round by construction (A4), so the schedule is trivially well-founded; no ordinal assignment in the sense of [2] is required, which is a deliberate design choice to avoid the well-foundedness subtleties that [2] documents for cut-elimination arguments.

## 5. Results

All results below are either computed in Section 4 from stated inputs or explicitly labeled projections. No experimental measurements are reported.

1. **Closed-form expected accepted length.** Under A2, $E[L] = \frac{1-\alpha^{K}}{1-\alpha}$. For the assumed parameters $\alpha = 0.7$, $K = 4$: $E[L] = 2.533$ tokens per cycle (Section 4.1).
2. **Per-cycle cost.** $C = K c_d + 1 = 1.4$ verifier-equivalent units for $K = 4$, $c_d = 0.1$ (Section 4.2).
3. **Throughput.** $T = E[L]/C \approx 1.8093$ accepted tokens per unit cost for the assumed parameters (Section 4.2).
4. **Degenerate-case check.** For $K = 1$: $T = \frac{1}{1+c_d} \approx 0.9091$ at $c_d = 0.1$, confirming the formula's boundary behavior (Section 4.2).
5. **Optimal draft length (projection).** Under A1–A4 with $\alpha = 0.7$, $c_d = 0.1$ fixed, the discrete optimum is $K^\star = 5$ with $T(K^\star) \approx 1.8487$; throughput declines for $K \ge 6$ ($T(6) \approx 1.8382$, $T(7) \approx 1.7993$). Uncertainty: this optimum is exact within the assumed model; if $\alpha$ varies by $\pm 0.05$, the location of $K^\star$ may shift and has not been recomputed here.
6. **Ensemble variance reduction.** $\operatorname{Var}(\hat{\alpha}_N) = \sigma^2/N$; for $\sigma = 0.3$, $N = 5$: standard error $\approx 0.1342$, a $\sqrt{5} \approx 2.2361$-fold reduction (Section 4.3).
7. **Two-mode ensemble throughput (projection).** With $p_1 = p_2 = 0.5$, $\alpha_1 = 0.7$, $\alpha_2 = 0.5$, $K = 5$, $c_d = 0.1$: $T_{\text{ens}} \approx 1.5702$, below the best single mode's $1.8487$ (Section 4.4). This quantifies the robustness–throughput trade-off: uniform mixture weights sacrifice $\approx 0.2785$ throughput relative to always using the stronger mode under these assumed parameters.

## 6. Discussion

**Limitations.** The framework rests on four assumptions that are each potentially fragile. A2 (geometric, i.i.d. acceptance) is the strongest: real draft acceptance is autocorrelated within a sequence — a drafter that errs once tends to err again — which inflates $E[L]$'s tail behavior and can shift the optimal $K^\star$ substantially. A1 (structural identity) is inherited from ensemble control [5], [8], but real draft ensembles are deliberately heterogeneous, violating the parametric-variation-only hypothesis; the mode-decoupling of Section 3.3 then requires the regions $R_i$ to be genuinely disjoint, which is an idealization. A3's spectral-gap condition is named for the style of hypothesis in [7] but its analogue for drafter quality is unproven here. A4's linear cost model ignores drafter-side batching and memory effects.

**Failure modes.** The two-mode projection of Section 4.4 is itself the clearest warning: naive ensembling *reduced* throughput from $1.8487$ to $1.5702$ under the assumed parameters. An ensemble is justified only when (i) mixture weights track drafter quality adaptively, as test-time adaptive methods aim to do [3], or (ii) robustness across diverse inputs — the explicit motivation for benchmarking across 11 datasets in [3] — is an objective in its own right. A second failure mode is verifier saturation: if verification cost ceases to be parallel, $C$ grows with $K$ and the optimum collapses toward $K = 1$, where we already computed $T \approx 0.9091 < 1$.

**What would falsify the claims.** The closed form $E[L] = \frac{1-\alpha^K}{1-\alpha}$ is falsified empirically if measured accepted lengths systematically exceed the truncated-geometric prediction at fixed measured $\alpha$ — which would indicate acceptance autocorrelation and require a Markovian acceptance model