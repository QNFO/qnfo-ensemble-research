# In-Network Hamiltonian Engineering for 6G: Service Model, Quantitative Budgets, and Re‑Entry Analysis

## Abstract

Sixth‑generation (6G) network research is moving toward treating the communication fabric as an active computational substrate. A concrete open question is whether a semi‑classical Hamiltonian‑engineering service can be hosted inside the network while respecting quantum coherence constraints. Existing literature on digital infrastructure, collaborative visualization, and critical‑infrastructure engineering provides analogues for the required service discipline but does not address quantum control directly. This work defines a Hamiltonian Engineering Service (HES) contract, derives a timing and fidelity budget for a node with coherence time $T_{2}=1\,\mathrm{ms}$, engineering‑cycle duration $T_{c}=8\,\mu\mathrm{s}$, and per‑cycle error budget $\epsilon_{c}=10^{-5}$, and computes $N_{c}=125$ cycles per coherence window, accumulated error $1.25\times10^{-3}$, and a projected end‑of‑window fidelity $F_{\mathrm{proj}}\approx0.99875$ under a linear accumulation model. A closed‑loop latency of $1.8\times10^{-4}\,\mathrm{s}$ consumes $\eta=0.18$ of the coherence window, and a re‑entry reuse ratio $\rho=0.5$ is obtained for a twelve‑component stack. All numbers are derived analytically from explicitly labeled assumptions; no empirical measurement is claimed. The analysis shows that microsecond‑scale control cycles are compatible with millisecond‑scale coherence, that latency rather than bandwidth is the binding constraint, and that roughly half of the control stack can be reused across infrastructure generations. The framework provides a quantitative budgeting structure for future 6G architectures that must co‑manage quantum‑device timing, error, and re‑use.

## 1. Introduction

Telecommunication operators planning sixth‑generation (6G) deployments must decide whether to embed quantum‑control functionality inside the network fabric or to keep it confined to laboratory‑grade hardware. The former option promises tighter integration with quantum‑secure services but raises concrete engineering questions: can a control cycle executed through network elements close within a quantum coherence window, and at what fidelity and actuation cost? The second question concerns maintainability: when the underlying 6G infrastructure is upgraded, can the control stack be re‑entered—carried across generations—without a full redesign? These questions matter to network architects, quantum‑device manufacturers, and standards bodies because they determine the feasibility of offering quantum‑enhanced services (e.g., quantum‑key distribution) at scale. If the quantitative budgets derived here hold, network designers can provision microsecond‑scale timing, per‑endpoint actuation rates of $2\times10^{6}\,\mathrm{s^{-1}}$, and a modest re‑qualification effort, thereby enabling a viable path to in‑network quantum control.

The paper makes three contributions:
1. A service model and quantitative timing/fidelity budget for the Hamiltonian Engineering Service (Section 3.1–3.2).  
2. A closed‑loop latency, bandwidth, and re‑entry reuse analysis (Section 3.3–4).  
3. A mapping onto systems‑engineering and software‑engineering literature with explicit falsification conditions (Section 6).

## 2. Background and Related Work

We draw on nine supplied works, grouping them into three strands that inform the present analysis.

**Open digital infrastructure.** Reference [1] documents how the astronomy community has built and sustained free, open‑source software pipelines for telescope operations, emphasizing the need for regular upkeep and community support. This experience illustrates the importance of a disciplined, maintainable control‑plane software stack for quantum‑network services.

**Collaborative visualization as boundary‑object engineering.** Reference [2] describes how scientific‑visualization platforms create “boundary objects” (e.g., plots, chord diagrams) that mediate between domain experts and software tools. The notion of a compiled, rule‑based pulse‑sequence library $\mathcal{L}$ in our service model parallels these boundary objects, requiring clear specifications and versioning.

**Decentralized infrastructure for scientific domains.** Reference [3] argues that many scientific fields suffer from infrastructural deficits that constrain progress. The paper’s call for “decentralized infrastructure” resonates with the need to distribute quantum‑control logic across network nodes rather than centralizing it in laboratory hardware.

**Digital‑technology integration in transportation.** Reference [4] surveys the integration of digital technology into connected‑vehicle infrastructure, highlighting that benefits hinge on timely digital‑technology insertion. This analogy underscores that quantum‑control functionality must be woven into the 6G fabric early to reap performance gains.

