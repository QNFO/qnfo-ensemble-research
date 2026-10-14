# Gate-Check Convergence: A Benchmark Protocol for Measuring Cross-Model Agreement on Fringe Physics Claims

## Abstract

Large language models (LLMs) are increasingly consulted as informal arbiters of scientific claims, including claims at the fringe of established physics. We propose a benchmark protocol—Gate‑Check Convergence (GCC)—for testing the hypothesis that independent LLMs, when asked to render verdicts on novel fringe physics claims, converge not only on the verdict but also on the reasoning scaffold used to reach it (e.g., Bell’s theorem, the $SU(2)\!\to\!SO(3)$ covering map, BCS gap arithmetic). We formalize the hypothesis as retrieval from an overlapping “consensus lattice” in the training corpora, which predicts higher inter‑model agreement on well‑represented consensus results than on frontier questions—a falsifiable signature distinguishing genuine gate‑check retrieval from correlated hallucination. The benchmark consists of three claim classes (falsified, trivial, valid‑but‑flawed) with expert‑adjudicated ground truth and a representation‑depth score $d_c\in[0,1]$. We derive the required sample sizes, chance‑agreement baselines, and power calculations in full arithmetic, and we present a worked illustrative Cohen’s $\kappa$ computation. No empirical model runs are reported; the contribution is the protocol, the formal retrieval model, and the analysis machinery needed to execute and falsify the claim.

## 1. Introduction

When a user asks an LLM whether some exotic claim—a faster‑than‑light signaling scheme, a classical reconstruction of quantum statistics, a room‑temperature superconductivity mechanism—is credible, the model performs what we call a *gate check*: a rapid triage of the claim against the boundaries of accepted physics. Anecdotal observation suggests that different models, from different families and trained by different organizations, often reach the same verdict *and* deploy the same argument: the same invocation of Bell’s theorem, the same appeal to the covering map from $SU(2)$ to $SO(3)$, the same BCS gap estimate. This observation motivates the central question of this paper:

> Is cross‑model convergence on fringe physics claims robust across claim domains, model families, and prompt framings, and does it correlate with accuracy against expert ground truth?

Two explanations compete. **Gate‑check convergence**: models retrieve a shared consensus lattice—the same textbooks, reviews, and canonical refutations present in all large training corpora—and the shared retrieval produces both the verdict and the argument structure. **Correlated hallucination**: models share systematic failure modes (similar pre‑training objectives, similar RLHF pressures toward confident‑sounding verdicts) that produce coincident wrong answers without genuine evidential grounding. These explanations diverge in a measurable way: gate‑check convergence predicts that agreement *rises* with how well‑represented the relevant consensus material is in the literature, and that agreement on frontier or genuinely novel questions drops toward the chance baseline; correlated hallucination predicts agreement that is high but *uncorrelated* with representation depth and uncorrelated with expert ground truth.

This paper makes three contributions. First, a benchmark design: a corpus of fringe physics claims with known expert verdicts, partitioned into three classes (falsified, trivial, valid‑but‑flawed), each annotated with the canonical consensus argument. Second, an evaluation protocol: blinded, prompt‑framing‑varied evaluations across multiple model families, scored with Cohen’s $\kappa$ on verdicts, an argument‑structure alignment metric, and citation‑quality variance. Third, a formal retrieval model that yields quantitative, falsifiable predictions, together with the full statistical machinery—sample sizes, chance baselines, and power calculations—derived explicitly.

We emphasize scope: this paper reports *no* model runs. It is a protocol and analysis paper. Every number in Section 4 is either derived from stated inputs by shown arithmetic or explicitly labeled a projection under stated assumptions.

## 2. Background and Related Work

The literature available for grounding this proposal spans several adjacent areas; we discuss each entry in turn, noting that several are only loosely connected and that the supplied summaries constrain what can be claimed about them.

