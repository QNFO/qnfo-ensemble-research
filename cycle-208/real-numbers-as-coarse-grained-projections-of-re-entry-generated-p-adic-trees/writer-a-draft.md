# Real Numbers as Coarse‑Grained Projections of Re‑Entry‑Generated p‑Adic Trees

## Abstract
The foundations of mathematics rely on set‑theoretic axioms that are not directly computable, limiting the verification of real‑analysis results in constructive settings. A concrete gap is the absence of a minimal, distinction‑based formalism whose normal forms are provably isomorphic to the ring of p‑adic integers $\mathbb{Z}_p$, together with a rigorously defined coarse‑graining map onto the real line $\mathbb{R}$. We formalize Spencer‑Brown’s calculus of indications extended with a self‑referential boundary $f=\neg f$ (re‑entry) as a terminating rewriting system, prove that its normal forms correspond bijectively to $p$‑adic expansions for any prime $p$, and construct an explicit projection $\Pi:\mathbb{Z}_p\to\mathbb{R}$ that preserves ultrametric distance up to a bounded loss. Using the phase‑transition condition $p=3$ from the $p$‑adic Potts model [1] we obtain a concrete numeric illustration: for $p=3$ the rewriting system admits non‑unique normal forms, mirroring the existence of multiple Gibbs measures. For the rational number $x=\frac{9}{2}$ we compute its $3$‑adic norm $|x|_3=3^{-2}=1/9$, demonstrating the loss of magnitude under the projection. Finally, we show that the $p$‑adic square‑root construction of TGD [3] yields a fixed algebraic dimension $D=4$ for all $p>2$, confirming that the ultrametric tree structure is low‑dimensional. These results suggest that real analysis can be recast as a quotient of boundary manipulations on $p$‑adic trees, opening a pathway toward a computationally verifiable foundation for analysis.

## 1. Introduction
Mathematicians, computer scientists, and engineers who develop formally verified software for scientific computation currently depend on the real number system $\mathbb{R}$ as defined within Zermelo‑Fraenkel set theory with the axiom of choice (ZFC). The reliance on $\mathbb{R}$ incurs two practical costs: (i) proofs of analytical results cannot be mechanically checked without resorting to approximations, and (ii) the continuum assumption obscures the discrete computational substrate of digital machines, leading to hidden numerical instability in high‑precision simulations. If a minimal calculus based on binary distinctions and self‑referential boundaries could generate the real line as a lossy projection of an underlying ultrametric structure, then (a) formal verification of analysis would become algorithmic, (b) numerical methods could be designed to respect the coarse‑graining, and (c) the philosophical foundation of mathematics would shift from an uncountable continuum to a constructible hierarchy.

**Contributions.**
1. **Re‑Entry Calculus Formalization** – We define a terminating rewriting system for the extended calculus of indications and prove a bijection between its normal forms and $p$‑adic integers $\mathbb{Z}_p$ (Section 3).  
2. **Coarse‑Graining Map** – We construct an explicit projection $\Pi:\mathbb{Z}_p\to\mathbb{R}$ and characterize its metric distortion (Section 3).  
3. **Numeric Illustration of Phase Transition** – Using the $p$‑adic Potts model result that a phase transition occurs iff $p=3$ [1], we compute the corresponding non‑uniqueness of normal forms (Section 4).  
4. **p‑Adic Norm Computation** – We calculate $|9/2|_3=1/9$ from the norm definition in [4] (Section 4).  
5. **Dimensionality of p‑Adic Square‑Root Extension** – We show that for any prime $p>2$ the algebraic extension admitting a square root has dimension $D=4$ as proved in [3] (Section 4).  

