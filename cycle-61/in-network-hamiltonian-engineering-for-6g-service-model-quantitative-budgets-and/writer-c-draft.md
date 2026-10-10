# Re-Entry from the QNFO Substrate: Assessing the Reusability of In-Network Hamiltonian Engineering Infrastructure Across 6G Generations

## Abstract

QNFO (In-Network Hamiltonian Engineering for 6G, DOI 10.5281/zenodo.18307388) proposes placing semi-classical Hamiltonian control logic inside the network fabric of a sixth-generation (6G) telecommunications infrastructure. This paper asks a question that any operator or systems engineer must answer before adopting such an architecture: can the underlying 6G infrastructure be re-entered, i.e., reused, re-integrated, and re-qualified when the quantum control payload changes or when the infrastructure itself evolves to a new generation? We formalize re-entry as a measurable reuse ratio over a component inventory of the QNFO control loop, derive the closed-loop latency budget of an in-network Hamiltonian feedback cycle from stated per-stage assumptions, and compute the control-plane bandwidth required per qubit. Under our stated assumptions, the loop latency is $1.8\times10^{-4}$ s against a millisecond-scale coherence budget, and the per-cycle control payload is $6.4\times10^{4}$ bits, occupying $6.4\times10^{-7}$ s of a $10^{11}$ bit/s link. We find that the re-entry question decomposes into a physics-facing layer (pulse sequences, Hamiltonian targets), which is highly portable, and an infrastructure-facing layer (timing, transport, qualification), which is not. We connect this decomposition to systems-engineering literature on quantum network architecture, Hamiltonian pulse design, and large-scale cyber-physical ecosystems, and we identify the open verification problem that re-entry creates.

## 1. Introduction

Sixth-generation network research increasingly treats the network not as a passive transport medium but as an active computational substrate. The QNFO concept (DOI 10.5281/zenodo.18307388) pushes this trend to an extreme: it proposes to perform Hamiltonian engineering — the deliberate reshaping of an effective quantum Hamiltonian by a semi-classical controller — inside the network itself, so that network nodes participate directly in quantum state and process control.

Any such architecture creates a dependency inversion. Traditionally, quantum control hardware sits in the laboratory and the network merely carries results. In QNFO, the network is the control instrument. This raises the question this paper addresses: what happens when the underlying 6G infrastructure must itself be upgraded, replaced, or re-qualified? Can the QNFO control stack be re-entered — carried across into the new infrastructure — without a full redesign? We call this the re-entry problem, by analogy with a spacecraft re-entering an atmosphere: the payload survives, but the vehicle around it must be substantially rebuilt.

We make three contributions. First, we define re-entry operationally as a component-level reuse ratio and apply it to a stated inventory of the QNFO control loop. Second, we derive the closed-loop latency and bandwidth budget of in-network Hamiltonian feedback from explicit per-stage assumptions, giving the operator a quantitative envelope within which re-entry is physically meaningful. Third, we map the re-entry problem onto the systems-engineering literature on quantum network architecture, Hamiltonian pulse-sequence design, and large-scale cyber-physical ecosystems, and we identify the verification gap that re-entry exposes.

The paper is deliberately conservative: every number is either computed here with shown arithmetic or explicitly labeled a projection with stated assumptions. We make no empirical claims about deployed 6G or quantum hardware.

## 2. Background and Related Work

We organize the related work into three strands: Hamiltonian engineering as a control discipline, systems engineering for quantum-networked infrastructure, and the engineering of large-scale software-defined and cyber-physical systems.

**Hamiltonian engineering.** Reference [1] describes strategies for using a semi-classical controller to engineer quantum Hamiltonians in order to solve control problems such as quantum state or process engineering and optimization of observables. This is precisely the control model QNFO inherits: a classical controller shapes a quantum dynamics problem in real time. QNFO's contribution is a placement decision — moving that semi-classical controller into network nodes — and [1] supplies the control-theoretic vocabulary (state engineering, process engineering, observable optimization) in which that placement must be justified. Reference [5] introduces a framework for designing Hamiltonian engineering pulse sequences that systematically accounts for higher-order contributions to the Floquet-Magnus expansion, yielding simple decoupling rules despite the higher-order terms naively involving complicated, non-local-in-time commutators. For the re-entry question, [5] matters because pulse sequences are the most portable artifact in the QNFO stack: a decoupling rule derived from the Floquet-Magnus structure does not depend on which generation of network hardware executes it, although the timing granularity at which it can be executed does.

