# Quantifying the Reuse Barrier in Published Omics Data: A Cost Model for Agent-Supported Retrieval, Reanalysis, and Synthesis

## Abstract

The biomedical literature contains a vast collection of omics studies, yet most published data remain functionally inaccessible for computational reuse: when raw data are deposited in public repositories, the information needed to reproduce reported results is dispersed across main text, supplementary files, and code repositories, and intermediate data such as protein abundance files are shared irregularly [1]. This paper asks what that dispersal costs a reanalysis effort and what an agent-supported retrieval framework changes. We formalize a published omics study as a set of reusable artifacts (raw data, metadata, processing code, intermediate tables) distributed over a set of document locations, and we derive closed-form expressions for the expected number of retrieval steps, the expected reanalysis cost, and the failure probability of a reproduction attempt, as functions of artifact dispersal breadth and retrieval reliability. Applying the model with explicitly stated assumptions, we find that for a study whose reproduction-critical artifacts are spread over $k = 5$ locations with per-location retrieval success probability $p = 0.8$, a manual reproduction attempt succeeds with probability $p^k \approx 0.328$ and requires an expected $k/p \approx 6.25$ retrieval visits, whereas an agent that retries failed locations with $r = 2$ additional attempts raises the success probability to $1-(1-p)^3 \approx 0.992$ per location and $0.960$ overall. The model turns the qualitative claim that "most published data remain functionally inaccessible" into a parameterized statement that can be measured per study, per repository, and per agent design, and it identifies which artifact types dominate the barrier.

## 1. Introduction

A computational biologist who wants to reanalyze a published proteomics or genomics study faces a concrete, recurring problem. The raw data may sit in a public repository, but the parameters that produced the reported results, the filtering thresholds, the version of the processing pipeline, and the mapping from supplementary figures to underlying tables are scattered across the article main text, supplementary files, and, where they exist at all, code repositories; intermediate artifacts such as protein abundance tables are shared only in a minority of cases and at irregular locations [1]. The practical consequence is that a reanalysis that should take hours instead takes days or fails outright, and the aggregate effect is that most published omics data are functionally inaccessible for computational reuse even when they are technically downloadable [1]. This blocks a specific class of decisions: whether to build on a published dataset rather than generate new data, whether a reported result can be reproduced under an alternative processing choice, and whether a meta-analysis across studies can be assembled at all.

If the dispersal barrier could be quantified per study, three things change. A journal or repository could report a single "reuse readiness" number alongside a deposit. A reanalysis agent could allocate its retrieval budget to the locations that dominate the failure probability. And an author preparing a supplement could see which missing artifact contributes most to the expected cost imposed on every future reuser.

This paper contributes a measurement framework rather than a deployed system. Its contributions are:

- A formal model of a published omics study as a dispersal of reproduction-critical artifacts over document locations, with closed-form expressions for reproduction success probability and expected retrieval cost (Section 3).
- Explicit numerical derivations, under stated assumptions, of the manual-versus-agent gap: for $k = 5$ dispersed artifacts at $p = 0.8$ per-location retrieval success, manual success probability $p^k \approx 0.328$ versus agent success probability $\approx 0.960$ with two retries, and expected retrieval visits $6.25$ versus $5.00$ (Section 4).
- A sensitivity decomposition showing that the barrier is dominated by the number of distinct locations $k$ and that agent retries substitute linearly for per-location reliability (Section 4).
- A discussion of what observations would falsify the model and which assumptions it rests on (Section 6).
- A practical pathway: who would use the reuse-readiness number, what readiness level the analytical work supports, and the smallest next measurement that would test it (Section 7).

## 2. Background and Related Work

The starting point for this work is the omics data discovery agents framework of Hutton and Meyer, which presents an agentic approach to the retrieval, reanalysis, and synthesis of published omics data and documents the core observation motivating everything here: most published data remain functionally inaccessible for computational reuse because reproduction-critical information is dispersed across main text, supplementary files, and code repositories, with intermediate data shared irregularly when at all [1]. That paper establishes the problem and the agent architecture; it does not, as far as its supplied summary states, provide a quantitative cost model of the dispersal barrier, which is the gap this paper addresses.

