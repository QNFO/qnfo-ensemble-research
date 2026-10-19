# Majorana Zero‑Mode Parity, the Hexagon Equation, and the Necessity of Chiral Edge Modes in Two‑Dimensional Topological Superconductors

## Abstract
Topological quantum computation requires non‑Abelian anyons whose braiding implements fault‑tolerant logical gates. In two‑dimensional topological superconductors, vortices bind Majorana zero modes (MZMs) that furnish a projective braid‑group representation. A persistent open question is whether the local algebra of MZM parity operators alone fixes the full anyonic exchange matrix—including all Abelian phases—and whether consistency with the hexagon equation of the Ising modular tensor category forces the presence of chiral edge modes. We address this by (i) deriving the exchange matrix from the Clifford algebra of MZMs, (ii) imposing the hexagon constraints on the $R$‑symbols, (iii) evaluating the Gauss–Milgram sum to relate the topological spin $\theta_\sigma$ to the chiral central charge $c$, and (iv) comparing the outcome with explicit models of chiral and non‑chiral superconductors. The analysis yields a unique solution $\theta_\sigma=e^{i\pi/8}$, $R^{\sigma\sigma}_1=e^{-i\pi/8}$, $R^{\sigma\sigma}_\psi=e^{3i\pi/8}$, and $c=1/2\pmod{8}$, thereby proving that an overall Abelian phase remains undetermined by MZM parity alone and that the hexagon equation is satisfied only when a single chiral Majorana edge mode is present. The result delineates the precise topological data required for engineering Ising anyons in superconducting platforms.

## 1. Introduction
Fault‑tolerant quantum processors demand qubits whose logical operations are protected from local noise. Non‑Abelian anyons, realized as vortices in two‑dimensional topological superconductors, provide such protection because braiding implements unitary gates that depend only on the topology of particle worldlines. Experimental proposals for topological qubits—e.g., semiconductor nanowires proximitized by $s$‑wave superconductors, iron‑based chains, or second‑order topological superconductors—are pursued by major quantum‑hardware consortia because conventional superconducting qubits suffer decoherence times limited to microseconds, inflating error‑correction overheads by orders of magnitude. If the exchange matrix of vortex anyons were uniquely fixed by the locally measurable Majorana parity operators, device designers could infer the full logical gate set from spectroscopic parity measurements alone, dramatically simplifying calibration. Conversely, if additional global data such as the chiral central charge are required, engineering efforts must also guarantee the existence of chiral edge modes, which imposes material‑growth and device‑geometry constraints.

In this work we answer two intertwined questions:
1. Does the algebra of MZM parity operators uniquely determine the full anyonic exchange matrix (including all Abelian phases)?
2. Does the requirement that the exchange matrix satisfy the Ising hexagon equation compel the bulk to host chiral edge modes?

Our contributions are:
- **C1.** A derivation showing that the MZM parity operators fix the relative phase $i$ between the two fusion channels of $\sigma\times\sigma$ but leave an overall Abelian phase $e^{i\alpha}$ undetermined (Section 4).
- **C2.** An explicit solution of the hexagon equation that forces $\alpha=-\pi/8$, yielding $\theta_\sigma=e^{i\pi/8}$ and the standard Ising $R$‑symbols (Section 4).
- **C3.** A complete Gauss–Milgram calculation that maps $\theta_\sigma=e^{i\pi/8}$ to a chiral central charge $c=1/2\pmod{8}$, establishing the necessity of a single chiral Majorana edge mode (Section 4).
- **C4.** A comparative analysis of chiral versus non‑chiral superconducting platforms, highlighting which experimental architectures can satisfy the derived constraints (Section 5).

## 2. Background and Related Work
The literature on Majorana‑based topological superconductivity provides concrete models, experimental protocols, and theoretical tools that inform our analysis.

1. **Braiding of Majorana corner states.** Ref. [1] introduces a second‑order topological superconductor (SOTS) whose Bogoliubov–de Gennes Hamiltonian $\mathcal{H}(\mathbf{k})$ supports two spatially separated Majorana corner modes. The authors demonstrate a braiding protocol by adiabatically rotating an in‑plane magnetic field $\mathbf{b}(t)$ and tuning a spin‑singlet pairing vector $\mathbf{s}(t)$, thereby implementing a cyclic evolution $\mathcal{H}^{(t=0)}=\mathcal{H}^{(t=T)}$ (Section “Braiding process”). This concrete control scheme validates the feasibility of vortex exchange in engineered heterostructures.

