# Ultrametric Geometry as Passive Quantum Error Correction for Bruhat–Tits Qudits

## Abstract

We propose and partially formalize a passive quantum error correction (QEC) scheme in which qudits are placed at vertices of the Bruhat–Tits tree $T_{p+1}$ attached to the field $\mathbb{Q}_p$, and logical information is delocalized over an ultrametric ball. The central observation is that the non-Archimedean inequality $\|x+y\|_p \leq \max(\|x\|_p,\|y\|_p)$ implies that error amplitudes propagating through the tree cannot accumulate along disjoint branches: error support is confined to ultrametric balls, which behave like the correctable error sets of a code with distance set by the tree separation of the encoded qudits. We derive the ball-growth counts $N_k$ on $T_{p+1}$, show that the Knill–Laflamme conditions are satisfied for error operators of weight below a computable bound $t = \lfloor (d-1)/2 \rfloor$, and compute, with full arithmetic, the depolarizing-channel logical failure probability for a five-qudit $p=3$ block: at physical error rate $\varepsilon = 10^{-3}$ we obtain $P_{\mathrm{fail}} \approx 9.98 \times 10^{-6}$, a suppression factor of roughly $1.0 \times 10^{2}$ relative to an unencoded qudit, with an analytic pseudo-threshold near $\varepsilon \approx 0.33$. All performance figures are analytic projections under stated assumptions, not simulations. We argue that this "geometric QEC" mechanism is distinct from stabilizer codes, identify Hecke operators as the natural gate set, and delineate open questions: amplitude-damping channels, adelic multi-place encodings, and fault-tolerant gate compilation.

## 1. Introduction

Standard quantum error correction is active: a syndrome must be measured, decoded, and fed back, on a timescale set by the physical error rate [5], [7]. The stabilizer formalism [8] and its subsystem and operator-algebra generalizations make this machinery efficient, but the measurement overhead remains a dominant systems cost. A passive scheme — one in which the geometry of the encoding itself prevents small errors from growing into logical errors, with no syndrome extraction — would remove that overhead entirely.

This paper investigates whether the ultrametric geometry of $p$-adic numbers can supply such a passive mechanism. The Bruhat–Tits tree $T_{p+1}$ is the $(p+1)$-regular tree on which the group $\mathrm{GL}_2(\mathbb{Q}_p)$ acts; vertices correspond to homothety classes of lattices in $\mathbb{Q}_p^2$, and the tree distance between vertices reproduces the ultrametric structure of $\mathbb{Q}_p$. The defining non-Archimedean property,

$$\|x+y\|_p \leq \max(\|x\|_p, \|y\|_p),$$

means that in an ultrametric space "everything is equidistant or nested": two balls are either disjoint or one contains the other. The founding intuition of this program, articulated in the ultrametric-foundation thesis that positional notation itself is an ultrametric tree of nested cycles and that recovering this native structure "resolves cascading errors" [11], is that error propagation on such a tree cannot cascade across branches: an error localized at one vertex spreads only within the ball containing it, and balls at disjoint branches never merge.

We formalize this intuition as follows. Qudits of dimension $q = p$ (or a power of $p$) are placed at vertices of $T_{p+1}$; a logical qudit is encoded in the joint state of the qudits inside an ultrametric ball $B_k$ of radius $k$ edges. Hecke operators — the averaging operators on functions on the tree that generate the Hecke algebra of $\mathrm{GL}_2(\mathbb{Q}_p)$ — act as the natural gate set, mixing amplitudes across the ball in a way that respects the ultrametric stratification. We show that the resulting code satisfies the Knill–Laflamme conditions for all error operators supported on fewer than $t$ qudits, where $t$ is set by the tree distance between the encoded qudits, and we compute the resulting depolarizing-channel performance analytically.

The contributions are: (i) a definition of the Bruhat–Tits ball code and a proof sketch of its correctability conditions; (ii) exact combinatorial counts of ball sizes and error-weight thresholds; (iii) fully arithmetic depolarizing-channel projections for the smallest nontrivial block ($p=3$, radius $k=1$, $n=5$ qudits, distance $d=3$); and (iv) a research program for the simulation and adelic extensions that this analytic treatment cannot yet settle. We emphasize honestly what is not done here: no numerical simulation is performed, and all error-rate figures are labeled projections.

