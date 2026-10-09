# The Thermodynamic Wall: Heat Dissipation as a Boundary Condition on Quantum Coherence Time

## Abstract

We introduce the *thermodynamic wall*: a boundary-condition formulation of the trade-off between heat dissipation and quantum coherence time in engineered quantum systems. Just as computational wall models in fluid dynamics encode unresolved near-boundary physics into an enriched boundary treatment, we encode unresolved thermal environments into an effective dissipative wall that imposes a flux constraint on any quantum processor. We derive a closed-form viability window: given a wall with thermal conductance $G_{\mathrm{th}}$ held across a temperature gap $\Delta T$, the maximum sustainable erasure rate is $R_{\max} = G_{\mathrm{th}}\Delta T/(k_B T \ln 2)$, which combined with a bit-erasure cost per logical cycle yields a maximum coherent operation count $N_{\max} = G_{\mathrm{th}}\Delta T\, T_2/(m k_B T \ln 2)$. For a representative cryogenic wall ($G_{\mathrm{th}}\Delta T = 10^{-13}\ \mathrm{W}$, $T = 20\ \mathrm{mK}$, $m = 10^{6}$ erased bits per logical cycle, $T_2 = 1\ \mathrm{s}$) we obtain $N_{\max} \approx 5.23\times 10^{8}$ coherent operations, and a thermal-occupation analysis at $5\ \mathrm{GHz}$ gives $n_{\mathrm{th}} \approx 6.14\times 10^{-6}$ and a thermal error time $\approx 16.3\ \mathrm{s}$. We situate the construction relative to wall modeling via function enrichment, the brick-wall model of black-hole thermodynamics, the analytic range of the heat operator, and the QNFO corpus on ultrametric relaxation and Planckian dissipation. The wall formulation turns dissipation from a nuisance into an explicit design boundary, and we state the conditions under which the resulting bounds would be falsified.

## 1. Introduction

Every quantum computer, sensor, or memory is bounded by two walls. The first is the coherence wall: decoherence processes limit the time $T_2$ over which a quantum state retains phase information. The second is the thermodynamic wall: the physical enclosure that isolates the cold quantum region from the warm classical world can only conduct heat away at a finite rate, and that rate caps how fast information can be reset, measured, and error-corrected. These two walls are usually studied by separate communities — coherence by quantum-information theorists, heat conduction by thermal engineers — but they act jointly, and their product determines whether a proposed architecture can perform a computation of a given depth at all.

The central claim of this paper is that the joint constraint is best expressed as a boundary-condition problem, and that this viewpoint has a productive precedent in computational physics. In turbulent-flow simulation, "wall modeling" replaces the unresolved near-wall region with an enriched boundary treatment so that the interior computation can proceed on coarse meshes [2],[3],[4],[7]. In black-hole thermodynamics, the "brick wall" model places an actual thermodynamic wall just outside a horizon and reads entropy and heat capacity off the wall's boundary condition [6]. In building physics, the wall is literally the dominant element of the thermal budget, and validated conduction models drive design [1]. In each case, the wall is where the resolved system meets an unresolved environment, and the wall's properties — not the interior equations — set the achievable performance. We import this discipline into quantum thermodynamics.

Concretely, we ask: given a wall that can remove heat at power $P_{\mathrm{wall}}$, and a machine whose logical cycles each irreversibly erase $m$ bits, how many coherent operations $N_{\max}$ can the machine perform before either (i) the dissipation budget is exhausted or (ii) thermal excitation of the qubits destroys coherence? We derive the answer in closed form and evaluate it for a representative cryogenic parameter set, with every arithmetic step shown. We also derive the thermal-occupation floor $n_{\mathrm{th}}$ that any wall-cooled qubit inherits, and combine the two into a single viability inequality.

The paper connects to the QNFO research program on thermodynamic viability [10], on ultrametric relaxation dynamics in topological quantum memory [9], and on Planckian dissipation in strongly correlated systems [11]: the thermodynamic wall is the engineered, mesoscopic counterpart of the Planckian dissipation bound that those works locate in correlated matter. The remainder of the paper is organized as follows. Section 2 reviews the related literature. Section 3 defines the model. Section 4 carries out the derivations with full arithmetic. Section 5 reports the results. Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

