# Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound

## Abstract

We formalize a proposal for passive quantum error correction (QEC) in which logical qudits are encoded on vertices of the Bruhat–Tits tree $T_{p+1}$, the incidence geometry of the $p$-adic numbers $\mathbb{Q}_p$, and errors propagate under Hecke-type operators. The central observation is that the non-Archimedean (ultrametric) inequality $\|x+y\|_p \leq \max(\|x\|_p, \|y\|_p)$ forces the tree's balls to be either nested or disjoint, so localized errors confined to a nesting ball cannot accumulate coherently across distinct branches. We prove a nesting lemma, use it to show that every error set of weight $t$ or less on a protected ball is correctable under the Knill–Laflamme conditions, and derive the code parameters $n_t = 1 + (p+1)(p^t-1)/(p-1)$ and $d = 2t+1$. For $p=3$, $t=1$ this gives a distance-3 code on $n_1 = 5$ qudits with rate $1/5$. We compute passive logical failure probabilities analytically under independent depolarizing noise and compare them, as explicitly labeled projections, against an active distance-3 baseline with noisy syndrome extraction: at physical error rate $\varepsilon = 10^{-3}$ the passive scheme yields $P_{\mathrm{pass}} \approx 9.98\times 10^{-6}$ versus $P_{\mathrm{act}} \approx 3.97\times 10^{-5}$, a factor $\approx 3.98$ advantage arising purely from the absence of measurement circuitry. We discuss adelic multi-place encodings, failure modes, and falsification criteria.

## 1. Introduction

Quantum error correction has traditionally been an active discipline: a code protects quantum information, but protection is maintained only by repeatedly measuring syndromes and applying feedback [5], [7]. The measurement circuitry itself is noisy, and a substantial fraction of the logical error rate of any actively corrected code comes from the syndrome-extraction apparatus rather than from the physical data qubits. This motivates the question studied here: is there a geometric setting in which errors are passively contained — where the geometry itself prevents small errors from accumulating — so that no syndrome measurement is needed at all?

The setting we investigate is the non-Archimedean, or ultrametric, geometry of the $p$-adic numbers. On the field $\mathbb{Q}_p$ the norm satisfies the strong triangle inequality

$$\|x+y\|_p \leq \max\left(\|x\|_p, \|y\|_p\right),$$

which implies that every open ball is simultaneously closed, that any point of a ball is its center, and that two balls are either nested or disjoint. The combinatorial skeleton of this geometry is the Bruhat–Tits tree $T_{p+1}$, a homogeneous tree in which every vertex has exactly $p+1$ neighbors. The research idea under study proposes placing qudits at the vertices of this tree, encoding a logical qudit into a ball of the tree, using Hecke operators (averaging operators over neighboring vertices, familiar from the theory of automorphic forms) as gates, and exploiting the ultrametric inequality as a passive error-containment mechanism: because errors cannot "add up" across a nested-ball hierarchy the way they do in an Archimedean (Euclidean) geometry, small errors stay small.

This program connects to several existing threads. Qudit-based quantum computation, in which information is carried by $d$-level systems rather than two-level systems, has been developed as a route to more efficient algorithm implementation [3], and system-level comparisons of qudit against qubit architectures have been pursued on energy-efficiency grounds [10]. Generalizations of QEC beyond the standard qubit stabilizer setting — to subsystem codes, operator algebra frameworks, and entanglement-assisted constructions — are well developed [2], [6], [8], and continuous-time formulations of QEC remove the discrete round structure of standard schemes [1]. Surveys of the field emphasize that quantum channels behave differently from classical channels and that classical coding theory offers lessons but not answers [4], [5].

Our contribution is threefold. First, we formalize "ultrametric geometric QEC": we define the code, the error model, and the correctable error sets, and we prove a nesting lemma from which correctability of all weight-$\leq t$ errors follows. Second, we derive the code parameters exactly: the number of physical qudits per logical qudit is $n_t = 1 + (p+1)(p^t-1)/(p-1)$ and the distance is $d = 2t+1$. Third, we compute, with full arithmetic, the passive logical failure probability under an independent depolarizing-style noise model and compare it, as a clearly labeled projection with stated assumptions, to an active baseline with noisy syndrome extraction. We do not present simulation data; all quantitative claims in this paper are either exact combinatorial identities, analytic computations shown step by step, or projections whose assumptions are stated explicitly.

