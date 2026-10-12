# Agent-Supported Discovery, Reanalysis, and Synthesis of Published Omics Data: A Cost and Feasibility Analysis of the Agentic Retrieval Pipeline

## Abstract

The biomedical literature contains a vast collection of omics studies, yet most published data remain functionally inaccessible for computational reuse: the information needed to reproduce a reported result is dispersed across main text, supplementary files, and code repositories, and intermediate data such as protein abundance tables are shared irregularly if at all [1]. This paper addresses the gap between data availability and data reusability by modeling, rather than merely proposing, an agentic retrieval-reanalysis-synthesis pipeline. We formalize the pipeline as a staged multi-agent workflow, derive a token-and-call cost model for the retrieval stage, derive an information-theoretic lower bound on the metadata an agent must extract before a reanalysis can be specified, and derive a reusability index that quantifies how much of the reuse burden shifts from human curation to agent execution. Under stated assumptions (a paper of $8{,}000$ words, a five-stage pipeline, and a per-stage extraction scope of $10$ to $40$ decision fields), the retrieval stage requires on the order of $10^{4}$ to $10^{5}$ tokens per paper, and the metadata specification carries a Hartley entropy of at least $\log_{2} 10^{10} \approx 33.2$ bits, which bounds how much curation effort any agent can absorb. The results change practice by giving repository operators and method developers concrete budgets for what an omics discovery agent must extract, verify, and record per study.

## 1. Introduction

Biomedical researchers who want to reuse published omics data face a concrete, daily obstacle. A computational biologist who wishes to reanalyze a published proteomics or transcriptomics study must first locate the raw data in a public repository, then reconstruct the analysis pipeline from fragments scattered across the main text, supplementary files, and code repositories; in the rarer cases where intermediate data such as protein abundance files are shared, their location is irregular and must be discovered by hand [1]. This is the problem the omics data discovery agent is built to solve: an agent-supported workflow for retrieval, reanalysis, and synthesis of published omics data [1]. Today the cost of that reconstruction is paid in human hours, one paper at a time, and the result is that most published data remain functionally inaccessible for computational reuse even when they are technically deposited [1]. The decision that changes if the present analysis holds is a design decision: repository operators, journal editors, and agent developers can specify, budget, and verify exactly which metadata fields an agent must extract per study, instead of treating reuse as an open-ended research problem.

The stakes are concrete. Every published omics study whose pipeline cannot be reconstructed is a lost replication opportunity and a lost input to meta-analysis and synthesis. If an agentic framework can be shown to have a bounded, predictable cost per paper — in tokens, calls, and extracted fields — then reuse can be planned as an engineering process with a per-study budget, rather than attempted ad hoc. Conversely, if the information an agent must extract to specify a reanalysis exceeds what the published record reliably contains, then no amount of agent capability will close the gap, and the binding constraint is publication practice itself. Both outcomes are actionable, and this paper derives conditions for each.

This work treats the pipeline proposed in [1] as the object of analysis. It does not propose a new agent architecture; it derives the cost structure, the information requirements, and the failure modes of any agent that performs the three functions — retrieval, reanalysis, synthesis — that [1] names. The analysis draws on the multi-agent systems literature for the coordination structure [2], [8], on the distributed-systems literature for the resilience question that arises when autonomous agents act on untrusted repository content [4], [5], and on the information-theoretic analysis of biological specification [11] for the bound on what metadata can capture.

The contributions are:

- A staged formalization of the omics discovery pipeline as a five-stage multi-agent workflow, with the coordination structure of each stage stated explicitly (Section 3).
- A derived token-and-call cost model for the retrieval stage, with full arithmetic, giving a per-paper budget of $1.6 \times 10^{4}$ to $1.6 \times 10^{5}$ tokens under stated assumptions (Section 4.1).
- A derived information-theoretic lower bound on the metadata specification required for reanalysis, giving $H_0 \geq 33.2$ bits of Hartley entropy and a Shannon-entropy comparison (Section 4.2).
- A derived reusability index $R$ that quantifies the fraction of reuse effort transferable from human curation to agent execution, evaluated over the parameter range of the cost model (Section 4.3).
- A resilience analysis of the pipeline against corrupted or adversarial repository content, adapted from the Byzantine-resilient distributed optimization setting (Section 4.4).
- A statement of which observations would falsify the central claims, and a limitations list naming every assumption the results rest on (Section 6).

