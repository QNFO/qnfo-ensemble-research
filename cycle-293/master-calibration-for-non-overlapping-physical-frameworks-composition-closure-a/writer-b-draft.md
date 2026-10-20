# Master Calibration for Non-Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation (Version 3.0)

## Abstract

Physics presents itself as convergent, yet a systematic inventory lists 29 unresolved bifurcations—general relativity versus quantum mechanics, continuum versus discrete description, the Heisenberg cut, and the status of the observer. We conjecture that such schisms are symptoms of frameworks that are each internally self-consistent over disjoint domains, lacking a *master calibration*: a family of partial translation maps that calibrates pairs of domains and composes consistently. We formalize frameworks as calibrated theories over domains, define translation maps with quantified error, and bound composition failure by a cycle-closure error. Counting pairwise maps and composition constraints for the 29-schism inventory yields $\binom{29}{2}=406$ maps against $\binom{29}{3}=3654$ square constraints, a constraint-to-map ratio of exactly $9.0$; a corrected counting argument shows that a hypothesized seven-domain family can host at most 21 distinct pairwise schisms, so a one-schism-per-pair assignment would leave at least 8 of the 29 unassigned. A three-edge closure budget gives $\Delta_{\gamma}\le 3.4965\times10^{-3}$, and an independence-model projection gives a success probability $\approx 10^{-167.3}$ for random composition of all 3654 squares at per-constraint compatibility $p=0.9$, with the largest family exceeding a $1\%$ success probability at $n_{\max}=7$. The results indicate that beyond small families, global consistency must be enforced by construction rather than hoped for, and they supply a closure criterion against which any proposed master calibration can be tested.

## 1. Introduction

Experimental and theoretical physicists repeatedly encounter pairs of successful theories that resist unification: general relativity and quantum mechanics, continuum field descriptions versus discrete spectra, the Heisenberg cut separating quantum from classical apparatus, and competing compositional versus holistic readings of state structure. The cost of this impasse is concrete. Multi-year international facility programs—the European strategy process for future colliders [1] and the linear-collider design study of [2]—are built on the expectation that a shared observable can bridge theoretical domains, yet no single framework currently yields a universally applicable predictive tool, and the inventory of [10] records 29 bifurcations that persist beneath the edifice of apparent unity. If a family of partial translation maps could be constructed that composes consistently across all frameworks, design decisions for future colliders, fusion reactors, and quantum technologies could be guided by a unified calibration budget rather than by ad-hoc compromises; if it could be shown that no such family composes without engineered enforcement, resources could be redirected toward explicit mediating structures instead of waiting for spontaneous unification. The present work therefore asks: **under what conditions does a master calibration exist, and how large is the combinatorial burden of enforcing global consistency?**

This paper is a revision of the prior version of the same analysis [9]. Two reported defects in the earlier derivations are corrected here. First, the earlier claim that "$29-21=8$ schisms lie outside any pairwise reduction involving only the seven claimed vocabularies" conflated schisms with pairwise relations: a single unordered pair can host more than one schism, so the subtraction is valid only under an explicit one-schism-per-pair assumption, which is now stated and its role analyzed (Section 4, Derivation 2). Second, the earlier falsifiability criterion asserted that an explicit family of $n\ge10$ frameworks with commuting squares "would contradict the combinatorial bound that random families succeed only up to $n_{\max}=7$"; an explicit construction does not contradict a statement about random families, and the criterion is restated so that it targets the paper's actual negative conjecture (Section 6).

