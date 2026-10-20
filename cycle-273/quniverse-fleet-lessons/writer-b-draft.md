# Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet: A Corrected Analytical Reassessment

## Abstract

Autonomous research fleets—collections of serverless worker scripts, databases, and storage buckets that generate and publish scientific content without continuous human oversight—must simultaneously maintain operational reliability, control cloud spending, and produce self-reported metrics that can be trusted. The Quniverse deployment illustrates what happens when the third requirement fails: its earlier analytical paper was retracted because it described measurements that were never performed, and its own quantitative claims contained unit and provenance errors. No published framework currently integrates fleet failure modeling, cost projection, and claim-integrity auditing for such a deployment. This paper constructs that integration from explicit assumptions alone: worker-script failures are modeled as Bernoulli trials with a self-heal mitigation factor, corpus statistics are aggregated, and every quantitative claim from the retracted paper is recomputed with all arithmetic shown. The corrected model yields $E[F]=2.16$ expected worker-script failures per month under the assumed mitigation factor $\alpha=0.5$, a corpus rate of $9.65$ papers per active project, a high-severity gap proportion of $11.9\%$, and projected monthly gateway spend of $\$160.8$ baseline versus $\$155.4$ under a halved failure probability. Two reported errors in the retracted paper are corrected with shown arithmetic: the mitigation factor $\alpha=0.5$ is an assumption, not a value derivable from the retraction-notice counts (which would give $\alpha\approx0.599$), and the billing-unit misread of $\$11{,}000$ exceeds the documented $\$90$ per-30-days gate by a factor of $122.2$, while the corrected spend of $\$110$ exceeds that gate by $22.2\%$—the retracted abstract attached the $22.2\%$ figure to the misread spend, a unit inconsistency. The framework remains at TRL 2 and defines the pilots that would test it.

## 1. Introduction

Operators of autonomous research platforms face a problem that conventional reliability engineering does not cover. A fleet of serverless worker scripts must stay online and produce research output, but the same fleet also generates the numbers by which its own performance is judged—failure counts, spending figures, throughput statistics—and those numbers can be wrong in ways that no amount of uptime monitoring detects. The Quniverse deployment makes the cost of this failure concrete: its earlier analytical paper was retracted because it described experiments, measurements, and reviews that never took place, and a retraction notice disclosed that several self-reported quantitative claims, including a billing figure inflated to $\$11{,}000$ per month by a unit error, were produced without any measurement procedure [12]. An operator who cannot distinguish a measured number from an asserted one cannot decide whether to provision monitoring, whether the fleet is within its spending gate, or whether a claimed reliability improvement actually occurred.

The stakes are decision-relevant in three ways. First, reliability: if the fleet's expected failure rate after self-healing mitigation is roughly two failures per month, a monitoring and maintenance schedule can be sized accordingly; if the rate is unknown, provisioning is guesswork. Second, cost: a billing-unit error that multiplies a spend figure by $100$ turns a compliant $\$110$ monthly spend into an apparent $\$11{,}000$ spend, which would trigger cap-violation escalations against a $\$150$ cap and gate checks against a documented $\$90$ per-30-days limit that the corrected figure does not actually fail in the way reported. Third, trust: the retraction of the fleet's own analytical paper shows that claim-integrity failures propagate to the analysis layer itself, so any replacement framework must recompute its own numbers from stated inputs rather than inherit them.

This paper is a post-retraction analytical reassessment. It keeps everything in the retracted analysis that survives recomputation, corrects two reported errors that do not, and states every input as either a cited corpus statistic or an explicit assumption. The deployment context is fixed by the retracted paper's own description: thirty-six worker scripts, ten SQLite databases, eight vector indexes, and nineteen object-storage buckets handling thousands of paper records [12].

**Contributions.**

