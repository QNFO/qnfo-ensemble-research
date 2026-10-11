# Structured Cross-Domain Translation as a Testable Consilience Mechanism: Protocol Design, Formal Conditions for Truth-Preserving Analogy, and a Computational Evaluation Blueprint

## Abstract

Interdisciplinary analogy-making is usually treated as an ad hoc rhetorical act rather than a reproducible research procedure. This paper formalizes a structured cross-domain translation (SCDT) protocol in which a single formal object—a theorem, model, or framework—is deliberately rendered into multiple domain lexicons (physics, computer science, cognitive science, information theory), after which a forced synthesis step must produce a unified meta-principle. We make three contributions. First, we give a formal characterization of when a cross-lexicon analogy is truth-preserving rather than spurious, based on relation-preserving mappings and a Jaccard-type structural-overlap score, with a worked derivation. Second, we derive the combinatorial cost structure of the protocol: for $n_t$ source objects and $n_d$ target lexicons, the method generates $n_t \binom{n_d}{2}$ pairwise analogy hypotheses, and we compute the expert-validation budget for a concrete configuration. Third, we specify a computational evaluation blueprint—LLM agents run with and without the protocol on a fixed benchmark, scored for novelty, expert-rated analogy validity, and predictive power of the synthesis step—and derive, under explicitly stated binomial assumptions, the statistical power such a study would need. We situate the proposal against the cross-domain machine-translation and transfer literature and against the QNFO consilience framework. The contribution is a testable, falsifiable design; no empirical results are reported here, and all quantitative forward-looking statements are labeled projections.

## 1. Introduction

Analogy is the oldest tool of theory construction and the least disciplined. When a researcher says that an information channel "is like" a thermodynamic engine, or that a cognitive architecture "is like" a compiler, the claim is usually evaluated informally, after the fact, and cannot be reproduced or falsified as a procedure. The research idea examined here—the QNFO-style conjecture that systematically translating one formal object into several domain lexicons and forcing a unified meta-principle synthesis produces genuine consilience—proposes to change this: to treat interdisciplinary analogy-making as a structured, repeatable operation whose outputs can be counted, rated, and checked against later confirmation.

The conjecture has three components that must be separated before they can be tested:

1. **Translation**: a single formal object $O$ is rendered into $n_d$ distinct domain lexicons, each rendering using the native primitives of the target domain.
2. **Comparison**: the $n_d$ renderings are compared pairwise, generating candidate structural analogies.
3. **Synthesis**: a forced unification step produces a single meta-principle claimed to hold across the domains, which is then treated as a prediction about connections no single-domain analysis would have produced.

The central scientific question is not whether such analogies *feel* illuminating but whether the procedure (a) generates hypotheses that are novel relative to single-domain baselines, (b) generates analogies that experts judge valid, and (c) produces syntheses whose claimed cross-domain connections survive later scrutiny. Each is measurable in principle; none has been measured under a controlled protocol, as far as the grounding material for this paper indicates.

This paper is deliberately a design-and-analysis paper, not an empirical one. We define the protocol formally (Section 3), derive its combinatorial and statistical structure with full arithmetic (Section 4), state formal conditions under which a lexicon crosswalk constitutes real isomorphism rather than surface similarity (Section 4), and specify the computational experiment that would confirm or falsify the conjecture (Sections 5 and 6). We report no measurements; every forward-looking number is a projection with stated assumptions.

## 2. Background and Related Work

The relevant literature falls into three clusters: cross-domain transfer in machine learning, structured generation/decoding in translation systems, and prior consilience frameworks. We discuss eight works from the supplied bibliography; we note explicitly where an entry's summary is too thin to support more than a minimal statement.

