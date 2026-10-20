# Re-Entry Analysis for In-Network Hamiltonian Engineering in 6G: Timing Budgets, Fidelity Budgets, and Control-Stack Portability Across Infrastructure Generations

## Abstract

Sixth-generation (6G) network research proposes placing semi-classical quantum control logic inside the network fabric, so that network nodes participate directly in quantum state and process control; the QNFO program (In-Network Hamiltonian Engineering for 6G) is one such proposal. The open question this paper addresses is re-entry: when the underlying 6G infrastructure is upgraded or replaced, how much of the in-network control stack can be carried across without full redesign, and at what qualification cost. No existing text under the QNFO identifier supplies a component inventory, timing budget, or portability metric, so this paper constructs all three. We define a Hamiltonian Engineering Service (HES) contract between quantum endpoints and in-network controllers, derive its timing and fidelity budget for a node with coherence time $T_2 = 1\,\mathrm{ms}$, an engineering cycle $T_c = 8\,\mu\mathrm{s}$, and a per-cycle error budget $\epsilon_c = 10^{-5}$: the budget admits $N_c = 125$ cycles per coherence window with accumulated error $1.25 \times 10^{-3}$ and a projected end-of-window fidelity $\approx 0.99875$ under a stated linear accumulation model, at an actuation rate of $2 \times 10^{6}\,\mathrm{s^{-1}}$ per endpoint. We formalize re-entry as a measurable reuse ratio over an explicit twelve-component inventory, obtaining $\rho = 0.5$ (bounded by $0.583$) and a projected re-qualification effort of 24 person-weeks (range 12–48). A closed-loop latency of $1.8 \times 10^{-4}\,\mathrm{s}$ consumes $\eta = 0.18$ of the coherence window against a design margin of $0.2$. Every number is computed here with shown arithmetic from explicitly labeled assumptions; none is an empirical measurement. The results give 6G architects a budget structure — cycle time, per-cycle error, coherence window, actuation rate, and portability fraction — that must be co-managed if quantum devices become infrastructure.

## 1. Introduction

Telecommunications operators and quantum-network system engineers face a problem that does not yet have a measurement: if quantum control moves into the network fabric of 6G, every infrastructure upgrade becomes a quantum-control re-qualification event. Today, quantum control hardware sits in laboratories and networks carry results, so network upgrades never touch control correctness. Under proposals such as the QNFO program's in-network Hamiltonian engineering, the network itself becomes the control instrument, and a router replacement, a timing-plane migration, or a transport reconfiguration can invalidate the pulse schedules that a deployed quantum endpoint depends on. What this costs, if it is unmanaged, is a full redesign of the control stack at every infrastructure generation; what it blocks is the incremental, backwards-compatible evolution that every large network depends on. A decision that would change if this paper's result holds is the partition of the control stack into a portable physics-facing layer and a generation-locked infrastructure-facing layer, with re-qualification scoped to the latter rather than to the whole.

The QNFO concept performs Hamiltonian engineering — the deliberate reshaping of an effective quantum Hamiltonian by a designed, time-dependent control Hamiltonian $H_c(t)$ applied on top of a natural Hamiltonian $H_0$ — inside the network itself. This creates a dependency inversion: the network is no longer a passive transport medium but the control instrument. Two questions follow. First, is the service physically realizable at network timescales: can a control cycle executed through network elements close within a coherence window, and at what fidelity and actuation cost? Second, is the architecture maintainable: when the underlying 6G infrastructure is upgraded or replaced, can the control stack be re-entered — carried across — without full redesign? This paper answers the second question quantitatively and gives the first question a budget structure.

Three observations motivate placing control in the network and treating its persistence across generations as a first-class design object. First, the benefits of advanced transport and sensing programs are consistently held back by the same factor: realization hinges on the timely integration of the new digital capability into existing infrastructure, a pattern documented for connected-vehicle programs where safety, mobility, environmental, energy, and economic benefits "largely hinge on the timely integration of digital technology into upcoming as well as existing transportation infrastructure" [4]. Second, the most pressing problems in new scientific capabilities are infrastructural rather than empirical or theoretical, as argued for decentralized research infrastructure [3]; an in-network quantum control stack is exactly such an infrastructure, and its cross-generation behavior is an infrastructural property, not a physics result. Third, digital infrastructure in mature scientific fields is maintained by small developer communities and is much harder to fund for upkeep than for initial development [1]; a control stack embedded in 6G will inherit this maintenance economics, so the fraction of the stack that survives a generation transition — the re-entry ratio — directly determines the recurring maintenance burden.

