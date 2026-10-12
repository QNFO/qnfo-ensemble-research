# Non-Computable Reals as Projection Artifacts: A Formal Framework for Tree-to-Manifold Construction of the Continuum

## Abstract

We develop a formal framework for the conjecture that the continuum is constructed rather than primitive: natural numbers, rationals, and computable reals arise from a single distinction operator via enclosure operations, while the full real line emerges only through a lossy projection — the Monna-map — of a discrete, non-Archimedean Bruhat–Tits tree onto a smooth Archimedean manifold. The central claim under analysis is that non-computable reals are not discovered but created by this projection: they are artifacts with no discrete counterpart, analogous to upsampling artifacts in signal generation. We formalize the distinction operator, define the projection, and prove which reals it adds. We derive with explicit arithmetic that the computable reals form a set of Lebesgue measure zero, so the artifact set has full measure, explaining the measure-theoretic dominance of non-computables as a projection effect rather than a physical fact. We quantify the gap between finite-depth tree approximations and their Archimedean shadows: at tree depth $n = 20$, exactly definable rational shadows number $129$ against $2^{20} = 1{,}048{,}576$ total paths, a definable fraction of $\approx 1.23 \times 10^{-4}$. We connect the framework to Spencer-Brown-style distinction logic, to rational-interval definitions of reals, and to projection theory, and state the open problems and falsification conditions.

## 1. Introduction

The standard set-theoretic presentation treats the real line $\mathbb{R}$ as a completed object, with the non-computable reals $\mathbb{R} \setminus \mathbb{R}_{\mathrm{comp}}$ as an uncountable majority whose existence is guaranteed by completeness. This paper takes the opposite stance, following the research program sketched in the QNFO corpus: the continuum is not primitive but constructed. A single distinction operator — the act of drawing a boundary, in the sense of Spencer-Brown's *Laws of Form* [9] — generates the natural numbers by iterated enclosure; enclosure operations on distinctions generate the rationals; and limits of rational procedures generate the computable reals $\mathbb{R}_{\mathrm{comp}}$. The full continuum $\mathbb{R}$ then emerges only at the last step, through a projection of a discrete, non-Archimedean structure onto a smooth Archimedean manifold.

The specific construction we analyze is a tree-to-manifold projection. The discrete side is a Bruhat–Tits tree: an infinite, non-Archimedean object in which "closeness" is measured by a non-Archimedean valuation rather than by an Archimedean metric. The Archimedean side is the familiar real line. The projection — which we call the Monna-map, following the corpus terminology [11] — is lossy: many distinct tree paths map to the same, or to no well-defined, Archimedean point. The key conjecture is that the non-computable reals live entirely on the Archimedean side of this map. They have no discrete counterpart: they are artifacts of projection, in the same sense that upsampling a signal can create spectral or visual features that exist in the output format but not in the source data [1], [5].

This reframing has two payoffs. First, it re-derives the computable/constructive hierarchy from pure distinction logic: the boundary between $\mathbb{R}_{\mathrm{comp}}$ and $\mathbb{R} \setminus \mathbb{R}_{\mathrm{comp}}$ becomes the boundary between what the discrete tree can encode and what only the projection can produce. Second, it explains the measure-theoretic dominance of non-computables — the fact that a uniformly random point of $[0,1]$ is non-computable with probability $1$ — as a projection effect: the projection adds a full-measure set of artifacts, while everything the tree actually encodes has measure zero. The corpus position that non-computable breadth is "physically vacuous" [10], [11] is thereby given a quantitative skeleton.

Our contributions are: (i) a precise definition of the distinction operator, the enclosure hierarchy, and the Monna-map projection (Section 3); (ii) explicit derivations showing that the computable reals have Lebesgue measure zero, that the artifact set has full measure, and that the density of finitely definable rational shadows among tree paths decays exponentially in tree depth (Section 4); (iii) a statement of results, projections, and their uncertainty (Section 5); and (iv) a discussion of limitations, failure modes, and falsification conditions (Section 6).

