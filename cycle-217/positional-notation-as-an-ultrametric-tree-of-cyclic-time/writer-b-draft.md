# Positional Notation as an Ultrametric Tree of Cyclic Time: A Formal Construction for Calendar-Structured Data

## Abstract

Calendar-structured time series — server logs, scheduling records, epidemiological contact data — are stored as timestamps on a linear axis, which discards the nested periodic structure (second in minute, minute in hour, hour in day, day in week) that every user of a clock implicitly navigates. This paper formalizes the claim that positional notation is natively an ultrametric tree whose levels encode nested cyclic time. We prove that any mixed-radix cyclic numeral system, such as the sexagesimal clock with radices (60, 60, 24, 7), induces a symbolic ultrametric on timestamps in which the distance between two instants is determined by the depth of their least common ancestor in the calendar tree, and we verify the strong triangle inequality directly. We derive explicit quantities for the week-structured clock: a state space of 604,800 instants requiring 19.2061 bits, only 5 distinct ultrametric distances against 604,799 linear ones, and level-sharing probabilities from 1.6667 × 10⁻² down to 1.6534 × 10⁻⁶. We show that the resulting geometry separates calendar-aligned periodicities by construction, propose a clustering benchmark against linear metrics, and connect the construction to prior ultrametric models of epidemic contact time. The result gives a formal geometry for calendar-structured data and a testable alternative to flattening time into a line.

## 1. Introduction

Every operator of a time-series database, every scheduler of transit or clinical appointments, and every modeler of human contact networks faces the same representational problem: their data are produced by clocks and calendars whose structure is nested and periodic, yet their tools store and compare timestamps as points on a single uniform axis. A query such as "all events at 03:14 on any Tuesday" is trivial for a human reading a calendar and awkward for a linear timestamp, because the linear encoding must be re-parsed through modular arithmetic on 60, 24, and 7 to recover the hierarchy that the written form 03:14:07 already displays. The cost is concrete: index structures, partitioning schemes, and seasonality detectors must each re-implement calendar logic that the numeral itself carries, and analyses that assume linear distance treat two instants one second apart across a midnight boundary identically to two instants one second apart within the same minute, even though they sit in different days of the calendar tree.

The decision that would change if this paper's result holds is the choice of distance function and storage layout for timestamped data. If calendar timestamps carry a natural ultrametric — a distance in which "closeness" means sharing a fine-grained calendar cell, not a small difference in seconds — then clustering, indexing, and anomaly detection on periodic data can operate directly on the calendar hierarchy, and the choice between a linear and a hierarchical metric becomes an explicit, testable engineering decision rather than an unexamined default.

The starting observation is due to the QNFO synthesis of nonlinear tree-based numeration: in any integer base $b \geq 2$, the distance between two integers measured by the highest power of $b$ dividing their difference is exactly the $b$-adic valuation $d(x,y) = b^{-v_b(x-y)}$, and two numbers share $k$ trailing digits in base $b$ precisely when $b^k \mid (x-y)$ but $b^{k+1} \nmid (x-y)$ [9]. The same source states the thesis that the digit string is a path from root to leaf and that the distance between two numbers is the depth of their lowest common ancestor [9]. A companion thesis argues that the radix is a silent parameter — the numeral "10" denotes the base itself in every base, so a numeral string cannot internally specify its own rule of interpretation — and that the equally spaced line is a geometric import rather than an intrinsic property of the integers [10]. This paper takes these claims seriously for time: a mixed-radix clock numeral such as 03:14:07 on a Tuesday is a path in a tree whose levels are observed periodicities, and the natural distance on such numerals is ultrametric.

Prior work supplies the ingredients but not the combination. Ultrametric structures have been formalized abstractly, with embedding, extension, and interpolation theorems for ultrametric spaces [1]; random ultrametric trees model populations sampled at the same instant, with the comb metric $\bar{d}_f(s,t) = 2\max_{(s \wedge t, s \vee t)} f$ giving an explicit ultrametric on a boundary [7]; and an ultrametric SIR model derives a distance on individuals from hierarchical clustering by average infectious contact time, with infection probability proportional to $1/d(x,y)$ [8]. None of these treats the calendar itself as the tree. This paper supplies that construction and its quantitative consequences.

The contributions are:

1. A proof that every mixed-radix cyclic numeral system induces a symbolic ultrametric in which distance is a monotone function of the number of least-significant coordinates shared, with the strong triangle inequality verified explicitly (Section 4.1).
2. A fully worked quantitative profile of the week-structured clock with radices $(60, 60, 24, 7)$: state-space size, bit cost, distance-value count, level-sharing probabilities, and per-level entropies, all with shown arithmetic (Section 4.2–4.4).
3. An analysis of why this "time tree" metric separates calendar-aligned periodicities by construction, and a specification of the clustering experiment that would confirm or refute its practical advantage over linear metrics (Sections 4.5 and 7).

