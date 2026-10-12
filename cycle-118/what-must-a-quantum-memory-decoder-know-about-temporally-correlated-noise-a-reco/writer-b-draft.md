# What Must a Quantum-Memory Decoder Know About Temporally Correlated Noise? An Analytical Exposition and Cost Accounting

## Abstract

Temporal correlations in physical noise are a known hazard for quantum error correction (QEC), but the precise informational demands they place on a decoder, and the price of ignoring them, have only recently been quantified. We present a self-contained analytical exposition of the framework of arXiv:2610.03545v1, which studies fixed stabilizer memory experiments with known system-environment interactions and asks what a decoder must know about temporally correlated noise and what it costs to learn. The source work's central example is a pair of noise models built from weak coherent $X$ rotations on CSS codes (including Shor, Steane, and odd-distance rotated surface codes) in which all physical qubits share a sign that is either fixed for the whole run or independently redrawn each interval. The two models are syndrome-identical and share the same spatiotemporal Pauli process, yet demand different logical corrections at suitable storage times. We reconstruct the calibration formalism in terms of fidelity differences selecting a Pauli recovery, derive the weak-noise error probabilities and calibration-cost scalings with explicit arithmetic, and exhibit a worked example in which the model-agnostic worst-case fidelity loss approaches $1/2$ while the calibration cost drops from $\theta^{-d_X}$ to $\theta^{-2}$ intervals under a relaxed extraction schedule. We situate the result in the surrounding literature on noise, correlated quantum states, and quantum memories, and discuss implications for honest resource accounting in QEC experiments.

## 1. Introduction

Quantum error correction protects quantum information by measuring syndromes and applying recovery operations. The standard abstraction treats the physical noise as a stochastic process that the decoder may model statistically; the decoder's job is then to infer the most likely error given the syndrome record. This abstraction quietly assumes that whatever statistics the decoder needs are either known a priori or estimable from data without ambiguity. Temporally correlated noise breaks this assumption in a sharp and quantifiable way: two noise models can produce *identical* syndrome statistics on every measurement round and yet require *different* logical corrections, so that no amount of syndrome data alone distinguishes them, and a decoder calibrated on the wrong model pays a fidelity penalty that can approach one half.

The paper under exposition, arXiv:2610.03545v1 [1, 2], formalizes this situation. It studies fixed stabilizer memory experiments with known system-environment interactions, formulates calibration in terms of the fidelity differences that select a Pauli recovery, and relates missing information to the resulting fidelity loss. Its main example uses weak coherent $X$ rotations in a class of CSS codes including Shor, Steane, and odd-distance rotated surface codes, with all physical qubits sharing a sign that is either fixed throughout a run or independently redrawn each interval. The two resulting models have identical syndrome statistics and the same spatiotemporal Pauli process (SPP), obtained by Pauli-twirling every noise interval, yet at suitable storage times they require different logical corrections.

This paper has three goals. First, to make the source work's setup and claims accessible to an adjacent-field expert by reconstructing the model, the calibration criterion, and the scaling laws with all definitions in place. Second, to provide explicit numerical derivations of the quantities the framework controls — per-interval error probabilities, logical failure rates, calibration costs, and worst-case fidelity gaps — so that the magnitudes are transparent rather than quoted. Third, to place the contribution in the context of the supplied bibliography and to assess honestly what the framework establishes, what it assumes, and where it could fail. Throughout, every quantitative claim is either derived in Section 4 with shown arithmetic or explicitly labeled as a projection with stated assumptions; no experimental or simulated data are reported, because none are supplied by the source material.

## 2. Background and Related Work

We review the supplied bibliography, restricting every statement to what each entry itself states.

