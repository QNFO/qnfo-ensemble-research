# Artifacts of Projection: Non-Computable Reals as Lossy Images of a Bruhat–Tits Tree onto the Archimedean Line

## Abstract

We develop a formal framework for a conjecture about the ontological status of the non-computable reals: that the continuum is not primitive but constructed, with natural numbers, rationals, and computable reals arising from a single distinction operator via enclosure operations, and the full real line emerging only through a lossy projection — the Monna-map — of a discrete, non-Archimedean Bruhat–Tits tree onto a smooth Archimedean manifold. The central claim is that the reals outside the computable subset, $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$, are not discovered but created by this projection: they are artifacts, in the precise sense in which upsampling and resampling operations in generative models create structure absent from the underlying discrete object. We give explicit derivations supporting the framework's coherence: (i) a counting argument showing the computable reals form a countable set, with $2^{n+1}-1$ candidate descriptions of length at most $n$ over a binary alphabet; (ii) a covering argument proving the computable reals have Lebesgue measure zero, so that projection artifacts, if they exist, occupy full measure; (iii) exact vertex and ray counts for finite-depth approximations of the $(p+1)$-regular Bruhat–Tits tree, e.g. $3\cdot 2^{d}-2$ vertices at depth $d$ for $p=2$; and (iv) a density computation of rational shadows among depth-limited tree paths. We propose falsifiable tests comparing finite-depth tree shadows to decimal expansions, and discuss failure modes, including the possibility that the projection metaphor fails to support any rigorous existence claim.

## 1. Introduction

The standard set-theoretic presentation of the continuum treats $\mathbb{R}$ as a completed object whose non-computable members are simply "there," differing from computable reals only in epistemic accessibility. This paper takes seriously an alternative conjecture, originating in a Spencer-Brown-style program in which the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed [9]. In that program, the uncountability of the reals has been argued to conflate two distinct properties: Archimedean completeness ("depth") and set-theoretic cardinality explosion ("breadth"), with all physically relevant properties preserved by the computable reals alone [10]. A three-axis ontology extends this by treating $p$-adic completions as information carriers alongside the computable depth and the physically vacuous breadth of non-computables [11].

The specific contribution here is a geometric mechanism for *why* the non-computable stratum exists at all: it is the image of a lossy projection from a discrete, non-Archimedean object — a Bruhat–Tits tree — onto the Archimedean line. The projection is conjectured to be surjective but non-injective in a strong sense: most points of $\mathbb{R}$ have no counterpart as a finite or limit-definable path in the tree. These points are *artifacts* of the projection, exactly analogous to the checkerboard patterns that upsampling layers introduce in neural image and audio synthesis, where the generated object contains structure absent from, and caused by, the discrete-to-continuous conversion itself [1], [5].

The word "artifact" is used deliberately and in a technical sense. Recent work has argued that mathematical objects themselves can be artifacts with consequences — that artifacts in mathematics are not neutral but carry commitments, by analogy with Langdon Winner's thesis that artifacts have politics [4]. If non-computable reals are projection artifacts, then the measure-theoretic fact that they dominate $\mathbb{R}$ (derived in Section 4) is a statement about the projection, not about a pre-existing continuum. This reframing has methodological consequences for reproducibility: an artifact-laden object cannot be regenerated from its discrete source, and only the source-plus-projection specification is reproducible in the sense emphasized in work on reproducible scientific artifacts [3].

Our results are deliberately modest. We do not prove the conjecture. We (a) state the framework precisely enough to be checked, (b) derive the counting and measure-theoretic facts that the framework predicts, with all arithmetic shown, (c) compute exact finite-depth tree quantities that any implementation must match, and (d) specify the simulation program — comparing finite-depth tree "shadows" to decimal expansions — whose outcome would confirm or falsify the central claim. We also connect the framework to adjacent constructions of the reals: the definition of a real number as a rule that answers Yes or No to membership in rational intervals [7], which is precisely the shape of a tree-path limit; and to the operator-algebraic theory of projections, whose range-closure questions mirror the question of whether the projection's image is all of $\mathbb{R}$ or a proper substructure [8].