A second thread concerns how multiple cooperating agents coordinate. The survey of multi-agent deep reinforcement learning with communication establishes that communication is an effective mechanism for coordinating the behaviors of multiple agents, broadening their views of the environment, and supporting their collaborations, and that agents can communicate various types of messages either to all or to subsets of other agents [2]. In the omics retrieval setting, the analogue is a division of labor in which one agent reads the article text while another queries repositories and a third executes code; the survey's framing supports treating such message-passing as the coordination primitive, though it says nothing specific about scientific documents.

Retrieval over heterogeneous, multimodal document collections is treated in LLandMark, a modular multi-agent framework for landmark-aware multimodal interactive video retrieval, in which specialized agents collaborate across four stages to handle real-world complex queries [8]. The structural lesson for omics retrieval is that a modular, staged agent design can handle diverse and large-scale document collections; the video domain differs in modality, but the problem shape — multimodal understanding, adaptive reasoning, and domain-specific knowledge integration over a large corpus — is the same shape as the omics literature problem.

Agentic discovery over data systems is examined in the declarative data services work, which observes that translating LLM-driven agentic discovery to multi-system data backends surfaces a harder problem: the search space is heterogeneous, the verifier is whether a deployed stack actually runs, and composition knowledge is unevenly captured in pretraining [6]. This maps directly onto omics reanalysis, where the "verifier" is whether a retrieved pipeline actually reproduces the published result and where pipeline-composition knowledge is exactly the kind of knowledge unevenly captured in pretraining. The entry's summary is truncated before its results, so we use it only for this problem framing.

Reliability of distributed computation under partial failure is the subject of two works on Byzantine resilience. Data encoding for Byzantine-resilient distributed optimization studies distributed optimization where data and computation are distributed among $m$ worker machines, $t$ of which may be corrupt, with compromised nodes able to collaboratively and arbitrarily deviate from their pre-specified programs [4]. Byzantine-resilient SGD in high dimensions on heterogeneous data considers the master-worker architecture under Byzantine attacks with heterogeneous data and no probabilistic assumptions on data generation, using a polynomial-time outlier-filtering procedure for robust mean estimation [5]. In the omics setting the failures are not adversarial but the structural question is identical: when a reproduction pipeline is assembled from $k$ independently fallible retrieval steps, the end-to-end reliability is a function of per-step reliability, and the distributed-optimality literature supplies the vocabulary of tolerating $t$ failures among $m$ components.

Local reanalysis methods appear in structural engineering: the meshless-based local reanalysis (MLR) method extends reanalysis methods to the Kriging interpolation meshless method, using combined approximations (CA) and indirect factorization updating (IFU) to reduce the computational cost of meshless methods [3]. The word "reanalysis" there means recomputing a modified structural model cheaply from a previously solved one; the transferable idea is that reanalysis is worthwhile exactly when the cost of full recomputation is high, which is the economic premise of omics reanalysis as well.

Reuse of existing measured data for parameter constraint is illustrated by the dark-energy study that uses H II starburst galaxy apparent magnitude versus redshift data from Siegel et al. (2005) to constrain cosmological model parameters, finding constraints generally consistent with those from other datasets but not as restrictive as the tightest currently available constraints [7]. This is a concrete instance of the payoff side of the ledger: published data, when retrievable, support new scientific constraints, and the quality of what can be extracted depends on what the data can support.

Finally, two QNFO entries bound what an agent can and cannot extract. The information-theoretic limits work shows that an organism does not contain enough organism-specific information to specify its own microscopic organization, treating the genome as a generator specification rather than a trajectory program, and establishes a coarse-graining threshold with dual Hartley/Shannon entropy faces [11]. For data discovery this implies that even a perfect retrieval agent cannot recover information that was never encoded in the published artifacts; the model below therefore treats missing artifacts as irreducible failure, not retrieval failure. The LiveBench-grounded audit of frontier large language models for scientific research and agentic AI reports, among its findings, that no Llama model ranks in the top 42 and that DeepSeek V4 Pro 0813 is the mathematics price-performance optimum [9]; its summary is truncated, so we use it only to note that model choice for the retrieval agent is an auditable, benchmark-grounded decision. The pattern-based ontology entry (PBO/Autaxys) concerns intrinsic self-ordering of patterns [10] and the categorical formalization entry states a Capability(S) $\sim$ End(X$_S$) conjecture with a Church-Turing-scoped resource-level thesis [12]; both are supplied with summaries too thin to support specific claims, and we cite them only as adjacent formal work within the same corpus.

