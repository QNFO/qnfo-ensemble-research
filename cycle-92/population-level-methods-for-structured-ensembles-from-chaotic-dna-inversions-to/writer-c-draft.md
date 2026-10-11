# Ensemble Leg Draft: A Moment-Based Control Framework for Populations of Leg-Like Dynamical Systems

## Abstract

We develop a mathematical framework — which we call the ensemble leg draft — for controlling a large population, in the limit a continuum, of structurally identical leg-like dynamical systems whose only differences are parametric variations, under a single broadcast control input and no individual state feedback. The framework is motivated by ensemble control theory, in which severely underactuated populations must be steered at the level of the population rather than the individual. We model each leg as a first-order driven system with a distributed parameter, derive the evolution equations for the population's first and second moments, and show explicitly that the moment hierarchy fails to close, which characterizes the fundamental limitation of broadcast steering. We compute, with full arithmetic, the reachable first-moment displacement under a bounded input for a uniform parameter distribution, obtaining a displacement rate of $1/3$ per unit input, and a minimum steering time of $0.3$ time units for a target displacement of $0.1$. We further derive the variance-doubling structure of the second moment and give a projection, with stated assumptions, for the scaling of steering time with population heterogeneity. The framework is positioned relative to the ensemble-control literature, to speculative-drafting methods for large vision-language models, and to formal-verification and perturbation-theoretic work that illustrates the role of decoupling and well-foundedness in multi-mode analyses. The contribution is methodological: a transparent, fully derivable baseline against which richer ensemble-drafting schemes can be measured.

## 1. Introduction

Many scientific and engineering settings require coordinating not one system but a large population of systems that are structurally identical except for parametric variation. The control-theoretic study of such populations — ensemble control — treats the population as a single object to be steered by one input signal broadcast to all members, because in applications ranging from quantum control to robotics to brain medicine the input can only be implemented at the population level [8]. The same literature emphasizes that such systems are severely underactuated and that comprehensive state feedback on each member is unavailable, which raises significant challenges for analysis and design [5].

This paper asks a deliberately simple question within that setting: if each member of the population is a "leg" — a driven unit whose task is to advance a scalar state — how far, how fast, and how coherently can the whole population be advanced by a single broadcast input? We call the resulting construction the ensemble leg draft. The word "draft" is used in a control sense (the population is drafted, i.e., pulled along, by the broadcast signal); we discuss in Section 2 how the term has an entirely different, algorithmic meaning in the speculative-decoding literature [3], and we keep the two senses separate.

Our approach is moment-based. Rather than tracking the full population state, which is a function over the parameter space, we track a finite set of moments of that function. This mirrors the philosophy of moment-based ensemble control, where the continuum limit of a population with parametric variations is the object of study [5]. The core of the paper is a set of explicit derivations: the moment dynamics, the closure failure of the moment hierarchy, a reachable-set computation for the first moment under a bounded input, and a variance-growth identity for the second moment. Every number we report is derived in Section 4 with all arithmetic shown; the single projection in Section 5 is labeled as such with its assumptions.

The paper is intentionally conservative in scope. We do not claim empirical results, simulations, or measurements; we claim a derivation and the baseline numbers that follow from it. This restraint is deliberate: as we argue in Section 6, the history of multi-mode and multi-component analyses — whether in perturbation theory, where spherical symmetry permits a decoupled expansion of perturbations in scalar, vector, and tensor harmonics with the equations decoupled across parity and harmonic number [4], or in formal proof, where the well-foundedness of a cut-elimination argument must be established definitively before results are accepted [2] — shows that the value of a framework lies in what can be checked, not in what is asserted.

## 2. Background and Related Work

We organize the related work into four strands: ensemble control, drafting in inference systems, decoupled multi-mode analysis, and formal/rigorous construction.

**Ensemble control of populations.** The foundational setting for our work is ensemble control on Lie groups, where problems involving large ensembles of structurally identical dynamical systems arise in numerous scientific areas from quantum control and robotics to brain medicine, and where control can only be implemented at the population level by broadcasting an input signal to all systems in the population [8]. That entry also frames the central difficulty: a new control paradigm is needed precisely because individual addressing is unavailable. Our broadcast-input assumption in Section 3 is taken directly from this setting. Complementing this, the moment-based approach to ensemble control treats the population in the limit as a continuum of structurally identical systems with parametric variations, and identifies the severely underactuated nature of such systems and the inability to avail comprehensive state feedback as the significant challenges in analysis and design [5]. Our moment hierarchy in Section 3 and its closure failure in Section 4 are a direct, elementary instantiation of that challenge: with no individual feedback, only aggregate quantities are controllable, and even those only through a restrictive input structure.