## 2. Background and Related Work

We organize the related work into four strands: artifacts produced by representational projection, alternative constructions of the reals, distinction-based foundations, and projection theory in mathematics.

**Artifacts of lossy representation.** Biswas and Paris report that upsampling layers in neural audio synthesis introduce undesired artifacts, and that while such artifacts are well studied in computer vision — where they are known as checkerboard artifacts due to their characteristic visual pattern — their effect had been overlooked in audio processing [1]. This is the closest methodological analogue to our thesis: a change of representational substrate (discrete samples to a continuous percept) creates features that exist only in the output format. In the image domain, the StyleGAN literature documents the same phenomenon: vanilla StyleGAN synthesizes high-resolution, hyper-realistic face images, but these sometimes contain prominent circular artifacts which severely degrade the quality of generated images, and one work provides a systematic investigation of how those circular artifacts arise and how to remove them [5]. Both [1] and [5] support the general principle we invoke: when a generator projects internal discrete structure onto a continuous output manifold, the projection itself can be the source of structured, systematic defects. Our claim is that $\mathbb{R} \setminus \mathbb{R}_{\mathrm{comp}}$ is exactly such a systematic defect of the tree-to-manifold projection.

**The artifact concept beyond engineering.** The notion that artifacts are not mere noise but carry structural consequences has been argued in mathematics itself: one paper extends Langdon Winner's idea that artifacts have politics into the realm of mathematics, first providing examples showing the existence of mathematical artifacts that have politics, then arguing that all mathematical artifacts have politics, and concluding with implications for embedding ethics into mathematical curricula [4]. Whatever one makes of the normative thesis, the descriptive core — that mathematical objects can be artifacts of the machinery that produces them, with real consequences — is precisely the ontology we assign to non-computable reals. On the practical side, the reproducibility literature emphasizes that the design and preparation of reproducible artifacts has a fundamental role in the development of science, given challenges of transparency, reliability, and reproducibility of empirical published results [3]; we adopt the corresponding methodological demand that every construction in this paper be reproducible from explicitly stated finite data — which, notably, is exactly the definition of computability.

**Alternative constructions of the reals.** The rational-interval definition of reals states that a real number is a rule which says Yes or No based on whether the real number ought to be in a given rational interval; that paper is a teaser for a fuller formalization under the title "Defining Real Numbers as Oracles" [7]. This is convergent with our framework: a real is a decision procedure over rational intervals, i.e., a finite-rule object on the discrete side of the projection. The supplied summary of [7] gives no further technical detail, so we use it only as evidence that rule-based definitions of reals are an active alternative to set-theoretic completion. In classical analysis, fractional calculus reviews applications to continuum and statistical mechanics, including mathematical modelling of viscoelastic bodies and the Basset problem of unsteady motion of a particle in a viscous fluid [2]; we cite it as evidence that continuum mechanics routinely employs operators (fractional derivatives) that do not reduce to pointwise classical operations — a precedent for continuum descriptions that presuppose a richer structure than the discrete one, which is the direction of our projection.

**Projection theory.** In operator algebra, a substantial literature studies projections on C*-algebras and their ranges; one paper's main goal is to find operator algebra variants of deep results of Stormer, Friedman and Russo, Choi and Effros, Effros and Stormer, Robertson and Youngson, Youngson, and others, investigating in particular the bicontractive projection problem [8]. This establishes that "which subobjects survive a projection, and what the projection's range looks like" is a mathematically deep question with a developed theory; our Monna-map is a set-theoretic and measure-theoretic instance of the same genre of question. Finally, in combinatorics, two related conjectures arising from i-matchings in random r-regular bipartite graphs involve only basic properties of convergent power series, one formulation involving Bell polynomials; the authors state they believe only a truly genius mathematician will prove them and advise others not to try [6]. We cite [6] as a cautionary register: our central conjectures are similarly easy to state and may be similarly hard, and we flag which of our claims are theorems (with derivations) and which remain conjecture.

