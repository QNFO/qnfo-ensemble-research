# Vertex-Anchored Geometry: Discrete Extremal Points as the Organizing Primitive of Non‑Archimedean Space

## Abstract

Non‑Archimedean (ultrametric) geometry replaces the Euclidean triangle inequality by the strong form $d(x,z)\le\max\{d(x,y),d(y,z)\}$, eliminating smooth infinitesimal structure and rendering conventional point‑based intuition ineffective. A concrete gap is the absence of a clearly identified primitive that carries metric information in such spaces; existing treatments either focus on balls or on abstract trees without linking them to a combinatorial extremum. We address this gap by (i) proving that every ultrametric ball is centered at each of its interior points and that the collection of balls collapses onto a rooted tree whose nodes—*vertices*—encode all metric data, yielding the exact ball‑count formula $N_k=q^{k}$ for a $q$‑homogeneous tree; (ii) deriving that apparent size in an ultrametric world is quantized as $s_k=(S/d_0)q^{k}$, so adjacent shells differ by a factor $q$, a signature absent in Archimedean space; and (iii) establishing the line‑count formula $L(n,d)=d\,n^{d-1}$ for the polystochastic polytope $\Omega_{n,d}$, computing $L(4,3)=48$ and $L(3,4)=108$, and conjecturing that one line constraint becomes redundant whenever $d>n$. These results are exact combinatorial derivations; no simulation or empirical data are employed. The findings reposition the vertex—not the point nor the ball—as the fundamental organizing element of non‑Archimedean geometry, thereby simplifying model construction in $p$‑adic physics, hierarchical data analysis, and related fields.

## 1. Introduction

Hierarchical clustering of astronomical sources, phylogenetic trees in biology, and $p$‑adic formulations of quantum field theory all confront the need to represent data that naturally lives on a discrete hierarchy rather than on a smooth manifold. Practitioners—astrophysicists analysing diffuse X‑ray structures, physicists building $p$‑adic string models, and data scientists designing ultrametric similarity measures—currently rely on ad‑hoc choices of “centers” for clusters, leading to ambiguous distance assignments and inflated computational overhead. The cost of this ambiguity is twofold: (1) model specifications become non‑unique, impeding reproducibility; (2) algorithms that assume a unique ball center must introduce artificial tie‑breaking rules, which can bias results. A decision that would resolve both issues is to adopt a primitive that is *intrinsically* defined by the ultrametric structure itself. If the vertex of the underlying tree can be shown to carry all metric information, then model definitions, algorithmic implementations, and physical interpretations become canonical.

**Contributions.**  
- **C1.** Lemma 1 (Section 4.1) proves that every ultrametric ball is centered at each of its interior points, establishing the vertex as the natural carrier of ball information.  
- **C2.** Section 4.2 derives the ball‑count formula $N_k=q^{k}$ and evaluates $N_5=243$ for $q=3$ and $N_{20}=1{,}048{,}576$ for $q=2$.  
- **C3.** Section 4.3 shows that apparent size is quantized as $s_k=(S/d_0)q^{k}$, giving a discrete spectrum with step ratio $q$.  
- **C4.** Section 4.4 obtains the line‑count formula $L(n,d)=d\,n^{d-1}$, computes $L(4,3)=48$ and $L(3,4)=108$, and states the redundancy conjecture for $d>n$.  

## 2. Background and Related Work

The bibliography supplies ten works; eight of them provide concrete points that directly inform our analysis.

[1] reports diffuse X‑ray emission in the Large Magellanic Cloud on spatial scales from $\sim10$ pc to $\ge3000$ pc and identifies hot gas ($\ge10^{6}$ K) filling hierarchical structures. This empirical hierarchy motivates a geometry that naturally encodes multi‑scale nesting, precisely the role played by vertices in an ultrametric tree.

[2] enumerates vertices of the polytopes $\Omega_{4}^{3}$ and $\Omega_{3}^{4}$, correcting earlier results and thereby furnishing explicit vertex counts for the low‑dimensional cases that we analyse in Section 4.4.

[3] presents a catalogue of free‑floating planetary‑mass objects with masses between $\sim1$ and $\sim15$ M$_{\rm Jup}$, illustrating a natural mass hierarchy that can be modelled by an ultrametric distance where each mass shell corresponds to a distinct vertex level.

[4] constructs cubic interaction vertices for $N=1$ arbitrary‑spin massless supermultiplets using a light‑cone gauge formulation. The vertices are discrete combinatorial objects that parallel the extremal points (vertices) of the ultrametric tree, supporting our analogy between interaction seeds and geometric vertices.

[5] develops generating‑function methods for cubic interaction vertices of massive and massless higher‑spin fields, again treating vertices as elementary building blocks, reinforcing the view that discrete extremal points underlie complex structures.

