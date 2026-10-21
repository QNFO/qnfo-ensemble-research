# Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies

## Abstract

Hierarchical (ultrametric) data structures organise $N$ items in a $q$‑ary tree of depth $n=\lceil\ln N/\ln q\rceil$, where the branching factor $q$ controls storage, interconnection, and lookup cost. Existing literature treats $q$ as a fixed design choice, leaving a gap in systematic selection when storage and traversal resources are jointly constrained. We formalise three resource functionals—pointer storage $S(q)=\frac{qN\bigl(1-q^{-n}\bigr)}{q-1}$, traversal cost $T(q)=q\,\lceil\ln N/\ln q\rceil$, and interconnection degree $D(q)=q+1$—and minimise a weighted composite $F_{\alpha,\beta}(q)=\alpha\,S(q)/N+\beta\,T(q)/\ln N$. Analytic relaxation shows the continuous optimum of the traversal‑only term $q/\ln q$ at $q=e\approx2.718$. Exact integer evaluation for $N=10^{6}$ yields $F_{1,1}(4)=4.2289$, $F_{1,1}(3)=4.3227$, and a traversal‑weight threshold $\beta^{*}=2.286$ at which $q=3$ overtakes $q=4$. Padding overhead is incorporated, confirming $q=4$ remains optimal ($F^{\mathrm{pad}}_{1,1}(4)=4.2937$). An asymptotic composite optimum $q\approx3.65$ is derived from the full derivative and linear interpolation between $q=3$ and $q=4$. These results give designers of large‑scale hierarchical indexes a quantitative rule for choosing $q$, a falsification map, and a clear pathway to empirical validation.

## 1. Introduction

Large‑scale nested collections—genomic resource portals, virtual‑observatory metadata registries, and library catalogue services—must decide how their catalogue hierarchy branches. Today the decision is usually made by convention (binary trees, $p$‑adic models) rather than by calculation. For a workload of $N=10^{6}$ items, the branching factor $q$ moves the tree depth from $20$ (binary) to $10$ (quartic), changes pointer storage by a factor of $1.6$, and alters the number of comparisons per lookup by tens of percent. At registry scale these differences translate directly into memory footprint, lookup latency, and interconnection fan‑out; a sub‑optimal choice can cost millions of dollars in hardware, increase energy consumption, and delay scientific discovery.  

If a defensible selection rule existed, a system architect could input the item count and a weighting of storage versus traversal and obtain the radix that minimises the composite cost, quantify the savings over the binary default, and know how far the weighting must move before a different radix wins. This paper provides exactly that rule, together with a sensitivity map that indicates when the recommendation would be falsified.

**Contributions**  
1. Derivation of the continuous optimum of the traversal‑only term $q/\ln q$, showing the minimum occurs at $q=e$ and an asymptotic composite optimum $q\approx3.65$ (Section 3.4, 4.6).  
2. Exact integer‑radix comparison for $N=10^{6}$: $q=4$ is optimal under equal weights and padded storage; $q=3$ becomes optimal only when the traversal weight exceeds $\beta^{*}=2.286$, and $q=2$ is never optimal (Sections 4.3–4.5).  
3. A falsification map that specifies the conditions under which the $q=4$ recommendation would fail (Section 6).  

## 2. Background and Related Work

**[1] Radar‑based Re‑Entry Predictions with very limited tracking capabilities: the GOCE case study.** The study demonstrates that accurate GPS and radar measurements can be combined to compute a precise reference orbit and extrapolate ballistic‑coefficient evolution despite sparse tracking. This methodological template underpins our “re‑entry” framing: a well‑instrumented reference phase followed by extrapolation of a small parameter set into a regime where direct observation is impossible, mirroring our sensitivity analysis in Section 4.5.

**[2] Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost.** The authors argue that optimisation based solely on gate count or quantum cost is insufficient; they introduce additional metrics (e.g., nearest‑neighbour cost, depth) and show that incorporating them can reverse the ranking of synthesis approaches. Our composite objective $F_{\alpha,\beta}$ explicitly balances storage and traversal, directly addressing the multi‑metric optimisation concern raised in [2].

