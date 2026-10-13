# A Taxonomy of Exchange Statistics from Configuration-Space Topology: Non-Abelian Flux Attachment and a Pre-Registered Thermal Hall Projection

## Abstract

The statistics of identical particles is fixed by the fundamental group of their configuration space: in $d \geq 3$ spatial dimensions this group is the symmetric group $S_N$, permitting only the bosonic ($+1$) and fermionic ($-1$) exchange phases, while in $d = 2$ it is the braid group $B_N$, whose one-dimensional representations give anyons and whose higher-dimensional representations give non-Abelian anyons. What is missing is a systematic classification of the exchange behaviors obtained by attaching fluxes drawn from a possibly non-Abelian group $G$ to particle worldlines, organized so that each class carries a falsifiable observable. This paper develops such a taxonomy as a four-axis classification: (A) the exchange group $G_N = \pi_1(C_N(M))$; (B) the dimension $r$ of the unitary representation $\rho: G_N \to U(r)$; (C) whether $\rho$ factors through a finite quotient; and (D) the chiral central charge $c_-$ of the associated topological order. We derive the abelianization $B_N^{\mathrm{ab}} \cong \mathbb{Z}$, compute the thermal Hall conductance quantum $\pi^2 k_B^2/(3h) = 9.464311516 \times 10^{-13}\ \mathrm{W\,K^{-2}}$ from the exact 2019-SI values of $k_B$ and $h$, and project $\kappa_{xy}/T = 1.419646727 \times 10^{-12}\ \mathrm{W\,K^{-2}}$ for a candidate non-Abelian class with $c_- = 3/2$, i.e. $\kappa_{xy} = 1.419646727 \times 10^{-14}\ \mathrm{W\,K^{-1}}$ at $T = 10\ \mathrm{mK}$ — a factor-of-3 discriminator against the Ising-type $c_- = 1/2$ alternative. Assumptions, failure modes, and falsification criteria are stated explicitly.

## 1. Introduction

Experimental groups measuring thermal transport in fractional quantum Hall and moiré devices currently face a diagnosis problem: several candidate topological orders produce indistinguishable charge-transport signatures, and the cleanest discriminator between them — the quantized thermal Hall conductance $\kappa_{xy}$ — has no published table of target values tied to a systematic classification of the possible exchange statistics. A measurement campaign that cannot name its target slope cannot distinguish confirmation of a candidate order from refutation of it; the cost is misassigned topological orders and, downstream, blocked progress toward topological quantum computation, where non-Abelian anyons are the resource. A derived taxonomy that assigns to each exchange-statistics class a definite thermal Hall slope would change the design of these experiments: the experimenter would measure a slope, read off a taxonomy class, and know immediately which alternative orders are excluded.

The theoretical starting point is that the statistical behavior of identical particles is not an independent postulate of quantum mechanics but a consequence of the topology of the configuration space. When $N$ identical particles move on a manifold $M$, the physically distinguishable configurations form the orbit space

$$C_N(M) = \frac{M^N \setminus \Delta}{S_N},$$

where $\Delta$ is the coincidence set, and quantization on this space requires a unitary representation of its fundamental group $\pi_1(C_N(M))$. In three or more dimensions $\pi_1(C_N(M)) \cong S_N$, whose abelianization is $\mathbb{Z}_2$, yielding exactly two exchange phases. In two dimensions $\pi_1(C_N(\mathbb{R}^2)) \cong B_N$, the braid group, whose abelianization is $\mathbb{Z}$, permitting any continuous exchange phase $e^{i\theta}$ and, through higher-dimensional representations, non-Abelian anyons whose braiding acts by matrices on a degenerate ground-state manifold. This dimension-dependent dichotomy is a theorem about the topology of the space in which particles move, as the configuration-space-topology (CST) framework states [10]; the same framework acknowledges that it rests on scaffolds — point-like particles, a fixed classical background manifold, a deleted hard-core diagonal, an externally imposed dimension — that it cannot itself derive [10].

