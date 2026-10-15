# Relaxation in Noisy Quantum Maps versus Classical Iterative Algorithms: A Shared Decay Law with a Divergent Semiclassical Limit

## Abstract

Iterative numerical algorithms and noisy quantum dynamics both converge to a stationary state by exponential damping, and practitioners who port workloads between classical solvers and quantum co‑processors need to know whether the two relaxation processes obey the same or different timing laws. The specific gap addressed here is that relaxation time has been formalized for noisy quantum maps on tori, where it was shown to be sensitive to classical chaos in a joint semiclassical and weak‑noise limit, while the corresponding convergence‑time laws of classical stationary iterations are usually analyzed separately, so no side‑by‑side scaling comparison with explicit arithmetic exists. We formulate both processes as linear contractions toward a fixed point, derive a common step‑count law  
$$t_\delta=\frac{\ln(\delta/D_0)}{\ln(1-\varepsilon)}$$  
for depolarizing strength $\varepsilon$ and tolerance $\delta$, and evaluate it explicitly: at $\varepsilon=0.01$ and $\delta=10^{-6}$ both a qubit under depolarizing noise and a classical stationary iteration with convergence factor $0.99$ need $1374.6$ steps. We further derive that a logical‑fidelity marker $F_\ast=0.874$ (imported from an external no‑go result) is crossed after $28.9$ steps at $\varepsilon=0.01$. The principal result is that the finite‑$\varepsilon$ relaxation law does not distinguish quantum from classical relaxation; any operational difference must enter through the joint $\hbar\to0$, $\varepsilon\to0$ limit. This redirects engineering attention from per‑step decay rates to limit‑ordering questions and yields a concrete falsification protocol.

## 1. Introduction

Hybrid compute facilities that combine classical solvers with quantum processors face a scheduling problem that is currently solved by guesswork. A relaxation‑type workload—driving a system from an arbitrary initial state to a target stationary or near‑stationary state—can run as a classical stationary iteration on a CPU cluster or as a repeatedly applied noisy quantum map on a quantum device, and the operator must decide how many steps, and therefore how much wall‑clock time and energy, each route needs. If the two routes obey different relaxation laws, one route can be ruled out by scaling alone before any hardware is bought; if they obey the same finite‑step law, the decision hinges on quantities such as noise strength and limit ordering instead. Today no side‑by‑side law is available in the literature in explicitly comparable form, so procurement and scheduling decisions rest on unquantified intuitions about “quantum speedup”.

The cost of this gap is concrete. A team that assumes a quadratic‑type quantum advantage for a relaxation task, by analogy with phase and amplitude estimation where a quadratic speedup is known, may commit to hardware whose actual relaxation time scales no better than a classical iteration at the relevant noise level. Conversely, a team that assumes equivalence may miss regimes, identified in the quantum‑maps literature, where relaxation time depends on the chaotic character of an underlying classical system and therefore cannot be matched by any classical iteration with a fixed convergence factor.

This paper answers the question: does relaxation in noisy quantum maps differ from relaxation in classical algorithms? We answer it by constructing the simplest common mathematical frame—linear contraction toward a fixed point—deriving the step‑count law both processes obey at fixed noise, evaluating that law with full arithmetic, and then identifying the one place, the joint semiclassical and weak‑noise limit, where the quantum case is known to behave differently. We also connect the relaxation clock to an independently published fidelity marker, and we state a pre‑registered falsification condition in the style of prior pre‑registered falsification work on measurement‑triggered relaxation.

**Contributions**

