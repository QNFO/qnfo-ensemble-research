# Quantization as Hydrodynamic Relaxation: Eigenstates as Attractor Basins in a Dissipative Madelung Fluid (Version 3.0)

## Abstract

Quantum measurement is presently modeled as an instantaneous stochastic collapse, a postulate that conflicts with the continuous unitary dynamics of the Schrödinger equation and complicates the error budgets of quantum hardware. We revise a deterministic alternative: adding a minimal linear drag term to the Madelung hydrodynamic formulation makes Hamiltonian eigenstate densities exact fixed points of a contractive flow, so that "quantum jumps" become continuous relaxation events. This version corrects two errors of the previous publication: the claimed global Lyapunov contractivity proof is withdrawn and replaced by an explicit linearized attractivity result, and the diffusion-timescale calculation is reclassified as a phenomenological estimate outside the overdamped regime that the same parameters occupy. We derive closed-form level-to-level relaxation times $t_{n\to n-1}=\ln[(n+\tfrac12)/(n-\tfrac12)]/(2\gamma)$, giving $t_{1\to0}=0.549306/\gamma$ and $t_{2\to1}=0.255413/\gamma$; for $\gamma=10^{9}\,\mathrm{s^{-1}}$ the per-period phase-space contraction factor is $0.881911$ at $\gamma/\omega=0.01$. A pre-registered falsification study of deterministic relaxation maps, which found a maximum Born-rule deviation of $0.5$ arising from a degenerate outcome channel, is incorporated: the Born rule is retained as an explicit ensemble assumption (Assumption B), not derived, and no purely deterministic map can derive it. The program yields testable structural predictions—accelerating relaxation with excitation and continuous deterministic trajectories—while its statistical postulate remains the primary falsification target.

## 1. Introduction

Quantum processors must repeatedly measure qubit states to extract computational results, and the fidelity of those measurements sets a hard ceiling on usable circuit depth. The Tianyan-287 superconducting platform reports single-qubit gate fidelity of $99.90\%$, two-qubit gate fidelity of $99.56\%$, and readout fidelity of $98.7\%$ [2]; readout is the weakest link in that chain. Every percentage point of readout error multiplies the overhead of error-correction protocols, directly affecting the cost and scalability of quantum-computing deployments. The conventional account of measurement—the collapse postulate—treats the event as fundamentally stochastic and discontinuous, so hardware designers cannot model or engineer it as a physical process; they can only characterize its statistics after the fact. If measurement were instead a continuous, deterministic relaxation of a quantum fluid with a computable timescale, designers could treat readout as a controllable dissipative process with an engineered relaxation rate, and error mitigation could target the relaxation dynamics rather than only its output statistics.

This paper investigates that possibility and repairs the two defects identified in its previous publication. First, the earlier text claimed that "a Lyapunov-energy argument proves global contractivity of the flow," while its own Limitations section conceded that the argument "guarantees attractivity of the fixed-point set but does not ensure convergence to a unique eigenstate." No Lyapunov construction appears in the derivations, and none is claimed here: what is actually established is a linearized stability result—every perturbation mode about an eigenstate density decays at rate $\gamma/2$—which is a local attractivity statement about the fixed-point set, not a proof of global convergence to a unique eigenstate. Second, the earlier diffusion calculation invoked the Einstein relation "in the overdamped limit" at $\gamma=10^{9}\,\mathrm{s^{-1}}$, while the paper's own crossover calculation classifies the same parameters as underdamped because $\hbar k^{2}/m=1.16\times10^{10}\,\mathrm{s^{-1}}>\gamma$. The inconsistency is resolved here by keeping the crossover classification and demoting the diffusion time to a clearly labeled phenomenological comparison, valid only as an order-of-magnitude bound.

