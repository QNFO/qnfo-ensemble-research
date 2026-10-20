# Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet

## Abstract

Autonomous research fleets must keep serverless worker scripts, databases, and storage buckets running while reporting reliable cost and performance metrics, yet existing treatments address fleet sizing, failure propagation, and claim validation in isolation. This paper builds an integrated analytical framework that models reliability, monetary impact, and claim-integrity auditing jointly for the Quniverse fleet. The approach combines a Bernoulli failure-propagation model with a self-healing mitigation factor, resource-consumption aggregation, a weighted composite autonomy score, and a claim-by-claim recomputation of the figures in the fleet's retraction notice, each with explicit arithmetic and unit-dimension checks. Under an assumed per-worker monthly failure probability of $p_f=0.12$ and mitigation factor $\alpha=0.5$, the model yields an expected $E[F]=2.16$ unresolved worker-script failures per month (standard deviation $1.425$), a corpus rate of $9.65$ papers per active project, a high-severity gap proportion of $11.9\%$, and a composite autonomy score of $4.26$ that rises to $4.66$ when the failure probability is halved. Projected monthly gateway spend is $\$160.8$ baseline and $\$155.4$ in the improved scenario. The retraction notice's billing-unit error inflates perceived spend to $\$11{,}000$ — $73.3$-fold the $\$150$ cap and $122.2$-fold the $\$90$ per-30-days gate — while the corrected spend of $\$110$ exceeds the gate by $22.2\%$. These results give operators, funders, and auditors analytically derived levers for reliability and fiscal compliance, at TRL 2 analytical readiness.

## 1. Introduction

Platform operators of the Quniverse autonomous research fleet run a continuously active collection of thirty-six serverless worker scripts, ten SQLite databases, eight vector indexes, and nineteen object-storage buckets that generates and publishes scientific content without human intervention [10]. Two intertwined problems currently block the fleet's value. First, unplanned downtime arises from script failures and drift between the service registry and the deployed code, and failures that escape both the self-healing layer and human notice accumulate silently. Second, self-reported metrics have been shown to be unreliable: the fleet's retraction notice revealed a billing-unit error that inflated the perceived monthly spend to $\$11{,}000$ — far above the documented $\$90$ per 30 days cost gate — and a composite autonomy assessment of $3.6/5$ that conflicted with internal metrics [10]. An operator who cannot trust either the failure counts or the dollar figures cannot budget, cannot set alert thresholds, and cannot demonstrate compliance to a funder.

The stakes are concrete. If the fleet could reduce its unresolved failure rate, align cost reporting with the actual monetary units, and attach a provenance check to every quantitative claim it publishes, three things change: research velocity rises because fewer failures interrupt pipelines, operational cost falls because failure-driven overruns are bounded, and stakeholder trust is restored because every published number can be recomputed from stated inputs. Conversely, if the reliability model proposed here is wrong, a month of monitoring will show it, and the operator will have lost only the cost of reading a log file.

This paper is a post-publication revision of the fleet's own quantitative study [10]. It keeps every derivation that survives recomputation, corrects the presentation of the billing-unit findings so that each ratio names its denominator explicitly, and grounds the framework in the current literature on fleet reliability, silent failures, and metric governance.

**Contributions.**
- **C1.** Derive a stochastic failure-propagation model and compute the expected number of unresolved worker-script failures per month, $E[F]=2.16$, with its Bernoulli variance (Section 4.1, Results R1, R1a, R12).
- **C2.** Quantify corpus productivity, $9.65$ papers per active project, and the high-severity gap proportion, $11.9\%$ (Section 4.2–4.3, Results R2–R3).
- **C3.** Show that a 50% reduction in per-worker failure probability raises the composite autonomy score from $4.26$ to $4.66$ and lowers projected monthly gateway spend from $\$160.8$ to $\$155.4$ (Section 4.5–4.6, Results R4–R7).
- **C4.** Recompute every quantitative claim of the retraction notice, separating the cap-relative ratio ($73.3$-fold against the $\$150$ cap) from the gate-relative ratio ($122.2$-fold against the $\$90$ gate) and the corrected-spend gate exceedance ($22.2\%$) (Section 4.7–4.9, Results R8–R10).
- **C5.** Specify two minimal pilots — a 30-day failure-count measurement and a billing-feed unit-dimension check — with explicit refutation thresholds, and map the results to engineering pathways (Section 7.3).

