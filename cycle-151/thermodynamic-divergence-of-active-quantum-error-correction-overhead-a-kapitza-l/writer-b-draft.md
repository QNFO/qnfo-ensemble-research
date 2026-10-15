# Thermodynamic Divergence of Active Quantum Error Correction Overhead: A Kapitza-Limited Feasibility Threshold for Gate-Based Architectures

## Abstract

Active quantum error correction (QEC) is conventionally analyzed as an algorithmic resource problem: how many physical qubits and gate cycles are needed per logical qubit. We propose a complementary thermodynamic feasibility criterion. In a gate-based architecture, every QEC cycle is driven by control wiring whose dissipation we model as a linear per-qubit term plus a quadratic routing term, while the heat sink available to each qubit is the Kapitza thermal conductance of its interconnects, which bounds the sustainable heat flux for a given allowed temperature rise. Setting generated heat equal to extractable heat yields an explicit critical qubit count $N_c$ above which no steady state exists at the operating temperature, independent of code distance: increasing code distance adds qubits, and therefore heat, faster than it adds logical protection. Under explicitly stated parameter assumptions we compute $N_c = 390$ for the quadratic-overhead model and $N_c \approx 738$ for an exponential wiring-dissipation model, with all arithmetic shown, and we derive sensitivities ($N_c = 190$ for a halved temperature budget; $N_c = 3{,}990$ for a tenfold Kapitza improvement) and logical-qubit budgets (15 at code distance $d=5$; 7 at $d=7$). We frame the proposal as a falsifiable conjecture, specify a Monte Carlo thermal-microenvironment protocol that we do not execute, and position the argument against literature on feedback-cooling thermodynamic costs, thermal runaway instabilities, and self-regulating heat–cool balance. The framework reframes scalability from algorithmic overhead to heat-flow physics.

## 1. Introduction

Cryogenic quantum-computing engineering teams today face a decision that has no quantitative answer in the literature: as a superconducting-qubit array grows past hundreds of devices, how much cooling capacity must be reserved per qubit site, and does that reservation grow fast enough to keep up with the control wiring that error correction demands? The practical cost of not knowing is concrete. A dilution refrigerator stage is specified by a finite cooling power at 10–20 $\mu\mathrm{W}$ scale at 10 mK [11]; if the per-qubit dissipation of an actively corrected array grows with qubit count, the array's thermal budget is exhausted at some finite size no matter how the code is designed, and every additional physical qubit added for protection makes the microenvironment of its neighbors worse. Today this question is absorbed into ad hoc wiring budgets and cryostat margins; a derived threshold would instead give architects an explicit stopping rule and tell them where to spend engineering effort — on interconnect thermal conductance rather than on code distance.

The mechanism we study is easy to state. QEC resource overhead grows at least quadratically with qubit count, because each logical qubit requires a code block of physical qubits and each syndrome-extraction round requires routing control signals to an expanding web of ancillas and interconnects. Local thermal dissipation from that control wiring, under the exponential-wiring hypothesis we test alongside the quadratic model, grows faster than any polynomial. Meanwhile, the heat leaving each qubit site is limited by the Kapitza interfacial conductance $G_K$ of the solid–solid boundaries between the qubit die, its packaging, and its interconnects. Kapitza conductance is a material property with finite magnitude; it does not scale with qubit count. At a critical qubit count $N_c$, the heat generated per qubit site exceeds the heat the local thermal path can carry away within the maximum tolerable temperature excursion $\Delta T_{\max}$, and decoherence becomes unavoidable regardless of how the code distance is chosen.

We call $N_c$ the thermodynamic feasibility limit. Its existence, if real, reframes scalability: the question is no longer only "how many physical qubits per logical qubit" but "does the thermal microenvironment of qubit $N_c + 1$ remain within specification." It also motivates a class of alternatives: substrates whose intrinsic energy gap suppresses thermal excitations as $e^{-\Delta_{\text{top}}/k_B T}$ without active feedback, so that their cooling requirement does not grow with control activity. Related proposals for passive, geometry-driven protection have been advanced in the p-adic ultrametric framework [11] and in the geodesic-evolution framework of Feynman matter [12]; fractional Chern insulators are the condensed-matter candidate for such passive topological substrates. We treat all of these as a hypothesis class, not a demonstrated technology.

This paper makes four contributions:

