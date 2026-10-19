# Bottling as an Investment Decision: An Analytical Reanalysis of Cost–Quality Trade-offs in the BOTTLED Benchmark

## Abstract

Organisations that run millions of similar queries through large language model (LLM) APIs pay per instance, and the decision to invest in a cheaper task-specific artifact is today made by hand, if at all. The BOTTLED benchmark shows that LLM agents can make this investment autonomously — a capability its authors call "bottling" — but that strong zero-shot performance does not reliably transfer: 48 of 60 bottling runs fall below the lower bound of the 95% confidence interval of their model's zero-shot score, and 31 of 60 underperform a small-model distillation baseline. What is missing is an explicit decision theory: when is bottling worth the setup cost, and how surprising are the observed failure rates? This paper supplies that analysis using only arithmetic on the published figures. Under an independence assumption, the probability of observing 48 or more of 60 runs below a per-model 95% confidence floor is approximately $1.3 \times 10^{-65}$, so bottling failure is a structural, model-level property rather than per-run noise; by contrast, 31 of 60 runs below a distillation baseline is statistically consistent with a coin flip ($z \approx 0.26$, two-sided $p \approx 0.80$). On the reported successes, Opus 5's bottled artifact delivers approximately 539 times more macro-F1 per unit of per-instance cost than direct querying, and 3.76 times more than the purpose-built "system one" model Jev, with a quality-adjusted break-even workload of $n^*_\rho \approx 1.22\,C_0/c_L$. The analysis converts BOTTLED's empirical findings into a usable investment rule, a null model for auditing future agent results, and a governance agenda for agent-created artifacts.

## 1. Introduction

A team operating a production LLM pipeline — classifying millions of query-product pairs, routing support tickets, labelling documents — pays per query. At per-instance API pricing, a workload of $10^6$ instances at even a modest per-query cost becomes a recurring line item that scales linearly with volume, and the standard remedies (prompt compression, smaller models, distillation) each require engineering effort that must be justified against the workload before it is spent. Today that justification is a human project decision: someone estimates volume, prototypes a small model or a reusable program, validates quality, and only then switches the workload over. The decision is slow, and for the long tail of medium-sized repetitive workloads it is often never made at all, so those workloads stay on expensive per-query inference indefinitely.

LLM agents change what is possible here. If an agent can receive an entire unlabelled workload and autonomously produce a cheaper task-specific solution — training a small model, or writing a reusable program — then the investment decision itself can be automated, and the long tail of repetitive workloads becomes addressable. The BOTTLED benchmark [1], [2] measures exactly this ability, which its authors name "bottling": turning general capabilities into task-specific solutions that balance answer quality and amortised cost, under fixed time, compute and LLM API budgets. Its headline findings cut both ways. Bottling can yield substantial savings — on query-product relevance classification, Opus 5 retains about 82% of its zero-shot macro-F1 at roughly 657 times lower reported cost, and recovers about 94% of the macro-F1 of Jev, a "system one" model built for cheap, repetitive inference, at a quarter of Jev's projected full-workload cost. But strong zero-shot performance does not reliably translate into strong bottling: models with similar zero-shot scores can differ substantially after bottling, 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's zero-shot performance, and 31 of 60 runs underperform the stronger of two small-model distillation baselines with the same token budget.

The benchmark's own experimental details sharpen both the opportunity and the risk. Each run operates under a 10-hour time budget and a 5-million-token budget on a single A100 GPU with 40 GB of VRAM [2], so the setup investment $C_0$ of a bottling attempt is physically bounded and small compared to the per-instance savings available on million-scale workloads. At the same time, an agent that delivers nothing is scored at a trivial fallback baseline [2], so headline savings attach only to runs that actually produce a working artifact — and the reported successes are few enough that a deployment decision needs to know how exceptional they are.