## 2. Background and Related Work

The formal backbone is the theory of ultrametrics. An ultrametric is a metric satisfying the strong triangle inequality $d(x,y) \leq d(x,z) \lor d(z,y)$, where $\lor$ is the maximum operator [1]. That paper develops the zero-dimensional analogue of ordinary metric space theory and proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem, using free modules over commutative rings and a zero-dimensional Michael continuous selection theorem in place of the classical paracompact-case tool [1]. For this paper, the relevance is that the calendar metric constructed in Section 4 is an ordinary object of this theory: whatever can be done for abstract ultrametric spaces — embedding into universal spaces, extension of partial definitions — is available to the time-tree metric without new machinery.

Random ultrametric trees provide the probabilistic and combinatorial vocabulary. An ultrametric tree is a tree whose leaves all lie at the same distance from the root; such trees model genealogies of populations sampled at the same point in time, and the set of leaves, called the boundary, is what is ultrametric with respect to the graph distance [7]. That work also gives the comb metric: for a comb-like function $f$ on a compact interval, $\bar{d}_f(s,t) = 2\max_{(s \wedge t, s \vee t)} f$ is an ultrametric on $\{f = 0\}$ [7]. The calendar tree of Section 3 is a finite, deterministic cousin of these objects: its leaves are instants of a finite horizon, and its levels are calendar periods rather than coalescence times.

The closest methodological precedent for putting time into an ultrametric is the ultrametric SIR model of epidemic spread. There, an infectious contact between two individuals is a time interval during which transmission is possible, hierarchical clustering of the population relative to average infectious contact time induces an ultrametric, and the distance between individuals equals the ratio of the population observation time to the minimum boundary value of the average infectious contact times within their smallest common cluster; the model then assumes the per-unit-time infection probability is proportional to $1/d(x,y)$ [8]. The authors note that infectious contact is a modeling construct that is difficult to compute exactly but always possible to approximate, and that it need not be physical contact [8]. That model builds the tree from contact statistics; the present paper builds it from the calendar, which is known a priori, and the two constructions could be composed: calendar levels give the prior hierarchy into which empirically estimated contact clusters are placed.

Ultrametric Cantor sets show that ultrametric distance and linear intuition can coexist on the same underlying set with different valuations. A family of Cantor sets is endowed with a scale-invariant ultrametric built from "relative infinitesimals" that satisfy an inversion rule, so that increments among infinitesimals are accomplished by inversions rather than translations; the associated valuation is both scale and reparametrization invariant, is given by an appropriate Cantor function, and offers a mechanism by which a measure-zero set grows into a fat Cantor set through distortion of scales [6]. This is directly analogous to the present thesis: the same instants carry both a linear distance (seconds elapsed) and an ultrametric one (calendar depth), and which distance governs behavior depends on the valuation chosen — the calendar valuation being the one that respects the nested periodic structure.

The claim that positional notation itself is a tree is stated and partially formalized in the QNFO synthesis. Its core theorem identifies the ultrametric of integer-base notation as the $b$-adic valuation $d(x,y) = b^{-v_b(x-y)}$, with the sketch that sharing $k$ trailing digits is equivalent to $b^k \mid (x-y)$ but $b^{k+1} \nmid (x-y)$, and the strong triangle inequality following from the fact that shared-digit counts compose by taking a minimum [9]. The same synthesis surveys extensions in which a digit's value depends on its vertex-to-root distance rather than string position, making "012" and "12" distinct values, and in which hyper-large numbers compress into hereditary trees of small depth [9]. The present paper extends the fixed-base theorem to mixed radices and reinterprets the levels as cyclic time.

The companion unified thesis supplies the conceptual framing this paper tests in a specific domain. It observes that in any base $b \geq 2$ the string "10" denotes $b$, so every base names itself "base-10" and no numeral string can internally specify its own interpretation — the radix is a silent parameter supplied from outside [10]. It further argues that the equal-interval assumption is a second hidden parameter, a geometric import from analytic geometry rather than an intrinsic property of the integers [10]. The calendar construction of Section 3 makes both observations operational for time: the radices $(60, 60, 24, 7)$ are supplied by the clock convention, not by the numerals, and the "line" of elapsed seconds is one valuation among at least two.