**[1] Conjectures on Convergence and Scalar Curvature (arXiv:2103.10093v1).** This work surveys compactness and geometric stability conjectures formulated by participants at the 2018 IAS Emerging Topics Workshop on Scalar Curvature and Convergence, focusing on sequences of compact Riemannian manifolds with non‑negative scalar curvature. We cite it as an example of a *consensus lattice node* in mathematics: a community‑formulated set of conjectures whose status is well‑represented in the literature and therefore, under our hypothesis, should elicit highly convergent LLM verdicts. The summary supplied gives no further detail on outcomes, and we claim none.

**[2] Leveraging LLMs for Unstructured Claims Data Analysis (arXiv:2606.06089v1).** This paper presents a proof‑of‑concept framework using large language models to process unstructured text—medical records, adjuster notes, call transcripts—in an actuarial claims context, motivated by the inconsistency and unscalability of manual document processing. It is relevant as evidence that LLM‑based claims evaluation is being deployed operationally, and its framing of claims as objects requiring consistent cross‑reviewer treatment parallels our inter‑model consistency requirement. The summary does not report accuracy figures, and we do not assert any.

**[3] Physics Briefing Book (arXiv:1910.11775v2).** This document describes the European Particle Physics Strategy Update (EPPSU) process, a bottom‑up community exercise in which national inputs and inputs from National Laboratories are solicited to shape particle physics priorities. We use it to illustrate how *expert consensus is formed and recorded* in physics: a documented, citable consensus process whose outputs populate the training corpora that our retrieval model posits. The summary states the process structure but no findings, and we rely only on that structure.

**[4] Physics and Technology of the Next Linear Collider (arXiv:hep-ex/9605011v1).** This Snowmass ’96 report presents design expectations for an $e^{+}e^{-}$ linear collider at center‑of‑mass energy $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$, reviews the experiments it would carry out in exploring physics beyond the Standard Model, and argues feasibility of construction. It serves as an example of a *frontier‑adjacent* consensus document: beyond‑Standard‑Model physics is a domain where the consensus lattice is thinner and more contested, which our model predicts should lower cross‑model agreement relative to settled domains.

**[5] A category mistake in observational claims regarding ultrashort‑lived unstable particles (arXiv:1502.01303v3).** This paper argues that the $5\sigma$‑convention in particle physics, as applied to claims that ultrashort‑lived unstable particles such as a Higgs boson have been observed, produces a category mistake in which pure reasoning is passed off as observation. This is directly relevant to our benchmark: it is precisely the kind of meta‑scientific consensus argument (a critique of evidential conventions) that we expect models to retrieve as a scaffold when evaluating “was X observed?” claims. It also supplies a claim class for our benchmark: verdicts that hinge on convention rather than fact.

**[6] Fact‑Checking Meets Fauxtography (arXiv:1908.11722v1).** This work addresses automated verification of claims about images, noting that the volume of claims requiring fact‑checking exceeds manual capacity by orders of magnitude and that prior automation work had largely ignored a modality‑specific gap (the summary indicates image claims were previously neglected). Methodologically it is the closest analogue to our problem—automated claim verification against ground truth—and its framing of the scale problem motivates automated gate‑checking. The supplied summary does not report its results in detail, and we do not cite specific performance numbers.

**[7] Integrating Proportionality and Egalitarianism in Claims Problems (arXiv:2605.26948v1).** This paper studies allocation of a finite estate among agents whose claims exceed resources, integrating the Proportional rule with the Constrained Equal Awards (CEA) rule. The connection is analogical: our benchmark allocates a finite evaluation budget (model runs, expert‑verification hours) across claim classes, and claims‑problem fairness rules offer a principled allocation template. We use it only for this structural analogy; the summary supports the rule definitions quoted above and nothing further.

**[8] Do Methods Support the Claims? Intra‑Paper Verification for Peer Review (arXiv:2607.26066v1).** This work targets LLM‑assisted peer review, observing that existing automated novelty assessment compares claimed contributions against prior literature while implicitly assuming those contributions are realized in the work itself, whereas human reviewers frequently challenge novelty claims at the level of method support. This is the closest published relative of our gate‑check question: it asks whether a claim is *supported by the reasoning behind it*, which is exactly what we ask models to assess for fringe physics claims. The summary states the motivation and gap; it does not report results, and we claim none.

