# Automorphisms and Scaling Transformations: A Re-Entry Framework for Structure-Preserving Maps Across Algebraic, Geometric, and Ultrametric Contexts

## Abstract

We propose a unifying "re-entry" framework in which automorphisms of mathematical structures are analyzed through their relationship to scaling transformations, i.e., one-parameter families of maps that rescale a chosen coordinate or grading while preserving the ambient structure. The motivating question, posed in the QNFO ultrametric physics research context, is whether automorphism groups admit canonical decompositions into scaling-type and non-scaling-type elements. We develop a vocabulary for this question and test it against eight concrete mathematical settings drawn from the recent literature: birational automorphism groups of varieties of Picard number two, automorphisms of Cayley-Dickson algebras (octonions and sedenions), moduli of K3 surfaces with nonsymplectic automorphisms, automorphisms of parabolic geometries, outer automorphisms of free-product splittings, bounds on orders of automorphisms of curves, induced automorphisms on irreducible symplectic manifolds, and holomorphic automorphisms of $\mathbb{C}^{2}$ with non-recurrent Fatou components. We derive explicit numerical invariants where the source summaries supply counts: the doubling of Cayley-Dickson dimension ($8 \to 16$), the growth of associative quaternion ring counts ($7 \to 35$, a factor of $5$), and combinatorial counts for free-product splittings. We argue that the scaling/automorphism dichotomy is best understood as a grading question and identify falsifiable predictions for the ultrametric physics program.

## 1. Introduction

An automorphism of a structure $X$ is an isomorphism $f: X \to X$ from $X$ to itself. A scaling transformation is, in this paper, a one-parameter family $\{s_t\}_{t \in \mathbb{R}}$ of self-maps of $X$ (or of a chosen grading, filtration, or metric on $X$) satisfying the composition law

$$s_{t_1} \circ s_{t_2} = s_{t_1 + t_2},$$

so that the family forms an action of the additive group $(\mathbb{R}, +)$, or of a discrete analogue $(\mathbb{Z}, +)$. The question addressed here — the "re-entry" question recorded in the QNFO research context — is: **to what extent can automorphism groups of mathematical structures be decomposed into, or related to, scaling transformations?**

The question is deliberately broad, and a single paper cannot answer it in full generality. What we do instead is threefold. First, we set up a precise vocabulary: a *scaling-compatible* automorphism is one that lies in, or normalizes, a subgroup isomorphic to $(\mathbb{R},+)$ or $(\mathbb{Z},+)$ acting with a rescaling interpretation on some canonical object attached to $X$ (a cone, a grading, a metric). Second, we survey eight recent arXiv works spanning algebra (non-associative algebras, free products, curves), geometry (projective varieties, symplectic manifolds, parabolic geometries), and dynamics (holomorphic automorphisms of $\mathbb{C}^2$), asking in each case what the source establishes about the structure of the relevant automorphism group and where a scaling interpretation could attach. Third, we compute explicit numerical invariants wherever the source material supplies counts, with all arithmetic shown, so that the framework is anchored in verifiable quantities rather than analogy alone.

The paper is written for an adjacent-field expert: a physicist or applied mathematician familiar with group actions and lattices but not with the specialized literature on automorphism groups in algebraic geometry and non-associative algebra. Jargon is defined once at first use.

The plan of the paper is as follows. Section 2 reviews the twelve source works. Section 3 states the framework definitions. Section 4 carries out the explicit derivations. Section 5 reports results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 concludes.

## 2. Background and Related Work

We discuss all twelve bibliography entries. Entries [1]–[8] are arXiv mathematics papers whose supplied summaries we quote or paraphrase strictly; entries [9]–[12] are QNFO corpus documents whose supplied summaries are empty, and we say so explicitly, relating them to our argument only through their titles.

**[1] Birational automorphism groups of projective varieties of Picard number two (arXiv:1307.5490v2).** The authors extend results of Oguiso on birational or automorphism groups, and of Lazić–Peternell on the Morrison–Kawamata cone conjecture, from Calabi–Yau manifolds of Picard number two to arbitrary singular varieties $X$ (resp. to klt Calabi–Yau pairs in broad sense) of Picard number two. The supplied summary states the headline dichotomy: when $X$ has only klt singularities and is not a complex torus, either $\mathrm{Aut}(X)$ is almost cyclic, or (the summary is truncated at this point). For our framework this is the central geometric datum: the *Picard number* $\rho(X)$, defined as the rank of the Néron–Severi group of divisor classes modulo numerical equivalence, equals $2$, so the natural cone object attached to $X$ is two-dimensional, and the automorphism group acts on it while a discrete scaling-type group (the group of divisor-class rescalings relevant to the cone conjecture setting) acts alongside it. The dichotomy "almost cyclic or otherwise" is precisely the kind of structural constraint a scaling decomposition must respect.