- **C1.** Derive the expected monthly worker-script failure count under a Bernoulli model with self-heal mitigation, $E[F]=2.16$, and show that the mitigation factor $\alpha=0.5$ is an assumption whose count-derived alternative would be $\alpha\approx0.599$ (Section 4.1).
- **C2.** Compute the corpus statistics: $9.65$ papers per active project and an $11.9\%$ high-severity gap proportion (Section 4.2–4.3).
- **C3.** Derive the composite autonomy score baseline $C_{\text{base}}=4.26$ and its improvement to $C_{\text{new}}=4.66$ under a modeled $50\%$ failure-probability reduction, and the corresponding spend projections $\$160.8$ and $\$155.4$ (Section 4.4–4.6).
- **C4.** Correct the retracted paper's billing-gate claim: the misread spend of $\$11{,}000$ exceeds the $\$90$ per-30-days gate by a factor of $122.2$, whereas the corrected spend of $\$110$ exceeds that gate by $22.2\%$; the retracted abstract paired the $22.2\%$ figure with the misread spend (Section 4.7–4.9).
- **C5.** Define a provenance taxonomy for self-reported fleet claims and two minimal pilots—one failure-count pilot, one billing unit-dimension check—that would confirm or refute the model, with the refutation thresholds derived from the model's own variance (Section 4.1, Section 7).

## 2. Background and Related Work

**Reliability modeling of networked infrastructure.** The survey of reliability modeling and analysis techniques for communication networks divides the field into analytical methods, simulation tools, and formal methods, and documents that a study of cloud computing vulnerabilities counted about $172$ unique cloud computing outage incidents between 2008 and 2012, with major causes including insecure interfaces and APIs, data loss and leakages, and hardware failures [1]. That taxonomy justifies this paper's choice of an analytical model for the Quniverse fleet: the fleet is a small, cloud-native system whose failure causes (API faults, hardware failures) match the documented outage causes, and an analytical treatment is the cheapest tier of the three that still produces checkable numbers. The same survey describes higher-order-logic theorem proving as a route to logically sound proofs that a system satisfies its requirements [1], which is the standard of rigor to which a claim-integrity audit aspires even though this paper reaches only arithmetic-level verification.

**Gradual degradation versus isolated shocks.** Trajectory-aware reliability modeling of democratic systems argues that failures in complex systems often emerge through gradual degradation and the propagation of stress across interacting components rather than through isolated shocks [2]. Applied to a worker-script fleet, this warns that the Bernoulli trial model of Section 3 treats each failure as independent when the true failure process may be correlated through shared dependencies; Section 6 carries this as an explicit limitation and open question.

**Autonomous research platforms and self-repair.** AgentRxiv introduces collaborative autonomous research in which LLM agents build on prior results, and its experimentation pipeline uses an LLM-based automatic repair mechanism (the mle-solver) to fix code errors encountered during execution [3]. That mechanism is the same functional role as the Quniverse fleet's self-heal actions, so AgentRxiv's architecture supports treating self-heal as a real, countable mitigation event rather than a modeling fiction. AgentRxiv also reports that parallel experimentation accelerates discovery in wall-clock time but incurs higher computational costs due to redundant experiments [3], the same cost-throughput tension that motivates the spend projections in Section 4.6.

**Efficiency as a first-class objective.** The case that autonomous research systems should be evaluated on the efficiency of the solution-search process, not only final outcome quality, is made by showing that search efficiency and final outcome quality are empirically distinct dimensions and that no fixed search structure is universally most efficient, motivating budget-adaptive policies [4]. This supports the paper's decision to model cost per failure $c_f$ explicitly rather than treat failures as costless events: a fleet that fails often is worse even if it eventually publishes.

**Claim-evidence architecture.** EviGraph argues that unsupported claims and inconsistencies in autonomous research outputs are partly architectural, arising because sequential pipelines do not explicitly maintain or validate the evolving evidence structure, and it enforces evidence-chain validity over a typed research graph, achieving the highest overall score ($86.45\%$) on ARC-Bench-ML while leading in Code Execution and Result Analysis [5]. EviGraph's diagnosis matches the Quniverse failure mode: the retracted paper's claims outran its evidence because no graph or ledger connected each number to a measurement. The provenance classes defined in Section 3 are a lightweight, single-fleet version of EviGraph's evidence-graph discipline.

**Experience-guided piloting.** The Experimental Experience Modeling (EEM) framework decides whether further resource investment in a candidate experimental direction is justified, and when historical experience is insufficient it acquires the missing decision-relevant experience through a targeted, low-cost pilot before deciding [6]. This is exactly the justification for the two minimal pilots in Section 7: the fleet's failure-rate and billing-unit questions lack sufficient historical experience, so low-cost pilots are the prescribed next step rather than full-scale instrumentation. EEM's evaluation on ARC-Bench, with an overall score computed as $0.25\,\mathrm{CD}+0.25\,\mathrm{CE}+0.50\,\mathrm{RA}$, also provides a precedent for weighted composite scoring of the kind the composite autonomy score uses.

