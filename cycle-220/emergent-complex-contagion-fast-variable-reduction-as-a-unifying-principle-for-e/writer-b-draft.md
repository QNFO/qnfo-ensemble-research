# Fast-Variable Reduction and Emergent Complex Contagion: A Unifying Reduction for Mechanism-Rich Epidemic Models

## Abstract

Models of epidemics and social contagion acquire realism by adding mechanism: network correlations, higher-order interactions, adaptive behavior, co-circulating strains, or memory of past exposures. Each mechanism enlarges the state space, and the resulting high-dimensional systems are typically analysed only by simulation, which is slow and offers no closed-form thresholds. We show that a broad class of mechanism-rich contagion models shares a hidden two-timescale structure: the mechanism-specific degrees of freedom are fast variables that equilibrate far quicker than the epidemic itself. Adiabatic elimination of these fast variables yields an emergent complex contagion, in which the macroscopic force of infection becomes a nonlinear, threshold-like function of prevalence even when every microscopic event is memoryless. We formalise the reduction, prove the adiabatic error bound $\Delta_i \le 1/\kappa_i$ in terms of the timescale separation $\kappa_i$, and work a fully explicit example of memory-induced exposure accumulation on a configuration network, deriving the reduced law $\dot{\rho} = 44\,\rho^3$ (in units of $\text{day}^{-1}$), the emergent threshold prevalence $\rho_c \approx 0.0674$, the adiabatic error $\epsilon(\rho) = 44\rho^2$ equal to $1.76\times10^{-2}$ at $\rho = 0.02$, and a seeding time of $111.1$ days from a $1\%$ seed. The reduction predicts algebraic rather than exponential early growth, explains why emergent complex contagions require seeding, and implies that threshold-like macrodynamics do not certify microlevel threshold rules.

## 1. Introduction

Public-health modelling groups, platform-integrity teams, and financial-risk analysts all face the same practical bottleneck: the contagion models they build to be realistic are the models they can no longer solve. A susceptible–infedted–susceptible model on a network with pairwise correlations, triangle closures, adaptive rewiring, or co-circulating strains carries one or more auxiliary variables per edge or per node, and closed-form quantities such as epidemic thresholds, final sizes, and intervention sensitivities disappear into simulation [1]. Simulation-based analysis is expensive, hard to invert for policy questions, and sensitive to unobserved parameters; what is missing is a systematic way to recover analytic handles from high-dimensional models without discarding the mechanisms that made them realistic.

The cost of this gap is concrete. Threshold estimates that come from full simulation must be recomputed for every parameter change, so scenario analysis during an outbreak or a misinformation surge is delayed by the compute budget rather than limited by data. A reliable reduction that maps a high-dimensional model onto a one-dimensional effective equation with an explicit error bound would change the workflow: thresholds and early-growth exponents would become algebraic functions of a handful of parameters, model comparison would reduce to comparing one-dimensional force-of-infection curves, and the question of which microscopic mechanism produced an observed spreading pattern could be asked separately from the question of what macrodynamics follow.

This paper advances a single organising claim: in many mechanism-rich contagion models, the added degrees of freedom are dynamically *fast*. They relax to quasi-equilibrium on a timescale $\tau_{\text{fast}}$ that is short compared with the epidemic timescale $\tau_{\text{epi}}$ over which prevalence changes appreciably. When this two-timescale structure holds, the fast variables can be eliminated by adiabatic (quasi-static) approximation, and the slow epidemic dynamics inherits an effective force of infection that is a nonlinear function of the slow variables. We call this *emergent complex contagion*: the macroscopic spreading law exhibits the signature of complex contagion — a need for repeated or collective exposure before transmission — even though no microscopic rule encodes a response threshold. The reduction principle itself is articulated for canonical network epidemic models in [1], [2], which show that the correlations making network models hard to study are fast and that eliminating them collapses diverse mechanisms onto common polynomial skeletons near threshold; here we extend the same logic to mechanism-added models with memory and reinforcement, work the reduction end-to-end with every number derived, and draw out its consequences for model comparison and inference.

