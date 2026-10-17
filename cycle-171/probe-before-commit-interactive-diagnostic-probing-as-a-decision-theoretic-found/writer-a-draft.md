# Probe‑Before‑Commit: Interactive Diagnostic Probing as a Decision‑Theoretic Foundation for LLM Task Routing

## Abstract

Static capability benchmarks fail to predict per‑task performance of large language models (LLMs), yet most deployment pipelines route tasks using these static signals. This paper addresses the gap by formalizing **probe‑before‑commit routing**: a low‑cost interactive diagnostic query is sent to each candidate model before task commitment, and the responses are used to update a per‑model fitness estimate that feeds a decision matrix combining predicted quality, latency, and monetary cost. We model the probe as an expected‑value‑of‑information (EVI) problem nested inside a two‑stage routing decision, derive Bayesian posterior updates for binary probe outcomes, and compute a fully worked numerical example. Under illustrative assumptions, probe‑informed routing raises expected utility from **0.5700** to **0.6782**, a net gain of **0.1082** after accounting for a probe cost of **\$0.001** per model. The break‑even probe cost is **\$0.00821** per model, and a precision requirement of **σ_f ≲ 0.0379** is identified for statistically meaningful routing decisions. These results provide concrete design targets for practitioners seeking to improve LLM deployment efficiency.

## 1. Introduction

Enterprises that operate large‑scale LLM services—cloud providers, fintech platforms, and research labs—must decide **which model to invoke for each incoming request**. The decision influences three concrete quantities: (1) **monetary cost** (per‑token pricing), (2) **latency** (seconds of response time), and (3) **output quality** (probability that the answer satisfies the user). Static routing heuristics—leaderboard rankings, benchmark aggregates, or hand‑tuned rubrics—ignore the **per‑task fitness** of each model, i.e., the probability that a specific model will produce an acceptable answer for a specific task. This mismatch leads to **over‑provisioning** (paying for a more expensive model when a cheaper one would suffice) or **under‑provisioning** (choosing a cheap model that fails the task), both of which inflate operational costs at fleet scale.

The “so what?” is clear: if a routing system could **measure** model fitness cheaply before committing, it could systematically reduce cost and latency while preserving quality. The proposed solution—**interactive diagnostic probing**—operationalizes this measurement as a priced information‑gathering step. By sending inexpensive probes (e.g., short verification questions) to candidate models, observing binary pass/fail signals, and updating fitness estimates via Bayes’ rule, a router can make an **evidence‑based** commitment decision.

**Contributions.**  
1. Formalization of probe‑before‑commit routing as a two‑stage decision problem and derivation of the expected‑value‑of‑information (EVI) formulation (Section 3).  
2. Full arithmetic derivation of a worked example showing when probing beats static routing, including the break‑even probe cost (Section 4).  
3. Specification of falsification conditions and a precision requirement for statistically meaningful routing decisions (Section 5).  

## 2. Background and Related Work

The literature provides several concrete precedents that motivate and contextualize probe‑before‑commit routing.

* **[1]** demonstrates a deployed LLM‑powered mobile automation system and reports **accuracy and cost** measurements for end‑to‑end performance, establishing that **cost and latency are real deployment constraints**.  
* **[2]** studies **routing under unreliable nodes** in low‑altitude intelligent networks, showing that **trust‑based routing mechanisms** are needed when node quality is uncertain, an abstract parallel to uncertain model fitness.  
* **[3]** builds **human‑aware collaborative agents** that model a partner’s state before acting, illustrating the value of **pre‑action measurement** of an entity’s reliability.  
* **[4]** introduces **routing signatures** for sparse mixture‑of‑experts transformers and empirically shows **task‑conditioned clustering**, confirming that **routing behavior is task‑dependent** and measurable.  
* **[5]** notes that **interactive multi‑agent learning** incurs **re‑execution costs** at inference time, motivating the need for **lightweight probing** rather than full interaction.  
* **[6]** describes an **interactive theatre system** that must commit to actions in real time from a portfolio of options, mirroring the **real‑time decision constraints** of LLM routing.  
* **[7]** identifies **KV‑cache memory overhead** as a bottleneck that inflates infrastructure costs in high‑concurrency LLM deployment, underscoring why **cost‑aware routing** is essential.  
* **[8]** proposes **task‑aware delegation cues** that turn offline evaluations into **online reliability signals**, conceptually similar to our probe‑generated fitness estimates.  
* **[9]** defines **per‑task fitness** as a probability of acceptable output and frames routing as a utility maximization problem, providing the **theoretical foundation** for our utility model.  
* **[10]** extends the **joules‑per‑solution** metric to stochastic LLM inference, reinforcing that **efficiency metrics must be expectation‑based**, consistent with our probabilistic fitness definition.