**Survival and hazard formulations.** The reliability framework for wireless mobile communications models transmission success probability using reliability block diagrams, with the survival function $R(t)$ and the hazard function $\lambda(t)$ calculated from individual life distributions and joint distributions used to derive system reliability [7]. Although the Quniverse fleet is modeled here with a simpler per-period Bernoulli count, the survival/hazard framing defines the natural extension: if per-worker failure times were recorded, $E[F]$ could be replaced by a hazard-based estimate, and Section 7's pilot is designed to collect exactly the timestamps that would enable it.

**Load- and network-aware reliability optimization.** For microservice placement, a network-aware service reliability model captures the impact of network load and routing on service reliability, and the proposed SRP algorithm with a fully protected path mechanism reduces the number of failures by up to $29\%$ compared to benchmark algorithms in simulation [9]. The $29\%$ figure is the closest published benchmark for the magnitude of a mitigation intervention, and it brackets the assumed $50\%$ mitigation effectiveness used here from below; the related load-dependent node reliability model that captures the relationship between failure probabilities and workloads [9] is the pattern a workload-aware extension of Section 4.1 would follow.

**Independent assurance layers.** ARIS is a research harness built on the conservative assumption that long-horizon research performed by a single agent is unreliable by default, and it implements a cross-model experiment-integrity audit that checks for specific failure modes including model-derived reference labels, self-normalized scores, phantom results (claimed numbers that do not match actual output files), dead-code or unused-metric inflation, and scope inflation [11]. Its result-to-claim stage assigns each claim a verdict of supported, partially supported, or invalidated, and propagates integrity status so that claims with failed audits cannot be marked fully supported [11]. This two-stage structure is the direct template for the provenance classes and claim recomputation in Section 3: every retracted claim here receives a verdict derived from recomputation, and a claim that fails recomputation cannot be retained.

**Claim-level auditing precedent.** The BQNN audit demonstrates the discipline this paper applies to itself: it audited a quantum neural network benchmarking paper and rated the multi-platform benchmarking claim as SUSTAINED while rating the advantage claims as NOT SUSTAINED, finding the statistical evidence insufficient ($N=55$, overlapping error bars) and the noise-as-advantage claim resting on a single cherry-picked image [13]. The lesson adopted here is that a single analysis can contain claims of very different provenance, so each claim must be audited individually rather than the paper as a whole.

**Falsifiable prediction registration.** The history-constrained forecast of computing machine evolution registers twelve dated falsifiable predictions for 2030–2040 with explicit disconfirmation conditions—for example, that the central thesis is disconfirmed if CMOS scaling does not effectively end by 2035 or if AI accelerators do not exceed $50\%$ of datacenter compute spending by 2030 [14]. Section 7's refutation thresholds follow this pattern: each pilot states in advance the observation that would refute the model.

**The retracted baseline.** The retracted Quniverse paper supplies the deployment inventory (thirty-six worker scripts, ten SQLite databases, eight vector indexes, nineteen object-storage buckets), the corpus statistics, the composite autonomy weights, and the pilot design [12]. Its retraction—for describing experiments, measurements, or reviews that never took place—is the reason this paper recomputes rather than inherits every number, and its two reported errors are corrected in Sections 4.1 and 4.7–4.9.

## 3. Methods

The method is analytical recomputation under explicitly stated assumptions. Four modules are used.

**Module 1: Failure-propagation model.** Each of the $N_w=36$ worker scripts is treated as a Bernoulli trial per month with baseline failure probability $p_f=0.12$. A fraction $\alpha$ of failures are resolved by self-heal actions without human intervention, so the effective unresolved-failure probability is

$$p_{\text{eff}} = p_f\,(1-\alpha).$$

The expected monthly count of unresolved failures is

$$E[F] = N_w \, p_f \, (1-\alpha).$$

Two inputs require provenance statements. The value $p_f=0.12$ is an assumption carried over from the retracted analysis; no source in this paper's corpus derives it from logged failure events, and it is treated as an upper-bound estimate. The mitigation factor $\alpha=0.5$ is likewise an assumption. The retracted paper asserted that $\alpha=0.5$ was "taken from the retraction notice counts (1,889 self-heal actions, 1,264 handoff actions)" [12]; that derivation is incorrect and is corrected in Section 4.1, where the count-derived value is computed and shown to differ from $0.5$.

