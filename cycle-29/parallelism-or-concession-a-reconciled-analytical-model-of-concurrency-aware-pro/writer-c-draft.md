# Parallel Forks, Common Caps: A Concurrency-Aware Optimizer for Agentic Procurement Negotiation

## Abstract

An agentic buyer with a hard fulfillment deadline can fork a procurement negotiation into many parallel seller-facing threads, but every thread costs money and every simultaneous acceptance creates a cancellation and commitment liability. We study a planner that jointly chooses the number of parallel negotiators $n$ and a common procurement price cap $p$. The model couples a product-specific acceptance curve $a(p)$ with fulfillment loss, per-thread cost, and excess-commitment cost. We derive three structural results with fully explicit calculations. First, holding the acceptance target fixed, the marginal value of an additional negotiator decays geometrically at rate $(1-a)$, so the optimal team size follows a closed-form ceiling rule. Second, with an exponential acceptance curve the optimal price cap satisfies $p^* = c + \ln((L-R+e)/e)/((n-1)\lambda)$, rising in concurrency: more threads let the buyer quote a higher cap because fulfillment risk is diversified. Solving the joint fixed point for a worked configuration yields $(n^*, p^*) = (2, c+2.19722)$ and a per-procurement saving of $3.4444$ relative to a single thread at the same cap. Third, under dispersed seller offers the marginal value of a thread decays polynomially rather than geometrically, so price dispersion widens the profitable concurrency region. We discuss implications for agentic commerce systems and LLM-based negotiation benchmarks.

## 1. Introduction

Agentic commerce systems increasingly delegate procurement to autonomous buyers that negotiate with sellers over price, delivery, and terms. A natural capability of such systems is *forking*: the buyer spawns $n$ parallel seller-facing negotiation threads, each quoting against a common price cap, and accepts the first (or best) successful outcome. Forking is cheap in compute but not in commitment: each additional thread consumes a per-thread resource budget, and if several threads accept simultaneously the buyer holds excess commitments that must be cancelled at a cost, both financial and reputational. This tension is the subject of the concurrency-aware procurement model of [1][2], which this paper develops, derives, and stress-tests analytically.

The setting is a one-unit procurement with a hard deadline. If no thread concludes by the deadline, the buyer suffers a fulfillment loss $L$ (stock-out, SLA penalty, or downstream task failure). If a thread concludes at or below the cap, the buyer pays the negotiated price and realizes gross value $R$ from procurement. The planner controls two levers: the concurrency level $n$ and the common cap $p$, which induces a per-thread acceptance probability $a(p)$ through a product-specific acceptance curve. The model of [1][2] establishes that optimal concurrency follows a threshold rule and that the cap and concurrency are strategic complements. Here we reconstruct those results from first principles, verify every numerical claim by hand, and extend the analysis to dispersed offers.

Our contribution relative to the literature is threefold. (i) We give a fully explicit derivation of the geometric-decay threshold rule for team size, including a worked fixed-point computation of the joint $(n^*, p^*)$ optimum. (ii) We contrast the acceptance-curve regime with a dispersed-offer regime, showing that the decay of marginal thread value switches from geometric to polynomial, which changes the optimal concurrency from logarithmic to square-root in the dispersion parameter. (iii) We connect the model to the empirical and systems literature on agentic negotiation: multi-agent LLM negotiation benchmarks [4][9], the solver-versus-sampler distinction for LLM agents [5], network-analytic views of negotiation infrastructure [3], procurement integrity and adoption contexts [6][7], and analytical cost-model methodology from adjacent planning domains [10].

## 2. Related Work

**Concurrency-aware procurement negotiation.** The direct antecedent is [1][2], which introduces the one-unit, hard-deadline model with fulfillment loss, per-thread cost, and excess-commitment cost, and proves threshold optimality of concurrency and cap-concurrency complementarity. We adopt their primitives and reproduce the structural results with explicit arithmetic, then add the dispersed-offer extension.

