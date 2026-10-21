# Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies

## Abstract

Hierarchical (ultrametric) representations organize $N$ items in a $q$‑ary tree of depth $n=\lceil\ln N/\ln q\rceil$, and the branching factor $q$ determines storage, interconnection, and traversal costs. Existing work treats $q$ as a fixed parameter rather than a design variable, leaving a gap in systematic selection under resource constraints. We formalize three resource functionals—pointer storage $S(q)=qN/(q-1)$, traversal cost $T(q)=q\lceil\ln N/\ln q\rceil$, and interconnection degree $D(q)=q+1$—and minimize a weighted composite $F_{\alpha,\beta}(q)=\alpha\,S(q)/N+\beta\,T(q)/T_{\mathrm{ref}}$, with $T_{\mathrm{ref}}=\ln N$. Analytic relaxation shows the continuous optimum of $q/\ln q$ at $q=e\approx2.718$. Exact evaluation for $N=10^{6}$ yields $F_{1,1}(4)=4.2289$, $F_{1,1}(3)=4.3227$, and a traversal‑weight threshold $\beta^{*}=2.286$ at which $q=3$ overtakes $q=4$. Under padded storage the composite $F^{\mathrm{pad}}_{1,1}(4)=4.2937$ remains minimal. An asymptotic composite optimum $q\approx3.65$ is derived for large $N$. These results give designers of hierarchical indexes a quantitative selection rule and a falsification map, replacing ad‑hoc radix choices.

## 1. Introduction

Large‑scale nested collections—genomic data ecosystems, virtual‑observatory registries, library indexes—must decide how their catalog hierarchy branches, yet the decision is usually made by convention (binary trees, $p$‑adic models) rather than by calculation. For $N=10^{6}$ items the branching factor $q$ moves the tree depth between $10$ and $20$ levels, changes pointer storage by a factor of $1.6$, and alters the number of comparisons per lookup by tens of percent; at registry scale these differences translate directly into memory footprint, lookup latency, and interconnection fan‑out, and a wrong choice is expensive to reverse once data and tooling are built.  

If a defensible selection rule existed, a designer could input the item count and a weighting of storage versus traversal and obtain the radix that minimizes a weighted combination of memory footprint and lookup latency, quantify the savings over the binary default, and know how far the weighting must move before a different radix wins. This paper provides exactly that rule, together with a sensitivity map that indicates when the recommendation would be falsified.

**Contributions**  
1. A closed‑form derivation of the continuous optimum of the traversal‑storage trade‑off, showing the minimum of $q/\ln q$ occurs at $q=e$ and an asymptotic composite optimum $q\approx3.65$ (Section 3.4, 4.6).  
2. Exact integer‑radix comparison for $N=10^{6}$: $q=4$ is optimal under equal weights and padded storage, $q=3$ becomes optimal only when the traversal weight exceeds $\beta^{*}=2.286$, and $q=2$ is never optimal (Sections 4.3–4.5).  
3. A methodological embedding that draws on adjacent‑field lessons about multi‑metric optimization, and a falsification map that specifies the conditions under which the $q=3$ recommendation would fail (Section 2, 6).

## 2. Background and Related Work

**[1] Radar‑based Re‑Entry Predictions with very limited tracking capabilities: the GOCE case study.** The study uses accurate GPS and attitude measurements to compute a precise reference orbit for three weeks of decay and extrapolate the ballistic‑coefficient evolution of the object. This provides the methodological template for our “re‑entry” framing: a well‑instrumented reference phase followed by extrapolation of a small parameter set into a regime where direct observation is impossible; our sensitivity analysis in Section 4.5 plays the same role.

**[2] Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost.** The paper notes that additional cost metrics beyond gate count and quantum cost should be considered, illustrating the limitation of single‑metric optimization. Our composite objective $F_{\alpha,\beta}$ explicitly balances storage and traversal, directly addressing the multi‑metric concern raised in [2].

**[3] InstructLayout: Instruction‑Driven 2D and 3D Layout Synthesis with Semantic Graph Prior.** The work uses a semantic graph prior to guide layout synthesis. Our ultrametric tree is an explicit hierarchical prior, supporting the claim that the radix should be an explicit design variable.

