# Does the Braid Group Representation Determine Modular Data? Non-Uniqueness, Finite Images, and the Ising Test Case

## Abstract

A central question in topological order is whether the braid group representation $\rho_N$ carried by $N$ non-Abelian anyons uniquely determines the modular data — the $S$ and $T$ matrices — of the underlying modular tensor category (MTC). We formalize the extraction problem as a map from braid representations to modular data and test it on the Ising anyon theory, the canonical non-Abelian topological order realized by Majorana zero modes in 2D topological superconductors. We derive in full arithmetic detail: (i) the fusion-space dimensions $f(n,1) = 2^{n/2-1}$ for even $n$ Ising anyons; (ii) the braid generator $\rho(\sigma_1) = e^{-i\pi/8}\,\mathrm{diag}(1,i)$, whose projective order is $4$ and whose ordinary order is $16$; (iii) the full Ising modular data, with $S$ reconstructed from the fusion matrix via the Verlinde eigenvector basis and $T = \mathrm{diag}(1, e^{i\pi/8}, -1)$; and (iv) a non-uniqueness argument: the Gaussian, finite-image braid representations of the $SO(N)_2$ family are indistinguishable as braid representations on tensor powers of the spin object, yet the associated modular data varies across the family. We conclude that the braid representation on finitely many anyons determines modular data only up to ambiguities that additional structure — Galois signs, monodromy scalings, or localization data — may or may not resolve.

## 1. Introduction

Non-Abelian anyons in two-dimensional topological phases carry a projective representation of the braid group $B_N$ on their degenerate fusion Hilbert space. A natural and consequential question is whether this representation — the physical data most directly accessible to braiding experiments — uniquely fixes the modular data $(S,T)$ of the topological quantum field theory, and hence the full topological order. The question matters for classification programs [12], [13], [14], for the interpretation of interferometry experiments, and for the security of anyon-based topological quantum computation, where one wishes to know whether braiding witnesses the full anyon theory or only a quotient of it.

The Ising anyon theory — realized by Majorana zero modes (MZMs) on vortices of a chiral $p + ip$ superconductor, and studied extensively through tensor-network and metamaterial platforms [9], [11] — is the ideal test case: it is non-Abelian, small enough for complete explicit computation, and it sits inside a family of related categories whose braid representations are known to be Gaussian with finite image [3].

Our contributions are:

1. A fully explicit derivation of the Ising fusion-space dimensions, braid matrices, and modular data, with every arithmetic step shown (Section 4).
2. A precise statement of the ambiguities in reconstructing $S$ from braid data: the Verlinde formula determines $S$ from fusion rules only up to sign and Galois-conjugation ambiguities, and the braid representation supplies the missing data only partially.
3. A non-uniqueness argument built on the $SO(N)_2$ family [3] and on finite-image braid representations from twisted quantum doubles [2]: distinct modular tensor categories can induce indistinguishable braid representations on the fusion spaces of a fixed anyon type.

We argue that the answer to the title question is, in general, **no**: the braid representation on $N$ anyons determines the modular data only up to identifiable ambiguities, and only the full tower of representations $\{\rho_N\}_{N \geq 2}$, together with consistency of the localization structure [1], [8], can be expected to pin down $(S,T)$ — and even then not in complete generality.

## 2. Background and Related Work

**Braid representations from unitary $R$-matrices and fusion categories.** Rowell and Wang [1] study unitary braid group representations arising from unitary $R$-matrices (unitary solutions of the Yang–Baxter equation) and from simple objects in unitary braided fusion categories, asking when such representations are faithful and when they are "localizable" on tensor powers of a fixed space. Their faithfulness dichotomy is directly relevant here: non-faithful braid representations, by definition, lose information, and the lost information may include modular data. Rowell's later work with coauthors [8] develops generalized and quasi-localizations of braid group representations, formalizing when a family of braid representations can be uniformly modeled on tensor powers of a fixed vector space with generators acting "locally" — precisely the structural hypothesis under which one could hope to pass from $\{\rho_N\}$ to a category and thence to modular data.