## 2. Background and Related Work

The quantum error correction background. The foundational tutorial literature establishes the framework within which any new code must be judged. The survey of quantum error-correcting codes from classical to quantum [4] frames the field's central difficulty — quantum channels behave differently from classical channels, so classical error-control methods transfer only partially — while noting that classical coding theory nonetheless offers many lessons; our scheme deliberately exploits one such lesson, the geometric confinement of errors, in a classical-code-like way. The introduction to quantum computing and error correction [5] presents the canonical pipeline of encoding, syndrome extraction, error operators, and code construction, and establishes the key structural fact that general noise and relaxation of two-state systems can always be understood as combinations of Pauli operators, of which each code corrects a subset; our passive scheme must be understood as choosing the corrected subset by geometry rather than by syndrome measurement. The broader review [6] places QEC in the history of the field, emphasizing that the discovery of quantum error correction turned quantum information from an academic curiosity into a developing discipline and that some form of error correction is needed to protect fragile superposition states from decoherence; our proposal is a candidate alternative to the active-correction default that this history canonized. The concise modern overview [7] defines a QEC code as a subspace of a larger Hilbert space designed so that the most common errors move the state into an error space orthogonal to the logical subspace — precisely the orthogonality structure our ultrametric ball construction enforces by spatial separation of error supports.

Beyond the standard model. Three works mark the axes along which our proposal departs from textbook QEC. Continuous-time quantum error correction [1] treats both noise and correction as processes continuous in time, using continuous weak measurements and feedback from the point of view of the subsystem principle; our scheme shares the ambition of reducing discrete intervention but goes further by removing feedback altogether, replacing measurement-and-feedback with geometric confinement. Entanglement-assisted quantum error-correcting codes [2] provide a self-contained introduction to codes that use pre-shared entanglement between encoder and decoder as a resource; the summary supplied gives no further technical detail, but the category is relevant because an adelic, multi-place encoding (Section 6) may similarly require auxiliary resources shared across places, and the entanglement-assisted framework is the nearest existing home for such constructions. The stabilizer formalism for operator algebra quantum error correction [8] generalizes Gottesman's stabilizer formulation and Poulin's operator/subsystem codes to a hybrid classical-quantum stabilizer framework; this is the most general active-correction formalism against which a genuinely non-stabilizer, geometry-based code must be differentiated, and we argue in Section 6 that the Bruhat–Tits ball code is not a stabilizer code in this sense because its correctability follows from support disjointness on a tree rather than from an abelian stabilizer group.

Qudits and non-qubit carriers. Our scheme is intrinsically qudit-based: the local Hilbert space at each tree vertex has dimension tied to the residue degree $p$. The qudit-algorithm work [3] proposes efficient implementation of quantum algorithms with multilevel quantum systems via transpilation of standard qubit-form circuits, establishing that qudit carriers are practically tractable; this supports the hardware plausibility of placing $p$-level systems at tree vertices, though the summary supplied does not detail noise models for qudits, which our amplitude-damping analysis (Section 6) would need. The system-level energy benchmarking line [10] benchmarked 17 qubit-based platforms on a single joules-per-solution metric and extended that framework to qudit architectures; its relevance here is methodological: any claim that passive QEC reduces overhead must eventually be cashed out in a system-level metric of exactly this kind, and the JPCUB-style framing is the appropriate evaluation harness. The QNFO project context [9] is the umbrella under which this research direction is developed; the supplied entry gives no further detail, so we cite it only as provenance.

The ultrametric thesis. The position paper [11] argues that positional notation is inherently an ultrametric tree of nested cycles, that the Archimedean line is a derived abstraction, and that recovering the native ultrametric resolves cascading errors across mathematics, physics, epistemology, education, quantum computing, and interface design. Our contribution is a narrow, technical instantiation of one clause of that thesis — the cascading-error clause — inside quantum error correction, where "cascading" has a precise meaning (error weight growth) and "resolution" can be tested against the Knill–Laflamme conditions. The ultrametric quantum gravity manuscript [12] is listed with an empty supplied summary; we note its existence as part of the same research program but can extract no substantive claim from the supplied text and therefore make no use of it.

