# Passive Control as Signal: A Systems-Theoretic Framing of the Signal-Worker Ontology

## Abstract

The QNFO corpus proposes a decomposition of wave-particle duality in which the boson is a "signal" (a delocalized field instruction) and the fermion is a "worker" (the localized state that performs work) [10]. This paper asks a control-theoretic question about that framing: under what conditions can a signal-carrying channel be engineered to function as a passive control system, so that the signal-worker boundary is stabilized without an active power source at the interface? We assemble the question from the passivity and data-driven control literature: passive iFIR controllers enforce passivity by construction in a model-free design [1]; passivity-based PI control survives communication delays when the channel is treated as a transport PDE [2]; sampled-data feedback with quantized actuators yields uniform global asymptotic stability of an attractor around the origin [3]; and classical linear controllers provably cannot generate steady-state entanglement in Gaussian quantum systems [5], bounding what a purely classical signal layer can achieve at a quantum interface. We then carry out an explicit energy-balance analysis for an idealized signal-worker interface, deriving the storage-function inequality that a passive signal layer must satisfy, and computing a numerical example with all arithmetic shown. We find that the passive-signal framing is internally consistent as a control abstraction, but that its quantum interpretation is bounded by no-go results of the type in [5]. The contribution is a disciplined, falsifiable restatement of the Signal-Worker ontology as a passivity claim.

## 1. Introduction

The research idea under revision is a re-entry of a QNFO corpus document (DOI 10.5281/zenodo.18515457) "engineered to function as a passive control system ('Signal')." The corpus context supplies two antecedent documents: one on structural versus driven quantum coherence (DOI 10.5281/zenodo.18441401), whose supplied summary is empty and which we therefore use only as a title-level pointer [9], and the Signal-Worker Boundary Confinement paper, which states the core ontology: the boson is the *signal*, "the delocalized field instruction," and the fermion is the *worker*, "the localized state that performs work," presented as a red-team-hardened correction of what the corpus calls the wave-particle duality fog [10].

The present paper takes that ontology seriously as an engineering specification rather than as a metaphor. If the bosonic channel is a "signal" in the sense of a delocalized instruction, then the natural formal home for the claim is control theory, and specifically passivity theory: a passive system is one that cannot deliver more energy than has been supplied to it, so a "passive signal" is a channel whose instruction-carrying role is achieved without injecting net energy into the worker subsystem. This reframing has three advantages. First, it converts an ontological assertion into a set of checkable inequalities. Second, it connects the corpus to a mature literature in which passivity is enforced by design rather than assumed: passive iFIR controllers are designed model-free with passivity enforced through constraints [1], and passivity of a loop containing a delayed communication channel can be guaranteed by treating the channel as a transport PDE [2]. Third, it exposes the limits of the framing: where the worker is a quantum system, classical linear signal layers cannot generate steady-state entanglement in Gaussian systems initialized in Gaussian states [5], so any claim that a passive classical signal can do quantum work at the interface must fail.

Our questions are: (Q1) What is the minimal formal statement of "the Signal functions as a passive control system"? (Q2) What storage-function inequality must the signal-worker interface satisfy, and what does a worked numerical example look like with fully shown arithmetic? (Q3) Which parts of the ontology survive the passivity restatement, and which are falsified or left unsupported?

The paper is organized as follows. Section 2 reviews the eight arXiv works in the supplied bibliography plus the two QNFO entries. Section 3 sets up the formal model. Section 4 performs the derivations, including a complete numerical example. Section 5 reports only what was computed. Section 6 discusses limitations and failure modes, and Section 7 concludes.

## 2. Background and Related Work

**Passive data-driven controllers.** Reference [1] introduces passive iFIR controllers, formed by the parallel action of an integrator and a finite impulse response filter; the supplied summary states that iFIRs are more expressive than PID controllers while retaining their features and simplicity, that the design is model-free and data-driven via virtual reference feedback tuning, and that passivity is enforced through constraints (the summary text is truncated mid-sentence at "constra", so the precise constraint mechanism is not further specified in the supplied material). This is the closest existing template for our question: it shows how "passive" can be a design constraint on a signal-shaping element rather than a property discovered after the fact. We adopt the same posture: the Signal is passive by construction, not by assumption.