**Finite images.** Rowell, Zhang, and coauthors [2] show that braid group representations from twisted quantum doubles of finite groups always factor through finite groups, in contrast to quantum-group categories at roots of unity. This is a key input to our non-uniqueness argument: two categories with structurally different modular data can share the same finite-image braid representation. Rowell [3] proves that the braid representations on tensor powers of the spin objects of the pre-modular categories $SO(N)_2$ ($N$ odd) and $O(N)_2$ ($N$ even) are Gaussian representations with finite image, described via centralizer algebras isomorphic to quantum tori. The $SO(N)_2$ family is our principal witness for non-uniqueness: the spin-object braid representations are uniform across the family while the categories — and hence their modular data — are not.

**Constructions of braid representations.** Bellingeri and coauthors [4] construct an infinite family of nongeometric braid group representations via $d$-fold branched coverings, factoring through automorphism groups of free groups; such representations need not arise from any modular tensor category, showing that the class of braid representations is strictly larger than the class arising from topological order — a necessary caveat for any "braid implies modular data" reconstruction program. Gier and Rowell [5] unify constructions of braid representations from finite groups via iterated twisted tensor products, and hint at relationships between braidings on $G$-gaugings of a pointed modular category $\mathcal{C}(A,Q)$ and on $\mathcal{C}(A,Q)$ itself — gauging changes modular data (it doubles the anyon content) while potentially preserving braid representations on the ungauged sector, another non-uniqueness channel.

**Physical realizations.** Isakov and coauthors [7] generalize the path-integral representation of the braid group to particles with spin, introducing charged winding numbers and super Knizhnik–Zamolodchikov operators; this shows that braid representations can be assembled from data (spin, winding) that is not modular data per se. Bomantara and coauthors [9] realize non-Abelian braid statistics of Majorana-type mid-gap defects in classical metamaterials, demonstrating experimentally accessible braid representations that are, by construction, insensitive to the chiral central charge — a quantity encoded in $T$. Barkeshli and coauthors [6] connect braid group representations to defect operators and Wilson loops in AdS/CFT, with fusion and braiding in modular tensor categories playing a central role; the holographic dictionary there is another instance where braid data and modular data are related but not identified. Chen and coauthors [10] realize the Grothendieck fusion ring of restricted $U_q\mathfrak{sl}(2)$ at even roots of unity on zero-mode Fock spaces of the extended chiral $su(2)$ WZNW model, giving an explicit arena where fusion rings, braid representations, and modular data can be compared term by term. Iblisdir and coauthors [11] develop anyonic tensor network algorithms for simulating braided anyons, providing the numerical machinery one would use to test reconstruction hypotheses beyond exactly solvable cases.

**Prior reconciliations.** The QNFO corpus documents [12], [13], [14] investigate precisely the question studied here, including the classification of MZM fusion rules in 2D topological superconductors and a reconciliation of non-uniqueness, finite images, and the Ising test case [14]. The present paper is a re-entry of that program with fully explicit arithmetic.

## 3. Methods

**Modular tensor category data.** A unitary modular tensor category $\mathcal{C}$ has a finite set $\mathcal{I} = \{a, b, \ldots\}$ of simple objects (anyon types) with a unit $1$, fusion coefficients $N_{ab}^{c} \in \mathbb{Z}_{\geq 0}$ defined by $a \times b = \bigoplus_c N_{ab}^{c}\, c$, quantum dimensions $d_a$ (the Perron–Frobenius eigenvector of the fusion matrices $N_a$), total quantum dimension

$$\mathcal{D} = \Big(\sum_{a \in \mathcal{I}} d_a^2\Big)^{1/2},$$

topological twists $\theta_a \in U(1)$, and modular data

$$S_{ab} = \frac{1}{\mathcal{D}} \sum_{c \in \mathcal{I}} \frac{N_{ab}^{c}\, \theta_c}{\theta_a \theta_b}, \qquad T_{ab} = \theta_a\, \delta_{ab}.$$

**Braid representation.** A simple object $x$ with fusion space $V_n = \mathrm{Hom}(1, x^{\otimes n})$ (or the full fusion space of $n$ $x$-anyons) carries a unitary representation

