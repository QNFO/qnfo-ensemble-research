# Quantization as Hydrodynamic Relaxation: Eigenstates as Attractor Basins in a Dissipative Madelung Fluid

## Abstract

We propose and partially develop a research program in which quantum jumps are reinterpreted as continuous, deterministic relaxation events in the Madelung hydrodynamic picture of quantum mechanics. In this picture the wavefunction is rewritten as a fluid with density $\rho$ and velocity field $\mathbf{v} = \nabla S / m$, and we add a linear dissipative term to the quantum Hamilton-Jacobi equation so that the resulting flow is contractive. We argue that Hamiltonian eigenstates then play the role of attractors: basins of attraction of a stable phase flow, with "quantization" emerging through measurement-induced stability rather than being an intrinsic, primitive feature of nature. We derive the relaxation dynamics explicitly, show by a Lyapunov-type energy argument that stationary eigenstate densities are the only fixed points of the damped flow, and compute concrete relaxation timescales in dimensionless units: the energy-decay law $E(t) = E_0 e^{-2\gamma t}$, the level-to-level relaxation time $t_{n \to n-1} = \ln\!\big[(n+\tfrac{1}{2})/(n-\tfrac{1}{2})\big]/(2\gamma)$, and the per-period phase-space contraction factor $e^{-2\pi\gamma/\omega}$. We connect the program to rigorous relaxation-limit results in quantum hydrodynamics and to hydrodynamic attractors in kinetic theory, and we specify a falsification protocol based on double-slit and Stern-Gerlach-type numerical experiments. The Born-rule statistics of outcomes remain an open, explicitly labeled assumption of the framework rather than a derived result.

## 1. Introduction

The standard interpretation of quantum mechanics treats measurement as a discontinuous, fundamentally stochastic event: the "collapse" of the wavefunction onto an eigenstate. This discontinuity sits awkwardly beside the continuous, deterministic unitary evolution that governs everything else, and it has motivated a century of interpretational work. The research program developed here takes a different route. It begins from the Madelung formulation, in which the Schrödinger wavefunction $\psi$ is written as $\psi = \sqrt{\rho}\, e^{iS/\hbar}$, so that quantum dynamics becomes the dynamics of a compressible, irrotational fluid with density $\rho$ and velocity $\mathbf{v} = \nabla S / m$. In this fluid picture, we add a minimal dissipative term to the quantum Hamilton-Jacobi equation. The claim we investigate is:

**Central hypothesis (H).** With a suitable dissipative term, the Madelung flow is contractive, and each Hamiltonian eigenstate is a basin of attraction of this flow. A "quantum jump" is then not a fundamental discontinuity but a continuous, deterministic relaxation event: the fluid flowing downhill into the nearest eigenstate basin. Quantization — the discreteness of outcomes — is a property of the attractor landscape stabilized by measurement-like perturbations, not an intrinsic primitive of nature.

If H is correct, it re-grounds quantum mechanics in classical measure theory: probability enters as ordinary measure over initial conditions in phase space, in the spirit of Kolmogorov, rather than as an irreducible postulate. Wavefunction collapse dissolves into relaxation.

The program has three methodological pillars, which structure this paper:

1. **Derivation** (Section 3): write the Madelung equations, add a dissipative term, and obtain closed-form relaxation laws.
2. **Stability** (Section 4): prove, at the level of a Lyapunov energy argument, that eigenstate densities are the only fixed points and that the flow contracts toward them; compute explicit timescales and contraction factors.
3. **Falsification protocol** (Sections 5 and 6): specify numerical double-slit and Stern-Gerlach-type experiments in which trajectories must converge to discrete outcomes while remaining continuous and deterministic throughout, and state in advance what result would falsify H.

We are explicit about what this paper does and does not establish. It establishes the relaxation dynamics and the fixed-point structure analytically, in dimensionless units. It does **not** derive the Born rule; the claim that relaxation endpoints are sampled with Born-rule weights over initial conditions is carried as a labeled assumption throughout, and its failure is one of the primary falsifiers of the program.

## 2. Background and Related Work

