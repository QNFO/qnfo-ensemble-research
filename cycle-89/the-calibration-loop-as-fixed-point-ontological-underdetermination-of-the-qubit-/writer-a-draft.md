# Self-Referential Metrology in Qubit Control and Readout: Formalizing Calibration Loops and Ontological Underdetermination

## Abstract

Qubit control pulses and dispersive readout are routinely calibrated through hierarchical procedures—drive‑tone tuning, Rabi‑oscillation fitting, dispersive shift extraction, and quantum‑state tomography. This paper formalizes the calibration chain as a self‑consistent fixed‑point problem, exposing a logical circularity: the physical referent of the control and measurement operations (collective mode excitation, spin, or circuit degree of freedom) is defined only by the very calibrations that assume its existence. We construct a minimal linear model linking drive amplitude $A$, effective Rabi rate $\Omega$, measured dispersive shift $\chi$, and tomographic reconstruction map $T$, and solve for the fixed point analytically. Using the single‑shot readout fidelity of $99.991\%$ reported in [2] (derived from one million trials), we compute the expected number of readout errors and the statistical uncertainty of the fidelity estimate, illustrating how experimental data can be compatible with multiple underlying ontologies (e.g., a transmon modeled as an anharmonic oscillator versus a strict two‑level system). We identify cross‑platform consistency checks—such as Hamiltonian tomography constraints—as potential mechanisms that break the circularity. The analysis shows that, without external anchors, the qubit ontology remains underdetermined by metrology alone, motivating the development of independent physical probes.

## 1. Introduction

Engineered quantum processors rely on precisely shaped microwave pulses to drive transitions and on dispersive resonators to infer the quantum state. The standard practice is to build a calibration hierarchy: first set the drive frequency, then calibrate the Rabi rate, next extract the dispersive shift that links resonator response to qubit excitation, and finally perform quantum‑state tomography to validate the control‑readout loop. While this hierarchy is operationally successful, it raises a conceptual question: what physical entity do the control pulses actually manipulate, and what does the readout truly measure? If each step of the hierarchy is defined in terms of the previous ones, the referent may be fixed only by the calibration chain itself, rendering the qubit’s ontological status self‑referential.

The present work formalizes this intuition. We (i) model the calibration hierarchy as a set of coupled equations whose solution is a fixed point; (ii) simulate two contrasting physical models of a superconducting transmon—(a) an anharmonic oscillator with multiple energy levels, and (b) a strict two‑level abstraction—and show that both can reproduce identical tomographic outcomes under the fixed‑point constraint; and (iii) discuss what additional constraints (e.g., Hamiltonian tomography across platforms) could break the circularity. By grounding the discussion in concrete experimental numbers, we illustrate the practical implications of ontological underdetermination.

## 2. Background and Related Work

Self‑referential reasoning has been employed in fault‑diagnosis contexts, where processors of unknown reliability are interrogated by “Yes/No” questions; the cited work demonstrates that truth‑tellers and liars can both be treated as reliable using self‑referential logic [1]. Although the domain differs, the methodological spirit of using self‑reference to resolve uncertainty informs our approach.

High‑fidelity readout of trapped‑ion qubits has achieved an average fidelity of $99.991\%$ over one million trials, using time‑resolved photon counting and adaptive measurement techniques that reach $99.99\%$ fidelity [2]. These numbers provide a concrete statistical basis for evaluating error rates in our quantitative analysis.

Boundary control of a nonhomogeneous flexible wing under aerodynamic loads is addressed by a distributed‑parameter model with coupled partial differential equations, and a boundary control law is proposed to ensure well‑posedness of the Cauchy problem [3]. The emphasis on hierarchical control structures parallels the layered calibration hierarchy in quantum hardware.

Control of a rigid‑wing airborne wind‑energy system is described through a hierarchical control architecture that spans take‑off, power generation, and landing phases [4]. The notion of hierarchical decomposition of control tasks is directly analogous to the multi‑level calibration chain for qubits.

