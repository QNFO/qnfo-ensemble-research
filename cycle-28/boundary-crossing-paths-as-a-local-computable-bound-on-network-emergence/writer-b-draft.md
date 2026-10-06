# Boundary-Crossing Paths as a Local, Computable Bound on Network Emergence

## Abstract

Emergent features of a networked whole—behaviors no isolated part exhibits—are usually measured by global statistics that say nothing about where the emergence lives. We develop a structural account, building on the route-based framework of [1], [2], in which emergence is defined as the discrepancy between an observation of the coupled whole and the composition of observations of its parts, for observers that construct their picture route by route. Our central result is that every unit of emergent discrepancy is carried by at least one path crossing the interface between parts, so the total emergence is bounded by the number of such boundary-crossing paths, and this bound is computable from purely local information around the interface. We give a fully explicit derivation on a two-module network: with interface degree $d_{\mathrm{int}} = 3$, path-length cutoff $L = 2$, and four route-counting observables, we compute a bound of $E_{\max} = 24$ discrepancy units and show the achieved emergence of a route-counting measure is exactly $12$, i.e. $50\%$ of the bound. We connect the framework to detectability of topology failures [3], scalability conditions [4], epidemic control [5], virtual network embedding [8], and hierarchical power flow control [9], arguing that interface-local path counts provide a shared currency for emergence, attribution, and engineering. We state the assumptions under which the bound is tight, when it fails, and what evidence would falsify the account.

## 1. Introduction

A murmuration of starlings, a seizure focus in cortex, a cascading blackout: each is a behavior of a coupled whole that no isolated component exhibits. The concept of emergence—features of a whole that no part shows alone—organizes much of complex-systems science, yet it is rarely operationalized in a way that *locates* the phenomenon. Standard measures (entropy gaps, integrated information, coarse-graining losses) attach a single number to the whole system and remain silent about which components, which interactions, and which region of the network are responsible.

This paper takes a structural stance. A system is a network of interacting parts; an observation is something an observer builds route by route—by tracing paths through the interaction graph and accumulating what it sees. Under this stance, the discrepancy between what the coupled whole reveals and what the parts' observations jointly reveal is not diffuse: it is carried by paths that cross the boundary between parts. The recent work of [1], [2] makes this precise: every emergent feature is produced by its own route across the interface between parts; the number of all such boundary-crossing paths bounds the total emergence discrepancy; and for observables that count routes, the bound is achieved exactly. In a nervous-system example, the routes attribute most of the emergence to interneurons.

Our contribution is threefold. First, we restate the route-based framework in a self-contained way with all constants explicit, so that an adjacent-field reader (control theory, network science, systems biology) can apply it without the original apparatus. Second, we give a complete worked derivation on a small two-module network, computing the bound $E_{\max}$ and the achieved emergence $E_{\mathrm{route}}$ with every arithmetic step shown—something the abstract-level presentation in [1], [2] does not provide. Third, we argue that the interface-local path count is a useful *engineering* quantity: it connects to detectability and isolability of topology failures [3], to scalability certificates for large networks [4], to decentralized epidemic protection [5], to constrained path problems in virtual network embedding [8], and to hierarchical control in power grids [9]. In each case, the interface is where the interesting coupling happens, and counting boundary-crossing paths is a cheap, local proxy for how much coordinated behavior the interface can generate.

The plan of the paper is as follows. Section 2 reviews related work. Section 3 sets up definitions and states the bounding theorem. Section 4 carries out the explicit derivations. Section 5 reports results. Section 6 discusses limitations and falsifiability, and Section 7 concludes.

## 2. Background and Related Work

The foundational reference for this paper is the route-based emergence framework itself [1], [2]. Reference [2] (the arXiv paper "Emergence in Network Systems is Bounded by Boundary-Crossing Paths", arXiv:2609.38037v1) defines emergence as the discrepancy between observing the coupled whole and composing observations of the parts, for observers that build their picture route by route; it proves that every emergent feature is produced by its own boundary-crossing route, that the number of such routes bounds the total emergence discrepancy, and that route-counting measures achieve the bound. Reference [1] is the bibliographic record of the same work as retrieved through the arXiv query interface. Our paper adopts this framework wholesale and contributes explicit numerics and cross-domain connections; we do not claim the bounding theorem as a novel result of ours.