We review the literature supplied with this proposal, in the fixed bibliography order. Three entries ([9], [10], [11]) are QNFO corpus items whose supplied summaries contain no substantive text; we say so explicitly and use them only as pointers to related internal work.

**[1] Affine quantization (arXiv:2108.04083v1).** This work contrasts canonical quantization, built on the commutator $[Q,P]=i\hbar\,1\!\!1$, with affine quantization, built on $[Q,D]=i\hbar\,Q$ where $D \equiv (PQ+QP)/2$. Its central observation is that canonical operators must fit $-\infty < P, Q < \infty$, while affine quantization accommodates half-line or punctured-line domains for $Q$, such as $0 < Q < \infty$. This is directly relevant to our program: the Madelung density $\rho$ is non-negative by construction, so the configuration variable of a hydrodynamic re-foundation of quantum mechanics naturally lives on a domain where affine-type quantization, not canonical quantization, is the appropriate algebraic starting point. The summary supplied also indicates that affine quantization is proposed as relevant even for quantum gravity, suggesting the algebraic flexibility we invoke is not limited to toy domains.

**[2] Tianyan quantum cloud platform (arXiv:2512.10504v2).** This entry describes a cloud-accessible superconducting quantum prototype, Tianyan-287, with 105 qubits and operational fidelities of 99.90% (single-qubit gates), 99.56% (two-qubit gates), and 98.7% (readout). We cite it as evidence of the experimental infrastructure context in which any alternative account of measurement must ultimately be tested: a deterministic-relaxation account of measurement must be compatible with devices whose readout fidelity is already at the $98.7\%$ level. The entry supplies no further theoretical detail, and we draw no dynamical claims from it.

**[3] Time-relaxation limit for quantum hydrodynamics (arXiv:2412.16800v2).** This is the closest rigorous anchor for our program. The paper analyzes weak solutions of the quantum hydrodynamics (QHD) system with a collisional term on the one-dimensional torus and rigorously proves a time-relaxation limit toward the quantum drift-diffusion (QDD) equation; it also states that global-in-time, finite-energy weak solutions can be proved by straightforward exploitation of the structure (the summary is truncated at this point). For us, this result is a proof of concept that adding collisional/dissipative structure to a quantum hydrodynamic system produces a well-defined relaxation limit rather than pathologies — precisely the mathematical behavior hypothesis H requires, albeit for a different target equation (QDD rather than eigenstate attractors).

**[4] Hydrodynamic attractors for Gubser flow (arXiv:2001.10756v2).** This work solves the Boltzmann equation in the relaxation-time approximation using a hierarchy of angular moments of the distribution function, for an azimuthally symmetric, radially expanding, boost-invariant conformal system undergoing Gubser flow, and compares truncated moment solutions to the exact solution. Its importance for us is conceptual: it demonstrates, in a kinetic setting, that far-from-equilibrium dynamics can exhibit universal attractor behavior in which details of the initial state are rapidly forgotten. Hypothesis H transplants this attractor paradigm from relativistic kinetic theory to the Madelung fluid, with eigenstates replacing hydrodynamic constitutive relations as the attractors.

**[5] Eigenvalues and eigenstates of the quantum Rabi model (arXiv:2104.12771v2).** This paper addresses the analytical solution of the quantum Rabi model, motivated by its widespread use in quantum optics, quantum computing, cavity QED, and nanoelectromechanical systems, and by the need to describe a two-level system interacting with a quantum oscillator when the rotating wave approximation fails. Within our program, the Rabi model is a natural first testbed beyond the harmonic oscillator: it is a system whose discrete two-level structure is emergent from a continuous underlying dynamics, so a hydrodynamic-relaxation account must reproduce its eigenstate basins. The supplied summary describes motivation and context rather than solution techniques, and we rely on it only for that context.

**[6] Quantum simulation of nuclear dynamics in first quantization (arXiv:2507.22814v3).** This entry notes that real-time nuclear dynamics underpins predictions of cross sections relevant to terrestrial experiments and astrophysics, and that first-principles simulation is hindered by exponential classical cost, motivating scalable quantum simulation. Its relevance is as a stress-test domain: nuclear dynamics involves real-time scattering and transition events that a relaxation picture must re-describe as continuous flow between basins. The summary supplies no methodological detail beyond this motivation, and we use it only to identify the application class.

