# Passive Fault Tolerance as a Thermodynamic Phase: Energy-Budget Analysis of a 4D Topological Bandgap in a Floquet-Driven Photonic Lattice

## Abstract

Active quantum error correction protects logical information by measuring syndromes and decoding, at a hardware and energy cost that grows with code size. Passive, self-correcting memories offer an alternative in which errors are thermodynamically suppressed rather than algorithmically reversed, but known constructions rely on many-body Gibbs dynamics of engineered Hamiltonians. This paper analyzes a concrete hardware proposal for the same end: a four-dimensional Harper-Hofstadter band structure, synthesized in a silicon-nitride/lithium-niobate photonic lattice using frequency and orbital-angular-momentum synthetic dimensions under a THz Floquet drive, whose topological mass gap $\Delta$ would make logical errors Boltzmann-suppressed excitations. We derive the protection criterion $\Delta \gg k_{B}T$, evaluate the proposed operating point ($\Delta \approx 14.5$ meV, $T = 80$ K), and find it gives a suppression factor $e^{-\Delta/k_{B}T} \approx 0.122$ — insufficient for fault tolerance. We compute the requirements that do suffice: $\Delta \geq 47.6$ meV at 80 K for a $10^{-3}$ excitation probability, or $T \leq 24.4$ K at the proposed gap; a $1$ s memory lifetime requires $\Delta \geq 142.9$ meV at 80 K or $T \leq 8.12$ K. We further derive the Floquet-drive constraints ($\hbar\omega > 2\Delta$ implies $\nu > 7.01$ THz) and a cryogenic power floor of $27.5$ µW wall power per µW of absorbed heat at 80 K. The analysis converts the proposal into falsifiable engineering targets.

## 1. Introduction

Scalable quantum computation is blocked today by the cost of error correction. The dominant architecture encodes each logical qubit in many physical qubits and repeatedly measures error syndromes, feeding the results to a classical decoder; the framework is well understood [6], and recent work continues to reduce its overheads, for example by replacing the usual $d$ rounds of syndrome extraction with a single round interleaved with transversal logical operations [3]. Nevertheless, every logical operation in this paradigm consumes measurement, control, and classical-computing resources that scale with code distance, and the resource overhead — the number of physical systems per logical qubit — remains a central obstacle identified in the fault-tolerance literature [7]. A hardware platform whose physical substrate suppressed errors by itself, without syndrome measurement, would change the scaling of the machine: the decision facing a quantum-computing architect is how much of the error budget to buy with active machinery and how much, if at all, can be bought with the material phase itself.

Passive protection is not a new idea, but its known realizations are thermodynamic. In self-correcting memories, a Hamiltonian whose low-energy sector stores the logical information is coupled to a thermal bath; the environment then corrects errors, and storage times grow exponentially with system size [1]. The proposal examined here pushes this logic into band theory: instead of a Gibbs state of a many-body Hamiltonian, the logical information lives in the ground sector of a topological band structure with a nonzero second Chern number, realized in a photonic lattice with synthetic dimensions, and errors are excitations across a mass gap $\Delta$. The claim under test is that fault tolerance becomes a property of a material phase — a thermodynamic phase — rather than an algorithm running on top of the hardware.

The contribution of this paper is not to assert that the proposed device works, but to derive, with explicit arithmetic, the conditions under which it could, and to show that the operating point stated in the proposal does not meet them. Specifically:

- We derive the Boltzmann protection criterion and evaluate the proposed operating point ($\Delta \approx 14.5$ meV, $T = 80$ K), obtaining a suppression factor of $0.122$ and concluding that the stated gap is too small for fault-tolerant suppression at 80 K (Sections 4 and 5).
- We compute the gap and temperature targets that achieve excitation probabilities of $10^{-3}$ and $10^{-6}$ and memory lifetimes of $1$ s, giving $\Delta \geq 47.6$ meV at 80 K, $T \leq 24.4$ K at the proposed gap, and $\Delta \geq 142.9$ meV for a 1 s lifetime at 80 K (Sections 4 and 5).
- We derive the Floquet-drive frequency constraints from the requirement that the quasienergy gap survive the drive, giving $\nu > 3.51$ THz for gap non-closure and $\nu > 7.01$ THz for the stronger no-folding condition (Section 4).
- We derive a cryogenic power floor for maintaining the non-equilibrium steady state, $27.5$ µW of wall power per µW of heat absorbed at 80 K at 10% of Carnot efficiency, and set up the energy comparison between the passive scheme and an active decoding chain as a labeled projection (Sections 4 and 5).
- We state the falsifiable tests — a Lindblad simulation of the driven open system and a phonon-extraction rate condition — that would confirm or refute the passive-protection claim (Sections 6 and 7).

