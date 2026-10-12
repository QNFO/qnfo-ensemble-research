# Amortisation Accounting for Bottled Agents: Decision Rules for When LLM Agents Should Invest in Reusable Artifacts

## Abstract

Large language model (LLM) agents can in principle convert a general capability into a cheap, task-specific artifact — a small trained model or a reusable program — that completes a large repetitive workload at a fraction of the per-query cost; the BOTTLED benchmark measures this "bottling" ability and reports that it is unreliable, with 48 of 60 bottling runs falling below the zero-shot confidence band of the same model. The specific gap addressed here is that BOTTLED reports outcome statistics but no decision rule: a practitioner with a workload of $N$ items still lacks an explicit criterion for when attempting to bottle is worth the setup cost, and an auditor lacks a null model against which the reported failure counts can be judged. We derive such a rule from a two-term amortisation account (fixed artifact-building cost plus reduced per-item cost), compute break-even workload sizes, quality-per-dollar multipliers, and binomial null models for the reported failure counts, using only the numbers published in the BOTTLED abstract. The principal results are: under a null hypothesis that bottling preserves zero-shot performance, the expected number of sub-confidence-band runs out of 60 is $1.5$ with standard deviation $1.21$, so the observed 48 corresponds to $z \approx 38.4$; the reported Opus 5 result implies a quality-per-dollar multiplier of $538.7$; and the 31-of-60 count against a distillation baseline is statistically indistinguishable from chance ($z \approx 0.26$). These computations turn BOTTLED's summary statistics into actionable thresholds for workload sizing and agent evaluation.

## 1. Introduction

Teams that use LLMs for bulk repetitive work — classifying millions of query-product pairs, labelling corpora, moderating content at scale — face a cost structure in which per-query API pricing multiplies directly with workload size. Querying a frontier model separately for each of millions of related instances is, as the BOTTLED benchmark's authors put it, prohibitively expensive [1], [2]. The alternative is to have an agent *bottle* its capability: build once a cheaper artifact (a distilled small model or a reusable program) and run it over the whole workload. The decision a practitioner actually faces is not "can my model do this task zero-shot?" but "should I spend budget now on an artifact whose quality I cannot guarantee, in order to save money later?" — and today that decision is made by intuition, because no published decision rule connects artifact-building cost, per-item cost reduction, and expected quality retention.

What is at stake is concrete. The BOTTLED results show both directions of the risk: bottling can retain about 82% of zero-shot macro-F1 at roughly 657 times lower reported cost on query-product relevance classification, yet 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's own zero-shot performance, and 31 of 60 runs underperform the stronger of two small-model distillation baselines given the same token budget [1], [2]. A practitioner who bottles blindly therefore faces a coin-flip-or-worse chance of producing an artifact that is *worse per dollar of total outcome* than just running the frontier model, and an agent developer has no diagnostic that predicts which of two models with similar zero-shot scores will bottle well — BOTTLED reports that models with similar zero-shot scores can differ substantially after bottling [1], [2]. If an explicit amortisation rule and null model existed, workload owners could size the minimum workload at which bottling is even arithmetically capable of paying off, and benchmark auditors could distinguish "agents fail at bottling" from "the metric would flag any run half the time."

This paper supplies both, derived entirely from the published BOTTLED summary statistics; it adds no new experiments and claims none. The contributions are:

- A two-term amortisation model (fixed artifact cost $S$ plus reduced per-item cost $c_b$) with a closed-form break-even workload size $N^{\*}$, derived in Section 4.1.
- A quality-per-dollar multiplier $E = r \cdot (c/c_b)$ for a bottled artifact retaining fraction $r$ of quality at per-item cost ratio $c_b/c$, evaluated at $E = 538.7$ for the reported Opus 5 result, derived in Section 4.2.
- A binomial null model showing the observed 48-of-60 sub-confidence-band count is incompatible with "bottling preserves zero-shot performance" at $z \approx 38.4$, while the 31-of-60 count against the distillation baseline is compatible with chance at $z \approx 0.26$, derived in Section 4.3.
- A decision procedure and audit checklist translating these quantities into practice, given in Sections 5 and 7.

## 2. Background and Related Work