**Cross-domain transfer as an engineering problem.** A consistent finding across the applied literature is that naive reuse across domains fails, and that success requires an explicit mechanism for identifying what carries over. In cross-domain offline reinforcement learning, the core challenge is stated as identifying and utilizing source samples most relevant to the target domain, with existing approaches measuring domain gaps through domain classifiers, target transition dynamics modeling, or mutual information [4]. This is directly analogous to our problem: when translating a formal object into a new lexicon, most of the source structure is irrelevant, and the protocol needs an explicit relevance filter—our structural-overlap score in Section 4 plays that role. In cross-domain dependency parsing, a neural parser built on stack-pointer networks with self-attention representations was submitted to the NLPCC 2019 shared task on semi-supervised cross-domain adaptation [3]; the entry's summary describes the system architecture but supplies no results, so we cite it only as evidence that cross-domain adaptation is treated as a defined shared-task problem with fixed evaluation—an evaluation discipline our proposal imports into analogy-making. In cross-domain facial action unit detection, existing vision-based approaches are described as heavily susceptible to variation across domains, motivating a decoupled doubly contrastive adaptation approach to learn a purified, semantically structured representation [6]. The notion of "purifying" a representation before transfer maps onto our requirement that each domain rendering strip domain-specific surface features before comparison. In egocentric video reasoning, the EgoCross challenge at CVPR 2026 evaluates multimodal large language models reasoning across surgery, industry, extreme sports, and animal perspective, formulated as a robust cross-domain embodied video reasoning problem; the authors report achieving second place in both the Source-Limited and Open-Source tracks [5]. This is the closest existing instance of "one reasoner, many domain lexicons," though for perception rather than formal objects; the entry's summary is truncated and supplies no further methodological detail.

**Structured generation and selection.** Our protocol's comparison and synthesis steps are search procedures over a space of candidate analogies, and the translation literature offers the relevant control mechanisms. Neural machine translation trains a large network to maximize translation performance on a parallel corpus and then uses a left-to-right beam-search decoder that approximately maximizes the trained conditional probability [2]; the entry's summary is truncated before describing the specific beam strategies, so we use it only for the foundational point that translation quality depends on structured decoding rather than greedy one-step choice—an argument for making our synthesis step a beam over candidate meta-principles rather than a single shot. Transductive data-selection algorithms for fine-tuning NMT adapt a model to a given test set by selecting training data matched to the target's characteristics, on the premise that models trained for particular document characteristics perform better [8]; the summary is truncated and gives no algorithmic detail, but the selection-before-adaptation principle supports our design choice that the synthesis step should condition on the specific object being translated, not on a generic prompt. For low-resource settings, work on massively parallel cross-lingual learning identifies three challenges—lack of low-resource data, effective cross-lingual transfer, and the variable-binding problem common in neural systems—and builds a translation system tested across eight European language families [7]. The variable-binding problem is directly relevant: a domain lexicon is precisely a binding scheme between abstract roles and domain-specific fillers, and instability of that binding is one candidate mechanism for spurious analogy, which we formalize in Section 4. Finally, in image generation, off-the-shelf diffusion models have been shown to perform a wide range of cross-domain compositing tasks—image blending, object immersion, texture replacement, CG2Real translation and stylization—using a localized, iterative procedure [1]; the summary is truncated mid-description of that procedure, but the demonstrated existence of many distinct cross-domain "translation" modes within a single generative model illustrates the plausibility of one object carrying multiple lexicon renderings.

**Prior consilience frameworks.** The QNFO corpus supplies the immediate intellectual context. The Consilience Framework document describes a synthesis of valuation theory with a foundational hierarchy (void, distinction, ZFC, valuation) together with a "Universal Consilience Prompt" and an autonomous four-phase LLM research workflow [9]. Our protocol can be read as a formalization and evaluation plan for the translation-and-synthesis phases of such a workflow; crucially, [9] supplies no empirical evaluation, which is exactly the gap this paper addresses. Three further QNFO entries—Epistemic Dynamics [10], Syntactic Generation [11], and the Ultrametric Consilience Atlas on cross-domain applications of $p$-adic mathematical structure [12]—have summaries that supply no substantive content beyond their titles; we therefore cite them only as evidence that a program of cross-domain structural application exists in this corpus, and draw no methodological claims from them.

In summary, the neighboring literature treats cross-domain transfer as a solved-enough engineering problem with explicit gap-measurement, purification, and selection mechanisms, and treats translation itself as a structured decoding problem. What it does not contain—per the supplied materials—is a controlled test of structured multi-lexicon translation as an *ideation* mechanism. That is the gap this paper targets.

## 3. Methods

### 3.1 Definitions

Let $O$ be a formal object (theorem, model, or framework), represented as a relational structure:

$$O = (E_O, R_O)$$