## 2. Background and Related Work

Reliability modeling for distributed and autonomous systems supplies the methodological foundation of this work, and the most recent literature points to exactly the gap this paper fills. Han and Schotten argue that, with the convergence of communication, computing, and control in future industrial applications, "analytical and optimizing frameworks, however, are not yet readily developed for this new technical trend" [7]; the Quniverse fleet — serverless compute, databases, and storage bound into one autonomous pipeline — is precisely such a converged system, and the integrated framework developed here is a small analytical step into that gap.

The closest methodological precedent for our failure model treats reliability qualification as a sequential decision problem rather than a static calculation. The adaptive test-planning framework of [3] couples Monte Carlo Tree Search with EKF belief-state estimation to choose stress tests for semiconductor devices, and reports that over 5,000 planning iterations the planner improves characterization yield from 20% to over 54% while keeping damage fractions below 0.57 in the best successful test sequence. Our monthly Bernoulli model is the static special case of such a sequential view; Section 6 discusses how timestamped failure data would let the fleet move from a fixed $p_f$ to an adaptive, per-worker estimate.

A second recent strand concerns failures that systems do not report. The FAME framework for verifiable AI reliability defines silent failures — confident but incorrect outputs with no internal indication of degradation — and demonstrates their severity empirically: in 100 challenging scenarios a deep network failed its safety requirement in 31 runs, all silent, and the FAME monitor detected 29 of the 31, a 93.5% detection rate [6]. The unresolved failures counted by $E[F]$ are the fleet-level analogue of silent failures: worker-script breakdowns that self-healing does not repair and that no alert catches. FAME's result that a dedicated monitor recovers most but not all silent failures supports our choice to model mitigation as a fraction $\alpha < 1$ rather than assuming complete self-healing.

Fleet-scale data handling motivates our resource-aggregation module. Robot fleets "ingest massive amounts of heterogeneous streaming data silos generated by interacting with their environments, far more than what can be stored or transmitted with ease" [4], which is why fleet-level methods aggregate rather than centralize; the Quniverse bookkeeping faces the same pressure, and Section 4.4 aggregates database and vector-index storage into a single figure for exactly this reason. On the cost side, fleet-composition optimization shows that heterogeneous fleets carry heterogeneous running costs: the vehicle-routing work of [5] sizes a fleet in which "refrigerated vehicles are more expensive to run than regular vehicles," using separate demand classes to determine how many of each type are required, and finds its stable-fleet MIP formulation outperforms a CP-based LNS approach on most instances. Our cost-per-failure parameter $c_f$ plays the same role at much smaller scale: it prices the expensive members of the fleet (failing workers) so that reliability investment can be traded against spend.

The empirical validation of any such model requires a testbed that reproduces operational conditions. The FLEET testbed was built because "existing evaluation tools often fail to model realistic operational conditions," and it integrates the Flower federated-learning framework with the Containernet network emulator, exporting comprehensive metrics to ZMQ, CSV, or log files [2]. A validation pilot for the Quniverse model (Section 7.3) needs the same capability in miniature: per-worker failure timestamps and self-heal outcomes exported as structured logs. FLEET's demonstration that its testbed supports reproducible research into "the complex interplay between FL algorithms, system resources, and network conditions" [2] is the pattern our pilot follows.