**Distinction-based foundations.** Spencer-Brown's *Laws of Form* (1969) proposed the act of drawing a distinction as the primitive operation from which logic, mathematics, and physics can be constructed; a consolidation synthesizes known quantum correspondences, identifies 7 open problem categories, and proposes 4 extensions [9]. Our distinction operator is a direct formalization of this primitive. The QNFO corpus supplies the specific thesis we analyze: that the uncountability of the reals conflates Archimedean completeness (depth) and set-theoretic cardinality explosion (breadth), with all physically relevant properties preserved by computable reals [10]; and the three-axis framework of Depth (computable reals), Breadth (non-computable reals, described as physically vacuous), and Valuation (p-adic completions as information carriers), with falsifiable predications for quantum error correction and gauge structure [11]. The entry for "Syntactic Generation" [12] carries no substantive summary text, so we note only that it belongs to the same corpus and that its title suggests a generation-by-syntax program consonant with our enclosure hierarchy; we make no claim about its contents.

## 3. Methods

### 3.1 The distinction operator and enclosure hierarchy

Following [9], we take as primitive the act of drawing a distinction. Formally, fix a two-value form $V_2 = \{0, 1\}$ and let the distinction operator $\delta$ be a map that, applied to an unmarked space, produces a marked and an unmarked region. Iterated application generates a rooted binary structure.

**Definition 3.1 (Enclosure hierarchy).** Define inductively:
- $E_0 = \{\varnothing\}$, the undifferentiated space.
- $E_{k+1} = \mathcal{P}_{\mathrm{fin}}(E_k)$, finite enclosures of level-$k$ objects.

Level-$1$ objects correspond to single distinctions; finite multisets of level-$1$ distinctions, ordered by iteration, yield the natural numbers $\mathbb{N}$. Pairwise enclosure of naturals with an orientation yields the integers $\mathbb{Z}$ and then the rationals $\mathbb{Q}$ as ordered pairs $(p, q)$ with $q \neq 0$, $q \in \mathbb{N}$, modulo the usual identification $(p_1, q_1) \sim (p_2, q_2)$ iff $p_1 q_2 = p_2 q_1$. Every element of this hierarchy is finitely specifiable: it is a finite syntactic object built by $\delta$ and enclosure.

### 3.2 The discrete side: a Bruhat–Tits tree

**Definition 3.2 (Valuation tree).** Fix a prime $p$ and let $T_p$ be the Bruhat–Tits tree of $\mathbb{Q}_p$: the tree whose vertices at level $n$ correspond to residue classes mod $p^{n+1}$, each vertex having $p$ children. A path from the root is an element of the boundary $\partial T_p$, which carries a natural ultrametric $d_p$ induced by the $p$-adic valuation $v_p$. The corpus framework [11] treats such $p$-adic completions as information carriers (the Valuation axis); here they serve as the canonical discrete substrate.

For concreteness and computability of all counts, we work primarily with the binary tree $T_2$ ($p = 2$), whose boundary $\partial T_2$ is in bijection with infinite binary sequences.

### 3.3 The Monna-map projection

**Definition 3.3 (Monna-map).** The Monna-map is the projection
$$\mu : \partial T_2 \to [0, 1], \qquad \mu\big((b_1, b_2, b_3, \ldots)\big) = \sum_{k=1}^{\infty} b_k \, 2^{-k},$$
i.e., the standard binary-expansion identification of the Cantor-set boundary with the unit interval. It is the Archimedean shadow of the non-Archimedean boundary: the tree carries the ultrametric $d_2$, the interval carries the Euclidean metric $d_{\infty}(x, y) = |x - y|$, and $\mu$ is continuous from the ultrametric topology onto the Euclidean topology but is many-to-one on a countable set (the dyadic rationals, which have two expansions) and collapses all ultrametric structure.

