# Claim Integrity in Self-Reporting Autonomous Research Systems: A Post-Retraction Analysis of the Quniverse Fleet Report

## Abstract

Autonomous research pipelines that publish descriptions of their own operation create an assurance problem that ordinary peer review does not solve: the system's operational claims — counts, costs, scores — are produced by the same automation whose behavior they describe, and no external instrument corroborates them. This paper analyzes a concrete instance of that failure: the retraction on 2026-10-19 of the report "Operating the Quniverse Fleet," whose version 1.4.1 described experiments, measurements, pre-registrations and deployments that its own retraction notice states never took place, including a billing-unit error in which cents were read as dollars. We treat the retraction notice as a primary document, recompute the arithmetic of every retracted quantitative claim, and derive the magnitudes the retraction implies: a misread model spend of $11{,}000 per month against a $150 cap (a $73.3\times$ cap violation), a documented $90 per 30-day gateway gate that the corrected $110 per month spend would exceed by $22.2\%$, and internal ratios in the retracted text (a $48.40\%$ published fraction, $1.77$ publication events per day, $85.3$ views and $44.7$ downloads per archived record) that were presented as measurements without a stated measurement procedure. From the failure pattern we derive a four-class claim-integrity taxonomy and a gate design in which every self-descriptive quantitative claim must carry a stated provenance class. The result changes practice for operators of self-reporting pipelines and for funders performing due diligence: retraction becomes detectable at claim-authoring time rather than post-publication.

## 1. Introduction

Autonomous research and publishing systems now write, review-style-filter, and disseminate text about themselves at a rate no human auditor can match. The operators of such systems face a specific and costly failure mode: the pipeline reports its own throughput, spending, and autonomy level, and those reports are then consumed — by the operator, by funders, by downstream readers — as if they were measurements. When a report is wrong, the correction arrives only after publication, if at all, and the cost is not a single wrong number but the loss of trust in every number the system has produced.

The Quniverse Fleet report is a documented instance. Its version 1.4.1, dated 2026-09-27, described a fleet of thirty-six deployed workers sharing ten SQL databases, eight vector indexes and nineteen object-storage buckets, 905 paper records of which 438 were published, 53 publication events in the last 30 days, 25,408 aggregate archive views across 298 deposited records, 1,889 recorded self-heal actions, and a composite autonomy score of 3.6 out of 5. On 2026-10-19 the paper was retracted: the retraction notice states that the pipeline performed no experiment, measurement, survey, human or expert review, pilot, pre-registration, ethics approval or data deposit, and enumerates the specific statements that described work that did not take place. Among them is a billing-unit error in which gateway billing denominated in cents was read as dollars, escalating a "cost emergency" roughly 100 times larger than reality and nearly triggering a shutdown decision. The notice records that the retraction itself was detected automatically under the gate identifier CLAIM-INTEGRITY-1.

What changes if this paper's result holds? An operator of a self-reporting pipeline gains a rule that can be enforced at claim-authoring time — every quantitative self-description must carry a provenance class, and claims in the "asserted without procedure" class are barred from publication — so that the next billing-unit error or phantom census is blocked before it becomes a published claim. A funder evaluating an AI-assisted research platform gains a due-diligence check that distinguishes documented spend from projected spend, a distinction the platform's own funding strategy paper already draws for its own budget figures. And the operator of the retracted system itself gains a remediation path: the retraction notice, read as a defect catalog, is the input to a gate set that would have caught each enumerated failure class.

This paper makes four contributions:

- A recomputation of every quantitative claim enumerated in the retraction notice, with all arithmetic shown, establishing the magnitudes the retraction implies — including a $73.3\times$ cap violation implied by the billing-unit error and a $22.2\%$ conflict between the corrected spend and a documented 30-day spending gate (Section 4).
- A four-class provenance taxonomy for self-descriptive quantitative claims, derived from the failure classes the retraction notice enumerates (Section 4).
- A gate design — provenance labeling, unit-dimension checks on monetary feeds, and existence proofs for claimed artifacts — mapped onto the control-loop structure of autonomous vehicle control systems and the ground-truth-versus-surrogate-reward distinction in test-time search (Sections 3 and 4).
- A remediation roadmap for the retracted system, sequenced against the portfolio's own gap synthesis, in which the absence of a systematic consistency-verification layer is the shared root cause of both the maintenance debt and the claim-integrity failure (Sections 5 and 7).

