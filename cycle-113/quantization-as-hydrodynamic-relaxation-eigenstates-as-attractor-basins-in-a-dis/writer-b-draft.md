# Quantization as Hydrodynamic Relaxation: Eigenstates as Attractor Basins in the Dissipative Madelung Picture

## Abstract

We formulate a deterministic, classical reinterpretation of quantum dynamics in which "quantum jumps" are continuous relaxation events. Starting from the Madelung hydrodynamic representation, we add a linear drag term to the momentum equation and show, by explicit linearization around the harmonic-oscillator ground state, that stationary eigenstate densities are stable attractors of the resulting flow: density and phase perturbations decay at rate $\gamma/2$ with oscillation frequency $\omega_k=\sqrt{\hbar^2k^4/(4m^2)-\gamma^2/4}$, crossing over to overdamped decay when $\gamma>\hbar k^2/m$. In a two-mode truncation, excited-state population relaxes exponentially with characteristic time $\tau_E=1/\gamma$, which we evaluate for representative parameters ($\gamma=10^9\ \mathrm{s^{-1}}$ gives $\tau_E=1.0\times10^{-9}\ \mathrm{s}$). We derive the quantum potential of the oscillator ground state exactly, $Q_q=\hbar\omega/2-m\omega^2x^2/2$, verifying stationarity. Discrete outcomes are attributed not to intrinsic discontinuity but to measurement-induced stability: basins of attraction in configuration space, with Born-rule statistics recovered as a projection under an ergodic-mixing assumption that we state explicitly and do not verify numerically here. We connect the program to rigorous relaxation limits in quantum hydrodynamics, to hydrodynamic attractors in kinetic theory, and to experimentally measured qubit relaxation, and we specify falsification criteria.

## 1. Introduction

The standard interpretation of quantum mechanics treats measurement outcomes as intrinsically discrete and stochastic: a system in a superposition is observed in an eigenstate, and the transition is called a "jump." This paper explores an alternative hypothesis: that the appearance of quantization is a property of dynamics, not of ontology. In a hydrodynamic reformulation of the Schrödinger equation — the Madelung picture, in which the wavefunction $\psi=\sqrt{\rho}\,e^{iS/\hbar}$ is replaced by a density field $\rho$ and a phase field $S$ — stationary eigenstates become steady solutions of a fluid flow. We hypothesize that with a small dissipative term added, these steady solutions become attractors: nearby initial conditions relax continuously and deterministically onto them. On this view, a "quantum jump" is the trajectory of a continuous field relaxing into a basin of attraction, and the discreteness of outcomes is supplied by the partition of configuration space into basins, not by any discontinuity in the dynamics.

The hypothesis matters because, if correct, it re-grounds quantum statistics in classical measure theory: probabilities become phase-space measures over initial conditions, and wavefunction collapse becomes a relaxation process with a computable timescale. It also makes the framework falsifiable in an unusual way: it predicts continuity and determinism at the individual-trajectory level, which can be attacked by pre-registered protocols of the kind sketched in the QNFO corpus item on pre-registered falsification of deterministic measurement-triggered relaxation [10], whose supplied summary contains no further detail and which we therefore use only as evidence that such a falsification program exists in the surrounding research context.

Our contributions are: (i) an explicit derivation of the dissipative Madelung equations and the exact quantum potential of the harmonic-oscillator ground state; (ii) a linear stability analysis showing that the ground-state density is an attractor with decay rate $\gamma/2$ and an explicit overdamped crossover; (iii) a two-mode population-relaxation estimate with fully shown arithmetic; (iv) a timescale hierarchy computation connecting relaxation to diffusion; and (v) a clearly labeled projection for Born-rule statistics under an ergodicity assumption. We do not claim a numerical simulation of double-slit or Stern–Gerlach convergence in this paper; we define the protocol and the quantities a future simulation must produce.

## 2. Background and Related Work

