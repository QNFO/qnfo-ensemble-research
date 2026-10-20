# Quantifying the Reuse Barrier in Published Omics Data: Dispersal, Cost, and Feasibility Models for Agent-Supported Retrieval, Reanalysis, and Synthesis

## Abstract

Most published omics data remain functionally inaccessible for computational reuse because critical information is scattered across article main text, supplementary files, and code repositories, and intermediate data such as protein abundance tables are shared irregularly. Existing descriptions of this problem are qualitative; no published model quantifies the dispersal cost to a reuser or the effect of an agent. We formalize a study as a set of reproduction‑critical artifacts dispersed over document locations, derive closed‑form expressions for reproduction success probability and expected retrieval cost, and construct a token‑and‑call cost model for the retrieval stage of an agent pipeline. We also derive an information‑theoretic bound on the metadata an agent must extract. Under stated assumptions (five dispersed artifacts, per‑location retrieval success 0.8), a manual reproduction succeeds with probability 0.32768 and requires 6.25 expected retrieval visits, while an agent with two retries succeeds with probability ≈ 0.9606 at 6.20 visits; the retrieval stage costs 60 400 tokens and 30 calls per paper before screening. The model turns “most data are inaccessible” into three measurable quantities—dispersal breadth k, per‑location reliability p, and missing‑artifact fraction—giving repository operators and agent developers concrete targets for measurement and deposition policy.

## 1. Introduction

A computational biologist who wants to reanalyse a published proteomics or genomics study faces a concrete, recurring obstacle. The raw data may sit in a public repository, but the parameters that produced the reported results, the filtering thresholds, the pipeline version, and the mapping from supplementary figures to underlying tables are scattered across the article main text, supplementary files, and, where they exist at all, code repositories; intermediate artifacts such as protein abundance tables are shared only in a minority of cases and at irregular locations [1]. The practical consequence is that a reanalysis that should take hours instead takes days or fails outright, and the aggregate effect is that most published omics data are functionally inaccessible for computational reuse even when they are technically downloadable [1]. This blocks specific decisions: whether to build on a published dataset rather than generate new data, whether a reported result survives an alternative processing choice, and whether a meta‑analysis across studies can be assembled at all. Today the cost of reconstruction is paid in human hours, one paper at a time.

If the dispersal barrier could be quantified per study, three things change. A journal or repository could report a single reuse‑readiness figure alongside a deposit. A reanalysis agent could allocate its retrieval budget to the locations that dominate the failure probability. And an author preparing a supplement could see which missing artifact contributes most to the expected cost imposed on every future reuser. Conversely, if the information an agent must extract to specify a reanalysis exceeds what the published record reliably contains, then no amount of agent capability closes the gap, and the binding constraint is publication practice itself. Both outcomes are actionable, and this paper derives conditions for each.

This work treats the pipeline proposed in [1] as the object of analysis. It does not propose a new agent architecture; it derives the cost structure, the information requirements, and the failure modes of any agent that performs the three functions—retrieval, reanalysis, synthesis—named in [1]. The analysis draws on the multi‑agent systems literature for the coordination structure [2], [8], on the distributed‑systems literature for the reliability question that arises when a pipeline is assembled from independently fallible retrieval steps [4], [5], and on the information‑theoretic analysis of biological specification [11] for the bound on what metadata can capture.

**Contributions**

- A staged formalisation of the omics discovery pipeline as a five‑stage multi‑agent workflow, with the coordination structure of each stage stated explicitly (Section 3).  
- A dispersal model of a published study with closed‑form expressions for reproduction success probability and expected retrieval cost, evaluated numerically under stated assumptions: manual success 0.32768 versus agent success ≈ 0.9606 at k = 5, p = 0.8, r = 2 (Sections 3 and 4.4–4.5).  
- A derived token‑and‑call cost model for the retrieval stage, giving 60 400 tokens and 30 calls per paper before screening, and 169 400 tokens with a 10:1 screening ratio (Section 4.1).  
- A derived information‑theoretic bound on the reanalysis specification, giving Hartley entropy ≈ 83.05 bits at F = 25 and a Shannon‑entropy comparison (Section 4.2).  
- A sensitivity decomposition showing that dispersal breadth k dominates the barrier and that agent retries substitute for per‑location reliability (Sections 4.4–4.5).  
- A statement of which observations would falsify the central claims, a limitations list naming every assumption, and a practical pathway from the analytical result to a first measurement (Sections 6 and 7).

