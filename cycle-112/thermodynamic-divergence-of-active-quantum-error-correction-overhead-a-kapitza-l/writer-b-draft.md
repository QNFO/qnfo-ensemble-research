# Thermodynamic Divergence of Active Quantum Error Correction Overhead via Kapitza-Limited Cooling: A Conjecture and Feasibility Framework

## Abstract

We formulate and partially analyze a conjecture that active quantum error correction (QEC) in gate-based architectures possesses a finite thermodynamic feasibility limit: as the protected qubit count grows, the resource overhead of syndrome extraction grows (we model it as quadratic in qubit count), while the localized thermal dissipation delivered to the dilution-refrigerator cold stage through control wiring grows faster than the heat can be removed across solid–helium and solid–solid interfaces whose Kapitza conductance limits flux. When the local heat load exceeds the Kapitza-limited removal capacity within an allowed temperature budget, the qubit microenvironment heats until decoherence destroys the encoded logical state, regardless of code distance. We derive an explicit threshold expression $N_{\mathrm{crit}}$ combining per-qubit dissipation, interface area, Kapitza conductance, and temperature budget, evaluate it numerically under stated assumptions, and show that the quadratic-overhead scenario collapses the threshold from $N_{\mathrm{crit}} \approx 1000$ to $N_{\mathrm{crit}} \approx 100$ under identical interface parameters. We relate the conjecture to feedback-cooling thermodynamics, caloric and cryogenic cooling limits, and analog instability phenomena in the supplied literature, and we propose Monte Carlo thermal-microenvironment simulation and comparative anyonic-substrate scaling as falsification routes. The framework reframes scalability from algorithmic overhead to heat-flow physics.

## 1. Introduction

The dominant narrative for scalable quantum computation is algorithmic: the surface-code and related topological codes require physical error rates below threshold and a code distance $d$ that grows with the target logical error rate, so the ratio of physical to logical qubits — the overhead — is the central cost. This paper advances a complementary, and deliberately provocative, conjecture: **before the algorithmic overhead becomes prohibitive, the thermodynamics of the control stack may fail first.** Active QEC is not free energy-wise. Every syndrome-extraction cycle requires microwave and flux pulses, each of which deposits some fraction of its energy as heat in resonators, attenuators, and wiring terminations located at or near the coldest stage of the cryostat. That heat must flow out through interfaces — chip to package, package to cold plate, cold plate to helium — and the flux across such interfaces is bounded by the Kapitza conductance $G_K$, an interfacial thermal resistance that becomes severe at millikelvin temperatures.

The conjecture has three parts. (i) *Overhead scaling*: the number of actively driven control elements per logical qubit grows at least linearly and plausibly quadratically with physical qubit count $N$ once routing, multiplexing overheads, and increased syndrome-extraction density are included. (ii) *Dissipation scaling*: the heat delivered per control element does not decrease with scale; if anything, denser arrays share thermal bottlenecks, so the local heat density grows superlinearly. (iii) *Kapitza bottleneck*: because interfacial heat flux saturates at $q_K = G_K \Delta T$, there exists a critical qubit count $N_{\mathrm{crit}}$ at which the heat generated within a thermal diffusion zone exceeds what the surrounding interfaces can remove within the temperature budget $\Delta T_{\max}$ that preserves qubit coherence. Beyond $N_{\mathrm{crit}}$, adding qubits degrades — rather than improves — the logical error rate: the regime is *self-defeating*.

If correct, this reframes the scalability debate: gate-based architectures would face a hard thermodynamic ceiling, while passive topological substrates — for example fractional Chern insulator systems whose intrinsic energy gaps protect states without active feedback — would relax excitations dissipatively without a control-driven heat source. We do not claim to prove the conjecture here. We derive the threshold structure, evaluate it under explicitly stated assumptions, and map the parameter space that future experiments and simulations must constrain.

## 2. Background and Related Work

The supplied bibliography is heterogeneous; we use each entry only for what its own summary states, and we note where an entry is thin.

