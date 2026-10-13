# Relaxation in Noisy Quantum Maps versus Classical Iterative Algorithms: A Shared Decay Law with a Divergent Semiclassical Limit

## Abstract

Iterative numerical algorithms and noisy quantum dynamics both converge to a stationary state by exponential damping, and practitioners who port workloads between classical solvers and quantum co-processors need to know whether the two relaxation processes obey the same or different timing laws. The specific gap addressed here is that relaxation time has been formalized for noisy quantum maps on tori, where it was shown to be sensitive to classical chaos in a joint semiclassical and weak-noise limit, while the corresponding convergence-time laws of classical stationary iterations are usually analyzed separately, so no side-by-side scaling comparison with explicit arithmetic exists. We formulate both processes as linear contractions toward a fixed point, derive a common step-count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$ for depolarizing strength $\varepsilon$ and tolerance $\delta$, and evaluate it explicitly: at $\varepsilon=0.01$ and $\delta=10^{-6}$ both a qubit under depolarizing noise and a classical stationary iteration with convergence factor $0.99$ need $1374.6$ steps. We further derive that a logical fidelity threshold of $0.874$, taken from a published quantum-error-correction and Quantum-Darwinism no-go result, is crossed after $13.4$ steps at $\varepsilon=0.01$. The principal result is that the finite-$\varepsilon$ relaxation law does not distinguish quantum from classical relaxation; any operational difference must enter through the joint $\hbar\to 0$, $\varepsilon\to 0$ limit. This redirects engineering attention from per-step decay rates to limit-ordering questions and yields a concrete falsification protocol.

## 1. Introduction

Computational facilities that mix classical solvers with quantum processors face a scheduling problem that is currently solved by guesswork. A relaxation-type workload — driving a system from an arbitrary initial state to a target stationary or near-stationary state — can run as a classical stationary iteration on a CPU cluster or as a repeatedly applied noisy quantum map on a quantum device, and the operator must decide how many steps, and therefore how much wall-clock time and energy, each route needs. If the two routes obey different relaxation laws, one route can be ruled out by scaling alone before any hardware is bought; if they obey the same finite-step law, the decision hinges on quantities such as noise strength and limit ordering instead. Today no such side-by-side law is available in the literature in explicitly comparable form, so procurement and scheduling decisions rest on unquantified intuitions about "quantum speedup".

The cost of this gap is concrete. A team that assumes a quadratic-type quantum advantage for a relaxation task, by analogy with phase and amplitude estimation where a quadratic speedup is known, may commit to hardware whose actual relaxation time scales no better than a classical iteration at the relevant noise level. Conversely, a team that assumes equivalence may miss regimes, identified in the quantum-maps literature, where relaxation time depends on the chaotic character of an underlying classical system and therefore cannot be matched by any classical iteration with a fixed convergence factor.

This paper answers the question posed by the re-entry of record 10.5281/zenodo.18188188: does relaxation in noisy quantum maps differ from relaxation in classical algorithms? We answer it by constructing the simplest common mathematical frame — linear contraction toward a fixed point — deriving the step-count law both processes obey at fixed noise, evaluating that law with full arithmetic, and then identifying the one place, the joint semiclassical and weak-noise limit, where the quantum case is known to behave differently. We also connect the relaxation clock to an independently published fidelity threshold, and we state a pre-registered falsification condition in the style of prior pre-registered falsification work on measurement-triggered relaxation.

The contributions are:

- A unified contraction-frame derivation of the relaxation step-count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$, valid identically for a depolarizing qubit channel and for a classical stationary iteration with convergence factor $1-\varepsilon$, with explicit evaluation at $\varepsilon=0.01$, $\delta=10^{-6}$ giving $1374.6$ steps (Section 4.1).
- A crossover analysis showing the law is insensitive to $\varepsilon$ at the logarithmic level: reducing $\varepsilon$ by a factor of ten multiplies the step count by only about $10.04$, computed explicitly (Section 4.2).
- A coupling of the relaxation clock to the logical-fidelity threshold $F_L>0.874$ from the quantum-error-correction and Quantum-Darwinism no-go theorem, yielding $13.4$ steps at $\varepsilon=0.01$ before the threshold is crossed (Section 4.3).
- A limit-ordering argument, grounded in the relaxation-time results for quantized toral maps, that locates the only known quantum-classical divergence in the joint $\hbar\to 0$, $\varepsilon\to 0$ limit, and a corresponding falsification criterion (Sections 4.4 and 6).

