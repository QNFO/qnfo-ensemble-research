# Spectral Decomposition of the Bruhat–Tits Tree and Its Prospects for Standard Model Mass Ratios

## Abstract

We investigate whether the eigenvalue spectrum of a natural Laplacian on the Bruhat–Tits tree of the $p$‑adic field $\mathbb{Q}_p$ can encode the hierarchy of particle masses in the Standard Model. Starting from the regular $(p\!+\!1)$‑valent infinite tree, we define a discrete Laplace operator with boundary conditions inspired by the adelic product formula. For a finite truncation of depth $N=3$ and the prime $p=2$, we compute the adjacency matrix eigenvalues analytically, transform them into Laplacian eigenvalues, and obtain the ratio $\mu_{3}/\mu_{1}=5$. We compare this ratio to the empirical muon‑to‑electron mass ratio ($\approx 206.8$) and discuss the discrepancy. The analysis also incorporates the $p$‑adic minimal length $1/p=0.5$ from Zúñiga–Galindo’s Dirac analysis as a natural scale. While the simple model does not reproduce the observed hierarchy, it illustrates a concrete computational pipeline that can be refined by (i) deeper truncations, (ii) alternative boundary conditions, and (iii) adelic constraints across all places. Our work thus provides a transparent benchmark for future attempts to bridge $p$‑adic geometry and particle phenomenology.

## 1. Introduction

The Bruhat–Tits tree $\mathcal{T}_p$ associated with the $p$‑adic field $\mathbb{Q}_p$ is a regular infinite graph of degree $p\!+\!1$ that plays a central role in non‑Archimedean geometry, representation theory, and the emerging $p$‑adic AdS/CFT correspondence. Recent proposals (e.g., Chen–Liu–Hung) have employed $\mathcal{T}_p$ to model holographic bulk dynamics, yet a direct link to the spectrum of elementary particles remains speculative. The present study asks whether a spectral decomposition of a Laplacian on $\mathcal{T}_p$ can generate eigenvalue ratios that mirror Standard Model (SM) mass ratios. If successful, such a number‑theoretic construction would echo the adelic CFT proof of quadratic reciprocity (Huang–Stoica–Zhong) and provide a novel, testable bridge between $p$‑adic geometry and phenomenology.

Our contribution is threefold. First, we formulate a discrete Laplacian on a finite truncation $\mathcal{T}_p^{(N)}$ with boundary conditions motivated by the adelic product formula. Second, we carry out an explicit analytic computation of the spectrum for $p=2$, $N=3$, and derive concrete eigenvalue ratios. Third, we compare these ratios to SM mass ratios and to the $p$‑adic minimal length $1/p$, highlighting both the promise and the limitations of the approach.

## 2. Background and Related Work

The literature on Bruhat–Tits trees spans algebraic, geometric, and physical perspectives. The foundational work of [1] introduced the notion of *branches*—sub‑trees encoding maximal orders in matrix algebras over local fields—and demonstrated their utility in global selectivity problems. This algebraic framework underlies our construction of the Laplacian’s domain.

Bending the tree to emulate a BTZ black hole geometry was explored in [2], where a novel $p$‑adic exponential function was defined to transplant Wilson line observables onto $\mathcal{T}_p$. Their methodology informs our choice of boundary conditions, which we adapt to respect adelic invariance.

The formal verification of $\mathcal{T}_p$ in the Lean theorem prover, presented in [3], provides a rigorous foundation for manipulating harmonic cochains on the tree. Our spectral analysis relies on the same harmonic structure, ensuring that our Laplacian is mathematically well‑defined.

Spinor field theories on $\mathcal{T}_p$ were investigated in [4], revealing that integrating out interior vertices yields a boundary action reminiscent of scalar $p$‑adic field theory. This result motivates our focus on the *boundary* spectrum as the potential carrier of physical mass information.

Geodesic bulk diagrams, shown in [5] to compute global conformal blocks in $p$‑adic AdS/CFT, illustrate how bulk graph combinatorics translate into boundary correlators. Our eigenvalue ratios can be interpreted as a simplified analogue of such diagrammatic weights.

