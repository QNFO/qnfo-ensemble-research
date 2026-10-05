# Error Attribution as a Resource-Allocation Principle for Quantum Error Correction: An Analytical Study of Sensitivity-Guided Noise Reduction

## Abstract

Logical error rate is the standard benchmark for quantum error correction (QEC), but it is an aggregate quantity: it says nothing about which circuit components actually drive logical failure. Recent work introduced an error attribution scheme that computes component-level sensitivities of the logical error rate jointly from the Monte Carlo samples already used for benchmarking, and showed that halving noise on the few most sensitive components yields roughly twice the improvement of the same intervention applied at random locations [1]. In this paper we develop an analytical framework that makes the economics of attribution-guided intervention explicit. We model the logical error rate as a first-order expansion in component error probabilities, define sensitivity coefficients $s_i = \partial p_L / \partial \epsilon_i$, and derive closed-form expressions for the expected gain of targeted versus random noise reduction, the sample complexity of joint sensitivity estimation, and the scaling of gains with code distance. We work a fully explicit numerical example for a distance-3 rotated surface code memory, showing that a hotspot carrying a $15\%$ share of the logical error budget yields a $7.5\%$ logical error reduction when its noise is halved, versus a $2.94\%$ mean reduction from random selection — a $2.55\times$ advantage consistent in structure with the simulation findings of [1]. We situate attribution within the broader landscape of noise-aware QEC optimization [2,4,5,8], discuss coherent-error caveats [6], and identify failure modes of the first-order approach, including sensitivity redistribution under intervention and breakdown near threshold.

## 1. Introduction

Quantum error correction converts a noisy ensemble of physical qubits into a protected logical qubit whose quality is summarized by the logical error rate $p_L$. This single number is indispensable for comparing codes, decoders, and hardware platforms, but it is a severe compression of the underlying information. Two circuit locations with identical physical error probabilities can contribute very differently to logical failure: a data qubit at the code's geometric core participates in more stabilizer checks and more likely-error chains than an edge qubit; a particular ancilla placement may be disproportionately represented in decoder-confusing error configurations. Benchmarking by $p_L$ alone discards exactly the information a hardware engineer needs to decide where to spend a limited budget of calibration effort, better gates, or materials improvements.

Reference [1] addresses this gap with an error attribution scheme: using the same Monte Carlo samples that estimate $p_L$, it computes the sensitivity of $p_L$ to each physical circuit component, producing a sensitivity map that identifies hotspots. Simulations of rotated surface codes and lifted-product codes showed that halving the noise on roughly $5\%$–$7\%$ of components selected by sensitivity reduces $p_L$ by approximately $15\%$–$25\%$, about twice the reduction from randomly selected components [1]. This is a striking empirical result, but the structural reasons for the advantage — and the conditions under which it persists or collapses — benefit from analytical treatment.

This paper's contribution is an explicit analytical study of attribution-guided intervention. We (i) formalize the first-order attribution model and its sensitivity coefficients; (ii) derive the expected gain of targeted versus random intervention under stated assumptions; (iii) derive the Monte Carlo sample complexity of joint sensitivity estimation; (iv) work a complete numerical example with every arithmetic step shown; and (v) analyze failure modes, including the nonlinearity that arises when interventions are large or the code operates near threshold. Our aim is not to replace simulation but to give the practitioner scaling laws and back-of-envelope bounds that make attribution-based resource allocation predictable before committing simulation or laboratory time.

The paper is organized as follows. Section 2 reviews related work on noise-aware QEC optimization. Section 3 sets out the methods and formalism. Section 4 contains the derivations and the worked example. Section 5 reports results. Section 6 discusses limitations and falsifiability, and Section 7 concludes.

## 2. Background and Related Work

