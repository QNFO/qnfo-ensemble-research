# Emergent Universality from Symmetric Rules: How Three Trivial Cellular Automata Generate the Chirality of Rule 110

## Abstract

Elementary cellular automaton rule 110 is Turing complete, yet its update rule is intrinsically asymmetric: it distinguishes left from right. We study the construction of [1], [2], in which rule 110 is emulated by alternating, in a fixed spatial sequence, three constituent elementary rules that are each individually symmetric under parity (left-right reflection). Because no constituent rule can distinguish left from right, the chirality required for rule 110's universal dynamics resides entirely in the *arrangement* of the rules, not in any local rule. This demonstrates that diversity of simple components, repeated in a structured sequence, suffices to generate computational complexity. We formalize the emulation as a block-map composition, show that the parity-breaking arises from the non-commutation of the constituent maps, and analyze two statistical phenomena reported in [1]: (i) random initial conditions lock on to rule 110 dynamics in over 90% of cases, which we explain through domain-wall motion between desynchronized regions; and (ii) under random noise of strength $\epsilon$, the steady-state domain-wall fraction scales as $\rho \propto \sqrt{\epsilon}$, which we derive from a mean-field rate equation with explicit arithmetic. We situate the result in the broader context of Turing's theory of computation and small universal machines [3], [5], [7], [8], [9], and discuss implications for models of complexity generation in biological and physical systems.

## 1. Introduction

A central question in the sciences of complexity is which minimal ingredients are needed for a system to support universal computation. Turing's 1936 analysis established that a machine with a finite table of simple instructions, a tape, and a head suffices for all of computation [3], and the existence of unsolvable problems within this framework reshaped scientific notions of predictability [9]. Turing's work also seeded the modern concept of complexity itself [7], and small universal Turing machines have long been studied as a way to probe the trade-off between descriptional and computational complexity [8].

In cellular automata (CAs), the analogous question is: how simple can the local update rule be while the global dynamics remains Turing complete? Cook's proof that elementary CA rule 110 is universal answered this dramatically: a one-dimensional binary lattice with a radius-1 rule supports universal computation. Rule 110, however, is *chiral*: its rule table treats the left and right neighbors differently. This raises a natural question, which motivates the present work: is chirality a fundamental requirement for universality in this class, or can it be an emergent property of an arrangement of parity-symmetric components?

The construction of [1], [2] answers the latter. Three elementary CA rules, each individually symmetric under left-right reflection, are applied in a fixed spatially repeating sequence $R_1, R_2, R_3, R_1, R_2, R_3, \ldots$. The composite dynamics emulates rule 110. Since each $R_i$ satisfies $R_i(\text{reflected configuration}) = \text{reflection of } R_i(\text{configuration})$, no local update can create or destroy parity asymmetry; yet the composite is chiral. The chirality is carried by the *sequence order*, an organizational property rather than a property of any rule.

Beyond the existence proof, [1] reports two quantitative phenomena. First, random initial conditions converge to (lock on to) rule 110 dynamics in over 90% of trials, an attractor-like robustness explained by the motion of domain walls between desynchronized regions. Second, when random noise of strength $\epsilon$ is added, errors seed domain walls whose steady-state fraction scales as $\sqrt{\epsilon}$, captured by a simple rate equation. Both phenomena suggest a general route to complexity: repeated, perturbed, individually trivial units — a scenario ubiquitous in biology, from genetic regulatory lattices to cortical microcircuits. The result also carries a lesson for CA-based models of quantum field theory: broken symmetries such as parity need not be present in the local rules to appear in the effective dynamics [1].

This paper has three aims: (1) to give a clean formal statement of the emulation and the origin of chirality in the non-commutation of the constituent maps; (2) to derive, with explicit arithmetic, the $\sqrt{\epsilon}$ scaling of the domain-wall fraction from a rate-equation model; (3) to discuss the robustness of the lock-on phenomenon and its implications.

## 2. Background and Related Work

**Rule 110 and universality.** The primary source [1], [2] establishes the central result under study: the Turing-complete elementary CA rule 110 can be emulated by alternating three simple symmetric rules in space. The constituent rules are individually trivial and parity-symmetric; the chirality of rule 110 is created by their arrangement. The abstract of [1] further reports the two statistical regularities analyzed here: lock-on from random initial conditions in over 90% of cases, and a $\sqrt{\epsilon}$ scaling of the noise-induced domain-wall fraction. Our paper is a formalization and analysis companion to this work, not a claim of novelty for the underlying construction.

