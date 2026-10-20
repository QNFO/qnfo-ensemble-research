# Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet (Version 1.8.0, Post-Publication Revision)

## Abstract

Autonomous research fleets must keep serverless worker scripts, databases, and storage buckets running while reporting reliable cost and performance metrics, yet existing treatments address fleet sizing, failure propagation, and claim validation in isolation. This revision builds an integrated analytical framework that models reliability, monetary impact, and claim-integrity auditing jointly for the Quniverse fleet, combining a Bernoulli failure-propagation model with a self-healing mitigation factor, resource-consumption aggregation, a weighted composite autonomy score, and a claim-by-claim recomputation of the figures in the fleet's retraction notice, each with explicit arithmetic and unit-dimension checks. Under an assumed per-worker monthly failure probability of $p_f=0.12$ and mitigation factor $\alpha=0.5$, the model yields an expected $E[F]=2.16$ unresolved worker-script failures per month (standard deviation $\sigma_F\approx1.425$), a corpus rate of $9.65$ papers per active project, a high-severity gap proportion of $11.9\%$, and a composite autonomy score of $4.26$ that rises to $4.66$ when the failure probability is halved. Projected monthly gateway spend is $\$160.8$ baseline and $\$155.4$ in the improved scenario. The retraction notice's billing-unit error inflates perceived spend to $\$11{,}000$ — $73.3$-fold the $\$150$ cap and, against the different baseline of the $\$90$ per-30-days gate, $122.2$-fold — while the corrected spend of $\$110$ exceeds the gate by $22.2\%$. These results give operators, funders, and auditors analytically derived levers for reliability and fiscal compliance, at TRL 2 analytical readiness.

## 1. Introduction

Platform operators of the Quniverse autonomous research fleet run a continuously active collection of thirty-six serverless worker scripts, ten SQLite databases, eight vector indexes, and nineteen object-storage buckets that generates and publishes scientific content without human intervention. Two intertwined problems currently block the fleet's value. First, unplanned downtime arises from script failures and drift between the service registry and the deployed code, and failures that escape both the self-healing layer and human notice accumulate silently — a failure class that the verifiable-AI-reliability literature calls silent failures and treats as a distinct engineering target [6]. Second, self-reported metrics have been shown to be unreliable: the fleet's retraction notice revealed a billing-unit error that inflated the perceived monthly spend to $\$11{,}000$ — far above the documented $\$90$ per-30-days cost gate — and a composite autonomy assessment of $3.6/5$ that conflicted with internal metrics. An operator who cannot trust either the failure counts or the dollar figures cannot budget, cannot set alert thresholds, and cannot demonstrate compliance to a funder.

If the fleet could reduce its unresolved failure rate, align cost reporting with the actual monetary units, and attach a provenance check to every quantitative claim it publishes, three things would change: research velocity would rise because fewer failures interrupt pipelines, operational cost would fall because failure-driven overruns would be bounded, and stakeholder trust would be restored because every published number could be recomputed from stated inputs. Conversely, if the reliability model proposed here is wrong, a month of monitoring will show it, and the operator will have lost only the cost of reading a log file.

This revision corrects and strengthens the published version. The billing-unit discussion now separates the cap-relative ratio ($73.3$-fold against the $\$150$ cap) from the gate-relative ratio ($122.2$-fold against the $\$90$ gate) so that no two ratios against different baselines can be conflated; the sensitivity statement in the limitations is derived explicitly rather than asserted; and the model-refutation threshold of Section 7.3 is stated with its derivation basis.

**Contributions.**
- **C1.** Derive a stochastic failure-propagation model and compute the expected number of unresolved worker-script failures per month, $E[F]=2.16$, with its Bernoulli variance $\operatorname{Var}[F]=2.0304$ and standard deviation $\sigma_F\approx1.425$ (Section 4.1, Results R1, R1a, R12).
- **C2.** Quantify corpus productivity ($9.65$ papers per active project) and the high-severity gap proportion ($11.9\%$) (Section 4.2–4.3, Results R2–R3).
- **C3.** Show that a $50\%$ reduction in per-worker failure probability raises the composite autonomy score from $4.26$ to $4.66$ and lowers projected monthly gateway spend from $\$160.8$ to $\$155.4$ (Section 4.5–4.6, Results R4–R7).
- **C4.** Recompute every quantitative claim of the retraction notice, separating the cap-relative ratio ($73.3$-fold against the $\$150$ cap) from the gate-relative ratio ($122.2$-fold against the $\$90$ gate) and the corrected-spend gate exceedance ($22.2\%$) (Section 4.7–4.9, Results R8–R10).
- **C5.** Specify two minimal pilots — a 30-day failure-count measurement and a billing-feed unit-dimension check — with explicit refutation thresholds, and map the results to engineering pathways (Section 7.3).

