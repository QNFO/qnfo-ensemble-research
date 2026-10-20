# Grounding block - source: rem-9e69ce22-2d14-4d23-9468-cb130b873d86

## Research idea

Bayesian Decision Model for PQC Migration Under Unproven Factoring Hardness. The note's strongest original idea is that PQC migration urgency rests on the unproven conjecture FACTORING ∉ BPP, so migration timelines should treat this as an explicit Bayesian prior rather than a settled fact. A paper could formalize this: construct a decision-theoretic model where the probability of a classical polynomial-time factoring breakthrough (informed by GNFS constant stability since 1993, expert surveys, and complexity-class separation evidence) is a prior over crossover timelines, then compute optimal migration schedules and insurance-like cost-benefit curves for RSA-2048. Sensitivity analysis over priors would show how conclusions change if FACTORING ∈ BPP becomes likely. A companion formal analysis could quantify how much of claimed quantum advantage depends on this single unproven premise, and stress-test the claim that ≥80% of exponential speedups reduce to abelian hidden subgroup structure by classifying known speedups.

Source: owner notebook notes/v1/2026/07/14/_26195142717.md

## Existing paper under revision (remediation only)

# Factoring Hardness as a Bayesian Prior: A Decision-Theoretic Model of Post-Quantum Cryptography Migration Timing

## Abstract

The urgency of post-quantum cryptography (PQC) migration is usually justified by the anticipated capability of quantum computers to factor integers, yet that threat rests on an unproven complexity-theoretic conjecture: that integer factoring is not in BPP, the class of decision problems solvable in bounded-error probabilistic polynomial time. This paper treats that conjecture as an explicit Bayesian prior rather than a settled fact, and embeds it in a decision-theoretic model of migration timing for RSA-2048. We adopt a two-hypothesis mixture: under hypothesis $H_{\mathrm{BPP}}$ a cryptographically relevant breakthrough arrives with annual hazard $h_{\mathrm{BPP}} = 0.10$; under $H_{\mathrm{HARD}}$ the hazard is $h_{\mathrm{HARD}} = 0.01$; the prior weight is $\pi = \Pr(H_{\mathrm{BPP}})$. With migration cost normalized to $C_m = 1$, breach loss $L$, and discount rate $r = 0.05$, we derive a closed-form loss threshold $L^{\ast}(\pi) = 1 + r/\bar{h}$ above which immediate migration is optimal, where $\bar{h}$ is the mixture hazard. At the baseline $\pi = 0.2$ the mixed hazard is $\bar{h} = 0.028$ and $L^{\ast} \approx 2.785714$: any asset whose compromise costs more than $2.79$ migration-cost units justifies migrating immediately. Sensitivity analysis shows the immediate-migration region is robust: for $L = 10$ even $\pi = 0$ triggers immediate migration, while for $L = 2$ the prior must exceed $\pi^{\ast} \approx 0.444444$. Two alternative parameterizations — a discrete two-point scenario and a continuous two-hazard Poisson model with numerically solved optimal timing — are reported as labeled scenarios. The framework converts an unproven conjecture into an auditable sensitivity parameter.

## 1. Introduction

The deployment of post-quantum cryptography is one of the largest planned cryptographic transitions, and its urgency is almost always argued from the anticipated capability of quantum computers to factor integers in polynomial time via Shor's algorithm. But the security relevance of that argument depends on a logical structure that is rarely made explicit: quantum factoring threatens RSA-2048 only if classical polynomial-time factoring is impossible, i.e., only if FACTORING $\notin$ BPP, where BPP is the class of decision problems solvable in bounded-error probabilistic polynomial time. If a classical algorithm ever factored RSA-2048 efficiently, quantum computers would be irrelevant to the RSA threat; if factoring is hard classically, the quantum threat is real but its arrival time is governed by engineering timelines. The conjecture FACTORING $\notin$ BPP is unproven. Migration policy therefore conditions on a conjecture, and the rational response to conditioning on an unproven proposition is to treat one's confidence in it as a prior and propagate it through the decision.

This paper does exactly that. We construct a minimal decision-theoretic model in which the probability mass assigned to a fast-breakthrough regime is a first-class parameter $\pi$, and we compute migration recommendations for RSA-2048 assets as a function of $\pi$, the breach loss $L$, the migration cost $C_m$, and the discount rate $r$. The model is deliberately simple — two hypotheses, constant hazards, exponential discounting — because its purpose is not forecasting but exposing the sensitivity structure: which conclusions about migration timing survive, and which collapse, when the epistemic status of the hardness conjecture is made explicit.

Our contributions are:

1. A closed-form Bayesian decision model for PQC migration under a two-hypothesis mixture over factoring hardness (Section 3).
2. Full arithmetic derivations of the mixed hazard, the expected discounted loss of remaining exposed, and the critical loss threshold $L^{\ast}(\pi)$ (Section 4).
3. A sensitivity analysis over the prior $\pi$ showing that for high-value assets the "migrate now" recommendation is robust even at $\pi = 0$, while for low-value assets the decision flips at a computable prior threshold $\pi^{\ast}$ (Sections 4 and 5).
4. Two labeled alternative scenarios, reconciled from independent draft parameterizations: a discrete two-point cost scenario and a continuous two-hazard Poisson model in which the optimal migration time $T^{\ast}$ solves a first-order condition numerically (Sections 3.4 and 4.4).
5. A discussion of how much of the quantum-advantage narrative for cryptography depends on the single unproven premise FACTORING $\notin$ BPP, and of a proposed stress-test program classifying known exponential speedups by their dependence on abelian hidden-subgroup structure (Section 6).

Throughout, every number is either an input declared in Section 3 or computed with shown arithmetic in Section 4. No empirical data on expert surveys or engineering timelines are invented; where such data would refine the inputs, we say so explicitly.

## 2. Background and Related Work

We organize the related work into three threads: the PQC migration problem itself, Bayesian methods for priors and expert judgement, and analogues of migration, hardness, and displacement modeling in adjacent fields. Every statement below is restricted to what the supplied bibliography entry supports; where an entry's summary is thin, we say so.

