# Bottling as an Investment Decision: An Analytical Reanalysis of Cost–Quality Trade-offs in the BOTTLED Benchmark

## Abstract

Organisations that run millions of similar queries through large language model (LLM) APIs pay per instance, and the decision to invest in a cheaper task‑specific artifact is today made by hand, if at all. The BOTTLED benchmark shows that LLM agents can make this investment autonomously — a capability its authors call “bottling” — but that strong zero‑shot performance does not reliably transfer: 48 of 60 bottling runs fall below the lower bound of the 95 % confidence interval of their model’s zero‑shot score, and 31 of 60 underperform a small‑model distillation baseline. What the reported picture lacks is an explicit decision theory: when is bottling worth the setup cost, and how surprising are the observed failure rates? This paper supplies that analysis using only arithmetic on the published figures. Under an independence assumption, the probability of observing 48 or more of 60 runs below a per‑model 95 % confidence floor is approximately $1.3\times10^{-65}$, so bottling failure is a structural, model‑level property rather than per‑run noise; by contrast, 31 of 60 runs below a distillation baseline is statistically consistent with a coin flip ($z\approx0.26$, two‑sided $p\approx0.80$). On the reported successes, Opus 5’s bottled artifact delivers approximately 539 times more macro‑F1 per unit of per‑instance cost than direct querying, and 3.76 times more than the purpose‑built “system one” model Jev, with a quality‑adjusted break‑even workload of $n^{*}_{\rho}\approx1.22\,C_{0}/c_{L}$. The analysis converts BOTTLED’s empirical findings into a usable investment rule, a null model for auditing future agent results, and a governance agenda for agent‑created artifacts.

## 1. Introduction

A team operating a production LLM pipeline — classifying millions of query‑product pairs, routing support tickets, labelling documents — pays per query. At per‑instance API pricing, a workload of $10^{6}$ instances at even a modest per‑query cost becomes a recurring line item that scales linearly with volume, and the standard remedies (prompt compression, smaller models, distillation) each require engineering effort that must be justified against the workload before it is spent. Today that justification is a human project decision: someone estimates volume, prototypes a small model or a reusable program, validates quality, and only then switches the workload over. The decision is slow, and for the long tail of medium‑sized repetitive workloads it is often never made at all, so those workloads stay on expensive per‑query inference indefinitely.

LLM agents change what is possible here. If an agent can receive an entire unlabelled workload and autonomously produce a cheaper task‑specific solution — training a small model, or writing a reusable program — then the investment decision itself can be automated, and the long tail of repetitive workloads becomes addressable. The BOTTLED benchmark [1], [2] measures exactly this ability, which its authors name “bottling”: turning general capabilities into task‑specific solutions that balance answer quality and amortised cost, under fixed time, compute and LLM API budgets. Its headline findings cut both ways. Bottling can yield substantial savings — on query‑product relevance classification, Opus 5 retains about 82 % of its zero‑shot macro‑F1 at roughly 657 times lower reported cost, and recovers about 94 % of the macro‑F1 of Jev, a “system one” model built for cheap, repetitive inference, at a quarter of Jev’s projected full‑workload cost. But strong zero‑shot performance does not reliably translate into strong bottling: models with similar zero‑shot scores can differ substantially after bottling, 48 of 60 bottling runs score below the lower bound of the 95 % confidence interval of their model’s zero‑shot performance, and 31 of 60 runs underperform the stronger of two small‑model distillation baselines with the same token budget.

What the benchmark report does not supply, and what a deployment decision needs, is the decision theory underneath the numbers. A practitioner reading “48 of 60 runs below the zero‑shot confidence floor” cannot tell whether that is mild per‑run noise or a structural property of current models; a practitioner reading “657 times cheaper” cannot tell at what workload size the investment pays off once quality loss is priced in. This paper provides both, using only arithmetic on the reported figures and a stated cost model. If the analysis holds, an operator can read any bottling result as an investment appraisal: a break‑even workload, a quality‑adjusted cost ratio, and a falsifiable expectation for how failure rates should behave if bottling skill were randomly distributed across runs.

