# Critical Values on a Non-Uniform Number Line: Bifurcation Markers, Normalization Dependence, and the Conjectured Specialness of Physical Constants

## Abstract

We examine the conjecture that the real number line, as a model of physical state space, is misleadingly uniform: that certain parameter values act as topological phase boundaries rather than smooth increments, and that fundamental constants such as the fine-structure constant $\alpha \approx 1/137$ may mark bifurcation points between qualitatively different dynamical regimes. The specific gap is that the conjecture has been stated qualitatively, without a formal map from parameter values to dynamical regimes and without checking whether the conjectured constants actually sit at the thresholds of minimal models built to test the idea. We formalize a number-to-phase-space map $\Phi$ that assigns to each parameter value the topological equivalence class of the associated dynamics, making precise in what sense a parameter value can be a "boundary." We work three canonical examples in full arithmetic: the simple pendulum, whose separatrix sits at normalized energy $\varepsilon = 2$ exactly; the double pendulum, whose flip threshold is an excess energy $\Delta E = 4\,mgl$, yielding critical values $1$, $4/3$, or $4$ under different normalizations; and a central-force problem with a $1/r^{2}$ correction, whose fall-to-center threshold sits at dimensionless coupling $\beta = -1$ exactly. Every small-integer threshold is shown to be a normalization artifact. We compute $\alpha \approx 7.29927 \times 10^{-3}$ from the value $1/137$, show it lies a factor of $\approx 137$, i.e., $\log_{10}(1/\alpha) \approx 2.14$ orders of magnitude, below the order-unity thresholds of the minimal models, and state the conjectured dynamical role of $\alpha$ as an explicitly labeled hypothesis with falsification conditions. A labeled projection for $N = 100$ coupled subsystems sharing one threshold yields a configuration space of order $10^{30}$. The practical change: model-builders proposing constants-as-bifurcation-points now have an explicit requirement to meet — a derived threshold at $\beta_{c} = \alpha$ — and a falsification protocol.

## 1. Introduction

Physics pedagogy and practice overwhelmingly treat the real numbers as a uniform stage: the interval between $1.0$ and $1.1$ is, by assumption of the formalism, "the same kind" of interval as that between $2.0$ and $2.1$. Working dynamical intuition contradicts this. In pendulum systems, crossing a single normalized energy value changes the qualitative character of all future motion; on either side of that value, infinitesimally nearby parameter points belong to dynamically distinct worlds.

Who faces this problem concretely? Anyone who builds or interprets models with dimensionless control parameters: the dynamical-systems researcher choosing normalizations, the physics educator explaining why certain values seem "special," and, at the speculative frontier, model-builders who hope to explain the numerical values of fundamental constants rather than treat them as free inputs. Today the first two groups handle normalization as an unexamined convention, and the third group — represented here by the Continuum Critique programme, whose Paper P2 hypothesizes that the fine-structure constant $\alpha \approx 1/137$ is "a critical eigenvalue of a helical null-curve stability condition — a geometric fixed point, not a free parameter" [10] — has no shared formal criterion for what would count as a constant sitting at a threshold. If the result of this paper holds — that threshold numerals are normalization artifacts while the existence of thresholds is physical, and that $\alpha$ does not sit at the threshold of the minimal test models — then the third group gains a precise, checkable requirement, and the first two gain an argument for reporting bifurcation structure rather than critical numerals.

The source conjecture motivating this paper holds that (i) the real number line is a misleading projection of physical state spaces, whose intervals are not uniformly meaningful; (ii) certain values — the conjecture's example is the integer $1$ at the double pendulum's flip threshold under a suitable normalization — act as topological phase boundaries, where the accessible topology of motion changes qualitatively rather than smoothly; and (iii) fundamental constants such as the fine-structure constant $\alpha \approx 1/137$ may similarly mark bifurcation points separating qualitatively different regimes, for example bound helical versus unbound motion in a Zitterbewegung-type self-interacting particle model. The Continuum Critique monograph states the underlying thesis directly: "The real-number continuum is a flat projection that conceals qualitative phase boundaries, topological transitions, and the discrete combinatorial substrate of physical and mathematical law" [10].

