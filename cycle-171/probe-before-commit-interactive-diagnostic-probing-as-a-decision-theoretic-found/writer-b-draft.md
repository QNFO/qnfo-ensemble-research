# Probe-Before-Commit: Interactive Diagnostic Probing as a Decision-Theoretic Foundation for LLM Task Routing

## Abstract

Static capability benchmarks poorly predict how well a given large language model (LLM) will perform on a specific task, yet most routing systems assign tasks to models using exactly such static signals. The gap is that per-task fitness — the probability that a specific model produces an acceptable answer to a specific task — is never measured before commitment. We propose operationalizing intelligent routing as a low-cost interactive probe: before committing a task, the router sends cheap diagnostic queries to candidate models, observes their responses, updates a per-model fitness estimate, and routes according to a decision matrix combining predicted quality, latency, and monetary cost. We formalize the probe as an expected-value-of-information (EVI) problem nested inside a routing decision, derive the posterior update for binary probe signals, and give a fully worked numerical example in which probe-informed routing raises expected utility from $0.5700$ to $0.6782$ (a net gain of $0.1082$ after probe costs) at a probe cost of $\$0.003$ per task, with a break-even per-probe cost of $c_p^{\ast} \approx \$0.00821$. A complementary precision analysis shows a routing decision is statistically meaningful only if per-candidate probe precision satisfies $\sigma_f \lesssim 0.0379$. The framework gives router builders concrete design targets — a probe price ceiling and a precision floor — and states explicit falsification conditions for the claim that probing beats static routing.

## 1. Introduction

Organizations that deploy LLMs face a routing problem: for each incoming task, choose among several candidate models that differ in predicted output quality, latency, and per-token cost. The dominant practice is to route by static signals — leaderboard rankings, benchmark aggregates, or hand-tuned heuristics. The cost of this mismatch is concrete: a router that sends a mathematics task to a model with a strong general reputation but weak mathematics fitness pays premium per-token prices for rejected or low-quality outputs, while a router that over-avoids expensive models pays in rework and failed tasks. What would change if this paper's result holds: a router builder could decide, before building any probing infrastructure, whether probing can pay at all at their probe price point, by checking one derived number — the break-even per-probe cost — and one precision target.

The premise of this paper is that static routing is structurally mismatched to the problem, because per-task fitness (the probability that a specific model produces an acceptable answer to a specific task) is exactly the quantity that static aggregates fail to estimate, while it is precisely the quantity a cheap interactive measurement could estimate directly.

The research idea examined here is: before committing a task, send cheap diagnostic queries ("probes") to candidate models; use the responses to estimate each model's fitness for the task; then route based on a decision matrix combining predicted quality, latency, and cost. The idea matters because routing heuristics are rarely grounded in measured fitness, and because probing converts an inference-time guess into a measurement problem with a well-defined price.

The stakes are practical. Efficiency-focused work on LLM deployment shows that serving costs and latency constraints are structural: YouZhi identifies KV-cache memory overhead as the bottleneck that "inflates infrastructure costs and throttles scalability" in high-concurrency deployment, and reports that a naive architecture transition degrades Llama3-8B perplexity from $6.1$ to $25.8$ while its layer-adaptive transition limits the degradation to $6.1 \to 12.9$ [7]. Serving-cost differences across candidate models are therefore real and persistent, so the difference between routing to an adequate cheap model and an over-provisioned expensive one compounds at deployment scale. On the other side, work on LLM stochasticity shows that output quality is not a fixed model property: AutoDroid observes a $2.1\%$ accuracy reduction when the temperature of GPT-3.5 is set to $0$ and a $3.8\%$ accuracy boost when it is raised to $0.7$ [1], which motivates defining fitness as a probability rather than a deterministic attribute.

This paper makes three contributions. First, it formalizes probe-based routing as a two-stage decision problem — a probe-design stage (which queries to send, at what cost) and a routing stage (which model to commit, given probe responses) — and shows the probe decision is an EVI calculation (Section 3). Second, it derives, with full arithmetic, a worked example demonstrating when probing beats static routing and when it barely pays, including the break-even probe cost of $c_p^{\ast} \approx \$0.00821$ and the precision requirement $\sigma_f \lesssim 0.0379$ (Section 4). Third, it specifies who would use the result, at what readiness level, and what the smallest falsifying experiment is (Sections 6 and 7).

