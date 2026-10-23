# Master Calibration for Non‑Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation (Version 3.0)

## Abstract

Physics is fragmented by persistent bifurcations—general relativity versus quantum mechanics, continuum versus discrete descriptions, the Heisenberg cut, and the status of the observer. These schisms impose concrete costs: collider, fusion, and quantum‑hardware programmes proceed without a shared observable that can bridge the frameworks underlying their design choices. This work asks whether a *master calibration*—a family of partial translation maps that composes consistently across all frameworks—can exist, and what combinatorial and error‑budget burden such a calibration imposes. Counting arguments applied to a 29‑schism inventory yield 406 unordered pairwise maps and 3654 independent composition constraints, a constraint‑to‑map ratio of exactly 9.0. A seven‑domain family admits only 21 unordered pairs, so at least eight schisms lie outside any pairwise reduction under a one‑schism‑per‑pair assumption. A three‑framework loop with edge errors $10^{-3}$, $2\times10^{-3}$, and $5\times10^{-4}$ gives a closure‑error bound of $3.4965\times10^{-3}$. A genericity projection with independent square‑constraint success probability $p=0.9$ yields a master‑calibration success probability of $6.34\times10^{-168}$ and a maximal family size of $n_{\max}=7$ at a 1% success threshold. A corrected correlation analysis replaces an earlier invalid linear model: Fréchet bounds show that positive correlation raises the joint success probability above the independent value while negative correlation drives it toward zero, so independence is neither a best‑ nor worst‑case assumption. The results separate structural schisms (no admissible translation within tolerance) from conventional ones (admissible but costly) and show that beyond small families global consistency must be enforced by construction rather than hoped for.

## 1. Introduction

Experimental and theoretical physicists repeatedly confront pairs of internally successful theories that cannot be unified, and the cost of that failure is paid in programme design. The European Particle Physics Strategy Update aggregates community proposals for collider projects and quantifies the scientific reach of a shared observable: at future $e^{+}e^{-}$ colliders the oblique parameters will be measured with a precision of $\sim1\%$, about a factor 10 better than the current precision, with $10^{12}$ $Z$ bosons available at circular colliders [1]. The design study for a next linear collider specifies a centre‑of‑mass energy window of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ in its abstract and $0.5$–$1.5\ \mathrm{TeV}$ in its preface [2]. In fusion energy, the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC) represent low‑density steady‑state and high‑density pulsed pathways whose magnetohydrodynamic stability assessments differ: for CFETR, active control methods may be required for resistive‑wall‑mode stabilization in 80% of steady‑state‑operation scenarios [4]. In quantum computing, the unresolved measurement problem and the Heisenberg cut separate quantum control from classical engineering, and divergent compositional versus holistic readings of quantum states impede error‑corrected processor design.

A systematic inventory of such fractures enumerates 29 distinct unresolved bifurcations, spanning topics from the nature of the continuum to the status of the observer, and argues that they are interconnected rather than isolated puzzles [10]. The same inventory records that quantum electrodynamics predicts the electron's magnetic moment to eleven decimal places while the cosmological constant is off by 120 orders of magnitude from naive expectations—precision and failure coexisting inside one edifice [10]. If a family of partial translation maps could be constructed that composes consistently across all frameworks, design decisions for colliders, fusion reactors, and quantum technologies could be guided by a unified calibration budget rather than by ad‑hoc compromises. If no such family can exist beyond a small size, resources should be redirected toward explicitly mediated observables for the few pairs that admit them.

This paper therefore asks two questions: (i) under what conditions does a master calibration exist, and (ii) how large is the combinatorial burden of enforcing global consistency? The analysis formalizes frameworks as calibrated theories over disjoint domains, defines translation maps with explicit error budgets, bounds composition failure by cycle‑closure error, and applies counting arguments to the 29‑schism inventory [10] and to a modeled seven‑domain family. This version corrects four errors identified in the published predecessor [9]: the pairwise‑capacity arithmetic of Derivation 2 (confirmed correct and retained), the falsifiability statement attached to the combinatorial bound (restated as model‑dependent), an inconsistent claim that a contraction‑mapping iteration bound agrees with the chain‑length bound (retracted and replaced by an explicit statement of the discrepancy), and an invalid linear correlation model whose "joint probability" exceeded unity (replaced by exact Fréchet bounds and a corrected independent value $0.9^{35}\approx0.02503$).