This paper tests the internal logic of that conjecture rather than asserting or dismissing it. We do four things. First, we formalize a number-to-phase-space map: given a family of dynamical systems indexed by a parameter $\lambda$, we characterize how the qualitative structure of solutions changes across critical values $\lambda_{c}$, and we show how the numerical value of $\lambda_{c}$ depends on normalization. Second, we carry out explicit derivations for the simple pendulum separatrix, the double pendulum flip threshold, and the fall-to-center threshold of a central-force problem with a $1/r^{2}$ correction, showing that each yields a small-integer critical value under the normalizations the conjecture implicitly uses, and explaining arithmetically why this is so. Third, we compute the fine-structure constant from the value $1/137$ and ask whether an $\alpha$-scale coupling could sit at the threshold of a minimal helical self-interacting particle model; we find that it cannot without fine-tuning, since the derived threshold is at order unity while $\alpha \approx 7.29927 \times 10^{-3}$, a separation of roughly two orders of magnitude. Fourth, we quantify the combinatorial richness that a single shared threshold generates across many coupled subsystems, as a labeled projection.

Our conclusion is deliberately two-sided. The conjecture is correct that parameter space is not phenomenologically uniform: bifurcation values genuinely partition it into regimes with different accessible topology, a fact documented in the bifurcation literature we review. But the further step — that the specific numerical values of fundamental constants are therefore explained as bifurcation points — does not follow, because the numerical value of a dimensionless critical parameter is convention-dependent once normalization is fixed, and because the constants we examine do not sit at the thresholds of the minimal models built to test the idea. We state the conditions under which this negative conclusion would be overturned.

The contributions are:

- A formal number-to-phase-space map $\Phi$ whose discontinuities define "bifurcation markers," with the normalization-dependence of marker numerals made explicit (derived in Section 3.1 and applied in Sections 4.1–4.3).
- A full derivation that the double pendulum's flip threshold is an excess energy $\Delta E = 4\,mgl$, giving critical values $1$, $4/3$, or $4$ under three conventions — showing that the conjecture's flagship integer $1$ is produced by dividing the threshold by itself (Section 4.2).
- A full derivation of the fall-to-center threshold $\beta = 2mB/L^{2} = -1$ for a central-force model with a $1/r^{2}$ correction, the minimal stand-in for the conjectured helical self-interacting particle (Section 4.3).
- A quantitative gap computation: $\alpha \approx 7.29927 \times 10^{-3}$ sits a factor of $\approx 137$, i.e., $\log_{10}(1/\alpha) \approx 2.14$ orders of magnitude, below the order-unity thresholds, so any constants-as-bifurcation model must contain a mechanism shifting thresholds by two orders of magnitude (Section 4.4).
- A labeled projection that $N = 100$ independent binary subsystems sharing one threshold generate $2^{100} \approx 1.27 \times 10^{30}$ regime configurations, quantifying the combinatorial reach of a single threshold (Section 4.5).
- Falsification conditions and a proposed smallest next test for the $\alpha$-as-marker hypothesis (Sections 6 and 7).

## 2. Background and Related Work

This section discusses ten works from the literature, in four groups: bifurcation phenomenology, non-uniform representation, threshold-based decision structure, and arithmetic perspectives on special numbers, plus the two QNFO works that state the conjecture itself.

**Bifurcation phenomenology as the physics of non-uniform parameter space.** Reference [3] presents experimental results on the quenching dynamics of an extended thermo-convective system — a network array of approximately 100 convective oscillators — going through a secondary subcritical bifurcation, and characterizes the resulting dynamical phase transition through the nature of the one-dimensional domain-wall fronts connecting the basic multicellular pattern with a new oscillating one. Its experimental setup fixes the control parameter as the vertical temperature difference $\Delta T_{v} = T_{h} - T_{a}$ and defines a reduced control parameter $\varepsilon = (\Delta T_{v} - \Delta T_{vc})/\Delta T_{v}$, where $\Delta T_{vc}$ is the critical value at the threshold [3]. This is directly relevant to our argument: it is an experimental demonstration that a control parameter's crossing of a critical value changes the *topology* of the accessible pattern space (new domains, new walls between domains), not merely the values of observables. It also supplies the concrete subsystem count used in our combinatorial projection of Section 4.5: the initial stationary pattern has wavelength $\lambda_{s} = 4.75 \pm 0.05$ mm, corresponding to an array of 95 latent oscillators [3]. Note also that [3]'s reduced parameter $\varepsilon$ is itself a normalization — the temperature difference measured relative to its own critical value — which is exactly the convention-dependence this paper formalizes.

Reference [4] studies orbital behavior near complex unstable periodic orbits in a three-dimensional autonomous Hamiltonian system of galactic type, showing that at a transition of a family of periodic orbits from stability to complex instability — the Hamiltonian Hopf bifurcation — the four eigenvalues of the stable periodic orbits move out of the unit circle and the orbits become complex unstable [4]. Its conclusions describe the post-bifurcation phase-space structure concretely: near the bifurcation, the consequents of complex unstable periodic orbits form a spiral structure that is a four-dimensional object, and they form a "confined torus" disk structure on which they arrive at a maximum distance from the periodic orbit and move inward, repeatedly [4]. This supplies a precise, eigenvalue-level mechanism by which a smooth change of a parameter produces a qualitative regime change — exactly the "phase boundary on the number line" phenomenon the conjecture gestures at, but stated in invariant terms (eigenvalues crossing the unit circle) rather than in terms of a critical numeral.

Reference [5] reviews bifurcation sequences of periodic orbits in general position for a family of resonant Hamiltonian normal forms with nearly equal unperturbed frequencies, invariant under $\mathbb{Z}_{2} \times \mathbb{Z}_{2}$ symmetry, investigated with geometric methods and connected to the singularity-theory approach [5]. Its normal form is built on a quasi-resonance condition $\omega_{1} = (1 + \delta)\omega_{2}$ with detuning parameter $\delta$, and the reduced Hamiltonian to first order is $\mathcal{K} = \mathcal{E} + \alpha_{2}\mathcal{E}^{2} + (\delta - (2\alpha_{2} + \alpha_{3})\mathcal{E})J + (\alpha_{1} + \alpha_{2} - \alpha_{3})J^{2} + \alpha_{4}J(\mathcal{E} - J)\cos 2\psi$ [5]. It shows that near a single resonance, parameter space is organized into an entire *sequence* of bifurcations, not one boundary — reinforcing our point that critical values are dense, structured features of families, not isolated magic numbers.

**Non-uniformity of representation.** Reference [6] addresses visualization of large datasets, where almost every visual technique reveals drawbacks at scale; it introduces a formal environment modeling image features such as absolute and relative density in a virtual space, and builds on these measures an automatic non-uniform sampling strategy aimed at reducing degradation [6]. Its conclusion states the mechanism: a low-grain non-uniform sampling technique automatically reduces visual clutter in a 2D scatter plot and preserves relative densities, using a formal model describing overplotting, screen occupation, and both data density and represented data density, which allows computing where, how, and how much to sample [6]. Its core move is directly analogous to ours: a uniform grid over a domain misrepresents the domain's structure, and a non-uniform re-parameterization preserves features (there, density; here, bifurcation topology) that uniform treatment destroys. We use it as the closest methodological precedent for a "non-uniform number line" in the literature we review.

**Threshold-based decision structure.** References [1] and [2] come from power-infrastructure risk, and we cite them for their structural analogy, not their subject matter. Reference [1] frames wildfire-ignition mitigation from power line faults as a prioritization problem: long-term ignition prevention strategies, especially converting overhead lines to underground cables, are expensive, so it is important to prioritize upgrades on lines that will reduce wildfire ignition risk the most [1]. Its method defines, for each line segment $l$, an associated wildfire risk $R_{l}$ and a cost of undergrounding $C_{l}$, with a binary decision variable $z_{l}$ representing whether the segment is undergrounded [1]. Reference [2] proposes a mathematical optimization problem — the Multi-period Optimal Power Shutoff And Restoration (MOPSAR) problem — to help utilities decide where and when to implement preemptive power shutoffs, which mitigate ignition risk but cause widespread outages, and how to co-optimize shutoffs with restoration in a rolling-horizon framework [2]. Its conclusion reports that a higher risk threshold incentivizes more system redundancy, thus increasing operational security but also wildfire risk [2]. Both works embody the same logical form as a bifurcation threshold: a continuous risk landscape acted on by a discrete intervention that is worthwhile only above a critical value. They illustrate that "critical value" reasoning is a general decision-theoretic pattern, independent of any specialness of the critical number itself — and in [2] the threshold is explicitly a tunable policy parameter, underlining how conventional threshold numerals can be.

**Arithmetic perspectives on special numbers.** Reference [7] investigates the $a$-numbers of $\mathbb{Z}/p^{2}\mathbb{Z}$-covers of the projective line in characteristic $p > 2$, extending a technique originally introduced by Farnell and Pries for $\mathbb{Z}/p\mathbb{Z}$-covers, and demonstrates as an application that the $a$-numbers of "minimal" $\mathbb{Z}/9\mathbb{Z}$-covers can be deduced from the associated branching datum [7]. Its main theorem gives the formula explicitly: for a minimal $\mathbb{Z}/9\mathbb{Z}$-cover $Y_{2} \to \mathbb{P}^{1}$ with branching datum encoded by counts $n_{1}, n_{2}, n_{3}, n_{4}$, the $a$-number satisfies $a_{Y_{2}} = 3n_{1} + 7n_{2} + 0n_{3} + 3n_{4}$ [7]. This is a case where an integer-valued invariant of a geometric object is *determined* by discrete arithmetic data — a rigorous instance of numbers being "special" for structural reasons.

Reference [8] proves, for a non-CM simple abelian variety $A$ over a number field $K$ with connected monodromy groups, that the set of places $v$ of good reduction for which the Frobenius field $F(A,v)$ is isomorphic to a fixed number field has upper Dirichlet density zero [8]. Its proof strategy uses the Chebotarev density theorem to bound the relevant union of conjugacy classes, and its quantitative version combines the effective Chebotarev theorem of Lagarias–Odlyzko with the Selberg sieve to obtain a power saving upper bound for the number of places with a given Frobenius field [8]. This is a density-zero statement: in a precise arithmetic sense, most places are *not* special, and the exceptional set is thin. We use both works as contrasts: arithmetic structure can make specific numbers distinguished, but the distinguished sets are provably thin — a caution against reading every salient constant as a generic feature.

**The QNFO works stating the conjecture.** Reference [9] is the prior version of the present paper, which formalizes the same number-to-phase-space map, derives the same three thresholds ($\varepsilon_{\text{sep}} = 2$ for the pendulum, $\Delta E = 4\,mgl$ with critical values $1$, $4/3$, $4$ for the double pendulum, and $\beta = 2mB/L^{2} = -1$ for the central-force model), and already flags in its discussion that if bifurcation markers under natural normalizations are generically irrational rather than concentrated on small integers, then "special values" reduce to convention and the non-uniformity thesis loses content [9]. The present paper extends [9] by adding the practical-implications analysis of Section 7 and sharpening the falsification protocol. Reference [10] is the Continuum Critique Trilogy, whose Paper P2 states the strongest form of the conjecture we test: "The fine-structure constant $\alpha \approx 1/137$ is hypothesised to be a critical eigenvalue of a helical null-curve stability condition — a geometric fixed point, not a free parameter" [10]. Its meta-principle claims that a flat continuous projection conceals a discrete, phase-structured substrate, and that the act of choosing a representation determines which invariants are visible and which problems appear unsolved [10]. We take [10]'s P2 claim as the hypothesis under test in Sections 4.4 and 6; notably, [10] states the hypothesis but its excerpted text gives no stability calculation, so the eigenvalue claim remains, on the evidence available, a conjecture rather than a derivation.

## 3. Methods

### 3.1 The number-to-phase-space map

Let $\mathcal{F} = \{ \dot{x} = f_{\lambda}(x) \}_{\lambda \in \mathbb{R}}$ be a one-parameter family of dynamical systems on a state space $M$, with $x \in M$. Define the *phase portrait map*

$$
\Phi : \mathbb{R} \to \mathcal{P}(M), \qquad \lambda \mapsto \Phi(\lambda) = \text{topological equivalence class of the flow } f_{\lambda},
$$

where $\mathcal{P}(M)$ denotes the set of topological equivalence classes of flows on $M$. The conjecture's "non-uniform number line" is then the statement that $\Phi$ is a *step function with finitely or countably many discontinuities* on any compact interval: for $\lambda$ in an open interval between consecutive bifurcation values, $\Phi(\lambda)$ is constant, while at a bifurcation value $\lambda_{c}$, $\Phi$ jumps. We call such a $\lambda_{c}$ a *bifurcation marker*. The uniformity of the number line as a *metric* object is irrelevant to the physics; what matters is the partition induced by $\Phi$.

Two methodological commitments follow. First, the numerical value of $\lambda_{c}$ is meaningful only after a normalization of $\lambda$ is fixed; a re-parameterization $\lambda' = g(\lambda)$ with monotone $g$ moves $\lambda_{c}$ to $g(\lambda_{c})$ without changing the physics. Any claim that a critical value "is" a specific number must therefore be relativized to a canonical normalization — typically one in which the dimensional constants of the system are absorbed into $\lambda$. Second, the physically meaningful statement is about the *existence* of a jump in $\Phi$, not the arithmetic proximity of $\lambda_{c}$ to a "nice" number. This is the same distinction that [4] makes in invariant language: what changes at the Hamiltonian Hopf bifurcation is the position of eigenvalues relative to the unit circle, an invariant statement, not the numeral attached to the parameter.

We additionally define a logarithmic regime measure

$$
\mu_{\log}(a, b) = \left| \ln \frac{b}{a} \right|,
$$

so that multiplicative rather than additive proximity is the natural metric near thresholds — consistent with the non-uniform sampling philosophy of [6], where sampling density is allocated by local structure rather than uniformly.

### 3.2 Case study A: the simple pendulum

The simple pendulum of mass $m$, length $L$, under gravity $g$, has energy

$$
E = \frac{1}{2} m L^{2} \dot{\theta}^{2} + m g L (1 - \cos\theta).
$$

Its phase portrait is exactly solvable, providing a closed-form bifurcation marker between libration and rotation. The derivation is given in Section 4.1.

### 3.3 Case study B: double pendulum flip threshold

We use the idealized planar double pendulum: two point masses $m$, both equal, on two massless rods of length $l$, both equal, in uniform gravity $g$, with angles $\theta_{1}, \theta_{2}$ measured from the downward vertical. The bob heights are

$$
h_{1} = -l\cos\theta_{1}, \qquad h_{2} = -l\cos\theta_{1} - l\cos\theta_{2},
$$

so the potential energy (zero at the pivot) is

$$
V(\theta_{1},\theta_{2}) = -mgl\bigl(2\cos\theta_{1} + \cos\theta_{2}\bigr).
$$

A "flip" is a trajectory in which the upper bob passes over the pivot, i.e., $\theta_{1}$ reaches $\pi$. We launch from rest at initial angles $(\theta_{1}^{(0)}, \theta_{2}^{(0)})$, so the conserved energy equals the initial potential energy. The derivation is given in Section 4.2.

### 3.4 Case study C: fall-to-center threshold with a $1/r^{2}$ correction

To model the conjecture's "helical self-interacting particle," we use the minimal central-force problem with potential

$$
V(r) = -\frac{A}{r} + \frac{B}{r^{2}}, \qquad A > 0,
$$

where $B$ plays the role of a self-interaction (or angular-momentum-like) coupling. Radial motion with angular momentum $L$ has effective potential

$$
U_{\text{eff}}(r) = \frac{L^{2}}{2mr^{2}} - \frac{A}{r} + \frac{B}{r^{2}} = \frac{L^{2} + 2mB}{2mr^{2}} - \frac{A}{r}.
$$

The sign of the coefficient $L^{2} + 2mB$ determines whether the effective potential is repulsive at small $r$ (bounded orbits possible) or attractive (fall to center). The derivation is given in Section 4.3. This model is a deliberate minimalization: [10] hypothesizes a helical null-curve stability condition with $\alpha$ as a critical eigenvalue, but supplies no equations for it, so we test the conjecture's *scale* claim — that a self-interaction threshold could plausibly sit at $\alpha$ — on the simplest model that has such a threshold at all.

### 3.5 Epistemic labeling

Every quantitative statement carries one of three labels: **[D]** derived with shown arithmetic; **[P]** projection, with stated assumptions and uncertainty bounds; **[H]** hypothesis, explicitly not established here.

## 4. Analysis

### 4.1 Simple pendulum separatrix [D]

**Inputs.** Mass $m$, length $L$, gravity $g$ (Section 3.2); energy zero at the hanging equilibrium.

**Step 1: separatrix energy.** The minimum energy is $E_{\min} = 0$ at $\theta = 0$, $\dot{\theta} = 0$. The separatrix — the orbit asymptotic to the unstable equilibrium at $\theta = \pi$ — has energy

$$
E_{\text{sep}} = m g L (1 - \cos\pi) = m g L (1 - (-1)) = 2 m g L.
$$

**Step 2: normalization.** Define the normalized energy $\varepsilon = E / (m g L)$. Then