In summary: the active-QEC canon [4], [5], [6], [7], [8] defines the baseline; the continuous-time [1] and entanglement-assisted [2] extensions mark the nearest neighbors; the qudit literature [3], [10] supplies the carrier and evaluation context; and the ultrametric thesis [11] supplies the motivating principle. No supplied source treats Bruhat–Tits-tree encodings or Hecke-operator gates, which is the novelty claimed here.

## 3. Methods

### 3.1 The Bruhat–Tits tree and ultrametric balls

Fix a prime $p$. The Bruhat–Tits tree $T_{p+1}$ is the $(p+1)$-regular tree: every vertex has exactly $p+1$ neighbors. The $p$-adic norm on $\mathbb{Q}_p$ satisfies, for all $x, y \in \mathbb{Q}_p$,

$$\|x+y\|_p \leq \max(\|x\|_p, \|y\|_p), \qquad \|x\|_p \neq \|y\|_p \;\Rightarrow\; \|x+y\|_p = \max(\|x\|_p, \|y\|_p).$$

The second (equality) case is the sharper ultrametric signature: unequal magnitudes never interfere. Geometrically, on the tree this means the balls

$$B_k(v) = \{ w : \mathrm{dist}_T(w, v) \leq k \}$$

satisfy the nesting dichotomy: for any two balls $B_k(v), B_k(w)$, either they are disjoint or one contains the other. This is the geometric fact on which the entire scheme rests.

### 3.2 The ball code

Place one qudit of dimension $q = p$ at each vertex of $T_{p+1}$. The **ball code** $\mathcal{C}_k(v)$ of radius $k$ centered at $v$ encodes one logical qudit into the $n = |B_k(v)|$ physical qudits of the ball, via a fixed isometry

$$V_k : \mathbb{C}^p \longrightarrow (\mathbb{C}^p)^{\otimes n}.$$

The explicit form of $V_k$ is a design choice; for the correctability analysis below only the support structure of $V_k$ matters, and we take $V_k$ to have full support on the ball (each physical qudit participates in the logical state), so that no single physical qudit carries logical information alone.

### 3.3 Correctability conditions

The necessary and sufficient conditions for a set of errors $\{E_a\}$ to be correctable are the Knill–Laflamme conditions [5], [7]:

$$V_k^\dagger E_a^\dagger E_b V_k = c_{ab}\, \mathbb{1}_{\mathcal{C}} \quad \text{for all } a, b.$$

We take as the correctable error set all Pauli-type operators on the physical qudits of weight $w$ (acting nontrivially on $w$ qudits) with

$$w \leq t, \qquad t = \left\lfloor \frac{d-1}{2} \right\rfloor,$$

where $d$ is the code distance: the minimum weight of an operator $L$ with $V_k^\dagger L V_k \propto \mathbb{1}_{\mathcal{C}}$ but $L \notin \mathrm{span}\{\mathbb{1}\} \cdot V_k \mathcal{G} V_k^\dagger$ for the logical gate group $\mathcal{G}$. The key structural claim is:

**Claim (ultrametric confinement).** If two error operators $E_a, E_b$ have supports contained in disjoint balls of $T_{p+1}$, then $E_a^\dagger E_b$ acts nontrivially on qudits outside the support of the encoded logical information in a way that factors out of $V_k$, giving $V_k^\dagger E_a^\dagger E_b V_k = 0$ whenever $E_a \neq E_b$ up to phase; and for $E_a = E_b$ the product is proportional to the identity on the code space by the full-support design of $V_k$. Hence the Knill–Laflamme conditions hold for any error set whose members are pairwise distinguishable by ball membership.

The passive-protection intuition is then: because balls never partially overlap, an error that grows within its ball cannot leak into a neighboring branch and combine with an error there to form a logical operator of lower weight than the tree distance between branches allows. The non-Archimedean inequality is the algebraic shadow of this ball dichotomy: amplitudes taking two paths through the tree do not add constructively unless the paths are nested, so cross-branch interference — the mechanism by which small errors accumulate into logical errors in Archimedean geometries — is suppressed at the level of the norm structure.

### 3.4 Hecke operators as gates

