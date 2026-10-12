# Thermodynamic Divergence of Active Quantum Error Correction Overhead: A Kapitza-Limited Feasibility Threshold for Gate-Based Architectures

## Abstract

Active quantum error correction (QEC) is conventionally analyzed as an algorithmic resource problem: the question is how many physical qubits and gate cycles are needed per logical qubit. We propose a complementary, thermodynamic feasibility criterion. In a gate-based architecture, every QEC cycle is driven by control wiring whose dissipation we model as a linear per-qubit term plus a quadratic routing term, while the only heat sink available to each qubit is the Kapitza thermal conductance of its interconnects, which bounds the heat flux sustainable for a given allowed temperature rise. Setting total generated heat equal to total extractable heat yields an explicit critical qubit count $N_c$ above which no steady state exists at the operating temperature, independent of code distance: increasing code distance adds qubits and therefore adds heat faster than it adds logical protection. Under the stated parameter assumptions we compute $N_c = 390$ for the quadratic-overhead model and $N_c \approx 738$ for an exponential wiring-dissipation model, with full arithmetic shown. We argue that this defines a thermodynamic feasibility limit for actively corrected gate systems, and that architectures whose error protection is passive and intrinsic — such as substrates whose energy gaps relax excitations without feedback — escape the divergence because their cooling requirement does not scale with control activity. We frame the proposal as a conjecture with a concrete falsification program, and we position it against the supplied literature on feedback-cooling thermodynamic costs, thermal runaway instabilities, and self-regulating heat-cool balance.

## 1. Introduction

The scalability debate in quantum computing is dominated by overhead accounting: how many physical qubits per logical qubit, how many cycles per logical operation, how many gates per syndrome round. This accounting treats the machine as an information-processing object and treats heat as an engineering afterthought to be handled by better cryogenics. The conjecture developed here inverts the framing. We ask whether there is a regime in which the act of performing quantum error correction destroys the very coherence it is meant to protect — not through control errors, but through heat.

The mechanism is simple to state. QEC resource overhead grows at least quadratically with the number of logical qubits, because each logical qubit requires a code block of physical qubits and each syndrome-extraction round requires routing control signals to an expanding web of ancillas and interconnects. Local thermal dissipation from that control wiring, under the exponential-wiring hypothesis we test alongside the quadratic model, grows faster than any polynomial. Meanwhile, the heat leaving each qubit site is limited by the Kapitza interfacial conductance $G_K$ of the solid–solid boundaries between the qubit die, its packaging, and its interconnects. Kapitza conductance is a material property with finite magnitude; it does not scale with qubit count. At a critical qubit count $N_c$, the heat generated per qubit site exceeds the heat that the local thermal path can carry away for the maximum tolerable temperature excursion $\Delta T_{\max}$, and decoherence becomes unavoidable regardless of how the code distance is chosen.

We call $N_c$ the thermodynamic feasibility limit. Its existence, if real, reframes scalability: the question is no longer only "how many physical qubits per logical qubit" but "does the thermal microenvironment of qubit $N_c + 1$ remain within specification." It also motivates a class of alternatives: substrates whose topological order supplies an intrinsic energy gap $\Delta_{\text{top}}$ that suppresses thermal excitations as $e^{-\Delta_{\text{top}}/k_B T}$ without any active feedback, so that their cooling requirement does not grow with control activity. Fractional Chern insulator proposals are the canonical candidate for such passive topological substrates; we treat them here as a hypothesis class, not as a demonstrated technology.

This paper makes three contributions. First, we write down an explicit heat-balance model combining QEC overhead scaling with Kapitza-limited heat extraction, and we show every arithmetic step leading to the critical counts. Second, we specify a Monte Carlo thermal microenvironment protocol — simulating arrays of $1{,}000$ or more qubits with per-site heat injection and Kapitza-limited extraction — that would map micro-Kelvin temperature spikes and locate the breaking point empirically; we do not report simulation results, because none have been run for this paper. Third, we define the comparative test: uncorrected anyonic substrates versus corrected gate systems, with the crossover predicted where the gate system crosses $N_c$.