In summary, the adjacent literature provides: automated claims‑verification precedents [2], [6], [8]; examples of consensus formation and consensus documents in physics [1], [3], [4]; a meta‑scientific critique relevant to verdict conventions [5]; an allocation‑theoretic analogy [7]; and a pool of fringe‑adjacent candidate claims [9]–[12]. No prior work in this list measures cross‑LLM agreement on fringe physics verdicts, which is the gap this protocol addresses.

## 3. Methods

### 3.1 Benchmark construction

The benchmark consists of $N_{\mathrm{claims}}$ fringe physics claims, each annotated with:

- an **expert verdict** $v_e \in \{\text{falsified}, \text{trivial}, \text{valid‑but‑flawed}\}$, established by at least two independent domain experts with a documented adjudication rule for disagreement;
- a **consensus‑scaffold label** $s_c$: the canonical argument a physicist would deploy (e.g., Bell’s theorem, the $SU(2)\!\to\!SO(3)$ covering map, BCS gap arithmetic, the $5\sigma$ convention critique of [5]);
- a **representation‑depth score** $d_c \in [0,1]$: an operationalized estimate of how well‑represented the scaffold is in the published literature, measured by a documented proxy (e.g., count of canonical textbook treatments, normalized).

Claim classes follow the trichotomy of the research idea: *falsified* (contradicts established results), *trivial* (restates known results as if novel), *valid‑but‑flawed* (sound motivation, defective execution), with candidate items drawn from the fringe corpus exemplified by [9]–[12] and from beyond‑Standard‑Model territory of the kind surveyed in [4].

### 3.2 Evaluation protocol

Each claim is evaluated by $M$ models from at least three families, under $F \geq 3$ prompt framings (neutral, adversarial, charitable), blinded in the sense that no model output is visible to any other evaluation and order is randomized. For each run we record:

1. the **verdict** $v_{m,f,c} \in \{\text{falsified}, \text{trivial}, \text{valid‑but‑flawed}, \text{other}\}$;
2. the **argument structure**, parsed into a scaffold graph whose nodes are argument primitives and whose edges are inferential steps; alignment between two runs is the Jaccard similarity of their primitive sets:
$$
J_{(i,j)} = \frac{|S_i \cap S_j|}{|S_i \cup S_j|},
$$
where $S_i$ is the scaffold‑primitive set of run $i$;
3. the **citations** offered, scored for quality (verifiability, relevance, correctness) on a rubric scale.

### 3.3 Statistics

**Verdict agreement.** For each model pair $(m_1,m_2)$ we compute Cohen’s $\kappa$:
$$
\kappa = \frac{p_o - p_e}{1 - p_e},
$$
where $p_o$ is observed agreement and $p_e$ the chance agreement from the marginal distributions.

**Argument alignment.** Mean pairwise Jaccard $\bar{J}$ per claim, compared against a permutation baseline $\bar{J}_0$ obtained by shuffling scaffold sets across claims.

**Convergence signature.** The core falsifiable prediction of the retrieval model is a positive association between representation depth $d_c$ and agreement. We test it with a rank correlation between $d_c$ and per‑claim $\kappa_c$, and with a two‑group comparison of $\bar{J}$ between high‑depth ($d_c \geq 0.5$) and low‑depth ($d_c < 0.5$) claims.

### 3.4 Formal retrieval model

Let $\mathcal{L}$ be the consensus lattice: a set of canonical argument nodes, each with a retrieval probability $r_s$ for model $m$ on claim $c$. Under gate‑check convergence, model $m$’s scaffold is drawn i.i.d. from a distribution $P_m(\cdot\mid c)$ concentrated on the lattice neighborhood of $s_c$, with concentration increasing in $d_c$. Under correlated hallucination, scaffolds are drawn from a model‑idiosyncratic distribution with no dependence on $d_c$. The two hypotheses differ observably only through the $d_c$‑dependence and the ground‑truth correlation, which is why the benchmark must span the depth range.