**PQC migration management.** The most directly relevant work is the PMMP framework of [2], which addresses the problem that organizations must plan migration to quantum-resilient cryptographic measures (PQC), notes that this is difficult, and states that — to the authors' knowledge — no generalized approach existed that manages such a complex migration while explicitly integrating into organizations' steering mechanisms and control systems; PMMP presents a risk-based process for this purpose. Our model is complementary to [2] in a specific sense: PMMP supplies the organizational process through which a migration decision is executed, while we supply the decision-theoretic core that determines *when* the migration should occur, conditional on an explicit prior over the hardness conjecture. A risk-based process needs a quantified risk; Sections 3–5 provide one candidate quantification whose inputs are auditable.

**Hardness under restrictions.** Work on computational hardness under severe restrictions offers a cautionary analogy. The Tetris analysis of [1] proves that Tetris clearing and survival remain NP-hard even when the piece set is restricted to a single tetromino type, for every tetromino type except the O piece. The structural lesson we import is twofold: first, hardness claims can be established rigorously for restricted problem variants, so "hardness" is a property that can be pinned down rather than asserted; second, the result of [1] is a *worst-case* NP-hardness statement about a puzzle, whereas cryptographic security needs *average-case* hardness against natural distributions — a gap that is exactly why the RSA-2048 threat ultimately rests on the unproven average-case conjecture FACTORING $\notin$ BPP rather than on any worst-case theorem.

**Bayesian priors, mixtures, and expert judgement.** Our two-hypothesis prior over factoring hardness is a spike-and-slab-style mixture: a point mass on "breakthrough regime" and a diffuse mass on "hard regime." The Bayesian group lasso work of [5] revisits the Bayesian group lasso using spike-and-slab priors for group variable selection, demonstrates the connection of the model with penalized regression, and shows the posterior median estimator has the oracle property under orthogonal designs. We borrow the structural idea — a two-component prior in which one component is a point mass — and apply it to a hypothesis rather than a coefficient. On the question of where the prior $\pi$ should come from, the Posterior Belief Assessment framework of [7] addresses precisely the situation in which a Bayesian analysis is too complex to assert a precise correspondence between expert probabilistic judgements and the chosen prior and likelihood, and proposes a finite procedure for attributing meaning to the results of such an analysis; this is the natural methodological home for eliciting $\pi$ from complexity-theory experts, though we do not perform such an elicitation here. On the choice of prior form itself, the objective Bayesian analysis of bilateral data in [8] derives Jeffreys' prior and Bernardo's reference prior for the risk difference, the risk ratio, and the odds ratio under Dallal's model and the saturated model; the analogy is that when little is known, an objective or reference prior over the hardness hypothesis is a defensible default, and our sensitivity analysis over $\pi \in [0,1]$ is the practical substitute for committing to one. Finally, [4] develops Bayesian inference for design-based sampling with inverse-probability weights, using a hierarchical approach that models the distribution of the weights of nonsampled units and includes them as predictors in a nonparametric model. This is relevant to a future refinement of our model in which expert survey opinions are reweighted for selection effects before being pooled into $\pi$; the supplied summary of [4] supports the general point that Bayesian inference under informative weighting requires explicit modeling of the weights, and gives no further detail we rely on.

**Migration and displacement analogues.** The Migration Networks chapter of [3] reviews the study of macroscale migration patterns as networks whose nodes represent places (countries, cities, rural areas) and whose edges encode migration ties, surveying network-analysis methods applied to such networks. We borrow the framing, not the content: cryptographic migration can be viewed as a flow problem over an asset graph, in which "migration pressure" propagates from broken primitives through dependent protocols and systems. The entry supports only this general description of network-based migration analysis, and we make no claim about its specific findings. The co-design study of [6] addresses performance analysis of migrating tasks from software to hardware in multiprocessor systems-on-chip, motivated by the complexity of multimedia applications and deadline pressure on designers; the supplied summary truncates before giving quantitative results we could use. Its relevance is the shared structural problem — deciding *when* to move a function between implementation substrates under cost and deadline pressure — which is isomorphic to our migration-timing problem with the roles of "hardware" and "PQC" interchanged.

**Default parameters made explicit.** Two entries supply methodological siblings for our central move of turning an inherited default into a decision variable. The radix study of [9] examines hierarchical (ultrametric) representations organizing $N$ items in a $q$-ary tree of depth $n = \lceil \ln N / \ln q \rceil$, in which the branching factor $q$ determines how storage, interconnection, and traversal resources scale, and notes that prior modeling treated the radix as a fixed inherited structural parameter. Prior PQC planning similarly treats "the quantum threat is real" as a fixed inherited parameter; our contribution is to make that parameter a choice variable of the model, exactly as [9] does for $q$. The non-Archimedean geometry assessment of [10] observes that the real numbers are the default continuum for physical modeling — quantum states live in Hilbert space over $\mathbb{C}$, neural networks optimize over $\mathbb{R}^n$, codes are designed with Euclidean distance — while Ostrowski's theorem demonstrates that alternative completions exist; it is a structured assessment of a thesis whose adoption hinges on a foundational comparison. Both papers ask when a community should abandon a default foundation (the reals; classical hardness) given that the alternative is mathematically coherent but practically unproven. The negotiation study of [11] examines an agentic buyer with a hard fulfillment deadline who can fork a procurement negotiation into parallel seller-facing threads, where each thread consumes resources and each simultaneous acceptance creates cancellation and commitment liability; the structural analogy is to migration scheduling under a hard deadline: early migration consumes resources now, deferred migration creates liability exposure later, and the planner must jointly choose timing and intensity of commitment. Finally, [12] belongs to the popular-facing genre in which quantum-urgency narratives circulate; its supplied summary gives no substantive text beyond its title, so we draw no technical claim from it.

Together these twelve works supply the process layer [2], the epistemology of hardness claims [1], the prior-elicitation machinery [4], [5], [7], [8], and a family of structural analogues [3], [6], [9], [10], [11], [12] for the model we now build.

## 3. Methods

### 3.1 Model primitives (main model)

Time is measured in years. The organization holds RSA-2048 assets whose compromise would cause loss $L$, expressed in units of the migration cost $C_m$ (so $C_m = 1$ by normalization). The discount rate is $r$ per year. The hardness conjecture is represented by a two-hypothesis mixture:

