# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Pairwise chance agreement under uniform four-category model is 0.25",
    "inputs": "K=4 categories, uniform probability 1/4 per category",
    "formula": "p_e = sum_{k=1}^{4} (1/4)^2 = 4 * 1/16 = 0.25"
  },
  {
    "id": "Q2",
    "statement": "Chance that M models all agree on one claim: 0.0625 for M=3, 0.003906 for M=5, 0.0002441 for M=7",
    "inputs": "p=1/4 per model, M in {3,5,7}",
    "formula": "p_all(M) = (1/4)^(M-1)"
  },
  {
    "id": "Q3",
    "statement": "Chance that 5 models all agree on all 60 claims is approximately 3.2e-145",
    "inputs": "M=5, n=60, p=1/4, log10(4)=0.60206",
    "formula": "p_unanimous = (1/4)^((M-1)*n) = 4^(-240); log10 p = -240*0.60206 = -144.494"
  },
  {
    "id": "Q4",
    "statement": "Benchmark size n approximately 110 claims for kappa CI half-width w=0.10",
    "inputs": "p_o=0.80, p_e=0.25, w=0.10, z=1.96 (z^2=3.8416)",
    "formula": "n = p_o*(1-p_o) / (w^2*(1-p_e)^2) * z^2 = 0.16/0.005625 * 3.8416"
  },
  {
    "id": "Q5",
    "statement": "Benchmark size n approximately 49 claims for half-width w=0.15",
    "inputs": "p_o=0.80, p_e=0.25, w=0.15, z^2=3.8416",
    "formula": "n = 0.16/(0.0225*0.5625) * 3.8416"
  },
  {
    "id": "Q6",
    "statement": "Worst-case benchmark size n_max approximately 171 claims for w=0.10",
    "inputs": "max p_o(1-p_o)=0.25 at p_o=0.5, p_e=0.25, w=0.10, z^2=3.8416",
    "formula": "n_max = 0.25/0.005625 * 3.8416"
  },
  {
    "id": "Q7",
    "statement": "Worked illustrative kappa: p_o=0.80, p_e=0.33, kappa approximately 0.7015",
    "inputs": "confusion matrix diagonal sum=40, n=50, marginal products sum=825 (23*21=483, 13*14=182, 12*13=156, 2*2=4)",
    "formula": "p_o=40/50=0.80; p_e=825/2500=0.33; kappa=(0.80-0.33)/(1-0.33)"
  },
  {
    "id": "Q8",
    "statement": "Approximately 68 claims needed to detect Spearman correlation rho=0.35 at power 0.80, alpha=0.05 two-sided",
    "inputs": "z_0.975=1.96, z_0.80=0.8416, rho=0.35",
    "formula": "n = ((z_0.975+z_0.80)/rho)^2 + 3 = (2.8016/0.35)^2 + 3"
  }
]

