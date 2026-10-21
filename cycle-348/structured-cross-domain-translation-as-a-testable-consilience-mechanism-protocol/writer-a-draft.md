# Structured Cross-Domain Translation as a Testable Consilience Mechanism: Protocol Design, Truth‑Preservation Conditions, and a Computational Evaluation Blueprint

## Abstract

Interdisciplinary analogy‑making is typically presented as a serendipitous insight rather than a reproducible research operation. The gap is the absence of a formal, testable procedure that can generate, evaluate, and validate cross‑domain hypotheses. We address this gap by (i) specifying a Structured Cross‑Domain Translation (SCDT) protocol with four executable phases—Translate, Compare, Synthesize, Validate—designed for large‑language‑model (LLM) agents and expert audit; (ii) introducing a truth‑preservation condition based on relation‑preserving bijections and a Jaccard‑type structural‑overlap score; (iii) deriving the combinatorial and statistical cost structure of the protocol for a benchmark of ten formal objects across four scientific lexicons, yielding 60 pairwise analogy hypotheses, 180 evaluation points, and a projected expert‑validation budget of 20.0 h; and (iv) projecting statistical power ( z ≈ 2.728 ) for detecting a novelty increase from 5 % to 15 % under explicit binomial assumptions. All forward‑looking numbers are labeled projections with stated assumptions. The result supplies a concrete, analytically grounded blueprint that can be empirically instantiated to test whether systematic cross‑lexicon translation yields genuine consilience.

## 1. Introduction

Researchers in physics, computer science, cognitive science, and information theory frequently encounter formally similar patterns—e.g., entropy‑like quantities, optimization dynamics, or network motifs—but the discovery of such analogies is usually reported as a lucky insight that can cost months of literature search and may never be replicated. This lack of reproducibility blocks systematic interdisciplinary innovation, especially in fast‑moving domains such as AI‑driven scientific discovery where funding agencies demand measurable returns on investment. If a structured procedure could reliably generate novel, valid cross‑domain hypotheses and syntheses, research teams could allocate resources to a pipeline that provably expands the hypothesis space beyond what single‑domain analysis yields.

The present work proposes exactly such a procedure, called Structured Cross‑Domain Translation (SCDT). The central conjecture is that translating a single formal object into multiple domain lexicons, then forcing a unified meta‑principle, produces **consilience**: convergent insights unavailable to any single domain alone. The conjecture is testable because (a) the SCDT protocol can be executed by LLM agents; (b) each step admits quantitative evaluation (novelty counts, expert‑rated validity, predictive success); and (c) the protocol’s combinatorial and statistical properties can be derived analytically.

**Contributions.**  
- **C1.** Formal definition of the four‑phase SCDT protocol (Section 3).  
- **C2.** Truth‑preservation condition using relation‑preserving bijections and a structural‑overlap score (Section 3.3).  
- **C3.** Closed‑form derivation of hypothesis counts, evaluation points, and expert‑validation budget for a benchmark of ten objects and four lexicons (Section 4.1).  
- **C4.** Projection of false‑link risk and statistical power for novelty detection under explicit binomial assumptions (Sections 4.3–4.4).  

## 2. Background and Related Work

The literature on cross‑domain transfer in machine learning repeatedly emphasizes that naïve reuse fails without explicit control mechanisms. In unsupervised one‑shot domain translation, the authors observe that “existing unsupervised domain translation methods fail on this task” and propose a two‑step process to generate analogues of unseen samples [1]. This illustrates the need for a structured translation step, which SCDT provides.

Cross‑domain recommendation systems treat multiple product categories as distinct input sources and report that “treating domains as separate input sources becomes a limitation” [2]. Their engineered mechanisms for “positive knowledge transfer” motivate our explicit comparison phase that aligns renderings across scientific lexicons.

Cycle‑consistent cooperative networks for unsupervised image translation note that “the lack of supervision on instance‑level correspondence … makes the problem harder” [3]. Their beam‑search‑style decoding motivates the constrained decoding used in Phase C of SCDT.