- $H_{\mathrm{BPP}}$: the world is in a regime where cryptographically relevant factoring breakthroughs arrive with annual hazard $h_{\mathrm{BPP}}$;
- $H_{\mathrm{HARD}}$: breakthroughs arrive with annual hazard $h_{\mathrm{HARD}} \ll h_{\mathrm{BPP}}$;
- $\pi = \Pr(H_{\mathrm{BPP}})$ is the Bayesian prior weight on the fast-breakthrough regime.

The mixture (predictive) hazard is

$$
\bar{h}(\pi) = \pi\, h_{\mathrm{BPP}} + (1 - \pi)\, h_{\mathrm{HARD}}.
$$

A breakthrough is modeled as a memoryless Poisson event: conditional on the regime, the waiting time to breakthrough is exponential with the regime's hazard. The prior $\pi$ is the Bayesian object of interest: it is not a physical constant but a posterior summary of the community's belief that the fast-breakthrough regime obtains. We treat $\pi$ as an input with a full sensitivity range $[0,1]$ rather than a point estimate, and we recommend eliciting it via the finite procedure of Posterior Belief Assessment described in [7], which is designed for exactly the case where the correspondence between expert judgements and prior forms cannot be asserted precisely. Where expert opinion is sparse, an objective-prior construction in the spirit of Jeffreys or reference priors [8] is an alternative we leave open.

### 3.2 Expected discounted loss of remaining exposed

If the organization never migrates proactively and a breakthrough arrives at time $t$, it suffers the loss $L$ at $t$, discounted to present value by $e^{-rt}$. Averaging over the exponential waiting time under the mixture hazard $\bar{h}$:

$$
E_{\mathrm{exposed}} = \int_0^{\infty} L\, \bar{h}\, e^{-\bar{h} t}\, e^{-rt}\, dt = L\, \bar{h} \int_0^{\infty} e^{-(\bar{h} + r)t}\, dt = \frac{L\, \bar{h}}{\bar{h} + r}.
$$

Immediate migration costs $C_m = 1$ at $t = 0$ and eliminates the exposure. Immediate migration is optimal exactly when

$$
1 < \frac{L\, \bar{h}}{\bar{h} + r}
\quad \Longleftrightarrow \quad
L > L^{\ast}(\pi) = \frac{\bar{h} + r}{\bar{h}} = 1 + \frac{r}{\bar{h}}.
$$

The threshold $L^{\ast}(\pi)$ is the paper's central closed-form result: it is decreasing in $\pi$, and as $\pi \to 1$ it approaches $1 + r/h_{\mathrm{BPP}}$, while as $\pi \to 0$ it approaches $1 + r/h_{\mathrm{HARD}}$.

### 3.3 Prior threshold for a given asset value

Inverting the threshold for a given $L$: immediate migration is optimal iff $\bar{h}(\pi) > r/(L - 1)$ (for $L > 1$; for $L \le 1$ migration is never immediately worthwhile under this criterion). Since $\bar{h}(\pi) = h_{\mathrm{HARD}} + \pi (h_{\mathrm{BPP}} - h_{\mathrm{HARD}})$, the critical prior is

$$
\pi^{\ast}(L) = \frac{\dfrac{r}{L-1} - h_{\mathrm{HARD}}}{h_{\mathrm{BPP}} - h_{\mathrm{HARD}}}.
$$

### 3.4 Alternative scenario models (reconciled from independent parameterizations)

Two further parameterizations are reported as labeled scenarios in Section 4.4, with their own declared inputs and shown arithmetic.

**Scenario D (discrete two-point).** A single horizon $T$, a prior $p$ of a breakthrough within the horizon, migration cost $C_m$ paid at $t=0$ if migrating immediately, breach cost $C_b$ discounted by $d = e^{-rT}$ if the organization waits. The expected cost of waiting until the horizon is $E_{\mathrm{wait}} = p\, C_b\, d + (1-p)\, C_m$, and the break-even prior under the simplified comparison (migration forced at $T$) is $p^{\ast} = C_m / (C_b\, d)$.

**Scenario P (continuous two-hazard Poisson).** A classical breakthrough arrives with hazard $\lambda$ and a quantum capability with independent hazard $\mu$; combined hazard $\Lambda = \lambda + \mu$. Migration at time $T$ costs $C_m$ (discounted); if a breakthrough of either type occurs at $t < T$, loss accrues at rate $L$ per year until $T$. The expected discounted cost is

$$
E[C](T) = C_m e^{-rT} + L\,\Lambda \int_0^T e^{-\Lambda t}\,(T-t)\,e^{-rt}\,dt,
$$

and with $a = \Lambda + r$ the first-order condition for the optimal migration time $T^{\ast}$ is

$$
r\,C_m e^{-rT^{\ast}} = \frac{L\,\Lambda}{a}\left(1 - e^{-aT^{\ast}}\right),
$$

solved numerically by bisection in Section 4.4. Scenario P makes the counterfactual structure explicit: the quantum-only literature implicitly sets $\lambda = 0$, so all urgency flows from hardware; our model adds the classical-hazard term that the purely quantum framing omits.

### 3.5 The reduction-of-urgency argument

The entire quantum-advantage case for RSA-2048 urgency reduces to the single unproven premise FACTORING $\notin$ BPP: if the premise fails, quantum hardware is irrelevant to RSA. A companion structural question — what fraction of known exponential speedups depend on abelian hidden-subgroup structure, of which factoring is the flagship instance — is a classification problem we flag as a labeled stress-test hypothesis in Section 6, not as a computed result.

## 4. Analysis

Every input number below is stated with its source: all monetary and rate parameters are *modeling assumptions of this paper* (declared here, not measured), and all outputs are computed from them by the arithmetic shown.

### 4.1 Main model: mixture hazard and loss threshold

**Inputs (assumptions of this paper).** $h_{\mathrm{BPP}} = 0.10$ per year; $h_{\mathrm{HARD}} = 0.01$ per year; $\pi = 0.2$; $r = 0.05$ per year; $C_m = 1$ (normalization).

**Step 1: mixture hazard.**

$$
\bar{h} = \pi h_{\mathrm{BPP}} + (1-\pi) h_{\mathrm{HARD}} = 0.2 \times 0.10 + 0.8 \times 0.01 = 0.020 + 0.008 = 0.028.
$$

**Step 2: expected discounted loss of remaining exposed, for $L = 10$.**

$$
E_{\mathrm{exposed}} = \frac{L\,\bar{h}}{\bar{h} + r} = \frac{10 \times 0.028}{0.028 + 0.05} = \frac{0.28}{0.078} \approx 3.589744.
$$

