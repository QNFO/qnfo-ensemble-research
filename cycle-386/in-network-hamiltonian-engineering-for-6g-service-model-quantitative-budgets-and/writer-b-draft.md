# In-Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re-Entry Analysis (Revised)

## Abstract

Sixth-generation (6G) network research seeks to embed semi-classical quantum-control functionality within the communication fabric, yet designers lack a quantitative budgeting framework that determines whether a Hamiltonian-engineering service can operate inside quantum-coherence windows and how much of its control stack survives infrastructure upgrades. This revision corrects three quantitative claims of the published version and strengthens the derivations behind them. We define a Hamiltonian Engineering Service (HES) contract, derive a timing and fidelity budget for a node with coherence time $T_{2}=1\,\mathrm{ms}$, engineering-cycle duration $T_{c}=8\,\mu\mathrm{s}$, and per-cycle error budget $\epsilon_{c}=10^{-5}$, and compute $N_{c}=125$ cycles per coherence window, accumulated first-order error $1.25\times10^{-3}$, and a projected end-of-window fidelity $F_{\mathrm{proj}}^{(1)}=0.99875$. Adding a second-order commutator contribution $\epsilon_{2}=9.81\times10^{-5}$ tightens the fidelity projection to $F_{\mathrm{proj}}^{(2)}=0.9986519$; the second-order term reduces fidelity by $9.81\times10^{-5}$ relative to the linear model, not the $1.3\times10^{-4}$ previously stated. The corrected validity condition $\epsilon_{c}\le 0.01\,T_{c}/T_{2}=8\times10^{-5}$ replaces the prior $10^{-4}$ claim, and we show the condition generalizes as $\epsilon_{c}\le 0.01\,T_{c}/T_{2}$ for any $T_{2}$ and $T_{c}$. A closed-loop latency of $1.8\times10^{-4}\,\mathrm{s}$ consumes $\eta=0.18$ of the coherence window, yielding a minimum coherence $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$; for the $10$–$100\,\mu\mathrm{s}$ windows of current solid-state hardware the loop budget fails, leaving only feed-forward operation viable. A re-entry reuse ratio $\rho=0.5$ (bounds $0.5$–$0.583$) and a projected re-qualification effort of $24$ person-weeks (range $12$–$48$) are derived. All numbers follow analytically from explicitly labeled assumptions; no empirical measurement is claimed.

## 1. Introduction

Telecommunication operators and quantum-network system engineers must decide whether to embed quantum-control functionality inside the 6G network fabric or to keep it confined to laboratory-grade hardware. The decision is forced by a concrete physical conflict: the coherence windows of quantum endpoints (typically $10$–$100\,\mu\mathrm{s}$ in current solid-state devices) and the timing behavior of packet networks (jitter of $100$–$500\,\mu\mathrm{s}$) differ by orders of magnitude [8]. Embedding control promises tighter integration with quantum-secure services but raises two engineering questions: (i) can a control cycle executed through network elements close within a quantum coherence window, and at what fidelity and actuation cost? (ii) when the underlying 6G infrastructure is upgraded, can the control stack be re-entered—carried across generations—without a full redesign? A wrong answer either strands capital in control hardware that cannot meet quantum timing, or forces every quantum service to remain a bespoke laboratory installation. If the quantitative budgets derived here hold, network designers can provision microsecond-scale timing, per-endpoint actuation rates of $2\times10^{6}\,\mathrm{s^{-1}}$, and a modest re-qualification effort, thereby enabling a viable path to in-network quantum control; if they fail, the control function must remain hardware-adjacent and the network reverts to transport-only.

This paper is a post-publication revision of the predecessor service-model paper [9]. Three quantitative claims in the published version were reported as errors, and each is checked here against the paper's own derivations and sources. All three errors are confirmed and corrected:

1. The published Section 6 stated that the architectural conclusion "follows whenever $T_{2}$ is in the millisecond range and $\epsilon_{c}$ is at or below $10^{-4}$." Substituting $\epsilon_{c}=10^{-4}$ into the accumulation model gives $\epsilon_{\mathrm{tot}}^{(1)}=125\times10^{-4}=1.25\times10^{-2}>0.01$, so the claim fails; the correct bound is $\epsilon_{c}\le 0.01\,T_{c}/T_{2}=8\times10^{-5}$ (Section 4, Derivations 8 and 8b).
2. The published Section 7 stated the structural relation $N_{c}=T_{2}/T_{c}$ and $\epsilon_{\mathrm{tot}}=N_{c}\,\epsilon_{c}$ "holds for any inputs," which is correct as far as it goes, but the accompanying threshold $\epsilon_{c}\le 0.01\,T_{c}/T_{2}$ was misquoted as $\epsilon_{c}\le 10^{-4}$; the general condition is restated and derived here (Section 4, Derivation 8b).
3. The published Section 6.1 stated that "the second-order term reduces the fidelity by roughly $1.3\times10^{-4}$ relative to the linear model." The actual reduction is $F_{\mathrm{proj}}^{(1)}-F_{\mathrm{proj}}^{(2)}=0.99875-0.9986519=9.81\times10^{-5}$, which equals $\epsilon_{2}$ by construction; the $1.3\times10^{-4}$ figure conflated the total second-order error $\epsilon_{\mathrm{tot}}^{(2)}=1.3481\times10^{-3}$ with the increment (Section 4, Derivation 14b).

The contributions of this work are:
1. A corrected and generalized validity condition $\epsilon_{c}\le 0.01\,T_{c}/T_{2}$, giving $8\times10^{-5}$ at the nominal cycle parameters and replacing the predecessor's $10^{-4}$ claim (Section 4, Derivations 8 and 8b).
2. A service model and quantitative timing/fidelity budget for the Hamiltonian Engineering Service, including a second-order commutator correction and an uncertainty propagation, yielding $F_{\mathrm{proj}}^{(2)}=0.9986519$ at nominal parameters, with the second-order increment explicitly computed as $9.81\times10^{-5}$ (Sections 3.1–3.2; computed in Section 4, Derivations 1–5, 14, 14b, 15).
3. A closed-loop latency, jitter, and re-entry analysis, including a twelve-component inventory giving $\rho=0.5$ (bounds $0.5$–$0.583$), a projected re-qualification effort of $24$ person-weeks (range $12$–$48$), a minimum-coherence condition $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$, and a jitter budget $J\le 0.2\,T_{c}=1.6\,\mu\mathrm{s}$ that current packet networks violate (Sections 3.3 and 4, Derivations 7, 9–13, 16–17, 19).
4. A discussion of model limitations, falsification conditions, and open research questions (Section 6).

## 2. Background and Related Work

**Semi-classical quantum control.** Reference [1] outlines strategies for using a semi-classical controller—sensors and actuators that interact with the quantum system but accept classical input and return classical information—to solve problems such as quantum state or process engineering and optimization of observables. Its control-system model places the controller at the interface between the quantum and classical worlds, which is exactly the boundary the HES contract formalizes: the in-network controller $C_{n}$ is a classical device issuing settings to quantum hardware. Reference [1] also distinguishes closed-loop learning techniques, which involve repeated experiments on many copies of the system, from real-time quantum feedback control, which relies on continuous observation of the same system via weak measurements. This distinction maps directly onto the feed-forward versus closed-loop split derived in Section 4: with current hardware coherence windows, only the feed-forward mode survives, and the closed-loop learning mode of [1]—which tolerates latencies far larger than a single coherence window because it operates across many repetitions—is the natural fallback.

**Higher-order pulse-sequence design.** Reference [5] introduces a framework for designing Hamiltonian-engineering pulse sequences that systematically accounts for higher-order contributions to the Floquet–Magnus expansion, and shows that many higher-order decoupling conditions retain simple algebraic interpretations when the sequence has suitable structure. Its decoupling-rule table gives, for each pair of interaction types, an algebraic condition for ideal pulses, a finite-pulse correction of order $(2\tau_{p}/\pi)^{2}$, and a cancellation condition; its DROID-R2D2 sequence reduces residual first-order cross terms relative to the earlier DROID sequence, and adapts to Hamiltonian engineering by tuning frame durations to produce an XXZ interaction with tunable coefficient $\lambda$. This work uses that framework as the physical basis for introducing a second-order error term $\epsilon_{2}$ (Derivation 14): the finite-pulse corrections tabulated in [5] are precisely the class of commutator contributions that the linear accumulation model of Section 3.2 omits.

