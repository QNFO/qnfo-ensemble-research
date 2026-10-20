# Master Calibration for Non-Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation (Revised Version)

## Abstract

Physics is fragmented by persistent bifurcations—general relativity versus quantum mechanics, continuum versus discrete descriptions, the Heisenberg cut, and the status of the observer. These schisms impose concrete costs: collider, fusion, and quantum-hardware programmes proceed without a shared observable that can bridge the frameworks underlying their design choices. This work asks whether a *master calibration*—a family of partial translation maps that composes consistently across all frameworks—can exist, and what combinatorial and error-budget burden such a calibration imposes. Frameworks, translation maps with quantified error, composition failure, and master calibration are formalized. Counting arguments applied to a 29-schism inventory yield 406 unordered pairwise maps and 3654 independent composition constraints, a constraint-to-map ratio of exactly 9.0. A seven-domain family admits only 21 unordered pairs, so at least 8 schisms lie outside any pairwise reduction under a one-schism-per-pair assumption. A three-framework loop with edge errors $10^{-3}$, $2\times10^{-3}$, and $5\times10^{-4}$ gives a closure-error bound of $3.4965\times10^{-3}$. A genericity projection with independent square-constraint success probability $p=0.9$ gives a master-calibration success probability of $6.34\times10^{-168}$ and a maximal family size of $n_{\max}=7$ at a $1\%$ success threshold. The results separate structural schisms (no admissible translation within tolerance) from conventional ones (admissible but costly) and show that beyond small families global consistency must be enforced by construction rather than hoped for.

## 1. Introduction

Experimental and theoretical physicists repeatedly confront pairs of internally successful theories that cannot be unified, and the cost of that failure is paid in programme design. The European Particle Physics Strategy Update aggregates community proposals for near-term, mid-term, and longer-term collider projects precisely because no single framework tells the community which observable to build next [1]. The design study for a next linear collider specifies a centre-of-mass energy window of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ and justifies the machine by its role in exploring physics beyond the Standard Model—a proposed shared observable whose reach is set by the frameworks it must bridge [2]. In fusion energy, the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC) represent low-density steady-state and high-density pulsed pathways whose magnetohydrodynamic stability assessments differ, so that for CFETR active control methods may be required for resistive-wall-mode stabilization in 80% of steady-state-operation scenarios [4]. In quantum computing, the unresolved measurement problem and the Heisenberg cut separate quantum control from classical engineering, and divergent compositional versus holistic readings of quantum states impede error-corrected processor design.

A systematic inventory of such fractures enumerates 29 distinct unresolved bifurcations, spanning topics from the nature of the continuum to the status of the observer, and argues that they are interconnected rather than isolated puzzles [10]. The same inventory notes the scale of the stakes: quantum electrodynamics predicts the electron's magnetic moment to eleven decimal places while the cosmological constant disagrees with naive expectations by 120 orders of magnitude, so individual frameworks can be spectacularly accurate inside their domains while remaining mutually uncalibrated [10]. If a family of partial translation maps could be constructed that composes consistently across all frameworks, design decisions for colliders, fusion reactors, and quantum technologies could be guided by a unified calibration budget rather than by ad-hoc compromises. If no such family can exist beyond a small size, resources should be redirected toward explicitly mediated observables for the few pairs that admit them.

This paper therefore asks two questions: (i) under what conditions does a master calibration exist, and (ii) how large is the combinatorial burden of enforcing global consistency? The analysis formalizes frameworks as calibrated theories over disjoint domains, defines translation maps with explicit error budgets, bounds composition failure by cycle-closure error, and applies counting arguments to the 29-schism inventory [10] and to a modeled seven-domain family. This version corrects and tightens the derivations of the earlier published version [9]: the pairwise-capacity argument and the falsifiability criterion are restated with their assumptions explicit, and the sensitivity computation of the closure error under uniform error scaling is corrected (Derivation 8).

