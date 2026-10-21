# Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet (Post-Retraction Revision)

## Abstract
Autonomous research fleets must keep serverless worker scripts, databases, and storage buckets operational while publishing cost and performance metrics that outsiders can trust. Existing studies treat fleet sizing, failure propagation, and claim validation separately, leaving operators without a unified decision framework. This paper presents an integrated analytical model that jointly captures reliability, monetary impact, and claim-integrity auditing for the Quniverse fleet, and it corrects two quantitative errors identified in the published version: a billing-unit conflation in which a 73.3-fold cap ratio was presented alongside a 22.2% gate exceedance without separating denominators, and a mitigation factor α = 0.5 that is now derived from the retraction notice's own counts (1,889 self-heal actions, 1,264 handoff actions), giving α = 1,889/3,153 ≈ 0.5991. With N_w = 36 workers and p_f = 0.12, the model yields E[F] = 1.732 unresolved failures per month (σ_F ≈ 1.284), 9.65 papers per active project, an 11.9% high-severity gap proportion, and a composite autonomy score of 4.26 rising to 4.66 when p_f is halved. The billing-unit error inflates perceived spend to $11,000: 73.3× the $150 cap (an excess of 72.3×) and 122.2× the $90 per-30-day gate, while the corrected spend of $110 exceeds the gate by 22.2%. The framework lets operators size monitoring, budget accurately, and enforce claim integrity; it remains analytical and unreviewed, at TRL 1–2.

## 1. Introduction
Platform operators of the Quniverse autonomous research fleet run a continuously active collection of thirty-six serverless worker scripts, ten SQLite databases, eight vector indexes, and nineteen object-storage buckets that generate and publish scientific content without human intervention. Two intertwined problems currently block the fleet's value. First, unplanned downtime arises from script failures and drift between the service registry and the deployed code; failures that escape both the self-healing layer and human notice accumulate silently. Second, self-reported metrics may be unreliable: the fleet's own publication was retracted because it described quantitative results that its derivations and sources did not support, and the retraction notice itself contains a billing-unit conflation and an underived mitigation factor. An operator who cannot trust either the failure counts or the dollar figures cannot budget, cannot set alert thresholds, and cannot demonstrate compliance to a funder.

The cost of these problems is concrete. A misread billing unit turned a $110 monthly spend into a perceived $11,000 spend, which would trigger a 73.3-fold apparent violation of the fleet's $150 cap and invite unnecessary intervention; conversely, an underived mitigation factor understates or overstates the expected failure burden by up to 25% (E[F] = 2.16 under α = 0.5 versus 1.732 under the count-derived α ≈ 0.5991). If the fleet can reduce its unresolved failure rate, align cost reporting with the actual monetary units, and attach a provenance check to every quantitative claim it publishes, three things change: research velocity rises because fewer failures interrupt pipelines, operational cost falls because failure-driven overruns are bounded, and stakeholder trust is restored because every published number can be recomputed from stated inputs. Conversely, if the reliability model proposed here is wrong, a month of monitoring will show it, and the operator will have lost only the cost of reading a log file.

This revision corrects the two confirmed errors of the published version. The mitigation factor is no longer assumed; it is derived from the retraction notice's action counts. The billing analysis now names the denominator of every ratio explicitly, separating the cap-relative ratio (73.3×), the cap-relative excess (72.3×), the gate-relative ratio (122.2×), and the corrected-spend gate exceedance (22.2%), which the published abstract had juxtaposed without distinction.