## 2. Background and Related Work

The closest conceptual relative of this proposal is the theory of self-correcting quantum memories. [1] proves that classical and quantum LDPC codes with linear confinement are self-correcting: $N$ physical (qu)bits undergoing local, memoryless, time-reversal-symmetric Gibbs-sampling dynamics at low but nonzero temperature protect $\mathrm{O}(N)$ logical (qu)bits for infinite time in the thermodynamic limit, and the authors emphasize that thermal phase transitions are unnecessary for passive error correction, which can be performed by sampling the thermal Gibbs state. Their motivating picture is the ferromagnetic phase of the 2D Ising model, in which the sign of the magnetization stores a classical bit and the time to corruption is exponentially long in system size, and their quantum analogue is the four-dimensional toric code, "two copies of the 2D Ising model" with half of the dimensions protecting against $X$ errors and half against $Z$ errors. The present proposal adopts the same goal — protection by the thermal/energetic structure of the hardware rather than by measurement and decoding — but relocates the mechanism from a Gibbs state of a many-body Hamiltonian to the band gap of a topological band structure; [1]'s result that passive correction survives even in thermodynamically trivial systems supports the plausibility of protection without a conventional phase transition.

The active paradigm that this proposal aims to bypass is described in [6], which lays out the framework of fault-tolerant, error-corrected quantum computing: because of the no-cloning theorem an unknown state cannot be protected by copying, and because measurement collapses the state, encoded information cannot be protected by directly measuring parts of the block, so codes must be designed so that syndrome extraction reveals error information without revealing logical information. [6] also states the failure mode that motivates fault-tolerant circuit design: interactions between qubits during circuit execution copy errors, and if this happens in an uncontrolled manner the code is overwhelmed. Any passive scheme must be compared against this baseline, whose costs scale with the number of syndrome rounds and decoded qubits.

Within the active paradigm, several research programs reduce its overhead, and they mark the points of comparison for what a passive scheme would have to beat. [3] develops transversal algorithmic fault tolerance, in which all logical operations are transversal and interleaved with a single syndrome-extraction round instead of $d$ rounds, using mid-circuit partial decoding and feed-forward; their numerical evaluation includes a $\lvert\overline{S}\rangle$ state distillation factory based on the $[[7,1,3]]$ Steane code operated at circuit noise $p = 0.1\%$, and they argue that the time-cost reduction previously established for Clifford-only circuits extends to universal quantum computation with magic states. [4] constructs fault-tolerant logical gates from homological product codes: given two chain complexes with boundary operators $\delta_{1}$ and $\delta_{2}$ satisfying $\delta_{i}^{2} = 0$, the product operator $\partial = \delta_{1}\otimes\mathbb{1} + \mathbb{1}\otimes\delta_{2}$ defines a CSS code, and if the constituent codes have complementary classes of transversal gates, one can fault-tolerantly map between encoded representations so that a universal gate set is implemented while stabilizer generators remain sparse. [7] encodes a qubit in a large spin qudit with a spin-cat code — for $J = 9/2$, $d = 2J+1 = 10$ levels — correcting error operators linear or quadratic in the components of angular momentum, and frames the enterprise by the threshold theorem: if the component error rate stays below a constant threshold, arbitrarily long computation is possible, with resource overhead the critical quantity. [8] makes holonomic quantum computation fault tolerant by driving the code subsystem with Hamiltonians drawn from the stabilizer or gauge group of the code; with the Bacon-Shor code this needs only 2- and 3-qubit Hamiltonians, and the scheme inherits the error threshold of the dynamical scheme it mirrors, though adiabatic gates are slower and the environmental-noise threshold is correspondingly lower. All four works lower the cost of active correction; none removes the need for syndrome measurement or active feedback. The passive scheme proposed here is complementary: it targets the error rate itself, so that the residual work of active correction is applied to a much smaller population of thermally excited errors.

Classical fault-tolerance engineering supplies two further framing points. [2] proposes an orthogonal fault tolerance model for dynamically adaptive systems, as a means to manage and reason about multiple fault tolerance mechanisms that coexist in one system, and identifies feature interaction among dynamically evolving fault-tolerance mechanisms as a key challenge. This is directly relevant to a hybrid architecture in which a passive thermodynamic mechanism coexists with residual active correction: the two mechanisms must not interfere, and the passive gap must remain open while active control fields are applied. [5] studies Byzantine fault tolerance in cloud clusters and notes that Byzantine faults are a serious challenge because they often go undetected at the initial stage and can propagate to other virtual machines before detection, which is why mission-critical applications such as air traffic control and online banking have stayed away from the cloud for such reasons. The analogue for a quantum memory is an error mechanism that is not Boltzmann-suppressed — for example a drive-induced heating channel or a correlated fabrication defect — which would propagate through the lattice undetected by any energy-based protection; the analysis in Section 4 therefore treats drive-induced heating as the Byzantine channel of the proposed device.