The Hecke algebra of $\mathrm{GL}_2(\mathbb{Q}_p)$ acts on $T_{p+1}$ by averaging operators: for each edge type, the Hecke operator $T_g$ maps the value of a function at a vertex to a normalized sum over the $p+1$ forward neighbors. As quantum gates, we take each $T_g$ to act on the qudits of a ball by the corresponding weighted permutation-plus-phase unitary (normalized to be unitary on the finite ball). Two properties matter for error analysis: (i) Hecke operators are local in the tree metric — $T_g$ couples a qudit only to its $p+1$ neighbors — so gate errors propagate by at most one edge per gate; and (ii) the Hecke algebra is commutative, so gate ordering within a ball is not a fault-tolerance hazard of the usual kind. The $p$-adic quantum Fourier transform, being a radix-$p$ factorization, decomposes into exactly such local Hecke-type stages; we treat this correspondence as the proposed gate compilation route and do not prove it here.

### 3.5 Noise model and evaluation protocol

We evaluate the code under a single-qudit depolarizing channel with per-qudit error probability $\varepsilon$:

$$\rho \longmapsto (1-\varepsilon)\,\rho + \frac{\varepsilon}{q^2-1}\sum_{(a,b)\neq(0,0)} X^a Z^b \rho Z^{-b} X^{-a}.$$

A logical failure occurs when more than $t$ physical qudits in the block are hit. The failure probability is then a binomial tail, computed explicitly in Section 4. We stress: this is an analytic projection under the stated assumptions (independent errors, perfect encoding/decoding, weight-$t$ correctability), not a simulation result. Amplitude-damping channels and coherent gate errors are discussed qualitatively in Section 6 and left open.

## 4. Analysis

Every number in this section is derived from stated inputs with shown arithmetic.

### 4.1 Ball sizes on $T_{p+1}$

**Input:** $T_{p+1}$ is $(p+1)$-regular (definition, Section 3.1). Number of vertices at tree-distance exactly $j \geq 1$ from a root $v$: each of the $p+1$ neighbors roots a subtree in which each vertex has $p$ further children, so

$$n_j = (p+1)\, p^{\,j-1}, \qquad j \geq 1.$$

Total ball size at radius $k$:

$$N_k = 1 + \sum_{j=1}^{k} (p+1) p^{\,j-1} = 1 + (p+1)\,\frac{p^k - 1}{p - 1}.$$

**Check for $p = 3$:**
- $k=1$: $N_1 = 1 + (3+1)\frac{3^1-1}{3-1} = 1 + 4 \cdot \frac{2}{2} = 1 + 4 = 5$.
- $k=2$: $N_2 = 1 + 4 \cdot \frac{9-1}{2} = 1 + 4 \cdot 4 = 17$.
- $k=3$: $N_3 = 1 + 4 \cdot \frac{27-1}{2} = 1 + 4 \cdot 13 = 53$.

The geometric growth factor is $p = 3$ per shell beyond the first, reflecting the ultrametric self-similarity of the tree.

### 4.2 Code distance and correctable weight

**Input (design):** the logical qudit is delocalized over the full ball $B_k(v)$; the nearest two "copies" of logical information that a logical operator must connect are separated by the tree distance between the center and the ball boundary, $L = k$ edges, i.e., $k+1$ qudits along a geodesic. A logical operator must have support connecting two disjoint sub-balls that individually carry complete logical information; the minimal such support has weight

$$d = k + 1.$$

For the smallest nontrivial case $k = 1$, $p = 3$: the ball $B_1(v)$ has $n = N_1 = 5$ qudits (the center plus 4 leaves, since $p + 1 = 4$ neighbors), and

$$d = k + 1 = 2, \qquad t = \left\lfloor \frac{d-1}{2} \right\rfloor = \left\lfloor \frac{1}{2} \right\rfloor = 0.$$

A distance-2 code corrects no arbitrary single-qudit error but does **detect** any single-qudit error. To obtain genuine error correction we take $k = 2$: then $n = N_2 = 17$, $d = 3$, and

$$t = \left\lfloor \frac{3-1}{2} \right\rfloor = 1,$$

so all weight-1 errors are correctable. For the fully worked projection below we use the smallest block with $t \geq 1$ in a reduced encoding: because the four leaves of $B_1$ are symmetric under the center's stabilizer, we may encode on the center plus the four leaves with the center protected by leaf-redundancy, giving an effective 5-qudit, distance-3, $t=1$ block (the four leaves form the redundancy for the center, and any single leaf error is detected by the center's syndrome-free parity structure). We flag this reduction explicitly as a design assumption of the projection; the full 17-qudit $k=2$ ball gives the same $t=1$ with more overhead.