We stress the epistemic status of the central claim. It is a conjecture, derived from a stylized model with assumed parameters. Its value lies in being falsifiable: each parameter is in principle measurable, and the threshold prediction moves measurably with each one.

## 2. Background and Related Work

The supplied bibliography is heterogeneous, spanning condensed-matter cooling, plasma astrophysics, statistical estimation, and cognitive science. We cite each entry strictly on the basis of its supplied title and summary text; where a summary is thin, we say so and use the work only at the level its summary supports.

[7] is the closest methodological relative. Its summary states that feedback cooling enables a system to reach low temperatures through measurement-based control, and that the work establishes a thermodynamic uncertainty relation (TUR) for feedback cooling in classical underdamped Langevin systems, deriving a trade-off between the thermodynamic cost and the achievable cooling within finite time. This is precisely the tension we generalize: active QEC is measurement-based control applied $10^{2}$–$10^{3}$ times per second per qubit block, and [7] supplies the conceptual warrant that such control carries an irreducible thermodynamic cost that grows as one demands better effective cooling. Our model makes that cost concrete as wiring dissipation and asks when it overwhelms the cooling channel.

[2] proposes using a single Cooper pair box (Josephson qubit) to actively cool nanomechanical resonators, noting that Josephson qubit experiments had demonstrated coherence times of order microseconds at special symmetry points, sufficient for an analog of laser cooling. The entry is relevant in two directions: it shows the same physical platform (Josephson devices) being used for active thermal management, and it documents that coherence at these symmetry points is finite and of order microseconds — the resource our heat load erodes. The summary supplied gives no further quantitative detail, so we use it only at this level.

[8] analyzes catastrophic cooling instability in optically thin plasmas, using the solar corona as the prototype of a low-density environment heated externally and cooled radiatively, with the MHD equations modified to include energy source terms approximating local heating and cooling. The structural analogy is direct: a system with a heat source, a finite-capacity cooling channel, and a runaway mode when heating outruns cooling. Our Kapitza-limited qubit array is a solid-state cousin of this instability structure, and [8] supplies the precedent that such cooling–heating imbalance produces catastrophic rather than graceful degradation.

[6] puts forward an alternative view of the feedback between heating and cooling in cooling-flow galaxy clusters, adopting the view that heating comes from an active galactic nucleus accreting mass and launching jets or winds, and proposing that the feedback occurs with the entire cool inner region rather than a localized Bondi radius. The entry supports the general principle that heating–cooling balance is a global, self-regulating quantity, not a purely local one — a principle we import when arguing that thermal microenvironments in qubit arrays couple through shared heat sinks.

[1] demonstrates a liquid crystal as a liquid barocaloric material with cooling potential, noting that its phase transition requires only a small stress (tens of MPa) and can be operated near room temperature, as an alternative to vapor compression based on gas–liquid transitions of hazardous gases. We cite it as evidence that the cooling-technology community actively seeks non-vapor-compression heat management; the summary supplied gives no cryogenic-relevant data, so we draw no quantitative claim from it for millikelvin operation.

[3] develops asymptotic breakdown point analysis for a general class of minimum divergence estimators, building on the density power divergence family introduced by Basu et al. (1998) for robust estimation. The connection is terminological and structural: the "breakdown point" — the contamination level at which an estimator fails catastrophically — is the statistical analogue of our thermodynamic feasibility limit, the qubit count at which the system's error-correction guarantee fails regardless of code design. The summary supplied gives no further detail connecting it to physics, and we do not claim more.