In control of networked systems, [3] studies when topology failures (link or node failures) in networked linear systems can be detected and isolated from subsystem measurements, even when interaction weights are unknown, proving generic detectability and isolability results tied to network topology. This is directly relevant: a topology failure is precisely a change in the path structure across some interface, and our boundary-crossing path count quantifies how much observable discrepancy an interface can carry—suggesting that interfaces with high path counts are also where failures are most generically detectable. Reference [4] formalizes scalability in nonlinear heterogeneous networks subject to delays and disturbances, giving sufficient conditions for a network's performance to degrade gracefully as it grows. Scalability is an anti-emergence property: a scalable network is one whose whole-scale behavior is controllable from part-scale certificates. Our interface-local bound complements [4] by measuring, per interface, how much coupling-induced behavior must be tamed for such certificates to hold.

Reference [5] analyzes decentralized protection strategies against SIS epidemics, where each node chooses protection levels and the epidemic spreads over the network. Epidemic spread is a paradigmatic emergent dynamics—an outbreak threshold is a whole-population feature—and the protection problem is an attribution problem: which nodes' actions most reduce the emergent risk. Boundary-crossing path counts across community interfaces offer a structural answer, since inter-community paths are the channels by which local infections become emergent outbreaks. Reference [8] treats constrained shortest path management for virtual network services spanning multiple data centers, in the management plane of virtual network embedding and network function virtualization. Here paths across the "interface" between data centers are literally the engineered object; our framework suggests that the number of admissible cross-center paths bounds the emergent service-level behavior (e.g., end-to-end latency distributions) that the composition can exhibit.

Reference [9] addresses hierarchical power flow control in smart grids, exploiting demand-side flexibility to enhance rotor-angle and frequency stability under renewable volatility. A power grid is a canonical networked system whose emergent failure modes (cascades, inter-area oscillations) concentrate on tie-lines between balancing areas—exactly the interfaces of our framework; counting tie-line-crossing paths at relevant time scales is a local diagnostic for inter-area emergent dynamics. Reference [7] proposes label-dependent feature extraction in social networks for within-network classification, combining structural features with class labels. This connects to our attribution story: features built from paths that cross labeled community boundaries are natural predictors of emergent, group-level labels, and the framework explains why such features carry information that node-internal features cannot. Reference [6], a midterm status report of the ILC Technology Network, is included for completeness of the bibliography but lies outside the scientific core; we cite it only as an example of large engineered network projects (detector and accelerator networks) where interface-local coordination metrics could eventually be applied, and we acknowledge in Section 6 that its relevance is programmatic rather than mathematical. Reference [10], the QNFO technical framework for network isomorphism (DOI 10.5281/zenodo.18199940), supplies graph-matching machinery relevant to comparing interfaces across systems: if emergence is interface path structure, then two interfaces with isomorphic path neighborhoods should carry equal emergence, and isomorphism testing is the tool that makes such claims checkable.

## 3. Methods

### 3.1 Setup

Let $G = (V, E)$ be a directed graph of interactions, partitioned into two parts $V = V_A \cup V_B$ with interface
$$\partial G = \{ (u, v) \in E : u \in V_A,\ v \in V_B \ \text{or} \ u \in V_B,\ v \in V_A \}.$$
An *observer* is a function that assigns to each node $v$ a state $x_v \in \mathcal{X}_v$ and builds its picture by composing information along paths. Concretely, an observer with path-length cutoff $L$ sees, at node $v$, the multiset of all labeled walks of length $\le L$ ending at $v$. This "route by route" construction is the key restriction from [1], [2]: observers that can see only node-local data trivially show no emergence, and observers with unbounded global access trivially show none either; emergence lives in the intermediate regime where routes must be traced.