1. An explicit heat-balance model combining QEC overhead scaling with Kapitza-limited heat extraction, with every arithmetic step shown to the critical counts $N_c = 390$ (quadratic model) and $N_c \approx 738$ (exponential model) — derived in Sections 3 and 4.
2. Sensitivity results showing the threshold moves from $190$ to $3{,}990$ across plausible single-parameter changes, and logical-qubit budgets of 15 at $d=5$ and 7 at $d=7$ — derived in Section 4.
3. A local-stability condition, transposed from the catastrophic-cooling-instability analysis of coronal plasmas [8], giving a maximum tolerable dissipation–temperature feedback coefficient of $4 \times 10^{-7}\ \mathrm{W\,K^{-1}}$ per qubit — derived in Sections 3 and 4.
4. A Monte Carlo thermal-microenvironment protocol, specified but not executed, that would map micro-Kelvin temperature spikes and locate the breaking point empirically — specified in Section 3.4.

We stress the epistemic status of the central claim. It is a conjecture derived from a stylized model with assumed parameters. Its value lies in being falsifiable: each parameter is in principle measurable, and the threshold prediction moves measurably with each one.

## 2. Background and Related Work

The relevant literature spans stochastic thermodynamics, condensed-matter cooling, plasma astrophysics, robust statistics, and prior thermodynamic analyses of fault-tolerant quantum computation. We cite each work for the specific result its text establishes and use it accordingly.

[7] is the closest methodological relative. The work establishes a thermodynamic uncertainty relation (TUR) for feedback cooling in classical underdamped Langevin systems, deriving a trade-off between cooling efficiency and entropy reduction rate (its Eq. 29), and shows as a byproduct that non-negativity of one component of an orthogonal decomposition of the partial entropy production rate represents an information-thermodynamic cooling limit (its Eq. 19). This is precisely the tension we generalize: active QEC is measurement-based control applied continuously per qubit block, and [7] supplies the warrant that such control carries an irreducible thermodynamic cost that grows as one demands better effective cooling. Our model makes that cost concrete as wiring dissipation and asks when it overwhelms the cooling channel. We note in Section 6 that transplanting a classical Langevin bound to quantum error correction is a hypothesis, not a theorem.

[2] proposes using a single Cooper pair box (Josephson qubit) to actively cool nanomechanical resonators, noting that Josephson-qubit experiments had demonstrated coherence times of order microseconds at special symmetry points. Its conclusions quantify the achievable performance: for a 100 MHz oscillator coupled to a practically realizable Josephson qubit, at external temperatures below 1 K, the thermal occupancy of the oscillator mode can be reduced by three orders of magnitude with externally driven AC cooling, while a self-driven scheme using AC Josephson oscillations is found to be less effective. The work is relevant in two directions: it shows the same physical platform being used for active thermal management, and it documents that the coherence resource is finite and of order microseconds — the resource our heat load erodes.

[8] analyzes catastrophic cooling instability in optically thin plasmas, using the solar corona as the prototype of a low-density environment heated externally and cooled radiatively, with the MHD equations modified to include energy source terms. Its linear theory yields a wavenumber-independent dispersion relation $\sigma = -(1/c_V)(\partial\mathcal{L}/\partial T)_\rho$ for the catastrophic-cooling (CC) mode, and shows that because the CC mode cannot be stabilized by thermal conduction, it can lead to condensation formation even where the Field length exceeds perturbation wavelengths. The structural analogy is direct: a system with a heat source, a finite-capacity cooling channel, and a runaway mode when heating outruns cooling. Our Kapitza-limited qubit array is a solid-state cousin of this instability structure, and [8] supplies the precedent that such heating–cooling imbalance produces catastrophic rather than graceful degradation. We accordingly add an explicit stability condition to our model in Section 3.3.

[6] puts forward an alternative view of the feedback between heating and cooling in cooling-flow galaxy clusters, adopting the view that heating comes from an active galactic nucleus accreting mass and launching jets or winds, and proposing that the feedback occurs with the entire cool inner region ($r \lesssim 5$–$30\ \mathrm{kpc}$) rather than a localized Bondi radius. Its summary section lists four conditions the participating inner region must satisfy and gives a typical interval of $\approx 10^{8}\ \mathrm{yr}$ between heating events at a specific region. The work supports the principle that heating–cooling balance is a global, self-regulating quantity, not a purely local one — a principle we import when arguing that thermal microenvironments in qubit arrays couple through shared heat sinks.

[1] demonstrates a liquid crystal as a liquid barocaloric material with cooling potential, noting that its phase transition requires only a small stress (tens of MPa) and can be operated near room temperature, as an alternative to vapor compression based on gas–liquid transitions of hazardous gases. We cite it as evidence that the cooling-technology community actively seeks non-vapor-compression heat management; its text gives no cryogenic-relevant data, so we draw no quantitative claim from it for millikelvin operation.

