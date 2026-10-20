# Master Calibration for Non‑Overlapping Physical Frameworks: Composition, Closure, and the Limits of Partial Translation

## Abstract

Physics is fragmented by persistent bifurcations—general relativity versus quantum mechanics, continuum versus discrete descriptions, the Heisenberg cut, and the status of the observer. These schisms impose concrete costs: collider, fusion, and quantum‑hardware programmes proceed without a shared observable that can bridge the frameworks underlying their design choices. This work asks whether a *master calibration*—a family of partial translation maps that composes consistently across all frameworks—can exist, and what combinatorial and error‑budget burden such a calibration imposes. Counting arguments applied to a 29‑schism inventory yield 406 unordered pairwise maps and 3 654 independent composition constraints, a constraint‑to‑map ratio of exactly 9.0. A seven‑domain family admits only 21 unordered pairs, so at least eight schisms lie outside any pairwise reduction under a one‑schism‑per‑pair assumption. A three‑framework loop with edge errors $10^{-3}$, $2\times10^{-3}$, and $5\times10^{-4}$ gives a closure‑error bound of $3.4965\times10^{-3}$. A genericity projection with independent square‑constraint success probability $p=0.9$ yields a master‑calibration success probability of $6.34\times10^{-168}$ and a maximal family size of $n_{\max}=7$ at a $1\%$ success threshold. The results separate structural schisms (no admissible translation within tolerance) from conventional ones (admissible but costly) and show that beyond small families global consistency must be enforced by construction rather than hoped for.

## 1. Introduction

Experimental and theoretical physicists repeatedly confront pairs of internally successful theories that cannot be unified, and the cost of that failure is paid in programme design. The European Particle Physics Strategy Update aggregates community proposals for collider projects and quantifies the scientific reach of a shared observable, reporting expected measurement precisions of about 1 % for oblique parameters [1]. The design study for a next linear collider specifies a centre‑of‑mass energy window of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ [2]. In fusion energy, the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC) represent low‑density steady‑state and high‑density pulsed pathways whose magnetohydrodynamic stability assessments differ, so that for CFETR active control methods may be required for resistive‑wall‑mode stabilization in $80\%$ of steady‑state‑operation scenarios [4]. In quantum computing, the unresolved measurement problem and the Heisenberg cut separate quantum control from classical engineering, and divergent compositional versus holistic readings of quantum states impede error‑corrected processor design.

A systematic inventory of such fractures enumerates 29 distinct unresolved bifurcations, spanning topics from the nature of the continuum to the status of the observer, and argues that they are interconnected rather than isolated puzzles [10]. The same inventory notes the scale of the stakes: quantum electrodynamics predicts the electron’s magnetic moment to eleven decimal places while the cosmological constant disagrees with naive expectations by $120$ orders of magnitude, so individual frameworks can be spectacularly accurate inside their domains while remaining mutually uncalibrated [10]. If a family of partial translation maps could be constructed that composes consistently across all frameworks, design decisions for colliders, fusion reactors, and quantum technologies could be guided by a unified calibration budget rather than by ad‑hoc compromises. If no such family can exist beyond a small size, resources should be redirected toward explicitly mediated observables for the few pairs that admit them.

This paper therefore asks two questions: (i) under what conditions does a master calibration exist, and (ii) how large is the combinatorial burden of enforcing global consistency? The analysis formalizes frameworks as calibrated theories over disjoint domains, defines translation maps with explicit error budgets, bounds composition failure by cycle‑closure error, and applies counting arguments to the 29‑schism inventory [10] and to a modeled seven‑domain family.

