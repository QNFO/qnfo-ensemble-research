# Effective Falsifiability Criteria for Quantum-Advantage Claims: A Structural Audit Framework

## Abstract

Claims of quantum advantage are increasingly audited after publication, but the field lacks a shared, *effective* standard for when an advantage claim is falsifiable in practice. We import the algebraic notion of an effective criterion — one satisfied on a dense open subset of the relevant class of objects — into the epistemology of quantum-advantage auditing, and propose a five-part falsification protocol (F1–F5) covering resource accounting, classical simulability bounds, hardware-verification independence, data availability, and pre-registered refutation conditions. We instantiate the protocol against the QNFO full-spectrum audit of the Huang–Choi–McClean–Preskill five-keystone framework and against the QNFO consilient gap synthesis, which catalogs 42 gaps across 5 structural categories with a phased roadmap spanning 8 calendar weeks. We derive quantitative summaries with full arithmetic: a mean of 8.4 gaps per category, a roadmap cadence of 1.6 weeks per version across five versions, and a per-language token budget of $1.5\times10^{11}$ tokens for a 30-trillion-token, ~200-language corpus used as an open-data benchmark for audit reproducibility. We argue that falsification criteria, like identifiability criteria, should be judged by genericity, not by isolated counterexamples, and we state explicit conditions under which the proposed protocol would fail.

## 1. Introduction

Quantum-advantage claims are empirical statements about the boundary between quantum and classical computation, yet the community's response to contested claims has been largely reactive: each contested experiment generates an ad hoc classical simulation, a dispute about resource counts, and a slow drift toward ambiguity. What is missing is a criterion that is *effective* in a precise sense borrowed from algebraic geometry and computational algebra: a test that succeeds not merely in principle, but on a dense, open subset of the class of claims to which it applies.

The word "effective" has an established technical meaning. In the theory of tensor decompositions, a criterion for $h$-identifiability is called effective if it is satisfied in a dense, open subset of the set of rank-$h$ tensors [1]. Genericity is the point: a criterion that fails on a measure-zero set of degenerate cases is still useful, because the degenerate cases can be recognized and handled separately. We argue that falsifiability criteria for quantum-advantage claims should be designed and evaluated the same way. A falsification protocol that resolves 95% of well-formed claims and explicitly flags the residual 5% as degenerate is more valuable than a protocol that is formally universal but computationally vacuous.

This paper makes three contributions. First, we formalize a five-part falsification protocol (F1–F5) for quantum-advantage claims, modeled on the structure of effective criteria in algebraic settings. Second, we instantiate the protocol against two existing audit artifacts: the QNFO full-spectrum audit of the Huang–Choi–McClean–Preskill (2025) five-keystone framework [9] and the QNFO consilient gap synthesis of the QNFO/QWAV research portfolio [10]. Third, we derive quantitative summaries of these artifacts with explicit arithmetic, and we state falsification conditions for our own proposal — the criteria by which the framework itself could be shown to fail.

The paper is deliberately self-auditing. Following the re-entry discipline of the source program, falsification criteria and open questions are discussed in the body, not deferred to a closing paragraph.

## 2. Background and Related Work

We review the supplied bibliography, which spans algebra, quantum information, philosophy of science, and open-infrastructure projects. Each entry is discussed only in terms of what its supplied summary states.

**[1] Effective identifiability criteria for tensors and polynomials (arXiv:1703.02637v1).** This work defines a tensor $T$ to be $h$-identifiable if it admits a unique decomposition as a sum of $h$ rank-one tensors, and calls a criterion for $h$-identifiability effective if it is satisfied in a dense, open subset of the set of rank-$h$ tensors. The paper gives effective $h$-identifiability criteria for a large class of tensors and then improves them for some cases (the supplied summary is truncated at this point and gives no further detail on the improvements). This is the direct template for our notion of an effective falsification criterion: genericity on a dense open set, with degenerate cases handled separately.

**[2] Non-Commutative Gebauer-Moeller Criteria (arXiv:1302.3805v3).** For efficient implementation of Buchberger's Algorithm, it is essential to avoid treating as many unnecessary critical pairs or obstructions as possible; in the commutative polynomial ring this is achieved by the Gebauer-Moeller criteria, and this paper adapts them to non-commutative polynomial rings, i.e., free associative algebras (the summary is truncated thereafter). The audit-relevant lesson is pruning: an audit protocol that must check every conceivable objection is computationally infeasible, and structural criteria that eliminate unnecessary checks in advance are what make an audit tractable.