A further constraint, absent from the earlier version, now shapes the whole program. A pre-registered simulation of deterministic measurement-triggered relaxation toward eigenstate basins found that a deterministic map from a fixed initial state produces a degenerate outcome channel—probabilities of only $0$ or $1$—with a maximum deviation of $0.5$ from the Born rule across all seven tested configurations, fifty times the pre-registered tolerance of $10^{-2}$ [10]. That result is structural, not parametric: no deterministic map from a fixed initial state can reproduce fractional Born probabilities. Accordingly, this paper carries the Born rule as an explicit ensemble assumption over initial conditions (Assumption B), states plainly that the deterministic relaxation dynamics alone cannot supply it, and identifies the ensemble ingredient as the program's central open problem and falsification target.

**Contributions.**
- **C1.** Derivation of the damped Madelung equations and demonstration that eigenstate densities are exact fixed points of the flow (Section 4.1).
- **C2.** Linearized analysis showing universal decay rate $\gamma/2$ for all wavenumbers, with the overdamped crossover at $\gamma=\hbar k^{2}/m$, and the explicit retraction of the earlier global-contractivity claim (Section 4.2).
- **C3.** Closed-form level-to-level relaxation law $t_{n\to n-1}=\ln[(n+\tfrac12)/(n-\tfrac12)]/(2\gamma)$ with computed values $t_{1\to0}=0.549306/\gamma$ and $t_{2\to1}=0.255413/\gamma$ (Section 4.3).
- **C4.** Per-period phase-space contraction factors and a corrected, clearly labeled timescale comparison between relaxation and diffusion (Sections 4.4–4.5).
- **C5.** Integration of the pre-registered falsification of deterministic Born-rule reproduction into the framework: the Born rule is an ensemble assumption, and the deterministic dynamics alone is provably insufficient (Section 4.7, drawing on [10]).
- **C6.** A falsification protocol targeting the $n$-dependence of relaxation times and the continuity of trajectories, specified as proposed future work (Sections 3.3 and 7).

## 2. Background and Related Work

**[1] Affine quantization.** The work shows that the commutator $[Q,D]=i\hbar\,Q$, with $D\equiv(PQ+QP)/2$, defines an affine quantization whose operators can live on half-line domains such as $0<Q<\infty$, in contrast to canonical quantization, which requires $-\infty<P,Q<\infty$ [1]. This matters here because the Madelung density $\rho$ is non-negative by construction; an algebraic foundation that accommodates half-line variables is the natural setting if the hydrodynamic picture is to be promoted from a reformulation to a foundation.

**[2] Tianyan quantum cloud platform.** The platform report gives the hardware context: the Tianyan-287 processor features 105 qubits with single-qubit gate, two-qubit gate, and readout fidelities of $99.90\%$, $99.56\%$, and $98.7\%$ respectively, and demonstrated a large-scale random-circuit-sampling experiment with 74 qubits and 24 cycles [2]. These are the numbers against which any alternative measurement theory must eventually show operational relevance, and they are used quantitatively in Section 4.6.

**[3] Time-relaxation limit for quantum hydrodynamics.** The work studies weak solutions of the one-dimensional quantum hydrodynamics (QHD) system with a collisional drag term $-J/\tau$ on a torus and rigorously proves the time-relaxation limit $\tau\to0$ toward the quantum drift-diffusion (QDD) equation, including global well-posedness of finite-energy weak solutions with strictly positive density [3]. This supplies the closest mathematical analogue to the present program: a hydrodynamic formulation with a momentum-relaxation term that possesses a well-defined long-time limit. The analogy is partial—the proven limit is convergence to a drift-diffusion equation, not convergence to discrete eigenstate basins—and Section 6 discusses this limitation explicitly.

**[4] Hydrodynamic attractors for Gubser flow.** The work solves the Boltzmann equation in relaxation-time approximation via a hierarchy of angular moments for a system undergoing Gubser flow, and finds that the moments converge rapidly to an attractor before entering the viscous hydrodynamic regime, at a timescale much shorter than isotropization [4]. This is the same memory-loss mechanism that eigenstate attractor basins exploit: late-time observables lose sensitivity to initial conditions. The transposition is from a relativistic kinetic fluid to the non-relativistic Madelung fluid.

