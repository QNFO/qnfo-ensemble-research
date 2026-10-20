# Fixed Points in Possibility Space: A Derivable Model Linking the Convergence of Physical Systems to the Polygenesis of Theories

## Abstract

Scientific ideas are sometimes discovered independently by researchers with no contact, just as unrelated physical systems sometimes exhibit identical macroscopic behavior. Both phenomena are conventionally treated as separate: one as sociology of science, the other as physics. This paper tests the claim, advanced in prior meta-analysis, that they are two manifestations of a single structure — attractors in a "possibility space" of consistent theories, organized by renormalization-group (RG) flow. The gap is formal: no existing work defines a metric on theory space, derives a polygenesis probability from attractor geometry, or states what observation would falsify the claim. We model theory space as a metric space of Lagrangians equipped with coarse-graining flows, define a similarity distance through shared long-distance observables, and derive two quantitative results. First, the probability that $k$ independent discovery trajectories converge to the same fixed point equals the Herfindahl concentration $\sum_i p_i^k$ of the basin-volume distribution $\{p_i\}$; for an illustrative five-basin landscape this gives $P_{3}=0.08875$ for triple polygenesis and $P_{2}=0.275$ for double. Second, discovery trajectories behave as strongly convex optimization, so the iteration count to reach an $\epsilon$-neighborhood of a fixed point scales as $O(1/\epsilon)$, matching known convergence times of dual subgradient methods; a worked case gives $458.2$ iterations. The framework makes the philosophical claim falsifiable: basin-geometry measurements must predict which ideas are multiply discovered, with an odds ratio of $(p_{\max}/p_{2})^{2}=2.56$ in the worked landscape. This converts a metaphysical thesis into a testable model of scientific priority disputes, research-strategy design, and the predictability of discovery.

## 1. Introduction

Research teams at pharmaceutical companies, national laboratories, and machine-learning firms routinely discover that a result they worked months to obtain was found independently, and nearly simultaneously, by a rival group. Historians of science document the pattern at scale: the calculus of Newton and Leibniz, the independent invention of zero in Maya and Indian mathematics, and the renormalization group developed along distinct lines by the Gell-Mann/Low and Kadanoff/Wilson schools [8]. Each episode of such "polygenesis" costs the losing parties priority, patents, and careers, and each costs the research system resources spent duplicating work whose inevitability nobody could estimate. Today no method exists to predict, before the fact, which open problems are likely to be solved independently and which are likely to have a single discoverer. A capability that estimated polygenesis risk from the structure of a problem itself would change how funders sequence grants, how firms decide between racing and waiting, and how historians adjudicate priority claims.

The same structure appears on the physical side. Unrelated microscopic systems — a random quantum antiferromagnetic chain and a transverse-field Ising chain, for instance — flow under coarse-graining to the same infinite-randomness fixed point and share asymptotic low-energy properties [4]. Inflationary models from the $\alpha$-attractor and $\xi$-attractor families, constructed independently, give identical tree-level predictions $n_{s}=1-2/N+O(N^{-2})$ and $r=12/N^{2}+O(N^{-3})$, and these predictions survive quantum corrections exactly to leading order in $1/N$ [2]. Universality of critical exponents near infrared fixed points is the standard explanatory tool for this physical convergence [5]. The prior meta-analysis of [8] argues that physical convergence and epistemic consilience are "symmetric faces" of attractors in possibility space, with the renormalization group simultaneously an instance, a mechanism, and a model of the unity. What that argument lacks, and what this paper supplies, is a mathematical object: a metric on theory space, a flow, and a theorem-level statement of when independent searchers must meet.

The core idea is simple to state. If the space of consistent Lagrangians or equations is not flat — if it has hills, valleys, and fixed points under coarse-graining — then both a physical system relaxing under RG flow and a research community searching through hypotheses are trajectories on the same landscape. Trajectories that start far apart but fall into the same basin end at the same fixed point; the physicist calls this universality, the historian calls it simultaneous discovery. The claim becomes science when basin geometry is measured and polygenesis rates are predicted from it, because a wrong basin geometry gives wrong polygenesis statistics.