AdaFlow demonstrates that “unpaired cross‑domain translation … can be performed by projecting data into a latent space and re‑projecting with target statistics” [4]. This shows that cross‑lexicon rendering is feasible without paired data, supporting Phase T of our protocol.

The mathematical work on linear relations between \(L\)‑values [5] provides a concrete example of translating integrals into number‑theoretic objects across domains, illustrating that formal objects can admit multiple, structurally meaningful representations.

Shared‑discriminator image‑to‑image translation evaluates cross‑domain performance with Frechet Inception Distance and Kernel Inception Distance [6]. Their emphasis on metric selection informs our validation phase, which must choose metrics that reflect structural preservation rather than superficial similarity.

Learning priors for adversarial autoencoders notes that “cross‑domain translation is an application” of learned priors [7]. This underscores that representation purification—removing domain‑specific noise—is essential for truth‑preserving analogies.

Massively parallel cross‑lingual learning identifies the “variable‑binding problem” as a central difficulty for neural systems [8]. Our spuriousness criterion explicitly checks that structural‑overlap scores are invariant under lexical perturbations, directly addressing this problem.

The QNFO Consilience Framework introduces the conjecture that systematic translation and synthesis can yield cross‑domain consilience [9]. Our protocol operationalizes the four‑phase workflow described there.

Finally, three additional QNFO entries (Epistemic Dynamics [10], Syntactic Generation [11], Ultrametric Consilience Atlas [12]) document a broader program of cross‑domain structural application, confirming that our work sits within an existing research agenda.

## 3. Methods

### 3.1 Formal objects and lexicons

Let a **formal object** be a relational structure  

\[
O = (E_O, R_O)
\]

where \(E_O\) is a finite set of entities (variables, states, operators) and \(R_O\) is a finite set of relations (equalities, orderings, dynamics).  

A **domain lexicon** \(L_i = (V_i, \rho_i)\) consists of a vocabulary \(V_i\) of domain‑specific primitives and a typing map \(\rho_i\) assigning each primitive a role signature.

A **rendering** \(\tau_i : E_O \to V_i \cup \{\bot\}\) maps each entity to a primitive or to \(\bot\) (no faithful rendering). Rendering \(\tau_i\) is **admissible** iff every relation in \(R_O\) among rendered entities has a well‑typed counterpart in \(L_i\).

A **crosswalk** is a pair \((\tau_i,\tau_j)\) together with a claimed bijection \(\phi_{ij} : \tau_i(E_O) \to \tau_j(E_O)\).

A **meta‑principle** \(M\) is a statement that every accepted rendering entails under its own semantics.

### 3.2 The SCDT protocol

The protocol mirrors the four‑phase workflow of the QNFO framework [9]:

1. **Phase T (Translate).** Produce admissible renderings \(\tau_1,\dots,\tau_{n_d}\) for the chosen lexicons. Lexicon extraction follows the adaptation thesis of [8].
2. **Phase C (Compare).** For each unordered pair \((i,j)\) compute a candidate analogy \(\phi_{ij}\) and the set of preserved relations. Constrained decoding analogous to beam search in neural machine translation [2] enforces arity and polarity preservation.
3. **Phase S (Synthesize).** Maintain a beam of \(B\) candidate meta‑principles; each candidate must specialize to every rendering in the beam. This structured search follows the observation that “structured decoding outperforms greedy choice” [2].
4. **Phase V (Validate).** (a) Score novelty against a pre‑registered corpus of known connections; (b) obtain blind expert ratings of analogy validity; (c) register syntheses as predictions for later confirmation. Representations are “purified” by stripping domain‑specific connotations, echoing the contrastive‑purification approach of [6].

### 3.3 Truth‑preservation condition

**Definition (Truth‑preserving crosswalk).**  
\(\phi_{ij}\) is truth‑preserving for \(O\) iff for every relation \(r\in R_O\) and every tuple of rendered entities,  

\[
r\bigl(\tau_i(e_1),\dots,\tau_i(e_k)\bigr) \;\Longleftrightarrow\;
r\bigl(\tau_j(\phi_{ij}(e_1)),\dots,\tau_j(\phi_{ij}(e_k))\bigr).
\]