**[5] Eigenvalues and eigenstates of the quantum Rabi model.** The work addresses the quantum Rabi model—a two-level system coupled to a quantum oscillator—in the regime where the rotating wave approximation fails, a model widely used in quantum optics, quantum computing, cavity QED, and nanoelectromechanical systems [5]. The second version of this preprint was withdrawn, so its results are not relied on here; the entry is cited only for the observation that explicitly solvable non-harmonic spectra of this coupled class are the natural next test bed for the fixed-point claim of Section 4.1, which is proved here only for the harmonic oscillator.

**[6] Relaxation of excited qubit states in silicon quantum dots.** The work treats relaxation of orbital, valley, and spin excited states in single-electron silicon dots, reporting that relaxation times depend sensitively on dot size and external magnetic field, and comparing its spin-relaxation theory against measured $T_{1}$ data at magnetic fields between 1 and 2 T, where the data appear to follow a $B^{-7}$ rate [6]. This provides the empirical class of systems against which the predicted $n$-dependence of relaxation times (Section 4.3) can be confronted: the theory here predicts relaxation that accelerates with excitation, and any measured opposite trend in a comparable platform would falsify the linear-drag model.

**[7] Hydrodynamic attractor in periodically driven ultracold quantum gases.** The work extends hydrodynamic attractors to periodically driven systems, showing that attractor behavior—rapid hydrodynamization far from local equilibrium—arises in quantum fluids under external periodic driving, a setting previously explored only for monotonic expansion [7]. This parallels the present picture of measurement-like driving steering a quantum fluid toward stationary attractor densities, and it demonstrates that attractor dynamics under driving is an established phenomenon in quantum fluids rather than an artifact of heavy-ion kinetics alone.

**[8] Prior version of this program.** The published predecessor states the same core results that Sections 4.1–4.5 here re-derive with corrections: eigenstate densities as exact fixed points of the damped flow, linearized decay at rate $\gamma/2$ with crossover at $\gamma=\hbar k^{2}/m$, the relaxation law with $t_{1\to0}=0.549306/\gamma$, and the limitation that the attractivity argument establishes convergence to the fixed-point set but not to a unique eigenstate [8]. The two errors identified in that version—the unsupported global Lyapunov claim and the overdamped/underdamped inconsistency—are corrected in this revision.

**[9] Hydrodynamic stability hypothesis.** The work identifies a "chronological fallacy" in quantum foundations—the axiomatization of quantum mechanics by von Neumann (1932) predating the rigorous formulation of classical probability by Kolmogorov (1933)—and proposes a hybrid model in which the system is a continuous fluid that appears discrete because it is observed only after settling into stable resonant modes, and it issues a call for weak energy tomography on a hydrogen superposition as the decisive experiment [9]. This supplies the interpretive frame for the present program: quantization as a measurement-induced stability phenomenon rather than an intrinsic discreteness of nature, and a concrete proposed experiment aimed at the same continuous-versus-discrete question.

**[10] Pre-registered falsification of deterministic relaxation.** The work reports a pre-registered simulation testing whether deterministic measurement-triggered relaxation toward eigenstate basins can reproduce the Born probabilities of a two-level system; all seven configurations produced the verdict FAIL with a maximum deviation of $0.5$ against a tolerance of $10^{-2}$, because a deterministic map from a fixed initial state always produces the same trajectory and hence the same outcome, yielding a degenerate outcome channel with probabilities of only $0$ or $1$ [10]. The work concludes that any hydrodynamic account of measurement must add an ensemble over initial states, stochastic dynamics, or contextual hidden variables. This negative result is incorporated directly: it converts the Born rule from a hoped-for derivation into a mandatory, explicitly labeled ensemble assumption (Assumption B, Section 4.7), and it defines the structural shape of the program's remaining open problem.

## 3. Methods

### 3.1 The Madelung formulation

Writing the wavefunction as $\psi(\mathbf{x},t)=\sqrt{\rho(\mathbf{x},t)}\,e^{iS(\mathbf{x},t)/\hbar}$ and substituting into the Schrödinger equation $i\hbar\,\partial_t\psi=\hat{H}\psi$ with $\hat{H}=-\frac{\hbar^{2}}{2m}\nabla^{2}+V$ yields the Madelung system

