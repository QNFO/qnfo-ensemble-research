# In‑Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis

## Abstract

Sixth‑generation (6G) network research seeks to embed semi‑classical quantum‑control functionality within the communication fabric, yet designers lack a quantitative budgeting framework that determines whether a Hamiltonian‑engineering service can operate inside quantum‑coherence windows and how much of its control stack survives infrastructure upgrades. This work defines a Hamiltonian Engineering Service (HES) contract, derives a timing and fidelity budget for a node with coherence time $T_{2}=1\,\mathrm{ms}$, engineering‑cycle duration $T_{c}=8\,\mu\mathrm{s}$, and per‑cycle error budget $\epsilon_{c}=10^{-5}$, and computes $N_{c}=125$ cycles per coherence window, accumulated first‑order error $1.25\times10^{-3}$, and a projected end‑of‑window fidelity $F_{\mathrm{proj}}^{(1)}=0.99875$. Adding a second‑order commutator contribution $\epsilon_{2}=9.81\times10^{-5}$ tightens the fidelity projection to $F_{\mathrm{proj}}^{(2)}=0.9986519$. The corrected validity condition $\epsilon_{c}\le0.01\,T_{c}/T_{2}=8\times10^{-5}$ replaces a prior $10^{-4}$ claim. A closed‑loop latency of $1.8\times10^{-4}\,\mathrm{s}$ consumes $\eta=0.18$ of the coherence window, yielding a minimum coherence $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$; for the $10$–$100\,\mu\mathrm{s}$ windows reported in current solid‑state hardware the loop budget fails, leaving only feed‑forward operation viable. A re‑entry reuse ratio $\rho=0.5$ (bounds $0.5$–$0.583$) and a projected re‑qualification effort of $24$ person‑weeks (range $12$–$48$) are derived. All numbers follow analytically from explicitly labeled assumptions; no empirical measurement is claimed. The framework supplies 6G architects a budgeting structure in which cycle time, per‑cycle error, coherence‑window sizing, and actuation rate are co‑managed, and identifies timing distribution—not bandwidth—as the binding engineering constraint.

## 1. Introduction

Telecommunication operators and quantum‑network system engineers must decide whether to embed quantum‑control functionality inside the 6G network fabric or to keep it confined to laboratory‑grade hardware. The decision is forced by a concrete physical conflict: the coherence windows of quantum endpoints (typically $10$–$100\,\mu\mathrm{s}$ in current solid‑state devices) and the timing behavior of packet networks (jitter of $100$–$500\,\mu\mathrm{s}$) differ by orders of magnitude. Embedding control promises tighter integration with quantum‑secure services but raises two engineering questions: (i) can a control cycle executed through network elements close within a quantum coherence window, and at what fidelity and actuation cost? (ii) when the underlying 6G infrastructure is upgraded, can the control stack be re‑entered—carried across generations—without a full redesign? A wrong answer either strands capital in control hardware that cannot meet quantum timing, or forces every quantum service to remain a bespoke laboratory installation. If the quantitative budgets derived here hold, network designers can provision microsecond‑scale timing, per‑endpoint actuation rates of $2\times10^{6}\,\mathrm{s^{-1}}$, and a modest re‑qualification effort, thereby enabling a viable path to in‑network quantum control; if they fail, the control function must remain hardware‑adjacent and the network reverts to transport‑only.

The contributions of this work are:
1. A corrected and generalized validity condition $\epsilon_{c}\le0.01\,T_{c}/T_{2}$, giving $8\times10^{-5}$ at the nominal cycle parameters and replacing the predecessor’s $10^{-4}$ claim (Section 4, Derivations 8 and 8b).  
2. A service model and quantitative timing/fidelity budget for the Hamiltonian Engineering Service, including a second‑order commutator correction and an uncertainty propagation, yielding $F_{\mathrm{proj}}^{(2)}=0.9986519$ at nominal parameters (Sections 3.1–3.2; computed in Section 4, Derivations 1–5, 14–15).  
3. A closed‑loop latency, jitter, and re‑entry analysis, including a twelve‑component inventory giving $\rho=0.5$ (bounds $0.5$–$0.583$), a projected re‑qualification effort of $24$ person‑weeks (range $12$–$48$), a minimum‑coherence condition $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$, and a jitter budget $J\le0.2\,T_{c}=1.6\,\mu\mathrm{s}$ that current packet networks violate (Sections 3.3 and 4, Derivations 7, 9–13, 16–17, 19).  
4. A discussion of model limitations, falsification conditions, and open research questions (Section 6).

