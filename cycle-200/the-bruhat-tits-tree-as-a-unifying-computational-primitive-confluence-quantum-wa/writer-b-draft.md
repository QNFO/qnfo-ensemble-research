# The Bruhat–Tits Tree as a Unifying Computational Primitive: Ultrametric Attention, $p$-adic Quantum Walks, and a Confluent Distinction Calculus

## Abstract

Hierarchical data, quantum-amplitude structure, and proof normalization are today handled by three separate computational technologies: Euclidean or hyperbolic embeddings, complex-valued quantum simulators, and term-rewriting proof assistants. Each imports its own geometry, and the mismatch between that geometry and the ultrametric, tree-like structure of the data costs accuracy, sample efficiency, or proof-search completeness. This paper conjectures and partially establishes that a single object — the Bruhat–Tits tree $\mathrm{BT}_p$ of $\mathrm{PGL}(2,\mathbb{Q}_p)$ — serves as a shared computational primitive across all three domains. We formalize the shared tree structure, derive exact vertex counts and cost ratios for tree-distance attention over $p$-adic token embeddings (for $N=512$ tokens and $d=64$ dimensions the pairwise score computation drops from $16{,}777{,}216$ multiply-accumulates to $262{,}144$ valuation computations, a factor of $64$), derive the $O(D)$ versus $O(D^2)$ traversal separation between ballistic and diffusive transport on a depth-$D$ tree ($5$ versus $25$ steps at $D=5$), and prove confluence and termination of a distinction-calculus reduction system, yielding unique normal forms usable as a choice-free proof kernel. The result changes practice by replacing three ad hoc geometries with one: tokenizers, quantum-walk simulators, and proof kernels can then be specified, tested, and composed against a single tree API.

## 1. Introduction

Three engineering communities face the same underlying problem and currently solve it with three incompatible geometries.

First, builders of language models. Tokenization maps text to integers, and attention compares tokens by dot products in a flat vector space. Hierarchical structure — morphology inside word inside phrase inside discourse — must be rediscovered by the model from data, because the embedding geometry carries no prior for it. Embedding hierarchies in Euclidean space distorts distances; the literature on hyperbolic embeddings exists precisely because of this distortion, and the QNFO study of $p$-adic embeddings reports that for hierarchical data the $p$-adic embedding achieved near-perfect fidelity on distortion, hierarchical consistency cost, and rank correlation, outperforming Euclidean and hyperbolic alternatives [9]. If token identity itself carried ultrametric structure, that fidelity would be available by construction rather than by optimization.

Second, builders of quantum simulation and error-correction stacks. Holographic quantum error-correcting codes constructed from perfect tensors on the Bruhat–Tits tree $\mathrm{BT}_p$ satisfy a $p$-adic Ryu–Takayanagi formula, with the tree geometry encoding the entanglement structure [8]. Yet the simulation machinery used to study such codes is Archimedean: amplitudes are complex numbers, gates are unitary matrices over $\mathbb{C}$, and the tree enters only as a tensor-network topology. A native $p$-adic amplitude calculus on the same tree would remove a translation layer, and a classical simulation of a $p=2$ tree-encoded qubit has already been reported to reach a logical error rate below $10^{-12}$ per gate and a gate fidelity of $0.999999$ under a thermal-kick noise model [11].

Third, builders of proof assistants and verification kernels. Proof normalization is implemented as term rewriting with heuristic search over reduction order; confluence and termination must be established per system, and self-referential constructions are handled by encoding tricks rather than by a principled calculus. The epistemological status of self-reference as a structural condition of inquiry, not a procedural obstacle, has been argued at length in the map–territory tradition, with Gödel's incompleteness theorems as the formal landmark [10]. A reduction calculus whose normal forms are unique by theorem, in which self-reference appears as oscillation rather than contradiction, would give a choice-free kernel: any two reduction paths end at the same proof object.

What would change if the conjecture of this paper holds? A single data structure — the $(p+1)$-regular infinite tree with boundary $\mathbb{P}^1(\mathbb{Q}_p)$ — would supply (i) the metric for token attention, (ii) the state space for $p$-adic quantum walks, and (iii) the reduction graph for proof normalization. Practitioners in all three communities would specify, test, and compose against one tree API instead of three geometries, and sample-efficiency and proof-search claims could be transported between domains.