This paper's contributions are:

- A formal definition of theory space as a metric space of Lagrangians with a similarity distance built from shared infrared observables, and the identification of the RG flow as the dynamics on it (Section 3).
- A derivation that the probability of $k$-fold polygenesis equals the order-$k$ Herfindahl concentration of the basin-volume distribution, computed for an illustrative landscape as $P_{2}=0.275$ and $P_{3}=0.08875$ (Section 4.2).
- A derivation that discovery trajectories, modeled as dual subgradient ascent on a strongly convex program, reach an $\epsilon$-neighborhood of a fixed point in $O(1/\epsilon)$ iterations, with the worked value $458.2$ iterations for the stated parameters (Section 4.3).
- A falsifiable prediction: the odds ratio for the most-discovered versus second-most-discovered idea is $(p_{\max}/p_{2})^{2}$, equal to $2.56$ in the worked landscape, so basin-volume measurements alone rank polygenesis risk (Section 4.4).
- A mapping of the framework onto the cited RG literature — geometric convergence [1], cosmological attractors [2], optimization convergence [3], strong randomness [4], nonequilibrium functional RG [5], disordered systems [6], confinement [7] — showing each supplies one structural ingredient (Sections 2 and 4.5).

## 2. Background and Related Work

The thesis that convergence and consilience share a single underlying structure originates in the meta-analysis of [8], which defines convergence as the independent origin of similar traits or ideas in distinct lineages or minds without contact, and consilience as knowledge from different disciplines converging on the same truths. That document argues the two are symmetric — convergence the ontological signature of attractors in possibility space, consilience the epistemological program that reconstructs them — and presents the renormalization group as the meta-example, at once a case of independent invention (Gell-Mann/Low versus Kadanoff/Wilson) and the mathematical mechanism explaining why convergence occurs [8]. This paper accepts that framing as its hypothesis and converts it into a quantitative model; where [8] argues by gallery of examples, we derive probabilities and falsification conditions.

The first ingredient is a well-behaved notion of convergence on an abstract space of mathematical objects. Geometric analysis supplies a cautionary and constructive precedent. The survey of compactness and stability conjectures from the 2018 IAS workshop on scalar curvature and convergence shows that even for three-dimensional manifolds with positive scalar curvature, a single increasingly thin well prevents a smooth or Lipschitz limit, and increasingly many wells destroy even the Gromov-Hausdorff limit; the authors therefore develop weaker notions, such as the $\mathcal{VF}$ (intrinsic flat) convergence, under which a sequence of manifolds with no GH limit can still converge to a round sphere [1]. The lesson transferred here is that the choice of metric on the space of objects determines whether convergence theorems exist at all: with the wrong metric, sequences that "should" converge do not. Our similarity metric on theory space (Section 3) is the analogue of choosing intrinsic-flat over Gromov-Hausdorff distance — it must be weak enough that distinct derivations of the same theory register as close, and strong enough that genuinely different theories stay separated.

The second ingredient is the RG as a flow with robust, metric-independent outcomes. The analysis of cosmological attractors demonstrates exactly the robustness property the polygenesis model needs: working with the RG-improved action, the authors show that although slow-roll parameters and efold counts acquire beta-function dependence, "when calculating the spectral index and tensor-to-scalar ratio, all corrections exactly cancel," so the predictions $n_{s}=1-2/N$ and $r=12/N^{2}$ are unaffected by quantum corrections to leading order in $1/N$ [2]. In our language, the $\alpha$- and $\xi$-attractor families are distinct coordinate patches of theory space flowing to one infrared fixed point, and the cancellation result shows the fixed point's observable signature is invariant under a large class of deformations of the flow itself — precisely the condition under which independent discoverers, using different formalisms, agree on the same numbers.