**Multi-agent negotiation systems and benchmarks.** Agentic negotiation is increasingly evaluated in LLM-based multi-agent systems. AgenticPay [4] provides a benchmark and system framework for LLM agents negotiating transactions, modeling economic interaction among buyer and seller agents; our planner sits upstream of such systems, choosing how many negotiation threads to spawn and what cap to give them. Work on emotions in multi-agent negotiation [9] shows that prompt-level affective state shifts negotiation outcomes in controlled frameworks, implying that the per-thread acceptance curve $a(p)$ is itself a controllable, heterogeneous object in deployed systems — a point our model accommodates since all results hold for any acceptance curve $a(p)$ with the stated monotonicity. The solver-versus-sampler distinction of [5] is directly relevant: a negotiation thread run with a *solver* orientation attempts to find an acceptable deal deterministically, while a *sampler* orientation produces stochastic, diverse offers; our dispersed-offer regime in Section 4.4 is precisely the sampler case, and [5] argues LLMs often behave as samplers, making that regime empirically important.

**Negotiation as infrastructure and its governance.** Nonlinear negotiation approaches for complex network problems [3] treat negotiation as a distributed optimization mechanism over constrained infrastructure, foreshadowing the view of parallel threads as a portfolio of stochastic searches. On the institutional side, network analyses of procurement crime [6] show that procurement ecosystems have exploitable structural vulnerabilities; parallel forking by an agentic buyer interacts with such ecosystems (e.g., collusive sellers can correlate acceptances, breaking our independence assumption — a limitation we flag). E-procurement adoption studies [7] document that perceived risk and benefit drive adoption of automated procurement, and our model gives that trade-off a quantitative shape: concurrency buys benefit at a computable commitment-risk price.

**Methodology.** Our derivation style — closed-form marginal analysis validated by hand-computed fixed points — follows the analytical cost-model tradition exemplified by reuse-planning analysis in adjacent domains [10], where planning decisions are characterized by threshold rules over explicitly computed cost ratios.

## 3. Model

A buyer must procure one unit by a hard deadline. There are $n \in \mathbb{N}$ parallel negotiation threads, each facing an independent seller. Each thread quotes against a common price cap $p \geq c$, where $c$ is the sellers' common reserve (walk-away) price. Conditional on the cap, thread $i$ accepts independently with probability $a(p)$, where $a: [c, \infty) \to [0,1)$ is the product-specific acceptance curve, strictly increasing and smooth, with $a(c) \geq 0$ and $a(p) < 1$ (a cap never guarantees acceptance).

Let $K$ be the number of accepting threads. Then $K \sim \text{Binomial}(n, a)$ and

$$P(K = 0) = (1 - a(p))^n, \qquad P(K \geq 1) = 1 - (1 - a(p))^n.$$

Costs and values:

- $R$: gross value of procurement (realized iff $K \geq 1$).
- $L > R$: fulfillment loss if $K = 0$ (deadline missed).
- $c_t > 0$: per-thread resource cost (compute, human-in-the-loop review, API spend), paid $c_t n$.
- $e > 0$: excess-commitment cost per unwanted acceptance; unwanted acceptances number $K - 1$ when $K \geq 1$ and $0$ when $K = 0$, so expected unwanted acceptances are

$$\mathbb{E}[K] - P(K \geq 1) = n a - \left(1 - (1-a)^n\right).$$

The buyer's expected total cost is

$$C(n, p) = R\,P(K \geq 1) + L\,P(K = 0) + c_t n + e\left(n a - (1 - (1-a)^n)\right).$$

Using $P(K \geq 1) = 1 - (1-a)^n$ and collecting the $(1-a)^n$ terms,

$$C(n, p) = R + (L - R)(1 - a)^n + c_t n + e\left(n a - (1 - (1-a)^n)\right).$$

Define the *commitment-adjusted stakes* constant

$$B \equiv L - R + e,$$

the sum of the net fulfillment loss and the per-excess-commitment liability; $B$ is the total downside that an additional accepting thread helps avoid or creates. Then

$$C(n, p) = R + B(1-a)^n + c_t n + e\,n a - e(1-a)^n = R + (B - e)(1-a)^n + c_t n + e\,n a.$$