Since $E_{\mathrm{exposed}} \approx 3.59 > C_m = 1$, immediate migration is optimal at the baseline for a ten-unit asset.

**Step 3: loss threshold.**

$$
L^{\ast}(\pi) = 1 + \frac{r}{\bar{h}} = 1 + \frac{0.05}{0.028} = 1 + 1.785714\ldots \approx 2.785714.
$$

(Here $0.05/0.028 = 50/28 = 25/14 = 1.785714\ldots$) Any asset with $L > 2.785714$ migration-cost units justifies immediate migration at $\pi = 0.2$.

**Step 4: sensitivity in $\pi$.**

- $\pi = 0$: $\bar{h} = 0.01$, so $L^{\ast} = 1 + 0.05/0.01 = 1 + 5 = 6$. An asset with $L = 10 > 6$ still triggers immediate migration even if the fast-breakthrough regime has zero prior weight — the recommendation is robust to the conjecture entirely failing to be doubted.
- $\pi = 1$: $\bar{h} = 0.10$, so $L^{\ast} = 1 + 0.05/0.10 = 1.5$.

**Step 5: critical prior for a low-value asset, $L = 2$.** Required mixture hazard:

$$
\bar{h}^{\mathrm{req}} = \frac{r}{L - 1} = \frac{0.05}{2 - 1} = 0.05.
$$

Solve $0.01 + 0.09\,\pi = 0.05$:

$$
\pi^{\ast} = \frac{0.05 - 0.01}{0.09} = \frac{0.04}{0.09} = 0.444444\ldots
$$

For a two-unit asset, the fast-breakthrough regime must carry more than a $44.44\%$ prior before immediate migration beats waiting.

### 4.2 Scenario D (discrete two-point): full arithmetic

**Inputs (assumptions of this paper, in dollars).** $p = 0.05$ (prior probability of a breakthrough within the horizon); $C_m = \text{\$}10{,}000{,}000$; $C_b = \text{\$}200{,}000{,}000$; $r = 0.05$ per year (continuous); $T = 10$ years.

**Step 1: discount factor.** $d = e^{-rT} = e^{-0.05 \times 10} = e^{-0.5} \approx 0.606531$.

**Step 2: expected discounted breach cost when waiting.**

$$
p\, C_b\, d = 0.05 \times 200{,}000{,}000 \times 0.606531 = 10{,}000{,}000 \times 0.606531 \approx \text{\$}6{,}065{,}310.
$$

**Step 3: expected total cost of waiting.**

$$
E_{\mathrm{wait}} = p\, C_b\, d + (1-p)\, C_m = 6{,}065{,}310 + 0.95 \times 10{,}000{,}000 = 6{,}065{,}310 + 9{,}500{,}000 = \$15{,}565{,}310.
$$

Since $C_m = \text{\$}10{,}000{,}000 < E_{\mathrm{wait}} \approx \text{\$}15.57$ million, immediate migration is optimal under Scenario D's baseline.

**Step 4: break-even prior (simplified comparison with migration forced at $T$).**

$$
C_b\, d = 200{,}000{,}000 \times 0.606531 \approx \$121{,}306{,}200,
\qquad
p

## References

[1] Tetris is Hard with Just One Piece Type. arXiv:2603.09958v1. https://arxiv.org/abs/2603.09958v1
[2] PMMP -- PQC Migration Management Process. arXiv:2301.04491v4. https://arxiv.org/abs/2301.04491v4
[3] Migration Networks: Applications of Network Analysis to Macroscale Migration Patterns. arXiv:2002.10992v2. https://arxiv.org/abs/2002.10992v2
[4] Bayesian Nonparametric Weighted Sampling Inference. arXiv:1309.1799v4. https://arxiv.org/abs/1309.1799v4
[5] Bayesian Variable Selection and Estimation for Group Lasso. arXiv:1512.01013v1. https://arxiv.org/abs/1512.01013v1
[6] Performance Analysis of Software to Hardware Task Migration in Codesign. arXiv:1002.1154v1. https://arxiv.org/abs/1002.1154v1
[7] Posterior Belief Assessment: Extracting Meaningful Subjective Judgements from Bayesian Analyses with Complex Statistical Models. arXiv:1512.00969v1. https://arxiv.org/abs/1512.00969v1
[8] Objective Bayesian Inference for Bilateral Data. arXiv:1504.06523v1. https://arxiv.org/abs/1504.06523v1
[9] QNFO: Optimal Radix q under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies
[10] QNFO: When Will Non-Archimedean Geometry Displace the Real Numbers? A Structured Assessment of the Adelic Substrate Thesis
[11] QNFO: Parallelism or Concession? A Reconciled Analytical Model of Concurrency-Aware Procurement Negotiation for Agentic Commerce
[12] QNFO: The Revolutionary Beginner's Guide to Quantum Computing: Why We Don't Have Quantum Computers Yet â€” and What the Geometric Alternative Offers

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2603.09958v1 | Tetris is Hard with Just One Piece Type
arXiv:2002.10992v2 | Migration Networks: Applications of Network Analysis to Macroscale Migration Patterns
arXiv:1309.1799v4 | Bayesian Nonparametric Weighted Sampling Inference
arXiv:1512.01013v1 | Bayesian Variable Selection and Estimation for Group Lasso
arXiv:1002.1154v1 | Performance Analysis of Software to Hardware Task Migration in Codesign
arXiv:1512.00969v1 | Posterior Belief Assessment: Extracting Meaningful Subjective Judgements from Bayesian Analyses with Complex Statistical Models
arXiv:1504.06523v1 | Objective Bayesian Inference for Bilateral Data

## QNFO corpus context (Vectorize)