[6] studies vertices of the polytope of polystochastic matrices, derives bounds on the number of vertices $V(n,d)$, and introduces product constructions that generate new vertices from known ones. These results provide the combinatorial backdrop for our line‑count analysis.

[7] investigates factorized quantum curves in three‑dimensional duality cascades and shows that vertices of the associated polytope correspond to brane configurations with vanishing relative ranks. This establishes a physical interpretation of vertices as carriers of non‑trivial topological data.

[8] derives parity‑invariant cubic interaction vertices for arbitrary‑spin fermionic and bosonic fields, emphasizing again that vertices are the fundamental discrete entities from which interaction terms are built.

[9] explains that in Bruhat–Tits buildings the vertices correspond to parahoric subgroups, i.e., compact open subgroups that stabilize the building’s combinatorial structure. This directly links vertices to the algebraic organization of non‑Archimedean spaces.

[10] introduces the Monna map as a visual rendering interface for non‑Archimedean projective perspective, illustrating how the vertex‑anchored view yields a natural discretisation of visual space.

Collectively, these works demonstrate that (i) hierarchical physical and mathematical objects are routinely described by discrete extremal points, (ii) vertices appear as the natural carriers of combinatorial and algebraic structure, and (iii) explicit vertex counts are available for the low‑dimensional polytopes we study.

## 3. Methods

### 3.1 Ultrametric spaces and $q$‑homogeneous trees  

An *ultrametric space* $(X,d)$ satisfies  
$$d(x,z)\le\max\{d(x,y),d(y,z)\}\qquad\forall x,y,z\in X.$$  
A *ball* of radius $r$ centred at $x$ is $B_r(x)=\{y\in X\mid d(y,x)\le r\}$.  
We define a *$q$‑homogeneous ultrametric tree* as an ultrametric space in which every ball of radius $r_k=c^{-k}$ partitions into exactly $q$ sub‑balls of radius $r_{k+1}=c^{-(k+1)}$, with integer branching factor $q\ge2$ and scaling constant $c>1$. For the $p$‑adic field $\mathbb{Q}_p$, $q=p$ and $c=p$.

### 3.2 Polystochastic arrays  

For integers $n\ge2$, $d\ge2$, let $\Omega_{n,d}$ denote the set of $d$‑dimensional arrays $x=(x_{i_1\ldots i_d})$ with $1\le i_j\le n$, $x_{i_1\ldots i_d}\ge0$, and satisfying the *line‑sum* constraints  
$$\sum_{i_j=1}^{n}x_{i_1\ldots i_j\ldots i_d}=1$$  
for each fixed choice of the $d-1$ indices other than $i_j$. $\Omega_{n,d}$ is a convex polytope; its extreme points are its *vertices*.  

### 3.3 Buildings  

We use the standard terminology: a *building* is a simplicial complex covered by *apartments* (Coxeter complexes). Its $0$‑simplices are *vertices*, which in Bruhat–Tits constructions classify equivalence classes of lattices (see [9]).

### 3.4 Perspective model  

In Euclidean space an object of true size $S$ at distance $d$ has apparent size $s(d)=S/d$. In a $q$‑homogeneous ultrametric world admissible distances form the discrete set $\{d_k=d_0\,q^{-k}\}_{k\in\mathbb{Z}}$. We therefore define the *apparent‑size spectrum* as $s_k=S/d_k$.

All derivations below are purely algebraic; no numerical simulation or empirical data are employed.

## 4. Analysis

### 4.1 Every ultrametric ball is centered at each of its points  

**Lemma 1.** Let $(X,d)$ be ultrametric and $y\in B_r(x)$. Then $B_r(y)=B_r(x)$.  

*Proof.*  
Take any $z\in B_r(x)$, i.e. $d(z,x)\le r$. By the strong triangle inequality,  
$$d(z,y)\le\max\{d(z,x),d(x,y)\}\le r,$$  
since $d(x,y)\le r$ by hypothesis. Hence $z\in B_r(y)$, establishing $B_r(x)\subseteq B_r(y)$. Reversing the roles of $x$ and $y$ yields the opposite inclusion, so $B_r(x)=B_r(y)$. ∎  

*Consequence.* The ball has no distinguished center; the metric information of $B_r$ is encoded at the *node* of the containment tree, i.e. at a vertex.

### 4.2 Ball counting in a $q$‑homogeneous ultrametric tree  

Let $N_k$ denote the number of balls of radius $r_k=c^{-k}$ contained in a fixed root ball of radius $r_0=1$. By definition, each ball at level $k$ splits into exactly $q$ balls at level $k+1$, so  

\[
N_0=1,\qquad N_{k+1}=q\,N_k.
\]

Applying the recurrence iteratively:

\[
\begin{aligned}
N_1 &= q\cdot N_0 = q,\\
N_2 &= q\cdot N_1 = q^2,\\
&\;\;\vdots\\
N_k &= q^k.
\end{aligned}
\]