$$\rho_n : B_N \to U(V_n),$$

where the generator $\sigma_i$ exchanges the $i$-th and $(i{+}1)$-th anyons and acts as the $R$-matrix $R_{xx}$ composed with the fusion tree isomorphism. The reconstruction problem is: given $\rho_n$ for some or all $n$, recover $(S, T)$.

**Extraction pipeline.** Our method is: (1) compute fusion-space dimensions from the fusion rules by induction; (2) compute the braid matrices $\rho_n(\sigma_i)$ from the $R$-symbol; (3) attempt to invert: read the eigenvalues of $\rho_2(\sigma_1)$ to obtain the $R$-symbol eigenvalues $R^{xx}_{c}$; (4) use monodromy ($\sigma_1^2$ eigenvalue ratios) and the ribbon identity $\theta_{c} = $ (twist eigenvalue) to assemble $T$; (5) reconstruct $S$ from the fusion matrix $N_x$ via the Verlinde eigenvector basis, checking consistency against the $R$-derived phases. Each step is executed with explicit arithmetic in Section 4.

## 4. Analysis

### 4.1 Ising fusion rules and quantum dimensions

The Ising anyon theory has three simple objects $\mathcal{I} = \{1, \sigma, \psi\}$ with fusion rules

$$\sigma \times \sigma = 1 + \psi, \qquad \sigma \times \psi = \sigma, \qquad \psi \times \psi = 1.$$

The fusion matrix for $x = \sigma$, with rows and columns ordered $(1, \sigma, \psi)$, is

$$N_\sigma = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}.$$

Its characteristic polynomial: expanding $\det(N_\sigma - \lambda I) = -\lambda(\lambda^2 - 2) + 1 \cdot (1 \cdot (-\lambda) - 0) $; computing directly, $\det(N_\sigma - \lambda I) = -\lambda\big(\lambda^2 - 1\big) - 1\big(-\lambda\big) = -\lambda^3 + 2\lambda$, so the eigenvalues are

$$\lambda \in \{+\sqrt{2},\; -\sqrt{2},\; 0\}.$$

The Perron–Frobenius (largest-eigenvalue) eigenvector gives the quantum dimensions $d = (d_1, d_\sigma, d_\psi)$. Solving $N_\sigma d = \sqrt{2}\, d$: row $1$: $d_\sigma = \sqrt{2}\, d_1$; row $\sigma$: $d_1 + d_\psi = \sqrt{2}\, d_\sigma$; row $\psi$: $d_\sigma = \sqrt{2}\, d_\psi$. With $d_1 = 1$ by convention: $d_\sigma = \sqrt{2}$, then $d_\psi = d_\sigma/\sqrt{2} = 1$, and the middle row checks: $1 + 1 = \sqrt{2} \cdot \sqrt{2} = 2$. ✓. Hence

$$d_1 = 1, \qquad d_\sigma = \sqrt{2} \approx 1.414214, \qquad d_\psi = 1,$$

and the total quantum dimension is

$$\mathcal{D} = \sqrt{1^2 + (\sqrt{2})^2 + 1^2} = \sqrt{1 + 2 + 1} = \sqrt{4} = 2.$$

### 4.2 Fusion-space dimensions

Let $f(n, a)$ denote the dimension of the fusion space of $n$ $\sigma$ anyons with total charge $a$. By the $\mathbb{Z}_2$ symmetry of the fusion rules under relabeling $1 \leftrightarrow \psi$ (both are invertible and $\sigma \times \psi = \sigma$), $f(n,1) = f(n,\psi)$. Fusing the last anyon onto an $(n{-}1)$-anyon state:

$$f(n, 1) = f(n{-}1, \sigma), \qquad f(n, \sigma) = f(n{-}1, 1) + f(n{-}1, \psi) = 2 f(n{-}1, 1).$$

Combining, $f(n,1) = 2 f(n{-}2, 1)$, with base cases $f(0,1) = 1$ and $f(1,1) = 0$ (a single $\sigma$ cannot fuse to $1$). Therefore, for even $n$:

$$f(n, 1) = 2^{n/2 - 1}, \qquad n \text{ even},$$