The central prior work is the BOTTLED benchmark itself, which appears twice in the supplied bibliography as the arXiv query record [1] and the paper entry [2]; we treat them as one source and cite both where the text is identical. BOTTLED defines bottling as the ability to turn general capabilities into task-specific solutions balancing answer quality and amortised cost; agents receive an entire unlabelled workload and must complete it under fixed time, compute and LLM API budgets, choosing their own approach such as training a small model or writing a reusable program [1], [2]. Its headline findings, which are the sole quantitative inputs to this paper, are the 48-of-60 and 31-of-60 failure counts, the ten-models-three-tasks scope, the 82%-retention-at-657x-lower-cost result for Opus 5 on query-product relevance classification, and the comparison against Jev, a "system one" model built for cheap repetitive inference, where Opus 5 recovers about 94% of Jev's macro-F1 at a quarter of Jev's projected full-workload cost [1], [2]. The supplied abstract gives no further detail on the tasks' construction, the confidence-interval estimation procedure, or the distillation baselines' architecture; this paper therefore treats those quantities as reported summary statistics and derives everything else arithmetically.

The remaining supplied works sit adjacent to bottling rather than inside it, and we state only what their entries support. The survey of multi-agent deep reinforcement learning with communication argues that communication is an effective mechanism for coordinating the behaviors of multiple agents, broadening their views and supporting collaboration, with agents exchanging various types of messages [3]. This is relevant to bottling only as background on how artificial agents coordinate and share state; the entry says nothing about LLM artifact creation, and we draw no finding from it beyond that framing. The "Agents at Risk" paper studies how users unwittingly undermine LLM safety, showing on its stated scope that LLM-based agents performing complex planning and execution tasks are vulnerable to context confusion, where external adversarial content in the agent's reasoning context may be treated as task-relevant constraints [4]. For bottling, the entry supports one caution: an agent that is autonomous enough to train models or write programs is also exposed to content in its context that it may misread as constraints, so a bottling run's artifact inherits whatever confusion occurred during its construction; the entry supplies no quantification of this risk, and we flag it as an open question. Focus Agent is an LLM-powered framework that simulates a focus group for data collection and acts as a moderator, motivated by focus groups being a resource-intensive methodology demanding skilled moderators and meticulous preparation [5]; it is an example of replacing a resource-intensive human process with an LLM-driven one, which is the same economic motivation as bottling, though the entry describes no cost accounting and we use it only as a motivational parallel. The mechanism for discovering semantic relationships among agent communication protocols addresses inter-agent communication at the semantic level within the Semantic Web framework, introducing an efficient mechanism whose main features the supplied summary does not enumerate [6]; because the summary is thin, we relate it to our argument only through its stated goal of protocol interoperability, which is analogous to the interface question of how a bottled artifact's outputs are consumed downstream. The Hanabi convention-augmentation work studies multi-agent reinforcement learning in a cooperative, partially observable game with limited communication, and explores augmenting the action space with conventions to improve cooperation [7]; its relevance is the notion that a convention — a shared, cheap, reusable device — can substitute for expensive per-step coordination, which is structurally the trade bottling makes between a one-time investment and repeated cheap execution; the entry reports no quantitative outcome we may cite. The preference-based and inverse reinforcement learning work on learning agents' value systems situates itself in Agreement Technologies, where autonomous agents interact on behalf of humans and agreements must remain aligned with ethical principles and moral values [8]; for bottling it supplies the governance framing that an agent's autonomous choices, including its choice of artifact, act on a human's behalf and so need value alignment, again without quantitative support in the entry. The plan-reuse mechanism for LLM-driven agents describes assistants that generate plans with an LLM, execute them through tools, and return results, and contributes a plan reuse mechanism for such agents [9]; plan reuse is the closest published relative of bottling in the supplied set — both amortise a one-time LLM investment over repeated executions — but the entry gives no cost or quality numbers, so we cite it as prior art in kind, not in magnitude.