## 2. Background and Related Work

The direct object of this paper is the omics data discovery agent framework of Hutton and Meyer, which presents an agentic framework for agent-supported retrieval, reanalysis, and synthesis of published omics data [1]. Its motivating observation, which this paper takes as its starting problem statement, is that most published omics data remain functionally inaccessible for computational reuse because the information needed to reproduce reported results is dispersed across main text, supplementary files, and code repositories, and intermediate data such as protein abundance files are shared irregularly and at unpredictable locations [1]. The summary supplied for [1] describes the framework and its motivation but gives no quantitative performance figures; accordingly, this paper treats [1] as the qualitative specification of the pipeline and supplies the quantitative analysis that its summary does not contain.

The coordination structure of the pipeline places it in the multi-agent systems literature. The survey of multi-agent deep reinforcement learning with communication establishes that communication is an effective mechanism for coordinating the behaviors of multiple agents, broadening their views of the environment, and supporting their collaborations, and that agents can communicate various types of messages, either to all agents or to subsets [2]. The summary supplied for [2] is truncated before its specific findings on message types are completed; this paper uses only the general claim it states — that inter-agent communication coordinates behavior and broadens environmental views — as the justification for modeling the omics pipeline as communicating specialist agents rather than a single monolithic model. The same modular pattern appears outside biology: LLandMark is a modular multi-agent framework for landmark-aware multimodal interactive video retrieval, featuring specialized agents that collaborate across four stages to handle real-world complex queries in a domain where the diversity and scale of data demand multimodal understanding, adaptive reasoning, and domain-specific knowledge integration [8]. The structural analogy is direct — both [1] and [8] decompose a retrieval problem into specialized collaborating agents across sequential stages — and this paper uses the four-stage decomposition of [8] as a comparative template when formalizing the five-stage omics pipeline in Section 3.

A second relevant thread is agentic discovery over heterogeneous data backends. Declarative Data Services observes that agentic discovery has shown that LLM-driven search can find novel algorithms, designs, and code under benchmark conditions, but that translating the paradigm to multi-system data backends surfaces a harder problem: the search space is heterogeneous, the verifier is whether a deployed stack actually runs, and composition knowledge is unevenly captured in pretraining [6]. This is precisely the difficulty the omics setting inherits: the "backend" is the set of public omics repositories, the search space is heterogeneous across repositories and file formats, and the verifier for a retrieved dataset is whether the reported reanalysis actually runs on it. The summary of [6] is truncated before its proposed solution is stated; this paper uses only the problem statement it supplies, and treats the verifier-runs question as an open design constraint carried into Sections 4 and 6.

The resilience question — what happens when an autonomous agent reads content that is wrong or adversarially corrupted — has a formal analogue in distributed optimization. The Byzantine-resilient distributed optimization setting studies distributed optimization where both data and computation are distributed among $m$ worker machines, $t$ of which may be corrupt, with compromised nodes able to collaboratively and arbitrarily deviate from their pre-specified programs while a designated master node iteratively computes the model or parameter vector for generalized linear models [4]. The Byzantine-resilient SGD work extends this to high dimensions on heterogeneous data, considering a master-worker architecture under Byzantine attacks with heterogeneous local datasets and no probabilistic assumptions on data generation, using a polynomial-time outlier-filtering procedure for robust mean estimation at its core [5]. Neither summary states its resilience threshold or convergence guarantee in the supplied text; this paper therefore imports only the structural mapping — repository-provided metadata and agent-extracted fields play the role of worker messages, and a corrupted or mislabeled repository record plays the role of a Byzantine worker — and derives the corresponding majority-vote requirement arithmetically in Section 4.4 rather than citing a threshold the sources do not state.

Reanalysis as a general computational concept predates the agentic setting. The meshless-based local reanalysis method for structural analysis extends reanalysis methods to the Kriging interpolation meshless method, utilizing combined approximations and indirect factorization updating, motivated by the computational cost of meshless methods [3]. Its summary is truncated before quantitative results; the relevance here is conceptual only: reanalysis is the practice of recomputing a system's response after a modification without redoing the full analysis from scratch, and the omics reanalysis stage of [1] is the biological analogue — recomputing a study's result under a modified hypothesis without re-collecting the data. This paper uses that analogy once, in Section 3, and makes no further claim about [3].