**Passivity across delayed channels.** Reference [2] revisits PI control of first-order linear passive systems through a delayed communication channel, using the relative stability concept called sigma-stability. The channel is treated as a transport PDE, the passivity of the overall control loop is guaranteed, and the resulting closed-loop system is of neutral type; spectral methods are then applied (the summary truncates at "obt", so the spectral results themselves are not further specified here). This matters for the Signal-Worker framing because the "delocalized field instruction" is naturally modeled as a transport delay: an instruction propagating through a field is exactly a transport-PDE channel. Reference [2] supplies the precedent that such a channel can be embedded in a passive loop without destroying passivity.

**Quantization and hybrid closure.** Reference [3] designs sampled-data state feedback for continuous-time linear systems with uniform input quantization, ensuring uniform global asymptotic stability (UGAS) of an attractor surrounding the origin, and rewrites the closed loop as a hybrid dynamical system using an auxiliary construction (the summary truncates at "auxilia"). For us this is the discrete-signal analogue: a signal that reaches the worker only in sampled, quantized packets is a legitimate control channel, provided the analysis is closed in the hybrid formalism. The "attractor surrounding the origin" language is also useful: it suggests that a passive Signal need not drive the worker to an exact state, only to a guaranteed neighborhood.

**Quantum control and bilinear systems.** Reference [4] is a tutorial invitation to quantum computing and its relation to bilinear control systems; the supplied summary motivates quantum devices as an active field of research (the text truncates at "re", giving no further methodological detail). We use [4] only to justify treating the quantum worker as a bilinear control object, i.e., one in which the control enters multiplicatively, which is the standard reading the summary supports by its title and framing. Reference [8] explores the use of quantum computers for problems in systems and control theory, noting that quantum algorithms have been developed for binary optimization, which the summary says plays an important role in various control- (again truncated). We cite [8] for the reverse direction of the interface: control theory consuming quantum computation, symmetric to our Signal consuming a quantum worker.

**No-go results for classical control of quantum systems.** Reference [5] uses a system-theoretic approach to show two results, both stated in the supplied summary: classical linear time-invariant controllers cannot generate steady-state entanglement in a bipartite Gaussian quantum system initialized in a Gaussian state, and classical linear controllers cannot generate entanglement in finite time from a bipartite system initialized in a separable Gaussian state. This is the sharpest constraint on the Signal-Worker ontology in its quantum regime: if the Signal layer is classical and linear, and the worker pair is Gaussian and initialized in a Gaussian (or separable Gaussian) state, then the Signal cannot be the source of entanglement-based "work." Any quantum reading of the ontology must therefore either allow a nonclassical or nonlinear signal layer, or locate the work elsewhere.

**Safety under parametric uncertainty.** Reference [6] addresses control barrier functions, which guarantee safety but require accurate system models; parametric uncertainty invalidates these guarantees. Existing robust methods maintain safety via worst-case bounds at the cost of performance, while modular learning schemes decouple estimation from safety and risk constraint violations during transients; the paper presents composite adaptive control barrier functions (the summary truncates at "functi"). This is relevant because the Signal-Worker boundary is, in our framing, a safety constraint on the interface: the Signal must not push the worker out of its admissible set. Reference [6] supplies the modern vocabulary for keeping such guarantees alive under uncertainty.

**Robust synthesis.** Reference [7] treats finite-horizon constrained robust optimal control for nonlinear systems with norm-bounded disturbances, decomposing the uncertain nonlinear system via a first-order Taylor expansion into a nominal system and an error described as an uncertain linear time-varying system, which allows leveraging (the summary truncates at "lever"). We use [7] as the template for handling the gap between the idealized passive Signal and the real corpus document: the ontology is the nominal system; the deviation is the uncertain LTV error, and robustness must be argued for the pair.

**The QNFO corpus entries.** Reference [10] supplies the Signal-Worker ontology itself, with the boson-as-signal and fermion-as-worker decomposition and the claim of a red-team-hardened correction; beyond the quoted characterization, the supplied summary gives no equations, so we treat [10] as a source of the conceptual specification only. Reference [9], "Structural vs Driven Quantum Coherence" (DOI 10.5281/zenodo.18441401), has an empty supplied summary; we therefore make no claim about its content and use it solely as evidence that the corpus contains a structural/driven coherence distinction that our passivity framing may later formalize. The re-entry document itself (DOI 10.5281/zenodo.18515457) is named in the grounding input but not summarized; we accordingly do not attribute any content to it beyond its stated role as the object "engineered to function as a passive control system."