The third ingredient is a convergence-time theorem for search trajectories. The study of dual subgradient methods for strongly convex programs proves that for general strongly convex programs the convergence time of the dual method with simple running averages improves from the general convex bound $O(1/\epsilon^{2})$ to $O(1/\epsilon)$, and further to $O(\log(1/\epsilon))$ when the dual function is locally quadratic [3]. The program class matters: it covers non-differentiable objectives with Lipschitz constraints, arising in model predictive control, decentralized multi-agent control, and network flow control [3]. We import this theorem in Section 4.3 as the dynamics of a discovery process: a researcher (or research community) accumulating evidence is modeled as dual ascent, and strong convexity of the "evidence functional" is the assumption under which discovery time is polynomial rather than quadratic in the precision demanded.

The fourth ingredient is the phenomenology of RG fixed points beyond the translationally invariant, perturbative setting. The strong-randomness RG review records that almost all RGs coarse-grain by integrating out the highest-energy or stiffest degrees of freedom, that the first strong-randomness RG (Ma, Dasgupta and Hu, 1979) treated random quantum antiferromagnets whose ground state is a random-singlet state of spin pairs at sample-dependent distances, and that the transverse-field Ising chain's infinite-randomness fixed point is closely related to the random-singlet one, with an infinite series of discretely distinct infinite-randomness fixed points governing other one-dimensional systems [4]. This is the cleanest known physical instance of polygenesis-by-attractor: two microscopically unrelated Hamiltonians share one fixed point, and the shared asymptotics (e.g., activated scaling) are the "same equation discovered twice." The review also notes generalization to the many-body localization transition [4], showing the attractor picture extends across problem classes — the analogue of one mathematical structure recurring across scientific fields.

The fifth ingredient is the generality of the RG framework across formulations. The nonequilibrium functional RG lectures note that equilibrium classification by RG fixed points, especially infrared fixed points characterized by universality, is powerful, while a fixed-point classification far from equilibrium is much less developed; they then show, for wave turbulence in relativistic scalar field theory, that the functional RG describes both perturbative and nonperturbative regimes where Boltzmann equations describe only the former, solved approximately with a 2PI resummed large-$N$ expansion to NLO [5]. For our model this supplies the warning and the promise: attractor landscapes exist even out of equilibrium, but their basin structure is harder to compute, so a polygenesis theory for "far-from-equilibrium" scientific fields (fast-moving, noisy evidence accumulation) will need the coarse-graining operators to be constructed rather than assumed.

The sixth ingredient is a setting where the RG acts on a hierarchical rather than Euclidean structure. The thesis on disordered systems builds spin and structural-glass models on Dyson hierarchical lattices — "the simplest non-mean-field systems where the RG framework emerges in a natural way" — and reports the first evidence of a non-mean-field supercooled liquid undergoing a Kauzmann transition in the Hierarchical Random Energy Model, plus a two-loop Wilson-style perturbative calculation generating invariants such as $\text{Tr}[Q^{2}]$, $\text{Tr}[Q^{3}]$ up to fifth order in $Q$ [6]. Hierarchical lattices are the natural discretization of our possibility space: a tree of coarse-grainings in which each node is a theory and each edge a simplification step. The HREM result shows that even on such trees, phase structure (here, which basin dominates) can be established nontrivially [6].

The seventh ingredient is a case where the RG generates structure rather than merely classifying it. The confinement review presents quark confinement as "the quintessential problem of dimensional transmutation, where renormalization introduces a length scale into a classically scale-invariant system," records that lattice gauge theory established the physical basis (a force independent of distance at large separation, with string tension $\sigma$ the force constant at infinite separation), and describes the $R^{3}\times S^{1}$ models where confinement is reliably demonstrable semiclassically through center symmetry, the effective potential for the Polyakov line $P$, instantons, and monopoles [7]. Dimensional transmutation is the mechanism by which a featureless theory space acquires a distinguished scale and hence distinguished basins; without scale generation, all trajectories are equivalent and polygenesis would be structureless. The review's conclusion that approaches "have more in common with each other than the use of the renormalization group" [7] is itself a consilience datum of the type the model should predict.

Together these seven works and the framing document [8] supply, respectively: the metric lesson [1], the robustness condition [2], the convergence-time theorem [3], the multi-system attractor phenomenology [4], the out-of-equilibrium extension [5], the hierarchical discretization [6], and the scale-generation mechanism [7], all under the hypothesis of [8]. No one of them states the polygenesis theorem; Section 3 assembles them into a model that does.