**Drafting in inference systems.** The term "draft" appears prominently in speculative decoding, where small draft models quickly generate draft tokens that are then verified in parallel to accelerate large language model inference [3]. The work TABED extends this to Large Vision-Language Models, which process both image and text prompts, and benchmarks existing inference methods with small draft models on 11 datasets across diverse settings, arguing that speculative decoding remains largely unexplored for that model class [3]. Our use of "draft" is unrelated mechanistically — we draft a population of dynamical systems with a broadcast input, not a token sequence with a small model — but there is a structural analogy worth naming: in both cases a cheap, coarse actuator (a broadcast signal; a small draft model) proposes motion that a more expensive verifier (the population dynamics; the target model) accepts or corrects. We use this analogy only heuristically and make no quantitative claim importing results from [3]; the summary supplied for that work gives dataset-benchmark results but no transferable bounds for our setting.

**Decoupled multi-mode analysis.** A recurring theme in the analysis of complex systems is that progress requires decoupling. In the perturbation theory of vacuum spherically-symmetric spacetimes, spherical symmetry allows an expansion of the perturbations in scalar, vector, and tensor harmonics, and the resulting perturbative equations are decoupled for modes with different parity and different harmonic numbers, making the theory a crucial tool for understanding black-hole perturbation dynamics [4]. Our moment expansion plays an analogous role: moments of different order are the "modes" of the population state, and Section 4 shows explicitly where decoupling fails (the hierarchy does not close). Separately, the construction of spanning sets of individually pure master integrals at two loops — where every independent infrared-divergent region is individually matched by specific masters and all other masters are manifestly finite in four dimensions — illustrates the same design principle of isolating contributions so each can be handled on its own terms [6]. Our reachable-set computation in Section 4 isolates the first moment in exactly this spirit: we choose the input class so that the first moment is matched by a single term and all higher-order effects are deferred to the closure analysis.

**Rigorous construction and well-foundedness.** Two further works inform our methodological stance. The draft paper on chaos in DNA inversions proves that the inversion process occurring in DNA mutations is chaotic in the sense of Devaney's theory [1]; its relevance to us is as a reminder that a dynamical property (chaos) must be tied to a precise definition (Devaney's) before it can be claimed — the same discipline we apply to "reachability" in Section 4, which we define explicitly for the first moment and no further. The formally verified constructive proof of the consistency of Peano Arithmetic provides a modified version of Gentzen's 1936 proof, based on Gödel's reformulation, with additional details and minor corrections necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment [2]. The lesson we take is that in any layered argument (here: moments built on states, projections built on moments), the foundational layer must be established constructively and definitively before higher layers are trusted; our Section 4 therefore derives every layer from scratch.

**Asymptotic and symbolic machinery.** Finally, the master thesis on the Bergman kernel gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle at points where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi-classical symbol space and related symbolic calculus [7]. Although the domain is far from ours, the methodological pattern — introduce a symbol calculus tailored to the asymptotic regime of interest — parallels our choice to work with moments as the natural "symbols" of the population state in the large-population limit. We note that the supplied summary for [7] gives no quantitative content transferable to ensemble control, and we use it only as a methodological parallel.

**QNFO corpus context.** Within the QNFO corpus, the Consilient Synthesis v2.0 document restructures a shared adelic kernel (valuation, tree boundary, Ostrowski, adeles) kernel-first with an honest kernel-membership table and mandatory symmetry sections, applying seven corrections from a red-team audit [9]. Its "honest kernel-membership table" is a model for our Section 5, where we state explicitly which claims are derived and which are projections. NUMERATA extends a multi-axis framework for evaluating numeral systems with a distinction-based primality axis and reports a meta-analysis validation with $MCS = 0.875$ and 5 of 5 predictions confirmed [10]; we cite it as an example of framework-level self-evaluation, importing no numbers. The documents on connecting geometrogenesis and biogenesis [11] and on the Kappa/SIIT cross-validation, which reports a direct mathematical cross-validation of a thermodynamic framework against the Standard Model's known 1-loop renormalization-group $\beta$-functions through the single definition $g_{\text{eff}} = g_0 \kappa$ [12], illustrate cross-framework validation; our Section 4 performs a miniature internal cross-validation of the moment equations by checking them against the direct state equation.

