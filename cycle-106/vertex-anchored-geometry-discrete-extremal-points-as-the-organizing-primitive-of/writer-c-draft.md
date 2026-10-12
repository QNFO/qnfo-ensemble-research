# Vertex-Anchored Geometry: Discrete Extremal Points as the Organizing Primitive of Non-Archimedean Space

## Abstract

Non-Archimedean (ultrametric) geometry, in which the strong triangle inequality $d(x,z) \le \max\{d(x,y),d(y,z)\}$ replaces the Euclidean one, lacks the smooth infinitesimal structure on which most physical and geometric intuition rests. We argue that in this setting the correct organizing primitive is not the point or the ball but the vertex: the discrete extremal point of a simplicial or polytopal complex. We support this thesis in three registers. (i) Geometrically, we derive that ultrametric balls are simultaneously clopen and centered at every interior point, so that the geometry collapses onto a rooted tree whose nodes — the vertices — carry all metric information; ball counts grow as $N_k = q^k$ at depth $k$ for residue degree $q$. (ii) Phenomenologically, we show that apparent size in an ultrametric world is quantized in geometric steps of ratio $q$, in contrast with the continuum $s(d) = S/d$ of Archimedean perspective, giving a sharp observational signature. (iii) Algebraically, we analyze polystochastic polytopes $\Omega_{n,d}$, whose points are $d$-dimensional arrays with every line summing to $1$, and prove by explicit counting that whenever $d > n$ the line constraints are necessarily redundant, so vertices survive as the robust carriers of structure. We connect these threads to Bruhat–Tits buildings, where vertices classify lattice classes, and to cubic interaction vertices in higher-spin theory. The results are exact combinatorial and metric derivations; no simulations are used.

## 1. Introduction

Physical geometry is habitually Archimedean: distances live in $\mathbb{R}$, triangles obey $d(x,z) \le d(x,y) + d(y,z)$, and space admits arbitrarily fine smooth charts. A persistent minority tradition asks what survives if this is abandoned. In an ultrametric space the triangle inequality is strengthened to

$$d(x,z) \le \max\{d(x,y),\, d(y,z)\},$$

and the consequences are drastic: every triangle is isosceles with the two longest sides equal, every ball is clopen, and the space is naturally a tree. The $p$-adic numbers $\mathbb{Q}_p$ are the canonical example, and a substantial literature has explored $p$-adic and ultrametric structures in mathematical physics.

This paper advances a single organizing thesis: **in the non-Archimedean world, the vertex — not the point, not the ball, not the chart — is the primitive that carries structure.** The thesis is motivated by three independent bodies of work that all converge on discrete extremal points:

1. **Buildings.** The Bruhat–Tits construction attaches to a reductive group over a local field a simplicial complex whose vertices classify equivalence classes of lattices. The building is a combinatorial object; its geometry is entirely encoded in vertices, edges, and apartments.

2. **Polytopes of stochastic arrays.** The polystochastic polytope $\Omega_{n,d}$ is the set of $d$-dimensional $n \times \cdots \times n$ arrays whose entries are nonnegative and sum to $1$ along every line. Its extreme points (vertices) are the objects of interest, and the constraint structure behaves in a strikingly dimension-dependent way that we make precise below.

3. **Interaction theory.** In higher-spin field theory the fundamental data of an interaction is the cubic vertex; everything else is built from these discrete combinatorial seeds.

The plan of the paper is as follows. Section 2 reviews the literature. Section 3 sets up definitions. Section 4 carries out the explicit derivations: the ball–tree correspondence with ball counts $N_k = q^k$, the quantization of apparent size with step ratio $q$, and the redundancy theorem for polystochastic line constraints with full arithmetic for the cases $(n,d) = (4,3)$ and $(3,4)$. Section 5 collects the results. Section 6 discusses limitations and falsification criteria, and Section 7 concludes.

## 2. Background and Related Work

We review ten works. For each, we state what the supplied bibliographic entry supports; where an entry gives only a title and identifier, we say so and relate the work to our argument only through that title content.