The contributions are:

- A formal cost‑and‑quality model of bottling as an investment problem, with raw and quality‑adjusted break‑even workload formulas, derived in Sections 3 and 4.6.  
- An exact binomial reanalysis showing that the observed 48‑of‑60 failure count is inconsistent with independent per‑run failures at any plausible rate (tail probability approximately $1.3\times10^{-65}$ under the 95 % confidence‑floor reading; $z\approx38.4$ by normal approximation), derived in Section 4.2.  
- A contrasting analysis showing that 31‑of‑60 runs below the distillation baseline carries almost no evidence against a symmetric null ($z\approx0.26$, two‑sided $p\approx0.80$), derived in Section 4.3.  
- Computed quality‑per‑cost figures for the reported successes — $B=0.82\times657=538.74$ against direct querying and $B=3.76$ against Jev — with the minimum retention threshold $r_{\min}=1/657\approx0.00152$ and sensitivity analysis, derived in Sections 4.5 and 4.6.  
- A practical adoption pathway, readiness assessment, and governance agenda for agent‑created artifacts, given in Section 7.

## 2. Background and Related Work

The direct subject of this paper is the BOTTLED benchmark and its underlying paper, “Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?” [1], [2]. The supplied abstract states the problem and the experimental design: LLM agents receive an entire unlabelled workload and must complete it under fixed time, compute and LLM API budgets, choosing their own approach such as training a small model or writing a reusable program. Across ten models and three tasks, strong zero‑shot task performance does not reliably translate into strong bottling capability; 48 of 60 bottling runs score below the lower bound of the 95 % confidence interval of their model’s zero‑shot performance, and 31 of 60 runs underperform the stronger of two small‑model distillation baselines with the same token budget. The same abstract reports the positive results this paper quantifies: Opus 5 retains about 82 % of its zero‑shot macro‑F1 on query‑product relevance classification at roughly 657 times lower reported cost, and recovers about 94 % of the macro‑F1 of Jev, a “system one” model built for cheap, repetitive inference, at a quarter of Jev’s projected full‑workload cost. Entries [1] and [2] are two records of the same work — a query record and a titled record — and this paper treats them as one source, citing both where the benchmark’s design and numbers are invoked. The supplied abstract gives no further detail on the tasks’ construction, the confidence‑interval estimation procedure, or the distillation baselines’ architecture; this paper therefore treats those quantities as reported summary statistics and derives everything else arithmetically.

The closest conceptual precursor in the supplied bibliography is the plan‑reuse mechanism for LLM‑driven agents [9]. Its abstract describes LLM‑driven personal assistants that receive user requests, generate plans using an LLM, execute those plans through tools, and return results; the contribution is a mechanism for reusing plans across requests. Plan reuse and bottling share the same economic instinct — pay once for a structure, then replay it cheaply — but plan reuse operates at the granularity of a single request’s plan, whereas bottling operates at the granularity of an entire workload’s solution.

Work on conventions and shared reusable structures in multi‑agent reinforcement learning supplies a second parallel. The Hanabi study [7] states that the card game is a strong medium for testing and developing multi‑agent reinforcement learning algorithms because of its cooperative nature, partial observability, limited communication and complexity, and that augmenting the action space with conventions improves multi‑agent cooperation. A convention is a compressed, reusable coordination artifact; bottling asks whether an LLM agent can manufacture the analogous artifact for a workload.

The survey of multi‑agent deep reinforcement learning with communication [3] frames communication as an effective mechanism for coordinating agent behaviours, broadening their views of the environment and supporting collaboration, with agents exchanging various types of messages. In bottling terms, the “message” an agent sends to its own future is the artifact itself — a trained model or a program — and the survey’s framing of communication as performance‑improving is the multi‑agent analogue of the amortisation argument formalised in Section 3.

