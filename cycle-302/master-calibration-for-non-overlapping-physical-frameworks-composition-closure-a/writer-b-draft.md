# Master Calibration for Non-Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation

## Abstract

Physics carries a large inventory of persistent bifurcations—general relativity versus quantum mechanics, continuum versus discrete descriptions, the Heisenberg cut, and the status of the observer—each internally consistent over its own domain but lacking a shared observable that bridges it to its rival. This paper asks whether a *master calibration*, a family of partial translation maps that composes consistently across all frameworks, can exist, and what combinatorial burden such a calibration imposes. Frameworks, translation maps with quantified error, composition failure, and master calibration are formalized, and counting arguments are applied to a 29-schism inventory. The inventory yields $\binom{29}{2}=406$ unordered pairwise maps subject to $\binom{29}{3}=3654$ independent composition constraints, a constraint-to-map ratio of exactly $9.0$. A hypothetical seven-domain family admits only $21$ unordered pairs, so under a one-schism-per-pair assumption at least $29-21=8$ schisms lie outside any pairwise reduction. A three-framework loop with edge errors $10^{-3}$, $2\times10^{-3}$, $5\times10^{-4}$ has closure-error bound $3.4965\times10^{-3}$. A genericity projection with independent square-constraint success probability $p=0.9$ gives a master-calibration success probability of $10^{-167.3}$ and a maximal family size with $>1\%$ success of $n_{\max}=7$. Beyond small families, global consistency must therefore be enforced by construction rather than hoped for; the results separate structural from conventional schisms and set quantitative budgets for engineering mediating observables.

## 1. Introduction

Experimental and theoretical physicists repeatedly confront pairs of internally successful theories that cannot be unified, and the failure to unify has a measurable institutional cost. The European Particle Physics Strategy Update aggregates community proposals for near-term, mid-term and longer-term projects precisely because the field must choose where to spend multi-year, multi-billion-dollar facility budgets without an agreed bridge between competing theoretical descriptions [1]. The design study for a next linear collider specifies a centre-of-mass energy of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ and justifies the machine by the observation that electroweak symmetry is broken by an agent that is not yet known and must provide new phenomena at the TeV scale [2]; whether that agent is accessible depends on how translations between the Standard Model and its candidate extensions are calibrated. In fusion energy, magnetohydrodynamic stability analysis of the China Fusion Engineering Test Reactor and the Huazhong Field Reversed Configuration shows that the two devices represent divergent low-density steady-state and high-density pulsed pathways, and that the tokamak route requires a size and cost expected to demand collaborative efforts of multiple countries for many years [4]. In quantum technologies, the Heisenberg cut separates quantum control from classical engineering, and the measurement problem remains unresolved after a century [10].

These bifurcations translate into concrete blocked decisions. A collider programme that cannot state how its precision observables translate across framework boundaries cannot rank its options except by convention. A fusion programme choosing between confinement pathways lacks a shared diagnostic language between its MHD modelling regimes [4]. Quantum-computing hardware lacks a criterion for when a quantum-to-classical translation is admissible rather than merely conventional. If a family of partial translation maps could be constructed that composes consistently across all frameworks, these decisions could be guided by a unified calibration budget instead of ad-hoc compromise; if the combinatorial burden of such a family is prohibitive, the correct strategy changes to constructing explicit mediating observables for small clusters of frameworks.

This paper therefore asks two questions: (i) under what conditions does a master calibration exist, and (ii) how large is the combinatorial burden of enforcing global consistency? The analysis formalizes frameworks as calibrated theories over disjoint domains, defines translation maps with explicit error budgets, bounds composition failure by cycle-closure error, and applies counting arguments to the 29-schism inventory of [10] and to a modeled seven-domain family. The inventory of [10] enumerates 29 unresolved bifurcations spanning the nature of the continuum, the status of the observer, and the meaning of explanation, and argues that they are interconnected rather than isolated puzzles; this paper treats that inventory as the framework count and derives the consequences.

