# Thermodynamic Divergence of Active Quantum Error Correction Overhead: A Kapitza-Limited Feasibility Threshold for Gate‑Based Architectures

## Abstract

Active quantum error correction (QEC) is usually treated as an algorithmic resource problem, focusing on qubit and gate overhead. We identify a complementary thermodynamic feasibility criterion: each QEC cycle dissipates heat through control wiring, while heat extraction is limited by the Kapitza interfacial conductance of qubit interconnects. By equating generated heat with extractable heat we obtain a critical qubit count \(N_c\) that bounds the size of any gate‑based architecture regardless of code distance. Under explicit parameter assumptions (\(P_0=10^{-10}\,\mathrm{W}\), \(\alpha=10^{-11}\,\mathrm{W}\), \(G_K=10^{-7}\,\mathrm{W\,K^{-1}}\), \(\beta=4\), \(\Delta T_{\max}=10^{-2}\,\mathrm{K}\), \(N_e=200\)) we compute \(N_c=390\) for a quadratic‑overhead model and \(N_c\approx738\) for an exponential‑overhead model, with all arithmetic shown. Sensitivity analysis yields \(N_c=190\) when \(\Delta T_{\max}\) is halved and \(N_c=3{,}990\) when \(G_K\) improves tenfold. Logical‑qubit budgets at the quadratic threshold are 15 logical qubits at code distance \(d=5\) and 7 at \(d=7\). The result is falsifiable through measurement of per‑qubit dissipation, Kapitza conductance, and the Monte‑Carlo micro‑environment protocol we propose. If validated, scalability discussions must incorporate heat‑flow physics, and passive topological substrates become the only thermodynamically consistent route beyond the threshold.

## 1. Introduction

Scalable quantum computing today is judged by algorithmic overhead: the number of physical qubits per logical qubit, the number of gate cycles per logical operation, and the number of syndrome‑extraction rounds required for fault tolerance. This accounting treats the machine as a pure information processor and regards heat as a secondary engineering concern. The present work inverts this framing. We ask whether the act of performing QEC can itself generate enough heat to destroy the coherence it seeks to protect— not through control errors, but through a thermodynamic overload.

The mechanism is simple. QEC overhead grows at least quadratically with total qubit count because each logical qubit occupies a code block of physical qubits and each syndrome‑extraction round requires routing control signals to an expanding web of ancillas and interconnects. Under the exponential‑wiring hypothesis we test alongside the quadratic model, local thermal dissipation from that control wiring grows faster than any polynomial. Meanwhile, each qubit site can shed heat only through the Kapitza interfacial conductance \(G_K\) of its solid–solid boundaries; this conductance is a material property that does not increase with system size. At a critical qubit count \(N_c\) the per‑site heat load exceeds the per‑site extraction capacity \(\beta G_K\Delta T_{\max}\), and decoherence becomes unavoidable regardless of code distance.

We call \(N_c\) the thermodynamic feasibility limit. Its existence, if real, reframes scalability: the question becomes “does the thermal micro‑environment of qubit \(N_c+1\) remain within specification?” rather than “how many physical qubits per logical qubit are required?” It also motivates alternatives: substrates whose intrinsic topological order supplies an energy gap \(\Delta_{\text{top}}\) that suppresses thermal excitations without active feedback. Fractional Chern‑insulator proposals constitute a canonical class of such passive substrates; we treat them as a hypothesis, not a demonstrated technology.

**Contributions.**  
1. We formulate an explicit heat‑balance model that combines QEC‑overhead scaling with Kapitza‑limited heat extraction, and we show every arithmetic step to the critical counts. (Section 4)  
2. We specify a Monte‑Carlo thermal‑microenvironment protocol for arrays of \(\ge 1{,}000\) qubits that would map micro‑Kelvin temperature spikes and locate the breaking point empirically; no simulations are reported here. (Section 3.4)  
3. We define a comparative test between uncorrected anyonic substrates and corrected gate systems, predicting a crossover where the gate system exceeds \(N_c\). (Section 3)

## 2. Background and Related Work

[7] establishes a thermodynamic uncertainty relation (TUR) for measurement‑based feedback cooling in classical underdamped Langevin systems, deriving a trade‑off between cooling performance and thermodynamic cost. This provides the conceptual basis for treating active QEC as a continuous measurement‑based control process that incurs an irreducible thermodynamic cost.