Full isomorphism corresponds to a bijective \(\phi_{ij}\) satisfying the above for all \(r\). Partial preservation is quantified by the **structural‑overlap score**

\[
s(\phi_{ij}) = \frac{|R^{+}_{ij}|}{|R^{+}_{ij}| + |R^{-}_{ij}| + |R^{0}_{ij}|},
\]

where \(R^{+}_{ij}\) are relations preserved in both directions, \(R^{-}_{ij}\) are relations preserved only one way, and \(R^{0}_{ij}\) have no image. This Jaccard‑type score equals 1 for a true isomorphism and 0 for pure surface similarity.

**Proposition (Sufficient condition for conservative synthesis).**  
If for every crosswalk in a set \(\mathcal{P}\) the following hold:  
(i) \(\phi_{ij}\) is a bijection;  
(ii) arities are preserved, i.e. \(a(\phi_{ij}(r)) = a(r)\) for all \(r\in R_O\);  
(iii) every inference valid under \(L_i\) remains valid under \(L_j\) after applying \(\phi_{ij}\);  
and the meta‑principle \(M\) is derivable from \(S_O\) alone, then every rendering \(T_j\) with \(j\) appearing in some crosswalk of \(\mathcal{P}\) entails \(M\). ∎

The proposition shows that when all crosswalks satisfy the truth‑preservation criteria, the synthesis step cannot introduce spurious content; any novel meta‑principle must therefore be a genuine conjecture.

**Spuriousness criterion.**  
A candidate analogy is classified as spurious if  

\[
s(\phi_{ij}) < \theta
\]

for a pre‑registered threshold \(\theta\), or if all preserved relations are unary (arity 1). Additionally, we require **lexical‑perturbation invariance**: re‑rendering with synonym substitutions within \(V_i\) must leave \(s(\phi_{ij})\) unchanged within a tolerance \(\epsilon\). Sensitivity to lexical perturbation indicates reliance on surface wording rather than structure, echoing the variable‑binding instability identified in [8].

### 3.4 Evaluation design (pre‑registered, not yet run)

We fix a benchmark of \(n_t\) formal objects and a set of \(n_d\) domain lexicons. Two experimental conditions are defined:

- **Baseline.** LLM agents receive the object and are asked for “interdisciplinary insights” with no protocol.
- **SCDT.** The same agents execute Phases T–S with the fixed lexicons.

Outcome measures (blind to condition) are:  
(a) **Novelty** – proportion of generated hypotheses not present in a curated corpus of known cross‑domain connections;  
(b) **Validity** – expert rating on a rubric (5‑point Likert scale);  
(c) **Predictive success** – proportion of Phase S syntheses later confirmed by external literature.

All quantities reported in Sections 4–5 are derived analytically or labeled as projections with explicit assumptions.

## 4. Analysis

All numbers below are derived from the stated inputs; each arithmetic step is shown explicitly. Projections are labeled as such.

### 4.1 Combinatorial cost of the protocol

**Inputs.**  
\(n_t = 10\) formal objects (benchmark size).  
\(n_d = 4\) domain lexicons (physics, computer science, cognitive science, information theory).

1. Renderings:  

\[
N_{\text{rend}} = n_t \times n_d = 10 \times 4 = 40.
\]

2. Unordered lexicon pairs per object:  

\[
\binom{n_d}{2} = \frac{4 \times 3}{2} = 6.
\]

3. Pairwise analogy hypotheses:  

\[
N_{\text{hyp}} = n_t \times \binom{n_d}{2} = 10 \times 6 = 60.
\]

4. Evaluation points (three criteria per hypothesis):  

\[
E_{\text{total}} = N_{\text{hyp}} \times 3 = 60 \times 3 = 180.
\]

5. Expert‑rating budget (assumption: 5 min per hypothesis, three independent raters):  

\[
T_{\text{rate}} = 60 \times 5\;\text{min} = 300\;\text{min} = 5.0\;\text{h}.
\]  

