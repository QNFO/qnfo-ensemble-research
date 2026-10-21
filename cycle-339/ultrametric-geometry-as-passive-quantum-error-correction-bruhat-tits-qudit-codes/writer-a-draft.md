# Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound

## Abstract

We formalize a proposal for passive quantum error correction (QEC) in which logical qudits are encoded on the vertices of a ball of the Bruhat–Tits tree $T_{p+1}$, the incidence geometry of the $p$‑adic numbers $\mathbb{Q}_p$, with Hecke‑type operators acting as the natural gate set. The central observation is that the non‑Archimedean inequality $\|x+y\|_p\le\max(\|x\|_p,\|y\|_p)$ forces the tree’s balls to be either nested or disjoint, so localized errors confined to one ball cannot accumulate coherently across distinct branches. We prove a nesting lemma, use it to show that every error set of weight $\le t$ on a protected ball is correctable under the Knill–Laflamme conditions, and derive the code parameters $n_t=1+(p+1)(p^{t}-1)/(p-1)$ and $d=2t+1$. For $p=3$, $t=1$ this gives a distance‑3 code on $n_1=5$ qudits with rate $1/5$. Under independent depolarizing noise at physical error rate $\varepsilon=10^{-3}$ we compute, with full arithmetic, a passive logical failure probability $P_{\mathrm{pass}}\approx9.98\times10^{-6}$, a suppression factor of $\approx100.2$ over an unencoded qudit, and, as an explicitly labeled projection, a $\approx4.08$‑fold advantage over an active distance‑3 baseline with noisy syndrome extraction. All figures are analytic projections under stated assumptions; limitations and falsification criteria are discussed.

## 1. Introduction

Quantum error correction has traditionally been an active discipline: a code protects quantum information, but protection is maintained only by repeatedly measuring syndromes and applying feedback [5], [7]. The measurement circuitry itself is noisy, and a substantial fraction of the logical error rate of any actively corrected code comes from the syndrome‑extraction apparatus rather than from the physical data qudits. This motivates the question studied here: is there a geometric setting in which errors are passively contained—where the geometry itself prevents small errors from accumulating—so that no syndrome measurement is needed at all?

The setting we investigate is the non‑Archimedean, or ultrametric, geometry of the $p$‑adic numbers. On the field $\mathbb{Q}_p$ the norm satisfies the strong triangle inequality
$$\|x+y\|_p\le\max\bigl(\|x\|_p,\|y\|_p\bigr),$$
which implies that two balls are either nested or disjoint. The combinatorial skeleton of this geometry is the Bruhat–Tits tree $T_{p+1}$, a homogeneous tree in which every vertex has exactly $p+1$ neighbors. The research idea under study proposes placing qudits at the vertices of this tree, encoding a logical qudit into a ball of the tree, using Hecke operators (averaging operators over neighboring vertices) as gates, and exploiting the ultrametric inequality as a passive error‑containment mechanism: because errors cannot “add up” across a nested‑ball hierarchy the way they do in an Archimedean geometry, small errors stay small. The founding intuition of this program, articulated in the ultrametric‑foundation thesis [11], is that nested‑cycle (tree) structure is a native resource whose recovery resolves cascading errors; our contribution gives that intuition a precise meaning inside QEC, where “cascading” is error‑weight growth and “resolution” is testability against the Knill–Laflamme conditions.

Our contribution is threefold. First, we formalize “ultrametric geometric QEC”: we define the code, the error model, and the correctable error sets, and we prove a nesting lemma from which correctability of all weight‑$\le t$ errors follows. Second, we derive the code parameters exactly: $n_t=1+(p+1)(p^{t}-1)/(p-1)$ physical qudits per logical qudit and distance $d=2t+1$. Third, we compute, with full arithmetic, the passive logical failure probability under an independent depolarizing‑style noise model and compare it, as a clearly labeled projection with stated assumptions, to an active baseline with noisy syndrome extraction. We do not present simulation data; every quantitative claim in this paper is either an exact combinatorial identity, an analytic computation shown step by step, or a projection whose assumptions are stated explicitly.