This paper treats flux attachment as a homomorphism from the braid group into a target group $G$ — possibly non-Abelian — and derives a taxonomy of the resulting exchange statistics from computable topological data. The program extends the CST derivation program of Ref. [9], which formulates exchange statistics as an "exchange scalar" derived from configuration-space topology, with the familiar $\pm 1$ boson/fermion dichotomy appearing as an abelianized "shadow" of the full representation data.

The practical motivation is predictive. Non-Abelian anyon phases support topologically protected degeneracies and, when the phase is chiral, a quantized thermal Hall conductance $\kappa_{xy}$ proportional to the chiral central charge $c_-$. Because $\kappa_{xy}$ is insensitive to disorder and couples only to the topological sector, it is the cleanest experimental handle on non-Abelian order. We derive explicit numerical targets for $\kappa_{xy}/T$ for candidate classes in the taxonomy and frame a falsifiable, pre-registered projection on an 18-month horizon.

The contributions of this paper are:

1. A four-axis taxonomy $(G_N, r, \mathrm{factor}, c_-)$ of exchange statistics under homomorphism-defined flux attachment, with the Abelian/non-Abelian and finite-factor/genuinely-braided distinctions made explicit (Section 3.3).
2. A derivation of the abelianizations $B_N^{\mathrm{ab}} \cong \mathbb{Z}$ and $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$ from the braid and permutation presentations, establishing the anyonic continuum in $d = 2$ and its collapse to $\{0, \pi\}$ in $d \geq 3$ (Section 4.2).
3. A first-principles computation of the thermal Hall conductance quantum $\pi^2 k_B^2/(3h) = 9.464311516 \times 10^{-13}\ \mathrm{W\,K^{-2}}$ from exact 2019-SI inputs, with every arithmetic step shown (Section 4.3).
4. Numerical family predictions $\kappa_{xy}/T$ for $c_- \in \{1/2, 1, 3/2, 5/2\}$ and the factor-of-3 discriminator between the $c_- = 3/2$ and $c_- = 1/2$ classes at $T = 10\ \mathrm{mK}$ (Section 4.4).
5. A pre-registered, falsifiable projection with an explicit null hypothesis and confirmation/refutation criteria built on the permutation-test methodology of Ref. [5] (Section 5).

## 2. Background and Related Work

**Configuration spaces of Artin and Coxeter groups [1].** This work reviews topological and algebraic aspects of Artin and Coxeter groups, computes the Schwartz genus of the covering associated to the orbit space for all affine Artin groups, and gives a partial computation of the cohomology of the braid group [1]. The braid group $B_N$ is the Artin group of type $A_{N-1}$, so cohomological computations of the kind [1] performs constrain the characteristic classes available to flat $G$-bundles over braid configuration spaces — the objects that encode flux attachment in our taxonomy. The Schwartz-genus computation for orbit coverings also supplies the covering-theoretic language in which we state how many sheets of the unordered configuration space a flux-carrying excitation can be tracked across.

**Persistence modules and interleaving distances [2].** This work studies classes of persistence modules arising in topological data analysis and establishes that the interleaving distance between them equals the bottleneck distance between the corresponding persistence diagrams for many module classes [2]. It further shows that the extended metric space of persistence diagrams with the bottleneck distance is "big", so that restricting to a compact set of diagrams is "a drastic step" [2]. We invoke this machinery methodologically: the taxonomy assigns to each flux-attachment class a persistence-like grading (the winding number), and the interleaving formalism provides a metric on the space of such gradings, stating when two attachment rules are topologically indistinguishable at finite braid length. The "bigness" result of [2] is the reason we do not attempt to compactify the space of attachment rules: the correct robustness criterion is stability of $G_N$ under sample perturbations, not compactness of the classifying space.

