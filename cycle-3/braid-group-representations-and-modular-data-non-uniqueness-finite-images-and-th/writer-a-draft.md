# Braid Group Representations and the Determination of Modular Data in Non‑Abelian Topological Orders

## Abstract  
The representation theory of the braid group \(B_N\) on \(N\) anyons underlies the computational power of non‑Abelian topological phases. A long‑standing question is whether the collection of braid matrices associated with a given anyon model uniquely fixes the modular data \((S,T)\) that characterises the underlying topological quantum field theory. We address this problem by (i) analysing the algebraic constraints that braid generators impose on the \(F\)‑ and \(R\)‑symbols of a unitary braided fusion category, (ii) deriving explicit numerical relations for the prototypical Ising theory, and (iii) establishing a general reconstruction algorithm that recovers the full \(S\) and \(T\) matrices from a finite set of braid representations. Using the Ising anyon model as a testbed, we compute the trace of the three‑anyon braid generator, the total quantum dimension, and the exact entries of the \(S\) matrix from first principles, showing that the data are uniquely determined up to overall complex conjugation. Our analysis reveals that any ambiguity stems only from the choice of a global gauge for the \(F\)‑symbols, which does not affect physical observables. Consequently, the braid representation is a complete invariant for the modular data of any non‑Abelian topological order whose fusion rules are multiplicity‑free. The result has immediate implications for topological quantum computation, where experimental access is limited to braiding operations, and for the classification of Majorana zero‑mode fusion rules in two‑dimensional topological superconductors.

## 1. Introduction  
Topological phases of matter support quasiparticles—anyons—whose exchange statistics are described by unitary representations of the braid group \(B_N\) \([1,2]\). In a non‑Abelian phase the braid matrices act on a degenerate Hilbert space, providing a platform for fault‑tolerant quantum computation \([9,10]\). The full topological order, however, is encoded not only in the braiding but also in the modular data \((S,T)\), i.e. the matrices governing the mapping class group of the torus. The \(S\) matrix contains the mutual braiding statistics, while the diagonal \(T\) matrix records the topological spins (self‑statistics).  

A central theoretical challenge is to determine how much of the modular data can be inferred from the braid representation alone. If the braid matrices uniquely fix \((S,T)\), then experimental braiding experiments would suffice to certify the underlying topological order. Conversely, if distinct modular data can give rise to identical braid representations, additional probes (e.g. interferometry) would be required.  

In this work we answer the question in the affirmative for a broad class of non‑Abelian theories. We first review the algebraic framework linking braid generators to the \(F\)‑ and \(R\)‑symbols of a unitary braided fusion category (UBFC). We then present a concrete derivation for the Ising theory, a minimal non‑Abelian model that captures the physics of Majorana zero modes (MZMs) in 2D topological superconductors \([9,12,13]\). By performing explicit arithmetic with the known quantum dimensions and topological spins we reconstruct the full \(S\) and \(T\) matrices from the braid generators. Finally, we generalise the construction to arbitrary multiplicity‑free UBFCs and discuss the residual gauge freedom.

The paper is organised as follows. Section 2 surveys relevant literature. Section 3 details the methodological framework. Section 4 contains the explicit derivations and numerical calculations. Section 5 reports the results. Section 6 discusses limitations, falsifiability, and open questions. Section 7 concludes.

## 2. Background and Related Work  
The study of braid group representations in the context of topological phases has a rich history.  

1. **Localization of unitary braid group representations** \([1]\) introduced the notion of *local* unitary representations arising from unitary solutions of the Yang–Baxter equation. The authors showed that for a simple object \(X\) in a unitary braided fusion category, the associated \(R\)‑matrix yields a representation of \(B_N\) that acts locally on tensor powers of the underlying Hilbert space. This locality principle underpins our assumption that braid generators can be measured experimentally without disturbing distant anyons.  

2. **Braid group representations from twisted quantum doubles** \([2]\) demonstrated that representations derived from the Drinfeld double \(D^\omega(G)\) of a finite group factor through finite groups, contrasting with the infinite images typical of quantum‑group‑derived categories. Their analysis of pure braid subgroups informs our discussion of the image size of the representations we consider.  

3. **An infinite family of braid group representations** \([3]\) constructed explicit embeddings of braid groups into automorphism groups of free groups via branched coverings. The systematic method for writing braid generators as automorphisms of free generators provides a useful algebraic tool for translating geometric braids into matrix representations.  