$$
\varepsilon_{\text{sep}} = \frac{2 m g L}{m g L} = 2.
$$

For $\varepsilon < 2$ all orbits are librations; for $\varepsilon > 2$ all orbits are rotations. The bifurcation marker is the integer $2$ in this normalization. Note immediately that choosing $\tilde{\varepsilon} = E/(2mgL)$ moves the marker to $\tilde{\varepsilon}_{\text{sep}} = 1$: the numeral is a normalization artifact, while the jump in $\Phi$ is not.

### 4.2 Double pendulum: derivation of the flip threshold [D]

**Inputs.** Equal masses $m$, equal lengths $l$, gravity $g$ (Section 3.3); launch from rest, so $E = V(\theta_{1}^{(0)},\theta_{2}^{(0)})$.

**Step 1: energy at the flip configuration.** A flip requires the energy surface to reach some configuration with $\theta_{1} = \pi$. At $\theta_{1} = \pi$, $\cos\theta_{1} = -1$, so

$$
V(\pi, \theta_{2}) = -mgl\bigl(2(-1) + \cos\theta_{2}\bigr) = mgl\bigl(2 - \cos\theta_{2}\bigr).
$$

**Step 2: minimize over $\theta_{2}$.** Since $\cos\theta_{2} \in [-1, 1]$, the minimum of $2 - \cos\theta_{2}$ is attained at $\cos\theta_{2} = 1$, i.e., $\theta_{2} = 0$:

$$
E_{c} = \min_{\theta_{2}} V(\pi, \theta_{2}) = mgl(2 - 1) = mgl.
$$

**Step 3: reference energy of the hanging state.** At the fully hanging rest state $(\theta_{1},\theta_{2}) = (0,0)$:

$$
V(0,0) = -mgl(2\cdot 1 + 1) = -3\,mgl.
$$

Launching from rest at $(0,0)$ gives $E = -3mgl$, and energy is conserved. The flip condition is that the conserved energy reach the minimum energy of the set $\{\theta_{1} = \pi\}$, which is $E_{c} = +mgl$. The required *excess* energy above the hanging state is therefore

$$
\Delta E = E_{c} - V(0,0) = mgl - (-3mgl) = 4\,mgl.
$$

**Step 4: normalization.** Define the dimensionless excess energy $\varepsilon \equiv \Delta E/(4\,mgl)$. Then the flip threshold is exactly

$$
\varepsilon_{c} = \frac{4\,mgl}{4\,mgl} = 1.
$$

Equivalently, normalizing by the well depth $|V(0,0)| = 3mgl$ gives $\Delta E/|V(0,0)| = 4mgl/3mgl = 4/3 \approx 1.333\ldots$; normalizing by $mgl$ with the zero of energy at the hanging state gives $E/(mgl) = 4$. The critical value is $1$, $4/3$, or $4$ depending on convention — the physics (a jump in $\Phi$) is identical in all three.

**Interpretation.** The conjecture's example — the integer $1$ at the flip threshold — is correct *under the normalization* $\varepsilon = \Delta E/(4mgl)$, which is the normalization in which the threshold coincides with the energy of the "upper bob over pivot, lower bob hanging" configuration. The value $1$ is not discovered in nature; it is produced by dividing the threshold by itself. What is physical is the existence of the jump in $\Phi$ at that configuration, not the numeral.

### 4.3 Central-force model: derivation of the fall-to-center threshold [D]

**Inputs.** $V(r) = -A/r + B/r^{2}$ with $A > 0$; angular momentum $L$; mass $m$ (Section 3.4).

**Step 1: small-$r$ behavior.** As $r \to 0$, the $r^{-2}$ term dominates the $r^{-1}$ term. The coefficient of $r^{-2}$ in $U_{\text{eff}}$ is $(L^{2} + 2mB)/(2m)$.

- If $L^{2} + 2mB > 0$, then $U_{\text{eff}} \to +\infty$ as $r \to 0$: an impenetrable barrier exists, and bounded orbits can exist.
- If $L^{2} + 2mB < 0$, then $U_{\text{eff}} \to -\infty$ as $r \to 0$: the particle spirals into the center for generic inward motion — a qualitatively different regime.

**Step 2: critical coupling.** The boundary between regimes is

$$
L^{2} + 2mB_{c} = 0 \quad \Longrightarrow \quad B_{c} = -\frac{L^{2}}{2m}.
$$