**[2] Automorphisms of Sedenions (arXiv:2512.07210v3).** This paper extends the octonion calibration in Clifford algebra to two related sedenion calibrations. Associative calibrations map quaternion rings in Clifford algebra to those in Cayley–Dickson algebras, with octonions consisting of seven rings and sedenions having $35$ rings. A new non-associative calibration is found that is related to the sedenion associative calibration but is invertible (the summary truncates here). This is the entry that supplies our cleanest numerical material: the counts $7$ and $35$ of associative quaternion rings, and the Cayley–Dickson doubling structure, in which each step of the construction doubles the real dimension of the algebra. The scaling connection is direct: the Cayley–Doubling procedure is literally a discrete scaling of dimension, $d \mapsto 2d$, and the automorphism/calibration data scale along with it in a nontrivial, countable way.

**[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism (arXiv:2110.13834v2).** The authors construct a modular compactification via stable slc pairs for the moduli spaces of K3 surfaces equipped with a nonsymplectic group of automorphisms, under the assumption that some combination of the fixed loci of the automorphisms defines an effective big divisor, and prove that the compactification is semitoroidal. A *nonsymplectic* automorphism is one that does not preserve the holomorphic symplectic form of the K3 surface. For our framework, the fixed-locus/divisor condition is a compatibility condition between automorphisms and a divisorial (cone-like) object, and "semitoroidal" compactifications are built from toroidal (cone-complex) data, i.e., from the same cone-scaling geometry that appears in entry [1].

**[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries (arXiv:1312.7318v3).** The authors consider automorphisms of homogeneous parabolic geometries with a fixed point. Parabolic geometries carry distinguished distributions, and the paper studies those automorphisms which enjoy natural actions on the distributions at the fixed points; the sets of such automorphisms are described in detail, and the paper classifies whether there are non-flat homogeneous parabolic geometries (the summary truncates). The relevance here is that a *distinguished distribution* is a graded object, and an automorphism acting "naturally" on it at a fixed point is a linear (hence potentially scaling-type) action on graded pieces — the closest entry in the corpus to a literal tangent-space scaling statement.

**[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product (arXiv:2412.04250v2).** The authors give a concise presentation for the group of pure symmetric outer automorphisms of a splitting of a free product $G_{1} \ast \dots \ast G_{n}$: these are the (outer) automorphisms which preserve the conjugacy classes of the free factors $G_{i}$. The presentation is achieved by considering the action of these automorphisms on a particular subcomplex of Outer Space, which the authors show to be simply connected. The "symmetric" condition means the automorphisms may permute the factor conjugacy classes among themselves, so there is a natural action on a set of $n$ objects — the combinatorial skeleton on which our counting derivations in Section 4 rest.

**[6] Bounding the order of automorphisms of certain curves (arXiv:alg-geom/9411016v2).** The authors study upper bounds on the order of automorphisms of non-singular curves $X$ satisfying at least one of two hypotheses: (1) $X$ is an $m$-sheeted covering of exactly one non-singular curve of genus $\gamma$, where $m$ is prime; (2) the center of the group of automorphisms of $X$ is non-trivial. The supplied summary states no explicit numerical bound, so we use this entry only qualitatively: it is a source of *finiteness* constraints on automorphism orders, which in our framework bound how far a cyclic (discrete-scaling) subgroup can generate nontrivial dynamics on a curve of fixed type.

**[7] Induced Automorphisms on Irreducible Symplectic Manifolds (arXiv:1405.5706v2).** The authors introduce the notion of induced automorphisms in order to state a criterion determining whether a given automorphism on a manifold of $K3^{[n]}$ type is in fact induced by an automorphism of a K3 surface, with the manifold a moduli space of stable objects on the K3. The criterion is applied to the classification of non-symplectic prime order automorphisms on manifolds of $K3^{[2]}$ type (the summary truncates). For our framework this is a *descent* statement: an automorphism at one level of a hierarchy (the $K3^{[n]}$ manifold) is explained by an automorphism at a lower level (the K3 surface), which is structurally analogous to a scaling relation between levels of a hierarchy — the organizing principle of the ultrametric context discussed below.

**[8] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$ (arXiv:1909.00765v2).** The authors show the existence of automorphisms $F$ of $\mathbb{C}^{2}$ with a non-recurrent Fatou component $\Omega$ biholomorphic to $\mathbb{C} \times \mathbb{C}^{*}$ that is the basin of attraction to an invariant entire curve on which $F$ acts as an irrational rotation. They further show that the biholomorphism $\Omega \to \mathbb{C} \times \mathbb{C}^{*}$ can be chosen so that it conjugates $F$ to a translation (the summary truncates mid-formula). This is the most dynamically explicit entry: on the invariant curve, $F$ is conjugate to a rotation (a bounded, recurrent-type motion), while the ambient conjugation target is a translation — an unbounded, translation-type map, which is exactly the additive-scaling law $s_{t_1} \circ s_{t_2} = s_{t_1+t_2}$ of our Introduction.

**[9]–[12] QNFO corpus documents.** Entries [9] (QNFO: ULTRAMETRIC PHYSICS), [10] (QNFO: Ultrametric Physics Research Plan), [11] (QNFO: Meta-Analysis of Categorical Equivalence and Scale Invariance), and [12] (QNFO: Alpha Pi Project) are supplied with empty summaries; the supplied material gives no further detail beyond the titles. We therefore relate them to our argument only through those titles: [9] and [10] name an ultrametric physics program and its research plan, in which hierarchical (ultrametric) scale structure is the organizing object and the re-entry question of Section 1 originates; [11] names a meta-analysis of categorical equivalence and scale invariance, which is precisely the pairing of structure-preservation (categorical equivalence, the automorphism side) with scaling (scale invariance) that this paper formalizes; [12] names the Alpha Pi Project, whose title alone supplies no content we can use. We flag this thinness explicitly rather than importing outside knowledge.

## 3. Methods

### 3.1 Definitions

Let $X$ be a mathematical structure and $G = \mathrm{Aut}(X)$ its automorphism group.

**Definition 3.1 (Scaling transformation).** A *scaling transformation* of $X$ is a homomorphism $s: \mathbb{R} \to \mathrm{Aut}(X)$ (continuous case) or $s: \mathbb{Z} \to \mathrm{Aut}(X)$ (discrete case) together with a distinguished object $C_X$ attached to $X$ (a cone, a grading $\bigoplus_i X_i$, a filtration, or a metric) such that each $s_t$ acts on $C_X$ by rescaling: there exist quantities $q_i$ indexed by the pieces of $C_X$ with

$$q_i(s_t(x)) = e^{\alpha_i t}\, q_i(x)$$

for exponents $\alpha_i \in \mathbb{R}$ determined by $s$.

**Definition 3.2 (Scaling-compatible automorphism).** An automorphism $f \in \mathrm{Aut}(X)$ is *scaling-compatible* if $f$ normalizes the image of some scaling transformation $s$, i.e., $f \, s_t \, f^{-1} = s_{c(t)}$ for some automorphism $c$ of the parameter group. In the discrete case with $s$ of cyclic image of order $k$, normalization forces $c$ to be multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$.

**Definition 3.3 (Re-entry map).** A *re-entry* of a structure $X$ into a context $Y$ is a functor- or homomorphism-level assignment $\Phi: \mathrm{Aut}(X) \to \mathrm{Aut}(Y)$ (or to $\mathrm{Aut}$ of a graded object associated to $Y$) such that scaling-compatible elements of $\mathrm{Aut}(X)$ map to scaling-compatible elements of $\mathrm{Aut}(Y)$. The question of the paper is when re-entry maps exist and what they preserve.

### 3.2 Method of survey-and-count

Because the supplied source material consists of abstracts, our method is necessarily conservative: (i) extract from each abstract the structural claims it explicitly makes about an automorphism group or a scaling-like construction; (ii) where the abstract supplies integer counts (as in [2] and [5]), compute derived invariants with full arithmetic; (iii) where the abstract is truncated or silent, record the gap and use the entry only at the level of its explicit statements. No claim in this paper about a cited work goes beyond its supplied summary.

### 3.3 Toy invariant

For a Cayley–Dickson algebra $A$ of real dimension $D$ carrying $N$ associative quaternion rings (in the sense of [2]), we define the *ring density*

$$\delta(A) = \frac{N}{D},$$

and the *density growth factor* between two algebras $A_1, A_2$ as $\delta(A_2)/\delta(A_1)$. This is a toy quantity: it measures how the associative substructure scales relative to raw dimension under the Cayley–Dickson doubling, and it is the concrete hook on which the scaling/automorphism question is tested numerically in Section 4.

## 4. Analysis

All inputs below are stated with their sources; all arithmetic is shown step by step.

### 4.1 Cayley–Dickson dimensions

**Input (source [2]).** The octonions and sedenions are Cayley–Dickson algebras; the construction proceeds by repeated doubling. The octonions sit three doubling steps above the reals and the sedenions four.

**Derivation.** Each doubling step sends real dimension $D$ to $2D$, so after $d$ steps the dimension is

$$D_d = 2^{d}.$$

For the octonions ($d = 3$):

$$D_3 = 2^{3} = 8.$$

For the sedenions ($d = 4$):

$$D_4 = 2^{4} = 16.$$

The dimension growth factor is

$$\frac{D_4}{D_3} = \frac{16}{8} = 2.$$

This confirms that the Cayley–Dickson construction is a discrete scaling of dimension with ratio exactly $2$ per step.

### 4.2 Associative quaternion ring counts

**Input (source [2]).** The octonions consist of seven quaternion rings and the sedenions have $35$ rings:

$$N_3 = 7, \qquad N_4 = 35.$$

**Derivation (ring growth factor).**

$$\frac{N_4}{N_3} = \frac{35}{7} = 5.$$

So while dimension scales by $2$ per doubling step, the count of associative quaternion rings scales by $5$ over the same step (from octonions to sedenions). The two scaling rates disagree: ring count grows faster than dimension.

### 4.3 Ring density and density growth

**Derivation (octonion density).** Using Definition 3.3 with $D_3 = 8$ and $N_3 = 7$:

$$\delta(\mathbb{O}) = \frac{N_3}{D_3} = \frac{7}{8} = 0.875.$$

**Derivation (sedenion density).** With $D_4 = 16$ and $N_4 = 35$:

$$\delta(\mathbb{S}) = \frac{N_4}{D_4} = \frac{35}{16} = 2.1875.$$

**Derivation (density growth factor).**

$$\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})} = \frac{2.1875}{0.875} = 2.5.$$

