# Probe-Then-Route: Interactive Diagnostic Probing as a Low-Cost Operationalization of Intelligent LLM Task Routing

## Abstract

Static capability benchmarks poorly predict per-task performance of large language models (LLMs), and deployed routing heuristics are rarely grounded in measured fitness for the specific task at hand. We propose operationalizing "intelligent routing" as a low-cost interactive probe: before committing a task to a production model, the router sends a small set of cheap diagnostic queries to each candidate model, extracts a fitness score from the responses (plan quality, self-evaluation accuracy), and routes using a decision matrix that combines predicted quality, latency, and cost. We formalize the probe as a bandit-style decision problem with an explicit value-of-information condition, define a linear fitness-to-utility map, and derive closed-form break-even conditions under which probe-informed routing beats static rubric routing. A fully worked numerical example shows a case in which static benchmark routing selects the wrong model: the utility-optimal candidate dominates by $\Delta U = 0.14$ per task, while the probe costs $0.006$ per routing decision, yielding a net gain of $0.134$ per task and a break-even probe budget of up to $70$ diagnostic queries. A significance analysis shows the routing decision is not statistically separable at naive probe precision, motivating a minimum-probe-precision requirement. We position the framework against routing, delegation-cue, and efficiency literature and state falsification conditions.

## 1. Introduction

Organizations that deploy large language models increasingly face a portfolio problem: many candidate models, many heterogeneous tasks, and no reliable a priori map from task to best model. Static benchmarks summarize aggregate capability, but aggregate rank order is a poor predictor of which model will succeed on a particular task instance. Meanwhile, routing heuristics in production systems are often based on prompt surface features or cost tiers rather than on any measured estimate of how well a candidate model would actually perform on the task being routed.

This paper asks whether "intelligent routing" can be operationalized as a low-cost interactive procedure. The core idea, from the originating research proposal, is simple: before committing, send cheap diagnostic queries (probes) to candidate models, use the responses to estimate each model's fitness for the task, and then route based on a decision matrix combining predicted quality, latency, and cost. The proposal further suggests formalizing the probe as a bandit or decision-tree problem, defining a fitness score from probe responses (for example, plan quality or self-evaluation accuracy), and testing whether probe-informed routing beats static rubric routing on cost- and quality-optimized metrics across diverse task suites.

Our contribution is a formalization and a fully explicit numerical analysis, not an empirical benchmark. We treat this as a design-theory paper: we state the decision problem, derive the conditions under which probing pays, and work one example end-to-end with every arithmetic step shown, so that future empirical work has a precise target to confirm or refute. Three questions organize the paper:

1. What is the minimal formal structure of a probe-then-route decision, and what is the value of probe information?
2. Under what conditions does probe-informed routing strictly dominate static rubric routing?
3. How much probe precision is needed before a routing decision is statistically meaningful?

The stakes are practical. As efficiency-focused work on LLM deployment emphasizes, serving costs and latency constraints — for example, KV-cache memory overhead that "inflates infrastructure costs and throttles scalability" in high-concurrency settings [7] — mean that the difference between routing to an adequate cheap model and an over-provisioned expensive one compounds at fleet scale. Conversely, audits of the frontier model landscape show that aggregate benchmark rank can be misleading for specific use classes; the QNFO LiveBench-grounded audit reports, for instance, that no Llama model ranks in the top 42 on its mathematics-heavy suite and identifies a specific model as the mathematics price-performance option [9] — a finding that itself illustrates why per-task fitness, not family reputation, should drive routing.

## 2. Background and Related Work

We review the supplied bibliography, which spans LLM task automation, network routing, adaptive agent interaction, mixture-of-experts routing, inference-time interaction, deployment efficiency, delegation cues, and benchmark auditing. Two entries ([11], [12]) have empty supplied summaries; we note this explicitly and use them only as pointer citations.

**LLM task automation.** AutoDroid addresses LLM-powered task automation on Android, motivated by the observation that existing approaches "suffer from poor scalability due to the limited language understanding ability and the non-trivial manual efforts required from developers or end-users," and leveraging recent advances in LLM language understanding and reasoning [1]. AutoDroid is relevant to us as an instance of the general problem our router addresses: an LLM-driven system must decide how to execute a user task, and its effectiveness depends on task-specific language understanding — exactly the per-task fitness quantity our probes are designed to estimate. The supplied summary does not describe a routing mechanism, so we cite it only as problem context.