Two QNFO corpus items supply the information-theoretic grounding. The information-theoretic limits work shows via information theory that an organism does not contain enough organism-specific information to specify its own microscopic organization, that the genome is a generator specification rather than a trajectory program, and that it establishes a coarse-graining threshold with dual Hartley and Shannon entropy faces [11]. This paper borrows the dual Hartley/Shannon framing — Hartley entropy ($H_0 = \log_{2} N$, the log of the number of possibilities) for counting the discrete metadata fields an agent must resolve, Shannon entropy for the uncertainty actually reduced by extracted evidence — and applies it to metadata specification rather than organism specification. The categorical formalization work states the Capability(S) $\sim$ End(X_S) conjecture, a five-pillar verification program, and a Church-Turing-scoped resource-level thesis distinguishing computability-level equivalence from resource-level difference [12]. Its supplied summary is a fragment; the paper uses only the resource-level distinction it names, in Section 6, to separate the question of whether an agent can in principle perform a reanalysis (computability) from what it costs (resources).

Finally, two works serve as boundary markers. The dark-energy constraints paper uses H II starburst galaxy apparent magnitude versus redshift data from Siegel et al. (2005) to constrain dark energy cosmological model parameters, finding constraints generally consistent with those from other data sets but not as restrictive as the tightest currently available [7]. It is included here as a worked instance of the exact practice the omics pipeline automates: reanalysis of a published dataset to derive a new constraint, with an honest statement that the reused data yield weaker constraints than purpose-collected data — an analogy for the information loss incurred when reanalysis works from published rather than raw records. The LiveBench-grounded audit of frontier large language models for scientific research and agentic AI reports, from the LiveBench 2026-06-25 contamination-free benchmark, that no Llama model ranks in the top 42 and that DeepSeek V4 Pro 0813 is the mathematics price-performance optimum [9]; its supplied summary is truncated mid-sentence, so this paper uses only those two stated findings, as the basis for the assumption in Section 4 that the retrieval agent runs on a frontier-class model whose per-token cost is a free parameter. The PBO/Autaxys pattern-based ontology entry states only its title-level thesis, pattern-based ontology as intrinsic self-ordering, with no further detail in the supplied summary [10]; it is cited here only to acknowledge that ontology-learning approaches to scientific data organization exist as an alternative to the field-extraction approach modeled in this paper, and no claim about its content is made beyond what the summary states.

## 3. Methods

### 3.1 Pipeline formalization

Following [1], the pipeline has three functions — retrieval, reanalysis, and synthesis. We formalize these as five sequential stages, each implemented by a specialist agent in the modular pattern of [2] and [8]:

$$
\text{S}_1 \to \text{S}_2 \to \text{S}_3 \to \text{S}_4 \to \text{S}_5
$$

with stages:

- $\text{S}_1$ (corpus scan): identify candidate papers from the literature and determine whether omics data exist for each.
- $\text{S}_2$ (asset location): locate raw data deposits in public repositories and any intermediate data files, whose location [1] notes is irregular.
- $\text{S}_3$ (protocol extraction): reconstruct the analysis pipeline from main text, supplementary files, and code repositories [1].
- $\text{S}_4$ (reanalysis execution): run the reconstructed pipeline on the located data, with a verifier of the form used in agentic discovery over deployed stacks — the pipeline either runs and reproduces a reported result or it does not [6].
- $\text{S}_5$ (synthesis): aggregate reanalyzed outputs across studies.

Each stage $\text{S}_i$ has an input context $C_i$, an output record $O_i$, and a communication channel to downstream stages, in the sense of [2] that communication broadens each agent's view of the shared environment. The output record $O_3$ — the extracted protocol — is the pivotal artifact: it is the metadata specification on which $\text{S}_4$ depends, and Section 4.2 bounds its information content.

### 3.2 Cost model inputs

The cost model of Section 4.1 takes as free parameters: paper length in tokens $L$, the number of documents an agent must consult per paper $D$ (main text, supplementary files, code files, repository records), the number of decision fields to extract $F$, and tokens per extracted field $f$. All values used are stated assumptions of this analysis, not measurements; they are chosen to bracket the range a typical omics paper plausibly occupies, and Section 6 treats their sensitivity explicitly.

