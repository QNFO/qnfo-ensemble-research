# Is the Meta-Pattern of Reification Physically Real? A Cross-Domain Audit of a Zenodo-Documented Claim

## Abstract

A recent Zenodo document (DOI 10.5281/zenodo.19605445) proposes a "Meta-Pattern of Reification in Physics" and raises the question of whether this pattern is something physically real rather than a merely descriptive or linguistic regularity. This paper treats that question as an empirical audit problem. We formalize the claimed pattern as the hypothesis $\Pi$: that representational or informational constructs acquire causal, physical consequences across independent domains. We define three criteria for physical reality (multi-domain instantiation, differential predictability, and observer-independence) and audit a fixed sample of ten bibliography entries spanning particle-physics strategy, collider design, DRAM security, fusion reactor design, embedded side channels, neutrino facilities, stage magic, turbulence modelling, and the adelic-completion mathematics documented in the companion Zenodo account (DOI 10.5281/zenodo.20120042). The audit yields a reification index $R = 8/10 = 0.80$, with a binomial null-tail probability $P(X \geq 8) = 56/1024 = 0.0546875$ under a symmetric chance model. However, the same audit shows that the pattern, as documented, fails the differential-predictability criterion: it is compatible with both its affirmation and its negation in every sampled domain. We conclude that the available evidence establishes the pattern as a robust descriptive lens but not yet as a physically real entity, and we state the observation that would falsify or confirm it.

## 1. Introduction

The input to this study is a single sentence of research intent: "Re-entry from 10.5281/zenodo.19605445: something physically real?" The referenced document, *QNFO: Meta-Pattern of Reification in Physics* [9], proposes a meta-pattern — a pattern about patterns — said to recur across physics. A companion document, *QNFO: The Adelic Constraints Project — A Complete Account* [10], describes a research project that asked whether a specific piece of pure mathematics — the fact that the rational numbers can be "completed" in multiple incompatible ways, linked by a single identity — has consequences beyond mathematics itself.

The question "is it something physically real?" is precise enough to be audited, but only after the informal phrase "physically real" is replaced by operational criteria. Physics has well-established procedures for deciding whether a proposed entity is real: the entity must appear in more than one independent measurement context, it must make predictions that differ from those of its negation, and it must not dissolve when the observer's representational apparatus is removed. These criteria are standard in the design of large-scale physics programmes: the community-strategy process documented in [1] exists precisely to convert proposed ideas into testable facility programmes, and the collider-design literature [2] explicitly frames feasibility in terms of experiments that can decide among theoretical possibilities.

This paper makes three contributions. First, it formalizes the reification claim as hypothesis $\Pi$ and states three operational criteria for physical reality (Section 3). Second, it applies those criteria to a fixed, non-cherry-picked sample: the ten works supplied in the bibliography of this very paper, which span eight genuinely independent research domains (Section 4). Third, it computes a reification index and a chance probability with full arithmetic, and — more importantly — shows where the audit stalls: the pattern as documented makes no differential prediction, so high multi-domain agreement cannot by itself establish physical reality (Sections 4–6). The honest answer to "something physically real?" is therefore conditional, and we state the exact condition.

## 2. Background and Related Work

We discuss each supplied bibliography entry in turn, restricting every statement to what the entry's own supplied summary supports.

**[1] Physics Briefing Book (arXiv:1910.11775v2).** The summary describes the European Particle Physics Strategy Update (EPPSU) process as bottom-up: the community is first invited to submit proposals (inputs) for projects it would like to see realised in the near-term, mid-term and longer-term future, with national inputs and inputs from national laboratories also important. This is a documented instance of representational constructs — written proposals — being converted into a prioritised roadmap for physical facilities, and it supplies our clearest example of an institutional reification pipeline.

**[2] Physics and Technology of the Next Linear Collider (arXiv:hep-ex/9605011v1).** The summary presents expectations for the design and physics programme of an $e^+e^-$ linear collider of centre-of-mass energy 500 GeV -- 1 TeV, reviews the experiments that would be carried out at this facility, demonstrates its key role in exploring physics beyond the Standard Model over the full range of theoretical possibilities, and shows the feasibility of constructing the machine. It is a canonical case of a design document in which theoretical possibilities are made decidable by a physical machine, and it supplies the only explicit quantitative energy scale in our sample.