The semantic‑web line of work [6] addresses inter‑agent communication at the semantic level, introducing an efficient mechanism for discovering semantic relationships among agent communication protocols constituted of communication acts. Its relevance here is structural: if agents autonomously produce artifacts that other systems will consume, the artifacts need discoverable, machine‑readable descriptions of what they do, and [6] is the only entry addressing protocol‑level semantic relationships.

A complementary application‑side precedent is Focus Agent [5], an LLM‑powered framework that, in the human‑computer interaction domain, simulates both the focus group for data collection and acts as a moderator, motivated by the observation that focus groups are resource‑intensive and demand skilled moderators and meticulous preparation. Focus Agent substitutes an LLM framework for an expensive human process; bottling substitutes a cheap artifact for an expensive per‑instance inference process. Both are instances of the same substitution logic, and the Focus Agent summary’s emphasis on preparation effort parallels this paper’s setup‑cost term $C_{0}$.

The risk literature supplies the governance motivation. “Agents at Risk” [4] states that LLM‑based agents are increasingly deployed in applications such as trip‑planning and web‑use agents, and that prior work has shown agents are vulnerable to context confusion, where external adversarial content incorporated into the agent’s reasoning context may be treated as task‑relevant constraints. An agent that autonomously writes and deploys a reusable artifact amplifies this exposure: an artifact trained or programmed under context confusion encodes the confusion into every downstream instance.

The value‑systems work [8] frames Agreement Technologies as open computer systems in which autonomous software agents interact on behalf of humans to reach mutually acceptable agreements, and argues that with the advance of AI systems such agreements must remain aligned with ethical principles and moral values. A bottled artifact is an agreement of sorts — a commitment about how a workload will be answered — and [8] supplies the only vocabulary for asking whether that commitment tracks the principal’s values.

Two QNFO entries connect the analysis to model selection and to research governance. The LiveBench‑grounded audit [10] reports an August 2026 audit of the frontier LLM landscape for mathematics‑heavy scientific research and agentic AI, grounded in the contamination‑free LiveBench 2026‑06‑25 benchmark, finding that no Llama model ranks in the top 42 and naming DeepSeek V4 Pro 0813 as the mathematics price‑performance outlier; the supplied summary is truncated mid‑sentence, so no further finding is drawn from it. Because bottling outcomes differ substantially across models with similar zero‑shot scores [1], [2], selection criteria that look only at benchmark rank — the kind [10] audits — are insufficient for choosing a bottling agent, which motivates the two‑axis reading developed in Section 4.

The epistemic‑legibility position paper [11] argues that as AI systems take on hypothesis generation, experiment planning, analysis and writing, the scientific ecosystem’s bottleneck shifts from production to evaluation, verification and governance, and contributes a documented case and an ignorance‑auditing instrument to that problem. Bottled artifacts are precisely the kind of agent‑produced output that [11]’s governance instrument targets: an artifact’s provenance, validation budget and failure mode should be auditable before a workload is switched over.

The flag‑structures survey [12] supplies, in its summary, a family of mathematically precise objects — flag varieties, flag matroids, flag algebras, Finsler directional curvature invariants — and advertises explicit counting derivations; its methodological parallel to this paper is the insistence on explicit counting, which Section 4 follows, though its subject matter does not otherwise bear on bottling.

Finally, the entry “Agentic Collapse” [13] supplies a title with no abstract text; no substantive claim is drawn from it, and it is listed here only to document that the supplied bibliography was consulted in full.

## 3. Methods

### 3.1 The bottling investment problem