**[1] and [2] (arXiv:2610.03545v1, "What Must a Quantum-Memory Decoder Know About Temporally Correlated Noise?").** These two bibliography entries refer to the same arXiv identifier and carry the same abstract text; [1] is the full fetched abstract and [2] a truncated version. The work asks what a quantum error-correction decoder must know about temporally correlated noise and what it costs to learn, for fixed stabilizer memory experiments with known system-environment interactions. It formulates calibration in terms of the fidelity differences that select a Pauli recovery and relates missing information to the resulting fidelity loss. Its main example uses weak coherent $X$ rotations in a class of CSS codes including Shor, Steane, and odd-distance rotated surface codes, with all physical qubits sharing a sign either fixed throughout a run or independently redrawn each interval. The two models have identical syndrome statistics and the same spatiotemporal Pauli process obtained by Pauli-twirling every noise interval, yet at suitable storage times require different logical corrections. In the weak-noise limit each model is almost perfectly correctable when known; without model information, even the best final recovery has a worst-case fidelity loss approaching $1/2$ relative to the noise-aware optimum, despite access to the full syndrome record. For this pair of models, at fixed code and fixed positive target loss below $1/2$, matching calibration bounds are proved; with logical preparation and final readout, complete QEC cycles require a number of noise intervals scaling as the inverse rotation angle raised to the code's $X$ distance, and allowing two uninterrupted intervals before one extraction reduces the optimal cost to inverse-square scaling. Physical Pauli twirling of every noise interval changes both recovery performance and its information requirements; discarding the record of applied random Pauli operations makes the SPP sufficient for optimal recovery, while keeping the record can improve attainable fidelity but may require additional noise information. This is the primary object of exposition in the present paper.

**[3] (arXiv:1008.0667v2, "Noise and Bell's inequality").** This entry concerns the foundational discussion of reality beginning with the EPR paradox and the Bell inequality, noting that considerable evidence exists that the inequality can be violated even by classical systems, so that experiments showing quantum behavior may be confounded. The entry is truncated at this point and supplies no further detail. Its relevance here is thematic only: it flags that distinguishing genuinely quantum behavior from classical correlated alternatives is a standing interpretive problem, a concern that echoes the source work's finding that syndrome-identical noise models can be behaviorally distinct at the logical level.

**[4] (arXiv:1310.1481v1, "Strongly correlated superconductivity").** These are lecture notes for an international school emphasizing that, although band theory and BCS theory are arguably the most successful theories of condensed matter physics, they fail in a number of materials, in particular the high-temperature superconductors and the layered organic superconductors, and that low-energy properties of a phase of matter are generally emergent. The entry is truncated and gives no further detail. We cite it only as an example from a neighboring field in which correlations beyond a baseline mean-level theory dominate phenomenology — the same structural situation as temporally correlated noise beyond an independent-error baseline.

**[5] (arXiv:1612.01464v2, "Finite blocklength and moderate deviation analysis of hypothesis testing of correlated quantum states and application to classical-quantum channels with memory").** This work applies martingale concentration inequalities — described as a powerful mathematical tool across probability, statistics, information theory, and machine learning — to quantum hypothesis testing, the problem of discriminating quantum states belonging to two different sequences $\{\rho_n\}$. The entry is truncated before stating its results. Its relevance is methodological: hypothesis testing between sequences of correlated quantum states is formally the same discrimination problem a decoder faces when two temporally correlated noise models must be told apart, and the entry confirms that finite-blocklength and memory-aware tools exist for such problems.

**[6] (arXiv:1601.00157v1, "Theory of noise suppression in $\Lambda$-type quantum memories by means of a cavity").** This work treats quantum memories capable of storing single photons or other quantum states of light for on-demand retrieval, a route to large-scale quantum information processing with light, focusing on far-off-resonant Raman absorption in ensembles of $\Lambda$-type atoms, where at room temperature unwanted four-wave mixing is prohibitive. The entry is truncated. It supplies the hardware-side motivation: physical quantum memories come with structured, unwanted noise processes whose suppression is an active design problem, complementing the decoder-side question of what must be *known* about such processes.

**[7] (arXiv:1612.03430v1, "Quantum and Classical Frontiers of Noise").** This is an introduction to the eleven works of a special issue on Quantum and Classical Frontiers of Noise. It uses the weather and its butterfly effect as the typical example explaining why many natural phenomena are not predictable with certainty, and understands noise in classical or quantum phenomena as the difference between the empirical output of an experiment and its statistical description. The entry is truncated. It frames noise as a definitional and epistemic matter — the gap between empirical output and statistical model — which is precisely the gap the source work prices in fidelity units.