### 3.3 Information model

Section 4.2 applies the dual Hartley/Shannon framing of [11]. For a protocol specification with $F$ independent fields, each with $n_j$ admissible values, the Hartley entropy is

$$
H_0 = \log_{2} \prod_{j=1}^{F} n_j = \sum_{j=1}^{F} \log_{2} n_j,
$$

and the Shannon entropy $H = -\sum_j p_j \log_2 p_j \leq H_0$ measures the uncertainty remaining when field values are drawn non-uniformly. The distinction matters because $H_0$ bounds what a complete specification must be able to express, while $H$ bounds what an agent must actually resolve per paper.

### 3.4 Resilience model

Section 4.4 maps the pipeline onto the master-worker Byzantine setting of [4], [5]: each consulted source (repository record, supplementary file, code comment) is a "worker" whose message (a metadata claim) may be corrupt, and the extraction agent is the "master" that must decide a field value from $m$ messages of which $t$ may be wrong. We derive the majority-vote condition arithmetically rather than importing a threshold, since the supplied summaries of [4] and [5] do not state one.

## 4. Analysis

### 4.1 Token-and-call cost of the retrieval stage

**Inputs (stated assumptions of this analysis).** Paper main text: $L = 8{,}000$ words, at $1.3$ tokens per word, giving $L_{\text{tok}} = 8{,}000 \times 1.3 = 10{,}400$ tokens. Supplementary and code documents consulted: $D = 5$ documents, average $2{,}000$ tokens each, giving $5 \times 2{,}000 = 10{,}000$ tokens. Decision fields to extract: $F = 25$ (a bracket of $10$ to $40$ is carried through). Tokens per extraction call overhead (prompt scaffolding, schema, tool descriptions): $f_{\text{oh}} = 500$ tokens per call. One extraction call per field, plus one call per document to summarize it into the context: $D$ summarization calls plus $F$ extraction calls.

**Arithmetic.** Total input tokens consumed:

$$
T_{\text{in}} = L_{\text{tok}} + D \times 2{,}000 + (D + F) \times f_{\text{oh}}.
$$

With $L_{\text{tok}} = 10{,}400$, $D = 5$, $F = 25$, $f_{\text{oh}} = 500$:

$$
T_{\text{in}} = 10{,}400 + 10{,}000 + 30 \times 500 = 10{,}400 + 10{,}000 + 15{,}000 = 35{,}400 \text{ tokens}.
$$

Each extraction call also carries the relevant document context; assume the agent re-reads an average of $1{,}000$ tokens of context per extraction call, adding $F \times 1{,}000 = 25{,}000$ tokens:

$$
T_{\text{total}} = 35{,}400 + 25{,}000 = 60{,}400 \text{ tokens per paper}.
$$

Number of agent calls:

$$
N_{\text{calls}} = D + F = 5 + 25 = 30 \text{ calls per paper}.
$$

**Bracketing.** For the field-count bracket $F \in \{10, 40\}$, holding other inputs fixed:

- Lower: $T_{\text{total}} = 10{,}400 + 10{,}000 + (5 + 10) \times 500 + 10 \times 1{,}000 = 10{,}400 + 10{,}000 + 7{,}500 + 10{,}000 = 37{,}900$ tokens; $N_{\text{calls}} = 15$.
- Upper: $T_{\text{total}} = 10{,}400 + 10{,}000 + (5 + 40) \times 500 + 40 \times 1{,}000 = 10{,}400 + 10{,}000 + 22{,}500 + 40{,}000 = 82{,}900$ tokens; $N_{\text{calls}} = 45$.

If the corpus-scan stage $\text{S}_1$ must additionally screen $S = 10$ candidate papers per accepted paper, each screened at $L_{\text{tok}} = 10{,}400$ tokens with a single call of overhead $500$, the screening cost is $10 \times (10{,}400 + 500) = 109{,}000$ tokens, and the full retrieval stage (screening plus extraction) for one accepted paper is

$$
T_{\text{retr}} = 109{,}000 + 60{,}400 = 169{,}400 \text{ tokens},
$$

with the bracket $T_{\text{retr}} \in [146{,}900,\ 191{,}900]$ tokens. These are projections under the stated assumptions, not measurements.