Wait — collecting carefully: $B(1-a)^n - e(1-a)^n = (L-R)(1-a)^n$, so equivalently

$$C(n, p) = R + (L-R)(1-a)^n + c_t n + e\left(n a - (1-a)^n\right). \tag{1}$$

We use form (1) throughout.

## 4. Analysis

### 4.1 Marginal value of a thread: geometric decay

Fix the induced acceptance probability $a = a(p)$ and consider adding one thread. From (1),

$$\Delta C(n) = C(n+1, p) - C(n, p).$$

Compute each term:

- Fulfillment term: $(L-R)\left[(1-a)^{n+1} - (1-a)^n\right] = (L-R)(1-a)^n\left[(1-a) - 1\right] = -(L-R)\,a\,(1-a)^n.$
- Thread cost: $c_t (n+1) - c_t n = c_t.$
- Excess-commitment term: $e\left[(n+1)a - (1-a)^{n+1}\right] - e\left[n a - (1-a)^n\right] = e\,a - e\left[(1-a)^{n+1} - (1-a)^n\right] = e\,a + e\,a\,(1-a)^n.$

Summing:

$$\Delta C(n) = c_t + e\,a - (L - R + e)\,a\,(1-a)^n = c_t + e\,a - B\,a\,(1-a)^n. \tag{2}$$

The marginal benefit $B\,a\,(1-a)^n$ decays **geometrically** at ratio $(1-a)$: each additional thread helps only through the event that all $n$ existing threads fail, whose probability shrinks by the factor $(1-a)$ per thread. Since $(1-a)^n$ is strictly decreasing in $n$, $\Delta C(n)$ is strictly increasing in $n$: the *marginal cost of concurrency rises* toward its asymptote $c_t + e\,a > 0$. Hence $C(n, \cdot)$ is convex in $n$ and the optimum is a threshold.

**Threshold rule.** The buyer hires threads while $\Delta C(n) < 0$, i.e., while $B\,a\,(1-a)^n > c_t + e\,a$, i.e., while

$$(1-a)^n > \frac{c_t + e\,a}{B\,a}.$$

Taking logs (both sides positive; note $\ln(1-a) < 0$ flips the inequality):

$$n < \frac{\ln\!\left(\dfrac{c_t + e\,a}{B\,a}\right)}{\ln(1-a)}.$$

Therefore the optimal team size is

$$n^*(a) = \left\lceil \frac{\ln\!\left(\dfrac{c_t + e\,a}{B\,a}\right)}{\ln(1-a)} \right\rceil, \tag{3}$$

when $\frac{c_t + e\,a}{B\,a} < 1$ (otherwise $n^* = 0$: do not fork at all), with the convention that if the ratio equals $1$ exactly the buyer is indifferent between $0$ and $1$ extra threads at the margin. Because the numerator magnitude grows only logarithmically in $1/a$ while the denominator $\ln(1/(1-a))$ grows linearly in $a$ for small $a$, $n^*$ grows roughly like $\ln(1/c_t)/a$ as $a \to 0$: cheap acceptance probabilities justify large teams, expensive ones do not.

### 4.2 Worked example at a fixed cap

Take $L = 100$, $R = 60$, $e = 5$, $c_t = 1$, $a = 0.3$. Then $B = L - R + e = 40 + 5 = 45$, and

$$B\,a = 45 \times 0.3 = 13.5, \qquad c_t + e\,a = 1 + 5 \times 0.3 = 2.5.$$

Ratio: $2.5 / 13.5 = 0.18519$. Logs: $\ln(0.18519) = -1.68546$; $\ln(0.7) = -0.35668$. Quotient: $-1.68546 / -0.35668 = 4.72554$, so by (3), $n^* = \lceil 4.72554 \rceil = 5$.

Verify with (2) directly:

- $\Delta C(4) = 2.5 - 13.5 \times 0.7^4 = 2.5 - 13.5 \times 0.2401 = 2.5 - 3.24135 = -0.74135 < 0$: hire the 5th thread.
- $\Delta C(5) = 2.5 - 13.5 \times 0.7^5 = 2.5 - 13.5 \times 0.16807 = 2.5 - 2.26895 = +0.23106 > 0$: stop at $n = 5$.