giving $f(2,1) = 2^{0} = 1$, $f(4,1) = 2^{1} = 2$, $f(6,1) = 2^{2} = 4$, $f(8,1) = 2^{3} = 8$. For odd $n$, $f(n,1) = 0$ and $f(n,\sigma) = 2^{(n-1)/2}$: e.g., $f(3,\sigma) = 2$, $f(5,\sigma) = 4$. These are the Hilbert-space dimensions on which $\rho_n$ acts.

### 4.3 The braid generator and its order

The Ising $R$-symbol eigenvalues on the two-$\sigma$ fusion channels are

$$R^{\sigma\sigma}_{1} = e^{-i\pi/8}, \qquad R^{\sigma\sigma}_{\psi} = e^{3i\pi/8} = i\, e^{-i\pi/8}.$$

In the fusion basis $\{|1\rangle, |\psi\rangle\}$ of $V_2$ (with $\dim V_2 = f(2,1) = 1$ per total charge; we take the two-dimensional space spanned by both channels), the braid generator is diagonal:

$$\rho_2(\sigma_1) = e^{-i\pi/8} \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}.$$

**Order.** The diagonal part satisfies $\mathrm{diag}(1,i)^2 = \mathrm{diag}(1,-1)$ and $\mathrm{diag}(1,i)^4 = I$. The phase satisfies $(e^{-i\pi/8})^8 = e^{-i\pi} = -1$. Hence

$$\rho_2(\sigma_1)^8 = -I_2, \qquad \rho_2(\sigma_1)^{16} = I_2,$$

so the ordinary order of $\rho_2(\sigma_1)$ is $16$ and its **projective order** (order in $PU(2)$, i.e., up to phase) is $4$. This finite projective order is the fingerprint of the Gaussian, finite-image character of the Ising braid representation noted in [3].

**Trace.** $\mathrm{tr}\,\rho_2(\sigma_1) = e^{-i\pi/8}(1 + i) = e^{-i\pi/8} \cdot \sqrt{2}\, e^{i\pi/4} = \sqrt{2}\, e^{i\pi/8}$, so $|\mathrm{tr}\,\rho_2(\sigma_1)| = \sqrt{2} \approx 1.414214$.

### 4.4 Extracting $T$

The twist of $\sigma$ is read from the ribbon identity relating the $R$-symbol to the twists: for the fusion channel $c = 1$ (with $\theta_1 = 1$), the monodromy eigenvalue is $(R^{\sigma\sigma}_{1})^2 = e^{-i\pi/4}$, and the balancing equation gives $\theta_{\sigma}^2 / (\theta_1 \cdot \theta_1)$-type relations; the standard Ising values, consistent with $R^{\sigma\sigma}_\psi / R^{\sigma\sigma}_1 = i = \theta_\psi \theta_1 / \theta_\sigma^2 \cdot (\text{phase conventions})$, are

$$\theta_1 = 1, \qquad \theta_\sigma = e^{i\pi/8}, \qquad \theta_\psi = -1 = e^{i\pi}.$$

Consistency check: $\theta_\sigma^2 = e^{i\pi/4}$ and the monodromy on the $\psi$ channel is $(R^{\sigma\sigma}_{\psi})^2 = e^{3i\pi/4}$; the ratio $e^{3i\pi/4}/e^{-i\pi/4} = e^{i\pi} = -1 = \theta_\psi$, matching the mutual braiding phase of two $\sigma$ anyons fusing through $\psi$ versus $1$. ✓. Thus

$$T = \mathrm{diag}\big(1,\; e^{i\pi/8},\; -1\big).$$

Note what the braid representation alone gives us: the **ratio** $\theta_\psi/\theta_\sigma^2 \cdot \theta_\sigma^2 \ldots$ is only accessible up to an overall phase convention on each channel; the absolute phases $\theta_\sigma = e^{i\pi/8}$ versus $e^{-i\pi/8}$ (the conjugate theory $\overline{\text{Ising}}$, with opposite chiral central charge $c = \mp 1/2$) produce braid matrices that differ only by complex conjugation, which is indistinguishable from a basis relabeling without interferometric input beyond braiding.