### 4.2 Information bound on the reanalysis specification

**Inputs.** The extracted protocol must fix, per [1], the pipeline steps, parameters, software versions, input files, and output definitions. Assume $F = 25$ fields. Assume a conservative field cardinality: each field takes one of $n_j$ admissible values with the geometric mean cardinality $\bar{n} = 10$ (e.g., a normalization method chosen among roughly ten standard options; a threshold parameter with ten plausible settings). Then:

$$
H_0 = F \log_{2} \bar{n} = 25 \times \log_{2} 10 = 25 \times 3.3219 = 83.05 \text{ bits}.
$$

For the bracket $F \in \{10, 40\}$:

- Lower: $H_0 = 10 \times 3.3219 = 33.22$ bits.
- Upper: $H_0 = 40 \times 3.3219 = 132.88$ bits.

**Shannon comparison.** If field values are drawn non-uniformly — say the most common value for each field has probability $p = 0.5$ and the remaining $0.5$ is spread over the other nine values — the Shannon entropy per field is bounded by the standard two-level decomposition: with probability $0.5$ the field is resolved for free, and with probability $0.5$ it carries at most $\log_{2} 10 = 3.3219$ bits, so

$$
H \leq 0.5 \times 0 + 0.5 \times 3.3219 = 1.661 \text{ bits per field},
$$

and over $F = 25$ fields, $H \leq 25 \times 1.661 = 41.5$ bits. The gap between $H_0 = 83.05$ bits and $H \leq 41.5$ bits is the dual-face result in the sense of [11]: the specification space the agent must be able to express is twice, in this parameterization, what a typical paper actually resolves, which is why defaults and conventions absorb part of the curation burden.

**The binding constraint.** The bound that matters for feasibility is not the agent's capacity to express $H_0 \approx 83$ bits — trivially small by machine standards — but whether the published record contains the evidence to resolve those bits. [1] states that the needed information is dispersed across main text, supplementary files, and code repositories, and that intermediate data locations are irregular; the information-theoretic framing says the agent's task is to reduce $H$ to $0$ per field using only those dispersed sources. Where a field's value is stated nowhere, its conditional entropy stays at its prior, and the reanalysis is underdetermined. This is the formal statement of the accessibility gap [1] describes qualitatively.

### 4.3 Reusability index

Define the reusability index $R$ as the fraction of the fields an agent can resolve from the published record without human intervention:

$$
R = \frac{F_{\text{resolved}}}{F},
$$

where $F_{\text{resolved}}$ is the number of fields whose value is stated or derivable in the dispersed record. Using the Shannon model of Section 4.2, if each field is stated with probability $p = 0.5$ (the same assumption), then $F_{\text{resolved}} = pF$ and

$$
R = p = 0.5.
$$

Sensitivity: $R$ is linear in $p$. If publication practice improves so that $p = 0.9$, then $R = 0.9$ and the human curation burden per paper falls from $F(1 - 0.5) = 12.5$ fields to $F(1 - 0.9) = 2.5$ fields — a fivefold reduction, computed as $12.5 / 2.5 = 5$. This is the quantitative form of the claim that the binding constraint is publication practice: the agent absorbs exactly the resolved fraction, and the residual $(1 - R)F$ fields are the irreducible human cost under current practice. These are model projections, not measurements of any corpus.

### 4.4 Resilience to corrupted sources

Map each consulted source to a worker in the sense of [4]: $m$ sources inform a field, of which $t$ may be wrong (mislabeled repository records, outdated supplementary files, contradictory code comments). A majority vote over $m$ independent sources tolerates up to $\lfloor (m-1)/2 \rfloor$ corrupt sources. For $m = 3$:

$$
t_{\max} = \left\lfloor \frac{3-1}{2} \right\rfloor = 1,
$$

so three independent sources per field tolerate one corrupt source. For $m = 5$: $t_{\max} = 2$. The cost of this tolerance is additional retrieval: consulting $m$ sources per field multiplies the context-reading term of Section 4.1 by $m$. With $m = 3$ and $F = 25$:

$$
T_{\text{ctx}} = 3 \times 25 \times 1{,}000 = 75{,}000 \text{ tokens},
$$