where $E_O$ is a set of entities (variables, states, operators) and $R_O$ is a set of relations among them (equalities, orderings, dynamics, type constraints). A **domain lexicon** $L_i$ ($i = 1, \dots, n_d$) is a pair $(V_i, \rho_i)$ where $V_i$ is a vocabulary of domain primitives and $\rho_i$ is a typing map assigning each primitive a role signature. A **rendering** of $O$ in $L_i$ is a map:

$$\tau_i : E_O \to V_i \cup \{\bot\}$$

where $\bot$ denotes "no faithful rendering exists in this lexicon." A rendering is **admissible** if every relation in $R_O$ among rendered entities has a well-typed counterpart in $L_i$.

### 3.2 The SCDT protocol

The protocol has four phases, mirroring the four-phase workflow structure described in the QNFO Consilience Framework [9]:

1. **Phase T (Translate)**: produce renderings $\tau_1, \dots, \tau_{n_d}$ of the same object $O$, one per lexicon, each required to be admissible or to explicitly report $\bot$.
2. **Phase C (Compare)**: for each pair $(i, j)$, extract the candidate analogy: a bijection $\phi_{ij}$ between rendered entity sets, together with the set of relations preserved under $\phi_{ij}$.
3. **Phase S (Synthesize)**: force a single meta-principle $M$ stated in lexicon-neutral terms, required to specialize to each rendering. Following the beam-search principle that structured decoding outperforms greedy choice [2], Phase S maintains a beam of $B$ candidate meta-principles rather than one.
4. **Phase V (Validate)**: score novelty against single-domain baselines, submit analogies for expert rating, and register syntheses as predictions.

### 3.3 Truth-preservation condition

The central formal question is when the crosswalk $\phi_{ij}$ constitutes real isomorphism rather than surface similarity. We define:

**Definition (Truth-preserving crosswalk).** The crosswalk $\phi_{ij} : \tau_i(E_O) \to \tau_j(E_O)$ is truth-preserving for $O$ if there exists a bijection $\phi_{ij}$ such that for every relation $r \in R_O$ and all tuples of rendered entities, $r$ holds on the $L_i$ side if and only if its $\phi_{ij}$-image holds on the $L_j$ side.

Full truth-preservation is an isomorphism; partial preservation is graded. We quantify it with a structural-overlap score:

$$s(\phi_{ij}) = \frac{|R^{+}_{ij}|}{|R^{+}_{ij}| + |R^{-}_{ij}| + |R^{0}_{ij}|}$$

where $R^{+}_{ij}$ is the set of relations preserved by $\phi_{ij}$, $R^{-}_{ij}$ the set preserved in the reverse direction only (image holds but source does not, or vice versa), and $R^{0}_{ij}$ the set of relations with no image under $\phi_{ij}$. This is a Jaccard-type score on the relation sets. A crosswalk with $s(\phi_{ij}) = 1$ is a true isomorphism; $s(\phi_{ij}) = 0$ means no relation survives, i.e., pure surface similarity.

**Spuriousness criterion.** A candidate analogy is classified spurious if $s(\phi_{ij}) < \theta$ for a pre-registered threshold $\theta$, or if the preserved relations are all of arity 1 (unary predicates carry no relational structure). The variable-binding instability noted for neural cross-lingual systems [7] motivates an additional check: re-rendering with a perturbed lexicon (synonym substitution within $V_i$) must leave $s(\phi_{ij})$ unchanged to within a pre-registered tolerance; sensitivity to lexical perturbation indicates that the analogy rides on surface wording rather than structure.

### 3.4 Evaluation design

The computational experiment compares two conditions on a fixed benchmark of $n_t$ formal objects:

- **Baseline condition**: LLM agents asked, per object, for "interdisciplinary insights," with no protocol.
- **SCDT condition**: the same agents run through Phases T–S with $n_d$ fixed lexicons.

Outcome measures: (a) novelty of cross-domain hypotheses, judged against a pre-registered corpus of known connections; (b) expert-rated validity of analogies on a defined scale; (c) predictive success of Phase-S syntheses, scored by whether registered connections are later confirmed. This mirrors the shared-task discipline of cross-domain adaptation benchmarks [3], [5].

## 4. Analysis

All numbers in this section are derived here from stated inputs. Forward-looking quantities are labeled projections with their assumptions.

### 4.1 Combinatorial cost of the protocol

**Inputs** (design choices, stated here as protocol parameters): $n_t = 10$ formal objects on the benchmark; $n_d = 4$ domain lexicons (physics, computer science, cognitive science, information theory, per the research idea).