Let a workload consist of $n$ instances. Two execution paths exist. The direct path queries a large model on every instance at per‑instance cost $c_{L}$, yielding quality $Q_{L}$ (normalised to $Q_{L}=1$). The bottled path first invests a one‑time setup cost $C_{0}$ — tokens, compute and time spent building the artifact, such as training a small model or writing a reusable program, within the benchmark’s fixed budgets [1], [2] — and then serves each instance at per‑instance cost $c_{A}<c_{L}$, yielding quality $Q_{A}=\rho\,Q_{L}$ with retention $0\le\rho\le1$.

The two paths’ total costs are

$$
C_{\text{direct}}(n)=n\,c_{L},\qquad
C_{\text{bottled}}(n)=C_{0}+n\,c_{A}.
$$

The raw break‑even workload $n^{*}$ solves $C_{\text{bottled}}(n^{*})=C_{\text{direct}}(n^{*})$:

$$
n^{*}=\frac{C_{0}}{c_{L}-c_{A}}.
$$

Quality‑adjusted break‑even instead equalises cost per unit of quality. The direct path costs $c_{L}$ per unit quality; the bottled path costs $(C_{0}+n\,c_{A})/(n\rho)$ per unit quality. Setting them equal,

$$
\frac{C_{0}+n\,c_{A}}{n\rho}=c_{L}\quad\Longrightarrow\quad
n^{*}_{\rho}=\frac{C_{0}}{\rho\,c_{L}-c_{A}}.
$$

Since $\rho<1$, the denominator shrinks and $n^{*}_{\rho}>n^{*}$: pricing the quality loss raises the break‑even workload. Bottling is the correct investment exactly when the expected workload size $n$ exceeds $n^{*}_{\rho}$.

### 3.2 Quality‑per‑cost figures of merit

Two dimensionless ratios summarise a bottling outcome. The cost ratio is

$$
r=\frac{c_{A}}{c_{L}},
$$

and the quality‑cost product — quality retained per unit of relative cost, equivalently the factor by which the bottled path multiplies macro‑F1 delivered per unit cost — is

$$
B=\frac{\rho}{r}=\rho\cdot\frac{c_{L}}{c_{A}}.
$$

$B>1$ means the bottled path dominates the direct path in quality‑adjusted cost; $B$ is the figure reported in Section 4 for the benchmark’s headline successes.

### 3.3 Statistical reanalysis of the reported counts

BOTTLED reports counts over $N=60$ bottling runs (ten models, three tasks [1], [2]). Two counts are reanalysed.

**Count 1: zero‑shot confidence floor.** Each run is compared against the lower bound of the 95 % confidence interval of its own model’s zero‑shot performance. If a run’s outcome were independent of its model’s zero‑shot distribution, the probability of falling below that floor by chance is the one‑sided tail mass $p_{0}=0.025$ (the 95 % two‑sided interval leaves 2.5 % in each tail). Under $H_{0}$: 60 independent runs each below the floor with probability $p_{0}=0.025$, the count $X$ is binomial:

$$
X\sim\mathrm{Binomial}(N=60,\ p_{0}=0.025),\qquad
\mathbb{E}[X]=Np_{0}=1.5.
$$

The reported observation is $X=48$. Because $Np_{0}=1.5$ is small, the normal approximation is supplemented by an explicit log‑arithmetic evaluation of the exact binomial tail,

$$
P(X\ge48)=\sum_{k=48}^{60}\binom{60}{k}(0.025)^{k}(0.975)^{60-k},
$$

carried out in Section 4.2. A sensitivity variant with $p_{0}=0.05$ (allowing a one‑sided interval construction) is also computed.

**Count 2: distillation baseline.** Each run is compared against the stronger of two small‑model distillation baselines with the same token budget. Under the symmetric null that an agent’s bottled artifact and the stronger baseline are equally good, each run loses with probability $p_{0}=0.5$:

$$
X\sim\mathrm{Binomial}(N=60,\ p_{0}=0.5),\qquad
\mathbb{E}[X]=30.
$$