**Contributions.**  
- **C1** – Formal definitions of framework, translation map, composition failure, and master calibration (Section 3).  
- **C2** – Derivation of the pairwise‑map count $\binom{29}{2}=406$ and composition‑constraint count $\binom{29}{3}=3654$, with the exact constraint‑to‑map ratio $9.0$ (Section 4, Derivation 1).  
- **C3** – Pairwise‑capacity result for a seven‑domain family: $\binom{7}{2}=21$ pairs against $29$ schisms, so at least $8$ schisms remain unassigned under the one‑schism‑per‑pair assumption (Section 4, Derivation 2).  
- **C4** – Two‑framework corner for the Feynman–Shor bifurcation: a pair of frameworks carries no composition constraint (Section 4, Derivation 2′).  
- **C5** – Three‑framework closure bound $\Delta_{\gamma}\le3.4965\times10^{-3}$ for edge errors $10^{-3}$, $2\times10^{-3}$, $5\times10^{-4}$ (Section 4, Derivation 3).  
- **C6** – Structural‑versus‑conventional classification criterion, including the chain‑length bound $k\le\ln(1-\tau)/\ln(1-\varepsilon_{\min})$ (Section 3.5 and Section 4, Derivation 4).  
- **C7** – Genericity projection $P_{\mathrm{master}}=p^{3654}=6.34\times10^{-168}$ at $p=0.9$, the threshold count $\binom{n}{3}\le43.7$, and the maximal family size $n_{\max}=7$ (Section 4, Derivation 5).  
- **C8** – Energy‑window factors $2$ (abstract) and $3$ (preface) for the linear‑collider design ranges, and mean schisms per domain $29/7\approx4.14$ under a uniformity assumption (Section 4, Derivation 6).  
- **C9** – Mediated‑translation price $1-(1-\varepsilon)^{2}=0.0199$ for $\varepsilon=10^{-2}$ (Section 4, Derivation 7).  
- **C10** – Corrected sensitivity analysis of closure error under uniform scaling of edge errors, $\Delta'_{\gamma}=1.7491\times10^{-3}$ at scaling factor $f=0.5$ (Section 4, Derivation 8).  
- **C11** – Required per‑edge error $\varepsilon\le3.33\times10^{-4}$ for a three‑edge loop to meet tolerance $\tau=10^{-3}$ (Section 4, Derivation 9).

## 2. Background and Related Work

Calibration across non‑overlapping domains has been demonstrated in engineering contexts, and these demonstrations supply both the vocabulary and the performance baselines used below.

* Road‑marking mediated calibration enables targetless extrinsic calibration of a stereo camera and a LiDAR whose fields of view do not overlap; the method reports positional accuracy of approximately $0.02\ \mathrm{m}$ and angular accuracy of $0.086^{\circ}$ without manual operation [3]. The work also flags locally accurate odometry as a fragile auxiliary assumption, illustrating how mediated calibrations can become conventional schisms when that assumption fails.

* Thru‑free multiline calibration eliminates the need for a thru standard in vector‑network‑analyzer calibration by using an arbitrary transmissive two‑port device together with an additional reflect standard; verification shows excellent agreement with traditional multiline TRL when a thru standard is available, exemplifying the construction of a calibration family from weaker or partially defined standards [8].

* In 21 cm cosmology, calibration precision is identified as a limiting systematic because astrophysical foregrounds are $10^{4}$–$10^{5}$ times brighter than the cosmological signal; the work motivates a non‑zero error floor and demonstrates how sky‑based and redundant calibration paradigms can be combined to improve performance [6].

* Multi‑environment calibration in machine learning defines calibration across environments by $\mathbb{E}[Y\mid f(X)=\alpha, E=e_i]=\alpha$ for every environment $e_i$ and proves that models calibrated on multiple domains are free of spurious correlations, providing a formal precedent for requiring a calibration property to hold over a family of domains simultaneously [5].

* Domain‑drift calibration evaluation tests methods over 28 distinct perturbation types not seen during training and shows that while in‑domain calibration can be excellent, uncertainty degrades sharply under large shifts, producing overconfident predictions; replacing the validation set by a transformed validation set improves calibration under drift, motivating the restriction of translation maps to calibrated overlap regions [7].

* The European Particle Physics Strategy Update aggregates community proposals for collider projects and quantifies the scientific reach of a shared observable: future $e^{+}e^{-}$ colliders are expected to measure oblique parameters with $\sim1\%$ precision, about a factor ten better than current precision [1].

