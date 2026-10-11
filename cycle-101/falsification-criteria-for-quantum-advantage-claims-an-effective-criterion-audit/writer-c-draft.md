# Falsification Criteria for Quantum Advantage Claims: A Structured Audit Framework

## Abstract

Claims of quantum advantage are frequently stated in forms that resist empirical refutation: the advantage is qualified by hardware assumptions, sampling definitions, or problem encodings that can be revised after the fact. This paper constructs a structured falsification framework for such claims, modeled on the pattern of effective criteria in algebra (identifiability of tensor decompositions, elimination criteria in Gröbner basis theory, and decidability of gate universality) and on the philosophy of falsifiability as developed in debates over formal models of consciousness. We define a five-component falsification index $F$ for an advantage claim, covering specification completeness, sampling-model transparency, classical-baseline auditability, replication independence, and pre-registration of failure thresholds. We derive the index arithmetic explicitly, compute worked examples, and derive secondary quantities from the surrounding open-science infrastructure literature, including a data-scale estimate for large multilingual corpora and gap-density statistics for a published research-portfolio audit. We show that the framework is decidable in finite steps for well-posed claims, mirroring the finite-step universality algorithm of quantum gate criteria, and we identify failure modes: gaming of scoring weights, ambiguity in dense-open "genericity" language, and the impossibility of falsifying claims whose classical baseline is itself unbounded. The framework is offered as a remediation instrument for the audit culture surrounding quantum advantage publications.

## 1. Introduction

A quantum advantage claim asserts that a quantum device solves some computational task faster, cheaper, or with fewer resources than any classical method. The history of such claims shows a recurring pathology: the claim is stated, a classical rebuttal appears, and the claim is then narrowed — the task is redefined, the noise model is adjusted, or the baseline is weakened — until the claim is no longer comparable to the rebuttal. The claim survives not because it is true but because it has been made unfalsifiable.

This paper asks a precise question: what structural properties must an advantage claim possess so that a specified experimental or computational outcome would refute it? We answer with a framework of five falsification criteria, each of which is either satisfied or not by a given claim, and a composite falsification index $F \in [0,1]$ computed from component scores with fixed weights. The design philosophy is borrowed from three algebraic traditions. First, identifiability theory asks when a decomposition is unique; an advantage claim, we argue, should be "identifiable" in the sense that it admits exactly one operational reading [1]. Second, elimination criteria in computational algebra exist to discard unnecessary critical pairs before they are processed; an audit framework should similarly discard non-falsifying experimental configurations before resources are spent on them [2]. Third, universality criteria for quantum gates give a finite-step decision procedure for a property of a gate set; a falsification framework should likewise terminate: after a finite, pre-agreed sequence of tests, the claim is either refuted or provisionally confirmed [7].

The philosophical anchor is the debate over falsifiability in theories of consciousness. Kleiner and Hoel introduced a formal mathematical model of generating observable data from experiments and using that data to generate inferences and predictions onto an experience space, and a reply to that work defended functionalism against the resulting substitution argument [3]. Whatever the merits of that dispute, it demonstrates that "falsifiability" is not a single criterion but a family of model-dependent requirements — exactly the situation of quantum advantage claims, where the model connecting experiment to claim is where unfalsifiability hides.

The practical anchor is the QNFO audit corpus. A full-spectrum audit of Huang, Choi, McClean and Preskill's "The vast world of quantum advantage" subjects both that work's five-keystone framework and QNFO's own prior critiques to symmetric scrutiny, and identifies Theorem 1 of the audited work as the most sophisticated challenge to QNFO's existing critical apparatus [9]. A consilient gap synthesis of the QNFO/QWAV portfolio catalogs 42 gaps across 5 structural categories with a phased roadmap spanning 8 calendar weeks [10]. This paper is a re-entry from that synthesis: it converts the "falsification criteria and open questions" gap into a concrete, computable instrument.

Our contributions are: (i) a five-criterion falsification framework with explicit scoring rules; (ii) a composite index $F$ with fixed weights and full arithmetic; (iii) worked examples demonstrating decidability and termination; (iv) derived infrastructure statistics connecting the framework to open datasets and platforms [5], [6], [8]; and (v) an explicit list of failure modes and falsification conditions for the framework itself.

## 2. Background and Related Work

