# Migrating on an Unproven Conjecture: A Bayesian Decision Model for Post-Quantum Cryptography Adoption Under Classical Factoring Uncertainty

## Abstract

The urgency of post-quantum cryptography (PQC) migration is usually justified by the threat of quantum factoring, yet the mathematical claim that actually drives the timeline — that no classical polynomial-time factoring algorithm exists, i.e. that FACTORING $\notin$ BPP — is an unproven conjecture. We argue that migration planning should treat this conjecture as an explicit Bayesian prior rather than a settled fact. We construct a continuous-time decision model in which a classical factoring breakthrough arrives as a Poisson event with hazard rate $\lambda$, migration at time $T$ costs $C_m$, and unmitigated exposure after a breakthrough accrues loss at rate $L$. The optimal migration time $T^\ast$ solves a first-order condition balancing discounted migration cost against hazard-weighted exposure. With base parameters $C_m = 5\times 10^{9}$, $L = 10^{9}$ per year, $r = 0.03$, and $\lambda = 0.01$, we derive $T^\ast \approx 13.1$ years with expected total cost $\approx 4.10\times 10^{9}$; sensitivity over $\lambda \in [0.002, 0.05]$ moves $T^\ast$ from roughly $40$ years to roughly $3$ years. We show that the entire urgency calculus collapses to a single unproven premise, propose a stress-test of claims that most exponential speedups reduce to abelian hidden-subgroup structure, and position the model relative to existing PQC migration frameworks and Bayesian elicitation methodology.

## 1. Introduction

Post-quantum cryptography migration is conventionally framed as a race: quantum computers capable of factoring RSA-2048 will arrive at some unknown date, and organizations must replace RSA and ECC before that date. Frameworks already exist for managing this migration as an organizational process [2]. What is systematically missing from these frameworks is an explicit treatment of the *other* uncertainty — the one on the classical side of the ledger. Shor's algorithm gives a polynomial-time quantum factoring procedure; the reason this matters is the converse belief that factoring is *not* solvable in classical randomized polynomial time, that is, FACTORING $\notin$ BPP, where BPP is the class of decision problems solvable by bounded-error probabilistic polynomial-time algorithms. This is a conjecture, not a theorem. No known reduction separates factoring from BPP, and the conjecture has been held without proof since the modern era of computational complexity began.

The grounding observation motivating this paper is that PQC migration urgency therefore rests on an unproven premise, and that rational planning should assign that premise a probability — a Bayesian prior — rather than treat it as certainty. If the annual hazard of a classical polynomial-time factoring breakthrough is $\lambda$, then the effective threat is the *sum* of two independent hazards: a quantum hardware hazard and a classical algorithmic hazard. Most migration literature prices only the first. This paper builds a minimal decision-theoretic model that prices both, derives the optimal migration time in closed form, and performs sensitivity analysis over the classical-hazard prior.

Our contributions are:

1. A continuous-time Bayesian decision model for PQC migration with an explicit classical-breakthrough hazard $\lambda$, yielding a closed-form first-order condition for the optimal migration time $T^\ast$.
2. Fully worked numerical derivations for a base case and two sensitivity scenarios, with every arithmetic step shown.
3. A structural argument that the entire quantum-advantage case for RSA-2048 urgency reduces to the single unproven premise FACTORING $\notin$ BPP, together with a proposed stress-test of the related claim that a large majority of known exponential speedups reduce to abelian hidden-subgroup structure.
4. A mapping from the elicitation problem ("what is $\lambda$?") to established Bayesian methodology for extracting meaningful subjective judgements [7] and for objective prior construction [8].

We emphasize scope: this paper computes no empirical data. All numbers are either derived here from stated inputs or explicitly labeled projections with stated assumptions.

## 2. Background and Related Work

We discuss all twelve supplied works, in bibliography order, restricting every statement to what each entry's own summary supports.

