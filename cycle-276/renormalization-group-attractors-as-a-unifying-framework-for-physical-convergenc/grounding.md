# Grounding block - source: rem-rev-24f6ef52-c15c-45b7-9309-26508242d5d7

## Research idea

Convergence and consilience as dual manifestations of renormalization-group attractors. Claim: independent rediscovery of the same mathematical structures by disconnected researchers (consilience) and independent emergence of identical behavior in disconnected physical systems (convergence) are two faces of one phenomenon: a non-flat 'possibility space' of consistent theories whose fixed points, under renormalization-group flow, attract both physical systems and theory-building minds. The RG is simultaneously an instance, mechanism, and model of this hierarchy. Test: formalize 'theory space' as a flow on a space of Lagrangians/equations, define a metric of theoretical similarity, and show computationally that independent discovery trajectories (e.g., historical derivation paths reconstructed as search processes) converge to the same fixed points with basins whose structure predicts which ideas get multiply discovered. Alternatively, simulate agents exploring a structured hypothesis space with coarse-graining operators and measure polygenesis rates against the attractor landscape. A derivation could show that universality of critical exponents and universality of discovered equations follow from the same fixed-point theorem, making the philosophical claim empirically falsifiable via basin geometry.

Source: owner notebook notes/v1/2026/05/20/_26140075451.md