- A unified contraction‑frame derivation of the relaxation step‑count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$, valid identically for a depolarizing qubit channel and for a classical stationary iteration with convergence factor $1-\varepsilon$, with explicit evaluation at $\varepsilon=0.01$, $\delta=10^{-6}$ giving $1374.6$ steps (Section 4.1).  
- A crossover analysis showing the law is insensitive to $\varepsilon$ at the logarithmic level: reducing $\varepsilon$ by a factor of ten multiplies the step count by only about $10.04$, computed explicitly (Section 4.2).  
- A coupling of the relaxation clock to the logical‑fidelity marker $F_\ast=0.874$, yielding $28.9$ steps at $\varepsilon=0.01$ before the marker is crossed (Section 4.3).  
- A limit‑ordering argument, grounded in the relaxation‑time results for quantized toral maps, that locates the only known quantum‑classical divergence in the joint $\hbar\to0$, $\varepsilon\to0$ limit, and a corresponding falsification criterion (Sections 4.4 and 6).

## 2. Background and Related Work

The notion of relaxation time for noisy quantum maps on the $2d$‑dimensional torus generalizes the earlier concept of dissipation time and shows sensitivity to chaotic behavior when the semiclassical limit ($\hbar\to0$) and the small‑noise limit ($\varepsilon\to0$) are taken jointly [6]. This result supplies the motivation for examining the fixed‑$\varepsilon$ regime.

On the classical side, parallel Jacobi algorithms have been modified to improve distribution over clusters [4]. The work presents concrete algorithmic changes to a state‑of‑the‑art exact maximum‑clique solver, illustrating how modest software modifications can achieve a “costup” (performance gain exceeding cost increase) [1]. The same paper details a distribution strategy that splits the search tree across $p$ processors, providing a concrete example of workload parallelization.

Submodular maximization literature emphasizes that practical runtime is often dominated by the cost of repeatedly querying the objective function, an insight that translates directly to relaxation where per‑step cost matters as much as step count [2]. Approximation algorithms for the Euclidean traveling‑salesman problem with neighborhoods (TSPN) demonstrate that structured generalizations of classical problems admit constant‑factor approximations, reminding us that results for structured maps (e.g., toral maps) need not transfer automatically to unstructured instances [3].

Consensus‑tree algorithms achieve optimal $O(kn)$ construction time because the input size is $\Omega(kn)$, illustrating that existence of a quantity (a consensus tree) does not guarantee an efficient procedure to compute it [7]. Similarly, the odd‑gracefulness work notes the scarcity of algorithms despite many published labeling papers, underscoring the gap between theoretical existence and practical computability [8].

The quantum‑speedup literature records that phase estimation admits a quadratic quantum advantage and that a continuous trade‑off between speedup and circuit depth exists via the $\alpha$‑QPE family [5]. This establishes that even for well‑understood quantum speedups the advantage is a trade‑off curve rather than a simple constant factor.

Finally, the QEC‑Darwinism trade‑off theorem states that quantum error correction and emergent classical objectivity cannot coexist above a critical logical fidelity $F_L>0.874$ [11]. Although the theorem does not address relaxation dynamics, the numerical bound provides a useful external marker for interpreting fidelity decay.

## 3. Methods

### 3.1 Common contraction frame

Both processes under comparison are discrete‑time linear contractions toward a fixed point. Let $x_t$ be the state after $t$ steps, $x_\ast$ the fixed point, and suppose  

$$\|x_{t+1}-x_\ast\|\le\rho\,\|x_t-x_\ast\|,$$  

with contraction factor $0\le\rho<1$. Iterating gives  

$$\|x_t-x_\ast\|\le\rho^{\,t}\,\|x_0-x_\ast\|.$$

Define the initial distance $D_0=\|x_0-x_\ast\|$ and a tolerance $\delta$ with $0<\delta<D_0$. The step count $t_\delta$ at which the distance first falls to $\delta$ satisfies $\rho^{\,t_\delta}D_0=\delta$, hence  

$$t_\delta=\frac{\ln(\delta/D_0)}{\ln\rho}.$$

This frame assumes linearity of the contraction, time‑independence of $\rho$, and a norm in which the contraction inequality holds.

### 3.2 Quantum instantiation: depolarizing noise on a qubit

For a single qubit undergoing a depolarizing channel of strength $\varepsilon$ per step, the state updates as  