Layered system architecture is the natural frame for a fleet whose components span compute, data, and control. The autonomous-vehicle literature models the vehicle as a stack of perception, planning, and control subsystems, with the control system "responsible for regulating or maintaining the process conditions of a plant at their respective desired values" [9]; the Quniverse fleet has an analogous stack (worker scripts above databases and indexes above object storage), and our composite autonomy score is a system-level, rather than component-level, summary of that stack's behavior.

Two historical and governance arguments complete the frame. The history-constrained forecast of computing machine evolution documents that in the electromechanical era "the Harvard Mark I's ~3,000 relays failed measurably during operation" and concludes that "reliability, not raw logic, was the binding constraint" [11] — the same binding constraint this paper quantifies for a software fleet. And on the audit side, the QWAV strategy paper records how measurement standards acquired trust: SPEC's benchmarks "carry weight because no single vendor controls them," the core of its neutral-stewardship playbook [12]. The claim-integrity recomputation of Section 4.7–4.9 is a single-auditor version of that principle; institutionalizing it would require the neutral-stewardship pattern. Finally, the JPCUB competitive landscape shows why published, recomputable measurements matter for any metric: of the platforms it surveys, only one (IBM Eagle, at $0.89$ J/solution) has a published measurement while others are listed as not yet measured [13]; a fleet metric such as the composite autonomy score earns credibility the same way, by being recomputable from stated inputs, which is what Section 4 does for every number the retraction notice asserted. Where uncertainty quantification is needed, the landslide-erosion literature offers a template: its Monte Carlo analysis of 1,000 simulations and bootstrap analysis of 10,000 runs attach uncertainty bounds to a derived soil-loss estimate [1]; our exact Bernoulli variance computation (Section 4.1) is the closed-form counterpart for the failure count.

## 3. Methods

The analytical pipeline consists of four deterministic modules, each expressed in closed-form equations. All calculations are performed symbolically and then evaluated numerically with the input values listed in Section 4. No empirical measurements are introduced: the corpus statistics are inherited from the fleet's own published accounting [10], and every other input is labeled an assumption.

**3.1 Failure-Propagation Model.**
Each of the $N_w$ worker scripts experiences a baseline failure probability $p_f$ per month. A fraction $\alpha$ of failures are resolved automatically (self-heal). The effective unresolved-failure probability is

$$p_{\text{eff}} = p_f \times (1-\alpha),$$

and the expected monthly unresolved-failure count is

$$E[F] = N_w \times p_{\text{eff}} = N_w \, p_f \, (1-\alpha).$$

Because the $N_w$ trials are treated as independent Bernoulli trials with common probability $p_{\text{eff}}$, the count $F$ follows a binomial distribution with variance

$$\operatorname{Var}[F] = N_w \, p_{\text{eff}} \, (1 - p_{\text{eff}}).$$

A count-derived alternative to the assumed $\alpha$ is obtained from the fleet's own action tallies: if $H$ self-heal actions and $X$ handoff (unresolved) actions are recorded, then

$$\alpha_{\text{counts}} = \frac{H}{H + X}.$$

**3.2 Resource-Consumption Aggregation.**
Total storage $S_{\text{tot}}$ is the sum of database and vector-index sizes:

$$S_{\text{tot}} = S_{db} + S_{vi},$$

where $S_{db} = 304\ \text{MB}$ (ten D1 databases) and $S_{vi}$ is the product of the vector-index row count and the per-row byte size. We treat MB and MiB as interchangeable at the precision reported (one decimal place); the difference is at most $4.9\%$ per term and is stated as an assumption of the aggregation.

**3.3 Composite Autonomy Score.**
A weighted linear model combines three sub-scores:

$$C = w_c S_c + w_{sh} S_{sh} + w_{oc} S_{oc},$$