## 2. Background and Related Work

**Distinction as primitive.** Spencer-Brown's *Laws of Form* proposed the act of drawing a distinction as the primitive operation from which logic, mathematics, and physics can be constructed; the QNFO consolidation synthesizes known quantum correspondences of this program, identifies seven open problem categories, and proposes four extensions [9]. Our construction takes the distinction operator as the generator of the discrete tree: each branching is a distinction, and enclosure operations (re-entering the form) generate the natural numbers, hence the rationals. The companion note "Syntactic Generation" [12] supplies only a title in the material available to us, and we therefore cite it solely as the locus of the syntactic-generation mechanism, without attributing further content to it.

**Depth without breadth.** The claim that uncountability conflates Archimedean completeness with cardinality explosion, and that all physically relevant properties are preserved by computable reals, is argued in [10]. Our measure-theoretic derivation in Section 4 gives this claim quantitative teeth: the computable stratum is not merely sufficient physically, it is measure-theoretically negligible, so "physically relevant" and "full measure" come apart sharply. The three-axis ontology of [11] — Depth (computable reals), Breadth (non-computable reals, physically vacuous), Valuation ($p$-adic completions as information carriers) — supplies the architectural role of the Bruhat–Tits tree: the tree is the Valuation axis made geometric, and the Monna-map is the passage from Valuation to Depth/Breadth. That work also proposes falsifiable predications for quantum error correction and gauge structure, which we take as downstream targets, not inputs.

**Reals as rules.** A recent definition takes a real number to be a rule which says Yes or No based on whether the real number ought to be in a given rational interval [7]. This is a teaser for a fuller program ("Defining Real Numbers as Oracles"), and the supplied summary gives no further detail; but the definition as stated is exactly the interface our tree shadows present: a path in a nested-enclosure tree is a Yes/No rule over rational intervals. The convergence is structural: on this definition, $\mathbb{R}_{\mathrm{comp}}$ is the set of rules with finite descriptions, and the "oracle" reals are rules with no finite description — our artifacts.

**Projections and their ranges.** The operator-algebra literature studies projections on C*-algebras and their ranges, including the "bicontractive projection problem" and variants of results of Stormer, Friedman and Russo, Choi and Effros, Effros and Stormer, Robertson and Youngson, and Youngson [8]. The supplied summary indicates the focus is on completely contractive projections and the structure of their ranges. Our question — is the Monna-map's image closed, and does it equal the codomain? — is a set-theoretic shadow of the range problem: a projection whose range is a proper, non-closed subobject generates points of the ambient space that are limits of range points but not range points themselves. We use [8] as a structural analogy only, since the summary does not state specific range theorems we could import.

**Artifacts in generative systems.** Upsampling layers in neural audio synthesis introduce undesired artifacts; the phenomenon was studied in computer vision as checkerboard artifacts but had been overlooked in audio, and [1] addresses that gap. The mechanism — a discrete-to-continuous conversion whose regularities imprint spurious structure on the continuous output — is the template for our central claim. In image generation, vanilla StyleGAN produces prominent circular artifacts that degrade quality, and [5] provides a systematic investigation of how those circular artifacts arise and how to remove them. Together [1] and [5] establish the methodological pattern we import: characterize the artifact, trace it to the projection operator, and ask what the artifact-free image would have been. Our proposal is that $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ is the artifact class and the Monna-map is the operator.

**Artifacts with consequences.** That mathematical artifacts have politics is argued in [4], which extends Langdon Winner's idea into mathematics: first by listing examples showing mathematical artifacts with politics exist, then by arguing all mathematical artifacts have politics, with implications for embedding ethics into curricula. If non-computable reals are artifacts, [4] implies they are not ontologically neutral: the choice to treat $\mathbb{R}$ as completed embeds a commitment about what counts as a number. We note this as a philosophical consequence, not a mathematical result.