[4] and [5] come from active-inference cognitive modeling. [4] frames cognitive effort as the cost of resolving conflict between habits and optimal policies within an evidence-accumulator drift-diffusion account; [5] models second-person social cognition as coupled active inference in which each agent tracks violations of its predictive coherence. Both support, at the level of analogy, the thesis that active control has a cost that scales with the intensity of control and that systems which must continuously correct themselves face a resource divergence that passively stable systems avoid. The summaries supplied give no quantitative content transferable to qubit thermodynamics, and we use these works only as conceptual parallels.

[9]–[12] are QNFO corpus entries whose supplied summaries are empty. Their titles — on thermodynamic and informational bottlenecks of scalable fault-tolerant quantum computation [9], thermodynamic and quantum constraints on scalable quantum computing [10], spectral dynamics and thermodynamic stability [11], and thermodynamic viability and universality of Feynman matter [12] — indicate a research line treating thermodynamic constraints as primary limits on scalable quantum computation, which is the frame of this paper. Because no summary text is supplied, we cannot state what these works did or found, and we cite them only as indicating the existence of this research direction.

No entry in the supplied bibliography directly treats Kapitza conductance or QEC overhead scaling; the quantitative model below is therefore original to this paper, and its parameters are stated assumptions rather than values taken from any cited work.

## 3. Methods

### 3.1 Heat generation model

Let $N$ be the number of physical qubits in the array. We model total heat generated inside the cold stage per unit time as

$$P_{\text{tot}}(N) = P_0\, N + \alpha\, N^2,$$

where $P_0$ is the per-qubit static and linear-control dissipation and $\alpha\, N^2$ is the quadratic routing term: each additional qubit adds control lines that must cross the wiring web of all previously added qubits, so routing dissipation grows as the square of qubit count. This quadratic form is the conservative case; the exponential alternative,

$$P_{\text{tot}}^{(\text{exp})}(N) = P_0\, N\, e^{N/N_e},$$

with characteristic wiring-density scale $N_e$, is analyzed in parallel because the source conjecture posits exponential growth of local thermal dissipation from control wiring.

### 3.2 Kapitza-limited extraction model

Each qubit site is coupled to the mixing-chamber heat sink through $\beta$ interconnects, each of Kapitza conductance $G_K$ (units $\text{W}\,\text{K}^{-1}$). Kapitza conductance is the thermal boundary conductance at the interface between two solids; it is finite, material-dependent, and does not increase with system size. The total thermal conductance of the array is

$$G_{\text{tot}}(N) = \beta\, G_K\, N.$$

The maximum heat flux sustainable while keeping every qubit site within a temperature excursion $\Delta T_{\max}$ of the bath temperature $T_b$ is

$$P_{\text{ext}}^{\max}(N) = G_{\text{tot}}(N)\, \Delta T_{\max} = \beta\, G_K\, \Delta T_{\max}\, N.$$

### 3.3 Feasibility condition

A steady state at temperature $T_b + \Delta T_{\max}$ exists if and only if

$$P_{\text{tot}}(N) \le P_{\text{ext}}^{\max}(N).$$

Dividing both sides by $N > 0$ (the per-qubit form), the quadratic model gives

$$P_0 + \alpha\, N \le \beta\, G_K\, \Delta T_{\max},$$

so the critical count is

$$N_c = \frac{\beta\, G_K\, \Delta T_{\max} - P_0}{\alpha}.$$

For the exponential model, dividing by $N$ gives

$$P_0\, e^{N/N_e} \le \beta\, G_K\, \Delta T_{\max}
\quad\Longrightarrow\quad
N_c^{(\text{exp})} = N_e \ln\!\left(\frac{\beta\, G_K\, \Delta T_{\max}}{P_0}\right).$$

Both thresholds are independent of code distance $d$: increasing $d$ increases the number of physical qubits per logical qubit (as $d^2$ in the standard surface-code counting), which moves the array toward $N_c$ faster while buying logical protection. This is the formal content of the "self-defeating regime": past $N_c$, more QEC resources strictly worsen the thermal environment.

### 3.4 Monte Carlo microenvironment protocol (proposed, not executed)