Equivalently, and exactly:

$$\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})} = \frac{N_4 / D_4}{N_3 / D_3} = \frac{N_4}{N_3} \cdot \frac{D_3}{D_4} = 5 \cdot \frac{8}{16} = 5 \cdot \frac{1}{2} = 2.5.$$

**Interpretation.** Under one Cayley–Dickson doubling, the density of associative quaternion subalgebras per real dimension grows by exactly $2.5$. This is a concrete, checkable instance of the paper's thesis: a scaling transformation of the ambient object (dimension doubling) does not scale the automorphism-relevant substructure (calibration rings) linearly; the mismatch factor here is $5/2$.

### 4.4 Combinatorics of free-product splittings

**Input (source [5]).** The group studied consists of outer automorphisms preserving the conjugacy classes of the free factors $G_i$ of $G_1 \ast \dots \ast G_n$, with a "symmetric" permutation action on those classes.

**Derivation (permutation counts).** The set of factor conjugacy classes has $n$ elements, so the symmetric group on it has order

$$|S_n| = n!$$

For the first few values:

$$3! = 3 \cdot 2 \cdot 1 = 6, \qquad 4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24, \qquad 5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120.$$

These are combinatorial counts of the maximal possible permutation scope of the symmetric condition, not claims that the group of [5] achieves these orders; the paper's actual group is presented via a simply connected subcomplex of Outer Space, and the supplied summary gives no group order. The count $n!$ serves as the natural combinatorial ceiling against which any scaling decomposition of the pure symmetric outer automorphism group would be measured.