Our contributions are:
- **C1** – Formal definitions of framework, translation map, composition failure, and master calibration (Section 3).
- **C2** – Derivation of the pairwise-map count $\binom{29}{2}=406$ and composition-constraint count $\binom{29}{3}=3654$ for the 29-schism inventory of [10], with the exact constraint-to-map ratio $9.0$ and the factor-2 reading $N=58$ giving $1653$ maps and $30856$ constraints (Section 4, Derivation 1 and Derivation 8).
- **C3** – A corrected counting argument for the hypothesized seven-domain family: at most $\binom{7}{2}=21$ distinct unordered pairs exist, so under a one-schism-per-pair assignment at least $29-21=8$ of the 29 bifurcations of [10] cannot be given a distinct pair within the family; without that assumption no such conclusion follows (Section 4, Derivation 2).
- **C4** – Computation of the three-framework closure bound $\Delta_{\gamma}\le 3.4965\times10^{-3}$ for illustrative edge errors $10^{-3}$, $2\times10^{-3}$, $5\times10^{-4}$, and of the mediated-translation price $1-(1-\varepsilon)^2=0.0199$ versus the direct error $0.01$ at $\varepsilon=10^{-2}$ (Section 4, Derivations 3 and 7).
- **C5** – Classification criterion separating structural from conventional schisms based on per-edge error floors and a tolerance $\tau$ (Section 3.5 and Section 4, Derivation 4).
- **C6** – Projection that a random translation family with per-constraint compatibility probability $p=0.9$ succeeds with probability $\approx10^{-167.3}$, and that the largest family size with success probability $\ge1\%$ is $n_{\max}=7$ (Section 4, Derivation 5).
- **C7** – Worked two-framework corner showing that a pair of frameworks carries no composition constraint, under the assumption of a two-ontology split (Section 4, Derivation 2$'$).
- **C8** – Energy-scale window factor $2$ for the linear-collider design of [2] under its abstract range, with the preface range giving a factor $3$, and mean schisms per domain $\approx 4.14$ under a uniformity assumption (Section 4, Derivation 6).

## 2. Background and Related Work

**Calibration with non-overlapping coverage.** Targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap exploits road markings as static, robust features mediating between the two sensors; the method estimates the rigid-body transformation with a reported accuracy of approximately $0.02\ \mathrm{m}$ and $0.086^{\circ}$ without manual operation by a human operator, while noting that its assumption of locally accurate odometry can fail under repeated vehicle accelerations [3]. This demonstrates that two internally consistent instruments with disjoint coverage can be jointly used through an indirect, mediating structure—the exact engineering analogue of the mediating domains introduced in Section 3.4. In microwave metrology, the thru-free multiline calibration for vector network analyzers eliminates the need for a thru standard by using an arbitrary transmissive two-port device together with an additional reflect standard; verification measurements over $1$–$150\ \mathrm{GHz}$ with $299$ frequency points per sweep showed excellent agreement with multiline TRL when a thru was available, and the method sets the calibration-plane location automatically from the measured artifacts [8]. Work [8] thus shows that a calibration family can be constructed from weaker standards while preserving internal consistency, supporting the paper's claim that mediated translation chains are buildable but carry a quantifiable error price.

**Calibration as a limiting systematic.** In 21 cm cosmology, calibration precision is identified as a limiting systematic: astrophysical foreground emission is $4$–$5$ orders of magnitude brighter than the cosmological signal, so separating the two requires extremely precise instrumental calibration, and the field's two paradigms—sky-based calibration, relying on very good a priori models of sky and instrument, and redundant calibration, relying on perfectly redundant baselines and antenna responses—rest on distinct and partly incompatible assumptions [6]. The same work reports that a unified approach combining redundant calibration with a sky-model prior can improve calibration performance in simulation [6]. This is a direct instance of two calibration paradigms coexisting for one instrument class, each self-consistent on its own assumptions, mirroring a physics schism that would require a unifying framework; it also motivates the non-zero error floors used in Derivation 4.

**Calibration under domain shift.** Machine-learning work links out-of-domain generalization to multi-environment calibration: a classifier $f$ is calibrated when $\mathbb{E}_P[Y\mid f(X)=\alpha]=\alpha$ for all $\alpha$ in the range of $f$, and multi-domain calibration is argued to be viewable as an invariant representation, with a proof in a linear-Gaussian setting that models calibrated on multiple domains are free of spurious correlations and therefore generalize out of domain [5]. Complementing this, post-hoc uncertainty calibration under domain drift shows that standard methods, excellent in-domain, produce highly overconfident predictions as the test distribution shifts; across $28$ distinct perturbation types ($9$ affine transformations and $19$ image perturbations), calibration quality decreases with increasing shift for all baseline methods, and replacing the validation set by a transformed validation set substantially improves calibration under drift [7]. Both studies support the view that a model calibrated on its home domain may be uncalibrated after translation, reinforcing the need for explicit translation maps between frameworks and for error budgets that account for drift.

**Community-scale priority setting and shared observables.** The European Particle Physics Strategy Update aggregates community proposals for near-, mid-, and longer-term projects through a bottom-up process in which the community is first invited to submit inputs, and its briefing book records that the list of Standard-Model puzzles—electroweak symmetry breaking, the Higgs boson's nature, quark and lepton masses, the neutrino nature and mass, and on the cosmology side dark matter, dark energy, inflation, and the matter-antimatter asymmetry—did not change in the post-Run 2 LHC era [1]. The same source states that at future $e^{+}e^{-}$ colliders the oblique parameters will be measured with a precision of $\sim1\%$, about a factor 10 better than current precision [1], which supplies the quantitative precision target used in Derivation 6. The design study for an $e^{+}e^{-}$ linear collider specifies a center-of-mass energy of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ in its abstract and $0.5$–$1.5\ \mathrm{TeV}$ in its preface, and argues that the agent breaking electroweak symmetry "must provide new physical phenomena at the TeV energy scale" [2]; the facility is thereby a proposed shared observable intended to bridge theoretical domains, and the two stated ranges are carried through Derivation 6 as alternative conventions. In fusion, the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC) represent the low-density steady-state and high-density pulsed pathways to fusion, both under intensive design in China; their MHD assessment predicts the electron-cyclotron current drive power required for full stabilization of the neoclassical tearing mode on CFETR, finds that for $80\%$ of steady-state-operation scenarios active control may be required for resistive-wall-mode stabilization, and works with a Lundquist number $S=5.56\times10^{6}$ in the tearing-mode simulations [4]. Two internally coherent confinement pathways whose joint assessment remains an open task provide a concrete analogue of a physics schism at the scale of national programs.

**The schisms inventory and the prior version.** The QNFO synthesis reports 29 unresolved bifurcations spanning the nature of the continuum, the status of the observer, the consistency of mathematical language, and the meaning of explanation, and records the scale of the agreement side: quantum electrodynamics predicts the electron's magnetic moment to eleven decimal places while the cosmological constant is off by 120 orders of magnitude from naive expectations [10]. The same work states its Bootstrap Theorem: if the distinction function is ultrametric, the calibration operator $\Phi$ is a contraction mapping on the theory space and, by the Banach fixed-point theorem, possesses a unique fixed point $T^{*}=\Phi(T^{*})$ [10]. That theorem is a claim about convergence of a self-referential calibration loop on a single theory space; it does not supply translation maps between disjoint frameworks, which is precisely the gap the present paper formalizes. The prior version of this analysis [9] introduced the framework/translation formalism, the closure bound, and the counting results R1–R3 reproduced and corrected here; the present revision repairs its Derivation 2 and its falsifiability criterion, adds the mediated-translation price quantified against [3] and [8], and restricts every claim about cited works to what those works state.

## 3. Methods

### 3.1 Frameworks and domains

**Definition 3.1 (Framework).** A framework is a pair $F_i=(D_i,\mathcal{P}_i)$ where $D_i$ is a domain (set of states, configurations, or propositions) and $\mathcal{P}_i$ is a set of primitives (quantities, operations, or axioms) taken as given without further calibration. Internal consistency means no contradiction is derivable within $D_i$ using $\mathcal{P}_i$.

*Examples.* Non-relativistic quantum mechanics $F_{\mathrm{QM}}$ with primitives $|\psi\rangle$ and $U_t=e^{-iHt/\hbar}$; classical statistical mechanics $F_{\mathrm{SM}}$ with phase-space measure and coarse-graining cells; general relativity $F_{\mathrm{GR}}$ with metric $g_{\mu\nu}$.

### 3.2 Translation maps and error

**Definition 3.2 (Translation map).** A translation $\tau_{ij}:S_{ij}\to D_j$ is a partial map defined on an overlap $S_{ij}\subseteq D_i$, equipped with a *translation error* $\varepsilon_{ij}\in[0,1)$ measured as the fraction of propositions on a chosen test battery for which $\tau_{ij}$ disagrees with the best $F_j$-native rendering. Directionality is allowed: $\varepsilon_{ij}\neq\varepsilon_{ji}$.

*Canonical examples.* Decoherence supplies $\tau_{\mathrm{QM}\to\mathrm{cl}}$ on the sector where environment-induced superselection holds; coarse-graining supplies $\tau_{\mu\to M}$ above a resolution scale $\ell_{\mathrm{cg}}$.

### 3.3 Composition and closure

For composable translations $\tau_{ij}$ and $\tau_{jk}$, the composed error obeys the first-order bound

$$\varepsilon_{ij\circ jk}\le\varepsilon_{ij}+\varepsilon_{jk}+\varepsilon_{ij}\,\varepsilon_{jk}.$$

**Definition 3.3 (Composition failure).** Failure occurs if there exists $x\in\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$ such that $(\tau_{jk}\circ\tau_{ij})(x)\neq\tau_{ik}(x)$.

For a cycle $\gamma$ with edges $e\in\gamma$ and errors $\varepsilon_e$, the *closure error* satisfies

$$\Delta_{\gamma}\le1-\prod_{e\in\gamma}(1-\varepsilon_e).$$

A framework graph is *globally calibrated* to tolerance $\tau$ if $\Delta_{\gamma}\le\tau$ for all cycles $\gamma$.

**Definition 3.4 (Master calibration).** A family $\mathcal{T}=\{\tau_{ij}\}_{i<j}$ is a master calibration if every square commutes: $\tau_{jk}\circ\tau_{ij}=\tau_{ik}$ on $\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$.

### 3.4 Mediating domains

Following the engineering strategy exemplified by road-marking mediation between non-overlapping sensor fields of view [3] and by the construction of a calibration family from weaker standards in microwave metrology [8], we introduce a mediating domain $M$ with translations $\tau_{iM}:S_{iM}\to M$ and $\tau_{Mj}:M\supset\tau_{iM}(S_{iM})\to D_j$. The mediated translation $\tau_{Mj}\circ\tau_{iM}$ incurs two edge errors instead of one direct error, a price quantified in Derivation 7.

### 3.5 Structural versus conventional schisms

**Definition 3.5.** A schism between $F_i$ and $F_j$ is *structural* at tolerance $\tau$ if no admissible translation chain from $i$ to $j$ achieves $\Delta\le\tau$ (or if $S_{ij}=\varnothing$). It is *conventional* if such a chain exists but is costly (e.g., long, or requiring strong auxiliary assumptions such as the extremely accurate foreground model on which sky-based 21 cm calibration relies [6]). The master-calibration problem asks whether an assignment of edge errors can make all cycles close within $\tau$.

## 4. Analysis

All inputs below are stated with their sources or as explicit assumptions; all arithmetic is shown step by step. No empirical data are collected or used in this paper; where a number originates in a cited work it is attributed to that work.

**Input 1 (from [10]):** the number of unresolved bifurcations is $N_{\mathrm{schism}}=29$.

**Input 2 (assumption):** we hypothesize a candidate family of $n=7$ research domains as a modeling scenario for a small master-calibration problem; no cited work is relied upon for this number.

**Input 3 (assumption):** for the two-framework corner we assume a worked two-sided foundational split with $m=2$ ontologies, as a modeling scenario.

**Input 4 (from [2]):** the proposed linear-collider center-of-mass energy range is $E_{\mathrm{cm}}=500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ (abstract) and $0.5$–$1.5\ \mathrm{TeV}$ (preface).

**Input 5 (from [6]):** calibration precision is a limiting systematic in 21 cm cosmology, with foregrounds $4$–$5$ orders of magnitude brighter than the signal (qualitative; used to justify non-zero error floors).

**Input 6 (from [1]):** oblique parameters at future $e^{+}e^{-}$ colliders are expected to be measured with a precision of $\sim1\%$, about a factor 10 better than current precision.

**Input 7 (from [3]):** mediated (road-marking) calibration of non-overlapping sensors achieved approximately $0.02\ \mathrm{m}$ and $0.086^{\circ}$ accuracy.

### Derivation 1: counting maps and composition constraints.

Treating the 29 bifurcations as 29 frameworks, the number of unordered pairwise translation maps is

$$\binom{N}{2}=\frac{29\times28}{2}=406.$$

Each unordered triple $\{i,j,k\}$ yields one independent square constraint, giving

$$\binom{29}{3}=\frac{29\times28\times27}{6}=\frac{21924}{6}=3654.$$

The constraint-to-map ratio is

$$\frac{3654}{406}=9.0,$$

exactly because $\binom{N}{3}/\binom{N}{2}=(N-2)/3=27/3=9$.

### Derivation 2: pairwise capacity of the seven-domain family (corrected).

For $n=7$ domains, unordered pairs are

$$P=\binom{7}{2}=\frac{7\times6}{2}=21,$$

and directed pairs number $7\times6=42$.

The earlier version of this derivation [9] inferred directly that $29-21=8$ schisms "lie outside any pairwise reduction involving only the seven claimed vocabularies." That inference is invalid as stated, because a single unordered pair can host more than one schism: nothing in the definitions forces a one-to-one correspondence between the 29 bifurcations of [10] and the 21 unordered pairs of the family. The correct statement is a capacity statement:

- A seven-domain family contains exactly $21$ distinct unordered pairs, so at most $21$ bifurcations can be assigned a *distinct* pair within the family.
- **Additional assumption (one-schism-per-pair):** if each of the 29 bifurcations must occupy a distinct unordered pair of the family, then at least

$$29-21=8$$

bifurcations cannot be so assigned, and would require either a repeated pair (two or more schisms on the same edge) or additional domains beyond the seven.

Without the one-schism-per-pair assumption, the number $8$ does not follow, and the correct conclusion is only the capacity bound: the family's pairwise capacity is $21$ against an inventory of $29$, a shortfall of $8$ under the distinctness assumption. This correction weakens the earlier claim but keeps the structural point: a seven-domain family is pairwise-saturated by the inventory only if schisms may share edges.

### Derivation 2$'$: two-framework corner.

For $m=2$ ontologies (Input 3), the number of unordered pairs is

$$\binom{2}{2}=1,$$

and the number of unordered triples is

$$\binom{2}{3}=0.$$

Thus a pair of frameworks carries no composition constraint: any single translation map, however imperfect, trivially satisfies the master-calibration condition for that pair, because there is no third framework to create a cycle.

### Derivation 3: closure-error budget for a three-framework loop.

Choose edge errors

$$\varepsilon_{12}=10^{-3},\qquad\varepsilon_{23}=2\times10^{-3},\qquad\varepsilon_{31}=5\times10^{-4}.$$

The closure bound is

$$\Delta_{\gamma}\le1-(1-10^{-3})(1-2\times10^{-3})(1-5\times10^{-4}).$$

Compute each factor:

$(1-10^{-3})=0.999$,

$(1-2\times10^{-3})=0.998$,

$(1-5\times10^{-4})=0.9995$.

Product: $0.999\times0.998=0.997002$;

$0.997002\times0.9995=0.997002-0.997002\times0.0005=0.997002-0.000498501=0.996503499$.

Thus

$$\Delta_{\gamma}\le1-0.996503499=0.003496501\approx3.4965\times10^{-3}.$$

The additive first-order bound $\varepsilon_{12}+\varepsilon_{23}+\varepsilon_{31}=3.5\times10^{-3}$ agrees with the exact product bound to within $3.5\times10^{-6}$.

### Derivation 4: tolerance at which a schism becomes structural.

Assume a translation chain of $k=4$ edges, each with a floor $\varepsilon_{\min}=10^{-2}$ (assumption motivated qualitatively by the limiting-systematic status of calibration in 21 cm cosmology [6]). The closure bound is

$$\Delta\le1-(1-10^{-2})^{4}=1-0.99^{4}.$$

Compute: $0.99^{2}=0.9801$; $0.9801^{2}=0.96059601$. Hence

$$\Delta\le1-0.96059601=0.03940399\