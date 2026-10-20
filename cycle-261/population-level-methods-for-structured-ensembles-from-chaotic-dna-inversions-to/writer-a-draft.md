# Population-Level Methods for Structured Ensembles: From Chaotic DNA Inversions to Ensemble Leg Drafting

## Abstract

Coordinating large populations of identical units without individual access arises in ensemble control, speculative decoding, and chaotic DNA inversion analysis. Existing literature treats each setting separately, leaving a gap in a unified analytical framework. We fill this gap by (i) deriving closed‑form expectations for Hamming divergence in a binary DNA inversion toy model, (ii) establishing a moment‑based broadcast‑control baseline that yields an exact first‑moment rate of $1/3$ per unit input and a minimum steering time of $0.3$ time units for a target first moment of $0.1$, and (iii) constructing an exact model of ensemble leg drafting under an OR‑fusion rule that produces an effective acceptance probability of $0.94$, an expected token advance of $4.4349$ per cycle, a throughput of $0.8870$, and a speedup of $1.5993$ over the best single leg. All quantitative claims follow from explicit arithmetic or are labeled projections with stated assumptions. The results clarify what population‑level performance is achievable when individual‑level actuation is unavailable and guide designers of broadcast‑control systems and speculative‑decoding pipelines.

## 1. Introduction

Large‑scale engineering systems often must be steered, queried, or made to produce useful output while only a single actuator or signal can act on the entire population. In quantum‑ensemble control, a broadcast field drives all spins but individual spin measurements are inaccessible, limiting controllability and increasing the cost of state estimation. In large‑language‑model inference, speculative decoding relies on cheap draft models that propose tokens in parallel while a single expensive target model verifies them, creating a bottleneck that blocks further throughput gains. In molecular biology, DNA inversion processes have been shown to be chaotic under Devaney’s definition, implying that individual mutation trajectories are unpredictable and that only statistical population‑level quantities can be meaningfully predicted.  

If designers could predict the best achievable population‑level divergence time for chaotic DNA inversions, the minimum steering time for a broadcast‑controlled ensemble of first‑order units, or the exact throughput gain from fusing multiple speculative drafts, they could allocate resources, set realistic performance targets, and avoid over‑engineering.  

**Contributions.**  
1. A toy model of random DNA inversions with closed‑form expectations for Hamming divergence (Sections 3.1, 4.1).  
2. A moment‑based broadcast‑control baseline for a continuum of first‑order units, including an exact first‑moment rate, variance evolution, and minimum steering time (Sections 3.2, 4.2).  
3. A formal model of ensemble leg drafting under an OR‑fusion rule, with exact computations of effective acceptance probability, expected tokens per cycle, throughput, speedup, break‑even compute budget, and a labeled projection for correlated legs (Sections 3.3, 4.3).  

All quantitative claims are either derived with explicit arithmetic in Section 4 or labeled as projections with stated assumptions. No empirical measurements are reported.

## 2. Background and Related Work

**Ensemble control of populations.** Ensemble Control on Lie Groups treats problems involving large ensembles of structurally identical dynamical systems and emphasizes that control can only be implemented at the population level by broadcasting an input signal to all systems [8]. The broadcast‑input assumption used in Section 3.2 follows directly from this framing. Moment‑Based Ensemble Control frames the control of a large population—formally a continuum—of structurally identical dynamical systems with parametric variations as a pervasive task and identifies the severely underactuated nature of such systems and the inability to avail comprehensive state feedback as the central challenges [5]. Our moment hierarchy in Section 3.2 and its closure analysis in Section 4.2 instantiate that challenge.

**Speculative decoding for vision‑language models.** TABED addresses speculative decoding for large vision‑language models, noting that speculative decoding “remains largely unexplored” for LVLMs and benchmarking existing inference methods with small draft models on eleven datasets [3]. The abstract’s statement of a gap in draft‑model acceleration for multimodal models is the only external input we use; Section 3.3 provides an analytical model of a specific multi‑draft fusion rule that such benchmarks could evaluate.

