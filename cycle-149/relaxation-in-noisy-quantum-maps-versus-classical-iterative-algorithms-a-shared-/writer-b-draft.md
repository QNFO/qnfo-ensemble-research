# Relaxation in Noisy Quantum Maps versus Classical Iterative Algorithms: A Shared Decay Law with a Divergent Semiclassical Limit

## Abstract

Operators of hybrid classical-quantum compute facilities must decide, before any hardware is committed, whether a relaxation-type workload converges faster as a classical stationary iteration on a CPU cluster or as a repeatedly applied noisy quantum map on a quantum co-processor; no side-by-side convergence law with explicit arithmetic is available to guide that decision. This paper supplies one. Both processes are formulated as linear contractions toward a fixed point, yielding the shared step-count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$ for depolarizing strength $\varepsilon$, initial distance $D_0$, and tolerance $\delta$. Evaluated at $\varepsilon=0.01$, $D_0=1$, $\delta=10^{-6}$, both a qubit under depolarizing noise and a classical iteration with convergence factor $0.99$ need $1374.6$ steps ($1375$ integer steps); reducing $\varepsilon$ tenfold raises the count only to $13808.6$, a factor of $10.045$. A fidelity clock $F(t)=\frac{1}{2}(1+(1-\varepsilon)^t)$ converts any threshold $F_\ast>1/2$ into a step count, giving $2.011$ steps to $F_\ast=0.99$ at $\varepsilon=0.01$. The principal result is that at fixed $\varepsilon$ and finite $\hbar$ the two relaxations are step-count-indistinguishable; the only grounded locus of divergence is the joint $\hbar\to 0$, $\varepsilon\to 0$ limit, where relaxation time of quantized toral maps is sensitive to classical chaos. This redirects deployment decisions from speedup exponents to per-step costs and limit ordering, and yields a pre-registered falsification protocol.

## 1. Introduction

Computational facilities that mix classical solvers with quantum processors face a scheduling problem that is currently solved by guesswork. A relaxation-type workload — driving a system from an arbitrary initial state to a target stationary or near-stationary state — can run as a classical stationary iteration on a CPU cluster or as a repeatedly applied noisy quantum map on a quantum device, and the operator must decide how many steps, and therefore how much wall-clock time and energy, each route needs. If the two routes obey different relaxation laws, one route can be ruled out by scaling alone before any hardware is bought; if they obey the same finite-step law, the decision hinges on per-step cost and on limit-ordering questions instead. Today no such side-by-side law is available in explicitly comparable form, so procurement and scheduling decisions rest on unquantified intuitions about "quantum speedup".

The cost of this gap is concrete in both directions. A team that assumes a quadratic-type quantum advantage for a relaxation task, by analogy with phase and amplitude estimation where a quadratic speedup is known [4], may commit to hardware whose actual relaxation time scales no better than a classical iteration at the relevant noise level. A team that assumes equivalence may miss regimes, identified in the quantum-maps literature, where relaxation time depends on the chaotic character of an underlying classical system and therefore cannot be matched by any classical iteration with a fixed convergence factor [5]. A decision rule that separates the regime where the two processes coincide from the regime where they can differ would change what is computed before purchase, what is measured during commissioning, and what a claimed quantum advantage must demonstrate to be credited to quantumness rather than to unmatched parameters.

This paper answers the question: does relaxation in noisy quantum maps differ from relaxation in classical algorithms? The answer is constructed by placing both processes in the simplest common mathematical frame — linear contraction toward a fixed point — deriving the step-count law both obey at fixed noise strength, evaluating that law with full arithmetic, contrasting it with two relaxation laws from the literature that are genuinely different in form (a continuous-time level-to-level decay from a damped Madelung fluid model [8] and an algebraic coarsening law from a cellular-automaton emulation study [9]), and then identifying the one place, the joint semiclassical and weak-noise limit, where the quantum case is known to behave differently [5]. The falsification condition is stated in advance, following the pre-registered falsification methodology demonstrated for measurement-triggered relaxation claims [10], and the analysis extends a prior version of this comparison [11] by adding the cross-model law contrasts and a sharpened falsification protocol.

The contributions are:

- A unified contraction-frame derivation of the relaxation step-count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$, valid identically for a depolarizing qubit channel and for a classical stationary iteration with convergence factor $1-\varepsilon$, with explicit evaluation at $\varepsilon=0.01$, $\delta=10^{-6}$, $D_0=1$ giving $1374.6$ steps (Section 4.1).
- A crossover analysis showing the law is logarithmically insensitive to $\varepsilon$: reducing $\varepsilon$ by a factor of ten multiplies the step count by $10.045$, computed explicitly, against a factor of exactly $10$ for the algebraic law $\tau=1/\sqrt{ab\varepsilon}$ of the rule-110 emulation study (Section 4.2).
- A fidelity clock $F(t)=\frac{1}{2}(1+(1-\varepsilon)^t)$ with worked threshold crossings at $F_\ast=0.99$ for three noise strengths (Section 4.3).
- A limit-ordering argument, grounded in the relaxation-time results for quantized toral maps [5], that locates the only known quantum-classical divergence in the joint $\hbar\to 0$, $\varepsilon\to 0$ limit, together with a pre-registered falsification criterion modeled on the checksummed, tolerance-based protocol of [10] (Sections 4.4, 4.5 and 6).

## 2. Background and Related Work

The closest formal antecedent on the quantum side is the relaxation time introduced for noisy quantum maps on the $2d$-dimensional torus, which generalizes the earlier classical notion of dissipation time [5]. That work shows that relaxation time is sensitive to the chaotic behavior of the corresponding classical system when the semiclassical limit ($\hbar\to 0$) and the limit of small noise strength ($\varepsilon\to 0$) are considered simultaneously. Two features of this result drive the present analysis. First, relaxation time is a property of the map's approach to equilibrium, exactly the quantity a classical numerical analyst calls convergence time; the paper's own introduction frames it as the speed at which a conservative dynamical system subjected to noise converges to equilibrium, generalizing the dissipation-time studies in which density fluctuations decay during noisy evolution. Second, the sensitivity to chaos appears only in a joint limit, which means that at fixed $\hbar$ and fixed $\varepsilon$ no statement of difference is available from that result. The present paper supplies the fixed-$\varepsilon$ comparison that [5] deliberately does not address, and then uses the joint-limit sensitivity as the candidate locus of genuine divergence. The same source also fixes useful asymptotic conventions: $a(\epsilon)\ll b(\epsilon)$ iff $a(\epsilon)/b(\epsilon)\to 0$, $a(\epsilon)\sim b(\epsilon)$ iff the ratio is bounded above and below by positive constants, and $a(\epsilon)\approx b(\epsilon)$ iff the ratio tends to $1$; these conventions are adopted in Section 4.4.

On the classical side, the parallel Jacobi family of one-sided trigonometric and hyperbolic Jacobi-type algorithms for Hermitian eigenvalue problems is the named representative of the class of stationary iterations whose convergence factor is treated here as a free parameter. The prior version of this analysis used exactly this role for the Jacobi family and noted that its convergence quality is instance-dependent in ways a single-$\rho$ model hides [11]. The present paper keeps that role: the derivation of Section 4.1 is a comparison of structural laws, not of specific implementations.

The quantum speedup question is bounded by known results on phase and amplitude estimation, which admit a quadratic quantum speedup [4]. The same work records that Wang, Higgott and Brierley showed there is a continuous trade-off between quantum speedup and circuit depth through a family of algorithms known as $\alpha$-QPE, and derives the scaling of $\alpha$-QPE within the Quantum Singular Value Transformation (QSVT) framework. Its discussion makes the trade-off explicit: approximating the step function up to error $\eta/2$ outside $[-\delta,\delta]$ relates the parameters as $\eta+\frac{1}{2}\delta^{\alpha}=1$, so that $\alpha$ parametrizes how lower-degree polynomials (lower circuit depths) are compensated by running the circuits more times. This matters here because it shows that even for the best-understood quantum speedups the advantage is a trade-off curve, not a step-count constant; a relaxation comparison that reports only asymptotic exponents would overstate the practical difference. The present analysis keeps the comparison at the level of explicit step counts at fixed parameters.