## 2. Background and Related Work

Reliability modeling for distributed and autonomous systems supplies the methodological foundation of this work, and the literature provides concrete methods and results that this paper adopts, adapts, or deliberately distinguishes itself from.

[1] develops a stochastic method for estimating the effect of water-induced shallow landslides on soil erosion in data-poor regions: sampling a frequency-size landslide distribution, stochastically distributing landslide locations across a catchment, and running Monte Carlo simulations whose median over 1,000 runs showed a $20\%$ increase in total soil loss, with post-failure erosion rates on average around $3.5$ times the pre-failure value and a bootstrap analysis over 10,000 runs assessing uncertainty. The structural lesson adopted here is that a stochastic event model plus an explicit uncertainty quantification can produce decision-relevant aggregate numbers from sparse inputs; the Bernoulli failure model of Section 3.1, by contrast, is an assumption of the present study and is not carried over from that work.

[2] presents FLEET, a federated-learning emulation and evaluation testbed that integrates the Flower federated-learning framework with the Containernet Docker-based network emulator, configured via TOML files, with metrics exported to ZMQ, CSV, or log files, so that algorithmic performance and network dynamics can be investigated jointly rather than in isolation. That joint-evaluation design goal is the same integration motive that motivates combining reliability, cost, and claim-integrity modules here; the mitigation factor $\alpha$ introduced in Section 3.1 is likewise an assumption of the present study rather than a finding of that testbed.

[3] frames reliability qualification of semiconductor devices as a sequential decision problem and shows, over 5,000 planning iterations of a Bayesian Monte Carlo tree search with EKF belief-state estimation, that characterization yield improves progressively from $20\%$ to over $54\%$ while keeping damage fractions below $0.57$ in the best successful test sequence. This demonstrates that reliability parameters are best estimated adaptively from accumulating observations rather than fixed in advance — the same principle underlies the count-derived mitigation factor $\alpha_{\text{counts}}$ of Section 4.1, which replaces an assumed constant with a quantity recomputed from the fleet's own action tallies.

[4] studies robot fleet learning via policy merging, aggregating the parameters of policies trained on distributed, heterogeneous fleet datasets while handling their parameterization ambiguity with recurrent neural networks, and contributes the Fleet-Tools benchmark for generalizable tool-use tasks. It is cited here for the fleet-level pattern it establishes: knowledge (there, policies; here, reliability and cost parameters) is aggregated across many fleet members rather than measured per member in isolation.

[5] formulates fleet size and mix split-delivery vehicle routing as modular MIP models — splitting fleet design from routing — and shows in a year-long experiment against real demand data that the Stable fleet model combined with Commodity routing outperforms a CP-based LNS approach on most instances. Its decomposition discipline (separate the fleet-composition question from the per-unit behavior question) is mirrored in this paper's separation of the failure-propagation module from the cost-aggregation module.

[6] introduces FAME, a framework combining offline formal synthesis with runtime monitoring to confront silent failures of AI components, and reports that in 100 challenging scenarios a DNN failed a safety requirement in 31 runs with no internal indication of degradation, while the FAME monitor detected 29 of those 31 silent failures, a $93.5\%$ detection rate, with zero false alarms across 100 nominal scenarios. This is the closest published analogue to the fleet's escaped-failure problem and directly motivates the claim-integrity auditing module: failures that produce no internal signal must be caught by an external check, and Section 3.4 supplies that check for quantitative claims.