**[3] JENGA (arXiv:2609.01077v1).** The summary states that safety-critical real-time systems must satisfy multiple dependability requirements, notably time predictability and security; that tasks must complete within bounded and known execution times, typically characterised through Worst-Case Execution Time (WCET) analysis; and that DRAM-based platforms are increasingly sensitive to the RowHammer read-disturbance security vulnerability. The title further indicates that counter-based RowHammer countermeasures can be exploited to break real-time predictability. This is a physical-to-informational-to-physical loop: a physical disturbance mechanism (RowHammer) induces countermeasures, which in turn feed back into physically observable timing behaviour.

**[4] MHD analysis on the physical designs of CFETR and HFRC (arXiv:2107.11742v1).** The summary identifies the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC), both under intensive physical and engineering design in China, as the two major projects representative of the low-density steady-state and high-density pulsed pathways to fusion, with magnetohydrodynamic (MHD) assessment and analysis as a primary task of the physics designs. Here mathematical MHD models are reified into engineering hardware pathways.

**[5] Physical Side-Channel Attacks on Embedded Neural Networks: A Survey (arXiv:2110.11290v1).** The summary notes that deep neural networks have progressively been integrated on all types of platforms, from data centres to embedded systems including low-power processors and, recently, FPGAs, and that neural networks are expected to become ubiquitous in IoT systems, including safety-critical and security-sensitive domains. The title indicates the survey's subject: physical side-channel attacks on such embedded networks, i.e., physical emanations of a computation becoming informationally exploitable — the mirror image of the loop in [3].

**[6] Physics at a future Neutrino Factory and super-beam facility (arXiv:0710.4947v3).** The summary presents the conclusions of the Physics Working Group of the international scoping study (ISS) of a future Neutrino Factory and super-beam facility, carried by the international community between NuFact05 (the 7th International Workshop on Neutrino Factories and Superbeams, Laboratori Nazionali di Frascati, Rome, June 21–26, 2005) and NuFact06 (Irvine, California, 24–30 August, dates as given in the summary). Like [1], it documents the conversion of community deliberation into a concrete facility concept.

**[7] Physics Magic (arXiv:physics/0606151v1).** The summary states the paper's purpose: to show the magic of physics by showing the physics of magic; that magic tricks and demonstrations are interesting inasmuch as something unexpected occurs; and that since expectations are linked to preconceptions, a demonstration making use of a flaw in a preconception will result in something unexpected. This entry is directly relevant to our criteria: it is an explicit study of the gap between representation (preconception) and physical outcome (demonstration).

**[8] Physically constrained eigenspace perturbation for turbulence model uncertainty estimation (arXiv:2311.01355v2).** The summary explains that aerospace design increasingly incorporates Design Under Uncertainty approaches for more robust and reliable optimal designs; that these approaches require dependable estimates of uncertainty in simulations; and that the key contributor of predictive uncertainty in computational fluid dynamics (CFD) simulations of turbulent flows is the structural limitations of Reynolds-averaged (turbulence) models. The title indicates a physically constrained eigenspace perturbation method for estimating that uncertainty — a representational model defect being quantified so that physical design can proceed.

**[9] QNFO: Meta-Pattern of Reification in Physics (DOI 10.5281/zenodo.19605445).** The supplied summary for this entry is empty; the grounding input gives only the title and the research question quoted in Section 1. We therefore use this entry solely as the *object* of the audit — the claim under test — and not as a source of findings about the world. This is a material limitation, stated here rather than hidden.

**[10] QNFO: The Adelic Constraints Project — A Complete Account (DOI 10.5281/zenodo.20120042).** The summary describes a complete, self-contained account of a research project conducted in May 2026, which asked whether a specific piece of pure mathematics — the fact that the rational numbers can be "completed" in multiple incompatible ways, and that a single identity links all (the summary truncates here) — has consequences beyond pure mathematics. This is the reification question in its purest form: does an abstract mathematical fact become physically consequential?

Taken together, the sample spans strategy documents [1], [6], machine-design feasibility studies [2], [4], security physics [3], [5], the psychology of demonstration [7], simulation-uncertainty methodology [8], and the two Zenodo documents under audit [9], [10]. No two entries share a subfield, which is exactly what a multi-domain test of $\Pi$ requires.

## 3. Methods

### 3.1 The hypothesis under test