with weights $w_c = 0.4$, $w_{sh} = 0.3$, $w_{oc} = 0.3$ taken from the original fleet assessment [10]. Baseline sub-scores are $S_c = 4.5$, $S_{sh} = 4.0$, $S_{oc} = 4.2$. A 50% reduction in failure probability is modeled as a uniform sub-score increment $\Delta = 0.4$, yielding $S_c' = 4.9$, $S_{sh}' = 4.4$, $S_{oc}' = 4.6$. The increment is a modeling choice, not a measurement; its role is to translate a reliability improvement into the assessment scale the fleet already uses.

**3.4 Claim-Integrity Recomputation.**
For each quantitative claim extracted from the retraction notice [10] we: (i) parse the quoted numbers; (ii) reconstruct the asserted arithmetic relation; (iii) recompute the relation step by step; (iv) apply unit-dimension checks to monetary feeds (a value quoted in dollars must be traceable to a source quoted in the same unit, and a cents-to-dollars conversion must divide by 100); and (v) assign a provenance class — Procedure-backed, Unit-dimensioned, Existence-proof, or Surrogate-reward — following the streamlined taxonomy used in the prior version of this study [10]. Every ratio reported in Section 4.7–4.9 names its denominator explicitly, so that no two ratios against different baselines can be conflated.

## 4. Analysis

### 4.1 Expected Failures per Month and Mitigation Factor

Inputs: $N_w = 36$ (fleet inventory [10]); $p_f = 0.12$ (assumption, an upper-bound monthly per-worker failure probability); $\alpha = 0.5$ (assumption, the fraction of failures resolved by self-healing).

Effective failure probability:

$$p_{\text{eff}} = 0.12 \times (1 - 0.5) = 0.12 \times 0.5 = 0.06.$$

Expected unresolved failures:

$$E[F] = 36 \times 0.06 = 2.16.$$

**Alternative mitigation factor from counts.** The retraction notice reports $1{,}889$ self-heal actions and $1{,}264$ handoff actions [10]. The total action count is

$$N_{\text{total}} = 1{,}889 + 1{,}264 = 3{,}153,$$

and the count-derived self-heal fraction is

$$\alpha_{\text{counts}} = \frac{1{,}889}{3{,}153} = 0.59911\ldots \approx 0.599.$$

Using $\alpha_{\text{counts}}$:

$$p_{\text{eff}}^{\text{counts}} = 0.12 \times (1 - 0.599) = 0.12 \times 0.401 = 0.04812,$$
$$E[F]^{\text{counts}} = 36 \times 0.04812 = 1.73232 \approx 1.73.$$

The assumed $\alpha = 0.5$ is therefore the conservative (higher-failure) choice: it predicts $2.16$ unresolved failures where the action tallies predict $1.73$.

**Variance and standard deviation (Bernoulli aggregation).**

$$\operatorname{Var}[F] = N_w \, p_{\text{eff}} (1 - p_{\text{eff}}) = 36 \times 0.06 \times 0.94 = 2.0304,$$
$$\sigma_F = \sqrt{2.0304} = 1.42492\ldots \approx 1.425.$$

**Sensitivity.** $E[F]$ is linear in both $p_f$ and $(1-\alpha)$: halving $p_f$ to $0.06$ gives $E[F] = 36 \times 0.06 \times 0.5 = 1.08$, the improved scenario used in Section 4.6. A one-percentage-point change in $p_f$ changes $E[F]$ by $36 \times 0.01 \times 0.5 = 0.18$ failures per month.

### 4.2 Papers per Active Project

Inputs: total papers $P_{\text{total}} = 917$, active projects $N_{\text{proj}} = 95$ (fleet accounting [10]).

$$\frac{P_{\text{total}}}{N_{\text{proj}}} = \frac{917}{95} = 9.65263\ldots \approx 9.65 \ \text{papers per project}.$$

### 4.3 High-Severity Gap Proportion

Inputs: high-severity gaps $G_{\text{high}} = 5$, total gaps $G_{\text{total}} = 42$ (fleet accounting [10]).

