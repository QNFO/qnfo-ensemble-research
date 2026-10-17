# Network Tracing Capacity as an Informational Event Horizon: A Delay-Based Causal Bound for Networked Control

## Abstract

Distributed control systems—power electronics clusters, vehicle platoons, coordinated robot fleets—stabilize unstable plants through communication networks, and the latency of that communication, not the control law, frequently decides whether stabilization succeeds. Existing design practice treats this as a per-application tuning problem; no topology-level invariant is known that states, in one number, which instability rates a given communication topology can and cannot propagate. We propose such an invariant, the Network Tracing Capacity (NTC), defined for a benchmark class of scalar unstable modes under delayed feedback as $\Theta = 1/(h\tau)$, where $h$ is the controller-to-sensor hop count and $\tau$ the per-hop delay, and we conjecture that modes with growth rate $\lambda > \Theta$ are practically unobservable through the topology, a boundary we interpret as an informational analog of a relativistic event horizon. We build the correspondence mapping (instability rate, delay, hop count) onto (expansion rate, signal speed, metric scale), anchor its operational criteria in how the Event Horizon Telescope actually detects and is limited by horizons, and derive a worked example: a five-hop network with $\tau = 10\,\mathrm{ms}$ yields $\Theta = 20\,\mathrm{s^{-1}}$, so a plant with $\lambda = 35\,\mathrm{s^{-1}}$ lies beyond the horizon at hop $3$ of $5$, with state growth factor $e^{1.75} \approx 5.75$ per delay interval. The result, if validated, converts latency budgets into hop-count-aware instability-rate budgets for control topology design.

## 1. Introduction

Engineers who close control loops over communication networks face a failure mode that no amount of controller gain can remove. When the plant is unstable with growth rate $\lambda$ and the measurement of its state must travel $h$ communication hops, each with delay $\tau$, the controller acts on information about a state that has already grown by a factor $e^{\lambda h \tau}$ since it was measured. Beyond a critical product of instability rate, hop count, and per-hop delay, the loop diverges regardless of the algorithm at either end. The practitioners who hit this wall are the designers of networked control systems: distributed power-electronics clusters, platooning vehicles, teleoperated and swarm robotics, and any plant whose sensors and actuators are separated by a multi-hop network. Today the boundary is found per deployment, empirically, by tuning and testing; a design that works on one topology silently fails when a routing change adds a hop. What is missing is a single, topology-level number that tells the designer, before deployment, which instability rates the topology can propagate and which it structurally cannot.

If such a number exists and has the character we conjecture—an informational event horizon, analogous to the causal horizon that the speed of light $c$ creates in spacetime—then three things change. First, controllability and observability analysis acquires a topology-independent bound: the question "can this plant be stabilized over this network?" becomes a comparison of two scalars, $\lambda$ and $\Theta$, computable from the graph and its latencies alone. Second, the design lever shifts from controller synthesis to topology and latency engineering, because $\Theta$ depends only on $h$ and $\tau$. Third, control-theoretic observability and relativistic causality would be unified under one invariance principle: in both settings, a finite propagation speed creates a boundary beyond which information about a region ceases to influence—and cease to be recoverable from—observations.

This paper is a first, deliberately modest step toward that conjecture. We do not prove a general theorem for all networked control systems; we construct the benchmark class in which the claim is derivable, derive the threshold with explicit arithmetic, and state precisely what would falsify the analogy. Our contributions are:

- We define the Network Tracing Capacity $\Theta(G,\tau) = 1/(h_{\max}\tau)$ for a communication topology $G$ with uniform per-hop delay $\tau$, and the horizon condition $\lambda < \Theta$, under a stated benchmark criterion for delayed stabilization of a scalar unstable mode (Section 3, formalized and derived in Section 4).
- We construct the explicit correspondence mapping from (instability rate $\lambda$, per-hop delay $\tau$, hop count $h$) onto (expansion rate, invariant signal speed, metric scale), and identify the operational criteria any horizon analog must satisfy (Section 3).
- We derive, with full arithmetic, a worked example: for $h = 5$ hops and $\tau = 10\,\mathrm{ms}$, $\Theta = 20\,\mathrm{s^{-1}}$; a plant with $\lambda = 35\,\mathrm{s^{-1}}$ crosses the horizon at hop $3$, and the state grows by $e^{1.75} \approx 5.75$ across the full delay; reducing $\tau$ to $2\,\mathrm{ms}$ restores $\Theta = 100\,\mathrm{s^{-1}} > \lambda$ (Sections 4 and 5).
- We assess the analogy against the operational practice of horizon science—how the Event Horizon Telescope detects horizon-scale structure and where its inference demonstrably degrades—and state the falsification condition for the control-side claim (Sections 2, 6, and 7).