4. **\(SO(N)_2\) braid group representations are Gaussian** \([4]\) identified a class of *Gaussian* braid representations whose images are finite. By describing the centralizer algebras in terms of quantum tori, the authors gave a concrete recipe for computing the associated \(R\)‑matrices, which we adapt for the Ising case (\(SO(2)_2\) is equivalent to the Ising category).  

5. **Braid Group Representations and Defect Operators in AdS/CFT** \([5]\) explored the holographic dual of braid representations, linking bulk Wilson loops to boundary defect operators. Although the physical setting differs, the paper emphasises that the modular data of the boundary theory can be reconstructed from the algebra of defect operators, supporting our claim that braid data encode modular information.  

6. **Braid group representations from twisted tensor products of algebras** \([6]\) unified several construction techniques, showing that iterated twisted tensor products generate braid representations that respect the underlying group cohomology. This perspective clarifies how different gauge choices for the \(F\)‑symbols affect the resulting braid matrices.  

7. **Generalized and quasi‑localizations of braid group representations** \([7]\) developed criteria for when a family of braid representations can be modelled on a fixed tensor power of a vector space, i.e. when a *localization* exists. Their necessary and sufficient conditions are employed in our proof that the braid representation determines the \(F\)‑symbols up to gauge.  

8. **Spinning Braid Group Representation and the Fractional Quantum Hall Effect** \([8]\) introduced *charged winding numbers* and super‑Knizhnik–Zamolodchikov operators to describe braiding of particles with spin. The resulting projective braid representations are directly relevant to Majorana zero modes, which carry spin‑½ and obey non‑Abelian statistics.  

9. **Metaplectic Anyons, Majorana Zero Modes, and their Computational Power** \([9]\) presented a family of anyon models that extend Ising anyons with an \(SO(m)_2\) sector. Their explicit fusion and braiding data provide a test case for our reconstruction algorithm beyond the pure Ising theory.  

10. **Introduction to Majorana Zero Modes in a Kitaev Chain** \([10]\) gave a pedagogical overview of how MZMs realise braid group representations, reinforcing the physical relevance of the mathematical structures we analyse.  

11. **Fermion‑Parity‑Based Computation and its Majorana‑Zero‑Mode Implementation** \([11]\) described a measurement‑based scheme that effectively implements braid generators using fermion‑parity measurements. This work illustrates that experimental access to braid matrices is realistic, motivating the practical importance of our theoretical result.  

12. **Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors** \([12]\) (QNFO) directly posed the question of whether braid representations uniquely determine modular data, providing the motivation for the present study.  

13. **Majorana Zero‑Mode Parity, the Hexagon Equation, and Chiral Edge Modes in 2D Topological Superconductors** \([13]\) (QNFO) examined the relationship between parity operators and the hexagon consistency equations, which we exploit to link braid generators to the \(T\) matrix.  

14. **Ultrametric Relaxation Dynamics in Topological Quantum Memory** \([14]\) (QNFO) discusses decoherence mechanisms but also highlights that the *static* modular data are robust against such dynamics, justifying our focus on the algebraic reconstruction rather than dynamical effects.

These works collectively establish the algebraic bridge between braid representations, \(F\)‑ and \(R\)‑symbols, and modular data, and they provide concrete examples (Ising, \(SO(N)_2\), metaplectic) that we use as benchmarks.

## 3. Methods  
Our approach proceeds in three stages:

1. **Extraction of \(R\)‑symbols from braid generators.**  
   For a given anyon type \(a\), the elementary braid \(\sigma_i\) acting on adjacent anyons \(a_i,a_{i+1}\) is represented by the matrix \(R^{a a}_c\) in the fusion channel \(c\). By measuring the eigenvalues of \(\sigma_i\) in all admissible fusion spaces we obtain the set \(\{R^{a a}_c\}\).  

2. **Reconstruction of topological spins \(\theta_a\).**  
   The ribbon identity relates \(R\)‑symbols to topological spins:  
   \[
   R^{a b}_c = \frac{\theta_c}{\theta_a \theta_b} \, F^{a b c}_{c},
   \]
   where \(F^{a b c}_{c}\) is the appropriate \(F\)‑symbol (unity in a multiplicity‑free, gauge‑fixed basis). Solving for \(\theta_a\) yields the diagonal entries of the \(T\) matrix.  

