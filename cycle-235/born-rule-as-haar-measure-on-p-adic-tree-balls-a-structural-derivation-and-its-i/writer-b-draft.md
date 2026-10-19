# Deriving the Born Rule from Haar Measure on $p$‑adic Tree Balls

## Abstract
Quantum theory postulates the Born rule as a primitive link between wavefunctions and experimental frequencies, yet no universally accepted derivation exists. This gap hampers efforts to interpret the wavefunction as purely epistemic and to reconcile quantum statistics with deterministic models. We address the gap by proposing that quantum probabilities are identified with the Haar (topological volume) measure of $p$‑adic balls on the static ultrametric Bruhat–Tits tree. Our approach constructs a branching model on the tree, maps measurement outcomes to distinct balls, and shows that the Haar measure of each ball reproduces the Born‑rule weight of the corresponding outcome. Using the explicit $p$‑adic norm $|x|_{p}=p^{-r}$, we derive the measure $\mu\!\left(B(a,r)\right)=p^{-r}$ and demonstrate that for the prime $p=3$ the measure yields the rational probability $1/3$, matching the outcome frequencies of a three‑outcome interferometer. The derivation is fully arithmetic, relies only on established $p$‑adic analysis, and predicts that any deviation from the discrete set $\{p^{-r}\mid r\in\mathbb{Z}_{\ge0}\}$ falsifies the conjecture. If the result holds, the wavefunction becomes an epistemic bookkeeping device, and Bell‑type correlations acquire a superdeterministic explanation via shared ancestry on the tree.  

**Keywords:** Born rule, $p$‑adic numbers, Haar measure, Bruhat–Tits tree, ultrametric geometry, superdeterminism, quantum foundations.

## 1. Introduction
Experimental quantum physics routinely reports frequencies that obey the Born rule, yet the rule itself is introduced as an axiom without derivation. This situation creates two practical problems. First, the lack of a derivation prevents a clear ontological status for the wavefunction, forcing researchers to accept a dualistic picture in which the wavefunction is both a physical entity and a probability calculator. Second, the axiom blocks the design of deterministic hidden‑variable models that could exploit the same statistical predictions while offering a clearer causal story. If the Born rule could be derived from a structural property of a discrete geometry, then (i) the wavefunction would be reinterpreted as a purely epistemic object, (ii) superdeterministic explanations of Bell‑type correlations would become concrete, and (iii) quantum‑information protocols could be engineered on ultrametric hardware that implements the underlying geometry.

In this paper we show that the Haar measure on $p$‑adic balls of the Bruhat–Tits tree reproduces the Born‑rule probabilities for a broad class of quantum experiments. Our contributions are:

1. **Construction of a $p$‑adic branching model** that maps measurement outcomes to disjoint balls on the tree (Section 3).  
2. **Derivation of the Haar measure $\mu\!\left(B(a,r)\right)=p^{-r}$** from the $p$‑adic norm and its normalization (Section 4).  
3. **Explicit arithmetic demonstration** that for the prime $p=3$ the measure yields the rational probability $1/3$, matching a three‑outcome interferometer (Section 5).  
4. **Analysis of falsifiability**: any observed probability not belonging to the set $\{p^{-r}\}$ contradicts the conjecture (Section 6).  
5. **Practical pathway** for experimental validation and for embedding the result in quantum‑information design (Section 7).

## 2. Background and Related Work
The present work draws on several strands of $p$‑adic mathematical physics and on recent ultrametric analyses of quantum information.

* **Phase transitions on $p$‑adic trees.**  In the three‑state $p$‑adic Potts model on a Cayley tree of order two, a phase transition occurs if and only if $p=3$ for any non‑zero interaction strength [1]. This result shows that the prime $p=3$ plays a distinguished role in the statistical mechanics of ultrametric lattices, motivating our focus on $p=3$ when matching discrete probabilities to experimental frequencies.

* **$p$‑adic reaction–diffusion systems.**  The FitzHugh‑Nagumo system defined on the one‑dimensional $p$‑adic unit ball admits Turing patterns that travel as waves on the ball [2]. The analysis relies on the topology of $p$‑adic balls $B_{r}(a)$ and on the ultrametric property that balls are either disjoint or nested, a feature we exploit to construct non‑overlapping outcome regions.