Finally, three QNFO corpus items frame the evaluation context. The LiveBench-grounded audit of the frontier LLM landscape reports, per its summary, that no Llama model ranks in the top 42 and that DeepSeek V4 Pro 0813 is the mathematics price-performance optimum, on the LiveBench 2026-06-25 contamination-free benchmark [10]; this supports the premise that model choice is price-performance-sensitive, which is exactly the axis bottling acts on, though the audit says nothing about bottling itself. The epistemic-legibility position paper argues that as AI systems take on hypothesis generation, experiment planning, analysis and writing, the scientific ecosystem's bottleneck shifts from production to evaluation, verification and governance, and contributes a documented case and an instrument for ignorance auditing [11]; we use it to motivate auditing bottled artifacts rather than trusting them. The flag-structures survey is a cross-domain mathematical survey with explicit counting derivations and a posed re-entry problem [12]; its supplied summary concerns nested subspaces, flag matroids, flag algebras and Finsler curvature, and bears on this paper only as a stylistic exemplar of explicit counting derivations, which Section 4 follows. The final QNFO entry, "Agentic Collapse," has an empty supplied summary [13]; it states no content we can use, and we note that limitation explicitly rather than inferring one.

## 3. Methods

The method is analytical reconstruction from published summary statistics. All input numbers come from the BOTTLED abstract as supplied in entries [1] and [2]; no new data are collected, simulated, or assumed beyond explicitly labelled modelling assumptions. The method has three components.

**Amortisation model.** We model a bottling attempt as a two-cost process. Building the artifact costs a fixed budget $S$, measured in the same unit as LLM spending (tokens or currency); running the artifact costs $c_b$ per item, against a zero-shot frontier cost of $c$ per item. Total cost of the bottled route over a workload of $N$ items is

$$C_{\text{bottle}}(N) = S + N c_b,$$

and the zero-shot route costs $C_{\text{zero}}(N) = N c$. Quality is summarised by a retention fraction $r \in [0,1]$, the bottled artifact's task metric divided by the model's zero-shot task metric on the same evaluation. The reported BOTTLED numbers give one realised $(r, c/c_b)$ pair; the model turns that pair into decision quantities.

**Null models for failure counts.** The BOTTLED abstract reports that 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's zero-shot performance [1], [2]. We construct the null hypothesis $H_0$: bottling does not change task performance, so each run's score is exchangeable with the zero-shot distribution, and the probability of falling below the lower bound of that distribution's 95% two-sided confidence interval is $p_0 = 0.025$. Under $H_0$ the count $X$ of such runs among $n = 60$ independent runs is $\mathrm{Binomial}(60, 0.025)$. The same construction applies to the 31-of-60 count against the stronger distillation baseline, with null $p_0 = 0.5$ (a run is equally likely to beat or lose to a baseline of comparable budget). We use the normal approximation to the binomial, valid here because $n p_0 = 1.5$ is small for the first case — we therefore also compute the exact binomial probability for the first case rather than relying on the normal tail — and $n p_0 = 30$ for the second, where the approximation is standard.

**Quality-per-dollar accounting.** We define the quality-per-dollar multiplier

$$E = \frac{r / c_b}{1 / c} = r \cdot \frac{c}{c_b},$$

the factor by which bottling improves task quality obtained per unit of per-item spend, ignoring the fixed cost $S$. $E > 1$ is the necessary condition for bottling to be worth attempting on a large workload; the sufficient condition additionally requires $N > N^{\*}$, the break-even size derived in Section 4.1. All arithmetic is shown step by step in Section 4.

## 4. Analysis

### 4.1 Break-even workload size

**Inputs.** Per-item zero-shot cost $c$ and bottled per-item cost $c_b$, with the cost ratio from BOTTLED's reported result: Opus 5 retains about 82% of zero-shot macro-F1 at roughly 657 times lower reported cost on query-product relevance classification [1], [2]. We set $c / c_b = 657$ and $r = 0.82$. The fixed artifact cost $S$ is not reported in the supplied abstract; we therefore carry it symbolically and express the break-even in units of $S/c$, the artifact cost measured in zero-shot-query equivalents.

**Derivation.** Bottling is cheaper in total when

$$S + N c_b < N c.$$

Solving for $N$:

$$S < N\left(c - c_b\right) \quad\Longrightarrow\quad N > \frac{S}{c - c_b} = \frac{S}{c\left(1 - c_b/c\right)} = \frac{S}{c} \cdot \frac{1}{1 - \tfrac{1}{657}}.$$

Computing the correction factor:

$$\frac{1}{1 - \tfrac{1}{657}} = \frac{657}{656} \approx 1.001524.$$

So the break-even workload size is