**Wall modeling via function enrichment.** The methodological core of this paper is borrowed from a line of work in computational fluid dynamics. Krais, Sander, Beck and Gassner [3] introduced wall modeling for RANS (Reynolds-averaged Navier–Stokes) simulation within a high-order discontinuous Galerkin method: instead of imposing wall functions as boundary conditions, they build the near-wall velocity profile into the function space as a local enrichment, so the Galerkin projection automatically selects the best combination of polynomial and enriched shape functions. This is precisely the move we make in Section 3: the unresolved thermal microphysics of the environment is built into an *enriched boundary object* (the thermodynamic wall) rather than modeled in the interior. Krank, Krais, Beck and Wall [4] extended this to hybrid RANS/LES, showing that enrichment overcomes the RANS–LES transition problem and permits coarse meshes near the boundary; the analogue is that our wall formulation lets the quantum modeler ignore microscopic thermal degrees of freedom while retaining the correct flux. Krank and Wall [7] established the base method for incompressible LES, demonstrating that a problem-tailored function space predicts turbulent boundary-layer gradients on very coarse meshes — the direct ancestor of the "coarse interior, enriched boundary" structure we use. Krais et al. [2] further extended the approach to detached-eddy simulation while keeping the full Navier–Stokes equations discretely fulfilled, including pressure gradient and convective terms; the lesson we take is that an enriched wall model must remain consistent with the conservation laws of the interior, which for us means the wall must respect the first and second laws of thermodynamics exactly, even though it resolves none of the environmental microstates.

**The brick wall and black-hole thermodynamics.** Zhu [6] revises the brick-wall method for computing black-hole thermodynamic quantities: a scalar field's contributions to entropy and other thermodynamic quantities are computed by imposing a cutoff wall in Rindler space, with momentum–frequency relations determined numerically to better than $10\%$ accuracy. The brick wall is the cleanest historical example of a *thermodynamic wall*: an artificial boundary whose placement controls the entropy budget of the system. Our construction is the non-relativistic, engineered analogue — the wall placement (i.e., the thermal conductance $G_{\mathrm{th}}$ chosen by the cryogenic engineer) controls the computational entropy budget, in the sense of the erasure-rate bound derived in Section 4.

**Heat conduction as an engineering discipline.** Bastian and Cracheur [1] recall the modes of heat transfer and their integration into the building-simulation software CODYRUN, with validated applications to flat-plate air collectors and Trombe solar walls. Although the application domain is buildings, the mathematical content — conduction through layered walls with a fixed temperature gap — is exactly the flux model we adopt for the cryostat wall in Eq. (1). The building-energy community has, in effect, already validated the conduction arithmetic we reuse.

**The heat operator and irreversibility.** Brown [8] characterizes the range of the time-$t$ heat operator on Euclidean spaces, spheres, and hyperbolic spaces: functions in the range are roughly those admitting analytic continuation to a complexified manifold with controlled imaginary-axis growth. This gives a rigorous statement of what dissipation destroys: after any nonzero heat-kernel time $t$, the set of reachable states shrinks to a strictly smaller analytic class. In our language, the heat operator is the infinitesimal version of the thermodynamic wall acting on the *information* side: coherence lost to the wall is not recoverable because the lost functions have left the range. This supplies the formal justification for treating wall-induced decoherence as irreversible erasure rather than reversible dephasing.

**Foliation and boundary structure.** Fatibene, Ferraris and Francaviglia [5] develop the geometry of space-time foliations: a foliation $\Sigma$ compatible with the metric $g$ determines a fibration $\pi: M \to N$ whose leaves are spacelike surfaces, and the tangent-splitting $TM = \Sigma + T^0 M$ defines lifts of curves across leaves. We use this only structurally: a quantum computation is naturally foliated into thermal-equilibrium slices (the wall enforces a fixed temperature on each slice), and the wall is the object that transports state between slices while carrying an irreducible thermodynamic cost. The splitting of dynamics into "along-slice" (coherent) and "across-slice" (dissipative) parts mirrors the tangent splitting of [5].

**QNFO corpus.** Three QNFO works frame the physical stakes. *Ultrametric Relaxation Dynamics in Topological Quantum Memory* [9] studies relaxation in memory architectures whose energy landscapes are ultrametric, so that relaxation times hierarchically separate; our wall model supplies the boundary flux that drives that relaxation. *Thermodynamic Viability and the Universality of Feynman Matter* [10] argues that viability of physical computation is thermodynamically, not algorithmically, bounded; the viability window derived in Section 4 is a concrete instantiation of that thesis. *Structural Mediation of Planckian Dissipation in Strongly Correlated Electron Systems* [11] locates a universal (Planckian) dissipation rate in correlated matter; we discuss in Section 6 how the Planckian rate would act as a lower bound on the wall's microscopic dissipation channel, tightening our engineered bounds.