[3] develops asymptotic breakdown point analysis for a general class of minimum divergence estimators, building on the density power divergence (DPD) family introduced by Basu et al. (1998) and the larger S-divergence class that subsumes it. Its conclusion reports that for many illustrated examples the asymptotic breakdown point is free of the dimension of the data for various contaminating distributions, justifying minimum S-divergence estimators as viable robust alternatives for high-dimensional parametric inference. This becomes directly useful in the Monte Carlo protocol of Section 3.4: robust estimation of heavy-tailed temperature-spike statistics requires estimators whose breakdown behavior is characterized, since single hot-spot events are heavy-tailed outliers.

[4] and [5] come from active-inference cognitive modeling, and we use them only as conceptual parallels. [4] frames cognitive effort as the cost of resolving the conflict between habits and optimal policies within an evidence-accumulator drift-diffusion account, and reports Bayesian model comparison in which the full AIF-DDM model was selected under AIC with protected exceedance probability 0.97. [5] models second-person social cognition as coupled active inference in which each agent maintains a self-model that tracks violations of its predictive coherence, formalizing affect as a valuation of identity-relevant surprise. Both support, at the level of analogy, the thesis that active control has a cost that scales with the intensity of control and that systems which must continuously correct themselves face a resource burden that passively stable systems avoid; neither text provides quantitative content transferable to qubit thermodynamics, and we claim none.

Three prior thermodynamic analyses of fault-tolerant quantum computation frame the debate this paper enters. [10] develops an integrated thermal equilibrium model that quantitatively links physical gate fidelity, QEC overhead, and cryogenic cooling capacity to determine the viability of a large-scale system, and uses the implementation requirements of Shor's algorithm as a case study in what it terms asymptotic infeasibility. [11] quantifies a "Thermodynamic Wall": for a surface code of distance $d$ the physical qubit count scales as $N = 2d^2 - 1$, each cycle generates entropy proportional to the parity-check frequency $f$ and measurement energy $E_{meas}$, and its simulations indicate that for $10^5$ qubits active QEC generates heat loads exceeding the 10–20 $\mu\mathrm{W}$ cooling capacity of standard dilution refrigerators at 10 mK; it then proposes a passive p-adic ultrametric substrate, noting a $\sim 10$ nm lithographic resolution cutoff that truncates the hierarchical barrier structure. [12] quantifies a "Protection Deficit" of approximately $10^{12}$ between the metabolic efficiency of biological systems and the energy cost of state-of-the-art engineered quantum processors, and argues that discrete forced control hits a thermodynamic wall while geodesic evolution on a quantum information manifold would not. Our contribution relative to [10], [11], and [12] is a closed-form, code-distance-independent threshold with explicit sensitivities and a stability condition, derived from a minimal heat-balance model whose every input is stated; a precursor formulation of the same conjecture appears in [9].

No cited work directly treats Kapitza conductance in qubit packages or measures per-qubit QEC dissipation; the quantitative model below is therefore original to this paper, and its parameters are stated assumptions rather than values taken from any cited work.

## 3. Methods

### 3.1 Heat generation model

Let $N$ be the number of physical qubits in the array. We model total heat generated inside the cold stage per unit time as

$$P_{\text{tot}}(N) = P_0\, N + \alpha\, N^2,$$

where $P_0$ is the per-qubit static and linear-control dissipation and $\alpha\, N^2$ is the quadratic routing term: each additional qubit adds control lines that must cross the wiring web of all previously added qubits, so routing dissipation grows as the square of qubit count. The quadratic routing term is a modeling hypothesis, not a derived law; we carry it because surface-code qubit counts themselves scale as $d^2$ [11], so the physical footprint of protection grows quadratically in the natural counting. The exponential alternative,

$$P_{\text{tot}}^{(\text{exp})}(N) = P_0\, N\, e^{N/N_e},$$

with characteristic wiring-density scale $N_e$, is analyzed in parallel because the source conjecture posits exponential growth of local thermal dissipation from control wiring.

### 3.2 Kapitza-limited extraction model

Each qubit site is coupled to the mixing-chamber heat sink through $\beta$ interconnects, each of Kapitza conductance $G_K$ (units $\mathrm{W\,K^{-1}}$). Kapitza conductance is the thermal boundary conductance at the interface between two solids; it is finite, material-dependent, and does not increase with system size. The total thermal conductance of the array is