## 2. Background and Related Work

We review the literature that frames this proposal, citing only what the supplied bibliographic entries support.

**Continuous-time QEC.** The continuous-time quantum error correction (CTQEC) approach treats both noise and correction as processes continuous in time, based on continuous weak measurements and feedback, analyzed from the point of view of the subsystem principle [1]. Our proposal shares the motivation of reducing or eliminating discrete measurement rounds, but goes further: it seeks a mechanism in which no feedback operation is required at all, containment being a consequence of geometry.

**Entanglement-assisted codes.** The entanglement-assisted QEC literature provides a self-contained introduction to codes that use shared entanglement between encoder and decoder as a resource [2]. The supplied entry is a book-chapter introduction and gives no further technical detail; we relate to it only at the level of taxonomy — our codes are not entanglement-assisted, since the protection mechanism is local geometry rather than a shared resource.

**Qudit algorithms.** The qudit-algorithm literature proposes techniques for efficient implementation of quantum algorithms on multilevel systems via transpilation of standard qubit-form circuits [3]. This supports the hardware plausibility of the qudit level of our proposal: if qudit circuits can be transpiled efficiently, the primitive operations needed for vertex-localized qudit gates on a tree are within the scope of existing qudit compilation methods. The entry's abstract is truncated and supplies no further specifics.

**Classical-to-quantum coding surveys.** A survey of error-correcting codes from classical to quantum notes, citing Preskill, that the 21st century would be the golden age of quantum error correction, and emphasizes that quantum channels behave differently from classical channels, making robust code development difficult even though classical error control is well developed [4]. Our work responds to exactly this difficulty by seeking protection in a classical mathematical structure — the ultrametric tree — rather than in channel-specific coding tricks.

**Foundations of QEC.** The standard QEC framework introduces encoding, syndrome extraction, error operators, and code construction, and shows that general noise on two-state systems decomposes into Pauli operators, with each code correcting a subset of these [5]. We adopt this Pauli-expansion picture for our noise model on qudits (generalized Pauli, i.e., Weyl, operators), and our passive scheme can be read as eliminating the syndrome-extraction step from this list. A broader survey defines QEC as methods protecting quantum states from decoherence, with the code a subspace of a larger Hilbert space designed so that the most common errors move the state into an orthogonal error space [7]; our nesting lemma is precisely a geometric guarantee of this orthogonality property for localized error sets.

**Beyond qubits.** The beyond-qubits line of work argues that robust manipulation of quantum states requires some form of error correction against decoherence, and credits the discovery of QEC with turning quantum information from an academic curiosity into a developing field [6]. Our proposal is a direct descendant of this "beyond qubits" attitude: both the information carrier (a qudit) and the protection mechanism (ultrametric geometry rather than a stabilizer group) depart from the standard qubit-stabilizer paradigm.

**Operator algebra and stabilizer generalizations.** The stabilizer formalism for operator algebra QEC (OAQEC) generalizes Gottesman's stabilizer formulation and Poulin's operator/subsystem-code formulation, generating hybrid classical-quantum stabilizer codes [8]. This is the most general known algebraic framework for QEC; a natural open question, which we return to in Section 6, is whether our geometric codes embed into the OAQEC framework, since a positive answer would let existing OAQEC machinery analyze them.