## 3. Methods

### 3.1 The wall as an enriched boundary object

Consider a quantum processor occupying a cold region $\Omega$ at temperature $T_c$, separated from a hot reservoir at $T_h > T_c$ by a wall $W$ of area $A$, thickness $L$, and thermal conductivity $\kappa$. Following the enrichment philosophy of [3],[7], we do not model the wall's microstructure; we enrich the boundary with a single effective parameter, the thermal conductance

$$G_{\mathrm{th}} = \frac{\kappa A}{L},$$

with units $\mathrm{W\,K^{-1}}$. The steady-state heat flux the wall can remove is

$$P_{\mathrm{wall}} = G_{\mathrm{th}}\,\Delta T, \qquad \Delta T = T_h - T_c. \tag{1}$$

This is the standard conduction law as used, e.g., in building-wall simulation [1]; we adopt it unchanged. The wall is *enriched* in the sense of [3]: it carries exactly one degree of freedom ($G_{\mathrm{th}}$) beyond the interior description, and the interior equations (unitary dynamics plus Markovian decoherence) remain discretely fulfilled, in analogy with the constraint preservation of [2].

### 3.2 The erasure budget

Each logical cycle of the processor irreversibly resets (erases) $m$ physical bits — measurement outcomes, error-syndrome bits, and reset qubits. By Landauer's principle, erasing one bit at temperature $T_c$ costs at least

$$E_{\mathrm{bit}} = k_B T_c \ln 2$$

in dissipated heat. Hence the maximum sustainable logical-cycle rate is

$$f_{\max} = \frac{P_{\mathrm{wall}}}{m\, k_B T_c \ln 2} = \frac{G_{\mathrm{th}}\,\Delta T}{m\, k_B T_c \ln 2}. \tag{2}$$

### 3.3 The coherence budget

Thermal excitations at frequency $f_q$ (the qubit transition frequency) have mean occupation

$$n_{\mathrm{th}} = \frac{1}{e^{h f_q / k_B T_c} - 1}. \tag{3}$$

If thermal quanta couple into the qubit at rate $\gamma_c$ (the cavity or qubit linewidth in $\mathrm{s^{-1}}$), the thermal error rate is $\Gamma_{\mathrm{th}} = n_{\mathrm{th}}\gamma_c$ and the associated thermal error time is

$$T_{\mathrm{th}} = \frac{1}{n_{\mathrm{th}}\,\gamma_c}. \tag{4}$$

### 3.4 The viability window

Let $T_2$ be the coherence time from all non-thermal sources. The number of coherent operations the machine can perform is bounded by the *smaller* of the dissipation budget and the coherence budget:

$$N_{\max} = \min\!\left(f_{\max}\, T_2,\; f_{\max}\, T_{\mathrm{th}}\right) = f_{\max}\,\min(T_2, T_{\mathrm{th}}). \tag{5}$$

Equation (5) is the thermodynamic wall inequality: it is the product of a boundary flux (1), an information cost (Landauer), and a coherence clock. It is the engineered counterpart of the thermodynamic-viability thesis of [10] and of the ultrametric relaxation hierarchy of [9], in which slow relaxation channels dominate the long-time budget exactly as $T_{\mathrm{th}}$ dominates here when $n_{\mathrm{th}}$ is exponentially small.

## 4. Analysis

We now evaluate Eqs. (1)–(5) for a representative cryogenic parameter set. Every input number is stated with its source (a stated design assumption or a textbook constant), and every arithmetic step is shown.

