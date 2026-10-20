# Trapped-Ion Quantum Simulation as a Falsification Instrument for the Posner Molecule Hypothesis

## Abstract

The Posner molecule hypothesis proposes that phosphorus-31 nuclear spins in $\mathrm{Ca}_9(\mathrm{PO}_4)_6$ clusters retain quantum coherence long enough to influence neural processes, but no experiment can currently isolate and control these spins in their biological environment, so the hypothesis has remained untestable. We close this gap from the simulation side by mapping the Posner spin Hamiltonian onto a trapped-ion quantum processor. A rotating-frame transformation removes the Zeeman term exactly with zero gates; a second-order Trotter decomposition handles the weak scalar coupling $J \approx 0.18\,\mathrm{Hz}$ with two steps per simulated second; and the dipolar term is modeled as a Lindblad dephasing channel, avoiding an estimated $10^4$ Trotter steps per simulated second. The resulting protocol requires six Mølmer-Sørensen gates per simulated second for a four-qubit dimer, runs in approximately $450\,\mu\mathrm{s}$ of wall-clock time per simulated second, and achieves a gate-limited fidelity of $0.995^6 \approx 0.9704$ (about $97\%$), with a Trotter error below $0.15\%$ per simulated second. Extending to a trimer raises the count to at most 18 gates per simulated second, which remains constant in the total simulated time. These numbers define a concrete falsification threshold of about $3.1\%$ total error, testable on current hardware: deviations of the five proposed observables beyond this bound would refute the Posner dynamics.

## 1. Introduction

Researchers in quantum biology have proposed that the phosphorus-31 nuclear spins inside Posner molecules, $\mathrm{Ca}_9(\mathrm{PO}_4)_6$, could act as long-lived qubits that mediate quantum effects in the brain [8]. If the hypothesis is true, it would supply a physical substrate for quantum-level processing in a warm biological environment, with consequences for neuroscience and for the design of bio-inspired quantum technologies. Today the hypothesis blocks progress in both fields because it cannot be tested: direct measurement of Posner spin dynamics in situ is experimentally inaccessible, the predicted interaction strengths ($J \approx 0.18\,\mathrm{Hz}$) lie far below typical laboratory noise floors, and no existing platform has a worked-out protocol that reproduces the Posner Hamiltonian with quantified error. The decision that would change if this paper's result holds is concrete: an experimentalist can schedule a table-top test on an existing trapped-ion processor, and a negative outcome redirects resources in quantum biology away from spin-based mechanisms.

A decisive experiment would reproduce the Posner Hamiltonian on a controllable quantum processor, measure the five proposed observables (singlet decay, beat frequencies, concurrence, field-dependent phase diagram, and singlet yield), and compare them with the theoretical predictions of the hypothesis. If the simulated dynamics match the predictions within quantified error bounds, the hypothesis gains empirical credibility; if they diverge beyond those bounds, the hypothesis is falsified. This paper derives the protocol, its gate budget, its error budget, and the resulting falsification threshold, so that the experiment is specified tightly enough to be scheduled and adjudicated.

**Contributions.**

- **C1.** Derive a rotating-frame mapping that eliminates the Zeeman term without any quantum gates (Section 3.2).
- **C2.** Formulate a two-step Trotter decomposition for the $J$-coupling and compute the required gate count of six Mølmer-Sørensen gates per simulated second for the dimer (Sections 3.3 and 4.1).
- **C3.** Model the dipolar coupling as a Lindblad channel and quantify the approximately $10^4$ Trotter steps per simulated second that this avoids (Sections 3.4 and 4.4).
- **C4.** Compute the overall simulation fidelity $F = 0.995^6 \approx 0.9704$ and the Trotter error bound under realistic gate errors (Section 4.2 and 4.3).
- **C5.** Show that scaling to a trimer costs at most 18 gates per simulated second and remains constant in the total simulated time (Section 4.5).
- **C6.** Convert the gate budget into wall-clock time ($450\,\mu\mathrm{s}$ per simulated second), energy ($6\,\mu\mathrm{J}$ per simulated second, a labeled projection), and a falsification threshold of about $3.1\%$, and specify the experimental protocol and its criteria (Sections 4.6 through 4.9 and Section 7).

## 2. Background and Related Work

This work draws on three strands of literature: trapped-ion simulation methods, the energetics and engineering of trapped-ion processors, and the biological claims that the protocol is designed to test.