The claim matters for three reasons. First, it offers a unified reading of otherwise disparate models: memory-induced reinforcement, behavioral feedback, and payoff-biased imitation can all be viewed as fast variables whose quasi-equilibrium shapes the force of infection. Second, it gives a diagnostic: if a high-dimensional contagion model can be reduced, its macroscopic behavior should show the algebraic early growth and threshold-like dependence derived below, distinguishing it from simple contagion. Third, it connects to the empirical problem of telling simple from complex contagion in data: emergent complex contagion provides one mechanism by which complex-contagion phenomenology can arise without explicit thresholds, so macro-level observations underdetermine micro-level rules.

Our contributions are:

- A general two-timescale formulation of mechanism-augmented epidemic models and the adiabatic reduction procedure, with the explicit error bound $\Delta_i \le 1/\kappa_i$ derived in Section 3.2.
- A fully worked analytic example — memory-induced exposure accumulation on a configuration network — deriving the reduced growth coefficient $c_2 = 44\ \text{day}^{-1}$, the threshold prevalence $\rho_c \approx 0.0674$, the adiabatic error $\epsilon(\rho) = 44\rho^2$, and the seeding time $t \approx 111.1$ days, with every arithmetic step shown in Section 4.
- A demonstration that the same microscopic rules with linear hazard give $R_0 = 2200$ while the quadratic-hazard system is subcritical below $\rho_c$, establishing algebraic-versus-exponential early growth as the operational signature of emergent complex contagion (Section 4.3).
- A reading of the reduction's practical consequences for model comparison, inference, and the design of the smallest falsifying numerical test (Sections 6 and 7).

## 2. Background and Related Work

**The reduction principle for canonical network epidemics.** Reference [1] frames the modern landscape of epidemic models as a departure from the classical mass-action assumption: models replace identical interactions with detailed transmission mechanisms and explicit contact structure, and the classical pairwise susceptible–infected–susceptible (SIS) model on networks captures correlations between adjacent susceptible–infected pairs, with later generalisations to triangle correlations and degree heterogeneity that shift epidemic thresholds. The central move of [1] is to observe that the global prevalence $i$ is the slow, observable quantity while the correlations that make network models hard to study are fast; collecting the fast quantities into a vector $\mathbf{p}$, every model considered takes the generic form $\dot{i} = i[\beta(\mathbf{p},i) - \gamma(\mathbf{p},i)]$, $\dot{\mathbf{p}} = \mathbf{F}(i,\mathbf{p})$, and $\mathbf{p}$ equilibrates much faster than the epidemic itself. Applying this recipe to five canonical models — pairwise SIS with pair correlations, simplicial contagion with three-body interactions, adaptive networks with co-evolving topology, strain interaction between co-circulating pathogens, and the pairwise SIR model with a second slow variable — [1] obtains analytical bifurcation insights that were not uncovered by traditional techniques in the models' original presentations. Its conclusion states the comparison consequence that motivates our extension: near threshold the reduction collapses many models and mechanisms onto similar polynomial skeletons, so mechanisms sharing a characteristic form can be macroscopically indistinguishable. Reference [2] is the same work in its v1 form and states the same generic two-compartment structure and the same five-model reduction programme; we cite it where the v1 phrasing is the relevant record. Our paper takes this reduction principle as established for correlation- and interaction-driven mechanisms and asks the complementary question: what happens when the added mechanism is an explicit *memory or behavior* variable rather than a network correlation, and what does the reduced force of infection look like when the fast variable is an exposure accumulator?

**Complex contagion and threshold models.** Reference [3] studies complex contagions, in which individuals may require multiple transmissions before changing state, as models of behaviors adopted only after perceiving a consensus among others. Its derivation follows the edge-based compartmental modelling approach — a shift of focus from the proportion of the population in each status to the probability that a random node has each status, equivalent to the cavity method — applied to the Watts Threshold Model on Configuration Model and triangle-based networks. Among its results, [3] finds that in Configuration Model networks activation of an arbitrarily small initial proportion leads to activation of a large fraction of the population if and only if the nodes requiring only a single transmission ($r=1$) form a giant component. This result is the explicit-threshold benchmark against which our emergent threshold should be read: in [3] the threshold is stipulated in the microscopic rule, whereas in our worked example the threshold prevalence $\rho_c$ emerges from a memoryless accumulator plus timescale separation. The contrast sharpens the inference question: the two routes to a macroscopic threshold are mechanistically different, and Section 6 argues that spreading data alone may not distinguish them.