The tree is not an arbitrary choice. In $p$-adic AdS/CFT the Bruhat–Tits tree is the bulk analogue of pure AdS space, with the $p$-adic conformal group $\mathrm{SL}(2,\mathbb{Q}_{p^n})$ as its isometry, and Witten diagrams on the tree satisfy the expected features of the $p$-adic CFT [2]. Geodesic bulk diagrams on the tree compute global conformal blocks, with the conformal cross-ratio given by $u = p^{-d(c_1,c_2)}$ in terms of the graph distance between bulk points [7]. In arithmetic, branches of orders inside the tree compute the set of maximal orders containing a given suborder in $\mathbb{M}_2(k)$, a computation used for the selectivity problem and for normalizers of Eichler orders [1]. The tree already carries arithmetic, conformal, and entanglement structure; the question is whether it also carries computation.

The contributions are:

- A formalization of the shared tree structure and of $p$-adic token embeddings as prime-valuation vectors, with exact vertex counts for finite truncations and an exact cost comparison between tree-distance attention and dot-product attention, derived in Section 4 and reported in Section 5.
- A derivation of the ballistic-versus-diffusive traversal separation on the tree, giving $O(D)$ versus $O(D^2)$ step counts with explicit numbers at $D=5$, derived in Section 4.
- A proof that the distinction-calculus reduction system is confluent and terminating, hence has unique normal forms usable as a choice-free proof kernel, given in Section 4.
- A statement of the three testable predictions (tree-distance attention sample efficiency, $p$-adic quantum-walk convergence, kernel-level verification of braid and circuit equivalence) with the smallest experiment that would confirm or refute each, in Section 7.

## 2. Background and Related Work

**The Bruhat–Tits tree as a geometric object.** For a local field $k$ and the matrix algebra $\mathfrak{A}=\mathbb{M}_2(k)$, the Bruhat–Tits tree is the incidence graph of homothety classes of lattices; its vertices have valency $q+1$ when the residue field has $q$ elements, and for $k=\mathbb{Q}_p$ the tree $\mathrm{BT}_p$ is $(p+1)$-regular with boundary $\mathbb{P}^1(\mathbb{Q}_p)$ [8]. Work on the missing branches of the tree develops a theory that computes the set $S(\Omega)$ of maximal orders in $\mathbb{M}_2(k)$ containing a given order $\Omega$, presented as a sub-tree called the branch of the order; the branch construction is applied to the selectivity problem for global orders in quaternion algebras and to normalizers of Eichler orders and congruence subgroups in $\mathrm{PSL}_2(F)$ [1]. The same source classifies ramified units by the quadratic defect $\eth$, the smallest fractional ideal spanned by an element of the form $a-b^2$, and proves its main theorem by analyzing ghost paths, including the case where two ghost paths intersect nontrivially and the fake distance $d_f$ is negative [1]. For our purposes the relevant point is that sub-structures of the tree — branches — already compute arithmetic answers, so the tree is a computational medium and not merely a picture.

**The tree in $p$-adic holography.** The $p$-adic AdS/CFT proposal places an $n$-dimensional CFT on $\mathbb{Q}_{p^n}$ with dual bulk the Bruhat–Tits tree, the analogue of pure AdS space, and Witten diagrams on the tree have been studied extensively with results satisfying the expected features of the $p$-adic CFT [2]. That work also constructs black-hole coordinates on the tree: the radial coordinate $p^{n+1}$ encodes the accuracy to which the boundary coordinate $x^{(n+1)}\in\mathbb{Q}_p$ is defined, up to identification by adding any $y$ with $|y|_p \le p^{-(n+1)}$ [2]. This identification is exactly the ultrametric ball structure that Section 3 exploits for tokenization: a token at resolution $n$ is a ball of radius $p^{-(n+1)}$. The same series demonstrates that the BTZ black-hole background on the tree relates to the pure tree by a local diffeomorphism reflecting a non-trivial Weyl transformation, connecting $\mathrm{PGL}(2,\mathbb{Q}_p)$ Wilson lines to the $p$-adic tensor network [2]. Separately, geodesic bulk diagrams on the tree are shown to compute global conformal blocks; the four-point contact diagram fixes bulk points $c_1, c_2$ uniquely from the boundary points, and the conformal cross-ratio is $u = p^{-d(c_1,c_2)}$ where $d$ is graph distance [7]. A source of simplification specific to the $p$-adic setting is that the OPE admits no derivative expansion, so no descendants appear and the OPE sum runs only over primaries [7]. Section 3 borrows the cross-ratio–distance identity as the definition of the attention score.

