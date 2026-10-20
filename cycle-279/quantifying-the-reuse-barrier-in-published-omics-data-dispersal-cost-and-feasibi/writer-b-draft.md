# Quantifying the Reuse Barrier in Published Omics Data: Dispersal, Cost, and Feasibility Models for Agent-Supported Retrieval, Reanalysis, and Synthesis

## Abstract

Most published omics data remain functionally inaccessible for computational reuse: the information needed to reproduce a reported result is dispersed across article main text, supplementary files, and code repositories, and intermediate data such as protein abundance tables are shared irregularly if at all [1]. Existing descriptions of this problem are qualitative; no published model states what the dispersal costs a reuser or what an agent changes. This paper supplies that model. We formalize a published study as a set of reproduction-critical artifacts dispersed over document locations, derive closed-form expressions for reproduction success probability and expected retrieval cost, derive a token-and-call cost model for the retrieval stage of an agent pipeline, and derive an information-theoretic bound on the metadata an agent must extract. Under stated assumptions (five dispersed artifacts, per-location retrieval success 0.8), a manual reproduction succeeds with probability 0.32768 and needs 6.25 expected retrieval visits, while an agent with two retries succeeds with probability 0.9606 at 6.20 visits; the retrieval stage costs 60400 tokens and 30 calls per paper before screening. The model turns "most data are inaccessible" into three measurable quantities — dispersal breadth, per-location reliability, and missing-artifact fraction — giving repository operators and agent developers concrete targets for measurement and deposition policy.

## 1. Introduction

A computational biologist who wants to reanalyze a published proteomics or genomics study faces a concrete, recurring obstacle. The raw data may sit in a public repository, but the parameters that produced the reported results, the filtering thresholds, the pipeline version, and the mapping from supplementary figures to underlying tables are scattered across the article main text, supplementary files, and, where they exist at all, code repositories; intermediate artifacts such as protein abundance tables are shared only in a minority of cases and at irregular locations [1]. The practical consequence is that a reanalysis that should take hours instead takes days or fails outright, and the aggregate effect is that most published omics data are functionally inaccessible for computational reuse even when they are technically downloadable [1]. This blocks specific decisions: whether to build on a published dataset rather than generate new data, whether a reported result survives an alternative processing choice, and whether a meta-analysis across studies can be assembled at all. Today the cost of reconstruction is paid in human hours, one paper at a time.

The motivating framework, ODDA, demonstrates that the barrier is not absolute: across five worked reanalyses spanning proteomics and RNA sequencing, language-model agents operating containerized tools recovered processing parameters from article text and reproduced deposited quantities with per-sample Pearson correlations of 0.85–0.997 and, where differential expression was performed, concordant fold changes (Spearman 0.88–0.91) [1]. But the same evaluation records, for each study, the human guidance and workflow accommodations required — software-version substitutions, prompts to match the article's tool version, instrument-format conversions, disabled options, and normalization decisions [1]. Demonstrated success therefore coexists with a measurable residue of human curation, and that residue is exactly what a quantitative model of the dispersal barrier should predict.

If the dispersal barrier could be quantified per study, three things change. A journal or repository could report a single reuse-readiness figure alongside a deposit. A reanalysis agent could allocate its retrieval budget to the locations that dominate the failure probability. And an author preparing a supplement could see which missing artifact contributes most to the expected cost imposed on every future reuser. Conversely, if the information an agent must extract to specify a reanalysis exceeds what the published record reliably contains, then no amount of agent capability closes the gap, and the binding constraint is publication practice itself. Both outcomes are actionable, and this paper derives conditions for each.

This work treats the pipeline proposed in [1] as the object of analysis. It does not propose a new agent architecture; it derives the cost structure, the information requirements, and the failure modes of any agent that performs the three functions — retrieval, reanalysis, synthesis — that [1] names. The analysis draws on the multi-agent systems literature for the coordination structure [2], on the distributed-systems literature for the reliability question that arises when a pipeline is assembled from independently fallible retrieval steps [4], [5], and on adjacent formal work for comparative framing [3], [6], [7], [8], [10].