$$N^{\*} \approx 1.0015 \cdot \frac{S}{c}.$$

**Interpretation.** With a 657-fold per-item cost reduction, the break-even condition is almost exactly "the artifact must cost less to build than one zero-shot pass over the workload would have cost." The steep per-item saving makes the fixed cost nearly irrelevant *once the per-item ratio is this large*; the binding uncertainty is $r$, not $S$. Note the asymmetry: if a bottling attempt achieves only a modest ratio, say $c/c_b = 4$ (the ratio implied on the Jev comparison, Section 4.2), then $N^{\*} = \frac{4}{3} \cdot \frac{S}{c} \approx 1.333 \cdot \frac{S}{c}$, and the fixed cost begins to matter.

### 4.2 Quality-per-dollar multipliers

**Opus 5 bottled vs. its own zero-shot.** With $r = 0.82$ and $c/c_b = 657$:

$$E_{\text{Opus}} = 0.82 \times 657 = 538.74.$$

So per unit of per-item spend, the bottled artifact delivers about $539$ times more macro-F1 than querying Opus 5 zero-shot, before accounting for the fixed cost $S$. The threshold retention for $E > 1$ at this cost ratio is

$$r_{\min} = \frac{1}{657} \approx 0.001522,$$

i.e., the artifact needs to retain only about 0.15% of zero-shot quality for the per-item economics to favour it — which is why the observed failures are so informative: runs fail not because the arithmetic cannot work but because agents frequently produce artifacts far worse than the trivial threshold, or fail to produce a working artifact at all within budget.

**Opus 5 bottled vs. Jev.** BOTTLED reports Opus 5 recovers about 94% of Jev's macro-F1 at a quarter of Jev's projected full-workload cost [1], [2]. Setting Jev's quality to $1$ and cost to $c_J$: bottled Opus 5 has $r' = 0.94$ and $c_b = c_J / 4$, so

$$E_{\text{vs Jev}} = \frac{0.94}{1/4} = 0.94 \times 4 = 3.76.$$

Per dollar, bottled Opus 5 delivers $3.76$ times Jev's quality-per-dollar — but in absolute quality it reaches only 94% of Jev, so Jev remains the higher-quality option and the comparison is a Pareto trade, not a dominance.

**General threshold.** For a bottling attempt with retention $r$ and cost ratio $\rho = c/c_b$, the quality-per-dollar condition is

$$E = r \rho > 1 \quad\Longleftrightarrow\quad r > \frac{1}{\rho}.$$

At the reported $\rho = 657$, the condition is nearly free; at a modest $\rho = 4$, the artifact must retain more than $r_{\min} = 0.25$ of zero-shot quality.

### 4.3 Null models for the failure counts

**Count below the zero-shot confidence band.** Input: 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's zero-shot performance [1], [2]. Under $H_0$ (bottling preserves the zero-shot distribution), $p_0 = 0.025$ per run, $n = 60$.

Expected count:

$$\mu = n p_0 = 60 \times 0.025 = 1.5.$$

Standard deviation:

$$\sigma = \sqrt{n p_0 (1 - p_0)} = \sqrt{60 \times 0.025 \times 0.975} = \sqrt{1.4625} \approx 1.20934.$$

Observed $x = 48$. Normal-approximation $z$-score:

$$z = \frac{48 - 1.5}{1.20934} = \frac{46.5}{1.20934} \approx 38.45.$$

Because $n p_0 = 1.5$ is small, we also bound the exact binomial tail. The probability of exactly $k$ runs is $\binom{60}{k} p_0^k (1-p_0)^{60-k}$. The single most likely value is $k = 1$: $\binom{60}{1} (0.025)(0.975)^{59} = 60 \times 0.025 \times (0.975)^{59}$. Computing $(0.975)^{59}$: $\ln(0.975) \approx -0.025318$, so $59 \times (-0.025318) = -1.49376$, and $e^{-1.49376} \approx 0.22459$. Thus $P(X = 1) \approx 60 \times 0.025 \times 0.22459 = 0.33689$. The tail $P(X \geq 48)$ is dominated by its first term:

$$P(X = 48) = \binom{60}{48} (0.025)^{48} (0.975)^{12}.$$

