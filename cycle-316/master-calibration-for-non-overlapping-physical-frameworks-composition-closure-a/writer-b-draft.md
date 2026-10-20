# Master Calibration for Non‑Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation (Revised Edition, v3.0.0)

## Abstract

Physics is fragmented by persistent bifurcations—general relativity versus quantum mechanics, continuum versus discrete descriptions, the Heisenberg cut, and the status of the observer. These schisms impose concrete costs: collider, fusion, and quantum‑hardware programmes proceed without a shared observable that can bridge the frameworks underlying their design choices. What is missing is an account of whether a *master calibration*—a family of partial translation maps that composes consistently across all frameworks—can exist at all, and what combinatorial and error‑budget burden such a calibration imposes. This paper formalizes frameworks as internally consistent theories over disjoint domains, defines translation maps with explicit error budgets, and derives consequences by counting and by cycle‑closure bounds. A 29‑schism inventory yields $\binom{29}{2}=406$ unordered pairwise maps and $\binom{29}{3}=3654$ independent composition constraints, an exact constraint‑to‑map ratio of $9.0$. A seven‑domain family admits only $\binom{7}{2}=21$ unordered pairs, so at least $29-21=8$ schisms lie outside any pairwise reduction under a one‑schism‑per‑pair assumption. A three‑framework loop with edge errors $10^{-3}$, $2\times10^{-3}$, and $5\times10^{-4}$ gives a closure‑error bound of $3.4965\times10^{-3}$. A genericity projection with independent square‑constraint success probability $p=0.9$ yields a master‑calibration success probability of $6.34\times10^{-168}$ and a maximal family size of $n_{\max}=7$ at a $1\%$ success threshold. The results separate structural schisms (no admissible translation within tolerance) from conventional ones (admissible but costly) and show that beyond small families global consistency must be enforced by construction rather than hoped for.

## 1. Introduction

Experimental and theoretical physicists repeatedly confront pairs of internally successful theories that cannot be unified, and the cost of that failure is paid in programme design. The European Particle Physics Strategy Update aggregates community proposals for collider projects and quantifies the scientific reach of a shared observable: at future $e^{+}e^{-}$ colliders the oblique parameters will be measured with a precision of $\sim1\%$, about a factor ten better than the current precision [1]. The design study for a next linear collider specifies a centre‑of‑mass energy window of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ in its abstract and $0.5$–$1.5\ \mathrm{TeV}$ in its preface, and argues that the missing agent behind electroweak symmetry breaking "must provide new physical phenomena at the TeV energy scale" [2]. In fusion energy, the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC) represent low‑density steady‑state and high‑density pulsed pathways whose magnetohydrodynamic stability assessments differ: for CFETR, active control methods may be required for resistive‑wall‑mode stabilization in $80\%$ of steady‑state‑operation scenarios [4]. In quantum computing, the unresolved measurement problem and the Heisenberg cut separate quantum control from classical engineering, and divergent compositional versus holistic readings of quantum states impede error‑corrected processor design.

A systematic inventory of such fractures enumerates 29 distinct unresolved bifurcations, spanning topics from the nature of the continuum to the status of the observer, and argues that they are interconnected rather than isolated puzzles [10]. The same inventory notes the scale of the stakes: quantum electrodynamics predicts the electron's magnetic moment to eleven decimal places while the cosmological constant disagrees with naive expectations by $120$ orders of magnitude, so individual frameworks can be spectacularly accurate inside their domains while remaining mutually uncalibrated [10]. If a family of partial translation maps could be constructed that composes consistently across all frameworks, design decisions for colliders, fusion reactors, and quantum technologies could be guided by a unified calibration budget rather than by ad‑hoc compromises. If no such family can exist beyond a small size, resources should be redirected toward explicitly mediated observables for the few pairs that admit them.

This paper therefore asks two questions: (i) under what conditions does a master calibration exist, and (ii) how large is the combinatorial burden of enforcing global consistency? The analysis formalizes frameworks as calibrated theories over disjoint domains, defines translation maps with explicit error budgets, bounds composition failure by cycle‑closure error, and applies counting arguments to the 29‑schism inventory [10] and to a modeled seven‑domain family. The method is analytical throughout: no experiment, measurement, or simulation is performed, and every numerical input is either taken from a cited work or stated as an explicit assumption.