The idea that QEC should exploit knowledge of the actual noise, rather than correcting an abstract worst case, has a substantial history. Poulin et al. developed channel-optimized QEC, constructing recovery procedures tailored to a given noise channel and robust to uncertainties in that channel, demonstrating numerically that optimized procedures always outperform noise-agnostic standard error correction [2]. Attribution-guided intervention shares the philosophy of exploiting noise structure but operates at the level of hardware resource allocation rather than recovery-circuit design. Fletcher et al. similarly optimized QEC protocols for small-scale devices where dominant error sources are understood, arguing that known error structure is a resource [5]; sensitivity maps are precisely a systematic way of extracting that structure from benchmarking data itself.

A complementary line of work optimizes the code or its decomposition rather than the noise budget. Nautrup et al. used reinforcement learning to search over encodings adapted to unknown or device-specific error channels [4], and later applied deep reinforcement learning to discover autonomous QEC encodings for bosonic systems, where active measurement-based correction itself introduces errors [9]. Gaiotto-type gauge freedoms in QEC codes were exploited to find decompositions into elementary operations best matched to available experimental controls [8]. These approaches change the code; attribution changes where the hardware effort is spent, and the two are composable: a sensitivity map computed for an optimized encoding can still guide calibration priorities.

Erasure-biased qubits offer another targeted-intervention route: by converting unknown errors into flagged erasures, they reduce QEC overhead, at the cost of extra erasure-check operations that add noise and runtime [7]. The trade-off analysis in [7] is structurally similar to attribution economics — one pays overhead at specific circuit locations to buy disproportionate logical gains — and our framework can be viewed as a general method for locating where such conversions pay off most.

Attribution also interacts with error modeling. Fully coherent simulations of $d=3$ Steane and surface code circuits show that failure distributions under coherent errors differ markedly from those under stochastic models, with no simple mapping between the two [6]. This is a direct caveat for any sensitivity analysis calibrated under a stochastic Pauli noise model: sensitivities extracted under one noise family may not transfer to coherent-dominant regimes. On the foundations side, continuous-time QEC treats both noise and correction as processes continuous in time [10], a setting in which "component" attribution must be reinterpreted as attribution to continuous noise channels rather than discrete gate locations. Entanglement-assisted codes broaden the design space within which attribution could be applied [11], and survey treatments of QEC's implications for computing frame the benchmarking-to-optimization pipeline as part of the discipline's broader engineering maturation [12]. Finally, recent theoretical work on the tension between QEC and Quantum Darwinism, establishing a no-go tradeoff above critical logical fidelity $F_L > 0.874$ [13], is a reminder that logical performance metrics cannot be optimized in isolation from the information-theoretic role of the encoded system; we note this as context but it does not constrain the memory-experiment regime we study.

Our direct starting point is [1] (and its query-record form [3]), which supplies the attribution estimator and the empirical $2\times$ advantage that we aim to explain analytically.

## 3. Methods

### 3.1 Setting and notation

Consider a QEC memory experiment: a code $\mathcal{C}$ of distance $d$, a syndrome-extraction circuit with $M$ physical components (data-qubit locations, ancilla qubits, individual gates, or measurement events — the granularity is a modeling choice), and a decoder. Each component $i \in \{1,\dots,M\}$ has an error probability $\epsilon_i$. The logical error rate is

$$p_L(\boldsymbol{\epsilon}) = \Pr(\text{decoder output} \neq \text{encoded state}), \qquad \boldsymbol{\epsilon} = (\epsilon_1, \dots, \epsilon_M).$$

### 3.2 First-order attribution model

Define the sensitivity of component $i$ as

$$s_i \equiv \frac{\partial p_L}{\partial \epsilon_i}\bigg|_{\boldsymbol{\epsilon}_0},$$

evaluated at the operating point $\boldsymbol{\epsilon}_0$. For small interventions, the first-order expansion gives

$$\Delta p_L \approx \sum_{i=1}^{M} s_i \, \Delta \epsilon_i.$$

We define the attribution share of component $i$ as

$$f_i \equiv \frac{s_i \, \epsilon_i}{\sum_{j=1}^{M} s_j \, \epsilon_j}, \qquad \sum_i f_i = 1,$$

so that $f_i$ is the fraction of the logical error budget attributable to component $i$ under the linear model. Note $f_i$ combines sensitivity and exposure: a highly sensitive component with tiny $\epsilon_i$ may have a small share.