**Temporal mismatch in 6G-DQC.** Reference [8] quantifies the central obstacle: transverse coherence times $T_{2}^{*}$ of $10$ to $100\,\mu\mathrm{s}$ in current solid-state hardware, against packet delay variations (jitter) of $100$ to $500\,\mu\mathrm{s}$ under typical load in 6G networks, creating what it calls a "synchronization void" in which classical control signals arrive after the target quantum state has decohered. Reference [8] further proposes the Q-NET architecture, which uses P4-programmable data planes to offload Hamiltonian control logic to the network edge, together with a Coherence-Aware Scheduler. The present paper takes the numbers from [8] as hardware inputs (Derivations 7, 17, 19) but treats the architectural claim—that standard 6G infrastructure can become an active stabilization layer—as a hypothesis to be tested against explicit budgets rather than an established result.

**Original service-model paper.** The predecessor paper [9] defined the HES service model, the derivation structure, and the results table reproduced and corrected here: $T_{c}=8\,\mu\mathrm{s}$, $N_{c}=125$, $F_{\mathrm{proj}}^{(1)}=0.99875$, $F_{\mathrm{proj}}^{(2)}=0.9986519$, $T_{\mathrm{loop}}=1.8\times10^{-4}\,\mathrm{s}$, $\eta=0.18$, $\rho=0.5$, $E_{\mathrm{req}}=24$ person-weeks, and $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$. Its Discussion already flagged that the linear model may under-estimate coherent error growth when pulse imperfections correlate across cycles; this revision keeps that caveat and corrects the three quantitative errors listed in Section 1.

**Systematic engineering of web-based services.** Reference [3] defines Web Engineering as the application of systematic, disciplined, and quantifiable approaches to the development, operation, and maintenance of web-based applications, and frames it as both a pro-active approach and a growing collection of theoretical and empirical research. That definition supplies the methodological standard the HES service model attempts to meet: every budget in Section 4 is quantifiable and traceable to a labeled assumption, in the same spirit that [3] demands for web applications.

**Cognitive biases in software projects.** Reference [4] identifies systematic errors introduced by human cognitive biases as one source of software project challenges and failures, and notes that investigation of such biases has only recently gained popularity in software engineering research. This motivates a failure mode discussed in Section 6: a specification template for the HES library $\mathcal{L}$ that is silently mismatched to the actual hardware parameters is a cognitive-bias failure of exactly the kind [4] catalogues, and the machine-checkable applicability predicates of Section 3.1 are the proposed mitigation.

**Generative-AI-driven software engineering.** Reference [2] surveys generative-AI tools that automatically synthesize, repair, refactor, and explain code and generate test cases, with well over one hundred code-synthesis models published, and argues that their trustworthiness will improve when models are trained on dynamic (runtime) as well as static aspects of software. It further argues that adoption of any new technology depends on large-scale test-driven experimentation with stimulus-response data structures. Both points inform the view of the HES library $\mathcal{L}$ as an automatically generated, version-controlled repository whose templates must be validated by test-driven experiments before deployment, not merely by static inspection.

**Benchmarking infrastructure.** Reference [6] documents that current benchmarks for code-capable language models focus on narrow tasks and single metrics—hiding gaps in robustness, interpretability, fairness, efficiency, and real-world usability—and proposes the BEHELM infrastructure for holistic, multi-dimensional evaluation with standardized data-engineering pipelines. The $5\%$ relative uncertainty assigned to $\epsilon_{c}$ in this paper (Assumption A18, Derivation 15) is a single-metric uncertainty treatment of exactly the kind [6] criticizes; extending uncertainty quantification to timing jitter and component portability, in the multi-dimensional style of BEHELM, is listed as an open question in Section 6.

**AI-driven software engineering outlook.** Reference [7] envisions a symbiotic partnership between human developers and AI systems, including an always-active AI maintenance phase that monitors external sources to proactively gather issues and improvement opportunities, while cautioning against over-reliance on AI and insisting that human judgment remains indispensable for critically assessing AI-generated artifacts. This supports the maintenance model for the HES library in Section 7: automated template generation and verification with mandatory human review of applicability predicates, because an unreviewed machine-generated predicate that mis-bounds $\epsilon_{c}$ would reproduce precisely the $10^{-4}$ error corrected in this revision.

**Stability and persistence across environments.** Reference [10] introduces the topological extension framework, in which entities are modeled as finite-volume stable modes of non-linear evolution equations, and defines persistence as the ability of a mode to maintain its coherence against the dispersive forces of the environment; it derives that a "thing" is a low-resolution approximation of a "process," valid only within the stability basin of the mode. This framing is used in Section 6 to interpret the re-entry analysis: the HES stack persists across infrastructure generations exactly to the degree that its components decouple from generation-specific environmental parameters, which is what the portability criterion of Section 3.3 formalizes.

## 3. Methods

### 3.1 Service model

We define a network service, the Hamiltonian Engineering Service (HES), with the following contract. A quantum endpoint $E_{q}$ (a memory, transducer, or QKD node) exposes: (i) its natural Hamiltonian parameters $H_{0}(\theta)$, where $\theta$ is a vector of slowly drifting device parameters; (ii) a coherence time $T_{2}$; and (iii) a pulse-actuation interface accepting control waveforms with minimum pulse width $\tau_{p}$. An in-network controller $C_{n}$ (hosted on an edge node or smart network interface card) exposes: (i) a sequence-template library $\mathcal{L}$, each template $L_{k}$ being a compiled decoupling or recoupling sequence of the kind systematized in [5]; (ii) a scheduler that aligns cycle boundaries with network timing signals; and (iii) a verification module that checks the template's applicability conditions against the reported $\theta$, with the conditions expressed as machine-checkable algebraic predicates in the spirit of the decoupling-rule tables of [5] and the bias-resistant design stance of [4].

The service-level objective is an effective-Hamiltonian error tolerance:
$$
\bigl\|\bar{H} - H_{\mathrm{eff}}\bigr\| \le \epsilon_{c}\,\|H_{0}\|,
$$
where $\bar{H}$ is the cycle-averaged Hamiltonian and $\epsilon_{c}$ is the per-cycle relative error budget. This contract follows the semi-classical control model of [1], in which a classical controller drives quantum hardware through classical input channels.

### 3.2 Timing and fidelity model

Each cycle consists of $n_{p}$ pulses of width $\tau_{p}$ separated by idle intervals, so
$$
T_{c}=n_{p}(\tau_{p}+\tau_{i}),\qquad
f=\frac{n_{p}\tau_{p}}{T_{c}}=\frac{\tau_{p}}{\tau_{p}+\tau_{i}},
$$
with $f$ the actuation duty factor. The controller must issue actuation updates at rate $R_{u}=1/\tau_{p}$ per endpoint; a node hosting $K$ endpoints presents an aggregate update rate $K\,R_{u}$.

We adopt a first-order accumulation model in which per-cycle fractional error contributions add linearly over $N_{c}$ cycles within one coherence window:
$$
N_{c}=\Bigl\lfloor\frac{T_{2}}{T_{c}}\Bigr\rfloor,\qquad
\epsilon_{\mathrm{tot}}^{(1)}=N_{c}\,\epsilon_{c},\qquad
F_{\mathrm{proj}}^{(1)}\approx1-\epsilon_{\mathrm{tot}}^{(1)}.
$$
A second-order commutator contribution $\epsilon_{2}$ is introduced as a projection (Assumption A17) motivated by the finite-pulse corrections of the Floquet–Magnus framework of [5]. The total projected error is then
$$
\epsilon_{\mathrm{tot}}^{(2)}=\epsilon_{\mathrm{tot}}^{(1)}+\epsilon_{2},\qquad
F_{\mathrm{proj}}^{(2)}\approx1-\epsilon_{\mathrm{tot}}^{(2)}.
$$
Uncertainty on $\epsilon_{c}$ is modeled as a $5\%$ relative standard deviation (Assumption A18), yielding an uncertainty band on $\epsilon_{\mathrm{tot}}^{(1)}$ and $F_{\mathrm{proj}}^{(1)}$ (Derivation 15).

### 3.3 Closed-loop latency, jitter, and re-entry models

We model one in-network feedback cycle as four sequential stages:
$$
T_{\mathrm{loop}}=T_{s}+T_{p}+T_{c}'+T_{a},
$$
where $T_{s}$ is the sensing/measurement interval, $T_{p}$ the packet-transport latency, $T_{c}'$ the compute time for the control update, and $T_{a}$ the actuation setup time. Re-entry is physically meaningful only if the loop closes within the coherence window:
$$
\frac{T_{\mathrm{loop}}}{T_{2}}\le\eta_{\mathrm{max}},
$$
with $\eta_{\mathrm{max}}=0.2$ a design margin. Cycle alignment additionally requires timing jitter $J$ to remain a bounded fraction of the cycle period; we require $J\le 0.2\,T_{c}$ (Derivation 19), so that no more than one fifth of a cycle period is consumed by stochastic arrival spread.

For re-entry, let the HES stack consist of $N_{\mathrm{tot}}$ components partitioned into a physics-facing layer $\mathcal{P}$ and an infrastructure-facing layer $\mathcal{I}$. The re-entry reuse ratio is
$$
\rho=\frac{N_{\mathrm{reuse}}}{N_{\mathrm{tot}}},\qquad
N_{\mathrm{reuse}}=|\mathcal{P}_{\mathrm{portable}}|+|\mathcal{I}_{\mathrm{portable}}|,
$$
where a component is portable if its specification does not reference generation-specific infrastructure parameters. The inventory is enumerated explicitly in Section 4 so that $\rho$ is auditable. Re-qualification effort is modeled as linear in the number of non-portable components:
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}}),
$$
with $e$ a per-component effort assumption (Assumption A16).

### 3.4 Method status and correction audit

The method of this paper is analytical derivation from labeled assumptions, together with a correction audit of the predecessor's derivations [9] against the model of Sections 3.1–3.3 and against the hardware parameters reported in [8]. Each reported error is tested by substituting the published claim into the paper's own equations and comparing against the stated thresholds; the audit results appear as Derivations 8b and 14b. No hardware experiment, simulation, survey, or expert review was performed; a study that would test the results is proposed in Section 7.

## 4. Analysis

All inputs are design assumptions (A1–A19) unless otherwise noted.

**Inputs (timing/fidelity model).**
- $T_{2}=1\,\mathrm{ms}=10^{-3}\,\mathrm{s}$ (A1).
- $\tau_{p}=0.5\,\mu\mathrm{s}=5\times10^{-7}\,\mathrm{s}$ (A2).
- $\tau_{i}=0.5\,\mu\mathrm{s}=5\times10^{-7}\,\mathrm{s}$ (A3).
- $n_{p}=8$ (A4).
- $\epsilon_{c}=10^{-5}$ (A5).
- $K=64$ endpoints per node (A6).

**Derivation 1 — cycle time.**
$$
T_{c}=n_{p}(\tau_{p}+\tau_{i})
=8\times(5\times10^{-7}+5\times10^{-7})\,\mathrm{s}
=8\times10^{-6}\,\mathrm{s}=8\,\mu\mathrm{s}.
$$

**Derivation 2 — duty factor.**
$$
f=\frac{\tau_{p}}{\tau_{p}+\tau_{i}}
=\frac{5\times10^{-7}}{10^{-6}}=0.5.
$$

**Derivation 3 — cycles per coherence window.**
$$
\frac{T_{2}}{T_{c}}=\frac{10^{-3}}{8\times10^{-6}}=125,\qquad
N_{c}=\lfloor125\rfloor=125.
$$

