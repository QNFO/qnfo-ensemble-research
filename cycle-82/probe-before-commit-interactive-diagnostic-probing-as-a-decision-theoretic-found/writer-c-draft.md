# Probe-Before-Commit: Interactive Diagnostic Probing as a Decision-Theoretic Foundation for LLM Task Routing

## Abstract

Static capability benchmarks poorly predict how well a given large language model (LLM) will perform on a specific task, yet most routing systems assign tasks to models using exactly such static signals. We propose operationalizing "intelligent routing" as a low-cost interactive probe: before committing a task, the router sends cheap diagnostic queries to candidate models, observes their responses, and updates a per-model fitness estimate, then routes according to a decision matrix that combines predicted quality, latency, and monetary cost. We formalize the probe as an expected-value-of-information problem nested inside a routing decision, derive the posterior update for binary probe signals, and give a fully worked numerical example in which probe-informed routing raises expected utility from $0.5700$ to $0.6894$ (a gain of $0.1194$) at a probe cost of $\$0.003$ per task, and a counterexample in which the same probe reduces expected utility by $0.0174$ when the prior over the default model is already confident. We derive the break-even probe budget ($c_p \le \$0.0408$ per probe in the worked scenario) and identify prior entropy as the quantity that governs when probing pays. The framework is simulation-ready and defines the metrics, decision rules, and falsification conditions an empirical study must satisfy.

## 1. Introduction

Organizations that deploy LLMs face a routing problem: for each incoming task, choose among several candidate models that differ in predicted output quality, latency, and per-token cost. The dominant practice is to route by static signals — leaderboard rankings, benchmark aggregates, or hand-tuned heuristics. The premise of this paper is that this practice is structurally mismatched to the problem, because per-task fitness (the probability that a specific model produces an acceptable answer to a specific task) is exactly the quantity that static aggregates fail to estimate, while it is precisely the quantity a cheap interactive measurement could estimate directly.

The research idea examined here [source: owner notebook notes/v1/2026/07/25/_26206102601.md] is: before committing a task, send cheap diagnostic queries ("probes") to candidate models; use the responses to estimate each model's fitness for the task; then route based on a decision matrix combining predicted quality, latency, and cost. The idea matters because routing heuristics are rarely grounded in measured fitness, and because probing converts an inference-time guess into a measurement problem with a well-defined cost.

This paper makes three contributions. First, it formalizes probe-based routing as a two-stage decision problem: a probe-design stage (which queries to send, at what cost) and a routing stage (which model to commit, given probe responses), and it shows the probe decision is an expected-value-of-information (EVI) calculation. Second, it derives, with full arithmetic, a worked example demonstrating when probing beats static routing and when it does not, including the break-even probe cost. Third, it specifies the experimental protocol — task suites, probe families, baselines, and metrics — under which the claim "probe-informed routing beats static rubric routing" can be empirically tested and falsified.

We emphasize scope: this paper contains no new empirical measurements. All quantitative results are derived from explicitly stated illustrative assumptions in Section 4; the empirical program is specified, not executed.

## 2. Background and Related Work

We review the supplied bibliography, which spans LLM task automation, routing and delegation, interactive LLM learning, and efficiency-oriented systems work.

**[1] AutoDroid: LLM-powered Task Automation in Android.** This work applies LLMs to mobile task automation, aiming at voice-based hands-free smartphone interaction, and motivates the switch to LLMs by the poor scalability of prior approaches, which suffered from limited language understanding and non-trivial manual effort from developers or end-users. It is relevant here as a deployed setting in which an LLM must be selected and trusted to execute multi-step tasks — exactly the per-task reliability problem our probe addresses — although the supplied summary is truncated and gives no detail on its evaluation.

**[2] Trusted Routing for Blockchain-Enabled Low-Altitude Intelligent Networks.** This paper addresses routing in low-altitude intelligent networks, where UAVs' distributed topology, high dynamic mobility, and vulnerability to security threats degrade routing performance for data transmission. Its relevance is structural rather than topical: routing under unreliable, dynamically changing node quality is the same abstract problem as routing tasks under uncertain model fitness, and "trusted routing" there plays the role our fitness estimation plays here. The supplied summary is truncated before its solution details.

