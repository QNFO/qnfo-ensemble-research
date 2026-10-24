# Constraint Adherence in Long-Form LLM Drafting: A Reliability Analysis of a Halted Sixteen-Chapter Generation Phase

## Abstract

Long-form writing projects that delegate chapter drafting to large language models (LLMs) routinely stall, but the failure is rarely analyzed quantitatively, so project owners cannot tell whether their targets are achievable at all. This paper analyzes a documented case: the "Strange Loop of Being" drafting phase, in which sixteen book chapters were drafted against a per-chapter target of roughly 2500–3000 tokens and repeated style and depth constraints, and the phase was formally halted after persistent shortfalls in length, depth, and format adherence [12]. The gap this paper addresses is the absence of a reliability model connecting per-chapter constraint adherence to phase-level success. We model the phase as a sequence of independent chapter-generation trials, each of which must simultaneously satisfy multiple constraints, and derive the per-chapter and per-constraint reliability thresholds that a sixteen-chapter phase requires. The principal result is quantitative: for a coin-flip chance (probability 0.5) that an entire sixteen-chapter phase completes without a single constraint failure, per-chapter all-constraint adherence must reach $0.5^{1/16} \approx 0.958$, and with three simultaneous constraints (length, depth, style/format, as documented in the phase report) per-constraint adherence must reach $0.5^{1/48} \approx 0.986$. At a realistic adherence of 0.9 per chapter, the probability of a failure-free phase is only $0.9^{16} \approx 0.185$. These thresholds, derived in Section 4, reframe the observed failure as a structural property of multi-constraint long-horizon generation rather than an anomaly, and they imply that drafting processes must be redesigned around sub-section decomposition, automated constraint checks, and bounded critique loops, a design direction supported by recent multi-round and review-based generation systems.

## 1. Introduction

Writers, editors, and research groups that use LLMs to draft book-length manuscripts face a specific operational problem: the model produces text that is individually plausible but collectively fails the project's constraints, and the human cost of detecting and correcting each failure falls on the project owner. The documented case analyzed here is the "Strange Loop of Being" project, whose initial drafting phase attempted sixteen chapters against an outline of 32 sections, a per-chapter length target of approximately 2500–3000 tokens, and explicit depth, integration, style, and formatting requirements. The phase was formally closed with the status "Halted for Process Review" because drafts "frequently fell short of target length," stylistic errors such as bullet-point usage and non-unique titles recurred, and several chapters were flagged as needing substantial revision for depth [12]. The cost of this failure mode is concrete: every shortfall triggers a draft–critique–revise cycle whose inefficiency the closure report itself lists as a point of failure, and the project owner must decide whether to restart drafting, restructure the outline, or abandon autonomous drafting altogether.

What would change if the failure could be anticipated arithmetically? A project owner who knew the per-chapter reliability that a sixteen-chapter phase demands could set realistic length targets from the start — a change the closure report explicitly recommends — could budget revision passes in advance, and could decide, before generation begins, whether the task complexity exceeds what the pipeline can reliably deliver. This paper supplies that arithmetic. It treats the halted phase not as an anecdote but as a case from which a general reliability model of multi-constraint long-form generation is extracted, and it connects the model's prescriptions to mechanisms demonstrated in the recent literature: bounded feedback length [1], parallel and multi-round verification structures [2], [9], [10], review-and-adjustment loops with measured ablation gains [8], and exact automated checking of formal constraints [5].

The contributions are:

- A reliability model of a multi-chapter LLM drafting phase, in which phase success requires every chapter to satisfy every constraint, with the derivation of the per-chapter threshold $p^{*} = 0.5^{1/16} \approx 0.958$ and the per-constraint threshold $q^{*} = 0.5^{1/48} \approx 0.986$ for a failure-free phase to have probability at least 0.5 (Sections 3 and 4).
- An expected-revision-pass analysis showing that at first-pass adherence $p = 0.5$ the sixteen-chapter phase requires a factor-of-2 generation overhead (32 passes against an ideal of 16), and that the overhead shrinks to approximately 4.4% at the threshold adherence $p^{*}$ (Section 4).
- A synthesis of the drafting-phase evidence with quantitative results from the literature on iterative and multi-agent generation — including APEX's ablation gain in instruction fulfillment from 7.32 to 7.97 when a review-and-adjustment module is added [8] and MARCH's clinical-fidelity F1 improvement from 0.219 (single-round, single-agent) to 0.399 (multi-round, multi-agent) [9] — used to argue that the observed failure pattern is structural and that the remedy is architectural, not motivational (Sections 2 and 5).
- A concrete redesign protocol for the halted project — sub-section decomposition, automated style checks, bounded critique length, and per-chapter acceptance gates — with the smallest next experiment that would confirm or refute the model (Section 7).

