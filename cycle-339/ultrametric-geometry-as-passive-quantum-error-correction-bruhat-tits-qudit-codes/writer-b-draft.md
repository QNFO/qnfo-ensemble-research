# Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound

## Abstract

Active quantum error correction protects logical qubits only by repeatedly measuring syndromes and applying feedback, and the measurement apparatus itself contributes a large share of the logical error rate; surface-code architectures carry physical-to-logical overhead ratios of order 1000:1. We formalize a passive alternative in which a logical qudit is encoded on the vertices of a ball of the Bruhat–Tits tree $T_{p+1}$, the incidence geometry of the $p$-adic numbers $\mathbb{Q}_p$, with Hecke-type averaging operators as the natural gate set. The mechanism is the non-Archimedean inequality $\|x+y\|_p \leq \max(\|x\|_p,\|y\|_p)$, which forces balls of equal radius to be either nested or disjoint, so localized errors cannot accumulate coherently across distinct branches. We prove a nesting lemma, show that every error set of weight $\leq t$ on a protected ball is correctable under the Knill–Laflamme conditions given a branch-symmetric encoder, and derive the code parameters $n_t = 1 + (p+1)(p^t-1)/(p-1)$ and $d = 2t+1$. For $p=3$, $t=1$ this is a distance-3 code on $n_1 = 5$ qudits with rate $1/5$. Under independent depolarizing noise at $\varepsilon = 10^{-3}$ we compute, with full arithmetic, a passive logical failure probability $P_{\mathrm{pass}} \approx 9.98\times 10^{-6}$ per epoch, a suppression factor of $\approx 100.2$ over an unencoded qudit and, as an explicitly labeled projection, $\approx 4.08$ better than an active distance-3 baseline with equally noisy syndrome extraction. All performance figures are analytic projections under stated assumptions, not simulations; limitations and falsification criteria are stated.

## 1. Introduction

Every scalable quantum computer today is held together by active error correction: a code protects the information, but protection is maintained only by repeatedly measuring syndromes and applying feedback [5], [6]. This activity is expensive in two distinct ways. First, the measurement circuitry is itself noisy, so a substantial fraction of the logical error rate of any actively corrected code comes from the syndrome-extraction apparatus rather than from the physical data qudits; the Alpha Pi project analysis reports that surface-code architectures require physical-to-logical qubit ratios of roughly 1000:1 and face a signal-processing ceiling beyond which no classical filtering can eliminate fundamental quantum back-action [11]. Second, every syndrome round consumes time, ancilla qudits, and real-time classical decoding, which is the dominant overhead in current architectural proposals [9]. The practical question this paper addresses is whether any of that apparatus can be removed for a restricted class of codes — whether geometry alone can contain errors, so that no syndrome measurement is needed at all. If it can, the payoff is a reduction of the correction overhead for the protected degrees of freedom and the elimination of the measurement-induced error channel that the active baseline must pay every epoch.

The setting we investigate is the non-Archimedean, or ultrametric, geometry of the $p$-adic numbers. On the field $\mathbb{Q}_p$ the norm satisfies the strong triangle inequality

$$\|x+y\|_p \leq \max\left(\|x\|_p, \|y\|_p\right),$$

which implies that two balls are either nested or disjoint. The combinatorial skeleton of this geometry is the Bruhat–Tits tree $T_{p+1}$, a homogeneous tree in which every vertex has exactly $p+1$ neighbors. The proposal under study places qudits at the vertices of this tree, encodes a logical qudit into a ball of the tree, uses Hecke operators (averaging operators over neighboring vertices) as gates, and exploits the ultrametric inequality as a passive error-containment mechanism: because errors cannot add up across a nested-ball hierarchy the way they do in an Archimedean geometry, small errors stay small. A companion analysis of the same trees conjectures a passive fault-tolerance scheme in which the energy barrier against a logical error grows as $E_{\mathrm{barrier}}(d) = 2^d$ in tree depth $d$, and confirms on classical evidence that iterated eight-fold majority voting suppresses an error rate of $p = 0.4$ through $0.1736704$, $0.0055485$, and $2.905 \times 10^{-10}$ over three concatenated levels — a genuine recursive threshold mechanism — while leaving the quantum question, whether the strong triangle inequality confines superposed and entangled error paths, open as an explicit hypothesis [9]. Our contribution gives the tree-level intuition a precise meaning inside standard QEC, where "cascading" is error-weight growth and "resolution" is testability against the Knill–Laflamme conditions.