## 3. Methods

### 3.1 Dispersal model of a published omics study

We model a published omics study as a set $A = \{a_1, \dots, a_k\}$ of $k$ reproduction-critical artifacts. An artifact is any item a reuser must obtain to reproduce or extend a reported result: the raw data deposit, the processing parameters, the pipeline code, an intermediate table such as a protein abundance matrix, or a mapping from figure to underlying data. Each artifact $a_i$ resides in exactly one location $\ell_i$ drawn from the set of document locations $L$ = {article main text, supplementary files, code repository, external repository landing page, author contact}. The dispersal breadth of the study is $k$, the number of distinct artifacts that must be retrieved; the location spread is the number of distinct elements among $\{\ell_1, \dots, \ell_k\}$.

The central empirical claim of the motivating work, taken from its supplied text, is that this information "is dispersed across main text, supplementary files, and code repositories" and that intermediate data are shared only irregularly [1]. The model makes that claim parameterized: $k$ and the location spread are measurable per study.

### 3.2 Retrieval reliability

Let $p \in [0,1]$ be the per-attempt success probability of retrieving and correctly interpreting a single artifact from its location. For a human reuser, $p$ aggregates finding the location, gaining access, and interpreting the artifact. For an agent, we separate $p$ into a first-attempt success probability $p$ and the option of $r$ independent retries at the same location, each succeeding with probability $p$ conditional on prior failures being independent. The per-location success probability with $r$ retries is then

$$P_{\text{loc}}(p, r) = 1 - (1-p)^{r+1}.$$

### 3.3 End-to-end reproduction success and cost

Assuming artifact retrievals are independent, the end-to-end reproduction success probability is

$$P_{\text{rep}} = \prod_{i=1}^{k} P_{\text{loc},i}.$$

Under the homogeneous assumption $P_{\text{loc},i} = P_{\text{loc}}$ for all $i$,

$$P_{\text{rep}}(k, p, r) = \left[1 - (1-p)^{r+1}\right]^{k}.$$

The expected number of retrieval visits per artifact is the expected value of a geometric random variable truncated at $r+1$ attempts:

$$E[N] = \sum_{j=1}^{r+1} j \, (1-p)^{j-1} p + (r+1)(1-p)^{r+1},$$

which for the no-retry case $r = 0$ reduces to $E[N] = 1/p$. The expected total retrieval visits for the study is $k \cdot E[N]$.

### 3.4 What the model does not claim

The model treats artifacts as binary (retrieved or not) and retrievals as independent. It does not model semantic difficulty, cross-artifact consistency checking, or the cost of executing a retrieved pipeline; those enter only as qualitative considerations. All numerical results below follow from the closed forms above with stated inputs.

## 4. Analysis

### 4.1 Input values and their sources

The model has three free parameters. None is measured here; each is set to a stated value so that the closed forms of Section 3 can be evaluated, and every result below is a conditional consequence of those settings.

- $k = 5$: the number of reproduction-critical artifacts. This is a modeling choice representing a typical minimal set: raw data deposit, processing parameters, pipeline code, an intermediate abundance table, and a figure-to-data mapping. The motivating work states that reproduction information is dispersed across main text, supplementary files, and code repositories [1], which establishes that multiple distinct locations are involved; the specific value $k=5$ is an assumption, tested in Section 4.4 across a range.
- $p = 0.8$: per-attempt retrieval success. This is an assumption, not a measurement; its role is to represent a reuser who usually but not always succeeds at a given location.
- $r = 2$: agent retries per artifact. This is a design parameter of the agent, not an empirical quantity.

### 4.2 Manual reproduction (no retries, $r = 0$)

With $r = 0$, per-location success is $P_{\text{loc}} = p = 0.8$. End-to-end:

$$P_{\text{rep}}(5, 0.8, 0) = 0.8^{5}.$$