$$\rho_{t+1}=(1-\varepsilon)\,\rho_t+\varepsilon\,\frac{\mathbb{I}}{2},$$  

so that after $t$ steps  

$$\rho_t=(1-\varepsilon)^t\rho_0+\bigl(1-(1-\varepsilon)^t\bigr)\frac{\mathbb{I}}{2}.$$

The maximally mixed state $\mathbb{I}/2$ is the fixed point, and the trace distance contracts as  

$$D\bigl(\rho_t,\mathbb{I}/2\bigr)=(1-\varepsilon)^t\,D\bigl(\rho_0,\mathbb{I}/2\bigr),$$  

identifying $\rho=1-\varepsilon$.

### 3.3 Classical instantiation: stationary iteration

For a classical stationary iteration $x_{t+1}=Mx_t+c$ with iteration matrix $M$ of spectral radius $\rho(M)<1$, the error propagates as $e_{t+1}=Me_t$, giving $\|e_t\|\le\rho(M)^t\|e_0\|$. Setting $\rho(M)=1-\varepsilon$ makes the classical and quantum instantiations share the identical step‑count law with identical parameters.

### 3.4 Fidelity clock and external marker

For the qubit channel of Section 3.2, the fidelity between $\rho_t$ and the pure initial state $\rho_0=|\psi\rangle\langle\psi|$ is  

$$F(t)=\langle\psi|\rho_t|\psi\rangle=\frac{1+(1-\varepsilon)^t}{2}.$$

Solving $F(t)=F_\ast$ for a chosen marker $F_\ast$ yields  

$$t_\ast=\frac{\ln(2F_\ast-1)}{\ln(1-\varepsilon)},$$  

valid when $F_\ast>1/2$. We adopt $F_\ast=0.874$ as an external logical‑fidelity marker.

### 3.5 Falsification protocol

Following the pre‑registration pattern of prior work on deterministic measurement‑triggered relaxation, we state in advance the observation that would falsify the central claim. The central claim is: at fixed $\varepsilon$ and fixed finite $\hbar$, quantum and classical relaxation obey the same step‑count law. The pre‑registered falsifier is any rigorously derived or empirically measured pair $(t_\delta^{\mathrm{Q}},t_\delta^{\mathrm{C}})$ at the same $\varepsilon$, $\delta$, and $D_0$ whose ratio differs from $1$ by more than the combined numerical and statistical uncertainty.

## 4. Analysis

### 4.1 Baseline step count at $\varepsilon=0.01$, $\delta=10^{-6}$

Inputs: $\varepsilon=0.01$, $D_0=1$, $\delta=10^{-6}$.

1. Contraction factor $\rho=1-\varepsilon=0.99$.  
2. $\ln(\delta/D_0)=\ln(10^{-6})=-6\ln10=-6\times2.302585=-13.815510$.  
3. $\ln\rho=\ln(0.99)$. Using the series $\ln(1-x)=-x-x^2/2-x^3/3-\dots$ with $x=0.01$ gives $-0.01-0.00005-0.000000333-0.0000000025=-0.010050336$.  
4.  

$$t_\delta=\frac{-13.815510}{-0.010050336}=1374.6.$$

Thus both the depolarizing qubit and the classical iteration with $\rho=0.99$ need $1374.6$ steps (rounded up to $1375$ integer steps) to reach $\delta=10^{-6}$.

### 4.2 Logarithmic insensitivity to $\varepsilon$

Reduce the noise strength to $\varepsilon=0.001$ ($\rho=0.999$).  

$\ln(0.999)=-0.001-0.0000005-0.000000000333=-0.001000500333$.  

Then  

$$t_\delta=\frac{13.815510}{0.001000500333}=13808.6.$$

The ratio to the $\varepsilon=0.01$ case is  

$$\frac{13808.6}{1374.6}=10.045.$$

A tenfold reduction in $\varepsilon$ multiplies the relaxation step count by $10.045$, confirming the logarithmic correction described by the series expansion.