**Behavioral contagion coupled to epidemics.** Reference [6] models the interplay of a classical pairwise SIR epidemic spread with a vaccination drive driven by a social complex contagion process based on the Watts–Granovetter threshold model, grounded in surveys on vaccine hesitancy that showed complex contagion features in attitudes toward vaccine uptake. Its simulations track the activation cascade size $\Delta n_A(\infty)$, the vaccination coverage $v(\infty)$, and the disease prevalence $r(\infty)$ across the control parameters of initial activated fraction $n_A(0)$ and activation threshold $\theta$, with appendices covering homogeneous thresholds and survey-derived heterogeneous thresholds. This model is a natural two-timescale candidate for our reduction — the behavioral activation state is plausibly the fast variable relative to the epidemic — but its threshold structure is stipulated rather than emergent; Section 6 discusses what a reduction of that class would and would not explain, and we do not claim a numerical reduction of it here.

**Modular structure.** Reference [7] applies a message-passing framework to study how the modular structure of the social network affects complex contagion, focusing on *optimal modularity* — the prediction that global cascades occur when the network exhibits just the right amount of modularity — and generalises the original findings to many communities with heterogeneous sizes and non-uniform initial activation. Unlike simple contagion, where modules simply slow spreading, complex contagion may be either enhanced or hampered by modular structure. In our framework, modularity enters as a modifier of the degree moments $\langle k^{\ell}\rangle$ that control the effective force of infection; the community-level message-passing equations of [7] indicate how those moments would become community-indexed, though we do not compute modular corrections in this paper.

**Memory as a unifying mechanism.** Reference [8] develops *generalized contagion*, motivated by the observation that spreading and contagion of all kinds involve some form of system memory, with the aim of unifying models of biological and social contagion in a single discrete-time framework. It covers independent-interaction models of biological contagion in the SIR/SIRS lineage and interdependent-interaction models of social contagion in the Granovetter threshold lineage, and its concluding remarks identify memory as the binding agent that lets a single mechanism produce both disease-like and social-like spreading behavior, including a Vanishing Critical Mass class in which dramatic behavioral changes arise in the infinitesimal-seed limit. Our reduction is complementary and more mechanistic in one specific respect: rather than postulating memory in the update rule, we derive the memory variable's quasi-equilibrium from a fast accumulator and show the resulting nonlinear force of infection explicitly, with an error bound. The Vanishing Critical Mass phenomenology of [8] corresponds in our language to the algebraic early growth $\dot{\rho} \propto \rho^{\ell+1}$ with $\ell > 1$, which we derive in Section 3.3.

**Network sparsification as a computational counterpart.** Reference [9] addresses the computational cost that motivates analytic reduction in the first place: simulating stochastic epidemic models on dense networks derived from high-resolution mobility data is expensive, worsened by the need for many independent runs to characterise outcome distributions and test interventions. Its approach is sparsification — choosing a subset of important links so that a sparser network faithfully reproduces the original behavior — via the novel concept of an infection spanning tree and a notion of epidemic edge importance contrasted against effective resistance; the Spielman–Srivastava sampling procedure allowed removal of up to $75\%$ of edges in certain networks while approximately preserving average epidemic dynamics, though both sampling procedures failed on one dense transport network (AirNet). Sparsification reduces dimension in the *network*; our reduction reduces dimension in the *dynamics*. The two are composable — a sparsified network supplies modified moments to a reduced equation — and both exist because the same underlying difficulty, high-dimensional mechanism-rich models, blocks analysis.