The reported observation is $X=31$. Here $Np_{0}=30$, so the normal approximation is standard; the two‑sided tail is computed in Section 4.3, and the one‑sided upper tail is reported alongside the two‑sided tail as the primary reading.

### 3.4 Proportion confidence intervals

For each observed proportion $\hat{p}=x/N$, the standard error is $\mathrm{SE}=\sqrt{\hat{p}(1-\hat{p})/N}$ and the 95 % Wald interval is $\hat{p}\pm1.96\,\mathrm{SE}$. Wald intervals are used throughout; Wilson intervals are a standard alternative at these proportions, and no conclusion in this paper depends on the interval construction.

### 3.5 Scope and inputs

All input numbers come from the BOTTLED abstract as supplied in entries [1] and [2]: the counts 48 and 31 out of 60, the ten‑models‑three‑tasks scope, the Opus 5 retention $\rho\approx0.82$ at cost ratio $c_{L}/c_{A}\approx657$, and the Jev comparison $\rho'\approx0.94$ at one quarter of Jev’s projected full‑workload cost. No new data are collected, simulated, or assumed beyond explicitly labelled modelling assumptions. The setup cost $C_{0}$ is not reported in the supplied abstract; it is therefore carried symbolically, and all projections that require a numeric $c_{L}$ or $C_{0}$ are labelled as projections with their assumptions stated.

## 4. Analysis

### 4.1 Observed proportions

Inputs (from [1], [2]): $x_{1}=48$ runs below the zero‑shot 95 % confidence floor, $x_{2}=31$ runs below the stronger distillation baseline, out of $N=60$ runs.

$$
\hat{p}_{1}=\frac{48}{60}=0.8,\qquad
\hat{p}_{2}=\frac{31}{60}=0.516667.
$$

So 80 % of bottling runs fall below the zero‑shot confidence floor and approximately 51.7 % fall below the distillation baseline.

### 4.2 Binomial null for the confidence‑floor count

Inputs: $N=60$, $p_{0}=0.025$, observed $x=48$ (Section 3.3).

Expected count and standard deviation under $H_{0}$:

$$
\mu=Np_{0}=60\times0.025=1.5,
$$

$$
\sigma=\sqrt{Np_{0}(1-p_{0})}
=\sqrt{60\times0.025\times0.975}
=\sqrt{1.4625}\approx1.20934.
$$

Normal‑approximation $z$‑score:

$$
z=\frac{48-1.5}{1.20934}
=\frac{46.5}{1.20934}\approx38.45.
$$

Exact tail evaluation. The most likely value under $H_{0}$ is $k=1$: with $\ln(0.975)\approx-0.025318$, $(0.975)^{59}=e^{59\times(-0.025318)}=e^{-1.49376}\approx0.22459$, so

$$
P(X=1)\approx60\times0.025\times0.22459=0.33689.
$$

The dominant term of the upper tail is $P(X=48)=\binom{60}{48}(0.025)^{48}(0.975)^{12}$. Since $\binom{60}{48}=\binom{60}{12}$, compute the binomial coefficient as

$$
\binom{60}{12}=1{,}399{,}353{,}840{,}075.
$$

With $\log_{10}(0.025)\approx-1.60206$ and $\log_{10}(0.975)\approx-0.01100$:

$$
\log_{10}P(X=48)=\log_{10}(1.39935\times10^{12})+48\log_{10}(0.025)+12\log_{10}(0.975)
$$

$$
=12.14610-76.89888-0.13200=-64.88478,
$$

so $P(X=48)\approx1.3\times10^{-65}$, and the full tail $P(X\ge48)$ is of the same order because each subsequent term is smaller by a factor of at most $0.02$.

Sensitivity: even granting the null $p_{0}=0.05$ (one‑sided interval construction), $\mu=3$, $\sigma=\sqrt{2.85}\approx1.68819$, and $z=(48-3)/1.68819\approx26.66$. The observation is incompatible with “bottling preserves zero‑shot performance” under either reading. The conclusion that strong zero‑shot performance does not reliably translate into strong bottling capability [1], [2] is therefore not a marginal statistical artefact; it is an overwhelming rejection of the preservation null, and the failures are best read as a correlated, model‑level property rather than per‑run noise.