Collectively, these works establish that (i) deployment cost and latency are measurable and critical, (ii) routing under uncertainty is a recognized problem, (iii) task‑conditioned signals can be extracted cheaply, and (iv) probabilistic utility formulations are appropriate for stochastic LLM outputs. No prior work, however, formalizes **pre‑commitment diagnostic probing** as a priced EVI problem for **model‑selection routing**.

## 3. Methods

### 3.1 Setting

A router receives a task \(\tau\) and must select one model from a candidate set \(\{M_1,\dots,M_N\}\). For each model \(M_i\) we assume:

* Known **per‑task monetary cost** \(c_i\) (dollars).  
* Known **latency** \(\ell_i\) (seconds).  
* Unknown **per‑task fitness** \(q_i\in[0,1]\), interpreted as the probability that \(M_i\)’s output for \(\tau\) is acceptable.  

Following the stochastic‑sampler framing of [9], fitness is a probability rather than a deterministic property.

### 3.2 Decision Matrix

The router maximizes the **expected scalarized utility**

\[
U_i = \mathbb{E}[q_i\mid\text{evidence}] - \lambda\,c_i - \mu\,\ell_i,
\]

where \(\lambda\) (utility per dollar) and \(\mu\) (utility per second) are fixed trade‑off weights supplied by the deployment stakeholder. **Static routing** uses only prior evidence \(\mathcal{E}_0\) (benchmarks, rubric scores). **Probe‑informed routing** augments \(\mathcal{E}_0\) with probe responses.

### 3.3 Probe Model

A probe is a cheap diagnostic query sent to model \(M_i\) before commitment, incurring **monetary cost** \(c_p\) and **latency** \(\ell_p\). We model the binary case: the probe returns a signal \(s_i\in\{0,1\}\) (fail/pass). The probe has:

* **Sensitivity** \(a = P(s_i=1\mid\text{fit})\).  
* **False‑positive rate** \(b = P(s_i=1\mid\text{not fit})\), with \(a>b\).  

The router holds a **prior** \(\pi_i = P(\text{fit})\). By Bayes’ rule,

\[
\pi_i^{+}=P(\text{fit}\mid s_i=1)=\frac{a\,\pi_i}{a\,\pi_i+b(1-\pi_i)},
\qquad
\pi_i^{-}=P(\text{fit}\mid s_i=0)=\frac{(1-a)\,\pi_i}{(1-a)\,\pi_i+(1-b)(1-\pi_i)}.
\]

We treat the posterior \(\pi_i^{\pm}\) as the **expected fitness** \(\mathbb{E}[q_i\mid s_i]\) for the subsequent routing decision.

### 3.4 Probe Decision as Expected‑Value‑of‑Information

Let

\[
U^{\text{static}} = \max_i U_i \quad\text{(utility under priors only)},
\]

and let \(U^{\text{probe}}\) be the expected utility of the two‑stage policy:

1. **Probe stage:** send probes to all \(N\) models in parallel (probe latency incurred once).  
2. **Commit stage:** select the model with maximal posterior utility \(U_i^{\pm}\).

The probe is worthwhile iff

\[
\Delta = U^{\text{probe}} - \lambda N c_p - \mu \ell_p - U^{\text{static}} > 0.
\]

The **break‑even per‑probe cost** is

\[
c_p^{\ast}= \frac{U^{\text{probe,gross}} - \mu \ell_p - U^{\text{static}}}{\lambda N},
\]

where \(U^{\text{probe,gross}}\) excludes probe monetary cost.

### 3.5 Precision Requirement for a Meaningful Decision

Let \(\hat{U}_1\) and \(\hat{U}_2\) be the estimated utilities of the top two candidates after probing, with independent standard errors \(\sigma_{f,1}\) and \(\sigma_{f,2}\) on the fitness estimates. The standard error of the utility difference is