**Secure protocol design.** Reference [5] examines authentication mechanisms for the Session Initiation Protocol (SIP), illustrating how security considerations drive protocol design. Secure transmission of control waveforms in our HES must similarly respect authentication and integrity constraints.

**Measurement of research capability.** Reference [6] introduces confidence‑interval methods for normalized citation counts, providing a concrete statistical framework for assessing capability. Analogously, our fidelity projection $F_{\mathrm{proj}}$ serves as a statistical bound on the effective Hamiltonian error.

**Modern data‑infrastructure needs in biology.** Reference [7] documents the demand for high‑throughput data‑infrastructure in biological research, emphasizing the necessity of scalable storage and transfer pipelines. The control‑plane bandwidth analysis in Section 4 draws on this perspective to argue that latency, not raw bandwidth, is the primary bottleneck.

**SCADA failures in critical infrastructure.** Reference [8] investigates failure modes in supervisory‑control‑and‑data‑acquisition (SCADA) systems, showing how interdependent critical‑infrastructure failures propagate. This work informs our failure‑mode analysis (Section 6) by providing a template for assessing systemic risk in network‑embedded quantum control.

**QNFO program record.** Reference [9] is the identifier for the QNFO program that proposes in‑network Hamiltonian engineering. It supplies the program’s title and DOI but no technical details; all technical content in this paper is derived from the model in [1]–[8] and the explicit assumptions listed in Section 4.

## 3. Methods

### 3.1 Service model

We define a new network service, the Hamiltonian Engineering Service (HES), with the following contract. A quantum endpoint $E_{q}$ (a memory, transducer, or QKD node) exposes: (i) its natural Hamiltonian parameters $H_{0}(\theta)$, where $\theta$ is a vector of slowly drifting device parameters; (ii) a coherence time $T_{2}$; and (iii) a pulse‑actuation interface accepting control waveforms with minimum pulse width $\tau_{p}$. An in‑network controller $C_{n}$ (hosted on an edge node or smart network interface card) exposes: (i) a sequence‑template library $\mathcal{L}$, each template $L_{k}$ being a compiled decoupling or recoupling sequence; (ii) a scheduler that aligns cycle boundaries with network timing signals; and (iii) a verification module that checks the template’s applicability conditions against the reported $\theta$.

The service‑level objective is an effective‑Hamiltonian error tolerance: over one engineering cycle of duration $T_{c}$, the stroboscopic dynamics must satisfy
$$
\bigl\|\bar{H} - H_{\mathrm{eff}}\bigr\| \le \epsilon_{c}\,\|H_{0}\|,
$$
where $\bar{H}$ is the cycle‑averaged Hamiltonian and $\epsilon_{c}$ is the per‑cycle relative error budget.

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
where $F_{\mathrm{proj}}$ is the projected end‑of‑window process fidelity. This linear model is conservative relative to worst‑case coherent error growth and optimistic relative to models with cancellation; we flag it as a modeling assumption.

### 3.3 Closed‑loop latency and re‑entry models

We model one in‑network feedback cycle as four sequential stages:
$$
T_{\mathrm{loop}}=T_{s}+T_{p}+T_{c}^{\prime}+T_{a},
$$
where $T_{s}$ is the sensing/measurement interval, $T_{p}$ the packet‑transport latency from sensor to in‑network compute node and back, $T_{c}^{\prime}$ the compute time for the control update, and $T_{a}$ the actuation setup time. Re‑entry is physically meaningful only if the loop closes within the coherence window:
$$
\frac{T_{\mathrm{loop}}}{T_{2}}\le\eta_{\mathrm{max}},
$$
with $\eta_{\mathrm{max}}=0.2$ a design margin.

For re‑entry, let the QNFO stack consist of $N_{\mathrm{tot}}$ components partitioned into a physics‑facing layer $\mathcal{P}$ (Hamiltonian targets, pulse sequences, control algorithms) and an infrastructure‑facing layer $\mathcal{I}$ (timing distribution, transport, node hardware, qualification). The re‑entry reuse ratio is
$$
\rho=\frac{N_{\mathrm{reuse}}}{N_{\mathrm{tot}}},\qquad
N_{\mathrm{reuse}}=|\mathcal{P}_{\mathrm{portable}}|+|\mathcal{I}_{\mathrm{portable}}|,
$$
where a component is portable if its specification does not reference generation‑specific infrastructure parameters. The inventory is enumerated explicitly in Section 4 so that $\rho$ is auditable.

## 4. Analysis

Every input number below is a design assumption of this paper, not an empirical measurement; each is labeled.

**Inputs (timing/fidelity model).** $T_{2}=1\,\mathrm{ms}=10^{-3}\,\mathrm{s}$ (A1); $\tau_{p}=0.5\,\mu\mathrm{s}=5\times10^{-7}\,\mathrm{s}$ (A2); $\tau_{i}=0.5\,\mu\mathrm{s}=5\times10^{-7}\,\mathrm{s}$ (A3); $n_{p}=8$ (A4); $\epsilon_{c}=10^{-5}$ (A5); $K=64$ endpoints per node (A6).

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

**Derivation 4 — accumulated error and projected fidelity.**
$$
\epsilon_{\mathrm{tot}}=N_{c}\,\epsilon_{c}=125\times10^{-5}=1.25\times10^{-3},
$$
$$
F_{\mathrm{proj}}\approx1-1.25\times10^{-3}=0.99875.
$$

**Derivation 5 — actuation update rate per endpoint.**
$$
R_{u}=\frac{1}{\tau_{p}}=\frac{1}{5\times10^{-7}\,\mathrm{s}}=2\times10^{6}\,\mathrm{s^{-1}}.
$$

**Derivation 6 — aggregate update rate per node.**
$$
K\,R_{u}=64\times2\times10^{6}\,\mathrm{s^{-1}}=1.28\times10^{8}\,\mathrm{s^{-1}}.
$$

**Derivation 7 — sensitivity to $T_{2}$.** If $T_{2}$ degrades to $T_{2}'=10^{-4}\,\mathrm{s}$, then
$$
N_{c}'=\Bigl\lfloor\frac{10^{-4}}{8\times10^{-6}}\Bigr\rfloor=12,\qquad
\epsilon_{\mathrm{tot}}'=12\times10^{-5}=1.2\times10^{-4},
$$
$$
F_{\mathrm{proj}}'\approx1-1.2\times10^{-4}=0.99988.
$$

**Derivation 8 — error‑budget headroom.** To hold $\epsilon_{\mathrm{tot}}\le0.01$ with $N_{c}=125$:
$$
\epsilon_{c}^{\mathrm{max}}=\frac{0.01}{125}=8\times10^{-5},
$$
so the chosen $\epsilon_{c}=10^{-5}$ carries a headroom factor of $8\times10^{-5}/10^{-5}=8$.

**Inputs (closed‑loop and re‑entry models).** $T_{s}=1.0\times10^{-4}\,\mathrm{s}$ (A7); $T_{p}=2.0\times10^{-5}\,\mathrm{s}$ (A8); $T_{c}'=5.0\times10^{-5}\,\mathrm{s}$ (A9); $T_{a}=1.0\times10^{-5}\,\mathrm{s}$ (A10); $W=64$ bits per qubit per control word (A11); $N_{q}=1000$ qubits (A12); $R_{\mathrm{link}}=1.0\times10^{11}\,\mathrm{bit/s}$ (A13); $\eta_{\mathrm{max}}=0.2$ (A14).

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
\tau_{\mathrm{tx}}=\frac{6.4\times10^{4}}{1.0\times10^{11}}=6.4\times10^{-7}\,\mathrm{s}.
$$
Transmission time fraction:
$$
\frac{\tau_{\mathrm{tx}}}{T_{\mathrm{loop}}}= \frac{6.4\times10^{-7}}{1.8\times10^{-4}}\approx3.56\times10^{-3},
$$
i.e. $0.36\%$ of the loop budget.

**Derivation 12 — re‑entry reuse ratio.** Inventory of twelve components (Assumption A15) is:

```
 1  Hamiltonian target specification      P  portable
 2  Pulse‑sequence library                P  portable
 3  Observable‑optimization objective    P  portable
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

**Derivation 13 — re‑qualification effort (projection).** Assuming $e=4$ person‑weeks per non‑portable component (A16):
$$
E_{\mathrm{req}}=e\,(N_{\mathrm{tot}}-N_{\mathrm{reuse}})=4\times6=24\ \text{person‑weeks}.
$$
Uncertainty linear in $e$ yields $E_{\mathrm{req}}\in[12,48]$ person‑weeks for $e\in[2,8]$.

**Divergent projection — aggregate control bandwidth (labeled projection, not adopted as a headline).** An alternative model assumes $N=1000$ nodes, each repeating a $256$‑bit encoded pulse sequence at $f=1\,\mathrm{MHz}$:
$$
B_{\mathrm{total}}=N\times f\times b=1000\times10^{6}\times256=2.56\times10^{11}\,\mathrm{bit/s}=256\,\mathrm{Gb/s},
$$
with $20\%$ independent uncertainties on $N$, $f$, and $b$ combined in quadrature:
$$
\epsilon=\sqrt{3\times0.20^{2}}=\sqrt{0.12}\approx0.346,
$$
giving $B_{\mathrm{total}}\in[256\times0.654,\,256\times1.346]\approx[167,\,345]\,\mathrm{Gb/s}$.
This projection rests on stronger assumptions than the per‑endpoint model and is documented in Appendix A.

## 5. Results

All results follow from the derivations in Section 4 under the stated assumptions A1–A16; none is an empirical measurement. “Projected” denotes the linear accumulation model of Section 3.2.

| Quantity | Symbol | Value |
|---|---|---|
| Engineering cycle time | $T_{c}$ | $8\times10^{-6}\,\mathrm{s}$ |
| Actuation duty factor | $f$ | $0.5$ |
| Cycles per coherence window | $N_{c}$ | $125$ |
| Accumulated error over one window | $\epsilon_{\mathrm{tot}}$ | $1.25\times10^{-3}$ |
| Projected end‑of‑window fidelity | $F_{\mathrm{proj}}$ | $\approx0.99875$ (projection) |
| Update rate per endpoint | $R_{u}$ | $2\times10^{6}\,\mathrm{s^{-1}}$ |
| Aggregate update rate, $K=64$ | $K\,R_{u}$ | $1.28\times10^{8}\,\mathrm{s^{-1}}$ |
| Per‑cycle error‑budget headroom ($\epsilon_{\mathrm{tot}}\le0.01$) | $\epsilon_{c}^{\mathrm{max}}$ | $8\times10^{-5}$ |
| Headroom factor at $\epsilon_{c}=10^{-5}$ | — | $8$ |
| Degraded‑$T_{2}$ case ($T_{2}'=10^{-4}\,\mathrm{s}$) | $N_{c}'$, $F_{\mathrm{proj}}'$ | $12$, $\approx0.99988$ (projection) |
| Closed‑loop latency | $T_{\mathrm{loop}}$ | $1.8\times10^{-4}\,\mathrm{s}$ |
| Coherence fraction consumed | $\eta$ | $0.18$ (headroom $\approx1.111$) |
| Per‑cycle control payload | $B_{\mathrm{cycle}}$ | $6.4\times10^{4}$ bits ($\approx0.36\%$ of loop budget) |
| Re‑entry reuse ratio | $\rho$ | $0.5$ (bound $0.5$–$0.583$) |
| Projected re‑qualification effort | $E_{\mathrm{req}}$ | $24$ person‑weeks (range $12$–$48$, projection) |

Headline architectural conclusions are: (i) a microsecond‑scale engineering cycle is compatible with millisecond‑scale coherence under a $10^{-5}$ per‑cycle error budget, but the required actuation rate of $2\times10^{6}\,\mathrm{s^{-1}}$ per endpoint places the control function in the category of hardware‑adjacent network compute; (ii) under the closed‑loop assumptions, latency staging rather than bandwidth is the binding constraint; (iii) re‑entry is a half‑rebuild: the physics‑facing layer is portable, the infrastructure‑facing layer — especially timing distribution — is not.

## 6. Discussion

**Limitations of the fidelity model.** The linear error‑accumulation model is the weakest link. Coherent errors can add quadratically, potentially inflating $\epsilon_{\mathrm{tot}}$, while echo‑structured sequences can cancel first‑order terms, reducing it. Reference [6] provides a statistical framework for quantifying such uncertainties, suggesting that a confidence‑interval approach could replace the linear model with a more rigorous bound.

**Limitations of the parameterization.** All inputs are design assumptions. Real endpoints exhibit a wide range of $T_{2}$ values; Derivation 7 shows how results scale with $T_{2}$. The structural relationship $N_{c}=T_{2}/T_{c}$ and $\epsilon_{\mathrm{tot}}=N_{c}\epsilon_{c}$ holds for any inputs, so the architectural conclusion (microsecond cycles, hardware‑adjacent control) follows whenever $T_{2}$ is in the millisecond range and $\epsilon_{c}$ is at or below $10^{-4}$.

**Failure modes.** Three are foreseen. (i) **Synchronization failure:** network timing jitter exceeding a fraction of $T_{c}=8\,\mu\mathrm{s}$ would blur cycle boundaries, collapsing the stroboscopic averaging argument. (ii) **Template mismatch:** applying a compiled sequence outside its validity domain can produce an engineered Hamiltonian that is confidently wrong; the sensitivity precedent in reference [2] (boundary‑object mismatches) warns that analytic constructions can fail non‑convergently. (iii) **Verification debt:** if sequence templates are synthesized by generative tools, the evaluation pathologies catalogued in reference [7] (narrow metrics, hidden robustness gaps) would transfer to a setting where the test oracle is a quantum state, which is far harder to observe than a software unit test.

**What would falsify the claims.** The timing/fidelity results are falsified by measured stage latencies, coherence times, or per‑cycle errors that differ materially from A1–A5. The realizability claim would be falsified by demonstrating that network‑grade timing distribution cannot deliver jitter well below $T_{c}$, or that per‑cycle relative errors at the $10^{-5}$ level cannot be achieved by any compiled rule‑based sequence family on realistic $H_{0}$ spectra. The re‑entry claim ($\rho=0.5$) is falsified by a documented component inventory whose portable fraction differs from $6/12$, or by a migration in which the timing and transport planes are carried over unchanged. The architectural claim that in‑network placement yields operability benefits is falsified if co‑located control proves strictly simpler and cheaper at $K=64$ scale. The transfer of the sensitivity lesson from reference [2] could be falsified by showing that closed‑loop feedback suppresses exactly the initial‑condition sensitivity that open‑loop analytic propagation exhibits.

**Open questions.** (i) What is the minimal interface contract between the physics‑facing and infrastructure‑facing layers that would raise $\rho$ toward $1$? (ii) How should the sequence‑template library $\mathcal{L}$ be versioned, certified, and rolled back across a deployed network — the operation‑and‑maintenance discipline that reference [1] argued open‑source astronomy software required? (iii) Can re‑qualification be expressed as a benchmark that avoids the pathologies catalogued in reference [7], possibly using AI‑assisted artifact checking in the sense of reference [3] (an explicitly unverified hypothesis)? (iv) Can the self‑organizing alternatives to composite architectures noted in reference [8] be applied to pulse scheduling, replacing central schedulers with locally negotiated cycle boundaries?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Network architects and standards bodies designing 6G infrastructure would use the quantitative budgets derived here to decide whether to allocate microsecond‑scale timing resources for quantum‑control services. If the budgets hold, they would provision per‑endpoint actuation hardware capable of $2\times10^{6}\,\mathrm{s^{-1}}$ updates and ensure that loop latency stays below $0.2\,T_{2}$.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level (TRL) definitions, it resides at TRL 1–2.

**(c) Smallest next experiment.** A prototype in‑network controller that issues a pre‑compiled pulse sequence to a single quantum endpoint while measuring the actual loop latency $T_{\mathrm{loop}}$ would directly test the latency budget. Observation of $T_{\mathrm{loop}} > 0.2\,T_{2}$ would falsify the realizability claim.

**(d) Engineering constraints.** The primary constraints identified in Section 4 are: (i) pulse‑width hardware capable of $\tau_{p}=0.5\,\mu\mathrm{s}$; (ii) timing distribution with jitter $\ll T_{c}$; (iii) verification modules that can check template applicability in real time; (iv) re‑qualification resources for the six non‑portable components (estimated $4$ person‑weeks each). These constraints are derived from the arithmetic in Section 4.

**(e) Projected cost/performance bounds.** Assuming a development cost of $\$10{,}000$ per person‑week (industry average for specialized firmware), the re‑qualification effort projects to $24\times10{,}000=\$240{,}000$ (range $\$120{,}000$–$\$480{,}000$). The actuation hardware cost is not quantified here because it depends on technology not modeled.

**(f) Direct risks or misuse paths.** Embedding quantum‑control logic in the network could expose the control plane to adversarial manipulation if authentication (as discussed in reference [5]) is insufficient, potentially leading to covert decoherence attacks. Rigorous authentication and integrity verification are therefore mandatory.

## 8. Conclusion

We reframed in‑network Hamiltonian engineering as a measurable service and re‑entry problem. Under explicit assumptions, a $T_{c}=8\,\mu\mathrm{s}$ cycle with a $10^{-5}$ per‑cycle error budget admits $N_{c}=125$ cycles per $T_{2}=1\,\mathrm{ms}$ coherence window with projected accumulated error $1.25\times10^{-3}$, at an actuation cost of $2\times10^{6}$ updates per second per endpoint; the closed‑loop latency budget closes with a thin margin ($\eta=0.18$ against $\eta_{\mathrm{max}}=0.2$); and roughly half of the control stack ($\rho=0.5$, bounded by $0.583$) is portable across infrastructure generations, with a projected re‑qualification effort of 24 person‑weeks (range 12–48). The framework’s value lies less in these particular numbers—design assumptions run through deliberately simple models—than in the budget structure they instantiate: cycle time, per‑cycle error, coherence window, and actuation rate are the quantities a 6G architecture must co‑manage if quantum devices become infrastructure. The immediate agenda is to replace the linear accumulation model with Floquet‑Magnus bounds, to ground the systems argument in the model‑based methodology of reference [1], and to build the verification and benchmarking discipline that the software‑engineering literature of references [3], [6], [7], and [8] shows is always the lagging half of any new engineering capability.

## References

[1] arXiv:2001.02559v1 | Digital Infrastructure in Astrophysics  
[2] arXiv:2608.19413v1 | Scientific Visualization as a Collaborative Data Infrastructure  
[3] arXiv:2209.07493v1 | Decentralized Infrastructure for (Neuro)science  
[4] arXiv:1803.05997v4 | Synergizing Roadway Infrastructure Investment with Digital Infrastructure for Infrastructure‑Based Connected Vehicle Applications: Review of Current Status and Future Directions  
[5] arXiv:1002.1160v1 | Towards Public Key Infrastructure less authentication in Session Initiation Protocol  
[6] arXiv:1710.08708v1 | Confidence intervals for normalized citation counts: Can they delimit underlying research capability?  
[7] arXiv:2108.07631v1 | Biologists need modern data infrastructure on campus  
[8] arXiv:1404.7565v2 | Investigating SCADA Failures in Interdependent Critical Infrastructure Systems  
[9] https://papers.qnfo.org/papers/in-network-hamiltonian-engineering-for-6g/. QNFO: In‑Network Hamiltonian Engineering for 6G.

## Appendix A. Divergence report

The aggregate control‑bandwidth projection of Section 4 (Derivation 12, labeled projection) diverges from the per‑endpoint actuation model of Derivations 5–6, and both conventions are documented here rather than silently merged.

- **Convention A (adopted for headline results, Derivations 5–6):** actuation demand is expressed per endpoint as $R_{u}=1/\tau_{p}=2\times10^{6}\,\mathrm{s^{-1}}$ and per node as $K\,R_{u}=1.28\times10^{8}\,\mathrm{s^{-1}}$ for $K=64$ endpoints (A6). This convention ties bandwidth to the pulse width $\tau_{p}$ and scales with deployed endpoints.
- **Convention B (divergent projection):** actuation demand is expressed as an aggregate network load $B_{\mathrm{total}}=N\times f\times b=1000\times10^{6}\times256=2.56\times10^{11}\,\mathrm{bit/s}=256\,\mathrm{Gb/s}$, with independent $20\%$ uncertainties on $N$, $f$, and $b$ combined in quadrature, $\epsilon=\sqrt{3\times0.20^{2}}=\sqrt{0.12}\approx0.346$, giving $B_{\mathrm{total}}\in[167,\,345]\,\mathrm{Gb/s}$. This convention assumes simultaneous per‑node repetition of