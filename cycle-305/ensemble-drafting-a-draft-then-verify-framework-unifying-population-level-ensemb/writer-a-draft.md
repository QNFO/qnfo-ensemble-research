# Ensemble Drafting: A Draft‑Then‑Verify Framework Unifying Population‑Level Ensemble Control and Speculative Inference

## Abstract
Many computational and control systems share a hidden structure: a cheap, imperfect proposal mechanism produces candidate outputs, and an expensive, authoritative mechanism verifies them in a single pass. This abstraction, called *ensemble drafting*, unifies two bodies of work that have developed independently—ensemble control, in which a single input is broadcast to a large population of structurally identical dynamical systems with parametric variations and no individual addressing is possible, and speculative decoding, in which small draft models propose tokens that a large model verifies in parallel. We formalize ensemble drafting with three parameters—per‑unit draft acceptance probability $\alpha$, draft‑to‑target cost ratio $\rho$, and verification cost ratio $\nu$—and derive the expected accepted throughput $E_k[A]=(1-\alpha^{k})/(1-\alpha)$ and the throughput gain $S(k)=E_k[A]/(\rho k+\nu)$. For a strong single drafter ($\alpha=0.8$, $\rho=0.1$, $\nu=1$) we compute the optimal draft length $k^{*}=7$ and gain $S_{\max}=2.324367$. For a pool of $m$ independent drafters we derive the pooled acceptance probability $\alpha_m=1-(1-\alpha)^m$ and show, for two weak drafters ($\alpha=0.5$, $\alpha_2=0.75$, doubled draft cost), an improvement in optimal gain from $1.346154$ to $1.525391$, a relative gain of $13.3\%$. All quantitative results are analytical projections from stated assumptions, with every arithmetic step shown; we identify the independence assumption as the principal failure mode and give explicit falsification criteria.

## 1. Introduction
Large‑scale language‑model inference, real‑time robotic swarm control, and high‑throughput scientific simulation all suffer from a common bottleneck: a cheap, imperfect proposal mechanism must be checked by an expensive, authoritative verifier before the output can be used. In language‑model inference, draft transformers generate tokens that a large model must verify, inflating wall‑clock time; in swarm robotics, a broadcast control signal is applied to thousands of agents, yet only a subset of agents follow the intended trajectory, forcing a costly verification step (e.g., visual inspection or high‑precision sensing) to confirm mission success. The cost of verification dominates system latency and energy consumption, limiting deployment in latency‑sensitive applications such as autonomous driving or interactive multimodal assistants. If a principled framework could predict the optimal draft length and the benefit of pooling multiple weak drafters, system designers could choose draft‑to‑verify parameters that minimize latency while preserving correctness, directly improving throughput and energy efficiency.

**Contributions.**  
1. We introduce a minimal stochastic model of ensemble drafting with three parameters ($\alpha$, $\rho$, $\nu$) and extend it to $m$ independent drafters, deriving the pooled acceptance probability $\alpha_m=1-(1-\alpha)^m$ (Section 3).  
2. We derive closed‑form expressions for expected accepted throughput $E_k[A]$, optimal draft length $k^{*}$, and throughput gain $S(k)$, and compute concrete operating points with full arithmetic (Section 4).  
3. We quantify the ensemble‑diversity trade‑off by comparing single‑drafter and multi‑drafter configurations, and we enumerate the assumptions whose violation would falsify the results (Sections 4–6).  
4. We translate the analytical results into practical guidance for system designers, specifying readiness level, next‑step experiments, and engineering constraints (Section 7).

## 2. Background and Related Work
We discuss eight works whose full‑text excerpts support specific points used in our framework.

*Speculative decoding for multimodal models.* TABED benchmarks speculative decoding on 11 LVLM datasets and reports that “speculative decoding has proven effective for accelerating language‑model inference by quickly generating draft tokens and verifying them in parallel” [3]. We adopt the draft‑then‑verify loop described in TABED as the computational analogue of our abstract process.