## 3. Methods

This paper is an analytical study. It performs no experiment, simulation on hardware, or measurement; its method is model construction, derivation, and arithmetic evaluation, with all inputs either taken from the proposal under analysis or stated as explicit assumptions.

**Physical model.** The proposed device is a photonic lattice in a silicon-nitride/lithium-niobate platform supporting two synthetic dimensions: a frequency dimension (a lattice of resonator modes indexed by frequency) and an orbital-angular-momentum (OAM) dimension (modes indexed by OAM index $\ell$). Coupling along the synthetic dimensions is engineered by a THz Floquet drive, so that the static description is a 4D Harper-Hofstadter Hamiltonian $H_{0}$ on the product lattice, with flux per plaquette set by the drive phases. The design target stated in the proposal is a topological mass gap $\Delta \approx 14.5$ meV between the ground band sector (storing the logical information) and the first excited band sector, with a nonzero second Chern number

$$C_{2} = \frac{1}{8\pi^{2}}\int_{\mathrm{BZ}_{4}} \mathrm{Tr}\left(\mathcal{F}\wedge\mathcal{F}\right),$$

over the 4D Brillouin zone, where $\mathcal{F}$ is the Berry curvature 2-form. A nonzero $C_{2}$ guarantees that the gap cannot close without a topological phase transition, so gap stability reduces to tracking perturbations that could close it.

**Floquet effective Hamiltonian.** For a periodically driven system $H(t) = H(t + T_{\mathrm{dr}})$ with $T_{\mathrm{dr}} = 2\pi/\omega$, the high-frequency (van Vleck) expansion gives the effective Floquet Hamiltonian to first order in $1/\omega$:

$$H_{F} = H_{0} + \frac{[H_{-1}, H_{+1}]}{\hbar\omega} + \mathrm{O}(\omega^{-2}),$$

where $H_{m}$ are the Fourier components of $H(t)$. Two conditions follow. First, the expansion must converge, requiring $\hbar\omega$ large compared with the drive-induced bandwidth. Second, the quasienergy gap must survive the folding of the spectrum into the Floquet zone; a sufficient condition is $\hbar\omega > 2\Delta$, so that ground-sector and excited-sector quasienergies do not overlap across the zone boundary.

**Open-system criterion.** Errors are modeled as transitions from the ground sector to the excited sector of $H_{F}$ under a thermal bath at temperature $T$. In the simplest two-level reduction, the excited-state population is

$$p_{\mathrm{ex}} = \frac{1}{1 + e^{\Delta/k_{B}T}} \approx e^{-\Delta/k_{B}T} \quad (\Delta \gg k_{B}T),$$

and the memory lifetime against a thermally activated error scales as $\tau = \tau_{0}\, e^{\Delta/k_{B}T}$, where $\tau_{0}$ is the attempt time set by the system-bath coupling. The proposal's claim — that errors become Boltzmann-suppressed high-energy excitations — is thus quantified by the ratio $\Delta/k_{B}T$.

**Non-equilibrium steady state.** The drive deposits heat; the gap survives only if phonon extraction removes heat faster than thermo-optic detuning shifts the band edges. We model this as a rate condition: the phonon extraction rate $\Gamma_{\mathrm{ph}}$ must exceed the thermalization rate into the relevant modes, and the resulting steady-state temperature rise $\delta T$ must satisfy $\left(\partial\Delta/\partial T\right)\delta T \ll \Delta$. Because the proposal supplies no value for $\partial\Delta/\partial T$, we treat the detuning budget as an open question (Section 6) and derive only the cryogenic power cost of removing a specified heat load.

**Energy comparison.** The active baseline is parameterized, not measured: an active scheme with $N_{\mathrm{phys}}$ physical qubits, cycle frequency $f_{\mathrm{cyc}}$, and energy $E_{\mathrm{op}}$ per physical-qubit operation consumes

$$P_{\mathrm{active}} = N_{\mathrm{phys}}\, f_{\mathrm{cyc}}\, E_{\mathrm{op}}.$$

The passive scheme consumes only the cryogenic power needed to hold the lattice at $T$ against the absorbed drive heat $P_{\mathrm{load}}$, computed from the Carnot limit. All numerical values in this comparison are labeled assumptions or projections.