This paper makes three contributions:

1. A service model and quantitative timing/fidelity budget for a Hamiltonian Engineering Service, derived in Sections 3 and 4: for $T_2 = 1\,\mathrm{ms}$, $T_c = 8\,\mu\mathrm{s}$, and $\epsilon_c = 10^{-5}$, the budget yields $N_c = 125$ cycles per window, accumulated error $1.25 \times 10^{-3}$, projected fidelity $\approx 0.99875$, and actuation at $2 \times 10^{6}\,\mathrm{s^{-1}}$ per endpoint (Section 4, Derivations 1–8).
2. A closed-loop latency and bandwidth analysis showing that under the stated assumptions latency staging, not bandwidth, is the binding constraint: $T_{\mathrm{loop}} = 1.8 \times 10^{-4}\,\mathrm{s}$, $\eta = 0.18$ against a margin of $0.2$, with control payload transmission consuming about $0.36\%$ of the loop budget (Section 4, Derivations 9–11).
3. A re-entry analysis formalized as an auditable reuse ratio over an explicit twelve-component inventory, giving $\rho = 0.5$ (bound $0.5$–$0.583$) and a projected re-qualification effort of 24 person-weeks with range 12–48 (Section 4, Derivations 12–13), together with the falsification conditions for every claim (Section 6).

Every number is either computed here with shown arithmetic from labeled assumptions or explicitly labeled a projection with stated assumptions. This paper performs no experiment, measurement, or simulation on hardware, and makes no empirical claims about deployed 6G or quantum systems.

## 2. Background and Related Work

The eight works cited here all concern digital infrastructure — its integration burdens, its maintenance economics, its failure modes, and its measurement — and none concerns quantum control directly. They are used for what their texts state about infrastructure problems that the in-network quantum control stack will inherit.

**Infrastructure integration as the binding constraint.** Reference [4] reviews connected-vehicle (CV) applications and states in its opening that the safety, mobility, environmental, energy, and economic benefits of transportation systems "are potentially dramatic," but that "realization of these benefits largely hinges on the timely integration of digital technology into upcoming as well as existing transportation infrastructure," with vehicles required to broadcast and receive data. The record shows the review matured through four versions between March 2018 and August 2019 [4]. The parallel is direct: whatever benefits in-network quantum control offers, their realization hinges on integrating pulse-level control into existing 6G infrastructure, and re-entry is the mechanism by which that integration survives successive infrastructure generations rather than being repeated at each one.

**Infrastructure deficits as the primary obstacle.** Reference [3] opens with the claim that "the most pressing problems in science are neither empirical nor theoretical, but infrastructural," and that scientific practice is defined by "coproductive, mutually reinforcing infrastructural deficits and incentive systems" that constrain research; the work argues for decentralized infrastructure for (neuro)science, submitted in September 2022 [3]. Applied here: the obstacles to in-network Hamiltonian engineering are not the control-theory primitives, which exist, but the infrastructural deficits — timing distribution, qualification, versioning — that no single stakeholder owns. Re-entry analysis is a way of pricing one such deficit, the generation-coupling of control software to infrastructure hardware.

**Maintenance economics of long-lived infrastructure.** Reference [1], a workshop report on open digital infrastructure in astrophysics, documents that astronomy "has long encouraged the development of free, open digital infrastructure," that "nearly all astronomical research relies on free, open source software written and maintained by a small number of developers," that "like the physical infrastructure of roads or bridges, digital infrastructure needs regular upkeep and maintenance," and — the point this paper uses — that "financial support for maintaining existing digital infrastructure is generally much harder to secure than funding for developing new digital infrastructures that promise new science" [1]. The re-entry ratio $\rho$ is precisely the quantity that scales this maintenance burden for a quantum control stack: a stack with $\rho = 0.5$ must re-qualify half its components at every infrastructure generation, and the person-week cost of that re-qualification is the recurring, unfunded-upkeep class of expense that [1] identifies. The workshop's focus on sustainability plans and developer models across FOSS projects [1] is the same governance question the QNFO stack will face for its sequence-template library.