$$
\partial_t\rho+\nabla\!\cdot\!(\rho\,\mathbf{v})=0, \tag{M1}
$$

$$
\partial_t S+\frac{m}{2}|\mathbf{v}|^{2}+V+Q=0, \tag{M2}
$$

where $\mathbf{v}=\nabla S/m$ and the quantum potential is

$$
Q(\mathbf{x},t)\equiv-\frac{\hbar^{2}}{2m}\frac{\nabla^{2}\sqrt{\rho}}{\sqrt{\rho}}.
$$

Taking the gradient of (M2) gives the Newton-like equation

$$
m(\partial_t+\mathbf{v}\!\cdot\!\nabla)\mathbf{v}=-\nabla(V+Q).
$$

The Madelung form is mathematically equivalent to the Schrödinger equation for single-valued, node-free densities; its value here is that dissipation can be added as a local fluid force without leaving the hydrodynamic picture.

### 3.2 The dissipative extension

We introduce a minimal linear drag term in the Newtonian form:

$$
m(\partial_t+\mathbf{v}\!\cdot\!\nabla)\mathbf{v}=-\nabla\!\bigl(V+Q\bigr)-m\gamma\,\mathbf{v},\qquad\gamma>0. \tag{M2-d}
$$

The continuity equation (M1) remains unchanged, so the total probability $\int\rho\,d^{3}x$ is conserved exactly. Because stationary eigenstates satisfy $\mathbf{v}=0$, the drag term vanishes there, which is the mechanism preserving eigenstate densities as exact fixed points. Throughout the analysis we use dimensionless units $\hbar=m=\omega=1$ unless SI values are stated explicitly; the electron mass $m_e=9.109\times10^{-31}\,\mathrm{kg}$, Boltzmann constant $k_{B}=1.381\times10^{-23}\,\mathrm{J\,K^{-1}}$, temperature $T=300\,\mathrm{K}$, and $\hbar=1.055\times10^{-34}\,\mathrm{J\,s}$ appear in the numerical instances.

The drag coefficient $\gamma$ is phenomenological. Its microscopic origin—whether it derives from environmental coupling, an effective measurement back-action, or an internal fluid viscosity—is not derived here and is listed as an open question in Section 6.

### 3.3 Numerical protocol (specified, not executed)

No simulations are reported in this paper. The proposed protocol would:

- Propagate the damped Madelung fluid through a double-slit potential and verify continuous deterministic trajectories and Born-rule endpoint statistics under an explicitly specified ensemble over initial conditions.
- Propagate a spin-fluid analogue through a Stern–Gerlach field gradient and verify convergence to two spatially separated attractor basins.
- Falsify the continuity hypothesis if any trajectory discontinuity or step-size-sensitive statistics are observed, and falsify Assumption B if the endpoint statistics deviate from Born-rule weights at fixed dynamics.

The ensemble specification is not optional: as the pre-registered falsification establishes, a deterministic map from a fixed initial state yields a degenerate outcome channel and cannot produce fractional probabilities at all [10]. Any execution of this protocol must therefore define the initial-condition ensemble before statistics can be meaningfully compared with the Born rule.

## 4. Analysis

All inputs are either structural equations from Section 3 or explicitly stated assumptions. Every number is computed step by step.

### 4.1 Exact quantum potential of the oscillator ground state

**Input 1.** Harmonic potential $V(x)=\tfrac12 m\omega^{2}x^{2}$ and ground-state density $\rho_{0}(x)=\frac{1}{\sqrt{\pi}\sigma}\,e^{-x^{2}/\sigma^{2}}$ with $\sigma^{2}=\hbar/(m\omega)$.

$$
\sqrt{\rho_{0}}\propto e^{-x^{2}/(2\sigma^{2})},\qquad
\frac{d^{2}}{dx^{2}}\sqrt{\rho_{0}}=\Bigl(\frac{x^{2}}{\sigma^{4}}-\frac{1}{\sigma^{2}}\Bigr)\sqrt{\rho_{0}}.
$$