What the benchmark report does not supply, and what a deployment decision needs, is the decision theory underneath the numbers. A practitioner reading "48 of 60 runs below the zero-shot confidence floor" cannot tell whether that is mild per-run noise or a structural property of current models; a practitioner reading "657 times cheaper" cannot tell at what workload size the investment pays off once quality loss is priced in. This paper provides both, using only arithmetic on the reported figures and a stated cost model. If the analysis holds, an operator can read any bottling result as an investment appraisal: a break-even workload, a quality-adjusted cost ratio, and a falsifiable expectation for how failure rates should behave if bottling skill were randomly distributed across runs.

The contributions are:

- A formal cost-and-quality model of bottling as an investment problem, with raw and quality-adjusted break-even workload formulas, derived in Sections 3 and 4.6.
- An exact binomial reanalysis showing that the observed 48-of-60 failure count is inconsistent with independent per-run failures at any plausible rate (tail probability approximately $1.3 \times 10^{-65}$ under the 95% confidence-floor reading; $z \approx 38.45$ by normal approximation), derived in Section 4.2.
- A contrasting analysis showing that 31 of 60 runs below the distillation baseline carries almost no evidence against a symmetric null ($z \approx 0.26$, two-sided $p \approx 0.80$), derived in Section 4.3.
- Computed quality-per-cost figures for the reported successes — $B = 0.82 \times 657 = 538.74$ against direct querying and $B = 3.76$ against Jev — with the minimum retention threshold $r_{\min} = 1/657 \approx 0.00152$ and sensitivity analysis, derived in Sections 4.5 and 4.6.
- A budget-bounded reading of the setup cost: because each run is capped at 5 million tokens and 10 hours [2], the setup cost $C_0$ admits an upper bound in token terms, which turns the break-even formulas into concrete projections, derived in Section 4.7.
- A practical adoption pathway, readiness assessment, and governance agenda for agent-created artifacts, given in Section 7.

## 2. Background and Related Work

The direct subject of this paper is the BOTTLED benchmark and its underlying paper, "Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?" [1], [2]. The work defines bottling as the ability to turn general capabilities into task-specific solutions that balance answer quality and amortised cost, and instantiates it as a benchmark in which agents receive an entire unlabelled workload and must complete it under fixed time, compute and LLM API budgets, choosing their own approach such as training a small model or writing a reusable program. Across ten models and three tasks, strong zero-shot task performance does not reliably translate into strong bottling capability: 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's zero-shot performance, and 31 of 60 runs underperform the stronger of two small-model distillation baselines with the same token budget. The same work reports the positive results this paper quantifies: Opus 5 retains about 82% of its zero-shot macro-F1 on query-product relevance classification at roughly 657 times lower reported cost, and recovers about 94% of the macro-F1 of Jev, a "system one" model built for cheap, repetitive inference, at a quarter of Jev's projected full-workload cost. Entries [1] and [2] are two records of the same work — a query record and a titled record — and this paper treats them as one source, citing both where the benchmark's design and numbers are invoked.

Several experimental details reported in [2] matter for the reanalysis. All runs use the same OpenCode harness, which lets the study disentangle harness influence from the underlying LLM's capabilities; each agent receives a single NVIDIA A100 GPU with 40 GB of VRAM, 8 CPU cores and 64 GB of RAM, a 10-hour time budget, and a 5-million-token budget in which output tokens count twice as much as uncached input tokens and cached input tokens count one-tenth as much. Zero-shot scores are computed on a 1000-instance sample of each task with 95% bootstrap confidence intervals over 2000 resamples, and bottled scores are means over two independent runs per model and task — so the 60 runs are 10 models by 3 tasks by 2 repetitions. On MAVE, zero-shot F1 spans only 0.426 to 0.510 across models, yet bottled F1 ranges more than $5\times$ as wide, with Gemini 3.1 Flash-Lite near the trivial baseline and Opus 5 at 0.461; the corresponding spreads on ESCI and RAID are more than $3\times$ and $2\times$. The scoring rule replaces missing predictions with task-specific fallbacks carrying no information about the instance, so an agent that delivers nothing receives the same score as one that answers uninformatively. These details feed directly into the statistical model of Section 3.3 and the budget analysis of Section 4.7.