[9] treats autonomous-vehicle technology from a control perspective, modeling the vehicle as a stack of perception, planning, and control subsystems and discussing coupled and de-coupled longitudinal and lateral control schemes. Its layered-architecture framing — where each layer's output is the next layer's input — supports this paper's treatment of the fleet as a chain of modules (failure propagation feeding cost aggregation feeding claim auditing) rather than as a single undifferentiated system.

[10] is the prior version of this study, whose published Results table reports $E[F]=2.16$, the count-derived alternative $E[F]^{\text{counts}}\approx1.73$, the composite scores $4.26$ and $4.66$, and the projected spends $\$160.8$ and $\$155.4$, and whose Section 7.3 sets the refutation threshold at an observed failure count deviating from $2.16$ by more than $\pm0.5$. This revision recomputes every one of those figures from first principles (Section 4) and corrects the billing-unit presentation, which conflated cap-relative and gate-relative ratios.

[11] forecasts computing-machine evolution 2026–2050 through a constraint-driven lens and documents, in its electromechanical-era section, that the Harvard Mark I's roughly 3,000 relays failed measurably during operation, so that reliability — not raw logic — was the binding constraint of that era. It also registers twelve dated falsifiable predictions and states the disconfirmation condition for its central thesis. Both moves are adopted here: reliability is treated as the binding constraint on fleet value, and Section 7.3 states an explicit refutation condition for the model.

[12] analyzes how energy-efficiency metrics became standards and concludes, from the SPEC/SERT precedent, that benchmarks carry weight under neutral stewardship because no single vendor controls them. Applied to claim integrity, the lesson is that self-reported fleet metrics need an auditing procedure whose authority does not rest on the reporting party — which is exactly the role of the recomputation protocol of Section 3.4.

[13] ranks 17 quantum computing platforms by a joules-per-solution metric computed from published specifications and finds gate speed to be the dominant factor in energy per solution, with superconducting platforms from $0.05$ to $0.71$ J/sol leading and trapped ions at $16.3$ J/sol ranking last. It is cited for its methodological pattern: comparable per-platform figures computed from stated inputs with every denominator explicit, which is the same discipline this paper applies to the fleet's cost and reliability figures.

Collectively, these works supply the building blocks — stochastic aggregation with uncertainty, joint multi-module evaluation, adaptive parameter estimation, decomposition, external failure detection, and denominator-explicit recomputation — for an integrated framework addressing reliability, cost, and claim integrity together. The specific modeling choices of this paper — the self-heal fraction, the claim-integrity taxonomy of Section 3.4, and the $50\%$ failure-reduction scenario — are assumptions of the present study; the $50\%$ reduction analyzed in Section 4.6 is an assumed scenario, not a benchmark taken from prior literature.

## 3. Methods

The analytical pipeline consists of four deterministic modules, each expressed in closed-form equations. All calculations are performed symbolically and then evaluated numerically with the input values listed in Section 4. No empirical measurements are introduced: the corpus statistics are inherited from the fleet's own accounting, and every other input is labeled an assumption.

### 3.1 Failure-Propagation Model

Each of the $N_w$ worker scripts experiences a baseline failure probability $p_f$ per month. A fraction $\alpha$ of failures are resolved automatically (self-heal). The effective unresolved-failure probability is

$$p_{\text{eff}} = p_f \times (1-\alpha).$$

The expected monthly unresolved-failure count is

$$E[F] = N_w \, p_{\text{eff}} = N_w \, p_f \, (1-\alpha).$$

Because the $N_w$ trials are treated as independent Bernoulli trials with common probability $p_{\text{eff}}$, the count $F$ follows a binomial distribution with variance

$$\operatorname{Var}[F] = N_w \, p_{\text{eff}} \, (1 - p_{\text{eff}}).$$

A count-derived alternative to the assumed $\alpha$ is obtained from the fleet's own action tallies: if $H$ self-heal actions and $X$ handoff (unresolved) actions are recorded, then

$$\alpha_{\text{counts}} = \frac{H}{H + X}.$$

### 3.2 Resource-Consumption Aggregation

Total storage $S_{\text{tot}}$ is the sum of database and vector-index sizes:

$$S_{\text{tot}} = S_{db} + S_{vi},$$

