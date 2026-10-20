# Positional Notation as Native Ultrametric Geometry of Nested Cycles: Formal Foundations and Testable Consequences

## Abstract

Positional notation is universally treated as a linear device: a digit string is decoded onto the Archimedean real line and the geometry of the representation is assumed to be Euclidean. This paper addresses a specific gap: the tree of nested cycles that positional notation intrinsically encodes — one level per digit position, one branch per digit value — is never given its own metric status, so practitioners who group, query, or index by numerals (calendar systems, database partitioning, periodic-process scheduling) inherit a linear distance that may not match the structure the notation actually carries. We formalize the claim that the $b$-adic distance $d(x,y)=b^{-v_b(x-y)}$, where $v_b$ is the base-$b$ valuation, is the natural metric of positional notation, prove it satisfies the strong triangle inequality, and extend it to mixed-radix numerals such as calendar dates. We derive quantitative consequences with full arithmetic: the expected number of shared trailing digits between two random $n$-digit numerals is $1/(b-1)$ (exactly $1$ in binary, $1/9\approx 0.1111$ in decimal); the ultrametric ball of radius $b^{-k}$ in a $b^n$-element domain contains exactly $b^{n-k}$ elements; and for Gregorian dates the mixed-radix ultrametric separates adjacent months by a factor of exactly $31$ in distance, while the linear day-count distance separates "next month" from "half a month away" by only $6.25\%$. These results re-found numeral representation on explicit, base-matched ultrametric geometry and specify falsifiable simulations and hardware tests.

## 1. Introduction

Anyone who builds software or instruments that deal with periodic time faces the same structural mismatch every day. Calendar systems, scheduling engines, time-series databases, and astronomical ephemeris interfaces all store dates as linear day counts (Unix timestamps, Julian day numbers) or as digit strings decoded onto a line, yet the questions users and systems actually ask are cyclic and hierarchical: which dates fall in the same month, which fall in the same season, which share a weekday phase. Today this mismatch is patched by hand: every calendar library carries bespoke partitioning logic (month boundaries, leap rules, timezone buckets) layered on top of a linear representation, and every date-range index must be re-derived per application because the representation itself supplies no grouping. The cost is concrete: partition pruning in temporal databases, seasonal aggregation in climatology and agriculture, and recurrence rules in scheduling all require auxiliary structures that the numeral system could carry natively if the shared-prefix structure of the notation were treated as the primary geometry rather than an accident of string formatting.

A second community faces a version of the same problem at a different scale. Architects of quantum error correction choose between lattice topologies (surface codes) and tree topologies, and the choice is currently made without a principled account of what geometry the underlying register representation natively supports; recent work on tree-topology error confinement reports that the expected advantage of tree geometry fails to materialize at moderate error rates, which makes the representational question — what metric is native to a positional register — practically urgent rather than merely philosophical.

If the claim of this paper holds — that positional notation intrinsically encodes a tree of nested cycles and that the $b$-adic (ultrametric) distance between numerals is the natural metric of the representation, not an artifact — then three decisions change. Designers of calendar and time interfaces would use shared-prefix distance as the default grouping and zoom metric instead of linear day-count. Database and file-format designers would partition temporal data by radix-aligned prefix rather than by fixed linear ranges. And researchers in error-correcting architectures would have a principled criterion for when a tree-topology register is representationally native versus imposed.

The contributions are:

- A proof that the shared-trailing-digit distance $d(x,y)=b^{-v_b(x-y)}$ on the integers is an ultrametric, with the carrying operation of positional arithmetic identified as exactly the tree-branching event (Section 4.1).
- An extension of the construction to mixed-radix numerals, with calendar dates as the worked case, including the exact distance values $1$, $1/12$, and $1/372$ for year, month, and day levels and the derived $31\times$ separation ratio (Section 4.2).
- Closed-form quantitative consequences: expected shared trailing digits $\mathbb{E}[v_b]=1/(b-1)$, ball sizes $b^{n-k}$, and ball counts $b^k$, each with full arithmetic (Section 4.3).
- A quantitative contrast showing the linear day-count metric loses month-boundary information by a factor of $16$ relative to the mixed-radix ultrametric on the worked calendar example (Section 4.4).
- A specification of the conditions under which base-matched representation is empirically superior, and the minimal falsification experiments, drawn from the existing tree-topology simulation and hardware literature (Sections 5 and 7).

## 2. Background and Related Work