A cautionary counterpoint comes from [2], which analyzes the Jupiter–Saturn 2:5 near-commensurability in a fully analytic Hamiltonian planetary theory, with computations for the Sun–Jupiter–Saturn system extending to third order in the masses and eighth degree in the eccentricities and inclinations, and finds an unexpectedly sensitive dependence of the solution on initial data and its likely nonconvergence. The lesson we draw for QNFO re-entry is structural: long-horizon analytic Hamiltonian computations can be fragile with respect to initial conditions, so a control stack re-entered onto new infrastructure with even slightly different timing or initialization behavior may produce qualitatively different closed-loop dynamics. The summary of [2] is truncated and gives no further detail on the source of the sensitivity, so we use it only as a qualitative warning, not as a quantitative bound.

**Quantum systems engineering.** Reference [4] explores evolving quantum key distribution (QKD) network architecture using model-based systems engineering, arguing that realization of significant advances in sensors, computing, timing, and communication enabled by quantum technologies depends on engineering highly complex systems that integrate quantum devices into existing classical infrastructure, and considering a systems-engineering approach to address the need for quantum-secure telecommunications. This is the closest methodological relative of the re-entry problem: [4] treats the quantum/classical boundary as a systems-engineering object, and re-entry is exactly a question about the stability of that boundary across infrastructure generations. The supplied summary of [4] is truncated and does not state which specific architecture evolution results were obtained, so we cite it for its framing rather than for any specific finding.

**Large-scale software and cyber-physical systems engineering.** Reference [6] defines Web Engineering as the application of systematic, disciplined and quantifiable approaches to development, operation, and maintenance of Web-based applications, describing it as both a pro-active approach and a growing collection of theoretical and empirical research. Although Web Engineering targets a different substrate, its core claim — that discipline and quantifiability must be applied to operation and maintenance, not only initial development — is the template we adopt for re-entry: re-entry is a maintenance-phase activity and must be made quantifiable. Reference [8] characterizes today's distributed and pervasive computing as addressing large-scale cyber-physical ecosystems, with dense and large networks of devices capable of computation, communication and interaction with the environment and people, and notes that while most research treats these systems as "composites" (heterogeneous functional complexes), recent developments in fields such as self-organization (the summary is truncated here) are changing that picture. QNFO's in-network control nodes are naturally read as members of such an ecosystem rather than as a fixed composite, which is why re-entry across generations is even conceivable: if the ecosystem self-organizes around stable interfaces, components can migrate.

Reference [3] surveys the use of Generative AI to automatically check, synthesize and modify software engineering artifacts, noting that this is one of the most rapidly expanding fields of software engineering research, with over a hundred LLM-based code models published since 2021; the summary is truncated before stating its conclusions about limitations. We invoke [3] only for the hypothesis, clearly labeled as such in Section 6, that AI-assisted artifact checking could partially automate re-entry qualification. Reference [7] argues that large language models for code are advancing fast while evaluation lags behind: current benchmarks focus on narrow tasks and single metrics, hiding critical gaps in robustness, interpretability, fairness, efficiency, and real-world usability, and suffer from inconsistent data engineering practices, limited software engineering context, and widespread contamination issues. Applied to re-entry, [7] warns that any benchmark we construct to certify that a re-entered QNFO stack behaves correctly on new infrastructure will itself inherit narrow-task and contamination pathologies unless designed against exactly these failure modes.

Finally, reference [9] is the QNFO concept document itself (DOI 10.5281/zenodo.18307388); the supplied corpus context gives only its title and identifier and no further technical detail, so throughout this paper QNFO's technical content is reconstructed from the control model of [1] plus the placement decision implied by its title, and every such reconstruction is stated as an assumption.

## 3. Methods

### 3.1 The QNFO control loop model

We reconstruct the QNFO loop from [1]'s semi-classical controller model. The controller observes a quantum register, computes a control update, and applies it via modulated fields. In QNFO the controller logic executes in network nodes. We model one feedback cycle as four sequential stages:

$$T_{\text{loop}} = T_s + T_p + T_c + T_a,$$

where $T_s$ is the sensing/measurement interval, $T_p$ the packet transport latency from sensor to in-network compute node and back, $T_c$ the compute time for the control update in the node, and $T_a$ the actuation setup time. Each stage is an input assumption, stated in Section 4.

### 3.2 Control-plane bandwidth model

Each control update is a control word of $W$ bits per qubit, for $N_q$ qubits, per cycle:

$$B_{\text{cycle}} = W \cdot N_q \quad \text{[bits]},$$

and the link occupancy at rate $R_{\text{link}}$ is

$$\tau_{\text{tx}} = \frac{B_{\text{cycle}}}{R_{\text{link}}}.$$

### 3.3 Re-entry reuse ratio

We define re-entry quantitatively. Let the QNFO stack consist of $N_{\text{tot}}$ components partitioned into a physics-facing layer $\mathcal{P}$ (Hamiltonian targets, pulse sequences, control algorithms) and an infrastructure-facing layer $\mathcal{I}$ (timing distribution, transport, node hardware, qualification procedures). The re-entry reuse ratio for a migration to a new infrastructure generation is

$$\rho = \frac{N_{\text{reuse}}}{N_{\text{tot}}}, \qquad N_{\text{reuse}} = |\mathcal{P}_{\text{portable}}| + |\mathcal{I}_{\text{portable}}|.$$

A component is portable if its specification does not reference generation-specific infrastructure parameters. We enumerate the inventory explicitly in Section 4 so that $\rho$ is auditable.

### 3.4 Coherence feasibility criterion

Re-entry is physically meaningful only if the loop closes within the coherence window. We use the criterion

$$\frac{T_{\text{loop}}}{T_2} \le \eta_{\max},$$

with $T_2$ the dephasing time of the register and $\eta_{\max}$ a stated design margin. We take $\eta_{\max} = 0.2$ as the requirement that at most one fifth of the coherence window is consumed per feedback cycle.

## 4. Analysis

Every input number below is an assumption of this paper, not a measurement; each is labeled with its role.

**Inputs.**
- $T_s = 1.0\times10^{-4}$ s (assumed sensing interval for a millisecond-class register; Assumption A1).
- $T_p = 2.0\times10^{-5}$ s (assumed one-hop edge round-trip transport latency; Assumption A2).
- $T_c = 5.0\times10^{-5}$ s (assumed in-network compute time for one control update; Assumption A3).
- $T_a = 1.0\times10^{-5}$ s (assumed actuation setup time; Assumption A4).
- $T_2 = 1.0\times10^{-3}$ s (assumed dephasing time of the controlled register; Assumption A5).
- $W = 64$ bits per qubit per control word (assumed word size; Assumption A6).
- $N_q = 1000$ qubits (assumed register size; Assumption A7).
- $R_{\text{link}} = 1.0\times10^{11}$ bit/s (assumed link rate of the in-network fabric; Assumption A8).
- $\eta_{\max} = 0.2$ (design margin; Assumption A9).

**Derivation 1: loop latency.**

$$T_{\text{loop}} = T_s + T_p + T_c + T_a = 1.0\times10^{-4} + 2.0\times10^{-5} + 5.0\times10^{-5} + 1.0\times10^{-5} = 1.8\times10^{-4}\ \text{s}.$$

**Derivation 2: coherence fraction.**

$$\eta = \frac{T_{\text{loop}}}{T_2} = \frac{1.8\times10^{-4}}{1.0\times10^{-3}} = 0.18.$$

Since $0.18 \le \eta_{\max} = 0.2$, the assumed configuration satisfies the feasibility criterion, with margin $\eta_{\max} - \eta = 0.02$. This is tight: a $12\%$ increase in any stage latency (since $0.18 \times 1.111\ldots \approx 0.2$, i.e., a multiplicative headroom factor of $\eta_{\max}/\eta = 0.2/0.18 \approx 1.111$) exhausts the margin.

**Derivation 3: control-plane bandwidth.**

$$B_{\text{cycle}} = W \cdot N_q = 64 \times 1000 = 6.4\times10^{4}\ \text{bits per cycle}.$$

$$\tau_{\text{tx}} = \frac{B_{\text{cycle}}}{R_{\text{link}}} = \frac{6.4\times10^{4}}{1.0\times10^{11}} = 6.4\times10^{-7}\ \text{s}.$$

The transmission time is negligible relative to $T_{\text{loop}}$: $\tau_{\text{tx}}/T_{\text{loop}} = 6.4\times10^{-7} / 1.8\times10^{-4} \approx 3.56\times10^{-3}$, i.e., about $0.36\%$ of the loop budget. Bandwidth is therefore not the binding constraint under these assumptions; latency staging is.