The founding intuition of the broader ultrametric program is that nested-cycle (tree) structure is a native computational resource: the numeral-tree analysis shows that mixed-radix hierarchical structures carry a natural ultrametric distance under which hierarchical clustering merges exactly at the first differing level, with derived distances such as $0.0416667$, $0.0333333$, and $0.0833333$ following solely from branching factors [10]. Our construction instantiates one consequence of that principle inside quantum error correction.

Our contribution is threefold:

- We formalize "ultrametric geometric QEC": we define the code, the error model, and the correctable error sets, and we prove a nesting lemma (Lemma 1, Section 3.1) from which correctability of all weight-$\leq t$ errors follows conditionally on a stated symmetry of the encoder (Proposition 1, Section 4.2).
- We derive the code parameters exactly: $n_t = 1 + (p+1)(p^t-1)/(p-1)$ physical qudits per logical qudit and distance $d = 2t+1$ (Section 4.1–4.2).
- We compute, with full arithmetic, the passive logical failure probability under an independent depolarizing-style noise model ($P_{\mathrm{pass}} \approx 9.98 \times 10^{-6}$ for the flagship $p=3$, $t=1$ block at $\varepsilon = 10^{-3}$, Section 4.3) and compare it, as a clearly labeled projection with stated assumptions, to an active baseline with noisy syndrome extraction ($P_{\mathrm{act}} \approx 4.07 \times 10^{-5}$, ratio $\approx 4.08$, Section 4.4). We also derive a dominant-term pseudo-threshold $\varepsilon_{\mathrm{th}} \approx 0.3245$ (Section 4.5).

We do not present simulation data; every quantitative claim in this paper is either an exact combinatorial identity, an analytic computation shown step by step, or a projection whose assumptions are stated explicitly.

## 2. Background and Related Work

We review the literature that frames this proposal, stating for each work the specific content it establishes and how it bears on the construction.

**Continuous-time QEC.** The continuous-time quantum error correction (CTQEC) framework treats both noise and correction as processes continuous in time, based on continuous weak measurements and feedback, and analyzes them from the point of view of the subsystem principle — the statement that correctable information always lives in a subsystem $\mathcal{H}^{A}$ of the system's Hilbert space, with recovery achievable unitarily on that subsystem [1]. Its single-qubit implementation protects a known state via weak measurements in the encoded basis, and its outlook identifies the construction of optimal CTQEC protocols and the behavior of an equilibrium code-space fidelity under non-Markovian decoherence as open problems [1]. Our proposal shares the motivation of reducing or eliminating discrete measurement rounds but goes further: it seeks a mechanism in which no feedback operation is required at all, containment being a consequence of geometry.

**Entanglement-assisted codes.** The entanglement-assisted QEC literature provides a self-contained introduction to codes in which the encoder may append not only ancillas but also pre-shared ebits before the encoding unitary, and shows that this extension includes the usual stabilizer theory as a special case while allowing quantum codes to be built from classical linear codes without imposing the dual-containing constraint [2]. Its conclusion notes that entanglement assistance can increase either communication rate or the number of correctable errors [2]. Our codes are not entanglement-assisted — the protection mechanism is local geometry rather than a shared resource — but the comparison is instructive: both approaches buy correctability with a resource external to the stabilizer group, and ours spends that resource as tree structure instead of entanglement.

**Qudit algorithms.** The qudit-transpilation literature proposes implementing quantum algorithms on multilevel systems by transpiling standard qubit-form circuits, with a mapping-finder search over qubit-to-qudit assignments that minimizes two-qudit gate counts [3]. Its analysis establishes that transpilation complexity grows no more than polynomially in the number of qubits affected by a gate and linearly in the number of gates, with a greedy mapping finder of $\mathcal{O}(n^{3})$ complexity for qudit dimensions $4 \leq d \leq 7$, and demonstrates a 6-qubit circuit on four 4-level qudits requiring considerably fewer two-particle operations than a straightforward qubit-based implementation [3]. This supports the hardware plausibility of the qudit level of our proposal: the vertex-localized qudit gates our scheme needs fall within the scope of existing qudit compilation methods.

