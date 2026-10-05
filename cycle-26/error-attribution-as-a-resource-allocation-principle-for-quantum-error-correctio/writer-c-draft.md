# Error Attribution as a Resource-Allocation Principle for Quantum Error Correction: An Analytic Study of Sensitivity-Guided Noise Reduction

## Abstract

Logical error rate is the standard benchmark for quantum error correction (QEC), but it aggregates the effects of all physical noise channels into a single number, hiding the fact that circuit locations with equal error probabilities can contribute very unequally to logical failure. Recent work introduced an error attribution scheme that computes per-component sensitivities jointly from the same Monte Carlo samples used to estimate the logical error rate, and showed that halving the noise on the 5%–7% most sensitive components reduces logical error rates by roughly 15%–25%, about twice the improvement from randomly chosen components [1,3]. This paper develops the analytic structure underlying such attribution-guided optimization. We formalize the logical error rate as a first-order sensitivity expansion over component error probabilities, derive closed-form expressions for the gain of targeted versus random interventions, and evaluate them numerically for explicit model noise distributions. For a 100-component circuit with a mild sensitivity skew, we show that selecting the top 5% of components yields a 6.8% relative logical error reduction versus 2.5% for random selection, a 2.7× advantage consistent in structure with the reported 2× advantage. We further derive Monte Carlo variance requirements for the sensitivity estimator and translate logical error reductions into equivalent physical error rate reductions for distance-3 surface codes. We discuss failure modes, falsifiability, and connections to channel-optimized and reinforcement-learning-based QEC.

## 1. Introduction

Quantum error correction protects quantum information by encoding it redundantly and decoding against syndrome measurements. Its performance is almost universally reported as a logical error rate $p_L$: the probability that the encoded information is corrupted after a decoding cycle. This aggregate is the right quantity for benchmarking, but it is the wrong quantity for engineering. A hardware engineer or pulse designer does not control "the noise"; they control specific gates, specific qubits, specific measurement channels. Two circuit locations with identical physical error probability $p$ can differ by an order of magnitude in how strongly their errors propagate to logical failure, because error propagation depends on circuit topology, syndrome extraction schedule, and decoder structure.

The recently introduced error attribution scheme addresses exactly this gap [1,3]. It defines a per-component sensitivity — the first-order response of the logical error rate to a change in that component's error probability — and, crucially, computes all sensitivities jointly from the same Monte Carlo samples already being collected to estimate $p_L$, so attribution comes nearly for free alongside standard benchmarking. Simulations of rotated surface codes and high-rate lifted product codes showed that halving the noise strength on the roughly 5%–7% of components selected by sensitivity reduces $p_L$ by approximately 15%–25%, roughly twice the mean reduction obtained by intervening on an equal number of randomly selected components [1,3].

This paper is an independent analytic companion to that result. Our contributions are:

1. A first-order sensitivity model of the logical error rate, $p_L \approx \sum_i s_i p_i$, with precise definitions of the sensitivity coefficients $s_i$ and their estimator.
2. Closed-form expressions for the expected gain of targeted versus random noise reduction, showing that the advantage ratio equals the ratio of selected to population-mean sensitivity.
3. Explicit numerical evaluation of these formulas for stated model parameters, reproducing the qualitative structure (and approximate magnitude) of the reported 2× advantage without any new simulation.
4. A variance analysis of the Monte Carlo sensitivity estimator, giving the sample complexity needed to resolve sensitivities above a given signal-to-noise threshold.
5. A translation layer from logical error reductions to equivalent physical error rate reductions, connecting attribution to the standard threshold framework.

Throughout, every number is either derived here with full arithmetic, quoted as a reported result with citation, or explicitly labeled a projection with stated assumptions.

## 2. Background and Related Work

The error attribution scheme itself is the direct subject of this paper. In [1,3], the authors define component sensitivities, estimate them from shared Monte Carlo samples, and demonstrate on rotated surface code memories and high-rate lifted product codes that sensitivity-guided halving of noise on 5%–7% of components yields 15%–25% logical error reduction, roughly twice the random-selection baseline. Our work takes their empirical finding as input and asks what analytic structure explains it, when it holds, and when it fails.

