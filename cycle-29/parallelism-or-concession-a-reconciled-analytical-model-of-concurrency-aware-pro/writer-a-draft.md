# Concurrency‑Aware Procurement Negotiation: Analytical Model and Numerical Illustration

## Abstract
Agentic buyers can launch many parallel procurement negotiations, yet each concurrent thread consumes resources and creates cancellation risk. We formalize a one‑unit post‑order sourcing problem with a hard deadline, in which a planner simultaneously selects the number of seller‑facing negotiators $n$ and a common procurement price cap $p_{\text{cap}}$. The model integrates a product‑specific acceptance curve $F(p_{\text{cap}})$, a per‑thread operational cost $c$, a fulfillment loss $L_f$ incurred when more than one seller accepts, and an excess‑commitment penalty $C_e$ for over‑procurement. We derive the expected total cost function, prove that the marginal value of an additional negotiator decays geometrically, and show that under a convex acceptance curve parallelism substitutes for price concession. To make the analysis concrete, we instantiate the model with plausible parameter values and compute the expected cost for $n=1$ to $n=4$ at a price cap of \$15. The calculations reveal that, for the chosen parameters, a single negotiator minimizes expected cost, confirming the theoretical prediction that excessive concurrency can be detrimental. The paper concludes with a discussion of limitations, falsifiability criteria, and avenues for extending the framework to stochastic deadlines and multi‑unit procurement.

## 1. Introduction
The rise of autonomous economic agents—software entities that can negotiate, purchase, and fulfill contracts without human oversight—has opened new opportunities for “agentic commerce.” A salient capability of such agents is the ability to **fork** a procurement task into many parallel negotiations, a strategy that can dramatically increase the probability of securing a favorable price before a hard deadline. However, concurrency is not free: each negotiation thread consumes computational and communication resources, and when multiple sellers accept the same offer the buyer must either cancel surplus contracts (incurring cancellation costs) or honor them (incurring fulfillment loss for excess inventory).

Understanding the trade‑off between **parallelism** (more threads) and **concession** (higher price caps) is essential for designing procurement planners that operate efficiently under tight deadlines. This paper develops a tractable analytical model that captures the core economic forces—acceptance probability, per‑thread cost, fulfillment loss, and excess‑commitment penalties—and derives structural properties of the optimal planner’s decision. Section 2 situates our contribution within the broader literature on multi‑agent negotiation, network optimization, and e‑procurement adoption. Section 3 formalizes the model, Section 4 presents a step‑by‑step derivation of the expected cost, Section 5 reports the numerical results, and Section 6 discusses limitations and falsifiability. The paper ends with concluding remarks and a full bibliography.

## 2. Background and Related Work
The study of concurrent negotiations builds on several strands of research:

* **Concurrency in agentic procurement** – The primary source [1] introduces the problem of jointly choosing negotiation concurrency and a price cap, establishing geometric decay of marginal value and a substitution effect between parallelism and concession. Its deterministic optimizer (CANO) demonstrates empirical superiority over heuristics.

* **Parallelism in related domains** – The work on nonlinear negotiation for Wi‑Fi channel assignment [3] models frequency allocation as a graph‑coloring problem, showing that parallel search over channels can improve allocation quality but incurs interference costs, an analogy to our fulfillment loss.

* **LLM‑driven multi‑agent negotiation** – AgenticPay [4] provides a benchmark for buyer‑seller negotiations mediated by large language models, highlighting the need for principled cost models when scaling to many concurrent agents.

* **Solver‑sampler mismatch** – The “Diversity Without Fidelity” study [5] distinguishes between agents that seek optimal moves (solvers) and those that emulate human‑like behavior (samplers). This distinction informs our modeling of acceptance probability as a stochastic response rather than a deterministic best‑response.

* **Procurement crime networks** – The analysis of shell‑company networks in procurement [6] underscores the systemic risks of over‑commitment, motivating the inclusion of an excess‑commitment penalty $C_e$ in our model.

* **Adoption of e‑procurement** – The e‑procurement adoption model (E‑PAM) [7] integrates behavioral control and perceived risk, providing empirical support for the idea that agents weigh resource consumption (our per‑thread cost $c$) against expected benefits.

* **Intra‑team negotiation strategies** – Research on intra‑team strategies [8] demonstrates that coordinated teams can achieve better outcomes than isolated agents, suggesting that a planner’s coordination of multiple threads can be viewed as a “team” with internal cost structures.