We emphasize scope: this paper contains no new empirical measurements. All quantitative results are derived from explicitly stated illustrative assumptions in Section 4; the empirical program is specified, not executed.

## 2. Background and Related Work

The literature relevant to probe-before-commit routing spans four threads: deployed LLM task execution and its stochasticity, routing under uncertain node quality, measurable task-conditioned structure in model computation, and online signals derived from offline evaluations. We discuss each thread through specific results, then state the gap.

**Deployed LLM task execution and stochasticity.** AutoDroid applies LLMs to mobile task automation, motivated by the poor scalability of prior approaches, which suffered from limited language understanding ability and non-trivial manual effort from developers or end-users [1]. Its evaluation deploys Vicuna-7B both on the smartphone itself and on an edge server with an NVIDIA 3090 to assess inference latency, and it fine-tunes on the MoTiF dataset of more than $4.7$k tasks; its discussion reports that setting the temperature of GPT-3.5 to $0$ reduces accuracy by $2.1\%$ while raising it to $0.7$ boosts action accuracy by $3.8\%$, and proposes an instruction cache to reduce latency by reusing common commands [1]. Two of these results bear directly on our formalism: the temperature findings show that the same model's task accuracy shifts measurably with sampling conditions, supporting our definition of fitness as a probability $q_i \in [0,1]$ rather than a fixed attribute, and the edge-versus-device deployment shows that latency and invocation cost differ across serving configurations, supporting the cost and latency terms in our utility function.

**Routing under uncertain node quality.** Trusted routing in blockchain-enabled low-altitude intelligent networks formulates routing among UAVs whose distributed topology, high mobility, and vulnerability to attacks and node failures make links unreliable, and reformulates the problem as a Dec-POMDP to cope with the absence of global information, solved with a SHERB-MADDQN algorithm that embeds observed state into rewards; simulations over a $15\,\text{km} \times 5\,\text{km}$ area show the algorithm outperforming alternatives in delay, convergence, and training loss [2]. The structural parallel is exact: [2] routes data through nodes whose availability is uncertain and partially observable, and it treats state estimation as part of the routing problem rather than a preprocessing step. Our router faces the same abstract structure with models in place of UAVs; the difference is that our uncertainty reduction mechanism is a purchased measurement (the probe) with an explicit price, which lets us derive a break-even condition that a learned POMDP policy does not expose.

**Adaptive interaction with a modeled partner state.** The common-model-of-cognition coaching work builds human-aware collaborative agents that model, learn, and reason about a human partner's physiological, cognitive, and affective states, and evaluates PARCcoach with $60$ participants over more than $28$ days, finding that participants confident in their target behavior complied more and that CMC-guided reminders improved behavioral compliance [3]. This supplies the closest conceptual ancestor of our probe: a coaching agent adapts its interaction to a measured partner state before acting, exactly as our router adapts model selection to a measured model state before committing. The PARCcoach finding that the ideal adaptive coach must be cognizant of difficulty as it pertains to each individual trainee [3] is the human-facing analogue of our claim that fitness is task- and instance-specific, not a global model property.

**Measurable task-conditioned structure inside models.** The routing-signatures work introduces vector representations summarizing expert activation patterns across layers for a given prompt in sparse Mixture-of-Experts transformers, and demonstrates in OLMoE that routing signatures cluster strongly by task category, that this clustering exceeds what sparse load-balancing constraints alone would produce, that task signal increases toward deeper layers, and that signatures alone support high-accuracy linear classification of task type; it releases the MoE-Xray toolkit for routing telemetry [4]. This is the closest internal-routing analogue to our proposal: [4] establishes empirically that how a model allocates computation is task-conditioned and measurable rather than assumed. Our probe operationalizes the same thesis at the model-selection level, observing input-output behavior of opaque models at the API boundary where internal routing telemetry is unavailable.

**The cost of inference-time interaction.** Interactive Learning for LLM Reasoning (ILR) notes that existing multi-agent learning approaches build interactive training environments among multiple LLMs, but that at inference they require re-executing the multi-agent system to obtain final solutions, which diverges from human cognition, in which individuals enhance reasoning without re-execution [5]. ILR's own protocol estimates each LLM's capability parameter $\gamma_i$ offline from a randomly selected validation set of $1{,}000$ MATH samples before training, and compares this one-time measurement against a periodic-update strategy [5]. Two points connect to our framework. First, ILR's offline $\gamma_i$ estimation is a static fitness estimate of exactly the kind our probe is designed to refine per task; its periodic-update comparison shows the authors already recognize that stale fitness estimates lose value. Second, the re-execution objection motivates our cost constraint: any inference-time interaction must be cheap enough to preserve the economics that motivated routing, so our probe is deliberately non-re-executive — a lightweight pre-commitment measurement, not a full multi-agent execution.