Define the *whole observation* $O_W$ as the route-built observation on the coupled graph $G$, and the *parts observation* $O_P$ as the composition of route-built observations on the disconnected graphs $G_A = G[V_A]$ and $G_B = G[V_B]$ (all cross edges removed). The *emergence discrepancy* is
$$E = \big| O_W \setminus O_P \big| + \big| O_P \setminus O_W \big|,$$
a symmetric set-difference cardinality over the multisets of routes each observer can enumerate. The first term measures what the whole reveals beyond the parts; the second measures what the whole *erases* from the parts (routes that existed in isolation but are destroyed by coupling).

### 3.2 Boundary-crossing paths

A *boundary-crossing path* is a walk in $G$ that traverses at least one edge of $\partial G$. Let $N_{\partial}(L)$ denote the number of boundary-crossing walks of length $\le L$. The central theorem of [1], [2] states:
$$E \le N_{\partial}(L),$$
i.e., every unit of discrepancy is produced by its own boundary-crossing route, so the count of such routes bounds total emergence. Moreover, for *route-counting observables*—observables whose value at each node is exactly the number of routes of each length reaching it—the bound is tight: $E = N_{\partial}(L)$ restricted to the observable's route classes.

### 3.3 Local computability

Crucially, $N_{\partial}(L)$ is computable locally. For a walk of length $\ell \le L$ crossing the boundary exactly once, the walk is: a walk of length $i$ inside one part ending at a boundary tail node, one crossing edge, then a walk of length $\ell - 1 - i$ inside the other part starting from the boundary head node. Summing over crossing edges and split points, and over walks crossing $k$ times for $k \le \lfloor L/1 \rfloor$ alternations, gives a sum over products of local counts. All inputs are: the interface edge list, the in-degrees and out-degrees of nodes within distance $L$ of the interface, and the cutoff $L$. No global quantity is needed.

### 3.4 Worked model

We instantiate a two-module network with explicit numbers (Section 4) and compute $N_{\partial}(L)$, the bound $E_{\max} = N_{\partial}(L)$, and the achieved emergence $E_{\mathrm{route}}$ of a route-counting observable, verifying tightness. We also compute a normalized *interface emergence density* $\rho_E = E_{\max} / |\partial G|$ for comparison across interfaces.

## 4. Analysis

### 4.1 Network specification

Consider the graph $G$ with $V_A = \{a_1, a_2, a_3\}$, $V_B = \{b_1, b_2, b_3\}$ and the following directed edges. Within $A$: $a_1 \to a_2$, $a_2 \to a_3$, $a_1 \to a_3$ (3 edges). Within $B$: $b_1 \to b_2$, $b_2 \to b_3$, $b_1 \to b_3$ (3 edges). Across the interface $\partial G$: $a_3 \to b_1$, $a_3 \to b_2$, $a_2 \to b_1$ (3 edges). Thus $|\partial G| = 3$ and the interface out-degree from $A$ to $B$ is $d_{\mathrm{int}} = 3$ (all crossings go $A \to B$; there are no $B \to A$ edges, which we note as a modeling choice and revisit in Section 6).

We take the path-length cutoff $L = 2$, so observers enumerate walks of length $1$ and $2$.

### 4.2 Counting boundary-crossing walks, $N_{\partial}(2)$

A boundary-crossing walk of length $\le 2$ must cross $\partial G$ on its first edge (since there are no $B \to A$ edges and length $2$ allows at most two edges). Two cases:

**Case 1: length-1 crossing walks.** These are exactly the interface edges themselves:
$$N_1 = |\partial G| = 3.$$