Computing step by step: $0.8^2 = 0.64$; $0.8^3 = 0.64 \times 0.8 = 0.512$; $0.8^4 = 0.512 \times 0.8 = 0.4096$; $0.8^5 = 0.4096 \times 0.8 = 0.32768$.

$$P_{\text{rep}}(5, 0.8, 0) = 0.32768.$$

So under these assumptions a manual reproduction attempt succeeds about $32.8\%$ of the time; roughly two of every three attempts fail.

Expected retrieval visits per artifact with $r=0$ is $E[N] = 1/p = 1/0.8 = 1.25$, and total expected visits:

$$k \cdot E[N] = 5 \times 1.25 = 6.25.$$

### 4.3 Agent reproduction with $r = 2$ retries

Per-location success with two retries:

$$P_{\text{loc}}(0.8, 2) = 1 - (1-0.8)^{3} = 1 - 0.2^{3} = 1 - 0.008 = 0.992.$$

End-to-end:

$$P_{\text{rep}}(5, 0.8, 2) = 0.992^{5}.$$

Computing: $0.992^2 = 0.984064$; $0.992^3 = 0.984064 \times 0.992 = 0.976191488$; $0.992^4 = 0.976191488 \times 0.992 = 0.967981956096$; $0.992^5 = 0.967981956096 \times 0.992 = 0.960238100443136$.

$$P_{\text{rep}}(5, 0.8, 2) \approx 0.9602.$$

The agent raises reproduction success from $0.32768$ to $\approx 0.9602$, a factor of

$$\frac{0.960238100443136}{0.32768} \approx 2.9303.$$

Expected visits per artifact with $r = 2$:

$$E[N] = \sum_{j=1}^{3} j(0.2)^{j-1}(0.8) + 3(0.2)^{3}.$$

Term by term: $j=1$: $1 \times 1 \times 0.8 = 0.8$. $j=2$: $2 \times 0.2 \times 0.8 = 0.32$. $j=3$: $3 \times 0.04 \times 0.8 = 0.096$. Truncation term: $3 \times 0.008 = 0.024$. Sum:

$$E[N] = 0.8 + 0.32 + 0.096 + 0.024 = 1.24.$$

Total expected visits: $5 \times 1.24 = 6.20$. The agent achieves its $\approx 2.93\times$ success improvement at essentially the same expected visit count ($6.20$ vs $6.25$), because retries are triggered only on the $20\%$ of first attempts that fail.

### 4.4 Sensitivity to dispersal breadth $k$

Holding $p = 0.8$, $r = 0$:

$$P_{\text{rep}}(k) = 0.8^{k}.$$

- $k=2$: $0.64$
- $k=3$: $0.512$
- $k=4$: $0.4096$
- $k=5$: $0.32768$
- $k=8$: $0.8^8 = 0.16777216$
- $k=10$: $0.8^{10} = 0.1073741824$

Each additional dispersed artifact multiplies success by $0.8$, i.e., removes $20\%$ of the remaining success probability. Going from $k=2$ to $k=5$ cuts success from $0.64$ to $0.32768$, a $48.8\%$ relative reduction ($1 - 0.32768/0.64 = 1 - 0.512 = 0.488$).

With the agent ($r=2$), the same range gives $0.992^k$: $k=5 \Rightarrow 0.9602$; $k=10 \Rightarrow 0.992^{10}$. Computing: $0.992^{10} = (0.992^5)^2 = 0.960238100443136^2 = 0.9220572498...$; more precisely $0.960238100443136^2 = 0.922057249829... \approx 0.9221$. The agent's advantage grows with $k$: at $k=10$ the manual success is $0.1074$ versus agent $0.9221$, a factor of $\approx 8.59$ ($0.922057249829/0.1073741824 \approx 8.5879$).

### 4.5 Sensitivity to per-location reliability $p$

Holding $k=5$, $r=0$, manual success is $p^5$:

- $p=0.6$: $0.6^5 = 0.07776$
- $p=0.8$: $0.32768$
- $p=0.95$: $0.95^5 = 0.7737809375$

The barrier is therefore jointly driven: even a highly reliable reuser ($p = 0.95$) succeeds only $77.4\%$ of the time at $k=5$, while a moderately reliable agent with retries at $p=0.8$ reaches $96.0\%$. Retries substitute for per-location skill: $P_{\text{loc}}(0.6, 2) = 1 - 0.4^3 = 1 - 0.064 = 0.936$, so a weaker retriever with retries ($0.936$ per location) outperforms a stronger one without ($0.8$ per location).