**Hawaiian groups and wild topology [3].** This work determines the structure of the $n$-dimensional Hawaiian group of the $m$-dimensional Hawaiian earring space for all $1 \leq m \leq n$, and studies Hawaiian groups under product spaces, weak join spaces, cone spaces, covering spaces, and locally trivial bundles [3]; its Theorem 3.1 gives, for a first countable, locally strongly contractible pointed space, an isomorphism of the infinite-dimensional Hawaiian group onto a weak product of ordinary homotopy groups [3]. Although our physical configuration spaces are locally tame, the Hawaiian-group formalism is the diagnostic for a failure mode we must exclude: on configuration spaces with accumulating punctures (e.g., finite-density anyon gases in the thermodynamic limit), the fundamental group develops wild, non-discrete behavior, and flux attachment by ordinary homomorphisms breaks down. Section 6 treats this as a boundary of validity of the taxonomy.

**Classifying spaces for families of subgroups [4].** This work generalizes the existence theorems of Milnor (1956), Gelfand–Fuks (1968), and Segal (1975) for classifying spaces of principal $G$-bundles to $G$-spaces with torsion: its Theorem 2.5 states that any $G$-space isovariantly covered by $\kappa$-many $\mathcal{F}$-tubes is $G$-homeomorphic to the pullback $f^{*}(\mathscr{E}_{\mathcal{F}}^{\kappa}G)$ for a map $f: X/G \to \mathscr{B}_{\mathcal{F}}^{\kappa}G$, with the conclusion holding for $E_{\mathcal{F}}^{\kappa}G$ when the cover is only approximate and each isotropy group is closed [4]; its Corollary 2.7 recovers Segal's result for principal bundles covered by $\kappa$-many local trivializations [4]. A flux-attachment rule is precisely a principal-$G$ bundle structure over the braid configuration space; the classifying-space machinery of [4] guarantees that, for any topological flux group $G$ and any admissible family of stabilizer subgroups, a universal flux-bundle space exists, so the taxonomy is not vacuous — every class it labels is realizable by some bundle.

**Permutation statistics for block designs [5].** This work introduces a nonparametric test statistic $\Lambda$ for the permutation test in complete block designs, finds the region in which the statistic exists, considers its properties on the boundary of that region, and proves that saddlepoint approximations for tail probabilities can be obtained in the interior [5]. Its power study compares the $\Lambda$-statistic against the $F$-statistic for a design with 10 blocks of size 4, finding under the exponential error distribution a slight power increase for small $\sum \mu^2$ and under the exponentially squared distribution a substantial increase for moderate $\sum \mu^2$ [5]. We use [5] twice: for its method of boundary analysis — our taxonomy has an analogous boundary, the Abelian/non-Abelian transition at representation dimension $r = 2$ — and for the inferential framework of the pre-registered projection in Section 5, where a permutation-based test statistic with an explicitly stated null region defines confirmation versus refutation of the measured $\kappa_{xy}/T$.

**Tight contact structures on $\Sigma_2 \times I$ [6].** This work classifies tight contact structures on the closed oriented genus-2 surface times the interval, with a boundary condition forcing the contact Euler class to vanish on each boundary component, and proves that there exists a unique, non-product tight contact structure in this case [6]. Its method is cut-and-paste: the manifold is decomposed along incompressible surfaces into pieces, and the possible bypasses along each cutting surface are strictly limited, which is what forces uniqueness [6]. Genus-2 surfaces are the natural stage for doubled non-Abelian anyon theories, and the uniqueness result of [6] suggests that the gluing data of the topological sector relevant to our $c_- = 3/2$ candidate class is rigid: there is essentially one way to glue the flux sectors, strengthening the robustness of the thermal Hall prediction. The contact-topological distinction between tight and overtwisted structures [6] also serves as the low-dimensional analogue of chirality: orientation reversal of $M$ flips the sign of the thermal Hall response.

