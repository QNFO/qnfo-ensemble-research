# Factoring Hardness as a Bayesian Prior: A Decision-Theoretic Model of Post‑Quantum Cryptography Migration Timing

## Abstract

The urgency of post‑quantum cryptography (PQC) migration is usually justified by the anticipated capability of quantum computers to factor integers, yet that threat rests on the unproven conjecture that integer factoring is not in BPP. This paper treats the conjecture as an explicit Bayesian prior and embeds it in a decision‑theoretic model for RSA‑2048 migration. The model mixes two hypotheses—fast‑breakthrough (hazard $h_{\mathrm{BPP}}$) and hard‑regime (hazard $h_{\mathrm{HARD}}$)—with prior weight $\pi$. Using the mixture hazard $\bar{h}(\pi)=\pi h_{\mathrm{BPP}}+(1-\pi)h_{\mathrm{HARD}}$, we derive a closed‑form loss threshold $L^{\ast}(\pi)=1+r/\bar{h}$ that determines when immediate migration is optimal. With baseline inputs $h_{\mathrm{BPP}}=0.10$, $h_{\mathrm{HARD}}=0.01$, $r=0.05$, and $\pi=0.20$, the mixed hazard is $\bar{h}=0.028$ and $L^{\ast}\approx2.79$. Assets with breach loss $L>2.79$ therefore merit immediate migration. Sensitivity analysis shows that for $L=10$ immediate migration is optimal even at $\pi=0$, while for $L=2$ the prior must exceed $\pi^{\ast}\approx0.44$ to trigger migration. An alternative continuous‑hazard scenario yields an optimal migration time $T^{\ast}\approx0.046$ yr (≈ 17 days) under the same numeric inputs. The framework converts an unproven complexity‑theoretic conjecture into an auditable parameter, enabling organizations to quantify the impact of epistemic uncertainty on migration timing.

## 1. Introduction

Large‑scale enterprises, government agencies, and standards bodies face the concrete problem of replacing RSA‑2048 with post‑quantum alternatives before a cryptanalytic breakthrough renders current deployments insecure. The cost of a breach—loss of confidential data, reputational damage, and regulatory penalties—can exceed billions of dollars, while premature migration incurs substantial engineering, testing, and operational expenses. Decision makers therefore need a principled method to balance breach loss against migration cost under uncertainty about the underlying hardness of integer factoring.

If integer factoring were ever solved in classical polynomial time, quantum computers would no longer pose a unique threat to RSA‑2048; the security guarantee would collapse regardless of quantum progress. Conversely, if factoring remains hard for classical algorithms, the timeline for a quantum breakthrough becomes the dominant uncertainty. The unproven conjecture FACTORING ∉ BPP therefore sits at the core of the migration urgency argument. Treating this conjecture as a fixed fact obscures the sensitivity of migration recommendations to the community’s confidence in it.

This paper addresses the “so what?” by providing a quantitative decision model that makes the conjecture an explicit Bayesian prior. The model yields a simple loss threshold that tells a planner exactly when immediate migration is justified, given any numeric loss $L$, discount rate $r$, and prior $\pi$. By varying $\pi$ the model reveals how robust the migration recommendation is to changes in belief about factoring hardness.

**Contributions**

1. A closed‑form Bayesian decision model for PQC migration under a two‑hypothesis mixture over factoring hardness (Section 3).  
2. Full arithmetic derivations of the mixed hazard, the expected discounted loss of remaining exposure, and the critical loss threshold $L^{\ast}(\pi)$ (Section 4).  
3. A sensitivity analysis over the prior $\pi$, including the critical prior $\pi^{\ast}(L)$ for low‑value assets (Sections 4 and 5).  
4. Two alternative scenarios—discrete two‑point (Scenario D) and continuous two‑hazard Poisson (Scenario P)—with complete arithmetic and a numerical solution for the optimal migration time $T^{\ast}$ (Section 4.4).  
5. A discussion of the dependence of the quantum‑advantage narrative on the single unproven premise FACTORING ∉ BPP and a proposal for a stress‑test classification of known exponential speedups (Section 6).

All numbers are either declared as modeling assumptions (Section 3) or derived with explicit arithmetic (Section 4). No empirical measurements are invented.

## 2. Background and Related Work

**PQC migration management.** The PMMP framework of [2] addresses the organizational challenge of planning migration to quantum‑resilient cryptographic measures. It notes that no generalized approach existed that integrates risk quantification into steering mechanisms. Our model supplies the quantitative risk core that determines *when* migration should occur, complementing the process described in [2].

