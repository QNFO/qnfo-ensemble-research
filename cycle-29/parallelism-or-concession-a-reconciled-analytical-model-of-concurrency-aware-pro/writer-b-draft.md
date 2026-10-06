# Parallelism or Concession? An Analytical Study of Concurrency-Aware Procurement Negotiation for Agentic Commerce

## Abstract

Agentic commerce systems can fork a single procurement task into many parallel seller-facing negotiation threads, but concurrency consumes resources and simultaneous agreements create cancellation and commitment risk. We study a one-unit, hard-deadline sourcing problem in which a planner jointly chooses the number of negotiators $n$ and a common price cap $p$, trading off fulfillment loss, per-thread cost, and excess-commitment cost against a product-specific acceptance curve. We rederive the structure of the Concurrency-Aware Negotiation Optimizer (CANO) proposed in recent work and extend it with closed-form comparative statics. We show that the marginal value of an additional negotiator decays geometrically at rate $(1-q)$, where $q$ is the per-thread acceptance probability, yielding an explicit stopping threshold; we prove constructively that under a convex acceptance curve, equal-success procurement requires weakly lower per-thread acceptance targets and price caps as $n$ grows; and we numerically trace how the optimal policy shifts from concession toward parallelism as excess-commitment costs fall and acceptance curves steepen. In a fully worked calibration, the optimum is two negotiators at a price cap of $100.00$ with expected cost $115.125$, and lowering the excess-commitment cost from $30.00$ to $10.00$ shifts the optimum under a steeper curve from two to three threads. The results give agentic procurement systems a transparent, auditable rule for sizing negotiation fan-out.

## 1. Introduction

An agentic buyer that receives a purchase order with a hard deadline must source one unit of a good. Large language model (LLM) agents make it mechanically trivial to open many simultaneous negotiation threads with different sellers: forking is nearly free in compute terms. Economically, however, forking is not free. Each thread consumes negotiation budget, and if several threads settle simultaneously the buyer faces excess commitments that must be cancelled, sometimes at a penalty. The planner therefore faces a genuine joint optimization: how many threads to open, and what price cap to give each.

Recent work formalized this tension in the Concurrency-Aware Negotiation Optimizer (CANO) [1], [2], establishing three structural results: geometric decay of the marginal value of negotiators, substitution of parallelism for concession under convex acceptance curves, and a dispersion comparative static under which buyers benefit from searching harder rather than offering higher prices. This paper has three goals. First, we reconstruct the model from first principles so that the structural claims are auditable without access to the original implementation. Second, we derive closed-form expressions for the concurrency threshold and the equal-success price ladder, making the substitution result fully explicit. Third, we work a complete numerical calibration — every input stated, every arithmetic step shown — and trace the policy response to changes in the excess-commitment cost and the steepness of the acceptance curve, connecting the dispersion result of [2] to concrete parameter regimes.

Our contribution is deliberately conservative: we do not claim new theorems beyond what is implicit in [1], [2], but we provide derivations, a worked calibration, and a sensitivity analysis that together turn the structural results into an operational recipe. We also probe where the recipe is fragile, and identify parameter regimes in which the "search harder, do not concede" prescription can reverse.

The remainder proceeds as follows. Section 2 situates the problem in the negotiation, agentic-commerce, and procurement literatures. Section 3 specifies the model. Section 4 contains the derivations and the full numerical calibration. Section 5 reports results. Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

The direct antecedent is the CANO model of concurrency-aware procurement negotiation [1], [2], which defines the one-unit, single-deadline sourcing problem with fulfillment loss, per-thread cost, and excess-commitment cost, proves the geometric marginal-value decay and the parallelism-for-concession substitution under convex quantile curves, and reports Monte Carlo and stress-test validation of the resulting optimizer against heuristic policies. Our paper independently reconstructs that model, derives the threshold and price-ladder formulas in closed form, and supplies a fully documented numerical calibration.

A methodological ancestor is the nonlinear-negotiation approach to complex-network optimization of [3], which recasts Wi-Fi channel assignment as a graph-coloring problem solved through negotiation-inspired dynamics. Its relevance is structural rather than economic: it demonstrates that negotiation abstractions can serve as optimization devices in engineering domains, prefiguring the use of negotiation fan-out as a controlled design parameter rather than a social ritual.

The empirical substrate for our seller model comes from the emerging literature on LLM-mediated bargaining. AgenticPay [4] provides a benchmark and simulation framework for multi-agent buyer-seller negotiation driven by natural language, modeling market structure and counterpart behavior; it supplies the motivation for treating per-thread acceptance as a stochastic, price-dependent quantity $q(p)$ rather than a deterministic reservation threshold. The solver-sampler mismatch study of [5] warns that language models asked to simulate realistic negotiators — hesitating, conceding late, settling for imperfect deals — behave very differently from models asked to find the best move. This matters directly for our calibration: the acceptance curve $q(p)$ estimated from LLM-sampler behavior may differ substantially from the curve faced by a solver-style agent, and Section 6 returns to this as a failure mode. The emotions study of [9] shows that prompt-conditioned emotional states measurably shift LLM price-negotiation outcomes, implying that $q(p)$ is not a stable product-specific object but can drift with agent configuration — a caveat for any planner that estimates the curve once and reuses it.