* The linear‑collider design study specifies a centre‑of‑mass energy window of $500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ in its abstract and $0.5$–$1.5\ \mathrm{TeV}$ in its preface, providing the numerical factors used in Derivation 6 [2].

* CFETR and HFRC illustrate a second domain‑specific calibration problem: magnetohydrodynamic simulations for CFETR predict a Lundquist number $S=5.56\times10^{6}$ at a $q=2$ surface, and active control methods may be required for $80\%$ of steady‑state‑operation scenarios, highlighting how different pathways demand different mediating observables [4].

* The inventory of unresolved bifurcations enumerates 29 distinct schisms and develops a self‑referential calibration framework in which a calibration operator on the space of theories is shown, under an ultrametric distinction function, to be a contraction mapping possessing a unique fixed point; this global‑existence claim rests on strong geometric assumptions, motivating the present work’s local, assumption‑light counting and error‑budget analysis [10].

## 3. Methods

### 3.1 Frameworks and domains

**Definition 3.1 (Framework).** A framework is a pair $F_i=(D_i,\mathcal{P}_i)$ where $D_i$ is a domain (a set of states, configurations, or propositions) and $\mathcal{P}_i$ is a set of primitives (quantities, operations, or axioms) taken as given without further calibration. *Internal consistency* means that no contradiction is derivable within $D_i$ using $\mathcal{P}_i$.

*Examples.* $F_{\mathrm{QM}}$ (non‑relativistic quantum mechanics) with primitives $|\psi\rangle$ and $U_t=e^{-iHt/\hbar}$; $F_{\mathrm{SM}}$ (classical statistical mechanics) with phase‑space measure and coarse‑graining cells; $F_{\mathrm{GR}}$ (general relativity) with metric $g_{\mu\nu}$.

### 3.2 Translation maps and error

**Definition 3.2 (Translation map).** A translation $\tau_{ij}:S_{ij}\to D_j$ is a partial map defined on an overlap $S_{ij}\subseteq D_i$, equipped with a *translation error* $\varepsilon_{ij}\in[0,1)$ measured as the fraction of propositions on a chosen test battery for which $\tau_{ij}$ disagrees with the best $F_j$‑native rendering. Directionality is allowed: $\varepsilon_{ij}\neq\varepsilon_{ji}$.

The restriction to $S_{ij}$ is essential: in domain‑drift scenarios calibration quality degrades monotonically with shift magnitude, and a translation map used outside its calibrated overlap exhibits the same failure mode [7].

### 3.3 Composition and closure

For composable translations $\tau_{ij}$ and $\tau_{jk}$, the composed error obeys the first‑order bound  

$$\varepsilon_{ij\circ jk}\le\varepsilon_{ij}+\varepsilon_{jk}+\varepsilon_{ij}\,\varepsilon_{jk}.$$

**Definition 3.3 (Composition failure).** Failure occurs if there exists $x\in\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$ such that $(\tau_{jk}\circ\tau_{ij})(x)\neq\tau_{ik}(x)$.

For a cycle $\gamma$ with edges $e\in\gamma$ and errors $\varepsilon_e$, the *closure error* satisfies  

$$\Delta_{\gamma}\le 1-\prod_{e\in\gamma}(1-\varepsilon_e).$$

A framework graph is *globally calibrated* to tolerance $\tau$ if $\Delta_{\gamma}\le\tau$ for all cycles $\gamma$.

**Definition 3.4 (Master calibration).** A family $\mathcal{T}=\{\tau_{ij}\}_{i<j}$ is a master calibration if every square commutes: $\tau_{jk}\circ\tau_{ij}=\tau_{ik}$ on $\tau_{ij}^{-1}(S_{jk})\cap S_{ik}$.

### 3.4 Mediating domains

Following the engineering strategies exemplified by road‑marking mediation [3] and thru‑free multiline calibration [8], introduce a mediating domain $M$ with translations $\tau_{iM}:S_{iM}\to M$ and $\tau_{Mj}:M\supset\tau_{iM}(S_{iM})\to D_j$. The mediated translation $\tau_{Mj}\circ\tau_{iM}$ incurs two edge errors instead of one; Derivation 7 quantifies this price.

