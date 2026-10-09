# Emergent Universality from Symmetric Micro-Rules: Domain-Wall Dynamics in Alternating Cellular Automata

## Abstract

Elementary cellular automaton rule 110 is Turing complete, yet its local update is manifestly chiral: it distinguishes left from right. Recent work [1, 2] shows that rule 110 can be emulated by alternating three simple rules that are individually symmetric under spatial reflection, so that the chirality required for universality resides entirely in the temporal-spatial arrangement of the rules rather than in any single rule. We analyze this construction from the standpoint of non-equilibrium statistical mechanics. We formalize the emulation as a product map on a doubled time step, show that the parity-breaking operator is the cyclic composition of the three symmetric rules, and develop a domain-wall picture in which desynchronized regions of the lattice are separated by moving walls that annihilate on collision. Under this picture, random initial conditions lock on to rule 110 dynamics over more than 90% of configurations, as reported in [1, 2]. We derive, from a two-parameter rate equation for wall creation and annihilation, that the steady-state wall fraction scales as $\rho^{*} \propto \varepsilon^{1/2}$ in the noise strength $\varepsilon$, reproducing the scaling reported in the source work, and we compute explicit numerical values for representative parameters. The result supports a general thesis: computational complexity can emerge from repeated, individually trivial and symmetric units, with asymmetry supplied only by ordering.

## 1. Introduction

The question of how complexity arises from simple components is central to computability theory and to statistical physics alike. Turing's 1936 model established that a machine with a small, fixed set of local operations can perform any effective computation [3, 7, 9]. In cellular automata (CAs) — lattices of finite-state cells updated by a uniform local rule — this theme finds its sharpest expression in Cook's proof that elementary CA rule 110 is universal: a one-dimensional lattice of binary cells, updated by a single fixed rule, can simulate any Turing machine [8]. Rule 110 is, however, chiral: its update table treats the left and right neighbors asymmetrically, and this handedness is essential to its glider dynamics, which carry the information processed in the universal computation.

A recent result [1, 2] destabilizes the intuition that such asymmetry must be present in the microscopic dynamics. The authors show that rule 110 can be emulated by alternating, in a fixed repeating sequence, three elementary rules each of which is individually symmetric under spatial reflection ($a_{i} \leftrightarrow a_{-i}$). No constituent rule can tell left from right; the chirality of the composite dynamics is created purely by the arrangement — the order in which the symmetric rules are applied. The constituent rules are described as trivial. The claim is therefore not merely that a complicated composite can mimic a complicated rule, but that diversity of simple, symmetric parts plus ordering suffices to generate a universal computer.

Two further quantitative phenomena are reported in [1, 2]. First, random initial conditions lock on to rule 110 behavior over 90% of the time, an aggregation effect explained through the motion of domain walls between desynchronized regions of the lattice. Second, when random noise (spontaneous bit flips) is added, the errors seed new domain walls, and the fraction of the lattice occupied by walls scales with the square root of the noise strength, a behavior the authors explain with a simple rate equation.

This paper has three aims. First, we give a compact formalization of the alternating-rule construction, making precise in what sense parity is broken by composition rather than by any local rule (Section 3). Second, we derive the $\varepsilon^{1/2}$ wall-fraction scaling from an explicit rate equation, showing every arithmetic step and computing numerical values for representative parameters (Section 4). Third, we situate the result in the broader context of universality, small machines, and emergent computation (Sections 2 and 6), and we argue that the mechanism — repeated perturbed units generating order through wall dynamics — is a plausible route to complexity in biological and physical systems.

Our contribution is analytical and expository: we do not present new simulations. All quantitative claims are either (i) derived here with shown arithmetic from stated assumptions, (ii) explicitly labeled as projections under stated assumptions, or (iii) reported results of [1, 2], cited as such.

## 2. Background and Related Work

**Universality and small machines.** The theoretical backdrop is Turing's definition of effective computation [3], which established that a fixed finite instruction set suffices for universal computation; the paper [3] surveys the Turing machine's influence on computational complexity, framing the question of how much structure a universal system minimally requires. The trade-off between program-size complexity and time complexity in small Turing machines is studied in [8], which introduces computability and universality concepts and explores how descriptive and computational complexity trade against each other — directly relevant here, because the alternating-rule construction reduces the complexity of the *local* rules while pushing structure into the *schedule*, a trade-off of exactly the kind [8] investigates. Rule 110 universality [1, 2] is the extreme case: an elementary CA, the smallest standard universal dynamical system, emulated by rules simpler than itself.