## 2. Background and Related Work

The physical side of our analogy rests on how event horizons are actually observed, not merely defined. The Event Horizon Telescope (EHT) is a global very long baseline interferometry (VLBI) array operating at $1.3\,\mathrm{mm}$ wavelength, composed of millimeter/submillimeter telescopes scattered across the globe—from Hawaii and Arizona to Chile, Mexico, the South Pole, and Spain and France—with the primary goal of imaging supermassive black holes at a few gravitational radii $r_g$ [1]. Two features of this program matter for us. First, the horizon manifests observationally as a stable geometric scale: the $1.3\,\mathrm{mm}$ emission regions in Sgr A* and M87 have an effective size of only a few $r_g$, and their small sizes combined with weak infrared emission are the core of the observational case that these sources possess event horizons [1]. Second, the horizon-scale structure is measured to be stable across years: reanalyses of M87* across the 2017, 2018, and 2021 epochs find ring diameters of $[42.0, 46.4]\,\mu\mathrm{as}$ in 2017, $[40.7, 44.4]\,\mu\mathrm{as}$ in 2018, and $[43.1, 44.4]\,\mu\mathrm{as}$ in 2021, consistent across methods and epochs, exactly as accretion theory predicts for a geometry-set scale [5]. A horizon, operationally, is a boundary whose geometric signature is invariant even as the plasma near it varies—a property our proposed $\Theta$ threshold is meant to share.

The same literature also demonstrates where inference near a horizon degrades, which is the behavior our unobservability claim mirrors. The first EHT analysis of circular polarization in M87* developed five independent imaging approaches, all validated on synthetic data from GRMHD simulations, and all found a moderate degree of image circular polarization; yet the reconstructed circular polarization structures vary considerably among the five methods, and the collaboration concludes that the structure cannot be reliably inferred without additional data or stronger assumptions [2]. For Sgr A*, dynamic imaging and geometric snapshot modeling of minute-timescale variability recover the position angle in some synthetic GRMHD movies but produce prominently biased results in others [3]. This is precisely the phenomenology of an informational boundary: observables that straddle the horizon carry information that reconstruction cannot fully recover, and different pipelines disagree because the missing information is not a noise problem but a causal one. The Sgr A* campaign itself illustrates the cost of fighting variability across a delay-limited aperture: Sgr A* is highly variable, with flickering and flares on short timescales, and among known black holes it has the largest predicted angular size, approximately $50\,\mu\mathrm{as}$ [6]; the 2017 imaging relied on the best-coverage day, April 7, because April 11 showed the highest light-curve variability, rendering static imaging for that day particularly challenging [3]. Calibration of such variable sources required novel methods and two independent pipelines, EHT-HOPS and rPICARD [6].

Horizon-scale imaging also feeds back into fundamental tests, which shows what a mature "horizon metrology" can deliver. The Sgr A* images constrain deviations from the Kerr metric—the only stationary, vacuum, axisymmetric, uncharged solution of Einstein's equations without pathologies outside the event horizon—and the combination of imaging with infrared limits strengthens the argument that Sgr A* lacks a thermalizing surface, because the discrepancy between the maximum steady infrared luminosity the source can have and the minimum luminosity a surface would produce is too large to be circumvented by small model fixes [8]. The mid-range science program extends this metrology toward dynamics, including the untested prediction that the M87* jet is powered by the black hole's spin through an analog of the Penrose process, while the operational cycle—observations proposed a year ahead, nearly a year to assemble recorded data at correlator sites, and another year for calibration and validation—shows how severely finite information transport rates bind even flagship science [4]. Polarized emission at $230\,\mathrm{GHz}$ around M87, imaged on event-horizon scales, probes magnetic-field structure and plasma properties near the horizon [7], completing the picture of a boundary that is probed, bounded, and exploited rather than merely postulated.

On the network side, the closest precedent for cross-domain structural claims is the framework of network isomorphism, which defines isomorphism as exact structural equivalence—two networks are isomorphic if one transforms into the other by moving and relabeling nodes without altering connections—and argues that equivalence between complex systems cannot be captured by a single measure but must be assessed progressively across layers of topological structure, functional architecture, and dynamic behavior, packaged methodologically as the L1–L2–L3 isomorphism hierarchy and the Abstract Network Object [9]. Our correspondence mapping is a dynamic-layer (L3) claim in exactly that sense: we do not claim that a communication topology is geometrically isomorphic to spacetime, but that a dynamically defined quantity—the propagatable instability rate—maps onto a dynamically defined relativistic quantity. A second precedent establishes that physics–network-engineering isomorphisms can be made productive: the topological extension framework models entities as finite-volume stable modes of nonlinear evolution equations, asserts that "existence" is functionally equivalent to "persistence" of a mode against dispersive forces, and maps the screening mechanisms of cosmological chameleon fields onto route flap damping protocols in interdomain routing, yielding a structural isomorphism in which stability is maintained by a conserved topological charge and environmental coupling [11]. Our horizon conjecture follows the same pattern—identify a mechanism (causal suppression of instability) that recurs in two domains and give it one name.

Finally, the methodological template for turning a structural analogy into checkable arithmetic comes from the boundary-crossing-path theory of network emergence. That work proves, verified by exhaustive enumeration on a reference network, that for route-accumulating observations the emergence discrepancy equals the boundary-touching walk count exactly, with per-length values $D^{(1)} = 4$, $D^{(2)} = 12$, $D^{(3)} = 28$ (cumulative $44$) and closed-form growth $D_{\le L} = 2^{L+3} - 8 - 4L$, giving $D_{\le 5} = 220$ and $D_{\le 10} = 8144$; its discussion is explicit that the identity holds for a narrow class of observations and that weighted or stochastic interactions would require replacing walk counts by weighted path sums [10]. We adopt the same discipline: derive the bound exactly in a narrow benchmark class, state the class boundary, and treat generalization as an open question rather than an assertion.

What no cited work provides—and what motivates this paper—is a quantitative, topology-level threshold at which a networked control loop transitions from observable to unobservable, phrased so that the threshold can be compared, term by term, with a relativistic horizon. The EHT literature supplies the operational anatomy of a horizon; the network-isomorphism literature supplies the licensing for cross-domain mappings; the missing piece is the control-theoretic derivation, which Sections 3 and 4 supply for the benchmark class.

## 3. Methods

### 3.1 Benchmark plant and communication model

We consider the minimal object to which the conjecture can be applied without ambiguity: a scalar unstable plant mode

$$
\dot{x}(t) = \lambda x(t) + u(t), \qquad \lambda > 0,
$$

whose state $x(t)$ is measured at a sensor node and must reach a controller node across a communication topology $G$ along a path of $h$ hops, each hop imposing a deterministic transport delay $\tau$. The total information delay is

$$
\tau_d = h \tau .
$$

We assume deterministic delays, no packet loss, and a single dominant unstable mode; these restrictions are load-bearing and are revisited in Section 6.

### 3.2 The benchmark stabilization criterion

The derivation requires a criterion that separates "stabilizable over the network" from "not stabilizable over the network." We adopt the following as the defining criterion of the benchmark class, stated openly as a modeling assumption rather than as established literature:

**Assumption A1 (delay-budget criterion).** A delayed-feedback scheme for the scalar mode maintains bounded estimation and control error only if the uncontrolled growth accumulated over one full information delay is at most a factor $e$; that is,

$$
\lambda \tau_d \le 1 .
$$

The rationale is a growth-versus-correction budget: over one delay interval $\tau_d$, the uncontrolled state grows by $e^{\lambda \tau_d}$, and the controller must undo this accumulated growth using information that is itself $\tau_d$ old. We take unity exponent as the boundary of the benchmark class because it is the value at which the growth over one delay equals the natural exponential scale of the mode itself; the qualitative structure of everything below is unchanged if the constant is replaced by any fixed $\kappa$, with the threshold rescaled to $\kappa/(h\tau)$. Choosing the constant is a modeling decision; the paper's claim is about the structure of the threshold, not the value of its constant.