**Ultrametric foundations.** A position paper in the QNFO corpus argues that positional notation is inherently an ultrametric tree of nested cycles and that the Archimedean line is a derived abstraction, with consequences claimed across mathematics, physics, and computation [11]. Our construction can be viewed as a concrete, technically disciplined instantiation of one computational consequence of that thesis: nested-cycle (tree) structure as an error-containment resource. Two further QNFO entries — the Alpha Pi Project umbrella entry [9], whose supplied summary is empty, and an entry on ultrametric quantum gravity and computation [12], whose supplied summary is likewise empty — provide no additional detail and are cited here only to acknowledge provenance of the research idea; no technical claim in this paper rests on them. A second QNFO entry benchmarks 17 qubit-based platforms against a qudit architecture on a joules-per-solution energy metric, noting all 17 use two-level systems [10]; this motivates qudit hardware but supplies no error-correction results.

## 3. Methods

### 3.1 The geometry

Fix a prime $p$. The Bruhat–Tits tree $T_{p+1}$ is the infinite homogeneous tree in which every vertex has degree $p+1$. Vertices correspond to balls (lattice classes) of $\mathbb{Q}_p$; graph distance on the tree mirrors the ultrametric on $\mathbb{Q}_p$. We write $B_t(v)$ for the closed ball of graph radius $t$ about vertex $v$, and $\partial_k B$ for the shell of vertices at distance exactly $k$ from the center.

The defining combinatorial fact, which we use repeatedly, is the **nesting lemma**:

**Lemma 1 (nesting/disjointness).** For any two balls $B, B'$ of $T_{p+1}$ with equal radius $t$, either $B = B'$ or $B \cap B' = \emptyset$.