### 3.3 Intervention policies

An intervention halves the noise on a chosen set $S$ of $k$ components: $\epsilon_i \to \epsilon_i / 2$ for $i \in S$. Under the linear model,

$$\frac{\Delta p_L}{p_L} = -\frac{1}{2}\sum_{i \in S} f_i.$$

Two policies are compared:

- **Targeted:** choose the $k$ components with largest $f_i$.
- **Random:** choose $k$ components uniformly at random; the expected reduction is $\frac{1}{2}\sum_i f_i \cdot \frac{k}{M} = \frac{k}{2M}$.

The advantage ratio is

$$R \equiv \frac{\text{targeted reduction}}{\text{mean random reduction}} = \frac{M \sum_{i \in \text{top } k} f_i}{k}.$$

If shares were uniform ($f_i = 1/M$), $R = 1$ and attribution buys nothing; $R > 1$ measures the concentration of the error budget.

### 3.4 Monte Carlo estimation

Both $p_L$ and the $s_i$ are estimated from the same Monte Carlo run of $N$ circuit samples, following the joint-estimation principle of [1]. The logical error rate estimator $\hat{p}_L$ has relative standard error

$$\frac{\sigma(\hat{p}_L)}{p_L} = \sqrt{\frac{1 - p_L}{N p_L}} \approx \frac{1}{\sqrt{N p_L}},$$

and each sensitivity estimator inherits variance from the same sample budget; we derive the resulting requirement on $N$ in Section 4.

## 4. Analysis

### 4.1 Input numbers and their sources

We state every input number and its provenance:

1. **Code:** rotated surface code, distance $d = 3$, with $n_d = 9$ data qubits and $n_a = 8$ ancilla qubits, hence $M = 17$ components at data-qubit-plus-ancilla granularity. The qubit counts follow from the standard rotated surface code tiling at $d=3$ (standard construction; consistent with the rotated surface code memories simulated in [1]).
2. **Physical error probability:** $\epsilon = 10^{-3}$ per component, a representative near-term operating point (assumption; chosen for illustration).
3. **Subthreshold scaling amplitude and threshold:** $p_L \approx A \left(\epsilon / \epsilon_{\text{th}}\right)^{(d+1)/2}$ with $A = 0.1$ and $\epsilon_{\text{th}} = 10^{-2}$ (assumed values, standard phenomenological form; $A$ and $\epsilon_{\text{th}}$ are illustrative, not measured).
4. **Hotspot concentration:** the most sensitive component carries attribution share $f_{\max} = 0.15$ (assumption for the worked example; the empirical range in [1] — $15\%$–$25\%$ logical reduction from intervening on $5\%$–$7\%$ of components — motivates shares of this order).
5. **Intervention size:** $k = 1$ component out of $M = 17$, i.e., $k/M \approx 5.9\%$, matching the $5\%$–$7\%$ intervention fraction reported in [1].
6. **Monte Carlo budget target:** $10\%$ relative standard error on $\hat{p}_L$ (design requirement).

### 4.2 Logical error rate baseline

With $d = 3$, $\epsilon = 10^{-3}$, $\epsilon_{\text{th}} = 10^{-2}$, $A = 0.1$:

$$\frac{\epsilon}{\epsilon_{\text{th}}} = \frac{10^{-3}}{10^{-2}} = 10^{-1},$$

$$p_L \approx A \left(\frac{\epsilon}{\epsilon_{\text{th}}}\right)^{(d+1)/2} = 0.1 \times (10^{-1})^{2} = 0.1 \times 10^{-2} = 10^{-3}.$$

So the baseline logical error rate is $p_L = 10^{-3}$ per memory round.

### 4.3 Targeted intervention gain

Under the linear model with the hotspot share $f_{\max} = 0.15$, halving the noise on the top component gives

$$\frac{\Delta p_L}{p_L} = -\frac{1}{2} f_{\max} = -\frac{1}{2} \times 0.15 = -0.075,$$

so the logical error rate falls by $7.5\%$:

$$p_L^{\text{new}} = 10^{-3} \times (1 - 0.075) = 0.925 \times 10^{-3} = 9.25 \times 10^{-4}.$$

### 4.4 Random intervention gain

Randomly selecting $k = 1$ of $M = 17$ components, the expected reduction is

$$\frac{k}{2M} = \frac{1}{2 \times 17} = \frac{1}{34} \approx 0.02941,$$

i.e., a mean reduction of $2.94\%$:

$$p_L^{\text{rand}} = 10^{-3} \times \left(1 - \frac{1}{34}\right) = 10^{-3} \times \frac{33}{34} \approx 9.71 \times 10^{-4}.$$

### 4.5 Advantage ratio

$$R = \frac{0.075}{0.02941} = 0.075 \times 34 = 2.55.$$

Equivalently, $R = M f_{\max} / k = 17 \times 0.15 / 1 = 2.55$. The targeted policy is $2.55$ times more effective per component intervened upon — the same qualitative structure, and the same order of magnitude, as the approximately $2\times$ advantage observed in simulation in [1]. The gap between our $2.55\times$ and their $\approx 2\times$ is consistent with real sensitivity distributions being less concentrated at a single component than our single-hotspot assumption, spreading the top-$k$ mass across more components.

### 4.6 Scaling with distance

For $d = 5$ at the same $\epsilon$:

$$p_L(d{=}5) \approx 0.1 \times (10^{-1})^{3} = 10^{-4}.$$

Under the linear model, the *fractional* gain of an intervention is unchanged (it depends only on shares $f_i$), but the *absolute* gain shrinks proportionally: halving the hotspot now saves $0.075 \times 10^{-4} = 7.5 \times 10^{-6}$ in $p_L$, versus $7.5 \times 10^{-5}$ at $d = 3$. Conversely, near threshold the linear model fails: if $\epsilon = 5 \times 10^{-3}$, then $\epsilon/\epsilon_{\text{th}} = 0.5$ and

$$p_L \approx 0.1 \times (0.5)^{2} = 0.1 \times 0.25 = 2.5 \times 10^{-2},$$

at which point higher-order terms $\frac{1}{2}\sum_{i,j} \frac{\partial^2 p_L}{\partial \epsilon_i \partial \epsilon_j}\Delta\epsilon_i \Delta\epsilon_j$ are no longer negligible and first-order predictions overestimate linearity of response.

### 4.7 Sample complexity of joint estimation

To estimate $p_L = 10^{-3}$ with $10\%$ relative standard error:

$$\frac{1}{\sqrt{N p_L}} \le 0.1 \;\Rightarrow\; N \ge \frac{1}{0.01 \times 10^{-3}} = \frac{1}{10^{-5}} = 10^{5}.$$

So $N = 100{,}000$ samples suffice for the aggregate rate. For sensitivities, the key point of [1] is that the $s_i$ are extracted from the *same* samples, e.g., by conditioning statistics on the presence of specific component errors, so the marginal cost of the full sensitivity map is bookkeeping rather than additional simulation. A crude variance bound: if component $i$'s error appears in a fraction $\epsilon_i = 10^{-3}$ of samples, the effective number of informative samples for $s_i$ is $N \epsilon_i = 10^5 \times 10^{-3} = 100$, giving a relative statistical uncertainty of order $1/\sqrt{100} = 10\%$ on that component's conditional contribution — adequate for ranking hotspots, though insufficient for fine-grained ordering among near-tied components. Components with smaller $\epsilon_i$ proportionally fewer informative samples: at $\epsilon_i = 10^{-4}$, only $N\epsilon_i = 10$ informative samples and $\approx 32\%$ relative uncertainty ($1/\sqrt{10} \approx 0.316$).

### 4.8 Budget-concentration requirement

For the targeted policy to achieve a factor-$R$ advantage, the top $k$ shares must satisfy $\sum_{i \in \text{top }k} f_i = Rk/M$. For $R = 2$, $k/M = 0.05$, this requires the top $5\%$ of components to carry $\ge 10\%$ of the error budget — a mild concentration requirement, plausibly satisfied in real circuits given the empirical $15\%$–$25\%$ reductions in [1].

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; nothing is simulated or measured.