**Contributions.**
- **C1** – Formal definitions of framework, translation map, composition failure, and master calibration (Section 3).
- **C2** – Derivation of the pairwise‑map count $\binom{29}{2}=406$ and composition‑constraint count $\binom{29}{3}=3654$, with the exact constraint‑to‑map ratio $9.0$ (Section 4, Derivation 1).
- **C3** – Pairwise‑capacity result for a seven‑domain family: $\binom{7}{2}=21$ pairs against 29 schisms, so at least 8 schisms remain unassigned under the one‑schism‑per‑pair assumption (Section 4, Derivation 2).
- **C4** – Two‑framework corner: a pair of frameworks carries no composition constraint (Section 4, Derivation 2′).
- **C5** – Three‑framework closure bound $\Delta_{\gamma}\le3.4965\times10^{-3}$ for edge errors $10^{-3}$, $2\times10^{-3}$, and $5\times10^{-4}$ (Section 4, Derivation 3).
- **C6** – Structural‑versus‑conventional classification criterion, including the chain‑length bound $k\le\ln(1-\tau)/\ln(1-\varepsilon_{\min})\approx0.0995$ at $\tau=10^{-3}$, $\varepsilon_{\min}=10^{-2}$ (Section 4, Derivation 4).
- **C7** – Genericity projection $P_{\mathrm{master}}=p^{3654}=6.34\times10^{-168}$ at $p=0.9$, the threshold count $\binom{n}{3}\le43.71$, and the maximal family size $n_{\max}=7$ (Section 4, Derivation 5).
- **C8** – Corrected correlation analysis: the linear factor model is invalid at $m=35$ (it returns $3.38>1$); exact Fréchet bounds give $P(\text{all succeed})\in[\,0,\ 0.9\,]$, with the independent value $0.9^{35}\approx0.02503$ (Section 4, Derivation 5′).
- **C9** – Mediated‑translation price $1-(1-\varepsilon)^{2}=0.0199$ for $\varepsilon=10^{-2}$, and a worked two‑standard mediated example with $\Delta_{\mathrm{mediated}}=2.098\times10^{-2}$ (Section 4, Derivation 7; Section 6.1).
- **C10** – Sensitivity analysis of closure error under uniform scaling, $\Delta'_{\gamma}=1.7491\times10^{-3}$ at scaling factor $f=0.5$ (Section 4, Derivation 8).
- **C11** – Required per‑edge error $\varepsilon\le3.33\times10^{-4}$ for a three‑edge loop to meet tolerance $\tau=10^{-3}$ (Section 4, Derivation 9).
- **C12** – Falsifiability criteria: a three‑subsystem closure test whose outcome would refute the first‑order composition model, and the statement that an $n\ge10$ family with all commuting squares would contradict the model‑derived bound $n_{\max}=7$ (Section 6).

## 2. Background and Related Work

Calibration across non‑overlapping or weakly overlapping domains has been studied and demonstrated in engineering and machine‑learning contexts, and these works supply both the vocabulary and the performance baselines used below.

The European Particle Physics Strategy Update process takes a bottom‑up approach in which the community is first invited to submit proposals for projects to be realised in the near‑, mid‑ and longer‑term future [1]. Its precision‑physics section reports that at future $e^{+}e^{-}$ colliders the oblique parameters will be measured with a precision of $\sim1\%$, about a factor 10 better than the current precision, and that $10^{12}$ $Z$ bosons would be available at circular colliders [1]. This is an instance of a shared observable—electroweak precision parameters—acting as a calibration target across otherwise separate experimental programmes, and it fixes the $\sim1\%$ scale used as a benchmark precision in Section 4.

The next linear collider report presents the current expectations for the design and physics programme of an $e^{+}e^{-}$ linear collider of centre‑of‑mass energy 500 GeV–1 TeV [2]; its preface states the design range as 0.5–1.5 TeV [2]. The two stated ranges differ by a factor of 1.5 at the upper end, and Section 4 uses both to derive energy‑window factors as an example of how a single design document can carry two internally consistent but non‑identical specifications that a calibration programme must reconcile.