**Handoff and shared interfaces between expert communities.** Reference [2] reports a retrospective on collaborative Mars geoscience at the NASA Jet Propulsion Lab using the PIXLISE spectroscopic analysis platform, and its discussion states that scientific visualization systems "regularly encounter the infrastructural tensions identified by Ribes and Finholt, despite high commitment from their users," and that the platform "supports handoff between experts with differing backgrounds" [2]. Its analysis identifies four boundary objects specific to Mars geoscience practices that are operationalized in the software, including "models" and "evidence" referring to background knowledge and context drawn from scientific papers [2]. The boundary-object concept maps onto the interface contract between the physics-facing layer (Hamiltonian targets, pulse sequences) and the infrastructure-facing layer (timing, transport, drivers) of the QNFO stack: the portable components in the inventory of Section 4 are exactly those whose specifications can serve as boundary objects that do not reference generation-specific parameters, and the handoff problem between control theorists and network engineers is the same expert-handoff problem PIXLISE was built to manage.

**Lightweight trust and credentialing in protocol stacks.** Reference [5] addresses authentication in the Session Initiation Protocol, stating that SIP "has become the most predominant protocol for Voice over Internet Protocol (VoIP) signaling," that SIP security is an important consideration because traffic crosses insecure IP networks, and that "the authentication process in SIP ranges from pre-shared secret based solutions to Public Key Infrastructure (PKI) based solution," motivating authentication schemes that reduce PKI dependence [5]. The QNFO endpoint-to-controller interface faces the same spectrum: full PKI-based attestation of every in-network controller is heavy at microsecond actuation cadence, while pre-shared credentials per endpoint-controller pair scale as $O(K)$ per node. The SIP precedent shows that protocol communities have already traded heavyweight against lightweight authentication for latency-sensitive signaling, and the same trade must be made explicit in the HES contract of Section 3.

**Measuring capability rather than single outcomes.** Reference [6] notes that "normalised citation counts are routinely used to assess the average impact of research groups or nations," that there is controversy over whether confidence intervals for them are theoretically valid or practically useful, and introduces "the concept of a group's underlying research capability to produce impactful research," investigating whether confidence intervals could delimit it [6]. The methodological point transfers to re-entry benchmarking: a single migration event is a single outcome, and statements about a stack's re-entry capability across future, unobserved migrations require interval-valued or distributional characterizations rather than a point estimate. This paper respects that distinction by reporting $\rho$ as a bounded interval ($0.5$–$0.583$) and the re-qualification effort as a range (12–48 person-weeks) rather than as point predictions.

**Infrastructure lag behind instrument capability.** Reference [7] states that modern biological tools, especially microscopy, "have rapidly advanced in recent years," generating "increasingly large amounts of data on a regular basis," with the result that "scientists desperately need state-of-the-art technical infrastructure for raw data storage, transfer, and processing" while they "currently rely on outdated ways to move and store data" [7]. This is the lag pattern the QNFO stack must avoid: quantum endpoint capability (coherence times, endpoint counts) will advance on a different schedule than network control-plane capability, and the timing/fidelity budget of Section 4 is the instrument for detecting when the control plane, not the quantum device, becomes the bottleneck.

**Failure analysis and dependability notation for control infrastructure.** Reference [8] states that "SCADA systems are widely used within critical infrastructures to perform system controls and deliver services to linked and dependent systems," and describes a PhD-proposal-stage investigation of SCADA failures in interdependent critical infrastructure systems whose results "will be used to develop a new notation to help risk assessment using dependable computing concepts" [8]. In-network Hamiltonian engineering places the control function in a SCADA-like position: a network-hosted controller issuing real-time commands to physical processes (quantum endpoints) with safety-relevant failure modes. The dependable-computing notation program of [8] is the nearest methodological neighbor for a re-entry risk assessment: the component inventory and portability classification of Section 4 is a first, informal step in exactly that direction, and a failure-notation treatment of the HES would make the classification auditable rather than enumerative.

No cited work treats quantum control, pulse sequences, or coherence; the quantum-control content of this paper is therefore built entirely from the model stated in Sections 3 and 4 as this paper's own assumptions, and the cited literature is used only for the infrastructure-side patterns named above. This restriction is stated as a limitation in Section 6.

## 3. Methods

### 3.1 Service model

We define one new network service, the Hamiltonian Engineering Service (HES), with the following contract. A quantum endpoint $E_q$ (a memory, transducer, or quantum-secure communication node) exposes: (i) its natural Hamiltonian parameters $H_0(\theta)$, where $\theta$ is a vector of slowly drifting device parameters; (ii) a coherence time $T_2$; and (iii) a pulse-actuation interface accepting control waveforms with minimum pulse width $\tau_p$. An in-network controller $C_n$ (hosted on an edge node or smart network interface card) exposes: (i) a sequence-template library $\mathcal{L}$, each template $L_k$ being a compiled decoupling or recoupling sequence; (ii) a scheduler that aligns cycle boundaries with network timing signals; and (iii) a verification module that checks the template's applicability conditions against the reported $\theta$.