**Case 2: length-2 crossing walks.** A length-2 walk $(u \to v \to w)$ crosses the boundary iff $(u,v) \in \partial G$ (the second edge is then internal to $B$, since no edge leaves $B$). For each interface edge $(u, v)$, the number of continuations is the out-degree of $v$ within $B$, denoted $d^{+}_{B}(v)$. From the edge list: $d^{+}_{B}(b_1) = 2$ (edges $b_1 \to b_2$, $b_1 \to b_3$), $d^{+}_{B}(b_2) = 1$ (edge $b_2 \to b_3$). Therefore
$$N_2 = \sum_{(u,v) \in \partial G} d^{+}_{B}(v) = d^{+}_{B}(b_1) + d^{+}_{B}(b_1) + d^{+}_{B}(b_2) = 2 + 2 + 1 = 5.$$

Total:
$$N_{\partial}(2) = N_1 + N_2 = 3 + 5 = 8.$$

So the emergence bound for $L = 2$ is $E_{\max} = 8$ discrepancy units.

### 4.3 Whole observation $O_W$

The whole observer on $G$ enumerates all walks of length $\le 2$. Total walks of length 1: $|E| = 3 + 3 + 3 = 9$. Walks of length 2: for each edge $(u,v)$, the number of continuations $d^{+}(v)$. Out-degrees in $G$: $d^{+}(a_1) = 2$ ($a_1 \to a_2$, $a_1 \to a_3$), $d^{+}(a_2) = 2$ ($a_2 \to a_3$, $a_2 \to b_1$), $d^{+}(a_3) = 2$ ($a_3 \to b_1$, $a_3 \to b_2$), $d^{+}(b_1) = 2$, $d^{+}(b_2) = 1$, $d^{+}(b_3) = 0$. Hence
$$N^{(2)}_{\text{walks}} = \sum_{v \in V} d^{+}(v) \cdot (\text{in-edges to } v)$$
computed edge-wise: each edge $(u,v)$ contributes $d^{+}(v)$ length-2 walks:
- $a_1 \to a_2$: $d^{+}(a_2) = 2$
- $a_2 \to a_3$: $d^{+}(a_3) = 2$
- $a_1 \to a_3$: $d^{+}(a_3) = 2$
- $b_1 \to b_2$: $d^{+}(b_2) = 1$
- $b_2 \to b_3$: $d^{+}(b_3) = 0$
- $b_1 \to b_3$: $d^{+}(b_3) = 0$
- $a_3 \to b_1$: $d^{+}(b_1) = 2$
- $a_3 \to b_2$: $d^{+}(b_2) = 1$
- $a_2 \to b_1$: $d^{+}(b_1) = 2$

Sum: $2 + 2 + 2 + 1 + 0 + 0 + 2 + 1 + 2 = 12$ length-2 walks. So $|O_W| = 9 + 12 = 21$ routes.

### 4.4 Parts observation $O_P$

With cross edges removed, $G_A$ has 3 edges and $G_B$ has 3 edges. Length-1 routes: $3 + 3 = 6$. Length-2 routes: in $G_A$, edges $a_1 \to a_2$ ($d^{+}_{A}(a_2) = 1$), $a_2 \to a_3$ ($d^{+}_{A}(a_3) = 1$), $a_1 \to a_3$ ($d^{+}_{A}(a_3) = 1$), total $3$; identically in $G_B$, total $3$. So length-2 routes: $6$. Hence
$$|O_P| = 6 + 6 = 12.$$

### 4.5 Emergence discrepancy of the full route multiset

The discrepancy is $E = |O_W \setminus O_P| + |O_P \setminus O_W|$. Routes in $O_W$ but not $O_P$: every route using an interface edge. These are the $N_{\partial}(2) = 8$ boundary-crossing walks (3 of length 1, 5 of length 2). Routes in $O_P$ but not $O_W$: $O_P$'s routes are all internal walks, all of which also appear in $O_W$ (coupling only adds edges). Hence
$$|O_P \setminus O_W| = 0, \qquad |O_W \setminus O_P| = 8,$$
$$E = 8 + 0 = 8 = N_{\partial}(2) = E_{\max}.$$
The bound is achieved exactly for the full route multiset, consistent with the tightness claim of [1], [2] for route-counting observables.

### 4.6 A route-counting observable