$$\frac{G_{\text{high}}}{G_{\text{total}}} = \frac{5}{42} = 0.119048\ldots \approx 11.9\%.$$

### 4.4 Storage Aggregation

Inputs: $S_{db} = 304\ \text{MB}$; vector-index rows $34{,}657$ at $512\ \text{B}$ per row.

$$S_{vi} = 34{,}657 \times 512\ \text{B} = 17{,}744{,}384\ \text{B}.$$

Converting to MiB ($1\ \text{MiB} = 1{,}048{,}576\ \text{B}$):

$$S_{vi} = \frac{17{,}744{,}384}{1{,}048{,}576} = 16.9219\ \text{MiB} \approx 16.922\ \text{MiB}.$$

Under the stated MB–MiB interchangeability assumption:

$$S_{\text{tot}} = 304 + 16.922 = 320.922 \approx 320.9\ \text{MB}.$$

### 4.5 Composite Autonomy Score

Baseline sub-scores $S_c = 4.5$, $S_{sh} = 4.0$, $S_{oc} = 4.2$; weights $w_c = 0.4$, $w_{sh} = 0.3$, $w_{oc} = 0.3$.

$$C_{\text{base}} = 0.4 \times 4.5 + 0.3 \times 4.0 + 0.3 \times 4.2 = 1.8 + 1.2 + 1.26 = 4.26.$$

Improved sub-scores (increment $\Delta = 0.4$): $S_c' = 4.9$, $S_{sh}' = 4.4$, $S_{oc}' = 4.6$.

$$C_{\text{new}} = 0.4 \times 4.9 + 0.3 \times 4.4 + 0.3 \times 4.6 = 1.96 + 1.32 + 1.38 = 4.66.$$

Increment: $C_{\text{new}} - C_{\text{base}} = 4.66 - 4.26 = 0.40$. Because the model is linear, the increment equals $\Delta \times (w_c + w_{sh} + w_{oc}) = 0.4 \times 1.0 = 0.40$, confirming internal consistency.

### 4.6 Monthly Gateway Spend Projection

Assumptions: baseline monthly spend $S_{\text{base}} = \$150$ (the documented cap level [10]); extra cost per unresolved failure $c_f = \$5$ (assumption).

Baseline extra cost:

$$E_{\text{extra}} = E[F] \times c_f = 2.16 \times 5 = \$10.8.$$

Projected baseline spend:

$$S_{\text{proj}} = 150 + 10.8 = \$160.8.$$

Improved scenario (halved $p_f$, so $E[F] = 1.08$):

$$E_{\text{extra}}' = 1.08 \times 5 = \$5.4,$$
$$S_{\text{proj}}' = 150 + 5.4 = \$155.4.$$

The projected saving is $S_{\text{proj}} - S_{\text{proj}}' = \$5.4$ per month.

### 4.7 Billing-Unit Misread

Inputs: unit-error factor $f_{\text{unit}} = 100$ (cents interpreted as dollars); corrected spend $S_{\text{corr}} = \$110$ (the baseline $\$150$ minus a $\$40$ discount, with no unit error).

Misread spend:

$$S_{\text{misread}} = f_{\text{unit}} \times S_{\text{corr}} = 100 \times 110 = \$11{,}000.$$

This reproduces the figure stated in the retraction notice [10], confirming that a cents-as-dollars misreading is arithmetically sufficient to produce it.

### 4.8 Cap-Violation Ratio (denominator: the $\$150$ cap)

Cap $C_{\text{cap}} = \$150$.

$$\frac{S_{\text{misread}}}{C_{\text{cap}}} = \frac{11{,}000}{150} = 73.3333\ldots \approx 73.3.$$

The misread spend exceeds the $\$150$ cap by a factor of $73.3$.

### 4.9 Gate Exceedance (denominator: the $\$90$ per-30-days gate)

Gate $G_{\text{gate}} = \$90$ per 30 days.