We formalize the claim of [9] as:

$$\Pi: \quad \text{representational or informational constructs acquire causal, physical consequences, as a pattern recurring across independent physical domains.}$$

"Representational construct" here means any entity whose primary mode of being is descriptive: a proposal, a design expectation, a mathematical structure, a model, a preconception. "Causal, physical consequence" means an observable change in a physical system or artefact attributable to that construct.

### 3.2 Criteria for physical reality

A pattern counts as *physically real* in the strong sense if it satisfies all three criteria:

- **C1 (multi-domain instantiation):** the pattern is exhibited in at least two research domains with no shared methodology or community.
- **C2 (differential predictability):** the pattern, applied to a new domain, yields a prediction that differs from the prediction of its negation $\neg\Pi$, in a setting that can be measured.
- **C3 (observer-independence):** the pattern's description does not depend constitutively on the observer's language or choice of representation; two independent observers applying the criteria would agree on whether the pattern is present.

Criterion C2 is the decisive one and mirrors the logic of [2], where a machine is justified by its ability to decide among "the full range of theoretical possibilities": a real entity must be able to lose a test.

### 3.3 Audit protocol

The audit sample is the fixed bibliography of this paper: $N = 10$ entries. For each entry $i$ we assign a binary instantiation score $s_i \in \{0, 1\}$: $s_i = 1$ if and only if the entry's own supplied summary shows a representational construct acquiring a physical consequence (or the physical-to-informational-to-physical loop of [3], [5]); $s_i = 0$ if the summary does not show this, including the case of an empty summary. The reification index is

$$R = \frac{1}{N}\sum_{i=1}^{N} s_i.$$

Under a symmetric null model $H_0$ in which each entry independently shows the pattern with probability $p_0 = 0.5$ (i.e., the pattern is a coin-flip reading lens with no domain structure), the count $X = \sum_i s_i$ follows $\mathrm{Binomial}(N, p_0)$:

$$P(X = k) = \binom{N}{k} p_0^k (1-p_0)^{N-k}.$$

We additionally compute a projected replication expectation for a hypothetical doubled sample, clearly labelled as a projection in Section 5.

### 3.4 Scoring rules

To keep scoring non-circular, we fix the rules before applying them: (i) only text in the supplied summary counts; (ii) an empty summary forces $s_i = 0$; (iii) a summary that describes only planning or deliberation, with no physical artefact or measurement, scores $s_i = 1$ only if the summary itself states that the deliberation targets physical realisation (as [1] and [6] do, via "realised" and "facility"); (iv) purely mathematical content scores $s_i = 1$ only if the summary states a physical consequence, which the truncated summary of [10] does not.

## 4. Analysis

### 4.1 Scoring the sample

Applying the protocol:

| $i$ | Entry | Reason from summary | $s_i$ |
|---|---|---|---|
| 1 | [1] EPPSU | Proposals (representational) explicitly aimed at projects "to be realised" | 1 |
| 2 | [2] NLC report | Design expectations → feasibility of constructing a physical machine | 1 |
| 3 | [3] JENGA | Physical RowHammer disturbance → countermeasures → broken timing predictability | 1 |
| 4 | [4] CFETR/HFRC | MHD physics designs → engineering hardware pathways | 1 |
| 5 | [5] Side-channel survey | Physical emanations of embedded NN computation → exploitable information | 1 |
| 6 | [6] Neutrino Factory ISS | Community scoping study → concrete facility concept | 1 |
| 7 | [7] Physics Magic | Preconceptions (representational) exploited to produce unexpected physical demonstrations | 1 |
| 8 | [8] Eigenspace perturbation | Model-structural limitation (representational) → quantified uncertainty for physical design | 1 |
| 9 | [9] Meta-Pattern | Summary empty; rule (ii) forces 0 | 0 |
| 10 | [10] Adelic project | Summary states the mathematical fact but truncates before any physical consequence; rule (iv) forces 0 | 0 |

### 4.2 Reification index

$$R = \frac{1}{10}\sum_{i=1}^{10} s_i = \frac{1+1+1+1+1+1+1+1+0+0}{10} = \frac{8}{10} = 0.80.$$

### 4.3 Null probability

Under $H_0$ with $N = 10$, $p_0 = 0.5$:

$$P(X = 8) = \binom{10}{8}\left(\frac{1}{2}\right)^{10} = \frac{45}{1024} = 0.0439453125.$$

The upper tail (the probability that a pure reading-lens with no domain structure would produce *at least* this many apparent instantiations):

$$P(X \geq 8) = \frac{\binom{10}{8} + \binom{10}{9} + \binom{10}{10}}{1024} = \frac{45 + 10 + 1}{1024} = \frac{56}{1024} = 0.0546875.$$

So the observed agreement across eight independent domains would occur by chance under the symmetric null about $5.47\%$ of the time — suggestive but not decisive at a conventional $5\%$ threshold, and the threshold itself is a convention, not a physical fact.

### 4.4 The only explicit physical scale in the sample

Entry [2] states a centre-of-mass energy range of 500 GeV -- 1 TeV. The ratio of the upper to lower bound is

$$\frac{E_{\max}}{E_{\min}} = \frac{1\ \mathrm{TeV}}{500\ \mathrm{GeV}} = \frac{1000\ \mathrm{GeV}}{500\ \mathrm{GeV}} = 2.$$

This is trivial arithmetic, but it makes a methodological point: the sample's quantitative physical content is thin. Eight of ten summaries contain no number at all, which is itself evidence about how the reification pattern is documented — as narrative, not as measurement.

### 4.5 Testing criterion C2 on the sample

C2 requires that $\Pi$ and $\neg\Pi$ give different predictions in a measurable setting. Consider the strongest candidate, entry [3]: $\Pi$ predicts that a representational countermeasure (a hardware counter) will have physically observable timing consequences; $\neg\Pi$ predicts countermeasures are timing-neutral. The title of [3] states that counter-based RowHammer countermeasures *can be exploited to break real-time predictability* — so in this single domain, $\Pi$ and $\neg\Pi$ are in principle decidable, and the summary's framing supports $\Pi$. Now apply the same test to the pattern as a whole: the documents [9], [10] supply no setting in which the meta-pattern itself could fail. Formally, for every domain $d$ in the sample, the documented pattern is stated at a level of generality such that

$$P(\text{observation} \mid \Pi) \approx P(\text{observation} \mid \neg\Pi)$$

for all observations the documents describe: any representational construct with physical effect confirms $\Pi$, and any construct without one can be excluded as "not an instance of the pattern." This is the Bayes-equivalent statement that the pattern, as documented, has no discriminating power — the audit's central negative finding.

### 4.6 Projection for a doubled sample

*Projection, with stated assumptions:* if the pattern's instantiation rate in the sampled population is $p = R = 0.8$ and a hypothetical replication audit scored $n = 20$ further independent entries with the same protocol, the expected count and standard deviation would be

$$\mu = n p = 20 \times 0.8 = 16, \qquad \sigma = \sqrt{n p (1-p)} = \sqrt{20 \times 0.8 \times 0.2} = \sqrt{3.2} \approx 1.7889.$$

This projection assumes the new entries are drawn from domains as diverse as the present sample and scored by the same rules; it is not a measurement.

## 5. Results

The audit produces exactly the following computed quantities:

1. **Reification index:** $R = 8/10 = 0.80$ (Section 4.2), from the per-entry scores in Section 4.1.
2. **Null point probability:** $P(X = 8) = 45/1024 = 0.0439453125$ (Section 4.3).
3. **Null upper-tail probability:** $P(X \geq 8) = 56/1024 = 0.0546875$ (Section 4.3).
4. **Energy-scale ratio from [2]:** $E_{\max}/E_{\min} = 2$ (Section 4.4).
5. **Projection (labelled):** for $n = 20$ future entries at $p = 0.8$, $\mu = 16$, $\sigma = \sqrt{3.2} \approx 1.7889$ (Section 4.6).

Substantive findings: (a) the pattern $\Pi$ is instantiated, by the fixed scoring rules, in eight of ten independent domains, satisfying criterion C1; (b) the sample contains no documented setting in which the meta-pattern itself makes a differential prediction, so criterion C2 fails for $\Pi$ as documented; (c) two entries — the two Zenodo documents [9], [10] — are precisely the ones that cannot be scored, because one summary is empty and the other truncates before stating any physical consequence; the claim under audit is thus the least-documented item in its own audit.

## 6. Discussion