## Script
```python
# Gate-Check Convergence: A Benchmark Protocol for Measuring Cross-Model Agreement on Fringe Physics Claims

## Abstract

Large language models (LLMs) are increasingly consulted as informal arbiters of scientific claims, including claims at the fringe of established physics. We propose a benchmark protocol — Gate-Check Convergence (GCC) — for testing a specific hypothesis: that independent LLMs, when asked to render verdicts on novel fringe physics claims, converge not merely on the verdict itself but on the reasoning scaffold used to reach it (for example, Bell's theorem for hidden-variable claims, the $SU(2)/SO(3)$ homomorphism for spin claims, or BCS gap arithmetic for superconductivity claims). We formalize the hypothesis as retrieval from an overlapping "consensus lattice" in the training corpora, which predicts higher inter-model agreement on well-represented consensus results than on frontier questions — a falsifiable signature distinguishing genuine gate-checking from correlated hallucination. We specify the benchmark construction (falsified, trivial, and valid-but-flawed claim classes with expert ground truth), the blinded evaluation protocol, and the statistics: Cohen's $\kappa$ on verdicts, argument-structure alignment scores, and citation-quality variance. We derive the required sample sizes, chance-agreement baselines, and power calculations in full arithmetic, and we present a worked illustrative kappa computation ($\kappa \approx 0.7015$ on a hypothetical $50$-claim matrix). No empirical model runs are reported here; the paper contributes the protocol, the formal model, and the analysis machinery needed to execute and falsify the claim.

## 1. Introduction

When a user asks an LLM whether some exotic claim — a faster-than-light signaling scheme, a classical reconstruction of quantum statistics, a room-temperature superconductivity mechanism — is credible, the model performs what we call a *gate check*: a rapid triage of the claim against the boundaries of accepted physics. Anecdotal observation suggests that different models, from different families and trained by different organizations, often reach the same verdict *and* deploy the same argument: the same invocation of Bell's theorem, the same appeal to the covering map from $SU(2)$ to $SO(3)$, the same BCS gap estimate. This observation motivates the central question of this paper:

> Is cross-model convergence on fringe physics claims robust across claim domains, model families, and prompt framings, and does it correlate with accuracy against expert ground truth?

Two explanations compete. **Gate-check convergence**: models retrieve a shared consensus lattice — the same textbooks, reviews, and canonical refutations present in all large training corpora — and the shared retrieval produces both the verdict and the argument structure. **Correlated hallucination**: models share systematic failure modes (similar pretraining objectives, similar RLHF pressures toward confident-sounding verdicts) that produce coincident wrong answers without genuine evidential grounding. These explanations diverge in a measurable way: gate-check convergence predicts that agreement *rises* with how well-represented the relevant consensus material is in the literature, and that agreement on frontier or genuinely novel questions drops toward the chance baseline; correlated hallucination predicts agreement that is high but *uncorrelated* with representation depth and uncorrelated with expert ground truth.

This paper makes three contributions. First, a benchmark design: a corpus of fringe physics claims with known expert verdicts, partitioned into three classes (falsified, trivial, valid-but-flawed), each annotated with the canonical consensus argument. Second, an evaluation protocol: blinded, prompt-framing-varied evaluations across multiple model families, scored with Cohen's $\kappa$ on verdicts, an argument-structure alignment metric, and citation-quality variance. Third, a formal retrieval model that yields quantitative, falsifiable predictions, together with the full statistical machinery — sample sizes, chance baselines, and power calculations — derived explicitly.

We emphasize scope: this paper reports *no* model runs. It is a protocol and analysis paper. Every number in Section 4 is either derived from stated inputs by shown arithmetic or explicitly labeled a projection under stated assumptions.

## 2. Background and Related Work

The literature available for grounding this proposal spans several adjacent areas; we discuss each entry in turn, noting that several are only loosely connected and that the supplied summaries constrain what can be claimed about them.

**[1] Conjectures on Convergence and Scalar Curvature (arXiv:2103.10093v1).** This work surveys compactness and geometric stability conjectures formulated by participants at the 2018 IAS Emerging Topics Workshop on Scalar Curvature and Convergence, focusing on sequences of compact Riemannian manifolds with nonnegative scalar curvature. We cite it as an example of a *consensus lattice node* in mathematics: a community-formulated set of conjectures whose status is well-represented in the literature and therefore, under our hypothesis, should elicit highly convergent LLM verdicts. The summary supplied gives no further detail on outcomes, and we claim none.

**[2] Leveraging LLMs for Unstructured Claims Data Analysis (arXiv:2606.06089v1).** This paper presents a proof-of-concept framework using large language models to process unstructured text — medical records, adjuster notes, call transcripts — in an actuarial claims context, motivated by the inconsistency and unscalability of manual document processing. It is relevant as evidence that LLM-based claims evaluation is being deployed operationally, and its framing of claims as objects requiring consistent cross-reviewer treatment parallels our inter-model consistency requirement. The summary does not report accuracy figures, and we do not assert any.

**[3] Physics Briefing Book (arXiv:1910.11775v2).** This document describes the European Particle Physics Strategy Update (EPPSU) process, a bottom-up community exercise in which national inputs and inputs from National Laboratories are solicited to shape particle physics priorities. We use it to illustrate how *expert consensus is formed and recorded* in physics: a documented, citable consensus process whose outputs populate the training corpora that our retrieval model posits. The summary states the process structure but no findings, and we rely only on that structure.

**[4] Physics and Technology of the Next Linear Collider (arXiv:hep-ex/9605011v1).** This Snowmass '96 report presents design expectations for an $e^+e^-$ linear collider at center-of-mass energy $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$, reviews the experiments it would carry out in exploring physics beyond the Standard Model, and argues feasibility of construction. It serves as an example of a *frontier-adjacent* consensus document: beyond-Standard-Model physics is a domain where the consensus lattice is thinner and more contested, which our model predicts should lower cross-model agreement relative to settled domains.

**[5] A category mistake in observational claims regarding ultrashort-lived unstable particles (arXiv:1502.01303v3).** This paper argues that the $5\sigma$-convention in particle physics, as applied to claims that ultrashort-lived unstable particles such as a Higgs boson have been observed, produces a category mistake in which pure reasoning is passed off as observation. This is directly relevant to our benchmark: it is precisely the kind of meta-scientific consensus argument (a critique of evidential conventions) that we expect models to retrieve as a scaffold when evaluating "was X observed?" claims. It also supplies a claim class for our benchmark: verdicts that hinge on convention rather than fact.

**[6] Fact-Checking Meets Fauxtography (arXiv:1908.11722v1).** This work addresses automated verification of claims about images, noting that the volume of claims requiring fact-checking exceeds manual capacity by orders of magnitude and that prior automation work had largely ignored a modality-specific gap (the summary indicates image claims were previously neglected). Methodologically it is the closest analogue to our problem — automated claim verification against ground truth — and its framing of the scale problem motivates automated gate-checking. The supplied summary does not report its results in detail, and we do not cite specific performance numbers.

**[7] Integrating Proportionality and Egalitarianism in Claims Problems (arXiv:2605.26948v1).** This paper studies allocation of a finite estate among agents whose claims exceed resources, integrating the Proportional rule with the Constrained Equal Awards (CEA) rule. The connection is analogical: our benchmark allocates a finite evaluation budget (model runs, expert-verification hours) across claim classes, and claims-problem fairness rules offer a principled allocation template. We use it only for this structural analogy; the summary supports the rule definitions quoted above and nothing further.

**[8] Do Methods Support the Claims? Intra-Paper Verification for Peer Review (arXiv:2607.26066v1).** This work targets LLM-assisted peer review, observing that existing automated novelty assessment compares claimed contributions against prior literature while implicitly assuming those contributions are realized in the work itself, whereas human reviewers frequently challenge novelty claims at the level of method support. This is the closest published relative of our gate-check question: it asks whether a claim is *supported by the reasoning behind it*, which is exactly what we ask models to assess for fringe physics claims. The summary states the motivation and gap; it does not report results, and we claim none.

**[9] Five Pillars, One Structure: Consilient Convergence in QNFO Research (DOI 10.5281/zenodo.21603374).** This document reports that five independent QNFO research programs converge on a single structural insight: that ultrametric (non-Archimedean) mathematics provides the correct state-space geometry for fundamental physics, quantum computation, and optimization. It is a live example of a fringe-adjacent convergence claim — convergence of research programs on a structural thesis — and thus a natural benchmark item: models asked to evaluate it should, under our hypothesis, converge on a gate-check verdict, and the expert ground truth for that verdict is itself contested, making it a stress case for the accuracy-correlation question.

**[10] The Continuum Critique Trilogy (DOI 10.5281/zenodo.21691415).** The supplied summary is empty; no substantive content is available. We note its existence as part of the fringe-corpus candidate pool and can relate it to our argument only as an unannotated benchmark candidate whose expert verdict would need to be established de novo.

**[11] A Critical Treatise on the Load-Bearing Assumptions of Quantum Mechanics, Thermodynamics, and Computation (DOI 10.5281/zenodo.21975507).** This treatise examines load-bearing but rarely interrogated assumptions in the theoretical structure surrounding the electron — described as the most precisely measured particle in physics — including the complex Hilbert-space postulate and the spin-statistics theorem. It exemplifies the "valid-but-flawed" claim class: critiques of foundational assumptions that are legitimate philosophical targets but whose radical conclusions typically fail gate checks. The canonical scaffolds it interrogates (Hilbert-space postulate, spin-statistics) are exactly the consensus nodes our retrieval model names.

**[12] Five Objections, One Standard: An Evidence-Graded Adjudication of a Critique of Post-Quantum Synthesis (DOI 10.5281/zenodo.22010489).** The supplied summary is empty beyond the title. The title indicates an evidence-graded adjudication of objections to a synthesis critique, which matches our benchmark's need for graded expert verdicts; beyond that, the entry gives no detail, and we make no claims about its content.

In summary, the adjacent literature provides: automated claims-verification precedents [2], [6], [8]; examples of consensus formation and consensus documents in physics [1], [3], [4]; a meta-scientific critique relevant to verdict conventions [5]; an allocation-theoretic analogy [7]; and a pool of fringe-adjacent candidate claims [9], [10], [11], [12]. No prior work in this list measures cross-LLM agreement on fringe physics verdicts, which is the gap this protocol addresses.

## 3. Methods

### 3.1 Benchmark construction

The benchmark consists of $N_{\mathrm{claims}}$ fringe physics claims, each annotated with:

- an **expert verdict** $v_e \in \{\text{falsified}, \text{trivial}, \text{valid-but-flawed}\}$, established by at least two independent domain experts with a documented adjudication rule for disagreement;
- a **consensus-scaffold label** $s_c$: the canonical argument a physicist would deploy (e.g., Bell's theorem, the $SU(2) \to SO(3)$ covering map, BCS gap arithmetic, the $5\sigma$ convention critique of [5]);
- a **representation-depth score** $d_c \in [0,1]$: an operationalized estimate of how well-represented the scaffold is in the published literature, measured by a documented proxy (e.g., count of canonical textbook treatments, normalized).

Claim classes follow the trichotomy of the research idea: *falsified* (contradicts established results), *trivial* (restates known results as if novel), *valid-but-flawed* (sound motivation, defective execution), with candidate items drawn from the fringe corpus exemplified by [9], [10], [11], [12] and from beyond-Standard-Model territory of the kind surveyed in [4].

### 3.2 Evaluation protocol

Each claim is evaluated by $M$ models from at least three families, under $F \geq 3$ prompt framings (neutral, adversarial, charitable), blinded in the sense that no model output is visible to any other evaluation and order is randomized. For each run we record:

1. the **verdict** $v_{m,f,c} \in \{\text{falsified}, \text{trivial}, \text{valid-but-flawed}, \text{other}\}$;
2. the **argument structure**, parsed into a scaffold graph whose nodes are argument primitives and whose edges are inferential steps; alignment between two runs is the Jaccard similarity of their primitive sets:
$$J_{(i,j)} = \frac{|S_i \cap S_j|}{|S_i \cup S_j|},$$
where $S_i$ is the scaffold-primitive set of run $i$;
3. the **citations** offered, scored for quality (verifiability, relevance, correctness) on a rubric scale.

### 3.3 Statistics

**Verdict agreement.** For each model pair $(m_1, m_2)$ we compute Cohen's $\kappa$:
$$\kappa = \frac{p_o - p_e}{1 - p_e},$$
where $p_o$ is observed agreement and $p_e$ the chance agreement from the marginal distributions.

**Argument alignment.** Mean pairwise Jaccard $\bar{J}$ per claim, compared against a permutation baseline $\bar{J}_0$ obtained by shuffling scaffold sets across claims.

**Convergence signature.** The core falsifiable prediction of the retrieval model is a positive association between representation depth $d_c$ and agreement. We test it with a rank correlation between $d_c$ and per-claim $\kappa_c$, and with a two-group comparison of $\bar{J}$ between high-depth ($d_c \geq 0.5$) and low-depth ($d_c < 0.5$) claims.

### 3.4 Formal retrieval model

Let $\mathcal{L}$ be the consensus lattice: a set of canonical argument nodes, each with a retrieval probability $r_s$ for model $m$ on claim $c$. Under gate-check convergence, model $m$'s scaffold is drawn i.i.d. from a distribution $P_m(\cdot \mid c)$ concentrated on the lattice neighborhood of $s_c$, with concentration increasing in $d_c$. Under correlated hallucination, scaffolds are drawn from a model-idiosyncratic distribution with no dependence on $d_c$. The two hypotheses differ observably only through the $d_c$-dependence and the ground-truth correlation, which is why the benchmark must span the depth range.

## 4. Analysis

All numbers in this section are derived from explicitly stated inputs. Where an input is an assumption of the protocol design rather than an empirical measurement, it is labeled as such.

### 4.1 Chance agreement baseline

**Input (design assumption).** With $K = 4$ verdict categories and, pessimistically, a uniform verdict distribution, the probability that two independent models agree on a single claim by chance is:
$$p_e^{(1)} = \sum_{k=1}^{4} \left(\frac{1}{4}\right)^2 = 4 \times \frac{1}{16} = \frac{1}{4} = 0.25.$$

**Chance that $M$ models all agree on one claim.** For $M$ independent models:
$$p_{\mathrm{all}}(M) = \left(\frac{1}{4}\right)^{M-1}.$$
Computing for $M = 3, 5, 7$:
$$p_{\mathrm{all}}(3) = \left(\frac{1}{4}\right)^2 = \frac{1}{16} = 0.0625,$$
$$p_{\mathrm{all}}(5) = \left(\frac{1}{4}\right)^4 = \frac{1}{256} \approx 3.906 \times 10^{-3},$$
$$p_{\mathrm{all}}(7) = \left(\frac{1}{4}\right)^6 = \frac{1}{4096} \approx 2.441 \times 10^{-4}.$$

**Chance that $M$ models all agree on all $n$ claims in a benchmark.** For $n$ independent claims:
$$p_{\mathrm{unanimous}}(M, n) = \left(\frac{1}{4}\right)^{(M-1)n}.$$
For $M = 5$ models and $n = 60$ claims:
$$p_{\mathrm{unanimous}}(5, 60) = \left(\frac{1}{4}\right)^{240} = 4^{-240}.$$
In base 10: $\log_{10}(4) \approx 0.60206$, so
$$\log_{10} p_{\mathrm{unanimous}} = -240 \times 0.60206 = -144.494,$$
$$p_{\mathrm{unanimous}}(5, 60) \approx 3.2 \times 10^{-145}.$$
This establishes that unanimous cross-model agreement on a 60-claim benchmark is essentially impossible under the uniform-chance null, so any observed near-unanimity demands an explanation (shared retrieval or shared bias).

### 4.2 Benchmark size for a usable kappa confidence interval

**Inputs (design assumptions).** We require a $95\%$ confidence interval on $\kappa$ of half-width $w = 0.10$. A standard large-sample approximation for the variance of $\kappa$ (Fleiss-style) is $\mathrm{Var}(\hat{\kappa}) \approx \frac{p_o(1-p_o)}{n(1-p_e)^2}$. Take an anticipated observed agreement $p_o = 0.80$ (a design target, not a measurement) and the uniform $p_e = 0.25$ from Section 4.1.

Then $1 - p_e = 0.75$, $(1-p_e)^2 = 0.5625$, and:
$$n = \frac{p_o(1-p_o)}{w^2 (1-p_e)^2} \times z_{0.975}^2,$$
with $z_{0.975} \approx 1.96$, $z^2 \approx 3.8416$.

Compute step by step:
$$p_o(1-p_o) = 0.80 \times 0.20 = 0.16,$$
$$w^2 = 0.10^2 = 0.01,$$
$$w^2 (1-p_e)^2 = 0.01 \times 0.5625 = 0.005625,$$
$$\frac{p_o(1-p_o)}{w^2(1-p_e)^2} = \frac{0.16}{0.005625} \approx 28.444,$$
$$n = 28.444 \times 3.8416 \approx 109.3.$$

So approximately $n \approx 110$ paired evaluations per model pair are needed. Since each claim yields one paired evaluation per model pair, and we have $\binom{M}{2}$ pairs, a benchmark of $n = 110$ claims evaluated by all models gives each pair the full $n$. If instead we accept a coarser half-width $w = 0.15$:
$$w^2 = 0.0225, \quad w^2(1-p_e)^2 = 0.0225 \times 0.5625 = 0.012656,$$
$$\frac{0.16}{0.012656} \approx 12.642, \quad n = 12.642 \times 3.8416 \approx 48.6,$$
i.e., $n \approx 49$ claims. We therefore specify a benchmark of **at least 50 claims** for exploratory analysis and **110 claims** for the confirmatory analysis, with the caveat that these figures assume $p_o = 0.80$; if true agreement is lower, required $n$ rises as $p_o(1-p_o)$ grows toward its maximum $0.25$ at $p_o = 0.5$, giving an upper bound:
$$n_{\max} = \frac{0.25}{0.005625} \times 3.8416 = 44.444 \times 3.8416 \approx 170.7,$$
i.e., at most about $171$ claims suffice for $w = 0.10$ under this approximation regardless of $p_o$.

### 4.3 Worked illustrative kappa computation

To make the metric concrete, we present a **fully hypothetical** confusion matrix for one model pair over $n = 50$ claims (labeled illustrative; not a measurement). Suppose the paired verdicts distribute as:

| | Model B: falsified | Model B: trivial | Model B: valid-flawed | Model B: other | row total |
|---|---|---|---|---|---|
| **Model A: falsified** | 19 | 2 | 2 | 0 | 23 |
| **Model A: trivial** | 1 | 10 | 2 | 0 | 13 |
| **Model A: valid-flawed** | 1 | 2 | 9 | 0 | 12 |
| **Model A: other** | 0 | 0 | 0 | 2 | 2 |
| **column total** | 21 | 14 | 13 | 2 | 50 |

Check row sums: $19+2+2+0 = 23$; $1+10+2+0 = 13$; $1+2+9+0 = 12$; $0+0+0+2 = 2$; total $23+13+12+2 = 50$. Check column sums: $19+1+1+0 = 21$; $2+10+2+0 = 14$; $2+2+9+0 = 13$; $0+0+0+2 = 2$; total $21+14+13+2 = 50$.

**Observed agreement.** Diagonal sum:
$$a_{11} + a_{22} + a_{33} + a_{44} = 19 + 10 + 9 + 2 = 40,$$
$$p_o = \frac{40}{50} = 0.80.$$

**Chance agreement.** From the marginal products:
$$p_e = \frac{(23)(21) + (13)(14) + (12)(13) + (2)(2)}{50^2} = \frac{483 + 182 + 156 + 4}{2500} = \frac{825}{2500} = 0.33.$$

**Kappa.**
$$\kappa = \frac{p_o - p_e}{1 - p_e} = \frac{0.80 - 0.33}{1 - 0.33} = \frac{0.47}{0.67} \approx 0.7015.$$

This illustrative value sits in the "substantial agreement" band and is the kind of number the confirmatory benchmark is powered to resolve (Section 4.2): with $n = 110$, the half-width $w = 0.10$ means a true $\kappa$ anywhere in $[0.60, 0.80]$ would be distinguishable from the chance-consistent value $\kappa = 0$ at the design precision.

### 4.4 Power for the depth–agreement correlation

**Inputs (design assumptions).** The core falsifiable prediction is a positive rank correlation between representation depth $d_c$ and per-claim agreement. We power the study to detect a Spearman correlation $\rho = 0.35$ (a modest effect, chosen as a design target, not a measurement) at power $1 - \beta = 0.80$ with two-sided $\alpha = 0.05$. Using the standard Fisher-style approximation for sample size for a correlation:
$$n = \left(\frac{z_{0.975} + z_{0.80}}{\rho}\right)^2 + 3,$$
with $z_{0.975} = 1.96$ and $z_{0.80} = 0.8416$.

Compute step by step:
$$z_{0.975} + z_{0.80} = 1.96 + 0.8416 = 2.8016,$$
$$\frac{2.8016}{0.35} \approx 8.0046,$$
$$\left(8.0046\right)^2 \approx 64.073,$$
$$n = 64.073 + 3 \approx 67.1.$$

So approximately $68$ claims are needed to detect $\rho = 0.35$ at the stated power. This is below the exploratory benchmark size of $50$ only marginally short; the confirmatory benchmark of $110$ claims comfortably exceeds it, and would detect correlations as small as roughly $\rho \approx 0.28$ at the same power (solving $\left(2.8016/\rho\right)^2 + 3 = 110$ gives $2.8016/\rho = \sqrt{107} \approx 10.344$, hence $\rho \approx 0.2709$; conservatively reported as $\rho \approx 0.27$–$0.28$).

### 4.5 Budget allocation analogy

Following the allocation template of [7], if the confirmatory benchmark contains $n = 110$ claims and the expert-verification budget allows only $b = 80$ full expert adjudications, the Proportional rule would allocate each claim class $i$ with claim count $n_i$ a share $b_i = b \cdot n_i / n$; e.g., for a design mix of $n_1 = 44$ falsified, $n_2 = 33$ trivial, $n_3 = 33$ valid-but-flawed claims:
$$b_1 = 80 \times \frac{44}{110} = 32, \quad b_2 = 80 \times \frac{33}{110} = 24, \quad b_3 = 24.$$
This is a design illustration of the analogy only; the fairness properties of the rule are not investigated here.

## 5. Results

This paper reports no empirical model runs; the results are the derived design quantities of Section 4, each computed there with shown arithmetic:

1. **Chance baselines (Section 4.1).** Pairwise chance agreement $p_e^{(1)} = 0.25$ under the uniform four-category null; chance of unanimous agreement by $M$ models on one claim $p_{\mathrm{all}}(3) = 0.0625$, $p_{\mathrm{all}}(5) \approx 3.906 \times 10^{-3}$, $p_{\mathrm{all}}(7) \approx 2.441 \times 10^{-4}$; chance of unanimous agreement by $M = 5$ models on all $n = 60$ claims $p_{\mathrm{unanimous}} \approx 3.2 \times 10^{-145}$.
2. **Sample sizes (Section 4.2).** For a $95\%$ CI half-width $w = 0.10$ on $\kappa$ at anticipated $p_o = 0.80$: $n \approx 110$ claims; for $w = 0.15$: $n \approx 49$ claims; worst case over $p_o$: $n_{\max} \approx 171$ claims.
3. **Illustrative kappa (Section 4.3).** On the hypothetical $50$-claim confusion matrix: $p_o = 0.80$, $p_e = 0.33$, $\kappa \approx 0.7015$.
4. **Correlation power (Section 4.4).** $n \approx 68$ claims to detect $\rho = 0.35$ at power $0.80$, $\alpha = 0.05$ two-sided; the $110$-claim confirmatory benchmark detects $\rho \approx 0.27$ at the same power.
5. **Budget allocation (Section 4.5).** Under the stated design mix and $b = 80$: $(b_1, b_2, b_3) = (32, 24, 24)$.

All of these are consequences of stated design assumptions, not measurements. The empirical results the protocol is designed to produce — per-pair $\kappa$, scaffold-alignment $\bar{J}$ versus permutation baseline $\bar{J}_0$, and the depth–agreement rank correlation — remain to be measured by executing the protocol.

## 6. Discussion

**Limitations of the design assumptions.** Every sample-size figure rests on $p_e = 0.25$ from a uniform-category assumption. Real verdict marginals will be non-uniform — models will rarely answer "other" — which raises $p_e$ above $0.25$ and makes the uniform baseline conservative in one direction while the Fleiss-style variance approximation is itself only approximate. The anticipated $p_o = 0.80$ is a design target: if true agreement is near $0.5$, the required $n$ grows to the computed worst case of about $171$ claims. The correlation power calculation assumes independence of claims; correlated scaffolds across claims within a domain would inflate the effective sample size requirement.

**Failure modes of the benchmark itself.** Three are salient. First, *scaffold-label leakage*: if the representation-depth score $d_c$ is computed from the same literature the models trained on, the depth–agreement correlation could be an artifact of annotation rather than a property of models; the documented-proxy requirement of Section 3.1 mitigates but does not eliminate this. Second, *verdict-category collapse*: if models rarely use "other," the effective category count drops toward $K = 3$ and the
```