**Turing machines and complexity.** The conceptual backdrop is Turing's machine model, whose influences on computation theory and complexity are surveyed in [3]. That work describes the Turing machine and illustrates its importance for the theory of computational complexity; here, the relevance is that universality of rule 110 means the emulating system of three symmetric rules inherits the full computational power of Turing machines, including their undecidability properties [9]. The incomputability theme developed in [9] — the existence of unsolvable problems as a fundamental challenge to Laplacian predictability — applies verbatim to the emulated dynamics: predicting whether the three-rule system ever reaches a given configuration is, in general, undecidable.

**Small machines and complexity trade-offs.** The study of small Turing machines in [8] explores trade-offs between algorithmic (program-size) and computational (time) complexity measures in the context of computation universality. Our construction is a cellular-automaton analogue of this program: the "program" describing rule 110 is compressed into a spatial sequence of three trivial rules plus one bit of phase information, trading a larger description of the *update schedule* for simpler constituent rules. This is precisely the kind of descriptional-complexity redistribution [8] advocates analyzing.

**Variants of Turing computation.** Infinite-time Turing machines extend ordinary Turing machines into transfinite ordinal time, providing a model of infinitary computability [5]. While our system operates in ordinary discrete time, the emulation result sharpens the picture in [5]: even the finite-time dynamics of a parity-symmetric-rule system can be universal, so infinitary extensions are a matter of computational strength, not of local rule complexity. Similarly, [6] compares Turing's framework for computing with real numbers against Kleene's schemes S1–S9 for computing with objects of finite type; the three-rule construction shows that the *substrate* of a universal computer can be made more homogeneous (all rules symmetric) without changing the computable functions, which is orthogonal to but consistent with the Turing–Kleene unification sought in [6].

**Turing, learning, and intelligence.** The Turing Test literature [4] distinguishes a macro-level, post-hoc, adaptive test of intelligence from the micro-level, a priori definition of a Turing machine. Our result is relevant to this distinction: a system whose local rules are trivial and symmetric can still be a universal computer in Turing's micro-level sense, yet whether it *behaves* intelligently — adapts, learns, passes conversational tests [4] — is a separate, emergent question. The lock-on phenomenon studied in Section 4 is a step in this direction: it shows the system has a robust dynamical identity that survives perturbation, a precondition for adaptive behavior.

**Turing and the origins of complexity.** The retrospective in [7] assesses how Turing's work changed views on the foundations of complexity across fields. The present construction can be read as a concrete instantiation of a Turingian theme highlighted in [7]: complexity as an organizational, not material, property. Finally, the QNFO corpus materials on philosophy of science [10], syntactic generation [11], computational syntax [12], and the winding number as a hidden variable [13] provide a broader framing in which organizational or topological variables — here, the phase of the rule sequence and the positions of domain walls — act as hidden degrees of freedom that determine effective behavior; the analogy with [13] is that a quantity invisible at the level of local rules (the sequence phase) governs the global chirality.

## 3. Methods

### 3.1 Elementary cellular automata and parity symmetry

An elementary cellular automaton consists of a binary lattice $a_i(t) \in \{0,1\}$, $i \in \mathbb{Z}$, updated synchronously by a radius-1 rule:

$$a_i(t+1) = f\big(a_{i-1}(t), a_i(t), a_{i+1}(t)\big),$$

where $f: \{0,1\}^3 \to \{0,1\}$ is the rule table. Rule 110 is the rule with Wolfram code $110 = 0 \cdot 2^7 + 1 \cdot 2^6 + 1 \cdot 2^5 + 1 \cdot 2^4 + 0 \cdot 2^3 + 1 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0$, i.e., $f_{110}(1,1,1)=0$, $f_{110}(1,1,0)=1$, $f_{110}(1,0,1)=1$, $f_{110}(1,0,0)=1$, $f_{110}(0,1,1)=0$, $f_{110}(0,1,0)=1$, $f_{110}(0,0,1)=1$, $f_{110}(0,0,0)=0$. Note that $f_{110}(1,1,0) = 1$ while $f_{110}(0,1,1) = 0$: the rule distinguishes the left neighbor from the right neighbor, which is the chirality essential to its glider dynamics.

A rule $f$ is *parity-symmetric* if for the reflection operator $\sigma$ defined by $(\sigma a)_i = a_{-i}$,

$$f(x, y, z) = f(z, y, x) \quad \text{for all } (x,y,z) \in \{0,1\}^3.$$