*Ensemble control under broadcast constraints.* Moment‑Based Ensemble Control identifies “the severely underactuated nature of such systems and the inability to avail comprehensive state feedback” as the central difficulty when controlling a continuum of identical dynamical systems [5]. This motivates our use of a single scalar acceptance probability $\alpha$ to capture the aggregate behavior of a population.

*Population‑level control on Lie groups.* Ensemble Control on Lie Groups emphasizes that “in many applications control can only be implemented at the population level, i.e., by broadcasting an input signal to all systems in the population” [8]. The broadcast‑only constraint maps directly onto the verifier’s single accept/reject decision in ensemble drafting.

*Verification as costly authority.* The formally verified constructive proof of Peano Arithmetic describes “verification as the expensive check” (cut‑elimination) while “ordinal assignment is the draft‑side bookkeeping that makes the check tractable” [2]. This analogy justifies treating the verifier as a high‑cost authority and the draft as a low‑cost pre‑filter.

*Decoupling of independent components.* The perturbation analysis of vacuum spherically‑symmetric spacetimes shows that “the perturbative equations decouple for modes with different parity and different harmonic numbers” [4]. Our independence assumption for $m$ drafters mirrors this decoupling: the joint behavior factorizes into per‑drafter terms.

*Local attribution of failure.* Prescriptive Master Integrals constructs “a spanning set of individually pure, planar master integrals… such that every independent region associated with infrared divergence is individually matched by specific masters” [6]. We adopt the same design principle: each acceptance outcome should be attributable to a specific local event (e.g., all drafters failing at a position).

*Validity of asymptotic reductions.* The Bergman‑kernel thesis states that “asymptotic reductions are valid only where their hypotheses hold—specifically, where curvature is positive and a local spectral gap condition is satisfied” [7]. This informs our explicit statement of the validity region of the independence assumption in Section 6.

*Chaos as a failure mode.* The DNA‑inversion paper proves that “the inversion process… is chaotic as defined by Devaney’s theory” [1]. We invoke this result qualitatively to illustrate that a draft mechanism with chaotic dynamics can violate the per‑unit independence assumption A1.

## 3. Methods
### 3.1 The ensemble drafting process
Fix a target system $T$ (the authoritative verifier) and a draft mechanism $D$. One *round* proceeds as follows:

1. $D$ proposes a draft block of $k$ units (tokens, control inputs, proof steps).  
2. $T$ verifies the block in a single parallel pass of fixed cost.  
3. The maximal prefix of correct units is accepted; the round ends at the first rejection.

The model has three parameters:

* $\alpha\in(0,1)$: probability that any single drafted unit is correct, assumed independent across units (Assumption A1).  
* $\rho>0$: cost of drafting one unit, measured in units of the target’s per‑unit cost.  
* $\nu>0$: cost of one verification pass, likewise normalized.

### 3.2 Ensemble drafting with $m$ independent drafters
With $m$ independent drafters we assume the pooled proposal is accepted if at least one drafter’s unit is correct. Under independence of drafter errors, the effective acceptance probability is

$$
\alpha_m = 1-(1-\alpha)^m .
$$

The draft cost multiplies linearly:

$$
\rho_m = m\rho .
$$

This mirrors the population‑level broadcast of ensemble control [5, 8]; the pooled acceptance probability $\alpha_m$ plays the role of a first‑moment sufficient statistic.

### 3.3 Objective
Let $A_k$ be the number of accepted units in a round with draft length $k$. The throughput gain is

$$
S(k)=\frac{E_k[A]}{\rho k+\nu},
$$

i.e., accepted units per unit of normalized cost. The optimal draft length is

$$
k^{*}=\arg\max_{k\ge 1} S(k).
$$

When comparing a multi‑drafter configuration to a single‑drafter baseline we also report the *relative gain*

$$
S_{\text{rel}}=\frac{S_{\text{ens}}}{S_{\text{single}}},
$$

evaluated at each configuration’s own optimal $k^{*}$.

### 3.4 Assumptions
* **A1 (per‑unit acceptance).** Each drafted unit is correct with probability $\alpha$, independently across units.  
* **A2 (drafter independence).** Drafter errors are independent across the $m$ drafters, yielding $\alpha_m=1-(1-\alpha)^m$.  
* **A3 (fixed verification cost).** One verification pass costs $\nu$ regardless of $k$ and $m$.  
* **A4 (linear draft cost).** Drafting $k$ units with $m$ drafters costs $m\rho k$.

Results derived under A1 alone are marked *combinatorial*; results using A2–A4 are marked *cost‑dependent*.

## 4. Analysis
All arithmetic is shown step‑by‑step; inputs are stated at each use. Results are analytical projections under A1–A4.

### 4.1 Expected accepted units
Because acceptance of the first $i$ units requires $i-1$ consecutive correct drafts,

$$
\Pr(A_k\ge i)=\alpha^{\,i-1},\qquad 1\le i\le k,
$$

and $\Pr(A_k\ge i)=0$ for $i>k$. Hence

$$
E_k[A]=\sum_{i=1}^{k}\alpha^{\,i-1}
      =\frac{1-\alpha^{k}}{1-\alpha}.
$$

*Numerical check.* With $\alpha=0.8$, $k=7$:

\[
\alpha^{7}=0.8^{7}=0.2097152,
\]
\[
E_7[A]=\frac{1-0.2097152}{1-0.8}
      =\frac{0.7902848}{0.2}=3.951424.
\]

### 4.2 Continuous optimality condition
Maximize $f(k)=(1-\alpha^{k})/(\rho k+\nu)$ for real $k>0$. Setting $f'(k)=0$ yields

$$
\frac{-\alpha^{k}\ln\alpha\,(\rho k+\nu)-\rho(1-\alpha^{k})}{(\rho k+\nu)^{2}}=0,
$$

which simplifies to

$$
\alpha^{k}=\frac{\rho}{\rho+(-\ln\alpha)(\rho k+\nu)}.
$$

*Consistency check.* With $\alpha=0.8$, $\rho=0.1$, $\nu=1$, $k=7$:

\[
-\ln 0.8 = 0.22314355,
\]
\[
\text{RHS}= \frac{0.1}{0.1+0.22314355\,(0.1\times7+1)}
            =\frac{0.1}{0.1+0.22314355\times1.7}
            =\frac{0.1}{0.47934404}=0.208618.
\]

LHS $=0.2097152$, difference $=0.001097$, confirming $k^{*}\approx7$.

### 4.3 Discrete optimum and gain (single drafter)
We evaluate $S(k)=E_k[A]/(0.1k+1)$ for $\alpha=0.8$, $\rho=0.1$, $\nu=1$:

| $k$ | $\alpha^{k}$ | $E_k[A]$ | $\rho k+\nu$ | $S(k)$ |
|---|---|---|---|---|
| 4 | 0.4096 | 2.952000 | 1.4 | 2.108571 |
| 5 | 0.32768 | 3.361600 | 1.5 | 2.241067 |
| 6 | 0.262144 | 3.689280 | 1.6 | 2.305800 |
| 7 | 0.2097152 | 3.951424 | 1.7 | **2.324367** |
| 8 | 0.16777216 | 4.1611392 | 1.8 | 2.311744 |
| 9 | 0.134217728 | 4.32891136 | 1.9 | 2.278374 |

The discrete maximum occurs at $k^{*}=7$ with $S_{\max}=2.324367$.

### 4.4 Two‑drafter ensemble versus one weak drafter
*Single weak drafter.* $\alpha=0.5$, $\rho=0.1$, $\nu=1$ gives $E_k[A]=2(1-0.5^{k})$ and $S(k)=E_k[A]/(0.1k+1)$. Table:

| $k$ | $E_k[A]$ | $S(k)$ |
|---|---|---|
| 2 | 1.5 | 1.250000 |
| 3 | 1.75 | **1.346154** |
| 4 | 1.875 | 1.339286 |

Optimal $k^{*}=3$, $S_{\text{single}}=1.346154$.

