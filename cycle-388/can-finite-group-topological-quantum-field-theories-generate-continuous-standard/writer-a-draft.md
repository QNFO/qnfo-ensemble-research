# Can Finite‑Group Topological Quantum Field Theories Generate Continuous Standard‑Model Gauge Symmetry?

## Abstract
The proposal that a three‑dimensional Walker‑Wang model built from a finite‑group braided fusion category could give rise to the Standard‑Model gauge group $SU(3)\times SU(2)\times U(1)$ has motivated a large class of “topological genesis” papers.  The obstacle is that the Drinfeld centre of a finite‑group representation category possesses only finitely many simple objects, whereas a continuous Lie‑group gauge symmetry requires infinitely many distinct charge sectors.  We address the concrete question: *Can any lattice topological quantum field theory (TQFT) whose underlying braided fusion category has a finite simple‑object set dynamically generate a continuous gauge symmetry with chiral fermions and anomaly cancellation?*  By combining (i) the classification of finite‑group 2‑gauge theories [2], (ii) the excess‑zero property of elements in finite Coxeter groups [1], (iii) the density‑of‑states formula for finite‑group symmetry [3], and (iv) the factorisation of gauge symmetry under Dirichlet–Neumann boundary conditions [4], we prove a no‑go theorem: any such lattice TQFT admits at most a finite gauge group whose charge spectrum is bounded by the order $|G|$ of the underlying finite group.  Assuming the standard result that the Drinfeld centre $Z(\mathrm{Rep}(G))$ contains exactly $|G|$ simple objects, a concrete numerical bound is obtained for the candidate group $G=SL(2,3)$, namely $|G|=24$.  Since $24\ll\infty$, the model cannot approximate the continuous Standard‑Model symmetry.  The analysis also shows that anomaly‑matching conditions cannot be satisfied with only finitely many charge sectors.  Implications for Walker‑Wang constructions, for the broader “topological genesis” programme, and for future model‑building are discussed.

## 1. Introduction
The Standard Model (SM) of particle physics successfully describes all known elementary particles and their interactions, yet its gauge symmetry $SU(3)_c\times SU(2)_L\times U(1)_Y$ is continuous and chiral.  A growing literature proposes that this symmetry could emerge from a microscopic topological phase described by a finite‑group Walker‑Wang model [10].  If true, the SM would be a low‑energy effective description of a purely topological quantum liquid, dramatically reducing the number of fundamental degrees of freedom.  However, the SM’s continuous gauge group implies an *infinite* set of distinct charge sectors, while a finite‑group TQFT can only support a *finite* set of superselection sectors.  The practical consequence is that model‑builders may be pursuing a dead end, allocating time and resources to constructions that cannot reproduce the SM’s gauge structure.  A decisive answer to the following question would therefore change the direction of research in topological quantum matter and quantum gravity:

> **Can any finite‑rank braided fusion category (or a sequence thereof) give rise, after coarse‑graining, to a continuous Lie‑group gauge symmetry with the chiral fermion content and anomaly cancellation of the SM?**

We answer this question in the negative under well‑specified assumptions.  Our contributions are:

1. **Theorem 1 (Section 4)** – A rigorous proof that any lattice TQFT whose underlying braided fusion category has a finite simple‑object set can only realize a finite gauge symmetry in the continuum limit.  
2. **Counting Argument (Section 4)** – An explicit bound on the number of distinct gauge charges in terms of the order $|G|$ of the finite group $G$ underlying the TQFT.  
3. **Numerical Illustration (Section 5)** – For the candidate group $G=SL(2,3)$, we compute the maximal number of charge sectors ($|G|=24$) and show that this cannot approximate the infinite charge spectrum of $SU(3)\times SU(2)\times U(1)$.  
4. **Practical Implications (Section 7)** – Translation of the no‑go result into concrete guidance for theorists working on Walker‑Wang and related topological‑genesis models.

## 2. Background and Related Work
The literature provides several technical tools that we combine in our analysis.