### 4.3 Fidelity marker crossing at $F_\ast=0.874$

1. Compute $2F_\ast-1=2\times0.874-1=0.748$.  
2. $\ln(0.748)$. Using $\ln(0.748)=\ln(748)-\ln(1000)$.  
   - $\ln(748)=\ln(7.48)+\ln(100)=2.012220+4.605170=6.617390$.  
   - $\ln(1000)=6.907755$.  
   Hence $\ln(0.748)=6.617390-6.907755=-0.290365$.  
3. With $\varepsilon=0.01$ ($\ln\rho=-0.010050336$),  

$$t_\ast=\frac{-0.290365}{-0.010050336}=28.89.$$

Thus the fidelity marker $F_\ast=0.874$ is crossed after $28.9$ steps at $\varepsilon=0.01$. For comparison, at $\varepsilon=0.1$ ($\ln0.9=-0.105361$) the crossing occurs after $2.756$ steps, and at $\varepsilon=0.001$ after $290.2$ steps.

### 4.4 Where the quantum case can diverge: the joint limit

At fixed $\varepsilon$ and finite $\hbar$, Sections 4.1–4.3 show the quantum relaxation clock is fully determined by the contraction factor $1-\varepsilon$ and is identical in form to the classical stationary‑iteration clock. The known point of divergence is supplied by the toral‑map result [6]: relaxation time is sensitive to the chaotic behavior of the corresponding classical system when the semiclassical limit ($\hbar\to0$) and the small‑noise limit ($\varepsilon\to0$) are taken simultaneously. The structural reason the two limits must be joint is visible in our own formulas: as $\varepsilon\to0$ at fixed tolerance, $t_\delta\to\infty$ like $1/\varepsilon$, so the noise‑induced relaxation that defines the clock vanishes exactly in the regime where classical dynamics would dominate; any chaos‑dependence must therefore be resolved in the ordering of $\hbar\to0$ relative to $\varepsilon\to0$.

### 4.5 Per‑step cost and the costup criterion

Step count alone does not determine wall‑clock time. Let $c_{\mathrm{Q}}$ and $c_{\mathrm{C}}$ be the per‑step costs (in time or energy) of one quantum‑map application and one classical iteration, respectively. Wall‑clock parity requires  

$$c_{\mathrm{Q}}\,t_\delta^{\mathrm{Q}}<c_{\mathrm{C}}\,t_\delta^{\mathrm{C}}.$$

Since $t_\delta^{\mathrm{Q}}=t_\delta^{\mathrm{C}}$ at matched parameters, parity reduces to $c_{\mathrm{Q}}<c_{\mathrm{C}}$. The costup concept from [1]—significant speedup with minimal development effort—provides the qualitative gate a deployment must pass.

## 5. Results

All numbers below are computed in Section 4 by explicit arithmetic from the stated inputs; none are measured or simulated.

**R1 (shared step‑count law).** At $\varepsilon=0.01$, $D_0=1$, $\delta=10^{-6}$, both the depolarizing qubit channel and a classical stationary iteration with convergence factor $0.99$ relax in $t_\delta=1374.6$ steps ($1375$ integer steps). The two processes are step‑count‑indistinguishable at matched parameters.

**R2 (logarithmic insensitivity).** Reducing $\varepsilon$ from $0.01$ to $0.001$ raises the step count from $1374.6$ to $13808.6$, a factor of $10.045$. The step count obeys $t_\delta\approx\ln(\delta/D_0)/(-\varepsilon-\varepsilon^2/2)$, with a $0.498\%$ logarithmic correction at $\varepsilon=0.01$.

**R3 (fidelity marker crossing).** The fidelity marker $F_\ast=0.874$ is crossed after $28.9$ steps at $\varepsilon=0.01$, after $2.756$ steps at $\varepsilon=0.1$, and after $290.2$ steps at $\varepsilon=0.001$. The marker sits at $25.2\%$ of the initial‑to‑fixed‑point distance.

**R4 (locus of divergence).** At fixed $\varepsilon$ and finite $\hbar$, no divergence between quantum and classical relaxation is derivable in the contraction frame. The only grounded locus of divergence is the joint $\hbar\to0$, $\varepsilon\to0$ limit, where relaxation time of noisy quantum maps on tori is sensitive to the chaos of the underlying classical system [6]. The quantitative ordering parameter (an Ehrenfest‑time‑to‑$1/\varepsilon$ ratio) is not computable from the supplied grounding and is listed as open.

**R5 (cost gate).** Wall‑clock parity at matched parameters requires $c_{\mathrm{Q}}<c_{\mathrm{C}}$; no per‑step cost values are derivable from the grounding, so this is stated as a gate, not a number.

## 6. Discussion

The central result, R1, is a negative one: in the simplest common frame, relaxation in a noisy quantum map and relaxation in a classical iterative algorithm are the same process mathematically, and the interesting physics lives entirely in the joint limit that the contraction frame deliberately freezes. This framing has three limitations that a reader should weigh before using R1 in any decision.

*First*, the contraction frame assumes a time‑independent, linear contraction with a single fixed point. Real quantum maps can have multiple fixed points, limit cycles, or non‑normal contraction structure, and real classical solvers use preconditioning, acceleration, and adaptive tolerances that change the effective $\rho$ from step to step. The parallel Jacobi algorithms described in [4] illustrate that convergence quality can be instance‑dependent in ways a single‑$\rho$ model hides.

*Second*, the identification $\rho(M)=1-\varepsilon$ is a modeling choice. A classical iteration with $\rho=0.99$ and a qubit under $\varepsilon=0.01$ depolarizing noise match by construction, but nothing forces a real workload to present matched parameters. The falsification protocol of Section 3.5 is designed around exactly this conditionality.

*Third*, the imported fidelity marker $0.874$ comes from an external no‑go theorem about coexistence of quantum error correction and emergent classical objectivity; we use it as a generic clock marker. That theorem constrains information‑theoretic roles, not the step count of a relaxation process. Hence R3 should be read as a consistency illustration rather than a hardware‑relevant lifetime prediction.

**What would falsify the main result.** The main result (R1, with R4 as its boundary) is falsified if any of the following is established: (i) a noisy quantum map at fixed $\varepsilon$ and finite $\hbar$ whose relaxation time to tolerance $\delta$ differs from $\ln(\delta/D_0)/\ln(1-\varepsilon)$ by more than numerical uncertainty; (ii) a classical stationary iteration and a quantum map with matched contraction factors whose measured or rigorously derived step counts differ at the same $\delta$ and $D_0$; (iii) a derivation showing that the chaos‑sensitivity of relaxation time in the toral‑map setting [6] survives at fixed finite $\hbar$ and $\varepsilon$, rather than only in the joint limit. Any one of these would force a revision of R1; none is currently available in the grounding.

**Limitations list.**