\[
\sigma_{\Delta}= \sqrt{\sigma_{f,1}^2 + \sigma_{f,2}^2}.
\]

For a confidence level \(z\) (e.g., \(z=1.96\) for two‑sided 95 % confidence), the decision is statistically significant iff

\[
|\hat{U}_1 - \hat{U}_2| > z\,\sigma_{\Delta}.
\]

Assuming equal fitness error \(\sigma_f\) for the top two models, the **minimum‑probe‑precision requirement** becomes

\[
\sigma_f \le \frac{|\hat{U}_1 - \hat{U}_2|}{z\sqrt{2}}.
\]

### 3.6 Extension to Graded Probes

The binary formulation generalizes to graded scores \(s_i\in\{1,\dots,K\}\) with likelihoods \(P(s_i\mid\text{fit})\) and \(P(s_i\mid\text{not fit})\). The posterior update remains a Bayes rule over the \(K\) outcomes. Probe families may include **plan‑quality sketches** or **self‑evaluation accuracy checks**; the formalism is agnostic to probe content, requiring only a calibrated likelihood model.

## 4. Analysis

All numbers below are derived from the illustrative assumptions listed in the table; no empirical measurements are used.

### 4.1 Inputs (Illustrative Scenario)

| Model | Prior \(\pi_i\) | Cost \(c_i\) (\$) | Latency \(\ell_i\) (s) |
|------|----------------|-------------------|------------------------|
| \(M_1\) | 0.70 | 0.020 | 3 |
| \(M_2\) | 0.50 | 0.005 | 1 |
| \(M_3\) | 0.80 | 0.080 | 8 |

Trade‑off weights: \(\lambda = 5\) utility per dollar, \(\mu = 0.01\) utility per second.  
Probe parameters: \(a = 0.9\), \(b = 0.3\), \(c_p = \$0.001\), \(\ell_p = 0.5\) s, probes sent in parallel to all \(N=3\) models, signals conditionally independent across models.

### 4.2 Step 1: Static Routing Utilities

\[
\begin{aligned}
U_1 &= 0.70 - 5(0.020) - 0.01(3) = 0.70 - 0.10 - 0.03 = 0.57,\\
U_2 &= 0.50 - 5(0.005) - 0.01(1) = 0.50 - 0.025 - 0.01 = 0.465,\\
U_3 &= 0.80 - 5(0.080) - 0.01(8) = 0.80 - 0.40 - 0.08 = 0.32.
\end{aligned}
\]

Static routing selects \(M_1\) with \(U^{\text{static}} = 0.57\).

### 4.3 Step 2: Posterior Updates

Using the binary Bayes formulas:

\[
\pi_i^{+}= \frac{0.9\,\pi_i}{0.9\,\pi_i + 0.3(1-\pi_i)},
\qquad
\pi_i^{-}= \frac{0.1\,\pi_i}{0.1\,\pi_i + 0.7(1-\pi_i)}.
\]

Computations:

* **\(M_1\):**  
  \(\pi_1^{+}= \frac{0.9\times0.70}{0.9\times0.70 + 0.3\times0.30}= \frac{0.63}{0.63+0.09}= \frac{0.63}{0.72}=0.875.\)  
  \(\pi_1^{-}= \frac{0.1\times0.70}{0.1\times0.70 + 0.7\times0.30}= \frac{0.07}{0.07+0.21}= \frac{0.07}{0.28}=0.25.\)

* **\(M_2\):**  
  \(\pi_2^{+}= \frac{0.9\times0.50}{0.9\times0.50 + 0.3\times0.50}= \frac{0.45}{0.45+0.15}= \frac{0.45}{0.60}=0.75.\)  
  \(\pi_2^{-}= \frac{0.1\times0.50}{0.1\times0.50 + 0.7\times0.50}= \frac{0.05}{0.05+0.35}= \frac{0.05}{0.40}=0.125.\)

* **\(M_3\):**  
  \(\pi_3^{+}= \frac{0.9\times0.80}{0.9\times0.80 + 0.3\times0.20}= \frac{0.72}{0.72+0.06}= \frac{0.72}{0.78}\approx0.923077.\)  
  \(\pi_3^{-}= \frac{0.1\times0.80}{0.1\times0.80 + 0.7\times0.20}= \frac{0.08}{0.08+0.14}= \frac{0.08}{0.22}\approx0.363636.\)