**Contributions.**
- **C1** – Formal definitions of framework, translation map, composition failure, and master calibration (Section 3).
- **C2** – Derivation of the pairwise‑map count $\binom{29}{2}=406$ and composition‑constraint count $\binom{29}{3}=3654$, with the exact constraint‑to‑map ratio $9.0$ (Section 4, Derivation 1).
- **C3** – Pairwise‑capacity result for a seven‑domain family: $\binom{7}{2}=21$ pairs against $29$ schisms, so at least $8$ schisms remain unassigned under the one‑schism‑per‑pair assumption (Section 4, Derivation 2).
- **C4** – Two‑framework corner for the Feynman–Shor bifurcation: a pair of frameworks carries no composition constraint (Section 4, Derivation 2′).
- **C5** – Three‑framework closure bound $\Delta_{\gamma}\le3.4965\times10^{-3}$ for edge errors $10^{-3}$, $2\times10^{-3}$, $5\times10^{-4}$ (Section 4, Derivation 3).
- **C6** – Structural‑versus‑conventional classification criterion, including the chain‑length bound $k\le\ln(1-\tau)/\ln(1-\varepsilon_{\min})$ (Section 3.5 and Section 4, Derivation 4).
- **C7** – Genericity projection $P_{\mathrm{master}}=p^{3654}=6.34\times10^{-168}$ at $p=0.9$, the threshold count $\binom{n}{3}\le43.7$, and the maximal family size $n_{\max}=7$ (Section 4, Derivation 5).
- **C8** – Energy‑window factors $2$ (abstract) and $3$ (preface) for the linear‑collider design ranges, and mean schisms per domain $29/7\approx4.14$ under a uniformity assumption (Section 4, Derivation 6).
- **C9** – Mediated‑translation price $1-(1-\varepsilon)^{2}=0.0199$ for $\varepsilon=10^{-2}$ (Section 4, Derivation 7).
- **C10** – Sensitivity analysis of closure error under uniform scaling of edge errors, $\Delta'_{\gamma}=1.7491\times10^{-3}$ at scaling factor $f=0.5$ (Section 4, Derivation 8).
- **C11** – Required per‑edge error $\varepsilon\le3.33\times10^{-4}$ for a three‑edge loop to meet tolerance $\tau=10^{-3}$ (Section 4, Derivation 9).
- **C12** – A falsifiability criterion: a proposed three‑subsystem closure test whose outcome would refute the first‑order composition model, and the statement that an $n\ge10$ family with commuting squares would contradict the combinatorial bound $n_{\max}=7$ (Sections 6.1 and 4, Derivation 5).

## 2. Background and Related Work

Calibration across non‑overlapping domains has been studied and demonstrated in several engineering and scientific contexts, and these works supply both the vocabulary and the performance baselines used below.

The European Particle Physics Strategy Update takes a bottom‑up approach in which the community submits proposals for projects to be realised in the near‑, mid‑ and longer‑term future, and it identifies a rich programme of precision measurements of the Higgs boson and of electroweak observables; in particular it states that at future $e^{+}e^{-}$ colliders the oblique parameters will be measured with a precision of $\sim1\%$, about a factor ten better than current precision [1]. This figure is used here as a concrete instance of what a shared, precisely calibrated observable buys across otherwise separate experimental programmes.

The next linear collider report presents the design and physics programme of an $e^{+}e^{-}$ linear collider of centre‑of‑mass energy $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ in its abstract, while its preface summarizes the design basis for a machine of $0.5$–$1.5\ \mathrm{TeV}$; the report further argues that the agent breaking electroweak symmetry must provide new phenomena at the TeV scale [2]. The two stated energy windows supply the numerical inputs for the energy‑window factors computed in Derivation 6, and the report's account of the Stanford Linear Collider—built to study the $100$‑GeV scale and to develop the accelerator physics needed for future colliders—illustrates how a single facility can mediate between an existing framework and a planned one.