## 4. Analysis

All numbers in this section are derived from explicitly stated inputs. Where an input is an assumption of the protocol design rather than an empirical measurement, it is labeled as such.

### 4.1 Chance agreement baseline

**Input (design assumption).** With $K = 4$ verdict categories and, pessimistically, a uniform verdict distribution, the probability that two independent models agree on a single claim by chance is:
$$
p_e^{(1)} = \sum_{k=1}^{4} \left(\frac{1}{4}\right)^2 = 4 \times \frac{1}{16} = \frac{1}{4} = 0.25.
$$

**Chance that $M$ models all agree on one claim.** For $M$ independent models:
$$
p_{\mathrm{all}}(M) = \left(\frac{1}{4}\right)^{M-1}.
$$
Computing for $M = 3, 5, 7$:
$$
p_{\mathrm{all}}(3) = \left(\frac{1}{4}\right)^2 = \frac{1}{16} = 0.0625,
$$
$$
p_{\mathrm{all}}(5) = \left(\frac{1}{4}\right)^4 = \frac{1}{256} \approx 3.906 \times 10^{-3},
$$
$$
p_{\mathrm{all}}(7) = \left(\frac{1}{4}\right)^6 = \frac{1}{4096} \approx 2.441 \times 10^{-4}.
$$

**Chance that $M$ models all agree on all $n$ claims in a benchmark.** For $n$ independent claims:
$$
p_{\mathrm{unanimous}}(M, n) = \left(\frac{1}{4}\right)^{(M-1)n}.
$$
For $M = 5$ models and $n = 60$ claims:
$$
p_{\mathrm{unanimous}}(5, 60) = \left(\frac{1}{4}\right)^{240} = 4^{-240}.
$$
In base 10: $\log_{10}(4) \approx 0.60206$, so
$$
\log_{10} p_{\mathrm{unanimous}} = -240 \times 0.60206 = -144.494,
$$
$$
p_{\mathrm{unanimous}}(5, 60) \approx 3.2 \times 10^{-145}.
$$
This establishes that unanimous cross‑model agreement on a 60‑claim benchmark is essentially impossible under the uniform‑chance null, so any observed near‑unanimity demands an explanation (shared retrieval or shared bias).

### 4.2 Benchmark size for a usable kappa confidence interval

**Inputs (design assumptions).** We require a $95\%$ confidence interval on $\kappa$ of half‑width $w = 0.10$. A standard large‑sample approximation for the variance of $\kappa$ (Fleiss‑style) is $\mathrm{Var}(\hat{\kappa}) \approx \frac{p_o(1-p_o)}{n(1-p_e)^2}$. Take an anticipated observed agreement $p_o = 0.80$ (a design target, not a measurement) and the uniform $p_e = 0.25$ from Section 4.1.

Then $1 - p_e = 0.75$, $(1-p_e)^2 = 0.5625$, and:
$$
n = \frac{p_o(1-p_o)}{w^2 (1-p_e)^2} \times z_{0.975}^2,
$$
with $z_{0.975} \approx 1.96$, $z^2 \approx 3.8416$.

Compute step by step:
$$
p_o(1-p_o) = 0.80 \times 0.20 = 0.16,
$$
$$
w^2 = 0.10^2 = 0.01,
$$
$$
w^2 (1-p_e)^2 = 0.01 \times 0.5625 = 0.005625,
$$
$$
\frac{p_o(1-p_o)}{w^2(1-p_e)^2} = \frac{0.16}{0.005625} \approx 28.444,
$$
$$
n = 28.444 \times 3.8416 \approx 109.3.
$$