### 4.5 Reconstructing $S$ from the fusion matrix

Since $N_\sigma$ is symmetric and real, it is diagonalized by a real orthogonal matrix. The normalized eigenvectors are:

- $\lambda = +\sqrt{2}$: $(1, \sqrt{2}, 1)^{\mathsf{T}}/\sqrt{1 + 2 + 1} = (1, \sqrt{2}, 1)^{\mathsf{T}}/2$;
- $\lambda = -\sqrt{2}$: $(1, -\sqrt{2}, 1)^{\mathsf{T}}/2$;
- $\lambda = 0$: $(1, 0, -1)^{\mathsf{T}}/\sqrt{2}$.

Assembling these as columns gives a candidate $S$-matrix (Verlinde construction):

$$S = \frac{1}{2}\begin{pmatrix} 1 & 1 & \sqrt{2} \\ \sqrt{2} & -\sqrt{2} & 0 \\ 1 & 1 & -\sqrt{2} \end{pmatrix},$$

up to permutation of columns (ordering of anyon types) and column signs. Check unitarity: row $\sigma$ has norm $(\sqrt{2}/2)^2 + (\sqrt{2}/2)^2 + 0 = 1/2 + 1/2 = 1$. ✓. Row $1$ vs row $\psi$ inner product: $\frac{1}{4} + \frac{1}{4} - \frac{2}{4} = 0$. ✓. Check Verlinde: $N_\sigma = S\, \mathrm{diag}(\sqrt{2}, -\sqrt{2}, 0)\, S^{\mathsf{T}}$, which holds by construction. The standard convention (permuting columns to $(1,\sigma,\psi)$ order and fixing signs by $S_{1a} > 0$) yields

$$S = \frac{1}{2}\begin{pmatrix} 1 & \sqrt{2} & 1 \\ \sqrt{2} & 0 & -\sqrt{2} \\ 1 & -\sqrt{2} & 1 \end{pmatrix}.$$

**The ambiguity.** The fusion ring determines $S$ only up to: (a) column/row sign flips consistent with $S_{1a} > 0$ being imposed by convention, and (b) Galois conjugation — applying an automorphism of the cyclotomic field $\mathbb{Q}(e^{i\pi/8})$ to all entries. The braid representation fixes some of this: the eigenvalue data of $\rho_2(\sigma_1)$ distinguishes the $+\sqrt{2}$ from the $-\sqrt{2}$ channel only if we can label which fusion channel carries which $R$-phase, which requires the $F$-symbol data, not braiding alone. This is the precise locus of non-uniqueness.

### 4.6 Non-uniqueness: the $SO(N)_2$ family

Rowell [3] shows that for the pre-modular categories $SO(N)_2$ ($N$ odd) and $O(N)_2$ ($N$ even), the braid representations on tensor powers of the spin object are Gaussian with finite image, with centralizer algebras described by quantum $(n{-}1)$-tori. The spin object of $SO(N)_2$ (odd $N$) has Ising-type local fusion: the braid representation generated on $n$ spin anyons is, projectively, the same Gaussian representation as the Ising one — same projective generator order $4$, same finite image structure. Yet the categories $SO(N)_2$ for different $N$ have different simple-object content and different modular data (for $N$ even the category $O(N)_2$ is even a pre-modular, non-modular category with nontrivial transparent objects). Hence:

$$\rho_n^{SO(N)_2} \cong \rho_n^{\mathrm{Ising}} \text{ (projectively, on spin anyons)} \quad \Longrightarrow \quad (S, T)_{SO(N)_2} \neq (S,T)_{\mathrm{Ising}}.$$

The same mechanism operates for twisted quantum doubles of finite groups [2], whose braid representations factor through finite groups and can coincide as representations while the underlying doubles differ; and gauging constructions [5] double the anyon content (changing $\mathcal{D}$ and $S$) while leaving the ungauged braid sector intact. Concretely, for Ising $\mathcal{D} = 2$ (computed above); a $\mathbb{Z}_2$ gauging of Ising (the $\mathrm{Ising} \times \overline{\mathrm{Ising}}$-type double) has $\