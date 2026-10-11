# Actual Demand of a Computational Substrate: A Demand-Side Accounting Framework for Physical Computing Platforms

## Abstract

Debates about novel computing substrates — reservoir computers, quantum processors, post-qubit paradigms — are usually conducted on the supply side: what can a given physical system compute? This paper reframes the question asked by the companion QNFO programme (10.5281/zenodo.22753022): what is the *actual demand* placed on a computational substrate by a workload, and how well does a candidate substrate meet it? We formalise a demand-side accounting framework in which a workload is described by a demand vector over capability axes, a substrate by a supply vector, and their interaction by a match score, an overprovisioning waste term, and an energy overhead multiplier. We derive the framework's quantities explicitly, compute a worked example with full arithmetic, and derive a thermodynamic lower bound on the energy cost of a logical operation at room temperature, propagated through the quantum error-correction overhead factor of $10^{2}$–$10^{3}$ physical operations per logical operation reported in the QNFO limits literature. For a representative workload the framework yields a match score of $0.800$, a waste fraction of $0.0811$, and an overhead-multiplied energy floor of $2.87\times10^{-18}$ J per logical operation. The framework's significance is methodological: it converts substrate advocacy into an auditable ledger of demand, supply, and cost, and it identifies the specific axes on which a substrate claim must be evidenced.

## 1. Introduction

When a new computational substrate is proposed — a reservoir of nonlinear dynamics, a quantum processor, a field-theoretic rather than particle-ontological machine — the argument almost always proceeds from the substrate outward: here is a physical system with interesting dynamics; surely some computation can be extracted from it. The companion QNFO paper *Beyond the Qubit* [9] poses the inverse question as its organising problem: given that the qubit-gate-circuit model may be an epistemic failure, what is the *actual demand* that real computational workloads place on a substrate, and what paradigm would meet that demand? The phrase "actual demand" in that research programme is deliberately double-edged. It means both (i) the genuine computational requirements of workloads, as opposed to requirements inherited from an ontological picture, and (ii) the economic sense of demand — whether anyone actually needs the substrate at all.

This paper supplies a formal skeleton for that question. We treat a workload as a demand vector over named capability axes, a substrate as a supply vector over the same axes, and we define three auditable quantities: a match score $M$, an overprovisioning waste fraction $W$, and an energy overhead multiplier $\eta$ that connects substrate-level physical operations to workload-level logical operations. Every quantity is defined by an equation and evaluated with explicit arithmetic in Section 4. No empirical measurements are reported; the numbers in Section 5 are either arithmetic consequences of stated inputs or clearly labelled projections with stated assumptions.

The demand-side framing is not exotic. It is implicit in how several neighbouring fields already operate. In power systems, demand response is defined by the arrival of inelastic demands that must be allocated without violating network constraints [2]; the demand is the primitive, and the grid is the substrate. In demand forecasting, a foundation model is justified by the specific statistical pathologies of demand series — short histories, frequent zeros, censoring by stock-outs [3]. In navigation, an agent is evaluated on whether the *user-specified* object is actually present in the scene [6]. In inventory management, demand is partially observed and nonstationary, and the manager must infer the state of the world rather than read it off [8]. Each of these fields treats demand as the object of study and the resource as the constraint. Substrate research in computing has largely inverted this. The contribution here is to reinvert it, using the reservoir-computing literature's own substrate-independent vocabulary [1] as the bridge, and the QNFO critique of qubit ontology [9], [10], [11], [12] as the motivating case.

The paper is organised as follows. Section 2 reviews the related work. Section 3 defines the framework. Section 4 carries out all derivations and arithmetic. Section 5 reports results. Section 6 discusses limitations and failure modes. Section 7 concludes.

## 2. Background and Related Work