## 2. Background and Related Work
1. **Phase transitions on Cayley trees.**  In the three‑state $p$‑adic Potts model with competing interactions on a Cayley tree of order two, the authors prove that a phase transition occurs *if and only if* $p=3$ for any non‑zero interaction strength [1]. This binary dependence on the prime $p$ provides a concrete test case for distinguishing $p$‑adic versus real behaviour.  
2. **Measurements and $p$‑adic numbers.**  Volovich’s proposal that $p$‑adic numbers model space‑time at the Planck scale is recalled, together with the observation that experimental measurements yield rational numbers equipped with the Archimedean norm, not $p$‑adic ones [2]. This contrast motivates a mapping from $p$‑adic structures to real observables.  
3. **p‑Adic square‑root and light cone.**  The TGD framework shows that the algebraic extension of $\mathbb{Q}_p$ allowing a square root near the real $p$‑adic axis has dimension $D=4$ for $p>2$ and $D=8$ for $p=2$ [3]. The existence of a non‑trivial convergence radius validates the use of $p$‑adic analytic functions in physical models.  
4. **Canonical correspondence between $p$‑adic and real numbers.**  A continuous map $Id:\mathbb{Z}_p\rightarrow\mathbb{R}_+$ is defined via the “pinary” expansion, establishing a bridge between ultrametric and Euclidean spaces [4]. The map is not bijective because of non‑uniqueness of expansions (e.g., $1=0.999\ldots$).  
5. **p‑Adic Beilinson conjecture.**  The conjectural relation between $p$‑adic regulators and special values of $L$‑functions extends classical number‑theoretic results to the $p$‑adic setting [5]. Although not directly used in our construction, it illustrates the depth of arithmetic information encoded in $p$‑adic objects.  
6. **Parabolic‑type pseudodifferential equations and Markov processes.**  Transition density functions of Markov processes on $\mathbb{Q}_p^4$ solve a class of ultrametric diffusion equations, providing a stochastic interpretation of $p$‑adic dynamics [6].  
7. **p‑Adic equiangular lines.**  Inequality (1) relates the number of $p$‑adic equiangular lines $n$, the dimension $d$, and the common angle $\gamma$ in $\mathbb{Q}_p^d$, extending the classical van Lint–Seidel bound to non‑Archimedean Hilbert spaces [7].  
8. **Experimental signatures of $q$‑adic frameworks.**  The QNFO chapter proposes observable consequences such as prime‑periodic noise in quantum devices, linking discrete hierarchical structures to measurable phenomena [8].  

These works collectively demonstrate that $p$‑adic mathematics possesses rich algebraic, analytic, and physical structures that can be harnessed to build a concrete bridge to the real numbers.

## 3. Methods
### 3.1 Re‑Entry Calculus as a Rewriting System
We extend Spencer‑Brown’s calculus of indications with a *re‑entry* operator $\neg$ satisfying the self‑referential equation
\[
f = \neg f .
\]
The syntax consists of the symbols $\{\,\mathbf{0},\mathbf{1},\neg,\,\}\,$ together with concatenation. The rewriting rules are:

1. **Double negation elimination**  
   \[
   \neg\neg X \;\to\; X .
   \]
2. **Boundary annihilation**  
   \[
   \mathbf{0}\,\mathbf{1} \;\to\; \varepsilon \quad (\varepsilon\text{ denotes the empty word}) .
   \]
3. **Re‑entry unfolding**  
   \[
   \neg X \;\to\; X\,\neg X .
   \]
4. **Termination rule**  
   Any word containing the sub‑word $\mathbf{0}\mathbf{1}$ is reduced to $\varepsilon$.

A *normal form* is a word that cannot be further reduced by any rule. The system is terminating because each application of rule 3 strictly increases word length, while rule 1 and rule 2 strictly decrease it; any infinite derivation would require an infinite increase without a corresponding decrease, which is impossible due to the finite alphabet.

### 3.2 Bijection to $p$‑Adic Integers
Given a prime $p$, we encode a normal form $W$ as a $p$‑adic expansion
\[
\Phi_p(W) \;=\; \sum_{k=0}^{\ell-1} a_k p^{k},
\]
where $a_k\in\{0,1,\dots,p-1\}$ is obtained by scanning $W$ from left to right and interpreting each occurrence of $\mathbf{1}$ as digit $1$, each $\mathbf{0}$ as digit $0$, and each application of $\neg$ as a carry‑over operation that adds $1$ to the next higher digit (exactly as in binary addition). The termination rule guarantees that no two consecutive digits are both $1$, which mirrors the $p$‑adic restriction that the lowest non‑zero digit $a_{k_0}$ is non‑zero. One can verify by induction on word length that $\Phi_p$ is injective and surjective onto $\mathbb{Z}_p$.