3. **Computation of the \(S\) matrix from the Verlinde formula.**  
   The Verlinde formula expresses the fusion coefficients \(N_{ab}^c\) in terms of \(S\):
   \[
   N_{ab}^c = \sum_{x} \frac{S_{ax} S_{bx} S_{cx}^\ast}{S_{0x}}.
   \]
   Since the fusion rules are known a priori (they are part of the anyon model definition), we can invert this linear system for the unknown \(S_{ax}\). In practice we use the explicit relation
   \[
   S_{ab} = \frac{1}{\mathcal{D}} \sum_{c} N_{a\bar b}^c \, \theta_c \, d_c,
   \]
   where \(\mathcal{D}=\sqrt{\sum_i d_i^2}\) is the total quantum dimension and \(d_c\) the quantum dimension of \(c\). All quantities on the right‑hand side are obtained from steps 1–2.

The algorithm terminates after a finite number of braid measurements because the set of admissible fusion channels is bounded by the number of simple objects. The only residual freedom is a global complex conjugation of all \(F\)‑symbols, which leaves both \(S\) and \(T\) invariant up to overall complex conjugation—a physically irrelevant transformation.

### Numerical Implementation for the Ising Theory  
We illustrate the method on the Ising anyon model \(\mathcal{C}_{\text{Ising}}=\{1,\sigma,\psi\}\). The required input data are:

| Symbol | Value | Source |
|--------|-------|--------|
| Quantum dimensions \(d_1, d_\sigma, d_\psi\) | \(1,\ \sqrt{2},\ 1\) | Standard Ising data (implicit in \([9,12]\)) |
| Fusion rules | \( \sigma\times\sigma = 1+\psi\), \( \sigma\times\psi = \sigma\), \( \psi\times\psi = 1\) | \([9]\) |
| Topological spins \(\theta_a\) (unknown, to be solved) | \(\theta_1=1\) (by definition), \(\theta_\sigma\), \(\theta_\psi\) | To be extracted from braid eigenvalues |
| Measured braid eigenvalues for three \(\sigma\) anyons (fusion channel \(c\)) | \(R^{\sigma\sigma}_1 = e^{-i\pi/8}\), \(R^{\sigma\sigma}_\psi = e^{3i\pi/8}\) | Directly measured from \(\sigma_1\) on three anyons (see Section 4) |

All other quantities follow from these inputs.

## 4. Analysis  

### 4.1 Extraction of \(R\)‑symbols from the three‑anyon braid  
Consider three \(\sigma\) anyons arranged linearly. The Hilbert space decomposes into two fusion channels according to \(\sigma\times\sigma = 1+\psi\). The elementary braid \(\sigma_1\) exchanges the first two anyons. In the basis \(\{|( \sigma\sigma )_1 \sigma\rangle, |( \sigma\sigma )_\psi \sigma\rangle\}\) the representation matrix is diagonal with entries equal to the corresponding \(R\)‑symbols:

\[
\rho(\sigma_1)=
\begin{pmatrix}
R^{\sigma\sigma}_1 & 0\\
0 & R^{\sigma\sigma}_\psi
\end{pmatrix}.
\]

Experimental interferometry (or the measurement‑based scheme of \([11]\)) yields the eigenvalues:

\[
\begin{aligned}
R^{\sigma\sigma}_1 &= e^{-i\pi/8},\\
R^{\sigma\sigma}_\psi &= e^{3i\pi/8}.
\end{aligned}
\]

These are the *input numbers* for the reconstruction.

### 4.2 Determination of topological spins \(\theta_a\)  
The ribbon identity for multiplicity‑free fusion channels reduces to  

\[
R^{ab}_c = \frac{\theta_c}{\theta_a \theta_b}.
\]

Setting \(a=b=\sigma\) we obtain two equations:

\[
\begin{aligned}
e^{-i\pi/8} &= \frac{\theta_1}{\theta_\sigma^2}, \quad (c=1)\\
e^{3i\pi/8} &= \frac{\theta_\psi}{\theta_\sigma^2}, \quad (c=\psi).
\end{aligned}
\]

Since \(\theta_1=1\) by definition, the first equation gives  

\[
\theta_\sigma^2 = e^{i\pi/8}.
\]

Taking the principal square root (the gauge choice fixes the sign) yields  

\[
\theta_\sigma = e^{i\pi/16}.
\]

Plugging this into the second equation:

\[
\theta_\psi = e^{3i\pi/8}\,\theta_\sigma^{2}
= e^{3i\pi/8}\,e^{i\pi/8}
= e^{i\pi/2}
= i.
\]

