# Critical Values on a Non-Uniform Number Line: Bifurcation Markers, Normalization Dependence, and the Conjectured Specialness of Physical Constants

## Abstract

We examine the conjecture that the real number line, as a model of physical state space, is misleadingly uniform: that certain parameter values act as topological phase boundaries rather than smooth increments, and that fundamental constants such as the fine‑structure constant $\alpha \approx 1/137$ may mark bifurcation points between qualitatively different dynamical regimes. We formalize a number‑to‑phase‑space map $\Phi$ that assigns to each parameter value the topological equivalence class of the associated dynamics, making precise in what sense a parameter value can be a “boundary.” We work two canonical examples in full arithmetic: the simple pendulum, whose separatrix sits at normalized energy $\varepsilon = 2$ exactly, and a central‑force problem with a $1/r^{2}$ correction, whose fall‑to‑center threshold sits at dimensionless coupling $\beta = -1$ exactly. Both thresholds land on small integers only because normalization conventions absorb dimensional constants into the critical value; the same physics yields $1$, $4/3$, or $4$ under different normalizations of the double‑pendulum flip energy. We compute $\alpha \approx 7.29927 \times 10^{-3}$ from the supplied value $1/137$, show it lies roughly $2.14$ orders of magnitude below the order‑unity thresholds of our minimal models, and state the fine‑structure constant’s conjectured dynamical role as an explicitly labeled hypothesis with falsification conditions. A combinatorial projection for $N \approx 100$ coupled subsystems sharing one threshold yields a configuration space of order $10^{30}$. We argue that the “specialness” of constants is better explained as a normalization artifact plus generic bifurcation structure, unless additional model‑building succeeds.

## 1. Introduction

Physics pedagogy and practice overwhelmingly treat the real numbers as a uniform stage: the interval between $1.0$ and $1.1$ is, by assumption of the formalism, “the same kind” of interval as that between $2.0$ and $2.1$. Working dynamical intuition contradicts this. In pendulum systems, crossing a single normalized energy value changes the qualitative character of all future motion; on either side of that value, infinitesimally nearby parameter points belong to dynamically distinct worlds.

The source conjecture motivating this paper holds that (i) the real number line is a misleading projection of physical state spaces, whose intervals are not uniformly meaningful; (ii) certain values — the conjecture’s example is the integer $1$ at the double pendulum’s flip threshold under a suitable normalization — act as topological phase boundaries, where the accessible topology of motion changes qualitatively rather than smoothly; and (iii) fundamental constants such as the fine‑structure constant $\alpha \approx 1/137$ (as supplied in the grounding material) may similarly mark bifurcation points separating qualitatively different regimes, for example bound helical versus unbound motion in a Zitterbewegung‑type self‑interacting particle model.

This paper tests the internal logic of that conjecture rather than asserting or dismissing it. We do four things. First, we formalize a number‑to‑phase‑space map: given a family of dynamical systems indexed by a parameter $\lambda$, we characterize how the qualitative structure of solutions changes across critical values $\lambda_{c}$, and we show how the numerical value of $\lambda_{c}$ depends on normalization. Second, we carry out explicit derivations for the simple pendulum separatrix, the double pendulum flip threshold, and the fall‑to‑center threshold of a corrected central‑force problem, showing that each yields a small‑integer critical value under the normalizations the conjecture implicitly uses, and explaining arithmetically why this is so. Third, we compute the fine‑structure constant from its supplied value and ask whether an $\alpha$‑scale coupling could sit at the threshold of a minimal helical self‑interacting particle model; we find that it cannot without fine‑tuning, since the derived threshold is at order unity while $\alpha \approx 7.29927 \times 10^{-3}$, a separation of roughly two orders of magnitude. Fourth, we quantify the combinatorial richness that a single shared threshold generates across many coupled subsystems, as a labeled projection.