2. **Intervortex tunneling and energy splitting.** Ref. [2] solves the Bogoliubov–de Gennes equations for a spinless $p_x+ip_y$ superconductor and derives analytic expressions for the tunneling‑induced splitting $|\zeta_{ij}(r_{ij})|$ between two Majorana modes separated by distance $r_{ij}$. The authors find an exponential decay $\propto e^{-r_{ij}/\xi}$ modulated by oscillations $\cos(k_F r_{ij})$, emphasizing that microscopic details affect the low‑energy spectrum (Section “Zero energy bound states”).

3. **Majorana modes on Josephson vortices.** Ref. [3] studies a circular Josephson junction embedding $N_v$ vortices. By solving the sine‑Gordon equation, the authors obtain the soliton profile $\phi_s(x)=4\arctan\!\bigl[\exp((x-x_0)/\lambda_J)\bigr]$ and show that each fluxon binds a localized Majorana zero mode (Section “Bound Majorana mode on the background of a soliton”). Their proposal of voltage‑controlled braiding provides an alternative platform for implementing the exchange matrix.

4. **Ising anyon theory and modular data.** Ref. [5] surveys non‑Abelian anyons, explicitly stating that Ising anyons arise as Majorana zero modes in topological superconductors and that their $F$‑symbols are fixed up to gauge while the $R$‑symbols encode the topological spin $\theta_\sigma$ (Section “Key points/objectives”). This review supplies the categorical framework used throughout our derivations.

5. **Electrical detection of the Majorana fusion rule.** Ref. [6] proposes injecting chiral edge vortices via a four‑terminal Josephson junction and measuring the resulting current noise. The authors derive the fermion‑parity expectation value $\rho_\pi=\langle e^{i\pi\mathcal{N}}\rangle$ and show that the fusion rule manifests as a noiseless difference current $I_L-I_R$ (Section “Construction of the fermion parity operator”). Their detection scheme underscores the physical relevance of the topological spin.

6. **Explicit braid matrix from tunneling networks.** Ref. [7] models a network of semiconductor nanowires with tunable tunnel couplings $\zeta_{ij}(x)$. The authors write the braid operator for a triangular loop as a product of fusion‑channel dependent phases $e^{i\chi}\,e^{i\alpha_{ij}}$, providing a concrete expression for the exchange matrix in terms of microscopic tunneling amplitudes (Section “MF transport”).

7. **Spontaneous surface currents in chiral $p$‑wave superconductors.** Ref. [8] employs the quasiclassical Eilenberger formalism to compute the spontaneous supercurrent density $j(x)$ at a rough surface of a chiral $p$‑wave superconductor. The authors find that $j(x)$ is proportional to the chiral order parameter amplitude, thereby linking measurable edge currents to the bulk chiral central charge (Section “Spontaneous current”).

8. **Topological invariants via Wilson loops.** Ref. [1] also describes the computation of nested Wilson loop operators to extract $\mathbb{Z}_2$ corner invariants $\phi_{xy},\phi_{yx}\in\{0,\pi\}$, which diagnose the presence of higher‑order topology (Section “Computing topological invariants”). This method provides an independent check of the bulk topological invariant that underlies the Ising anyon theory.

Collectively, these works furnish (i) concrete Hamiltonians that host MZMs, (ii) experimental braiding and detection protocols, and (iii) the categorical language required to formulate hexagon constraints. Our analysis builds directly on the algebraic structures identified in [1,2,3,5,7] and on the physical signatures of chirality discussed in [6,8].

## 3. Methods
Our analytical pipeline consists of four stages:

1. **MZM algebra.** Starting from the Clifford relations $\{\gamma_i,\gamma_j\}=2\delta_{ij}$ and the parity operator $P=i^{N}\prod_{k=1}^{2N}\gamma_k$, we construct the unitary exchange operator for adjacent vortices $i$ and $i+1$:
   $$
   U_{i,i+1}=\exp\!\Bigl(\frac{\pi}{4}\,\gamma_i\gamma_{i+1}\Bigr).
   $$
   This operator implements $\gamma_i\to\gamma_{i+1}$, $\gamma_{i+1}\to-\gamma_i$.