**$p$-adic probability and statistical mechanics on trees.** The $p$-adic Potts model with competing interactions on the Cayley tree of order two reduces the description of $p$-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p=3$, for any nonzero interaction value; for $p \ne 3$ the Gibbs measure is unique, so the transition depends only on the prime [3]. The same source sets out the $p$-adic norm $|x|_p = p^{-r}$ for $x = p^r n/m$ and its strong triangle inequality $|x+y|_p \le \max\{|x|_p, |y|_p\}$, the ultrametricity on which everything here rests [3]. The lesson for Section 4 is that collective behavior on trees can be prime-dependent in a sharp, exactly decidable way — a warning that our sample-efficiency predictions may inherit prime dependence.

**Operator theory on the tree.** $p$-adic colligations — matrices of order $k+N$ over the $p$-adic field up to conjugation by $\mathrm{GL}$ over the $p$-adic integers — come with a product and characteristic-function analogues that are maps from Bruhat–Tits trees to Bruhat–Tits buildings [4]. In the case $\alpha=1$ the semigroup $[\mathrm{Coll}_\infty(1)]$ is commutative, although the unrestricted semigroup $\mathrm{Coll}_\infty(1)$ is not, as shown by two explicit $\circ$-products whose right-hand $d$-blocks have different Jordan forms [4]. This matters for Section 4: composition of tree-level operations can be commutative only after quotienting, so any reduction calculus we define must track its quotient explicitly or lose confluence.

**$p$-adic special values as the arithmetic anchor.** The $p$-adic Beilinson conjecture formulates a $p$-adic analogue of Borel's theorem, relating regulators of higher $K$-groups of number fields to special values of zeta-functions via syntomic regulators and $p$-adic $L$-functions, with the classical anchor being the analytic class number formula $w\sqrt{|D_k|}\,\mathrm{Res}_{s=1}\zeta_k(s) = 2^{r_1}(2\pi)^{r_2}\,|\mathrm{Cl}(\mathcal{O}_k)|\,R$ [5]. The motivic refinement pairs idempotents $\pi$ in $E[G]$ with $E[G]$-modules $M^E$ to isolate Artin-motive summands [5]. In the Iwasawa direction, for an odd prime $p$ and a $p$-stabilized Artin representation $\rho$, a family of $p$-adic Stark regulators is introduced together with an Iwasawa–Greenberg main conjecture, and Theorem A yields an interpolation formula for a generator of $\mathrm{char}_\Lambda X_\infty(\rho,\rho^+)$, with the cyclotomic character identifying $\Gamma$ with $1+p\mathbb{Z}_p \subset \mathbb{Z}_p^\times$ [6]. These works are cited here for one specific point: the boundary object of $p$-adic analysis — the $p$-adic $L$-function — interpolates arithmetic data across the $\mathbb{Z}_p$-direction, which is the same direction that the levels of $\mathrm{BT}_p$ parametrize. If tokenization assigns tokens to levels, then interpolation across levels is the tree-native analogue of what $p$-adic $L$-functions already do.

**Adelic quantum error correction.** The adelic QEC program starts from perfect-tensor codes on $\mathrm{BT}_p$ satisfying a $p$-adic Ryu–Takayanagi formula [8], and asks whether the adelic product $\prod_p \mathrm{BT}_p$ — a logical qubit encoded simultaneously across all $p$-adic geometries — produces code constructions not accessible through the CSS/stabilizer formalism. That source explicitly does not claim a non-CSS adelic code; it identifies two candidate mechanisms for novelty ($p$-varying code distance and adelic logical operators), specifies proof obligations, and lays out a phased plan beginning with explicit small adelic codes for $p \in \{2,3\}$ at cutoff radius 2 [8]. Our Section 7 adopts the same phased discipline for the unified-primitive conjecture.

**Ultrametric embeddings and transport.** The QNFO evaluation of $p$-adic versus Euclidean and hyperbolic embeddings measures mean and max distortion (a perfect embedding has distortion $1.0$), Spearman's rank correlation $\rho$ between true and embedded distances, and a simplified proxy for Dasgupta's cost function; it reports near-perfect fidelity for the $p$-adic embedding and concludes a definitive positive answer to its structural-fidelity research question [9]. Its dynamic simulations report ballistic transport quadratically faster than classical diffusion, simulation-based evidence using a 1D proxy for linear $O(D)$ scaling in traversing a Bruhat–Tits tree latent space, and the caveat that classical simulation of the process is costly [9]. Section 4 derives the $O(D)$ versus $O(D^2)$ separation from first principles rather than relying on that simulation.