An earlier analytical reanalysis of the same benchmark [10] developed the investment framing this paper extends: it derived the raw and quality-adjusted break-even workloads, computed the quality-cost products $B = 538.74$ and $B = 3.76$ for the reported Opus 5 results, showed that the 48-of-60 count rejects independent per-run preservation at a tail probability of approximately $1.3 \times 10^{-65}$ while the 31-of-60 count is consistent with a coin flip, and proposed a governance agenda for agent-created artifacts. The present paper revises that analysis and strengthens it with the run-structure and budget details of [2]: the two-runs-per-cell design changes what "independence of runs" can mean, and the 5-million-token cap converts the previously symbolic setup cost into a bounded quantity.

The closest mechanistic precursor is the plan-reuse mechanism AgentReuse for LLM-driven agents [8]. AgentReuse targets LLM-driven personal assistants that receive user requests, generate plans with an LLM, execute them through tools, and return results; on the SMP dataset of 2,664 task requests across 23 intent categories, it achieves an effective plan-reuse rate of 93%, an F1 score for similarity definition 6.8 percentage points higher than existing methods, accuracy 13.06 percentage points higher, and latency reduced by 60.61 percentage points, at an extra VRAM cost of about 100 MB, per-request memory under 1 MB, and added latency under 10 ms. Plan reuse and bottling share the same economic instinct — pay once for a structure, then replay it cheaply — but AgentReuse operates at the granularity of a single request's plan, whereas bottling operates at the granularity of an entire workload's solution. The 93% reuse rate is also a useful empirical anchor for what "replay hits" look like in a neighbouring setting.

Work on conventions in multi-agent reinforcement learning supplies a second parallel. The Hanabi study [6] argues that the card game is a strong medium for testing and developing multi-agent reinforcement learning algorithms because of its cooperative nature, partial observability, limited communication and complexity, and its contribution is to encode existing human conventions as artificial conventions incorporated into existing algorithms through action-space augmentation. In preliminary Small Hanabi tests this yielded faster training times and improved policies, and the full-game evaluation applies an augmented action-convention space to the Rainbow baseline, chosen for its training speed, sample efficiency and low run-to-run variance. A convention is a compressed, reusable coordination artifact; bottling asks whether an LLM agent can manufacture the analogous artifact for a workload. The survey of multi-agent deep reinforcement learning with communication [3] frames communication as an effective mechanism for coordinating agent behaviours, broadening their views of the environment and supporting collaboration, and organises the literature along nine dimensions, concluding that communication can be extended to non-cooperative settings, heterogeneous players and larger agent populations. In bottling terms, the "message" an agent sends to its own future is the artifact itself — a trained model or a program — and the survey's framing of communication as performance-improving is the multi-agent analogue of the amortisation argument formalised in Section 3.

The semantic-web line of work [5] addresses inter-agent communication at the semantic level: it introduces a mechanism for discovering semantic relationships among agent communication protocols, built on an ontology (CommOnt) whose main categories are communication acts, modelled following speech-act theory, and protocol contents, with protocols represented in OWL-DL and compared by the sets of fluents associated with protocol branches rather than by protocol structure. Its relevance here is structural: if agents autonomously produce artifacts that other systems will consume, the artifacts need discoverable, machine-readable descriptions of what they do, and [5] is the closest prior art on comparing behavioural specifications semantically rather than syntactically — the same distinction a provenance record for a bottled artifact would need.

A complementary application-side precedent is Focus Agent [4], an L-powered framework in human-computer interaction that simulates both the focus group for data collection and acts as a moderator, motivated by the observation that focus groups are resource-intensive and demand skilled moderators and meticulous preparation. Its evaluation reports a word error rate of 2.5% and an F1 of 0.9 for its speech-to-text system, and a user study in which participants acknowledged the AI moderator's capability while perceiving it more as a tool than a sentient interlocutor. Focus Agent substitutes an LLM framework for an expensive human process; bottling substitutes a cheap artifact for an expensive per-instance inference process. Both are instances of the same substitution logic, and the preparation-effort motivation parallels this paper's setup-cost term $C_0$.