**Contributions.**
- **C1** – Formal definitions of framework, translation map, composition failure, and master calibration (Section 3).
- **C2** – Derivation of the pairwise-map count $\binom{29}{2}=406$ and composition-constraint count $\binom{29}{3}=3654$, with the exact constraint-to-map ratio $9.0$ (Section 4, Derivation 1).
- **C3** – Computation of the three-framework closure bound $\Delta_{\gamma}\le3.4965\times10^{-3}$ for edge errors $10^{-3}$, $2\times10^{-3}$, $5\times10^{-4}$ (Section 4, Derivation 3).
- **C4** – Classification criterion separating structural from conventional schisms based on per-edge error floors and tolerance $\tau$ (Section 3.5 and Derivation 4).
- **C5** – Application of the combinatorial machinery to a hypothesized seven-domain family, showing that at least eight schisms lie outside any pairwise reduction under a one-schism-per-pair assumption (Section 4, Derivation 2).
- **C6** – Projection that a random translation family with per-constraint compatibility probability $p=0.9$ succeeds with probability $10^{-167.3}$, and that the largest family with $>1\%$ success probability is $n_{\max}=7$ (Section 4, Derivation 5).
- **C7** – Worked two-framework corner for the Feynman-Shor bifurcation, showing that a pair of frameworks carries no composition constraint (Section 4, Derivation 2′).
- **C8** – Energy-scale window factors $2$ and $3$ for the linear-collider design ranges, and mean schisms per domain $\approx4.14$ under a uniformity assumption (Section 4, Derivation 6).
- **C9** – Mediated-translation price: replacing a direct translation error $\varepsilon=10^{-2}$ with a two-edge mediated chain incurs error $1-(1-\varepsilon)^2=0.0199$ (Section 4, Derivation 7).

## 2. Background and Related Work

Calibration across non-overlapping domains has been demonstrated in engineering contexts, and these demonstrations supply both the vocabulary and the performance baselines used in this paper. Road markings serve as a static mediating structure that enables targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap; the method exploits road markings as static and robust features among dynamic objects, and its experimental section reports that extrinsic parameters could be calculated with an accuracy of approximately $0.02\ \mathrm{m}$ and $0.086^{\circ}$ without manual operation by a human operator [3]. This is the concrete existence proof for Definition 3.4's mediating domains: two sensors that share no common field of view nevertheless acquire a consistent relative pose through a third structure visible to both. In microwave metrology, a thru-free multiline calibration for vector network analyzers eliminates the need for a thru standard by using an arbitrary transmissive two-port device together with an additional reflect standard; the method's eigenvalue formulation produces the same normalized error terms as multiline TRL because a thru definition is not required in the formulation, and the calibration plane is set automatically by the measured artifacts [8]. Work [8] thus demonstrates that a calibration family can be built from weaker, partially defined standards while preserving internal consistency—an exact analogue of building a master calibration from partial translation maps.

Observational cosmology supplies the clearest case in which calibration precision itself is the binding constraint. In 21 cm cosmology, calibration precision is currently a limiting systematic: the astrophysical foreground emission is 4–5 orders of magnitude brighter than the cosmological signal, so separating the two requires extremely precise instrumental calibration, and the field's approaches divide into sky-based calibration, which relies on an extremely accurate model of foreground emission, and redundant calibration, which requires a precisely regular array with near-identical antenna response patterns [6]. Work [6] further shows by simulation that a unified approach combining redundant calibration with a sky-model prior can improve calibration performance. For this paper, [6] motivates the non-zero per-edge error floor used in Derivation 4 and illustrates that two calibration paradigms can coexist for the same instrument class without a master calibration between them.

Machine-learning research supplies formal definitions of multi-domain calibration that parallel the present framework. Work [5] defines a classifier as calibrated when predicted confidence equals empirical accuracy, extends the definition to multiple environments, and proves in a linear-Gaussian setting that models calibrated on multiple domains are free of spurious correlations and therefore generalize out of domain, proposing multi-domain calibration as a measurable surrogate for out-of-domain performance [5]. This establishes that "calibrated across domains" is a property one can define, measure (via the Expected Calibration Error) and optimize for, supporting the paper's treatment of translation error as a measurable quantity on a test battery. Complementarily, work [7] shows that standard post-hoc calibration methods degrade under domain drift: for CIFAR-10, in-domain calibration can be excellent, but the quality of uncertainty decreases with increasing domain shift for all methods, producing highly overconfident predictions for images far from the training domain, and replacing the validation set by a transformed validation set substantially improves calibration under drift [7]. This is the empirical signature of a translation map whose error grows as it is applied farther from its defined overlap region—precisely the failure mode Definition 3.2's restriction to $S_{ij}\subseteq D_i$ is designed to exclude.

Community-scale priority setting provides a concrete institutional analogue of a physics schism. The European Particle Physics Strategy Update takes a bottom-up approach in which the community is first invited to submit proposals for projects it would like to see realised in the near-term, mid-term and longer-term future, with national and laboratory inputs as important elements [1]; its briefing book lists the fundamental puzzles unresolved in the post-Run 2 LHC era—on the particle-physics side the origin of electroweak symmetry breaking, the nature of the Higgs boson, the pattern of quark and lepton masses, and the neutrino nature and mass, and on the cosmology side dark matter, dark energy, inflation and the matter-antimatter asymmetry—and notes that this list did not change in the post-Run 2 era [1]. The same source states that at future $e^{+}e^{-}$ colliders the oblique parameters will be measured with a precision of $\sim1\%$, about a factor 10 better than current precision [1]; this $1\%$ figure is used in Section 4 as the tolerance against which translation chains are judged. The design study for the next linear collider presents the current expectations for an $e^{+}e^{-}$ linear collider of centre-of-mass energy $500\ \mathrm{GeV}$–$1\ \mathrm{TeV}$ in its abstract and $0.5$–$1.5\ \mathrm{TeV}$ in its preface, and argues that the symmetry-breaking agent must provide new physical phenomena at the TeV energy scale [2]; the two stated ranges differ by a factor 2 versus a factor 3 in window width, a discrepancy quantified in Derivation 6.

In fusion energy, work [4] examines CFETR and HFRC through MHD analysis of their physical designs, employing Westerhof-Pratt's closure relation for the ECCD density in its simulations and reporting that for CFETR the ECCD power and current required for full stabilization of the neoclassical tearing mode have been predicted, while for 80% of the SSO scenarios active control methods may be required for resistive-wall-mode stabilization [4]. Its introduction notes that the complexity and economic cost associated with tokamak size is expected to far exceed existing devices, often requiring collaborative efforts of multiple countries and unions for many years [4]. This supplies the cost side of the introduction's problem statement: framework choices in fusion are multi-decade, multi-nation commitments.

The inventory of unresolved bifurcations enumerates 29 distinct schisms spanning topics from the nature of the continuum to the status of the observer, and argues they are facets of a single underlying assumption rather than independent puzzles [10]. Its introduction records the precision baseline against which the schisms stand—quantum electrodynamics predicting the electron's magnetic moment to eleven decimal places while the cosmological constant is off by 120 orders of magnitude from naive expectations—and its conclusion proposes a self-referential calibration framework in which a calibration operator is a contraction mapping whose fixed point is the physics [10]. The present paper takes a complementary, deliberately conservative route: rather than assuming convergence to a fixed point, it counts the constraints a master calibration must satisfy and bounds the probability that an unengineered family satisfies them. The prior version of this paper [9] introduced the framework definitions and the counting programme; the present text revises and completes those derivations, in particular the seven-domain capacity argument of [9]'s Derivation 2 and the closure and genericity computations of its Results section.

## 3. Methods

### 3.1 Frameworks and domains

**Definition 3.1 (Framework).** A framework is a pair $F_i=(D_i,\mathcal{P}_i)$ where $D_i$ is a domain (set of states, configurations, or propositions) and $\mathcal{P}_i$ is a set of primitives (quantities, operations, or axioms) taken as given without further calibration. *Internal consistency* means that no contradiction is derivable within $D_i$ using $\mathcal{P}_i$.