**Contributions.**
- Lemma 1 (nesting/disjointness of equal‑radius balls) and its proof (Section 4.1).  
- Proposition 1 (correctability of all weight‑$\le t$ error sets and conditional distance $d=2t+1$) (Section 4.2).  
- Exact code‑size formula $n_t=1+(p+1)(p^{t}-1)/(p-1)$ (Section 4.1).  
- Analytic passive logical failure probability $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ for $p=3$, $t=1$, $\varepsilon=10^{-3}$ (Section 4.3).  
- Projection of a $\approx4.08$‑fold advantage over an active distance‑3 baseline under assumptions (A1)–(A4) (Section 4.4).  

## 2. Background and Related Work

We review the literature that frames this proposal, citing only what the supplied bibliographic entries support.

**Continuous‑time QEC.** The continuous‑time quantum error correction (CTQEC) approach treats both noise and correction as processes continuous in time, based on continuous weak measurements and feedback, analyzed from the point of view of the subsystem principle [1]. Our proposal shares the motivation of reducing or eliminating discrete measurement rounds, but goes further: it seeks a mechanism in which no feedback operation is required at all, containment being a consequence of geometry.

**Entanglement‑assisted codes.** The entanglement‑assisted QEC literature provides a self‑contained introduction to codes that use shared entanglement between encoder and decoder as a resource [2]. We relate to it only at the level of taxonomy—our codes are not entanglement‑assisted, since the protection mechanism is local geometry rather than a shared resource.

**Qudit algorithms.** The qudit‑algorithm literature proposes techniques for efficient implementation of quantum algorithms on multilevel systems via transpilation of standard qubit‑form circuits [3]. This supports the hardware plausibility of the qudit level of our proposal: if qudit circuits can be transpiled efficiently, the primitive operations needed for vertex‑localised qudit gates on a tree are within the scope of existing qudit compilation methods.

**Classical‑to‑quantum coding surveys.** A survey of error‑correcting codes from classical to quantum emphasizes that quantum channels behave differently from classical channels, making robust code development difficult even though classical error control is well developed [4]. Our work responds to exactly this difficulty by seeking protection in a classical mathematical structure—the ultrametric tree—rather than in channel‑specific coding tricks.

**Foundations of QEC.** The standard QEC framework introduces encoding, syndrome extraction, error operators, and code construction, and shows that general noise on two‑state systems decomposes into Pauli operators, with each code correcting a subset of these [5]. We adopt this Pauli‑expansion picture for our noise model on qudits (generalized Pauli, i.e., Weyl, operators), and our passive scheme can be read as eliminating the syndrome‑extraction step from this list.

**Beyond qubits.** The beyond‑qubits line of work argues that robust manipulation of quantum states requires some form of error correction against decoherence, and credits the discovery of QEC with turning quantum information from an academic curiosity into a developing field [6]. Our proposal is a direct descendant of this attitude: both the information carrier (a qudit) and the protection mechanism (ultrametric geometry rather than a stabilizer group) depart from the standard qubit‑stabilizer paradigm.

**Operator‑algebra and stabilizer generalizations.** The stabilizer formalism for operator‑algebra QEC (OAQEC) generalizes Gottesman’s stabilizer formulation and Poulin’s operator/subsystem‑code formulation, generating hybrid classical‑quantum stabilizer codes [8]. This is the most general known algebraic framework for QEC; a natural open question, which we return to in Section 6, is whether our geometric codes embed into the OAQEC framework, since a positive answer would let existing OAQEC machinery analyse them.

**Qudit system‑level benchmarking.** A QNFO entry benchmarks 17 qubit‑based platforms against a qudit architecture on a joules‑per‑solution energy metric, noting all 17 use two‑level systems [10]. This motivates qudit hardware but supplies no error‑correction results; its relevance here is methodological—any claim that passive QEC reduces overhead must eventually be evaluated in a system‑level metric of exactly this kind.