**Extensions of the Turing framework.** Infinite-time Turing machines [5] extend computation into transfinite ordinal time, providing a model of infinitary computability; they illustrate that the boundaries of the Turing paradigm remain an active object of study, and they contrast with our setting, where the interest is not in extending computational power but in minimizing the asymmetry of the underlying rules while retaining universality. The paper [6] compares Turing's machine model for computing with reals to Kleene's schemes S1–S9 for finite-type computation, asking whether a framework can marry the best of both; this reflects the same theme of how the choice of computational substrate shapes what is computable, which in our case concerns whether parity symmetry of the substrate is an obstruction to universality (it is not).

**Turing and the origins of complexity.** The anniversary assessment [7] reviews how Turing's work changed views on the foundations of complexity across fields; our result is a concrete instance of the trend [7] documents: complexity emerging from minimal, well-understood primitives. The paper [9] examines incomputability as a central theme in Turing's thought, arising from the 1936 discovery (with Church) of unsolvable problems; in the CA context, universality of the emulated dynamics implies that global properties of the alternating-rule system — such as whether a given initial condition ever settles — are undecidable, connecting the statistical-mechanics questions studied here to genuine incomputability. Finally, [4] argues that an "out-of-the-box" Turing machine will not pass the Turing Test because intelligence involves adaptive, macro-level interaction; while far from our formal setting, it usefully cautions that computational universality is a micro-level property and does not by itself imply higher-level intelligent behavior — a caution we adopt when interpreting the biological significance of our results.

**The source result.** The primary object of study is [1, 2]: rule 110 emulated by three alternating symmetric rules, lock-on from random initial conditions over 90% of trials, and noise-induced domain walls with fraction scaling as $\varepsilon^{1/2}$. Our analysis takes these reported phenomena as inputs and supplies derivations and interpretation.

**Corpus context.** The QNFO corpus materials on philosophy of science [10], syntactic generation [11], computational syntax [12], and the winding number as hidden variable [13] provide broader context for treating arrangement and ordering — rather than local content — as the carrier of structure; the winding-number work [13] in particular exemplifies how global (topological) quantities can encode information absent from local rules, a pattern parallel to chirality emerging from rule ordering here.

## 3. Methods

### 3.1 Elementary cellular automata and symmetry

An elementary cellular automaton consists of a bi-infinite binary lattice $a_{i}(t) \in \{0,1\}$, $i \in \mathbb{Z}$, updated synchronously by a local rule of radius 1:

$$a_{i}(t+1) = f\!\left(a_{i-1}(t),\, a_{i}(t),\, a_{i+1}(t)\right),$$

with $f: \{0,1\}^{3} \to \{0,1\}$ encoded as an 8-bit rule number $R = \sum_{k=0}^{7} f(k_{2},k_{1},k_{0})\, 2^{k}$, where $(k_{2},k_{1},k_{0})$ is the binary neighborhood. Rule 110 has $R_{110} = 110 = 2^{6} + 2^{5} + 2^{3} + 2^{1}$, i.e. $01101110_{2}$.

A rule is *left-right symmetric* if $f(x, y, z) = f(z, y, x)$ for all neighborhoods; equivalently, its rule number is invariant under the mirror involution $M$ on the 8-bit table. The three constituent rules of [1, 2] each satisfy this symmetry, so none carries a preferred direction.

### 3.2 The alternating construction

Let $f_{1}, f_{2}, f_{3}$ denote the three symmetric rules. The emulating dynamics applies them in a fixed cyclic schedule. Define the global update operators $F_{j}$, $j \in \{1,2,3\}$, by $(F_{j} a)_{i} = f_{j}(a_{i-1}, a_{i}, a_{i+1})$. One macro-step of the emulating system is the composition

$$\Phi = F_{3} \circ F_{2} \circ F_{1},$$

applied once per three micro-steps. The key structural fact is:

**Proposition (chirality by arrangement).** Each $F_{j}$ commutes with the lattice reflection $\Pi: i \mapsto -i$, i.e. $F_{j}\,\Pi = \Pi\, F_{j}$. The composition $\Phi$ therefore also commutes with $\Pi$. Nevertheless, the *cyclic order* $(f_{1}, f_{2}, f_{3})$ is a distinguished oriented sequence: the reversed schedule $\Phi' = F_{1} \circ F_{2} \circ F_{3}$ is, in general, a different map, and it is $\Phi'$ (or a conjugate) that emulates the mirror image dynamics of rule 110 rather than rule 110 itself. Chirality thus lives in the schedule, not in any $F_{j}$.