## 3. Methods

### 3.1 Theory space and its metric

We define theory space $\mathcal{T}$ as the set of equivalence classes of Lagrangians (or, more generally, systems of equations) that are internally consistent, meaning they admit a well-defined variational principle and a well-defined long-distance limit. Two Lagrangians that differ by a total derivative or a field redefinition define the same class. This is a definition of the model, not a claim about the world.

The similarity metric is built from observables, following the lesson of [1] that the metric must be adapted to the structure one wants to preserve. Let $\mathcal{O}$ be a countable set of long-distance observables (correlation functions, critical exponents, dimensionless ratios) on which all theories in $\mathcal{T}$ can be compared. For theories $T_{a}, T_{b} \in \mathcal{T}$ define

$$
d(T_{a}, T_{b}) \;=\; \sup_{O \in \mathcal{O}} \; \frac{\big|\,O[T_{a}] - O[T_{b}]\,\big|}{1 + \big|\,O[T_{a}]\big| + \big|\,O[T_{b}]\big|} \, .
$$

This is a relative-error supremum: it is weak enough that theories agreeing on all infrared observables have $d = 0$ (they are the same fixed point, whatever their microscopic notation), and strong enough that a single sharply differing observable keeps theories separated. We assume $\mathcal{O}$ is chosen so that $d$ is a true metric (nonnegativity, symmetry, triangle inequality hold by construction of the supremum form; the only nontrivial assumption is that $d(T_a,T_b)=0$ implies equivalence, which holds because equivalence was defined through shared observables).

### 3.2 The flow

The dynamics on $\mathcal{T}$ is coarse-graining: Wilsonian integration of short-distance degrees of freedom, which [4] identifies as the near-universal feature of all RGs ("integrating out of the highest-energy or in some sense 'stiffest' degrees of freedom"). We write the flow as

$$
\frac{d T}{d \ell} \;=\; -\nabla_{\mathcal{T}} \Phi(T) + \eta(\ell)\,,
$$

where $\ell = \ln b$ is the logarithm of the coarse-graining scale $b$, $\Phi$ is a potential whose minima are the consistent long-distance theories, and $\eta$ represents stochastic perturbations (for a physical system, thermal or quenched noise as in the strong-randomness setting [4]; for a research trajectory, idiosyncratic choices of formalism, notation, and auxiliary assumptions). A fixed point $T^{*}$ satisfies $\nabla_{\mathcal{T}}\Phi(T^{*}) = 0$. The basin $B_{i}$ of fixed point $T^{*}_{i}$ is the set of initial conditions flowing to it.

For a research trajectory, the same equation is read as evidence accumulation: the "coarse-graining" step discards fine details of the hypothesis (failed formalisms, redundant notation) and keeps only what survives scrutiny. This reading is the model's central interpretive move, taken from [8]; its justification is predictive success, tested in Section 4.

### 3.3 Discovery as optimization

We model an individual discovery trajectory as a dual subgradient method on a strongly convex program, in the class studied in [3]:

$$
\min_{x \in \mathcal{X}} \; f(x) \quad \text{s.t.} \quad g_{k}(x) \le 0, \; k = 1,\dots,m\,,
$$

where $x$ parametrizes the hypothesis under consideration, $f$ is an evidence functional (a measure of unexplained phenomena given the hypothesis, assumed continuous and strongly convex on the closed convex set $\mathcal{X}$), and the constraints $g_{k}$ encode consistency requirements (Lipschitz continuous and convex, as in [3]). Strong convexity of $f$ implies the optimum is unique, exactly as stated in [3]; the unique optimum is the fixed point $T^{*}$ toward which the trajectory converges. The dual method with running averages is the algorithm; its convergence time in the class of [3] is $O(1/\epsilon)$ for an $\epsilon$-approximate solution (defined there as a feasible $x^{\epsilon}$ with $f(x^{\epsilon}) \le f(x^{*}) + \epsilon$).