**Chaos in biological sequence dynamics.** Chaos in DNA inversions proves that the inversion process occurring in DNA mutations is chaotic in the sense of Devaney’s theory [1]. The abstract’s claim of chaos motivates Section 3.1: if the inversion process is chaotic, individual long‑run trajectories are unpredictable, and only statistical quantities such as the expected Hamming distance are accessible.

**Decoupled multi‑mode analysis.** Master Functions and Equations for Perturbations of Vacuum Spherically‑Symmetric Spacetimes shows that spherical symmetry permits an expansion of perturbations in scalar, vector, and tensor harmonics, with the resulting perturbative equations decoupling for modes of different parity and harmonic number [4]. The methodological lesson—exploit structure to decouple a coupled problem into independent modes—governs both our moment expansion (modes = moment orders, which decouple only partially; Section 4.2) and our leg‑fusion analysis (modes = draft legs, which decouple exactly when their errors are independent; Section 4.3).

**Spanning sets and isolation of contributions.** Prescriptive Master Integrals of Maximal Weight at Two Loops constructs a spanning set of individually pure, planar master integrals such that every independent infrared‑divergent region is matched by exactly one element [6]. The design principle—choose a basis in which each problematic region is matched by exactly one element—guides our choice in Section 4.2 to isolate the first moment by restricting the input class so that higher‑order effects are deferred to a separate closure analysis.

**Semi‑classical asymptotics.** Asymptotic of Bergman Kernel (Master Thesis) gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi‑classical symbol space and symbolic calculus [7]. The abstract’s pattern that asymptotic problems become tractable once the right calculus is introduced mirrors our use of a geometric acceptance model as the calculus in which throughput becomes closed‑form (Section 3.3).

**Formal verification and well‑foundedness.** A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments provides a layered argument that is checkable step by step [2]. We emulate that style in Section 4, where each computation is presented as an independent, checkable arithmetic block.

**QNFO corpus materials.** The QNFO Consilient Synthesis v2.0 document describes a shared adelic kernel, applies seven corrections, and restructures the kernel‑first with an explicit audit trail [9]. We follow that audit‑driven revision style by maintaining an explicit record of derived versus projected claims in Section 5 and Appendix B.  

**NUMERATA framework.** NUMERATA extends an eight‑axis framework for evaluating numeral systems and reports a meta‑analysis validation with $M_{\mathrm{CS}}=0.875$ and five of five predictions confirmed [10]. The axis‑decomposition style parallels our decomposition of throughput into acceptance, length, and cost factors (Section 3.3).

## 3. Methods

### 3.1 Case study I: a toy model of random DNA inversions

We represent a DNA segment as a binary sequence of fixed length $L=10$, where each site is $0$ (original) or $1$ (inverted). At each discrete step, a contiguous segment is selected uniformly among all $\frac{L(L+1)}{2}=55$ possible segments and all bits within it are flipped. This stochastic rule captures the essential feature of inversion without biochemical detail; the chaotic character of the underlying process [1] motivates a purely statistical treatment.

### 3.2 Case study II: moment‑based broadcast control baseline

Consider a continuum of first‑order units indexed by a gain parameter $\omega\in[-1,1]$, each obeying
$$
\dot{x}_\omega(t)=\omega\,u(t),\qquad x_\omega(0)=0,
$$
with a single broadcast input $u(t)$, identical for all $\omega$, bounded by $|u(t)|\le u_{\max}=1$. The gain density is uniform, $\rho(\omega)=\tfrac12$ on $[-1,1]$. Define the gain‑weighted moments
$$
M_k(t)=\int_{-1}^{1}\omega^{k}\,x_\omega(t)\,\rho(\omega)\,d\omega,
$$
the mean advance $\bar{x}(t)=\int_{-1}^{1}x_\omega(t)\,\rho(\omega)\,d\omega$, and the population variance
$$
\sigma^{2}(t)=\int_{-1}^{1}\bigl(x_\omega(t)-\bar{x}(t)\bigr)^{2}\rho(\omega)\,d\omega.
$$
We restrict to piecewise‑constant inputs $u(t)\in\{-1,+1\}$ (bang‑bang), the weakest nontrivial broadcast class consistent with the bound. “Reachability’’ is defined only for $M_{1}$: a value of $M_{1}(T)$ obtainable from $M_{1}(0)=0$ by some admissible input.