The proof is immediate: reflection-conjugating a symmetric micro-step returns the same micro-step, so conjugating the whole product reverses only the order of factors. Because rule 110's gliders have a definite handedness, the emulating system must break parity at the level of the macro-step, and the only available breaking mechanism is the ordering of the factors — hence the claim of [1, 2] that "the chirality of rule 110 is created by their arrangement."

### 3.3 Domain walls and lock-on

The emulating dynamics does not enforce global phase coherence: different regions of the lattice may run the three-rule cycle in different relative phases (desynchronized regions). Boundaries between phase domains behave as *domain walls*: localized defects that move through the lattice and annihilate on collision. When two walls collide, the region between them is absorbed and a single phase domain results. Lock-on to rule 110 behavior is the absorption of all phase boundaries, after which the lattice evolves as a coherent rule-110-equivalent system.

We model walls as point particles on a line of length $L$ with density $\rho(t)$ (walls per site), moving with characteristic speed $v$ (sites per macro-step) and annihilating on contact. Noise of strength $\varepsilon$ (probability per site per macro-step of a spontaneous bit flip) creates new walls at rate $a\varepsilon$ per site per macro-step, where $a$ is a susceptibility constant depending on how often a flip actually destabilizes the local phase.

### 3.4 Rate equation

The mean-field rate equation for the wall density is

$$\frac{d\rho}{dt} = a\,\varepsilon - b\,\rho^{2},$$

where the annihilation term $b\rho^{2}$ encodes pairwise wall collisions (each collision removes two walls, giving the quadratic loss term standard in coarsening theory) and $b > 0$ is the collision-rate constant. We solve this equation exactly and extract the steady state and the coarsening time in Section 4.

## 4. Analysis

### 4.1 Steady-state wall fraction and the $\varepsilon^{1/2}$ law

Set $d\rho/dt = 0$ in the rate equation:

$$0 = a\,\varepsilon - b\,\rho^{2} \quad\Longrightarrow\quad \rho^{2} = \frac{a\,\varepsilon}{b} \quad\Longrightarrow\quad \rho^{*} = \sqrt{\frac{a}{b}}\;\varepsilon^{1/2}.$$

This reproduces the square-root scaling of the wall fraction with noise strength reported in [1, 2]. The exponent $1/2$ follows solely from the structure creation-is-linear-in-noise / annihilation-is-quadratic-in-density; it is independent of the constants $a$ and $b$.

**Numerical illustration (labeled illustrative parameters).** Take the representative values $a = 1$ (every noise event seeds a wall, the maximal-susceptibility case) and $b = 1$ (unit collision rate), in units where $\rho$ is measured per site and $t$ per macro-step. Then:

- For $\varepsilon = 10^{-2}$: $\rho^{*} = \sqrt{1 \cdot 10^{-2} / 1} = \sqrt{10^{-2}} = 10^{-1} = 0.1$. That is, 10% of sites host a wall.
- For $\varepsilon = 10^{-4}$: $\rho^{*} = \sqrt{10^{-4}} = 10^{-2} = 0.01$, i.e. 1%.
- For $\varepsilon = 0.25$: $\rho^{*} = \sqrt{0.25} = 0.5$, i.e. 50%.

Check of the scaling: reducing $\varepsilon$ by a factor of $10^{2}$ (from $10^{-2}$ to $10^{-4}$) reduces $\rho^{*}$ by a factor of $10^{1}$ (from $0.1$ to $0.01$), consistent with $\rho^{*} \propto \varepsilon^{1/2}$ since $(10^{2})^{1/2} = 10$.

### 4.2 Transient solution

The rate equation is a Riccati-type ODE solvable by separation. With initial condition $\rho(0) = \rho_{0}$:

$$\int \frac{d\rho}{a\varepsilon - b\rho^{2}} = t \quad\Longrightarrow\quad \frac{1}{\sqrt{a b\,\varepsilon}}\,\operatorname{artanh}\!\left(\rho\,\sqrt{\frac{b}{a\varepsilon}}\right) = t + C.$$

Solving for $\rho(t)$ with $C$ fixed by $\rho(0) = \rho_{0}$:

$$\rho(t) = \sqrt{\frac{a\varepsilon}{b}}\;\tanh\!\left(\sqrt{a b\,\varepsilon}\; t + \operatorname{artanh}\!\left(\rho_{0}\sqrt{\frac{b}{a\varepsilon}}\right)\right).$$

**Relaxation time.** The approach to steady state occurs on the timescale

$$\tau = \frac{1}{\sqrt{a b\,\varepsilon}}.$$

With the illustrative parameters $a = b = 1$ and $\varepsilon = 10^{-2}$: $\tau = 1/\sqrt{10^{-2}} = 1/10^{-1} = 10$ macro-steps. For $\varepsilon = 10^{-4}$: $\tau = 1/\sqrt{10^{-4}} = 1/10^{-2} = 100$ macro-steps. Thus weaker noise both lowers the steady wall fraction and lengthens the relaxation time — the system is cleaner but slower to reach its stationary defect density.

### 4.3 Lock-on from random initial conditions

Without noise ($\varepsilon = 0$), the rate equation gives pure annihilation, $d\rho/dt = -b\rho^{2}$, with solution

$$\rho(t) = \frac{\rho_{0}}{1 + b\,\rho_{0}\, t}.$$

**Derivation.** Separating: $d\rho/\rho^{2} = -b\,dt$; integrating: $-1/\rho = -bt + C$; with $\rho(0) = \rho_{0}$, $C = -1/\rho_{0}$; hence $1/\rho = bt + 1/\rho_{0}$, giving the expression above.

**Lock-on criterion.** Take the reported lock-on fraction of over 90% of random initial conditions [1, 2] and ask what initial wall density $\rho_{0}$ is compatible with full coarsening within a window of $T = 1000$ macro-steps on a lattice of length $L = 10^{3}$ sites, assuming walls move at speed $v = 1$ site per macro-step and annihilate in pairs. Full lock-on requires every wall to meet a partner: the mean distance between walls is $\ell = 1/\rho_{0}$, and two approaching walls close the gap at relative speed $2v$, so the mean annihilation time is

$$t_{\text{ann}} = \frac{\ell}{2v} = \frac{1}{2 v \rho_{0}}.$$

Requiring $t_{\text{ann}} \leq T$ with $v = 1$, $T = 1000$:

$$\frac{1}{2\rho_{0}} \leq 1000 \quad\Longrightarrow\quad \rho_{0} \geq \frac{1}{2000} = 5 \times 10^{-4}.$$

So lock-on within $10^{3}$ steps is expected whenever the initial wall density exceeds $5 \times 10^{-4}$ walls per site — i.e., on average one wall per 2000 sites. A random initial condition on $L = 10^{3}$ sites produces desynchronized patches of typical size much smaller than $L$ (each patch boundary is a wall), so $\rho_{0}$ is of order $10^{-2}$–$10^{-1}$ per site, comfortably above the threshold; this is consistent with the >90% lock-on rate reported in [1, 2], and the residual <10% corresponds to initial conditions whose phase texture is already globally coherent or whose walls are pinned by stable embedded structures of the rule-110-equivalent dynamics (gliders acting as permanent walls). We emphasize that $\rho_{0} \sim 10^{-2}$ is an order-of-magnitude assumption, not a measured value; the derivation above shows only the *compatibility* of the reported lock-on rate with the wall picture, not an independent prediction of it.

### 4.4 Noise threshold for sustained computation

A useful derived quantity is the noise strength at which the steady wall fraction equals the wall density needed to sustain one wall per computation-relevant structure. If a universal computation requires at most one defect per $N_{c}$ sites to remain non-disruptive, the tolerable noise satisfies

$$\sqrt{\frac{a\,\varepsilon}{b}} \leq \frac{1}{N_{c}} \quad\Longrightarrow\quad \varepsilon \leq \frac{b}{a\, N_{c}^{2}}.$$

With $a = b = 1$ and, illustratively, $N_{c} = 100$ (one tolerated defect per 100 sites):

$$\varepsilon_{\max} = \frac{1}{100^{2}} = \frac{1}{10^{4}} = 10^{-4}.$$

This quadratic sensitivity — tolerable noise falling as $N_{c}^{-2}$ — is a direct consequence of the $\varepsilon^{1/2}$ law and is, to our knowledge, the main practical constraint on using such emulating systems for actual computation in a noisy environment.

## 5. Results

We report the following, distinguishing derived values, illustrative computations, and reported results.