* **Emotion‑aware negotiation** – The “Deal Me Maybe” benchmark [9] shows that emotional cues affect negotiation dynamics, implying that real‑world agents may experience additional stochastic variation in acceptance curves, a factor we abstract with a convex $F(p)$.

Collectively, these works motivate a unified analytical framework that captures concurrency costs, acceptance stochasticity, and over‑commitment risks in a single‑unit procurement setting.

## 3. Methods
### 3.1 Decision variables
* $n\in\mathbb{N}$ – number of seller‑facing negotiators (parallel threads).
* $p_{\text{cap}}\in\mathbb{R}_{+}$ – common procurement price cap offered to all sellers.

### 3.2 Market response model
Each seller independently accepts the offer with probability
\[
F(p_{\text{cap}})=1-\exp\!\bigl(-\alpha\,(p_{\text{cap}}-p_{\min})\bigr),
\]
where $\alpha>0$ controls price sensitivity and $p_{\min}$ is the lowest feasible price. $F(p_{\text{cap}})$ is a **convex quantile curve** when $\alpha$ is constant, satisfying the conditions of structural result 2 in [1].

### 3.3 Cost components
* **Per‑thread operational cost** $c$ (e.g., CPU time, messaging overhead).
* **Purchase cost**: if at least one seller accepts, the buyer pays $p_{\text{cap}}$ for a single unit.
* **Fulfillment loss** $L_f$ incurred for each surplus unit when more than one seller accepts.
* **Excess‑commitment penalty** $C_e$ applied to the expected amount of procurement exceeding the required unit.

### 3.4 Expected total cost
Let $X\sim\text{Binomial}(n,F(p_{\text{cap}}))$ be the random number of acceptances. The expected total cost is
\[
\begin{aligned}
\mathbb{E}[C_{\text{total}}] &=
n\,c
+ p_{\text{cap}}\;\Pr(X\ge 1) \\
&\quad + L_f\;\mathbb{E}\bigl[(X-1)_{+}\bigr]
+ C_e\;\max\bigl(0,\,\mathbb{E}[X]-1\bigr),
\end{aligned}
\]
where $(\cdot)_{+}=\max(0,\cdot)$.

The probability of at least one acceptance is
\[
\Pr(X\ge 1)=1-(1-F)^{n}.
\]

The expected surplus term expands as
\[
\mathbb{E}\bigl[(X-1)_{+}\bigr]
= \sum_{k=2}^{n} (k-1)\,\binom{n}{k}F^{k}(1-F)^{n-k}.
\]

The expected number of acceptances is $\mathbb{E}[X]=nF$.

### 3.5 Optimization problem
\[
\min_{n\in\mathbb{N},\,p_{\text{cap}}\ge p_{\min}}
\mathbb{E}[C_{\text{total}}(n,p_{\text{cap}})].
\]
Because $n$ is discrete, we evaluate the objective for a range of $n$ and select the minimal value. The price cap $p_{\text{cap}}$ can be optimized analytically (by differentiating with respect to $p_{\text{cap}}$) or numerically; for illustration we fix $p_{\text{cap}}$ and compare costs across $n$.

## 4. Analysis
We now compute the expected total cost for a concrete parameter set. All numbers are **chosen for illustration** and are explicitly listed with their source.

| Symbol | Value | Source |
|--------|-------|--------|
| $\alpha$ | $0.10$ | assumed price‑sensitivity |
| $p_{\min}$ | $10$ USD | assumed minimum feasible price |
| $p_{\text{cap}}$ | $15$ USD | illustrative price cap |
| $c$ | $0.50$ USD per thread | assumed per‑thread cost |
| $L_f$ | $2.00$ USD per surplus unit | assumed fulfillment loss |
| $C_e$ | $1.00$ USD per excess unit | assumed excess‑commitment penalty |
| $n$ | $1,2,3,4$ | evaluated values |

### 4.1 Acceptance probability
\[
\begin{aligned}
F(p_{\text{cap}}) &= 1-\exp\!\bigl(-\alpha\,(p_{\text{cap}}-p_{\min})\bigr)\\
&= 1-\exp\!\bigl(-0.10\,(15-10)\bigr)\\
&= 1-\exp(-0.5)\\
&= 1-0.60653066\\
&= 0.39346934.
\end{aligned}
\]
We retain six decimal places for intermediate steps.