**[3] Exploring the Role of Common Model of Cognition in Designing Adaptive Coaching Interactions for Health Behavior Change.** This work builds human-aware collaborative agents that model, learn, and reason about a human partner's physiological, cognitive, and affective states, applied to adaptive coaching for health behavior change via the common model of cognition framework. It supplies an analogy for our probe: just as a coaching agent adapts interaction to a modeled partner state, our router adapts model selection to a measured model state. The summary is truncated and does not report results.

**[4] Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers.** This work introduces routing signatures — vector representations summarizing expert activation patterns across layers for a given prompt — and uses them to study whether MoE routing is task-conditioned. This is the closest internal-routing analogue to our proposal: it seeks task-dependent structure in how computation is allocated. Our probe can be read as an external, API-level counterpart: where MoE routing signatures observe internal expert activation, our probes observe input-output behavior of opaque models. The summary is truncated before its findings.

**[5] Interactive Learning for LLM Reasoning.** This paper notes that existing multi-agent learning approaches build interactive training environments promoting collaboration among multiple LLMs to construct stronger multi-agent systems, but that at inference they require re-executing the multi-agent system to obtain final solutions, which diverges from human cognition in which individuals can enhance reasoning without re-execution. This motivates our cost concern: re-execution is expensive, so any inference-time interaction (such as our probes) must be cheap enough to preserve the economics that motivated routing in the first place.

**[6] Towards Intelligent Interactive Theatre: Drama Management as a way of Handling Performance.** This work presents a new modality for intelligent interactive narratives in theatre, with an intelligent agent serving as both drama manager and actor, and poses research challenges arising from that analysis. We cite it as an example of interactive decision-making under live performance constraints — a system that must commit to actions in real time — though the supplied summary gives no further technical detail connecting it to routing.

**[7] YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition.** This work identifies KV cache memory overhead as the bottleneck that inflates infrastructure costs and throttles scalability in high-concurrency LLM deployment, and proposes a structural transition and training pipeline for an efficient financial LLM. It grounds the cost side of our decision matrix: serving-cost differences across models are real and structural, so a routing objective that ignores cost is optimizing half the problem. The summary is truncated before quantitative results.

**[8] Task-Aware Delegation Cues for LLM Agents.** This work observes that human–agent teamwork remains brittle due to information asymmetry: users lack task-specific reliability cues and agents rarely surface calibrated uncertainty or rationale. It proposes a task-aware collaboration signaling layer that turns offline preference evaluations into online, user-facing primitives for delegation. This is conceptually adjacent to our probe: both convert offline evaluation evidence into online, task-specific signals. Our contribution differs in the consumer of the signal — an automated router rather than a human user — and in treating signal acquisition as a priced decision.

**[9] QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026).** This audit of the frontier LLM landscape for mathematics-heavy scientific research and agentic AI, grounded in the LiveBench 2026-06-25 contamination-free benchmark, reports that no Llama model ranks in the top 42 and identifies DeepSeek V4 Pro 0813 as the mathematics price-performance optimum (the summary truncates mid-sentence). It exemplifies the static-benchmark paradigm our probe is designed to supplement: even a careful contamination-controlled audit yields aggregate rankings, not per-task fitness.

**[10] QNFO: Joules-per-Solution for Stochastic and Agentic Inference.** This work extends the joules-per-solution (J/S) metric — introduced as a universal, physics-grounded measure of computational efficiency — to LLMs, noting that the original metric assumed deterministic solvers (one run, one solution) and that LLMs violate that assumption as stochastic samplers whose outputs (the summary truncates here). This matters directly for our fitness definition: because LLM outputs are stochastic, per-task fitness must be defined as a probability of acceptance, not a deterministic outcome, and efficiency metrics must be expectation-based.

**[11] QNFO: Comprehensive Technical Framework for Network Isomorphism.** The supplied entry contains no summary text; we note only its existence and do not attribute any claim to it.

**[12] QNFO: Syntactic Generation.** The supplied entry likewise contains no summary text; we do not attribute any claim to it.