**R1 (scaling law, derived).** From the rate equation $d\rho/dt = a\varepsilon - b\rho^{2}$, the steady-state wall fraction is $\rho^{*} = \sqrt{a\varepsilon/b}$, scaling as $\varepsilon^{1/2}$, independent of $a$ and $b$. This reproduces the square-root scaling reported in [1, 2].

**R2 (illustrative steady states).** With $a = b = 1$: $\rho^{*} = 0.1$ at $\varepsilon = 10^{-2}$; $\rho^{*} = 0.01$ at $\varepsilon = 10^{-4}$; $\rho^{*} = 0.5$ at $\varepsilon = 0.25$ (arithmetic in Section 4.1).

**R3 (relaxation times, illustrative).** $\tau = 1/\sqrt{ab\varepsilon}$: $\tau = 10$ macro-steps at $\varepsilon = 10^{-2}$ and $\tau = 100$ macro-steps at $\varepsilon = 10^{-4}$, for $a = b = 1$.

**R4 (transient law, derived).** $\rho(t) = \rho_{0}/(1 + b\rho_{0}t)$ in the noiseless case; walls coarsen algebraically, not exponentially.

**R5 (lock-on compatibility, projection).** Under the stated assumptions ($v = 1$ site/step, pairwise annihilation, lock-on window $T = 1000$ steps), lock-on within the window requires $\rho_{0} \geq 5 \times 10^{-4}$ walls per site. Given that random initial conditions generically produce $\rho_{0}$ of order $10^{-2}$–$10^{-1}$ per site (assumption, not measurement), the >90% lock-on rate reported in [1, 2] is consistent with the domain-wall picture; the residual failures are attributed to pinned walls formed by stable glider structures. Uncertainty: the projection is sensitive to the assumed wall speed; if $v = 0.1$, the threshold rises to $\rho_{0} \geq 1/(2 \cdot 0.1 \cdot 1000) = 1/200 = 5 \times 10^{-3}$, still below the assumed generic density.

**R6 (noise tolerance, derived with illustrative $N_{c}$).** The tolerable noise scales as $\varepsilon_{\max} = b/(aN_{c}^{2})$; for $N_{c} = 100$, $a = b = 1$: $\varepsilon_{\max} = 10^{-4}$.

**R7 (reported, not computed here).** Random initial conditions lock on to rule 110 over 90% of the time [1, 2]. We treat this as an empirical input, analyzed for consistency in R5.

## 6. Discussion

**Limitations.** The rate-equation treatment is mean-field: it ignores spatial correlations between walls, fluctuations in wall velocity, and the possibility of wall *creation* by wall–glider collisions. In one dimension, coarsening systems with pairwise annihilation are known to exhibit corrections to mean-field scaling (e.g., wall-density decay constants differing from the mean-field exponent), so the exact prefactor $\sqrt{a/b}$ should be regarded as schematic; the exponent $1/2$ itself is robust within the mean-field description but could be modified by correlated ballistic dynamics. All numerical values in R2, R3, R5, and R6 use illustrative parameters ($a = b = 1$, $v = 1$, $N_{c} = 100$); they demonstrate the structure of the theory, not measured properties of the specific three-rule system of [1, 2], whose constants we do not have access to.

**Failure modes.** Three ways the picture could fail: (i) walls might not be point-like — if walls have internal structure or bind to gliders, annihilation may be incomplete and lock-on would stall above the predicted threshold; (ii) noise might create not only walls but also persistent localized structures (gliders) that never annihilate, in which case the steady state would include a non-vanishing glider gas and the $\varepsilon^{1/2}$ law would hold only for the wall component; (iii) the emulation might be only approximate, holding on a subset of configurations, in which case "lock-on" measures entry into the emulating subset rather than true universality of the composite map.

**What would falsify the claims.** The $\varepsilon^{1/2}$ law would be falsified by direct simulation of [1, 2]'s system showing a steady wall fraction scaling with a different exponent (e.g., $\varepsilon^{1}$, indicating linear rather than quadratic annihilation, or logarithmic scaling indicating an energy-barrier structure). The chirality-by-arrangement claim would be falsified if the reversed schedule $\Phi' = F_{1} \circ F_{2} \circ F_{3}$ emulated rule 110 equally well, which would mean the ordering carries no directional information. The lock-on explanation would be falsified if lock-on probability were found to be independent of the initial density of phase boundaries.