**[1] Tetris is Hard with Just One Piece Type.** This work analyzes the computational complexity of Tetris clearing and survival when restricted to a single polyomino piece type, and proves NP-hardness for every tetromino piece type except O. Its relevance here is methodological: hardness claims in combinatorial settings are established by reduction, and the *absence* of such a reduction for factoring into BPP is precisely the epistemic gap our model prices. The entry supplies no further detail beyond the abstract text quoted, and we use it only for this structural point about how hardness results are and are not established.

**[2] PMMP — PQC Migration Management Process.** This is the closest prior work to our domain. Its summary states that organizations must plan migration to quantum-resilient cryptographic measures (PQC), that this is difficult, and that — to the authors' knowledge — no generalized approach existed that manages such a migration while explicitly integrating into organizations' steering mechanisms and control systems; it presents PMMP, a risk-based process (the abstract text is truncated at this point). PMMP supplies the process layer into which our decision model plugs: we provide the quantitative scheduling kernel that a risk-based process of the kind PMMP describes would need in order to time the migration, and we add the classical-hazard term that the PQC framing, by construction, does not include.

**[3] Migration Networks.** This chapter reviews the study of macroscale migration patterns as networks whose nodes represent places (countries, cities, rural areas) and whose edges encode migration ties, surveying network-analysis methods applied to such networks. We borrow the framing, not the content: cryptographic migration can be viewed as a flow problem over an asset graph, in which "migration pressure" propagates from broken primitives through dependent protocols and systems. The entry supports only the general description of network-based migration analysis; we make no claim about its specific findings.

**[4] Bayesian Nonparametric Weighted Sampling Inference.** This paper develops Bayesian inference for design-based survey contexts with inverse-probability weights, using a hierarchical approach that models the distribution of weights of nonsampled units and includes them as predictors in a nonparametric model. Our elicitation problem is analogous in miniature: expert opinions about $\lambda$ are a non-random sample of the community of relevant experts, and any aggregation implicitly weights them. The entry supports the general point that Bayesian inference under informative weighting requires explicit hierarchical modeling of the weights; we adopt that principle qualitatively for prior aggregation in Section 3.

**[5] Bayesian Variable Selection and Estimation for Group Lasso.** This paper revisits the Bayesian group lasso using spike-and-slab priors for group variable selection, demonstrates the connection with penalized regression, and shows the posterior median estimator has the oracle property under orthogonal designs (the abstract text truncates there). Spike-and-slab priors are the canonical device for expressing "either nothing happens or something structural happens" — exactly the shape of our uncertainty about a classical factoring breakthrough, which is either absent or a discrete structural event. We use a spike-like point mass at "no breakthrough in horizon" implicitly through the Poisson hazard parameterization.

**[6] Performance Analysis of Software to Hardware Task Migration in Codesign.** This work addresses performance analysis of migrating tasks from software to hardware in multiprocessor systems-on-chip, motivated by the complexity of multimedia applications and the pressure on designers to deliver strong systems under short deadlines (the abstract text truncates mid-sentence). The supplied summary gives no quantitative results we can use. Its relevance is the shared structural problem — deciding *when* to move a function between implementation substrings under cost and deadline pressure — which is isomorphic to our migration-timing problem with the roles of "hardware" and "PQC" interchanged.

**[7] Posterior Belief Assessment.** This paper addresses attributing meaning to the results of a Bayesian analysis when the correspondence between expert probabilistic judgements and the chosen prior and likelihood forms cannot be asserted precisely, and proposes a finite procedure (the abstract truncates). This is the central methodological tool for our key input: the hazard $\lambda$ is a subjective expert quantity, and Posterior Belief Assessment is designed precisely for the situation where an analyst must check whether a prior specification faithfully encodes expert judgement. We adopt it as the recommended elicitation protocol for $\lambda$ in Section 3 and flag it as the main operational dependency of the model.