Road‑marking mediated calibration enables targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap, by exploiting static road markings as features [3]. The method reports positional accuracy of approximately $0.02\ \mathrm{m}$ and angular accuracy of $0.086^{\circ}$ without manual operation by a human operator [3]. The same work flags a fragile auxiliary assumption: it used the assumption that the odometry generating the point cloud is locally accurate, and notes that under repeated accelerations and decelerations the 3D map may be distorted by motion‑estimation errors, preferring formulations that fold odometry uncertainty into the optimization [3]. This is a concrete example of a conventional schism that becomes structural when an auxiliary capability fails, and it motivates the mediated‑domain construction of Section 3.4.

In fusion energy, the MHD analysis of CFETR and HFRC assesses the two design pathways' stability. For CFETR, the work predicts the ECCD power and current required for full stabilization of neoclassical tearing modes, performs a thorough investigation of resistive‑wall‑mode stability, and finds that for 80% of the steady‑state‑operation scenarios active control methods may be required for RWM stabilization [4]. The simulations use parameters such as a Lundquist number $S=5.56\times10^{6}$ and a local bootstrap current fraction $j_{b}/j_{p}=0.3$ at the resonant surface [4]. This is a case where two fusion pathways rely on different stability assessments—precisely the kind of framework‑pair a translation map with an error budget would have to cover.

In machine learning, the connection between calibration and out‑of‑domain generalization is made precise by a definition of multi‑environment calibration: a classifier $f$ is calibrated on a set of environments $E_{\mathrm{train}}$ if for every environment $e_{i}$ and every value $\alpha$ in the range of $f$ restricted to $e_{i}$, $\mathbb{E}\left[Y\mid f(X)=\alpha,E=e_{i}\right]=\alpha$ [5]. That work proves in a linear‑Gaussian setting that models calibrated on multiple domains are free of spurious correlations and therefore generalize out of domain, and it proposes optimizing calibration through the Expected Calibration Error (ECE), the average deviation between model accuracy and model confidence [5]. Section 6.3 uses this definition to construct a machine‑learning analogue of the three‑framework closure computation.

Calibration precision is currently a limiting systematic in 21 cm cosmology experiments: the cosmological signal is contaminated by astrophysical foreground emission that is 4–5 orders of magnitude brighter, so separating the signals requires extremely precise instrumental calibration [6]. The field's approaches divide into 'sky‑based' calibration, relying on an extremely accurate model of astronomical foreground emission, and 'redundant' calibration, requiring a precisely regular array with near‑identical antenna response patterns; each class rests on strong assumptions that the other avoids [6]. This supplies the paper's motivating error floor: a domain in which the calibration systematic is the limiting uncertainty justifies treating $10^{-2}$‑scale per‑edge errors as realistic in unfavorable cases.

Post‑hoc uncertainty calibration under domain drift shows what happens when a translation is used outside its calibrated range. That work evaluates post‑hoc calibration methods across 28 distinct perturbation types not seen during training, computing the micro‑averaged ECE at 10 perturbation levels per sample [7]. Its central finding is that while excellent in‑domain calibration can be achieved with standard baselines, the quality of uncertainty decreases with increasing domain shift for all methods, resulting in highly overconfident predictions for images far from the training domain, and that replacing the validation set by a transformed validation set sampled along drift directions substantially improves calibration under shift [7]. Section 3.2 imports this as the restriction of translation maps to calibrated overlaps: a map used outside its overlap exhibits the same monotone degradation.

In radio‑frequency metrology, the thru‑free multiline calibration modifies traditional multiline TRL calibration for vector network analyzers by eliminating the need for a thru (or line) standard, using an arbitrary transmissive two‑port device together with a reflect standard [8]. The method's verification collected 25 frequency sweeps per standard at an IF‑bandwidth of $100\ \mathrm{Hz}$ over $1$–$150\ \mathrm{GHz}$ with 299 frequency points, and observed excellent agreement between the proposed method and multiline TRL when a thru standard was used to set the reference plane [8]. This demonstrates that a calibration standard previously thought definitional—the thru—can be eliminated by reformulating the eigenvalue problem, an existence proof that a seemingly structural dependency can be conventional.

The predecessor of this paper [9] introduced the definitions of framework, translation map, composition failure, and master calibration used here, the mediated‑domain construction, and the derivations on pairwise capacity and energy‑window factors that Section 4 carries forward with corrections [9]. The 29‑schism inventory [10] supplies the counting basis: it enumerates 29 unresolved bifurcations and hidden assumptions, from the nature of the continuum to the status of the observer, and argues they are facets of a single assumption—that physics can be formulated from a perspective no physical agent can occupy [10]. Its Bootstrap Theorem states that if the distinction function $d$ is an ultrametric on the proposition space, the calibration operator $\Phi$ is a contraction mapping on the space of theories, so by the Banach fixed‑point theorem a unique fixed point $T^{*}=\Phi(T^{*})$ exists [10]. Section 6.2 examines what that contraction picture does and does not imply for the error bounds derived here.

