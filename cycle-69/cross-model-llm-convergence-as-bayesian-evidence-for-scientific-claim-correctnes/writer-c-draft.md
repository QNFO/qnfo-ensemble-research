# Convergence of Independently Trained LLMs as Bayesian Evidence for Scientific Claim Correctness: A Formal Framework and a Calibration Protocol

## Abstract

We propose and formalize a Bayesian account of a proposed gate-checking method for novel or fringe scientific claims: when two or more large language models (LLMs), trained independently by different organizations on different architectures and data pipelines, converge not only on a conclusion but on the same multi-step argument structure while evaluating a claim, that convergence may constitute evidence of claim correctness beyond what any single model evaluation provides. We derive the likelihood structure of this argument: under a shared-training-data-bias null hypothesis, convergence is expected on retrieval-like questions but not on multi-step synthesis questions, so the diagnostic value of convergence depends on question type. We compute explicit Bayes factors for a two-model and an $N$-model cascade, showing that with a prior probability of correctness of $0.1$, a per-model truth-tracking convergence likelihood of $0.4$ against a shared-bias convergence likelihood of $0.05$, two convergent models raise the posterior to approximately $0.471$ and four convergent models to approximately $0.983$. We show that the same formalism correctly assigns evidence *against* correctness when convergence occurs on deliberately designed trap claims, and we specify a benchmark protocol — fringe claims with known ground truth, trap claims, and retrieval-versus-synthesis splits — that would measure the discriminative power of the method. We position the proposal against existing work on scientific claim verification, Bayesian evidence computation, and correctness in scientific computing, and we state the assumptions under which the framework would fail.

## 1. Introduction

Scientific claim verification is bottlenecked by domain expertise. The literature on automated scientific fact-checking repeatedly notes that verifying a scientific claim requires in-depth knowledge and substantial labor from domain experts to assemble supporting and refuting evidence from credible sources [3], and misinformation pressure from the growth of digital outlets makes the problem worse [3]. Retrieval-augmented systems such as CIBER have been built to identify corroborating and refuting documents as evidence for scientific claim verification, addressing the inherent uncertainty in LLMs by evaluating response consistency across diverse interrogation probes [4]. These systems still anchor on retrieved documents; they do not ask whether an LLM's *reasoning* is independently reproducible.

This paper develops a different signal. Suppose two LLMs, trained independently — different architectures, different data mixtures, different organizations — are each asked to evaluate a fringe physics claim, and both not only reach the same verdict but reproduce the same multi-step argument structure (the same chain of intermediate propositions in the same order). Intuitively, two independent instruments agreeing is stronger evidence than one instrument's report. We formalize this intuition as a Bayesian model comparison between two hypotheses:

- $H_c$: the claim is correct, and model convergence on an argument structure is (partly) truth-tracking.
- $H_b$: the claim's apparent support is an artifact of shared training-data bias, i.e., both models absorbed the same corpus-level error or the same popularized framing.

The key structural insight, taken directly from the research idea under development, is that the null hypothesis $H_b$ makes *different predictions depending on question type*. For retrieval-only questions (questions answerable by recalling a fact present in the shared corpus), $H_b$ predicts convergence. For multi-step synthesis questions (questions requiring the model to construct a novel chain of reasoning), $H_b$ predicts convergence only if the shared corpus contains the full argument — which is precisely what distinguishes a genuinely fringe claim from a merely obscure one. Therefore convergence on multi-step synthesis arguments discriminates between $H_c$ and $H_b$ in a way that convergence on retrieval answers does not.

Our contributions are: (i) an explicit Bayesian model with per-question-type likelihoods and a closed-form $N$-model cascade; (ii) fully worked numerical examples with all arithmetic shown; (iii) a design for trap claims that induce false consensus, showing that the framework assigns evidence in the correct direction when convergence is bias-driven rather than truth-driven; and (iv) a benchmark protocol specification. We do not report empirical measurements; all numbers in this paper are either computed from stated assumptions in Section 4 or labeled as projections in Section 5.