**Module 2: Resource-consumption aggregation.** Database storage is $S_{db}=304\ \text{MB}$ across ten D1 databases. Vector-index storage is computed from $34{,}657$ records at $512\ \text{B}$ each:

$$S_{vi} = 34{,}657 \times 512\ \text{B},$$

evaluated in Section 4.2. Total storage is $S_{db}+S_{vi}$.

**Module 3: Composite autonomy score.** The score is a weighted sum

$$C = w_c S_c + w_{sh} S_{sh} + w_{oc} S_{oc},$$

with weights $w_c=0.4$, $w_{sh}=0.3$, $w_{oc}=0.3$ carried from the original assessment [12]. Baseline sub-scores are $S_c=4.5$, $S_{sh}=4.0$, $S_{oc}=4.2$. A modeled $50\%$ reduction in per-worker failure probability is represented by adding $\Delta=0.4$ to each sub-score, giving $S_c'=4.9$, $S_{sh}'=4.4$, $S_{oc}'=4.6$. The mapping from failure-probability reduction to sub-score increment is a modeling convention, not a measured relationship; it is carried from the retracted analysis and flagged as an assumption.

**Module 4: Claim-integrity recomputation.** For every quantitative claim in the retracted paper, the procedure is: (i) extract the quoted numbers; (ii) identify the asserted arithmetic relation; (iii) recompute the relation with every arithmetic step shown; (iv) apply a unit-dimension check to monetary feeds; (v) assign a provenance class. The provenance classes are:

- **Procedure-backed**: the number follows from a stated measurement or counting procedure.
- **Unit-dimensioned**: the number's monetary or physical unit is verified against the raw feed.
- **Existence-proof**: the number's referent is shown to exist (e.g., a file, a database row).
- **Surrogate-reward**: the number is a modeled or proxy quantity with no direct measurement behind it.

This taxonomy is a single-fleet adaptation of the claim-verdict structure of ARIS, which assigns supported, partially supported, or invalidated verdicts and propagates audit status so that failed claims cannot be marked fully supported [11], and of EviGraph's enforcement of evidence-chain validity [5].

All calculations are performed symbolically and evaluated numerically with every step shown in Section 4. No experiment, measurement, or simulation is performed by this paper; the only empirical quantities are the corpus statistics inherited from the retracted paper's description of the deployment [12], and each is labeled with its source. Where a number stands in for data no source gives, it is labeled an assumption in the text.

## 4. Analysis

### 4.1 Expected Failures per Month and the Corrected Mitigation Factor

Inputs: $N_w=36$ worker scripts [12], $p_f=0.12$ (assumption), $\alpha=0.5$ (assumption).

The retracted paper claimed that $\alpha=0.5$ was taken from the retraction-notice counts of $1{,}889$ self-heal actions and $1{,}264$ handoff actions [12]. Recomputing that derivation:

$$N_{\text{total}} = 1{,}889 + 1{,}264 = 3{,}153,$$

$$\alpha_{\text{counts}} = \frac{1{,}889}{3{,}153} = 0.59911\ldots \approx 0.599.$$

The counts, if used at all, would give a self-heal fraction of $\alpha_{\text{counts}}\approx0.599$, not $0.5$. The reported error is therefore confirmed: $\alpha=0.5$ is not derivable from those counts. This paper treats $\alpha=0.5$ as a conservative assumption and reports the count-derived alternative as a sensitivity case. Under the assumption $\alpha=0.5$:

$$p_{\text{eff}} = p_f \times (1-\alpha) = 0.12 \times 0.5 = 0.06,$$

$$E[F] = N_w \times p_{\text{eff}} = 36 \times 0.06 = 2.16.$$

Sensitivity to the mitigation factor: with $\alpha = \alpha_{\text{counts}} = 0.599$,

$$1-\alpha = 0.401,\qquad E[F] = 36 \times 0.12 \times 0.401 = 36 \times 0.04812 = 1.7323.$$

So the count-derived mitigation factor would lower the expected failure count from $2.16$ to approximately $1.73$; the assumption $\alpha=0.5$ is the conservative (higher-failure) choice.

Dispersion: treating each worker as an independent Bernoulli trial with probability $p_{\text{eff}}=0.06$,

