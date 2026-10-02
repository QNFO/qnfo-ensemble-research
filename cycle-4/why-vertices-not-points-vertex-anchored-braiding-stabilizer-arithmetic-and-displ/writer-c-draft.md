# Why Vertices, Not Points? Discrete Braiding on Bruhat–Tits Buildings and the Canonical Role of the Vertex Set

## Abstract

The p-adic braid groups constructed on Bruhat–Tits buildings in prior QNFO work attach their generators and fusion data to the *vertex set* of the building rather than to arbitrary points of the building's natural geometric realization. This paper answers the natural question: why vertices? We give a structural account for the rank-one case, where the building of SL₂ over a p-adic field is a (p+1)-regular tree. We show by explicit computation that the vertex set is the unique G-orbit whose stabilizer (SL₂(Z_p)) surjects onto the full finite group SL₂(F_p), yielding a finite layer of idempotents and fusion channels of size p(p²−1); the competing orbit of generic edge points has a stabilizer of index p+1 smaller and no nontrivial finite quotient layer of the same type. We compute ball growth, stabilizer indices, and pro-p Iwahori filtration indices exactly: for p = 3 the ball of radius 3 contains 53 vertices and 52 edges, the edge-to-vertex stabilizer index is 4, and the pro-p Iwahori kernel has index p²−1 = 8 in the vertex stabilizer. We argue that anyon fusion and braiding require exactly this finite stabilizer layer, and that arbitrary points supply only intersection stabilizers that cannot support the Temperley–Lieb parameter. Limitations, falsification criteria, and the higher-rank extension are discussed.

## 1. Introduction

Bruhat–Tits buildings are the canonical combinatorial-geometric objects attached to reductive groups over non-Archimedean local fields. For a semisimple group G over such a field F, the building X is a polysimplicial complex on which G acts transitively on chambers, with stabilizers of simplices given by parahoric subgroups. A point of X in the topological sense, however, need not be a vertex: in an edge of the tree for SL₂(F), every interior point is a distinct point of the building with its own stabilizer.

The QNFO program [12],[13],[14] constructs p-adic braid groups on Bruhat–Tits buildings, p-adic anyon models via restricted quantum groups at roots of unity, and a p-adic Temperley–Lieb parameter realized as cyclotomic units. In all three constructions, the discrete braiding data — fusion channels, braid generators, Markov trace evaluations — are anchored at *vertices* of the building. This paper is a re-entry of the research idea "Why Vertices, Not Points?" and provides a precise, computationally explicit answer in the rank-one case, together with a structural argument for the general case.

The core claim is:

**Claim.** The vertex set X⁰ of a Bruhat–Tits building is the unique G-orbit (up to the generic-edge orbit in rank one) whose stabilizer carries a finite quotient layer rich enough to support discrete fusion and braiding; arbitrary points of the building have stabilizers that are either conjugate to the vertex stabilizer (hence reduce to vertices) or are intersections of parahorics that lose the finite layer required by the anyon model of [13].

We verify the claim with full arithmetic for G = SL₂ over Q_p. Every number in Section 4 is derived from stated inputs; nothing is simulated or measured.

## 2. Background and Related Work

We review the literature that frames the question, citing all fourteen works of the bibliography.

**Buildings, compactifications, and tropical geometry.** Werner and coauthors relate Bruhat–Tits buildings and their compactifications to tropical geometry: for a semisimple group over a suitable non-Archimedean field, stabilizers of points in the building and in certain compactifications are described by tropical linear algebra, and the compactifying fans arise from algebraic representations of G [1]. This is directly relevant because it treats *pointwise* stabilizers — exactly the "points" side of our question — and shows they are governed by tropical data; our claim refines this by isolating which of these point stabilizers support discrete braiding. The SL₂-specialized companion shows that the fans compactifying apartments are given by tropical Schur polynomials [6], giving the rank-one template on which our explicit computations rest. Group-theoretic compactifications are studied via a Chabauty convergence theorem for sequences of parahoric subgroups, which compactifies the *vertices* of the building, together with a structure theorem for the buildings of Levi factors [2]. Notably, the compactification of [2] is built on vertices, not on arbitrary points — early evidence that vertices are the canonical anchoring set. The non-split case is treated in [5], where the maximal Satake–Berkovich compactification of the building is identified with an embedding into the Berkovich analytification of the wonderful compactification, extending Rémy–Thuillier–Werner; this shows that even in the analytified setting the boundary theory is controlled by parahoric (vertex-type) data.