*Examples.*
- $F_{\mathrm{QM}}$ (non-relativistic quantum mechanics) with primitives $|\psi\rangle$ and $U_t=e^{-iHt/\hbar}$.
- $F_{\mathrm{SM}}$ (classical statistical mechanics) with phase-space measure and coarse-graining cells.
- $F_{\mathrm{GR}}$ (general relativity) with metric $g_{\mu\nu}$.

### 3.2 Translation maps and error

**Definition 3.2 (Translation map).** A translation $\tau_{ij}:S_{ij}\to D_j$ is a partial map defined on overlap $S_{ij}\subseteq D_i$, equipped with a *translation error* $\varepsilon_{ij}\in[0,1)$ measured as the fraction of propositions on a chosen test battery for which $\tau_{ij}$ disagrees with the best $F_j$-native rendering. Directionality is allowed: $\varepsilon_{ij}\neq\varepsilon_{ji}$.

The restriction to $S_{ij}$ is not decorative. Work [7] documents the empirical consequence of ignoring it: post-hoc calibrated models become highly overconfident when applied to inputs far from the training domain, with calibration quality decreasing monotonically with domain shift across all methods tested [7]. A translation map is therefore defined only where a test battery exists, and its error is a property of that battery.

*Canonical examples.*
- Decoherence supplies $\tau_{\mathrm{QM}\to\mathrm{cl}}$ on the sector where environment-induced superselection holds.
- Coarse-graining supplies $\tau_{\mu\to M}$ above a resolution scale $\ell_{\mathrm{cg}}$.

### 3.3 Composition and closure

For composable translations $\tau_{ij}$ and $\tau_{jk}$, the composed error obeys the first-order bound

$$\varepsilon_{ij\circ jk}\le\varepsilon_{ij}+\varepsilon_{jk}+\varepsilon_{ij}\,\varepsilon_{jk}.$$

**Definition 3.3 (Composition failure).** Failure occurs if there exists $x\in\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$ such that $(\tau_{jk}\circ\tau_{ij})(x)\neq\tau_{ik}(x)$.

For a cycle $\gamma$ with edges $e\in\gamma$ and errors $\varepsilon_e$, the *closure error* satisfies

$$\Delta_{\gamma}\le1-\prod_{e\in\gamma}(1-\varepsilon_e).$$

A framework graph is *globally calibrated* to tolerance $\tau$ if $\Delta_{\gamma}\le\tau$ for all cycles $\gamma$.

**Definition 3.4 (Master calibration).** A family $\mathcal{T}=\{\tau_{ij}\}_{i<j}$ is a master calibration if every square commutes: $\tau_{jk}\circ\tau_{ij}=\tau_{ik}$ on $\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$.

### 3.4 Mediating domains

Following the engineering strategy exemplified by road-marking mediation between non-overlapping sensor fields of view [3] and by the construction of a calibration family from partially defined standards in microwave metrology [8], we introduce a mediating domain $M$ with translations $\tau_{iM}:S_{iM}\to M$ and $\tau_{Mj}:M\supset\tau_{iM}(S_{iM})\to D_j$. The mediated translation $\tau_{Mj}\circ\tau_{iM}$ incurs two edge errors instead of one direct error, a price quantified in Derivation 7. The road-marking result of [3]—$0.02\ \mathrm{m}$ and $0.086^{\circ}$ accuracy without a human operator—demonstrates that mediation can be both automatic and accurate in a real non-overlapping configuration.

### 3.5 Structural versus conventional schisms

**Definition 3.5.** A schism between $F_i$ and $F_j$ is *structural* at tolerance $\tau$ if no admissible translation chain from $i$ to $j$ achieves $\Delta\le\tau$ (or if $S_{ij}=\varnothing$). It is *conventional* if such a chain exists but is costly (e.g., long, or requiring strong auxiliary assumptions such as the extremely accurate foreground model on which sky-based 21 cm calibration relies [6]). The master-calibration problem asks whether an assignment of edge errors can make all cycles close within $\tau$.

## 4. Analysis

All inputs below are stated with sources or as explicit assumptions; all arithmetic is shown step by step. No empirical data are collected or used in this paper.

**Input 1 (from [10]):** the number of unresolved bifurcations is $N_{\mathrm{schism}}=29$.