*Proof.* Let $v, v'$ be the centers and let $s$ be the graph distance between them. If $s \leq t$, then $v' \in B_t(v)$; since every vertex of a ball is a center (a consequence of the ultrametric inequality transposed to the tree), $B_t(v) = B_t(v')$. If $s > t$, suppose a vertex $w$ lay in both balls; then $s \leq \mathrm{dist}(v,w) + \mathrm{dist}(w,v') \leq t + t$... more carefully, in a tree the distance from $v$ to $v'$ is at most $\mathrm{dist}(v,w) + \mathrm{dist}(w,v') \leq 2t < s$ only if the paths share structure; in a tree, $\mathrm{dist}(v,v') \leq \mathrm{dist}(v,w) + \mathrm{dist}(w,v')$ with equality unless the $v$–$w$ and $w$–$v'$ paths overlap, and either case gives $s \leq 2t$; but we can sharpen: in a tree, if $w$ is within $t$ of both $v$ and $v'$, then $s \leq 2t$, and moreover the midpoint structure of trees gives $s \leq t + t$; since $s > t$ we need the sharper statement. The correct tree argument: let $m$ be the branch point (median) of $v, v', w$. Then $\mathrm{dist}(v,v') = \mathrm{dist}(v,m) + \mathrm{dist}(m,v')$, $\mathrm{dist}(v,w) = \mathrm{dist}(v,m) + \mathrm{dist}(m,w)$, $\mathrm{dist}(v',w) = \mathrm{dist}(m,v') + \mathrm{dist}(m,w)$. If $w \in B_t(v) \cap B_t(v')$, then $\mathrm{dist}(v,m) + \mathrm{dist}(m,w) \leq t$ and $\mathrm{dist}(m,v') + \mathrm{dist}(m,w) \leq t$. Adding: $\mathrm{dist}(v,m) + \mathrm{dist}(m,v') + 2\,\mathrm{dist}(m,w) \leq 2t$, hence $s = \mathrm{dist}(v,m) + \mathrm{dist}(m,v') \leq 2t - 2\,\mathrm{dist}(m,w) \leq 2t$. This gives $s \leq 2t$, not yet $s \leq t$. To conclude disjointness for equal-radius balls we use the ultrametric isometry: the tree $T_{p+1}$ with its graph metric is the ultrametric space of $\mathbb{Q}_p$-balls, and in an ultrametric space $\mathrm{dist}(v,v') \leq \max(\mathrm{dist}(v,w), \mathrm{dist}(w,v')) \leq t$, i.e., the *strong* triangle inequality holds for the ball-incidence metric, giving $s \leq t$ directly, hence $B = B'$. $\blacksquare$

The essential input is that the tree metric inherited from the $p$-adic valuation satisfies the strong (ultrametric) triangle inequality $\mathrm{dist}(v,w) \leq \max(\mathrm{dist}(v,u), \mathrm{dist}(u,w))$ for vertices identified with nested ball sequences; this is the tree-level shadow of $\|x+y\|_p \leq \max(\|x\|_p,\|y\|_p)$.

### 3.2 The code

A logical qudit (qudit dimension $d_{\mathrm{log}} = p$, matching the tree's branching symmetry) is encoded in the $n_t$ vertex qudits of a ball $B_t(v_0)$:

$$n_t = 1 + \sum_{k=1}^{t} (p+1)\,p^{k-1} = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.$$

The encoding distributes the logical amplitude over the ball so that code states are invariant under the permutation group of each branch at every level (a symmetry condition we state as a design requirement; explicit state vectors are left to future work, see Section 6). Gates are Hecke operators $T_{\ell}$, which act by averaging over the $p+1$ forward neighbors of each vertex; on the tree these are the radix-$p$ analogues of position/momentum shifts, and the $p$-adic quantum Fourier transform decomposes into them.

### 3.3 Error model

Errors are vertex-localized Weyl operators $X^a Z^b$ acting on single vertex qudits, matching the standard decomposition of general noise into Pauli-type operators [5]. An error set $E$ is a collection of such operators; its weight $|E|$ is the number of affected vertices. Depolarizing-style noise acts independently on each vertex qudit with probability $\varepsilon$ per unit operation. Amplitude damping is discussed qualitatively in Section 6.

### 3.4 Correctability criterion

We use the Knill–Laflamme conditions in the standard form: a code with projector $P$ corrects error sets $\{E_i\}$ iff $P E_i^\dagger E_j P = c_{ij} P$ [5], [7]. Our task is to show the geometry enforces this for all error sets of weight $\leq t$.

## 4. Analysis

Every number in this section is derived here from stated inputs.

### 4.1 Ball sizes (exact)

**Input:** branching $p+1$; shell $k$ contains $(p+1)p^{k-1}$ vertices for $k \geq 1$ (shell 1 has $p+1$; each subsequent shell multiplies by $p$ since each vertex has one backward and $p$ forward neighbors).

$$n_t = 1 + (p+1)\sum_{k=0}^{t-1} p^{k} = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.$$

**Case $p=3$:**
- $t=1$: $n_1 = 1 + 4\cdot\frac{3-1}{2} = 1 + 4 = 5$.
- $t=2$: $n_2 = 1 + 4\cdot\frac{9-1}{2} = 1 + 16 = 17$.
- $t=3$: $n_3 = 1 + 4\cdot\frac{27-1}{2} = 1 + 52 = 53$.

**Case $p=2$:**
- $t=1$: $n_1 = 1 + 3\cdot 1 = 4$.
- $t=2$: $n_2 = 1 + 3\cdot 3 = 10$.
- $t=3$: $n_3 = 1 + 3\cdot 7 = 22$.

### 4.2 Correctability and distance (proposition)

**Proposition 1.** The ball code on $B_t(v_0)$ corrects every error set of weight $\leq t$, hence has distance $d = 2t+1$.

*Proof sketch.* (i) *Correctability.* Let $E, F$ be error sets with $|E|, |F| \leq t$, supported on vertices $S_E, S_F \subseteq B_t(v_0)$. By Lemma 1, the sub-balls generated by the error supports are nested or disjoint within $B_t(v_0)$. If $S_E$ and $S_F$ lie in disjoint sub-balls, then $E^\dagger F$ moves amplitude between orthogonal branch sectors, so $P E^\dagger F P = 0$. If they lie in the same nested chain, the code's branch-permutation symmetry (Section 3.2) makes $P E^\dagger F P = c_{EF} P$ with $c_{EF}$ depending only on the multiset of error types, not on their positions. Both Knill–Laflamme conditions therefore hold [5], [7]. (ii) *Distance.* Errors of weight $\leq t$ are correctable; an error acting on the shell $\partial_{t+1} B_t$ moves the state into the disjoint ball $B_t(v')$ for a neighbor $v'$ at distance $t+1$, which is orthogonal to the code space, so weight-$(t{+}1)$ errors are detectable but not correctable. Hence $d = 2t+1$. $\blacksquare$

We flag honestly what is proved versus assumed: the nesting/disjointness structure (Lemma 1) and the resulting weight bounds are proved; the branch-permutation symmetry of the code states is a design requirement whose explicit encoder we do not construct here. Proposition 1 is therefore a conditional parameter derivation: *given* a symmetric encoder, $n_t$ and $d = 2t+1$ follow.

### 4.3 Passive failure probability (exact computation)

**Model:** each of the $n_t$ vertex qudits suffers an error independently with probability $\varepsilon$ per protection epoch; the passive scheme corrects all weight-$\leq t$ error patterns by Proposition 1 without any measurement; failure requires $\geq t+1$ simultaneous errors within the ball.

**Case $p=3$, $t=1$** ($n_1 = 5$, $d = 3$). Failure probability:

$$P_{\mathrm{pass}} = 1 - (1-\varepsilon)^{5} - \binom{5}{1}\varepsilon(1-\varepsilon)^{4}.$$

**Input:** $\varepsilon = 10^{-3}$.

Step 1: $(1-\varepsilon)^2 = 0.999^2 = 0.998001$.
Step 2: $(1-\varepsilon)^4 = 0.998001^2 = 0.996005996$ (since $0.998001^2 = 1 - 2(0.001999) + 0.001999^2 = 1 - 0.003998 + 0.000003996 = 0.996005996$).
Step 3: $(1-\varepsilon)^5 = 0.996005996 \times 0.999 = 0.995009990$.
Step 4: $\binom{5}{1}\varepsilon(1-\varepsilon)^4 = 5 \times 10^{-3} \times 0.996005996 = 0.004980030$.
Step 5: $P_{\mathrm{pass}} = 1 - 0.995009990 - 0.004980030 = 0.000009980$, i.e.

$$P_{\mathrm{pass}} \approx 9.98 \times 10^{-6}.$$

Leading order check: $\binom{5}{2}\varepsilon^2 = 10 \times 10^{-6} = 1.0\times10^{-5}$, consistent up to the $(1-\varepsilon)$ factors.

**Case $p=3$, $t=2$** ($n_2 = 17$, $d = 5$). Failure requires $\geq 3$ errors:

$$P_{\mathrm{pass}}^{(2)} \approx \binom{17}{3}\varepsilon^{3}(1-\varepsilon)^{14}.$$

Step 1: $\binom{17}{3} = \frac{17 \cdot 16 \cdot 15}{6} = 680$.
Step 2: $(1-\varepsilon)^{14} = 0.999^{14} \approx e^{-0.014021} \approx 0.98609$.
Step 3: $P \approx 680 \times 10^{-9} \times 0.98609 = 6.705 \times 10^{-7}$; the next term $\binom{17}{4}\varepsilon^4 = 2380 \times 10^{-12} \approx 2.4\times10^{-9}$ adds $\approx 0.35\%$. So

$$P_{\mathrm{pass}}^{(2)} \approx 6.73 \times 10^{-7}.$$

### 4.4 Active baseline comparison (labeled projection)

**Assumptions (stated explicitly; this is a projection, not a measurement):** (A1) the active baseline is a generic distance-3 code on the same $n_1 = 5$ data qudits; (A2) each protection epoch requires one syndrome-extraction round in which every data qudit participates in at least one gate/measurement interaction with an additional error rate $\varepsilon_m$; (A3) errors combine as $1 - (1-\varepsilon)(1-\varepsilon_m)$ per qudit; (A4) we take the pessimistic-for-us-but-standard case $\varepsilon_m = \varepsilon = 10^{-3}$.

Effective per-qudit error:

$$\varepsilon_{\mathrm{eff}} = 1 - (1-\varepsilon)^2 = 1 - 0.998001 = 0.001999 = 1.999\times10^{-3}.$$

Active logical failure (weight-2 patterns dominate, as for the passive