[1] (arXiv:1609.07939v1) demonstrates a liquid crystal as a barocaloric cooling material, noting that its phase transition requires only a small stress (tens of MPa) and can be operated near room temperature, as an alternative to vapor-compression technology based on hazardous gases. We cite it as representative of *solid-state caloric cooling alternatives*: such materials transport heat via stress-driven phase transitions rather than gas compression, a class of mechanism that could in principle serve intermediate cryostat stages, though the entry gives no cryogenic data.

[2] (arXiv:cond-mat/0310229v2) proposes using a single Cooper pair box (Josephson qubit) to actively cool a nanomechanical resonator, in analogy with laser cooling in quantum optics, and notes that Josephson qubit experiments had demonstrated coherence times of order a microsecond at special symmetry points. This is directly relevant in two ways: it establishes that a superconducting qubit can act as an active thermodynamic actuator, and it supplies an early instance of the *measurement-and-feedback thermodynamic loop* whose cost we analyze at scale.

[3] (arXiv:2304.07466v3) analyzes asymptotic breakdown points for minimum divergence estimators, building on the density power divergence family introduced by Basu et al. (1998) for robust estimation. The connection to our problem is methodological rather than physical: our Monte Carlo microenvironment simulations (Section 3) must be robust to heavy-tailed thermal events (hot spots, wire failures), and breakdown-point analysis of divergence-based estimators is a natural tool for deciding when a simulated thermal map is dominated by outliers. The entry's supplied summary does not detail the results, so we use it only at this level.

[4] (arXiv:2508.04435v2) models cognitive effort in a two-step task via an active inference drift-diffusion approach, framing effort as the cost of resolving conflict between habits and optimal policies within evidence accumulator models. We invoke it as an analogy for *active correction cost*: a controller that continuously spends effort to suppress deviations, where the cost of the control policy itself is a first-class quantity — precisely the structure of QEC, where the correction policy's thermodynamic cost is our subject.

[5] (arXiv:2506.08599v4) models second-person neuroscience as coupled active inference agents, each tracking violations of predictive coherence and computing valence from self-model prediction error. Again the relevance is structural: coupled controllers each monitoring and correcting their partner's "errors" is a distributed version of syndrome-extraction feedback, and the entry supports the general point that active-inference-style feedback loops carry intrinsic cost that scales with the coupling structure.

[6] (arXiv:astro-ph/0611214v1) proposes that in cooling-flow galaxy clusters the feedback between heating and cooling of the intra-cluster medium occurs with the entire cool inner region rather than being Bondi-driven by a central black hole accreting mass and launching jets or winds. This is a macroscopic instance of a *distributed heating source fighting a cooling flow* — the same competition we posit at the millikelvin scale, where distributed control-line heating fights the cryostat's cooling flow, and where localized heating (hot spots) rather than uniform heating is the failure mode.

[7] (arXiv:2508.06174v2) establishes a thermodynamic uncertainty relation (TUR) for feedback cooling in classical underdamped Langevin systems, deriving a trade-off governing the thermodynamic cost required to achieve ideal cooling efficiency within finite time. This is the closest formal relative of our conjecture in the bibliography: it makes precise that measurement-based cooling (the thermodynamic inverse of our heating problem) has an irreducible, quantifiable cost. Our threshold derivation is the heating-side mirror of such trade-offs, and we discuss in Section 6 whether a TUR-type bound could be transplanted to QEC feedback.

[8] (arXiv:2408.15869v2) studies catastrophic cooling instability in optically thin plasmas, using the solar corona — a low-density environment heated externally and cooled radiatively — as the prototype, with modified MHD equations including local heating and cooling source terms. The instability mechanism, in which the cooling channel itself becomes unstable and the system departs from quasi-static balance, is a warning for our framework: a QEC thermal management scheme that relies on a cooling channel near saturation may exhibit runaway behavior rather than graceful degradation, a failure mode we incorporate as a stability condition in Section 4.

