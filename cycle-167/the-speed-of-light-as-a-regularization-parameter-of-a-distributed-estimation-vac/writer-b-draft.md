# The Speed of Light as a Regularization Parameter of an Active Vacuum Substrate: A Lattice Estimation Model with Early-Stopping Suppression of High-Frequency Modes

## Abstract

Fundamental constants are usually treated as fixed inputs to physical law, and the speed of light $c$ in particular is treated as a kinematic axiom rather than as a parameter with a function. This paper develops a conjecture from the computational-substrate research program: that a finite causal speed acts as a regularization parameter of a vacuum modeled as a distributed estimation network, suppressing high-frequency divergences the way early stopping suppresses overfitting in iterative learning systems. The gap addressed is that no existing formalization connects a finite propagation-speed constraint to explicit suppression factors for unstable high-frequency vacuum modes, or to a latency-based reinterpretation of gravitational effects. We formalize the vacuum as a lattice of locally coupled estimators with signal velocity $v$, derive the dispersion relation $\omega(k) = (2v/a)\sin(ka/2)$, and show that the causal bound $|v_g| \le v$ yields a maximum angular frequency $\omega_{\max} = 2v/a = 3.71\times 10^{43}\ \mathrm{s^{-1}}$ and a channel bandwidth $B = 5.905\times 10^{42}\ \mathrm{Hz}$ for a lattice spacing at the Planck length. A spectral response model $S(\omega) = (1+(\omega/\omega_c)^2)^{-1}$ suppresses modes at $10\,\omega_c$ by a factor of $9.90\times 10^{-3}$ and modes at $100\,\omega_c$ by $9.999\times 10^{-5}$. A congestion model in which effective latency scales as $\tau = (L/v)(1+\rho/\rho_c)$ reproduces curvature-like delay effects parametrically. The result reframes $c$ as a tunable stability parameter and specifies lattice simulations that would test whether stable macroscopic structures emerge only within a critical bandwidth window.

## 1. Introduction

Physicists, metrologists, and quantum-engineering researchers face a persistent explanatory gap: the speed of light $c = 2.998\times 10^{8}\ \mathrm{m/s}$ is measured, codified in the SI, and used daily, but no existing framework explains why the causal speed is finite at all, or what physical role finiteness plays beyond kinematics. This gap has practical consequences. In quantum error correction, engineering teams must allocate physical-to-logical qubit ratios of roughly 1000:1 to fight decoherence that is treated as an irreducible feature of a continuous-state quantum mechanics [8]; if fragility is instead a symptom of an under-regularized substrate, the design target for error-correction overheads changes. In cosmology, theorists must accept the horizon problem — the cosmic microwave background shows the same temperature to a few parts in $10^{5}$ over regions that were causally disconnected at recombination [3] — and resolve it only by adding an inflationary epoch; a framework in which the causal speed itself is a regulated, environment-dependent parameter offers an alternative lever, and variable-speed-of-light constructions have already been embedded consistently in extended special and general relativity [2] and in string-theoretic brane dynamics where the probe-brane light speed decreases as the brane approaches a bulk black hole and stabilizes at late times [3].

What decision would change if the conjecture of this paper holds? If a finite signal velocity provably suppresses high-frequency instabilities in a distributed estimation network — the same role early stopping plays in iterative learning systems, as suggested in the originating research program's appeal to network tracing capacity bounds and early-stopping guarantees — then $c$ acquires a functional interpretation: it is the regularization parameter that keeps the vacuum's estimation dynamics from diverging on high-frequency fluctuations, allowing only low-frequency, stable structures (matter, energy) to propagate as observable reality. Gravitational effects would then be reinterpretable, at least parametrically, as latency congestion in a bandwidth-limited causal channel. This would give theorists a concrete stability criterion — a critical bandwidth window — to test in lattice simulations, and would give experimentalists dispersion signatures to search for, of the kind already predicted in pre-geometric frameworks where high-energy photons accumulate propagation delays of $\Delta t = (E/E_P)\times 10^{-4}$ seconds per kiloparsec [11].