**Definition 3.4 (Computable shadow, artifact set).** A point $x \in [0,1]$ is a *computable shadow* if there is a finite program (equivalently, a finite rule in the sense of [7]) that, given $n$, outputs the first $n$ bits of a binary expansion of $x$. Let $\mathbb{R}_{\mathrm{comp}}[0,1]$ denote the set of computable shadows. The *artifact set* is
$$A = [0,1] \setminus \mathbb{R}_{\mathrm{comp}}[0,1].$$
The central conjecture of the research program is: **(C)** every element of $A$ has no counterpart on the discrete side — it is created by $\mu$, not discovered in $\partial T_2$ — because a discrete counterpart would be an infinite path with a finite specification, which is exactly the definition of a computable shadow.

### 3.4 Method of analysis

We do not simulate; we derive. All quantitative claims in Section 4 follow from three inputs: (i) the countability of finite programs, (ii) the countability of $\mathbb{Q}$ and the Farey counting function, and (iii) the exact enumeration of binary-tree paths at finite depth. Each derivation shows its inputs, formula, and arithmetic.

## 4. Analysis

### 4.1 Input numbers and their sources

- $I_1$: The number of binary strings of length exactly $k$ is $2^k$ (combinatorial identity; the tree $T_2$ has $2^k$ nodes at depth $k$).
- $I_2$: The number of reduced fractions in $[0,1]$ with denominator at most $n$ is $|F_n| = 1 + \sum_{k=1}^{n} \varphi(k)$, where $F_n$ is the Farey sequence of order $n$ and $\varphi$ is Euler's totient (standard Farey identity; each fraction $a/k$ with $\gcd(a,k)=1$, $0 \le a \le k$, contributes, and $\varphi(k)$ counts them for each $k$, plus the endpoint $0/1$).
- $I_3$: Euler's totient values for $k = 1, \ldots, 20$, computed directly: $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$, $\varphi(7)=6$, $\varphi(8)=4$, $\varphi(9)=6$, $\varphi(10)=4$, $\varphi(11)=10$, $\varphi(12)=4$, $\varphi(13)=12$, $\varphi(14)=6$, $\varphi(15)=8$, $\varphi(16)=8$, $\varphi(17)=16$, $\varphi(18)=6$, $\varphi(19)=18$, $\varphi(20)=8$. Each $\varphi(k)$ is the count of integers in $[1,k]$ coprime to $k$, verified by direct listing (e.g., $\varphi(10)$: coprime to $10$ are $1, 3, 7, 9$, so $\varphi(10) = 4$).
- $I_4$: The number of binary programs of length at most $L$ is $\sum_{k=0}^{L} 2^k = 2^{L+1} - 1$ (geometric sum).

### 4.2 Derivation 1: the computable shadows have measure zero

Every computable shadow is specified by a finite program. By $I_4$, the number of programs of length at most $L$ is $N_L = 2^{L+1} - 1$. Each program determines at most one real in $[0,1]$. Hence the set $C_L$ of reals computable by programs of length $\le L$ satisfies $|C_L| \le 2^{L+1} - 1$. A finite set has Lebesgue measure zero, so
$$\lambda(C_L) = 0 \quad \text{for every finite } L.$$
The set of all computable shadows is $\mathbb{R}_{\mathrm{comp}}[0,1] = \bigcup_{L=0}^{\infty} C_L$, a countable union of measure-zero sets, so by countable subadditivity of Lebesgue measure,
$$\lambda\big(\mathbb{R}_{\mathrm{comp}}[0,1]\big) \le \sum_{L=0}^{\infty} \lambda(C_L) = \sum_{L=0}^{\infty} 0 = 0.$$
Therefore $\lambda(\mathbb{R}_{\mathrm{comp}}[0,1]) = 0$, and since $\lambda([0,1]) = 1$,
$$\lambda(A) = \lambda([0,1]) - \lambda(\mathbb{R}_{\mathrm{comp}}[0,1]) = 1 - 0 = 1.$$
The artifact set has full measure. This is the formal content of the claim that the measure-theoretic dominance of non-computables is a projection effect: everything the discrete side finitely encodes occupies measure zero of the shadow; the projection adds the rest.