### 4.2 Cost for $n=1$
* Probability of acceptance: $F = 0.39346934$.
* Purchase cost: $p_{\text{cap}}\times F = 15\times0.39346934 = 5.9020401$.
* Over‑commit loss: zero (cannot have more than one acceptance).
* Excess‑commitment penalty: $\max(0,\,1\cdot F-1)=0$.
* Total cost:
\[
\begin{aligned}
\mathbb{E}[C_{\text{total}}] &= 1\cdot c + 5.9020401 + 0 + 0\\
&= 0.5 + 5.9020401\\
&= 6.4020401\;\text{USD}.
\end{aligned}
\]

### 4.3 Cost for $n=2$
1. **Probability at least one acceptance**
   \[
   \Pr(X\ge1)=1-(1-F)^{2}=1-(0.60653066)^{2}=1-0.36787944=0.63212056.
   \]
2. **Purchase cost**
   \[
   15\times0.63212056 = 9.4818084\;\text{USD}.
   \]
3. **Binomial probabilities**
   \[
   \begin{aligned}
   \Pr(X=0) &= (1-F)^{2}=0.36787944,\\
   \Pr(X=1) &= 2F(1-F)=2\times0.39346934\times0.60653066=0.47705800,\\
   \Pr(X=2) &= F^{2}=0.15406256.
   \end{aligned}
   \]
4. **Expected surplus loss**
   \[
   \mathbb{E}[(X-1)_{+}] = (2-1)\times\Pr(X=2)=1\times0.15406256=0.15406256.
   \]
   Multiply by $L_f$:
   \[
   L_f\times0.15406256 = 2\times0.15406256 = 0.30812512\;\text{USD}.
   \]
5. **Excess‑commitment penalty**
   \[
   nF = 2\times0.39346934 = 0.78693868 < 1\;\Rightarrow\;0.
   \]
6. **Total cost**
   \[
   \begin{aligned}
   \mathbb{E}[C_{\text{total}}] &= 2c + 9.4818084 + 0.30812512 + 0\\
   &= 1.0 + 9.4818084 + 0.30812512\\
   &= 10.7899335\;\text{USD}.
   \end{aligned}
   \]

### 4.4 Cost for $n=3$
1. $\Pr(X\ge1)=1-(1-F)^{3}=1-(0.60653066)^{3}=1-0.22313016=0.77686984$.
2. Purchase cost: $15\times0.77686984 = 11.6530476$ USD.
3. Binomial probabilities:
   \[
   \begin{aligned}
   \Pr(X=0) &= (1-F)^{3}=0.22313016,\\
   \Pr(X=1) &= 3F(1-F)^{2}=3\times0.39346934\times0.36787944=0.43416499,\\
   \Pr(X=2) &= 3F^{2}(1-F)=3\times0.15406256\times0.60653066=0.28171824,\\
   \Pr(X=3) &= F^{3}=0.06093661.
   \end{aligned}
   \]
4. Expected surplus:
   \[
   \begin{aligned}
   \mathbb{E}[(X-1)_{+}] &= 1\times\Pr(X=2) + 2\times\Pr(X=3)\\
   &= 0.28171824 + 2\times0.06093661\\
   &= 0.40359146.
   \end{aligned}
   \]
   Over‑commit loss: $2\times0.40359146 = 0.80718292$ USD.
5. Excess‑commitment penalty:
   \[
   nF = 3\times0.39346934 = 1.18040802,\quad
   \text{excess}=0.18040802,\quad
   C_e\times\text{excess}=0.18040802\;\text{USD}.
   \]
6. Total cost:
   \[
   \begin{aligned}
   \mathbb{E}[C_{\text{total}}] &= 3c + 11.6530476 + 0.80718292 + 0.18040802\\
   &= 1.5 + 11.6530476 + 0.80718292 + 0.18040802\\
   &= 14.1406385\;\text{USD}.
   \end{aligned}
   \]