**The present work in context.** Reference [10] is the predecessor preprint of this paper, which proposed emergent complex contagion via fast-variable elimination, derived the error bound $\Delta_i \le 1/\kappa_i$, and worked the same memory-accumulator example to $c_2 = 44\ \text{day}^{-1}$ and $\rho_c \approx 0.0674$. The present paper is a revision and consolidation of that work: we tighten the derivation chain, state the validity domain of the reduction quantitatively through the adiabatic error $\epsilon(\rho) = 44\rho^2$, and add the practical-implications analysis of Section 7, which the predecessor lacked.

## 3. Methods

### 3.1 General two-timescale form

Let $\rho(t) = I(t)/N$ denote prevalence (the slow variable) and let $\mathbf{m}(t)$ collect mechanism-specific fast variables: memory levels, behavioral states, imitation pressures, correlation moments, or trigger intensities. We consider systems of the form

$$
\dot{\rho} = F\big(\rho, \mathbf{m}\big), \qquad
\dot{m}_i = \frac{1}{\tau_{\text{fast}}}\, G_i(\rho, \mathbf{m}),
$$

where $\tau_{\text{fast}}$ is the fast relaxation time and $F$, $G_i$ are smooth. This is the same generic structure as the $\dot{i}$–$\dot{\mathbf{p}}$ pair of [1], with the interpretation of $\mathbf{m}$ widened from network correlation moments to any mechanism-added variable. The fast subsystem $G_i = 0$ defines a quasi-equilibrium manifold $\mathbf{m} = \mathbf{m}^*(\rho)$. Substitution gives the reduced one-dimensional system

$$
\dot{\rho} = F\big(\rho, \mathbf{m}^*(\rho)\big) \equiv f(\rho).
$$

The dimension of $\mathbf{m}$ is immaterial to the principle, as [1] notes for its own models: what matters is that every component of $\mathbf{m}$ equilibrates on $\tau_{\text{fast}} \ll \tau_{\text{epi}}$.

### 3.2 Adiabatic error bound

Let $\gamma_i$ be the linear relaxation rate of $m_i$ near its quasi-steady state and let $\kappa_i = \gamma_i/\mu$ be the separation from the epidemic recovery rate $\mu$. To first order in $1/\kappa_i$, the slaved solution is

$$
m_i = m_i^*(\rho) - \dot{\rho}\,\frac{\partial m_i^*/\partial \rho}{\gamma_i} + \mathcal{O}\!\left(\kappa_i^{-2}\right).
$$

Since prevalence changes by at most $\mathcal{O}(1)$ over the time $1/\mu$, the lag term is at most of order $\mu/\gamma_i$ relative to $m_i^*$, giving the relative adiabatic error bound

$$
\Delta_i \;\le\; \frac{\mu}{\gamma_i} \;=\; \frac{1}{\kappa_i}.
$$

Thus a one-order-of-magnitude separation ($\kappa_i = 10$) guarantees errors of at most $\mathcal{O}(10^{-1})$ in the fast variables, and the error decreases linearly in $\kappa_i$. Equivalently, the reduction is valid to leading order when

$$
\epsilon(\rho) \equiv \tau_{\text{fast}}\,|f'(\rho)| \ll 1,
$$

that is, when prevalence changes little over one fast relaxation time. Section 4.4 quantifies $\epsilon(\rho)$ for the worked example.

### 3.3 Worked model: memory-induced emergent complex contagion

Individuals sit on a configuration-model network with degree distribution $p_k$; infected individuals recover at rate $\gamma$ (units $\text{day}^{-1}$). Each susceptible individual of degree $k$ carries a scalar memory (exposure) variable $m$ obeying

$$
\dot{m} = \beta\, k\, \rho - \gamma_m\, m,
$$

where $\beta$ is the per-edge exposure rate from a unit-infected population and $\gamma_m$ is the memory decay rate. Infection occurs at hazard $\alpha\, m^{\ell}$ with reinforcement exponent $\ell \ge 1$; $\ell = 1$ recovers simple contagion and $\ell = 2$ is the minimal emergent-complex case. The microscopic rules are memoryless in the Markov sense: $m$ is a mechanistic accumulator, not a response threshold, yet the macroscopic hazard $\alpha m^{\ell}$ is threshold-like for $\ell > 1$.