### 4.3 Derivation 2: definable rationals versus tree paths at finite depth

At depth $n$, the tree $T_2$ has $2^n$ nodes (by $I_1$), hence $2^n$ candidate finite path-prefixes whose natural Archimedean shadows are the dyadic rationals $m/2^n$. The finitely specifiable rational shadows of *arbitrary* denominator up to $n$ number $|F_n| = 1 + \sum_{k=1}^{n} \varphi(k)$ (by $I_2$, $I_3$).

For $n = 10$: the totient sum is
$$\sum_{k=1}^{10} \varphi(k) = 1+1+2+2+4+2+6+4+6+4 = 32,$$
so $|F_{10}| = 1 + 32 = 33$. The path count is $2^{10} = 1024$. The definable fraction is
$$f_{10} = \frac{33}{1024} \approx 0.032227.$$

For $n = 20$: continuing the cumulative sum,
$$\sum_{k=1}^{20} \varphi(k) = 32 + 10 + 4 + 12 + 6 + 8 + 8 + 16 + 6 + 18 + 8 = 128,$$
so $|F_{20}| = 1 + 128 = 129$. The path count is $2^{20} = 1{,}048{,}576$. The definable fraction is
$$f_{20} = \frac{129}{1{,}048{,}576} \approx 1.2307 \times 10^{-4}.$$

The growth comparison: $|F_n| = 1 + \sum_{k=1}^{n} \varphi(k)$ grows polynomially (asymptotically $\sim \frac{3}{\pi^2} n^2$, with $\frac{3}{\pi^2} \approx 0.303961$), while $2^n$ grows exponentially. The ratio
$$f_n = \frac{1 + \sum_{k=1}^{n} \varphi(k)}{2^n} \longrightarrow 0 \quad \text{as } n \to \infty,$$
with exponential decay rate dominated by the factor $2^{-n}$. As a labeled projection with stated assumptions: assuming the asymptotic $\sum_{k=1}^{n}\varphi(k) \approx \frac{3}{\pi^2}n^2$ holds with relative error below a factor of $2$ for $n \ge 100$ (a conservative assumption; the totient summatory function is known to fluctuate around this constant), we project $f_{100} \approx \frac{0.303961 \times 100^2}{2^{100}} = \frac{3039.61}{1.26765 \times 10^{30}} \approx 2.40 \times 10^{-27}$, with an uncertainty bound of one order of magnitude in either direction from the totient fluctuation. This is a projection, not a computation from exact totient values.

### 4.4 Derivation 3: program-count gap

By $I_4$, programs of length at most $L = 100$ number $2^{101} - 1$. Computing: $2^{10} = 1024$, $2^{20} = 1{,}048{,}576$, $2^{100} = (2^{10})^{10} = 1024^{10}$. Then $2^{101} = 2 \times 1024^{10}$. Using $1024^{10} = (2^{10})^{10} = 2^{100} \approx 1.267651 \times 10^{30}$ (since $2^{100} = 1{,}267{,}650{,}600{,}228{,}229{,}401{,}496{,}703{,}205{,}376$ exactly, obtained by repeated squaring: $2^{10}=1024$, $2^{20}=1024^2 = 1{,}048{,}576$, $2^{40} = 1{,}048{,}576^2 = 1{,}099{,}511{,}627{,}776$, $2^{80} = (2^{40})^2 = 1{,}208{,}925{,}819{,}614{,}629{,}174{,}706{,}176$, and $2^{100} = 2^{80} \times 2^{20} = 1{,}208{,}925{,}819{,}614{,}629{,}174{,}706{,}176 \times 1{,}048{,}576 = 1{,}267{,}650{,}600{,}228{,}229{,}401{,}496{,}703{,}205{,}376$). Hence
$$N_{100} = 2^{101} - 1 = 2{,}535{,}301{,}200{,}456{,}458{,}802{,}993{,}406{,}410{,}751 \approx 2.535 \times 10^{30}.$$
Against the continuum cardinality of $[0,1]$, this count is not merely small — by Derivation 1 it is measure-theoretically negligible: even the union over all finite $L$ has measure $0$.