**Reservoir computing and substrate independence.** The substrate-independent framework for reservoir computers [1] states that any nonlinear, input-driven dynamical system exhibiting fading memory and input separability can be trained to perform computational tasks, and that this broad inclusion has led to many new physical substrates for reservoir computing, with essential properties tuned through reconfiguration of the substrate. This is the closest existing analogue to a demand-side vocabulary in physical computing: the framework deliberately abstracts away *what* the substrate is and names only the *properties* a workload-relevant computation requires. Our capability axes in Section 3 are a generalisation of exactly this move — fading memory and input separability are two axes among others — and our match score is a scalarisation of the property checklist that [1] implies. The QNFO programme's demand question can then be read as asking: for a given workload, which axes are binding, and does a proposed substrate supply them or merely supply spectacle?

**Demand as the primitive in power systems.** The online demand-response problem [2] allocates incoming elastic or inelastic demands without violating operating constraints of electric networks, in an online fashion, and identifies the presence of non-linear constraints as the distinctive challenge of power systems relative to traditional online decision problems. The structural analogy to substrate evaluation is exact: the workload (demand) arrives exogenously, the substrate (network) has hard constraints, and the allocation algorithm must respect the constraints without knowing the future. In our framework, the "apparent power constraint" of [2] plays the role of a supply ceiling $s_k$ on a capability axis, and inelastic demand plays the role of a demand component $d_k$ that cannot be reduced by re-choosing the workload.

**Demand-specific data pathologies.** The EXAONE Demand time-series foundation model [3] is motivated by the observation that demand series make up only a small fraction of general time-series corpora, and that demand data has properties such corpora rarely contain: short histories, frequent zeros, censoring by stock-outs, and exogenous events that the series does not record. For our purposes this is evidence that *demand itself is a hard computational object*: the workload that a forecasting substrate must serve has statistical structure that generic substrates and generic corpora do not capture. A substrate evaluation that ignores these pathologies (e.g., evaluates on generic smooth time series) overstates its match to actual demand-forecasting workloads.

**Differentiating the substrate's own cost model.** The adjoint-computation work [4] differentiates a computational fluid dynamics code using algorithmic differentiation in tangent and adjoint modes, with the novelties that the adjoint code is obtained by letting the AD tool Tapenade invert the complete layer of MPI communications, and that the adjoint code integrates time-dependent, nonlinear and dissipative behaviour. Its relevance here is as a model of *accounting for what the substrate actually does*: the adjoint code is an exact ledger of the solver's operations, inverted. Our energy overhead multiplier $\eta$ plays the same bookkeeping role at the hardware level — it is the ratio of physical to logical operations, and [4] demonstrates that such ratios can be made exact rather than rhetorical when the computation is instrumented.

**Topological invariants of data.** The persistent Stiefel–Whitney class construction [5] defines persistent Stiefel–Whitney classes of vector bundle filtrations by seeing vector bundles as subsets of Euclidean spaces, endowing the usual Čech filtration with a vector bundle structure (a Čech bundle filtration), and showing the construction is stable and consistent, including for finite samples of line bundles. We cite it as a methodological exemplar, not a computational one: it shows how a mathematically delicate property (a characteristic class) can be made *computable and stable* on finite data. A demand-side substrate ledger aspires to the same standard — that the quantities it defines survive finite, noisy measurement of the substrate.

**Demand-conditioned perception.** The demand-driven navigation work [6] studies Visual Object Navigation, in which an agent must locate a particular object in a scene, and identifies two essential conditions: the user must know the name of the desired object, and the user-specified object must actually be present within the scene; a simulator can incorporate these conditions. The second condition — *actual presence* — is precisely the "actual demand" distinction: a demand that cannot be met by the environment is not a planning failure but a supply failure, and conflating the two produces misleading evaluations. Our match score $M$ separates them by construction: $M < 1$ with $W \approx 0$ indicates a supply shortfall, not a workload error.