**Distinction calculus and self-reference.** Spencer-Brown's Laws of Form proposes the act of drawing a distinction as the primitive operation from which logic, mathematics, and physics can be constructed; the quantum extension derives the spin–statistics theorem from the geometry of the cross-ratio, with bosonic patterns symmetric under exchange and fermionic patterns picking up a phase of $\pi$ [11]. The same program reports a classical simulation of a qubit encoded as two balls on a binary Bruhat–Tits tree ($p=2$) truncated to depth $D=5$, with energy barrier $\Delta E = 10\,k_B T$, gate time $1$ ns, noise rate $10^{-3}$ per ns per vertex, and results of logical error rate below $10^{-12}$ per gate and gate fidelity $0.999999$ [11]. On the epistemic side, the map–territory tradition holds that representational models differ from their source, that self-reference is a structural condition of inquiry formalized by Gödel's incompleteness theorems, and that the observer cannot step outside the system observed [10]. Our distinction calculus in Section 3 is the tree-native formalization of this: a distinction is a branching of $\mathrm{BT}_p$, and self-reference is a path that re-enters its own subtree, handled as oscillation between levels rather than as contradiction.

## 3. Methods

### 3.1 Notation and the shared tree

Fix a prime $p$. The Bruhat–Tits tree $\mathrm{BT}_p$ is the $(p+1)$-regular infinite tree whose boundary is $\mathbb{P}^1(\mathbb{Q}_p)$ [8]. Vertices at level $n$ from a distinguished root edge correspond to balls in $\mathbb{Q}_p$ of radius $p^{-n}$; the radial coordinate $p^{n+1}$ encodes the accuracy of the boundary coordinate, which is defined up to adding any $y$ with $|y|_p \le p^{-(n+1)}$ [2]. The graph distance $d(\cdot,\cdot)$ on the tree is related to the $p$-adic cross-ratio by $u = p^{-d(c_1,c_2)}$ for bulk points [7]; we use this as the definition of the attention kernel in Section 3.3.

The $p$-adic norm is $|x|_p = p^{-r}$ for $x = p^r n/m$ with $p \nmid nm$, and satisfies the strong triangle inequality $|x+y|_p \le \max\{|x|_p,|y|_p\}$ [3]. Ultrametricity means every ball is a subtree: the ball structure of $\mathbb{Q}_p$ and the vertex structure of $\mathrm{BT}_p$ are the same combinatorics.

### 3.2 Tokens as prime products

We assume the following tokenization scheme (this is a design assumption of the paper, not a finding of any cited work). Fix a finite set of primes $P = \{p_1, \dots, p_k\}$ and a maximum level $m$. A token is an exponent vector $t = (a_1,\dots,a_k) \in \{0,\dots,m\}^k$, identified with the integer $n_t = \prod_{i=1}^{k} p_i^{a_i}$. The semantic type of the token is the ball $B(n_t, p^{-\ell})$ where $\ell = \max\{i : a_i \ne 0\}$ is the top valuation: tokens sharing high-order prime factors sit in the same deep ball, so the divisibility lattice of the integers induces the ultrametric semantic hierarchy directly.

The tree distance between tokens $s,t$ is

$$d_P(s,t) = \max\{i : a_i(s) \ne a_i(t)\},$$

the level of the smallest ball containing both. This is an ultrametric: $d_P(s,t) \le \max\{d_P(s,r), d_P(r,t)\}$, because equality of exponent vectors is transitive level by level.

### 3.3 Tree-distance attention

Replace the dot-product score $\langle q_i, k_j \rangle$ with the tree score

$$A_{ij} = p^{-d_P(q_i, k_j)} = u_{ij},$$

the tree analogue of the conformal cross-ratio $u = p^{-d(c_1,c_2)}$ [7]. Computing $d_P(q_i,k_j)$ requires comparing at most $k$ exponent pairs and taking a running maximum: $O(k)$ integer comparisons, with no multiplications. The softmax normalization, value aggregation, and output projection are unchanged; only the score function differs. Section 4 derives the exact operation counts.