## 2. Background and Related Work

The direct object of this paper is the omics data discovery agents framework, which presents an agentic approach to the retrieval, reanalysis, and synthesis of published omics data and documents the core observation motivating everything here: most published data remain functionally inaccessible for computational reuse because reproduction‑critical information is dispersed across main text, supplementary files, and code repositories, with intermediate data such as protein abundance files shared irregularly when at all [1]. That work establishes the problem and the agent architecture; its supplied summary provides no quantitative cost model of the dispersal barrier, which is the gap this paper addresses.

A second thread concerns how multiple cooperating agents coordinate. The survey of multi‑agent deep reinforcement learning with communication establishes that communication is an effective mechanism for coordinating the behaviours of multiple agents, broadening their views of the environment, and supporting their collaborations [2]. In the omics retrieval setting, the analogue is a division of labour in which one agent reads the article text while another queries repositories and a third executes code; the survey’s framing supports treating such message‑passing as the coordination primitive.

Retrieval over heterogeneous, multimodal document collections is treated in LLandMark, a modular multi‑agent framework for landmark‑aware multimodal interactive video retrieval, in which specialised agents collaborate across four stages to handle real‑world complex queries in a domain where the diversity and scale of data demand multimodal understanding, adaptive reasoning, and domain‑specific knowledge integration [8]. The structural lesson for omics retrieval is that a modular, staged agent design can handle diverse and large‑scale document collections; the video domain differs in modality, but the problem shape is the same as the omics literature problem, and the four‑stage decomposition serves as a comparative template for the five‑stage formalisation in Section 3.

Agentic discovery over data systems is examined in the declarative data services work, which observes that translating LLM‑driven agentic discovery to multi‑system data backends surfaces a harder problem: the search space is heterogeneous, the verifier is whether a deployed stack actually runs, and composition knowledge is unevenly captured in pretraining [6]. This maps directly onto omics reanalysis, where the verifier is whether a retrieved pipeline actually reproduces the published result and where pipeline‑composition knowledge is exactly the kind of knowledge unevenly captured in pretraining.

Reliability of distributed computation under partial failure is the subject of two works on Byzantine resilience. Data encoding for Byzantine‑resilient distributed optimisation studies distributed optimisation where data and computation are distributed among m worker machines, t of which may be corrupt, with compromised nodes able to collaboratively and arbitrarily deviate from their pre‑specified programmes while a designated master node iteratively computes the model or parameter vector [4]. Byzantine‑resilient SGD in high dimensions on heterogeneous data considers the master‑worker architecture under Byzantine attacks with heterogeneous local datasets and no probabilistic assumptions on data generation, using a polynomial‑time outlier‑filtering procedure for robust mean estimation at its core [5]. In the omics setting the failures are not adversarial, but the structural question is identical: when a reproduction pipeline is assembled from k independently fallible retrieval steps, end‑to‑end reliability is a function of per‑step reliability, and this literature supplies the vocabulary of tolerating t failures among m components.

Local reanalysis methods appear in structural engineering: the meshless‑based local reanalysis (MLR) method extends reanalysis methods to the Kriging interpolation meshless method, using combined approximations and indirect factorisation updating to reduce the computational cost of meshless methods [3]. There, “reanalysis” means recomputing a modified structural model cheaply from a previously solved one; the transferable idea is that reanalysis is worthwhile exactly when full recomputation is expensive, which is the economic premise of omics reanalysis as well.

Reuse of existing measured data for parameter constraint is illustrated by the dark‑energy study that uses H II starburst galaxy apparent magnitude versus redshift data to constrain cosmological model parameters, finding constraints generally consistent with those from other datasets but not as restrictive as the tightest currently available [7]. This is a concrete instance of the payoff side of the ledger: published data, when retrievable, support new scientific constraints, and the quality of what can be extracted depends on what the data can support — an analogy for the information loss incurred when reanalysis works from published rather than raw records.