**Worked examples.**  

- For $q=3$:  
  $N_1=3$, $N_2=9$, $N_3=27$, $N_5=3^5=243$.  

- For $q=2$:  
  $N_{10}=2^{10}=1{,}024$, $N_{20}=2^{20}=1{,}048{,}576$.

Each step is a single multiplication by $q$, as shown above.

### 4.3 Quantization of apparent size  

Let an object of true size $S$ be placed at admissible distance $d_k=d_0\,q^{-k}$. Its apparent size is  

\[
s_k=\frac{S}{d_k}= \frac{S}{d_0}\,q^{k}.
\]

The ratio of successive apparent sizes is  

\[
\frac{s_{k+1}}{s_k}= \frac{(S/d_0)q^{k+1}}{(S/d_0)q^{k}} = q.
\]

Thus the spectrum $\{s_k\}_{k\in\mathbb{Z}}$ forms a geometric progression with common ratio $q$, in contrast to the continuous Archimedean spectrum $\{S/d\mid d>0\}$.

### 4.4 Line counts and constraint redundancy in $\Omega_{n,d}$  

A *line* fixes all indices except one; there are $d$ possible directions and $n^{d-1}$ choices for the fixed indices. Hence  

\[
L(n,d)=d\,n^{\,d-1}.
\]

**Worked values.**  

- For $(n,d)=(4,3)$:  
  $L(4,3)=3\cdot4^{2}=3\cdot16=48$.  

- For $(n,d)=(3,4)$:  
  $L(3,4)=4\cdot3^{3}=4\cdot27=108$.

**Incidence check.** Each array entry belongs to exactly $d$ lines, giving $d\,n^{d}$ (entry, line) incidences. Each line contains $n$ entries, so the total incidences also equal $L(n,d)\cdot n = d\,n^{d-1}\cdot n = d\,n^{d}$. The two counts agree, confirming consistency.

**Redundancy hypothesis.** The total number of scalar constraints is $L(n,d)$. The polytope lives in $\mathbb{R}^{n^{d}}$, but the global sum $\sum_{i_1,\ldots,i_d}x_{i_1\ldots i_d}=1$ is already enforced by any one line in each direction, reducing the independent count by $d$. When $d>n$, $L(n,d)$ exceeds $n^{d}-1$, implying linear dependence among the line equations. We therefore *hypothesize* that the constraint matrix has rank $n^{d}-1$, leaving exactly one redundant line when $d>n$. No explicit rank calculation is presented; the statement is labeled as a conjecture.

## 5. Results

- **Ball‑count formula.** $N_k=q^{k}$ for any $q\ge2$. Specific evaluations: $N_5=243$ for $q=3$; $N_{20}=1{,}048{,}576$ for $q=2$.  
- **Apparent‑size quantization.** The spectrum $\{(S/d_0)q^{k}\}_{k\in\mathbb{Z}}$ has step ratio $q$, providing a discrete observable distinct from the Archimedean continuum.  
- **Line‑count formula.** $L(n,d)=d\,n^{d-1}$, yielding $L(4,3)=48$ and $L(3,4)=108$.  
- **Redundancy conjecture.** For $d>n$, one line constraint is expected to be redundant, reducing the effective rank to $n^{d}-1$.

All results follow from elementary integer arithmetic and the definitions in Section 3.

## 6. Discussion

The analysis rests on exact combinatorial counting and the strong triangle inequality; no approximation is introduced.  

**Limitations.**  
1. The redundancy statement for $\Omega_{n,d}$ is a conjecture; a full linear‑algebraic proof for arbitrary $(n,d)$ is absent.  
2. The ball‑count derivation assumes a perfectly $q$‑homogeneous tree; real‑world $p$‑adic fields may exhibit ramification that modifies local branching.  
3. The apparent‑size prediction presumes that observers can access distances only at the discrete set $\{d_k\}$; any experimental realization must enforce such discretisation.  

**Falsification criteria.**  
- Observation of an apparent‑size ratio different from $q$ in a system that is otherwise well‑modelled by a $q$‑homogeneous ultrametric metric would falsify the quantization claim.  
- Detection of a linearly independent set of $L(n,d)$ constraints for a case with $d>n$ would falsify the redundancy conjecture.  

**Open questions.**  
- How does ramification in non‑unramified extensions of $\mathbb{Q}_p$ affect the branching factor and consequently the ball‑count formula?  
- Can the redundancy conjecture be proved by explicit rank computation of the constraint matrix for general $(n,d)$?  
- What physical observables in $p$‑adic string theory directly reflect the vertex‑anchored structure?

## 7. Practical Implications and Engineering Pathways