So approximately $n \approx 110$ paired evaluations per model pair are needed. Since each claim yields one paired evaluation per model pair, and we have $\binom{M}{2}$ pairs, a benchmark of $n = 110$ claims evaluated by all models gives each pair the full $n$. If instead we accept a coarser half‑width $w = 0.15$:
$$
w^2 = 0.0225, \quad w^2(1-p_e)^2 = 0.0225 \times 0.5625 = 0.012656,
$$
$$
\frac{0.16}{0.012656} \approx 12.642, \quad n = 12.642 \times 3.8416 \approx 48.6,
$$
i.e., $n \approx 49$ claims. We therefore specify a benchmark of **at least 50 claims** for exploratory analysis and **110 claims** for the confirmatory analysis, with the caveat that these figures assume $p_o = 0.80$; if true agreement is lower, required $n$ rises as $p_o(1-p_o)$ grows toward its maximum $0.25$ at $p_o = 0.5$, giving an upper bound:
$$
n_{\max} = \frac{0.25}{0.005625} \times 3.8416 = 44.444 \times 3.8416 \approx 170.7,
$$
i.e., at most about $171$ claims suffice for $w = 0.10$ under this approximation regardless of $p_o$.

### 4.3 Worked illustrative kappa computation

To make the metric concrete, we present a **fully hypothetical** confusion matrix for one model pair over $n = 50$ claims (labeled illustrative; not a measurement). Suppose the paired verdicts distribute as:

| | Model B: falsified | Model B: trivial | Model B: valid‑flawed | Model B: other | row total |
|---|---|---|---|---|---|
| **A: falsified** | 20 | 2 | 1 | 0 | 23 |
| **A: trivial** | 1 | 10 | 2 | 0 | 13 |
| **A: valid‑flawed** | 0 | 2 | 9 | 1 | 12 |
| **A: other** | 0 | 0 | 1 | 1 | 2 |
| **col total** | 21 | 14 | 13 | 2 | 50 |

Observed agreement:
$$
p_o = \frac{20 + 10 + 9 + 1}{50} = \frac{40}{50} = 0.80.
$$

Expected agreement by chance, from the product of marginals:
$$
p_e = \frac{1}{50^2}\left(23 \times 21 + 13 \times 14 + 12 \times 13 + 2 \times 2\right).
$$
Compute each term: $23 \times 21 = 483$; $13 \times 14 = 182$; $12 \times 13 = 156$; $2 \times 2 = 4$. Sum: $483 + 182 + 156 + 4 = 825$.
$$
p_e = \frac{825}{2500} = 0.33.
$$

Then:
$$
\kappa = \frac{0.80 - 0.33}{1 - 0.33} = \frac{0.47}{0.67} \approx 0.7015.
$$

This illustrates the interpretation scale: $\kappa \approx 0.70$ would indicate substantial agreement well above the chance level $p_e = 0.33$ implied by these marginals — notably higher than the uniform‑chance $0.25$ because both models favor the “falsified” category.

### 4.4 Power for the depth‑agreement correlation

**Inputs (design assumptions).** The falsifiable signature is a positive rank correlation $\rho$ between representation depth $d_c$ and per‑claim agreement $\kappa_c$. For a Spearman correlation, the approximate sample size to detect effect size $\rho$ with power $1-\beta = 0.80$ at $\alpha = 0.05$ (two‑sided) is:
$$
n = \left(\frac{z_{0.975} + z_{0.80}}{\rho}\right)^2 + 3,
$$
with $z_{0.80} \approx 0.8416$. For a moderate effect $\rho = 0.35$:
$$
z_{0.975} + z_{0.80} = 1.96 + 0.8416 = 2.8016,
$$
$$
\left(\frac{2.8016}{0.35}\right)^2 = (8.0046)^2 \approx 64.07,
$$
$$
n = 64.07 + 3 \approx 67.1.
$$
So roughly $n \approx 68$ claims are needed to detect a depth–agreement correlation of $\rho = 0.35$; the confirmatory benchmark of $n = 110$ (Section 4.2) comfortably exceeds this, and even the exploratory $n = 50$ gives power for effects of $\rho \gtrsim 0.42$:
$$
\rho_{\min} \approx \frac{2.8016}{\sqrt{50 - 3}} = \frac{2.8016}{\sqrt{47}} = \frac{2.8016}{6.8557} \approx 0.4087.
$$

### 4.5 Distinguishing signature: agreement gap projection