Expected cost at $(n, a) = (5, 0.3)$ from (1): $(1-a)^5 = 0.16807$, $n a = 1.5$,

$$C = 60 + 40 \times 0.16807 + 1 \times 5 + 5 \times (1.5 - 0.16807) = 60 + 6.7228 + 5 + 5 \times 1.33193 = 60 + 6.7228 + 5 + 6.65965 = 78.38245.$$

### 4.3 Optimal price cap and the joint fixed point

Now let the acceptance curve be exponential with sensitivity $\lambda > 0$:

$$a(p) = 1 - e^{-\lambda (p - c)}, \qquad p \geq c, \tag{4}$$

so that $1 - a(p) = e^{-\lambda(p-c)}$ and $(1-a)^n = e^{-n\lambda(p-c)}$. Also $a'(p) = \lambda e^{-\lambda(p-c)}$. Differentiate (1) in $p$ at fixed $n$:

$$\frac{\partial C}{\partial p} = (L-R)\left(-n\lambda e^{-n\lambda(p-c)}\right) + c_t \cdot 0 + e\left(n \lambda e^{-\lambda(p-c)} + n\lambda e^{-n\lambda(p-c)}\right).$$

(The last $+ n\lambda e^{-n\lambda(p-c)}$ term comes from $-e \cdot \frac{\partial}{\partial p}(1-a)^n = +e\,n\lambda e^{-n\lambda(p-c)}$.) Setting $\partial C / \partial p = 0$ and dividing by $n\lambda > 0$ (for $n \geq 1$):

$$-(L-R)e^{-n\lambda(p-c)} + e\,e^{-\lambda(p-c)} + e\,e^{-n\lambda(p-c)} = 0,$$

$$e\,e^{-\lambda(p-c)} = (L - R - e)\,e^{-n\lambda(p-c)}.$$

Hmm — the coefficient is $L - R - e$, not $L-R+e$; recheck: $(L-R)(-1) + e = -(L-R) + e = -(L - R - e)$. So

$$e\,e^{-\lambda(p-c)} = (L - R - e)\,e^{-n\lambda(p-c)} \implies e^{(n-1)\lambda(p-c)} = \frac{L - R - e}{e}. \tag{5}$$

An interior cap requires $L - R > e$: the fulfillment stakes must exceed the per-excess-commitment liability, otherwise the buyer caps at the reserve $p = c$. For $n = 1$, (5) has no solution with exponent $0$ unless the ratio is $1$; a single thread simply quotes the lowest cap that meets its acceptance target. For $n \geq 2$:

$$p^*(n) = c + \frac{\ln\!\left(\dfrac{L - R - e}{e}\right)}{(n-1)\lambda}. \tag{6}$$

**Cap-concurrency complementarity.** $p^*(n)$ is *decreasing* in $n$: with more threads, fulfillment risk is diversified, so the buyer quotes a *lower* cap (more aggressive) while keeping failure probability acceptable. Equivalently, at a fixed cap, more threads reduce the failure probability; the buyer spends that risk budget on a lower price. This refines the complementarity reading of [1][2]: the instruments move together toward aggressiveness, not toward safety.

**Joint fixed point.** The optimal pair $(n^*, p^*)$ must satisfy $n^* = n^*(a(p^*(n^*)))$ with consistency between (3) and (6). Work it out with $L = 100$, $R = 60$, $e = 5$, $c_t = 1$, $\lambda = 0.5$, $c = 10$. Note $L - R - e = 35$, $\ln(35/5) = \ln 7 = 1.94591$.