Now $\binom{60}{48} = \binom{60}{12}$. Computing $\binom{60}{12}$: this equals $\frac{60!}{12! \, 48!}$. Step by step: $\binom{60}{12} = 1{,}399{,}353{,}840{,}075$ (standard value of the binomial coefficient; obtained as the product $\prod_{i=1}^{12} \frac{60 - 12 + i}{i} = \frac{49}{1}\cdot\frac{50}{2}\cdot\frac{51}{3}\cdot\frac{52}{4}\cdot\frac{53}{5}\cdot\frac{54}{6}\cdot\frac{55}{7}\cdot\frac{56}{8}\cdot\frac{57}{9}\cdot\frac{58}{10}\cdot\frac{59}{11}\cdot\frac{60}{12}$, which evaluates term-by-term to $49 \times 25 \times 17 \times 13 \times 10.6 \times 9 \times 7.857 \times 7 \times 6.333 \times 5.8 \times 5.364 \times 5$; multiplying the exact integer chain gives $1{,}399{,}353{,}840{,}075$). Then

$$\log_{10} P(X{=}48) = \log_{10}(1.39935 \times 10^{12}) + 48 \log_{10}(0.025) + 12 \log_{10}(0.975).$$

With $\log_{10}(0.025) \approx -1.60206$ and $\log_{10}(0.975) \approx -0.01100$:

$$= 12.14610 - 76.89888 - 0.13200 = -64.88478,$$

so $P(X = 48) \approx 1.3 \times 10^{-65}$, and the full tail $P(X \geq 48)$ is of the same order. Even granting the null generous slack (e.g., doubling $p_0$ to $0.05$ to allow for one-sided interval construction, giving $\mu = 3$, $\sigma = \sqrt{60 \times 0.05 \times 0.95} = \sqrt{2.85} \approx 1.68819$, $z = 45/1.68819 \approx 26.66$), the observation is incompatible with "bottling preserves zero-shot performance." The conclusion that strong zero-shot performance does not reliably translate into strong bottling capability [1], [2] is therefore not a marginal statistical artefact; it is an overwhelming rejection of the preservation null.

**Count below the distillation baseline.** Input: 31 of 60 runs underperform the stronger of two small-model distillation baselines with the same token budget [1], [2]. Under the null that an agent's bottled artifact and the stronger baseline are equally good, each run loses with $p_0 = 0.5$:

$$\mu = 60 \times 0.5 = 30, \qquad \sigma = \sqrt{60 \times 0.5 \times 0.5} = \sqrt{15} \approx 3.87298.$$

Observed $x = 31$:

$$z = \frac{31 - 30}{3.87298} \approx 0.25820.$$

