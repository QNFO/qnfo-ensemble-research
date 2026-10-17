# Attractor Calculus: A Formal Operator Language for Steering Cognition Across Substrates

## Abstract

Prompt engineering, neural stimulation, and cognitive intervention all face the same underlying problem: steering an information-processing system into a desired dynamical state, with no principled language for saying what "steering" means or what it should cost. Practitioners in each domain currently work system-by-system, with no way to state whether a control primitive discovered in one substrate transfers to another. This paper formalizes that gap. We define an Attractor Calculus: a small operator set (CREATE_ATTRACTOR, DEEPEN_BASIN, SHIFT_BOUNDARY, PERTURB, HOLD) over attractor-based dynamical systems, together with a cost functional and a composition algebra. We derive closed-form minimal-energy costs for basin transitions in a canonical bistable potential $V(x)=x^{4}/4-x^{2}/2$: an impulse crossing costs $E_{\mathrm{imp}}=2\Delta V=0.5$, a constant-tilt crossing costs at the rate $u_{c}^{2}=4/27\approx0.148148$ per unit time, and the break-even horizon between the two strategies is $T^{*}=27/8=3.375$. Under noise intensity $D=0.05$ and a dwell-time reliability requirement of failure probability $\leq10^{-3}$ over $T_{d}=10^{6}$ time units, DEEPEN_BASIN must add $\delta d\approx0.786138$ of barrier depth, raising impulse cost by $2\delta d\approx1.572277$. We prove a partial universality result: impulse-operator cost depends only on the invariant barrier height $\Delta V$, while tilt-operator cost depends on substrate geometry, so the operator set splits into portable and substrate-specific classes. This gives practitioners a testable criterion for which control levers should transfer across substrates and which must be re-derived per system.

## 1. Introduction

Anyone who deploys large language models, designs brain-stimulation protocols, or runs behavioral interventions faces the same operational problem: a target system sits in some dynamical regime, the desired behavior corresponds to a different regime, and the practitioner must find an input sequence that moves the system between the two reliably and cheaply. Today this is done by hand. Prompt engineers iterate on wording until outputs improve, with no vocabulary for stating what a prompt did to the model's internal state or why a fix that worked on one model fails on another. Neuromodulation and neurofeedback protocols are tuned per patient and per device. Behavioral interventions are designed case by case. In each domain the absence of a common control language blocks three concrete capabilities: predicting the cost of a steering maneuver before attempting it, reusing a control primitive discovered in one system inside another, and auditing whether a stimulus sequence is doing semantic work or merely pushing latent state.

The research idea this paper develops conjectures that information-processing systems, whether large language models or brains, are attractor-based dynamical systems, and that a formal operator calculus over attractor basins could compile high-level cognitive goals into minimal-energy stimulus sequences. If the conjecture holds, a control primitive validated in a toy recurrent network should transfer, with predictable cost rescaling, to a transformer or a neural circuit, and the question "is there a substrate-independent machine code of cognition?" becomes an empirical program rather than a slogan. If it fails, the failure itself is informative: it would show that steering levers are irreducibly substrate-specific and that cross-substrate transfer claims in prompting and neurostimulation should be treated with suspicion.

This paper does not settle the conjecture empirically. It builds the formal layer that makes the conjecture testable, and it derives the first closed-form results that the formal layer predicts. The contributions are:

- A definition of the Attractor Calculus: a state-space semantics, five operators (CREATE_ATTRACTOR, DEEPEN_BASIN, SHIFT_BOUNDARY, PERTURB, HOLD), a quadratic cost functional, and a composition algebra with an additivity theorem (Section 3).
- Closed-form minimal-energy derivations for basin transition in a canonical bistable potential: impulse cost $E_{\mathrm{imp}}=2\Delta V$, tilt cost rate $u_{c}^{2}=4/27$, break-even horizon $T^{*}=27/8$, and their generalization to the family $V(x)=x^{4}/4-ax^{2}/2$ giving $T^{*}(a)=27/(8a)$ (Section 4).
- A noise-robustness derivation: under noise intensity $D$ and a failure-probability requirement $\varepsilon$ over dwell time $T_{d}$, the required basin depth is $\Delta V'\geq D\ln\!\bigl(T_{d}/(-\ln(1-\varepsilon))\bigr)$, with the numerical consequence $\delta d\approx0.786138$ for the assumed operating point (Section 4).
- A universality criterion and a partial classification of the operator set: PERTURB cost is a function of the invariant $\Delta V$ alone and is therefore portable across substrates in the defined sense, while SHIFT_BOUNDARY cost depends on local barrier geometry and is substrate-specific (Sections 4 and 5).
- An engineering pathway: the smallest experiment that would de-risk or falsify the calculus on a real trained network, the readiness level of the current work, and the binding constraints (Section 7).