The service-level objective is stated as an effective-Hamiltonian error tolerance: over one engineering cycle of duration $T_c$, the stroboscopic dynamics must satisfy

$$\left\| \bar{H} - H_{\mathrm{eff}} \right\| \le \epsilon_c \, \|H_0\|,$$

where $\bar{H}$ is the cycle-averaged Hamiltonian and $\epsilon_c$ is the per-cycle relative error budget. We assume the template library consists of precompiled, rule-based sequences whose error scaling is analytically understood, because a network control plane cannot host per-device numerical optimization at microsecond cadence; this is an assumption of the model (A0), not a claim about any existing library.

### 3.2 Timing and fidelity model

Each cycle consists of $n_p$ pulses of width $\tau_p$ separated by idle intervals, so

$$T_c = n_p (\tau_p + \tau_i), \qquad f = \frac{n_p \tau_p}{T_c} = \frac{\tau_p}{\tau_p + \tau_i},$$

with $f$ the actuation duty factor. The controller must issue actuation updates at rate $R_u = 1/\tau_p$ per endpoint; a node hosting $K$ endpoints presents an aggregate update rate $K R_u$.

We adopt a first-order accumulation model in which per-cycle fractional error contributions add linearly over $N_c$ cycles within one coherence window:

$$N_c = \left\lfloor \frac{T_2}{T_c} \right\rfloor, \qquad \epsilon_{\mathrm{tot}} = N_c \, \epsilon_c, \qquad F_{\mathrm{proj}} \approx 1 - \epsilon_{\mathrm{tot}},$$

where $F_{\mathrm{proj}}$ is the projected end-of-window process fidelity. This linear model is conservative relative to coherent-error growth models in the worst case and optimistic relative to models with cancellation; it is a modeling assumption, not a measurement, and Section 6 discusses its replacement.

### 3.3 Closed-loop latency and re-entry models

We model one in-network feedback cycle as four sequential stages:

$$T_{\mathrm{loop}} = T_s + T_p + T_c' + T_a,$$

where $T_s$ is the sensing/measurement interval, $T_p$ the packet transport latency from sensor to in-network compute node and back, $T_c'$ the compute time for the control update, and $T_a$ the actuation setup time. Re-entry of the loop into the coherence window is physically meaningful only if

$$\frac{T_{\mathrm{loop}}}{T_2} \le \eta_{\mathrm{max}},$$

with $\eta_{\mathrm{max}}$ a stated design margin; we take $\eta_{\mathrm{max}} = 0.2$ (A14).

For re-entry, let the QNFO stack consist of $N_{\mathrm{tot}}$ components partitioned into a physics-facing layer $\mathcal{P}$ (Hamiltonian targets, pulse sequences, control algorithms) and an infrastructure-facing layer $\mathcal{I}$ (timing distribution, transport, node hardware, qualification). The re-entry reuse ratio is

$$\rho = \frac{N_{\mathrm{reuse}}}{N_{\mathrm{tot}}}, \qquad N_{\mathrm{reuse}} = |\mathcal{P}_{\mathrm{portable}}| + |\mathcal{I}_{\mathrm{portable}}|,$$

where a component is portable if its specification does not reference generation-specific infrastructure parameters. The inventory is enumerated explicitly in Section 4 so that $\rho$ is auditable component by component. Re-qualification effort is modeled as linear in the number of non-portable components:

$$E_{\mathrm{req}} = e \,(N_{\mathrm{tot}} - N_{\mathrm{reuse}}),$$

with $e$ a per-component effort assumption.

### 3.4 Method status

The method of this paper is analytical derivation from labeled assumptions. No hardware experiment, simulation, survey, or expert review was performed; a study that would test the results against hardware is proposed in Section 7 as future work, written in the conditional.

## 4. Analysis

Every input number below is a design assumption of this paper, not an empirical measurement; each is labeled A1–A16.

**Inputs (timing/fidelity model).** $T_2 = 1\,\mathrm{ms} = 10^{-3}\,\mathrm{s}$ (A1); $\tau_p = 0.5\,\mu\mathrm{s} = 5 \times 10^{-7}\,\mathrm{s}$ (A2); $\tau_i = 0.5\,\mu\mathrm{s} = 5 \times 10^{-7}\,\mathrm{s}$ (A3); $n_p = 8$ (A4); $\epsilon_c = 10^{-5}$ (A5); $K = 64$ endpoints per node (A6).