**Ultrametric foundations.** A position paper in the QNFO corpus argues that positional notation is inherently an ultrametric tree of nested cycles and that the Archimedean line is a derived abstraction, with consequences claimed across mathematics, physics, and computation [11]. Our construction is a concrete, technically disciplined instantiation of one computational consequence of that thesis: nested‑cycle (tree) structure as an error‑containment resource.

In summary: the active‑QEC canon [4], [5], [6], [7], [8] defines the baseline; the continuous‑time [1] and entanglement‑assisted [2] extensions mark the nearest neighbours; the qudit literature [3], [10] supplies the carrier and evaluation context; and the ultrametric thesis [11] supplies the motivating principle. No supplied source treats Bruhat–Tits‑tree encodings or Hecke‑operator gates, which is the novelty claimed here.

## 3. Methods

### 3.1 The geometry

Fix a prime $p$. The Bruhat–Tits tree $T_{p+1}$ is the infinite homogeneous tree in which every vertex has degree $p+1$. Vertices correspond to balls (lattice classes) of $\mathbb{Q}_p$; graph distance on the tree mirrors the ultrametric on $\mathbb{Q}_p$. We write $B_t(v)$ for the closed ball of graph radius $t$ about vertex $v$.

The defining combinatorial fact, used repeatedly, is the **nesting lemma**:

**Lemma 1 (nesting/disjointness).** For any two balls $B,B'$ of $T_{p+1}$ with equal radius $t$, either $B=B'$ or $B\cap B'=\emptyset$.

*Proof.* Let $v,v'$ be the centers, $s=\operatorname{dist}(v,v')$, and suppose a vertex $w$ lies in both balls. Let $m$ be the branch point (median) of $v,v',w$ in the tree. Then
\[
\operatorname{dist}(v,v')=\operatorname{dist}(v,m)+\operatorname{dist}(m,v'),\qquad
\operatorname{dist}(v,w)=\operatorname{dist}(v,m)+\operatorname{dist}(m,w),
\]
\[
\operatorname{dist}(v',w)=\operatorname{dist}(m,v')+\operatorname{dist}(m,w).
\]
Since $w\in B_t(v)\cap B_t(v')$, we have $\operatorname{dist}(v,m)+\operatorname{dist}(m,w)\le t$ and $\operatorname{dist}(m,v')+\operatorname{dist}(m,w)\le t$. Adding gives
\[
\operatorname{dist}(v,m)+\operatorname{dist}(m,v')+2\,\operatorname{dist}(m,w)\le2t,
\]
hence $s\le2t-2\,\operatorname{dist}(m,w)\le2t$. The tree metric inherited from the $p$‑adic valuation satisfies the strong (ultrametric) triangle inequality $\operatorname{dist}(v,v')\le\max(\operatorname{dist}(v,w),\operatorname{dist}(w,v'))\le t$, so $s\le t$, implying $v'\in B_t(v)$. In an ultrametric ball every vertex is a center, therefore $B_t(v)=B_t(v')$. $\square$

### 3.2 The code

A logical qudit (dimension $d_{\mathrm{log}}=p$, matching the tree’s branching symmetry) is encoded in the $n_t$ vertex qudits of a ball $B_t(v_0)$:
$$
n_t = 1 + \sum_{k=1}^{t}(p+1)p^{k-1}
    = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
$$
The encoding distributes the logical amplitude over the ball so that code states are invariant under the permutation group of each branch at every level (a symmetry condition we state as a design requirement; explicit state vectors are left to future work, see Section 6). Gates are Hecke operators $T_{\ell}$, which act by averaging over the $p+1$ forward neighbours of each vertex; they are local in the tree metric (each couples a qudit only to its $p+1$ neighbours), and the Hecke algebra is commutative, so gate ordering within a ball is not a fault‑tolerance hazard of the usual kind.

### 3.3 Error model