## 2. Background and Related Work

The calculus proposed here sits at the intersection of three literatures: dynamical systems theory applied across substrates, formal language methods applied to learned systems, and the engineering of formal specification languages. Each supplies a specific tool or a specific caution.

On the dynamical side, the strongest precedent for substrate-independent control motifs is the recent treatment of habituation. [2] frames habituation not as a biological phenomenon but as a problem of designing a dynamical system: given qualitative constraints on transient response, identify the minimal dynamical ingredients that meet them, using a behavioral (Willems-style) formulation in which a system is defined by the set of admissible input-output trajectories $\mathcal{B}$ rather than by state-space equations. Two of its results carry directly into our setting. First, habituation has been observed not only in animals but in unicellular organisms and in non-living devices such as electronic circuits and neuromorphic materials, which is empirical evidence that a learned dynamical motif can recur across substrates with no shared biology. Second, the review proves that nonnegative, bounded habituation rules out linearity, making nonlinearity structural rather than optional, and that a single fading-memory state with a static nonlinear readout already captures the core hallmarks. Our universality criterion (Section 4) is the steering-side analogue of their synthesis question: which control operators have costs determined by structural invariants rather than by substrate detail.

Formal language theory has repeatedly been used to describe the behavior of learned neural systems, and each use exposes both the power and the limits of the approach. [3] surveys the connection from Chomsky's hierarchy to modern NLP and records a caution that directly constrains our claims: constructions in which recurrent networks encode large computations exploit arbitrary numerical precision, such encodings are highly sensitive to slight perturbations of network parameters, and they correspond to steep valleys in parameter space that gradient-based optimization is unlikely to find. Any attractor calculus that assumes clean, well-separated basins in a trained network must therefore state how it behaves when basins are shallow or ill-conditioned; we address this in Section 6. [8] provides the closest methodological precedent on the descriptive side: the LEXR framework explains the decision-making of recurrent neural networks using Linear Temporal Logic, generates model-agnostic post-hoc local explanations inside a user-defined region of interest, carries a PAC-style guarantee on explanation accuracy, and empirically produces explanations that are often smaller and easier to interpret than DFA-based extractions from RNN acceptors. LEXR shows that a formal language can be fitted to a trained recurrent system after the fact; our calculus asks the inverse question, namely which formal operators can be fitted before the fact as control commands. [11] quantifies what formal structure buys when used as an inductive bias during control: imposing formal-language constraints on Markov decision processes, combined with PPO and Lagrangian enforcement in Safety Gym, reduced the accumulated cost rate often by between almost one half and an order of magnitude, at the price of decreased performance in the earliest training steps while the constraint embedding was learned. That measured trade, formal structure purchased for a concrete cost reduction, is the pattern of benefit our calculus predicts for steering, and their observation that early training degrades before improving warns that operator-based steering may carry a transient cost of its own.

The engineering of formal specification languages supplies the second pillar: evidence that a small, well-chosen operator or component vocabulary can carry the weight of an entire specification practice. [5] describes the CBS framework, in which programming-language semantics are specified by translating programs to reusable constructs called funcons, whose semantics are defined once and for all in a modular variant of structural operational semantics; the framework exists precisely because scaling up full-language formal semantics by hand is usually regarded as a huge effort not worth undertaking. Our operator set is designed with the same reuse goal: each operator's cost theorem should be proved once and instantiated per substrate. [9] demonstrates the maturity such an approach can reach: Wasm SpecTec generates a formal specification, prose pseudocode, and mechanized definitions from a single source of truth written in a domain-specific language, and the extracted Wasm semantics passes all 23,778 applicable tests in the official Wasm test suite. SpecTec's stated success criterion, adoption by industrial stakeholders so that the normative definition is written in the DSL, is the adoption model we propose for an attractor-calculus standard in Section 7. On the mathematical side, [4] shows that a lightweight $\lambda$-calculus-style syntax (the $\mu$-syntax) can represent an entire algebraic structure, the cyclic operad, compactly enough to give a complete step-by-step proof of the equivalence between its biased and unbiased definitions; this is a precedent for our claim that a small operator syntax can support nontrivial equivalence and cost proofs rather than merely serving as notation. [10] contributes an inheritance theorem of the shape we seek: a language-convexity criterion under which regularity of a language representation passes from a group to its finite-index subgroups, yielding Theorem 1.1, that a finitely generated group with a regular positive cone passes regularity to finite-index subgroups. The pattern, a criterion under which a property survives a change of substrate (group to subgroup), is exactly the logical form of our portability question (system to system). [7] illustrates how much structure a language class alone can carry: defining $L_{n}=\{w\in\Sigma^{*}:\xi(w)\text{ is divisible by }n\}$ with $\xi(w)=|w|_{a}-|w|_{b}$, the languages $L_{n}$ are regular, and their union over primes equals $\{w:\xi(w)\neq\pm1\}$, from which the infinitude of primes follows; we use the same discipline of deriving system-level facts from the closure properties of an operator language. [6] shows the graded expressiveness that formal automata families provide, with iterated pushdown automata sitting strictly between pushdown automata and Turing machines, and gives the Fibonacci language $a^{f_{n}}$ as a concrete 2-iterated-pushdown example; this graded hierarchy is a reminder that our operator set should be classified by expressive power, not assumed maximal. Finally, [1] constructs reflectica, a formal language that is its own meta-language, in which every object, including expressions and their values, is a finite string with a canonical name; a calculus of steering that is intended to describe systems which themselves process the calculus' tokens (such as language models prompted in the calculus' own notation) will eventually need exactly this self-referential capacity, and we flag it as future work rather than claiming it here.

Two adjacent speculative frameworks round out the context. [13] builds a formal system from a single primitive, the act of drawing a boundary, with a void acting as an identity element under juxtaposition; this is a philosophical antecedent for founding a calculus on operator primitives rather than on physical state variables, though it makes no contact with control or cost. [14] proposes that cognitive state spaces are ultrametric, modeling the brain as a cocycle solver on a Bruhat-Tits tree and reporting that simulated neural replicas reject the Euclidean baseline with $p<0.001$ and exhibit power-law retrieval times consistent with p-adic diffusion; if cognitive basins are organized ultrametrically rather than Euclideanally, the geometry in which our operators are instantiated changes, and we treat this as an open question in Section 6. [12], in a different domain, articulates the methodological problem our conjecture also faces: frameworks that challenge a field's governing axiom (there, Measurement Independence; here, substrate-specificity of control) are often expelled rather than comparatively assessed, and a research programme needs explicit criteria by which its central conjecture could be accepted or rejected. Section 6 supplies such criteria for the attractor conjecture.

## 3. Methods

### 3.1 State-space semantics

We assume every information-processing system is modeled as a controlled dynamical system

$$
\dot{x}=f(x,u)+\sigma\xi(t),\qquad x\in\mathbb{R}^{n},
$$

where $x$ is the internal state, $u\in\mathcal{U}$ is the control signal (a prompt, a stimulus, a stimulation current), $\sigma\xi(t)$ is additive noise of intensity $D=\sigma^{2}/2$, and the uncontrolled flow $f(x,0)$ possesses a set of attracting equilibria or attracting sets $\{A_{i}\}$, the attractors. The basin $B_{i}$ of $A_{i}$ is the set of initial conditions whose trajectories converge to $A_{i}$. For the analytical results of this paper we work in one dimension with a bistable gradient system