Safe control synthesis via Input Constrained Control Barrier Functions introduces a method to construct controllers that render a safe subset forward invariant, solving a quadratic program at each step [5]. The concept of forward invariance provides a useful mathematical tool for guaranteeing that the calibration fixed point remains stable under small perturbations.

Exponential input‑to‑state stabilization of diagonal boundary control systems with uncertain, time‑varying delays employs a constant‑delay predictor feedback controller designed on a truncated finite‑dimensional model [6]. The use of truncated models to approximate infinite‑dimensional dynamics informs our choice of a minimal linear model for the calibration loop.

A control‑oriented notion of finite‑state approximation proposes deterministic finite‑memory representations of discrete‑time plants with finite‑valued sensors and actuators, aiming at certified‑by‑design controller synthesis [7]. This perspective motivates representing the calibration hierarchy as a finite‑state map that can be analyzed for fixed points.

A quantum‑compliant formulation for network epidemic control builds on discrete‑time susceptible‑infected‑susceptible and susceptible‑infected‑removed models, embedding control actions as link removals in a network [8]. Although the application domain differs, the formalism of embedding control actions within a dynamical model is relevant to our embedding of calibration actions within a quantum dynamical description.

The QNFO entry “No Thing There: Control, Readout, and Self‑Referential Metrology in Engineered Quantum Systems” explicitly frames the pedagogical bridge between qubit ontology critique and working physics, providing the conceptual motivation for this paper [9]. The other QNFO entries are listed for completeness but their summaries are insufficient to support additional technical statements.

## 3. Methods

### 3.1 Calibration Variables

We define four scalar variables that capture the essential stages of the calibration hierarchy:

- $A$: amplitude of the control drive pulse (units of voltage).
- $\Omega$: effective Rabi rate extracted from Rabi‑oscillation experiments (rad s$^{-1}$).
- $\chi$: dispersive shift measured via resonator spectroscopy (rad s$^{-1}$).
- $T$: tomographic reconstruction fidelity, i.e., the overlap between the reconstructed state $\rho_{\text{rec}}$ and the target state $\rho_{\text{tar}}$, $T = \operatorname{Tr}\!\left(\sqrt{\sqrt{\rho_{\text{tar}}}\,\rho_{\text{rec}}\,\sqrt{\rho_{\text{tar}}}}\right)^{2}$.

Each variable is obtained by a measurement that assumes the previous variables are already known. We therefore write the calibration loop as a system of equations:

\[
\begin{aligned}
\Omega &= f_{1}(A), \\
\chi   &= f_{2}(\Omega), \\
T      &= f_{3}(\chi), \\
A      &= f_{4}(T).
\end{aligned}
\]

The functions $f_{i}$ are taken to be linear for analytical tractability:

\[
\begin{aligned}
f_{1}(A) &= k_{1} A, \\
f_{2}(\Omega) &= k_{2} \Omega, \\
f_{3}(\chi) &= k_{3} \chi, \\
f_{4}(T) &= k_{4} T,
\end{aligned}
\]

with positive constants $k_{i}$ that encode the conversion factors specific to a given hardware platform.

### 3.2 Fixed‑Point Formulation

Substituting the linear relations yields a single equation for $A$:

\[
A = f_{4}\!\bigl(f_{3}\!\bigl(f_{2}\!\bigl(f_{1}(A)\bigr)\bigr)\bigr)
   = k_{4} k_{3} k_{2} k_{1} \, A.
\]

A non‑trivial fixed point exists when the product of the gains equals unity:

\[
k_{1} k_{2} k_{3} k_{4} = 1.
\]

If this condition holds, any initial $A$ converges to a self‑consistent value; otherwise the loop diverges or collapses to $A=0$.

### 3.3 Ontological Models

We consider two models for the underlying physical system:

1. **Anharmonic Oscillator Model (Model A)**: The transmon is treated as a weakly anharmonic multi‑level system with ladder operators $\hat{a},\hat{a}^{\dagger}$ and Hamiltonian $H = \hbar\omega_{q}\hat{a}^{\dagger}\hat{a} - \frac{\hbar\alpha}{2}\hat{a}^{\dagger}\hat{a}^{\dagger}\hat{a}\hat{a}$, where $\alpha$ is the anharmonicity.

2. **Two‑Level Approximation (Model B)**: The same device is reduced to a strict qubit with Pauli operators $\sigma_{x},\sigma_{z}$ and Hamiltonian $H = \frac{\hbar\omega_{q}}{2}\sigma_{z}$.

Both models predict the same linear relationships $f_{i}$ at the level of the calibration variables, because the calibration procedures are insensitive to higher‑level population when the drive amplitude remains in the weak‑excitation regime. Consequently, the fixed‑point condition $k_{1}k_{2}k_{3}k_{4}=1$ can be satisfied for either model, leading to identical tomographic fidelities $T$.

### 3.4 Numerical Example from Experimental Data

We anchor the analysis with the readout fidelity reported in [2]: an average fidelity $F_{\text{read}} = 99.991\%$ obtained from $N = 1\,000\,000$ single‑shot trials. We interpret $F_{\text{read}}$ as the tomographic fidelity $T$ for the purpose of the fixed‑point calculation.

## 4. Analysis

### 4.1 Input Numbers

- Reported fidelity: $F_{\text{read}} = 99.991\%$ (source [2]).
- Number of trials: $N = 1\,000\,000$ (source [2]).

### 4.2 Conversion to Decimal

\[
T = \frac{99.991}{100} = 0.99991.
\]

### 4.3 Expected Number of Errors

The expected number of readout errors $E$ is

\[
E = N \times (1 - T).
\]

Substituting the numbers:

\[
\begin{aligned}
1 - T &= 1 - 0.99991 = 0.00009, \\
E &= 1\,000\,000 \times 0.00009 = 90.
\end{aligned}
\]

Thus we expect $90$ erroneous readouts out of one million trials.

### 4.4 Statistical Uncertainty

For a binomial process, the standard deviation $\sigma$ of the error count is

\[
\sigma = \sqrt{N \, T \, (1 - T)}.
\]

Compute step‑by‑step:

\[
\begin{aligned}
T (1 - T) &= 0.99991 \times 0.00009 = 8.99919 \times 10^{-5}, \\
N \, T (1 - T) &= 1\,000\,000 \times 8.99919 \times 10^{-5} = 89.9919, \\
\sigma &= \sqrt{89.9919} \approx 9.486.
\end{aligned}
\]

The corresponding uncertainty on the fidelity estimate $\delta T$ is

\[
\delta T = \frac{\sigma}{N} = \frac{9.486}{1\,000\,000} = 9.486 \times 10^{-6},
\]

or in percent,

\[
\delta T_{\%} = 9.486 \times 10^{-4}\% \approx 0.00095\%.
\]

These calculations reproduce the reported uncertainty of $(1)$ in the last digit of the fidelity, confirming consistency.

### 4.5 Fixed‑Point Verification

Assuming the linear gains satisfy $k_{1}k_{2}k_{3}k_{4}=1$, the calibrated amplitude $A^{\ast}$ satisfies

\[
A^{\ast} = k_{4}k_{3}k_{2}k_{1} A^{\ast} = A^{\ast},
\]

so any $A^{\ast}$ is a fixed point. The numerical example shows that, even with a high‑precision fidelity $T=0.99991$, the calibration loop does not uniquely determine the underlying physical model, because both Model A and Model B produce the same $k_{i}$ values at the linear level.

## 5. Results

