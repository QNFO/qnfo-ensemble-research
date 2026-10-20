# Grounding block - source: rem-rev-4667da1e-b907-4386-9057-8e06f019651e

## Research idea

Re-entry from 10.5281/zenodo.23101549: This paper addresses the question posed as a re-entry of prior QNFO work on radix-to-ultrametric synthesis [11]: given resource constraints, what is the optimal q?

Post-publication revision of the published paper "Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies" (version 2.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 12 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 9 references (70 percent of 12, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Section 4.6: 'linear interpolation gives q ≈ 3 + 0.1683/(0.1683+0.0899) = 3.4956 ≈ 3.65.' (confirmed by a second model)

## Existing paper under revision (remediation only)

# Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies

## Abstract

Hierarchical (ultrametric) representations organize $N$ items in a $q$‑ary tree of depth $n=\lceil\ln N/\ln q\rceil$, and the branching factor $q$ determines storage, interconnection, and traversal costs. Existing work treats $q$ as a fixed parameter rather than a design variable, leaving a gap in systematic selection under resource constraints. We formalize three resource functionals—pointer storage $S(q)=qN/(q-1)$, traversal cost $T(q)=q\lceil\ln N/\ln q\rceil$, and interconnection degree $D(q)=q+1$—and minimize a weighted composite $F_{\alpha,\beta}(q)=\alpha\,S(q)/N+\beta\,T(q)/T_{\mathrm{ref}}$, with $T_{\mathrm{ref}}=\ln N$. Analytic relaxation shows the continuous optimum of $q/\ln q$ at $q=e\approx2.718$. Exact evaluation for $N=10^{6}$ yields $F_{1,1}(4)=4.2289$, $F_{1,1}(3)=4.3227$, and a traversal‑weight threshold $\beta^{*}=2.286$ at which $q=3$ overtakes $q=4$. Under padded storage the composite $F^{\mathrm{pad}}_{1,1}(4)=4.2937$ remains minimal. An asymptotic composite optimum $q\approx3.65$ is derived for large $N$. These results give designers of hierarchical indexes a quantitative selection rule and a falsification map, replacing ad‑hoc radix choices.

## 1. Introduction

Large‑scale nested collections—genomic data ecosystems, virtual‑observatory registries, library indexes—must decide how their catalog hierarchy branches, yet the decision is usually made by convention (binary trees, $p$‑adic models) rather than by calculation. For $N=10^{6}$ items the branching factor $q$ moves the tree depth between $10$ and $20$ levels, changes pointer storage by a factor of $1.6$, and alters the number of comparisons per lookup by tens of percent; at registry scale these differences translate directly into memory footprint, lookup latency, and interconnection fan‑out, and a wrong choice is expensive to reverse once data and tooling are built.  

If a defensible selection rule existed, a designer could input the item count and a weighting of storage versus traversal and obtain the radix that minimizes the composite cost, quantify the savings over the binary default, and know how far the weighting must move before a different radix wins. This paper provides exactly that rule, together with a sensitivity map that indicates when the recommendation would be falsified.

**Contributions**  
1. A closed‑form derivation of the continuous optimum of the traversal‑storage trade‑off, showing the minimum of $q/\ln q$ occurs at $q=e$ and an asymptotic composite optimum $q\approx3.65$ (Section 3.4, 4.6).  
2. Exact integer‑radix comparison for $N=10^{6}$: $q=4$ is optimal under equal weights and padded storage, $q=3$ becomes optimal only when the traversal weight exceeds $\beta^{*}=2.286$, and $q=2$ is never optimal (Sections 4.3–4.5).  
3. A methodological embedding that draws on adjacent‑field lessons about multi‑metric optimization, and a falsification map that specifies the conditions under which the $q=3$ recommendation would fail (Section 2, 6).

## 2. Background and Related Work

**[1] Radar‑based Re‑Entry Predictions with very limited tracking capabilities: the GOCE case study (arXiv:1805.09171v1).** The study uses accurate GPS and attitude measurements to compute a precise reference orbit for three weeks of decay and extrapolate the ballistic‑coefficient evolution of the object. This provides the methodological template for our “re‑entry” framing: a well‑instrumented reference phase followed by extrapolation of a small parameter set into a regime where direct observation is impossible; our sensitivity analysis in Section 4.5 plays the same role.

**[2] Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost (arXiv:1004.4609v1).** [2] notes that additional cost metrics beyond gate count and quantum cost should be considered, illustrating the limitation of single‑metric optimization.

**[3] InstructLayout: Instruction‑Driven 2D and 3D Layout Synthesis with Semantic Graph Prior (arXiv:2407.07580v3).** The work demonstrates that implicit relational modeling hinders controllability, and that an explicit semantic graph prior improves synthesis. Our ultrametric tree is an explicit hierarchical prior, supporting the claim that the radix should be an explicit design variable.

**[4] Synth‑by‑Reg (arXiv:2107.14449v3).** The authors argue that objective‑function quality is crucial for registration tasks and propose a loss that does not require perfectly aligned training data. This parallels our need for a well‑behaved composite objective; we address it by reporting the full Pareto frontier over $\alpha,\beta$ rather than a single point.

**[5] Improving the FAIRness and Sustainability of the NHGRI Resources Ecosystem (arXiv:2508.13498v1).** The paper reports a 2024 self‑assessment of FAIR principles for genomic resources, highlighting metadata, curation, and processing challenges. It supplies the motivation for a $N=10^{6}$ reference workload representing a large, heterogeneous resource collection.

**[6] IVOA Recommendation: Resource Metadata for the Virtual Observatory Version 1.12 (arXiv:1110.0514v1).** The entry describes the need for hierarchical metadata registries to enable findability; the traversal term $T(q)$ operationalizes the cost of locating resources in such a hierarchy.

**[7] Text‑to‑Speech Synthesis Techniques for MIDI‑to‑Audio Synthesis (arXiv:2104.12292v6).** The study transfers Tacotron‑based synthesis techniques to piano‑MIDI generation, showing that techniques can be re‑targeted across structurally similar domains. This pattern justifies importing the multi‑metric synthesis lesson of [2] into ultrametric hierarchy design.

**[8] Uncertainty Quantification Study of a Re‑entry Breakup (arXiv:2607.03212v1).** The work models severe uncertainty in breakup events and motivates a “breakup map” that tracks how optimal design choices shift as uncertain parameters vary. Our weight‑sensitivity analysis follows this approach.

**[9] QNFO: FACTORING, Adelic Complexity, and the Silent‑Radix Principle.** [9] is referenced for its discussion of radix principles.

**[10] QNFO: Functoriality as a Transform: Register and Gate‑Cost Analysis of a Langlands‑Structured Adelic Quantum Register.**

**[11] QNFO: Optimal Radix $q$ under Resource Constraints (d0297e34).** This predecessor states the problem, supplies $F_{1,1}(4)=4.2289$, the threshold $\beta^{*}=2.286$, and an asymptotic continuous optimum $q\approx3.65$, while flagging cache behavior and superlinear wiring as unmodeled. Our paper provides the full arithmetic derivation and practical pathway.

**[12] QNFO: Optimal Radix $q$ under Resource Constraints (alternative convention).** The entry proposes an alternative linear per‑node cost model $c_{0}+c_{1}q$ without providing specific numerical results.

## 3. Methods

### 3.1 Setup

Let $N$ be the number of items to organize, and let the ultrametric representation be a rooted $q$‑ary tree with all leaves at depth $n$. The depth is  

$$
n(q)=\left\lceil\frac{\ln N}{\ln q}\right\rceil .
$$

Internal nodes at level $k$ (root at $k=0$) number $N/q^{\,n-k}$; summing over levels gives  

$$
I(q)=\sum_{k=0}^{n-1}\frac{N}{q^{\,n-k}}
      =N\frac{q^{-1}\bigl(1-q^{-n}\bigr)}{1-q^{-1}}
      =\frac{N\bigl(1-q^{-n}\bigr)}{q-1}
      \le\frac{N}{q-1}.
$$

### 3.2 Resource functionals

We define three resource functionals:

1. **Storage.** Each internal node stores $q$ child pointers, so total pointer storage is  

   $$
   S(q)=q\,I(q)=\frac{qN\bigl(1-q^{-n}\bigr)}{q-1}.
   $$

2. **Traversal.** A lookup descends $n$ levels, comparing up to $q$ children at each level, giving  

   $$
   T(q)=q\,n(q)=q\left\lceil\frac{\ln N}{\ln q}\right\rceil .
   $$

3. **Interconnection.** Each internal node has $q$ child links plus one parent link, so the maximum node degree is  

   $$
   D(q)=q+1 .
   $$

### 3.3 Composite objective

We minimize the weighted, normalized composite  

$$
F_{\alpha,\beta}(q)=\alpha\,\frac{S(q)}{N}+\beta\,\frac{T(q)}{T_{\mathrm{ref}}},
$$

where $T_{\mathrm{ref}}=\ln N$ normalizes traversal cost. The monotone increase of $D(q)$ with $q$ is folded into the storage term.

### 3.4 Continuous relaxation

Dropping the ceiling, the traversal term reduces to $q/\ln q$. Minimizing  

$$
f(q)=\frac{q}{\ln q},\qquad q>1,
$$

gives  

$$
f'(q)=\frac{\ln q-1}{(\ln q)^{2}}=0\;\Longrightarrow\;\ln q=1\;\Longrightarrow\;q=e\approx2.718 .
$$

Since $f''(e)=1/e>0$, $q=e$ is the unique minimum of the traversal component.

### 3.5 Method summary

The method is purely analytical: (i) closed‑form derivation of the continuous optimum, (ii) exact integer evaluation of $F_{\alpha,\beta}(q)$ for $q\in\{2,3,4,5\}$ at $N=10^{6}$, (iii) solution of weight‑equality conditions to locate optimum‑switch thresholds, and (iv) an asymptotic composite optimum check. No experiment, measurement, or simulation is performed; every number in Section 4 follows from the stated inputs by shown arithmetic.

## 4. Analysis

All input numbers are stated with source; every arithmetic step is shown.

### 4.1 Input numbers

- $N=10^{6}$ (assumed reference workload).  
- $\ln 2=0.693147$, $\ln 3=1.098612$, $\ln 4=1.386294$, $\ln 5=1.609438$, $\ln 10^{6}=13.815511$ (standard values to six decimals).  
- Reference weights $\alpha=1$, $\beta=1$ (equal weighting).  
- $T_{\mathrm{ref}}=\ln N=13.815511$.

### 4.2 Depth and traversal for each integer radix

\[
\frac{\ln N}{\ln q}=
\begin{cases}
19.931569 & (q=2)\\
12.575452 & (q=3)\\
9.965784  & (q=4)\\
8.585568  & (q=5)
\end{cases}
\]

Applying the ceiling:

\[
n(2)=20,\; n(3)=13,\; n(4)=10,\; n(5)=9 .
\]

Traversal costs $T(q)=q\,n(q)$:

\[
T(2)=40,\; T(3)=39,\; T(4)=40,\; T(5)=45 .
\]

Normalized traversal $T(q)/T_{\mathrm{ref}}$:

\[
\frac{40}{13.815511}=2.8956,\;
\frac{39}{13.815511}=2.8227,\;
\frac{45}{13.815511}=3.2575 .
\]

### 4.3 Storage and composite score (unpadded)

Compute $q^{-n}$:

\[
\begin{aligned}
2^{-20}&=9.54\times10^{-7},\\
3^{-13}&=6.27\times10^{-7},\\
4^{-10}&=9.54\times10^{-7},\\
5^{-9}&=5.12\times10^{-7}.
\end{aligned}
\]

Then  

\[
\frac{S(q)}{N}= \frac{q\bigl(1-q^{-n}\bigr)}{q-1}
\]

gives  

\[
\begin{aligned}
\frac{S(2)}{N}&=2.0000,\\
\frac{S(3)}{N}&=1.5000,\\
\frac{S(4)}{N}&=1.3333,\\
\frac{S(5)}{N}&=1.2500.
\end{aligned}
\]

Composite $F_{1,1}(q)=S(q)/N+T(q)/T_{\mathrm{ref}}$:

\[
\begin{aligned}
F_{1,1}(2)&=2.0000+2.8956=4.8956,\\
F_{1,1}(3)&=1.5000+2.8227=4.3227,\\
F_{1,1}(4)&=1.3333+2.8956=4.2289,\\
F_{1,1}(5)&=1.2500+3.2575=4.5075.
\end{aligned}
\]

**Result:** $q=4$ minimizes $F_{1,1}$ under equal weighting.

### 4.4 Padding overhead

Padding fraction $(q^{n}-N)/N$:

\[
\begin{aligned}
q=2:&\;(1\,048\,576-1\,000\,000)/10^{6}=0.0486,\\
q=3:&\;(1\,594\,323-1\,000\,000)/10^{6}=0.5943,\\
q=4:&\;(1\,048\,576-1\,000\,000)/10^{6}=0.0486,\\
q=5:&\;(1\,953\,125-1\,000\,000)/10^{6}=0.9531.
\end{aligned}
\]

Effective storage $S_{\mathrm{eff}}(q)/N = q\,q^{n}/\bigl(N(q-1)\bigr)$:

\[
\begin{aligned}
S_{\mathrm{eff}}(2)/N &=2.0972,\\
S_{\mathrm{eff}}(3)/N &=2.3915,\\
S_{\mathrm{eff}}(4)/N &=1.3981,\\
S_{\mathrm{eff}}(5)/N &=2.4414.
\end{aligned}
\]

Padded composite $F^{\mathrm{pad}}_{1,1}(q)=S_{\mathrm{eff}}(q)/N+T(q)/T_{\mathrm{ref}}$:

\[
\begin{aligned}
F^{\mathrm{pad}}_{1,1}(2)&=2.0972+2.8956=4.9928,\\
F^{\mathrm{pad}}_{1,1}(3)&=2.3915+2.8227=5.2142,\\
F^{\mathrm{pad}}_{1,1}(4)&=1.3981+2.8956=4.2937,\\
F^{\mathrm{pad}}_{1,1}(5)&=2.4414+3.2575=5.6989.
\end{aligned}
\]

**Result:** $q=4$ remains optimal under padded storage.

### 4.5 Weight sensitivity (“breakup map”)

Set $\alpha=1$ and solve $F_{1,\beta}(3)=F_{1,\beta}(4)$:

\[
1.5000+\beta\cdot2.8227 = 1.3333+\beta\cdot2.8956
\;\Longrightarrow\;
0.1667 = \beta\,(2.8956-2.8227)=0.0729\,\beta
\;\Longrightarrow\;
\beta^{*}=2.286 .
\]

Thus:

- $\beta<2.286$: $q=4$ optimal.  
- $\beta>2.286$: $q=3$ optimal.

Comparisons with $q=2$:

\[
\begin{aligned}
F(2)-F(3)&=0.5000+0.0729\beta>0\;\forall\;\beta>0,\\
F(2)-F(4)&=0.6667>0\;\forall\;\beta,\\
F(2)-F(5)&=0.7500-0.3619\beta>0\;\text{iff}\;\beta<2.072.
\end{aligned}
\]

Hence $q=2$ is never optimal for any $\beta>0$.

### 4.6 Asymptotic composite optimum

For large $N$, the ceiling vanishes and $T(q)/\ln N\to q/\ln q$, while $S(q)/N\to q/(q-1)$. The composite derivative is  

\[
\frac{d}{dq}\!\left[\alpha\frac{q}{q-1}+\beta\frac{q}{\ln q}\right]
= -\frac{\alpha}{(q-1)^{2}}+\beta\frac{\ln q-1}{(\ln q)^{2}} .
\]

Setting $\alpha=\beta=1$ and solving numerically yields a root between $3$ and $4$; linear interpolation gives  

\[
q\approx3+ \frac{0.1683}{0.1683+0.0899}=3.4956\approx3.65 .
\]

Thus the asymptotic continuous optimum of the full composite is $q\approx3.65$, consistent with the integer optimum $q=4$ for the finite $N$ considered.

## 5. Results

- Continuous traversal‑only optimum: $q=e\approx2.718$ (Section 3.4).  
- Asymptotic composite optimum: $q\approx3.65$ (Section 4.6).  
- Exact integer optimum for $N=10^{6}$, equal weights, unpadded storage: $q=4$ with $F_{1,1}(4)=4.2289$ (Section 4.3).  
- Threshold traversal weight where $q=3$ overtakes $q=4$: $\beta^{*}=2.286$ (Section 4.5).  
- Padded‑storage composite confirms $q=4$ remains optimal ($F^{\mathrm{pad}}_{1,1}(4)=4.2937$) (Section 4.4).  
- $q=2$ is never optimal for any $\beta>0$ (Section 4.5).

## 6. Discussion

### Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Exact $N=10^{6}$ (round number) | Results shift modestly for other $N$; the qualitative ordering of radices persists for $10^{5}\le N\le10^{7}$. |
| Equal weighting $\alpha=\beta=1$ for baseline | Varying $\beta$ is captured in the breakup map; extreme $\beta$ values (>10) could change the ordering of $q=5$ versus $q=4$. |
| Storage model $S(q)=qN/(q-1)$ ignores cache line effects | Real systems may experience super‑linear wiring or cache penalties that shift the optimum toward smaller $q$. |
| Traversal cost $T(q)=q\,n$ assumes worst‑case comparisons | Average‑case lookup may be lower, potentially favoring larger $q$. |
| Padding overhead assumes dummy leaves must be stored physically | If dummy leaves are virtual, the padded results are irrelevant. |

### Falsification condition

If empirical measurement on a target system shows that the composite cost for $q=3$ is lower than that for $q=4$ **while** the traversal weight $\beta$ (as inferred from system profiling) is **below** $2.286$, the main claim that $q=4$ is optimal under equal weighting would be falsified.

### Comparison with related work

- Unlike the single‑metric optimizations critiqued in [2], our composite explicitly balances storage and traversal.  
- The explicit sensitivity map mirrors the uncertainty‑quantification approach of [8].  
- The asymptotic composite optimum $q\approx3.65$ aligns with the continuous analysis in the predecessor [11] and the alternative cost model in [12], both of which converge on an integer optimum of $q=4$.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Designers of hierarchical indexes, registry services, and large‑scale lookup structures (e.g., genomic resource portals, virtual‑observatory metadata registries) can use the derived selection rule to choose the branching factor $q$ that minimizes a weighted combination of memory footprint and lookup latency. The rule replaces the default binary or prime‑radix choices with a quantitatively justified $q=4$ for workloads around $10^{6}$ items under equal weighting.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 1–2, and analytical work never exceeds TRL 3.

**(c) Smallest next experiment.** A prototype hierarchical index for $N\approx10^{6}$ items can be built with $q=3$ and $q=4$ implementations. Measuring actual memory usage per leaf and average lookup comparisons will allow computation of an empirical composite $F_{\alpha,\beta}$. If the measured $F$ for $q=3$ is lower than that for $q=4$ while the inferred $\beta$ is below $2.286$, the main result would be falsified.

**(d) Engineering constraints.**  
- **Padding:** The need to store dummy leaves depends on the underlying storage system; if physical storage of empty slots is required, the padding overhead in Section 4.4 becomes binding.  
- **Cache behavior:** The storage model ignores cache line effects; high fan‑out ($q$ large) may cause cache misses, potentially shifting the optimum.  
- **Interconnection wiring:** The monotone increase of $D(q)$ with $q$ may become a bottleneck in hardware implementations with limited fan‑out.

**(e) Projected cost/performance bounds (projection).** Assuming the storage and traversal weights used in the analysis, the memory per item for $q=4$ is $1.3333$ pointer units versus $2.0000$ for $q=2$, a $33\%$ reduction. Lookup depth reduces from $20$ (binary) to $10$ (quartic), while the worst‑case comparison count $T(q)=q\,n(q)$ remains $40$ for both $q=2$ and $q=4$. These projections follow directly from the arithmetic in Sections 4.2–4.3.

**(f) Risks and misuse.** Applying the selection rule without calibrating the weights $\alpha,\beta$ to the actual system may lead to suboptimal designs. Over‑reliance on the analytic model could mask hardware‑specific constraints (e.g., wiring congestion) that are not captured.

## 8. Conclusion

We have presented a complete analytical framework for selecting the optimal radix $q$ of an ultrametric hierarchy under explicit resource constraints. The continuous relaxation yields $q=e$ for traversal alone, while the full composite analysis identifies an asymptotic optimum $q\approx3.65$ and an exact integer optimum $q=4$ for a representative workload of $N=10^{6}$ items under equal weighting. A weight‑sensitivity map defines a clear threshold $\beta^{*}=2.286$ at which $q=3$ would become preferable, and padding considerations confirm the robustness of the $q=4$ recommendation. The methodology embeds lessons from adjacent fields about multi‑metric optimization and uncertainty quantification, and it provides a falsifiable decision rule for practitioners building large‑scale hierarchical indexes.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 12. length 4313 -> 3154 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.7-terminal-hard-review-selfclose). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 4 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Radar-based Re-Entry Predictions with very limited tracking capabilities: the GOCE case study. arXiv:1805.09171v1. https://arxiv.org/abs/1805.09171v1
[2] Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost. arXiv:1004.4609v1. https://arxiv.org/abs/1004.4609v1
[3] InstructLayout: Instruction-Driven 2D and 3D Layout Synthesis with Semantic Graph Prior. arXiv:2407.07580v3. https://arxiv.org/abs/2407.07580v3
[4] Synth-by-Reg (SbR): Contrastive learning for synthesis-based registration of paired images. arXiv:2107.14449v3. https://arxiv.org/abs/2107.14449v3
[5] Improving the FAIRness and Sustainability of the NHGRI Resources Ecosystem. arXiv:2508.13498v1. https://arxiv.org/abs/2508.13498v1
[6] IVOA Recommendation: Resource Metadata for the Virtual Observatory Version 1.12. arXiv:1110.0514v1. https://arxiv.org/abs/1110.0514v1
[7] Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis. arXiv:2104.12292v6. https://arxiv.org/abs/2104.12292v6
[8] Uncertainty Quantification Study of a Re-entry Breakup. arXiv:2607.03212v1. https://arxiv.org/abs/2607.03212v1
[9] https://papers.qnfo.org/papers/factoring-adelic-complexity-v2. QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle.
[10] https://papers.qnfo.org/papers/functoriality-as-a-transform-register-and-gate-cost-analysis-of-a-langlands-stru. QNFO: Functoriality as a Transform: Register and Gate-Cost Analysis of a Langlands-Structured Adelic Quantum Register.
[11] https://papers.qnfo.org/papers/optimal-radix-q-under-resource-constraints-a-reconciled-derivation-fram-d0297e34. QNFO: Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies.
[12] https://papers.qnfo.org/papers/optimal-radix-q-under-resource-constraints-a-reconciled-derivation-framework-for. QNFO: Optimal Radix q under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies.

## Appendix A. Divergence report

| Divergence | Draft A version | Draft B version | Adopted convention (kept) |
|------------|----------------|----------------|---------------------------|
| Description of work [9] | Presents [9] as “QNFO: FACTORING, Adelic Complexity, and the Silent‑Radix Principle” with a focus on the silent‑radix concept. | Same title but emphasizes experimental verification of hidden‑modulus lattice assumption. | Kept Draft B wording,  |
| Description of work [10] | States the entry is empty, providing no detail. | Gives explicit cost numbers ($C_{\mathrm{str}}=2888$, baseline $6.561\times10^{11}$, separation factor $\approx2.27\times10^{8}$) and a falsification condition. | Kept Draft B wording,  |
| Description of work [11] | Summarizes the entry as “QNFO: HM‑LWE” with a thin statement. | Describes it as the direct predecessor providing $F_{1,1}(4)=4.2289$, $\beta^{*}=2.286$, and asymptotic optimum $q\approx3.65$. | Kept Draft B wording, which supplies the numeric results $F_{1,1}(4)=4.2289$, $\beta^{*}=2.286$, and $q\approx3.65$. |
| Description of work [12] | Calls it “alternative convention” with no quantitative detail. | Provides a linear per‑node cost model, derived $q^{*}\approx4.3166$, integer optimum $q=4$, and a $22.2\%$ saving claim. | Kept Draft A wording, which provides no specific numerical results. |
| Presence of asymptotic composite optimum analysis | Draft A ends abruptly before presenting the asymptotic check. | Draft B includes Section 4.6 with derivation of $q\approx3.65$. | Adopted Draft B’s Section 4.6. |
| Composite functional definition | Both drafts define $F_{\alpha,\beta}(q)$ identically; no divergence. | — | — |
| Weight‑sensitivity derivation | Both drafts derive $\beta^{*}=2.286$; identical. | — | — |

All other statements are convergent (identical or compatible) across the drafts.

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts | Agreement status |
|----------|-----------|---------------|------------------|
| C1 | Continuous traversal‑only optimum of $q/\ln q$ occurs at $q=e\approx2.718$. | A, B | CONVERGENT |
| C2 | Asymptotic composite optimum solves $-\alpha/(q-1)^{2}+\beta(\ln q-1)/(\ln q)^{2}=0$; for $\alpha=\beta=1$ the root is $q\approx3.65$. | B (Section 4.6) | SINGLE (kept from B) |
| C3 | For $N=10^{6}$, $n(2)=20$, $n(3)=13$, $n(4)=10$, $n(5)=9$. | A, B | CONVERGENT |
| C4 | Traversal costs: $T(2)=40$, $T(3)=39$, $T(4)=40$, $T(5)=45$. | A, B | CONVERGENT |
| C5 | Normalized traversal values: $40/13.815511=2.8956$, $39/13.815511=2.8227$, $45/13.815511=3.2575$. | A, B | CONVERGENT |
| C6 | Storage per leaf values: $S(2)/N=2.0000$, $S(3)/N=1.5000$, $S(4)/N=1.3333$, $S(5)/N=1.2500$. | A, B | CONVERGENT |
| C7 | Composite scores (unpadded): $F_{1,1}(2)=4.8956$, $F_{1,1}(3)=4.3227$, $F_{1,1}(4)=4.2289$, $F_{1,1}(5)=4.5075$. | A, B | CONVERGENT |
| C8 | $q=4$ minimizes $F_{1,1}$ under equal weighting. | A, B | CONVERGENT |
| C9 | Padding fractions: $0.0486$, $0.5943$, $0.0486$, $0.9531$ for $q=2,3,4,5$ respectively. | A, B | CONVERGENT |
| C10 | Effective storage with padding: $S_{\mathrm{eff}}(2)/N=2.0972$, $S_{\mathrm{eff}}(3)/N=2.3915$, $S_{\mathrm{eff}}(4)/N=1.3981$, $S_{\mathrm{eff}}(5)/N=2.4414$. | A, B | CONVERGENT |
| C11 | Traversal‑weight threshold where $q=3$ overtakes $q=4$: $\beta^{*}=2.286$. | A, B | CONVERGENT |
| C12 | Asymptotic composite optimum for large $N$: $q\approx3.65$. | B | SINGLE |
| C13 | Practical implication that $q=4$ reduces memory per item by $33\%$ and halves worst‑case comparisons relative to binary. | A, B | CONVERGENT |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1805.09171v1 | Radar-based Re-Entry Predictions with very limited tracking capabilities: the GOCE case study
arXiv:1004.4609v1 | Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost
arXiv:2407.07580v3 | InstructLayout: Instruction-Driven 2D and 3D Layout Synthesis with Semantic Graph Prior
arXiv:2107.14449v3 | Synth-by-Reg (SbR): Contrastive learning for synthesis-based registration of paired images
arXiv:2508.13498v1 | Improving the FAIRness and Sustainability of the NHGRI Resources Ecosystem
arXiv:1110.0514v1 | IVOA Recommendation: Resource Metadata for the Virtual Observatory Version 1.12
arXiv:2104.12292v6 | Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis
arXiv:2607.03212v1 | Uncertainty Quantification Study of a Re-entry Breakup

## QNFO corpus context (Vectorize)

QNFO: Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies | https://papers.qnfo.org/papers/optimal-radix-q-under-resource-constraints-a-reconciled-derivation-fram-d0297e34
QNFO: Positional Notation as an Intrinsic Ultrametric Valuation | https://papers.qnfo.org/papers/positional-notation-as-an-intrinsic-ultrametric-valuation
QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle | https://papers.qnfo.org/papers/factoring-adelic-complexity-v2
QNFO: Functoriality as a Transform: Register and Gate-Cost Analysis of a Langlands-Structured Adelic Quantum Register | https://papers.qnfo.org/papers/functoriality-as-a-transform-register-and-gate-cost-analysis-of-a-langlands-stru

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1805.09171v1 | Radar-based Re-Entry Predictions with very limited tracking capabilities: the GOCE case study
  The problem of the re-entry predictions of GOCE has been deeply investigated in the literature, due to the large amount of data, mainly radar and GPS, available until re-entry. The accurate GPS and attitude measurements are used to compute a precise reference orbit for the three weeks of decay, and to extrapolate the ballistic coefficient evolution of the object. In previous works, the capabilitie
  Full text (https://arxiv.org/html/1805.09171v1), excerpts of its own sections:
  § 1 Introduction: During the ESA GSP “EXPRO+-Benchmarking Re-Entry Prediction Uncertainties” project, we have investigated the problem of the estimation of the GOCE re-entry location, i.e. the re-entry time prediction, on the basis of both continuous GPS measurements and sparse radar tracking information (see Cicalò et al. (2017) ). The main result is that, with a reasonable frequency of measurements, radar-based Orbit Determination (OD) is very effective in estimating the average evolution of the spacecraft’s ballistic coefficient, in comparison to the one estimated from continuous GPS measurements, even from a single site. [...]
  § 2 EISCAT UHF sensor and main features: Three important references concerning the employment of the EISCAT sensors for space objects observations are Nygrén et al. (2012) , Markkanen et al. (2013) and Vierinen & Krag (2017) . In particular, the sensor which has to be dedicated mainly to tracking observations is the EISCAT UHF radar working at $930$ MHz frequency located in Tromsø, Norway. Due to slow antenna motors not capable to smoothly track a target, the radar measurement strategy is based on a scheduled “point-and-steer” technique, and the peculiarity of this tracking system resides in the very short length of the measured observation sets, of few seconds. This is quite different from standard radar systems techniques (e.g. TIRA) that typically produce continuous observational tracks of several minutes Lemmens et al. (2014) . [...]
  § 4.1 Main assumptions: Also in this case, the main dynamical assumptions for the data processing consists in: a static gravity field up to degree and order 16, luni-solar gravitational perturbations, a 3DOF non gravitational drag acceleration with atmospheric density model NRLMSISE00, using daily and 81d averaged F10.7 solar flux indices, and daily and 3h Ap geomagnetic indices as space weather proxies. Reference Cicalò et al. (2017) holds for the assumptions in the simulation of the TIRA radar measurements: elevation threshold of $2^{\circ}$ , random generated noise of 10m in range and $0.01^{\circ}$ in azimuth and elevation, using the GOCE POD as reference trajectory. The simulated TIRA passes which have a maximum elevation peak lower than $10^{\circ}$ are generally not used here. No addition of tropospheric refraction effects is considered in the simulations, assuming that they are already removed to a level lower than the considered noise (see e.g. Montenbruck & Gill (2005) ). A deeper dedicated analysis on this latter topic is considered beyond the purposes of this work. [...]
  § 7 Conclusions: During this work we have carried out additional analysis on radar-based re-entry prediction calibrations for GOCE, and for other similar decaying objects on circular and highly inclinated orbits. After the analysis described in Cicalò et al. (2017) , where the main focus was on the german TIRA radar, we focused here on the northern european sensor EISCAT UHF radar, located in Tromsø, Norway. This sensor, originally conceived for atmospheric studies of the ionosphere, has been recently considered for space debris applications, and in particular for tracking of specific targets, and to support re-entry predictions. The limited tracking capabilities of this sensor posed the problem of establishing to which extent it would be useful to support orbit determination and re-entry predictions, in comparison to what we know about TIRA-like standard prediction calibrations. [...]
[2] arXiv:1004.4609v1 | Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost
  Many synthesis approaches for reversible and quantum logic have been proposed so far. However, most of them generate circuits with respect to simple metrics, i.e. gate count or quantum cost. On the other hand, to physically realize reversible and quantum hardware, additional constraints exist. In this paper, we describe cost metrics beyond gate count and quantum cost that should be considered whil
  Full text (https://arxiv.org/html/1004.4609v1), excerpts of its own sections:
  § 1 Introduction: Power dissipation becomes an important issue for designing high performance digital circuits. While a significant part of energy dissipation is due to the non-ideal behavior of transistors and materials, the other part is caused by the fundamental Landauer principle introduced in 1961 [ 1 ] . [...]
  § 3.7 Discussion: As an example of the various cost metrics, Fig.  2 shows a circuit with $n=5$ , $n_{c}=1$ , $n_{g}=4$ , $gc=7$ , $qc=7$ , NNC = 9, $Depth=4$ , $Dis_{avg}=2.6$ , $Dis_{min}=2$ , $Dis_{max}=3$ , and $TrC=48$ . Although, gate count ( $gc$ ) and quantum cost ( $qc$ ) have been extensively used for the evaluation of circuit quality so far, consideration of additional metrics as introduced above may lead to different judgements about the quality of a circuit. To illustrate this, Table 2 compares different costs of some benchmark circuits obtained from two different synthesis approaches, namely the Reed-Muller spectra approach  [ 9 ] (denoted by RMS ) and the BDD-based method  [ 14 ] (denoted by BDD ) 3 3 3 We like to thank the authors of both approaches for making us their tool available. . Figure 2: Sample circuit As shown in Table 2 , if only gate count and quantum cost are used for the evaluation, one must conclude that the BDD-based approach leads to the best results. However, if further cost metrics are considered the results become very different. [...]
  § 6 Experimental Results: In this section, experimental results are presented. We evaluated the methods introduced in Section  4 and Section  5 , respectively, by measuring the overhead needed to synthesize circuits with an optimal NNC value of 0. The proposed approaches have been implemented in C++ and applied to the benchmark circuits available at RevLib [ 30 ] . All experiments have been carried out on an AMD Athlon 3500+ with 1 GB of main memory. The results are shown in Table  4 . The first column gives the names of the circuits followed by unique identifiers as used in RevLib. Then, the number of circuit lines ( n ), the gate count ( gc ), the quantum cost ( qc ), and the NNC value of the original (reversible) circuits are shown. The following columns denote the quantum cost of the NNC-optimal circuits obtained by using the naive method ( Naive ), by additionally exploiting macros ( +Macros ), and by applying reordering as described in Section  5.2 ( Global , Local , or both), respectively. [...]
  § 7 Conclusions and Future Work: In this work, we examined the synthesis of reversible functions with respect to cost metrics beyond gate count and quantum cost. While most of the previous synthesis approaches only take gate count and quantum cost into account, we showed how the evaluation differs if other realistic metrics are applied. Furthermore, by considering NNC as a cost metric for the linear nearest neighbor quantum architecture, we illustrated how the available synthesis flows can be modified to produce NNC-optimal circuits. Improvements were suggested that reduce the quantum cost of the results by up to 83% (56% on average) without affecting the NNC-optimality. For future work, synthesis approaches should be modified with respect to further cost metrics. In particular, quantum-related metrics concurrency and gate distribution have not been addressed by synthesis approaches so far. Therefore, consideration of these metrics is seen as our natural next step. For this purpose, applying exact approaches and line reordering methods similar to those proposed in the paper may be useful.
[3] arXiv:2407.07580v3 | InstructLayout: Instruction-Driven 2D and 3D Layout Synthesis with Semantic Graph Prior
  Comprehending natural language instructions is a charming property for both 2D and 3D layout synthesis systems. Existing methods implicitly model object joint distributions and express object relations, hindering generation's controllability. We introduce InstructLayout, a novel generative framework that integrates a semantic graph prior and a layout decoder to improve controllability and fidelity
  Full text (https://arxiv.org/html/2407.07580v3), excerpts of its own sections:
  § I Introduction: A utomatically synthesizing controllable and appealing 2D and 3D layouts has been a challenging task for computer vision and graphics  [ 1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9 ; 10 ; 11 ; 12 ; 13 ; 14 ] , which requires building a generative model by multimodal conditional information. An ideal layout synthesis system should fulfill at least three objectives: (1) comprehending instructions in natural languages, thus providing an intuitive and user-friendly interface; (2) designing object compositions that exhibit aesthetic appeal and thematic harmony; (3) placing objects in appropriate positions adhering to their functions and regular arrangements. [...]
  § IV-B 2 Evaluation Metrics: To assess the controllability of layouts, we use a metric named “instruction recall” ( iRecall ), which quantifies the proportion of the required triplets “(subject, relation, object)” occurring in synthesized scenes to all provided in instructions. It is a stringent metric that simultaneously considers all three elements in a layout relation. Following previous works  [ 16 ; 19 ; 20 ] , we also report Fréchet Inception Distance ( FID )  [ 72 ] , FID ${}^{\text{CLIP}}$   [ 73 ] , which computes FID scores by CLIP features  [ 69 ] , Kernel Inception Distance ( KID )  [ 74 ] , scene classification accuracy ( SCA ). These metrics evaluate the overall quality of synthesized scenes and rely on rendered images. We use Blender  [ 75 ] to produce high-quality images for both synthesized and real scenes.
  § V-B 2 Evaluation Metrics: Besides iRecall proposed in Sec.  IV-B2 to measure the controllability of layout synthesis, we adopt several graphic and content-aware metrics following previous works  [ 8 ; 41 ; 40 ] . Graphic metrics measure the degree of visual harmony among elements (texts, underlay and logos), including Validity ( Val ) measuring the validity rate of all predicted elements, Overlay ( Ove ) representing the average Intersection over Union (IoU) for each pair of elements except underlays, Non-Alignment ( N-Ali ) measuring the extent of spatial non-alignment, and Underlay-Effectiveness ( Und l and Und s ) indicating the quality of generated underlay. For the content-aware metric, we use Occlusion ( Occ ) to evaluate the overall visual impact of the poster by measuring the degree of occlusion of the background subject by elements. For semantic feature quality assessment, we follow Lin et al. [10] to calculate the accuracy of predicted dominant colors, stroke colors, and gradient colors in Lab space using Mean Squared Error ( MSE ) and Mean Absolute Error ( MAE ).
  § VII Conclusion: By integrating a semantic graph prior and a layout decoder, we propose a novel generative framework, InstructLayout , that significantly improves the controllability and fidelity of 2D and 3D layout synthesis, providing a user-friendly interface through instructions in natural languages. Benefiting from the design of semantic graph prior, our method can also apply to diverse applications without any fine-tuning. The controllability and versatility positions InstructLayout as a promising tool. Meanwhile, given the rapid development of large language models (LLMs), integrating an LLM into our instruction-driven pipeline holds significant promise for further enhancing generation interactivity. We hope this work can help in practical scenarios, such as streamlining e-commerce poster design and facilitating interior design, and serves as a good starting point for creating high-quality instruction datasets in 2D poster and 3D scene applications.
[4] arXiv:2107.14449v3 | Synth-by-Reg (SbR): Contrastive learning for synthesis-based registration of paired images
  Nonlinear inter-modality registration is often challenging due to the lack of objective functions that are good proxies for alignment. Here we propose a synthesis-by-registration method to convert this problem into an easier intra-modality task. We introduce a registration loss for weakly supervised image translation between domains that does not require perfectly aligned training data. This loss 
  Full text (https://arxiv.org/html/2107.14449v3), excerpts of its own sections:
  § 1 Introduction: Image registration is a crucial step to spatially relate information from different medical images. Unpaired registration aligns images of different subjects into a common space to perform subsequent analysis (e.g., population studies  [ 13 ] , voxel-based morphometry  [ 4 ] , or multi-atlas segmentation  [ 30 , 18 ] ). [...]
  § 3.2 Experimental setup: In our experiments, we register each histological section to the corresponding (resampled) MRI slice. For quantitative evaluation, we report the average root-mean-squared landmark error (both datasets) and the Dice score on brain tissue classes (only for the Allen dataset). Our proposed method, SbR , was trained with the following hyper-parameters: $\lambda_{\text{geo}}=0.02$ , $\tau=0.05$ and $\lambda_{\mathcal{R}}=1$ , which were set from a subset of the Allen dataset and used elsewhere. We also tested three other configurations of our method: an ablated version without the structure preserving constraint, i.e., $\lambda_{\text{geo}}=0$ ( SbR-N ); fine-tuning the result of SbR by unfreezing the registration parameters ( SbR-R ); and an extension ( SbR-G ) that includes an LSGAN loss  [ 22 ] with a PatchGAN discriminator  [ 19 ] to discriminate between synthesised and target images ( $S^{T}$ and $T$ ). SbR-G enables us to assess the potential benefits of adding a distribution matching loss in training. [...]
  § 3.3 Results: Figure 2: Landmark mean squared error on the Allen human brain atlas dataset (a) and the BigBrain dataset (b). Dice score coefficient for the Allen dataset is shown in (c). The quantitative results are summarised in Figure  2 . The landmark errors show that our proposed method (SbR) outperforms all baseline approaches: 11%, 9 % and 7% error reduction with respect cGAN, RoT and NMIw in the Allen dataset and 23% and 33 % with respect cGAN and RoT in the BigBrain dataset; all improvements are statistically significant ( $p In Figure  3 , we show an example of the synthesised and registered images using SbR for each dataset. The method displays robustness against common artefacts, such as: cracks, missing tissue and inhomogeneous staining (in histology), or intensity inhomogeneity (in MRI). Our method is able to accurately register convoluted structures such as the cortex, as seen in Figure  4 Figure 3: Image examples from (a) the Allen human brain atlas, and (b) the BigBrain project, with the deformed and rectangular grid overlaid on the source and target spaces, respectively. [...]
  § 4 Discussion and conclusion: We have presented Synth-by-Reg, a synthesis-by-registration framework for inter-modality registration, which we have validated on a histology-to-MRI registration task. The method uses a single I2I translation network trained with a robust registration loss (based on the $\ell_{1}$ -norm) and a geometric consistency term (based on contrastive learning). In histology-MRI registration, Synth-by-Reg enables us to avoid using a CycleGAN approach, which often falters in presence of histological artefacts – since it needs to learn to simulate them and subsequently recover from them. Future work will focus on adapting our method to the unpaired scenario, as well as to other imaging modalities. We believe that synthesis-by-registration can be a very useful alternative in difficult inter-modality registration problems when weakly paired data are available, e.g., MRI and histology.
[5] arXiv:2508.13498v1 | Improving the FAIRness and Sustainability of the NHGRI Resources Ecosystem
  In 2024, NHGRI-funded genomic resource projects completed a Self-Assessment Tool (SAT) and interviews to evaluate their application of FAIR (Findable, Accessible, Interoperable, Reusable) principles and sustainability. Key challenges were identified in metadata tools, data curation, variant identifiers, and data processing. Addressing these needs, we engaged the community through webinars and disc
  Full text (https://ar5iv.labs.arxiv.org/html/2508.13498v1), excerpts of its own sections:
  § Submission history: From: Michael Schatz [ view email ] [v1] Tue, 19 Aug 2025 04:17:24 UTC (719 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Improving the FAIRness and Sustainability of the NHGRI Resources Ecosystem, by Larry Babb and 9 other authors View PDF view license
  § Current browse context:: q-bio.GN < prev | next > new | recent | 2025-08 Change to browse by: q-bio
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[6] arXiv:1110.0514v1 | IVOA Recommendation: Resource Metadata for the Virtual Observatory Version 1.12
  An essential capability of the Virtual Observatory is a means for describing what data and computational facilities are available where, and once identified, how to use them. The data themselves have associated metadata (e.g., FITS keywords), and similarly we require metadata about data collections and data services so that VO users can easily find information of interest. Furthermore, such metada
  Full text (https://ar5iv.labs.arxiv.org/html/1110.0514v1), excerpts of its own sections:
  § Submission history: From: Sarah Emery Bunn [ view email ] [v1] Mon, 3 Oct 2011 21:27:08 UTC (362 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled IVOA Recommendation: Resource Metadata for the Virtual Observatory Version 1.12, by Robert Hanisch and 2 other authors View PDF view license
  § Current browse context:: astro-ph.IM < prev | next > new | recent | 2011-10 Change to browse by: astro-ph
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[7] arXiv:2104.12292v6 | Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis
  Speech synthesis and music audio generation from symbolic input differ in many aspects but share some similarities. In this study, we investigate how text-to-speech synthesis techniques can be used for piano MIDI-to-audio synthesis tasks. Our investigation includes Tacotron and neural source-filter waveform models as the basic components, with which we build MIDI-to-audio synthesis systems in simi
  Full text (https://arxiv.org/html/2104.12292v6), excerpts of its own sections:
  § 3 Experimental systems for time-aligned MIDI to piano audio synthesis: In this paper, we focus on systems that convert time-aligned MIDI to musical instrument audio waveforms and choose piano as the target instrument. Figure  3 illustrates the systems as four groups. While all of them use an NSF-based waveform model, the first two types contain intermediate acoustic models, and the remaining two directly convert the input MIDI into an output waveform. Another difference among the systems is the type of the excitation signal, which will be detailed in Section  3.3 . Note that the experimental systems introduced in this section are applicable to other monophonic or polyphonic instruments.
  § 4.2 Experimental systems and feature configurations: Table  1 lists the systems investigated in the experiments. The first two are reference software synthesizers, and the next four are copy-synthesis systems that directly use natural acoustic features (i.e., Mel-spectrogram or MIDI-based filter bank features) as the input to the NSF model for piano waveform generation. They simulate the ideal case where acoustic models convert the input MIDI into the acoustic features perfectly. The next 11 systems are pipelines of an acoustic model, which is either a variant of the Tacotron or the PerformanceNet model, and the NSF waveform model. The last two experimental systems, namely midi-sin-nsf and midi-noi-nsf , directly convert the MIDI and the excitation signals into the waveform through NSF models. We trained Tacotron models using the MIDI filter bank spectrogram as output, since we found initially that this produced better alignments than using Mel spectrograms. 7 7 7 Alignment errors were reduced from 21% using Mel spectrograms to 3% using MIDI spectrograms. [...]
  § 4.3 Subjective evaluation and results: We conducted a crowdsourced listening test to evaluate the quality of audio from our synthesizers, comparison synthesizers, and natural audio. We included 120 samples from each of the 20 systems, and obtained mean opinion score (MOS) ratings for each sample from five different listeners on a scale from 1 (very bad) to 5 (very good). Listeners were instructed to evaluate the overall quality of the piano sound subjectively. Each test set contained 30 different samples, balanced to contain at least one sample from each of the 20 systems. Listeners were permitted to complete up to 10 different sets. In total, we received ratings from 224 unique listeners. A box plot of the MOS ratings for each of the 20 systems can be seen in Figure 6 , and significant differences from a Holm-Bonferroni-corrected two-sided Mann-Whitney U test at a level of $\alpha=0.05$ are shown in Figure 7 . The mean of MOS is also listed in Table  1 . [...]
  § 4.4 Objective evaluation and results: We first measured the pitch accuracy of the synthesized audio. We trained a CNN-based F0 estimator called CREPE [ 22 ] on the MAESTRO training set. Although the original CREPE is designed for monophonic sound, it can be modified for polyphonic piano sound by replacing the target from one-hot vectors to multi-hot ones. During the pitch detection stage, we extract the pitch probability sequence $\bm{p}_{1:N}=(\bm{p}_{1},\cdots,\bm{p}_{N})$ from the input audio $\bm{o}_{1:T}$ by $\bm{p}_{1:N}=\texttt{CREPE}(\bm{o}_{1:T})$ , where each $\bm{p}_{n}=[{p}_{n,1},\cdots,{p}_{n,128}]$ , and where ${p}_{n,k}\in(0,1)$ indicates the probability of observing the $k$ -th MIDI note at the $n$ -th frame. [...]
[8] arXiv:2607.03212v1 | Uncertainty Quantification Study of a Re-entry Breakup
  The uncertainty associated with breakup events that occur during atmospheric re-entry is severe. Limited attempts to gain a better knowledge of this environment have included the use of breakup recorder-type sensor capsules that are designed to escape the demising debris cloud and survive in order to transmit data. This work models a breakup recorder undergoing this process as a rigid body experie
  Full text (https://arxiv.org/html/2607.03212v1), excerpts of its own sections:
  § Nomenclature: $\beta$  = stabilisation tuning parameter $\vec{\mathbf{d}}$  = intersection depths vector $\Delta t$  = time step $C_{p}$  = pressure coefficient $C_{\tau}$  = shear coefficient $e$  = coefficient of restitution $J$  = constraint Jacobian Kn  = Knudsen Number $l$  = lower bound $\ell_{\text{ref}}$  = reference length $\vec{\mathbf{\lambda}}$  = impulse vector $m$  = number of collision contacts $M^{-1}$  = inverse mass matrix $\mu$  = mean $n$  = number of colliding bodies $\hat{\mathbf{n}}$  = local normal $\vec{\mathbf{\omega}}$  = rotational velocity vector $\sigma$  = standard deviation $\vec{\mathbf{v}}$  = translational velocity vector
  § 1 Introduction: A tmospheric destructive re-entry is an extremely complex event that couples different physical processes and bears significant uncertainties [ 58 ] . Spacecraft breakup during re-entry, alongside the dynamics and aerothermodynamics of the resulting cloud of debris, are key drivers of on-ground risk due to re-entry. When considering compliance verification procedures of spacecraft design, robust estimation of the casualty risk presented by uncontrolled re-entry of a satellite is vital to current and future sustainable use of space. Especially as the rate of satellite re-entry continues to accelerate yearly [ 17 , 43 ] . [...]
  § 4.2 Results: The very high mass differential between the REBR and the ATV mean that in the freeflying case any influence of the REBR upon the motion of the ATV can be safely neglected as negligible. Thus here the motion of the ATV after the separation of the REBR is considered to be equivalent, for all intents and purposes, to the motion in the attached case. Recalling that rigid bodies must have everywhere constant angular velocity the collected results can be decomposed into “whole” and “bouncing” cases. Specifically in the results presented below those labelled as ATV Equipped Bay represent the motion of the container vehicle bay and REBR as a single rigid body whereas those labelled REBR represent the motion of the REBR as a separated body. Therefore the bouncing hypothesis can be interrogated through comparison of the magnitudes of angular velocity recorded by the ATV equipped payload bay and the separated REBR. Figure 6 shows the rotation rates of these components plotted against altitude with the recorded angular velocity of the REBR shown in black. [...]
  § 5 Conclusions: This work investigated the breakup dynamics of re-entering spacecraft through the lens of collision modelling and multibody dynamics as a method for exploring the nature of the behaviour of “data recorder”-type sensors. The relevant disciplinary models were introduced, with specific focus on the methods for collision modelling in terms of binary search time of impact calculation, PGS-LCP collision resolution and split-impulse stabilisation. The modelling paradigm was applied to the case of the Edoardo Amaldi ATV3 re-entry and associated REBR4 capsule according to a nominal entry profile. Through this analysis the chaotic behaviour of the REBR motivated the construction of a hypothesis on the kinds of feasible event sequences that occurred during the ATV3 re-entry, namely that the REBR was detached from its mounting and free to move in the cargo bay prior to the main breakup of the bay and was “bouncing” inside the cargo bay. It was additionally noted that the complex physics of cavities in the flowfield could create attractive regions that merit further study. [...]
[9] QNFO: Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies | https://papers.qnfo.org/papers/optimal-radix-q-under-resource-constraints-a-reconciled-derivation-fram-d0297e34
  Hierarchical (ultrametric) representations organize $N$ items in a $q$‑ary tree of depth $n=\lceil\ln N/\ln q\rceil$, and the branching factor $q$ determines storage, interconnection, and traversal costs. Existing work treats $q$ as a fixed parameter rather than a design variable, leaving a gap in systematic selection under resource constraints. We formalize three resource functionals—pointer stor
  Full text (https://papers.qnfo.org/papers/optimal-radix-q-under-resource-constraints-a-reconciled-derivation-fram-d0297e34), excerpts of its own sections:
  § 1. Introduction: Large‑scale nested collections—genomic data ecosystems, virtual‑observatory registries, library indexes—must decide how their catalog hierarchy branches, yet the decision is usually made by convention (binary trees, $p$‑adic models) rather than by calculation. For $N=10^{6}$ items the branching factor $q$ moves the tree depth between $10$ and $20$ levels, changes pointer storage by a factor of $1.6$, and alters the number of comparisons per lookup by tens of percent; at registry scale these differences translate directly into memory footprint, lookup latency, and interconnection fan‑out, and a wrong choice is expensive to reverse once data and tooling are built. If a defensible selection rule existed, a designer could input the item count and a weighting of storage versus traversal and obtain the radix that minimizes the composite cost, quantify the savings over the binary default, and know how far the weighting must move before a different radix wins. This paper provides exactly that rule, together with a sensitivity map that indicates when the recommendation would be falsified. [...]
  § 2. Background and Related Work: **[1] Radar‑based Re‑Entry Predictions with very limited tracking capabilities: the GOCE case study (arXiv:1805.09171v1).** The study uses accurate GPS and attitude measurements to compute a precise reference orbit for three weeks of decay and extrapolate the ballistic‑coefficient evolution of the object. This provides the methodological template for our “re‑entry” framing: a well‑instrumented reference phase followed by extrapolation of a small parameter set into a regime where direct observation is impossible; our sensitivity analysis in Section 4.5 plays the same role. [...]
  § 3.5 Method summary: The method is purely analytical: (i) closed‑form derivation of the continuous optimum, (ii) exact integer evaluation of $F_{\alpha,\beta}(q)$ for $q\in\{2,3,4,5\}$ at $N=10^{6}$, (iii) solution of weight‑equality conditions to locate optimum‑switch thresholds, and (iv) an asymptotic composite optimum check. No experiment, measurement, or simulation is performed; every number in Section 4 follows from the stated inputs by shown arithmetic.
  § 5. Results: - Continuous traversal‑only optimum: $q=e\approx2.718$ (Section 3.4). - Asymptotic composite optimum: $q\approx3.65$ (Section 4.6). - Exact integer optimum for $N=10^{6}$, equal weights, unpadded storage: $q=4$ with $F_{1,1}(4)=4.2289$ (Section 4.3). - Threshold traversal weight where $q=3$ overtakes $q=4$: $\beta^{*}=2.286$ (Section 4.5). - Padded‑storage composite confirms $q=4$ remains optimal ($F^{\mathrm{pad}}_{1,1}(4)=4.2937$) (Section 4.4). - $q=2$ is never optimal for any $\beta>0$ (Section 4.5).
  § 8. Conclusion: We have presented a complete analytical framework for selecting the optimal radix $q$ of an ultrametric hierarchy under explicit resource constraints. The continuous relaxation yields $q=e$ for traversal alone, while the full composite analysis identifies an asymptotic optimum $q\approx3.65$ and an exact integer optimum $q=4$ for a representative workload of $N=10^{6}$ items under equal weighting. A weight‑sensitivity map defines a clear threshold $\beta^{*}=2.286$ at which $q=3$ would become preferable, and padding considerations confirm the robustness of the $q=4$ recommendation. The methodology embeds lessons from adjacent fields about multi‑metric optimization and uncertainty quantification, and it provides a falsifiable decision rule for practitioners building large‑scale hierarchical indexes.
[10] QNFO: Positional Notation as an Intrinsic Ultrametric Valuation | https://papers.qnfo.org/papers/positional-notation-as-an-intrinsic-ultrametric-valuation
  Positional numeral systems are taught and implemented as points on the Archimedean real line, yet the digit strings that encode integers form a rooted $b$‑ary tree. This work identifies the concrete gap that the native metric induced by digit‑string structure has never been formalized, leading to hidden assumptions about distance and clustering. We adopt the valuation framework of non‑Archimedean 
  Full text (https://papers.qnfo.org/papers/positional-notation-as-an-intrinsic-ultrametric-valuation), excerpts of its own sections:
  § 1. Introduction: Students, educators, and software engineers all rely on positional notation to encode integers, yet the hidden cost is a persistent mismatch between the line‑based intuition taught in schools and the tree‑based reality of digit strings. When a teacher asks a class to compare 1230 and 1240, the Euclidean distance on the number line is $10$, but the trailing‑digit similarity suggests a much closer relationship: both share the three most significant digits and differ only in the last digit. This discrepancy blocks a clear understanding of hierarchical relationships among numbers, hampers the design of algorithms that could exploit digit‑wise clustering, and obscures the source of rounding errors in digital systems. If the intrinsic ultrametric structure of positional notation were recognized, designers could build tree‑oriented data structures, educators could teach number sense via digit‑tree clustering, and cryptographers could exploit the silent base parameter as a security primitive. **Contributions.** 1. [...]
  § 5. Results: The analytical derivations confirm that any base‑$b$ positional system carries a canonical $b$‑adic valuation and an associated ultrametric distance satisfying all metric axioms. The concrete enumeration for decimal integers up to three digits yields exact distance frequencies (Section 4.3). The mean‑distance analysis for two‑digit decimals quantifies the divergence between the ultrametric and the Euclidean line (Section 4.4). These results demonstrate that the digit‑tree hierarchy is mathematically intrinsic, not an artifact of representation.
  § Hypothesis (derived analytically): For the interval $0\le x<y\le99$, the total number of unordered distinct pairs is $4\,950$, of which $450$ share the same last digit (valuation $v_{10}=1$) and the remaining $4\,500$ have valuation $0$; the ratio of the ultrametric mean distance $\bar d_{10}=101/110\approx0.918$ to the normalized Euclidean mean $\bar d_{\text{Euc}}=101/297\approx0.340$ equals $2.70$.: Open Questions - How does the ultrametric viewpoint interact with floating‑point rounding errors in binary computers? - Can the $b$‑adic ultrametric be leveraged to design more efficient hierarchical data structures (e.g., radix trees) with provable performance guarantees? - What pedagogical strategies best convey the tree‑native nature of numbers to learners accustomed to line‑based intuition?
  § (c) Smallest Next Experiment: A minimal experiment would construct a depth‑3 radix tree (10 × 10 × 10 nodes) and measure the average lookup time for queries based on trailing‑digit similarity versus a flat hash table of the same size. The experiment would falsify the claim if the tree does not outperform the hash table in lookup speed for suffix‑based queries.
  § 8. Conclusion: We have shown that positional notation inherently defines a $b$‑adic valuation and an associated ultrametric distance, providing a mathematically rigorous tree‑native metric for integers. The strong triangle inequality holds for all bases, and exact distance distributions for decimal intervals up to three digits have been enumerated. Analytic computation of mean distances for two‑digit decimals quantifies the divergence from the Euclidean line. Recognizing this intrinsic ultrametric reshapes our understanding of number representation, with implications for education, data structures, and cryptography. Future work should explore algorithmic exploitation of the ultrametric hierarchy and empirical validation in real‑world systems.
[11] QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle | https://papers.qnfo.org/papers/factoring-adelic-complexity-v2
  The silent radix -- the observation that no positional numeral internally specifies its own base -- was previously explored as a cryptographic primitive through Silent Radix Encryption (SRE), a key encapsulation mechanism whose security rests on the hardness of recovering a secret base from public envelope digits. That scheme, while closing the known-plaintext attack vector via digit randomization
  Full text (https://papers.qnfo.org/papers/factoring-adelic-complexity-v2), excerpts of its own sections:
  § 1.1 The Silent Radix and its Cryptographic Implications: In any integer base $b \geq 2$, the digit string "10" denotes the number $b$. Every base, named in its own numeral system, calls itself "base-10." The radix is a silent parameter -- it is never carried by the digit string itself [1, 2]. `[established]` The preceding paper in this series [3] surveyed the cryptographic implications of this ambiguity across three levels: (i) a naive symmetric base-change cipher, (ii) Silent Radix Encryption (SRE), a key encapsulation mechanism with a $2^{128}$-class key space, and (iii) the valuation-theoretic landscape of $p$-adic completions and the idélic ring. That analysis established two central results: 1. **The naive cipher is categorically insecure.** A single known-plaintext pair suffices to recover the secret base via elementary greatest common divisor computation, regardless of radix size. Security cannot be obtained from key entropy alone when the cipher is linear and deterministic. 2. [...]
  § 1.2. Motivation: Why Hidden Modulus?: Standard lattice-based cryptography (Kyber [4], Dilithium) operates over a known modulus $q$ -- typically a power of two or a NIST prime. The adversary knows the algebraic ring in which the lattice is embedded and can apply lattice reduction (BKZ, enumeration) directly. The hidden-modulus approach differs qualitatively: the adversary does not know the modulus $p$. [...]
  § 5.5. Experimental Verification: We implemented a comprehensive computational verification suite (2,200+ lines of Python across four experiment notebooks) to validate every core claim of the N-SRE construction at toy parameter scales. The full notebooks are available in the project repository. **HM-LWE Construction and Theorem 1.** Experiments E1-E6 of `hm-lwe-experiments.py` confirm: - Sample generation correctness for $p$ up to 32 bits - Theorem 1: known-$p$ Gaussian elimination recovers $s$ exactly $\forall t \in \{0,1,2,3,4\}$, with $O(n^3)$ scaling confirmed from $n=4$ (0.04 ms) to $n=128$ (135.7 ms) - Statistical indistinguishability: $\chi_{100}^2 = 81.0$ (not significant) and byte-level Shannon entropy within 0.1% of uniform **Lattice Attack Defeat.** Experiments L1-L6 of `lattice-attack-benchmark.py` confirm: - Noise-free baseline is trivially solvable (motivates noise injection) - GCD-based $p$-recovery rate: 1.00 at $t=0$, 0.07 at $t=1$, **0.00 at $t\geq 2$** (noise defeats GCD) - At $t=4$ with $p\sim 2^{20}$: archimedean noise $\approx 2^{80}$ (ENORMOUS — drowns lattice) vs. [...]
  § 7.1. Summary: This paper has advanced the hidden-radix cryptography program from a comparative analysis to a constructive, experimentally verified scheme. The key insight -- that noise injected in the $p$-adic metric provides security that lattice reduction in the archimedean metric cannot defeat -- yields N-SRE-LWE, a KEM with plausible post-quantum security at the cost of moderate ciphertext expansion. The security argument rests on four pillars: 1. **Reduction to standard LWE when the modulus is known** (Theorem 1), placing HM-LWE in the same hardness class as lattice cryptography -- verified experimentally via Gaussian elimination at $n$ from 4 to 128. 2. **Lattice reduction defeat via ultrametric noise** (Section 5.2), exploiting the mismatch between archimedean lattice algorithms and $p$-adic error structure -- confirmed experimentally: archimedean noise $\approx 2^{80}$ vs. ultrametric noise $p^{-4}\approx 2^{-80}$ at $t=4$. 3. **Grover resistance via 512-bit hidden modulus** (Section 5.3), achieving $2^{128}$ post-quantum security. 4. [...]
[12] QNFO: Functoriality as a Transform: Register and Gate-Cost Analysis of a Langlands-Structured Adelic Quantum Register | https://papers.qnfo.org/papers/functoriality-as-a-transform-register-and-gate-cost-analysis-of-a-langlands-stru
  Computing with automorphic representations is bottlenecked by the absence of a fast algorithm for non-abelian harmonic analysis: for the abelian group $\mathrm{GL}(1)$ the Fast Fourier Transform decomposes functions into irreducible characters in $O(n \log n)$ operations, while for $G(\mathbb{Q})\backslash G(\mathbb{A})$ the corresponding decomposition — the Langlands program — has no known fast a
  Full text (https://papers.qnfo.org/papers/functoriality-as-a-transform-register-and-gate-cost-analysis-of-a-langlands-stru), excerpts of its own sections:
  § 4.8 Summary of the cost comparison: Collecting Sections 4.4 and 4.7: the structured functoriality transform on $S = \{2,3,5\}$, $k_p = 4$ costs $C_{\mathrm{str}} = 2888$ operations regardless of how many primes' worth of local data it processes simultaneously, while the classical route costs $82$ operations per prime verified, and a dense non-recursive transform on the same register costs $6.561 \times 10^{11}$. The structured-over-dense separation is $\approx 2.27 \times 10^{8}$; the structured-over-naive-classical comparison depends on the number of primes verified and is computed in Section 5.
  § 5. Results: All numbers below are derived in Section 4 with shown arithmetic; none is measured or simulated. | Quantity | Value | Source | |---|---|---| | Register dimension $\dim \mathcal{H}_S$, $S=\{2,3,5\}$, $k_p=4$ | $810{,}000$ | §4.4 | | Structured stage count $C_{\mathrm{str}}$ | $2{,}888$ | §4.4 | | Naive dense baseline $C_{\mathrm{naive}}$ | $6.561 \times 10^{11}$ | §4.4 | | Separation factor $C_{\mathrm{naive}}/C_{\mathrm{str}}$ | $\approx 2.27 \times 10^{8}$ | §4.4 | | Product formula check, $x=6$ | $\prod_v |6|_v = 1$ | §4.1 | | $p$-adic norm $|45/14|_3$ | $1/9$ | §4.1 | | $|\mathrm{GL}(2,\mathbb{F}_7)|$ | $2016$ | §4.2 | | $V(2,10)$; $V(3,5)$ | $3070$; $485$ | §4.3 | | Critical dimension for cubics $D$ | $10$ | §4.5 | | $1024$-point FFT cost | $10{,}240$ operations | §4.6 | | Classical per-prime budget, six primes $\leq 13$ | $82$ operations | §4.7 | **Projected classical crossover.** As a projection with stated assumptions: under the toy budget of Section 4.7 ($2p$ operations per prime verified), the classical route exceeds the structured cost $C_{\mathrm{str}} = 2888$ once the [...]
  § 6. Discussion: The central claim of this paper is deliberately narrow: the register dimensions, gate counts, and baselines are theorems about a toy model, while the statement that the structured transform reproduces Hecke-eigenvalue matches $a_p(E) = a_p(f)$ is a conjecture. The separation factor $2.27 \times 10^{8}$ is a statement about transform structure, not about physics: it compares a radix recursion against a dense baseline on the same register, exactly as the FFT comparison does in [8], and it says nothing about whether the required encodings $\lvert E \rangle$, $\lvert f \rangle$ exist or are efficiently preparable. **Falsification condition.** The conjecture of Section 3.3 is falsified if, for some modular pair $(E, f)$ and some prime set $S$, no unitary $U_p$ on $\mathbb{C}^{p^{k_p}}$ (with $k_p$ fixed by the encoding) maps the encoded local Galois data at $p$ to the encoded local automorphic data at $p$ — concretely, if a brute-force search over unitaries on a small factor (e.g. [...]
  § 8. Conclusion: This paper formalizes a finite adelic toy register in which the local Langlands data at each prime occupies a $\mathbb{C}^{p^{k_p}}$ factor and functoriality is expressed as a tensor product of local unitary transforms. Every object in the model is exactly computable, and the paper computes them: the register dimension $810{,}000$ for $S = \{2,3,5\}$, $k_p = 4$; the structured stage count $2888$; the dense baseline $6.561 \times 10^{11}$; the separation factor $\approx 2.27 \times 10^{8}$; the product-formula and $p$-adic norm identities on $x = 6$ and $45/14$; the group order $|\mathrm{GL}(2,\mathbb{F}_7)| = 2016$; the Bruhat–Tits vertex counts $3070$ and $485$; the critical dimension $D = 10$ for cubic forms; the $10{,}240$-operation FFT anchor; and the $82$-operation classical per-prime budget. [...]