The strong triangle inequality is the defining axiom of the spaces this paper works in. Nakayama [1] takes as the definition of an ultrametric that $d(x,y)\leq d(x,z)\lor d(z,y)$ with $\lor$ the maximum operator, and develops the general theory: an ultrametric version of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization of ultrametrizable compacta, proved via free modules over commutative rings and a $0$-dimensional Michael continuous selection theorem. This matters here because it establishes that ultrametric spaces are not pathological curiosities but support the same foundational infrastructure (embedding, extension, selection) as ordinary metric spaces; any proposal to treat numeral space as ultrametric inherits a mature theory rather than starting from scratch.

The linear (Archimedean) alternative is not a single geometry either, and its asymptotic behavior is well quantified. Berckmoes, Colbois and Verovic's collaborator line of work is represented by the Hilbert geometry paper [2], which computes the volume growth entropy of spheres in Hilbert geometry: for an $(n+1)$-dimensional Hilbert geometry over a bounded convex domain with $C^{3}$ boundary of positive normal curvature, $\lim_{t\to\infty}\ln(\mathrm{Vol}(S_t^n))/t = n$, matching the Lobachevsky space, with the Hilbert distance given explicitly as $d_U(p,q)=\frac{1}{2}\ln\frac{\|q-q_1\|}{\|q-p_1\|}\times\frac{\|p-p_1\|}{\|p-q_1\|}$. The relevance is methodological: [2] shows what it looks like to derive the large-scale geometry of a representation from its distance function, which is exactly the program this paper runs for the $b$-adic distance, with the difference that the ultrametric case yields discrete trees rather than Finsler geodesic flows.

A cautionary structural parallel comes from Einstein-metric existence theory. Boyer, Galicki and Kollár's program [3] uses Sasakian geometry and symmetry reduction to produce an abundance of Einstein metrics on odd-dimensional spheres, including exotic ones, with the Brieskorn graph theorem supplying the combinatorial criterion: the link $L(\mathbf{a})$ is homeomorphic to a sphere exactly when the gcd-graph $G(\mathbf{a})$ — vertices connected iff $\gcd(a_i,a_j)>1$ — satisfies one of two isolation conditions. The gcd-graph is a valuation-theoretic object: divisibility structure made into adjacency. This is the same move this paper makes on numerals — reading arithmetic divisibility ($b^k \mid x-y$) as geometric structure — and [3] demonstrates that such graph-encoded divisibility can carry rich, non-obvious geometry.

Notation systems beyond the decimal default have been analyzed on their own terms. Ryan's just-intonation work [4] presents a notation system for arbitrary rational frequencies in free Just Intonation and shows that transposition up requires multiplication to be defined for any two notations and transposition down requires inversion to be defined for any notation — i.e., the algebraic closure of the notation system, not the string format, is what determines its usability. This supports the present thesis that a notation's fitness is a property of its internal metric-algebraic structure; the submission history in [4] (v1 August 2015 through v4 December 2016) also illustrates that notation redesign is an iterative, multi-year process, which tempers expectations for rapid adoption of any alternative numeral geometry.

Alternative notations within a fixed number system are catalogued in the quaternionic differential geometry paper [5], which collects the Cartesian, polar ($q=\rho(\cos\theta + I\sin\theta)$ with $I=\cos\phi\, i+\sin\phi\, e^{i\xi}j$), and symplectic ($q=z_0+z_1 j$) notations of quaternions and notes that the symplectic notation is not unique, with several equivalent forms obtained by exchanging imaginary units. The lesson drawn here is that representation choice within one mathematical object is genuinely multi-valued, and each notation exposes different structure — precisely the situation between the Archimedean line reading and the ultrametric tree reading of positional numerals.

The question of what geometry is "native" to a space has a precise formulation in Buliga's dilatation structures [6], which give an intrinsic treatment of sub-riemannian geometry by proving that regular sub-riemannian manifolds admit dilatation structures — local, scale-dependent metric limits that replace the Euclidean tangent space. The paper works with the Gromov–Hausdorff distance on pointed compact metric spaces and notes that from the metric point of view such spaces are fractals, the Hausdorff dimension with respect to the Carnot–Carathéodory distance strictly exceeding the topological dimension. This is the formal template for the present claim: the "tangent" or local geometry of a representation need not be the flat line, and the correct local geometry is discovered by taking rescaled limits — which for positional numerals are exactly the $b$-adic balls.

