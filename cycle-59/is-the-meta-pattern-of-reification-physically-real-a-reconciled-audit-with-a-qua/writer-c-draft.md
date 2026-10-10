# Reification and Its Costs: A Framework for Asking Whether an Abstract Object Is Physically Real

## Abstract

We address the question posed by the research prompt "Re-entry from 10.5281/zenodo.19605445: something physically real?" — that is, under what conditions a reified abstraction (a number, a constraint, a mathematical identity) can be said to be physically real. We propose a three-test framework — instantiation, intervention, and invariance — that converts the vague question "is $X$ physically real?" into a decidable checklist with explicit costs. We apply the framework to three case studies drawn from the supplied literature: fusion device design, where magnetohydrodynamic stability criteria are reified as design constraints [4]; turbulence model uncertainty, where physically constrained eigenspace perturbations discipline reified model forms [8]; and the adelic completion of the rationals, where a single identity links incompatible completions of $\mathbb{Q}$ [10]. We derive a quantitative "reification cost" metric: for a constraint with $n$ independent physical realizations each of relative tolerance $\epsilon$, the joint failure probability scales as $p_{\mathrm{fail}} \approx 1 - (1 - \epsilon)^{n}$, which we evaluate explicitly for representative parameters. We conclude that physical reality is not a binary property of an abstraction but a graded property of the coupling between the abstraction and an intervention-capable apparatus, and that the re-entry of a mathematical result into physical discourse is legitimate exactly when all three tests are passed at stated cost.

## 1. Introduction

The prompt behind this paper is deliberately provocative: "Re-entry from 10.5281/zenodo.19605445: something physically real?" The phrase "re-entry" suggests that an object which began as pure mathematics — in the case of the Zenodo record 10.5281/zenodo.19605445, a "Meta-Pattern of Reification in Physics" [9] — is being proposed for return into the physical world. The companion record, "The Adelic Constraints Project — A Complete Account" [10], describes a research project that asked whether a specific piece of pure mathematics — the fact that the rational numbers can be "completed" in multiple incompatible ways, and that a single identity links all of these completions — has physical significance.

The question "is this abstraction physically real?" is usually answered by rhetoric rather than analysis. Physicists say "the field is real" when they can measure it; philosophers say "realism about $X$" when they want an argument. What is missing is a neutral, operational checklist that an adjacent-field expert can apply without committing to a metaphysical camp. This paper supplies one.

Our contribution is threefold. First, we define reification (Section 3): the act of promoting an abstract structure — a number, an identity, a constraint — to an object with causal standing in a physical theory. Second, we give three tests (instantiation, intervention, invariance) and a quantitative cost model for passing them. Third, we apply the framework to case studies grounded in the supplied bibliography, including the adelic case [10], and show explicitly where the tests pass, fail, or remain undecidable.

A note on scope and honesty: the supplied summary of [9] is empty, and the summary of [10] is truncated. We therefore treat [9] as a title-only source and [10] as supporting only the statements explicitly quoted above. All quantitative claims in this paper are derived in Section 4 with shown arithmetic or are labeled projections.

## 2. Background and Related Work

We discuss the eight supplied arXiv works and the two Zenodo records, in bibliography order.

**[1] Physics Briefing Book (arXiv:1910.11775v2).** This document describes the European Particle Physics Strategy Update (EPPSU) process, which takes a bottom-up approach: the community is first invited to submit proposals (inputs) for projects it would like to see realised in the near-term, mid-term and longer-term future, with national inputs and inputs from national laboratories as important elements. For our purposes, the EPPSU process is a large-scale institutional instance of reification: community proposals (abstract wishes) are converted into concrete facility commitments. The summary supplied gives no further detail, so we use it only as evidence that reification-by-committee is an organized, staged process with explicit time horizons.

**[2] Physics and Technology of the Next Linear Collider (arXiv:hep-ex/9605011v1).** This report presents the current expectations for the design and physics program of an $e^{+}e^{-}$ linear collider of center-of-mass energy $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$, reviews the experiments that would be carried out at the facility, demonstrates its key role in exploring physics beyond the Standard Model over the full range of theoretical possibilities, and shows the feasibility of constructing the machine. It is a canonical example of a design study reifying a future apparatus on paper: the collider is "physically real" only in the intervention-test sense of Section 3 — constructible, with a stated feasibility argument, but not yet instantiated.

**[3] JENGA (arXiv:2609.01077v1).** This work addresses safety-critical real-time systems, which must satisfy multiple dependability requirements, notably time predictability and security; tasks must complete within bounded and known execution times, typically characterised through Worst-Case Execution Time (WCET) analysis, while DRAM-based platforms are increasingly sensitive to the RowHammer read-disturbance security vulnerability. The title indicates that JENGA exploits counter-based RowHammer countermeasures to break real-time predictability. This is a case where a security countermeasure (an abstract protective policy) re-enters the physical world with a cost: it perturbs the timing predictability the system depends on. It supplies our clearest example of a reification cost that is measurable in time units.

**[4] MHD analysis on the physical designs of CFETR and HFRC (arXiv:2107.11742v1).** This paper analyzes the physical designs of the China Fusion Engineering Test Reactor (CFETR) and the Huazhong Field Reversed Configuration (HFRC), described as the two major projects representative of the low-density steady-state and high-density pulsed pathways to fusion, both under intensive physical and engineering design in China; a primary task of the physics designs is assessment and analysis (the summary truncates here). We use it as our principal case study of constraints reified into hardware: magnetohydrodynamic (MHD) stability criteria, which are mathematical conditions on plasma equilibria, act as binding design constraints on real machines.

**[5] Physical Side-Channel Attacks on Embedded Neural Networks: A Survey (arXiv:2110.11290v1).** This survey documents how Deep Neural Networks have progressively been integrated on all types of platforms, from data centers to embedded systems including low-power processors and, recently, FPGAs, and that Neural Networks are expected to become ubiquitous in IoT systems, including in safety-critical and security-sensitive domains (the summary truncates). It grounds the observation that a reified mathematical object — a trained network, a weight tensor $W \in \mathbb{R}^{m \times n}$ — acquires a physical attack surface precisely because it is instantiated in hardware.

**[6] Physics at a future Neutrino Factory and super-beam facility (arXiv:0710.4947v3).** This presents the conclusions of the Physics Working Group of the international scoping study (ISS) of a future Neutrino Factory and super-beam facility, carried by the international community between NuFact05 (the 7th International Workshop on Neutrino Factories and Superbeams, Laboratori Nazionali di Frascati, Rome, June 21–26, 2005) and NuFact06 (Irvine, California, 24–30 August 2006, per the truncated summary). Like [2], it is a paper-stage reification of a not-yet-built facility, with the added structure of a dated, community-carried scoping process.

**[7] Physics Magic (arXiv:physics/0606151v1).** This paper aims to show the magic of physics by showing the physics of magic: what makes magic tricks interesting is that something unexpected occurs, and demonstrations are interesting inasmuch as they produce something unexpected; since expectations are linked to preconceptions, a demonstration exploiting a flaw in a preconception produces an unexpected result (the summary truncates). It is directly relevant to our framing: the "surprise" of a physical demonstration is the felt signature of a failed preconception — i.e., of a reified abstraction that behaved differently from the mental model. We cite it as the pedagogical face of the intervention test.

**[8] Physically constrained eigenspace perturbation for turbulence model uncertainty estimation (arXiv:2311.01355v2).** This work notes that aerospace design increasingly incorporates Design Under Uncertainty approaches for more robust and reliable optimal designs, which require dependable estimates of uncertainty in simulations; the key contributor of predictive uncertainty in Computational Fluid Dynamics (CFD) simulations of turbulent flows is the structural limitations of Reynolds-averaged (the summary truncates, presumably Reynolds-Averaged Navier–Stokes closures, but we assert only what is written). The method of the title — physically constrained eigenspace perturbation — is exactly a disciplined reification: model-form uncertainty is represented as a perturbation of an eigenspace, but constrained so that the abstract perturbation cannot violate known physics. This is our methodological template for Section 3.

**[9] QNFO: Meta-Pattern of Reification in Physics (DOI 10.5281/zenodo.19605445).** The supplied entry gives only the title and DOI; no summary text is provided. We therefore make no claim about its content beyond what the title states: it concerns a meta-pattern of reification in physics, and it is the object whose "re-entry" the research prompt asks about.

**[10] QNFO: The Adelic Constraints Project — A Complete Account (DOI 10.5281/zenodo.20120042).** The supplied summary states that this is a complete, self-contained account of a research project conducted in May 2026, which asked whether a specific piece of pure mathematics — the fact that the rational numbers can be "completed" in multiple incompatible ways, and that a single identity links all (the summary truncates) — has some further property we cannot read. We use only the stated content: multiple incompatible completions of $\mathbb{Q}$, and a single linking identity. In adelic number theory (jargon defined: the adele ring $\mathbb{A}_{\mathbb{Q}}$ combines the real completion $\mathbb{R}$ with the $p$-adic completions $\mathbb{Q}_{p}$ for all primes $p$ into one locally compact ring), such an identity would be a product formula over all places. We do not assert the specific formula, since the summary does not state it; we treat "a single identity links all completions" as the reification candidate under test.

## 3. Methods

### 3.1 Definitions

**Definition 1 (Abstraction).** An abstraction $A$ is a mathematical or formal structure: a number, set, identity, algorithm, or constraint.

**Definition 2 (Reification).** $A$ is reified in theory $T$ if $T$ assigns $A$ a causal or constitutive role: some state $s$ of $T$'s domain satisfies $P_{A}(s)$, where $P_{A}$ is a predicate defined by $A$, and changes in $A$-relevant quantities change predictions of $T$.

**Definition 3 (Physical reality, graded).** $A$ is physically real to degree $r(A) \in \{0, 1, 2, 3\}$, defined by the three tests:

- $T_{1}$ (Instantiation): there exists an apparatus $\mathcal{A}$ whose state realizes $A$.
- $T_{2}$ (Intervention): an intervention on $\mathcal{A}$ that changes $A$ produces a detectable, predicted change in an observable $O$.
- $T_{3}$ (Invariance): the relation $A \mapsto O$ is invariant under change of apparatus, i.e., two independent apparatuses $\mathcal{A}_{1}, \mathcal{A}_{2}$ give consistent $O$ within stated tolerance.

Then $r(A) = 0$ if no test passes, $r(A) = 1$ if only $T_{1}$ passes, $r(A) = 2$ if $T_{1}, T_{2}$ pass, $r(A) = 3$ if all pass.

### 3.2 Cost model

Let $A$ be a constraint whose physical enforcement requires $n$ independent realizations (e.g., $n$ independent hardware components, $n$ repeated measurements, or $n$ independent completions in the adelic analogy). Let each realization fail to meet tolerance with probability $\epsilon$ per operational cycle, independently. The probability that at least one realization fails in a cycle is

$$p_{\mathrm{fail}}(n, \epsilon) = 1 - (1 - \epsilon)^{n}.$$

For small $\epsilon$, the first-order expansion gives

$$p_{\mathrm{fail}}(n, \epsilon) = n\epsilon - \frac{n(n-1)}{2}\epsilon^{2} + O(\epsilon^{3}),$$

so the reification cost grows linearly in $n$ at fixed $\epsilon$. Conversely, if a budget $p^{*}$ is given, the per-realization tolerance required is

$$\epsilon_{\max}(n, p^{*}) = 1 - (1 - p^{*})^{1/n}.$$

This is the quantitative core of the framework: reifying a constraint across $n$ channels multiplies the failure exposure by approximately $n$, so "physically real everywhere" is strictly more expensive than "physically real in one place."

### 3.3 Application protocol

For each case study we (i) identify $A$, (ii) identify the apparatus $\mathcal{A}$ and observable $O$, (iii) assign $r(A)$ with justification, and (iv) where numbers exist, evaluate $p_{\mathrm{fail}}$ or $\epsilon_{\max}$ with shown arithmetic.

## 4. Analysis

All inputs below are either stated in the bibliography entries or are explicitly labeled illustrative assumptions.

**Input 1 (from [2]).** The Next Linear Collider design study states a center-of-mass energy range of $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$. Converting the upper bound: $1\,\mathrm{TeV} = 1000\,\mathrm{GeV}$. The ratio of upper to lower bound is

$$\frac{E_{\max}}{E_{\min}} = \frac{1000\,\mathrm{GeV}}{500\,\mathrm{GeV}} = 2.$$

So the design space spans a factor of exactly $2$ in collision energy — a concrete, sourced number.

**Input 2 (illustrative assumption, labeled).** For the cost model, take a constraint reified across $n = 4$ independent realizations with per-realization failure probability $\epsilon = 10^{-3}$ per cycle, and a budget $p^{*} = 10^{-2}$. These values are chosen for arithmetic transparency, not measured anywhere.

*Derivation 1 (failure probability).* 

$$p_{\mathrm{fail}} = 1 - (1 - 10^{-3})^{4} = 1 - (0.999)^{4}.$$

Compute $(0.999)^{2} = 0.998001$; then $(0.999)^{4} = (0.998001)^{2} = 0.996005998001$. Hence

$$p_{\mathrm{fail}} = 1 - 0.996005998001 = 0.003994001999 \approx 3.99 \times 10^{-3}.$$

First-order check: $n\epsilon = 4 \times 10^{-3} = 4.00 \times 10^{-3}$; the exact value $3.994 \times 10^{-3}$ is below it by $6.0 \times 10^{-6}$, consistent with the quadratic correction $\frac{n(n-1)}{2}\epsilon^{2} = 6 \times 10^{-6}$.

*Derivation 2 (required tolerance).* With $p^{*} = 10^{-2}$ and $n = 4$:

$$\epsilon_{\max} = 1 - (1 - 10^{-2})^{1/4} = 1 - (0.99)^{0.25}.$$

Compute $\ln(0.99) = -0.01005034$; divided by $4$: $-0.00251258$; exponentiating: $e^{-0.00251258} = 0.99749071$. Hence

$$\epsilon_{\max} = 1 - 0.99749071 = 2.50929 \times 10^{-3} \approx 2.51 \times 10^{-3}.$$

Check: with $\epsilon = 2.50929 \times 10^{-3}$, $(1-\epsilon)^{4} = (0.99749071)^{4}$. $(0.99749071)^{2} = 0.99498749$; squared again: $0.99000062 \approx 0.99$, so $p_{\mathrm{fail}} \approx 1 - 0.99 = 10^{-2} = p^{*}$. Consistent.

*Derivation 3 (scaling law).* The ratio of exact to first-order failure probability at $n = 4$, $\epsilon = 10^{-3}$:

$$\frac{p_{\mathrm{fail}}}{n\epsilon} = \frac{3.994002 \times 10^{-3}}{4.0 \times 10^{-3}} = 0.99850.$$

So the linear approximation underestimates nothing here — it overestimates by a factor $1/0.99850 \approx 1.0015$, i.e., $0.15\%$ at these parameters. For $\epsilon \le 10^{-3}$ and $n \le 4$, the linear rule $p_{\mathrm{fail}} \approx n\epsilon$ is accurate to better than $0.2\%$.

**Input 3 (from [10], qualitative).** The Adelic Constraints Project concerns multiple incompatible completions of $\mathbb{Q}$ linked by a single identity. If the identity couples $k$ completions (one real, $k-1$ $p$-adic), the framework treats $k$ as the analogue of $n$ in Derivation 1: the "re-entry" of the identity into physics would require $k$ independent physical realizations of the completion structure, each with its own tolerance $\epsilon_{i}$. The summary does not state $k$ or any $\epsilon_{i}$, so we make no numerical claim for this case; we state only the structural mapping.

**Input 4 (from [3], qualitative with one sourced quantity class).** JENGA exploits counter-based RowHammer countermeasures to break real-time predictability. The cost of the security reification is a timing perturbation; the summary states WCET analysis characterizes bounded execution times but gives no numeric WCET, so we report the cost qualitatively: the countermeasure's reification cost is paid in the WCET budget.

## 5. Results

**R1 (Sourced).** The Next Linear Collider design study [2] spans a center-of-mass energy range from $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$, i.e., a factor of exactly $2$ (Derivation 1 of Input 1).

**R2 (Computed, illustrative parameters).** For a constraint reified across $n = 4$ independent realizations with per-realization failure probability $\epsilon = 10^{-3}$ per cycle (assumed values, not measurements), the per-cycle system failure probability is

$$p_{\mathrm{fail}} = 3.994002 \times 10^{-3} \approx 3.99 \times 10^{-3},$$

and the linear approximation $p_{\mathrm{fail}} \approx n\epsilon = 4.00 \times 10^{-3}$ is accurate to $0.15\%$ (Derivations 1 and 3).

**R3 (Computed, illustrative parameters).** To hold system failure at or below $p^{*} = 10^{-2}$ across $n = 4$ realizations, each realization requires tolerance

$$\epsilon_{\max} = 2.50929 \times 10^{-3} \approx 2.51 \times 10^{-3},$$

i.e., roughly $2.5$ times tighter than the single-channel tolerance that would give the same budget ($\epsilon_{\mathrm{single}} = 10^{-2}$). The tightening factor is

$$\frac{\epsilon_{\mathrm{single}}}{\epsilon_{\max}} = \frac{10^{-2}}{2.50929 \times 10^{-3}} = 3.985 \approx 4 - 2 \times 10^{-3}/10^{-2}\text{-scale correction},$$

more simply: $3.985$, computed as $0.01 / 0.00250929$.

**R4 (Projection, labeled).** If the adelic identity of [10] were to be tested physically across $k$ completions with equal tolerances $\epsilon$, the projected failure probability would be $p_{\mathrm{fail}} \approx k\epsilon$ for $\epsilon \le 10^{-3}$ (accuracy better than $0.2\%$ for $k \le 4$ by the same expansion verified in Derivation 3). Since [10]'s supplied summary states neither $k$ nor $\epsilon$, this is a structural projection only, with uncertainty dominated by the unknown $k$; no physical claim is made.

**R5 (Qualitative grades).** Applying the framework: the collider designs of [2] and [6] sit at $r = 1$ (paper-stage instantiation arguments, no apparatus); the fusion designs of [4] sit at $r \in \{1, 2\}$ (intensive engineering design implies intervention analysis exists, but the summary does not confirm construction); the RowHammer countermeasure of [3] sits at $r = 3$ (real DRAM platforms, measurable timing cost); embedded neural networks of [5] sit at $r = 3$ (deployed hardware with physical attack surface); the adelic identity of [10] sits at $r \le 1$ pending a proposed apparatus; the demonstrations of [7] sit at $r = 3$ for the physical effects shown, by construction of a live demonstration.

## 6. Discussion

**Limitations.** The framework's grades $r(A)$ are ordinal, not metric; two objects at $r = 3$ may differ by orders of magnitude in measurement precision. The cost model assumes independence of realizations; correlated failures (common cause, shared fabrication batch) break the factorization $(1-\epsilon)^{n}$ and would raise $p_{\mathrm{fail}}$ above our computed values. The illustrative parameters ($n = 4$, $\epsilon = 10^{-3}$, $p^{*} = 10^{-2}$) were chosen for arithmetic transparency; no measured system in the bibliography supplies these numbers, so R2 and R3 are method demonstrations, not empirical findings.

**The adelic case, argued against ourselves.** The strongest objection to our treatment of [10] is that the framework may be category-mistake-prone: a mathematical identity does not need physical instantiation to be "real" in the sense mathematicians intend, and forcing it through $T_{1}$–$T_{3}$ may be a false reification of the reification question itself. A defender of [10]'s project might respond that the identity constrains which physical theories are internally consistent — a $T_{3}$-style invariance claim at the level of theory space rather than apparatus. Our framework can express this (invariance over models, not instruments), but we have not formalized it, and doing so is open. Conversely, if no apparatus can ever be described whose observable depends on the distinction between completions of $\mathbb{Q}$, then the adelic identity's $r$-grade is permanently $0$ for physics, and the "re-entry" the prompt asks about does not occur — which would itself be a clean, falsifiable-in-spirit outcome.

**What would falsify our claims.** The claim that reification cost scales as $n\epsilon$ (R2, R3) would be falsified by a counterexample system with strongly correlated failures where measured system failure rate exceeds $n\epsilon$ substantially at small $\epsilon$; our model would then need a copula-style correction. The grading scheme would be falsified as a useful taxonomy if a clear case emerged where $T_{2}$ passes without $T_{1}$ — intervention without instantiation — which our definitions declare impossible by construction; a convincing such case would force a redesign.

**Failure modes.** The most likely misuse of this framework is grade inflation: advocates assigning $r = 2$ on the strength of a single intervention study. The EPPSU process of [1] is instructive: it stages reification through explicit community input over near-, mid-, and long-term horizons, i.e., it institutionalizes the gap between $r = 1$ and $r = 3$ rather than collapsing it.

**Open questions.** (i) Can the invariance test $T_{3}$ be given a statistical formulation (e.g., a consistency test across apparatuses with stated tolerance) that is standard enough to be applied uniformly? (ii) What is the correct cost model when realizations are partially correlated? (iii) Does the "single identity linking all completions" of [10] admit any physical observable at all, even in principle — and if the answer is no, does that diminish the mathematics? We argue it does not; the value of a result in $\mathbb{Q}$-completion theory is internal to mathematics, and the framework's $r = 0$ is a statement about physics, not about worth.

## 7. Conclusion

We converted the prompt "Re-entry from 10.5281/zenodo.19605445: something physically real?" into an operational framework: an abstraction is physically real to a graded degree determined by instantiation, intervention, and invariance tests, with a quantifiable cost of reification across $n$ channels of $p_{\mathrm{fail}} = 1 - (1-\epsilon)^{n} \approx n\epsilon$, accurate to $0.15\%$ for the parameters computed here. Applied to the supplied literature, the framework locates paper-stage collider and fusion designs at low grades, deployed hardware (RowHammer countermeasures, embedded neural networks) at the top grade with measurable costs, and the adelic identity of the Zenodo record [10] at a grade that is currently undecidable for lack of any proposed apparatus. The honest answer to the prompt is therefore conditional: something is physically real exactly when the three tests are passed and their cost is paid; mathematics re-enters physics not by declaration but by instantiation, intervention, and invariance, each with a price.

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book

[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[3] arXiv:2609.01077v1 | JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability

[4] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC

[5] arXiv:2110.11290v1 | Physical Side-Channel Attacks on Embedded Neural Networks: A Survey

[6] arXiv:0710.4947v3 | Physics at a future Neutrino Factory and super-beam facility

[7] arXiv:physics/0606151v1 | Physics Magic

[8] arXiv:2311.01355v2 | Physically constrained eigenspace perturbation for turbulence model uncertainty estimation

[9] QNFO: Meta-Pattern of Reification in Physics | DOI 10.5281/zenodo.19605445

[10] QNFO: The Adelic Constraints Project — A Complete Account | DOI 10.5281/zenodo.20120042