A different relaxation law from the quantum-foundations side comes from the hydrodynamic research program in which quantum jumps are reinterpreted as continuous, deterministic relaxation events in a damped Madelung fluid [8]. That work adds a linear drag term $-m\gamma\mathbf{v}$ to the Madelung momentum equation, shows eigenstate densities remain exact fixed points of the damped flow, and derives closed-form level-to-level relaxation times $t_{n\to n-1}=\ln[(n+\tfrac{1}{2})/(n-\tfrac{1}{2})]/(2\gamma)$, giving $t_{1\to 0}=0.549306/\gamma$ and $t_{2\to 1}=0.255413/\gamma$, with energy decay $E(t)=E_0\,e^{-2\gamma t}$ under orbit averaging. Its own discussion flags that the Lyapunov argument establishes attractivity of the fixed-point set, not global convergence to a unique eigenstate, and that degenerate spectra, limit cycles, or chaotic attractors could prevent convergence to a single outcome. This is directly relevant: it is a second exponential relaxation law, in continuous time and with mode-dependent rates, and its stated failure modes (persistent oscillations when perturbations inject energy faster than dissipation removes it) mark exactly the conditions under which a single-contraction-factor frame fails. Section 4.2 uses its $t_{1\to 0}=0.549306/\gamma$ as the continuous-time counterpart of the discrete step-count law.

A third, algebraic relaxation law comes from the study of emergent universality in cellular automata, in which the Turing-complete, chiral elementary cellular automaton rule 110 is emulated by three individually mirror-symmetric and individually trivial rules — rules 36, 37, and 5 — arranged in a fixed period-3 spatial schedule [9]. That work models the desynchronization boundaries between phase domains as point particles with density $\rho(t)$ that annihilate on contact, with noise of strength $\varepsilon$ creating new walls at rate $a\,\varepsilon$ per site per step. Its derived results include the steady-state scaling $\rho^{*}=\sqrt{a\varepsilon/b}$, the relaxation time $\tau=1/\sqrt{ab\varepsilon}$ (giving $\tau=10$ steps at $\varepsilon=10^{-2}$ and $\tau=100$ steps at $\varepsilon=10^{-4}$ for $a=b=1$), and the transient law $\rho(t)=\rho_0/(1+b\rho_0 t)$ at zero noise, showing algebraic coarsening. Its discussion concedes that one-dimensional coarsening can admit logarithmic corrections to mean-field exponents and that the prefactor $\sqrt{a/b}$ has not been measured. Section 4.2 uses this law as the contrast case: an algebraic relaxation whose parameter sensitivity differs qualitatively from the exponential contraction law derived here.

The methodology of stating a falsification condition in advance is taken from the pre-registered falsification of deterministic measurement-triggered relaxation [10]. That work tested whether deterministic relaxation toward eigenstate basins can reproduce Born probabilities of a two-level system: all seven configurations produced the verdict FAIL, with a maximum deviation of $0.5$ against a pre-registered tolerance of $10^{-2}$, because a deterministic map from a fixed initial state yields a degenerate outcome channel taking only the values $0$ or $1$. Its practitioner section packages the protocol as reusable: fixed Hamiltonian, sealed test set, pre-registered tolerance, checksummed code, threshold terminal rule, so that a claim can be re-verified in minutes without trusting the authors. Section 3.5 and Section 6 adopt this template for the present central claim.

The prior version of this comparison [11] established the shared step-count law and its evaluation ($1374.6$ steps at $\varepsilon=0.01$, $\delta=10^{-6}$; a factor of $10.045$ for a tenfold noise reduction; a fidelity-threshold crossing analysis), and located the divergence locus in the joint semiclassical and weak-noise limit. The present paper re-derives those results with the arithmetic shown, replaces the prior paper's imported external fidelity threshold — which is not available in the current source set — with a generic threshold analysis at $F_\ast=0.99$, and adds the cross-model law contrasts against [8] and [9] that sharpen what "different relaxation" would even mean.

