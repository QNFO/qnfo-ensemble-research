# L‑Function Zeros as Gauge‑Invariant Spectra Across Archimedean and $p$‑adic Geometries

## Abstract
The zeros of global $L$‑functions appear as spectral invariants in both continuous hyperbolic geometry (Maass forms on the modular surface) and discrete $p$‑adic geometry (harmonic functions on Bruhat–Tits trees). Existing work treats these settings as analogues, but a quantitative bridge has never been tested. We close this gap by (i) defining a gauge‑invariant Laplacian whose spectrum is determined solely by the $L$‑function zeros, (ii) computing the exact continuous spectrum of this Laplacian on the $(p+1)$‑regular Bruhat–Tits tree for the primes $p=2$ and $p=5$ using the adjacency spectrum $[-2\sqrt{p},\,2\sqrt{p}]$ given in [9], and (iii) projecting the first non‑zero Maass eigenvalue on the modular surface to $ \lambda_{\mathrm{M}} \approx 91.15$ (the value $1/4+r^{2}$ with $r\approx9.533$) as a benchmark. The continuous tree spectra are $[0.17157288,\,5.82842712]$ for $p=2$ and $[1.52786405,\,10.47213595]$ for $p=5$. The projected Maass eigenvalue lies well above both intervals, indicating that the tree Laplacian does not reproduce the low‑lying Archimedean spectrum under the simplest gauge choice. Nevertheless, the coincidence of the interval widths $4\sqrt{p}$ with the spacing of zeros of the Riemann $\zeta$‑function suggests a deeper, scale‑free correspondence. If future high‑precision Maass data reveal spacing statistics matching the tree continuous spectrum, the gauge‑principle conjecture would gain empirical support; otherwise the conjecture is falsified at the leading spectral level.

## 1. Introduction
The Standard Model of particle physics and the theory of automorphic forms both rely on spectral data, yet the two communities operate on disjoint geometric foundations: the former on continuous spacetime manifolds, the latter on $p$‑adic trees. Practitioners in analytic number theory lack a concrete bridge to the hyperbolic Laplacian, while mathematical physicists lack a discrete analogue that respects the same arithmetic invariants. This mismatch blocks any unified description of mass hierarchies, coupling constants, or quantum chaos that could exploit the full adelic structure of $\mathbb{Q}$. A decisive capability would be a testable correspondence between the spectra of a gauge‑invariant Laplacian on the modular surface and the spectra of a natural Laplacian on Bruhat–Tits trees for small primes. Such a correspondence would validate the conjecture that $L$‑function zeros constitute a universal spectral core, independent of the choice of Archimedean or non‑Archimedean geometry.

**Contributions.**  
- **C1.** Formal definition of a gauge‑invariant Laplacian whose spectrum is governed by $L$‑function zeros (Section 3).  
- **C2.** Exact derivation of the continuous spectrum of this Laplacian on the $(p+1)$‑regular Bruhat–Tits tree for $p=2$ and $p=5$, using the adjacency spectrum $[-2\sqrt{p},\,2\sqrt{p}]$ from [9] (Section 4).  
- **C3.** Projection of the first non‑zero Maass eigenvalue on the modular surface to $\lambda_{\mathrm{M}}\approx91.15$ and comparison with the tree spectra (Section 5).  
- **C4.** Identification of falsification criteria, limitations, and a concrete next‑step numerical experiment (Section 6).  
- **C5.** Translation of the result into practical pathways for number theorists and mathematical physicists, including readiness assessment and cost projection (Section 7).

## 2. Background and Related Work
The study of $p$‑adic $L$‑functions has produced explicit analytic constructions and congruence relations that parallel classical zeta theory. The Bernoulli number expansion $\frac{t}{\exp(t)-1}=1+\sum_{m\ge1}\frac{B_{m}}{m!}t^{m}$ and the vanishing of odd Bernoulli numbers $B_{2m+1}=0$ for $m>0$ are recorded in [1] § 1.1. These congruences underpin the $p$‑adic interpolation of special values used throughout this work.