### 3.5 Structural versus conventional schisms

**Definition 3.5.** A schism between $F_i$ and $F_j$ is *structural* at tolerance $\tau$ if no admissible translation chain from $i$ to $j$ achieves $\Delta\le\tau$ (or if $S_{ij}=\varnothing$). It is *conventional* if such a chain exists but is costly—for example, long, or requiring strong auxiliary assumptions such as the extremely accurate foreground model needed in 21 cm cosmology [6].

### 3.6 Method summary

The method is analytical: definitions 3.1–3.5 are stated, and Sections 4 and 5 derive consequences by (i) combinatorial counting over the schism inventory of [10], (ii) exact evaluation of the closure‑error bound of Section 3.3 for stated edge errors, and (iii) a probabilistic projection under an explicitly assumed independence model. No experiment, measurement, or simulation is performed; every numerical input is either taken from a cited work and labeled with its citation, or stated as an explicit assumption.

## 4. Analysis

All inputs are stated with sources or as explicit assumptions, and all arithmetic is shown step by step.

**Input 1 (from [10]):** number of unresolved bifurcations $N_{\mathrm{schism}}=29$.

**Input 2 (assumption):** candidate family size $n=7$ research domains.

**Input 3 (assumption):** Feynman–Shor bifurcation partitions quantum computing into $m=2$ ontologies.

**Input 4 (from [2]):** linear‑collider centre‑of‑mass energy range $E_{\mathrm{cm}}=500\ \mathrm{GeV}$ to $1\ \mathrm{TeV}$ (abstract) and $0.5$–$1.5\ \mathrm{TeV}$ (preface).

**Input 5 (from [6]):** calibration precision is a limiting systematic in 21 cm cosmology; foregrounds are $10^{4}$–$10^{5}$ times brighter than the signal, motivating a non‑zero error floor.

**Input 6 (from [1]):** oblique parameters at future $e^{+}e^{-}$ colliders are expected to be measured with $\sim1\%$ precision, about a factor ten better than current precision.

**Input 7 (from [3]):** mediated (road‑marking) calibration achieved positional accuracy $\approx0.02\ \mathrm{m}$ and angular accuracy $\approx0.086^{\circ}$.

### Derivation 1: counting maps and composition constraints

Treat the 29 bifurcations as 29 frameworks.  
Unordered pairwise translation maps:  

$$\binom{29}{2}=\frac{29\times28}{2}=406.$$

Unordered triples (each yielding one independent square constraint):  

$$\binom{29}{3}=\frac{29\times28\times27}{6}=3654.$$

Constraint‑to‑map ratio:  

$$\frac{3654}{406}=9.0,$$

exact because  

$$\frac{\binom{N}{3}}{\binom{N}{2}}=\frac{N-2}{3}=\frac{27}{3}=9.$$

*Factor‑2 reading.* If each bifurcation is counted as two opposite‑direction frameworks ($N=58$), then  

$$\binom{58}{2}=1653,\qquad \binom{58}{3}=30856,$$

and the ratio becomes $\frac{30856}{1653}\approx18.667$.

### Derivation 2: pairwise capacity for the seven‑domain family

Unordered pairs for $n=7$:  

$$P=\binom{7}{2}=21.$$

Assuming *one‑schism‑per‑pair*, each of the $29$ bifurcations must be assigned a distinct unordered pair. Since $29>21$, at most $21$ bifurcations can be assigned, leaving  

$$29-21=8$$

unassigned. Thus at least eight schisms lie outside any pairwise reduction involving only the seven domains.

### Derivation 2′: two‑framework corner (Feynman–Shor)

For $m=2$ ontologies:  

$$\binom{2}{2}=1,\qquad \binom{2}{3}=0.$$

Hence a pair of frameworks carries no composition constraint; any single translation map trivially satisfies the master‑calibration condition for that pair.