## 2. Background and Related Work

The closest antecedent to this paper is the closure report itself [12], which documents the phase this analysis models. The report records that sixteen chapters were drafted against Outline v10.0 (32 sections), that Objective 2 (adhere to length/depth, with a target of roughly 2500–3000+ tokens per chapter) was "Not Met Consistently," that Objective 3 (style/format) failed repeatedly on bullet points, concluding phrases, and unique titles, and that the draft–critique–revise cycle was inefficient because of low initial draft quality. The report also records the project's own proposed remedies: shorter initial length targets, more structured per-chapter prompts that request elaboration and integration points before generation, automated checks for stylistic errors, and breaking chapter generation into smaller sub-sections. This paper takes those qualitative lessons and supplies the quantitative reliability thresholds that determine when each remedy is necessary rather than optional.

Three works bear directly on the generation-and-verification loop that the drafting phase instantiated. PEARL addresses speculative decoding, in which a draft model proposes tokens and a target model verifies them in parallel, and identifies a "mutual waiting problem" in which each model stalls while the other works; by removing that stall, PEARL achieves up to $4.43\times$ speedup over vanilla autoregressive decoding and $1.50\times$ over vanilla speculative decoding on HumanEval across model pairs such as 7B/70B [2]. The structural analogy is exact: in the drafting phase, the human critique step is the verifier, and the sequential draft-then-critique-then-revise arrangement wastes the same kind of time that PEARL removes from token generation. S$^4$C, a speculative sampling framework with a multi-head drafting structure, reports an acceleration ratio of $2.26\times$ to $2.60\times$ over standard autoregressive decoding on the Spec-bench benchmark, under a controlled configuration (greedy decoding, FP16 precision, batch size one) designed so that variation is attributable to the acceleration method alone [10]. Its evaluation discipline — isolating the mechanism under test by fixing everything else — is the measurement standard that the next drafting-phase experiment in Section 7 adopts. APEX, an agentic system for interactive academic poster editing, reports an ablation in which removing the review-and-adjustment module drops instruction fulfillment from 7.97 to 7.32 and removing both review and API access drops it to 5.12, at a per-edit cost of \$0.022 for the full system [8]. This is direct quantitative evidence, in a document-editing domain adjacent to chapter drafting, that an explicit review loop buys adherence to user instructions — the same adherence whose absence halted the Strange Loop phase.

Two works quantify the value of multi-round, multi-agent structure. MARCH, a multi-agent framework for CT report generation, coordinates initial drafting, retrieval-augmented revision, and consensus-driven finalization; its ablation shows clinical-entity F1 rising from 0.219 (single-round, single-agent) through 0.332 (single-round, multi-agent) to 0.399 (multi-round, multi-agent), with BLEU-4 rising from 0.246 to 0.257 across the same progression [9]. The monotone improvement across rounds and agents supports this paper's claim that iteration is not a sign of process failure but a load-bearing component that must be budgeted. On the feedback side, a three-iteration deployment of LLM-generated feedback in a live programming course found that longer feedback was associated with lower next-submission correctness, more remaining attempts, and longer resubmission time, and the authors suggest that feedback systems "place bounds on response length while preserving useful guidance" [1]. This bears on the critique step of the drafting loop: the closure report's inefficient draft–critique–revise cycle plausibly suffered from critique messages that were long relative to their actionable content, and [1] provides the empirical ground for bounding them.