### 3.4 Polygenesis probability

Let the landscape have $N_{b}$ accessible fixed points with basin volumes $v_{1}, \dots, v_{N_{b}}$ measured as fractions of the total volume of the reachable region of $\mathcal{T}$, so $\sum_{i} v_{i} = 1$. We assume that a discovery trajectory's initial condition is drawn independently and uniformly from the reachable region — this is the model's key stochastic assumption, and it is the assumption whose failure the falsification test of Section 4.4 targets. Then the probability that a single trajectory lands in basin $i$ is $p_{i} = v_{i}$, and for $k$ independent trajectories the probability that all land in the same basin is

$$
P_{k} \;=\; \sum_{i=1}^{N_{b}} p_{i}^{\,k}\,,
$$

the order-$k$ Herfindahl concentration of the basin-volume distribution. The probability that at least two of $k$ trajectories coincide is $1 - k!\,e_{k}(p_{1},\dots,p_{N_b})$-type combinatorial expressions; we compute only the all-agreement case $P_k$ and the pairwise quantity needed for the odds ratio, keeping every arithmetic explicit.

### 3.5 What is computed and what is assumed

The paper performs no simulation and no measurement. Section 4 contains: (i) exact algebraic derivations of the polygenesis formulas; (ii) fully worked numerical evaluations on one illustrative basin distribution, labeled as illustrative; (iii) a worked convergence-time calculation importing the $O(1/\epsilon)$ theorem of [3] with stated parameter values, labeled as assumptions; and (iv) a structural comparison with the cited RG literature. All numerical inputs not taken from a cited work are declared as assumptions at the point of use.

## 4. Analysis

### 4.1 Setup of the illustrative landscape

We need a concrete basin-volume distribution to evaluate the formulas. No source supplies one, so we construct an illustrative landscape and label every number as an assumption.

**Assumption A1.** The reachable region of theory space for a given problem class contains $N_{b} = 5$ fixed points with basin-volume fractions

$$
p_{1} = 0.40, \quad p_{2} = 0.25, \quad p_{3} = 0.20, \quad p_{4} = 0.10, \quad p_{5} = 0.05\,.
$$

Check of normalization: $0.40 + 0.25 + 0.20 + 0.10 + 0.05 = 1.00$. ✓

The distribution is deliberately skewed: one dominant attractor (the "obvious" theory), one strong competitor, and a tail of niche fixed points. This shape is qualitatively motivated by the strong-randomness phenomenology of [4], where a small set of infinite-randomness fixed points governs wide classes of one-dimensional systems, but the specific values are ours.

### 4.2 Polygenesis probabilities

**Claim 1 (pairwise polygenesis).** For two independent trajectories, the probability both reach the same fixed point is

$$
P_{2} = \sum_{i=1}^{5} p_{i}^{2}\,.
$$

Arithmetic, term by term:

$$
p_{1}^{2} = 0.40^{2} = 0.1600\,,
$$
$$
p_{2}^{2} = 0.25^{2} = 0.0625\,,
$$
$$
p_{3}^{2} = 0.20^{2} = 0.0400\,,
$$
$$
p_{4}^{2} = 0.10^{2} = 0.0100\,,
$$
$$
p_{5}^{2} = 0.05^{2} = 0.0025\,.
$$

Summing:

$$
P_{2} = 0.1600 + 0.0625 + 0.0400 + 0.0100 + 0.0025 = 0.2750\,.
$$

So under Assumption A1, two independent discoverers of a problem in this class agree on the same theory with probability $P_{2} = 0.275$, i.e., $27.5\%$.

**Claim 2 (triple polygenesis).** For three independent trajectories, all three agree with probability

$$
P_{3} = \sum_{i=1}^{5} p_{i}^{3}\,.
$$

Arithmetic:

$$
p_{1}^{3} = 0.40^{3} = 0.064000\,,
$$
$$
p_{2}^{3} = 0.25^{3} = 0.015625\,,
$$
$$
p_{3}^{3} = 0.20^{3} = 0.008000\,,
$$
$$
p_{4}^{3} = 0.10^{3} = 0.001000\,,
$$
$$
p_{5}^{3} = 0.05^{3} = 0.000125\,.
$$