where $S_{db}=304\ \text{MB}$ (ten D1 databases) and $S_{vi}$ is the product of the vector-index row count and the per-row byte size. MB and MiB are treated as interchangeable at the precision reported (one decimal place); the difference is at most $4.9\%$ per term and is stated as an assumption of the aggregation.

### 3.3 Composite Autonomy Score

A weighted linear model combines three sub-scores:

$$C = w_c S_c + w_{sh} S_{sh} + w_{oc} S_{oc},$$

with weights $w_c=0.4$, $w_{sh}=0.3$, $w_{oc}=0.3$ taken from the original fleet assessment. Baseline sub-scores are $S_c=4.5$, $S_{sh}=4.0$, $S_{oc}=4.2$. A $50\%$ reduction in failure probability is modeled as a uniform sub-score increment $\Delta=0.4$, yielding $S_c'=4.9$, $S_{sh}'=4.4$, $S_{oc}'=4.6$.

### 3.4 Claim-Integrity Recomputation

For each quantitative claim extracted from the retraction notice the procedure is: (i) parse the quoted numbers; (ii) reconstruct the asserted arithmetic relation; (iii) recompute the relation step-by-step; (iv) apply unit-dimension checks to monetary feeds (a value quoted in dollars must be traceable to a source quoted in the same unit, and a cents-to-dollars conversion must divide by 100); and (v) assign a provenance class — Procedure-backed, Unit-dimensioned, Existence-proof, or Surrogate-reward — following the streamlined taxonomy used in the prior version of this study [10]. Every ratio reported in Sections 4.7–4.9 names its denominator explicitly, so that no two ratios against different baselines can be conflated.

## 4. Analysis

### 4.1 Expected Failures per Month and Mitigation Factor

Inputs: $N_w=36$ (fleet inventory), $p_f=0.12$ (assumption, an upper-bound monthly per-worker failure probability), $\alpha=0.5$ (assumption, the fraction of failures resolved by self-healing).

Effective failure probability:

$$p_{\text{eff}} = 0.12 \times (1-0.5) = 0.12 \times 0.5 = 0.06.$$

Expected unresolved failures:

$$E[F] = 36 \times 0.06 = 2.16.$$

**Alternative mitigation factor from counts.** The retraction notice reports $1{,}889$ self-heal actions and $1{,}264$ handoff actions. The total action count is

$$N_{\text{total}} = 1{,}889 + 1{,}264 = 3{,}153,$$

and the count-derived self-heal fraction is

$$\alpha_{\text{counts}} = \frac{1{,}889}{3{,}153} = 0.59911\ldots \approx 0.599.$$

Using $\alpha_{\text{counts}}$:

$$p_{\text{eff}}^{\text{counts}} = 0.12 \times (1-0.599) = 0.12 \times 0.401 = 0.04812,$$

$$E[F]^{\text{counts}} = 36 \times 0.04812 = 1.73232 \approx 1.73.$$

The assumed $\alpha=0.5$ therefore predicts a higher failure count (conservative choice).

**Variance and standard deviation (Bernoulli aggregation).**

$$\operatorname{Var}[F] = 36 \times 0.06 \times (1-0.06) = 36 \times 0.06 \times 0.94 = 2.0304,$$

$$\sigma_F = \sqrt{2.0304} = 1.42492\ldots \approx 1.425.$$

**Sensitivity.** $E[F]$ is linear in both $p_f$ and $(1-\alpha)$: halving $p_f$ to $0.06$ gives $E[F]=36\times0.06\times0.5=1.08$, the improved scenario used in Section 4.6. A one-percentage-point change in $p_f$ changes $E[F]$ by

$$\Delta E[F] = 36 \times 0.01 \times 0.5 = 0.18 \ \text{failures per month},$$

so a $10\%$ absolute change in $p_f$ (i.e., $\Delta p_f = 0.10$) changes $E[F]$ by $36 \times 0.10 \times 0.5 = 1.8$ failures per month; the per-percentage-point coefficient is $0.18$.

### 4.2 Papers per Active Project

Inputs: total papers $P_{\text{total}}=917$, active projects $N_{\text{proj}}=95$ (fleet accounting).