**Continuum mechanics and fractional calculus.** Fractional calculus has been applied to model viscoelastic bodies and the Basset problem of unsteady motion of a particle in a viscous fluid, with fractional orders entering the constitutive analysis [2]. The relevance is methodological: non-integer orders are a continuum-level artifact of memory effects, and the supplied summary indicates the fractional analysis arises "in the former analysis" of fractal-type structure — a case where the mathematical apparatus itself encodes non-smooth underlying geometry. We cite [2] as a physical precedent for effective continuum descriptions carrying traces of discrete or fractal generators.

**Conjecture discipline.** Finally, [6] presents two related conjectures arising from $i$-matchings in random $r$-regular bipartite graphs, stated via basic properties of convergent power series and Bell polynomials, with the authors advising others not to try to prove them. We cite it as a normative model: a conjecture paper should state its conjectures crisply, mark what is proved versus proposed, and calibrate ambition. Our Conjectures C1–C3 in Section 3 follow that discipline.

## 3. Methods

### 3.1 The discrete stage: enclosure tree

Fix a prime $p$. The Bruhat–Tits tree $\mathcal{T}_p$ of $\mathrm{PGL}_2$ over $\mathbb{Q}_p$ is a $(p+1)$-regular tree: every vertex has $p+1$ neighbors. We use it as the geometric instantiation of the distinction operator: each vertex is a distinction; its $p+1$ descendants are the distinguishable enclosures. The $p$-adic valuation supplies edge lengths, making $\mathcal{T}_p$ non-Archimedean.

**Definition 3.1 (Shadow).** A *depth-$d$ shadow* of $\mathcal{T}_p$ is an assignment of a real interval to each ray of length $d$ from a root, such that sibling shadows are disjoint rational intervals and the union over each level covers the parent. The Monna-map conjecture (C2 below) is that the limit of shadows along an infinite ray is a real number, and that every real arises this way.

### 3.2 Conjectures

- **C1 (Generation).** $\mathbb{N}$, $\mathbb{Q}$, and $\mathbb{R}_{\mathrm{comp}}$ arise from the distinction operator by enclosure operations; each computable real corresponds to a finite or limit-definable tree path.
- **C2 (Projection).** There is a surjective, non-injective projection $\pi:\mathcal{T}_p^{\infty}\to\mathbb{R}$ (the Monna-map) from infinite rays to reals, under which points of $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ have no finite or limit-definable preimage: they are artifacts.
- **C3 (Dominance).** The artifact set has full Lebesgue measure in $\mathbb{R}$.

C3 is *derived conditionally* in Section 4 from C2 plus the classical covering argument; C1 and C2 remain conjectures.

### 3.3 Simulation protocol (proposed, not executed)

Finite-depth trees of depths $d\in\{4,8,16,32\}$ with $p\in\{2,3,5\}$ are enumerated; each depth-$d$ ray is mapped to the rational midpoint of its shadow interval; the resulting finite decimal strings are compared to decimal expansions of benchmark computable reals. The test of C1 is whether every benchmark real's expansion is matched by some ray sequence; the test of C2's converse is whether ray sequences exist whose limits are not limit-definable — which cannot be decided finitistically and is flagged as such.

## 4. Analysis

All arithmetic below is shown step by step. Inputs are stated with their source: structural facts about $\mathcal{T}_p$ come from Definition 3.1 and the $(p+1)$-regularity stated in Section 3.1; the covering inputs come from the enumeration of finite descriptions.

### 4.1 Counting finite descriptions (input to C1)

Let descriptions be strings over a binary alphabet $\{0,1\}$. The number of strings of length exactly $k$ is $2^{k}$. The number of descriptions of length at most $n$ is the geometric sum

$$D_n=\sum_{k=0}^{n}2^{k}=\frac{2^{n+1}-1}{2-1}=2^{n+1}-1.$$

For $n=100$:

$$D_{100}=2^{101}-1.$$