The ultrametric side of Cantor-set structure is developed by Raut and Datta [7], who study a family of Cantor sets endowed with a scale-invariant ultrametric built from "relative infinitesimals" and an inversion rule, in which increments are accomplished by inversions rather than translations; they prove that the associated valuation is given by an appropriate Cantor function and that the construction is both scale and reparametrisation invariant, offering "an insight how a measure zero set might grow into a fat Cantor set because of a distortion (deformation) of scales." This is directly load-bearing for the present paper: it shows that the ultrametric on a digit-tree space can be deformed while remaining an ultrametric, which is the mechanism by which mixed-radix and non-uniform calendar trees stay ultrametric under unequal month lengths.

The cyclic-time connection has a formal analogue in conservation-law structure. Callaway, Culcer, Lechtenfeld and collaborators' multisymplectic Noether theorem [8] extends the correspondence between conserved quantities and continuous symmetries to multi-Hamiltonian systems via homotopy co-momentum maps, generalizing the symplectic case where a conserved $f$ yields a Hamiltonian vector field $X_f$ with $\mathcal{L}_X\omega=0$. Periodic phenomena — the subject of this paper's calendar application — are precisely systems with cyclic symmetry, and [8] provides the framework in which a cycle (a symmetry) corresponds to a conserved structure (the phase label); a representation that encodes the cycle as a digit level makes that conserved structure explicit, while the linear encoding buries it in arithmetic mod $P$.

The synthesis that motivates this paper is stated in the QNFO unified thesis [9], which argues that "the ultrametric tree that underlies all quantitative representation was systematically flattened into an Archimedean line," beginning from the observation that in any base $b\geq 2$ the digit string "10" denotes $b$, so every base names itself "base-10" and a numeral string cannot internally specify its own rule of interpretation — the radix is a silent parameter supplied by an external meta-language. The thesis also identifies the equal-interval assumption as a second hidden parameter, "a geometric import from Descartes and analytic geometry — an epistemological tool reified into an ontological property," and proposes a concrete falsification experiment: a depth-2 tree of 8 transmon qubits connected via coaxial cavities enforcing tree-only gates, compared against a 2D nearest-neighbour layout, with the central claim falsified if the tree geometry does not yield a statistically significant improvement in logical error rate. This paper takes [9]'s structural claim as its hypothesis and supplies the formal proofs and quantitative derivations that [9] states as conjecture.

The core theorem itself is stated and sketched in the QNFO tree-numeration synthesis [10]: in any integer base $b\geq 2$, $d(x,y)=b^{-v_b(x-y)}$ satisfies $d(x,z)\leq\max\{d(x,y),d(y,z)\}$, because two numbers share $k$ trailing digits iff $b^k\mid(x-y)$ but $b^{k+1}\nmid(x-y)$, and shared-trailing-digit counts satisfy a min-lattice property. [10] also consolidates five extension threads: distance-dependent weighting in the style of Rofa (2013), where a digit's value depends on its vertex-to-root depth and the digit "0" becomes active so that "012" and "12" differ; hereditary binary arithmetic in the style of Tarau (2013), where recursively run-length-compressed binary strings form a tree of trees in which numbers requiring $10^{100}$ decimal digits compress to depth $\sim 20$ and arithmetic remains computable on the compressed form; and rational-base representation trees in the style of Akiyama et al., prompted by the fact that in integer bases not every rational has a finite expansion. These threads show the tree view is already computationally productive; this paper adds the metric formalization and the periodic-domain application.

The quantum extension is developed in the QNFO qudit QEC paper [11], which defines the tree distance on an $n$-qubit register as $d_T(i,j)=n-\lfloor\log_2(i\oplus j)\rfloor$ — an ultrametric making the register Cantor-set-like — and proves a subtree error confinement theorem with correlated-error probability bounded by $(cp)^{2(d-\ell)}$ for two qubits whose lowest common ancestor sits at depth $\ell$. Critically for calibration, [11]'s own simulation results, using normalized crossing criteria, show that for independent Pauli errors at moderate rates the tree topology does not outperform the 2D grid and at some error rates performs worse: at $p=10^{-4}$ tree crossing is $0.000$ versus grid $0.333$, but at $p=2.7\times 10^{-4}$ tree crossing is $1.000$ versus grid $0.462$. Any claim that tree-native representation is automatically better must therefore survive this negative result, which this paper treats as a boundary condition rather than a refutation of the representational thesis.