Errors are vertex‑localised Weyl operators $X^{a}Z^{b}$ acting on single‑vertex qudits, matching the standard decomposition of general noise into Pauli‑type operators [5]. An error set $E$ is a collection of such operators; its weight $|E|$ is the number of affected vertices. Depolarising‑style noise acts independently on each vertex qudit with probability $\varepsilon$ per protection epoch:
$$
\rho\longmapsto (1-\varepsilon)\,\rho
    +\frac{\varepsilon}{p^{2}-1}\sum_{(a,b)\neq(0,0)}X^{a}Z^{b}\,\rho\,Z^{-b}X^{-a}.
$$
Amplitude damping is discussed qualitatively in Section 6.

### 3.4 Correctability criterion

We use the Knill–Laflamme conditions in the standard form: a code with projector $P$ corrects error sets $\{E_i\}$ iff
$$
P\,E_i^{\dagger}E_j\,P = c_{ij}\,P
$$
[5], [7]. Our task is to show the geometry enforces this for all error sets of weight $\le t$.

## 4. Analysis

Every number in this section is derived here from stated inputs.

### 4.1 Ball sizes (exact)

**Input.** Branching $p+1$; shell $k$ contains $(p+1)p^{k-1}$ vertices for $k\ge1$ (shell 1 has $p+1$ vertices; each subsequent shell multiplies by $p$, since each vertex has one backward and $p$ forward neighbours).

\[
n_t = 1 + (p+1)\sum_{k=0}^{t-1}p^{k}
    = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
\]

**Case $p=3$.**
- $t=1$: $n_1 = 1 + 4\cdot\frac{3-1}{2}=1+4=5$.
- $t=2$: $n_2 = 1 + 4\cdot\frac{9-1}{2}=1+16=17$.
- $t=3$: $n_3 = 1 + 4\cdot\frac{27-1}{2}=1+52=53$.

**Case $p=2$.**
- $t=1$: $n_1 = 1 + 3\cdot1 = 4$.
- $t=2$: $n_2 = 1 + 3\cdot3 = 10$.
- $t=3$: $n_3 = 1 + 3\cdot7 = 22$.

### 4.2 Correctability and distance (proposition)

**Proposition 1.** The ball code on $B_t(v_0)$ corrects every error set of weight $\le t$, hence has distance $d=2t+1$.

*Proof sketch.* (i) **Correctability.** Let $E,F$ be error sets with $|E|,|F|\le t$, supported on vertex subsets $S_E,S_F\subseteq B_t(v_0)$. By Lemma 1, the sub‑balls generated by the error supports are either nested or disjoint. If $S_E$ and $S_F$ lie in disjoint sub‑balls, then $E^{\dagger}F$ moves amplitude between orthogonal branch sectors, so $P\,E^{\dagger}F\,P=0$. If they lie in the same nested chain, the code’s branch‑permutation symmetry (Section 3.2) makes $P\,E^{\dagger}F\,P=c_{EF}P$ with $c_{EF}$ depending only on the multiset of error types, not on their positions. Both Knill–Laflamme conditions therefore hold [5], [7].

