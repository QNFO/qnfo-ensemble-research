# In‑Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis (Revised)

## Abstract

Sixth‑generation (6G) network research is investigating the placement of semi‑classical quantum‑control functionality inside the communication fabric, yet designers lack a quantitative budgeting framework that tells whether a Hamiltonian‑engineering service can operate within quantum‑coherence constraints and how much of its control stack survives infrastructure upgrades. The predecessor version of this paper overstated the validity range of its central architectural conclusion, claiming compatibility for per‑cycle errors up to $10^{-4}$ and mis‑stating the size of the second‑order fidelity correction. This revision defines a Hamiltonian Engineering Service (HES) contract, derives a timing and fidelity budget for a node with coherence time $T_{2}=1\,\mathrm{ms}$, engineering‑cycle duration $T_{c}=8\,\mu\mathrm{s}$, and per‑cycle error budget $\epsilon_{c}=10^{-5}$, and computes $N_{c}=125$ cycles per coherence window, accumulated first‑order error $1.25\times10^{-3}$, and a projected end‑of‑window fidelity $F_{\mathrm{proj}}^{(1)}=0.99875$. With a second‑order commutator contribution of $9.81\times10^{-5}$ (projection), the fidelity tightens to $F_{\mathrm{proj}}^{(2)}=0.9986519$; the second‑order term reduces fidelity by $9.81\times10^{-5}$ relative to the linear model, correcting the predecessor's $\approx1.3\times10^{-4}$ figure. The architectural conclusion that microsecond‑scale cycles are compatible with millisecond‑scale coherence holds only when $\epsilon_{c}\le0.01\,T_{c}/T_{2}=8\times10^{-5}$, replacing the earlier $10^{-4}$ claim. A closed‑loop latency of $1.8\times10^{-4}\,\mathrm{s}$ consumes $\eta=0.18$ of the coherence window, giving $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$; for the $10$–$100\,\mu\mathrm{s}$ windows of current solid‑state hardware the loop budget fails and only feed‑forward operation remains. A re‑entry reuse ratio $\rho=0.5$ (bounds $0.5$–$0.583$) and a projected re‑qualification effort of $24$ person‑weeks (range $12$–$48$) are derived. All numbers follow analytically from labeled assumptions; no empirical measurement is claimed.

## 1. Introduction

Telecommunication operators and quantum‑network system engineers must decide whether to embed quantum‑control functionality inside the 6G network fabric or to keep it confined to laboratory‑grade hardware. The decision is forced by a concrete physical conflict: the coherence windows of quantum endpoints (typically $10$–$100\,\mu\mathrm{s}$ in current solid‑state devices [8]) and the timing behavior of packet networks (jitter of $100$–$500\,\mu\mathrm{s}$ under typical load [8]) differ by orders of magnitude. Embedding control promises tighter integration with quantum‑secure services but raises two engineering questions: (i) can a control cycle executed through network elements close within a quantum coherence window, and at what fidelity and actuation cost? (ii) when the underlying 6G infrastructure is upgraded, can the control stack be re‑entered—carried across generations—without a full redesign? A wrong answer either strands capital in control hardware that cannot meet quantum timing, or forces every quantum service to remain a bespoke laboratory installation. If the quantitative budgets derived here hold, network designers can provision microsecond‑scale timing, per‑endpoint actuation rates of $2\times10^{6}\,\mathrm{s^{-1}}$, and a modest re‑qualification effort, giving a viable path to in‑network quantum control; if they fail, the control function must remain hardware‑adjacent and the network reverts to transport‑only.

This paper is a post‑publication revision of the predecessor analysis [9]. Three defects in that version are corrected here, each re‑derived from the paper's own model:

1. The predecessor's Section 6 asserted that the architectural conclusion "follows whenever $T_{2}$ is in the millisecond range and $\epsilon_{c}$ is at or below $10^{-4}$." Testing that claim against the accumulation model (Derivation 8b below) shows it fails: at $\epsilon_{c}=10^{-4}$ the accumulated error is $1.25\times10^{-2}$, breaching the $0.01$ fidelity threshold. The corrected validity condition is $\epsilon_{c}\le0.01\,T_{c}/T_{2}$, giving $8\times10^{-5}$ at nominal parameters.
2. The predecessor's Section 7 stated the structural relationship $N_{c}=T_{2}/T_{c}$ and $\epsilon_{\mathrm{tot}}=N_{c}\,\epsilon_{c}$ together with the incorrect threshold. The structural relationship is correct and is retained; the threshold attached to it is corrected to $\epsilon_{c}\le0.01\,T_{c}/T_{2}$ (Derivation 8b).
3. The predecessor's Section 6.1 stated that "the second‑order term reduces the fidelity by roughly $1.3\times10^{-4}$ relative to the linear model." The derived reduction equals the second‑order contribution itself, $\epsilon_{2}=9.81\times10^{-5}$ (Derivation 14); the $1.3\times10^{-4}$ figure is corrected accordingly.