### 4.5 Picard number two: cone combinatorics

**Input (source [1]).** The varieties considered have Picard number two, i.e., $\rho(X) = 2$.

**Derivation (face count of a 2-dimensional cone).** A strictly convex closed cone in a real vector space of rank $\rho = 2$ has faces of each dimension $0, 1, 2$: the apex, the extreme rays, and the cone itself. The number of faces of dimension $k$ in a simplicial 2-cone is $\binom{2}{k}$, so the total face count is

$$F = \binom{2}{0} + \binom{2}{1} + \binom{2}{2} = 1 + 2 + 1 = 4.$$

Thus the cone object on which $\mathrm{Aut}(X)$ acts in the setting of [1] has exactly $4$ faces and $2$ extreme rays. This smallness is what makes the almost-cyclic dichotomy of [1] plausible: a discrete group acting faithfully on a $2$-ray cone has very little room beyond cyclic behavior, which is consistent with the summary's dichotomy (almost cyclic, or the truncated alternative).

### 4.6 Scaling-compatibility in the discrete cyclic case

**Derivation (unit group size).** By Definition 3.2, if $s: \mathbb{Z} \to \mathrm{Aut}(X)$ has cyclic image of order $k$, a scaling-compatible $f$ induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$. The number of units is given by Euler's totient function $\varphi(k)$. For the smallest nontrivial cyclic orders:

$$\varphi(2) = 1, \qquad \varphi(3) = 2, \qquad \varphi(4) = 2, \qquad \varphi(5) = 4, \qquad \varphi(6) = 2.$$

(For example, $\varphi(5) = 5 - 1 = 4$ since $5$ is prime; $\varphi(6) = |\{1,5\}| = 2$.) Consequently, for cyclic scaling subgroups of prime order $p$, the scaling-compatible automorphisms can rescale the parameter by any of $p - 1$ nonzero residues, while for $k = 2$ the only possibility is the identity rescaling. This gives a sharp, computable constraint: **discrete scaling of order $2$ admits no nontrivial parameter rescaling**, which will matter in Section 5 when we connect the doubling step of Section 4.1 (ratio exactly $2$) to the automorphism side.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (Dimension scaling, exact).** Under Cayley–Dickson doubling, real dimensions go $D_3 = 2^3 = 8$ (octonions) to $D_4 = 2^4 = 16$ (sedenions); growth factor $16/8 = 2$. Source of inputs: [2].

**R2 (Ring-count scaling, exact).** Associative quaternion ring counts go $N_3 = 7$ to $N_4 = 35$; growth factor $35/7 = 5$. Source of inputs: [2].

**R3 (Ring density, exact).** $\delta(\mathbb{O}) = 7/8 = 0.875$; $\delta(\mathbb{S}) = 35/16 = 2.1875$; density growth factor $= 2.5$ exactly (equivalently $5 \times 1/2$). Source of inputs: [2]; formula defined in Section 3.3.

**R4 (Cone combinatorics, exact).** For Picard number $\rho = 2$ (source [1]), a simplicial 2-cone has $2$ extreme rays and $1 + 2 + 1 = 4$ faces.

**R5 (Permutation ceiling, exact).** For a free-product splitting with $n$ factors (source [5]), the symmetric-group ceiling on factor permutation is $n!$: $6$ for $n=3$, $24$ for $n=4$, $120$ for $n=5$. This is a combinatorial ceiling, not a group order.

**R6 (Discrete-scaling rigidity, exact).** A cyclic scaling subgroup of order $k$ admits $\varphi(k)$ parameter rescalings; in particular $\varphi(2) = 1$, so order-$2$ discrete scaling admits no nontrivial rescaling of its own parameter.

**Projection P1 (labeled as a projection, not a computation).** If the ring-count growth factor of $5$ per doubling step were to persist for the next Cayley–Dickson step (the algebra beyond the sedenions, of dimension $2^5 = 32$), the ring count would be $35 \times 5 = 175$ and the density would be $175/32 = 5.46875$. **Assumptions and uncertainty:** the supplied summary of [2] states counts only for octonions and sedenions; the factor-$5$ persistence is an unverified extrapolation of a single observed step, and the true count at the next level could differ arbitrarily. We state this projection solely to make the framework's predictive content explicit and falsifiable.