Finally, four QNFO entries bound what an agent can and cannot extract. The information‑theoretic limits work shows that an organism does not contain enough organism‑specific information to specify its own microscopic organisation, treating the genome as a generator specification rather than a trajectory programme, and establishes a coarse‑graining threshold with dual Hartley and Shannon entropy faces [11]. For data discovery this implies that even a perfect retrieval agent cannot recover information that was never encoded in the published artifacts; Section 4 adopts the dual Hartley/Shannon framing for the metadata specification problem. The LiveBench‑grounded audit of frontier large language models for scientific research and agentic AI reports that no Llama model ranks in the top 42 and that DeepSeek V4 Pro 0813 is the mathematics price‑performance optimum [9]; its observation that model choice for the retrieval agent is an auditable, benchmark‑grounded decision and that per‑token cost is a model‑dependent free parameter informs the cost analysis. The pattern‑based ontology entry (PBO/Autaxys) concerns intrinsic self‑ordering of patterns [10], and the categorical formalisation entry states a Capability(S) ≈ End(X_S) conjecture with a Church‑Turing‑scoped resource‑level thesis distinguishing computability‑level equivalence from resource‑level difference [12]; both are cited as adjacent formal work.

## 3. Methods

### 3.1 Pipeline formalisation

Following [1], the pipeline has three functions — retrieval, reanalysis, and synthesis. We formalise these as five sequential stages, each implemented by a specialist agent in the modular, communicating pattern of [2] and [8]:

$$
S_1 \rightarrow S_2 \rightarrow S_3 \rightarrow S_4 \rightarrow S_5
$$

with stages:

- $S_1$ (corpus scan): identify candidate papers and determine whether omics data exist for each.  
- $S_2$ (asset location): locate raw data deposits in public repositories and any intermediate data files.  
- $S_3$ (protocol extraction): reconstruct the analysis pipeline from main text, supplementary files, and code repositories.  
- $S_4$ (reanalysis execution): run the reconstructed pipeline on the located data, with a verifier that the pipeline either runs and reproduces a reported result or it does not.  
- $S_5$ (synthesis): aggregate reanalysed outputs across studies into a common, searchable form.

Each stage $S_i$ has an input context $C_i$, an output record $O_i$, and a message channel to downstream stages, in the sense of [2] that communication broadens each agent’s view of the shared environment. The output record $O_3$ — the extracted protocol — is the pivotal artifact: it is the metadata specification on which $S_4$ depends, and Section 4.2 bounds its information content.

### 3.2 Dispersal model of a published omics study

We model a published omics study as a set $A = \{a_1, \dots, a_k\}$ of $k$ reproduction‑critical artifacts. An artifact is any item a reuser must obtain to reproduce or extend a reported result: the raw data deposit, the processing parameters, the pipeline code, an intermediate table such as a protein abundance matrix, or a mapping from figure to underlying data. Each artifact $a_i$ resides in exactly one location $\ell_i$ drawn from the set of document locations $L = \{\text{article main text}, \text{supplementary files}, \text{code repository}, \text{external repository landing page}, \text{author contact}\}$. The dispersal breadth of the study is $k$; the location spread is the number of distinct elements among $\{\ell_1, \dots, \ell_k\}$.

### 3.3 Retrieval reliability

Let $p\in[0,1]$ be the per‑attempt success probability of retrieving and correctly interpreting a single artifact from its location. For a human reuser, $p$ aggregates finding the location, gaining access, and interpreting the artifact. For an agent, we separate a first‑attempt success probability $p$ from $r$ independent retries at the same location, each succeeding with probability $p$ conditional on prior failures being independent. The per‑location success probability with $r$ retries is

$$
P_{\text{loc}}(p, r) = 1 - (1-p)^{r+1}.
$$

### 3.4 End‑to‑end reproduction success and cost

Assuming artifact retrievals are independent, the end‑to‑end reproduction success probability is

$$
P_{\text{rep}} = \prod_{i=1}^{k} P_{\text{loc},i},
$$

which under the homogeneous assumption $P_{\text{loc},i}=P_{\text{loc}}$ becomes

$$
P_{\text{rep}}(k, p, r) = \left[1 - (1-p)^{r+1}\right]^{k}.
$$

The expected number of retrieval visits per artifact is the mean of a geometric random variable truncated at $r+1$ attempts:

$$
E[N] = \sum_{j=1}^{r+1} j\,(1-p)^{j-1}p + (r+1)(1-p)^{r+1},
$$

which for the no‑retry case $r=0$ reduces to $E[N]=1/p$. The expected total retrieval visits for the study is $k\cdot E[N]$.