**Input 2 (assumption):** a candidate family of $n=7$ research domains is modeled as a small master-calibration problem; no cited work provides this number.

**Input 3 (assumption):** the Feynman-Shor bifurcation partitions quantum computing into $m=2$ ontologies.

**Input 4 (from [2]):** the proposed linear-collider centre-of-mass energy range is $E_{\mathrm{cm}}=500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ (abstract) and $0.5$–$1.5\ \mathrm{TeV}$ (preface).

**Input 5 (from [6]):** calibration precision is a limiting systematic in 21 cm cosmology, with foregrounds 4–5 orders of magnitude brighter than the cosmological signal, motivating a non-zero error floor.

**Input 6 (from [1]):** oblique parameters at future $e^{+}e^{-}$ colliders are expected to be measured with a precision of $\sim1\%$.

**Input 7 (from [3]):** mediated (road-marking) calibration of non-overlapping sensors achieved approximately $0.02\ \mathrm{m}$ and $0.086^{\circ}$ accuracy.

### Derivation 1: counting maps and composition constraints.

Treat the 29 bifurcations as 29 frameworks. The number of unordered pairwise translation maps is

$$\binom{N}{2}=\frac{29\times28}{2}=406.$$

Each unordered triple $\{i,j,k\}$ yields one independent square constraint, giving

$$\binom{29}{3}=\frac{29\times28\times27}{6}=3654.$$

The constraint-to-map ratio is

$$\frac{3654}{406}=9.0,$$

exactly because $\displaystyle\frac{\binom{N}{3}}{\binom{N}{2}}=\frac{N-2}{3}=\frac{27}{3}=9$.

*Factor-2 reading.* If each bifurcation is counted as two opposite-direction frameworks, $N=58$, giving

$$\binom{58}{2}=1653,\qquad\binom{58}{3}=30856,$$

and a ratio $30856/1653\approx18.667$.

### Derivation 2: pairwise capacity for the seven-domain family.

For $n=7$ domains, unordered pairs are

$$P=\binom{7}{2}=\frac{7\times6}{2}=21,$$

and directed pairs are $7\times6=42$. Since $N_{\mathrm{schism}}=29>21$, the family can host at most $21$ distinct unordered pairs.

**Additional assumption (one-schism-per-pair).** If each of the 29 bifurcations must occupy a distinct unordered pair, then at least

$$29-21=8$$

bifurcations cannot be assigned a distinct pair and would require either repeated pairs or additional domains. Equivalently: since $N_{\mathrm{schism}}=29>21$, at least $29-21=8$ schisms lie outside any pairwise reduction involving only the seven claimed vocabularies.

### Derivation 2′: two-framework corner (Feynman-Shor).

For $m=2$ ontologies, the number of unordered pairs is

$$\binom{2}{2}=1,$$

and the number of unordered triples is

$$\binom{2}{3}=0.$$

Thus a pair of frameworks carries no composition constraint: any single translation map, however imperfect, trivially satisfies the master-calibration condition for that pair because there is no third framework to create a cycle.

### Derivation 3: closure-error budget for a three-framework loop.

Choose edge errors

$$\varepsilon_{12}=10^{-3},\qquad\varepsilon_{23}=2\times10^{-3},\qquad\varepsilon_{31}=5\times10^{-4}.$$

The closure bound is

$$\Delta_{\gamma}\le1-(1-\varepsilon_{12})(1-\varepsilon_{23})(1-\varepsilon_{31}).$$

Compute each factor:

$$1-\varepsilon_{12}=0.999,$$
$$1-\varepsilon_{23}=0.998,$$
$$1-\varepsilon_{31}=0.9995.$$

Product:

$$0.999\times0.998=0.997002,$$
$$0.997002\times0.9995=0.996503499.$$

Hence

$$\Delta_{\gamma}\le1-0.996503499=0.003496501\approx3.4965\times10^{-3}.$$

The additive first-order bound $\varepsilon_{12}+\varepsilon_{23}+\varepsilon_{31}=3.5\times10^{-3}$ agrees to within $3.5\times10^{-6}$.