**Derivation 1 — cycle time.**

$$T_c = n_p (\tau_p + \tau_i) = 8 \times (5 \times 10^{-7} + 5 \times 10^{-7})\,\mathrm{s} = 8 \times 10^{-6}\,\mathrm{s} = 8\,\mu\mathrm{s}.$$

**Derivation 2 — duty factor.**

$$f = \frac{\tau_p}{\tau_p + \tau_i} = \frac{5 \times 10^{-7}}{10^{-6}} = 0.5.$$

Half of every coherence window is consumed by actuation; the endpoint is available for data operations only in the idle fraction $1 - f = 0.5$.

**Derivation 3 — cycles per coherence window.**

$$\frac{T_2}{T_c} = \frac{10^{-3}}{8 \times 10^{-6}} = 125, \qquad N_c = \lfloor 125 \rfloor = 125.$$

**Derivation 4 — accumulated error and projected fidelity.**

$$\epsilon_{\mathrm{tot}} = N_c \, \epsilon_c = 125 \times 10^{-5} = 1.25 \times 10^{-3}, \qquad F_{\mathrm{proj}} \approx 1 - 1.25 \times 10^{-3} = 0.99875.$$

$F_{\mathrm{proj}}$ is a projection under the linear accumulation model of Section 3.2, not a fidelity prediction.

**Derivation 5 — actuation update rate per endpoint.**

$$R_u = \frac{1}{\tau_p} = \frac{1}{5 \times 10^{-7}\,\mathrm{s}} = 2 \times 10^{6}\,\mathrm{s^{-1}}.$$

**Derivation 6 — aggregate update rate per node.**

$$K R_u = 64 \times 2 \times 10^{6}\,\mathrm{s^{-1}} = 1.28 \times 10^{8}\,\mathrm{s^{-1}}.$$

**Derivation 7 — sensitivity to $T_2$.** If $T_2$ degrades to $T_2' = 10^{-4}\,\mathrm{s}$, then

$$N_c' = \left\lfloor \frac{10^{-4}}{8 \times 10^{-6}} \right\rfloor = 12, \qquad \epsilon_{\mathrm{tot}}' = 12 \times 10^{-5} = 1.2 \times 10^{-4}, \qquad F_{\mathrm{proj}}' \approx 0.99988.$$

Note the counterintuitive direction: shorter $T_2$ reduces accumulated error because fewer cycles execute before the window closes, but it also reduces the useful window by the same factor — the fidelity metric alone understates the cost of decoherence, so we report $N_c$ alongside $F_{\mathrm{proj}}$.

**Derivation 8 — error budget headroom.** To hold $\epsilon_{\mathrm{tot}} \le 0.01$ (adopted here as a design target, not a community standard) with $N_c = 125$:

$$\epsilon_c \le \frac{0.01}{125} = 8 \times 10^{-5},$$

so the chosen $\epsilon_c = 10^{-5}$ carries a headroom factor of $8 \times 10^{-5} / 10^{-5} = 8$.

**Inputs (closed-loop and re-entry models).** $T_s = 1.0 \times 10^{-4}\,\mathrm{s}$ (A7); $T_p = 2.0 \times 10^{-5}\,\mathrm{s}$ (A8); $T_c' = 5.0 \times 10^{-5}\,\mathrm{s}$ (A9); $T_a = 1.0 \times 10^{-5}\,\mathrm{s}$ (A10); $W = 64$ bits per qubit per control word (A11); $N_q = 1000$ qubits (A12); $R_{\mathrm{link}} = 1.0 \times 10^{11}\,\mathrm{bit/s}$ (A13); $\eta_{\mathrm{max}} = 0.2$ (A14).

**Derivation 9 — loop latency.**

$$T_{\mathrm{loop}} = 1.0 \times 10^{-4} + 2.0 \times 10^{-5} + 5.0 \times 10^{-5} + 1.0 \times 10^{-5} = 1.8 \times 10^{-4}\,\mathrm{s}.$$

**Derivation 10 — coherence fraction.**

$$\eta = \frac{T_{\mathrm{loop}}}{T_2} = \frac{1.8 \times 10^{-4}}{1.0 \times 10^{-3}} = 0.18 \le \eta_{\mathrm{max}} = 0.2,$$