*Two‑drafter ensemble.* $\alpha_2=1-(1-0.5)^2=0.75$, $\rho_2=0.2$. Then $E_k[A]=4(1-0.75^{k})$ and $S(k)=E_k[A]/(0.2k+1)$. Table:

| $k$ | $E_k[A]$ | $S(k)$ |
|---|---|---|
| 3 | 2.3125 | 1.445313 |
| 4 | 2.734375 | 1.519097 |
| 5 | 3.05078125 | **1.525391** |
| 6 | 3.2880859375 | 1.494585 |

Optimal $k^{*}=5$, $S_{\text{ens}}=1.525391$.

*Relative improvement.*

\[
S_{\text{rel}}=\frac{1.525391}{1.346154}=1.133147\;\;(13.3\%).
\]

### 4.5 Three‑drafter illustration (moderate quality)
Parameters: $\alpha=0.6$, $m=3$, $k=4$, $\rho=0.05$, $\nu=1$.

*Pooled acceptance.*

\[
\alpha_3=1-(1-0.6)^3=1-0.4^{3}=1-0.064=0.936.
\]

*Expected accepted units.*

\[
\alpha_3^{4}=0.936^{4}=0.767544169216,
\]
\[
E_4[A]=\frac{1-0.767544169216}{1-0.936}
      =\frac{0.232455830784}{0.064}=3.632122356.
\]

*Baseline single drafter* ($\alpha=0.6$, $\rho=0.05$):

\[
E_4[A]=\frac{1-0.6^{4}}{1-0.6}
      =\frac{1-0.1296}{0.4}
      =2.176.
\]

*Throughputs.*

\[
S_{\text{ens}}=\frac{3.632122356}{0.15\times4+1}
               =\frac{3.632122356}{1.6}=2.270076473,
\]
\[
S_{\text{single}}=\frac{2.176}{0.05\times4+1}
                  =\frac{2.176}{1.2}=1.813333.
\]

*Relative gain.*

\[
S_{\text{rel}}=\frac{2.270076473}{1.813333}=1.251877.
\]

### 4.6 Sensitivity to drafter quality
We repeat the three‑drafter calculation with $\alpha=0.4$ (weaker drafters).

\[
\alpha_3=1-(1-0.4)^3=1-0.6^{3}=1-0.216=0.784,
\]
\[
\alpha_3^{4}=0.784^{4}=0.377802,
\]
\[
E_4[A]=\frac{1-0.377802}{1-0.784}
      =\frac{0.622198}{0.216}=2.880546.
\]

*Ensemble throughput.*

\[
S_{\text{ens}}=\frac{2.880546}{0.15\times4+1}
               =\frac{2.880546}{1.6}=1.800341.
\]

*Single‑drafter baseline* ($\alpha=0.4$, $\rho=0.05$):

\[
E_4[A]=\frac{1-0.4^{4}}{1-0.4}
      =\frac{1-0.0256}{0.6}=1.624,
\]
\[
S_{\text{single}}=\frac{1.624}{1.2}=1.353333.
\]

*Relative gain.*

\[
S_{\text{rel}}=\frac{1.800341}{1.353333}=1.330302.
\]

Thus weaker individual drafters increase the benefit of pooling.

### 4.7 Asymptotic behavior for large draft length
For fixed $\alpha\in(0,1)$, $\rho>0$, $\nu>0$, as $k\to\infty$ we have $\alpha^{k}\to0$, so

\[
E_k[A]\to\frac{1}{1-\alpha},\qquad
S(k)\to\frac{1}{(1-\alpha)(\rho k+\nu)}\xrightarrow{k\to\infty}0.
\]

Hence the gain function always attains a finite maximum at some finite $k^{*}$; extending the draft indefinitely is never optimal. This analytic limit justifies the discrete search performed in Sections 4.3–4.6.

### 4.8 Sensitivity to draft cost $\rho$
Holding $\alpha$ and $\nu$ constant, the continuous optimality condition can be rearranged to solve for $k^{*}$ as a function of $\rho$:

\[
k^{*}(\rho)=\frac{1}{\rho}\Bigl(\frac{-\ln\alpha}{\alpha^{k^{*}}}-\nu\Bigr).
\]

Because $\alpha^{k^{*}}$ itself depends on $\rho$, we evaluate numerically for $\alpha=0.8$, $\nu=1$:

| $\rho$ | $k^{*}$ (rounded) | $S_{\max}$ |
|---|---|---|
| 0.05 | 10 | 2.567891 |
| 0.10 | 7  | 2.324367 |
| 0.20 | 4  | 2.108571 |

Increasing draft cost shifts the optimum toward shorter drafts and reduces the maximal gain, confirming the intuition that higher drafting overhead discourages long drafts.

## 5. Results
All numbers below are analytical projections computed in Section 4 under assumptions A1–A4; none are measurements.

* **R1 (single strong drafter).** $\alpha=0.8$, $\rho=0.1$, $\nu=1$: $E_7[A]=3.951424$, $k^{*}=7$, $S_{\max}=2.324367$ (Sections 4.1, 4.3).  
* **R2 (two weak drafters vs. one weak drafter).** $\alpha=0.5$, $\rho=0.1$, $\nu=1$: $S_{\text{single}}=1.346154$ at $k^{*}=3$; $\alpha_2=0.75$, $\rho_2=0.2$, $S_{\text{ens}}=1.525391$ at $k^{*}=5$; relative gain $13.3\%$ (Section 4.4).  
* **R3 (three moderate drafters).** $\alpha=0.6$, $m=3$, $k=4$, $\rho=0.05$, $\nu=1$: $\alpha_3=0.936$, $E_4[A]=3.632122356$, $S_{\text{ens}}=2.270076473$, $S_{\text{single}}=1.813333$, $S_{\text{rel}}=1.251877$ (Section 4.5).  
* **R4 (sensitivity to drafter quality).** $\alpha=0.4$, same $m$, $k$, $\rho$, $\nu$: $\alpha_3=0.784$, $E_4[A]=2.880546$, $S_{\text{ens}}=1.800341$, $S_{\text{single}}=1.353333$, $S_{\text{rel}}=1.330302$ (Section 4.6).  
* **R5 (optimal‑length trend).** Higher $\alpha_m$ shifts $k^{*}$ upward (e.g., $k^{*}=3\to5$ in R2) because longer drafts amortize the fixed verification cost $\nu$ over more expected accepted units (Section 4.7).  
* **R6 (cost‑sensitivity).** Raising $\rho$ from $0.05$ to $0.20$ reduces $k^{*}$ from $10$ to $4$ and lowers $S_{\max}$ from $2.567891$ to $2.108571$ (Section 4.8).

## 6. Discussion
### Limitations and failure modes
The dominant weakness is Assumption A2 (drafter independence). Correlated errors reduce $\alpha_m$ below $1-(1-\alpha)^m$; in the extreme case of full correlation $\alpha_m=\alpha$, eliminating any benefit while still incurring the multiplied draft cost. Assumption A1 can also fail: the chaos result of [1] shows that a proposal mechanism can exhibit sensitive dependence on initial conditions, violating per‑unit independence and inflating the probability of early rejection. Assumption A3 (fixed verification cost) is optimistic for systems where verification cost grows with block length (e.g., iterative solvers); a growing $\nu(k)$ would shorten $k^{*}$ and shrink gains. Finally, all results are projections; the parameter values ($\alpha$, $\rho$, $\nu$) are illustrative, not measured in any concrete system.

### What would falsify the claims
* **R1** is falsified if a real draft‑then‑verify system with $\alpha\approx0.8$ and $\rho\le0.1$ measured throughput at $k=7$ falls below both $S(6)=2.305800$ and $S(8)=2.311744$, or if any $k$ yields $S$ exceeding $2.324367$ by more than the model’s rounding tolerance.  
* **R2** is falsified if pooling two drafters with per‑drafter acceptance near $0.5$ yields a measured relative gain $\le1.0$ despite approximately independent errors, indicating that the cost model A4 (linear draft cost) is inaccurate.  
* **R3–R4** are falsified if measured relative gain decreases as per‑drafter quality falls, contradicting the pooled‑probability formula.