**Real-time commitment under live constraints.** The intelligent interactive theatre work proposes an intelligent agent that serves simultaneously as drama manager and as an actor playing a character in live theatre, and poses the research challenges of believable acting skills, learning character behavior from actors and players, and combining these into a single system [6]. We cite it for its control pattern: a system that must commit to actions in real time from a portfolio of options under live performance constraints, which is the commitment structure our router instantiates with models as the portfolio. The work's own proposed steps — developing narrative permutations, learning behavior from player modelling, then combining into one system [6] — mirror our two-stage decomposition of probe design followed by commitment.

**Structural serving cost.** YouZhi identifies KV-cache memory overhead as the bottleneck that inflates infrastructure costs and throttles scalability in high-concurrency LLM deployment, and proposes an adaptive GQA-to-MLA structural transition with a post-training pipeline, evaluated on Huawei Ascend clusters [7]. Its quantified results ground the cost side of our decision matrix: the layer-adaptive transition reduces perplexity degradation by $65\%$ relative to the TransMLA baseline on Llama3-8B ($6.1 \to 12.9$ versus $6.1 \to 25.8$), and the resulting YouZhi-7B and YouZhi-14B achieve average general-benchmark scores of $66.8$ and $68.0$ [7]. The lesson for routing is that quality, cost, and serving efficiency vary across models and configurations simultaneously, so a routing objective that ignores cost or latency optimizes only part of the problem — hence the $\lambda c_i$ and $\mu \ell_i$ terms in our utility.

**Online signals from offline evaluations.** Task-aware delegation cues observes that human–agent teamwork remains brittle due to information asymmetry: users lack task-specific reliability cues and agents rarely surface calibrated uncertainty or rationale, and proposes a collaboration signaling layer that turns offline preference evaluations into online, user-facing primitives for delegation [8]. Its experiments validate two task-conditioned signals — a capability profile (task-specific win tendency) and a coordination-risk cue — on Chatbot-Arena-style pairwise comparisons, using stratified 5-fold cross-validation in which Ridge regularization performs best for both tasks, and removing cluster features reduces Task A accuracy and increases Task B mean squared error [8]. This is conceptually the nearest neighbor of our probe: both convert offline evaluation evidence into online, task-specific signals. Our contribution differs in the consumer of the signal — an automated router rather than a human user — and in treating signal acquisition as a priced decision with a derivable break-even cost, which [8] does not attempt.

**The gap.** Across these eight threads, no work formalizes pre-commitment diagnostic probing of candidate LLMs as a priced expected-value-of-information problem with an explicit break-even probe cost and a precision requirement on the fitness estimate. That is the gap this paper addresses.

## 3. Methods

### 3.1 Setting

A router receives a task $\tau$ and chooses among $N$ candidate models $M_1, \dots, M_N$. Each model $M_i$ has a known per-task monetary cost $c_i$ (dollars), a known latency $\ell_i$ (seconds), and an unknown per-task fitness $q_i \in [0,1]$, the probability that $M_i$'s output for $\tau$ is acceptable. Following the stochasticity evidence reviewed above — for example the temperature-dependent accuracy shifts reported in [1] — fitness is a probability, not a deterministic property.

### 3.2 Decision matrix

The router maximizes expected scalarized utility

$$U_i = \mathbb{E}[q_i \mid \text{evidence}] - \lambda\, c_i - \mu\, \ell_i,$$

where $\lambda$ (utility per dollar) and $\mu$ (utility per second) are fixed trade-off weights. Static rubric routing uses only prior evidence $\mathcal{E}_0$ (benchmarks, rubric scores); probe-informed routing augments it with probe responses.

### 3.3 Probe model

A probe is a cheap diagnostic query sent to model $M_i$ before commitment, costing $c_p$ dollars and $\ell_p$ seconds. We model the binary case: the probe returns a signal $s_i \in \{0,1\}$ (fail/pass). The probe has sensitivity $a = P(s_i = 1 \mid M_i \text{ fit})$ and false-positive rate $b = P(s_i = 1 \mid M_i \text{ not fit})$, with $a > b$. The router holds a prior $\pi_i = P(M_i \text{ fit})$. By Bayes' rule,