Finally, the Bruhat–Tits tree QEC analysis [12] studies a conjectured passive fault-tolerance scheme with energy barrier $E_{\text{barrier}}(d)=2^d$ in tree depth $d$, and reports computed classical evidence: iterated eight-fold majority voting suppresses an error rate $p=0.4$ through $p^{(1)}=0.1736704$, $p^{(2)}\approx 0.0055485$, and $p^{(3)}\approx 2.905\times 10^{-10}$ over three levels, while a reported zero-error simulation bounds the logical error probability only at $p_L\leq 2.9957\times 10^{-5}$ for $N=10^5$ trials. [12] is explicit that the barrier scaling is a conjecture not proved for quantum dynamics and that coherent error paths reconverging across branches would falsify the confinement hypothesis. This paper adopts the same epistemic discipline: the ultrametric claim about notation is proved here at the representational level, while all physical-transfer claims remain labeled hypotheses with stated falsifiers.

## 3. Methods

### 3.1 Definitions

**Definition 3.1 (Ultrametric).** A metric $d$ on a set $X$ is an ultrametric if for all $x,y,z\in X$,
$$d(x,y)\leq \max\{d(x,z),\,d(z,y)\}.$$
This is the strong triangle inequality of [1]. Two consequences used throughout: every triangle is isosceles with a short base, and every point inside a ball is its center.

**Definition 3.2 (Base-$b$ valuation).** For a nonzero integer $n$ and integer base $b\geq 2$, $v_b(n)$ is the largest $k$ such that $b^k$ divides $n$; $v_b(0)=+\infty$.

**Definition 3.3 ($b$-adic distance).** On $\mathbb{Z}$, define
$$d_b(x,y)=b^{-v_b(x-y)},\qquad d_b(x,x)=0.$$

**Definition 3.4 (Mixed-radix numeral and shared-prefix distance).** A mixed-radix numeral of depth $m$ is a tuple $x=(x_1,\dots,x_m)$ with component $i$ drawn from an ordered set of size $L_i$ (the level-$i$ cycle length). The shared-prefix distance is
$$d_{\mathrm{mr}}(x,y)=w_k,\quad k=\min\{i:\ x_i\neq y_i\},$$
where the level weights satisfy $w_1 > w_2 > \dots > w_m > 0$ and each $w_i$ exceeds the sum of all strictly smaller weight values reachable below it; we use the multiplicative choice $w_i=\prod_{j\le i} L_j^{-1}$, i.e. $w_1 = 1/L_1$... wait, we set $w_0 = 1$ for a differing first component and $w_i = \left(\prod_{j=1}^{i} L_j\right)^{-1}$ for a first difference at component $i+1$; concretely, differing at level $i$ (0-indexed root) gives distance $\left(\prod_{j=1}^{i} L_j\right)^{-1}$.

**Definition 3.5 (Linear reference distance).** The linear (day-count) distance on dates is $d_{\mathrm{lin}}(x,y)=|t_x - t_y|$, the absolute difference of ordinal day numbers.

### 3.2 Method of proof and derivation

All results in Section 4 are exact algebraic derivations on finite or countable sets; no simulation is used. The calendar case uses the proleptic Gregorian month lengths $L = (31,28,31,30,31,30,31,31,30,31,30,31)$ with 2024 treated as a leap year (February $=29$ days), which is the standard civil calendar and is stated here as the paper's explicit modeling assumption. The quantum-topology numbers quoted in the Discussion and Section 7 are taken from the cited sources and are identified as such; every number computed in this paper is derived in Section 4 with all arithmetic shown.

## 4. Analysis

### 4.1 The shared-trailing-digit distance is an ultrametric

**Claim C1.** $d_b(x,y)=b^{-v_b(x-y)}$ is an ultrametric on $\mathbb{Z}$.

*Derivation.* Take any $x,y,z\in\mathbb{Z}$. Write $k_1 = v_b(x-y)$ and $k_2 = v_b(y-z)$. By definition, $b^{k_1}\mid (x-y)$ and $b^{k_2}\mid (y-z)$. Then
$$(x-z) = (x-y) + (y-z),$$
and each summand is divisible by $b^{\min(k_1,k_2)}$, so their sum is divisible by $b^{\min(k_1,k_2)}$. Hence
$$v_b(x-z)\ \geq\ \min(k_1,k_2).$$
Applying the order-reversing map $k \mapsto b^{-k}$ (strictly decreasing, so it turns $\geq$ on exponents into $\leq$ on distances and $\min$ into $\max$):
$$d_b(x,z) = b^{-v_b(x-z)} \ \leq\ b^{-\min(k_1,k_2)} = \max\left(b^{-k_1},\, b^{-k_2}\right) = \max\{d_b(x,y),\, d_b(y,z)\}.$$
This is exactly the strong triangle inequality. Symmetry $d_b(x,y)=d_b(y,x)$ is immediate from $v_b(x-y)=v_b(y-x)$ (divisibility is sign-blind), and $d_b(x,y)=0\iff x=y$ holds because $v_b(0)=+\infty$ is the only case giving distance $0$ under the convention of Definition 3.3. $\square$

