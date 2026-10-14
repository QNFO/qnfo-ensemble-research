# Emergent Universality from Symmetric Rules: Rule-110 Emulation by Alternating Trivial Cellular Automaton Rules

## Abstract

Elementary cellular automaton (ECA) rule 110 is Turing complete, yet its local rule is chiral: it treats its left and right neighbors differently, and this handedness underlies the glider dynamics that carry its computation. A recent construction shows that rule 110 can nevertheless be emulated by three constituent ECA rules — rules 36, 37, and 5 — each of which is individually mirror-symmetric and individually produces only trivial frozen or oscillatory patterns; the chirality resides entirely in their fixed spatial arrangement. The open question this paper addresses is quantitative: under what noise and scale conditions does such an arrangement actually behave as a coherent universal system, and how robust is that behavior? We formalize the construction, show that parity breaking arises from the ordering map $c(i) = i \bmod 3$ rather than from any constituent rule, and analyze domain walls between desynchronized regions with a two-parameter mean-field rate equation. With explicit arithmetic we derive the steady-state wall fraction $\rho^{*} = \sqrt{a\varepsilon/b}$, reproducing the $\varepsilon^{1/2}$ scaling reported for the construction; illustrative values are $\rho^{*} = 0.1$ at $\varepsilon = 10^{-2}$ and $\rho^{*} = 0.01$ at $\varepsilon = 10^{-4}$. We derive the relaxation time $\tau = 1/\sqrt{ab\varepsilon}$, a lock-on compatibility threshold $\rho_0 \geq 5 \times 10^{-4}$ walls per site for a $10^{3}$-step window, consistent with the reported observation that random initial conditions lock on to rule 110 over 90% of the time, and a noise-tolerance bound $\varepsilon_{\max} = b/(aN_c^{2})$, equal to $10^{-4}$ for one tolerated defect per 100 sites. Because the emulation runs at a time factor $\lambda = 3$, the physical noise budget tightens by a factor of three, to $\varepsilon_{\max} \approx 3.3 \times 10^{-5}$. The analysis changes the design question for self-organizing computation from "how sophisticated must each unit be?" to "what ordering of trivial units suffices, and what noise budget does the ordering buy?".

## 1. Introduction

Engineers who want computation to emerge from large ensembles of simple, unreliable units — amorphous computing, synthetic biology gene networks, self-configuring materials — face a persistent design barrier. The classical route to universal computation in a spatially extended system is to install one sophisticated, asymmetric rule at every site: rule 110 in elementary cellular automata, or Conway's Game of Life, both of which are rigorously proven to be computationally universal [11]. That route forces every unit to carry the full complexity of the rule table, and it offers no guidance on how much of that complexity can be offloaded onto the organization of the ensemble rather than the unit. Where the units are biological or physical components that cannot be individually programmed with high precision, the barrier is practical: the design either demands per-unit sophistication the substrate cannot deliver, or it abandons universality altogether. A demonstration that a repeating sequence of individually trivial, individually symmetric rules can emulate a Turing-complete chiral rule changes the design space: it shows that asymmetry can be supplied by arrangement, so the per-unit specification can be reduced to nearly nothing provided the schedule is fixed and correct.

The concrete construction is due to [1, 2]. Three elementary rules — rule 36, rule 37, and rule 5 — are assigned to sites by position modulo 3, and three steps of the mixture equal one step of rule 110 under a block encoding. Each constituent is mirror-symmetric and, alone, evolves to trivial frozen or oscillatory patterns; the composite emulates the Turing-complete rule 110. Two statistical regularities are reported with it: random initial conditions lock on to rule 110 behavior over 90% of the time, explained through the motion of domain walls between desynchronized regions, and under random noise of strength $\varepsilon$ the fraction of the lattice occupied by noise-seeded domain walls scales as $\varepsilon^{1/2}$, explained through a simple rate equation [1, 2].