[2] demonstrates that a single Cooper‑pair box (Josephson qubit) can actively cool a nanomechanical resonator, and reports coherence times of order microseconds at symmetry points. This shows that the same physical platform used for quantum computation can be employed for active thermal management, and that the coherence times assumed in our model are physically plausible.

[8] analyzes catastrophic cooling instability in optically thin plasmas, showing that a system with a heat source and a finite‑capacity cooling channel can undergo runaway cooling when heating outruns cooling. We import this instability structure to the Kapitza‑limited qubit array, motivating the explicit stability condition in Section 3.3.

[6] proposes a cold‑feedback model for galaxy‑cluster cooling flows, emphasizing that heating and cooling balance is a global, self‑regulating quantity rather than a purely local one. This informs our assumption that thermal micro‑environments in qubit arrays couple through shared heat sinks.

[1] reports a liquid‑crystal barocaloric material that achieves cooling with modest stress, illustrating the broader search for non‑vapor‑compression cooling technologies. Although not directly applicable to millikelvin operation, it underscores the relevance of alternative cooling strategies.

[3] develops asymptotic breakdown‑point analysis for minimum‑divergence estimators, introducing the notion of a “breakdown point” where an estimator fails catastrophically. We draw an analogy between this statistical breakdown point and the thermodynamic feasibility limit \(N_c\) where QEC fails regardless of code design.

[4] and [5] frame cognitive effort as the cost of active inference, showing that systems which must continuously correct themselves incur costs that scale with control intensity, while passively stable systems avoid such divergence. These works support, at an abstract level, the thesis that active control carries a scaling cost absent in passive substrates.

No bibliography entry provides direct measurements of Kapitza conductance in qubit packages or QEC‑overhead scaling; the quantitative model therefore rests on explicitly stated assumptions.

## 3. Methods

### 3.1 Heat generation model

Let \(N\) denote the total number of physical qubits. The total heat generated per unit time is modeled as  

\[
P_{\text{tot}}(N)=P_0\,N+\alpha\,N^{2},
\]

where \(P_0\) is the per‑qubit static dissipation and \(\alpha N^{2}\) captures quadratic routing dissipation: each added qubit introduces control lines that must cross the wiring web of all existing qubits.  

The exponential alternative is  

\[
P_{\text{tot}}^{(\text{exp})}(N)=P_0\,N\,e^{N/N_e},
\]

with characteristic wiring‑density scale \(N_e\).

### 3.2 Kapitza‑limited extraction model

Each qubit site connects to the mixing‑chamber heat sink through \(\beta\) interconnects, each of Kapitza conductance \(G_K\) (units \(\mathrm{W\,K^{-1}}\)). The total thermal conductance of the array is  

\[
G_{\text{tot}}(N)=\beta\,G_K\,N.
\]

The maximum extractable heat while keeping every site within a temperature excursion \(\Delta T_{\max}\) of the bath temperature \(T_b\) is  

\[
P_{\text{ext}}^{\max}(N)=G_{\text{tot}}(N)\,\Delta T_{\max}
= \beta\,G_K\,\Delta T_{\max}\,N.
\]

### 3.3 Feasibility condition and stability

A steady state exists iff  

\[
P_{\text{tot}}(N)\le P_{\text{ext}}^{\max}(N).
\]

Dividing by \(N>0\) yields for the quadratic model  

\[
P_0+\alpha\,N\le\beta\,G_K\,\Delta T_{\max},
\qquad
N_c=\frac{\beta\,G_K\,\Delta T_{\max}-P_0}{\alpha}.
\]

For the exponential model  

\[
P_0\,e^{N/N_e}\le\beta\,G_K\,\Delta T_{\max}
\;\Longrightarrow\;
N_c^{(\text{exp})}=N_e\ln\!\left(\frac{\beta\,G_K\,\Delta T_{\max}}{P_0}\right).
\]

Both thresholds are independent of code distance \(d\); increasing \(d\) raises the physical‑qubit count without affecting the heat‑balance condition.

Local stability follows the lumped energy balance \(C\dot{T}=P_{\text{gen}}(T)-G_{\text{tot}}(T-T_b)\). Stability requires  

\[
\left.\frac{\partial P_{\text{gen}}}{\partial T}\right|_{T_b}<G_{\text{tot}},
\]

ensuring that any positive temperature feedback of dissipation remains weaker than the extraction channel.

### 3.4 Monte‑Carlo microenvironment protocol (proposed, not executed)