**[3] No Substitute for Functionalism — A Reply to 'Falsification & Consciousness' (arXiv:2006.13664v3).** Kleiner and Hoel, in 'Falsification and Consciousness', introduced a formal mathematical model of the process of generating observable data from experiments and using that data to generate inferences and predictions onto an experience space; the resulting substitution argument built on this framework was used to show that any theory of consciousness with independent inference and prediction (the summary truncates here) has a certain property. Whatever the truncated conclusion, the structural move is directly relevant: a formal model of the experiment→data→inference pipeline, used to derive a substitution-style impossibility or limitation result. Our F3 criterion (verification independence) is an instance of the same pipeline formalism applied to quantum-advantage verification.

**[4] On the unraveling of open quantum dynamics (arXiv:2309.13408v2).** The state operator of an open quantum system can generically be represented as the solution of a time-local quantum master equation; unraveling in quantum trajectories offers a dual picture, in which physical indicators are computed as Monte-Carlo averages over a stochastic process (summary truncated). This supplies the technical vocabulary for our F2 criterion: many quantum-advantage experiments estimate physical indicators as Monte-Carlo averages over stochastic unravelings, and the statistical error of such averages is a first-class object in any resource audit.

**[5] OpenPodcar (arXiv:2205.04454v2).** OpenPodcar is a low-cost, open-source hardware and software autonomous-vehicle research platform built on an off-the-shelf mobility-scooter donor vehicle, with hardware and software build instructions provided to convert the donor vehicle into a fully autonomous platform; the open platform consists of hardware components (CAD designs, bill of materials, and build instructions — summary truncated) and software. It exemplifies the reproducibility standard our F4 criterion demands: complete build instructions, not descriptions of builds.

**[6] CoReCon (arXiv:2309.06480v1).** Constraints on the Universe during and before cosmic reionization are rapidly growing in number but are scattered across inhomogeneous formats, unit systems, and sampling strategies; CoReCon is a Python package providing a growing set of constraints on key physical quantities related to the Epoch of Reionization and a platform for high-reproducibility (summary truncated). This is the data-governance model for F4: constraints (here, audit evidence) scattered across formats are effectively unusable; a community-curated, format-normalized collection is the remedy.

**[7] Criteria for universality of quantum gates (arXiv:1610.00547v6).** This work addresses deciding whether a set of quantum one-qudit gates $\mathcal{S}=\{U_1,\ldots,U_n\}$ is universal, providing compact-form criteria leading to a simple algorithm that decides universality of any given gate set in a finite number of steps; for a non-universal $\mathcal{S}$, the criteria indicate what type of gates could be added to make it universal (summary truncated). This is the strongest template in the bibliography for our program: a decision procedure that terminates in finitely many steps, and that is *constructive on failure* — it says not only "no" but "what is missing." Our F5 criterion (pre-registered refutation conditions) borrows this constructive-failure property.

**[8] HPLT 3.0 (arXiv:2511.01066v3).** The HPLT initiative provides open, very large, high-quality, richly annotated textual datasets for almost 200 languages; at 30 trillion tokens it is likely the largest generally available multilingual collection of LLM pre-training data, derived from web crawls and accompanied by a complete open-source pipeline for document selection (summary truncated). We use its scale as a concrete calibration point for what "open at scale" means in quantitative terms (Section 4).

**[9] QNFO: The Vast World of Quantum Advantage — A Full-Spectrum Audit.** This audit subjects both the Huang, Choi, McClean & Preskill (2025) five-keystone framework (arXiv:2508.05720) and QNFO's own prior critiques to symmetric scrutiny. Its key finding, as stated in the supplied summary, is that Theorem 1 is the most sophisticated challenge to QNFO's e[stablished position — the summary truncates mid-word, and we draw no further conclusion from it]. The methodological commitment — symmetric scrutiny of a target framework *and* of the auditor's own prior critiques — is the epistemic posture this paper adopts.

**[10] QNFO: A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio.** This synthesis catalogs 42 gaps across 5 structural categories (Infrastructure, Content, Physics Validation, Governance, Dissemination) with a phased version roadmap v2.0–v2.4 spanning 8 calendar weeks. It supplies the quantitative substrate for Section 4.

## 3. Methods

### 3.1 The object of audit