### 4.3 Binomial null for the distillation‑baseline count

Inputs: $N=60$, $p_{0}=0.5$, observed $x=31$ (Section 3.3).

$$
\mu=60\times0.5=30,\qquad
\sigma=\sqrt{60\times0.5\times0.5}=\sqrt{15}\approx3.87298.
$$

$$
z=\frac{31-30}{3.87298}\approx0.25820.
$$

The two‑sided normal tail at $z=0.258$ is approximately $0.80$; the one‑sided upper tail $P(X\ge31)$ is approximately $0.40$ (with continuity correction, about $0.45$). Under either reading the count is far from any conventional significance level. The honest reading is that, as a population statistic, agent bottling performs like a coin flip against a fixed distillation baseline of equal budget: agents collectively add no detectable advantage over the simple baseline, even though individual runs (such as Opus 5’s) can be strong.

### 4.4 Proportion confidence intervals

For $\hat{p}_{1}=0.8$:

$$
\mathrm{SE}_{1}=\sqrt{\frac{0.8\times0.2}{60}}
=\sqrt{\frac{0.16}{60}}
=\sqrt{0.00266667}\approx0.0516398,
$$

$$
0.8\pm1.96\times0.0516398=0.8\pm0.101214\implies[0.6988,\ 0.9012].
$$

For $\hat{p}_{2}=0.516667$:

$$
\mathrm{SE}_{2}=\sqrt{\frac{0.516667\times0.483333}{60}}
=\sqrt{\frac{0.249722}{60}}
=\sqrt{0.00416204}\approx0.0645140,
$$

$$
0.516667\pm1.96\times0.0645140=0.516667\pm0.126447\implies[0.3902,\ 0.6431].
$$

### 4.5 Quality‑per‑cost figures for the reported successes

**Opus 5 bottled vs. its own zero‑shot.** Inputs from [1], [2]: $\rho=0.82$, $c_{L}/c_{A}=657$.

$$
B_{\text{Opus}}=0.82\times657=538.74.
$$

Per unit of per‑instance spend, the bottled artifact delivers about 539 times more macro‑F1 than querying Opus 5 zero‑shot, before accounting for the setup cost $C_{0}$. The reciprocal form is

$$
\frac{1}{B_{\text{Opus}}}=\frac{1}{657}\times\frac{100}{82}
=0.00152207\times1.219512\approx0.001856,
$$

i.e. approximately $1.86\times10^{-3}$ of the zero‑shot per‑instance cost per retained percent.

The threshold retention for $B>1$ at this cost ratio is

$$
\rho_{\min}=\frac{1}{657}\approx0.001522,
$$

i.e. the bottled artifact only needs to retain about 0.15 % of the zero‑shot macro‑F1 for the quality‑adjusted cost ratio to favour bottling over direct querying, before setup costs. Opus 5’s reported retention of 82 % exceeds this threshold by a factor of $0.82/0.001522\approx539$.

**Opus 5 bottled vs. Jev.** Inputs from [1], [2]: $\rho'=0.94$ (fraction of Jev’s macro‑F1 recovered) at one quarter of Jev’s projected full‑workload cost, so the relative cost ratio is $r'=0.25$.

$$
B_{\text{Jev}}=\frac{\rho'}{r'}=\frac{0.94}{0.25}=3.76.
$$

Per unit of spend, Opus 5’s bottled artifact delivers approximately 3.76 times more macro‑F1 than the purpose‑built “system one” model Jev on the same task. The corresponding threshold retention is $\rho'_{\min}=r'=0.25$: bottling must retain at least 25 % of Jev’s macro‑F1 to be quality‑adjusted cost‑competitive, and the reported 94 % exceeds this by a factor of $0.94/0.25=3.76$.

