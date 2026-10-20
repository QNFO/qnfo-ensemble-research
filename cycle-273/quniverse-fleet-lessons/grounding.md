# Grounding block - source: rem-rev-beb0d1ac-6130-4e69-8cca-da5a32e43ae2

## Research idea

Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet. This paper is retracted: it described experiments, measurements or reviews as done that never took place. See the retraction notice.

Post-publication revision of the published paper "Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet" (version 1.5.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Abstract: the billing-unit error 'exceeds the documented $90 per 30 days gate by 22.2%' alongside a '73.3× cap violation'. (confirmed by a second model)
2. α = 0.5 is 'taken from the retraction notice counts (1,889 self-heal actions, 1,264 handoff actions)'. (confirmed by a second model)

## Existing paper under revision (remediation only)

# Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet

## Abstract
Autonomous research fleets such as the Quniverse deployment must balance operational reliability, cost efficiency, and the integrity of self‑reported quantitative claims. Existing literature provides methods for fleet‑size optimization, failure‑propagation analysis, and claim‑validation, yet no integrated analytical framework addresses all three aspects simultaneously. We fill this gap by (i) constructing a stochastic failure‑propagation model for the serverless worker scripts, (ii) aggregating resource‑consumption metrics, (iii) projecting cost impacts of failure rates, and (iv) recomputing every quantitative claim enumerated in the retraction notice to expose unit‑error and consistency failures. The model predicts **2.16 expected failures per month** after self‑healing mitigation, a production rate of **9.65 papers per active project**, and a high‑severity gap proportion of **11.9 %**. Incorporating a 50 % reduction in per‑worker failure probability raises the composite autonomy score from the baseline **4.26** to **4.66** and lowers the projected monthly gateway spend from **\$160.8** to **\$155.4**. A billing‑unit error identified in the retraction inflates the perceived spend to **\$11 000 per month**, a **73.3 ×** cap violation, and exceeds the documented **\$90 per 30 days** gate by **22.2 %**. These results inform operators, funders, and auditors about concrete levers for improving reliability and preventing claim‑integrity failures while remaining at **TRL 2** analytical readiness.

## 1. Introduction
Researchers and platform operators who depend on continuous, automated generation and publication of scientific content confront a dual problem: (1) maintaining a cloud‑native fleet of serverless functions that remains operational without frequent human intervention, and (2) trusting the fleet’s self‑reported metrics for cost, throughput, and autonomy. In the Quniverse deployment, thirty‑six worker scripts, ten SQLite databases, eight vector indexes, and nineteen object‑storage buckets must stay online while handling thousands of paper records. We assume that drift between the service registry and deployed scripts leads to unplanned downtime and that the composite autonomy assessment is **3.6 / 5**. Simultaneously, a retraction notice disclosed that several self‑reported quantitative claims were produced without any measurement procedure, including a billing‑unit error that inflated the perceived monthly spend to **\$11 000**. If the fleet could (i) reduce failure rates, (ii) align cost reporting with actual units, and (iii) embed provenance checks for every self‑descriptive claim, research velocity would increase, operational costs would fall, and trust in the platform would be restored.

**Contributions.**  
- **C1.** Derive an analytical failure‑propagation model and compute the expected number of failures per month (Section 4, Result R1).  
- **C2.** Quantify papers per active project and high‑severity gap proportion using corpus statistics (Section 4, Results R2–R3).  
- **C3.** Show that a 50 % reduction in per‑worker failure probability raises the composite autonomy score from **4.26** to **4.66** and reduces projected gateway spend (Section 4, Results R4–R5).  
- **C4.** Recompute every quantitative claim listed in the retraction notice, exposing a **73.3 ×** cap violation (Section 4, Results R6–R9).  
- **C5.** Propose two minimal pilots—one to validate the failure‑rate model, the other to verify unit‑dimension checks on billing feeds—and map the results to engineering pathways (Section 7).

## 2. Background and Related Work
*Robot fleet learning* demonstrates that heterogeneous data streams and limited bandwidth require explicit aggregation checks; the paper notes that “the data heterogeneity and total amount of the data are becoming as much of a challenge as a benefit” [1]. This motivates our consistency verification for fleet‑wide counts.  

*Fleet‑size optimization for split‑delivery routing* shows that “beyond routing their vehicles at the least cost, goods carriers often want to know what is the best fleet to use” [2]. We adapt this insight to determine the optimal number of worker scripts for a target throughput.  

*Federated‑learning testbeds* address how distributed research infrastructure can be evaluated in a controlled, reproducible setting before deployment [3]. The Quniverse instruction‑set versioning parallels this concern for controlled evaluation, and it motivates our claim‑integrity taxonomy for self‑descriptive fleet metrics.  

*Control strategies for autonomous vehicles* treat the vehicle as a plant driven by a dedicated control system that must track a prescribed trajectory [4]. We use this plant–controller framing as an analogy: a billing‑unit error acts like a calibration fault in the sensing layer that propagates to the actuation of spending decisions, justifying our focus on unit‑dimension checks.  

*FLEET for text generation* studies how generation trajectories can be improved by exploiting logit entropy during decoding [5]. Its separation of ground‑truth verification from surrogate reward signals mirrors the gap we formalize between verified operational metrics and self‑reported claims.  

*Intersection‑focused verification* develops a situation‑coverage verification and validation framework for autonomous vehicles, implemented in the CARLA simulator [6]. Its focus on validating behavior at high‑risk decision points underscores the need for rigorous checks at the fleet’s own high‑risk gate, namely cost‑cap enforcement.  

  

*QNFO funding strategy* documents a monthly AI‑stack spend of **\$400–\$600** and a target of **\$100–\$200** per month, providing the cost baseline for our economic analysis [8].  

*QNFO gap synthesis* enumerates **42** gaps, of which **5** are high severity, and reports a DAG depth $\le$ 3 for dependency resolution [9]. These statistics are used to compute the high‑severity gap proportion and to contextualize the root‑cause analysis.  

*Claim‑integrity taxonomy* demonstrates how to register dated, falsifiable predictions with explicit disconfirmation criteria [10]. This work supplies the template for our provenance‑class labeling of self‑descriptive quantitative claims.

## 3. Methods
Our analytical pipeline consists of four modules:

1. **Failure‑Propagation Model.** Each worker script is a Bernoulli trial with baseline failure probability $p_f$. Expected monthly failures are $E[F]=N_w \times p_f \times (1-\alpha)$, where $\alpha$ is the self‑heal mitigation factor. Baseline values $N_w=36$, $p_f=0.12$, $\alpha=0.5$ are taken from the retraction notice counts (1,889 self‑heal actions, 1,264 handoff actions) and treated as upper‑bound estimates.  

2. **Resource‑Consumption Aggregation.** Database size $S_{db}=304\ \text{MB}$ (ten D1 databases) and vector‑index size $S_{vi}=34{,}657 \times 512\ \text{B}=16.9\ \text{MB}$ are summed to obtain total storage.  

3. **Composite Autonomy Score.** The score $C$ is a weighted sum $C = w_c S_c + w_{sh} S_{sh} + w_{oc} S_{oc}$ with weights $w_c=0.4$, $w_{sh}=0.3$, $w_{oc}=0.3$ (from the original assessment). Baseline sub‑scores $S_c=4.5$, $S_{sh}=4.0$, $S_{oc}=4.2$ are used; a 50 % reduction in failure probability is modeled by adding $\Delta=0.4$ to each sub‑score.  

4. **Claim‑Integrity Re‑Computation.** For every quantitative claim listed in the retraction notice we (i) extract the quoted numbers, (ii) identify the asserted arithmetic relation, and (iii) recompute the relation with all steps shown. Unit‑dimension checks are applied to monetary feeds, and provenance classes are assigned (Procedure‑backed, Unit‑dimensioned, Existence‑proof, Surrogate‑reward).  

All calculations are performed symbolically and then evaluated numerically. No empirical measurements beyond the cited corpus statistics are introduced.

## 4. Analysis
### 4.1 Expected Failures per Month
Inputs: $N_w=36$, $p_f=0.12$, $\alpha=0.5$.

\[
p_{\text{eff}} = p_f \times (1-\alpha) = 0.12 \times 0.5 = 0.06
\]

\[
E[F] = N_w \times p_{\text{eff}} = 36 \times 0.06 = 2.16
\]

### 4.2 Papers per Active Project
Inputs: $P_{\text{total}}=917$, $N_{\text{proj}}=95$.

\[
\frac{P_{\text{total}}}{N_{\text{proj}}}= \frac{917}{95}=9.65263158 \approx 9.65
\]

### 4.3 High‑Severity Gap Proportion
Inputs: $G_{\text{high}}=5$, $G_{\text{total}}=42$.

\[
\frac{G_{\text{high}}}{G_{\text{total}}}= \frac{5}{42}=0.11904762 \approx 11.9\%
\]

### 4.4 Composite Autonomy Score Baseline
Inputs: $S_c=4.5$, $S_{sh}=4.0$, $S_{oc}=4.2$, $w_c=0.4$, $w_{sh}=0.3$, $w_{oc}=0.3$.

\[
C_{\text{base}} = 0.4\times4.5 + 0.3\times4.0 + 0.3\times4.2 = 1.8 + 1.2 + 1.26 = 4.26
\]

### 4.5 Composite Autonomy Score After Improvement
New sub‑scores: $S_c'=4.9$, $S_{sh}'=4.4$, $S_{oc}'=4.6$.

\[
C_{\text{new}} = 0.4\times4.9 + 0.3\times4.4 + 0.3\times4.6 = 1.96 + 1.32 + 1.38 = 4.66
\]

### 4.6 Monthly Gateway Spend Projection
Assumptions: baseline monthly spend $S_{\text{base}}=150\ \$$, extra cost per failure $c_f=5\ \$$.

Baseline extra cost:
\[
E_{\text{extra}} = E[F]\times c_f = 2.16 \times 5 = 10.8\ \$
\]

Projected spend:
\[
S_{\text{proj}} = S_{\text{base}} + E_{\text{extra}} = 150 + 10.8 = 160.8\ \$
\]

If $p_f$ is halved, $E[F]$ becomes $1.08$ and $E_{\text{extra}}=5.4\ \$$, yielding $S_{\text{proj}}=155.4\ \$$.

### 4.7 Billing‑Unit Error Misread
Inputs: unit‑error factor $f_{\text{unit}}=100$, corrected spend $S_{\text{corr}}=110\ \$$.

\[
S_{\text{misread}} = f_{\text{unit}} \times S_{\text{corr}} = 100 \times 110 = 11{,}000\ \$
\]

### 4.8 Cap‑Violation Ratio Under Misread
Cap $C=150\ \$$.

\[
\frac{S_{\text{misread}}}{C} = \frac{11{,}000}{150}=73.3\overline{3}\approx 73.3
\]

Corrected ratio:
\[
\frac{S_{\text{corr}}}{C}= \frac{110}{150}=0.733\approx 0.733
\]

## 5. Results
The analytical derivations of Section 4 yield the following quantitative outcomes.

| Result | Value | Interpretation |
|--------|-------|----------------|
| **R1. Expected failures per month** | $E[F]=2.16$ | On average two to three worker‑script failures are anticipated each month after self‑healing mitigation. |
| **R2. Papers per active project** | $9.65$ papers/project | Each active research project contributes roughly ten papers to the corpus. |
| **R3. High‑severity gap proportion** | $11.9\%$ | Five of the forty‑two identified gaps are classified as high severity. |
| **R4. Baseline composite autonomy score** | $C_{\text{base}}=4.26$ | The fleet’s autonomy assessment before mitigation. |
| **R5. Improved composite autonomy score** | $C_{\text{new}}=4.66$ | A 50 % reduction in per‑worker failure probability raises the score by $0.40$. |
| **R6. Projected monthly gateway spend (baseline)** | $S_{\text{proj}}=\$160.8$ | Baseline spend assumes a base of $\$150$ plus extra cost from expected failures. |
| **R7. Projected monthly gateway spend (improved)** | $S_{\text{proj}}=\$155.4$ | Halving the failure probability reduces the extra cost to $\$5.4$. |
| **R8. Billing‑unit misread spend** | $S_{\text{misread}}=\$11{,}000$ | Interpreting cents as dollars inflates the reported spend by a factor of $100$. |
| **R9. Cap‑violation ratio (misread)** | $73.3$‑fold | The misread spend exceeds the \$150 cap by $73.3$ times; the correctly interpreted spend is $0.733$‑fold the cap. |

All values follow directly from the arithmetic steps shown in Section 4; no additional empirical measurements are introduced.

## 6. Discussion
### 6.1 Limitations
The analysis rests on several explicit assumptions:

1. **Failure probability $p_f$** is taken as $0.12$ from the retraction notice; the true underlying distribution may differ.  
2. **Self‑heal mitigation factor $\alpha$** is fixed at $0.5$, implying that half of failures are automatically resolved; real mitigation effectiveness could be higher or lower.  
3. **Cost per failure $c_f$** is assumed to be $\$5$; actual downstream costs (e.g., lost compute time) are not modeled.  
4. **Baseline monthly spend $S_{\text{base}}$** is set to $\$150$ based on the documented cap; actual spend may fluctuate due to workload variations.  
5. **Unit‑error factor $f_{\text{unit}}$** is $100$, reflecting the specific billing‑unit mistake identified; other unit inconsistencies are not considered.  

Sensitivity analysis (not shown) indicates that the expected failure count scales linearly with $p_f$ and $(1-\alpha)$, while the autonomy score changes linearly with the added sub‑score $\Delta=0.4$ per sub‑component.

### 6.2 Potential Failure Modes
The main claim—that reducing $p_f$ by 50 % improves autonomy and reduces spend—would be falsified if empirical monitoring over a full month showed:

* An observed failure count $F_{\text{obs}}$ **significantly greater** than $2.16$ despite the mitigation, **or**  
* No measurable reduction in spend after implementing the failure‑probability reduction, i.e., $S_{\text{obs}} \approx \$160.8$ unchanged.

Such observations would indicate that the Bernoulli failure model or the cost attribution is insufficient.

### 6.3 Open Questions
* How does failure correlation across workers affect the aggregate failure count?  
* What is the impact of dynamic workload scaling on $c_f$?  
* Can more granular billing logs reveal additional unit‑dimension errors beyond the identified factor of $100$?

## 7. Practical Implications and Engineering Pathways
### 7.1 Intended Users and Decision Impact
* **Platform operators** can use the expected‑failure estimate to provision monitoring resources and schedule preventive maintenance.  
* **Funders and auditors** can rely on the corrected spend figures to assess compliance with the \$150 cap and to allocate budgets more accurately.  
* **Developers of autonomous agents** can incorporate the autonomy‑score improvement as a target metric when refining self‑healing mechanisms.

### 7.2 Technology Readiness Level
The work is purely analytical, peer‑review‑free, and therefore resides at **TRL 2** (concept formulation and basic analytical studies).

### 7.3 Minimal Next Experiment
A pilot study would:

1. **Measure** the actual number of worker‑script failures over a 30‑day window, recording both raw failure events and self‑heal actions.  
2. **Verify** the billing feed by extracting raw usage in cents and converting to dollars, checking for unit‑dimension consistency.

If the observed failure count deviates from $2.16$ by more than $\pm0.5$ or the billing conversion yields a factor other than $100$, the model assumptions would be refuted.

### 7.4 Engineering Constraints
* **Logging infrastructure** must capture per‑worker failure timestamps and self‑heal outcomes.  
* **Billing API access** is required to retrieve raw usage in the original monetary unit (cents).  
* **Configuration control** to adjust $p_f$ (e.g., by deploying updated health‑check scripts) is needed to test the 50 % reduction scenario.

### 7.5 Projected Cost Bounds (Assumptions Stated)
Assuming the baseline spend $S_{\text{base}}=\$150$, cost per failure $c_f=\$5$, and the derived $E[F]$ values:

* **Baseline projection:** $S_{\text{proj}} = \$150 + 2.16 \times \$5 = \$160.8$.  
* **Improved projection:** $S_{\text{proj}} = \$150 + 1.08 \times \$5 = \$155.4$.

These bounds hold provided the failure probability and mitigation factor remain as modeled.

### 7.6 Risks and Misuse Paths
* **Over‑reliance on the model** could lead operators to ignore real‑world anomalies not captured by the Bernoulli assumption.  
* **Misinterpretation of the autonomy score** as a definitive safety guarantee may obscure underlying architectural weaknesses.  
* **Incorrect unit handling** in other subsystems could propagate similar billing errors if not systematically audited.

Mitigation strategies include periodic empirical validation (Section 7.3) and automated unit‑dimension checks integrated into the deployment pipeline.

## 8. Conclusion
An integrated analytical framework has been constructed to assess reliability, cost, and claim integrity for the Quniverse autonomous research fleet. By modeling worker‑script failures as Bernoulli trials with self‑heal mitigation, aggregating resource consumption, and recomputing all self‑reported quantitative claims, the study identifies concrete levers for improvement:

* Expected monthly failures are modest ($2.16$) but non‑trivial, suggesting targeted reliability engineering.  
* A 50 % reduction in per‑worker failure probability yields a measurable uplift in the composite autonomy score ($4.26 \rightarrow 4.66$) and a modest cost saving ($\$160.8 \rightarrow \$155.4$).  
* A billing‑unit error inflates perceived spend by $73.3$‑fold, underscoring the necessity of unit‑dimension validation.

The results are ready for validation at **TRL 2** and provide a clear roadmap for pilots that can de‑risk the assumptions and guide the fleet toward higher autonomy and fiscal compliance.

## Version History

- Version 1.4.0 (2026-09-27, from 1.3.0): Correct Appendix B live-census list: drop retired qnfo-goal-author and qnfo-skills-mcp (flagged by CMD RED TEAM 2026-09-28 as an undisclosed internal contradiction). Optional: refresh Appendix A same-day counts.
- Version 1.4.2 (2026-10-19, from 1.4.1): retracted
- Version 1.4.2 (2026-10-19, from 1.4.1): retracted
- Version 1.5.0 (2026-10-19, from 1.4.2): revised against the current literature, re-reviewed and re-verified. new sections: Abstract; Introduction; Background and Related Work; Methods; Analysis; Results. references 0 -> 9. length 619 -> 2989 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.1-proportionate-notice). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 10 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Robot Fleet Learning via Policy Merging. arXiv:2310.01362v3. https://arxiv.org/abs/2310.01362v3
[2] Fleet Size and Mix Split-Delivery Vehicle Routing. arXiv:1612.01691v1. https://arxiv.org/abs/1612.01691v1
[3] FLEET: A Federated Learning Emulation and Evaluation Testbed for Holistic Research. arXiv:2509.00621v2. https://arxiv.org/abs/2509.00621v2
[4] Control Strategies for Autonomous Vehicles. arXiv:2011.08729v3. https://arxiv.org/abs/2011.08729v3
[5] FLEET: From Logits Entropy to Enhanced Trajectories in Text Generation. arXiv:2609.27657v1. https://arxiv.org/abs/2609.27657v1
[6] Intersection focused Situation Coverage-based Verification and Validation Framework for Autonomous Vehicles Implemented in CARLA. arXiv:2112.14706v2. https://arxiv.org/abs/2112.14706v2
[8] https://papers.qnfo.org/papers/funding-strategy-2026-08-13. QNFO: QNFO Funding Strategy — Verified Funder Landscape & Shortlist.
[9] https://papers.qnfo.org/papers/consilient-gap-synthesis. QNFO: A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio.
[10] https://papers.qnfo.org/papers/computing-machines. QNFO: Computing After Silicon: A History-Constrained Forecast of Computing Machine Evolution, 2026-2050.