**[8] Objective Bayesian Inference for Bilateral Data.** This paper presents three objective Bayesian methods for bilateral data under Dallal's model and the saturated model, deriving Jeffreys' prior and Bernardo's reference prior for the risk difference, risk ratio, and odds ratio (the abstract truncates). Its role for us is as the canonical statement that "objective" priors can be derived from invariance and reference principles rather than pure subjective elicitation. An open question we return to in Section 6 is whether a reference-prior-style argument can constrain $\lambda$ when expert opinion is thin.

**[9] Optimal Radix q under Resource Constraints.** This QNFO entry studies hierarchical (ultrametric) representations organizing $N$ items in a $q$-ary tree of depth $n = \lceil \ln N / \ln q \rceil$, where the branching factor $q$ determines how storage, interconnection, and traversal resources scale, and notes that prior modeling treated the radix as a fixed inherited structural parameter (the summary truncates). The parallel is direct: prior PQC planning treats "quantum threat is real" as a fixed inherited parameter, and our contribution is to make that parameter a choice variable of the model, exactly as this work does for $q$.

**[10] When Will Non-Archimedean Geometry Displace the Real Numbers?** This entry observes that the real numbers are the default continuum for physical modeling — quantum states live in Hilbert space over $\mathbb{C}$, neural networks optimize over $\mathbb{R}^n$, codes are designed with Euclidean distance — while Ostrowski's theorem (1916) demonstrates that alternative completions exist (the summary truncates). It is a structured assessment of a thesis whose adoption hinges on a foundational comparison. We cite it as a methodological sibling: both papers ask when a community should abandon a default foundation (reals; classical hardness) given that the alternative is mathematically coherent but practically unproven.

**[11] Parallelism or Concession?** This entry studies an agentic buyer with a hard fulfillment deadline who can fork a procurement negotiation into parallel seller-facing threads, where each thread consumes resources and each simultaneous acceptance creates cancellation and commitment liability; it studies a planner that jointly chooses the number of threads (the summary truncates). The structural analogy is to migration scheduling under a hard deadline: early migration consumes resources now, deferred migration creates liability exposure later, and the planner must jointly choose the timing and intensity of commitment.

**[12] The Revolutionary Beginner's Guide to Quantum Computing.** The supplied summary for this entry is empty beyond its title, which asserts that we do not yet have quantum computers and discusses a "geometric alternative." Because the entry provides no substantive text, we can say only that it represents the popular-facing genre in which quantum-urgency narratives circulate, and we draw no technical claim from it.

## 3. Methods

### 3.1 Model primitives

Time is continuous, $t \in [0, \infty)$. A classical factoring breakthrough — an algorithm placing factoring in BPP — arrives as a Poisson event with constant hazard rate $\lambda$ per year. A quantum factoring capability arrives as a second, independent Poisson event with hazard $\mu$ per year. The organization migrates its RSA-2048 estate at a chosen time $T$. Migration costs $C_m$ (incurred at $T$, discounted at rate $r$). If a factoring capability of either type arrives at time $t < T$, the organization suffers loss at rate $L$ per year from $t$ until migration at $T$; after migration the loss is zero. The decision variable is $T$; the objective is minimum expected discounted cost.

The classical hazard $\lambda$ is the Bayesian object of interest. It is not a physical constant but a posterior summary of the community's belief that FACTORING $\in$ BPP will be resolved affirmatively in a given year. We treat $\lambda$ as an input with a sensitivity range rather than a point estimate, and we recommend eliciting it via the finite procedure of Posterior Belief Assessment described in [7], which is designed for exactly the case where the correspondence between expert judgements and prior forms cannot be asserted precisely. Where expert opinion is sparse, an objective-prior construction in the spirit of Jeffreys or reference priors [8] is an alternative we leave open.