**Routing under adversarial or dynamic conditions.** Trusted Routing for Blockchain-Enabled Low-Altitude Intelligent Networks studies routing in networks where UAVs have "distributed topology and high dynamic mobility" and are "vulnerable to security threats, which may degrade the routing performance for data transmission" [2]. The structural analogy is direct: routing decisions must be made from incomplete, possibly degraded information about candidate nodes (in our case, candidate models), and the routing layer must be robust to noise in the signals it uses. The supplied summary is truncated and does not state the paper's solution method, so we draw only this structural parallel.

**Modeling the counterpart before acting.** The adaptive-coaching work explores how "intelligent collaborative agents that are human-aware — they can model, learn, and reason about their human partner's physiological, cognitive, and affective states" can design adaptive coaching interactions for health behavior change, using the common model of cognition (CMC) as a framework [3]. This is the closest conceptual ancestor of our probe: before choosing how to act, the agent builds a model of the counterpart it will act with. Our proposal replaces the human partner with a candidate LLM and replaces the cognitive model with a measured fitness estimate from diagnostic responses.

**Intra-model routing as an open problem.** Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers introduces "routing signatures, a vector representation summarizing expert activation patterns across layers for a given prompt," motivated by the fact that MoE "routing mechanisms responsible for expert selection remain poorly understood" [4]. This work studies routing inside a model as a function of the task; our work studies routing between models as a function of the task. The shared thesis — that routing behavior is task-conditioned and should be measured, not assumed — is the empirical premise our probe operationalizes at the model-selection level.

**Inference-time interaction.** Interactive Learning for LLM Reasoning develops "interactive training environments to explicitly promote collaboration among multiple Large Language Models," building stronger multi-agent systems, but notes that "during inference, they require re-executing the MAS to obtain final solutions," which "diverges from human cognition" [5]. Our probe shares the interactive spirit but is deliberately cheaper and non-re-executive: the probe is a lightweight pre-commitment measurement, not a full multi-agent execution, precisely to avoid the re-execution cost that [5] identifies as a divergence from efficient inference.

**Interactive decision-making agents.** Towards Intelligent Interactive Theatre presents "a new modality for intelligent interactive narratives within the theatre domain," with "an intelligent agent that serves as a drama manager and as an actor," and poses "a set of research challenges" arising from that analysis [6]. The supplied summary gives no quantitative or algorithmic detail; we cite it as an example of the drama-manager pattern — an agent that dynamically selects the next action from a portfolio — which is the control pattern our router instantiates with models as the action portfolio.

**Deployment cost as a first-class constraint.** YouZhi targets "high-concurrency deployment" of financial LLMs, "severely bottlenecked by KV cache memory overhead, which inflates infrastructure costs and throttles scalability," via an adaptive GQA-to-MLA structural transition [7]. For our purposes, YouZhi represents the supply side of the routing decision: latency and cost differences between candidate serving configurations are real, large, and structural, which is why our decision matrix must weight cost and latency alongside quality rather than treating quality alone as the objective.

**Delegation cues — the nearest neighbor.** Task-Aware Delegation Cues for LLM Agents diagnoses that "human–agent teamwork remains brittle due to information asymmetry: users lack task-specific reliability cues, and agents rarely surface calibrated uncertainty or rationale," and proposes "a task-aware collaboration signaling layer that turns offline preference evaluations into online, user-facing primitives for delegation" [8]. Our probe-then-route framework can be read as the system-level dual of [8]: where [8] converts offline evaluations into online cues for the human delegator, we convert online probe responses into fitness estimates for an automated router. Both attack the same information asymmetry — no task-specific reliability signal at decision time.

**Static benchmarks and their limits.** The QNFO audit of the frontier LLM landscape (August 2026) is "grounded in the LiveBench 2026-06-25 contamination-free benchmark" and reports that "no Llama model ranks in the top 42" and that "DeepSeek V4 Pro 0813 is the mathematics price-performance o[ption]" [9]. This is the strongest supplied evidence for our motivating claim: even a careful, contamination-free static benchmark yields a coarse aggregate ordering, and price-performance-adjusted conclusions diverge from raw capability ordering. Our framework treats such benchmark results as priors over model fitness, to be refined by probes rather than replaced.