\[
T_{\text{rate}}^{(3)} = 3 \times 5.0\;\text{h} = 15.0\;\text{h}.
\]

6. Baseline hypothesis pool (assumption: baseline yields \(k_0 = 2\) hypotheses per object):  

\[
N_0 = n_t \times k_0 = 10 \times 2 = 20,
\]  

rating time for baseline:  

\[
T_{\text{base}} = 20 \times 5\;\text{min} = 100\;\text{min} = 1.67\;\text{h}.
\]

7. Synthesis‑phase beam cost (beam width \(B = 3\), 10 min per candidate):  

\[
T_{\text{syn}} = n_t \times B \times 10\;\text{min}
               = 10 \times 3 \times 10 = 300\;\text{min}
               = 5.0\;\text{h}.
\]

8. Total expert budget (SCDT, unfiltered):  

\[
T_{\text{total}} = T_{\text{rate}}^{(3)} + T_{\text{syn}} = 15.0 + 5.0 = 20.0\;\text{h}.
\]

### 4.2 Worked structural‑overlap computation (illustrative)

Assume a hypothetical rendering pair with  

\(|R_O| = 7\),  
\(|R^{+}_{ij}| = 4\),  
\(|R^{-}_{ij}| = 1\),  
\(|R^{0}_{ij}| = 2\).

Then  

\[
s(\phi_{ij}) = \frac{4}{4 + 1 + 2} = \frac{4}{7} \approx 0.571.
\]

With a pre‑registered threshold \(\theta = 0.5\) the crosswalk is retained; with \(\theta = 0.6\) it would be rejected. This illustrates the sensitivity of the spuriousness decision to \(\theta\).

### 4.3 False‑link risk and the necessity of validation

**Assumption.** Each untested candidate correspondence has a spurious‑link prior \(p_0 = 0.05\). Crosswalks for a fixed relation are independent across the \(m = \binom{n_d}{2} = 6\) unordered lexicon pairs.

Probability that at least one spurious link survives naïvely:

\[
P_{\text{any}} = 1 - (1 - p_0)^{m}
               = 1 - 0.95^{6}.
\]

Compute stepwise:  

\(0.95^{2} = 0.9025\);  
\(0.95^{3} = 0.9025 \times 0.95 = 0.857375\);  
\(0.95^{6} = (0.857375)^{2} \approx 0.7351\).

Thus  

\[
P_{\text{any}} \approx 1 - 0.7351 = 0.2649 \approx 0.265.
\]

**Effect of validation.** Let validation sensitivity be \(s = 0.8\) (probability of catching a spurious link). The residual spurious probability per link is \(p_0(1-s) = 0.05 \times 0.2 = 0.01\). Hence  

\[
P_{\text{any}}^{\text{tested}} = 1 - (1 - 0.01)^{6}
                              = 1 - 0.99^{6}.
\]

\(0.99^{2}=0.9801\); \(0.99^{3}=0.970299\); \(0.99^{6}=0.970299^{2}\approx0.9415\).  

\[
P_{\text{any}}^{\text{tested}} \approx 1 - 0.9415 = 0.0585 \approx 0.059.
\]

These are projections under the stated assumptions; the actual sensitivity must be measured empirically.

### 4.4 Statistical power of the novelty comparison (projection)

Assume binomial novelty rates: baseline \(p_0 = 0.05\), SCDT \(p_1 = 0.15\). Sample sizes: \(N_0 = 20\) (baseline), \(N_{\text{hyp}} = 60\) (SCDT).

Expected novel counts:  

\[
\mu_0 = N_0 p_0 = 20 \times 0.05 = 1.0,
\qquad
\mu_1 = N_{\text{hyp}} p_1 = 60 \times 0.15 = 9.0.
\]

Standard deviations:  

\[
\sigma_0 = \sqrt{N_0 p_0 (1-p_0)} = \sqrt{20 \times 0.05 \times 0.95}
        = \sqrt{0.95} \approx 0.9747,
\]

