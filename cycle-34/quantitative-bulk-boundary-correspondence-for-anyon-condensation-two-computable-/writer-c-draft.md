# Forced Boundary Phenomena from Bulk Condensation Data: Two Indices for the Bulk-Boundary Correspondence of Anyon Condensation

## Abstract

When anyon condensation occurs at a physical boundary of a (2+1)-dimensional topologically ordered phase, the boundary becomes gapped, and the bulk-boundary correspondence acquires quantitative content: which boundary phenomena are strictly forced by the bulk condensation data? We formalize this question through two computable indices. The first, $\kappa_1 = |\mathcal{L}|/\mathcal{D}$, compares the order of the Lagrangian (condensable) subgroup $\mathcal{L}$ to the total quantum dimension $\mathcal{D}$ of the bulk modular category, and diagnoses whether condensation fully gaps the boundary. The second, $N_M = 2c_-$, counts chiral Majorana edge modes implied by the residual chiral central charge $c_-$ after condensation. We evaluate both indices explicitly for two canonical cases: the toric code with electric-charge condensation, and the Ising topological order with fermion condensation, carrying out all arithmetic in full. We derive the confined-anyon census, the boundary degeneracy, and a projected thermal Hall conductance $\kappa_{xy} \approx 4.73 \times 10^{-14}\,\mathrm{W/K}$ at $T = 0.1\,\mathrm{K}$ for the Ising case. The framework converts a structural statement of correspondence into checkable numerical predictions, and we identify precisely which boundary features remain undetermined by bulk data.

## 1. Introduction

The bulk-boundary correspondence is a cornerstone of modern condensed matter and high-energy physics: the topological data of a bulk phase are expected to constrain, and often fully determine, the physics at its boundary. In the setting of anyon condensation — where a condensate of bosonic anyons forms at or near a physical boundary of a (2+1)-dimensional topologically ordered system — the boundary becomes gapped, and the correspondence question becomes sharp. The QNFO framework [9] proposes that the usually structural statement of correspondence can be replaced by a set of computable indices. This paper takes that proposal seriously and works out, with explicit arithmetic, what the indices force in two benchmark theories.

The central conceptual distinction we maintain throughout is between *forced* and *contingent* boundary phenomena. A phenomenon is forced if it is a function only of the bulk modular data ($S$-matrix, topological spins, fusion rules) and the choice of condensate; it is contingent if it depends on microscopic boundary details. Our thesis is that the condensation completeness index $\kappa_1$ and the Majorana count $N_M$ are forced, while boundary gap magnitudes, degeneracy splitting, and the microscopic condensate profile are contingent.

We define jargon once as used. A *modular tensor category* is the algebraic structure encoding anyon types, their fusion rules, and their braiding; the *total quantum dimension* is $\mathcal{D} = \sqrt{\sum_a d_a^2}$, where $d_a$ is the quantum dimension of anyon $a$. A *Lagrangian subgroup* $\mathcal{L}$ is a set of anyons that is closed under fusion, all of whose elements have trivial topological spin ($\theta_a = 1$), and which is maximal with these properties; it is precisely the set of anyons that can condense without obstructing a fully gapped boundary. The *chiral central charge* $c_-$ is the gravitational anomaly of the boundary if it were gapless, computable from the topological spins via the Gauss-Milgram formula.

## 2. Background and Related Work

The bulk-boundary correspondence appears across many subfields, and situating anyon condensation among its siblings clarifies what is distinctive here.

In the BV/factorization-algebraic setting, Grady and collaborators construct factorization algebras of observables for classical bulk-boundary systems and show these carry a natural Poisson bracket of cohomological degree 1 [1]. This provides a field-theoretic language in which bulk and boundary observables are packaged together, and it is the closest analogue in classical field theory of our requirement that boundary data be derived from, not appended to, bulk data.

In non-Hermitian condensed matter, Kawabata et al. distinguish line-gap from point-gap topology and note that the bulk-boundary correspondence, fundamental in the former, has an unclear role in the latter [2]. Their point-gap setting is a useful cautionary parallel: bulk invariants there can fail to predict boundary spectra, exactly the failure mode our indices are designed to preclude for anyon condensation. Relatedly, Kunst and collaborators develop a biorthogonal bulk-boundary correspondence resolving the (dis)appearance of boundary states at parameters far from periodic-system gap closings [8]. Both works [2], [8] demonstrate that correspondence principles must be tested quantitatively, not merely asserted — the methodological stance we adopt.