To locate the breaking point beyond the mean-field threshold, we specify: simulate arrays of $N \ge 1{,}000$ qubits; assign each qubit a heat-injection rate drawn from the $P_0 + \alpha N$ per-qubit load with spatial clustering to mimic routing congestion; solve the discrete heat equation with per-interconnect Kapitza conductance as the extraction boundary; record the distribution of local temperature spikes $\delta T_i$ above $T_b$. The predicted signature is a heavy tail in $\delta T_i$ emerging as $N$ approaches $N_c$. No results from this protocol are reported in this paper.

## 4. Analysis

Every input number below is a stated model assumption, not a measurement; the derivations are exact given the assumptions.

**Inputs (assumed):**

- $P_0 = 10^{-10}\ \text{W}$ per qubit (linear dissipation).
- $\alpha = 10^{-11}\ \text{W}$ per qubit (coefficient of the quadratic routing term).
- $G_K = 10^{-7}\ \text{W}\,\text{K}^{-1}$ per interconnect.
- $\beta = 4$ interconnects per qubit.
- $\Delta T_{\max} = 10^{-2}\ \text{K}$ (maximum tolerable excursion above the bath).
- $N_e = 200$ (exponential wiring-density scale, exponential model only).

**Step 1: extractable heat per qubit.**

$$\beta\, G_K\, \Delta T_{\max} = 4 \times 10^{-7}\ \text{W}\,\text{K}^{-1} \times 10^{-2}\ \text{K} = 4 \times 10^{-9}\ \text{W}.$$

So each qubit site can shed at most $4 \times 10^{-9}\ \text{W}$ while staying within $\Delta T_{\max}$.

**Step 2: quadratic-model threshold.**

$$N_c = \frac{4 \times 10^{-9} - 10^{-10}}{10^{-11}} = \frac{3.9 \times 10^{-9}}{10^{-11}} = 390.$$

Check by substitution at $N = 390$: generated heat is $P_{\text{tot}} = 10^{-10} \times 390 + 10^{-11} \times 390^2 = 3.9 \times 10^{-8} + 10^{-11} \times 152{,}100 = 3.9 \times 10^{-8} + 1.521 \times 10^{-6} = 1.560 \times 10^{-6}\ \text{W}$. Extractable heat is $G_{\text{tot}} \Delta T_{\max} = 4 \times 10^{-7} \times 390 \times 10^{-2} = 1.560 \times 10^{-6}\ \text{W}$. The two sides match exactly, confirming $N_c = 390$.

**Step 3: exponential-model threshold.**

$$N_c^{(\text{exp})} = N_e \ln\!\left(\frac{4 \times 10^{-9}}{10^{-10}}\right) = 200 \ln(40).$$

Since $\ln(40) = \ln(4) + \ln(10) \approx 1.386294 + 2.302585 = 3.688879$,

$$N_c^{(\text{exp})} = 200 \times 3.688879 = 737.7758 \approx 738.$$

Check by substitution at $N = 737.7758$: $e^{N/N_e} = e^{3.688879} = 40$ exactly, so per-qubit generation is $10^{-10} \times 40 = 4 \times 10^{-9}\ \text{W}$, equal to the per-qubit extraction limit from Step 1. Confirmed.

**Step 4: sensitivity of the quadratic threshold to $\Delta T_{\max}$.** Since $N_c$ is linear in $\Delta T_{\max}$, halving the allowed excursion to $5 \times 10^{-3}\ \text{K}$ halves the extraction budget to $2 \times 10^{-9}\ \text{W}$ and gives

$$N_c = \frac{2 \times 10^{-9} - 10^{-10}}{10^{-11}} = \frac{1.9 \times 10^{-9}}{10^{-11}} = 190.$$

**Step 5: sensitivity to Kapitza conductance.** A tenfold improvement, $G_K = 10^{-6}\ \text{W}\,\text{K}^{-1}$, gives extraction $4 \times 10^{-8}\ \text{W}$ per qubit and