## 3. Methods

### 3.1 Formal model

We model the Signal-Worker interface as a feedback interconnection of two passive blocks. The Signal block $S$ has input $u_S$ (the supplied instruction energy) and output $y_S$; the Worker block $W$ has input $u_W = y_S$ and output $y_W$, with $u_S = -y_W$ closing the loop (negative feedback). Passivity of each block means there exist storage functions $V_S \geq 0$ and $V_W \geq 0$ with

$$
\dot{V}_S \leq u_S^{\top} y_S - \epsilon_S \|u_S\|^2, \qquad
\dot{V}_W \leq u_W^{\top} y_W - \epsilon_W \|u_W\|^2,
$$

where $\epsilon_S, \epsilon_W \geq 0$ are input feedthrough passivity margins (strictly positive for input-strict passivity). The defining claim "the Signal functions as a passive control system" is then:

$$
\text{(P-Signal)} \quad \exists\, V_S \geq 0,\ \epsilon_S > 0 \ \text{such that} \ \dot{V}_S \leq u_S^{\top} y_S - \epsilon_S \|u_S\|^2 \ \text{for all admissible } u_S.
$$

### 3.2 Loop passivity with a delocalized channel

Following the transport-PDE treatment of delayed channels in [2], we insert a pure transport delay $T_d$ in the loop: $u_W(t) = y_S(t - T_d)$. The delayed channel itself is a lossless transport element, so it preserves the passivity supply rate; the loop storage function is $V = V_S + V_W$, and

$$
\dot{V} \leq u_S^{\top} y_S + u_W^{\top} y_W - \epsilon_S \|u_S\|^2 - \epsilon_W \|u_W\|^2.
$$

Under negative feedback $u_S = -y_W$ and $u_W = y_S(t-T_d)$, the instantaneous cross terms cancel only in the zero-delay case; for $T_d > 0$ the loop is passive in the sense of [2] provided the product of passivity margins dominates the delay-induced phase loss. We do not prove a new theorem here; we use the structure of [2] as the assumed guarantee and quantify the margin condition numerically in Section 4.

### 3.3 Quantized, sampled signal delivery

Following [3], the Signal delivers instructions in sampled, uniformly quantized packets. The worker's guaranteed behavior is then UGAS of an attractor $\mathcal{A}$ surrounding the origin rather than asymptotic stability of the origin itself. We adopt this as the correctness notion for the Worker under a passive Signal: convergence to a neighborhood, not to a point.

### 3.4 Safety and robustness wrappers

The admissible set of the Worker is enforced by a barrier-style condition in the spirit of [6], with the caveat that parametric uncertainty in the Worker model degrades the guarantee to a worst-case bound at performance cost, per the trade-off [6] describes. The gap between the idealized passive Signal and the corpus document is handled as a nominal-plus-error decomposition in the spirit of [7]: nominal passive dynamics plus an uncertain LTV deviation with norm-bounded disturbance.

### 3.5 Quantum worker bound

Where the Worker is a bipartite Gaussian quantum system, we impose the constraint of [5]: a classical LTI Signal layer cannot generate steady-state entanglement from a Gaussian initial state, nor finite-time entanglement from a separable Gaussian initial state. This is used as a hard admissibility condition on any quantum interpretation of the ontology.

## 4. Analysis

All numerical inputs in this section are *illustrative parameters chosen for the worked example*, stated explicitly; every derived number follows from them by shown arithmetic. No number below is an empirical measurement.

### 4.1 Input list

- $k_S = 2.0$: static gain of the Signal's dissipative path (dimensionless), chosen.
- $\epsilon_S = 0.1$: Signal passivity margin (dimensionless), chosen.
- $\epsilon_W = 0.2$: Worker passivity margin (dimensionless), chosen.
- $T_d = 0.5\ \mathrm{s}$: transport delay of the delocalized channel, chosen.
- $\omega_c = 1.0\ \mathrm{rad\,s^{-1}}$: loop crossover frequency at which the delay phase loss is evaluated, chosen.
- $\Delta = 0.05$: uniform quantization step of the Signal's delivered instruction, chosen.
- $u_{\max} = 1.0$: norm bound on the instruction magnitude, chosen.

### 4.2 Derivation 1: the passivity margin condition at the crossover frequency

A pure delay $T_d$ contributes phase lag $\phi_d(\omega) = \omega T_d$ (in radians) at frequency $\omega$. At $\omega = \omega_c$:

$$
\phi_d(\omega_c) = \omega_c T_d = (1.0\ \mathrm{rad\,s^{-1}})(0.5\ \mathrm{s}) = 0.5\ \mathrm{rad}.
$$

Converting to degrees: $\phi_d = 0.5 \times \frac{180}{\pi} \approx 0.5 \times 57.29578 \approx 28.65^{\circ}$.

The passivity-based loop of Section 3.2 tolerates this lag if the combined dissipative margin exceeds the delay-induced loss. We take the combined margin proxy as the sum of the input-strictness margins scaled by the loop gain $k_S$:

$$
M = k_S(\epsilon_S + \epsilon_W) = 2.0 \times (0.1 + 0.2) = 2.0 \times 0.3 = 0.6.
$$

The delay phase loss in normalized form is $\ell_d = \phi_d(\omega_c)/(2\pi) = 0.5/(2\pi) \approx 0.0796$. The normalized margin is $M_n = M/(1+M) = 0.6/1.6 = 0.375$. Since $M_n = 0.375 > \ell_d \approx 0.0796$, the illustrative margin condition is satisfied with ratio

$$
\rho = \frac{M_n}{\ell_d} = \frac{0.375}{0.0796} \approx 4.71.
$$

Interpretation: under these chosen parameters, the passive Signal retains roughly $4.7$ times more normalized dissipative margin than the delay consumes at crossover, consistent with the loop-passivity guarantee pattern of [2].

### 4.3 Derivation 2: worst-case energy delivered per quantized instruction

Each delivered instruction packet carries energy bounded by the passivity supply rate. With input norm bounded by $u_{\max}$ and quantization step $\Delta$, the quantization error is at most $\Delta/2$ in each delivered sample (uniform quantizer, midpoint rounding). The worst-case excess energy per packet attributable to quantization is bounded by the passivity supply evaluated at the error:

$$
E_q \leq \left(\frac{\Delta}{2}\right) u_{\max} = \left(\frac{0.05}{2}\right)(1.0) = 0.025\ \mathrm{J}.
$$

The nominal per-packet supply at full magnitude is $E_0 = u_{\max}^2 = (1.0)^2 = 1.0\ \mathrm{J}$ (taking the supply rate $u^{\top}y$ with $y = u$ at unit feedthrough as the conservative bound). The relative quantization overhead is therefore

$$
\frac{E_q}{E_0} = \frac{0.025}{1.0} = 0.025 = 2.5\%.
$$

Interpretation: the quantized, sampled delivery mode of [3] costs at most $2.5\%$ extra supply energy per packet under these parameters, which is the quantitative price of the Signal's discreteness.

### 4.4 Derivation 3: attractor radius for the Worker under quantized delivery

If the Worker's closed-loop contraction rate toward the attractor is at least $\lambda$ per unit input error, and the input error is bounded by $\Delta/2$, the guaranteed attractor radius scales linearly. Taking the illustrative contraction constant $\lambda_W = 0.5\ \mathrm{s^{-1}}$ (chosen), the radius contribution from quantization is

$$
r_q = \frac{\Delta/2}{\lambda_W} = \frac{0.025}{0.5} = 0.05.
$$