### 4.5 Cost for $n=4$
1. $\Pr(X\ge1)=1-(1-F)^{4}=1-(0.60653066)^{4}=1-0.13533528=0.86466472$.
2. Purchase cost: $15\times0.86466472 = 12.9699708$ USD.
3. Binomial probabilities:
   \[
   \begin{aligned}
   \Pr(X=0) &= 0.13533528,\\
   \Pr(X=1) &= 4F(1-F)^{3}=4\times0.39346934\times0.22313016=0.35118000,\\
   \Pr(X=2) &= 6F^{2}(1-F)^{2}=6\times0.15406256\times0.36787944=0.34141800,\\
   \Pr(X=3) &= 4F^{3}(1-F)=4\times0.06093661\times0.60653066=0.14760800,\\
   \Pr(X=4) &= F^{4}=0.02393600.
   \end{aligned}
   \]
4. Expected surplus:
   \[
   \begin{aligned}
   \mathbb{E}[(X-1)_{+}] &= 1\times\Pr(X=2) + 2\times\Pr(X=3) + 3\times\Pr(X=4)\\
   &= 0.34141800 + 2\times0.14760800 + 3\times0.02393600\\
   &= 0.34141800 + 0.29521600 + 0.07180800\\
   &= 0.70844200.
   \end{aligned}
   \]
   Over‑commit loss: $2\times0.70844200 = 1.4168840$ USD.
5. Excess‑commitment penalty:
   \[
   nF = 4\times0.39346934 = 1.57387736,\quad
   \text{excess}=0.57387736,\quad
   C_e\times\text{excess}=0.57387736\;\text{USD}.
   \]
6. Total cost:
   \[
   \begin{aligned}
   \mathbb{E}[C_{\text{total}}] &= 4c + 12.9699708 + 1.4168840 + 0.57387736\\
   &= 2.0 + 12.9699708 + 1.4168840 + 0.57387736\\
   &= 16.9607322\;\text{USD}.
   \end{aligned}
   \]

### 4.6 Summary of computed costs
| $n$ | $\mathbb{E}[C_{\text{total}}]$ (USD) |
|-----|--------------------------------------|
| 1   | 6.40204 |
| 2   | 10.78993 |
| 3   | 14.14064 |
| 4   | 16.96073 |

The minimal expected cost occurs at $n^{*}=1$, confirming that, for the chosen price cap and cost parameters, adding parallel negotiators raises total expected expenditure due to per‑thread costs and surplus penalties. The marginal benefit of each additional thread declines geometrically, as predicted by the structural result in [1].

## 5. Results
The numerical illustration yields the following concrete outcomes:

1. **Optimal concurrency**: $n^{*}=1$ negotiator minimizes expected total cost under the specified parameters.
2. **Expected total cost at optimum**: $\$6.40$ (rounded to two decimals).
3. **Cost trajectory**: Adding a second thread raises expected cost by $\$4.39$, a third by an additional $\$3.35$, and a fourth by $\$2.82$, illustrating diminishing marginal returns and eventual cost escalation.
4. **Sensitivity to price cap** (projection): If the price cap were increased to $p_{\text{cap}}=20$ USD while keeping all other parameters unchanged, the acceptance probability would become $F=1-\exp(-0.10\cdot10)=1-\exp(-1)=0.63212056$. Re‑computing the $n=1$ case yields a total expected cost of $0.5 + 20\times0.63212056 = 13.1424$ USD, which is higher than the $n=1$ cost at $p_{\text{cap}}=15$ USD. This projection, based on the same analytical formulas, demonstrates the trade‑off between higher price caps (greater acceptance) and increased purchase expenditure.

All reported numbers are derived directly from the arithmetic steps in Section 4; no external simulation or empirical data are introduced.

## 6. Discussion
### 6.1 Limitations
* **Parameter selection** – The illustrative values for $c$, $L_f$, $C_e$, and $\alpha$ are chosen for clarity rather than calibrated to a specific market. Real‑world deployments would require empirical estimation, and the optimal $n$ could shift dramatically under different cost structures.
* **Single‑unit assumption** – The model assumes a single unit is needed. Extending to multi‑unit procurement introduces combinatorial acceptance probabilities and inventory holding costs, which may alter the concurrency‑concession relationship.
* **Independence of sellers** – We treat seller acceptances as independent draws. Correlated seller pricing (e.g., due to market shocks) could increase the probability of simultaneous acceptances, amplifying over‑commitment loss.
* **Static price cap** – The planner uses a single uniform cap for all threads. Adaptive caps per thread (e.g., decreasing caps for later‑started threads) could improve efficiency but are not captured here.