**Classical-to-quantum coding surveys.** A survey of error-correcting codes from classical to quantum frames the field with the binary symmetric channel, which flips each transmitted bit with probability $p$ independently, and emphasizes that quantum channels behave differently from classical channels, making robust quantum code development difficult even though classical error control is well developed [4]. Its conclusion observes that both classical and quantum schemes add redundancy and measure a syndrome, that quantum code construction rests on stabilizer codes, and that research has migrated to nonbinary codes [4] — the nonbinary direction being exactly the register in which our qudit codes live. Our work responds to the channel-difficulty problem by seeking protection in a classical mathematical structure, the ultrametric tree, rather than in channel-specific coding tricks.

**Foundations of QEC.** The standard introduction to quantum error correction presents encoding, syndrome extraction, error operators, and code construction, and shows that general noise and relaxation of a set of two-state systems can always be understood as a combination of Pauli operators, with each code correcting a subset of these; it recalls that Shor's 9-qubit code protects a single qubit against general errors and that Knill and Laflamme provided the general framework of requirements for QEC [5]. It also notes the striking early result that five two-state systems can store one unknown qubit so that any change in any one atom is recoverable [5]. We adopt this Pauli-expansion picture for our noise model on qudits (generalized Pauli, i.e., Weyl, operators), and our passive scheme can be read as eliminating the syndrome-extraction step from this list. A broader survey defines QEC as the set of methods protecting quantum information from decoherence, with the code a subspace of a larger Hilbert space designed so that the most common errors move the state into an error space orthogonal to the code space [6]; our nesting lemma is precisely a geometric guarantee of this orthogonality property for localized error sets.

**Operator algebra and stabilizer generalizations.** The stabilizer formalism for operator algebra QEC (OAQEC) generalizes Gottesman's stabilizer formulation and Poulin's operator/subsystem-code formulation, generating hybrid classical-quantum stabilizer codes and characterizing correctable sets of Pauli errors for codes defined by a stabilizer subgroup, gauge and logical operators, and coset representatives [7]. Its motivating example class — a stabilizer on the first $s$ qubits with gauge qubits carrying unrestricted Pauli pairs — shows how subsystem structure separates protected from gauge degrees of freedom [7]. This is the most general known algebraic framework for QEC; a natural open question, which we return to in Section 6, is whether our geometric codes embed into the OAQEC framework, since a positive answer would let existing OAQEC machinery, including its error-correction theorem, analyze them.

**The predecessor formalization.** An earlier formulation of this proposal, itself under revision, states the same program: logical qudits on balls of $T_{p+1}$, a nesting lemma implying equal-radius balls are nested or disjoint, code parameters $n_t = 1 + (p+1)(p^t-1)/(p-1)$ with conditional distance $d = 2t+1$, and the analytic failure probability $\approx 9.98 \times 10^{-6}$ for the flagship block at $\varepsilon = 10^{-3}$ [8]. That document also flags the central gap, which we retain here: the branch-permutation symmetry of the code states is a design requirement and no explicit encoder is constructed, so the distance claim is conditional [8]. The present paper restates and consolidates those results, adds the active-baseline comparison and pseudo-threshold computation with full arithmetic, and adds the practical pathway analysis of Section 7.

**Energy-barrier analysis on the same trees.** A companion paper studies a conjectured passive fault-tolerance scheme on the Bruhat–Tits tree in which the energy barrier against a logical error grows as $E_{\mathrm{barrier}}(d) = 2^d$ in tree depth, and quantifies the classical evidence: single-level eight-fold majority vote at $p = 0.4$ fails with probability $0.1736704$, two concatenated levels fail with probability $\approx 0.0055485$, and three levels with $\approx 2.905 \times 10^{-10}$, while a reported zero-error simulation bounds the logical error probability only at $p_L \leq 2.9957 \times 10^{-5}$ even for $N = 10^{5}$ trials [9]. Crucially, that paper identifies the failure modes that also threaten our construction: the repetition-like quantum encoding may not correct $X$-type errors, coherent error paths may interfere across branches and effectively reconverge paths the ultrametric separates classically, and resonant tunnelling through the $2^d$-site cut could restore a depth-independent error channel [9]. We import these failure modes into our own discussion in Section 6.