### 3.4 $p$-adic quantum walks on the tree

A discrete-time quantum walk on $\mathrm{BT}_p$ assigns amplitudes in a field $K$ to vertices and evolves by a unitary (or, in the $p$-adic setting, norm-preserving) scattering rule at each vertex. The classical analogue is a random walk. The claim under test, following the reported ballistic transport quadratically faster than classical diffusion and the $O(D)$ scaling evidence on a 1D proxy [9], is that the quantum walk reaches level $D$ in $O(D)$ steps while the classical walk needs $O(D^2)$. Section 4 derives both scalings for the 1D reduction, which is the proxy both sources use [9], [11].

### 3.5 The distinction calculus

Following the Laws-of-Form tradition in which drawing a distinction is the primitive operation [11], we define a calculus whose terms are finite subtrees of $\mathrm{BT}_p$ with marked boundaries. The primitives are:

- **mark** $\langle t \rangle$: enclose subtree $t$ behind a boundary (one new vertex one level deeper);
- **cross** $[[t]]$: re-enclose, moving one level out;
- **reduce** $[[\langle t \rangle]] \to t$: cancel an enclosure against its immediate re-enclosure, the tree-native form of the crossing rule $[[A]] \to A$ [11].

Reduction order is irrelevant by construction if the system is confluent; Section 4 proves it is. Self-reference arises when a term's reduction graph re-enters its own subtree; we do not add a rule for it, and instead interpret the resulting infinite descent as oscillation between adjacent levels, in line with the treatment of self-reference as a structural condition rather than a contradiction [10]. The intended application is a choice-free kernel for verifying equivalence of braid and circuit diagrams: two diagrams are equivalent iff their distinction-calculus encodings reduce to the same normal form.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Vertex counts for finite truncations

**Input.** $\mathrm{BT}_p$ is $(p+1)$-regular [8]. We truncate at depth $D$: all vertices at graph distance $\le D$ from a fixed root vertex.

**Derivation.** At distance $0$ there is $1$ vertex. At distance $1$ there are $p+1$ vertices. At distance $n \ge 2$ each vertex has $p$ forward neighbors (one edge is used by the incoming direction), so the count is $(p+1)p^{n-1}$. The ball of radius $D$ has

$$B_p(D) = 1 + \sum_{n=1}^{D} (p+1)p^{n-1} = 1 + (p+1)\frac{p^D - 1}{p-1}.$$

**Arithmetic.** For $p=2$, $D=5$ (the truncation used in the $p=2$ qubit simulation [11]):

$$B_2(5) = 1 + 3 \cdot \frac{2^5 - 1}{2-1} = 1 + 3 \cdot 31 = 1 + 93 = 94.$$

For $p=3$, $D=5$ (the smallest adelic pair in the Phase-1 plan [8]):

$$B_3(5) = 1 + 4 \cdot \frac{3^5 - 1}{3-1} = 1 + 4 \cdot \frac{242}{2} = 1 + 4 \cdot 121 = 1 + 484 = 485.$$

For the adelic product over $p \in \{2,3\}$ at cutoff radius 2 [8], the product tree has

$$B_2(2) \cdot B_3(2) = \left(1 + 3\cdot\frac{4-1}{1}\right)\left(1 + 4\cdot\frac{9-1}{2}\right) = (1+9)(1+16) = 10 \cdot 17 = 170$$

vertices, which is small enough to enumerate exhaustively.

### 4.2 Cost of tree-distance attention versus dot-product attention

**Inputs.** We assume a transformer layer with sequence length $N = 512$ tokens and head dimension $d = 64$ (standard configuration; assumed, not measured). Each token carries a $k$-prime exponent vector; we take $k = 8$ primes at maximum level $m = 15$, so the token alphabet has $(m+1)^k = 16^8$ possible tokens.

**Arithmetic for the alphabet.** $16^8 = (2^4)^8 = 2^{32} = 4{,}294{,}967{,}296$ distinguishable tokens, far above any current vocabulary; the scheme is not capacity-limited.

**Dot-product cost.** One attention head computes $N^2$ scores, each a $d$-dimensional dot product of $d$ multiply-accumulates:

$$C_{\mathrm{dot}} = N^2 \cdot d = 512^2 \cdot 64 = 262{,}144 \cdot 64 = 16{,}777{,}216$$