**[7] Relaxation of excited qubit states in silicon quantum dots (arXiv:1301.0260v2).** This work treats relaxation physics of low-lying excited states — orbital, valley, and spin — in ideal single-electron silicon quantum dots for quantum computing, noting that relaxation times depend sensitively on dot size and external magnetic field, and that orbital relaxation times are generally short (the summary truncates here). This is the experimental face of relaxation in real quantum systems: excited states genuinely decay, with system-parameter-dependent timescales. Our program makes a strong structural claim about such decay — that it is the same continuous relaxation mechanism that constitutes measurement — and therefore must confront the measured parameter dependence of relaxation times in devices of this type.

**[8] Hydrodynamic attractor in periodically driven ultracold quantum gases (arXiv:2501.19240v2).** This paper states that hydrodynamic attractors are a universal phenomenon of strongly interacting systems describing hydrodynamic-like evolution far from local equilibrium, that rapid hydrodynamization of the Quark-Gluon Plasma underlies the success of hydrodynamic models of high-energy nuclear collisions, and that hydrodynamic attractors had so far been explored only in systems undergoing monotone (the summary truncates; the title indicates periodic driving). This is the most direct precedent for hypothesis H's central move: attractor behavior in a quantum fluid under external driving. Extending attractor phenomenology from monotone to periodically driven quantum gases supports the plausibility that measurement-like, time-dependent perturbations can generate stable attractor basins in a Madelung fluid.

**[9] QNFO: Hydrodynamic Stability Hypothesis.** The supplied entry contains no summary text. We note it as an internal corpus item presumably related to the stability analysis of Section 4, but no claim about its content can be made from the supplied material.

**[10] QNFO: A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation.** The supplied entry likewise contains no summary text. Its title indicates that a pre-registered falsification protocol for deterministic measurement-triggered relaxation exists in the corpus; this aligns with the falsification protocol of Section 5, but we cannot attribute any specific content to it from the supplied entry.

**[11] QNFO: Hydrodynamic-Topological Continuum.** The supplied entry contains no summary text. Its title suggests a related continuum formulation combining hydrodynamic and topological structure; again, no substantive claim is drawn from it.

In summary, the supplied literature provides (i) rigorous precedent for dissipative relaxation limits in quantum hydrodynamic systems [3], (ii) an established attractor paradigm in classical and quantum hydrodynamics [4, 8], (iii) an algebraic framework suited to the non-negative density domains of a hydrodynamic picture [1], and (iv) experimental and application contexts in which relaxation and discrete outcomes coexist [2, 5, 6, 7]. What is missing — and what this paper supplies in preliminary form — is the specific identification of Hamiltonian eigenstates as attractor basins of a damped Madelung flow.

## 3. Methods

### 3.1 The Madelung formulation

Write the wavefunction in polar form:

$$\psi(\mathbf{x}, t) = \sqrt{\rho(\mathbf{x}, t)}\, e^{i S(\mathbf{x}, t)/\hbar},$$

where $\rho \geq 0$ is the position density and $S$ is the phase action. Substituting into the Schrödinger equation $i\hbar\, \partial_t \psi = \hat{H} \psi$ with $\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{x})$ and separating real and imaginary parts yields the Madelung system:

$$\partial_t \rho + \nabla \cdot (\rho \mathbf{v}) = 0, \tag{M1}$$

$$\partial_t S + \frac{m}{2} |\mathbf{v}|^2 + V + Q = 0, \tag{M2}$$

where $\mathbf{v} = \nabla S / m$ and

$$Q(\mathbf{x}, t) \equiv -\frac{\hbar^2}{2m} \frac{\nabla^2 \sqrt{\rho}}{\sqrt{\rho}}$$

is the quantum potential — the only place $\hbar$ enters the fluid equations beyond the definition of $\mathbf{v}$. Equation (M1) is an ordinary continuity equation; equation (M2) is a quantum Hamilton-Jacobi equation. Taking $\nabla$ of (M2) gives a Newton-like form $m(\partial_t + \mathbf{v}\cdot\nabla)\mathbf{v} = -\nabla(V + Q)$.