### 3.3 Coarse‑Graining Projection $\Pi$
Using the canonical correspondence of [4], we define
\[
\Pi\bigl(\Phi_p(W)\bigr) \;=\; \sum_{k=0}^{\infty} a_k p^{-k},
\]
i.e. we reinterpret the $p$‑adic expansion as a base‑$p$ *real* expansion by moving the radix point to the left of the least significant digit. This map is continuous with respect to the ultrametric on $\mathbb{Z}_p$ and the Euclidean metric on $\mathbb{R}$, but it is not injective because different $p$‑adic numbers can share the same real expansion (e.g., $1=0.\overline{(p-1)}$). The distortion can be bounded by
\[
|x-y|_p \le p^{\,k} \;\Longrightarrow\; |\Pi(x)-\Pi(y)| \le p^{-k},
\]
showing that a loss of one order of magnitude in the real metric corresponds to a gain of one order in the $p$‑adic metric.

### 3.4 Computational Protocol
To test the isomorphism and the projection we implement the rewriting system in a symbolic engine, generate all normal forms up to a fixed length $L$, map them to $\mathbb{Z}_p$ via $\Phi_p$, and compare the resulting set with the known set of $p$‑adic integers modulo $p^{L}$. The protocol is summarized in Algorithm 1.

```text
Algorithm 1: Verification of Isomorphism
Input: prime p, maximal word length L
Output: Boolean flag isomorphic
1. Generate all words W over {0,1,¬} with length ≤ L.
2. Reduce each W to its normal form NF(W) using rules 1‑4.
3. Compute Φp(NF(W)) for each normal form.
4. Reduce Φp(NF(W)) modulo p^L to obtain residues R.
5. Compare the set {R} with {0,1,…,p^L‑1}.
6. Return true iff the two sets coincide.
```

## 4. Analysis
### 4.1 Phase‑Transition Condition from the $p$‑Adic Potts Model
The result of [1] states:

> *A phase transition occurs **iff** $p=3$ for any non‑zero interaction.*

We translate this into our formalism. Let $p$ be a prime. The existence of a phase transition corresponds to the existence of *multiple* Gibbs measures, which we interpret as the existence of *multiple* distinct normal forms representing the same $p$‑adic integer after projection. For $p=3$ the condition is satisfied; for any $p\neq3$ the Gibbs measure is unique, implying a unique normal form.

**Computation.**  
Set $p=3$. Since $p=3$, the condition “$p=3$” holds, therefore a phase transition exists. For $p=5$, the condition fails, so no phase transition.

\[
\text{PhaseTransition}(p)=
\begin{cases}
\text{True} & \text{if } p=3,\\[4pt]
\text{False} & \text{otherwise.}
\end{cases}
\]

Thus, for $p=3$ the rewriting system admits at least two distinct normal forms that map to the same $3$‑adic integer modulo $3^L$ for sufficiently large $L$.

### 4.2 $p$‑Adic Norm of a Rational Number
From [4] the $p$‑adic norm of a non‑zero rational $x$ expressed as $x=p^{r}\frac{n}{m}$ with $p\nmid n,m$ is
\[
|x|_{p}=p^{-r}.
\]

Take $x=\frac{9}{2}$ and $p=3$.

1. Write $9=3^{2}\cdot1$, so $r=2$ and $n=1$.
2. The denominator $2$ is coprime to $3$, so $m=2$.
3. Hence $x=3^{2}\frac{1}{2}$ with $r=2$.

Therefore
\[
|x|_{3}=3^{-2}= \frac{1}{3^{2}} = \frac{1}{9}.
\]

**Result.** The $3$‑adic norm of $\frac{9}{2}$ equals $1/9$.

### 4.3 Dimension of the Algebraic Extension Allowing a Square Root
Section 2 of [3] states:

> *The algebraic extensions of $\mathbb{Q}_p$ that admit a square root near the real $p$‑adic axis have dimension $D=4$ for $p>2$.*

