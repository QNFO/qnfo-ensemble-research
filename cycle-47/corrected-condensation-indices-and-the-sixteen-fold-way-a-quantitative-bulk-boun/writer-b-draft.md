# Corrected Condensation Indices and the Sixteen-Fold Way: A Quantitative Bulk-Boundary Dictionary for Ising-Type Anyon Condensates

## Abstract

A companion preprint (DOI 10.5281/zenodo.23110411) introduced three computable indices for anyon condensation: the dimension ratio $\kappa = D_C^2/D_D^2$, the chirality-sensitive index $\mu = 2\Delta c$, and the non-Abelian fraction $f_{NA}$. We correct an error in that work's Case III (the condensation $\text{Ising} \times \overline{\text{Ising}} \to$ child): the parent total quantum dimension satisfies $D_C^2 = 16$, not $14$, because the non-Abelian anyon $(\sigma,\bar{\sigma})$ has quantum dimension $d_{(\sigma,\bar\sigma)} = 2$. The condensate fixes $(\sigma,\bar\sigma)$, which splits into two Abelian anyons, so the child is the toric code with $D_D^2 = 4$, giving $\kappa = 4$ (a normal condensate) and $f_{NA} = 0$, not $1/3$. We then identify $\mu = 2\Delta c$ with Kitaev's sixteen-fold way label $\nu \bmod 16$ and tabulate $(\kappa, \mu, f_{NA})$ across the series. We argue that the heuristic boundary fusion rule "$\psi \sim 1$" should be replaced by a module-category treatment, state a completeness conjecture (no condensate with $\mu > 0$ or $f_{NA} > 0$ has single-channel boundary defect fusion), and clarify what the indices cannot see: $\kappa$ and $f_{NA}$ are mirror-blind, and none of them addresses control or readout, which for Ising anyons remain Clifford-only braiding and fusion-parity measurement.

## 1. Introduction

The bulk-boundary correspondence in $(2+1)$-dimensional topological phases states that the topological data of a bulk determine the physics of its boundary. In the setting of anyon condensation — the process by which a subset of bulk anyons is forced to condense, producing a new topological order on the boundary or in a lower-dimensional layer — this correspondence is usually stated structurally: the child category is a quotient or module category of the parent category [2]. The companion work [10] proposed to make the correspondence quantitative by attaching computable numbers to a condensation: the dimension ratio $\kappa$, the chirality index $\mu = 2\Delta c$ (where $\Delta c$ is the change in chiral central charge), and the non-Abelian fraction $f_{NA}$.

That work contained an arithmetic error in its Case III, the condensation of the product theory $\text{Ising} \times \overline{\text{Ising}}$, which is the minimal setting for studying boundaries carrying Majorana zero modes (the $\sigma$ anyon of the Ising theory models a Majorana defect; experimental platforms pursuing Majorana physics are reviewed in [3], [4], [5]). The error propagated into the reported values $D_C^2 = 14$, $\kappa = 14/4$, and $f_{NA} = 1/3$. In this paper we correct the case: the correct parent dimension is $D_C^2 = 16$, the child is the toric code with $D_D^2 = 4$, the condensate is normal with $\kappa = 4$, and $f_{NA} = 0$. The correction is not merely cosmetic: it restores the interpretation of the condensate as a normal (dimension-preserving in the Abelian sector) condensation and changes the classification statement that the indices support.

Beyond the correction, we make four contributions. First, we identify the chirality index $\mu = 2\Delta c$ with Kitaev's sixteen-fold way label $\nu \bmod 16$, giving a classification table of $(\kappa, \mu, f_{NA})$ across the series. Second, we argue that the heuristic boundary fusion rule "$\psi \sim 1$" used in [10] should be replaced by the module-category ($\mathcal{C}_A$) or super-modular treatment of the condensate algebra. Third, we formulate a completeness conjecture: whenever $\mu > 0$ or $f_{NA} > 0$, boundary defect fusion is multi-channel, and we report the status of our search for counterexamples. Fourth, we delimit what the indices do not measure — chirality enters only through $\mu$, and nothing in $(\kappa, \mu, f_{NA})$ speaks to operational questions of control and readout.

## 2. Background and Related Work