**Hardness under restrictions.** The Tetris analysis of [1] proves NP‑hardness of Tetris clearing for every tetromino type except O, illustrating that hardness can be rigorously established for restricted variants. This informs our view that “hardness” is a property that can be pinned down rather than asserted, and highlights the gap between worst‑case NP‑hardness (as in [1]) and the average‑case hardness conjecture FACTORING ∉ BPP that underlies RSA security.

**Bayesian priors, mixtures, and expert judgement.** The Bayesian group‑lasso work of [5] introduces spike‑and‑slab priors that combine a point mass with a diffuse component. We adopt the same structural idea for a hypothesis mixture rather than a regression coefficient. The Posterior Belief Assessment framework of [7] proposes a finite procedure for attributing meaning to Bayesian analyses when expert judgements cannot be mapped precisely to prior forms; this is the methodological home for eliciting $\pi$ from complexity‑theory experts. Objective‑Bayesian analysis of bilateral data in [8] derives Jeffreys’ and reference priors for parameters with little prior information, motivating our use of a uniform sensitivity sweep over $\pi\in[0,1]$.

**Migration and displacement analogues.** The Migration Networks chapter of [3] surveys network‑analysis methods for macroscale migration, providing a framing in which cryptographic migration can be viewed as a flow over an asset graph. The co‑design study of [6] examines task migration between software and hardware under cost and deadline pressure, an isomorphic structural problem to our timing decision.

**Default parameters made explicit.** The radix study of [9] shows how a structural parameter (radix $q$) can be treated as a decision variable rather than a fixed inherited constant. Analogously, we treat the conjecture FACTORING ∉ BPP as a decision variable. The non‑Archimedean geometry assessment of [10] discusses when a community should abandon a default foundation (the real numbers) in favor of an alternative (adeles); our work mirrors this by questioning the default assumption of factoring hardness. The negotiation study of [11] models resource consumption under hard deadlines, directly analogous to the trade‑off between early migration cost and later breach liability.

Together these twelve works provide process, epistemic, methodological, and structural context for the model we construct.

## 3. Methods

### 3.1 Model primitives (main model)

Time is measured in years. An organization holds RSA‑2048 assets whose compromise would cause loss $L$, expressed in units of the migration cost $C_m$ (so $C_m=1$ by normalization). The discount rate is $r$ per year. The hardness conjecture is represented by a two‑hypothesis mixture:

* $H_{\mathrm{BPP}}$: a regime where cryptographically relevant factoring breakthroughs arrive with annual hazard $h_{\mathrm{BPP}}$;
* $H_{\mathrm{HARD}}$: a regime where breakthroughs arrive with annual hazard $h_{\mathrm{HARD}}\ll h_{\mathrm{BPP}}$;
* $\pi=\Pr(H_{\mathrm{BPP}})$ is the Bayesian prior weight on the fast‑breakthrough regime.

The predictive (mixture) hazard is  

$$
\bar{h}(\pi)=\pi\,h_{\mathrm{BPP}}+(1-\pi)\,h_{\mathrm{HARD}}.
$$

A breakthrough is modeled as a memoryless Poisson event: conditional on the regime, the waiting time to breakthrough is exponential with the regime’s hazard. The prior $\pi$ is treated as an input; we recommend eliciting it via the finite procedure of Posterior Belief Assessment [7] or, in the absence of expert input, adopting an objective uniform prior as in [8].

### 3.2 Expected discounted loss of remaining exposed

If the organization never migrates proactively and a breakthrough arrives at time $t$, it suffers loss $L$ at $t$, discounted to present value by $e^{-rt}$. Averaging over the exponential waiting time under the mixture hazard $\bar{h}$:

$$
E_{\mathrm{exposed}}=\int_{0}^{\infty}L\,\bar{h}\,e^{-\bar{h}t}\,e^{-rt}\,dt
= L\,\bar{h}\int_{0}^{\infty}e^{-(\bar{h}+r)t}\,dt
= \frac{L\,\bar{h}}{\bar{h}+r}.
$$

Immediate migration costs $C_m=1$ at $t=0$ and eliminates exposure. Immediate migration is optimal exactly when  

$$
1<\frac{L\,\bar{h}}{\bar{h}+r}
\;\Longleftrightarrow\;
L>L^{\ast}(\pi)=\frac{\bar{h}+r}{\bar{h}}=1+\frac{r}{\bar{h}}.
$$