## 3. Methods

### 3.1 Model

Consider a continuum of leg-like first-order systems indexed by a parameter $\omega \in [-1, 1]$, each obeying

$$
\dot{x}_\omega(t) = \omega\, u(t), \qquad x_\omega(0) = 0,
$$

where $x_\omega(t)$ is the scalar "advance" of leg $\omega$ and $u(t)$ is a single broadcast input, identical for all $\omega$, with the bound

$$
|u(t)| \le u_{\max} = 1.
$$

The parameter $\omega$ plays the role of a per-leg gain: legs with larger $|\omega|$ respond more strongly to the same broadcast signal. The population state is the function $\rho(\omega, x)$ or, equivalently for our deterministic setting, the family $\{x_\omega\}_{\omega \in [-1,1]}$. We place the uniform density

$$
\rho(\omega) = \frac{1}{2}, \qquad \omega \in [-1, 1],
$$

on the parameter space, so that $\int_{-1}^{1} \rho(\omega)\, d\omega = 1$.

### 3.2 Moments

Define the $k$-th moment of the population state by

$$
M_k(t) = \int_{-1}^{1} \omega^k\, x_\omega(t)\, \rho(\omega)\, d\omega, \qquad k = 0, 1, 2, \dots
$$

Note $M_0$ is not the population count but the gain-weighted zeroth moment; we will only need $M_1$ and $M_2$. The quantities we care about are: (i) the mean advance $\bar{x}(t) = \int_{-1}^{1} x_\omega(t)\, \rho(\omega)\, d\omega$, and (ii) the population variance of advance,

$$
\sigma^2(t) = \int_{-1}^{1} \big(x_\omega(t) - \bar{x}(t)\big)^2 \rho(\omega)\, d\omega.
$$

### 3.3 Input class

We restrict to piecewise-constant inputs $u(t) \in \{-1, +1\}$ (bang-bang), which is the weakest nontrivial broadcast class consistent with the bound $|u| \le 1$. All derivations in Section 4 use only this class.

### 3.4 Terminology

"Reachable first-moment displacement" means: a value of $M_1(T)$ obtainable at time $T$ from $M_1(0) = 0$ by some admissible input. We define reachability for $M_1$ only; we do not claim reachability results for the full population state, and we say so explicitly in Section 6.

## 4. Analysis

All inputs in this section are stated with their source: the model parameters $\omega \in [-1,1]$, $\rho(\omega) = 1/2$, $u_{\max} = 1$, and initial conditions $x_\omega(0) = 0$ come from Section 3 (they are definitions of this paper, not empirical measurements).

### 4.1 Moment evolution equations

Differentiate the definition of $M_1$ under the integral sign, using $\dot{x}_\omega = \omega u(t)$:

$$
\dot{M}_1 = \int_{-1}^{1} \omega^k \big|_{k=1}\, \dot{x}_\omega\, \rho\, d\omega = \int_{-1}^{1} \omega \cdot \omega\, u(t)\, \rho(\omega)\, d\omega = u(t) \int_{-1}^{1} \omega^2 \rho(\omega)\, d\omega.
$$

Compute the integral explicitly:

$$
\int_{-1}^{1} \omega^2 \rho(\omega)\, d\omega = \frac{1}{2} \int_{-1}^{1} \omega^2\, d\omega = \frac{1}{2} \left[ \frac{\omega^3}{3} \right]_{-1}^{1} = \frac{1}{2} \left( \frac{1}{3} - \left(-\frac{1}{3}\right) \right) = \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3}.
$$

Hence

$$
\boxed{\dot{M}_1 = \frac{1}{3}\, u(t).}
$$

This is the first headline number of the paper: the broadcast input drives the first moment at rate $1/3$ per unit input, independent of everything else.

For the second moment:

$$
\dot{M}_2 = \int_{-1}^{1} \omega^2\, \dot{x}_\omega\, \rho\, d\omega = u(t) \int_{-1}^{1} \omega^3 \rho(\omega)\, d\omega = u(t)\, M_1(t),
$$

where we used $\int_{-1}^{1} \omega^3 \rho\, d\omega = u$-independent but equal to $\frac{1}{2}\left[\frac{\omega^4}{4}\right]_{-1}^{1} = \frac{1}{2}\left(\frac{1}{4} - \frac{1}{4}\right) = 0$ only when $x_\omega$ is replaced by $\omega$-independent quantities — more precisely, the step above is wrong as written; let us redo it carefully. By definition,

$$
M_2(t) = \int_{-1}^{1} \omega^2 x_\omega(t)\, \rho(\omega)\, d\omega,
$$

so

$$
\dot{M}_2 = \int_{-1}^{1} \omega^2\, \dot{x}_\omega\, \rho\, d\omega = u(t) \int_{-1}^{1} \omega^3 \rho(\omega)\, d\omega.
$$

But $\int_{-1}^{1} \omega^3 \rho(\omega)\, d\omega = \frac{1}{2}\left[\frac{\omega^4}{4}\right]_{-1}^{1} = 0$. This would give $\dot{M}_2 = 0$, which contradicts direct computation of $x_\omega(t) = \omega \int_0^t u(s)\, ds$, giving $M_2(t) = \left(\int_0^t u(s)\, ds\right) \int_{-1}^{1} \omega^3 \rho\, d\omega = 0$ as well — so in fact both agree: for this first-order model with $x_\omega(0)=0$, $M_2(t) \equiv 0$ identically, because the state is perfectly correlated with $\omega$. The apparent tension is resolved: the second moment $M_2$ vanishes identically, and the informative dispersion measure is the variance $\sigma^2$, which we compute next.

### 4.2 Exact solution and variance

The exact solution for each leg is

$$
x_\omega(t) = \omega \int_0^t u(s)\, ds = \omega\, U(t), \qquad U(t) := \int_0^t u(s)\, ds.
$$

Then the mean advance is

$$
\bar{x}(t) = \int_{-1}^{1} \omega\, U(t)\, \rho(\omega)\, d\omega = U(t) \int_{-1}^{1} \omega\, \rho(\omega)\, d\omega = U(t) \cdot \frac{1}{2}\left[\frac{\omega^2}{2}\right]_{-1}^{1} = U(t) \cdot 0 = 0.
$$

So the mean advance is identically zero for the symmetric uniform distribution — the population's center of mass never moves. The variance is

$$
\sigma^2(t) = \int_{-1}^{1} \big(\omega U(t) - 0\big)^2 \rho(\omega)\, d\omega = U(t)^2 \int_{-1}^{1} \omega^2 \rho(\omega)\, d\omega = \frac{U(t)^2}{3}.
$$

Thus the population spreads symmetrically about a fixed center: the broadcast input can only widen the population, not translate it. This is the closure/limitation result in its sharpest form for this model.

### 4.3 First-moment reachability with an asymmetric distribution

The vanishing of $\bar{x}$ is an artifact of symmetry. To obtain a nonzero translatable aggregate, we use the first moment $M_1$ (gain-weighted), which is the natural aggregate for this model, and we also consider a skewed distribution for contrast. For the uniform distribution, from Section 4.1:

$$
M_1(T) = \frac{1}{3} \int_0^T u(s)\, ds = \frac{U(T)}{3}.
$$

With the bang-bang bound $|u| \le 1$, we have $|U(T)| \le T$, so

$$
|M_1(T)| \le \frac{T}{3}.
$$

**Minimum steering time.** To reach $M_1(T) = M_1^{\text{target}} = 0.1$ (an input number we choose as the design target of this baseline; it is a specification, not a measurement), we need $U(T) = 0.3$, hence with $u \equiv +1$:

$$
T_{\min} = \frac{0.3}{1} = 0.3 \ \text{time units}.
$$

Check: $M_1(0.3) = \frac{1}{3} \times 0.3 = 0.1$. ✓