What is missing from the reported result, and what this paper supplies, is the quantitative skeleton underneath those claims. The reported scaling is an observation; the rate equation that explains it is stated but not evaluated; the lock-on fraction is an empirical number without a stated density threshold; and the noise budget that a would-be user of such a system could tolerate is nowhere computed. This paper derives each of these quantities with every arithmetic step shown, from a two-parameter mean-field model whose assumptions are stated explicitly, and it separates carefully between (i) results derived here from stated assumptions, (ii) illustrative numerical evaluations under labeled parameter choices, and (iii) empirical results reported in [1, 2] and cited as such. No new simulations are presented.

The conceptual stakes extend beyond cellular automata. Turing's machine model, in which a finite control manipulates a tape through a single access pointer, remains the operational definition of computability and the basis for the major complexity classes such as P and NP [3]; Turing's work separated software from hardware by isolating "local information" and "state of mind" as the two relevant ingredients of calculation [7]. The construction of [1, 2] instantiates a Turingian theme in a sharpened form: the "program" of the universal machine is redistributed from the local rule table into the spatial ordering of the rules, in the same spirit as the program-size versus time-complexity trade-offs studied for small universal Turing machines [8]. Whether such redistribution genuinely saves descriptive complexity is contested — the source work itself concludes that diversity does not save information in this construction [1] — and we examine that objection directly in Section 6.

The contributions are:

1. A formal statement that the composite update map of the three-rule mixture breaks parity through the ordering map $c(i) = i \bmod 3$ while every constituent satisfies $f(x,y,z) = f(z,y,x)$, with the constituent rules identified as rules 36, 37, and 5 and the emulation carrying time factor $\lambda = 3$ (Section 3).
2. A mean-field derivation, with explicit arithmetic, of the steady-state noise-seeded wall fraction $\rho^{*} = \sqrt{a\varepsilon/b}$, reproducing the $\varepsilon^{1/2}$ scaling reported in [1, 2], with illustrative values $0.1$, $0.01$, and $0.5$ at $\varepsilon = 10^{-2}$, $10^{-4}$, and $0.25$ (Section 4.1).
3. The exact transient solution of the rate equation, giving relaxation time $\tau = 1/\sqrt{ab\varepsilon}$, and the noiseless coarsening law $\rho(t) = \rho_0/(1 + b\rho_0 t)$ (Section 4.2).
4. A lock-on compatibility threshold $\rho_0 \geq 5 \times 10^{-4}$ walls per site for a $10^{3}$-step window under ballistic wall motion, shown to be consistent with the >90% lock-on rate reported in [1, 2] (Section 4.3).
5. A noise-tolerance bound $\varepsilon_{\max} = b/(aN_c^{2}) = 10^{-4}$ for one tolerated defect per $N_c = 100$ sites, corrected for the emulation time factor $\lambda = 3$ to a physical per-step budget $\varepsilon_{\max} \approx 3.3 \times 10^{-5}$ (Section 4.4).

## 2. Background and Related Work

**The source construction.** The primary object of study is the demonstration in [1, 2] that the Turing-complete ECA rule 110 can be emulated by alternating three simple symmetric rules in space. The constituent rules are given explicitly there: rule 36 ("become active only if both neighbours are the opposite color of the cell"), rule 37 ("the same as rule 36, but also activate if all sites are inactive"), and rule 5 ("become active only if both outer neighbours are inactive"); all three are mirror-symmetric and individually evolve to trivial frozen or oscillatory patterns [1, 2]. Rule 36 is assigned to sites with $i \bmod 3 = 0$, rule 37 to $i \bmod 1 = 1$, and rule 5 to $i \bmod 3 = 2$; logical 0 is encoded as the block [100] and logical 1 as [000], and three steps of the mixture equal one step of rule 110 [1, 2]. The same work reports that the mixture usually self-organizes into rule 110 from random initial conditions, with failures explained by domain walls between desynchronized regions, that lock-on occurs over 90% of the time, and that under noise the wall density scales as $\sqrt{\varepsilon}$ via a rate equation [1, 2]. Its discussion adds two points this paper builds on: the chirality of the composite is "explicitly seen in the speeds of domain walls", and the hope that diversity saves information — several simple rules replacing one complex rule — is explicitly not realized in this construction [1]. Our analysis takes the reported regularities as empirical inputs and supplies the missing quantitative derivations.