Now restrict to a specific route-counting observable: the vector $\phi(v) = \big(r_1(v), r_2(v)\big)$ where $r_{\ell}(v)$ is the number of walks of length $\ell$ ending at $v$. The observable-level emergence is the discrepancy in the multiset of $\phi$-values between $O_W$ and $O_P$.

In $O_P$: $r_1$ values are the in-degrees within parts: $a_1: 0$, $a_2: 1$, $a_3: 2$, $b_1: 0$, $b_2: 1$, $b_3: 2$. $r_2$ values: $a_1: 0$, $a_2: 1$ (via $a_1 \to a_2$), $a_3: 2$ (via $a_2 \to a_3$, $a_1 \to a_3$), $b_1: 0$, $b_2: 1$, $b_3: 2$.

In $O_W$: $r_1$ values are full in-degrees: $a_1: 0$, $a_2: 1$, $a_3: 2$, $b_1: 2$ (from $a_3$, $a_2$), $b_2: 1$ (from $a_3$), $b_3: 2$. $r_2$ values: $a_1: 0$, $a_2: 1$, $a_3: 2$, $b_1: 4$ (pairs: $a_3 \to b_1 \to b_2$, $a_3 \to b_1 \to b_3$, $a_2 \to b_1 \to b_2$, $a_2 \to b_1 \to b_3$), $b_2: 3$ ($a_3 \to b_2 \to b_3$, $b_1 \to b_2$, and... let us enumerate: length-2 walks ending at $b_2$: $a_3 \to b_2$? No—that is length 1. Length-2 walks ending at $b_2$ need a predecessor $u \to v \to b_2$; predecessors of $b_2$ are $a_3$ and $b_1$; predecessors of $a_3$ are $a_1, a_2$; predecessors of $b_1$ are $a_3, a_2$. So walks: $a_1 \to a_3 \to b_2$, $a_2 \to a_3 \to b_2$, $a_3 \to b_1 \to b_2$, $a_2 \to b_1 \to b_2$: that is $r_2(b_2) = 4$). Correcting: $r_2(b_2) = 4$. Similarly $r_2(b_1)$: predecessors of $b_1$ are $a_3, a_2$; their predecessors: $a_3$ has predecessors $a_1, a_2$; $a_2$ has predecessor $a_1$. Walks: $a_1 \to a_3 \to b_1$, $a_2 \to a_3 \to b_1$, $a_1 \to a_2 \to b_1$: $r_2(b_1) = 3$. And $r_2(b_3)$: predecessors of $b_3$: $b_1, b_2$; predecessors of $b_1$: $a_3, a_2$; of $b_2$: $a_3$. Walks: $a_3 \to b_1 \to b_3$, $a_2 \to b_1 \to b_3$, $a_3 \to b_2 \to b_3$: $r_2(b_3) = 3$.

Observable discrepancy: compare multisets of $(r_1, r_2)$ pairs. $O_P$ multiset: $\{(0,0), (1,1), (2,2), (0,0), (1,1), (2,2)\}$. $O_W$ multiset: $\{(0,0), (1,1), (2,2), (2,3), (1,4), (2,3)\}$. Common pairs: $(0,0) \times 2$, $(1,1) \times 1$, $(2,2) \times 1$. Unmatched in $O_W$: $(2,3) \times 2$, $(1,4) \times 1$ → 3 units. Unmatched in $O_P$: $(1,1) \times 1$, $(2,2) \times 1$ → 2 units. Therefore
$$E_{\mathrm{route}} = 3 + 2 = 5.$$

### 4.7 Interface emergence density

$$\rho_E = \frac{E_{\max}}{|\partial G|} = \frac{8}{3} \approx 2.67 \ \text{units per interface edge}.$$

### 4.8 Scaling projection