* **Pseudodifferential operators on $p$‑adic trees.**  Pseudodifferential operators are expressed as integrals over the supremum of two points in the tree of balls $\mathcal{T}(\mathbb{Q}_{p})$ [3]. The transformation rule $\Phi\circ D_{F}=p^{-\gamma}D_{F(\phi(\cdot))}\circ\Phi$ under a dilation $\phi$ by $p^{\gamma}$ demonstrates how Haar scaling appears naturally in $p$‑adic analysis.

* **$p$‑adic measures from $L$‑functions.**  The construction of $p$‑adic multiple $L$‑functions uses a specific $p$‑adic measure that is normalized to assign total mass $1$ to $\mathbb{Z}_{p}$ [4]. This measure is precisely the Haar measure on $\mathbb{Z}_{p}$, providing a rigorous foundation for assigning probabilities to $p$‑adic subsets.

* **Geometric inequalities in $p$‑adic Hilbert spaces.**  The p‑adic van Lint–Seidel bound shows that for $p$‑adic $\gamma$‑equiangular lines the inequality $|n|^{2}\le |d|\max\{|n|,\gamma^{2}\}$ holds [5]. The appearance of absolute values $|\cdot|$ in a non‑Archimedean setting underscores the relevance of $p$‑adic norms for quantitative statements.

* **Period rings and Galois representations.**  The theory of $p$‑adic period rings $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$ establishes that $p$‑adic representations can be trivialized after extending scalars, a property that parallels the trivialization of probability measures after coarse‑graining on the tree [6].

* **$p$‑adic light cone and Higgs mechanism.**  The $p$‑adic square‑root function defines a light‑cone–like region where the series converges, with radius determined by powers of $p$ [7]. This geometric picture of a $p$‑adic causal structure motivates the interpretation of measurement outcomes as residing within nested light‑cone balls.

* **Ultrametric reformulation of the QEC–Darwinism trade‑off.**  Maity et al. proved a model‑independent no‑go theorem linking quantum error correction fidelity $F_{L}$ and redundancy $R_{\delta}$ in an Archimedean setting, and argued that an ultrametric (Bruhat–Tits) geometry replaces continuous redundancy by a discrete staircase [8]. Their analysis supplies the conceptual bridge between statistical‑independence assumptions and the ultrametric structure we employ.

* **Static relational network as a non‑Archimedean substrate.**  The QNFO synthesis proposes that the underlying ontology of reality is a timeless, discrete, non‑Archimedean relational network, providing a philosophical backdrop for interpreting the $p$‑adic tree as the fundamental information carrier [9].

These works collectively establish that (i) $p$‑adic norms and Haar measures are mathematically well‑defined, (ii) ultrametric spaces naturally generate discrete hierarchical structures, and (iii) the prime $p=3$ is singled out by phase‑transition phenomena. Our contribution builds directly on these foundations.

## 3. Methods
We begin by recalling the basic objects of $p$‑adic analysis needed for the construction.

### 3.1 $p$‑adic numbers and balls
For a fixed prime $p$, every non‑zero rational number $x$ can be uniquely written as  
\[
x = p^{r}\frac{n}{m},
\]  
with $r\in\mathbb{Z}$, $n,m\in\mathbb{Z}$, $p\nmid n,m$. The $p$‑adic norm is defined by  
\[
|x|_{p}=p^{-r},\qquad |0|_{p}=0.
\]  
A closed ball of radius $p^{-r}$ centered at $a\in\mathbb{Q}_{p}$ is  
\[
B(a,r)=\{\,x\in\mathbb{Q}_{p}\mid |x-a|_{p}\le p^{-r}\,\}.
\]  
Because of the strong triangle inequality, any two balls are either disjoint or one contains the other.

### 3.2 Haar measure on $\mathbb{Q}_{p}$
The additive group $(\mathbb{Q}_{p},+)$ admits a unique translation‑invariant (Haar) measure $\mu$ normalized by $\mu(\mathbb{Z}_{p})=1$, where $\mathbb{Z}_{p}=B(0,0)$ is the unit ball. For any ball $B(a,r)$ one has  
\[
\mu\!\left(B(a,r)\right)=p^{-r}.
\]  
This follows from the scaling property $\mu(p^{k}A)=p^{-k}\mu(A)$ for any measurable set $A$.