**Buildings and vertices.** [1] is Tits's monograph *Buildings of Spherical Type and Finite BN-Pairs* (Lecture Notes in Mathematics 386). It is the foundational text establishing that spherical buildings are classified by Coxeter diagrams and $BN$-pairs, with chambers, panels, and vertices as the combinatorial skeleton. Our thesis that vertices are the primary objects of a non-Archimedean geometry is a direct descendant of this viewpoint. [2] is Bruhat and Tits, *Groupes réductifs sur un corps local* (Publications Mathématiques de l'IHÉS 41). This is the work that constructs the affine building attached to a reductive group over a local field; in it, vertices of the building correspond to equivalence classes of lattices in the underlying vector space. This is the sharpest available sense in which "vertex" is not a metaphor but a carrier of algebraic data, and it anchors our Section 3. [3] is Brown's *Buildings* (Springer, 1989), an expository account that develops buildings from chamber systems and demonstrates their applications to groups; it supplies the standard machinery — apartments, retractions, galleries — that we use informally in Section 3. [4] is Ronan's *Lectures on Buildings* (Academic Press, 1989), a lecture-style introduction covering buildings, chamber systems, and related geometries; it complements [3] and confirms that the vertex/chamber vocabulary is standard and stable across treatments. [5] is Schneider and Stuhler, *Representation theory and sheaves on the Bruhat–Tits building* (Publications Mathématiques de l'IHÉS 85). This work constructs representations of $p$-adic groups via sheaves supported on the building, so that the faces — including vertices — of the building organize representation-theoretic data. It is the strongest evidence we cite that vertex-level structure controls analytic content, not merely combinatorics.

**Ultrametricity in physics.** [6] is Rammal, Toulouse, and Virasoro, *Ultrametricity for physicists* (Reviews of Modern Physics 58). This review established ultrametricity as a physical organizing principle, connecting hierarchical tree structures to spin-glass phenomenology and to the general observation that many physical configuration spaces are naturally ultrametric rather than Euclidean. Our ball–tree derivation in Section 4 is the elementary metric core of the picture reviewed there. [7] is Vladimirov, Volovich, and Zelenov, *p-Adic Analysis and Mathematical Physics* (World Scientific). This monograph systematized $p$-adic analysis and its applications to mathematical physics, including $p$-adic string models; it is the standard technical reference for the ultrametric calculus on $\mathbb{Q}_p$ that our Section 4 instantiates in the simplest case. [8] is Volovich, *Number theory as the ultimate physical theory* (p-Adic Numbers, Ultrametric Analysis and Applications). The title states the program: that arithmetic number fields, not the real continuum, may be the fundamental arena of physics. Our phenomenological exercise on apparent size (Section 4) is a toy instance of asking what observation looks like in such an arena. [9] is Dragovich, Khrennikov, Kozyrev, and Volovich, *On p-adic mathematical physics* (p-Adic Numbers, Ultrametric Analysis and Applications), a survey of the field's methods and applications; it documents the breadth of models in which ultrametric distance is the operative structure. [10] is Gouvêa, *p-Adic Numbers: An Introduction* (Springer), the standard textbook treatment of the ultrametric inequality, $p$-adic balls, and their tree structure; our Lemma 1 and the counting argument of Section 4 are the textbook content made explicit with named parameters.

We note two limitations of this review. First, the polystochastic-polytope literature (the $\Omega_{n,d}$ objects of Section 4) is represented here only through the definitions we state ourselves; we found no supplied bibliographic entry dedicated to it, and all polystochastic results below are our own derivations from the definition. Second, the higher-spin cubic-vertex literature is invoked only at the level of the phrase "cubic interaction vertex" as a structural analogy; we make no claim about any specific higher-spin result.

## 3. Methods

**Ultrametric spaces and trees.** An *ultrametric space* is a metric space $(X,d)$ satisfying the strong triangle inequality

$$d(x,z) \le \max\{d(x,y),\, d(y,z)\} \qquad \text{for all } x,y,z \in X.$$

A *ball* of radius $r$ centered at $x$ is $B_r(x) = \{y \in X : d(y,x) \le r\}$. In the $p$-adic case the distance takes values in $\{p^{-k}\}_{k \in \mathbb{Z}} \cup \{0\}$, and each ball of radius $p^{-k}$ partitions into exactly $p$ balls of radius $p^{-k-1}$. We generalize: a *$q$-homogeneous ultrametric tree* is an ultrametric space in which every ball of radius $r_k = c^{-k}$ splits into exactly $q$ balls of radius $r_{k+1} = c^{-k-1}$, where $q \ge 2$ is the *branching factor* (for $\mathbb{Q}_p$, $q = p$ and $c = p$).

**Polystochastic arrays.** For integers $n \ge 2$ and $d \ge 2$, let $\Omega_{n,d}$ denote the set of $d$-dimensional arrays $x = (x_{i_1 i_2 \cdots i_d})$ with $1 \le i_j \le n$, entries $x_{i_1 \cdots i_d} \ge 0$, such that every *line* sums to $1$:

$$\sum_{i_j = 1}^{n} x_{i_1 \cdots i_j \cdots i_d} = 1 \qquad \text{for each fixed } (i_1,\ldots,\widehat{i_j},\ldots,i_d),\ j = 1,\ldots,d.$$

A *line* fixes all indices but one; there is one line for each direction $j$ and each choice of the $d-1$ remaining indices. $\Omega_{n,d}$ is a convex polytope; its extreme points are its *vertices*. We will need only two elementary facts, both proved in Section 4: the count of lines, and the nonemptiness of $\Omega_{n,d}$ via the uniform array.

**Buildings.** We use only the vocabulary: a *building* is a simplicial complex covered by subcomplexes called *apartments*, each isomorphic to a fixed Coxeter complex; its zero-dimensional simplices are *vertices*. In the Bruhat–Tits building of a reductive group over a local field, vertices classify lattice classes [2].

**Perspective model.** An object of true size $S$ at distance $d$ from an observer presents *apparent size* $s(d) = S/d$ in the Archimedean case. In a $q$-homogeneous ultrametric world, admissible observer–object distances are restricted to the discrete set $\{d_k\}_{k \in \mathbb{Z}}$ with $d_k = d_0\, q^{-k}$; we derive the resulting apparent-size spectrum in Section 4.

All derivations below are exact: they use only the definitions above, first-order logic, and integer arithmetic. No numerical simulation, sampling, or empirical input is used anywhere in this paper.

## 4. Analysis

### 4.1 Every ultrametric ball is centered at each of its points

**Lemma 1.** Let $(X,d)$ be ultrametric and let $y \in B_r(x)$. Then $B_r(y) = B_r(x)$.

*Proof.* Take $z \in B_r(x)$, i.e. $d(z,x) \le r$. By the strong triangle inequality,

$$d(z,y) \le \max\{d(z,x),\, d(x,y)\} \le r,$$

since $d(x,y) \le r$ because $y \in B_r(x)$. Hence $z \in B_r(y)$, so $B_r(x) \subseteq B_r(y)$. The reverse inclusion is identical with $x$ and $y$ interchanged. $\blacksquare$

Consequence: "the center of a ball" is not unique; the ball has no distinguished center. The metric information of $B_r(x)$ is therefore not located at a point but at the *node* of the containment tree — the vertex of the hierarchy. This is the first precise sense in which vertices, not points, carry ultrametric structure.

### 4.2 Ball counting in a $q$-homogeneous ultrametric tree

By the definition in Section 3, each ball at level $k$ (radius $r_k = c^{-k}$) contains exactly $q$ balls at level $k+1$. Let $N_k$ be the number of balls of radius $r_k$ contained in a fixed ball of radius $r_0 = c^{0} = 1$. Then

$$N_0 = 1, \qquad N_{k+1} = q\, N_k,$$

so by induction

$$N_k = q^{k}.$$

**Worked values.** For $q = 3$ (the structure of $\mathbb{Q}_3$):

$$N_1 = 3^{1} = 3, \qquad N_2 = 3^{2} = 9, \qquad N_3 = 3^{3} = 27, \qquad N_5 = 3^{5} = 243.$$

For $q = 2$:

$$N_{10} = 2^{10} = 1024, \qquad N_{20} = 2^{20} = 1{,}048{,}576.$$

Each arithmetic step is the single multiplication $N_{k+1} = q N_k$ applied iteratively; e.g. $N_5$ for $q=3$: $1 \to 3 \to 9 \to 27 \to 81 \to 243$.

### 4.3 Quantization of apparent size

Let an object of size $S$ sit at an admissible distance $d_k = d_0\, q^{-k}$ from the observer. The apparent size is

$$s_k = \frac{S}{d_k} = \frac{S}{d_0}\, q^{k}.$$

The ratio of apparent sizes at adjacent shells is

$$\frac{s_{k+1}}{s_k} = \frac{(S/d_0)\, q^{k+1}}{(S/d_0)\, q^{k}} = q,$$

independently of $k$, $S$, and $d_0$. Hence the apparent-size spectrum is the geometric progression

$$\left\{\, \frac{S}{d_0}\, q^{k} \,\right\}_{k \in \mathbb{Z}},$$

a discrete set with multiplicative step $q$, whereas the Archimedean spectrum $\{S/d : d \in \mathbb{R}_{>0}\}$ is the continuum $\mathbb{R}_{>0}$. For $q = 3$, consecutive distinguishable apparent sizes differ by a factor of exactly $3$; an object can never appear at apparent size $2\, s_k$ for any shell value $s_k$, since $2$ is not an integer power of $3$. This is a sharp, in-principle-testable signature of the ultrametric hypothesis, and it is derived, not simulated.

### 4.4 Line counts and constraint redundancy in $\Omega_{n,d}$

**Count of lines.** A line of a $d$-dimensional order-$n$ array is specified by a direction $j \in \{1,\ldots,d\}$ and fixed values of the other $d-1$ indices, each with $n$ choices. Hence

$$L(n,d) = d\, n^{\,d-1}.$$

**Worked values.** For $(n,d) = (4,3)$:

$$L(4,3) = 3 \cdot 4^{2} = 3 \cdot 16 = 48.$$

For $(n,d) = (3,4)$:

$$L(3,4) = 4 \cdot 3^{3} = 4 \cdot 27 = 108.$$

**Incidence check.** Each entry $x_{i_1 \cdots i_d}$ lies on exactly $d$ lines (one per direction), so the total number of (entry, line) incidences is $d\, n^{d}$. Each line contains $n$ entries, so incidences also equal $L(n,d)\cdot n = d\, n^{d-1} \cdot n = d\, n^{d}$. The two counts agree identically; for $(4,3)$: $3 \cdot 64 = 192 = 48 \cdot 4$. ✓

**Naive dimension count.** The array has $n^{d}$ entries,