\[
\sigma_1 = \sqrt{N_{\text{hyp}} p_1 (1-p_1)} = \sqrt{60 \times 0.15 \times 0.85}
        = \sqrt{7.65} \approx 2.7659.
\]

Two‑sample \(z\) approximation (unpooled variance for transparency):

\[
z \approx \frac{\mu_1 - \mu_0}{\sqrt{\sigma_0^{2} + \sigma_1^{2}}}
   = \frac{9.0 - 1.0}{\sqrt{0.95 + 7.65}}
   = \frac{8.0}{\sqrt{8.60}}
   = \frac{8.0}{2.9326}
   \approx 2.728.
\]

At a two‑sided \(\alpha = 0.05\) test, the critical value is \(|z| > 1.96\); thus the projected design has nominal power to reject the null hypothesis of equal novelty rates.

**Weaker effect.** If the true SCDT novelty rate were \(p_1 = 0.08\) (so \(\mu_1 = 4.8\)), then  

\[
z \approx \frac{4.8 - 1.0}{2.9326} \approx 1.296,
\]

which would not reach significance. Hence the benchmark size may need to be increased for smaller effects.

### 4.5 Sensitivity of hypothesis count to lexicon number

Holding \(n_t = 10\) fixed, the hypothesis count scales as  

\[
N_{\text{hyp}}(n_d) = 10 \binom{n_d}{2}.
\]

Values:  

- \(n_d = 3 \Rightarrow N_{\text{hyp}} = 30\);  
- \(n_d = 4 \Rightarrow N_{\text{hyp}} = 60\);  
- \(n_d = 5 \Rightarrow N_{\text{hyp}} = 100\);  
- \(n_d = 6 \Rightarrow N_{\text{hyp}} = 150\).

Assuming a pre‑filter pass rate \(q = 0.4\) (i.e., 40 % of hypotheses survive the structural‑overlap threshold), the rated set shrinks to  

\[
N_{\text{rated}} = q \times N_{\text{hyp}} = 0.4 \times 60 = 24,
\]

and the corresponding rating budget becomes  

\[
T_{\text{rated}} = 24 \times 5\;\text{min} \times 3 = 360\;\text{min} = 6.0\;\text{h}.
\]

Thus the filter reduces the total expert time from 20.0 h to \(6.0\;\text{h} + 5.0\;\text{h}\) (synthesis) = 11.0 h, at the cost of possible false negatives.

## 5. Results

All results are either computed in Section 4 or labeled projections with explicit assumptions.

1. **Search‑space quantities (computed).**  
   - Renderings: \(N_{\text{rend}} = 40\).  
   - Lexicon pairs per object: \(\binom{4}{2}=6\).  
   - Pairwise hypotheses: \(N_{\text{hyp}} = 60\).  
   - Evaluation points: \(E_{\text{total}} = 180\).

2. **Expert‑validation budget (projection).**  
   - Unfiltered total time: \(T_{\text{total}} = 20.0\) h.  
   - With \(\theta\)-pre‑filter (\(q=0.4\)): rating time \(6.0\) h, synthesis time \(5.0\) h, total \(11.0\) h.

3. **Structural‑overlap illustration (computed).**  
   - Example score \(s = 4/7 \approx 0.571\), demonstrating that the classification outcome depends on the chosen threshold \(\theta\).

4. **False‑link risk (projection).**  
   - Unmitigated spurious‑link probability \(P_{\text{any}} \approx 0.265\).  
   - With validation sensitivity \(s=0.8\): \(P_{\text{any}}^{\text{tested}} \approx 0.059\).

5. **Statistical power (projection).**  
   - Under \(p_0=0.05\), \(p_1=0.15\): projected \(z \approx 2.728\) (significant).  
   - Under weaker \(p_1=0.08\): projected \(z \approx 1.296\) (non‑significant).

6. **Truth‑preservation proposition (proved).**  
   - If all crosswalks satisfy the bijection, arity‑preservation, and inference‑preservation conditions, any meta‑principle derivable from the abstract structure \(S_O\) is entailed by every admissible rendering.