Effective field theories on subspaces of $\mathcal{T}_p$ were derived in [6], where the limit to the tree’s boundary reproduces a conformal field theory over $p$‑adic numbers. This limit parallels the adelic product formula that we employ to constrain the Laplacian’s spectrum.

The exponential mixing properties of geodesic translation maps on locally finite trees, proved in [7], guarantee rapid decay of correlations, a feature that could be essential for stabilising mass hierarchies derived from spectral data.

Finally, the study of $p$‑adic colligations and rational maps in [8] introduced transfer‑function techniques that map tree dynamics to building automorphisms. Such transfer functions could be used in future work to relate eigenvectors of the Laplacian to physical states.

Collectively, these works provide algebraic, analytic, and physical tools that we synthesize in the present paper.

## 3. Methods

### 3.1. Tree Truncation and Vertex Set

We consider the $(p\!+\!1)$‑regular infinite Bruhat–Tits tree $\mathcal{T}_p$. For computational tractability we truncate at depth $N$, retaining all vertices whose graph distance from a distinguished root $v_0$ satisfies $0\le d(v_0,v)\le N$. The resulting finite tree $\mathcal{T}_p^{(N)}$ contains
\[
\#V = 1 + (p+1)\sum_{k=0}^{N-1} p^{k}
= 1 + (p+1)\frac{p^{N}-1}{p-1}
\]
vertices. For $p=2$, $N=3$ this yields
\[
\#V = 1 + 3\frac{2^{3}-1}{2-1}=1+3\cdot7=22.
\]

### 3.2. Adjacency Matrix

Let $A$ be the $\#V\times\#V$ adjacency matrix of $\mathcal{T}_p^{(N)}$, with $A_{ij}=1$ iff vertices $i$ and $j$ are connected by an edge, and $0$ otherwise.

### 3.3. Laplacian Definition

We define the (unnormalised) graph Laplacian
\[
L = (p+1)I - A,
\]
where $I$ is the identity matrix. This choice mirrors the combinatorial Laplacian on a regular graph of degree $p+1$.

### 3.4. Boundary Conditions from the Adelic Product Formula

The adelic product formula states that for any non‑zero rational number $x$,
\[
\prod_{v\in\{\infty, p\}} |x|_v = 1,
\]
where $|\cdot|_v$ denotes the absolute value at the place $v$. Translating to the tree, we impose Dirichlet conditions on the outermost layer (depth $N$) such that the eigenfunctions vanish there. This mimics the “adelic truncation” used in $p$‑adic string amplitudes.

### 3.5. Analytic Spectrum for Radial Functions

Because $\mathcal{T}_p^{(N)}$ is radially symmetric, eigenfunctions can be taken to depend only on the distance $k$ from the root. The adjacency action on a radial vector $f_k$ satisfies the recurrence
\[
\lambda f_k = p\, f_{k-1} + f_{k+1},
\quad 1\le k\le N-1,
\]
with boundary equations
\[
\lambda f_0 = (p+1) f_1,\qquad
\lambda f_N = p\, f_{N-1},
\]
where $\lambda$ denotes an adjacency eigenvalue. Solving this linear difference equation yields
\[
\lambda_m = 2\sqrt{p}\,\cos\!\left(\frac{m\pi}{N+1}\right),
\quad m=1,\dots,N.
\]

### 3.6. Laplacian Eigenvalues

Given $\lambda_m$, the corresponding Laplacian eigenvalues are
\[
\mu_m = (p+1) - \lambda_m.
\]

## 4. Analysis

We now compute the spectrum explicitly for the concrete parameters $p=2$ and $N=3$.

### 4.1. Compute $\sqrt{p}$

\[
\sqrt{p} = \sqrt{2} \approx 1.41421356.
\]

### 4.2. Compute the factor $2\sqrt{p}$

\[
2\sqrt{p} = 2 \times 1.41421356 \approx 2.82842712.
\]

### 4.3. Determine the angles $\theta_m = \frac{m\pi}{N+1}$

For $N=3$, $N+1=4$.