Because $\gamma_m^{-1}$ is short compared with the epidemic timescale (verified a posteriori in Section 4.4), we set $\dot{m} \approx 0$:

$$
m^*(\rho, k) = \frac{\beta\, k\, \rho}{\gamma_m}.
$$

The reduced prevalence equation, with susceptible fraction $\approx 1$ in the early phase, is

$$
\dot{\rho} = \sum_k p_k\, \alpha\, \big[m^*(\rho,k)\big]^{\ell}\,\rho
= \frac{\alpha\, \beta^{\ell}\, \langle k^{\ell}\rangle}{\gamma_m^{\ell}}\; \rho^{\ell+1}
\equiv c_{\ell}\, \rho^{\ell+1}.
$$

The instantaneous (per-capita) reproduction number is

$$
R_{\text{eff}}(\rho) = \frac{c_{\ell}\, \rho^{\ell}}{\gamma},
$$

and the emergent threshold prevalence solves $R_{\text{eff}}(\rho_c) = 1$:

$$
\rho_c = \left(\frac{\gamma\, \gamma_m^{\ell}}{\alpha\, \beta^{\ell}\, \langle k^{\ell}\rangle}\right)^{1/\ell}.
$$

For $\ell > 1$ the early growth is algebraic, not exponential: the system has no autonomous takeoff from an infinitesimal seed, the hallmark of complex contagion. This is the emergent analogue of the $r > 1$ regime in the explicit-threshold model of [3], produced here without any stipulated threshold.

### 3.4 Continuous-state extension

For continuous-state contagions, the same reduction applies with $m$ a continuous distress or exposure level and $\ell$ effectively set by the local scaling of the hazard near equilibrium; the threshold $\rho_c$ becomes a continuous instability boundary rather than a binary cascade condition. We state this extension as a structural observation only; no continuous-state model is reduced numerically in this paper.

## 4. Analysis

Every input number below is stated with its origin: all parameter values are *reference choices made in this paper* for the worked model of Section 3.3; all derived numbers follow from the formulas of Section 3.3 by explicit arithmetic. None are empirical measurements.

### 4.1 Network moments

We take a Poisson (configuration) degree distribution with mean $\langle k \rangle = 10$. For a Poisson distribution the second moment is $\langle k^2\rangle = \langle k\rangle^2 + \langle k\rangle$:

$$
\langle k^2\rangle = 10^2 + 10 = 100 + 10 = 110.
$$

Since $\ell = 2$ in the emergent case, the required moment is $\langle k^{\ell}\rangle = \langle k^2\rangle = 110$.

### 4.2 Reduced growth coefficient

Reference parameters: $\beta = 0.1\ \text{day}^{-1}$, $\gamma_m = 1.0\ \text{day}^{-1}$, $\alpha = 40\ \text{day}^{-1}$, $\gamma = 0.2\ \text{day}^{-1}$, $\ell = 2$. Then

$$
c_2 = \frac{\alpha\,\beta^{2}\,\langle k^{2}\rangle}{\gamma_m^{2}}
= \frac{40 \times 0.1^2 \times 110}{1.0^2}
= \frac{40 \times 0.01 \times 110}{1}
= \frac{44}{1}
= 44\ \text{day}^{-1},
$$

so the reduced dynamics is $\dot{\rho} = 44\, \rho^{3}$.

### 4.3 Emergent threshold and effective reproduction number

$$
\rho_c = \sqrt{\frac{\gamma}{c_2}} = \sqrt{\frac{0.2}{44}} = \sqrt{4.5454545\times10^{-3}} = 0.0674200
$$

($\approx 6.74\%$ of the population). The instantaneous reproduction number is

$$
R_{\text{eff}}(\rho) = \frac{c_2\rho^2}{\gamma} = \frac{44\,\rho^2}{0.2} = 220\,\rho^2.
$$

Checks:

- At $\rho = 0.05$: $R_{\text{eff}} = 220 \times (0.05)^2 = 220 \times 2.5\times10^{-3} = 0.55 < 1$.
- At $\rho = 0.10$: $R_{\text{eff}} = 220 \times 0.01 = 2.2 > 1$.
- At $\rho = \rho_c$: $R_{\text{eff}} = 220 \times \rho_c^2 = 220 \times (\gamma/c_2) = 220 \times (0.2/44) = 220 \times (1/220) = 1$ exactly.

