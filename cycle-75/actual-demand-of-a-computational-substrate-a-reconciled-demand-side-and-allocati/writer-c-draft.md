# Actual Demand of a Computational Substrate: An Allocation-Theoretic Framework for Post-Classical Computing

## Abstract

Debates about novel computational substrates—reservoir systems, post-qubit quantum architectures, thermodynamics-limited devices—rarely ask the economic question: what is the *actual demand* for such a substrate, and how should capacity against that demand be provisioned? We propose an allocation-theoretic framework that treats a computational substrate as a capacity-constrained service whose demand stream must be forecast, filtered, and served online. The framework imports three ideas from the demand-allocation literature: online allocation under non-linear constraints, filtering of partially observed non-stationary demand, and demand-conditioned task specification. We couple this to physical floor costs derived from the Landauer bound and from quantum error-correction overhead factors of $10^{2}$–$10^{3}$ physical operations per logical operation. We derive explicit numbers: a Landauer floor of $2.871\times10^{-21}$ J per operation at $T=300$ K, a per-logical-operation floor range of $2.871\times10^{-19}$ to $2.871\times10^{-18}$ J under the stated overhead assumption, and a two-state provisioning model in which waste and shortfall trade off symmetrically at $0.168$ of peak demand. The framework yields a falsifiable criterion—realized utilization $\rho$ against a computed break-even—for when a substrate's actual demand justifies its existence, independent of its physical implementation.

## 1. Introduction

Every proposed computational substrate arrives with a claim about what it will compute. Far fewer arrive with a claim about who will demand that computation, at what rate, with what variance, and at what physical cost floor. This asymmetry is not benign. A substrate whose capacity is provisioned against an imagined demand profile wastes resources when demand is low and fails its users when demand spikes; a substrate whose floor cost per operation exceeds what any realistic workload can pay is stillborn regardless of its theoretical power.

The present paper takes its cue from a question posed in the QNFO corpus: after the critique of qubit-centred ontology, what is the *actually demanded* role of a computational substrate [9], [11]? Rather than answering at the level of ontology, we answer at the level of allocation theory. We model a substrate as a server with capacity $C$ (operations per second) facing a stochastic demand stream $d(t)$ (demanded operations per second), and we ask three questions:

1. **Forecasting**: what structure does demand for a novel substrate have, and how much history does a forecaster need?
2. **Allocation**: how should capacity be provisioned online when demand is only partially observable and non-stationary?
3. **Floor cost**: what is the minimum thermodynamic price per operation, and how do error-correction overheads multiply it?

The answers combine into a single criterion: a substrate is *actually demanded* if its realized utilization $\rho = D_{\text{act}}/(C\,T_{\text{horizon}})$ exceeds a break-even threshold computed from its floor cost and its fixed provisioning cost. Our contribution is not a new algorithm but a framework that makes the demand question explicit and quantitative for substrates—physical reservoirs, post-qubit quantum architectures, thermodynamically bounded devices—where it is usually left implicit.

The paper proceeds as follows. Section 2 reviews the related literature. Section 3 defines the demand, allocation, and cost models. Section 4 carries out all derivations with explicit arithmetic. Section 5 reports results. Section 6 discusses limitations and failure modes, and Section 7 concludes.

## 2. Background and Related Work

We draw on two literatures that rarely meet: the physics-of-computation and substrate-characterization literature, and the demand-forecasting-and-allocation literature.

**Substrate characterization.** Cucchi et al. [1] formalize the Reservoir Computing (RC) framework, in which any non-linear, input-driven dynamical system exhibiting fading memory and input separability can be trained to perform computational tasks; this broad inclusion criterion has led to many new physical substrates for RC, with essential computational properties tuned through reconfiguration of the substrate. This is the clearest existing statement that "substrate" is a functional, not material, category—exactly the abstraction our demand framework requires. If substrates are interchangeable at the functional level, then competition among them is governed by demand-side and cost-side quantities, not by implementation details. The entry supplied for [1] is truncated and gives no experimental results, so we use it only for the framework statement.