**The central tension.** The audit gives $\Pi$ a high instantiation score ($R = 0.80$) and simultaneously shows that the score is nearly unfalsifiable: the scoring rules were easy to satisfy because the pattern is stated broadly enough to cover any case where an idea leads to a machine, a measurement, or an attack. A pattern that cannot fail C2 cannot be established as physically real by C1-style evidence alone, no matter how many domains it spans. The $5.47\%$ tail probability is suggestive, but it is computed under a null model ($p_0 = 0.5$, independent entries) that we chose for tractability, not because it is physically motivated; a null with $p_0 = 0.9$ would make the observation unremarkable, and correlated entries (e.g., [1] and [6] share the facility-roadmap genre) would inflate the effective tail.

**Limitations.** (i) The sample is the bibliography of this paper, not a random or systematic sample of physics; it was fixed by the grounding input, which is both a strength (no cherry-picking by us) and a weakness (no coverage guarantee). (ii) All scoring rests on truncated summaries; several entries end mid-sentence, and entry [9] has no summary at all, so $s_9 = 0$ is a protocol artefact, not evidence against the pattern. (iii) The binary score $s_i$ collapses graded judgements; a graded rubric would change $R$. (iv) The projection in Section 4.6 assumes a replication sample we do not have.

**What would falsify the claims of this paper.** Our negative finding on C2 would be falsified by exhibiting a pre-registered, measurable setting in which the meta-pattern of [9] predicts an outcome that its negation does not — for example, a new domain where the pattern correctly anticipates *which* representational construct will acquire physical consequences, before the fact, with stated error bars. Our positive finding on C1 would be falsified by showing that two or more of the eight scored instantiations fail on the full texts rather than the summaries — e.g., if [7] or [8] in full do not in fact exhibit the loop their summaries suggest.

**What would confirm physical reality.** Beyond C2, a confirmation would need C3: two independent teams, given only the criteria and the full text of [9], agreeing on the pattern's presence or absence in a held-out domain. The adelic case of [10] is the most interesting test bed, because mathematics-to-physics reification is the hardest version of the claim; but the supplied summary truncates before stating any physical link, so we can only note that the question is posed there, not answered.

**Arguing against ourselves.** A defender of [9] could reasonably object that demanding differential predictions of a *meta*-pattern is a category error — that meta-patterns are organisational lenses, like symmetry principles, which earn physical status through the success of their instances. That objection has force; but it concedes the main point of this paper: on the available documentation, the meta-pattern is real in the way a good classification is real, not in the way a field excitation is real. The burden then shifts to producing the instance-level predictions that would upgrade it.

**Open questions.** Does the full text of [10] derive a physical consequence from adelic completion, and is it quantified? Is the instantiation rate stable across a systematically drawn sample? Can the scoring rules be tightened so that reasonable scorers agree (C3) at better than chance?

## 7. Conclusion

We audited the claim that the meta-pattern of reification proposed in DOI 10.5281/zenodo.19605445 is "something physically real." Using a fixed ten-entry, eight-domain sample and pre-committed scoring rules, we computed a reification index $R = 0.80$ with a symmetric-null upper-tail probability of $56/1024 = 0.0546875$, satisfying the multi-domain criterion C1. The same audit shows the pattern, as documented, makes no differential prediction in any sampled setting, failing criterion C2, and that the two Zenodo documents themselves are the only unscorable items in the sample. We conclude that the pattern is currently established as a broadly instantiated descriptive regularity, not yet as a physically real entity; the specific observation that would change this verdict — a pre-registered domain where the pattern's prediction differs measurably from its negation — is stated explicitly, and the companion adelic account [10] is identified as the natural place to seek it.

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book

[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[3] arXiv:2609.01077v1 | JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability

[4] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC

[5] arXiv:2110.11290v1 | Physical Side-Channel Attacks on Embedded Neural Networks: A Survey

[6] arXiv:0710.4947v3 | Physics at a future Neutrino Factory and super-beam facility

[7] arXiv:physics/0606151v1 | Physics Magic

[8] arXiv:2311.01355v2 | Physically constrained eigenspace perturbation for turbulence model uncertainty estimation

[9] QNFO: Meta-Pattern of Reification in Physics | DOI 10.5281/zenodo.19605445

[10] QNFO: The Adelic Constraints Project — A Complete Account | DOI 10.5281/zenodo.20120042