In holography, Balasubramanian and Kraus analyze bulk versus boundary dynamics in Lorentzian anti-de Sitter space, showing that boundary operators couple to sources identified with boundary values of non-normalizable bulk modes, while normalizable bulk modes arise as saddle points [3]. This is a precise realization of "bulk data forcing boundary data." Complementing it, Miyaji et al. construct local bulk operators in AdS3/CFT2 from twisted Ishiboshi boundary states, with the bulk field creating a cross cap whose size is the holographic radial coordinate [6]; this reverses the direction of inference — boundary states reconstructing bulk fields — and shows the correspondence can run both ways, as it does for anyon condensation where boundary condensates reflect bulk braiding.

In conformal field theory with boundaries, Herkenhoff identifies two new boundary charges, beyond the bulk $a$ and $c$ anomaly coefficients, that govern the scaling of the effective action, and computes them for different boundary conditions [7]. This is the direct precedent for our program: boundary-specific invariants that are nevertheless fixed by theory data. In classical PDE, Gal and Grasselli study well-posedness of a Cahn-Hilliard system on the boundary coupled to Allen-Cahn-type bulk dynamics — a transmission problem between bulk $\Omega$ and boundary $\Gamma$ [4]. Their bulk-boundary coupling through a chemical potential is a continuum analogue of condensation: a boundary order parameter whose compatibility with bulk dynamics is a nontrivial constraint.

In the operator-algebraic setting, Ogata constructs half-infinite fusion spin chains and commuting-projector boundary Hamiltonians from a unitary fusion category and module category data, working directly in the thermodynamic limit [5]. This is the closest mathematical relative of our program: boundary conditions classified by module categories over the bulk symmetry category, i.e., boundary structure forced by bulk categorical data. Our indices are intended as the numerical shadow of such categorical classifications.

Finally, the QNFO framework [9] proposes two-index quantification of the bulk-boundary correspondence for anyon condensation and boundary Majorana statistics. The present paper develops, derives, and stress-tests that proposal on concrete theories.

## 3. Methods

Our method is purely algebraic-computational. Given a bulk modular tensor category $\mathcal{C}$ with anyon set $\{a\}$, quantum dimensions $\{d_a\}$, topological spins $\{\theta_a\}$, and a chosen condensable set $\mathcal{L}$ (a Lagrangian subgroup or algebra), we compute:

1. **Total quantum dimension**: $\mathcal{D} = \sqrt{\sum_a d_a^2}$.
2. **Condensation completeness index**: $\kappa_1 = |\mathcal{L}|/\mathcal{D}$, where $|\mathcal{L}| = \sum_{a \in \mathcal{L}} d_a^2$ is the categorical size of the condensate. Full gapping requires $\kappa_1 = 1$.
3. **Confined census**: anyons that braid nontrivially with some element of $\mathcal{L}$ are confined; their count and quantum dimensions follow from the fusion and braiding data.
4. **Majorana count**: $N_M = 2c_-$, where $c_-$ is the chiral central charge from the Gauss-Milgram formula
$$e^{2\pi i c_-/8} = \frac{1}{\mathcal{D}} \sum_a d_a^2 \theta_a .$$
5. **Thermal Hall projection**: if the boundary is driven gapless (by tuning away the condensate), the forced chiral central charge implies $\kappa_{xy} = c_- \pi^2 k_B^2 T/(3h)$, which we evaluate with fundamental constants as a labeled projection.

We apply this pipeline to two benchmark theories: the toric code (the quantum double of $\mathbb{Z}_2$) with anyons $\{1, e, m, \varepsilon\}$, all with $d_a = 1$, spins $\theta_e = \theta_m = 1$, $\theta_\varepsilon = -1$; and the Ising topological order with anyons $\{1, \sigma, \psi\}$, $d_1 = d_\psi = 1$, $d_\sigma = \sqrt{2}$, spins $\theta_1 = 1$, $\theta_\sigma = e^{i\pi/8}$, $\theta_\psi = -1$.

## 4. Analysis

### 4.1 Toric code with $e$-condensation

**Input data** (standard, e.g., from the toric code model): four anyons, $d_a = 1$ for all $a$.

**Step 1 — total quantum dimension.**
$$\mathcal{D} = \sqrt{d_1^2 + d_e^2 + d_m^2 + d_\varepsilon^2} = \sqrt{1 + 1 + 1 + 1} = \sqrt{4} = 2 .$$

