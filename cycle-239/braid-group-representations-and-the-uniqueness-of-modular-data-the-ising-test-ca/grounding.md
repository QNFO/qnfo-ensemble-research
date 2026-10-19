# Grounding block - source: rem-rev-06ca4cbf-5176-4281-8cd0-2626d6681852

## Research idea

Re-entry from 10.5281/zenodo.23086421: Does the braid group representation on $N$ anyons uniquely determine the modular data — the $S$ and $T$ matrices — of the non-Abelian topological order?

Post-publication revision of the published paper "Braid Group Representations and the Uniqueness of Modular Data: The Ising Test Case and General Limitations" (version 1.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

## Existing paper under revision (remediation only)

# Braid Group Representations and the Uniqueness of Modular Data: The Ising Test Case and General Limitations

## Abstract
We investigate whether the unitary braid group representation carried by a collection of non‑Abelian anyons uniquely determines the modular data—namely the $S$ and $T$ matrices—of the underlying modular tensor category (MTC). Using the Ising anyon theory as a concrete laboratory, we reconstruct the full modular data from the elementary braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ together with the fusion rule $\sigma\times\sigma=1+\psi$. Explicit arithmetic yields the quantum dimension $d_{\sigma}=\sqrt{2}\approx1.4142$, the total quantum dimension $D=2$, the $S$‑entry $S_{\sigma 1}= \sqrt{2}/2\approx0.7071$, the vanishing diagonal $S_{\sigma\sigma}=0$, and the $T$‑entry $T_{\sigma\sigma}=e^{i\pi/8}\approx0.9239+0.3827\,i$. We also compute the fusion‑space dimensions $f(n,1)=2^{n/2-1}$ for even $n$, and the braid generator’s ordinary order $16$ (projective order $4$). By contrasting these positive results with families of braid representations that have finite image—twisted quantum doubles, Gaussian $SO(N)_2$ representations, and infinite non‑geometric embeddings—we formulate a **partial uniqueness theorem**: dense braid images determine $(S,T)$ up to a global phase, whereas finite braid images leave essential ambiguities. The analysis clarifies the informational content of braiding experiments in Majorana‑based platforms and delineates the need for complementary probes when braid images are non‑dense.

## 1. Introduction
Topological phases of matter support anyonic excitations whose adiabatic exchange is described by a unitary representation of the braid group $B_N$ \[1\]. An MTC encodes the full topological data in its modular $S$ and $T$ matrices, which together determine fusion rules, quantum dimensions, and braiding phases \[12\]. A central question—explicitly raised in recent QNFO reports \[13,14\]—is whether the braid representation on $N$ anyons suffices to reconstruct $S$ and $T$ uniquely.

The practical relevance is immediate: experimental platforms based on Majorana zero modes (MZMs) implement projective braid operations \[13\]; if these operations uniquely fix the modular data, braiding alone could certify the underlying topological order. Conversely, if distinct MTCs share identical braid images, additional probes (e.g., interferometry) would be required.

In this work we (i) formulate a concrete reconstruction pipeline for $S$ and $T$ from braid generators, (ii) apply it to the Ising anyon model, (iii) compute auxiliary quantities (fusion‑space dimensions, braid order), and (iv) analyze broader families of braid representations from the literature to delineate when uniqueness holds. Section 2 surveys relevant prior results, Section 3 details the methodology, Section 4 presents explicit derivations, Section 5 reports the numerical outcomes, Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work
Unitary braid group representations derived from solutions of the Yang–Baxter equation have been studied extensively.

* **Localization of unitary braid group representations** \[1\] connects unitary $R$‑matrices to simple objects in unitary braided fusion categories, establishing locality constraints essential for topological quantum computation.
* **Twisted quantum doubles** \[2\] show that braid representations arising from finite groups always factor through finite groups, implying that the image of $B_N$ can be too small to capture full modular data.
* **Gaussian $SO(N)_2$ representations** \[3\] prove that braid representations on tensor powers of the spin object are Gaussian with finite image, limiting the information content of the braid group alone.
* **Infinite non‑geometric braid embeddings** \[4\] construct an infinite family of braid representations via $d$‑fold branched coverings, demonstrating that braid images can be highly non‑universal.
* **Twisted tensor product constructions** \[5\] illustrate how gauging a pointed modular category can change modular data while preserving braid representations on the ungauged sector.
* **Defect‑operator analyses in AdS/CFT** \[6\] connect braid group representations to holographic defect operators, emphasizing that braid data and modular data are related but not identical.
* **Spinning braid representations in the fractional quantum Hall effect** \[7\] generalize braid representations to particles with spin, showing that additional algebraic data (e.g., spin structures) lie beyond the braid group.
* **Generalized and quasi‑localizations** \[8\] emphasize the role of additional algebraic data (e.g., $F$‑symbols) beyond the braid group for reconstructing full modular data.
* **Classical meta‑material realizations of non‑Abelian defects** \[9\] provide experimental platforms where braid representations are accessible but modular data may remain hidden.
* **Extended chiral $su(2)$ WZNW model** \[10\] offers a theoretical arena where fusion rings, braid operators, and modular data can be compared term by term.
* **Anyonic tensor‑network simulations** \[11\] enable numerical extraction of $S$ and $T$, yet these methods rely on explicit knowledge of the underlying MTC.

Collectively, these works suggest that while braid representations are a necessary ingredient, they are not universally sufficient for reconstructing modular data. Our contribution is to make this statement precise for a representative set of models.

## 3. Methods
Our reconstruction proceeds in three steps:

1. **Extract braid eigenvalues.** For a simple object $a$, the elementary braid generator $R_{aa}$ acts on the two‑anyon Hilbert space $V_{aa}=\bigoplus_c N_{aa}^c\,V_c$ with eigenvalues $\theta_c/\theta_a$, where $\theta_x$ denotes the topological spin of $x$ \[12\].

2. **Determine quantum dimensions.** The quantum dimension $d_a$ follows from the trace of the braid representation on $V_{aa}$:
 $$
 \operatorname{Tr}(R_{aa}) = \sum_c N_{aa}^c \frac{\theta_c}{\theta_a} d_c .
 $$
 Solving this linear system yields the total quantum dimension $D=\sqrt{\sum_x d_x^2}$.

3. **Construct $S$ and $T$.** The $T$ matrix is diagonal with entries $T_{aa}= \theta_a$. The $S$ matrix obeys the Verlinde formula
 $$
 N_{ab}^c = \sum_x \frac{S_{ax} S_{bx} S_{cx}^\ast}{S_{1x}} ,
 $$
 which can be inverted to obtain $S_{ax}= \frac{d_a d_x}{D}\, \frac{\theta_a \theta_x}{\theta_{a\otimes x}}$ for Abelian fusion channels. For non‑Abelian channels we use the orthonormality condition
 $$
 \sum_x S_{ax} S_{bx}^\ast = \delta_{ab}.
 $$

We apply this pipeline to the Ising MTC, whose braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ is experimentally accessible in Majorana platforms \[13\]. The fusion rules are $\sigma\times\sigma=1+\psi$, with $1$ and $\psi$ Abelian.

## 4. Analysis
### 4.1 Input data
| Symbol | Meaning | Value | Source |
|--------|---------|-------|--------|
| $R_{\sigma\sigma}$ | Braid eigenvalue for two $\sigma$ anyons | $e^{-i\pi/8}$ | \[13\] |
| $\theta_1$ | Topological spin of vacuum | $1$ | definition |
| $\theta_\psi$ | Topological spin of fermion $\psi$ | $-1$ | \[13\] |
| Fusion rule $\sigma\times\sigma$ | $1+\psi$ | — | \[13\] |
| $d_1$, $d_\psi$ | Quantum dimensions of $1$ and $\psi$ | $1$ each | definition |
| $d_\sigma$ | Quantum dimension of $\sigma$ (unknown) | — | to be solved |
| $N_{\sigma\sigma}^1$, $N_{\sigma\sigma}^\psi$ | Fusion multiplicities | $1$ each | \[13\] |

### 4.2 Determining $d_\sigma$
From the fusion rule,
\[
d_\sigma^2 = \sum_{c} N_{\sigma\sigma}^{c} d_c = N_{\sigma\sigma}^{1} d_1 + N_{\sigma\sigma}^{\psi} d_\psi = 1+1 = 2 .
\]
Hence
\[
d_\sigma = \sqrt{2} \approx 1.4142 .
\]

### 4.3 Total quantum dimension $D$
\[
D = \sqrt{d_1^2 + d_\sigma^2 + d_\psi^2}
 = \sqrt{1^2 + (\sqrt{2})^2 + 1^2}
 = \sqrt{1+2+1}
 = \sqrt{4}
 = 2 .
\]

### 4.4 Computing $T$ from monodromy
The braid eigenvalues on the two fusion channels are
\[
r_1 = e^{-i\pi/8}, \qquad r_\psi = e^{-i\pi/8}\, i = e^{3i\pi/8}.
\]
Monodromy eigenvalues (double braid) are
\[
m_1 = r_1^2 = e^{-i\pi/4}, \qquad
m_\psi = r_\psi^2 = e^{3i\pi/4}.
\]
The ribbon relation $m_c = \theta_c / \theta_\sigma^2$ gives
\[
\theta_\sigma^2 = \frac{1}{m_1} = e^{i\pi/4} \;\Rightarrow\;
\theta_\sigma = e^{i\pi/8},
\]
choosing the principal root (the opposite sign corresponds to the global anomaly discussed in Section 6). The ratio $m_\psi/m_1 = -1$ yields $\theta_\psi = -1$, consistent with a fermion. Thus
\[
T = \operatorname{diag}\bigl(1,\; e^{i\pi/8},\; -1\bigr)
 = \operatorname{diag}\bigl(1,\; 0.9239+0.3827\,i,\; -1\bigr).
\]

### 4.5 Reconstructing $S$ from the Verlinde formula
Using $D=2$ and the known spins, we evaluate each entry.

* $S_{\sigma 1}$ (fusion channel $c=\sigma$):
\[
S_{\sigma 1}= \frac{d_\sigma d_1}{D}
 = \frac{\sqrt{2}\times 1}{2}
 = \frac{\sqrt{2}}{2}
 \approx 0.7071 .
\]

* $S_{\sigma\psi}$ (fusion channel $c=\sigma$):
\[
S_{\sigma\psi}= \frac{d_\sigma d_\psi}{D}\,\frac{\theta_\sigma}{\theta_\sigma\theta_\psi}
 = \frac{\sqrt{2}\times 1}{2}\,\frac{1}{-1}
 = -\frac{\sqrt{2}}{2}
 \approx -0.7071 .
\]

* $S_{\sigma\sigma}$ (channels $c=1,\psi$):
\[
S_{\sigma\sigma}= \frac{1}{D}\!\left(
\frac{\theta_1}{\theta_\sigma^2}d_1
+\frac{\theta_\psi}{\theta_\sigma^2}d_\psi\right)
= \frac{1}{2}\!\left(e^{-i\pi/4}+ \frac{-1}{e^{i\pi/4}}\right)=0 .
\]

* $S_{11}$, $S_{\psi\psi}$, $S_{1\psi}$: for Abelian objects the fusion channel is unique, so the Abelian formula $S_{ax}=\frac{d_a d_x}{D}$ applies with no spin factor. Using the inputs of Section 4.1, $d_1=1$, $d_\psi=1$, and $D=2$ (Section 4.3), each of these entries is
\[
S_{11}= \frac{d_1 d_1}{D} = \frac{1\times 1}{2} = \frac{1}{2}, \qquad
S_{1\psi}= \frac{d_1 d_\psi}{D} = \frac{1\times 1}{2} = \frac{1}{2}, \qquad
S_{\psi\psi}= \frac{d_\psi d_\psi}{D} = \frac{1\times 1}{2} = \frac{1}{2},
\]\nthe same steps as for $S_{\sigma 1}$ in Section 4.5, specialized to Abelian labels.

Arranging rows/columns in the order $(1,\sigma,\psi)$,
\[
S = \frac{1}{2}
\begin{pmatrix}
1 & \sqrt{2} & 1 \\
\sqrt{2} & 0 & -\sqrt{2} \\
1 & -\sqrt{2} & 1
\end{pmatrix}.
\]

All entries satisfy unitarity and the Verlinde eigenvalue relation.

### 4.6 Fusion‑space dimensions for multiple $\sigma$ anyons
Let $f(n,1)$ denote the dimension of the fusion space of $n$ $\sigma$ anyons with total charge $1$. Using the coupled recursion $f(n,1)=f(n-2,1)+f(n-2,\psi)$ and $f(n,\psi)=f(n-2,1)+f(n-2,\psi)$, with base values $f(2,1)=1$ and $f(2,\psi)=1$ (since $\sigma\times\sigma=1+\psi$), we obtain for even $n$: $f(4,1)=f(2,1)+f(2,\psi)=1+1=2$, $f(6,1)=f(4,1)+f(4,\psi)=2+2=4$, $f(8,1)=f(6,1)+f(6,\psi)=4+4=8$, consistent with the closed form
\[
f(n,1)=2^{\,n/2-1}, \qquad n\text{ even}.
\]
Thus $f(2,1)=1$, $f(4,1)=2$, $f(6,1)=4$, $f(8,1)=8$, etc. For odd $n$, $f(n,1)=0$ and $f(n,\sigma)=2^{(n-1)/2}$.

### 4.7 Order of the elementary braid generator
The braid matrix on $V_{\sigma\sigma}$ is
\[
\rho_2(\sigma_1)=e^{-i\pi/8}\begin{pmatrix}1 & 0 \\ 0 & i\end{pmatrix}.
\]
The diagonal part satisfies $\operatorname{diag}(1,i)^4=I$, giving a **projective order** $4$. The overall phase satisfies $(e^{-i\pi/8})^{16}=1$, so the **ordinary order** is $16$:
\[
\rho_2(\sigma_1)^{16}=I_2,\qquad
\rho_2(\sigma_1)^{8}=-I_2 .
\]

### 4.8 Summary of derived quantities
| Quantity | Numerical value | Interpretation |
|----------|----------------|----------------|
| $d_\sigma$ | $\sqrt{2}\approx1.4142$ | Quantum dimension of $\sigma$ |
| $D$ | $2$ | Total quantum dimension |
| $S_{\sigma 1}$ | $0.7071$ | Overlap of $\sigma$ with vacuum |
| $S_{\sigma\psi}$ | $-0.7071$ | Overlap of $\sigma$ with fermion |
| $S_{\sigma\sigma}$ | $0$ | Vanishing diagonal entry |
| $T_{\sigma\sigma}$ | $0.9239+0.3827\,i$ | Topological spin of $\sigma$ |
| $f(n,1)$ (even $n$) | $2^{n/2-1}$ | Fusion‑space dimension |
| $\operatorname{ord}(\rho_2(\sigma_1))$ | $16$ (projective $4$) | Braid generator order |

These values match the canonical Ising modular data \[13\], confirming that the braid eigenvalue alone suffices to reconstruct $S$ and $T$ for this model.

## 5. Results
The explicit arithmetic in Section 4 yields the following concrete numerical results for the Ising anyon theory:

1. **Quantum dimension** $d_\sigma = \sqrt{2}\approx1.4142$.
2. **Total quantum dimension** $D = 2$.
3. **Modular $S$ matrix** (rows/columns ordered $1,\sigma,\psi$):
 $$
 S = \frac{1}{2}
 \begin{pmatrix}
 1 & \sqrt{2} & 1 \\
 \sqrt{2} & 0 & -\sqrt{2} \\
 1 & -\sqrt{2} & 1
 \end{pmatrix},
 $$
 giving $S_{\sigma 1}=0.7071$, $S_{\sigma\psi}=-0.7071$, $S_{\sigma\sigma}=0$.
4. **Modular $T$ matrix**:
 $$
 T = \operatorname{diag}\bigl(1,\; e^{i\pi/8},\; -1\bigr)
 = \operatorname{diag}\bigl(1,\; 0.9239+0.3827\,i,\; -1\bigr).
 $$
5. **Fusion‑space dimensions** $f(n,1)=2^{n/2-1}$ for even $n$.
6. **Braid generator order** ordinary $16$, projective $4$.

All numbers arise directly from the braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ and the fusion rule $\sigma\times\sigma=1+\psi$; no additional simulations were performed.

## 6. Discussion
### 6.1 Scope of uniqueness
Our reconstruction demonstrates that for the Ising MTC the braid representation on two anyons uniquely determines the modular data up to an overall sign of $\theta_\sigma$ (the **global anomaly**). This aligns with the intuition that **dense** braid images—those generating the full unitary group on the fusion space—encode enough information to invert the Verlinde relations.

However, the literature provides numerous counterexamples:

* **Twisted quantum doubles** \[2\] yield braid representations that factor through finite groups, so distinct doubles can share identical braid matrices while possessing different $S$ matrices.
* **Gaussian $SO(N)_2$ representations** \[3\] have finite image; the spin‑object braid representation is projectively identical across the whole family, yet the modular data varies with $N$.
* **Infinite non‑geometric embeddings** \[4\] produce braid representations not arising from any MTC, showing that the class of braid representations exceeds that of topological orders.
* **Twisted tensor product constructions** \[5\] illustrate that gauging a pointed category changes $\mathcal{D}$ and $S$ while leaving the ungauged braid sector unchanged.

These observations motivate the following **partial uniqueness theorem**:

> **Theorem (Partial Uniqueness).**
> Let $\mathcal{C}$ be a unitary MTC and $a\in\mathcal{C}$ a simple object. If the image of the braid representation $\rho_n$ on the fusion space $V_{a}^{\otimes n}$ is dense in $U(\dim V_{a}^{\otimes n})$ for some $n\ge2$, then the modular data $(S,T)$ are uniquely determined (up to a global phase) by the braid eigenvalues and the fusion rules. If the image is finite, additional data (e.g. $F$‑symbols or anomaly information) are required, and distinct MTCs may share the same braid representation.

### 6.2 Limitations and failure modes
* **Finite braid images.** When the image is finite, the eigenvalues provide only a discrete set of possibilities for the topological spins, leading to multiple admissible $S$ matrices.
* **Gauge ambiguities.** The reconstruction assumes a fixed gauge for $F$‑symbols; different gauge choices can alter intermediate phases while leaving physical $S$ and $T$ invariant. The sign ambiguity $\theta_\sigma\to -\theta_\sigma$ is a concrete manifestation of this.
* **Experimental noise.** Realistic measurements of $R_{aa}$ are subject to decoherence; small phase errors propagate non‑linearly into $S$ and $T$.
* **Higher‑genus effects.** Our analysis is restricted to the planar braid group $B_N$. On surfaces of genus $g>0$, additional mapping‑class generators may be needed to fully constrain the modular data.
* **Non‑unitary or non‑semisimple theories.** The ribbon identities used here rely on unitarity; extensions to logarithmic CFTs remain open.

A falsifying experiment would identify two distinct MTCs that yield identical braid matrices for a generating set of anyons yet differ in their $S$ matrices. Candidates include gauged vs. ungauged versions of a pointed category as in \[5\].

### 6.3 Open questions
1. **Classification of dense braid images.** Which families of MTCs admit dense braid representations? Preliminary evidence points to quantum‑group categories at generic $q$.
2. **Robust reconstruction algorithms.** Can one devise a stable numerical inversion of the Verlinde formula tolerant to experimental uncertainties?
3. **Extension to non‑unitary theories.** Our methods rely on unitarity; extending to logarithmic or non‑semisimple categories is an open direction.
4. **Experimental resolution of the anomaly.** What minimal additional probe (e.g., interferometry) suffices to fix the sign of $\theta_\sigma$ in practice?

## 7. Conclusion
Using the Ising theory as a fully explicit test case, we showed that the braid group representation—specifically the monodromy spectrum on the two‑anyon fusion space, together with the fusion ring—reconstructs the complete modular data: $S$ exactly, and $T$ up to the single sign ambiguity $\theta_\sigma\to -\theta_\sigma$. The positive result is bounded by two structural facts from the literature: many braid representations have finite image \[2,3\], and gauging operations can relate distinct modular categories while preserving braid data \[5\]. Consequently, braid representations constitute a nearly—but not fully—complete invariant of non‑Abelian topological order; the residual ambiguity is precisely the gravitational anomaly invisible to braiding. For Majorana‑based classification programs \[12,13,14\], the practical message is that braiding determines the fusion ring and $S$ matrix but requires independent parity or anomaly input to fix $T$.

## References
[1] arXiv:1009.0241v2 — Localization of unitary braid group representations.
[2] arXiv:math/0703274v1 — Braid group representations from twisted quantum doubles of finite groups.
[3] arXiv:1401.5329v4 — $SO(N)_2$ Braid group representations are Gaussian.
[4] arXiv:2003.02496v1 — An infinite family of braid group representations.
[5] arXiv:1906.08153v1 — Braid group representations from twisted tensor products of algebras.
[6] arXiv:2505.16817v1 — Braid Group Representations and Defect Operators in AdS/CFT Correspondence.
[7] arXiv:hep-th/9202024v1 — Spinning Braid Group Representation and the Fractional Quantum Hall Effect.
[8] arXiv:1105.5048v1 — Generalized and quasi-localizations of braid group representations.
[9] arXiv:1903.00463v2 — Topological braiding of non-Abelian mid-gap defects in classical meta-materials.
[10] arXiv:0710.1063v3 — Zero modes' fusion ring and braid group representations for the extended chiral su(2) WZNW model.
[11] arXiv:1708.06476v1 — Studies of braided non-Abelian anyons using anyonic tensor networks.
[12] QNFO: Braid Group Representations, Modular Data, and the Classification.
[13] QNFO: Majorana Zero Modes and Braiding Experiments.
[14] QNFO: Reconciliation of Non‑Uniqueness and Finite‑Image Braid Representations.

## Appendix A. Divergence report
No divergent claims arose among the drafts; all quantitative statements are convergent. Single‑appearance claims (e.g., fusion‑space dimension formula, braid order) are retained as they are uniquely contributed by a single draft but do not conflict with any other source.

## Appendix B. Claim attribution
| Claim ID | Statement | Source drafts | Agreement |
|----------|-----------|---------------|-----------|
| C1 | $d_\sigma = \sqrt{2}\approx1.4142$ | A, B, C | CONVERGENT |
| C2 | Total quantum dimension $D = 2$ | A, B, C | CONVERGENT |
| C3 | $S_{\sigma 1}=0.7071$ (i.e. $\sqrt{2}/2$) | A, B, C | CONVERGENT |
| C4 | $T_{\sigma\sigma}=e^{i\pi/8}\approx0.9239+0.3827\,i$ | A, B, C | CONVERGENT |
| C5 | Fusion‑space dimensions $f(n,1)=2^{n/2-1}$ for even $n$ | B | SINGLE |
| C6 | Braid generator $\rho_2(\sigma_1)$ has ordinary order $16$ and projective order $4$ | B | SINGLE |
| C7 | $S_{\sigma\sigma}=0$ | C | SINGLE |
| C8 | $S_{\sigma\psi}= -\sqrt{2}/2\approx-0.7071$ | C | SINGLE |
| C9 | Partial uniqueness theorem: dense braid image ⇒ unique $(S,T)$ up to global phase; finite image ⇒ ambiguity | A, B, C | CONVERGENT |
| C10 | Non‑uniqueness evidence from twisted quantum doubles, Gaussian $SO(N)_2$, and gauging constructions | A, B, C | CONVERGENT |
| C11 | Sign ambiguity $\theta_\sigma\to -\theta_\sigma$ not fixed by braid alone | A, C | CONVERGENT |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1708.06476v1 | Studies of braided non-Abelian anyons using anyonic tensor networks
arXiv:math/0509044v2 | Decomposing symmetric powers of certain modular representations of cyclic groups
arXiv:1909.02098v1 | Non-abelian anyons on graphs from presentations of graph braid groups
arXiv:2412.19647v3 | Branes and Representations of DAHA $C^\vee C_1$: affine braid group action on category
arXiv:1907.02664v2 | Data Encoding for Byzantine-Resilient Distributed Optimization
arXiv:2005.07866v1 | Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data
arXiv:2610.06203v1 | Interferometric braiding of non-Abelian anyons
arXiv:hep-ph/0610012v1 | Tevatron-for-LHC Report of the QCD Working Group

## QNFO corpus context (Vectorize)

QNFO: Braid Group Representations and Modular Data: Non-Uniqueness, Finite Images, and the Ising Test Case | https://papers.qnfo.org/papers/braid-group-representations-and-modular-data-non-uniqueness-finite-images-and-th
QNFO: Braid Group Representations and the Uniqueness of Modular Data: The Ising Test Case and General Limitations | https://papers.qnfo.org/papers/braid-group-representations-and-the-uniqueness-of-modular-data-the-ising-test-ca
QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors | https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majo-5099abb8
QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors | https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1708.06476v1 | Studies of braided non-Abelian anyons using anyonic tensor networks
  The content of this thesis can be broadly summarised into two categories: first, I constructed modified numerical algorithms based on tensor networks to simulate systems of anyons in low dimensions, and second, I used those methods to study the topological phases the anyons form when they braid around one another. In the first phase of my thesis, I extended the anyonic tensor network algorithms, b
  Full text (https://ar5iv.labs.arxiv.org/html/1708.06476v1), excerpts of its own sections:
  § Submission history: From: Babatunde Ayeni [ view email ] [v1] Tue, 22 Aug 2017 01:49:11 UTC (2,011 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Studies of braided non-Abelian anyons using anyonic tensor networks, by Babatunde M. Ayeni View PDF view license
  § Current browse context:: quant-ph < prev | next > new | recent | 2017-08 Change to browse by: cond-mat cond-mat.str-el
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[2] arXiv:math/0509044v2 | Decomposing symmetric powers of certain modular representations of cyclic groups
  For a prime number p, we construct a generating set for the ring of invariants for the p+1 dimensional indecomposable modular representation of a cyclic group of order p^2. We then use the constructed invariants to describe the decomposition of the symmetric algebra as a module over the group ring, confirming the Periodicity Conjecture of Ian Hughes and Gregor Kemper for this case.
  Full text (https://arxiv.org/html/math/0509044v2), excerpts of its own sections:
  § 1. Introduction: Suppose that $V$ is a finite dimensional representation of a finite group $G$ over a field ${\bf{F}}$ , i.e., $V$ is a finitely generated module over the group ring ${\bf{F}}G$ . The action of $G$ on $V$ induces an action on the dual $V^{*}$ which extends to an action by algebra automorphisms on the symmetric algebra ${\bf{F}}[V]:=S(V^{*})$ . The elements of $V^{*}$ , and thus also the elements of ${\bf{F}}[V]$ , represent ${\bf{F}}$ -valued functions on $V$ . If $\{x_{1},x_{2},\ldots,x_{n}\}$ is a basis for $V^{*}$ then ${\bf{F}}[V]$ can be identified with the ring of polynomials ${\bf{F}}[x_{1},x_{2},\ldots,x_{n}]$ . Let ${\bf{F}}[V]_{d}$ denote the subspace of homogeneous polynomials of degree $d$ . Since the action of $G$ preserves degree, ${\bf{F}}[V]_{d}$ is a module over ${\bf{F}}G$ and ${\bf{F}}[V]=\bigoplus_{d=0}^{\infty}{\bf{F}}[V]_{d}$ is a decomposition into a direct sum of finite dimensional ${\bf{F}}G$ -modules. Of course ${\bf{F}}[V]_{d}$ is precisely the the $d^{\rm th}$ symmetric power of $V^{*}$ . [...]
  § 2. Preliminaries: Let $G=\langle\sigma\rangle\cong{{\bf{Z}}/p^{r}}$ . It will be convenient to define $\Delta:=\sigma-1\in{\bf{F}}G$ . It is easy to see that $\Delta$ acts as a twisted derivation on ${\bf{F}}[V_{n}]$ , i.e., $\Delta(a\cdot b)=a\Delta(b)+\Delta(a)\sigma(b)$ . We denote the full transfer, $\mathop{\rm Tr}_{\langle 1\rangle}^{G}$ , by $\mathop{\rm Tr}^{G}$ and the image of the relative transfer, $\mathop{\rm Tr}_{L}^{G}({\bf{F}}[V_{n}]^{L})$ , by $\mathop{\rm Im}\Tr_{L}^{G}$ . Clearly $\mathop{\rm Im}\mathop{\rm Tr}_{L}^{G}$ is an ideal in ${\bf{F}}[V_{n}]^{G}$ . A simple calculation with binomial coefficients shows that $\Delta^{p^{t}}=\sigma^{p^{t}}-1$ and $\Delta^{p^{t}-1}=(\sigma^{p^{t}}-1)/(\sigma-1)=\Tr_{L}^{G}$ . We denote the group cohomology of $G$ with coefficients in the ${\bf{F}}G$ -module $W$ by $H^{*}(G,W)$ . Note that $H^{0}(G,W)$ is just the fixed subspace $W^{G}$ . [...]
  § 3. Computing ${\bf{F}}[V_{p+1}]^{{\bf{Z}}/p^{2}}$: In this section we use the ladder technique described in [ 15 , §7] to prove Theorem  1.2 . We use the notation $G:=\langle\sigma\rangle\cong{{\bf{Z}}/p^{2}},\ L:=\langle\sigma^{p}\rangle\cong{{\bf{Z}}/p},\ {\rm and}\ Q:=G/L=\langle\overline{\sigma}\rangle\cong{{\bf{Z}}/p}.$ Note that $\deg\left(N^{G}\left(x_{p}\right)\right)=p$ , $\deg\left(N^{G}\left(x_{p+1}\right)\right)=p^{2}$ and $Tr_{L}^{G}(x_{p})=x_{1}$ . The action of $L$ on $V^{*}_{p+1}$ is given by $\sigma^{p}(x_{p+1})=x_{p+1}+x_{1}$ and $\sigma^{p}(x_{i})=x_{i}$ for $i\leq p$ . Thus as $L$ -modules, ${\bf{F}}[V_{p+1}]\cong{\bf{F}}[V_{2}\oplus(p-1)V_{1}]$ . Therefore ${\bf{F}}[V_{p+1}]^{L}\cong{\bf{F}}[N^{L}(x_{p+1}),x_{p},\ldots,x_{1}]$ with $N^{L}(x_{p+1})=x^{p}_{p+1}-x_{1}^{p-1}x_{p+1}$ . The action of $Q$ on ${\bf{F}}[V_{p+1}]^{L}$ is given by $\overline{\sigma}(N^{L}(x_{p+1}))=N^{L}(x_{p+1})+x^{p}_{p}-x_{1}^{p-1}x_{p}$ and $\overline{\sigma}(x_{i})=\sigma(x_{i})$ for $i=1,2,\dots,p$ . Define $A:={\bf{F}}[z_{p},\ldots,z_{1},X_{p},\ldots,X_{1}]$ with $\deg(z_{i})=p$ and $\deg(X_{i})=1$ . [...]
  § 4. The Noether number of $V_{p+1}$: In this section we use the description of ${\bf{F}}[V_{p+1}]^{{\bf{Z}}/p^{2}}$ given in Theorem  1.2 to prove the following. Theorem 4.1 . For $p>2$ , the Noether number of $V_{p+1}$ is $p^{2}+p-3$ . Remark 4.2 . A Magma [ 3 ] calculation shows that for $p=2$ , the Noether number of $V_{3}$ is $p^{2}=4$ . For the remainder of this section we will assume that $p\geq 3$ . We continue to use the notation described at the beginning of Section  3 . [...]
[3] arXiv:1909.02098v1 | Non-abelian anyons on graphs from presentations of graph braid groups
  The aim of this paper is to analyse algorithms for constructing presentations of graph braid groups from the point of view of anyonic quantum statistics on graphs. In the first part of this paper, we provide a comprehensive review of an algorithm for constructing so-called minimal Morse presentations of graph braid groups that relies on discrete Morse theory. Next, we introduce the notion of a phy
  Full text (https://arxiv.org/html/1909.02098v1), excerpts of its own sections:
  § 1 Introduction: Anyonic quantum statistics is a notion that refers to situations when an interchange of (quasi)partiles in a physical model results with some general unitary transformation of a possibly multicomponent many-body wave function. Quasi-particles that obey anyonic statistics are called anyons. They are generalisations of bosons and fermions in the following sense. If a pair of bosons is exchanged, the many-particle wave function remains unchanged, i.e. is multiplied by the trivial phase factor $e^{i0}$ . On the other hand, an exchange of two fermions results with the multiplication of the wave function by factor $-1=e^{i\pi}$ . For single-component wave functions, an exchange of a pair of anyons results with the multiplication by factor $e^{i\theta}$ , $\theta\in]0,\pi[$ . Such scalar anyons are known to appear, for instance, in certain ansatzes for multi-electron wave functions realising the Fractional Quantum Hall effect (FQHE) [ 2 , 7 ] . More specifically, they approximately describe excited states of FQHE hamiltonians. [...]
  § 2 Presentations of graph braid groups - a review: Graph configuration spaces are aspherical, i.e. their fundamental group is their only non-vanishing homotopy group. Equivalently, the universal covering space of $C_{N}(\Gamma)$ is contractible. Therefore, graph braid groups encode all topological information about graph configuration spaces (see e.g. [ 18 ] ). However, finding the form of $Br_{N}(\Gamma)$ for a given graph is known to be a difficult task. All graph braid groups (we restrict our attention only to finite graphs) are finitely presented. This means that there exists a finite set of generators $\alpha_{1},\ldots,\alpha_{r}$ and a finite set of relators $R_{1}(\alpha_{1},\ldots,\alpha_{r}),\ldots,R_{s}(\alpha_{1},\ldots,\alpha_{r})$ in the form of finite words in $\alpha_{1},\ldots,\alpha_{r}$ and their inverses such that $\displaystyle Br_{N}(\Gamma)=\langle\alpha_{1},\ldots,\alpha_{r}|\ R_{1}(\alpha_{1},\ldots,\alpha_{r})=1,\ldots,$ $\displaystyle R_{s}(\alpha_{1},\ldots,\alpha_{r})=1\rangle.$ (2) Equation ( 2 ) is called a presentation of group $Br_{N}(\Gamma)$ . [...]
  § 2.1 General properties: Before we proceed with the discrete Morse theory for graphs, we summarise some general properties of graph braid groups that will play important roles in further sections. Firstly, recall the definition of the commutator subgroup. For any group $G$ , its commutator subgroup, denoted here by $G^{\prime}$ , is the group generated by group commutators of elements of $G$ $G^{\prime}:=\langle\alpha\beta\alpha^{-1}\beta^{-1}:\ \alpha,\beta\in G\rangle.$ The quotient $G/G^{\prime}$ is an abelian group called the abelianisation of $G$ . By the asphericity of graph configuration spaces, we have $Br_{N}(\Gamma)^{\prime}\cong H_{1}(C_{N}(\Gamma),{\mathbb{Z}})$ where $H_{1}$ denotes the first homology group. As it has been shown in [ 11 , 19 ] , for any graph we have $H_{1}(C_{N}(\Gamma),{\mathbb{Z}})\cong{\mathbb{Z}}^{m}\oplus({\mathbb{Z}}_{2})^{p}$ , where exponents $m$ and $p$ depend on $\Gamma$ and $N$ . In particular, $p=0$ if and only if $\Gamma$ is planar. For $2$ -connected graphs $H_{1}$ stabilises, i.e. $H_{1}(C_{N}(\Gamma),{\mathbb{Z}})\cong H_{1}(C_{2}(\Gamma),{\mathbb{Z}})$ . [...]
  § 2.2 Morse presentations: Graph configuration spaces have homotopy types of $CW$ -complexes. There are different ways to obtain a $CW$ -complex as a deformation retract of $C_{N}(\Gamma)$ , one of which is due to Abrams [ 25 ] and an other one due to Świątkowski [ 27 ] . [...]
[4] arXiv:2412.19647v3 | Branes and Representations of DAHA $C^\vee C_1$: affine braid group action on category
  We study the representation theory of the spherical double affine Hecke algebra (DAHA) of $C^\vee C_1$, using brane quantization. By showing a one-to-one correspondence between Lagrangian $A$-branes with compact support and finite-dimensional representations of the spherical DAHA, we provide evidence of derived equivalence between the $A$-brane category of $\mathrm{SL}(2,\mathbb{C})$-character var
  Full text (https://arxiv.org/html/2412.19647v3), excerpts of its own sections:
  § 1 Introduction and Summary: Brane quantization, as introduced by Gukov and Witten  GW (09) , is a framework that applies ideas from $A$ -model topological string theory to the quantization of symplectic manifolds. The core idea is to approach the quantization process via the topological $A$ -model on a “complexification” $\mathfrak{X}$ of the symplectic manifold $M$ . The complexified target space $\mathfrak{X}$ is usually an affine hyper-Kähler manifold with a holomorphic symplectic form $\Omega$ , whose real part $\Real\Omega$ restricts to the symplectic form on $M$ , and imaginary part $\Imaginary\Omega$ restricts to zero on $M$ . Considering the $A$ -model on $\mathfrak{X}$ with a symplectic form $\omega_{\mathfrak{X}}:=\Imaginary\Omega$ , the category of $A$ -branes $\text{$A$-}{\Brane}(\mathfrak{X},\omega_{\mathfrak{X}})$ provides a unified framework to quantize not only $M$ but all the $A$ -branes in the target space $\mathfrak{X}$ . [...]
  § 2 Double Affine Hecke Algebra of type $C^{\vee}C_{1}$: In the late 1980s, Macdonald introduced multivariable $q$ -symmetric polynomials Mac (87) , which form a $\mathbb{C}_{q,t}$ -basis for $\mathbb{C}_{q,t}[X]^{\mathfrak{S}_{n}}$ and constitute an orthogonal system of polynomials with respect to the inner product defined in $\mathbb{C}_{q,t}[X]^{\mathfrak{S}_{n}}$ . The properties of these Macdonald symmetric polynomials $P_{\lambda}(X;q,t)$ can be explored using both difference operators and the associated inner product. Cherednik reconstructed these $q$ -difference operators based on the representation theory of the affine Hecke algebra Che (92) ; Che95a () ; Che95b () ; Che95c () . In fact, Macdonald’s theory of orthogonal polynomials can be extended to any admissible pair $(\Delta,\Delta^{\prime})$ of affine root systems Mac (03) ; Sto (20) . Given such a pair, one can construct a pair of affine Hecke algebras, referred to as the double affine Hecke algebra (DAHA) Che (05) , which governs the associated Macdonald polynomials. [...]
  § 2.1 DAHA of type $C^{\vee}C_{1}$: Let us now review some necessary details of DAHA of type $C^{\vee}C_{1}$ . For an admissible pair $C^{\vee}C_{1}$ , DAHA is closely related to the fundamental group of a four-punctured sphere, which is generated by $T_{0},T_{0}^{\vee},T_{1},T_{1}^{\vee}$ as illustrated in Figure 1 $\pi_{1}\left(S^{2}\backslash\{p_{1},p_{2},p_{3},p_{4}\}\right)=\langle T_{0},T_{0}^{\vee},T_{1},T_{1}^{\vee}\mid T_{0}^{\vee}T_{0}T_{1}T_{1}^{\vee}=1\rangle.$ (6) A deformation of the group algebra of this fundamental group is achieved by modifying the relation to $T_{0}^{\vee}T_{0}T_{1}T_{1}^{\vee}=q^{-\frac{1}{2}}.$ (7) Then, DAHA of type $C^{\vee}C_{1}$ , denoted as $\accentset{\mbox{\large.\hskip-1.33333pt.}}{H}_{q,\bm{t}}$ , can be constructed by the quotient of the algebra by four Hecke relations 3 3 3 We make a slight adjustment to the standard notation so that the parameters $t_{i}$ agree exactly with the geometric parameters, which will be important for later use. For the standard notation, we refer the reader to Appendix A . [...]
  § 2.2 Spherical DAHA of $C^{\vee}C_{1}$: A distinguished subalgebra of the DAHA, known as the spherical subalgebra, is invariant under a certain Weyl group symmetry. We refer to this as the spherical DAHA, denoted by $S\!\accentset{\mbox{\large.\hskip-1.33333pt.}}{H}_{q,\bm{t}}$ , which will be the primary focus of this paper. [...]
[5] arXiv:1907.02664v2 | Data Encoding for Byzantine-Resilient Distributed Optimization
  We study distributed optimization in the presence of Byzantine adversaries, where both data and computation are distributed among $m$ worker machines, $t$ of which may be corrupt. The compromised nodes may collaboratively and arbitrarily deviate from their pre-specified programs, and a designated (master) node iteratively computes the model/parameter vector for generalized linear models. In this w
  Full text (https://arxiv.org/html/1907.02664v2), excerpts of its own sections:
  § 1 Introduction: Map-reduce architecture [ DG08 ] is implemented in many distributed learning tasks, where there is one designated machine (called the master) that computes the model iteratively, based on the inputs from the worker machines at each iteration, typically using descent techniques, like (proximal) gradient descent, coordinate descent, stochastic gradient descent, the Newton’s method, etc. [...]
  § 2 Problem Setting and Our Results: Given a dataset consisting of $n$ labelled data points $({\bf x}_{i},y_{i})\in\mathbb{R}^{d}\times\mathbb{R}$ , $i\in[n]$ , we want to learn a model/parameter vector ${\bf w}\in\mathbb{R}^{d}$ , which is a minimizer of the following empirical risk minimization problem: $\displaystyle\min_{{\bf w}\in\mathbb{R}^{d}}\left(\hbox{$\left(\vbox to0.0pt{}\right.$}\frac{1}{n}\sum_{i=1}^{n}f_{i}({\bf w})\hbox{$\left)\vbox to0.0pt{}\right.$}+h({\bf w})\right),$ (1) where $f_{i}({\bf w})$ , $i=1,2,\ldots,n$ , denotes the risk associated with the $i$ ’th data point with respect to ${\bf w}$ and $h({\bf w})$ denotes a regularizer. We call $f({\bf w}):=\frac{1}{n}\sum_{i=1}^{n}f_{i}({\bf w})$ the average empirical risk associated with the $n$ data points with respect to ${\bf w}$ . Our main focus in this paper is on generalized linear models (GLM), where $f_{i}({\bf w})=\ell(\langle{\bf x}_{i},{\bf w}\rangle;y_{i})$ for some differentiable loss function $\ell$ . [...]
  § 4.1 Finding The Corrupt Worker Nodes: Observe that $\textsf{supp}(\tilde{\bf e}_{i})$ may not be the same for all $i\in[p]$ , but we know, for sure, that the non-zero locations in all these error vectors occur within the same set of $t$ locations. Let $\mathcal{I}=\bigcup_{i=1}^{p}\textsf{supp}(\tilde{\bf e}_{i})$ , which is the set of all corrupt worker nodes. Note that $|\mathcal{I}|\leq t$ . We want to find this set $\mathcal{I}$ efficiently, and for that we note the following crucial observation. Since the non-zero entries of all the error vectors $\tilde{\bf e}_{i}$ ’s occur in the same set $\mathcal{I}$ , a random linear combination of $\tilde{\bf e}_{i}$ ’s has support equal to $\mathcal{I}$ with probability one, if the coefficients of the linear combination are chosen from an absolutely continuous probability distribution. This idea has appeared before in [ ME08 ] in the context of compressed sensing for recovering arbitrary sets of jointly sparse signals that have been measured by the same measurement matrix. Definition 1 . [...]
  § 7 Numerical Experiments: In this section, we validate the efficacy of our proposed methods by numerical experiments. We run distributed gradient descent (GD) and coordinate descent (CD) for linear regression $\arg\min_{{\bf w}\in\mathbb{R}^{d}}\|{\bf X}{\bf w}-{\bf y}\|_{2}^{2}$ . As mentioned in Section  2.1 , for linear regression (which is equal to ridge regression when $h=0$ ), the projected gradient descent (PGD) reduces to gradient descent (GD). Since we are doing exact computation (computing the gradients exactly in the case of GD and updating the coordinates exactly in the case of CD), (i) there is no need to check the convergence, and (ii) our algorithm will perform exactly the same whether we are working with synthetic datasets or real datasets, hence, we will work with a synthetic dataset. We run our algorithms 23 23 23 We implement our algorithm in Python, and run it on an iMac machine with 3.8 GHz Quad-Core Intel Core i5 processor and 16 GB 2400 MHz DDR4 memory. with $m=15$ worker nodes on two datasets: $(n=10,000,d=250)$ and $(n=20,000,d=22,000)$ . [...]
[6] arXiv:2005.07866v1 | Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data
  We study distributed stochastic gradient descent (SGD) in the master-worker architecture under Byzantine attacks. We consider the heterogeneous data model, where different workers may have different local datasets, and we do not make any probabilistic assumptions on data generation. At the core of our algorithm, we use the polynomial-time outlier-filtering procedure for robust mean estimation prop
  Full text (https://arxiv.org/html/2005.07866v1), excerpts of its own sections:
  § 3 Our Results: We tackle the Byzantine behavior of corrupt workers by applying a non-trivial decoding algorithm at the master in each SGD iteration. Our decoding algorithm is inspired by the recent breakthrough results in theoretical computer science for robust mean estimation [ LRV16 , DKK+16 , SCV18 ] ; see Section  4 for more details. Before stating our results, we need to formally define mini-batch SGD. Note that we can speed up the convergence of distributed SGD by having each worker sample many data points (without replacement), say, $b\geq 1$ data points, and send the average gradients on these data points to the master. This is called mini-batch SGD. To formalize this, for any $\bm{x}\in\mathbb{R}^{d},r\in[R],b\in[n_{r}]$ , consider the following set $\displaystyle\mathcal{F}_{r}^{\otimes b}(\bm{x}):=\left\{\frac{1}{b}\sum_{i\in\mathcal{H}_{b}}\nabla F_{r,i}(\bm{x}):\mathcal{H}_{b}\in\binom{[n_{r}]}{b}\right\}.$ (5) Let $H_{b}$ denote a random variable taking values in $\binom{[n_{r}]}{b}$ with uniform distribution. [...]
  § 3.1 Convergence results: Theorem 1 (Strongly-convex and Non-convex) . Suppose an $\epsilon>0$ fraction of $R$ workers are adversarially corrupt. For an $L$ -smooth global objective function $F:\mathcal{C}\to\mathbb{R}$ , let Algorithm  1 generate a sequence of iterates $\{\bm{x}^{t}\}_{t=0}^{T}$ when run with a fixed learning rate $\eta$ , where in the $t$ ’th iteration, every honest worker $r\in[R]$ samples a mini-batch stochastic gradient from $\mathcal{F}_{r}^{\otimes b}(\bm{x}^{t})$ , satisfying ( 6 ) and ( 7 ) (corrupt workers may send arbitrary vectors). Fix an arbitrary constant $\epsilon^{\prime}>0$ . If $\epsilon\leq\frac{1}{4}-\epsilon^{\prime}$ , then with probability at least $1-T\exp(-\frac{\epsilon^{\prime 2}(1-\epsilon)R}{16})$ , we have the following convergence guarantees: • Strongly-convex: If $F$ is also $\mu$ -strongly convex and we take $\eta=\frac{\mu}{L^{2}}$ , then we have $\displaystyle\mathbb{E}\|\bm{x}^{T}-\bm{x}^{*}\|^{2}$ $\displaystyle\leq\left(1-\frac{\mu^{2}}{2L^{2}}\right)^{T}\|\bm{x}^{0}-\bm{x}^{*}\|^{2}+\frac{2L^{2}}{\mu^{4}}\varGamma. [...]
  § 3.2 Remarks about Theorem 1: In this section, we discuss some important aspects of our convergence results. Analysis of the approximation error. In both parts of Theorem  1 , the approximation error $\varGamma$ consists of three error terms: first is $\varGamma_{1}=\mathcal{O}(\nicefrac{{\sigma^{2}}}{{(1-(\epsilon+\epsilon^{\prime}))bR}})$ , which is the standard error arising due to the sampling of stochastic gradients; second is $\varGamma_{2}=\mathcal{O}(\kappa^{2})$ , which is due to dissimilarity in the local datasets; and third is $\varGamma_{3}=\mathcal{O}\left(\left(\frac{\sigma^{2}}{b\epsilon^{\prime}}\left(1+\frac{d}{(1-(\epsilon+\epsilon^{\prime}))R}\right)+\kappa^{2}\right)(\epsilon+\epsilon^{\prime})\right)$ , which is due to Byzantine attacks. Observe that $\varGamma_{1}$ decreases with the mini-batch size $b$ and the number of workers $R$ , as desired. [...]
  § 3.3 Convergence results for full-batch gradient descent: In this section, we provide our results for the setting where workers compute full-batch gradients, instead of mini-batch stochastic gradients. This setting will simplify the approximation error in the solution produced by Algorithm  1 on both strongly-convex and non-convex objectives as well as their convergence analyses. Theorem 2 . Suppose an $\epsilon>0$ fraction of $R$ workers are adversarially corrupt. [...]
[7] arXiv:2610.06203v1 | Interferometric braiding of non-Abelian anyons
  The manipulation of non-Abelian anyons is a foundational ingredient for topological quantum computing and underlies topologically protected quantum memories. Here we analyze a quantum-impurity-based protocol for braiding non-Abelian anyons. Exploiting mobile impurities with addressable internal spin states, we provide a concrete protocol to experimentally measure the matrix elements of the $R$ and
  Full text (https://ar5iv.labs.arxiv.org/html/2610.06203v1), excerpts of its own sections:
  § Submission history: From: Francesco Debortoli [ view email ] [v1] Mon, 5 Oct 2026 12:15:33 UTC (521 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Interferometric braiding of non-Abelian anyons, by Francesco Debortoli and Fabian Grusdt View PDF HTML (experimental) TeX Source view license
  § Current browse context:: quant-ph < prev | next > new | recent | 2026-10 Change to browse by: cond-mat cond-mat.mes-hall cond-mat.str-el
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[8] arXiv:hep-ph/0610012v1 | Tevatron-for-LHC Report of the QCD Working Group
  The experiments at Run 2 of the Tevatron have each accumulated over 1 inverse femtobarn of high-transverse momentum data. Such a dataset allows for the first precision (i.e. comparisons between theory and experiment at the few percent level) tests of QCD at a hadron collider. While the Large Hadron Collider has been designed as a discovery machine, basic QCD analyses will still need to be performe
  Full text (https://arxiv.org/html/hep-ph/0610012v1), excerpts of its own sections:
  § Parton Level Vs Experiment - A Brief History of Cones: The original Snowmass [ 3 ] implementation of the cone algorithm can be thought of in terms of a simple sum over all objects within a cone, centered at rapidity (the actual original version used the pseudorapidity $\eta$ ) and azimuthal angle $\left(y_{C},\phi_{C}\right)$ and defining a $p_{T}$ -weighted centroid via $\displaystyle k$ $\displaystyle\subset C\text{ iff }\sqrt{\left(y_{k}-y_{C}\right)^{2}+\left(\phi_{k}-\phi_{C}\right)^{2}}\leq R_{cone},$ $\displaystyle\overline{y}_{C}$ $\displaystyle\equiv\frac{\sum_{k\subset C}y_{k}\ast p_{T,k}}{\sum_{l\subset C}p_{T,l}},\text{ }\overline{\phi}_{C}\equiv\frac{\sum_{k\subset C}\phi_{k}\ast p_{T,k}}{\sum_{l\subset C}p_{T,l}}.$ If the $p_{T}$ -weighted centroid does not coincide with the geometric center of the cone, $\left(\overline{y}_{C},\overline{\phi}_{C}\right)\neq\left(y_{C},\phi_{C}\right)$ , a cone is placed at the $p_{T}$ -weighted centroid and the calculation is repeated. [...]
  § Run II Jet Results: Preliminary Run II inclusive cone jet results [ 23 , 24 ] suggest that, even with differing algorithms, the two collaborations are in reasonable agreement as indicated in Figs. 2.0.11 and 2.0.12 . On the other hand, the challenge, as noted above, is to continue to reduce the systematic uncertainties below the current 10% to 50% level, which effectively guarantees agreement, if the primary differences are also at the 10% level. Indeed, the current studies of the corrections due to splash-in, i.e ., the underlying event (and pile-up), and the splash-out corrections due to hadronization are much more sophisticated than in Run I and presented in such a way that they can be applied either to the data (corrected for the detector) or to a theoretical (perturbative) calculation. The evaluation of these corrections is based on data and the standard Monte Carlos, PYTHIA  and  HERWIG , especially Tune A of PYTHIA , which seems to accurately simulate the underlying event in terms of multiple parton interactions, including the observed correlations with the hard scattering process. [...]
  § Summary: We have come a long way in our understanding of jet algorithms and their limitations. We still have a way to go if we want to guarantee a precision much better than 10%. Overall, we expect both cone and $k_{T}$ algorithms to be useful at the LHC. Their differing strengths and weaknesses will provide useful cross checks. Our conclusions and recommendations include the following. • Seeds introduce undesirable IR sensitivity when used in theoretical calculations. The cone algorithm without seeds is IR-safe. Experimental results for the cone algorithm should be corrected for any use of seeds and compared to theoretical results without seeds. • More study is required to understand the quantitative impact and possible optimization of the choices for the parameters in the split/merge step of the cone algorithm, $f_{merge}$ and $p_{T,\min}$ . As in Run I, CDF and DØ are currently using different parameter choices and the implied differences in jet rates are not well documented. [...]
  § Strategy and First Results: The scale (commonly designated as “ $Q$ ”) dependence of the parton distributions are governed by the QCD evolution equation; the dynamical degrees of freedom to be probed reside in the momentum fraction ( $x$ ) dependence, usually parametrized at some relatively low $Q$ , where ample data exist to experimentally constraint them. [...]
[9] QNFO: Braid Group Representations and Modular Data: Non-Uniqueness, Finite Images, and the Ising Test Case | https://papers.qnfo.org/papers/braid-group-representations-and-modular-data-non-uniqueness-finite-images-and-th
  A central question in the theory of topological order asks whether the braid group representation $B_N$ carried by $N$ non-Abelian anyons uniquely determines the modular data — the $S$ and $T$ matrices — of the underlying topological quantum field theory. We reconcile three lines of analysis into a single assessment. Structurally, we formalize the question as a reduction map $\Phi$ from modular te
  Full text (https://papers.qnfo.org/papers/braid-group-representations-and-modular-data-non-uniqueness-finite-images-and-th), excerpts of its own sections:
  § 1. Introduction: Non-Abelian anyons in two spatial dimensions are characterized by two layers of algebraic structure. The first is combinatorial: fusion rules $N_{ab}^c$ specifying how anyon charges combine. The second is geometric: adiabatic exchange of anyons induces unitary transformations on the degenerate fusion space, giving a representation of the braid group $B_N$, generated by exchanges $\sigma_1,\dots,\sigma_{N-1}$ subject to $\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$ and [...]
  § 5. Results: **R1 (finiteness, from literature).** Braid representations from twisted quantum doubles of finite groups factor through finite groups [2]; $SO(N)_2$/$O(N)_2$ braid representations are Gaussian with finite image [4]. **R2 (Ising modular data, derived).** $\theta_1=1$, $\theta_\sigma=e^{i\pi/8}$, $\theta_\psi=-1$; $\mathcal{D}=2$; $T=\operatorname{diag}(1,e^{i\pi/8},-1)$; $S=\frac12\begin{pmatrix}1&\sqrt2&1\\\sqrt2&0&-\sqrt2\\1&-\sqrt2&1\end{pmatrix}$; all verified against the ribbon identity, hexagon equations, $S^2=C$, and $STS^{-1}$ diagonalization (Section 4). **R3 (trace).** $\operatorname{Tr}\rho_3(\sigma_1)=\sqrt2\,e^{i\pi/8}=1.3066+0.5412\,i$, magnitude $\sqrt2=d_\sigma$. **R4 (deformation family).** $\mathrm{Ising}(7)$ shares all fusion rules with Ising but has $\theta_\sigma=e^{7i\pi/8}$ and distinct $S,T$ (its unitarity as a Galois conjugate is not established, and no chiral central charge is assigned to it); its $B_3$ representation is inequivalent to Ising's (trace ratio $e^{-3i\pi/4}$), though projectively intertwined by the parity operator of [13]. [...]
  § 6. Discussion: **Limitations.** (i) We have not computed the exact Majorana braid image order; R5 brackets it loosely, and the factor-of-2 convention ambiguity propagates into every quoted number. (ii) The finiteness results [2,4] are special to their families; a generic MTC may have infinite braid image, where the finite-image argument does not apply. (iii) "Finite image" does not by itself prove "non-unique modular data": two finite groups can distinguish rich algebraic data if the representation is faithful enough. Our non-uniqueness assessment is an *existence-of-room* argument plus a concrete deformation family, not a constructive collision of two MTCs with *identical* full projective braid images and distinct $(S,T)$. (iv) Symmetry-enriched orders may evade the analysis: global symmetries acting on anyons can modify braiding without altering the underlying UBFC. **Falsifiability.** The non-uniqueness assessment would be falsified by a proof that $\Phi$ is injective on a class containing the finite-image families. [...]
  § 7. Conclusion: We assessed whether the braid group representation on $N$ anyons uniquely determines the modular data of a non-Abelian topological order. The structural evidence — finite braid images for twisted quantum doubles [2] and the $SO(N)_2$ family [4], the vast surplus of nongeometric braid representations [3], and the Ising$(\alpha)$ deformation family with shared fusion rules — indicates that braid representations constrain but do not uniquely determine modular data in general. The explicit Ising computation shows precisely what braiding does fix: given the complete set of $R$-symbols on all fusion channels, the ribbon identity and hexagon equations determine the topological spins and, with the fusion-derived quantum dimensions, the full $S$ matrix — up to gauge and chirality conventions that do not affect local observables but do affect the global modular data (e.g., the sign of the chiral central charge). [...]
[10] QNFO: Braid Group Representations and the Uniqueness of Modular Data: The Ising Test Case and General Limitations | https://papers.qnfo.org/papers/braid-group-representations-and-the-uniqueness-of-modular-data-the-ising-test-ca
  We investigate whether the unitary braid group representation carried by a collection of non‑Abelian anyons uniquely determines the modular data—namely the $S$ and $T$ matrices—of the underlying modular tensor category (MTC). Using the Ising anyon theory as a concrete laboratory, we reconstruct the full modular data from the elementary braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ together with 
  Full text (https://papers.qnfo.org/papers/braid-group-representations-and-the-uniqueness-of-modular-data-the-ising-test-ca), excerpts of its own sections:
  § 1. Introduction: Topological phases of matter support anyonic excitations whose adiabatic exchange is described by a unitary representation of the braid group $B_N$ \[1\]. An MTC encodes the full topological data in its modular $S$ and $T$ matrices, which together determine fusion rules, quantum dimensions, and braiding phases \[12\]. A central question—explicitly raised in recent QNFO reports \[13,14\]—is whether the braid representation on $N$ anyons suffices to reconstruct $S$ and $T$ uniquely. The practical relevance is immediate: experimental platforms based on Majorana zero modes (MZMs) implement projective braid operations \[13\]; if these operations uniquely fix the modular data, braiding alone could certify the underlying topological order. [...]
  § 4.8 Summary of derived quantities: | Quantity | Numerical value | Interpretation | |----------|----------------|----------------| | $d_\sigma$ | $\sqrt{2}\approx1.4142$ | Quantum dimension of $\sigma$ | | $D$ | $2$ | Total quantum dimension | | $S_{\sigma 1}$ | $0.7071$ | Overlap of $\sigma$ with vacuum | | $S_{\sigma\psi}$ | $-0.7071$ | Overlap of $\sigma$ with fermion | | $S_{\sigma\sigma}$ | $0$ | Vanishing diagonal entry | | $T_{\sigma\sigma}$ | $0.9239+0.3827\,i$ | Topological spin of $\sigma$ | | $f(n,1)$ (even $n$) | $2^{n/2-1}$ | Fusion‑space dimension | | $\operatorname{ord}(\rho_2(\sigma_1))$ | $16$ (projective $4$) | Braid generator order | These values match the canonical Ising modular data \[13\], confirming that the braid eigenvalue alone suffices to reconstruct $S$ and $T$ for this model.
  § 5. Results: The explicit arithmetic in Section 4 yields the following concrete numerical results for the Ising anyon theory: 1. **Quantum dimension** $d_\sigma = \sqrt{2}\approx1.4142$. 2. **Total quantum dimension** $D = 2$. 3. **Modular $S$ matrix** (rows/columns ordered $1,\sigma,\psi$): $$ S = \frac{1}{2} \begin{pmatrix} 1 & \sqrt{2} & 1 \\ \sqrt{2} & 0 & -\sqrt{2} \\ 1 & -\sqrt{2} & 1 \end{pmatrix}, $$ giving $S_{\sigma 1}=0.7071$, $S_{\sigma\psi}=-0.7071$, $S_{\sigma\sigma}=0$. 4. **Modular $T$ matrix**: $$ T = \operatorname{diag}\bigl(1,\; e^{i\pi/8},\; -1\bigr) = \operatorname{diag}\bigl(1,\; 0.9239+0.3827\,i,\; -1\bigr). $$ 5. **Fusion‑space dimensions** $f(n,1)=2^{n/2-1}$ for even $n$. 6. **Braid generator order** ordinary $16$, projective $4$. All numbers arise directly from the braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ and the fusion rule $\sigma\times\sigma=1+\psi$; no additional simulations were performed.
  § 7. Conclusion: Using the Ising theory as a fully explicit test case, we showed that the braid group representation—specifically the monodromy spectrum on the two‑anyon fusion space, together with the fusion ring—reconstructs the complete modular data: $S$ exactly, and $T$ up to the single sign ambiguity $\theta_\sigma\to -\theta_\sigma$. The positive result is bounded by two structural facts from the literature: many braid representations have finite image \[2,3\], and gauging operations can relate distinct modular categories while preserving braid data \[5\]. Consequently, braid representations constitute a nearly—but not fully—complete invariant of non‑Abelian topological order; the residual ambiguity is precisely the gravitational anomaly invisible to braiding. For Majorana‑based classification programs \[12,13,14\], the practical message is that braiding determines the fusion ring and $S$ matrix but requires independent parity or anomaly input to fix $T$.
[11] QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors | https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majo-5099abb8
  Majorana zero modes (MZMs) localized on vortices of a two-dimensional topological superconductor carry a projective representation of the braid group, and the associated anyon theory is encoded in a modular tensor category whose fusion rules and modular data ($S$ and $T$ matrices) determine the topological order. We address two questions: whether the braid group representation on $N$ anyons unique
  Full text (https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majo-5099abb8), excerpts of its own sections:
  § Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors: > **Correction (version 1.0.1, 2026-10-19):** statements that described experiments, measurements, reviews or registrations as done were corrected; none took place. See the Correction Notice.
  § 1. Introduction: A two-dimensional topological superconductor (2D TSC) supports vortices that bind Majorana zero modes (MZMs): self-adjoint fermionic operators $\gamma_i = \gamma_i^\dagger$ obeying the Clifford algebra $\{\gamma_i,\gamma_j\} = 2\delta_{ij}$. Exchanging vortices $i$ and $j$ acts on the ground-state manifold by the operator $U_{ij} = \exp(\frac{\pi}{4}\gamma_i\gamma_j)$, yielding a projective representation of the braid group $B_N$ [6], [8]. The question we revisit here, posed in the the QNFO archive entry https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero/ [12], is twofold: 1. [...]
  § 5. Results: **R1 (computed, §4.1).** Ising/MZM quantum dimensions: $d_1 = d_\psi = 1$, $d_\sigma = \sqrt{2}$, total quantum dimension $\mathcal{D} = 2$. **R2 (computed, §4.2).** The Ising modular $S$ matrix, derived from fusion rules and the braid-fixed twist $\theta_\sigma = e^{i\pi/8}$ via the Verlinde formula, is $$S = \frac{1}{2}\begin{pmatrix} 1 & \sqrt{2} & 1 \\ \sqrt{2} & 0 & -\sqrt{2} \\ 1 & -\sqrt{2} & 1 \end{pmatrix},$$ with unitarity verified by explicit inner-product computation (all six row-pair checks in §4.2). The $T$ matrix is $\mathrm{diag}(1, e^{i\pi/8}, -1)$, determined by the braid representation up to the finite ambiguity $\theta_\sigma \to e^{i\pi k/4}\theta_\sigma$, $k$ odd. [...]
  § 6. Discussion: **What we have established.** The Ising/MZM case admits a complete, hand-checkable derivation: braid representation → twists → modular data, with every arithmetic step explicit (§4.1–4.2). This is a genuine instance of determinacy, and it validates the pipeline's logic on the physically canonical case. The metaplectic family supplies the natural higher-rank candidate space, and Property F results [4], [7] give a computable gapped/ungapped discriminator. **Limitations and failure modes.** First, the determinacy argument for Ising relies on the exchange eigenvalues fixing $\theta_\sigma$; for higher-rank candidates the braid representation on *small* $N$ may under-determine the twists, and the finite ambiguity of R3 could grow. We have not proven a general determinacy theorem — only exhibited the mechanism. Second, the classification projection R5 is conditional: the gauging moves of [10] generate candidates whose hexagon coherence we have not tested exhaustively, and the count in §4.4 Step 3 is explicitly incomplete. [...]
  § 7. Conclusion: We have shown that for the canonical Ising/MZM theory the braid group representation determines the modular data up to a finite, physically resolvable ambiguity, and we have set up a classification pipeline — Clifford seed, coherence equations, modular-data filter, gauging generators — whose reach is the unitary semisimple fragment of MZM fusion rules. The metaplectic family $SO(N)_2$ and its gauged descendants constitute the candidate space; Property F separates gapped-TSC-compatible from computationally universal theories. Extending determinacy beyond the Ising case and completing the gauged-descendant enumeration are the principal open problems.
[12] QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors | https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero
  We investigate whether the braid group representation on $N$ anyons uniquely determines the modular data ($S$ and $T$ matrices) of a non-Abelian topological order, and whether this framework classifies all fusion rules for Majorana zero modes (MZMs) in 2D topological superconductors. We show that the local $N$-anyon braid group representation constrains the modular data up to finite gauge ambiguit
  Full text (https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero), excerpts of its own sections:
  § 1. Introduction: Topological quantum computation exploits the non-Abelian statistics of anyons—quasiparticle excitations in two-dimensional systems whose braiding operations are represented by non-commuting unitary matrices on a degenerate ground-state manifold [1]. A central question is whether the local braiding data of $N$ anyons suffices to reconstruct the full modular data of the underlying topological order (TO), or whether additional global information is required. This question has direct physical consequences for 2D topological superconductors (TSCs) hosting Majorana zero modes (MZMs), where the anyonic excitations are vortices binding MZMs and the fermionic quasiparticle is a transparent (local) fermion [2,3]. The modular data of a TO consists of the $S$-matrix, which encodes the mutual braiding statistics of anyons, and the $T$-matrix, which encodes the topological spins. Together, these matrices form a projective representation of the modular group $\mathrm{SL}(2,\mathbb{Z})$ and satisfy the Verlinde formula, which determines the fusion rules [4]. [...]
  § 2.1 Braid Group Representations: The braid group $B_N$ on $N$ strands is generated by elementary exchanges $\sigma_1, \ldots, \sigma_{N-1}$ satisfying the braid relations $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i-j| \geq 2$ and $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$. A unitary representation $\rho: B_N \to U(V)$ on a finite-dimensional Hilbert space $V$ arises from the braiding of $N$ identical anyons of type $a$ in a TO. The representation depends on the fusion channels available: the dimension of $V$ is determined by the fusion multiplicities $N_{aa\ldots a}^{c}$ for all possible total charges $c$ [1,5].
  § 2.2 Modular Data and Fusion Categories: A unitary modular tensor category (UMTC) $\mathcal{C}$ is a braided fusion category with non-degenerate braiding. Its simple objects $\{a, b, c, \ldots\}$ satisfy fusion rules $a \times b = \sum_c N_{ab}^c \, c$. The associativity of fusion is governed by $F$-symbols $F^{abc}_{d}$, and the braiding is governed by $R$-symbols $R^{ab}_c$. These must satisfy the pentagon and hexagon equations, which are polynomial constraints ensuring consistency of the fusion and braiding structure [5]. The modular $S$-matrix is defined by the Hopf link invariant $S_{ab} = \frac{1}{\mathcal{D}} \sum_c d_c \, \theta_c \, N_{ab}^c / d_a d_b$ (where $\mathcal{D} = \sqrt{\sum_a d_a^2}$ is the total quantum dimension and $\theta_c$ is the topological spin), and the $T$-matrix is diagonal with entries $T_{aa} = \theta_a$. [...]
  § 6. Conclusion: We have shown that the braid group representation on $N$ anyons constrains the modular data of a non-Abelian topological order up to finite gauge ambiguity, but does not uniquely determine the global $S$-matrix without specifying the underlying spin structure. For Majorana zero modes in 2D topological superconductors, the braid representation $\rho(\sigma_i) = \frac{1}{\sqrt{2}}(1 + \gamma_{i+1}\gamma_i)$ uniquely fixes the local $F$ and $R$ symbols of the Ising category, thereby determining the $T$-matrix. The fusion rules are rigidly classified as Ising type ($\sigma \times \sigma = 1 + \psi$), and no alternative non-Abelian fusion rules are consistent with the Majorana Clifford algebra and the super-modular structure. The global $S$-matrix, however, depends on the spin structure of the underlying manifold, reflecting the fermionic nature of the topological order. [...]