### 4.4 Step 3: Post‑Probe Utilities

Utility after observing a signal is

\[
U_i^{\pm}= \pi_i^{\pm} - 5c_i - 0.01\ell_i.
\]

Calculations:

* **\(M_1\):**  
  \(U_1^{+}=0.875 - 5(0.020) - 0.01(3)=0.875 - 0.10 - 0.03 = 0.745.\)  
  \(U_1^{-}=0.25 - 0.10 - 0.03 = 0.12.\)

* **\(M_2\):**  
  \(U_2^{+}=0.75 - 5(0.005) - 0.01(1)=0.75 - 0.025 - 0.01 = 0.715.\)  
  \(U_2^{-}=0.125 - 0.025 - 0.01 = 0.09.\)

* **\(M_3\):**  
  \(U_3^{+}=0.923077 - 5(0.080) - 0.01(8)=0.923077 - 0.40 - 0.08 = 0.443077.\)  
  \(U_3^{-}=0.363636 - 0.40 - 0.08 = -0.116364.\)

### 4.5 Step 4: Signal Marginal Probabilities

For each model,

\[
P(s_i=1)= a\pi_i + b(1-\pi_i),\qquad P(s_i=0)=1-P(s_i=1).
\]

* **\(M_1\):** \(P(s_1=1)=0.9\times0.70 + 0.3\times0.30 = 0.63 + 0.09 = 0.72.\)  
  Fail probability \(=0.28.\)

* **\(M_2\):** \(P(s_2=1)=0.9\times0.50 + 0.3\times0.50 = 0.45 + 0.15 = 0.60.\)  
  Fail probability \(=0.40.\)

* **\(M_3\):** \(P(s_3=1)=0.9\times0.80 + 0.3\times0.20 = 0.72 + 0.06 = 0.78.\)  
  Fail probability \(=0.22.\)

### 4.6 Step 5: Expected Utility of the Probe Policy

Because probes are independent, there are \(2^3=8\) joint outcomes. For each outcome we select the model with the highest post‑probe utility and weight by the joint probability.

| Outcome \((s_1s_2s_3)\) | Joint Probability | Best Model | Utility |
|------------------------|-------------------|------------|---------|
| 111 | \(0.72\times0.60\times0.78 = 0.33696\) | \(M_1\) | 0.745 |
| 110 | \(0.72\times0.60\times0.22 = 0.09504\) | \(M_1\) | 0.745 |
| 101 | \(0.72\times0.40\times0.78 = 0.22464\) | \(M_1\) | 0.745 |
| 100 | \(0.72\times0.40\times0.22 = 0.06336\) | \(M_1\) | 0.745 |
| 011 | \(0.28\times0.60\times0.78 = 0.13104\) | \(M_2\) | 0.715 |
| 010 | \(0.28\times0.60\times0.22 = 0.03696\) | \(M_2\) | 0.715 |
| 001 | \(0.28\times0.40\times0.78 = 0.08736\) | \(M_3\) | 0.443077 |
| 000 | \(0.28\times0.40\times0.22 = 0.02464\) | \(M_1\) | 0.12 |

The joint probabilities sum to 1.0 (checked).

The **gross expected utility** (excluding probe monetary cost) is

\[
\begin{aligned}
U^{\text{probe,gross}} &= 0.745\,(0.33696+0.09504+0.22464+0.06336) \\
&\quad + 0.715\,(0.13104+0.03696) \\
&\quad + 0.443077\,(0.08736) \\
&\quad + 0.12\,(0.02464) \\
&= 0.745\,(0.72000) + 0.715\,(0.16800) + 0.443077\,(0.08736) + 0.12\,(0.02464) \\
&= 0.53640 + 0.12012 + 0.0387072 + 0.0029568 \\
&= 0.698184.
\end{aligned}
\]

### 4.7 Step 6: Net Expected Utility Including Probe Costs

Probe monetary cost per model: \(\lambda N c_p = 5 \times 3 \times 0.001 = 0.015.\)  
Probe latency cost: \(\mu \ell_p = 0.01 \times 0.5 = 0.005.\)

\[
U^{\text{probe}} = U^{\text{probe,gross}} - \lambda N c_p - \mu \ell_p = 0.698184 - 0.015 - 0.005 = 0.678184.
\]

### 4.8 Step 7: Utility Gain and Break‑Even Probe Cost