**Numerical conventions.** We use $k_{B} = 8.617333262\times 10^{-2}$ meV/K and $\hbar = 4.135668$ meV·ps (so that a drive at $\nu$ THz has $\hbar\omega = 4.135668\,\nu$ meV). All arithmetic is shown in Section 4.

## 4. Analysis

**Input numbers and their status.** The gap $\Delta = 14.5$ meV and the operating temperature $T = 80$ K are the proposal's stated design targets, treated here as given inputs. Physical constants $k_{B}$ and $\hbar$ are standard. The attempt time $\tau_{0} = 1$ ns, the active-baseline parameters, and the cryocooler efficiency fraction are explicit assumptions, labeled as such where used.

**Step 1: Thermal energy at 80 K.**

$$k_{B}T = (8.617333262\times 10^{-2}\ \mathrm{meV/K})\times 80\ \mathrm{K} = 6.89387\ \mathrm{meV}.$$

**Step 2: Protection ratio at the proposed operating point.**

$$\frac{\Delta}{k_{B}T} = \frac{14.5}{6.89387} = 2.10350.$$

**Step 3: Boltzmann suppression factor.**

$$e^{-\Delta/k_{B}T} = e^{-2.10350} = 0.12206.$$

Equivalently, the excited-state population is $p_{\mathrm{ex}} \approx 1/(1 + e^{2.10350}) = 1/(1+8.1929) = 0.10871$; the asymptotic form $e^{-\Delta/k_{B}T}$ overestimates $p_{\mathrm{ex}}$ slightly, and we quote the conservative value $0.122$ as the suppression factor. A suppression factor of $0.122$ means roughly one error attempt in eight lands in the excited sector — a factor of about $8$, not the many-orders-of-magnitude suppression fault tolerance requires.

**Step 4: Gap required for a target excitation probability at 80 K.** Setting $e^{-\Delta/k_{B}T} = p$ gives $\Delta = k_{B}T \ln(1/p)$. For $p = 10^{-3}$:

$$\Delta_{\mathrm{req}} = 6.89387\times \ln(10^{3}) = 6.89387\times 6.90776 = 47.621\ \mathrm{meV}.$$

For $p = 10^{-6}$:

$$\Delta_{\mathrm{req}} = 6.89387\times \ln(10^{6}) = 6.89387\times 13.81551 = 95.243\ \mathrm{meV}.$$

**Step 5: Temperature required at the proposed gap.** For $p = 10^{-3}$ and $\Delta = 14.5$ meV:

$$T_{\mathrm{req}} = \frac{\Delta}{k_{B}\ln(10^{3})} = \frac{14.5}{(8.617333262\times 10^{-2})\times 6.90776} = \frac{14.5}{0.595268} = 24.361\ \mathrm{K}.$$

For $p = 10^{-6}$:

$$T_{\mathrm{req}} = \frac{14.5}{(8.617333262\times 10^{-2})\times 13.81551} = \frac{14.5}{1.190541} = 12.177\ \mathrm{K}.$$

**Step 6: Memory lifetime.** With the assumption $\tau_{0} = 1$ ns (the attempt time for a bath-coupled photonic mode; no value is given by the proposal), the lifetime is

$$\tau = \tau_{0}\, e^{\Delta/k_{B}T} = 1\ \mathrm{ns}\times e^{2.10350} = 8.1886\ \mathrm{ns}.$$

For a $1$ s lifetime the required exponent is $\ln(\tau/\tau_{0}) = \ln(10^{9}) = 20.7233$, giving at 80 K

$$\Delta_{\mathrm{req}} = 6.89387\times 20.7233 = 142.85\ \mathrm{meV},$$

or at $\Delta = 14.5$ meV

$$T_{\mathrm{req}} = \frac{14.5}{(8.617333262\times 10^{-2})\times 20.7233} = \frac{14.5}{1.785779} = 8.1196\ \mathrm{K}.$$

**Step 7: Attempt-rate upper bound.** Taking the fastest conceivable attempt rate as $\Gamma_{0} \sim k_{B}T/\hbar$:

$$\Gamma_{0} = \frac{6.89387\ \mathrm{meV}}{6.58212\times 10^{-13}\ \mathrm{meV\,s}} = 1.0474\times 10^{13}\ \mathrm{s^{-1}},$$

so the Boltzmann-suppressed rate would be $\Gamma = 0.12206\times 1.0474\times 10^{13} = 1.2783\times 10^{12}\ \mathrm{s^{-1}}$. This bound is physically meaningless as an error rate — real transition rates are set by the system-bath coupling matrix element, not by the thermal energy divided by $\hbar$ — but it shows that the suppression factor, not the attempt rate, is the quantity that must carry the entire protection burden, and at $0.122$ it does not.

**Step 8: Floquet drive constraints.**