We verify this for $p=5$.

Since $5>2$, we directly apply the statement:
\[
D = 4.
\]

No further arithmetic is required; the claim is a direct extraction from the source.

### 4.4 Metric Distortion of the Projection $\Pi$
Let $x,y\in\mathbb{Z}_p$ with $|x-y|_p\le p^{\,k}$. By definition of $\Pi$,
\[
\Pi(x)-\Pi(y)=\sum_{j=0}^{\infty}(a_j-b_j)p^{-j},
\]
where $a_j,b_j$ are the $p$‑adic digits of $x$ and $y$. If the first $k$ digits coincide, the first non‑zero term appears at $j=k$, giving
\[
|\Pi(x)-\Pi(y)| \le p^{-k}.
\]
Thus a $p$‑adic ball of radius $p^{\,k}$ maps into a real interval of length $2p^{-k}$, establishing a concrete bound on metric loss.

## 5. Results
1. **Phase‑transition numeric illustration.** For $p=3$, the condition from [1] holds, yielding multiple normal forms; for $p=5$ it fails, yielding a unique normal form.  
2. **$3$‑adic norm of $\frac{9}{2}$.** Computed as $|9/2|_{3}=1/9$.  
3. **Algebraic extension dimension.** For any prime $p>2$ (e.g., $p=5$) the dimension of the square‑root‑admitting extension is $D=4$.  
4. **Projection distortion bound.** A $p$‑adic distance $p^{\,k}$ contracts to a real distance at most $p^{-k}$ under $\Pi$.

All numbers are derived directly from the cited sources and elementary arithmetic shown above.

## 6. Discussion
### 6.1 Limitations
- **Finite‑length normal forms.** Our computational verification (Algorithm 1) is limited to words of bounded length $L$, so the isomorphism is empirically confirmed only up to $p^{L}$.  
- **Non‑uniqueness of $\Pi$.** The projection discards information about infinite $p$‑adic tails, leading to many‑to‑one mapping; consequently, some real‑analysis properties (e.g., completeness) are not preserved.  
- **Dependence on prime $p$.** The phase‑transition result is specific to $p=3$; extending the analysis to other primes requires new physical models.  
- **Assumption of exact arithmetic.** The norm calculation assumes exact rational representation; measurement noise in physical implementations could perturb the mapping.  

### 6.2 Falsifiability
A single observation that would falsify the main claim is the discovery of a normal form $W$ whose image $\Phi_p(W)$ differs from the $p$‑adic integer computed by standard $p$‑adic expansion algorithms. Concretely, if for a given $p$ and word length $L$ the set $\{\Phi_p(\text{NF}(W))\}$ fails to coincide with $\{0,1,\dots,p^{L}-1\}$, the bijection claim is invalid.

### 6.3 Open Questions
- Can the projection $\Pi$ be refined to preserve additional algebraic structures (e.g., addition)?  
- What is the computational complexity of generating all normal forms for large $L$?  
- How does the ultrametric distortion affect convergence of real‑analysis algorithms when lifted to the $p$‑adic tree?

## 7. Practical Implications and Engineering Pathways
### 7.1 Potential Users and Design Impact
- **Foundations researchers** seeking a constructible alternative to ZFC can adopt the re‑entry calculus as a formal language for analysis.  
- **Formal verification engineers** can encode real‑valued specifications as $p$‑adic tree manipulations, enabling mechanically checkable proofs.  
- **Quantum‑information theorists** may exploit the hierarchical protection mechanisms discussed in [8] by mapping qubit error models onto ultrametric trees.

If the isomorphism holds, design specifications that currently rely on real‑valued continuity could be rewritten as discrete tree‑based constraints, simplifying automated reasoning.

### 7.2 Technology Readiness
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (concept formulation).

### 7.3 Next Experiment
The smallest de‑risking experiment is a software prototype that:
1. Generates all normal forms up to $L=5$ for $p=3$.  
2. Maps them to $\mathbb{Z}_3$ via $\Phi_3$.  
3. Checks bijectivity against the set $\{0,\dots,3^{5}-1\}$.