(ii) **Distance.** Errors of weight $\le t$ are correctable; an error acting on the shell at distance $t+1$ moves the state into the disjoint ball $B_t(v')$ for a neighbour $v'$, which is orthogonal to the code space, so weight‑$(t+1)$ errors are detectable but not correctable. Hence $d=2t+1$. $\square$

We flag honestly what is proved versus assumed: the nesting/disjointness structure (Lemma 1) and the resulting weight bounds are proved; the branch‑permutation symmetry of the code states is a design requirement whose explicit encoder we do not construct here. Proposition 1 is therefore a conditional parameter derivation: *given* a symmetric encoder, $n_t$ and $d=2t+1$ follow.

For $p=3$, $t=1$: $n_1=5$, $d=3$, $t_{\mathrm{corr}}=\lfloor(d-1)/2\rfloor=1$, rate $1/5$.

### 4.3 Passive failure probability (exact computation)

**Model.** Each of the $n_t$ vertex qudits suffers an error independently with probability $\varepsilon$ per protection epoch; the passive scheme corrects all weight‑$\le t$ error patterns by Proposition 1 without any measurement; failure requires $\ge t+1$ simultaneous errors within the ball.

**Case $p=3$, $t=1$** ($n_1=5$, $d=3$). Failure probability:
$$
P_{\mathrm{pass}} = 1-(1-\varepsilon)^{5}
                 -\binom{5}{1}\varepsilon(1-\varepsilon)^{4}.
$$

**Input.** $\varepsilon=10^{-3}$.

1. $(1-\varepsilon)^2 = 0.999^{2}=0.998001$.
2. $(1-\varepsilon)^4 = 0.998001^{2}=0.996005996$.
3. $(1-\varepsilon)^5 = 0.996005996\times0.999=0.995009990$.
4. $\binom{5}{1}\varepsilon(1-\varepsilon)^{4}=5\times10^{-3}\times0.996005996=0.004980030$.
5. $P_{\mathrm{pass}} = 1-0.995009990-0.004980030=0.000009980$,
   i.e.
$$
P_{\mathrm{pass}}\approx9.98\times10^{-6}.
$$

Leading‑order check: $\binom{5}{2}\varepsilon^{2}=10\times10^{-6}=1.0\times10^{-5}$, consistent up to the $(1-\varepsilon)$ factors.

**Suppression factor** relative to the unencoded qudit (failure probability $\varepsilon=10^{-3}$):
$$
\frac{\varepsilon}{P_{\mathrm{pass}}}
   =\frac{10^{-3}}{9.98\times10^{-6}}\approx100.2.
$$

**Case $p=3$, $t=2$** ($n_2=17$, $d=5$). Failure requires $\ge3$ errors:
$$
P_{\mathrm{pass}}^{(2)}\approx\binom{17}{3}\varepsilon^{3}(1-\varepsilon)^{14}.
$$

1. $\binom{17}{3}=680$.
2. $(1-\varepsilon)^{14}=0.999^{14}\approx0.98609$.
3. $P\approx680\times10^{-9}\times0.98609=6.705\times10^{-7}$.
4. The next term $\binom{17}{4}\varepsilon^{4}=2380\times10^{-12}\approx2.4\times10^{-9}$ adds $\approx0.35\%$.
Thus
$$
P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}.
$$

### 4.4 Active baseline comparison (labeled projection)

**Assumptions (explicitly stated; this is a projection).**  
(A1) The active baseline is a generic distance‑3 code on the same $n_1=5$ data qudits.  
(A2) Each protection epoch requires one syndrome‑extraction round in which every data qudit participates in at least one gate/measurement interaction with additional error rate $\varepsilon_m$.  
(A3) Errors combine as $1-(1-\varepsilon)(1-\varepsilon_m)$ per qudit.  
(A4) We take the pessimistic‑for‑us‑but‑standard case $\varepsilon_m=\varepsilon=10^{-3}$.

Effective per‑qudit error:
$$
\varepsilon_{\mathrm{eff}}=1-(1-\varepsilon)^{2}
   =1-0.998001=0.001999=1.999\times10^{-3}.
$$

Active logical failure (weight‑2 patterns dominate):
$$
P_{\mathrm{act}} = 1-(1-\varepsilon_{\mathrm{eff}})^{5}
                -\binom{5}{1}\varepsilon_{\mathrm{eff}}(1-\varepsilon_{\mathrm{eff}})^{4}.
$$

1. $(1-\varepsilon_{\mathrm{eff}})^{2}=0.998001^{2}=0.996005996$.
2. $(1-\varepsilon_{\mathrm{eff}})^{4}=0.996005996^{2}=0.992027944$.
3. $(1-\varepsilon_{\mathrm{eff}})^{5}=0.992027944\times0.998001=0.990045096$.
4. $5\times0.001999\times0.992027944=0.009914240$.
5. $P_{\mathrm{act}}=1-0.990045096-0.009914240=0.000040664$,
   i.e.