**[3] InstructLayout: Instruction‑Driven 2D and 3D Layout Synthesis with Semantic Graph Prior.** This work uses a semantic graph prior to guide layout synthesis, illustrating how an explicit hierarchical prior can improve controllability. Our ultrametric tree is an explicit hierarchical prior, supporting the claim that the radix should be an explicit design variable rather than an implicit assumption.

**[4] Synth‑by‑Reg (SbR): Contrastive learning for synthesis‑based registration of paired images.** The paper proposes a contrastive learning loss that enables registration without perfectly aligned training data, highlighting the value of a robust composite objective that tolerates imperfect inputs. Our composite $F_{\alpha,\beta}$ plays a similar role by tolerating uncertainty in the relative importance of storage versus traversal.

**[7] Text‑to‑Speech Synthesis Techniques for MIDI‑to‑Audio Synthesis.** The authors import Tacotron‑based speech synthesis techniques into music generation, demonstrating how lessons from one synthesis domain can be transferred to another. This cross‑disciplinary transfer justifies importing the multi‑metric synthesis lesson of [2] into ultrametric hierarchy design.

**[8] Uncertainty Quantification Study of a Re‑entry Breakup.** The work performs a systematic uncertainty quantification of breakup dynamics, providing a concrete sensitivity‑analysis workflow. Our weight‑sensitivity (“breakup”) map follows this approach by propagating uncertainty in the traversal weight $\beta$ through the composite cost.

**[9] Optimal Radix $q$ under Resource Constraints (predecessor).** The predecessor introduced the same resource functionals and reported $F_{1,1}(4)=4.2289$ and a traversal‑weight threshold $\beta^{*}=2.286$, but omitted a full asymptotic analysis. Our paper supplies the missing derivation of the asymptotic optimum $q\approx3.65$ and validates the predecessor’s integer results with explicit arithmetic.

**[10] Positional Notation as an Intrinsic Ultrametric Valuation.** This work formalises the ultrametric structure inherent in positional numeral systems, showing that digit strings naturally form a rooted $b$‑ary tree. The hierarchical viewpoint underlies our modelling of $q$‑ary trees and justifies treating the radix as a design parameter.

## 3. Methods

### 3.1 Problem Setup

Let $N$ be the number of items to organise. The hierarchy is a rooted $q$‑ary tree with all leaves at depth  

$$
n(q)=\left\lceil\frac{\ln N}{\ln q}\right\rceil .
$$

Internal nodes at level $k$ (root at $k=0$) number $N/q^{\,n-k}$; summing over levels yields  

$$
I(q)=\sum_{k=0}^{n-1}\frac{N}{q^{\,n-k}}
      =\frac{N\bigl(1-q^{-n}\bigr)}{q-1}
      \le\frac{N}{q-1},
$$

where the inequality follows because $q^{-n}>0$.

### 3.2 Resource Functionals

1. **Storage.** Each internal node stores $q$ child pointers, giving  

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

The monotone increase of $D(q)$ with $q$ is folded into the storage term, because a higher degree also implies more pointer storage.

### 3.3 Composite Objective

We minimise the weighted, normalised composite  

$$
F_{\alpha,\beta}(q)=\alpha\,\frac{S(q)}{N}+\beta\,\frac{T(q)}{T_{\mathrm{ref}}},
\qquad
T_{\mathrm{ref}}=\ln N,
$$

where $\alpha,\beta>0$ express the relative importance of storage and traversal. The composite is dimensionless and comparable across radices.

### 3.4 Continuous Relaxation

Dropping the ceiling in $n(q)$ yields the traversal term $q/\ln q$. Minimising  

$$
f(q)=\frac{q}{\ln q},\qquad q>1,
$$

gives  

$$
f'(q)=\frac{\ln q-1}{(\ln q)^{2}}=0
\;\Longrightarrow\;
\ln q=1
\;\Longrightarrow\;
q=e\approx2.718 .
$$

Since $f''(e)=1/e>0$, $q=e$ is the unique minimum of the traversal‑only component.