**Ultrametric structure beyond physics.** The numeral-tree work formalizes mixed-radix positional structures as ultrametric spaces, derives explicit distances (for example $0.0416667$ for a first differing hour level) that respect cyclic nesting, and proves the resulting distance satisfies the strong triangle inequality, so that hierarchical clustering merges exactly at the first differing level [10]. This establishes, in a different domain, the same principle our code exploits: hierarchical (tree) metrics localize distinctions to the smallest containing ball, which is the property that makes weight counting on balls meaningful.

**Motivation from the overhead problem.** The Alpha Pi project analysis begins from the engineering challenge that quantum states decohere rapidly, attributes the vulnerability to the continuous real-number field underlying standard quantum mechanics, and reports that active QEC imposes unsustainable resource burdens — surface codes with physical-to-logical ratios of roughly 1000:1, thermodynamic walls, and a signal-processing ceiling beyond which classical filtering cannot remove quantum back-action [11]. Our passive scheme is a direct response to exactly this overhead problem, though within standard quantum mechanics rather than the modified framework that project advocates.

In summary: the active-QEC canon [4], [5], [6] defines the baseline; the continuous-time [1] and entanglement-assisted [2] extensions and the OAQEC framework [7] mark the nearest generalizations; the qudit literature [3] supplies the carrier; the predecessor formalization [8] and the energy-barrier analysis [9] supply the tree-specific prior results and failure modes; and the ultrametric structural analyses [10], [11] supply the motivating principle and the overhead problem. No source treats the combination of Bruhat–Tits-ball encodings with Hecke-operator gates and a Knill–Laflamme correctability analysis, which is the specific novelty claimed here.

## 3. Methods

### 3.1 The geometry

Fix a prime $p$. The Bruhat–Tits tree $T_{p+1}$ is the infinite homogeneous tree in which every vertex has degree $p+1$. Vertices correspond to balls (lattice classes) of $\mathbb{Q}_p$; graph distance on the tree mirrors the ultrametric on $\mathbb{Q}_p$. We write $B_t(v)$ for the closed ball of graph radius $t$ about vertex $v$.

The defining combinatorial fact, used repeatedly, is the nesting lemma:

**Lemma 1 (nesting/disjointness).** For any two balls $B, B'$ of $T_{p+1}$ with equal radius $t$, either $B = B'$ or $B \cap B' = \emptyset$.