The threshold $L^{\ast}(\pi)$ is decreasing in $\pi$; as $\pi\to1$ it approaches $1+r/h_{\mathrm{BPP}}$, while as $\pi\to0$ it approaches $1+r/h_{\mathrm{HARD}}$.

### 3.3 Prior threshold for a given asset value

For a given loss $L>1$, rearranging the optimality condition yields the required mixture hazard  

$$
\bar{h}(\pi)>\frac{r}{L-1}.
$$

Since $\bar{h}(\pi)=h_{\mathrm{HARD}}+\pi\,(h_{\mathrm{BPP}}-h_{\mathrm{HARD}})$, solving for $\pi$ gives the critical prior  

$$
\pi^{\ast}(L)=\frac{\dfrac{r}{L-1}-h_{\mathrm{HARD}}}{h_{\mathrm{BPP}}-h_{\mathrm{HARD}}}.
$$

### 3.4 Alternative scenario models (reconciled from independent parameterizations)

**Scenario D (discrete two‑point).** A single horizon $T$, a prior $p$ of a breakthrough within the horizon, migration cost $C_m$ paid at $t=0$ if migrating immediately, breach cost $C_b$ discounted by $d=e^{-rT}$ if the organization waits. The expected cost of waiting is  

$$
E_{\mathrm{wait}}=p\,C_b\,d+(1-p)\,C_m,
$$

and the break‑even prior under the simplified comparison (migration forced at $T$) is  

$$
p^{\ast}= \frac{C_m}{C_b\,d}.
$$

**Scenario P (continuous two‑hazard Poisson).** A classical breakthrough arrives with hazard $\lambda$, a quantum capability with independent hazard $\mu$; combined hazard $\Lambda=\lambda+\mu$. Migration at time $T$ costs $C_m$ (discounted). If a breakthrough of either type occurs at $t<T$, loss accrues at rate $L$ per year until $T$. The expected discounted cost is  

$$
E[C](T)=C_m e^{-rT}+L\,\Lambda\int_{0}^{T}e^{-\Lambda t}\,(T-t)\,e^{-rt}\,dt.
$$

Let $a=\Lambda+r$. Evaluating the integral yields  

$$
E[C](T)=C_m e^{-rT}+ \frac{L\,\Lambda}{a^{2}}\Bigl[1-(1+aT)e^{-aT}\Bigr].
$$

The first‑order condition for the optimal migration time $T^{\ast}$ is  

$$
r\,C_m e^{-rT^{\ast}}=\frac{L\,\Lambda}{a}\bigl(1-e^{-aT^{\ast}}\bigr).
$$

We solve this equation numerically in Section 4.4.

### 3.5 The reduction‑of‑urgency argument

The entire quantum‑advantage case for RSA‑2048 urgency reduces to the single unproven premise FACTORING ∉ BPP: if the premise fails, quantum hardware is irrelevant to RSA. A companion structural question—what fraction of known exponential speedups depend on abelian hidden‑subgroup structure—is flagged as a stress‑test hypothesis in Section 6, not as a computed result.

## 4. Analysis

All input numbers are declared in Section 3.1 and reproduced here for transparency.

### 4.1 Main model: mixture hazard and loss threshold

**Inputs (modeling assumptions).**  

* $h_{\mathrm{BPP}}=0.10$ yr⁻¹  
* $h_{\mathrm{HARD}}=0.01$ yr⁻¹  
* $\pi=0.20$  
* $r=0.05$ yr⁻¹  
* $C_m=1$ (normalization)

**Step 1: mixture hazard.**  

\[
\bar{h}= \pi h_{\mathrm{BPP}}+(1-\pi)h_{\mathrm{HARD}}
=0.2\times0.10+0.8\times0.01
=0.020+0.008
=0.028\;\text{yr}^{-1}.
\]

**Step 2: expected discounted loss for $L=10$.**  

\[
E_{\mathrm{exposed}}=\frac{L\,\bar{h}}{\bar{h}+r}
=\frac{10\times0.028}{0.028+0.05}
=\frac{0.28}{0.078}
\approx3.589744.
\]

Since $E_{\mathrm{exposed}}\approx3.59>C_m=1$, immediate migration is optimal for a ten‑unit asset.

**Step 3: loss threshold.**  

\[
L^{\ast}(\pi)=1+\frac{r}{\bar{h}}
=1+\frac{0.05}{0.028}
=1+1.785714\ldots
\approx2.785714.
\]