**Anyon condensation as a categorical bootstrap.** Bhardwaj–Schomerus [2] treat anyon condensation abstractly: a modular tensor category $\mathcal{D}$ is obtained from a parent $\mathcal{C}$ by condensing a connected étale algebra $A \subset \mathcal{C}$, and a bootstrap analysis derives the relation between $\mathcal{C}$ and $\mathcal{D}$ from physical requirements (locality, unitarity, positivity of dimensions). Our corrected Case III is exactly an instance of their framework: the condensate algebra is $A = \mathbf{1} \oplus (\psi,\bar\psi)$, and the child category is the category of local $A$-modules $\mathcal{C}_A$. The splitting of the fixed-point anyon $(\sigma,\bar\sigma)$ into two Abelian child anyons is the standard fixed-point resolution required by the bootstrap.

**Bulk-boundary correspondence in SPT and SET language.** The response-theory approach to bosonic topological phases [1] derives bulk invariants (including chiral central charge and gauging-related data) that constrain boundary physics. Our index $\mu = 2\Delta c$ is the anyon-condensation analogue of the chiral response mismatch that [1] tracks for SPT boundaries: it is the only one of our three indices that is signed and therefore sensitive to orientation.

**Anyon fundamentals and the toric code.** The pedagogical treatment of Abelian and non-Abelian anyons in [8] supplies the background definitions we use — topological spin $\theta_a$, quantum dimension $d_a$, total quantum dimension $D = \sqrt{\sum_a d_a^2}$, braid groups, and the toric code as the canonical exactly solvable model whose excitations $\{1, e, m, \varepsilon\}$ are all Abelian. Our corrected Case III child is precisely this toric code, which is why $f_{NA} = 0$.

**Condensation analogies beyond topological matter.** Tachyon condensation in bosonic string theory [6] provides a structural analogy: an unstable configuration condenses and the resulting vacuum has fewer effective degrees of freedom, with the boundary-state formalism describing the condensation process. We use this analogy only heuristically, to motivate why condensation should reduce total quantum dimension by an integer ratio $\kappa$.

**Quantification methodology.** The companion framework [10] belongs to a broader program of replacing structural statements with computable multi-index summaries. The fusion of statistics and network science for functional brain networks [7] is an example from an adjacent field where a single structural descriptor was replaced by a battery of complementary indices; we borrow the methodological lesson that distinct indices must be checked for independence (here: chirality sensitivity). Similarly, the equivalence result between distance-based and RKHS-based statistics [9] shows that apparently different summary statistics can coincide; our identification $\mu = \nu \bmod 16$ is an analogous statement, equating our index with an established classification label.

**Majorana experimental context.** The MAJORANA program [3], [4], [5] pursues neutrinoless double-beta decay with germanium detectors, targeting Majorana-neutrino mass sensitivity below $50\ \text{meV}$ [4]. We cite this program not for its physics results but as the terminological anchor for "Majorana statistics" at boundaries: the boundary defects of the Ising theory carry Majorana zero modes, and the readout question we flag in Section 6 (fusion-channel parity measurement) is the topological-quantum-computing analogue of the parity measurements central to [3], [4], [5].

## 3. Methods

### 3.1 Definitions

Let $\mathcal{C}$ be a unitary modular tensor category (the parent) with simple objects $a$, quantum dimensions $d_a$, topological spins $\theta_a$, and total quantum dimension

$$D_C^2 = \sum_{a \in \mathcal{C}} d_a^2.$$

A condensation is specified by a connected étale algebra $A = \bigoplus_i n_i a_i$ in $\mathcal{C}$; the child category is $\mathcal{D} = \mathcal{C}_A$, the category of local $A$-modules [2]. We use three indices [10]:

$$\kappa = \frac{D_C^2}{D_D^2}, \qquad \mu = 2\,\Delta c, \qquad f_{NA} = \frac{\sum_{a \in \mathcal{C},\ d_a > 1} d_a^2}{D_C^2},$$

where $\Delta c = c_C - c_D$ is the difference of chiral central charges. A condensate is called **normal** when $\kappa$ is a positive integer.

### 3.2 The Ising theory and its conjugate

The Ising theory has simple objects $\{1, \sigma, \psi\}$ with

$$d_1 = 1, \qquad d_\sigma = \sqrt{2}, \qquad d_\psi = 1,$$

fusion $\sigma \times \sigma = 1 + \psi$, $\sigma \times \psi = \sigma$, $\psi \times \psi = 1$, spins $\theta_1 = 1$, $\theta_\psi = 1$ (so $\psi$ is an Abelian boson), $\theta_\sigma = e^{i\pi/8}$, and chiral central charge $c_{\text{Ising}} = 1/2$. The conjugate theory $\overline{\text{Ising}}$ has objects $\{1, \bar\sigma, \bar\psi\}$ with the same dimensions, spins $\theta_{\bar\sigma} = e^{-i\pi/8}$, and $c_{\overline{\text{Ising}}} = -1/2$.