**Derivation 4: re-entry reuse ratio.** We enumerate a twelve-component inventory of the QNFO stack (Assumption A10; the partition is ours, since [9]'s supplied context gives no component list):

| # | Component | Layer | Portable across 6G generations? |
|---|-----------|-------|-------------------------------|
| 1 | Hamiltonian target specification | $\mathcal{P}$ | Yes |
| 2 | Pulse-sequence library (Floquet-Magnus rules, cf. [5]) | $\mathcal{P}$ | Yes |
| 3 | Observable-optimization objective (cf. [1]) | $\mathcal{P}$ | Yes |
| 4 | Control-update algorithm | $\mathcal{P}$ | Yes |
| 5 | Control-word encoding | $\mathcal{P}$ | Yes |
| 6 | Timing distribution service | $\mathcal{I}$ | No (generation-specific clock plane) |
| 7 | Transport/queueing configuration | $\mathcal{I}$ | No |
| 8 | In-network compute node image | $\mathcal{I}$ | No |
| 9 | Sensor/actuator drivers | $\mathcal{I}$ | No |
| 10 | Latency budget manifest | $\mathcal{I}$ | No (must be re-derived) |
| 11 | Qualification test suite | $\mathcal{I}$ | Partial — counted No (conservative) |
| 12 | Monitoring/telemetry schema | $\mathcal{I}$ | Yes |

Portable count: components 1–5 and 12 give $N_{\text{reuse}} = 6$; $N_{\text{tot}} = 12$; therefore

$$\rho = \frac{6}{12} = 0.5.$$

Counting component 11 as portable (optimistic reading) would give $\rho = 7/12 \approx 0.583$; we report the conservative $\rho = 0.5$ as the headline and the optimistic value as a bound: $0.5 \le \rho \le 0.583$.

**Derivation 5: re-qualification cost scaling (projection).** If re-qualification effort per non-portable component is $e$ person-weeks (Assumption A11, $e = 4$), then

$$E_{\text{req}} = e \cdot (N_{\text{tot}} - N_{\text{reuse}}) = 4 \times 6 = 24\ \text{person-weeks}.$$

This is a projection under A11, not a measurement; its uncertainty is linear in $e$, so $E_{\text{req}} \in [12, 48]$ person-weeks for $e \in [2, 8]$.

## 5. Results

All results below follow from the derivations in Section 4 under the stated assumptions A1–A11; none is an empirical measurement.

- **R1.** The assumed QNFO feedback loop closes in $T_{\text{loop}} = 1.8\times10^{-4}$ s (Derivation 1).
- **R2.** This consumes $\eta = 0.18$ of the assumed $T_2 = 1.0\times10^{-3}$ s coherence window, satisfying the $\eta_{\max} = 0.2$ criterion with a headroom factor of only $\approx 1.111$ (Derivation 2).
- **R3.** The per-cycle control payload is $B_{\text{cycle}} = 6.4\times10^{4}$ bits, occupying $\tau_{\text{tx}} = 6.4\times10^{-7}$ s, i.e., $\approx 0.36\%$ of the loop budget at the assumed $R_{\text{link}} = 1.0\times10^{11}$ bit/s (Derivation 3). Latency staging, not bandwidth, is the binding constraint.
- **R4.** The conservative re-entry reuse ratio is $\rho = 0.5$, bounded above by $\rho \le 0.583$ under the optimistic counting of the qualification suite (Derivation 4).
- **R5.** Projected re-qualification effort is $E_{\text{req}} = 24$ person-weeks, with a labeled projection range of $[12, 48]$ person-weeks under $e \in [2,8]$ person-weeks per non-portable component (Derivation 5).

## 6. Discussion

**Interpretation.** The re-entry question decomposes cleanly. The physics-facing layer — Hamiltonian targets, pulse sequences in the spirit of [5], control objectives in the sense of [1] — carries across infrastructure generations essentially unchanged, because its specification is in terms of quantum dynamics, not network hardware. The infrastructure-facing layer does not: timing distribution, transport configuration, node images, and latency budgets are all functions of the specific 6G generation, and our inventory assigns six of twelve components to it. The headline $\rho = 0.5$ says that re-entry is a half-rebuild, not a lift-and-shift.

**The fragility warning.** The result of [2] — sensitive dependence of an analytic Hamiltonian solution on initial data, with likely nonconvergence — is the strongest argument against complacency. A re-entered control stack whose timing plane differs by even small amounts from the generation it was designed for is a Hamiltonian feedback system running on perturbed initial conditions. Our latency margin (headroom factor $\approx 1.111$) means that plausible inter-generation timing differences could push the loop past $\eta_{\max}$, and the qualitative lesson of [2] is that the resulting dynamics may not degrade gracefully. We stress that [2] concerns planetary dynamics, not control loops; the transfer is an analogy, and we label it as such.

**The verification gap.** Reference [7] identifies benchmark pathologies — narrow tasks, single metrics, contamination — that any re-entry certification suite would risk inheriting. A qualification suite built on one infrastructure generation and replayed on another is precisely a contaminated benchmark unless the test data and timing envelopes are regenerated. Reference [3]'s observation that GAI can automatically check, synthesize and modify software engineering artifacts suggests a hypothesis, which we state explicitly as an unverified hypothesis: AI-assisted differential checking between the old and new qualification runs could reduce the $E_{\text{req}}$ projection. The supplied summary of [3] is truncated and does not evaluate this use case, so we offer no quantitative estimate for it.

**Self-critique and failure modes.** First, every number rests on assumptions A1–A11; if the true $T_2$ is $1.0\times10^{-2}$ s the feasibility problem vanishes, and if it is $1.0\times10^{-4}$ s the loop cannot close at all ($\eta = 1.8 > 1$). Second, the component inventory (A10) is ours, not QNFO's: the supplied context for [9] gives only a title and DOI, so $\rho = 0.5$ is a property of our reconstruction, not of the documented QNFO design. Third, the four-stage latency model ignores serialization, queueing under load, and error-correction overhead in the control plane; any of these could dominate $T_p$ and $T_c$. Fourth, the transfer of [2]'s sensitivity lesson to control loops is analogical and could be falsified by showing that closed-loop feedback suppresses exactly the initial-condition sensitivity that open-loop analytic propagation exhibits. Fifth, the projection in R5 assumes linear cost scaling in component count; a fixed re-qualification overhead would change the scaling to $E_{\text{req}} = E_0 + e\,(N_{\text{tot}} - N_{\text{reuse}})$ with unknown $E_0$.

**What would falsify our claims.** R1–R3 are falsified by measured stage latencies or coherence times differing materially from A1–A5. R4 is falsified by a documented QNFO component inventory whose portable fraction differs from $6/12$. The central qualitative claim — that re-entry is a half-rebuild dominated by the infrastructure layer — is falsified by a migration in which the timing and transport planes carried over unchanged, which would require generation-stable interfaces of the kind the ecosystem view of [8] anticipates and the model-based approach of [4] is designed to specify.

**Open questions.** (i) What is the minimal interface contract between the physics-facing and infrastructure-facing layers that would raise $\rho$ toward $1$? (ii) Can re-entry qualification be expressed as a benchmark that avoids the pathologies catalogued in [7]? (iii) Does the quantifiable-maintenance discipline of [6] extend to control-plane artifacts whose correctness criterion is physical (coherence) rather than functional?

## 7. Conclusion

We framed the re-entry of the 6G infrastructure underlying QNFO as a measurable reuse problem and found, under explicit assumptions, that the loop latency budget closes with a thin margin ($\eta = 0.18$ against $\eta_{\max} = 0.2$), that bandwidth is not binding ($\approx 0.36\%$ loop occupancy), and that roughly half of the control stack ($\rho = 0.5$, bounded by $0.583$) is portable across infrastructure generations, with a projected re-qualification effort of 24 person-weeks (range 12–48). The binding constraint on re-entry is the infrastructure-facing layer, above all the timing plane. The principal open deliverable is an interface contract between the two layers, designed with the benchmark pathologies of [7] and the systems-engineering discipline of [4] and [6] in view.

## References

[1] arXiv:quant-ph/0602014v2 | Hamiltonian engineering for quantum systems
[2] arXiv:chao-dyn/9311011v2 | The Great Inequality In A Hamiltonian Planetary Theory
[3] arXiv:2406.04710v2 | Morescient GAI for Software Engineering (Extended Version)
[4] arXiv:2508.15733v1 | Exploration of Evolving Quantum Key Distribution Network Architecture Using Model-Based Systems Engineering
[5] arXiv:2303.07374v1 | Higher-Order Methods for Hamiltonian Engineering Pulse Sequence Design
[6] arXiv:cs/0306108v1 | Web Engineering
[7] arXiv:2601.21070v1 | Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering
[8] arXiv:2406.04780v1 | Software Engineering for Collective Cyber-Physical Ecosystems
[9] QNFO: In-Network Hamiltonian Engineering for 6G | DOI 10.5281/zenodo.18307388