**Step 1.** Number of renderings produced:

$$N_{\text{rend}} = n_t \cdot n_d = 10 \times 4 = 40$$

**Step 2.** Number of pairwise comparisons per object:

$$\binom{n_d}{2} = \frac{4 \times 3}{2} = 6$$

**Step 3.** Total pairwise analogy hypotheses across the benchmark:

$$N_{\text{hyp}} = n_t \binom{n_d}{2} = 10 \times 6 = 60$$

**Step 4.** Expert-validation budget. Assume (stated assumption) each hypothesis requires one expert rating of 5 minutes. Total rating time:

$$T_{\text{rate}} = 60 \times 5\ \text{min} = 300\ \text{min} = 5.0\ \text{h}$$

With (stated assumption) 3 independent raters per hypothesis for reliability, the budget triples:

$$T_{\text{rate}}^{(3)} = 3 \times 5.0\ \text{h} = 15.0\ \text{h}$$

**Step 5.** Baseline comparison set. The baseline condition produces, per object, an unstructured set of insights; assume (stated assumption) the baseline yields on average $k_0 = 2$ cross-domain hypotheses per object, i.e., $N_0 = 10 \times 2 = 20$ hypotheses to rate under the identical rubric, at $20 \times 5 \times 3 = 300\ \text{min} = 5.0\ \text{h}$ of rater time. The SCDT condition triples the hypothesis pool for $3\times$ the rating cost in this configuration.

### 4.2 Worked structural-overlap computation

To make the spuriousness criterion concrete, consider a hypothetical (illustrative, not measured) rendering pair where the source object has $|R_O| = 7$ relations; under $\phi_{ij}$, $|R^{+}_{ij}| = 4$ relations are preserved, $|R^{-}_{ij}| = 1$ relation conflicts, and $|R^{0}_{ij}| = 2$ relations have no image. Then:

$$s(\phi_{ij}) = \frac{4}{4 + 1 + 2} = \frac{4}{7} \approx 0.571$$

With the pre-registered threshold $\theta = 0.5$, this crosswalk is retained as candidate-structural ($0.571 > 0.5$); with $\theta = 0.6$ it would be classified spurious. This example shows the threshold is load-bearing and must be fixed before data collection; we flag this in Section 6.

### 4.3 Statistical power of the novelty comparison (projection)

**Projection with stated assumptions.** Assume (i) each hypothesis is novel with probability $p$ independent of others; (ii) the baseline novelty rate is $p_0 = 0.05$ and the SCDT rate is $p_1 = 0.15$; (iii) sample sizes $N_0 = 20$ and $N_{\text{hyp}} = 60$ from Section 4.1.

Expected novel hypotheses:

$$\mu_0 = N_0\, p_0 = 20 \times 0.05 = 1.0, \qquad \mu_1 = N_{\text{hyp}}\, p_1 = 60 \times 0.15 = 9.0$$

Standard deviations under the binomial model:

$$\sigma_0 = \sqrt{N_0\, p_0 (1 - p_0)} = \sqrt{20 \times 0.05 \times 0.95} = \sqrt{0.95} \approx 0.9747$$

$$\sigma_1 = \sqrt{N_{\text{hyp}}\, p_1 (1 - p_1)} = \sqrt{60 \times 0.15 \times 0.85} = \sqrt{7.65} \approx 2.7659$$

The standardized effect (two-sample $z$-approximation, ignoring the pooled-variance refinement for transparency):

$$z \approx \frac{\mu_1 - \mu_0}{\sqrt{\sigma_0^2 + \sigma_1^2}} = \frac{9.0 - 1.0}{\sqrt{0.95 + 7.65}} = \frac{8.0}{\sqrt{8.60}} = \frac{8.0}{2.9326} \approx 2.728$$

A two-sided standard normal test at level $\alpha = 0.05$ rejects at $|z| > 1.96$; the projected $z \approx 2.728$ exceeds this, so under the stated assumptions the design has nominal power to detect the assumed effect. **Caveat**: this is a projection conditional on the assumed rates $p_0, p_1$, which are illustrative placeholders, not measurements; if the true effect is smaller (e.g., $p_1 = 0.08$, giving $\mu_1 = 4.8$ and $z \approx (4.8 - 1.0)/2.9326 \approx 1.296$), the same design would not reach significance. The benchmark size is therefore a design variable to be increased before the experiment, not after.