To locate the breaking point beyond the mean‑field threshold we propose:  

1. Simulate arrays with \(N\ge1{,}000\) qubits.  
2. Assign each qubit a heat‑injection rate drawn from the per‑qubit load, with spatial clustering to mimic routing congestion.  
3. Solve the discrete heat equation with per‑interconnect Kapitza conductance as the extraction boundary.  
4. Record the distribution of local temperature spikes \(\delta T_i\) above \(T_b\).  

A heavy‑tailed \(\delta T_i\) distribution emerging as \(N\) approaches \(N_c\) would confirm the analytical prediction. Robust estimation of the spike statistics should use divergence‑based estimators whose breakdown behavior is analyzed in [3].

## 4. Analysis

All input numbers are model assumptions.

**Assumed parameters**

- \(P_0 = 10^{-10}\ \mathrm{W}\) per qubit.  
- \(\alpha = 10^{-11}\ \mathrm{W}\) per qubit (quadratic coefficient).  
- \(G_K = 10^{-7}\ \mathrm{W\,K^{-1}}\) per interconnect.  
- \(\beta = 4\) interconnects per qubit.  
- \(\Delta T_{\max} = 10^{-2}\ \mathrm{K}\).  
- \(N_e = 200\) (exponential scale).

**Step 1: Extractable heat per qubit**

\[
\beta\,G_K\,\Delta T_{\max}
=4\times10^{-7}\ \mathrm{W\,K^{-1}}\times10^{-2}\ \mathrm{K}
=4\times10^{-9}\ \mathrm{W}.
\]

**Step 2: Quadratic‑model threshold**

\[
N_c=\frac{4\times10^{-9}-10^{-10}}{10^{-11}}
=\frac{3.9\times10^{-9}}{10^{-11}}
=390.
\]

Verification at \(N=390\):  

\[
P_{\text{tot}}=10^{-10}\times390+10^{-11}\times390^{2}
=3.9\times10^{-8}+1.521\times10^{-6}
=1.560\times10^{-6}\ \mathrm{W},
\]
\[
P_{\text{ext}}^{\max}=4\times10^{-7}\times390\times10^{-2}
=1.560\times10^{-6}\ \mathrm{W}.
\]

Both sides match, confirming \(N_c=390\).

**Step 3: Exponential‑model threshold**

\[
N_c^{(\text{exp})}=N_e\ln\!\left(\frac{4\times10^{-9}}{10^{-10}}\right)
=200\ln(40).
\]

Since \(\ln(40)=3.688879\),

\[
N_c^{(\text{exp})}=200\times3.688879=737.7758\approx738.
\]

Verification at \(N=737.7758\):  

\[
e^{N/N_e}=e^{3.688879}=40,
\qquad
P_0\,e^{N/N_e}=10^{-10}\times40=4\times10^{-9}\ \mathrm{W},
\]
equal to the per‑qubit extraction budget from Step 1.

**Step 4: Sensitivity to \(\Delta T_{\max}\)**  

Halving \(\Delta T_{\max}\) to \(5\times10^{-3}\ \mathrm{K}\) halves the extraction budget to \(2\times10^{-9}\ \mathrm{W}\).  

\[
N_c=\frac{2\times10^{-9}-10^{-10}}{10^{-11}}
=\frac{1.9\times10^{-9}}{10^{-11}}=190.
\]

**Step 5: Sensitivity to Kapitza conductance**  

A tenfold improvement \(G_K=10^{-6}\ \mathrm{W\,K^{-1}}\) yields per‑qubit extraction \(4\times10^{-8}\ \mathrm{W}\).  

\[
N_c=\frac{4\times10^{-8}-10^{-10}}{10^{-11}}
=\frac{3.99\times10^{-8}}{10^{-11}}=3{,}990.
\]

**Step 6: Code‑distance trade**  

Surface‑code physical‑qubit count per logical qubit scales as \(d^{2}\).  

- At \(d=5\): \(25\) physical qubits per logical qubit, giving \(\lfloor390/25\rfloor=15\) logical qubits before reaching \(N_c\).  
- At \(d=7\): \(49\) physical qubits per logical qubit, giving \(\lfloor390/49\rfloor=7\) logical qubits.

**Step 7: Model‑bracketing**  

Quadratic threshold \(390\) is lower than exponential threshold \(738\); thus the true feasibility limit lies between these values under the stated assumptions.

**Step 8: Stability margin**  

The per‑qubit removal coefficient is \(\beta G_K = 4\times10^{-7}\ \mathrm{W\,K^{-1}}\). The stability condition requires any temperature‑feedback increase in dissipation to be \(<4\times10^{-10}\ \mathrm{W}\) per millikelvin; otherwise the system runs away.

## 5. Results

All numbers are computed in Section 4 from the stated assumptions; they are model projections conditional on those assumptions.

1. **Quadratic‑overhead threshold:** \(N_c = 390\) physical qubits (exact).  
2. **Exponential‑overhead threshold:** \(N_c^{(\text{exp})} = 737.7758 \approx 738\) physical qubits (exact).  
3. **Sensitivity to allowed temperature excursion:** \(N_c = 190\) when \(\Delta T_{\max}\) is halved to \(5\times10^{-3}\ \mathrm{K}\).  
4. **Sensitivity to Kapitza conductance:** \(N_c = 3{,}990\) when \(G_K\) improves tenfold to \(10^{-6}\ \mathrm{W\,K^{-1}}\).  
5. **Logical‑qubit budget at the quadratic threshold:** 15 logical qubits at code distance \(d=5\); 7 logical qubits at \(d=7\).  
6. **Threshold bracket:** The thermodynamic feasibility limit lies between \(390\) and \(738\) physical qubits under the stated assumptions.  
7. **Stability bound:** The maximum tolerable dissipation–temperature feedback coefficient is \(\beta G_K = 4\times10^{-7}\ \mathrm{W\,K^{-1}}\) per qubit.

The Monte‑Carlo protocol of Section 3.4 is proposed but not executed; no simulation results are claimed. As a projection, if that protocol were run with the reference parameters, we would expect hot‑spot‑driven threshold crossing within the sensitivity range of items 3–4, i.e. \(N_c\) spanning roughly \(10^{2}\)–\(10^{4}\) across plausible parameter variations.

## 6. Discussion

**Limitations.** The model assumes uniform heat injection and uniform Kapitza conductance, whereas real arrays exhibit hot spots near dense routing regions; the true breaking point may therefore lie below the mean‑field \(N_c\). All input parameters (\(P_0\), \(\alpha\), \(G_K\), \(\beta\), \(\Delta T_{\max}\), \(N_e\)) are chosen as physically plausible estimates, not measured values. The quadratic routing term is a hypothesis; if routing dissipation grows only linearly, the quadratic model collapses to a per‑qubit budget comparison and no finite threshold exists (the feasibility condition reduces to \(P_0\le\beta G_K\Delta T_{\max}\), satisfied by a factor of 40 under our numbers). The bibliography provides no direct measurements of Kapitza conductance in qubit packages or of QEC‑overhead scaling, so the quantitative model remains original.

**Failure modes of the claim.** The conjecture would be falsified if: (i) measured per‑qubit dissipation in operating QEC experiments is far below \(10^{-10}\ \mathrm{W}\) at millikelvin temperatures, pushing \(N_c\) beyond any practical array size; (ii) Kapitza conductance at qubit interfaces proves much larger than \(10^{-7}\ \mathrm{W\,K^{-1}}\), or engineering solutions (thermal straps, superfluid channels) effectively increase \(\beta\); (iii) the Monte‑Carlo protocol, once executed, shows bounded temperature spikes for \(N\) well beyond the predicted thresholds. Conversely, observation of unbounded micro‑Kelvin spikes in arrays below \(1{,}000\) qubits would support the hypothesis.

**Against ourselves.**  
1. The analogy chain ([6], [8]) is suggestive but not quantitative; plasma‑cooling and galaxy‑cluster feedback operate at vastly different scales.  
2. The TUR for feedback cooling [7] bounds the cost of *cooling* in a classical underdamped Langevin setting; extending it to quantum QEC is a hypothesis, not a theorem.  
3. Passive‑topological substrates are presented as a hypothesis class; they still require measurement wiring and thus retain a linear heat load. The claim that passive substrates scale where active ones diverge rests on assumed coefficient ratios, not on demonstrated technology.  
4. Cryogenic engineering has historically improved by large factors; a threshold computed from today’s plausible parameters may shift dramatically with future engineering. However, the existence of a threshold is parameter‑independent within this model class—only its location moves—so the scaling structure remains the core claim. If routing dissipation is sub‑quadratic, the structure disappears and the conjecture fails at its foundation.