**Minimal topological groups and the Roelcke uniformity [7].** This work studies minimal topological groups — those admitting no strictly coarser Hausdorff group topology — and Roelcke-precompact groups, motivated by the questions of which subgroups are minimal and which are lower precompact [7]. Its §8 proves that the isometry group $G = \mathrm{Iso}(M)$ of a complete $\omega$-homogeneous Urysohn metric space is Roelcke-precompact, with the Roelcke compactification identified with the space of bi-Katětov functions, and that $G$ is minimal and topologically simple [7]. Compact flux groups such as $SU(2)$ and its finite subgroups fall under the precompact side of this theory, and minimality ensures that the flux-attachment homomorphism $\varphi: B_N \to G$ cannot be degraded by coarsening the topology of $G$: the discrete quantum-statistics content of the attachment is topologically locked. This underwrites the claim that the taxonomy is stable under physical regularization, and informs the discussion of the $N \to \infty$ limit, where the discrete taxonomy must be replaced by a coarse structure.

**String topology and homotopy invariance [8].** This work proves that the Chas–Sullivan string topology loop product $\mu: H_*(LM) \otimes H_*(LM) \to H_*(LM)$ of degree $-n$ and the string bracket of degree $2-n$ on the free loop space $LM$ of a closed oriented $n$-manifold are homotopy invariants [8]. Its proof strategy is itself configuration-theoretic: it decomposes $M \times M = D(\tau_M) \cup_{S(\tau_M)} F(M,2)$ into a disk bundle of the diagonal and the ordered two-point configuration space, and reduces homotopy invariance of the loop product to homotopy invariance of the configuration-space data under a homotopy equivalence $f: M_1 \to M_2$ [8]. Worldline braiding of anyons is naturally a loop-space phenomenon: the loop product is the homological shadow of concatenating excitation worldlines, and the homotopy invariance proved in [8] guarantees that the statistics classification — which depends only on the homotopy class of braids — is invariant under continuous deformations of the anyon trajectories, as physics requires.

**The CST derivation program [9], [10].** Ref. [9] formulates exchange statistics as an "exchange scalar" derived from configuration-space topology, with the $\pm 1$ boson/fermion shadow in $d \geq 3$ as a special case, and pre-registers a derivation program for extending the calculus to non-Abelian settings; its own Results section already lists the thermal Hall conductance quantum and the family predictions that this paper re-derives with full arithmetic. Ref. [10] states the dimension theorem $\pi_1(C_N(\mathbb{R}^d)) = B_N$ for $d = 2$ and $S_N$ for $d \geq 3$ with Artin's presentation and the quotient $S_N \cong B_N / \langle \sigma_i^2 = 1 \rangle$, cites the established derivations of the boson/fermion dichotomy and of anyons, and explicitly acknowledges that the framework's scaffolds — point particles, fixed background, deleted diagonal, imposed dimension, adiabatic exchange — are under external test and that its spin-statistics boundary requires relativistic input the framework cannot supply [10]. This paper executes one branch of the pre-registered program: the non-Abelian extension of the exchange calculus, with the thermal Hall response as the falsifiable output.

## 3. Methods

### 3.1 Configuration spaces and their fundamental groups

Let $M$ be a connected surface and define the ordered and unordered configuration spaces

$$F_N(M) = \{(x_1, \dots, x_N) \in M^N : x_i \neq x_j \text{ for } i \neq j\}, \qquad C_N(M) = F_N(M)/S_N.$$

The covering $F_N(M) \to C_N(M)$ has deck group $S_N$. For $M = \mathbb{R}^d$:

$$\pi_1(C_N(\mathbb{R}^d)) \cong \begin{cases} S_N & d \geq 3, \\ B_N & d = 2, \end{cases}$$

where $B_N$ is generated by elementary braids $\sigma_1, \dots, \sigma_{N-1}$ subject to

$$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}, \qquad \sigma_i \sigma_j = \sigma_j \sigma_i \ \ (|i - j| \geq 2),$$