### 3.3 Network Tracing Capacity and the horizon condition

Under Assumption A1, the largest instability rate the topology can propagate is

$$
\Theta(G, \tau) \;=\; \frac{1}{h \tau} \;=\; \frac{1}{\tau_d},
$$

which we call the Network Tracing Capacity (NTC) of the topology. The horizon condition is

$$
\lambda < \Theta \quad \Longleftrightarrow \quad \lambda h \tau < 1 .
$$

Modes with $\lambda \ge \Theta$ are declared beyond the horizon in the benchmark class: no controller at the far end of an $h$-hop, $\tau$-delay path can stabilize them, because the information on which it acts describes a state that has grown by more than the criterion allows.

### 3.4 The correspondence mapping

The conjectured isomorphism assigns, term by term:

| Networked control | Relativistic spacetime |
|---|---|
| Instability rate $\lambda$ | Local expansion rate of the congruence of worldlines |
| Per-hop delay $\tau$, hop count $h$ | Metric scale; invariant speed $c$ sets $\tau$ per unit distance |
| NTC $\Theta = 1/(h\tau)$ | Invariant speed $c$ as the propagatable rate bound |
| Hop index $k$ with $\lambda k \tau = 1$ | Horizon radius: the last surface sending signals that arrive |
| $\lambda \tau_d > 1$: unobservable mode | Region beyond the horizon: causally disconnected |

The mapping is structural, not physical: no claim is made that network delay is Lorentz-invariant or that instability is geometric expansion. The claim is that both systems instantiate the same mechanism—a finite propagation rate interacting with a super-linear-growing quantity creates a sharp boundary beyond which information about the growing quantity cannot reach the observer in usable form.

### 3.5 Operational criteria for a horizon analog

Borrowing the operational anatomy of horizon science (Section 2), we require that a genuine informational horizon satisfy three criteria: (O1) the boundary is a function of structure and propagation rate alone, not of the observer's algorithm; (O2) the boundary's location is stable under variation of conditions away from the boundary, as the M87* ring diameter is stable across 2017–2021 [5]; (O3) inference about states beyond the boundary degrades in a way that is pipeline-dependent rather than noise-limited, as the M87* circular polarization structure "cannot be reliably inferred without additional data or stronger assumptions" across five independent methods [2]. Criterion O1 is built into the definition of $\Theta$; O2 and O3 are what the simulation program of Section 7 must test.

## 4. Analysis

Every number in this section is derived from the inputs stated here: $h = 5$ hops, per-hop delay $\tau = 10\,\mathrm{ms} = 0.01\,\mathrm{s}$ (Scenario 1), $\tau = 2\,\mathrm{ms} = 0.002\,\mathrm{s}$ (Scenario 2), and plant instability rate $\lambda = 35\,\mathrm{s^{-1}}$. The criterion constant is $1$ (Assumption A1).

**Step 1: Total information delay, Scenario 1.**

$$
\tau_d = h \tau = 5 \times 0.01\,\mathrm{s} = 0.05\,\mathrm{s} = 50\,\mathrm{ms}.
$$

**Step 2: Network Tracing Capacity, Scenario 1.**

$$
\Theta = \frac{1}{\tau_d} = \frac{1}{0.05\,\mathrm{s}} = 20\,\mathrm{s^{-1}}.
$$

**Step 3: Horizon test.** The plant has $\lambda = 35\,\mathrm{s^{-1}}$. Compare:

$$
\lambda \tau_d = 35 \times 0.05 = 1.75 > 1,
$$

so $\lambda = 35\,\mathrm{s^{-1}} > \Theta = 20\,\mathrm{s^{-1}}$: the mode lies beyond the horizon in the benchmark class.

**Step 4: Growth factor across the full delay.** The uncontrolled state grows, over one full information delay, by

$$
e^{\lambda \tau_d} = e^{1.75}.
$$

Computing: $e^{1.75} = e^{1} \cdot e^{0.75}$; $e^{0.75} \approx 2.117000$ (since $e^{0.7} \approx 2.013753$ and $e^{0.05} \approx 1.051271$, so $e^{0.75} \approx 2.013753 \times 1.051271 \approx 2.117000$). Hence