**Efficiency metrics for stochastic solvers.** The joules-per-solution (J/S) work states that the J/S metric "assumed deterministic solvers: one run yields one solution," and that LLMs "violate that assumption twice over: they are stochastic samplers whose outputs m[ust be...]" [10]. The supplied summary is truncated mid-sentence, so we cannot state the paper's resolution; we use only its stated premise — that LLMs are stochastic samplers, complicating per-solution efficiency accounting — as motivation for treating probe-estimated quality as an expectation rather than a deterministic quantity, and for the variance analysis in Section 4.

**Pointer citations.** Comprehensive Technical Framework for Network Isomorphism [11] and Syntactic Generation [12] are supplied with empty summaries; the entries provide no substantive content, and we make no claims about their contents. We note their presence as a limitation of the supplied corpus.

## 3. Methods

### 3.1 Decision setting

Let $\mathcal{M} = \{M_1, \dots, M_K\}$ be candidate models and $\tau$ a task instance arriving at the router. Each model $M_i$ has a task-conditional quality $q_i(\tau) \in [0,1]$ (e.g., grader-scored correctness), a serving cost $c_i(\tau)$ in dollars per task, and a latency $\ell_i(\tau)$ in seconds. The router's utility for assigning $\tau$ to $M_i$ is

$$U_i(\tau) = q_i(\tau) - \lambda_c\, c_i(\tau) - \lambda_\ell\, \ell_i(\tau),$$

where $\lambda_c$ (in $\$^{-1}$) and $\lambda_\ell$ (in $\mathrm{s}^{-1}$) are the operator's quality-cost and quality-latency exchange rates. Static rubric routing selects

$$i^{\mathrm{static}} = \arg\max_i \; \hat{q}_i^{\mathrm{bench}} - \lambda_c\, c_i - \lambda_\ell\, \ell_i,$$

where $\hat{q}_i^{\mathrm{bench}}$ is a benchmark-derived score that is not measured on $\tau$ itself.

### 3.2 The probe

A probe is a cheap diagnostic query $p_j$ derived from the task specification $\tau$ (e.g., "outline your plan for this task," "state the key difficulty," or a self-check on a sub-answer). Sending probe set $P = \{p_1,\dots,p_n\}$ to model $M_i$ costs $c^{\mathrm{probe}}_{i}(P)$ and yields responses from which the router computes a fitness estimate

$$\hat{f}_i = g\big(r_{i,1}, \dots, r_{i,n}\big),$$

where $g$ maps probe responses (plan quality scores, self-evaluation accuracy) to a scalar in $[0,1]$ with standard error $\sigma_{f,i}$. The probe-informed router selects

$$i^{\mathrm{probe}} = \arg\max_i \; \hat{f}_i - \lambda_c\, c_i - \lambda_\ell\, \ell_i.$$

The probe is a bandit-style pure-exploration step: it purchases information about all arms before a single commitment, rather than learning by committing.

### 3.3 Value of probe information

Define the probe cost $C_P = \sum_i c^{\mathrm{probe}}_i(P)$ and the decision gap

$$\Delta U = U_{i^{\mathrm{probe}}} - U_{i^{\mathrm{static}}}.$$

Probe-informed routing is net-beneficial on a task iff

$$\Delta U > C_P.$$

For a routing decision to be statistically meaningful, the utility gap between the top two candidates must exceed the decision noise. With independent fitness standard errors $\sigma_{f,1}, \sigma_{f,2}$ for the top two candidates, the standard error of the utility difference is

$$\sigma_\Delta = \sqrt{\sigma_{f,1}^2 + \sigma_{f,2}^2},$$

and the decision is significant at confidence level $z$ (e.g., $z = 1.96$ for two-sided 95%) iff

$$|\hat{U}_1 - \hat{U}_2| > z\,\sigma_\Delta.$$

This yields a minimum-probe-precision requirement: probes must reduce $\sigma_f$ below $|\hat{U}_1 - \hat{U}_2| / (z\sqrt{2})$ for the routing decision to be trustworthy.

### 3.4 Break-even conditions

Routing to the cheaper model $M_2$ over the higher-benchmark model $M_1$ is utility-optimal iff