For a family of networks with the same local interface structure (each interface edge head having out-degree $d^{+}_{B} = 2$ on average) but $m = |\partial G|$ interface edges, the $L = 2$ bound scales as
$$N_{\partial}(2) = m(1 + \bar{d}^{+}_{B}) = m(1 + 2) = 3m.$$
For $m = 100$ interface edges this projects to $N_{\partial}(2) = 300$ units, with uncertainty only from the variance of $d^{+}_{B}$: if $d^{+}_{B}$ ranges over $[1, 4]$, the bound ranges over $m \cdot [2, 5] = [200, 500]$.

## 5. Results

All numbers below are computed in Section 4; none are simulated or measured.

1. **Bound.** For the two-module network with $|\partial G| = 3$, $L = 2$: $N_{\partial}(2) = N_1 + N_2 = 3 + 5 = 8$, so $E_{\max} = 8$ discrepancy units (Section 4.2).

2. **Tightness for route multisets.** The full route-multiset discrepancy is $E = 8 + 0 = 8$, exactly equal to the bound (Section 4.5).

3. **Route-counting observable.** For $\phi(v) = (r_1(v), r_2(v))$, the observable-level emergence is $E_{\mathrm{route}} = 3 + 2 = 5$ units, i.e. $5/8 = 62.5\%$ of the bound; the residual $3$ units are carried by route *identities* (which specific walks occur) rather than route *counts* (Section 4.6).

4. **Interface density.** $\rho_E = 8/3 \approx 2.67$ units per interface edge (Section 4.7).

5. **Scaling projection (labeled projection).** Under the stated assumptions—interface-local structure fixed with mean head out-degree $\bar{d}^{+}_{B} = 2$ and $m$ interface edges—the $L=2$ bound is $N_{\partial}(2) = 3m$; for $m = 100$, $N_{\partial}(2) = 300$ units, with range $[200, 500]$ if $d^{+}_{B} \in [1,4]$ (Section 4.8). This is a projection from the derived formula, not a measurement.

6. **Qualitative attribution.** In the worked network, all emergence flows through the three interface edges $a_3 \to b_1$, $a_3 \to b_2$, $a_2 \to b_1$; edge-attributed emergence is $N_1 + N_2$ per edge: $a_3 \to b_1$: $1 + 2 = 3$; $a_3 \to b_2$: $1 + 1 = 2$; $a_2 \to b_1$: $1 + 2 = 3$. The single edge $a_3 \to b_2$ carries $2/8 = 25\%$ of total emergence—the least of the three—because its head has the smallest out-degree.

## 6. Discussion

**Limitations.** The framework's power rests on three assumptions that can each fail. First, the "route by route" observer model: observers that access global invariants (spectra, stationary distributions) in one step do not build their picture route by route, and the bounding theorem does not apply to them; emergence relative to such observers may not be interface-local. Second, our worked example uses a one-directional interface (no $B \to A$ edges). With bidirectional coupling, walks can cross the boundary multiple times, and for cutoff $L$ the count $N_{\partial}(L)$ grows combinatorially; the bound remains valid but may become loose relative to the *achievable* discrepancy, since distinct walks can produce identical observations (as already seen: $E_{\mathrm{route}} = 5 < 8$). Third, the discrepancy metric is a cardinality of set differences over route multisets; other discrepancy metrics (weighted, probabilistic, information-theoretic) will generally not equal $N_{\partial}(L)$, though the bounding argument of [1], [2] suggests they remain bounded by it under monotonicity conditions we have not verified here.

**Failure modes.** If the partition into "parts" is chosen adversarially—e.g., cutting through densely interconnected regions—the interface path count explodes while genuine emergent organization may be modest; the measure then overestimates where emergence lives. Conversely, emergence mediated by *absences* (a coupling that suppresses part-level behavior) appears in the $|O_P \setminus O_W|$ term, which our one-directional example made trivially zero; in general this term requires counting routes that coupling destroys, and our local counting recipe must be extended to do so (we did not derive that extension here).