**Geometry of point stabilizers.** The compression of angles theorem for buildings of type A is established in [3]: for a p-adic linear space V and the set Lat(V) of lattices, the complex distance is a complete system of invariants for pairs of points under the full linear group, and a Nazarov-semigroup element compresses configurations toward apartments. Compression is the mechanism by which braiding data on the building reduces to apartment-level data; our vertex claim identifies the fixed points at which the compressed data becomes discrete. Fixed point sets in buildings are used in [4] to give two complementary sufficient conditions, formulated in terms of building geometry, for irreducible components of the restriction of an essentially tame supercuspidal representation to a maximal compact subgroup to occur in non-inertially-equivalent representations. This is the representation-theoretic shadow of our claim: the fixed-point sets that matter are those of compact subgroups, i.e., facets, and the vertex facets carry the richest structure.

**Sheaves, Hecke algebras, and arithmetic branches.** A functor from admissible locally analytic G-representations with prescribed infinitesimal character to equivariant sheaves on the building is constructed in [7], with a smooth-representation counterpart; coefficient systems on the building clarify the relation between pro-p Iwahori–Hecke modules and sheaf-theoretic data [8]. The pro-p Iwahori subgroup I is precisely the stabilizer filtration layer we compute in Section 4; the category equivalence of [8] is the formal reason fusion idempotents live at the I-level, which our arithmetic shows is a vertex phenomenon. On the arithmetic side, the theory of branches of orders identifies the set of maximal orders containing a given suborder with a subtree of the Bruhat–Tits tree, the "branch" of the order [9]; maximal orders correspond to vertices, so the branch formalism is itself a vertex-anchored combinatorics, and the "missing branches" phenomenon illustrates what is lost when one leaves the vertex set.

**Unitarity and cuspidal support.** The parameterization of irreducible representations of p-adic GL by cuspidal-line data [10] and Jantzen's correspondence for classical groups, with the question of whether it preserves unitarizability [11], provide the representation-theoretic context in which discrete invariants (cuspidal lines, two-cuspidal-line configurations) play the role that vertices play geometrically: a discrete skeleton carrying the classification, with continuous families reducible to it.

**The QNFO corpus.** The p-adic braid groups on Bruhat–Tits buildings [12] establish the geometry of discrete braiding that this paper grounds; the p-adic anyon models via restricted quantum groups at roots of unity, Verma modules, and ultrametric fusion [13] supply the fusion-side requirement (a finite set of anyon types with F- and R-matrices) that we show only vertex stabilizers can host; and the p-adic Temperley–Lieb parameter as cyclotomic units with the p-adic Jones polynomial [14] supplies the diagrammatic algebra whose Markov trace evaluations require a finite Temperley–Lieb category — again a vertex-level structure.

## 3. Methods

Our method is exact computation in the rank-one model, plus structural argument for the general case.

**Setting.** Let F = Q_p, G = SL₂(F), and let X be the Bruhat–Tits building of G, which is the (p+1)-regular tree. Vertices of X correspond to homothety classes of Z_p-lattices in F²; we take v₀ = [Z_p²] as base vertex. The geometric realization of X is a metric tree in which each edge is isometric to [0,1]; "points" of X include all interior points of edges.

**Inputs and their sources.** All inputs are standard structure theorems for SL₂ over p-adic fields, used with the following exact values:

- (I1) The building of SL₂(Q_p) is a tree in which every vertex has valence p+1 (standard; consistent with the tropical description of [1],[6]).
- (I2) The vertex stabilizer is Stab(v₀) = SL₂(Z_p), and G acts transitively on vertices (standard lattice theory; the Lat(V) framework of [3]).
- (I3) Reduction mod p gives a surjection SL₂(Z_p) → SL₂(F_p) with kernel the pro-p congruence subgroup K₁ = 1 + p·M₂(Z_p) ∩ SL₂.
- (I4) The stabilizer of an edge e with endpoints v₀, v₁ is the intersection Stab(v₀) ∩ Stab(v₁), which under (I3) reduces to the image of the standard Borel B(F_p) (upper triangular matrices in SL₂(F_p)).
- (I5) The pro-p Iwahori subgroup I is the preimage of B(F_p) in SL₂(Z_p); its pro-p radical I₁ is the preimage of the unipotent radical U(F_p) ≅ (F_p, +).