Three further works shape the engineering framing. The distributed maximum-clique work defines the target figure of merit as the costup — an increase in performance greater than the increase in cost, be it measured in money or energy — and achieves it by a simple modification of a state-of-the-art exact algorithm distributed over an ad-hoc cluster of over 100 teaching machines accessible only through SSH, NFS and Java [1]. Its conclusion reports concrete numbers: instances that take weeks on a single machine solved in under 4 to 11 hours on the cluster, with less than a week of development effort, e.g. frb35-17-2 in under 7 hours against over 13 days on a single machine. The costup is adopted here as the gate any quantum-relaxation deployment must pass: a route wins only if its step-count advantage survives the development effort of realizing it.

The submodular maximization literature supplies the per-step-cost lesson. Maximizing a non-negative monotone submodular function under a cardinality constraint admits polynomial-time approximation algorithms, yet solving it in practice often involves frequently querying the submodular function, so query cost dominates runtime [2]. The same work's algorithms achieve adaptive complexities independent of $n$ — the main algorithm LS+GS has adaptive complexity dependent on parameters $p$ and $k$, with query complexity $O((\frac{1}{\varepsilon k}+1)\frac{n}{\varepsilon^{3}})$ for its LALS subroutine — demonstrating that the resource that binds in practice (queries, i.e. per-step evaluations) is distinct from the iteration count. The analogue for relaxation is that per-step cost, not step count alone, determines wall-clock time; Section 4.5 formalizes this as a parity condition.

The TSP-with-neighborhoods work illustrates how far structural results transfer across instance classes. TSPN, a generalization of the Euclidean TSP in which the salesman must visit connected regions rather than points, is NP-hard; for disjoint unit disks a constant-factor approximation exists with tour length $|T|\leq((1+\frac{8}{\pi})|T^{*}|+8)(1+\epsilon)$, and a PTAS exists for equal-size disjoint disks, but a recent APX-hardness result rules out a PTAS for the general case [3]. Its conclusion lists as open whether a constant-factor approximation exists for arbitrary connected regions in the plane. By analogy, relaxation-time results for structured maps (tori, as in [5]) need not transfer to unstructured instances; Section 6 carries this as a limitation.

Finally, two algorithmic existence results are reminders that existence of a quantity does not imply availability of an efficient procedure to control it. The consensus-tree work constructs the majority rule (+) consensus tree in $O(kn)$ time, which is optimal because the input size is $\Omega(kn)$, and the frequency-difference consensus tree in $\min\{O(kn^{2}),\,O(kn(k+\log^{2}n))\}$ time, fully deterministically and without hashing [6]. The odd-gracefulness work states that in spite of the large number of papers published on graph labeling, there are few algorithms researchers can actually use to gracefully label graphs, and provides generalized odd graceful solutions for a specific graph construction [7]. Both patterns recur here: a relaxation time can be defined for a broad class of systems, as [5] does, while the efficient computation or control of that quantity — the thing an operator actually needs — is the missing piece this paper addresses at the level of explicit laws.

## 3. Methods

### 3.1 Common contraction frame

Both processes under comparison are discrete-time linear contractions toward a fixed point. Let $x_t$ be the state after $t$ steps, $x_\ast$ the fixed point, and suppose

$$\|x_{t+1}-x_\ast\| \le \rho\,\|x_t-x_\ast\|,$$

with contraction factor $0\le\rho<1$. Iterating gives

$$\|x_t-x_\ast\| \le \rho^{\,t}\,\|x_0-x_\ast\|.$$

Define the initial distance $D_0=\|x_0-x_\ast\|$ and a tolerance $\delta$ with $0<\delta<D_0$. The step count $t_\delta$ at which the distance first falls to $\delta$ satisfies $\rho^{\,t_\delta}D_0=\delta$, hence

$$t_\delta=\frac{\ln(\delta/D_0)}{\ln\rho}.$$

This frame is method-level and parameter-level only. It assumes linearity of the contraction, time-independence of $\rho$, and a norm in which the contraction inequality holds. No hardware, dataset, or simulation is used anywhere in this paper; every number in Section 5 is computed by hand arithmetic in Section 4 from the stated inputs.

### 3.2 Quantum instantiation: depolarizing noise on a qubit

For a single qubit undergoing a depolarizing channel of strength $\varepsilon$ per step, the state updates as

$$\rho_{t+1}=(1-\varepsilon)\,\rho_t+\varepsilon\,\frac{\mathbb{I}}{2},$$