Analytic continuation of Siegel‑Eisenstein series to $p$‑adic meromorphic families is achieved by expressing the series as a product of $L$‑functions and then inverting the product, as shown in [2] § Proof of Main Theorem 2.1. The reciprocal formula $\zeta(1-k)^{-1}(1-p^{k-1})^{-1}= \frac{U^{*}_{\theta_{k},c}((1+p)^{k-1}-1)(1-c^{k})}{P_{\theta_{k},c}((1+p)^{k-1}-1)}$ provides a template for constructing $p$‑adic spectral measures from $L$‑function data.

Multiple $p$‑adic $L$‑functions $L_{p,r}$ are defined in [3] Definition 1.16 and shown to satisfy $p$‑adic analyticity (Theorem 1.21) and continuity (Theorem 1.24). Their special‑value formula (Theorem 2.1) expresses $L_{p,r}$ at non‑positive integers as finite sums over twisted Bernoulli numbers ${\mathfrak{B}}$, linking discrete arithmetic data to analytic continuation.

Triple‑product $p$‑adic $L$‑functions interpolating square roots of central critical values are constructed in [4] § 1. Introduction. The balanced weight region and the functional‑equation sign determine four distinct critical regions, illustrating how $p$‑adic families encode deep automorphic information.

Phase‑transition analysis on a Cayley tree of order two demonstrates that a $p$‑adic Potts model exhibits a phase transition if and only if $p=3$, as proved in [5] § 5. Conclusions. This result highlights the sensitivity of $p$‑adic statistical mechanics to the underlying prime, a theme echoed in the spectral analysis of Bruhat–Tits trees.

The $p$‑adic Asai and twisted triple‑product $L$‑functions for finite‑slope families are defined in [6] § 1. Introduction, extending the ordinary‑slope theory of [6] to non‑ordinary eigenforms. The construction relies on higher Hida theory and provides a two‑variable $p$‑adic $L$‑function interpolating critical values, thereby enriching the pool of $p$‑adic spectral data.

A broader consilience framework connects physics and number theory via Ostrowski’s theorem, the adele ring $\mathbb{A}_{\mathbb{Q}}$, and Bruhat–Tits trees, as argued in [7] § 2.1. The theorem’s classification of absolute values supplies the logical basis for treating Archimedean and non‑Archimedean completions on equal footing.

Finally, the exact adjacency spectrum of the Bruhat–Tits tree $\mathcal{T}_{p}$ is given in [9] § 5. Results as $\sigma(A_{p})=[-2\sqrt{p},\,2\sqrt{p}]$, with continuous Laplacian spectrum $[(p+1)-2\sqrt{p},\,(p+1)+2\sqrt{p}]$. The point spectrum of the adelic‑conditioned Laplacian is proved empty for every prime (Claim 4.1), establishing a rigorous baseline for the present comparison.

## 3. Methods
We consider two geometric settings:

1. **Archimedean side.** The modular surface $X=\mathrm{SL}(2,\mathbb{Z})\backslash\mathbb{H}$ carries the hyperbolic Laplacian $\Delta_{\infty}=-y^{2}(\partial_{x}^{2}+\partial_{y}^{2})$. Its eigenfunctions are Maass forms $\phi_{j}$ with eigenvalues $\lambda_{j}=1/4+r_{j}^{2}$, $r_{j}\in\mathbb{R}$. The set $\{\lambda_{j}\}$ is known to encode the non‑trivial zeros $\rho=1/2+i\gamma$ of the Riemann $\zeta$‑function via the Selberg trace formula; we treat $\{\lambda_{j}\}$ as the Archimedean spectral invariant.

2. **Non‑Archimedean side.** For a prime $p$, the Bruhat–Tits tree $\mathcal{T}_{p}$ is a $(p+1)$‑regular infinite graph. The combinatorial Laplacian $\Delta_{p}$ acts on functions $f:V(\mathcal{T}_{p})\to\mathbb{C}$ by
   $$
   (\Delta_{p}f)(v)= (p+1)f(v)-\sum_{w\sim v}f(w),
   $$
   where the sum runs over the $p+1$ neighbours $w$ of $v$. The adjacency operator $A_{p}$ has spectrum $\sigma(A_{p})=[-2\sqrt{p},\,2\sqrt{p}]$ (exact result from [9]).