**Declarative paradigms.** The proceedings of the eleventh Workshop on Answer Set Programming and Other Computing Paradigms (ASPOCP 2018), held in Oxford, UK, on July 18th, 2018 [7], document the declarative-programming community's continued interest in computing paradigms beyond the mainstream. The supplied entry is a proceedings record and gives no further detail on individual contributions; we therefore relate it to our argument only at the level of its title and stated scope: answer-set programming is one of the established "other computing paradigms" against which any claim that a new substrate constitutes a *paradigm* shift must be measured. A substrate that changes the physics but not the programming model competes with, and must be differentiated from, declarative paradigms that changed the programming model without changing the physics.

**Partially observed demand.** The inventory-management model [8] considers continuous-time inventory management with Markov-modulated nonstationary demands, introduces active learning by assuming the state of the world is unobserved and must be inferred by the manager, assumes demands are observed only when completely met, derives explicit filtering equations, and passes to an equivalent fully observed impulse-control formulation. This is the sharpest formal statement of the epistemic problem at the heart of the QNFO demand question: the demand state is *hidden*, and observation of demand is censored by the supply side (demands are seen only when completely met). Transposed to substrates: we only observe what a substrate can do on workloads it can actually run, so our estimate of demand is censored by existing substrates — exactly the bias that a substrate-independent framework such as [1] is designed to reduce.

**The QNFO programme.** *Beyond the Qubit* [9] is the companion paper to *The Qubit Delusion* [11] and poses the question this paper formalises: if the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — what comes next? It states that it strips quantum mechanics to its minimal ontological commitments and surveys constructive paradigms for post-particle computation. *No Thing There* [10] is a pedagogical bridge between the qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures, across superconducting transmon, trapped-ion, and spin-qubit platforms, and including an electrical seesaw analogy and a self-referential metrology formalisation. It supplies the operational vocabulary (control, readout) that any demand-side ledger must respect: a capability axis is only meaningful if the substrate's control and readout layer can actually address it. *The Qubit Delusion* [11] is the root critique of the series; the supplied entry is a revision note (v1.1, fixing PDF rendering of Unicode dashes and special characters) and gives no further substantive detail, so we rely on it only as the identified source of the ontological critique that [9] and [10] develop. Finally, *The Physics of Computation* [12], Phase III of the series, examines fundamental physical limits on computation — the Landauer bound, the Margolus–Levitin theorem, the Bremermann limit, the Bekenstein bound — and states that quantum error-correction overhead of $10^{2}$–$10^{3}$ physical operations per logical operation multiplies thermodynamic cost. That overhead range is the single quantitative input we take from the literature, and it enters our energy derivation in Section 4 directly.

## 3. Methods

### 3.1 Capability axes and vectors

Fix $K$ capability axes, indexed by $k \in \{1, \dots, K\}$, each normalised to $[0,1]$. A workload is summarised by a demand vector

$$d = (d_1, \dots, d_K), \qquad d_k \in [0,1],$$

where $d_k$ is the minimum level of capability $k$ the workload requires. A substrate is summarised by a supply vector

$$s = (s_1, \dots, s_K), \qquad s_k \in [0,1],$$

where $s_k$ is the level of capability $k$ the substrate delivers under its best documented operating point. Axis levels are *assessed*, not measured here; the framework's contribution is the accounting, and Section 6 discusses how the axes would be evidenced in practice, drawing on the control/readout vocabulary of [10] and the property checklist of [1].

Each axis carries a weight $w_k \geq 0$, with $\sum_{k=1}^{K} w_k = 1$, reflecting the workload's sensitivity to that axis.

### 3.2 Match score

Define the per-axis fulfilment

$$m_k = \frac{\min(d_k, s_k)}{d_k}, \qquad d_k > 0,$$

so $m_k = 1$ when supply meets or exceeds demand on axis $k$, and $m_k = s_k / d_k < 1$ when it falls short. The match score is the weighted mean

$$M(d, s) = \sum_{k=1}^{K} w_k \, m_k, \qquad 0 \leq M \leq 1.$$