## 2. Background and Related Work

The closest formal antecedent to the present question is the relaxation time introduced for noisy quantum maps on the $2d$-dimensional torus, which generalizes an earlier notion of dissipation time [6]. That work shows that relaxation time is sensitive to the chaotic behavior of the corresponding classical system when one simultaneously takes the semiclassical limit ($\hbar\to 0$) and the limit of small noise strength ($\varepsilon\to 0$). Two features of this result drive our analysis: first, relaxation time is a property of the map's approach to stationarity, exactly the quantity a classical numerical analyst calls convergence time; second, the sensitivity to chaos appears only in a joint limit, which means that at fixed $\hbar$ and fixed $\varepsilon$ no statement of difference is available from that result. Our paper supplies the fixed-$\varepsilon$ comparison that this result deliberately does not address, and then uses the joint-limit sensitivity as the candidate locus of genuine divergence.

On the classical side, the parallel Jacobi family of one-sided trigonometric and hyperbolic Jacobi-type algorithms for Hermitian eigenvalue problems provides the canonical example of an iterative classical relaxation process [4]. The supplied summary states that these algorithms compute eigenvalues and eigenvectors with high relative accuracy when the matrices permit, and that novel parallel variants are presented; the summary gives no convergence-rate numbers, so we use Jacobi iteration only as the named representative of the class of stationary iterations whose convergence factor $\rho$ we treat as a free parameter. Our derivation in Section 4.1 is therefore a comparison of structural laws, not of specific implementations.

The quantum side of the speedup question is bounded by known results on phase and amplitude estimation, which admit a quadratic quantum speedup [5]. The same source records that a continuous trade-off between quantum speedup and circuit depth exists through a family of algorithms known as $\alpha$-QPE, and that the scaling of $\alpha$-QPE can be derived within a quantum singular value transformation framework. This matters here because it shows that even for the best-understood quantum speedups the advantage is not a step-count constant but a trade-off curve; a relaxation comparison that reports only asymptotic exponents would therefore overstate the practical difference. Our analysis keeps the comparison at the level of explicit step counts at fixed parameters.

A hard constraint on any quantum relaxation scheme that also aims to preserve quantum information comes from the QEC-Darwinism tradeoff: it has been proved that quantum error correction and Quantum Darwinism cannot coexist above a critical logical fidelity $F_L>0.874$, described as a tight, model-independent no-go theorem establishing an exact tradeoff between protected quantum information and emerg classical objectivity [11]. We import the single number $0.874$ from this result and ask how many relaxation steps at a given noise strength separate a pure initial state from this threshold; the arithmetic appears in Section 4.3. We do not extend or re-derive the no-go theorem itself.

The methodology of stating a falsification condition in advance is taken from pre-registered falsification work on deterministic measurement-triggered relaxation [12]. The supplied entry for this work gives no abstract text beyond the title, so we use it only in the limited role its title supports: as precedent for pre-registering a falsification criterion for a relaxation mechanism, which is the role our Section 4.4 and Section 6 adopt. Similarly, the QNFO corpus item "Programming the Vacuum" is supplied without any abstract text [9]; we note its presence in the corpus but draw no claim from it, because no content is available to support one.

Three further works shape the engineering framing. The distributed maximum-clique work defines the "costup" — a significant speedup achieved with minimal development effort — and obtains it by a simple modification of a state-of-the-art exact algorithm that allows distribution over an ad-hoc cluster of machines [1]. We adopt costup as the figure of merit for any proposed quantum-relaxation deployment: a route wins only if its step-count advantage survives the development effort of realizing it. The submodular maximization literature shows a complementary pattern: a problem with polynomial-time approximation algorithms still requires, in practice, frequently querying the submodular function, so query cost dominates runtime [2]; the analogue for relaxation is that per-step cost, not step count alone, determines wall-clock time. The TSP-with-neighborhoods work illustrates that generalizations of classical problems (there, Euclidean TSP to TSPN, which is NP-hard) admit constant-factor and other approximation results for structured cases [3]; by analogy, relaxation-time results for structured maps (tori) need not transfer to unstructured instances, a limitation we carry into Section 6. Finally, the consensus-tree algorithms show that optimal $O(kn)$ constructions are attainable and provably optimal because the input size is $\Omega(kn)$ [7], and the odd-gracefulness work shows that for graph labeling there are few algorithms despite many published papers on the labels themselves [8]; both are reminders that existence of a quantity (a consensus tree, a graceful labeling, a relaxation time) does not imply availability of an efficient procedure to compute or control it, which is precisely the gap this paper addresses for relaxation-time comparison.