**Post-qubit critique.** The QNFO corpus supplies the motivating position. *The Qubit Delusion* [11] argues that the qubit-gate-circuit model is an epistemic failure—a projection of particle ontology onto relational, field-theoretic reality; the supplied entry is a revision note (v1.1, fixing PDF rendering of Unicode dashes) and states no technical content beyond the title's thesis, so we cite it only as the source of the critique. Its companion, *Beyond the Qubit* [9], asks what comes next if that model fails: it strips quantum mechanics to its minimal ontological commitments and surveys constructive paradigms for post-particle computation; again the entry is truncated, and we rely on it for the framing question only. *No Thing There* [10] is described as a pedagogical bridge between the qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped-ion, and spin qubit platforms, including an electrical seesaw analogy and a self-referential metrology formalization; this supports our insistence that substrate capacity be defined at the level of what is actually controllable and measurable, not at the level of notional Hilbert-space resources. Most quantitatively relevant here, *The Physics of Computation* [12] examines fundamental physical limits—Landauer bound, Margolus-Levitin theorem, Bremermann limit, Bekenstein bound—and states that quantum error-correction overhead of $10^{2}$–$10^{3}$ physical operations per logical operation multiplies thermodynamic cost. We take the overhead range $r \in [10^{2}, 10^{3}]$ directly from this entry and use it as the multiplier in our floor-cost derivation in Section 4.

**Demand forecasting.** EXAONE Demand 1.0 [3] is a time series foundation model for demand forecasting, motivated by the observation that demand series have properties that general-purpose corpora rarely contain: short histories, frequent zeros, censoring by stock-outs, and exogenous events that the series does not record. Each of these pathologies has an exact analogue for a novel computational substrate: deployment histories are short, utilization can be zero for long stretches, observed "demand" is censored by capacity stock-outs (requests refused are often unrecorded), and exogenous events (algorithmic breakthroughs, hardware failures) are not recorded in the usage series. We adopt [3]'s taxonomy of demand-pathologies as the specification of what a substrate-demand forecaster must handle; the entry supplied does not report forecast accuracy numbers, so we make no quantitative claim from it.

**Online allocation under constraints.** The online demand-response literature [2] studies allocating incoming elastic or inelastic demands without violating network operating constraints, in an online fashion, highlighting non-linear constraints as the distinctive challenge of power systems relative to traditional online decision problems. Computational substrates face the same structure: demand arrives online, some of it is inelastic (a deadline-bound workload cannot be deferred), and the constraints (capacity $C$, thermodynamic floor) are non-linear in the decision variables. We import the elastic/inelastic distinction from [2] as a primitive of our model.

**Partially observed non-stationary demand.** The inventory model of [8] considers continuous-time inventory management with Markov-modulated non-stationary demands, introduces active learning by assuming the state of the world is unobserved and must be inferred by the manager, assumes demands are observed only when completely met, and derives explicit filtering equations passing to an equivalent fully observed impulse-control problem. The "observed only when completely met" assumption is precisely the stock-out censoring that [3] identifies in demand data; for substrates it means that refused jobs are invisible, so the demand process must be filtered, not merely measured. We use the two-state Markov-modulated structure of [8] as the skeleton of our illustrative demand model.

**Demand-conditioned specification.** The demand-driven navigation work of [6] learns a demand-conditioned object attribute space so that an agent can locate an object when the user knows its name and the object is actually present in the scene. Transposed to substrates, this separates *what is demanded* (a task specification) from *whether the substrate can actually supply it* (presence in the scene); a substrate demand model must therefore condition on task attributes, not just on aggregate operation counts. The supplied entry describes the task conditions and the simulator-based approach but gives no quantitative results, so we use it conceptually.