### 3.5 Cost‑model and information‑model inputs

The token cost model of Section 4.1 takes as free parameters: paper length in tokens $L$, the number of documents consulted per paper $D$, the number of decision fields to extract $F$, and tokens per extraction call overhead $f_{\text{oh}}$. All values used are stated assumptions of this analysis, not measurements; they are chosen to bracket the range a typical omics paper plausibly occupies, and Section 6 treats their sensitivity explicitly.

Section 4.2 applies the dual Hartley/Shannon framing of [11]. For a protocol specification with $F$ independent fields, each with $n_j$ admissible values, the Hartley entropy is

$$
H_0 = \log_2 \prod_{j=1}^{F} n_j = \sum_{j=1}^{F} \log_2 n_j,
$$

and the Shannon entropy $H = -\sum_j p_j \log_2 p_j \le H_0$ measures the uncertainty actually reduced by extracted evidence. $H_0$ bounds what a complete specification must be able to express; $H$ bounds what an agent must resolve per paper.

### 3.6 What the model does not claim

The dispersal model treats artifacts as binary (retrieved or not) and retrievals as independent. It does not model semantic difficulty, cross‑artifact consistency checking, or the compute cost of executing a retrieved pipeline; those enter only as qualitative considerations. All numerical results below follow from the closed forms above with stated inputs.

## 4. Analysis

### 4.1 Token‑and‑call cost of the retrieval stage

**Inputs (stated assumptions).** Paper main text: $L = 8000$ words at $1.3$ tokens per word, giving $L_{\text{tok}} = 8000 \times 1.3 = 10400$ tokens. Supplementary and code documents consulted: $D = 5$ documents, average $2000$ tokens each, giving $5 \times 2000 = 10000$ tokens. Decision fields to extract: $F = 25$. Tokens per call overhead: $f_{\text{oh}} = 500$. One extraction call per field plus one summarisation call per document gives $D + F$ calls.

**Arithmetic.** Total structured input tokens:

$$
T_{\text{in}} = L_{\text{tok}} + D \times 2000 + (D + F) \times f_{\text{oh}}.
$$

With $L_{\text{tok}} = 10400$, $D = 5$, $F = 25$, $f_{\text{oh}} = 500$:

$$
T_{\text{in}} = 10400 + 10000 + 30 \times 500 = 10400 + 10000 + 15000 = 35400 \text{ tokens}.
$$

Each extraction call also carries document context; assume the agent re‑reads an average of $1000$ tokens per extraction call, adding $F \times 1000 = 25000$ tokens:

$$
T_{\text{total}} = 35400 + 25000 = 60400 \text{ tokens per paper}.
$$

Number of agent calls:

$$
N_{\text{calls}} = D + F = 5 + 25 = 30 \text{ calls per paper}.
$$

**Bracketing.** For $F \in \{10, 40\}$, holding other inputs fixed:

- Lower: $T_{\text{total}} = 10400 + 10000 + (5+10) \times 500 + 10 \times 1000 = 10400 + 10000 + 7500 + 10000 = 37900$ tokens; $N_{\text{calls}} = 15$.
- Upper: $T_{\text{total}} = 10400 + 10000 + (5+40) \times 500 + 40 \times 1000 = 10400 + 10000 + 22500 + 40000 = 82900$ tokens; $N_{\text{calls}} = 45$.

If the corpus‑scan stage $S_1$ must screen $S = 10$ candidate papers per accepted paper, each at $L_{\text{tok}} = 10400$ tokens with one call of overhead $500$, the screening cost is $10 \times (10400 + 500) = 109000$ tokens, and the full retrieval stage for one accepted paper is

$$
T_{\text{retr}} = 109000 + 60400 = 169400 \text{ tokens},
$$

with bracket $T_{\text{retr}} \in [146900, 191900]$ tokens. These are projections under the stated assumptions, not measurements.

### 4.2 Information bound on the reanalysis specification

**Inputs.** Assume $F = 25$ fields with geometric‑mean cardinality $\bar{n}=10$ admissible values per field. Then

$$
H_0 = F \log_2 \bar{n} = 25 \times \log_2 10 = 25 \times 3.3219 = 83.05 \text{ bits}.
$$

For the bracket $F \in \{10, 40\}$:

- Lower: $H_0 = 10 \times 3.3219 = 33.22$ bits.  
- Upper: $H_0 = 40 \times 3.3219 = 132.88$ bits.

**Shannon comparison.** If the most common value of each field has probability $p=0.5$ and the remaining $0.5$ is spread over the other nine values, then per field the resolved entropy is at most

$$
H \le 0.5 \times 0 + 0.5 \times \log_2 10 = 1.661 \text{ bits},
$$

and over $F=25$ fields $H \le 25 \times 1.661 = 41.5$ bits. The gap between $H_0 = 83.05$ bits and $H \le 41.5$ bits is the dual‑face result of [11]: the specification space the agent must be able to express is roughly twice what a typical paper actually resolves, which is why defaults and conventions absorb part of the curation burden.

### 4.3 Reusability index

Define the reusability index $R$ as the fraction of fields an agent can resolve from the published record without human intervention:

$$
R = \frac{F_{\text{resolved}}}{F}.
$$

If each field is stated with probability $p=0.5$, then $F_{\text{resolved}} = pF$ and $R = p = 0.5$. Sensitivity: $R$ is linear in $p$. If publication practice improves so that $p=0.9$, the human curation burden per paper falls from $F(1-0.5)=12.5$ fields to $F(1-0.9)=2.5$ fields — a fivefold reduction, computed as $12.5/2.5 = 5$.

### 4.4 Manual reproduction (no retries, $r=0$)

With $r=0$, per‑location success is $P_{\text{loc}} = p = 0.8$. End‑to‑end, with $k=5$:

$$
P_{\text{rep}}(5,0.8,0) = 0.8^5.
$$

Step‑by‑step: $0.8^2 = 0.64$; $0.8^3 = 0.512$; $0.8^4 = 0.4096$; $0.8^5 = 0.32768$.

$$
P_{\text{rep}}(5,0.8,0) = 0.32768.
$$

Expected retrieval visits per artifact with $r=0$ is $E[N]=1/p=1/0.8=1.25$, and total expected visits:

$$
k \cdot E[N] = 5 \times 1.25 = 6.25.
$$

### 4.5 Agent reproduction with $r=2$ retries

Per‑location success with two retries:

$$
P_{\text{loc}}(0.8,2) = 1 - (1-0.8)^3 = 1 - 0.2^3 = 0.992.
$$

End‑to‑end:

$$
P_{\text{rep}}(5,0.8,2) = 0.992^5.
$$

Computing: $0.992^2 = 0.984064$; $0.992^3 = 0.976191488$; $0.992^4 = 0.968381956096$; $0.992^5 = 0.960634900447232$.

$$
P_{\text{rep}}(5,0.8,2) \approx 0.9606.
$$

The factor increase is

$$
\frac{0.960634900447232}{0.32768} \approx 2.9316.
$$

Expected visits per artifact with $r=2$:

$$
E[N] = \sum_{j=1}^{3} j\,(0.2)^{j-1}(0.8) + 3\,(0.2)^3.
$$

Term‑by‑term: $j=1$: $0.8$; $j=2$: $0.32$; $j=3$: $0.096$; truncation term: $0.024$. Sum:

$$
E[N] = 0.8 + 0.32 + 0.096 + 0.024 = 1.24.
$$

Total expected visits: $5 \times 1.24 = 6.20$.

### 4.6 Sensitivity to dispersal breadth $k$

Holding $p=0.8$, $r=0$:

$$
P_{\text{rep}}(k) = 0.8^{k}.
$$

Values: $k=2$: 0.64; $k=3$: 0.512; $k=4$: 0.4096; $k=5$: 0.32768; $k=8$: 0.16777216; $k=10$: 0.1073741824. Each additional dispersed artifact multiplies success by 0.8. With the agent ($r=2$), the same range gives $0.992^{k}$; at $k=10$, $0.992^{10} \approx 0.9228$. The agent’s advantage grows with $k$: at $k=10$ manual success ≈ 0.1074 versus agent ≈ 0.9228, a factor ≈ 8.59.

### 4.7 Sensitivity to per‑location reliability $p$

Holding $k=5$, $r=0$:

- $p=0.6$: $0.6^{5}=0.07776$  
- $p=0.8$: $0.32768$  
- $p=0.95$: $0.95^{5}=0.7737809375$

Retrieval retries substitute for per‑location skill: $P_{\text{loc}}(0.6,2)=1-0.4^{3}=0.936$, so a weaker retriever with retries ($0.936$ per location) outperforms a stronger one without ($0.8$ per location).

### 4.8 Resilience to corrupted sources

Map each consulted source to a worker in the sense of [4]: $m$ sources inform a field, of which $t$ may be wrong. A majority vote over $m$ independent sources tolerates up to $\lfloor (m-1)/2 \rfloor$ corrupt sources. For $m=3$, $t_{\max}=1$. Consulting $m$ sources per field multiplies the context‑reading term of Section 4.1 by $m$. With $m=3$ and $F=25$:

$$
T_{\text{ctx}} = 3 \times 25 \times 1000 = 75000 \text{ tokens},
$$

versus $25000$ at $m=1$, raising the no‑screening total from $60400$ to $110400$ tokens per paper. The structural point, following [4] and [5], is that resilience is purchasable in tokens: the master‑agent must either consult redundant sources or accept single‑point‑of‑failure metadata.

## 5. Results

The results below are the numerical consequences of the closed forms in Section 3 and the arithmetic in Section 4, under the stated assumptions ($k=5$, $p=0.8$, $r=2$, $F=25$, $D=5$). They are model outputs, not measurements of any corpus.

- **R1.** Manual reproduction success is low and falls multiplicatively with dispersal. With no retries, $P_{\text{rep}}(5,0.8,0)=0.32768$ (Section 4.4): roughly one manual attempt in three succeeds. Each additional dispersed artifact multiplies success by 0.8; at $k=10$, manual success is $0.1073741824$ (Section 4.6).

- **R2.** Agent retries raise success to ≈ 0.9606 at essentially unchanged retrieval effort. With $r=2$, per‑location success is 0.992 and end‑to‑end success is ≈ 0.9606 (Section 4.5), a factor of ≈ 2.9316 over the manual case. Expected visits are $6.20$ versus $6.25$ manual.

- **R3.** The retrieval stage costs $60 400$ tokens and $30$ calls per paper before screening. With a 10:1 screening ratio, the full retrieval stage is $169 400$ tokens per accepted paper, bracketed at $[146 900,191 900]$ tokens for $F\in\{10,40\}$ (Section 4.1). These are projections under the stated assumptions.

- **R4.** The specification space is about twice what a typical paper resolves. Hartley entropy of the protocol specification is $H_0=83.05$ bits at $F=25$, $\bar{n}=10$; the Shannon comparison gives $H\le41.5$ bits (Section 4.2). The unresolved remainder, $R=0.5$ of fields under the stated prior, is the irreducible human curation burden under current practice (Section 4.3).

- **R5.** Dispersal breadth $k$ dominates the barrier; retries substitute for per‑location reliability. Going from $k=2$ to $k=5$ cuts manual success by $48.8\%$ relative (Section 4.6). A weaker retriever with retries ($P_{\text{loc}}(0.6,2)=0.936$) outperforms a stronger one without ($0.8$) (Section 4.7). At $k=10$ the agent’s advantage grows to a factor of ≈ 8.59 ($0.9228$ vs $0.1074$).

- **R6.** Resilience to corrupted sources is purchasable in tokens. Majority voting over $m=3$ independent sources per field tolerates one corrupt source and raises the no‑screening retrieval total from $60 400$ to $110 400$ tokens (Section 4.8).

## 6. Discussion

The central claim of this paper is that the omics reuse barrier decomposes into three measurable quantities — dispersal breadth $k$, per‑location reliability $p$, and the resolved‑field fraction $R$ — and that under the stated parameterisation the barrier is dominated by $k$, while agent retries cheaply compensate for low $p$. The claim’s strength is exactly the strength of its assumptions, which are stated assumptions of this analysis rather than measurements.

**Limitations.** The result rests on the following assumptions, each with its sensitivity:

- **Independence of artifact retrievals.** $P_{\text{rep}} = P_{\text{loc}}^{k}$ assumes failures are uncorrelated. Correlated failures would alter the effective $k$ and shift the barrier.  
- **Homogeneous $p$ across artifacts and locations.** Real per‑location success varies; a heterogeneous model would replace $P_{\text{loc}}^{k}$ with $\prod_i P_{\text{loc