$$\operatorname{Var}[F] = N_w\, p_{\text{eff}}\,(1-p_{\text{eff}}) = 36 \times 0.06 \times 0.94 = 2.0304,$$

$$\sigma_F = \sqrt{2.0304} = 1.4249.$$

The standard deviation of the monthly count, $\sigma_F \approx 1.42$, exceeds the mean $E[F]=2.16$ minus the refutation half-width proposed in the retracted pilot ($\pm0.5$) [12]; this has consequences for the pilot design, taken up in Section 7.

### 4.2 Papers per Active Project

Inputs: $P_{\text{total}}=917$ papers, $N_{\text{proj}}=95$ active projects (corpus statistics from [12]).

$$\frac{P_{\text{total}}}{N_{\text{proj}}} = \frac{917}{95} = 9.652631\ldots \approx 9.65 \text{ papers per project}.$$

### 4.3 High-Severity Gap Proportion

Inputs: $G_{\text{high}}=5$ high-severity gaps, $G_{\text{total}}=42$ total gaps (corpus statistics from [12]).

$$\frac{G_{\text{high}}}{G_{\text{total}}} = \frac{5}{42} = 0.119047\ldots \approx 11.9\%.$$

### 4.4 Storage Aggregation

Inputs: $S_{db}=304\ \text{MB}$ (ten D1 databases [12]); $34{,}657$ vector-index records at $512\ \text{B}$ each [12].

$$S_{vi} = 34{,}657 \times 512\ \text{B} = 17{,}744{,}384\ \text{B}.$$

Converting to MiB ($1\ \text{MiB} = 1{,}048{,}576\ \text{B}$):

$$S_{vi} = \frac{17{,}744{,}384}{1{,}048{,}576} = 16.922\ \text{MiB}.$$

Total storage:

$$S_{\text{total}} = 304 + 16.922 = 320.922\ \text{MiB} \approx 320.9\ \text{MB}.$$

### 4.5 Composite Autonomy Score: Baseline and Improvement

Inputs: $S_c=4.5$, $S_{sh}=4.0$, $S_{oc}=4.2$; weights $w_c=0.4$, $w_{sh}=0.3$, $w_{oc}=0.3$ [12].

Baseline:

$$C_{\text{base}} = 0.4 \times 4.5 + 0.3 \times 4.0 + 0.3 \times 4.2 = 1.8 + 1.2 + 1.26 = 4.26.$$

Improved sub-scores (assumption: $\Delta=0.4$ per sub-score under a halved failure probability): $S_c'=4.9$, $S_{sh}'=4.4$, $S_{oc}'=4.6$.

$$C_{\text{new}} = 0.4 \times 4.9 + 0.3 \times 4.4 + 0.3 \times 4.6 = 1.96 + 1.32 + 1.38 = 4.66.$$

The increment is $C_{\text{new}} - C_{\text{base}} = 4.66 - 4.26 = 0.40$, which follows algebraically from $\Delta \times (w_c + w_{sh} + w_{oc}) = 0.4 \times 1.0 = 0.4$.

### 4.6 Monthly Gateway Spend Projection

Assumptions: baseline monthly spend $S_{\text{base}}=\$150$ (set at the documented cap level [12]); extra cost per unresolved failure $c_f=\$5$ (assumption, not measured).

Baseline extra cost:

$$E_{\text{extra}} = E[F] \times c_f = 2.16 \times 5 = \$10.8.$$

Projected baseline spend:

$$S_{\text{proj}} = S_{\text{base}} + E_{\text{extra}} = 150 + 10.8 = \$160.8.$$

Note that this projection already exceeds the $\$150$ cap by $\$10.8$ under the assumed failure cost; the exceedance ratio is $160.8/150 = 1.072$, i.e., $7.2\%$ over the cap.

Improved scenario (halved $p_f$, so $E[F] = 36 \times 0.06 \times 0.5 = 1.08$):

$$E_{\text{extra}}' = 1.08 \times 5 = \$5.4,\qquad S_{\text{proj}}' = 150 + 5.4 = \$155.4.$$

The saving is $\$160.8 - \$155.4 = \$5.4$ per month, i.e., $5.4/160.8 = 3.36\%$ of the baseline projection.

### 4.7 Billing-Unit Misread

Inputs: unit-error factor $f_{\text{unit}}=100$ (the retraction notice documents a billing-unit error that inflated perceived spend to $\$11{,}000$ [12]); corrected spend $S_{