## Appendix A. Divergence report
| Divergent Claim | Draft A (Operating the Quniverse Fleet) | Draft B (Claim Integrity Analysis) | Resolution Choice |
|-----------------|------------------------------------------|------------------------------------|-------------------|
| Composite autonomy score baseline (4.26) and improvement to 4.66 | Presented with full derivation (Section 4.4–4.5) | Not addressed | Retain (A) because it is fully derived from cited weights and sub‑scores. |
| Billing‑unit error misread spend ($11 000) and cap‑violation ratio (73.3×) | Not present | Derived from retraction notice (Section 4.7–4.8) | Retain (B) because it is directly recomputed from the retraction notice and uses only cited inputs. |
| Gate conflict (22.2 % exceedance of \$90/30‑day gate) | Not present | Derived in Section 4.9 | Retain (B) for the same reason as above. |


| Minimal next experiment (failure‑rate pilot) | Proposed in Section 7 (A) | Proposed in Section 7 (B) with different focus | Both retained as separate pilots (failure‑rate pilot and unit‑dimension verification pilot). |
| Provenance taxonomy | Not present | Developed in Section 4.12 (B) | Retain (B) as it is a logical derivation from the retraction notice. |

All other quantitative claims are convergent (identical in both drafts) and therefore kept unchanged.