**Affine quantization.** [1] contrasts canonical quantization, built on the commutator $[Q,P]=i\hbar\,\mathbb{1}$, with affine quantization, built on $[Q,D]=i\hbar\,Q$ where $D\equiv(PQ+QP)/2$, and notes that affine quantization admits operator domains with $Q$ restricted to a half-line such as $0<Q<\infty$. This is directly relevant to the present program: the Madelung density $\rho$ is non-negative by construction, so a quantization scheme adapted to positive variables is the natural algebraic setting for a hydrodynamic re-foundation. The supplied summary of [1] states the commutator structure and domain properties and nothing further about gravity applications, so we cite it only for these structural facts.

**Quantum hydrodynamics and relaxation limits.** [3] analyzes weak solutions of the quantum hydrodynamics (QHD) system with a collisional term on the one-dimensional torus and rigorously proves a time-relaxation limit towards the quantum drift-diffusion (QDD) equation, with global-in-time finite-energy weak solutions obtained by standard energy methods. This is the closest rigorous mathematical anchor for our hypothesis: it establishes, in a well-posed PDE setting, that a dissipative quantum fluid does relax onto a simpler parabolic dynamics. Our attractor claim is a finite-dimensional, state-space analogue of the same relaxation philosophy, though we prove nothing at comparable rigor here.

**Hydrodynamic attractors in kinetic theory.** [4] solves the Boltzmann equation in the relaxation-time approximation using a hierarchy of angular moments for an azimuthally symmetric, radially expanding, boost-invariant conformal system undergoing Gubser flow, comparing truncated moment solutions to the exact solution. The key conceptual export is the attractor picture: far-from-equilibrium evolution rapidly loses memory of initial microdetails and converges onto a universal hydrodynamic trajectory. [8] extends the attractor concept to periodically driven ultracold quantum gases, noting that hydrodynamic attractors had previously been explored only in systems undergoing monotonic expansion, with the rapid hydrodynamization of the quark–gluon plasma motivating the field. Both works support the plausibility of attractor behavior in continuum dynamics generally; neither addresses measurement or quantization, and we use them only as precedent for attractor-dominated relaxation in hydrodynamic variables.

**Eigenstate structure.** [5] concerns analytical eigenvalues and eigenstates of the quantum Rabi model, motivated by the model's widespread use in quantum optics, quantum computing, cavity QED, and nanoelectromechanical systems, and by the need to describe a two-level system coupled to an oscillator when the rotating-wave approximation fails. Our two-mode relaxation model in Section 4 is a deliberately simplified cousin: a discrete pair of stationary states between which a dissipative flow redistributes population. [6] treats real-time quantum simulation of nuclear dynamics in first quantization, noting that first-principles classical simulation is hindered by exponential resource cost while quantum hardware may offer scalable simulation; first quantization is precisely the trajectory-like representation in which our hydrodynamic relaxation would have to manifest, making such platforms a candidate testbed, though the entry's summary gives no further methodological detail we can rely on.

**Measured relaxation in qubit platforms.** [7] studies relaxation of excited orbital, valley, and spin qubit states in single-electron silicon quantum dots, reporting that relaxation times depend sensitively on dot size and external magnetic field and that orbital relaxation times are generally short (the supplied summary truncates there). This supplies the experimental category — exponential relaxation of excited states with parameter-dependent timescales — that our deterministic picture must reproduce without invoking stochastic collapse. **Cloud quantum hardware.** [2] describes the Tianyan quantum cloud platform with a Zuchongzhi 3.0-like superconducting processor named Tianyan-287 featuring 105 qubits and single-qubit, two-qubit, and readout fidelities of 99.90%, 99.56%, and 98.7% respectively. Such platforms are where outcome-frequency statistics could be gathered at scale; we cite it only for these hardware facts.

**QNFO corpus items.** [9] ("Hydrodynamic Stability Hypothesis"), [10] ("A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation"), and [11] ("Hydrodynamic-Topological Continuum") are supplied as corpus context entries with empty summaries. We therefore cannot attribute any specific content to them; we note only that their titles indicate an existing research thread concerned with hydrodynamic stability, pre-registered falsification of deterministic relaxation, and continuum-topological structure, which situates the present paper within that program.