Under the retrieval model, define the predicted agreement gap:
$$
\Delta = \kappa_{\mathrm{high\text{-}depth}} - \kappa_{\mathrm{low\text{-}depth}}.
$$
Gate‑check convergence predicts $\Delta > 0$; correlated hallucination predicts $\Delta \approx 0$. With the two‑group sizes implied by a split at $d_c = 0.5$ over $n = 110$ claims (assume a balanced split, $n_1 = n_2 = 55$ as a design assumption), the standard error of the difference of two independent kappa estimates, each with variance approximated as in Section 4.2 scaled to $n_1 = n_2 = 55$, is:
$$
\mathrm{Var}(\hat{\kappa}_i) \approx \frac{0.16}{55 \times 0.5625} = \frac{0.16}{30.9375} \approx 5.171 \times 10^{-3},
$$
$$
\mathrm{SE}(\Delta) = \sqrt{2 \times 5.171 \times 10^{-3}} = \sqrt{1.0341 \times 10^{-2}} \approx 0.1017.
$$
Thus a gap of $\Delta = 0.20$ would be about $0.20 / 0.1017 \approx 1.97$ standard errors — marginal at $\alpha = 0.05$ two‑sided — while $\Delta = 0.30$ would be $\approx 2.95$ standard errors and clearly detectable. This calibrates the effect size the benchmark can resolve: the protocol is powered for gaps of roughly $\Delta \geq 0.30$ under the stated assumptions.

## 5. Results

This paper reports no empirical model runs; the results are the protocol‑level quantities derived in Section 4, plus explicitly labeled projections.

**R1 (computed).** Under a uniform four‑category chance model, pairwise chance agreement is $p_e^{(1)} = 0.25$ (Section 4.1).

**R2 (computed).** Unanimous agreement of $M$ models on one claim has chance probability $4^{-(M-1)}$: $0.0625$ for $M=3$, $\approx 3.906 \times 10^{-3}$ for $M=5$, $\approx 2.441 \times 10^{-4}$ for $M=7$ (Section 4.1).

**R3 (computed).** Unanimous agreement of $M = 5$ models across $n = 60$ claims has chance probability $\approx 3.2 \times 10^{-145}$ (Section 4.1).

**R4 (computed).** Benchmark size: $n \approx 110$ claims for a kappa confidence interval of half‑width $w = 0.10$ on $\kappa$ (Section 4.2); $n \approx 49$ claims suffice for the coarser half‑width $w = 0.15$; and the worst‑case upper bound over all values of $p_o$ is $n_{\max} \approx 171$ claims for $w = 0.10$ (Section 4.2). The protocol therefore specifies at least 50 claims for exploratory analysis and 110 claims for confirmatory analysis.

**R5 (computed).** Power for the depth–agreement signature: approximately $n \approx 68$ claims are required to detect a Spearman correlation of $\rho = 0.35$ between representation depth $d_c$ and per‑claim agreement $\kappa_c$ at power $0.80$, $\alpha = 0.05$ two‑sided; the exploratory benchmark of $n = 50$ claims is powered only for effects $\rho \gtrsim 0.41$ (Section 4.4).

**R6 (computed).** Resolution of the agreement gap: with a balanced two‑group split ($n_1 = n_2 = 55$) of a 110‑claim benchmark, the standard error of the difference $\Delta = \kappa_{\mathrm{high\text{-}depth}} - \kappa_{\mathrm{low\text{-}depth}}$ is $\mathrm{SE}(\Delta) \approx 0.1017$, so the protocol resolves gaps of $\Delta \gtrsim 0.30$ at two‑sided $\alpha = 0.05$; a gap of $\Delta = 0.20$ is only about $1.97$ standard errors and marginal (Section 4.5).

**R7 (computed, illustrative).** The worked kappa computation of Section 4.3, on a fully hypothetical confusion matrix over $n = 50$ claims, yields $p_o = 0.80$, $p_e = 0.33$, and $\kappa \approx 0.7015$. This is an illustration of the metric machinery only, not a measurement of any model pair.

## 6. Discussion

