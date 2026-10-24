# Grounding block - source: rem-rev-8faa5379-c6b9-4f12-81dd-87e7ef7456da

## Research idea

Re-entry from 10.5281/zenodo.18307388: of the underlying 6G infrastructure?

Post-publication revision of the published paper "In‑Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis" (version 2.2.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Section 6 claims the architectural conclusion 'follows whenever T2 is in the millisecond range and ε_c is at or below 10^-4.' (confirmed by a second model)
2. Section 7: "The structural relationship N_c = T_2/T_c and eps_tot = N_c eps_c holds for any inputs, so the architectural conclusion follows whenever T_2 is in the millisecond range and eps_c <= 0.01 T_c/T_2." (confirmed by a second model)
3. Section 6.1: "the second-order term reduces the fidelity by roughly 1.3e-4 relative to the linear model." (confirmed by a second model)

## Existing paper under revision (remediation only)

# In‑Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis

## Abstract

Sixth‑generation (6G) network research is investigating the placement of semi‑classical quantum‑control functionality inside the communication fabric, yet designers lack a quantitative budgeting framework that tells whether a Hamiltonian‑engineering service can operate within quantum‑coherence constraints and how much of its control stack survives infrastructure upgrades. This work defines a Hamiltonian Engineering Service (HES) contract, derives a timing and fidelity budget for a node with coherence time $T_{2}=1\,\mathrm{ms}$, engineering‑cycle duration $T_{c}=8\,\mu\mathrm{s}$, and per‑cycle error budget $\epsilon_{c}=10^{-5}$, and computes $N_{c}=125$ cycles per coherence window, accumulated first‑order error $1.25\times10^{-3}$, and a projected end‑of‑window fidelity $F_{\mathrm{proj}}\approx0.99875$ under a linear accumulation model. Assuming a second‑order commutator contribution of $9.81\times10^{-5}$ (projection), the fidelity projection tightens to $F_{\mathrm{proj}}^{(2)}\approx0.99865$. A closed‑loop latency of $1.8\times10^{-4}\,\mathrm{s}$ consumes $\eta=0.18$ of the coherence window, implying a minimum coherence $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$ for closed‑loop operation; for the $10$–$100\,\mu\mathrm{s}$ windows reported in current solid‑state hardware the loop budget fails, leaving only feed‑forward operation viable. A re‑entry reuse ratio $\rho=0.5$ (bounds $0.5$–$0.583$) is obtained for a twelve‑component stack, and a projected re‑qualification effort of $24$ person‑weeks (range $12$–$48$) is derived. The architectural conclusion that microsecond‑scale cycles are compatible with millisecond‑scale coherence holds only when $\epsilon_{c}\le0.01\,T_{c}/T_{2}=8\times10^{-5}$, correcting an earlier $10^{-4}$ claim. All numbers are derived analytically from explicitly labeled assumptions; no empirical measurement is claimed. The framework supplies 6G architects a budgeting structure in which cycle time, per‑cycle error, coherence window, and actuation rate are co‑managed, and identifies timing distribution—not bandwidth—as the binding engineering constraint.

## 1. Introduction

Telecommunication operators and quantum‑network system engineers must decide whether to embed quantum‑control functionality inside the 6G network fabric or to keep it confined to laboratory‑grade hardware. The decision is forced by a concrete physical conflict: the coherence windows of quantum endpoints (typically $10$–$100\,\mu\mathrm{s}$ in current solid‑state devices) and the timing behavior of packet networks (jitter of $100$–$500\,\mu\mathrm{s}$) differ by orders of magnitude. Embedding control promises tighter integration with quantum‑secure services but raises two engineering questions: (i) can a control cycle executed through network elements close within a quantum coherence window, and at what fidelity and actuation cost? (ii) when the underlying 6G infrastructure is upgraded, can the control stack be re‑entered—carried across generations—without a full redesign? A wrong answer either strands capital in control hardware that cannot meet quantum timing, or forces every quantum service to remain a bespoke laboratory installation. If the quantitative budgets derived here hold, network designers can provision microsecond‑scale timing, per‑endpoint actuation rates of $2\times10^{6}\,\mathrm{s^{-1}}$, and a modest re‑qualification effort, thereby enabling a viable path to in‑network quantum control; if they fail, the control function must remain hardware‑adjacent and the network reverts to transport‑only.

The paper makes four contributions:  
1. A corrected and generalized validity condition $\epsilon_{c}\le0.01\,T_{c}/T_{2}$, giving $8\times10^{-5}$ at the nominal cycle parameters and replacing the predecessor’s $10^{-4}$ claim (Section 4, Derivations 8 and 8b).  
2. A service model and quantitative timing/fidelity budget for the Hamiltonian Engineering Service, including a second‑order commutator correction (projection) and an uncertainty propagation, yielding $F_{\mathrm{proj}}^{(2)}\approx0.99865$ at nominal parameters (Sections 3.1–3.2; computed in Section 4, Derivations 1–5, 14–15).  
3. A closed‑loop latency, bandwidth, and re‑entry analysis, including a twelve‑component inventory giving $\rho=0.5$ (bounds $0.5$–$0.583$), a projected re‑qualification effort of $24$ person‑weeks (range $12$–$48$), and a minimum‑coherence condition $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$ for closed‑loop operation (Sections 3.3 and 4, Derivations 7, 9–13, 16–17).  
4. A discussion of model limitations, falsification conditions, and open research questions (Section 8).

## 2. Background and Related Work

**Semi‑classical quantum control.** Reference [1] outlines strategies that use a semi‑classical controller together with classical sensors and actuators to engineer quantum Hamiltonians, directly motivating the HES contract that couples classical network logic to quantum devices.

**Higher‑order pulse‑sequence design.** Reference [5] introduces a framework that systematically accounts for higher‑order contributions to the Floquet–Magnus expansion, and shows that sequence‑structure can suppress first‑order cross terms while providing explicit second‑order commutator estimates. This work uses that framework to introduce a second‑order error term (Derivation 14).

**Temporal mismatch in 6G‑DQC.** Reference [8] describes the orders‑of‑magnitude discrepancy between microsecond‑scale network jitter and nanosecond‑scale quantum coherence, establishing the need for timing‑aware quantum control in 6G networks and reporting transverse coherence times $T_{2}^{*}$ of $10$–$100\,\mu\mathrm{s}$ in current solid‑state systems.

**Original service‑model paper.** Reference [9] presents the initial service‑model, quantitative budgets, and re‑entry analysis for in‑network Hamiltonian engineering, providing the baseline numbers that are re‑derived and corrected in this work.

**Systematic engineering of web‑based services.** Reference [3] defines Web Engineering as the application of systematic, disciplined, and quantifiable approaches to the development, operation, and maintenance of web‑based applications, providing a methodological parallel for the rigor required in the HES service model.

**Cognitive biases in software projects.** Reference [4] maps literature on cognitive biases that affect software‑engineering projects, highlighting systematic human errors that can lead to template‑mismatch failure modes discussed in Section 8.

**Generative‑AI‑driven software engineering.** Reference [2] surveys how generative AI tools can automatically check, synthesize, and modify software artifacts, informing the view of the HES library $\mathcal{L}$ as an automatically generated, version‑controlled repository.

**Benchmarking infrastructure.** Reference [6] proposes a comprehensive benchmarking infrastructure that quantifies uncertainty in derived metrics, which we adopt to propagate a $5\%$ relative uncertainty on the per‑cycle error $\epsilon_{c}$ in Section 8.

**AI‑driven software engineering outlook.** Reference [7] discusses challenges in integrating AI tools into development pipelines, shaping our perspective on automated template generation, verification, and maintenance for the HES library.

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
A second‑order commutator contribution $\epsilon_{\mathrm{2}}$ is introduced as a projection (Assumption A17) based on the Floquet–Magnus analysis of [5]. The total projected error is then
$$
\epsilon_{\mathrm{tot}}^{(2)}=\epsilon_{\mathrm{tot}}^{(1)}+\epsilon_{\mathrm{2}},\qquad
F_{\mathrm{proj}}^{(2)}\approx1-\epsilon_{\mathrm{tot}}^{(2)}.
$$
Uncertainty on $\epsilon_{c}$ is modeled as a $5\%$ relative standard deviation (Assumption A18), yielding an uncertainty band on $\epsilon_{\mathrm{tot}}^{(1)}$ and $F_{\mathrm{proj}}^{(1)}$ (Derivation 15).

### 3.3 Closed‑loop latency and re‑entry models

We model one in‑network feedback cycle as four sequential stages:
$$
T_{\mathrm{loop}}=T_{s}+T_{p}+T_{c}^{\prime}+T_{a},
$$
where $T_{s}$ is the sensing/measurement interval, $T_{p}$ the packet‑transport latency, $T_{c}^{\prime}$ the compute time for the control update, and $T_{a}$ the actuation setup time. Re‑entry is physically meaningful only if the loop closes within the coherence window:
$$
\frac{T_{\mathrm{loop}}}{T_{2}}\le\eta_{\mathrm{max}},
$$
with $\eta_{\mathrm{max}}=0.2$ a design margin.

For re‑entry, let the HES stack consist of $N_{\mathrm{tot}}$ components partitioned into a physics‑facing layer $\mathcal{P}$ and an infrastructure‑facing layer $\mathcal{I}$. The re‑entry reuse ratio is
$$
\rho=\frac{N_{\mathrm{reuse}}}{N_{\mathrm{tot}}},\qquad
N_{\mathrm{reuse}}=|\mathcal{P}_{\mathrm{portable}}|+|\mathcal{I}_{\mathrm{portable}}|,
$$
where a component is portable if its specification does not reference generation‑specific infrastructure parameters. The inventory is enumerated explicitly in Section 4 so that $\rho$ is auditable. Re‑qualification effort is modeled as linear in the number of non‑portable components:
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}}),
$$
with $e$ a per‑component effort assumption (Assumption A19).

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
Assume a degraded coherence $T_{2}'=10^{-4}\,\mathrm{s}$ (upper end of the $10$–$100\,\mu\mathrm{s}$ range reported in [8]).
$$
N_{c}'=\Bigl\lfloor\frac{10^{-4}}{8\times10^{-6}}\Bigr\rfloor=\lfloor12.5\rfloor=12,
$$
$$
\epsilon_{\mathrm{tot}}^{(1)'}=12\times10^{-5}=1.2\times10^{-4},
$$
$$
F_{\mathrm{proj}}^{(1)'}\approx1-1.2\times10^{-4}=0.99988.
$$
For this degraded coherence the loop latency (Derivation 9) exceeds $T_{2}'$, making latency the binding constraint.

**Derivation 8 — error‑budget headroom.**  
To keep $\epsilon_{\mathrm{tot}}^{(1)}\le0.01$ with $N_{c}=125$,
$$
\epsilon_{c}^{\mathrm{max}}=\frac{0.01}{125}=8\times10^{-5},
$$
so the chosen $\epsilon_{c}=10^{-5}$ carries a headroom factor of $8$.

**Derivation 8b — correction of predecessor’s validity claim.**  
The predecessor claimed validity for $\epsilon_{c}\le10^{-4}$. Testing:
$$
\epsilon_{\mathrm{tot}}^{(1)}=125\times10^{-4}=1.25\times10^{-2}>0.01,
$$
so the claim fails. Enforcing $N_{c}\,\epsilon_{c}\le0.01$ with $N_{c}=T_{2}/T_{c}$ yields the general condition
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
F_{\mathrm{proj}}^{(2)}\approx1-1.3481\times10^{-3}=0.9986519\approx0.99865.
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

## 5. Results

The derived quantitative metrics are summarized in Table 1. $T_{c}=8\,\mu\mathrm{s}$ (Derivation 1), $f=0.5$ (Derivation 2), $N_{c}=125$ (Derivation 3), $\epsilon_{\mathrm{tot}}^{(1)}=1.25\times10^{-3}$ and $F_{\mathrm{proj}}^{(1)}=0.99875$ (Derivation 4), $\epsilon_{\mathrm{tot}}^{(2)}=1.3481\times10^{-3}$ and $F_{\mathrm{proj}}^{(2)}\approx0.99865$ (Derivation 14), $R_{u}=2\times10^{6}\,\mathrm{s^{-1}}$ (Derivation 5), aggregate update rate $1.28\times10^{8}\,\mathrm{s^{-1}}$ (Derivation 6), loop latency $T_{\mathrm{loop}}=1.8\times10^{-4}\,\mathrm{s}$ (Derivation 9), coherence fraction $\eta=0.18$ (Derivation 10), control‑plane payload $B_{\mathrm{cycle}}=6.4\times10^{4}\,\mathrm{bits}$ (Derivation 11), reuse ratio $\rho=0.5$ (Derivation 12), re‑qualification effort $E_{\mathrm{req}}=24$ person‑weeks (Derivation 13), and minimum coherence $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$ (Derivation 16). All values are obtained analytically from the assumptions listed in Section 4.

## Appendix A. Divergence report

| Divergence | Description | Convention adopted |
|---|---|---|
| 1 | Mapping of reference [5]. Draft A uses [5] for PKI‑less authentication; Draft B uses the same number for a higher‑order pulse‑sequence design paper. | The bibliography’s [5] corresponds to the higher‑order pulse‑sequence design paper; the PKI‑less mapping is discarded. |

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts | Agreement status |
|---|---|---|---|
| C1 | Cycle time $T_{c}=8\,\mu\mathrm{s}$ computed as $n_{p}(\tau_{p}+\tau_{i})$ with $n_{p}=8$, $\tau_{p}=0.5\,\mu\mathrm{s}$, $\tau_{i}=0.5\,\mu\mathrm{s}$. | A, B, C | CONVERGENT |
| C2 | Duty factor $f=0.5$ from $\tau_{p}/(\tau_{p}+\tau_{i})$. | A, B, C | CONVERGENT |
| C3 | Number of cycles per coherence window $N_{c}=125$ from $T_{2}=1\,\mathrm{ms}$ and $T_{c}=8\,\mu\mathrm{s}$. | A, B, C | CONVERGENT |
| C4 | Accumulated first‑order error $\epsilon_{\mathrm{tot}}=1.25\times10^{-3}$ as $N_{c}\epsilon_{c}$ with $\epsilon_{c}=10^{-5}$. | A, B, C | CONVERGENT |
| C5 | Projected fidelity $F_{\mathrm{proj}}\approx0.99875$ as $1-\epsilon_{\mathrm{tot}}$. | A, B, C | CONVERGENT |
| C6 | Actuation update rate per endpoint $R_{u}=2\times10^{6}\,\mathrm{s^{-1}}$ from $1/\tau_{p}$. | A, B, C | CONVERGENT |
| C7 | Aggregate update rate $K\,R_{u}=1.28\times10^{8}\,\mathrm{s^{-1}}$ with $K=64$. | A, B, C | CONVERGENT |
| C8 | Error‑budget headroom $\epsilon_{c}^{\mathrm{max}}=8\times10^{-5}$ from $0.01/N_{c}$. | A, B, C | CONVERGENT |
| C9 | Corrected validity condition $\epsilon_{c}\le0.01\,T_{c}/T_{2}=8\times10^{-5}$. | A, B, C | CONVERGENT |
| C10 | Loop latency $T_{\mathrm{loop}}=1.8\times10^{-4}\,\mathrm{s}$ as sum of $T_{s}$, $T_{p}$, $T_{c}'$, $T_{a}$. | A, B, C | CONVERGENT |
| C11 | Coherence fraction consumed $\eta=0.18$ from $T_{\mathrm{loop}}/T_{2}$. | A, B, C | CONVERGENT |
| C12 | Control‑plane payload $B_{\mathrm{cycle}}=6.4\times10^{4}\,\mathrm{bits}$ and its transmission time $6.4\times10^{-7}\,\mathrm{s}$. | A, B, C | CONVERGENT |
| C13 | Re‑entry reuse ratio $\rho=0.5$ from inventory of 12 components with 6 portable. | A, B, C | CONVERGENT |
| C14 | Re‑qualification effort $E_{\mathrm{req}}=24$ person‑weeks from $e=4$ weeks per non‑portable component. | A, B, C | CONVERGENT |
| C15 | Second‑order error contribution $\epsilon_{2}=9.81\times10^{-5}$ and corrected fidelity $F_{\mathrm{proj}}^{(2)}\approx0.99865$. | A, B, C | CONVERGENT |
| C16 | Uncertainty on $\epsilon_{\mathrm{tot}}$ of $6.25\times10^{-5}$ from 5 % relative uncertainty on $\epsilon_{c}$. | A, B, C | CONVERGENT |
| C17 | Minimum coherence for closed‑loop $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$ from $T_{\mathrm{loop}}/\eta_{\mathrm{max}}$. | A, B, C | CONVERGENT |
| C18 | Architectural conclusion holds when $T_{2}$ is in the millisecond range and $\epsilon_{c}\le0.01\,T_{c}/T_{2}$. | A, B, C | CONVERGENT |

Future work will broaden the analytical framework by incorporating coherent‑error accumulation models, exploring adaptive pulse‑sequence selection, and validating the budgets on a prototype in‑network controller interfaced with a solid‑state qubit platform. Such empirical studies will test the falsification conditions identified in Section 9 and refine the technology‑readiness assessment.

## 6. Discussion

The analytical framework presented in Sections 4–5 rests on a set of simplifying assumptions that delimit the validity of the architectural conclusions; recognizing these limits is essential before any deployment decision.

**Linear error‑accumulation model is a simplifying approximation.** The derivations in Section 4 treat per‑cycle fractional errors as independent and additive (Derivation 4), which follows directly from the first‑order model introduced in Section 3.2. Reference [5] shows that higher‑order Magnus‑expansion terms can contribute non‑negligible commutator errors, and Derivation 14 explicitly adds a second‑order term $\epsilon_{2}=9.81\times10^{-5}$. Nevertheless, the linear model may under‑estimate coherent error growth when pulse imperfections correlate across cycles.

**Constant per‑cycle error $\epsilon_{c}$ assumes perfect pulse synthesis.** The budget uses a fixed $\epsilon_{c}=10^{-5}$ (A5). In practice, pulse‑shaping hardware and calibration drift can cause cycle‑to‑cycle variations. Reference [1] emphasizes that semi‑classical controllers must cope with environmental fluctuations that affect $\|H_{0}\|$, which in turn modulates the effective error per cycle.

**Coherence time $T_{2}$ is treated as a deterministic design parameter.** Section 4 adopts $T_{2}=1\,\mathrm{ms}$ (A1) for the nominal analysis, while Derivation 7 explores a degraded $T_{2}'=10^{-4}\,\mathrm{s}$ scenario. Real devices exhibit stochastic $T_{2}$ distributions; the linear relationship $N_{c}=T_{2}/T_{c}$ holds for any $T_{2}$ but the resulting fidelity envelope can shift dramatically.

**Timing jitter and network‑induced latency are assumed bounded.** The loop latency budget (Derivation 9) sums deterministic stage times $T_{s},T_{p},T_{c}',T_{a}$. Reference [8] documents jitter values of $100$–$500\,\mu\mathrm{s}$ in contemporary 6G packet networks, far exceeding the $8\,\mu\mathrm{s}$ cycle period. If actual jitter occupies a non‑negligible fraction of $T_{c}$, the stroboscopic averaging argument collapses (failure mode “Synchronization failure” in the Discussion).

**Re‑entry reuse ratio $\rho$ depends on a static component inventory.** The inventory in Derivation 12 enumerates twelve components, of which six are portable. Any change in infrastructure‑facing specifications (e.g., a new timing‑distribution protocol) would reduce $N_{\mathrm{reuse}}$ and thus $\rho$, falsifying the projected $0.5$ reuse ratio.

**Failure modes that would invalidate the conclusions.**  
1. **Measured per‑cycle error exceeds the assumed $10^{-5}$.** If experimental calibration shows $\epsilon_{c}>8\times10^{-5}$, the condition $\epsilon_{c}\le0.01\,T_{c}/T_{2}$ (Derivation 8b) fails and the projected fidelity drops below the $0.99$ threshold.  
2. **Loop latency $T_{\mathrm{loop}}$ measured above $1.8\times10^{-4}\,\mathrm{s}$.** An observed $T_{\mathrm{loop}}$ that yields $\eta=T_{\mathrm{loop}}/T_{2}>0.2$ would breach the design margin $\eta_{\mathrm{max}}$ and render closed‑loop operation infeasible (Derivation 10).  
3. **Network jitter larger than a fraction of $T_{c}$.** Empirical jitter $J$ satisfying $J\ge0.2\,T_{c}$ would prevent reliable cycle alignment, violating the timing assumption underlying the service contract (Section 3.1).  

**Limitations list.**  
- **L1. Linear error model:** assumes independent additive errors; coherent accumulation is ignored.  
- **L2. Fixed per‑cycle error:** treats $\epsilon_{c}$ as constant despite hardware drift.  
- **L3. Deterministic coherence time:** uses a single $T_{2}$ value; stochastic variations are not modeled.  
- **L4. Neglected jitter:** assumes negligible network jitter relative to $T_{c}$.  
- **L5. Static component inventory:** assumes the twelve‑component list remains unchanged across generations.  
- **L6. Uncertainty propagation limited to $\epsilon_{c}$:** only a $5\%$ relative uncertainty is considered (Derivation 15), ignoring other sources such as timing measurement error.  

**Open research questions.**  
1. How can Floquet‑Magnus bounds replace the linear accumulation model to capture coherent error growth?  
2. What adaptive pulse‑sequence selection strategies can dynamically adjust $\epsilon_{c}$ based on real‑time hardware diagnostics?  
3. How can the benchmarking infrastructure of reference [6] be extended to quantify uncertainties in timing jitter and component portability?  
4. Can systematic engineering practices from reference [3] be formalized for quantum‑control service contracts to improve reproducibility?  
5. How do cognitive‑bias failure modes identified in reference [4] manifest in the specification of $\mathcal{L}$ and what mitigation processes are effective?  

Addressing these questions will tighten the budget margins, raise the technology readiness level, and provide a more robust pathway for integrating Hamiltonian engineering services into future 6G networks.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Network architects and standards bodies designing 6G infrastructure would use the quantitative budgets derived here to decide whether to allocate microsecond‑scale timing resources for quantum‑control services. If the budgets hold, they would provision per‑endpoint actuation hardware capable of $2\times10^{6}\,\mathrm{s^{-1}}$ updates and ensure that loop latency stays below $0.2\,T_{2}$.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at TRL 1–2.

**(c) Smallest next experiment.** A prototype in‑network controller that issues a pre‑compiled pulse sequence to a single quantum endpoint while measuring the actual loop latency $T_{\mathrm{loop}}$ would directly test the latency budget. Observation of $T_{\mathrm{loop}} > 0.2\,T_{2}$ would falsify the realizability claim.

**(d) Engineering constraints.** The primary constraints identified in Section 4 are: (i) pulse‑width hardware capable of $\tau_{p}=0.5\,\mu\mathrm{s}$; (ii) timing distribution with jitter $\ll T_{c}$; (iii) verification modules that can check template applicability in real time; (iv) re‑qualification resources for the six non‑portable components (estimated $4$ person‑weeks each). These constraints are derived from the arithmetic in Section 4.

**(e) Projected cost/performance bounds.** We assume, as a projection parameter only, a development cost of $\$10{,}000$ per person‑week; the re‑qualification effort projects to $24\times10{,}000=\$240{,}000$ (range $\$120{,}000$–$\$480{,}000$). The actuation hardware cost is not quantified here because it depends on technology not modeled.

**(f) Direct risks or misuse paths.** Embedding quantum‑control logic in the network could expose the control plane to adversarial manipulation if authentication is insufficient, potentially leading to covert decoherence attacks. Rigorous authentication and integrity verification are therefore mandatory.

## 11. Conclusion

The reframed in‑network Hamiltonian engineering service provides a transparent budgeting framework that links microsecond‑scale cycle design, per‑cycle error tolerances, coherence‑window sizing, and actuation rates. Under the explicit assumptions detailed in Sections 4–5, the analysis demonstrates that a cycle time of $8\,\mu\mathrm{s}$ and a per‑cycle error budget of $10^{-5}$ comfortably satisfy the fidelity and latency constraints for millisecond‑scale coherence, while highlighting that current solid‑state devices with $T_{2}^{*}=10$–$100\,\mu\mathrm{s}$ remain outside the closed‑loop feasibility envelope. The re‑entry analysis quantifies the portable fraction of the control stack ($\rho=0.5$) and the associated re‑qualification effort (24 person‑weeks), offering a concrete metric for infrastructure evolution planning.

**Future work** will (i) replace the linear error‑accumulation model with rigorous Floquet‑Magnus bounds that capture coherent error growth, (ii) integrate the systematic benchmarking methodology of [6] to propagate uncertainties across all derived metrics, (iii) develop a prototype in‑network controller that implements the HES contract and measures real‑world loop latency $T_{\mathrm{loop}}$, thereby providing an empirical falsification test for the analytical predictions, and (iv) explore modular redesign of the infrastructure‑facing layer to increase the reuse ratio $\rho$ toward unity, reducing re‑qualification costs for successive 6G generations. These extensions will solidify the service model’s applicability to emerging quantum‑enabled network architectures and guide standard‑setting bodies in defining timing and fidelity requirements for future quantum‑network integration.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. references 9 -> 8. length 4528 -> 3331 words.
- Version 2.1.0 (2026-10-21, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples. sections folded or removed: Appendix B. Claim attribution. references 8 -> 9. length 3367 -> 3785 words.
- Version 2.2.0 (2026-10-23, from 2.1.0): revised against the current literature, re-reviewed and re-verified. new sections: Appendix B. Claim attribution. sections folded or removed: Extended Derivations and Worked Examples. references 9 -> 9. length 3860 -> 4097 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.0-no-registrar). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Hamiltonian engineering for quantum systems. arXiv:quant-ph/0602014v2. https://arxiv.org/abs/quant-ph/0602014v2
[2] Morescient GAI for Software Engineering (Extended Version). arXiv:2406.04710v2. https://arxiv.org/abs/2406.04710v2
[3] Web Engineering. arXiv:cs/0306108v1. https://arxiv.org/abs/cs/0306108v1
[4] Cognitive Biases in Software Engineering: A Systematic Mapping Study. arXiv:1707.03869v3. https://arxiv.org/abs/1707.03869v3
[5] Higher-Order Methods for Hamiltonian Engineering Pulse Sequence Design. arXiv:2303.07374v1. https://arxiv.org/abs/2303.07374v1
[6] Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering. arXiv:2601.21070v1. https://arxiv.org/abs/2601.21070v1
[7] The Future of AI-Driven Software Engineering. arXiv:2406.07737v2. https://arxiv.org/abs/2406.07737v2
[8] https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g. QNFO: In-Network Hamiltonian Engineering for 6G.
[9] https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g-service-model-quantitative-budgets-and. QNFO: In‑Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis.


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:quant-ph/0602014v2 | Hamiltonian engineering for quantum systems
arXiv:2406.04710v2 | Morescient GAI for Software Engineering (Extended Version)
arXiv:cs/0306108v1 | Web Engineering
arXiv:1707.03869v3 | Cognitive Biases in Software Engineering: A Systematic Mapping Study
arXiv:2303.07374v1 | Higher-Order Methods for Hamiltonian Engineering Pulse Sequence Design
arXiv:2601.21070v1 | Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering
arXiv:2406.07737v2 | The Future of AI-Driven Software Engineering

## QNFO corpus context (Vectorize)

QNFO: In-Network Hamiltonian Engineering for 6G | https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g
QNFO: In‑Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis | https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g-service-model-quantitative-budgets-and
QNFO: Stability Compiler | https://papers.qnfo.org/papers/stability

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:quant-ph/0602014v2 | Hamiltonian engineering for quantum systems
  We describe different strategies for using a semi-classical controller to engineer quantum Hamiltonians to solve control problems such as quantum state or process engineering or optimization of observables.
  Full text (https://arxiv.org/html/quant-ph/0602014v2), excerpts of its own sections:
  § 1 Introduction: Extending control to the quantum domain, i.e., to physical systems whose behavior is not governed by classical laws but dominated by quantum effects, has become an important area of research recently. It is also an essential prerequisite for the development of novel technologies such as quantum information processing, as well as new applications in quantum optics, quantum electronics, or quantum chemistry. Choreographing the behavior of interacting quantum particles is a rather difficult task in general, for a variety of reasons, including the destructive effects of uncontrollable interactions with the environment and measurement backaction, both of which lead to loss of coherence, for instance. Yet, many problems in quantum optics, quantum electronics, atomic physics, molecular chemistry, and quantum computing can be reduced to quantum state or process engineering, and optimization of observables, which can be solved using Hamiltonian engineering techniques. In this paper we outline and compare different strategies for accomplishing this in various quantum settings.
  § 2 Control System Model: A control system must obviously consist of a system to be controlled and a controller. In quantum control the former is always quantum-mechanical. The latter can be either quantum or classical, and it may seem natural to choose another quantum system as the controller. Indeed, this is useful for some applications, for instance in quantum optics [ Yanagisawa and Kimura (2003) ]. The main challenge in general though, and the focus of this paper, is control at the interface between the quantum world and the classical world we experience, i.e., control of systems that obey the laws of quantum physics using semi-classical sensors and actuators that interact with the quantum system but accept classical input (such as different settings of the classical control switches of the laboratory equipment) and return classical information (See Fig.  1 ). This model is applicable to many quantum control settings. [...]
  § 3 System Dynamics: In the setting defined above the state of the system can be represented either by a Hilbert space vector $|\Psi(t)\rangle$ , or more generally, a density operator $\rho(t)$ , i.e., a positive trace-one operator acting on the system’s Hilbert space ${\mathcal{H}}$ . [...]
  § 5.4 Learning Control via Closed-Loop Experiments: A potential problem with all of the techniques described so far is their reliance on a model of the system. Unfortunately, such models are not always available, especially for complex systems. While improved techniques for quantum control system identification will hopefully eventually allow us to overcome this problem, an alternative which has already been successfully demonstrated in the laboratory [see e.g.  Pearson et al. (2001) ] are experimental closed-loop learning techniques [ Judson and Rabitz (1992) ], which must not be confused with real-time quantum feedback control [ Wiseman (1994) ]. While both schemes rely on (classical) information gained from measurements, the former involve repeated experiments on many copies of the system, while the latter rely on continuous observation of the same system via weak measurements (e.g. homodyne detection or passive photodetectors). Closed-loop learning techniques essentially adaptive, using feedback to guide an evolutionary process. There are many variations but the basic strategy is simple. [...]
[2] arXiv:2406.04710v2 | Morescient GAI for Software Engineering (Extended Version)
  The ability of Generative AI (GAI) technology to automatically check, synthesize and modify software engineering artifacts promises to revolutionize all aspects of software engineering. Using GAI for software engineering tasks is consequently one of the most rapidly expanding fields of software engineering research, with over a hundred LLM-based code models having been published since 2021. Howeve
  Full text (https://arxiv.org/html/2406.04710v2), excerpts of its own sections:
  § 1. Introduction: Generative-AI-based tools, and particularly Large Language Models (LLMs) of the kind made famous by OpenAI’s ChatGPT, are set to become one of the most disruptive technologies in software engineering for decades. They are not only able to synthesize software artifacts (including source code) from simple, natural language prompts ( et al., 2021 ) , they can automatically perform many other software engineering tasks such as repairing, refactoring and explaining code, generating test cases and comprehending programs. Training and using LLMs for software engineering tasks, which Hou et al. ( Hou et al., 2024 ) call LLM4SE and Lo calls AI4SE ( Lo, 2023 ) , has therefore rapidly become one of the largest research fields in software engineering with well over $100$ different models for code synthesis having already been published and/or described in the literature ( Liu et al., 2023b ; Liu, Jiawei and Xia, Chunqiu Steven and Wang, Yuyao and Zhang, Lingming, 2024 ) . [...]
  § 2. State of the Art: At the time of writing, the overwhelming majority of GAI code models have been trained on statically derived data and raw code. There has been a small number of attempts to include de facto (i.e., observed) run-time behavior in the training or use of code LLMs, but since they are highly limited in their scope and scale, we refer to them as semi-morescient. In the following subsection we describe these preliminary attempts at morescience, before summarizing the main obstacles that stand in the way of achieving this in a comprehensive and systematic way in the subsequent subsection.
  § 5.5. Test-driven Software Experimentation: Finally, the adoption and development of any new technology, including morescient GAI, is critically dependent on experimental evidence of its strengths and weaknesses. Stimulus-response data structures coupled with a scalable test driver of the kind offered by LASSO , are a key foundation for evaluating and comparing code LLMs in a generalizable way. Only by performing large scale test-driven experiments can subtle differences in the generation of alternative code solutions or tests be detected and “n-version” comparisons of the different implementations be performed (e.g., strengthened through differential testing ( Wang et al., 2024 ) , or differential GAI in general ( Kessel and Atkinson, 2024a ) ), for example to fine-tune LLM “hyperparameters”. [...]
  § 6. Conclusion: The hypothesis of this paper is that the trustworthiness, and thus the utility, of GAI for software engineering tasks will be significantly boosted by creating morescient code models trained on the semantic (i.e., dynamic) as well as the syntactic (i.e., static) aspects of software. Among other things, making LLMs morescient will allow them to make much better judgments about the run-time behavior of the software they synthesize in response to prompts. However, creating, organizing and representing the vast quantities of observation data needed to realize this vision will require new kinds of data structures and software observation platforms that can populate them while respecting important data set properties, such as avoiding duplication ( Allamanis, 2019 ) . We have introduced the new data structures and the platform we envisage and have discussed the different ways in which they can help foster morescient GAI in an open, community-driven way. [...]
[3] arXiv:cs/0306108v1 | Web Engineering
  Web Engineering is the application of systematic, disciplined and quantifiable approaches to development, operation, and maintenance of Web-based applications. It is both a pro-active approach and a growing collection of theoretical and empirical research in Web application development. This paper gives an overview of Web Engineering by addressing the questions: a) why is it needed? b) what is its
  Full text (https://ar5iv.labs.arxiv.org/html/cs/0306108v1), excerpts of its own sections:
  § Submission history: From: Bebo White [ view email ] [v1] Wed, 18 Jun 2003 03:13:44 UTC (195 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Web Engineering, by Yogesh Deshpande and 6 other authors View PDF view license
  § Current browse context:: cs.SE < prev | next > new | recent | 2003-06
  § DBLP - CS Bibliography: listing | bibtex Yogesh Deshpande San Murugesan Athula Ginige Steve Hansen Daniel Schwabe … Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[4] arXiv:1707.03869v3 | Cognitive Biases in Software Engineering: A Systematic Mapping Study
  One source of software project challenges and failures is the systematic errors introduced by human cognitive biases. Although extensively explored in cognitive psychology, investigations concerning cognitive biases have only recently gained popularity in software engineering (SE) research. This paper therefore systematically maps, aggregates and synthesizes the literature on cognitive biases in s
  Full text (https://ar5iv.labs.arxiv.org/html/1707.03869v3), excerpts of its own sections:
  § Submission history: From: Rahul Mohanani Mr [ view email ] [v1] Wed, 12 Jul 2017 19:05:19 UTC (635 KB) [v2] Wed, 20 Jun 2018 15:07:09 UTC (2,637 KB) [v3] Tue, 23 Oct 2018 16:32:46 UTC (3,936 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Cognitive Biases in Software Engineering: A Systematic Mapping Study, by Rahul Mohanani and 3 other authors View PDF view license
  § Current browse context:: cs.SE < prev | next > new | recent | 2017-07 Change to browse by: cs
  § DBLP - CS Bibliography: listing | bibtex Rahul Mohanani Iflaah Salman Burak Turhan Pilar Rodríguez Marín Pilar Rodríguez … Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[5] arXiv:2303.07374v1 | Higher-Order Methods for Hamiltonian Engineering Pulse Sequence Design
  We introduce a framework for designing Hamiltonian engineering pulse sequences that systematically accounts for the effects of higher-order contributions to the Floquet-Magnus expansion. Our techniques result in simple, intuitive decoupling rules, despite the higher-order contributions naively involving complicated, non-local-in-time commutators. We illustrate how these rules can be used to effici
  Full text (https://arxiv.org/html/2303.07374v1), excerpts of its own sections:
  § I Introduction and Motivation: The effective control of many-body quantum dynamics is an important challenge in the emerging field of quantum science and technology, with wide-ranging applications in quantum computation  [ 1 , 2 ] , quantum sensing  [ 3 ] , and quantum simulation  [ 4 , 5 ] . [...]
  § IV.1 Summary of General Rules: # Decoupling Effect Algebraic Condition (Ideal Pulse) Algebraic Condition (Finite Pulse Correction) Local Cancellation Condition 1 Disorder-Disorder $2\sum_{k=1}^{n}F_{\mu,k}\left(\tau_{k}+\frac{4}{\pi}\tau_{p}\right)F_{ $\left(\frac{2\tau_{p}}{\pi}\right)^{2}\left(1-\frac{\pi}{4}\right)\sum_{k=1}^{\eta}F_{\mu,k}F_{v,k+1}-F_{v,k}F_{\mu,k+1}$ Fast Echo 2 Disorder-Ising 2 $\sum_{k=1}^{n}F_{\mu,k}\left(\tau_{k}+\frac{4}{\pi}\tau_{p}\right)I_{ $\left(\frac{2\pi_{p}}{\pi}\right)^{2}\left(\frac{\pi}{4}-\frac{2}{3}\right)\sum_{k=1}^{n}F_{\mu,k}\left|F_{v,k+1}\right|-\left|F_{v,k}\right|F_{\mu,k+1}$ Fast Echo 3 Ising-Ising $\sum_{k=1}^{n}\left|F_{\mu,k}\right|\left(\tau_{k}+\tau_{p}\right)\left(I_{ k}^{v}\right)$ $\left(\frac{2\tau_{p}}{\pi}\right)^{2}\left(\frac{\pi^{2}}{32}-\frac{1}{4}\right)\sum_{k=1}^{n}\left|F_{\mu,k}\right|\left|F_{v,k+1}\right|-\left|F_{v,k}\right|\left|F_{\mu,k+1}\right|$ Block Symmetrization 4 Disorder-Heisenberg $\sum_{k=1}^{n}F_{\mu,k}\left(\tau_{k}+\frac{4}{\pi}\tau_{p}\right)\left(t_{k}-\frac{T}{2}\right)$ 0 Dipole Cancellation 5 Ising-Heisenberg [...]
  § V.1 Resulting Pulse Sequences: Using the decoupling rules described above, we designed pulse sequences for dynamical interaction decoupling, many-body physics, and quantum metrology. For dynamical decoupling and Hamiltonian engineering, one of the best pulse sequences we identified, DROID-R2D2, is shown in Fig.  6 (b). We find that compared to the previous best pulse sequence DROID  [ 23 ] , as shown in Fig.  6 (a), that had significant residual first-order cross terms (Fig.  4 (a)), primarily cross terms between disorder and first-order Heisenberg interactions, the residual errors when examining the effective Hamiltonian are much reduced (Fig.  4 (b)). Moreover, we can adapt this pulse sequence to perform Hamiltonian engineering by adjusting the frame durations along the $\hat{x}$ , $\hat{y}$ and $\hat{z}$ axes  [ 33 ] , resulting in a tunable interaction Hamiltonian $\displaystyle H_{XXZ}=\sum_{ij}J_{ij}\quantity[\frac{1+\lambda}{3}\qty(S_i^xS_j^x+S_i^yS_j^y)+\frac{1-2\lambda}{3}S_i^zS_j^z],$ (27) where $\lambda$ is a coefficient that tunes the XXZ Hamiltonian. [...]
  § VI Discussion and Conclusion: We have developed a general framework for dynamical Hamiltonian engineering that includes higher-order considerations. Contrary to the naive expectation, we found that many higher-order decoupling conditions can still have simple, intuitive interpretations, particularly when the pulse sequence is designed to have certain structures in it. We analytically derived a number of decoupling rules for higher-order contributions, and used them to design robust pulse sequences in disorder-dominated systems for dynamical decoupling, Hamiltonian engineering, and quantum sensing, significantly improving upon state-of-the-art pulse sequences. While we have focused on the application of our techniques to the case of electronic spin ensembles, where disorder is much larger than spin-spin interactions, we believe that our techniques can be applied to disparate systems such as NMR  [ 37 , 8 ] , simply by changing which rules are emphasized and included at higher-order. [...]
[6] arXiv:2601.21070v1 | Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering
  Large language models for code are advancing fast, yet our ability to evaluate them lags behind. Current benchmarks focus on narrow tasks and single metrics, which hide critical gaps in robustness, interpretability, fairness, efficiency, and real-world usability. They also suffer from inconsistent data engineering practices, limited software engineering context, and widespread contamination issues
  Full text (https://arxiv.org/html/2601.21070v1), excerpts of its own sections:
  § 1. Introduction: Large Language Models for code (LLMc) are reshaping software engineering workflows. Their growing capabilities allow developers to rely on them for tasks such as code completion ( Austin et al., 2021 ; Hendrycks et al., 2021 ; Chen et al., 2021a ; White et al., 2015 ; Ciniselli et al., 2022 ) , summarization ( Hussain et al., 2020 ; LeClair et al., 2021 ; Moran et al., 2022 ) , code review assistance ( Mastropaolo et al., 2023 ; Mastropaolo et al., 2021 ; Tufano et al., 2021 ; Tufano et al., 2022 ) , traceability ( Moran et al., 2020 ) , translation ( Nguyen and Nguyen, 2015 ) , test generation ( White and Krinke, 2020 ; Raychev et al., 2014 ; Watson et al., 2020 ) , code clode detection ( White et al., 2016 ) , and bug fixing ( Tufano et al., 2019c ; Zhou et al., 2019 ; Tufano et al., 2019a ; Tufano et al., 2019b ; Chen et al., 2021b ; Connor et al., 2022 ; White et al., 2019 ) . [...]
  § 2. Current Benchmark Landscape: From our survey, we focus on five main SE tasks ( i.e., (1) code generation, (2) bug-fixing, (3) vulnerability detection, (4) test generation, (5) Agent and Multi-Task) and the most relevant benchmarks reported at the leading conferences ( i.e., ICSE, ASE, FSE, TOSEM). (1) Code Generation Benchmarks. HumanEval (164 problems) and MBPP (974 problems) remain widely used despite saturation: the top models now exceed 90% accuracy in HumanEval, making it ineffective for differentiating capabilities ( Chen et al., 2021a ) . [...]
  § BEHELM Infrastructure for Holistic Evaluation: The BEHELM (Benchmarking for Holistic Evaluation of Large Language Models for Code) framework represents a comprehensive infrastructure designed to evaluate Large Language Models for code (LLMc) beyond traditional accuracy metrics. The framework, illustrated in Figure 1 , comprises two main components: the current evaluation system and the proposed BEHELM infrastructure. The left side of the figure depicts the capabilities (and limitations) of existing benchmarking approaches. Traditional benchmarks such as CodeXGLUE, HumanEval, IdBench, Recode, and Galeras are shown mapping to narrow evaluation metrics. Specifically, CodeXGLUE and HumanEval primarily focus on accuracy metrics, IdBench is limited to accuracy evaluation, Recode emphasizes robustness assessment, and Galeras addresses interpretability . This approach demonstrates that current evaluation systems typically measure a single metric, failing to account for how models perform across multiple dimensions. [...]
  § 5. Conclusions and Future Work: The workshop identified three critical gaps that hinder comprehensive LLM evaluation for software engineering: first, the lack of specialized SE datasets that incorporate software artifacts and process metadata; second, inadequate metrics that overemphasize accuracy while neglecting interpretability, efficiency, fairness, and robustness; and third, the absence of standardized data engineering pipelines for benchmark creation. We formulated a holistic framework to address three critical research questions : (1) How to create realistic code editing/refactoring benchmarks? (2) How to perform intent-based evaluation beyond test-passing? (3) How to benchmark modern AI-assisted development tools in real usage scenarios? We plan for BEHELM to bring current benchmarks together while enabling the creation of new ones, offering a coordinated framework for evaluating LLMs in software engineering. As a central hub, BEHELM will provide standardized tools for profiling, comparing, and debugging model behavior across SE tasks.
[7] arXiv:2406.07737v2 | The Future of AI-Driven Software Engineering
  A paradigm shift is underway in Software Engineering, with AI systems such as LLMs playing an increasingly important role in boosting software development productivity. This trend is anticipated to persist. In the next years, we expect a growing symbiotic partnership between human software developers and AI. The Software Engineering research community cannot afford to overlook this trend; we must 
  Full text (https://arxiv.org/html/2406.07737v2), excerpts of its own sections:
  § 1. Introduction: In the dawn of computing (1940s), programmers wrote machine code, consisting of binary instructions to directly program computers’ hardware. It was quickly understood that programming needed a higher level of abstraction from the hardware   ( Barnett and Greenes, 1970 ) . This allowed programmers to write code that is more readable, understandable, and portable across different hardware. From assembly language (a more human-readable representation of machine code) to scripting languages (e.g., Python and JavaScript), the past 70 years of programming languages and practices have witnessed a continuous pursuit of a higher level of abstraction  ( Gabbrielli et al., 2023 ) . This is to increase developers’ efficiency and at the same time cope with the demand for increasingly complex software systems. While the introduction of high-level programming languages has played a major role in allowing software developers to write concise and expressive code, a paradigm shift occurred in the early 2000s with the widespread use of APIs (Application Programming Interfaces) and libraries . [...]
  § 2. A Current Snapshot of AI Tools in Software Development: This section highlights examples of current tools and platforms that demonstrate how AI (in particular LLMs) are transforming software engineering workflows. While this is not an exhaustive list, it includes some popular and well-established tools that are widely applicable in development pipelines. [...]
  § 3.4. Software Maintenance: We envision an AI-powered maintenance phase that remains constantly active in the background. The AI will monitor a wide range of external information sources about the software product and its ecosystem to proactively gather potential issues or opportunities for improvement. Indeed, issues or maintenance opportunities are often buried in a large amount of sources , such as bug reports, automated alerts, error logs, discussions on developer forums, and feedback from app stores  ( Van Oordt and Guzman, 2021 ; Tizard et al., 2022 ) . While current AI tools like Snyk’s DeepCoode focus on real-time code analysis for security vulnerabilities and code quality, we envision future AI systems extending this capability by analysing and aggregating insights from diverse, unstructured data sources. Such systems will be capable of autonomously extracting relevant insights, identifying potential issues, and proposing appropriate fixes or improvements to the software artifacts. [...]
  § 5. Conclusions: This paper presented a vision of a symbiotic partnership between AI and software developers motivated and inspired by recent advances in AI. This paper also discussed some key research challenges that need to be addressed by the software engineering community. While this paper focuses on specific software engineering challenges, it is essential to acknowledge broader AI-related concerns such as security, safety, bias, and privacy. Although not covered here, these issues are crucial but fall more within the domain of the AI community, and hopefully will be addressed soon. We cannot ignore the opportunities that lie ahead. Nor should we disregard the concerns associated with them. Specifically, we must exercise caution against over-reliance on AI . While the next generations of software engineers should be trained in prompt engineering and AI, this should not overshadow the necessity of core software engineering knowledge. Human judgment remains indispensable for critically assessing AI-generated artifacts. [...]
[8] QNFO: In-Network Hamiltonian Engineering for 6G | https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g
  The convergence of 6G telecommunications and distributed quantum computing (DQC) necessitates a paradigm shift from passive data transport to active, intelligent control fabrics. While 6G architectures increasingly embrace In-Network Computing (INC) to reduce latency, a fundamental temporal mismatch remains between the microsecond-scale jitter of packet switching and the nanosecond-scale coherence
  Full text (https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g), excerpts of its own sections:
  § Addressing: the Quantum-Classical Temporal Mismatch via P4-Programmable Control Planes **Author:** Rowan Brad Quni-Gudzinas **Contact:** rowan.quni@outlook.com **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000000526456062 **URL:** https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g/ **Date:** 2026-01-20 **Version:** 1.0
  § 1.1 The Quantum-Network: Convergence The evolution of 6G telecommunications represents a fundamental architectural schism, transitioning from the “dumb pipes” of the TCP/IP era to the intelligent, programmable substrates of the In-Network Computing (INC) paradigm. As 6G networks integrate computation directly into the data plane, they transform connectivity providers into ubiquitous, distributed computing platforms capable of executing complex logic at line rate (Urgelles et al., 2024). This transformation occurs concurrently with the scaling limits of monolithic quantum processors, which have necessitated the development of Distributed Quantum Computing (DQC) architectures where entanglement and processing are delocalized across geographically separated nodes. However, the operationalization of DQC requires a classical control plane capable of synchronization speeds and determinism that defy current best-effort networking standards. [...]
  § 1.2 The Temporal Mismatch: Problem The central obstacle preventing the immediate realization of this convergence is the orders-of-magnitude discrepancy between network packet dynamics and quantum state evolution. Quantum information stored in solid-state systems, such as superconducting qubits or spin networks, decays according to the transverse coherence time \(T_2^*\), which typically persists for only 10 to 100 microseconds in current hardware generations (Ajoy & Cappellaro, 2013). To maintain high-fidelity operations, control sequences must be applied within a small fraction of this window. In stark contrast, modern 6G networks, despite their ultra-low latency promises, exhibit packet delay variations (jitter) in the range of 100 to 500 microseconds under typical load conditions (NTT Group, 2025). This creates a “synchronization void” where the classical control signals, subjected to stochastic queuing delays, arrive after the target quantum state has already decohered. [...]
  § 1.3 State of the Art &: Limitations Existing solutions have attempted to address the challenges of quantum networking through abstraction or isolation, yet neither approach provides a sufficient remedy for the temporal mismatch in 6G-DQC [...]
  § 6.1 Summary of Contributions: This study has introduced and validated “Compute-on-Network Hamiltonian Engineering,” a novel architectural paradigm that bridges the fundamental operational gap between 6G telecommunications and distributed quantum computing. We defined the “Temporal Mismatch Problem” as the primary barrier to this convergence, identifying the incompatibility between microsecond-scale network jitter and nanosecond-scale quantum coherence. To resolve this, we developed the **Q-NET** architecture, which utilizes P4-programmable data planes to offload Hamiltonian control logic to the network edge. Through the implementation of a **Stochastic Hamiltonian Control** framework and the **Coherence-Aware Scheduler (CAS)**, we demonstrated that standard 6G infrastructure can be transformed from a source of decoherence into an active stabilization layer for quantum states. Our results show that this approach effectively synchronizes the stochastic heartbeat of the global network with the deterministic pulse of the quantum processor.
[9] QNFO: In‑Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis | https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g-service-model-quantitative-budgets-and
  Sixth‑generation (6G) network research is investigating the placement of semi‑classical quantum‑control functionality inside the communication fabric, yet designers lack a quantitative budgeting framework that tells whether a Hamiltonian‑engineering service can operate within quantum‑coherence constraints and how much of its control stack survives infrastructure upgrades. This work defines a Hamil
  Full text (https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g-service-model-quantitative-budgets-and), excerpts of its own sections:
  § 1. Introduction: Telecommunication operators and quantum‑network system engineers must decide whether to embed quantum‑control functionality inside the 6G network fabric or to keep it confined to laboratory‑grade hardware. The decision is forced by a concrete physical conflict: the coherence windows of quantum endpoints (typically $10$–$100\,\mu\mathrm{s}$ in current solid‑state devices) and the timing behavior of packet networks (jitter of $100$–$500\,\mu\mathrm{s}$) differ by orders of magnitude. [...]
  § 5. Results: The derived quantitative metrics are summarized in Table 1. $T_{c}=8\,\mu\mathrm{s}$ (Derivation 1), $f=0.5$ (Derivation 2), $N_{c}=125$ (Derivation 3), $\epsilon_{\mathrm{tot}}^{(1)}=1.25\times10^{-3}$ and $F_{\mathrm{proj}}^{(1)}=0.99875$ (Derivation 4), $\epsilon_{\mathrm{tot}}^{(2)}=1.3481\times10^{-3}$ and $F_{\mathrm{proj}}^{(2)}\approx0.99865$ (Derivation 14), $R_{u}=2\times10^{6}\,\mathrm{s^{-1}}$ (Derivation 5), aggregate update rate $1.28\times10^{8}\,\mathrm{s^{-1}}$ (Derivation 6), loop latency $T_{\mathrm{loop}}=1.8\times10^{-4}\,\mathrm{s}$ (Derivation 9), coherence fraction $\eta=0.18$ (Derivation 10), control‑plane payload $B_{\mathrm{cycle}}=6.4\times10^{4}\,\mathrm{bits}$ (Derivation 11), reuse ratio $\rho=0.5$ (Derivation 12), re‑qualification effort $E_{\mathrm{req}}=24$ person‑weeks (Derivation 13), and minimum coherence $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$ (Derivation 16). All values are obtained analytically from the assumptions listed in Section 4.
  § 6. Discussion: The analytical framework presented in Sections 4–5 rests on a set of simplifying assumptions that delimit the validity of the architectural conclusions; recognizing these limits is essential before any deployment decision. **Linear error‑accumulation model is a simplifying approximation.** The derivations in Section 4 treat per‑cycle fractional errors as independent and additive (Derivation 4), which follows directly from the first‑order model introduced in Section 3.2. Reference [5] shows that higher‑order Magnus‑expansion terms can contribute non‑negligible commutator errors, and Derivation 14 explicitly adds a second‑order term $\epsilon_{2}=9.81\times10^{-5}$. Nevertheless, the linear model may under‑estimate coherent error growth when pulse imperfections correlate across cycles. **Constant per‑cycle error $\epsilon_{c}$ assumes perfect pulse synthesis.** The budget uses a fixed $\epsilon_{c}=10^{-5}$ (A5). In practice, pulse‑shaping hardware and calibration drift can cause cycle‑to‑cycle variations. [...]
  § 11. Conclusion: The reframed in‑network Hamiltonian engineering service provides a transparent budgeting framework that links microsecond‑scale cycle design, per‑cycle error tolerances, coherence‑window sizing, and actuation rates. Under the explicit assumptions detailed in Sections 4–5, the analysis demonstrates that a cycle time of $8\,\mu\mathrm{s}$ and a per‑cycle error budget of $10^{-5}$ comfortably satisfy the fidelity and latency constraints for millisecond‑scale coherence, while highlighting that current solid‑state devices with $T_{2}^{*}=10$–$100\,\mu\mathrm{s}$ remain outside the closed‑loop feasibility envelope. The re‑entry analysis quantifies the portable fraction of the control stack ($\rho=0.5$) and the associated re‑qualification effort (24 person‑weeks), offering a concrete metric for infrastructure evolution planning. [...]
[10] QNFO: Stability Compiler | https://papers.qnfo.org/papers/stability
  The modeling of fundamental entities as zero-dimensional points creates singularities across physics and network engineering. Current regularization methods like renormalization are procedural patches that fail to explain the origin of finite scales. This paper introduces the topological extension framework (TEF), modeling entities as finite-volume stable modes of non-linear evolution equations. W
  Full text (https://papers.qnfo.org/papers/stability), excerpts of its own sections:
  § CONTEXTUAL: PERSISTENCE VIA THE TOPOLOGICAL EXTENSION FRAMEWORK **Author:** Rowan Brad Quni-Gudzinas **Contact:** rowan.quni@outlook.com **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604) **ISNI:** [0000000526456062](https://isni.org/isni/0000000526456062) **URL:** https://papers.qnfo.org/papers **Publication Date:** 2025-11-29 **Version:** 1.0 **Abstract**: The modeling of fundamental entities as zero-dimensional points creates singularities across physics and network engineering. Current regularization methods like renormalization are procedural patches that fail to explain the origin of finite scales. This paper introduces the topological extension framework (TEF), modeling entities as finite-volume stable modes of non-linear evolution equations. We map the screening mechanisms of cosmological chameleon fields to the route flap damping protocols of interdomain routing. The analysis reveals a structural isomorphism where stability is maintained by a conserved topological charge and environmental coupling. [...]
  § 1.1 The Ontological Crisis: The fundamental error pervading standard modeling across physical and information sciences is the axiomatic assumption that density distributions—whether of mass, charge, or routing information—can be effectively modeled as zero-dimensional coordinates. This reductionist approach, while computationally convenient for linear approximations, leads inevitably to the divergence of self-energy integrals, as the density squared approaches infinity when the volume element tends toward zero. Snyder (1947) argued that the assumption of a continuous Euclidean background at all scales is an unjustified extrapolation that results in infinite energy densities in quantum field theory, necessitating the use of subtraction schemes such as renormalization. We posit that this mathematical singularity is not merely a calculational nuisance but a symptom of a deeper ontological failure: the inability of the point-particle model to account for the intrinsic finiteness of physical reality. [...]
  § 1.2 The Emergent Stable Mode: A re-evaluation of ontology, supported by evidence from cosmology to computation, reveals that reality is not composed of static, self-contained objects but is rather a set of persistent, dynamic patterns. Fedorova and Zeitlin (2005) demonstrated that in the quantum domain, entities appear not as pre-existing elements but as metastable localized patterns, or “waveletons,” which are the eigensolutions to the nonlinear kinetic equations governing the system. We assert that “existence” in this context is functionally equivalent to “persistence,” defined by the ability of a mode to maintain its coherence against the dispersive forces of the environment. [...]
  § 4.14 Synthesis of Findings: The cumulative analysis of these diverse domains validates the dynamic-modal ontology. The structural isomorphism between the verified reference objects—from the chameleon field to the network route—confirms that reality is a hierarchy of stable modes, not a collection of static objects. We derive the final conclusion that the “thing” is a low-resolution approximation of the “process,” valid only within the stability basin of the mode. This contrasts sharply with the static worldview of classical physics. We imply a fundamental shift in the scientific paradigm, moving from the study of substance to the study of stability, from the geometry of positions to the topology of relations.