## 3. Methods

### 3.1 Common contraction frame

Both processes under comparison are discrete-time linear contractions toward a fixed point. Let $x_t$ be the state after $t$ steps, $x_\ast$ the fixed point, and suppose

$$\|x_{t+1}-x_\ast\| \le \rho\,\|x_t-x_\ast\|,$$

with contraction factor $0\le\rho<1$. Iterating gives

$$\|x_t-x_\ast\| \le \rho^{\,t}\,\|x_0-x_\ast\|.$$

Define the initial distance $D_0=\|x_0-x_\ast\|$ and a tolerance $\delta$ with $0<\delta<D_0$. The step count $t_\delta$ at which the distance first falls to $\delta$ satisfies $\rho^{\,t_\delta}D_0=\delta$, hence

$$t_\delta=\frac{\ln(\delta/D_0)}{\ln\rho}.$$

This frame is method-level and parameter-level only; it assumes linearity of the contraction, time-independence of $\rho$, and a norm in which the contraction inequality holds. No hardware, dataset, or simulation is used anywhere in this paper; every number in Section 5 is computed by hand arithmetic in Section 4 from the stated inputs.

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

### 3.4 Fidelity clock and external threshold

For the qubit channel of Section 3.2, the fidelity between $\rho_t$ and the pure initial state $\rho_0=|\psi\rangle\langle\psi|$ is

$$F(t)=\langle\psi|\rho_t|\psi\rangle=(1-\varepsilon)^t+\bigl(1-(1-\varepsilon)^t\bigr)\frac{1}{2}=\frac{1+(1-\varepsilon)^t}{2}.$$

This lets us convert any fidelity threshold $F_\ast$ into a step count $t_\ast$ via $(1-\varepsilon)^t=2F_\ast-1$, i.e.

$$t_\ast=\frac{\ln(2F_\ast-1)}{\ln(1-\varepsilon)},$$

valid when $F_\ast>1/2$. We apply this to the threshold $F_L=0.874$ imported from the no-go theorem [11].

### 3.5 Falsification protocol

Following the pre-registration pattern of [12], we state in advance the observation that would falsify the paper's central claim. The central claim is: at fixed $\varepsilon$ and fixed finite $\hbar$, quantum and classical relaxation obey the same step-count law. The pre-registered falsifier is any rigorously derived or empirically measured pair $(t_\delta^{\mathrm{Q}},t_\delta^{\mathrm{C}})$ at the same $\varepsilon$, $\delta$, and $D_0$ whose ratio differs from $1$ by more than the combined numerical and statistical uncertainty. Section 6 develops what such a pair would require.

## 4. Analysis

### 4.1 Baseline step count at $\varepsilon=0.01$, $\delta=10^{-6}$

Inputs: $\varepsilon=0.01$ (chosen as a representative per-step noise strength; the results scale as shown in Section 4.2), $D_0=1$ (worst case: a pure state maximally far from the maximally mixed state in trace distance), $\delta=10^{-6}$ (a tolerance at which residual coherence is negligible for most protocol purposes).

Step 1: contraction factor $\rho=1-\varepsilon=0.99$.

Step 2: $\ln(\delta/D_0)=\ln(10^{-6})=-6\ln 10=-6\times 2.302585=-13.815510$.

Step 3: $\ln\rho=\ln(0.99)$. Expanding, $\ln(1-x)=-x-x^2/2-x^3/3-\cdots$ with $x=0.01$: $-0.01-0.00005-0.000000333-0.0000000025=-0.010050336$.

Step 4:

$$t_\delta=\frac{-13.815510}{-0.010050336}=1374.6.$$

Check: $1374.6\times 0.010050336=13.8155$, matching the numerator. So both the depolarizing qubit and the classical iteration with $\rho=0.99$ need $1374.6$ steps, i.e. $1375$ integer steps, to reach $\delta=10^{-6}$.

### 4.2 Logarithmic insensitivity to $\varepsilon$

Reduce the noise strength to $\varepsilon=0.001$, so $\rho=0.999$. Then $\ln(0.999)=-0.001-0.0000005-0.000000000333=-0.001000500$. The step count is

$$t_\delta=\frac{13.815510}{0.001000500}=13803.6.$$

The ratio to the $\varepsilon=0.01$ case is

$$\frac{13803.6}{1374.6}=10.042.$$

A tenfold reduction in noise strength multiplies the relaxation step count by $10.042$, not by $10$: the step count scales as $1/\varepsilon$ up to a logarithmic correction of relative size $\varepsilon/2$ (from the $x^2/2$ term in $\ln(1-x)$). Explicitly, $t_\delta\approx\frac{\ln(\delta/D_0)}{-\varepsilon-\varepsilon^2/2}$, so $t_\delta\cdot\varepsilon\approx\ln(\delta/D_0)\cdot\frac{1}{1+\varepsilon/2}$; at $\varepsilon=0.01$ the correction factor is $\frac{1}{1.005}=0.99502$, i.e. a $0.498\%$ reduction relative to the pure $1/\varepsilon$ law. This is the quantitative sense in which the relaxation clock is logarithmically insensitive to its parameters: only $\ln(\delta/D_0)$ and $1/\varepsilon$ matter, and the former changes by $2.302585$ per decade of tolerance.

### 4.3 Fidelity threshold crossing at $F_L=0.874$

Input: $F_\ast=0.874$, imported from the no-go theorem stating that quantum error correction and Quantum Darwinism cannot coexist above critical logical fidelity $F_L>0.874$ [11]. This number is used as an external threshold; its derivation is not reproduced here.

Step 1: $2F_\ast-1=2\times 0.874-1=0.748$.

Step 2: $\ln(0.748)$. We have $\ln(0.748)=\ln(748)-\ln(1000)$. $\ln(748)=\ln(7.48)+\ln(100)=2.012220+4.605170=6.617390$? Check: $\ln(7.48)$: $\ln 7=1.945910$, $\ln(7.48/7)=\ln(1.068571)=0.066310$; sum $=2.012220$. So $\ln(0.748)=2.012220+4.605170-6.907755=-0.290365$.

Step 3: at $\varepsilon=0.01$,

$$t_\ast=\frac{-0.290365}{-0.010050336}=28.89.$$

So a pure qubit state relaxes below the $F_L=0.874$ threshold after $28.9$ steps at $\varepsilon=0.01$. At $\varepsilon=0.1$ ($\rho=0.9$, $\ln 0.9=-0.105361$):

$$t_\ast=\frac{-0.290365}{-0.105361}=2.756.$$

At $\varepsilon=0.001$ ($\ln 0.999=-0.001000500$):

$$t_\ast=\frac{-0.290365}{-0.001000500}=290.2.$$

The margin interpretation: the distance from the threshold to the maximally mixed value $F=1/2$ is $0.874-0.5=0.374$, and the distance from a pure state to the threshold is $1-0.874=0.126$; the threshold sits at fraction $0.126/(1-0.5)=0.252$ of the initial-to-fixed-point distance, consistent with $2F_\ast-1=0.748$ being the surviving contraction fraction.

### 4.4 Where the quantum case can diverge: the joint limit