versus $25{,}000$ at $m = 1$ — a threefold increase in the context term, raising the no-screening total from $60{,}400$ to $60{,}400 - 25{,}000 + 75{,}000 = 110{,}400$ tokens per paper. The structural point, following [4] and [5], is that resilience is purchasable in tokens: the master-agent must either consult redundant sources or accept single-point-of-failure metadata. Neither [4] nor [5] states a domain-specific threshold in its supplied summary, so this derivation is self-contained arithmetic on the majority-vote structure, not an imported guarantee.

## 5. Results

All numbers in this section are those computed in Section 4 under its stated assumptions; they are projections of the cost model, not empirical measurements.

**R1 (retrieval cost).** Under the assumptions $L = 8{,}000$ words, $D = 5$ documents, $F = 25$ fields, $f_{\text{oh}} = 500$ tokens, and $1{,}000$ tokens of context per extraction call, the retrieval stage costs $60{,}400$ tokens and $30$ agent calls per accepted paper without corpus screening, and $169{,}400$ tokens with a $10{:}1$ screening ratio (Section 4.1). The field-count bracket $F \in [10, 40]$ gives $T_{\text{total}} \in [37{,}900,\ 82{,}900]$ tokens without screening.

**R2 (specification entropy).** The reanalysis specification carries Hartley entropy $H_0 = 83.05$ bits at $F = 25$ fields with geometric-mean cardinality $\bar{n} = 10$, bracketed as $H_0 \in [33.22,\ 132.88]$ bits for $F \in [10, 40]$ (Section 4.2). Under a non-uniform value distribution with top probability $0.5$, the Shannon entropy is at most $41.5$ bits — half the Hartley bound in this parameterization.

**R3 (reusability index).** With each field stated in the published record with probability $p$, the reusability index is $R = p$; at $p = 0.5$ the agent absorbs half the curation burden and the residual human cost is $12.5$ fields per paper, falling to $2.5$ fields (a fivefold reduction) if $p$ rises to $0.9$ (Section 4.3).

**R4 (resilience cost).** Majority-vote verification over $m = 3$ sources per field tolerates one corrupt source and raises the per-paper token cost from $60{,}400$ to $110{,}400$ — an $82.8\%$ increase, computed as $(110{,}400 - 60{,}400)/60{,}400 = 0.828$ (Section 4.4).

**R5 (calls).** The call count scales linearly in both $D$ and $F$: $N_{\text{calls}} = D + F$, giving $15$ to $45$ calls per paper over the field bracket, before any retry on failed verification at stage $\text{S}_4$.

## 6. Discussion

The central claim of this paper is that the omics discovery pipeline of [1] has a bounded, linear cost structure — linear in documents consulted, fields extracted, and sources per field — and that its feasibility is governed not by agent capability but by the fraction $p$ of metadata fields the published record actually resolves. The derivations support the linearity and the bound; they do not measure $p$, and that is the principal limitation.

**Limitations list.** Every result rests on the following assumptions, with sensitivity stated:

- Paper length $L = 8{,}000$ words ($10{,}400$ tokens): $T_{\text{total}}$ scales linearly in $L$; doubling $L$ doubles the main-text term ($10{,}400 \to 20{,}800$), raising the no-screening total from $60{,}400$ to $70{,}800$ tokens, a $17.2\%$ increase.
- Documents per paper $D = 5$: linear; $D = 10$ adds $5{,}000$ context tokens and $5$ calls.
- Fields $F = 25$ with bracket $[10, 40]$: linear in $F$ for both tokens and calls; the entropy bound is linear in $F$ at fixed $\bar{n}$.
- Field cardinality $\bar{n} = 10$: $H_0$ scales as $\log_{2} \bar{n}$; $\bar{n} = 100$ gives $25 \times 6.6439 = 166.1$ bits, doubling the bound.
- Statement probability $p = 0.5$: $R$ is exactly $p$; the residual human cost $(1-p)F$ is the quantity most sensitive to publication practice, and no measurement of $p$ on any corpus is offered here.
- Screening ratio $10{:}1$: dominates the with-screening total ($109{,}000$ of $169{,}400$ tokens); a $3{:}1$ ratio gives $3 \times 10{,}900 = 32{,}700$ screening tokens and $T_{\text{retr}} = 93{,}100$.
- Uniform independence of sources in the resilience model: real repository records are correlated (a supplementary file often repeats the main text), so effective $m$ is lower than nominal $m$, and the tolerance $t_{\max} = 1$ at $m = 3$ is an upper bound on real tolerance.
- Token cost per call is left as a free parameter; [9] establishes that frontier-model price-performance varies across models (reporting DeepSeek V4 Pro 0813 as the mathematics price-performance optimum on the LiveBench 2026-06-25 benchmark), so the dollar cost of $T_{\text{retr}}$ is model-dependent and deliberately not converted here.