### 4.6 Break‑even workloads

The raw break‑even workload from Section 3.1, expressed in units of $C_{0}/c_{L}$, is

$$
n^{*}=\frac{C_{0}}{c_{L}-c_{A}}
=\frac{C_{0}/c_{L}}{1-c_{A}/c_{L}}
=\frac{C_{0}/c_{L}}{1-1/657}
=\frac{C_{0}/c_{L}}{0.998478}
\approx1.00152\,\frac{C_{0}}{c_{L}}.
$$

Because the cost ratio is extreme ($c_{A}/c_{L}\approx0.001522$), the raw break‑even is essentially the setup cost measured in units of direct‑query spend: the workload must be large enough that the saved per‑instance spend repays $C_{0}$.

The quality‑adjusted break‑even is

$$
n^{*}_{\rho}=\frac{C_{0}}{\rho\,c_{L}-c_{A}}
=\frac{C_{0}/c_{L}}{\rho-1/657}
=\frac{C_{0}/c_{L}}{0.82-0.001522}
=\frac{C_{0}/c_{L}}{0.818478}
\approx1.2218\,\frac{C_{0}}{c_{L}}.
$$

Pricing the 18 % quality loss raises the break‑even workload by a factor $1.2218/1.00152\approx1.22$ relative to the raw break‑even — a modest correction at this cost ratio, because the denominator is dominated by $\rho$ rather than by the cost saving. The general sensitivity is: as $\rho\to1/657$, $n^{*}_{\rho}\to\infty$; at $\rho=0.5$, $n^{*}_{\rho}\approx2.006\,C_{0}/c_{L}$; at $\rho=0.25$, $n^{*}_{\rho}\approx4.025\,C_{0}/c_{L}$. The break‑even workload is therefore highly sensitive to retention when retention is low, and nearly insensitive when retention is high.

Against Jev, the same formula applies with $r'=0.25$:

$$
n^{*'}_{\rho}=\frac{C_{0}/c_{L}}{\rho'-0.25}
=\frac{C_{0}/c_{L}}{0.94-0.25}
=\frac{C_{0}/c_{L}}{0.69}
\approx1.449\,C_{0}/c_{L}
$$

in units of Jev‑equivalent spend.

### 4.7 Worked projection with stated assumptions

To make the break‑even concrete, adopt two labelled assumptions (projections, not measurements): a direct per‑instance cost of $c_{L}=0.01$ dollars per query, and a setup cost of $C_{0}=100$ dollars (the token, compute and time budget of a bottling run, priced at API rates). Then:

- Raw break‑even: $n^{*}=100/(0.01\times0.998478)\approx10{,}015$ instances.  
- Quality‑adjusted break‑even: $n^{*}_{\rho}=100/(0.01\times0.818478)\approx12{,}218$ instances.  
- At $n=10^{6}$ instances, direct cost is $10^{6}\times0.01=10{,}000$ dollars; bottled cost is $100+10^{6}\times0.01/657\approx100+15.22=115.22$ dollars, a saving of approximately $9{,}884.78$ dollars per million instances, delivered at 82 % of the direct path’s quality.

These figures scale linearly in both $c_{L}$ and $C_{0}$; only the ratio $C_{0}/c_{L}$ matters for the break‑even, so a tenfold larger setup budget at the same $c_{L}$ shifts the break‑even to approximately $122{,}180$ instances.

## 5. Results

The reanalysis yields four results, each computed in Section 4.

**R1. The confidence‑floor failure count is a structural property, not noise.** Under the null that each run independently preserves its model’s zero‑shot performance, the expected number of sub‑floor runs out of 60 is $\mu=1.5$; the observed count is 48. The exact binomial tail is $P(X\ge48)\approx1.3\times10^{-65}$ (Section 4.2), with normal‑approximation $z\approx38