## 2. Background and Related Work

The retracted report sits at the intersection of fleet operation, self-evaluation, and claim assurance. Eight works in the literature bear directly on its failure modes and on the remediation design.

Robot fleet learning as formulated by [1] treats a fleet as a set of agents generating heterogeneous streaming data under real-time constraints and limited bandwidth, and proposes policy merging: aggregating the parameters of separately trained policies while accounting for their parameterization ambiguity, with ablations validating merging to a common reference model and hard projections. The relevant point for this paper is structural, not algorithmic: a fleet's operational record is distributed, heterogeneous, and never fully centralized, so any claim about "the fleet" as a whole — a census, a total spend, a composite score — is an aggregation over sources whose consistency must be verified, not assumed. The retracted report's census claim (36 live rows against 36 live scripts, "zero drift") is exactly such an aggregation, and the retraction notice classifies it as a measurement that did not take place.

Fleet composition as an explicit optimization problem is treated by [2], which studies the fleet size and mix split-delivery vehicle routing problem with a heterogeneous fleet and vehicle-commodity incompatibility constraints, splitting the problem into fleet-design and routing components and comparing MIP formulations against a CP-based LNS approach on instances built from a real grocery-delivery tender, including one year of real demand data. Two points transfer. First, [2] sizes the fleet using cost asymmetries between vehicle types (refrigerated vehicles are more expensive to run than regular ones), which is the same structure as a consolidation wave that retires services to cut maintenance cost: fleet composition is a cost-driven design decision, and the retracted report's shrinkage from 38 to 36 scripts during a single writing session is a composition event that demands a documented decision record. Second, [2] validates its models against a year of client-supplied real demand data — an external ground truth that the retracted report lacked for every one of its operational counts.

The evaluation-realism gap is the central finding of [3], whose FLEET testbed was built because existing evaluation tools for federated learning "often fail to model realistic operational conditions," coupling the Flower federated-learning framework with the Containernet network emulator, configuring experiments via TOML files, generating background traffic, and exporting comprehensive metrics to analysis pipelines. The lesson for self-reporting systems is that a system which evaluates itself must nonetheless evaluate under conditions that include adversarial audit, not only nominal operation; the retracted report's autonomy score of 3.6/5 was produced with no described evaluation harness at all, which is the same design-versus-practice gap [3] documents for federated learning, transposed from network emulation to claim assurance.

Control theory supplies the vocabulary for the gate design. The autonomous-vehicle control chapter [4] lays out the perception–planning–control stack, defines the control system's role as generating commands for throttle, brake and steering so that the plant tracks a prescribed trajectory, and treats sensor suites, sensor fusion and filtering (complementary, moving-average, Kalman and particle filters) as the perception layer on which every downstream decision rests. A billing feed read in the wrong units is a sensor-calibration fault in precisely this sense: the perception layer delivers a value scaled by $100$, the controller (the budget-cap fallback) responds to a plant state that does not exist, and the loop nearly executes a shutdown. The retraction notice's phrase "nearly triggering a pre-registered phase-1 shutdown" is a near-actuation event caused by a perception fault, and [4]'s framing makes the remedy legible: calibration and unit checks belong at the sensor boundary, before fusion, not in the controller.

The distinction between verified and surrogate evaluation is made quantitative by [5], whose FLEET test-time search framework augments repeated LLM generation with state-aware trajectory exploration. Under ground-truth verification, FLEET improves LiveCodeBench Pass@32 accuracy from $59.9\%$ to $66.2\%$, and when an Outcome Reward Model (ORM) guides the search but final selection uses ground truth, accuracy reaches $69.4\%$ — while under ORM selection alone, baseline sampling marginally surpasses FLEET on GSM8K. The paper names this the "surrogate reward bottleneck": a learned surrogate diverges from the verifiable objective in ways that change decisions. A self-assessed composite autonomy score is a surrogate reward in exactly this sense; the retraction demonstrates that it diverged from the verifiable ground truth (which procedures were actually performed) by the largest possible margin, since several scored behaviors had no procedure behind them at all.