1. **Baseline logical error rate** (phenomenological model, $d=3$, $\epsilon = 10^{-3}$, $A = 0.1$, $\epsilon_{\text{th}} = 10^{-2}$): $p_L = 10^{-3}$ per round (Section 4.2).
2. **Targeted intervention:** halving noise on the single most sensitive component ($k/M \approx 5.9\%$ of components) reduces $p_L$ by $7.5\%$, to $9.25 \times 10^{-4}$ (Section 4.3).
3. **Random intervention:** the same intervention at a uniformly random component yields a mean reduction of $2.94\%$, to $\approx 9.71 \times 10^{-4}$ (Section 4.4).
4. **Advantage ratio:** $R = 2.55$ (Section 4.5), of the same order as the $\approx 2\times$ advantage observed in circuit simulation in [1].
5. **Distance scaling:** at $d = 5$, $p_L = 10^{-4}$; the fractional gain is unchanged but the absolute gain drops tenfold to $7.5 \times 10^{-6}$ (Section 4.6).
6. **Near-threshold breakdown:** at $\epsilon = 5 \times 10^{-3}$, $p_L \approx 2.5 \times 10^{-2}$ and first-order linearity is unreliable (Section 4.6).
7. **Sample complexity:** $N = 10^{5}$ Monte Carlo samples give $10\%$ relative error on $p_L$; per-component sensitivity estimates carry $\approx 10\%$ relative uncertainty at $\epsilon_i = 10^{-3}$ and $\approx 32\%$ at $\epsilon_i = 10^{-4}$ from the same sample budget (Section 4.7).
8. **Concentration requirement (projection):** assuming the empirical concentration levels of [1] persist, a $2\times$ advantage requires the top $5\%$ of components to carry $\ge 10\%$ of the attribution share; uncertainty in real concentration profiles is the dominant unknown and must be measured per device.

## 6. Discussion

**Limitations.** The first-order model is the central limitation. It assumes (i) small interventions, (ii) approximately independent component errors, and (iii) locally linear decoder response. Real syndrome-extraction circuits violate all three to some degree: errors correlate across shared ancillas, decoders are nonlinear maximum-likelihood objects, and a $2\times$ noise reduction on a hotspot is not infinitesimal. Near threshold (Section 4.6) the linear model degrades quantitatively, and the true gain of targeted intervention may be either larger (if hotspots are superlinear contributors) or smaller (if error chains re-route around the improved component, redistributing sensitivity). The single-hotspot worked example is deliberately stylized; real sensitivity distributions are continuous, and the top-$k$ advantage depends on the full ranked profile $f_{(1)} \ge f_{(2)} \ge \cdots$, not just $f_{\max}$.

**Failure modes.** First, *sensitivity redistribution*: after intervening on a hotspot, the attribution map changes, and a greedy iterate-intervene-recompute loop may oscillate or plateau; the framework gives no guarantee that greedy sequential intervention approaches the optimum of the constrained problem. Second, *model mismatch under coherent noise*: as [6] showed, coherent and stochastic error models produce markedly different failure distributions with no simple mapping between them, so sensitivities calibrated under a Pauli-twirled model may misrank components on coherent-noise hardware. Third, *estimation noise in the tail*: components with small $\epsilon_i$ have few informative Monte Carlo samples (Section 4.7), so the sensitivity ranking of low-exposure components is statistically fragile — precisely where a practitioner might be tempted to intervene on the map's fine structure. Fourth, *granularity choice*: attributing to data qubits versus individual gates versus measurement events changes both $M$ and the shares, and the optimal granularity for decision-making is device-dependent.

**What would falsify the claims.** The analytical claims here are conditional on the linear model and stated inputs; they are falsified if (a) circuit-level simulation with realistic noise shows that targeted intervention on sensitivity-ranked components yields no better than random improvement (contradicting both [1] and our $R > 1$ analysis), or (b) the advantage ratio $R$ fails to persist as $d$ grows, indicating that error-budget concentration is a small-code artifact. Our specific numerical example ($R = 2.55$) is falsified by any measured concentration profile in which the top component carries $f_{\max} \le 1/M \approx 0.059$, which would force $R \le 1$.

**Arguing against ourselves.** One might object that attribution is unnecessary because a hardware engineer already knows the worst components (e.g., the noisiest ancilla) and would fix them anyway. The counter-response is that physical error probability and logical sensitivity are distinct: the most *logically* damaging component need not be the most *physically* noisy, and only the product $s_i \epsilon_i$ ranks intervention value. A stronger objection: if sensitivities must be estimated per device via $10^5$-sample Monte Carlo runs, the approach may not scale to large codes where $p_L$ is tiny and $N$ explodes as $1/p_L$; at $p_L = 10^{-6}$, the same $10\%$ relative error requires $N = 10^{8}$ samples. Mitigations — importance sampling, conditioning estimators, and the joint-estimation trick of [1] — partially address this but remain an open engineering question.

**Open questions.** How do sensitivity profiles behave under code deformation and gauge choices [8]? Can attribution be performed online from syndrome statistics rather than offline simulation, connecting to continuous-time formulations [10]? Does the QEC–Darwinism tradeoff at high logical fidelity [13] constrain attribution-guided optimization in regimes where the encoded system also serves as an environment-monitoring resource? And can attribution-guided noise budgets be combined with reinforcement-learning code search [4,9] so that the agent optimizes over interventions rather than encodings?

## 7. Conclusion

We developed an analytical framework for error attribution in quantum error correction, making explicit the economics of sensitivity-guided noise reduction. Under a first-order model, the advantage of targeted over random intervention reduces to a concentration ratio $R = M \sum_{i \in \text{top }k} f_i / k$, which we evaluated in full for a distance-3 rotated surface code: a hotspot carrying $15\%$ of the error budget, intervened upon at the $5.9\%$ level, yields a $7.5\%$ logical error reduction versus a $2.94\%$ random-selection mean — a $2.55\times$ advantage, consistent in structure with the simulation findings of [1]. We derived the sample complexity of joint estimation ($N = 10^5$ for $10\%$ aggregate precision at $p_L = 10^{-3}$), quantified the statistical fragility of low-exposure sensitivities, and mapped the regime of validity of the linear approach, which breaks down near threshold. The framework converts attribution from an empirical observation into a predictable design tool: given a measured concentration profile, the practitioner can compute the expected return on calibration effort before spending it. Future work should validate the predicted scaling at larger distances and under coherent noise, and integrate attribution into closed-loop optimization pipelines.

## References

[1] arXiv Query: search_query=&id_list=2610.03399&start=0&max_results=1 — "Optimizing quantum error correction through error attribution" (abstract record).

[2] arXiv:0810.2524v1 | Channel-Optimized Quantum Error Correction.

[3] arXiv:2610.03399v1 | Optimizing quantum error correction through error attribution.

[4] arXiv:1812.08451v5 | Optimizing Quantum Error Correction Codes with Reinforcement Learning.

[5] arXiv:1909.05156v2 | Robustness-optimized quantum error correction.

[6] arXiv:1704.03961v1 | Quantum error correction failure distributions: comparison of coherent and stochastic error models.

[7] arXiv:2408.00829v3 | Optimizing quantum error correction protocols with erasure qubits.

[8] arXiv:1411.1779v2 | Optimized Quantum Error Correction Codes for Experiments.

[9] arXiv:2511.12482v2 | Discovering autonomous quantum error correction via deep reinforcement learning.

[10] arXiv:1311.2485v2 | Continuous-time quantum error correction.

[11] arXiv:1610.04013v1 | Entanglement-Assisted Quantum Error-Correcting Codes.

[12] QNFO: Implications for Computing and Quantum Error Correction | DOI 10.5281/zenodo.21979060.

[13] QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces | DOI 10.5281/zenodo.21964674.

[14] QNFO: Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology | DOI 10.5281/zenodo.21748299.