**Turing machines and complexity.** The computational backdrop is the Turing machine, defined in [3] as a finite control manipulating a linear tape through one access pointer, with discrete time and a distinguished start cell and start state; that work describes how major complexity classes, notably P and NP, are characterized by appropriately restricted Turing machines, and formalizes partial computable functions from $n$-tuples of integers to integers [3]. The relevance here is precise: because rule 110 is Turing complete [1, 2], the three-rule mixture inherits the full class of partial computable functions, including their undecidability structure, so no prediction procedure for the emulated dynamics can exist in general.

**Turing's legacy and incomputability.** The anniversary assessment in [7] reviews how Turing's 1936 work reshaped views of computation across disciplines: it emphasizes that Turing separated software from hardware by isolating local information and state of mind as the relevant ingredients of calculation, that in the same paper Turing proved there are things that cannot be computed, and that Chaitin later formalized what is knowable and unknowable on that basis, implying that logical randomness is common even in mathematics [7]. The construction studied here is a concrete instance of the software–hardware separation: the "software" of rule 110 is carried partly by the spatial schedule rather than the local hardware of each cell. The theme of incomputability as a barrier to prediction is developed further in [9], which focuses on incomputability as a powerful theme in Turing's work, rooted in the 1936 discovery (with Church) of unsolvable problems and framed against the erosion of Laplacian predictability [9]. For the present system, the practical reading is that once lock-on is achieved, long-term prediction of the emulated dynamics is bounded by the incomputability of rule 110's behavior, not by the simplicity of the constituent rules.

**Small machines and complexity trade-offs.** The study of small Turing machines in [8] introduces computability and universality concepts and explores trade-offs between algorithmic (program-size) and computational (time) complexity as a means of explaining these measures in a novel manner [8]. The three-rule construction is a cellular-automaton analogue of exactly this trade: the description of the universal machine is redistributed from an 8-bit chiral rule table into three simpler rule tables plus a period-3 spatial schedule plus a block encoding, paying a time factor $\lambda = 3$. Whether the redistribution reduces total description length is examined adversarially in Section 6, in light of the source work's own conclusion that diversity does not save information here [1].

**Variants of Turing computation.** Infinite time Turing machines extend ordinary Turing machines into transfinite ordinal time, providing a natural model of infinitary computability and a setting for analyzing supertask algorithms; notably, the halting problem for classical Turing machines, undecidable classically, is decidable in $\omega$ many steps by an infinite time machine that simulates the computation and reads off the limit state [5]. The present construction sharpens the contrast: even the finite-time dynamics of a system whose local rules are all parity-symmetric is already universal, so infinitary extensions concern computational strength over time, not local rule complexity. Along a different axis, [6] compares Turing's machine model for computing with real numbers against Kleene's schemes S1–S9 for objects of finite type, proposes an extension of the scope of Turing computability motivated by a fragment of the Axiom of Choice, and establishes results — including functionals that no type-2 functional can compute while $\exists^{3}$ can — based on a notion of $N$-reduction [6]. That program concerns which higher-order objects are computable; the three-rule construction is orthogonal to it, showing that the substrate of ordinary first-order universality can be made locally homogeneous without changing the computable functions.

**Turing, learning, and intelligence.** The analysis of the Turing Test in [4] distinguishes a macro-level, post-hoc test of human intelligence, involving repeated interaction and adaptation to a conversation partner, from the micro-level, a priori definition of a Turing machine, and argues that an "out-of-the-box" Turing machine will not pass the Turing Test because intelligence involves repeated interactive learning [4]. The distinction matters here: the three-rule mixture is universal in Turing's micro-level sense, yet universality does not entail adaptive behavior. The lock-on phenomenon analyzed in Section 4.3 is a robustness property — the system recovers a coherent dynamical identity from perturbation — which is a precondition for, but by [4]'s argument not a route to, adaptive behavior.