$$\pi_i^{+} = P(\text{fit} \mid s_i = 1) = \frac{a\,\pi_i}{a\,\pi_i + b(1 - \pi_i)}, \qquad \pi_i^{-} = P(\text{fit} \mid s_i = 0) = \frac{(1-a)\,\pi_i}{(1-a)\,\pi_i + (1-b)(1 - \pi_i)}.$$

We take fitness probability as the quality term, i.e., $\mathbb{E}[q_i \mid s_i] = \pi_i^{\pm}$, so that a fit model yields an acceptable solution with probability $1$ and an unfit model with probability $0$; this is a conservative two-point approximation to a continuous fitness distribution.

### 3.4 Probe decision as EVI

Let $U^{\text{static}} = \max_i U_i$ under priors, and let $U^{\text{probe}}$ be the expected utility of the two-stage policy: probe all $N$ candidates (in parallel, so probe latency is $\ell_p$ once), then commit optimally. The probe is worth sending iff

$$\Delta = U^{\text{probe}} - \lambda N c_p - \mu \ell_p - U^{\text{static}} > 0.$$

The break-even per-probe cost is $c_p^{\ast} = (U^{\text{probe,gross}} - \mu \ell_p - U^{\text{static}}) / (\lambda N)$, where $U^{\text{probe,gross}}$ excludes probe cost.

### 3.5 Precision requirement for a meaningful decision

For a routing decision to be statistically meaningful, the utility gap between the top two candidates must exceed the decision noise. With independent fitness standard errors $\sigma_{f,1}, \sigma_{f,2}$ for the top two candidates, the standard error of the utility difference is $\sigma_\Delta = \sqrt{\sigma_{f,1}^2 + \sigma_{f,2}^2}$, and the decision is significant at confidence level $z$ (e.g., $z = 1.96$ for two-sided 95%) iff $|\hat{U}_1 - \hat{U}_2| > z\,\sigma_\Delta$. Setting $\sigma_{f,1} = \sigma_{f,2} = \sigma_f$ yields a minimum-probe-precision requirement

$$\sigma_f \le \frac{|\hat{U}_1 - \hat{U}_2|}{z\sqrt{2}}.$$

### 3.6 Extension to graded probes

Binary probes generalize to graded scores $s_i \in \{1, \dots, K\}$ with likelihoods $P(s_i \mid \text{fit})$ and $P(s_i \mid \text{not fit})$; the posterior update is the same Bayes rule over $K$ outcomes. Probe families may include plan-quality sketches and self-evaluation accuracy checks; the formalism is agnostic to probe content, requiring only a likelihood model.

## 4. Analysis

All numbers below are derived from explicitly stated illustrative assumptions; none are empirical measurements.

**Inputs (assumed for the worked scenario).** Three candidate models with priors, costs, and latencies:

| Model | Prior $\pi_i$ | Cost $c_i$ (\$) | Latency $\ell_i$ (s) |
|---|---|---|---|
| $M_1$ | $0.70$ | $0.020$ | $3$ |
| $M_2$ | $0.50$ | $0.005$ | $1$ |
| $M_3$ | $0.80$ | $0.080$ | $8$ |

Trade-off weights: $\lambda = 5$ utility per dollar, $\mu = 0.01$ utility per second. Probe parameters: sensitivity $a = 0.9$, false-positive rate $b = 0.3$, probe cost $c_p = \$0.001$, probe latency $\ell_p = 0.5$ s, probes sent in parallel to all $N = 3$ models, signals conditionally independent across models.

**Step 1: Static routing.** The static utility of each model is $U_i = \pi_i - \lambda c_i - \mu \ell_i$:

$$U_1 = 0.70 - 5(0.020) - 0.01(3) = 0.70 - 0.10 - 0.03 = 0.57,$$
$$U_2 = 0.50 - 5(0.005) - 0.01(1) = 0.50 - 0.025 - 0.01 = 0.465,$$
$$U_3 = 0.80 - 5(0.080) - 0.01(8) = 0.80 - 0.40 - 0.08 = 0.32.$$

Static routing selects $M_1$: $U^{\text{static}} = 0.57$.