**Derivation 4 — accumulated first-order error and projected fidelity.**
$$
\epsilon_{\mathrm{tot}}^{(1)}=N_{c}\,\epsilon_{c}=125\times10^{-5}=1.25\times10^{-3},
$$
$$
F_{\mathrm{proj}}^{(1)}\approx1-1.25\times10^{-3}=0.99875.
$$

**Derivation 5 — actuation update rate per endpoint.**
$$
R_{u}=\frac{1}{\tau_{p}}=\frac{1}{5\times10^{-7}\,\mathrm{s}}=2\times10^{6}\,\mathrm{s^{-1}}.
$$

**Derivation 6 — aggregate update rate per node.**
$$
K\,R_{u}=64\times2\times10^{6}\,\mathrm{s^{-1}}=1.28\times10^{8}\,\mathrm{s^{-1}}.
$$

**Derivation 7 — sensitivity to $T_{2}$.**
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
For this degraded coherence the loop latency (Derivation 9) exceeds $T_{2}'$, making latency the binding constraint rather than fidelity.

**Derivation 8 — error-budget headroom.**
To keep $\epsilon_{\mathrm{tot}}^{(1)}\le 0.01$ with $N_{c}=125$,
$$
\epsilon_{c}^{\mathrm{max}}=\frac{0.01}{125}=8\times10^{-5},
$$
so the chosen $\epsilon_{c}=10^{-5}$ carries a headroom factor of $8$.

**Derivation 8b — correction of the predecessor's validity claim.**
Testing the predecessor's claim $\epsilon_{c}\le 10^{-4}$:
$$
\epsilon_{\mathrm{tot}}^{(1)}=125\times10^{-4}=1.25\times10^{-2}>0.01,
$$
so the claim fails: a per-cycle error of $10^{-4}$ would drive the end-of-window fidelity to $1-1.25\times10^{-2}=0.9875$, below the $0.99$ threshold. Enforcing $N_{c}\,\epsilon_{c}\le 0.01$ with $N_{c}=\lfloor T_{2}/T_{c}\rfloor$ yields the general condition
$$
\epsilon_{c}\le\frac{0.01\,T_{c}}{T_{2}}.
$$
For $T_{2}=1\,\mathrm{ms}$ and $T_{c}=8\,\mu\mathrm{s}$ this gives $\epsilon_{c}\le 8\times10^{-5}$. Because the condition is expressed in $T_{c}$ and $T_{2}$ alone, it holds for any cycle duration and coherence time in the millisecond range, not only at the nominal point: e.g., for $T_{2}=2\,\mathrm{ms}$ and the same $T_{c}$ it tightens to $\epsilon_{c}\le 4\times10^{-5}$, and for $T_{2}=0.5\,\mathrm{ms}$ it relaxes to $\epsilon_{c}\le 1.6\times10^{-4}$. The architectural conclusion therefore follows whenever $T_{2}$ is in the millisecond range and $\epsilon_{c}\le 0.01\,T_{c}/T_{2}$; the predecessor's fixed $10^{-4}$ figure was correct only for $T_{2}=0.8\,\mathrm{ms}$ at $T_{c}=8\,\mu\mathrm{s}$, not for the nominal $T_{2}=1\,\mathrm{ms}$.

**Inputs (closed-loop and re-entry models).**
- $T_{s}=1.0\times10^{-4}\,\mathrm{s}$ (A7).
- $T_{p}=2.0\times10^{-5}\,\mathrm{s}$ (A8).
- $T_{c}'=5.0\times10^{-5}\,\mathrm{s}$ (A9).
- $T_{a}=1.0\times10^{-5}\,\mathrm{s}$ (A10).
- $W=64$ bits per qubit per control word (A11).
- $N_{q}=1000$ qubits (A12).
- $R_{\mathrm{link}}=1.0\times10^{11}\,\mathrm{bit/s}$ (A13).
- $\eta_{\mathrm{max}}=0.2$ (A14).

**Derivation 9 — loop latency.**
$$
T_{\mathrm{loop}}=1.0\times10^{-4}+2.0\times10^{-5}+5.0\times10^{-5}+1.0\times10^{-5}=1.8\times10^{-4}\,\mathrm{s}.
$$