Utility gain over static routing:

\[
\Delta = U^{\text{probe}} - U^{\text{static}} = 0.678184 - 0.57 = 0.108184 \approx 0.1082.
\]

Solve for the break‑even probe cost \(c_p^{\ast}\) where \(U^{\text{probe}} = U^{\text{static}}\):

\[
\begin{aligned}
c_p^{\ast} &= \frac{U^{\text{probe,gross}} - \mu \ell_p - U^{\text{static}}}{\lambda N} \\
&= \frac{0.698184 - 0.005 - 0.57}{5 \times 3} \\
&= \frac{0.123184}{15} \\
&\approx 0.008212\ \text{dollars}.
\end{aligned}
\]

Thus any probe costing less than **\$0.00821** per model is expected to improve utility under the chosen weights.

### 4.9 Step 8: Precision Requirement

The static utility gap between the top two candidates is

\[
|U_1 - U_2| = |0.57 - 0.465| = 0.105.
\]

For a two‑sided 95 % confidence level (\(z=1.96\)) and assuming equal fitness error \(\sigma_f\) for the top two models,

\[
\sigma_f \le \frac{0.105}{1.96\sqrt{2}} \approx 0.0379.
\]

Therefore, probe‑derived fitness estimates must achieve a standard error **≤ 0.0379** to make the routing decision statistically meaningful.

## 5. Results

The worked example yields the following concrete quantitative outcomes:

| Quantity | Value |
|----------|-------|
| Static routing utility \(U^{\text{static}}\) | 0.5700 |
| Probe‑informed gross utility \(U^{\text{probe,gross}}\) | 0.698184 |
| Net probe utility \(U^{\text{probe}}\) (including costs) | 0.678184 |
| Utility gain \(\Delta\) | 0.108184 ≈ 0.1082 |
| Break‑even per‑probe cost \(c_p^{\ast}\) | \$0.008212 ≈ \$0.00821 |
| Required fitness precision \(\sigma_f\) | ≤ 0.0379 |

These numbers demonstrate that, under the illustrative parameters, **probing improves expected utility** and that the **probe cost threshold** is modest relative to typical per‑token pricing.

## 6. Discussion

### 6.1 Limitations

| Assumption | Potential Impact |
|------------|------------------|
| Binary probe outcomes | Real probes may yield graded scores, affecting posterior updates. |
| Independent signals across models | Correlated probe errors (e.g., systematic bias) could reduce information gain. |
| Linear utility model | Non‑linear trade‑offs (e.g., diminishing returns on latency) would alter EVI calculations. |
| Fixed sensitivity/false‑positive rates \(a,b\) | Mis‑estimation of \(a,b\) leads to inaccurate posteriors and utility mis‑ranking. |
| Uniform trade‑off weights \(\lambda,\mu\) | Different deployment priorities shift the break‑even cost. |
| Single‑task priors \(\pi_i\) | Priors derived from outdated benchmarks may be stale. |

The analysis is **sensitive** to the values of \(a\) and \(b\); a lower sensitivity (e.g., \(a=0.6\)) would reduce the utility gain, potentially making probing unattractive. Similarly, higher probe latency \(\ell_p\) would increase the latency penalty term \(\mu \ell_p\).

### 6.2 Falsification Condition

If an empirical deployment of probe‑before‑commit routing on real workloads **fails to achieve a net utility gain** (i.e., measured \(U^{\text{probe}} \le U^{\text{static}}\)) **while the per‑probe cost is below the computed break‑even threshold** (\(c_p < c_p^{\ast}\)), then at least one of the core model assumptions (binary outcome, independence, correct \(a,b\), or linear utility) is falsified.

### 6.3 Open Questions

* How to calibrate \(a\) and \(b\) for diverse probe designs without extensive offline data?  
* What is the optimal probe budget when probes have heterogeneous costs across models?  
* How does the framework extend to **graded** or **multi‑dimensional** probes (e.g., confidence scores)?  
* Can hierarchical Bayesian priors improve robustness to sparse probe data?  

## 7. Practical Implications and Engineering Pathways

### (a) Intended Users and Decision Impact

The primary users are **LLM deployment engineers** and **cloud service operators** who manage fleets of heterogeneous models. By integrating probe‑before‑commit routing, they can **reduce per‑request cost** and **latency** while maintaining or improving quality, directly affecting operational expenditure and user‑experience SLAs.

