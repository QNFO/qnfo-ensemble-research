# In‑Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis (Revised)

## Abstract

Sixth‑generation (6G) network research is exploring the placement of semi‑classical quantum‑control functionality inside the communication fabric, but designers lack a quantitative budget that tells them whether a Hamiltonian‑engineering service can operate within quantum coherence constraints and how much of its control stack survives an infrastructure upgrade. This revised paper defines a Hamiltonian Engineering Service (HES) contract, derives a timing and fidelity budget for a node with coherence time $T_{2}=1\,\mathrm{ms}$, engineering‑cycle duration $T_{c}=8\,\mu\mathrm{s}$, and per‑cycle error budget $\epsilon_{c}=10^{-5}$, and computes $N_{c}=125$ cycles per coherence window, accumulated error $1.25\times10^{-3}$, and a projected end‑of‑window fidelity $F_{\mathrm{proj}}\approx0.99875$ under a linear accumulation model. A closed‑loop latency of $1.8\times10^{-4}\,\mathrm{s}$ consumes $\eta=0.18$ of the coherence window, and a re‑entry reuse ratio $\rho=0.5$ is obtained for a twelve‑component stack. The revision corrects a published error: the architectural conclusion does not extend to $\epsilon_{c}=10^{-4}$, because $125\times10^{-4}=1.25\times10^{-2}$ exceeds a $0.01$ total‑error target; the valid condition is $\epsilon_{c}\le8\times10^{-5}$ for these cycle parameters. All numbers are derived analytically from explicitly labeled assumptions; no empirical measurement is claimed. The framework gives 6G architects a budgeting structure in which cycle time, per‑cycle error, coherence window, and actuation rate are co‑managed, and identifies timing distribution, not bandwidth, as the binding engineering constraint.

## 1. Introduction

Telecommunication operators and quantum‑network system engineers must decide whether to embed quantum‑control functionality inside the 6G network fabric or to keep it confined to laboratory‑grade hardware. Embedding control promises tighter integration with quantum‑secure services, but it raises two concrete engineering questions: (i) can a control cycle executed through network elements close within a quantum coherence window, and at what fidelity and actuation cost? (ii) when the underlying 6G infrastructure is upgraded, can the control stack be re‑entered—carried across generations—without a full redesign? These questions matter because a wrong answer either strands capital in control hardware that cannot meet quantum timing, or forces every quantum service to remain a bespoke laboratory installation. If the quantitative budgets derived here hold, network designers can provision microsecond‑scale timing, per‑endpoint actuation rates of $2\times10^{6}\,\mathrm{s^{-1}}$, and a modest re‑qualification effort, giving a viable path to in‑network quantum control; if they fail, the control function must stay hardware‑adjacent and the network reverts to transport only.

The predecessor of this paper [9] established the service model and the budget structure. This revision keeps everything that its derivations support and makes three corrections and strengthenings. First, it repairs an error in the predecessor's Discussion: the claim that the architectural conclusion "follows whenever $T_{2}$ is in the millisecond range and $\epsilon_{c}$ is at or below $10^{-4}$" is arithmetically false at the predecessor's own cycle parameters, because $N_{c}\,\epsilon_{c}=125\times10^{-4}=1.25\times10^{-2}$ exceeds the $0.01$ total‑error target used in the predecessor's headroom derivation; the corrected condition, derived in Section 4, is $\epsilon_{c}\le0.01\,T_{c}/T_{2}=8\times10^{-5}$. Second, it grounds the fidelity model in the higher‑order Floquet‑Magnus framework of pulse‑sequence design [5], which shows both why the linear accumulation model is a simplification and what a principled replacement looks like. Third, it replaces the predecessor's generic systems analogies with literature that bears directly on the two hard parts of the problem: the semi‑classical control interface [1] and the verification, benchmarking, and maintenance discipline that a deployed control stack would need [2], [6], [7], with the general lesson that engineering must be systematic, disciplined, and quantifiable [3] and that unexamined human assumptions are a documented source of project failure [4].

The contributions are:

1. A corrected validity condition for the architectural conclusion: the microsecond‑cycle/hardware‑adjacent‑control conclusion holds for $T_{2}=1\,\mathrm{ms}$ and $T_{c}=8\,\mu\mathrm{s}$ only when $\epsilon_{c}\le8\times10^{-5}$, not $10^{-4}$ (derived in Section 4, Derivation 8b).
2. A service model and quantitative timing/fidelity budget for the Hamiltonian Engineering Service, with all sixteen inputs labeled as assumptions (Sections 3.1–3.2, computed in Section 4).
3. A closed‑loop latency, bandwidth, and re‑entry reuse analysis, including a twelve‑component inventory giving $\rho=0.5$ with bounds $0.5\le\rho\le0.583$ (Sections 3.3 and 4).
4. A fidelity‑model critique anchored in higher‑order Floquet‑Magnus pulse‑sequence design [5] and a verification/benchmarking agenda anchored in the software‑engineering literature [2], [6], [7] (Sections 2 and 6).

## 2. Background and Related Work

This section groups the nine works into four strands: the quantum‑control physics that defines what the service must do, the network‑architecture problem that motivates doing it in the fabric, and the software‑engineering discipline that determines whether a deployed control stack can be verified, benchmarked, and maintained.

**Semi‑classical quantum control.** Reference [1] frames quantum control as the manipulation of a quantum system by a controller that accepts classical input and returns classical information—the semi‑classical interface—and notes that the destructive effects of uncontrolled environmental interactions and measurement backaction lead to loss of coherence, which is precisely the constraint our timing budget must respect. The paper distinguishes closed‑loop learning techniques, which involve repeated experiments on many copies of the system, from real‑time quantum feedback control, which relies on continuous observation of the same system [1]. This distinction matters for the HES design: the closed‑loop latency budget of Section 3.3 applies to the real‑time feedback case, and the much looser learning case does not need to fit inside a single coherence window at all. Reference [1] also observes that model‑based techniques are problematic when models of the system are unavailable, which motivates the HES verification module that checks a template's applicability conditions against reported device parameters before use.

**Higher‑order pulse‑sequence design.** Reference [5] introduces a framework for designing Hamiltonian‑engineering pulse sequences that systematically accounts for higher‑order contributions to the Floquet‑Magnus expansion, and finds, contrary to naive expectation, that many higher‑order decoupling conditions retain simple algebraic interpretations such as echo and symmetrization conditions. Using these rules the authors designed sequences—among them DROID‑R2D2—whose residual errors in the effective Hamiltonian are much reduced relative to the prior best sequence DROID, whose significant residual first‑order cross terms between disorder and Heisenberg interactions the same work documents [5]. This is the concrete alternative to the linear error‑accumulation model of Section 3.2: a per‑cycle error budget justified by first‑order averaging can be tightened or replaced by computing the second‑order Floquet‑Magnus terms for the specific sequence family, and the existence of closed‑form second‑order correction terms in [5] shows the computation is tractable. The same work demonstrates a tunable interaction Hamiltonian $H_{XXZ}$ obtained by adjusting frame durations, which is exactly the kind of engineered target an HES template would encode.

**The network‑side problem.** Reference [8] states the temporal mismatch directly: quantum information in solid‑state systems such as superconducting qubits or spin networks decays with a transverse coherence time $T_2^*$ that typically persists for only 10 to 100 microseconds in current hardware generations, while 6G networks exhibit packet delay variations (jitter) in the range of 100 to 500 microseconds under typical load, creating a synchronization void in which control signals subjected to stochastic queuing delays arrive after the target quantum state has decohered [8]. That work proposes the Q‑NET architecture, using P4‑programmable data planes to offload Hamiltonian control logic to the network edge together with a Coherence‑Aware Scheduler, arguing that the network can be transformed from a source of decoherence into an active stabilization layer [8]. Two consequences for this paper follow from [8]'s numbers. First, its $T_2^*$ range of $10$–$100\,\mu\mathrm{s}$ is one to two orders of magnitude below the $T_{2}=1\,\mathrm{ms}$ assumed here; our Derivation 7 therefore evaluates the degraded case $T_{2}'=10^{-4}\,\mathrm{s}$ explicitly, and Section 6 treats the millisecond assumption as the load‑bearing one. Second, its jitter range of $100$–$500\,\mu\mathrm{s}$ exceeds our entire cycle time $T_{c}=8\,\mu\mathrm{s}$ by more than an order of magnitude, so the synchronization requirement identified in Section 6 is not a marginal design margin but a hard architectural requirement that only a deterministic, non‑queuing timing path can meet.

**Verification, benchmarking, and maintenance of a deployed control stack.** Reference [2] surveys generative AI for software engineering, counts well over one hundred different models for code synthesis already published, and argues that the trustworthiness of such tools will be boosted by training on the semantic (dynamic) as well as the syntactic (static) aspects of software, with stimulus‑response data structures and scalable test drivers as the foundation for evaluating them [2]. If HES sequence templates are ever synthesized by generative tools, this is the evaluation discipline they would need; the dynamic‑behavior emphasis of [2] maps onto the fact that the HES test oracle is a quantum state, observable only through tomography‑like measurements. Reference [6] documents why evaluation infrastructure must be built deliberately: current benchmarks focus on narrow tasks and single metrics, HumanEval's top models now exceed 90% accuracy making it ineffective for differentiating capabilities, and the work proposes the BEHELM framework to evaluate models across robustness, interpretability, fairness, and efficiency dimensions [6]. An HES template library would face the same failure mode—a benchmark that certifies templates on narrow device classes while remaining silent on robustness to parameter drift. Reference [7] envisions an AI‑powered maintenance phase that remains constantly active, monitoring external sources to gather issues and maintenance opportunities, while cautioning against over‑reliance on AI and insisting that human judgment remains indispensable for assessing AI‑generated artifacts [7]; this is the operational posture a fleet of deployed HES controllers would require, with the caveat that autonomous re‑optimization of control waveforms touches the physical layer and cannot be treated as a software‑only maintenance problem. Reference [3] supplies the general standard—Web Engineering is defined as the application of systematic, disciplined and quantifiable approaches to development, operation, and maintenance of web‑based applications [3]—which is the standard the HES specification, versioning, and rollback procedures of Section 3.1 must meet to be an engineering practice rather than a laboratory recipe. Finally, reference [4] systematically maps the literature on cognitive biases in software engineering and takes as its premise that systematic errors introduced by human cognitive biases are one source of software project challenges and failures [4]; in this paper's context, the relevant bias risk is anchoring on the predecessor's assumptions (A1–A16), which is why every input is restated and re‑derived here rather than inherited.

**The predecessor.** Reference [9] is the published version under revision. Its derivations of $T_{c}=8\,\mu\mathrm{s}$, $N_{c}=125$, $\epsilon_{\mathrm{tot}}=1.25\times10^{-3}$, $T_{\mathrm{loop}}=1.8\times10^{-4}\,\mathrm{s}$, and $\rho=0.5$ are arithmetically correct and are retained; its Discussion claim extending the architectural conclusion to $\epsilon_{c}=10^{-4}$ is not, and is corrected in Section 4.

## 3. Methods

### 3.1 Service model

We define a network service, the Hamiltonian Engineering Service (HES), with the following contract. A quantum endpoint $E_{q}$ (a memory, transducer, or QKD node) exposes: (i) its natural Hamiltonian parameters $H_{0}(\theta)$, where $\theta$ is a vector of slowly drifting device parameters; (ii) a coherence time $T_{2}$; and (iii) a pulse‑actuation interface accepting control waveforms with minimum pulse width $\tau_{p}$. An in‑network controller $C_{n}$ (hosted on an edge node or smart network interface card) exposes: (i) a sequence‑template library $\mathcal{L}$, each template $L_{k}$ being a compiled decoupling or recoupling sequence; (ii) a scheduler that aligns cycle boundaries with network timing signals; and (iii) a verification module that checks the template's applicability conditions against the reported $\theta$.

The service‑level objective is an effective‑Hamiltonian error tolerance:
$$
\bigl\|\bar{H} - H_{\mathrm{eff}}\bigr\| \le \epsilon_{c}\,\|H_{0}\|,
$$
where $\bar{H}$ is the cycle‑averaged Hamiltonian and $\epsilon_{c}$ is the per‑cycle relative error budget. This contract follows the semi‑classical control model of [1], in which the controller accepts classical input and returns classical information while the system under control is quantum‑mechanical; the HES makes that interface explicit as a network service.

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
\epsilon_{\mathrm{tot}}=N_{c}\,\epsilon_{c},\qquad
F_{\mathrm{proj}}\approx1-\epsilon_{\mathrm{tot}},
$$
where $F_{\mathrm{proj}}$ is the projected end‑of‑window process fidelity. This linear model is a modeling assumption, and Section 6 discusses its replacement by second‑order Floquet‑Magnus bounds in the spirit of [5].

### 3.3 Closed‑loop latency and re‑entry models

We model one in‑network feedback cycle as four sequential stages:
$$
T_{\mathrm{loop}}=T_{s}+T_{p}+T_{c}'+T_{a},
$$
where $T_{s}$ is the sensing/measurement interval, $T_{p}$ the packet‑transport latency, $T_{c}'$ the compute time for the control update, and $T_{a}$ the actuation setup time. Re‑entry is physically meaningful only if the loop closes within the coherence window:
$$
\frac{T_{\mathrm{loop}}}{T_{2}}\le\eta_{\mathrm{max}},
$$
with $\eta_{\mathrm{max}}=0.2$ a design margin. As noted in Section 2, this budget applies to real‑time feedback in the sense of [1], not to closed‑loop learning over many copies.

For re‑entry, let the HES stack consist of $N_{\mathrm{tot}}$ components partitioned into a physics‑facing layer $\mathcal{P}$ and an infrastructure‑facing layer $\mathcal{I}$. The re‑entry reuse ratio is
$$
\rho=\frac{N_{\mathrm{reuse}}}{N_{\mathrm{tot}}},\qquad
N_{\mathrm{reuse}}=|\mathcal{P}_{\mathrm{portable}}|+|\mathcal{I}_{\mathrm{portable}}|,
$$
where a component is portable if its specification does not reference generation‑specific infrastructure parameters. The inventory is enumerated explicitly in Section 4 so that $\rho$ is auditable. Re‑qualification effort is modeled as linear in the number of non‑portable components:
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}}),
$$
with $e$ a per‑component effort assumption.

### 3.4 Method status

The method of this paper is analytical derivation from labeled assumptions, together with a correction audit of the predecessor's derivations [9]. No hardware experiment, simulation, survey, or expert review was performed; a study that would test the results is proposed in Section 7.

## 4. Analysis

Every input number below is a design assumption, not an empirical measurement; each is labeled A1–A16. Where a number is inherited from the predecessor [9], the derivation is restated in full so the paper is self‑contained.

**Inputs (timing/fidelity model).** $T_{2}=1\,\mathrm{ms}=10^{-3}\,\mathrm{s}$ (A1); $\tau_{p}=0.5\,\mu\mathrm{s}=5\times10^{-7}\,\mathrm{s}$ (A2); $\tau_{i}=0.5\,\mu\mathrm{s}=5\times10^{-7}\,\mathrm{s}$ (A3); $n_{p}=8$ (A4); $\epsilon_{c}=10^{-5}$ (A5); $K=64$ endpoints per node (A6).

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

**Derivation 4 — accumulated error and projected fidelity.**
$$
\epsilon_{\mathrm{tot}}=N_{c}\,\epsilon_{c}=125\times10^{-5}=1.25\times10^{-3},
$$
$$
F_{\mathrm{proj}}\approx1-1.25\times10^{-3}=0.99875.
$$

**Derivation 5 — actuation update rate per endpoint.**
$$
R_{u}=\frac{1}{\tau_{p}}=\frac{1}{5\times10^{-7}\,\mathrm{s}}=2\times10^{6}\,\mathrm{s^{-1}}.
$$

**Derivation 6 — aggregate update rate per node.**
$$
K\,R_{u}=64\times2\times10^{6}\,\mathrm{s^{-1}}=1.28\times10^{8}\,\mathrm{s^{-1}}.
$$

**Derivation 7 — sensitivity to $T_{2}$.** If $T_{2}'=10^{-4}\,\mathrm{s}$ (the upper end of the $10$–$100\,\mu\mathrm{s}$ hardware range reported in [8]),
$$
N_{c}'=\Bigl\lfloor\frac{10^{-4}}{8\times10^{-6}}\Bigr\rfloor=12,\qquad
\epsilon_{\mathrm{tot}}'=12\times10^{-5}=1.2\times10^{-4},
$$
$$
F_{\mathrm{proj}}'\approx1-1.2\times10^{-4}=0.99988.
$$
The cycle structure survives the degraded coherence; the binding constraint at short $T_{2}$ is instead the latency budget of Derivation 10, since $T_{\mathrm{loop}}=1.8\times10^{-4}\,\mathrm{s}$ would exceed $T_{2}'=10^{-4}\,\mathrm{s}$ outright.

**Derivation 8 — error‑budget headroom.** To hold $\epsilon_{\mathrm{tot}}\le0.01$ with $N_{c}=125$,
$$
\epsilon_{c}^{\mathrm{max}}=\frac{0.01}{125}=8\times10^{-5},
$$
so the chosen $\epsilon_{c}=10^{-5}$ carries a headroom factor of $8$.

**Derivation 8b — correction of the predecessor's validity claim.** The predecessor's Discussion states that the architectural conclusion follows whenever $T_{2}$ is in the millisecond range and $\epsilon_{c}$ is at or below $10^{-4}$ [9]. Testing that claim against the predecessor's own model: with $\epsilon_{c}=10^{-4}$ and $N_{c}=125$,
$$
\epsilon_{\mathrm{tot}}=125\times10^{-4}=1.25\times10^{-2},
$$
which exceeds the $0.01$ total‑error target used in Derivation 8 by a factor of $1.25$. The claim therefore fails at the predecessor's own cycle parameters, and the correct general condition is obtained by requiring $N_{c}\,\epsilon_{c}\le0.01$ with $N_{c}=T_{2}/T_{c}$:
$$
\epsilon_{c}\le\frac{0.01\,T_{c}}{T_{2}}.
$$
For $T_{2}=1\,\mathrm{ms}$ and $T_{c}=8\,\mu\mathrm{s}$ this gives $\epsilon_{c}\le8\times10^{-5}$, confirming Derivation 8. The corrected statement is: the architectural conclusion (microsecond cycles, hardware‑adjacent control) follows whenever $T_{2}$ is in the millisecond range and $\epsilon_{c}\le0.01\,T_{c}/T_{2}$; at $T_{c}=8\,\mu\mathrm{s}$ this is $\epsilon_{c}\le8\times10^{-5}$, and the looser threshold $\epsilon_{c}\le10^{-4}$ is admissible only if $T_{c}\le1.25\times10^{-5}\,\mathrm{s}$ is relaxed upward or the total‑error target is relaxed to $1.25\times10^{-2}$.

**Inputs (closed‑loop and re‑entry models).** $T_{s}=1.0\times10^{-4}\,\mathrm{s}$ (A7); $T_{p}=2.0\times10^{-5}\,\mathrm{s}$ (A8); $T_{c}'=5.0\times10^{-5}\,\mathrm{s}$ (A9); $T_{a}=1.0\times10^{-5}\,\mathrm{s}$ (A10); $W=64$ bits per qubit per control word (A11); $N_{q}=1000$ qubits (A12); $R_{\mathrm{link}}=1.0\times10^{11}\,\mathrm{bit/s}$ (A13); $\eta_{\mathrm{max}}=0.2$ (A14).

**Derivation 9 — loop latency.**
$$
T_{\mathrm{loop}}=1.0\times10^{-4}+2.0\times10^{-5}+5.0\times10^{-5}+1.0\times10^{-5}=1.8\times10^{-4}\,\mathrm{s}.
$$

**Derivation 10 — coherence fraction consumed.**
$$
\eta=\frac{T_{\mathrm{loop}}}{T_{2}}=\frac{1.8\times10^{-4}}{1.0\times10^{-3}}=0.18\le\eta_{\mathrm{max}}=0.2,
$$
margin $=0.02$, headroom factor $=0.2/0.18\approx1.111$.

**Derivation 11 — control‑plane bandwidth per cycle.**
$$
B_{\mathrm{cycle}}=W\cdot N_{q}=64\times1000=6.4\times10^{4}\,\mathrm{bits},
$$
$$
\tau_{\mathrm{tx}}=\frac{6.4\times10^{4}}{1.0\times10^{11}}=6.4\times10^{-7}\,\mathrm{s},
$$
$$
\frac{\tau_{\mathrm{tx}}}{T_{\mathrm{loop}}}= \frac{6.4\times10^{-7}}{1.8\times10^{-4}}\approx3.56\times10^{-3},
$$
i.e. $0.36\%$ of the loop budget. Transport bandwidth is therefore not the binding constraint; the stage latencies $T_{s}$ and $T_{c}'$ dominate the loop.

**Derivation 12 — re‑entry reuse ratio.** Inventory of twelve components (Assumption A15) is:

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
Counting component 11 as portable would raise $\rho$ to $7/12\approx0.583$; we report the conservative $\rho=0.5$ with bounds $0.5\le\rho\le0.583$.

**Derivation 13 — re‑qualification effort (projection).** Assuming $e=4$ person‑weeks per non‑portable component (A16):
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}})=4\times6=24\ \text{person‑weeks}.
$$
Uncertainty linear in $e$ yields $E_{\mathrm{req}}\in[12,48]$ person‑weeks for $e\in[2,8]$.

**Labeled projection — aggregate control‑bandwidth (not adopted as a headline).** An alternative model assumes $N=1000$ nodes, each repeating a $256$‑bit encoded pulse sequence at $f=1\,\mathrm{MHz}$:
$$
B_{\mathrm{total}}=N\times f\times b=1000\times10^{6}\times256=2.56\times10^{11}\,\mathrm{bit/s}=256\,\mathrm{Gb/s},
$$
with $20\%$ independent uncertainties on $N$, $f$, and $b$ combined in quadrature:
$$
\epsilon=\sqrt{3\times0.20^{2}}=\sqrt{0.12}\approx0.346,
$$
giving $B_{\mathrm{total}}\in[256\times0.654,\,256\times1.346]\approx[167,\,345]\,\mathrm{Gb/s}$. This projection rests on stronger assumptions than the per‑endpoint model (simultaneous per‑node repetition across 1000 nodes) and is retained only for transport‑planning use; the headline actuation figures are those of Derivations 5–6.

## 5. Results

All results follow from the derivations in Section 4 under the stated assumptions A1–A16; none is an empirical measurement. "Projected" denotes the linear accumulation model of Section 3.2.

| Quantity | Symbol | Value |
|---|---|---|
| Engineering cycle time | $T_{c}$ | $8\times10^{-6}\,\mathrm{s}$ |
| Actuation duty factor | $f$ | $0.5$ |
| Cycles per coherence window | $N_{c}$ | $125$ |
| Accumulated error over one window | $\epsilon_{\mathrm{tot}}$ | $1.25\times10^{-3}$ |
| Projected end‑of‑window fidelity | $F_{\mathrm{proj}}$ | $\approx0.99875$ (projection) |
| Update rate per endpoint | $R_{u}$ | $2\times10^{6}\,\mathrm{s^{-1}}$ |
| Aggregate update rate, $K=64$ | $K\,R_{u}$ | $1.28\times10^{8}\,\mathrm{s^{-1}}$ |
| Per‑cycle error‑budget ceiling ($\epsilon_{\mathrm{tot}}\le0.01$) | $\epsilon_{c}^{\mathrm{max}}$ | $8\times10^{-5}$ |
| Headroom factor at $\epsilon_{c}=10^{-5}$ | — | $8$ |
| Corrected validity threshold (Derivation 8b) | $\epsilon_{c}\le0.01\,T_{c}/T_{2}$ | $8\times10^{-5}$ (not $10^{-4}$) |
| Degraded‑$T_{2}$ case ($T_{2}'=10^{-4}\,\mathrm{s}$) | $N_{c}'$, $F_{\mathrm{proj}}'$ | $12$, $\approx0.99988$ (projection) |
| Closed‑loop latency | $T_{\mathrm{loop}}$ | $1.8\times10^{-4}\,\mathrm{s}$ |
| Coherence fraction consumed | $\eta$ | $0.18$ (headroom $\approx1.111$) |
| Per‑cycle control payload | $B_{\mathrm{cycle}}$ | $6.4\times10^{4}$ bits ($\approx0.36\%$ of loop budget) |
| Re‑entry reuse ratio | $\rho$ | $0.5$ (bound $0.5$–$0.583$) |
| Projected re‑qualification effort | $E_{\mathrm{req}}$ | $24$ person‑weeks (range $12$–$48$, projection) |

Headline architectural conclusions are: (i) a microsecond‑scale engineering cycle is compatible with millisecond‑scale coherence under a $10^{-5}$ per‑cycle error budget, but the required actuation rate of $2\times10^{6}\,\mathrm{s^{-1}}$ per endpoint places the control function in the category of hardware‑adjacent network compute; (ii) under the closed‑loop assumptions, latency staging rather than bandwidth is the binding constraint; (iii) re‑entry is a half‑rebuild: the physics‑facing layer is portable, the infrastructure‑facing layer—especially timing distribution—is not; and (iv) the validity envelope of conclusion (i) is $\epsilon_{c}\le8\times10^{-5}$ at these cycle parameters, a correction to the predecessor's stated $10^{-4}$.

## 6. Discussion

**Limitations of the fidelity model.** The linear error‑accumulation model is the weakest link. Coherent errors can add quadratically, potentially inflating $\epsilon_{\mathrm{tot}}$, while echo‑structured sequences can cancel first‑order terms, reducing