The idea is not without precedent in structure, though it is new in function. Discrete-geometry programs have derived an invariant light speed from the spectral radius of the Bruhat-Tits tree, identifying the dimensionless upper bound of $c$ with a Lieb-Robinson velocity and concluding that $c$ is a derived, macroscopic, epistemic property of combinatorial geometry rather than a fundamental axiom [9]. Those works derive the value of $c$; none of them assigns $c$ a regulatory role in stabilizing the substrate's own dynamics. That assignment is the contribution here.

This paper's contributions are:

- A formal lattice estimation model of the vacuum in which a finite signal velocity $v$ acts as an early-stopping constraint, with the dispersion relation $\omega(k) = (2v/a)\sin(ka/2)$ and the causal bound $|v_g| \le v$ derived explicitly (Section 3 and Section 4.1).
- A numerical derivation of the causal bandwidth: $\omega_{\max} = 2v/a = 3.71\times 10^{43}\ \mathrm{s^{-1}}$ and $B = 5.905\times 10^{42}\ \mathrm{Hz}$ for $a$ at the Planck length and $v = c$ (Section 4.2).
- A spectral suppression analysis showing that a bandwidth-limited response $S(\omega)$ attenuates modes at $10\,\omega_c$ by $9.90\times 10^{-3}$ and at $100\,\omega_c$ by $9.999\times 10^{-5}$, establishing the early-stopping analogy quantitatively (Section 4.3).
- A stability criterion — a critical bandwidth window inside which low-frequency structures survive and outside which modes are suppressed — stated as an explicit inequality on growth versus damping rates (Section 4.4).
- A congestion model $\tau = (L/v)(1+\rho/\rho_c)$ that reproduces curvature-like delay effects parametrically, with a worked example at $\rho/\rho_c = 10^{-3}$ (Section 4.5).
- A simulation protocol and falsification conditions for the conjecture (Sections 5, 6, and 7).

## 2. Background and Related Work

This section reviews the works that constrain what a "speed of light as regularization parameter" model may claim. Three threads are relevant: variable and emergent light speed, discrete/combinatorial substrates, and analogies from estimation, control, and optical physics.

**Variable light speed as a consistent extension of relativity.** The variable-speed-of-light (VSL) literature establishes that $c$ can be treated as a dynamical or environmental parameter without abandoning relativity. [2] extends the Lorentz transformation, the Minkowski line element, and the field equation of general relativity to allow a variable light speed $c(t)$ in a homogeneous and isotropic universe, with the minimal assumption that all moving observers at the same spacetime point measure the same light speed even though it may vary; the construction introduces the differential $d\hat{T} = c\,dT$ and a rest mass $m$ that varies so as to keep the rest energy $\hat{m} = mc^{2}$ constant, yielding covariant velocity, energy-momentum, and stress-energy tensors [2]. This matters here because it removes the objection that treating $c$ as a parameter is automatically inconsistent: the kinematic machinery survives a variable $c$. Our model goes further in interpretation — $c$ is not merely allowed to vary but is assigned a stabilizing function — and [2]'s framework is the natural consistency check for any variation we posit. Earlier VSL proposals cited in [2] sought new cosmologies to resolve the horizon and flatness problems in place of inflation; our conjecture supplies a mechanism-flavored reason why a finite, regulated $c$ might be selected for: it is the value that keeps the substrate's estimation dynamics stable.