Road‑marking mediated calibration enables targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap; the method exploits static road markings and reports extrinsic parameters accurate to approximately $0.02\ \mathrm{m}$ and $0.086^{\circ}$ without manual operation by a human operator [3]. The same work flags a fragile auxiliary assumption: it used the assumption that the odometry generating the point cloud is locally accurate, and notes that vehicle accelerations and decelerations can distort the 3D map through motion‑estimation errors. This is a direct engineering instance of a mediated calibration whose validity rests on an auxiliary capability—precisely the failure mode that Definition 3.5 classifies as a conventional rather than structural schism.

Thru‑free multiline calibration eliminates the need for a thru standard in vector‑network‑analyzer calibration by using an arbitrary transmissive two‑port device together with an additional reflect standard; the authors observe excellent agreement between the proposed method and traditional multiline TRL when a thru standard is available, and note that in the thru‑free method all calibration standards become partially defined [8]. This exemplifies the construction of a calibration family from weaker or partially defined standards, which is the engineering analogue of building translation maps on overlaps $S_{ij}$ rather than on whole domains.

In 21 cm cosmology, calibration precision is identified as a limiting systematic: astrophysical foreground emission is $4$–$5$ orders of magnitude brighter than the cosmological signal, so separating the two requires extremely precise instrumental calibration [6]. The work categorizes calibration as sky‑based (relying on an extremely accurate foreground model) or redundant (requiring a precisely regular array), shows by simulation that a unified approach combining redundant calibration with a sky‑model prior can improve performance, and catalogues the strong assumptions each paradigm makes. This motivates the non‑zero error floor $\varepsilon_{\min}$ used in Derivations 4 and 9 and illustrates how a conventional schism can be opened by the cost of an auxiliary model.

Multi‑environment calibration in machine learning defines calibration across environments by $\mathbb{E}[Y\mid f(X)=\alpha, E=e_i]=\alpha$ for every environment $e_i$ and $\alpha$ in the range of $f$, and proves in a linear setting that models calibrated on multiple domains are free of spurious correlations and therefore generalize out of domain [5]. The work also proposes a training objective that directly penalizes multi‑domain calibration error. This provides a formal precedent for requiring a calibration property to hold over a family of domains simultaneously—the logical structure of the master‑calibration condition of Definition 3.4.

Domain‑drift calibration evaluation quantifies calibration under $28$ distinct perturbation types not seen during training, at $10$ perturbation levels each, and shows that while excellent in‑domain calibration can be achieved with standard post‑hoc baselines, the quality of uncertainty decreases with increasing domain shift, resulting in highly overconfident predictions far from the training domain; replacing the validation set by a transformed validation set substantially improves calibration under drift [7]. This motivates the restriction of translation maps to calibrated overlap regions $S_{ij}$ in Definition 3.2: a translation used outside its calibrated overlap exhibits exactly this overconfidence failure.

CFETR and HFRC illustrate a second domain‑specific calibration problem: magnetohydrodynamic simulations for CFETR take the Lundquist number $S=5.56\times10^{6}$ at a $q=2$ surface with $r_{s}=0.51a$, predict the electron‑cyclotron current drive power required for full neoclassical‑tearing‑mode stabilization, and find that for $80\%$ of steady‑state‑operation scenarios active control methods may be required for resistive‑wall‑mode stabilization [4]. Different fusion pathways thus demand different mediating observables and control systems, a concrete case of framework‑specific calibration burdens.

The inventory of unresolved bifurcations enumerates 29 distinct schisms—from the nature of the continuum to the status of the observer—and develops a self‑referential calibration framework in which a calibration operator $\Phi$ on the space of theories is shown, under an ultrametric distinction function, to be a contraction mapping possessing a unique fixed point by the Banach fixed‑point theorem [10]. That global‑existence claim rests on strong geometric assumptions (ultrametricity of the distinction space, via an Ostrowski‑type argument); the present work deliberately adopts a local, assumption‑light counting and error‑budget analysis so that its conclusions do not depend on those geometric premises.

Finally, the published predecessor of this paper states the definitions of framework, translation map, and mediating domain used here, and reports the derivations that this revision re‑checks and corrects—notably the pairwise‑capacity result that $29>21$ leaves at least $29-21=8$ schisms outside any pairwise reduction among seven domains, and the energy‑window factors $2$ and $3$ [9]. The present version strengthens those derivations, corrects an arithmetic slip in the sensitivity analysis (Derivation 8), and supplies the previously missing computation behind the four‑edge chain result R4.