Two further sources support the general claim that notations carry structure beyond their strings. In tree-adjoining grammar, each sentence derivation yields two parse trees: a derived tree representing phrase structure and a derivation tree recording how elementary trees were combined, with the derivation tree offering a first insight into sentence semantics and its language being a regular tree language, much simpler to manipulate than the derived tree language [3]. The analogy is exact for numerals: the string is the derived object, the tree path is the derivation, and hierarchical queries are naturally asked of the derivation. In music notation for just intonation, a notation system for arbitrary rational frequencies requires that transposition up be supported by multiplication defined on any two notations and transposition down by inversion, showing that a notation's fitness is judged by the operations its structure supports [4]. The time-tree metric of Section 4 is likewise judged by the operations it supports — hierarchical grouping, periodicity detection — rather than by string economy.

Finally, two sources mark the boundaries of the analogy. In general relativity, a spacetime foliation by three-dimensional spacelike surfaces determines a fibration of the four-manifold over a one-dimensional leaf space, with the leaves as fibers of a surjective submersion [2]; the quotient to a one-dimensional leaf space is the rigorous version of "flattening" a layered structure onto a line, and the calendar tree can be seen as refusing that quotient for civil time. In arithmetic geometry, cyclic $p$-power extensions are represented by length-$n$ Witt vectors and organized into Hurwitz trees, with the differential Hurwitz tree obstruction for the cyclic refined local lifting problem proven to vanish by a recursive extension argument that extends a lower tree one branch at a time [5]. That work demonstrates that tree-organized cyclic structures support rigorous recursive induction; the calendar tree here uses the same shape for descriptive rather than arithmetic purposes. On the cognitive side, the embodied-mathematics review reports that Lakoff and Núñez ground mathematics in conceptual metaphor, that newborns at 3–4 days can discriminate collections of 2 versus 3 items, and that the number–numeral distinction is a bridge between cognitive and structural accounts [12] — a reminder that the linear number line itself is a metaphorical import, which is the psychological counterpart of the representational argument made here.

## 3. Methods

### 3.1 Objects: mixed-radix cyclic numeral systems

A mixed-radix cyclic numeral system is a tuple $R = (r_1, r_2, \ldots, r_D)$ of integers $r_j \geq 2$, called the radices, ordered from the finest period to the coarsest. An instant is a coordinate vector $x = (x_1, x_2, \ldots, x_D)$ with $0 \leq x_j < r_j$. The radix $r_j$ is the cardinality of the $j$-th observed periodicity: for the civil clock, $r_1 = 60$ (seconds per minute), $r_2 = 60$ (minutes per hour), $r_3 = 24$ (hours per day), $r_4 = 7$ (days per week). The state space is the product $X_R = \prod_{j=1}^{D} \{0, \ldots, r_j - 1\}$, with

$$N_R = \prod_{j=1}^{D} r_j.$$

We assume a finite horizon of exactly one full cycle of the coarsest period; longer horizons are handled by adding levels, and the analysis of Section 4 is per-cycle.

### 3.2 The calendar tree

$X_R$ is the leaf set of a rooted tree $T_R$ of depth $D$: the root is the whole cycle; the level-$j$ nodes partition the cycle into $\prod_{k=j}^{D} r_k$ cells, each a block of $\prod_{k=1}^{j-1} r_k$ consecutive finest-grain positions; the leaves are the $N_R$ instants. Two instants $x, y$ are siblings at level $j$ if they agree in coordinates $1, \ldots, j$ (the finest $j$ coordinates) — equivalently, if they lie in the same level-$j$ cell. The least common ancestor of $x$ and $y$ sits at level $k + 1$ where $k$ is the largest integer such that $x_i = y_i$ for all $i \leq k$; if $x_1 \neq y_1$ the LCA is the root.

### 3.3 The time-tree metric

Define, for a fixed parameter $\lambda > 1$ (we take $\lambda = 2$ throughout for concreteness; any $\lambda > 1$ gives an equivalent ultrametric up to monotone rescaling):

$$d_R(x, y) = \lambda^{-k(x,y)}, \qquad k(x,y) = \max\{k : x_i = y_i \text{ for all } i \leq k\},$$

with $k(x,y) = 0$ when $x_1 \neq y_1$, so that $d_R(x,y) = 1$ for instants in different top-level cells and $d_R(x,y) = \lambda^{-D}$ only for $x = y$. This is exactly the LCA-depth distance: distance decreases as the least common ancestor descends toward the leaves. It is the mixed-radix generalization of the fixed-base valuation $d(x,y) = b^{-v_b(x-y)}$ of [9], since in a fixed base $b$, $v_b(x - y)$ counts shared trailing digits.