## 3. Methods

### 3.1 Frameworks and domains

**Definition 3.1 (Framework).** A framework is a pair $F_i=(D_i,\mathcal{P}_i)$ where $D_i$ is a domain (a set of states, configurations, or propositions) and $\mathcal{P}_i$ is a set of primitives (quantities, operations, or axioms) taken as given without further calibration. *Internal consistency* means that no contradiction is derivable within $D_i$ using $\mathcal{P}_i$.

*Examples.* $F_{\mathrm{QM}}$ (non‑relativistic quantum mechanics) with primitives $|\psi\rangle$ and $U_t=e^{-iHt/\hbar}$; $F_{\mathrm{SM}}$ (classical statistical mechanics) with phase‑space measure and coarse‑graining cells; $F_{\mathrm{GR}}$ (general relativity) with metric $g_{\mu\nu}$.

### 3.2 Translation maps and error

**Definition 3.2 (Translation map).** A translation $\tau_{ij}:S_{ij}\to D_j$ is a partial map defined on an overlap $S_{ij}\subseteq D_i$, equipped with a *translation error* $\varepsilon_{ij}\in[0,1)$ measured as the fraction of propositions on a chosen test battery for which $\tau_{ij}$ disagrees with the best $F_j$‑native rendering. Directionality is allowed: $\varepsilon_{ij}\neq\varepsilon_{ji}$.

The restriction to $S_{ij}$ is essential. In domain‑drift scenarios calibration quality degrades monotonically with shift magnitude: post‑hoc methods that are excellent in‑domain produce highly overconfident predictions far from the training domain, across all 28 perturbation types tested [7]. A translation map used outside its calibrated overlap exhibits the same failure mode.

### 3.3 Composition and closure

For composable translations $\tau_{ij}$ and $\tau_{jk}$, the composed error obeys the first‑order bound

$$\varepsilon_{ij\circ jk}\le\varepsilon_{ij}+\varepsilon_{jk}+\varepsilon_{ij}\,\varepsilon_{jk}.$$

**Definition 3.3 (Composition failure).** Failure occurs if there exists $x\in\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$ such that $(\tau_{jk}\circ\tau_{ij})(x)\neq\tau_{ik}(x)$.

For a cycle $\gamma$ with edges $e\in\gamma$ and errors $\varepsilon_e$, the *closure error* satisfies

$$\Delta_{\gamma}\le 1-\prod_{e\in\gamma}(1-\varepsilon_e).$$

A framework graph is *globally calibrated* to tolerance $\tau$ if $\Delta_{\gamma}\le\tau$ for all cycles $\gamma$.

**Definition 3.4 (Master calibration).** A family $\mathcal{T}=\{\tau_{ij}\}_{i<j}$ is a master calibration if every square commutes: $\tau_{jk}\circ\tau_{ij}=\tau_{ik}$ on $\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$.

### 3.4 Mediating domains

Following the engineering strategy exemplified by road‑marking mediation [3] and by the thru‑free elimination of a definitional standard in VNA calibration [8], introduce a mediating domain $M$ with translations $\tau_{iM}:S_{iM}\to M$ and $\tau_{Mj}:M\supset\tau_{iM}(S_{iM})\to D_j$. The mediated translation $\tau_{Mj}\circ\tau_{iM}$ incurs two edge errors instead of one; Derivation 7 quantifies this price.

### 3.5 Structural versus conventional schisms

**Definition 3.5.** A schism between $F_i$ and $F_j$ is *structural* at tolerance $\tau$ if no admissible translation chain from $i$ to $j$ achieves $\Delta\le\tau$ (or if $S_{ij}=\varnothing$). It is *conventional* if such a chain exists but is costly—for example, long, or requiring strong auxiliary assumptions such as the extremely accurate foreground model of sky‑based calibration in 21 cm cosmology [6] or the locally accurate odometry assumed in road‑marking calibration [3]. The thru‑free multiline result shows that a dependency that appears definitional (the thru standard) can be removed by reformulation [8], which is the operational signature of a conventional rather than structural obstruction.