### Derivation 4: tolerance at which a schism becomes structural.

Assume a translation chain of $k=4$ edges, each with a floor $\varepsilon_{\min}=10^{-2}$ (motivated by the limiting systematic in 21 cm cosmology [6]). The closure bound is

$$\Delta\le1-(1-\varepsilon_{\min})^{k}=1-(0.99)^{4}.$$

Compute:

$$0.99^{2}=0.9801,\qquad0.9801^{2}=0.96059601.$$

Thus

$$\Delta\le1-0.96059601=0.03940399\approx3.94\times10^{-2}.$$

Any application demanding $\tau<3.94\times10^{-2}$ classifies the schism as structural under this chain. Solving

$$1-(1-\varepsilon_{\min})^{k}\le\tau$$

for $k$ yields

$$k\le\frac{\ln(1-\tau)}{\ln(1-\varepsilon_{\min})}.$$

For $\tau=10^{-2}$ and $\varepsilon_{\min}=10^{-2}$,

$$k\le\frac{\ln(0.99)}{\ln(0.99)}=1,$$

showing that only direct translations can meet a $1\%$ tolerance—the precision at which [1] reports oblique parameters will be measured at future $e^{+}e^{-}$ colliders.

### Derivation 5: genericity of commutative squares (projection).

Assume each of the $3654$ square constraints holds independently with probability $p$. The probability that **all** constraints hold is

$$P_{\mathrm{master}}=p^{3654}.$$

For $p=0.9$,

$$\ln p=\ln 0.9=-0.1053605,$$
$$\ln P_{\mathrm{master}}=3654\times(-0.1053605)=-385.2,$$
$$P_{\mathrm{master}}=e^{-385.2}\approx10^{-167.3}.$$

To achieve success probability $\ge0.01$, we require

$$\binom{n}{3}\le\frac{\ln(0.01)}{\ln(0.9)}\approx43.7.$$

The largest integer $n$ satisfying this inequality is $n_{\max}=7$ because $\binom{7}{3}=35$ and $\binom{8}{3}=56>43.7$.

*Projection with $p=0.99$ (assumption).* If $p=0.99$,

$$P_{\mathrm{master}}=0.99^{3654}=e^{3654\ln 0.99}\approx e^{-36.8}\approx10^{-15.9},$$

still negligible.

### Derivation 6: energy-scale window and schism density.

The collider energy window spans a factor

$$\frac{1\ \mathrm{TeV}}{500\ \mathrm{GeV}}=2$$

using the abstract range of [2], and a factor

$$\frac{1.5\ \mathrm{TeV}}{0.5\ \mathrm{TeV}}=3$$

using the preface range of [2]. Assuming a uniform distribution of the $29$ schisms over the $7$ domains, the mean per-domain count is

$$\frac{29}{7}=4.142857\approx4.14.$$

### Derivation 7: mediated-translation price.

A direct translation edge with error $\varepsilon=10^{-2}$ incurs error $\varepsilon$. Introducing a mediating domain replaces the direct edge by two edges each with error $\varepsilon$, yielding total error

$$\varepsilon_{\text{mediated}}=1-(1-\varepsilon)^2=1-(0.99)^2=0.0199.$$

Thus the mediated chain roughly doubles the error budget, illustrating the cost of adding a mediating domain. The road-marking calibration in [3] provides a concrete performance baseline for mediated calibrations.

## 5. Results

Only quantities computed in Section 4 are reported, together with clearly labeled projections.

**R1 (computed).** A master calibration over $N=29$ frameworks requires $\binom{29}{2}=406$ pairwise translation maps subject to $\binom{29}{3}=3654$ independent composition constraints—a constraint-to-map ratio of exactly $9.0$. Under the factor-2 reading ($N=58$) the counts are $1653$ maps and $30856$ constraints, ratio $18.667$.

**R2 (computed).** For the hypothesized $n=7$ domain family, the number of unordered pairwise translations is $P=21$ (directed: $42$). Since $N_{\mathrm{schism}}=29$ [10] and $29>21$, at most $21$ bifurcations can be assigned distinct unordered pairs; under the one-schism-per-pair assumption at least $8$ bifurcations remain unassigned, i.e. at least $8$ schisms lie outside any pairwise reduction involving only the seven claimed vocabularies.