On verification and measurement, three works supply the tools the redesign requires. The readability project formulates integer linear programs (ILPs) for the exact computation of the graph parameter called readability, implemented for bipartite graphs in Java with IBM ILOG CPLEX, and notes that while the number of variables and constraints can be large even for moderately sized graphs, fast ILP solvers make exact checking feasible for small instances [5]. This is the template for automated constraint checking in drafting: a style or structure rule, once formalized, becomes an exact check whose cost is bounded and predictable, exactly what the closure report's suggestion of "automated checks for stylistic errors" needs. The connectomics project reports the cost of unaided human verification: manually segmenting the 300 neurons and 7000 synapses of *C. elegans* took about 12 years of part-time work by one scientist, and its own spectral-clustering implementation was slow enough (about two minutes for one example) that comparison against an existing method was left undone [6]. The lesson transferred here is that human-in-the-loop verification does not scale, so the drafting process must shift verification onto cheap automated checks and reserve human attention for depth judgments. The actor-action video classification challenge report compiles team submissions measured in precision, recall, and F1-score, with the best F1-score at 62.9 across a multi-label task of seven actor and eight action classes [3]; it demonstrates the practice of scoring every unit of output against a fixed rubric, which is what a per-chapter acceptance gate requires.

Two further works frame the broader setting. The Swiss lake-ice monitoring report motivates integrated, multi-temporal monitoring by noting that lake observables including lake ice are related to climate and are considered an Essential Climate Variable of the Global Climate Observing System, with MeteoSwiss charged with integrated monitoring across Switzerland [4]; the analogy is to treating drafting-quality metrics as a monitored variable tracked across the whole project rather than inspected once at closure. The cultural astronomy teaching paper describes the burden interdisciplinary research places on students, who must be widely read within and across disciplines to do the work [11]; the Strange Loop project — spanning cognition, symbolism, formal systems, institutions, and embodiment — carries exactly this breadth burden, which is one reason its per-chapter depth targets were hard to meet in a single pass. Finally, the perfectoid fields survey shows how a hard problem is made tractable by translation: the theory of perfectoid spaces establishes a framework relating geometric questions over local fields of mixed characteristic to questions over fields of equal characteristic, where the result is known, via the tilting functor [7]. The redesign in Section 7 applies the same move to drafting: translate a single hard sixteen-chapter generation problem into many small, independently verifiable sub-problems.

## 3. Methods

The object of analysis is the drafting phase documented in [12]. From that document we take the following inputs, each stated in the report itself: the phase attempted $N = 16$ chapters; the per-chapter length target was approximately 2500–3000+ tokens; three objectives were tracked (draft the chapters; adhere to length/depth; adhere to style/format); Objectives 2 and 3 were assessed as "Not Met Consistently"; and several chapters (10, 12, 13) were explicitly flagged as needing substantial revision for depth.

The model is a reliability model of sequential constrained generation. We define a chapter trial as a single generation pass that either satisfies all active constraints (length, depth, style/format) or does not. Let $p$ denote the per-chapter probability that a first-pass draft satisfies all constraints simultaneously, and let $q$ denote the per-constraint probability that a single constraint is satisfied on a given chapter. We assume:

1. **Independence across chapters.** The outcome of each chapter trial is independent of the others. This is an idealization; in practice a shared system prompt and shared outline create correlation, and we examine its effect in Section 6.
2. **Independence across constraints within a chapter.** The three constraint families fail independently. This is conservative in the sense that it makes joint adherence harder than correlated failure would (correlated failures concentrate failures in the same chapters, leaving more chapters clean).
3. **Phase success means zero failures.** Following the closure report's own standard — the phase was halted because inconsistencies were "persistent," not because a single chapter failed — we define phase success as all $N$ chapters passing all constraints without rework.
4. **Geometric rework.** When a chapter fails, it is regenerated until it passes, with each attempt succeeding independently with probability $p$.

Under these assumptions the probability that a phase of $N$ chapters completes without any failure is

$$P_{\text{phase}}(p) = p^{N},$$

and, if the $c$ per-chapter constraints each hold independently with probability $q$, then $p = q^{c}$ and

$$P_{\text{phase}}(q) = q^{Nc}.$$