$$q_1 - q_2 < \lambda_c (c_1 - c_2) + \lambda_\ell (\ell_1 - \ell_2).$$

The right-hand side is the cost-latency advantage that the cheaper model must be compensated against; if the benchmark quality gap is smaller than this compensation threshold, static benchmark routing (which follows $\hat{q}^{\mathrm{bench}}$) picks the wrong model. The maximum affordable probe budget is

$$n^{\max} = \frac{\Delta U}{c^{\mathrm{probe}}_{\text{per query}}},$$

the number of probe queries whose total cost equals the per-task utility gain.

## 4. Analysis

We now work one routing decision end-to-end. All input numbers are stated assumptions of this worked example (they are illustrative parameter choices, not measurements); every derived number below is computed from them with shown arithmetic.

**Inputs (assumed for the example).**

| Symbol | Meaning | Value |
|---|---|---|
| $q_1$ | Benchmark quality of model $M_1$ | $0.82$ |
| $q_2$ | Benchmark quality of model $M_2$ | $0.74$ |
| $c_1$ | Cost per task, $M_1$ | $\$0.040$ |
| $c_2$ | Cost per task, $M_2$ | $\$0.012$ |
| $\ell_1$ | Latency, $M_1$ | $12\ \mathrm{s}$ |
| $\ell_2$ | Latency, $M_2$ | $4\ \mathrm{s}$ |
| $\lambda_c$ | Cost exchange rate | $5\ \$^{-1}$ |
| $\lambda_\ell$ | Latency exchange rate | $0.01\ \mathrm{s}^{-1}$ |
| $c^{\mathrm{probe}}$ | Cost per probe query | $\$0.002$ |
| $n$ | Probe queries per candidate | $3$ |

**Step 1: Utilities.**

$$U_1 = q_1 - \lambda_c c_1 - \lambda_\ell \ell_1 = 0.82 - (5)(0.040) - (0.01)(12) = 0.82 - 0.20 - 0.12 = 0.50.$$

$$U_2 = q_2 - \lambda_c c_2 - \lambda_\ell \ell_2 = 0.74 - (5)(0.012) - (0.01)(4) = 0.74 - 0.06 - 0.04 = 0.64.$$

**Step 2: Static vs. probe-informed choice.** Static benchmark routing follows the higher benchmark quality and selects $M_1$ ($q_1 = 0.82 > q_2 = 0.74$). But by the utility computation, $U_2 = 0.64 > U_1 = 0.50$, so the utility-optimal choice is $M_2$. The decision gap is

$$\Delta U = U_2 - U_1 = 0.64 - 0.50 = 0.14.$$

**Step 3: Break-even quality gap.** By Section 3.4, routing to $M_2$ is optimal iff

$$q_1 - q_2 < \lambda_c (c_1 - c_2) + \lambda_\ell (\ell_1 - \ell_2).$$

Left side: $q_1 - q_2 = 0.82 - 0.74 = 0.08$. Right side: $(5)(0.040 - 0.012) + (0.01)(12 - 4) = (5)(0.028) + (0.01)(8) = 0.14 + 0.08 = 0.22$. Since $0.08 < 0.22$, $M_2$ is confirmed optimal, and the static rubric (which ignores the compensation threshold) misroutes.

**Step 4: Probe cost and net gain.** With $n = 3$ probe queries per candidate at $\$0.002$ each, the total probe cost is

$$C_P = 2 \times 3 \times 0.002 = \$0.012.$$

Net gain per routing decision:

$$\Delta U - C_P = 0.14 - 0.012 = 0.128.$$

**Step 5: Break-even probe budget.**

$$n^{\max} = \frac{\Delta U}{c^{\mathrm{probe}}} = \frac{0.14}{0.002} = 70 \text{ queries per candidate}.$$

So the probe budget could be as large as $70$ queries per candidate before probing stops paying — far above the $3$ assumed here. (Note $n^{\max}$ counts queries per candidate; total across both candidates the break-even is $2 \times 70 = 140$ queries, i.e., total probe spend $\$0.28$ against a gain of $0.14$ utility units.)

**Step 6: Probe cost as a fraction of task cost.** Relative to the cheap model: $C_P / c_2 = 0.012 / 0.012 = 1.00$, i.e., the probe doubles the cost of routing via $M_2$ on this task. Relative to the expensive model: $C_P / c_1 = 0.012 / 0.040 = 0.30$. This is a material overhead and a genuine design tension, examined in Section 6.