### 4.6 The irreducible floor from missing artifacts

The information-theoretic result that an organism does not contain enough organism-specific information to specify its own microscopic organization, with the genome acting as a generator specification rather than a trajectory program [11], has a direct analogue here: a published study does not contain enough information to specify every processing decision unless those decisions were explicitly recorded. If an artifact was never deposited, no retrieval strategy recovers it. If a fraction $q$ of studies lack at least one reproduction-critical artifact entirely, the achievable reproduction success is capped at $1 - q$ regardless of $p$, $r$, or agent design. The model's agent ceiling of $0.9602$ at $k=5$, $p=0.8$ is therefore an upper bound only under the assumption that all $k$ artifacts exist somewhere; the motivating work's observation that intermediate data are shared only irregularly [1] means $q > 0$ in practice, and measuring $q$ per data type is the empirical task the model motivates.

## 5. Results

All numbers in this section are computed in Section 4 from the stated inputs $k=5$, $p=0.8$, $r=2$ (and the ranges stated there); none is an empirical measurement.

1. **Manual reproduction success.** With $k=5$ dispersed artifacts and per-attempt success $p=0.8$, a manual reproduction attempt succeeds with probability $P_{\text{rep}} = 0.8^5 = 0.32768$ (Section 4.2).
2. **Agent reproduction success.** With two retries per artifact, $P_{\text{rep}} = 0.992^5 \approx 0.9602$ (Section 4.3), a $2.93\times$ improvement over manual retrieval under the same $p$.
3. **Retrieval cost is nearly unchanged.** Expected retrieval visits are $6.25$ (manual) versus $6.20$ (agent with retries) for the same five artifacts (Sections 4.2, 4.3).
4. **Dispersal breadth dominates.** Each additional artifact multiplies success by $p = 0.8$; over $k = 2$ to $10$, manual success falls from $0.64$ to $0.1074$, while agent success falls only from $0.992^2 = 0.984064$ to $0.9221$ (Section 4.4). The manual-agent gap grows from $1.54\times$ at $k=2$ ($0.984064/0.64$) to $8.59\times$ at $k=10$.
5. **Retries substitute for reliability.** A retriever with $p = 0.6$ and two retries achieves $0.936$ per-location success, exceeding a retriever with $p = 0.8$ and no retries ($0.8$) (Section 4.5).
6. **An irreducible ceiling.** If a fraction $q$ of studies lack at least one reproduction-critical artifact entirely, reproduction success is capped at $1-q$ for any retrieval strategy; the agent figures above assume $q = 0$ (Section 4.6).

The headline statement, conditional on the stated assumptions: at $k=5$ and $p=0.8$, moving from unaided retrieval to an agent with two retries raises the probability that a published omics study can actually be reproduced from $32.8\%$ to $96.0\%$ at essentially no additional retrieval cost.

## 6. Discussion

The model's value is that it converts a qualitative complaint — dispersal makes data functionally inaccessible [1] — into three measurable quantities: dispersal breadth $k$, per-location reliability $p$, and the missing-artifact fraction $q$. Its weakness is that every numerical result above is conditional on assumed parameter values. The $2.93\times$ improvement is not a finding about the world; it is a consequence of $k=5$, $p=0.8$, $r=2$, and the independence assumption, and it should be read as a demonstration that the model produces decision-relevant gaps under plausible parameters, not as evidence that it does so under the actual parameters of the omics literature.

**Independence is the most fragile assumption.** Retrieval failures are plausibly correlated: a reuser who cannot parse a supplementary archive naming scheme will fail on several artifacts for the same reason. With correlation, $P_{\text{rep}}$ is no longer $\prod_i P_{\text{loc},i}$ and the multiplicative decay in $k$ overstates the penalty. A correlated-failure variant would need a joint failure model, which the present closed forms do not provide.

**Artifact granularity is a hidden degree of freedom.** Whether a study has $k=3$ or $k=8$ reproduction-critical artifacts depends on how finely one decomposes "the information needed to reproduce reported results" [1]. The sensitivity analysis (Section 4.4) shows the model is highly sensitive to $k$, so any empirical application must fix a decomposition convention in advance.

