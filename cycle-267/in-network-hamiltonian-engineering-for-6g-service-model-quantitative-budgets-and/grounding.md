# Grounding block - source: rem-f7b2081e-05e2-4af9-9c7d-3187c0fff738

## Research idea

Re-entry from 10.5281/zenodo.18307388: of the underlying 6G infrastructure?

## Existing paper under revision (remediation only)

# In-Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re-Entry Analysis

## Abstract

The QNFO program (In-Network Hamiltonian Engineering for 6G, https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g/) proposes placing semi-classical Hamiltonian control logic inside the network fabric of sixth-generation (6G) telecommunications infrastructure, so that network nodes participate directly in quantum state and process control. This paper develops the concept in three quantitative steps. First, we define a Hamiltonian Engineering Service (HES): a contract between quantum endpoints and in-network controllers, executed at microsecond cadence against millisecond coherence budgets. Second, we derive the timing and fidelity budget of the service: for a node with coherence time $T_2 = 1\,\mathrm{ms}$, an engineering cycle $T_c = 8\,\mu\mathrm{s}$, and a per-cycle error budget $\epsilon_c = 10^{-5}$, we compute $N_c = 125$ cycles per coherence window, accumulated error $1.25 \times 10^{-3}$, and a projected end-of-window fidelity $\approx 0.99875$ under a stated linear accumulation model, at an actuation rate of $2 \times 10^{6}\,\mathrm{s^{-1}}$ per endpoint. Third, we formalize re-entry — reuse of the control stack across infrastructure generations — as a measurable ratio, obtaining $\rho = 0.5$ for a stated twelve-component inventory, and a closed-loop latency of $1.8 \times 10^{-4}\,\mathrm{s}$ consuming $\eta = 0.18$ of the coherence window. Every number is computed here with shown arithmetic from explicitly labeled assumptions; none is an empirical measurement. We situate the framework in the Hamiltonian-engineering, quantum-network systems-engineering, and software-engineering literatures, and identify verification and benchmarking as the principal open problems.

## 1. Introduction

Sixth-generation network research increasingly treats the network not as a passive transport medium but as an active computational substrate. The QNFO concept pushes this trend to an extreme: it proposes to perform Hamiltonian engineering — the deliberate reshaping of an effective quantum Hamiltonian by a designed, time-dependent control Hamiltonian $H_c(t)$ applied on top of a natural Hamiltonian $H_0$ — inside the network itself, so that network nodes participate directly in quantum state and process control.

This creates a dependency inversion. Traditionally, quantum control hardware sits in the laboratory and the network merely carries results. In QNFO, the network is the control instrument. Two questions follow. First, is the service physically realizable at network timescales: can a control cycle executed through network elements close within a coherence window, and at what fidelity and actuation cost? Second, is the architecture maintainable: when the underlying 6G infrastructure is upgraded or replaced, can the control stack be re-entered — carried across — without full redesign?

Three observations motivate the placement of control in the network. First, quantum-secure telecommunications are already recognized as a systems-integration problem: realizing quantum-technology advances depends on engineering highly complex systems that integrate quantum devices into existing classical infrastructure [4]. Second, the control theory needed — using a semi-classical controller to engineer quantum Hamiltonians for state, process, or observable-optimization objectives — is generic and does not intrinsically require co-location [1]. Third, pulse-sequence design has matured to where higher-order effects in the Floquet-Magnus expansion can be systematically accounted for with simple, intuitive decoupling rules [5], which is precisely the kind of compiled, rule-based artifact a network control plane can distribute and execute.

The paper makes three contributions: (i) a service model and quantitative timing/fidelity budget for the Hamiltonian Engineering Service; (ii) a closed-loop latency, bandwidth, and re-entry reuse analysis; (iii) a mapping onto the systems-engineering and software-engineering literatures with an explicit statement of what would falsify each claim. Every number is either computed here with shown arithmetic or explicitly labeled a projection with stated assumptions. We make no empirical claims about deployed 6G or quantum hardware.

## 2. Background and Related Work

We group the nine supplied works into three strands: quantum control theory, quantum-network systems engineering, and engineering-methodology analogies from software and web engineering.

**Quantum control and Hamiltonian engineering.** Reference [1] describes strategies for using a semi-classical controller to engineer quantum Hamiltonians in order to solve control problems such as quantum state or process engineering or optimization of observables. This is the theoretical foundation of the in-network approach: the controller is semi-classical, meaning it treats the quantum system as the object being steered while itself running on classical hardware, which is exactly the deployment position QNFO assigns to network elements. Reference [5] introduces a framework for designing Hamiltonian engineering pulse sequences that systematically accounts for higher-order contributions to the Floquet-Magnus expansion, yielding simple, intuitive decoupling rules despite the higher-order contributions naively involving complicated, non-local-in-time decoupling rules despite the higher-order contributions naively involving complicated, non-local-in-time commutators. A network control plane cannot host per-device numerical optimization at microsecond cadence; it needs precompiled, rule-based sequence templates whose error scaling is analytically understood, which is what [5] provides. Reference [2], from a different domain, analyzes the Jupiter–Saturn 2:5 near-commensurability in a fully analytic Hamiltonian planetary theory, with computations for the Sun–Jupiter–Saturn system extending to third order in the masses and eighth degree in the eccentricities and inclinations; these computations reveal an unexpectedly sensitive dependence of the solution on initial data and its likely nonconvergence. We cite it as a cautionary precedent from Hamiltonian methods: analytic perturbation treatments of near-resonant Hamiltonian systems can exhibit extreme sensitivity to initial conditions, and engineered effective Hamiltonians are likewise near-resonant constructions whose validity must be bounded, not assumed.