**Universality as physical substrate.** Two further works illustrate how universal cellular automata are used as substrates for broader claims. The Self-Computing Universe framework in [11] constructs a formal mapping from the dynamics of a Turing-complete universal cellular automaton — citing Conway's Game of Life and Wolfram's rule 110 as rigorously proven computationally universal — to an axiomatic structure in which an event is a state change of an individual cell and causal precedence holds when one event is in the future light-cone of another [11]. The winding-number framework in [13] likewise posits a universal computation of pattern writing, evolution, and projection as the generator of spacetime and particles [13]. Neither work is a source for the present construction; both are cited to show that the choice of universal substrate, and the question of how robustly a substrate self-organizes into its universal behavior, is load-bearing in frameworks that ground physics in computation. The noise-tolerance bound derived in Section 4.4 is exactly the kind of quantity such frameworks inherit when they adopt a cellular-automaton substrate. Finally, the incompleteness results reviewed in [12] — that any consistent, effectively axiomatized formal system strong enough to express elementary arithmetic is incomplete, with the proof technique relying on Gödel numbering and diagonalization [12] — mark the outer boundary of what any universal substrate, including this one, can decide about itself.

## 3. Methods

### 3.1 Elementary cellular automata and parity symmetry

An elementary cellular automaton (ECA) consists of a bi-infinite binary lattice $a_i(t) \in \{0,1\}$, $i \in \mathbb{Z}$, updated synchronously by a radius-1 rule:

$$a_i(t+1) = f\big(a_{i-1}(t),\, a_i(t),\, a_{i+1}(t)\big),$$

with $f: \{0,1\}^3 \to \{0,1\}$ encoded as an 8-bit rule number $R = \sum_{k=0}^{7} f_k\, 2^{k}$. Rule 110 has $R_{110} = 110 = 2^{6} + 2^{5} + 2^{3} + 2^{1}$, i.e., binary $01101110$. Explicitly, $f_{110}(1,1,0) = 1$ while $f_{110}(0,1,1) = 0$: the rule distinguishes the left neighbor from the right neighbor. This chirality is essential to the glider dynamics that carry information in rule 110's universal computation [1, 2].

A rule $f$ is *parity-symmetric* (mirror-symmetric) if

$$f(x, y, z) = f(z, y, x) \quad \text{for all } (x,y,z) \in \{0,1\}^3,$$

equivalently, its rule number is invariant under the mirror involution on the 8-bit table. The three constituent rules of [1, 2] each satisfy this condition, so no local update carries a preferred direction. Their verbal definitions, as given in [1, 2], are:

- Rule 36: become active only if both neighbours are the opposite color of the cell.
- Rule 37: the same as rule 36, but also activate if all sites are inactive.
- Rule 5: become active only if both outer neighbours are inactive.

Each is individually trivial in the sense of [1, 2]: alone, each eventually results in frozen or oscillatory patterns.

### 3.2 The alternating construction

Following [1, 2], the three symmetric rules are applied in a fixed repeating *spatial* sequence: site $i$ is assigned rule 36 if $i \bmod 3 = 0$, rule 37 if $i \bmod 3 = 1$, and rule 5 if $i \bmod 3 = 2$. Writing $f_1 = f_{36}$, $f_2 = f_{37}$, $f_3 = f_{5}$, and $c(i) = i \bmod 3$, every site updates simultaneously with its assigned rule:

$$a_i(t+1) = f_{c(i)+1}\big(a_{i-1}(t),\, a_i(t),\, a_{i+1}(t)\big).$$

The composite update map $T$ is not parity-symmetric. For the reflection operator $\sigma$ defined by $(\sigma a)_i = a_{-i}$, each constituent satisfies $f_j(\sigma a) = \sigma f_j(a)$, but the class pattern is not reflection-invariant: defining $c^{-}(i) = c(-i)$, we have $c(i) \neq c^{-}(i)$ for $i \not\equiv 0 \pmod 3$. Concretely, at $i = 1$: $c(1) = 1$, so the forward update at site 1 uses $f_2$ (rule 37), while $c^{-}(1) = 2$, so the reflected update uses $f_3$ (rule 5). Hence