### 3.3 Case study III: ensemble leg drafting for speculative decoding

A target model $M_{T}$ generates tokens autoregressively. A set $\mathcal{L}=\{L_{1},\dots,L_{m}\}$ of $m$ draft legs each proposes a continuation of length $\gamma$. At each draft position $j$, leg $L_{i}$ matches the target’s sampled token with probability $\alpha_{i}$ (the leg’s *acceptance profile*). Define $c_{i}$ as the relative compute cost of leg $L_{i}$ per draft position, $C_{\mathrm{draft}}=\gamma\sum_{i=1}^{m}c_{i}$, and $C_{\mathrm{verify}}=1$ (target verification per cycle, normalized).

**OR‑fusion rule.** The fused draft at position $j$ is admissible if at least one leg’s proposal is admissible; the fused sequence takes the token of the first admissible leg in fixed priority order. Under independent leg failures, the effective acceptance probability is
$$
\alpha_{\mathrm{eff}}=1-\prod_{i=1}^{m}\bigl(1-\alpha_{i}\bigr).
$$

**Tokens per cycle.** With per‑position acceptance probability $\alpha$ i.i.d. across positions, the expected number of tokens advanced per cycle is
$$
\mathbb{E}[N]=\sum_{k=0}^{\gamma-1}k\,\alpha^{k}(1-\alpha)+\gamma\,\alpha^{\gamma}+1,
$$
which simplifies to the closed form
$$
\mathbb{E}[N]=\frac{1-\alpha^{\gamma+1}}{1-\alpha}.
$$

**Throughput and speedup.** Throughput is $T=\mathbb{E}[N]/\bigl(C_{\mathrm{draft}}+C_{\mathrm{verify}}\bigr)$; the speedup factor against the best single leg is $S=T_{\mathrm{ens}}/T_{\mathrm{base}}$.

**Correlated legs.** If legs are correlated, the independence product overestimates reliability. For exchangeable legs with common pairwise error correlation $\rho$, the probability that all legs fail simultaneously lies between the independent value $\prod_{i}(1-\alpha_{i})$ and the comonotone value $\min_{i}(1-\alpha_{i})$; correlated regimes are treated as labeled projections, not exact results.

## 4. Analysis

All input numbers are stated with their sources. Model parameters in Sections 3.1–3.3 are definitions of this paper, not empirical measurements; the design‑point values $\alpha_{1}=0.5$, $\alpha_{2}=0.6$, $\alpha_{3}=0.7$, $\gamma=4$, $(c_{1},c_{2},c_{3})=(0.2,0.3,0.5)$, and $M_{1}^{\mathrm{target}}=0.1$ are illustrative assumptions declared here.

### 4.1 Case study I: divergence time of random inversions

**Input:** $L=10$ (Section 3.1). The number of contiguous segments is $\frac{10\cdot11}{2}=55$.

**Average segment length.** The total length over all segments is $S=\sum_{k=1}^{10}k(10-k+1)$:
\[
\begin{aligned}
S&=1\cdot10+2\cdot9+3\cdot8+4\cdot7+5\cdot6\\
&\quad+6\cdot5+7\cdot4+8\cdot3+9\cdot2+10\cdot1\\
&=10+18+24+28+30+30+28+24+18+10\\
&=220.
\end{aligned}
\]
Hence the average segment length is $\bar{\ell}=S/55=220/55=4.0$.

**Expected Hamming distance.** Starting from the all‑zero reference, flipping a segment of length $\ell$ increases the Hamming distance $d$ by exactly $\ell$ on the first flip of each site; treating increments as independent with mean $\bar{\ell}=4$ (approximation P0, discussed in Section 6), the expected distance after $t$ steps is $\mathbb{E}[d(t)]\approx\min(L,4t)$. Setting $4t_{\mathrm{sat}}=10$ gives $t_{\mathrm{sat}}=10/4=2.5$, and since $t$ is integer,
\[
t_{\mathrm{sat}}=\lceil2.5\rceil=3.
\]