## Execution output
```

[stderr]
  File "<string>", line 5
    Large language models (LLMs) are increasingly consulted as informal arbiters of scientific claims, including claims at the fringe of established physics. We propose a benchmark protocol — Gate-Check Convergence (GCC) — for testing a specific hypothesis: that independent LLMs, when asked to render verdicts on novel fringe physics claims, converge not merely on the verdict itself but on the reasoning scaffold used to reach it (for example, Bell's theorem for hidden-variable claims, the $SU(2)/SO(3)$ homomorphism for spin claims, or BCS gap arithmetic for superconductivity claims). We formalize the hypothesis as retrieval from an overlapping "consensus lattice" in the training corpora, which predicts higher inter-model agreement on well-represented consensus results than on frontier questions — a falsifiable signature distinguishing genuine gate-checking from correlated hallucination. We specify the benchmark construction (falsified, trivial, and valid-but-flawed claim classes with expert ground truth), the blinded evaluation protocol, and the statistics: Cohen's $\kappa$ on verdicts, argument-structure alignment scores, and citation-quality variance. We derive the required sample sizes, chance-agreement baselines, and power calculations in full arithmetic, and we present a worked illustrative kappa computation ($\kappa \approx 0.7015$ on a hypothetical $50$-claim matrix). No empirical model runs are reported here; the paper contributes the protocol, the formal model, and the analysis machinery needed to execute and falsify the claim.
                                                                                                                                                                                              ^
SyntaxError: invalid character '—' (U+2014)

[exit 1]
```