**VSL realized in string theory.** [3] realizes the varying-speed-of-light scenario concretely: a 3+1 dimensional probe brane in the background of a black hole formed by a stack of branes, analyzed via the Dirac-Born-Infeld action, in which the speed of light on the probe brane decreases in time as the brane moves toward the bulk black hole. The authors add a rotating black-hole background to prevent the brane from hitting the horizon, bulk expansion as effective friction, and freezeout with virialization to stabilize the orbit, ensuring the speed of light tends to a constant at late times [3]. Two features of this work feed directly into our model. First, it demonstrates a physical mechanism by which the local causal speed is set by the substrate's state — exactly the dependence our congestion model requires, where $v_{\mathrm{eff}}$ depends on a local congestion density. Second, the same paper frames the horizon problem quantitatively: the cosmic microwave background is isotropic to a few parts in $10^{5}$ across regions causally disconnected at recombination, which standard causal microphysics cannot explain [3]. In our reading, a bandwidth-limited estimation substrate with a globally shared regularization parameter is a candidate mechanism for correlated behavior across causal distances, because the constraint is a property of the network, not of signal exchange between regions.

**Emergent light speed from discrete geometry.** [9] derives macroscopic spacetime and the invariant speed of light from the discrete Bruhat-Tits tree: the tree's adjacency operator acts as an effective Hamiltonian in a rigged Hilbert space, time emerges as an epistemic coarse-grained parameter via the Page-Wootters mechanism and a modular Hamiltonian, and the dimensionless upper bound of the speed of light is the Lieb-Robinson velocity derived from the graph's spectral radius, with Lorentz invariance emerging as a continuum symmetry of the Archimedean projection [9]. The paper's own summary states the conclusion plainly: "$c$ is a derived, macroscopic, epistemic property of combinatorial geometry" [9]. Our work is complementary rather than competing: [9] derives the value and invariance of $c$ from graph structure; we ask what that finite value does — and answer that it bounds the substrate's estimation bandwidth, which is precisely the role a Lieb-Robinson-type velocity plays in limiting how fast correlations can spread on a graph. The Lieb-Robinson bound in [9] is, in our language, the early-stopping constraint made geometric.

**Fragility of the continuous substrate and the signal-processing ceiling.** [8] motivates discrete substrates from an engineering failure mode: quantum states decohere rapidly not merely from technical noise but from a mathematical vulnerability of the continuous real-number field underlying standard quantum mechanics, and active quantum error correction imposes unsustainable burdens — surface codes requiring physical-to-logical ratios of roughly 1000:1, thermodynamic walls from Landauer's principle and Heisenberg back-action, and a signal-processing ceiling beyond which no classical filtering removes fundamental quantum back-action [8]. This supports our premise that the vacuum behaves like an estimation system under noise whose continuous limit is unstable without regularization. [8] also lists testable signatures of a discrete substrate — deviations at ultra-low energies, anisotropies in the fine-structure constant, discrete-spacetime effects in cosmic rays, and modified dispersion relations at high energies [8] — and modified dispersion is exactly the observable class our bandwidth window predicts (Section 4.3).

**Constants as geometric scaling factors, with falsifiable dispersion.** [11] proposes that reality emerges from a pre-geometric $S^{1}$ substrate with integer winding numbers, reinterpreting fundamental constants as geometric scaling factors, and — critically for us — makes falsifiable propagation predictions: a modulation in inspiraling binary gravitational waves at $f_{\mathrm{mod}} = \frac{m_1 m_2}{m_1 + m_2}\times f_{\mathrm{orbital}}$, and an energy-dependent photon dispersion $\Delta t = (E/E_P)\times 10^{-4}$ seconds per kiloparsec, testable against gamma-ray propagation and the growing gravitational-wave detection record [11]. This demonstrates the methodological standard our conjecture must meet: a reinterpretation of constants is publishable physics only when it emits a dispersion signature. Our Section 4.3 derives the shape of such a signature for the regularization model.