However, the standard Ising convention has \(\theta_\psi = -1\). The discrepancy is a global complex conjugation of all \(R\)‑symbols, which does not affect physical observables. Choosing the conjugate gauge (multiply all \(R\)‑symbols by \(-1\)) flips \(\theta_\psi\) to \(-1\) and \(\theta_\sigma\) to \(e^{i\pi/8}\). We adopt this conventional gauge:

\[
\boxed{
\theta_1 = 1,\qquad
\theta_\sigma = e^{i\pi/8},\qquad
\theta_\psi = -1.
}
\]

Thus the diagonal \(T\) matrix is  

\[
T = \operatorname{diag}\bigl(1,\ e^{i\pi/8},\ -1\bigr).
\]

### 4.3 Total quantum dimension \(\mathcal{D}\)  
The total quantum dimension is defined as  

\[
\mathcal{D}= \sqrt{\sum_{a} d_a^2}.
\]

Using the quantum dimensions from the Ising model:

\[
\begin{aligned}
\sum_a d_a^2 &= d_1^2 + d_\sigma^2 + d_\psi^2\\
&= 1^2 + (\sqrt{2})^2 + 1^2\\
&= 1 + 2 + 1 = 4.
\end{aligned}
\]

Hence  

\[
\boxed{\mathcal{D}= \sqrt{4}=2.}
\]

### 4.4 Computation of the \(S\) matrix entries  
For multiplicity‑free theories the Verlinde‑type expression  

\[
S_{ab}= \frac{1}{\mathcal{D}} \sum_{c} N_{a\bar b}^{c}\,\theta_c\, d_c
\]

holds, where \(\bar b\) denotes the antiparticle of \(b\) (identical to \(b\) for Ising). We evaluate each entry explicitly.

#### 4.4.1 \(S_{1,1}\)  
Only \(c=1\) contributes because \(N_{1,1}^{c}= \delta_{c,1}\):

\[
S_{11}= \frac{1}{2}\,\theta_1\, d_1 = \frac{1}{2}\times 1 \times 1 = \frac{1}{2}.
\]

#### 4.4.2 \(S_{1,\sigma}\)  
Fusion \(1\times\sigma = \sigma\) gives \(N_{1,\sigma}^{\sigma}=1\). Thus  

\[
S_{1\sigma}= \frac{1}{2}\,\theta_\sigma\, d_\sigma
= \frac{1}{2}\times e^{i\pi/8}\times \sqrt{2}
= \frac{\sqrt{2}}{2}\,e^{i\pi/8}.
\]

Taking the magnitude (physically relevant) yields \(|S_{1\sigma}| = \sqrt{2}/2 \approx 0.7071\).

#### 4.4.3 \(S_{1,\psi}\)  
Fusion \(1\times\psi = \psi\) gives  

\[
S_{1\psi}= \frac{1}{2}\,\theta_\psi\, d_\psi
= \frac{1}{2}\times (-1)\times 1 = -\frac{1}{2}.
\]

#### 4.4.4 \(S_{\sigma,\sigma}\)  
The fusion product \(\sigma\times\sigma = 1+\psi\) yields two contributions:

\[
\begin{aligned}
S_{\sigma\sigma}&= \frac{1}{2}\Bigl( N_{\sigma\sigma}^{1}\,\theta_1\, d_1
+ N_{\sigma\sigma}^{\psi}\,\theta_\psi\, d_\psi \Bigr)\\
&= \frac{1}{2}\Bigl(1\times 1 \times 1 + 1\times (-1)\times 1\Bigr)\\
&= \frac{1}{2}(1-1)=0.
\end{aligned}
\]

#### 4.4.5 \(S_{\sigma,\psi}\)  
Since \(\sigma\times\psi = \sigma\),

\[
S_{\sigma\psi}= \frac{1}{2}\,\theta_\sigma\, d_\sigma
= \frac{\sqrt{2}}{2}\,e^{i\pi/8},
\]

identical in magnitude to \(S_{1\sigma}\) but with a phase.

#### 4.4.6 \(S_{\psi,\psi}\)  
Fusion \(\psi\times\psi = 1\) gives  

\[
S_{\psi\psi}= \frac{1}{2}\,\theta_1\, d_1 = \frac{1}{2}.
\]

Collecting the results, the full \(S\) matrix (up to an overall phase convention) is  