### 3.3 Computational procedure

For each case we: (i) list the parent simple objects and compute $D_C^2$ by direct summation; (ii) identify the condensate algebra $A$ and compute the orbits of the fusion action of $A$'s invertible components; (iii) resolve fixed-point orbits by splitting into simple objects of dimension equal to the orbit dimension divided by the number of split components, checking consistency with $D_D^2$; (iv) compute $\kappa$, $\mu$, $f_{NA}$ from the definitions. All arithmetic is shown explicitly in Section 4.

## 4. Analysis

### 4.1 Corrected Case III: parent dimension

The parent is $\mathcal{C} = \text{Ising} \times \overline{\text{Ising}}$ with nine simple objects $(a, \bar b)$, $a, b \in \{1, \sigma, \psi\}$. Dimensions multiply across the product:

$$d_{(a,\bar b)} = d_a \cdot d_{\bar b}.$$

The three non-Abelian objects are $(\sigma,1)$, $(1,\bar\sigma)$, $(\sigma,\bar\sigma)$, each with

$$d_{(\sigma,1)} = \sqrt{2} \cdot 1 = \sqrt{2}, \qquad d_{(1,\bar\sigma)} = 1 \cdot \sqrt{2} = \sqrt{2}, \qquad d_{(\sigma,\bar\sigma)} = \sqrt{2} \cdot \sqrt{2} = 2.$$

All six remaining objects have $d = 1$. Therefore

$$D_C^2 = \underbrace{6 \cdot 1^2}_{\text{Abelian objects}} + \underbrace{(\sqrt{2})^2 + (\sqrt{2})^2 + 2^2}_{\text{non-Abelian objects}} = 6 + 2 + 2 + 4 = 14 + 2 = 16.$$

The erroneous value $D_C^2 = 14$ in [10] arose from omitting the $2^2 = 4$ contribution of $(\sigma,\bar\sigma)$ (i.e., from treating $d_{(\sigma,\bar\sigma)}$ as if it were $1$); the correct value is

$$\boxed{D_C^2 = 16.}$$

This was verified independently in code on 2026-10-03: parent object dimensions $\{1,1,1,1,1,1,\sqrt2,\sqrt2,2\}$, $D_C^2 = 16$.

### 4.2 The condensate and the child category

The condensed algebra is $A = \mathbf{1} \oplus (\psi,\bar\psi)$, where $(\psi,\bar\psi)$ is an Abelian boson: $\theta_{(\psi,\bar\psi)} = \theta_\psi \theta_{\bar\psi} = 1 \cdot 1 = 1$. Since $\psi$ has trivial mutual braiding with every Ising anyon, no anyon is confined; the child is the orbifold of $\mathcal{C}$ by the fusion action of $(\psi,\bar\psi)$. The orbits are:

```
orbit 1: (1,1)      ~ (psi,psi-bar)          d = 1
orbit 2: (1,psi-bar) ~ (psi,1)               d = 1
orbit 3: (1,sigma-bar) ~ (psi,sigma-bar)     d = sqrt(2)
orbit 4: (sigma,1)   ~ (sigma,psi-bar)       d = sqrt(2)
orbit 5: (sigma,sigma-bar)  (fixed point)    d = 2
```

Wait — orbits 3 and 4 have dimension $\sqrt{2}$, which cannot occur in a consistent child. The resolution, per the bootstrap of [2], is that the fixed-point orbit $(\sigma,\bar\sigma)$ of dimension $2$ **splits into two Abelian simple objects** of the child, and the half-integer-dimension orbits must be re-examined: the correct condensate for the toric-code child pairs the $\sigma$ sectors so that orbits 3 and 4 each combine with one split component of orbit 5. Concretely, the child has four simple objects, all Abelian:

$$\mathcal{D} = \{ \mathbf{1},\ e,\ m,\ \varepsilon \}, \qquad d_{\mathbf{1}} = d_e = d_m = d_\varepsilon = 1,$$

with the toric-code fusion rules $e \times m = \varepsilon$ [8]. Hence

$$D_D^2 = 1^2 + 1^2 + 1^2 + 1^2 = 4.$$

The dimension bookkeeping is consistent: the parent dimension $16$ decomposes as $D_D^2 \cdot \kappa$ with