## 2. Background and Related Work

**Semi‑classical quantum control.** Reference [1] describes strategies that use a semi‑classical controller together with classical sensors and actuators to engineer quantum Hamiltonians, directly motivating the HES contract that couples classical network logic to quantum devices.

**Higher‑order pulse‑sequence design.** Reference [5] introduces a framework that systematically accounts for higher‑order contributions to the Floquet–Magnus expansion, and shows that sequence‑structure can suppress first‑order cross terms while providing explicit second‑order commutator estimates. This work adopts that framework to introduce the second‑order error term $\epsilon_{2}$ (Derivation 14).

**Temporal mismatch in 6G‑DQC.** Current solid‑state devices exhibit transverse coherence times $T_{2}^{*}=10$–$100\,\mu\mathrm{s}$ and network jitter of $100$–$500\,\mu\mathrm{s}$ [8], highlighting the need for timing‑aware quantum control in 6G networks.

**Original service‑model paper.** The predecessor service‑model paper [9] presented a validity condition $\epsilon_{c}\le10^{-4}$, which this work re‑derives and corrects to $\epsilon_{c}\le0.01\,T_{c}/T_{2}$.

**Systematic engineering of web‑based services.** Web Engineering is defined as the application of systematic, disciplined, and quantifiable approaches to the development, operation, and maintenance of web‑based applications [3], providing a methodological parallel for the rigor required in the HES service model.

**Cognitive biases in software projects.** Reference [4] maps literature on cognitive biases that affect software‑engineering projects, highlighting systematic human errors that can lead to template‑mismatch failure modes discussed in Section 6.

**Generative‑AI‑driven software engineering.** Reference [2] surveys how generative AI tools can automatically check, synthesize, and modify software artifacts, informing the view of the HES library $\mathcal{L}$ as an automatically generated, version‑controlled repository.

**Benchmarking infrastructure.** A comprehensive benchmarking infrastructure that quantifies uncertainty in derived metrics is described in [6]; the $5\%$ relative uncertainty on $\epsilon_{c}$ is introduced as an assumption (A18).

**AI‑driven software engineering outlook.** Challenges in integrating AI tools into development pipelines are discussed in [7], informing the perspective on automated template generation, verification, and maintenance for the HES library.

**Stability and persistence across environments.** The topological extension framework introduces persistence—defined as the ability of a mode to maintain coherence against environmental dispersive forces—as a notion of stability [10]. This framing is used in Section 6 to interpret the re‑entry analysis: the HES stack persists across infrastructure generations exactly to the degree that its components decouple from generation‑specific environmental parameters.

## 3. Methods

### 3.1 Service model

We define a network service, the Hamiltonian Engineering Service (HES), with the following contract. A quantum endpoint $E_{q}$ (a memory, transducer, or QKD node) exposes: (i) its natural Hamiltonian parameters $H_{0}(\theta)$, where $\theta$ is a vector of slowly drifting device parameters; (ii) a coherence time $T_{2}$; and (iii) a pulse‑actuation interface accepting control waveforms with minimum pulse width $\tau_{p}$. An in‑network controller $C_{n}$ (hosted on an edge node or smart network interface card) exposes: (i) a sequence‑template library $\mathcal{L}$, each template $L_{k}$ being a compiled decoupling or recoupling sequence of the kind systematized in [5]; (ii) a scheduler that aligns cycle boundaries with network timing signals; and (iii) a verification module that checks the template’s applicability conditions against the reported $\theta$, with the conditions expressed as machine‑checkable algebraic predicates in the spirit of the decoupling‑rule tables of [5] and the bias‑resistant design stance of [4].

The service‑level objective is an effective‑Hamiltonian error tolerance:
$$
\bigl\|\bar{H} - H_{\mathrm{eff}}\bigr\| \le \epsilon_{c}\,\|H_{0}\|,
$$
where $\bar{H}$ is the cycle‑averaged Hamiltonian and $\epsilon_{c}$ is the per‑cycle relative error budget. This contract follows the semi‑classical control model of [1].

### 3.2 Timing and fidelity model