Our conclusion is deliberately two‑sided. The conjecture is correct that parameter space is not phenomenologically uniform: bifurcation values genuinely partition it into regimes with different accessible topology, a fact documented in the bifurcation literature we review. But the further step — that the specific numerical values of fundamental constants are therefore explained as bifurcation points — does not follow, because the numerical value of a dimensionless critical parameter is convention‑dependent once normalization is fixed, and because the constants we examine do not sit at the thresholds of the minimal models built to test the idea. We state the conditions under which this negative conclusion would be overturned.

## 2. Background and Related Work

We discuss all twelve supplied works. Entries [9]–[12] carry only titles and identifiers, and we say so explicitly rather than attributing content to them.

**Bifurcation phenomenology as the physics of non‑uniform parameter space.** Reference [3] (arXiv:1103.1495v1) presents experimental results on quenching dynamics in an extended thermo‑convective system — a network array of approximately $100$ convective oscillators — going through a secondary subcritical bifurcation, and characterizes the resulting dynamical phase transition through the nature of the one‑dimensional domain‑wall fronts connecting a basic multicellular pattern with a new oscillating one. This is directly relevant to our argument: it is an experimental demonstration that a control parameter’s crossing of a critical value changes the *topology* of the accessible pattern space (new domains, new walls between domains), not merely the values of observables. It also supplies the concrete subsystem count $N \approx 100$ used in our combinatorial projection of Section 4.5.

Reference [4] (arXiv:1012.2463v2) studies orbital behavior near complex unstable periodic orbits in a three‑dimensional autonomous Hamiltonian system of galactic type, showing that at a Hamiltonian Hopf bifurcation the four eigenvalues of stable periodic orbits move off the unit circle and the orbits become complex unstable. This supplies a precise, eigenvalue‑level mechanism by which a smooth change of a parameter produces a qualitative regime change — exactly the “phase boundary on the number line” phenomenon the conjecture gestures at.

Reference [5] (arXiv:1512.00707v1) reviews bifurcation sequences of periodic orbits in resonant Hamiltonian normal forms with nearly equal unperturbed frequencies, invariant under $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$ symmetry, investigated with geometric methods and connected to singularity theory. It shows that near a single resonance, parameter space is organized into an entire *sequence* of bifurcations, not one boundary — reinforcing our point that critical values are dense, structured features of families, not isolated magic numbers.

**Non‑uniformity of representation.** Reference [6] (arXiv:1701.07110v1) addresses visualization of large datasets, noting that almost every visual technique reveals drawbacks at scale, and introduces a formal environment modeling image features such as absolute and relative density in a virtual space, using non‑uniform sampling to preserve relative density. The supplied summary gives no further detail, but its core move is directly analogous to ours: a uniform grid over a domain misrepresents the domain’s structure, and a non‑uniform re‑parameterization preserves features (there, density; here, bifurcation topology) that uniform treatment destroys. We use it as the closest methodological precedent for a “non‑uniform number line” in the supplied literature.

**Threshold‑based decision structure.** References [1] and [2] come from power‑infrastructure risk, and we cite them for their structural analogy, not their subject matter. Reference [1] (arXiv:2110.07348v3) frames wildfire‑ignition mitigation from power line faults as a prioritization problem: long‑term strategies such as converting overhead lines to underground cables are expensive, so upgrades must be targeted at lines that reduce ignition risk the most; the supplied summary is truncated at this prioritization principle and gives no further methodological detail. Reference [2] (arXiv:2204.02507v3) proposes a mathematical optimization problem for utilities to decide where and when to implement pre‑emptive power shutoffs, which mitigate ignition risk but cause widespread outages, and how to co‑optimize shutoffs with restoration. Both works embody the same logical form as a bifurcation threshold: a continuous risk landscape acted on by a discrete intervention that is worthwhile only above a critical value. They illustrate that “critical value” reasoning is a general decision‑theoretic pattern, independent of any specialness of the critical number itself.