Channel-optimized QEC [2] is the conceptual ancestor of noise-aware code design: it develops a theory of QEC procedures optimized for a given noise channel, robust to uncertainties in that channel, and shows numerically that optimized procedures always beat the noise-agnostic standard. Error attribution complements this by supplying the fine-grained channel knowledge (which components matter, not just which error types) that channel-optimized designs consume. Robustness-optimized QEC [5] makes the complementary point that in small-scale devices, where dominant error sources are understood, exploiting that knowledge yields more efficient correction than source-agnostic design; sensitivity maps are precisely the quantitative instrument for such exploitation at component granularity.

Reinforcement learning approaches search the QEC design space automatically: [4] trains RL agents to optimize and fault-tolerantly adapt QEC codes for unknown or device-specific error channels, and [9] extends deep RL to discover autonomous QEC encodings for bosonic systems under Knill–Laflamme constraints. Both are powerful but sample-hungry black-box optimizers; attribution provides a gradient-like signal that could seed or constrain such searches, potentially reducing the search dimensionality from the full circuit space to the sensitivity-ranked subspace.

Gauge-optimization work [8] identifies gauge freedoms in QEC codes and uses optimal control to find decompositions into elementary operations easiest to realize on a given physical system. This is structurally analogous to attribution: both ask "given this hardware, which degrees of freedom of the code matter most?", though [8] optimizes implementation decomposition while attribution optimizes noise budget allocation.

Erasure-qubit protocols [7] analyze how converting unknown errors into flagged erasures improves surface code performance, at the cost of erasure-check overhead. Attribution and erasure conversion are complementary levers: erasure qubits change the error structure globally, while attribution targets the residual location-dependent noise that remains.

On the modeling side, [6] compares fully coherent simulations of $d=3$ Steane and surface code circuits against stochastic error models and finds markedly different failure distributions with no simple mapping between them. This is a serious caveat for any first-order stochastic sensitivity analysis, including ours: coherent errors can add constructively in ways the linear model in Eq. (1) below does not capture. Continuous-time QEC [10] reframes both noise and correction as continuous processes via weak measurement and feedback; in that setting, "component" attribution would need redefinition as attribution over time intervals or measurement channels, an open generalization. Entanglement-assisted codes [11] provide code-construction machinery where attribution could similarly guide which ancilla entanglement-assisted checks deserve hardware investment.

Finally, the QNFO corpus situates QEC benchmarking in a broader landscape: [12] surveys implications of QEC for computing, [13] reports a no-go result (attributed to Maity et al., arXiv:2608.03944) that QEC and Quantum Darwinism cannot coexist above a critical logical fidelity $F_L > 0.874$, and [14] proposes passive error resilience via ultrametric ($p$-adic) geometry for quantum metrology. If the [13] tradeoff holds, sensitivity-guided improvements pushing $F_L$ upward would eventually collide with a Darwinism boundary — a speculative but intriguing interaction we flag in Section 6.

## 3. Methods

### 3.1 Sensitivity model

Let a QEC circuit consist of $N$ noise locations ("components": gates, idles, measurements), with component $i$ failing with probability $p_i$ per cycle via a stochastic Pauli-type channel. Define the logical error rate functional $p_L(p_1,\dots,p_N)$. The first-order (dominant-term) expansion is

$$
p_L \;\approx\; \sum_{i=1}^{N} s_i\, p_i, \qquad s_i \;\equiv\; \left.\frac{\partial p_L}{\partial p_i}\right|_{\mathbf{p}=\mathbf{p}^{(0)}} ,
$$

valid when $\sum_i p_i \ll 1$ and logical failure is dominated by single-component fault paths; higher-order terms scale as $O\!\left(\big(\sum_i p_i\big)^2\right)$. The sensitivity $s_i$ is dimensionless and counts, roughly, the number of minimal logical-fault paths through component $i$, weighted by their syndromic detectability.

### 3.2 Attribution estimator