Hence

$$
Q_{q}=-\frac{\hbar^{2}}{2m}\Bigl(\frac{x^{2}}{\sigma^{4}}-\frac{1}{\sigma^{2}}\Bigr)
=\frac{\hbar^{2}}{2m\sigma^{2}}-\frac{\hbar^{2}x^{2}}{2m\sigma^{4}}.
$$

Substituting $\sigma^{2}=\hbar/(m\omega)$:

$$
\frac{\hbar^{2}}{2m\sigma^{2}}=\frac{\hbar^{2}}{2m}\cdot\frac{m\omega}{\hbar}=\frac{\hbar\omega}{2},\qquad
\frac{\hbar^{2}}{2m\sigma^{4}}=\frac{\hbar^{2}}{2m}\cdot\frac{m^{2}\omega^{2}}{\hbar^{2}}=\frac{m\omega^{2}}{2},
$$

so

$$
Q_{q}(x)=\frac{\hbar\omega}{2}-\frac{m\omega^{2}x^{2}}{2}.
$$

With $S_{0}=\text{const}$ the Hamilton–Jacobi equation (M2) requires $V+Q_{q}=E_{0}$; indeed

$$
V+Q_{q}=\frac{m\omega^{2}x^{2}}{2}+\frac{\hbar\omega}{2}-\frac{m\omega^{2}x^{2}}{2}
=\frac{\hbar\omega}{2}=E_{0}.
$$

Thus the ground state is an exact fixed point of the flow, with or without drag, because $\mathbf{v}=0$ makes the drag term vanish identically. The same argument applies to any eigenstate density $\rho_{n}$ with $\mathbf{v}=0$: the drag term vanishes and the undragged Madelung equations are satisfied exactly. The fixed-point property therefore holds for the full oscillator spectrum, though the explicit closed-form check above is carried out only for $n=0$.

### 4.2 Linearized attractor dynamics

**Input 2.** Perturb $\rho=\rho_{0}(1+\eta)$, $\mathbf{v}=\delta\mathbf{u}$, with $\eta\ll1$. To first order the quantum-potential perturbation is $\delta Q_{q}=-(\hbar^{2}/4m)\nabla^{2}\eta$. For a plane wave $\eta\propto e^{i(kx-\Omega t)}$, $\delta Q_{q}=(\hbar^{2}k^{2}/4m)\eta$. The linearized equations are

$$
\partial_t\eta+\partial_x\delta u_x=0,\qquad
m\partial_t\delta u_x=-\partial_x\delta Q_{q}-m\gamma\,\delta u_x.
$$

Fourier substitution $\eta\to\eta\,e^{i(kx-\Omega t)}$, $\delta u_x\to\delta u_x\,e^{i(kx-\Omega t)}$ yields

$$
-i\Omega\eta+ik\,\delta u_x=0\;\Rightarrow\;\delta u_x=\frac{\Omega}{k}\eta,
$$

$$
-i m\Omega\frac{\Omega}{k}\eta=-ik\frac{\hbar^{2}k^{2}}{4m}\eta-m\gamma\frac{\Omega}{k}\eta.
$$

Cancelling common factors gives the quadratic dispersion relation

$$
\Omega^{2}+i\gamma\Omega-\frac{\hbar^{2}k^{4}}{4m^{2}}=0,
$$

with solutions

$$
\Omega=-\frac{i\gamma}{2}\pm\sqrt{\frac{\hbar^{2}k^{4}}{4m^{2}}-\frac{\gamma^{2}}{4}}.
$$

Every mode therefore decays as $e^{-\gamma t/2}$; the oscillation frequency $\omega_{k}=\sqrt{\hbar^{2}k^{4}/(4m^{2})-\gamma^{2}/4}$ is real (underdamped) when $\gamma<\hbar k^{2}/m$ and imaginary (overdamped) otherwise. Since $\operatorname{Im}\Omega=-\gamma/2<0$ for all $k$ when $\gamma>0$, the ground-state density is linearly stable for every wavenumber.