### Derivation 3: closure‑error budget for a three‑framework loop

Edge errors: $\varepsilon_{12}=10^{-3}$, $\varepsilon_{23}=2\times10^{-3}$, $\varepsilon_{31}=5\times10^{-4}$.  

Compute  

$$1-\varepsilon_{12}=0.999,\quad 1-\varepsilon_{23}=0.998,\quad 1-\varepsilon_{31}=0.9995.$$

Product:  

$$0.999\times0.998=0.997002,$$  
$$0.997002\times0.9995=0.996503499.$$

Closure bound:  

$$\Delta_{\gamma}\le1-0.996503499=0.003496501\approx3.4965\times10^{-3}.$$

### Derivation 4: chain‑length bound for structural versus conventional classification

Given a minimum edge error $\varepsilon_{\min}=10^{-2}$ and tolerance $\tau$, a chain of $k$ edges yields  

$$\Delta=1-(1-\varepsilon_{\min})^{k}.$$

Solving $\Delta\le\tau$ for $k$ gives  

$$k\le\frac{\ln(1-\tau)}{\ln(1-\varepsilon_{\min})}.$$

For $\tau=10^{-3}$ and $\varepsilon_{\min}=10^{-2}$,  

$$k\le\frac{\ln(0.999)}{\ln(0.99)}\approx\frac{-0.0010005}{-0.0100503}\approx0.0995,$$

so a single edge already exceeds the tolerance; any longer chain is structural.

### Derivation 5: genericity projection

Assume each independent square constraint succeeds with probability $p=0.9$ and that successes are independent. The probability that *all* $3654$ constraints succeed is  

$$P_{\mathrm{master}}=p^{3654}=0.9^{3654}=6.34\times10^{-168}.$$

For a family of size $n$, the number of independent constraints is $\binom{n}{3}$. Requiring $P_{\mathrm{master}}\ge0.01$ gives  

$$0.9^{\binom{n}{3}}\ge0.01\;\Longrightarrow\;\binom{n}{3}\le\frac{\ln(0.01)}{\ln(0.9)}\approx43.7.$$

The largest integer $n$ satisfying $\binom{n}{3}\le43$ is $n_{\max}=7$.

### Derivation 6: energy‑window factors and mean schisms per domain

From Input 4, the abstract energy window is $1\ \mathrm{TeV}/0.5\ \mathrm{TeV}=2$.  
The preface window is $1.5\ \mathrm{TeV}/0.5\ \mathrm{TeV}=3$.

Mean schisms per domain under a uniform distribution:  

$$\frac{N_{\mathrm{schism}}}{n}=\frac{29}{7}=4.142857\approx4.14.$$

### Derivation 7: price of mediated translation

A mediated translation replaces a direct edge of error $\varepsilon$ by two edges each of error $\varepsilon$. The effective error becomes  

$$\Delta_{\text{mediated}}=1-(1-\varepsilon)^{2}=1-(1-2\varepsilon+\varepsilon^{2})=2\varepsilon-\varepsilon^{2}.$$

For $\varepsilon=10^{-2}$,  

$$\Delta_{\text{mediated}}=2\times10^{-2}-(10^{-2})^{2}=0.02-0.0001=0.0199.$$

### Derivation 8: sensitivity of closure error to uniform scaling

Scale all edge errors by factor $f$. Original product in Derivation 3 is $P=0.996503499$. Scaled product becomes  

$$P'(f)=(1-f\varepsilon_{12})(1-f\varepsilon_{23})(1-f\varepsilon_{31}).$$

For $f=0.5$:  

$$1-0.5\varepsilon_{12}=0.9995,\quad 1-0.5\varepsilon_{23}=0.999,\quad 1-0.5\varepsilon_{31}=0.99975.$$

Product:  

$$0.9995\times0.999=0.9985005,$$  
$$0.9985005\times0.99975=0.9982511249.$$

Closure bound:  

$$\Delta'_{\gamma}=1-0.9982511249=0.0017488751\approx1.7491\times10^{-3}.$$