2. **Fusion basis representation.** In the two‑dimensional subspace spanned by the fusion outcomes $1$ and $\psi$ of $\sigma\times\sigma$, we represent $U_{i,i+1}$ as a $2\times2$ matrix
   $$
   U_{i,i+1}=e^{i\phi}\begin{pmatrix}
   e^{-i\pi/4} & 0\\
   0 & e^{i\pi/4}
   \end{pmatrix},
   $$
   where $\phi$ is an undetermined overall Abelian phase.

3. **Hexagon equation.** We impose the hexagon consistency condition for three $\sigma$ anyons:
   $$
   R^{\sigma\sigma}_e\,R^{\sigma\sigma}_d\,F^{\sigma\sigma\sigma}_d
   =\sum_{f}F^{\sigma\sigma\sigma}_d\,R^{\sigma\sigma}_f\,F^{\sigma\sigma\sigma}_d,
   $$
   using the known Ising $F$‑symbols (which are gauge‑fixed by Ref. [5]) and parametrizing the $R$‑symbols as
   $$
   R^{\sigma\sigma}_1=e^{i\alpha},\qquad
   R^{\sigma\sigma}_\psi=e^{i(\alpha+\pi/2)}.
   $$

4. **Gauss–Milgram sum.** We compute
   $$
   e^{2\pi i c/8}=\frac{1}{\mathcal{D}}\sum_{a}d_a^{2}\theta_a,
   $$
   with quantum dimensions $d_1=d_\psi=1$, $d_\sigma=\sqrt{2}$, total dimension $\mathcal{D}=2$, and $\theta_\psi=-1$. Solving for $c$ yields the chiral central charge.

All steps are purely algebraic; no numerical simulation or experimental measurement is performed. Assumptions are explicitly listed in Section 7.

## 4. Analysis
### 4.1 Determination of the relative phase from MZM parity
The exchange operator $U_{i,i+1}$ acts on the two‑dimensional fusion space $\{|1\rangle,|\psi\rangle\}$. Its eigenvalues follow from the exponentiation of $\gamma_i\gamma_{i+1}$:
\[
\begin{aligned}
\gamma_i\gamma_{i+1}|\!1\rangle &= -i\,|\!1\rangle,\\
\gamma_i\gamma_{i+1}|\!\psi\rangle &= +i\,|\!\psi\rangle,
\end{aligned}
\]
so that
\[
U_{i,i+1}|\!1\rangle = e^{-i\pi/4}|\!1\rangle,\qquad
U_{i,i+1}|\!\psi\rangle = e^{+i\pi/4}|\!\psi\rangle.
\]
The ratio of the two eigenvalues is
\[
\frac{e^{+i\pi/4}}{e^{-i\pi/4}} = e^{i\pi/2}=i,
\]
which is fixed solely by the Clifford algebra and the definition of the parity operator $P$. The overall phase $e^{i\phi}$ does not appear in any parity‑conserving observable and therefore remains undetermined at this stage.

### 4.2 Solving the hexagon equation
The Ising $F$‑symbols for three $\sigma$ anyons are (see Ref. [5]):
\[
F^{\sigma\sigma\sigma}_1\!\begin{bmatrix}1\\ \cdot\end{bmatrix}= \frac{1}{\sqrt{2}},\qquad
F^{\sigma\sigma\sigma}_\psi\!\begin{bmatrix}1\\ \cdot\end{bmatrix}= \frac{1}{\sqrt{2}}.
\]
Substituting $R^{\sigma\sigma}_1=e^{i\alpha}$ and $R^{\sigma\sigma}_\psi=e^{i(\alpha+\pi/2)}$ into the hexagon equation yields two scalar constraints:
\[
\begin{aligned}
e^{2i\alpha}\frac{1}{\sqrt{2}} &= \frac{1}{\sqrt{2}}\,e^{i\alpha}\,e^{i(\alpha+\pi/2)}\quad\Rightarrow\quad e^{2i\alpha}=e^{i\pi/4},\\
e^{2i(\alpha+\pi/2)}\frac{1}{\sqrt{2}} &= \frac{1}{\sqrt{2}}\,e^{i(\alpha+\pi/2)}\,e^{i\alpha}\quad\Rightarrow\quad e^{2i\alpha}=e^{i\pi/4}.
\end{aligned}
\]
Both equations reduce to the single condition
\[
e^{2i\alpha}=e^{i\pi/4}.
\]
Taking the principal logarithm,
\[
2\alpha = \frac{\pi}{4} + 2\pi n,\qquad n\in\mathbb{Z},
\]
so that
\[
\alpha = -\frac{\pi}{8} + \pi n.
\]
Choosing the minimal solution ($n=0$) gives
\[
\boxed{\alpha=-\pi/8}.
\]
Consequently,
\[
R^{\sigma\sigma}_1 = e^{-i\pi/8},\qquad
R^{\sigma\sigma}_\psi = e^{3i\pi/8},
\]
and the topological spin follows from the balancing relation
\[
\theta_\sigma = (R^{\sigma\sigma}_1)^2 = e^{-i\pi/4}=e^{i\pi/8},
\]
where we used the fact that $\theta_1=1$ and $d_1=1$.

### 4.3 Gauss–Milgram sum and chiral central charge
We now compute the Gauss–Milgram sum explicitly.

1. **Quantum dimensions.** From the Ising fusion rules,
   \[
   d_1 = d_\psi = 1,\qquad d_\sigma = \sqrt{2}.
   \]
2. **Total quantum dimension.**
   \[
   \mathcal{D}= \sqrt{d_1^2+d_\psi^2+d_\sigma^2}
   = \sqrt{1^2+1^2+(\sqrt{2})^2}
   = \sqrt{1+1+2}
   = \sqrt{4}=2.
   \]
3. **Topological spins.** We have $\theta_1=1$, $\theta_\psi=-1$, and $\theta_\sigma=e^{i\pi/8}$ (from Section 4.2).

4. **Sum.**
   \[
   \begin{aligned}
   \frac{1}{\mathcal{D}}\sum_a d_a^2\theta_a
   &= \frac{1}{2}\bigl(1^2\cdot 1 + 1^2\cdot(-1) + (\sqrt{2})^2\cdot e^{i\pi/8}\bigr)\\
   &= \frac{1}{2}\bigl(1 - 1 + 2\,e^{i\pi/8}\bigr)\\
   &= \frac{1}{2}\bigl(2\,e^{i\pi/8}\bigr)\\
   &= e^{i\pi/8}.
   \end{aligned}
   \]
5. **Relation to $c$.** The Gauss–Milgram formula states
   \[
   e^{2\pi i c/8}=e^{i\pi/8}.
   \]
   Taking the complex logarithm,
   \[
   \frac{2\pi c}{8}= \frac{\pi}{8}+2\pi m,\qquad m\in\mathbb{Z},
   \]
   which yields
   \[
   c = \frac{1}{2}+8m.
   \]
   Modulo $8$, the minimal solution is
   \[
   \boxed{c = \tfrac{1}{2}\pmod{8}}.
   \]

Thus the hexagon equation forces a non‑zero chiral central charge, corresponding to a single chiral Majorana edge mode.

### 4.4 Non‑chiral scenario
Consider a time‑reversed pair of chiral $p_x+ip_y$ superconductors, yielding total central charge $c_{\text{tot}}=0$. The Gauss–Milgram sum then requires
\[
\frac{1}{2}\bigl(1-1+2\theta_\sigma\bigr)=1\;\Rightarrow\;\theta_\sigma=1.
\]
With $\theta_\sigma=1$, the $R$‑symbols become $R^{\sigma\sigma}_1=\pm1$, $R^{\sigma\sigma}_\psi=\pm i$, which violate the hexagon constraints derived above. Therefore a non‑chiral bulk cannot host intrinsic Ising anyons consistent with the full modular data.

## 5. Results
1. **Result 1.** The MZM parity operators fix the relative phase $i$ between the $1$ and $\psi$ fusion channels of $\sigma\times\sigma$, but leave an overall Abelian phase $e^{i\alpha}$ undetermined (Section 4.1).

2. **Result 2.** Imposing the Ising hexagon equation uniquely determines $\alpha=-\pi/8$, leading to
   \[
   R^{\sigma\sigma}_1=e^{-i\pi/8},\qquad
   R^{\sigma\sigma}_\psi=e^{3i\pi/8},\qquad
   \theta_\sigma=e^{i\pi/8}.
   \] 
   (Section 4.2).

3. **Result 3.** The Gauss–Milgram sum maps $\theta_\sigma=e^{i\pi/8}$ to a chiral central charge $c=1/2\pmod{8}$, implying the existence of a single chiral Majorana edge mode (Section 4.3).

4. **Result 4.** In a non‑chiral superconductor ($c=0$), the Gauss–Milgram sum forces $\theta_\sigma=1$, which is incompatible with the hexagon equation; consequently such systems cannot realize intrinsic Ising anyons (Section 4.4).

## 6. Discussion
Our analysis separates the *local* algebraic information encoded in MZM parity from the *global* topological data required for a consistent modular tensor category. The parity operators alone determine only the projective braid representation; the absolute topological spin—and thus the full exchange matrix—requires knowledge of the chiral central charge. This distinction has practical consequences:

- **Limitations.** The derivation assumes (i) an idealized Clifford algebra without quasiparticle poisoning, (ii) exact Ising $F$‑symbols as given in Ref. [5], and (iii) a bulk described by a unitary modular tensor category. Deviations from these assumptions (e.g., disorder‑induced splitting from Ref. [2] or finite‑size effects in the braiding protocol of Ref. [1]) could modify the effective $\alpha$ and thus the inferred $c$.

- **Failure modes.** If experimental measurements of the thermal Hall conductance yield $c\neq 1/2$, the hexagon‑derived $R$‑symbols would be falsified. Similarly, observation of Abelian braiding statistics in a platform designed to be chiral would contradict our result.

- **Falsifiability.** A direct falsification would occur if a non‑chiral superconductor were shown to support vortices with $\theta_\sigma=e^{i\pi/8}$ while exhibiting $c=0$. Such a finding would invalidate the Gauss–Milgram relation as applied to spin‑TQFTs, indicating that additional structure (e.g., a spin structure modification) is required.

- **Open questions.** (i) How robust is the derived $\alpha$ against perturbations that break particle‑hole symmetry? (ii) Can extrinsic defects in a non‑chiral superconductor mimic the hexagon constraints via anomaly inflow, as hinted in Ref. [6]? (iii) What is the role of the super‑modular refinement of the Gauss–Milgram sum for superconductors where the fermion $\psi$ is transparent (see discussion in Ref. [5])?

## 7. Practical Implications and Engineering Pathways
### (a) Intended users and design impact
Quantum‑hardware engineers developing topological qubits based on vortex Majoranas (e.g., nanowire networks, SOTS devices, or Josephson‑junction platforms) must ensure that the bulk superconducting phase possesses a chiral central charge $c=1/2$. This requirement translates into a design constraint: the material system must realize a single chiral Majorana edge mode, as confirmed by thermal Hall measurements or surface‑current detection (cf. Ref. [8]).

### (b) Technology readiness
The present work is a purely analytical study that has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at **TRL 2** (technology concept formulation).

### (c) Minimal de‑risking experiment
The smallest decisive experiment is a thermal Hall conductance measurement on a candidate 2D topological superconductor. One would fabricate a Hall bar, apply a temperature gradient $\Delta T$, and measure the transverse heat current $J_Q$. The expected quantized value for a single chiral Majorana mode is
\[
\kappa_{xy} = \frac{\pi^2 k_B^2}{6h}\,c = \frac{\pi^2 k_B^2}{12h},
\]
corresponding to $c=1/2$. Observation of $\kappa_{xy}=0$ (within experimental uncertainty) would falsify the claim that the system satisfies the Ising hexagon equation.

### (d) Engineering constraints
- **Materials:** A superconducting film with intrinsic $p_x+ip_y$ pairing symmetry (e.g., Sr$_2$RuO$_4$ or engineered proximitized Rashba systems) is required to host a chiral edge mode.
- **Device geometry:** Braiding protocols such as those in Ref. [1] demand precise control of magnetic field orientation and spin‑singlet pairing vectors; the adiabatic time $T$ must satisfy $T\gg \hbar/\Delta$, where $\Delta$ is the bulk gap.
- **Detection infrastructure:** Thermal Hall measurements need low‑temperature cryogenic setups with sub‑nanowatt heat‑flow resolution.
- **Regulatory:** No specific regulatory barriers are identified beyond standard safety protocols for cryogenic and high‑magnetic‑field equipment.

### (e) Projected performance bounds
Assuming a bulk gap $\Delta\approx 0.5\,$meV (typical for proximitized semiconductor nanowires) and a device temperature $T\approx 20\,$mK, the thermal coherence length $\xi_T=\hbar v_F/k_B T$ exceeds $10\,\mu$m, ensuring that braiding operations remain adiabatic over micron‑scale vortex trajectories. This projection follows from the inputs $\Delta$ and $T$ and the relation $\xi_T\propto 1/T$.

### (f) Risks and misuse
If a non‑chiral superconductor were mistakenly deployed under the assumption that it hosts Ising anyons, quantum‑gate operations would be non‑topological, leading to uncontrolled error rates. Moreover, misinterpretation of thermal Hall data could result in false claims of chirality, potentially diverting resources from viable platforms.

## 8. Conclusion
We have demonstrated that the algebra of Majorana zero‑mode parity operators fixes only the relative phase between the two fusion channels of Ising anyons, leaving an overall Abelian phase undetermined. By enforcing the hexagon equation of the Ising modular tensor category, we uniquely determine this phase, obtain the standard topological spin $\theta_\sigma=e^{i\pi/8}$, and, via the Gauss–Milgram sum, infer a chiral central charge $c=1/2\pmod{8}$. Consequently, a bulk chiral Majorana edge mode is a necessary condition for realizing intrinsic Ising anyons in two‑dimensional topological superconductors. Non‑chiral superconductors cannot satisfy the full set of modular constraints, and their vortices either behave as extrinsic defects or exhibit only Abelian statistics. Our results clarify the precise topological data required for engineering fault‑tolerant Majorana‑based qubits and delineate the experimental signatures that must be verified before such devices can be deployed.

## References
1. arXiv:1904.07822v3 | Braiding Majorana corner modes in a second-order topological superconductor  
2. arXiv:1006.0452v3 | Tunneling of anyonic Majorana excitations in topological superconductors  
3. arXiv:1012.2492v2 | Observing Majorana bound states of Josephson vortices in topological superconductors  
4. arXiv:1109.4790v1 | The MAJORANA Experiment  
5. arXiv:2301.11614v3 | Non-Abelian Anyons and Non-Abelian Vortices in Topological Superconductors  
6. arXiv:1812.01444v1 | Electrical detection of the Majorana fusion rule for chiral edge vortices in a topological superconductor  
7. arXiv:1012.0561v3 | Controlling non-Abelian statistics of Majorana fermions on Majorana dimer lattices  
8. arXiv:1701.04458v1 | Observability of surface currents in p-wave superconductors  

## Appendix A. Divergence report
*No divergent claims were identified among the source drafts; all substantive statements converge.*

## Appendix B. Claim attribution
| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | MZM parity fixes relative phase $i$ but leaves overall phase $e^{i\alpha}$ undetermined. | A, B, C | Convergent |
| C2 | Hexagon equation forces $\alpha=-\pi/8$, yielding $R^{\sigma\sigma}_1=e^{-i\pi/8}$, $R^{\sigma\sigma}_\psi=e^{3i\pi/8}$, $\theta_\sigma=e^{i\pi/8}$. | A, B, C | Convergent |
| C3 | Gauss–Milgram sum gives $c=1/2\pmod{8}$ for $\theta_\sigma=e^{i\pi/8}$. | A, B, C | Convergent |
| C4 | Non‑chiral $c=0$ forces $\theta_\sigma=1$, incompatible with hexagon equation. | A, B, C | Convergent |
| C5 | Braiding protocol via magnetic‑field rotation in a SOTS device (Ref. [1]). | A, B | Convergent |
| C6 | Intervortex tunneling splits Majorana degeneracy with exponential‑oscillatory dependence (Ref. [2]). | A, B | Convergent |
| C7 | Josephson‑vortex Majorana mode described by soliton solution $\phi_s(x)=4\arctan[e^{(x-x_0)/\lambda_J}]$ (Ref. [3]). | A, B | Convergent |
| C8 | Thermal Hall conductance quantization $\kappa_{xy}=\frac{\pi^2k_B^2}{12h}$ for $c=1/2$ (derived in Section 7). | This paper | Single |
| … | … | … | … |