### 3.4 Comparison metrics

The linear metric on the same state space is $d_{\text{lin}}(x,y) = |n(x) - n(y)|$, where $n(x) = \sum_{j=1}^{D} x_j \prod_{i=1}^{j-1} r_i$ is the elapsed-position encoding. We compare the two by: (i) the number of distinct distance values each attains on $X_R \times X_R$; (ii) the probability distribution of distances under the uniform distribution on pairs; (iii) whether calendar-aligned periodicities (fixed hour-of-day, fixed day-of-week) are level sets of the metric.

### 3.5 Method of quantification

All quantities in Section 4 are computed by explicit arithmetic from the radices $(60, 60, 24, 7)$ and the definitions above. No simulation is reported; the clustering experiment that would test the practical claim is specified, not run (Section 7). This mirrors the methodology of the QNFO fault-tolerance study, which reports computed results from stated inputs separately from clearly labeled projections [11].

## 4. Analysis

### 4.1 Theorem: the time-tree metric is an ultrametric

**Theorem 1.** For any mixed-radix cyclic numeral system $R = (r_1, \ldots, r_D)$ and any $\lambda > 1$, the function $d_R$ of Section 3.3 is an ultrametric on $X_R$: it satisfies the strong triangle inequality

$$d_R(x, z) \leq \max\{d_R(x, y),\, d_R(y, z)\} \quad \text{for all } x, y, z \in X_R.$$

**Proof.** Write $k(x,y)$ for the number of leading (finest) coordinates shared by $x$ and $y$, so $d_R(x,y) = \lambda^{-k(x,y)}$. First, $d_R$ is symmetric and $d_R(x,y) = 0$ iff $x = y$ (since $k(x,x) = D$ gives $\lambda^{-D} \neq 0$, we work with the convention that identical points have distance $0$ by definition and $\lambda^{-k}$ otherwise; this is the standard symbolic-ultrametric convention and does not affect the inequality). Let $k_1 = k(x,y)$ and $k_2 = k(y,z)$. For every coordinate $i \leq \min(k_1, k_2)$ we have $x_i = y_i$ and $y_i = z_i$, hence $x_i = z_i$. Therefore $k(x,z) \geq \min(k_1, k_2)$, and since $\lambda > 1$ the map $k \mapsto \lambda^{-k}$ is decreasing:

$$d_R(x,z) = \lambda^{-k(x,z)} \leq \lambda^{-\min(k_1, k_2)} = \max\{\lambda^{-k_1}, \lambda^{-k_2}\} = \max\{d_R(x,y), d_R(y,z)\}.$$

This is the same argument as the fixed-base case in [9], where $x$ and $z$ share at least $\min(k_1, k_2)$ trailing digits; mixed radices change only the meaning of "digit position," not the composition of shared prefixes. $\blacksquare$

The distance takes at most $D + 1$ values, $\{\lambda^{-D}, \lambda^{-(D-1)}, \ldots, \lambda^{-1}, 1\}$ (with $0$ for identical points), one per tree level — this is the sense in which the metric "encodes" the hierarchy.

### 4.2 State-space size and bit cost of the week clock

For the civil week clock, $R = (60, 60, 24, 7)$. The state-space size is

$$N_R = 60 \times 60 \times 24 \times 7.$$

Computing step by step: $60 \times 60 = 3600$; $3600 \times 24 = 86400$; $86400 \times 7 = 604800$. So $N_R = 604800$ instants.

The number of bits needed to index the state space is

$$\log_2 N_R = \log_2(2^7 \cdot 3^3 \cdot 5^2 \cdot 7),$$

since $60 = 2^2 \cdot 3 \cdot 5$, so $60^2 = 2^4 \cdot 3^2 \cdot 5^2$, and $60^2 \cdot 24 = 2^4 \cdot 3^2 \cdot 5^2 \cdot 2^3 \cdot 3 = 2^7 \cdot 3^3 \cdot 5^2$, and multiplying by $7$ gives $2^7 \cdot 3^3 \cdot 5^2 \cdot 7$. Using $\log_2 3 = 1.584963$, $\log_2 5 = 2.321928$, $\log_2 7 = 2.807355$:

$$\log_2 N_R = 7 + 3(1.584963) + 2(2.321928) + 2.807355 = 7 + 4.754889 + 4.643856 + 2.807355 = 19.206100.$$

So indexing one week of seconds requires $19.2061$ bits, consistent with the per-level entropy sum computed in Section 4.4.

### 4.3 Distance-value counts and sharing probabilities