**Against ourselves.** One might object that "diversity alone generates complexity" overstates the result: the *schedule* is itself a structured object, and encoding chirality in a schedule is not obviously cheaper than encoding it in a rule — the composite description $(f_{1}, f_{2}, f_{3}, \text{order})$ may have the same algorithmic content as a chiral rule, in the spirit of the program-size versus time trade-offs studied in [8]. A second objection: universality of the noiseless system says little about the noisy, finite, embodied systems that matter biologically; as [4] argues, micro-level computational competence does not entail macro-level adaptive behavior. A third: our lock-on analysis assumes wall motion is ballistic and unpinned; if walls diffuse rather than ballistically translate, the annihilation time acquires a different density dependence and R5's threshold changes qualitatively.

**Open questions.** What is the exact wall velocity distribution in the three-rule system? Do the walls exhibit bound states? Does the $\varepsilon^{1/2}$ law cross over to a different regime at very small $\varepsilon$, where wall creation becomes rarer than the natural coarsening time? And can the construction be generalized: does *any* chiral universal CA admit an emulation by a cyclic sequence of symmetric rules, and if so, what is the minimum number of constituent rules?

**Significance.** The result of [1, 2], given analytical grounding here, supports a route to complexity through repeated, perturbed units — a pattern ubiquitous in biology, where asymmetric function arises from ordered ensembles of symmetric components. It also carries a message for CA-based models of quantum field theory: broken symmetries such as parity need not be present in the local rules; they can be generated by the dynamics' organization. Incomputability of global properties [9, 3] remains the backdrop: once universality is achieved by any means — however symmetric the parts — undecidability of long-term behavior follows.

## 7. Conclusion

We analyzed the recent demonstration [1, 2] that the Turing-complete elementary cellular automaton rule 110 can be emulated by alternating three individually reflection-symmetric rules. We formalized the construction as a cyclic composition $\Phi = F_{3} \circ F_{2} \circ F_{1}$ of reflection-commuting operators, showing that parity breaking resides in the ordering of the factors. We derived, from the rate equation $d\rho/dt = a\varepsilon - b\rho^{2}$, the steady-state wall fraction $\rho^{*} = \sqrt{a\varepsilon/b}$, reproducing the reported $\varepsilon^{1/2}$ scaling; computed illustrative values ($\rho^{*} = 0.1$ at $\varepsilon = 10^{-2}$, $\rho^{*} = 0.01$ at $\varepsilon = 10^{-4}$ for $a = b = 1$); obtained the algebraic coarsening law $\rho(t) = \rho_{0}/(1 + b\rho_{0}t)$; and showed that the reported >90% lock-on rate from random initial conditions is consistent with a domain-wall annihilation picture, requiring only $\rho_{0} \geq 5 \times 10^{-4}$ walls per site under stated assumptions. The tolerable noise for computation scales quadratically with defect spacing, $\varepsilon_{\max} = b/(aN_{c}^{2})$. The collective message: chirality and universality need not be microscopic properties; they can be emergent consequences of ordering simple, symmetric, repeated units — a mechanism with evident resonance in biological organization.

## References

[1] arXiv Query: search_query=&id_list=2610.09879&start=0&max_results=1 — "We show that the Turing complete rule 110 in elementary cellular automata can be emulated by alternating three simple symmetric rules in space..."

[2] arXiv:2610.09879v1 | A repeating sequence of simple rules creates a universal computer

[3] arXiv:1201.1223v1 | Turing Machines and Understanding Computational Complexity

[4] arXiv:1203.3376v1 | Learning, Social Intelligence and the Turing Test - why an "out-of-the-box" Turing Machine will not pass the Turing Test

[5] arXiv:math/0212047v1 | Infinite Time Turing Machines: Supertask Computation

[6] arXiv:2111.05052v1 | Between Turing and Kleene

[7] arXiv:1110.0271v1 | Alan Turing and the Origins of Complexity

[8] arXiv:1010.1328v2 | Complejidad descriptiva y computacional en maquinas de Turing pequenas

[9] arXiv:1206.1706v1 | The Incomputable Alan Turing

[10] QNFO: Philosophy of Science | DOI 10.5281/zenodo.22757008

[11] QNFO: Syntactic Generation | DOI 10.5281/zenodo.22758173

[12] QNFO: Computational Syntax of Reality | DOI 10.5281/zenodo.19528343

[13] QNFO: Winding Number as Hidden Variable | DOI 10.5281/zenodo.17364877