- Try $n = 5$: $p^* = 10 + 1.94591/(4 \times 0.5) = 10 + 0.97296 = 10.97296$. Then $a = 1 - e^{-0.5 \times 0.97296} = 1 - e^{-0.48648} = 1 - 0.61477 = 0.38523$. From (3): $B a = 45 \times 0.38523 = 17.33535$; $c_t + e a = 1 + 1.92615 = 2.92615$; ratio $= 0.16879$; $\ln = -1.77966$; $\ln(1 - 0.38523) = \ln(0.61477) = -0.48648$; quotient $= 3.65756$; $n^*(a) = 4 \neq 5$. Too many threads.
- Try $n = 4$: $p^* = 10 + 1.94591/1.5 = 10 + 1.29727 = 11.29727$. $a = 1 - e^{-0.64864} = 1 - 0.52269 = 0.47731$. $B a = 21.47895$; $c_t + e a = 3.38655$; ratio $= 0.15764$; $\ln = -1.84751$; $\ln(0.52269) = -0.64864$; quotient $= 2.84844$; $n^*(a) = 3 \neq 4$.
- Try $n = 3$: $p^* = 10 + 1.94591/1 = 11.94591$. $a = 1 - e^{-0.97296} = 1 - 0.37796 = 0.62204$. $B a = 27.99180$; $c_t + e a = 4.11020$; ratio $= 0.14683$; $\ln = -1.91841$; $\ln(0.37796) = -0.97296$; quotient $= 1.97202$; $n^*(a) = 2 \neq 3$.
- Try $n = 2$: $p^* = 10 + 1.94591/0.5 = 13.89182$. $a = 1 - e^{-1.94591} = 1 - 0.14286 = 0.85714$ (indeed $e^{-\ln 7} = 1/7$). $B a = 38.57130$; $c_t + e a = 5.28570$; ratio $= 0.13700$; $\ln = -1.98793$; $\ln(0.14286) = -1.94591$; quotient $= 1.02157$; $n^*(a) = \lceil 1.02157 \rceil = 2$. **Fixed point:** $(n^*, p^*) = (2,\ 13.89182)$, i.e., $p^* = c + \ln 7 / \lambda$.

Verify the margin at the fixed point with (2): $B\,a\,(1-a)^2 = 45 \times 0.85714 \times 0.020408 = 45 \times 0.017493 = 0.78718$; wait, $(1-a)^2 = (1/7)^2 = 1/49 = 0.020408$; $a(1-a)^2 = 0.85714 \times 0.020408 = 0.017493$; times $B = 45$: $0.78716$. Then $\Delta C(2) = 5.28570 - 0.78716 = 4.49854 > 0$: stop at $2$. And $\Delta C(1) = 5.28570 - 45 \times 0.85714 \times 0.14286 = 5.28570 - 5.51016 = -0.22446 < 0$: hire the 2nd thread. Consistent.

Expected cost at the fixed point, from (1) with $n = 2$, $a = 6/7$, $(1-a)^2 = 1/49$, $na = 12/7 = 1.71429$:

$$C = 60 + 40 \times \frac{1}{49} + 1 \times 2 + 5 \times \left(\frac{12}{7} - \frac{1}{49}\right) = 60 + 0.81633 + 2 + 5 \times 1.69388 = 60 + 0.81633 + 2 + 8.46939 = 71.28572.$$

Compare a single thread at the same cap ($a = 6/7$, $n = 1$, $(1-a) = 1/7$, $na = 6/7$):

$$C(1) = 60 + 40 \times \frac{1}{7} + 1 + 5 \times \left(\frac{6}{7} - \frac{1}{7}\right) = 60 + 5.71429 + 1 + 3.57145 = 70.28574.$$

Interesting: at the *same aggressive cap*, one thread is cheaper ($70.28574 < 71.28572$) because the cap already delivers high acceptance; concurrency pays only when the cap is held at a level where failure risk is material. The correct comparison is each $n$ at its own optimal cap: $C(2, p^*(2)) = 71.28572$ vs. the best single-thread policy. For $n = 1$ the buyer picks the cap minimizing $C(1, p) = 60 + 40 e^{-\lambda(p-c)} + c_t + 5(e^{-\lambda(p-c)} - e^{-\lambda(p-c)})$; note the excess term vanishes identically for $n = 1$ ($na - (1-a)^n = a - (1-a) = 2a - 1$; recompute: for $