and $S_N \cong B_N / \langle \sigma_i^2 = 1 \rangle$ [10]. For $M$ a general surface, $G_N$ is a surface braid group, modified by $\pi_1(M)$ and by boundaries.

### 3.2 Flux attachment as a homomorphism

A flux-attachment rule is a homomorphism

$$\varphi: B_N \to G,$$

where $G$ is the flux group (e.g., $U(1)$ for Abelian anyons, $SU(2)$ or a finite quotient for non-Abelian anyons). Because $B_N$ is generated by the $\sigma_i$, $\varphi$ is determined by the tuple $(g_1, \dots, g_{N-1})$, $g_i = \varphi(\sigma_i) \in G$, subject to the braid relations. The exchange statistics of two particles in flux sector $a$ is the conjugacy class $[a]$ of $a = \varphi(\sigma_i)$ in $G$; the statistics is Abelian iff $[a]$ is central, i.e., $\varphi(\sigma_i) \in Z(G)$.

### 3.3 The four-axis taxonomy

We assign to any physical exchange behavior a quadruple $(G_N, r, \mathrm{factor}, c_-)$:

- **Axis (A): Exchange group.** $G_N = \pi_1(C_N(M))$: $S_N$ for $\dim M \geq 3$, $B_N$ for $M = \mathbb{R}^2$.
- **Axis (B): Representation dimension.** A statistics assignment is $\rho: G_N \to U(r)$. For $r = 1$, $\rho$ factors through the abelianization $G_N^{\mathrm{ab}}$; the particle is an Abelian anyon with exchange phase $\theta = \arg \rho(\sigma_i) \in \mathbb{R}/2\pi\mathbb{Z}$. For $r > 1$ with non-commuting image, exchanges act by matrices on a degenerate internal space: a non-Abelian anyon.
- **Axis (C): Finite factoring.** If $\rho$ factors through a finite quotient $q: G_N \to F$ (e.g., $B_N \to S_N$ via $\sigma_i \mapsto (i\ i{+}1)$), the statistics is parastatistics-like: exchanges permute finite internal types with no braiding phase. If $\rho$ does not factor finitely and $r > 1$, the statistics is genuinely braided non-Abelian. Axis (C) exists precisely to separate these two $r > 1$ cases.
- **Axis (D): Chiral central charge.** If $(G_N, \rho)$ is realized by a gapped topological phase with topological order $\mathcal{C}$, the chiral central charge $c_-$ of $\mathcal{C}$ fixes the thermal Hall response

$$\kappa_{xy} = c_- \, \frac{\pi^2 k_B^2}{3h}\, T.$$

Axis (D) is not determined by (A)–(C) alone: distinct modular tensor categories can share the same braid group representation but differ in $c_-$. The taxonomy is therefore a surjection, not a bijection, from phases to quadruples; it classifies exchange behavior, not topological order.

### 3.4 Thermal Hall conductance as the observable

For a chiral topological phase with chiral central charge $c_-$,

$$\frac{\kappa_{xy}}{T} = c_- \, \frac{\pi^2 k_B^2}{3h},$$

with $k_B = 1.380649 \times 10^{-23}\ \mathrm{J\,K^{-1}}$ and $h = 6.62607015 \times 10^{-34}\ \mathrm{J\,s}$, both exact 2019-SI defined values. Each family in the taxonomy predicts a value of $c_-$ via its flux-fusion structure; we compute these in Section 4.

## 4. Analysis

### 4.1 Axis (A): explicit computations

**$N = 2$, $M = \mathbb{R}^2$.** $C_2(\mathbb{R}^2) \simeq \mathbb{R}^2 \times (\mathbb{R}^2 \setminus \{0\})$, so

$$G_2 = \pi_1(C_2(\mathbb{R}^2)) \cong \pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z},$$

generated by the single braid $\sigma_1$ with no relations. The square $\sigma_1^2$ is the double braid (monodromy of one particle around the other). This is the entire group-theoretic content of anyonic statistics in two dimensions.