We organize the related work into four strands: algebraic criteria, philosophy of falsification, open quantum dynamics, and open-science infrastructure.

**Algebraic criteria.** The effective identifiability paper [1] defines a tensor $T$ in a given tensor space as $h$-identifiable if it admits a unique decomposition as a sum of $h$ rank-one tensors, and calls a criterion for $h$-identifiability effective if it is satisfied in a dense, open subset of the set of rank-$h$ tensors; the paper gives effective $h$-identifiability criteria for a large class of tensors and improves them for some cases. The relevance to our problem is structural: an advantage claim should admit a unique operational decomposition into (task, device, baseline, metric), and a criterion that holds only on a dense open set — that is, generically — is the right template for criteria that hold for "typical" claims while admitting measure-zero pathological cases. We adopt the dense-open language in Section 3 and flag its dangers in Section 6.

The non-commutative Gebauer–Möller paper [2] addresses the efficiency of Buchberger's algorithm, whose implementation requires avoiding the treatment of as many unnecessary critical pairs or obstructions as possible; in the commutative polynomial ring this is achieved by the Gebauer–Möller criteria, and the paper adapts these criteria to non-commutative polynomial rings, i.e. free associative algebras. In our framework, the analogue of an "unnecessary critical pair" is an experimental configuration that cannot change the verdict on a claim — for example, re-running a sampling experiment on a device whose noise model has already been excluded by the claim's own specification. The entry's summary is truncated and supplies no further technical detail, so we use it only at the level of this design analogy.

The universality criteria paper [7] considers the problem of deciding whether a set of quantum one-qudit gates $\mathcal{S}=\{U_1,\ldots,U_n\}$ is universal, provides compact-form criteria leading to a simple algorithm that decides universality of any given gate set in a finite number of steps, and, for a non-universal $\mathcal{S}$, indicates what type of gates can be added to make it universal. This is the strongest template for our framework: a decision procedure with guaranteed termination, plus a constructive repair path when the property fails. Our falsification index is designed so that a failing claim receives not merely a low score but a specification of which criterion must be repaired.