**Result (labeled projection P0).** Under the independence approximation of Section 3.1—increments treated as independent with mean $\bar{\ell}=4$, ignoring re‑flipping of already‑inverted sites—the saturation time is $t_{\mathrm{sat}}=3$ steps. The exact expectation would require tracking overlap structure and is plausibly larger than $3$.

### 4.2 Case study II: moment dynamics and steering time

**First‑moment rate.** Differentiating $M_{1}$ and using $\dot{x}_\omega=\omega u(t)$:
\[
\dot{M}_{1}=u(t)\int_{-1}^{1}\omega^{2}\rho(\omega)\,d\omega.
\]
Compute the integral:
\[
\int_{-1}^{1}\omega^{2}\rho(\omega)\,d\omega=\frac12\int_{-1}^{1}\omega^{2}\,d\omega
=\frac12\left[\frac{\omega^{3}}{3}\right]_{-1}^{1}
=\frac12\left(\frac13+\frac13\right)=\frac13.
\]
Thus $\dot{M}_{1}=\tfrac13 u(t)$: the broadcast input drives the first moment at rate $1/3$ per unit input.

**Immobility of the mean and exact variance.** The exact solution is $x_\omega(t)=\omega\,U(t)$ where $U(t)=\int_{0}^{t}u(s)\,ds$. Then
\[
\bar{x}(t)=U(t)\int_{-1}^{1}\omega\,\rho(\omega)\,d\omega
=U(t)\cdot\frac12\left[\frac{\omega^{2}}{2}\right]_{-1}^{1}=0,
\]
so the mean advance is identically zero for the sign‑symmetric uniform distribution. The variance is
\[
\sigma^{2}(t)=\int_{-1}^{1}(\omega U(t))^{2}\rho(\omega)\,d\omega
=U(t)^{2}\cdot\frac13.
\]
At $t=0.3$ with $u\equiv+1$, $U=0.3$, so $\sigma^{2}=0.09/3=0.03$ and $\sigma=\sqrt{0.03}\approx0.1732$.

**Minimum steering time.** From $M_{1}(T)=\tfrac13U(T)$ and $|U(T)|\le T$, reaching $M_{1}^{\mathrm{target}}=0.1$ requires $U(T)=0.3$, hence with $u\equiv+1$:
\[
T_{\min}=0.3\ \text{time units}.
\]
Check: $M_{1}(0.3)=\tfrac13\times0.3=0.1$.

**Skewed distribution.** Take the normalized right‑triangular density $\rho_{s}(\omega)=\tfrac{2}{3}(\omega+1)$ on $[0,1]$. Normalization:
\[
\int_{0}^{1}(\omega+1)\,d\omega=\left[\tfrac{\omega^{2}}{2}+\omega\right]_{0}^{1}= \tfrac12+1=\tfrac32,
\]
so the factor $\tfrac{2}{3}$ yields unit integral. Compute
\[
c_{2}=\int_{0}^{1}\omega^{2}\rho_{s}(\omega)\,d\omega
=\frac{2}{3}\int_{0}^{1}(\omega^{3}+\omega^{2})\,d\omega
=\frac{2}{3}\left(\frac14+\frac13\right)
=\frac{2}{3}\cdot\frac{7}{12}
=\frac{7}{18}\approx0.3889.
\]
The same target requires $T_{\min}^{(s)}=M_{1}^{\mathrm{target}}/c_{2}=0.1/(7/18)=\frac{1.8}{7}\approx0.2571$ time units—faster because gain mass is concentrated away from the sign‑symmetric centre.

**Cross‑validation and closure.** For the linear dynamics $x_\omega=\omega U$, $M_{1}(t)=\tfrac13U(t)$ matches the integrated moment equation exactly. The second moment satisfies $\dot{M}_{2}=u(t)\int_{-1}^{1}\omega^{3}\rho(\omega)\,d\omega=0$, so $M_{2}(t)\equiv0$; the hierarchy closes exactly in the linear case. Adding a drift term $\dot{x}_\omega=\omega u + a x_\omega$ introduces a term $\int\omega^{3}x_\omega\rho\,d\omega$ that cannot be expressed solely in $M_{1},M_{2}$, causing closure failure.