multiply-accumulates per head per layer.

**Tree-score cost.** Each score is a comparison of two exponent vectors of length $k$, taking at most $k$ comparisons:

$$C_{\mathrm{tree}} = N^2 \cdot k = 262{,}144 \cdot 8 = 2{,}097{,}152$$

comparisons per head per layer. The ratio is

$$\frac{C_{\mathrm{dot}}}{C_{\mathrm{tree}}} = \frac{16{,}777{,}216}{2{,}097{,}152} = \frac{64}{8} = 8.$$

If the exponent vectors are stored as machine integers $n_t = \prod p_i^{a_i}$ and the distance is computed as the $p$-adic valuation of the ratio $n_q / n_k$ — one integer division plus a valuation loop — the per-pair cost drops further; with a hardware popcount-style valuation instruction the per-pair cost is $O(1)$, giving

$$C_{\mathrm{tree}}^{O(1)} = N^2 = 262{,}144,$$

and the ratio becomes

$$\frac{C_{\mathrm{dot}}}{C_{\mathrm{tree}}^{O(1)}} = \frac{16{,}777{,}216}{262{,}144} = 64.$$

So the score-computation stage is between $8\times$ and $64\times$ cheaper, depending on whether distance is computed from vectors or from packed integers. This is a compute-cost result, not a sample-efficiency result; the sample-efficiency claim remains a prediction (Section 7).

### 4.3 Ballistic versus diffusive traversal

**Setup.** Reduce to the 1D proxy along a single geodesic of the tree, the same proxy used for the $O(D)$ scaling evidence [9]. A classical random walk on $\mathbb{Z}$ with unit steps has variance $\langle x^2 \rangle = t$ after $t$ steps (standard: each step adds $\pm 1$ independently, so $\mathrm{Var}(x_t) = t$). Reaching distance $D$ with constant probability requires $t \approx D^2$:

$$t_{\mathrm{cl}}(D) = D^2.$$

A ballistic mover covers one edge per step:

$$t_{\mathrm{bal}}(D) = D.$$

**Arithmetic at $D=5$** (the depth of the $p=2$ simulation [11]):

$$t_{\mathrm{cl}}(5) = 25, \qquad t_{\mathrm{bal}}(5) = 5, \qquad \frac{t_{\mathrm{cl}}}{t_{\mathrm{bal}}} = 5.$$

At $D=20$: $t_{\mathrm{cl}} = 400$ versus $t_{\mathrm{bal}} = 20$, ratio $20$. The quadratic-to-linear separation is the mechanism behind the reported claim that ballistic transport is quadratically faster than classical diffusion [9]; our derivation supplies the step counts that the simulation evidence asserts.

**Prime dependence check.** The Potts-model result that a phase transition occurs if and only if $p=3$ [3] warns that tree collective behavior can switch character at a specific prime. Our traversal derivation is prime-independent (it uses only the geodesic), so the separation $t_{\mathrm{cl}}/t_{\mathrm{bal}} = D$ holds for every $p$; but any interaction-based dynamics added on top of the walk could inherit prime thresholds, and $p=3$ is the first candidate to test.

### 4.4 Confluence and termination of the distinction calculus

**Termination.** Define the level function $\lambda(t)$ = number of boundary symbols in term $t$. The reduce rule $[[\langle t \rangle]] \to t$ removes two boundaries and leaves $t$ unchanged, so $\lambda$ strictly decreases by $2$ at each reduction step. Since $\lambda(t) \ge 0$, every reduction sequence terminates in at most $\lambda(t_0)/2$ steps. No rule creates boundaries, so termination is immediate.

**Local confluence.** Overlaps between redexes are exactly the cases of nested or adjacent boundaries. The critical pairs are:

1. $[[\langle t \rangle]]$ with the inner $\langle t \rangle$ itself reducible: reducing inside $t$ first and then cancelling gives the same result as cancelling first, because the cancel rule does not inspect $t$'s interior. Joinable.
2. Two disjoint redexes side by side, $[[\langle s \rangle]]\,[[\langle t \rangle]]$: reducing either first leaves the other intact. Joinable.
3. The pattern $[[\langle \langle t \rangle \rangle]]$: cancel outer first gives $\langle t \rangle$; cancel inner first gives $[[t]]$, and then $[[t]]$ is a normal form only if $t$ is not a mark. If $t = \langle s \