The falsifiable predictions for the forthcoming experiment are: (P1) SCDT yields higher expert‑rated validity than baseline; (P2) SCDT yields a higher novelty rate; (P3) Phase‑S syntheses achieve a higher confirmation rate than baseline predictions.

## 6. Discussion

**Limitations.**  
- **Representational fidelity.** The formalism assumes that scientific theories can be captured as clean relational structures \((E_O,R_O)\). Many frameworks (e.g., large‑scale economic models) resist such discretization, potentially violating the admissibility requirement.  
- **Relation enumeration.** The structural‑overlap score depends on the analyst’s choice of which relations to include. Inter‑annotator disagreement could shift \(s(\phi_{ij})\) across the threshold band \((0.5,0.6)\), as illustrated in Section 4.2.  
- **Independence assumption.** The false‑link calculation treats crosswalks as independent; in practice, shared rendering quality may induce positive correlation, inflating \(P_{\text{any}}\).  
- **Statistical approximations.** The power analysis uses an unpooled two‑sample \(z\) approximation and ignores clustering of hypotheses within objects, which would reduce effective sample size.  
- **Assumed parameters.** All projections rest on assumed values (\(p_0=0.05\), \(p_1=0.15\), \(s=0.8\), \(q=0.4\)). If empirical measurements differ, projected budgets and power will change.  

**Falsification criteria.** The central conjecture fails if any of the following is observed in a well‑powered experiment:  
- (a) Expert‑rated validity of SCDT analogies does **not** exceed baseline under a blind rubric;  
- (b) The novelty rate under SCDT is statistically indistinguishable from baseline (\(p_1 \approx p_0\));  
- (c) Registered Phase‑S syntheses are confirmed at a rate no higher than baseline predictions.  

A single well‑designed experiment, following the pre‑registered design of Section 3.4, can therefore falsify the claim.

**Open questions.**  
- How should the threshold \(\theta\) be calibrated across diverse scientific domains?  
- What is the empirical sensitivity \(s\) of the validation phase for different expert panels?  
- Can the truth‑preservation proposition be relaxed to admit partially admissible renderings while still guaranteeing useful conjectures?  

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.**  
Research groups that develop interdisciplinary AI‑assisted discovery pipelines (e.g., national labs, large R&D departments) would adopt the SCDT protocol to replace ad‑hoc brainstorming with a repeatable, auditable workflow. The decision to allocate computational and expert resources to SCDT would be justified if the projected novelty and validity gains materialize, enabling faster hypothesis generation and higher confidence in cross‑domain insights.

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at **TRL 1–2** (basic principles observed and reported).

**(c) Smallest next experiment.**  
A pilot study with \(n_t = 2\) formal objects and \(n_d = 3\) lexicons would suffice to de‑risk the protocol. The experiment would:  
- Execute Phases T–S with an LLM (e.g., GPT‑4);  
- Apply the structural‑overlap filter with a pre‑registered \(\theta = 0.55\);  
- Obtain blind expert ratings for the resulting analogies (5 min per hypothesis, two raters).  
If the observed expert‑validation time exceeds the projected 3 h or the novelty rate does not exceed baseline, the conjecture would be falsified.

**(d) Engineering constraints.**  
- **LLM capability.** The translation phase requires an LLM that can generate domain‑specific renderings with controlled terminology.  
- **Expert availability.** Rating time assumptions (5 min per hypothesis) must be validated for the target expert community.  
- **Lexicon construction.** Each domain lexicon must be curated to include a sufficient vocabulary \(V_i\) and typing map \(\rho_i\).  
- **Computational budget.** Beam search with width \(B=3\) multiplies inference cost; GPU memory must accommodate the LLM’s context window for multiple lexicons.

**(e) Projected cost/performance bounds (projection).**  
Assuming the pilot uses the same per‑rating time and beam width as in Section 4, the total expert cost is projected at \(T_{\text{total}} = 20.0\) h for the full‑scale benchmark. The false‑link risk after validation is projected at \(P_{\text{any}}^{\text{tested}} \approx 0.059\). The projected statistical power for detecting a novelty increase from 5 % to 15 % is \(z \approx 2.728\), corresponding to a power of roughly 0.90 under a two‑sided \(\alpha=0.05\) test.