The three constituent rules $R_1, R_2, R_3$ of [1], [2] each satisfy this condition. Consequently, for any configuration $a$,

$$R_i(\sigma a) = \sigma R_i(a), \qquad i \in \{1,2,3\}.$$

### 3.2 The alternating construction

The emulating system applies the three rules in a fixed spatial sequence. Partition the lattice into blocks of three sites; site $i$ belongs to class $c(i) = i \bmod 3$. At each global time step $t$, every site is updated by the rule assigned to its class:

$$a_i(t+1) = R_{c(i)+1}\big(a_{i-1}(t), a_i(t), a_{i+1}(t)\big),$$

with the class index taken modulo 3. The update map is thus the direct sum over classes:

$$T = R_1 \oplus R_2 \oplus R_3,$$

applied to the whole lattice simultaneously, with the spatial period-3 pattern of rules fixed for all time. Because the pattern $R_1, R_2, R_3$ repeats with period 3 in space and is applied uniformly in time, the composite map $T$ is *not* parity-symmetric: reflecting the lattice maps the class pattern $c(i)$ to $c(-i) = (-i) \bmod 3$, which reverses the order of the rules. Formally,

$$T(\sigma a) = \sigma (T^{-1}_{\text{seq}} T)(a) \neq \sigma T(a) \quad \text{in general},$$

where $T^{-1}_{\text{seq}}$ denotes reversal of the rule sequence. The chirality of the composite is therefore carried entirely by the *ordering* of the three symmetric rules — an organizational, not local, property.

### 3.3 Emulation of rule 110

Following [1], [2], the composite dynamics $T$ emulates rule 110 in the standard sense of block emulation: there exists a coarse-graining map $\Phi$ from configurations of the three-rule system to configurations of rule 110, and a time-scale factor $\lambda \geq 1$, such that

$$\Phi\big(T^{\lambda n}(A)\big) = F_{110}^{n}\big(\Phi(A)\big)$$

for all initial conditions $A$ in a suitable set, where $F_{110}$ is the global map of rule 110. The emulation is exact on the set of configurations reachable from the encoded initial conditions, and the constituent rules are chosen so that the period-3 spatial structure of $T$ reproduces the asymmetric neighborhood sampling that rule 110 performs. Since rule 110 is Turing complete [1], [2], the three-rule system is Turing complete as well.

### 3.4 Domain walls and noise

Two statistical phenomena are analyzed. First, *lock-on*: starting from random initial conditions, the system converges to the emulated rule 110 dynamics in over 90% of trials [1]. The mechanism is the motion of domain walls — boundaries between regions of the lattice that are in different phases of the period-3 rule pattern relative to the local rule 110 structure. Walls move, annihilate on contact, and the surviving region imposes its phase on the whole lattice.

Second, *noise-driven wall production*: with probability $\epsilon$ per site per time step, a site's value is flipped after the deterministic update. Each flip is an *error* that can seed a new domain wall. We model the wall density $\rho(t)$ (fraction of adjacent site pairs that are domain walls) with a mean-field rate equation in Section 4.

## 4. Analysis

### 4.1 Parity breaking by sequence order

We first verify the claim that no constituent rule breaks parity, but the composite does. Each $R_i$ satisfies $R_i(x,y,z) = R_i(z,y,x)$ by construction [1]. Consider the composite acting on a reflected configuration. Let $c(i) = i \bmod 3$ and define the reflected class function $c^{-}(i) = c(-i)$. Then

$$T(\sigma a)_i = R_{c(i)+1}\big(a_{-i-1}, a_{-i}, a_{-i+1}\big) = R_{c(i)+1}\big((\sigma a)_{i-1}, (\sigma a)_i, (\sigma a)_{i+1}\big),$$

whereas

$$\sigma (T a)_i = (T a)_{-i} = R_{c(-i)+1}\big(a_{-i-1}, a_{-i}, a_{-i+1}\big) = R_{c^{-}(i)+1}\big(a_{-i-1}, a_{-i}, a_{-i+1}\big).$$

Since $c(i) + 1 \neq c^{-}(i) + 1$ for $i \not\equiv 0 \pmod 3$ (for example, at $i = 1$: $c(1) = 1$ so the left expression uses $R_2$, while $c^{-}(1) = c(-1) = 2$ so the right expression uses $R_3$), the two expressions differ whenever $R_2 \neq R_3$ on the relevant neighborhood. Hence $T(\sigma a) \neq \sigma T(a)$ generically: the composite is chiral even though no constituent is. This is the precise sense in which "the chirality of rule 110 is created by their arrangement" [1].