**Contributions.**
- **C1** – Formal definitions of framework, translation map, composition failure, and master calibration (Section 3).
- **C2** – Derivation of the pairwise-map count $\binom{29}{2}=406$ and composition-constraint count $\binom{29}{3}=3654$, with the exact constraint-to-map ratio $9.0$ and its factor-2 variant (Section 4, Derivation 1).
- **C3** – The pairwise-capacity result for a seven-domain family: $\binom{7}{2}=21$ pairs against 29 schisms, so at least $29-21=8$ schisms lie outside any pairwise reduction under the one-schism-per-pair assumption (Section 4, Derivation 2).
- **C4** – The two-framework corner for the Feynman–Shor bifurcation: a pair of frameworks carries no composition constraint (Section 4, Derivation 2′).
- **C5** – The three-framework closure bound $\Delta_{\gamma}\le 3.4965\times10^{-3}$ for edge errors $10^{-3}$, $2\times10^{-3}$, $5\times10^{-4}$ (Section 4, Derivation 3).
- **C6** – The structural-versus-conventional classification criterion, including the chain-length bound $k\le\ln(1-\tau)/\ln(1-\varepsilon_{\min})$ (Section 3.5 and Section 4, Derivation 4).
- **C7** – The genericity projection $P_{\mathrm{master}}=p^{3654}=6.34\times10^{-168}$ at $p=0.9$, the threshold count $\binom{n}{3}\le 43.7$, and the maximal family size $n_{\max}=7$ (Section 4, Derivation 5).
- **C8** – Energy-scale window factors $2$ and $3$ for the linear-collider design ranges, and mean schisms per domain $29/7\approx 4.14$ under a uniformity assumption (Section 4, Derivation 6).
- **C9** – The mediated-translation price $1-(1-\varepsilon)^2=0.0199$ for $\varepsilon=10^{-2}$ (Section 4, Derivation 7).
- **C10** – The corrected sensitivity analysis of closure error under uniform scaling of edge errors, $\Delta'_{\gamma}=1.7491\times10^{-3}$ at $f=0.5$ (Section 4, Derivation 8).
- **C11** – The required per-edge error $\varepsilon\le 3.33\times10^{-4}$ for a three-edge loop to meet a tolerance $\tau=10^{-3}$ (Section 4, Derivation 9).

## 2. Background and Related Work

Calibration across non-overlapping domains has been demonstrated in engineering contexts, and these demonstrations supply both the vocabulary and the performance baselines used below. Road markings serve as a static mediating structure that enables targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap; the method exploits road markings as static and robust features among dynamic objects, and its conclusion reports that extrinsic parameters can be computed with an accuracy of approximately $0.02\ \mathrm{m}$ and $0.086^{\circ}$ without manual operation by a human operator [3]. The same work cautions that its assumption of locally accurate odometry can fail under repeated vehicle accelerations, which would distort the 3D map—a concrete instance of an auxiliary assumption limiting a mediated calibration, the situation Definition 3.5 below calls a conventional schism. In microwave metrology, the thru-free multiline calibration eliminates the need for a thru standard in vector-network-analyzer calibration by using an arbitrary transmissive two-port device together with an additional reflect standard; the method's verification shows excellent agreement with multiline TRL when a thru standard is available, and it sets the calibration-plane location automatically from the measured artifacts [8]. This is an engineering realization of building a calibration family from weaker or partially defined standards, which is exactly the mediating-domain strategy of Section 3.4.

In observational cosmology, calibration precision is identified as a limiting systematic in 21 cm experiments: astrophysical foreground emission is 4–5 orders of magnitude brighter than the cosmological signal, so separating the two requires extremely precise instrumental calibration, and the field's two paradigms—sky-based calibration, which relies on very good a priori models of sky and instrument, and redundant calibration, which assumes perfectly redundant baselines—each lean on distinct external regularities [6]. The same work's simulation results indicate that a unified approach combining redundant calibration with a sky-model prior can improve calibration performance, an example of two calibration paradigms coexisting for one instrument class and of a partial merge across them. In machine learning, calibration is defined across multiple environments by the condition $\mathbb{E}[Y\mid f(X)=\alpha, E=e_i]=\alpha$ for every training environment $e_i$; the linear-Gaussian analysis proves that models calibrated on multiple domains are free of spurious correlations and therefore generalize out of domain, and multi-domain calibration is proposed as a practical, measurable surrogate for out-of-domain performance [5]. This supplies a formal precedent for requiring a calibration property to hold over a family of domains simultaneously, which is the structure of the master-calibration condition in Definition 3.4.