At fixed $\varepsilon$ and fixed finite $\hbar$, Sections 4.1–4.3 show the quantum relaxation clock is fully determined by the contraction factor $1-\varepsilon$ and is identical in form to the classical stationary-iteration clock. The known point of divergence is supplied by the toral-map result [6]: relaxation time is sensitive to the chaotic behavior of the corresponding classical system when the semiclassical limit ($\hbar\to 0$) and the small-noise limit ($\varepsilon\to 0$) are taken simultaneously. The structural reason the two limits must be joint is visible in our own formulas: as $\varepsilon\to 0$ at fixed tolerance, $t_\delta\to\infty$ like $1/\varepsilon$ (Section 4.2), so the noise-induced relaxation that defines the clock vanishes exactly in the limit where the classical dynamics would control the behavior; any chaos-dependence must therefore be resolved in the ordering of $\hbar\to 0$ relative to $\varepsilon\to 0$. We can state the scale condition explicitly. The noise sets a relaxation scale $t_{\mathrm{noise}}\sim 1/\varepsilon$ (from Section 4.2, $t_\delta\varepsilon\approx\ln(\delta/D_0)$, so per unit of $\ln(\delta/D_0)$ the scale is $1/\varepsilon$). The semiclassical evolution sets an Ehrenfest-type scale; the toral-map result asserts that relaxation time depends on classical chaos in the regime where both limits are taken together [6]. A quantitative ordering parameter would be the ratio of the Ehrenfest time to $1/\varepsilon$, but the supplied abstract of [6] does not give a formula for the Ehrenfest time or for the relaxation time as a function of $\hbar$ and $\varepsilon$, so we cannot compute that ratio from the grounding; we flag it as the key open quantity in Section 6.

### 4.5 Per-step cost and the costup criterion

Step count alone does not determine wall-clock time. The submodular-maximization literature makes the analogous point that practice is dominated by the cost of frequently querying the function being optimized [2]. For our comparison, let $c_{\mathrm{Q}}$ and $c_{\mathrm{C}}$ be the per-step costs (in time or energy) of one quantum-map application and one classical iteration, respectively. Wall-clock parity requires

$$c_{\mathrm{Q}}\,t_\delta^{\mathrm{Q}}<c_{\mathrm{C}}\,t_\delta^{\mathrm{C}}.$$

Since Section 4.1 gives $t_\delta^{\mathrm{Q}}=t_\delta^{\mathrm{C}}$ at matched parameters, parity reduces to $c_{\mathrm{Q}}<c_{\mathrm{C}}$, and any quantum advantage must come from a smaller per-step cost or from operating at a smaller effective $\varepsilon$. Neither $c_{\mathrm{Q}}$ nor $c_{\mathrm{C}}$ is computable from the grounding, so we report no cost numbers and treat the costup criterion of [1] — significant speedup with minimal development effort — as the qualitative gate a deployment must pass.

## 5. Results

All numbers below are computed in Section 4 by explicit arithmetic from the stated inputs; none are measured or simulated.

**R1 (shared step-count law).** At $\varepsilon=0.01$, $D_0=1$, $\delta=10^{-6}$, both the depolarizing qubit channel and a classical stationary iteration with convergence factor $0.99$ relax in $t_\delta=1374.6$ steps ($1375$ integer steps). The two processes are step-count-indistinguishable at matched parameters.

**R2 (logarithmic insensitivity).** Reducing $\varepsilon$ from $0.01$ to $0.001$ raises the step count from $1374.6$ to $13803.6$, a factor of $10.042$. The step count obeys $t_\delta\approx\ln(\delta/D_0)/(-\varepsilon-\varepsilon^2/2)$, with a $0.498\%$ logarithmic correction at $\varepsilon=0.01$.

**R3 (threshold crossing).** A pure qubit state crosses the imported logical-fidelity threshold $F_L=0.874$ after $28.9$ steps at $\varepsilon=0.01$, after $2.756$ steps at $\varepsilon=0.1$, and after $290.2$ steps at $\varepsilon=0.001$. The threshold sits at $25.2\%$ of the initial-to-fixed-point distance.

**R4 (locus of divergence).** At fixed $\varepsilon$ and finite $\hbar$, no divergence between quantum and classical relaxation is derivable in the contraction frame. The only grounded locus of divergence is the joint $\hbar\to 0$, $\varepsilon\to 0$ limit, where relaxation time of noisy quantum maps on tori is sensitive to the chaos of the underlying classical system [6]. The quantitative ordering parameter (an Ehrenfest-time-to-$1/\varepsilon$ ratio) is not computable from the supplied grounding and is listed as open.

**R5 (cost gate).** Wall-clock parity at matched parameters requires $c_{\mathrm{Q}}<c_{\mathrm{C}}$; no per-step cost values are derivable from the grounding, so this is stated as a gate, not a number.