### 4.2 Rate equation for the domain-wall fraction

We now derive the $\sqrt{\epsilon}$ scaling reported in [1]. Let $\rho(t)$ denote the fraction of domain walls per lattice site at time $t$. Two processes govern $\rho$:

1. **Production:** noise of strength $\epsilon$ (probability of a random flip per site per step) creates errors; a fraction $p_{\text{seed}}$ of errors seed a new domain wall. Production rate per site: $g = p_{\text{seed}} \, \epsilon$.
2. **Annihilation:** domain walls perform biased or diffusive motion and annihilate when two walls meet. In a mean-field picture, the annihilation rate is proportional to the probability of finding two walls adjacent, which scales as $\rho^2$. With annihilation coefficient $k$ (in units of walls per site per step), the loss term is $k \rho^2$.

The mean-field rate equation is:

$$\frac{d\rho}{dt} = p_{\text{seed}} \, \epsilon - k \rho^2.$$

At steady state, $\frac{d\rho}{dt} = 0$, so

$$k \rho_{\text{ss}}^2 = p_{\text{seed}} \, \epsilon \quad \Longrightarrow \quad \rho_{\text{ss}} = \sqrt{\frac{p_{\text{seed}} \, \epsilon}{k}}.$$

Thus $\rho_{\text{ss}} \propto \sqrt{\epsilon}$, independent of the constants, which is the scaling reported in [1]: "the fraction scales with the square root of noise strength."

**Explicit numerical example.** Take the maximally favorable seeding fraction $p_{\text{seed}} = 1$ (every error seeds a wall — an upper bound) and annihilation coefficient $k = 1$ (each adjacent wall pair annihilates within one time step — a normalization choice). For noise strength $\epsilon = 10^{-4}$:

$$\rho_{\text{ss}} = \sqrt{\frac{1 \times 10^{-4}}{1}} = \sqrt{10^{-4}} = 10^{-2} = 0.01.$$

So at $\epsilon = 10^{-4}$, the steady-state wall fraction is $\rho_{\text{ss}} = 0.01$, i.e., one domain wall per 100 sites. Doubling the noise to $\epsilon = 4 \times 10^{-4}$ gives

$$\rho_{\text{ss}} = \sqrt{4 \times 10^{-4}} = 2 \times 10^{-2} = 0.02,$$

confirming the square-root law: a factor-of-4 increase in $\epsilon$ yields a factor-of-2 increase in $\rho_{\text{ss}}$. More generally, for a target wall fraction $\rho_{\text{ss}}$, the critical noise strength is

$$\epsilon_{\text{crit}} = \frac{k \, \rho_{\text{ss}}^2}{p_{\text{seed}}}.$$

For $\rho_{\text{ss}} = 0.05$ with $k = 1$, $p_{\text{seed}} = 1$: $\epsilon_{\text{crit}} = (0.05)^2 = 2.5 \times 10^{-3}$. Below this noise strength, the mean-field model predicts the wall fraction stays under 5%.

### 4.3 Lock-on and domain-wall dynamics

The lock-on phenomenon — convergence to rule 110 dynamics from random initial conditions in over 90% of trials [1] — can be understood with the same wall picture. Random initial conditions generate many desynchronized regions; their bounding walls move with velocity $v$ (determined by the phase relationship between the period-3 rule pattern and the rule 110 glider structure) and annihilate pairwise. If walls annihilate faster than they are created (no noise, $\epsilon = 0$, so production $g = 0$), the wall density decays and the system locks on to a single phase — the emulated rule 110 dynamics.

The reported lock-on fraction exceeding 90% implies a failure fraction below 10%:

$$1 - 0.90 = 0.10,$$

i.e., at most $10^{-1}$ of random initial conditions fail to lock on. These failures correspond to initial conditions whose wall configuration is a dynamical trap — e.g., walls that are stationary or form stable periodic patterns rather than annihilating. The mean-field annihilation picture predicts complete lock-on ($\rho \to 0$) in the absence of noise; the observed $\sim 10\%$ failure rate measures the measure of such trapped initial conditions, which the mean-field model does not capture. We therefore treat the 90% figure as an empirical input from [1], not a derivation.

### 4.4 Consistency check: wall density versus lock-on

As a consistency check on the two regimes, note that the noise-driven steady state of Section 4.2 and the noiseless lock-on of Section 4.3 are limiting cases of the same rate equation. With production and annihilation both active, the relaxation time toward steady state is obtained by linearizing around $\rho_{\text{ss}}$. Writing $\rho = \rho_{\text{ss}} + \delta$, with $\delta \ll \rho_{\text{ss}}$:

$$\frac{d\delta}{dt} = -k(\rho_{\text{ss}} + \delta)^2 + k \rho_{\text{ss}}^2 \approx -2 k \rho_{\text{ss}} \, \delta,$$

so the relaxation rate is $\Gamma = 2 k \rho_{\text{ss}}$ and the relaxation time is

$$\tau = \frac{1}{2 k \rho_{\text{ss}}}.$$

For the example of Section 4.2 ($k = 1$, $\rho_{\text{ss}} = 0.01$ at $\epsilon = 10^{-4}$):

$$\tau = \frac{1}{2 \times 1 \times 0.01} = \frac{1}{0.02} = 50 \text{ time steps}.$$

Thus at $\epsilon = 10^{-4}$ the system re-equilibrates its wall population on a timescale of $50$ steps under the mean-field model, which is fast compared with the timescales of the emulated rule 110 computation, explaining why computation and error correction coexist: the wall population reaches steady state long before the emulated dynamics decorrelates.

## 5. Results

We report the following results, distinguishing derivations from empirical inputs.

**R1 (derived).** The composite map $T = R_1 \oplus R_2 \oplus R_3$ with spatially period-3 rule assignment is not parity-symmetric even though each $R_i$ is: at site $i = 1$, the forward update uses rule $R_2$ (since $c(1) = 1$) while the reflected update uses rule $R_3$ (since $c(-1) = 2$), and $R_2 \neq R_3$ on generic neighborhoods. Chirality is therefore a property of the arrangement alone (Section 4.1).

**R2 (derived, mean-field).** The steady-state domain-wall fraction under noise obeys $\rho_{\text{ss}} = \sqrt{p_{\text{seed}} \epsilon / k}$, hence $\rho_{\text{ss}} \propto \sqrt{\epsilon}$. With the normalization $p_{\text{seed}} = 1$, $k = 1$: at $\epsilon = 10^{-4}$, $\rho_{\text{ss}} = 0.01$; at $\epsilon = 4 \times 10^{-4}$, $\rho_{\text{ss}} = 0.02$; the critical noise for $\rho_{\text{ss}} = 0.05$ is $\epsilon_{\text{crit}} = 2.5 \times 10^{-3}$ (Section 4.2). The proportionality $\rho_{\text{ss}} \propto \sqrt{\epsilon}$ is the scaling reported empirically in [1]; the absolute prefactor $\sqrt{p_{\text{seed}}/k}$ is a model normalization, not a measured quantity.

**R3 (derived, mean-field).** The relaxation time of the wall population is $\tau = 1/(2 k \rho_{\text{ss}})$; at $\epsilon = 10^{-4}$ with $k = 1$, $\tau = 50$ time steps (Section 4.4).

**R4 (empirical input from [1], not derived here).** Random initial conditions lock on to rule 110 dynamics in over 90% of trials; equivalently, the failure fraction is below $0.10$. We computed only the arithmetic complement $1 - 0.90 = 0.10$; the 90% figure itself is an empirical report of [1] and its mechanism (domain-wall motion between desynchronized regions) is consistent with, but not derived by, our rate equation.

**R5 (structural).** Because rule 110 is Turing complete and the three-rule system emulates it [1], [2], the three-rule system is Turing complete. Consequently, by the undecidability results underlying Turing's theory [3], [9], prediction of the emulated dynamics is in general incomputable, and the system instantiates the program-size versus time-complexity trade-offs studied for small universal machines [8] in a cellular-automaton setting.

## 6. Discussion

**Limitations of the mean-field model.** The rate equation $\frac{d\rho}{dt} = p_{\text{seed}} \epsilon - k \rho^2$ assumes spatially homogeneous wall mixing, which is valid only if walls diffuse rapidly relative to their creation. In one dimension, annihilation processes of the form $A + A \to \emptyset$ with initially random positions are known to show density scaling that can deviate from mean field at long times because of fluctuations and the depletion of the wall population into ever-larger empty intervals. The $\sqrt{\epsilon}$ law reported in [1] is an empirical observation; our derivation shows it is the natural mean-field outcome, but a fluctuation-corrected treatment could modify the exponent or introduce logarithmic corrections. Testing this would require stochastic simulations, which we have not performed here and do not report.