## 3. Methods

### 3.1 Frameworks and domains

**Definition 3.1 (Framework).** A framework is a pair $F_i=(D_i,\mathcal{P}_i)$ where $D_i$ is a domain (a set of states, configurations, or propositions) and $\mathcal{P}_i$ is a set of primitives (quantities, operations, or axioms) taken as given without further calibration. *Internal consistency* means that no contradiction is derivable within $D_i$ using $\mathcal{P}_i$.

*Examples.* $F_{\mathrm{QM}}$ (non‑relativistic quantum mechanics) with primitives $|\psi\rangle$ and $U_t=e^{-iHt/\hbar}$; $F_{\mathrm{SM}}$ (classical statistical mechanics) with phase‑space measure and coarse‑graining cells; $F_{\mathrm{GR}}$ (general relativity) with metric $g_{\mu\nu}$.

### 3.2 Translation maps and error

**Definition 3.2 (Translation map).** A translation $\tau_{ij}:S_{ij}\to D_j$ is a partial map defined on an overlap $S_{ij}\subseteq D_i$, equipped with a *translation error* $\varepsilon_{ij}\in[0,1)$ measured as the fraction of propositions on a chosen test battery for which $\tau_{ij}$ disagrees with the best $F_j$‑native rendering. Directionality is allowed: $\varepsilon_{ij}\neq\varepsilon_{ji}$.

The restriction to $S_{ij}$ is essential: in domain‑drift scenarios calibration quality degrades with shift magnitude and predictions become overconfident far from the training domain, and a translation map used outside its calibrated overlap exhibits the same failure mode [7].

### 3.3 Composition and closure

For composable translations $\tau_{ij}$ and $\tau_{jk}$, the composed error obeys the first‑order bound

$$\varepsilon_{ij\circ jk}\le\varepsilon_{ij}+\varepsilon_{jk}+\varepsilon_{ij}\,\varepsilon_{jk}.$$

**Definition 3.3 (Composition failure).** Failure occurs if there exists $x\in\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$ such that $(\tau_{jk}\circ\tau_{ij})(x)\neq\tau_{ik}(x)$.

For a cycle $\gamma$ with edges $e\in\gamma$ and errors $\varepsilon_e$, the *closure error* satisfies

$$\Delta_{\gamma}\le 1-\prod_{e\in\gamma}(1-\varepsilon_e).$$

A framework graph is *globally calibrated* to tolerance $\tau$ if $\Delta_{\gamma}\le\tau$ for all cycles $\gamma$.

**Definition 3.4 (Master calibration).** A family $\mathcal{T}=\{\tau_{ij}\}_{i<j}$ is a master calibration if every square commutes: $\tau_{jk}\circ\tau_{ij}=\tau_{ik}$ on $\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$.

### 3.4 Mediating domains

Following the engineering strategies exemplified by road‑marking mediation [3] and thru‑free multiline calibration [8], introduce a mediating domain $M$ with translations $\tau_{iM}:S_{iM}\to M$ and $\tau_{Mj}:M\supset\tau_{iM}(S_{iM})\to D_j$. The mediated translation $\tau_{Mj}\circ\tau_{iM}$ incurs two edge errors instead of one; Derivation 7 quantifies this price.

### 3.5 Structural versus conventional schisms

**Definition 3.5.** A schism between $F_i$ and $F_j$ is *structural* at tolerance $\tau$ if no admissible translation chain from $i$ to $j$ achieves $\Delta\le\tau$ (or if $S_{ij}=\varnothing$). It is *conventional* if such a chain exists but is costly—for example, long, or requiring strong auxiliary assumptions such as the extremely accurate foreground model needed in 21 cm cosmology [6] or the locally accurate odometry assumed in road‑marking calibration [3].

### 3.6 Method summary

The method is analytical: Definitions 3.1–3.5 are stated, and Sections 4 and 5 derive consequences by (i) combinatorial counting over the schism inventory of [10], (ii) exact evaluation of the closure‑error bound of Section 3.3 for stated edge errors, and (iii) a probabilistic projection under an explicitly assumed independence model. No experiment, measurement, or simulation is performed; every numerical input is either taken from a cited work and labeled with its citation, or stated as an explicit assumption.