**What would falsify the main result.** The central claim is that retries at fixed $p$ raise end-to-end success substantially at negligible extra visit cost. This is falsified if measurement shows that agent retrieval failures are persistent rather than independent — that is, if a location that fails once fails on retry with probability near $1$, so that $P_{\text{loc}}(p, r) \approx p$ rather than $1-(1-p)^{r+1}$. A single well-designed measurement — logging, over a corpus of reanalysis attempts, whether second attempts at the same location succeed at a rate consistent with independence — would confirm or refute the model's central mechanism. If second-attempt success is near zero, the agent advantage collapses toward $1\times$ and the barrier must be attacked by improving first-attempt reliability or by deposition-side fixes, not by retries.

**The ceiling may bind in practice.** The motivating work states that intermediate data are shared only in rarer cases and at irregular locations [1]. If $q$, the fraction of studies with a wholly missing artifact, is large, the agent's $96.0\%$ conditional ceiling is unreachable and the binding constraint moves from retrieval to deposition policy. The model deliberately exposes this: the ratio of the conditional ceiling $1-(1-p)^{r+1}$ raised to $k$, to the unconditional ceiling $1-q$, is itself a measurable diagnostic of where intervention should occur.

**Limitations list.**

- *Assumed $k=5$.* Sensitivity: success varies by orders of magnitude across $k \in [2,10]$ (Section 4.4); the headline number is meaningless without a measured $k$ distribution.
- *Assumed $p=0.8$.* Sensitivity: manual success ranges from $0.078$ to $0.774$ across $p \in [0.6, 0.95]$ at $k=5$ (Section 4.5).
- *Independence of retrievals.* If failures correlate, the multiplicative model overstates the penalty and the agent advantage; direction of error is known, magnitude is not.
- *Binary artifacts.* Semantic partial usability (an abundance table with undocumented columns) is not modeled.
- *$q=0$ assumed for the agent figures.* Any missing-artifact rate caps success at $1-q$; the motivating work's own text implies $q > 0$ for intermediate data [1].
- *Cost measured in visits only.* Human time per visit, compute cost of pipeline execution, and synthesis effort are outside the model.
- *No empirical validation.* No parameter of the model has been measured against a corpus of published omics studies; the work is analytical throughout.

An adjacent limitation is bibliographic: the corpus available to this paper contains few works directly on scientific-data retrieval agents [1], [6], [8], and several supplied entries ([9], [10], [11], [12]) carry summaries too thin to support detailed engagement; the related-work treatment is correspondingly constrained to what those entries state.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** Three user groups follow directly from the model's quantities. Journal and repository operators could compute and publish a reuse-readiness figure for each deposit — in the simplest form, the measured dispersal breadth $k$ and the presence/absence flag for each artifact class — because Section 4.4 shows $k$ alone moves reproduction success by orders of magnitude. Reanalysis-agent developers could use the retry-substitution result (Section 4.5) to decide between investing in retrieval accuracy and investing in retry logic: the model says retries at fixed per-attempt reliability dominate when failures are independent, a checkable design assumption. Authors preparing supplements could see, from the $k$-sensitivity, that consolidating reproduction-critical artifacts into fewer locations is the single highest-leverage deposition action, since each removed artifact multiplies the reuser's success probability by $1/p$.

**(b) Current readiness.** This work is purely analytical: closed-form models with assumed parameters, no measurements, and no peer review. Against the NASA Technology Readiness Level definitions, it sits at TRL 1–2 (basic principles observed and reported; concept formulated). It does not exceed TRL 3 under any framing, since no component of the model has been tested against even a laboratory-scale corpus, and no manufacturing or deployment readiness is claimed.

**(c) The smallest next test.** The minimal de-risking measurement is a retrieval audit on a small corpus: take $n = 20$ published omics studies, enumerate their reproduction-critical artifacts under a fixed decomposition convention, record for each artifact its location and whether an automated retrieval attempt (and a single retry on failure) obtains it. This yields measured distributions of $k$, $p$, and the second-attempt success rate. The outcome that refutes the model is a second-attempt success rate near zero (persistent failures), which would invalidate the independence assumption underlying the retry mechanism (Section 4.3). The outcome that refutes the practical significance is a measured $k$ distribution concentrated near $1$–$2$, where the manual-agent gap is only $1.0$–$1.5\times$ (Section 4.4).