### 3.6 Method summary

The method is analytical: Definitions 3.1–3.5 are stated, and Sections 4–6 derive consequences by (i) combinatorial counting over the schism inventory of [10], (ii) exact evaluation of the closure‑error bound of Section 3.3 for stated edge errors, and (iii) a probabilistic projection under an explicitly assumed independence model, together with exact Fréchet bounds for the correlated case. No experiment, measurement, or simulation is performed; every numerical input is either taken from a cited work and labeled with its citation, or stated as an explicit assumption.

## 4. Analysis

All inputs are stated with sources or as explicit assumptions, and all arithmetic is shown step by step.

**Input 1 (from [10]):** number of unresolved bifurcations $N_{\mathrm{schism}}=29$.

**Input 2 (assumption):** candidate family size $n=7$ research domains.

**Input 3 (assumption):** a two‑ontology bifurcation partitions one domain into $m=2$ frameworks.

**Input 4 (from [2]):** linear‑collider centre‑of‑mass energy range $E_{\mathrm{cm}}=500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ (abstract) and $0.5$–$1.5\ \mathrm{TeV}$ (preface).

**Input 5 (from [6]):** calibration precision is a limiting systematic in 21 cm cosmology; foregrounds are 4–5 orders of magnitude ($10^{4}$–$10^{5}$) brighter than the signal, motivating a non‑zero error floor.

**Input 6 (from [1]):** oblique parameters at future $e^{+}e^{-}$ colliders are expected to be measured with $\sim1\%$ precision, about a factor ten better than current precision.

**Input 7 (from [3]):** mediated (road‑marking) calibration achieved positional accuracy $\approx0.02\ \mathrm{m}$ and angular accuracy $\approx0.086^{\circ}$.

**Input 8 (assumption):** genericity model—each independent square constraint succeeds with probability $p=0.9$, independently of all others.

**Input 9 (assumption):** tolerance $\tau=10^{-3}$ and minimum per‑edge error $\varepsilon_{\min}=10^{-2}$ where used.

### Derivation 1: counting maps and composition constraints

Treat the 29 bifurcations as 29 frameworks.

Unordered pairwise translation maps:

$$\binom{29}{2}=\frac{29\times28}{2}=\frac{812}{2}=406.$$

Unordered triples (each yielding one independent square constraint):

$$\binom{29}{3}=\frac{29\times28\times27}{6}=\frac{21924}{6}=3654.$$

Constraint‑to‑map ratio:

$$\frac{3654}{406}=9.0,$$

exact because

$$\frac{\binom{N}{3}}{\binom{N}{2}}=\frac{N-2}{3}=\frac{27}{3}=9.$$

*Factor‑2 reading.* If each bifurcation is counted as two opposite‑direction frameworks ($N=58$), then

$$\binom{58}{2}=\frac{58\times57}{2}=1653,\qquad \binom{58}{3}=\frac{58\times57\times56}{6}=30856,$$

and the ratio becomes $\frac{30856}{1653}=\frac{56}{3}\approx18.667$.

### Derivation 2: pairwise capacity for the seven‑domain family

Unordered pairs for $n=7$:

$$P=\binom{7}{2}=\frac{7\times6}{2}=21.$$

Assuming *one‑schism‑per‑pair*, each of the 29 bifurcations must be assigned a distinct unordered pair. Since $29>21$, at most 21 bifurcations can be assigned, leaving

$$29-21=8$$

unassigned. Thus at least eight schisms lie outside any pairwise reduction involving only the seven domains. This arithmetic is confirmed and stands as stated.

### Derivation 2′: two‑framework corner

For $m=2$ frameworks:

$$\binom{2}{2}=1,\qquad \binom{2}{3}=0.$$

Hence a pair of frameworks carries no composition constraint; any single translation map trivially satisfies the master‑calibration condition for that pair. Two‑framework calibration problems—such as the camera–LiDAR pair of [3] or the CFETR–HFRC stability comparison [4]—are therefore structurally easier than any problem involving three or more frameworks.

### Derivation 3: closure‑error budget for a three‑framework loop

Edge errors: $\varepsilon_{12}=10^{-3}$, $\varepsilon_{23}=2\times10^{-3}$, $\varepsilon_{31}=5\times10^{-4}$.

Compute

$$1-\varepsilon_{12}=0.999,\quad 1-\varepsilon_{23}=0.998,\quad 1-\varepsilon