The contributions of this revision are:

- A corrected and generalized validity condition $\epsilon_{c}\le0.01\,T_{c}/T_{2}$, giving $8\times10^{-5}$ at the nominal cycle parameters and replacing the predecessor's $10^{-4}$ claim, with a sensitivity table over $T_{2}$ from $0.1$ to $10\,\mathrm{ms}$ (Section 4, Derivations 8, 8b, and 18).
- A service model and quantitative timing/fidelity budget for the Hamiltonian Engineering Service, including a second‑order commutator correction (projection) and an uncertainty propagation, yielding $F_{\mathrm{proj}}^{(2)}=0.9986519$ at nominal parameters and a corrected second‑order reduction of $9.81\times10^{-5}$ (Sections 3.1–3.2; computed in Section 4, Derivations 1–5, 14–15).
- A closed‑loop latency, bandwidth, jitter, and re‑entry analysis, including a twelve‑component inventory giving $\rho=0.5$ (bounds $0.5$–$0.583$), a projected re‑qualification effort of $24$ person‑weeks (range $12$–$48$), a minimum‑coherence condition $T_{2}^{\min}=9\times10^{-4}\,\mathrm{s}$, and a jitter budget $J\le0.2\,T_{c}=1.6\,\mu\mathrm{s}$ that current packet networks violate by more than an order of magnitude (Sections 3.3 and 4, Derivations 7, 9–13, 16–17, 19).
- A discussion of model limitations, falsification conditions, and open research questions (Section 6).

## 2. Background and Related Work

**Semi‑classical quantum control.** Reference [1] outlines strategies that use a semi‑classical controller—classical sensors and actuators that interact with the quantum system but accept classical input and return classical information—to engineer quantum Hamiltonians for state and process engineering and observable optimization. That interface model is exactly the situation of an in‑network controller driving a quantum endpoint, and it supplies the control‑system template for the HES contract in Section 3.1. Reference [1] also distinguishes closed‑loop learning, which operates by repeated experiments on many copies of the system, from real‑time quantum feedback control, which relies on continuous observation of the same system; this distinction maps directly onto the feed‑forward versus closed‑loop operating modes analyzed in Section 4, because a network‑hosted controller with loop latency comparable to $T_{2}$ can only support the repeated‑experiment mode, not real‑time feedback.

**Higher‑order pulse‑sequence design.** Reference [5] introduces a framework for designing Hamiltonian‑engineering pulse sequences that systematically accounts for higher‑order contributions to the Floquet–Magnus expansion, and shows that despite the naive complexity of higher‑order commutators, the resulting decoupling conditions admit simple algebraic forms, tabulated as ideal‑pulse and finite‑pulse‑correction conditions. The framework's sequence DROID‑R2D2 reduces residual first‑order cross terms relative to the prior best sequence DROID, whose residual errors were dominated by disorder–Heisenberg cross terms. This paper uses that framework in two places: the template library $\mathcal{L}$ stores compiled sequences of the kind [5] systematizes, with applicability predicates modeled on its algebraic decoupling conditions, and the second‑order error term $\epsilon_{2}$ in Derivation 14 is introduced as a projection motivated by its higher‑order analysis.

**Temporal mismatch in 6G‑DQC.** Reference [8] identifies the central obstacle to converging 6G networking with distributed quantum computing as the orders‑of‑magnitude discrepancy between packet dynamics and quantum state evolution: transverse coherence times $T_{2}^{*}$ of $10$–$100\,\mu\mathrm{s}$ in current solid‑state hardware against packet delay variations of $100$–$500\,\mu\mathrm{s}$ under typical load, producing a "synchronization void" in which control signals arrive after decoherence. It proposes the Q‑NET architecture, using P4‑programmable data planes to offload Hamiltonian control logic to the network edge with a Coherence‑Aware Scheduler. This paper adopts [8]'s hardware and jitter figures as the empirical anchors for Derivations 7, 17, and 19, and treats its architectural claim as the hypothesis that the budgets derived here would have to satisfy.

**Original service‑model paper.** Reference [9] presents the initial service model, quantitative budgets, and re‑entry analysis for in‑network Hamiltonian engineering, including the $8\,\mu\mathrm{s}$ cycle, the $125$‑cycle budget, the $1.8\times10^{-4}\,\mathrm{s}$ loop latency, and the $\rho=0.5$ reuse ratio. It also contains the three defects listed in Section 1. This revision re‑derives every baseline number of [9] from labeled assumptions, retains those that survive the re‑derivation, and corrects the validity condition, the attached threshold, and the second‑order reduction figure.

**Systematic engineering of web‑based services.** Reference [3] defines Web Engineering as the application of systematic, disciplined, and quantifiable approaches to the development, operation, and maintenance of web‑based applications. That definition is the methodological standard this paper applies to a quantum‑control network service: the HES contract, the auditable component inventory of Derivation 12, and the labeled‑assumption derivations are all instances of making the service quantifiable in [3]'s sense.

**Cognitive biases in software projects.** Reference [4] systematically maps the literature on cognitive biases in software engineering, identifying systematic human errors as one source of software project challenges and failures. The predecessor's $10^{-4}$ validity claim is a concrete instance of the failure mode [4] documents: a threshold carried over from an earlier draft without re‑checking it against the model it was supposed to follow. Section 6 uses this mapping to motivate machine‑checkable applicability predicates over human‑reviewed prose in the HES verification module.

**Generative‑AI‑driven software engineering.** Reference [2] surveys generative‑AI tools that automatically check, synthesize, and modify software engineering artifacts, noting over a hundred LLM‑based code models published since 2021, and argues that trustworthiness requires models trained on dynamic (run‑time) as well as static aspects of software, supported by large‑scale test‑driven experimentation. This informs the view of the HES library $\mathcal{L}$ as an automatically generated, version‑controlled repository whose templates are validated by executable conformance tests rather than by inspection alone.

**Benchmarking infrastructure.** Reference [6] proposes the BEHELM framework, a comprehensive infrastructure for evaluating code LLMs beyond single accuracy metrics, explicitly covering robustness, interpretability, efficiency, and fairness dimensions that narrow benchmarks hide, and identifies the lack of standardized data‑engineering pipelines as a critical gap. This paper adopts the same evaluation philosophy in a narrower form: a single point estimate of $\epsilon_{c}$ is treated as insufficient, and a $5\%$ relative uncertainty is propagated through the budget (Derivation 15), with the open question of extending the propagation to timing quantities flagged in Section 6.

**AI‑driven software engineering outlook.** Reference [7] presents a vision of a symbiotic partnership between human developers and AI systems across the software life cycle, including an always‑active AI maintenance phase that monitors external sources for issues, while cautioning against over‑reliance on AI and insisting that human judgment remains indispensable for critically assessing AI‑generated artifacts. This shapes the operational model for $\mathcal{L}$ in Section 7: automated template generation and drift monitoring, with human‑gated qualification at each re‑entry event.

**Stability and persistence across environments.** Reference [10] introduces the topological extension framework, in which persistence—defined as the ability of a mode to maintain coherence against the dispersive forces of its environment—is treated as the operative notion of stability, and maps screening mechanisms in physics to route‑damping protocols in interdomain routing via a structural isomorphism. That framing is used in Section 6 to interpret the re‑entry analysis: the HES stack persists across infrastructure generations exactly to the degree that its components decouple from generation‑specific environmental parameters, which is what the portability criterion of Section 3.3 formalizes.

## 3. Methods

### 3.1 Service model

We define a network service, the Hamiltonian Engineering Service (HES), with the following contract. A quantum endpoint $E_{q}$ (a memory, transducer, or QKD node) exposes: (i) its natural Hamiltonian parameters $H_{0}(\theta)$, where $\theta$ is a vector of slowly drifting device parameters; (ii) a coherence time $T_{2}$; and (iii) a pulse‑actuation interface accepting control waveforms with minimum pulse width $\tau_{p}$. An in‑network controller $C_{n}$ (hosted on an edge node or smart network interface card) exposes: (i) a sequence‑template library $\mathcal{L}$, each template $L_{k}$ being a compiled decoupling or recoupling sequence of the kind systematized in [5]; (ii) a scheduler that aligns cycle boundaries with network timing signals; and (iii) a verification module that checks the template's applicability conditions against the reported $\theta$, with the conditions expressed as machine‑checkable algebraic predicates in the spirit of the decoupling‑rule tables of [5] and the bias‑resistant design stance of [4].