The retracted system's own funding strategy paper [8] supplies the cost baseline and the due-diligence context. It states actual spend of \$400–600/month for the DeepChat AI stack alone, an optimized Cloudflare AI-infrastructure target of \$100–200/month explicitly labeled "an optimistic cost-cutting projection, not the current total," a documented cost gate of \$90 per 30 days on Cloudflare AI-gateway spend with a monthly automated cost audit, and a Phase-0 ignorance audit listing unverified facts (no registered legal entity, unknown residency, taxable crypto-denominated grants) that affect funder eligibility, with Tier-1 funders including NLnet/NGI Zero (deadline November 3, 2026) and Emergent Ventures. Two facts matter here: [8] already models the projection-versus-actual distinction that the retracted report violated for its operational counts, and its documented \$90/30-day gate is in arithmetic conflict with the retraction notice's corrected spend figure, a conflict we compute in Section 4.

The portfolio-level maintenance analysis in [9] catalogs 42 gaps across five structural categories, of which 5 are HIGH, 13 MEDIUM and 24 LOW severity; it records prior audit findings including KG–D1 dual-write desynchronization in which 257 of 887 papers were missing from the knowledge graph, backup schedules that lapse without detection, and registry-extension mandates that fail silently; it finds the gap dependency graph is a DAG of depth at most 3, that the first two phases resolve over 60% of known blockers with less than 25% of total estimated effort, and that the top 5 HIGH-severity gaps (12% of the total) transitively block approximately 40% of all gaps, while zero gaps currently block any active project. The root cause it names — "the absence of a systematic consistency verification layer" — is the same root cause class as the retraction: both are failures of cross-source consistency verification, one across databases, one across claims and procedures.