Each cycle consists of $n_{p}$ pulses of width $\tau_{p}$ separated by idle intervals, so
$$
T_{c}=n_{p}(\tau_{p}+\tau_{i}),\qquad
f=\frac{n_{p}\tau_{p}}{T_{c}}=\frac{\tau_{p}}{\tau_{p}+\tau_{i}},
$$
with $f$ the actuation duty factor. The controller must issue actuation updates at rate $R_{u}=1/\tau_{p}$ per endpoint; a node hosting $K$ endpoints presents an aggregate update rate $K\,R_{u}$.

We adopt a first‑order accumulation model in which per‑cycle fractional error contributions add linearly over $N_{c}$ cycles within one coherence window:
$$
N_{c}=\Bigl\lfloor\frac{T_{2}}{T_{c}}\Bigr\rfloor,\qquad
\epsilon_{\mathrm{tot}}^{(1)}=N_{c}\,\epsilon_{c},\qquad
F_{\mathrm{proj}}^{(1)}\approx1-\epsilon_{\mathrm{tot}}^{(1)}.
$$
A second‑order commutator contribution $\epsilon_{2}$ is introduced as a projection (Assumption A17) based on the Floquet–Magnus analysis of [5]. The total projected error is then
$$
\epsilon_{\mathrm{tot}}^{(2)}=\epsilon_{\mathrm{tot}}^{(1)}+\epsilon_{2},\qquad
F_{\mathrm{proj}}^{(2)}\approx1-\epsilon_{\mathrm{tot}}^{(2)}.
$$
Uncertainty on $\epsilon_{c}$ is modeled as a $5\%$ relative standard deviation (Assumption A18), yielding an uncertainty band on $\epsilon_{\mathrm{tot}}^{(1)}$ and $F_{\mathrm{proj}}^{(1)}$ (Derivation 15).

### 3.3 Closed‑loop latency, jitter, and re‑entry models

We model one in‑network feedback cycle as four sequential stages:
$$
T_{\mathrm{loop}}=T_{s}+T_{p}+T_{c}^{\prime}+T_{a},
$$
where $T_{s}$ is the sensing/measurement interval, $T_{p}$ the packet‑transport latency, $T_{c}^{\prime}$ the compute time for the control update, and $T_{a}$ the actuation setup time. Re‑entry is physically meaningful only if the loop closes within the coherence window:
$$
\frac{T_{\mathrm{loop}}}{T_{2}}\le\eta_{\mathrm{max}},
$$
with $\eta_{\mathrm{max}}=0.2$ a design margin. Cycle alignment additionally requires timing jitter $J$ to remain a bounded fraction of the cycle period; we require $J\le0.2\,T_{c}$ (Derivation 19), so that no more than one fifth of a cycle period is consumed by stochastic arrival spread.

For re‑entry, let the HES stack consist of $N_{\mathrm{tot}}$ components partitioned into a physics‑facing layer $\mathcal{P}$ and an infrastructure‑facing layer $\mathcal{I}$. The re‑entry reuse ratio is
$$
\rho=\frac{N_{\mathrm{reuse}}}{N_{\mathrm{tot}}},\qquad
N_{\mathrm{reuse}}=|\mathcal{P}_{\mathrm{portable}}|+|\mathcal{I}_{\mathrm{portable}}|,
$$
where a component is portable if its specification does not reference generation‑specific infrastructure parameters. The inventory is enumerated explicitly in Section 4 so that $\rho$ is auditable. Re‑qualification effort is modeled as linear in the number of non‑portable components:
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}}),
$$
with $e$ a per‑component effort assumption (Assumption A16).

### 3.4 Method status

The method of this paper is analytical derivation from labeled assumptions, together with a correction audit of the predecessor’s derivations [9] against the model and against the hardware parameters reported in [8]. No hardware experiment, simulation, survey, or expert review was performed; a study that would test the results is proposed in Section 7.

## 4. Analysis

All inputs are design assumptions (A1–A19) unless otherwise noted.

**Inputs (timing/fidelity model).**  
- $T_{2}=1\,\mathrm{ms}=10^{-3}\,\mathrm{s}$ (A1).  
- $\tau_{p}=0.5\,\mu\mathrm{s}=5\times10^{-7}\,\mathrm{s}$ (A2).  
- $\tau_{i}=0.5\,\mu\mathrm{s}=5\times10^{-7}\,\mathrm{s}$ (A3).  
- $n_{p}=8$ (A4).  
- $\epsilon_{c}=10^{-5}$ (A5).  
- $K=64$ endpoints per node (A6).  

**Derivation 1 — cycle time.**  
$$
T_{c}=n_{p}(\tau_{p}+\tau_{i})
=8\times(5\times10^{-7}+5\times10^{-7})\,\mathrm{s}
=8\times10^{-6}\,\mathrm{s}=8\,\mu\mathrm{s}.
$$

**Derivation 2 — duty factor.**  
$$
f=\frac{\tau_{p}}{\tau_{p}+\tau_{i}}
=\frac{5\times10^{-7}}{10^{-6}}=0.5.
$$

**Derivation 3 — cycles per coherence window.**  
$$
\frac{T_{2}}{T_{c}}=\frac{10^{-3}}{8\times10^{-6}}=125,\qquad
N_{c}=\lfloor125\rfloor=125.
$$

**Derivation 4 — accumulated first‑order error and projected fidelity.**  
$$
\epsilon_{\mathrm{tot}}^{(1)}=N_{c}\,\epsilon_{c}=125\times10^{-5}=1.25\times10^{-3},
$$
$$
F_{\mathrm{proj}}^{(1)}\approx1-1.25\times10^{-3}=0.99875.
$$

**Derivation 5 — actuation update rate per endpoint.**  
$$
R_{u}=\frac{1}{\tau_{p}}=\frac{1}{5\times10^{-7}\,\mathrm{s}}=2\times10^{6}\,\mathrm{s^{-1}}.
$$

**Derivation 6 — aggregate update rate per node.**  
$$
K\,R_{u}=64\times2\times10^{6}\,\mathrm{s^{-1}}=1.28\times10^{8}\,\mathrm{s^{-1}}.
$$