Summing:

$$
P_{3} = 0.064000 + 0.015625 + 0.008000 + 0.001000 + 0.000125 = 0.088750\,.
$$

So three independent discoverers all converge to one theory with probability $P_{3} = 0.08875$, i.e., $8.875\%$.

**Claim 3 (dominant-basin share of polygenesis).** The fraction of all pairwise polygenesis events attributable to the dominant basin $B_{1}$ is

$$
\frac{p_{1}^{2}}{P_{2}} = \frac{0.1600}{0.2750} = 0.581818\ldots \approx 0.582\,.
$$

Arithmetic: $0.1600 / 0.2750 = 16/27.5 = 0.581818\ldots$ So about $58.2\%$ of two-discoverer coincidences happen because both fell into the largest basin; the dominant attractor dominates the polygenesis record.

### 4.3 Convergence time of a discovery trajectory

We now import the convergence-time theorem of [3]. That work proves that for general strongly convex programs (possibly non-differentiable, with Lipschitz convex constraints), the dual subgradient method with simple running averages converges in $O(1/\epsilon)$ iterations to an $\epsilon$-approximate solution, improving on the $O(1/\epsilon^{2})$ bound for general convex programs, and reaching $O(\log(1/\epsilon))$ when the dual function is locally quadratic [3].

**Assumption A2.** A research trajectory is a dual subgradient iteration in the class of [3]: the evidence functional is strongly convex with strong-convexity parameter $\mu$, the step size is $\eta = 1/\mu$ scaled so that the distance to the optimum contracts by the factor $q = 1 - \mu\eta$ per iteration in the regime where the running average dominates. We take the concrete values

$$
\mu\eta = 0.01 \quad\Rightarrow\quad q = 0.99\,,
$$
$$
d_{0} = 1 \quad (\text{initial distance to the fixed point, in units of the reachable-region diameter})\,,
$$
$$
\epsilon = 10^{-2} \quad (\text{target relative precision on the observables defining } T^{*})\,.
$$

**Claim 4 (iteration count).** Under linear contraction, the iteration count $n$ satisfies $d_{0}\, q^{\,n} \le \epsilon$, so

$$
n \;=\; \frac{\ln(\epsilon / d_{0})}{\ln q} \,.
$$

Arithmetic:

$$
\ln(\epsilon / d_{0}) = \ln(10^{-2}) = -4.605170\,,
$$
$$
\ln(0.99) = -0.01005034\,,
$$
$$
n = \frac{-4.605170}{-0.01005034} = 458.21\ldots \approx 458.2\,.
$$

So with a one-percent per-iteration contraction, a discovery trajectory reaches one-percent precision on the fixed point's observables in approximately $458$ iterations. Each "iteration" is one coarse-graining cycle of the research process — one round of simplification, consistency checking, and comparison against evidence. The number is a projection under Assumptions A2's parameter values; the structural content, the $O(1/\epsilon)$ scaling, is the theorem of [3] and is parameter-free within its class.

**Claim 5 (logarithmic regime).** If the dual function is locally quadratic at the fixed point — the additional condition identified in [3] — the convergence time drops to $O(\log(1/\epsilon))$. Repeating the same contraction arithmetic with a locally quadratic dual, for which [3]'s Appendix E analysis shows the Hessian $\nabla^{2}_{\lambda} q(\lambda^{*})$ is negative definite on the active constraint set, the effective contraction accelerates; the qualitative prediction is that mature problems (where the evidence functional is smooth and locally quadratic near the answer) are discovered faster per unit of remaining precision than frontier problems. This is a structural corollary of [3]'s two regimes, not an independent measurement.

### 4.4 The falsifiable prediction: basin geometry ranks polygenesis

The model's empirical content is that basin volumes, which are in principle measurable from the RG landscape (by sampling initial conditions and integrating the flow, or by measuring the attraction coefficients of competing formalisms), predict the polygenesis record.