The expected number of generation passes per chapter under geometric rework is

$$\mathbb{E}[\text{passes}] = \frac{1}{p},$$

so the expected total passes for the phase is $N/p$ against an ideal of $N$, giving an overhead factor of $1/p$.

All arithmetic is carried out explicitly in Section 4. The model contains no fitted parameters: every number is either taken from [12] or derived from the two thresholds we solve for. The literature results cited in Section 2 ([1], [2], [3], [5], [6], [8], [9], [10]) are used only as external evidence about mechanism and magnitude, never as inputs to the derivations.

## 4. Analysis

**D1. Total token budget of the phase.** The report states a per-chapter target of approximately 2500–3000+ tokens and $N = 16$ chapters [12]. The minimum budget is

$$16 \times 2500 = 40{,}000 \text{ tokens},$$

and the nominal budget is

$$16 \times 3000 = 48{,}000 \text{ tokens}.$$

Any phase-level generation plan must therefore sustain coherent constraint adherence over at least $4.0 \times 10^{4}$ output tokens, before any revision passes.

**D2. Per-chapter reliability threshold.** We solve for the per-chapter adherence $p^{*}$ at which the failure-free phase probability equals 0.5:

$$p^{*16} = 0.5 \quad\Longrightarrow\quad p^{*} = 0.5^{1/16}.$$

Computing: $\ln 0.5 = -0.693147$, so $\ln p^{*} = -0.693147/16 = -0.0433217$, and

$$p^{*} = e^{-0.0433217} \approx 0.9576.$$

Check: $0.9576^{16} = e^{16 \ln 0.9576} = e^{16 \times (-0.043322)} = e^{-0.69315} = 0.5$. ✓

So a sixteen-chapter phase has a coin-flip chance of completing without rework only if each chapter passes all constraints on the first pass with probability at least 0.958 — roughly one failure allowed per 23 chapters.

**D3. Per-constraint reliability threshold.** With $c = 3$ constraint families (length/depth, style/format, and integration/depth of argument, matching the three objectives tracked in [12]), $p = q^{3}$, so

$$q^{*} = 0.5^{1/48}.$$

Computing: $\ln q^{*} = -0.693147/48 = -0.0144406$, and

$$q^{*} = e^{-0.0144406} \approx 0.9857.$$

Check: $0.9857^{48} = e^{48 \times \ln 0.9857} = e^{48 \times (-0.014441)} = e^{-0.69317} \approx 0.500$. ✓

Each individual constraint must hold with probability at least 0.986 per chapter — about one violation per 70 constraint checks — for the phase to reach even a 50% failure-free probability.

**D4. Failure-free probability at a realistic adherence level.** Suppose each chapter passes with $p = 0.9$, i.e., one chapter in ten needs rework. Then

$$P_{\text{phase}} = 0.9^{16}.$$

Computing stepwise: $0.9^{2} = 0.81$; $0.9^{4} = 0.81^{2} = 0.6561$; $0.9^{8} = 0.6561^{2} = 0.43046721$; $0.9^{16} = 0.43046721^{2} = 0.185302$.

So at 90% per-chapter adherence, the probability that all sixteen chapters pass cleanly is about 0.185 — the phase fails without rework roughly four times out of five. This is consistent with the observed outcome: the phase was halted after persistent inconsistencies [12].

**D5. Expected rework overhead.** Under geometric rework with per-attempt success $p$, the expected passes per chapter is $1/p$ and the phase total is $N/p$.

At $p = 0.5$: expected passes per chapter $= 1/0.5 = 2$; phase total $= 16/0.5 = 32$ passes against an ideal of 16, an overhead factor of $2.0\times$.

At the threshold $p^{*} = 0.9576$: expected passes per chapter $= 1/0.9576 = 1.0443$; phase total $= 16 \times 1.0443 = 16.71$ passes, an overhead of about 4.4%.

The gap between these two cases is the arithmetic content of the closure report's complaint that the draft–critique–revise cycle was inefficient: halving first-pass adherence doubles the generation workload.