**Input 1 — wall conductance product.** Assume a low-conductivity cryogenic wall with $\kappa = 1.0\times 10^{-4}\ \mathrm{W\,m^{-1}K^{-1}}$ (design assumption: a low-$k$ support or mica-style isolation, at the low end of dielectric conductivities), cold-stage area $A = 1.0\times 10^{-6}\ \mathrm{m^2}$ (a $1\ \mathrm{mm}\times 1\ \mathrm{mm}$ thermal link), thickness $L = 1.0\times 10^{-3}\ \mathrm{m}$ (1 mm), and temperature gap $\Delta T = 1.0\times 10^{-3}\ \mathrm{K}$ (design assumption: the mixing-chamber holds the cold stage $1\ \mathrm{mK}$ below the wall's warm face). Then

$$G_{\mathrm{th}} = \frac{\kappa A}{L} = \frac{(1.0\times 10^{-4})\,(1.0\times 10^{-6})}{1.0\times 10^{-3}}\ \mathrm{W\,K^{-1}} = \frac{1.0\times 10^{-10}}{1.0\times 10^{-3}} = 1.0\times 10^{-7}\ \mathrm{W\,K^{-1}},$$

and from Eq. (1),

$$P_{\mathrm{wall}} = G_{\mathrm{th}}\,\Delta T = (1.0\times 10^{-7})\,(1.0\times 10^{-3})\ \mathrm{W} = 1.0\times 10^{-10}\ \mathrm{W}.$$

So the wall removes one hundred picowatts. This is the entire heat budget for erasure.

**Input 2 — cold-stage temperature.** $T_c = 2.0\times 10^{-2}\ \mathrm{K}$ ($20\ \mathrm{mK}$; standard dilution-refrigerator base temperature, design assumption).

**Input 3 — Landauer cost.** With $k_B = 1.380649\times 10^{-23}\ \mathrm{J\,K^{-1}}$ (SI defined value) and $\ln 2 = 0.693147$:

$$E_{\mathrm{bit}} = k_B T_c \ln 2 = (1.380649\times 10^{-23})\,(2.0\times 10^{-2})\,(0.693147)\ \mathrm{J}.$$

Step 1: $(1.380649\times 10^{-23})\times(2.0\times 10^{-2}) = 2.761298\times 10^{-25}$.
Step 2: $(2.761298\times 10^{-25})\times 0.693147 = 1.913979\times 10^{-25}\ \mathrm{J}$.

So $E_{\mathrm{bit}} \approx 1.914\times 10^{-25}\ \mathrm{J}$ per erased bit.

**Input 4 — erasure cost per logical cycle.** $m = 1.0\times 10^{6}$ bits per logical cycle (design assumption: a surface-code-style cycle measuring $\sim 10^{6}$ syndrome/reset bits per logical operation at moderate code distance; the scaling with $m$ is linear and shown explicitly in Eq. (2)).

**Derivation 1 — maximum logical-cycle rate.** From Eq. (2):

$$f_{\max} = \frac{P_{\mathrm{wall}}}{m\,E_{\mathrm{bit}}} = \frac{1.0\times 10^{-10}}{(1.0\times 10^{6})\,(1.913979\times 10^{-25})}\ \mathrm{s^{-1}}.$$

Step 1: denominator $= 1.0\times 10^{6}\times 1.913979\times 10^{-25} = 1.913979\times 10^{-19}\ \mathrm{J}$ per cycle.
Step 2: $f_{\max} = 1.0\times 10^{-10} / 1.913979\times 10^{-19} = 5.2247\times 10^{8}\ \mathrm{s^{-1}}$.

So the wall supports at most $f_{\max} \approx 5.22\times 10^{8}$ logical cycles per second. Note the check: $f_{\max}$ is far below the gigahertz physical clock rates of superconducting qubits, so for this wall the dissipation budget, not the electronics, is binding — which is the paper's central point.

**Input 5 — qubit frequency.** $f_q = 5.0\times 10^{9}\ \mathrm{Hz}$ (typical transmon transition; design assumption). With $h = 6.62607015\times 10^{-34}\ \mathrm{J\,s}$ (SI defined value):

$$\frac{h f_q}{k_B T_c} = \frac{(6.62607015\times 10^{-34})\,(5.0\times 10^{9})}{(1.380649\times 10^{-23})\,(2.0\times 10^{-2})}.$$

Step 1: numerator $= 3.313035\times 10^{-24}\ \mathrm{J}$.
Step 2: denominator $= 2.761298\times 10^{-25}\ \mathrm{J}$.
Step 3: ratio $= 3.313035\times 10^{-24} / 2.761298\times 10^{-25} = 11.9975$.

**Derivation 2 — thermal occupation.** From Eq. (3), with $x = 11.9975$:

$$n_{\mathrm{th}} = \frac{1}{e^{x} - 1}.$$

Since $e^{11.9975} \approx 1.627\times 10^{5}$ (because $e^{12} = 162754.79$ and $e^{-0.0025}\approx 0.99750$, so $e^{11.9975} \approx 162754.79\times 0.99750 = 162347.4$),

$$n_{\mathrm{th}} = \frac{1}{162347.4 - 1} = \frac{1}{162346.4} = 6.1596\times 10^{-6}.$$

So $n_{\mathrm{th}} \approx 6.16\times 10^{-6}$: thermal excitation of the qubit is exponentially suppressed, but not zero.

**Input 6 — coupling rate.** $\gamma_c = 1.0\times 10^{4}\ \mathrm{s^{-1}}$ (design assumption: qubit linewidth of $10\ \mathrm{\mu s}^{-1}$, i.e., a $100\ \mathrm{\mu s}$-scale linewidth, typical of planar superconducting qubits).

**Derivation 3 — thermal error time.** From Eq. (4):

$$\Gamma_{\mathrm{th}} = n_{\mathrm{th}}\,\gamma_c = (6.1596\times 10^{-6})\,(1.0\times 10^{4})\ \mathrm{s^{-1}} = 6.1596\times 10^{-2}\ \mathrm{s^{-1}},$$

$$T_{\mathrm{th}} = \frac{1}{\Gamma_{\mathrm{th}}} = \frac{1}{6.1596\times 10^{-2}} = 16.235\ \mathrm{s}.$$

So thermal excitation produces an error roughly every $16.2\ \mathrm{s}$ per qubit.

**Input 7 — coherence time.** $T_2 = 1.0\ \mathrm{s}$ (design assumption: a dephasing-limited protected or long-lived qubit; the scaling of all results with $T_2$ is linear per Eq. (5)).

**Derivation 4 — the viability window.** Since $T_2 = 1.0\ \mathrm{s} < T_{\mathrm{th}} = 16.235\ \mathrm{s}$, the coherence budget binds, and Eq. (5) gives

$$N_{\max} = f_{\max}\,T_2 = (5.2247\times 10^{8})\,(1.0) = 5.2247\times 10^{8}.$$

So the machine can perform at most $N_{\max} \approx 5.22\times 10^{8}$ coherent logical operations before the wall's dissipation budget is exhausted within one coherence time. Had $T_2$ exceeded $T_{\mathrm{th}} = 16.235\ \mathrm{s}$, the bound would instead be $N_{\max} = f_{\max} T_{\mathrm{th}} = (5.2247\times 10^{8})\times(16.235) = 8.482\times 10^{9}$ operations (arithmetic: $5.2247\times 16.235 = 84.824$, times $10^{8}$).

**Derivation 5 — sensitivity scaling.** From Eq. (5), $N_{\max} \propto G_{\mathrm{th}}\,\Delta T\, T_2 / (m\, T_c)$. Halving $T_c$ doubles $f_{\max}$ (via $1/T_c$) but also doubles $h f_q/k_B T_c$, squaring down $n_{\mathrm{th}}$: at $T_c = 10\ \mathrm{mK}$, $x = 23.995$, $n_{\mathrm{th}} \approx e^{-23.995} \approx 3.79\times 10^{-11}$ (using $e^{-24} = 3.775\times 10^{-11}$), and $T_{\mathrm{th}} = 1/[(3.79\times 10^{-11})(1.0\times 10^{4})] = 1/3.79\times 10^{-7} = 2.639\times 10^{6}\ \mathrm{s} \approx 30.5$ days. Cooling helps both walls, but with radically different exponents: linearly for the flux wall, exponentially for the thermal wall. This asymmetry is the quantitative content of the "wall" picture.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are measured or simulated.

1. **Wall heat budget.** For $G_{\mathrm{th}} = 1.0\times 10^{-7}\ \mathrm{W\,K^{-1}}$ and $\Delta T = 1.0\times 10^{-3}\ \mathrm{K}$, the wall removes $P_{\mathrm{wall}} = 1.0\times 10^{-10}\ \mathrm{W}$.

2. **Landauer cost.** At $T_c = 20\ \mathrm{mK}$, one bit erasure costs $E_{\mathrm{bit}} = 1.914\times 10^{-25}\ \mathrm{J}$.

3. **Maximum logical-cycle rate.** With $m = 10^{6}$ erased bits per cycle, $f_{\max} = 5.22\times 10^{8}\ \mathrm{s^{-1}}$.

4. **Thermal occupation floor.** At $f_q = 5\ \mathrm{GHz}$ and $T_c = 20\ \mathrm{mK}$, $n_{\mathrm{th}} = 6.16\times 10^{-6}$; with $\gamma_c = 10^{4}\ \mathrm{s^{-1}}$, the thermal error time is $T_{\mathrm{th}} = 16.2\ \mathrm{s}$.

5. **Viability window.** With $T_2 = 1.0\ \mathrm{s}$, the machine performs at most $N_{\max} = 5.22\times 10^{8}$ coherent logical operations; if $T_2$ were extended beyond $T_{\mathrm{th}}$, the bound would rise to $8.48\times 10^{9}$ operations.

6. **Scaling law (projection, stated assumptions).** Because $N_{\max} = G_{\mathrm{th}}\Delta T\, T_2/(m k_B T_c \ln 2)$ holds exactly within the model, a $10\times$ improvement in any of $G_{\mathrm{th}}\Delta T$ or $T_2$, or a $10\times$ reduction in $m$ or $T_c$, shifts $N_{\max}$ by exactly one decade, with no uncertainty beyond the input assumptions; the thermal wall $T_{\mathrm{th}}$ instead improves exponentially in $1/T_c$ (at $10\ \mathrm{mK}$, $T_{\mathrm{th}} \approx 2.64\times 10^{6}\ \mathrm{s}$, computed in Derivation 5).

The headline qualitative result: for realistic cryogenic parameters, the dissipation budget ($f_{\max}\sim 5\times 10^{8}\ \mathrm{s^{-1}}$) binds an order of magnitude below plausible physical clock rates, i.e., the thermodynamic wall — not gate speed or even, in this regime, thermal excitation — is the binding constraint on coherent throughput.

## 6. Discussion

**Limitations.** The model has four principal limitations. First, the wall is characterized by a single scalar $G_{\mathrm{th}}$; real cryogenic systems have multiple parallel heat channels (wiring, radiation, residual gas), and the effective conductance is the parallel sum, which can exceed any single-channel estimate. If the true $G_{\mathrm{th}}$ is $10\times$ larger, $N_{\max}$ rises one decade to $\approx 5.22\times 10^{9}$ — the bound is correspondingly soft. Second, Landauer's bound is a lower bound; real reset and measurement protocols dissipate $10$–$10^3\times$ more per bit, which would reduce $f_{\max}$ by the same factor. Third, we assumed erasure is the only heat load; coherent control pulses and quasiparticle generation add loads not captured by Eq. (2). Fourth, the thermal-error model assumes a single thermal bath at $T_c$ coupled at rate $\gamma_c$; nonequilibrium quasiparticle populations can exceed the equilibrium $n_{\mathrm{th}}$ by orders of magnitude, shortening $T_{\mathrm{th}}$ below the computed $16.2\ \mathrm{s}$.

**Relation to Planckian dissipation.** QNFO work on Planckian dissipation [11] suggests a universal microscopic dissipation rate $\Gamma_P \sim k_B T/\hbar$ in strongly correlated matter. At $T_c = 20\ \mathrm{mK}$, $\Gamma_P \approx (1.380649\times 10^{-23}\times 2.0\times 10^{-2})/(1.054571817\times 10^{-34}) = (2.761298\times 10^{-25})/(1.054571817\times 10^{-34}) = 2.618\times 10^{9}\ \mathrm{s^{-1}}$. If the wall's microscopic channel were Planckian-limited at this rate, it would be far faster than our flux-limited budget and hence non-binding — but this is a hypothesis imported from [11], not derived here, and it may fail for engineered mesoscopic walls where disorder and isolation suppress the correlated dissipation channel.

**What would falsify the claims.** The viability inequality (5) would be falsified by (i) a demonstrated architecture sustaining logical-cycle rates $f > f_{\max} = P_{\mathrm{wall}}/(m k_B T_c \ln 2)$ at the stated wall power — this would require violating Landauer's bound or the conduction law (1); or (ii) a demonstrated thermal error time far shorter than Eq. (4) predicts at equilibrium occupation — which would indicate nonequilibrium heating, i.e., that the single-$T_c$ wall model is incomplete rather than wrong. The stronger claim that the wall is *the* binding constraint (rather than $a$ constraint) is falsified by any architecture whose coherence-limited throughput $T_2^{-1}$-scaled rate falls below $f_{\max}$; our numerical example has $f_{\max}$ above typical $T_2$-limited rates, so the claim is parameter-dependent and we do not assert it universally.

**Open questions.** Does the enrichment viewpoint of [3],[4],[7] admit a rigorous variational formulation for thermal boundary layers, i.e., a Galerkin-optimal wall? Does the analytic-range characterization of the heat operator [8] yield an operational measure of how much coherence is irrecoverably lost per unit wall flux? And can the foliation structure of [5] be used to prove a lower bound on across-slice transport cost, tightening Eq. (2) beyond Landauer? Finally, the ultrametric relaxation hierarchy of [9] suggests that in topological memories the effective $m$ may