## 2. Background and Related Work

We discuss the supplied bibliography in its exact numbering. Because the bibliography is drawn from adjacent fields rather than from prior work on cross-model convergence specifically, we are careful to state only what each entry's own summary supports.

[1] surveys the compactness and geometric stability conjectures formulated by participants at the 2018 IAS Emerging Topics Workshop on Scalar Curvature and Convergence, focusing on sequences of compact Riemannian manifolds with nonnegative scalar curvature. Its relevance here is thematic rather than methodological: it is a body of mathematics in which "convergence of sequences" is itself the object of study, and in which stability of a limit object under perturbation is a central concern — an analogy for our question of when agreement between two noisy reasoners is stable evidence rather than coincidence. The entry's summary supplies no further detail we can rely on beyond this scope statement.

[2] describes the International Particle Physics Outreach Group (IPPOG), which has made systematic efforts to present and popularize particle physics across all audiences and age groups since 1997, and is described as a strategic pillar in fostering long-term sustainable support for fundamental research. This is directly relevant to our shared-bias null: outreach and popularization shape the corpus-level framing of physics claims, and a fringe claim that has been popularized (correctly or incorrectly) is exactly the case where two LLMs may share a biased framing. The summary supplied gives no further detail on specific programs.

[3] motivates RerrFact, reduced evidence retrieval representations for scientific claim verification, by the exponential growth in digital information outlets and the race to publish, which have made scientific misinformation more prevalent; it notes that scientific claim verification requires in-depth knowledge and great labor from domain experts to substantiate supporting and refuting evidence from credible sources. This establishes the expert bottleneck our method targets, and the summary supplied gives no further detail on the method's internals.

[4] introduces CIBER (Claim Investigation Based on Evidence Retrieval), an extension of the retrieval-augmented generation framework designed to identify corroborating and refuting documents as evidence for scientific claim verification; notably, CIBER addresses the inherent uncertainty in LLMs by evaluating response consistency across diverse interrogation probes. This is the closest published relative of our proposal: it already treats *consistency across probes of a single system* as a signal. Our proposal differs in the locus of consistency — agreement across independently trained models on argument structure rather than consistency across probes of one model — and Section 3 makes precise why independence across models changes the likelihood model.

[5] gives exact formulae for the Bayesian evidence in the case of Gaussian likelihoods with arbitrary correlations, motivated by the fact that the Bayesian evidence is a key tool in model selection whose use in cosmological model analysis has been limited by computational difficulty, with current numerical algorithms requiring supercomputers. This supports our choice of an analytic, closed-form likelihood treatment: we follow the same spirit of exact analytic Bayes factors rather than simulation-based estimation, though our likelihoods are discrete (converge/diverge on argument structure) rather than Gaussian.