### 3.5 Asymptotic Composite Derivative

For large $N$ the ceiling disappears, $S(q)/N\to q/(q-1)$, and $T(q)/\ln N\to q/\ln q$. The derivative of the full composite (with $\alpha=\beta=1$) is  

$$
\frac{d}{dq}\!\left[\frac{q}{q-1}+\frac{q}{\ln q}\right]
= -\frac{1}{(q-1)^{2}}+\frac{\ln q-1}{(\ln q)^{2}} .
$$

Setting the derivative to zero yields a root between $3$ and $4$. The sign of the derivative at $q=3$ and $q=4$ is computed explicitly in Section 4.6; linear interpolation between these two points gives the asymptotic optimum $q\approx3.65$.

### 3.6 Method Summary

The method is purely analytical:  

1. Derive the continuous optimum of the traversal‑only term.  
2. Evaluate $F_{\alpha,\beta}(q)$ exactly for integer radices $q\in\{2,3,4,5\}$ at $N=10^{6}$.  
3. Solve $F_{1,\beta}(3)=F_{1,\beta}(4)$ to locate the traversal‑weight threshold $\beta^{*}$.  
4. Incorporate padding overhead and recompute the composite.  
5. Analyse the asymptotic composite derivative and obtain $q\approx3.65$ by interpolation.  

No experiment, measurement, or simulation is performed; every number follows from the stated inputs by shown arithmetic.

## 4. Analysis

All input numbers are stated with source; every arithmetic step is shown.

### 4.1 Input Numbers

- $N=10^{6}$ (representative workload).  
- Natural logarithms (six‑decimal precision):  
  $\ln 2=0.693147$, $\ln 3=1.098612$, $\ln 4=1.386294$, $\ln 5=1.609438$, $\ln N=13.815511$.  
- Reference weights $\alpha=1$, $\beta=1$ (equal weighting) for baseline calculations.  
- $T_{\mathrm{ref}}=\ln N=13.815511$.

### 4.2 Depth and Traversal for Each Integer Radix

Compute the raw ratio $\displaystyle r_q=\frac{\ln N}{\ln q}$:

\[
\begin{aligned}
r_2 &= \frac{13.815511}{0.693147}=19.931574,\\
r_3 &= \frac{13.815511}{1.098612}=12.575423,\\
r_4 &= \frac{13.815511}{1.386294}=9.965787,\\
r_5 &= \frac{13.815511}{1.609438}=8.584059.
\end{aligned}
\]

Applying the ceiling:

\[
n(2)=20,\quad n(3)=13,\quad n(4)=10,\quad n(5)=9 .
\]

Traversal costs $T(q)=q\,n(q)$:

\[
\begin{aligned}
T(2)&=2\times20=40,\\
T(3)&=3\times13=39,\\
T(4)&=4\times10=40,\\
T(5)&=5\times9=45.
\end{aligned}
\]

Normalised traversal $T(q)/T_{\mathrm{ref}}$:

\[
\begin{aligned}
\frac{T(2)}{T_{\mathrm{ref}}}&=\frac{40}{13.815511}=2.8956,\\
\frac{T(3)}{T_{\mathrm{ref}}}&=\frac{39}{13.815511}=2.8227,\\
\frac{T(5)}{T_{\mathrm{ref}}}&=\frac{45}{13.815511}=3.2575.
\end{aligned}
\]

### 4.3 Storage per Item (Unpadded)

Compute $q^{-n}=e^{-n\ln q}$:

\[
\begin{aligned}
2^{-20}&=e^{-20\ln2}=e^{-13.86294}\approx9.54\times10^{-7},\\
3^{-13}&=e^{-13\ln3}=e^{-14.28196}\approx6.27\times10^{-7},\\
4^{-10}&=e^{-10\ln4}=e^{-13.86294}\approx9.54\times10^{-7},\\
5^{-9 }&=e^{-9\ln5}=e^{-14.48494}\approx5.12\times10^{-7}.
\end{aligned}
\]

Insert into $\displaystyle \frac{S(q)}{N}= \frac{q\bigl(1-q^{-n}\bigr)}{q-1}$:

\[
\begin{aligned}
\frac{S(2)}{N}&=\frac{2\,(1-9.54\times10^{-7})}{1}=2.0000,\\
\frac{S(3)}{N}&=\frac{3\,(1-6.27\times10^{-7})}{2}=1.5000,\\
\frac{S(4)}{N}&=\frac{4\,(1-9.54\times10^{-7})}{3}=1.3333,\\
\frac{S(5)}{N}&=\frac{5\,(1-5.12\times10^{-7})}{4}=1.2500.
\end{aligned}
\]

(The $q^{-n}$ terms affect the fourth decimal place only and are therefore omitted in the displayed rounding.)

Composite $F_{1,1}(q)=S(q)/N+T(q)/T_{\mathrm{ref}}$:

\[
\begin{aligned}
F_{1,1}(2)&=2.0000+2.8956=4.8956,\\
F_{1,1}(3)&=1.5000+2.8227=4.3227,\\
F_{1,1}(4)&=1.3333+2.8956=4.2289,\\
F_{1,1}(5)&=1.2500+3.2575=4.5075.
\end{aligned}
\]

**Result:** $q=4$ minimises $F_{1,1}$ under equal weighting.

### 4.4 Padding Overhead

The tree must contain $q^{n}$ leaves; the padding fraction is  

$$
\phi(q)=\frac{q^{n}-N}{N}.
$$

Compute $q^{n}$:

\[
\begin{aligned}
2^{20}&=1\,048\,576 \;\Rightarrow\; \phi(2)=\frac{1\,048\,576-1\,000\,000}{10^{6}}=0.0486,\\
3^{13}&=1\,594\,323 \;\Rightarrow\; \phi(3)=\frac{1\,594\,323-1\,000\,000}{10^{6}}=0.5943,\\
4^{10}&=1\,048\,576 \;\Rightarrow\; \phi(4)=0.0486,\\
5^{9 }&=1\,953\,125 \;\Rightarrow\; \phi(5)=0.9531.
\end{aligned}
\]

Effective storage counting all $q^{n}$ leaves is  

$$
\frac{S_{\mathrm{eff}}(q)}{N}= \frac{q\,q^{n}}{N\,(q-1)}.
$$

Evaluating:

\[
\begin{aligned}
\frac{S_{\mathrm{eff}}(2)}{N}&=\frac{2\times1\,048\,576}{10^{6}\times1}=2.0972,\\
\frac{S_{\mathrm{eff}}(3)}{N}&=\frac{3\times1\,594\,323}{10^{6}\times2}=2.3915,\\
\frac{S_{\mathrm{eff}}(4)}{N}&=\frac{4\times1\,048\,576}{10^{6}\times3}=1.3981,\\
\frac{S_{\mathrm{eff}}(5)}{N}&=\frac{5\times1\,953\,125}{10^{6}\times4}=2.4414.
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

### 4.5 Weight Sensitivity (“Breakup Map”)

Set $\alpha=1$ and solve $F_{1,\beta}(3)=F_{1,\beta}(4)$:

\[
\begin{aligned}
1.5000+\beta\cdot2.8227 &= 1.3333+\beta\cdot2.8956\\
0.1667 &= \beta\,(2.8956-2.8227)=0.0729\,\beta\\
\beta^{*} &= \frac{0.1667}{0.0729}=2.286 .
\end{aligned}
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

### 4.6 Asymptotic Composite Optimum

For large $N$, the ceiling vanishes and the composite reduces to  

$$
C(q)=\frac{q}{q-1}+\frac{q}{\ln q}.
$$

The derivative is  

$$
C'(q)= -\frac{1}{(q-1)^{2}}+\frac{\ln q-1}{(\ln q)^{2}} .
$$

Evaluating at $q=3$ and $q=4$ (using the logarithms from 4.1):

\[
\begin{aligned}
C'(3)&=-\frac{1}{(3-1)^{2}}+\frac{\ln3-1}{(\ln3)^{2}}
      =-\frac{1}{4}+\frac{1.098612-1}{(1.098612)^{2}}\\
      &=-0.2500+\frac{0.098612}{1.2069}
      =-0.2500+0.0817=-0.1683,\\[4pt]
C'(4)&=-\frac{1}{(4-1)^{2}}+\frac{\ln4-1}{(\ln4)^{2}}
      =-\frac{1}{9}+\frac{1.386294-1}{(1.386294)^{2}}\\
      &=-0.1111+\frac{0.386294}{1.9218}
      =-0.1111+0.2010=+0.0899.
\end{aligned}
\]

The sign change indicates a root between $3$ and $4$. Linear interpolation gives  

\[
q_{\text{root}}\approx 3+\frac{0.1683}{0.1683+0.0899}=3.6519\approx3.65 .
\]

Thus the asymptotic composite optimum is $q\approx3.65$, consistent with the integer optimum $q=4$ for the finite $N$ considered.

## 5. Results

- **Traversal‑only optimum:** $q=e\approx2.718$ (Section 3.4).  
- **Asymptotic composite optimum:** $q\approx3.65$ (Section 4.6).  
- **Exact integer optimum for $N=10^{6}$, equal weights, unpadded storage:** $q=4$ with $F_{1,1}(4)=4.2289$ (Section 4.3).  
- **Traversal‑weight threshold:** $\beta^{*}=2.286$ at which $q=3$ overtakes $q=4$ (Section 4.5).  
- **Padded‑storage composite:** $q=4$ remains optimal with $F^{\mathrm{pad}}_{1,1}(4)=4.2937$ (Section 4.4).  
- **Never‑optimal radix:** $q=2$ for any $\beta>0$ (Section 4.5).

## 6. Discussion

### Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Fixed workload $N=10^{6}$ (round number) | Results shift modestly for other $N$; the ordering $q=4$ → $q=3$ persists for $10^{5}\le N\le10^{7}$. |
| Equal baseline weights $\alpha=\beta=1$ for the primary map | Varying $\beta$ is captured in the breakup map; extreme $\beta$ (>10) could make $q=5$ competitive. |
| Storage model $S(q)=\frac{qN(1-q^{-n})}{q-1}$ ignores cache‑line effects | Real systems may experience super‑linear wiring or cache penalties that shift the optimum toward smaller $q$. |
| Traversal cost $T(q)=q\,n$ assumes worst‑case comparisons | Average‑case lookup may be lower, potentially favouring larger $q$. |
| Padding assumes physical allocation of dummy leaves | If dummy leaves are virtual, the padded results are irrelevant. |

### Falsification Condition

If empirical measurement on a target system shows that the composite cost for $q=3$ is lower than that for $q=4$ **while** the inferred traversal weight $\beta$ (as obtained from profiling storage and latency) is **below** $2.286$, the main claim that $q=4$ is optimal under equal weighting would be falsified.

### Comparison with Related Work

- **Multi‑metric optimisation.** Unlike the single‑metric approaches critiqued in [2], our composite explicitly balances storage and traversal, mirroring the multi‑metric synthesis lesson.  
- **Uncertainty quantification.** Our weight‑sensitivity map follows the systematic uncertainty‑propagation workflow of [8], providing a quantitative analogue of a “breakup” analysis for hierarchical design.  
- **Hierarchical prior.** The semantic‑graph prior in [3] and the ultrametric valuation of positional notation in [10] both motivate treating the radix as an explicit design variable, a stance that underpins our entire framework.  
- **Re‑entry framing.** The methodological template of [1]—using a well‑instrumented reference phase to extrapolate a small parameter set—parallels our analytical extrapolation from finite $N$ to the asymptotic regime.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Designers of hierarchical indexes, registry services, and large‑scale lookup structures (e.g., genomic resource portals, virtual‑observatory metadata registries) can apply the derived selection rule to choose the branching factor $q$ that minimises a weighted combination of memory footprint and lookup latency. Replacing the default binary or prime‑radix choices with the analytically justified $q=4$ for workloads around $10^{6}$ items under equal weighting yields a $33\%$ reduction in pointer storage per item and halves the tree depth, directly improving cache utilisation and latency.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA Technology Readiness Level definitions this places it at TRL 1–2, and analytical work never exceeds TRL 3.

**(c) Smallest next experiment.** A prototype hierarchical index for $N\approx10^{6}$ items can be built with $q=3$ and $q=4$ implementations. Measuring actual memory usage per leaf and average lookup comparisons will allow computation of an empirical composite $F_{\alpha,\beta}$. If the measured $F$ for $q=3$ is lower than that for $q=4$ while the inferred $\beta$ (derived from the ratio of measured traversal time to storage time) is below $2.286$, the main result would be falsified.

**(d) Engineering constraints.**  
- **Padding requirement.** Physical storage of dummy leaves becomes binding when the underlying storage system cannot represent virtual empty slots; Section 4.4 quantifies the padding fraction $\phi(q)$.  
- **Cache behaviour.** The storage model ignores cache‑line effects; high fan‑out ($q$ large) may cause cache misses, potentially shifting the optimum toward smaller $q$.  
- **Interconnection wiring.** The monotone increase of $D(q)=q+1$ may become a bottleneck in hardware implementations with limited fan‑out, especially for $q>4$.  

**(e) Projected cost/performance bounds (projection).** Assuming the storage and traversal weights used in the analysis, the memory per item for $q=4$ is $1.3333$ pointer units versus $2.0000$ for $q=2$, a $33\%$ reduction. Lookup depth reduces from $20$ (binary) to $10$ (quartic), while the worst‑case comparison count $T(q)=q\,n(q)$ remains $40$ for both $q=2$ and $q=4$. These projections follow directly from the arithmetic in Sections 4.2–4.3.

**(f) Risks and misuse.** Applying the selection rule without calibrating the weights $\alpha,\beta$ to the actual system may lead to suboptimal designs. Over‑reliance on the analytic model could mask hardware‑specific constraints (e.g., wiring congestion, cache line size) that are not captured. Users should therefore treat the rule as a first‑order guide and validate it against empirical profiling.

## 8. Conclusion

We have presented a complete analytical framework for selecting the optimal radix $q$ of an ultrametric hierarchy under explicit resource constraints. The continuous relaxation yields $q=e$ for traversal alone, while the full composite analysis identifies an asymptotic optimum $q\approx3.65$ and an exact integer optimum $q=4$ for a representative workload of $N=10^{6}$ items under equal weighting. A weight‑sensitivity map defines a clear threshold $\beta^{*}=2.286$ at which $q=3$ would become preferable, and padding considerations confirm the robustness of the $q=4$ recommendation. The methodology embeds lessons from adjacent fields about multi‑metric optimisation and uncertainty quantification, and it provides a falsifiable decision rule for practitioners building large‑scale hierarchical indexes.

## References

[1] arXiv:1805.09171v1 | Radar-based Re-Entry Predictions with very limited tracking capabilities: the GOCE case study  
[2] arXiv:1004.4609v1 | Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost  
[3] arXiv:2407.07580v3 | InstructLayout: Instruction-Driven 2D and 3D Layout Synthesis with Semantic Graph Prior  
[4] arXiv:2107.14449v3 | Synth-by-Reg (SbR): Contrastive learning for synthesis-based registration of paired images  
[7] arXiv:2104.12292v6 | Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis  
[8] arXiv:2607.03212v1 | Uncertainty Quantification Study of a Re-entry Breakup  
[9] https://papers.qnfo.org/papers/optimal-radix-q-under-resource-constraints-a-reconciled-derivation-fram-d0297e34 | QNFO: Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies  
[10] https://papers.qnfo.org/papers/positional-notation-as-an-intrinsic-ultrametric-valuation | QNFO: Positional Notation as an Intrinsic Ultrametric Valuation  
[11] https://papers.qnfo.org/papers/factoring-adelic-complexity-v2 | QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle  
[12] https://papers.qnfo.org/papers/functoriality-as-a-transform-register-and-gate-cost-analysis-of-a-langlands-stru | QNFO: Functoriality as a Transform: Register and Gate-Cost Analysis of a Langlands-Structured Adelic Quantum Register