QNFO: Factoring Hardness as a Bayesian Prior: A Decision-Theoretic Model of Post-Quantum Cryptography Migration Timing | https://papers.qnfo.org/papers/factoring-hardness-as-a-bayesian-prior-a-decision-theoretic-model-of-post-quantu

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2603.09958v1 | Tetris is Hard with Just One Piece Type
  We analyze the computational complexity of Tetris clearing (determining whether the player can clear an initial board using a given sequence of pieces) and survival (determining whether the player can avoid losing before placing all the given pieces in an initial board) when restricted to a single polyomino piece type. We prove, for any tetromino piece type $P$ except for O, the NP-hardness of Tet
  Full text (https://arxiv.org/html/2603.09958v1), excerpts of its own sections:
  § 1 Introduction: Tetris is one of the oldest and most popular puzzle video games, originally created by Alexey Pajitnov in 1984. Tetris has reached mainstream media many times, most recently in the biopic Tetris [ 14 ] and with the news of 16-year-old Michael Artiaga being the first person to go through all 255 levels of the NES version of Tetris [ 10 ] . In the base version of Tetris, a player is given a rectangular grid of unit-square cells ( squares ). [...]
  § 1.1 Our Results: In this paper, we analyze Tetris clearing and survival under the restriction that the input sequence contains exactly one polyomino piece type, resolving open problems posed in previous Tetris papers [ 4 , 6 , 12 ] . On the positive side, we give polynomial-time algorithms for Tetris clearing and survival when the input sequence consists of only dominoes. These results assume a particularly simple falling rotation model for dominoes, where pieces move monotonically downward; we leave open the complexity for other rotation models. The clearing result also only applies to infinite (or sufficiently long) sequences of dominoes. Other than these catches, our results solve two of the three remaining open problems posed in [ 6 ] regarding $n$ -tris for various $n$ . (The only remaining open problem is surviving a sequence of unrotatable dominoes.) Key subroutines we develop are strategies for both clearing and survival using only $1\times k$ pieces, for any fixed $k$ , provided the top $k-1$ rows of the board are empty. [...]
  § 1.2 Outline: The structure of the rest of the paper is as follows. Section 2 details the rotation systems being considered in our paper, including the Super Rotation System (SRS) for tetrominoes and our falling rotation model for dominoes. Section 3 discusses our positive results regarding Tetris survival and clearing with $1\times k$ pieces. Section 4 describes the 1-in-3SAT and Graph Orientation problems, which our hardness proofs reduce from. Section 5 describes our hardness result for Tetris clearing with SRS with only pieces, along with how the hardness result can be modified to get NP-hardness for Tetris clearing if the sequence of pieces has to be able to be generated from a 7-bag randomizer or a $7k$ -bag randomizer for $k>1$ . Section 6 describes our hardness result for Tetris clearing with SRS with only pieces or with only pieces, Section 7 describes our hardness result for Tetris clearing with SRS with only pieces, and Section 8 describes our hardness result for Tetris clearing with SRS with only pieces or with only pieces. [...]
  § 2.1 Super Rotation System (SRS): For our hardness results involving tetrominoes, we assume the standard Super Rotation System (SRS) [ 17 ] . Each piece has a defined rotation center , as indicated by dots in Figure 1 , except for and , whose rotation centers are the centers of the $4\times 4$ squares in Figure 1 . When unobstructed, all non- tetrominoes will rotate purely about the rotation center (note that pieces cannot rotate). The key feature about SRS is kicking : if a tetromino is obstructed when a rotation is attempted, the game will attempt to “kick” the tetromino into one of four alternate positions, each tested sequentially; if all four positions do not work, then the rotation will fail. See Figure 2 for an example of this kicking process. The full data for wall kicks can be found in Tables 1 and 2 , and at [ 17 ] ; a visualization of the locations of the tests in relation to the piece can be found in Figure 44 . [...]
[2] arXiv:2002.10992v2 | Migration Networks: Applications of Network Analysis to Macroscale Migration Patterns
  An emerging area of research is the study of macroscale migration patterns as a network of nodes that represent places (e.g., countries, cities, and rural areas) and edges that encode migration ties that connect those places. In this chapter, we first review advances in the study of migration networks and recent work that has employed network analysis to examine such networks at different geograph
  Full text (https://ar5iv.labs.arxiv.org/html/2002.10992v2), excerpts of its own sections:
  § Submission history: From: Mason A. Porter [ view email ] [v1] Tue, 25 Feb 2020 16:04:16 UTC (468 KB) [v2] Tue, 26 May 2020 22:51:51 UTC (575 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Migration Networks: Applications of Network Analysis to Macroscale Migration Patterns, by Valentin Danchev and Mason A. Porter View PDF view license
  § Current browse context:: cs.SI < prev | next > new | recent | 2020-02 Change to browse by: cs nlin nlin.AO physics physics.soc-ph
  § DBLP - CS Bibliography: listing | bibtex Valentin Danchev Mason A. Porter Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[3] arXiv:1309.1799v4 | Bayesian Nonparametric Weighted Sampling Inference
  It has historically been a challenge to perform Bayesian inference in a design-based survey context. The present paper develops a Bayesian model for sampling inference in the presence of inverse-probability weights. We use a hierarchical approach in which we model the distribution of the weights of the nonsampled units in the population and simultaneously include them as predictors in a nonparamet
  Full text (https://arxiv.org/html/1309.1799v4), excerpts of its own sections:
  § 1.1 The problem: Survey weighting adjusts for known or expected differences between sample and population. These differences arise from sampling design, undercoverage, nonresponse, and limited sample size in subpopulations of interest. Weights are constructed based on design or benchmarking calibration variables that are predictors of inclusion probability $\pi_{i}$ , defined as the probability that unit $i$ will be included in the sample, where inclusion refers to both selection into the sample and response given selection. However, weights have problems. As pointed out by Gelman (2007) and the associated discussions, current approaches for construction of weights are not systematic, with much judgment required on which variables to include in weighting, which interactions to consider, and whether and how weights should be trimmed. [...]
  § 1.2 Background: Consider a survey response with population values $Y_{i}$ , $i=1,\dots,N$ , with the sampled values labeled $y_{i}$ , for $i=1,\dots,n$ , where $N$ is the population size and $n$ is the sample size. Design-based inference treats $Y_{i}$ in the population as fixed and the inclusion indicators $I_{i}$ as random. Model-based survey inference builds models on $y_{i}$ and uses the model to predict the nonsampled values $Y_{i}$ . Rubin (1983) and Little (1983) point out that, to satisfy the likelihood principle, any model for survey outcomes should be conditional on all information that predicts the inclusion probabilities. If these probabilities take on discrete values, this corresponds to modeling within strata defined by the inclusion probabilities. We assume that the survey comes with weights that are proportional to the inverse of the inclusion probabilities, so that we can map the unique values of sample weights to form the strata. We call the strata poststratification cells since they are constructed based on the weights in the sample. [...]
  § 1.3 Contributions of this paper: Existing methods for the Bayesian analysis of weighted survey data, with the exception of Zangeneh and Little (2012) , assume the weights to be known for all population units, but we assume that the weights are known for the sample units only, which is more common in practice. [...]
  § 2 Bayesian model for survey data with externally-supplied weights: In the collected dataset, we observe $(w_{j[i]},y_{i})$ , for $i=1,\dots,n$ , with the weight $w_{j}$ being proportional to the inverse probability of sampling for units in cell $j$ , for $j=1,\dots,J$ , and [...]
  § 6 Discussion: We have demonstrated a nonparametric Bayesian estimation for population inference for the problem in which inverse-probability sampling weights on the observed units represent all the information that is known about the design. Our approach proceeds by estimating the weights for the nonsampled units in the population and simultaneously modeling the survey outcome given the weights as predictors using a robust Gaussian process regression model. This novel procedure captures uncertainty in the sampling as well as in the unobserved outcomes. We implement the model in Stan, a flexible Bayesian inference environment that can allow the model to be easily expanded to include additional predictors and levels of modeling, as well as alternative link functions and error distributions. In simulation studies, our fully Bayesian approach performs well compared to classical design-based inference. Partial pooling across small cells allows the Bayesian estimator to be more efficient in terms of smaller variance, smaller RMSE, and better coverage rates. [...]
[4] arXiv:1512.01013v1 | Bayesian Variable Selection and Estimation for Group Lasso
  The paper revisits the Bayesian group lasso and uses spike and slab priors for group variable selection. In the process, the connection of our model with penalized regression is demonstrated, and the role of posterior median for thresholding is pointed out. We show that the posterior median estimator has the oracle property for group variable selection and estimation under orthogonal designs, whil
  Full text (https://arxiv.org/html/1512.01013v1), excerpts of its own sections:
  § 1 Introduction: Group structures of predictors arise naturally in many statistical applications: • In a regression model, a multi-level categorical predictor is usually represented by a group of dummy variables. • In an additive model, a continuous predictor may be represented by a group of basis functions to incorporate nonlinear relationship. • Grouping structure of variables may be introduced into a model to make use of some domain specific prior knowledge. Genes in the same biological pathway, for example, form a natural group. For a thorough review of the application of group variable selection methods in statistical problems, one may refer to Huang et al. (2012) , in which semiparametric regression models, varying coefficients models, seemingly unrelated regressions and analysis of genomic data are discussed. It is usually desirable to use the prior information on the grouping structure to select variables group-wise. Depending on the application, selecting individual variables in a group may or may not be relevant. [...]
  § 2.1 Model Formulation: We consider the regression problem with grouped variables in ( 1 ). Kyung et al. (2010) demonstrated that the prior $\displaystyle\pi\left(\bm{\beta}_{g}\right)\propto\exp\left\{-\frac{\lambda}{\sigma}\|\bm{\beta}_{g}\|_{2}\right\},$ (5) a multivariate generalization of the double exponential prior, can also be expressed as a scale mixture of normals with Gamma hyperpriors. Specifically, with $\displaystyle\bm{\beta}_{g}|\tau_{g}^{2},\sigma^{2}\stackrel{{\scriptstyle ind}}{{\sim}}\bm{N}_{m_{g}}\left(\bm{0},\tau_{g}^{2}\sigma^{2}\bm{I}_{m_{g}}\right),\tau_{g}^{2}\stackrel{{\scriptstyle ind}}{{\sim}}\text{Gamma}\left(\frac{m_{g}+1}{2},\frac{\lambda^{2}}{2}\right)$ , (6) the marginal distribution of $\bm{\beta}_{g}$ is of the form ( 5 ). This Bayesian formulation encourages shrinkage of coefficients at the group level and provides comparable prediction performance with the group lasso. However, this approach, based on estimation of $\bm{\beta}_{g}(g=1,\dots,G)$ by posterior means or medians, does not produce exact 0 estimates. [...]
  § 2.2 Marginal Prior for $\bm{\beta}_{g}$ and Connection with Penalized Regression: Integrating out $\tau_{g}^{2}$ in ( 8 ) and ( 9 ), the marginal prior for $\bm{\beta}_{g}$ is a mixture of point mass at $\bm{0}\in\mathbb{R}^{m_{g}}$ and a Multi-Laplace distribution: $\displaystyle\bm{\beta}_{g}|\sigma^{2}\sim\left(1-\pi_{0}\right)\text{M-Laplace}\left(\bm{0},\frac{\sigma}{\lambda}\right)+\pi_{0}\delta_{0}\left(\bm{\beta}_{g}\right)$ , (11) where the density function for an $m_{g}$ -dimensional Multi-Laplace distribution is [...]
  § 5 Discussion: The primary goal of the group lasso is to both select groups of variables and estimate corresponding coefficients. Previous Bayesian approaches via multivariate scale mixture of normals do have shrinkage effects at the group level but do not yield sparse estimators. Spike and slab type priors facilitate variable selection by putting a point mass at 0, or in the case of group variable selection, a multivariate point mass at $\bm{0}_{m\times 1}$ for an $m$ -dimensional coefficients group. Since the posterior mean estimator still does not produce sparse estimators, two variable selection criterion were proposed. Highest posterior probability model ( Geweke, 1994 ; Kuo and Mallick, 1998 ; George and McCulloch, 1997 ) is a very popular one since via Gibbs sampling simulations we could easily obtain the model and an estimate of its corresponding posterior probability. [...]
[5] arXiv:1002.1154v1 | Performance Analysis of Software to Hardware Task Migration in Codesign
  The complexity of multimedia applications in terms of intensity of computation and heterogeneity of treated data led the designers to embark them on multiprocessor systems on chip. The complexity of these systems on one hand and the expectations of the consumers on the other hand complicate the designers job to conceive and supply strong and successful systems in the shortest deadlines. They have 
  Full text (https://ar5iv.labs.arxiv.org/html/1002.1154v1), excerpts of its own sections:
  § Submission history: From: Vishal Goyal [ view email ] [v1] Fri, 5 Feb 2010 08:51:44 UTC (505 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Performance Analysis of Software to Hardware Task Migration in Codesign, by Dorsaf Sebai and 2 other authors View PDF view license
  § Current browse context:: cs.PF < prev | next > new | recent | 2010-02 Change to browse by: cs
  § DBLP - CS Bibliography: listing | bibtex Dorsaf Sebai Abderrazak Jemai Imed Bennour Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[6] arXiv:1512.00969v1 | Posterior Belief Assessment: Extracting Meaningful Subjective Judgements from Bayesian Analyses with Complex Statistical Models
  In this paper, we are concerned with attributing meaning to the results of a Bayesian analysis for a problem which is sufficiently complex that we are unable to assert a precise correspondence between the expert probabilistic judgements of the analyst and the particular forms chosen for the prior specification and the likelihood for the analysis. In order to do this, we propose performing a finite
  Full text (https://arxiv.org/html/1512.00969v1), excerpts of its own sections:
  § 1 Introduction: The idea that uncertainty is a subjective property of individuals underlies the development of the field of Bayesian statistics ( Savage, 1977 ; Lindley, 2000 , cf.) . You are uncertain about some aspect of the world, you specify this uncertainty in the form of a prior probability distribution. You specify a probability model describing the data generating process that you will use to learn about the world and update your prior probabilities to posterior probabilities, upon observation of the data, using Bayes theorem. We term this the subjective Bayesian approach. Many aspects of a Bayesian analysis are challenging, in particular, when a prior and likelihood have been established, computing or sampling from the posterior distribution can be extremely difficult. This challenge, however, has been well met by the Bayesian field, with modern techniques in Markov Chain Monte Carlo (MCMC) allowing even the most complicated statistical models to be sampled from in order to obtain posterior probabilities ( Liang et al., 2010 , see, for example,) . [...]
  § 2 A motivating example: Throughout the paper we will discuss current judgements and alternative judgements regarding our models and specification for the prior and likelihood in complex statistical problems, and we will claim that perhaps none of these actually reflect our internal expert probabilistic judgements on the observables or any key elements of the problem for which we intend to make probabilistic inference (if such probabilistic judgements could ever exist or be obtained if they did). To motivate this discussion, we introduce an example from our own work that is sufficiently complex to illustrate these ideas and to make concrete some of our terminology. We apply our methodology to this example in Section 6 . Our example involves the calibration of a computationally expensive ocean model used to learn about the state of the real ocean. We describe the particular ocean model we are using and our experiments on it in detail in Section 6 . [...]
  § 3 Interpreting a Bayesian analysis: There are different views as to the primitive concepts underpinning the Bayesian approach to inference. In this paper, we are driven by the requirement to give a formal and operational treatment which deals with the difference between the inferences made within a traditional Bayesian model for a complex problem and the actual inferences that we are confident to assert on the basis of our modelling and analysis. [...]
  § 7 Discussion: Performing a truly subjective Bayesian analysis (where all elements of the prior modelling are held subjective beliefs, leading to a clear interpretation of the posterior distribution) in problems requiring complex statistical models, would be extremely challenging, expensive and time consuming. This would be the case even if elicitation of high-dimensional joint distributions, even for non-standard forms, was well supported and routine in Bayesian analysis. However, the case where we require posterior beliefs for every, or even very many, combinations of quantities in our statistical model is perhaps rare at best, though likely non-existent. Posterior belief assessment is a methodology that allows us to use the full Bayesian machinery in order to obtain beliefs for key quantities of interest using as many alternative forms of prior and likelihood modelling judgements as we are prepared to consider as representative of our judgements regarding the problem structure and our beliefs before undertaking the analysis. [...]
[7] arXiv:1504.06523v1 | Objective Bayesian Inference for Bilateral Data
  This paper presents three objective Bayesian methods for analyzing bilateral data under Dallal's model and the saturated model. Three parameters are of interest, namely, the risk difference, the risk ratio, and the odds ratio. We derive Jeffreys' prior and Bernardo's reference prior associated with the three parameters that characterize Dallal's model. We derive the functional forms of the posteri
  Full text (https://arxiv.org/html/1504.06523v1), excerpts of its own sections:
  § 1 Introduction: Bilateral data arise in medicine when a group of randomly chosen patients with a condition receive a new treatment, for example, surgery, on paired body parts within the same individual (eyes, ears, breasts, arms, hands, knees, legs, or feet), while another group of patients with this condition receive a control treatment, for example, the currently accepted medical treatment. The investigator records paired Bernoulli outcomes about a particular characteristic, for example, absence of the condition, that are then grouped into one of three categories. (i) The two body parts are cured, recorded as $(1,1)$ . The counts of patients with this characteristic from the control and treatment groups are denoted by $m_{20}$ and $m_{21}$ . (ii) One of the two body parts is cured while the other remains diseased, recorded as $(1,0)$ or $(0,1)$ . However, these $(1,0)$ and $(0,1)$ outcomes are thrown away and this detailed information is no longer available. Only the counts of patients from the control and treatment groups in that category, $m_{10}$ and $m_{11}$ are available. [...]
  § 2 Dallal’s Dependence Model: Dallal’s model was presented for the first time as model 2 in Dallal (1988) . Let “ $i=1$ ” and “ $i=0$ ” denote the treatment group and the control group, respectively. Denote by $Z_{ijk}$ a binary variable such that $Z_{ijk}=1$ if the $k$ th site ( $k$ th body part) of the $j$ th subject in the $i$ th treatment group is free of disease at the end of the study and 0 otherwise for $i=0,1$ , $j=1,\dots,m_{+i}$ , and $k=1,2$ . Dallal’s (reduced) model is characterized by the following assumptions: Assumption 1: $P\big(Z_{ijk}=1\big)=\lambda_{i}$ for $i=0,1$ with $0 Assumption 2: $P\big(Z_{ijk}=1\mid Z_{ij(3-k)}=1\big)=1-\gamma$ with $0 Assumption 2 states that the conditional probability of an occurrence of a particular characteristic at one site given an occurrence of that characteristic at the other site to be the same in the two treatment groups. [...]
  § 3 Bayesian Analysis: A key component in Bayesian analysis is the choice of the prior distribution. Traditionally, Bayesians have turned to conjugate priors. However, the concept of conjugate priors is only universal in standard univariate problems. In addition, when little or no prior information is available, conjugate priors become subjective. Thus, non-informative or objective priors are more widely accepted. The uniform distribution over the parameter space is an obvious non-informative prior. [...]
  § 7 Concluding Remarks: Using the parameterization $(\gamma,U,V)$ , it can be deduced that $\Delta=\dfrac{V-U}{1+\gamma}$ . This result highlights a direct dependence of the risk difference on the nuisance parameter $\gamma$ . This result also points out the main difference between the risk difference in $3\times 2$ bilateral data and the risk difference, $V-U$ , in an ordinary $2\times 2$ table where one collects a single measurement per subject. In other words, the divisor $1+\gamma$ is the term that connects the two disease risks in the bilateral data context. Indeed, according to the expression of the likelihood, $L(\gamma,U,V)$ , given in Appendix 1, the parameters $U$ and $V$ can be interpreted as the proportions of cases with one or more body part(s) cured in the placebo and treatment groups. On the opposite side, $\lambda_{0}$ and $\lambda_{1}$ are interpreted as the proportions of body parts cured in the placebo and treatment groups. So unlike $U$ and $V$ , one individual can contribute twice in the computation of $\lambda_{0}$ and $\lambda_{1}$ . [...]
[8] QNFO: Factoring Hardness as a Bayesian Prior: A Decision-Theoretic Model of Post-Quantum Cryptography Migration Timing | https://papers.qnfo.org/papers/factoring-hardness-as-a-bayesian-prior-a-decision-theoretic-model-of-post-quantu
  The urgency of post-quantum cryptography (PQC) migration is usually justified by the anticipated capability of quantum computers to factor integers, yet that threat rests on an unproven complexity-theoretic conjecture: that integer factoring is not in BPP, the class of decision problems solvable in bounded-error probabilistic polynomial time. This paper treats that conjecture as an explicit Bayesi
  Full text (https://papers.qnfo.org/papers/factoring-hardness-as-a-bayesian-prior-a-decision-theoretic-model-of-post-quantu), excerpts of its own sections:
  § 1. Introduction: The deployment of post-quantum cryptography is one of the largest planned cryptographic transitions, and its urgency is almost always argued from the anticipated capability of quantum computers to factor integers in polynomial time via Shor's algorithm. [...]
  § 3.1 Model primitives (main model): Time is measured in years. The organization holds RSA-2048 assets whose compromise would cause loss $L$, expressed in units of the migration cost $C_m$ (so $C_m = 1$ by normalization). The discount rate is $r$ per year. The hardness conjecture is represented by a two-hypothesis mixture: - $H_{\mathrm{BPP}}$: the world is in a regime where cryptographically relevant factoring breakthroughs arrive with annual hazard $h_{\mathrm{BPP}}$; - $H_{\mathrm{HARD}}$: breakthroughs arrive with annual hazard $h_{\mathrm{HARD}} \ll h_{\mathrm{BPP}}$; - $\pi = \Pr(H_{\mathrm{BPP}})$ is the Bayesian prior weight on the fast-breakthrough regime. The mixture (predictive) hazard is $$ \bar{h}(\pi) = \pi\, h_{\mathrm{BPP}} + (1 - \pi)\, h_{\mathrm{HARD}}. $$ A breakthrough is modeled as a memoryless Poisson event: conditional on the regime, the waiting time to breakthrough is exponential with the regime's hazard. The prior $\pi$ is the Bayesian object of interest: it is not a physical constant but a posterior summary of the community's belief that the fast-breakthrough regime obtains. [...]
  § 3.2 Expected discounted loss of remaining exposed: If the organization never migrates proactively and a breakthrough arrives at time $t$, it suffers the loss $L$ at $t$, discounted to present value by $e^{-rt}$. Averaging over the exponential waiting time under the mixture hazard $\bar{h}$: $$ E_{\mathrm{exposed}} = \int_0^{\infty} L\, \bar{h}\, e^{-\bar{h} t}\, e^{-rt}\, dt = L\, \bar{h} \int_0^{\infty} e^{-(\bar{h} + r)t}\, dt = \frac{L\, \bar{h}}{\bar{h} + r}. $$ Immediate migration costs $C_m = 1$ at $t = 0$ and eliminates the exposure. Immediate migration is optimal exactly when $$ 1 < \frac{L\, \bar{h}}{\bar{h} + r} \quad \Longleftrightarrow \quad L > L^{\ast}(\pi) = \frac{\bar{h} + r}{\bar{h}} = 1 + \frac{r}{\bar{h}}. $$ The threshold $L^{\ast}(\pi)$ is the paper's central closed-form result: it is decreasing in $\pi$, and as $\pi \to 1$ it approaches $1 + r/h_{\mathrm{BPP}}$, while as $\pi \to 0$ it approaches $1 + r/h_{\mathrm{HARD}}$.
  § 4.1 Main model: mixture hazard and loss threshold: **Inputs (assumptions of this paper).** $h_{\mathrm{BPP}} = 0.10$ per year; $h_{\mathrm{HARD}} = 0.01$ per year; $\pi = 0.2$; $r = 0.05$ per year; $C_m = 1$ (normalization). **Step 1: mixture hazard.** $$ \bar{h} = \pi h_{\mathrm{BPP}} + (1-\pi) h_{\mathrm{HARD}} = 0.2 \times 0.10 + 0.8 \times 0.01 = 0.020 + 0.008 = 0.028. $$ **Step 2: expected discounted loss of remaining exposed, for $L = 10$.** $$ E_{\mathrm{exposed}} = \frac{L\,\bar{h}}{\bar{h} + r} = \frac{10 \times 0.028}{0.028 + 0.05} = \frac{0.28}{0.078} \approx 3.589744. $$ Since $E_{\mathrm{exposed}} \approx 3.59 > C_m = 1$, immediate migration is optimal at the baseline for a ten-unit asset. **Step 3: loss threshold.** $$ L^{\ast}(\pi) = 1 + \frac{r}{\bar{h}} = 1 + \frac{0.05}{0.028} = 1 + 1.785714\ldots \approx 2.785714. $$ (Here $0.05/0.028 = 50/28 = 25/14 = 1.785714\ldots$) Any asset with $L > 2.785714$ migration-cost units justifies immediate migration at $\pi = 0.2$. **Step 4: sensitivity in $\pi$.** - $\pi = 0$: $\bar{h} = 0.01$, so $L^{\ast} = 1 + 0.05/0.01 = 1 + 5 = 6$. [...]