## 4. Analysis

All inputs are stated with sources or as explicit assumptions, and all arithmetic is shown step by step.

**Input 1 (from [10]):** number of unresolved bifurcations $N_{\mathrm{schism}}=29$.

**Input 2 (assumption):** candidate family size $n=7$ research domains.

**Input 3 (assumption):** the Feynman–Shor bifurcation partitions quantum computing into $m=2$ ontologies.

**Input 4 (from [2]):** linear‑collider centre‑of‑mass energy range $E_{\mathrm{cm}}=500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ (abstract) and $0.5$–$1.5\ \mathrm{TeV}$ (preface).

**Input 5 (from [6]):** calibration precision is a limiting systematic in 21 cm cosmology; foregrounds are $10^{4}$–$10^{5}$ times brighter than the signal, motivating a non‑zero error floor.

**Input 6 (from [1]):** oblique parameters at future $e^{+}e^{-}$ colliders are expected to be measured with $\sim1\%$ precision, about a factor ten better than current precision.

**Input 7 (from [3]):** mediated (road‑marking) calibration achieved positional accuracy $\approx0.02\ \mathrm{m}$ and angular accuracy $\approx0.086^{\circ}$.

**Input 8 (assumption):** genericity model—each independent square constraint succeeds with probability $p=0.9$, independently of all others.

**Input 9 (assumption):** tolerance $\tau=10^{-3}$ and minimum per‑edge error $\varepsilon_{\min}=10^{-2}$ where used.

### Derivation 1: counting maps and composition constraints

Treat the 29 bifurcations as 29 frameworks. Unordered pairwise translation maps:

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

Assuming *one‑schism‑per‑pair*, each of the $29$ bifurcations must be assigned a distinct unordered pair. Since $29>21$, at most $21$ bifurcations can be assigned, leaving

$$29-21=8$$

unassigned. Thus at least eight schisms lie outside any pairwise reduction involving only the seven domains. This result is independent of which seven domains are chosen: it depends only on the counts $29$ and $7$.

### Derivation 2′: two‑framework corner (Feynman–Shor)

For $m=2$ ontologies:

$$\binom{2}{2}=1,\qquad \binom{2}{3}=0.$$

Hence a pair of frameworks carries no composition constraint; any single translation map trivially satisfies the master‑calibration condition for that pair. Two‑framework schisms are therefore never structural *by virtue of composition*—they can only be structural through the error budget (Derivation 4) or through an empty overlap $S_{ij}=\varnothing$.

### Derivation 3: closure‑error budget for a three‑framework loop

Edge errors: $\varepsilon_{12}=10^{-3}$, $\varepsilon_{23}=2\times10^{-3}$, $\varepsilon_{31}=5\times10^{-4}$.

Compute

$$1-\varepsilon_{12}=0.999,\quad 1-\varepsilon_{23}=0.998,\quad 1-\varepsilon_{31}=0.9995.$$

Product:

$$0.999\times0.998=0.997002,$$
$$0.997002\times0.9995=0.997002-0.997002\times0.0005=0.997002-0.000498501=0.996503499.$$

Closure bound:

$$\Delta_{\gamma}\le1-0.996503499=0.003496501\approx3.4965\times10^{-3}.$$

### Derivation 4: chain‑length bound for structural versus conventional classification

Given a minimum edge error $\varepsilon_{\min}=10^{-2}$ and tolerance $\tau$, a chain of $k$ edges yields

$$\Delta=1-(1-\varepsilon_{\min})^{k}.$$

Solving $\Delta\le\tau$ for $k$ gives

$$k\le\frac{\ln(1-\tau)}{\ln(1-\varepsilon_{\min})}.$$

For $\tau=10^{-3}$ and $\varepsilon_{\min}=10^{-2}$,

$$k\le\frac{\ln(0.999)}{\ln(0.99)}\approx\frac{-0.0010005}{-0.0100503}\approx0.0995,$$

so even a single edge already exceeds the tolerance; any longer chain is structural at this tolerance. As a projection for a looser tolerance, a chain of $k=4$ edges with $\varepsilon_{\min}=10^{-2}$ gives

$$(1-0.01)^{4}=0.99^{4}=0.96059601,$$
$$\Delta=1-0.96059601=0.03940399\approx3.94\times10^{-2},$$