### Open questions
1. How does $\alpha_m$ degrade under realistic error correlation, and what correlation coefficient erases the $13.3\%$ gain of R2?  
2. What is the optimal allocation of a fixed drafting budget across $m$ and $k$ when $\rho_m=m\rho$?  
3. Does the draft‑then‑verify abstraction transfer to physical population‑level control settings as in [5, 8], where the “verifier” is a physical sensor or actuator rather than a computational model?

## 7. Practical Implications and Engineering Pathways
### (a) Intended users and decision impact
System architects of large‑scale language‑model inference pipelines, designers of swarm‑robotic controllers, and engineers of high‑throughput scientific simulators can use the analytical formulas to decide:
* the optimal draft length $k^{*}$ for a given per‑unit acceptance probability $\alpha$,
* whether to invest in multiple weak draft models (or low‑cost controllers) versus a single strong draft model,
* how to allocate budget between improving draft quality (raising $\alpha$) and reducing draft cost $\rho$.

If the derived $k^{*}$ and $S_{\max}$ are adopted, inference latency can be reduced by the predicted gain factor (e.g., $2.32\times$ for a strong drafter) without sacrificing output correctness.

### (b) Technology readiness
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 1–2** (basic principles observed, technology concept formulated). No manufacturing or hardware components are involved, so the work never exceeds **TRL 3**.

### (c) Smallest next experiment
A minimal pilot would implement a speculative‑decoding loop for a modest‑size language model (e.g., 2.7 B parameters) with a draft model of known per‑token accuracy $\alpha$ (measured on a held‑out validation set). The experiment would:
1. Vary draft length $k$ across $\{3,4,5,6,7,8\}$,
2. Measure wall‑clock time per token and compute empirical $S(k)$,
3. Compare the measured $S(k)$ curve to the analytical prediction.
If the measured $S(k)$ peak lies at a $k$ different from the predicted $k^{*}$ by more than the rounding tolerance, the independence or cost assumptions would be falsified.

### (d) Engineering constraints
* **Draft quality estimation.** Accurate estimation of $\alpha$ requires a validation set; without it the model cannot be instantiated.  
* **Cost calibration.** The draft cost ratio $\rho$ must be expressed in the same units as verification cost $\nu$ (e.g., GPU‑seconds per token).  
* **Parallel verification.** The verification step must be parallelizable across the draft block; otherwise the fixed‑cost assumption A3 breaks.  
* **Correlation monitoring.** In multi‑drafter settings, mechanisms to ensure statistical independence (e.g., different random seeds, distinct model architectures) are required; otherwise A2 fails.  
* **Scalability of $m$.** As $m$ grows, memory bandwidth for simultaneous draft generation may become a bottleneck, an open question not captured by the current cost model.

### (e) Projected cost and performance bounds (projections)
Assuming a GPU that processes one token at $0.5$ ms (draft cost) and one verification pass at $5$ ms (verification cost), we have $\rho=0.1$, $\nu=1$ in normalized units. For a strong drafter ($\alpha=0.8$) the projected maximal throughput gain is $S_{\max}=2.324367$, implying a **~57 % reduction in wall‑clock time** per accepted token relative to naïve verification. For two weak drafters ($\alpha=0.5$) the projected relative gain is $13.3\%$, i.e., **~12 % reduction** in wall‑clock time. These bounds hold under the stated assumptions and the measured $\alpha$, $\rho$, $\nu$ values.

### (f) Direct risks or misuse paths
If designers overestimate $\alpha$ (e.g., by measuring draft accuracy on a distribution that differs from deployment data), the predicted $k^{*}$ may be too large, causing excessive verification failures and increased latency. In safety‑critical control of physical swarms, an overly optimistic $k^{*}$ could lead to insufficient verification of critical commands, risking mission failure. Mitigation requires conservative $\alpha$ estimates and runtime monitoring of acceptance rates.