**Carrying as tree-branching.** In base $b$, the $k$-th digit (from the right, 0-indexed) of $x$ and $y$ agree if and only if $x\equiv y \pmod{b^{k+1}}$, i.e. $v_b(x-y)\geq k+1$. The carry operation in addition is precisely the event where a digit sum reaches $b$ and increments the next level; in tree terms, the addition path crosses from one branch of the level-$(k{+}1)$ node to another. Thus the nested digit positions are the levels of a rooted $b$-ary tree, each integer is a leaf path, and $d_b$ is the depth of the lowest common ancestor, mapped through $k\mapsto b^{-k}$. This is the formal content of the claim that positional notation "is" a tree of nested cycles: each digit position is a cycle of length $b$ nested inside the cycle of the position to its left, and carrying is the re-entry event that closes the outer cycle.

### 4.2 Mixed-radix extension and the calendar case

**Claim C2.** The shared-prefix distance of Definition 3.4 is an ultrametric whenever the level weights are nested as specified.

*Derivation.* Let $x,y,z$ be mixed-radix tuples and let $k_{xy}$, $k_{yz}$, $k_{xz}$ be the first indices at which the respective pairs differ. If $x$ and $y$ agree on components $1..k$ and $y$ and $z$ agree on components $1..l$, then $x$ and $z$ agree on components $1..\min(k,l)$; hence $k_{xz}\geq \min(k_{xy},k_{yz})$. Since the weight sequence $w$ is strictly decreasing in the index, $w_{k_{xz}} \leq w_{\min(k_{xy},k_{yz})} = \max(w_{k_{xy}}, w_{k_{yz}})$, which is the strong triangle inequality. $\square$

**Calendar instantiation.** Model a date as the mixed-radix tuple (year, month, day) with level sizes $L_1 = 12$ (months per year) and $L_2 = 31$ (the maximal month length; shorter months are leaves at shallower depth within the day level, which preserves the ultrametric property because it only removes leaves, never merges subtrees). The weights are:
$$w_{\text{year}} = 1, \qquad w_{\text{month}} = \frac{1}{L_1} = \frac{1}{12}, \qquad w_{\text{day}} = \frac{1}{L_1 L_2} = \frac{1}{12\times 31} = \frac{1}{372}.$$
Arithmetic: $12\times 31 = 372$.

Worked pairs (all in year 2024 unless noted; 2024 is a leap year, so February has 29 days and the year has 366 days):

- Pair A: 2024-03-15 vs 2024-03-20. Same year, same month, different day:
$$d_{\mathrm{mr}} = \frac{1}{372} \approx 0.00268817.$$
- Pair B: 2024-03-15 vs 2024-04-15. Same year, different month:
$$d_{\mathrm{mr}} = \frac{1}{12} \approx 0.08333333.$$
- Pair C: 2023-03-15 vs 2024-03-15. Different year:
$$d_{\mathrm{mr}} = 1.$$

The separation ratio between consecutive levels is
$$\frac{w_{\text{month}}}{w_{\text{day}}} = \frac{1/12}{1/372} = \frac{372}{12} = 31,$$
exactly the maximal month length, and
$$\frac{w_{\text{year}}}{w_{\text{month}}} = \frac{1}{1/12} = 12,$$
exactly the number of months. The ultrametric gap between levels equals the cycle length of the finer level — the geometry encodes the cycle structure by construction.

### 4.3 Closed-form consequences for uniform numerals

**Claim C3 (probability of shared trailing digits).** For $x,y$ independent and uniform on the residues modulo $b^k$,
$$\Pr\left[v_b(x-y)\geq k\right] = \frac{1}{b^k}.$$

*Derivation.* $v_b(x-y)\geq k$ iff $x\equiv y \pmod{b^k}$. Among the $b^{2k}$ ordered pairs $(x,y)$ of residues mod