**Differentiation and verification tools.** The adjoint-computation work of [4] differentiates a parallel computational fluid dynamics solver in tangent and adjoint modes, with the novelties that the AD tool Tapenade inverts the complete MPI communication layer and that the adjoint code integrates time-dependent, non-linear and dissipative dynamics. For us this is the model of how a substrate's *sensitivity*—the derivative of outcome quality with respect to substrate parameters—can be computed at all in a realistic, communication-coupled, time-dependent setting; a demand model that cannot be differentiated against substrate parameters cannot be optimized. The entry is truncated and reports no specific performance figures. Persistent Stiefel-Whitney classes [5] offer a stable, consistent topological invariant for vector-bundle filtrations seen as subsets of Euclidean spaces, applicable when the dataset is a finite sample of a line bundle; we cite this as an example of structure-preserving invariants that could certify when two substrates are topologically equivalent as resource manifolds—a sufficient condition for demand to transfer between them—while noting the entry gives no computational-cost data. Finally, the ASPOCP 2018 proceedings [7] record a workshop held in Oxford, UK, on July 18th, 2018, on answer set programming and other computing paradigms; the entry supplies no further detail, and we reference it only as evidence that declarative, non-numeric computing paradigms sustain an active community whose demand profile differs qualitatively from numeric workloads.

## 3. Methods

### 3.1 Demand model

Following the Markov-modulated structure of [8], we model substrate demand as a continuous-time process $d(t)$ modulated by a hidden world-state $s(t) \in \{h, l\}$ (high and low demand regimes) with stationary occupancy probabilities $p_h = p$ and $p_l = 1-p$. Within regime $s$, demand takes the value $d_s$:

$$d(t) = d_{h} \quad \text{if } s(t) = h, \qquad d(t) = d_{l} \quad \text{if } s(t) = l,$$

with $d_{h} > d_{l} \geq 0$. All demand is not directly observable: following [8] and the censoring pathology of [3], demand is observed only when it is completely met, so measured demand $\hat{d}(t) = \min(d(t), C)$ is right-censored by capacity.

### 3.2 Allocation model

Following [2], incoming demand is partitioned into elastic demand (deferrable) and inelastic demand (must be served on arrival). The substrate has capacity $C$ operations per second. The allocator chooses a provisioning level $C$ ex ante; ex post, over a horizon of length $T_{\text{horizon}}$,

$$W(C) = \int_{0}^{T_{\text{horizon}}} \bigl(C - d(t)\bigr)^{+}\, dt \qquad \text{(waste)},$$

$$S(C) = \int_{0}^{T_{\text{horizon}}} \bigl(d(t) - C\bigr)^{+}\, dt \qquad \text{(shortfall)},$$

where $x^{+} = \max(x, 0)$. Waste is capacity bought but unused; shortfall is demand refused, which under censoring is invisible in $\hat{d}$ and must be inferred by a filter in the sense of [8].

### 3.3 Cost floor

Following [12], each operation carries a thermodynamic floor. The Landauer bound gives the minimum energy to erase one bit:

$$E_{\min}(T) = k_{B}\, T \ln 2,$$

with $k_{B} = 1.380649 \times 10^{-23}$ J/K. If error correction requires an overhead factor $r$ physical operations per logical operation, with $r \in [10^{2}, 10^{3}]$ as stated in [12], the per-logical-operation floor is

$$E_{\text{logical}}(r) = r\, E_{\min}(T).$$

### 3.4 Utilization and break-even

Define realized demand over the horizon as $D_{\text{act}} = \int_{0}^{T_{\text{horizon}}} d(t)\, dt$ and realized utilization as

$$\rho = \frac{D_{\text{act}}}{C\, T_{\text{horizon}}}.$$

A substrate is *actually demanded*, in the operational sense of this paper, if $\rho$ exceeds a break-even utilization $\rho^{*}$ that balances the fixed cost of maintaining the substrate against the marginal floor cost of the operations it performs. We compute $\rho$ exactly for the two-state model in Section 4; we state the break-even criterion structurally and flag its calibration as an open problem (Section 6), since no fixed-cost figure for any specific substrate is supplied in the source material.

### 3.5 Demand-conditioned task attributes