so that after $t$ steps

$$\rho_t=(1-\varepsilon)^t\rho_0+\bigl(1-(1-\varepsilon)^t\bigr)\frac{\mathbb{I}}{2}.$$

The maximally mixed state $\mathbb{I}/2$ is the fixed point, and the trace distance from the fixed point contracts as

$$D\bigl(\rho_t,\mathbb{I}/2\bigr)=(1-\varepsilon)^t\,D\bigl(\rho_0,\mathbb{I}/2\bigr),$$

which is the contraction frame with $\rho=1-\varepsilon$. The identification of the depolarizing channel as a convex mixture with the maximally mixed state is the standard definition of that channel; no empirical claim is involved.

### 3.3 Classical instantiation: stationary iteration

For a classical stationary iteration $x_{t+1}=Mx_t+c$ with iteration matrix $M$ of spectral radius $\rho(M)<1$, the error propagates as $e_{t+1}=Me_t$, giving $\|e_t\|\le\rho(M)^t\|e_0\|$. Setting $\rho(M)=1-\varepsilon$ makes the classical and quantum instantiations share the identical step-count law with identical parameters. This identification is a modeling choice, and its consequence — that at fixed $\varepsilon$ the two processes are step-count-indistinguishable — is a theorem of the frame, not an empirical observation.

### 3.4 Fidelity clock

For the qubit channel of Section 3.2, the fidelity between $\rho_t$ and the pure initial state $\rho_0=|\psi\rangle\langle\psi|$ is

$$F(t)=\langle\psi|\rho_t|\psi\rangle=(1-\varepsilon)^t+\bigl(1-(1-\varepsilon)^t\bigr)\frac{1}{2}=\frac{1+(1-\varepsilon)^t}{2}.$$

This converts any fidelity threshold $F_\ast$ into a step count $t_\ast$ via $(1-\varepsilon)^t=2F_\ast-1$, i.e.

$$t_\ast=\frac{\ln(2F_\ast-1)}{\ln(1-\varepsilon)},$$

valid when $F_\ast>1/2$. Section 4.3 evaluates this clock at the representative threshold $F_\ast=0.99$ for three noise strengths. No external fidelity threshold is imported in this version: the prior version's imported threshold [11] is not available in the current source set, and the generic threshold analysis preserves the demonstrative content without borrowing an unsupported number.

### 3.5 Falsification protocol

Following the pre-registration pattern of [10] — fixed test set, pre-registered tolerance, checksummed code, and a verdict rule fixed before the run — the observation that would falsify the paper's central claim is stated in advance. The central claim is: at fixed $\varepsilon$ and fixed finite $\hbar$, quantum and classical relaxation obey the same step-count law. The pre-registered falsifier is any rigorously derived or empirically measured pair $(t_\delta^{\mathrm{Q}},t_\delta^{\mathrm{C}})$ at the same $\varepsilon$, $\delta$, and $D_0$ whose ratio differs from $1$ by more than a pre-registered tolerance, set here at $10^{-2}$ relative, matching the tolerance discipline of [10]. Section 6 develops what such a pair would require.

## 4. Analysis

### 4.1 Baseline step count at $\varepsilon=0.01$, $\delta=10^{-6}$

Inputs: $\varepsilon=0.01$ (chosen as a representative per-step noise strength; the scaling is derived in Section 4.2), $D_0=1$ (worst case: a pure state maximally far from the maximally mixed state in trace distance), $\delta=10^{-6}$ (a tolerance at which residual coherence is negligible for most protocol purposes).

Step 1: contraction factor $\rho=1-\varepsilon=0.99$.

Step 2: $\ln(\delta/D_0)=\ln(10^{-6})=-6\ln 10=-6\times 2.302585=-13.815510$.

Step 3: $\ln\rho=\ln(0.99)$. Expanding $\ln(1-x)=-x-x^2/2-x^3/3-\cdots$ with $x=0.01$:

$$\ln(0.99)=-0.01-0.00005-0.000000333-0.0000000025=-0.010050336.$$

Step 4:

$$t_\delta=\frac{-13.815510}{-0.010050336}=1374.6.$$