### 3.2 The dissipative extension

We add the minimal linear dissipative term to (M2), following the relaxation-time pattern familiar from kinetic theory [4]:

$$\partial_t S + \frac{m}{2} |\mathbf{v}|^2 + V + Q = -\hbar\,\gamma\, \Phi[S], \tag{M2-d}$$

where $\gamma > 0$ is a damping rate and $\Phi[S]$ is a phase-functional to be chosen. We take the simplest choice consistent with relaxation toward stationary phase configurations:

$$\Phi[S] \equiv \frac{1}{\hbar}\big(S - S_{\mathrm{ss}}\big),$$

where $S_{\mathrm{ss}}$ is the phase of the nearest stationary (eigenstate) configuration. In the Newtonian form this is equivalent to a friction force $m\, d\mathbf{v}/dt \supset -m\gamma\, \mathbf{v}$ acting along the flow. The continuity equation (M1) is left untouched: the fluid is damped, not leaked. All analysis below is performed in dimensionless units $\hbar = m = \omega = 1$ unless stated otherwise.

### 3.3 Numerical protocol (specified, not yet executed)

No simulation results are reported in this paper. We specify the protocol that will be executed and pre-registered:

- **Double-slit test:** propagate the damped Madelung fluid through a double-slit potential in two dimensions; verify that individual trajectories remain continuous and deterministic for all $t$, and that the endpoint distribution over detectors converges to the interference pattern.
- **Stern-Gerlach test:** propagate a spin-fluid analogue through a field gradient; verify convergence to two spatially separated attractor basins.
- **Falsifier:** if trajectories exhibit any discontinuity, any sensitivity to integration step size in the endpoint distribution beyond numerical tolerance, or endpoint statistics that are stable across initial-condition ensembles but inconsistent with Born weights, hypothesis H fails in its current form.

## 4. Analysis

All inputs in this section are either (a) structural equations from Section 3, or (b) explicitly stated dimensionless assumptions. Every number below is computed here, step by step. No empirical data are used.

### 4.1 Energy decay law of the damped oscillator

**Input 1 (assumption, dimensionless units):** harmonic potential $V = \frac{1}{2}\omega^2 x^2$ with $\omega = 1$, damping rate $\gamma$.

Under linear friction $m\dot{v} \supset -m\gamma v$, the mechanical energy $E = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}m\omega^2 x^2$ obeys:

$$\frac{dE}{dt} = m\dot{x}\ddot{x} + m\omega^2 x \dot{x} = \dot{x}\big(m\ddot{x} + m\omega^2 x\big) = \dot{x}\big(-m\gamma \dot{x}\big) = -2\gamma \cdot \tfrac{1}{2} m \dot{x}^2 \leq -2\gamma \cdot 0.$$

More precisely, $dE/dt = -m\gamma \dot{x}^2$, and averaging over a period for weak damping ($\gamma \ll \omega$) gives $\langle \dot{x}^2 \rangle = E/m$ (equipartition within the orbit), hence:

$$\frac{dE}{dt} = -2\gamma E \quad \Longrightarrow \quad E(t) = E_0\, e^{-2\gamma t}. \tag{D1}$$

This is the Lyapunov function of the theory: $E$ is strictly decreasing except at fixed points, so the flow is contractive and can only settle at minima of the effective energy landscape.

### 4.2 Eigenstates as the only fixed points

**Input 2 (structural):** a stationary eigenstate of $\hat{H}$ has $\rho_n = |\psi_n|^2$ time-independent and $S_n = -E_n t + \sigma_n(\mathbf{x})$ with time-independent reduced phase $\sigma_n$.

At a fixed point of the damped flow, (M1) requires $\nabla \cdot (\rho \mathbf{v}) = 0$ and (M2-d) with $\partial_t S = -E$ requires:

$$E = \frac{m}{2}|\mathbf{v}|^2 + V + Q + \hbar\gamma\,\Phi[S].$$