- *Single fixed point, linear contraction.* R1 holds only within the frame of Section 3.1; sensitivity to this assumption is total.  
- *Depolarizing noise model.* The quantum instantiation uses the standard depolarizing channel; other channels can give different fixed points, so R1’s numerical value $1374.6$ is model‑specific.  
- *Matched‑parameter condition.* Equality in R1 requires $\rho(M)=1-\varepsilon$; unmatched parameters reintroduce a difference that is trivially large.  
- *Imported fidelity marker.* R3 reinterprets the external marker $0.874$ as a clock; the underlying theorem does not concern relaxation dynamics.  
- *No per‑step costs.* R5 is a gate without numbers because no cost data exist in the grounding.  
- *Open ordering parameter.* The ratio of the Ehrenfest‑type time to $1/\varepsilon$, which would quantify R4, is not derivable from the supplied abstract of [6]; the divergence claim is therefore qualitative at exactly the point where it would be most useful.  
- *Thin grounding for two sources.* The entries for the pre‑registered falsification work [12] and “Programming the Vacuum” [9] supply no abstract text; claims resting on them are correspondingly minimal, and the bibliography contains twelve works of which two are content‑less in this grounding—a limitation of the source set itself.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are operators and architects of hybrid classical‑quantum compute facilities who must decide, for a relaxation‑type workload, whether to schedule it on classical hardware or on a quantum co‑processor. If R1 holds, the decision rule changes from “estimate the quantum speedup exponent” to “compare per‑step costs $c_{\mathrm{Q}}$ and $c_{\mathrm{C}}$ at matched contraction parameters, and check whether the workload’s effective noise strength $\varepsilon$ can be lowered on either route.” Concretely, a scheduling policy derived from R1 is: compute $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$ for the workload’s tolerance and noise level, apply it identically to both routes, and break the tie only on per‑step cost and limit‑ordering risk (R4). A second user group is the authors and consumers of quantum‑relaxation proposals: R1 supplies the fair‑comparison condition $\rho(M)=1-\varepsilon$ that any claimed quantum advantage must satisfy before it is credited to quantumness rather than to unmatched parameters. A third group is error‑correction system designers, for whom R3 gives a derived illustration: at $\varepsilon=0.01$, the imported marker $F_\ast=0.874$ is crossed after $28.9$ steps, so any protocol that must keep logical fidelity above that marker has a per‑step noise budget of order $10^{-3}$ or smaller for runs of hundreds of steps.

**(b) Current readiness.** This work is purely analytical and has not been peer reviewed: the contraction frame of Section 3.1, the derivations of Section 4, and the falsification protocol of Section 3.5 are all pen‑and‑paper results with no hardware, simulation, or experimental component. Against the NASA Technology Readiness Level definitions, this places the work at TRL 1–2: basic principles observed and reported, with the underlying physical and mathematical assumptions formulated but not applied in any demonstrated context. Analytical work cannot exceed TRL 3, and nothing in this paper supports a claim of experimental validation, component development, or manufacturing readiness.

**(c) The smallest next test.** The smallest de‑risking calculation is a numerical one, requiring no quantum hardware: implement the depolarizing qubit channel of Section 3.2 and a classical stationary iteration with $\rho(M)=1-\varepsilon$ on the same computer, run both from matched initial conditions to tolerance $\delta=10^{-6}$ at $\varepsilon=0.01$, and verify that both reach the tolerance at the same step count, predicted to be $1375$ integer steps (Section 4.1). The outcome that refutes R1 is a measured step‑count mismatch between the two implementations at matched parameters beyond floating‑point round‑off; the outcome that refutes the frame itself is a quantum‑map simulation at fixed $\varepsilon$ and finite effective $\hbar$ whose relaxation step count deviates from $\ln(\delta/D_0)/\ln(1-\varepsilon)$ by more than numerical uncertainty.

**(d) Binding constraints.** Because this is analytical work, the constraints that would bind first in any future engineering use are, in order: (i) *noise characterization* — the law’s input $\varepsilon$ must be the actual per‑step noise strength of the device; (ii) *channel validity* — the quantum instantiation assumes depolarizing noise; (iii) *per‑step cost data* — the cost gate of R5 requires $c_{\mathrm{Q}}$ and $c_{\mathrm{C}}$, neither of which is derivable from the grounding; (iv) *limit‑ordering theory* — the Ehrenfest‑time‑to‑$1/\varepsilon$ ratio of Section 4.4 is not computable from the supplied abstract of [6], so any deployment in the joint‑limit regime is blocked on theory before it is blocked on hardware.

**(e) Order‑of‑magnitude bounds.** Assuming the depolarizing model and $D_0=1$: a tenfold reduction in tolerance (one decade of $\delta$) adds $2.302585/0.010050336\approx229.1$ steps at $\varepsilon=0.01$; a tenfold reduction in $\varepsilon$ multiplies the step count by $10.045$ (Section 4.2). No cost, energy, market, or performance figures are stated, because no per‑step cost or device data exist in the grounding; any such figure would be unsupported.