$$N_c = \frac{4 \times 10^{-8} - 10^{-10}}{10^{-11}} = \frac{3.99 \times 10^{-8}}{10^{-11}} = 3{,}990.$$

**Step 6: code-distance trade.** In the standard surface-code counting, physical qubits per logical qubit scale as $d^2$. At $d = 5$, one logical qubit costs $25$ physical qubits; the quadratic model therefore supports at most $\lfloor 390 / 25 \rfloor = 15$ logical qubits at distance $5$ before the thermal budget is exhausted — under the stated assumptions. At $d = 7$ the cost is $49$ physical qubits per logical qubit, giving $\lfloor 390/49 \rfloor = 7$ logical qubits. Increasing $d$ from $5$ to $7$ buys a lower logical error rate but consumes the thermal budget more than twice as fast per logical qubit, which is the quantitative form of the self-defeating regime.

**Step 7: crossover between models.** The quadratic model is more conservative for $N < N_c^{(\text{exp})}$ in the sense that it fails first ($390 < 738$) under these parameters; the exponential model's larger threshold arises because its per-qubit load $P_0 e^{N/N_e}$ equals $P_0 = 10^{-10}\ \text{W}$ at $N = 0$ and only reaches the extraction limit at $N \approx 738$, whereas the quadratic model's per-qubit load $P_0 + \alpha N$ grows linearly and reaches the limit at $N = 390$. The two models bracket the threshold between $390$ and $738$ qubits under the stated assumptions.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions; they are model projections conditional on those assumptions, not measurements.

1. **Quadratic-overhead threshold:** $N_c = 390$ physical qubits (exact under the assumed parameters; verified by substitution in Step 2).
2. **Exponential-overhead threshold:** $N_c^{(\text{exp})} = 737.7758 \approx 738$ physical qubits (verified by substitution in Step 3).
3. **Sensitivity to allowed temperature excursion:** $N_c = 190$ if $\Delta T_{\max}$ is halved to $5 \times 10^{-3}\ \text{K}$ (Step 4).
4. **Sensitivity to Kapitza conductance:** $N_c = 3{,}990$ if $G_K$ improves tenfold to $10^{-6}\ \text{W}\,\text{K}^{-1}$ (Step 5).
5. **Logical-qubit budget at the quadratic threshold:** $15$ logical qubits at code distance $d = 5$; $7$ logical qubits at $d = 7$ (Step 6).
6. **Threshold bracket:** under the stated assumptions, the thermodynamic feasibility limit lies between $390$ and $738$ physical qubits (Step 7).

The Monte Carlo protocol of Section 3.4 is proposed but not executed; no simulation results are claimed.

## 6. Discussion

**Limitations.** The model is mean-field: it assumes uniform heat injection and uniform Kapitza conductance, whereas real arrays have hot spots near dense routing regions, so the true breaking point may lie below the mean-field $N_c$. The parameters $P_0$, $\alpha$, $G_K$, $\beta$, $\Delta T_{\max}$, and $N_e$ are assumptions chosen to be physically plausible in magnitude, not measured values; every headline number scales linearly (or, for the exponential model, logarithmically) with them, and the sensitivity results (Steps 4–5) show the threshold spans more than an order of magnitude across plausible parameter ranges. The quadratic routing term is a modeling hypothesis, not a derived law; if routing dissipation in fact grows only linearly, the quadratic model reduces to a per-qubit budget comparison and no finite threshold exists at all — the feasibility condition becomes $P_0 \le \beta G_K \Delta T_{\max}$, which is satisfied by a factor of $40$ under the assumed numbers. This is the single most important internal vulnerability of the conjecture.