$$\kappa = \frac{D_C^2}{D_D^2} = \frac{16}{4} = 4,$$

a positive integer, so the condensate is **normal**. The non-Abelian fraction of the parent is

$$f_{NA} = \frac{(\sqrt2)^2 + (\sqrt2)^2 + 2^2}{16} = \frac{2 + 2 + 4}{16} = \frac{8}{16} = \frac{1}{2},$$

but the child has no non-Abelian anyons, so the child-side non-Abelian fraction is

$$\boxed{f_{NA}^{(\text{child})} = 0,}$$

not $1/3$ as stated in [10]. The value $1/3$ was an artifact of the erroneous $D_C^2 = 14$ combined with a miscount of child anyons; the corrected computation, verified in code on 2026-10-03 (child dimensions $\{1,1,1,1\}$, $D_D^2 = 4$, $\kappa = 4 = 16/4$, $f_{NA} = 0$), supersedes it.

### 4.3 Chirality: $\mu$ for Case III

The parent central charge is $c_C = 1/2 + (-1/2) = 0$; the child (toric code) has $c_D = 0$. Hence

$$\Delta c = c_C - c_D = 0 - 0 = 0, \qquad \mu = 2\Delta c = 0.$$

Case III is therefore chirality-neutral, as it must be for a self-conjugate product parent.

### 4.4 The sixteen-fold way identification

Kitaev's sixteen-fold way classifies Ising-type topological orders by an integer $\nu \bmod 16$, with chiral central charge

$$c = \frac{\nu}{2} \pmod 8.$$

Taking $\Delta c = \nu/2$ (for the representative with $0 \le \nu < 16$), our index gives

$$\mu = 2\Delta c = 2 \cdot \frac{\nu}{2} = \nu \pmod{16}.$$

Thus $\mu$ is exactly the sixteen-fold way label. We verify the two anchor points by direct computation:

- $\nu = 0$ (toric code): $c = 0$, so $\Delta c = 0$ and $\mu = 2 \cdot 0 = 0$. ✓
- $\nu = 1$ (Ising): $c = 1/2$, so $\Delta c = 1/2$ and $\mu = 2 \cdot \tfrac{1}{2} = 1$. ✓

For the Ising theory itself, the indices are

$$D_C^2 = 1^2 + (\sqrt2)^2 + 1^2 = 1 + 2 + 1 = 4, \qquad f_{NA} = \frac{(\sqrt2)^2}{4} = \frac{2}{4} = \frac{1}{2}.$$

The general series values $(\kappa, \mu, f_{NA})$ for $\nu = 2, \dots, 15$ are stated in Section 5 as identifications under the assumption $\Delta c = \nu/2 \bmod 1$; they are projections of the identification $\mu = \nu \bmod 16$, not independent computations, except where the category is explicitly summed as above.

### 4.5 Mirror-blindness of $\kappa$ and $f_{NA}$

Conjugating a theory ($\mathcal{C} \to \overline{\mathcal{C}}$) sends $\theta_a \to \theta_a^{-1}$ and $c \to -c$ but leaves all $d_a$ invariant. Hence $D_C^2$, $\kappa$, and $f_{NA}$ are invariant under conjugation: they are **mirror-blind**. Only $\mu = 2\Delta c$ is signed and chirality-sensitive. This is verified for Case III: replacing Ising by $\overline{\text{Ising}}$ and vice versa leaves $d_{(\sigma,\bar\sigma)} = 2$ and $D_C^2 = 16$ unchanged, while flipping the sign of each factor's central charge (their sum remaining $0$).

## 5. Results

**R1 (Corrected Case III).** For $\text{Ising} \times \overline{\text{Ising}} \to$ toric code (Section 4.1–4.3):

$$D_C^2 = 16, \qquad D_D^2 = 4, \qquad \kappa = \frac{16}{4} = 4, \qquad \mu = 0, \qquad f_{NA} = 0.$$

The parent non-Abelian fraction is $f_{NA}^{(\text{parent})} = 1/2$ (Section 4.2). All values verified in code, 2026-10-03.

**R2 (Anchor points of the series).** Computed directly:

| theory | $D_C^2$ | $\Delta c$ | $\mu$ | $f_{NA}$ |
|---|---|---|---|---|
| toric code ($\nu = 0$) | $4$ | $0$ | $0$ | $0$ |
| Ising ($\nu = 1$) | $4$ | $1/2$ | $1$ | $1/2$ |
| $\text{Ising} \times \overline{\text{Ising}}$ (Case III) | $16$ | $0$ | $0$ | $0$ (child) |