**(f) Risks and misuse paths.** The principal misuse is the one the paper is designed to prevent, in both directions: citing R1 to claim “no quantum advantage is possible” (it constrains only matched‑parameter, fixed‑$\varepsilon$, single‑fixed‑point comparisons), or citing R4 to claim “quantum relaxation is chaos‑accelerated” (the chaos‑sensitivity of [6] is established only in the joint $\hbar\to0$, $\varepsilon\to0$ limit, and no ordering parameter is computed here). A second misuse path is reading R3 as a hardware lifetime prediction; Section 6 states explicitly that R3 is a consistency illustration of the fidelity clock, not a property of the external theorem. A third is treating the external marker $0.874$ as a certified operating point; its provenance is a single external source, and this paper neither re‑derives nor validates it.

## 8. Conclusion

Relaxation in a noisy quantum map and relaxation in a classical stationary iteration, placed in the same linear‑contraction frame with matched parameters, obey the identical step‑count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$: at $\varepsilon=0.01$ and $\delta=10^{-6}$ both need $1374.6$ steps, and the law is logarithmically insensitive to its inputs, a tenfold noise reduction buying only a factor of $10.045$ in step count. The fidelity clock derived from the same frame crosses the external marker $F_\ast=0.874$ after $28.9$ steps at $\varepsilon=0.01$. Within this frame, therefore, there is no quantum‑classical distinction to exploit or fear; the one grounded locus of distinction is the joint semiclassical and weak‑noise limit, where relaxation time of quantized toral maps is known to depend on the chaos of the underlying classical system, and where the quantitative ordering parameter remains open. The practical yield of the analysis is a fair‑comparison condition, a pre‑registered falsifier, and a smallest next test—a matched‑parameter numerical run of the depolarizing channel against a stationary iteration, predicted to terminate at the same $1375$th step—by which the central claim can be refuted if it is wrong.

## References

[1] arXiv:1209.4560v1 | Distributing an Exact Algorithm for Maximum Clique: maximising the costup  
[2] arXiv:2311.13123v2 | Fast Parallel Algorithms for Submodular $p$-Superseparable Maximization  
[3] arXiv:1703.01640v1 | Approximation algorithms for TSP with neighborhoods in the plane  
[4] arXiv:1008.0201v2 | Novel Modifications of Parallel Jacobi Algorithms  
[5] arXiv:2207.14810v3 | Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations  
[6] arXiv:math-ph/0406055v3 | Relaxation Time of Quantized Toral Maps  
[7] arXiv:1307.7821v2 | Algorithms for the Majority Rule (+) Consensus Tree and the Frequency Difference Consensus Tree  
[8] arXiv:1103.4502v1 | An Algorithm for Odd Gracefulness of the Tensor Product of Two Line Graphs  
[9] QNFO: Programming the Vacuum  
[11] QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces  
[12] QNFO: A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation  

## Appendix A. Divergence report

*No divergent claims were identified among the drafts; all substantive claims converged.*

## Appendix B. Claim attribution

| Claim ID | Source Draft(s) | Agreement |
|----------|-----------------|-----------|
| C1 | A, B, C | CONVERGENT |
| C2 | A, B, C | CONVERGENT |
| C3 | A, B, C | CONVERGENT |
| C4 | A, B, C | CONVERGENT |
| C5 | A, B, C | CONVERGENT |
| C6 | A, B, C | CONVERGENT |
| C7 | A, B, C | CONVERGENT |
| C8 | A, B, C | CONVERGENT |
| C9 | A, B, C | CONVERGENT |
| C10 | A, B, C | CONVERGENT |
| C11 | A, B, C | CONVERGENT |
| C12 | A, B, C | CONVERGENT |
| C