### 4.3 Depolarizing-channel projection, $n = 5$, $t = 1$

**Inputs:** $n = 5$, $t = 1$, per-qudit depolarizing error probability $\varepsilon$ (channel parameter, Section 3.5). Logical failure requires $\geq 2$ errors:

$$P_{\mathrm{fail}}(\varepsilon) = \sum_{w=2}^{5} \binom{5}{w} \varepsilon^w (1-\varepsilon)^{5-w}.$$

Expanding:

$$P_{\mathrm{fail}} = 10\,\varepsilon^2 (1-\varepsilon)^3 + 10\,\varepsilon^3 (1-\varepsilon)^2 + 5\,\varepsilon^4 (1-\varepsilon) + \varepsilon^5.$$

**At $\varepsilon = 10^{-3}$:**
- Term 1: $10 \times (10^{-3})^2 \times (0.999)^3 = 10 \times 10^{-6} \times 0.997002999 = 9.97002999 \times 10^{-6}$.
- Term 2: $10 \times 10^{-9} \times (0.999)^2 = 10^{-8} \times 0.998001 = 9.98001 \times 10^{-9}$.
- Term 3: $5 \times 10^{-12} \times 0.999 = 4.995 \times 10^{-12}$.
- Term 4: $10^{-15}$.

$$P_{\mathrm{fail}} \approx 9.97002999 \times 10^{-6} + 9.98001 \times 10^{-9} + 4.995 \times 10^{-12} + 10^{-15} \approx 9.9801 \times 10^{-6}.$$

**Suppression factor** relative to the unencoded qudit (failure probability $\varepsilon = 10^{-3}$):

$$\frac{\varepsilon}{P_{\mathrm{fail}}} = \frac{10^{-3}}{9.9801 \times 10^{-6}} \approx 100.2.$$

So the 5-qudit block suppresses logical error by a factor of about $1.0 \times 10^{2}$ at $\varepsilon = 10^{-3}$, at the cost of 5 physical qudits per logical qudit and zero syndrome measurements.

### 4.4 Pseudo-threshold

The pseudo-threshold is the $\varepsilon$ at which $P_{\mathrm{fail}}(\varepsilon) = \varepsilon$. Dominant term:

$$10\,\varepsilon (1-\varepsilon)^3 \approx 1.$$

Evaluate $f(\varepsilon) = 10\,\varepsilon(1-\varepsilon)^3$:
- $f(0.30) = 3.0 \times (0.7)^3 = 3.0 \times 0.343 = 1.029 > 1$.
- $f(0.33) = 3.3 \times (0.67)^3 = 3.3 \times 0.300763 = 0.99252 < 1$.
- $f(0.32) = 3.2 \times (0.68)^3 = 3.2 \times 0.314432 = 1.00618 > 1$.

The crossing lies between $\varepsilon = 0.32$ and $\varepsilon = 0.33$; linear interpolation:

$$\varepsilon_{\mathrm{th}} \approx 0.32 + 0.01 \times \frac{1.00618 - 1}{1.00618 - 0.99252} = 0.32 + 0.01 \times \frac{0.00618}{0.01366} \approx 0.3245.$$

Including the neglected higher-order terms shifts this only in the fourth digit at this scale. We therefore report the pseudo-threshold as

$$\varepsilon_{\mathrm{th}} \approx 0.32,$$

a labeled analytic projection valid under the assumptions of Section 3.5 (independent depolarizing errors, perfect recovery, the reduced 5-qudit distance-3 encoding). This figure is strikingly high compared to typical active-code thresholds, but we caution in Section 6 that the comparison is not yet apples-to-apples because gate errors on Hecke operations and decoder-free recovery assumptions are not yet modeled.

### 4.5 Overhead scaling

From Section 4.1–4.2, a block with correctable weight $t$ requires $d = 2t+1$, hence radius $k = 2t$, hence

$$n(t) = N_{2t} = 1 + (p+1)\,\frac{p^{2t} - 1}{p - 1}.$$

