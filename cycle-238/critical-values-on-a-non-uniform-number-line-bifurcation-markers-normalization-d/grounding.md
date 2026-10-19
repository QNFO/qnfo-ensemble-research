# Grounding block - source: rem-3f9c61f3-63c7-42f5-a99b-3a06d5e2d716

## Research idea

Physical constants as bifurcation parameters on a non-uniform number line. The author conjectures that the real number line is a misleading projection of physical state spaces: intervals between numbers are not uniform, and certain values (like the integer 1 for the double pendulum's flip threshold) act as topological phase boundaries rather than smooth increments. He speculates that fundamental constants such as the fine-structure constant α ≈ 1/137 may similarly mark bifurcation points separating qualitatively different dynamical regimes (e.g., bound helical vs. unbound motion in a Zitterbewegung-type model). A paper could test this by (1) formalizing a 'number-to-phase-space' map for canonical systems (pendula, coupled oscillators) and characterizing how accessible topology changes across critical parameter values; (2) simulating a helical self-interacting particle model to check whether α-like ratios emerge as stability thresholds between distinct motion regimes; and (3) deriving whether such bifurcation structure explains why constants appear 'special' rather than arbitrary decimals.

Source: owner notebook notes/v1/2026/07/18/_26199084040.md

## Existing paper under revision (remediation only)

# Critical Values on a Non-Uniform Number Line: Bifurcation Markers, Normalization Dependence, and the Conjectured Specialness of Physical Constants

## Abstract

We examine the conjecture that the real number line, as a model of physical state space, is misleadingly uniform: that certain parameter values act as topological phase boundaries rather than smooth increments, and that fundamental constants such as the fine-structure constant $\alpha \approx 1/137$ may mark bifurcation points between qualitatively different dynamical regimes. We formalize a number-to-phase-space map $\Phi$ that assigns to each parameter value the topological equivalence class of the associated dynamics, making precise in what sense a parameter value can be a "boundary." We work two canonical examples in full arithmetic: the simple pendulum, whose separatrix sits at normalized energy $\varepsilon = 2$ exactly, and a central-force problem with a $1/r^{2}$ correction, whose fall-to-center threshold sits at dimensionless coupling $\beta = -1$ exactly. Both thresholds land on small integers only because normalization conventions absorb dimensional constants into the critical value; the same physics yields $1$, $4/3$, or $4$ under different normalizations of the double-pendulum flip energy. We compute $\alpha \approx 7.29927 \times 10^{-3}$ from the supplied value $1/137$, show it lies roughly $2.14$ orders of magnitude below the order-unity thresholds of our minimal models, and state the fine-structure constant's conjectured dynamical role as an explicitly labeled hypothesis with falsification conditions. A combinatorial projection for $N \approx 100$ coupled subsystems sharing one threshold yields a configuration space of order $10^{30}$. We argue that the "specialness" of constants is better explained as normalization artifact plus generic bifurcation structure, unless additional model-building succeeds.

## 1. Introduction

Physics pedagogy and practice overwhelmingly treat the real numbers as a uniform stage: the interval between $1.0$ and $1.1$ is, by assumption of the formalism, "the same kind" of interval as that between $2.0$ and $2.1$. Working dynamical intuition contradicts this. In pendulum systems, crossing a single normalized energy value changes the qualitative character of all future motion; on either side of that value, infinitesimally nearby parameter points belong to dynamically distinct worlds.

The source conjecture motivating this paper holds that (i) the real number line is a misleading projection of physical state spaces, whose intervals are not uniformly meaningful; (ii) certain values — the conjecture's example is the integer $1$ at the double pendulum's flip threshold under a suitable normalization — act as topological phase boundaries, where the accessible topology of motion changes qualitatively rather than smoothly; and (iii) fundamental constants such as the fine-structure constant $\alpha \approx 1/137$ (as supplied in the grounding material) may similarly mark bifurcation points separating qualitatively different regimes, for example bound helical versus unbound motion in a Zitterbewegung-type self-interacting particle model.

This paper tests the internal logic of that conjecture rather than asserting or dismissing it. We do four things. First, we formalize a number-to-phase-space map: given a family of dynamical systems indexed by a parameter $\lambda$, we characterize how the qualitative structure of solutions changes across critical values $\lambda_{c}$, and we show how the numerical value of $\lambda_{c}$ depends on normalization. Second, we carry out explicit derivations for the simple pendulum separatrix, the double pendulum flip threshold, and the fall-to-center threshold of a corrected central-force problem, showing that each yields a small-integer critical value under the normalizations the conjecture implicitly uses, and explaining arithmetically why this is so. Third, we compute the fine-structure constant from its supplied value and ask whether an $\alpha$-scale coupling could sit at the threshold of a minimal helical self-interacting particle model; we find that it cannot without fine-tuning, since the derived threshold is at order unity while $\alpha \approx 7.29927 \times 10^{-3}$, a separation of roughly two orders of magnitude. Fourth, we quantify the combinatorial richness that a single shared threshold generates across many coupled subsystems, as a labeled projection.

Our conclusion is deliberately two-sided. The conjecture is correct that parameter space is not phenomenologically uniform: bifurcation values genuinely partition it into regimes with different accessible topology, a fact documented in the bifurcation literature we review. But the further step — that the specific numerical values of fundamental constants are therefore explained as bifurcation points — does not follow, because the numerical value of a dimensionless critical parameter is convention-dependent once normalization is fixed, and because the constants we examine do not sit at the thresholds of the minimal models built to test the idea. We state the conditions under which this negative conclusion would be overturned.

## 2. Background and Related Work

We discuss all twelve supplied works. Entries [9]–[12] carry only titles and identifiers, and we say so explicitly rather than attributing content to them.

**Bifurcation phenomenology as the physics of non-uniform parameter space.** Reference [3] (arXiv:1103.1495v1) presents experimental results on quenching dynamics in an extended thermo-convective system — a network array of approximately $100$ convective oscillators — going through a secondary subcritical bifurcation, and characterizes the resulting dynamical phase transition through the nature of the one-dimensional domain-wall fronts connecting a basic multicellular pattern with a new oscillating one. This is directly relevant to our argument: it is an experimental demonstration that a control parameter's crossing of a critical value changes the *topology* of the accessible pattern space (new domains, new walls between domains), not merely the values of observables. It also supplies the concrete subsystem count $N \approx 100$ used in our combinatorial projection of Section 4.5.

Reference [4] (arXiv:1012.2463v2) studies orbital behavior near complex unstable periodic orbits in a three-dimensional autonomous Hamiltonian system of galactic type, showing that at a Hamiltonian Hopf bifurcation the four eigenvalues of stable periodic orbits move off the unit circle and the orbits become complex unstable. This supplies a precise, eigenvalue-level mechanism by which a smooth change of a parameter produces a qualitative regime change — exactly the "phase boundary on the number line" phenomenon the conjecture gestures at.

Reference [5] (arXiv:1512.00707v1) reviews bifurcation sequences of periodic orbits in resonant Hamiltonian normal forms with nearly equal unperturbed frequencies, invariant under $\mathbb{Z}_{2} \times \mathbb{Z}_{2}$ symmetry, investigated with geometric methods and connected to singularity theory. It shows that near a single resonance, parameter space is organized into an entire *sequence* of bifurcations, not one boundary — reinforcing our point that critical values are dense, structured features of families, not isolated magic numbers.

**Non-uniformity of representation.** Reference [6] (arXiv:1701.07110v1) addresses visualization of large datasets, noting that almost every visual technique reveals drawbacks at scale, and introduces a formal environment modeling image features such as absolute and relative density in a virtual space, using non-uniform sampling to preserve relative density. The supplied summary gives no further detail, but its core move is directly analogous to ours: a uniform grid over a domain misrepresents the domain's structure, and a non-uniform re-parameterization preserves features (there, density; here, bifurcation topology) that uniform treatment destroys. We use it as the closest methodological precedent for a "non-uniform number line" in the supplied literature.

**Threshold-based decision structure.** References [1] and [2] come from power-infrastructure risk, and we cite them for their structural analogy, not their subject matter. Reference [1] (arXiv:2110.07348v3) frames wildfire-ignition mitigation from power line faults as a prioritization problem: long-term strategies such as converting overhead lines to underground cables are expensive, so upgrades must be targeted at lines that reduce ignition risk the most; the supplied summary is truncated at this prioritization principle and gives no further methodological detail. Reference [2] (arXiv:2204.02507v3) proposes a mathematical optimization problem for utilities to decide where and when to implement preemptive power shutoffs, which mitigate ignition risk but cause widespread outages, and how to co-optimize shutoffs with restoration. Both works embody the same logical form as a bifurcation threshold: a continuous risk landscape acted on by a discrete intervention that is worthwhile only above a critical value. They illustrate that "critical value" reasoning is a general decision-theoretic pattern, independent of any specialness of the critical number itself.

**Arithmetic perspectives on special numbers.** Reference [7] (arXiv:2309.12153v2) investigates the $a$-numbers of $\mathbb{Z}/p^{2}\mathbb{Z}$-covers of the projective line in characteristic $p > 2$, extending a technique of Farnell and Pries for $\mathbb{Z}/p\mathbb{Z}$-covers, and shows that the $a$-numbers of "minimal" $\mathbb{Z}/9\mathbb{Z}$-covers can be deduced from the associated branching datum. This is a case where an integer-valued invariant of a geometric object is *determined* by discrete arithmetic data — a rigorous instance of numbers being "special" for structural reasons.

Reference [8] (arXiv:2402.07935v3) proves, for a non-CM simple abelian variety $A$ over a number field $K$ with connected monodromy groups, that the set of places $v$ of good reduction for which the Frobenius field $F(A,v)$ is isomorphic to a fixed number field has upper Dirichlet density zero. This is a density-zero statement: in a precise arithmetic sense, most places are *not* special, and the exceptional set is thin. We use both works as contrasts: arithmetic structure can make specific numbers distinguished, but the distinguished sets are provably thin — a caution against reading every salient constant as a generic feature.

**The QNFO corpus.** References [9]–[12] are supplied as titles and DOIs only: [9] "QNFO: Time as Epistemic Cognitive Fiction" (https://papers.qnfo.org/papers/time-as-epistemic-cognitive-fiction/), [10] "QNFO: COMMUTATIVE PHYSICS", [11] "QNFO: The Continuum Critique Trilogy" (https://papers.qnfo.org/papers/continuum-critique-trilogy/), and [12] "QNFO: Invariant Structural Value: Fundamental Constants and Formulas as Invariant Relations" (https://papers.qnfo.org/papers/invariant-structural-value/). No summary text is supplied for any of them, so we cannot state what they argue. By their titles, [11] and [12] appear closest to the present conjecture — a critique of the continuum, and a treatment of constants as invariant structural relations — and we flag them as natural companion reading; but we make no claim about their content, since the supplied entries give none.

## 3. Methods

### 3.1 The number-to-phase-space map

Let $\mathcal{F} = \{ \dot{x} = f_{\lambda}(x) \}_{\lambda \in \mathbb{R}}$ be a one-parameter family of dynamical systems on a state space $M$, with $x \in M$. Define the *phase portrait map*

$$
\Phi : \mathbb{R} \to \mathcal{P}(M), \qquad \lambda \mapsto \Phi(\lambda) = \text{topological equivalence class of the flow } f_{\lambda},
$$

where $\mathcal{P}(M)$ denotes the set of topological equivalence classes of flows on $M$. The conjecture's "non-uniform number line" is then the statement that $\Phi$ is a *step function with finitely or countably many discontinuities* on any compact interval: for $\lambda$ in an open interval between consecutive bifurcation values, $\Phi(\lambda)$ is constant, while at a bifurcation value $\lambda_{c}$, $\Phi$ jumps. We call such a $\lambda_{c}$ a *bifurcation marker*. The uniformity of the number line as a *metric* object is irrelevant to the physics; what matters is the partition induced by $\Phi$.

Two methodological commitments follow. First, the numerical value of $\lambda_{c}$ is meaningful only after a normalization of $\lambda$ is fixed; a re-parameterization $\lambda' = g(\lambda)$ with monotone $g$ moves $\lambda_{c}$ to $g(\lambda_{c})$ without changing the physics. Any claim that a critical value "is" a specific number must therefore be relativized to a canonical normalization — typically one in which the dimensional constants of the system are absorbed into $\lambda$. Second, the physically meaningful statement is about the *existence* of a jump in $\Phi$, not the arithmetic proximity of $\lambda_{c}$ to a "nice" number.

We additionally define a logarithmic regime measure

$$
\mu_{\log}(a, b) = \left| \ln \frac{b}{a} \right|,
$$

so that multiplicative rather than additive proximity is the natural metric near thresholds — consistent with the non-uniform sampling philosophy of [6].

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

The sign of the coefficient $L^{2} + 2mB$ determines whether the effective potential is repulsive at small $r$ (bounded orbits possible) or attractive (fall to center). The derivation is given in Section 4.3.

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

**Input.** The grounding material supplies $\alpha \approx 1/137$.

**Computation.** Long division gives $1/137 = 0.00729927\ldots$; check: $137 \times 0.00729927 = 0.99999999$, confirming the reciprocal to the stated precision. Thus

$$
\alpha \approx \frac{1}{137} = 7.29927 \times 10^{-3}.
$$

**Comparison with thresholds.** The thresholds derived above sit at $|\beta_{c}| = 1$ in their natural dimensionless variables. The separation between an $\alpha$-scale coupling and an order-unity threshold is

$$
\frac{1}{\alpha} \approx 137, \qquad \log_{10}\!\left(\frac{1}{\alpha}\right) \approx 2.14,
$$

since $10^{2} = 100 < 137 < 1000 = 10^{3}$ and $\log_{10}(137) = \log_{10}(1.37) + 2 \approx 0.1367 + 2 = 2.1367$. An $\alpha$-scale coupling is therefore about $2.14$ orders of magnitude below the natural threshold value $1$ in the minimal model of Section 4.3. For $\alpha$ itself to be a bifurcation coupling, the model would need a threshold at $\beta_{c} = \alpha$, i.e., a mechanism shifting the critical value by a factor of $\approx 137$ from the naive one — for example a coupling entering as $\beta_{\text{eff}} = \beta/\alpha$ with an additional small parameter. We state this as an explicit requirement, not a finding: no such mechanism is constructed here. The claim that $\alpha$ marks a bifurcation between bound helical and unbound motion in a Zitterbewegung-type model is **[H]**: the source material conjectures it; no derivation or simulation in this paper supports it; Section 6 defines the falsification conditions.

### 4.5 Combinatorial projection for many coupled subsystems [P]

**Labeled projection, with assumptions.** Reference [3] reports an experimental network of approximately $100$ convective oscillators undergoing a secondary subcritical bifurcation. Assume (i) $N = 100$ subsystems each subject to the same binary regime split at a shared critical value, (ii) subsystems are statistically independent so that all $2^{N}$ regime assignments are realizable, and (iii) no additional constraints reduce the count. Then the configuration space has size

$$
|\mathcal{C}| = 2^{N} = 2^{100}.
$$

To evaluate $2^{100}$, use $2^{10} = 1024 = 1.024 \times 10^{3}$ and raise to the 10th power:

$$
2^{100} = (2^{10})^{10} = (1.024 \times 10^{3})^{10} = (1.024)^{10} \times 10^{30}.
$$

Using the binomial expansion $(1 + x)^{10} \approx 1 + 10x$ for $x = 0.024$: $(1.024)^{10} \approx 1.24 + \text{(higher-order terms)} \approx 1.27$. Hence

$$
|\mathcal{C}| \approx 1.27 \times 10^{30}.
$$

Uncertainty: the exact value $2^{100} = 1.2676506\ldots \times 10^{30}$ is exact arithmetic; the *physical* relevance is the uncertain part, since assumptions (i)–(iii) are idealizations — real oscillators may exhibit multi-branch behavior or correlations that reduce the effective count below $2^{N}$. This projection quantifies only how much combinatorial structure a single shared threshold *can* generate, not that it does in the experiment of [3].

### 4.6 Logarithmic measure of the pendulum's guarded regime [D]

Using the measure of Section 3.1, the logarithmic distance from the libration floor ($\varepsilon = 1$, the minimum in the shifted normalization) to the separatrix is

$$
\mu_{\log}(1, 2) = \ln\frac{2}{1} = \ln 2 \approx 0.693147,
$$

where $\ln 2 = 0.6931471805\ldots$. By contrast, the additive distance is $2 - 1 = 1$. The two measures disagree by a factor $1/0.693147 \approx 1.4427$, illustrating concretely that "how far" a parameter value is from a threshold depends on the measure chosen — the operational content of non-uniformity.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

**R1 [D] (simple pendulum).** The separatrix occurs at normalized energy $\varepsilon_{\text{sep}} = 2$ exactly, derived from $E_{\text{sep}} = 2mgL$ and $\varepsilon = E/(mgL)$ (Section 4.1). The integer $2$ is a bifurcation marker in the sense of Section 3.1: $\Phi$ is discontinuous there, separating libration from rotation.

**R2 [D] (double pendulum).** Under the idealized equal-mass, equal-length model launched from rest, the flip threshold is an excess energy $\Delta E = 4\,mgl$ above the hanging state (Section 4.2). In the normalization $\varepsilon = \Delta E/(4mgl)$, the critical value is exactly $\varepsilon_{c} = 1$; in the well-depth normalization it is $4/3 \approx 1.333$; in the $E/(mgl)$ normalization with zero at the hanging state it is $4$.

**R3 [D] (central-force model).** For $V(r) = -A/r + B/r^{2}$, the regime boundary between barrier-protected bounded motion and fall-to-center is at $\beta = 2mB/L^{2} = -1$, exactly (Section 4.3). Stable circular orbits exist at radius $r_{\min} = (L^{2} + 2mB)/(mA)$ for $\beta > -1$, with minimum effective potential $-mA^{2}/(2(L^{2}+2mB))$.

**R4 [D] ($\alpha$ scale).** From the supplied $\alpha \approx 1/137$, we compute $\alpha \approx 7.29927 \times 10^{-3}$ and $1/\alpha \approx 137$, i.e., $\log_{10}(1/\alpha) \approx 2.14$ (Section 4.4). An $\alpha$-scale coupling is $\approx 137$ times smaller than the order-unity thresholds of R1–R3 in their natural dimensionless variables.

**R5 [P] (combinatorial projection).** Under the assumptions of Section 4.5 ($N = 100$ independent binary subsystems sharing one threshold), $|\mathcal{C}| = 2^{100} \approx 1.27 \times 10^{30}$. This is a conditional projection, not an observed property of the experiment of [3].

**R6 [D] (logarithmic measure).** As an illustrative comparison on the interval $[1, 2]$ (not tied to a stated normalization), the logarithmic measure is $\mu_{\log}(1,2) = \ln 2 \approx 0.693147$, versus additive distance $1$; the measures differ by a factor $\approx 1.4427$ (Section 4.6).

**R7 [H] (hypothesis).** The conjecture that $\alpha$ functions as a bifurcation marker between bound helical and unbound motion in a helical self-interacting particle model is stated as a hypothesis, not a result. No number in this paper supports it beyond the value of $\alpha$ itself.

**R8 (structural).** The critical values in R1–R3 are normalization-dependent ($1$, $4/3$, $4$ for the same double-pendulum physics), while the existence and regime-structure of the jumps in $\Phi$ are normalization-independent. The physically defensible version of the "non-uniform number line" is the partition induced by $\Phi$, not the numeral.

## 6. Discussion

**Limitations.** The formalization of Section 3.1 is deliberately coarse: topological equivalence of phase portraits is a strong notion, and weaker (or stronger) notions of "same regime" would move the location of markers. The pendulum examples are the friendliest possible — low-dimensional, exactly solvable. The helical-particle model is specified only at the level of qualitative description; the supplied QNFO summaries contain no equations, so we could not and did not derive a threshold for it. The combinatorial projection of Section 4.5 assumes independence and binary regimes, both idealizations.

**What would falsify the program.** Three failure modes. (i) If, across a broad class of canonical systems, bifurcation markers under natural normalizations are *not* concentrated on small integers or simple rationals but are generically irrational and non-repeating, then "special values" reduce to convention and the non-uniformity thesis loses content. (ii) If a helical self-interacting model can be constructed whose bound/unbound threshold is continuously tunable away from $\alpha$ by changing innocuous model choices, then $\alpha$-as-marker is falsified for that model class. Conversely, our own analysis suggests the conjecture is in difficulty: the minimal central-force model places its threshold at $|\beta_{c}| = 1$, roughly $137$ times larger than $\alpha$, so the conjecture requires an additional mechanism shifting thresholds by two orders of magnitude — a requirement we state but cannot meet. (iii) If the logarithmic measure $\mu_{\log}$ fails to track any physical or informational quantity better than the additive measure does, the non-uniformity is purely formal.

**Against ourselves.** The strongest objection is that every integer threshold derived here is an artifact of normalization: choose $\tilde{\varepsilon} = E/(2mgL)$ and the pendulum marker becomes $1$; choose $\hat{\varepsilon} = E/(\pi m g L)$ and it becomes $2/\pi$. The conjecture's content therefore cannot be "the marker is an integer" but must be "a natural normalization exists in which the marker is structurally distinguished" — a much weaker claim, and one we can only illustrate, not prove. The analogy to [7] and [8] is structural, not derivational: those works show that arithmetic structure can make specific numbers distinguished while the distinguished sets remain provably thin, whereas our examples show that dynamical structure can make specific numerals distinguished while the numerals themselves remain provably conventional. A second objection is that our negative result about $\alpha$ is model-relative: we tested only a minimal central-force model, and a different model class could in principle place a threshold at $\beta_{c} = \alpha \approx 7.29927 \times 10^{-3}$. Our claim is therefore not that $\alpha$ cannot be a bifurcation marker, but that no mechanism producing such a threshold has been supplied, and the burden of construction lies with the conjecture's proponents. Third, the combinatorial projection of Section 4.5 assumes statistical independence of $N = 100$ subsystems; correlations, which are generic in spatially extended systems such as the network of [3], would reduce the effective configuration count below $2^{100} \approx 1.27 \times 10^{30}$, possibly by many orders of magnitude. Finally, the logarithmic measure $\mu_{\log}$ is introduced here as a definition, not derived from any operational protocol; its physical content is an open question.

**Open questions.** (a) Is there a normalization-independent characterization of "structurally distinguished" critical values, analogous to how rationality or algebraicity is normalization-independent for dimensionless ratios? (b) Can a self-interacting particle model be written down whose bound/unbound threshold is a derived function of $\alpha$, rather than an assumed one? (c) What is the effective, correlation-corrected configuration count for the network experiment of [3]? These questions are stated, not answered, in this paper.

## 7. Conclusion

We formalized the conjecture that the real number line is a misleadingly uniform model of physical parameter space by introducing the phase-portrait map $\Phi$, which partitions parameter values into regimes and whose discontinuities are bifurcation markers. Working three canonical examples in full arithmetic, we found that the simple pendulum separatrix sits at $\varepsilon_{\text{sep}} = 2$ in one natural normalization and $1$ in another; that the double pendulum flip threshold is $\Delta E = 4\,mgl$ above the hanging state, yielding critical values $1$, $4/3$, or $4$ under three conventions; and that the fall-to-center threshold of a corrected central-force problem sits at $\beta = 2mB/L^{2} = -1$ exactly. In every case the small-integer numeral is a normalization artifact — produced, in the extreme case, by dividing the threshold by itself — while the existence of the jump in $\Phi$ is convention-independent and physically real.

Applying this lens to the fine-structure constant, computed from the supplied value as $\alpha \approx 1/137 = 7.29927 \times 10^{-3}$, we found that an $\alpha$-scale coupling lies a factor of $\approx 137$, i.e., $\log_{10}(1/\alpha) \approx 2.14$ orders of magnitude, below the order-unity thresholds of the minimal models. The conjecture that $\alpha$ marks a bifurcation between bound helical and unbound motion therefore requires an additional mechanism shifting thresholds by roughly two orders of magnitude; we stated this requirement explicitly as a hypothesis with falsification conditions and did not construct such a mechanism. A labeled projection for $N = 100$ independent binary subsystems sharing one threshold gave a configuration space of order $2^{100} \approx 1.27 \times 10^{30}$, quantifying how much combinatorial structure a single shared threshold can generate.

Our two-sided conclusion stands. Parameter space is genuinely non-uniform in the operational sense that $\Phi$ partitions it into qualitatively distinct regimes separated by markers; but the specific numerals at those markers are conventions, and the fundamental constants examined do not sit at the thresholds of the minimal models built to test the idea. The "specialness" of constants such as $\alpha$ is better explained as normalization artifact plus generic bifurcation structure, unless a model is produced whose derived threshold equals $\alpha$.

## References

[1] A Framework for Risk Assessment and Optimal Line Upgrade Selection to Mitigate Wildfire Risk. arXiv:2110.07348v3. https://arxiv.org/abs/2110.07348v3
[2] Co-optimization of power line shutoff and restoration under high wildfire ignition risk. arXiv:2204.02507v3. https://arxiv.org/abs/2204.02507v3
[3] Exploring the Kibble-Zurek mechanism in a secondary bifurcation. arXiv:1103.1495v1. https://arxiv.org/abs/1103.1495v1
[4] The structure and evolution of confined tori near a Hamiltonian Hopf Bifurcation. arXiv:1012.2463v2. https://arxiv.org/abs/1012.2463v2
[5] Bifurcation sequences in the symmetric 1:1 Hamiltonian resonance. arXiv:1512.00707v1. https://arxiv.org/abs/1512.00707v1
[6] By chance is not enough: Preserving relative density through non uniform sampling. arXiv:1701.07110v1. https://arxiv.org/abs/1701.07110v1
[7] $a$-Numbers of Cyclic Degree $p^2$ Covers of the Projective Line. arXiv:2309.12153v2. https://arxiv.org/abs/2309.12153v2
[8] On the Frobenius fields of abelian varieties over number fields. arXiv:2402.07935v3. https://arxiv.org/abs/2402.07935v3
[9] https://papers.qnfo.org/papers/time-as-epistemic-cognitive-fiction/. QNFO: Time as Epistemic Cognitive Fiction.
[10] QNFO: COMMUTATIVE PHYSICS
[11] https://papers.qnfo.org/papers/continuum-critique-trilogy/. QNFO: The Continuum Critique Trilogy.
[12] https://papers.qnfo.org/papers/invariant-structural-value/. QNFO: Invariant Structural Value: Fundamental Constants and Formulas as Invariant Relations.

## Appendix A. Divergence report

The reconciled drafts agreed on all substantive claims: the pendulum separatrix value $\varepsilon_{\text{sep}} = 2$, the double-pendulum excess energy $\Delta E = 4\,mgl$ with convention-dependent critical values $1$, $4/3$, $4$, the central-force threshold $\beta_{c} = -1$, the computation $\alpha \approx 7.29927 \times 10^{-3}$ from the supplied $1/137$, the separation $\log_{10}(1/\alpha) \approx 2.14$, and the projection $2^{100} \approx 1.27 \times 10^{30}$. No conflicting conventions or assumptions between drafts required resolution, so no divergences are reported. One presentational choice is documented for completeness: drafts differed in whether the hypothesis that $\alpha$ functions as a bifurcation marker should appear in the Results section; the reconciled text includes it as R7 with the explicit **[H]** label, keeping derived and hypothesized claims separated.

## Appendix B. Claim attribution

| Claim | Substance | Source drafts | Status |
|---|---|---|---|
| C1 | Phase-portrait map $\Phi$ formalizes bifurcation markers; marker numerals are normalization-dependent | A, B, C | CONVERGENT |
| C2 | Simple pendulum separatrix at $\varepsilon_{\text{sep}} = 2$; alternative normalization gives $1$ | A, B, C | CONVERGENT |
| C3 | Double pendulum flip threshold $\Delta E = 4\,mgl$; critical values $1$, $4/3$, $4$ by convention | A, B, C | CONVERGENT |
| C4 | Central-force fall-to-center threshold at $\beta = 2mB/L^{2} = -1$; circular orbit at $r_{\min} = (L^{2}+2mB)/(mA)$ | A, B, C | CONVERGENT |
| C5 | $\alpha \approx 1/137 = 7.29927 \times 10^{-3}$; $\log_{10}(1/\alpha) \approx 2.14$ below order-unity thresholds | A, B, C | CONVERGENT |
| C6 | $\alpha$-as-bifurcation-marker is a labeled hypothesis with falsification conditions, not a result | A, B, C | CONVERGENT |
| C7 | Combinatorial projection $2^{100} \approx 1.27 \times 10^{30}$ for $N = 100$ independent binary subsystems, motivated by the network of [3] | A, B, C | CONVERGENT |
| C8 | Logarithmic regime measure $\mu_{\log}(1,2) = \ln 2 \approx 0.693147$ versus additive distance $1$ | A, B | CONVERGENT (C silent) |
| C9 | Literature synthesis: [3], [4], [5] as bifurcation phenomenology; [6] as non-uniform sampling analogy; [1], [2] as threshold decision structure; [7], [8] as thin distinguished sets; [9]–[12] title-only | A, B, C | CONVERGENT |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2110.07348v3 | A Framework for Risk Assessment and Optimal Line Upgrade Selection to Mitigate Wildfire Risk
arXiv:2204.02507v3 | Co-optimization of power line shutoff and restoration under high wildfire ignition risk
arXiv:1103.1495v1 | Exploring the Kibble-Zurek mechanism in a secondary bifurcation
arXiv:1012.2463v2 | The structure and evolution of confined tori near a Hamiltonian Hopf Bifurcation
arXiv:1512.00707v1 | Bifurcation sequences in the symmetric 1:1 Hamiltonian resonance
arXiv:1701.07110v1 | By chance is not enough: Preserving relative density through non uniform sampling
arXiv:2309.12153v2 | $a$-Numbers of Cyclic Degree $p^2$ Covers of the Projective Line
arXiv:2402.07935v3 | On the Frobenius fields of abelian varieties over number fields

## QNFO corpus context (Vectorize)

QNFO: Critical Values on a Non-Uniform Number Line: Bifurcation Markers, Normalization Dependence, and the Conjectured Specialness of Physical Constants | https://papers.qnfo.org/papers/critical-values-on-a-non-uniform-number-line-bifurcation-markers-normalization-d
QNFO: The Continuum Critique Trilogy | https://papers.qnfo.org/papers/continuum-critique-trilogy

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2110.07348v3 | A Framework for Risk Assessment and Optimal Line Upgrade Selection to Mitigate Wildfire Risk
  As wildfires in the United States are becoming more frequent and severe, mitigating wildfire ignition risk from power line faults is an increasingly crucial effort. Long-term ignition prevention strategies, especially converting overhead lines to underground cables, are expensive. Thus, it is important to prioritize upgrades on lines that will reduce wildfire ignition risk the most. However, since
  Full text (https://arxiv.org/html/2110.07348v3), excerpts of its own sections:
  § I Introduction: In the United States, the total area burned by wildfires, wildfire frequency, and federal fire suppression costs per year have increased significantly since 1985 [ 1 ] . Wildfire prevention is an increasingly crucial effort, especially as climate change exacerbates future fire risk conditions [ 2 ] . Power line faults are one of the major sources of wildfire ignitions [ 3 ] . Downed lines, vegetation contact, conductor slap, or component failures can produce fault currents and sparks that may ignite fires under hot, dry, and windy conditions [ 4 , 5 ] . The deadliest and most destructive wildfire in California’s history, the 2018 Camp Fire, was ignited by an aging transmission line [ 6 ] . A particular challenge of ignitions from electric power lines is that a common factor – high wind speeds – increases both the probability of ignitions due to electric faults and promotes a rapid spread of the resulting fire. As a result, wildfires ignited by power lines tend to be larger than fires from other causes [ 7 ] . [...]
  § II Identifying the Optimal Set of Power Lines for Undergrounding: In this section, we present a simple optimization-based method to demonstrate how data on wildfire risk can be used to support decisions regarding which power lines should be prioritized for undergrounding in a region with significant wildfire risk. We consider a power system with $N$ overhead power lines. In most cases, a utility likely would not underground the entire length of a long transmission line due to high cost. Therefore, we split the lines up into line segments represented by the set $\mathcal{L}$ . Note that the number of line segments $N_{L}=|\mathcal{L}|\geq N$ . For each line segment $l\in\mathcal{L}$ , we define the associated wildfire risk as $R_{l}$ and the cost of undergrounding by $C_{l}$ . Further, we define a binary decision variable $z_{l}$ which represents whether line segment $l$ is undergrounded ( $z_{l}=1$ ) or not ( $z_{l}=0$ ). [...]
  § V Test Case Results: The proposed risk assignment and upgrade selection methods are demonstrated through several test cases. First, a simple example using the CCC problem variant is presented. This is then expanded to show the effect of using different line segment lengths in the problem. Next, the performance of the CCC problem is compared with the MMM problem, along with the tradeoff between the two. Finally, an example that weighs risk values based on line voltage is presented to demonstrate how grid-specific data can be incorporated to quantify the relative probability of electric fault.
  § VI Conclusion: The main contributions of this paper are a framework for assessing the wildfire ignition risk associated with power lines and an optimization model that selects lines for undergrounding such that wildfire risk is minimized. In particular, we discuss two different metrics for wildfire risk, and assess how the choice of risk metric impacts the optimal undergrounding decisions. This method is simpler than gathering and synthesizing data from multiple sources to estimate the risk of ignition associated with power lines, which is advantageous when such data is complex or not publicly available. Further, the proposed method is flexible, and can incorporate grid- and component-specific information on the probability of ignition if such information is available. One limitation of this work is that the WFPI indicates historical wildfire potential, not future potential. Due to climate change and human activity, historical risk may not be representative of future fire conditions. [...]
[2] arXiv:2204.02507v3 | Co-optimization of power line shutoff and restoration under high wildfire ignition risk
  Electric power infrastructure has ignited several of the most destructive wildfires in recent history. Preemptive power shutoffs are an effective tool to mitigate the risk of ignitions from power lines, but at the same time can cause widespread power outages. This work proposes a mathematical optimization problem to help utilities decide where and when to implement these shutoffs, as well as how t
  Full text (https://arxiv.org/html/2204.02507v3), excerpts of its own sections:
  § I INTRODUCTION: Wildfire ignitions caused by electrical equipment are an increasing concern for power grid operators. In Australia, electrical infrastructure accounts for 30% of bushfire ignitions during droughts and heat-waves  [ 1 ] . The state firefighting organization in California reports that between 2015-2020, wildfires ignited by electrical equipment were responsible for more than 70% of damages ($17.5 billion) despite accounting for only 10% of ignitions [ 2 ] . Given these insights, focus on wildfire-grid interactions has expanded from almost exclusively considering how the grid is impacted by fires (discussed in e.g. [ 3 , 4 , 5 , 6 , 7 ] ) to also consider how to reduce the risk of wildfire ignitions. Refs. [ 8 , 9 , 10 , 11 ] review approaches to reduce the risk of ignitions, many of which are already being implemented or planned by utilities. [...]
  § II Modeling and Problem Formulation: In this section, we formulate the Multi-period Optimal Power Shutoff And Restoration (MOPSAR) problem that provides an optimized schedule for both power line shutoffs and restoration. It is solved daily in a rolling horizon framework as new risk forecast data is made available each day.
  § II-A Rolling Horizon Formulation: We consider a power grid with a set of buses $\mathcal{B}$ , lines $\mathcal{L}$ , generators $\mathcal{G}$ and loads $\mathcal{D}$ . This grid has elevated wildfire risk, and the operator is planning a public safety power shutoff to mitigate the wildfire threat. The operator must make decisions on the power lines they may shutdown, customers they may disconnect, and how to re-energize the grid. Their goal is to reduce wildfire risk while minimizing the size and duration of customer power outages and maintaining grid reliability. Wildfire risk depends on ambient conditions such as vegetation cover, humidity and wind speed. The Wildland Fire Potential Index (WFPI) [ 28 ] provides wildfire risk data for the contiguous United States, is released daily and includes current data along with 7-day forecasts. Because it takes time to restore a power line after it has been shut off, we need to take the forecasted risk into account when deciding on an optimal schedule for power shutoffs and restoration. [...]
  § II-B Objective function: The system operator is pursuing three different objectives, namely maximizing load, minimizing wildfire risk and maintaining grid reliability. We describe each of these below.
  § IV CONCLUSION: This paper proposes the Multi-period Optimal Power Shutoff And Restoration (MOPSAR) problem, which co-optimizes preemptive power shutoffs and restoration efforts in power systems with high wildfire risk. The MOPSAR problem is implemented in a rolling horizon framework where the schedules are re-optimized on a daily basis as new information about wildfire risk become available. We apply the proposed method to the RTS-GMLC system and find that (i) a longer forecast horizon better accounts for the impact of de-energization on load shed, (ii) a larger restoration budget reduces risk by allowing for disabling and restoring more lines, and (iii) a higher risk threshold incentivizes more system redundancy, thus increasing operational security but also wildfire risk. The proposed framework provide several avenues for future work. For example, there is a need to extend the model to consider N-1 security constraints and investigate the impact of using the full AC power flow model. [...]
[3] arXiv:1103.1495v1 | Exploring the Kibble-Zurek mechanism in a secondary bifurcation
  We present new experimental results on the quenching dynamics of an extended thermo-convective system (a network array of approximately 100 convective oscillators) going through a secondary subcritical bifurcation. We characterize a dynamical phase transition through the nature of the domain walls (1D-fronts) that connect the basic multicellular pattern with the new oscillating one. Two different 
  Full text (https://arxiv.org/html/1103.1495v1), excerpts of its own sections:
  § I Introduction: A dynamical synchronization transition is the closest expression of a ’real’ phase transition in nature. Some recent interest on synchronization processes  [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] is meant to understand the interaction between oscillating units which give rise to a collective [...]
  § II Experimental setup: Our system consists on a rectangular cell $L_{x}\times L_{y}$ ( $L_{x}=470$ mm, $L_{y}=60$ mm) filled with a Silicone oil of viscosity 5cSt. Convection is achieved by heating the fluid layer from below and along a central line (in the widest direction $\hat{x}$ ). The fluid layer lies over a plane plate with a heating rail underneath. Temperature on this underlying plate ( $T_{b}$ ) is selected at a heating bath ( $T_{h}$ ). The upper surface of the fluid layer is opened to the atmosphere and the depth of the fluid layer $d$ is measured with a micrometric screw. Lateral cooled walls ( $T_{c}$ ) and room temperature ( $T_{a}$ ) are kept at $20.0\pm 0.1^{\circ}$ C. The control parameter for a fixed depth is the vertical temperature difference $\Delta T_{v}=T_{h}-T_{a}$ and the reduced control parameter is defined as $\varepsilon=\frac{\Delta T_{v}-\Delta T_{vc}}{\Delta T_{v}}$ , where $\Delta T_{vc}=T_{hc}-T_{a}$ is the critical value at the threshold. A more detailed description of the present experimental setup can be found in  Miranda and Burguete [51] . [...]
  § IV Results and discussion: The initial pattern at the beginning of each quench is the stationary one (ST), with wavelength $\lambda_{s}=4.75\pm 0.05$ mm, which corresponds to an array of 95 latent oscillators, although we observe only the central region of the system (approximately 33 oscillators). Once the quenched regime bifurcates towards an oscillatory pattern, we obtain the corresponding front $t=f_{\mu}(x)$ by selecting the Fourier oscillatory modes with the minimum frequency in order to obtain the first unstable front from the multicellular pattern. In Fig.  4 , we show the wavenumbers and frequencies of the critical modes. From Fig.  4 (a) we have measured an average wavelength of $8.76\pm 0.01$ mm for $\mu\leq 0.0095^{\circ}$ C/s, and of $9.25\pm 0.02$ mm for $\mu>0.0095^{\circ}$ C/s. The gap between these values might be inherited from two different and consecutive subcritical thresholds in the permanent regimes  [ 51 ] . This observation will be checked with the corresponding spatiotemporal diagrams and fronts further on. [...]
  § V Further remarks and conclusions: In this paper we report experimental evidence of the slow response dynamics arising from quenched transitions in a quasi-1D convective system. The quenched dynamics goes through a secondary and weakly subcritical bifurcation for a depth of the fluid layer of $d=7.5$ mm. Complementary results concerning quenches through a stronger subcritical bifurcation are going to be reported elsewhere  [ 56 ] . Specifically, these results correspond to the kind of ramped symmetry breaking bifurcations where an initially quasi-degenerated state (ST) undergoes a phase transition where it looses some symmetries towards the oscillatory patterns (ST/ALT+TW or ALT). This dynamics can be characterized from the shape of the fronts where defects become trapped above a critical value of the crossing rate $\mu_{c}$ . Fronts and topological defects are the kind of localized coherent structures that have survived a sudden transition in the laboratory, and represent an interesting analogy to the cosmological objects after the Big Bang  [ 57 ] . Figure 10: Sketch of the quenching mechanism. [...]
[4] arXiv:1012.2463v2 | The structure and evolution of confined tori near a Hamiltonian Hopf Bifurcation
  We study the orbital behavior at the neighborhood of complex unstable periodic orbits in a 3D autonomous Hamiltonian system of galactic type. At a transition of a family of periodic orbits from stability to complex instability (also known as Hamiltonian Hopf Bifurcation) the four eigenvalues of the stable periodic orbits move out of the unit circle. Then the periodic orbits become complex unstable
  Full text (https://arxiv.org/html/1012.2463v2), excerpts of its own sections:
  § 1 Introduction: The aim of this paper is to study the orbital behavior at the neighborhood of a complex unstable periodic orbit in a 3D autonomous Hamiltonian system of galactic type. Complex instability is a type of instability of periodic orbits that appears in Hamiltonian systems of three or more degrees of freedom. In order to study the dynamical behavior at the neighborhood of a complex unstable periodic orbit we use the method of surfaces of section [Poincaré 1892], which has many applications to Dynamical Astronomy [for a review see e.g. Contopoulos 2002]. A basic problem in Hamiltonian systems of three degrees of freedom is the visualization of the 4D surfaces of section. Let us assume the phase space of an autonomous Hamiltonian system, that has 6 dimensions, e.g. in Cartesian coordinates, $(x,y,z,\dot{x},\dot{y},\dot{z})$ . For a given Jacobi constant a trajectory lies on a 5D manifold. In this manifold the surface of section is 4D. This does not allow us to visualize directly the surface of section. Patsis and Zachilas [1994] proposed a method to visualize 4D spaces of section. [...]
  § 2 The Hamiltonian System: The system we use for our applications is described in details in Katsanikas and Patsis [2011]. It rotates around its z-axis with angular velocity $\Omega_{b}=60\;km\;s^{-1}\;kpc^{-1}$ . The Hamiltonian of our system is: $\displaystyle H(x,y,z,\dot{x},\dot{y},\dot{z})=$ $\displaystyle\frac{1}{2}(\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2})+\Phi(x,y,z)$ $\displaystyle-\frac{1}{2}\Omega_{b}^{2}(x^{2}+y^{2}),$ (4) where $\Phi(x,y,z)$ is our potential. The potential $\Phi(x,y,z)$ in its axisymmetric form can be considered as a representation of the Milky Way approximated by two Miyamoto disks with masses $M_{1}$ and $M_{2}$ respectively [Miyamoto and Nagai 1975]. The parameters we use in the present study are the same as in Katsanikas and Patsis [2011]. In our units, the distance $R$ =1 corresponds to 1 kpc. The velocity unit corresponds to 209.64  $km/sec$ . For the Jacobi constant (hereafter called the “energy”) $E_{j}$ =1 corresponds to 43950 $(km/sec)^{2}$ , while the velocity unit is 209.64 $km/sec$ .
  § 3 Spaces of section: A method to follow the stability of a family of periodic orbits in a system is by means of the “stability diagram” [Contopoulos and Barbanis 1985, Pfenniger 1985a]. The stability diagram gives the evolution of the stability of a family of periodic orbits in a system as one parameter varies, by means of the evolution of the stability indices $b_{1},b_{2}$ . [...]
  § 4 Conclusions: In this paper we studied the phase space structure at the neighborhood of a complex unstable periodic orbit after a direct Hamiltonian Hopf bifurcation. Close to a Hamiltonian Hopf bifurcation we observe that: 1. We have a spiral structure formed by the consequents at the neighborhood of complex unstable periodic orbits in the 2D projections of the 4D surface of section as in Contopoulos et al [1994] and Papadaki et al [1995]. Here we find that we have this spiral structure in the 3D projections and we observe a smooth color variation along their arms. This means that this spiral structure is a 4D object. 2. The consequents near a complex unstable periodic orbit arrive at a maximum distance from the periodic orbit and they move inwards. By repeating this process, a disk structure is formed in the 3D projection of the 4D surface of section, which is called a confined torus [Pfenniger 1985a,b, Jorba & Ollé 2004 and Ollé et al 2004]. On this disk structure we observe a smooth color succession. [...]
[5] arXiv:1512.00707v1 | Bifurcation sequences in the symmetric 1:1 Hamiltonian resonance
  We present a general review of the bifurcation sequences of periodic orbits in general position of a family of resonant Hamiltonian normal forms with nearly equal unperturbed frequencies, invariant under $Z_2 \times Z_2$ symmetry. The rich structure of these classical systems is investigated with geometric methods and the relation with the singularity theory approach is also highlighted. The geome
  Full text (https://arxiv.org/html/1512.00707v1), excerpts of its own sections:
  § 1 Introduction: Resonant Hamiltonian normal forms is a field of utmost interest for applications in a wide range of fields. Just to mention a few of them: celestial mechanics and astrodynamics, galactic dynamics, molecular and semi-classical quantum physics, structural engineering, etc. At the same time it is still the subject of active studies in analytical mechanics since it gives many clues for understanding non-integrable dynamics by the combination of different techniques such as group theory, algebraic and differential geometry, singularity theory, etc. For the readers involved in applications is not easy to appreciate the ability of these methods in characterizing the regular dynamics of non-integrable systems. Aim of this review is to provide an account of how to obtain a deep and ‘useful’ framework to analyze a specific class of systems by exploiting a good deal of advanced tools, but avoiding a too formal apparatus and relying only on basic knowledges of analysis and geometry. Where strictly necessary, more sophisticated tools are introduced and described in a self-consistent way. [...]
  § 2 The normal form: Let us consider a two-degrees of freedom system whose Hamiltonian is an analytic function in a neighborhood of an elliptic equilibrium. Its series expansion about the equilibrium point can be written as $H(\bm{p},\bm{q})=\sum_{j=0}^{\infty}H_{j}(\bm{p},\bm{q}),$ (1) where $H_{j}(\bm{p},\bm{q})$ , $j\geq 0$ , are homogeneous polynomials of degree $j+2$ in the canonical variables. Let us take the zero-order term ${H}_{0}$ to be in the positive definite form $H_{0}(\bm{p},\bm{q})=\frac{1}{2}\omega_{1}(p_{1}^{2}+q_{1}^{2})+\frac{1}{2}\omega_{2}(p_{2}^{2}+q_{2}^{2})$ (2) and assume that the ‘unperturbed’ frequencies satisfy a quasi-resonance condition of the form $\omega_{1}=\left(1+\delta\right)\omega_{2},$ (3) where $\delta\in\mathbb{R}$ is a ‘detuning’ parameter Henrard [1970] ; Schmidt [1974] ; Verhulst [1979] . [...]
  § 3 Further simplification of the normal form: The canonical variables $J_{\ell},\phi_{\ell}$ are the most natural to investigate the dynamics in a perturbative framework. However, several other coordinate systems can be used to unveil the aspects of this class of systems. We list those that will be useful in the following. First of all we use coordinates ‘adapted to the resonance’ Sanders et al. [2007] . There are various ways to do this: a standard recipe is to use the canonical transformation Broer et al. [1998b] $\left\{\begin{array}[]{l}J_{1}=J\\ J_{2}=\mathcal{E}-J\\ \psi=\phi_{1}-\phi_{2}\\ \chi=\phi_{2}.\end{array}\right.$ (30) This is used to perform a first reduction of the normal form, since $\chi$ is cyclic and its conjugate action $\mathcal{E}$ is the additional integral of motion. To first order, the reduced Hamiltonian is ${\mathcal{K}}=\mathcal{E}+\alpha_{2}\mathcal{E}^{2}+\left(\delta-(2\alpha_{2}+\alpha_{3})\mathcal{E}\right)J+(\alpha_{1}+\alpha_{2}-\alpha_{3})J^{2}+\alpha_{4}J(\mathcal{E}-J)\cos 2\psi. [...]
  § 4 Geometric reduction: Exploiting the transformation ( 38 ) in order to use the invariant polynomials as phase-space variables, we can therefore adopt the function ${\mathcal{K}}_{I}(I_{1},I_{2},I_{3};\mathcal{E})=\left(1+\Delta\right)\mathcal{E}+A_{1}\mathcal{E}^{2}+(B\mathcal{E}+\Delta)I_{3}+AI_{3}^{2}+C(I_{1}^{2}-I_{2}^{2})$ (45) on the reduced phase space given by the sphere ( 35 ) to study the general behavior of the family. [...]
[6] arXiv:1701.07110v1 | By chance is not enough: Preserving relative density through non uniform sampling
  Dealing with visualizations containing large data set is a challenging issue and, in the field of Information Visualization, almost every visual technique reveals its drawback when visualizing large number of items. To deal with this problem we introduce a formal environment, modeling in a virtual space the image features we are interested in (e.g, absolute and relative density, clusters, etc.) an
  Full text (https://arxiv.org/html/1701.07110v1), excerpts of its own sections:
  § 1 Introduction: Visualizing large data sets results, very often, in a cluttered image in which a lot of graphical elements overlap and many pixels become over plotted, hiding from the user the main image visual features. We deal with this problem providing a formal framework to measure the amount of decay resulting from a given visualization, then we build, upon these measures, an automatic non uniform sampling strategy that aims at reducing such a degradation. We focus on a very common visual technique, 2D scatter-plots, analyzing the loss of information derived by overlapping pixels. In this paper we improve and extend some preliminary results presented in [ 1 ] , defining a formal model that estimates the amount of overlapping elements in a given area and the remaining free space. These pieces of information give an objective indication of what is eventually visualized on the physical device; exploiting such measures we can estimate the quality of the displayed graphic devising techniques able to recover the decayed visualization. [...]
  § 2 Related Work: This paper deals with issues concerning metrics for Information Visualization and techniques to address the problem of overlapping pixels and visual clutter in computer displays. In the following we illustrate the research proposals closer to our approach and their relationship with our work.
  § 5 Discussion: In this section we show the effectiveness of our technique commenting the images obtained applying different sampling strategies. We compare the images acquired visualizing a real dataset: the one containing 160,000 mail parcels already mentioned in Section 3 . The images come from a tool specifically developed for our purposes. It is a Java based application that permits to inspect several characteristics of the displayed image such as: the data/represented density of each sample area, some quality metrics, and the number of overlapping pixels. It is also possible to apply uniform and non-uniform sampling, and to filter sample areas with data/represented density out of a specific range. Figure 5 shows: (a) the original visualization (no sampling), (b) the one obtained uniformly sampling the data leaving 80% of the original dataset, (c) the one obtained uniformly sampling the data leaving 20% of the original dataset (this value is the best uniform sampling ratio computed by the proposal shown in [ 1 ] ), (d)the one obtained using non uniform sampling. [...]
  § 6 Conclusions and future work: In this paper we presented a low grain, non uniform sampling sampling technique that automatically reduces visual clutter in a 2D scatter plot and preserves relative densities. To the best of our knowledge this approach is a quite novel way of sampling visual data. The technique exploits some statistical results and a formal model describing and measuring over plotting, screen occupation, and both data density and represented data density. Such a model allows for computing where , how , and how much to sample preserving some image characteristics (i.e., relative density). Figure 6: Non uniform sampling Several open issues rise from this work: • users must be involved. Our strategy provides precise figures but we need to map them against user perceptions. As an example, still referring to our approach, if a sample area contains twice as many active pixels as another one, does the user perceive the feeling of observing a double density for any total occupation of the areas? [...]
[7] arXiv:2309.12153v2 | $a$-Numbers of Cyclic Degree $p^2$ Covers of the Projective Line
  We investigate the $a$-numbers of $\mathbb{Z}/p^2\mathbb{Z}$-covers in characteristic $p&gt;2$ and extend a technique originally introduced by Farnell and Pries for $\mathbb{Z}/p\mathbb{Z}$-covers. As an application of our approach, we demonstrate that the $a$-numbers of ``minimal'' $\mathbb{Z}/9\mathbb{Z}$-covers can be deduced from the associated branching datum.
  Full text (https://arxiv.org/html/2309.12153v2), excerpts of its own sections:
  § 1. Introduction: Consider an algebraically closed field $k$ of characteristic $p>2$ , and let $\pi:Y\rightarrow X$ be a Galois branched cover of smooth, projective, connected curves. A prevalent research direction is to investigate to what extent invariants of $Y$ are determined by the branching datum of the cover $\pi$ . See Section  2.1 for a precise definition of the branching datum. For instance, if $Y$ is an elliptic curve, then the branching datum of $\pi$ does not determine whether $Y$ is ordinary or supersingular. Of particular interest is the case when $p$ divides $\lvert G\rvert$ , i.e. when the cover is wildly ramified. Then the ramification of $\pi$ is more complicated, due to the additional structure of the filtration of higher ramification groups. In this paper we restrict to the case when $G$ is a cyclic $p$ -group, and we write $G=\mathbb{Z}/p^{n}\mathbb{Z}$ . Some well-known invariants for curves in characteristic $p$ include the genus, $p$ -rank, and $a$ -number. [...]
  § 1.1. Outline: The rest of the paper is organized as follows. In Section 2 , we provide background information on Artin-Schreier-Witt theory and the ramification of cyclic covers of the projective line in characteristic $p$ . Additionally, we review the Cartier-Manin matrix and its relationship with the $a$ -number of a curve. We also discuss the motivation behind our question and make comparisons with existing results in this section. [...]
  § 2.5. Comparison with the known results: In this section, we compare our results and conjectures with those that are already known for Artin-Schreier covers. Consider a $\mathbb{Z}/p^{n}\mathbb{Z}$ -Galois cover $\phi_{n}:Y_{n}\xrightarrow{}\ldots\xrightarrow{}Y_{1}\xrightarrow{}Y_{0}$ of curves. Since $\phi_{n/(n-1)}:Y_{n}\xrightarrow{}Y_{n-1}$ is an Artin-Schreier cover, we can establish bounds on the $a$ -number of $Y_{n}$ inductively, building upon what is known for $\mathbb{Z}/p\mathbb{Z}$ -covers. Suppose $P\in Y_{0}$ is a branch point with ramification index $p^{n}$ . Let $(m_{1},\ldots,m_{n})$ denote the upper ramification jumps of $\phi_{n}$ at $P$ . By applying the Herbrand function and its inverse, one can compute the (unique) upper ramification jump of $\phi_{n/(n-1)}$ at the branch point $P_{n-1}\in Y_{n-1}$ that lies above $P$ . Proposition 2.18 . With the above notation, the jump of the intermediate Artin–Schreier extension $Y_{n}\to Y_{n-1}$ at $P_{n-1}$ is $\widetilde{m}_{n}=p^{n-1}m_{n}-\sum_{i=1}^{n-1}(p-1)p^{i-1}m_{i}.$ Proof. [...]
  § 4.7. The main theorem: Let $Y_{2}\to\mathbb{P}^{1}$ be a $\mathbb{Z}/9\mathbb{Z}$ -cover which is minimal in the sense of Definition  2.14 . We now prove a formula for the $a$ -number of $Y_{2}$ , implying that Conjecture  2.15 holds under the assumptions $p=3$ and $n=2$ . Theorem 4.1 . Suppose $Y_{2}\xrightarrow{}\mathbb{P}^{1}$ has branching datum $\left[\begin{array}[]{rrrrrrrr}2&\ldots&3&\ldots&0&\ldots&0&\ldots\\ \makebox[0.0pt][l]{$\smash{\underbrace{\phantom{\begin{matrix}4&\ldots\end{matrix}}}_{\text{$n_{1}$}}}$}4&\ldots&\makebox[0.0pt][l]{$\smash{\underbrace{\phantom{\begin{matrix}7&\ldots\end{matrix}}}_{\text{$n_{2}$}}}$}7&\ldots&\makebox[0.0pt][l]{$\smash{\underbrace{\phantom{\begin{matrix}2&\ldots\end{matrix}}}_{\text{$n_{3}$}}}$}2&\ldots&\makebox[0.0pt][l]{$\smash{\underbrace{\phantom{\begin{matrix}{3}&\ldots\end{matrix}}}_{\text{$n_{4}$}}}$}{3}&\ldots\\ \end{array}\right]^{\intercal}$ Then the $a$ -number of $Y_{2}$ satisfies the formula $a_{Y_{2}}=3n_{1}+7n_{2}+0n_{3}+3n_{4}.$ Proof. [...]
[8] arXiv:2402.07935v3 | On the Frobenius fields of abelian varieties over number fields
  Let $A$ be a non-CM simple abelian variety over a number field $K$. For a place $v$ of $K$ such that $A$ has good reduction at $v$, let $F(A,v)$ denote the Frobenius field generated by the corresponding Frobenius eigenvalues. Assuming $A$ has connected monodromy groups, we show that the set of places $v$ such that $F(A,v)$ is isomorphic to a fixed number field has upper Dirichlet density zero. Ass
  Full text (https://arxiv.org/html/2402.07935v3), excerpts of its own sections:
  § Main results: Let $K$ be a number field and ${\varSigma}_{K}$ the set of its finite places. For $\overline{K}$ an algebraic closure, let $G_{K}=\mathop{\rm Gal}\nolimits(\overline{K}/K)$ be the corresponding absolute Galois group. For a place $v\in{\varSigma}_{K}$ , let ${\rm Frob}_{v}$ be an associated geometric Frobenius. Let $A$ be an abelian variety defined over $K$ of dimension $g$ and conductor $\mathfrak{N}$ . For a prime $p$ , let $T_{p}A$ be the $p$ -adic Tate module of $A$ and $\rho_{A,p}:G_{K}\rightarrow\mathop{\rm Aut}\nolimits_{\mathbb{Z}_{p}}T_{p}A$ the associated $p$ -adic Galois representation. For $v\nmid p\mathfrak{N}$ , it is unramified at $v$ . Let $F(A,v)$ be the splitting field of the characteristic polynomial of $\rho_{A,p}({\rm Frob}_{v})$ . As $(\rho_{A,p})_{p}$ is a compatible system of Galois representations, $F(A,v)$ is a number field independent of $p$ , referred to as the Frobenius field associated to the pair $(A,v)$ . [...]
  § 3. Results on finite reductive groups: Let $\mathbf{G}$ be a connected reductive group defined over $\mathbb{F}_{p}$ . In this section we will give a volume upper bound for the union of certain conjugacy classes.
  § 4. Proof of Main Theorem: We now prove the main results. The first subsection sets up some notation. Then the second contains a short proof of the qualitative version (cf. Theorem  1.1 ). Finally, the third subsection is dedicated to the quantitative version (cf. Theorem  1.3 ).
  § 4.2. Proof of Theorem 1.1: Let $d$ be a square-free product of primes in ${\mathcal{P}}$ . Let ${\mathcal{F}}_{d}$ be the union of all conjugacy classes $\overline{\rho}_{d}^{\mathrm{ss}}(\mathrm{Frob}_{v})$ for $v\in S_{A,M}$ not dividing $d$ . By Lemma  4.1 , we have ${\mathcal{F}}_{d}\subseteq\Big(\prod_{p|d}\mathcal{B}_{p}\Big)\cap\overline{\rho}_{d}^{\mathrm{ss}}(G_{K})$ where $\mathcal{B}_{p}$ is the bounding set for $\mathbf{G}_{p}^{\mathrm{ss}}$ introduced in Definition  3.3 . The Chebotarev density theorem implies that (4.1) $\mathrm{ud}(S_{A,M})\leq\frac{\left|{\mathcal{F}}_{d}\right|}{\left|\overline{\rho}_{d}^{\mathrm{ss}}(G_{K})\right|}\leq\frac{\big|\big(\prod_{p|d}\mathcal{B}_{p}\big)\cap\overline{\rho}_{d}^{\mathrm{ss}}(G_{K})\big|}{\left|\overline{\rho}_{d}^{\mathrm{ss}}(G_{K})\right|}.$ To estimate the right hand side, we utilise the following decomposition $\overline{\rho}_{d}^{\mathrm{ss}}(G_{K})=\bigsqcup_{i=1}^{s}\Big(g_{i}\prod_{p|d}I_{p}\Big)=\bigsqcup_{i=1}^{s}\Big(\prod_{p|d}g_{i,p}I_{p}\Big)$ given by Lemma  4.2 . [...]
  § 4.3. Proof of Theorem 1.3: We will now use the effective Chebotarev theorem of Lagarias–Odlyzko and the Selberg sieve to obtain a power saving upper bound for the number of places with a given Frobenius field $M$ . This is possibly the approach suggested by Serre in [ 30 , §8.2] . In this section we will write $f(X)=O(g(X))$ or $f(X)\ll g(X)$ to mean the existence of an absolute constant $c$ such that $\left|f(X)\right|\leq c\left|g(X)\right|$ for all $X$ . If the constant is allowed to depend on some other object, we will indicate so in the subscripts. All constants are in fact effectively computable. Remark 4.3 . This section will be conditional on the GRH. Unconditionally, we expect that the standard methods lead to an upper bound of the form $O\big(\frac{X}{(\log X)^{\alpha}}\big)$ for some explicit $\alpha>1$ , but we have not worked out the details.
[9] QNFO: Critical Values on a Non-Uniform Number Line: Bifurcation Markers, Normalization Dependence, and the Conjectured Specialness of Physical Constants | https://papers.qnfo.org/papers/critical-values-on-a-non-uniform-number-line-bifurcation-markers-normalization-d
  We examine the conjecture that the real number line, as a model of physical state space, is misleadingly uniform: that certain parameter values act as topological phase boundaries rather than smooth increments, and that fundamental constants such as the fine-structure constant $\alpha \approx 1/137$ may mark bifurcation points between qualitatively different dynamical regimes. We formalize a numbe
  Full text (https://papers.qnfo.org/papers/critical-values-on-a-non-uniform-number-line-bifurcation-markers-normalization-d), excerpts of its own sections:
  § 1. Introduction: Physics pedagogy and practice overwhelmingly treat the real numbers as a uniform stage: the interval between $1.0$ and $1.1$ is, by assumption of the formalism, "the same kind" of interval as that between $2.0$ and $2.1$. Working dynamical intuition contradicts this. In pendulum systems, crossing a single normalized energy value changes the qualitative character of all future motion; on either side of that value, infinitesimally nearby parameter points belong to dynamically distinct worlds. [...]
  § 5. Results: All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured. **R1 [D] (simple pendulum).** The separatrix occurs at normalized energy $\varepsilon_{\text{sep}} = 2$ exactly, derived from $E_{\text{sep}} = 2mgL$ and $\varepsilon = E/(mgL)$ (Section 4.1). The integer $2$ is a bifurcation marker in the sense of Section 3.1: $\Phi$ is discontinuous there, separating libration from rotation. **R2 [D] (double pendulum).** Under the idealized equal-mass, equal-length model launched from rest, the flip threshold is an excess energy $\Delta E = 4\,mgl$ above the hanging state (Section 4.2). In the normalization $\varepsilon = \Delta E/(4mgl)$, the critical value is exactly $\varepsilon_{c} = 1$; in the well-depth normalization it is $4/3 \approx 1.333$; in the $E/(mgl)$ normalization with zero at the hanging state it is $4$. **R3 [D] (central-force model).** For $V(r) = -A/r + B/r^{2}$, the regime boundary between barrier-protected bounded motion and fall-to-center is at $\beta = 2mB/L^{2} = -1$, exactly (Section 4.3). [...]
  § 6. Discussion: **Limitations.** The formalization of Section 3.1 is deliberately coarse: topological equivalence of phase portraits is a strong notion, and weaker (or stronger) notions of "same regime" would move the location of markers. The pendulum examples are the friendliest possible — low-dimensional, exactly solvable. The helical-particle model is specified only at the level of qualitative description; the supplied QNFO summaries contain no equations, so we could not and did not derive a threshold for it. The combinatorial projection of Section 4.5 assumes independence and binary regimes, both idealizations. **What would falsify the program.** Three failure modes. (i) If, across a broad class of canonical systems, bifurcation markers under natural normalizations are *not* concentrated on small integers or simple rationals but are generically irrational and non-repeating, then "special values" reduce to convention and the non-uniformity thesis loses content. [...]
  § 7. Conclusion: We formalized the conjecture that the real number line is a misleadingly uniform model of physical parameter space by introducing the phase-portrait map $\Phi$, which partitions parameter values into regimes and whose discontinuities are bifurcation markers. Working three canonical examples in full arithmetic, we found that the simple pendulum separatrix sits at $\varepsilon_{\text{sep}} = 2$ in one natural normalization and $1$ in another; that the double pendulum flip threshold is $\Delta E = 4\,mgl$ above the hanging state, yielding critical values $1$, $4/3$, or $4$ under three conventions; and that the fall-to-center threshold of a corrected central-force problem sits at $\beta = 2mB/L^{2} = -1$ exactly. In every case the small-integer numeral is a normalization artifact — produced, in the extreme case, by dividing the threshold by itself — while the existence of the jump in $\Phi$ is convention-independent and physically real. [...]
[10] QNFO: The Continuum Critique Trilogy | https://papers.qnfo.org/papers/continuum-critique-trilogy
  Three papers, one thesis: **the real-number continuum is a map, not the territory — and many "unsolved problems" in mathematics and physics are artifacts of representational choices rather than genuine ignorance.** This monograph unifies three companion papers into a single narrative. Paper I (The Notation Problem) proposes the scaffold-stripping hypothesis: six marginalised formal systems — Laws 
  Full text (https://papers.qnfo.org/papers/continuum-critique-trilogy), excerpts of its own sections:
  § I.1 Three Convergent Threads: This monograph collects three papers written on a single day — 2026-07-29 — each addressing a different facet of a single thesis. The thesis is this: > **The real-number continuum is a flat projection that conceals qualitative phase boundaries, topological transitions, and the discrete combinatorial substrate of physical and mathematical law. Many "unsolved problems" are artifacts of representational choices — continuum, decimal base, container-based notation — rather than genuine ignorance. Moving to a representation whose native topology matches the phenomenon reveals invariants and dissolves pseudo-problems.** This thesis emerged from a synthesis of 12 Obsidian research notes spanning 2026-07-09 through 2026-07-29 [1]. [...]
  § I.2 The Three Papers: | Paper | Title | DOI | Core Claim | |:------|:------|:----|:-----------| | P1 | The Notation Problem | `https://papers.qnfo.org/papers` | Six marginalised formalisms contain valid category-theoretic invariants — their marginalisation is a notation problem, not a content problem | | P2 | Alpha as Bifurcation Parameter | `https://papers.qnfo.org/papers` | The fine-structure constant α ≈ 1/137 is hypothesised to be a critical eigenvalue of a helical null-curve stability condition — a geometric fixed point, not a free parameter | | P3 | Poisson Summation as the Adelic Bridge | `https://papers.qnfo.org/papers` | The Poisson summation formula is the analytic expression of Q self-duality in the adele ring — the Gaussian bridges discrete (Q) and continuous (R) at every place |
  § I.3 The Meta-Principle: Cross-Domain Consilience: A cross-domain consilience audit across six disciplines — Physics, Computer Science, Cognitive Science, Information Theory, Biology, and Sociology — confirmed that the same structural pattern recurs in all six [2]: > **A flat, continuous projection (ℝ, floating-point arithmetic, the mental number line, dosage-response curves, the political spectrum) conceals a discrete, phase-structured substrate (p-adic ultrametric, base-dependent representation, rhythmic-distinction perception, all-or-nothing molecular switches, tipping-point coalition dynamics).** The act of choosing a representation is not epistemologically neutral — it determines which invariants are visible and which problems appear unsolved. ---
  § Part VII: Conclusion — The Map and the Territory: Three papers, 36 pages, one thesis. The real-number continuum is a map — a flat, Archimedean projection that conceals the qualitative phase boundaries, discrete combinatorial structures, and projective invariants that constitute the territory. The territory itself — the physically accessible mathematical universe — is richer, more structured, and fundamentally different from its Archimedean shadow. The scaffold-stripping methodology (P1) shows that changing the representation reveals invariants. The helical null-curve stability problem (P2) shows that what appears as a free parameter in one representation is a geometric eigenvalue in another. Poisson summation (P3) is the analytic machinery that guarantees cross-representation consistency — the bridge that connects discrete to continuous, local to global, archimedean to ultrametric. The adelic physics programme is the attempt to take this thesis seriously: if Q is the physically accessible base field, then all completions are physically meaningful, and the continuum is one projection among many. [...]