## Appendix B. Claim attribution
| Claim ID | Section | Source(s) |
|----------|---------|-----------|
| C1 | 4.1 | Draft A (baseline $p_f$, $\alpha$) |
| C2 | 4.2 | Draft A (total papers = 917, projects = 95) |
| C3 | 4.3 | Draft A (high‑severity gaps = 5, total = 42) |
| C4 | 4.4 | Draft A (sub‑scores and weights) |
| C5 | 4.5 | Draft A (sub‑score increase $\Delta=0.4$) |
| C6 | 4.6 | Draft A (cost per failure $=5\$$) |
| C7 | 4.7 | Draft B (unit‑error factor $=100$, corrected spend $=110\$$) |
| C8 | 4.8 | Draft B (cap $=150\$$) |
| C12 | 7 | Both drafts (failure‑rate pilot) |
| C13 | 7 | Draft B (unit‑dimension verification pilot) |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1612.08910 | Reliability Modeling and Analysis of Communication Networks
arXiv:2604.20127 | Trajectory-Aware Reliability Modeling of Democratic Systems
arXiv:2503.18102 | AgentRxiv: Towards Collaborative Autonomous Research
arXiv:2607.24647 | Efficiency Matters in Autonomous Research
arXiv:2608.04738 | EviGraph: Evidence-Guided Autonomous Research Agents
arXiv:2609.39392 | Experimental Experience Modeling for Autonomous Research
arXiv:1811.12271 | Reliability Modeling, Analysis and Prediction of Wireless Mobile Communications
arXiv:2603.11468 | Stage-Adaptive Reliability Modeling for Continuous Valence-Arousal Estimation
arXiv:2405.18001 | Network-Aware Reliability Modeling and Optimization for Microservice Placement
arXiv:2301.01850 | Bayesian Weapon System Reliability Modeling with Cox-Weibull Neural Network
arXiv:2605.03042 | ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration

## QNFO corpus context (Vectorize)