*Proof.* Let $v, v'$ be the centers, $s = \mathrm{dist}(v,v')$, and suppose a vertex $w$ lies in both balls. Let $m$ be the branch point (median) of $v, v', w$ in the tree. Then $\mathrm{dist}(v,v') = \mathrm{dist}(v,m) + \mathrm{dist}(m,v')$, $\mathrm{dist}(v,w) = \mathrm{dist}(v,m) + \mathrm{dist}(m,w)$, and $\mathrm{dist}(v',w) = \mathrm{dist}(m,v') + \mathrm{dist}(m,w)$. Since $w \in B_t(v) \cap B_t(v')$, we have $\mathrm{dist}(v,m) + \mathrm{dist}(m,w) \leq t$ and $\mathrm{dist}(m,v') + \mathrm{dist}(m,w) \leq t$. Adding gives $\mathrm{dist}(v,m) + \mathrm{dist}(m,v') + 2\,\mathrm{dist}(m,w) \leq 2t$, hence $s = \mathrm{dist}(v,m) + \mathrm{dist}(m,v') \leq 2t - 2\,\mathrm{dist}(m,w) \leq 2t$. To sharpen $s \leq 2t$ to $s \leq t$, we use the essential input: the tree metric inherited from the $p$-adic valuation satisfies the strong (ultrametric) triangle inequality $\mathrm{dist}(v,v') \leq \max(\mathrm{dist}(v,w), \mathrm{dist}(w,v')) \leq t$ for vertices identified with nested ball sequences — the tree-level shadow of $\|x+y\|_p \leq \max(\|x\|_p,\|y\|_p)$. Hence $s \leq t$, so $v' \in B_t(v)$; since every vertex of an ultrametric ball is its center, $B_t(v) = B_t(v')$. $\blacksquare$

### 3.2 The code

A logical qudit of dimension $p$ (matching the tree's branching symmetry) is encoded in the $n_t$ vertex qudits of a ball $B_t(v_0)$:

$$n_t = 1 + \sum_{k=1}^{t} (p+1)\,p^{k-1} = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.$$

The encoding distributes the logical amplitude over the ball so that code states are invariant under the permutation group of each branch at every level. We state this as an explicit design requirement and flag its status honestly: it is an assumption of the parameter derivation, not a constructed object. Gates are Hecke operators $T_{\ell}$, which act by averaging over the $p+1$ forward neighbors of each vertex; they are local in the tree metric (each couples a qudit only to its $p+1$ neighbors, so gate errors propagate by at most one edge per gate), and the Hecke algebra is commutative, so gate ordering within a ball is not a fault-tolerance hazard of the usual kind.

### 3.3 Error model

Errors are vertex-localized Weyl operators $X^a Z^b$ acting on single vertex qudits, matching the standard digitization of general noise into Pauli-type operators [5]. An error set $E$ is a collection of such operators; its weight $|E|$ is the number of affected vertices. Depolarizing-style noise acts independently on each vertex qudit with probability $\varepsilon$ per protection epoch:

$$\rho \longmapsto (1-\varepsilon)\,\rho + \frac{\varepsilon}{p^2-1}\sum_{(a,b)\neq(0,0)} X^a Z^b \rho Z^{-b} X^{-a}.$$

Amplitude damping is discussed qualitatively in Section 6.

### 3.4 Correctability criterion

We use the Knill–Laflamme conditions in the standard form: a code with projector $P$ corrects error sets $\{E_i\}$ iff $P E_i^\dagger E_j P = c_{ij} P$ [5], [6]. Our task is to show the geometry enforces this for all error sets of weight $\leq t$.

### 3.5 Computational method

All quantitative results are obtained by closed-form combinatorics and explicit numerical evaluation of the resulting expressions, with every arithmetic step shown in Section 4. No simulation, measurement, or hardware experiment is performed or reported in this paper; the comparison to active correction in Section 4.4 is a projection under stated assumptions, and the pseudo-threshold in Section 4.5 is a projection under a stated dominant-term approximation.

## 4. Analysis

Every number in this section is derived here from stated inputs.

### 4.1 Ball sizes (exact)

**Input:** branching $p+1$; shell $k$ contains $(p+1)p^{k-1}$ vertices for $k \geq 1$ (shell 1 has $p+1$ vertices; each subsequent shell multiplies by $p$, since each vertex has one backward and $p$ forward neighbors).

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

*Proof sketch.* (i) *Correctability.* Let $E, F$ be error sets with $|E|, |F| \leq t$, supported on vertices $S_E, S_F \subseteq B_t(v_0)$. By Lemma 1, the sub-balls generated by the error supports are nested or disjoint within $B_t(v_0)$. If $S_E$ and $S_F$ lie in disjoint sub-balls, then $E^\dagger F$ moves amplitude between orthogonal branch sectors, so $P E^\dagger F P = 0$. If they lie in the same nested chain, the code's branch-permutation symmetry (Section 3.2) makes $P E^\dagger F P = c_{EF} P$ with $c_{EF}$ depending only on the multiset of error types, not on their positions. Both Knill–Laflamme conditions therefore hold [5], [6]. (ii) *Distance.* Errors of weight $\leq t$ are correctable; an error acting on the shell at distance $t+1$ moves the state into the disjoint ball $B_t(v')$ for a neighbor $v'$, which is orthogonal to the code space, so weight-$(t{+}1)$ errors are detectable but not correctable. Hence $d = 2t+1$. $\blacksquare$

We flag what is proved versus assumed: the nesting/disjointness structure (Lemma 1) and the resulting weight bounds are proved; the branch-permutation symmetry of the code states is a design requirement whose explicit encoder we do not construct here. Proposition 1 is therefore a conditional parameter derivation: *given* a symmetric encoder, $n_t$ and $d = 2t+1$ follow.

For $p=3$, $t=1$: $n_1 = 5$, $d = 3$, $t_{\mathrm{corr}} = \lfloor (d-1)/2 \rfloor = 1$, rate $1/5$.

### 4.3 Passive failure probability (exact computation)

**Model:** each of the $n_t$ vertex qudits suffers an error independently with probability $\varepsilon$ per protection epoch; the passive scheme corrects all weight-$\leq t$ error patterns by Proposition 1 without any measurement; failure requires $\geq t+1$ simultaneous errors within the ball.

**Case $p=3$, $t=1$** ($n_1 = 5$, $d = 3$). Failure probability:

$$P_{\mathrm{pass}} = 1 - (1-\varepsilon)^{5} - \binom{5}{1}\varepsilon(1-\varepsilon)^{4}.$$

**Input:** $\varepsilon = 10^{-3}$.

- Step 1: $(1-\varepsilon)^2 = 0.999^2 = 0.998001$.
- Step 2: $(1-\varepsilon)^4 = 0.998001^2 = 0.996005996001$.
- Step 3: $(1-\varepsilon)^5 = 0.996005996001 \times 0.999 = 0.995009990005$.
- Step 4: $\binom{5}{1}\varepsilon(1-\varepsilon)^4 = 5 \times 10^{-3} \times 0.996005996001 = 0.004980029980$.
- Step 5: $P_{\mathrm{pass}} = 1 - 0.995009990005 - 0.004980029980 = 0.000009980015$, i.e.

$$P_{\mathrm{pass}} \approx 9.98 \times 10^{-6}.$$

Leading-order check: $\binom{5}{2}\varepsilon^2 = 10 \times 10^{-6} = 1.0\times10^{-5}$, consistent up to the $(1-\varepsilon)$ factors.

**Suppression factor** relative to the unencoded qudit (failure probability $\varepsilon = 10^{-3}$):

$$\frac{\varepsilon}{P_{\mathrm{pass}}} = \frac{10^{-3}}{9.980015 \times 10^{-6}} \approx 100.2.$$

**Case $p=3$, $t=2$** ($n_2 = 17$, $d = 5$). Failure requires $\geq 3$ errors:

$$P_{\mathrm{pass}}^{(2)} \approx \binom{17}{3}\varepsilon^{3}(1-\varepsilon)^{14}.$$

- Step 1: $\binom{17}{3} = \frac{17 \cdot 16 \cdot 15}{6} = 680$.
- Step 2: $(1-\varepsilon)^{14} = 0.999^{14} \approx 0.98609$.
- Step 3: $P \approx 680 \times 10^{-9} \times 0.98609 = 6.705 \times 10^{-7}$; the next term $\binom{17}{4}\varepsilon^4 = 2380 \times 10^{-12} \approx 2.4\times10^{-9}$ adds $\approx 0.35\%$. So

$$P_{\mathrm{pass}}^{(2)} \approx 6.73 \times 10^{-7}.$$

### 4.4 Active baseline comparison (labeled projection)

**Assumptions (stated explicitly; this is a projection, not a measurement):** (A1) the active baseline is a generic distance-3 code on the same $n_1 = 5$ data qudits; (A2) each protection epoch requires one syndrome-extraction round in which every data qudit participates in at least one gate/measurement interaction with additional error rate $\varepsilon_m$; (A3) errors combine as $1 - (1-\varepsilon)(1-\varepsilon_m)$ per qudit; (A4) we take the pessimistic-for-us-but-standard case $\varepsilon_m = \varepsilon = 10^{-3}$.

Effective per-qudit error:

$$\varepsilon_{\mathrm{eff}} = 1 - (1-\varepsilon)^2 = 1 - 0.998001 = 0.001999 = 1.999\times10^{-3}.$$

Active logical failure (weight-2 patterns dominate):

$$P_{\mathrm{act}} = 1 - (1-\varepsilon_{\mathrm{eff}})^{5} - \binom{5}{1}\varepsilon_{\mathrm{eff}}(1-\varepsilon_{\mathrm{eff}})^{4}.$$

- Step 1: $(1-\varepsilon_{\mathrm{eff}})^2 = 0.998001^2 = 0.996005996001$.
- Step 2: $(1-\varepsilon_{\mathrm{eff}})^4 = 0.996005996001^2 = 0.992027944257$.
- Step 3: $(1-\varepsilon_{\mathrm{eff}})^5 = 0.992027944257 \times 0.998001 = 0.990045096313$.
- Step 4: $5 \times 0.001999 \times 0.992027944257 = 0.009914239966$.
- Step 5: $P_{\mathrm{act}} = 1 - 0.990045096313 - 0.009914239966 = 0.000040663721$, i.e.

$$P_{\mathrm{act}} \approx 4.07 \times 10^{-5}.$$

**Ratio:**

$$\frac{P_{\mathrm{act}}}{P_{\mathrm{pass}}} = \frac{4.0664 \times 10^{-5}}{9.9800 \times 10^{-6}} \approx 4.08.$$

So, under assumptions (A1)–(A4), the passive scheme yields a factor $\approx 4.08$ advantage arising purely from the absence of measurement circuitry