**[8] (arXiv:2311.17794v1, "Noise Dynamics in the Quantum Regime").** This experimental work shows that a time-dependent bias voltage on a tunnel junction generates a time-dependent modulation of its current fluctuations, in particular of their variance, translating into an excitation at frequency $\tilde{f}$ that generates correlations between current fluctuating at any frequency $f$ and at frequency $\pm\tilde{f}-f$; the authors report the measurement of such a correlation in the fully quantum regime. This is a concrete instance of engineered temporal correlations in a quantum-noise source, the physical raw material from which decoder-facing correlated noise models are built.

**[9] (arXiv:1605.07838v1, "Decoherence and noise in open quantum system dynamics").** This work considers the description of quantum noise within the Copenhagen interpretation applied to a composite system-environment setting, where averaging over environmental degrees of freedom leads to stochastic quantum dynamics described by equations complying with the constraints arising from the statistical structure of quantum mechanics. The entry is truncated. It supplies the standard open-system formal background: noise as environment-induced stochastic dynamics, the level at which the source work's system-environment interactions are specified.

**[10]–[13] (QNFO corpus).** Entry [10] describes a framework matching computational problem classes to optimal physical substrates as part of a critique-driven investment portfolio. Entry [11] is supplied with an empty summary and gives no further detail; we note only its title's topic, spectral benchmarking of holographic quantum simulations, and draw no substantive claim from it. Entry [12] describes an audit of a tunable quantum neural network implemented on three quantum computing platforms, conducted through a multi-phase research pipeline including due diligence and an external literature search across 32 papers. Entry [13] examines fundamental physical limits on computation — the Landauer bound, Margolus-Levitin theorem, Bremermann limit, and Bekenstein bound — and shows that quantum error-correction overhead of $10^2$–$10^3$ physical operations per logical operation multiplies thermodynamic cost. Entry [13] is directly relevant to our cost accounting: any calibration overhead identified by the source work multiplies the already large QEC overhead it documents.

In summary, the bibliography contains one central technical source ([1]/[2]) and a ring of contextual works on noise foundations [3], [7], correlated-state discrimination [5], memory hardware [6], engineered noise correlations [8], open-system dynamics [9], condensed-matter correlations [4], and computation-cost accounting [10]–[13]. Several entries are truncated; where so, we have said so and drawn no unsupported inference.

## 3. Methods

### 3.1 Setting

Following [1], consider a fixed stabilizer memory experiment: a CSS code (the class named includes Shor, Steane, and odd-distance rotated surface codes) storing a logical qubit for a storage time divided into $N_{\mathrm{int}}$ noise intervals, with logical preparation at the start and final readout at the end. The system-environment interaction is assumed known: in the main example it is a weak coherent $X$ rotation, i.e., every physical qubit undergoes a rotation $\exp(-i\theta X_j/2)$ per interval with small rotation angle $\theta$, whose sign $s_k \in \{+1,-1\}$ in interval $k$ is random. Two models are compared:

- **Model F (fixed sign):** a single sign $s$ is drawn once and fixed throughout the run.
- **Model R (redrawn sign):** the sign $s_k$ is drawn independently and uniformly in each interval.

### 3.2 Pauli twirling and the SPP

Pauli twirling a noise interval means replacing the coherent rotation by a randomly chosen Pauli operation matched to reproduce the same average channel; the resulting classical process over Pauli errors is the spatiotemporal Pauli process (SPP). Per [1], both models yield identical syndrome statistics and the same SPP under twirling of every interval. The SPP is thus a *sufficient statistic for the syndrome-generating process* but, as [1] shows, not always for optimal recovery: at suitable storage times the two models require different logical corrections.

### 3.3 Calibration criterion

Calibration is formulated in terms of the fidelity differences that select a Pauli recovery: for each candidate Pauli recovery $R_a$, let $F_a^{(m)}$ denote the resulting logical fidelity under model $m \in \{\mathrm{F},\mathrm{R}\}$. The selected recovery under model $m$ is

$$a^\star(m) = \arg\max_a F_a^{(m)},$$

and the calibration loss of using model $m$'s optimum when model $m'$ governs is

$$\Delta F(m \to m') = F_{a^\star(m')}^{(m')} - F_{a^\star(m)}^{(m')}.$$

Missing information about the model maps directly into this fidelity loss; [1] proves matching calibration bounds for this model pair at fixed code and fixed positive target loss below $1/2$.

### 3.4 Extraction schedules

With logical preparation and final readout, complete QEC cycles require a number of noise intervals scaling as $\theta^{-d_X}$, where $d_X$ is the code's $X$ distance (the minimum weight of a Pauli-$X$-type logical operator). Allowing two uninterrupted noise intervals before one syndrome extraction reduces the optimal cost to inverse-square scaling, i.e., proportional to $\theta^{-2}$.

## 4. Analysis

All inputs below come from the abstract of [1] (rotation angle $\theta$ as a small parameter, $X$ distance $d_X$, the $\theta^{-d_X}$ and $\theta^{-2}$ scalings, the $1/2$ worst-case loss bound) or are standard small-angle trigonometric expansions, whose arithmetic is shown in full.

**Input 1 (from [1]):** the noise is weak coherent $X$ rotation with angle $\theta$ per interval; "weak-noise limit" means $\theta \ll 1$.

**Derivation D1 — per-qubit $X$-error probability per interval.** A coherent rotation $\exp(-i\theta X/2)$ applied to a computational-basis state produces an $X$-error component with probability

$$p_X(\theta) = \sin^2\!\left(\frac{\theta}{2}\right).$$

For small $\theta$, using $\sin u \approx u - u^3/6$ with $u = \theta/2$:

$$\sin^2\!\left(\frac{\theta}{2}\right) = \left(\frac{\theta}{2}\right)^2 - \frac{1}{3}\left(\frac{\theta}{2}\right)^4 + O(\theta^6) \approx \frac{\theta^2}{4}.$$

Concrete value: take $\theta = 10^{-2}$ rad (a representative weak angle; the choice is ours for illustration, not from [1]). Then

$$p_X = \sin^2(5 \times 10^{-3}) \approx \frac{(10^{-2})^2}{4} = \frac{10^{-4}}{4} = 2.5 \times 10^{-5}.$$

More precisely, $\sin(5\times10^{-3}) = 4.99998\times10^{-3}$ to six decimals, so $\sin^2(5\times10^{-3}) = 2.49998\times10^{-5}$; the leading-order value $2.5\times10^{-5}$ is accurate to relative error $\approx \theta^2/12 = 8.33\times10^{-7}$.

**Derivation D2 — logical failure probability per interval.** For a CSS code with $X$ distance $d_X$, a logical $X$-type failure requires a chain of at least $d_X$ physical $X$ errors aligned with a logical operator. In the weak-noise limit the dominant contribution is the minimum-weight chain, so the per-interval logical failure probability satisfies, to leading order,

$$p_L \approx C_{d_X}\, p_X^{\,d_X},$$

where $C_{d_X}$ is the number of minimum-weight logical operators (a code-dependent combinatorial factor; for the Steane code, which has weight-3 $X$-type logicals, $C_{d_X} \geq 1$; we keep $C_{d_X}$ symbolic since [1] does not specify it). With $p_X = 2.5\times10^{-5}$ and $d_X = 3$ (both Shor and Steane codes have $d_X = 3$; this is standard code data, stated here as the definition of these codes' distances):

$$p_L \approx C_3 \,(2.5\times10^{-5})^3 = C_3 \times 1.5625\times10^{-14}.$$

So even with $C_3$ as large as $10^2$, $p_L \lesssim 1.5625\times10^{-12}$ per interval — each model is, as [1] states, almost perfectly correctable when known.

**Derivation D3 — calibration cost, one-extraction schedule.** From [1]: complete QEC cycles require a number of noise intervals scaling as the inverse rotation angle raised to the code's $X$ distance:

$$N_{\mathrm{cal}}^{(1)} \sim \theta^{-d_X}.$$

With $\theta = 10^{-2}$ and $d_X = 3$:

$$N_{\mathrm{cal}}^{(1)} \sim (10^{-2})^{-3} = 10^{6} \text{ intervals}.$$

**Derivation D4 — calibration cost, two-intervals-per-extraction schedule.** From [1]: allowing two uninterrupted intervals before one extraction reduces the optimal cost to inverse-square scaling:

$$N_{\mathrm{cal}}^{(2)} \sim \theta^{-2}.$$

With $\theta = 10^{-2}$:

$$N_{\mathrm{cal}}^{(2)} \sim (10^{-2})^{-2} = 10^{4} \text{ intervals}.$$

The improvement factor is

$$\frac{N_{\mathrm{cal}}^{(1)}}{N_{\mathrm{cal}}^{(2)}} \sim \frac{10^{6}}{10^{4}} = 10^{2} = \theta^{-(d_X - 2)} = (10^{-2})^{-1} = 100.$$

For a distance-5 rotated surface code at the same angle, $N_{\mathrm{cal}}^{(1)} \sim (10^{-2})^{-5} = 10^{10}$ versus $N_{\mathrm{cal}}^{(2)} \sim 10^{4}$, a factor of $10^{6}$.

**Derivation D5 — worst-case model-agnostic fidelity loss.** From [1]: without model information, even the best final recovery has a worst-case fidelity loss approaching $1/2$ relative to the noise-aware optimum, despite access to the full syndrome record. Take the noise-aware optimum fidelity at a suitable storage time to be $F_{\mathrm{opt}}$. The model-agnostic best fidelity is then bounded by

$$F_{\mathrm{agg}} \leq F_{\mathrm{opt}} - \frac{1}{2} \quad (\text{worst case, as } \Delta F \to \tfrac{1}{2}).$$

Illustrative arithmetic: in the weak-noise limit with $\theta = 10^{-2}$, $d_X = 3$, and a storage time of $N_{\mathrm{int}} = 10^{3}$ intervals, the noise-aware optimum is nearly perfect; projecting with the per-interval logical failure rate of D2 and assuming independence across intervals (a stated assumption of this projection, not a claim of [1]),

$$F_{\mathrm{opt}} \gtrsim 1 - N_{\mathrm{int}}\, p_L = 1 - 10^{3} \times C_3 \times 1.5625\times10^{-14} = 1 - C_3 \times 1.5625\times10^{-11}.$$

Even with $C_3 = 10^{2}$, $F_{\mathrm{opt}} \gtrsim 1 - 1.5625\times10^{-9} \approx 0.999999998$. The worst-case model-agnostic fidelity is then

$$F_{\mathrm{agg}} \leq 0.999999998 - 0.5 = 0.499999998,$$

i.e., the decoder can be worse than a coin flip in fidelity terms, despite seeing the complete syndrome record. This is the quantitative content of [1]'s headline claim: the loss is not a small modeling error but an order-one penalty.

**Derivation D6 — target-loss calibration bounds.** From [1]: at fixed code and fixed positive target loss $\delta$ with $0 < \delta < 1/2$, matching calibration bounds hold. The bounds being *matching* means the number of noise intervals needed to guarantee calibration loss at most $\delta$ equals, up to constants, the number needed for information-theoretic identifiability of the model-relevant statistics. The scalings of D3–D4 are the $\delta$-independent backbone of these bounds; [1]'s abstract does not supply the $\delta$-dependent prefactor, so we do not state one.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

1. **Per-qubit $X$-error probability (computed).** For weak coherent $X$ rotation with $\theta = 10^{-2}$ rad, $p_X = \sin^2(\theta/2) \approx 2.5\times10^{-5}$ per qubit per interval (D1).

2. **Per-interval logical failure rate (computed, with symbolic code factor).** For $d_X = 3$, $p_L \approx C_3 \times 1.5625\times10^{-14}$ per interval, with $C_3$ the code's minimum-weight-logical multiplicity (D2). With $C_3 \leq 10^{2}$, $p_L \lesssim 1.5625\times10^{-12}$.

3. **Calibration cost, one-extraction schedule (computed from stated scaling).** $N_{\mathrm{cal}}^{(1)} \sim \theta^{-d_X}$; at $\theta = 10^{-2}$, $d_X = 3$: $10^{6}$ intervals; at $d_X = 5$: $10^{10}$ intervals (D3).

4. **Calibration cost, two-interval schedule (computed from stated scaling).** $N_{\mathrm{cal}}^{(2)} \sim \theta^{-2}$; at $\theta = 10^{-2}$: $10^{4}$ intervals, an improvement factor of $10^{2}$ at $d_X = 3$ and $10^{6}$ at $d_X = 5$ (D4).

5. **Worst-case model-agnostic fidelity (computed illustration of [1]'s bound).** With $F_{\mathrm{opt}} \approx 1 - C_3\times1.5625\times10^{-11}$ at $N_{\mathrm{int}} = 10^{3}$ (projection assuming interval-independent logical failures, stated in D5), the worst-case model-agnostic fidelity is $F_{\mathrm{agg}} \leq F_{\mathrm{opt}} - 1/2 \approx 0.499999998$ for $C_3 = 10^{2}$ (D5).

6. **Qualitative results from [1], restated without new numbers.** The fixed-sign and redrawn-sign models have identical syndrome statistics and the same SPP, yet require different logical corrections at suitable storage times; physical Pauli twirling of every interval changes both recovery performance and information requirements; discarding the record of applied random Pauli operations makes the SPP sufficient for optimal recovery, while keeping the record can improve attainable fidelity but may require additional noise information.

## 6. Discussion

**What the framework establishes.** The source work converts a folklore worry — correlated noise might confuse decoders — into a precise statement: there exist syndrome-indistinguishable noise models whose optimal logical corrections differ, and the fidelity price of ignorance is order one ($\to 1/2$), not perturbative. Equally important is the constructive side: the calibration cost is finite and scales as $\theta^{-d_X}$ (or $\theta^{-2}$ under relaxed extraction), so the required information is learnable in principle, and the extraction schedule is a genuine design lever.

**Limitations and failure modes.** First, the results are proved for a specific model pair (fixed versus redrawn shared sign under weak coherent $X$ rotations) on CSS codes with known system-environment interactions. The abstract of [1] does not state that the scalings extend to arbitrary correlated noise, partial knowledge of the interaction, or non-CSS codes; generalization is an open question. Second, our numerical illustrations (D1–D5) fix $\theta = 10^{-2}$ and $N_{\mathrm{int}} = 10^{3}$ by choice, and D5 additionally assumes interval-independent logical failures — an assumption the source work does not make and which may be false precisely because the noise is correlated; the projection should be read as an order-of-magnitude illustration only. Third, the combinatorial factor $C_{d_X}$ is left symbolic because [1] does not specify it; for large codes it could shift absolute numbers by orders of magnitude, though not the scalings. Fourth, the calibration bounds are stated for target loss $\delta < 1/2$; the behavior at $\delta \geq 1/2$ or the constants in the bounds are not supplied by the abstract.

**What would falsify the claims.** The indistinguishability claim would be falsified by exhibiting a decoder that, using only the syndrome record, achieves fidelity approaching the noise-aware optimum on both models at the relevant storage times — i.e., if the differing logical corrections could be resolved from syndrome data alone, the $1/2$ gap would collapse. The scaling claims would be falsified by calibration protocols achieving sub-$\theta^{-2}$ cost for this model pair, or by demonstrations that the $\theta^{-d_X}$ requirement is an artifact of the specific extraction schedule rather than a matching bound. The SPP-sufficiency claim would be falsified by a recovery strategy that beats SPP-based optimal recovery without using the record of applied random Pauli operations.

**Arguing against ourselves.** One might object that the worst-case $1/2$ loss is a minimax artifact: a Bayesian decoder with a prior over the two models would suffer at most half of that on average. [1]'s abstract reports worst-case results and does not state Bayesian averages, so we cannot adjudicate here; but an experimenter with a well-calibrated prior faces a materially smaller penalty, and the practical relevance of the worst-case bound depends on how adversarial the prior-free setting really is. A second objection: real experiments rarely have exactly known system-environment interactions, whereas the framework assumes them; robustness to interaction-model error is unaddressed in the supplied material. A third: the $\theta^{-2}$ improvement requires *two uninterrupted intervals before one extraction*, which changes the measurable syndrome stream; whether hardware timing constraints permit this in specific architectures is outside the supplied scope.

**Cost accounting context.** Entry [13] documents QEC overheads of $10^2$–$10^3$ physical operations per logical operation multiplying thermodynamic cost. Calibration adds a one-time (or periodic) cost of $10^{4}$–$10^{10}$ noise intervals depending on schedule and distance (D3–D4); whether this is amortizable over a memory's lifetime is an open economic question that the framework motivates but does not answer.

**Open questions.** (i) Do the matching calibration bounds extend to noise models with more than two sign hypotheses or spatially varying correlations? (ii) What is the optimal interpolation between the one-extraction and two-interval schedules? (iii) How do the results interact with physical twirling implemented in hardware, which [1] states changes both performance and information requirements? (iv) What are the $\delta$-dependent constants in the calibration bounds?

## 7. Conclusion

We have given a self-contained exposition of the decoder-knowledge question for temporally correlated noise posed and answered in arXiv:2610.03545v1. The core finding survives restatement in elementary terms: two noise models that are twins at the syndrome level — identical statistics, identical twirled Pauli process — can demand different logical corrections, and ignorance of which twin governs costs up to a fidelity factor approaching one half, even with the full syndrome record in hand. The price of knowledge is finite and characterizable: calibration costs scaling as $\theta^{-d_X}$ under standard extraction, reducible to $\theta^{-2}$ by batching two noise intervals per extraction — a factor of $10^{2}$ at distance 3 and $10^{6}$ at distance 5 for $\theta = 10^{-2}$. For the QEC engineering community, the message is that the extraction schedule and the record-keeping policy around applied Pauli operations are not implementation details but information-theoretic levers of first order. For the broader noise literature represented in the bibliography — from foundational questions about noise and reality [3], [7], through engineered noise correlations [8] and open-system dynamics [9], to memory hardware [6] and computation-cost accounting [13] — the source work supplies a concrete instance of a general principle: the gap between an experiment's empirical output and its statistical model has a price, and that price can be computed.

## References

[1] arXiv Query: search_query=&id_list=2610.03545&start=0&max_results=1 — "What must a quantum error-correction decoder know about temporally correlated noise, and what does it cost to learn?..." (fetched abstract of arXiv:2610.03545v1).

[2] arXiv:2610.03545v1 | What Must a Quantum-Memory Decoder Know About Temporally Correlated Noise?

[3] arXiv:1008.0667v2 | Noise and Bell's inequality

[4] arXiv:1310.1481v1 | Strongly correlated superconductivity

[5] arXiv:1612.01464v2 | Finite blocklength and moderate deviation analysis of hypothesis testing of correlated quantum states and application to classical-quantum channels with memory

[6] arXiv:1601.00157v1 | Theory of noise suppression in $\Lambda$-type quantum memories by means of a cavity

[7] arXiv:1612.03430v1 | Quantum and Classical Frontiers of Noise

[8] arXiv:2311.17794v1 | Noise Dynamics in the Quantum Regime

[9] arXiv:1605.07838v1 | Decoherence and noise in open quantum system dynamics

[10] QNFO: The Problem-Substrate Mapping: A Framework for Honest Computational Investment

[11] QNFO: Spectral Benchmarking of Holographic Quantum Simulations

[12] QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage?

[13] QNFO: The Physics of Computation: Fundamental Limits and the Honest Boundaries of Post-Classical Computing