$$
e^{1.75} \approx 2.718282 \times 2.117000 \approx 5.754603 \approx 5.75.
$$

Each delay interval, the controller's information describes a state $5.75$ times smaller than the current one, and the deficit compounds every interval—this is the divergence mechanism behind the horizon.

**Step 5: Location of the horizon in hop space.** The horizon condition in hop index $k$ is $\lambda k \tau < 1$, i.e., $k < 1/(\lambda \tau)$. Compute:

$$
\frac{1}{\lambda \tau} = \frac{1}{35 \times 0.01} = \frac{1}{0.35} = 2.857142\ldots \approx 2.86.
$$

Hops $k = 1$ and $k = 2$ give $\lambda k \tau = 0.35$ and $0.70$, both below $1$: information arriving from one or two hops away is inside the horizon. Hop $k = 3$ gives $\lambda k \tau = 1.05 > 1$: the horizon sits between hop $2$ and hop $3$, so the effective horizon hop is

$$
h^* = \left\lceil \frac{1}{\lambda \tau} \right\rceil = 3 .
$$

Of the $h = 5$ hops, $h - h^* = 2$ hops lie beyond the horizon: state information originating at those distances cannot be used for stabilization in the benchmark class, even though the packets physically arrive.

**Step 6: The topology lever, Scenario 2.** Reduce the per-hop delay to $\tau = 2\,\mathrm{ms} = 0.002\,\mathrm{s}$ at unchanged hop count:

$$
\tau_d = 5 \times 0.002 = 0.01\,\mathrm{s}, \qquad \Theta = \frac{1}{0.01} = 100\,\mathrm{s^{-1}}.
$$

Now $\lambda = 35\,\mathrm{s^{-1}} < \Theta = 100\,\mathrm{s^{-1}}$, and the horizon test gives $\lambda \tau_d = 35 \times 0.01 = 0.35 < 1$: the same plant, same controller, same hop count, is inside the horizon. The growth factor per delay drops from $e^{1.75} \approx 5.75$ to

$$
e^{0.35} \approx 1.419068 \approx 1.42 .
$$

**Step 7: Scaling law.** From $\Theta = 1/(h\tau)$, the NTC scales inversely in each factor: doubling the hop count halves $\Theta$; halving the per-hop delay doubles it. Formally, for a fractional change,

$$
\frac{\Delta \Theta}{\Theta} \approx -\frac{\Delta h}{h} - \frac{\Delta \tau}{\tau},
$$

to first order. The horizon hop moves as $h^* = \lceil 1/(\lambda\tau) \rceil$, independent of total hop count: adding hops never rescues a mode once $\lambda \tau \ge 1$ per hop pair budget is exceeded at the required distance—it only pushes more of the path beyond the horizon.

**Step 8: What the derivation establishes and what it does not.** Steps 1–7 establish: within the benchmark class (scalar mode, deterministic delays, Assumption A1), the topology admits a single propagatable-rate number $\Theta$, a sharp horizon condition, a computable horizon hop $h^*$, and a topology-only lever. The derivation does not establish that Assumption A1 holds for general plants, vector states, stochastic delays, or packet loss; those extensions are open (Section 6). The strong conjecture of the research program—that the boundary is a structural analog of a relativistic event horizon rather than an engineering limitation—is supported here only to the extent that the benchmark threshold exhibits criteria O1–O3; O1 holds by construction, O2 and O3 are untested and are the target of the falsification test in Section 7.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are measured or simulated.

**R1 (NTC of the reference topology).** For $h = 5$ hops and $\tau = 10\,\mathrm{ms}$, the Network Tracing Capacity is $\Theta = 20\,\mathrm{s^{-1}}$ (Section 4, Step 2).

**R2 (Horizon crossing).** A plant mode with $\lambda = 35\,\mathrm{s^{-1}}$ exceeds the NTC ($\lambda \tau_d = 1.75 > 1$) and is beyond the horizon in the benchmark class (Step 3).

**R3 (Growth factor).** Across one full information delay, the uncontrolled state grows by $e^{1.75} \approx 5.75$ (Step 4).

**R4 (Horizon hop).** The horizon sits between hops $2$ and $3$: $h^* = \lceil 1/(0.35) \rceil = 3$,