For bound states with nodes, the only nonsingular stationary density compatible with (M1) and the single-valuedness of $S$ is an eigenstate density $\rho_n$ (this is the standard stationary-state correspondence of the Madelung picture, here inherited unchanged since we did not modify (M1)). The damping term does not create new fixed points; it only makes the fixed points attractive rather than neutrally stable. Formally: define the Lyapunov functional

$$\mathcal{L}[\rho, S] \equiv E[\rho, S] + \hbar\gamma \int \frac{(S - S_{\mathrm{ss}})^2}{2\hbar^2}\, \rho\, d^dx,$$

with $d\mathcal{L}/dt \leq 0$ by construction of (M2-d) (each contribution to $dE/dt$ from the damping is negative semidefinite, as in Eq. (D1)). Equality holds only on the stationary set. Hence every initial condition flows to some eigenstate basin — this is the precise sense in which eigenstates are attractors under H.

### 4.3 Level-to-level relaxation time

**Input 3 (structural):** harmonic oscillator eigenenergies $E_n = \hbar\omega(n + \tfrac{1}{2})$, $n = 0, 1, 2, \dots$; in dimensionless units $E_n = n + \tfrac{1}{2}$.

Using the decay law (D1), the time to relax from level $n$ to level $n-1$ is the time for $E$ to fall from $E_n$ to $E_{n-1}$:

$$E_{n-1} = E_n\, e^{-2\gamma t_{n \to n-1}} \quad \Longrightarrow \quad t_{n \to n-1} = \frac{1}{2\gamma} \ln\frac{E_n}{E_{n-1}} = \frac{1}{2\gamma} \ln\frac{n + \tfrac{1}{2}}{n - \tfrac{1}{2}}.$$

**Concrete computation (headline number).** For the first transition, $n = 1$:

$$t_{1 \to 0} = \frac{1}{2\gamma} \ln\frac{1 + \tfrac{1}{2}}{1 - \tfrac{1}{2}} = \frac{1}{2\gamma} \ln\frac{3/2}{1/2} = \frac{1}{2\gamma} \ln 3.$$

With $\ln 3 = 1.098612\ldots$:

$$t_{1 \to 0} = \frac{1.098612}{2\gamma} = \frac{0.549306}{\gamma}. \tag{R1}$$

For $n = 2$: $t_{2 \to 1} = \frac{1}{2\gamma}\ln\frac{5/2}{3/2} = \frac{1}{2\gamma}\ln\frac{5}{3} = \frac{0.510826}{2\gamma}\cdot 2 = \frac{0.255413}{\gamma}\cdot\frac{1}{1}\cdot$ — carrying the arithmetic explicitly: $\ln(5/3) = \ln 5 - \ln 3 = 1.609438 - 1.098612 = 0.510826$, so

$$t_{2 \to 1} = \frac{0.510826}{2\gamma} = \frac{0.255413}{\gamma}. \tag{R2}$$

Note the structural prediction: relaxation accelerates at higher excitation ($t_{2\to1} < t_{1\to0}$), since the fractional energy gap $\ln(E_n/E_{n-1})$ shrinks with $n$. This $n$-dependence is a sharp, falsifiable signature of the linear-damping model, directly testable against the parameter-dependent relaxation times measured in systems such as silicon quantum dots [7].

### 4.4 Per-period phase-space contraction

**Input 4 (assumption):** weak damping $\gamma/\omega \ll 1$; over one oscillator period $T = 2\pi/\omega$, the amplitude of the classical damped oscillator contracts by $e^{-\gamma T}$ in each of position and momentum, i.e., the phase-space area element contracts by $e^{-2\gamma T}$.

**Concrete computation.** Take the illustrative ratio $\gamma/\omega = 0.01$. Then:

$$\gamma T = \gamma \cdot \frac{2\pi}{\omega} = 2\pi \cdot 0.01 = 0.062832,$$

$$e^{-2\gamma T} = e^{-0.125663} = 0.881895. \tag{R3}$$

So each period, the phase-space area occupied by a basin-crossing ensemble shrinks by a factor of approximately $0.8819$; equivalently, the radial contraction per period is $e^{-\gamma T} = e^{-0.062832} = 0.939115$. After $k$ periods the contraction is $e^{-2\pi k \gamma/\omega}$; for $k = 10$:

$$e^{-2\pi \cdot 10 \cdot 0.01} = e^{-0.628319} = 0.533488. \tag{R4}$$

Ten periods suffice to shrink an initial ensemble to about $53.3\%$ of its phase-space area at $\gamma/\omega = 0.01$ — the quantitative content of the claim that measurement-like perturbations induce stability by contraction.

### 4.5 Basin discrimination timescale versus measurement duration

**Input 5 (assumption, for a labeled projection only):** a measurement-like perturbation acts for a duration $\tau_m$; for the relaxation picture to reproduce discrete outcomes, we require $\tau_m \gg t_{1\to0} = 0.549306/\gamma$ (from R1), i.e.,

$$\gamma\, \tau_m \gg 0.549306. \tag{P1}$$

As a labeled projection with stated assumptions: if a device implements effective damping $\gamma = 10^{6}\ \mathrm{s^{-1}}$ (an assumption about the measurement apparatus, not a measurement), then $t_{1\to0} = 0.549306 \times 10^{-6}\ \mathrm{s} = 5.49306 \times 10^{-7}\ \mathrm{s}$, and any perturbation lasting $\tau_m \gg 0.55\ \mu\mathrm{s}$ would drive full relaxation. The uncertainty bound on this projection is entirely the uncertainty in the assumed $\gamma$; the dimensionless coefficient $0.549306$ is exact to the digits shown (from $\ln 3 / 2$).

### 4.6 What is not derived

The Born rule is not derived here. Under H, the endpoint distribution is a measure over initial conditions in the basin; the claim that this measure equals $|\langle \psi_{\mathrm{in}} | \phi_n\rangle|^2$ for the incoming state $\psi_{\mathrm{in}}$ and outcome $\phi_n$ is **Assumption B**, carried openly. Its status and falsification role are discussed in Section 6.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**Result 1 (energy decay).** The damped Madelung fluid obeys $E(t) = E_0\, e^{-2\gamma t}$ (Eq. D1), derived from the linear friction term with the equipartition averaging over an orbit at $\gamma \ll \omega$.

**Result 2 (fixed-point structure).** The damped flow has as fixed points exactly the stationary Madelung configurations (eigenstate densities), which are attractive rather than neutrally stable; the Lyapunov functional $\mathcal{L}$ of Section 4.2 decreases monotonically off the fixed-point set.

**Result 3 (relaxation times).** In dimensionless units:
- $t_{1 \to 0} = 0.549306/\gamma$ (R1),
- $t_{2 \to 1} = 0.255413/\gamma$ (R2),
with the general law $t_{n \to n-1} = \ln\!\big[(n+\tfrac{1}{2})/(n-\tfrac{1}{2})\big]/(2\gamma)$, decreasing in $n$.

**Result 4 (contraction).** At $\gamma/\omega = 0.01$: per-period phase-space area contraction factor $0.881895$ (R3); after 10 periods, $0.533488$ (R4).

**Result 5 (labeled projection).** Under the stated assumption $\gamma = 10^{6}\ \mathrm{s^{-1}}$ for a measurement-like apparatus, full first-level relaxation occurs within $t_{1\to0} = 5.49306 \times 10^{-7}\ \mathrm{s}$, with uncertainty dominated entirely by the assumed $\gamma$ (P1). No experimental data are claimed; this is a design target for the numerical protocol of Section 3.3.

**Result 6 (protocol status).** The double-slit and Stern-Gerlach numerical tests of Section 3.3 are specified but not executed; no simulation outcomes are reported in this paper.

## 6. Discussion

**Limitations of the analysis.** The energy-decay derivation (D1) uses orbit averaging, valid only for $\gamma \ll \omega$; the strong-damping regime, where relaxation may be overdamped and the level-to-level picture may fail, is untreated. The fixed-point argument of Section 4.2 leans on the standard stationary-state correspondence of the undamped Madelung picture and on a specific choice of $\Phi[S]$; other dissipative terms (e.g., nonlinear in $S - S_{\mathrm{ss}}$, or acting on $\rho$) could introduce spurious fixed points or destroy the Lyapunov property. The claim that damping does not create new fixed points is argued, not proven, for multi-dimensional and nodal systems; a rigorous proof would need the machinery of the type deployed for QHD relaxation limits on the torus [3], and even [3] proves relaxation to a drift-diffusion equation, not to eigenstate attractors — the analogy should not be overstated.