**Derivation 10 — coherence fraction consumed.**
$$
\eta=\frac{T_{\mathrm{loop}}}{T_{2}}=\frac{1.8\times10^{-4}}{1.0\times10^{-3}}=0.18\le\eta_{\mathrm{max}}=0.2,
$$
margin $=0.02$, headroom factor $=0.2/0.18\approx1.111$.

**Derivation 11 — control-plane bandwidth per cycle.**
$$
B_{\mathrm{cycle}}=W\cdot N_{q}=64\times1000=6.4\times10^{4}\,\mathrm{bits},
$$
$$
\tau_{\mathrm{tx}}=\frac{B_{\mathrm{cycle}}}{R_{\mathrm{link}}}=\frac{6.4\times10^{4}}{1.0\times10^{11}}=6.4\times10^{-7}\,\mathrm{s},
$$
$$
\frac{\tau_{\mathrm{tx}}}{T_{\mathrm{loop}}}=\frac{6.4\times10^{-7}}{1.8\times10^{-4}}\approx3.56\times10^{-3},
$$
i.e. $0.36\%$ of the loop budget. Transport bandwidth is therefore not the binding constraint; the stage latencies $T_{s}$ and $T_{c}'$ dominate the loop.

**Derivation 12 — re-entry reuse ratio.** Inventory of twelve components (Assumption A15) is:

```
 1  Hamiltonian target specification      P  portable
 2  Pulse-sequence library                P  portable
 3  Observable-optimization objective     P  portable
 4  Control-update algorithm              P  portable
 5  Control-word encoding                 P  portable
 6  Timing distribution service           I  not portable
 7  Transport/queueing configuration      I  not portable
 8  In-network compute node image         I  not portable
 9  Sensor/actuator drivers               I  not portable
10  Latency budget manifest               I  not portable
11  Qualification test suite              I  not portable (conservative)
12  Monitoring/telemetry schema           I  portable
```

Portable count $N_{\mathrm{reuse}}=6$, total $N_{\mathrm{tot}}=12$, therefore
$$
\rho=\frac{6}{12}=0.5.
$$
Counting component 11 as portable would raise $\rho$ to $7/12\approx0.583$; we report the conservative $\rho=0.5$ with bounds $0.5\le\rho\le0.583$.

**Derivation 13 — re-qualification effort (projection).**
Assume $e=4$ person-weeks per non-portable component (A16):
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}})=4\times6=24\ \text{person-weeks}.
$$
Linear uncertainty in $e$ yields $E_{\mathrm{req}}\in[12,48]$ person-weeks for $e\in[2,8]$.

**Derivation 14 — second-order commutator error (projection).**
Assume a second-order error contribution $\epsilon_{2}=9.81\times10^{-5}$ (A17). Then
$$
\epsilon_{\mathrm{tot}}^{(2)}=\epsilon_{\mathrm{tot}}^{(1)}+\epsilon_{2}=1.25\times10^{-3}+9.81\times10^{-5}=1.3481\times10^{-3},
$$
$$
F_{\mathrm{proj}}^{(2)}\approx1-1.3481\times10^{-3}=0.9986519.
$$

**Derivation 14b — correction of the second-order increment claim.**
The published version stated that the second-order term reduces the fidelity by roughly $1.3\times10^{-4}$ relative to the linear model. The actual reduction is
$$
\Delta F=F_{\mathrm{proj}}^{(1)}-F_{\mathrm{proj}}^{(2)}=0.99875-0.9986519=9.81\times10^{-5},
$$
which equals $\epsilon_{2}$ by construction of Derivation 14. The published figure apparently conflated the total second-order error $\epsilon_{\mathrm{tot}}^{(2)}=1.3481\times10^{-3}$ with the increment attributable to the second-order term alone; the correct increment is $9.81\times10^{-5}$, about $25\%$ smaller than the stated $1.3\times10^{-4}$.

**Derivation 15 — uncertainty propagation (projection).**
Assume a $5\%$ relative standard deviation on $\epsilon_{c}$ (A18). The standard deviation on $\epsilon_{\mathrm{tot}}^{(1)}$ is
$$
\sigma_{\epsilon}=N_{c