On the methods side, [3] analyzes the efficiency of quantum simulations of fermionic and bosonic models in trapped ions and shows that a digital-analog scheme can implement each nonlocal spin term, obtained after a Jordan-Wigner transformation and a Trotter expansion, with two Mølmer-Sørensen gates and a local gate, yielding polynomial-resource protocols. Our gate sequence for the Posner $J$-coupling follows this digital-analog style; the specific three-pulse-per-pair-per-step count used here is our own design assumption, chosen conservatively relative to the two-gate scheme of [3]. [7] reviews quantum simulations with cold trapped ions and documents the experimental toolkit the field relies on, including chains of up to 50 ions in which phonon occupation is mapped onto the internal state and read out through resonance fluorescence [7]; this readout practice is the precedent for measuring the Posner observables on an ion register. [1] demonstrates the measurement technique we adopt for observable extraction: full counting statistics and probability distributions reconstructed with classical shadows, in which local random unitaries drawn from a unitary 2-design are applied before projective readout, with the experiments reported there using $N_u = 500$ random rotations and between 30 and 150 shots per rotation [1]. Shadow estimation is what makes the five Posner observables measurable with a bounded number of shots. [5] establishes that the many-body physics of symmetric-top molecules maps onto magnetic-dipole systems whose dipole-dipole interactions are typically two orders of magnitude stronger than those of naturally occurring magnetic dipoles [5]; this comparison supports our treatment of the Posner dipolar term as a weak perturbation relative to the scalar coupling, since real nuclear dipole-dipole couplings in the millihertz range are far below the $0.18\,\mathrm{Hz}$ scalar coupling.

On the platform side, [4] reviews the physics of trapped ions, explaining that ions suspended in vacuum by electromagnetic fields are shielded from the decohering environment that affects solid-state qubits, and that their motional degrees of freedom provide a "quantum bus" that mediates entanglement between distant ions [4]; we adopt the Mølmer-Sørensen interaction as the native entangling gate on this basis, and treat laser power and beam stability as engineering constraints rather than derived quantities. [6] presents a compiler for a shuttling-based trapped-ion computer whose block commutation and phase-tracking techniques reduce gate counts by factors of up to 5.11 compared to Pytket and 2.22 compared to Qiskit [6]; such compilation is the route by which our fixed pulse sequence would be embedded in a specific machine's native gate set, and the same work identifies simultaneous addressed manipulation of larger ion subsets as the architectural step that would let our trimer pulses run in parallel. [2] quantifies the energetics of a trapped-ion computation by analyzing a three-qubit quantum Fourier transform on microwave-driven $\mathrm{{}^{171}Yb^{+}}$ ions and finds that the dominant energetic cost is the supply of the Paul trap, with the total cost of the gate sequence itself low [2]; this framing motivates our energy accounting in Section 4.8, although the per-gate fidelity of $99.5\%$ used in our error model is stated here as an assumption, not a value taken from [2]. [9] organizes a research program into a falsifiability register and reports the competitive-landscape figure we use for the energy comparison: the joules-per-solution metric ranks trapped ions last among seventeen platforms at $8.5$ to $16.3\,\mathrm{J/sol}$, because $50$ to $100\,\mu\mathrm{s}$ gate times overwhelm their room-temperature power advantage [9]. The same work argues that a testable program must keep its negative results, which is the epistemic stance of the present protocol.

On the biological side, [8] argues that the nucleus, not the electron or the cytoplasm, is the only viable repository for quantum information in a thermal environment, noting that at $310\,\mathrm{K}$ the thermal energy $k_B T$ is approximately $26\,\mathrm{meV}$ and that the "nuclear pivot" reorients quantum biology toward the atomic nucleus [8]; this is the physical rationale for targeting phosphorus-31 nuclear spins. [11] establishes a quantitative boundary between engineered and biological quantum coherence by benchmarking the Google Willow superconducting processor, which achieves a logical coherence time of $291\,\mu\mathrm{s}$ at $20\,\mathrm{mK}$ with active error correction, against a biological requirement of $25\,\mathrm{ms}$ at $310\,\mathrm{K}$, identifying a protection deficit of approximately $10^{12}$ [11]; we use this benchmark in Section 4.9 to place our simulator's error budget in thermodynamic context. Finally, [10] argues within a unified-state-space framework that Bell's 1964 theorem relies on the assumption of statistical independence between observer and observed [10]; we invoke this point only to make explicit an assumption of our own falsification logic, namely that the statistics measured on the simulator are independent of the biological hypothesis under test, so that a null result carries evidential weight.

## 3. Methods

### 3.1 Hamiltonian of the Posner Molecule

The Posner spin Hamiltonian for a dimer of two phosphorus-31 nuclei is written as

$$
H_{\mathrm{Pos}} = \underbrace{\sum_{i} \gamma B_0 I_z^{(i)}}_{\text{Zeeman}} + \underbrace{J \sum_{\langle i,j\rangle} \mathbf{I}^{(i)} \cdot \mathbf{I}^{(j)}}_{\text{$J$-coupling}} + \underbrace{\sum_{i<j} D_{ij}\, \mathcal{L}_{ij}}_{\text{dipolar (Lindblad)}} ,
$$