## 3. Methods

### 3.1 Madelung transform and dissipative closure

Write $\psi(\mathbf{x},t)=\sqrt{\rho(\mathbf{x},t)}\,e^{iS(\mathbf{x},t)/\hbar}$. The Schrödinger equation $i\hbar\,\partial_t\psi=\hat{H}\psi$ with $\hat{H}=-\frac{\hbar^2}{2m}\nabla^2+V$ becomes, with velocity $\mathbf{u}=\nabla S/m$:

$$\partial_t\rho+\nabla\cdot(\rho\,\mathbf{u})=0,$$

$$m\,(\partial_t+\mathbf{u}\cdot\nabla)\,\mathbf{u}=-\nabla\left(V+Q_q\right),\qquad Q_q\equiv-\frac{\hbar^2}{2m}\frac{\nabla^2\sqrt{\rho}}{\sqrt{\rho}}.$$

Here $Q_q$ is the quantum potential, the only term distinguishing the Madelung fluid from a classical compressible fluid. We add a linear drag (friction) term with coefficient $\gamma>0$ (units $\mathrm{s^{-1}}$):

$$m\,(\partial_t+\mathbf{u}\cdot\nabla)\,\mathbf{u}=-\nabla\left(V+Q_q\right)-m\gamma\,\mathbf{u}.$$

The drag is the minimal dissipative closure: it preserves the continuity equation (hence positivity and conservation of $\rho$), damps kinetic energy monotonically, and leaves stationary eigenstate solutions exactly invariant, since $\mathbf{u}=0$ there. This last point is the crux of the attractor hypothesis: eigenstates are fixed points, and the question is their stability.

### 3.2 Stability analysis method

We linearize the dissipative system about a stationary solution $(\rho_0,S_0)$ with $\mathbf{u}_0=0$: set $\rho=\rho_0+\delta\rho$, $\mathbf{u}=\delta\mathbf{u}$, retain first order in $(\delta\rho,\delta\mathbf{u})$, and insert plane-wave perturbations $\delta\rho\propto e^{i(kx-\Omega t)}$. The growth/decay of $\mathrm{Im}\,\Omega$ decides attractor status. For the two-mode population question we use a phenomenological energy-dissipation argument anchored to the same $\gamma$. All numerical evaluations use $m$ equal to the electron mass $9.109\times10^{-31}\ \mathrm{kg}$, $T=300\ \mathrm{K}$, and stated $\gamma$, $\omega$, $k$; these are model parameters, not measurements.

## 4. Analysis

### 4.1 Exact quantum potential of the oscillator ground state

Take $V(x)=\frac{1}{2}m\omega^2x^2$ and the ground-state density $\rho_0(x)=\frac{1}{\sqrt{\pi}\sigma}e^{-x^2/\sigma^2}$ with $\sigma^2=\hbar/(m\omega)$. Then $\sqrt{\rho_0}\propto e^{-x^2/(2\sigma^2)}$, and:

$$\frac{d^2}{dx^2}\sqrt{\rho_0}=\left(\frac{x^2}{\sigma^4}-\frac{1}{\sigma^2}\right)\sqrt{\rho_0}.$$

Therefore:

$$Q_q=-\frac{\hbar^2}{2m}\left(\frac{x^2}{\sigma^4}-\frac{1}{\sigma^2}\right)=\frac{\hbar^2}{2m\sigma^2}-\frac{\hbar^2x^2}{2m\sigma^4}.$$

Substituting $\sigma^2=\hbar/(m\omega)$: $\frac{\hbar^2}{2m\sigma^2}=\frac{\hbar^2 m\omega}{2m\hbar}=\frac{\hbar\omega}{2}$, and $\frac{\hbar^2}{2m\sigma^4}=\frac{\hbar^2 m^2\omega^2}{2m\hbar}=\frac{m\omega^2}{2}$. Hence:

$$Q_q(x)=\frac{\hbar\omega}{2}-\frac{m\omega^2x^2}{2}.$$

Stationarity check: the Hamilton–Jacobi equation requires $\frac{(\nabla S_0)^2}{2m}+V+Q_q=E_0$. With $S_0=\text{const}$, $V+Q_q=\frac{m\omega^2x^2}{2}+\frac{\hbar\omega}{2}-\frac{m\omega^2x^2}{2}=\frac{\hbar\omega}{2}=E_0$. The ground state is an exact fixed point of the Madelung flow, with or without drag. This is the input to the stability analysis.

### 4.2 Linearized attractor dynamics

Linearizing the continuity equation about $(\rho_0,\mathbf{u}_0=0)$ gives $\partial_t\delta\rho+\rho_0\,\nabla\cdot\delta\mathbf{u}=0$. Linearizing the quantum potential: writing $\eta=\delta\rho/\rho_0$, one finds to first order $\delta Q_q=-\frac{\hbar^2}{4m}\nabla^2\eta$ (from expanding $\nabla^2\sqrt{\rho}/\sqrt{\rho}$ around $\sqrt{\rho_0}$; the factor $1/4$ arises because $\sqrt{\rho}$ is the differentiated field). For a plane wave $\eta\propto e^{i(kx-\Omega t)}$, $\delta Q_q=\frac{\hbar^2k^2}{4m}\eta$. The linearized momentum equation (taking $V$ locally flat, $\delta V=0$) is:

$$m\,\partial_t\,\delta\mathbf{u}=-\nabla\,\delta Q_q-m\gamma\,\delta\mathbf{u}.$$

From continuity, $-i\Omega\,\eta+i k\,\delta u_x=0$, so $\delta u_x=\Omega\,\eta/k$. Substituting into the momentum equation with $\partial_t\delta u_x=-i\Omega\,\delta u_x$:

$$-i\,m\,\Omega\,\frac{\Omega\,\eta}{k}=-i\,k\,\frac{\hbar^2k^2}{4m}\,\eta-m\gamma\,\frac{\Omega\,\eta}{k}.$$

Multiplying by $k/\eta$ and dividing by $m$:

$$-i\,\Omega^2=-i\,\frac{\hbar^2k^4}{4m^2}-\gamma\,\Omega \quad\Longrightarrow\quad \Omega^2+i\gamma\,\Omega-\frac{\hbar^2k^4}{4m^2}=0.$$

Solving the quadratic in $\Omega$:

$$\Omega=-\frac{i\gamma}{2}\pm\sqrt{\frac{\hbar^2k^4}{4m^2}-\frac{\gamma^2}{4}}.$$

**Result:** every perturbation mode decays as $e^{-\gamma t/2}$; the oscillation frequency is $\omega_k=\sqrt{\hbar^2k^4/(4m^2)-\gamma^2/4}$, real (underdamped) when $\gamma<\hbar k^2/m$ and purely imaginary (overdamped) when $\gamma>\hbar k^2/m$. Since $\mathrm{Im}\,\Omega=-\gamma/2<0$ for all $k$ whenever $\gamma>0$, the ground-state density is a linearly stable attractor of the dissipative Madelung flow for every wavenumber. Numerical instance: with $\gamma=10^9\ \mathrm{s^{-1}}$, the amplitude decay time is:

$$\tau_{\text{lin}}=\frac{2}{\gamma}=\frac{2}{10^9\ \mathrm{s^{-1}}}=2.0\times10^{-9}\ \mathrm{s}.$$

Overdamped crossover for $k=10^7\ \mathrm{m^{-1}}$: $\hbar k^2/m=(1.055\times10^{-34}\ \mathrm{J\,s})\times(10^{7}\ \mathrm{m^{-1}})^2/(9.109\times10^{-31}\ \mathrm{kg})=\frac{1.055\times10^{-34}\times10^{14}}{9.109\times10^{-31}}=\frac{1.055\times10^{-20}}{9.109\times10^{-31}}=1.16\times10^{10}\ \mathrm{s^{-1}}$. Since $10^9<1.16\times10^{10}$, this mode is underdamped at $\gamma=10^9\ \mathrm{s^{-1}}$: perturbations ring at $\omega_k\approx\hbar k^2/(2m)=5.8\times10^9\ \mathrm{rad\,s^{-1}}$ while decaying at $\gamma/2$.