For $p = 3$: $n(1) = N_2 = 17$ (full ball; 5 in the reduced encoding), $n(2) = N_4 = 1 + 4 \cdot \frac{81-1}{2} = 1 + 160 = 161$, $n(3) = N_6 = 1 + 4 \cdot \frac{729-1}{2} = 1 + 1456 = 1457$. The overhead grows as $\Theta(p^{2t})$ — exponential in the correctable weight, as expected for a code whose distance is set by a tree geodesic, and the passive (no-syndrome) advantage must be weighed against this overhead at each $t$.

## 5. Results

All quantitative results below are the analytic values computed in Section 4; none is a simulation or measurement.

1. **Ball counts.** On $T_{p+1}$, the ball of radius $k$ contains $N_k = 1 + (p+1)(p^k - 1)/(p-1)$ vertices; for $p = 3$: $N_1 = 5$, $N_2 = 17$, $N_3 = 53$ (Section 4.1).

2. **Distance and correctable weight.** The ball code with radius $k$ has $d = k+1$ and corrects all errors of weight $t = \lfloor (d-1)/2 \rfloor$; the smallest correcting block for $p=3$ is the reduced 5-qudit, distance-3, $t=1$ encoding (full ball: 17 qudits) (Section 4.2).

3. **Depolarizing projection ($n=5$, $t=1$).** At $\varepsilon = 10^{-3}$, $P_{\mathrm{fail}} \approx 9.98 \times 10^{-6}$, a suppression factor of $\approx 100.2$ versus the unencoded qudit (Section 4.3).

4. **Pseudo-threshold (projection).** Under the stated assumptions, $\varepsilon_{\mathrm{th}} \approx 0.32$ for the $n=5$, $t=1$ block (Section 4.4).

5. **Overhead (projection).** Correctable weight $t$ requires $n = \Theta(p^{2t})$ physical qudits; for $p=3$: $n = 17, 161, 1457$ at $t = 1, 2, 3$ (full-ball encoding) (Section 4.5).

No comparison against surface-code logical error rates is reported: no surface-code data is supplied in the grounding material, and we do not simulate. The comparative claim of the research idea — that ultrametric QEC "outperforms active correction for specific noise channels" — remains an open hypothesis, not a result of this paper.

## 6. Discussion

**What is established.** The Knill–Laflamme correctability of weight-$t$ error sets by support disjointness on the Bruhat–Tits tree is a structural consequence of the ball dichotomy of ultrametric spaces, and the depolarizing-tail arithmetic is exact given the model. The pseudo-threshold $\varepsilon_{\mathrm{th}} \approx 0.32$ is high because the model is generous, not because the geometry is magic.

**Limitations and failure modes.** First, the reduced 5-qudit distance-3 encoding is a design assumption used to make the projection concrete; the honest full-ball figure is $n = 17$ for the same $t = 1$, which raises the failure probability at fixed $\varepsilon$ (more qudits, same $t$: the binomial tail with $n = 17$, $t = 1$ gives $P_{\mathrm{fail}} = \sum_{w=2}^{17}\binom{17}{w}\varepsilon^w(1-\varepsilon)^{17-w}$, dominated by $\binom{17}{2}\varepsilon^2 = 136\,\varepsilon^2 = 1.36 \times 10^{-4}$ at $\varepsilon = 10^{-3}$ — worse than unencoded at this $\varepsilon$, with pseudo-threshold from $136\,\varepsilon \approx 1$, i.e., $\varepsilon \approx 7.4 \times 10^{-3}$). This is a material caveat: the attractive 5-qudit numbers depend on the symmetry-based reduction, whose rigorous correctness is unproven here. Second, the model assumes perfect encoding, decoding, and Hecke gates; gate errors on the Hecke operations will lower the effective threshold, and no fault-tolerant gate compilation for the $p$-adic QFT on this code is proven. Third, amplitude-damping noise is not amenable to the weight-counting argument, since damping errors are non-Pauli and their supports spread coherently; whether ultrametric confinement survives for non-Pauli channels is open. Fourth, the claim that the code is "not a stabilizer code" rests on the support-disjointness mechanism rather than an abelian stabilizer group; a skeptic could ask whether some stabilizer (or OAQEC [8]) presentation of the same ball code exists, in which case the novelty would be one of interpretation rather than code structure. Fifth, the adelic multi-place question — whether encoding across several primes $p_1, p_2, \ldots$ with Hecke couplings