which is the computation behind Result R4; it assumes the four edge errors are independent and equal.

### Derivation 5: genericity projection

Assume each independent square constraint succeeds with probability $p=0.9$ and that successes are independent (Input 8). The probability that *all* $3654$ constraints succeed is

$$P_{\mathrm{master}}=p^{3654}=0.9^{3654}.$$

Compute the exponent: $\ln(0.9)=-0.1053605$, so $\ln P_{\mathrm{master}}=3654\times(-0.1053605)=-384.987$. Converting to base 10: $-384.987/2.302585=-167.19$, hence

$$P_{\mathrm{master}}=10^{-167.19}\approx6.34\times10^{-168}.$$

For a family of size $n$, the number of independent constraints is $\binom{n}{3}$. Requiring $P_{\mathrm{master}}\ge0.01$ gives

$$0.9^{\binom{n}{3}}\ge0.01\;\Longrightarrow\;\binom{n}{3}\le\frac{\ln(0.01)}{\ln(0.9)}=\frac{-4.605170}{-0.1053605}\approx43.71.$$

The largest integer $n$ satisfying $\binom{n}{3}\le43.71$ is $n_{\max}=7$, since $\binom{7}{3}=35\le43.71$ while $\binom{8}{3}=56>43.71$. An $n\ge10$ family with all squares commuting would require $\binom{10}{3}=120$ simultaneous successes, which under the independence model has probability $0.9^{120}\approx3.2\times10^{-6}$—demonstrated success at that size would contradict the combinatorial bound that random families succeed only up to $n_{\max}=7$, and would indicate that real translation maps are strongly correlated rather than independent.

### Derivation 6: energy‑window factors and mean schisms per domain

From Input 4, the abstract energy window is

$$\frac{1\ \mathrm{TeV}}{0.5\ \mathrm{TeV}}=2.$$

The preface window is

$$\frac{1.5\ \mathrm{TeV}}{0.5\ \mathrm{TeV}}=3.$$

Mean schisms per domain under a uniform distribution:

$$\frac{N_{\mathrm{schism}}}{n}=\frac{29}{7}=4.142857\approx4.14.$$

### Derivation 7: price of mediated translation

A mediated translation replaces a direct edge of error $\varepsilon$ by two edges each of error $\varepsilon$. The effective error becomes

$$\Delta_{\text{mediated}}=1-(1-\varepsilon)^{2}=1-(1-2\varepsilon+\varepsilon^{2})=2\varepsilon-\varepsilon^{2}.$$

For $\varepsilon=10^{-2}$,

$$\Delta_{\text{mediated}}=2\times10^{-2}-(10^{-2})^{2}=0.02-0.0001=0.0199.$$

The mediated link therefore costs an additional $9.9\times10^{-3}$ of error budget relative to the direct edge.

### Derivation 8: sensitivity of closure error to uniform scaling

Scale all edge errors of Derivation 3 by factor $f$. The original product is $P=0.996503499$. The scaled product is

$$P'(f)=(1-f\varepsilon_{12})(1-f\varepsilon_{23})(1-f\varepsilon_{31}).$$

For $f=0.5$:

$$1-0.5\varepsilon_{12}=0.9995,\quad 1-0.5\varepsilon_{23}=0.999,\quad 1-0.5\varepsilon_{31}=0.99975.$$

Product:

$$0.9995\times0.999=0.9985005,$$
$$0.9985005\times0.99975=0.9985005-0.9985005\times0.00025=0.9985005-0.0002496251=0.9982508749.$$

Closure bound:

$$\Delta'_{\gamma}=1-0.9982508749=0.0017491251\approx1.7491\times10^{-3}.$$

Thus halving all edge errors roughly halves the closure bound ($3.4965\times10^{-3}\to1.7491\times10^{-3}$), as expected to first order since $\Delta_{\gamma}\approx\sum_e\varepsilon_e$ for small errors. (This corrects the intermediate product printed in the published version, which carried a transposition in the fifth decimal place; the final bound is unchanged at the stated precision.)

### Derivation 9: per‑edge error requirement for a three‑edge loop

For a three‑edge loop with identical edge error $\varepsilon$,