- $m=1$: $\theta_1 = \frac{1\pi}{4}= \frac{\pi}{4}\approx 0.78539816$ rad.
- $m=2$: $\theta_2 = \frac{2\pi}{4}= \frac{\pi}{2}\approx 1.57079633$ rad.
- $m=3$: $\theta_3 = \frac{3\pi}{4}= 2.35619449$ rad.

### 4.4. Compute $\cos(\theta_m)$

- $\cos(\theta_1)=\cos(\pi/4)=\frac{\sqrt{2}}{2}\approx 0.70710678$.
- $\cos(\theta_2)=\cos(\pi/2)=0$.
- $\cos(\theta_3)=\cos(3\pi/4)=-\frac{\sqrt{2}}{2}\approx -0.70710678$.

### 4.5. Compute adjacency eigenvalues $\lambda_m = 2\sqrt{p}\cos(\theta_m)$

- $\lambda_1 = 2.82842712 \times 0.70710678 \approx 2.00000000$ (rounded to $2$).
- $\lambda_2 = 2.82842712 \times 0 = 0$.
- $\lambda_3 = 2.82842712 \times (-0.70710678) \approx -2.00000000$ (rounded to $-2$).

### 4.6. Compute Laplacian eigenvalues $\mu_m = (p+1) - \lambda_m$

Since $p+1 = 3$:

- $\mu_1 = 3 - 2 = 1$.
- $\mu_2 = 3 - 0 = 3$.
- $\mu_3 = 3 - (-2) = 5$.

### 4.7. Eigenvalue Ratios

We focus on the ratio of the largest to the smallest non‑zero Laplacian eigenvalue:

\[
R = \frac{\mu_3}{\mu_1} = \frac{5}{1} = 5.
\]

### 4.8. Comparison to Physical Mass Ratios

The empirical muon‑to‑electron mass ratio is

\[
R_{\text{exp}} = \frac{m_{\mu}}{m_{e}} \approx \frac{105.66\ \text{MeV}}{0.511\ \text{MeV}} \approx 206.768.
\]

Our computed ratio $R=5$ is therefore off by a factor of roughly $41.35$.

### 4.9. $p$‑adic Minimal Length

Zúñiga–Galindo’s $p$‑adic Dirac analysis introduces a natural length scale $\ell_{\min}=1/p$.

For $p=2$:

\[
\ell_{\min}= \frac{1}{2}=0.5.
\]

We note that $\ell_{\min}$ does not directly appear in the eigenvalue ratios but provides a dimensional anchor for interpreting the Laplacian spectrum as a set of inverse‑length squared quantities.

## 5. Results

| Quantity | Value | Derivation |
|----------|-------|------------|
| $\sqrt{p}$ | $1.41421356$ | $\sqrt{2}$ |
| $2\sqrt{p}$ | $2.82842712$ | $2\times\sqrt{p}$ |
| $\lambda_1$ | $2$ | $2\sqrt{p}\cos(\pi/4)$ |
| $\lambda_2$ | $0$ | $2\sqrt{p}\cos(\pi/2)$ |
| $\lambda_3$ | $-2$ | $2\sqrt{p}\cos(3\pi/4)$ |
| $\mu_1$ | $1$ | $3-\lambda_1$ |
| $\mu_2$ | $3$ | $3-\lambda_2$ |
| $\mu_3$ | $5$ | $3-\lambda_3$ |
| Eigenvalue ratio $R$ | $5$ | $\mu_3/\mu_1$ |
| Muon/electron mass ratio $R_{\text{exp}}$ | $206.768$ | Empirical data |
| $p$‑adic minimal length $\ell_{\min}$ | $0.5$ | $1/p$ |

The explicit arithmetic demonstrates that, for the simplest truncation, the Laplacian spectrum yields a modest integer ratio $5$, far from the observed SM mass hierarchy.

## 6. Discussion

### 6.1. Limitations of the Current Model