### 4.4 Beam-width cost of the synthesis phase

**Inputs**: beam width $B = 3$ candidate meta-principles (design choice), each candidate requiring one synthesis pass costing (stated assumption) one LLM generation of negligible marginal cost but one expert screening of 10 minutes.

$$T_{\text{syn}} = n_t \cdot B \cdot 10\ \text{min} = 10 \times 3 \times 10 = 300\ \text{min} = 5.0\ \text{h}$$

Total expert budget across all phases for this configuration:

$$T_{\text{total}} = T_{\text{rate}}^{(3)} + T_{\text{syn}} = 15.0 + 5.0 = 20.0\ \text{h}$$

### 4.5 Sensitivity of hypothesis count to lexicon number

Holding $n_t = 10$ fixed, $N_{\text{hyp}}(n_d) = 10 \binom{n_d}{2}$ grows quadratically: $n_d = 3$ gives $10 \times 3 = 30$; $n_d = 4$ gives $60$; $n_d = 5$ gives $10 \times 10 = 100$; $n_d = 6$ gives $10 \times 15 = 150$. The expert budget therefore scales as $\binom{n_d}{2}$, which bounds the practical lexicon count and motivates the structural-overlap pre-filter of Section 3.3: applying the $\theta$-filter before expert rating, at an assumed pre-filter pass rate of $q = 0.4$ (stated assumption), the rated set shrinks to:

$$N_{\text{rated}} = q \cdot N_{\text{hyp}} = 0.4 \times 60 = 24$$

and the rating budget to $24 \times 5 \times 3 = 360\ \text{min} = 6.0\ \text{h}$, i.e., a $60\%$ reduction relative to the unfiltered $15.0\ \text{h}$, at the cost of the filter's own false-negative risk (discussed in Section 6).

## 5. Results

This paper reports no empirical measurements. The results are the derived design quantities of Section 4, restated for reference:

1. For a benchmark of $n_t = 10$ objects and $n_d = 4$ lexicons, the SCDT protocol generates $N_{\text{rend}} = 40$ renderings and $N_{\text{hyp}} = 60$ pairwise analogy hypotheses (Section 4.1).
2. The full expert-validation budget for this configuration is $T_{\text{total}} = 20.0$ h under the stated per-rating time assumptions, reducible to $11.0$ h ($6.0$ h rating + $5.0$ h synthesis screening) with the $\theta$-pre-filter at assumed pass rate $q = 0.4$ (Sections 4.1, 4.4, 4.5).
3. The structural-overlap score for the illustrative relation counts $(4, 1, 2)$ is $s = 4/7 \approx 0.571$, straddling any threshold in $(0.5, 0.6)$, demonstrating threshold sensitivity (Section 4.2).
4. **Projection**: under assumed novelty rates $p_0 = 0.05$ and $p_1 = 0.15$, the design yields a projected standardized effect $z \approx 2.728$, above the $1.96$ significance cutoff; under the weaker assumption $p_1 = 0.08$, the projected $z \approx 1.296$ falls below it (Section 4.3). Both figures are conditional projections, not findings.

The falsifiable predictions the proposed experiment must test are: (P1) the SCDT condition produces a higher expert-rated analogy validity than the baseline; (P2) the SCDT condition produces a higher novelty rate; (P3) Phase-S syntheses predict later-confirmed connections at a rate above the baseline's. No outcome of these tests is known from the materials available to this paper.

## 6. Discussion

**Limitations.** The formalism of Section 3 assumes formal objects are cleanly representable as relational structures $(E_O, R_O)$; many objects of interest (frameworks, research programs) resist such clean representation, and the admissibility requirement on renderings may be unenforceable in practice. The structural-overlap score $s(\phi_{ij})$ depends on how relations are enumerated, which is itself a judgment call; two annotators may produce different $R_O$ for the same object, changing $s$ and hence the spuriousness classification. The illustrative computation in Section 4.2 shows the classification flips within the narrow threshold band $(0.5, 0.6)$, so inter-annotator reliability of the relation enumeration must be measured before the threshold is trusted.