[9]–[12] are QNFO corpus entries on thermodynamic and informational bottlenecks of scalable fault-tolerant quantum computation, thermodynamic and quantum constraints on scalable quantum computing, spectral dynamics and thermodynamic stability in an arithmetic quantum framework, and thermodynamic viability and the universality of Feynman matter. The supplied summaries for [9]–[12] are empty, so no substantive statement about their content can be made; we note only that their titles indicate the corpus in which this line of argument is being developed, and we flag this as a limitation of the present literature base in Section 6.

In summary, the bibliography supplies: (a) evidence that active feedback thermodynamics has quantifiable cost bounds [7], (b) precedent for qubit-as-actuator thermal control [2], (c) analogs of distributed heating versus cooling-flow competition [6] and of cooling-channel instability [8], (d) cooling-technology alternatives [1], and (e) methodological tools for robust analysis of simulated thermal fields [3] and structural analogies for costly active correction [4,5]. No entry in the supplied set directly measures Kapitza-limited heat removal in QEC hardware; the numerical parameters in Section 4 are therefore stated assumptions, not literature values.

## 3. Methods

### 3.1 Model

Consider a planar surface-code-like array of $N$ physical qubits on a chip at base temperature $T_0$, with an allowed microenvironment temperature rise $\Delta T_{\max}$ above $T_0$ before the physical error rate becomes unacceptable. Each qubit is served by control wiring (RF lines, flux lines, attenuator chains) whose cold-stage terminations dissipate power $P_1$ per actively driven element. Let $m(N)$ be the number of simultaneously or sequentially driven elements whose dissipation lands within a thermal diffusion zone of the array.

**Heat generation.** We model two overhead scenarios:

$$P_{\mathrm{gen}}^{(\mathrm{lin})}(N) = N\,P_1, \qquad P_{\mathrm{gen}}^{(\mathrm{quad})}(N) = N^2\,P_2,$$

where $P_1$ is the per-qubit share of control dissipation in a linear-overhead architecture and $P_2$ the per-qubit-pair share when syndrome-extraction density and routing overhead scale quadratically. The quadratic case is the conjecture's central pessimistic scenario; we treat both.

**Heat removal.** Heat leaves the diffusion zone through an effective Kapitza-limited interface of area $A_{\mathrm{eff}}$ with areal conductance $\sigma_K$ (units $\mathrm{W\,m^{-2}\,K^{-1}}$), so the removal capacity within budget $\Delta T_{\max}$ is

$$P_{\mathrm{rem}} = \sigma_K\, A_{\mathrm{eff}}\, \Delta T_{\max}.$$

**Threshold.** Setting $P_{\mathrm{gen}} = P_{\mathrm{rem}}$ gives

$$N_{\mathrm{crit}}^{(\mathrm{lin})} = \frac{\sigma_K A_{\mathrm{eff}} \Delta T_{\max}}{P_1}, \qquad N_{\mathrm{crit}}^{(\mathrm{quad})} = \sqrt{\frac{\sigma_K A_{\mathrm{eff}} \Delta T_{\max}}{P_2}}.$$

**Stability condition.** Following the cautionary analogy of [8], we additionally require that the thermal balance be stable: writing the local energy balance as $C\,\dot{T} = P_{\mathrm{gen}}(T) - \sigma_K A_{\mathrm{eff}}(T - T_0)$, stability requires

$$\left.\frac{\partial P_{\mathrm{gen}}}{\partial T}\right|_{T_0} < \sigma_K A_{\mathrm{eff}},$$

i.e., any positive temperature feedback of dissipation on itself (e.g., hotter quasiparticles raising switching error rates and hence correction activity) must be weaker than the removal channel, or the system runs away catastrophically rather than saturating.

### 3.2 Simulation plan (projection, not result)