with margin $\eta_{\mathrm{max}} - \eta = 0.02$ and headroom factor $\eta_{\mathrm{max}}/\eta = 0.2/0.18 \approx 1.111$. The margin is thin: an increase of about $11\%$ in any single stage latency exhausts it, since $0.18 \times 1.111 \approx 0.2$.

**Derivation 11 — control-plane bandwidth per cycle.**

$$B_{\mathrm{cycle}} = W \cdot N_q = 64 \times 1000 = 6.4 \times 10^{4}\,\mathrm{bits}, \qquad \tau_{\mathrm{tx}} = \frac{6.4 \times 10^{4}}{1.0 \times 10^{11}} = 6.4 \times 10^{-7}\,\mathrm{s}.$$

The transmission time relative to the loop budget is

$$\frac{\tau_{\mathrm{tx}}}{T_{\mathrm{loop}}} = \frac{6.4 \times 10^{-7}}{1.8 \times 10^{-4}} \approx 3.56 \times 10^{-3},$$

i.e., about $0.36\%$ of the loop budget. Under these assumptions, bandwidth is not the binding constraint; latency staging is.

**Derivation 12 — re-entry reuse ratio.** We enumerate a twelve-component inventory of the QNFO stack (Assumption A15; the partition is this paper's reconstruction, since no component list exists under the QNFO identifier):

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
11  Qualification test suite              I  counted not portable (conservative)
12  Monitoring/telemetry schema           I  portable
```

Portable count: components 1–5 and 12 give $N_{\mathrm{reuse}} = 6$; $N_{\mathrm{tot}} = 12$; therefore

$$\rho = \frac{6}{12} = 0.5.$$

Counting component 11 as portable would give $\rho = 7/12 \approx 0.583$; we report the conservative $\rho = 0.5$ as the headline and $0.5 \le \rho \le 0.583$ as the bound.

**Derivation 13 — re-qualification effort (projection).** If re-qualification effort per non-portable component is $e = 4$ person-weeks (Assumption A16), then

$$E_{\mathrm{req}} = e \,(N_{\mathrm{tot}} - N_{\mathrm{reuse}}) = 4 \times 6 = 24\,\text{person-weeks}.$$

This is a projection under A16; its uncertainty is linear in $e$, giving $E_{\mathrm{req}} \in [12, 48]$ person-weeks for $e \in [2, 8]$.

**Divergent projection — aggregate control bandwidth (labeled projection, not adopted as a headline).** An alternative aggregate model assumes $N = 1000$ nodes, each repeating a 256-bit encoded pulse sequence at $f_{\mathrm{rep}} = 1\,\mathrm{MHz}$, giving

$$B_{\mathrm{total}} = N \times f_{\mathrm{rep}} \times b = 1000 \times 10^{6} \times 256 = 2.56 \times 10^{11}\,\mathrm{bit/s} = 256\,\mathrm{Gb/s},$$

with independent $20\%$ uncertainties on $N$, $f_{\mathrm{rep}}$, and $b$ combined in quadrature:

$$\epsilon_B = \sqrt{3 \times 0.20^{2}} = \sqrt{0.12} \approx 0.346, \quad B_{\mathrm{total}} \in [256 \times 0.654,\, 256 \times 1.346] \approx [167,\, 345]\,\mathrm{Gb/s}.$$

This projection rests on assumptions (simultaneous per-node repetition at $1\,\mathrm{MHz}$ across 1000 nodes) that are stronger than those of Derivations 5–6, and it measures a different quantity: encoded-sequence traffic aggregated over the network, rather than control-word updates at the endpoint interface. The two conventions are not directly comparable without a mapping from $\tau_p$-driven updates to encoded-sequence repetitions, which this paper does not supply; we therefore retain Convention A (Derivations 5–6, per-endpoint actuation) for the headline results and record Convention B here as a labeled projection for transport-planning use only.

## 5. Results

All results below follow from the derivations in Section 4 under the stated assumptions A1–A16; none is an empirical measurement. Where "projected" appears, the projection is the linear accumulation model of Section 3.2 applied to the stated inputs.

| Quantity | Symbol | Value |
|---|---|---|
| Engineering cycle time | $T_c$ | $8 \times 10^{-6}\,\mathrm{s}$ |
| Actuation duty factor | $f$ | $0.5$ |
| Cycles per coherence window | $N_c$ | $125$ |
| Accumulated error over one window | $\epsilon_{\mathrm{tot}}$ | $1.25 \times 10^{-