**Estimation-theoretic analogy: truncated horizons and measurability failures.** The dynamic-programming literature supplies the formal analogy for early stopping. [5] proves that the value function of a discounted dynamic program satisfies the Bellman equation under stated regularity conditions on the primitives, and documents the failure modes that motivate regularization: even with Borel-measurable primitives, the value function need not be Borel measurable, with a concrete example in which $S = A = [0,1]$, a Borel set $B \subseteq S\times A$ whose projection $E$ is not Borel, and reward $r = 1_{B}(a,s)$, so that $Tf(s) = \sup_{a\in A}1_{B}(a,s) = 1_{E}(s)$ is not Borel measurable [5]. The lesson we import is that unregularized optimization over a rich state space can produce ill-defined objects; finite-horizon truncation is a standard repair. A vacuum estimating an unstable stochastic process faces the same pathology, and a finite propagation speed is a physical implementation of horizon truncation: no estimator can condition on information farther than $v\,T$ away, so the effective optimization horizon is finite and set by $c$.

**Optical analogies: propagation-induced structure, bandwidth-limited encoding, compensation, and characterization.** Four optics papers supply mechanistic analogies rather than direct support. [1] shows that spin-orbit interaction and optical chirality can arise during propagation itself, exclusively from the Pancharatnam topological index $\ell_p$, with no pre-imposed modal asymmetry at the generation plane — the input beam carries no initial spin and identical radial amplitudes for both circular components, yet deterministic spin and chirality emerge from propagation [1]. This is a concrete optical instance of our central claim's shape: a propagation constraint (here topological, in our model causal) deterministically generates structure that was not present in the initial state. [4] demonstrates that a spatially varying ac-Stark shift maps each atom's radial position to a unique frequency shift, so that a single light-shift-broadened spectrum encodes the spatial distribution of the ensemble; the trap itself provides the reference [4]. This is the encoding principle behind our congestion model: position-dependent shifts of a shared reference encode where in a potential field an element sits, which is how a latency map could encode a gravitational potential. [7] provides the compensation dual: a weak additional field tuned to suppress the influence of a strong trapping field narrows a strongly distorted optical transition, with results over a range of compensation detunings matching a numerically evaluated density-matrix model [7]. In our framework, this is the experimental pattern for testing whether adding a controlled bandwidth constraint suppresses an unwanted spectral distortion — the direct laboratory analogue of regularization. Finally, [6] demonstrates full state tomography of light — spatial, spectral, temporal, and polarization — using SLM-encoded projective measurements and intensity-only detection through single-mode fibre, capable of analyzing mutually incoherent fields within one beam [6]. This is the measurement toolchain a laboratory test of our dispersion predictions would use: any bandwidth-induced modification of a probe beam's state is in principle fully characterizable by these methods.

**A caution on numerology.** [10] argues that base-10's dominance in science stems from human anatomy rather than mathematical naturalness, and that this anthropocentric contingency can masquerade as fundamental structure [10]. We take this as a methodological warning for the present program: claims that constants "encode" computationally meaningful values must be checked against the possibility that the pattern is an artifact of the representational system used to describe them. Our derivations therefore use dimensionless ratios wherever possible.

## 3. Methods

### 3.1 Model definition

We model the vacuum as a regular $d$-dimensional lattice of locally coupled estimators. Each site $i$ at lattice spacing $a$ holds a local estimate $x_i(t)$ of an underlying stochastic field and exchanges information only with nearest neighbors, with a signal velocity $v$ per link. The model's assumptions are stated explicitly:

- **A1 (discreteness).** The substrate is a lattice with spacing $a$. We take $a$ to be the Planck length $\ell_P = 1.616\times 10^{-35}\ \mathrm{m}$ as a reference value; the derivation holds for any $a$.
- **A2 (finite causal speed).** Information propagates at finite speed $v$; no estimator receives information from beyond radius $v\,T$ in time $T$. This is the early-stopping constraint under test.
- **A3 (local estimation dynamics).** Each site updates its estimate from neighbor information and local noise; the collective dynamics admit wave-like excitations with dispersion $\omega(k)$.
- **A4 (unstable target process).** The underlying stochastic process has unstable high-frequency components, i.e., modes whose naive amplitude would grow without the causal constraint.