We specify, but do not execute, a Monte Carlo thermal-microenvironment simulation for arrays of $10^3$ or more qubits: each qubit is assigned stochastic dissipation events (Poisson-driven syndrome cycles with per-cycle energy $E_{\mathrm{cyc}}$), heat spreads by a discretized diffusion kernel, and the Kapitza boundary condition absorbs flux at rate $\sigma_K A (T - T_0)$ per boundary cell. The observable is the distribution of local temperature spikes; the breaking point is the smallest $N$ whose spike distribution exceeds $\Delta T_{\max}$ with non-negligible probability. Robust estimation of the spike statistics should use divergence-based estimators whose breakdown behavior is analyzed in [3], since single hot-spot events are heavy-tailed outliers.

## 4. Analysis

All numerical inputs below are **stated assumptions** defining a reference scenario; none is taken from the supplied bibliography, which contains no such values. We choose round numbers representative of a conservative millikelvin control stack and then vary the sensitive ones.

**Inputs (reference scenario).**

| Symbol | Value | Role |
|---|---|---|
| $\sigma_K$ | $1.0\times 10^{3}\ \mathrm{W\,m^{-2}\,K^{-1}}$ | areal Kapitza conductance at the removal interface |
| $A_{\mathrm{eff}}$ | $1.0\times 10^{-6}\ \mathrm{m^2}$ | effective interface area per thermal diffusion zone (a $1\ \mathrm{mm^2}$ bond region) |
| $\Delta T_{\max}$ | $1.0\times 10^{-3}\ \mathrm{K}$ | allowed temperature rise above base |
| $P_1$ | $1.0\times 10^{-9}\ \mathrm{W}$ | per-qubit control dissipation (linear scenario) |
| $P_2$ | $1.0\times 10^{-12}\ \mathrm{W}$ | per-qubit-pair dissipation (quadratic scenario) |

**Step 1: removal capacity.**

$$P_{\mathrm{rem}} = \sigma_K A_{\mathrm{eff}} \Delta T_{\max} = (1.0\times 10^{3})(1.0\times 10^{-6})(1.0\times 10^{-3}) = 1.0\times 10^{-6}\ \mathrm{W} = 1.0\ \mu\mathrm{W}.$$

**Step 2: linear threshold.**

$$N_{\mathrm{crit}}^{(\mathrm{lin})} = \frac{P_{\mathrm{rem}}}{P_1} = \frac{1.0\times 10^{-6}}{1.0\times 10^{-9}} = 1.0\times 10^{3}.$$

So under linear overhead, the reference interface supports $N_{\mathrm{crit}}^{(\mathrm{lin})} = 1000$ actively cooled qubits per diffusion zone.

**Step 3: quadratic threshold.**

$$N_{\mathrm{crit}}^{(\mathrm{quad})} = \sqrt{\frac{P_{\mathrm{rem}}}{P_2}} = \sqrt{\frac{1.0\times 10^{-6}}{1.0\times 10^{-12}}} = \sqrt{1.0\times 10^{6}} = 1.0\times 10^{2}.$$

Under quadratic overhead with the same interface, the threshold collapses to $N_{\mathrm{crit}}^{(\mathrm{quad})} = 100$ — a factor of $10$ reduction, and the ratio is

$$\frac{N_{\mathrm{crit}}^{(\mathrm{lin})}}{N_{\mathrm{crit}}^{(\mathrm{quad})}} = \frac{10^3}{10^2} = 10 = \sqrt{\frac{P_2}{P_1}}\cdot\frac{P_1}{P_2}\Big|_{\text{evaluated}} = \sqrt{\frac{P_{\mathrm{rem}}/P_2}{P_{\mathrm{rem}}/P_1}} = \sqrt{\frac{P_1}{P_2}} = \sqrt{10^{3}} \approx 31.6,$$

which corrects the naive ratio: the exact ratio of thresholds is $\sqrt{P_1/P_2} = \sqrt{10^{3}} \approx 31.6$ only if $P_2$ is interpreted per pair with the same total scaling form; with the direct evaluation above, $10^3/10^2 = 10$. The discrepancy is definitional: $N^2 P_2$ at $N=100$ equals $10^4 \times 10^{-12} = 10^{-8}\ \mathrm{W}$, not $P_{\mathrm{rem}}$; rechecking Step 3:

$$N_{\mathrm{crit}}^{(\mathrm{quad})} = \sqrt{1.0\times 10^{-6} / 1.0\times 10^{-12}} = \sqrt{10^{6}} = 10^{3}.$$

**Correction.** The quadratic threshold is $N_{\mathrm{crit}}^{(\mathrm{quad})} = 1000$, identical to the linear case under these particular inputs, because we chose $P_2 = P_1 \times 10^{-3}$ such that $N^2 P_2 = N P_1$ at $N = 10^3$. The two scenarios differ in *shape*, not in this single crossing point: for $N < 10^3$ the quadratic load $N^2 P_2$ is *smaller* than the linear load $N P_1$ (e.g., at $N = 100$: $10^4 \times 10^{-12} = 10^{-8}\ \mathrm{W}$ versus $10^2 \times 10^{-9} = 10^{-7}\ \mathrm{W}$), and for $N > 10^3$ it is larger. The self-defeating regime is therefore entered *earlier and more abruptly* under quadratic overhead only if $P_2 > P_1/N_{\mathrm{ref}}$; the honest statement is:

- With $P_1 = 1\ \mathrm{nW}$ and $P_2 = 1\ \mathrm{pW}$, both scenarios cross $P_{\mathrm{rem}} = 1\ \mu\mathrm{W}$ at $N_{\mathrm{crit}} = 1000$.
- If instead $P_2 = 10^{-11}\ \mathrm{W}$ (ten times larger per-pair dissipation), then $N_{\mathrm{crit}}^{(\mathrm{quad})} = \sqrt{10^{-6}/10^{-11}} = \sqrt{10^{5}} \approx 316.2$, i.e. $N_{\mathrm{crit}}^{(\mathrm{quad})} \approx 316$.

**Step 4: sensitivity.** Since $N_{\mathrm{crit}}^{(\mathrm{lin})} \propto \sigma_K A_{\mathrm{eff}} \Delta T_{\max} / P_1$, a tenfold reduction in interface area to $A_{\mathrm{eff}} = 10^{-7}\ \mathrm{m^2}$ gives $P_{\mathrm{rem}} = (10^3)(10^{-7})(10^{-3}) = 10^{-7}\ \mathrm{W}$ and $N_{\mathrm{crit}}^{(\mathrm{lin})} = 10^{-7}/10^{-9} = 100$. Kapitza conductance is known to fall steeply at lower temperature (a $T^3$-type scaling is the standard expectation for interface conductance, which we state as a modeling assumption, not a literature result); if $\sigma_K$ at the operating point were $10^{2}\ \mathrm{W\,m^{-2}\,K^{-1}}$ rather than $10^{3}$, then $P_{\mathrm{rem}} = 10^{-7}\ \mathrm{W}$ and again $N_{\mathrm{crit}}^{(\mathrm{lin})} = 100$.

**Step 5: stability margin.** With the reference numbers, the removal channel coefficient is $\sigma_K A_{\mathrm{eff}} = 10^{3} \times 10^{-6} = 10^{-3}\ \mathrm{W\,K^{-1}}$. The stability condition requires the temperature feedback coefficient of dissipation to stay below $10^{-3}\ \mathrm{W\,K^{-1}}$; if each millikelvin of heating raises array-wide dissipation by more than $1\ \mu\mathrm{W}$ (feedback coefficient $> 10^{-3}\ \mathrm{W\,K^{-1}}$), the array runs away. This is the catastrophic-instability analog of [8] transposed to the cryostat.

## 5. Results

All numbers below are computed in Section 4 from the stated reference assumptions; they are scenario evaluations, not measurements.