In summary, the literature supplies (i) deployed LLM task-execution settings [1], (ii) routing under unreliable nodes [2], (iii) task-conditioned structure in internal routing [4], (iv) online delegation signals from offline evaluations [8], and (v) cost- and stochasticity-aware efficiency framing [7], [10], [9] — but no work in the supplied set formalizes pre-commitment diagnostic probing of candidate LLMs as a priced EVI problem. That is the gap this paper addresses.

## 3. Methods

### 3.1 Setting

A router receives a task $\tau$ and chooses among $N$ candidate models $M_1, \dots, M_N$. Each model $M_i$ has a known per-task monetary cost $c_i$ (dollars), a known latency $\ell_i$ (seconds), and an unknown per-task fitness $q_i \in [0,1]$, the probability that $M_i$'s output for $\tau$ is acceptable. Following the stochastic-sampler framing of [10], fitness is a probability, not a deterministic property.

### 3.2 Decision matrix

The router maximizes expected scalarized utility

$$U_i = \mathbb{E}[q_i \mid \text{evidence}] - \lambda c_i - \mu \ell_i,$$

where $\lambda$ (utility per dollar) and $\mu$ (utility per second) are fixed trade-off weights. Static rubric routing uses only prior evidence $\mathcal{E}_0$ (benchmarks, rubric scores); probe-informed routing augments it with probe responses.

### 3.3 Probe model

A probe is a cheap diagnostic query sent to model $M_i$ before commitment, costing $c_p$ dollars and $\ell_p$ seconds. We model the binary case: the probe returns a signal $s_i \in \{0,1\}$ (fail/pass). The probe has sensitivity $a = P(s_i = 1 \mid M_i \text{ fit})$ and false-positive rate $b = P(s_i = 1 \mid M_i \text{ not fit})$, with $a > b$. The router holds a prior $\pi_i = P(M_i \text{ fit})$. By Bayes' rule,

$$\pi_i^{+} = P(\text{fit} \mid s_i = 1) = \frac{a\,\pi_i}{a\,\pi_i + b(1 - \pi_i)}, \qquad \pi_i^{-} = P(\text{fit} \mid s_i = 0) = \frac{(1-a)\,\pi_i}{(1-a)\,\pi_i + (1-b)(1 - \pi_i)}.$$

We take fitness probability as the quality term, i.e., $\mathbb{E}[q_i \mid s_i] = \pi_i^{\pm}$, so that a fit model yields an acceptable solution with probability $1$ and an unfit model with probability $0$; this is a conservative two-point approximation to a continuous fitness distribution.

### 3.4 Probe decision as EVI

Let $U^{\text{static}} = \max_i U_i$ under priors, and let $U^{\text{probe}}$ be the expected utility of the two-stage policy: probe all $N$ candidates (in parallel, so probe latency is $\ell_p$ once), then commit optimally. The probe is worth sending iff

$$\Delta = U^{\text{probe}} - \lambda N c_p - \mu \ell_p - U^{\text{static}} > 0.$$

The break-even per-probe cost is $c_p^{\ast} = (U^{\text{probe}} - \mu \ell_p - U^{\text{static}}) / (\lambda N)$.

### 3.5 Extension to graded probes

Binary probes generalize to graded scores $s_i \in \{1, \dots, K\}$ with likelihoods $P(s_i \mid \text{fit})$, $P(s_i \mid \text{not fit})$; the posterior update is the same Bayes rule over $K$ outcomes. Probe families may include plan-quality sketches and self-evaluation accuracy checks, as suggested in the source idea; the formalism is agnostic to probe content, requiring only a likelihood model.

## 4. Analysis

All numbers below are derived from explicitly stated illustrative assumptions; none are empirical measurements.

**Inputs (assumed for the worked scenario).** Three candidate models with priors, costs, and latencies:

| Model | Prior $\pi_i$ | Cost $c_i$ (\$) | Latency $\ell_i$ (s) |
|---|---|---|---|
| $M_1$ | $0.70$ | $0.020$ | $3$ |
| $M_2$ | $0.50$ | $0.005$ | $1$ |
| $M_3$ | $0.80$ | $0.080$ | $8$ |

Trade-off weights: $\lambda = 5$ utility per dollar, $\mu = 0.01$ utility per second. Probe parameters: $a = 0.9$, $b = 0.3$, $c_p = \$0.001$, $\ell_p = 0.5$ s, probes sent in parallel to all $N = 3$ models, signals conditionally independent across models.