**The Born rule problem.** Assumption B is the weakest link. Deterministic relaxation maps each initial condition to exactly one endpoint; the endpoint statistics are then fixed by the initial-condition measure. Nothing in Sections 3–5 shows this measure reproduces $|\langle\psi_{\mathrm{in}}|\phi_n\rangle|^2$; a deterministic contraction flow could equally produce statistics tied to basin volumes in a way that generically violates Born weights. If numerical experiments of the Section 3.3 type yield stable, initial-measure-independent endpoint statistics that deviate from Born weights, H is falsified in its strong form. A weaker fallback — relaxation plus explicit classical measure over unknown initial conditions, with Born weights as a measured contingency — would preserve determinism but forfeit the reductive ambition.

**What would falsify the program.** (i) Observation of genuinely discontinuous outcome selection in the numerical protocol (trajectories jumping between basins under refinement). (ii) Endpoint statistics depending on integration step size or on irrelevant details of the damping model — indicating the attractor picture is not well-posed. (iii) Relaxation times inconsistent with the predicted $n$-dependence $t_{n\to n-1} \propto \ln[(n+\tfrac{1}{2})/(n-\tfrac{1}{2})]$ in a clean system where the effective $\gamma$ can be calibrated; the sensitive parameter dependence of relaxation in quantum dots [7] offers both a testing ground and a potential refuter. (iv) Persistence of superposition signatures (e.g., sustained interference) in regimes where the model demands full relaxation.

**Against ourselves.** A skeptic will note three points. First, adding dissipation by hand to a fundamentally unitary theory may simply describe open systems, not measurement: the damped Madelung fluid may be a model of decoherence-adjacent physics, and "measurement" may be nothing more than environmental coupling — in which case the program restates, rather than replaces, standard open-system theory. Second, the hydrodynamic attractor paradigm [4, 8] concerns forgetting of initial details in coarse-grained variables; eigenstate attractors would require the opposite in one respect — fine-grained, state-specific endpoints — and it is unproven that a contractive flow supports that richness. Third, the algebraic domain argument via affine quantization [1] motivates non-negative densities but does not by itself constrain the dynamics; it is scaffolding, not evidence. Finally, the QNFO corpus items [9, 10, 11] carry no supplied content; in particular, the pre-registered falsification suggested by the title of [10] could not be consulted for this draft, and the protocol of Section 3.3 is our own specification, which should be reconciled with that document before execution.

**Open questions.** What is the physical origin and measured value of $\gamma$ in real measurement devices? Can the Born-rule measure be derived from basin geometry, or must it remain an assumption? Does the framework extend to entangled systems, where the Madelung fluid lives in configuration space and "basins" are not spatially local? Can the relaxation-limit technology of [3] be adapted to prove global convergence to eigenstate attractors, closing the gap between our Lyapunov argument and a theorem?

## 7. Conclusion

We have formulated a concrete research program in which quantization is not primitive: Hamiltonian eigenstates are attractor basins of a deterministically relaxing Madelung fluid, and quantum jumps are continuous relaxation events stabilized by measurement-like perturbations. We derived the damped dynamics, established the fixed-point structure via a Lyapunov argument, and computed explicit dimensionless results: the decay law $E(t) = E_0 e^{-2\gamma t}$, relaxation times $t_{1\to0} = 0.549306/\gamma$ and $t_{2\to1} = 0.255413/\gamma$, and per-period phase-space contraction $0.881895$ at $\gamma/\omega = 0.01$. The Born rule remains an explicit, falsifiable assumption rather than a derivation, and the numerical double-slit and Stern-Gerlach protocols are specified but not executed. The program stands or falls on whether deterministic contraction flows can reproduce Born statistics — a question we have