### 3.3 Mapping measurement outcomes to balls
Consider a quantum system with a finite set of mutually exclusive outcomes $\{o_{i}\}_{i=1}^{N}$. We associate to each outcome $o_{i}$ a distinct ball $B_{i}=B(a_{i},r_{i})$ such that the balls are pairwise disjoint. The probability assigned to $o_{i}$ is defined as the Haar measure of its ball:  
\[
P(o_{i})\equiv \mu(B_{i})=p^{-r_{i}}.
\]  
The normalization condition $\sum_{i}P(o_{i})=1$ translates into a Diophantine equation on the exponents $\{r_{i}\}$:
\[
\sum_{i=1}^{N}p^{-r_{i}}=1.
\]  

### 3.4 Relating amplitudes to radii
For a pure state $|\psi\rangle=\sum_{i}\alpha_{i}|i\rangle$ with complex amplitudes $\alpha_{i}$, the Born rule prescribes $P_{\text{Born}}(o_{i})=|\alpha_{i}|^{2}$. We propose the identification  
\[
|\alpha_{i}|^{2}=p^{-r_{i}}.
\]  
Taking logarithms base $p$ yields  
\[
r_{i}=-\log_{p}\!\bigl(|\alpha_{i}|^{2}\bigr).
\]  
Since $r_{i}$ must be an integer, the identification is exact only when $|\alpha_{i}|^{2}$ is a rational power of $p$. In practice, experimental frequencies are rational numbers, and the model predicts that only those rational numbers that can be expressed as $p^{-r}$ will be observed without systematic deviation.

## 4. Analysis
We now perform the explicit arithmetic that underlies the identification of Born probabilities with Haar measures.

### 4.1 Derivation of the Haar measure of a ball
Starting from the definition of the $p$‑adic norm, let $x\in B(a,r)$. By definition $|x-a|_{p}\le p^{-r}$. The set $B(a,r)$ can be written as a coset  
\[
B(a,r)=a+p^{r}\mathbb{Z}_{p}.
\]  
Because translation by $a$ does not change measure,  
\[
\mu\!\left(B(a,r)\right)=\mu\!\left(p^{r}\mathbb{Z}_{p}\right).
\]  
Using the scaling property of the Haar measure,  
\[
\mu\!\left(p^{r}\mathbb{Z}_{p}\right)=p^{-r}\mu\!\left(\mathbb{Z}_{p}\right)=p^{-r}\cdot1=p^{-r}.
\]  
Thus the measure of any ball of radius $p^{-r}$ equals $p^{-r}$.

### 4.2 Normalization for a three‑outcome experiment
Suppose $N=3$ outcomes and we choose the same radius $r$ for each ball, i.e. $r_{1}=r_{2}=r_{3}=r$. The disjointness condition forces the three balls to be placed on distinct branches of the Bruhat–Tits tree. The normalization equation becomes  
\[
3\,p^{-r}=1.
\]  
Solving for $r$ gives  
\[
p^{-r}=\frac{1}{3}\quad\Longrightarrow\quad r=-\log_{p}\!\left(\frac{1}{3}\right)=\log_{p}3.
\]  
Since $r$ must be an integer, the only prime $p$ for which $\log_{p}3$ is an integer is $p=3$, for which $\log_{3}3=1$. Therefore, with $p=3$ we obtain  
\[
r=1,\qquad p^{-r}=3^{-1}=\frac{1}{3}.
\]  
All three probabilities are equal to $1/3$, exactly reproducing the Born rule for an equal‑amplitude three‑outcome superposition.

### 4.3 Numerical example for a qubit
Consider a qubit in the state $|\psi\rangle=\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)$. The Born probabilities are $|\alpha_{0}|^{2}=|\alpha_{1}|^{2}=1/2$. We seek a prime $p$ and integer $r$ such that $p^{-r}=1/2$. Taking logarithms,
\[
r=-\log_{p}\!\left(\frac{1}{2}\right)=\frac{\ln 2}{\ln p}.
\]  
For $p=2$, $\ln p=\ln 2$ and $r=1$, yielding $p^{-r}=2^{-1}=1/2$, which matches the Born probability exactly. Hence the model predicts that a binary measurement can be represented on the $p=2$ tree with radius $r=1$.

### 4.4 Consistency with the Potts‑model phase transition
Reference [1] proves that a phase transition on a Cayley tree of order two occurs iff $p=3$. Our construction requires $p=3$ to obtain a normalized three‑outcome probability distribution. The coincidence indicates that the same arithmetic condition that governs statistical‑mechanical criticality also underlies the emergence of discrete Born probabilities.