The value-systems work [7] frames Agreement Technologies as open computer systems in which autonomous software agents interact on behalf of humans to reach mutually acceptable agreements, and argues that with the advance of AI systems such agreements must remain aligned with ethical principles and moral values. It proposes a framework for learning welfarist utilitarian models of human values, evaluated in simulation on two synthetic domains — Firefighters, with 10,000 pairs of trajectories sampled over a pool of 9,000, and Roadworld, with 7,000 comparisons over 2,500 trajectories — covering both value grounding and value-system identification. A bottled artifact is an agreement of sorts — a commitment about how a workload will be answered — and [7] supplies vocabulary and an operational pipeline for asking whether that commitment tracks the principal's values.

For model selection, the LiveBench-grounded audit [11] reports an August 2026 audit of the frontier LLM landscape for mathematics-heavy scientific research and agentic AI, grounded in the contamination-free LiveBench 2026-06-25 benchmark. It finds that no Llama model ranks in the top 42, that DeepSeek V4 Pro 0813 is the mathematics price-performance optimum (95.1 at USD 0.044 per run, within 1.1 points of the top score at 1/12 the cost, in a class with a 33-fold cost spread), and that the agentic axis inverts the mathematics ranking, with Claude 5 Opus Thinking at 65.2 followed closely by open-weights models. Because bottling outcomes differ substantially across models with similar zero-shot scores [1], [2], selection criteria that look only at benchmark rank — exactly the kind of aggregate leaderboard [11] audits and then decomposes by axis — are insufficient for choosing a bottling agent, which motivates the two-axis reading developed in Section 4.

Two further works inform method and scope. The RecoAtlas benchmark [9] evaluates LLM recommendation agents at the level of structured recommendation reports rather than single items, reporting SetHit@K alongside learned reward models and LLM-judge scores, with $K = 20$, across three Amazon product categories and 1,500 agent episodes per method, and shows that LLM judging favours semantically plausible recommendations that do not necessarily satisfy downstream utility. Its lesson for this paper is methodological: a bottled artifact's quality, like a recommendation report's, should not be collapsed into one plausible-sounding scalar, which is a caution against the scalar-retention model of Section 3. The Attractor Calculus paper [12] demonstrates the analytical style this paper adopts — every number derived with shown arithmetic from labelled assumptions, with the empirical program explicitly left as the test — and the lifetime-aware KV-cache placement study [13] likewise presents an analytical audit in which all quantitative grounding is labelled as assumed inputs with computed consequences. Both are cited here for that methodological standard, which Section 4 follows.

## 3. Methods

### 3.1 The bottling investment problem

Let a workload consist of $n$ instances. Two execution paths exist. The direct path queries a large model on every instance at per-instance cost $c_L$, yielding quality $Q_L$ (normalised to $Q_L = 1$). The bottled path first invests a one-time setup cost $C_0$ — tokens, compute and time spent building the artifact, such as training a small model or writing a reusable program, within the benchmark's fixed budgets [1], [2] — and then serves each instance at per-instance cost $c_A < c_L$, yielding quality $Q_A = \rho\, Q_L$ with retention $0 \le \rho \le 1$.

The two paths' total costs are

$$C_{\text{direct}}(n) = n\,c_L, \qquad C_{\text{bottled}}(n) = C_0 + n\,c_A.$$

The raw break-even workload $n^*$ solves $C_{\text{bottled}}(n^*) = C_{\text{direct}}(n^*)$:

$$n^* = \frac{C_0}{c_L - c_A}.$$

Quality-adjusted break-even instead equalises cost per unit of quality. The direct path costs $c_L$ per unit quality; the bottled path costs $(C_0 + n c_A)/(n\rho)$ per unit quality. Setting them equal,

$$\frac{C_0 + n c_A}{n \rho} = c_L \quad\Longrightarrow\quad n^*_\rho = \frac{C_0}{\rho\, c_L - c_A}.$$

Since $\rho < 1$, the denominator shrinks and $n^*_\rho > n^*$: pricing the quality loss raises the break-even workload. Bottling is the correct investment exactly when the expected workload size $n$ exceeds $n^*_\rho$.