Check: $1374.6\times 0.010050336=13.8155$, matching the numerator. So both the depolarizing qubit and the classical iteration with $\rho=0.99$ need $1374.6$ steps, i.e. $1375$ integer steps, to reach $\delta=10^{-6}$.

### 4.2 Logarithmic insensitivity to $\varepsilon$, and contrast with two other relaxation laws

Reduce the noise strength to $\varepsilon=0.001$, so $\rho=0.999$. Then

$$\ln(0.999)=-0.001-0.0000005-0.000000000333=-0.001000500.$$

The step count is

$$t_\delta=\frac{13.815510}{0.001000500}=13808.6.$$

The ratio to the $\varepsilon=0.01$ case is

$$\frac{13808.6}{1374.6}=10.045.$$

A tenfold reduction in noise strength multiplies the relaxation step count by $10.045$, not by $10$: the step count scales as $1/\varepsilon$ up to a logarithmic correction of relative size $\varepsilon/2$ from the $x^2/2$ term in $\ln(1-x)$. Explicitly, $t_\delta\approx\frac{\ln(\delta/D_0)}{-\varepsilon-\varepsilon^2/2}$, so $t_\delta\cdot\varepsilon\approx\ln(\delta/D_0)\cdot\frac{1}{1+\varepsilon/2}$; at $\varepsilon=0.01$ the correction factor is $\frac{1}{1.005}=0.99502$, i.e. a $0.498\%$ reduction relative to the pure $1/\varepsilon$ law. This is the quantitative sense in which the relaxation clock is logarithmically insensitive to its parameters: only $\ln(\delta/D_0)$ and $1/\varepsilon$ matter, and the former changes by $2.302585$ per decade of tolerance.

Two relaxation laws from the literature have different parameter sensitivity, which shows what a genuine law-level difference would look like. First, the continuous-time level-to-level law of the damped Madelung program [8], $t_{n\to n-1}=\ln[(n+\tfrac{1}{2})/(n-\tfrac{1}{2})]/(2\gamma)$, gives $t_{1\to 0}=0.549306/\gamma$: the relaxation time depends on the damping rate $\gamma$ and on the level index $n$, not on a tolerance $\delta$, and its mode dependence ($t_{2\to 1}=0.255413/\gamma$, decreasing in $n$) has no counterpart in the single-$\rho$ frame. Second, the algebraic law of the rule-110 emulation study [9], $\tau=1/\sqrt{ab\varepsilon}$, gives $\tau=10$ steps at $\varepsilon=10^{-2}$ and $\tau=100$ steps at $\varepsilon=10^{-4}$ for $a=b=1$: a tenfold reduction in $\varepsilon$ multiplies $\tau$ by exactly $10$, and the transient $\rho(t)=\rho_0/(1+b\rho_0 t)$ decays algebraically, not exponentially. The contraction law derived here sits between these: like the algebraic law it is controlled by a single noise parameter, but like the Madelung law it is exponential, and its decade-per-tolerance cost of $2.302585/0.010050336=229.1$ steps (at $\varepsilon=0.01$) has no analogue in either. A claimed quantum-classical relaxation difference must therefore specify which law class is alleged before any step count can be compared.

### 4.3 Fidelity clock at $F_\ast=0.99$

Input: $F_\ast=0.99$, chosen as a representative high-fidelity threshold; the method accepts any $F_\ast>1/2$.

Step 1: $2F_\ast-1=2\times 0.99-1=0.98$.

Step 2: $\ln(0.98)$. Expanding $\ln(1-x)$ with $x=0.02$:

$$\ln(0.98)=-0.02-0.0002-0.000002667-0.00000000004=-0.020203.$$

Step 3: at $\varepsilon=0.01$,

$$t_\ast=\frac{-0.020203}{-0.010050336}=2.011.$$

So a pure qubit state's fidelity with its initial state falls below $0.99$ after $2.011$ steps, i.e. during the third step, at $\varepsilon=0.01$. At $\varepsilon=0.1$ ($\rho=0.9$, $\ln 0.9=-0.105361$):

$$t_\ast=\frac{-0.020203}{-0.105361}=0.192,$$

i.e. the threshold is crossed within the first step. At