**$N = 2$, $\dim M \geq 3$.** $\pi_1(\mathbb{R}^d \setminus \{0\}) \cong \pi_1(S^{d-1})$, trivial for $d \geq 3$; the exchange group is $S_2 \cong \mathbb{Z}/2\mathbb{Z}$. The relation $\sigma_1^2 = 1$ collapses the anyonic continuum $\theta \in [0, 2\pi)$ to the two points $\theta = 0, \pi$ — the topological origin of the boson/fermion dichotomy in three and higher dimensions.

**$N = 3$, $M = \mathbb{R}^2$.** $G_3 = B_3 = \langle \sigma_1, \sigma_2 \mid \sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2 \rangle$. The abelianization is $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ (both generators map to $1$; the braid relation is homogeneous and vanishes in the abelianization). The center is $Z(B_3) = \langle (\sigma_1 \sigma_2)^3 \rangle \cong \mathbb{Z}$. The finite quotient $B_3 \to S_3$ exists because transpositions satisfy the braid relation: $(12)(23)(12) = (13) = (23)(12)(23)$.

### 4.2 Axis (B): abelianization and the exchange phase

**Step 1.** Abelianization imposes commutativity: the braid relation becomes $\sigma_i \sigma_{i+1} = \sigma_{i+1} \sigma_i$, which is the commutativity relation itself and so carries no information in an Abelian group; far-commutativity is already trivial. Hence no independent relation survives, and

$$B_N^{\mathrm{ab}} \cong \mathbb{Z}, \qquad \mathrm{ab}(\sigma_i) = 1 \ \text{for all } i.$$

**Step 2.** A one-dimensional unitary representation is $\rho: B_N \to U(1)$ with $\rho(\sigma_i) = e^{i\theta}$ for all $i$ (the braid relations force equal phases). The exchange of two identical anyons multiplies the wavefunction by $e^{i\theta}$; the monodromy $\sigma_1^2$ gives $e^{2i\theta}$. For $\theta = \pi \chi_1$ with $\chi_1 \in \mathbb{Z}$ we recover bosons ($\chi_1$ even) and fermions ($\chi_1$ odd); for general real $\theta$ we obtain Abelian anyons. In $d \geq 3$, $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$ forces $\chi_1 \in \{0, 1\}$ — the CST exchange-scalar dichotomy of [9], i.e., the $\pm 1$ shadow.

**Non-Abelian anyons.** For $r > 1$, the image $\rho(B_N) \subset U(r)$ need not commute. The minimal illustrative case is a representation of $B_3$ in which $\sigma_1, \sigma_2$ act on a two-dimensional fusion space by matrices whose products depend on order: $\rho(\sigma_1)\rho(\sigma_2) \neq \rho(\sigma_2)\rho(\sigma_1)$. The physical consequence is order-dependent fusion: bringing a third particle to a pair can yield different outcome channels depending on the braid history — the operational definition of non-Abelian statistics.

**Axis (C) in action.** The representation $\rho: B_3 \to S_3 \to U(3)$ (permutation matrices) has $r = 3 > 1$ but factors finitely; exchanges permute internal types without phase. This is parastatistics, topologically distinct from genuine non-Abelian braiding even though both have $r > 1$.

### 4.3 Axis (D): the thermal Hall conductance quantum

**Input numbers.** $k_B = 1.380649 \times 10^{-23}\ \mathrm{J\,K^{-1}}$ and $h = 6.62607015 \times 10^{-34}\ \mathrm{J\,s}$, exact 2019-SI values; $\pi = 3.141592654$, so $\pi^2 = 9.869604401$.

**Step 1.** Square $k_B$: $1.380649^2 = 1.380649 \times 1.380649$. Computing: $1.380649 \times 0.3 = 0.4141947$; $1.380649 \times 0.08 = 0