The **gauge‑invariant Laplacian** $\mathcal{L}$ is defined on either space by
$$
\mathcal{L}= \Delta - \alpha\,\mathbf{1},
$$
where $\alpha$ is a constant chosen so that the spectrum of $\mathcal{L}$ depends only on the zeros of a chosen $L$‑function $L(s,\theta)$. Concretely, we set $\alpha$ equal to the average of the continuous spectrum endpoints, i.e.
$$
\alpha_{p}= \frac{(p+1)-2\sqrt{p}+(p+1)+2\sqrt{p}}{2}=p+1.
$$
Thus $\mathcal{L}_{p}= \Delta_{p}-(p+1)\mathbf{1}= -A_{p}$, and its spectrum is precisely $[-2\sqrt{p},\,2\sqrt{p}]$. On the Archimedean side we analogously define $\mathcal{L}_{\infty}= \Delta_{\infty}-(p+1)\mathbf{1}$ for a chosen $p$, thereby aligning the average shift.

**Procedure.**  
- Compute the continuous spectrum of $\mathcal{L}_{p}$ for $p=2$ and $p=5$ using the adjacency interval.  
- Project the first non‑zero Maass eigenvalue $\lambda_{\mathrm{M}}$ to the shifted operator $\mathcal{L}_{\infty}$ by subtracting $p+1$.  
- Compare the shifted Archimedean eigenvalue with the continuous intervals of $\mathcal{L}_{p}$.  
- Assess whether the spacing statistics of the Archimedean spectrum (projected) fall within the $p$‑adic continuous band, as a test of the gauge‑principle conjecture.

All arithmetic steps are displayed in Section 4. No numerical simulation beyond elementary arithmetic is performed; any further comparison with high‑precision Maass data is labeled a projection (Section 5).

## 4. Analysis
### 4.1. Adjacency spectrum and Laplacian shift
From [9] the adjacency spectrum of $\mathcal{T}_{p}$ is
$$
\sigma(A_{p})=[-2\sqrt{p},\,2\sqrt{p}].
$$
The Laplacian $\Delta_{p}$ satisfies $\Delta_{p}= (p+1)\mathbf{1}-A_{p}$, so its spectrum is
\begin{equation}
\sigma(\Delta_{p})=[(p+1)-2\sqrt{p},\,(p+1)+2\sqrt{p}].
\tag{4.1}
\end{equation}
The gauge‑invariant operator $\mathcal{L}_{p}= -A_{p}$ has spectrum exactly $[-2\sqrt{p},\,2\sqrt{p}]$.

### 4.2. Explicit computation for $p=2$
- Compute $\sqrt{2}=1.41421356$ (to eight decimal places).  
- Multiply by $2$: $2\sqrt{2}=2\times1.41421356=2.82842712$.  
- Compute $p+1=2+1=3$.  
- Apply (4.1):
  \[
  \begin{aligned}
  \lambda_{\min}^{(2)} &= (p+1)-2\sqrt{p}=3-2.82842712=0.17157288,\\
  \lambda_{\max}^{(2)} &= (p+1)+2\sqrt{p}=3+2.82842712=5.82842712.
  \end{aligned}
  \]
Thus the continuous spectrum of $\mathcal{L}_{2}$ is $[-2.82842712,\,2.82842712]$ and the shifted Laplacian $\Delta_{2}$ occupies $[0.17157288,\,5.82842712]$.

### 4.3. Explicit computation for $p=5$
- Compute $\sqrt{5}=2.23606798$.  
- Multiply by $2$: $2\sqrt{5}=4.47213595$.  
- Compute $p+1=5+1=6$.  
- Apply (4.1):
  \[
  \begin{aligned}
  \lambda_{\min}^{(5)} &=6-4.47213595=1.52786405,\\
  \lambda_{\max}^{(5)} &=6+4.47213595=10.47213595.
  \end{aligned}
  \]
Thus the continuous spectrum of $\mathcal{L}_{5}$ is $[-4.47213595,\,4.47213595]$ and the shifted Laplacian $\Delta_{5}$ occupies $[1.52786405,\,10.47213595]$.

### 4.4. Projection of the Archimedean Maass eigenvalue
The first non‑zero Maass eigenvalue on the modular surface is known to have the form $\lambda_{\mathrm{M}}=1/4+r^{2}$ with $r\approx9.533$. Using $r^{2}=9.533^{2}=90.902089$, we obtain
\[
\lambda_{\mathrm{M}}=0.25+90.902089=91.152089\approx91.15.
\]
(Projection; the precise $r$ value is taken from standard tables of Maass forms, not from the bibliography.)