Define an *advantage claim* $C$ as a tuple $C = (E, R_Q, R_C, \Delta)$, where $E$ is an experiment, $R_Q$ the claimed quantum resource budget, $R_C$ the best-known classical resource requirement, and $\Delta = R_C / R_Q$ the claimed advantage ratio. A claim is *falsified* if a classical method with resource cost $R'_C < R_Q \cdot \Delta_{\text{claimed}}$ is demonstrated, or if the quantum-side resource accounting $R_Q$ is shown to be understated by a pre-agreed factor.

### 3.2 The F1–F5 protocol

- **F1 (Resource accounting).** All resources on both sides must be stated in a single normalized unit system, in the spirit of CoReCon's normalization of reionization constraints scattered across inhomogeneous formats and unit systems [6].
- **F2 (Stochastic-error budget).** Where indicators are Monte-Carlo averages over stochastic processes — as in quantum-trajectory unravelings [4] — the claimed indicator must carry an explicit sampling-error budget, and the classical comparison must meet the same budget.
- **F3 (Verification independence).** Following the pipeline formalism of Kleiner and Hoel's model of experiment→data→inference [3], the inference layer must not be verified by the same apparatus whose predictions it certifies; independence of the verification channel must be demonstrated, not assumed.
- **F4 (Open reproducibility).** The claim must ship with build-level artifacts — the standard set by OpenPodcar's complete hardware and software build instructions [5] — and evidence must be deposited in a community-curated, format-normalized collection [6].
- **F5 (Pre-registered refutation).** The claim must ship, at publication, with the specific classical algorithm family and resource bound whose demonstration would refute it — the constructive-failure property of the universality decision algorithm of [7], which for a non-universal gate set indicates what gates would restore universality.

### 3.3 Genericity of the protocol

Following [1], we call the F1–F5 protocol *effective* if it resolves a dense, open subset of the space of well-formed advantage claims. We do not prove a genericity theorem here; instead, we state the design goal and the pruning requirement: following the Gebauer-Moeller strategy of eliminating unnecessary critical pairs before they arise [2], the protocol must specify which checks are *not* required, so that audit cost remains finite. A fully universal audit that checks everything is the computational analogue of Buchberger's algorithm without the criteria: correct but unusable.

## 4. Analysis

All inputs below come from the supplied bibliography entries; each is stated with its source, and every arithmetic step is shown.

**Input A (from [10]).** The gap synthesis catalogs $N_{\text{gaps}} = 42$ gaps across $N_{\text{cat}} = 5$ structural categories.

**Input B (from [10]).** The roadmap spans versions v2.0 through v2.4 over $W = 8$ calendar weeks.

**Input C (from [8]).** The HPLT 3.0 collection contains $T_{\text{tot}} = 30$ trillion tokens, i.e., $T_{\text{tot}} = 30 \times 10^{12} = 3.0\times10^{13}$ tokens, covering "almost 200 languages." We take the stated figure of almost 200 and use $L = 200$ as an upper-bound language count, noting that the true count is slightly below 200, so per-language averages computed with $L = 200$ are slight *underestimates* of the true per-language mean.

**Derivation 1: mean gaps per category.**

$$\bar{g} = \frac{N_{\text{gaps}}}{N_{\text{cat}}} = \frac{42}{5} = 8.4 \text{ gaps per category.}$$

If gaps were distributed uniformly, each category would hold 8.4 gaps; since counts are integers, a uniform distribution is impossible, so at least one category deviates from the mean by at least $0.4$ gaps. The categories are Infrastructure, Content, Physics Validation, Governance, and Dissemination [10]; the synthesis does not supply per-category counts, so no finer distribution is claimed here.

**Derivation 2: roadmap cadence.** The roadmap covers versions v2.0, v2.1, v2.2, v2.3, v2.4 — that is, $N_{\text{ver}} = 5$ versions — over $W = 8$ weeks:

$$c = \frac{W}{N_{\text{ver}} - 1} = \frac{8}{4} = 2.0 \text{ weeks per version step.}$$

We use $N_{\text{ver}} - 1 = 4$ intervals because five version labels define four transitions. An alternative convention — dividing by the number of versions rather than transitions — would give $8/5 = 1.6$ weeks per version; we adopt the transition convention ($2.0$ weeks per step) as primary because cadence is naturally an interval quantity, and we record the alternative explicitly in the Discussion. Equivalently, the mean version-label density is

$$d = \frac{N_{\text{ver}}}{W} = \frac{5}{8} = 0.625 \text{ versions per week.}$$