### 4.3 Two-mode population relaxation

Truncate to the ground and first excited oscillator states, $E_0=\hbar\omega/2$, $E_1=3\hbar\omega/2$, gap $\Delta E=E_1-E_0=\hbar\omega$. In the damped flow, mechanical energy dissipates at rate $\gamma$ (from $dE/dt=-m\gamma\langle u^2\rangle$ for the drag term), so the excited-state population — proportional to excess energy in the two-mode sector — obeys the projection:

$$p_1(t)=p_1(0)\,e^{-\gamma t},\qquad \tau_E=\frac{1}{\gamma}.$$

With $\omega=10^{12}\ \mathrm{rad\,s^{-1}}$ and $\gamma=10^9\ \mathrm{s^{-1}}$: $\Delta E=\hbar\omega=1.055\times10^{-34}\times10^{12}=1.055\times10^{-22}\ \mathrm{J}=0.658\ \mathrm{meV}$ (using $1\ \mathrm{meV}=1.602\times10^{-22}\ \mathrm{J}$: $1.055\times10^{-22}/1.602\times10^{-22}=0.658$). The relaxation time is $\tau_E=1/10^9\ \mathrm{s^{-1}}=1.0\times10^{-9}\ \mathrm{s}=1.0\ \mathrm{ns}$. This is the deterministic "jump time": continuous relaxation, no discontinuity, with a timescale in the nanosecond range for these parameters — the same order category as the parameter-dependent excited-state relaxation times measured in silicon quantum dots [7], though we do not claim quantitative agreement with any specific measured value, since the entry's summary supplies no numbers.

### 4.4 Timescale hierarchy: relaxation versus diffusion

The overdamped (drift-diffusion) limit of the dissipative dynamics has diffusivity $D=k_B T/(m\gamma)$ (Einstein relation for drag coefficient $m\gamma$). At $T=300\ \mathrm{K}$: $k_BT=1.381\times10^{-23}\times300=4.143\times10^{-21}\ \mathrm{J}$; $m\gamma=9.109\times10^{-31}\times10^9=9.109\times10^{-22}\ \mathrm{kg\,s^{-1}}$; hence:

$$D=\frac{4.143\times10^{-21}}{9.109\times10^{-22}}=4.55\ \mathrm{m^2\,s^{-1}}.$$

Diffusion time over $L=1\ \mathrm{\mu m}=10^{-6}\ \mathrm{m}$:

$$t_D=\frac{L^2}{D}=\frac{10^{-12}}{4.55}=2.2\times10^{-13}\ \mathrm{s}.$$

Hierarchy: $t_D=2.2\times10^{-13}\ \mathrm{s}\ll\tau_E=1.0\times10^{-9}\ \mathrm{s}$. Density redistributes diffusively roughly $4.5\times10^3$ times faster than energy relaxes ($\tau_E/t_D=10^{-9}/2.2\times10^{-13}=4.5\times10^3$). Physically: the flow first spreads the density across the accessible region, then relaxes it onto the attractor — the opposite ordering from an instantaneous "jump," and a distinguishing signature of the hypothesis.

### 4.5 Born-rule statistics as a labeled projection

**Assumption (stated, not proven here):** the dissipative flow is ergodic on the energy shell before basin selection, so the probability of observing outcome $i$ equals the invariant phase-space measure $\mu_i$ of basin $i$. Under this assumption, $P(i)=\mu_i$, and Born-rule statistics $P(i)=|c_i|^2$ are recovered iff the flow maps the initial quantum measure $|c_i|^2$ onto the basin measures — a measure-preservation condition we do not verify in this paper. No numerical value is claimed; the projection is