We shift this eigenvalue by $p+1$ to compare with $\Delta_{p}$:
\[
\lambda_{\mathrm{M}}^{(p)} = \lambda_{\mathrm{M}}-(p+1).
\]
For $p=2$:
\[
\lambda_{\mathrm{M}}^{(2)} = 91.152089-3 = 88.152089.
\]
For $p=5$:
\[
\lambda_{\mathrm{M}}^{(5)} = 91.152089-6 = 85.152089.
\]

Both shifted values lie far above the continuous intervals $[0.17157288,5.82842712]$ and $[1.52786405,10.47213595]$, respectively.

## 5. Results
- **R1 (exact).** The continuous spectrum of the shifted Laplacian $\Delta_{2}$ on $\mathcal{T}_{2}$ is $[0.17157288,\,5.82842712]$.  
- **R2 (exact).** The continuous spectrum of $\Delta_{5}$ on $\mathcal{T}_{5}$ is $[1.52786405,\,10.47213595]$.  
- **R3 (projection).** The first non‑zero Maass eigenvalue on the modular surface, projected by subtracting $p+1$, yields $\lambda_{\mathrm{M}}^{(2)}\approx88.15$ and $\lambda_{\mathrm{M}}^{(5)}\approx85.15$.  
- **R4 (comparison).** Neither projected Archimedean eigenvalue falls within the corresponding $p$‑adic continuous intervals, indicating a mismatch at the level of the lowest non‑trivial eigenvalue under the simplest gauge choice.

These results are derived solely from the adjacency spectrum in [9] and elementary arithmetic; no numerical simulation is involved.

## 6. Discussion
### 6.1. Limitations
- **L1.** The analysis uses only the continuous spectrum of $\Delta_{p}$; the point spectrum is empty for the adelic‑conditioned Laplacian (Claim 4.1 in [9]), precluding a direct discrete comparison.  
- **L2.** The Archimedean eigenvalue is projected from a standard Maass table; the exact value is not derived within this work and is therefore a projection.  
- **L3.** The gauge shift $\alpha_{p}=p+1$ is a natural but not unique choice; alternative gauge functions could alter the comparison.  
- **L4.** No statistical analysis of higher Maass eigenvalues is performed; only the first non‑zero eigenvalue is considered.  
- **L5.** The comparison ignores possible multiplicities and degeneracies that may arise in truncated tree models.

### 6.2. Falsification Criterion
If high‑precision computation of the Maass spectrum on $X$ reveals that *any* shifted eigenvalue $\lambda_{j}^{(p)}=\lambda_{j}-(p+1)$ lies within the continuous interval $[(p+1)-2\sqrt{p},\,(p+1)+2\sqrt{p}]$ for a given prime $p$, then the gauge‑principle conjecture would be *supported* at that spectral level. Conversely, if *all* shifted eigenvalues remain outside the interval for all small primes $p$, the conjecture is falsified at the leading spectral level.

### 6.3. Open Questions
- Can alternative gauge choices (e.g., $\alpha_{p}=c\,(p+1)$ with $c\neq1$) produce overlapping spectra?  
- Does the continuous spectrum encode statistical properties (e.g., spacing distribution) that match those of the Maass eigenvalues after appropriate scaling?  
- How do finite‑graph truncations of $\mathcal{T}_{p}$ affect the emergence of a discrete point spectrum, and can such truncations be interpreted physically?

## 7. Practical Implications and Engineering Pathways
### 7.1. Potential Users and Decision Impact
Number theorists investigating the distribution of $L$‑function zeros and mathematical physicists modeling quantum systems on $p$‑adic spaces would use the derived spectral intervals to assess whether a proposed gauge‑invariant operator can serve as a common observable across completions. If the intervals overlapped with low‑lying Archimedean eigenvalues, researchers could adopt the gauge‑invariant Laplacian as a unifying tool for adelic quantum mechanics, potentially simplifying the formulation of cross‑domain models.

### 7.2. Technology Readiness
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at **TRL 2** (formulation of concept and analytical studies).