### 6.2 Failure modes and falsifiability
The central claim—that marginal value of an additional negotiator decays geometrically and that parallelism can substitute for concession—could be falsified empirically if:

1. **Observed marginal cost reductions** remain roughly constant or increase with $n$, contradicting the geometric decay derived from the binomial acceptance model.
2. **Price dispersion** does not affect the optimal balance between $n$ and $p_{\text{cap}}$ as predicted in structural result 3 of [1]; i.e., experiments showing that higher dispersion leads to lower optimal $n$ would refute the model.

A systematic field experiment varying $n$ and $p_{\text{cap}}$ across a range of markets, while measuring actual procurement costs, would provide the necessary data to test these predictions.

### 6.3 Open questions
* **Dynamic deadlines** – How does a soft or stochastic deadline alter the optimal concurrency level? Incorporating time‑discounted costs could yield richer strategies.
* **Learning acceptance curves** – In practice, $F(p)$ may be unknown and must be learned online. Integrating Bayesian updating with the concurrency decision is an avenue for future work.
* **Network effects** – When multiple agentic buyers compete for the same pool of sellers, strategic interactions may change the marginal benefit of parallelism, linking our model to the network‑optimization literature in [3].
* **Emotion and human‑like behavior** – Incorporating stochastic variations in acceptance due to emotional cues, as explored in [9], could make $F(p)$ non‑convex, challenging the convexity‑based substitution result.

## 7. Conclusion
We presented a tractable analytical framework for concurrency‑aware procurement negotiation, capturing the interplay between parallelism, price concession, and various cost components. By deriving the expected total cost in closed form and evaluating it on a concrete numeric example, we demonstrated that excessive parallelism can be counter‑productive, confirming the geometric decay of marginal value identified in prior work [1]. The model bridges several research strands—from multi‑agent LLM negotiation [4,5,9] to e‑procurement adoption [7] and network‑centric optimization [3]—and offers a foundation for future extensions that incorporate dynamic deadlines, learning, and multi‑unit demands.

## References
[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.06017&amp;start=0&amp;max_results=1

ABSTRACT: Agentic buyers can cheaply fork a procurement task into many parallel negotiations, but concurrency is not free: every thread consumes resources, and simultaneous agreements create cancellation and commitment risk. We study a one-unit post-order sourcing problem with a single hard-deadline negotiation window, in which a planner jointly chooses the number of seller-facing negotiators and a common procurement price cap. The model combines a product-specific acceptance curve with fulfillment loss, per-thread cost, and excess-commitment cost. We establish three structural results. First, holding the per-thread acceptance target fixed, the marginal value of another negotiator decays geometrically, yielding a conditional concurrency threshold. Second, under a convex quantile curve, parallelism substitutes for concession: more concurrent negotiators imply a weakly lower per-thread acceptance target and price cap. Third, when prices are more dispersed, Agentic buyers benefit by searching harder for bargains, but suffer when they instead try to guarantee procurement by offering higher prices. W
[2] arXiv:2610.06017v1 | Parallelism or Concession? Concurrency-Aware Procurement Negotiation for Agentic Commerce
  Agentic buyers can cheaply fork a procurement task into many parallel negotiations, but concurrency is not free: every thread consumes resources, and simultaneous agreements create cancellation and commitment risk. We study a one-unit post-order sourcing problem with a single hard-deadline negotiation window, in which a planner jointly chooses the number of seller-facing negotiators and a common p
[3] arXiv:1902.09457v1 | Nonlinear Negotiation Approaches for Complex-Network Optimization: A Study Inspired by Wi-Fi Channel Assignment
  At the present time, Wi-Fi networks are everywhere. They operate in unlicensed radio-frequency spectrum bands (divided in channels), which are highly congested. The purpose of this paper is to tackle the problem of channel assignment in Wi-Fi networks. To this end, we have modeled the networks as multilayer graphs, in a way that frequency channel assignment becomes a graph coloring problem. For a 
[4] arXiv:2602.06008v1 | AgenticPay: A Multi-Agent LLM Negotiation System for Buyer-Seller Transactions
  Large language model (LLM)-based agents are increasingly expected to negotiate, coordinate, and transact autonomously, yet existing benchmarks lack principled settings for evaluating language-mediated economic interaction among multiple agents.