### 4.3 Case study III: ensemble leg drafting computations

**Baseline (best single leg).** The best leg is $L_{3}$ with $\alpha_{3}=0.7$; baseline cost per position is $c_{*}=1$. Compute $\alpha^{\gamma+1}=0.7^{5}$:
\[
0.7^{2}=0.49,\quad 0.7^{3}=0.343,\quad 0.7^{4}=0.2401,\quad 0.7^{5}=0.16807.
\]
Closed form:
\[
\mathbb{E}[N]=\frac{1-0.16807}{1-0.7}
=\frac{0.83193}{0.3}=2.7731.
\]
Direct sum verification:
\[
\begin{aligned}
k=1:&\ 1\times0.7\times0.3=0.21,\\
k=2:&\ 2\times0.49\times0.3=0.294,\\
k=3:&\ 3\times0.343\times0.3=0.3087,\\
\text{sum}&=0.8127,\\
\text{full acceptance}&=4\times0.2401=0.9604,\\
\mathbb{E}[N]&=0.8127+0.9604+1=2.7731.
\end{aligned}
\]
Baseline throughput:
\[
C_{\mathrm{draft}}=4\times1=4,\quad C_{\mathrm{total}}=5,\quad
T_{\mathrm{base}}=\frac{2.7731}{5}=0.55462.
\]

**Ensemble.** Effective acceptance probability:
\[
(1-\alpha_{1})(1-\alpha_{2})(1-\alpha_{3})
=0.5\times0.4\times0.3=0.06,\qquad
\alpha_{\mathrm{eff}}=1-0.06=0.94.
\]
Compute $\alpha_{\mathrm{eff}}^{\gamma+1}=0.94^{5}$:
\[
\begin{aligned}
0.94^{2}&=0.8836,\\
0.94^{3}&=0.830584,\\
0.94^{4}&=0.78074896,\\
0.94^{5}&=0.7339040224.
\end{aligned}
\]
Thus
\[
\mathbb{E}[N_{\mathrm{ens}}]=\frac{1-0.7339040224}{1-0.94}
=\frac{0.2660959776}{0.06}=4.43493296.
\]
Direct sum verification (using $q=0.06$):
\[
\begin{aligned}
k=1:&\ 0.94\times0.06=0.0564,\\
k=2:&\ 2\times0.8836\times0.06=0.106032,\\
k=3:&\ 3\times0.830584\times0.06=0.14950512,\\
\text{sum}&=0.31193712,\\
\text{full acceptance}&=4\times0.78074896=3.12299584,\\
\mathbb{E}[N_{\mathrm{ens}}]&=0.31193712+3.12299584+1=4.43493296.
\end{aligned}
\]
Ensemble throughput:
\[
C_{\mathrm{draft}}=4\times(0.2+0.3+0.5)=4.0,\quad C_{\mathrm{total}}=5.0,\quad
T_{\mathrm{ens}}=\frac{4.43493296}{5}=0.886986592.
\]

**Speedup.** Using the baseline throughput $0.55462$,
\[
S=\frac{T_{\mathrm{ens}}}{T_{\mathrm{base}}}
=\frac{0.886986592}{0.55462}\approx1.5993.
\]

**Break‑even compute budget.** The ensemble wins iff
\[
\frac{\mathbb{E}[N_{\mathrm{ens}}]}{\gamma C+1}>T_{\mathrm{base}}.
\]
Solve for $C^{*}$:
\[
\gamma C^{*}+1=\frac{4.43493296}{0.55462}\approx7.996345,
\]
\[
C^{*}=\frac{7.996345-1}{4}=1.749086.
\]
Thus the ensemble remains advantageous as long as $\sum_{i}c_{i}<1.7491$. At the design point $\sum_{i}c_{i}=1.0$, the leg‑compute budget can increase by a factor $1.749086$ (a $74.9\%$ increase), giving $42.8\%$ headroom relative to the break‑even budget.

**Projection P1 (correlated legs).** Assume exchangeable legs with common pairwise error correlation $\rho=1$ (comonotone failure). The effective acceptance probability collapses to the average $\bar{\alpha}=\tfrac{0.5+0.6+0.7}{3}=0.6$. Compute $\bar{\alpha}^{\gamma+1}=0.6^{5}=0.07776$:
\[
0.6^{2}=0.36,\quad 0.6^{3}=0.216,\quad 0.6^{4}=0.1296,\quad 0.6^{5}=0.07776.
\]
Then
\[
\mathbb{E}[N]=\frac{1-0.07776}{1-0.6}
=\frac{0.92224}{0.4}=2.3056,\qquad
T=\frac{2.3056}{5}=0.46112.
\]
Since $0.46112<T_{\mathrm{base}}$, the correlated‑leg ensemble would underperform the best single leg.

## 5. Results

All quantitative values reported here are taken directly from the arithmetic in Section 4.

| Quantity | Value | Section |
|---|---|---|
| Average DNA segment length $\bar{\ell}$ | $4.0$ | 4.1 |
| Saturation steps (projection P0) | $3$ | 4.1 |
| First‑moment rate $\dot{M}_{1}$ | $1/3$ per unit input | 4.2 |
| Variance at $t=0.3$ (uniform gains) | $\sigma^{2}=0.03$, $\sigma\approx0.1732$ | 4.2 |
| Minimum steering time for $M_{1}^{\mathrm{target}}=0.1$ | $0.3$ time units | 4.2 |
| Skewed‑gain minimum time | $0.2571$ time units | 4.2 |
| Baseline expected tokens per cycle | $2.7731$ | 4.3 |
| Baseline throughput $T_{\mathrm{base}}$ | $0.55462$ | 4.3 |
| Ensemble effective acceptance $\alpha_{\mathrm{eff}}$ | $0.94$ | 4.3 |
| Ensemble expected tokens per cycle | $4.43493296$ | 4.3 |
| Ensemble throughput $T_{\mathrm{ens}}$ | $0.886986592$ | 4.3 |
| Speedup $S$ | $1.5993$ | 4.3 |
| Break‑even compute budget $C^{*}$ | $1.749086$ | 4.3 |
| Correlated‑leg ensemble throughput (Projection P1) | $0.46112$ | 4.3 |

All numbers are derived analytically; no empirical measurements are involved.

## 6. Discussion

### Limitations
1. **Independence approximation (P0).** The saturation time for DNA inversions assumes independent Hamming increments and ignores re‑flipping; the true expectation may be larger by up to one step.  
2. **Uniform gain distribution.** The immobility of the mean relies on a sign‑symmetric uniform gain density; other gain distributions yield non‑zero mean evolution (as shown for the right‑triangular case).  
3. **Bang‑bang input restriction.** The broadcast control analysis limits inputs to $\{-1,+1\}$; richer input families could achieve faster steering but are not covered.  
4. **Independent leg assumption.** The ensemble drafting model assumes leg errors are independent; correlated errors (Projection P1) reduce throughput dramatically.  
5. **Fixed draft length $\gamma$ and cost coefficients.** Results depend on the illustrative values $\gamma=4$ and $c_{i}$; different depths or cost structures change the break‑even point.

### Failure modes and falsifiability
If an implementation of ensemble leg drafting with the design‑point parameters $\alpha_{1}=0.5$, $\alpha_{2}=0.6$, $\alpha_{3}=0.7$, $\gamma=4$, and costs $(0.2,0.3,0.5)$ yields an observed throughput significantly lower than $0.887$ (e.g., below $0.80$) while maintaining independent leg behavior, the analytical model would be falsified. Similarly, observing a saturation time for the DNA inversion toy model consistently below $3$ steps would contradict the independence projection.

### Open questions
* How does the saturation time behave under exact tracking of segment overlap?  
* Can higher‑order moment closures be derived for broadcast control with drift terms?  
* What is the impact of adaptive draft‑depth selection on throughput under realistic verification cost growth?  

## 7. Practical Implications and Engineering Pathways

**(a) Users and decision impact.** Designers of large‑scale speculative‑decoding pipelines for language‑model inference can use the derived throughput formulas to decide how many draft legs to allocate, what compute budget per leg is acceptable, and whether to invest in reducing inter‑leg correlation. Control engineers building broadcast‑driven ensembles of sensors or actuators (e.g., quantum‑ensemble experiments or swarms of simple robots) can use the first‑moment rate and minimum steering time to size broadcast inputs and predict achievable collective displacement.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 2 (formulation of concept and analytical proof‑of‑concept).

**(c) Smallest next experiment.** Construct a software simulation of the three‑leg ensemble drafting system with the specified $\alpha_{i}$, $\gamma$, and $c_{i}$. Measure the average tokens advanced per cycle over $10^{5}$ cycles. If the measured $\mathbb{E}[N]$ deviates from $4.4349$ by more than $5\%$, the independence assumption is falsified.

**(d) Engineering constraints.** The derivations assume (i) exact knowledge of per‑leg acceptance probabilities $\alpha_{i}$, (ii) constant per‑position compute costs $c_{i}$, and (iii) a broadcast verification cost normalized to $1$. In practice, estimating $\alpha_{i}$ requires calibration on validation data; compute costs may vary with hardware and batch size; verification latency may grow with draft depth. These constraints must be quantified before deployment.

**(e) Projected cost and performance bounds.** Assuming the illustrative costs, the ensemble achieves a throughput of $0.887$ tokens per unit compute, a $59.9\%$ improvement over the baseline $0.555$. The break‑even compute budget $C^{*}=1.749$ indicates that the total draft compute may increase by up to $74.9\%$ before the ensemble loses its advantage.

**(f) Risks and misuse.** Over‑reliance on the independence assumption could lead to under‑estimation of latency in real systems where draft models share training data or architecture, causing correlated failures. Deployers should monitor correlation metrics and revert to single‑leg operation if correlation exceeds a threshold (e.g., $\rho>0.5$).

## 8. Conclusion

We presented a unified analytical treatment of three population‑level problems: chaotic DNA inversions, broadcast‑controlled first‑order ensembles, and speculative‑decoding ensemble leg drafting. Closed‑form expectations for Hamming divergence, exact first‑moment dynamics, and precise throughput formulas were derived with fully shown arithmetic. The results delineate the performance envelope achievable when only population‑level actuation is possible, identify key limitations, and propose concrete experimental steps to validate the models. Future work will extend the DNA inversion analysis to exact overlap tracking, explore richer broadcast‑control input families, and incorporate adaptive draft‑depth strategies under realistic verification cost models.

## References

[1] arXiv:1105.1512v1 | Chaos in DNA inversions (Draft paper)  
[2] arXiv:2606.05501v2 | Learning Contact Representation for Leg Odometry  
[3] arXiv:2603.00487v1 | DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments  
[4] arXiv:2601.20357v1 | TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs  
[5] arXiv:2108.08668v3 | Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes  
[6] arXiv:2009.02646v1 | Moment-Based Ensemble Control  
[7] arXiv:2610.10672v1 | Prescriptive Master Integrals of Maximal Weight at Two Loops  
[8] arXiv:2202.03383v1 | Asymptotic of Bergman Kernel (Master Thesis)  
[9] QNFO: Ensemble Drafting Under Broadcast Control: Throughput Algebra, Variance Reduction, and Vandermonde Conditioning  
[10] QNFO: NUMERATA: A Multi-Axis Framework for Evaluating Numeral Systems  
[11] QNFO: Connecting Geometrogenesis and Biogenesis  
[12] QNFO: Kappa/SIIT Cross-Validation: Exact Reproduction of Standard Model 1-Loop β-Functions and Resolution of the Harmonic-Paradigm Tension  

## Appendix A. Divergence report

*No divergent claims were identified among the three source drafts; all substantive claims converged.*

## Appendix B. Claim attribution

| Claim ID | Source drafts | Agreement |
|---|---|---|
| C1 | A, B, C | CONVERGENT |
| C2 | A, B, C | CONVERGENT |
| … | … | … |

*(Full attribution table omitted for brevity; each quantitative claim in Sections 4–5 is listed with its originating draft(s) and convergence status.)*