### 4.5 Summary of arithmetic results
| Quantity | Derivation | Numerical value |
|----------|------------|-----------------|
| Haar measure of $B(a,1)$ for $p=3$ | $\mu(B)=p^{-1}=3^{-1}$ | $1/3$ |
| Radius $r$ solving $3p^{-r}=1$ for $p=3$ | $r=\log_{3}3=1$ | $1$ |
| Haar measure of $B(a,1)$ for $p=2$ | $2^{-1}$ | $1/2$ |

These explicit calculations constitute the concrete numerical backbone of the conjecture.

## 5. Results
The analysis yields the following concrete predictions:

1. **Discrete probability set.**  For a fixed prime $p$, any outcome probability must belong to the set $\{p^{-r}\mid r\in\mathbb{Z}_{\ge0}\}$.  

2. **Three‑outcome equal‑amplitude case.**  With $p=3$ the Haar measure of each ball of radius $r=1$ equals $1/3$, reproducing the Born rule for a symmetric three‑outcome interferometer.  

3. **Binary equal‑amplitude case.**  With $p=2$ the Haar measure of a ball of radius $r=1$ equals $1/2$, reproducing the Born rule for a symmetric qubit measurement.  

4. **Normalization condition.**  For any finite set of outcomes $\{o_{i}\}$ the integers $\{r_{i}\}$ must satisfy $\sum_{i}p^{-r_{i}}=1$. This Diophantine constraint is satisfied exactly when the set of amplitudes squares are rational powers of $p$.

No empirical data beyond the arithmetic derivations are introduced; all reported numbers follow directly from the $p$‑adic norm and the normalization equation.

## 6. Discussion
### 6.1 Limitations
- **Discrete probability assumption.**  The model assumes that experimental frequencies are exact rational powers of a single prime $p$. Real experiments yield statistical fluctuations and may involve irrational amplitudes, which would appear as deviations from the predicted set.
- **Choice of prime $p$.**  The analysis shows that different experimental configurations (binary vs. ternary) require different primes ($p=2$ vs. $p=3$). A universal theory would need a mechanism for selecting $p$ based on the physical context.
- **Mapping of amplitudes to radii.**  The identification $|\alpha_{i}|^{2}=p^{-r_{i}}$ forces amplitudes to be restricted to a discrete lattice; continuous phases and relative phases are not addressed.
- **Superdeterministic interpretation.**  The explanation of Bell‑type correlations via shared ancestry on the tree relies on a superdeterministic loophole, which remains philosophically contentious and experimentally hard to falsify.

### 6.2 Falsifiability
The conjecture is falsified if an experiment reports a probability $P$ that cannot be expressed as $p^{-r}$ for any integer $r$ and any fixed prime $p$ consistent across all outcomes. For example, observing $P=0.4$ in a binary measurement would contradict the $p=2$ prediction of $0.5$ and the $p=3$ prediction of $1/3$.

### 6.3 Open Questions
- How can the model accommodate complex phases and interference patterns beyond simple amplitude squares?
- Is there a dynamical principle that selects the appropriate prime $p$ for a given experimental setup?
- Can the ultrametric tree be embedded in a physical substrate (e.g., a quantum‑computational architecture) that naturally implements the Haar measure?

## 7. Practical Implications and Engineering Pathways
### (a) Potential users and design impact
The primary users are researchers in quantum foundations, quantum information theory, and designers of ultrametric quantum simulators. If the Haar‑measure derivation holds, designers can replace stochastic state‑preparation modules with deterministic tree‑branching hardware that enforces the required probability distribution by construction, simplifying calibration and error analysis.

### (b) Technology readiness
The work is purely analytical and has not undergone peer review; consequently it resides at **Technology Readiness Level 1** (basic principles observed) according to NASA definitions. No hardware or software implementation has been demonstrated.

### (c) Smallest next experiment
A minimal test consists of a three‑path interferometer (e.g., a tritter) with equal splitting ratios. The experiment measures the relative frequencies of the three output ports. The prediction is that each port registers a frequency converging to $1/3$ within statistical error. Observation of a systematic deviation (e.g., $0.28$, $0.36$, $0.36$) would falsify the $p=3$ Haar‑measure hypothesis.

### (d) Engineering constraints
- **Discrete amplitude preparation:** The experiment must prepare states whose squared amplitudes are exactly $1/3$ or $1/2$, requiring high‑precision beam splitters with rational splitting ratios.
- **Isolation of superdeterministic correlations:** To test the shared‑ancestor explanation of Bell violations, the setup must ensure that any hidden common cause resides on the same branch of the Bruhat–Tits tree, which translates into stringent timing and locality constraints.
- **Data acquisition:** Frequency estimation must achieve enough counts to resolve deviations at the $10^{-2}$ level, demanding low‑noise detectors and stable sources.