Domain drift sharpens the point that translations degrade outside their home territory. Post-hoc uncertainty calibration for domain drift scenarios evaluates methods over 28 distinct perturbation types not seen during training and shows that while excellent in-domain calibration is achievable, the quality of uncertainty decreases with increasing domain shift, producing highly overconfident predictions for images far from the training domain; replacing the validation set by a transformed validation set substantially improves calibration under drift [7]. This motivates the restriction of each translation map to an explicit overlap region $S_{ij}$ in Definition 3.2: a translation applied outside its calibrated overlap is documented to fail in exactly this way.

Community-scale priority setting provides a concrete analogue of a physics schism being adjudicated without a master framework. The European Particle Physics Strategy Update takes a bottom-up approach in which the community submits proposals for projects it would like to see realised in the near-term, mid-term, and longer-term future, with national and laboratory inputs as important elements [1]. Its briefing book also quantifies what a shared observable can deliver: at future $e^{+}e^{-}$ colliders the oblique parameters will be measured with a precision of $\sim 1\%$, about a factor 10 better than current precision, and at circular colliders $10^{12}$ Z-bosons would be available [1]. The design study for the next linear collider presents a centre-of-mass energy of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ in its abstract and $0.5$–$1.5\ \mathrm{TeV}$ in its preface, reviews the experiments the facility would carry out, and reports that microwave power sources had already exceeded the requirements for the initial stage of the machine [2]; the Stanford Linear Collider was conceived to study the 100-GeV scale and to develop the accelerator physics needed for future colliders [2]. These two energy ranges are used as inputs in Derivation 6.

Fusion energy supplies a second domain-specific calibration problem. CFETR and HFRC are the two major Chinese projects representative of the low-density steady-state and high-density pulsed pathways to fusion, and one primary task of their physics designs is the assessment of magnetohydrodynamic stability [4]. For CFETR, the work predicts the electron-cyclotron current drive power and current required for full stabilization of the neoclassical tearing mode, performs magnetohydrodynamic simulations with a Lundquist number $S=5.56\times10^{6}$ at a $q=2$ surface, and finds that for 80% of steady-state-operation scenarios active control methods may be required for resistive-wall-mode stabilization [4]. The differing diagnostics and control requirements between the two pathways exemplify how two internally consistent frameworks can demand different mediating observables.

The inventory of unresolved bifurcations enumerates 29 distinct schisms and argues they are facets of a single underlying assumption rather than independent puzzles; it also develops a self-referential calibration framework in which a calibration operator on the space of theories is shown, under an ultrametric distinction function, to be a contraction mapping possessing a unique fixed point [10]. That fixed-point result is a global-existence claim under strong geometric assumptions; the present paper complements it with local, assumption-light counting and error-budget results that show what any calibration family must pay. Finally, the earlier published version of this work [9] introduced the framework definitions, the mediating-domain construction, and the core derivations R1–R3; the present revision restates those results with corrected arithmetic where needed and with the assumptions behind the pairwise-capacity and falsifiability statements made explicit.

## 3. Methods

### 3.1 Frameworks and domains

**Definition 3.1 (Framework).** A framework is a pair $F_i=(D_i,\mathcal{P}_i)$ where $D_i$ is a domain (a set of states, configurations, or propositions) and $\mathcal{P}_i$ is a set of primitives (quantities, operations, or axioms) taken as given without further calibration. *Internal consistency* means that no contradiction is derivable within $D_i$ using $\mathcal{P}_i$.

*Examples.*
- $F_{\mathrm{QM}}$ (non-relativistic quantum mechanics) with primitives $|\psi\rangle$ and $U_t=e^{-iHt/\hbar}$.
- $F_{\mathrm{SM}}$ (classical statistical mechanics) with phase-space measure and coarse-graining cells.
- $F_{\mathrm{GR}}$ (general relativity) with metric $g_{\mu\nu}$.

These definitions carry over from the published version [9]; they are restated here because every derivation below depends on them.

### 3.2 Translation maps and error

**Definition 3.2 (Translation map).** A translation $\tau_{ij}:S_{ij}\to D_j$ is a partial map defined on an overlap $S_{ij}\subseteq D_i$, equipped with a *translation error* $\varepsilon_{ij}\in[0,1)$ measured as the fraction of propositions on a chosen test battery for which $\tau_{ij}$ disagrees with the best $F_j$-native rendering. Directionality is allowed: $\varepsilon_{ij}\neq\varepsilon_{ji}$.