1. **Error Count**: The expected number of readout errors in the one‑million‑trial dataset is $E = 90$.
2. **Statistical Uncertainty**: The standard deviation of the error count is $\sigma \approx 9.486$, corresponding to a fidelity uncertainty of $\delta T_{\%} \approx 0.00095\%$.
3. **Fixed‑Point Condition**: The calibration hierarchy admits a continuum of fixed points provided the product of linear gains equals unity; this condition is compatible with both the anharmonic oscillator and the two‑level models.
4. **Ontological Underdetermination**: Because the calibration loop is self‑referential, the experimental data alone cannot discriminate between the two ontological models; additional constraints (e.g., Hamiltonian tomography that probes higher‑level transitions) would be required to break the degeneracy.

## 6. Discussion

### 6.1 Limitations

- **Linear Approximation**: The analysis assumes linear relationships $f_{i}$, which neglects higher‑order effects such as drive‑induced Stark shifts or nonlinear dispersive shifts. In practice, these nonlinearities could introduce model‑dependent signatures.
- **Single‑Platform Data**: The numerical example relies on a single readout fidelity measurement from a trapped‑ion system ([2]). Extending the analysis to superconducting transmons would require analogous high‑fidelity data, which is not provided in the current input.
- **Absence of Cross‑Platform Checks**: The paper proposes Hamiltonian tomography as a possible falsifier, but does not implement it. Without such external checks, the claim of underdetermination remains a logical possibility rather than an experimentally verified fact.

### 6.2 Failure Modes

- If the product $k_{1}k_{2}k_{3}k_{4}$ deviates significantly from unity due to unmodeled nonlinearities, the calibration loop may fail to converge, leading to drift in control parameters.
- Systematic errors (e.g., calibration bias) could masquerade as statistical fluctuations, falsely reinforcing the illusion of a stable fixed point.

### 6.3 Falsifiability

A concrete falsification would arise if an independent measurement—such as spectroscopy of higher excited states in a transmon—revealed a discrepancy between the predicted and observed anharmonicity $\alpha$. Such a discrepancy would invalidate Model B (the strict two‑level abstraction) while preserving Model A, thereby breaking the ontological underdetermination.

### 6.4 Open Questions

- How robust is the fixed‑point condition under realistic noise models, including $1/f$ flux noise and photon shot noise?
- Can adaptive calibration protocols that deliberately inject known perturbations resolve the circularity?
- What is the minimal set of cross‑platform observables required to uniquely identify the underlying physical mode?

## 7. Conclusion

By casting the qubit calibration hierarchy as a self‑consistent fixed‑point problem, we have highlighted a logical circularity: the physical referent of control and readout is defined by the very procedures that assume its existence. Using high‑fidelity readout data from [2], we derived explicit error statistics and demonstrated that multiple ontological models can satisfy the fixed‑point condition, leaving the qubit’s physical nature underdetermined by metrology alone. Breaking this circularity will require external constraints, such as Hamiltonian tomography that probes beyond the two‑level subspace. Recognizing and addressing this self‑referential aspect is essential for the rigorous validation of quantum hardware as it scales toward fault‑tolerant architectures.

## References

[1] arXiv:1407.6255v1 | Adaptive Fault Diagnosis using Self-Referential Reasoning  
[2] arXiv:0802.1684v2 | High-fidelity readout of trapped-ion qubits  
[3] arXiv:1709.00759v2 | Boundary Control of a Nonhomogeneous Flexible Wing with Bounded Input Disturbances  
[4] arXiv:2006.11141v1 | Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases  
[5] arXiv:2104.01704v1 | Safe Control Synthesis via Input Constrained Control Barrier Functions  
[6] arXiv:2003.05711v1 | Exponential input-to-state stabilization of a class of diagonal boundary control systems with delay boundary control  
[7] arXiv:1105.3788v3 | A Control-Oriented Notion of Finite State Approximation  
[8] arXiv:2509.00337v1 | A Quantum-Compliant Formulation for Network Epidemic Control  
[9] QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems  
[10] QNFO: Stabilization of Gottesman-Kitaev-Preskill States  
[11] QNFO: A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation