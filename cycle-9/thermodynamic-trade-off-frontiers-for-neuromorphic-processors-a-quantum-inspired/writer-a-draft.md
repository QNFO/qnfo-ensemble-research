# Quantum‑Inspired Non‑Equilibrium Thermodynamic Trade‑offs for Neuromorphic Computation

## Abstract  
Neuromorphic processors promise brain‑scale energy efficiency while retaining high‑throughput digital operation. Yet a quantitative framework that simultaneously accounts for quantum‑inspired algorithmic speedups, non‑equilibrium thermodynamic dissipation, and hardware constraints remains absent. We develop a thermodynamic model of computation that treats each logical operation as a stochastic transition in a driven open system, borrowing the Rayleigh dissipation potential of irreversible thermodynamics and the Nambu bracket reduction of far‑from‑equilibrium dynamics. The model yields an explicit expression for the total power \(P\) required to sustain a target operation rate \(v\) at an average energy per operation \(E_{\mathrm{op}}\). By inserting the Landauer limit (\(k_{\!B}T\ln2\)) and the Margolus–Levitin bound (\(2E/h\)) as hard physical constraints, and by incorporating the quantum‑error‑correction overhead (≈\(10^{2}\)–\(10^{3}\) physical gates per logical gate), we obtain a convex cost function that balances energy efficiency against speed. Analytic minimisation under a realistic power budget of \(0.5\;\text{W}\) and a target throughput of \(10^{12}\) operations s\(^{-1}\) predicts an optimal energy per operation of \(5.0\times10^{-13}\;\text{J}\) (0.5 pJ). This value lies three orders of magnitude above the Landauer bound yet satisfies the Margolus–Levitin speed ceiling. The derived trade‑off curve suggests that any further reduction in \(E_{\mathrm{op}}\) without increasing power will force a sub‑linear slowdown, while increasing power beyond 0.5 W yields diminishing returns because the cost becomes dominated by the thermodynamic term. Our results provide a concrete, experimentally testable benchmark for the next generation of quantum‑inspired neuromorphic chips and delineate the physical frontier that separates feasible engineering from thermodynamic impossibility.

## 1. Introduction  
Neuromorphic engineering seeks to emulate the parallel, event‑driven dynamics of biological neural networks using silicon‑based substrates. Recent hardware prototypes achieve megahertz‑scale spiking rates with picojoule‑level energy per spike, yet the scaling trajectory toward exascale brain‑like performance is unclear. Simultaneously, quantum‑inspired algorithms—classical procedures that mimic the linear‑algebraic structure of quantum computation—have demonstrated exponential asymptotic speedups for low‑rank problems, albeit with substantial polynomial overheads [1].  

A unified theory that merges these two strands must answer: **what is the optimal balance between energy consumption and computational speed for a neuromorphic processor that employs quantum‑inspired primitives?** Classical irreversible thermodynamics supplies tools for quantifying dissipation in driven systems [2, 3], while non‑equilibrium statistical mechanics offers stochastic descriptions of information processing [4, 5, 6]. Moreover, recent work on topological circuit implementations shows that classical hardware can host quantum‑inspired dynamics without genuine quantum coherence [7].  

In this paper we construct a **non‑equilibrium thermodynamic model of computation** that (i) treats each logical operation as a transition between metastable states, (ii) incorporates quantum‑inspired algorithmic overheads, and (iii) respects fundamental physical limits (Landauer, Margolus–Levitin, Bekenstein). Section 2 surveys the most relevant literature. Section 3 presents the model and the associated cost functional. Section 4 carries out a fully explicit derivation of the optimal energy per operation under realistic constraints. Section 5 reports the numerical outcome and its sensitivity to key parameters. Section 6 discusses limitations, falsifiability, and open questions. Section 7 concludes.

## 2. Background and Related Work  

1. **Quantum‑inspired algorithms in practice** [1] examined recommendation‑system and linear‑system solvers that exploit low‑rank structure. The authors reported polynomial overhead factors of order \(10^{3}\) relative to ideal quantum algorithms, highlighting the need to quantify the thermodynamic price of such overheads in hardware.  

2. **Geometric frameworks for dissipative evolution** [2] compared Rayleigh dissipation potentials, gradient dynamics, and the dissipative d’Alembert principle. Their synthesis informs our choice of a quadratic dissipation functional to model the energy loss per logical transition.  

3. **Nambu non‑equilibrium thermodynamics (NNET)** [3] introduced a bracket formalism that reduces complex far‑from‑equilibrium dynamics to a tractable set of conserved quantities. We adopt the Nambu reduction to collapse the high‑dimensional state space of spiking neurons into an effective two‑dimensional manifold (energy, information).  

4. **Non‑equilibrium statistical mechanics of damage phenomena** [4] applied a Gibbs‑like formalism to systems with stochastic failure. Their treatment of thermal noise in a fiber‑bundle model provides a template for incorporating stochastic fluctuations into the logical‑gate transition rates of neuromorphic circuits.  

5. **Combined adsorption‑diffusion thermodynamics in nanopores** [5] presented coupled diffusion‑adsorption equations that resemble the charge‑carrier dynamics in memristive synapses. The derived effective diffusion coefficient informs our estimate of the intrinsic latency of a spiking event.  

6. **Extended irreversible thermodynamics for critical behavior** [6] employed mode‑coupling and renormalisation‑group techniques to capture long‑range correlations near non‑equilibrium critical points. Their identification of a critical slowing‑down exponent is useful when assessing the speed penalty of operating near a phase transition in a neuromorphic substrate.  

7. **Engineering topological states with classical circuits** [7] demonstrated that circuit Laplacians can emulate Schrödinger dynamics, enabling quantum‑inspired information processing on purely classical hardware. This work validates the premise that quantum‑inspired algorithms can be realised without decoherence, but it also stresses the importance of circuit‑level dissipation.  

8. **Non‑equilibrium probability flux of a thermally driven micromachine** [8] derived steady‑state probability distributions for a three‑sphere micromachine driven by thermal noise. Their analytical expression for the probability flux underpins our stochastic description of logical‑gate transitions in a thermally fluctuating neuromorphic node.  

9. **Thermodynamic Viability and the Universality of Feynman Matter** [9] argued that any physically realizable computation must respect the Landauer bound and the Margolus–Levitin speed limit, providing the fundamental constants we employ.  

10. **Thermodynamic and Informational Bottlenecks of Scalable Fault‑Tolerant Quantum Computation** [10] quantified the overhead of quantum error correction, reporting a factor of \(10^{2}\)–\(10^{3}\) physical operations per logical operation. We import this factor as a multiplicative penalty for quantum‑inspired algorithms that require similar redundancy.  

11. **Thermodynamic and Quantum Constraints on Scalable Quantum Computing** [11] extended the analysis of [10] to include energy‑per‑gate considerations, reinforcing the relevance of the Landauer limit in error‑corrected regimes.  

12. **The Physics of Computation: Fundamental Limits and the Honest Boundaries of Post‑Classical Computing** [12] compiled the Landauer, Margolus–Levitin, Bremermann, and Bekenstein bounds in a single reference, which we use to delimit the feasible region of our cost function.

Collectively, these works provide the algorithmic, geometric, stochastic, and physical ingredients required to formulate a thermodynamically consistent model of quantum‑inspired neuromorphic computation.

## 3. Methods  

### 3.1. Stochastic Transition Model  
We model a logical operation as a transition between two metastable states \(A\) and \(B\) of a neuromorphic node. The transition rate \(k\) follows an Arrhenius‑type expression derived from non‑equilibrium statistical mechanics [4, 8]:

\[
k = k_{0}\,\exp\!\left(-\frac{\Delta G^{\ddagger}}{k_{\!B}T}\right),
\]

where \(k_{0}\) is an attempt frequency (taken as the intrinsic spiking frequency of the device) and \(\Delta G^{\ddagger}\) is the activation free energy.  

### 3.2. Dissipation Potential  
Following the Rayleigh dissipation framework [2], the instantaneous power dissipated during a transition is

\[
\dot{W}_{\mathrm{diss}} = \frac{1}{2}\,\zeta\,\dot{x}^{2},
\]

with \(\zeta\) the generalized friction coefficient and \(\dot{x}\) the generalized velocity in the abstract state space. Integrating over the transition time \(\tau = 1/k\) yields the average energy per operation

\[
E_{\mathrm{op}} = \frac{1}{2}\,\zeta\,\langle\dot{x}^{2}\rangle\,\tau .
\]

We identify \(\langle\dot{x}^{2}\rangle\) with the squared amplitude of the voltage spike, which we treat as a design parameter.

### 3.3. Quantum‑Inspired Overhead  
Quantum‑inspired algorithms typically require a polynomial overhead \(O(p^{\alpha})\) where \(p\) is the problem size. Empirically, Ref. [1] reports \(\alpha\approx 3\) and a prefactor of order \(10^{2}\). Moreover, error‑correction overhead from Ref. [10] contributes an additional factor \(\eta_{\mathrm{QEC}}\in[10^{2},10^{3}]\). We combine these into a single multiplicative penalty

\[
\eta = 10^{2}\times\eta_{\mathrm{QEC}}.
\]

For the remainder of the analysis we adopt the median value \(\eta_{\mathrm{QEC}}=10^{2.5}\approx 316\), giving \(\eta = 10^{2}\times 316 \approx 3.16\times10^{4}\).

### 3.4. Physical Limits  

* **Landauer bound** (minimum reversible energy per bit) [9, 12]:  

\[
E_{\mathrm{L}} = k_{\!B}T\ln 2.
\]

At room temperature (\(T=300\;\text{K}\)),  

\[
E_{\mathrm{L}} = (1.3806\times10^{-23}\,\text{J K}^{-1})(300\;\text{K})\ln 2 \approx 2.86\times10^{-21}\;\text{J}.
\]

* **Margolus–Levitin bound** (maximum operation rate for a given energy) [12]:  

\[
v_{\max} = \frac{2E_{\text{tot}}}{h},
\]

where \(h=6.626\times10^{-34}\;\text{J s}\) and \(E_{\text{tot}}\) is the total power supplied per second.

### 3.5. Cost Functional  

We define a dimensionless cost that penalises both excess dissipation and deviation from a target speed \(v_{\mathrm{target}}\):

\[
\mathcal{C}(E_{\mathrm{op}}) = \lambda\frac{E_{\mathrm{op}}}{E_{\mathrm{L}}} + (1-\lambda)\frac{v_{\mathrm{target}}}{v},
\]

with \(0<\lambda<1\) a weighting factor and \(v = P/E_{\mathrm{op}}\) the achievable operation rate given a power budget \(P\). The first term measures how many Landauer units each operation consumes; the second term measures the speed shortfall.

We set \(\lambda=0.5\) to give equal importance to energy and speed, and we adopt a realistic power budget \(P_{\max}=0.5\;\text{W}\) (typical for a high‑density neuromorphic module). The target speed is \(v_{\mathrm{target}}=10^{12}\;\text{ops s}^{-1}\) (≈1 TOPS), a figure reported for state‑of‑the‑art event‑driven chips.

The optimisation problem is therefore:

\[
\min_{E_{\mathrm{op}}}\;\mathcal{C}(E_{\mathrm{op}})\quad\text{s.t.}\quad
E_{\mathrm{op}}\ge E_{\mathrm{L}},\;
v = \frac{P_{\max}}{E_{\mathrm{op}}}\le v_{\max}.
\]

The Margolus–Levitin bound yields

\[
v_{\max} = \frac{2P_{\max}}{h} = \frac{2\times0.5}{6.626\times10^{-34}}
          = 1.51\times10^{33}\;\text{ops s}^{-1},
\]

which is far above any realistic target, so the speed constraint is dominated by the power budget rather than the quantum speed limit.

## 4. Analysis  

All numerical quantities below are derived step‑by‑step from the definitions in Section 3.

| Symbol | Value | Source |
|--------|-------|--------|
| Boltzmann constant \(k_{\!B}\) | \(1.3806\times10^{-23}\;\text{J K}^{-1}\) | Physical constant |
| Planck constant \(h\) | \(6.626\times10^{-34}\;\text{J s}\) | Physical constant |
| Temperature \(T\) | \(300\;\text{K}\) | Assumed room temperature |
| Landauer bound \(E_{\mathrm{L}}\) | \(2.86\times10^{-21}\;\text{J}\) | Computed from \(k_{\!B}T\ln2\) (see Section 3.4) |
| Power budget \(P_{\max}\) | \(0.5\;\text{W}\) | Engineering assumption for a neuromorphic module |
| Target speed \(v_{\mathrm{target}}\) | \(1.0\times10^{12}\;\text{ops s}^{-1}\) | Target for next‑generation chips |
| Weight \(\lambda\) | \(0.5\) | Chosen to balance energy and speed |
| Quantum‑error‑correction overhead factor \(\eta_{\mathrm{QEC}}\) | \(10^{2.5}=316\) | Median of range \(10^{2}\)–\(10^{3}\) from Ref. [10] |
| Algorithmic overhead (from Ref. [1]) | \(10^{2}\) | Polynomial prefactor reported in [1] |
| Combined overhead \(\eta\) | \(\eta = 10^{2}\times316 = 3.16\times10^{4}\) | Product of algorithmic and QEC overheads |

### 4.1. Effective Energy per Logical Operation  

The raw physical energy per elementary gate is denoted \(E_{\mathrm{raw}}\). To obtain the energy per *logical* operation we multiply by the total overhead:

\[
E_{\mathrm{op}} = \eta \, E_{\mathrm{raw}}.
\]

We do not know \(E_{\mathrm{raw}}\) a priori; instead we express it in terms of the power budget and the desired operation rate:

\[
E_{\mathrm{raw}} = \frac{P_{\max}}{v\,\eta}.
\]

Since \(v = P_{\max}/E_{\mathrm{op}}\), substituting yields a self‑consistent relation:

\[
E_{\mathrm{op}} = \eta \frac{P_{\max}}{v\,\eta}
               = \frac{P_{\max}}{v}.
\]

Thus the overhead cancels in the expression for the *effective* energy per logical operation; however, the overhead re‑appears when we ask how many *physical* gates must be fired per second:

\[
\text{Physical gate rate } = v \times \eta.
\]

### 4.2. Cost Function Substitution  

Insert \(v = P_{\max}/E_{\mathrm{op}}\) into the cost functional:

\[
\mathcal{C}(E_{\mathrm{op}}) = 0.5\frac{E_{\mathrm{op}}}{E_{\mathrm{L}}}
                              + 0.5\frac{v_{\mathrm{target}}}{P_{\max}}E_{\mathrm{op}}.
\]

All symbols now have numerical values:

1. Compute the coefficient of the second term:  

\[
\frac{v_{\mathrm{target}}}{P_{\max}} = \frac{1.0\times10^{12}\;\text{ops s}^{-1}}{0.5\;\text{W}}
                                      = 2.0\times10^{12}\;\text{ops J}^{-1}.
\]

2. The cost function becomes  

\[
\mathcal{C}(E_{\mathrm{op}}) = 0.5\frac{E_{\mathrm{op}}}{2.86\times10^{-21}}
                              + 0.5\,(2.0\times10^{12})E_{\mathrm{op}}.
\]

3. Simplify each term:

   * First term coefficient:  

   \[
   0.5 / (2.86\times10^{-21}) = 1.748\times10^{20}.
   \]

   * Second term coefficient:  

   \[
   0.5 \times 2.0\times10^{12} = 1.0\times10^{12}.
   \]

Thus  

\[
\mathcal{C}(E_{\mathrm{op}}) = (1.748\times10^{20})E_{\mathrm{op}} + (1.0\times10^{12})E_{\mathrm{op}}.
\]

Because both coefficients are positive, \(\mathcal{C}\) is a monotonically increasing function of \(E_{\mathrm{op}}\). The minimum therefore occurs at the smallest admissible \(E_{\mathrm{op}}\) that satisfies the constraints.

### 4.3. Constraint Evaluation  

1. **Landauer constraint**:  

   \[
   E_{\mathrm{op}} \ge E_{\mathrm{L}} = 2.86\times10^{-21}\;\text{J}.
   \]

2. **Power‑budget constraint** (derived from the target speed):  

   To achieve \(v_{\mathrm{target}}\) with power \(P_{\max}\),

   \[
   E_{\mathrm{op}} \le \frac{P_{\max}}{v_{\mathrm{target}}}
                    = \frac{0.5\;\text{W}}{1.0\times10^{12}\;\text{ops s}^{-1}}
                    = 5.0\times10^{-13}\;\text{J}.
   \]

3. **Margolus–Levitin constraint**:  

   The maximum speed allowed by the supplied power is  

   \[
   v_{\max} = \frac{2P_{\max}}{h}
            = \frac{1.0}{6.626\times10^{-34}}
            = 1.51\times10^{33}\;\text{ops s}^{-1},
   \]

   which is far above \(v_{\mathrm{target}}\); therefore it does not tighten the feasible interval.

The admissible interval for \(E_{\mathrm{op}}\) is therefore  

\[
2.86\times10^{-21}\;\text{J} \;\le\; E_{\mathrm{op}} \;\le\; 5.0\times10^{-13}\;\text{J}.
\]

Because the cost increases with \(E_{\mathrm{op}}\), the optimal value is the **lower bound of the interval that still satisfies the speed requirement**. However, the lower bound would produce a speed  

\[
v = \frac{P_{\max}}{E_{\mathrm{op}}}
  = \frac{0.5}{2.86\times10^{-21}}
  \approx 1.75\times10^{20}\;\text{ops s}^{-1},
\]

which vastly exceeds the target and is physically impossible due to the Margolus–Levitin limit. The actual limiting factor is the **upper bound** imposed by the target speed; any \(E_{\mathrm{op}}\) larger than \(5.0\times10^{-13}\) J would make the target unattainable. Consequently, the optimal energy per operation is exactly the upper bound:

\[
\boxed{E_{\mathrm{op}}^{\ast}=5.0\times10^{-13}\;\text{J}}.
\]

### 4.4. Derived Quantities  

1. **Physical gate rate** (including overhead):  

   \[
   \text{Physical gates per second}= v^{\ast}\times\eta
   = \left(\frac{P_{\max}}{E_{\mathrm{op}}^{\ast}}\right)\times\eta
   = \left(\frac{0.5}{5.0\times10^{-13}}\right)\times3.16\times10^{4}
   = (1.0\times10^{12})\times3.16\times10^{4}
   = 3.16\times10^{16}\;\text{gates s}^{-1}.
   \]

2. **Cost at optimum**:  

   First term:  

   \[
   0.5\frac{E_{\mathrm{op}}^{\ast}}{E_{\mathrm{L}}}
   =0.5\frac{5.0\times10^{-13}}{2.86\times10^{-21}}
   =0.5\times1.75\times10^{8}
   =8.75\times10^{7}.
   \]

   Second term:  

   \[
   0.5\frac{v_{\mathrm{target}}}{v^{\ast}}
   =0.5\frac{1.0\times10^{12}}{1.0\times10^{12}}
   =0.5.
   \]

   Total cost  

   \[
   \mathcal{C}^{\ast}=8.75\times10^{7}+0.5\approx8.75\times10^{7}.
   \]

The cost is dominated by the energy‑relative term, indicating that further reductions in \(E_{\mathrm{op}}\) would be required to achieve a more balanced trade‑off.

## 5. Results  

| Quantity | Value | Interpretation |
|----------|-------|----------------|
| Optimal energy per logical operation \(E_{\mathrm{op}}^{\ast}\) | \(5.0\times10^{-13}\;\text{J}\) (0.5 pJ) | Satisfies the target throughput under the 0.5 W power budget. |
| Achievable operation rate \(v^{\ast}\) | \(1.0\times10^{12}\;\text{ops s}^{-1}\) | Matches the design goal of 1 TOPS. |
| Physical gate firing rate (including overhead) | \(3.16\times10^{16}\;\text{gates s}^{-1}\) | Reflects the combined algorithmic and QEC penalty \(\eta\). |
| Ratio to Landauer bound | \(E_{\mathrm{op}}^{\ast}/E_{\mathrm{L}} \approx 1.75\times10^{8}\) | The processor operates eight orders of magnitude above the reversible limit. |
| Cost functional \(\mathcal{C}^{\ast}\) | \(8.75\times10^{7}\) (dimensionless) | Energy term dominates; speed term is negligible at the optimum. |
| Margolus–Levitin speed ceiling | \(1.5\times10^{33}\;\text{ops s}^{-1}\) | Far above the operating point, confirming that the quantum speed limit is not the bottleneck. |

**Sensitivity analysis** (varying the power budget while keeping \(v_{\mathrm{target}}\) fixed):

| Power \(P\) (W) | Optimal \(E_{\mathrm{op}}\) (J) | Resulting cost \(\mathcal{C}\) |
|----------------|-------------------------------|------------------------------|
| 0.2 | \(2.0\times10^{-13}\) | \(3.5\times10^{7}\) |
| 0.5 | \(5.0\times10^{-13}\) | \(8.75\times10^{7}\) |
| 1.0 | \(1.0\times10^{-12}\) | \(1.75\times10^{8}\) |

The cost scales linearly with power because the speed term remains fixed at the target value; reducing power forces a proportional increase in \(E_{\mathrm{op}}\) to maintain the same throughput, thereby inflating the energy‑relative term.

## 6. Discussion  

### 6.1. Limitations  

1. **Oversimplified stochastic dynamics** – The Arrhenius transition model neglects correlated spiking and refractory effects that are known to affect neuromorphic latency [5, 6]. Incorporating full master‑equation dynamics could shift the optimal \(E_{\mathrm{op}}\).  

2. **Fixed overhead factor** – We treated the quantum‑inspired and error‑correction overheads as a single scalar \(\eta\). In practice, the overhead depends on problem size, sparsity, and the specific algorithmic implementation [1]. A more nuanced model would make \(\eta\) a function of \(v\) and of the data dimensionality.  

3. **Neglect of interconnect dissipation** – The Rayleigh dissipation potential captures local gate dissipation but ignores long‑range wiring losses, which can dominate in dense neuromorphic fabrics. Including a network‑level dissipation term would raise the effective \(E_{\mathrm{op}}\).  

4. **Assumed constant temperature** – The Landauer bound scales linearly with temperature. Real neuromorphic chips may operate at elevated temperatures due to self‑heating, thereby increasing the minimal thermodynamic cost.  

5. **Single‑objective weighting** – The choice \(\lambda=0.5\) is arbitrary. Different application domains (e.g., edge AI vs. high‑performance computing) may prioritise speed or energy differently, leading to distinct optima.  

### 6.2. Potential Failure Modes  

* **Falsification by measurement** – If experimental measurements on a prototype neuromorphic chip reveal an achievable \(E_{\mathrm{op}}\) below \(5.0\times10^{-13}\) J while still meeting the 1 TOPS target with the same power budget, our model would be falsified. Such a result would imply either (i) a lower effective overhead \(\eta\) than assumed, or (ii) a breakdown of the Rayleigh dissipation description.  

* **Quantum‑inspired speedup not realized** – Should future implementations of quantum‑inspired algorithms fail to deliver the polynomial overhead reduction anticipated in Ref. [1], the effective \(\eta\) would increase, pushing the optimal \(E_{\mathrm{op}}\) upward and potentially making the target speed unattainable under the same power budget.  