**Quantum networks as engineered systems.** Reference [4] explores evolving quantum key distribution (QKD) network architecture using a model-based systems-engineering approach, motivated by the growing need for quantum-secure telecommunications that overcome threats to encryption; its entry states that realization of quantum-technology advances in sensors, computing, timing, and communication depends on engineering highly complex systems that integrate quantum devices into existing classical infrastructure. The in-network approach extends this integration agenda one layer down: where [4] treats the QKD network architecture as the system under design, QNFO treats pulse-level control of the quantum endpoints as a service the network must host, schedule, and verify. The supplied summary of [4] is truncated and does not state which specific architecture-evolution results were obtained, so we cite it for its framing rather than for any specific finding.

**Engineering-methodology analogies.** Reference [6] defines Web Engineering as the application of systematic, disciplined, and quantifiable approaches to the development, operation, and maintenance of Web-based applications, framed as both a pro-active approach and a growing body of theoretical and empirical research. The analogy is deliberate: in-network quantum control needs the same discipline — quantifiable approaches to operation and maintenance — that Web Engineering argued the Web needed, applied to control-plane software whose "runtime" is quantum state. Reference [8] addresses software engineering for collective cyber-physical ecosystems, characterized by dense and large networks of devices capable of computation, communication, and interaction with the environment and people; it notes that most research treats such systems as composites, i.e., heterogeneous functional complexes, while recent developments in fields such as self-organization (the entry's text is truncated at this point) are changing that picture. A network of quantum endpoints plus in-network controllers is precisely such a dense cyber-physical ecosystem, and the composite-versus-self-organizing tension maps onto the choice between centrally scheduled and locally autonomous pulse generation. Reference [3] surveys generative AI for software engineering, noting that the ability to automatically check, synthesize, and modify software engineering artifacts promises to revolutionize the field and that over a hundred LLM-based code models have been published since 2021; the entry's text is truncated mid-sentence and supplies no further findings. We invoke it only for the claim that automated artifact synthesis and checking is an active, large-scale capability that could in principle be pointed at pulse-sequence artifacts. Reference [7] argues that large language models for code are advancing fast while evaluation lags behind: current benchmarks focus on narrow tasks and single metrics, hiding critical gaps in robustness, interpretability, fairness, efficiency, and real-world usability, and suffer from inconsistent data engineering practices, limited software engineering context, and widespread contamination issues. This bears directly on the verification problem: if pulse-schedule generators become AI-assisted artifacts, the benchmarking pathologies catalogued in [7] would apply to software whose failure mode is silent decoherence rather than a wrong test result.

Finally, reference [9] is the QNFO program record itself (https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g/); its supplied entry contains only the title and identifier, and this paper is the first substantive text produced under that identifier. All QNFO-specific technical content below is reconstructed from the control model of [1] plus the placement decision implied by the title, and every such reconstruction is stated as an assumption.

## 3. Methods

### 3.1 Service model

We define one new network service, the Hamiltonian Engineering Service (HES), with the following contract. A quantum endpoint $E_q$ (a memory, transducer, or QKD node) exposes: (i) its natural Hamiltonian parameters $H_0(\theta)$, where $\theta$ is a vector of slowly drifting device parameters; (ii) a coherence time $T_2$; and (iii) a pulse-actuation interface accepting control waveforms with minimum pulse width $\tau_p$. An in-network controller $C_n$ (hosted on an edge node or smart network interface card) exposes: (i) a sequence-template library $\mathcal{L}$, each template $L_k$ being a compiled decoupling or recoupling sequence in the sense of [5]; (ii) a scheduler that aligns cycle boundaries with network timing signals; and (iii) a verification module that checks the template's applicability conditions against the reported $\theta$.

The service-level objective is stated as an effective-Hamiltonian error tolerance: over one engineering cycle of duration $T_c$, the stroboscopic dynamics must satisfy

$$\left\| \bar{H} - H_{\mathrm{eff}} \right\| \le \epsilon_c \, \|H_0\|,$$

where $\bar{H}$ is the cycle-averaged Hamiltonian and $\epsilon_c$ is the per-cycle relative error budget.

### 3.2 Timing and fidelity model

Each cycle consists of $n_p$ pulses of width $\tau_p$ separated by idle intervals, so

$$T_c = n_p (\tau_p + \tau_i), \qquad f = \frac{n_p \tau_p}{T_c} = \frac{\tau_p}{\tau_p + \tau_i},$$

with $f$ the actuation duty factor. The controller must issue actuation updates at rate $R_u = 1/\tau_p$ per endpoint; a node hosting $K$ endpoints presents an aggregate update rate $K R_u$.

We adopt a first-order accumulation model in which per-cycle fractional error contributions add linearly over $N_c$ cycles within one coherence window:

$$N_c = \left\lfloor \frac{T_2}{T_c} \right\rfloor, \qquad \epsilon_{\mathrm{tot}} = N_c \, \epsilon_c, \qquad F_{\mathrm{proj}} \approx 1 - \epsilon_{\mathrm{tot}},$$

where $F_{\mathrm{proj}}$ is the projected end-of-window process fidelity. This linear model is conservative relative to coherent-error growth models in the worst case and optimistic relative to models with cancellation; we flag it as a modeling assumption, not a measurement.

### 3.3 Closed-loop latency and re-entry models

We model one in-network feedback cycle as four sequential stages:

$$T_{\mathrm{loop}} = T_s + T_p + T_c' + T_a,$$

where $T_s$ is the sensing/measurement interval, $T_p$ the packet transport latency from sensor to in-network compute node and back, $T_c'$ the compute time for the control update, and $T_a$ the actuation setup time. Re-entry is physically meaningful only if the loop closes within the coherence window:

$$\frac{T_{\mathrm{loop}}}{T_2} \le \eta_{\mathrm{max}},$$

with $\eta_{\mathrm{max}}$ a stated design margin (we take $\eta_{\mathrm{max}} = 0.2$).

For re-entry, let the QNFO stack consist of $N_{\mathrm{tot}}$ components partitioned into a physics-facing layer $\mathcal{P}$ (Hamiltonian targets, pulse sequences, control algorithms) and an infrastructure-facing layer $\mathcal{I}$ (timing distribution, transport, node hardware, qualification). The re-entry reuse ratio is

$$\rho = \frac{N_{\mathrm{reuse}}}{N_{\mathrm{tot}}}, \qquad N_{\mathrm{reuse}} = |\mathcal{P}_{\mathrm{portable}}| + |\mathcal{I}_{\mathrm{portable}}|,$$

where a component is portable if its specification does not reference generation-specific infrastructure parameters. The inventory is enumerated explicitly in Section 4 so that $\rho$ is auditable.

## 4. Analysis

Every input number below is a design assumption of this paper, not an empirical measurement; each is labeled.

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

with margin $\eta_{\mathrm{max}} - \eta = 0.02$ and headroom factor $\eta_{\mathrm{max}}/\eta = 0.2/0.18 \approx 1.111$. The margin is thin: an increase of about $11\%$ in any stage latency exhausts it.

**Derivation 11 — control-plane bandwidth per cycle.**

$$B_{\mathrm{cycle}} = W \cdot N_q = 64 \times 1000 = 6.4 \times 10^{4}\,\mathrm{bits}, \qquad \tau_{\mathrm{tx}} = \frac{6.4 \times 10^{4}}{1.0 \times 10^{11}} = 6.4 \times 10^{-7}\,\mathrm{s}.$$

The transmission time is negligible relative to $T_{\mathrm{loop}}$: $\tau_{\mathrm{tx}}/T_{\mathrm{loop}} = 6.4 \times 10^{-7} / 1.8 \times 10^{-4} \approx 3.56 \times 10^{-3}$, i.e., about $0.36\%$ of the loop budget. Under these assumptions, bandwidth is not the binding constraint; latency staging is.

**Derivation 12 — re-entry reuse ratio.** We enumerate a twelve-component inventory of the QNFO stack (Assumption A15; the partition is ours, since [9]'s supplied context gives no component list):

```
 1  Hamiltonian target specification      P  portable
 2  Pulse-sequence library (cf. [5])      P  portable
 3  Observable-optimization objective (cf. [1]) P portable
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

**Divergent projection — aggregate control bandwidth (labeled projection, not adopted as a headline).** An alternative aggregate model assumes $N = 1000$ nodes, each repeating a 256-bit encoded pulse sequence at $f = 1\,\mathrm{MHz}$, giving

$$B_{\mathrm{total}} = N \times f \times b = 1000 \times 10^{6} \times 256 = 2.56 \times 10^{11}\,\mathrm{bit/s} = 256\,\mathrm{Gb/s},$$

with independent $20\%$ uncertainties on $N$, $f$, and $b$ combined in quadrature:

$$\epsilon = \sqrt{3 \times 0.20^{2}} = \sqrt{0.12} \approx 0.346, \quad B_{\mathrm{total}} \in [256 \times 0.654,\, 256 \times 1.346] \approx [167,\, 345]\,\mathrm{Gb/s}.$$

This projection rests on assumptions (simultaneous per-node repetition at $1\,\mathrm{MHz}$ across 1000 nodes) that are stronger than those of Derivations 5–6; we report it in Appendix A as a documented divergence rather than as a result, together with the claim-attribution table in Appendix B.

## 5. Results

All results below follow from the derivations in Section 4 under the stated assumptions A1–A16; none is an empirical measurement. Where "projected" appears, the projection is the linear accumulation model of Section 3.2 applied to the stated inputs.

| Quantity | Symbol | Value |
|---|---|---|
| Engineering cycle time | $T_c$ | $8 \times 10^{-6}\,\mathrm{s}$ |
| Actuation duty factor | $f$ | $0.5$ |
| Cycles per coherence window | $N_c$ | $125$ |
| Accumulated error over one window | $\epsilon_{\mathrm{tot}}$ | $1.25 \times 10^{-3}$ |
| Projected end-of-window fidelity | $F_{\mathrm{proj}}$ | $\approx 0.99875$ (projection; linear model) |
| Update rate per endpoint | $R_u$ | $2 \times 10^{6}\,\mathrm{s^{-1}}$ |
| Aggregate update rate, $K = 64$ | $K R_u$ | $1.28 \times 10^{8}\,\mathrm{s^{-1}}$ |
| Per-cycle budget for $\epsilon_{\mathrm{tot}} \le 0.01$ | $\epsilon_c^{\mathrm{max}}$ | $8 \times 10^{-5}$ |
| Headroom factor at $\epsilon_c = 10^{-5}$ | — | $8$ |
| Degraded-$T_2$ case ($T_2' = 10^{-4}\,\mathrm{s}$) | $N_c'$, $F_{\mathrm{proj}}'$ | $12$, $\approx 0.99988$ (projection) |
| Closed-loop latency | $T_{\mathrm{loop}}$ | $1.8 \times 10^{-4}\,\mathrm{s}$ |
| Coherence fraction consumed | $\eta$ | $0.18$ (headroom $\approx 1.111$) |
| Per-cycle control payload | $B_{\mathrm{cycle}}$ | $6.4 \times 10^{4}$ bits ($\approx 0.36\%$ of loop budget) |
| Re-entry reuse ratio | $\rho$ | $0.5$ (bound $0.5$–$0.583$) |
| Projected re-qualification effort | $E_{\mathrm{req}}$ | $24$ person-weeks (range $12$–$48$, projection) |

The headline architectural conclusions are: (i) a microsecond-scale engineering cycle is compatible with millisecond-scale coherence under a $10^{-5}$ per-cycle error budget, but the required actuation rate of $2 \times 10^{6}\,\mathrm{s^{-1}}$ per endpoint places the control function in the category of hardware-adjacent network compute, not application-layer software; (ii) under the closed-loop assumptions, latency staging rather than bandwidth is the binding constraint; (iii) re-entry is a half-rebuild: the physics-facing layer is portable, the infrastructure-facing layer — above all the timing plane — is not.

## 6. Discussion

**Limitations of the fidelity model.** The linear error-accumulation model (Section 3.2) is the weakest link. Coherent errors from a repeated non-echoed average-Hamiltonian term can add quadratically or with constructive phase, making $\epsilon_{\mathrm{tot}}$ larger than $N_c \epsilon_c$; conversely, echo-structured sequences can cancel first-order terms, making it smaller. Reference [5] provides exactly the framework — systematic accounting of higher-order Floquet-Magnus contributions — that would replace the linear model with a commutator-based bound, and adopting it is the first remediation step. Until then, $F_{\mathrm{proj}} = 0.99875$ should be read as a budget-allocation statement, not a fidelity prediction.

**Limitations of the parameterization.** Every input number is a design assumption. Real endpoints vary by orders of magnitude in $T_2$, and Derivation 7 shows the results move accordingly. The claim that survives parameter variation is structural: $N_c = T_2/T_c$ and $\epsilon_{\mathrm{tot}} = N_c \epsilon_c$ hold under the model for any inputs, so the architectural conclusion (microsecond cycles, hardware-adjacent control) follows whenever $T_2$ is in the millisecond range and $\epsilon_c$ is at or below the $10^{-4}$ level. The closed-loop model ignores serialization, queueing under load, and error-correction overhead in the control plane; any of these could dominate $T_p$ and $T_c'$. The component inventory behind $\rho = 0.5$ is our reconstruction, not a documented QNFO design, since [9]'s supplied context gives only a title and DOI.

**Failure modes.** Three are foreseen. (i) Synchronization failure: if network timing jitter exceeds a fraction of $T_c = 8\,\mu\mathrm{s}$, cycle boundaries blur and the stroboscopic averaging argument collapses. (ii) Template mismatch: a compiled sequence $L_k$ applied outside its validity domain produces an engineered Hamiltonian that is confidently wrong — the near-resonant sensitivity precedent of [2] warns that analytic Hamiltonian constructions can fail nonconvergently rather than gracefully; we stress that [2] concerns planetary dynamics, not control loops, and the transfer is an analogy. (iii) Verification debt: if sequence templates are synthesized by generative tools in the manner of [3], the evaluation pathologies of [7] — narrow metrics, contamination, hidden robustness gaps — transfer to a setting where the test oracle is quantum state itself, which is far harder to observe than a unit-test suite.

**What would falsify the claims.** The timing/fidelity results are falsified by measured stage latencies, coherence times, or per-cycle errors differing materially from A1–A5. The realizability claim would be falsified by demonstrating that network-grade timing distribution cannot deliver jitter well below $T_c$, or that per-cycle relative errors at the $10^{-5}$ level cannot be achieved by any compiled rule-based sequence family on realistic $H_0$ spectra. The re-entry claim ($\rho = 0.5$) is falsified by a documented component inventory whose portable fraction differs from $6/12$, or by a migration in which the timing and transport planes carried over unchanged. The architectural claim that in-network placement yields operability benefits is falsified if co-located control proves strictly simpler and cheaper at $K = 64$ scale. The transfer of [2]'s sensitivity lesson to control loops could be falsified by showing that closed-loop feedback suppresses exactly the initial-condition sensitivity that open-loop analytic propagation exhibits.

**Open questions.** (i) What is the minimal interface contract between the physics-facing and infrastructure-facing layers that would raise $\rho$ toward $1$? (ii) How should the sequence-template library $\mathcal{L}$ be versioned, certified, and rolled back across a deployed network — the operation-and-maintenance discipline that [6] argued Web applications required? (iii) Can re-entry qualification be expressed as a benchmark that avoids the pathologies catalogued in [7], possibly using AI-assisted artifact checking in the sense of [3] (an explicitly unverified hypothesis; the supplied summary of [3] does not evaluate this use case)? (iv) Can the self-organizing alternatives to composite architectures noted in [8] be applied to pulse scheduling, replacing central schedulers with locally negotiated cycle boundaries?

## 7. Conclusion

We reframed in-network Hamiltonian engineering as a measurable service and re-entry problem. Under explicit assumptions, a $T_c = 8\,\mu\mathrm{s}$ cycle with a $10^{-5}$ per-cycle error budget admits $N_c = 125$ cycles per $T_2 = 1\,\mathrm{ms}$ coherence window with projected accumulated error $1.25 \times 10^{-3}$, at an actuation cost of $2 \times 10^{6}$ updates per second per endpoint; the closed-loop latency budget closes with a thin margin ($\eta = 0.18$ against $\eta_{\mathrm{max}} = 0.2$); and roughly half of the control stack ($\rho = 0.5$, bounded by $0.583$) is portable across infrastructure generations, with a projected re-qualification effort of 24 person-weeks (range 12–48). The framework's value lies less in these particular numbers — design assumptions run through deliberately simple models — than in the budget structure they instantiate: cycle time, per-cycle error, coherence window, and actuation rate are the quantities a 6G architecture must co-manage if quantum devices become infrastructure. The immediate agenda is to replace the linear accumulation model with Floquet-Magnus bounds of the kind developed in [5], to ground the systems argument in the model-based QKD-network methodology of [4], and to build the verification and benchmarking discipline that the software-engineering literature of [3], [6], [7], and [8] shows is always the lagging half of any new engineering capability.

## References

[1] Hamiltonian engineering for quantum systems. arXiv:quant-ph/0602014v2. https://arxiv.org/abs/quant-ph/0602014v2
[2] The Great Inequality In A Hamiltonian Planetary Theory. arXiv:chao-dyn/9311011v2. https://arxiv.org/abs/chao-dyn/9311011v2
[3] Morescient GAI for Software Engineering (Extended Version). arXiv:2406.04710v2. https://arxiv.org/abs/2406.04710v2
[4] Exploration of Evolving Quantum Key Distribution Network Architecture Using Model-Based Systems Engineering. arXiv:2508.15733v1. https://arxiv.org/abs/2508.15733v1
[5] Higher-Order Methods for Hamiltonian Engineering Pulse Sequence Design. arXiv:2303.07374v1. https://arxiv.org/abs/2303.07374v1
[6] Web Engineering. arXiv:cs/0306108v1. https://arxiv.org/abs/cs/0306108v1
[7] Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering. arXiv:2601.21070v1. https://arxiv.org/abs/2601.21070v1
[8] Software Engineering for Collective Cyber-Physical Ecosystems. arXiv:2406.04780v1. https://arxiv.org/abs/2406.04780v1
[9] https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g/. QNFO: In-Network Hamiltonian Engineering for 6G.

## Appendix A. Divergence report

The aggregate control-bandwidth projection of Section 4 (Derivation 12, labeled projection) diverges from the per-endpoint actuation model of Derivations 5–6, and both conventions are documented here rather than silently merged.

- Convention A (adopted for headline results, Derivations 5–6): actuation demand is expressed per endpoint as $R_u = 1/\tau_p = 2 \times 10^{6}\,\mathrm{s^{-1}}$ and per node as $K R_u = 1.28 \times 10^{8}\,\mathrm{s^{-1}}$ for $K = 64$ endpoints (A6). This convention ties bandwidth to the pulse width $\tau_p$ and scales with deployed endpoints.
- Convention B (divergent projection): actuation demand is expressed as an aggregate network load $B_{\mathrm{total}} = N \times f \times b = 1000 \times 10^{6} \times 256 = 2.56 \times 10^{11}\,\mathrm{bit/s} = 256\,\mathrm{Gb/s}$, with independent $20\%$ uncertainties on $N$, $f$, and $b$ combined in quadrature, $\epsilon = \sqrt{3 \times 0.20^{2}} = \sqrt{0.12} \approx 0.346$, giving $B_{\mathrm{total}} \in [167,\, 345]\,\mathrm{Gb/s}$. This convention assumes simultaneous per-node repetition of a 256-bit sequence at $f = 1\,\mathrm{MHz}$ across $N = 1000$ nodes, a stronger assumption than Convention A's.

The disagreement is one of accounting convention, not arithmetic: Convention A measures control-word updates at the endpoint interface, Convention B measures encoded-sequence traffic aggregated over the network. Convention A is adopted in the main text because its inputs (A2, A6) are shared with the timing model; Convention B is retained here as a projection because network-level aggregation may matter for transport planning. The two are not directly comparable without a mapping from $\tau_p$-driven updates to encoded-sequence repetitions, which this paper does not supply.

## Appendix B. Claim attribution

| ID | Claim | Source drafts | Status |
|---|---|---|---|
| C1 | HES service contract: endpoint exposes $H_0(\theta)$, $T_2$, pulse interface; controller exposes template library, scheduler, verification | A, B | CONVERGENT |
| C2 | Timing/fidelity model: $T_c = 8\,\mu\mathrm{s}$, $N_c = 125$, $\epsilon_{\mathrm{tot}} = 1.25 \times 10^{-3}$, $F_{\mathrm{proj}} \approx 0.99875$ under linear accumulation | A, B, C | CONVERGENT |
| C3 | Actuation rates $R_u = 2 \times 10^{6}\,\mathrm{s^{-1}}$ per endpoint, $K R_u = 1.28 \times 10^{8}\,\mathrm{s^{-1}}$ per node ($K = 64$) | A, B | CONVERGENT |
| C4 | Closed-loop latency $T_{\mathrm{loop}} = 1.8 \times 10^{-4}\,\mathrm{s}$, $\eta = 0.18 \le 0.2$ | A, B, C | CONVERGENT |
| C5 | Bandwidth non-binding: $\tau_{\mathrm{tx}}/T_{\mathrm{loop}} \approx 3.56 \times 10^{-3}$ | A, B | CONVERGENT |
| C6 | Re-entry ratio $\rho = 0.5$ from twelve-component inventory, bound $0.5$–$0.583$ | A, B, C | CONVERGENT |
| C7 | Re-qualification effort projection $E_{\mathrm{req}} = 24$ person-weeks (range 12–48) | B, C | CONVERGENT |
| C8 | Aggregate bandwidth projection $256\,\mathrm{Gb/s}$, range $[167, 345]\,\mathrm{Gb/s}$ | C only | SINGLE (retained as labeled projection in Appendix A, not a headline) |
| C9 | Degraded-$T_2$ sensitivity case ($N_c' = 12$, $F_{\mathrm{proj}}' \approx 0.99988$) with counterintuitive direction noted | A, B | CONVERGENT |
| C10 | Error-budget headroom factor $8$ at $\epsilon_c = 10^{-5}$ for $\epsilon_{\mathrm{tot}} \le 0.01$ | B only | SINGLE |
| C11 | Falsification conditions and failure modes (synchronization, template mismatch, verification debt) | A, B, C | CONVERGENT |
| C12 | Analogy to [2]'s near-resonant sensitivity, explicitly flagged as a cross-domain analogy | A, B | CONVERGENT |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2001.02559v1 | Digital Infrastructure in Astrophysics
arXiv:2608.19413v1 | Scientific Visualization as a Collaborative Data Infrastructure
arXiv:2209.07493v1 | Decentralized Infrastructure for (Neuro)science
arXiv:1803.05997v4 | Synergizing Roadway Infrastructure Investment with Digital Infrastructure for Infrastructure-Based Connected Vehicle Applications: Review of Current Status and Future Directions
arXiv:1002.1160v1 | Towards Public Key Infrastructure less authentication in Session Initiation Protocol
arXiv:1710.08708v1 | Confidence intervals for normalised citation counts: Can they delimit underlying research capability?
arXiv:2108.07631v1 | Biologists need modern data infrastructure on campus
arXiv:1404.7565v2 | Investigating SCADA Failures in Interdependent Critical Infrastructure Systems

## QNFO corpus context (Vectorize)

(none retrieved)

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2001.02559v1 | Digital Infrastructure in Astrophysics
  Astronomy, as a field, has long encouraged the development of free, open digital infrastructure (e.g., National Research Council 2010, 2011). Examples range from simple scripts that enable individual scientific research, through software instruments for entire communities, to data reduction pipelines for telescope operations at national facilities. As with the digital infrastructure of our larger 
  Full text (https://arxiv.org/html/2001.02559v1), excerpts of its own sections:
  § 1 Executive Summary: Astronomy, as a field, has long encouraged the development of free, open digital infrastructure ( National Research Council 2010 ; National Research Council 2011 , e.g.,) . Examples range from simple scripts that enable individual scientific research, through software instruments for entire communities, to data reduction pipelines for telescope operations at national facilities. As with the digital infrastructure of our larger society today ( Eghbal 2016 , e.g.,) , nearly all astronomical research relies on free, open source software (FOSS) written and maintained by a small number of developers. And like the physical infrastructure of roads or bridges, digital infrastructure needs regular upkeep and maintenance ( Eghbal 2016 , e.g.,) . In astronomy, financial support for maintaining existing digital infrastructure is generally much harder to secure than funding for developing new digital infrastructures that promise new science. [...]
  § 2 Open Digital Infrastructure in Astrophysics: The “Open Digital Infrastructure in Astrophysics” workshop was held June 4 - 5, 2019 at the Kavli Institute for Theoretical Physics (KITP) at UC Santa Barbara. The workshop’s intent was to highlight open-knowledge digital infrastructures, software instrument communities, metrics for success, developer models, diversity efforts, funding profiles, and sustainability plans. The workshop strove to attain five strategic objectives that align with the Ford and Sloan Foundation’s Digital Infrastructure Research program’s broader goals: $\bullet$ Serve as a focused forum for the principals of free and open source software projects within the fields of astronomy and astrophysics to share knowledge with each other; $\bullet$ Explore innovative topics emerging within their respective software communities; $\bullet$ Discuss emerging best practices across the software projects; $\bullet$ Stimulate thinking on new ways of achieving long-term software sustainability; $\bullet$ Share the aggregate information and experiences in a workshop report. [...]
  § 3 Vision and Execution of the Workshop: The Project Investigators (Timmes, Bildsten, and Townsend) discussed the vision, logistics, and execution of the workshop about once a week on average between February 2019 and June 2019. The vision was to host speakers who spanned a diversity of FOSS projects in stellar astrophysics: $\bullet$ from single developers, through small teams, to large distributed alliance models; $\bullet$ from user communities of a few, through hunderds, to thousands; $\bullet$ from funding models of volunteers, though science/software grants, to Foundations. By March 2019 the PIs converged on a list of potential speakers to ask, and by April 2019 the invited speaker list was finalized. The workshop website, http://cococubed.asu.edu/digital_infrastructure_astronomy , went online in May 2019. [...]
  § 4 Workshop Agenda and Focus Questions: Table 1 lists the invited speakers, their home institution, and their digital infrastructure project. The PIs encouraged the invited speakers to consider presenting quantitative and qualitative information, as appropriate, on the following 18 high-value questions and topics. In these questions, the word “instrument” was intended to be broadly interpreted to mean an open-source software instrument, an open data repository, or an open library. $\bullet$ What does your FOSS instrument do? $\bullet$ Who is your instrument’s community? $\bullet$ How many users does your instrument have, and how is this metric tracked? [...]
[2] arXiv:2608.19413v1 | Scientific Visualization as a Collaborative Data Infrastructure
  Scientific visualization is an active site of infrastructuring with many layers of data and evidential claims. This paper reflects on collaborative Mars geoscience research conducted at the NASA Jet Propulsion Lab, which produced the PIXLISE spectroscopic analysis platform, through a retrospective analysis of a scientific discovery made by the team using PIXLISE. The history of infrastructuring in
  Full text (https://arxiv.org/html/2608.19413v1), excerpts of its own sections:
  § 1. Introduction: While much of visualization research is framed around siloed, individual, cognitive activity  ( van Wijk, 2005 ) , scientific research is in practice both deeply collaborative and remarkably heterogeneous  ( Isenberg et al., 2011 ) . Visualization practitioners collaborate with scientists to create tools that can help experts advance and critique scientific claims particular to an interdisciplinary project. Yet the handoff of ‘partial findings’ between collaborators continues to be a key challenge in visual analytics research  ( Zhao et al., 2018 ) . [...]
  § 2.2. Visualization systems operationalize domain language: In Fig.  1 , we identified four boundary objects specific to Mars geoscience practices which are operationalized in PIXLISE ( P1 ). Two of these correspond roughly to specialized types of plot: the expressions, which form the axes of a mixing diagram; and the correlations, which form the $n^{2}$ edges of an $n$ -element chord diagram. In the PIXLISE interface, mixing diagrams represent each sample point from the context map (a 2D representation of the sample patch in Jezero crater). Sample points in the mixing diagram (which cluster according to their chemical compostion) become selected when the corresponding physical location is ‘lassoed’ on the context map and vice versa, employing the common linked brushing technique  ( Isenberg et al., 2011 ) . Our two exceptions are ‘models’ and ‘evidence’, referring respectively to background knowledge and context drawn from scientific papers; and various materials produced using PIXLISE, especially screenshots and slide decks. [...]
  § 3. Discussion: Scientific visualization systems are a core example of infrastructuring with expert users to produce new insights from their data  ( van Wijk, 2005 ) . This paper describes how the analysis needs of domain experts are identified, triaged, and communicated in the PIXLISE context (P1), and how PIXLISE itself supports handoff between experts with differing backgrounds (P2). Scientific visualization systems regularly encounter the infrastructural tensions identified by Ribes and Finholt  ( Ribes and Finholt, 2009 ) , despite high commitment from their users based at a variety of institutions. The broader visualization literature is also increasingly engaged with questions of rigor in situated research that reflect underlying infrastructuring needs, e.g. iteration, traceability, and reflection  ( Rogers et al., 2026 ) .
  § 4. Conclusion: Collaborative scientific visualization represents a rich set of case studies and relevant methodologies for data-intensive infrastructuring. Prototyping processes such as visualization design studies  ( Crisan et al., 2021 ) pave the way for maintainable infrastructure; as visualization practitioners learn from power users’ workflows, the boundary objects needed by other stakeholders become more crisply delineated and richly supported. On the Mars geoscience team, the source of new scientific knowledge is rarely a singular finding, but instead the consensus that emerges from contentious discussion and independent replication. Visualization plays a special role in making common knowledge , i.e. bringing technical arguments into conversations where they can help discern truths. Although space science is full of difficult problems, these are not wicked problems; it is clear that rocky formations visible on Mars arose through geological processes, and that competing theories of those processes are testable through physical sampling. [...]
[3] arXiv:2209.07493v1 | Decentralized Infrastructure for (Neuro)science
  The most pressing problems in science are neither empirical nor theoretical, but infrastructural. Scientific practice is defined by coproductive, mutually reinforcing infrastructural deficits and incentive systems that everywhere constrain and contort our art of curiosity in service of profit and prestige. Our infrastructural problems are not unique to science, but reflective of the broader logic 
  Full text (https://ar5iv.labs.arxiv.org/html/2209.07493v1), excerpts of its own sections:
  § Submission history: From: Jonny L Saunders [ view email ] [v1] Thu, 1 Sep 2022 01:46:29 UTC (2,142 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Decentralized Infrastructure for (Neuro)science, by Jonny L. Saunders View PDF view license
  § Current browse context:: cs.GL < prev | next > new | recent | 2022-09 Change to browse by: cs
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[4] arXiv:1803.05997v4 | Synergizing Roadway Infrastructure Investment with Digital Infrastructure for Infrastructure-Based Connected Vehicle Applications: Review of Current Status and Future Directions
  The safety, mobility, environmental, energy, and economic benefits of transportation systems, which are the focus of recent connected vehicle (CV) programs, are potentially dramatic. However, realization of these benefits largely hinges on the timely integration of digital technology into upcoming as well as existing transportation infrastructure. CVs must be enabled to broadcast and receive data 
  Full text (https://ar5iv.labs.arxiv.org/html/1803.05997v4), excerpts of its own sections:
  § Submission history: From: Sakib Khan [ view email ] [v1] Tue, 6 Mar 2018 05:50:35 UTC (414 KB) [v2] Thu, 5 Apr 2018 02:10:47 UTC (414 KB) [v3] Mon, 24 Dec 2018 21:23:59 UTC (896 KB) [v4] Mon, 26 Aug 2019 19:29:48 UTC (1,055 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Synergizing Roadway Infrastructure Investment with Digital Infrastructure for Infrastructure-Based Connected Vehicle Applications: Review of Current Status and Future Directions, by Sakib Mahmud Khan and 3 other authors View PDF view license
  § Current browse context:: cs.CY < prev | next > new | recent | 2018-03 Change to browse by: cs cs.GL
  § DBLP - CS Bibliography: listing | bibtex Sakib Mahmud Khan Mashrur Chowdhury Eric A. Morris Lipika Deka Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[5] arXiv:1002.1160v1 | Towards Public Key Infrastructure less authentication in Session Initiation Protocol
  The Session Initiation Protocol (SIP) has become the most predominant protocol for Voice over Internet Protocol (VoIP) signaling. Security of SIP is an important consideration for VoIP communication as the traffic is transmitted over the insecure IP network. And the authentication process in SIP ranges from pre-shared secret based solutions to Public Key Infrastructure (PKI) based solution. Howeve
  Full text (https://ar5iv.labs.arxiv.org/html/1002.1160v1), excerpts of its own sections:
  § Submission history: From: Vishal Goyal [ view email ] [v1] Fri, 5 Feb 2010 09:12:26 UTC (431 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Towards Public Key Infrastructure less authentication in Session Initiation Protocol, by Abdullah Al Hasib and 2 other authors View PDF view license
  § Current browse context:: cs.CR < prev | next > new | recent | 2010-02 Change to browse by: cs
  § DBLP - CS Bibliography: listing | bibtex Abdullah Al Hasib Abdullah Azfar Md. Sarwar Morshed Muhammad Sarwar Jahan Morshed Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[6] arXiv:1710.08708v1 | Confidence intervals for normalised citation counts: Can they delimit underlying research capability?
  Normalised citation counts are routinely used to assess the average impact of research groups or nations. There is controversy over whether confidence intervals for them are theoretically valid or practically useful. In response, this article introduces the concept of a group's underlying research capability to produce impactful research. It then investigates whether confidence intervals could del
  Full text (https://ar5iv.labs.arxiv.org/html/1710.08708v1), excerpts of its own sections:
  § Submission history: From: Mike Thelwall Prof [ view email ] [v1] Tue, 24 Oct 2017 11:26:55 UTC (927 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Confidence intervals for normalised citation counts: Can they delimit underlying research capability?, by Mike Thelwall View PDF view license
  § Current browse context:: cs.DL < prev | next > new | recent | 2017-10 Change to browse by: cs
  § DBLP - CS Bibliography: listing | bibtex Mike Thelwall Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[7] arXiv:2108.07631v1 | Biologists need modern data infrastructure on campus
  Modern tools for biological research, especially microscopy, have rapidly advanced in recent years, which has led to the generation of increasingly large amounts of data on a regular basis. The result is that scientists desperately need state-of-the-art technical infrastructure for raw data storage, transfer, and processing. These scientists currently rely on outdated ways to move and store data, 
  Full text (https://ar5iv.labs.arxiv.org/html/2108.07631v1), excerpts of its own sections:
  § Submission history: From: Andrey Andreev [ view email ] [v1] Tue, 17 Aug 2021 13:54:37 UTC (356 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Biologists need modern data infrastructure on campus, by Andrey Andreev and 4 other authors View PDF view license
  § Current browse context:: q-bio.OT < prev | next > new | recent | 2021-08 Change to browse by: q-bio
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[8] arXiv:1404.7565v2 | Investigating SCADA Failures in Interdependent Critical Infrastructure Systems
  This paper is based on the initial ideas of a PhD proposal which will investigate SCADA failures in physical infrastructure systems. The results will be used to develop a new notation to help risk assessment using dependable computing concepts. SCADA systems are widely used within critical infrastructures to perform system controls and deliver services to linked and dependent systems. Failures in 
  Full text (https://ar5iv.labs.arxiv.org/html/1404.7565v2), excerpts of its own sections:
  § Submission history: From: Razgar Ebrahimy [ view email ] [via Ana Mihut as proxy] [v1] Wed, 30 Apr 2014 00:52:03 UTC (205 KB) [v2] Mon, 19 May 2014 09:14:56 UTC (196 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Investigating SCADA Failures in Interdependent Critical Infrastructure Systems, by Razgar Ebrahimy View PDF view license
  § Current browse context:: cs.SE < prev | next > new | recent | 2014-04 Change to browse by: cs
  § DBLP - CS Bibliography: listing | bibtex Razgar Ebrahimy Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]