**R3 (computed).** For a three-edge cycle with edge errors $10^{-3}$, $2\times10^{-3}$, $5\times10^{-4}$, the closure error is bounded by $\Delta_{\gamma}\le3.4965\times10^{-3}$, consistent with the additive bound $3.5\times10^{-3}$.

**R4 (computed).** With a per-edge error floor of $10^{-2}$ and a $4$-edge chain, the minimum achievable closure error is $\approx3.94\times10^{-2}$; demanding $\tau=10^{-2}$ restricts admissible chains to $k\le1$.

**R5 (computed).** The collider energy window of [2] spans a factor of $2$ (abstract) and $3$ (preface); thus it can serve as a shared observable only for translations whose discriminating phenomena fall within that band.

**R6 (computed).** Mean schisms per domain under uniform distribution of $29$ over $7$ is $\approx4.14$.

**R7 (computed).** For the Feynman-Shor bifurcation ($m=2$), there is $1$ unordered pair and $0$ composition constraints, so any single translation trivially satisfies the master-calibration condition for that pair.

**Projection P1 (labeled projection).** Assuming independent square-constraint success probability $p=0.9$, the probability that all $3654$ squares commute is $P_{\mathrm{master}}\approx10^{-167.3}$, and the largest family size with $\ge1\%$ success probability is $n_{\max}=7$. At $p=0.99$ the probability is $\approx10^{-15.9}$, still negligible.

**Projection P2 (labeled projection).** Halving each edge error in the R3 cycle (factor $f=0.5$) yields a new closure bound

$$\Delta_{\gamma}'\le1-(1-0.5\times10^{-3})(1-0.5\times2\times10^{-3})(1-0.5\times5\times10^{-4})=1.749\times10^{-3},$$

approximately a factor-two reduction, consistent with first-order behavior.

**Projection P3 (labeled projection).** Introducing a mediating domain doubles the error budget from $\varepsilon=10^{-2}$ to $\varepsilon_{\text{mediated}}=0.0199$, illustrating the cost of mediation.

## 6. Discussion

### Limitations

1. **Framework identification.** Mapping the $29$ bifurcations of [10] to $29$ frameworks is a modeling choice; calibrating both sides of each dichotomy would double the tower count to $58$, but the qualitative overdetermination persists (ratio $18.667$ instead of $9.0$).
2. **Error-model abstraction.** The translation error $\varepsilon_{ij}$ depends on a chosen test battery of propositions, itself a convention. Correlated errors across frameworks would violate the independence assumption underlying the composition bound and could worsen closure beyond the estimates presented.
3. **Empirical measurability.** For frameworks as disparate as general relativity and quantum mechanics, no shared test battery currently exists, so $\varepsilon_{ij}$ cannot be measured today; this renders many schisms structural at any non-trivial tolerance.
4. **Genericity projection.** The probability estimates in Derivation 5 assume independent constraints with a uniform success probability $p$, an assumption that is unlikely to hold in practice; the numbers therefore illustrate overdetermination rather than predict actual success rates.
5. **One-schism-per-pair assumption.** The statement that $8$ bifurcations remain unassigned under a seven-domain family relies on the additional assumption that each bifurcation must occupy a distinct unordered pair; without this assumption the conclusion weakens to a capacity bound only.
6. **Bibliographic scope.** The citation base is limited to the works listed in the References; no claim in this paper depends on literature outside that list, and conclusions that would require broader empirical support (e.g., actual error floors in physical translation chains) are labeled as assumptions or projections.

### Falsifiability

The framework would be falsified by an explicit construction of a family of $n\ge10$ frameworks admitting translation maps whose squares commute to a tolerance $\tau$ without any engineered mediating domain or auxiliary standard. Demonstrating such a family would contradict the combinatorial bound that random families succeed only up to $n_{\max}=7$ (Derivation 5) and would show that global consistency can arise spontaneously rather than being enforced by construction. A second falsification path targets the closure bound