[6] reports the DOE/NSF Workshop on Correctness in Scientific Computing (CSC'23), held on June 17, 2023 as part of the Federated Computing Research Conference (FCRC) 2023, conceived by DOE and NSF to address growing concerns about correctness among those who employ computational methods for large-scale scientific simulations. This grounds the institutional motivation: correctness of computationally mediated science is an recognized community concern at the level of funding agencies, and LLM-mediated claim evaluation is a natural extension of that concern. The summary supplied gives no further detail on specific workshop recommendations.

[7] introduces CCSBench, evaluating compositional controllability in LLMs for scientific document summarization, motivated by the observation that existing research typically focuses on controlling single attributes while compositional control of multiple attributes (such as length and empirical focus) is underexplored. Its relevance is as evidence that the field's evaluation infrastructure for LLMs on scientific text is maturing toward multi-attribute, compositional benchmarks — the same style of benchmark design our protocol in Section 3.4 requires (jointly controlling claim type, question type, and trap status). The summary supplied gives no further detail on CCSBench's findings.

[8] proposes YouZhi-LLM, a highly efficient financial LLM built via an adaptive GQA-to-MLA transition and training pipeline, motivated by KV cache memory overhead bottlenecking high-concurrency deployment and inflating infrastructure costs. This matters for the *economics* of our method: gate-checking by running many independent LLMs is only scalable if per-query inference is cheap, and [8] illustrates that the field is actively attacking concurrency cost. The summary supplied gives no further detail on achieved cost figures.

[9] (Impact of Cognitive Linearity on Epistemic Modeling, DOI 10.5281/zenodo.18349711) and [11] (Projective Geometric Frameworks for Semantic Structures, DOI 10.5281/zenodo.19564091) and [12] (Convergence Consilience and the Hierarchical Architecture of Reality, DOI 10.5281/zenodo.20302276) have empty summaries in the supplied bibliography; we therefore cannot state what they contain, and we cite them only as corpus context indicating that "convergence" and "consilience" as epistemic notions are under active development in adjacent informal literature. [10] (Boundary Ultrametricity: The Tree vs. $\partial_\infty\mathcal{T}$ Distinction, Applied to the ZBW Transition Graph, DOI 10.5281/zenodo.21736091) is, per its own summary, a formal note establishing that a boundary Gromov metric on $dT_p$ is ultrametric and recovers $|\cdot|_p$ while the tree vertex metric is not ultrametric, and correcting a ZBW P1 claim (C2) to a 0-hyperbolic core rather than an ultrametric core, with 147/500 violations per paper data. It is useful to us as a concrete instance of the fringe-physics ecosystem our method would gate-check, and — importantly — as an instance of a claim *corrected* by formal analysis, illustrating the ground-truth annotation step of our benchmark.

## 3. Methods

### 3.1 Hypotheses and observables

Fix a scientific claim $C$. An evaluator run is a pair $(M_i, q)$: model $M_i$ answering question $q$ about $C$. The observable is the model's *argument structure* $S_i$: the ordered sequence of intermediate propositions the model asserts en route to a verdict, extracted by a fixed parser (e.g., a chain-of-thought segmentation into atomic propositions). Two runs converge if $S_i = S_j$ under a defined equivalence (same propositions, same order, modulo paraphrase), and additionally agree on the final verdict $V_i = V_j$.

We compare two hypotheses:

$$H_c: \text{the claim is correct and model reasoning is partially truth-tracking},$$
$$H_b: \text{both models share a corpus-level bias that determines their output}.$$

### 3.2 Likelihoods by question type

Let $q$ be of type $R$ (retrieval-only: the answer, and a canonical argument for it, exist in the shared corpus) or type $S$ (multi-step synthesis: a correct answer requires constructing a non-canonical argument chain). Define:

- $p^{R}_b = P(S_1 = S_2, V_1 = V_2 \mid H_b, q \in R)$: under shared bias, both models retrieve the same corpus framing, so convergence is likely.
- $p^{S}_b = P(S_1 = S_2, V_1 = V_2 \mid H_b, q \in S)$: under shared bias on a synthesis question about a genuinely fringe claim, the shared corpus does not contain the full argument, so convergence is unlikely *unless the bias itself supplies the whole argument* (the trap case, Section 3.3).
- $p^{R}_c, p^{S}_c$: the corresponding probabilities under $H_c$, where convergence occurs when both models' reasoning tracks the truth.

The per-pair Bayes factor is

$$K_q = \frac{P(\text{convergence} \mid H_c, q)}{P(\text{convergence} \mid H_b, q)} = \frac{p^q_c}{p^q_b}.$$

The design prediction from the research idea is:

$$K_R \approx 1 \quad \text{(retrieval convergence is uninformative)}, \qquad K_S > 1 \quad \text{(synthesis convergence is informative)}.$$

### 3.3 Trap claims

A trap claim $C_T$ is a claim engineered so that a plausible-sounding but incorrect argument chain is heavily represented in common training corpora (e.g., a seductive but wrong derivation of a known-false result). Under $H_b$, both models reproduce the biased chain: convergence probability is high. Under $H_c$ with independent models, each model independently avoids the trap with probability $1 - \epsilon_T$; both converge on the *correct* structure with probability $(1-\epsilon_T)^2$, but if we condition on convergence *on the trap answer*, the likelihood under $H_c$ is $\epsilon_T^2$ (both independently err identically — possible but improbable) versus approximately $p^{T}_b$ under $H_b$. Thus convergence on a trap answer yields

$$K_T = \frac{\epsilon_T^2}{p^{T}_b} \ll 1,$$

i.e., evidence *against* the shared-bias-free correctness of the reasoning pipeline. This asymmetry is the framework's self-correcting feature: convergence is not automatically evidence for correctness; its evidential direction depends on whether the converged content is truth-tracking or bias-tracking, which the trap benchmark calibrates.

### 3.4 Benchmark protocol

The protocol has four arms, mirroring the testing plan in the research idea:

1. **Ground-truth fringe claims**: claims with known truth values, spanning retrieval-like and synthesis-like question types.
2. **Trap claims**: designed false-consensus claims as in Section 3.3.
3. **Retrieval/synthesis split**: the same claims evaluated under both question types, to test the prediction $K_R \approx 1 < K_S$.
4. **Model panel**: at least two independently trained LLMs (different architectures, data, organizations), with argument structures extracted by a fixed parser and convergence scored by a paraphrase-robust matcher.

The measured quantity is the empirical convergence rate per arm, from which empirical Bayes factors are estimated; the discriminative power is the separation of the posterior distributions of $K$ across arms. No empirical numbers are reported in this paper; Section 5 gives only projections derived from the assumed likelihood values of Section 4.

## 4. Analysis

We now fix illustrative likelihood values, state each with its rationale, and carry out all arithmetic explicitly. These values are *assumptions for the worked example*, not measurements; Section 5 labels all downstream numbers as projections.

**Input assumptions.**

- $P(H_c) = 0.1$: prior probability that a randomly drawn fringe claim is correct. Source: a deliberately conservative modeling choice for the fringe-claim regime, stated as an assumption (no empirical source is claimed).
- Retrieval arm: $p^{R}_b = 0.9$, $p^{R}_c = 0.9$. Rationale: under both hypotheses, retrieval questions with corpus-present answers produce convergent answers with high probability; this encodes the design prediction $K_R \approx 1$.
- Synthesis arm: $p^{S}_b = 0.05$, $p^{S}_c = 0.4$. Rationale: under $H_b$, the shared corpus lacks the full argument for a genuinely fringe claim, so identical multi-step chains are rare ($0.05$); under $H_c$, truth-tracking reasoning converges on the same chain often but not always ($0.4$, allowing for paraphrase-equivalence failures and genuine multiplicity of valid argument paths).
- Trap arm: $\epsilon_T = 0.1$ (per-model probability of independently falling into the trap despite correct underlying reasoning), $p^{T}_b = 0.9$ (shared bias reliably reproduces the trap chain).

**Derivation 1: Retrieval arm Bayes factor.**

$$K_R = \frac{p^{R}_c}{p^{R}_b} = \frac{0.9}{0.9} = 1.$$

A Bayes factor of $1$ leaves posterior odds equal to prior odds: retrieval convergence carries zero evidential weight. This is the formal statement of the design prediction.

**Derivation 2: Synthesis arm, two models.**

$$K_S = \frac{p^{S}_c}{p^{S}_b} = \frac{0.4}{0.05} = 8.$$

Prior odds: $\frac{P(H_c)}{P(H_b)} = \frac{0.1}{1 - 0.1} = \frac{0.1}{0.9} = \frac{1}{9} \approx 0.1111$.

Posterior odds after two-model convergence on a synthesis question:

$$O_2 = \frac{1}{9} \times 8 = \frac{8}{9} \approx 0.8889.$$

Posterior probability:

$$P_2 = \frac{O_2}{1 + O_2} = \frac{8/9}{1 + 8/9} = \frac{8}{17} \approx 0.4706.$$

So under these assumptions, two-model synthesis convergence moves a $0.1$ prior to a posterior of approximately $0.471$ — a substantial but not decisive update.

**Derivation 3: $N$-model cascade.**

For $N$ mutually independent models each with likelihood ratio $K_S$, the Bayes factor multiplies:

$$K_N = K_S^{\,N-1} = 8^{\,N-1},$$

because the first model's output is absorbed into the prior (it establishes that the argument exists) and each additional independent model contributes a factor $K_S$. Then

$$O_N = \frac{1}{9} \cdot 8^{\,N-1}, \qquad P_N = \frac{O_N}{1 + O_N}.$$

Computing each case:

- $N = 2$: $O_2 = \frac{1}{9} \times 8 = 0.8889$, $P_2 = \frac{0.8889}{1.8889} \approx 0.4706$.
- $N = 3$: $O_3 = \frac{1}{9} \times 64 = 7.1111$, $P_3 = \frac{7.1111}{8.1111} \approx 0.8767$.
- $N = 4$: $O_4 = \frac{1}{9} \times 512 = 56.8889$, $P_4 = \frac{56.8889}{57.8889} \approx 0.9827$.

In base-10 logarithms, each additional model contributes $\log_{10} 8 \approx 0.903$ orders of magnitude of Bayes factor.

**Derivation 4: models needed for a $0.95$ posterior.** We require $P_N \geq 0.95$, i.e., $O_N \geq 19$. Solve:

$$\frac{1}{9} \cdot 8^{\,N-1} \geq 19 \;\Rightarrow\; 8^{\,N-1} \geq 171 \;\Rightarrow\; (N-1)\ln 8 \geq \ln 171.$$

With $\ln 8 \approx 2.0794$ and $\ln 171 \approx 5.1422$:

$$N - 1 \geq \frac{5.1422}{2.0794} \approx 2.473 \;\Rightarrow\; N \geq 3.473 \;\Rightarrow\; N = 4.$$

Consistent with Derivation 3: $P_3 \approx 0.877 < 0.95$ and $P_4 \approx 0.983 \geq 0.95$.

**Derivation 5: trap arm.**

$$K_T = \frac{\epsilon_T^2}{p^{T}_b} = \frac{0.1^2}{0.9} = \frac{0.01}{0.9} \approx 0.0111.$$

Posterior odds after two-model convergence on a trap answer:

$$O^{T}_2 = \frac{1}{9} \times 0.0111 \approx 0.001235, \qquad P^{T}_2 = \frac{0.001235}{1.001235} \approx 0.00123.$$

Convergence on a trap answer drives the posterior from $0.1$ down to approximately $0.0012$: the framework correctly treats false consensus as strong evidence *against* the reasoning pipeline's reliability on this claim family.

**Derivation 6: sensitivity of the two-model posterior to $p^{S}_b$.** Holding $p^{S}_c = 0.4$ and prior $0.1$ fixed:

- $p^{S}_b = 0.02$: $K_S = 20$, $O_2 = \frac{20}{9} \approx 2.222$, $P_2 = \frac{2.222}{3.222} \approx 0.690$.
- $p^{S}_b = 0.10$: $K_S = 4$, $O_2 = \frac{4}{9} \approx 0.444$, $P_2 = \frac{0.444}{1.444} \approx 0.308$.
- $p^{S}_b = 0.20$: $K_S = 2$, $O_2 = \frac{2}{9} \approx 0.222$, $P_2 = \frac{0.222}{1.222} \approx 0.182$.

The posterior is highly sensitive to the null's convergence probability: if shared bias can reproduce full argument chains at rate $0.2$, the two-model update nearly halves relative to the $0.05$ case. This is the single most important quantity for the benchmark to measure.

## 5. Results

All numbers below are either computed in Section 4 from the stated assumptions or are explicitly labeled projections of those computations. **No empirical measurements, simulations, or benchmark results are reported in this paper.**

**Computed results (from Section 4 assumptions: prior $P(H_c) = 0.1$; $p^{R}_b = p^{R}_c = 0.9$; $p^{S}_b = 0.05$, $p^{S}_c = 0.4$; $\epsilon_T = 0.1$, $p^{T}_b = 0.9$):**

1. Retrieval-arm Bayes factor: $K_R = 1$ exactly; retrieval convergence is uninformative under this model.
2. Synthesis-arm two-model Bayes factor: $K_S = 8$; posterior $P_2 = 8/17 \approx 0.4706$.
3. $N$-model cascade posteriors: $P_2 \approx 0.4706$, $P_3 \approx 0.8767$, $P_4 \approx 0.9827$.
4. Minimum panel size for posterior $\geq 0.95$: $N = 4$ models.
5. Trap-arm two-model Bayes factor: $K_T = 1/90 \approx 0.0111$; posterior $P^{T}_2 \approx 0.00123$.
6. Sensitivity: two-model synthesis posterior ranges from $\approx 0.690$ ($p^{S}_b = 0.02$) down to $\approx 0.182$ ($p^{S}_b = 0.20$).

**Projections (labeled as such; derived by applying the Section 4 formulas to values the benchmark would have to measure):**

- *Projection P1*: If the benchmark measures the empirical synthesis-arm null convergence rate $\hat{p}^{S}_b$ with a two-sided 95% confidence half-width of $\pm 0.02$ at the assumed true value $0.05$, the two-model Bayes factor $K_S = 0.4/\hat{p}^{S}_b$ would lie in the interval $[0.4/0.07,\, 0.4/0.03] = [5.71,\, 13.33]$, and the two-model posterior in $[0.388,\, 0.598]$ (computed by substituting the interval endpoints into $O_2 = K_S/9$ and $P_2 = O_2/(1+O_2)$: at $K_S = 5.71$, $O_2 = 0.634$, $P_2 = 0.388$; at $K_S = 13.33$, $O_2 = 1.481$, $P_2 = 0.597$). This projection assumes the point estimate equals the assumed value and that binomial sampling error dominates.
- *Projection P2*: The qualitative ordering $K_T \ll 1 < K_S$, with $K_R \approx 1$, is the falsifiable signature of the framework; the benchmark would confirm or refute it by measuring all three arms on the same model panel.

## 6. Discussion

**Limitations and failure modes.** The framework's central weakness is the independence assumption. Two LLMs from different organizations are not independent instruments in the Bayesian sense: they share web-scale corpora, share dominant textbooks and popularizations (the ecosystem [2] describes), share distillation lineages, and may share evaluation practices that shape reasoning style. If the effective shared-bias convergence probability on synthesis questions is $p^{S}_b = 0.2$ rather than $0.05$, the two-model posterior drops from $0.471$ to $0.182$ (Derivation 6) — the method's value is fragile to exactly the quantity that is hardest to estimate a priori. Argument-structure equivalence is also a modeling choice: a paraphrase-robust matcher that is too lenient inflates measured convergence under both hypotheses (compressing $K_S$ toward 1); one that is too strict deflates it. Trap claims partially mitigate this, since traps calibrate the direction of evidence, but a benchmark's traps are themselves designed by humans who may share the blind spots of the corpus.

**What would falsify the claims.** The framework is falsified if the benchmark shows (i) synthesis-arm convergence rates under known-shared-bias conditions comparable to truth-tracking conditions ($K_S \approx 1$), or (ii) trap-arm convergence that fails to lower the posterior, i.e., models converge on trap answers at rates indistinguishable from their convergence on correct synthesis chains. It is also falsified if convergence is dominated by stylistic artifacts — e.g., all models in the panel inherit similar chain-of-thought training, making $S_1 = S_2$ common regardless of truth.

**Arguing against ourselves.** A skeptic could object that the likelihood ratio $K_S = 8$ is not just assumed but *unmeasurable* in the abstract: $p^{S}_c$ conflates "models track truth" with "models share reasoning conventions," and no ground-truth benchmark fully separates these. A stronger objection: the method is circular for the very claims it targets. For claims with known ground truth (the benchmark), we can validate the likelihoods; but for genuinely novel fringe claims — the use case — there is no ground truth, and the transfer of calibrated likelihoods from benchmark claims to novel claims assumes the fringe-claim population is homogeneous in the relevant respects. The trap mechanism helps but cannot be exhaustive. Finally, the cascade model assumes conditional independence of models given the hypothesis; correlated errors (shared tokenizer artifacts, shared reasoning templates from common instruction-tuning practices) violate this and would inflate $K_N$ multiplicatively — the failure compounds with panel size, so a large panel is not automatically safer than a small one.

**Open questions.** How should argument-structure equivalence be defined operationally (propositional graphs vs. ordered chains)? What is the empirical shared-bias convergence rate on synthesis questions for frontier models — the pivotal quantity $p^{S}_b$? Can trap generation be automated adversarially? Does probe-consistency within a single model [4] compose with cross-model convergence into a single likelihood framework, or are they partially redundant signals? And what concurrency cost constraints [8] bound the practical panel size?

## 7. Conclusion

We have formalized cross-model LLM convergence on multi-step argument structures as Bayesian evidence for scientific claim correctness, with a likelihood structure that separates retrieval-type convergence (uninformative under the shared-bias null, $K_R = 1$) from synthesis-type convergence (informative, $K_S = 8$ under stated assumptions), an $N$-model cascade reaching a $0.983$ posterior at four models from a $0.1$ prior, and a trap mechanism that reverses the direction of evidence under false consensus ($K_T \approx 0.0111$, posterior $\approx 0.0012$). The framework's value hinges entirely on one measurable quantity — the shared-bias null's synthesis convergence rate — and on the approximate independence of the model panel; both are exactly what the proposed benchmark of ground-truth fringe claims, trap claims, and retrieval/synthesis splits is designed to measure. Until that benchmark is run, every posterior number here is a projection of assumed likelihoods, not a finding.

## References

[1] arXiv:2103.10093v1 | Conjectures on Convergence and Scalar Curvature

[2] arXiv:2011.14743v1 | IPPOG : Bridging the gap between science education at school and modern scientific research

[3] arXiv:2202.02646v2 | RerrFact: Reduced Evidence Retrieval Representations for Scientific Claim Verification

[4] arXiv:2503.07937v1 | LLM-based Corroborating and Refuting Evidence Retrieval for Scientific Claim Verification

[5] arXiv:2301.13783v1 | An analytical approach to Bayesian evidence computation

[6] arXiv:2312.15640v2 | Report of the DOE/NSF Workshop on Correctness in Scientific Computing, June 2023, Orlando, FL

[7] arXiv:2410.12601v3 | CCSBench: Evaluating Compositional Controllability in LLMs for Scientific Document Summarization

[8] arXiv:2606.05868v1 | YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition

[9] QNFO: Impact of Cognitive Linearity on Epistemic Modeling | DOI 10.5281/zenodo.18349711

[10] QNFO: Boundary Ultrametricity: The Tree vs. ∂∞𝒯 Distinction, Applied to the ZBW Transition Graph | DOI 10.5281/zenodo.21736091

[11] QNFO: Projective Geometric Frameworks for Semantic Structures | DOI 10.5281/zenodo.19564091

[12] QNFO: Convergence Consilience and the Hierarchical Architecture of Reality | DOI 10.5281/zenodo.20302276