For contrast, the $\ell = 1$ (simple-contagion) baseline with the same parameters gives

$$
R_0^{(\ell=1)} = \frac{\alpha\,\beta\,\langle k^{2}\rangle}{\gamma_m\,\gamma}
= \frac{40 \times 0.1 \times 110}{1.0 \times 0.2}
= \frac{440}{0.2} = 2200,
$$

that is, the same microscopic rules with linear hazard are massively supercritical from an infinitesimal seed, whereas the quadratic-hazard (memory-reinforced) system is subcritical below $\rho_c \approx 0.0674$. The comparison isolates the effect of the reinforcement exponent alone: nothing else in the model changes between the two rows.

### 4.4 Adiabatic error

The leading correction to the quasi-static memory is $m \approx m^* - \dot{m}^*/\gamma_m$, with $\dot{m}^* = \beta k \dot{\rho}/\gamma_m$. The relative correction is

$$
\frac{\dot{m}^*}{\gamma_m m^*} = \frac{\dot{\rho}}{\gamma_m\, \rho} = \frac{c_2\, \rho^2}{\gamma_m} = 44\,\rho^2 \quad (\gamma_m = 1.0).
$$

This equals $\tau_{\text{fast}}\,|f'(\rho)|$ up to order-unity factors, with $\tau_{\text{fast}} = 1/\gamma_m = 1$ day and $f'(\rho) = 3c_2\rho^2$; we quote the conservative value $\epsilon(\rho) = c_2\rho^2/\gamma_m$:

- At $\rho = 0.02$: $\epsilon = 44 \times (0.02)^2 = 44 \times 4\times10^{-4} = 1.76\times10^{-2}$.
- At $\rho = 0.05$: $\epsilon = 44 \times 2.5\times10^{-3} = 0.11$.
- At $\rho = \rho_c = 0.0674$: $\epsilon = 44 \times 4.5455\times10^{-3} = 0.20$.

The reduction is therefore accurate to about $2\%$ at $\rho = 0.02$ and degrades to $\mathcal{O}(1)$ near the threshold, where the intrinsic epidemic timescale $\tau_{\text{epi}} = 1/|f'(\rho)|$ becomes comparable to $\tau_{\text{fast}}$. This defines the validity domain of the reduction: deep in the early-growth regime and, with weaker accuracy, through the threshold crossing. Consistency with the general bound of Section 3.2 holds: the bound $\Delta \le 1/\kappa$ requires $\Delta < 1$, and $\epsilon(\rho_c) = 0.20 < 1$.

### 4.5 Growth times

Solving $\dot{\rho} = c_2\rho^3$ by separation: $\mathrm{d}(1/\rho^2)/\mathrm{d}t = -2c_2$, so the time to grow from $\rho_0$ to $\rho_1$ is

$$
t = \frac{1/\rho_0^2 - 1/\rho_1^2}{2c_2} = \frac{1/\rho_0^2 - 1/\rho_1^2}{88}.
$$

From $\rho_0 = 10^{-2}$ to $\rho_1 = \rho_c$ (using $1/\rho_c^2 = c_2/\gamma = 44/0.2 = 220$):

$$
t = \frac{10^{4} - 220}{88} = \frac{9780}{88} = 111.13636\ \text{days} \approx 111.1\ \text{days}.
$$

As a second point on the same trajectory, from $\rho_0 = 10^{-2}$ to $\rho_1 = 0.05$ (so $1/\rho_1^2 = 400$):

$$
t = \frac{10^{4} - 400}{88} = \frac{9600}{88} = 109.09091\ \text{days} \approx 109.1\ \text{days}.
$$

The two times differ by only $2.05$ days ($111.13636 - 109.09091 = 2.04545$) despite a $2.5$-fold prevalence change between $\rho = 0.05$ and $\rho = \rho_c$: nearly all the seeding time is spent at the lowest prevalences, which is the operational content of the statement that emergent complex contagions require seeding. An infinitesimal seed effectively never takes off, while a seed above $\rho_c$ invades directly.