The service‑level objective is an effective‑Hamiltonian error tolerance:
$$
\bigl\|\bar{H} - H_{\mathrm{eff}}\bigr\| \le \epsilon_{c}\,\|H_{0}\|,
$$
where $\bar{H}$ is the cycle‑averaged Hamiltonian and $\epsilon_{c}$ is the per‑cycle relative error budget. This contract follows the semi‑classical control model of [1], in which classical actuators drive the quantum system and classical sensors return measurement information across the quantum–classical interface.

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
A second‑order commutator contribution $\epsilon_{2}$ is introduced as a projection (Assumption A17) based on the Floquet–Magnus analysis of [5]. The total projected error is then
$$
\epsilon_{\mathrm{tot}}^{(2)}=\epsilon_{\mathrm{tot}}^{(1)}+\epsilon_{2},\qquad
F_{\mathrm{proj}}^{(2)}\approx1-\epsilon_{\mathrm{tot}}^{(2)}.
$$
Uncertainty on $\epsilon_{c}$ is modeled as a $5\%$ relative standard deviation (Assumption A18), yielding an uncertainty band on $\epsilon_{\mathrm{tot}}^{(1)}$ and $F_{\mathrm{proj}}^{(1)}$ (Derivation 15).

### 3.3 Closed‑loop latency, jitter, and re‑entry models

We model one in‑network feedback cycle as four sequential stages:
$$
T_{\mathrm{loop}}=T_{s}+T_{p}+T_{c}^{\prime}+T_{a},
$$
where $T_{s}$ is the sensing/measurement interval, $T_{p}$ the packet‑transport latency, $T_{c}^{\prime}$ the compute time for the control update, and $T_{a}$ the actuation setup time. Re‑entry is physically meaningful only if the loop closes within the coherence window:
$$
\frac{T_{\mathrm{loop}}}{T_{2}}\le\eta_{\mathrm{max}},
$$
with $\eta_{\mathrm{max}}=0.2$ a design margin. Cycle alignment additionally requires timing jitter $J$ to remain a bounded fraction of the cycle period; we require $J\le0.2\,T_{c}$ (Derivation 19), so that no more than one fifth of a cycle period is consumed by stochastic arrival spread.

For re‑entry, let the HES stack consist of $N_{\mathrm{tot}}$ components partitioned into a physics‑facing layer $\mathcal{P}$ and an infrastructure‑facing layer $\mathcal{I}$. The re‑entry reuse ratio is
$$
\rho=\frac{N_{\mathrm{reuse}}}{N_{\mathrm{tot}}},\qquad
N_{\mathrm{reuse}}=|\mathcal{P}_{\mathrm{portable}}|+|\mathcal{I}_{\mathrm{portable}}|,
$$
where a component is portable if its specification does not reference generation‑specific infrastructure parameters. The inventory is enumerated explicitly in Section 4 so that $\rho$ is auditable. Re‑qualification effort is modeled as linear in the number of non‑portable components:
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}}),
$$
with $e$ a per‑component effort assumption (Assumption A16).

### 3.4 Method status

The method of this paper is analytical derivation from labeled assumptions, together with a correction audit of the predecessor's derivations [9] against the model and against the hardware parameters reported in [8]. No hardware experiment, simulation, survey, or expert review was performed; a study that would test the results is proposed in Section 7.

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

**Derivation 4 — accumulated first‑order error and projected fidelity.**
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

**Derivation 8 — error‑budget headroom.**
To keep $\epsilon_{\mathrm{tot}}^{(1)}\le0.01$ with $N_{c}=125$,
$$
\epsilon_{c}^{\mathrm{max}}=\frac{0.01}{125}=8\times10^{-5},
$$
so the chosen $\epsilon_{c}=10^{-5}$ carries a headroom factor of $8$.

**Derivation 8b — correction of the predecessor's validity claim.**
The predecessor [9] claimed validity for $\epsilon_{c}\le10^{-4}$. Testing that claim:
$$
\epsilon_{\mathrm{tot}}^{(1)}=125\times10^{-4}=1.25\times10^{-2}>0.01,
$$
so the claim fails: at $\epsilon_{c}=10^{-4}$ the projected fidelity $F_{\mathrm{proj}}^{(1)}\approx0.9875$ falls below the $0.99$ threshold. Enforcing $N_{c}\,\epsilon_{c}\le0.01$ with $N_{c}=\lfloor T_{2}/T_{c}\rfloor$ yields the general condition
$$
\epsilon_{c}\le\frac{0.01\,T_{c}}{T_{2}}.
$$
For $T_{2}=1\,\mathrm{ms}$ and $T_{c}=8\,\mu\mathrm{s}$ this gives $\epsilon_{c}\le8\times10^{-5}$. The structural relationship $N_{c}=T_{2}/T_{c}$ and $\epsilon_{\mathrm{