$$T(\sigma a)_i = f_{c(i)+1}\big((\sigma a)_{i-1}, (\sigma a)_i, (\sigma a)_{i+1}\big) \neq f_{c^{-}(i)+1}\big((\sigma a)_{i-1}, (\sigma a)_i, (\sigma a)_{i+1}\big) = (\sigma T a)_i$$

generically. The composite is chiral even though no constituent is: the chirality is carried by the ordering map $c(i)$, an organizational property. This is the precise content of the statement in [1, 2] that "the chirality of rule 110 is created by their arrangement", and it is why the source work observes the chirality "explicitly" in the speeds of domain walls [1]: walls separating regions that run the three-rule cycle in opposite spatial phase inherit the handedness of the schedule.

### 3.3 Emulation of rule 110

Following [1, 2], the composite dynamics $T$ emulates rule 110 in the block-encoding sense: logical 0 is encoded as the block [100] and logical 1 as the block [000], and three steps of the mixture equal one step of rule 110 [1, 2]. Formally, there is a coarse-graining map $\Phi$ from configurations of the three-rule system to configurations of rule 110 and a time-scale factor $\lambda = 3$ such that

$$\Phi\big(T^{\lambda n}(A)\big) = F_{110}^{\,n}\big(\Phi(A)\big)$$

for initial conditions $A$ in the emulating subset, where $F_{110}$ is the global map of rule 110. The period-3 spatial structure of $T$ reproduces the asymmetric neighborhood sampling that rule 110 performs with its chiral rule table. Since rule 110 is Turing complete [1, 2], the three-rule system is Turing complete as well. We note that rule 36 can be replaced by rule 54, as the two rules only differ in positions that are never visited [1, 2]; nothing in the analysis below depends on which of the two is used.

### 3.4 Domain walls, lock-on, and noise

The emulating dynamics does not enforce global phase coherence: different regions of the lattice may run the three-rule cycle in different relative phases (desynchronized regions). Boundaries between phase domains behave as *domain walls*: localized defects that move through the lattice and annihilate on collision, as described in [1, 2]. Lock-on to rule 110 behavior is the absorption of all phase boundaries, after which the lattice evolves as a coherent rule-110-equivalent system.

We model walls as point particles on a line with density $\rho(t)$ (walls per site), moving with characteristic speed $v$ (sites per step) and annihilating on contact. Noise of strength $\varepsilon$ (probability per site per step of a spontaneous bit flip, applied after the deterministic update) creates new walls at rate $a\,\varepsilon$ per site per step, where $a$ is a susceptibility constant depending on how often a flip actually destabilizes the local phase. The mean-field rate equation, of the same form used in [1, 2] to explain the $\sqrt{\varepsilon}$ scaling, is

$$\frac{d\rho}{dt} = a\,\varepsilon - b\,\rho^{2},$$

where the annihilation term $b\,\rho^{2}$ encodes pairwise wall collisions (each collision removes two walls, giving the quadratic loss term standard in coarsening theory) and $b > 0$ is the collision-rate constant.

## 4. Analysis

### 4.1 Steady-state wall fraction and the $\varepsilon^{1/2}$ law

Set $d\rho/dt = 0$ in the rate equation:

$$0 = a\,\varepsilon - b\,\rho^{2} \quad\Longrightarrow\quad \rho^{2} = \frac{a\,\varepsilon}{b} \quad\Longrightarrow\quad \rho^{*} = \sqrt{\frac{a\,\varepsilon}{b}} = \sqrt{\frac{a}{b}}\;\varepsilon^{1/2}.$$

This reproduces the square-root scaling of the noise-seeded wall density reported in [1, 2]. The exponent $1/2$ follows solely from the structure *creation linear in noise, annihilation quadratic in density*; it is independent of the constants $a$ and $b$. The prefactor $\sqrt{a/b}$ is a model normalization, not a measured quantity.

**Numerical illustration (labeled illustrative parameters).** Take $a = 1$ (every noise event seeds a wall, the maximal-susceptibility upper bound) and $b = 1$ (unit collision rate), in units where $\rho$ is per site and $t$ per step. Inputs: $a = 1$, $b = 1$ (normalization choices, Section 3.4); $\varepsilon$ values are parameters of the thought experiment.