**Scope of this result.** This is a local linear stability statement about perturbations of a fixed eigenstate density. It establishes attractivity of the fixed-point set in its linear neighborhood; it does not establish global contractivity of the flow, does not exclude other attractors far from the fixed point, and does not determine which eigenstate a given initial condition relaxes to. The previous version's claim of a global Lyapunov contractivity proof is retracted: no such construction was given, and the Limitations of that version already acknowledged that only attractivity of the fixed-point set was supported.

**Numerical instance.** Take $\gamma=10^{9}\,\mathrm{s^{-1}}$, $k=10^{7}\,\mathrm{m^{-1}}$, $m=m_{e}=9.109\times10^{-31}\,\mathrm{kg}$.

Amplitude decay time:

$$
\tau_{\mathrm{lin}}=\frac{2}{\gamma}=\frac{2}{10^{9}}=2.0\times10^{-9}\,\mathrm{s}.
$$

Crossover frequency:

$$
\frac{\hbar k^{2}}{m}= \frac{1.055\times10^{-34}\times(10^{7})^{2}}{9.109\times10^{-31}}
=\frac{1.055\times10^{-34}\times10^{14}}{9.109\times10^{-31}}
=\frac{1.055\times10^{-20}}{9.109\times10^{-31}}
=1.16\times10^{10}\,\mathrm{s^{-1}}.
$$

Since $10^{9}<1.16\times10^{10}$, the mode is underdamped, with

$$
\omega_{k}\approx\frac{\hbar k^{2}}{2m}=\frac{1.16\times10^{10}}{2}=5.8\times10^{9}\,\mathrm{rad\,s^{-1}}.
$$

This classification is used consistently in Section 4.5.

### 4.3 Energy decay and level-to-level relaxation

**Input 3.** For a particle obeying the damped Newtonian equation $m\ddot{x}+m\gamma\dot{x}+m\omega^{2}x=0$, the mechanical energy $E=\tfrac12 m\dot{x}^{2}+\tfrac12 m\omega^{2}x^{2}$ satisfies

$$
\frac{dE}{dt}=m\dot{x}\ddot{x}+m\omega^{2}x\dot{x}
=\dot{x}(-m\gamma\dot{x}-m\omega^{2}x)+m\omega^{2}x\dot{x}
=-m\gamma\dot{x}^{2}.
$$

Averaging over an orbit for weak damping ($\gamma\ll\omega$) gives $\langle\dot{x}^{2}\rangle=E/m$, so

$$
\frac{dE}{dt}=-2\gamma E\quad\Longrightarrow\quad
E(t)=E_{0}\,e^{-2\gamma t}. \tag{D1}
$$

This derivation is valid only under orbit averaging and only for $\gamma\ll\omega$; strong damping requires the full linearized analysis of Section 4.2.

**Input 4.** Eigenenergies $E_{n}=\hbar\omega\left(n+\tfrac12\right)$. Identifying the relaxation of an excited fluid packet with the decay of its excess mechanical energy is a projection approximation, not a derivation from the field equations; it is the working hypothesis under test. Solving $E_{n}e^{-2\gamma t}=E_{n-1}$ for the relaxation time yields

$$
t_{n\to n-1}=\frac{1}{2\gamma}\ln\frac{E_{n}}{E_{n-1}}
=\frac{1}{2\gamma}\ln\frac{n+\tfrac12}{\,n-\tfrac12\,}.
$$

For $n=1$:

$$
t_{1\to0}=\frac{\ln 3}{2\gamma}= \frac{1.098612}{2\gamma}= \frac{0.549306}{\gamma}.
$$

For $n=2$:

$$
\ln\frac{5}{3}=\ln(1.666667)=0.510826\;\Rightarrow\;
t_{2\to1}= \frac{0.510826}{2\gamma}= \frac{0.255413}{\gamma}.
$$

Relaxation accelerates with excitation because the logarithmic factor $\ln[(n+\tfrac12)/(n-\tfrac12)]$ shrinks as $n$ grows; in the large-$n$ limit it scales as $1/n$, so $t_{n\to n-1}\sim 1/(2\gamma n)$.

