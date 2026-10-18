# A Particle-Type Framework for Social Dynamics: Typed Agents, Four Interaction Channels, and a Quantitative Design Study

## Abstract

Social influence campaigns, platform integrity teams, and policymakers currently rely on influence models that treat agents as homogeneous, which prevents them from reasoning about how leaders, carriers, mediators, and unobserved populations contribute differently to behavioral cascades. The specific gap is that no existing sociophysics model assigns distinct interaction potentials per agent type and per interaction channel, so the predictive value of such a typing scheme is unknown. We formalize a "Standard Model of social particles": agents typed as baryons (stable leaders), leptons (mobile information carriers), bosons (mediators), and dark matter (unobserved populations), interacting through four channels (strong family bonds, electromagnetic like/dislike attraction, weak random transformative events, and gravity-like cultural pull), with an effective-potential description adapted from particle physics. Because no simulation has yet been run, we derive analytical design-study results under stated assumptions. Under a linear-threshold mean field with mean degree 10, lepton edge weight 0.08, threshold 0.2, and boson mediation amplification $1+\mu f_M$ with $\mu=3$, $f_M=0.1$, the critical lepton seed fraction is 0.1923 versus 0.6667 for a homogeneous baseline, a factor-3.47 reduction. Weak-force events at rate $10^{-2}$ per day convert baryons with probability 0.3935 over 100 days, 4.13 times the lepton rate. An unobserved population fraction of 0.66 biases observed reach downward by a factor of 2.941. The typed model carries 60 extra coupling parameters, requiring a log-likelihood gain above 60 (AIC) or 207.2 (BIC at $n=1000$) to justify itself. These thresholds define the falsification criteria for the planned agent-based test.

## 1. Introduction

Marketing teams that run influencer campaigns, trust-and-safety teams that track coordinated manipulation, and civil-society organizations that design behavior-change programs all face the same operational problem: they must decide where to intervene in a social system, and their current models tell them only how many agents to activate, not which kinds of agents. Influencer-selection models do distinguish node classes in practice — [4] shows with simulations on a Twitter social graph and a synthetic Watts-Strogatz graph that customer acquisition cost and conversion ratio move in opposite directions depending on influencer type and product class — but the underlying dynamics models in wide use still treat the transmitting population as interchangeable. The cost of this homogeneity is concrete: a campaign or counter-campaign designed on a homogeneous-agent model can be sized wrong by a large factor, and Section 4 derives a factor of 3.47 between the seed fraction a typed model and a homogeneous model require for the same cascade.

What would change if a typed framework held? A campaign designer could compute, before spending, how many mobile carriers versus mediators versus leaders must be activated. A platform integrity team could estimate how much observed diffusion underestimates true reach when part of the population is invisible to measurement — Section 4 derives an underestimate by a factor of 2.941 at a 0.66 unobserved fraction. A policy analyst could estimate how large a random shock (a "weak-force" event) must be to flip stable leaders, which [2] shows is a live concern: that work documents how social bots were used during the 2016 US Presidential Election to sway conversation around candidates, and reviews bot-creation mechanics and detection methods, so the question of how non-human and human agent classes differ in diffusion dynamics is already operational.

This paper does not claim the framework works. It builds the framework, derives its first quantitative consequences, and states exactly what must be measured for the framework to be accepted or rejected. The stance follows [7], which advises modelers of complex social systems to build parsimonious models, balance assumptions against available data, design a clear testing method, and accept being "wrong in a meaningful way"; and it borrows its formal template from particle physics, where [8] presents the effective-potential formalism — a real scalar function of fields whose minima are the vacua — as the standard tool for analyzing transitions between states, and where [11] documents both the power of the Standard Model Lagrangian structure and its cost: at least 19 arbitrary, un-derived parameters supplied from measurement. Any social analog must confront the same parameter-count problem, and Section 4 quantifies it.

The contributions are:

1. A typed-agent formalism for social dynamics with four particle classes and four interaction channels, expressed as an effective potential in the form used in [8] (Section 3).
2. A mean-field derivation of the critical seed fraction for influence cascades, giving 0.1923 for the typed model against 0.6667 for a homogeneous baseline under stated assumptions (Section 4.1).
3. A derivation of weak-force perturbation sensitivity, giving baryon conversion probability 0.3935 over 100 days at event rate $10^{-2}$ per day, 4.13 times the lepton conversion probability, and a second-order reach estimate of 78.7 additional adopters (Section 4.2).
4. A derivation of the observational bias introduced by an unobserved "dark" population, a factor of 2.941 at $f_D = 0.66$ (Section 4.3).
5. A parameter-cost accounting: 64 typed coupling parameters against 4 homogeneous ones, with AIC and BIC break-even log-likelihood gains of 60 and 207.2 respectively, and a specification cost of 694.18 bits using the per-parameter entropy of 11.5697 bits from [9] (Section 4.4).
6. A spinodal calculation for the gravity channel: the external cultural-pull field needed to erase a metastable consensus is $h_{\mathrm{spin}} = 0.3849$ for the chosen potential (Section 4.5).

## 2. Background and Related Work

The proposed framework sits at the intersection of multirelational social network analysis, agent-based diffusion modeling, and physics-inspired sociophysics. Each strand supplies one ingredient, and each also supplies a caution.

Multirelational structure. [1] proposes a multidimensional social network in which the relations extracted from users' collective behavior in an online sharing system are grouped into layers built on two relation types, direct and object-based; this layering is the empirical precedent for typing social interactions into distinct channels rather than collapsing them into one weighted graph. [6] extends this line by introducing a multirelational social network covering both direct and object-based relationships for generating relation suggestions between users in a multimedia sharing system. Together these works establish that social data already separates into distinguishable relation types; what they do not do is assign different interaction dynamics per type, which is the step this paper takes.

Non-human and unobserved agents. [2] investigates the role of social bots in content spreading, reviewing how bots are created and operated, the challenges of detecting them via graph-centric, crowdsourcing, and feature-based supervised methods, and case studies including bot influence on political discussion during the 2016 US Presidential Election and social spam campaigns. This motivates two of the four particle classes: agents that diffuse without being human (a distinct type with distinct dynamics), and the population that platform measurement misses, which this paper models as dark matter. The detection problem documented in [2] is precisely the boundary-drawing problem for the dark sector.

Measuring dynamics. [3] defines differences between network snapshots by means of a Graph Differential Tuple, enabling distance measures and investigation of the speed of changes. Any test of the typed framework against empirical networks will need exactly such snapshot-difference machinery, because the four interaction channels predict different time signatures: strong bonds should change slowly, weak-force events should appear as discontinuous jumps. [3] supplies the measurement instrument for that comparison.

Typed diffusion models in practice. [4] models influencer marketing campaigns and validates on a real-world Twitter social graph whose outdegree distribution obeys a power law, plus a synthetic Watts-Strogatz small-world graph whose distribution does not; the authors find that customer acquisition cost decreases with smaller influencer types for non-luxury products ($\Omega=0.9$) while conversion ratio increases, that for luxury products ($\Omega=0.1$) acquisition cost increases with smaller influencers, and that observations made on the real-world network do not hold on the synthetic graph because the outdegree distributions differ. Each result was averaged over 10 trials. This is the closest existing practice to typed-agent dynamics, and its finding that conclusions are graph-dependent is a direct warning for the framework proposed here: type-dependent results must be validated per network, not assumed universal.

Physics-inspired social modeling. [5] models the Information Society with Ising agents and a multiagent system, running simulations with ten agents, equal selection pressure ($a=1$), $\beta=1$, and fixed $\gamma_{i,j}$ coupling values of $+1$ or $-1$; the conclusion reports that adequate policies drastically reduce the time for agents to arrive at the "in" state, that without an external field a lower number of agents is found "in" and the evolution range is around three times greater, and that the work gives an indication of the order of magnitude of the number of cooperating agents needed to overturn an opposing attitude. The external field in [5] is the direct ancestor of the gravity channel in this paper — an unconscious, global pull — and the factor-of-three evolution-range result is the kind of quantity a typed model should reproduce or improve upon.

Methodological framing. [7] surveys data-driven modeling of complex social systems — traffic, crowds, echo chambers, opinion dynamics — and argues for parsimonious models with clear testing methods, concluding with the advice that all models are "wrong" in some sense and the goal is to be wrong in a meaningful way. This paper adopts that stance explicitly: the typed framework is a hypothesis to be tested, not a truth claim. [10] supplies a complementary caution from network science: it develops a hierarchical framework in which equivalence between two networks must be assessed progressively across topological structure, functional architecture, and dynamic behavior (its L1-L2-L3 hierarchy), arguing that no single measure captures equivalence. Applied here, this means showing that the typed model reproduces empirical network structure (L1) is not enough; it must also match functional and dynamic behavior (L2-L3), which is why the test design in Section 7 checks cascade dynamics, not just clustering.

