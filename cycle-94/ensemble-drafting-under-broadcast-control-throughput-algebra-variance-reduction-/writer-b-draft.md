# Broadcast Control of Linear Ensembles: Vandermonde Conditioning and the Cost of Parameter Spread

## Abstract

Ensemble control studies populations of structurally identical dynamical systems that differ only in a parameter, driven by a single broadcast input signal; the controller cannot address individual systems. This paper analyzes the exact finite-horizon reachability of a canonical linear ensemble — $N$ scalar single-input integrators $\dot{x}_i = \lambda_i x_i + u(t)$ with distinct drift parameters $\lambda_i$ and one common input $u$ — and shows that the reachability map is a generalized Vandermonde matrix whose determinant factors into a nonzero Vandermonde product in $q_i = e^{-\lambda_i}$. We derive the determinant in closed form and evaluate it numerically for a well-separated parameter triple $(\lambda_1,\lambda_2,\lambda_3) = (0,1,2)$, obtaining $\det M \approx -14.01$, and for a clustered triple with spread $\epsilon = 0.01$, obtaining $\det M \approx -2.028 \times 10^{-6}$. From the singular-value inequality $\sigma_{\min}^3 \le |\det M|$ we derive a guaranteed lower bound on the worst-case control norm for unit-norm targets: at least $0.415$ in the separated case but at least $79.0$ in the clustered case, a degradation factor of approximately $190 \approx \epsilon^{-3}$ up to constants. We connect this conditioning barrier to moment-based and Lie-group ensemble control, to decoupling-by-symmetry arguments in perturbation theory, and to spanning-set constructions in the cited literature, and we state explicit assumptions under which a continuum ensemble requires $N \ge L/\epsilon + 1$ point systems to resolve to accuracy $\epsilon$.

## 1. Introduction

A defining difficulty of ensemble control is that the control signal is broadcast: one waveform $u(t)$ drives every member of a population simultaneously, and the only handle on individual behavior is the member's own parameter value. The literature frames this in two equivalent ways. Moment-based ensemble control treats the population in the limit of a continuum of structurally identical systems with parametric variations, and emphasizes that such systems are severely underactuated and lack comprehensive state feedback, which raises significant challenges for analysis and design [5]. Ensemble control on Lie groups likewise arises from quantum control, robotics, and brain medicine, and stresses that in many applications control can only be implemented at the population level through broadcasting an input signal to all systems [8].

Both framings raise the same quantitative question that this paper answers for a canonical linear case: *when the parameters of the population cluster together, how expensive does exact targeting become?* Intuition suggests degradation, but the mechanism and its scaling have a clean algebraic origin. For a finite ensemble of scalar systems with distinct drift parameters, exact reachability on a finite horizon is governed by a matrix whose determinant is a Vandermonde product in $q_i = e^{-\lambda_i}$; Vandermonde determinants are famously ill-conditioned under node clustering, and this ill-conditioning translates directly into control amplitude and noise-robustness costs.

The contributions are:

1. A closed-form derivation of the finite-horizon reachability matrix $M$ for the ensemble $\dot{x}_i = \lambda_i x_i + u(t)$, its factorization as a scaled Vandermonde determinant, and the resulting exact criterion for controllability: the parameters $\lambda_i$ must be pairwise distinct.
2. Fully explicit numerical evaluations for a separated triple and a clustered triple, with every arithmetic step shown, yielding determinant values $-14.01$ and $-2.028 \times 10^{-6}$ respectively.
3. A guaranteed worst-case control-cost lower bound derived from $\sigma_{\min}^3 \le |\det M|$, quantifying the price of parameter spread: a factor of approximately $190$ between the two configurations.
4. A labeled projection, under stated smoothness assumptions, giving the number of point systems $N \ge L/\epsilon + 1$ needed to resolve a continuum ensemble to accuracy $\epsilon$.

Throughout, "ensemble" means a family of systems indexed by a parameter; "broadcast input" means a single scalar signal applied identically to all members; "reachability matrix" is defined precisely in Section 3.

## 2. Background and Related Work

We discuss all twelve works of the supplied bibliography, in its exact order and numbering.

**[1] Chaos in DNA inversions (Draft paper).** This draft paper proves that the inversion process occurring in DNA mutations is chaotic in the sense of Devaney's theory. Its relevance here is methodological rather than direct: it is an example of taking a population-level biological transformation (inversions across a genome) and subjecting it to a rigorous dynamical-systems classification, the same discipline of exact classification that we apply to ensemble reachability.

**[2] DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments.** This work revisits Gentzen's 1936 proof of the consistency of Peano Arithmetic, providing a modified version based on Gödel's reformulation with additional details and minor corrections necessary to definitively prove the well-foundedness of the cut-elimination argument in a constructive environment. We cite it as a model of the standard this paper aspires to in miniature: every step of a delicate argument (there, well-foundedness; here, determinant non-degeneracy and singular-value bounds) made explicit and checkable.

**[3] TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs.** Speculative decoding accelerates LLM inference by quickly generating draft tokens and verifying them in parallel; this work extends the approach to Large Vision-Language Models, which process both image and text prompts, and benchmarks existing inference methods with small draft models on 11 datasets across diverse settings (the supplied abstract is truncated at this point). It is an "ensemble of drafters" in a different sense from ours — multiple draft models coordinated at test time rather than parameter-varied copies of one plant — but it shares the structural problem of combining heterogeneous members under a shared verification budget, and we use it to mark the boundary of our scope.

**[4] Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes.** Perturbation theory of vacuum spherically-symmetric spacetimes is a crucial tool for understanding black-hole perturbation dynamics; spherical symmetry permits an expansion in scalar, vector, and tensor harmonics, and the resulting perturbative equations decouple for modes with different parity and different harmonic numbers (the supplied abstract is truncated thereafter). This decoupling-by-symmetry is the exact phenomenon our Vandermonde factorization exhibits in miniature: structure in the parameter labels splits a coupled problem into independent, analyzable pieces.

**[5] Moment-Based Ensemble Control.** This work addresses control of a large population — in the limit a continuum — of structurally identical dynamical systems with parametric variations, a pervasive task in science and engineering, and identifies the severely underactuated nature of ensemble systems and the inability to avail comprehensive state feedback as the central challenges. Our Section 3 is a finite-dimensional, exactly solvable instance of precisely this setting, and our Section 4 projection on resolving a continuum by $N$ point systems is a bridge between the continuum view of [5] and finite ensembles.

**[6] Prescriptive Master Integrals of Maximal Weight at Two Loops.** This work constructs a spanning set of individually pure, planar master integrals involving massless particles in four dimensions including all maximal-weight contributions at two loops, such that every independent infrared-divergent region is individually matched by specific masters while all other masters are manifestly finite in four dimensions. The design pattern — a spanning set in which each hard direction is matched by a dedicated basis element — is the same pattern our moment/bracket counting follows: independent parameter directions must be matched by independent control functionals, and the determinant measures whether the matching is complete.

**[7] Asymptotic of Bergman Kernel (Master Thesis).** This thesis gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle at points where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi-classical symbol space and related symbolic calculus inspired by recent work of Hsiao and Savale (the supplied abstract is truncated at this point). The "local spectral gap" condition is conceptually parallel to our distinctness-of-$\lambda_i$ condition: a spectral non-degeneracy hypothesis that makes an otherwise degenerate asymptotic problem tractable.

**[8] Ensemble Control on Lie Groups.** This work treats problems involving control of large ensembles of structurally identical dynamical systems, arising in numerous scientific areas from quantum control and robotics to brain medicine, where control can only be implemented at the population level by broadcasting an input signal to all systems (the supplied abstract is truncated within this statement). This is the field-defining framing for our problem; our broadcast scalar input $u(t)$ is the simplest instance of the population-level signals it describes.

**[9] QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel.** This document describes a shared adelic kernel structured as valuation → tree boundary → Ostrowski → adeles, applying all 7 corrections (C1–C7) from a 2026-07-25 red-team audit and restructured kernel-first with an honest kernel-membership table and mandatory symmetry sections. We cite it as the methodological environment in which the present preprint was produced, and note its insistence on honest membership tables and symmetry sections as a norm this paper adopts (our Section 4 shows every arithmetic step; our Discussion states failure modes explicitly).

**[10] NUMERATA: A Multi-Axis Framework for Evaluating Numeral Systems.** NUMERATA v2.0 extends an 8-axis framework with Distinction-Based Primality (WP0.3, a 9th axis) and meta-analysis validation with MCS $= 0.875$ and 5/5 predictions confirmed; its sunburst notation makes primality visually immediate. We reference it only as a companion QNFO artifact illustrating multi-axis evaluation of representational systems; no numerical claim of this paper depends on it beyond the quoted MCS value, which we do not use.

**[11] QNFO: Connecting Geometrogenesis and Biogenesis.** The supplied bibliography entry for this work contains no summary text. We therefore make no claim about its content and note only that its title indicates a proposed connection between geometrogenesis and biogenesis within the QNFO corpus; it plays no role in our derivations.

**[12] QNFO: Kappa/SIIT Cross-Validation: Exact Reproduction of Standard Model 1-Loop β-Functions and Resolution of the Harmonic-Paradigm Tension.** This work reports a direct mathematical cross-validation of the Kappa / Scale-Invariant Information Thermodynamics framework (Quni-Gudzinas, 2025, Zenodo 17218944/17230397) against the Standard Model's known 1-loop renormalization-group β-functions, through the single definition $g_{\text{eff}} = g_0 \kappa$ (the supplied abstract is truncated within this definition). Its pattern — validating a framework by exact reproduction of known quantitative targets — is the pattern our Section 4 follows: the Vandermonde factorization is validated by exact numerical reproduction of the determinant for a case where all factors are computable by hand.

## 3. Methods

### 3.1 System class

We consider $N$ scalar systems

$$\dot{x}_i(t) = \lambda_i x_i(t) + u(t), \qquad i \in \{1, \dots, N\},$$

with a single broadcast scalar input $u(t)$, common horizon $T > 0$, and initial conditions $x_i(0) = 0$. The parameters $\lambda_i \in \mathbb{R}$ are the only distinguishing features of the members. This is the linearized, scalar-state core of the broadcast-control setting of [8] and the finite-ensemble restriction of the continuum setting of [5].

### 3.2 Reachability map

The solution at time $T$ is

$$x_i(T) = \int_0^T e^{\lambda_i (T - t)} u(t) \, dt.$$

We restrict $u$ to be piecewise constant on $N$ equal intervals of length $\Delta = T/N$, with $u(t) = u_j$ on $[t_{j-1}, t_j)$, $t_j = j\Delta$. This restriction is without loss for the controllability question: if the full functional map is surjective, some piecewise-constant $u$ already reaches any reachable point, and conversely piecewise-constant controls are admissible inputs. Define $u = (u_1, \dots, u_N)^{\top}$ and $x = (x_1(T), \dots, x_N(T))^{\top}$. Then

$$x = M u, \qquad M_{ij} = \int_{(j-1)\Delta}^{j\Delta} e^{\lambda_i (T - t)} \, dt.$$

For $\lambda_i \neq 0$,

$$M_{ij} = \frac{e^{\lambda_i(T - j\Delta)} - e^{\lambda_i(T - (j-1)\Delta)}}{\lambda_i} = \frac{1 - e^{-\lambda_i \Delta}}{\lambda_i} \, e^{\lambda_i (T - j\Delta)},$$

and for $\lambda_i = 0$ the factor is interpreted by its limit $d_i = \Delta$. Writing $d_i = \frac{1 - e^{-\lambda_i \Delta}}{\lambda_i}$ (with $d_i \to \Delta$ as $\lambda_i \to 0$) and $q_i = e^{-\lambda_i \Delta}$, we have

$$M_{ij} = d_i \, e^{\lambda_i T} \, q_i^{\,j}.$$

### 3.3 Determinant factorization

Row-scaling by $d_i e^{\lambda_i T} > 0$ and using the Vandermonde formula for the matrix $[q_i^{\,j}]_{i,j=1}^{N}$ (exponents $1, \dots, N$),

$$\det M = \left( \prod_{i=1}^{N} d_i e^{\lambda_i T} \right) \left( \prod_{i=1}^{N} q_i \right) \prod_{1 \le i < j \le N} (q_j - q_i).$$

Since $d_i > 0$, $e^{\lambda_i T} > 0$, $q_i > 0$, we obtain the exact controllability criterion:

$$\det M \neq 0 \iff q_i \neq q_j \ \forall\, i \neq j \iff \lambda_i \neq \lambda_j \ \forall\, i \neq j.$$

The ensemble is exactly controllable (on the piecewise-constant class, hence on the full class) if and only if the parameters are pairwise distinct. Degeneracy of the determinant is therefore a