1. **Truncation Depth**: We used $N=3$ for analytical convenience. Deeper truncations increase the number of eigenvalues and may produce ratios closer to physical values, but also introduce computational complexity.
2. **Boundary Conditions**: Dirichlet conditions at depth $N$ are a crude implementation of adelic invariance. Alternative mixed or Neumann conditions could modify the spectrum substantially.
3. **Prime Choice**: The calculation was performed for $p=2$. Other primes change the degree $p+1$ and the factor $2\sqrt{p}$, potentially yielding different ratios.
4. **Spectral Interpretation**: We identified Laplacian eigenvalues with inverse‑length squared scales, but the mapping to particle masses lacks a rigorous field‑theoretic justification.
5. **Neglected Interactions**: The model treats the tree as a free graph; coupling to gauge fields or spinor structures (as in [4]) may shift eigenvalues.

### 6.2. Failure Modes and Falsifiability

- **Empirical Mismatch**: If, after systematic exploration of $p$, $N$, and boundary conditions, no eigenvalue ratio approaches any known SM mass ratio within an order of magnitude, the conjecture that $\mathcal{T}_p$ directly encodes the mass spectrum would be falsified.
- **Adelic Consistency**: The adelic product formula imposes a global constraint across all primes. If a spectrum derived at a single prime cannot be extended to satisfy the product constraint, the approach fails.
- **Non‑integer Ratios**: Physical mass ratios are not simple integers; a model that only yields integer ratios may be too coarse.

### 6.3. Open Questions

1. **Higher‑Dimensional Generalisations**: Can one define a Laplacian on the product of Bruhat–Tits trees over all places and extract a joint spectrum?
2. **Incorporating Spinor Representations**: How does the spinor boundary theory of [4] modify the eigenvalue problem?
3. **Relation to Harmonic Cochains**: The formalisation in [3] suggests a cohomological interpretation of eigenfunctions; could cohomology classes correspond to particle families?
4. **Adelic Spectral Zeta Functions**: Defining a zeta function $\zeta_{\mathcal{T}}(s)=\sum \mu_m^{-s}$ and imposing adelic functional equations might constrain the spectrum more tightly.

### 6.4. Path Forward

A systematic numerical study varying $p\in\{2,3,5,7\}$ and $N\in\{3,\dots,10\}$, combined with mixed boundary conditions derived from the adelic product, is the next logical step. Parallel analytical work on the spectral measure of the infinite tree (continuous spectrum) may reveal scaling laws that better align with SM hierarchies.

## 7. Conclusion

We have presented a concrete, fully documented computation of the Laplacian spectrum on a finite Bruhat–Tits tree truncation and compared the resulting eigenvalue ratios to Standard Model mass ratios. The simple model yields a ratio of $5$, far from the empirical muon‑to‑electron ratio of $\approx 207$, highlighting the need for richer structures—deeper truncations, alternative boundary conditions, and adelic constraints. Nonetheless, the methodology establishes a clear pipeline for future investigations that aim to embed particle phenomenology within $p$‑adic geometric frameworks.

## References

[1] arXiv:1712.01463v2 | On the missing branches of the Bruhat-Tits tree  
[2] arXiv:2102.12024v2 | Bending the Bruhat-Tits Tree II: the p-adic BTZ Black hole and Local Diffeomorphism on the Bruhat-Tits Tree  
[3] arXiv:2505.12933v4 | Formalising the Bruhat-Tits Tree  
[4] arXiv:1910.09397v2 | The boundary theory of a spinor field theory on the Bruhat-Tits tree  
[5] arXiv:1704.01149v2 | Geodesic bulk diagrams on the Bruhat-Tits tree  
[6] arXiv:2402.03730v2 | Effective field theories on subspaces of the Bruhat-Tits tree  
[7] arXiv:1506.04306v1 | Effective Mixing and Counting in Bruhat-Tits Trees  
[8] arXiv:1301.5453v1 | On $p$-adic colligations and 'rational maps' of Bruhat-Tits trees  
[9] QNFO: Spectral Dynamics on Bruhat-Tits Trees | DOI 10.5281/zenodo.18629520  
[10] QNFO: The Adelic Cross-Domain Program v5.0: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat–Tits Trees | DOI 10.5281/zenodo.21965332  
[11] QNFO: Alpha Pi Project | DOI 10.5281/zenodo.19479493  
[12] QNFO: The Adelic Cross-Domain Program: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees (Phase 3-4 Update) | DOI 10.5281/zenodo.21498074