**Step 2: Posterior updates.** Using $\pi_i^{+} = \frac{0.9\,\pi_i}{0.9\,\pi_i + 0.3(1-\pi_i)}$ and $\pi_i^{-} = \frac{0.1\,\pi_i}{0.1\,\pi_i + 0.7(1-\pi_i)}$:

- $M_1$: $\pi_1^{+} = \frac{0.9 \times 0.70}{0.9 \times 0.70 + 0.3 \times 0.30} = \frac{0.63}{0.63 + 0.09} = \frac{0.63}{0.72} = 0.875$; $\pi_1^{-} = \frac{0.1 \times 0.70}{0.1 \times 0.70 + 0.7 \times 0.30} = \frac{0.07}{0.07 + 0.21} = \frac{0.07}{0.28} = 0.25$.
- $M_2$: $\pi_2^{+} = \frac{0.45}{0.45 + 0.15} = \frac{0.45}{0.60} = 0.75$; $\pi_2^{-} = \frac{0.05}{0.05 + 0.35} = \frac{0.05}{0.40} = 0.125$.
- $M_3$: $\pi_3^{+} = \frac{0.72}{0.72 + 0.06} = \frac{0.72}{0.78} \approx 0.923077$; $\pi_3^{-} = \frac{0.08}{0.08 + 0.14} = \frac{0.08}{0.22} \approx 0.363636$.

**Step 3: Post-probe utilities** ($U_i^{\pm} = \pi_i^{\pm} - \lambda c_i - \mu \ell_i$; the cost-latency deductions are $0.13$, $0.035$, and $0.48$ from Step 1):

- $M_1$: $U_1^{+} = 0.875 - 0.13 = 0.745$; $U_1^{-} = 0.25 - 0.13 = 0.12$.
- $M_2$: $U_2^{+} = 0.75 - 0.035 = 0.715$; $U_2^{-} = 0.125 - 0.035 = 0.09$.
- $M_3$: $U_3^{+} = 0.923077 - 0.48 = 0.443077$; $U_3^{-} = 0.363636 - 0.48 = -0.116364$.

**Step 4: Signal marginal probabilities.** $P(s_i = 1) = a\pi_i + b(1-\pi_i)$:

- $M_1$: $0.9(0.7) + 0.3(0.3) = 0.63 + 0.09 = 0.72$; fail: $1 - 0.72 = 0.28$.
- $M_2$: $0.9(0.5) + 0.3(0.5) = 0.45 + 0.15 = 0.60$; fail: $0.40$.
- $M_3$: $0.9(0.8) + 0.3(0.2) = 0.72 + 0.06 = 0.78$; fail: $0.22$.

**Step 5: Expected utility of the probe policy.** With independent signals there are $2^3 = 8$ joint outcomes. For each, the router picks the model with maximum $U_i^{\pm}$:

```
Outcome (s1 s2 s3)   Probability                    Best model   Utility
111                  0.72*0.60*0.78 = 0.33696       M1           0.745
110                  0.72*0.60*0.22 = 0.09504       M1           0.745
101                  0.72*0.40*0.78 = 0.22464       M1           0.745
100                  0.72*0.40*0.22 = 0.06336       M1           0.745
011                  0.28*0.60*0.78 = 0.13104       M2           0.715
010                  0.28*0.60*0.22 = 0.03696       M2           0.715
001                  0.28*0.40*0.78 = 0.08736       M3           0.443077
000                  0.28*0.40*0.22 = 0.02464       M1           0.12
```

Best-model checks: in outcome $000$ all probes fail, so the router picks $\max(0.12, 0.09, -0.116364) = 0.12$ ($M_1$); in outcome $011$ the choice is $\max(0.12, 0.715, 0.443077) = 0.715$ ($M_2$); in outcome $001$ the only passing model is $M_3$ with $0.443077$. Probability check: the eight products sum to $0.33696 + 0.09504 + 0.22464 + 0.06336 + 0.13104 + 0.03696 + 0.08736 + 0.02464 = 1.00000$. Grouping by best model: $M_1$ at utility $0.745$ carries probability $0.33696 + 0.09504 + 0.22464 + 0.06336 = 0.72$; $M_2$ at $0.715$ carries $0.13104 + 0.03696 = 0.168$; $M_3$ at $0.443077$ carries $0.08736$; and the $000$ outcome at $0.12$ carries $0.02464$. Then

$$U^{\text{probe,gross}} = 0.745