Any asset with $L>2.785714$ justifies immediate migration at the baseline prior.

**Step 4: sensitivity in $\pi$.**  

* $\pi=0$: $\bar{h}=0.01$, $L^{\ast}=1+0.05/0.01=6$.  
* $\pi=1$: $\bar{h}=0.10$, $L^{\ast}=1+0.05/0.10=1.5$.

Thus the threshold varies between $1.5$ and $6$ as the prior moves from certainty of a fast breakthrough to certainty of hardness.

**Step 5: critical prior for a low‑value asset $L=2$.**  

Required mixture hazard:  

\[
\bar{h}^{\mathrm{req}}=\frac{r}{L-1}=\frac{0.05}{1}=0.05.
\]

Solve $0.01+0.09\pi=0.05$:

\[
\pi^{\ast}=\frac{0.05-0.01}{0.09}
=\frac{0.04}{0.09}
=0.444444\ldots.
\]

Therefore a two‑unit asset requires $\pi>0.44$ for immediate migration to be optimal.

### 4.2 Scenario D (discrete two‑point)

**Inputs (modeling assumptions).**  

* $p=0.05$ (prior probability of breakthrough within horizon)  
* $C_m=\$10{,}000{,}000$  
* $C_b=\$200{,}000{,}000$  
* $r=0.05$ yr⁻¹ (continuous)  
* $T=10$ yr

**Step 1: discount factor.**  

\[
d=e^{-rT}=e^{-0.05\times10}=e^{-0.5}\approx0.606531.
\]

**Step 2: discounted breach cost when waiting.**  

\[
p\,C_b\,d=0.05\times200{,}000{,}000\times0.606531
=10{,}000{,}000\times0.606531
\approx\$6{,}065{,}310.
\]

**Step 3: expected total cost of waiting.**  

\[
E_{\mathrm{wait}}=p\,C_b\,d+(1-p)C_m
=6{,}065{,}310+0.95\times10{,}000{,}000
=6{,}065{,}310+9{,}500{,}000
=\$15{,}565{,}310.
\]

Since $C_m=\$10{,}000{,}000<E_{\mathrm{wait}}$, immediate migration is optimal under Scenario D.

**Step 4: break‑even prior (simplified comparison).**  

\[
p^{\ast}=\frac{C_m}{C_b\,d}
=\frac{10{,}000{,}000}{200{,}000{,}000\times0.606531}
=\frac{10{,}000{,}000}{121{,}306{,}200}
\approx0.0825.
\]

If the prior probability of a breakthrough within ten years exceeds $8.25\%$, waiting becomes preferable under the simplified comparison.

### 4.3 Scenario P (continuous two‑hazard Poisson)

**Inputs (modeling assumptions).**  

* Classical hazard $\lambda = h_{\mathrm{HARD}} = 0.01$ yr⁻¹  
* Quantum hazard $\mu = h_{\mathrm{BPP}} = 0.10$ yr⁻¹  
* Combined hazard $\Lambda = \lambda+\mu = 0.11$ yr⁻¹  
* Discount rate $r = 0.05$ yr⁻¹  
* Breach loss $L = 10$ (units of $C_m$)  
* Migration cost $C_m = 1$

**Step 1: auxiliary constant.**  

\[
a = \Lambda + r = 0.11 + 0.05 = 0.16\;\text{yr}^{-1}.
\]

**Step 2: first‑order condition for optimal $T^{\ast}$.**  

\[
r\,C_m e^{-rT^{\ast}} = \frac{L\,\Lambda}{a}\bigl(1-e^{-aT^{\ast}}\bigr).
\]

Substituting numbers:

\[
0.05\,e^{-0.05T^{\ast}} = \frac{10\times0.11}{0.16}\bigl(1-e^{-0.16T^{\ast}}\bigr)
=6.875\bigl(1-e^{-0.16T^{\ast}}\bigr).
\]

**Step 3: numerical solution (bisection).**  

We evaluate the left‑hand side (LHS) and right‑hand side (RHS) for candidate $T$ values:

| $T$ (yr) | LHS = $0.05e^{-0.05T}$ | RHS = $6.875(1-e^{-0.16T})$ |
|----------|------------------------|-----------------------------|
| 0.00     | 0.050000               | 0.000000                    |
| 0.02     | 0.049950               | 0.022000                    |
| 0.04     | 0.049900               | 0.045200                    |
| 0.045    | 0.049887               | 0.049400                    |
| 0.046    | 0.049882               | 0.050200                    |
| 0.047    | 0.049877               | 0.051000                    |