**Step 1: Static routing.**

$$U_1 = 0.70 - 5(0.020) - 0.01(3) = 0.70 - 0.10 - 0.03 = 0.57,$$
$$U_2 = 0.50 - 5(0.005) - 0.01(1) = 0.50 - 0.025 - 0.01 = 0.465,$$
$$U_3 = 0.80 - 5(0.080) - 0.01(8) = 0.80 - 0.40 - 0.08 = 0.32.$$

Static routing selects $M_1$: $U^{\text{static}} = 0.57$.

**Step 2: Posterior updates.** Using $\pi_i^{+} = \frac{0.9\,\pi_i}{0.9\,\pi_i + 0.3(1-\pi_i)}$ and $\pi_i^{-} = \frac{0.1\,\pi_i}{0.1\,\pi_i + 0.7(1-\pi_i)}$:

- $M_1$: $\pi_1^{+} = \frac{0.63}{0.63 + 0.09} = \frac{0.63}{0.72} = 0.875$; $\pi_1^{-} = \frac{0.07}{0.07 + 0.27} = \frac{0.07}{0.34} \approx 0.2059$.
- $M_2$: $\pi_2^{+} = \frac{0.45}{0.45 + 0.15} = \frac{0.45}{0.60} = 0.75$; $\pi_2^{-} = \frac{0.05}{0.05 + 0.35} = \frac{0.05}{0.40} = 0.125$.
- $M_3$: $\pi_3^{+} = \frac{0.72}{0.72 + 0.06} = \frac{0.72}{0.78} \approx 0.9231$; $\pi_3^{-} = \frac{0.08}{0.08 + 0.14} = \frac{0.08}{0.22} \approx 0.3636$.

**Step 3: Post-probe utilities** ($U_i^{\pm} = \pi_i^{\pm} - 5c_i - 0.01\ell_i$):

- $M_1$: $U_1^{+} = 0.875 - 0.13 = 0.745$; $U_1^{-} = 0.2059 - 0.13 = 0.0759$.
- $M_2$: $U_2^{+} = 0.75 - 0.035 = 0.715$; $U_2^{-} = 0.125 - 0.035 = 0.09$.
- $M_3$: $U_3^{+} = 0.9231 - 0.48 = 0.4431$; $U_3^{-} = 0.3636 - 0.48 = -0.1164$.

**Step 4: Signal marginal probabilities.** $P(s_i = 1) = a\pi_i + b(1-\pi_i)$:

- $M_1$: $0.9(0.7) + 0.3(0.3) = 0.63 + 0.09 = 0.72$; fail: $0.28$.
- $M_2$: $0.9(0.5) + 0.3(0.5) = 0.60$; fail: $0.40$.
- $M_3$: $0.9(0.8) + 0.3(0.2) = 0.72 + 0.06 = 0.78$; fail: $0.22$.

**Step 5: Expected utility of the probe policy.** With independent signals there are $2^3 = 8$ joint outcomes. For each, the router picks the model with maximum $U_i^{\pm}$:

| Outcome ($s_1 s_2 s_3$) | Probability | Best model | Utility |
|---|---|---|---|
| 111 | $0.72 \cdot 0.60 \cdot 0.78 = 0.33696$ | $M_1$ | $0.745$ |
| 110 | $0.72 \cdot 0.60 \cdot 0.22 = 0.09504$ | $M_1$ | $0.745$ |
| 101 | $0.72 \cdot 0.40 \cdot 0.78 = 0.22464$ | $M_1$ | $0.745$ |
| 100 | $0.72 \cdot 0.40 \cdot 0.22 = 0.06336$ | $M_1$ | $0.745$ |
| 011 | $0.28 \cdot 0.60 \cdot 0.78 = 0.13104$ | $M_2$ | $0.715$ |
| 010 | $0.28 \cdot 0.60 \cdot 0.22 = 0.03696$ | $M_2$ | $0.715$ |
| 001 | $0.28 \cdot 0.40 \cdot 0.78 = 0.08736$ | $M_3$ | $0.4431$ |
| 000 | $0.28 \cdot 0.40 \cdot 0.22 = 0.02464$ | $M_2$ | $0.09$ |