The linear metric $d_{\text{lin}}$ attains $N_R - 1 = 604800 - 1 = 604799$ distinct nonzero values ($1, 2, \ldots, 604799$ elapsed positions). The ultrametric $d_R$ with $\lambda = 2$ attains exactly $D + 1 = 5$ values: $\{2^{-4}, 2^{-3}, 2^{-2}, 2^{-1}, 1\} = \{0.0625, 0.125, 0.25, 0.5, 1\}$, plus $0$ for identical points. The ratio of resolution granularity is

$$\frac{604799}{5} \approx 120959.8,$$

i.e., the linear metric distinguishes about $1.21 \times 10^5$ times more distance values, all of which are calendar-invariant-free; the ultrametric collapses them into exactly the five calendar levels.

Under the uniform distribution on ordered pairs of distinct instants, the probability that two instants share the finest coordinate (same second-of-minute label, i.e., same $x_1$) is

$$P(k \geq 1) = \frac{1}{r_1} = \frac{1}{60} \approx 0.0166667.$$

Sharing the two finest coordinates:

$$P(k \geq 2) = \frac{1}{r_1 r_2} = \frac{1}{3600} \approx 0.000277778.$$

Sharing three:

$$P(k \geq 3) = \frac{1}{r_1 r_2 r_3} = \frac{1}{86400} \approx 0.0000115741.$$

Sharing all four (identical instant):

$$P(k = 4) = \frac{1}{604800} \approx 0.00000165344.$$

The probability mass at each ultrametric distance follows by subtraction. For distinct pairs: $P(d_R = 1) = 1 - \frac{1}{60} = \frac{59}{60} \approx 0.983333$; $P(d_R = 0.5) = \frac{1}{60} - \frac{1}{3600} = \frac{59}{3600} \approx 0.0163889$; $P(d_R = 0.25) = \frac{1}{3600} - \frac{1}{86400} = \frac{23}{86400} \approx 0.000266204$; $P(d_R = 0.0625) = \frac{1}{86400} - \frac{1}{604800} = \frac{6}{604800} \approx 0.00000992063$. Check of normalization:

$$0.983333 + 0.0163889 + 0.000266204 + 0.00000992063 = 0.999998 \approx 1,$$

with the residual $1.65344 \times 10^{-6}$ being the identical-pair mass $P(d_R = 0)$, confirming the total is $1$.

### 4.4 Per-level entropies

The information carried by each calendar level is the entropy of a uniform coordinate:

$$H_1 = \log_2 60 = \log_2(4 \cdot 15) = 2 + \log_2 15 = 2 + 3.906891 = 5.906891,$$

using $\log_2 15 = \log_2 3 + \log_2 5 = 1.584963 + 2.321928 = 3.906891$. Similarly,

$$H_2 = \log_2 60 = 5.906891, \qquad H_3 = \log_2 24 = \log_2(8 \cdot 3) = 3 + 1.584963 = 4.584963,$$

$$H_4 = \log_2 7 = 2.807355.$$

The total is

$$H_1 + H_2 + H_3 + H_4 = 5.906891 + 5.906891 + 4.584963 + 2.807355 = 19.206100 \text{ bits},$$

matching the direct computation $\log_2 604800 = 19.2061$ of Section 4.2, as it must since the coordinates jointly determine the instant. The distribution is markedly non-uniform across levels: the two sexagesimal levels carry $5.9069$ bits each while the weekly level carries only $2.8074$ bits, so a linear encoding spends its bits where the calendar hierarchy is shallowest in information but the periodic structure lives in the coarse levels.

### 4.5 Worked distance examples and periodicity separation

Take two instants written in the form (day-of-week, hour, minute, second), finest coordinate last for readability: $x = $ (Tuesday, 03, 14, 07) and $y = $ (Tuesday, 03, 15, 07). In coordinate order $(x_1, x_2, x_3, x_4) = (\text{second}, \text{minute}, \text{hour}, \text{day})$: $x = (07, 14, 03, 2)$, $y = (07, 15, 03, 2)$. They agree in coordinates $1$ and $3$? No — agreement must be a prefix. They agree in coordinate $1$ ($x_1 = y_1 = 07$) but differ in coordinate $2$ ($14 \neq 15$). Hence $k(x,y) = 1$ and

$$d_R(x, y) = 2^{-1} = 0.5.$$

Now compare $x = (07, 14, 03, 2)$ with $z = (08, 14, 03, 2)$ (one second later, same minute): they agree in coordinates $1, 2, 3$, differ in none until coordinate $4$? They agree in $x_1 = z_1 = 07$, $x_2 = z_2 = 14$, $x_3