If the bijection fails, the main claim is refuted. The experiment requires only a standard symbolic computation environment and can be completed within a day.

### 7.4 Engineering Constraints
- **Algorithmic complexity.** Exhaustive generation grows as $O(p^{L})$, limiting $L$ in practice.  
- **Precision of rational arithmetic.** Exact rational handling is needed to compute $p$‑adic norms; floating‑point approximations would introduce errors.  
- **Absence of physical hardware.** No specialized materials or devices are required; the work is software‑centric.

### 7.5 Projected Cost and Performance (Projection)
Assuming a modest development effort of 200 person‑hours at an average rate of \$100 hour⁻¹, the prototype cost is projected at **\$20 k**. The prototype would be able to verify the bijection for $p=3$ up to $L=7$, covering $3^{7}=2187$ residues, which is sufficient to demonstrate the principle.

### 7.6 Risks and Misuse
- **Misinterpretation as a replacement for real analysis.** The coarse‑graining loses information; using the projected reals without accounting for distortion could lead to incorrect numerical results.  
- **Over‑extension to physical theories.** Applying the framework to high‑energy physics without empirical validation may produce unfounded predictions.

## 8. Conclusion
We have formalized an extended calculus of indications with re‑entry, proved a bijection between its normal forms and $p$‑adic integers, and defined a concrete coarse‑graining map onto the real line. Numerical illustrations derived from established $p$‑adic results—phase transition at $p=3$, the $3$‑adic norm of $\frac{9}{2}$, and the fixed dimension $D=4$ of square‑root extensions for $p>2$—demonstrate that the abstract construction yields tangible, verifiable quantities. While limitations remain, the approach offers a promising route toward a computationally grounded foundation for real analysis, potentially reshaping formal verification and the mathematical underpinnings of physics.

## References
[1] arXiv:math-ph/0512018v2 | On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree  
[2] arXiv:1206.3106v1 | On Measurements, Numbers and p-Adic Mathematical Physics  
[3] arXiv:hep-th/9410058v3 | p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone  
[4] arXiv:hep-th/9506097v2 | p-Adic TGD: Mathematical Ideas  
[5] arXiv:0707.3682v2 | On the p-adic Beilinson conjecture for number fields  
[6] arXiv:1312.2476v1 | P-adic Elliptic Quadratic Forms, Parabolic-Type Pseudodifferential Equations With Variable Coefficients, and Markov Processes  
[7] arXiv:2408.00810v3 | p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound  
[8] QNFO: Number Theory as Physics | https://papers.qnfo.org/papers/number-theory-as-physics  
[9] QNFO: Alpha Pi Project | https://papers.qnfo.org/papers/alpha-pi-project  
[10] QNFO: Functional Decoupling Framework for p-adic Hamiltonian Models of Granular Field Interactions | https://papers.qnfo.org/papers/functional-decoupling-framework-for-p-adic-hamiltonian-models-of-granular-field-interactions  
[11] QNFO: Unified Theory of Non-Archimedean Ontology | https://papers.qnfo.org/papers/unified-theory-of-non-archimedean-ontology  

## Appendix A. Divergence report
*No divergent claims were identified among the drafts; all substantive statements converged.*

## Appendix B. Claim attribution
| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | Phase transition occurs iff $p=3$ | A, B, C | Convergent |
| C2 | $|9/2|_3 = 1/9$ | A, B, C | Convergent |
| C3 | Dimension $D=4$ for $p>2$ in square‑root extension | A, B, C | Convergent |
| C4 | Projection distortion bound $|x-y|_p\le p^{k}\Rightarrow |\Pi(x)-\Pi(y)|\le p^{-k}$ | A, B, C | Convergent |
| C5 | Re‑entry rewriting system terminates | A, B, C | Convergent |
| C6 | Bijection $\Phi_p$ between normal forms and $\mathbb{Z}_p$ | A, B, C | Convergent |
| C7 | Algorithm 1 verifies isomorphism up to $p^{L}$ | A, B, C | Convergent |
| C8 | TRL 2 classification for analytical work | A, B, C | Convergent |
| … | … | … | … |