$$G_{\text{tot}}(N) = \beta\, G_K\, N.$$

The maximum heat sustainable while keeping every qubit site within a temperature excursion $\Delta T_{\max}$ of the bath temperature $T_b$ is

$$P_{\text{ext}}^{\max}(N) = G_{\text{tot}}(N)\, \Delta T_{\max} = \beta\, G_K\, \Delta T_{\max}\, N.$$

### 3.3 Feasibility condition and stability

A steady state at temperature $T_b + \Delta T_{\max}$ exists if and only if

$$P_{\text{tot}}(N) \le P_{\text{ext}}^{\max}(N).$$

Dividing both sides by $N > 0$, the quadratic model gives

$$P_0 + \alpha\, N \le \beta\, G_K\, \Delta T_{\max},$$

so the critical count is

$$N_c = \frac{\beta\, G_K\, \Delta T_{\max} - P_0}{\alpha}.$$

For the exponential model, dividing by $N$ gives

$$P_0\, e^{N/N_e} \le \beta\, G_K\, \Delta T_{\max}
\quad\Longrightarrow\quad
N_c^{(\text{exp})} = N_e \ln\!\left(\frac{\beta\, G_K\, \Delta T_{\max}}{P_0}\right).$$

Both thresholds are independent of code distance $d$: increasing $d$ increases the number of physical qubits per logical qubit (as $d^2$ in the standard surface-code counting, consistent with the $N = 2d^2 - 1$ scaling quoted in [11]), which moves the array toward $N_c$ faster while buying logical protection. This is the formal content of the self-defeating regime: past $N_c$, more QEC resources strictly worsen the thermal environment.

Following the catastrophic-cooling-instability analysis of [8], we additionally require local stability. Writing the lumped energy balance as $C\,\dot{T} = P_{\text{gen}}(T) - G_{\text{tot}}(T - T_b)$, stability requires

$$\left.\frac{\partial P_{\text{gen}}}{\partial T}\right|_{T_b} < G_{\text{tot}},$$

i.e., any positive temperature feedback of dissipation on itself (e.g., hotter quasiparticles raising switching error rates and hence correction activity) must be weaker than the removal channel, or the system runs away catastrophically rather than saturating. This mirrors the plasma result that the catastrophic-cooling mode grows at rate $\sigma = -(1/c_V)(\partial\mathcal{L}/\partial T)_\rho$ and cannot be stabilized by thermal conduction [8]: in our lumped system, conduction to the bath is the only removal channel, so the sign of the feedback derivative decides between saturation and runaway.

### 3.4 Monte Carlo microenvironment protocol (proposed, not executed)

To locate the breaking point beyond the mean-field threshold, we specify: simulate arrays of $N \ge 1{,}000$ qubits; assign each qubit a heat-injection rate drawn from the per-qubit load with spatial clustering to mimic routing congestion; solve the discrete heat equation with per-interconnect Kapitza conductance as the extraction boundary; record the distribution of local temperature spikes $\delta T_i$ above $T_b$. The predicted signature is a heavy tail in $\delta T_i$ emerging as $N$ approaches $N_c$. Robust estimation of the spike statistics should use minimum-divergence estimators whose asymptotic breakdown behavior is characterized in [3], since single hot-spot events are heavy-tailed outliers and the breakdown-point results of [3] are dimension-free for many contaminating distributions. No results from this protocol are reported in this paper.

## 4. Analysis

Every input number below is a stated model assumption, not a measurement; the derivations are exact given the assumptions.

**Inputs (assumed):**

- $P_0 = 10^{-10}\ \mathrm{W}$ per qubit (linear dissipation).
- $\alpha = 10^{-11}\ \mathrm{W}$ per qubit (coefficient of the quadratic routing term).
- $G_K = 10^{-7}\ \mathrm{W\,K^{-1}}$ per interconnect.
- $\beta = 4$ interconnects per qubit.
- $\Delta T_{\max} = 10^{-2}\ \mathrm{K}$ (maximum tolerable excursion above the bath).
- $N_e = 200$ (exponential wiring-density scale, exponential model only).

**Step 1: extractable heat per qubit.**

$$\beta\, G_K\, \Delta T_{\max} = 4 \times 10^{-7}\ \mathrm{W\,K^{-1}} \times 10^{-2}\ \mathrm{K} = 4 \times 10^{-9}\ \mathrm{W}.$$

So each qubit site can shed at most $4 \times 10^{-9}\ \mathrm{W}$ while staying within $\Delta T_{\max}$.

**Step 2: quadratic-model threshold.**

$$N_c = \frac{4 \times 10^{-9} - 10^{-10}}{10^{-11}} = \frac{3.9 \times 10^{-9}}{10^{-11}} = 390.$$

Check by substitution at $N = 390$: generated heat is $P_{\text{tot}} = 10^{-10} \times 390 + 10^{-11} \times 390^2 = 3.9 \times 10^{-8} + 10^{-11} \times 152{,}100 = 3.9 \times 10^{-8} + 1.521 \times 10^{-6} = 1.560 \times 10^{-6}\ \mathrm{W}$. Extractable heat is $G_{\text{tot}} \Delta T_{\max} = 4 \times 10^{-7} \times 390 \times 10^{-2} = 1.560 \times 10^{-6}\ \mathrm{W}$. The two sides match exactly, confirming $N_c = 390$.

**Step 3: exponential-model threshold.**

$$N_c^{(\text{exp})} = N_e \ln\!\left(\frac{4 \times 10^{-9}}{10^{-10}}\right) = 200 \ln(40).$$

Since $\ln(40) = \ln(4) + \ln(10) \approx 1.386294 + 2.302585 = 3.688879$,

$$N_c^{(\text{exp})} = 200 \times 3.688879 = 737.7758 \approx 738.$$

Check by substitution at $N = 737.7758$: $e^{N/N_e} = e^{3.688879} = 40$ exactly, so per-qubit generation is $10^{-10} \times 40 = 4 \times 10^{-9}\ \mathrm{W}$, equal to the per-qubit extraction limit from Step 1. Confirmed.

**Step 4: sensitivity of the quadratic threshold to $\Delta T_{\max}$.** Since $N_c$ is linear in $\Delta T_{\max}$, halving the allowed excursion to $5 \times 10^{-3}\ \mathrm{K}$ halves the extraction budget to $2 \times 10^{-9}\ \mathrm{W}$ and gives

$$N_c = \frac{2 \times 10^{-9} - 10^{-10}}{10^{-11}} = \frac{1.9 \times 10^{-9}}{10^{-11}} = 190.$$

**Step 5: sensitivity to Kapitza conductance.** A tenfold improvement, $G_K = 10^{-6}\ \mathrm{W\,K^{-1}}$, gives extraction $4 \times 10^{-8}\ \mathrm{W}$ per qubit and

$$N_c = \frac{4 \times 10^{-8} - 10^{-10}}{10^{-11}} = \frac{3.99 \times 10^{-8}}{10^{-11}} = 3{,}990.$$

**Step 6: code-distance trade.** In the standard surface-code counting, physical qubits per logical qubit scale as $d^2$. At $d = 5$, one logical qubit costs $25$ physical qubits; the quadratic model therefore supports at most $\lfloor 390 / 25 \rfloor = 15$ logical qubits at distance $5$ before the thermal budget is exhausted — under the stated assumptions. At $d = 7$ the cost is $49$ physical qubits per logical qubit, giving $\lfloor 390/49 \rfloor = 7$ logical qubits. Increasing $d$ from $5$ to $7$ buys a lower logical error rate but consumes the thermal budget more than twice as fast per logical qubit, which is the quantitative form of the self-defeating regime.

**Step 7: crossover between models.** The quadratic model fails first ($390 < 738$) under these parameters; the exponential model's larger threshold arises because its per-qubit load $P_0 e^{N/N_e}$ equals $P_0 = 10^{-10}\ \mathrm{W}$ at $N = 0$ and only reaches the extraction limit at $N \approx 738$, whereas the quadratic model's per-qubit load $P_0 + \alpha N$ grows linearly and reaches the limit at $N = 390$. The two models bracket the threshold between $390$ and $738$ qubits under the stated assumptions.

**Step 8: stability margin.** With the reference numbers, the removal channel coefficient is $G_{\text{tot}}/N = \beta G_K = 4 \times 10^{-7}\ \mathrm{W\,K^{-1}}$ per qubit. The stability condition of Section 3.3 requires the temperature feedback coefficient of dissipation to stay below this value; if each millikelvin of heating raises per-qubit dissipation by more than $4 \times 10^{-10}\ \mathrm{W}$, the array runs away rather than saturating. This is the catastrophic-instability analog of [8] transposed to the cryostat.