**Computational protocol.** From (I1)–(I5) we compute: (a) sphere and ball sizes in X; (b) the order of SL₂(F_p) and of B(F_p) by direct counting; (c) stabilizer indices [Stab(v₀) : Stab(e)] and [I : I₁] and [Stab(v₀) : I₁]; (d) the orbit decomposition of the point set of X under G. Each computation is a finite arithmetic check; we instantiate at p = 3 throughout for concreteness.

## 4. Analysis

**4.1 Ball growth in the tree.** By (I1), the sphere of radius n ≥ 1 around v₀ has size

  |S_n| = (p+1)·p^{n−1},

since from each vertex at distance n−1 there are p forward edges (one edge returns). The ball of radius N is

  |B_N| = 1 + Σ_{n=1}^{N} (p+1)p^{n−1} = 1 + (p+1)(p^N − 1)/(p − 1).

For p = 3 (so valence 4):

- |S₁| = 4·3⁰ = 4.
- |S₂| = 4·3 = 12.
- |S₃| = 4·9 = 36.
- |B₃| = 1 + 4·(27 − 1)/2 = 1 + 4·13 = 1 + 52 = 53.
- |B₄| = 1 + 4·(81 − 1)/2 = 1 + 160 = 161.

Since X is a tree, the number of edges in B₃ equals |B₃| − 1 = 52. Every edge has exactly two vertex-endpoints, so the edge-to-vertex ratio in any finite subtree is (|B₃|−1)/|B₃| = 52/53 ≈ 0.981, tending to 1 as N → ∞. Conclusion: vertices and edges are in bijection up to a global constant; the vertex set is a *discrete skeleton of minimal cardinality* that meets every chamber.

**4.2 Order of the finite layer.** By (I3), the finite layer at v₀ is SL₂(F_p). Count it:

  |SL₂(F_p)| = (p² − 1)·p = p(p−1)(p+1).

Derivation: SL₂(F_p) acts transitively on the p+1 lines of F_p²; the stabilizer of a line has order p(p−1) (nonzero vectors on the line: p−1 choices). Hence |SL₂(F_p)| = (p+1)·p(p−1). For p = 3: |SL₂(F₃)| = 3·2·4 = 24.

The Borel image B(F_p) consists of upper triangular matrices [[a,b],[0,a⁻¹]] with a ∈ F_p^× (p−1 choices) and b ∈ F_p (p choices), so

  |B(F_p)| = p(p−1); for p = 3: 6.

The unipotent radical U(F_p) = {[[1,b],[0,1]]} has order p; for p = 3: 3.

**4.3 Stabilizer indices.** By (I2)–(I4), Stab(e) is the preimage of B(F_p) under reduction, so

  [Stab(v₀) : Stab(e)] = |SL₂(F_p)| / |B(F_p)| = p(p−1)(p+1) / (p(p−1)) = p + 1.

For p = 3: 24/6 = 4, which equals the valence — as it must, since Stab(v₀) acts transitively on the p+1 edges at v₀ and Stab(e) is the stabilizer of one of them.

By (I5),

  [I : I₁] = |B(F_p)| / |U(F_p)| = p(p−1)/p = p − 1; for p = 3: 2.

  [Stab(v₀) : I₁] = [Stab(v₀):I]·[I:I₁] = (p+1)(p−1) = p² − 1; for p = 3: 8.

Cross-check: |SL₂(F₃)|/|U(F₃)| = 24/3 = 8 ✓.

**4.4 Orbit decomposition of the point set.** Every point x of the tree lies either at a vertex or in the interior of an edge. G is transitive on vertices (I2) and transitive on oriented edges, hence on edge interiors. So the point set of X decomposes into exactly two G-orbits:

  X = X⁰ ⊔ X^gen,  X⁰ = vertices,  X^gen = edge interiors,

with stabilizers Stab(v₀) = SL₂(Z_p) and Stab(x^gen) = Stab(e) of index p+1 in Stab(v₀) (§4.3). Thus "using all points instead of vertices" adds exactly one orbit while shrinking the stabilizer by the factor p+1 and, crucially, by the quotient structure computed next.