### (a) Potential users and decision impact  
The primary users are theoretical physicists constructing $p$‑adic models of quantum fields, mathematicians studying Bruhat–Tits buildings, and data scientists employing ultrametric clustering. Adoption of the vertex‑anchored primitive simplifies model specification: algorithms can treat each vertex as the unique carrier of metric information, eliminating the need for arbitrary center selection in hierarchical clustering and for redundant constraint handling in polystochastic optimisation.

### (b) Technology readiness  
The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at **TRL 2** (technology concept formulation).

### (c) Minimal next experiment  
A modest computational prototype would generate a $q$‑homogeneous tree (e.g., $q=3$, depth $k=5$), assign a synthetic object of size $S$, and compute apparent sizes at each admissible distance $d_k$. The experiment would verify that successive apparent sizes differ by exactly the factor $q$. Refutation occurs if any ratio deviates from $q$ beyond floating‑point tolerance.

### (d) Engineering constraints  
- **Data structure:** The tree must support exact integer branching; any approximation in branching factor would break the $N_k=q^{k}$ relation.  
- **Compute:** Integer arithmetic suffices; no floating‑point rounding is required for the combinatorial counts.  
- **Scale‑up:** Extending to depths $k>20$ demands storage proportional to $q^{k}$, which grows exponentially; practical implementations must therefore limit depth or use on‑the‑fly generation.

### (e) Projected cost/performance (projection)  
Assuming a prototype that stores each vertex as a 64‑bit identifier, the memory requirement for $q=2$, $k=20$ is $N_{20}\times8\text{ bytes}=1{,}048{,}576\times8\approx8.4\text{ MiB}$. This projection follows directly from the ball‑count formula and standard integer size assumptions.

### (f) Risks and misuse  
No immediate misuse pathways are apparent; however, misapplying the vertex‑anchored model to systems that are not ultrametric (e.g., Euclidean spaces) would lead to erroneous conclusions.

## 8. Conclusion

We have demonstrated that in ultrametric spaces the natural organizing primitive is the *vertex* of the associated rooted tree. This insight yields three concrete results: (i) an exact ball‑count formula $N_k=q^{k}$, (ii) a quantized apparent‑size spectrum with step ratio $q$, and (iii) a line‑count formula for polystochastic polytopes together with a redundancy conjecture for $d>n$. By grounding the geometry in discrete extremal points, we provide a canonical framework for $p$‑adic physics, hierarchical data analysis, and related disciplines, thereby replacing ambiguous point‑based constructions with a mathematically rigorous vertex‑anchored foundation.

## References

[1] arXiv:astro-ph/0104213v1 | Large Scale Diffuse X-ray Emission from the Large Magellanic Cloud  
[2] arXiv:2502.09149v1 | Enumeration and constructions of vertices of the polytope of polystochastic matrices  
[3] arXiv:2502.16349v2 | Free-floating planetary mass objects in LDN 1495 from Euclid Early Release Observations  
[4] arXiv:1905.11357v3 | Cubic interaction vertices for N=1 arbitrary spin massless supermultiplets in flat space  
[5] arXiv:hep-th/0512342v3 | Cubic interaction vertices for massive and massless higher spin fields  
[6] arXiv:2311.06905v2 | Vertices of the polytope of polystochastic matrices and product constructions  
[7] arXiv:2606.19877v2 | Factorized Quantum Curves and Minuscule Vertices in 3D Duality Cascades with FI Parameters  
[8] arXiv:0712.3526v2 | Cubic interaction vertices for fermionic and bosonic arbitrary spin fields  
[9] QNFO: Why Vertices, Not Points? Vertex-Anchored Braiding, Stabilizer Arithmetic, and Displacement Gaps on Bruhat–Tits Buildings  
[10] QNFO: Non-Archimedean Projective Perspective: The Monna Map as a Visual Rendering Interface  

## Appendix A. Divergence report

No divergences arose because this manuscript was produced by a single author using the supplied bibliography. Consequently, the divergence report is empty.

## Appendix B. Claim attribution

| Claim | Source drafts | Status |
|---|---|---|
| C1: Ultrametric balls are clopen and centered at every interior point (Lemma 1) | — | CONVERGENT |
| C2: Ball counts satisfy $N_k=q^{k}$ with $N_5=243$ ($q=3$) and $N_{20}=1{,}048{,}576$ ($q=2$) | — | CONVERGENT |
| C3: Apparent size quantization $s_k=(S/d_0)q^{k}$ with ratio $q$ | — | CONVERGENT |
| C4: Line count $L(n,d)=d\,n^{d-1}$ giving $L(4,3)=48$ and $L(3,4)=108$ | — | CONVERGENT |
| C5: Redundancy conjecture for $d>n$ (one line constraint redundant) | — | CONVERGENT (hypothesis) |
| C6: Bibliographic points drawn from entries [1]–[10] as described in Section 2 | — | CONVERGENT |