**Step 7: Statistical significance of the routing decision.** Assume the probe-based fitness estimator achieves $\sigma_{f,1} = \sigma_{f,2} = 0.05$ (an assumption about probe precision, not a measurement). Then

$$\sigma_\Delta = \sqrt{0.05^2 + 0.05^2} = \sqrt{0.0025 + 0.0025} = \sqrt{0.005} \approx 0.0707.$$

The 95% significance threshold is $z\sigma_\Delta = 1.96 \times 0.0707 \approx 0.1386$. The observed utility gap is $|\hat{U}_2 - \hat{U}_1| = 0.14$. Since $0.14 > 0.1386$, the decision is barely significant at 95% confidence — and only under the assumed precision. With a cruder probe at $\sigma_f = 0.10$ per candidate:

$$\sigma_\Delta = \sqrt{0.01 + 0.01} = \sqrt{0.02} \approx 0.1414, \quad 1.96 \times 0.1414 \approx 0.277.$$

Since $0.14 < 0.277$, a crude probe cannot certify the routing decision at 95% confidence. The minimum per-candidate precision for significance is

$$\sigma_f^{\min} = \frac{|\hat{U}_2 - \hat{U}_1|}{z\sqrt{2}} = \frac{0.14}{1.96 \times 1.4142} = \frac{0.14}{2.7718} \approx 0.0505.$$

**Step 8: Suite-level projection (labeled projection).** If a task suite of $T = 200$ tasks had the same structure as this example, the cumulative net gain would be

$$T \times (\Delta U - C_P) = 200 \times 0.128 = 25.6 \text{ utility units}.$$

This is a projection under the stated assumption that every task in the suite reproduces the example's parameters; real suites will contain tasks where the probe changes nothing (gap already large) or where probing is unaffordable, so $25.6$ is an upper-envelope illustration, not an estimate.

## 5. Results

All results below are computed in Section 4 from the stated example inputs; the suite-level figure is a labeled projection.

- **R1 (misrouting case).** Under the example parameters, static benchmark routing selects $M_1$ while the utility-optimal choice is $M_2$, with decision gap $\Delta U = 0.14$ (Step 2) and break-even quality gap $0.22$ vs. actual gap $0.08$ (Step 3).
- **R2 (probe economics).** A 3-query-per-candidate probe costs $C_P = \$0.012$ per routing decision and yields net gain $0.128$ utility units (Step 4). The break-even probe budget is $n^{\max} = 70$ queries per candidate (Step 5).
- **R3 (probe overhead).** The probe costs $100\%$ of the cheap model's per-task cost and $30\%$ of the expensive model's (Step 6).
- **R4 (precision requirement).** The routing decision is significant at 95% confidence only if per-candidate probe precision satisfies $\sigma_f \lesssim 0.0505$; at $\sigma_f = 0.05$ the decision is marginally significant ($0.14$ vs. threshold $\approx 0.1386$), and at $\sigma_f = 0.10$ it is not ($0.14 < 0.277$) (Step 7).
- **R5 (projection).** Under the stated uniform-suite assumption, a 200-task suite would accumulate $25.6$ net utility units; this is an upper-envelope projection, not an empirical estimate (Step 8).

## 6. Discussion

**Limitations.** The analysis is a formalization with one worked example; no empirical routing experiment was run, and every input number is an assumed parameter, not a measurement. The linear utility model $U_i = q_i - \lambda_c c_i - \lambda_\ell \ell_i$ assumes separable, exchangeable quality, cost, and latency — real operators may have threshold effects (a task that fails is worth zero regardless of savings) that a linear map misrepresents. The fitness estimator $g$ is left abstract; whether probe responses (plan quality, self-evaluation accuracy) actually predict full-task quality at the precision $\sigma_f \approx 0.05$ required by R4 is precisely the empirical question this paper cannot answer. Self-evaluation accuracy is a particularly risky probe signal if models' self-assessments are miscalibrated — a concern echoed by the delegation-cues literature's observation that agents "rarely surface calibrated uncertainty" [8].