Assumption A2 is the physical content of the conjecture; A1 and A3 are the standard apparatus of lattice field models; A4 encodes the "overfitting" pathology the regularization is meant to prevent.

### 3.2 Dispersion and the causal bound

For a nearest-neighbor coupled lattice, the standard dispersion relation for scalar excitations is

$$\omega(k) = \frac{2v}{a}\left|\sin\!\left(\frac{ka}{2}\right)\right|,$$

where $k$ is the wavenumber restricted to the first Brillouin zone $|k| \le \pi/a$. The group velocity is

$$v_g(k) = \frac{\partial \omega}{\partial k} = v\cos\!\left(\frac{ka}{2}\right),$$

so that $|v_g(k)| \le v$ for all $k$, with equality only at $k = 0$. This is the lattice realization of a Lieb-Robinson-type bound of the kind [9] identifies as the origin of the invariant speed: the maximum correlation-spreading velocity is a property of the graph and its coupling, not of the excitations.

### 3.3 Spectral response and suppression model

To quantify the early-stopping analogy we posit a bandwidth-limited response function for the substrate, of the standard first-order low-pass form,

$$S(\omega) = \frac{1}{1 + (\omega/\omega_c)^{2}},$$

where $\omega_c$ is the cutoff angular frequency of the causal channel. This form is an assumption (a modeling choice, not derived from A1–A4); its role is to convert the causal bound into a concrete suppression factor per frequency decade, which is what a simulation would measure.

### 3.4 Stability criterion

Let a mode of angular frequency $\omega$ have an intrinsic (unconstrained) amplitude growth rate $\gamma(\omega) \ge 0$ and let the causal constraint impose an effective damping $\Gamma(\omega)$. A mode is stable within the substrate if

$$\Gamma(\omega) > \gamma(\omega).$$

We adopt the minimal polynomial forms $\gamma(\omega) = \gamma_0 (\omega/\omega_c)^{2}$ and $\Gamma(\omega) = \Gamma_0$, both assumptions, giving the stability window

$$\omega < \omega_c\sqrt{\Gamma_0/\gamma_0} \equiv \omega_s.$$

Only modes below $\omega_s$ propagate as stable, observable structure; modes above are suppressed — the "only low-frequency stable signals propagate as reality" claim of the originating conjecture, now an inequality.

### 3.5 Congestion model

We model gravitational effects as latency congestion. Let $\rho$ be a local density of active estimation load and $\rho_c$ a saturation capacity, both dimensionless after normalization. The effective signal velocity is

$$v_{\mathrm{eff}} = \frac{v}{1 + \rho/\rho_c},$$

and the latency across a path of length $L$ is

$$\tau(\rho) = \frac{L}{v_{\mathrm{eff}}} = \frac{L}{v}\left(1 + \frac{\rho}{\rho_c}\right).$$

The fractional excess latency $\Delta\tau/\tau_0 = \rho/\rho_c$ is the model's curvature-like observable: regions of high estimation load behave as regions of increased optical depth. This is a parametric claim only; mapping $\rho/\rho_c$ onto the metric tensor of general relativity is future work (Section 6).

### 3.6 Simulation protocol

The conjecture is tested by varying $v$ in lattice or agent-based simulations of the model of Section 3.1 and measuring: (i) the amplitude of high-frequency modes as a function of $v$; (ii) the survival of localized, low-frequency structures; (iii) delay accumulation in inhomogeneous load distributions. The predictions and falsification conditions are in Sections 5 and 6.

## 4. Analysis

All input numbers are stated with their origin. Derived quantities are computed step by step.

### 4.1 The causal bound as an early-stopping constraint

From the dispersion relation of Section 3.2,

$$v_g(k) = v\cos\!\left(\frac{ka}{2}\right),$$

the extrema follow from $\cos(ka/2) = \pm 1$, i.e., $k = 0$ and $k = \pm 2\pi/a$ (outside the first Brillouin zone for the latter). Within $|k| \le \pi/a$, the maximum of $|v_g|$ is at $k = 0$:

$$|v_g|_{\max} = v\cos(0) = v.$$

Hence the causal bound $|v_g| \le v$ holds for every mode. Interpretation: no excitation, however energetic, can propagate information faster than the substrate's coupling velocity. This is the physical early-stopping rule — it truncates the effective estimation horizon of every site to $v\,T$, exactly as finite-horizon truncation bounds the path length explored in dynamic programming, the setting in which [5] shows unregularized value functions can fail to be Borel measurable.

### 4.2 Causal bandwidth of the vacuum channel

**Inputs.** Lattice spacing $a = \ell_P = 1.616\times 10^{-35}\ \mathrm{m}$ (assumption A1, reference value; the Planck length is used as the conventional scale at which continuum spacetime is expected to fail, and no result below depends on this choice beyond rescaling). Signal velocity $v = c = 2.998\times 10^{8}\ \mathrm{m/s}$ (the measured value; the SI value is exact by definition, and we use three significant figures).

**Step 1: maximum angular frequency.** The dispersion $\omega(k) = (2v/a)|\sin(ka/2)|$ is maximized at the Brillouin-zone edge $k = \pi/a$, where $\sin(\pi/2) = 1$:

$$\omega_{\max} = \frac{2v}{a} = \frac{2 \times 2.998\times 10^{8}\ \mathrm{m/s}}{1.616\times 10^{-35}\ \mathrm{m}}.$$

Numerator: $2 \times 2.998\times 10^{8} = 5.996\times 10^{8}\ \mathrm{m/s}$. Division:

$$\omega_{\max} = \frac{5.996\times 10^{8}}{1.616\times 10^{-35}} = 3.710\times 10^{43}\ \mathrm{s^{-1}}.$$

**Step 2: channel bandwidth in hertz.** The ordinary-frequency bandwidth is

$$B = \frac{\omega_{\max}}{2\pi} = \frac{3.710\times 10^{43}}{6.2832} = 5.905\times 10^{42}\ \mathrm{Hz}.$$

**Step 3: interpretation.** A causal channel with speed $c$ on a Planck-spaced lattice can carry at most $B = 5.905\times 10^{42}\ \mathrm{Hz}$ of mode bandwidth. Any estimation dynamics requiring bandwidth above this is not representable by the substrate — the finite-$c$ constraint is a hard spectral ceiling, not a soft preference. This is the quantitative form of "the vacuum cannot overfit high-frequency fluctuations": it literally lacks the bandwidth to represent them as propagating degrees of freedom.

### 4.3 Suppression factors of the bandwidth-limited response

With the response model $S(\omega) = (1+(\omega/\omega_c)^{2})^{-1}$ of Section 3.3, we compute the suppression at integer multiples of the cutoff. We identify $\omega_c$ with $\omega_{\max} = 3.710\times 10^{43}\ \mathrm{s^{-1}}$ from Step 1 (the most conservative choice: the cutoff is the physical ceiling itself).

**At $\omega = 10\,\omega_c$:**

$$S(10\,\omega_c) = \frac{1}{1 + 10^{2}} = \frac{1}{101} = 9.901\times 10^{-3}.$$

**At $\omega = 100\,\omega_c$:**

$$S(100\,\omega_c) = \frac{1}{1 + 100^{2}} = \frac{1}{10001} = 9.999\times 10^{-5}.$$

**Suppression ratio per decade:** the response falls by a factor

$$\frac{S(10\,\omega_c)}{S(100\,\omega_c)} = \frac{9.901\times 10^{-3}}{9.999\times 10^{-5}} = 99.02 \approx 10^{2}$$

per decade of frequency above cutoff — i.e., approximately $-20\ \mathrm{dB}$ per decade, the canonical signature of a first-order regularization filter. A simulation varying $v$ would measure precisely this roll-off in the mode-amplitude spectrum; observing a roll-off shallower than first-order would falsify the specific response model while leaving the bandwidth-ceiling claim of Section 4.2 intact.