**Claim 6 (odds ratio).** For two independent trajectories, the probability of agreeing on the dominant theory versus agreeing on the runner-up is

$$
\frac{p_{1}^{2}}{p_{2}^{2}} = \left(\frac{p_{1}}{p_{2}}\right)^{2} = \left(\frac{0.40}{0.25}\right)^{2} = (1.6)^{2} = 2.56\,.
$$

Arithmetic: $0.40/0.25 = 1.6$; $1.6^{2} = 2.56$. So in the illustrative landscape, a coincidence on the dominant attractor is $2.56$ times as likely as a coincidence on the runner-up — the basin-volume ratio alone, squared, gives the odds ratio. This is the quantity a historical study would estimate: given a corpus of polygenesis episodes in a field, the observed frequency ratio of "same dominant theory" versus "same minority theory" events tests the measured basin hierarchy.

**Claim 7 (sensitivity of the prediction to the tail).** Because $P_{k}$ weights basins by $p_{i}^{k}$, higher-order polygenesis is exponentially insensitive to small basins. Compare the contribution of the two smallest basins to $P_{2}$ versus $P_{3}$:

$$
\frac{p_{4}^{2} + p_{5}^{2}}{P_{2}} = \frac{0.0100 + 0.0025}{0.2750} = \frac{0.0125}{0.2750} = 0.04545\ldots \approx 4.5\%\,,
$$
$$
\frac{p_{4}^{3} + p_{5}^{3}}{P_{3}} = \frac{0.001000 + 0.000125}{0.088750} = \frac{0.001125}{0.088750} = 0.012676\ldots \approx 1.3\%\,.
$$

Arithmetic: $0.0125/0.2750 = 0.045454\ldots$; $0.001125/0.088750 = 0.0126761\ldots$ So the niche attractors contribute $4.5\%$ of pairwise coincidences but only $1.3\%$ of triple coincidences: the more discoverers, the more the record concentrates on the dominant basin, and the less the prediction depends on accurately measuring small basins.

### 4.5 Structural consistency with the RG literature

The model's ingredients map onto the cited works as follows, with each mapping a check that the model does not contradict known RG phenomenology.

**Robustness of the fixed point's signature.** The cosmological-attractor result — that slow-roll parameters acquire beta-function dependence but $n_{s}$ and $r$ corrections "exactly cancel" to leading order in $1/N$ [2] — is the condition that the observable fingerprint of a fixed point is invariant under deformations of the flow. Without such invariance, two discoverers using different regularizations would extract different numbers from the same fixed point and polygenesis would not be observable as agreement. The cancellation mechanism of [2] is therefore the model's account of why agreement, when it happens, is exact rather than approximate.

**Multiple microscopies, one fixed point.** The strong-randomness review documents the random-singlet fixed point shared by the random Heisenberg chain and the closely related infinite-randomness fixed point of the transverse-field Ising chain, plus an infinite series of discretely distinct such fixed points [4]. In the model's terms, these are basins with macroscopic volumes: entire problem classes drain into them. The discretely distinct series of fixed points [4] corresponds to a landscape with several large basins, i.e., a less skewed $\{p_i\}$ and hence lower $P_{k}$ — a testable difference in polygenesis rates between problem classes with one dominant attractor and those with several comparable ones.

**Metric choice matters.** The scalar-curvature survey shows sequences of manifolds with positive scalar curvature that converge in the intrinsic-flat $\mathcal{VF}$ sense to a round sphere while having no Gromov-Hausdorff limit at all, because even a single thin well destroys GH convergence [1]. Transposed to theory space: with a metric that penalizes every formal difference (the GH analogue), independent derivations of the same theory would never register as convergent, and polygenesis would be invisible; with the observable-based relative-error metric of Section 3.1 (the $\mathcal{VF}$ analogue), they register as exactly convergent. The historical record of polygenesis is itself evidence that the effective metric of scientific comparison is observable-based, not notation-based.

**Hierarchical discretization.** The hierarchical-lattice RG for glasses provides the natural computational discretization: Dyson hierarchical lattices are trees on which Wilson's RG equations "emerge in a natural and simple way"