A two-sided normal tail at $z = 0.258$ is about $0.796$, far from any conventional significance level. The honest reading is that, *as a population statistic*, agent bottling performs like a coin flip against a fixed distillation baseline of equal budget: agents collectively add no detectable advantage over the simple baseline, even though individual runs (such as Opus 5's) can be strong.

### 4.4 Aggregate failure-rate confidence intervals

For the 48-of-60 rate, the standard error of the proportion is

$$\mathrm{SE} = \sqrt{\frac{0.8 \times 0.2}{60}} = \sqrt{\frac{0.16}{60}} = \sqrt{0.00266667} \approx 0.0516398,$$

giving a 95% Wald interval of $0.8 \pm 1.96 \times 0.0516398 = 0.8 \pm 0.101214$, i.e. $[0.6988, 0.9012]$. For the 31-of-60 rate:

$$\mathrm{SE} = \sqrt{\frac{0.516667 \times 0.483333}{60}} = \sqrt{\frac{0.2497222}{60}} = \sqrt{0.004162037} \approx 0.0645140,$$

so the 95% interval is $0.516667 \pm 1.96 \times 0.0645140 = 0.516667 \pm 0.126447$, i.e. $[0.3902, 0.6431]$. (Wald intervals at these proportions are adequate for $n = 60$; a Wilson interval would shift the first bound by at most a few percentage points and does not change any conclusion here.)

### 4.5 Worked decision example

A workload owner faces $N = 1{,}000{,}000$ items. Suppose (assumption, labelled as such) the zero-shot route costs $c = \$0.01$ per item, so $C_{\text{zero}} = \$10{,}000$, and a bottling attempt with the reported Opus 5 profile has $c_b = c/657 \approx \$0.00001522$ per item and retention $r = 0.82$. The bottled run cost is $N c_b = 1{,}000{,}000 \times 0.00001522 \approx \$15.22$. The fixed artifact budget can absorb up to

$$S_{\max} = C_{\text{zero}} - N c_b - (\text{quality penalty valued at } 0) = 10{,}000 - 15.22 = \$9{,}984.78$$

before the bottled route costs more in total than zero-shot — i.e., at this per-item ratio the fixed cost is essentially unconstrained. If instead the attempt achieves only the Jev-comparison profile ($r = 0.94$ relative to Jev, $c_b = c_J/4$), the per-item saving is 4-fold and the fixed budget must stay below roughly three-quarters of the zero-shot spend. These are illustrative projections from the two reported ratios, not measurements.

## 5. Results

All numbers below are computed in Section 4 from the BOTTLED summary statistics [1], [2] or explicitly labelled as projections.

**R1. Break-even workload size (Section 4.1).** At the reported cost ratio $c/c_b = 657$, the break-even size is $N^{\*} \approx 1.0015 \cdot S/c$: the artifact must simply cost less to build than one zero-shot pass over the workload. At a 4-fold ratio, $N^{\*} \approx 1.333 \cdot S/c$.

**R2. Quality-per-dollar multipliers (Section 4.2).** The reported Opus 5 bottling result implies $E_{\text{Opus}} = 0.82 \times 657 = 538.74$, i.e., about $539$ times the zero-shot quality per unit of per-item spend. Against Jev, bottled Opus 5 achieves $E = 0.94 \times 4 = 3.76$ times Jev's quality-per-dollar while retaining 94% of Jev's absolute macro-F1. The minimum retention for per-item profitability is $r_{\min} = 1/657 \approx 0.00152$ at the reported ratio, and $r_{\min} = 0.25$ at a 4-fold ratio.

**R3. Rejection of the preservation null (Section 4.3).** Under the null that bottling preserves zero-shot performance, the expected number of sub-confidence-band runs in 60 is $\mu = 1.5$ with $\sigma \approx 1.209$; the observed 48 gives $z \approx 38.45$ (normal approximation) and an exact first-tail term $P(X = 48) \approx 1.3 \times 10^{-65}$. Even with $p_0$ doubled to 0.05, $z \approx 26.66$. The finding that strong zero-shot performance does not translate into bottling capability is statistically overwhelming.

**R4. The distillation baseline is a fair coin (Section 4.3).** The 31-of-60 count against the stronger same-budget distillation baseline is consistent with $p_0 = 0.5$: $z \approx 0.258$, two-sided $p \approx 0.80$. As a population, current agent bottling adds no detectable advantage over simply distilling.

**R5. Failure-rate intervals (Section 4.4).** The sub-confidence-band failure rate is $0.80$ with 95% interval $[0.699, 0.901]$; the below-baseline rate is $0.517$ with 95% interval $[0.390, 0.643]$.

**R6. Worked projection (Section 4.5, labelled projection).** For a $10^6$-item workload at an assumed $\$0.01$ per-item zero-shot cost, a 657-fold-ratio artifact with 82% retention costs about $\$15.22$ to run and tolerates a fixed artifact budget up to about $\$9{,}985$ before losing to zero-shot in total cost; a 4-fold-ratio artifact requires the fixed budget to stay below about 75% of the zero-shot spend. These figures assume the stated per-item cost and inherit the reported ratios' uncertainty; they are not measurements.

## 6. Discussion

The results reframe BOTTLED's findings in two directions. First, R3 shows the headline failure count is not a borderline effect: if bottling merely preserved zero-shot quality, seeing 48 sub-confidence-band runs in 60 would be essentially impossible, so the correct interpretation is that bottling is a *distinct capability* whose presence or absence is only weakly indicated by zero-shot scores — consistent with BOTTLED's own observation that models with similar zero-shot scores can differ substantially after bottling [1], [2]. Second, R4 is the uncomfortable result: against a fixed distillation baseline with the same token budget, the agent population does no better than chance. The value of agentic bottling therefore cannot currently be argued on average performance; it must be argued on variance and tail behaviour — a few runs (Opus 5's) achieve large savings while