Following the separation in [6] between the demanded object and its actual presence, we tag each unit of demand with a task-attribute vector $a$ (precision, latency, reversibility, declarative form). Aggregate capacity $C$ is then attribute-specific: $C = \sum_{a} C_{a}$, and utilization must be evaluated per attribute class. We do not compute per-attribute numbers here—no attribute-resolved demand data is supplied—but the two-state model of Section 4 applies unchanged within each class.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Landauer floor

**Inputs.** $k_{B} = 1.380649 \times 10^{-23}$ J/K (SI defined value); $T = 300$ K (assumption: room temperature; the source [12] states the Landauer bound but not a temperature, so $T = 300$ K is an explicit assumption of this paper); $\ln 2 = 0.693147$.

**Step 1.** $k_{B} T = 1.380649 \times 10^{-23} \times 300 = 414.1947 \times 10^{-23} = 4.141947 \times 10^{-21}$ J.

**Step 2.** $E_{\min} = 4.141947 \times 10^{-21} \times 0.693147$. Compute $4.141947 \times 0.693147$: $4.141947 \times 0.7 = 2.899363$; subtract $4.141947 \times 0.006853 = 0.028382$; result $2.870981$. Therefore

$$E_{\min}(300\ \text{K}) = 2.870981 \times 10^{-21}\ \text{J} \approx 2.871 \times 10^{-21}\ \text{J}.$$

### 4.2 Per-logical-operation floor under error-correction overhead

**Inputs.** $r \in [10^{2}, 10^{3}]$ physical operations per logical operation, stated in [12]; $E_{\min} = 2.870981 \times 10^{-21}$ J from Section 4.1.

**Step 1 (lower end).** $E_{\text{logical}}(10^{2}) = 10^{2} \times 2.870981 \times 10^{-21} = 2.870981 \times 10^{-19}$ J.

**Step 2 (upper end).** $E_{\text{logical}}(10^{3}) = 10^{3} \times 2.870981 \times 10^{-21} = 2.870981 \times 10^{-18}$ J.

**Step 3 (spread).** The ratio of upper to lower floor is $10^{3}/10^{2} = 10$. The uncertainty in the overhead factor alone spans one order of magnitude in the thermodynamic cost of a logical operation, before any implementation inefficiency is counted.

### 4.3 Two-state provisioning: waste, shortfall, utilization

**Inputs (illustrative model parameters, not measurements).** $p = 0.3$ (fraction of time in the high-demand regime), $d_{h} = 1$ (normalized peak demand), $d_{l} = 0.2$. These values are chosen to make the trade-off arithmetic transparent; they are properties of the model, not claims about any real substrate.

**Case A: provision at peak, $C = d_{h} = 1$.**

- Waste: in the low regime, $(C - d_{l})^{+} = 1 - 0.2 = 0.8$; in the high regime, $(C - d_{h})^{+} = 0$. Per unit time, $W = (1 - p)(d_{h} - d_{l}) = 0.7 \times 0.8 = 0.56$.
- Shortfall: $S = 0$ by construction.
- Realized demand per unit time: $D_{\text{act}}/T_{\text{horizon}} = p\, d_{h} + (1-p)\, d_{l} = 0.3 \times 1 + 0.7 \times 0.2 = 0.3 + 0.14 = 0.44$.
- Utilization: $\rho = 0.44 / 1 = 0.44$.

**Case B: provision at mean demand, $C = \bar{d} = 0.44$.**

- Waste: in the high regime, $(C - d_{h})^{+} = 0$; in the low regime, $(C - d_{l})^{+} = 0.44 - 0.2 = 0.24$, active for fraction $1 - p = 0.7$: $W = 0.7 \times 0.24 = 0.168$.
- Shortfall: in the high regime, $(d_{h} - C)^{+} = 1 - 0.44 = 0.56$, active for fraction $p = 0.3$: $S = 0.3 \times 0.56 = 0.168$.
- Utilization: $\rho = 0.44 / 0.44 = 1.0$ in the served portion, but $30\%$ of high-regime demand is refused. Note the exact symmetry $W = S = 0.168$ at mean provisioning for this two-state model: because demand is bimodal, the mean splits the excess evenly between the two regimes.