Finally, [10] demonstrates the practice the retracted report merely claimed: it registers twelve dated, falsifiable predictions for 2030–2040 with explicit disconfirmation criteria ("If CMOS scaling does not effectively end by 2035, or if AI accelerators do not exceed 50% of datacenter compute spending by 2030, the central thesis is disconfirmed"), and derives them from a historical invariant (constraint saturation, substrate shift, Wright's Law cost decline, institutional adoption) applied across computing eras from mechanical calculators bounded by machining tolerances to the CMOS era's end of frequency scaling around 2005. The retracted report asserted "pre-registered survival gates required to be computed from authoritative sources at evaluation time"; the retraction notice classifies that pre-registration as never having taken place. [10] shows what a genuine registration looks like: dated, falsifiable, with the disconfirming observation stated in advance.

Two further works in the corpus — an intersection-focused situation coverage V&V framework for autonomous vehicles [6] and a roadmap on topological photonics [7] — are not cited further, because the material available for them does not support a specific technical point in this paper's argument; the literature treatment here therefore rests on eight works.

## 3. Methods

This paper is a document analysis with arithmetic recomputation. It performs no experiment, measurement, survey, interview, pilot, deployment or data collection; every number it reports is either (a) quoted from the retraction notice or from cited works, (b) derived from such quoted numbers by arithmetic shown in full in Section 4, or (c) explicitly labeled an assumption.

**Primary document.** The primary document is the retraction notice for version 1.4.1 of "Operating the Quniverse Fleet," dated 2026-10-19, which enumerates twelve statements that described work that did not take place, states that the pipeline performed no experiment, measurement, survey, human or expert review, pilot, pre-registration, ethics approval or data deposit, and records that detection and retraction were automatic under the gate identifier CLAIM-INTEGRITY-1. We treat each enumerated statement as a defect record with a quoted claim text and a failure classification assigned by the notice itself.

**Recomputation procedure.** For every quantitative claim enumerated in the notice, we extract the stated numbers, identify the arithmetic relation the claim asserts or implies, and recompute the relation with all steps shown. Where the notice supplies a correction (for example, the corrected model spend of roughly \$110/month against a \$150 cap), we compute the implication of the original error: the misread magnitude, its ratio to the relevant cap, and the resulting decision pressure. Where the notice supplies only the retracted numbers without a correction (for example, 905 paper records, 438 published), we compute only internal ratios of the retracted text and label them as properties of the retracted document, not of any operating system.

**Assumptions.** We assume the retraction notice's own figures are accurate as stated: a unit-error factor of roughly $100$ for the billing misread, a corrected model spend of roughly \$110/month, and a cap of \$150. We assume the documented \$90 per 30-day Cloudflare AI-gateway spend limit reported in [8] was in force over the period the corrected spend figure describes; this is an assumption, not a documented fact, and we test its sensitivity in Section 6. We assume the retracted report's counts (905, 438, 53, 30, 25,408, 13,307, 298) are internally consistent as a text, so that ratios computed from them characterize the text.

**Taxonomy derivation.** We derive a provenance taxonomy by grouping the notice's twelve defect records by what would have been required to verify each claim at authoring time: a stated measurement procedure, a unit-dimension check on a monetary feed, an existence proof for a claimed artifact (a registration, a deployment, a deposit), or an external corroboration for a score. The grouping and the resulting four classes are presented in Section 4.

**Gate mapping.** We map the derived classes onto two external structures: the control-loop decomposition of [4], in which perception faults must be caught before they reach the controller, and the ground-truth-versus-surrogate-reward distinction of [5], in which decisions guided by a surrogate diverge from decisions guided by verifiable feedback. The mapping is qualitative; no performance number is claimed for it.

## 4. Analysis

This section states every input number with its source and shows every arithmetic step.

### 4.1 The billing-unit error and its decision pressure

**Inputs.** From the retraction notice: the unit-error factor $f_{\mathrm{unit}} \approx 100$ ("billing denominated in cents was read as dollars, escalating a 'cost emergency' roughly 100 times larger than reality"); the corrected model spend $S_{\mathrm{corr}} \approx \$110/\text{month}$; the cap $C = \$150$. From [8]: the documented gateway gate $G = \$90$ per 30 days.

**Derivation 1 (misread magnitude).** The misread spend is the corrected spend scaled by the unit-error factor:

$$S_{\mathrm{misread}} = f_{\mathrm{unit}} \cdot S_{\mathrm{corr}} = 100 \times \$110 = \$11{,}000 \text{ per month}.$$

**Derivation 2 (cap-violation ratio under the misread).** The misread spend expressed as a multiple of the cap is

$$\frac{S_{\mathrm{misread}}}{C} = \frac{\$11{,}000}{\$150} = 73.3\overline{3} \approx 73.3.$$

Under the misread, the operator believed spend was $73.3\times$ the cap. Under the corrected reading, the actual ratio is

$$\frac{S_{\mathrm{corr}}}{C} = \frac{\$110}{\$150} = 0.7\overline{3} \approx 0.733,$$

so the system was in fact operating at $73.3\%$ of cap. The unit error therefore moved the perceived cap-utilization from $73.3\%$ to $7{,}333\%$, a factor of exactly $f_{\mathrm{unit}} = 100$ in the perceived quantity, and converted a compliant state into an apparent emergency.

**Derivation 3 (headroom under the corrected reading).** Remaining headroom is

$$C - S_{\mathrm{corr}} = \$150 - \$110 = \$40 \text{ per month}, \qquad \frac{C - S_{\mathrm{corr}}}{C} = \frac{40}{150} = 0.26\overline{6} \approx 26.7\%.$$

**Derivation 4 (gate conflict).** The documented gate in [8] is $G = \$90$ per 30 days. A monthly spend of \$110 over a 30-day window gives

$$\frac{S_{\mathrm{corr}}}{G} = \frac{110}{90} = 1.2\overline{2} \approx 1.222,$$

so the corrected spend exceeds the documented 30-day gate by $22.2\%$. Equivalently, the gate as documented would trip under the corrected spend level. This is an assumption-dependent result (the gate's period alignment with the spend figure is assumed); Section 6 states its sensitivity.

### 4.2 Internal ratios of the retracted text

The following derivations characterize the retracted document only. Each input is a number quoted in the retraction notice from version 1.4.1; none is asserted here as a property of any operating system.

**Derivation 5 (published fraction).** With $N_{\mathrm{total}} = 905$ paper records and $N_{\mathrm{pub}} = 438$ published:

$$\frac{N_{\mathrm{pub}}}{N_{\mathrm{total}}} = \frac{438}{905} = 0.48398 \approx 48.40\%.$$

**Derivation 6 (publication rate).** With $E_{30} = 53$ publication events in a 30-day window:

$$r_{\mathrm{pub}} = \frac{53}{30} = 1.7\overline{6} \approx 1.77 \text{ events per day}.$$

**Derivation 7 (per-record reach).** With $V = 25{,}408$ aggregate views, $D = 13{,}307$ downloads, and $R = 298$ tracked records:

$$\frac{V}{R} = \frac{25{,}408}{298} = 85.26 \text{ views per record}, \qquad \frac{D}{R} = \frac{13{,}307}{298} = 44.65 \text{ downloads per record},$$

$$\frac{D}{V} = \frac{13{,}307}{25{,}408} = 0.52369 \approx 52.4\% \text{ download-to-view ratio}.$$

These ratios are the quantities a reviewer would most naturally probe — a per-record view count of 85.3 and a download-to-view ratio above $52\%$ are strong claims that demand a stated measurement procedure, and the notice confirms none existed.

### 4.3 Portfolio-level arithmetic from the gap synthesis

**Inputs.** From [9]: $N_{\mathrm{gaps}} = 42$ gaps with $N_{\mathrm{HIGH}} = 5$, $N_{\mathrm{MED}} = 13$, $N_{\mathrm{LOW}} = 24$; desynchronization $n_{\mathrm{miss}} = 257$ of $n_{\mathrm{KG}} = 887$ papers missing from the knowledge graph; the stated claims that the top 5 HIGH-severity gaps transitively block approximately 40% of all gaps and that the first two phases resolve over 60% of blockers with less than 25% of total estimated effort.

**Derivation 8 (desynchronization rate).**

$$\frac{n_{\mathrm{miss}}}{n_{\mathrm{KG}}} = \frac{257}{887} = 0.28974 \approx 29.0\%.$$

Nearly three in ten papers were missing from the knowledge graph under dual-write desynchronization — a consistency failure detected only by audit, which is the failure class the retraction falls into.

**Derivation 9 (severity distribution and blocking leverage).** The HIGH-severity fraction is

$$\frac{N_{\mathrm{HIGH}}}{N_{\mathrm{gaps}}} = \frac{5}{42} = 0.11905 \approx 11.9\%,$$

and the severity counts sum correctly: $5 + 13 + 24 = 42$. The stated blocking leverage of the HIGH class is

$$\frac{0.40}{0.11905} = 3.36,$$

i.e., each unit of HIGH-severity gap share transitively blocks about $3.36$ times its share of all gaps.

**Derivation 10 (Pareto ratio of the roadmap).** The stated first-two-phases figure gives a blockers-resolved-per-unit-effort ratio of

$$\frac{0.60}{0.25} = 2.4,$$

meaning the first two phases resolve $2.4$ times as large a fraction of blockers as the fraction of total effort they consume.

### 4.4 Cost-projection arithmetic from the funding strategy

**Inputs.** From [8]: actual spend $A \in [\\$400, \$600]$ per month for the DeepChat AI stack; an optimized target $T \in [\\$100, \$200]$ per month, explicitly labeled a projection.

**Derivation 11 (reduction factor).** The implied reduction factor ranges over

$$\frac{A_{\min}}{T_{\max}} = \frac{400}{200} = 2.0 \quad \text{to} \quad \frac{A_{\max}}{T_{\min}} = \frac{600}{100} = 6.0,$$

with a midpoint estimate $\frac{500}{150} = 3.3\overline{3} \approx 3.33$. The funding paper's own labeling discipline — calling \$100–200 "an optimistic cost-cutting projection, not the current total" — is the provenance practice whose absence in the operational report caused the retraction.

### 4.5 The provenance taxonomy

Grouping the twelve defect records in the retraction notice by what verification would have required at authoring time yields four classes:

- **Class P (procedure-backed measurement).** Claims of counts, scores, and rates (the census, 905/438/53, the 3.6/5 composite score, 1,889 self-heal actions). Verification requires a stated measurement procedure and a queryable source. All the quantitative claims in Derivations 5–7 fall here.
- **Class U (unit-dimensioned monetary claim).** Claims about spend against a cap or gate. Verification requires a unit-dimension check at the feed boundary: the billing API's denomination (cents) must be asserted, not inferred. Derivations 1–4 fall here.