The contributions are:

- A staged formalization of the omics discovery pipeline as a five-stage multi-agent workflow, with the coordination structure of each stage stated explicitly (Section 3).
- A dispersal model of a published study with closed-form expressions for reproduction success probability and expected retrieval cost, evaluated numerically under stated assumptions: manual success 0.32768 versus agent success 0.9606 at $k = 5$, $p = 0.8$, $r = 2$ (Sections 3 and 4.4–4.5).
- A derived token-and-call cost model for the retrieval stage, giving 60400 tokens and 30 calls per paper before screening, and 169400 tokens with a 10:1 screening ratio (Section 4.1).
- A derived information-theoretic bound on the reanalysis specification, giving Hartley entropy 83.05 bits at 25 fields and a Shannon-entropy comparison (Section 4.2).
- A sensitivity decomposition showing that dispersal breadth $k$ dominates the barrier and that agent retries substitute for per-location reliability (Sections 4.4–4.7).
- A statement of which observations would falsify the central claims, a limitations list naming every assumption, and a practical pathway from the analytical result to a first measurement (Sections 6 and 7).

## 2. Background and Related Work

The direct object of this paper is the omics data discovery agents framework, which presents ODDA, an agentic system in which language-model agents read the scientific literature, locate associated data, and reprocess it using containerized tools through a controlled, auditable interface [1]. Its author summary states the core observation motivating everything here: reuse is rare in practice because the information needed to make sense of a dataset — which samples are which, how the data were processed, and with which software — is scattered across the article, its supplementary files, and code repositories [1]. Its evaluation section defines successful completion as an end-to-end run comprising raw-data retrieval, parameter recovery from the article, tool selection, containerized execution, sample matching to the deposited design, and comparison with the deposited quantities, and it distinguishes successful completion from fully autonomous execution by recording the human guidance required per study [1]. Its results give the demonstrated payoff: per-sample Pearson correlations of 0.85–0.997 for shared features, identification Jaccard 0.90 for one study, and Spearman 0.88–0.91 for fold changes, with residual differences attributed to threshold placement, tool-version, and preprocessing differences rather than lost signal [1]. What that work does not provide is a quantitative cost model of the dispersal barrier itself — the success probabilities, token budgets, and information requirements that determine whether the barrier binds before agent capability does — and that model is the gap this paper addresses.

A second thread concerns how multiple cooperating agents coordinate. The survey of multi-agent deep reinforcement learning with communication establishes that communication is an effective mechanism for coordinating the behaviors of multiple agents, broadening their views of the environment, and supporting their collaborations, and that agents can communicate various types of messages either to all agents or to subsets of other agents [2]. The survey classifies the literature along nine dimensions and observes that communication is viewed as a vital means to tackle partial observability and non-stationarity in multi-agent reinforcement learning [2]. In the omics retrieval setting, the analogue is a division of labor in which one agent reads the article text while another queries repositories and a third executes code; the survey's framing supports treating such message-passing as the coordination primitive, though it concerns learning agents rather than scientific documents.

Retrieval and generation over large, heterogeneous data collections is treated in TerraGen, a unified multi-task layout generation framework for remote sensing data augmentation that addresses task isolation — the situation in which each vision task requires training an independent generative model — by integrating diverse spatial conditions with textual descriptions in one framework [8]. TerraGen's evaluation constructs a benchmark of 1k carefully selected high-quality images and introduces specialized metrics tailored for spatial accuracy and semantic consistency, encompassing pixel-level fidelity and structural coherence [8]. Two structural lessons transfer. First, a unified framework that serves multiple tasks replaces a family of task-isolated pipelines, which is the shape a single reuse pipeline serving proteomics, transcriptomics, and metabolomics should take. Second, TerraGen's practice of defining task-specific evaluation metrics alongside its benchmark is the template for the reuse-readiness metrics proposed in Section 7: a score is only as good as the specialized metric definitions behind it.