Following [1,3], sensitivities are estimated from the same $M$ Monte Carlo samples used for $\hat p_L$. With common random numbers, each sample $m$ carries an attribution weight $w_i^{(m)}$ measuring component $i$'s involvement in the failure pattern of sample $m$; the estimator is

$$
\hat s_i \;=\; \frac{1}{M\, p_i}\sum_{m=1}^{M} \mathbb{1}[\text{fail}_m]\, w_i^{(m)} ,
$$

so all $N$ sensitivities are obtained jointly at no additional sampling cost beyond storing per-sample attribution weights.

### 3.3 Intervention model

An intervention halves the noise strength on a chosen subset $S$ of $k$ components: $p_i \mapsto p_i/2$ for $i \in S$. Under Eq. (1), the relative logical error reduction is

$$
r(S) \;=\; \frac{\Delta p_L}{p_L} \;=\; \frac{\tfrac{1}{2}\sum_{i\in S} s_i p_i}{\sum_{j=1}^{N} s_j p_j}.
$$

For uniform $p_i = p$ this simplifies to $r(S) = \frac{1}{2}\,\bar s_S / \bar s_{\text{all}}$, where $\bar s_S = \frac{1}{k}\sum_{i\in S} s_i$. The advantage of targeted over random selection is therefore

$$
A \;=\; \frac{r(S_{\text{top}})}{r(S_{\text{rand}})} \;=\; \frac{\bar s_{\text{top}}}{\bar s_{\text{all}}},
$$

independent of $p$, $k$, and $N$ — the entire game is the sensitivity skew.

### 3.4 Monte Carlo variance

The logical error estimate $\hat p_L$ from $M$ samples has binomial variance $p_L(1-p_L)/M$. A sensitivity estimate inherits variance from the failure indicator: writing $\mathrm{Var}[\mathbb{1}[\text{fail}]\,w_i] \le \mathbb{E}[w_i^2\,|\,\text{fail}]\,p_L$, we obtain the conservative bound

$$
\mathrm{Var}[\hat s_i] \;\le\; \frac{\mathbb{E}[w_i^2 \mid \text{fail}]}{M\, p_i^2}\, p_L .
$$

We evaluate this numerically in Section 4 for stated parameters.

## 4. Analysis

All numbers in this section are computed from the model of Section 3 with explicitly stated inputs. No empirical or simulated data beyond the reported results of [1,3] are used.