Thus halving all edge errors roughly halves the closure bound.

### Derivation 9: per‑edge error requirement for a three‑edge loop

For a three‑edge loop with identical edge error $\varepsilon$, the closure bound is  

$$\Delta=1-(1-\varepsilon)^{3}\le\tau.$$

Solving for $\varepsilon$ with $\tau=10^{-3}$:  

$$(1-\varepsilon)^{3}\ge1-\tau=0.999,$$  
$$1-\varepsilon\ge0.999^{1/3}\approx0.9996667,$$  
$$\varepsilon\le1-0.9996667\approx3.33\times10^{-4}.$$

## 5. Results

The quantitative outcomes derived in Section 4 are collected below.

| Identifier | Statement | Computation |
|------------|-----------|-------------|
| **R1** | Pairwise maps = 406; composition constraints = 3 654; ratio = 9.0. | $\binom{29}{2}=406$, $\binom{29}{3}=3654$, $3654/406=9.0$ (Derivation 1). |
| **R2** | For $n=7$, unordered pairs = 21; at least 8 schisms remain unassigned under one‑schism‑per‑pair. | $\binom{7}{2}=21$, $29-21=8$ (Derivation 2). |
| **R3** | Closure bound for edge errors $10^{-3},2\times10^{-3},5\times10^{-4}$ is $3.4965\times10^{-3}$. | $1-0.999\times0.998\times0.9995=3.4965\times10^{-3}$ (Derivation 3). |
| **R4** | Chain of four edges with $\varepsilon_{\min}=10^{-2}$ yields $\Delta=3.94\times10^{-2}$ (projection assuming independent edges). | $1-(1-0.01)^{4}=1-0.96059601=0.03940399\approx3.94\times10^{-2}$. |
| **R5** | Energy‑window factor = 2 (abstract) and = 3 (preface). | $1\ \mathrm{TeV}/0.5\ \mathrm{TeV}=2$, $1.5\ \mathrm{TeV}/0.5\ \mathrm{TeV}=3$ (Derivation 6). |
| **R6** | Mean schisms per domain = 4.14 (uniform assumption). | $29/7=4.142857\approx4.14$ (Derivation 6). |
| **R7** | Feynman–Shor bifurcation ($m=2$) yields no composition constraint. | $\binom{2}{3}=0$ (Derivation 2′). |
| **R8** | Random family success probability with $p=0.9$ is $6.34\times10^{-168}$; $n_{\max}=7$ for $>1\%$ success. | $0.9^{3654}=6.34\times10^{-168}$, $\binom{7}{3}=35\le43.7<\binom{8}{3}$ (Derivation 5). |
| **R9** | Halving all edge errors halves the closure bound to $1.7491\times10^{-3}$. | Re‑compute with $f=0.5$ (Derivation 8). |
| **R10** | Mediated translation doubles error from $10^{-2}$ to $0.0199$. | $1-(1-0.01)^{2}=0.0199$ (Derivation 7). |
| **R11** | Required per‑edge error $\varepsilon\le3.33\times10^{-4}$ for tolerance $\tau=10^{-3}$. | Solve $1-(1-\varepsilon)^{3}\le10^{-3}$ (Derivation 9). |

These numbers constitute the sole quantitative basis for the conclusions drawn in the paper. No additional empirical data have been introduced.

## 6. Discussion

The quantitative analysis establishes two complementary perspectives on the master‑calibration problem. The **combinatorial perspective** (Derivations 1 and 2) shows that the 29 unresolved bifurcations generate 406 unordered pairwise translation maps and 3 654 independent composition constraints, giving an exact constraint‑to‑map ratio of $9.0$. The **error‑budget perspective** (Derivations 3–9) quantifies how edge‑wise translation errors propagate around cycles and how mediating domains increase the effective error. Together these results answer the two research questions posed in the Introduction: (i) a master calibration can exist only for families whose pairwise‑map capacity exceeds the number of schisms, and (ii) even when this capacity condition holds, the error budget must be tight enough that every cycle closes within a prescribed tolerance $\tau$.