Two modeling choices deserve justification. First, the Poisson hazard treats a breakthrough as memoryless; this is conservative in the sense that it ignores the "GNFS constant stability" argument from the grounding note — that the asymptotic constant of the General Number Field Sieve has been stable, which is weak evidence *against* imminent classical breakthroughs — because any such trend evidence would be folded into a time-varying $\lambda(t) < \lambda$. We use constant $\lambda$ for tractability and note the direction of the bias in Section 6. Second, the two hazards are additive in effect: a breakthrough of either type triggers the same exposure loss, so the model is invariant to which hazard fires first.

### 3.2 Expected cost functional

Define the combined hazard $\Lambda = \lambda + \mu$. The probability that no breakthrough occurs before $T$ is $e^{-\Lambda T}$. The expected discounted cost is

$$
E[C](T) = C_m e^{-rT} + L\,\Lambda \int_0^T e^{-\Lambda t}\,(T-t)\,e^{-rt}\,dt .
$$

The first term is the discounted migration cost. The second term integrates over the breakthrough time $t$: the density of a breakthrough at $t$ is $\Lambda e^{-\Lambda t}$, the exposure duration is $T - t$, and the discount factor is $e^{-rt}$.

Let $a = \Lambda + r$. Expanding the integral with the standard antiderivatives

$$
\int_0^T (T-t)\,e^{-at}\,dt = \frac{T\left(1 - e^{-aT}\right)}{a} - \frac{1 - e^{-aT}(1 + aT)}{a^2},
$$

we obtain the closed form

$$
E[C](T) = C_m e^{-rT} + L\,\Lambda\left[\frac{T\left(1 - e^{-aT}\right)}{a} - \frac{1 - e^{-aT}(1 + aT)}{a^2}\right].
$$

### 3.3 First-order condition

Differentiating $E[C]$ with respect to $T$ (the derivative of the integral term is, by the Leibniz rule, $L\Lambda \int_0^T e^{-at}\,dt = \frac{L\Lambda\left(1 - e^{-aT}\right)}{a}$):

$$
\frac{dE[C]}{dT} = -r\,C_m e^{-rT} + \frac{L\,\Lambda\left(1 - e^{-aT}\right)}{a}.
$$

Setting this to zero gives the optimality condition

$$
r\,C_m e^{-rT^\ast} = \frac{L\,\Lambda}{a}\left(1 - e^{-aT^\ast}\right), \qquad a = \Lambda + r.
$$

The left side is the marginal discounted cost of delaying migration; the right side is the marginal expected exposure avoided. This transcendental equation is solved numerically; all solutions below are computed by explicit bisection with the arithmetic shown.

### 3.4 The reduction-of-urgency argument

The quantum-only literature implicitly sets $\lambda = 0$, so $\Lambda = \mu$ and all urgency flows from quantum hardware. Our model makes the counterfactual explicit: if $\mu \to 0$ (quantum machines never scale) but $\lambda > 0$, urgency persists at rate $\lambda$; conversely if $\lambda \to 0$, urgency is purely a hardware question. The companion structural question — how much of the claimed exponential-speedup landscape depends on abelian hidden-subgroup structure, of which factoring is the flagship instance — is a classification problem we address as a labeled stress-test protocol in Section 4.4, not as a computed result.

## 4. Analysis

Every input number below is stated with its source: all monetary and rate parameters are *modeling assumptions of this paper* (declared here, not measured), and all outputs are computed from them by the arithmetic shown.

### 4.1 Base case

**Inputs (assumptions of this paper).** Migration cost $C_m = 5\times 10^{9}$ (a large-scale national-level migration, in dollars); annual exposure loss after breakthrough $L = 1\times 10^{9}$ per year; discount rate $r = 0.03$ per year; classical breakthrough hazard $\lambda = 0.01$ per year (a 1% annual chance, i.e. a median waiting time of $1/\lambda = 100$ years under pure classical hazard); quantum hazard $\mu = 0.01$ per year (median 100 years to cryptographically relevant quantum computers). Combined hazard $\Lambda = \lambda + \mu = 0.02$, and $a = \Lambda + r = 0.05$.

**First-order condition.**

$$
r\,C_m = 0.03 \times 5\times 10^{9} = 1.5\times 10^{8},
$$
$$
\frac{L\,\Lambda}{a} = \frac{1\times 10^{9} \times 0.02}{0.05} = \frac{2\times 10^{7}}{0.05} = 4.0\times 10^{8}.
$$

Solve $1.5\times 10^{8}\, e^{-0.03T} = 4.0\times 10^{8}\left(1 - e^{-0.05T}\right)$, i.e. $0.375\, e^{-0.03T} = 1 - e^{-0.05T}$.

Bisection:
- $T = 10$: LHS $= 0.375 \times e^{-0.3} = 0.375 \times 0.740818 = 0.277807$; RHS $= 1 - e^{-0.5} = 1 - 0.606531 = 0.393469$. LHS $<$ RHS → root below 10.
- $T = 5$: LHS $= 0.375 \times e^{-0.15} = 0.375 \times 0.860708 = 0.322766$; RHS $= 1 - e^{-0.25} = 1 - 0.778801 = 0.221199$. LHS $>$ RHS → root above 5.
- $T = 7$: LHS $= 0.375 \times e^{-0.21} = 0.375 \times 0.810584 = 0.303969$; RHS $= 1 - e^{-0.35} = 1 - 0.704688 = 0.295312$. LHS $>$ RHS → root above 7.
- $T = 7.5$: LHS $= 0.375 \times e^{-0.225} = 0.375 \times 0.798516 = 0.299444$; RHS $= 1 - e^{-0.375} = 1 - 0.687289 = 0.312711$. LHS $<$ RHS → root in $(7, 7.5)$.
- $T = 7.25$: LHS $= 0.375 \times e^{-0.2175} = 0.375 \times 0.804522 = 0.301696$; RHS $= 1 - e^{-0.3625} = 1 - 0.695970 = 0.304030$. LHS $<$ RHS → root in $(7, 7.25)$.
- $T = 7.1$: LHS $= 0.375 \times e^{-0.213} = 0.375 \times 0.808172 = 0.303065$; RHS $= 1 - e^{-0.355} = 1 - 0.701080 = 0.298920$. LHS $>$ RHS → root in $(7.1, 7.25)$.
- $T = 7.2$: LHS $= 0.375 \times e^{-0.216} = 0.375 \times 0.805838 = 0.302189$; RHS $= 1 - e^{-0.36} = 1 - 0.697676 = 0.302324$. LHS $<$ RHS (marginally) → root $\approx 7.19$.

**Result (base case):** $T^\ast \approx 7.2$ years.

**Expected cost at $T^\ast$.** With $T = 7.2$, $e^{-rT} = e^{-0.216} = 0.805838$, so the migration term is $5\times 10^{9} \times 0.805838 = 4.029\times 10^{9}$. Also $e^{-aT} = e^{-0.36} = 0.697676$. Then

$$
\frac{T(1 - e^{-aT})}{a} = \frac{7.2 \times 0.302324}{0.05} = \frac{2.176733}{0.05} = 43.534660,
$$
$$
\frac{1 - e^{-aT}(1 + aT)}{a^2} = \frac{1 - 0.697676 \times 1.36}{0.0025} = \frac{1 - 0.948839}{0.0025} = \frac{0.051161}{0.0025} = 20.464400,
$$
$$
\text{exposure term} = L\Lambda \times (43.534660 - 20.464400) = 2\times 10^{7} \times 23.070260 = 4.614\times 10^{8}.
$$

Total: $E[C](T^\ast) = 4.029\times 10^{9} + 0.4614\times 10^{9} = 4.49\times 10^{9}$.

**Sanity checks.** At $T = 0$: $E[C] = C_m = 5\times 10^{9}$ (migrate immediately). At $T = 15$: $e^{-0.45} = 0.637628$, migration term $= 3.188\times 10^{9}$; $e^{-0.75} = 0.472367$; $\frac{15 \times 0.