### 3.2 Quality-per-cost figures of merit

Two dimensionless ratios summarise a bottling outcome. The cost ratio is

$$r = \frac{c_A}{c_L},$$

and the quality-cost product — quality retained per unit of relative cost, equivalently the factor by which the bottled path multiplies macro-F1 delivered per unit cost — is

$$B = \frac{\rho}{r} = \rho \cdot \frac{c_L}{c_A}.$$

$B > 1$ means the bottled path dominates the direct path in quality-adjusted cost; $B$ is the figure reported in Section 4 for the benchmark's headline successes.

### 3.3 Statistical reanalysis of the reported counts

BOTTLED reports counts over $N = 60$ bottling runs. The run structure reported in [2] — 10 models, 3 tasks, 2 independent runs per model and task — fixes how these 60 runs are generated. Two counts are reanalysed.

**Count 1: zero-shot confidence floor.** Each run is compared against the lower bound of the 95% confidence interval of its own model's zero-shot performance, where the intervals are bootstrap intervals over 2000 resamples on a 1000-instance sample [2]. If a run's outcome were independent of its model's zero-shot distribution, the probability of falling below that floor by chance is the one-sided tail mass $p_0 = 0.025$ (the 95% two-sided interval leaves 2.5% in each tail). Under $H_0$: 60 independent runs each below the floor with probability $p_0 = 0.025$, the count $X$ is binomial:

$$X \sim \mathrm{Binomial}(N=60,\ p_0 = 0.025), \qquad \mathbb{E}[X] = N p_0 = 1.5.$$

The reported observation is $X = 48$. Because $N p_0 = 1.5$ is small, the normal approximation is supplemented by an explicit log-arithmetic evaluation of the exact binomial tail,

$$P(X \ge 48) = \sum_{k=48}^{60} \binom{60}{k} (0.025)^k (0.975)^{60-k},$$

carried out in Section 4.2. A sensitivity variant with $p_0 = 0.05$ (allowing a one-sided interval construction) is also computed. The two-runs-per-cell structure is addressed separately in Section 4.2 as a correlation concern.

**Count 2: distillation baseline.** Each run is compared against the stronger of two small-model distillation baselines with the same token budget. Under the symmetric null that an agent's bottled artifact and the stronger baseline are equally good, each run loses with probability $p_0 = 0.5$:

$$X \sim \mathrm{Binomial}(N=60,\ p_0 = 0.5), \qquad \mathbb{E}[X] = 30.$$

The reported observation is $X = 31$. Here $N p_0 = 30$, so the normal approximation is standard; the two-sided tail is computed in Section 4.3, and the one-sided upper tail is reported alongside the two-sided tail.

### 3.4 Proportion confidence intervals

For each observed proportion $\hat{p} = x/N$, the standard error is $\mathrm{SE} = \sqrt{\hat{p}(1-\hat{p})/N}$ and the 95% Wald interval is $\hat{p} \pm 1.96\,\mathrm{SE}$. Wald intervals are used throughout; Wilson intervals are a standard alternative at these proportions, and no conclusion in this paper depends on the interval construction.

### 3.5 Scope and inputs

All input numbers come from the BOTTLED benchmark as reported in [1] and [2]: the counts 48 and 31 out of 60, the ten-models-three-tasks scope with two runs per cell, the run budgets (10 hours, 5 million weighted tokens, one A100 with 40 GB of VRAM), the Opus 5 retention $\rho \approx 0.82$ at cost ratio $c_L/c_A \approx 657$, and the Jev comparison $\rho' \approx 0.94$ at one quarter of Jev's projected full-workload cost. No new data are collected, simulated, or assumed beyond explicitly labelled modelling assumptions. The setup cost $C_0$ is not reported as a monetary figure; it is carried symbolically, bounded in token terms using the reported 5-million-token cap, and all projections that require a numeric $c_L$ or $C_0$ are labelled as projections with their assumptions stated.

## 4. Analysis

### 4.1 Observed proportions