**The 90% lock-on figure.** We take the lock-on fraction as an empirical input from [1]. Our framework explains the *mechanism* (wall motion and annihilation) but does not predict the *value*; the $\sim 10\%$ failure fraction is set by the measure of trapped initial configurations, which depends on details of the constituent rules and is not captured by any homogeneous rate equation. A falsification test for our wall-based explanation would be: if lock-on is wall-mediated, then suppressing wall mobility (e.g., by pinning the phase pattern) should reduce the lock-on fraction substantially; if lock-on persisted unchanged, the wall picture would be wrong.

**What would falsify the emulation claim.** The emulation rests on the existence of a coarse-graining $\Phi$ and time factor $\lambda$ such that $\Phi(T^{\lambda n}) = F_{110}^n \Phi$ on the relevant initial set. If the emulation held only on a set of measure zero, or required $\lambda$ growing with system size, the universality claim would be vacuous in the thermodynamic limit. The construction of [1], [2] asserts a genuine emulation; independent verification on finite lattices with explicit $\Phi$ and $\lambda$ would strengthen the result.

**Failure modes of the diversity argument.** The claim "diversity alone can generate emergent phenomena" must be qualified. Three arbitrary symmetric rules do not, in general, emulate rule 110; the specific triple and their specific order matter. Diversity is necessary in this construction but not sufficient — the *arrangement* is doing precise, nongeneric work. An overreading of the result would be that any heterogeneous ensemble of trivial rules becomes universal; the correct statement is that universality does not require any individually asymmetric (or individually complex) rule.

**Open questions.** (1) What is the minimal number of distinct symmetric rules needed for emulation — is three optimal, or can two suffice? (2) Does the $\sqrt{\epsilon}$ prefactor $\sqrt{p_{\text{seed}}/k}$ admit a universal value across rule triples, or is it construction-specific? (3) How does the lock-on fraction depend on the ensemble of initial conditions — e.g., product-random versus low-entropy initial states? (4) In CA models of quantum field theory [1], does the sequence-phase degree of freedom play the role of a hidden topological variable, in the spirit of the winding-number construction of [13]? (5) Does the lock-on phenomenon constitute a primitive form of the adaptive robustness discussed in the Turing Test context [4], or is it purely a passive attractor property?

**Relation to the broader Turing literature.** Our result is a data point in the program, traced in [7], of understanding complexity as arising from organization rather than from complicated parts. It complements the small-machine analysis of [8] (complexity redistributed between rule table and update schedule), the infinitary extensions of [5] (universality in ordinary discrete time suffices for the finite-time theory), the real-number versus finite-type computation comparison of [6] (the substrate can be made more homogeneous without changing computable content), and the incomputability theme of [9] (the emulated dynamics inherits undecidability). The philosophical framing of [10], [11], [12] — in which syntactic structure generated from simple elements carries semantic weight — offers a lens on the same phenomenon: the rule sequence is a minimal "syntax" whose ordering generates the "semantics" of chirality and computation.

## 7. Conclusion

We have analyzed the construction of [1], [2] in which the Turing-complete, chiral elementary cellular automaton rule 110 is emulated by three individually trivial, parity-symmetric rules applied in a fixed spatial sequence. We showed formally that parity breaking resides in the non-commutation of the composite with reflection — a consequence of the rule sequence order, not of any local rule — establishing that chirality here is an organizational property. We derived, via a mean-field rate equation with explicit arithmetic, the square-root scaling of the noise-induced domain-wall fraction, $\rho_{\text{ss}} = \sqrt{p_{\text{seed}} \epsilon / k}$, reproducing the $\sqrt{\epsilon}$ law reported in [1], with the numerical examples $\rho_{\text{ss}} = 0.01$ at $\epsilon = 10^{-4}$ and $\epsilon_{\text{crit}} = 2.5 \times 10^{-3}$ for a 5% wall fraction under the normalization $p_{\text{seed}} = k = 1$, and a relaxation time $\tau = 50$ steps at $\epsilon = 10^{-4}$. The reported lock-on of random initial conditions to rule 110 dynamics in over 90% of trials is consistent with domain-wall annihilation in the noiseless limit, with the residual $\sim 10\%$ failure fraction attributable to trapped wall configurations outside the mean-field description. The construction demonstrates a route to complexity through repeated, perturbed, individually trivial units — a scenario common in biology — and shows that in cellular-automaton models of quantum field theory, broken symmetries such as parity need not be present in the local rules [1]. The deeper message, in the lineage of Turing's work on universality and incomputability [3], [7], [9], is that computational complexity is a property of organization: a repeating sequence of simple rules creates a universal computer.

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