Computing $2^{101}$: $2^{10}=1024$, so $2^{100}=(2^{10})^{10}=1024^{10}$. $1024^{10}=2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376$ (exact, by repeated squaring: $2^{20}=1\,048\,576$; $2^{40}=1\,048\,576^{2}=1\,099\,511\,627\,776$; $2^{80}=(2^{40})^{2}=1\,209\,259\,259\,389\,742\,506\,817\,536\,576$; $2^{100}=2^{80}\cdot 2^{20}=1\,209\,259\,259\,389\,742\,506\,817\,536\,576\times 1\,048\,576=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376$). Hence

$$D_{100}=2^{101}-1=2\,535\,301\,200\,456\,458\,802\,993\,405\,410\,126\approx 2.5353\times 10^{30}.$$

Since every computable real has at least one finite description, and descriptions are countably many (a countable union of finite sets $\{k: \text{length}=k\}$), $\mathbb{R}_{\mathrm{comp}}$ is countable. This is the input to the measure computation.

### 4.2 Measure of the computable stratum (derivation of C3, conditional)

Enumerate the computable reals as $x_1,x_2,x_3,\dots$ (possible since they are countable, Section 4.1). Fix $\varepsilon>0$ and cover $x_i$ by the open interval $I_i$ of radius $\varepsilon\, 2^{-(i+1)}$ centered at $x_i$, i.e. length $\ell(I_i)=\varepsilon\, 2^{-i}$. Total cover length:

$$\sum_{i=1}^{\infty}\ell(I_i)=\sum_{i=1}^{\infty}\varepsilon\, 2^{-i}=\varepsilon\sum_{i=1}^{\infty}2^{-i}=\varepsilon\cdot 1=\varepsilon,$$

using the exact geometric identity $\sum_{i=1}^{\infty}2^{-i}=\frac{1/2}{1-1/2}=1$. Therefore the outer Lebesgue measure satisfies

$$m\big(\mathbb{R}_{\mathrm{comp}}\cap[0,1]\big)\le\varepsilon\quad\text{for every }\varepsilon>0,$$

so $m(\mathbb{R}_{\mathrm{comp}}\cap[0,1])=0$. Since $m([0,1])=1$, the artifact set satisfies

$$m\big(([0,1]\setminus\mathbb{R}_{\mathrm{comp}})\big)=1-0=1,$$

i.e. artifacts have full measure — *provided* C2 holds and the non-computable points are exactly $[0,1]\setminus\mathbb{R}_{\mathrm{comp}}$. The conditionality is emphasized: the derivation uses only the countability of $\mathbb{R}_{\mathrm{comp}}$ and standard covering, but its interpretation as "projection dominance" depends on C2.

### 4.3 Exact tree counts (finite-depth approximations)

**Vertices.** In the $(p+1)$-regular tree rooted at $v_0$, level $0$ has $1$ vertex; level $k\ge 1$ has $(p+1)p^{k-1}$ vertices (each level-$(k-1)$ vertex has $p$ forward children, one edge being the back-edge). The ball of radius $d$ has

$$V_d=1+\sum_{k=1}^{d}(p+1)p^{k-1}=1+(p+1)\frac{p^{d}-1}{p-1}.$$

For $p=2$: $V_d=1+3(2^{d}-1)=3\cdot 2^{d}-2$. At $d=10$:

$$V_{10}=3\cdot 2^{10}-2=3\cdot 1024-2=3072-2=3070.$$

**Rays.** The number of rays (directed paths) of length $d$ from the root is $(p+1)p^{d-1}$. For $p=2$, $d=10$:

$$R_{10}=3\cdot 2^{9}=3\cdot 512=1536.$$

**Check.** $V_{10}=1+\sum_{k=1}^{10}3\cdot 2^{k-1}=1+3(1+2+4+\cdots+512)=1+3(1023)=1+3069=3070$. ✓

### 4.4 Rational shadows and their density

The rationals in $[0,1]$ with denominator at most $N$ (in lowest terms, including $0/1$ and $1/1$) number

$$Q_N=1+\sum_{k=2}^{N}\varphi(k),$$