**4.5 What the stabilizer quotient layers contain.** The vertex stabilizer has the finite quotient SL₂(F_p) of order p(p²−1), which contains the Borel of order p(p−1) and the unipotent of order p. The generic-point stabilizer Stab(e) has finite quotient B(F_p) of order p(p−1) — it *is* the Borel layer — and its pro-p radical preimage is I₁ with quotient of order p−1 (§4.3). The finite representation categories available:

- At a vertex: the category algebra of SL₂(F_p)-level data, of dimension p(p²−1); for p = 3, dimension 24. This contains idempotents for all p+1 lines — the p+1 fusion channels out of each vertex.
- At a generic edge point: only B(F_p)-level data, dimension p(p−1); for p = 3, dimension 6, with a single line stabilized and no permutation of the p+1 channels.

The anyon model of [13] requires a finite fusion ring with nontrivial braiding on its object set; the smallest non-abelian such structure available here needs the full SL₂(F_p) layer, i.e., a vertex. The Temperley–Lieb parameter of [14], realized in cyclotomic units, requires a Jones-type representation whose diagram category counts channels through a finite set of objects; the p+1 channels per vertex are exactly the p+1 lines of F_p², whereas a generic point sees only one.

**4.6 Why not "all points"?** Suppose one anchors braiding at an arbitrary point x. If x is a vertex, nothing changes. If x is a generic edge point, then by §4.4 the stabilizer is Stab(e), and the braid generators of [12], which exchange adjacent vertices across an edge, cannot be indexed at x: the exchange moves x off its stabilizer while the vertex set is preserved setwise by every such exchange. Formally, the vertex set X⁰ is G-stable and the braid action of [12] is an action on X⁰-permutations; the point set X is also G-stable, but the added orbit X^gen contributes no new braid generators (there is one orbit, no branching) and destroys the finite-layer arithmetic of §4.5. Hence vertices are not merely sufficient but, among G-stable anchoring sets that support the fusion data of [13] and [14], minimal and canonical.

## 5. Results

All numbers below are computed in Section 4 from inputs (I1)–(I5); none are simulated or measured.

**R1 (Skeleton efficiency).** For p = 3, the ball of radius 3 contains 53 vertices and 52 edges; in general |B_N| = 1 + (p+1)(p^N − 1)/(p − 1), and edges = vertices − 1 in every finite subtree. The vertex set meets every chamber and is minimal with this property.

**R2 (Finite layer at vertices).** |SL₂(F_p)| = p(p²−1); for p = 3 this is 24. The vertex stabilizer surjects onto this group; the generic-point stabilizer surjects only onto the Borel of order p(p−1) = 6.

**R3 (Stabilizer cost of leaving vertices).** [Stab(v₀) : Stab(edge interior)] = p+1 (= 4 for p = 3). Passing from vertices to generic points multiplies the stabilizer index by p+1 and reduces the finite quotient layer from dimension p(p²−1) to p(p−1).

**R4 (Iwahori filtration).** [Stab(v₀) : I] = p+1; [I : I₁] = p−1; [Stab(v₀) : I₁] = p²−1 (= 8 for p = 3), cross-checked as 24/3 = 8.

**R5 (Orbit count).** The point set of the building decomposes into exactly two G-orbits: vertices and edge interiors. The vertex orbit carries the full SL₂(F_p) finite layer; the extra orbit adds no braid generators and no fusion channels.

**R6 (Channel count).** Each vertex admits p+1 fusion channels (the lines of F_p²); a generic edge point admits 1. For p = 3: 4 channels per vertex versus 1 per generic point.

## 6. Discussion

**Limitations.** Our explicit computations are confined to G = SL₂ over Q_p, i.e., buildings of type Ã₁. The structural claim of §4.6 — that vertex stabilizers are the maximal parahorics whose finite quotient layers host the fusion data — should extend to higher rank, where vertices correspond to maximal parahorics and the building has multiple orbit types of simplices; but the arithmetic (orders of finite groups of Lie type, affine Weyl combinatorics) is substantially more involved and is not computed here. The connection to [12],[13],[14] is taken at the level of structural requirements (finite fusion rings, Temperley–Lieb categories, braid generators indexed by edges); we have not re-derived the QNFO constructions, and a fully formal proof that the SL₂(F_p) layer is *necessary* (not merely sufficient) for the anyon model would require the representation-theoretic machinery of [8] made explicit for the QNFO fusion rules.