**Two-mode instance.** With $\omega=10^{12}\,\mathrm{rad\,s^{-1}}$, $\gamma=10^{9}\,\mathrm{s^{-1}}$ (so $\gamma/\omega=10^{-3}\ll1$, consistent with the weak-damping condition):

$$
\tau_{E}=1/\gamma=1.0\times10^{-9}\,\mathrm{s}=1.0\,\mathrm{ns},
$$

$$
\Delta E=\hbar\omega=1.055\times10^{-34}\times10^{12}=1.055\times10^{-22}\,\mathrm{J}.
$$

Converting to electronvolts, $1\,\mathrm{eV}=1.602\times10^{-19}\,\mathrm{J}$:

$$
\Delta E=\frac{1.055\times10^{-22}}{1.602\times10^{-19}}\,\mathrm{eV}=6.58\times10^{-4}\,\mathrm{eV}=0.658\,\mathrm{meV}.
$$

### 4.4 Per-period phase-space contraction

**Input 5.** For weak damping $\gamma/\omega=0.01$, the period $T=2\pi/\omega$ gives a contraction factor for the phase-space area element under the damped flow:

$$
e^{-2\gamma T}=e^{-2\gamma\frac{2\pi}{\omega}}=e^{-2\pi\times0.01}=e^{-0.125664}=0.881911.
$$

The radial contraction per period is $e^{-\gamma T}=e^{-0.062832}=0.939101$. After $k=10$ periods:

$$
e^{-2\pi\cdot10\cdot0.01}=e^{-0.628319}=0.533488.
$$

This contraction is computed for the classical damped oscillator flow; it quantifies the local phase-space squeezing that underlies the attractor picture but is not, by itself, a global contractivity proof.

### 4.5 Timescale comparison: relaxation versus diffusion (corrected)

**Input 6.** The previous version computed the diffusion time "in the overdamped limit" using the Einstein relation at $\gamma=10^{9}\,\mathrm{s^{-1}}$, while Section 4.2 classifies the same parameters as underdamped because $\hbar k^{2}/m=1.16\times10^{10}\,\mathrm{s^{-1}}>\gamma$. That inconsistency is resolved here in favor of the crossover calculation: at these parameters the fluid is underdamped, the Einstein relation $D=k_{B}T/(m\gamma)$ is not derived from the damped Madelung equations in this regime, and the following diffusion estimate is a phenomenological order-of-magnitude comparison only, not a prediction of the model.

With $k_{B}=1.381\times10^{-23}\,\mathrm{J\,K^{-1}}$, $T=300\,\mathrm{K}$, $m=m_{e}$, $\gamma=10^{9}\,\mathrm{s^{-1}}$:

$$
k_{B}T=1.381\times10^{-23}\times300=4.143\times10^{-21}\,\mathrm{J},
$$

$$
m\gamma=9.109\times10^{-31}\times10^{9}=9.109\times10^{-22}\,\mathrm{kg\,s^{-1}},
$$

$$
D=\frac{4.143\times10^{-21}}{9.109\times10^{-22}}=4.55\,\mathrm{m^{2}\,s^{-1}}.
$$

Diffusion time across $L=1\,\mu\mathrm{m}=10^{-6}\,\mathrm{m}$:

$$
t_{D}=\frac{L^{2}}{D}=\frac{10^{-12}}{4.55}=2.2\times10^{-13}\,\mathrm{s}.
$$

Hence the phenomenological diffusion time is far shorter than the energy-relaxation time $\tau_{E}=1.0\times10^{-9}\,\mathrm{s}$, with ratio

$$
\frac{\tau_{E}}{t_{D}}=\frac{1.0\times10^{-9}}{2.2\times10^{-13}}=4.5\times10^{3}.
$$

The comparison indicates that, if a diffusive channel of this magnitude existed, spatial spreading would outrun energetic relaxation by about three orders of magnitude. Whether such a channel exists in the underdamped regime—and what its true coefficient is—remains open; the number above is a bound derived from an Einstein relation whose validity here is assumed, not established.

### 4.6