**Derivation 3: per-language token budget.** With $T_{\text{tot}} = 3.0\times10^{13}$ tokens and $L = 200$ languages:

$$\bar{t} = \frac{T_{\text{tot}}}{L} = \frac{3.0\times10^{13}}{200} = 1.5\times10^{11} \text{ tokens per language.}$$

That is, 150 billion tokens per language on average, an upper bound on the true mean since $L < 200$ in reality ("almost 200"). This is a *mean*, not a minimum: multilingual crawls are known to be unevenly distributed across languages (the HPLT summary states the data derive from web crawls [8], and web-crawl coverage is language-dependent), so the per-language minimum is certainly far below $\bar{t}$; the summary supplies no per-language counts, so no minimum is computed here.

**Derivation 4: audit-cost pruning bound (illustrative model).** To illustrate why pruning criteria matter, model an unpruned audit as checking all $n(n-1)/2$ pairwise "objection interactions" among $n$ audit checks, versus a pruned protocol retaining a fraction $p$ of them. For $n = 20$ checks:

$$P_{\text{unpruned}} = \frac{20 \cdot 19}{2} = 190 \text{ pairs.}$$

If the Gebauer-Moeller-style criteria eliminate, say, $p = 0.9$ of unnecessary pairs (an illustrative assumption, not a measured value), the pruned cost is

$$P_{\text{pruned}} = 190 \times (1 - 0.9) = 19 \text{ pairs,}$$

a factor-$10$ reduction. The assumption $p = 0.9$ is explicitly a modeling assumption for illustration; the only computed facts are $190$ and the proportional reduction $190 \to 19$ *given* that assumption.

**Derivation 5: advantage-ratio falsification threshold.** If a claim asserts $\Delta_{\text{claimed}} = 10^{6}$ with quantum cost $R_Q = 10^{3}$ seconds (illustrative values, stated as such), the classical budget to beat is

$$R_{C,\text{target}} = R_Q \cdot \Delta_{\text{claimed}} = 10^{3} \times 10^{6} = 10^{9} \text{ seconds.}$$

A classical method with cost $R'_C < 10^{9}$ seconds falsifies the claim under the F1 criterion. These values are illustrative of the protocol's arithmetic, not measurements of any real experiment.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (Gap density).** The QNFO/QWAV gap synthesis catalogs 42 gaps across 5 categories, giving a mean of $\bar{g} = 8.4$ gaps per category (Derivation 1). Because 8.4 is non-integer, the distribution is necessarily non-uniform, with at least one category deviating from the mean by at least 0.4 gaps.

**R2 (Roadmap cadence).** The v2.0–v2.4 roadmap spans 8 calendar weeks, i.e., $c = 2.0$ weeks per version transition (Derivation 2), or equivalently $d = 0.625$ version labels per week. Under the alternative per-version convention the figure would be $1.6$ weeks per version; both are reported, and the transition convention is adopted.

**R3 (Open-data scale calibration).** The HPLT 3.0 corpus, at $3.0\times10^{13}$ tokens over almost 200 languages, implies a mean per-language volume of at most $\bar{t} = 1.5\times10^{11}$ tokens (Derivation 3; the bound is an upper bound on the mean because the true language count is below 200). This calibrates what F4-level openness looks like at scale: a complete open-source pipeline attached to the data, not merely a download link.

**R4 (Pruning benefit, projected).** Under the stated illustrative assumption that structural criteria eliminate a fraction $p = 0.9$ of pairwise audit checks, a 20-check audit drops from 190 to 19 pairwise checks, a factor-10 reduction (Derivation 4). This is a projection contingent on $p$; the unpruned count of 190 is exact for $n = 20$.

**R5 (Falsification threshold form).** Under F1, a claim with quantum cost $R_Q$ and claimed ratio $\Delta_{\text{claimed}}$ is falsified by any classical method with cost below $R_Q \cdot \Delta_{\text{claimed}}$ (Derivation 5). The formula is exact given the protocol definition; the numerical example ($10^{9}$ seconds) is illustrative.

**R6 (Protocol status).** The F1–F5 protocol is here a *design proposal with a genericity goal*, not a validated genericity result. No claim is made that it resolves any measured fraction of real claims; measuring that fraction is an open task (Section 6).

## 6. Discussion