**Contributions.**
- **C1.** Derive a Bernoulli failure-propagation model with a count-derived mitigation factor α = 1,889/3,153 ≈ 0.5991 and compute the expected number of unresolved worker-script failures per month, E[F] = 1.732, with variance Var[F] = 1.6485 and standard deviation σ_F ≈ 1.284 (Section 4.1).
- **C2.** Quantify corpus productivity (9.65 papers per active project) and the high-severity gap proportion (11.9%) (Sections 4.2–4.3).
- **C3.** Show that halving the per-worker failure probability lowers the expected failure count from 1.732 to 0.866 and projected monthly gateway spend from $158.66 to $154.33, and raises the composite autonomy score from 4.26 to 4.66 (Sections 4.5–4.6).
- **C4.** Recompute every quantitative claim of the retraction notice with explicit denominators, separating the cap-relative ratio (73.3× against the $150 cap), the cap-relative excess (72.3×), the gate-relative ratio (122.2× against the $90 gate), and the corrected-spend gate exceedance (22.2%) (Sections 4.7–4.9).
- **C5.** Specify a minimal pilot — a 30-day failure-count measurement and a billing-feed unit-dimension check — with explicit refutation thresholds (Section 7.3).

## 2. Background and Related Work
Analytical reliability modeling provides the methodological foundation of this study, and the emerging literature on autonomous research agents supplies both the failure modes and the auditing patterns that the model must capture.

The survey of reliability modeling in communication networks [1] organizes the field into analytical, simulation, and formal methods, and reports that about 172 unique cloud-computing outage incidents occurred between 2008 and 2012, with major causes including insecure interfaces, data loss, and hardware failures. That taxonomy justifies this paper's choice of a closed-form analytical model: the fleet's failure processes are simple enough for exact Bernoulli arithmetic, and formal methods would add assurance the current data cannot support. The same survey notes that higher-order-logic theorem proving can produce logically sound proofs that a system satisfies its requirements, a standard of assurance that claim-integrity auditing approximates in a weaker, arithmetic form.

Wireless reliability modeling [7] demonstrates the survival-function and hazard-function machinery (R(t), λ(t)) used to predict system reliability from component life distributions, and builds system reliability from reliability block diagrams spanning physical, medium-access, network, and application layers. This paper borrows the block-diagram philosophy in miniature: the fleet's reliability is composed of a per-worker failure probability and a mitigation layer, each treated as a separate block with its own parameter.

Microservice reliability [9] is the closest systems analogue to the fleet's serverless architecture. Its reliability model explicitly couples failure probability to workload, and its placement he exploit — the SRP algorithm with a fully protected path mechanism — reduces the number of failures by up to 29% compared with benchmark algorithms in simulation. The 29% figure is a useful calibration point for this paper's mitigation factor: the count-derived α ≈ 0.5991 implies a 59.9% automatic-resolution rate, which is plausible for a self-healing layer but must be verified against observed counts rather than assumed.

On the autonomous-research side, AgentRxiv [3] shows that LLM-based automatic repair mechanisms (its mle-solver module fixes code errors encountered during execution) are already a standard component of research agents, and that parallel experimentation accelerates discovery but incurs higher computational cost due to redundant work. This supports modeling the fleet's self-heal layer as a distinct action class with its own count, exactly the H and X quantities used in Section 4.1.

Efficiency in autonomous research [4] argues that a system that finds an excellent solution only after years of computation or billions of dollars in experiments has limited practical value, and proposes budget-adaptive policies that allocate search effort dynamically. This reframes the fleet's $90 per-30-day gate not as an arbitrary constraint but as an instance of the budget dimension that [4] argues should be a first-class evaluation objective.

EviGraph [5] diagnoses the failure mode that led to the fleet's retraction: autonomous systems propagate weak assumptions, unsupported claims, and experimental inconsistencies into final manuscripts because they are organized as sequential pipelines without explicit validation of the evidence chain. Its remedy — a typed graph of problems, hypotheses, experiments, findings, and claims, with repair agents operating on weak claim–evidence links — achieved the highest overall score (86.45%) on the ARC-Bench-ML benchmark. The claim-integrity recomputation of Sections 4.7–4.9 is a lightweight, arithmetic-only version of the same principle.