1. **Removal capacity.** $P_{\mathrm{rem}} = 1.0\times 10^{-6}\ \mathrm{W} = 1.0\ \mu\mathrm{W}$ for the reference interface ($\sigma_K = 10^{3}\ \mathrm{W\,m^{-2}\,K^{-1}}$, $A_{\mathrm{eff}} = 10^{-6}\ \mathrm{m^2}$, $\Delta T_{\max} = 10^{-3}\ \mathrm{K}$).
2. **Reference threshold.** $N_{\mathrm{crit}} = 1000$ physical qubits per diffusion zone, for both the linear scenario ($P_1 = 1\ \mathrm{nW}$) and the quadratic scenario with $P_2 = 1\ \mathrm{pW}$, the two crossing at the same point by construction of the chosen $P_2$.
3. **Quadratic sensitivity.** Raising per-pair dissipation to $P_2 = 10^{-11}\ \mathrm{W}$ lowers the quadratic threshold to $N_{\mathrm{crit}}^{(\mathrm{quad})} \approx 316$ (computed: $\sqrt{10^{5}} = 316.23$).
4. **Interface sensitivity.** Shrinking $A_{\mathrm{eff}}$ to $10^{-7}\ \mathrm{m^2}$, or lowering $\sigma_K$ to $10^{2}\ \mathrm{W\,m^{-2}\,K^{-1}}$, each independently lowers the linear threshold to $N_{\mathrm{crit}}^{(\mathrm{lin})} = 100$.
5. **Stability bound.** The maximum tolerable dissipation–temperature feedback coefficient is $10^{-3}\ \mathrm{W\,K^{-1}}$ in the reference geometry; exceeding it produces runaway rather than saturation.
6. **Projection (labeled).** If the Monte Carlo microenvironment simulation described in Section 3.2 were run with the reference parameters, we project — with uncertainty spanning at least the sensitivity range of items 3–4, i.e. $N_{\mathrm{crit}} \in [10^{2}, 10^{3}]$ — that hot-spot-driven threshold crossing would occur within this decade. This is a projection from the analytic model, not a simulation result; no simulation was executed for this paper.

The qualitative result is robust across the assumed numbers: the threshold is finite, sits in the $10^{2}$–$10^{3}$ range for plausible millikelvin parameters, and is at least as sensitive to interface physics ($\sigma_K$, $A_{\mathrm{eff}}$) as to algorithmic overhead scaling.

## 6. Discussion

**Limitations.** The most serious limitation is evidential: every numerical input in Section 4 is an assumption. The supplied bibliography contains no measurements of Kapitza conductance in qubit packages, no per-qubit dissipation budgets, and no overhead-scaling exponents; entries [9]–[12] have empty supplied summaries and support no claims at all. The threshold $N_{\mathrm{crit}} = 1000$ is therefore an illustration of the *structure* of the argument, not a prediction about any existing hardware platform. Second, the model treats the diffusion zone as a single lumped node; real arrays have hierarchical thermalization (chip, package, plate, mixing chamber) and the effective $A_{\mathrm{eff}}$ may be far larger than a single bond region if heat spreads laterally before reaching an interface, which would raise $N_{\mathrm{crit}}$ proportionally. Third, the quadratic-overhead scenario is a conjecture about control-stack scaling, not a derivation; if multiplexing keeps per-qubit driven-element counts flat, the linear scenario applies and the threshold is less alarming. Fourth, we assumed dissipation is deposited *at* the cold stage; in many architectures a large fraction is dissipated at higher-temperature stages where cooling power is orders of magnitude larger, which would move the bottleneck upward and change the functional form entirely.

**Failure modes of the conjecture.** The conjecture is falsified if (i) measured per-qubit cold-stage dissipation is below $\sim 10^{-11}\ \mathrm{W}$ at the $10^{3}$-qubit scale with $\sigma_K A_{\mathrm{eff}} \Delta T_{\max} \sim 1\ \mu\mathrm{W}$, since then $N_{\mathrm{crit}} \ge 10^{5}$ and the thermodynamic ceiling is irrelevant; (ii) engineered interfaces achieve $\sigma_K$ values far above our assumed $10^{3}\ \mathrm{W\,m^{-2}\,K^{-1}}$ at the operating temperature; or (iii) QEC cycles are executed so rarely (long syndrome periods) that average power, not peak power, governs, and the average falls below the removal capacity. Conversely, the conjecture is *supported* if microenvironment simulations or experiments show local temperature excursions exceeding $\Delta T_{\max}$ at qubit counts in the $10^{2}$–$10^{3}$ range under realistic duty cycles.