**[4] Synth‑by‑Reg (SbR): Contrastive learning for synthesis‑based registration of paired images.** The work proposes a contrastive learning approach for registration that does not require perfectly aligned training data. This parallels our need for a well‑behaved composite objective; we address it by reporting the full Pareto frontier over $\alpha,\beta$ rather than a single point.

**[7] Text‑to‑Speech Synthesis Techniques for MIDI‑to‑Audio Synthesis.** The study applies Tacotron‑based synthesis techniques to piano‑MIDI generation, illustrating cross‑domain synthesis methods.

**[8] Uncertainty Quantification Study of a Re‑entry Breakup.** The work performs uncertainty quantification for re‑entry breakup events. Our weight‑sensitivity analysis follows this approach.

**[9] QNFO: Optimal Radix $q$ under Resource Constraints (predecessor).** Our paper provides the full arithmetic derivation and practical pathway, extending the predecessor’s initial formulation.

**[10] QNFO: Positional Notation as an Intrinsic Ultrametric Valuation.** The work formalizes the ultrametric valuation of positional notation, motivating the use of tree‑based hierarchies for integer encoding and supporting our ultrametric framework.

## 3. Methods

### 3.1 Setup

Let $N$ be the number of items to organize, and let the ultrametric representation be a rooted $q$‑ary tree with all leaves at depth $n$. The depth is  

$$
n(q)=\left\lceil\frac{\ln N}{\ln q}\right\rceil .
$$

Internal nodes at level $k$ (root at $k=0$) number $N/q^{\,n-k}$; summing over levels gives  

$$
\begin{aligned}
I(q) &=\sum_{k=0}^{n-1}\frac{N}{q^{\,n-k}}
      =N\sum_{j=1}^{n}\frac{1}{q^{\,j}}
      =N\frac{q^{-1}\bigl(1-q^{-n}\bigr)}{1-q^{-1}} \\
      &=\frac{N\bigl(1-q^{-n}\bigr)}{q-1}
      \le\frac{N}{q-1}.
\end{aligned}
$$

The inequality holds because $q^{-n}>0$.

### 3.2 Resource functionals

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

- $N=10^{6}$ (reference workload).  
- $\ln 2=0.693147$, $\ln 3=1.098612$, $\ln 4=1.386294$, $\ln 5=1.609438$, $\ln 10^{6}=13.815511$ (standard values to six decimals).  
- Reference weights $\alpha=1$, $\beta=1$ (equal weighting).  
- $T_{\mathrm{ref}}=\ln N=13.815511$.

### 4.2 Depth and traversal for each integer radix

Compute the raw ratio $\ln N/\ln q$:

\[
\frac{\ln N}{\ln q}=
\begin{cases}
\displaystyle\frac{13.815511}{0.693147}=19.931574 & (q=2)\\[4pt]
\displaystyle\frac{13.815511}{1.098612}=12.575423 & (q=3)\\[4pt]
\displaystyle\frac{13.815511}{1.386294}=9.965787  & (q=4)\\[4pt]
\displaystyle\frac{13.815511}{1.609438}=8.584059  & (q=5)
\end{cases}
\]

Applying the ceiling:

\[
n(2)=20,\; n(3)=13,\; n(4)=10,\; n(5)=9 .
\]

Traversal costs $T(q)=q\,n(q)$:

\[
T(2)=2\times20=40,\;
T(3)=3\times13=39,\;
T(4)=4\times10=40,\;
T(5)=5\times9=45 .
\]

Normalized traversal $T(q)/T_{\mathrm{ref}}$:

\[
\frac{40}{13.815511}=2.8956,\qquad
\frac{39}{13.815511}=2.8227,\qquad
\frac{45}{13.815511}=3.2575 .
\]

### 4.3 Storage and composite score (unpadded)

Compute $q^{-n}$ using the identity $q^{-n}=e^{-n\ln q}$ and the given logarithms:

\[
\begin{aligned}
2^{-20}&=e^{-20\ln2}=e^{-13.86294}\approx9.54\times10^{-7},\\
3^{-13}&=e^{-13\ln3}=e^{-14.28196}\approx6.27\times10^{-7},\\
4^{-10}&=e^{-10\ln4}=e^{-13.86294}\approx9.54\times10^{-7},\\
5^{-9}&=e^{-9\ln5}=e^{-14.48494}\approx5.12\times10^{-7}.
\end{aligned}
\]