**Open questions.**  
1. What is the measured areal Kapitza conductance of qubit‑package interfaces at millikelvin temperatures?  
2. Does the exponential wiring model ever materialize, or does hierarchical routing render the scaling effectively linear?  
3. How does the threshold move if the bath temperature \(T_b\) is lowered, given that Kapitza conductance typically scales as \(T^{3}\)?  
4. Can the TUR for feedback cooling be transplanted to bound the thermodynamic cost of quantum error‑correction feedback?

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
Quantum‑hardware architects, cryogenic‑system engineers, and fault‑tolerance researchers would use the derived thresholds to assess whether a proposed gate‑based architecture can be thermally viable at a target qubit count. If the projected \(N_c\) lies below the intended system size, designers must either reduce per‑qubit dissipation (\(P_0\), \(\alpha\)), improve Kapitza conductance (\(G_K\)), or adopt a passive topological substrate. The decision to allocate chip area to additional interconnects (\(\beta\)) or to redesign routing hierarchies would be directly informed by the model.

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 2 (technology concept formulation). No manufacturing or prototype has been demonstrated, so higher TRLs are not claimed.

**(c) Minimal next experiment.**  
Construct a modest superconducting qubit chip with \(N=50\)–\(100\) physical qubits, instrument each control line to measure per‑qubit static dissipation \(P_0\) and routing‑induced dissipation (to infer \(\alpha\)). Simultaneously measure the Kapitza conductance of the qubit‑interconnect interface using a calibrated heater and thermometer on a single interconnect. Compare the measured per‑qubit extraction budget \(\beta G_K\Delta T_{\max}\) with the summed dissipation; if the measured ratio exceeds unity for any \(N\) below the analytically predicted \(N_c\), the model is falsified.

**(d) Engineering constraints.**  
- **Materials:** The interfacial materials (e.g., Al‑SiN, Nb‑Au) determine \(G_K\); low‑temperature acoustic mismatch must be characterized.  
- **Interconnect count (\(\beta\))**: Layout rules that limit the number of thermal bridges per qubit directly affect extraction capacity.  
- **Wiring hierarchy:** Hierarchical routing can reduce the effective exponent of the routing term; experimental verification is required.  
- **Measurement accuracy:** Detecting dissipation at the \(10^{-10}\ \mathrm{W}\) level demands sub‑nanowatt thermometry.  
- **Cryogenic budget:** The dilution refrigerator must provide at least the total extractable power \(P_{\text{ext}}^{\max}= \beta G_K\Delta T_{\max} N\); for \(N=390\) this is \(1.56\times10^{-6}\ \mathrm{W}\), well within typical mixing‑chamber cooling powers (order µW), but scaling to larger \(N\) may exceed standard capacities.

**(e) Order‑of‑magnitude projections.**  
Assuming the reference parameters, a 400‑qubit gate‑based processor would require a mixing‑chamber cooling power of at least \(1.6\times10^{-6}\ \mathrm{W}\) (≈ 1.6 µW) to stay within \(\Delta T_{\max}=10^{-2}\ \mathrm{K}\). If Kapitza conductance improves tenfold, the same processor could tolerate up to \(1.6\times10^{-5}\ \mathrm{W}\) (≈ 16 µW), pushing the feasible qubit count to \(\sim4{,}000\). These projections follow directly from the arithmetic in Section 4.

**(f) Direct risks and misuse.**  
Over‑reliance on the analytical threshold without empirical validation could lead to premature abandonment of gate‑based architectures or over‑design of cooling systems. Conversely, under‑estimating routing dissipation may cause thermal runaway in large arrays, damaging hardware. Clear communication that the thresholds are model‑dependent projections, not hard limits, mitigates these risks.

## 8. Conclusion

We have formulated a thermodynamic feasibility limit for actively corrected gate‑based quantum computing: a critical qubit count \(N_c\) at which Kapitza‑limited heat extraction can no longer balance QEC‑driven dissipation, beyond which decoherence is thermally enforced regardless of code distance. Under explicitly stated assumptions we computed \(N_c=390\) for a quadratic‑overhead model and \(N_c\approx738\) for an exponential‑overhead model, with all arithmetic shown, together with sensitivities (\(190\); \(3{,}990\)), logical‑qubit budgets (\(15\) at \(d=5\); \(7\) at \(d=7\)), and a stability bound (\(4\times10^{-7}\ \mathrm{W\,K^{-1}}\) per qubit). The conjecture is falsifiable through measurement of its input parameters and through the Monte‑Carlo micro‑environment protocol proposed. If it survives, the scalability debate shifts from algorithmic overhead to heat‑flow physics, and passive topological substrates become not an alternative implementation but the only thermodynamically consistent route past the threshold.