The sign changes between $T=0.045$ yr (RHS < LHS) and $T=0.046$ yr (RHS > LHS). Linear interpolation gives  

\[
T^{\ast}\approx0.0455\;\text{yr}.
\]

Converting to days: $0.0455\times365\approx16.6$ days. We report $T^{\ast}\approx0.046$ yr (≈ 17 days).

## 5. Results

| Quantity | Symbol | Computed value | Interpretation |
|----------|--------|----------------|----------------|
| Mixture hazard | $\bar{h}$ | $0.028$ yr⁻¹ | Expected breakthrough rate under baseline prior $\pi=0.2$. |
| Expected discounted loss ( $L=10$ ) | $E_{\mathrm{exposed}}$ | $3.589744$ | Loss exceeds migration cost; immediate migration optimal. |
| Loss threshold (baseline) | $L^{\ast}(0.2)$ | $2.785714$ | Assets with $L>2.79$ merit immediate migration. |
| Loss threshold ( $\pi=0$ ) | $L^{\ast}(0)$ | $6$ | Even with no fast‑breakthrough belief, high‑value assets still trigger migration. |
| Loss threshold ( $\pi=1$ ) | $L^{\ast}(1)$ | $1.5$ | If fast breakthrough is certain, even modest assets should migrate. |
| Critical prior for $L=2$ | $\pi^{\ast}$ | $0.444444$ | Prior must exceed $44.44\%$ for immediate migration of a low‑value asset. |
| Scenario D break‑even prior | $p^{\ast}$ | $0.0825$ | If breakthrough probability within ten years exceeds $8.25\%$, waiting becomes preferable under the simplified comparison. |
| Scenario P optimal migration time | $T^{\ast}$ | $0.046$ yr (≈ 17 days) | With both classical and quantum hazards, the cost‑minimizing migration occurs essentially immediately. |

All values follow directly from the arithmetic presented in Section 4.

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Hazards $h_{\mathrm{BPP}}$ and $h_{\mathrm{HARD}}$ are constant over time. | If hazards increase (e.g., accelerating research), $\bar{h}$ would be larger, lowering $L^{\ast}$ and strengthening the case for early migration. |
| Prior $\pi$ is treated as a scalar without temporal dynamics. | A time‑varying $\pi(t)$ could shift the optimal decision point; our static analysis provides a snapshot. |
| Discount rate $r$ is fixed at $0.05$ yr⁻¹. | Higher $r$ inflates $L^{\ast}$, making migration less attractive; lower $r$ has the opposite effect. |
| Loss $L$ is expressed in units of migration cost. | Mis‑specifying $L$ (e.g., under‑estimating breach impact) could lead to premature migration. |
| Scenario P assumes independent classical and quantum hazards. | Correlation between the two processes would alter the combined hazard $\Lambda$ and the optimal $T^{\ast}$. |
| Expert elicitation of $\pi$ is not performed. | The numerical results illustrate sensitivity; actual decision making requires a credible elicitation process. |

### 6.2 Failure modes and falsification

The central claim—that the loss threshold $L^{\ast}(\pi)=1+r/\bar{h}$ correctly determines the optimality of immediate migration—would be falsified if empirical observation showed a case where $L>L^{\ast}(\pi)$ yet delayed migration yielded lower total discounted cost. Such a counterexample would imply that the exponential waiting‑time model or the constant‑hazard assumption is invalid. A concrete falsification test is to monitor a controlled pilot deployment where migration timing and breach outcomes are recorded; if the observed discounted loss deviates systematically from the model prediction, the model assumptions must be revised.

### 6.3 Relation to prior work

Our closed‑form threshold extends the risk‑based process of [2] by providing a quantitative decision rule. The spike‑and‑slab prior structure mirrors that of [5] but is applied to a hypothesis rather than regression coefficients. The sensitivity sweep over $\pi$ implements the objective‑prior philosophy of [8] in a decision‑analytic context. The network‑flow framing of [3] motivates future extensions where assets are linked in a graph and migration pressure propagates, but such extensions lie beyond the scope of the present analytical treatment.

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended users and decision impact

The primary users are security architects, risk managers, and policy makers within large organizations that maintain RSA‑2048‑protected infrastructures (e.g., financial institutions, cloud providers, national security agencies). The model informs the *when* component of a migration plan: given an estimate of breach loss $L$, discount rate $r$, and a elicited prior $\pi$, the decision rule $L>L^{\ast}(\pi)$ tells whether to migrate immediately or to defer.