### 4.5 Derivation 4: the dyadic collapse of the Monna-map

The Monna-map $\mu$ is exactly two-to-one on the dyadic rationals $\{m/2^n\}$: the two expansions $0.b_1\ldots b_{n-1}1000\ldots$ and $0.b_1\ldots b_{n-1}0111\ldots$ both map to $m/2^n$. The number of dyadic rationals in $[0,1)$ with denominator $2^n$ is $2^n$ (values $m/2^n$, $m = 0, \ldots, 2^n - 1$), so the collision set at level $n$ has size $2^n$ while the path set has size $2^{n+1}$ counting both tails; the collision fraction of path-pairs is
$$c_n = \frac{2^n}{2^{n+1}} = \frac{1}{2}.$$
That is, at every depth, half of the local path structure is redundant under $\mu$ — a concrete, exactly computable instance of the projection's lossiness. All non-dyadic points, which constitute the full-measure artifact set of Derivation 1, have a unique preimage pair structure only in the limit; at any finite depth they are invisible.

## 5. Results

We report only quantities derived in Section 4, plus clearly labeled projections.

**R1 (Theorem, derived).** The computable shadows in $[0,1]$ form a set of Lebesgue measure exactly $0$; the artifact set $A$ has measure exactly $1$ (Section 4.2).

**R2 (Computed).** At tree depth $n = 10$: $|F_{10}| = 33$ definable rational shadows versus $2^{10} = 1024$ path-nodes; definable fraction $f_{10} = 33/1024 \approx 0.032227$. At $n = 20$: $|F_{20}| = 129$ versus $2^{20} = 1{,}048{,}576$; $f_{20} = 129/1{,}048{,}576 \approx 1.2307 \times 10^{-4}$ (Section 4.3).

**R3 (Computed).** Programs of length $\le 100$: $N_{100} = 2^{101} - 1 = 2{,}535{,}301{,}200{,}456{,}458{,}802{,}993{,}406{,}410{,}751 \approx 2.535 \times 10^{30}$ (Section 4.4).

**R4 (Computed).** The Monna-map is two-to-one on dyadic rationals at every level; the local collision fraction is $c_n = 1/2$ for all $n$ (Section 4.5).

**R5 (Projection, labeled).** Assuming the asymptotic $\sum_{k=1}^{n}\varphi(k) \approx \frac{3}{\pi^2}n^2$ with relative error below a factor of $2$ for $n \ge 100$, we project $f_{100} \approx 2.40 \times 10^{-27}$ with an uncertainty of one order of magnitude in either direction. This is not a computation from exact totient values and should be treated as an order-of-magnitude estimate only.

**R6 (Conjecture, not derived).** Conjecture (C) of Section 3.3 — that every artifact has no discrete counterpart — is supported by the definitional argument (a discrete counterpart with finite specification would be a computable shadow) but is not proved here as a theorem about an independently formalized Monna-map beyond the binary model; see Section 6.

## 6. Discussion

**Limitations.** First, our Monna-map is the binary-expansion map, which is the simplest tree-to-manifold projection; the corpus's Monna-map may be intended more generally (e.g., over arbitrary $p$-adic trees $T_p$ with the Valuation axis of [11] as information carriers). Conjecture (C) is proved here only in the sense that any finitely specified path is a computable shadow by definition; a stronger theorem — that no non-computable real arises from any discrete-side construction whatsoever — would require a formalization of "discrete counterpart" that is independent of computability, which we have not supplied. Second, the measure-zero result (R1) is standard in substance; its contribution here is interpretive, locating the standard fact inside the projection picture rather than deriving new measure theory. Third, the finite-depth counts (R2) compare rational shadows of denominator $\le n$ against binary path-nodes at depth $n$ — two different depth conventions. A critic could insist on comparing $|F_n|$ against $2^n$ only when the tree encodes base-$n$ rather than base-$2$ expansions; under that convention the numbers change, though the qualitative exponential-versus-polynomial gap does not.