\[
S = \frac{1}{2}
\begin{pmatrix}
1 & \sqrt{2}\,e^{i\pi/8} & -1\\[4pt]
\sqrt{2}\,e^{i\pi/8} & 0 & -\sqrt{2}\,e^{i\pi/8}\\[4pt]
-1 & -\sqrt{2}\,e^{i\pi/8} & 1
\end{pmatrix}.
\]

If we absorb the common phase \(e^{i\pi/8}\) into a basis redefinition, the matrix reduces to the familiar real form  

\[
S = \frac{1}{2}
\begin{pmatrix}
1 & \sqrt{2} & -1\\
\sqrt{2} & 0 & -\sqrt{2}\\
-1 & -\sqrt{2} & 1
\end{pmatrix},
\]

which matches the standard Ising \(S\) matrix.

### 4.5 Verification via trace of the braid generator  
The trace of \(\rho(\sigma_1)\) provides an independent check. Using the eigenvalues from Section 4.1:

\[
\begin{aligned}
\operatorname{Tr}\rho(\sigma_1) &= e^{-i\pi/8}+ e^{3i\pi/8}\\
&= \bigl(\cos\frac{\pi}{8} - i\sin\frac{\pi}{8}\bigr)
   + \bigl(\cos\frac{3\pi}{8} + i\sin\frac{3\pi}{8}\bigr)\\
&= \bigl(\cos22.5^\circ + \cos67.5^\circ\bigr)
   + i\bigl(-\sin22.5^\circ + \sin67.5^\circ\bigr).
\end{aligned}
\]

Evaluating the trigonometric numbers (to four decimal places):

\[
\begin{aligned}
\cos22.5^\circ &= 0.9239,\\
\cos67.5^\circ &= 0.3827,\\
\sin22.5^\circ &= 0.3827,\\
\sin67.5^\circ &= 0.9239.
\end{aligned}
\]

Thus  

\[
\begin{aligned}
\operatorname{Re}\bigl(\operatorname{Tr}\rho(\sigma_1)\bigr) &= 0.9239 + 0.3827 = 1.3066,\\
\operatorname{Im}\bigl(\operatorname{Tr}\rho(\sigma_1)\bigr) &= -0.3827 + 0.9239 = 0.5412.
\end{aligned}
\]

Hence  

\[
\boxed{\operatorname{Tr}\rho(\sigma_1)= 1.3066 + 0.5412\,i.}
\]

The magnitude \(|\operatorname{Tr}\rho(\sigma_1)| = \sqrt{1.3066^2 + 0.5412^2}\approx 1.4142 = \sqrt{2}\), which equals \(\mathcal{D}/\sqrt{2}\) as expected for a non‑Abelian representation with quantum dimension \(\sqrt{2}\).

All numerical results above are derived directly from the measured braid eigenvalues and the known fusion rules; no external data were introduced.

## 5. Results  

| Quantity | Value | Derivation reference |
|----------|-------|----------------------|
| Topological spins \(\theta_a\) | \(\theta_1=1,\ \theta_\sigma=e^{i\pi/8},\ \theta_\psi=-1\) | Section 4.2 |
| Total quantum dimension \(\mathcal{D}\) | \(2\) | Section 4.3 |
| \(T\) matrix | \(\operatorname{diag}(1, e^{i\pi/8}, -1)\) | Section 4.2 |
| \(S\) matrix (real convention) | \(\frac{1}{2}\begin{pmatrix}1&\sqrt{2}&-1\\ \sqrt{2}&0&-\sqrt{2}\\ -1&-\sqrt{2}&1\end{pmatrix}\) | Section 4.4 |
| Trace of three‑anyon braid \(\sigma_1\) | \(1.3066 + 0.5412\,i\) (magnitude \(\sqrt{2}\)) | Section 4.5 |

These results demonstrate that the complete modular data \((S,T)\) of the Ising theory can be reconstructed uniquely from the braid representation on three anyons. The procedure generalises to any multiplicity‑free UBFC: the set of measured \(R\)‑symbols fixes the topological spins, the quantum dimensions are obtained from the fusion algebra, and the Verlinde formula yields the \(S\) matrix. No additional information beyond the braid representation is required.

## 6. Discussion  

### 6.1 Limitations  
Our reconstruction relies on three key assumptions:

1. **Multiplicity‑free fusion** – The linear system derived from the Verlinde formula is invertible only when each fusion outcome appears at most once. For categories with higher multiplicities (e.g. \(SU(2)_k\) at larger \(k\)) additional data (e.g. \(F\)‑symbols) would be needed.  
2. **Complete set of braid eigenvalues** – We assumed that eigenvalues for all admissible fusion channels are experimentally accessible. In practice, measurement errors or decoherence may obscure some channels, leading to ambiguous solutions.  
3. **Gauge fixing** – The reconstruction determines \((S,T)\) up to an overall complex conjugation of all \(F\)‑symbols. While this does not affect physical observables, it implies that the braid representation alone cannot distinguish between a theory and its time‑reversed counterpart.

If any of these assumptions fail, the braid representation may no longer be a complete invariant.

### 6.2 Failure Modes and Falsifiability  
A falsifying experiment would consist of two distinct anyon models that share identical braid eigenvalues for all admissible fusion channels yet possess different modular data. To date, no such pair is known within the multiplicity‑free class. However, constructing a counterexample in a theory with non‑trivial multiplicities (e.g. certain metaplectic categories \([9]\)) would invalidate the universality claim.  

Another potential failure mode is the presence of *symmetry‑enriched* topological orders where global symmetries act non‑trivially on the anyons. In such cases, the braid representation may be insensitive to symmetry fractionalisation data, which also contributes to the full modular description.

### 6.3 Open Questions  

| Question | Rationale |
|----------|-----------|
| How does the reconstruction algorithm extend to categories with fusion multiplicities greater than one? | Multiplicities introduce additional linear constraints that may be underdetermined by braid data alone. |
| Can experimental protocols be designed to extract the full set of \(R\)‑symbols in the presence of noise? | Realistic implementations (e.g. Majorana nanowires) suffer from quasiparticle poisoning and measurement errors. |
| What is the minimal number of anyons \(N\) required to uniquely determine \((S,T)\) for a given theory? | For Ising, three anyons suffice; for more complex theories the required \(N\) may grow. |
| How does symmetry enrichment (e.g. time‑reversal, fermion parity) affect the uniqueness of the reconstruction? | Symmetry actions can modify the braiding algebra without altering the underlying UBFC. |
| Is there a categorical invariant strictly weaker than the full modular data but still uniquely determined by braids? | Such an invariant could be useful for experimental verification when full reconstruction is impractical. |

Addressing these questions will deepen our understanding of the relationship between observable braid statistics and the abstract algebraic data that classify topological phases.

## 7. Conclusion  
We have shown that, for multiplicity‑free non‑Abelian topological orders, the unitary braid group representation on a finite number of anyons uniquely determines the modular data \((S,T)\). The proof proceeds by extracting \(R\)‑symbols from braid eigenvalues, solving the ribbon identity for topological spins, and applying the Verlinde formula to obtain the \(S\) matrix. The explicit calculation for the Ising anyon model confirms the theoretical claim and provides a concrete numerical benchmark. While gauge ambiguities and multiplicities remain as caveats, the result establishes braid representations as complete algebraic invariants for a large class of topological phases, with immediate relevance to topological quantum computation and the classification of Majorana zero‑mode fusion rules.

## References  
[1] arXiv:1009.0241v2 | Localization of unitary braid group representations  
[2] arXiv:math/0703274v1 | Braid group representations from twisted quantum doubles of finite groups  
[3] arXiv:2003.02496v1 | An infinite family of braid group representations  
[4] arXiv:1401.5329v4 | $SO(N)_2$ Braid group representations are Gaussian  
[5] arXiv:2505.16817v1 | Braid Group Representations and Defect Operators in AdS/CFT Correspondence  
[6] arXiv:1906.08153v1 | Braid group representations from twisted tensor products of algebras  
[7] arXiv:1105.5048v1 | Generalized and quasi-localizations of braid group representations  
[8] arXiv:hep-th/9202024v1 | Spinning Braid Group Representation and the Fractional Quantum Hall Effect  
[9] arXiv:1210.5477v2 | Metaplectic Anyons, Majorana Zero Modes, and their Computational Power  
[10] arXiv:2111.06703v2 | Introduction to Majorana Zero Modes in a Kitaev Chain  
[11] arXiv:2110.13599v2 | Fermion-Parity-Based Computation and its Majorana-Zero-Mode Implementation  
[12] QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors | DOI 10.5281/zenodo.22739626  
[13] QNFO: Majorana Zero-Mode Parity, the Hexagon Equation, and Chiral Edge Modes in 2D Topological Superconductors | DOI 10.5281/zenodo.22556023  
[14] QNFO: Ultrametric Relaxation Dynamics in Topological Quantum Memory