$$
\dot{x}=-V'(x)+u,\qquad V(x)=\frac{x^{4}}{4}-\frac{x^{2}}{2},
$$

which has stable equilibria at $x=\pm1$ with $V(\pm1)=-1/4$ and a saddle at $x=0$ with $V(0)=0$. This potential is the canonical minimal model of two competing attractor basins separated by a barrier; every derivation in Section 4 states its inputs explicitly, and all of them are model choices or labeled assumptions, not measurements.

### 3.2 Cost functional

The cost of a control signal $u:[0,T]\to\mathcal{U}$ is the quadratic energy

$$
E[u]=\int_{0}^{T}\lVert u(t)\rVert^{2}\,dt.
$$

For an impulse $u(t)=p\,\delta(t)$, this gives $E[u]=p^{2}$. The quadratic functional is chosen because it is the standard minimal-energy criterion in control theory and because it makes the composition algebra in Section 3.4 additive; we examine the sensitivity of the results to this choice in Section 6.

### 3.3 Operator set

The calculus consists of five operators, each mapping a system state and a goal to a control signal:

- $\texttt{PERTURB}(A_{i}\to A_{j})$: deliver a minimal impulse that moves the state from basin $B_{i}$ across the separatrix into $B_{j}$.
- $\texttt{HOLD}(A_{j},T_{d})$: maintain the state inside $B_{j}$ for a dwell time $T_{d}$ against noise, typically by a sustaining input or by prior basin deepening.
- $\texttt{DEEPEN\_BASIN}(A_{j},\delta d)$: modify the system (or apply a sustained background input) so that the effective barrier protecting $A_{j}$ increases by $\delta d$.
- $\texttt{SHIFT\_BOUNDARY}(A_{i}\to A_{j})$: apply a sustained input that tilts the landscape until the separatrix moves and the state falls into $B_{j}$ without an impulse.
- $\texttt{CREATE\_ATTRACTOR}(A_{\mathrm{new}})$: introduce a parameter change that produces a new attracting equilibrium where none existed.

For this paper, CREATE_ATTRACTOR is defined but not costed: its minimal cost depends on global bifurcation structure that the one-dimensional model does not exhibit, and we state it as an open problem.

### 3.4 Composition algebra

Operators compose sequentially. If $u_{1}$ is supported on $[0,T_{1}]$ and $u_{2}$ on $[T_{1},T_{1}+T_{2}]$, then

$$
E[u_{1}\cdot u_{2}]=\int_{0}^{T_{1}}\lVert u_{1}\rVert^{2}dt+\int_{T_{1}}^{T_{1}+T_{2}}\lVert u_{2}\rVert^{2}dt=E[u_{1}]+E[u_{2}],
$$

so the cost functional is additive over sequential composition with disjoint time supports. This additivity is the algebraic backbone of the calculus: it lets a compiled steering program be costed by summing its operators' costs, exactly as a funcon-term program in [5] is given semantics by the once-and-for-all semantics of its components.

### 3.5 Universality criterion

We define an operator's cost function $c_{\mathrm{op}}$ to be portable across a class of substrates if $c_{\mathrm{op}}$ is a function only of invariant quantities of the attractor landscape, such as the barrier height $\Delta V$, the noise intensity $D$, and basin volumes, and not of substrate-specific quantities such as the local curvature profile of the barrier or the parameterization of the control channel. This criterion is deliberately analogous to the inheritance criterion of [10]: language-convexity there, cost-invariance here, both asking when a property survives a change of carrier.

## 4. Analysis

Every input number in this section is either a property of the model potential defined in Section 3.1 (a stated model choice) or an explicitly labeled assumption. All arithmetic is shown.

### 4.1 Barrier height of the canonical potential

With $V(x)=x^{4}/4-x^{2}/2$: the stationary points satisfy $V'(x)=x^{3}-x=0$, giving $x\in\{-1,0,1\}$. The minima are at $x=\pm1$:

$$
V(\pm1)=\frac{1}{4}-\frac{1}{2}=-\frac{1}{4},
$$

and the saddle at $x=0$ has $V(0)=0$. The barrier height separating the two basins is therefore