Inputs (from [1], [2]): $x_1 = 48$ runs below the zero-shot 95% confidence floor, $x_2 = 31$ runs below the stronger distillation baseline, out of $N = 60$ runs.

$$\hat{p}_1 = \frac{48}{60} = 0.8, \qquad \hat{p}_2 = \frac{31}{60} = 0.516667.$$

So 80% of bottling runs fall below the zero-shot confidence floor and approximately 51.7% fall below the distillation baseline.

### 4.2 Binomial null for the confidence-floor count

Inputs: $N = 60$, $p_0 = 0.025$, observed $x = 48$ (Section 3.3).

Expected count and standard deviation under $H_0$:

$$\mu = N p_0 = 60 \times 0.025 = 1.5,$$
$$\sigma = \sqrt{N p_0 (1-p_0)} = \sqrt{60 \times 0.025 \times 0.975} = \sqrt{1.4625} \approx 1.20934.$$

Normal-approximation $z$-score:

$$z = \frac{48 - 1.5}{1.20934} = \frac{46.5}{1.20934} \approx 38.45.$$

Exact tail evaluation. The single most likely value under $H_0$ is $k=1$: with $\ln(0.975) \approx -0.025318$, $(0.975)^{59} = e^{59 \times (-0.025318)} = e^{-1.49376} \approx 0.22459$, so $P(X=1) \approx 60 \times 0.025 \times 0.22459 = 0.33689$ — the null predicts roughly one sub-floor run, not 48.

The dominant term of the upper tail is $P(X = 48) = \binom{60}{48}(0.025)^{48}(0.975)^{12}$. Since $\binom{60}{48} = \binom{60}{12}$, compute the binomial coefficient as the product $\prod_{i=1}^{12} \frac{48+i}{i} = \frac{49}{1}\cdot\frac{50}{2}\cdot\frac{51}{3}\cdot\frac{52}{4}\cdot\frac{53}{5}\cdot\frac{54}{6}\cdot\frac{55}{7}\cdot\frac{56}{8}\cdot\frac{57}{9}\cdot\frac{58}{10}\cdot\frac{59}{11}\cdot\frac{60}{12}$, which evaluates term-by-term to the integer

$$\binom{60}{12} = 1{,}399{,}353{,}840{,}075.$$

Then, with $\log_{10}(0.025) \approx -1.60206$ and $\log_{10}(0.975) \approx -0.01100$:

$$\log_{10} P(X{=}48) = \log_{10}(1.39935 \times 10^{12}) + 48 \log_{10}(0.025) + 12 \log_{10}(0.975)$$
$$= 12.14610 - 76.89888 - 0.13200 = -64.88478,$$

so $P(X = 48) \approx 1.3 \times 10^{-65}$, and the full tail $P(X \ge 48)$ is of the same order because each subsequent term is smaller by a factor of at least $\frac{60-k}{k+1}\cdot\frac{0.025}{0.975} < 0.02$.

Correlation structure. The runs are not 60 independent draws in the strictest sense: they come in pairs, two independent runs per model and task [2], so at most 30 partially correlated units exist. This only strengthens the conclusion. Under the most extreme within-cell correlation, the effective sample is 30 units, and the null expectation becomes $30 \times 0.025 = 0.75$ sub-floor units against 30 observed (each pair either both sub-floor or not); the exact tail under $\mathrm{Binomial}(30, 0.025)$ with 30 observed is $(0.025)^{30} \approx 10^{-48}$, still overwhelmingly small. Under intermediate correlation the tail lies between $10^{-48}$ and $10^{-65}$. No correlation structure consistent with the reported design rescues the preservation null.

Sensitivity: even granting the null $p_0 = 0.05$ (one-sided interval construction), $\mu = 60 \times 0.05 = 3$, $\sigma = \sqrt{60 \times 0.05 \times 0.95} = \sqrt{2.85} \approx 1.68819$, and $z = (48-3)/1.68819 = 45/1.68819 \approx 26.66$. The observation is incompatible with "bottling preserves zero-shot performance"