where $\gamma$ is the gyromagnetic ratio, $B_0$ the static magnetic field, $J \approx 0.18\,\mathrm{Hz}$ the scalar coupling (input from the research proposal), $D_{ij}$ the dipolar strength, and $\mathcal{L}_{ij}$ a Lindblad superoperator describing dipolar dephasing. Each phosphorus-31 nucleus is a spin-$1/2$ system, so the dimer maps to four qubits (two qubits per nucleus to represent the two molecules' coupled spins) and the trimer to six.

### 3.2 Rotating-Frame Transformation

We move to a frame rotating at the Larmor frequency $\omega_L = \gamma B_0$:

$$
\tilde{H} = U^{\dagger} H_{\mathrm{Pos}} U - i U^{\dagger} \dot{U}, \qquad U = \exp\!\left(-i\,\omega_L t \sum_i I_z^{(i)}\right),
$$

which eliminates the Zeeman term exactly, yielding

$$
\tilde{H} = J \sum_{\langle i,j\rangle} \mathbf{I}^{(i)} \cdot \mathbf{I}^{(j)} + \sum_{i<j} D_{ij}\, \mathcal{L}_{ij}.
$$

No quantum gates are required for this transformation; it is a change of reference frame applied in classical post-processing of the measurement record (C1). The only physical requirement is that the simulator's own qubit frequencies be stable enough that the rotating-frame phase reference is tracked correctly; we treat residual field inhomogeneity as a systematic phase error in Section 6.

### 3.3 Trotter Decomposition of the $J$-Coupling

We discretize the evolution $\exp(-i\tilde{H}t)$ with a second-order Trotter formula using two steps per simulated second:

$$
e^{-i\tilde{H}\Delta t} \approx e^{-i (J\Delta t / 2) \sum_{\langle i,j\rangle} \mathbf{I}^{(i)} \cdot \mathbf{I}^{(j)}}\; e^{-i \Delta t \sum_{i<j} D_{ij} \mathcal{L}_{ij}}\; e^{-i (J\Delta t / 2) \sum_{\langle i,j\rangle} \mathbf{I}^{(i)} \cdot \mathbf{I}^{(j)}},
$$

with $\Delta t = 0.5\,\mathrm{s}$, since two steps cover one simulated second. The $J$-coupling term is implemented with the native Mølmer-Sørensen (MS) interaction, which generates an effective Ising coupling $\sigma_x^{(i)} \sigma_x^{(j)}$; combined with single-qubit rotations this yields the desired Heisenberg interaction $\mathbf{I}^{(i)} \cdot \mathbf{I}^{(j)}$, in the digital-analog style of [3]. We assume, as a conservative design choice, that each pair term in one Trotter step requires three MS pulses (the scheme of [3] uses two MS gates plus local gates per term; we budget three to cover the half-step structure of the second-order formula). This assumption is stated explicitly because no source supplies the exact count for the Posner Hamiltonian.

### 3.4 Lindblad Approximation for the Dipolar Coupling

The dipolar term is weak compared to the $J$-coupling and is treated as Markovian dephasing:

$$
\mathcal{L}_{ij}[\rho] = \gamma_{ij} \left( 2 I_z^{(i)} \rho I_z^{(j)} - \left\{ I_z^{(i)} I_z^{(j)}, \rho \right\} \right),
$$

with rates $\gamma_{ij}$ estimated from the Posner geometry. The channel is applied after each Trotter step. This avoids explicit Trotterization of the dipolar interaction, bypassing the approximately $10^4$ steps per simulated second that a naive discretization would require (C3); the $10^4$ figure is the design estimate carried from the research proposal and is used here as a stated assumption, not a derived value. The physical justification is the same weakness argument that [5] makes precise in a different setting: dipolar interactions of naturally occurring magnetic moments are far weaker than the engineered couplings around them, so the dipolar dynamics act on timescales long compared to the Trotter step and can be modeled as a Markovian channel to first order.

### 3.5 Gate Sequence per Simulated Second

Each Trotter step requires, per coupled pair, three MS gates under our conservative budget, plus single-qubit rotations that are an order of magnitude faster than MS gates and are not counted in the MS budget. With two steps per simulated second and one pair in the dimer, the total is

$$
N_{\mathrm{gate}} = 3 \times 2 = 6 \;\; \text{MS gates per simulated second (C2)}.
$$

### 3.6 Fidelity Model

We assume a per-gate fidelity $f_{\mathrm{MS}} = 0.995$ for MS gates, a realistic figure for current trapped-ion hardware; this is an assumption of our error model, not a measured value from any cited source. Assuming independent errors, the overall fidelity after $N_{\mathrm{gate}}$ gates is

$$
F = f_{\mathrm{MS}}^{N_{\mathrm{gate}}}.
$$

Correlated errors would violate the independence assumption; this is treated as a limitation in Section 6.

### 3.7 Wall-Clock and Energy Model

To convert the gate budget into resources, we assume an MS gate duration $t_{\mathrm{gate}} = 75\,\mu\mathrm{s}$, the midpoint of the $50$ to $100\,\mu\mathrm{s}$ range reported for trapped-ion gate times in the competitive landscape of [9], and a per-gate laser-pulse energy $E_{\mathrm{gate}} = 1\,\mu\mathrm{J}$, stated as an assumption because the exact pulse energy depends on the laser-system design. Both inputs are labeled assumptions and all downstream numbers that depend on them are labeled projections.

## 4. Analysis

### 4.1 Gate Count Calculation

Inputs: $J = 0.18\,\mathrm{Hz}$ (from the research proposal); $\Delta t = 0.5\,\mathrm{s}$; $g_{\mathrm{step}} = 3$ MS gates per pair per step (our stated design assumption, Section 3.3); $s = 2$ steps per simulated second; one coupled pair in the dimer. Hence

$$
N_{\mathrm{gate}} = g_{\mathrm{step}} \times s \times 1 = 3 \times 2 \times 1 = 6 \;\; \text{MS gates per simulated second}.
$$

This matches the six-gate figure proposed in the research idea.

### 4.2 Fidelity Computation

Given $f_{\mathrm{MS}} = 0.995$ and $N_{\mathrm{gate}} = 6$:

$$
F = 0.995^6.
$$

Step by step: $0.995^2 = 0.990025$; $0.995^3 = 0.990025 \times 0.995 = 0.985074875$; $0.995^6 = 0.985074875^2$. Computing the square: $0.985074875^2 = 0.985074875 \times 0.985074875$. Writing $0.985074875 = 0.985 + 0.000074875$, the square is $0.985^2 + 2 \times 0.985 \times 0.000074875 + (0.000074875)^2 = 0.970225 + 0.00014750 + 0.0000000056 = 0.9703725$. Thus

$$
F \approx 0.9704, \quad \text{i.e. } 97.04\%,
$$

and the gate-error probability per simulated second is

$$
p_{\mathrm{error}} = 1 - F = 1 - 0.9703725 = 0.0296275 \approx 2.96\%.
$$

We report $F \approx 97\%$ at two significant figures. (An earlier draft of this work quoted $0.995^6 = 0.970299$; the correct value is $0.970373$, and the corrected figure is used throughout.)

### 4.3 Trotter Error Bound

The second-order Trotter error scales as $\mathcal{O}\!\left((J\Delta t)^3\right)$ per step. With $J = 0.18\,\mathrm{Hz}$ and $\Delta t = 0.5\,\mathrm{s}$:

$$
J\Delta t = 0.18 \times 0.5 = 0.09,
$$
$$
(J\Delta t)^3 = 0.09^3 = 0.09 \times 0.09 \times 0.09 = 0.000729 = 7.29 \times 10^{-4},
$$

which is $0.0729\%$ per step. Over two steps per simulated second the cumulative Trotter error is approximately $2 \times 0.0729\% = 0.146\%$, so

$$
\epsilon_{\mathrm{Trotter}} \le 0.15\% \;\; \text{per simulated second}.
$$

This is more than an order of magnitude below the gate-error budget of $2.96\%$, so the discretization is not the binding constraint.

### 4.4 Lindblad Simplification

Modeling the dipolar coupling as a Lindblad channel removes the need to Trotterize it. The avoided overhead is the approximately $10^4$ Trotter steps per simulated second that explicit dipolar discretization would require (stated assumption, Section 3.4). Relative to the six gates per simulated second of the actual protocol, the avoided overhead is a factor of

$$
\frac{10^4}{6} \approx 1.7 \times 10^3
$$

in gate count per simulated second, i.e. roughly three orders of magnitude.

### 4.5 Scaling to Larger Clusters

For a trimer (three coupled nuclei) the number of pairwise $J$-couplings rises from 1 to 3. Under pairwise addressing, each pair requires $g_{\mathrm{step}} = 3$ MS gates per step, so

$$
N_{\mathrm{trimer}} = 3 \; \text{pairs} \times 3 \; \text{gates/pair/step} \times 2 \; \text{steps} = 18 \;\; \text{MS gates per simulated second}.
$$

This is the conservative pairwise bound. Global MS pulses that entangle several pairs at once, of the kind enabled by the simultaneous multi-ion manipulation identified as a next architectural step in [6], could reduce this count; we do not claim that reduction because it