So the Worker is guaranteed convergence to an attractor of radius at least $r_q = 0.05$ (in the Worker's normalized state units) attributable to quantization alone, in the UGAS-of-attractor sense of [3]. This is a structural statement: no passive quantized Signal can promise better than $r_q > 0$ from quantization alone.

### 4.5 Derivation 4: quantum-regime admissibility check

The constraint of [5] is binary, not numerical: for a classical LTI Signal layer and a bipartite Gaussian Worker initialized in a Gaussian state, steady-state entanglement generation is infeasible, and finite-time entanglement generation from a separable Gaussian initial state is infeasible. We therefore evaluate the ontology's quantum reading as a feasibility table rather than a number:

- Signal classical LTI, Worker Gaussian/Gaussian-initialized: steady-state entanglement generation infeasible [5] — the quantum reading of "Signal performs work via entanglement" is falsified in this regime.
- Signal classical LTI, Worker separable-Gaussian-initialized: finite-time entanglement generation infeasible [5] — same conclusion for the transient reading.
- Signal nonclassical or nonlinear: outside the scope of [5]'s results; no conclusion is drawn here.

### 4.6 Derivation 5: robustness budget for the nominal-error decomposition

Following the nominal-plus-error structure of [7], let the uncertain LTV deviation have norm bound $\delta$ on the Signal's passivity margin: $\epsilon_S^{\text{actual}} = \epsilon_S - \delta$. Passivity of the Signal block is retained iff $\delta < \epsilon_S$. With $\epsilon_S = 0.1$, the maximum tolerable relative margin erosion is

$$
\frac{\delta}{\epsilon_S} < 1 \quad \Rightarrow \quad \delta < 0.1.
$$

As a fraction of the combined margin $M = 0.6$ from Section 4.2, this is $\delta/M = 0.1/0.6 \approx 0.1667$, i.e., the Signal can tolerate erosion of up to about $16.7\%$ of the combined loop margin before its own passivity, and hence the (P-Signal) property, fails.

## 5. Results

All results below are the direct outputs of Section 4's derivations from the stated illustrative inputs; none are empirical.

- **R1 (loop margin).** With $k_S = 2.0$, $\epsilon_S = 0.1$, $\epsilon_W = 0.2$, $T_d = 0.5\ \mathrm{s}$, $\omega_c = 1.0\ \mathrm{rad\,s^{-1}}$: the delay phase lag at crossover is $\phi_d = 0.5\ \mathrm{rad} \approx 28.65^{\circ}$; the normalized dissipative margin is $M_n = 0.375$ against a normalized delay loss $\ell_d \approx 0.0796$; the safety ratio is $\rho \approx 4.71$.
- **R2 (quantization energy cost).** With $\Delta = 0.05$ and $u_{\max} = 1.0$: worst-case quantization energy per packet $E_q = 0.025\ \mathrm{J}$, i.e., $2.5\%$ of the nominal per-packet supply $E_0 = 1.0\ \mathrm{J}$.
- **R3 (attractor radius).** With $\lambda_W = 0.5\ \mathrm{s^{-1}}$: quantization-induced attractor radius $r_q = 0.05$ in normalized Worker units; a passive quantized Signal cannot guarantee convergence to a point.
- **R4 (quantum admissibility).** Under a classical LTI Signal layer, both steady-state and finite-time entanglement generation at a Gaussian Worker interface are infeasible per [5]; the quantum reading of the Signal-as-worker is falsified in that regime, and no claim is made for nonclassical Signal layers.
- **R5 (robustness budget).** The Signal's passivity survives margin erosion up to $\delta < 0.1$, i.e., about $16.7\%$ of the combined loop margin $M = 0.6$.

**Projection (labeled as such).** If a future revision of the re-entry document (DOI 10.5281/zenodo.18515457) specifies its own parameters $(k_S, \epsilon_S, \epsilon_W, T_d, \omega_c, \Delta)$, the formulas of Sections 4.2–4.3 and 4.6 apply unchanged; the results R1, R2, R5 scale as shown and no new derivation is needed. We project that the qualitative conclusions (positive margin ratio, percent-level quantization cost, nonzero attractor radius, classical-LTI quantum infeasibility) are robust to any parameter choice satisfying $\epsilon_S, \epsilon_W > 0$ and $M_n > \ell_d$; the quantitative values, however, are example-specific and carry no uncertainty bound beyond the exact arithmetic shown, since they are definitions of the chosen example rather than measurements.

## 6. Discussion

**What the framing buys.** Restating "the Signal" as a passive control element converts the corpus's ontological claim into inequality (P-Signal), which is checkable, and connects it to design templates where passivity is enforced by construction [1], preserved across delocalized transport channels [2], and compatible with quantized sampled delivery [3]. The worked example shows the framing is not vacuous: it produces concrete, arithmetic-checkable quantities (R1–R3, R5).

**Limitations and failure modes.** First, every number in Section 4 derives from illustrative parameters we chose; the paper establishes the *form* of the passivity claim, not its realization in any physical or corpus-internal system. Second, the loop-passivity argument for $T_d > 0$ leans on the guarantee pattern of [2] rather than a new proof; a neutral-type closed loop can lose stability in ways a finite-dimensional passive loop does not, and our margin proxy $M_n$ is a heuristic, not a sigma-stability certificate. Third, the attractor-radius result R3 assumes a linear contraction constant $\lambda_W$; for nonlinear Workers the radius bound does not transfer. Fourth, the barrier-style safety wrapper inherits exactly the fragility [6] identifies: parametric uncertainty invalidates the guarantees, and the robust fallback trades performance for safety. Fifth, the nominal-error decomposition of [7] presumes norm-bounded disturbances; heavy-tailed or structural model error escapes the budget R5.

**What would falsify the claims.** The central claim of this paper — that the Signal-Worker ontology is consistently expressible as a passivity property — would be falsified by a demonstration that no storage function $V_S$ satisfying (P-Signal) exists for the corpus's intended Signal dynamics, e.g., if the Signal's defining behavior requires active energy injection at the interface ($\epsilon_S < 0$ necessarily). The quantum reading is already bounded: [5]'s results would be contradicted only if a classical LTI Signal were shown to generate steady-state entanglement in a Gaussian-initialized bipartite Gaussian system, which would overturn [5], not merely our application of it.

**Arguing against ourselves.** A critic may say the passivity restatement is a category error: [10] proposes an ontology of wave-particle duality, not a control loop, and mapping "signal" onto a control input may discard precisely the content the corpus intends. We concede the risk. The supplied summary of [10] contains no equations, and [9]'s summary is empty, so the corpus's own formal content is unavailable to us; our formalization is an external discipline imposed on the ontology, not an exegesis of it. A second objection: the quantum no-go of [5] applies to classical LTI controllers and Gaussian systems, so the ontology's advocates could simply declare the Signal nonclassical — but then the burden shifts to specifying the nonclassical signal dynamics, which neither [10] nor the grounding input supplies. A third objection: the re-entry document (DOI 10.5281/zenodo.18515457) is named but not characterized in the input beyond its intended function; our analysis may not touch its actual content at all. This is a genuine limitation and the reason Section 5's projections are labeled as projections.

**Open questions.** (i) Does a strict input-strict passivity proof exist for a transport-delay Signal channel with finite sampling rate, combining [2] and [3] in one hybrid formalism? (ii) Can the composite adaptive barrier machinery of [6] be instantiated for the Signal-Worker boundary with learned Worker models? (iii) Does the bilinear structure highlighted in [4] offer a middle regime — neither classical LTI nor fully quantum — where the Signal can do bounded quantum work without violating [5]? (iv) What does the corpus's structural-versus-driven coherence distinction [9] correspond to in storage-function terms?

## 7. Conclusion

We have recast the QNFO corpus's Signal-Worker ontology — boson as delocalized field instruction, fermion as localized worker [10] — as a passivity claim on a feedback interconnection, drawing on passive data-driven controller design [1], passivity across transport-delay channels [2], quantized sampled-data stability [3], quantum-control tutorials and quantum-computing-for-control perspectives [4], [8], classical-control no-go results for Gaussian entanglement [5], adaptive safety under uncertainty [6], and robust synthesis under norm-bounded disturbances [7]. The worked analysis shows the framing yields concrete, checkable quantities: a margin ratio $\rho \approx 4.71$, a quantization energy overhead of $2.5\%$, an unavoidable attractor radius $r_q = 0.05$, and a robustness budget of $16.7\%$ margin erosion, all from stated illustrative parameters with full arithmetic. The quantum reading of the ontology is bounded by the infeasibility results of [5]. The contribution is methodological: the ontology becomes falsifiable once stated as (P-Signal), and the path to its verification runs through specifying the Signal's actual dynamics — a task this paper defines but, on the supplied evidence, cannot complete.

## References

[1] arXiv:2403.06640v2 | Passive iFIR Filters for Data-Driven Control
[2] arXiv:1507.01146v1 | Passivity-based PI control of first-order systems with I/O communication delays: A complete sigma-stability analysis
[3] arXiv:2208.05694v3 | Sampled-data control design for systems with quantized actuators
[4] arXiv:2412.00736v1 | Bringing Quantum Systems under Control: A Tutorial Invitation to Quantum Computing and Its Relation to Bilinear Control Systems
[5] arXiv:1107.3174v1 | On the infeasibility of entanglement generation in Gaussian quantum systems via classical control
[6] arXiv:2601.17683v3 | Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty
[7] arXiv:2301.04943v3 | Robust Nonlinear Optimal Control via System Level Synthesis
[8] arXiv:2403.17711v1 | Using quantum computers in control: interval matrix properties
[9] QNFO: Structural vs Driven Quantum Coherence | DOI 10.5281/zenodo.18441401
[10] QNFO: Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport | DOI 10.5281/zenodo.21974194