QNFO: Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet | https://papers.qnfo.org/papers/quniverse-fleet-lessons
QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage? | https://papers.qnfo.org/papers/auditing-bqnn
QNFO: Computing After Silicon: A History-Constrained Forecast of Computing Machine Evolution, 2026-2050 | https://papers.qnfo.org/papers/computing-machines

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1612.08910 | Reliability Modeling and Analysis of Communication Networks
  In recent times, the functioning of various aspects of modern society---ranging from the various infrastructural utilities such as electrical power, water to socio-economical aspects such as telecommunications, business, commerce, education---has become critically reliant on communication networks, and particularly on the Internet. With the migration of critical facilities to the Internet, it has 
  Full text (https://arxiv.org/html/1612.08910), excerpts of its own sections:
  § 1 Introduction: Communication networks have become an integral part of our daily life with applications ranging from ubiquitous hand held devices (like cell phones and remote car keys) to sophisticated equipment used in aircrafts, power systems, nuclear plants and healthcare devices. Given the safety and financial-critical nature of many of these applications, the failures in the underlying network elements can significantly affect the performance of network services and have detrimental, or even catastrophic, results. For instance, the virtualized environment of a virtual data center in a cloud computing network is often subjected to transient latency, dropped packets, and full-blown network partitions [ 1 ] . A study for the cloud computing vulnerabilities shows that there were about 172 unique cloud computing outage incidents between 2008 and 2012 [ 2 ] . The major causes of these incidents include (i) insecure interfaces and application programmer interfaces (APIs), (ii) data loss and leakages, and (iii) hardware failures. [...]
  § 1.1 Contributions and Organization of this Paper: The purpose of this survey paper is to provide a generic overview of the major reliability modeling and analysis techniques in the domain of communication networks. Based on the three kind of reliability analysis techniques, we divide this survey into three broad parts: (i) analytical (ii) simulation tools and (iii) formal methods. [...]
  § 3.3.3 Higher-order-Logic Theorem Proving: Higher-order Logic (HOL) is a system of deduction with a precise semantics and is expressive enough to model any system that can be expressed in a closed mathematical form. Moreover, in conjunction with general purpose proof assistant, such as Coq [ 69 ] , PVS [ 70 ] and HOL4 [ 71 ] , HOL can be utilized to develop automatic and interactive proof environments for reasoning about system properties. The formal analysis carried out in this manner is logically sound and provides an irrefutable proof that a system satisfies its requirements. A number of higher-order-logic formalizations of probability theory are available in higher-order logic (e.g., [ 72 , 73 , 74 ] ) and have been utilized to verify sampling algorithms of a number of commonly used discrete [ 72 ] and continuous random variables [ 75 ] based on their probabilistic and statistical properties [ 76 , 77 ] . [...]
  § 8 Conclusions: In this paper, we have provided a tutorial introduction to the modeling and analysis techniques that have been used for studying reliability and availability of communication networks. We have discussed the various reliability models constructed using the building blocks offered by the formalisms of reliability block diagram, fault trees, Markov chains, and Bayesian network models. We have also presented background, and a critical comparison, of the various reliability analysis techniques (such as analytical methods, simulation modeling, and formal methods). Apart from providing the necessary background, we have also provided a detailed survey of the application of these techniques in the existing literature focused on studying reliability of communication networks. The main contribution of this work is that it is the first work that has presented a comprehensive review of the various techniques available for reliability modeling and analysis of communication networks along with a critical analysis describing their pros and cons in various contexts.
[2] arXiv:2604.20127 | Trajectory-Aware Reliability Modeling of Democratic Systems
  Failures in complex systems often emerge through gradual degradation and the propagation of stress across interacting components rather than through isolated shocks. Democratic systems exhibit similar dynamics, where weakening institutions can trigger cascading deterioration in related institutional structures. Traditional reliability and survival models typically estimate failure risk based on th
  Full text (https://ar5iv.labs.arxiv.org/html/2604.20127), excerpts of its own sections:
  § Submission history: From: Valentina Kuskova [ view email ] [v1] Wed, 22 Apr 2026 02:47:31 UTC (479 KB) [v2] Fri, 15 May 2026 10:51:51 UTC (442 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Trajectory-Aware Reliability Modeling of Democratic Systems, by Dmitry Zaytsev and 2 other authors View PDF view license
  § Current browse context:: cs.LG < prev | next > new | recent | 2026-04 Change to browse by: cs cs.CY
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[3] arXiv:2503.18102 | AgentRxiv: Towards Collaborative Autonomous Research
  Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. To address these challenges, we int
  Full text (https://arxiv.org/html/2503.18102), excerpts of its own sections:
  § 1 Introduction: Scientific discovery has historically been an iterative process, characterized by the systematic formulation of hypotheses, the execution of controlled experiments, and the evaluation of results ( Chalmers (2013) ). Over time, these methods lead to the steady accumulation of knowledge, forming the basis upon which further inquiries are built ( Shapere (1964) ). In this manner, scientific progress does not typically arise from isolated breakthroughs but rather from incremental improvements that collectively advance our understanding of complex phenomena. In an effort to accelerate the process of scientific discovery, recent work has explored the ability of LLM agents to perform autonomous research ( Schmidgall et al. (2025) ; Swanson et al. (2024) ; Lu et al. (2024b) ). The AI Scientist framework ( Lu et al. [...]
  § Experimentation and Writing.: In the Experimentation phase, the PhD and Postdoc agents develop a research plan outlining the experimental components, while the ML Engineer and SW Engineer agents work together to prepare and refine data preparation code (Figure 2 ). Automation continues with the mle-solver module, which iteratively generates, tests, and improves machine learning code based on performance scoring and self-reflection. The mle-solver uses an LLM-based automatic repair mechanism to fix code errors encountered during execution. Finally, in the Report Writing phase, the Professor and PhD agents synthesize all findings into a structured LaTeX-based report using the paper-solver tool, with iterative edits and peer review–like refinements that support both autonomous and human-guided checkpoints. Both the mle-solver and the paper-solver use LLM-based reward functions to guide the process of code and paper development.
  § 5 Discussion: In this paper, we introduced AgentRxiv , a framework for collaborative research through interactions among autonomous LLM agents. Unlike previous agent-based research frameworks that focus on independent workflows, AgentRxiv emphasizes collaboration, enabling agents to incrementally build upon prior findings. Our empirical evaluations show that allowing agents to reference their previous work consistently improves performance compared to isolated approaches. Additionally, our results indicate that the insights generated through collaborative agent interactions are generalizable, transferring effectively across diverse benchmarks and multiple language models. We also evaluated the scalability of AgentRxiv by comparing parallel and sequential experimentation modes. Our experiments demonstrate that parallel research accelerates the discovery process in terms of wall-clock time. However, the parallel approach incurs higher computational costs due to redundant experiments conducted by independent laboratories. [...]
  § Conclusion.: In conclusion, AgentRxiv advances the state of agent-driven research by providing an effective platform for continuous, collaborative discovery among LLM agents. By facilitating cumulative knowledge-building, enhancing generalization across tasks, and potentially accelerating research cycles, AgentRxiv represents a promising development toward integrating autonomous systems more comprehensively into scientific workflows. Nonetheless, careful methodological refinement and ongoing scrutiny of ethical implications remain essential for responsibly leveraging automated collaboration within scientific research.
[4] arXiv:2607.24647 | Efficiency Matters in Autonomous Research
  AI-driven autonomous research (AR) systems are becoming increasingly effective across a broad range of tasks. Their performance, however, is still evaluated primarily by the quality of the final outcome. In this paper, we argue that the efficiency of the solution-search process is an equally important but often overlooked dimension of performance. A strong AR system should not only produce high-qu
  Full text (https://arxiv.org/html/2607.24647), excerpts of its own sections:
  § 1 Introduction: AI-driven autonomous research (AR) systems are becoming an increasingly promising approach to solving difficult problems across mathematics, algorithm design, software engineering, materials discovery, and other scientific and engineering domains  [ 1 ] . By repeatedly proposing hypotheses or candidate solutions, evaluating them, and using the resulting feedback to guide subsequent decisions, these systems can conduct increasingly long and complex research processes with limited human intervention. Existing AR systems are typically evaluated primarily by the quality of the best final solution they discover. This outcome-based evaluation is natural but incomplete. A capable AR system should not only find strong solutions, but find them within a reasonable budget. A system that eventually discovers an excellent solution only after years of computation or billions of dollars in experiments would be of limited practical value, regardless of the quality of its final result. [...]
  § 2 Related work: Search over candidate solutions.  Searching over a space of candidate solutions is a classical approach in problem solving and intelligence modeling. Game-playing systems search move trees  [ 6 , 7 ] , neural architecture search explores network designs  [ 8 ] , and evolutionary computation has long been used to optimize programs  [ 9 ] . The policy families studied here are drawn directly from this classical repertoire. What changes in AR is the proposal operator. Whereas earlier methods relied on a hand-designed move generator, sampler, or mutation operator, an LLM now proposes the next state conditioned on the task and the search history. The underlying search structures and questions of efficiency therefore remain relevant, even though the mechanism for generating candidates has changed. Whether the classical ordering of these search strategies persists under an LLM-based proposal operator is an empirical question that we investigate. Autonomous research and code agents. [...]
  § 3.1 Research as a Search Process: Search over a solution space is a natural paradigm for problem solving  [ 38 ] . The research process implemented by most AR systems can likewise be viewed as a search procedure comprising a proposal policy that generates candidate hypotheses or solutions, a verifier that evaluates them, and a search structure that records and organizes the states explored so far. This procedure repeats until the system finds a fully verified solution or exhausts its budget. [...]
  § 7 Discussion: Discovery efficiency, improvement per costly evaluation, should be treated as a first-class objective for AR. This perspective changes both how these systems are evaluated and how they should be designed. Our results show that search efficiency and final outcome quality are empirically distinct dimensions. Across the classical search structures we study — hill climbing, tree search, beam search, and evolutionary search — no fixed structure is universally the most efficient. This heterogeneity motivates adaptive policies that allocate search budget dynamically according to the demands of each task. Based on this observation, we introduce fluid , a budget-adaptive policy that nearly matches a per-task oracle without prior knowledge of which search structure is best suited to the task. The broader design principle supported by our results is budget adaptivity . A fixed search structure commits in advance to a particular way of spending the evaluation budget. [...]
[5] arXiv:2608.04738 | EviGraph: Evidence-Guided Autonomous Research Agents
  Autonomous research agents can generate hypotheses, execute experiments, and draft manuscripts, yet their outputs often contain unsupported claims and inconsistencies between research questions, experiments, results, and conclusions. We argue that this problem is partly architectural: existing systems organize research as sequential pipelines but do not explicitly maintain or validate the evolving
  Full text (https://arxiv.org/html/2608.04738), excerpts of its own sections:
  § 1 Introduction: Autonomous research systems built on large language models can now generate ideas, write code, run experiments, analyze results, and draft full manuscripts ( Lu et al. 2024 ; Schmidgall et al. 2025 ; InternAgent Team et al. 2025 ; Bran et al. 2024 ; Jansen et al. 2024 ) . Despite this progress, producing a fluent research paper does not guarantee that the underlying process is reliable. In practice, autonomous systems can propagate weak assumptions, unsupported claims, and experimental inconsistencies into the final manuscript, making it difficult to determine whether a conclusion is genuinely supported by the executed research ( Chen et al. 2025 ; Yang et al. 2026 ; Trehan and Chopra 2026 ; Min et al. 2023 ) . We argue that this problem is partly architectural. Most autonomous research systems are organized as sequential pipelines in which outputs move from idea generation to experimentation, analysis, and writing ( Lu et al. 2024 ; Liu et al. 2026 ; Qian et al. 2026 ; Xu et al. 2026 ) . [...]
  § 3.1 Framework Overview: Figure 1: Overall workflow of the EviGraph framework, organized into three collaborative phases. As illustrated in Figure 1 , EviGraph takes a research goal (q) as input. Initialization uses temporary structured records to build $G_{0}$ ; thereafter, graph-facing components read and update this shared graph of research problems, gaps, hypotheses, experiments, findings, and claims. The framework proceeds through three phases.
  § 4.1 Experiment Setup: We evaluate EviGraph on two autonomous-research benchmarks and compare its overall research performance and research reliability with existing end-to-end systems.
  § 5.1 Component-Evaluation Alignment: Table  5 summarizes the operational role of each component and the evaluation signals through which its contribution is most directly reflected. The Hypothesis Filter and Graph Builder determine which research directions enter the evidence graph and how their dependencies are represented, making their roles closely related to Result Analysis, Novelty, and claim support. The Graph Inspector, Repair Planner, and Repair Agents operate directly on weak claim–evidence relationships and affected downstream subgraphs, connecting them to CSR, EDC, Code Execution, and Result Analysis. The two graph libraries support the stability and continuity of this process: $\mathcal{M}_{S}$ preserves intermediate states for version selection and rollback, while $\mathcal{M}_{L}$ provides prior graph structures and repair experience for related research tasks. Finally, the Paper Writer and Paper Reviewer transform the validated graph into a manuscript and verify its faithfulness, linking their roles to Writing, Novelty, and CSR. [...]
  § 6 Conclusion: EviGraph reframes autonomous research from single-pass pipeline execution as iterative evidence construction, inspection, and repair over a typed research graph. Its graph structure makes evidence dependencies explicit so that weak links can be detected; the graph experience library preserves reliable states within and across runs; and the Hypothesis Filter screens candidate directions through staged pilot experiments. On ARC-Bench-ML, EviGraph achieves the highest Overall score (86.45%), leading in Code Exec and Result Analysis. On NanoResearch-20, it leads in Novelty, Performance, and Writing while matching the best E2E rate. These results confirm that enforcing evidence-chain validity during research strengthens both reliability and task quality.
[6] arXiv:2609.39392 | Experimental Experience Modeling for Autonomous Research
  Autonomous research agents can generate hypotheses and conduct experiments, but experimentation remains a major source of computational cost. A fundamental challenge is deciding which experiments are worth running, particularly when prior evidence is insufficient to resolve uncertainty. Yet current research agents lack a systematic way to leverage experimental experience when making such decisions
  Full text (https://arxiv.org/html/2609.39392), excerpts of its own sections:
  § 2.3 Experience-Guided Experimental Decision Making: For each candidate experimental direction, EEM determines whether further resource investment is justified using the experience available at decision time. The decision follows two possible paths: (i) When relevant historical experience already provides sufficient support, EEM directly reuses that experience to determine whether the direction should be pursued, revised, or rejected. (ii) When historical experience is insufficient, EEM identifies the missing decision-relevant experience, acquires it through a targeted, low-cost pilot, and then makes the decision using both historical and newly acquired experience. In this way, EEM maximizes reuse of accumulated experience while acquiring additional experience only when necessary. Decision Making with Sufficient Historical Experience. [...]
  § 3 Results: We evaluate EEM on ARC-Bench ( Liu et al., 2026 ) to examine whether reusable experimental experience and on-demand pilot acquisition improve autonomous research. Our experiments focus on five aspects: (i) overall performance: comparison with representative autonomous research systems across code development, code execution, and result analysis (Section  3.2 ); (ii) efficiency: comparison of model token consumption across planning, experimentation, and writing (Section  3.3 ); (iii) component effectiveness: ablations of experience distillation, on-demand pilot acquisition, and historical experience reuse (Section  3.4 ); (iv) backbone applicability: evaluation with a general-purpose model in addition to a coding-oriented model (Section  3.5 ); and (v) stability across runs: repeated executions under the same configuration to assess performance consistency (Section  3.6 ).
  § 3.1 Experimental Setup: Benchmark and Evaluation Metrics. We use ARC-Bench ( Liu et al., 2026 ) , which contains 25 machine learning research topics with specified research objectives and experimental requirements. The benchmark evaluates three aspects of experimentation: Code Development (CD), Code Execution (CE), and Result Analysis (RA). CD assesses the implementation of the proposed methods and baselines, CE measures successful execution and the production of required experimental evidence, and RA evaluates whether the conclusions are supported by the observed results. An LLM-based evaluator assigns scores according to the benchmark rubrics, with higher scores indicating better performance. The overall score is computed as $0.25\,\mathrm{CD}+0.25\,\mathrm{CE}+0.50\,\mathrm{RA}$ . Baselines and Implementation. We compare EEM with three autonomous research baselines: (i) AI Scientist v2 ( Yamada et al., 2025 ) automates the research workflow and uses agentic tree search to improve experiments. [...]
  § 5 Conclusion: We introduced Experimental Experience Modeling (EEM), a framework for experience-supported experimental decision making in autonomous research. EEM distills experimental trajectories into reusable experience, retrieves applicable experience to guide resource investment, and acquires missing decision-relevant experience through targeted, low-cost pilots when historical experience is insufficient. Experience from both pilot and full-scale experiments is accumulated for subsequent decisions. Experiments on ARC-Bench show that EEM improves research performance while reducing model token consumption, with ablation studies supporting the effectiveness of its design. [...]
[7] arXiv:1811.12271 | Reliability Modeling, Analysis and Prediction of Wireless Mobile Communications
  The future Fifth Generation (5G) mobile cellular networks that are currently in research phase today enable broad range of services/applications beyond classical mobile communications. One key enabler for Ultra-Reliable services to be integrated into mobile networks is the \textit{Reliability} of transmission success of a given data packet. This is harder mainly owing to the time-dependent effecti
  Full text (https://arxiv.org/html/1811.12271), excerpts of its own sections:
  § I Introduction: † † This is a preprint, the full paper is published in Proceedings of 79th IEEE Vehicular Technology Conference(IEEE VTC Spring 2014), ©2014 IEEE. Personal use of this material is permitted. However, permission to use this material for any other purposes must be obtained from the IEEE by sending a request to pubs-permissions@ieee.org. The exponential increase in the demand for mobile and wireless connectivity is witnessed by the increasing number of new services and applications, many of which require stringent reliability requirements. Examples of such services/application are Vehicle-to-Vehicle(V2V), Vehicle-to-Infrastructure(V2I), and other industrial applications(Sensor Networks)with varying design criteria which are typically specified in terms of Availability, rather than Reliability [ 4 ] . Analysis of these systems requires specialized application of reliability engineering theory and its principles [ 5 ] with performance expectations ranging from high to extreme [ 4 ] . [...]
  § I-A Wireless Channel Fading: In digital communication systems, the most frequently used channel model is the Additive White Gaussian Noise (AWGN) channel. However, this model is too simplistic and cannot support complex spatial and temporal variations [ 9 ] due to more basic factors such as pathloss, shadowing and multi-path propagation affecting the radio propagation.Each of this phenomenon is caused by a different underlying physical principle (Reflection, Refraction, Diffraction and Scattering of electromagnetic wave) and must be considered when designing and evaluating wireless communication systems. Among the three independent phenomena, only path loss is deterministic which depends only on the distance between Tx and Rx. Pathloss is more relevant on larger time scales like seconds/minutes, since the distance between the Tx and the Rx does not significantly change on smaller time scale [ 9 ] . On smaller time scales, its effect is visible for high mobile communications (mobility). On the other hand, shadowing and multi-path fading are not deterministic and have a stochastic nature [ 10 ] . [...]
  § IV Simulation Results: The Key Performance Indicators (KPI’s) for calculating the system reliability $R_{w}$ of the system $S_{w}$ are the survival/reliability function $R(t)$ and the hazard function/ Failure rate $\lambda(t)$ . These are calculated via the individual life distributions of the factors. Joint probability distributions are then used to derive the system reliability $R_{w}$ .
  § V Conclusion and Future Work: In this paper, a new framework for modeling, analyzing the reliability of wireless communication system is presented based on Reliability Analysis using RBD’s. The framework is used to model and analyze the transmission success probability under the effects of channel fading and retransmissions. Reliability prediction (Availability) has been done by considering wireless channel as a non-repairable system by means of survival $R(t)$ and hazard $\lambda(t)$ functions where Availability is the probability of the presence of a Reliable Transmission Link (RTL) for successful transmission [ 18 ] . The proposed framework is cross layer compatible (reliability of the tranmission can be modeled right from the data (packet) generation till packet decoding which spans PHY, MAC, Network and Application layers). It also allows for smoother integration of the 3GPP communication systems into the legacy systems (Automotive and other Industrial systems) since it is also based on the de facto standards of the industrial reliability analysis.
[8] arXiv:2603.11468 | Stage-Adaptive Reliability Modeling for Continuous Valence-Arousal Estimation
  Continuous valence-arousal estimation in real-world environments is challenging due to inconsistent modality reliability and interaction-dependent variability in audio-visual signals. Existing approaches primarily focus on modeling temporal dynamics, often overlooking the fact that modality reliability can vary substantially across interaction stages. To address this issue, we propose SAGE, a Stag
  Full text (https://arxiv.org/html/2603.11468), excerpts of its own sections:
  § 1 Introduction: Figure 1 : Temporal reliability varies within modalities due to expressive facial cues and varying speech activity. SAGE adaptively reweights modality contributions over time, leading to stable and accurate VA prediction. Emotion recognition has become an increasingly important research topic in machine intelligence, as it enables the development of intelligent systems capable of understanding human affective states  [ 31 , 24 , 7 , 8 , 9 ] . While many traditional approaches formulate emotion recognition as a categorical classification problem  [ 41 , 42 ] , an alternative paradigm represents emotions in a continuous space using valence and arousal (VA)  [ 3 ] . In this formulation, valence describes the degree of pleasantness, while arousal reflects the level of activation. Modeling emotions in a continuous VA space allows systems to capture subtle and ambiguous affective variations that are difficult to represent with discrete categories. [...]
  § 3.1 Overview: Figure  2 illustrates the overall architecture of the proposed SAGE model for continuous VA estimation. We design a reliability-aware adaptive fusion framework composed of four stages. (i) Multimodal Feature Extraction. Given a short video clip, preprocessed cropped video frames and the corresponding raw audio waveform are used as inputs. [...]
  § 4.2 Evaluation Metrics: To quantitatively evaluate continuous emotion estimation performance, we adopt the CCC as the primary evaluation metric. CCC measures the agreement between predictions and ground-truth annotations by jointly considering correlation and distributional similarity. It is defined as: $\mathrm{CCC}=\frac{2\rho\sigma_{x}\sigma_{y}}{\sigma_{x}^{2}+\sigma_{y}^{2}+(\mu_{x}-\mu_{y})^{2}},$ (15) where $\rho$ denotes the Pearson correlation coefficient between the prediction $x$ and the ground truth $y$ , $\mu_{x}$ and $\mu_{y}$ represent their respective means, and $\sigma_{x}^{2}$ and $\sigma_{y}^{2}$ denote their variances. Unlike Mean Squared Error (MSE), which evaluates point-wise discrepancies independently at each timestep, CCC explicitly accounts for both correlation consistency and mean–variance alignment across the entire temporal sequence. This characteristic makes CCC particularly suitable for continuous affect estimation tasks, where preserving global temporal dynamics and structural agreement is as important as minimizing instantaneous prediction errors. [...]
  § 5 Conclusion: In this paper, we investigated multimodal VA estimation from the perspective of modality reliability rather than architectural complexity alone. We introduced SAGE, a Stage-Adaptive reliability modeling framework that explicitly estimates and regulates modality-wise confidence during multimodal fusion. Extensive experiments conducted within the setting of the 10th ABAW Competition demonstrate that performance limitations in real-world emotion recognition frequently arise from unstable modality contributions rather than insufficient temporal modeling capacity. By dynamically calibrating cross-modal influence across interaction stages, SAGE produces more stable affect trajectories under noisy, imbalanced, and unconstrained conditions. These results suggest that reliability-aware modeling constitutes a fundamental design principle for robust multimodal emotion estimation. The proposed framework achieved competitive performance in the official evaluation of the 10th ABAW Competition, further validating its practical effectiveness on large-scale in-the-wild benchmarks.
[9] arXiv:2405.18001 | Network-Aware Reliability Modeling and Optimization for Microservice Placement
  Optimizing microservice placement to enhance the reliability of services is crucial for improving the service level of microservice architecture-based mobile networks and Internet of Things (IoT) networks. Despite extensive research on service reliability, the impact of network load and routing on service reliability remains understudied, leading to suboptimal models and unsatisfactory performance
  Full text (https://arxiv.org/html/2405.18001), excerpts of its own sections:
  § I Introduction: Cloud-native technologies [ 1 ] empower the creation and operation of applications in massively scalable distributed infrastructures, leveraging microservices architecture (MSA) [ 2 ] alongside platform technologies [ 3 ] like containers and virtual machines. With the Cloud Native Computing Foundation’s (CNCF) promotion of cloud-native technologies, MSA, which aims to improve software agility, is gradually coming into the limelight of both academia and industry. By splitting applications into microservices and interconnecting them using a lightweight application programming interface (API), MSA granulates complex services and provides an easier means of maintaining and updating software, accelerating new feature launches, and reducing manual costs. The benefits of MSA have led several major service providers such as Amazon, Netflix, and Spotify to use MSA to place their services [ 2 ] , as well as making the Internet of Things (IoT) paradigm consider using MSA for smart manufacturing, Internet of Vehicles (IoV), and Industrial IoT (IIoT) [ 4 ] . [...]
  § II Related Work: Due to the distributed nature of MSA-based services, assessing service reliability is critical to ensure the failure tolerance of the MSA-based service, which has been addressed by research on reliability models and microservice placement.
  § II-A Reliability Model: Studies on reliability models can be classified into two main categories based on failure causes: hardware reliability and software reliability [ 15 ] . For hardware reliability, most studies have modeled the arrival of hardware failures as Poisson processes [ 30 ] . Wang et al . [ 9 ] proposed an instance-sharing reliability model to aggregate multiple services into a composite and proposed an algorithm to improve its reliability. Zhu et al . [ 12 ] proposed a load-dependent node reliability model to capture the relationship between failure probabilities and workloads and introduced a recovery strategy to handle workload variations. Mtawa et al . [ 31 ] proposed a link reliability model to assess the all-pair reliability of the network and tested it on both conventional network and SDN. Similar to hardware failures, the arrival of software failures is also usually modeled as a Poisson process [ 10 ] . Liu et al . [...]
  § VII Performance Evaluation: We validate our modeling and algorithmic work through extensive simulations. Our simulation code can be accessed online [ 38 ] .
  § VIII Conclusion: In this paper, we address the intricate challenges of microservice placement with a focus on enhancing the reliability of MSA-based 5G and IoT services. The network-aware service reliability model thoroughly considers the impact of network load and routing on service reliability, offering profound insights into system reliability assessment. Based on the proposed service reliability model, we propose an innovative heuristic SRP algorithm that effectively addresses the microservices placement problem with the fully protected path mechanism. For the purpose of reducing bandwidth consumption, we further propose the SRP-S algorithm by considering the shared backup path contention caused by simultaneous failures, which effectively tackles the microservice placement problem with the shared backup path mechanism. Simulation results validate the proposed service reliability model and show that the SRP algorithm can reduce the number of failures by up to 29% compared to the benchmark algorithms with the fully protected path mechanism. [...]
[10] arXiv:2301.01850 | Bayesian Weapon System Reliability Modeling with Cox-Weibull Neural Network
  We propose to integrate weapon system features (such as weapon system manufacturer, deployment time and location, storage time and location, etc.) into a parameterized Cox-Weibull [1] reliability model via a neural network, like DeepSurv [2], to improve predictive maintenance. In parallel, we develop an alternative Bayesian model by parameterizing the Weibull parameters with a neural network and e
  Full text (https://ar5iv.labs.arxiv.org/html/2301.01850), excerpts of its own sections:
  § Submission history: From: Michael Potter [ view email ] [v1] Wed, 4 Jan 2023 23:28:58 UTC (470 KB) [v2] Mon, 9 Jan 2023 17:57:06 UTC (475 KB) [v3] Wed, 11 Jan 2023 01:15:08 UTC (478 KB) [v4] Thu, 9 Mar 2023 18:54:31 UTC (478 KB) [v5] Fri, 14 Apr 2023 17:11:53 UTC (479 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Bayesian Weapon System Reliability Modeling with Cox-Weibull Neural Network, by Michael Potter and 1 other authors View PDF view license
  § Current browse context:: stat.AP < prev | next > new | recent | 2023-01 Change to browse by: cs cs.AI cs.LG math math.PR stat
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[11] arXiv:2605.03042 | ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration
  This report describes ARIS (Auto-Research-in-sleep), an open-source research harness for autonomous research, including its architecture, assurance mechanisms, and early deployment experience. The performance of agent systems built on LLMs depends on both the model weights and the harness around them, which governs what information to store, retrieve, and present to the model. For long-horizon res
  Full text (https://arxiv.org/html/2605.03042), excerpts of its own sections:
  § 1 Introduction: Recent work on harness engineering  ( Lee et al., 2026 ) suggests that the performance of LLM systems can depend heavily on the harness —the surrounding system logic that governs storage, retrieval, and presentation—as well as on model weights. Machine-learning research poses an unusually complex harness-engineering problem: the workflow spans literature review and hypothesis generation through experimentation, internal critique, manuscript preparation, and responses to external feedback. This research harness is still assembled manually in many settings: researchers coordinate compute, references, manuscript tooling, and feedback workflows across separate systems  ( Lu et al., 2024 ; Schmidgall et al., 2025 ) . Several autonomous research agents now target specific parts of this workflow. [...]
  § Stage 1: Experiment-integrity audit ( /experiment-audit ).: A cross-model reviewer audits the evaluation code and outputs against the following integrity failure modes: (1)  model-derived reference labels —reference targets are synthesized from model outputs rather than obtained from the dataset or another declared source; (2)  self-normalized scores —metrics use denominators derived from the model’s own predictions, which can inflate or distort reported performance; (3)  phantom results —claimed numbers that do not match actual output files; (4)  dead-code or unused-metric inflation —evaluation code defines additional metrics or branches that are never executed but are described as part of the analysis; (5)  scope inflation —claims generalize beyond the tested datasets, seeds, or experimental settings. The audit produces a structured report ( EXPERIMENT_AUDIT.md ) and a machine-readable JSON summary. The audit is advisory at the workflow level: it does not halt execution, but downstream stages propagate warning or failure statuses into later claim judgments.
  § Stage 2: Result-to-claim mapping ( /result-to-claim ).: Each candidate experimental claim is evaluated against the available evidence and assigned one of three verdicts: supported , partially supported , or invalidated . If a Stage 1 audit report is available, its integrity_status is propagated to each claim record; claims with fail cannot be marked fully supported until the integrity issue is resolved. The output is a claim ledger that maps each experimental claim to the evidence that supports, qualifies, or contradicts it.
  § 7 Conclusion: This report presented Aris as a research harness built around a conservative assumption: long-horizon research performed by a single agent is unreliable by default, and the relevant failure mode is not visible breakdown but plausible unsupported success , where claims outrun evidence and later readers silently inherit the executor’s framing. Aris responds by decomposing the workflow into the three bottlenecks framed in § 1 —persistent research state, modular execution, and independent assurance—and by adopting a two-role cross-family reviewer-executor pattern as the practical minimum for breaking self-review blind spots. These three bottlenecks map to three layers: an execution layer of reusable Markdown-defined skills and a persistent research wiki, an orchestration layer for configurable workflow control and reviewer routing, and an assurance layer for evidence-to-claim auditing and manuscript checks. A prototype meta-optimization loop provides an initial mechanism for improving skill prompts, defaults, and convergence rules over time. [...]
[12] QNFO: Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet | https://papers.qnfo.org/papers/quniverse-fleet-lessons
  This paper is retracted: it described experiments, measurements or reviews as done that never took place. See the retraction notice.
  Full text (https://papers.qnfo.org/papers/quniverse-fleet-lessons), excerpts of its own sections:
  § 1. Introduction: Researchers and platform operators who depend on continuous, automated generation and publication of scientific content confront a dual problem: (1) maintaining a cloud‑native fleet of serverless functions that remains operational without frequent human intervention, and (2) trusting the fleet’s self‑reported metrics for cost, throughput, and autonomy. In the Quniverse deployment, thirty‑six worker scripts, ten SQLite databases, eight vector indexes, and nineteen object‑storage buckets must stay online while handling thousands of paper records. We assume that drift between the service registry and deployed scripts leads to unplanned downtime and that the composite autonomy assessment is **3.6 / 5**. Simultaneously, a retraction notice disclosed that several self‑reported quantitative claims were produced without any measurement procedure, including a billing‑unit error that inflated the perceived monthly spend to **\$11 000**. [...]
  § 5. Results: The analytical derivations of Section 4 yield the following quantitative outcomes. | Result | Value | Interpretation | |--------|-------|----------------| | **R1. Expected failures per month** | $E[F]=2.16$ | On average two to three worker‑script failures are anticipated each month after self‑healing mitigation. | | **R2. Papers per active project** | $9.65$ papers/project | Each active research project contributes roughly ten papers to the corpus. | | **R3. High‑severity gap proportion** | $11.9\%$ | Five of the forty‑two identified gaps are classified as high severity. | | **R4. Baseline composite autonomy score** | $C_{\text{base}}=4.26$ | The fleet’s autonomy assessment before mitigation. | | **R5. Improved composite autonomy score** | $C_{\text{new}}=4.66$ | A 50 % reduction in per‑worker failure probability raises the score by $0.40$. | | **R6. Projected monthly gateway spend (baseline)** | $S_{\text{proj}}=\$160.8$ | Baseline spend assumes a base of $\$150$ plus extra cost from expected failures. | | **R7. [...]
  § 7.3 Minimal Next Experiment: A pilot study would: 1. **Measure** the actual number of worker‑script failures over a 30‑day window, recording both raw failure events and self‑heal actions. 2. **Verify** the billing feed by extracting raw usage in cents and converting to dollars, checking for unit‑dimension consistency. If the observed failure count deviates from $2.16$ by more than $\pm0.5$ or the billing conversion yields a factor other than $100$, the model assumptions would be refuted.
  § 8. Conclusion: An integrated analytical framework has been constructed to assess reliability, cost, and claim integrity for the Quniverse autonomous research fleet. By modeling worker‑script failures as Bernoulli trials with self‑heal mitigation, aggregating resource consumption, and recomputing all self‑reported quantitative claims, the study identifies concrete levers for improvement: * Expected monthly failures are modest ($2.16$) but non‑trivial, suggesting targeted reliability engineering. * A 50 % reduction in per‑worker failure probability yields a measurable uplift in the composite autonomy score ($4.26 \rightarrow 4.66$) and a modest cost saving ($\$160.8 \rightarrow \$155.4$). * A billing‑unit error inflates perceived spend by $73.3$‑fold, underscoring the necessity of unit‑dimension validation. The results are ready for validation at **TRL 2** and provide a clear roadmap for pilots that can de‑risk the assumptions and guide the fleet toward higher autonomy and fiscal compliance.
[13] QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage? | https://papers.qnfo.org/papers/auditing-bqnn
  We audit the BQNN paper by Lakhdar-Hamina et al. (2025, PRL / arXiv:2507.21222v2) which implements a tunable quantum neural network on three quantum computing platforms. Through a complete Phase 1-4 research pipeline including due diligence, external literature search across 32 papers, and a 9-stage Bayesian deep-dive cascade with 5-adversary red-team audit, we evaluate every claim against the Phy
  Full text (https://papers.qnfo.org/papers/auditing-bqnn), excerpts of its own sections:
  § 1. Introduction: What BQNN Claims, and Why It Matters: On 6 August 2025, Lakhdar-Hamina, Liu, Barney, Miller, Green, Linke, and Galitski published "Benchmarking a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware" in Physical Review Letters (arXiv:2507.21222v2). The paper implements a quantum neural network — dubbed the Benchmark Quantum Neural Network (BQNN) — on three distinct hardware platforms: JQI trapped-ion processors with microwave-driven gates, JQI trapped-ion processors with laser-driven Raman gates, and IBM superconducting transmon processors (Eagle and Heron). It claims: 1. That BQNN in an intermediate "quantum" regime ($a \approx 0.5$) outperforms its classical limit ($a = 0$) on MNIST image classification. 2. That physical noise — normally considered an obstacle to quantum computation — can be *beneficial* for quantum machine learning at inference time, demonstrated on a single "NY" (No-Yes) image that classical networks misclassify. 3. [...]
  § 2.1 Due Diligence (Phase 1): We queried the QNFO Knowledge Graph (2,168 nodes, 1,462 edges across 37 node labels), Vectorize semantic search (10 QNFO-internal results), and D1 living-paper database for any prior QNFO work on quantum neural network benchmarking or hardware comparison. **Result:** Zero prior QNFO papers address QNN benchmarking or multi-platform comparison. BQNN is genuinely novel within the QNFO corpus. [...]
  § 3.1 Architecture Summary: BQNN is a partially binarized multilayer perceptron with the following key features: | Feature | Description | |:--------|:------------| | Layers | 3 hidden layers, 16 qubits per layer | | Activations | Constrained to $\pm 1$ (binarized) | | Quantum mapping | Neuron → qubit; activation → single-qubit rotation + projective measurement | | Tunability | Parameter $a$: $a = 0$ = classical deterministic; $a > 0$ = quantum non-deterministic | | Training | Classical simulation with straight-through estimator (STE) and SGD | | Inference | Quantum hardware, 10 shots per image, majority vote | | Circuit structure | **Fully separable** — executable on as few as 1 qubit | | Hardware | JQI trapped ions (microwave), JQI trapped ions (Raman), IBM Eagle/Heron (cloud) | | Dataset | MNIST, 55 test images | The circuit separability is a critical architectural fact: because BQNN's hidden-layer circuits contain no entangling gates, the entire quantum computation can be simulated classically with zero asymptotic overhead. [...]
  § 7. Conclusion: The BQNN paper by Lakhdar-Hamina et al. (2025) is a competently executed engineering demonstration of multi-platform quantum neural network inference. Its benchmarking methodology — the first comparison of QNN performance across three distinct hardware platforms — is novel, valuable, and should be adopted by the community. Its quantum advantage claims are not supported by the data. The statistical evidence is insufficient (N = 55, overlapping error bars), the noise-as-advantage claim rests on a single cherry-picked image, the circuit is fully separable and classically simulable, and the pathway to non-simulability requires seven unvalidated assumptions to all be true simultaneously. The joules-per-solution ratio is approximately $10^9$ above the classical break-even point. We rate the paper's strongest claim (multi-platform benchmarking) as **SUSTAINED** and its advantage claims as **NOT SUSTAINED**. The distinction between legitimate benchmarking and premature advantage framing is not academic — it is the difference between honest science and promissory engineering. [...]
[14] QNFO: Computing After Silicon: A History-Constrained Forecast of Computing Machine Evolution, 2026-2050 | https://papers.qnfo.org/papers/computing-machines
  A history-constrained forecast of computing machine evolution 2026-2050. Seven post-silicon candidates assessed; heterogeneous convergence (AI accelerators, quantum co-processors, processing-in-memory) is the central thesis; twelve dated falsifiable predictions registered for 2030-2040.
  Full text (https://papers.qnfo.org/papers/computing-machines), excerpts of its own sections:
  § 1. Introduction: Every era of computing has been defined by the physics of its substrate. The mechanical era was bounded by machining tolerances; the electromechanical era by relay switching time; the vacuum tube era by thermionic emission and power dissipation; the transistor era by lithography and doping control. Each transition followed the same invariant dynamic: constraint saturation → substrate shift → Wright's Law cost decline → institutional adoption. Understanding this invariant is the key to forecasting what comes after silicon. This paper addresses three questions. First, what does the historical record tell us about the structure of computing paradigm shifts? Second, which of the candidate post-silicon trajectories is most probable, and on what timescale? Third, what falsifiable predictions follow, and how would each be disconfirmed? We answer these questions using a cross-domain framework that treats computing evolution as a constraint-driven phase transition, structurally isomorphic across physics, biology, and sociology. The paper is organized as follows. [...]
  § 2.1 Mechanical Era: Mechanical calculators (Pascal, Leibniz, Babbage) were bounded by machining precision. The Analytical Engine's core constraint was physical: gear-train complexity could not scale because accumulated manufacturing error exceeded design tolerances. Wright's Law applied: each doubling of production drove cost declines, but the substrate itself capped performance.
  § 2.2 Electromechanical Era: Relays (Zuse, Harvard Mark I) switched in milliseconds and consumed power per switching event. The constraint was switching speed combined with maintenance failure rates — the Harvard Mark I's ~3,000 relays failed measurably during operation. Reliability, not raw logic, was the binding constraint.
  § 2.3 Vacuum Tube Era: ENIAC (1945) demonstrated that electronic switching could beat electromechanical by orders of magnitude, but tubes consumed kilowatts and failed frequently. The constraint was power density and mean time between failures. Tube computers were fundamentally limited by thermal management — the same constraint that would later cap CMOS.
  § 2.4 Transistor Era: The transistor removed the thermal bottleneck per switching element by orders of magnitude. Dennard scaling (1974) held that as transistors shrank, power density remained constant — enabling Moore's Law's exponential density growth for four decades. The era's defining constraint was lithographic resolution.
  § 2.5 Integrated Circuit and CMOS Era: From the microprocessor (1971) through multicore (2005) to the AI accelerator (2016), the IC era extended Dennard scaling until ~2005, when power density ended frequency scaling. [...]
  § 8. Conclusion: The next two decades will see not a single new substrate replacing silicon but a heterogeneous convergence: AI accelerators, quantum co-processors, and processing-in-memory architectures transforming the general-purpose computer into a museum artifact. The invariant dynamic across computing history — constraint saturation → substrate shift → Wright's Law cost decline → institutional adoption — is the analytic lens that makes this forecast tractable. Twelve falsifiable predictions, registered between 2030 and 2040, will test the forecast. If CMOS scaling does not effectively end by 2035, or if AI accelerators do not exceed 50% of datacenter compute spending by 2030, the central thesis is disconfirmed.