**Failure modes.** Three are salient. First, *lexicon-induced hallucination*: an LLM may produce fluent renderings that are not admissible in the Section 3.1 sense; the $\bot$ mechanism only works if the model can reliably detect non-renderability, which is untested. Second, *threshold gaming*: because the $\theta$-filter controls the expert budget (Section 4.5), there is pressure to set $\theta$ low to retain more hypotheses, which inflates the rated pool with spurious candidates and dilutes rater attention. Third, *synthesis overfitting*: forcing a meta-principle $M$ may produce vacuous unifications—statements so general they specialize trivially to every lexicon. A vacuity check (does $M$ rule out any observable?) must accompany Phase S; we flag this as an open design problem rather than solving it here.

**What would falsify the claims.** The conjecture fails if, in the proposed experiment, (i) expert-rated validity of SCDT analogies does not exceed baseline analogies under the same rubric, or (ii) novelty rates are statistically indistinguishable at adequate power, or (iii) registered syntheses confirm at or below baseline rate. Additionally, the formal claim that structural overlap ($s \geq \theta$) predicts later confirmation could fail even if raw novelty rises—producing many novel but spurious hypotheses—which would show the protocol generates volume, not consilience.

**Arguing against ourselves.** The strongest objection is that the protocol is elaborate packaging around what strong models already do when simply asked for interdisciplinary insight; the baseline condition of Section 3.4 is designed to test exactly this, but if baseline and SCDT outputs converge, the protocol's value reduces to auditability rather than quality—a real but modest benefit. A second objection: the projection in Section 4.3 assumed independent hypotheses; in reality hypotheses within one object are correlated (they share the same rendering), which inflates the effective variance and could deflate the projected $z$ below significance even at $p_1 = 0.15$. A cluster-aware analysis is required and may demand a larger $n_t$. Third, the thin summaries of several QNFO entries [10], [11], [12] mean we cannot verify how much of this design already exists in that corpus; our contribution claim is therefore limited to what is demonstrably new here: the truth-preservation criterion and the cost/power analysis.

**Open questions.** What is the right $\theta$, and should it be per-domain-pair? Does the beam over meta-principles (Phase S) improve over single-shot synthesis, and at what $B$ does expert screening cost outweigh quality gains? Can the pre-filter pass rate $q$ be raised by learning the filter from expert ratings, and does that introduce circularity into the validity measure?

## 7. Conclusion

We have formalized structured cross-domain translation as a four-phase protocol with an explicit truth-preservation criterion for cross-lexicon analogies, derived its combinatorial and expert-budget costs for a concrete configuration ($60$ hypotheses, $20.0$ h unfiltered, $11.0$ h with pre-filtering), and specified a controlled computational experiment with three falsifiable predictions. The analysis shows the design is feasible at modest expert cost but that its statistical power is fragile under plausible effect sizes, and that its central threshold parameter is load-bearing. The contribution is a testable blueprint: the conjecture that structured multi-lexicon translation yields genuine consilience is now stated precisely enough to be confirmed or refuted.

## References

[1] arXiv:2302.10167v2 | Cross-domain Compositing with Pretrained Diffusion Models
[2] arXiv:1702.01806v2 | Beam Search Strategies for Neural Machine Translation
[3] arXiv:1908.02895v1 | Neural Network based Deep Transfer Learning for Cross-domain Dependency Parsing
[4] arXiv:2507.20499v2 | DmC: Nearest Neighbor Guidance Diffusion Model for Offline Cross-domain Reinforcement Learning
[5] arXiv:2605.24481v3 | OmniEgo-R$^2$: A Routed Reasoning Framework for the 1st Cross-Domain EgoCross Challenge at CVPR 2026
[6] arXiv:2503.08977v1 | Decoupled Doubly Contrastive Learning for Cross Domain Facial Action Unit Detection
[7] arXiv:1804.07878v2 | Massively Parallel Cross-Lingual Learning in Low-Resource Target Language Translation
[8] arXiv:1908.09532v3 | Transductive Data-Selection Algorithms for Fine-Tuning Neural Machine Translation
[9] QNFO: The Consilience Framework: From Valuation Theory to the Void — A Cross-Domain Synthesis | DOI 10.5281/zenodo.21804073
[10] QNFO: Epistemic Dynamics | DOI 10.5281/zenodo.17230782
[11] QNFO: Syntactic Generation | DOI 10.5281/zenodo.22758173
[12] QNFO: Ultrametric Consilience Atlas: Cross-Domain Applications of p-Adic Mathematical Structure | DOI 10.5281/zenodo.21722395