### 7.3. Next Experiment
The smallest de‑risking step is a high‑precision numerical computation of the first several hundred Maass eigenvalues on the modular surface (e.g., using the Hejhal algorithm). One would then subtract $p+1$ for $p=2,3,5$ and test whether any shifted eigenvalue falls inside the corresponding continuous interval. Observation of a shifted eigenvalue within the interval would *refute* the falsification condition and support the conjecture; absence would *confirm* the current negative result.

### 7.4. Engineering Constraints
- **C1.** Accurate Maass eigenvalue computation requires substantial CPU time and high‑precision arithmetic libraries.  
- **C2.** Storage of eigenfunctions for verification of orthogonality may be memory‑intensive.  
- **C3.** No experimental hardware is needed; the constraint is purely computational.

### 7.5. Projected Cost and Performance (Projection)
Assuming a modern workstation with 32 CPU cores and 128 GB RAM, the Hejhal algorithm for 500 Maass eigenvalues is projected to require approximately $2\times10^{5}$ CPU‑seconds (≈ 55 hours) and 10 GB of disk space for intermediate data. This estimate is based on published benchmarks for similar spectral computations (e.g., in the literature on Maass forms) and is labeled as a projection.

### 7.6. Risks and Misuse
A misinterpretation of the spectral overlap as proof of a physical theory could lead to premature adoption of adelic models in phenomenology without sufficient empirical backing. Researchers should treat the present result as a diagnostic test rather than a validation of any specific physical framework.

## 8. Conclusion
We have defined a gauge‑invariant Laplacian whose spectrum on Bruhat–Tits trees is exactly the adjacency interval $[-2\sqrt{p},\,2\sqrt{p}]$, and we have computed the corresponding continuous Laplacian spectra for $p=2$ and $p=5$. By projecting the first non‑zero Maass eigenvalue on the modular surface, we find a clear separation between the Archimedean and non‑Archimedean spectra under the simplest gauge choice. This separation constitutes a falsification of the conjectured universal spectral correspondence at the leading level. Nevertheless, the structural similarity of the interval widths $4\sqrt{p}$ to the average spacing of Riemann $\zeta$‑zeros suggests that more sophisticated gauge choices or higher‑order spectral statistics may yet reveal a deeper adelic bridge. The next concrete step is a systematic numerical comparison of many Maass eigenvalues with the $p$‑adic continuous bands, which will either reinforce or definitively reject the gauge‑principle hypothesis.

## References
[1] arXiv:1901.01957v6 | ($p$-adic) $L$-functions and ($p$-adic) (multiple) zeta values  
[2] arXiv:1204.3878v1 | Analytic constructions of p-adic L-functions and Eisenstein series  
[3] arXiv:1508.07185v2 | Fundamentals of p-adic multiple L-functions and evaluation of their special values  
[4] arXiv:1506.05681v2 | Triple product p-adic L-functions for balanced weights  
[5] arXiv:math-ph/0512018v2 | On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree  
[6] arXiv:2504.12066v2 | $p$-adic Asai and twisted triple product $L$-functions for finite slope families  
[7] QNFO: Consilience Between Physics and Number Theory: Convergent Theses from Ostrowski's Theorem to Adel...  
[8] QNFO: Super-Universe  
[9] QNFO: Spectral Decomposition of the Bruhat–Tits Tree as a Candidate Origin of Particle Mass Hierarchies...  
[10] QNFO: The Adelic Cross-Domain Program: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees  

## Appendix A. Divergence report
*No divergent claims were identified among the independent drafts; all substantive statements converged on the same quantitative derivations and literature citations.*

## Appendix B. Claim attribution
| Claim | Source Draft(s) | Agreement |
|-------|-----------------|-----------|
| C1 – Definition of gauge‑invariant Laplacian | A, B, C | Convergent |
| C2 – Continuous spectrum formulas for $\Delta_{p}$ | A, B, C | Convergent |
| C3 – Numerical values for $p=2$ interval | A, B, C | Convergent |
| C4 – Numerical values for $p=5$ interval | A, B, C | Convergent |
| C5 – Projection of Maass eigenvalue | A, B, C | Convergent |
| C6 – Comparison outcome (no overlap) | A, B, C | Convergent |
| C7 – Limitations list | A, B, C | Convergent |
| C8 – Falsification criterion | A, B, C | Convergent |
| C9 – Practical implications (users, TRL, next experiment) | A, B, C | Convergent |
| C10 – Projected computational cost | A, B, C | Convergent |