**Arithmetic perspectives on special numbers.** Reference [7] (arXiv:2309.12153v2) investigates the $a$‑numbers of $\mathbb{Z}/p^{2}\mathbb{Z}$‑covers of the projective line in characteristic $p>2$, extending a technique of Farnell and Pries for $\mathbb{Z}/p\mathbb{Z}$‑covers, and shows that the $a$‑numbers of “minimal” $\mathbb{Z}/9\mathbb{Z}$‑covers can be deduced from the associated branching datum. This is a case where an integer‑valued invariant of a geometric object is *determined* by discrete arithmetic data — a rigorous instance of numbers being “special” for structural reasons.

Reference [8] (arXiv:2402.07935v3) proves, for a non‑CM simple abelian variety $A$ over a number field $K$ with connected monodromy groups, that the set of places $v$ of good reduction for which the Frobenius field $F(A,v)$ is isomorphic to a fixed number field has upper Dirichlet density zero. This is a density‑zero statement: in a precise arithmetic sense, most places are *not* special, and the exceptional set is thin. We use both works as contrasts: arithmetic structure can make specific numbers distinguished, but the distinguished sets are provably thin — a caution against reading every salient constant as a generic feature.

**The QNFO corpus.** References [9]–[12] are supplied as titles and DOIs only: [9] “QNFO: Time as Epistemic Cognitive Fiction” (https://papers.qnfo.org/papers/time-as-epistemic-cognitive-fiction/), [10] “QNFO: COMMUTATIVE PHYSICS”, [11] “QNFO: The Continuum Critique Trilogy” (https://papers.qnfo.org/papers/continuum-critique-trilogy/), and [12] “QNFO: Invariant Structural Value: Fundamental Constants and Formulas as Invariant Relations”. No summary text is supplied for any of them, so we cannot state what they argue. By their titles, [11] and [12] appear closest to the present conjecture — a critique of the continuum, and a treatment of constants as invariant structural relations — and we flag them as natural companion reading; but we make no claim about their content, since the supplied entries give none.

## 3. Methods

### 3.1 The number‑to‑phase‑space map

Let $\mathcal{F} = \{ \dot{x} = f_{\lambda}(x) \}_{\lambda \in \mathbb{R}}$ be a one‑parameter family of dynamical systems on a state space $M$, with $x \in M$. Define the *phase portrait map*

$$
\Phi : \mathbb{R} \to \mathcal{P}(M), \qquad \lambda \mapsto \Phi(\lambda) = \text{topological equivalence class of the flow } f_{\lambda},
$$

where $\mathcal{P}(M)$ denotes the set of topological equivalence classes of flows on $M$. The conjecture’s “non‑uniform number line” is then the statement that $\Phi$ is a *step function with finitely or countably many discontinuities* on any compact interval: for $\lambda$ in an open interval between consecutive bifurcation values, $\Phi(\lambda)$ is constant, while at a bifurcation value $\lambda_{c}$, $\Phi$ jumps. We call such a $\lambda_{c}$ a *bifurcation marker*. The uniformity of the number line as a *metric* object is irrelevant to the physics; what matters is the partition induced by $\Phi$.

Two methodological commitments follow. First, the numerical value of $\lambda_{c}$ is meaningful only after a normalization of $\lambda$ is fixed; a re‑parameterization $\lambda' = g(\lambda)$ with monotone $g$ moves $\lambda_{c}$ to $g(\lambda_{c})$ without changing the physics. Any claim that a critical value “is” a specific number must therefore be relativized to a canonical normalization — typically one in which the dimensional constants of the system are absorbed into $\lambda$. Second, the physically meaningful statement is about the *existence* of a jump in $\Phi$, not the arithmetic proximity of $\lambda_{c}$ to a “nice” number.

We additionally define a logarithmic regime measure

$$
\mu_{\log}(a, b) = \left| \ln \frac{b}{a} \right|,
$$

so that multiplicative rather than additive proximity is the natural metric near thresholds — consistent with the non‑uniform sampling philosophy of [6].

### 3.2 Case study A: the simple pendulum

The simple pendulum of mass $m$, length $L$, under gravity $g$, has energy

$$
E = \frac{1}{2} m L^{2} \dot{\theta}^{2} + m g L \bigl(1 - \cos\theta\bigr).
$$

Its phase portrait is exactly solvable, providing a closed‑form bifurcation marker between libration and rotation. The derivation is given in Section 4.1.

### 3.3 Case study B: double pendulum flip threshold

We use the idealized planar double pendulum: two point masses $m$, both equal, on two massless rods of length $l$, both equal, in uniform gravity $g$, with angles $\theta_{1}, \theta_{2}$ measured from the downward vertical. The bob heights are

$$
h_{1} = -l\cos\theta_{1}, \qquad h_{2} = -l\cos\theta_{1} - l\cos\theta_{2},
$$

so the potential energy (zero at the pivot) is

$$
V(\theta_{1},\theta_{2}) = -m g l \bigl(2\cos\theta_{1} + \cos\theta_{2}\bigr).
$$

A “flip’’ is a trajectory in which the upper bob passes over the pivot, i.e. $\theta_{1}$ reaches $\pi$. We launch from rest at initial angles $(\theta_{1}^{(0)},\theta_{2}^{(0)})$, so the conserved energy equals the initial potential energy. The derivation is given in Section 4.2.

### 3.4 Case study C: fall‑to‑center threshold with a $1/r^{2}$ correction

To model the conjecture’s “helical self‑interacting particle,” we use the minimal central‑force problem with potential

$$
V(r) = -\frac{A}{r} + \frac{B}{r^{2}}, \qquad A > 0,
$$

where $B$ plays the role of a self‑interaction (or angular‑momentum‑like) coupling. Radial motion with angular momentum $L$ has effective potential

$$
U_{\text{eff}}(r) = \frac{L^{2}}{2 m r^{2}} - \frac{A}{r} + \frac{B}{r^{2}} = \frac{L^{2} + 2 m B}{2 m r^{2}} - \frac{A}{r}.
$$

The sign of the coefficient $L^{2} + 2 m B$ determines whether the effective potential is repulsive at small $r$ (bounded orbits possible) or attractive (fall to centre). The derivation is given in Section 4.3.

### 3.5 Epistemic labeling

Every quantitative statement carries one of three labels: **[D]** derived with shown arithmetic; **[P]** projection, with stated assumptions and uncertainty bounds; **[H]** hypothesis, explicitly not established here.

## 4. Analysis

### 4.1 Simple pendulum separatrix \[D\]

**Inputs.** Mass $m$, length $L$, gravity $g$ (Section 3.2); energy zero at the hanging equilibrium.

**Step 1: separatrix energy.** The minimum energy is $E_{\min}=0$ at $\theta=0$, $\dot{\theta}=0$. The separatrix — the orbit asymptotic to the unstable equilibrium at $\theta=\pi$ — has energy

$$
E_{\text{sep}} = m g L \bigl(1 - \cos\pi\bigr) = m g L \bigl(1 - (-1)\bigr) = 2 m g L.
$$

**Step 2: normalization.** Define the normalized energy $\varepsilon = E/(m g L)$. Then

$$
\varepsilon_{\text{sep}} = \frac{2 m g L}{m g L} = 2.
$$

For $\varepsilon < 2$ all orbits are librations; for $\varepsilon > 2$ all orbits are rotations. The bifurcation marker is the integer $2$ in this normalization. Note immediately that choosing $\tilde{\varepsilon}=E/(2 m g L)$ moves the marker to $\tilde{\varepsilon}_{\text{sep}}=1$: the numeral is a normalization artifact, while the jump in $\Phi$ is not.

### 4.2 Double pendulum: derivation of the flip threshold \[D\]

**Inputs.** Equal masses $m$, equal lengths $l$, gravity $g$ (Section 3.3); launch from rest, so $E = V(\theta_{1}^{(0)},\theta_{2}^{(0)})$.

**Step 1: energy at the flip configuration.** A flip requires the energy surface to reach some configuration with $\theta_{1} = \pi$. At $\theta_{1} = \pi$, $\cos\theta_{1} = -1$, so

$$
V(\pi, \theta_{2}) = -m g l \bigl(2(-1) + \cos\theta_{2}\bigr) = m g l \bigl(2 - \cos\theta_{2}\bigr).
$$

**Step 2: minimize over $\theta_{2}$.** Since $\cos\theta_{2}\in[-1,1]$, the minimum of $2-\cos\theta_{2}$ is attained at $\cos\theta_{2}=1$, i.e. $\theta_{2}=0$:

$$
E_{c} = \min_{\theta_{2}} V(\pi,\theta_{2}) = m g l (2 - 1) = m g l.
$$

**Step 3: reference energy of the hanging state.** At the fully hanging rest state $(\theta_{1},\theta_{2})=(0,0)$:

$$
V(0,0) = -m g l \bigl(2\cdot 1 + 1\bigr) = -3\,m g l.
$$

Launching from rest at $(0,0)$ gives $E = -3 m g l$, and energy is conserved. The flip condition is that the conserved energy reach the minimum energy of the set $\{\theta_{1}=\pi\}$, which is $E_{c}=+m g l$. The required *excess* energy above the hanging state is therefore

$$
\Delta E = E_{c} - V(0,0) = m g l - (-3 m g l) = 4\,m g l.
$$

**Step 4: normalization.** Define the dimensionless excess energy $\varepsilon \equiv \Delta E/(4 m g l)$. Then the flip threshold is exactly

$$
\varepsilon_{c} = \frac{4 m g l}{4 m g l} = 1.
$$

Equivalently, normalizing by the well depth $|V(0,0)| = 3 m g l$ gives $\Delta E/|V(0,0)| = 4 m g l / 3 m g l = 4/3 \approx 1.333\ldots$; normalizing by $m g l$ with the zero of energy at the hanging state gives $E/(m g l)=4$. The critical value is $1$, $4/3$, or $4$ depending on convention — the physics (a jump in $\Phi$) is identical in all three.

**Interpretation.** The conjecture’s example — the integer $1$ at the flip threshold — is correct *under the normalization* $\varepsilon = \Delta E/(4 m g l)$, which is the normalization in which the threshold coincides with the energy of the “upper bob over pivot, lower bob hanging’’ configuration. The value $1$ is not discovered in nature; it is produced by dividing the threshold by itself. What is physical is the existence of the jump in $\Phi$ at that configuration, not the numeral.

### 4.3 Central‑force model: derivation of the fall‑to‑center threshold \[D\]

**Inputs.** $V(r) = -A/r + B/r^{2}$ with $A>0$; angular momentum $L$; mass $m$ (Section 3.4).

**Step 1: small‑$r$ behavior.** As $r\to 0$, the $r^{-2}$ term dominates the $r^{-1}$ term. The coefficient of $r^{-2}$ in $U_{\text{eff}}$ is $(L^{2}+2 m B)/(2 m)$.

- If $L^{2}+2 m B > 0$, then $U_{\text{eff}}\to +\infty$ as $r\to 0$: an impenetrable barrier exists, and bounded orbits can exist.
- If $L^{2}+2 m B < 0$, then $U_{\text{eff}}\to -\infty$ as $r\to 0$: the particle spirals into the centre for generic inward motion — a qualitatively different regime.

**Step 2: critical coupling.** The boundary between regimes is

$$
L^{2}+2 m B_{c}=0 \quad\Longrightarrow\quad B_{c}= -\frac{L^{2}}{2 m}.
$$

Define the dimensionless coupling $\beta \equiv 2 m B / L^{2}$. Then the threshold is

$$
\beta_{c}= \frac{2 m B_{c}}{L^{2}} = \frac{2 m \cdot (-L^{2}/2 m)}{L^{2}} = -1.
$$

With the sign convention $B>0$ (repulsive short‑distance core), bounded orbits exist for all $\beta > -1$, and the regime boundary sits at $\beta = -1$. If instead one defines $\tilde{\beta}= -\beta$ for an attractive correction $B<0$, the threshold sits at $\tilde{\beta}_{c}=1$. Again the numeral $1$ (or $-1$) is a normalization artifact; the physics is the sign change of $L^{2}+2 m B$.

**Step 3: existence of a circular orbit.** For $L^{2}+2 m B > 0$, $U_{\text{eff}}$ has a stationary point where

$$
\frac{dU_{\text{eff}}}{dr}= -\frac{L^{2}+2 m B}{m r^{3}} + \frac{A}{r^{2}} = 0
\quad\Longrightarrow\quad
r_{\min}= \frac{L^{2}+2 m B}{m A}.
$$

Since $U_{\text{eff}}\to +\infty$ as $r\to 0$ and as $r\to\infty$, this stationary point is a minimum, with value

$$
U_{\text{eff}}(r_{\min}) = \frac{L^{2}+2 m B}{2 m}\cdot\frac{m^{2} A^{2}}{(L^{2}+2 m B)^{2}} - \frac{m A}{L^{2}+2 m B}
= -\frac{m A^{2}}{2\,(L^{2}+2 m B)}.
$$

Bound (negative‑energy) orbits exist around this minimum whenever $E<0$; the regime boundary at $\beta=-1$, not the bound/unbound energy sign, is the topological event.

### 4.4 The fine‑structure constant scale \[D\] (on the constant; \[H\] on its dynamical role)

**Input.** The grounding material supplies $\alpha \approx 1/137$.

**Computation.** Long division gives $1/137 = 0.00729927\ldots$; check: $137 \times 0.00729927 = 0.99999999$, confirming the reciprocal to the stated precision. Thus

$$
\alpha \approx \frac{1}{137} = 7.29927 \times 10^{-3}.
$$

**Comparison with thresholds.** The thresholds derived above sit at $|\beta_{c}| = 1$ in their natural dimensionless variables. The separation between an $\alpha$‑scale coupling and an order‑unity threshold is

$$
\frac{1}{\alpha} \approx 137, \qquad \log_{10}\!\left(\frac{1}{\alpha}\right) \approx 2.14,
$$

since $10^{2}=100 < 137 < 1000 = 10^{3}$ and $\log_{10}(137)=\log_{10}(1.37)+2 \approx 0.1367+2 = 2.1367$. An $\alpha$‑scale coupling is therefore about $2.14$ orders of magnitude below the natural threshold value $1$ in the minimal model of Section 4.3. For $\alpha$ itself to be a bifurcation coupling, the model would need a threshold at $\beta_{c} = \alpha$, i.e. a mechanism shifting the critical value by a factor of $\approx 137$ from the naive one — for example a coupling entering as $\beta_{\text{eff}} = \beta/\alpha$ with an additional small parameter. We state this as an explicit requirement, not a finding: no such mechanism is constructed here. The claim that $\alpha$ marks a bifurcation between bound helical and unbound motion in a Zitterbewegung‑type model is **[H]**: the source material conjectures it; no derivation or simulation in this paper supports it; Section 6 defines the falsification conditions.

### 4.5 Combinatorial projection for many coupled subsystems \[P\]

**Labeled projection, with assumptions.** Reference [3] reports an experimental network of approximately $100$ convective oscillators undergoing a secondary subcritical bifurcation. Assume (i) $N = 100$ subsystems each subject to the same binary regime split at a shared critical value, (ii) subsystems are statistically independent so that all $2^{N}$ regime assignments are realizable, and (iii) no additional constraints reduce the count. Then the configuration space has size

$$
|\mathcal{C}| = 2^{N} = 2^{100}.
$$

To evaluate $2^{100}$, use $2^{10}=1024 = 1.024 \times 10^{3}$ and raise to the 10th power:

$$
2^{100} = (2^{10})^{10} = (1.024 \times 10^{3})^{10}
= (1.024)^{10} \times 10^{30}.
$$

Using the binomial expansion $(1+x)^{10}\approx 1+10x$ for $x=0.024$ gives $(1.024)^{10}\approx 1+10(0.024)=1.24$; a more accurate evaluation yields $1.2676506\ldots$. Hence

$$
|\mathcal{C}| \approx 1.27 \times 10^{30}.
$$

Uncertainty: the exact arithmetic value $2^{100}=1.2676506\ldots \times 10^{30}$ is exact; the *physical* relevance is the uncertain part, since assumptions (i)–(iii) are idealizations — real oscillators may exhibit multi‑branch behavior or correlations that reduce the effective count below $2^{N}$. This projection quantifies only how much combinatorial structure a single shared threshold *can* generate, not that it does in the experiment of [3].

### 4.6 Logarithmic measure of the pendulum’s guarded regime \[D\]

Using the measure of Section 3.1, the logarithmic distance from the libration floor ($\varepsilon = 1$, the minimum in the shifted normalization) to the separatrix is

$$
\mu_{\log}(1,2) = \ln\frac{2}{1} = \ln 2 \approx 0.693147,
$$

where $\ln 2 = 0.6931471805\ldots$. By contrast, the additive distance is $2-1 = 1$. The two measures disagree by a factor $1/0.693147 \approx 1.4427$, illustrating concretely that “how far’’ a parameter value is from a threshold depends on the measure chosen — the operational content of non‑uniformity.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

**R1 \[D\] (simple pendulum).** The separatrix occurs at normalized energy $\varepsilon_{\text{sep}} = 2$ exactly, derived from $E_{\text{sep}} = 2 m g L$ and $\varepsilon = E/(m g L)$ (Section 4.1). The integer $2$ is a bifurcation marker in the sense of Section 3.1: $\Phi$ is discontinuous there, separating libration from rotation.

**R2 \[D\] (double pendulum).** Under the idealized equal‑mass, equal‑length model launched from rest, the flip threshold is an excess energy $\Delta E = 4\,m g l$ above the hanging state (Section 4.2). In the normalization $\varepsilon = \Delta E/(4 m g l)$, the critical value is exactly $\varepsilon_{c}=1$; in the well‑depth normalization it is $4/3 \approx 1.333$; in the $E/(m g l)$ normalization with zero at the hanging state it is $4$.

**R3 \[D\] (central‑force model).** For $V(r) = -A/r + B/r^{2}$, the regime boundary between barrier‑protected bounded motion and fall‑to‑center is at $\beta = 2 m B / L^{2} = -1$, exactly (Section 4.3). Stable circular orbits exist at radius $r_{\min}= (L^{2}+2 m B)/(m A)$ for $\beta > -1$, with minimum effective potential $-m A^{2}/\bigl(2(L^{2}+2 m B)\bigr)$.

**R4 \[D\] ($\alpha$ scale).** From the supplied $\alpha \approx 1/137$, we compute $\alpha \approx 7.29927 \times 10^{-3}$ and $1/\alpha \approx 137$, i.e. $\log_{10}(1/\alpha) \approx 2.14$ (Section 4.4). An $\alpha$‑scale coupling is $\approx 137$ times smaller than the order‑unity thresholds of R1–R3 in their natural dimensionless variables.

**R5 \[P\] (combinatorial projection).** Under the assumptions of Section 4.5 ($N = 100