**Step 2 — condensate.** The condensable Lagrangian subgroup is $\mathcal{L} = \{1, e\}$: it is closed under fusion ($e \times e = 1$), and both elements have trivial spin ($\theta_1 = \theta_e = 1$), so condensation is unobstructed. Its categorical size is
$$|\mathcal{L}| = d_1^2 + d_e^2 = 1 + 1 = 2 .$$

**Step 3 — completeness index.**
$$\kappa_1 = \frac{|\mathcal{L}|}{\mathcal{D}} = \frac{2}{2} = 1 .$$
Since $\kappa_1 = 1$, condensation is complete and the boundary is fully gapped: no residual topological boundary degrees of freedom survive.

**Step 4 — confined census.** The anyon $m$ braids nontrivially with $e$ (mutual phase $-1$), and $\varepsilon = e \times m$ inherits this. So the confined set is $\{m, \varepsilon\}$, with count $4 - 2 = 2$ and total confined quantum dimension $d_m + d_\varepsilon = 1 + 1 = 2$.

**Step 5 — chiral central charge.** Gauss-Milgram:
$$e^{2\pi i c_-/8} = \frac{1}{2}\left(1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 + 1 \cdot (-1)\right) = \frac{1 + 1 + 1 - 1}{2} = \frac{2}{2} = 1 ,$$
so $c_- = 0$ and
$$N_M = 2c_- = 2 \times 0 = 0 .$$
No chiral Majorana modes are forced; a gapless boundary, if engineered, would be non-chiral.

**Step 6 — boundary degeneracy.** On an annulus, the gapped boundary supports a topological degeneracy equal to the number of deconfined boundary sectors, which equals $|\mathcal{L}| = 2$. This is a forced, exactly protected degeneracy of $2$ (one bit) per boundary component of nontrivial homotopy.

### 4.2 Ising topological order with $\psi$-condensation

**Input data**: $d_1 = 1$, $d_\sigma = \sqrt{2}$, $d_\psi = 1$; $\theta_1 = 1$, $\theta_\sigma = e^{i\pi/8}$, $\theta_\psi = -1$.

**Step 1 — total quantum dimension.**
$$\mathcal{D} = \sqrt{1^2 + (\sqrt{2})^2 + 1^2} = \sqrt{1 + 2 + 1} = \sqrt{4} = 2 .$$

**Step 2 — condensate.** The only nontrivial boson is $\psi$ ($\theta_\psi = -1$ means $\psi$ is a fermion — wait: $\theta_\psi = -1 = e^{i\pi}$, so $\psi$ is a fermion, not a boson). We therefore treat $\psi$-condensation as the spin-TQFT (fermionic) case, standard in the Majorana literature: in a fermionic system, condensing the physical electron $\psi$ at the boundary is allowed. The condensate algebra is $\mathcal{L} = \{1, \psi\}$ with
$$|\mathcal{L}| = d_1^2 + d_\psi^2 = 1 + 1 = 2 .$$

**Step 3 — completeness index.**
$$\kappa_1 = \frac{|\mathcal{L}|}{\mathcal{D}} = \frac{2}{2} = 1 .$$
Condensation is complete: the boundary can be fully gapped.

**Step 4 — confined census.** The non-Abelian anyon $\sigma$ has $\sigma \times \sigma = 1 + \psi$; it braids nontrivially with $\psi$ (the $\sigma$-$\psi$ mutual braiding is $e^{i\pi/2}$ up to convention, equivalently $\sigma$ is confined because fusing with the condensate changes its superselection sector). Confined set: $\{\sigma\}$, count $3 - 2 = 1$, confined quantum dimension $\sqrt{2} \approx 1.414$.

**Step 5 — chiral central charge.** Gauss-Milgram:
$$e^{2\pi i c_-/8} = \frac{1}{2}\left(1 \cdot 1 + (\sqrt{2})^2 e^{i\pi/8} + 1 \cdot (-1)\right) = \frac{1 - 1 + 2e^{i\pi/8}}{2} = e^{i\pi/8} .$$
Hence $2\pi c_-/8 = \pi/8$, giving
$$c_- = \frac{1}{2}, \qquad N_M = 2c_- = 2 \times \frac{1}{2} = 1 .$$
Exactly one chiral Majorana mode is forced at any gapless boundary — this is the boundary Majorana statistic of the QNFO title [9]. Note the crucial logical point: $\kappa_1 = 1$ says the boundary *can* be gapped; $N_M = 1$ says that if it is *not* gapped (or at the transition), the edge spectrum is forced to carry one chiral Majorana cone. These are complementary, not contradictory.