**Failure modes of the claim.** The conjecture would be falsified if: (i) measured per-qubit dissipation in operating QEC experiments is far below $10^{-10}\ \text{W}$ at millikelvin temperatures, pushing $N_c$ beyond any practically interesting array size; (ii) Kapitza conductance at qubit-relevant interfaces proves much larger than $10^{-7}\ \text{W}\,\text{K}^{-1}$, or engineering solutions (thermal straps, superfluid heat channels) effectively multiply $\beta$; (iii) the Monte Carlo protocol, once run, shows temperature spikes remaining bounded as $N$ grows past the predicted threshold. Conversely, observation of unbounded micro-Kelvin spike growth in arrays below $1{,}000$ qubits would support it.

**What would strengthen it.** Direct measurement of $G_K$ for the specific material stack used in gate-based QEC chips; calorimetric measurement of per-cycle control-wiring dissipation; and execution of the proposed $1{,}000$-qubit thermal simulation. Each is a concrete experiment that converts one assumed input into a measured one.

**Open questions.** Does the passive-topological alternative actually escape the divergence? A substrate with intrinsic gap $\Delta_{\text{top}}$ suppresses thermal excitations as $e^{-\Delta_{\text{top}}/k_B T}$ without feedback, but readout of any computational device still requires measurement wiring, so some linear heat load remains; the claim that passive substrates scale where active ones diverge is therefore a hypothesis about the coefficient ratios, not a theorem. Second, is the exponential wiring model ever realized in practice, or does routing become hierarchical and effectively linear? Third, how do the thresholds move if the bath temperature $T_b$ itself is lowered — Kapitza conductance typically falls with temperature, so the extraction budget may shrink even as the coherence improves, a coupling the present model does not capture.

**Against ourselves.** The strongest counterargument is historical: cryogenic engineering has repeatedly improved by large factors under commercial pressure, and a threshold computed from today's plausible parameters may be irrelevant to tomorrow's stack. Our response is that the threshold's existence is parameter-independent within this model class — only its location moves — so the conjecture is a statement about scaling structure, not about a fixed qubit count. But if the routing term is sub-quadratic, the structure itself disappears, and the conjecture fails at its foundation.

## 7. Conclusion

We have formulated a thermodynamic feasibility limit for actively corrected gate-based quantum computing: a critical qubit count $N_c$ at which Kapitza-limited heat extraction can no longer balance QEC-driven dissipation, beyond which decoherence is thermally enforced regardless of code distance. Under explicitly stated assumptions we computed $N_c = 390$ for a quadratic-overhead model and $N_c \approx 738$ for an exponential-overhead model, with all arithmetic shown, and we showed the threshold is independent of code distance — the formal content of the self-defeating regime. The conjecture is falsifiable through measurement of its four input parameters and through the proposed Monte Carlo microenvironment protocol. If it survives, the scalability debate shifts from algorithmic overhead to heat-flow physics, and passive topological substrates become not an alternative implementation but the only thermodynamically consistent route past the threshold.

## References

[1] arXiv:1609.07939v1 | Demonstration of liquid crystal for barocaloric cooling application

[2] arXiv:cond-mat/0310229v2 | Ground state cooling of mechanical resonators

[3] arXiv:2304.07466v3 | Asymptotic Breakdown Point Analysis for a General Class of Minimum Divergence Estimators

[4] arXiv:2508.04435v2 | Cognitive Effort in the Two-Step Task: An Active Inference Drift-Diffusion Model Approach

[5] arXiv:2506.08599v4 | Geometric Hyperscanning of Affect under Active Inference

[6] arXiv:astro-ph/0611214v1 | Cold Feedback in Cooling-Flow Galaxy Clusters

[7] arXiv:2508.06174v2 | Thermodynamic uncertainty relation for feedback cooling

[8] arXiv:2408.15869v2 | Catastrophic cooling instability in optically thin plasmas

[9] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation

[10] QNFO: Thermodynamic and Quantum Constraints on Scalable Quantum Computing

[11] QNFO: Spectral Dynamics and Thermodynamic Stability in the Arithmetic Quantum Framework

[12] QNFO: Thermodynamic Viability and the Universality of Feynman Matter