On the buyer side, the intra-team negotiation strategies of [8] study how a group negotiating jointly against a competitor, matcher, or conceder should coordinate internally. Our parallel threads are a mechanical, fully-coordinated special case of a negotiation team — the principal chooses a common cap, so intra-team strategic conflict is assumed away — but [8] suggests that when threads are semi-autonomous LLM agents, coordination costs beyond our per-thread cost $c$ may arise. Classical e-procurement adoption research such as [7] models organizational acceptance of electronic procurement through behavioral control, subjective norms, and perceived benefits and risks; it reminds us that the deployment environment for agentic sourcing includes institutional acceptance constraints that our deadline-and-cost model abstracts from. The procurement-crime network analysis of [6] shows that procurement ecosystems exhibit coordinated seller behavior, including shell-company structures; in our model, correlated sellers would violate the independence assumption behind the $1-(1-q)^n$ success probability, and [6] supplies the empirical reason to take that violation seriously.

Finally, from the QNFO corpus, the QuWARP cost-model assessment of workload-level reuse planning for quantum circuit simulation [10] offers a methodological analogy: like our planner, it uses an analytical cost model to size a fan-out (repeated-run workload) against resource constraints before committing compute, and its treatment of amortized per-task cost parallels our per-thread cost $c$. The Consilience Framework [11] and the pattern-based ontology work [12] are tangential to the quantitative model but inform the paper's stance that valuation and commitment structures should be derived from explicit primitives rather than inherited defaults; we cite them for completeness and note their limited direct bearing in Section 6.

## 3. Methods

**Setting.** A buyer needs one unit by a hard deadline. The planner chooses an integer concurrency level $n \in \mathbb{N}_{+}$ (number of simultaneous seller-facing negotiators) and a common price cap $p \in [p_{\min}, p_{\max}]$. Each thread independently settles at some price at or below $p$ with probability $q(p)$, the per-thread acceptance probability, where $q$ is continuous and increasing. The first settlement fulfills the order; any additional simultaneous settlement is an excess commitment.

**Costs.** Let $K$ denote the number of accepting threads. The planner incurs:

- procurement cost $p$ per accepted thread (each settlement is at the cap in the worst case; we price settlements conservatively at the cap, so expected procurement cost is $p\,\mathbb{E}[K \mid K \geq 1]$ bounded below by $p\,\Pr[K \geq 1]$ — we use the conservative cap-priced form);
- fulfillment loss $L_f > 0$ if $K = 0$ (the order is unfulfilled at deadline);
- per-thread cost $c > 0$ for each opened thread;
- excess-commitment cost $\kappa > 0$ per unit of excess, i.e., $\kappa\,(K-1)^{+}$.

**Objective.** With $q = q(p)$ and $\Pr[K = k] = \binom{n}{k} q^{k} (1-q)^{n-k}$ under seller independence, the expected cost is

$$
C(n, p) \;=\; p\,\Pr[K \geq 1] \;+\; L_f\,\Pr[K = 0] \;+\; n\,c \;+\; \kappa\,\mathbb{E}\!\left[(K-1)^{+}\right].
$$

Using $\mathbb{E}[K] = n q$ and $\mathbb{E}[(K-1)^{+}] = \mathbb{E}[K] - \Pr[K \geq 1] = n q - \bigl(1 - (1-q)^{n}\bigr)$, and writing $A_n(q) = 1 - (1-q)^{n}$ for the at-least-one-success probability,

$$
C(n, p) \;=\; L_f \;+\; n c \;+\; \bigl(p - L_f - \kappa\bigr)\, A_n(q) \;+\; \kappa\, n\, q.
$$

This is the canonical form we analyze. The planner solves $\min_{n \in \mathbb{N}_{+},\, p \in [p_{\min}, p_{\max}]} C(n,p)$.

**Acceptance curve.** We instantiate $q$ as a power quantile curve

$$
q(p) \;=\; \left(\frac{p - p_{\min}}{p_{\max} - p_{\min}}\right)^{\gamma}, \qquad \gamma > 1,
$$

which is convex on $[p_{\min}, p_{\max}]$ for $\gamma > 1$, matching the convex-quantile assumption under which [1], [2] prove the substitution result. The exponent $\gamma$ indexes curve steepness; we interpret larger $\gamma$ as greater effective price dispersion among sellers (acceptance at a given cap becomes rarer), following the dispersion comparative static of [2].

**Method of analysis.** All results are analytical derivations plus exhaustive hand-computed evaluations of $C(n,p)$ on a small grid; no simulation is performed, and every number in Section 5 is computed in Section 4.

## 4. Analysis

### 4.1 Marginal value of a negotiator and the concurrency threshold

Fix $p$, hence $q = q(p)$. Going from $n$ to $n+1$ threads changes $A_n$ by

$$
A_{n+1}(q) - A_n(q) \;=\; \bigl(1 - (1-q)^{n+1}\bigr) - \bigl(1 - (1-q)^{n}\bigr) \;=\; q\,(1-q)^{n}.
$$

Therefore

$$