Corrected-spend exceedance:

$$\text{Exceedance} = \frac{S_{\text{corr}} - G_{\text{gate}}}{G_{\text{gate}}} \times 100 = \frac{110 - 90}{90} \times 100 = \frac{20}{90} \times 100 = 22.222\ldots\% \approx 22.2\%.$$

Misread-spend ratio against the same gate, for completeness:

$$\frac{S_{\text{misread}}}{G_{\text{gate}}} = \frac{11{,}000}{90} = 122.222\ldots \approx 122.2.$$

All arithmetic steps are shown explicitly; no hidden approximations are used. The two misread ratios ($73.3$ against the cap, $122.2$ against the gate) are distinct results with distinct denominators and are never interchangeable.

## 5. Results

The analytical derivations of Section 4 produce the quantitative outcomes listed below.

| Result | Value | Interpretation |
|--------|-------|----------------|
| **R1. Expected failures per month** | $E[F] = 2.16$ | Two to three worker-script failures are anticipated each month after self-healing mitigation, under $p_f = 0.12$, $\alpha = 0.5$. |
| **R1a. Alternative expectation (count-derived $\alpha$)** | $E[F]^{\text{counts}} \approx 1.73$ | Using $\alpha_{\text{counts}} \approx 0.599$ from the action tallies lowers the expectation. |
| **R2. Papers per active project** | $9.65$ | Each active research project contributes roughly ten papers to the corpus. |
| **R3. High-severity gap proportion** | $11.9\%$ | Five of the forty-two identified gaps are classified as high severity. |
| **R4. Baseline composite autonomy score** | $C_{\text{base}} = 4.26$ | Autonomy assessment before mitigation. |
| **R5. Improved composite autonomy score** | $C_{\text{new}} = 4.66$ | Halving the failure probability raises the score by $0.40$. |
| **R6. Projected monthly gateway spend (baseline)** | $S_{\text{proj}} = \$160.8$ | Baseline spend of $\$150$ plus $\$10.8$ of expected failure cost. |
| **R7. Projected monthly gateway spend (improved)** | $S_{\text{proj}}' = \$155.4$ | Halving the failure probability reduces the extra cost to $\$5.4$. |
| **R8. Billing-unit misread spend** | $S_{\text{misread}} = \$11{,}000$ | Interpreting cents as dollars inflates the corrected spend of $\$110$ by a factor of $100$. |
| **R9. Cap-violation ratio (denominator: $\$150$ cap)** | $73.3$-fold | The misread spend is $73.3$ times the $\$150$ cap. |
| **R9a. Gate-violation ratio (denominator: $\$90$ gate)** | $122.2$-fold | The misread spend is $122.2$ times the $\$90$ per-30-days gate. |
| **R10. Gate exceedance for corrected spend** | $22.2\%$ | The corrected spend of $\$110$ exceeds the $\$90$ gate by $22.2\%$. |
| **R11. Storage total** | $320.9\ \text{MB}$ | Aggregated storage across databases and vector indexes. |
| **R12. Failure count variance** | $\operatorname{Var}[F] = 2.0304$, $\sigma_F \approx 1.425$ | Dispersion of the monthly failure count under the binomial model. |

All values follow directly from the arithmetic steps shown in Section 4; no additional empirical measurements are introduced.

## 6. Discussion

### 6.1 Limitations

The analysis rests on explicit assumptions, each with a stated sensitivity:

1. **Baseline failure probability $p_f = 0.12$** is an assumed upper bound; no source provides a measured value. $E[F]$ is linear in $p_f$: a true value of $0.06$ halves $E[F]$ to $1.08$, and each percentage point of $p_f$ moves $E[F]$ by $0.18$ (Section 4.1).
2. **Mitigation factor $\alpha = 0.5$** is an assumption; the count-derived $\alpha_{\text{counts}} \approx 0.599$ gives $