The physics template and its cost. [8] presents the effective-potential formalism used in particle physics: the effective potential is a real scalar function of one or more scalar fields whose minima are the vacua, with the tree-level potential in $d=4$ restricted by renormalizability to quartic powers of the fields, written as a constant term plus linear, quadratic, cubic, and quartic field terms. Section 3 adopts exactly this restricted form for a social order parameter. [8] also connects first-order phase transitions to observable signatures (gravitational waves from early-Universe transitions), which is the structural analogy for this paper's claim that weak-force perturbations should produce detectable discontinuities in social time series. On the cost side, [11] documents that the Standard Model's empirical success is coupled to severe formal deficits, including at least 19 arbitrary, un-derived parameters supplied from experiment, and a gauge architecture $G_{\mathrm{SM}} = \mathrm{SU(3)}_C \times \mathrm{SU(2)}_L \times \mathrm{U(1)}_Y$ whose Lagrangian decomposes into sectors including gauge dynamics with cubic and quartic self-interaction terms for the non-Abelian subgroups. The 19-parameter lesson is quantified for the social case in Section 4.4. [9] contributes the accounting tool: it computes the approximation entropy cost of specifying a continuous parameter at tolerance $\varepsilon = 10^{-4}$ as $H_{\mathrm{app}}(10^{-4}) = 11.5697$ bits (about 12 bits per continuous parameter), derived from a Farey-type count of the rational grid with maximal denominator $Q=100$ containing approximately 3040 distinct reduced fractions. Section 4.4 uses this figure to price the typed model's parameter specification. Finally, [12] frames theory evaluation through Lakatosian research programmes, with a "hard core" of axioms protected by a "protective belt" of auxiliary hypotheses, and notes that methodology has a clear procedure for rejecting theories that attack the hard core but no formal path for comparative assessment. Section 6 uses this framing to state which observation would expel the typed framework from consideration rather than merely adjusting its protective belt.

## 3. Methods

### 3.1 Agent types

We assume a closed population of $N$ agents partitioned into four classes:

- **Baryons** $B$: stable leaders. Low mobility, high connection stability, high resistance to conversion. Count $N_B = f_B N$.
- **Leptons** $L$: mobile information carriers. High mobility, low tie strength, low conversion resistance. Count $N_L = f_L N$.
- **Bosons** $M$: mediators. Agents whose presence amplifies transmission between other agents without themselves being primary sources. Count $N_M = f_M N$.
- **Dark matter** $D$: unobserved populations. Agents invisible to platform measurement but participating in dynamics. Count $N_D = f_D N$.

We assume throughout the design study $N = 1000$, $f_B = 0.04$, $f_L = 0.20$, $f_M = 0.10$, $f_D = 0.66$. These are illustrative design values, not measurements; Section 6 treats sensitivity to them.

### 3.2 Interaction channels

Four channels, each with its own potential, mirror the four physical forces:

- **Strong** $s$: family/close bonds. Short-range, high weight, slow to form or break.
- **Electromagnetic** $e$: like/dislike attraction, signed (attractive or repulsive), medium range.
- **Weak** $w$: random transformative events at low per-agent rate $\lambda_w$, changing an agent's state discontinuously.
- **Gravity** $g$: unconscious cultural pull, long-range, unscreened, modeled as an external field $h$ on a social order parameter.

### 3.3 Effective potential

Following the tree-level form in [8], which restricts renormalizable potentials in $d=4$ to quartic powers of the fields, we write a social effective potential for a scalar order parameter $\phi$ (population-level behavioral alignment, $\phi \in [-1, 1]$):

$$V(\phi) = \Lambda^4 + t\,\phi + \frac{1}{2}m^2 \phi^2 + \frac{1}{6}\kappa \phi^3 + \frac{1}{24}\lambda \phi^4 - h\,\phi,$$

where $t$ is a seed influence (analog of a source term), $m^2$ sets the stability of the current consensus, $\kappa$ and $\lambda$ are self-interaction strengths of the behavioral field, and $h$ is the gravity-channel external field, directly analogous to the external field in the Ising treatment of [5]. Minima of $V$ are social vacua (stable consensus states); a first-order transition between vacua, in the sense of [8], corresponds to a rapid population-wide behavioral flip. The weak channel enters not through $V$ but as a Poisson process on agent states, as specified in Section 4.2.