**Limitations of the statistical machinery.** All sample‑size and power figures rest on a large‑sample variance approximation $\mathrm{Var}(\hat{\kappa}) \approx p_o(1-p_o)/\bigl(n(1-p_e)^2\bigr)$, which ignores the higher‑order terms of the exact Fleiss variance and can be optimistic when marginals are skewed, as the illustrative matrix of Section 4.3 already shows ($p_e = 0.33$ rather than the uniform $0.25$). The uniform‑chance baseline $p_e^{(1)} = 0.25$ is a pessimistic floor: real verdict marginals are concentrated (models favor “falsified” on fringe claims), which raises chance agreement and lowers $\kappa$ for a given $p_o$. The design target $p_o = 0.80$ is an assumption, not a measurement; if true agreement is near $p_o = 0.5$, the required benchmark grows to $n_{\max} \approx 171$ claims (Section 4.2). The power formula for Spearman correlation is itself an approximation, and the balanced‑split assumption $n_1 = n_2 = 55$ may fail if representation depth $d_c$ is skewed toward high values, inflating $\mathrm{SE}(\Delta)$ beyond the computed $0.1017$.

**Limitations of the benchmark design.** The representation‑depth score $d_c \in [0,1]$ depends on a proxy (normalized count of canonical textbook treatments) that is itself a researcher judgment; a mis‑calibrated $d_c$ directly weakens the central falsifiable test, since the predicted signature is a positive association between $d_c$ and agreement. Expert verdicts require at least two independent domain experts with a documented adjudication rule, but for fringe‑adjacent items such as [9] the expert ground truth is itself contested, as noted in Section 2; for [10] and [12] the supplied documentation is empty or title‑only, so expert verdicts would have to be established de novo. The scaffold‑graph parsing of argument structure into primitives is a further manual step with its own inter‑annotator reliability problem, which this protocol does not yet quantify.

**Failure modes and what would falsify the claims.** The gate‑check‑convergence hypothesis is falsified if a benchmark of the specified size finds $\Delta \approx 0$ (no depth–agreement association) while overall agreement remains high; that pattern would support the correlated‑hallucination explanation. Conversely, finding $\Delta > 0$ with the predicted sign, robust across prompt framings and model families, would support retrieval from a shared consensus lattice — though it would not fully exclude a subtler shared‑bias contribution, since both mechanisms predict high agreement and only the depth‑dependence and ground‑truth correlation separate them. A third outcome — low agreement everywhere — would indicate that fringe physics claims are too idiosyncratic for any shared scaffold, collapsing the benchmark’s premise. An additional confound the protocol must control: prompt framing ($F \geq 3$ framings) could interact with depth, and a framing‑stratified reanalysis is required before attributing any gap to retrieval rather than to framing sensitivity.

**Open questions.** Whether the argument‑structure alignment $\bar{J}$ adds information beyond verdict $\kappa$; whether citation‑quality variance behaves as predicted under the two hypotheses; and how the trichotomy of claim classes maps onto verdict categories models actually use (the “other” category absorbs mismatches in the illustrative matrix of Section 4.3) all remain to be established empirically. The bibliography available for grounding is also limited: several entries ([10], [12]) supply no substantive content beyond titles, and others ([2], [7]) connect only analogically, so the related‑work coverage of the core question — cross‑LLM agreement measurement — is thinner than the entry count suggests.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers designing LLM evaluation benchmarks, AI‑safety teams assessing model reliability, and policy makers evaluating the trustworthiness of LLM‑generated scientific advice would use the GCC protocol to decide whether observed cross‑model agreement on fringe physics claims can be interpreted as evidence of consensus retrieval or as a correlated failure mode. If the depth‑agreement signature holds, developers may prioritize improving representation of consensus material in training data; if it fails, they may invest in mechanisms to detect and mitigate hallucination.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA Technology Readiness Level definitions, it resides at TRL 1–2 (basic principles observed and reported). Analytical work never exceeds TRL 3 without empirical validation.

**(c) Smallest next experiment.** A pilot study with $M = 3$