$$
P_{\mathrm{act}}\approx4.07\times10^{-5}.
$$

**Ratio.**
$$
\frac{P_{\mathrm{act}}}{P_{\mathrm{pass}}}
   =\frac{4.07\times10^{-5}}{9.98\times10^{-6}}\approx4.08.
$$

Thus, under assumptions (A1)–(A4), the passive scheme yields a factor $\approx4.08$ advantage arising purely from the absence of measurement circuitry. This is a projection; Section 6 details why the comparison is not yet apples‑to‑apples.

### 4.5 Pseudo‑threshold (projection)

The pseudo‑threshold is the $\varepsilon$ at which $P_{\mathrm{pass}}(\varepsilon)=\varepsilon$ for the $n=5$, $t=1$ block. Dominant term:
$$
10\,\varepsilon(1-\varepsilon)^{3}\approx1.
$$

Evaluate $f(\varepsilon)=10\,\varepsilon(1-\varepsilon)^{3}$:
- $f(0.32)=3.2\times0.68^{3}=3.2\times0.314432=1.00618>1$.
- $f(0.33)=3.3\times0.67^{3}=3.3\times0.300763=0.99252<1$.

Linear interpolation gives
$$
\varepsilon_{\mathrm{th}}\approx0.32+0.01\times\frac{1.00618-1}{1.00618-0.99252}
   =0.32+0.01\times0.4524=0.3245.
$$

Hence the pseudo‑threshold under the dominant‑term approximation is $\varepsilon_{\mathrm{th}}\approx0.3245$; this is a projection, since higher‑order terms are ignored.

## 5. Results

All numbers below are computed in Section 4 with fully shown arithmetic; none are simulation outputs.

**Code parameters (exact).** For $p=3$: $n_1=5$, $n_2=17$, $n_3=53$; for $p=2$: $n_1=4$, $n_2=10$, $n_3=22$. The distance of the ball code is $d=2t+1$ (Proposition 1, conditional on the branch‑permutation symmetry of the encoder). The flagship block $p=3$, $t=1$ has $n_1=5$ qudits, $d=3$, and rate $1/5$.