**Model inputs (stated assumptions).** (i) $N = 100$ components (illustrative circuit scale, comparable to a small rotated surface code patch's syndrome-extraction circuit). (ii) Uniform physical error probability $p_i = p = 10^{-4}$ per component per cycle — a plausible near-term gate error scale. (iii) Mild sensitivity skew: $n_1 = 5$ "hotspot" components with $s_1 = 3$, and $n_0 = 95$ background components with $s_0 = 1$. This skew is chosen to be conservative relative to the heterogeneous circuits of [1,3], where sensitivities "differ markedly."

**Step 1: Baseline logical error rate.**

$$
p_L^{(0)} = \sum_{i=1}^{100} s_i p_i = p\,(n_1 s_1 + n_0 s_0) = 10^{-4}\,(5 \times 3 + 95 \times 1) = 10^{-4} \times 110 = 1.10 \times 10^{-2}.
$$

**Step 2: Targeted intervention, $k = 5$ (top 5% by sensitivity).** Halving noise on the five hotspots:

$$
\Delta p_L = \frac{1}{2}\, p\, k\, s_1 = \frac{1}{2} \times 10^{-4} \times 5 \times 3 = 7.50 \times 10^{-4},
$$

$$
r_{\text{top}} = \frac{7.50 \times 10^{-4}}{1.10 \times 10^{-2}} = 0.0682 \;\approx\; 6.8\%.
$$

**Step 3: Random intervention, same $k = 5$.** A uniformly random 5-subset has expected sensitivity sum $\mathbb{E}\big[\sum_{i\in S_{\text{rand}}} s_i\big] = k\,\bar s_{\text{all}}$, with population mean

$$
\bar s_{\text{all}} = \frac{110}{100} = 1.10,
$$

so

$$
\Delta p_L^{\text{rand}} = \frac{1}{2} \times 10^{-4} \times 5 \times 1.10 = 2.75 \times 10^{-4}, \qquad
r_{\text{rand}} = \frac{2.75 \times 10^{-4}}{1.10 \times 10^{-2}} = 0.0250 \;\approx\; 2.5\%.
$$

**Step 4: Advantage ratio.**

$$
A = \frac{r_{\text{top}}}{r_{\text{rand}}} = \frac{\bar s_{\text{top}}}{\bar s_{\text{all}}} = \frac{3}{1.10} = 2.73.
$$

This reproduces the qualitative structure of the reported result — targeted selection roughly doubling (here: $2.7\times$) the mean random-selection gain — from a deliberately mild skew. The reported 15%–25% absolute reductions in [1,3] exceed our 6.8% because real circuits exhibit stronger skew and the intervention fraction there (5%–7%) acts on components whose sensitivities dominate the failure budget; Eq. (3) shows $r$ scales linearly with $\bar s_S$.

**Step 5: Skew needed to match the reported 15%–25%.** Inverting Eq. (3) with $k/N = 0.05$: $r_{\text{top}} = \frac{1}{2}\cdot 0.05 \cdot \bar s_{\text{top}}/\bar s_{\text{all}} \cdot N$... more directly, $r_{\text{top}} = \frac{k\, s_{\text{top}}}{2 \sum_j s_j}$. Setting $r_{\text{top}} = 0.20$ with $k=5$, $N=100$, $s_0=1$: $0.20 = \frac{5 s_1}{2(5 s_1 + 95)}$, so $0.40(5 s_1 + 95) = 5 s_1$, i.e., $2 s_1 + 38 = s_1$ — no positive solution with only 5 hotspots; the reported 20% reduction requires either broader hotspots or stronger concentration. With $k = 7$ and $s_1 = 20$ (a 20× skew, plausible for measurement-heavy locations): $r_{\text{top}} = \frac{7 \times 20}{2(7\times20 + 93\times1)} = \frac{140}{2 \times 233} = \frac{140}{466} = 0.300$ — above the reported range; with $s_1 = 10$: $r_{\text{top}} = \frac{70}{2(70+93)} = \frac{70}{326} = 0.215$, inside the reported 15%–25% band. A 10× sensitivity skew on 7% of components therefore suffices to reproduce the reported magnitudes exactly.

**Step 6: Monte Carlo variance.** With $p_L = 1.10\times10^{-2}$ and $M = 10^{5}$ samples:

$$
\mathrm{Var}[\hat p_L] = \frac{p_L(1-p_L)}{M} = \frac{0.0110 \times 0.9890}{10^{5}} = \frac{1.0879\times10^{-2}}{10^{5}} = 1.0879 \times 10^{-7},
$$

$$
\sigma_{\hat p_L} = \sqrt{1.0879\times10^{-7}} \approx 3.30 \times 10^{-4}, \qquad \frac{\sigma_{\hat p_L}}{p_L} \approx 3.0\%.
$$

For a single sensitivity with attribution weight bounded by $w_i \le 1$ and $p_i = 10^{-4}$, Eq. (5) gives

$$
\mathrm{Var}[\hat s_i] \le \frac{1 \times 1.10\times10^{-2}}{10^{5} \times (10^{-4})^2} = \frac{1.10\times10^{-2}}{10^{5} \times 10^{-8}} = \frac{1.10\times10^{-2}}{10^{-3}} = 11.0,
$$

i.e., $\sigma_{\hat s_i} \le 3.3$ — far too noisy to rank individual components at $M = 10^5$. Resolving a sensitivity contrast of $s_1/s_0 = 10$ at $2\sigma$ requires $\sigma_{\hat s_i} \lesssim 5$, still marginal; at $M = 10^{7}$, $\sigma_{\hat s_i} \le \sqrt{11.0}/10 = 0.33$, adequate. This is consistent with the joint-estimation design of [1,3]: attribution is cheap per component but demands the large sample counts already routine in code-threshold studies.

**Step 7: Translating logical gains to physical error budgets.** For surface codes below threshold, $p_L \sim A_d\,(p/p_{\text{th}})^{(d+1)/2}$; for $d = 3$ the exponent is $(3+1)/2 = 2$. If attribution-guided intervention reduces $p_L$ by a factor $(1 - r)$, the equivalent uniform physical error reduction factor is

$$
\frac{p_{\text{eff}}}{p} = (1-r)^{1/2}.
$$

For $r = 0.20$: $(1-0.20)^{1/2} = \sqrt{0.8} = 0.894$, i.e., a 20% logical reduction is equivalent to a uniform $\approx 10.6\%$ physical error rate reduction — achieved by touching only 5%–7% of components. For our model's $r = 0.068$: $\sqrt{0.932} = 0.9654$, a $3.5\%$ equivalent uniform reduction.

## 5. Results

All results below are computed in Section 4 from the stated model; reported empirical results of [1,3] are labeled as such.

1. **Baseline (model).** For $N=100$, $p = 10^{-4}$, sensitivities $\{3 \times 5,\, 1 \times 95\}$: $p_L^{(0)} = 1.10 \times 10^{-2}$.
2. **Targeted gain (model).** Halving noise on the top 5 components: $\Delta p_L = 7.50\times10^{-4}$, relative reduction $r_{\text{top}} = 6.8\%$.
3. **Random gain (model).** Same budget, random selection: $r_{\text{rand}} = 2.5\%$; advantage ratio $A = 2.73$.
4. **Skew calibration (model).** Reproducing the reported 15%–25% band of [1,3] requires a sensitivity skew of roughly $10\times$ on $\sim$7% of components (e.g., $k=7$, $s_1 = 10$ gives $r_{\text{top}} = 21.5\%$); a 20× skew overshoots ($30.0\%$).
5. **Reported (empirical, [1,3]).** Sensitivity-guided halving on 5%–7% of components yields $\approx$15%–25% logical error reduction, roughly $2\times$ the random-selection mean, in rotated surface codes and lifted product codes.
6. **Sampling requirement (model).** At $M = 10^{5}$ samples, $\sigma_{\hat p_L}/p_L \approx 3.0\%$, but per-component sensitivity standard deviation is bounded by $3.3$ — insufficient for ranking; $M = 10^{7}$ brings $\sigma_{\hat s_i} \le 0.33$, adequate for $10\times$ contrasts.
7. **Equivalent physical budget (model).** A 20% logical reduction corresponds to a uniform physical error reduction factor of $0.894$ ($\approx 10.6\%$); the model's 6.8% reduction corresponds to $0.9654$ ($\approx 3.5\%$).

**Projection (labeled).** If real circuits exhibit the $\ge 10\times$ skews calibrated in Result 4, then attribution-guided allocation of a fixed noise-reduction budget (e.g., improved calibration, dynamical decoupling, or gate recompilation on selected locations) should deliver 15%–25% logical improvements at 5%–7% hardware coverage, with uncertainty dominated by the unknown true sensitivity distribution; the linear model Eq. (1) itself contributes $O\big((\sum_i p_i)^2\big)$ bias, negligible for $\sum_i p_i \lesssim 10^{-2}$.

## 6. Discussion

**Limitations.** The first-order model Eq. (1) assumes stochastic, independent, Pauli-type errors. Reference [6] showed that coherent errors produce failure distributions with no simple mapping to the stochastic case, so sensitivities estimated under a stochastic model may misrank locations when coherent error accumulation dominates — a direct falsification channel for our framework. Second, Eq. (3)'s independence of $p$, $k$, $N$ holds only in the linear regime; near or above threshold, or for high-rate lifted product codes where correlated fault paths matter, higher-order terms compress the advantage. Third, our numerical model is illustrative: the 10× skew calibrated in Step 5 is a consistency requirement, not a measurement; the actual skew distribution in real circuits is the key unknown that only experiments or the full simulations of [1,3] can supply.

**Failure modes.** Attribution can mislead if (i) sensitivities are estimated with insufficient samples (Step 6 shows $M = 10^5$ is inadequate per-component; ranking noise could cause intervention on background components); (ii) the noise model is non-stationary, so sensitivity maps drift between calibration and deployment; (iii) interventions on hotspots shift the failure budget to previously subdominant components, saturating gains — the linear model predicts no such saturation, so observed saturation would itself be informative.

**Arguing against ourselves.** A skeptic could note that the 2× advantage of [1,3] is modest and might be matched by simpler heuristics (e.g., prioritizing measurement locations, which are known error hotspots) without any attribution machinery. Our Step 5 supports this concern partially: a 10× skew is what drives the gains, and if such skew correlates trivially with component type, attribution reduces to a lookup table. The counterargument is that attribution is data-driven and catches non-obvious hotspots (e.g., schedule-dependent idling locations), but this remains to be demonstrated against type-based baselines. A second objection: the sampling requirement of Result 6 ($M \sim 10^{7}$ for reliable ranking) may exceed what hardware can afford in real time, confining attribution to offline calibration campaigns — acceptable, but weakening the "nearly free" framing.

**Falsification.** The core claim — that sensitivity skew is large enough and stable enough for targeted intervention to beat random allocation by $\gtrsim 2\times$ — would be falsified by experiments showing (a) near-uniform sensitivity distributions across circuit components, (b) rapid drift of sensitivity rankings under recalibration, or (c) coherent-error dominance invalidating stochastic sensitivities per [6].

**Open questions.** How does attribution generalize to continuous-time QEC [10], where components are replaced by time intervals and weak-measurement channels? Can sensitivity maps seed the RL agents of [4,9] to accelerate code discovery? Do gauge-optimized decompositions [8] and erasure conversion [7] interact multiplicatively with attribution-guided noise budgets? Speculatively, if the QEC–Quantum Darwinism no-go at $F_L > 0.874$ reported in [13] is correct, attribution-guided gains push devices toward a fundamental tradeoff boundary rather than an unbounded improvement path; and passive ultrametric resilience schemes [14] would need their own attribution theory. Finally, the QNFO survey [12] suggests attribution-style fine-grained benchmarking may become standard practice for resource estimation in fault-tolerant architectures.

## 7. Conclusion

Error attribution converts the logical error rate from a single benchmark number into a spatial map of engineering leverage. We showed analytically that the advantage of sensitivity-guided over random noise reduction equals the ratio of selected to mean sensitivity (Eq. (4)), that a mild 3× skew already yields a 2.7× advantage in an explicit 100-component model, and that the empirically reported 15%–25% gains of [1,3] are consistent with a $\sim$10× skew on $\sim$7% of components. The framework's costs are a demanding (but standard) Monte Carlo budget and an assumption of stochastic, stationary noise. As QEC moves from demonstrating thresholds to optimizing deployed devices, attribution provides the missing link between benchmarking and resource-constrained design.

## References

[1] arXiv Query: search_query=&id_list=2610.03399&start=0&max_results=1 — "Optimizing quantum error correction through error attribution" (abstract record).

[2] arXiv:0810.2524v1 | Channel-Optimized Quantum Error Correction

[3] arXiv:2610.03399v1 | Optimizing quantum error correction through error attribution

[4] arXiv:1812.08451v5 | Optimizing Quantum Error Correction Codes with Reinforcement Learning

[5] arXiv:1909.05156v2 | Robustness-optimized quantum error correction

[6] arXiv:1704.03961v1 | Quantum error correction failure distributions: comparison of coherent and stochastic error models

[7] arXiv:2408.00829v3 | Optimizing quantum error correction protocols with erasure qubits

[8] arXiv:1411.1779v2 | Optimized Quantum Error Correction Codes for Experiments

[9] arXiv:2511.12482v2 | Discovering autonomous quantum error correction via deep reinforcement learning

[10] arXiv:1311.2485v2 | Continuous-time quantum error correction

[11] arXiv:1610.04013v1 | Entanglement-Assisted Quantum Error-Correcting Codes

[12] QNFO: Implications for Computing and Quantum Error Correction | DOI 10.5281/zenodo.21979060

[13] QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces | DOI 10.5281/zenodo.21964674

[14] QNFO: Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology | DOI 10.5281/zenodo.21748299