Define the dimensionless coupling $\beta \equiv 2mB/L^{2}$. Then the threshold is

$$
\beta_{c} = \frac{2mB_{c}}{L^{2}} = \frac{2m \cdot (-L^{2}/2m)}{L^{2}} = \frac{-L^{2}}{L^{2}} = -1.
$$

With the sign convention $B > 0$ (repulsive short-distance core), bounded orbits exist for all $\beta > -1$, and the regime boundary sits at $\beta = -1$. If instead one defines $\tilde{\beta} = -\beta$ for an attractive correction $B < 0$, the threshold sits at $\tilde{\beta}_{c} = 1$. Again the numeral $1$ (or $-1$) is a normalization artifact; the physics is the sign change of $L^{2} + 2mB$.

**Step 3: existence of a circular orbit.** For $L^{2} + 2mB > 0$, $U_{\text{eff}}$ has a stationary point where

$$
\frac{dU_{\text{eff}}}{dr} = -\frac{L^{2} + 2mB}{mr^{3}} + \frac{A}{r^{2}} = 0
\quad \Longrightarrow \quad
r_{\min} = \frac{L^{2} + 2mB}{mA}.
$$

Since $U_{\text{eff}} \to +\infty$ as $r \to 0$ and as $r \to \infty$, this stationary point is a minimum, with value

$$
U_{\text{eff}}(r_{\min}) = \frac{L^{2}+2mB}{2m}\cdot\frac{m^{2}A^{2}}{(L^{2}+2mB)^{2}} - \frac{mA}{L^{2}+2mB}
= -\frac{mA^{2}}{2(L^{2}+2mB)}.
$$

Bound (negative-energy) orbits exist around this minimum whenever $E < 0$; the regime boundary at $\beta = -1$, not the bound/unbound energy sign, is the topological event.

### 4.4 The fine-structure constant scale [D on the constant; H on its dynamical role]

**Input.** We take the conjecture's stated value $\alpha \approx 1/137$ [10].

**Computation.** Long division gives $1/137 = 0.00729927\ldots$; check: $137 \times 0.00729927 = 0.99999999$, confirming the reciprocal to the stated precision. Thus

$$
\alpha \approx \frac{1}{137} = 7.29927 \times 10^{-3}.
$$

**Comparison with thresholds.** The thresholds derived above sit at $|\beta_{c}| = 1$ in their natural dimensionless variables. The separation between an $\alpha$-scale coupling and an order-unity threshold is

$$
\frac{1}{\alpha} \approx 137, \qquad \log_{10}\!\left(\frac{1}{\alpha}\right) \approx 2.14,
$$

since $10^{2} = 100 < 137 < 1000 = 10^{3}$ and $\log_{10}(137) = \log_{10}(1.37) + 2 \approx 0.1367 + 2 = 2.1367$. An $\alpha$-scale coupling is therefore about $2.14$ orders of magnitude below the natural threshold value $1$ in the minimal model of Section 4.3. For $\alpha$ itself to be a bifurcation coupling, the model would need a threshold at $\beta_{c} = \alpha$, i.e., a mechanism shifting the critical value by a factor of $\approx 137$ from the naive one — for example a coupling entering as $\beta_{\text{eff}} = \beta/\alpha$ with an additional small parameter. We state this as an explicit requirement, not a finding: no such mechanism is constructed here, and [10]'s statement of the helical null-curve stability condition does not include the calculation that would produce one. The claim that $\alpha$ marks a bifurcation between bound helical and unbound motion in a Zitterbewegung-type model is **[H]**: the source conjecture asserts it; no derivation in this paper supports it; Section 6 defines the falsification conditions.

### 4.5 Combinatorial projection for many coupled subsystems [P]

**Labeled projection, with assumptions.** Reference [3] reports an experimental network of approximately 100 convective oscillators — its stationary pattern corresponds to an array of 95 latent oscillators [3] — undergoing a secondary subcritical bifurcation. Assume (i) $N = 100$ subsystems each subject to the same binary regime split at a shared critical value, (ii) subsystems are statistically independent so that all $2^{N}$ regime assignments are realizable, and (iii) no additional constraints reduce the count. Then the configuration space has size

$$
|\mathcal{C}| = 2^{N} = 2^{100}.
$$

To evaluate $2^{100}$, use $2^{10} = 1024 = 1.024 \times 10