**(d) Binding constraints.** In the order they would bind for an eventual agent system: first, the missing-artifact fraction $q$, since no retrieval engineering recovers never-deposited data (Section 4.6) and the motivating work indicates intermediate data are irregularly shared [1]; second, the decomposition convention for $k$, which must be standardized before cross-study comparison is meaningful; third, access-control and licensing heterogeneity across repositories, which the declarative data services work identifies as part of why multi-system search spaces are hard — the verifier is whether the stack actually runs [6]; fourth, the choice of underlying language model, which the LiveBench-grounded audit frames as a benchmark-auditable decision [9]. Cost drivers and scale-up constraints cannot be stated quantitatively because no cost inputs are derived in this paper; they are open questions.

**(e) Order-of-magnitude bounds.** The only quantitative projection available from the derivations is about retrieval visits, not money: for a study at $k=5$, both manual and agent-with-retries workflows require on the order of $6$ retrieval visits ($6.25$ and $6.20$ respectively, Sections 4.2–4.3), so the agent's benefit is measured in success probability per visit, not in visit reduction. Any cost figure in currency or compute-hours would require per-visit time and pricing inputs that this paper does not derive, and is therefore not projected here.

**(f) Risks and misuse paths.** A reuse-readiness score derived from this model could be gamed: an author could reduce measured $k$ by merging artifacts superficially (e.g., burying parameters in an unreadable supplementary PDF) without improving actual reusability. Any deployment of the score would need the decomposition convention to resist such gaming, for example by scoring interpretability of each artifact rather than location count alone. A second risk is over-reliance on the conditional success numbers: reporting "$96.0\%$ reproduction success" without the $q > 0$ caveat would misrepresent studies with missing artifacts as retrievable.

## 8. Conclusion

The functional inaccessibility of published omics data, documented qualitatively in the omics data discovery agents work [1], can be expressed as a three-parameter dispersal model: reproduction-critical artifacts $k$, per-location retrieval reliability $p$, and the missing-artifact fraction $q$. Under explicitly assumed parameters ($k=5$, $p=0.8$), the model yields a manual reproduction success of $0.8^5 = 0.32768$ and an agent-with-retries success of $0.992^5 \approx 0.9602$ at nearly identical expected retrieval cost ($6.25$ vs $6.20$ visits), with the gap widening as dispersal grows. The model's durable contributions are its falsifiable structure — persistent second-attempt failures would collapse the retry mechanism — and its identification of $k$ and $q$ as the quantities worth measuring first. The work is analytical at TRL 1–2; its next step is a twenty-study retrieval audit that would either supply measured parameters or refute the independence assumption on which the agent advantage rests.

## References

[1] arXiv:2603.10161v3 | Omics Data Discovery Agents: Agent-Supported Retrieval, Reanalysis, and Synthesis of Published Omics Data

[2] arXiv:2203.08975v2 | A Survey of Multi-Agent Deep Reinforcement Learning with Communication

[3] arXiv:1703.04355v2 | A Meshless-based Local Reanalysis Method for Structural Analysis

[4] arXiv:1907.02664v2 | Data Encoding for Byzantine-Resilient Distributed Optimization

[5] arXiv:2005.07866v1 | Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data

[6] arXiv:2605.20690v2 | Declarative Data Services: Structured Agentic Discovery for Composing Data Systems

[7] arXiv:1110.5626v1 | Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data

[8] arXiv:2603.02888v1 | LLandMark: A Multi-Agent Framework for Landmark-Aware Multimodal Interactive Video Retrieval

[9] QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026)

[10] QNFO: Pillar 3: PBO/Autaxys — Pattern-Based Ontology as Intrinsic Self-Ordering

[11] QNFO: Information-theoretic Limits on Programmatic Specification of Biological Systems | DOI 10.64898/2026.07.27.740886

[12] QNFO: The Substrate Is the Algorithm: A Categorical Formalization of the Strongest Consilience Thread