**Failure modes.** The framework fails if non-computable reals can be given finite specifications in a system stronger than Turing computation that is still "discrete" in the relevant sense — e.g., if the distinction operator $\delta$ is granted infinitary enclosure acts. Then the boundary between $\mathbb{R}_{\mathrm{comp}}$ and $A$ would shift, and the artifact thesis would need restatement relative to the stronger system. It also fails if physical measurement can access non-computable values directly, which would contradict the corpus's "physically vacuous" predication [10], [11]; the falsifiable predications for quantum error correction and gauge structure proposed in [11] are the natural empirical test bed, though we do not evaluate them here.

**What would falsify the claims.** R1–R4 are mathematical consequences of standard definitions and cannot be falsified, only their interpretation challenged. The interpretive claim — that non-computables are *created* by projection rather than *discovered* — would be undermined by a constructive, finitary procedure that produces a provably non-computable real without passing through an Archimedean completion step; no such procedure is known to us, and its existence would be a genuine refutation. The projection $f_{100} \approx 2.40 \times 10^{-27}$ (R5) would be falsified by exact computation of $\sum_{k=1}^{100}\varphi(k)$ differing from $\frac{3}{\pi^2} \cdot 100^2$ by more than the stated factor-of-$2$ bound.

**Open questions.** (1) Does the artifact set $A$ carry additional structure under $\mu$ — e.g., is it invariant under the tree's automorphism group in a sense that explains its full measure? (2) What is the correct multi-prime generalization, combining $T_p$ for several $p$ as in the Valuation axis [11]? (3) Can the bicontractive-style range analysis of projections [8] be transported to $\mu$ to characterize the range's operator-theoretic properties? (4) Following the caution of [6], we note that sharpening Conjecture (C) into a theorem may be substantially harder than stating it; we advise treating it as a research program, not a result.

## 7. Conclusion

We have given a formal skeleton for the conjecture that the continuum is constructed by projection. The distinction operator and enclosure hierarchy generate the finitely specifiable numbers; the Monna-map projects the Bruhat–Tits boundary onto the unit interval; and the projection is provably lossy in three exact senses: the computable shadows have measure zero while the artifact set has full measure, the definable rational fraction of tree paths decays from $0.032227$ at depth $10$ to $1.2307 \times 10^{-4}$ at depth $20$, and the map is two-to-one on half of all local path structure at every depth. On this picture, the non-computable reals are artifacts of the tree-to-manifold projection — created, not discovered — and their measure-theoretic dominance is a statement about the projection, not about physical reality. The framework re-derives the computable/constructive hierarchy from distinction logic in the spirit of Spencer-Brown [9] and the QNFO program [10], [11], aligns with rule-based definitions of reals [7], and inherits the general lesson of the artifact literature [1], [4], [5]: representational projections systematically create features absent from their sources. The remaining gap — a projection-independent formalization of "discrete counterpart" — is the principal open problem.

## References

[1] arXiv:2010.14356v2 | Upsampling artifacts in neural audio synthesis
[2] arXiv:1201.0863v1 | Fractional Calculus: Some Basic Problems in Continuum and Statistical Mechanics
[3] arXiv:2308.14122v1 | Preparing Reproducible Scientific Artifacts using Docker
[4] arXiv:2308.04871v1 | Mathematical Artifacts Have Politics: The Journey from Examples to Embedded Ethics
[5] arXiv:2103.01090v2 | Systematic Analysis and Removal of Circular Artifacts for StyleGAN
[6] arXiv:2002.03814v1 | The Genius Conjectures (via Bell Polynomials)
[7] arXiv:2305.00