### 3.4 Cascade dynamics

Transmission is a linear threshold process. Agent $i$ adopts a behavior when the weighted influence from active neighbors reaches its threshold $\theta_i$; we take a homogeneous threshold $\theta = 0.2$ for the design study. Lepton edges carry weight $w_L = 0.08$. Boson mediation multiplies lepton influence by an amplification factor $(1 + \mu f_M)$ with mediation strength $\mu = 3$. Each agent has mean degree $\bar{k} = 10$. The homogeneous baseline assigns every edge weight $w_h = 0.03$ and no mediation. All values in this paragraph are stated design assumptions; the derivations in Section 4 show every arithmetic step from them.

### 3.5 Validation design (specified, not executed)

No simulation or empirical measurement is reported in this paper. The planned validation, specified here for completeness, follows the practice of [4]: run the typed dynamics on a real-world social graph (the Twitter social graph and GooglePlus graph used in [4] are candidate substrates) and on a synthetic Watts-Strogatz graph, compare against homogeneous-agent and random baselines on clustering, cascade size, and cascade timing, and use snapshot-difference measures in the sense of [3] to test the predicted time signatures of the four channels. Results of that validation are future work.

## 4. Analysis

Every input number in this section is a stated design assumption from Section 3 or a figure attributed to a cited work; every arithmetic step is shown.

### 4.1 Critical seed fraction for cascades

**Setup.** In the mean field, a susceptible agent's influence from active leptons is

$$I_L = \bar{k}\, f_L\, w_L\,(1 + \mu f_M).$$

**Step 1: mediation amplification.** With $\mu = 3$ and $f_M = 0.10$:

$$1 + \mu f_M = 1 + 3 \times 0.10 = 1.30.$$

**Step 2: influence per unit lepton fraction.** With $\bar{k} = 10$ and $w_L = 0.08$:

$$\bar{k}\, w_L\,(1+\mu f_M) = 10 \times 0.08 \times 1.30 = 1.04.$$

**Step 3: critical fraction.** The cascade condition is $I_L \geq \theta$ with $\theta = 0.2$, so

$$f_L^{\mathrm{crit}} = \frac{\theta}{\bar{k}\, w_L\,(1+\mu f_M)} = \frac{0.2}{1.04} = 0.19231.$$

**Step 4: no-mediation comparison.** With $f_M = 0$ the amplification is $1.00$ and

$$f_{L,\,\mathrm{no\,med}}^{\mathrm{crit}} = \frac{0.2}{10 \times 0.08 \times 1.00} = \frac{0.2}{0.80} = 0.25.$$

**Step 5: relative reduction from mediation.**

$$\frac{0.25 - 0.19231}{0.25} = \frac{0.05769}{0.25} = 0.2308,$$

i.e. boson mediation lowers the required lepton seed fraction by 23.08%.

**Step 6: homogeneous baseline.** With all edges at $w_h = 0.03$ and no type structure, the critical active fraction is

$$f_h^{\mathrm{crit}} = \frac{\theta}{\bar{k}\, w_h} = \frac{0.2}{10 \times 0.03} = \frac{0.2}{0.30} = 0.6667.$$

**Step 7: typed-to-homogeneous ratio.**

$$\frac{f_h^{\mathrm{crit}}}{f_L^{\mathrm{crit}}} = \frac{0.6667}{0.19231} = 3.467.$$

Under these assumptions the typed model predicts cascades from a seed fraction 3.47 times smaller than the homogeneous model. This is the paper's headline analytical contrast; it is a consequence of the assumed weights, not a measurement.

### 4.2 Weak-force perturbation sensitivity

**Setup.** Weak events arrive as a Poisson process with rate $\lambda_w = 10^{-2}$ events per agent per day (assumption). Conversion resistance per class: $r_B = 0.5$ for baryons, $r_L = 0.1$ for leptons (assumptions). Effective conversion rate is $\lambda_w r$.

**Step 1: baryon conversion probability over $T = 100$ days.**

$$\lambda_w r_B T = 10^{-2} \times 0.5 \times 100 = 0.5,$$
$$p_B = 1 - e^{-0.5} = 1 - 0.60653 = 0.39347.$$

**Step 2: lepton conversion probability over the same window.**

$$\lambda_w r_L T = 10^{-2} \times 0.1 \times 100 = 0.1,$$
$$p_L = 1 - e^{-0.1} = 1 - 0.90484 = 0