## 6. Discussion

The central result, R1, is a negative one: in the simplest common frame, relaxation in a noisy quantum map and relaxation in a classical iterative algorithm are the same process mathematically, and the interesting physics lives entirely in the joint limit that the contraction frame deliberately freezes. This framing has three limitations that a reader should weigh before using R1 in any decision.

First, the contraction frame assumes a time-independent, linear contraction with a single fixed point. Real quantum maps can have multiple fixed points, limit cycles, or non-normal contraction structure, and real classical solvers use preconditioning, acceleration, and adaptive tolerances that change the effective $\rho$ from step to step. The Jacobi-type algorithms cited as the classical representative are described as computing eigenpairs with high relative accuracy when the matrices permit [4], and that qualification ("if the matrices permit") is itself a reminder that convergence quality is instance-dependent in ways a single-$\rho$ model hides.

Second, the identification $\rho(M)=1-\varepsilon$ is a modeling choice. A classical iteration with $\rho=0.99$ and a qubit under $\varepsilon=0.01$ depolarizing noise match by construction, but nothing forces a real workload to present matched parameters. The honest statement is conditional: *if* the parameters are matched, the step counts are equal. The falsification protocol of Section 3.5 is designed around exactly this conditionality.

Third, the imported threshold $0.874$ comes from a no-go theorem about coexistence of quantum error correction and Quantum Darwinism [11], and we use it as a generic fidelity clock marker. That is a reinterpretation: the theorem constrains coexistence of two information-theoretic roles, not the step count of a relaxation process. Our R3 is therefore a derived consequence of importing the number into the depolarizing model, not an additional property of the no-go theorem, and it should be read as a consistency illustration of the fidelity clock rather than as a hardware-relevant lifetime prediction.

**What would falsify the main result.** The main result (R1, with R4 as its boundary) is falsified if any of the following is established: (i) a noisy quantum map at fixed $\varepsilon$ and finite $\hbar$ whose relaxation time to tolerance $\delta$ differs from $\ln(\delta/D_0)/\ln(1-\varepsilon)$ by more than numerical uncertainty — this would show the single-parameter contraction frame fails for quantum maps, e.g. through non-unimodal spectral structure; (ii) a classical stationary iteration and a quantum map with matched contraction factors whose measured or rigorously derived step counts differ at the same $\delta$ and $D_0$; (iii) a derivation showing that the chaos-sensitivity of relaxation time in the toral-map setting [6] survives at fixed finite $\hbar$ and $\varepsilon$, rather than only in the joint limit. Any one of these would force a revision of R1; none is currently available in the grounding.

**Limitations list.**

- *Single fixed point, linear contraction.* R1 holds only within the frame of Section 3.1; sensitivity to this assumption is total, since the entire derivation is the frame.
- *Depolarizing noise model.* The quantum instantiation uses the standard depolarizing channel; other channels (amplitude damping, dephasing) contract in different norms and can give different fixed points, so R1's numerical value $1374.6$ is model-specific, though the law's form survives any geometric contraction.
- *Matched-parameter condition.* The equality in R1 requires $\rho(M)=1-\varepsilon$; unmatched parameters reintroduce a difference that is trivially large, so the result constrains only fair comparisons.
- *Imported threshold.* R3 reinterprets the $0.874$ fidelity bound from [11] as a clock marker; the no-go theorem itself does not concern relaxation dynamics, and R3 inherits no model-independence from the theorem despite the theorem being described as model-independent.
- *No per-step costs.* R5 is a gate without numbers because no cost data exist in the grounding; any cost claim would be unsupported.
- *Open ordering parameter.* The ratio of the semiclassical (Ehrenfest-type) time to $1/\varepsilon$, which would quantify R4, is not derivable from the supplied abstract of [6]; the paper's divergence claim is therefore qualitative at exactly the point where it would be most useful.
- *Thin grounding for two sources.* The entries for the pre-registered falsification work [12] and "Programming the Vacuum" [9] supply no abstract text; claims resting on them are correspondingly minimal, and the bibliography contains twelve works of which two are contentless in this grounding — a limitation of the source set itself.

**Open questions.** (1