where $\varphi$ is Euler's totient. For $N=10$: $\varphi(2)=1,\ \varphi(3)=2,\ \varphi(4)=2,\ \varphi(5)=4,\ \varphi(6)=2,\ \varphi(7)=6,\ \varphi(8)=4,\ \varphi(9)=6,\ \varphi(10)=4$. Sum: $1+2+2+4+2+6+4+6+4=31$; hence $Q_{10}=1+31=32$... including $1/1$ separately gives $Q_{10}=1+\sum_{k=2}^{10}\varphi(k)+1=33$ (the extra $1$ counts $1/1$, which is not generated by $k\ge 2$ proper fractions; $0/1$ is the leading $1$). So $Q_{10}=33$.

A depth-$10$ binary shadow structure has $R_{10}=1536$ rays (Section 4.3). If each rational with denominator $\le 10$ in $[0,1]$ is realized by at least one ray (each such rational has a finite binary expansion of length $\le 10$ or a eventually-periodic one approximable to depth $10$), the rational density among depth-10 shadows is at least

$$\rho_{10}=\frac{Q_{10}}{R_{10}}=\frac{33}{1536}=\frac{11}{512}\approx 0.021484375.$$

Exact: $33/1536 = 33/1536$; divide by $3$: $11/512$; $11/512 = 0.021484375$ exactly ($11\times 1953.125$... rather: $1/512=0.001953125$, $\times 11 = 0.021484375$). ✓

### 4.5 Resolution scaling

A depth-$d$ shadow resolves intervals of relative length $2^{-d}$ (bisection at each level). For $d=32$: $2^{-32}=\frac{1}{4\,294\,967\,296}\approx 2.3283\times 10^{-10}$. Doubling depth squares the resolution cost: reaching $10^{-16}$ (double precision) requires $d=\lceil 16/\log_{10}2\rceil=\lceil 16/0.30103\rceil=\lceil 53.15\rceil=54$ levels, with $V_{54}=3\cdot 2^{54}-2=3\cdot 18\,014\,398\,509\,481\,984-2=54\,043\,195\,528\,445\,952-2=54\,043\,195\,528\,445\,950$ vertices ($2^{54}=18\,014\,398\,509\,481\,984$ exactly). ✓

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are measured or simulated.

- **R1.** The number of binary descriptions of length $\le 100$ is $D_{100}=2^{101}-1=2\,535\,301\,200\,456\,458\,802\,993\,405\,410\,126\approx 2.5353\times 10^{30}$ (Section 4.1). Consequently $\mathbb{R}_{\mathrm{comp}}$ is countable.
- **R2.** $m(\mathbb{R}_{\mathrm{comp}}\cap[0,1])=0$ and, conditional on C2, the artifact set $[0,1]\setminus\mathbb{R}_{\mathrm{comp}}$ has measure exactly $1$ (Section 4.2). This is the precise form of the "measure-theoretic dominance as projection effect" claim.
- **R3.** The $(p+1)$-regular Bruhat–Tits tree with $p=2$ has $V_{10}=3070$ vertices within depth $10$ and $R_{10}=1536$ rays of length $10$; in general $V_d=3\cdot 2^{d}-2$ and $R_d=3\cdot 2^{d-1}$ (Section 4.3).
- **R4.** There are $Q_{10}=33$ rationals in $[0,1]$ with denominator $\le 10$; their density among depth-10 binary shadows is at least $\rho_{10}=11/512=0.021484375$ (Section 4.4).
- **R5.** Double-precision resolution ($10^{-16}$) requires depth $d=54$, i.e. $V_{54}=54\,043\,195\,528\,445\,950$ vertices for $p=2$ (Section 4.5).

**Projection (labeled as such).** If the simulation protocol of Section 3.3 is executed and every benchmark computable real's decimal expansion is matched by a ray sequence at the predicted depths, C1 gains empirical support; no numerical outcome of that protocol is reported here because it has not been run. The depth-54 requirement of R5 is a feasibility bound, not a measurement.

## 6. Discussion