### 6.1  Falsifiability criterion

A concrete falsification experiment follows directly from the closure‑error bound derived in Derivation 3.  Consider a three‑framework loop with edge errors  

$$\varepsilon_{12}=10^{-3},\qquad \varepsilon_{23}=2\times10^{-3},\qquad \varepsilon_{31}=5\times10^{-4}$$  

as used for Result R3.  A study would **assemble** three physical subsystems (e.g., a quantum‑optical platform, a classical interferometer, and a microwave resonator) that implement the translations $\tau_{12}$, $\tau_{23}$ and $\tau_{31}$, **measure** each $\varepsilon_{ij}$ on a common test battery, **compute** the closure error  

$$\Delta_{\gamma}=1-(1-\varepsilon_{12})(1-\varepsilon_{23})(1-\varepsilon_{31})$$  

and **compare** the result to the bound $3.4965\times10^{-3}$ obtained in R3.  Observation of $\Delta_{\gamma}>3.5\times10^{-3}$ would falsify the first‑order composition model assumed throughout the paper and would invalidate the genericity projection (Derivation 5) that treats each square constraint as an independent Bernoulli trial with probability $p=0.9$.

### 6.2  Limitations

- **Assumes independent translation errors.**  The closure bound in Derivation 3 treats the three edge errors as statistically independent, an assumption that is not guaranteed for physically coupled subsystems. Correlated errors would increase $\Delta_{\gamma}$ beyond the computed value.  
- **Relies on a uniform error floor $\varepsilon_{\min}=10^{-2}$.**  This floor is motivated by the limiting systematic identified in 21 cm cosmology [6]; any domain with a lower systematic floor would admit tighter chains, while a higher floor would render many chains structural.  
- **Uses the one‑schism‑per‑pair assumption.**  Derivation 2 assumes that each of the 29 bifurcations must occupy a distinct unordered pair; relaxing this assumption could change the unassigned‑schism count but would also require repeated use of the same pair, which may be infeasible in practice.  
- **Neglects higher‑order cycles.**  The analysis counts only unordered triples (square constraints). Cycles involving four or more frameworks introduce additional constraints that could further reduce the feasible family size.  
- **Mediating‑domain error model is first‑order.**  Derivation 7 approximates the mediated error as $1-(1-\varepsilon)^{2}$, ignoring possible error accumulation from imperfect overlap $S_{iM}$ or from additional calibration steps required to align $M$ with each framework.

### 6.3  Open questions

1. **Correlation structure of translation errors.**  Empirical studies could quantify how errors co‑vary across physically adjacent frameworks, informing a refined closure model.  
2. **Optimal mediating domain design.**  What geometric or informational properties of a mediating domain $M$ minimize the effective error $1-(1-\varepsilon)^{2}$ while preserving sufficient overlap $S_{iM}$?  
3. **Extension to hyper‑graph constraints.**  Incorporating composition constraints from cycles of length $>3$ may tighten the maximal family size $n_{\max}$ beyond the $7$ derived under the independence assumption.  
4. **Dynamic error budgeting.**  How does the closure bound evolve when edge errors are reduced adaptively (e.g., by hardware upgrades) versus uniformly scaled as in Derivation 8?  

Addressing these questions will require experimental prototypes and refined statistical models, but the present analytical framework provides a clear baseline against which such extensions can be measured.

## 7. Practical Implications and Engineering Pathways

### (a) Primary users and decision impact  
The results are directly relevant to theoretical physicists and engineering teams that design large‑scale research infrastructure (future colliders, fusion reactors, quantum‑computing platforms). The combinatorial feasibility test (Section 4, Derivation 1) tells a project‑planning committee whether a proposed set of shared observables can, in principle, be calibrated across the intended frameworks. If the test fails (e.g., a proposed family of $n=10$ frameworks would require $\binom{10}{2}=45$ unordered pairs, exceeding the $29$ available schisms), the committee must either reduce the family size or accept that additional medi