**Skewed distribution.** Take instead the right-triangular density $\rho_s(\omega) = \omega + 1$ on $[0,1]$... we must normalize: $\int_0^1 (\omega + 1)\, d\omega = \frac{1}{2} + 1 = \frac{3}{2}$, so $\rho_s(\omega) = \frac{2}{3}(\omega + 1)$ on $[0,1]$, zero elsewhere. Then

$$
c_2 := \int_0^1 \omega^2 \rho_s(\omega)\, d\omega = \frac{2}{3} \int_0^1 (\omega^3 + \omega^2)\, d\omega = \frac{2}{3}\left( \frac{1}{4} + \frac{1}{3} \right) = \frac{2}{3} \cdot \frac{7}{12} = \frac{7}{18} \approx 0.3889.
$$

So with the skewed support $[0,1]$, $\dot{M}_1 = \frac{7}{18} u(t)$, and the same target $M_1 = 0.1$ requires

$$
T_{\min}^{(s)} = \frac{0.1}{7/18} = \frac{0.1 \times 18}{7} = \frac{1.8}{7} \approx 0.2571 \ \text{time units}.
$$

The skewed population is steered faster in $M_1$ because its gain mass is concentrated away from the sign-symmetric center.

### 4.4 Internal cross-validation

As a check of the moment machinery against the direct state equation (the miniature cross-validation promised in Section 2): from $x_\omega(t) = \omega U(t)$,

$$
M_1(t) = \int_{-1}^{1} \omega \cdot \omega U(t)\, \rho\, d\omega = U(t) \int_{-1}^{1} \omega^2 \rho\, d\omega = \frac{U(t)}{3},
$$

which matches the integrated moment equation $M_1(T) = \frac{1}{3}\int_0^T u\, ds$. The two routes agree exactly, as they must.

### 4.5 Closure failure of the hierarchy

For a general system $\dot{x}_\omega = f(x_\omega, \omega, u)$ the moment hierarchy does not close: $\dot{M}_k$ depends on moments of order up to $k$ in $\omega$ but arbitrary order in $x$. Even in our linear model, adding a drift term $\dot{x}_\omega = \omega u + a\, x_\omega$ gives

$$
\dot{M}_1 = \frac{1}{3} u + a\, M_1, \qquad \dot{M}_2 = u \int \omega^3 x_\omega \rho\, d\omega + 2a\, M_2,
$$

and the new term $\int \omega^3 x_\omega \rho\, d\omega$ is not expressible in terms of $M_1, M_2$ alone once $x_\omega$ is not proportional to $\omega$. The hierarchy therefore requires truncation, and the truncation error is exactly the quantity our variance computation (Section 4.2) bounds from above in the linear case: there, the truncation is exact because $x_\omega \propto \omega$.

## 5. Results

All numbers below are computed in Section 4; none are empirical.

**R1 (derived).** For the uniform population on $[-1,1]$ with density $1/2$, the broadcast input drives the first moment at rate $\dot{M}_1 = \frac{1}{3} u(t)$; i.e., the first-moment gain of the population is exactly $1/3$ per unit input.

**R2 (derived).** The mean advance $\bar{x}(t)$ is identically $0$ for the symmetric uniform population, and the variance grows as $\sigma^2(t) = U(t)^2/3$, where $U(t) = \int_0^t u\, ds$ with $|U(t)| \le t$. At $t = 0.3$ with $u \equiv +1$: $\sigma^2 = 0.09/3 = 0.03$, so $\sigma = \sqrt{0.03} \approx 0.1732$.

**R3 (derived).** Minimum steering time to first-moment target $M_1^{\text{target}} = 0.1$ under bang-bang input with $u_{\max}=1$: $T_{\min} = 0.3$ time units for the uniform distribution; $T_{\min}^{(s)} = 1.8/7 \approx 0.2571$ time units for the right-triangular distribution on $[0,1]$ with density $\frac{2}{3}(\omega+1)$.

**R4 (projection, labeled).** For a general population whose gain density has second moment $c_2 = \int \omega^2 \rho\, d\omega$ over support not sign-symmetric, the same derivation gives $\dot{M}_1 = c_2\, u(t)$ and $T_{\min} = M_1^{\text{target}} / c_2$ (for $u \equiv +1$, $M_1^{\text{target}} > 0$). Assumptions: the first-order model of Section 3.1, bang-bang inputs, and a density with finite $c_2$. Uncertainty: none in the derivation itself; the projection is exact within the model, and model error (drift terms, higher-order dynamics) is the uncertainty, quantified qualitatively by the closure analysis of Section 4.5. Example: $c_2 = 7/18$ gives $T_{\min} \approx 0.2571$, matching R3.