- For $\varepsilon = 10^{-2}$: $\rho^{*} = \sqrt{1 \cdot 10^{-2} / 1} = \sqrt{10^{-2}} = 10^{-1} = 0.1$. That is, 10% of sites host a wall.
- For $\varepsilon = 10^{-4}$: $\rho^{*} = \sqrt{10^{-4}} = 10^{-2} = 0.01$, i.e., 1%.
- For $\varepsilon = 0.25$: $\rho^{*} = \sqrt{0.25} = 0.5$, i.e., 50%.

Check of the scaling: reducing $\varepsilon$ by a factor of $10^{2}$ (from $10^{-2}$ to $10^{-4}$) reduces $\rho^{*}$ by a factor of $10^{1}$ (from $0.1$ to $0.01$), consistent with $\rho^{*} \propto \varepsilon^{1/2}$ since $(10^{2})^{1/2} = 10$.

### 4.2 Transient solution and relaxation time

The rate equation is separable. With initial condition $\rho(0) = \rho_0$:

$$\int \frac{d\rho}{a\varepsilon - b\rho^{2}} = t \quad\Longrightarrow\quad \frac{1}{\sqrt{a b\,\varepsilon}}\,\operatorname{artanh}\!\left(\rho\,\sqrt{\frac{b}{a\varepsilon}}\right) = t + C,$$

so that

$$\rho(t) = \sqrt{\frac{a\varepsilon}{b}}\;\tanh\!\left(\sqrt{a b\,\varepsilon}\; t + \operatorname{artanh}\!\left(\rho_0\sqrt{\frac{b}{a\varepsilon}}\right)\right).$$

The approach to steady state occurs on the timescale

$$\tau = \frac{1}{\sqrt{a b\,\varepsilon}}.$$

With $a = b = 1$ and $\varepsilon = 10^{-2}$: $\tau = 1/\sqrt{10^{-2}} = 1/10^{-1} = 10$ steps. For $\varepsilon = 10^{-4}$: $\tau = 1/\sqrt{10^{-4}} = 1/10^{-2} = 100$ steps. Weaker noise therefore both lowers the steady wall fraction and lengthens the relaxation time. (A linearization around $\rho^{*}$ gives $\tau = 1/(2\sqrt{ab\varepsilon})$, a factor of 2 smaller; that value governs only the late-stage exponential tail, and we adopt the exact-solution value as the convention for the full approach.)

### 4.3 Noiseless coarsening and lock-on from random initial conditions

Without noise ($\varepsilon = 0$), the rate equation gives pure annihilation, $d\rho/dt = -b\rho^{2}$. Derivation: separating, $d\rho/\rho^{2} = -b\,dt$; integrating, $-1/\rho = -bt + C$; with $\rho(0) = \rho_0$, $C = -1/\rho_0$; hence $1/\rho = bt + 1/\rho_0$, giving

$$\rho(t) = \frac{\rho_0}{1 + b\,\rho_0\, t}.$$

Walls coarsen algebraically, not exponentially.

**Lock-on criterion (projection).** Take the reported lock-on fraction of over 90% of random initial conditions [1, 2] and ask what initial wall density $\rho_0$ is compatible with full coarsening within a window of $T = 1000$ steps on a lattice of length $L = 10^{3}$ sites, assuming walls move at speed $v = 1$ site per step and annihilate in pairs. Full lock-on requires every wall to meet a partner: the mean distance between walls is $\ell = 1/\rho_0$, and two approaching walls close the gap at relative speed $2v$, so the mean annihilation time is

$$t_{\text{ann}} = \frac{\ell}{2v} = \frac{1}{2 v \rho_0}.$$

Requiring $t_{\text{ann}} \leq T$ with $v = 1$, $T = 1000$:

$$\frac{1}{2\rho_0} \leq 1000 \quad\Longrightarrow\quad \rho_0 \geq \frac{1}{2000} = 5 \times 10^{-4}.$$

Lock-on within $10^{3}$ steps is therefore expected