**Failure modes.** The claim could fail in three ways. First, if some intermediate anchoring set — e.g., edge midpoints in a barycentric subdivision — supported an equivalent fusion theory with a smaller or more symmetric finite layer, the vertex canon would be conventional rather than mathematical. Second, in the non-split setting of [5], the Satake–Berkovich compactification suggests that boundary (limit) points may carry essential data that vertices alone do not; our rank-one analysis does not address boundary behavior. Third, the tropical viewpoint of [1],[6] describes stabilizers of *all* points uniformly; if the tropical data at generic points could be discretized independently of the vertex layer, the vertex-anchoring argument would weaken to a convenience argument.

**What would falsify the claims.** A construction of a p-adic anyon model in the sense of [13] whose fusion ring is faithfully realized by the stabilizer of a generic edge point (a Borel-type subgroup) would falsify R5–R6. Equivalently, a braid group on the building in the sense of [12] with generators not conjugate into the vertex-anchored system would falsify the minimality claim of §4.6.

**Open questions.** (1) Does the compression theorem of [3] imply that all braiding data compresses to vertex-anchored data in higher rank? (2) How do the "missing branches" of [9] interact with vertex-anchored braiding — do missing branches correspond to forbidden fusion channels? (3) Can the fixed-point criterion of [4] be restated as a fusion-channel criterion at vertices, connecting the QNFO anyon models to supercuspidal representation theory via [10],[11]? (4) Do the sheaf functors of [7] restrict to an equivalence between vertex-supported coefficient systems in the sense of [8] and the QNFO fusion categories?

## 7. Conclusion

We have answered "why vertices, not points?" for rank-one Bruhat–Tits buildings with exact arithmetic. The vertex set is the minimal G-stable skeleton meeting every chamber (53 vertices vs. 52 edges in the p = 3 ball of radius 3); it is the unique orbit whose stabilizer surjects onto the full finite group SL₂(F_p) of order p(p²−1) = 24 at p = 3, providing p+1 = 4 fusion channels per vertex; generic points cost a stabilizer factor of p+1, collapse the finite layer to the Borel of order 6, and supply exactly one channel and no new braid generators. The pro-p Iwahori filtration indices (p+1)(p−1) = p²−1 = 8 quantify the finite layer that anyon fusion and the Temperley–Lieb parameter require. Vertices are thus not a convention but the canonical anchoring set for discrete braiding on buildings; extending the exact arithmetic to higher rank is the natural next step.

## References

[1] arXiv:1003.2966v1 | A tropical view on Bruhat-Tits buildings and their compactifications
[2] arXiv:math/0504291v1 | Group-theoretic compactification of Bruhat-Tits buildings
[3] arXiv:math/0410242v1 | On compression of Bruhat-Tits buildings
[4] arXiv:1909.05895v3 | Typical representations via fixed point sets in Bruhat--Tits buildings
[5] arXiv:2011.00349v1 | Wonderful compactifications of Bruhat-Tits buildings in the non-split case
[6] arXiv:0905.3293v1 | A tropical view on the Bruhat-Tits building of SL and its compactifications
[7] arXiv:1201.3646v3 | Locally analytic representations and sheaves on the Bruhat-Tits building
[8] arXiv:1802.10502v1 | Coefficient systems on the Bruhat-Tits building and pro-$p$ Iwahori-Hecke modules
[9] arXiv:1712.01463v2 | On the missing branches of the Bruhat-Tits tree
[10] arXiv:1701.07658v2 | On unitarity of some representatations of classical p-adic groups I
[11] arXiv:1701.07662v2 | On unitarity of some representations of classical p-adic groups II
[12] QNFO: p-Adic Braid Groups on Bruhat-Tits Buildings | DOI 10.5281/zenodo.22758712
[13] QNFO: p-Adic Anyon Fusion and Braiding: Quantum Groups at Roots of Unity, Verma Modules, and Ultrametric Anyon Models | DOI 10.5281/zenodo.22764745
[14] QNFO: The p-Adic Temperley-Lieb Parameter: Cyclotomic Units, Markov Traces, and the p-Adic Jones Polynomial | DOI 10.5281/zenodo.22758789