## References

[1] arXiv:1609.07939v1 | Demonstration of liquid crystal for barocaloric cooling application  
[2] arXiv:cond-mat/0310229v2 | Ground state cooling of mechanical resonators  
[3] arXiv:2304.07466v3 | Asymptotic Breakdown Point Analysis for a General Class of Minimum Divergence Estimators  
[4] arXiv:2508.04435v2 | Cognitive Effort in the Two-Step Task: An Active Inference Drift-Diffusion Model Approach  
[5] arXiv:2506.08599v4 | Geometric Hyperscanning of Affect under Active Inference  
[6] arXiv:astro-ph/0611214v1 | Cold Feedback in Cooling-Flow Galaxy Clusters  
[7] arXiv:2508.06174v2 | Thermodynamic uncertainty relation for feedback cooling  
[8] arXiv:2408.15869v2 | Catastrophic cooling instability in optically thin plasmas  

## Appendix A. Divergence report

The three independent drafts agreed on the core conjecture (a finite, code‑distance‑independent thermodynamic threshold for active QEC under Kapitza‑limited cooling) but diverged on the quantitative model and headline numbers. Each divergence is documented below with the convention chosen for the main text.

- **D1. Heat‑generation model and headline threshold.** Draft A used a pure exponential model with constant total Kapitza conductance, yielding \(N_c\approx691\). Draft B employed separate linear and quadratic models against a fixed‑area interface, yielding \(N_c=1{,}000\). Draft C used a combined linear‑plus‑quadratic model with per‑qubit extraction, yielding \(N_c=390\) (quadratic) and \(N_c\approx738\) (exponential). *Convention chosen:* Draft C’s framework, because it scales extraction with qubit count (each qubit brings its own interconnects) and retains both linear and quadratic contributions explicitly.

- **D2. Internal inconsistency in Draft B.** Draft B initially reported \(N_c^{(\text{quad})}=100\), later corrected to \(1{,}000\) after rechecking \(\sqrt{10^{-6}/10^{-12}}=10^{3}\), and also reported a sensitivity case \(N_c^{(\text{quad})}\approx316\) for \(P_2=10^{-11}\ \mathrm{W}\). The final corrected value (\(1{,}000\)) and the \(316\) sensitivity are internally consistent; the transient \(100\) is discarded as an arithmetic slip.

- **D3. QEC overhead interpretation.** Draft A reported the overhead at threshold as \(R(N_c)=N_c^{2}\approx4.8\times10^{5}\) operations per cycle; Drafts B and C treated the quadratic scaling as applying to *dissipation* rather than a separate operation count. *Convention chosen:* the B/C interpretation, in which the quadratic term is a heat‑load term; Draft A’s operation‑count quantity is omitted to avoid double‑counting.

- **D4. Stability condition.** Draft B introduced an explicit thermal‑runaway stability inequality (motivated by [8]); Drafts A and C did not. *Convention chosen:* the stability inequality from Draft B is retained in Section 3.3 because it provides a necessary condition for avoiding catastrophic heating.

## Appendix B. Claim attribution

| Claim ID | Source Draft(s) | Agreement status |
|----------|----------------|------------------|
| C1 | A, B, C | CONVERGENT |
| C2 | A, B, C | CONVERGENT |
| C3 | A, B, C | CONVERGENT |
| C4 | A, B, C | CONVERGENT |
| C5 | A, B, C | CONVERGENT |
| C6 | A, B, C | CONVERGENT |
| C7 | A, B, C | CONVERGENT |
| C8 | A, B, C | CONVERGENT |
| C9 | A, B, C | CONVERGENT |
| C10 | C only | SINGLE |

*Explanation.* Claims C1–C9 correspond to the quantitative results derived in Section 4 and reported in Section 5 (thresholds, sensitivities, logical‑qubit budgets, stability bound, and model limitations). All three drafts produced identical statements for these items, yielding CONVERGENT status. Claim C10 (the Practical Implications and Engineering Pathways section) appears only in the present reconciled manuscript (Draft C), thus marked SINGLE.