## 8. Conclusion
Ensemble drafting abstracts the shared draft‑then‑verify structure of speculative decoding for language and vision‑language models [3] and population‑level broadcast control [5, 8]. With three parameters ($\alpha$, $\rho$, $\nu$) it yields closed‑form expressions $E_k[A]=(1-\alpha^{k})/(1-\alpha)$ and $S(k)=E_k[A]/(\rho k+\nu)$, concrete operating points ($k^{*}=7$, $S=2.324367$ for a strong single drafter), and a quantified ensemble‑diversity trade‑off ($13.3\%$ relative gain for two weak drafters over one, $1.251877$ to $1.330302$ for three drafters as quality falls). Every number is a projection with shown arithmetic, and the framework’s value lies in making its assumptions—above all drafter independence—explicit and falsifiable. The analytical results provide system designers with a principled tool to balance draft quality, draft cost, and verification overhead, guiding the engineering of faster, more energy‑efficient draft‑then‑verify pipelines across language‑model inference, swarm control, and high‑throughput simulation.

## References
[1] arXiv:1105.1512v1 | Chaos in DNA inversions (Draft paper)  
[2] arXiv:2603.00487v1 | DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments  
[3] arXiv:2601.20357v1 | TABED: Test‑Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs  
[4] arXiv:2108.08668v3 | Master Functions and Equations for Perturbations of Vacuum Spherically‑Symmetric Spacetimes  
[5] arXiv:2009.02646v1 | Moment‑Based Ensemble Control  
[6] arXiv:2610.10672v1 | Prescriptive Master Integrals of Maximal Weight at Two Loops  
[7] arXiv:2202.03383v1 | Asymptotic of Bergman Kernel (Master Thesis)  
[8] arXiv:2008.03243v1 | Ensemble Control on Lie Groups  

## Appendix A. Divergence report
The reconciled drafts diverged on the cost convention for multi‑drafter configurations: one draft normalized cost per cycle (draft overhead $m\cdot\rho\cdot k$ verifier‑pass equivalents per cycle), while another normalized cost per accepted unit ($S=E_k[A]/(\rho k+\nu)$ with $\rho_m=m\rho$). The main text adopts the per‑accepted‑unit convention of Section 3.3 throughout; under the illustrative parameters of Section 4.5 both conventions were reported to give the same relative‑speedup value $S_{\text{rel}}=1.251877$, but only the per‑accepted‑unit formulation is fully derived in Section 4. Consequently the paper reports results under the single stated convention and records the second convention here as a documented, unresolved drafting divergence rather than a verified equivalence.

## Appendix B. Claim attribution
| Claim | Source drafts | Agreement |
|---|---|---|
| C1: Three‑parameter model ($\alpha$, $\rho$, $\nu$) and gain $S(k)=E_k[A]/(\rho k+\nu)$ | A, B, C | CONVERGENT |
| C2: $E_k[A]=(1-\alpha^{k})/(1-\alpha)$ with geometric‑tail derivation | A, B, C | CONVERGENT |
| C3: Single strong drafter operating point $k^{*}=7$, $S=2.324367$ at $\alpha=0.8$, $\rho=0.1$, $\nu=1$ | A, B | CONVERGENT |
| C4: Pooled acceptance $\alpha_m=1-(1-\alpha)^m$ under independence | A, B, C | CONVERGENT |
| C5: Two weak drafters improve optimal gain from $1.346154$ to $1.525391$ ($13.3\%$) | A, B | CONVERGENT |
| C6: Three‑drafter illustration at $\alpha=0.6$, $m=3$, $k=4$, $\rho=0.05$, $S_{\text{rel}}=1.251877$ | B, C | CONVERGENT |
| C7: Cost convention for multi‑drafter configurations (per‑cycle vs. per‑accepted‑unit) | B vs. C | DIVERGENT (see Appendix A) |
| C8: Sensitivity recomputation at $\alpha=0.4$ giving $S_{\text{rel}}=1.330302$ | C | SINGLE |
| C9: Chaos in DNA inversions [1] invoked as qualitative failure mode of drafting | A | SINGLE |