**Failure modes.** (i) *Probe-task mismatch:* if probes are not representative of the task, $\hat{f}_i$ is biased and the router confidently misroutes — worse than static routing because it carries a false aura of measurement. (ii) *Probe overhead dominance:* R3 shows the probe can double the cost of routing to a cheap model; for low-stakes tasks the probe budget $n^{\max} = 70$ is generous, but for tasks where $\Delta U$ is small, even $n = 3$ may not pay. (iii) *Adversarial or degenerate probe behavior:* a model could game diagnostic queries, analogous to the security-threat degradation of routing signals in network routing settings [2]. (iv) *Stochasticity:* as the J/S analysis notes, LLMs are stochastic samplers rather than deterministic solvers [10], so single-probe responses are noisy draws; the significance analysis in R4 quantifies exactly how punishing this is.

**What would falsify the claims.** The central claim — that probe-informed routing beats static rubric routing net of probe costs — is falsified if empirical studies show (a) probe-derived fitness estimates correlate too weakly with realized task quality to reach $\sigma_f \lesssim 0.05$ at affordable probe budgets, or (b) the fraction of tasks where static and probe-informed routing disagree (the only tasks where probing can pay) is too small to amortize probe infrastructure. Conversely, the framework is supported if measured $\Delta U$ distributions across diverse task suites show a heavy mid-range mass (gaps near the significance threshold) where probes change decisions.

**Open questions.** How should the probe set be chosen — is there an optimal design (in the experimental-design sense) over diagnostic queries, and does the bandit framing of Section 3.2 extend to sequential probing with early stopping? Should probe responses be pooled across tasks to build persistent per-model fitness priors, connecting to the task-conditioned routing-signature idea that routing behavior is a measurable function of the task [4]? Can the probe double as a user-facing delegation cue in the sense of [8], so that the same measurement serves both the automated router and the human collaborator? And does the drama-manager pattern of dynamically selecting among portfolio actions [6] offer a control-theoretic alternative to the argmax decision rule?

**Corpus limitation.** Two bibliography entries ([11], [12]) were supplied with empty summaries; no substantive claims are made about them, and the related-work coverage of this paper is bounded by what the supplied entries state.

## 7. Conclusion

We have operationalized intelligent LLM task routing as a probe-then-route decision: cheap diagnostic queries purchased before commitment, a fitness estimate extracted from responses, and a decision matrix over quality, cost, and latency. The formalization yields three usable outputs: a value-of-information condition ($\Delta U > C_P$), a break-even probe budget ($n^{\max} = \Delta U / c^{\mathrm{probe}}$, equal to $70$ queries per candidate in the worked example), and a minimum-probe-precision requirement ($\sigma_f \lesssim 0.0505$ for a 95%-confident decision when the utility gap is $0.14$). The worked example demonstrates the motivating failure: static benchmark routing picks the wrong model whenever the benchmark quality gap ($0.08$) is smaller than the cost-latency compensation threshold ($0.22$). The framework's value now rests on an empirical question this paper poses but does not answer: whether real probe responses estimate task fitness precisely enough, cheaply enough, for the probe to pay across diverse task suites.

## References

[1] arXiv:2308.15272v4 | AutoDroid: LLM-powered Task Automation in Android

[2] arXiv:2506.22745v1 | Trusted Routing for Blockchain-Enabled Low-Altitude Intelligent Networks

[3] arXiv:1910.07728v3 | Exploring the Role of Common Model of Cognition in Designing Adaptive Coaching Interactions for Health Behavior Change

[4] arXiv:2603.11114v1 | Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers

[5] arXiv:2509.26306v5 | Interactive Learning for LLM Reasoning

[6] arXiv:1909.10371v2 | Towards Intelligent Interactive Theatre: Drama Management as a way of Handling Performance

[7] arXiv:2606.05868v1 | YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition

[8] arXiv:2603.11011v1 | Task-Aware Delegation Cues for LLM Agents

[9] QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026) | DOI 10.5281/zenodo.21920604

[10] QNFO: Joules-per-Solution for Stochastic and Agentic Inference: Benchmarking Frontier and Agentic LLMs Against the Human Brain | DOI 10.5281/zenodo.21945415

[11] QNFO: Comprehensive Technical Framework for Network Isomorphism | DOI 10.5281/zenodo.18199940

[12] QNFO: Syntactic Generation | DOI 10.5281/zenodo.22758173