**D6. Sub-section decomposition.** The report proposes breaking chapter generation into smaller sub-sections [12]. The model shows what this buys. If a chapter of 3000 tokens is generated as $m = 4$ sub-sections of 750 tokens each, and per-sub-section adherence $r$ is independent of length, the chapter passes if all sub-sections pass: $p_{\text{chapter}} = r^{4}$. For the chapter to meet the phase threshold $p^{*} = 0.9576$,

$$r^{*} = 0.9576^{1/4} = e^{\ln(0.9576)/4} = e^{-0.0433217/4} = e^{-0.0108304} \approx 0.9892.$$

The required per-unit reliability rises from 0.958 to 0.989, so decomposition alone is not sufficient unless shorter units are genuinely more reliable; the empirical question is whether per-token adherence improves enough at 750-token units to offset the multiplication. This is exactly what the next experiment in Section 7 must measure.

**D7. Automated checking.** If the style/format constraint family is moved from generation-time adherence to post-hoc automated checking — the ILP-style exact verification pattern of [5] — then the style constraint no longer draws from the same reliability budget. With style handled by a checker of accuracy $a$, the generation-side requirement becomes $q^{*}_{\text{gen}} = 0.5^{1/32}$ (two constraint families, $Nc = 32$):

$$\ln q^{*}_{\text{gen}} = -0.693147/32 = -0.021661, \quad q^{*}_{\text{gen}} = e^{-0.021661} \approx 0.9786.$$

Moving one of three constraint families to automated checking lowers the per-constraint generation threshold from 0.986 to 0.979, and, more importantly, converts style failures from stochastic generation events into deterministic, repairable defects.

## 5. Results

All numbers below are computed in Section 4 from the inputs of [12] and the model of Section 3; none is measured anew.

- **Token budget.** The sixteen-chapter phase requires a minimum of 40,000 output tokens (16 × 2500) and a nominal 48,000 tokens (16 × 3000) before rework (D1).
- **Per-chapter threshold.** Failure-free phase completion with probability 0.5 requires per-chapter all-constraint adherence $p^{*} = 0.5^{1/16} \approx 0.958$ (D2).
- **Per-constraint threshold.** With three independent constraint families, per-constraint adherence must reach $q^{*} = 0.5^{1/48} \approx 0.986$ (D3).
- **Realistic-adherence outcome.** At $p = 0.9$, the failure-free phase probability is $0.9^{16} \approx 0.185$ (D4); the phase almost certainly requires rework, matching the halt documented in [12].
- **Rework overhead.** At $p = 0.5$ the phase needs 32 expected generation passes (2.0× the ideal 16); at $p^{*} = 0.9576$ it needs 16.71 passes (1.044×) (D5).
- **Decomposition requirement.** Splitting each 3000-token chapter into four 750-token sub-sections raises the required per-unit reliability to $r^{*} \approx 0.989$; decomposition helps only if shorter units are proportionally more reliable (D6).
- **Automated checking benefit.** Shifting the style/format family to an automated checker lowers the per-constraint generation threshold from 0.986 to $0.5^{1/32} \approx 0.979$ (D7).

As external, cited magnitudes that calibrate what iterative architectures achieve in adjacent domains: adding a review-and-adjustment module raised APEX's instruction-fulfillment score from 7.32 to 7.97 [8]; moving from single-round single-agent to multi-round multi-agent generation raised MARCH's clinical-entity F1 from 0.219 to 0.399 [9]; and bounding feedback length is recommended because longer feedback was associated with worse subsequent performance in a live course [1]. These are reported by their sources, not measured here, and they serve as directional evidence that structured iteration and bounded critique improve constraint adherence.

## 6. Discussion

The central claim of this paper is that the halted phase failed for a structural reason: a sixteen-chapter phase with three constraint families multiplies modest per-constraint shortfalls into near-certain phase-level failure, so that even 90% per-chapter adherence yields only an 18.5% chance of a clean run. The closure report's own language — "persistent inconsistencies... despite iterative refinement" [12] — is what this multiplication looks like from inside the project.

**Limitations.** The result rests on every assumption of Section 3, and each should be weighed:

- **Independence across chapters.** Shared prompts and a shared outline likely correlate failures across chapters. Positive correlation makes clean-run probability *higher* than $p^{N}$ when $p$ is high (failures cluster, leaving more chapters clean) but also makes catastrophic correlated failures possible; the threshold $p^{*} = 0.958$ is therefore an approximation whose direction of error is not fixed.
- **Independence across constraints.** Length and depth failures probably co-occur (a short draft is often a shallow one), which would concentrate failures and raise the effective clean-run probability relative to the independent model.
- **Constant $p$.** Adherence likely drifts over a long phase as context accumulates; a declining $p$ makes late chapters the binding constraint, and the single-number threshold understates the difficulty of the phase's tail.
- **Phase success as zero failures.** A process that tolerates cheap, automatically repairable failures would judge the same phase more leniently; D7 shows how much the threshold moves when one family is checked mechanically.
- **Inputs from a single case.** $N = 16$, the 2500–3000 token target, and the three objectives come from one documented phase [12]; the thresholds scale as $0.5^{1/N}$ and $0.5^{1/Nc}$, so they transfer to other phases only through those parameters.

**What would falsify the claim.** The structural explanation is falsified if a drafting process with per-chapter adherence measured at or above $p^{*} \approx 0.958$ still halts with persistent multi-constraint inconsistencies, or, conversely, if a process measured well below the threshold repeatedly completes sixteen-chapter runs without rework. Either observation would show that phase success is not governed by the product of per-chapter reliabilities, and the independence model would need replacement by a correlated or drift model. The decomposition claim (D6) is falsified if per-unit adherence at 750-token sub-sections does not exceed 0.989 in a controlled comparison against whole-chapter generation.

**Open questions.** Three stand out. First, what is the actual per-chapter adherence of the existing sixteen drafts? The closure report gives categorical assessments ("Partially Met," "Not Met Consistently") but no per-chapter pass/fail counts; a scoring pass against a fixed rubric, in the manner of the challenge report that scored every submission in precision, recall, and F1 [3], would convert the case study into data. Second, how does adherence scale with unit length? The decomposition threshold of D6 makes a concrete, measurable prediction. Third, does the critique step help or hurt? The course-deployment evidence that longer feedback was associated with lower next-submission correctness [1] raises the possibility that some of the phase's revision cycles were actively counterproductive, a hypothesis this paper cannot test from the available record.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The users are authors, editors, and project managers who run long-form LLM drafting pipelines — precisely the role the Strange Loop project owner occupied. If the reliability thresholds hold, three decisions change. First, target-setting: the report's own recommendation to "set realistic expectations... based on demonstrated performance" [12] becomes an arithmetic rule — a phase of $N$ chapters with $c$ constraint families is worth attempting autonomously only if a measured pilot shows per-chapter adherence near $0.5^{1/Nc}$. Second, process design: the draft–critique–revise loop should be re-architected as bounded, structured critique (per [1]) with explicit review-and-adjustment stages (whose measured value in an adjacent editing domain is the APEX ablation gain from 7.32 to 7.97 in instruction fulfillment [8]) and multi-round refinement (whose measured value is MARCH's F1 rise from 0.219 to 0.399 across round/agent structure [9]). Third, verification allocation: formalizable constraints (unique titles, no bullet lists, required section structure) move to automated exact checks, following the ILP pattern in which a formalized property is checkable exactly even when the check is expensive [5].

**(b) Current readiness.** This work is purely analytical: a reliability model derived from one documented phase, not peer reviewed and not validated on any new run. Against the NASA Technology Readiness Level definitions it sits at TRL 1–2 — basic principles observed and a concept formulated. No claim is made beyond analytical work; nothing here has been demonstrated in hardware, software deployment, or a new drafting run.

**(c) The smallest next experiment.** Re-draft a single flagged chapter (the report names chapters 10, 12, and 13 as needing substantial revision [12]) twice under controlled conditions: once as a whole 3000-token generation and once as four 750-token sub-sections, with the same prompt template, the same model, and a fixed scoring rubric covering length, depth, and style. The measurement is the per-unit first-pass adherence rate in each condition. The outcome that refutes the decomposition claim is a sub-section adherence at or below the