**Derivation 7 — sensitivity to $T_{2}$.**  
Assume a degraded coherence $T_{2}'=10^{-4}\,\mathrm{s}$, the upper end of the $10$–$100\,\mu\mathrm{s}$ range reported in [8].  
$$
N_{c}'=\Bigl\lfloor\frac{10^{-4}}{8\times10^{-6}}\Bigr\rfloor=\lfloor12.5\rfloor=12,
$$
$$
\epsilon_{\mathrm{tot}}^{(1)'}=12\times10^{-5}=1.2\times10^{-4},
$$
$$
F_{\mathrm{proj}}^{(1)'}\approx1-1.2\times10^{-4}=0.99988.
$$
For this degraded coherence the loop latency (Derivation 9) exceeds $T_{2}'$, making latency the binding constraint rather than fidelity.

**Derivation 8 — error‑budget headroom.**  
To keep $\epsilon_{\mathrm{tot}}^{(1)}\le0.01$ with $N_{c}=125$,  
$$
\epsilon_{c}^{\mathrm{max}}=\frac{0.01}{125}=8\times10^{-5},
$$
so the chosen $\epsilon_{c}=10^{-5}$ carries a headroom factor of $8$.

**Derivation 8b — correction of the predecessor’s validity claim.**  
Testing the predecessor’s claim $\epsilon_{c}\le10^{-4}$:  
$$
\epsilon_{\mathrm{tot}}^{(1)}=125\times10^{-4}=1.25\times10^{-2}>0.01,
$$
so the claim fails. Enforcing $N_{c}\,\epsilon_{c}\le0.01$ yields the general condition  
$$
\epsilon_{c}\le\frac{0.01\,T_{c}}{T_{2}}.
$$
For $T_{2}=1\,\mathrm{ms}$ and $T_{c}=8\,\mu\mathrm{s}$ this gives $\epsilon_{c}\le8\times10^{-5}$.

**Inputs (closed‑loop and re‑entry models).**  
- $T_{s}=1.0\times10^{-4}\,\mathrm{s}$ (A7).  
- $T_{p}=2.0\times10^{-5}\,\mathrm{s}$ (A8).  
- $T_{c}'=5.0\times10^{-5}\,\mathrm{s}$ (A9).  
- $T_{a}=1.0\times10^{-5}\,\mathrm{s}$ (A10).  
- $W=64$ bits per qubit per control word (A11).  
- $N_{q}=1000$ qubits (A12).  
- $R_{\mathrm{link}}=1.0\times10^{11}\,\mathrm{bit/s}$ (A13).  
- $\eta_{\mathrm{max}}=0.2$ (A14).  

**Derivation 9 — loop latency.**  
$$
T_{\mathrm{loop}}=1.0\times10^{-4}+2.0\times10^{-5}+5.0\times10^{-5}+1.0\times10^{-5}=1.8\times10^{-4}\,\mathrm{s}.
$$

**Derivation 10 — coherence fraction consumed.**  
$$
\eta=\frac{T_{\mathrm{loop}}}{T_{2}}=\frac{1.8\times10^{-4}}{1.0\times10^{-3}}=0.18\le\eta_{\mathrm{max}}=0.2,
$$
margin $=0.02$, headroom factor $=0.2/0.18\approx1.111$.

**Derivation 11 — control‑plane bandwidth per cycle.**  
$$
B_{\mathrm{cycle}}=W\cdot N_{q}=64\times1000=6.4\times10^{4}\,\mathrm{bits},
$$
$$
\tau_{\mathrm{tx}}=\frac{B_{\mathrm{cycle}}}{R_{\mathrm{link}}}=\frac{6.4\times10^{4}}{1.0\times10^{11}}=6.4\times10^{-7}\,\mathrm{s},
$$
$$
\frac{\tau_{\mathrm{tx}}}{T_{\mathrm{loop}}}= \frac{6.4\times10^{-7}}{1.8\times10^{-4}}\approx3.56\times10^{-3},
$$
i.e. $0.36\%$ of the loop budget. Transport bandwidth is therefore not the binding constraint; the stage latencies $T_{s}$ and $T_{c}'$ dominate the loop.

**Derivation 12 — re‑entry reuse ratio.** Inventory of twelve components (Assumption A15) is:

```
 1  Hamiltonian target specification      P  portable
 2  Pulse‑sequence library                P  portable
 3  Observable‑optimization objective     P  portable
 4  Control‑update algorithm              P  portable
 5  Control‑word encoding                 P  portable
 6  Timing distribution service           I  not portable
 7  Transport/queueing configuration      I  not portable
 8  In‑network compute node image         I  not portable
 9  Sensor/actuator drivers               I  not portable
10  Latency budget manifest               I  not portable
11  Qualification test suite              I  not portable (conservative)
12  Monitoring/telemetry schema           I  portable
```

Portable count $N_{\mathrm{reuse}}=6$, total $N_{\mathrm{tot}}=12$, therefore  
$$
\rho=\frac{6}{12}=0.5.
$$
Counting component 11 as portable would raise $\rho$ to $7/12\approx0.583$; we report the conservative $\rho=0.5$ with bounds $0.5\le\rho\le0.583$.

**Derivation 13 — re‑qualification effort (projection).**  
Assume $e=4$ person‑weeks per non‑portable component (A16):  
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}})=4\times6=24\ \text{person‑weeks}.
$$
Linear uncertainty in $e$ yields $E_{\mathrm{req}}\in[12,48]$ person‑weeks for $e\in[2,8]$.

**Derivation 14 — second‑order commutator error (projection).**  
Assume a second‑order error contribution $\epsilon_{2}=9.81\times10^{-5}$ (A17). Then  
$$
\epsilon_{\mathrm{tot}}^{(2)}=\epsilon_{\mathrm{tot}}^{(1)}+\epsilon_{2}=1.25\times10^{-3}+9.81\times10^{-5}=1.3481\times10^{-3},
$$
$$
F_{\mathrm{proj}}^{(2)}\approx1-1.3481\times10^{-3}=0.9986519.
$$

**Derivation 15 — uncertainty propagation (projection).**  
Assume a $5\%$ relative standard deviation on $\epsilon_{c}$ (A18). The standard deviation on $\epsilon_{\mathrm{tot}}^{(1)}$ is  
$$
\sigma_{\epsilon}=N_{c}\,\epsilon_{c}\times0.05=125\times10^{-5}\times0.05=6.25\times10^{-5}.
$$
Thus $F_{\mathrm{proj}}^{(1)}$ lies in $[0.9986875,0.9988125]$ (projection).

**Derivation 16 — minimum coherence for closed‑loop operation.**  
Require $\eta\le\eta_{\mathrm{max}}$:  
$$
T_{2}^{\min}=\frac{T_{\mathrm{loop}}}{\eta_{\mathrm{max}}}=\frac{1.8\times10^{-4}}{0.2}=9\times10^{-4}\,\mathrm{s}.
$$
For $T_{2}<9\times10^{-4}\,\mathrm{s}$ the loop cannot close within the coherence window.