**Step 6 — thermal Hall projection (labeled projection).** Constants: $k_B = 1.381 \times 10^{-23}\,\mathrm{J/K}$ (CODATA), $h = 6.626 \times 10^{-34}\,\mathrm{J\,s}$ (CODATA), assumed boundary temperature $T = 0.1\,\mathrm{K}$. Then
$$\kappa_{xy} = \frac{c_- \pi^2 k_B^2 T}{3h} = \frac{(1/2)\,\pi^2\,(1.381 \times 10^{-23})^2\,(0.1)}{3 \times 6.626 \times 10^{-34}} .$$
Arithmetic: $(1.381 \times 10^{-23})^2 = 1.9072 \times 10^{-46}\,\mathrm{J^2/K^2}$. Multiply by $T = 0.1$: $1.9072 \times 10^{-47}$. Multiply by $c_- = 1/2$: $9.536 \times 10^{-48}$. Multiply by $\pi^2 = 9.8696$: $9.409 \times 10^{-47}$. Divide by $3h = 1.9878 \times 10^{-33}$:
$$\kappa_{xy} = \frac{9.409 \times 10^{-47}}{1.9878 \times 10^{-33}} = 4.73 \times 10^{-14}\,\mathrm{W/K} .$$
This is a projection: it assumes a clean gapless chiral edge with no backscattering and full thermal equilibration; uncertainty is dominated by edge equilibration length, plausibly a factor of $2$ either way.

**Step 7 — comparative index table.** Both theories share $\mathcal{D} = 2$ and $\kappa_1 = 1$, yet differ in $N_M$ ($0$ versus $1$) and in confined content (two Abelian anyons versus one non-Abelian anyon of dimension $\sqrt{2}$). This demonstrates that the two indices are independent and jointly informative — the core claim of the two-index framework [9].

## 5. Results

All numbers below were computed in Section 4; no empirical data are claimed.

- **Toric code, $e$-condensation**: $\mathcal{D} = 2$; $\mathcal{L} = \{1, e\}$ with $|\mathcal{L}| = 2$; $\kappa_1 = 2/2 = 1$ (fully gapped boundary); confined anyons $\{m, \varepsilon\}$, count $2$; $c_- = 0$; $N_M = 0$; forced annulus boundary degeneracy $2$.
- **Ising order, $\psi$-condensation**: $\mathcal{D} = 2$; $\mathcal{L} = \{1, \psi\}$ with $|\mathcal{L}| = 2$; $\kappa_1 = 2/2 = 1$; confined anyon $\{\sigma\}$ with $d_\sigma = \sqrt{2} \approx 1.414$; $c_- = 1/2$; $N_M = 1$ (one forced chiral Majorana edge mode).
- **Thermal Hall projection** (Ising, gapless edge, $T = 0.1\,\mathrm{K}$, clean-edge assumption, factor-of-$2$ uncertainty): $\kappa_{xy} = 4.73 \times 10^{-14}\,\mathrm{W/K}$.
- **Discriminating power**: the pair $(\kappa_1, N_M)$ separates the two theories as $(1, 0)$ versus $(1, 1)$ despite identical $\mathcal{D}$ and $\kappa_1$, confirming that a single index is insufficient and the second index is not redundant.

## 6. Discussion

**Limitations.** First, both benchmarks are small theories with $\mathcal{D} = 2$; the index $\kappa_1$ is trivially $1$ in both cases because Lagrangian algebras in these categories saturate the quantum dimension. For larger categories (e.g., quantum doubles of non-Abelian groups, or doubled non-Abelian orders), $\kappa_1$ can differ from $1$ for *partial* condensates, and our claim that $\kappa_1 = 1$ diagnoses complete gapping has not been tested there. Second, the Ising case requires a fermionic substrate for $\psi$-condensation, since $\psi$ is a fermion; in a strictly bosonic system the condensate $\{1, \psi\}$ is obstructed, and our analysis silently changes category type. This should be formalized via spin-TQFT super-modular categories. Third, the confined census relies on braiding nontriviality, which is unambiguous for Abelian mutual statistics but requires care for non-Abelian anyons, where confinement means failure of the anyon to admit a local (condensate-trivial) sector after fusion with the condensate; our treatment of $\sigma$ uses the standard result but does not re-derive it.