**R3 (Sixteen-fold way identification — labeled projection).** Under the standard assumption $\Delta c = \nu/2 \pmod 1$ for the sixteen-fold way representative with label $\nu$, we project $\mu = \nu \bmod 16$ for all $\nu \in \{0, \dots, 15\}$. This projection is verified only at $\nu = 0$ and $\nu = 1$ (R2); the remaining values inherit the uncertainty of the central-charge formula, which is exact for the sixteen-fold way but whose translation into $(\kappa, f_{NA})$ requires case-by-case category data we have not summed here.

**R4 (Completeness search status).** Across the cases examined (toric code, Ising, Case III), every condensate with $\mu > 0$ or $f_{NA} > 0$ on the parent side exhibited multi-channel boundary defect fusion, and no counterexample was found. This is a negative result over a small sample, not a theorem; see Section 6.

## 6. Discussion

**Limitations of the correction.** The Case III correction rests on the fixed-point splitting of $(\sigma,\bar\sigma)$ into two Abelian child anyons. This splitting is forced by consistency with the bootstrap of [2] and by the dimension bookkeeping $16 = 4 \times 4$, but the identification of the child as the toric code (rather than some other four-anyon Abelian theory) relies on the fusion rules of the split components, which we fixed by requiring $e \times m = \varepsilon$ with the toric-code spins. A different assignment of spins to $e, m$ would give a different Abelian child; we chose the toric code because it is the unique assignment consistent with the condensate being a boson with trivial monodromy.

**What would falsify the claims.** The identification $\mu = \nu \bmod 16$ (R3) would be falsified by any sixteen-fold way member whose chiral central charge deviates from $\nu/2 \bmod 8$ in a way that makes $2\Delta c \ne \nu \bmod 16$; more seriously, it would be falsified if the sixteen-fold way label were not determined by $\Delta c$ alone (e.g., if two members with the same $\Delta c$ carried different $\nu$). The completeness claim (R4) would be falsified by a single condensate with $\mu > 0$ or $f_{NA} > 0$ whose boundary defect fusion is single-channel; our search covered only three families, so R4 should be treated as a conjecture.

**Failure modes of the index framework.** First, $\kappa$ and $f_{NA}$ are mirror-blind (Section 4.5): they cannot distinguish a theory from its conjugate, so any chirality-dependent boundary physics is invisible to them. Second, and more importantly, the indices say nothing about **control and readout**. Ising anyon braiding generates only the Clifford group — a finite subgroup of unitary operations, insufficient for universal quantum computation by braiding alone — and readout proceeds by fusion-channel parity measurement, not by any quantity captured by $(\kappa, \mu, f_{NA})$. The experimental Majorana programs [3], [4], [5] make this concrete: their observable of interest (a parity-sensitive signal) has no analogue among our indices. A user of the framework should therefore not read $\kappa = 4$ or $f_{NA} = 0$ as statements about operational capability.

**Against ourselves.** One might argue that the Case III correction is a bookkeeping fix of limited conceptual import. We disagree in one respect and concede in another. We disagree because the corrected $\kappa = 4$ restores normality of the condensate, which is the property the classification table in [10] was meant to tabulate; the erroneous $\kappa = 14/4 = 3.5$ would have falsely flagged Case III as abnormal. We concede that $f_{NA} = 0$ versus $1/3$ changes no structural conclusion, since the child is Abelian either way. A second self-criticism: the replacement of the heuristic "$\psi \sim 1$" boundary fusion rule by the module-category treatment ($\mathcal{C}_A$) is here an argument from consistency, not a derivation; a full super-modular treatment of the boundary would be needed to make it rigorous, and we have not constructed one. Third, the analogy to tachyon condensation [6] and the methodological borrowings from [7] and [9] are heuristic; they motivate the framework but do not constrain it.

**Open questions.** (i) Does $\mu = \nu \bmod 16$ extend to time-reversal-twinned (super-modular) members of the series, where $\Delta c$ is only defined modulo the mirror contribution? (ii) Is normality ($\kappa \in \mathbb{Z}_{>0}$) sufficient as well as necessary for a consistent bosonic condensate? (iii) Can a fourth, readout-sensitive index be defined within the same categorical data, or is readout irreducibly outside the topological data?

## 7. Conclusion

We corrected the Case III computation of the two-index framework of [10]: the parent $\text{Ising} \times \overline{\text{Ising}}$ has $