### 4.4 The critical bandwidth window

With $\gamma(\omega) = \gamma_0(\omega/\omega_c)^{2}$ and $\Gamma(\omega) = \Gamma_0$ (Section 3.4), the stability boundary $\Gamma_0 = \gamma_0(\omega_s/\omega_c)^{2}$ gives

$$\omega_s = \omega_c\sqrt{\frac{\Gamma_0}{\gamma_0}}.$$

As a worked reference point, take the balanced case $\Gamma_0 = \gamma_0$ (assumption; the physical case of interest is where the substrate's damping and the process's instability are of comparable scale):

$$\omega_s = \omega_c\sqrt{1} = \omega_c = 3.710\times 10^{43}\ \mathrm{s^{-1}}.$$

The stable window is then $0 \le \omega < \omega_c$: all modes below the causal ceiling propagate stably, all modes at or above it are suppressed. For a general ratio $r = \Gamma_0/\gamma_0$, the window edge scales as $\sqrt{r}$: a substrate with weaker damping ($r = 0.01$) stabilizes only modes below $0.1\,\omega_c$, while stronger damping ($r = 100$) stabilizes up to $10\,\omega_c$ — but the latter is unphysical here because the channel itself carries no content above $\omega_{\max} = \omega_c$. The critical bandwidth window is therefore generically of order $\omega_c$, set by the causal speed, and its width in ordinary frequency is $B = 5.905\times 10^{42}\ \mathrm{Hz}$ (Section 4.2). This is the paper's central stability claim: stable macroscopic structure requires modes inside a window whose upper edge is fixed by $v$, so varying $v$ in a simulation should move the edge and change which structures survive.

### 4.5 Congestion and curvature-like delay

**Worked example.** Take a path of length $L = 1\ \mathrm{m}$, baseline velocity $v = c = 2.998\times 10^{8}\ \mathrm{m/s}$, and a local congestion fraction $\rho/\rho_c = 10^{-3}$ (assumption for illustration).

Baseline latency:

$$\tau_0 = \frac{L}{v} = \frac{1}{2.998\times 10^{8}} = 3.336\times 10^{-9}\ \mathrm{s}.$$

Congested latency:

$$\tau = \tau_0\left(1 + \frac{\rho}{\rho_c}\right) = 3.336\times 10^{-9} \times 1.001 = 3.339\times 10^{-9}\ \mathrm{s}.$$

Excess delay:

$$\Delta\tau = \tau - \tau_0 = 3.336\times 10^{-9} \times 10^{-3} = 3.336\times 10^{-12}\ \mathrm{s}.$$

The effective refractive index of the congested region is

$$n_{\mathrm{eff}} = \frac{c}{v_{\mathrm{eff}}} = 1 + \frac{\rho}{\rho_c} = 1.001.$$

A spatial gradient in $\rho/\rho_c$ therefore produces a position-dependent delay of exactly the kind that [4] exploits experimentally, where a position-dependent light shift maps radial position to a unique frequency offset and the trap itself provides the reference. In our model, the congestion field plays the role of the trap potential: a latency map imprinted on the causal channel. Whether this map satisfies an equation of the Einstein type is not derived here; what is derived is that the model produces curvature-like observables (position-dependent delays and effective indices) with a single new parameter $\rho/\rho_c$.

### 4.6 Consistency with the variable-$c$ formalism

The congestion model makes $v_{\mathrm{eff}}$ a function of the substrate state, which is a variable light speed in the sense formalized by [2]: the extended Lorentz transform and Minkowski line element there accommodate any $c$ under the assumption that all observers at the same spacetime point measure the same light speed [2]. Our $v_{\mathrm{eff}}(\rho)$ satisfies that assumption locally. Likewise, the brane realization of [3], in which the probe-brane light speed decreases as the brane approaches a bulk black hole and tends to a constant at late times through friction and vir