The restriction to $S_{ij}$ is essential rather than technical. In the machine-learning setting, models that are well calibrated in-domain produce highly overconfident predictions when applied far from their training distribution, and calibration quality degrades monotonically with the magnitude of the shift [7]; a translation map used outside its calibrated overlap is the same failure mode. Decoherence supplies a canonical $\tau_{\mathrm{QM}\to\mathrm{cl}}$ on the sector where environment-induced superselection holds, and coarse-graining supplies a $\tau_{\mu\to M}$ above a resolution scale $\ell_{\mathrm{cg}}$; both are partial by construction.

### 3.3 Composition and closure

For composable translations $\tau_{ij}$ and $\tau_{jk}$, the composed error obeys the first-order bound

$$\varepsilon_{ij\circ jk}\le\varepsilon_{ij}+\varepsilon_{jk}+\varepsilon_{ij}\,\varepsilon_{jk}.$$

**Definition 3.3 (Composition failure).** Failure occurs if there exists $x\in\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$ such that $(\tau_{jk}\circ\tau_{ij})(x)\neq\tau_{ik}(x)$.

For a cycle $\gamma$ with edges $e\in\gamma$ and errors $\varepsilon_e$, the *closure error* satisfies

$$\Delta_{\gamma}\le 1-\prod_{e\in\gamma}(1-\varepsilon_e).$$

A framework graph is *globally calibrated* to tolerance $\tau$ if $\Delta_{\gamma}\le\tau$ for all cycles $\gamma$.

**Definition 3.4 (Master calibration).** A family $\mathcal{T}=\{\tau_{ij}\}_{i<j}$ is a master calibration if every square commutes: $\tau_{jk}\circ\tau_{ij}=\tau_{ik}$ on $\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$.

The multi-environment calibration condition of [5]—that a calibrated property hold for every environment in a family simultaneously—is the direct analogue of Definition 3.4 with cycles in place of environments: both demand a single object that is consistent across an entire family of contexts, not merely pairwise.

### 3.4 Mediating domains

Following the engineering strategy exemplified by road-marking mediation between non-overlapping sensor fields of view [3] and by the construction of a calibration family from partially defined standards in microwave metrology [8], introduce a mediating domain $M$ with translations $\tau_{iM}:S_{iM}\to M$ and $\tau_{Mj}:M\supset\tau_{iM}(S_{iM})\to D_j$. The mediated translation $\tau_{Mj}\circ\tau_{iM}$ incurs two edge errors instead of one direct error; Derivation 7 quantifies this price. The road-marking result also illustrates the auxiliary-assumption cost: its accuracy figure of $0.02\ \mathrm{m}$ and $0.086^{\circ}$ rests on locally accurate odometry, an assumption its own conclusion flags as fragile under repeated vehicle acceleration [3].

### 3.5 Structural versus conventional schisms

**Definition 3.5.** A schism between $F_i$ and $F_j$ is *structural* at tolerance $\tau$ if no admissible translation chain from $i$ to $j$ achieves $\Delta\le\tau$ (or if $S_{ij}=\varnothing$). It is *conventional* if such a chain exists but is costly—for example, long, or requiring strong auxiliary assumptions such as the extremely accurate foreground model on which sky-based calibration in 21 cm cosmology relies [6]. The master-calibration problem asks whether an assignment of edge errors can make all cycles close within $\tau$.

### 3.6 Method summary

The method of this paper is analytical: definitions 3.1–3.5 are stated, and Sections 4 and 5 derive consequences by (i) combinatorial counting over the schism inventory of [10], (ii) exact evaluation of the closure-error bound of Section 3.3 for stated edge errors, and (iii) a probabilistic projection under an explicitly assumed independence model. No experiment, measurement, or simulation is performed here; every numerical input is either taken from a cited work and labeled with its citation, or stated as an explicit assumption.

## 4. Analysis

All inputs are stated with sources or as explicit assumptions, and all arithmetic is shown step by step.

**Input 1 (from [10]):** the number of unresolved bifurcations is $N_{\mathrm{schism}}=29$.

**Input 2 (assumption):** a candidate family of $n=7$ research domains is modeled as a small master-calibration problem; no cited work provides this number.

**Input 3 (assumption):** the Feynman–Shor bifurcation partitions quantum computing into $m=2$ ontologies.

**Input 4 (from [2]):** the proposed linear-collider centre-of-mass energy range is $E_{\mathrm{cm}}=500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ (abstract) and $0.5$–$1.5\ \mathrm{TeV}$ (preface).