**Failure modes.** Three dominate. First, underdetermined fields: where the record states nothing, the agent cannot reduce the field's entropy, and stage $\text{S}_4$ inherits an arbitrary default — the failure [1] attributes to dispersed and irregular information. Second, correlated corruption: if all $m$ consulted sources for a field derive from one upstream error (a wrong repository annotation copied into supplementary files), majority voting fails despite nominal redundancy; this is the correlated-failure case the Byzantine literature's independence assumptions do not cover, and neither [4] nor [5] addresses correlation in its supplied summary. Third, verifier failure at $\text{S}_4$: as [6] observes for multi-system backends, the verifier is whether the deployed stack actually runs; a reconstructed pipeline that runs but silently diverges from the authors' intent passes the verifier while producing a wrong reanalysis.

**Falsification.** The calculation that would falsify the central claim is a direct measurement of $p$: if a corpus study of published omics papers finds that the fraction of reanalysis-critical fields resolvable from the dispersed record is far below $0.5$ — say $p < 0.1$ — then the agent absorbs too little burden for the pipeline to change practice, and the residual human cost $(1 - p)F \approx 22.5$ fields per paper at $F = 25$ remains prohibitive. Conversely, a measured $p > 0.9$ would falsify the implicit premise that publication practice is the binding constraint, shifting attention to agent reliability. The cost-model claims (R1, R4, R5) are falsified if measured token counts on real papers depart from the linear model by more than the bracket widths stated above — for example, if extraction requires re-reading full documents rather than $1{,}000$-token contexts, the context term rises from $25{,}000$ toward $F \times L_{\text{tok}} = 260{,}000$ tokens, an order-of-magnitude departure.

**Open questions.** What is the measured distribution of $p$ across repositories and omics modalities? How correlated are metadata errors within a single study's record? Can the synthesis stage $\text{S}_5$ detect systematic extraction errors across studies, in the way cross-study consistency checks constrain reanalysis in other domains — as the dark-energy reanalysis of [7] illustrates, where constraints from reused data were consistent with other datasets but weaker than the tightest available, a pattern that reused omics reanalyses may replicate? And, at the level of [12], does the computability-level equivalence between agent-executed and human-executed reanalysis hold at the resource level, or does the token cost derived here grow intractably for the full space of published pipelines? The supplied summary of [12] states the resource-level distinction but no result resolving it, so this remains open. Finally, ontology-learning alternatives in the sense of [10] — pattern-based self-ordering rather than field extraction — are unmodeled here and may shift which fields need explicit resolution.

## 7. Practical Implications and Engineering Pathways

**(a) Users and changed decisions.** The users of this analysis are, first, the developers of omics discovery agents such as the framework of [1], who gain a per-paper budget ($\sim 6 \times 10^{4}$ tokens, $\sim 30$ calls, before screening) against which to size context windows, batch pipelines, and model choice; second, repository operators and journal editors, who gain a target field list — the $F$ fields whose resolution determines $R$ — and a reason to mandate that intermediate data locations be stated regularly, since raising $p$ from $0.5$ to $0.9$ cuts residual human curation fivefold (Section 4.3); third, research groups performing systematic reanalysis, who can decide per study whether the agent-resolved fraction suffices or human curation is required. No deployment market is claimed; the work is analytical.

**(b) Readiness.** This paper is purely analytical and has not been peer reviewed: by the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept formulated). The pipeline it analyzes, as presented in [1], is described in the literature but no performance figures are supplied in the entry used here; nothing in this paper constitutes demonstrated end-to-end operation, and no readiness above TRL 3 — analytical and experimental proof of concept — is claimed or claimable for analytical work of this kind.

**(c) Smallest next test.** The smallest de-risking experiment is a manual annotation study: take $n = 20$ published omics papers, have a human curator list the reanalysis-critical fields and whether each is