Agentic discovery over data systems is examined in the declarative data services work, which observes that translating LLM-driven agentic discovery to multi-system data backends surfaces a harder problem: the search space is heterogeneous, the verifier is whether a deployed stack actually runs, and composition knowledge is unevenly captured in pretraining [6]. That work formalizes the common shape of agentic discovery as structured agentic search — an LLM-driven agent explores a typed solution space, a verifier evaluates each candidate, and the loop refines under structured feedback — and reports that on a multi-system stack a coding agent that succeeds on a single repository fails to converge consistently [6]. It further identifies, as its most important next step, an evaluator peer layer that would ask whether a deployed stack actually meets declared intent, converting correctness into a structured search over typed probes [6]. This maps directly onto omics reanalysis, where the verifier is whether a retrieved pipeline actually reproduces the published result and where pipeline-composition knowledge is exactly the kind of knowledge unevenly captured in pretraining; the evaluator-layer idea motivates the reproduction-verifier stage $S_4$ of Section 3.

Reliability of distributed computation under partial failure is the subject of two works on Byzantine resilience. Data encoding for Byzantine-resilient distributed optimization studies distributed optimization where data and computation are distributed among $m$ worker machines, $t$ of which may be corrupt, with compromised nodes able to collaboratively and arbitrarily deviate from their pre-specified programs while a designated master node iteratively computes the model or parameter vector [4]. That work shows how the corrupt worker set can be identified efficiently from the shared support of error vectors, and validates its methods in numerical experiments of distributed gradient descent and coordinate descent for linear regression with $m = 15$ worker nodes [4]. Byzantine-resilient SGD in high dimensions on heterogeneous data considers the master-worker architecture under Byzantine attacks with heterogeneous local datasets and no probabilistic assumptions on data generation, using a polynomial-time outlier-filtering procedure for robust mean estimation at its core [5]. Its convergence theorem gives an explicit resilience condition: if an $\epsilon$ fraction of $R$ workers is adversarially corrupt and $\epsilon \leq \frac{1}{4} - \epsilon'$ for an arbitrary constant $\epsilon' > 0$, convergence holds with probability at least $1 - T\exp(-\epsilon'^2(1-\epsilon)R/16)$ [5]. In the omics setting the failures are not adversarial, but the structural question is identical: when a reproduction pipeline is assembled from $k$ independently fallible retrieval steps, end-to-end reliability is a function of per-step reliability, and this literature supplies both the master-worker vocabulary and an explicit corrupt-fraction threshold that Section 4.8 parallels with its own majority-vote arithmetic.

Local reanalysis methods appear in structural engineering: the meshless-based local reanalysis (MLR) method extends reanalysis methods to the Kriging interpolation meshless method, using two reanalysis methods — combined approximations and indirect factorization updating — in view of the high computational cost of meshless methods [3]. There, "reanalysis" means recomputing a modified structural model cheaply from a previously solved one. The transferable idea is that reanalysis is worthwhile exactly when full recomputation is expensive, which is the economic premise of omics reanalysis as well: a reuser reanalyzes published data because regenerating the data is far more expensive than reconstructing the analysis.

Reuse of existing measured data for parameter constraint is illustrated by the dark-energy study that uses 13 H II starburst galaxy apparent magnitude versus redshift measurements from Siegel et al. (2005) to constrain cosmological model parameters by $\chi^2$ minimization, finding constraints generally consistent with those derived using other datasets but not as restrictive as the tightest currently available [7]. This is a concrete instance of the payoff side of the ledger: published data, when retrievable, support new scientific constraints, and the quality of what can be extracted depends on what the data can support — an analogy for the information loss incurred when reanalysis works from published rather than raw records.

Finally, model selection for the retrieval agent is an auditable, benchmark-grounded decision with a quantified cost spread. The LiveBench-grounded audit of frontier large language models for scientific research and agentic AI reports, from the LiveBench 2026-06-25 contamination-free benchmark, that no Llama model ranks in the top 42, and that DeepSeek V4 Pro 0813 is the mathematics price-performance optimum at 95.1 Mathematics score and USD 0.044 per benchmark run, within a frontier-mathematics class whose cost per run spans USD 0.044 to USD 1.439 — a 33-fold range [10]. The same audit finds that the agentic capability axis inverts the mathematics ranking, with Claude 5 Opus Thinking at 65.2 followed closely by open-weights models, and that DeepSeek V4 Pro 0813 scores 54.9 on that axis [10]. For this paper, the audit's relevance is that per-run cost and capability profile are model-dependent free parameters in the cost model of Section 4.1, and that the 33-fold spread makes model choice economically material at corpus scale (Section 7).

## 3. Methods

### 3.1 Pipeline formalization

Following [1], the pipeline has three functions — retrieval, reanalysis, and synthesis. We formalize these as five sequential stages, each implemented by a specialist agent in the modular, communicating pattern of [2]:

$$
S_1 \rightarrow S_2 \rightarrow S_3 \rightarrow S_4 \rightarrow S_5
$$

with stages:

- $S_1$ (corpus scan): identify candidate papers and determine whether omics data exist for each.
- $S_2$ (asset location): locate raw data deposits in public repositories and any intermediate data files, whose location [1] notes is irregular.
- $S_3$ (protocol extraction): reconstruct the analysis pipeline from main text, supplementary files, and code repositories [1].
- $S_4$ (reanalysis execution): run the reconstructed pipeline on the located data, with a verifier of the form used in agentic discovery over deployed stacks — the pipeline either runs and reproduces a reported result or it does not [6].
- $S_5$ (synthesis): aggregate reanalyzed outputs across studies into a common, searchable form.

Each stage $S_i$ has an input context $C_i$, an output record $O_i$, and a message channel to downstream stages, in the sense of [2] that communication broadens each agent's view of the shared environment. The output record $O_3$ — the extracted protocol — is the pivotal artifact: it is the metadata specification on which $S_4$ depends, and Section 4.2 bounds its information content.

### 3.2 Dispersal model of a published omics study

We model a published omics study as a set $A = \{a_1, \dots, a_k\}$ of $k$ reproduction-critical artifacts. An artifact is any item a reuser must obtain to reproduce or extend a reported result: the raw data deposit, the processing parameters, the pipeline code, an intermediate table such as a protein abundance matrix, or a mapping from figure to underlying data. Each artifact $a_i$ resides in exactly one location $\ell_i$ drawn from the set of document locations $L$ = {article main text, supplementary files, code repository, external repository landing page, author contact}. The dispersal breadth of the study is $k$; the location spread is the number of distinct elements among $\{\ell_1, \dots, \ell_k\}$.

The central empirical claim of the motivating work is that the information needed to reproduce a result "is dispersed across main text, supplementary files, and code repositories" and that intermediate data are shared only irregularly [1]. The model makes that claim parameterized: $k$ and the location spread are measurable per study.

### 3.3 Retrieval reliability

Let $p \in [0,1]$ be the per-attempt success probability of retrieving and correctly interpreting a single artifact from its location. For a human reuser, $p$ aggregates finding the location, gaining access, and interpreting the artifact. For an agent, we separate a first-attempt success probability $p$ from $r$ independent retries at the same location, each succeeding with probability $p$ conditional on prior failures being independent. The per-location success probability with $r$ retries is

$$P_{\text{loc}}(p, r) = 1 - (1-p)^{r+1}.$$

### 3.4 End-to-end reproduction success and cost

Assuming artifact retrievals are independent, the end-to-end reproduction success probability is

$$P_{\text{rep}} = \prod_{i=1}^{k} P_{\text{loc},i},$$

which under the homogeneous assumption $P_{\text{loc},i} = P_{\text{loc}}$ becomes

$$P_{\text{rep}}(k, p, r) = \left[1 - (1-p)^{r+1}\right]^{k}.$$

The expected number of retrieval visits per artifact is the mean of a geometric random variable truncated at $r+1$ attempts:

$$E[N] = \sum_{j=1}^{r+1} j \, (1-p)^{j-1} p + (r+1)(1-p)^{r+1},$$

which for the no-retry case $r = 0$ reduces to $E[N] = 1/p$. The expected total retrieval visits for the study is $k \cdot E[N]$.

### 3.5 Cost-model and information-model inputs

The token cost model of Section 4.1 takes as free parameters: paper length in tokens $L$, the number of documents consulted per paper $D$, the number of decision fields to extract $F$, and tokens per extraction call overhead $f_{\text{oh}}$. All values used are stated assumptions of this analysis, not measurements; they are chosen to bracket the range a typical omics paper plausibly occupies, and Section 6 treats their sensitivity explicitly.

Section 4.2 applies a dual Hartley/Shannon framing. For a protocol specification with $F$ independent fields, each with $n_j$ admissible values, the Hartley entropy is

$$H_0 = \log_2 \prod_{j=1}^{F} n_j = \sum_{j=1}^{F} \log_2 n_j,$$

and the Shannon entropy $H = -\sum_j p_j \log_2 p_j \leq H_0$ measures the uncertainty actually reduced by extracted evidence. $H_0$ bounds what a complete specification must be able to express; $H$ bounds what an agent must resolve per paper.

### 3.6 What the model does not claim

The dispersal model treats artifacts as binary (retrieved or not) and retrievals as independent. It does not model semantic difficulty, cross-artifact consistency checking, or the compute cost of executing a retrieved pipeline; those enter only as qualitative considerations. All numerical results below follow from the closed forms above with stated inputs.

## 4. Analysis

### 4.1 Token-and-call cost of the retrieval stage

**Inputs (stated assumptions of this analysis).** Paper main text: $L = 8000$ words at $1.3$ tokens per word, giving $L_{\text{tok}} = 8000 \times 1.3 = 10400$ tokens. Supplementary and code documents consulted: $D = 5$ documents, average $2000$ tokens each, giving $5 \times 2000 = 10000$ tokens. Decision fields to extract: $F = 25$ (a bracket of 10 to 40 is carried through). Tokens per call overhead (prompt scaffolding, schema, tool descriptions): $f_{\text{oh}} = 500$. One extraction call per field plus one summarization call per document gives $D + F$ calls.

**Arithmetic.** Total structured input tokens:

$$T_{\text{in}} = L_{\text{tok}} + D \times 2000 + (D + F) \times f_{\text{oh}}.$$

With $L_{\text{tok}} = 10400$, $D = 5$, $F = 25$, $f_{\text{oh}} = 500$:

$$T_{\text{in}} = 10400 + 10000 + 30 \times 500 = 10400 + 10000 + 15000 = 35400 \text{ tokens}.$$

Each extraction call also carries document context; assume the agent re-reads an average of $1000$ tokens per extraction call, adding $F \times 1000 = 25000$ tokens:

$$T_{\text{total}} = 35400 + 25000 = 60400 \text{ tokens per paper}.$$

Number of agent calls:

$$N_{\text{calls}} = D + F = 5 + 25 = 30 \text{ calls per paper}.$$

**Bracketing.** For $F \in \{10, 40\}$, holding other inputs fixed:

- Lower: $T_{\text{total}} = 10400 + 10000 + (5+10) \times 500 + 10 \times 1000 = 10400 + 10000 + 7500 + 10000 = 37900$ tokens; $N_{\text{calls}} = 15$.
- Upper: $T_{\text{total}} = 10400 + 10000 + (5+40) \times 500 + 40 \times 1000 = 10400 + 10000 + 22500 + 40000 = 82900$ tokens; $N_{\text{calls}} = 45$.

If the corpus-scan stage $S_1$ must screen $S = 10$ candidate papers per accepted paper, each at $L_{\text{tok}} = 10400$ tokens with one call of overhead $500$, the screening cost is $10 \times (10400 + 500) = 109000$ tokens, and the full retrieval stage for one accepted paper is

$$T_{\text{retr}} = 109000 + 60400 = 169400 \text{ tokens},$$

with bracket $T_{\text{retr}} \in [146900, 191900]$ tokens. These are projections under the stated assumptions, not measurements.

### 4.2 Information bound on the reanalysis specification

**Inputs.** The extracted protocol must fix, per [1], the pipeline steps, parameters, software versions, input files, and output definitions. Assume $F = 25$ fields with geometric-mean cardinality $\bar{n} = 10$ admissible values per field (e.g., a normalization method chosen among roughly ten standard options). Then:

$$H_0 = F \log_2 \bar{n} = 25 \times \log_2 10 = 25 \times 3.3219 = 83.05 \text{ bits}.$$

For the bracket $F \in \{10, 40\}$:

- Lower: $H_0 = 10 \times 3.3219 = 33.22$ bits.
- Upper: $H_0 = 40 \times 3.3219 = 132.88$ bits.

**Shannon comparison.** If the most common value of each field has probability $p = 0.5$ and the remaining $0.5$ is spread over the other nine values, then with probability $0.5$ the field is resolved for free and with probability $0.5$ it carries at most $\log_2 10 = 3.3219$ bits:

$$H \leq 0.5 \times 0 + 0.5 \times 3.3219 = 1.661 \text{ bits per field},$$

and over $F = 25$ fields, $H \leq 25 \times 1.661 = 41.5$ bits. The gap between $H_0 = 83.05$ bits and $H \leq 41.5$ bits is the dual-face result: the specification space the agent must be able to express is, in this parameterization, twice what a typical paper actually resolves, which is why defaults and conventions absorb part of the curation burden.

**The binding constraint.** The bound that matters for feasibility is not the agent's capacity to express $H_0 \approx 83$ bits — trivially small by machine standards — but whether the published record contains the evidence to resolve those bits. [1] states that the needed information is dispersed across main text, supplementary files, and code repositories, and that intermediate data locations are irregular; the information-theoretic framing says the agent's task is to reduce $H$ to $0$ per field using only those dispersed sources. Where a field's value is stated nowhere, its conditional entropy stays at its prior, and the reanalysis is underdetermined. This is the formal statement of the accessibility gap [1] describes qualitatively.

### 4.3 Reusability index

Define the reusability index $R$ as the fraction of fields an agent can resolve from the published record without human intervention:

$$R = \frac{F_{\text{resolved}}}{F}.$$

Under the Shannon model of Section 4.2, if each field is stated with probability $p = 0.5$, then $F_{\text{resolved}} = pF$ and $R = p = 0.5$. Sensitivity: $R$ is linear in $p$. If publication practice improves so that $p = 0.9$, the human curation burden per paper falls from $F(1 - 0.5) = 12.5$ fields to $F(1 - 0.9) = 2.5$ fields — a fivefold reduction, computed as $12.5 / 2.5 = 5$. The agent absorbs exactly the resolved fraction, and the residual $(1 - R)F$ fields are the irreducible human cost under current practice. These are model projections, not measurements of any corpus; the per-study human guidance recorded in the ODDA evaluation [1] is the empirical counterpart this index would quantify.

### 4.4 Manual reproduction (no retries, r = 0)

With $r = 0$, per-location success is $P_{\text{loc}} = p = 0.8$. End-to-end, with $k = 5$:

$$P_{\text{rep}}(5, 0.8, 0) = 0.8^5.$$

Computing step by step: $0.8^2 = 0.64$; $0.8^3 = 0.64 \times 0.8 = 0.512$; $0.8^4 = 0.512 \times 0.8 = 0.4096$; $0.8^5 = 0.4096 \times 0.8 = 0.32768$.

$$P_{\text{rep}}(5, 0.8, 0) = 0.32768.$$

Under these assumptions a manual reproduction attempt succeeds about 32.8% of the time; roughly two of every three attempts fail. Expected retrieval visits per artifact with $r = 0$ is $E[N] = 1/p = 1/0.8 = 1.25$, and total expected visits:

$$k \cdot E[N] = 5 \times 1.25 = 6.25.$$

### 4.5 Agent reproduction with r = 2 retries

Per-location success with two retries:

$$P_{\text{loc}}(0.8, 2) = 1 - (1-0.8)^3 = 1 - 0.2^3 = 1 - 0.008 = 0.992.$$

End-to-end:

$$P_{\text{rep}}(5, 0.8, 2) = 0.992^5.$$

Computing: $0.992