**Input 5 (from [6]):** calibration precision is a limiting systematic in 21 cm cosmology, with foregrounds 4–5 orders of magnitude brighter than the cosmological signal, motivating a non-zero error floor.

**Input 6 (from [1]):** oblique parameters at future $e^{+}e^{-}$ colliders are expected to be measured with a precision of $\sim 1\%$, about a factor 10 better than current precision.

**Input 7 (from [3]):** mediated (road-marking) calibration of non-overlapping sensors achieved approximately $0.02\ \mathrm{m}$ and $0.086^{\circ}$ accuracy.

### Derivation 1: counting maps and composition constraints

Treat the 29 bifurcations as 29 frameworks. The number of unordered pairwise translation maps is

$$\binom{N}{2}=\frac{29\times28}{2}=406.$$

Each unordered triple $\{i,j,k\}$ yields one independent square constraint, giving

$$\binom{29}{3}=\frac{29\times28\times27}{6}=\frac{21924}{6}=3654.$$

The constraint-to-map ratio is

$$\frac{3654}{406}=9.0,$$

exactly, because in general

$$\frac{\binom{N}{3}}{\binom{N}{2}}=\frac{N-2}{3}=\frac{27}{3}=9.$$

*Factor-2 reading.* If each bifurcation is counted as two opposite-direction frameworks, $N=58$, giving

$$\binom{58}{2}=\frac{58\times57}{2}=1653,\qquad \binom{58}{3}=\frac{58\times57\times56}{6}=30856,$$

and a ratio $\frac{30856}{1653}=\frac{56}{3}\approx 18.667$.

### Derivation 2: pairwise capacity for the seven-domain family

For $n=7$ domains, unordered pairs number

$$P=\binom{7}{2}=\frac{7\times6}{2}=21,$$

and directed pairs number $7\times6=42$.

**Assumption (one-schism-per-pair).** Suppose each of the 29 bifurcations must be resolved by a distinct unordered pair of the seven domains—that is, each schism is assigned its own pairwise reduction, and no pair carries more than one schism. Since $N_{\mathrm{schism}}=29>21$, the family can host at most 21 distinct unordered pairs, so at least

$$29-21=8$$

bifurcations cannot be assigned a distinct pair. Under this assumption, at least 8 schisms lie outside any pairwise reduction involving only the seven claimed vocabularies; resolving them would require either repeated pairs (contradicting the assumption) or additional domains. The conclusion is a capacity statement conditional on the one-schism-per-pair assumption: if several schisms may share one pair, the count of unassignable schisms is smaller, and the derivation fixes only the pair budget $\binom{7}{2}=21$ against the demand of 29 distinct assignments.

### Derivation 2′: two-framework corner (Feynman–Shor)

For $m=2$ ontologies, the number of unordered pairs is

$$\binom{2}{2}=1,$$

and the number of unordered triples is

$$\binom{2}{3}=0.$$

A pair of frameworks therefore carries no composition constraint: any single translation map, however imperfect, trivially satisfies the master-calibration condition for that pair, because no third framework exists to create a cycle. This is the corner case in which the overdetermination argument of Derivation 1 does not bind.

### Derivation 3: closure-error budget for a three-framework loop

Choose edge errors

$$\varepsilon_{12}=10^{-3},\qquad \varepsilon_{23}=2\times10^{-3},\qquad \varepsilon_{31}=5\times10^{-4}.$$

The closure bound is

$$\Delta_{\gamma}\le 1-(1-\varepsilon_{12})(1-\varepsilon_{23})(1-\varepsilon_{31}).$$

Compute each factor:

$$1-\varepsilon_{12}=0.999,\qquad 1-\varepsilon_{23}=0.998,\qquad 1-\varepsilon_{31}=0.9995.$$

Product:

$$0.999\times0.998=0.997002,$$
$$0.997002\times0.9995=0.997002-0.997002\times0.0005=0.997002-0.000498501=0.996503499.$$

Hence

$$\Delta_{\gamma}\le 1-0.996503499=0.003496501\approx 3.4965\times10^{-3}.$$

The additive first-order bound $\varepsilon_{12}+\varepsilon_{23}+\varepsilon_{31}=3.5\times10^{-3}$ agrees with the exact product bound to within $3.5\times10^{-6}$,