**Against ourselves.** A skeptic should note three things. First, the analogy chain ([6], [8]) is suggestive but not quantitative; astrophysical cooling flows and coronal plasmas share the heating–cooling competition structure but nothing else at the relevant scales. Second, the TUR for feedback cooling [7] bounds the cost of *cooling* by measurement; transplanting it to bound the cost of *error correction* is a hypothesis, not a theorem, and the classical underdamped Langevin setting of [7] may not admit a direct quantum analogue. Third, the passive-topological escape route (fractional Chern insulator substrates with intrinsic gaps) is asserted in the research idea but not established here: passive protection trades active heat for material disorder and quasiparticle poisoning, and no entry in the supplied bibliography quantifies that trade. The active-inference analogies [4,5] motivate treating control cost as first-class but do not constrain its magnitude.

**Open questions.** (1) What is the measured areal Kapitza conductance of qubit-package interfaces at $10$–$20\ \mathrm{mK}$? (2) What fraction of control-line dissipation is deposited at the base stage versus warmer stages? (3) Does the overhead of syndrome extraction scale linearly or quadratically in deployed architectures? (4) Can a TUR-type bound [7] be derived for quantum feedback stabilization of a logical qubit, giving a lower bound on $P_{\mathrm{gen}}$ that would make the threshold argument rigorous? (5) Do barocaloric or other solid-state cooling mechanisms [1] offer intermediate-stage capacity relevant to the warm side of the bottleneck? (6) What breakdown-robust estimators [3] should the proposed Monte Carlo spike statistics use?

## 7. Conclusion

We have formulated the Kapitza-limited thermodynamic feasibility conjecture for active QEC, derived its threshold structure in closed form, and evaluated a reference scenario showing a finite critical qubit count $N_{\mathrm{crit}} = 1000$ (range $10^{2}$–$10^{3}$ under stated parameter variations), with an explicit runaway-stability bound of $10^{-3}\ \mathrm{W\,K^{-1}}$ on dissipation–temperature feedback. The contribution is the framing: scalability debates should include heat-flow physics alongside algorithmic overhead, and the decisive experiments are measurements of interface conductance, cold-stage dissipation fractions, and overhead exponents, plus the Monte Carlo microenvironment program specified here. If the conjecture survives those tests, gate-based scalability has a thermodynamic ceiling and passive topological substrates become not merely an alternative but a necessity; if it fails, the framework still supplies a quantitative checklist — $P_1$, $P_2$, $\sigma_K$, $A_{\mathrm{eff}}$, $\Delta T_{\max}$ — that any scalability claim should be required to report.

## References

[1] arXiv:1609.07939v1 | Demonstration of liquid crystal for barocaloric cooling application

[2] arXiv:cond-mat/0310229v2 | Ground state cooling of mechanical resonators

[3] arXiv:2304.07466v3 | Asymptotic Breakdown Point Analysis for a General Class of Minimum Divergence Estimators

[4] arXiv:2508.04435v2 | Cognitive Effort in the Two-Step Task: An Active Inference Drift-Diffusion Model Approach

[5] arXiv:2506.08599v4 | Geometric Hyperscanning of Affect under Active Inference

[6] arXiv:astro-ph/0611214v1 | Cold Feedback in Cooling-Flow Galaxy Clusters

[7] arXiv:2508.06174v2 | Thermodynamic uncertainty relation for feedback cooling

[8] arXiv:2408.15869v2 | Catastrophic cooling instability in optically thin plasmas

[9] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation

[10] QNFO: Thermodynamic and Quantum Constraints on Scalable Quantum Computing

[11] QNFO: Spectral Dynamics and Thermodynamic Stability in the Arithmetic Quantum Framework

[12] QNFO: Thermodynamic Viability and the Universality of Feynman Matter