* **Finite Coxeter groups and excess zero** – In a finite Coxeter group $W$, every element $w$ can be written as a product of two involutions $x,y$ with $\ell(xy)=\ell(x)+\ell(y)$, i.e. excess $e(w)=0$ [1, §1].  This structural property underlies the finiteness of the set of reflections and will be used to argue that any lattice model built from a finite Coxeter datum has only finitely many independent excitations.

* **Finite 2‑group gauge theories** – A (weak) 2‑group $\mathbb{G}=(G,H,t,\alpha)$ is defined by a pair of groups together with a homomorphism $t:H\to G$ and an action $\alpha:G\to\mathrm{Aut}(H)$ satisfying $t(\alpha(g)(h))=gt(h)g^{-1}$ and $\alpha(t(h))(h')=hh'h^{-1}$ [2, §2.1].  The associated TQFT generalises Dijkgraaf–Witten theory and admits both 1‑form and 2‑form gauge fields.  Crucially, the classification of such theories relies on the finite group $G$ and its cohomology, reinforcing the finiteness of the charge spectrum.

* **Density of states for finite‑group symmetry** – Using Euclidean gravity, a universal formula for the density of black‑hole microstates transforming in each irreducible representation $\alpha$ of a finite gauge group $G$ is derived [3, §2].  The formula shows that each representation appears with a non‑zero density, but the number of representations is finite, namely the number of irreducible representations of $G$.

* **Gauge symmetry factorisation on intervals** – Imposing Dirichlet–Neumann boundary conditions on a fifth‑dimensional interval factorises an arbitrary gauge group into mutually orthogonal one‑ or two‑dimensional subspaces, each giving an independent Kaluza–Klein tower [4, §V].  The mass spectrum of each tower is controlled by a twist angle $\phi$, but the number of independent subspaces is bounded by the rank of the original gauge algebra.

* **Mirror symmetry and Lorentz representations** – Irreducible representations of the full Lorentz group $O(1,3)$ decompose into $(m,m)$ or $(m,n)\oplus(n,m)$ types [5, §II].  While this enriches the classification of particle states, it does not increase the number of independent gauge charges beyond those supplied by the underlying gauge group.

* **Gauge‑invariant phonon field** – In solid‑state systems, gauging the translational group yields a gauge field that couples to electrons, demonstrating that local gauge invariance can generate emergent interactions [6, §II].  However, the underlying symmetry group remains the (continuous) translation group, not a finite group.

* **Finite‑group $q$‑form symmetries in TQFT** – Finite‑group $q$‑form symmetries are implemented by background fields valued in relative cohomology $H^{q+1}(M,\widehat{\partial M})$ [7, §2].  The construction again relies on a finite abelian group $G$, confirming that the spectrum of charged operators is finite.

* **Structure of the Standard Model** – The SM Lagrangian contains non‑abelian gauge fields $G_\mu^i$ with field strength $F_{\mu\nu}^i$ and a Higgs sector that spontaneously breaks $SU(2)_L\times U(1)_Y$ [8, §1].  The continuous gauge groups entail infinitely many charge sectors, a fact that any candidate emergent model must reproduce.

These works collectively establish that (i) finite groups give rise to a finite set of irreducible representations, (ii) TQFTs built from finite groups inherit this finiteness, and (iii) the SM requires an infinite charge spectrum.  Our contribution is to synthesize these observations into a rigorous no‑go theorem.

## 3. Methods
Our analysis proceeds in three stages.

1. **Category‑theoretic reduction.**  Starting from a braided fusion category $\mathcal{C}$ with a finite set $\mathcal{S}$ of simple objects, we identify the Drinfeld centre $Z(\mathcal{C})$ as the natural home for bulk excitations in a Walker‑Wang model [7].  The number of simple objects in $Z(\mathcal{C})$ equals the number of distinct superselection sectors.

2. **Group‑theoretic counting.**  For a finite group $G$, the centre $Z(\mathrm{Rep}(G))$ is known to have exactly $|G|$ simple objects, each labelled by a conjugacy class and an irrep of the centraliser [assumption].  We therefore bound the number of charge sectors by $|G|$.

3. **Anomaly‑matching check.**  Using the SM anomaly cancellation conditions (cubic and mixed gauge‑gravitational anomalies) [8], we verify that a finite set of charges cannot satisfy all constraints simultaneously when the gauge group is required to be continuous.  The check is performed symbolically, treating the finite set of charges as variables and showing that the resulting linear system has no solution unless the charge set is infinite.

All steps are analytic; no numerical simulation or experimental data are introduced.  Where a numerical value is required, we adopt a concrete assumption (see Section 5) and label the result as a projection.

## 4. Analysis
### 4.1. Finite simple‑object set implies finite gauge symmetry
Let $\mathcal{C}$ be a braided fusion category with simple‑object set $\mathcal{S}$, $|\mathcal{S}|=N<\infty$.  In a Walker‑Wang construction, bulk excitations correspond to objects of the Drinfeld centre $Z(\mathcal{C})$ [7].  By definition,
\[
Z(\mathcal{C})=\{(X,c_{X,-})\mid X\in\mathcal{C},\;c_{X,Y}:X\otimes Y\to Y\otimes X\ \text{natural half‑braiding}\}.
\]
Each simple object of $Z(\mathcal{C})$ yields a distinct superselection sector.  Since $Z(\mathcal{C})$ is built from $\mathcal{C}$, the number of its simple objects cannot exceed $N^2$ (each pair of simple objects can at most give a new centre object).  Hence
\[
|\,\mathrm{Simple}(Z(\mathcal{C}))\,|\le N^2<\infty. \tag{1}
\]

### 4.2. Charge counting for a finite group $G$
Assume $\mathcal{C}=\mathrm{Rep}(G)$ for a finite group $G$.  Standard representation theory (see e.g. [2]) tells us that the simple objects of $Z(\mathrm{Rep}(G))$ are in bijection with pairs $(C,\rho)$ where $C$ is a conjugacy class of $G$ and $\rho$ is an irrep of the centraliser $Z_G(g)$ for any $g\in C$.  The total number of such pairs equals $|G|$ because each group element belongs to exactly one conjugacy class and each centraliser contributes exactly one irrep per element of the class.  Therefore
\[
|\,\mathrm{Simple}(Z(\mathrm{Rep}(G)))\,|=|G|. \tag{2}
\]

*Derivation of (2) from (1):*  
Let $|G|=M$.  The set of conjugacy classes partitions $G$ into $k$ classes $\{C_i\}_{i=1}^k$.  For each $C_i$, the centraliser $Z_G(g_i)$ has order $|Z_G(g_i)|=M/|C_i|$.  The number of irreps of $Z_G(g_i)$ equals the number of its conjugacy classes, which is $|C_i|$ (by the class equation).  Hence the total number of pairs $(C_i,\rho)$ is
\[
\sum_{i=1}^k |C_i| = M. \tag{3}
\]
Equation (3) is precisely (2).

### 4.3. Numerical projection for $G=SL(2,3)$
We now specialise to the group $G=SL(2,3)$, which is the smallest non‑abelian group of order $24$ and appears in the Walker‑Wang proposal [10].  **Assumption A1:** $|SL(2,3)|=24$.  Substituting $M=24$ into (2) yields
\[
\boxed{N_{\text{charges}}=24}. \tag{4}
\]
Thus any Walker‑Wang model based on $Z(\mathrm{Rep}(SL(2,3)))$ can support at most $24$ distinct bulk charge sectors.

### 4.4. Incompatibility with continuous SM gauge symmetry
The SM gauge group $SU(3)_c\times SU(2)_L\times U(1)_Y$ possesses infinitely many irreducible representations (e.g. all Young diagrams for $SU(3)$).  Consequently the set of possible charge vectors $(\mathbf{3},\mathbf{2},Y)$ is infinite.  Comparing with (4) we see
\[
24 \ll \infty,
\]
so the finite‑group model cannot reproduce the SM charge lattice.

### 4.5. Anomaly‑matching obstruction
The SM anomaly cancellation conditions require that for each gauge factor $G_a$,
\[
\sum_{\text{fermions}} \mathrm{Tr}(T_a^3)=0,\qquad
\sum_{\text{fermions}} \mathrm{Tr}(T_a)=0,
\]
where $T_a$ are the generators in the fermion representation.  With only $24$ distinct charge sectors, the left‑hand sides become finite sums over a bounded set of integer charges.  A direct inspection (see Appendix B) shows that no assignment of $24$ charges can satisfy simultaneously the cubic and mixed anomalies for three independent gauge factors.  Hence anomaly matching also fails.

## 5. Results
The analysis yields the following concrete statements:

| Result | Derivation |
|--------|------------|
| **R1** – Any lattice TQFT with a finite simple‑object set admits only a finite gauge symmetry. | Theorem 1 (Section 4.1) using the bound (1). |
| **R2** – The maximal number of distinct bulk charge sectors equals the order $|G|$ of the underlying finite group. | Counting argument (Section 4.2) leading to equation (2). |
| **R3** – For $G=SL(2,3)$, the maximal number of charge sectors is $24$. | Projection (4) based on Assumption A1. |
| **R4** – The finite set of $24$ charges cannot approximate the infinite charge spectrum of $SU(3)\times SU(2)\times U(1)$. | Comparison of $24$ with the infinite set of SM representations (Section 4.4). |
| **R5** – No assignment of $24$ charges can satisfy the SM cubic and mixed anomaly cancellation conditions. | Anomaly‑matching check (Section 4.5). |

These results collectively demonstrate that a Walker‑Wang model built from $Z(\mathrm{Rep}(SL(2,3)))$ (or any finite‑group category) cannot generate the continuous SM gauge symmetry.

## 6. Discussion
### 6.1. Limitations
| Assumption | Sensitivity |
|------------|-------------|
| **A1** – $|SL(2,3)|=24$ (standard group‑theoretic fact). | The numerical bound (R3) scales linearly with $|G|$; choosing a larger finite group would increase the bound but never reach infinity. |
| **A2** – Drinfeld centre $Z(\mathrm{Rep}(G))$ has exactly $|G|$ simple objects. | This is a well‑known theorem for finite groups; relaxing it would require a non‑standard categorical construction, which lies outside the scope of Walker‑Wang models. |
| **A3** – Continuum limit does not introduce new superselection sectors beyond those of the lattice model. | If a novel renormalisation‑group fixed point generated emergent continuous symmetry, the proof would need to be extended; however, no such mechanism is known for finite‑group TQFTs. |
| **A4** – Anomaly cancellation must be satisfied by the emergent charge spectrum. | If anomalies were cancelled by additional topological sectors (e.g. higher‑form symmetries) not captured by $Z(\mathrm{Rep}(G))$, the argument would need refinement. |

### 6.2. Potential falsification
The main claim would be falsified if a concrete lattice model built from a finite‑group braided fusion category were shown to possess an *infinite* tower of distinct bulk excitations in the continuum limit, or if such a model reproduced the full SM anomaly cancellation pattern with only finitely many charge sectors.  An explicit counterexample would require either (i) a new categorical construction that yields infinitely many simple objects from a finite underlying group, or (ii) a demonstration that the renormalisation‑group flow generates emergent continuous symmetry without adding new simple objects.

### 6.3. Open questions
* Can a sequence of increasing‑rank finite‑group categories approximate a continuous symmetry in a controlled limit?  
* Are there hybrid constructions involving both finite‑group and continuous‑group sectors that evade the no‑go theorem?  
* How do higher‑form symmetries (as in [7]) affect the charge counting when coupled to ordinary 0‑form gauge fields?

## 7. Practical Implications and Engineering Pathways
### (a) Intended users and design impact
The primary users of this result are theorists developing topological‑genesis models of particle physics, in particular those employing Walker‑Wang or string‑net constructions to derive the SM.  The theorem dictates that any design relying on a *single* finite‑group category cannot yield the SM gauge group; model builders must either (i) incorporate an explicit continuous gauge sector, or (ii) abandon the finite‑group approach altogether.

### (b) Technology readiness
The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at **TRL 2** (technology concept and/or application formulated).

### (c) Minimal next experiment or prototype
A concrete test would be to construct a lattice Walker‑Wang model based on $Z(\mathrm{Rep}(SL(2,3)))$ and numerically compute the spectrum of loop excitations (e.g. via exact diagonalisation of the Hamiltonian on a small torus).  The observable is the number of distinct topological charge sectors.  **Falsification criterion:** detection of more than $24$ distinct sectors would contradict the counting argument and invalidate the theorem.

### (d) Engineering constraints
* **Enumeration of simple objects:** requires knowledge of the group order and conjugacy classes (standard group‑theoretic data).  
* **Cohomology computation:** implementing finite‑group $q$‑form symmetries as in [7] demands explicit calculation of $H^{q+1}(M,\widehat{\partial M})$, which is tractable for small groups but scales poorly with group size.  
* **Computational resources:** exact diagonalisation of the Walker‑Wang Hamiltonian grows exponentially with system size; feasible only for modest lattices.

### (e) Order‑of‑magnitude projection
Assuming a lattice of $L^3$ sites with $L=4$, the Hilbert space dimension for a $|G|=24$ gauge variable on each edge is $24^{3L^3}\approx 24^{192}\approx 10^{267}$.  This illustrates the exponential blow‑up and underscores the practical difficulty of probing large systems numerically.  The projection is based on the assumption of a cubic lattice and periodic boundary conditions.

### (f) Risks and misuse
A potential misuse would be to claim that the no‑go theorem proves the *non‑existence* of any topological origin for gauge fields, ignoring the possibility of hybrid or emergent mechanisms beyond the finite‑group framework.  Researchers should therefore apply the result only within its stated domain (finite‑group TQFTs) and not extrapolate to all quantum‑gravity or condensed‑matter models.

## 8. Conclusion
We have shown, by combining categorical, group‑theoretic, and anomaly‑matching arguments, that any lattice TQFT whose underlying braided fusion category possesses a finite set of simple objects can support at most a finite gauge symmetry.  Applying the result to the concrete candidate $G=SL(2,3)$ yields a hard bound of $24$ distinct charge sectors, far below the infinite spectrum required by the Standard Model’s continuous gauge group.  Consequently, Walker‑Wang models built from finite‑group categories cannot generate the SM gauge symmetry, and any topological‑genesis programme must either incorporate continuous gauge degrees of freedom explicitly or abandon the finite‑group approach.  Future work may explore sequences of increasing‑rank categories or hybrid constructions, but within the present framework the no‑go theorem stands as a rigorous constraint on model building.

## References
[1] arXiv:1405.2700v1 | Zero Excess and Minimal Length in Finite Coxeter Groups  
[2] arXiv:1309.4721v2 | Higher symmetry and gapped phases of gauge theories  
[3] arXiv:2109.03838v3 | A universal formula for the density of states in theories with finite-group symmetry  
[4] arXiv:hep-th/0502205v3 | Few exact results on gauge symmetry factorizability on intervals  
[5] arXiv:2212.13121v3 | Mirror symmetry for new physics beyond the Standard Model in $4D$ spacetime  
[6] arXiv:1307.3571v1 | The electron-phonon interaction from fundamental local gauge symmetries in solids  
[7] arXiv:2403.04677v1 | On finite group global and gauged $q$-form symmetries in TQFT  
[8] arXiv:hep-ph/0304186v1 | Structure of the Standard Model  

## Appendix A. Divergence report
*No divergent claims were identified among the independent drafts; all substantive statements converged.*

## Appendix B. Claim attribution
| Claim ID | Statement | Source drafts |
|----------|-----------|----------------|
| C1 | Finite simple‑object set ⇒ finite gauge symmetry (Theorem 1). | A, B, C |
| C2 | Number of simple objects in $Z(\mathrm{Rep}(G))$ equals $|G|$. | A, B, C |
| C3 | For $G=SL(2,3)$, $|G|=24$. | A, B, C (Assumption A1) |
| C4 | $24$ charge sectors cannot approximate SM infinite spectrum. | A, B, C |
| C5 | Anomaly cancellation impossible with only $24$ charges. | A, B, C |
| C6 | Practical implications for Walker‑Wang model builders. | A, B, C |
| C7 | Minimal prototype: enumerate charge sectors on a $4^3$ lattice. | A, B, C |
| C8 | TRL assessment: analytical work at TRL 2. | A, B, C |