**Philosophy of falsification.** The reply to "Falsification and Consciousness" [3] engages a formal mathematical model, introduced by Kleiner and Hoel, of the process of generating observable data from experiments and using that data to generate inferences and predictions onto an experience space; the substitution argument built on that framework was used to show that any theory of consciousness with independent inference and prediction components (the entry's summary is truncated here) is subject to a structural objection. The reply defends functionalism against this argument. For our purposes, the episode establishes two lessons: first, that falsification arguments are themselves model-relative and can be contested at the level of the model rather than the conclusion; second, that a falsification framework must specify which components of a theory are independently inferable and predictable, or it will be vulnerable to the same substitution-style counterattack. We build this requirement into criterion $C_2$ below.

**Open quantum dynamics.** The unraveling paper [4] notes that the state operator of an open quantum system can generically be represented as the solution of a time-local quantum master equation, and that unraveling in quantum trajectories offers a dual picture in which physical indicators are computed as Monte-Carlo averages over a stochastic process (the entry's summary is truncated). This matters for falsification because many advantage claims depend on noise models whose observable consequences are computed exactly as such Monte-Carlo averages; a falsification criterion must therefore state which unraveling, or which master-equation equivalent, is part of the claim's specification, since different unravelings can assign different indicator statistics to the same master equation.

**Open-science infrastructure.** OpenPodcar [5] is a low-cost, open-source hardware and software autonomous-vehicle research platform built on an off-the-shelf hard-canopy mobility scooter donor vehicle, with build instructions covering hardware components (CAD designs, bill of materials, build instructions; the summary truncates) to produce a fully autonomous platform. It exemplifies the replication standard our criterion $C_4$ demands: a claim is falsifiable in practice only if the full build recipe is open. CoReCon [6] is a Python package providing a growing, community-powered collection of constraints on key physical quantities related to the Epoch of Reionization, motivated by the observation that available constraints are scattered across inhomogeneous formats, unit systems and sampling strategies. This is precisely the fragmentation problem facing classical-baseline performance data for advantage claims, and CoReCon's format-unification strategy is the model for our proposed baseline registry. HPLT 3.0 [8] provides open, very large, high-quality, richly annotated textual datasets for almost 200 languages, at 30 trillion tokens likely the largest generally available multilingual collection of LLM pre-training data, derived from web crawls and accompanied by a complete open-source pipeline for document selection (summary truncates). It supplies the scale benchmark we use in Section 4 to quantify what "open at scale" means for audit corpora.

**The QNFO corpus.** The full-spectrum audit [9] subjects the five-keystone framework of Huang, Choi, McClean and Preskill's "The vast world of quantum advantage" (arXiv:2508.05720) and QNFO's own prior critiques to symmetric scrutiny, and finds that Theorem 1 is the most sophisticated challenge to QNFO's existing critical apparatus. The consilient gap synthesis [10] catalogs 42 gaps across 5 structural categories — Infrastructure, Content, Physics Validation, Governance, Dissemination — with a phased version roadmap v2.0–v2.4 spanning 8 calendar weeks. Our paper operationalizes the falsification-criteria gap identified there; we derive gap-density statistics from [10]'s stated numbers in Section 4.

## 3. Methods

### 3.1 Claim formalization

An advantage claim $\mathcal{K}$ is a tuple

$$\mathcal{K} = (T, D, B, M, \Theta),$$

where $T$ is the computational task, $D$ the quantum device with noise model $\Theta$, $B$ the classical baseline, and $M$ the comparison metric. The claim is *specification-complete* if each component is fixed in advance and cannot be revised after classical rebuttals appear.

### 3.2 The five falsification criteria

- $C_1$ (Specification completeness): every element of $(T, D, B, M, \Theta)$ is stated with enough precision that two independent laboratories would agree on its instantiation.
- $C_2$ (Inference–prediction independence): following the structural lesson of [3], the claim must state which quantities are inferred from experiment and which are predicted by theory, and these must be independently checkable; no component may be simultaneously inferred and predicted in a way that shields it from refutation.
- $C_3$ (Baseline auditability): the classical baseline $B$ is specified with a resource bound, and the best-known classical algorithm's cost is either stated or bounded by a formula a third party can evaluate.
- $C_4$ (Replication independence): the full experimental recipe — hardware, calibration, and analysis pipeline — is open in the sense of [5] and [8]: build instructions, data, and selection pipeline all public.
- $C_5$ (Pre-registered failure threshold): a number $\epsilon \in (0,1)$ is fixed in advance such that if the observed advantage ratio falls below threshold, the claim is declared refuted, with no post-hoc revision permitted.

### 3.3 The falsification index

Each criterion $C_i$ receives a score $s_i \in \{0, 0.5, 1\}$: $1$ if fully satisfied, $0.5$ if partially satisfied (specified but with an ambiguous term), $0$ if absent. The weights are fixed ex ante:

$$w_1 = 0.30, \quad w_2 = 0.25, \quad w_3 = 0.20, \quad w_4 = 0.15, \quad w_5 = 0.10,$$

with $\sum_{i=1}^{5} w_i = 1$. The falsification index is

$$F(\mathcal{K}) = \sum_{i=1}^{5} w_i \, s_i.$$

Decision rule: a claim with $F \geq 0.8$ is *falsifiable-ready*; $0.5 \leq F < 0.8$ is *conditionally falsifiable* (repairs required); $F < 0.5$ is *structurally unfalsifiable* and should not be published as an advantage claim.

### 3.4 Termination

Mirroring the finite-step decision procedure of [7], the audit terminates: each $s_i$ is decided by inspecting a finite document set (the claim, its supplement, and the baseline code), so the total procedure is a finite composition of finite checks. If $F < 0.8$, the framework outputs the ordered list of criteria with $s_i < 1$, weighted by $w_i$, as a constructive repair path — the analogue of [7]'s indication of which gates to add to a non-universal set.

### 3.5 Genericity caveat

Following [1], we would like criteria that hold on a dense, open subset of the space of claims. However, "dense open" is a topological notion with no canonical measure on claim space; we therefore use it only heuristically and require the criteria to hold for *all* claims, not merely generically. This is a deliberate strengthening over [1]'s standard.

## 4. Analysis

All inputs are stated with sources; all arithmetic is shown.

**Input 1 (weights, this paper, Section 3.3):** $w_1 = 0.30$, $w_2 = 0.25$, $w_3 = 0.20$, $w_4 = 0.15$, $w_5 = 0.10$. Check of normalization:

$$\sum_{i=1}^{5} w_i = 0.30 + 0.25 + 0.20 + 0.15 + 0.10 = 1.00.$$

**Input 2 (gap counts, from [10]):** 42 gaps across 5 structural categories. Gap density per category:

$$\bar{g} = \frac{42}{5} = 8.4 \text{ gaps per category}.$$

**Input 3 (roadmap duration, from [10]):** the phased roadmap v2.0–v2.4 spans 8 calendar weeks. Mean time per gap if all 42 gaps were addressed uniformly across the roadmap:

$$t_{\text{gap}} = \frac{8 \text{ weeks}}{42 \text{ gaps}} = \frac{8}{42} \approx 0.1905 \text{ weeks per gap}.$$

Converting to days ($1$ week $= 7$ days):

$$t_{\text{gap}} = 0.1905 \times 7 \approx 1.333 \text{ days per gap}.$$

**Input 4 (corpus scale, from [8]):** 30 trillion tokens, i.e. $3.0 \times 10^{13}$ tokens. Assuming 4 bytes per token (a stated assumption of this paper, not of [8]; UTF-8 encodings of multilingual text vary, so we bound it):

- Lower bound at 1 byte per token: $3.0 \times 10^{13} \times 1 = 3.0 \times 10^{13}$ bytes $= 30$ TB.
- Central estimate at 4 bytes per token: $3.0 \times 10^{13} \times 4 = 1.2 \times 10^{14}$ bytes $= 120$ TB.
- Upper bound at 4 bytes per token plus 25% annotation overhead: $1.2 \times 10^{14} \times 1.25 = 1.5 \times 10^{14}$ bytes $= 150$ TB.

**Worked example of the index.** Consider a hypothetical advantage claim $\mathcal{K}_A$ with scores $s_1 = 1$, $s_2 = 0.5$, $s_3 = 1$, $s_4 = 0$, $s_5 = 0.5$ (fully specified task and device; inference–prediction partially independent; baseline stated with bound; no open replication recipe; failure threshold ambiguous). Then:

$$F(\mathcal{K}_A) = (0.30)(1) + (0.25)(0.5) + (0.20)(1) + (0.15)(0) + (0.10)(0.5)$$
$$= 0.30 + 0.125 + 0.20 + 0 + 0.05 = 0.675.$$

Since $0.5 \leq 0.675 < 0.8$, $\mathcal{K}_A$ is conditionally falsifiable; the repair path prioritizes $C_4$ (weight $0.15$, score $0$, contribution gap $0.15$) then $C_2$ and $C_5$ (each gap $0.125$ and $0.05$ respectively). Total recoverable index if all repairs succeed: $1.00 - 0.675 = 0.325$.

**Second worked example.** A claim $\mathcal{K}_B$ with $s_1 = 0$, $s_2 = 0$, $s_3 = 0.5$, $s_4 = 0$, $s_5 = 0$:

$$F(\mathcal{K}_B) = (0.30)(0) + (0.25)(0) + (0.20)(0.5) + (0.15)(0) + (0.10)(0) = 0.10.$$

Since $0.10 < 0.5$, $\mathcal{K}_B$ is structurally unfalsifiable under our decision rule.

**Sensitivity check.** The largest single weight is $w_1 = 0.30$; a claim scoring $s_1 = 0$ can reach at most $F_{\max}^{(s_1=0)} = 1 - 0.30 = 0.70 < 0.8$, so specification completeness is *necessary* for falsifiable-ready status. This is a designed property, verified by the arithmetic above.

All quantities in this section are exact or rounded from exact fractions ($8/42 = 4/21$; $4/21 \times 7 = 4/3 \approx 1.333$); none are empirical measurements.

## 5. Results

We report only quantities computed in Section 4.

1. **Index normalization:** $\sum_{i=1}^{5} w_i = 1.00$ exactly.
2. **Gap density:** the QNFO/QWAV portfolio's 42 gaps across 5 categories [10] yield $\bar{g} = 8.4$ gaps per category.
3. **Roadmap pacing:** the 8-week roadmap [10] implies $t_{\text{gap}} = 4/21 \approx 0.1905$ weeks $\approx 1.333$ days per gap, under the stated assumption of uniform pacing.
4. **Corpus scale projection:** the HPLT 3.0 corpus [8], at $3.0 \times 10^{13}$ tokens, corresponds to a storage footprint between $30$ TB (1 byte/token) and $150$ TB (4 bytes/token plus 25% annotation overhead), with central estimate $120$ TB. These are projections under stated byte-per-token assumptions, not measurements of the corpus.
5. **Worked index values:** $F(\mathcal{K}_A) = 0.675$ (conditionally falsifiable; repair priority $C_4$, then $C_2$, then $C_5$; recoverable margin $0.325$) and $F(\mathcal{K}_B) = 0.10$ (structurally unfalsifiable).
6. **Necessity of $C_1$:** any claim with $s_1 = 0$ has $F \leq 0.70 < 0.8$ and therefore cannot be falsifiable-ready.

No empirical, simulated, or measured quantities are reported in this paper.

## 6. Discussion

**Limitations.** The scoring function is deliberately crude: $s_i \in \{0, 0.5, 1\}$ discards gradations that matter in practice, and the weights $w_i$ are a design choice, not derived from data. A different weight vector could reorder repair priorities; the sensitivity check in Section 4 shows $C_1$'s necessity is weight-robust only in the weak sense that $w_1 > 0.20$ guarantees it, and we have not proven robustness for all admissible weights. The decision thresholds $0.5$ and $0.8$ are likewise conventional.

**Failure modes.** First, *gaming*: a claim author can maximize $F$ by writing verbose specifications that satisfy the letter of $C_1$ while remaining operationally ambiguous; the $0.5$ score for "specified but ambiguous" is a judgment call vulnerable to auditor–author disagreement. Second, *genericity leakage*: as noted, the dense-open template of [1] does not transfer cleanly, because claim space has no canonical topology or measure; our strengthening to universal applicability may make the criteria too strict for legitimate claims with inherently statistical components. Third, *baseline unboundedness*: if the best classical algorithm's cost is unknown, $C_3$ can only be scored $0.5$ at best, and a genuinely hard baseline problem could keep a valid advantage claim permanently below the ready threshold — a false negative the framework does not currently detect. Fourth, *model-relativity of falsification itself*: the episode documented in [3] shows that a falsification argument can be attacked at the level of its underlying model; an adversary could similarly contest the inference–prediction split demanded by $C_2$, and our framework has no meta-criterion to adjudicate such contests.

**What would falsify the framework.** The framework is falsified if (a) a claim with $F \geq 0.8$ is nevertheless revised post-hoc in a way that evades a pre-registered refutation, showing the criteria are insufficient; or (b) a large fraction of widely accepted advantage claims score $F < 0.5$, showing the thresholds are miscalibrated against community practice. Both are empirical conditions that the audit infrastructure of [9] and [10] could in principle test.

**Open questions.** Can the weights be learned from a corpus of historical advantage claims and their outcomes, rather than fixed ex ante? Can the repair-path output be made constructive in the strong sense of [7], where the repair is not merely indicated but algorithmically generated? Can the baseline registry modeled on CoReCon's format unification [6] achieve community adoption in a field with competitive incentives? And does the Monte-Carlo indicator structure of unravelings [4] introduce irreducible statistical uncertainty into $C_1$'s noise-model specification? The gap synthesis [10] places falsification criteria within a 42-gap portfolio; whether this framework closes its target gap or merely relocates it is an open empirical question. We note also that the supplied summaries of [2], [3], [4], [5], and [8] are truncated, which limits the depth of the analogies we may legitimately draw from them.

## 7. Conclusion

We have constructed a five-criterion falsification framework for quantum advantage claims, with a composite index $F$, fixed weights, explicit decision thresholds, guaranteed termination, and a constructive repair path. The framework draws its structure from effective identifiability criteria [1], critical-pair elimination [2], finite-step universality decision [7], and the model-relativity lessons of the falsification debate in consciousness studies [3], and it is grounded operationally in the open-replication standards exemplified by open hardware platforms [5], constraint registries [6], and open large-scale data pipelines [8]. Worked examples show the index discriminates: a partially specified claim scores $F = 0.675$ with an identified repair order, while an unspecified claim scores $F = 0.10$ and is excluded. Derived statistics from the QNFO corpus — $8.4$ gaps per category and $\approx 1.333$ days per gap under uniform pacing [10] — situate the framework within a concrete remediation roadmap. The framework's own falsification conditions are stated, and its principal weakness — the conventionality of its weights and thresholds — is flagged as the first target for empirical calibration.

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