**Limitations.** The central weakness is that C2 — the existence and surjectivity of the Monna-map with the stated artifact property — is asserted, not proved. The measure-theoretic result R2 is unconditional as a statement about $\mathbb{R}_{\mathrm{comp}}$, but its interpretation as "artifacts dominate" collapses if C2 fails: if the projection is not surjective, the non-computable reals are not images of anything and the artifact language is empty. A second weakness is the analogy to generative artifacts [1], [5]: in those settings the artifact is *detectable* by comparison with a ground truth; here there is no artifact-free ground truth to compare against, since $\mathbb{R}$ *is* the output. The analogy may be structurally illuminating but evidentially empty.

**Falsification.** The framework is falsified if: (i) a non-computable real is shown to have a canonical finite or limit-definable tree path under any reasonable Monna-map definition, breaking the artifact classification; (ii) the simulation protocol of Section 3.3 systematically fails to match benchmark computable reals at the depths predicted by R5; or (iii) the enclosure-generation of $\mathbb{N}$ from the distinction operator (C1) cannot be carried out without smuggling in the continuum, e.g. requiring a limiting operation already presupposing $\mathbb{R}$. Conversely, confirmation would require proving that the specific projection adds exactly $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ — a characterization theorem, not a counting argument.

**Against ourselves.** A skeptic should note that R2 is classical: the measure zero of a countable set needs no tree ontology, so the framework risks explaining nothing, merely relabeling. Our reply is that the value lies in the mechanism (C2) and the finite-depth predictions (R3–R5), which are new and checkable; but if those predictions are trivially satisfied by any nested-interval scheme, the Bruhat–Tits apparatus is dispensable ornament. The operator-algebraic range question [8] suggests a sharper open problem: is the Monna-map's image closed in $\mathbb{R}$? If not, artifacts would include limits of computable shadows that are themselves non-computable — a strictly stronger claim than C3. The political-artifacts argument [4] raises a further question we cannot settle: whether treating artifacts as "physically vacuous" [10], [11] is itself a commitment with consequences, per [4]'s thesis that all mathematical artifacts have politics. Finally, the physical precedents of [2] — fractional orders modeling fractal-informed continua — suggest artifacts can be *useful* effective descriptions; whether non-computable reals play any such effective role is open. The reproducibility framing of [3] applies: only the discrete source plus projection rule is reproducible; the artifact stratum is not independently regenerable, which is a testable methodological claim about any implemented version.

## 7. Conclusion

We have given a precise, checkable formulation of the conjecture that non-computable reals are artifacts of a lossy projection from a Bruhat–Tits tree onto the Archimedean line, derived the measure-theoretic dominance result conditionally with full arithmetic, computed exact finite-depth tree quantities ($V_{10}=3070$, $R_{10}=1536$, $\rho_{10}=11/512$, $d=54$ for double precision), and specified the simulation protocol that would test the generation claim. The conjectures C1 and C2 remain open; the framework's value stands or falls on whether the Monna-map can be defined so that its artifact set is provably $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$.

## References

[1] arXiv:2010.14356v2 | Upsampling artifacts in neural audio synthesis
[2] arXiv:1201.0863v1 | Fractional Calculus: Some Basic Problems in Continuum and Statistical Mechanics
[3] arXiv:2308.14122v1 | Preparing Reproducible Scientific Artifacts using Docker
[4] arXiv:2308.04871v1 | Mathematical Artifacts Have Politics: The Journey from Examples to Embedded Ethics
[5] arXiv:2103.01090v2 | Systematic Analysis and Removal of Circular Artifacts for StyleGAN
[6] arXiv:2002.03814v1 | The Genius Conjectures (via Bell Polynomials)
[7] arXiv:2305.00981v1 | Rationally Querying the Reals
[8] arXiv:1508.01530v2 | Completely contractive projections on operator algebras
[9] QNFO: Quantum Laws of Form
[10] QNFO: The Computable Continuum: Depth Without Breadth
[11] QNFO: Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum
[12] QNFO: Syntactic Generation