Experimental Experience Modeling [6] addresses the decision of which experiments are worth running: when historical experience is insufficient, it acquires a targeted, low-cost pilot before committing resources. Section 7.3's minimal pilot follows this pattern — a 30-day failure count is exactly the low-cost acquisition of the experience needed to test the model's central parameter.

ARIS [11] provides the most direct auditing template. Its experiment-integrity audit checks five failure modes, including self-normalized scores (metrics whose denominators derive from the model's own predictions), phantom results (claimed numbers that do not match actual output files), and scope inflation; its result-to-claim stage assigns each claim one of three verdicts — supported, partially supported, or invalidated — and propagates integrity status so that claims with failed audits cannot be marked fully supported. The billing-unit error corrected in this revision is precisely a self-normalization/denominator failure: a ratio was quoted against one denominator ($150 cap) in a sentence whose percentage implied another ($90 gate). ARIS's verdict taxonomy is adopted in Section 3.4.

Two QNFO analyses supply the institutional context. The prior version of this very study [12] reports the result set that this revision recomputes — E[F] = 2.16 under the old assumed α, the 73.3-fold cap ratio, and the 22.2% gate exceedance — and its retraction demonstrates that even a purely analytical paper requires every published number to be recomputable from stated inputs. The BQNN audit [13] shows the audit discipline at work on physical claims: it rates a multi-platform benchmarking methodology as SUSTAINED while rating advantage claims as NOT SUSTAINED because the statistical evidence is insufficient (N = 55, overlapping error bars) and the circuit is fully separable and classically simulable. The lesson for this paper is that a single audit must be able to sustain some claims while rejecting others, rather than wholesale accepting or rejecting a result set.

Finally, the computing-evolution forecast [14] identifies the invariant dynamic constraint saturation → substrate shift → Wright's Law cost decline → institutional adoption across every computing era, from the Harvard Mark I's ~3,000 failing relays to the end of Dennard scaling around 2005. The fleet's $150 cap is a small-scale instance of a saturated constraint; Section 6 discusses what a substrate shift would mean for the cost model.

Collectively, these works supply the reliability formalism [1,7,9], the autonomous-agent failure taxonomy [3,4,5,6], the audit patterns [11,12,13], and the economic framing [4,14] for an integrated framework that addresses reliability, cost, and claim integrity together.

## 3. Methods
The analytical pipeline consists of four deterministic modules, each expressed in closed form. All calculations are performed symbolically and then evaluated numerically with the input values listed in Section 4. No empirical measurements are introduced; every input is either stated in the retraction notice, carried from the prior version of this study [12], or explicitly labeled an assumption.

### 3.1 Failure-Propagation Model
Each of the N_w worker scripts experiences a baseline failure probability p_f per month. A fraction α of failures are resolved automatically (self-heal). The effective unresolved-failure probability is
$$p_{\text{eff}} = p_f (1-\alpha).$$
The expected monthly unresolved-failure count is
$$E[F] = N_w p_{\text{eff}} = N_w p_f (1-\alpha).$$
Because the N_w trials are independent Bernoulli trials with common probability p_eff, the count F follows a binomial distribution with variance
$$\operatorname{Var}[F] = N_w p_{\text{eff}} (1 - p_{\text{eff}}).$$

The mitigation factor is derived from operational counts rather than assumed. If H self-heal actions and X handoff (unresolved) actions are recorded over the same period, then
$$\alpha = \frac{H}{H + X}.$$
This derivation is the principal correction to the published version, which assumed α = 0.5 without derivation. The retraction notice reports H = 1,889 and X = 1,264, so α is computed in Section 4.1. The assumed value α = 0.5 is retained only as a conservative sensitivity bound.

### 3.2 Resource-Consumption Aggregation
Total storage S_tot is the sum of database and vector-index sizes:
$$S_{\text{tot}} = S_{db} + S_{vi},$$
where S_db = 304 MB (ten D1 databases) and S_vi is the product of the vector-index row count and the per-row byte size. MB and MiB are treated as interchangeable at the reported precision (one decimal place); the conversion error is bounded by 5% and is stated as an assumption.

### 3.3 Composite Autonomy Score
A weighted linear model combines three sub-scores:
$$C = w_c S_c + w_{sh} S_{sh} + w_{oc} S_{oc},$$
with weights w_c = 0.4, w_sh = 0.3, w_oc = 0.3 taken from the fleet's internal assessment. Baseline sub-scores are S_c = 4.5, S_sh = 4.0, S_oc = 4.2. A 50% reduction in failure probability is modeled as a uniform sub-score increment Δ = 0.4, yielding S_c' = 4.9, S_sh' = 4.4, S_oc' = 4.6. The linear form ignores interactions between sub-scores; this limitation is listed in Section 6.

### 3.4 Claim-Integrity Recomputation
For each quantitative claim extracted from the retraction notice, following the audit pattern of ARIS's result-to-claim mapping [11], we: (i) parse the quoted numbers; (ii) reconstruct the asserted arithmetic relation; (iii) recompute the relation step by step; (iv) apply unit-dimension checks to monetary feeds — a value quoted in dollars must be traceable to a source quoted in the same unit, and a cents-to-dollars conversion must divide by 100; and (v) assign each recomputed claim a verdict of supported, partially supported, or invalidated, in the three-verdict taxonomy of [11]. Every ratio reported in Sections 4.7–4.9 names its denominator explicitly, which prevents the conflation of distinct baselines that constituted the published billing-unit error.

## 4. Analysis
All arithmetic steps are shown explicitly; no hidden approximations are used.

### 4.1 Expected Failures per Month and the Count-Derived Mitigation Factor
Inputs: N_w = 36 (fleet registry, per [12]); p_f = 0.12 (assumed per-worker monthly failure probability, carried from [12]); H = 1,889 self-heal actions and X = 1,264 handoff actions (retraction notice counts).

**Mitigation factor from counts.**
$$N_{\text{total}} = H + X = 1{,}889 + 1{,}264 = 3{,}153,$$
$$\alpha = \frac{1{,}889}{3{,}153} = 0.599114\ldots \approx 0.5991.$$
$$1 - \alpha = \frac{1{,}264}{3{,}153} = 0.400886\ldots \approx 0.4009.$$

**Effective failure probability.**
$$p_{\text{eff}} = 0.12 \times 0.400886 = 0.0481063.$$

**Expected unresolved failures.**
$$E[F] = 36 \times 0.0481063 = 1.731828 \approx 1.732.$$

**Variance and standard deviation.**
$$\operatorname{Var}[F] = 36 \times 0.0481063 \times (1 - 0.0481063) = 1.731828 \times 0.9518937 = 1.648523,$$
$$\sigma_F = \sqrt{1.648523} = 1.28395 \approx 1.284.$$

**Conservative bound (the published assumption).** If α = 0.5 is used instead,
$$p_{\text{eff}}^{(0.5)} = 0.12 \times 0.5 = 0.06, \quad E[F]^{(0.5)} = 36 \times 0.06 = 2.16,$$
$$\operatorname{Var}[F]^{(0.5)} = 36 \times 0.06 \times 0.94 = 2.0304, \quad \sigma_F^{(0.5)} = \sqrt{2.0304} = 1.4249 \approx 1.425.$$
The count-derived factor therefore lowers the expected failure count by 2.16 − 1.732 = 0.428 failures per month, a 19.8% reduction ((0.428/2.16) × 100 = 19.815%).

**Sensitivity.** E[F] is linear in both p_f and (1 − α). Halving p_f to 0.06 gives E[F] = 36 × 0.06 × 0.400886 = 0.865922 ≈ 0.866. A one-percentage-point change in p_f changes E[F] by 36 × 0.01 × 0.400886 = 0.144 failures per month. A change of the mitigation factor by Δα changes E[F] by −36 × 0.12 × Δα = −4.32 Δα; for example, reverting from α = 0.5991 to the unsupported α = 0.5 (Δα = −0.0991) raises E[F] by 4.32 × 0.0991 = 0.428, matching the difference above.

### 4.2 Papers per Active Project
Inputs: total papers P_total = 917, active projects N_proj = 95 (both from [12]).
$$\frac{P_{\text{total}}}{N_{\text{proj}}} = \frac{917}{95} = 9.6526 \approx 9.65 \text{ papers/project}.$$

### 4.3 High-Severity Gap Proportion
Inputs: high-severity gaps G_high = 5, total gaps G_total = 42 (from [12]).
$$\frac{G_{\text{high}}}{G_{\text{total}}} = \frac{5}{42} = 0.119048 \approx 11.9\%.$$

### 4.4 Storage Aggregation
Inputs: S_db = 304 MB; vector-index rows 34,657 at 512 B per row (from [12]).
$$S_{vi} = 34{,}657 \times 512 \text{ B} = 17{,}744{,}384 \text{ B}.$$
Convert to MiB (1 MiB = 1,048,576 B):
$$S_{vi} = \frac{17{,}744{,}384}{1{,}048{,}576} = 16.92236 \text{ MiB} \approx 16.922 \text{ MiB}.$$
Assuming MB–MiB interchangeability:
$$S_{\text{tot}} = 304 + 16.922 = 320.922 \approx 320.9 \text{ MB}.$$

### 4.5 Composite Autonomy Score
Baseline sub-scores S_c = 4.5, S_sh = 4.0, S_oc = 4.2; weights w_c = 0.4, w_sh = 0.3, w_oc = 0.3.
$$C_{\text{base}} = 0.4 \times 4.5 + 0.3 \times 4.0 + 0.3 \times 4.2 = 1.8 + 1.2 + 1.26 = 4.26.$$
Improved sub-scores (adding Δ = 0.4): S_c' = 4.9, S_sh' = 4.4, S_oc' = 4.6.
$$C_{\text{new}} = 0.4 \times 4.9 + 0.3 \times 4.4 + 0.3 \times 4.6 = 1.96 + 1.32 + 1.38 = 4.66.$$
Increment: C_new − C_base = 4.66 − 4.26 = 0.40.

### 4.6 Monthly Gateway Spend Projection
Assumptions: documented cap S_cap = 150 dollars; extra cost per unresolved failure c_f = 5 dollars (both from [12]).

Baseline extra cost (count-derived α):
$$E_{\text{extra}} = 1.731828 \times 5 = 8.65914 \approx \$8.66.$$
Projected baseline spend:
$$S_{\text{proj}} = 150 + 8.66 = \$158.66.$$

Improved scenario (halved p_f, so E[F] = 0.865922):
$$E_{\text{extra}}' = 0.865922 \times 5 = 4.32961 \approx \$4.33,$$
$$S_{\text{proj}}' = 150 + 4.33 = \$154.33.$$
Reduction: 158.66 − 154.33 = \$4.33 per month.

For reference, under the published (unsupported) α = 0.5 the same formulas give E_extra = 2.16 × 5 = \$10.80 and S_proj = \$160.80; the count-derived factor lowers the projected spend by \$2.14.

### 4.7 Billing-Unit Misread
Inputs: unit-error factor f_unit = 100 (cents interpreted as dollars); corrected spend S_corr = \$110 (both from [12]).
$$S_{\text{misread}} = f_{\text{unit}} \times S_{\text{corr}} = 100 \times 110 = \$11{,}000.$$

### 4.8 Cap-Violation Ratio and Excess
Cap C_cap = \$150. Two distinct quantities must be separated, which the published version failed to do:

Ratio (misread spend as a multiple of the cap):
$$\frac{S_{\text{misread}}}{C_{\text{cap}}} = \frac{11{