**Qualitative results.** (Q1) The corpus exhibits scaling structure in three distinct guises: literal dimension doubling ([2]), cone/grading geometry ([1], [3], [4]), and translation-type dynamics ([8]). (Q2) The automorphism side exhibits rigidity in three matching guises: the almost-cyclic dichotomy ([1]), order bounds for curve automorphisms ([6]), and descent criteria for induced automorphisms ([7]). (Q3) The mismatch between ambient scaling (factor $2$) and structural scaling (factor $5$; density factor $2.5$) in [2] is the sharpest quantitative signal that automorphism-relevant structure does not scale linearly with its ambient object.

## 6. Discussion

**Limitations.** The most serious limitation is evidential: our contact with the cited mathematics is through supplied abstracts, several of which are truncated mid-sentence ([1], [2], [4], [7], [8]). Where a truncation cuts off the second branch of a dichotomy ([1]) or the conclusion of a construction ([2]), we have deliberately not guessed the missing content. Entry [6] supplies no numerical bound, so our use of it is purely qualitative. Entries [9]–[12] have empty summaries; everything we say about them rests on titles alone, and the ultrametric-physics motivation of the re-entry question is therefore carried by title-level connection, not by documented content.

**Failure modes of the framework.** Definition 3.1 requires a distinguished object $C_X$ on which the scaling acts by rescaling. For many structures in the corpus — e.g., the free-product splittings of [5] — no canonical cone or grading is supplied by the source, so the framework does not even get started there; our treatment of [5] is combinatorial, not scaling-theoretic. Second, Definition 3.2's normalization condition is sufficient but not necessary for "relates to scaling"; a group could relate to scalings in a weaker sense (e.g., quasi-isometrically) that our definition misses. Third, the toy density $\delta(A)$ is sensitive to the choice of denominator; we chose raw dimension, but a denominator based on the number of independent associative triples would change the growth factor.

**Arguing against ourselves.** The strongest objection to the paper's thesis is that the factor-$5$ ring growth in [2] may be an accident of small-dimension exceptional arithmetic (octonions and sedenions are low-dimensional exceptional objects) rather than the first term of a scaling law. Projection P1 makes this objection testable: if the next-level ring count is not $175$, the "scaling law" reading collapses to an isolated observation. A second objection is that the almost-cyclic dichotomy of [1] concerns varieties that are *not* complex tori; tori, which are excluded, are precisely the structures with the most literal scaling automorphisms (multiplication by units), so the dichotomy may be carving scaling behavior out rather than capturing it. We cannot resolve this from the supplied summary, which truncates before stating the alternative branch. A third objection: our re-entry map concept (Definition 3.3) is stated but never instantiated with a proved example in this paper; the numerical results R1–R3 concern a construction (Cayley–Dickson doubling) that is scaling-like, but we have not exhibited a single concrete homomorphism $\Phi$ between two of the corpus's automorphism groups. The honest summary of the paper's status is therefore: a vocabulary, a set of exact small computations, and falsifiable projections — not a theorem about automorphisms and scaling.

**What would falsify the claims.** (F1) If the ring counts at Cayley–Dickson levels beyond the sedenions do not follow any regular multiple-close pattern, R3's density-growth reading as a scaling law is falsified. (F2) If a Picard-number-two klt variety in the setting of [1] has an automorphism group that is provably neither almost cyclic nor compatible with any $\mathbb{Z}$-action on its cone, the framework's central compatibility notion fails in its intended home. (F3) If the fixed-locus/divisor hypothesis of [3] fails for a natural nonsymplectic automorphism group, the cone-compatibility route from automorphisms to scaling geometry is blocked in the K3 setting.

**Open questions.** (O1) What is the exact ring count at Cayley–Dickson level $5$, and does a formula exist interpolating $7$ and $35$? (O2) Does the truncated second branch of the dichotomy in [1] admit a scaling interpretation? (O3) Can the Outer Space subcomplex of [5], shown simply connected there, be equipped with a metric making the pure symmetric outer automorphism action scaling-compatible in the sense of Definition 3.2? (O4) Do the translation-conjugating biholomorphisms of [8] induce re-entry maps between the dynamics on $\Omega \cong \mathbb{C} \times \mathbb{C}^{*}$ and scaling actions on the invariant curve?

## 7. Conclusion

We posed the re-entry question — how automorphisms relate to scaling transformations — and gave it a precise vocabulary (Definitions 3.1–3.3), a conservative survey of twelve