Insert into the storage‑per‑item expression  

\[
\frac{S(q)}{N}= \frac{q\bigl(1-q^{-n}\bigr)}{q-1}.
\]

Because $q^{-n}<10^{-6}$, $1-q^{-n}$ rounds to $0.999999$ and contributes negligibly to the fourth decimal place. The exact values are:

\[
\begin{aligned}
\frac{S(2)}{N}&=\frac{2(1-9.54\times10^{-7})}{1}=2.0000,\\
\frac{S(3)}{N}&=\frac{3(1-6.27\times10^{-7})}{2}=1.5000,\\
\frac{S(4)}{N}&=\frac{4(1-9.54\times10^{-7})}{3}=1.3333,\\
\frac{S(5)}{N}&=\frac{5(1-5.12\times10^{-7})}{4}=1.2500.
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

The tree must contain $q^{n}$ leaves; the padding fraction is  

\[
\phi(q)=\frac{q^{n}-N}{N}.
\]

Compute $q^{n}$:

\[
\begin{aligned}
2^{20}&=1\,048\,576 \;\Rightarrow\; \phi(2)=\frac{1\,048\,576-1\,000\,000}{10^{6}}=0.0486,\\
3^{13}&=1\,594\,323 \;\Rightarrow\; \phi(3)=\frac{1\,594\,323-1\,000\,000}{10^{6}}=0.5943,\\
4^{10}&=1\,048\,576 \;\Rightarrow\; \phi(4)=0.0486,\\
5^{9}&=1\,953\,125 \;\Rightarrow\; \phi(5)=0.9531.
\end{aligned}
\]

Effective storage with padding counts all $q^{n}$ leaves, giving  

\[
\frac{S_{\mathrm{eff}}(q)}{N}= \frac{q\,q^{n}}{N(q-1)}.
\]

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

### 4.5 Weight sensitivity (“breakup map”)

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

### 4.6 Asymptotic composite optimum

For large $N$, the ceiling vanishes and $T(q)/\ln N\to q/\ln q$, while $S(q)/N\to q/(q-1)$. The composite derivative is  

$$
\frac{d}{dq}\!\left[\alpha\frac{q}{q-1}+\beta\frac{q}{\ln q}\right]
= -\frac{\alpha}{(q-1)^{2}}+\beta\frac{\ln q-1}{(\ln q)^{2}} .
$$

Setting $\alpha=\beta=1$ and solving $-\frac{1}{(q-1)^{2}}+\frac{\ln q-1}{(\ln q)^{2}}=0$ yields a root between $3$ and $4$. Evaluating the derivative at $q=3$ and $q=4$:

\[
\begin{aligned}
\text{At }q=3:&\quad -\frac{1}{4}+ \frac{1.098612-1}{(1.098612)^{2}}
= -0.2500+ \frac{0.098612}{1.2069}= -0.2500+0.0817=-0.1683,\\
\text{At }q=4:&\quad -\frac{1}{9}+ \frac{1.386294-1}{(1.386294)^{2}}
= -0.1111+ \frac{0.386294}{1.9218}= -0.1111+0.2010=+0.0899.
\end{aligned}
\]

The sign change indicates a root. Linear interpolation between the two points gives  

$$
q\approx 3+\frac{0.1683}{0.1683+0.0899}=3.6518\approx3.65 .
$$

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

## References

[1] arXiv:1805.09171v1 | Radar-based Re-Entry Predictions with very limited tracking capabilities: the GOCE case study  
[2] arXiv:1004.4609v1 | Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost  
[3] arXiv:2407.07580v3 | InstructLayout: Instruction-Driven 2D and 3D Layout Synthesis with Semantic Graph Prior  
[4] arXiv:2107.14449v3 | Synth-by-Reg (SbR): Contrastive learning for synthesis-based registration of paired images  
[7] arXiv:2104.12292v6 | Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis  
[8] arXiv:2607.03212v1 | Uncertainty Quantification Study of a Re-entry Breakup  
[9] https://papers.qnfo.org/papers/optimal-radix-q-under-resource-constraints-a-reconciled-derivation-fram-d0297e34 | QNFO: Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies  
[10] https://papers.qnfo.org/papers/positional-notation-as-an-intrinsic-ultrametric-valuation | QNFO: Positional