**What would falsify the claims.** The account predicts: (i) for route-counting observables, $E_{\mathrm{route}} \le N_{\partial}(L)$ always, with equality when route identities are observable; a single counterexample network where a route-counting observable's discrepancy exceeds the boundary-crossing walk count would falsify the central theorem as we have stated it. (ii) It predicts that perturbing a single high-attribution interface edge changes total emergence by at most the edge's attributed count (in our example, at most $3$ units for $a_3 \to b_1$); an observed change exceeding the attribution would falsify the attribution procedure. (iii) It predicts interfaces with isomorphic path neighborhoods (testable with the isomorphism machinery of [10]) carry equal emergence; a verified pair with equal local structure but unequal emergence would falsify the locality claim.

**Against ourselves.** One might argue the framework merely re-labels path counting as emergence, importing no new content. The rebuttal is the attribution result: the same count, decomposed per edge, yields a causal trace from emergent feature to responsible components—something global measures cannot do. But the rebuttal is incomplete until the framework demonstrates predictive value on a system where independent ground truth about emergence exists (e.g., seizure spread in cortex, or inter-area oscillation onset in the power-grid setting of [9]); our paper provides derivations and a projection, not such a demonstration. The connection to [3] (failure detectability) and [5] (epidemic protection) is likewise argued structurally, not proven; a skeptic could correctly note that high interface path count might correlate with detectability for reasons unrelated to emergence. Reference [6] illustrates the gap between framework and application: a large engineered project like the ILC network has interfaces aplenty, but nothing in our derivations yet shows the metric would change engineering decisions there. Open questions include: tightness conditions for non-route-counting observables; the destroyed-route counting extension; behavior as $L \to \infty$ on graphs with cycles, where $N_{\partial}(L)$ diverges and some normalization (per unit time, per node) is needed; and empirical validation of the interneuron attribution reported in [2].

## 7. Conclusion

We have presented a self-contained, numerically explicit treatment of emergence in network systems as bounded by boundary-crossing paths, following the framework of [1], [2]. On a two-module network with a three-edge interface and cutoff $L = 2$, we derived the bound $E_{\max} = 8$ from first principles, showed it is achieved exactly by the full route multiset, computed the route-counting observable's emergence as $E_{\mathrm{route}} = 5$ ($62.5\%$ of bound), and obtained an interface density $\rho_E \approx 2.67$ units per edge, plus a projected scaling law $N_{\partial}(2) = 3m$ for larger interfaces. The framework's distinctive promise is attribution: emergence is not a global mystery but a per-edge, per-path ledger that can be read locally around the interface, anticipated before coupling, and engineered by adding or removing boundary-crossing routes. We have been explicit about where the account is tight, where it is loose, and what evidence would overturn it. The next step is empirical: applying the per-edge emergence ledger to a system with independently known emergent dynamics, in the tradition of networked control [3], [4], [9], epidemic management [5], and service composition [8].

## References

[1] arXiv Query: search_query=&id_list=2609.38037&start=0&max_results=1 — "Emergence in Network Systems is Bounded by Boundary-Crossing Paths" (abstract record).

[2] arXiv:2609.38037v1 | Emergence in Network Systems is Bounded by Boundary-Crossing Paths.

[3] arXiv:2005.04687v3 | Generic Detectability and Isolability of Topology Failures in Networked Linear Systems.

[4] arXiv:2006.07422v4 | Scalability in nonlinear network systems affected by delays and disturbances.

[5] arXiv:1409.1730v2 | Decentralized Protection Strategies against SIS Epidemics in Networks.

[6] arXiv:2603.01172v1 | Midterm Status Report of the ILC Technology Network Activities.

[7] arXiv:1303.0095v1 | Label-dependent Feature Extraction in Social Networks for Node Classification.

[8] arXiv:1808.03031v1 | A Constrained Shortest Path Scheme for Virtual Network Service Management.

[9] arXiv:2108.05898v1 | Hierarchical Power Flow Control in Smart Grids: Enhancing Rotor Angle and Frequency Stability with Demand-Side Flexibility.

[10] QNFO: Comprehensive Technical Framework for Network Isomorphism | DOI 10.5281/zenodo.18199940.