**Case C: provision at trough, $C = d_{l} = 0.2$.**

- Waste: $W = 0$ (capacity never exceeds demand).
- Shortfall: in the high regime, $(d_{h} - C)^{+} = 0.8$, fraction $p = 0.3$: $S = 0.3 \times 0.8 = 0.24$; in the low regime, $(d_{l} - C)^{+} = 0$.
- Utilization: $\rho = 0.44/0.2 = 2.2 > 1$, i.e., infeasible: sustained demand exceeds capacity by a factor of $2.2$ on average, and the excess $1.2$ per unit time ($= S/T_{\text{horizon}} = 0.24$ over the $0.2$-weighted horizon—equivalently, mean refused demand $= p(d_{h} - d_{l}) = 0.3 \times 0.8 = 0.24$) is lost, and, by the censoring assumption of [8], unmeasured.

**Cross-check.** In every case, served demand per unit time equals $D_{\text{act}}/T_{\text{horizon}} - S$: Case A: $0.44 - 0 = 0.44$; Case B: $0.44 - 0.168 = 0.272$; Case C: $0.44 - 0.24 = 0.2 = C$. Case C's served demand equals capacity exactly, as it must when capacity is the binding constraint at all times. The identities hold, confirming the arithmetic.

### 4.4 Censoring bias of measured demand

Under the observation model $\hat{d}(t) = \min(d(t), C)$, the measured mean is

$$\bar{\hat{d}} = p\, \min(d_{h}, C) + (1-p)\, \min(d_{l}, C).$$

For Case B ($C = 0.44$): $\bar{\hat{d}} = 0.3 \times 0.44 + 0.7 \times 0.2 = 0.132 + 0.14 = 0.272$. The true mean is $0.44$, so the censored measurement understates true demand by a factor $0.44/0.272 = 1.6176\ldots$, i.e., by $61.8\%$:

$$\frac{\bar{d} - \bar{\hat{d}}}{\bar{d}} = \frac{0.44 - 0.272}{0.44} = \frac{0.168}{0.44} = 0.3818\ldots,$$

so measured demand understates true demand by $38.2\%$ (the shortfall fraction $S$-per-unit-time $0.168$ divided by true mean $0.44$). A forecaster training on censored substrate-usage logs—exactly the stock-out censoring pathology named in [3]—would therefore systematically underestimate demand for a capacity-constrained substrate, and would under-provision it in the next planning cycle. This is the quantitative core of the paper's argument: for novel substrates, naive demand measurement is biased low by an amount equal to the shortfall ratio $S / \bar{d}$.

### 4.5 Time-to-saturation projection

**Projection, with stated assumptions.** Assume demand grows at a compound rate $g = 0.5$ per year ($50\%$ annual growth, an assumption for illustration, not a measurement) from an initial realized demand $D_{0} = 0.44$ (the mean of the model of Section 4.3) against fixed capacity $C = 1$. Time to saturation:

$$t_{\text{sat}} = \frac{\ln(C / D_{0})}{\ln(1 + g)} = \frac{\ln(1/0.44)}{\ln(1.5)} = \frac{\ln(2.2727)}{\ln(1.5)} = \frac{0.82098}{0.40546} = 2.025\ \text{years}.$$

Arithmetic: $\ln(2.2727)$: $\ln 2 = 0.693147$, $\ln(2.2727/2) = \ln(1.13636) \approx 0.127833$; sum $= 0.820980$. $\ln 1.5 = 0.405465$. Quotient $= 0.820980 / 0.405465 = 2.0249$. So under these assumptions the substrate saturates in approximately $2.0$ years. This is a projection contingent on the growth assumption; if $g = 0.1$ instead, $t_{\text{sat}} = 0.820980 / \ln(1.1) = 0.820980 / 0.095310 = 8.613$ years. The sensitivity is large: a five-fold change in the growth assumption moves time-to-saturation by a factor of $8.613/2.025 = 4.25$.

### 4.6 Thermodynamic cost of a year of saturated operation

**Projection, with stated assumptions.** Take a substrate performing $R = 10^{18}$ logical operations per year (assumption, chosen as a round figure for scale illustration) at the floor costs of Section 4.2.

- Lower floor: $10^{18} \times 2.870981 \times 10^{-19}\ \text{J} = 2.870981 \times 10^{-1}\ \text{J} \approx 0.287$ J per year.
- Upper floor: $10^{18} \times 2.870981 \times 10^{-18}\ \text{J} = 2.870981\ \text{J} \approx 2.87$ J per year.

The absolute floor energies are tiny; the significance of [12]'s overhead point is that it multiplies whatever the implementation actually dissipates, which for real devices is many orders of magnitude above the Landauer floor. The framework therefore treats $E_{\text{logical}}$ as a *lower bound on the marginal cost curve*, with the gap between floor and practice as the substrate-specific inefficiency that demand-side analysis must price.

## 5. Results

All numbers below are computed in Section 4; projections are labeled as such.

**R1 (Floor cost).** The Landauer floor at the assumed $T = 300$ K is $E_{\min} = 2.871 \times 10^{-21}$ J per bit erasure. With the error-correction overhead $r \in [10^{2}, 10^{3}]$ stated in [12], the per-logical-operation floor lies in $[2.871 \times 10^{-19},\ 2.871 \times 10^{-18}]$ J, a range spanning a factor of $10$.

**R2 (Provisioning trade-off).** In the two-state model with $p = 0.3$, $d_{h} = 1$, $d_{l} = 0.2$: provisioning at peak gives waste $0.56$ and shortfall $0$; provisioning at the mean ($\bar{d} = 0.44$) gives waste $=$ shortfall $= 0.168$ exactly; provisioning at the trough gives waste $0$ and shortfall $0.24$, with average demand exceeding capacity by a factor $2.2$.

**R3 (Utilization).** Realized utilization is $\rho = 0.44$ at peak provisioning, $\rho = 1.0$ (with $30\%$ of high-regime demand refused) at mean provisioning, and infeasible ($\rho = 2.2$) at trough provisioning.

**R4 (Censoring bias).** Under capacity-censored observation, measured mean demand at mean provisioning is $0.272$ against a true mean of $0.44$: an understatement of $38.2\%$, equal to the shortfall ratio $S/\bar{d} = 0.168/0.44$.

**R5 (Projection: saturation).** Under the stated assumptions ($D_{0} = 0.44$, $C = 1$, growth $g = 0.5$/yr), the substrate saturates in $t_{\text{sat}} \approx 2.02$ years; under $g = 0.1$/yr, in $8.61$ years—a factor-$4.25$ sensitivity to the growth assumption.

**R6 (Projection: annual floor energy).** At $R = 10^{18}$ logical operations per year, the thermodynamic floor energy is between $0.287$ J and $2.87$ J per year; this is a lower bound on marginal cost, with implementation inefficiency unpriced.

## 6. Discussion

**Limitations.** The two-state demand model is deliberately minimal. Real substrate demand is not bimodal; it is heavy-tailed, correlated, and attribute-dependent in the sense of [6]. The symmetry $W = S = 0.168$ at mean provisioning is an artifact of bimodality: with more regimes, mean provisioning no longer splits the excess evenly, and the optimal provisioning point must be found numerically. The parameters $p = 0.3$, $d_{h} = 1$, $d_{l} = 0.2$ are illustrative, not measured; every quantitative result in R2–R4 scales with them. The temperature $T = 300$ K is an assumption; the Landauer floor scales linearly in $T$, so at cryogenic operating temperatures typical of quantum platforms the floor is lower by the ratio of temperatures. The growth rate in R5 is an assumption; we present the $g$-sensitivity precisely because no growth figure for any substrate is supplied in the source material.

**Failure modes of the framework.** First, the break-even utilization $\rho^{*}$ is defined structurally but not calibrated: computing it requires a fixed-cost figure per substrate, and no such figure appears in the supplied sources. Until calibrated, the "actually demanded" criterion is a ratio to be measured, not a verdict.