**Step 9: cross-check against dilution-refrigerator capacity.** [11] states that standard dilution refrigerators provide 10–20 $\mu\mathrm{W}$ of cooling capacity at 10 mK and that $10^5$ actively corrected qubits exceed this capacity. Under our assumed coefficients, the total array heat at $N = 390$ is $1.560 \times 10^{-6}\ \mathrm{W} = 1.56\ \mu\mathrm{W}$ (Step 2), which is below 10 $\mu\mathrm{W}$; at $N = 10^5$, the same coefficients give $P_{\text{tot}} = 10^{-10} \times 10^{5} + 10^{-11} \times (10^{5})^2 = 10^{-5} + 10^{1} = 10.00001\ \mathrm{W}$, dominated by the quadratic term and exceeding 20 $\mu\mathrm{W}$ by a factor of $10.00001 / (2 \times 10^{-5}) \approx 5.0 \times 10^{5}$. This consistency check uses our assumed coefficients, not those of [11]; it shows only that our model, so parameterized, reproduces the qualitative statement of [11] that $10^5$ qubits overwhelm a standard refrigerator, and it locates the quantitative disagreement in the routing coefficient $\alpha$, which no cited work measures.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions; they are model projections conditional on those assumptions, not measurements.

1. **Quadratic-overhead threshold:** $N_c = 390$ physical qubits (exact under the assumed parameters; verified by substitution in Step 2).
2. **Exponential-overhead threshold:** $N_c^{(\text{exp})} = 737.7758 \approx 738$ physical qubits (verified by substitution in Step 3).
3. **Sensitivity to allowed temperature excursion:** $N_c = 190$ if $\Delta T_{\max}$ is halved to $5 \times 10^{-3}\ \mathrm{K}$ (Step 4).
4. **Sensitivity to Kapitza conductance:** $N_c = 3{,}990$ if $G_K$ improves tenfold to $10^{-6}\ \mathrm{W\,K^{-1}}$ (Step 5).
5. **Logical-qubit budget at the quadratic threshold:** $15$ logical qubits at code distance $d = 5$; $7$ logical qubits at $d = 7$ (Step 6).
6. **Threshold bracket:** under the stated assumptions, the thermodynamic feasibility limit lies between $390$ and $738$ physical qubits (Step 7).
7. **Stability bound:** the maximum tolerable dissipation–temperature feedback coefficient is $\beta G_K = 4 \times 10^{-7}\ \mathrm{W\,K^{-1}}$ per qubit in the reference geometry (Step 8).
8. **Refrigerator-capacity cross-check:** at $N = 390$ the modeled total array heat is $1.56\ \mu\mathrm{W}$, below the 10–20 $\mu\mathrm{W}$ capacity quoted in [11]; at $N = 10^5$ the same coefficients give $10.00001\ \mathrm{W}$, a factor of $\approx 5.0 \times 10^{5}$ above 20 $\mu\mathrm{W}$ (Step 9).

The Monte Carlo protocol of Section 3.4 is proposed but not executed; no simulation results are claimed. As a labeled projection only: if that protocol were run with the reference parameters, we expect hot-spot-driven threshold crossing within the sensitivity range of items 3–4, i.e. $N_c$ spanning roughly $10^{2}$–$10^{4}$ across plausible parameter variation; this is a projection from the analytic model with uncertainty at least spanning that range, not a simulation result.

## 6. Discussion

**Limitations.** The model is mean-field: it assumes uniform heat injection and uniform Kapitza conductance, whereas real arrays have hot spots near dense routing regions, so the true breaking point may lie below the mean-field $N_c$. The parameters $P_0$, $\alpha$, $G_K$, $\beta$, $\Delta T_{\max}$, and $N_e$ are assumptions chosen to be physically plausible in magnitude, not measured values; every headline number scales linearly (or, for the exponential model, logarithmically) with them, and the sensitivity results (Steps 4–5) show the threshold spans more than an order of magnitude across plausible parameter ranges. The quadratic routing term is a modeling hypothesis, not a derived law; if routing dissipation in fact grows only linearly, the quadratic model reduces to a per-qubit budget comparison and no finite threshold exists at all — the feasibility condition becomes $P_0 \le \beta G_K \Delta T_{\max}$, which is satisfied by a factor of $40$ under the assumed numbers. This is the single most important internal vulnerability of the conjecture. The literature base is also a limitation: no cited work measures Kapitza conductance in qubit packages, per-qubit dissipation budgets, or overhead-scaling exponents, so no cited work constrains any input number.

**Failure modes of the claim.** The conjecture would be falsified if: (i) measured per-qubit dissipation in operating Q