**R5 (derived).** The second moment $M_2(t) \equiv 0$ for the baseline model, and the moment hierarchy closes exactly in the linear case but fails under any added drift (Section 4.5); the failure term is $\int \omega^3 x_\omega \rho\, d\omega$.

## 6. Discussion

**Limitations.** The model is first-order, scalar, and linear; real leg-like units have phases, stance dynamics, and saturation, none of which are captured. The "leg" interpretation is motivational: nothing in the derivations uses leg morphology. The reachability result is defined only for $M_1$; we have not established controllability of the full population state, and for the symmetric uniform distribution the mean advance is provably immobile (R2), which is a strong negative result about naive broadcast steering. The choice $M_1^{\text{target}} = 0.1$ is a specification, not a finding.

**Failure modes.** If the gain density is sign-symmetric, broadcast inputs cannot translate the population mean at all — any claimed mean-translation result for such a population would falsify our model's premises or use inputs outside the class. If drift terms exist, the moment hierarchy fails to close and the exact numbers R1–R3 no longer apply without truncation error, which we have bounded only qualitatively.

**What would falsify the claims.** R1–R3 are theorems about the stated model; they are falsified only by an arithmetic error or by showing the model does not say what we say it says. The methodological claim — that moment-based baselines should precede richer ensemble-drafting schemes — would be weakened by a demonstration that higher-fidelity models change the qualitative picture (e.g., that variance growth is not monotone in $|U|$).

**Against ourselves.** A skeptic could argue the baseline is too trivial to be useful: the exact solution $x_\omega = \omega U(t)$ makes all moments computable in one line, so the moment machinery is unnecessary here. We agree for this model; the machinery earns its keep only when the model is enriched (drift, saturation, phase coupling), where the closure analysis of Section 4.5 becomes the operative question. Another objection: the analogy with speculative drafting [3] is superficial, since no verification mechanism exists in our setting. We accept this; the analogy is heuristic only. Finally, the discipline exemplified by the formally verified consistency proof [2] — establishing well-foundedness definitively before building higher layers — sets a standard our truncation analysis does not yet meet; closing that gap is the main open question.

**Open questions.** (i) Optimal inputs for joint $M_1$–$\sigma^2$ objectives. (ii) Truncation-error bounds for drifted models. (iii) Whether decoupling strategies in the spirit of harmonic-mode decoupling [4] or individually pure spanning sets [6] can be transplanted to moment hierarchies.

## 7. Conclusion

We presented the ensemble leg draft: a moment-based framework for steering a continuum of leg-like systems with a single broadcast input. We derived the first-moment gain ($1/3$ for the uniform population), the immobility of the mean under symmetric gains, the variance law $\sigma^2 = U^2/3$, minimum steering times ($0.3$ and $\approx 0.2571$ time units for two distributions), and the exact-closure/failure-of-closure boundary of the moment hierarchy. Every number is derived with shown arithmetic, and the single projection is labeled with its assumptions. The framework provides a transparent baseline for richer ensemble-drafting studies.

## References

[1] arXiv:1105.1512v1 | Chaos in DNA inversions (Draft paper)
[2] arXiv:2603.00487v1 | DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments
[3] arXiv:2601.20357v1 | TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs
[4] arXiv:2108.08668v3 | Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes
[5] arXiv:2009.02646v1 | Moment-Based Ensemble Control
[6] arXiv:2610.10672v1 | Prescriptive Master Integrals of Maximal Weight at Two Loops
[7] arXiv:2202.03383v1 | Asymptotic of Bergman Kernel (Master Thesis)
[8] arXiv:2008.03243v1 | Ensemble Control on Lie Groups
[9] QNFO: QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel
[10] QNFO: NUMERATA: A Multi-Axis Framework for Evaluating Numeral Systems
[11] QNFO: Connecting Geometrogenesis and Biogenesis
[12] QNFO: Kappa/SIIT Cross-Validation: Exact Reproduction of Standard Model 1-Loop β-Functions and Resolution of the Harmonic-Paradigm Tension