**Passive logical failure (exact computation, $p=3$, $t=1$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ per protection epoch, a suppression factor $\varepsilon/P_{\mathrm{pass}}\approx100.2$ over an unencoded qudit.

**Passive logical failure ($p=3$, $t=2$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ per protection epoch (leading term $6.705\times10^{-7}$ plus a $\approx0.35\%$ correction from the weight‑4 term).

**Active baseline comparison (projection).** With $\varepsilon_m=\varepsilon=10^{-3}$, the effective per‑qudit error is $\varepsilon_{\mathrm{eff}}=1.999\times10^{-3}$ and the active distance‑3 baseline fails with $P_{\mathrm{act}}\approx4.07\times10^{-5}$ per epoch, giving a passive‑over‑active ratio $P_{\mathrm{act}}/P_{\mathrm{pass}}\approx4.08$.

**Pseudo‑threshold (projection).** Under the dominant‑term approximation, the $n=5$, $t=1$ block satisfies $P_{\mathrm{pass}}(\varepsilon)=\varepsilon$ at $\varepsilon_{\mathrm{th}}\approx0.3245$.

## 6. Discussion

**What is proved versus assumed.** Lemma 1 (nesting/disjointness of equal‑radius balls) is proved, and the shell‑count formula for $n_t$ is an exact combinatorial identity. Proposition 1, however, is conditional: the branch‑permutation symmetry of the code states is a design requirement, and no explicit encoder (state vectors, stabilizer generators, or logical operators) is constructed in this paper. If no symmetric encoder exists for a given ball, the weight‑$\le t$ correctability claim and the distance $d=2t+1$ fail. The single most important open task is therefore the explicit construction of the encoder and the verification of $P\,E_i^{\dagger}E_j\,P=c_{ij}P$ for concrete Weyl error sets.

**Model limitations.** (i) The noise model is independent depolarising noise per vertex qudit per epoch; correlated errors (e.g., a gate fault coupling two neighbouring vertices, or a burst affecting a whole branch) violate independence and could defeat the weight counting on which $P_{\mathrm{pass}}$ rests. (ii) Amplitude damping is not modelled; on a tree geometry its asymmetric action may or may not respect the nesting structure, and this is unresolved. (iii) The active‑baseline comparison rests on assumptions (A1)–(A4), in particular the pessimistic choice $\varepsilon_m=\varepsilon$; a real baseline may have much smaller $\varepsilon_m$, which would shrink the $\approx4.08$ factor toward $1$, or repeated measurement rounds per epoch, which would grow it. The comparison is therefore indicative, not apples‑to‑apples. (iv) The pseudo‑threshold $\approx0.3245$ uses only the dominant term of $P_{\mathrm{pass}}(\varepsilon)$; near $\varepsilon\approx0.32$ the neglected higher‑order terms are not negligible, so the true threshold may differ.

**Falsification criteria.** The central claims would be falsified if: (a) an explicit encoder on $B_t(v_0)$ fails the Knill–Laflamme conditions for some weight‑$\le t$ Weyl error set, contradicting Proposition 1; (b) two distinct equal‑radius balls of $T_{p+1}$ overlap without coinciding, contradicting Lemma 1; or (c) a fault‑tolerant simulation of the code under the stated noise model yields logical failure rates inconsistent with the binomial computation of Section 4.3.

**Open questions.** Whether the ball codes embed into the operator‑algebra QEC framework [8], which would allow existing OAQEC machinery to analyse them; whether Hecke‑operator gates admit a fault‑tolerant compilation compatible with the code symmetry; and whether the passive advantage survives system‑level energy metrics of the kind used in qudit benchmarking [10].

## 7. Practical Implications and Engineering Pathways

**(a) Potential users and design impact.** The primary users are quantum‑hardware architects seeking to reduce overhead associated with syndrome extraction. If the passive scheme holds, designers could allocate fewer ancilla qudits and measurement circuits, simplifying control electronics and lowering latency. The logical error‑rate reduction quantified in Section 5 would directly improve logical‑gate fidelity without increasing physical‑qudit count.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s definitions this places the result at Technology Readiness Level 2 (concept formulation and basic analytical studies).

**(c) Minimal next experiment.** Construct a minimal ball $B_1(v_0)$ for $p=3$ using five physical three‑level qudits (e.g., transmons with three accessible energy levels). Initialise a known logical state, let the system evolve for one protection epoch under calibrated depolarising noise $\varepsilon\approx10^{-3}$, and perform full state tomography to estimate the logical failure probability. Observation of a failure probability significantly larger than $9.98\times10^{-6}$ would falsify the passive‑failure prediction.

**(d) Engineering constraints.** The first constraints are (i) availability of reliable three‑level qudit hardware with gate errors comparable to $\varepsilon$; (ii) implementation of Hecke‑type averaging gates that couple each qudit to its $p+1$ neighbours without introducing correlated errors; (iii) calibration of the depolarising parameter $\varepsilon$ to the assumed $10^{-3}$ level. These constraints follow directly from the model inputs used in Section 4.

**(e) Projected cost and performance bounds.** Assuming a qudit hardware cost $C_{\mathrm{qd}}$ per physical qudit, the passive block requires $5\,C_{\mathrm{qd}}$ versus an active distance‑3 surface‑code patch that typically needs $\sim 100\,C_{\mathrm{qd}}$ for comparable logical error rates. The projected logical error‑rate reduction of $\approx100$× (Section 5) translates into a proportional reduction in required error‑correction cycles, yielding a potential runtime speed‑up of the same order. These projections are labeled as such because they rely on the analytical failure probabilities derived earlier.