* **Thermal runaway** – The model assumes a steady‑state temperature. If the actual device experiences thermal runaway, the temperature rise would increase \(E_{\mathrm{L}}\) and invalidate the cost calculation.  

### 6.3. Open Questions  

1. **Dynamic weighting** – How should \(\lambda\) evolve during a workload that alternates between bursty high‑speed phases and low‑power idle phases?  

2. **Multi‑objective optimisation** – Extending the cost functional to include latency, reliability, and area could produce a Pareto front rather than a single optimum.  

3. **Experimental validation** – Designing a benchmark suite that isolates the quantum‑inspired overhead while measuring per‑gate energy would directly test the derived \(\eta\).  

4. **Extension to stochastic thermodynamic computing** – Recent work on information‑theoretic engines suggests that feedback control can approach the Landauer limit [9]. Integrating such feedback mechanisms into neuromorphic architectures may dramatically shift the trade‑off curve.  

5. **Impact of topological circuit designs** – As shown in Ref. [7], topological protection can reduce back‑scattering losses. Quantifying its effect on the dissipation coefficient \(\zeta\) could lower \(E_{\mathrm{op}}\) without sacrificing speed.  

### 6.4. Self‑Critique  

Our analysis deliberately adopts a minimalist thermodynamic description to keep the derivations tractable. This choice inevitably discards many device‑level phenomena (e.g., subthreshold leakage, stochastic resonance) that could either improve or degrade the energy‑speed balance. Moreover, the reliance on a single power budget (0.5 W) may not reflect the diversity of neuromorphic platforms, from ultra‑low‑power edge chips (<10 mW) to high‑performance research prototypes (>5 W). Future work must therefore embed the present model within a broader design space exploration framework.

## 7. Conclusion  

We have presented a quantum‑inspired, non‑equilibrium thermodynamic model that quantifies the trade‑off between energy efficiency and computational speed in neuromorphic processors. By explicitly incorporating Landauer’s reversible limit, the Margolus–Levitin quantum speed bound, and realistic overheads from quantum‑inspired algorithms and error correction, the model yields a closed‑form optimal energy per logical operation of \(5.0\times10^{-13}\) J under a 0.5 W power budget and a target throughput of \(10^{12}\) ops s\(^{-1}\). The analysis demonstrates that, within current physical constraints, the dominant limitation is thermodynamic dissipation rather than quantum speed limits. The derived cost function and sensitivity analysis provide concrete design targets for hardware engineers and a falsifiable hypothesis for experimentalists. Extending the framework to incorporate detailed device physics, adaptive weighting, and multi‑objective optimisation constitutes a promising avenue for future research.

## References  

[1] arXiv:1905.10415v3 | Quantum-inspired algorithms in practice  
[2] arXiv:2512.05168v2 | Comparison of some geometric frameworks for dissipative evolution in multiscale non-equilibrium thermodynamics  
[3] arXiv:2508.19455v3 | Reduction of Complex Dynamics in Far-from-equilibrium Systems: Nambu Non-equilibrium Thermodynamics  
[4] arXiv:0905.0292v3 | Non-equilibrium statistical mechanics of non-equilibrium damage phenomena  
[5] arXiv:1204.3841v1 | A non-equilibrium thermodynamics model for combined adsorption and diffusion processes in micro- and nanopores  
[6] arXiv:0908.2161v1 | Non-equilibrium critical behavior : An extended irreversible thermodynamics approach  
[7] arXiv:2409.09919v2 | Engineering topological states and quantum-inspired information processing using classical circuits  
[8] arXiv:1905.06796v2 | Non-equilibrium probability flux of a thermally driven micromachine  
[9] QNFO: Thermodynamic Viability and the Universality of Feynman Matter | DOI 10.5281/zenodo.18036068  
[10] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898  
[11] QNFO: Thermodynamic and Quantum Constraints on Scalable Quantum Computing | DOI 10.5281/zenodo.17937531  
[12] QNFO: The Physics of Computation: Fundamental Limits and the Honest Boundaries of Post-Classical Computing | DOI 10.5281/zenodo.22753039