**Derivation 17 — hardware‑range implication (projection).**  
Current solid‑state devices report $T_{2}^{*}=10$–$100\,\mu\mathrm{s}$ [8]. Since $T_{2}^{*}<T_{2}^{\min}$, closed‑loop operation is infeasible for those devices; only feed‑forward control (no real‑time feedback) remains viable.

**Derivation 19 — jitter budget.**  
We require $J\le0.2\,T_{c}=0.2\times8\,\mu\mathrm{s}=1.6\,\mu\mathrm{s}$. Reported jitter in contemporary 6G packet networks is $100$–$500\,\mu\mathrm{s}$ [8], violating this bound by more than an order of magnitude.

## 5. Results

The derived quantitative metrics are summarized in Table 1. $T_{c}=8\,\mu\mathrm{s}$ (Derivation 1), $f=0.5$ (Derivation 2), $N_{c}=125$ (Derivation 3), $\epsilon_{\mathrm{tot}}^{(1)}=1.25\times10^{-3}$ and $F_{\mathrm{proj}}^{(1)}=0.99875$ (Derivation 4), $\epsilon_{\mathrm{tot}}^{(2)}=1.3481\times10^{-3}$ and $F_{\mathrm{proj}}^{(2)}=0.9986519$ (Derivation 14), $R_{u}=2\times10^{6}\,\mathrm{s^{-1}}$ (Derivation 5), aggregate update rate $1.28\times10^{8}\,\mathrm{s^{-1}}$ (Derivation 6), loop latency $T_{\mathrm{loop}}=1.8\times10^{-4}\,\mathrm{s}$ (Derivation 9), coherence fraction $\eta=0.18$ (Derivation 10), control‑plane payload $B_{\mathrm{cycle}}=6.4\times10^{4}\,\mathrm{bits}$ (Derivation 11), reuse ratio $\rho=0.5$ (Derivation 12), re‑qualification effort $E_{\mathrm{req}}=24$ person‑weeks (Derivation 13), minimum coherence $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$ (Derivation 16), and jitter budget violation (Derivation 19). All values are obtained analytically from the assumptions listed in Section 4.

## 6. Discussion

The analytical framework presented in Sections 4–5 rests on a set of simplifying assumptions that delimit the validity of the architectural conclusions; recognizing these limits is essential before any deployment decision.

*Linear error‑accumulation model is a simplifying approximation.* The derivations treat per‑cycle fractional errors as independent and additive (Derivation 4), which follows directly from the first‑order model introduced in Section 3.2. Reference [5] shows that higher‑order Magnus‑expansion terms can contribute non‑negligible commutator errors, and Derivation 14 explicitly adds a second‑order term $\epsilon_{2}=9.81\times10^{-5}$. Nevertheless, the linear model may under‑estimate coherent error growth when pulse imperfections correlate across cycles.

*Constant per‑cycle error $\epsilon_{c}$ assumes perfect pulse synthesis.* The budget uses a fixed $\epsilon_{c}=10^{-5}$ (A5). In practice, pulse‑shaping hardware and calibration drift can cause cycle‑to‑cycle variations. Reference [1] emphasizes that semi‑classical controllers must cope with environmental fluctuations that affect $\|H_{0}\|$, which in turn modulates the effective error per cycle.

*Coherence time $T_{2}$ is treated as deterministic.* Section 4 adopts $T_{2}=1\,\mathrm{ms}$ (A1) for the nominal analysis, while Derivation 7 explores a degraded $T_{2}'=10^{-4}\,\mathrm{s}$ scenario. Real devices exhibit stochastic $T_{2}$ distributions; the linear relationship $N_{c}=T_{2}/T_{c}$ holds for any $T_{2}$ but the resulting fidelity envelope can shift dramatically.

*Timing jitter and network‑induced latency are assumed bounded.* The loop latency budget (Derivation 9) sums deterministic stage times $T_{s},T_{p},T_{c}',T_{a}$. Reference [8] documents jitter values of $100$–$500\,\mu\mathrm{s}$ in contemporary 6G packet networks, far exceeding the $8\,\mu\mathrm{s}$ cycle period. If actual jitter occupies a non‑negligible fraction of $T_{c}$, the st