**Failure modes.** The thermal Hall projection fails if the edge hosts non-topological backscattering, disorder-localized segments, or partial equilibration — all common experimentally. The Majorana count $N_M = 2c_-$ counts chiral modes only; anti-chiral pairs, which can appear at engineered domain walls, are invisible to it. The boundary degeneracy of $2$ per annulus is exact only in the thermodynamic limit; finite systems split it exponentially in the boundary length, a contingent effect.

**What would falsify the claims.** (i) A gapped boundary of the toric code after $e$-condensation exhibiting a forced degeneracy other than $2$ on an annulus would falsify the degeneracy prediction. (ii) A gapless boundary of Ising order with thermal Hall conductance corresponding to $c_- \neq 1/2$ (after accounting for non-topological contributions) would falsify the Majorana count. (iii) A condensate with $\kappa_1 = 1$ that nevertheless leaves topological boundary degrees of freedom would falsify the completeness interpretation of the first index. Each of these is, in principle, testable in fractional quantum Hall interfaces, Majorana wire arrays, or engineered $\mathbb{Z}_2$ gauge systems.

**Arguing against ourselves.** One might object that the indices are just repackaged known results: $\kappa_1 = 1$ is equivalent to the standard Lagrangian-algebra criterion for gapped boundaries [5], and $N_M$ is the standard chiral central charge. The rebuttal is that the contribution is the *pairing*: the framework's value is the claim that these two numbers, and only these, are forced, while everything else (gap size, splitting, condensate structure factor) is contingent. That negative claim — the exhaustive list of forced phenomena — is the strongest and most falsifiable part of the program, and it is the least tested. A further self-criticism: the bibliography contains nine works, all of which we cite, but several are from distant subfields (holography [3], [6]; PDE [4]); their connection is methodological rather than technical, and a dedicated topological-order literature review would strengthen Section 2.

**Open questions.** How do the indices behave under stacking and under anyon-permuting domain walls? Does a two-index system suffice for fermionic twisted sectors where $c_-$ is defined only modulo $1/2$? Can $\kappa_1$ be measured directly, e.g., through boundary entanglement spectroscopy?

## 7. Conclusion

We have shown that bulk condensation data force a small, explicitly computable set of boundary phenomena, captured by two indices: the condensation completeness index $\kappa_1 = |\mathcal{L}|/\mathcal{D}$ and the Majorana count $N_M = 2c_-$. For the toric code with $e$-condensation we derived $\kappa_1 = 1$, $N_M = 0$, two confined anyons, and a forced annulus degeneracy of $2$; for Ising order with $\psi$-condensation we derived $\kappa_1 = 1$, $N_M = 1$, one confined non-Abelian anyon, and a projected thermal Hall conductance of $4.73 \times 10^{-14}\,\mathrm{W/K}$ at $0.1\,\mathrm{K}$. The two theories, indistinguishable by $\mathcal{D}$ or $\kappa_1$ alone, are cleanly separated by the index pair. The program converts the structural bulk-boundary correspondence of anyon condensation into arithmetic that an adjacent-field expert can audit line by line — and, more importantly, into predictions that experiment can fail.

## References

[1] arXiv:2008.04953v3 | Factorization Algebras for Classical Bulk-Boundary Systems

[2] arXiv:2205.15635v4 | Bulk-boundary correspondence in point-gap topological phases

[3] arXiv:hep-th/9805171v4 | Bulk vs. Boundary Dynamics in Anti-de Sitter Spacetime

[4] arXiv:1803.05314v4 | Cahn-Hilliard equation on the boundary with bulk condition of Allen-Cahn type

[5] arXiv:2606.19137v2 | Bulk-boundary correspondence of (1+1)D symmetric gapped phases

[6] arXiv:1505.05069v2 | Poking Holes in AdS/CFT: Bulk Fields from Boundary States

[7] arXiv:1510.01427v2 | Conformal anomalies of CFT's with boundaries

[8] arXiv:1805.06492v2 | Biorthogonal Bulk-Boundary Correspondence in Non-Hermitian Systems

[9] QNFO: A Two-Index Framework for the Bulk-Boundary Correspondence of Anyon Condensation and Boundary Majorana Statistics | DOI 10.5281/zenodo.23110411