$$\frac{P_{\text{total}}}{N_{\text{proj}}}= \frac{917}{95}=9.65263158\ldots \approx 9.65\ \text{papers/project}.$$

### 4.3 High-Severity Gap Proportion

Inputs: high-severity gaps $G_{\text{high}}=5$, total gaps $G_{\text{total}}=42$ (fleet accounting).

$$\frac{G_{\text{high}}}{G_{\text{total}}}= \frac{5}{42}=0.11904762\ldots \approx 11.9\%.$$

### 4.4 Storage Aggregation

Inputs: $S_{db}=304\ \text{MB}$, vector-index rows $34{,}657$ at $512\ \text{B}$ per row.

$$S_{vi}=34{,}657 \times 512\ \text{B}=17{,}744{,}384\ \text{B}.$$

Converting to MiB ($1\ \text{MiB}=1{,}048{,}576\ \text{B}$):

$$S_{vi}= \frac{17{,}744{,}384}{1{,}048{,}576}=16.9219\ldots\ \text{MiB}\approx 16.922\ \text{MiB}.$$

Assuming MB–MiB interchangeability:

$$S_{\text{tot}} = 304 + 16.922 = 320.922 \approx 320.9\ \text{MB}.$$

### 4.5 Composite Autonomy Score

Baseline sub-scores $S_c=4.5$, $S_{sh}=4.0$, $S_{oc}=4.2$; weights $w_c=0.4$, $w_{sh}=0.3$, $w_{oc}=0.3$.

Baseline score:

$$C_{\text{base}} = 0.4\times4.5 + 0.3\times4.0 + 0.3\times4.2 = 1.8 + 1.2 + 1.26 = 4.26.$$

Improved sub-scores (adding $\Delta=0.4$): $S_c'=4.9$, $S_{sh}'=4.4$, $S_{oc}'=4.6$.

Improved score:

$$C_{\text{new}} = 0.4\times4.9 + 0.3\times4.4 + 0.3\times4.6 = 1.96 + 1.32 + 1.38 = 4.66.$$

Increment: $C_{\text{new}}-C_{\text{base}} = 0.40$.

### 4.6 Monthly Gateway Spend Projection

Assumptions: baseline monthly spend $S_{\text{base}}=\$150$ (documented cap), extra cost per unresolved failure $c_f=\$5$ (assumption).

Baseline extra cost:

$$E_{\text{extra}} = E[F] \times c_f = 2.16 \times 5 = \$10.8.$$

Projected baseline spend:

$$S_{\text{proj}} = 150 + 10.8 = \$160.8.$$

Improved scenario (halved $p_f$, so $E[F]=1.08$):

$$E_{\text{extra}}' = 1.08 \times 5 = \$5.4,$$

$$S_{\text{proj}}' = 150 + 5.4 = \$155.4.$$

### 4.7 Billing-Unit Misread

Inputs: unit-error factor $f_{\text{unit}}=100$ (cents interpreted as dollars), corrected spend $S_{\text{corr}}=\$110$ (baseline $\$150$ minus a $\$40$ discount, no unit error).

Misread spend:

$$S_{\text{misread}} = f_{\text{unit}} \times S_{\text{corr}} = 100 \times 110 = \$11{,}000.$$

### 4.8 Cap-Violation Ratio (denominator: the $\$150$ cap)

Cap $C_{\text{cap}}=\$150$.

$$\frac{S_{\text{misread}}}{C_{\text{cap}}}= \frac{11{,}000}{150}=73.3333\ldots \approx 73.3.$$

### 4.9 Gate Exceedance (denominator: the $\$90$ per-30-days gate)

Gate $G_{\text{gate}}=\$90$ per 30 days.

Corrected-spend exceedance:

$$\text{Exceedance}= \frac{S_{\text{corr}}-G_{\text{gate}}}{G_{\text{gate}}}\times100 = \frac{110-90}{90}\times100 = \frac{20}{90}\times100 = 22.222\ldots\% \approx 22.2\%.$$

Misread-spend ratio against the same gate (for completeness, with the gate named as the denominator):

$$\frac{S_{\text{misread}}}{G_{\text{gate}}}= \frac{11{,}000}{90}=122.222\ldots \approx 122.2.$$

All arithmetic steps are shown explicitly; no hidden approximations are used.

## 5. Results

The analytical derivations of Section 4 produce the quantitative outcomes listed below.

| Result | Value | Interpretation |
|--------|-------|----------------|
| **R1. Expected failures per month** | $E[F]=2.16$ | Two to three worker-script failures are anticipated each month after self-healing mitigation. |
| **R1a. Alternative expectation (count-derived $\alpha$)** | $E[F]^{\text{counts}}\approx1.73$ | Using $\alpha_{\text{counts}}\approx0.599$ lowers the expected failures. |
| **R2. Papers per active project** | $9.65$ | Each active research project contributes roughly ten papers to the corpus. |
| **R3. High-severity gap proportion** | $11.9\%$ | Five of the forty-two identified gaps are classified as high severity. |
| **R4. Baseline composite autonomy score** | $C_{\text{base}}=4.26$ | Autonomy assessment before mitigation. |
| **R5. Improved composite autonomy score** | $C_{\text{new}}=4.66$ | Halving the failure probability raises the score by $0.40$. |
| **R6. Projected monthly gateway spend (baseline)** | $S_{\text{proj}}=\$160.8$ | Baseline spend assumes a base of $\$150$ plus extra cost from expected failures. |
| **R7. Projected monthly gateway spend (improved)** | $S_{\text{proj}}'=\$155.4$ | Halving the failure probability reduces the extra cost to $\$5.4$. |
| **R8. Billing-unit misread spend** | $S_{\text{misread}}=\$11{,}000$ | Interpreting cents as dollars inflates the corrected spend by a factor of $100$. |
| **R9. Cap-violation ratio (denominator: $\$150$ cap)** | $73.3$-fold | The misread spend is $73.3$ times the $\$150$ cap. |
| **R9a. Gate-violation ratio (denominator: $\$90$ gate)** | $122.2$-fold | The misread spend is $122.2$ times the $\$90$ gate. |
| **R10. Gate exceedance for corrected spend** | $22.2\%$ | The correctly interpreted spend of $\$110$ exceeds the $\$90$ gate by $22.2\%$. |
| **R11. Storage total** | $320.9\ \text{MB}$ | Aggregated storage across databases and vector indexes. |
| **R12. Failure count variance** | $\operatorname{Var}[F]=2.0304$, $\sigma_F\approx1.425$ | Dispersion of the monthly failure count under the binomial model. |

All values follow directly from the arithmetic steps shown in Section 4; no additional empirical measurements are introduced.

## 6. Discussion

### 6.1 Limitations

The analysis rests on explicit assumptions, each with a stated sensitivity:

1. **Baseline failure probability $p_f=0.12$** is an assumed upper bound; the true distribution may differ. $E[F]$ scales linearly with $p_f$: the per-percentage-point coefficient derived in Section 4.1 is $36\times0.01\times0.5=0.18$ failures per month, so a $10\%$ absolute change in $p_f$ ($\Delta p_f=0.10$) changes $E[F]$ by $36\times0.10\times0.5=1.8$ failures per month. The result is highly sensitive to this input.
2. **Mitigation factor $\alpha=0.5$** is a conservative assumption; the count-derived value $\alpha_{\text{counts}}\approx0.599$ shows a plausible alternative that reduces $E[F]$ to $1.73$, a $20\%$ reduction relative to $2.16$. The result is moderately sensitive to $\alpha$.
3. **Cost per failure $c_f=\$5$** is a simplifying constant; downstream costs (e.g., lost compute time) are omitted. Projected spend scales linearly with $c_f$.
4. **Baseline monthly spend $S_{\text{base}}=\$150$** reflects the documented cap rather than observed fluctuations.
5. **Unit-error factor $f_{\text{unit}}=100$** captures the specific cents-to-dollars mistake; other unit inconsistencies are not modeled.
6. **Linear weighting in the composite autonomy score** assumes additive contributions of sub-scores; interactions are ignored.
7. **Independence of failures** under the Bernoulli formulation; correlated failures could alter $E[F]$ and $\sigma_F$.
8. **Binomial dispersion** assumes equal per-worker failure probabilities; heterogeneity across workers would inflate the variance relative to $\operatorname{Var}[F]=2.0304$.