### 7.2 Technology readiness

The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at **TRL 2** (technology concept and/or application formulated).

### 7.3 Minimal next experiment

A feasible next step is a **prior‑elicitation pilot**: assemble a panel of complexity‑theory experts, present the hazard parameters $h_{\mathrm{BPP}}$ and $h_{\mathrm{HARD}}$, and use the Posterior Belief Assessment procedure of [7] to obtain a quantitative prior $\pi$. The pilot would then compute $L^{\ast}(\pi)$ for a set of representative asset loss values. **Falsification condition:** if the elicited $\pi$ falls outside the interval $[0,1]$ or leads to a loss threshold that contradicts established industry migration timelines, the modeling assumptions would be called into question.

### 7.4 Engineering, manufacturing, or deployment constraints

* **Expert elicitation infrastructure:** requires a platform for structured Bayesian belief elicitation (e.g., online surveys with calibrated probability questions).  
* **Parameter estimation:** reliable estimates of $h_{\mathrm{BPP}}$ and $h_{\mathrm{HARD}}$ depend on historical analysis of algorithmic breakthroughs (e.g., GNFS performance trends).  
* **Discount rate selection:** organizations must agree on a financial discount rate consistent with their capital‑allocation policies.  
* **Loss quantification:** translating breach impact into units of migration cost demands a consistent accounting framework across assets.

These constraints are *data* and *process* constraints rather than material or manufacturing constraints.

### 7.5 Projected cost and performance bounds (projections)

Assuming the baseline inputs ($h_{\mathrm{BPP}}=0.10$, $h_{\mathrm{HARD}}=0.01$, $r=0.05$) and a prior $\pi=0.20$, the loss threshold is $L^{\ast}\approx2.79$. For an asset whose estimated breach loss is $L=5$, the model projects that immediate migration reduces expected discounted loss from $E_{\mathrm{exposed}}= \frac{5\times0.028}{0.078}\approx1.795$ to the migration cost $C_m=1$, a net expected saving of $0.795$ migration‑cost units. This projection holds under the stated assumptions; deviations in hazards or discount rate would scale the saving proportionally.

### 7.6 Risks and misuse paths

If an organization adopts the model but under‑estimates $L$ (e.g., by ignoring indirect regulatory penalties), it may postpone migration despite a high true breach loss, leading to greater exposure. Conversely, over‑estimating $\pi$ could trigger unnecessary early migration, incurring avoidable engineering costs. Transparent documentation of input assumptions mitigates these risks.

## 8. Conclusion

By treating the unproven conjecture FACTORING ∉ BPP as an explicit Bayesian prior, we have derived a simple, closed‑form decision rule that determines when immediate PQC migration for RSA‑2048 is optimal. The loss threshold $L^{\ast}(\pi)=1+r/\bar{h}$ captures the trade‑off between breach loss and migration cost under uncertainty about factoring hardness. Sensitivity analysis shows that high‑value assets warrant migration even if the fast‑breakthrough regime is deemed unlikely, while low‑value assets require a substantial prior belief in a fast breakthrough. Alternative scenario analyses (discrete and continuous hazards) reinforce the robustness of the conclusion: under realistic numeric inputs the optimal migration time is effectively immediate. The framework provides organizations with a transparent, auditable parameter ($\pi$) that can be refined through expert elicitation, enabling risk‑aware migration planning that explicitly acknowledges the epistemic status of a foundational complexity‑theoretic conjecture.

## References

[1] arXiv:2603.09958v1 | Tetris is Hard with Just One Piece Type  
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
[12] QNFO: The Revolutionary Beginner's Guide to Quantum Computing: Why We Don't Have Quantum Computers Yet — and What the Geometric Alternative Offers  

## Appendix A. Divergence report

*No divergent claims were identified among the source drafts; all substantive statements converged.*

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts | Agreement |
|----------|-----------|---------------|-----------|
| C1 | Mixture hazard $\bar{h}=0.028$ yr⁻¹ | A, B, C | Convergent |
| C2 | Expected discounted loss $E_{\mathrm{exposed}}=3.589744$ for $L=10$ | A, B, C | Convergent |
| C3 | Loss threshold $L^{\ast}=2.785714$ at $\pi=0.2$ | A, B, C | Convergent |
| C4 | $L^{\ast}=6$ when $\pi=0$ | A, B, C | Convergent |
| C5 | $L^{\ast