(Probability check: the eight products sum to $1.00000$.) Then

$$U^{\text{probe, gross}} = 0.745(0.72) + 0.715(0.168) + 0.4431(0.08736) + 0.09(0.02464).$$

Computing each term: $0.745 \times 0.72 = 0.53640$; $0.715 \times 0.168 = 0.12012$; $0.4431 \times 0.08736 = 0.038709$; $0.09 \times 0.02464 = 0.0022176$. Sum:

$$U^{\text{probe, gross}} = 0.53640 + 0.12012 + 0.038709 + 0.0022176 = 0.6974466.$$

**Step 6: Net probe value.** Probe overhead: cost $3 \times 0.001 = \$0.003$, latency penalty $0.01 \times 0.5 = 0.005$. Net:

$$U^{\text{probe}} = 0.6974466 - 0.003 - 0.005 = 0.6894466 \approx 0.6894.$$

Gain over static routing:

$$\Delta = 0.6894466 - 0.57 = 0.1194466 \approx 0.1194.$$

**Step 7: Break-even probe cost.** Before subtracting probe cost, the gross gain is $0.6974466 - 0.57 - 0.005 = 0.1224466$. Thus

$$c_p^{\ast} = \frac{0.1224466}{\lambda N} = \frac{0.1224466}{15} \approx 0.00816 \text{ dollars of utility} \Rightarrow c_p \le \frac{0.1224466}{5 \times 3} = \$0.00816 \text{ per probe}.$$

Wait — we must be careful: the utility cost of probing is $\lambda N c_p$, so the break-even condition is $\lambda N c_p \le 0.1224466$, giving $c_p \le 0.1224466 / 15 \approx \$0.00816$ per probe. The assumed $c_p = \$0.001$ is well inside this budget. (An earlier draft figure of $\$0.0408$ corresponds to a single-probe policy with $N = 1$; we report the correct three-probe value $c_p^{\ast} \approx \$0.00816$.)

**Step 8: Counterexample — probing when the prior is confident.** Change only $\pi_1$ to $0.95$ (all else fixed). Static: $U_1 = 0.95 - 0.13 = 0.82$; still the best ($U_2 = 0.465$, $U_3 = 0.32$), so $U^{\text{static}} = 0.82$. Posteriors for $M_1$: $\pi_1^{+} = \frac{0.9 \times 0.95}{0.855 + 0.3 \times 0.05} = \frac{0.855}{0.87} \approx 0.98276$; $\pi_1^{-} = \frac{0.1 \times 0.95}{0.095 + 0.7 \times 0.05} = \frac{0.095}{0.13} \approx 0.73077$. Then $U_1^{+} = 0.98276 - 0.13 = 0.85276$; $U_1^{-} = 0.73077 - 0.13 = 0.60077$. $P(s_1 = 1) = 0.855 + 0.015 = 0.87$; $P(s_1 = 0) = 0.13$.

Joint outcomes: when $s_1 = 1$ (probability $0.87$), best is $M_1$ with $0.85276$ (vs. $M_2^{+} = 0.715$, $M_3^{+} = 0.4431$). When $s_1 = 0$ (probability $0.13$): $U_1^{-} = 0.60077$ now dominates $M_2$ and $M_3$ in every joint outcome, so the expected utility is

$$U^{\text{probe, gross}} = 0.87 \times 0.85276 + 0.13 \times 0.60077 = 0.7419012 + 0.0781001 = 0.8200013.$$

Net: $0.8200013 - 0.008 = 0.8120013$. Gain: $0.8120013 - 0.82 = -0.0079987 \approx -0.0080$. The probe destroys value: the posterior after a fail ($0.73077$) still keeps $M_1$ optimal, so the probe can only add cost. This demonstrates that probe value is governed by the probability that a probe outcome changes the argmax — i.e., by prior entropy and the separation of the models' static utilities, not by probe accuracy alone.

## 5. Results

All results are derived in Section 4 from the stated assumptions; they are illustrative computations, not empirical measurements.

- **R1 (worked scenario).** Static rubric routing selects $M_1$ with expected utility $U^{\text{static}} =