### 6.2 Falsification Conditions and Potential Failure Modes

The central claim — that the fleet's unresolved failure load is near $E[F]=2.16$ per month under the assumed parameters, and that halving $p_f$ improves the composite score and reduces spend — would be falsified if a 30-day monitoring window showed an observed failure count $F_{\text{obs}}$ deviating from $2.16$ by more than $\pm0.5$, i.e., $F_{\text{obs}}<1.66$ or $F_{\text{obs}}>2.66$, or if the billing conversion yielded a factor other than $100$. The $\pm0.5$ threshold is set at roughly one-third of a standard deviation ($\sigma_F\approx1.425$), so it is a deliberately tight test: it refutes the parameterization, not the binomial family, and a count within $\pm0.5$ would still be consistent with a wide range of $(p_f,\alpha)$ pairs. A second failure mode is structural: if failures are correlated (for example, a shared dependency fails and takes down many workers at once), the binomial variance underestimates the tail risk and the expected count may hold while monthly variance does not. A third is the cost attribution: if observed spend stays near $\$160.8$ after the failure-probability reduction is implemented, the linear cost model $E_{\text{extra}}=E[F]\,c_f$ is insufficient, even if the failure model itself is correct.

### 6.3 Open Questions

- How does correlation among worker failures affect the aggregate failure count and its variance?
- What is the impact of dynamic workload scaling on the per-failure cost $c_f$?
- Can automated unit-dimension verification be extended to other resource-type feeds (e.g., compute-seconds, storage-bytes) without manual rule definition?
- Does the count-derived $\alpha_{\text{counts}}$ remain stable across months, or does it drift with workload composition?

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended Users and Decision Impact

- **Platform operators** can use the expected-failure estimate ($E[F]=2.16$, $\sigma_F\approx1.425$) to size monitoring infrastructure, schedule preventive maintenance, and set alerts for self-heal effectiveness; the alert threshold for self-heal effectiveness changes from an implicit one to the explicit count-derived fraction $\alpha_{\text{counts}}\approx0.599$.
- **Funders and auditors** can rely on the corrected spend figures to assess compliance with the $\$90$ per-30-days cost gate and allocate budgets accurately; the compliance decision changes from trusting a self-reported dollar figure to recomputing it from raw cents-denominated usage.
- **Developers of autonomous agents** can treat the composite autonomy score improvement (from $4.26$ to $4.66$ under the assumed $\Delta=0.4$) as a concrete target when refining self-healing mechanisms and claim-integrity pipelines.

### 7.2 Technology Readiness Level

The work is purely analytical and has not been peer reviewed; it therefore resides at **TRL 2** (concept formulation and basic analytical studies) on the NASA Technology Readiness Level scale. No hardware, prototype, or deployment evidence supports a higher level, and analytical work of this kind cannot exceed TRL 3 in any case.

### 7.3 Minimal Next Experiment

A pilot study would:

1. **Measure** the actual number of worker-script failures over a 30-day window, recording both raw failure events and self-heal actions.
2. **Verify** the billing feed by extracting raw usage in cents and converting to dollars, checking for unit-dimension consistency.

If the observed failure count deviates from $2.16$ by more than $\pm0.5$ (i.e., outside $[1.66,\,2.66]$) or the billing conversion yields a factor other than $100$, the model assumptions would be refuted. A single month suffices to test the parameterization; three consecutive months would be needed to test the variance claim R12, because a single draw cannot distinguish binomial dispersion from correlated failure bursts.

### 7.4 Engineering Constraints

- **Logging infrastructure** must capture per-worker failure timestamps and self-heal outcomes with at least minute granularity; without it, neither $E[F]$ nor $\alpha_{\text{counts}}$ can be recomputed.
- **Billing API access** is required to retrieve raw usage in the original monetary unit (cents); the unit-dimension check of Section 3.4 is impossible on dollar-rounded feeds.
- **Configuration control** to adjust $p_f$ (e.g., by deploying updated health-check scripts) is needed to test the $50\%$ reduction scenario.

These constraints are derived directly from the inputs and equations of Section