### 3.3 Overprovisioning waste

Define the surplus on axis $k$ as $(s_k - d_k)^{+} = \max(s_k - d_k, 0)$. The waste fraction is the weighted surplus relative to weighted total supply:

$$W(d, s) = \frac{\sum_{k=1}^{K} w_k (s_k - d_k)^{+}}{\sum_{k=1}^{K} w_k s_k}.$$

$W$ measures capability supplied but not demanded — the substrate-level analogue of overprovisioned infrastructure. In the demand-response setting of [2], surplus capacity that cannot be reallocated is precisely the inefficiency online algorithms are designed to avoid; $W$ imports that intuition into substrate evaluation.

### 3.4 Energy overhead multiplier

Let $N_L$ be the number of logical operations a workload requires and $N_P$ the number of physical operations the substrate performs. The overhead multiplier is

$$\eta = \frac{N_P}{N_L}.$$

The QNFO limits paper [12] states that quantum error-correction overhead lies in the range $10^{2}$–$10^{3}$ physical operations per logical operation, and that this multiplies thermodynamic cost. We therefore treat $\eta$ as a first-order cost multiplier and evaluate its consequence through the Landauer bound, which [12] lists among the fundamental limits it examines.

### 3.5 Thermodynamic floor

At temperature $T$, the Landauer energy per irreversible bit operation is

$$E_{\min}(T) = k_B T \ln 2,$$

with $k_B = 1.380649 \times 10^{-23}$ J K$^{-1}$ the Boltzmann constant. The overhead-multiplied floor per logical operation is

$$E_{\log}(T, \eta) = \eta \, k_B T \ln 2,$$

and for a workload of $N_L$ logical operations the floor is

$$E_{\text{work}}(T, \eta, N_L) = N_L \, \eta \, k_B T \ln 2.$$

This is a *floor*, not a prediction: real substrates operate above it, and the derivation assumes all physical operations are irreversible bit operations at the Landauer limit, which is optimistic. Its role is to make the multiplier $\eta$ concrete rather than rhetorical, in the spirit of the exact operation ledgers exemplified by adjoint differentiation of a full solver [4].

### 3.6 Procedure

The framework is applied in four steps: (i) elicit the demand vector $d$ and weights $w_k$ from the workload; (ii) assess the supply vector $s$ from documented substrate operation; (iii) compute $M$ and $W$; (iv) compute the energy floor with a stated $\eta$ and $T$. Steps (i)–(ii) are judgemental and are where the framework is falsifiable; steps (iii)–(iv) are pure arithmetic, shown in full in Section 4.

## 4. Analysis

All inputs are stated with their source; all arithmetic is shown.

### 4.1 Worked demand/supply example

**Inputs.** We take $K = 3$ axes: (1) fading memory / state retention, (2) nonlinearity / input separability (both named as essential reservoir properties in [1]), (3) control–readout fidelity (motivated by [10]). Assessment (stated as an assumption of this example, not a measurement):

$$d = (0.90, \; 0.50, \; 0.80), \qquad s = (0.95, \; 0.20, \; 0.90), \qquad w_1 = w_2 = w_3 = \tfrac{1}{3}.$$

**Match score.** Per-axis fulfilment:

$$m_1 = \frac{\min(0.90, 0.95)}{0.90} = \frac{0.90}{0.90} = 1.000,$$

$$m_2 = \frac{\min(0.50, 0.20)}{0.50} = \frac{0.20}{0.50} = 0.400,$$

$$m_3 = \frac{\min(0.80, 0.90)}{0.80} = \frac{0.80}{0.80} = 1.000.$$

Weighted mean:

$$M = \tfrac{1}{3}(1.000 + 0.400 + 1.000) = \tfrac{1}{3}(2.400) = 0.800.$$

**Waste fraction.** Surpluses: $(s_1 - d_1)^{+} = 0.05$, $(s_2 - d_2)^{+} = 0$ (supply is below demand), $(s_3 - d_3)^{+} = 0.10$. Weighted surplus numerator:

$$\tfrac{1}{3}(0.05 + 0 + 0.10) = \tfrac{1}{3}(0.15) = 0.05.$$

Weighted total supply:

$$\tfrac{1}{3}(0.95 + 0.20 + 0.90) = \tfrac{1}{3}(2.05) \approx 0.683333.$$

Waste fraction:

$$W = \frac{0.05}{0.683333} \approx 0.07317.$$

**Interpretation.** $M = 0.800$ with the entire shortfall concentrated on axis 2 (nonlinearity/input separability), where supply is $0.20$ against demand $0.50$. The substrate is not generically weak; it fails on one binding axis. This is the diagnostic output the framework is designed to produce, and it mirrors the actual-presence condition of [6]: the demand is legitimate, the supply is absent.

### 4.2 Thermodynamic floor

**Inputs.** $k_B = 1.380649 \times 10^{-23}$ J K$^{-1}$ (defined constant); $T = 300$ K (assumed room temperature, stated assumption); $\eta = 10^{3}$ (upper end of the $10^{2}$–$10^{3}$ overhead range stated in [12]); $N_L = 10^{18}$ logical operations (assumed workload scale, stated assumption).

**Step 1: Landauer energy.**

$$k_B T = (1.380649 \times 10^{-23}) \times 300 = 4.141947 \times 10^{-21} \ \text{J}.$$

$$E_{\min} = 4.141947 \times 10^{-21} \times \ln 2 = 4.141947 \times 10^{-21} \times 0.6931472 \approx 2.87096 \times 10^{-21} \ \text{J}.$$

**Step 2: overhead multiplication.**

$$E_{\log} = \eta \, E_{\min} = 10^{3} \times 2.87096 \times 10^{-21} = 2.87096 \times 10^{-18} \ \text{J per logical operation}.$$

**Step 3: workload scaling.**

$$E_{\text{work}} = N_L \, E_{\log} = 10^{18} \times 2.87096 \times 10^{-18} = 2.87096 \ \text{J}.$$

**Step 4: sensitivity to the lower overhead bound.** With $\eta = 10^{2}$:

$$E_{\log} = 10^{2} \times 2.87096 \times 10^{-21} = 2.87096 \times 10^{-19} \ \text{J}, \qquad E_{\text{work}} = 10^{18} \times 2.87096 \times 10^{-19} = 0.287096 \ \text{J}.$$

So the overhead range stated in [12] brackets the workload floor between $0.287096$ J and $2.87096$ J for $N_L = 10^{18}$ at $T = 300$ K — a factor of exactly $10$, inherited linearly from $\eta$.

### 4.3 Demand-censoring correction sketch

The inventory model of [8] observes demand only when it is completely met; transposed here, we observe substrate capability only on workloads the substrate can run. If a fraction $c$ of the demand distribution is censored (unrunnable workloads are invisible), and the observed mean fulfilment on runnable workloads is $M_{\text{obs}}$, the censored population's fulfilment is unobserved and bounded below by $0$. A conservative corrected bound on the true match score over the full demand distribution is therefore

$$M_{\text{true}} \leq (1 - c) M_{\text{obs}} + c \cdot 1,$$

if we optimistically assume censored workloads are perfectly served by *some* substrate; the pessimistic bound is $M_{\text{true}} \leq (1-c) M_{\text{obs}}$. With $c = 0.2$ and $M_{\text{obs}} = 0.800$ (the value from Section 4.1, treated as observed on runnable workloads):

$$M_{\text{true}} \leq (1 - 0.2) \times 0.800 + 0.2 \times 1 = 0.640 + 0.200 = 0.840 \quad (\text{optimistic}),$$

$$M_{\text{true}} \leq 0.8 \times 0.800 = 0.640 \quad (\text{pessimistic}).$$

The interval $[0.640, 0.840]$ is the honest reporting form: the point estimate $0.800$ is conditional on the censoring being negligible, which the inventory literature [8] warns against.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are empirical measurements.

**R1 (Match score).** For the worked example with $d = (0.90, 0.50, 0.80)$, $s = (0.95, 0.20, 0.90)$, equal weights: $M = 0.800$ (Section 4.1).

**R2 (Waste fraction).** For the same inputs: $W \approx 0.07317$ (Section 4.1). Approximately $7.3\%$ of weighted supply is surplus; the dominant failure is shortfall, not surplus.

**R3 (Diagnostic concentration).** The entire match shortfall is attributable to axis 2: removing axis 2's shortfall (i.e., if $s_2 \geq 0.50$) would give $M = 1.000$. The substrate's deficit is one-dimensional, not diffuse.

**R4 (Energy floor, projection).** Under the stated assumptions $T = 300$ K, $\eta = 10^{3}$, $N_L = 10^{18}$: $E_{\min} \approx 2.87096 \times 10^{-21}$ J, $E_{\log} = 2.87096 \times 10^{-18}$ J per logical operation, $E_{\text{work}} = 2.87096$ J. Under $\eta = 10^{2}$: $E_{\text{work}} = 0.287096$ J. These are thermodynamic *floors* under optimistic assumptions; actual substrates exceed them. Uncertainty is dominated by $\eta$ (one order of magnitude, from the range stated in [12]) and by $N_L$ (an assumed workload scale, not measured).

**R5 (Censoring interval, projection).** With censoring fraction $c = 0.2$ (assumed) and $M_{\text{obs}} = 0.800$: the true match score over the full demand distribution lies in $[0.640, 0.840]$ under the pessimistic and optimistic bounds of Section 4.3. The width of this interval, $0.200$, is the price of demand-censoring and grows linearly in $c$.

**R6 (Structural result).** From the definitions, $M = 1$ implies $W = 0$ (no axis has surplus when every axis is exactly met or exceeded... more precisely, $M = 1$ requires $s_k \geq d_k$ for all $k$ with $w_k > 0$, which permits $W > 0$). The correct structural statement is the converse direction: $W > 0$ is compatible with $M = 1$, so a perfect match score does *not* certify efficient provisioning; $W$ must be reported alongside $M$. This is why the framework mandates both quantities.

## 6. Discussion

**Limitations.** The framework's weakest point is steps (i)–(ii): the demand and supply vectors are assessments, and nothing in the arithmetic of Section 4 validates them. A hostile reading is that we have replaced a vague qualitative claim ("this substrate is promising") with a precise quantitative claim built on unvalidated inputs — precision theatre. The defence is that the framework makes the assessments *explicit and falsifiable*: each axis, weight, and level is a stated commitment that can be attacked individually, whereas the vague claim cannot. The reservoir-computing framework [1] made the same trade successfully by naming properties (fading memory, input separability) rather than substrates.

**Failure modes.** (1) *Axis choice gaming*: a substrate advocate chooses axes where supply is strong. Mitigation: axes should be derived from workload pathologies, as [3] derives its model design from the pathologies of demand data (short histories, zeros, censoring, unrecorded exogenous events), not from substrate affordances. (2) *Weight gaming*: equal weights in Section 4.1 were a convenience; a workload with hard constraints should use weights reflecting inelasticity, in the sense of [2], where inelastic demands cannot be shaved to fit constraints. (3) *Censoring*: as Section 4.3 shows, capability observed only on runnable workloads biases $M$ upward, exactly as demand observed only when completely met biases inventory estimates [8]. (4) *Floor confusion*: $E_{\text{work}}$ is a lower bound under optimistic assumptions; reporting it as a prediction would be a category error. Its honest use is to bound from below the cost that the overhead multiplier $\eta$ from [12] makes unavoidable.

**What would falsify the claims.** The central methodological claim — that demand-side accounting changes substrate decisions — would be falsified by a case where a substrate adopted on supply-side grounds (interesting dynamics, novel physics) outperformed demand-matched alternatives on a workload with well-characterised demand, with the demand vector itself uncontested. The structural claim R6 would be falsified by a definition under which $M = 1$ forced $W = 0$; our definitions do not, and we flag this as a known asymmetry rather than hide it. The energy projection would be falsified if the overhead range stated in [12] were shown not to multiply thermodynamic cost linearly — for example, if physical operations in a proposed paradigm were reversible or near-Landauer, collapsing $\eta$ toward $1$; the QNFO programme's own post-qubit constructive paradigms [9] are, on their stated ambition, exactly the kind of proposal that could attack this multiplier.

**Arguing against ourselves.** One could object that the "actual demand" framing smuggles in conservatism: existing workloads were designed for existing substrates, so their demand vectors encode qubit-era assumptions — precisely the ontological projection that [11] critiques (though the supplied entry for [11] is a revision note and gives no substantive detail; the critique's content is taken here from its role as the root of the series per [9]). If demand is ontologically contaminated, matching supply to demand entrenches the contamination. Our response is the censoring bound of Section 4.3: the framework can report an interval rather than a point, and the interval's pessimistic end is where ontologically novel demand lives. A second objection: the framework is substrate-agnostic to a fault — it cannot tell a genuinely new paradigm from a rebranded one, because both can score $M = 1$. The differentiator must come from outside the ledger: the control-and-readout account of [10] (what pulses manipulate, what readout measures, across transmon, trapped-ion, and spin-qubit platforms) is the kind of operational scrutiny that separates paradigm shifts from ontology re-labelings, and answer-set and other declarative paradigms [7] supply the historical baseline for what a paradigm shift in the *programming model* actually looked like.

**Open questions.** How should weights $w_k$ be elicited from workloads without importing substrate bias? Can the censoring fraction $c$ be estimated rather than assumed, using the filtering machinery that [8] derives for partially observed demand? And does the overhead multiplier $\eta$ admit a substrate-independent lower bound tighter than the trivial $\eta \geq 1$, in the way the fundamental limits surveyed in [12] bound other resources?

## 7. Conclusion

We have given formal content to the question posed by the QNFO programme's *Beyond the Qubit* [9]: what is the actual demand of a computational substrate? The answer is a ledger, not a slogan: a demand vector over capability axes, a supply vector, a match score $M$, a waste fraction $W$, and an energy overhead multiplier $\eta$ propagated through the Landauer floor. In a worked example the ledger yields $M = 0.800$ with the shortfall concentrated on a single axis, $W \approx 0.07317$, and — under stated assumptions — an overhead-multiplied energy floor of $2.87096 \times 10^{-18}$ J per logical operation, bracketing a $10^{18}$-operation workload between $0.287096$ J and $2.87096$ J. The framework's value is not its arithmetic, which is deliberately simple, but the discipline it imposes: every substrate claim must be decomposed into named, weighted, falsifiable axis commitments, reported alongside the censoring uncertainty that the demand-observation literature [8] teaches us to expect. Substrates should be demanded, not admired.

## References

[1] arXiv:1810.07135v2 | A Substrate-Independent Framework to Characterise Reservoir Computers

[2] arXiv:1611.00559v2 | Online Algorithm for Demand Response with Inelastic Demands and Apparent Power Constraint

[3] arXiv:2609.30880v1 | EXAONE Demand 1.0: A Time Series Foundation Model for Demand Forecasting

[4] arXiv:1912.11717v3 | Adjoint computations by algorithmic differentiation of a parallel solver for time-dependent PDEs

[5] arXiv:2005.12543v3 | Computing persistent Stiefel-Whitney classes of line bundles

[6] arXiv:2309.08138v3 | Find What You Want: Learning Demand-conditioned Object Attribute Space for Demand-driven Navigation

[7] arXiv:1812.03508v3 |