## 5. Results

All numbers below are computed in Section 4 from the stated parameter values; none are empirical measurements or simulations.

1. **Network moment.** For the Poisson reference network with $\langle k\rangle = 10$, $\langle k^2\rangle = 110$ (Section 4.1).
2. **Reduced growth coefficient.** $c_2 = 44\ \text{day}^{-1}$, giving $\dot{\rho} = 44\rho^3$ (Section 4.2).
3. **Emergent prevalence threshold.** $\rho_c = \sqrt{0.2/44} = 0.0674200 \approx 6.74\%$ of the population (Section 4.3).
4. **Reproduction numbers.** $R_{\text{eff}}(\rho) = 220\rho^2$; $R_{\text{eff}} = 0.55$ at $\rho = 0.05$, $2.2$ at $\rho = 0.10$, and $1$ exactly at $\rho_c$. The $\ell = 1$ baseline with the same parameters gives $R_0^{(\ell=1)} = 2200$ (Section 4.3).
5. **Adiabatic error.** $\epsilon(\rho) = 44\rho^2$: $1.76\times10^{-2}$ at $\rho = 0.02$, $0.11$ at $\rho = 0.05$, $0.20$ at $\rho_c$ (Section 4.4).
6. **Seeding time.** Growth from $\rho_0 = 10^{-2}$ to $\rho_c$ takes $t = 9780/88 \approx 111.1$ days; growth from $10^{-2}$ to $0.05$ takes $109.1$ days, so $2.05$ days cover the final $2.5$-fold rise (Section 4.5).

**Projection (labeled, not computed).** Applying the reduction to coupled behavior–epidemic systems of the kind in [6] — vaccine uptake as a fast behavioral variable coupled to a simple-contagion pathogen — should yield an effective force of infection modulated by a quasi-steady uptake state, with error bounded by the behavioral relaxation ratio $\kappa_v = \gamma_v/\mu$. We project qualitatively that such reductions will produce threshold phenomena in the *behavioral* variable analogous to $\rho_c$ above; we do not report numerical values for this class, since no parameter set for it is specified here.

## 6. Discussion

**What the reduction buys.** A single principle — fast auxiliary variables equilibrate and can be eliminated — converts a family of high-dimensional contagion models into one-dimensional effective systems with nonlinear forces of infection. The worked example shows that the hallmark of complex contagion (a finite prevalence threshold, algebraic early growth, seeding dependence) emerges from simple contagion plus a fast memory loop, with all quantities obtainable in closed form. This is the mechanism-added counterpart of the canonical-model reductions of [1], [2], which obtained analytical bifurcation insights for adaptive, higher-order, and interacting contagion models that their original presentations lacked; our contribution is to show that the same elimination applies when the fast variable is an exposure accumulator rather than a correlation moment, and that the resulting force of infection is threshold-like without any stipulated threshold. The result also sharpens the inference problem highlighted by the explicit-threshold literature: [3] derives macroscopic cascade conditions from stipulated per-node thresholds, and [6] grounds vaccination thresholds in survey evidence for complex-contagion attitudes, but if emergent complex contagion is generic under fast equilibration, then observing threshold-like macrodynamics does *not* certify microlevel multiple-exposure rules. The comparison consequence stated in [1] — mechanisms sharing a characteristic form can be macroscopically indistinguishable — applies with equal force to the stipulated-versus-emergent distinction.

**Limitations and failure modes.** (i) *Chosen parameters.* All parameter values ($\beta$, $\gamma_m$, $\alpha$, $\gamma$, $\langle k\rangle$, $\ell$) are reference choices, not empirical calibrations; the specific numbers ($c_2 = 44$, $\rho_c \approx 0.0674$, $t \approx 111.1$ days) illustrate the structure, not any particular real system. (ii) *Error near threshold.* The adiabatic error reaches $0.20$ at $\rho_c$ and grows as prevalence rises further; the reduction is quantitative only in the early-growth regime. (iii) *Degree distribution.* The Poisson moment computation