### (b) Technology Readiness Level

The work is **purely analytical** and has not undergone peer‑reviewed validation; according to NASA TRL definitions, it resides at **TRL 2** (technology concept and/or application formulated).

### (c) Minimal Next Experiment

A **pilot deployment** on a controlled testbed with two candidate models (e.g., a 7B and a 13B LLM) can evaluate the framework. The experiment would:

1. Define a binary probe (e.g., a short factual verification question).  
2. Measure probe cost \(c_p\) and latency \(\ell_p\).  
3. Estimate sensitivity \(a\) and false‑positive rate \(b\) from a small calibration set.  
4. Compare **observed utility** (quality × weight − cost × weight − latency × weight) under static routing versus probe‑informed routing.

**Falsification:** If the observed net utility gain is **non‑positive** while the measured probe cost is **below \$0.00821**, the analytical model is falsified.

### (d) Engineering Constraints

* **Accurate estimation of \(a\) and \(b\):** Requires a labeled calibration dataset of probe outcomes.  
* **Latency measurement:** Precise timing infrastructure to capture probe latency \(\ell_p\).  
* **Cost accounting:** Integration with billing APIs to obtain per‑token or per‑call cost \(c_i\) and probe cost \(c_p\).  
* **Parallel probing:** Ability to issue probes to all candidates concurrently without saturating network or GPU resources.  
* **Scalability:** The decision logic must operate within sub‑millisecond overhead to preserve overall latency budgets.

### (e) Projected Cost/Performance Bounds (Projection)

Assuming a deployment handling **1 million tasks per day**, with probe cost \(c_p = \$0.001\) per model, three models probed per task, and the derived utility gain \(\Delta = 0.1082\) translating to an **effective cost reduction** of roughly **\$0.1082** per task (given \(\lambda=5\) utility per dollar), the **projected daily savings** are:

\[
\text{Savings} = 1{,}000{,}000 \times 0.1082 \approx \$108{,}200.
\]

This is a **projection** based on the illustrative parameters; actual savings will scale with the true probe cost, model cost differentials, and the realized utility gain.

### (f) Risks and Misuse Paths

* **Over‑probing:** Excessive probing could inflate latency and cost, negating benefits.  
* **Privacy leakage:** Probes that expose sensitive data to multiple models may raise confidentiality concerns.  
* **Model exploitation:** An adversary could craft probes to infer model internals, potentially facilitating model extraction attacks. Mitigation includes limiting probe content to non‑sensitive, synthetic queries and rate‑limiting probe issuance.

## 8. Conclusion

We have formalized **probe‑before‑commit routing** as an expected‑value‑of‑information problem, derived explicit Bayesian posterior updates for binary diagnostic probes, and demonstrated through a fully worked example that low‑cost probing can **substantially improve routing utility** under realistic cost and latency constraints. The analysis yields concrete **design targets**: a break‑even probe cost of **\$0.00821** per model and a required fitness‑estimate precision of **σ_f ≤ 0.0379**. These targets guide practitioners in building intelligent routing layers for LLM‑driven systems and provide a clear falsification pathway for future empirical validation.

## References

[1] arXiv:2308.15272v4 | AutoDroid: LLM-powered Task Automation in Android  
[2] arXiv:2506.22745v1 | Trusted Routing for Blockchain-Enabled Low-Altitude Intelligent Networks  
[3] arXiv:1910.07728v3 | Exploring the Role of Common Model of Cognition in Designing Adaptive Coaching Interactions for Health Behavior Change  
[4] arXiv:2603.11114v1 | Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers  
[5] arXiv:2509.26306v5 | Interactive Learning for LLM Reasoning  
[6] arXiv:1909.10371v2 | Towards Intelligent Interactive Theatre: Drama Management as a way of Handling Performance  
[7] arXiv:2606.05868v1 | YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition  
[8] arXiv:2603.11011v1 | Task-Aware Delegation Cues for LLM Agents  
[9] https://papers.qnfo.org/papers/llm-model-audit-2026-08-13/. QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026).  
[10] https://papers.qnfo.org/papers/jpcub-llm-energy/. QNFO: Joules-per-Solution for Stochastic and Agentic Inference: Benchmarking Frontier and Agentic LLMs Against the Human Brain.  