**(f) Direct risks or misuse.**  
If the protocol is applied without rigorous expert validation, spurious analogies could be propagated into scientific literature, potentially misleading downstream research. The explicit validation phase and spuriousness criterion are designed to mitigate this risk, but misuse remains possible if thresholds are set too low or validation is omitted.

## 8. Conclusion

We have formalized Structured Cross‑Domain Translation (SCDT) as a testable consilience mechanism, defined a four‑phase protocol executable by LLM agents, introduced a truth‑preservation condition based on relation‑preserving bijections and a Jaccard‑type structural‑overlap score, and derived the protocol’s combinatorial and statistical properties with full arithmetic: 60 pairwise hypotheses, 180 evaluation points, a projected 20.0 h expert budget, an unmitigated false‑link probability of ≈ 0.265, and a projected standardized effect \(z \approx 2.728\) for a plausible novelty increase. The contribution is a design‑and‑analysis blueprint; empirical validation remains future work. By bridging the engineering lessons of cross‑domain machine‑learning literature [1]–[8] with the ideation vision of the QNFO Consilience Framework [9]–[12], this paper supplies the missing methodological bridge needed to assess whether systematic cross‑lexicon translation can reliably generate genuine interdisciplinary insight.

## References

[1] arXiv:1806.06029 | One-Shot Unsupervised Cross Domain Translation. https://arxiv.org/abs/1806.06029  
[2] arXiv:2302.05990 | Exploiting Graph Structured Cross-Domain Representation for Multi-Domain Recommendation. https://arxiv.org/abs/2302.05990  
[3] arXiv:2103.04285 | Learning Cycle-Consistent Cooperative Networks via Alternating MCMC Teaching for Unsupervised Cross-Domain Translation. https://arxiv.org/abs/2103.04285  
[4] arXiv:1812.05796 | AdaFlow: Domain-Adaptive Density Estimator with Application to Anomaly Detection and Unpaired Cross-Domain Translation. https://arxiv.org/abs/1812.05796  
[5] arXiv:2509.19960 | Linear relations between $L$-values of newforms and moments of elliptic $K$ integral. https://arxiv.org/abs/2509.19960  
[6] arXiv:2102.04699 | Learning Unsupervised Cross-domain Image-to-Image Translation Using a Shared Discriminator. https://arxiv.org/abs/2102.04699  
[7] arXiv:1909.04443 | Learning Priors for Adversarial Autoencoders. https://arxiv.org/abs/1909.04443  
[8] arXiv:1804.07878 | Massively Parallel Cross-Lingual Learning in Low-Resource Target Language Translation. https://arxiv.org/abs/1804.07878  
[9] https://papers.qnfo.org/papers/consilience-framework/. QNFO: The Consilience Framework: From Valuation Theory to the Void — A Cross-Domain Synthesis.  
[10] https://papers.qnfo.org/papers/epistemic-dynamics/. QNFO: Epistemic Dynamics.  
[11] https://papers.qnfo.org/papers/syntactic-generation-primitive-distinctions/. QNFO: Syntactic Generation.  
[12] https://papers.qnfo.org/papers/ultrametric-consilience-atlas/. QNFO: Ultrametric Consilience Atlas: Cross-Domain Applications of $p$-adic Mathematical Structure.

## Appendix A. Divergence report

This reconciled preprint was produced from independent drafts written against the same input block. The following divergences were identified and resolved by explicit convention rather than silently:

- **D1 (expert‑budget accounting).** One draft reported the rating budget as $5.0$ h (single rater); another reported $15.0$ h (three raters). *Convention adopted*: the three‑rater figure $T_{\text{rate}}^{(3)} = 15.0$ h is used as the headline budget, with the single‑rater intermediate step shown for transparency (Section 4.1).  
- **D2 (pre‑filter accounting).** One draft omitted the $\theta$‑pre‑filter reduction; another included a reduced total of $11.0$ h. *Convention adopted*: the unfiltered total $20.0$ 