Post-publication revision of the published paper "Renormalization‑Group Attractors as a Unifying Framework for Physical Convergence and Theory Polygenesis" (version 1.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 8 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 6 references (70 percent of 8, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Choosing N_0=(N_min+N_max)/2 'simplifies' the radius to R = 2/N_min − 2/N_max (Section 3, computed as 0.0114286 in 4.1). (confirmed by a second model)
2. 'For N∈[50,70], V_basin = 4.1×10^-4' (Results, item 1). (confirmed by a second model)

## Existing paper under revision (remediation only)

# Renormalization‑Group Attractors as a Unifying Framework for Physical Convergence and Theory Polygenesis

## Abstract
The independent emergence of identical mathematical structures in distinct scientific communities (polygenesis) and the parallel appearance of similar physical behavior in unrelated systems (convergence) both hint at a shared organizing principle. Existing literature identifies fixed‑point structures in scalar‑curvature geometry, cosmological attractors, dual‑subgradient optimization, strong‑randomness renormalization, nonequilibrium functional RG, hierarchical glass models, and quark confinement, but lacks a quantitative link between the geometry of theory space and the likelihood of independent discovery. We model theory space as a metric flow on the space of Lagrangians, define a similarity metric based on functional distance, and derive two complementary quantitative results. First, using the inflationary attractor formulas $n_s=1-2/N$ and $r=12/N^{2}$ we obtain a basin‑volume scaling $V_{\rm basin}(N)=1.0258\,N^{-2}$, which yields a polygenesis probability $P_{\rm poly}(N)=\kappa\,1.0258\,N^{-2}$ for a uniform prior on efold numbers. Second, we treat discovery trajectories as dual‑subgradient iterations on a strongly convex program, obtaining explicit iteration counts $T_{\rm simple}= \lceil 1/\epsilon\rceil$ and $T_{\rm sliding}= \lceil\ln(1/\epsilon)\rceil$, and, under a concrete contraction assumption, a projected $458.2$ iterations to reach $\epsilon=10^{-2}$ precision. An alternative Herfindahl‑based polygenesis model for an illustrative five‑basin landscape gives $P_{2}=0.275$ and $P_{3}=0.08875$. Both frameworks produce falsifiable predictions: the basin‑volume scaling predicts a $N^{-2}$ decline of polygenesis with efold number, while the Herfindahl model predicts specific coincidence probabilities for a given basin distribution. The results change practice by providing measurable criteria—basin volume and iteration‑count scaling—for assessing redundancy risk in theory development and for designing discovery processes.

## 1. Introduction
Researchers in high‑energy theory, cosmology, and the history of science repeatedly encounter cases where distinct groups arrive at the same mathematical structure without direct communication. The independent formulation of the renormalization group (RG) by Wilson and Kadanoff, the parallel invention of calculus by Newton and Leibniz, and the simultaneous emergence of inflationary attractor models in cosmology are emblematic examples. For practitioners, such polygenesis creates redundant effort, delays synthesis, and obscures the underlying unity of physical law. Experimental programs that rely on precise predictions of the scalar spectral index $n_s$ and the tensor‑to‑scalar ratio $r$ (e.g., CMB missions) must allocate resources to test models that may be mathematically equivalent under an RG fixed point. If a quantitative relationship between the geometry of theory space and the likelihood of independent rediscovery were known, funding agencies could prioritize research programs that explore genuinely novel basins, and theorists could design models whose basins are maximally large, thereby reducing the risk of redundant effort.

**Contributions.**  
- **C1.** Formal definition of a metric on theory space and derivation of basin‑volume scaling $V_{\rm basin}(N)=1.0258\,N^{-2}$ (Sections 3–4.1).  
- **C2.** Explicit computation of iteration counts for dual‑subgradient methods at tolerances $\epsilon=10^{-3}$ and $\epsilon=10^{-6}$ (Section 4.2).  
- **C3.** Derivation of a polygenesis probability proportional to basin volume, yielding $P_{\rm poly}(N)=\kappa\,1.0258\,N^{-2}$ (Section 4.3).  
- **C4.** Development of an alternative Herfindahl‑based polygenesis model for an illustrative five‑basin landscape, giving $P_{2}=0.275$ and $P_{3}=0.08875$ (Section 4.4).  
- **C5.** Projection of iteration count $458.2$ for a contraction‑parameterized discovery trajectory (Section 4.5).  
- **C6.** Presentation of falsifiability criteria based on historical polygenesis frequencies (Section 6).  
- **C7.** Practical pathway for assessing and engineering basin volumes in future theory‑building efforts (Section 7).

## 2. Background and Related Work
The literature provides multiple instances of fixed‑point structures governing both physical dynamics and theory construction.

[1] formulates Conjecture 7.1 that three‑dimensional manifolds homeomorphic to tori with ${\rm Scal}_j\ge -1/j$ and $\operatorname{MinA}(M_j^3)\ge\alpha>0$ have a subsequence converging in the $\mathcal{VF}$ sense to a flat torus, and notes the Ricci analogue was proven by Colding.

[2] studies α‑ and ξ‑attractor inflationary models and proves that the tree‑level predictions $n_s=1-2/N+O(N^{-2})$ and $r=12/N^{2}+O(N^{-3})$ are invariant under RG‑improved quantum corrections, establishing a universal fixed point for a broad class of cosmological theories.

[3] treats the convergence time of dual‑subgradient methods for strongly convex programs, and we adopt the iteration formulas $T_{\rm simple}=\lceil1/\epsilon\rceil$ and $T_{\rm sliding}=\lceil\ln(1/\epsilon)\rceil$ as our own assumptions.

[4] reviews strong‑randomness renormalization‑group approaches to disordered quantum systems.

[5] introduces the nonequilibrium functional renormalization group.

[6] investigates renormalization‑group techniques for disordered systems.

[7] reviews quark confinement in the context of renormalization‑group methods.

[8] proposes a meta‑analysis that treats convergence (ontological similarity) and consilience (epistemic similarity) as symmetric faces of a hierarchical reality shaped by RG attractors, supplying worked examples from gauge theory, effective field theory, universality, quantum geometry, and non‑equilibrium dynamics.

Collectively, these works demonstrate that (i) RG fixed points attract physical systems across diverse domains, (ii) theoretical frameworks often share invariant predictions under RG flow, and (iii) the geometry of the underlying possibility space influences both physical convergence and intellectual consilience.

## 3. Methods
We model **theory space** $\mathcal{T}$ as the set of all admissible Lagrangians $\mathcal{L}$ equipped with a metric $d(\mathcal{L}_1,\mathcal{L}_2)$ defined by the $L^{2}$ norm of the difference of their functional coefficients after a common field redefinition:
$$
d(\mathcal{L}_1,\mathcal{L}_2)=\sqrt{\sum_i (a_i-b_i)^2},
$$
where $\mathcal{L}_1=\sum_i a_i \mathcal{O}_i$ and $\mathcal{L}_2=\sum_i b_i \mathcal{O}_i$.

The **RG flow** $\Phi_t:\mathcal{T}\to\mathcal{T}$ satisfies
$$
\frac{\partial \mathcal{L}}{\partial t}= \beta[\mathcal{L}],
$$
with $\beta[\cdot]$ the beta functional derived from integrating out high‑energy modes. Fixed points $\mathcal{L}^\star$ satisfy $\beta[\mathcal{L}^\star]=0$.

A **basin of attraction** $\mathcal{B}(\mathcal{L}^\star)$ is the set of initial Lagrangians whose RG trajectories converge to $\mathcal{L}^\star$ as $t\to\infty$. Assuming isotropy near the fixed point, we approximate the basin as a $k$‑dimensional hypersphere of radius $R$:
$$
V_{\rm basin}\approx \frac{\pi^{k/2}}{\Gamma(k/2+1)}\,R^{k},
$$
where $k$ is the effective dimensionality of the relevant coupling subspace.

To connect $V_{\rm basin}$ to observable parameters we use the inflationary attractor formulas from [2]:
$$
n_s = 1-\frac{2}{N}+O(N^{-2}),\qquad
r = \frac{12}{N^{2}}+O(N^{-3}),
$$
with $N$ the number of efolds. The Euclidean distance between two models with efold numbers $N_1$ and $N_2$ in the observable space $(n_s,r)$ is
$$
d_{12}= \sqrt{\left(\frac{2}{N_2}-\frac{2}{N_1}\right)^{2}
        +\left(12\left(\frac{1}{N_1^{2}}-\frac{1}{N_2^{2}}\right)\right)^{2}}.
$$
For $N_1,N_2$ of the same order the first term dominates, yielding the approximation
$$
d_{12}\approx 2\Bigl|\frac{1}{N_2}-\frac{1}{N_1}\Bigr|.
$$

Assuming a uniform distribution of $N$ over $[N_{\min},N_{\max}]$, the maximal distance from a reference model $N_0$ occurs at the interval endpoints, giving a basin radius
$$
R = 2\max\!\Bigl(\Bigl|\frac{1}{N_{\min}}-\frac{1}{N_0}\Bigr|,
                 \Bigl|\frac{1}{N_{\max}}-\frac{1}{N_0}\Bigr|\Bigr).
$$
Choosing $N_0=(N_{\min}+N_{\max})/2$ simplifies to
$$
R = \frac{2}{N_{\min}}-\frac{2}{N_{\max}}.
$$

For the **algorithmic convergence** side we adopt the dual‑subgradient iteration count formulas from [3]:
$$
T_{\rm simple}= \left\lceil\frac{1}{\epsilon}\right\rceil,\qquad
T_{\rm sliding}= \left\lceil\ln\!\left(\frac{1}{\epsilon}\right)\right\rceil,
$$
where $\epsilon$ is a prescribed tolerance.

We also consider an **alternative polygenesis model** based on the Herfindahl concentration of basin‑volume fractions $\{p_i\}$ (Section 4.4). The probability that $k$ independent trajectories land in the same basin is
$$
P_{k}= \sum_{i=1}^{N_{b}} p_{i}^{\,k}.
$$

All calculations are analytical; no empirical data beyond the cited formulas are introduced.

## 4. Analysis
### 4.1 Basin‑volume scaling from inflationary attractors
Using $N_{\min}=50$ and $N_{\max}=70$ we compute
\[
\frac{2}{N_{\min}} = \frac{2}{50}=0.04,\qquad
\frac{2}{N_{\max}} = \frac{2}{70}\approx0.0285714,
\]
\[
R = 0.04-0.0285714 = 0.0114286.
\]
Treating the basin as a 2‑dimensional disk ($k=2$) gives
\[
V_{\rm basin}= \pi R^{2}= \pi (0.0114286)^{2}
\approx \pi \times 1.3061\times10^{-4}
\approx 4.103\times10^{-4}.
\]
Normalizing to $N=50$ yields the constant
\[
C = V_{\rm basin}(50)\times 50^{2}=4.103\times10^{-4}\times2500=1.0258,
\]
so the explicit scaling law is
\[
\boxed{V_{\rm basin}(N)=1.0258\,N^{-2}}.
\]

### 4.2 Iteration counts for dual‑subgradient convergence
For a tolerance $\epsilon=10^{-3}$:
\[
T_{\rm simple}= \lceil 10^{3}\rceil = 1000,\qquad
T_{\rm sliding}= \lceil\ln(10^{3})\rceil = \lceil 6.9078\rceil = 7.
\]
For $\epsilon=10^{-6}$:
\[
T_{\rm simple}= \lceil 10^{6}\rceil = 1\,000\,000,\qquad
T_{\rm sliding}= \lceil\ln(10^{6})\rceil = \lceil 13.8155\rceil = 14.
\]

### 4.3 Linking basin volume to polygenesis probability
Assuming polygenesis probability is proportional to basin volume,
\[
P_{\rm poly}(N)=\kappa\,V_{\rm basin}(N)=\kappa\,1.0258\,N^{-2}.
\]
Setting $\kappa=1$ for a dimensionless scale gives
\[
P_{\rm poly}(50)=1.0258\times 50^{-2}=4.103\times10^{-4},\qquad
P_{\rm poly}(60)=1.0258\times 60^{-2}=2.849\times10^{-4}.
\]
The ratio $P_{\rm poly}(60)/P_{\rm poly}(50)=0.694$, a $30\%$ reduction when the required efold number increases from $50$ to $60$.

### 4.4 Alternative Herfindahl‑based polygenesis model
Assume an illustrative landscape with five basins:
\[
p_{1}=0.40,\; p_{2}=0.25,\; p_{3}=0.20,\; p_{4}=0.10,\; p_{5}=0.05,
\]
which sum to $1$.

**Pairwise coincidence**:
\[
P_{2}= \sum_{i=1}^{5} p_{i}^{2}
=0.1600+0.0625+0.0400+0.0100+0.0025=0.2750.
\]

**Triple coincidence**:
\[
P_{3}= \sum_{i=1}^{5} p_{i}^{3}
=0.064000+0.015625+0.008000+0.001000+0.000125=0.088750.
\]

**Dominant‑basin share**:
\[
\frac{p_{1}^{2}}{P_{2}}=\frac{0.1600}{0.2750}=0.581818\approx0.582.
\]

**Odds ratio** between dominant and runner‑up basins:
\[
\frac{p_{1}^{2}}{p_{2}^{2}}=\left(\frac{0.40}{0.25}\right)^{2}=2.56.
\]

These numbers illustrate how the Herfindahl concentration of basin volumes directly determines polygenesis frequencies.

### 4.5 Convergence time of a discovery trajectory (contraction projection)
Assume a strongly convex evidence functional with strong‑convexity parameter $\mu$ and step size $\eta$ such that $\mu\eta=0.01$ (so $q=1-\mu\eta=0.99$). With initial distance $d_{0}=1$ and target precision $\epsilon=10^{-2}$, the iteration count $n$ satisfies $d_{0}q^{n}\le\epsilon$:
\[
n=\frac{\ln(\epsilon/d_{0})}{\ln q}
=\frac{\ln(10^{-2})}{\ln(0.99)}
=\frac{-4.605170}{-0.01005034}=458.21\approx458.2.
\]
Thus, under the stated contraction parameters, a discovery trajectory reaches $1\%$ precision after roughly $458$ iterations.

## 5. Results
1. **Basin‑volume formula.** $V_{\rm basin}(N)=1.0258\,N^{-2}$ (Section 4.1). For $N\in[50,70]$, $V_{\rm basin}=4.1\times10^{-4}$.
2. **Iteration counts.** Simple method: $1000$ ($\epsilon=10^{-3}$) and $1\,000\,000$ ($\epsilon=10^{-6}$). Sliding method: $7$ and $14$ respectively (Section 4.2).
3. **Polygenesis probability (basin‑volume model).** $P_{\rm poly}(50)=4.1\times10^{-4}$, $P_{\rm poly}(60)=2.8\times10^{-4}$ (Section 4.3).
4. **Herfindahl polygenesis model.** $P_{2}=0.275$, $P_{3}=0.08875$, odds ratio $2.56$ (Section 4.4).
5. **Contraction‑based iteration projection.** $458.2$ iterations to reach $\epsilon=10^{-2}$ (Section 4.5).

These quantitative outcomes connect the geometry of theory space (via $N$ or basin fractions) to both computational effort (via $\epsilon$) and the likelihood of convergent discovery.

## 6. Discussion
### 6.1 Limitations
- **L1. Metric choice.** The $L^{2}$ metric on coupling coefficients assumes linearity and neglects possible curvature of theory space; alternative metrics could modify the $N^{-2}$ scaling.
- **L2. Dimensionality $k$.** We set $k=2$ because $n_s$ and $r$ span the observable subspace; inclusion of additional observables (e.g., non‑Gaussianity) would increase $k$ and steepen the basin‑volume decay.
- **L3. Uniform $N$ distribution.** The derivation assumes a uniform prior over $N$; realistic model‑building practices may favor certain $N$ ranges, altering $R$.
- **L4. Neglect of higher‑order terms.** The $O(N^{-2})$ and $O(N^{-3})$ corrections in [2] are omitted; for small $N$ these corrections could be non‑negligible.
- **L5. Algorithmic constants.** The iteration formulas from [3] are asymptotic bounds; actual implementations may have prefactors that change absolute iteration counts.
- **L6. Herfindahl assumptions.** The illustrative five‑basin distribution is an assumption (A1); real theory landscapes may have different basin fractions, affecting $P_{k}$ values.

### 6.2 Failure modes and falsifiability
The central claim—that polygenesis probability scales as $N^{-2}$ (basin‑volume model) or as the Herfindahl concentration (alternative model)—would be falsified if a systematic historical analysis revealed a flat or increasing rate of independent rediscovery for models with larger $N$, or if observed coincidence frequencies for a well‑characterized basin distribution deviated from the predicted $P_{k}$ values.

> **Falsification criterion (basin‑volume model).** Compile a database of historically independent derivations of inflationary attractor models, record the efold numbers $N$, and compute the empirical frequency $f(N)$. If $f(N)$ does not decrease at least as fast as $N^{-2}$ across $N\in[40,80]$, the basin‑volume scaling hypothesis fails.

> **Falsification criterion (Herfindahl model).** For a field where basin fractions $\{p_i\}$ can be estimated (e.g., via RG flow sampling), compute $P_{2}$ and $P_{3}$ and compare to observed pairwise and triple coincidence rates. Significant deviation beyond statistical uncertainty falsifies the Herfindahl prediction.

### 6.3 Open questions
- How does inclusion of reheating parameters modify the basin geometry and the $N^{-2}$ scaling?
- Can the metric be refined to incorporate functional RG flow information from nonequilibrium systems [5]?
- What is the impact of disorder‑induced fixed points [6] on the universality of basin volumes across statistical physics and cosmology?
- How robust are the contraction parameters assumed in Section 4.5 for real research processes?

## 7. Practical Implications and Engineering Pathways
**(a) Users and decisions.** Theory developers, funding agencies, and interdisciplinary research consortia would use the basin‑volume formula $V_{\rm basin}(N)=1.0258\,N^{-2}$ to assess the risk of redundant effort when proposing new inflationary or more general RG‑based models. A model with a larger predicted basin volume (smaller $N$) would be flagged as having higher polygenesis risk, prompting either a shift toward novel parameter regimes or an explicit coordination effort.

**(b) Readiness level.** The present work is a purely analytical derivation that has not undergone peer review; according to NASA TRL definitions, it resides at TRL 1–2.

**(c) Smallest next experiment.** A “polygenesis audit” constitutes the minimal prototype. The audit would collect timestamps of independent publications that derive the same attractor structure, extract the associated $N$ values (for the basin‑volume model) or basin‑fraction estimates (for the Herfindahl model), and compute empirical frequencies. Observation of a frequency scaling inconsistent with $N^{-2}$ (or with the predicted $P_{k}$) would falsify the corresponding model.

**(d) Engineering constraints.** The primary constraint is the availability of reliable historical metadata (publication dates, citation networks, and model parameters). No material, computational, or manufacturing constraints arise because the result is analytical.

**(e) Projected cost bounds.** Assuming a modest literature‑mining effort requiring $10^{4}$ USD in researcher time and database access fees, the projected cost of the polygenesis audit is $O(10^{4}\,\text{USD})$, with uncertainty dominated by the completeness of the bibliographic corpus.

**(f) Risks and misuse.** Misapplication could occur if agencies use the basin‑volume metric to suppress high‑$N$ research without considering scientific merit, potentially stifling exploration of genuinely novel regimes. Careful contextualization of the metric is therefore essential.

## 8. Conclusion
We have formalized theory space as a metric flow under the renormalization group, derived an explicit basin‑volume scaling $V_{\rm basin}(N)=1.0258\,N^{-2}$ from inflationary attractor formulas, and linked this geometric quantity to the probability of independent rediscovery of a theory. By coupling the basin‑volume analysis with concrete iteration‑count formulas for dual‑subgradient convergence, we provide a unified quantitative framework that treats physical convergence and intellectual consilience as two faces of the same RG attractor landscape. The framework yields falsifiable predictions about the decline of polygenesis with increasing efold number and about coincidence probabilities for a given basin distribution, offering a practical tool for theory developers and funding bodies to manage redundancy in scientific research. Future work should refine the metric on theory space, incorporate additional observables, and perform the proposed historical audit to test the scaling laws empirically.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.1-proportionate-notice). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Conjectures on Convergence and Scalar Curvature. arXiv:2103.10093v1. https://arxiv.org/abs/2103.10093v1
[2] Renormalization Group independence of Cosmological Attractors. arXiv:1611.04997v2. https://arxiv.org/abs/1611.04997v2
[3] On the Convergence Time of Dual Subgradient Methods for Strongly Convex Programs. arXiv:1503.06235v4. https://arxiv.org/abs/1503.06235v4
[4] Strong-randomness renormalization groups. arXiv:2304.08572v1. https://arxiv.org/abs/2304.08572v1
[5] Introduction to the nonequilibrium functional renormalization group. arXiv:1204.1489v1. https://arxiv.org/abs/1204.1489v1
[6] The Renormalization Group for Disordered Systems. arXiv:1307.6891v1. https://arxiv.org/abs/1307.6891v1
[7] Quark Confinement and the Renormalization Group. arXiv:1010.1942v1. https://arxiv.org/abs/1010.1942v1
[8] https://papers.qnfo.org/papers/static-architecture-of-reality-and-its-biological-interface. QNFO: Convergence Consilience and the Hierarchical Architecture of Reality.

## Appendix A. Divergence report
*The three independent drafts converged on the definition of theory space, the metric, and the use of RG flow. Divergent claims arise in the quantitative modeling of polygenesis and iteration counts.*

| Divergent Claim | Draft A (baseline) | Draft B (alternative) | Chosen Convention for Main Text | Reason for Choice |
|-----------------|-------------------|-----------------------|--------------------------------|-------------------|
| Polygenesis probability model | $P_{\rm poly}(N)=\kappa\,1.0258\,N^{-2}$ (Section 4.3) | $P_{k}= \sum_i p_i^{\,k}$ with illustrative $p_i$ (Section 4.4) | Basin‑volume model (baseline) | Directly ties polygenesis to the inflationary efold number, uses only inputs from [2] and the derived basin‑volume scaling; provides a clear $N^{-2}$ prediction. |
| Numerical polygenesis values | $P_{\rm poly}(50)=4.1\times10^{-4}$, $P_{\rm poly}(60)=2.8\times10^{-4}$ | $P_{2}=0.275$, $P_{3}=0.08875$ (illustrative) | Basin‑volume values | Derived from the analytic $V_{\rm basin}(N)$ without additional assumptions about basin fractions. |
| Iteration‑count formula | $T_{\rm simple}= \lceil1/\epsilon\rceil$, $T_{\rm sliding}= \lceil\ln(1/\epsilon)\rceil$ (Section 4.2) | Contraction‑based projection $n=458.2$ for $\epsilon=10^{-2}$ (Section 4.5) | Both presented | The $O(1/\epsilon)$ formulas are exact theorems from [3]; the contraction projection is an explicit numerical illustration under additional assumptions (A2). Both are retained as complementary. |
| Basin‑volume dimensionality $k$ | $k=2$ (observable subspace) | Not specified (implicit in Herfindahl model) | $k=2$ | Directly follows from the two observables $n_s$ and $r$ used in the derivation. |
| Falsifiability criterion | Frequency vs $N^{-2}$ decline (Section 6) | Odds ratio $2.56$ vs observed basin hierarchy (Section 4.4) | Both criteria reported | Each follows from its respective model; both are valid falsification tests. |

## Appendix B. Claim attribution
| Claim ID | Description | Source Draft(s) | Agreement |
|----------|-------------|-----------------|-----------|
| C1 | Definition of metric on theory space and basin‑volume approximation | A, B, C | Convergent |
| C2 | Derivation of $V_{\rm basin}(N)=1.0258\,N^{-2}$ | A, B, C | Convergent |
| C3 | Computation of basin volume for $N\in[50,70]$ yielding $4.1\times10^{-4}$ | A, B, C | Convergent |
| C4 | Iteration counts $T_{\rm simple}$ and $T_{\rm sliding}$ from [3] | A, B, C | Convergent |
| C5 | Projection of $458.2$ iterations under contraction assumption | A, B, C | Convergent |
| C6 | Polygenesis probability scaling $P_{\rm poly}(N)=\kappa\,1.0258\,N^{-2}$ | A, B, C | Convergent |
| C7 | Herfindahl‑based polygenesis probabilities $P_{2}=0.275$, $P_{3}=0.08875$ | B, C | Convergent |
| C8 | Odds ratio $(p_{1}/p_{2})^{2}=2.56$ for illustrative landscape | B, C | Convergent |
| C9 | Limitations list (L1–L6) | A, B, C | Convergent |
| C10 | Falsifiability criteria for both models | A, B, C | Convergent |
| C11 | Practical implications (users, TRL, next experiment, constraints, cost, risks) | A, B, C | Convergent |
| C12 | Background citations of works [1]–[8] with specific points | A, B, C | Convergent |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2103.10093v1 | Conjectures on Convergence and Scalar Curvature
arXiv:1611.04997v2 | Renormalization Group independence of Cosmological Attractors
arXiv:1503.06235v4 | On the Convergence Time of Dual Subgradient Methods for Strongly Convex Programs
arXiv:2304.08572v1 | Strong-randomness renormalization groups
arXiv:1204.1489v1 | Introduction to the nonequilibrium functional renormalization group
arXiv:1307.6891v1 | The Renormalization Group for Disordered Systems
arXiv:1010.1942v1 | Quark Confinement and the Renormalization Group

## QNFO corpus context (Vectorize)

QNFO: Convergence Consilience and the Hierarchical Architecture of Reality | https://papers.qnfo.org/papers/static-architecture-of-reality-and-its-biological-interface

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2103.10093v1 | Conjectures on Convergence and Scalar Curvature
  Here we survey the compactness and geometric stability conjectures formulated by the participants at the 2018 IAS Emerging Topics Workshop on {\em Scalar Curvature and Convergence}. We have tried to survey all the progress towards these conjectures as well as related examples, although it is impossible to cover everything. We focus primarily on sequences of compact Riemannian manifolds with nonneg
  Full text (https://arxiv.org/html/2103.10093v1), excerpts of its own sections:
  § 1. Introduction: One of the greatest challenges in Geometric Analysis today is to develop a deeper understanding of the geometry of manifolds with lower bounds on their scalar curvature and their limit spaces. Even in three dimensions, manifolds with positive scalar curvature can have arbitrarily thin and deep wells and arbitrarily long or short tunnels (see Figure  1 ). The existence of a single increasingly thin well prevents the existence of a smooth or Lipschitz limit. If there are increasingly many wells, the sequence has no Gromov-Hausdorff (GH) limit either. For this reason we must consider weaker notions of convergence and at the same time work to develop a notion of convergence which is strong enough to preserve the key properties of scalar curvature. In Section  2 we review the key geometric properties of scalar curvature including new low regularity notions of nonnegative scalar curvature. Figure 1. A sequence of $M_{j}^{3}$ with positive scalar curvature that converges to a round sphere, ${\mathbb{S}}^{3}$ , in the $\mathcal{VF}$ sense but have no GH limit. [...]
  § 2. The Geometry of Scalar Curvature: Before we state our conjectures or define any notions of convergence, we review some of the key geometric properties of three dimensional Riemannian manifolds with scalar curvature bounds. [...]
  § 7. Geometric Stability of the Scalar Torus Rigidity Theorem: Let us begin with the geometric stability of the scalar torus rigidity theorem where our manifolds are still homeomorphic to three dimensional tori but we only have almost nonnegative scalar curvature : ${\rm Scal}_{j}\geq-1/j$ . See Figure  15 . Conjecture 7.1 . Geometric Stability of Scalar Torus Rigidity [Gromov-Sormani] Suppose $M_{j}^{3}$ are three dimensional Riemannian manifolds homeomorphic to tori with (109) ${\rm Scal}_{j}\geq-1/j\textrm{ and }\operatorname{MinA}(M_{j}^{3})\geq\alpha>0$ satisfying (110) $\operatorname{Diam}(M_{j})\leq D\textrm{ and }\operatorname{Vol}(M_{j})\leq V$ then a subsequence $M_{j_{k}}^{3}\xrightarrow{\mathcal{\,VF\,\,}}M_{\infty}$ where $M_{\infty}$ is isometric to a flat torus. Figure 15. A sequence of Riemannian manifolds satisfying the hypotheses of Conjecture  7.1 which has no GH limit. If we replace the scalar curvature condition with Ricci curvature, this conjecture was proven by Colding (see Lemma 3.11 in [ 45 ] ). He did not need the $\operatorname{MinA}$ condition, just a uniform lower bound on volume to prevent collapsing. [...]
  § 10.1. Using Compactness Theorems: Note that Wenger’s Compactness Theorem and the hypotheses of Conjecture  10.1 guarantee a subsequence of the $\Omega_{j}$ $\mathcal{F}$ converge to some $\Omega_{\infty}$ which might be the $0$ space. We would ”only” need to show that $\Omega_{\infty}$ is always a Euclidean ball and thus the original sequence converges as required in the conjecture. If we assume the $M_{j}$ are uniformly asymptotically flat in a strong enough way for $R\geq R_{0}$ that their asymptotically flat ends converge to an asymptotically flat end $E_{\infty}$ and we require that $\partial\Omega_{j}$ lie in this asymptotically flat regions, we might hope to prove $\partial\Omega_{j}$ cannot converge to $0$ space. This approach was suggested in Sormani’s survey article [ 135 ] and attempted in the graph setting by Huang-Lee-Sormani in [ 73 ] . We must ensure that extrinsic distances between points in $\partial\Omega_{j}$ do not all converge to $0$ which requires knowledge of geodesics which pass through $\Omega_{j}$ . [...]
[2] arXiv:1611.04997v2 | Renormalization Group independence of Cosmological Attractors
  The large class of inflationary models known as $α$- and $ξ$-attractors gives identical cosmological predictions at tree level (at leading order in inverse power of the number of efolds). Working with the renormalization group improved action, we show that these predictions are robust under quantum corrections. This means that for all the models considered the inflationary parameters $(n_s,r)$ are
  Full text (https://arxiv.org/html/1611.04997v2), excerpts of its own sections:
  § I Introduction: Successful inflationary models should satisfy some basic requirements. They have to be consistent within the theory in which they are formulated (QFT and GR). Moreover, for the models to be predictive, the predictions should depend on a number of parameters smaller than the number of predictions themselves. A large class of inflationary models, the so-called Cosmological Attractors, gives the same classical predictions for the inflationary observables 1 1 1 More precisely, for $\alpha\rightarrow 1$ and $\xi\rightarrow\infty$ in the $\alpha$ - and $\xi$ -attractors respectively. [ 1 ] . At leading order in the $1/N$ expansion, with $N$ the number of efolds, the tree-level spectral index and tensor-to-scalar ratio are given by $n_{s}=1-2/N+O(N^{-2})$ and $r=12/N^{2}+O(N^{-3})$ . A natural question to ask then is if these predictions are robust in the full quantum theory. Are the attractor models consistent and predictive at the quantum level? In this letter we will consider the effect of perturbative corrections due to the renormalization group (RG) flow. [...]
  § I.1 RG improving and renormalization scale: Let us briefly review some standard features of the effective action and the RG flow that we will use in the following. The quantum potential for a scalar field $\phi$ depends in general on powers of logarithms of the form $\ln\left({M_{i}^{2}(\phi)}/{\mu^{2}}\right)$ where $M_{i}^{2}(\phi)$ are the field-dependent masses of the particles running in the loops and $\mu$ the renormalization scale. The logarithms appear only up to $L$ -th power at the $L$ loop order. A well known result in quantum field theory [ 8 , 9 ] tells us that in each region of the field space it is possible to define an effective field theory (EFT) where only one logarithm remains relevant in the full effective potential. All the other mass scales decouple and their net effect will be a shift in the definition of the parameters of the EFT. Thus, schematically, each loop contribution will have the following form $V^{(L)}=\hbar^{-1}(v_{0}^{(L)}s^{L}+\hbar v_{1}^{(L)}s^{L-1}..+\hbar^{L}v_{L}^{(L)}),$ (3) where $s=\hbar\ln\left(\frac{M^{2}(\phi)}{\mu^{2}}\right)$ (4) is the only relevant log in the EFT. [...]
  § I.2 Key idea: The key point is that since only one log remains relevant during inflation there is (up to some irrelevant numerical factors) a unique choice for the function $\tilde{t}$ , i.e. the one implicitly defined by eq. ( 9 ). [...]
  § IV Conclusions: In this letter we analyzed the Cosmological Attractor models using the RG improved action to include the leading log quantum corrections. A consequence of this is that the slow roll parameters and the number of efolds will depend on the beta-functions, and differ from the respective tree-level expressions. However, when calculating the spectral index and tensor-to-scalar ratio, all corrections exactly cancel. This can be shown, expanding in the small parameter defying the inflationary regime, without explicitly solving the RGEs. This is our main result, the inflationary predictions for $\alpha$ and $\xi$ attractors are not affected by quantum corrections (to leading order in the $1/N$ expansion). This generalize our previous work on Higgs inflation [ 2 ] to the larger class of Cosmological Attractors. At the same time it extends beyond the tree level the unified picture provided in [ 1 ] . There is one caveat which allows quantum corrections to become important. [...]
[3] arXiv:1503.06235v4 | On the Convergence Time of Dual Subgradient Methods for Strongly Convex Programs
  This paper studies the convergence time of dual gradient methods for general (possibly non-differentiable) strongly convex programs. For general convex programs, the convergence time of dual subgradient/gradient methods with simple running averages (running averages started from iteration $0$) is known to be $O(\frac{1}{ε^{2}})$. This paper shows that the convergence time for general strongly conv
  Full text (https://arxiv.org/html/1503.06235v4), excerpts of its own sections:
  § I Introduction: Consider the following strongly convex program: $\displaystyle\min\quad$ $\displaystyle f(\mathbf{x})$ (1) s.t. $\displaystyle g_{k}(\mathbf{x})\leq 0,\forall k\in\{1,2,\ldots,m\}$ (2) $\displaystyle\mathbf{x}\in\mathcal{X}$ (3) where set $\mathcal{X}\subseteq{R}^{n}$ is closed and convex; function $f(\mathbf{x})$ is continuous and strongly convex on $\mathcal{X}$ (strong convexity is defined in Section II-A ); functions $g_{k}(\mathbf{x}),\forall k\in\{1,2,\ldots,m\}$ are Lipschitz continuous and convex on $\mathcal{X}$ . Note that the functions $f(\mathbf{x}),g_{1}(\mathbf{x}),\ldots,g_{m}(\mathbf{x})$ are not necessarily differentiable. It is assumed throughout that problem ( 1 )-( 3 ) has an optimal solution. Strong convexity of $f$ implies the optimum is unique. Convex program ( 1 )-( 3 ) arises often in control applications such as model predictive control (MPC) [ 2 ] , decentralized multi-agent control [ 3 ] , and network flow control [ 4 , 5 ] . [...]
  § I-A The $\epsilon$ -Approximate Solution: Definition 1 . Let $\mathbf{x}^{\ast}$ be the optimal solution to problem ( 1 )-( 3 ). For any $\epsilon>0$ , a point $\mathbf{x}^{\epsilon}\in\mathcal{X}$ is said to be an $\epsilon$ -approximate solution if $f(\mathbf{x}^{\epsilon})\leq f(\mathbf{x}^{\ast})+\epsilon$ and [...]
  § VII Conclusions: This paper studies the convergence time of the dual subgradient method strongly convex programs. This paper shows that the convergence time of the dual subgradient method with simple running averages for general strongly convex programs is $O(\frac{1}{\epsilon})$ . This paper also considers a variation of the primal averages, called the sliding running averages, and shows that if the dual function is locally quadratic then the convergence time is $O(\log(\frac{1}{\epsilon}))$ .
  § Appendix E Proof of Theorem 10: Lemma 16 . Let $q(\boldsymbol{\lambda}):\mathbb{R}^{m}_{+}\rightarrow\mathbb{R}$ be a concave function and $q(\boldsymbol{\lambda})$ be maximized at $\boldsymbol{\lambda}=\boldsymbol{\lambda}^{\ast}\geq\mathbf{0}$ . Denote $\mathbf{d}=\nabla_{\boldsymbol{\lambda}}q(\boldsymbol{\lambda}^{\ast})$ and $\mathbf{U}\boldsymbol{\Sigma}\mathbf{U}^{T}=\nabla_{\boldsymbol{\lambda}}^{2}q(\boldsymbol{\lambda}^{\ast})$ . Suppose that the following conditions are satisfied: 1. Suppose $\mathbf{d}\leq\mathbf{0}$ and $\lambda_{k}^{\ast}d_{k}=0,\forall k\in\{1,\ldots,m\}$ . Denote $\mathcal{K}=\{k\in\{1,\ldots,m\}:d_{k}=0\}$ and $l=|\mathcal{K}|$ . 2. Suppose $\boldsymbol{\Sigma}\prec 0$ and $\text{rank}(\mathbf{U}^{\prime})=l$ where $\mathbf{U}^{\prime}$ is an $l\times n$ submatrix of $\mathbf{U}$ composed by rows with indices in $\mathcal{K}$ . [...]
  § Appendix F Proof of Theorem 11: • Proof of Part (1): Let $\mathbf{x}^{\ast}$ be the optimal solution to problem ( 21 )-( 23 ). Since each column of $\mathbf{A}$ has at least one non-zero entry, we have $x_{i}^{\ast}\leq b^{\max},\forall i\in\{1,2,\ldots,n\}$ with $b^{\max}=\max_{1\leq i\leq n}b_{i}$ . Thus, problem ( 24 )-( 26 ) is equivalent to problem ( 21 )-( 23 ) since only a redundant constraint $\mathbf{x}\leq\mathbf{x}^{\max}$ is introduced. • Proof of Part (2): – To show Assumption 1 holds: It follows from the strong convexity of $\sum_{i=1}^{n}-w_{i}\log(x_{i})$ over set $\mathcal{X}=\{\mathbf{0}\leq\mathbf{x}\leq\mathbf{x}^{\max}\}$ . – To show Assumption 2 holds: It follows from the assumption that $\mathbf{A}\mathbf{x}^{\ast}\leq\mathbf{b}$ , which is Slater’s condition for convex programs only with linear inequality constraints. [...]
[4] arXiv:2304.08572v1 | Strong-randomness renormalization groups
  This is a very brief review article, written for a book (in preparation) in memory of Michael E. Fisher and to celebrate 50+ years since the Wilson-Fisher renormalization group. Strong-randomness renormalization groups were first developed to treat various quantum critical ground states, especially in one-dimensional systems. After briefly reviewing some of the earlier work with these methods, the
  Full text (https://arxiv.org/html/2304.08572v1), excerpts of its own sections:
  § I Introduction: Renormalization group approaches to systems in critical states have been developed for a wide variety of different types of systems. As a consequence of this variety, there are many very different types of renormalization group (RG) calculations. What do they all have in common? Almost all RGs coarse-grain a system of many degrees of freedom by some type of “integrating out” of the highest-energy or in some sense “stiffest” degrees of freedom. Good analytical control of the RG usually requires some level of simplicity of the couplings between the degrees of freedom that are integrated out and the remaining degrees of freedom. For many translationally-invariant systems the RG is implemented in momentum space, as in the seminal Wilson-Fisher paper  [ 1 , 2 ] . In many cases, the highest-energy (or stiffest) degrees of freedom are the remaining modes with the highest momenta, and these are integrated out, thus decreasing the ultraviolet momentum cutoff. [...]
  § II random-singlet ground state: The first strong-randomness RG was developed by Ma, Dasgupta and Hu (1979) for the low temperature properties of random quantum antiferromagnets  [ 10 , 11 , 12 , 13 ] . The system they considered is an antiferromagnetic Heisenberg spin-1/2 chain, with quenched random nearest-neighbor spin interactions. The Hamiltonian is: $H=\sum_{n}J_{n}\bm{\mathbf{\sigma}}_{n}\cdot\bm{\mathbf{\sigma}}_{n+1}~,$ (1) where the couplings $J_{n}>0$ are drawn from a probability distribution $P(\log J)$ that is broad, and $\bm{\mathbf{\sigma}}_{n}$ is the vector of Pauli operators for the spin-1/2 at site $n$ . The ground state of this spin chain is a so-called random-singlet state  [ 10 , 11 , 12 , 13 ] . This random-singlet ground state consists, to first approximation, of pairs of spins that are in their total spin zero singlet state, with the two spins in each such pair being at various distances along the chain determined by local details of that sample’s Hamiltonian. [...]
  § III other infinite-randomness fixed points: There are (infinitely) many other one-dimensional models, both quantum and classical, whose asymptotic ground state and/or low-frequency properties can be systematically and correctly obtained with a strong-randomness RG approach [ 7 , 8 , 9 ] . One notable example is the quantum critical point of the transverse-field Ising spin chain, whose infinite-randomness fixed point is very closely related to that of the random-singlet state [ 14 , 15 ] . An infinite series of discretely different infinite-randomness fixed points was also found. These govern the quantum critical ground states of certain spin chains with larger spin $S$ , as well as chains of interacting non-Abelian anyons [ 7 , 8 , 16 , 17 ] . For many of these one-dimensional models, the strong-randomness RG can be solved analytically. [...]
  § V conclusion: The strong-randomness renormalization group methods are versions of the renormalization group (RG) that are useful for treating certain systems with quenched randomness, particularly those whose low-energy behavior is governed by an infinite-randomness fixed point. These methods have wide applicability in certain one-dimensional quantum systems, as well as in various other systems, as reviewed in Refs.  [ 7 , 8 , 9 ] . More recently, such strong-randomness RG methods have been generalized to study the dynamic phase transition between many-body localization (MBL) and thermalization, as I have briefly reviewed here.
[5] arXiv:1204.1489v1 | Introduction to the nonequilibrium functional renormalization group
  In these lectures we introduce the functional renormalization group out of equilibrium. While in thermal equilibrium typically a Euclidean formulation is adequate, nonequilibrium properties require real-time descriptions. For quantum systems specified by a given density matrix at initial time, a generating functional for real-time correlation functions can be written down using the Schwinger-Keldy
  Full text (https://arxiv.org/html/1204.1489v1), excerpts of its own sections:
  § 1 Introduction: Thermal equilibrium properties of many-body or field theories are known to be efficiently classified in terms of renormalization group fixed points. A particularly powerful concept is the notion of infrared fixed points which are characterized by universality. These correspond to critical phenomena in thermal equilibrium, where the presence of a characteristic large correlation length leads to independence of long-distance properties from details of the underlying microscopic theory. In contrast, a classification of properties of theories far from thermal equilibrium in terms of renormalization group fixed points is much less developed. The notion of universality or criticality far from equilibrium is to a large extent unexplored, in particular, in relativistic quantum field theories. Here, the strong interest is mainly driven by theoretical and experimental advances in our understanding of early-universe cosmology as well as relativistic collision experiments of heavy nuclei in the laboratory. [...]
  § 2.1 Statistical and spectral functions: All information about a quantum theory is encoded in its correlation functions for a given density matrix $\varrho$ . In thermal equilibrium, for the case of a canonical ensemble with inverse temperature $\beta\equiv 1/T$ and Hamilton operator $H$ , the density matrix is given by $\varrho^{\rm(eq)}\sim e^{-\beta H}$ and it is normalized such that $\Tr\varrho^{\rm(eq)}=1$ . A thermal real-time correlation function for a Heisenberg field operator $\Phi(x)$ is given by the time-ordered trace $\displaystyle G^{\rm(eq)}(x-y)$ $\displaystyle=$ $\displaystyle\Tr\left\{\varrho^{\rm(eq)}\,\textrm{T}_{0}\Phi(x)\Phi(y)\right\}$ (1) $\displaystyle=$ $\displaystyle\langle\Phi(x)\Phi(y)\rangle_{\rm eq}\,\theta(x^{0}-y^{0})$ $\displaystyle+\>\langle\Phi(y)\Phi(x)\rangle_{\rm eq}\,\theta(y^{0}-x^{0})~,$ for a two-point function, and involves $n$ fields for a $n$ -point function. Here, $\textrm{T}_{0}$ is the time-ordering operator, $x=(x^{0},\boldsymbol{\mathit{x}})$ denotes the time $x^{0}$ and space $\boldsymbol{\mathit{x}}$ variables 1 1 1 We use a metric with signature $(+,-,-,-)$ . [...]
  § 2.2 Absence of a fluctuation-dissipation relation: In contrast to the general nonequilibrium case, it is an important simplification of thermal or vacuum theories that the statistical ( 4 ) and spectral function ( 5 ) are related by the so-called fluctuation-dissipation relation. We discuss this relation for the two-point correlation function with a canonical density matrix $\varrho^{\rm(eq)}\sim e^{-\beta H}$ . [...]
  § 7 Summary and outlook: In these lectures we have discussed different aspects of the nonequilibrium functional renormalization group. As an example, we considered the physics of wave turbulence in relativistic scalar $N$ -component field theory. We have seen that the standard treatment based on Boltzmann equations can only describe the perturbative regime of the associated stationary transport of conserved charges. In contrast, the functional renormalization group can efficiently describe the perturbative regime as well as the nonperturbative physics at low momenta. We have approximately solved the renormalization group equations using a (2PI) resummed large- $N$ expansion to NLO. This approximation is particularly suitable, since it provides an accurate description of the physics at not too small $N$ , while it is still analytically treatable. In particular, the scale derivatives are total derivatives in this approximation, which can be trivially integrated. [...]
[6] arXiv:1307.6891v1 | The Renormalization Group for Disordered Systems
  In this thesis we investigate the Renormalization Group (RG) approach in finite-dimensional glassy systems, whose critical features are still not well-established, or simply unknown. We focus on spin and structural-glass models built on hierarchical lattices, which are the simplest non-mean-field systems where the RG framework emerges in a natural way. The resulting critical properties shed light 
  Full text (https://arxiv.org/html/1307.6891v1), excerpts of its own sections:
  § Chapter 1 Historical outline: Paraphrasing P. W. Anderson [ 4 ] , “ the deepest and most interesting unsolved problem in solid state theory is probably the nature of glass and the glass transition ”. Indeed, the complex and rich behavior of simplified models for real, physical glassy systems has interested theoreticians for its challenging complexity and difficulty, and opened new avenues in a large number of other problems such as computational optimization and neural networks. When speaking of glassy systems, one can distinguish between two physically different classes of systems: spin glasses and structural glasses. Spin glasses have been originally [ 59 ] introduced as models to study disordered uniaxial magnetic materials, like a dilute solution of, say, Mn in Cu , modeled by an array of spins on the Mn arranged at random in the matrix of Cu , interacting with a potential which oscillates as a function of the separation of the spins. [...]
  § Chapter 2 Hierarchical models: In this Chapter we introduce hierarchical models. In Section 2.1 we first introduce the ferromagnetic version of hierarchical models originally introduced by Dyson, and in Section 2.2 we extend this definition to the disordered case, in the perspective to build up a non-mean-field hierarchical model of a spin or structural glass.
  § Part IV Conclusions: This thesis has investigated the implementation of renormalization-group (RG) techniques in finite-dimensional glassy systems, in order to shed light on the critical behavior of spin and structural glasses beyond mean field. In finite dimensions the existence of a phase transition in structural glasses is not well-established, and the structure of the low-temperature phase for both spin and structural glasses is fundamentally unknown and controversial. Since Wilson’s RG equations emerge in a natural and simple way in ferromagnetic spin models with a hierarchical interaction structure, in this work we considered two finite-dimensional models of spin and structural glasses built on Dyson’s hierarchical lattice [ 57 ] . After giving a brief introduction on spin and structural glasses in Part I , in Part II we focused on a structural-glass model built on a hierarchical lattice, the Hierarchical Random Energy Model (HREM) [ 33 , 32 ] . In this study, we showed the first evidence of a non-mean-field model of a supercooled liquid undergoing a Kauzmann phase transition. [...]
  § Appendix E Results of the two-loop RG calculation à la Wilson: Here we sketch the results of the perturbative calculation to the order $w_{k}^{5}$ mentioned in Section 5.1 . The invariants $I^{(j)}_{l}[Q]$ yielding $\mathscr{P}_{k}[Q]$ as a fifth-degree polynomial in $Q$ are given in Table E.1 . Table E.1: Invariants generated to the order $p=5$ . In each line of the table we show the invariants $I^{(j)}_{1}[Q],\ldots,I^{(j)}_{n_{j}}[Q]$ from left to right. $j$ $I_{l}^{(j)}[Q]$ $2$ $\text{Tr}[Q^{2}]$ $3$ $\text{Tr}[Q^{3}]$ $4$ $\text{Tr}[Q^{4}]$ $\text{Tr}[Q^{2}]^{2}$ $\sum_{a\neq c}Q_{ab}^{2}Q_{bc}^{2}$ $\sum_{ab}Q_{ab}^{4}$ $5$ $\text{Tr}[Q^{5}]$ $\text{Tr}[Q^{2}]\text{Tr}[Q^{3}]$ $\sum_{abcd}Q_{ab}^{2}Q_{bc}Q_{bd}Q_{cd}$ $\sum_{abc}Q_{ab}^{3}Q_{ac}Q_{bc}$ The recurrence RG equation ( 5.5 ) relating $\mathscr{P}_{k-1}[Q]$ to $\mathscr{P}_{k}[Q]$ yields a set of equations relating the coefficients $\{c^{(j)}_{l,\,k-1}\}_{j,l}$ to $\{c^{(j)}_{l,\,k}\}_{j,l}$ . [...]
[7] arXiv:1010.1942v1 | Quark Confinement and the Renormalization Group
  Recent approaches to quark confinement are reviewed, with an emphasis on their connection to renormalization group methods. Basic concepts related to confinement are introduced: the string tension, Wilson loops and Polyakov lines, string breaking, string tension scaling laws, center symmetry breaking, and the deconfinement transition at non-zero temperature. Current topics discussed include confin
  Full text (https://arxiv.org/html/1010.1942v1), excerpts of its own sections:
  § I Introduction: Quarks are the fermionic constituents of the hadrons, the strongly interacting particles such as the proton and the neutron. The problem of quark confinement, at its simplest, is to explain why quarks are not observed as physical states in high-energy scattering, but remain confined inside hadrons. The problem has been apparent for decades, and pre-dates quantum chromodynamics (QCD), the modern theory of the strong interactions [ 1 , 2 , 3 ] . Lattice gauge theory [ 4 , 5 ] has given us a physical basis for quark confinement: the force between quarks is independent of distance at large separation, and an infinite amount of energy would be required to isolate a single quark. The force constant at infinite separation is the string tension $\sigma$ . While lattice simulations have determined the relation of $\sigma$ to other observables of QCD with high precision, we are still far from a satisfactory understanding of quark confinement. [...]
  § II Fundamentals of confinement: The fundamental theory of the strong interactions is quantum chromodynamics (QCD), a quantum field theory describing the interactions of quarks and gluons. QCD is a gauge theory: Gluons are massless spin-1 bosons whose interactions are tightly constrained by the requirement of local gauge invariance in a manner similar to the case of QED (quantum electrodynamics) and photons. In QED, the symmetry group is $U(1)$ , the group of local phase transformations on charged fields: $\phi(x)\rightarrow e^{i\alpha(x)}\phi(x)$ . In QCD, the corresponding symmetry group is $SU(3)$ , and the symmetry acts on the three color charges carried by quarks, usually labeled as red, blue and green. There is a profound difference between QED and QCD: the gauge group $U(1)$ of QED is Abelian, but the gauge group $SU(3)$ of QCD is non-Abelian. Physically, this implies that the photon has no electric charge but gluons do carry color charge. [...]
  § III Confinement on $R^{3}\times S^{1}$: In the last few years, it has proven possible to construct four-dimensional gauge theories for which confinement may be reliably demonstrated using semiclassical methods [ 9 , 10 ] . These models combine $Z(N)$ symmetry, the effective potential for $P$ , instantons, and monopoles into a satisfying picture of confinement for a special class of models. All of the models in this class have one or more small compact directions. Models with an $R^{3}\times S^{1}$ topology have been most investigated, and discussion here will be restricted to this class. [...]
  § VI Conclusions: The problem of quark confinement is an important and vital subject in theoretical physics, connected not just to hadronic physics, but to many areas of physics by concepts and techniques. It is the quintessential problem of dimensional transmutation, where renormalization introduces a length scale into a classicaly scale-invariant system. Fundamental questions of mechanism, i.e., the cause of confinement, have not yet been answered. In addition to questions of mechanism, there are also questions surrounding the implications of confinements, e.g. , string tension scaling laws and other string properties. Approaches have been developed in the last few years that are shedding new light on these problems. The discovery of a rich set of new phases in gauge theories on $R^{3}\times S^{1}$ shows that there are new phenomena that remain to be uncovered. The topics discussed here, despite differences of approach and emphasis, have more in common with each other than the use of the renormalization group. [...]
[8] QNFO: Convergence Consilience and the Hierarchical Architecture of Reality | https://papers.qnfo.org/papers/static-architecture-of-reality-and-its-biological-interface
  This document argues that convergence (nature independently producing similar forms across separate lineages) and consilience (knowledge from different disciplines converging on the same truths) are symmetric faces of a single deeper structure: a hierarchically organized reality shaped by attractors in possibility space, as modeled by the renormalization group. Through a gallery of five interdisci
  Full text (https://papers.qnfo.org/papers/static-architecture-of-reality-and-its-biological-interface), excerpts of its own sections:
  § Convergence,: Consilience, and the Hierarchical Architecture of Reality **A Meta-Analysis with Worked Examples from Interdisciplinary Physics** **Author**: [Rowan Brad Quni-Gudzinas](mailto://rowan.quni@outlook.com) **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604) **DOI:** https://papers.qnfo.org/papers/static-architecture-of-reality-and-its-biological-interface/ **Date**: 2026-05-20 **Abstract**: This document argues that convergence (nature independently producing similar forms across separate lineages) and consilience (knowledge from different disciplines converging on the same truths) are symmetric faces of a single deeper structure: a hierarchically organized reality shaped by attractors in possibility space, as modeled by the renormalization group. Through a gallery of five interdisciplinary physics cases — gauge theory, effective field theory, universality, quantum geometry, and non-equilibrium dynamics — it demonstrates how mathematical structures discovered independently in disconnected fields later proved to be expressions of a deeper unity. [...]
  § §1. Introduction: What: This Project Is About This document is a **meta-analysis**: it does not construct a new physical framework (that space is occupied by the Consilience/Infomatics program; see [Consilience, 2025]), nor does it survey the historical landscape of convergent ideas (that work is done by Converging Reality; see [Converging Reality, 2025]). Rather, it analyzes convergence and consilience *as concepts*, examining their logical relationship, their empirical signatures, and their epistemological vulnerabilities. The analysis proceeds through three core claims: **Convergence and consilience are symmetric**: convergence is the ontological signature of attractors in possibility space; consilience is the epistemological program that reconstructs those attractors. They are the empirical and methodological faces of a single deeper assumption — that the tree of reality is shaped by lawful constraints that cross its branches. [...]
  § 2.1 Defining the Terms: **Convergence** (ontological): The independent origin of similar traits, forms, or ideas in distinct lineages, cultures, or minds — without direct descent or contact. Examples span biology (wings in birds, bats, and insects; camera eyes in vertebrates and cephalopods), culture (pyramids in Egypt and Mesoamerica; the independent invention of zero in Maya and Indian mathematics), and science (the calculus of Newton and Leibniz; the renormalization group of Gell-Mann/Low and Kadanoff/Wilson — see §5). [...]
  § §9. Summary: This document has argued for three claims: **Convergence and consilience are symmetric faces of a single deeper structure** — a hierarchically organized reality shaped by attractors in possibility space. Convergence is the ontological signature of those attractors; consilience is the epistemological program that reconstructs them. **The hierarchy is vindicated by a gallery of interdisciplinary physics convergences.** Gauge theory, effective field theory, universality, holography, and non-equilibrium dynamics all exhibit the same pattern: independent invention of the same mathematical structure in disconnected fields, followed by consilient recognition that the structure expresses a deeper unity. The renormalization group is the meta-example — simultaneously an instance of convergence and the mathematical mechanism that explains why convergence occurs. [...]