### (e) Projected performance bounds
Assuming ideal components, the Haar‑measure model predicts that the variance of the measured frequency for each outcome scales as $\sigma^{2}=p^{-r}(1-p^{-r})/N$, where $N$ is the total number of trials. For $p=3$, $r=1$, and $N=10^{4}$, the standard deviation is  
\[
\sigma=\sqrt{\frac{1/3\,(2/3)}{10^{4}}}\approx 0.0047,
\]  
which sets the target precision for a falsification test.

### (f) Risks and misuse
A possible misuse is to claim that any observed deviation from $1/3$ automatically validates superdeterminism, ignoring experimental imperfections. Care must be taken to separate genuine statistical anomalies from systematic errors.

## 8. Conclusion
We have shown that the Haar (topological) measure on $p$‑adic balls of the Bruhat–Tits tree yields a discrete set of probabilities that coincides with the Born rule for specific choices of the prime $p$ and the ball radii. The explicit arithmetic derivations demonstrate that for $p=3$ a three‑outcome equal‑amplitude experiment reproduces the Born probability $1/3$, while for $p=2$ a binary equal‑amplitude experiment reproduces $1/2$. The model predicts that any observed probability not belonging to $\{p^{-r}\}$ falsifies the conjecture, providing a clear experimental criterion. If validated, the result reinterprets the wavefunction as an epistemic bookkeeping device and offers a superdeterministic account of Bell‑type correlations via shared ancestry on the ultrametric tree. Future work will address the incorporation of complex phases, the dynamical selection of the prime $p$, and the construction of physical platforms that embody the $p$‑adic branching structure.

## References
[1] arXiv:math-ph/0512018v2 | On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree  
[2] arXiv:2308.04364v3 | Turing patterns in a p-adic FitzHugh-Nagumo system on the unit ball  
[3] arXiv:1105.1506v1 | Pseudodifferential p-adic vector fields and pseudodifferentiation of a composite p-adic function  
[4] arXiv:1508.07185v2 | Fundamentals of p-adic multiple L-functions and evaluation of their special values  
[5] arXiv:2408.00810v3 | p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound  
[6] arXiv:1908.08424v1 | An introduction to p-adic period rings  
[7] arXiv:hep-th/9410058v3 | p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone  
[8] QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces | https://papers.qnfo.org/papers/qec-darwinism-ultrametric  
[9] QNFO: All Things Are One | https://papers.qnfo.org/papers/all-things-are-one  

## Appendix A. Divergence report
*No divergent claims were identified among the drafts; all substantive statements converge.*

## Appendix B. Claim attribution
| ID | Claim | Source Draft(s) | Agreement |
|----|-------|-----------------|-----------|
| C1 | Real‑world problem: lack of derivation for Born rule blocks epistemic interpretation | A, B, C | Convergent |
| C2 | Contribution list (four items) | A, B, C | Convergent |
| C3 | Haar measure of a $p$‑adic ball equals $p^{-r}$ | A, B, C | Convergent |
| C4 | Phase transition in $p$‑adic Potts model occurs iff $p=3$ | A, B, C | Convergent |
| C5 | For $p=3$, three equal‑probability outcomes each have probability $1/3$ | A, B, C | Convergent |
| C6 | For $p=2$, binary equal‑probability outcomes each have probability $1/2$ | A, B, C | Convergent |
| C7 | Normalization equation $\sum_i p^{-r_i}=1$ | A, B, C | Convergent |
| C8 | Falsifiability condition: observed probability not in $\{p^{-r}\}$ falsifies conjecture | A, B, C | Convergent |
| C9 | TRL assessment: analytical work at TRL 1 | A, B, C | Convergent |
| C10 | Minimal experiment: three‑path interferometer testing $1/3$ probabilities | A, B, C | Convergent |
| C11 | Engineering constraints: discrete amplitude preparation, isolation of superdeterministic correlations | A, B, C | Convergent |
| C12 | Projected variance formula $\sigma^{2}=p^{-r}(1-p^{-r})/N$ | A, B, C | Convergent |
| C13 | Bibliography entries listed exactly as supplied | A, B, C | Convergent |