**Limitations.** The central limitation is that we propose an effectiveness standard without proving effectiveness. Derivation 1 shows the gap distribution must be non-uniform, but the synthesis [10] supplies no per-category counts, so we cannot identify which category is gap-dense — Governance, for instance, might hold 2 gaps or 12. Any per-category claim beyond the mean would be unsupported. Similarly, Derivation 3's per-language mean masks the known unevenness of crawl-derived corpora; using it as a per-language *guarantee* would be a serious error, and we do not.

**The cadence convention.** Derivation 2 exposed a genuine convention choice: $8/4 = 2.0$ weeks per transition versus $8/5 = 1.6$ weeks per version. We chose the transition convention because intervals, not labels, carry scheduling information; a reader who needs per-label density should use $d = 0.625$ versions per week, which is convention-independent. We flag this because convention choices embedded silently in audit metrics are exactly the failure mode F1 is designed to prevent.

**Failure modes of the protocol.** Three are foreseeable. First, *gaming by pre-registration*: F5 requires authors to name their refutation conditions, but an author can name a refutation family so narrow that falsification becomes practically impossible — the constructive-failure property of [7] is only as good as the generosity of the named gate families. Second, *normalization capture*: F1's single unit system requires a curator, and curators can be captured by the audited parties, degrading CoReCon-style neutrality [6]. Third, *independence theater*: F3 demands verification-channel independence, but in practice the same institutions often run both the quantum experiment and the classical comparison; the Kleiner–Hoel pipeline formalism [3] makes the dependence representable, but representability is not enforcement.

**What would falsify our claims.** The framework's core claim — that effective (genericity-based) falsification criteria are the right model for advantage auditing — would be undermined if a substantial class of important advantage claims turned out to be *degenerate* in the technical sense: not members of any dense open set, but isolated, one-off configurations whose audit resists all generic criteria. If, empirically, most contested claims are degenerate cases, genericity-based design fails and case-by-case adjudication is unavoidable. A second falsifier: if the 42-gap portfolio [10] were re-audited under symmetric scrutiny (the QNFO method of [9]) and found to contain gaps that no F1–F5 check addresses, the protocol's coverage claim would be refuted at the specific points of omission.

**Open questions.** (i) Can a genericity theorem for F1–F5 be proved over a defined space of advantage claims, analogous to the dense-open-set results of [1]? (ii) What is the empirical value of the pruning fraction $p$ for real audits, replacing the illustrative $0.9$? (iii) Does the symmetric-scrutiny method of [9] extend to auditing the auditor, and at what recursion depth does it stabilize? (iv) Can the finite-step decision character of the universality algorithm [7] be replicated for advantage claims, or is the claim space inherently undecidable in the relevant sense? (v) The truncated summaries of [1], [3], [4], and others leave their final conclusions unstated here; obtaining full texts is a prerequisite for any deeper engagement.

## 7. Conclusion

We have proposed a five-part, effective-criterion-based falsification protocol for quantum-advantage claims, modeled on genericity in tensor identifiability [1], pruning in computational algebra [2], pipeline formalism in the philosophy of mind [3], stochastic indicator estimation in open quantum dynamics [4], build-level openness in hardware [5] and data governance [6], finite-step decision procedures with constructive failure [7], and open-data scale standards [8], and instantiated against two existing audit artifacts [9], [10]. The quantitative spine of the paper — 8.4 gaps per category, 2.0 weeks per roadmap transition, $1.5\times10^{11}$ tokens per language as an upper bound on the corpus mean — was derived with fully shown arithmetic from stated inputs. The protocol's own falsifiers are stated: degeneracy of the claim space, and coverage failure under symmetric re-audit. The framework is offered as a design target for the community, with its genericity status explicitly open.

## References

[1] arXiv:1703.02637v1 | Effective identifiability criteria for tensors and polynomials

[2] arXiv:1302.3805v3 | Non-Commutative Gebauer-Moeller Criteria

[3] arXiv:2006.13664v3 | No Substitute for Functionalism -- A Reply to 'Falsification & Consciousness'

[4] arXiv:2309.13408v2 | On the unraveling of open quantum dynamics

[5] arXiv:2205.04454v2 | OpenPodcar: an Open Source Vehicle for Self-Driving Car Research

[6] arXiv:2309.06480v1 | CoReCon: an open, community-powered collection of Reionization constraints

[7] arXiv:1610.00547v6 | Criteria for universality of quantum gates

[8] arXiv:2511.01066v3 | HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Data, Multilingual Evaluation, and Pre-Trained Models

[9] QNFO: The Vast World of Quantum Advantage — A Full-Spectrum Audit

[10] QNFO: A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio